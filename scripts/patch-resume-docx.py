#!/usr/bin/env python3
"""Surgically maintain the OSS bullets of docs/Devayan_Mandal.docx.

The DOCX is hand-maintained and decoupled from docs/Devayan_Mandal-resume.txt
(19 Sep 2026): the sync workflow never renders or overwrites it, and Dev may
audit and edit it in Word at any time. This script is the ONLY automated
writer, run explicitly by the agent during a merge cascade or a professional
update, never by CI:

  patch-resume-docx.py --check [--root .]
  patch-resume-docx.py --add --head "owner/repo #123" --lang "Python"
      --impact "what changed, one sentence"
      --url "https://github.com/owner/repo/pull/123" [--root .]
  patch-resume-docx.py --remove --head "owner/repo #123" [--root .]

Ranking and condensing reuse scripts/render-resume-docx.py as a library
(IMPORTANCE, REPO_TIER, short_line): new bullets land in significance order and
read like the existing ones. Everything else in the file is preserved:
every zip part except word/document.xml and word/_rels/document.xml.rels
passes through byte-identical, and only touched paragraphs change inside those.

Notes:

- OSS bullets are found by PR hyperlinks (github.com/owner/repo/pull/N whose
  link text is "owner/repo #N"), not by headings, so the search survives
  hand edits that rename or move sections.
- New paragraphs clone the neighbouring bullet's formatting runs, so Word
  styling, colours and fonts carry over whatever they are. Only the texts,
  the hyperlink target and its rId are new.
- ElementTree normalises quoting inside the two rewritten parts on the first
  mutation after a Word edit. Content is unchanged and later runs are stable.
- rIds are never reused: --add takes max+1. Gaps left by --remove are valid.
- --check is read-only and never writes. Mutations write only when the bytes
  actually change.

No third-party dependencies.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import io
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
XML_SPACE = "http://www.w3.org/XML/1998/namespace"

ET.register_namespace("w", W)
ET.register_namespace("r", R)
ET.register_namespace("", REL)
for _prefix, _uri in (
    ("mc", "http://schemas.openxmlformats.org/markup-compatibility/2006"),
    ("wp", "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"),
    ("a", "http://schemas.openxmlformats.org/drawingml/2006/main"),
    ("pic", "http://schemas.openxmlformats.org/drawingml/2006/picture"),
    ("v", "urn:schemas-microsoft-com:vml"),
    ("o", "urn:schemas-microsoft-com:office:office"),
):
    ET.register_namespace(_prefix, _uri)

DOC_XML = "word/document.xml"
DOC_RELS = "word/_rels/document.xml.rels"
PULL_RE = re.compile(r"^https?://github\.com/([^/]+/[^/]+)/pull/(\d+)$")
HEAD_RE = re.compile(r"^(\S+\s+#\d+)")


def load_render_lib(scripts_dir: Path):
    loc = scripts_dir / "render-resume-docx.py"
    if not loc.exists():
        sys.exit(f"patch-resume-docx: missing render library {loc}")
    spec = importlib.util.spec_from_file_location("resume_render_lib", loc)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.iter(f"{{{W}}}t"))


def bullet_paragraphs(body, targets=None):
    """OSS bullet paragraphs: carry a PR hyperlink whose text matches its URL."""
    out = []
    for p in body.findall(f"{{{W}}}p"):
        for hl in p.findall(f"{{{W}}}hyperlink"):
            rid = hl.get(f"{{{R}}}id", "")
            head = "".join(t.text or "" for t in hl.iter(f"{{{W}}}t")).strip()
            m = HEAD_RE.match(head)
            if not (rid and m):
                continue
            if targets is not None:
                um = PULL_RE.match(targets.get(rid, ""))
                hm = re.match(r"^(\S+)\s+#(\d+)$", m.group(1))
                if not um or not hm:
                    continue
                if um.group(1).lower() != hm.group(1).lower() or um.group(2) != hm.group(2):
                    continue
            out.append((p, hl, rid, m.group(1)))
            break
    return out


def rel_targets(rels_root):
    return {
        rel.get("Id", ""): rel.get("Target", "")
        for rel in rels_root.findall(f"{{{REL}}}Relationship")
    }


def score_head(head: str, lib) -> float:
    order = {key.lower(): i for i, key in enumerate(lib.IMPORTANCE)}
    k = head.lower()
    if k in order:
        return order[k]
    m = re.match(r"^([^/]+/[^ ]+)\s+#", head)
    tier = lib.REPO_TIER.get(m.group(1).lower(), 0) if m else 0
    return lib.ENTRY_BASE + (lib.TIER_TOP - tier)


def first_run_rpr(p, inside_hyperlink: bool, position: str):
    """An rPr clone for a rebuilt run: hyperlink runs keep link styling."""
    if inside_hyperlink:
        hls = p.findall(f"{{{W}}}hyperlink")
        if hls:
            for r in hls[0].findall(f"{{{W}}}r"):
                rpr = r.find(f"{{{W}}}rPr")
                if rpr is not None:
                    return copy.deepcopy(rpr)
    runs = [r for r in p.findall(f"{{{W}}}r")]
    pool = runs if position == "first" else list(reversed(runs))
    for r in pool:
        rpr = r.find(f"{{{W}}}rPr")
        if rpr is not None:
            return copy.deepcopy(rpr)
    for r in p.iter(f"{{{W}}}r"):
        rpr = r.find(f"{{{W}}}rPr")
        if rpr is not None:
            return copy.deepcopy(rpr)
    return None


def make_run(text: str, rpr) -> object:
    r = ET.Element(f"{{{W}}}r")
    if rpr is not None:
        r.append(rpr)
    t = ET.SubElement(r, f"{{{W}}}t")
    t.set(f"{{{XML_SPACE}}}space", "preserve")
    t.text = text
    return r


def build_bullet(template_p, head: str, rest: str, rid: str):
    """A new bullet paragraph cloning the template's pPr and run styling."""
    new_p = ET.Element(f"{{{W}}}p")
    ppr = template_p.find(f"{{{W}}}pPr")
    if ppr is not None:
        new_p.append(copy.deepcopy(ppr))
    new_p.append(make_run("\u2022 ", first_run_rpr(template_p, False, "first")))
    hl = ET.SubElement(new_p, f"{{{W}}}hyperlink")
    hl.set(f"{{{R}}}id", rid)
    hl.set(f"{{{W}}}history", "1")
    hl.append(make_run(head, first_run_rpr(template_p, True, "first")))
    new_p.append(make_run(rest, first_run_rpr(template_p, False, "last")))
    return new_p


