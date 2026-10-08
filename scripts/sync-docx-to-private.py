#!/usr/bin/env python3
"""Auto-patch jobsearch-private Devayan_Mandal.docx from oss publications.

Wraps scripts/patch-resume-docx.py. Enforces the two-page budget (Dev, 22 Sep
2026): every merged record is ranked once with rank_pairs (IMPORTANCE, then
REPO_TIER, ties newest merge first, then entry key), the top MAX_SHOWN are the
shown set, missing shown entries are added and any other bullet is removed, and
the "N shown here; K more merged" footer is rewritten from the rest. The shown
set depends only on publications.json, never on the DOCX's current bullet
order, so a second run with no new merge changes nothing (8 Oct 2026: the old
add-everything-then-trim loop re-added the dropped tail each run and the
position tiebreak flipped the shown set between runs). Also keeps the Professional Summary count
(`Merged N pull requests ...`) in step with publications.json merged_count
(Dev, 30 Sep 2026): number-only swap, wording untouched. Idempotent, writes
only when bytes change. Shown bullets are displayed in rank order, highest
first. Fails loudly on patch errors so the ledger never
silently drifts.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

MAX_SHOWN = 20


def run_patch(patch: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(patch), *args],
        capture_output=True, text=True,
    )


def load_lib(scripts_dir: Path, name: str):
    loc = scripts_dir / name
    if not loc.exists():
        sys.exit(f"sync-docx: missing render library {loc}")
    spec = importlib.util.spec_from_file_location("docx_sync_lib", loc)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser(description="Sync DOCX bullets from publications")
    ap.add_argument("--oss-root", default=".")
    ap.add_argument("--private-root", default="private")
    args = ap.parse_args()

    oss_root = Path(args.oss_root).resolve()
    priv = Path(args.private_root).resolve()
    pubs_path = oss_root / "docs" / "triage" / "publications.json"
    patch = oss_root / "scripts" / "patch-resume-docx.py"
    if not pubs_path.exists():
        sys.exit(f"sync-docx: missing {pubs_path}")
    if not patch.exists():
        sys.exit(f"sync-docx: missing {patch}")
    lib = load_lib(oss_root / "scripts", "render-resume-docx.py")
    patch_mod = load_lib(oss_root / "scripts", "patch-resume-docx.py")

    pubs = json.loads(pubs_path.read_text(encoding="utf-8"))
    # Co-authored merges live in pubs["co_authored"] and never reach the DOCX
    # or its count; the role filter is a guard in case one lands in records.
    records = [r for r in pubs.get("records", []) if (r.get("role") or "author") != "co-author"]
    merged_n = pubs.get("merged_count") or len(records)
    by_key = {}
    for rec in records:
        by_key[f"{rec.get('repo', '')} #{rec.get('number', 0)}".lower()] = rec

    chk = run_patch(patch, "--check", "--root", str(priv),
                    "--lib-dir", str(oss_root / "scripts"))
    if chk.returncode != 0:
        print(chk.stdout + chk.stderr, file=sys.stderr)
        sys.exit(f"sync-docx: --check failed: {chk.stderr.strip()[:300]}")
    try:
        existing = json.loads(chk.stdout)
    except json.JSONDecodeError:
        sys.exit(f"sync-docx: --check returned non-JSON: {chk.stdout[:300]}")
    have = {(b.get("head", "").lower(), b.get("url", "")) for b in existing.get("bullets", [])}

    # Rank every record once. Ties break newest merge first (merged_at), so
    # the shown set is a pure function of publications.json.
    stamps = {k: (rec.get("merged_at") or rec.get("merged") or "") for k, rec in by_key.items()}
    all_pairs = []
    for rec in records:
        head = f"{rec.get('repo', '')} #{rec.get('number', 0)}"
        all_pairs.append((rec.get("resume_bullet") or f"{head} - ",
                          rec.get("url", f"https://github.com/{head.replace(' #', '/pull/')}")))
    ranked = lib.rank_pairs(all_pairs, merged_at=stamps)
    shown_keys = [lib.entry_key(e) for e, _u in ranked[:MAX_SHOWN]]
    shown = set(shown_keys)

    added = unchanged = 0
    # Lowest-ranked first: --add inserts before the first bullet scoring >= the
    # new one, so adding in reverse rank order leaves equal-score adds in rank
    # order relative to each other.
    for key in reversed(shown_keys):
        rec = by_key[key]
        repo = rec.get("repo", "")
        number = rec.get("number", 0)
        url = rec.get("url", f"https://github.com/{repo}/pull/{number}")
        head = f"{repo} #{number}"
        if (head.lower(), url) in have:
            unchanged += 1
            continue
        langs = rec.get("languages") or []
        lang = langs[0] if langs else "TypeScript"
        impact = (rec.get("ledger_what") or rec.get("resume_bullet") or "").strip()
        if not impact:
            print(f"skip {head}: no impact prose", file=sys.stderr)
            continue
        r = run_patch(patch, "--add", "--root", str(priv),
                      "--lib-dir", str(oss_root / "scripts"),
                      "--head", head, "--lang", lang,
                      "--impact", impact, "--url", url)
        print((r.stdout + r.stderr).strip())
        if r.returncode != 0:
            sys.exit(f"sync-docx: --add {head} failed")
        added += 1

    print(f"sync-docx: added={added} unchanged={unchanged} shown={len(shown_keys)} total={len(records)}")

    # Remove every bullet outside the shown set (dropped by rank, or a
    # bullet whose record is gone). Hand wording of kept bullets is untouched.
    docx_path = patch_mod.find_docx(priv)
    _data, _names, _zin, doc, _rels, _raw = patch_mod.read_docx(docx_path)
    W = patch_mod.W
    present = []
    for p in doc.find(f"{{{W}}}body").iter(f"{{{W}}}p"):
        for hl in p.findall(f"{{{W}}}hyperlink"):
            head = "".join(t.text or "" for t in hl.iter(f"{{{W}}}t")).strip()
            if head and re.match(r"^\S+\s+#\d+$", head):
                present.append(head)
                break
    drop_heads = [h for h in present if h.lower() not in shown]
    for head in drop_heads:
        r = run_patch(patch, "--remove", "--root", str(priv),
                      "--lib-dir", str(oss_root / "scripts"),
                      "--head", head)
        print((r.stdout + r.stderr).strip())
        if r.returncode != 0:
            sys.exit(f"sync-docx: --remove {head} failed")

    # Footer: "20 shown here; K more merged upstream across LANGS."
    _data2, names2, zin2, doc2, rels2, raw2 = patch_mod.read_docx(docx_path)
    # Display order follows rank, highest first (8 Oct 2026, Dev approved):
    # the shown bullets are put back into the same body slots they occupy, in
    # shown_keys order, so a hand-made order in Word does not persist. Only
    # whole paragraphs move; their runs and wording are untouched.
    body2 = doc2.find(f"{{{W}}}body")
    kids = list(body2)
    slots, by_head = [], {}
    for idx, p in enumerate(kids):
        if p.tag != f"{{{W}}}p":
            continue
        for hl in p.findall(f"{{{W}}}hyperlink"):
            head = "".join(t.text or "" for t in hl.iter(f"{{{W}}}t")).strip()
            if head and re.match(r"^\S+\s+#\d+$", head):
                slots.append(idx)
                by_head[head.lower()] = p
                break
    if set(by_head) != shown:
        sys.exit("sync-docx: shown bullets do not match the ranked set, refusing to reorder")
    current = [kids[i] for i in slots]
    wanted = [by_head[k] for k in shown_keys]
    reordered = current != wanted
    for idx, p in zip(slots, wanted):
        body2[idx] = p
    print(f"sync-docx: display order by rank (reordered={reordered})")

    footer = None
    for p in doc2.find(f"{{{W}}}body").iter(f"{{{W}}}p"):
        t = "".join(x.text or "" for x in p.iter(f"{{{W}}}t"))
        if "shown here;" in t:
            footer = p
            break
    n_hidden = len(records) - min(len(records), MAX_SHOWN)
    if len(records) > MAX_SHOWN:
        langs = []
        for e, _u in ranked[MAX_SHOWN:]:
            rec = by_key.get(lib.entry_key(e))
            for lang in (rec.get("languages") or [] if rec else []):
                if lang not in langs:
                    langs.append(lang)
        lang_str = langs[0] if len(langs) == 1 else ", ".join(langs[:-1]) + " and " + langs[-1] if langs else ""
        new_footer = f"{MAX_SHOWN} shown here; {n_hidden} more merged upstream across {lang_str}."
        if footer is None:
            sys.exit("sync-docx: footer paragraph not found, refusing to invent one")
        runs = footer.findall(f"{{{W}}}r")
        if footer.findall(f"{{{W}}}hyperlink"):
            sys.exit("sync-docx: footer carries a hyperlink, refusing to rewrite")
        runs = [r for r in runs if r.find(f"{{{W}}}t") is not None]
        if not runs:
            sys.exit("sync-docx: footer has no runs")
        runs[0].find(f"{{{W}}}t").text = new_footer
        for r in runs[1:]:
            t = r.find(f"{{{W}}}t")
            if t is not None:
                t.text = ""
        print(f"sync-docx: footer -> {new_footer}")
    elif footer is not None:
        body = doc2.find(f"{{{W}}}body")
        body.remove(footer)
        print("sync-docx: footer removed (list fits)")
    summary_changed = patch_mod.set_summary_count(doc2, merged_n)
    print(f"sync-docx: summary_count -> {merged_n} (changed={summary_changed})")
    out = patch_mod.write_docx(docx_path, names2, zin2, doc2, rels2, raw2)
    print(f"sync-docx: trimmed={len(drop_heads)} footer_written={out}")

    if drop_heads:
        print("sync-docx dropped: " + "; ".join(drop_heads))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
