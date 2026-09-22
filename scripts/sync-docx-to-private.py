#!/usr/bin/env python3
"""Auto-patch jobsearch-private Devayan_Mandal.docx from oss publications.

Wraps scripts/patch-resume-docx.py: for every merged publication record missing
from the DOCX, adds it in IMPORTANCE significance order. Then enforces the
two-page budget (Dev, 22 Sep 2026): the OSS list holds at most MAX_SHOWN
entries by rank_pairs order, and the "N shown here; K more merged" footer is
rewritten from the dropped set. Idempotent, writes only when bytes change.
Fails loudly on patch errors so the ledger never silently drifts.
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
    records = pubs.get("records", [])
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

    added = unchanged = 0
    for rec in sorted(records, key=lambda r: (r.get("repo", ""), r.get("number", 0))):
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

    print(f"sync-docx: added={added} unchanged={unchanged} total={len(records)}")

    # Two-page budget: cap the list at MAX_SHOWN by rank order, refresh footer.
    docx_path = patch_mod.find_docx(priv)
    _data, _names, _zin, doc, _rels, _raw = patch_mod.read_docx(docx_path)
    W = patch_mod.W
    bullets = []
    for p in doc.find(f"{{{W}}}body").iter(f"{{{W}}}p"):
        for hl in p.findall(f"{{{W}}}hyperlink"):
            head = "".join(t.text or "" for t in hl.iter(f"{{{W}}}t")).strip()
            if head and re.match(r"^\S+\s+#\d+$", head):
                text = "".join(t.text or "" for t in p.iter(f"{{{W}}}t"))
                bullets.append((p, head))
                break
    pairs = []
    for p, head in bullets:
        rec = by_key.get(head.lower())
        entry = rec.get("resume_bullet", f"{head} - ") if rec else f"{head} - "
        pairs.append((entry, rec.get("url", "") if rec else ""))
    ranked = lib.rank_pairs(pairs)
    # map back to heads via entry keys (heads are already "repo #num" form)
    key_to_head = {}
    for p, head in bullets:
        key_to_head[head.lower()] = head
    drop_heads = [key_to_head.get(lib.entry_key(e)) for e, _u in ranked[MAX_SHOWN:]]
    for head in drop_heads:
        if head is None:
            sys.exit("sync-docx: trim could not map a ranked entry to a bullet")
        r = run_patch(patch, "--remove", "--root", str(priv),
                      "--lib-dir", str(oss_root / "scripts"),
                      "--head", head)
        print((r.stdout + r.stderr).strip())
        if r.returncode != 0:
            sys.exit(f"sync-docx: --remove {head} failed")

    # Footer: "20 shown here; K more merged upstream across LANGS."
    _data2, names2, zin2, doc2, rels2, raw2 = patch_mod.read_docx(docx_path)
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
    out = patch_mod.write_docx(docx_path, names2, zin2, doc2, rels2, raw2)
    print(f"sync-docx: trimmed={len(drop_heads)} footer_written={out}")

    if drop_heads:
        print("sync-docx dropped: " + "; ".join(drop_heads))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