def rebuild_paragraph(p, head: str, rest: str):
    """Replace a bullet's runs, preserving its pPr and hyperlink rId."""
    bullet_rpr = first_run_rpr(p, False, "first")
    link_rpr = first_run_rpr(p, True, "first")
    rest_rpr = first_run_rpr(p, False, "last")
    hls = p.findall(f"{{{W}}}hyperlink")
    hl = hls[0] if hls else None
    old_rid = hl.get(f"{{{R}}}id", "") if hl is not None else ""
    for c in [c for c in list(p) if c.tag in (f"{{{W}}}r", f"{{{W}}}hyperlink")]:
        p.remove(c)
    p.append(make_run("\u2022 ", bullet_rpr))
    if hl is None:
        hl = ET.Element(f"{{{W}}}hyperlink")
        hl.set(f"{{{W}}}history", "1")
    else:
        for r in list(hl):
            hl.remove(r)
        if old_rid:
            hl.set(f"{{{R}}}id", old_rid)
    hl.append(make_run(head, link_rpr))
    # Runs are appended after the hyperlink so document order stays stable.
    p.append(hl)
    p.append(make_run(rest, rest_rpr))


def read_docx(path: Path):
    data = path.read_bytes()
    zin = zipfile.ZipFile(io.BytesIO(data))
    names = zin.namelist()
    doc = ET.fromstring(zin.read(DOC_XML))
    try:
        rels = ET.fromstring(zin.read(DOC_RELS))
    except KeyError:
        rels = ET.Element(
            f"{{{REL}}}Relationships",
            {"xmlns": REL},
        )
    return data, names, zin, doc, rels


def write_docx(path: Path, names, zin, doc, rels):
    out = io.BytesIO()
    payloads = {
        DOC_XML: ET.tostring(doc, encoding="utf-8", xml_declaration=True),
        DOC_RELS: ET.tostring(rels, encoding="utf-8", xml_declaration=True),
    }
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in names:
            if name in payloads:
                info = zin.getinfo(name)
                zf.writestr(info, payloads.pop(name))
            else:
                zf.writestr(zin.getinfo(name), zin.read(name))
        for name, blob in payloads.items():
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o600 << 16
            zf.writestr(info, blob)
    blob = out.getvalue()
    if blob == path.read_bytes():
        return False
    path.write_bytes(blob)
    return True


def cmd_check(doc, rels):
    body = doc.find(f"{{{W}}}body")
    targets = rel_targets(rels)
    bullets = [
        {"head": head, "url": targets.get(rid, ""), "text": para_text(p)}
        for p, _hl, rid, head in bullet_paragraphs(body, targets)
    ]
    print(json.dumps({"count": len(bullets), "bullets": bullets}, indent=2))
    return 0


def cmd_add(args, doc, rels, lib):
    entry = f"{args.head} ({args.lang}) - {args.impact.strip().rstrip('.')}"
    condensed = lib.short_line(entry)
    head, _lang, _impact = lib.split_entry(condensed)
    if not head or not condensed.startswith(head):
        sys.exit("patch-resume-docx: condensed bullet lost its head, refusing")
    rest = condensed[len(head):]
    m = PULL_RE.match(args.url.strip())
    if not m:
        sys.exit("patch-resume-docx: --url must be https://github.com/owner/repo/pull/N")
    url_repo = m.group(1)
    hm = re.match(r"^(\S+)\s+#\d+$", head)
    if not hm or hm.group(1).lower() != url_repo.lower():
        sys.exit("patch-resume-docx: --head repo does not match --url repo, refusing")

    body = doc.find(f"{{{W}}}body")
    targets = rel_targets(rels)
    bullets = bullet_paragraphs(body, targets)
    if not bullets:
        sys.exit("patch-resume-docx: no OSS bullets found, refusing")
    for p, _hl, rid, h in bullets:
        if h.lower() == head.lower() and targets.get(rid, "") == args.url.strip():
            if para_text(p).replace("\u2022 ", "", 1) == condensed:
                print(f"unchanged {head} (already present)")
                return 0
            # Same PR, revised wording: rebuild runs around the existing rId.
            rebuild_paragraph(p, head, rest)
            print(f"updated {head} (same link)")
            return 1

    new_score = score_head(head, lib)
    ref_p, ref_hl = None, None
    for p, hl, rid, h in bullets:
        if score_head(h, lib) >= new_score:
            ref_p, ref_hl = p, hl
            break
    template_p = ref_p if ref_p is not None else bullets[-1][0]
    existing = [int(r[3:]) for r in targets if re.fullmatch(r"rId\d+", r)]
    rid = f"rId{(max(existing) if existing else 0) + 1}"
    new_p = build_bullet(template_p, head, rest, rid)
    kids = list(body)
    if ref_p is not None:
        body.insert(kids.index(ref_p), new_p)
    else:
        body.insert(kids.index(bullets[-1][0]) + 1, new_p)
    rel = ET.SubElement(rels, f"{{{REL}}}Relationship")
    rel.set("Id", rid)
    rel.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink")
    rel.set("Target", args.url.strip())
    rel.set("TargetMode", "External")
    print(f"added {head} -> {rid}")
    return 1


def cmd_remove(args, doc, rels):
    body = doc.find(f"{{{W}}}body")
    targets = rel_targets(rels)
    removed = None
    for p, _hl, rid, h in bullet_paragraphs(body, targets):
        if h.lower() == args.head.strip().lower():
            kids = list(body)
            body.remove(p)
            for rel in rels.findall(f"{{{REL}}}Relationship"):
                if rel.get("Id") == rid:
                    rels.remove(rel)
            removed = (h, targets.get(rid, ""))
            break
    if removed is None:
        print(f"unchanged {args.head} (not present)")
        return 0
    print(f"removed {removed[0]} (was {removed[1]})")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Surgically maintain DOCX OSS bullets")
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--add", action="store_true")
    ap.add_argument("--remove", action="store_true")
    ap.add_argument("--head", default="")
    ap.add_argument("--lang", default="")
    ap.add_argument("--impact", default="")
    ap.add_argument("--url", default="")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    docx = root / "docs" / "Devayan_Mandal.docx"
    if not docx.exists():
        sys.exit(f"patch-resume-docx: missing {docx}")
    lib = load_render_lib(root / "scripts")

    data, names, zin, doc, rels = read_docx(docx)
    try:
        if args.check:
            return cmd_check(doc, rels)
        if args.add:
            if not (args.head and args.lang and args.impact and args.url):
                sys.exit("patch-resume-docx: --add needs --head, --lang, --impact, --url")
            dirty = cmd_add(args, doc, rels, lib)
        elif args.remove:
            if not args.head:
                sys.exit("patch-resume-docx: --remove needs --head")
            dirty = cmd_remove(args, doc, rels)
        else:
            sys.exit("patch-resume-docx: pass --check, --add or --remove")
        if not dirty:
            return 0
        changed = write_docx(docx, names, zin, doc, rels)
        print("wrote" if changed else "unchanged", docx)
        return 0
    finally:
        zin.close()


if __name__ == "__main__":
    raise SystemExit(main())
