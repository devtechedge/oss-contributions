#!/usr/bin/env python3
"""Render docs/Devayan_Mandal.docx from the ledger resume text.

Source of truth is docs/Devayan_Mandal-resume.txt, which the ledger workflow
rewrites on every merge. This script renders it to a DOCX that meets three
fixed requirements:

  * exactly two pages on US Letter
  * 0.4 inch margins on all four sides
  * no run set below 10pt

Because the page budget is fixed, the open-source section is re-summarised on
every run rather than pasted verbatim. The renderer tries the full bullet text
first, then condensed one-liners, then a shortened subset plus a roll-up line,
and stops at the first variant that fits the remaining space. If the hand
written sections leave no room at all, they are condensed too, cheapest first:
certifications to a single line, then small skill categories folded together,
then long experience bullets trimmed at clause boundaries.

Text is measured with real Calibri advance widths baked into _WIDTHS, so no
font engine is needed and the result does not depend on what CI has installed.
The file is rewritten only when the bytes actually change, so a no-op sync
still commits nothing.

No third-party dependencies.
"""
from __future__ import annotations

import io
import math
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

# --------------------------------------------------------------------- page box

PAGE_W = 12240  # twips, US Letter
PAGE_H = 15840
MARGIN = 576  # 0.4 inch

NAME_PT = 16.0
HEAD_PT = 10.5
BODY_PT = 10.0
MIN_PT = 10.0

LINE = 1.2207  # Calibri single-line height as a fraction of the point size
PACK = 0.96  # lines never fill edge to edge; be slightly pessimistic

# The file is written with MARGIN on all four sides and Word honours it. Some
# previewers substitute their own margins and report an extra page for any
# document, including the two-page original this replaced. That is a property
# of the viewer, not something to design the content around; RENDER_SAFETY is
# the whole allowance. Do not measure against a pessimistic page box: doing so
# costs roughly twenty percent of the content for no gain in the real target.
USABLE_W = (PAGE_W - 2 * MARGIN) / 20.0  # points
USABLE_H = (PAGE_H - 2 * MARGIN) / 20.0
BUDGET = 2 * USABLE_H  # two pages, in points

BULLET_INDENT = 180  # twips

# Advance widths in 1/1000 em for chr(32), chr(33..126), U+2022, U+2013,
# U+2019, U+00A0, read out of calibri.ttf.
_ORDER = [32] + list(range(33, 127)) + [0x2022, 0x2013, 0x2019, 0x00A0]
_WIDTHS = [
    226, 326, 401, 498, 507, 715, 682, 221, 303, 303, 498, 498, 250, 306, 252, 386,
    507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 268, 268, 498, 498, 498, 463,
    894, 579, 544, 533, 615, 488, 459, 631, 623, 252, 319, 520, 420, 855, 646, 662,
    517, 673, 543, 459, 487, 642, 567, 890, 519, 487, 468, 307, 386, 307, 498, 498,
    291, 479, 525, 423, 525, 498, 305, 471, 525, 229, 239, 455, 229, 799, 525, 527,
    525, 525, 349, 391, 335, 525, 452, 715, 433, 453, 395, 314, 460, 314, 498, 498,
    498, 250, 226,
]
_CAL = dict(zip(_ORDER, _WIDTHS))
_FALLBACK = 500

BULLET = "\u2022"
START = "<<<LEDGER:MERGED_LIST>>>"
END = "<<<END:LEDGER:MERGED_LIST>>>"
URL_TAIL = re.compile(r"\s+(?:https?://)?(?:www\.)?github\.com/\S+\s*$")
MERGED_TAIL = re.compile(r"\s*Merged\s+[A-Z][a-z]{2}\s+\d{4}\.\s*$")

SECTIONS = (
    "PROFESSIONAL SUMMARY",
    "TECHNICAL SKILLS",
    "PROFESSIONAL EXPERIENCE",
    "OPEN SOURCE CONTRIBUTIONS",
    "CERTIFICATIONS",
    "EDUCATION",
)


def em(text: str) -> float:
    return sum(_CAL.get(ord(ch), _FALLBACK) for ch in text) / 1000.0


def lines_for(text: str, size: float, width: float) -> int:
    if not text:
        return 1
    return max(1, int(math.ceil(em(text) * size / (width * PACK))))


# --------------------------------------------------------------------- blocks


class Block:
    __slots__ = ("text", "size", "bold", "kind", "before", "after")

    def __init__(self, text, size=BODY_PT, bold=False, kind="body", before=0.0, after=0.0):
        self.text = text
        self.size = size
        self.bold = bold
        self.kind = kind
        self.before = before
        self.after = after

    def height(self) -> float:
        size = max(self.size, MIN_PT)
        if self.kind == "bullet":
            usable = USABLE_W - BULLET_INDENT / 20.0
        else:
            usable = USABLE_W
        n = lines_for(self.text, size, usable)
        return (self.before + n * size * LINE + self.after) * RENDER_SAFETY


def total_height(blocks) -> float:
    return sum(b.height() for b in blocks)


# --------------------------------------------------------------------- resume.txt


def parse_resume(text: str) -> dict:
    lines = text.splitlines()

    name = lines[0].strip() if lines else ""
    tagline = lines[1].strip() if len(lines) > 1 else ""
    contact = []
    for line in lines[2:]:
        if not line.strip():
            break
        if line.strip() in SECTIONS:
            break
        contact.append(line.strip())
        if len(contact) >= 3:
            break

    sections: dict[str, list[str]] = {}
    current = None
    for line in lines:
        s = line.strip()
        if s in SECTIONS:
            current = s
            sections[current] = []
            continue
        if current and s:
            sections[current].append(s)

    entries: list[str] = []
    if START in text and END in text:
        block = text.split(START, 1)[1].split(END, 1)[0]
        for raw in block.splitlines():
            s = raw.strip()
            if s.startswith("- "):
                s = URL_TAIL.sub("", s[2:].strip()).strip()
                if s:
                    entries.append(s)

    intro = "Merged upstream:"
    after = text.split(END, 1)[1].splitlines() if END in text else []
    closing = ""
    for line in after:
        s = line.strip()
        if not s:
            continue
        if s == s.upper() and len(s) < 40:
            break
        closing = s
        break

    return {
        "name": name,
        "tagline": tagline,
        "contact": " | ".join(contact),
        "sections": sections,
        "entries": entries,
        "intro": intro,
        "closing": closing,
    }


# --------------------------------------------------------------------- condensing


def first_clause(text: str) -> str:
    """The leading claim of an impact sentence, before any qualification."""
    body = MERGED_TAIL.sub("", text).strip().rstrip(".")
    for sep in ("; ", ". "):
        if sep in body:
            head = body.split(sep, 1)[0].strip()
            if len(head) >= 40:
                return head
    return body


TAIL_WORDS = {
    "a", "an", "the", "and", "or", "but", "with", "to", "of", "in", "on", "for",
    "by", "from", "as", "at", "into", "that", "which", "are", "is", "was", "were",
    "be", "been", "being", "now", "also", "plus", "including", "other", "more",
    "its", "their", "when", "while", "than", "then", "so", "not", "no", "any",
    "before", "after", "during", "until", "upon", "against", "between", "among",
    "via", "using", "use", "across", "within", "without", "through", "about",
    "over", "under", "per", "toward", "towards", "along", "behind", "beyond",
}


def finish(text: str) -> str:
    """Close a trimmed line so it reads as a finished sentence."""
    text = text.rstrip(" ,;:.")
    if text.count("(") > text.count(")"):
        pos = text.rfind("(")
        if pos > 0:
            text = text[:pos].rstrip(" ,;:.")
    # A sentence cannot end on a function word; back off until it can.
    while len(text) > 25:
        tail = text.rsplit(" ", 1)[-1].strip(" ,;:.").lower()
        if tail in TAIL_WORDS:
            text = text.rsplit(" ", 1)[0].rstrip(" ,;:.")
        else:
            break
    return text + "."


def clip(text: str, limit: int) -> str:
    """Shorten to `limit`, preferring a clause boundary so the line still reads
    as a finished sentence rather than a severed one."""
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for sep in ("; ", ", "):
        pos = cut.rfind(sep)
        if pos > limit * 0.55:
            cand = text[:pos]
            # Never end on a dangling fragment such as ", and AAROP".
            tail_at = cand.rfind(", ")
            if tail_at > 0 and re.match(
                r"(?i)^(and|or|but|with|including|plus)\b", cand[tail_at + 2:].strip()
            ):
                cand = cand[:tail_at]
            return finish(cand)
    pos = cut.rfind(" ")
    if pos > limit * 0.6:
        cut = cut[:pos]
    return finish(cut)

LIVE_TAIL = re.compile(r"\sLive:\s[^.]*\.?$")


def shorten_prose(text: str, cap) -> str:
    """Trim a hand-written bullet to `cap` characters without mangling it.

    Whole trailing sentences go first, so the bullet still reads as a complete
    thought. A trailing "Live: demo.url" is re-attached because it is the one
    part of a portfolio bullet that a reader can act on.
    """
    if not cap or len(text) <= cap:
        return text
    live = ""
    lm = LIVE_TAIL.search(text)
    if lm:
        live = " " + lm.group(0).strip()
    body = text[:lm.start()] if lm else text
    budget = max(70, cap - len(live))

    parts = re.split(r"(?<=[.!?])\s+", body)
    out = parts[0]
    dropped = False
    for part in parts[1:]:
        if len(out) + 1 + len(part) <= budget:
            out += " " + part
        else:
            dropped = True
            break
    if len(out) > budget:
        # A single sentence longer than the cap still has to be cut.
        out = clip(out, budget)
    elif dropped and not out.endswith((".", "!", "?")):
        out += "..."
    return (out + live).strip()


# Condensation ladder, cheapest and least lossy first. The renderer walks it
# until the fixed sections leave a real open-source section room to breathe.
LEVELS = (
    (False, False, None),
    (True, False, None),
    (True, True, None),
    (True, True, 340),
    (True, True, 300),
    (True, True, 265),
    (True, True, 235),
    (True, True, 210),
    (True, True, 190),
    (True, True, 170),
    (True, True, 150),
)

# Small skill categories folded into their neighbour, dropping the prefix.
SKILL_MERGE = {
    "Realtime & Observability": "Backend & Data",
    "Practices": "Cloud & DevOps",
}

# Everything is measured as if it were this much larger before it is compared
# to the budget, which keeps a little slack for readers that substitute a wider
# font for Calibri or apply their own line spacing. Calibrated in Word: 1.00
# fills two pages, and Word's own PDF export agrees at 1.06.
#
# Keep this small. At 1.12 the open-source section fell from five repositories
# to three, and the slack buys nothing against viewers that add a page to every
# document regardless of content.
RENDER_SAFETY = 1.06

TARGET_FILL = 0.95  # 0.98 fits, 1.00 tips to three pages, so leave headroom
GOAL = BUDGET * TARGET_FILL
MIN_OSS = 130.0  # heading + intro + a handful of bullets + closing


def full_line(entry: str) -> str:
    return entry


def split_entry(entry: str):
    """(repo#number, language, impact) from a ledger resume bullet."""
    m = re.match(r"^(\S+\s+#\d+)\s+\(([^)]+)\)\s+-\s+(.*)$", entry)
    if m:
        return m.group(1), m.group(2), m.group(3)
    m = re.match(r"^(\S+\s+#\d+)\s+-\s+(.*)$", entry)
    if m:
        return m.group(1), None, m.group(2)
    return None, None, entry


def condensed_line(entry: str, limit: int = 150) -> str:
    """`limit` caps the whole rendered line, prefix included."""
    head, lang, impact = split_entry(entry)
    if head and lang:
        prefix = f"{head} ({lang}) - "
    elif head:
        prefix = f"{head} - "
    else:
        prefix = ""
    text = clip(first_clause(impact), max(50, limit - len(prefix)))
    return prefix + text


def short_line(entry: str) -> str:
    # Still long enough to end on a full clause. Cutting below about 110
    # characters forces mid-clause truncation, which reads badly on a resume.
    return condensed_line(entry, 145)


def repo_name(entry: str) -> str:
    m = re.match(r"^([^/]+/[^ ]+)\s+#", entry)
    return m.group(1) if m else entry.split()[0]


def rollup(items) -> str:
    names = []
    for e in items:
        n = repo_name(e)
        if n not in names:
            names.append(n)
    head = names[:2]
    extra = len(names) - len(head)
    shown = ", ".join(head)
    if extra > 0:
        shown = f"{shown} and {extra} other {'repository' if extra == 1 else 'repositories'}"
    return f"+{len(items)} more merged upstream PRs across {shown}."


# --------------------------------------------------------------------- layout


def build_fixed(data: dict, level=(False, False, None)) -> list[Block]:
    certs_compact, skills_merge, exp_cap = level
    out: list[Block] = []

    out.append(Block(data["name"], NAME_PT, True, "body", 0, 1))
    if data["tagline"]:
        out.append(Block(data["tagline"], BODY_PT, False, "body", 0, 1))
    if data["contact"]:
        out.append(Block(data["contact"], BODY_PT, False, "body", 0, 8))

    order = [s for s in SECTIONS if s in data["sections"]]
    for name in order:
        if name == "OPEN SOURCE CONTRIBUTIONS":
            continue
        out.append(Block(name, HEAD_PT, True, "heading", 8, 2))
        lines = list(data["sections"][name])

        if name == "TECHNICAL SKILLS" and skills_merge:
            lines = merge_skills(lines)
        if name == "CERTIFICATIONS" and certs_compact:
            items = [l[2:].strip().rstrip(".") for l in lines if l.startswith("- ")]
            if items:
                out.append(Block(BULLET + " " + "; ".join(items), BODY_PT, False, "bullet", 0, 1))
            continue

        for line in lines:
            if line.startswith("- "):
                text = line[2:].strip()
                if name == "PROFESSIONAL EXPERIENCE":
                    text = shorten_prose(text, exp_cap)
                out.append(Block(BULLET + " " + text, BODY_PT, False, "bullet", 0, 1))
            elif name == "PROFESSIONAL EXPERIENCE":
                if line == line.upper() and len(line) > 6:
                    out.append(Block(line, BODY_PT, True, "body", 4, 0))
                else:
                    out.append(Block(line, BODY_PT, False, "body", 0, 1))
            elif name == "EDUCATION" and line == line.upper() and len(line) > 6:
                out.append(Block(line, BODY_PT, True, "body", 4, 0))
            else:
                out.append(Block(line, BODY_PT, False, "body", 0, 2))
    return out


def merge_skills(lines: list[str]) -> list[str]:
    merged: dict[str, str] = {}
    order: list[str] = []
    for line in lines:
        if ": " not in line:
            order.append(line)
            merged[line] = line
            continue
        cat, rest = line.split(": ", 1)
        target = SKILL_MERGE.get(cat)
        if target and target in merged:
            merged[target] = f"{merged[target]}; {rest}"
            continue
        order.append(cat)
        merged[cat] = line
    return [merged.get(k, k) for k in order]


def oss_blocks(data: dict, lines: list[str]) -> list[Block]:
    out = [Block("OPEN SOURCE CONTRIBUTIONS", HEAD_PT, True, "heading", 8, 2)]
    if data["intro"]:
        out.append(Block(data["intro"], BODY_PT, False, "body", 0, 1))
    for line in lines:
        out.append(Block(BULLET + " " + line, BODY_PT, False, "bullet", 0, 1))
    if data["closing"]:
        out.append(Block(data["closing"], BODY_PT, False, "body", 2, 0))
    return out


def distinct_repos(entries):
    """Newest first, but at most one entry per repository.

    Two pages cannot hold nineteen bullets, and five merges in one repo read as
    padding next to five merges across five projects.
    """
    seen = set()
    out = []
    for e in entries:
        key = repo_name(e)
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


def fit_oss(data: dict, remaining: float):
    """Pick the richest open-source rendering that still fits `remaining`."""
    entries = data["entries"]
    if not entries:
        return []

    def height(lines):
        return total_height(oss_blocks(data, lines))

    for build in (full_line, condensed_line):
        lines = [build(e) for e in entries]
        if height(lines) <= remaining:
            return lines

    # Space is tight, so prefer showing more repositories tersely over fewer
    # at length: the portfolio breadth is the point on a two-page resume.
    picked = distinct_repos(entries)
    best = None
    for rank, build in enumerate((condensed_line, short_line)):
        for k in range(len(picked), 0, -1):
            shown = picked[:k]
            rest = [e for e in entries if e not in shown]
            lines = [build(e) for e in shown]
            if rest:
                lines.append(rollup(rest))
            if height(lines) <= remaining:
                if best is None or (k, -rank) > (best[0], -best[1]):
                    best = (k, rank, lines)
                break
    if best:
        return best[2]

    shown = picked[:1]
    return [short_line(shown[0]), rollup([e for e in entries if e != shown[0]])]


# --------------------------------------------------------------------- xml


def run(text: str, size: float, bold: bool) -> str:
    size = max(size, MIN_PT)
    half = int(round(size * 2))
    props = (
        f"<w:rPr>{'<w:b/>' if bold else ''}"
        f"<w:sz w:val='{half}'/><w:szCs w:val='{half}'/></w:rPr>"
    )
    return f"<w:r>{props}<w:t xml:space='preserve'>{escape(text)}</w:t></w:r>"


def paragraph(block: Block) -> str:
    size = max(block.size, MIN_PT)
    half = int(round(size * 2))
    before = int(round(block.before * 20))
    after = int(round(block.after * 20))
    spacing = (
        f"<w:spacing w:before='{before}' w:after='{after}' "
        f"w:line='240' w:lineRule='auto'/>"
    )
    ind = ""
    if block.kind == "bullet":
        ind = f"<w:ind w:left='{BULLET_INDENT}' w:hanging='{BULLET_INDENT}'/>"
    bdr = ""
    if block.kind == "heading":
        bdr = "<w:pBdr><w:bottom w:val='single' w:sz='6' w:space='1' w:color='666666'/></w:pBdr>"
    ppr = (
        f"<w:pPr>{spacing}{ind}{bdr}"
        f"<w:rPr><w:sz w:val='{half}'/><w:szCs w:val='{half}'/></w:rPr></w:pPr>"
    )
    return f"<w:p>{ppr}{run(block.text, size, block.bold)}</w:p>"


S_DEFAULTS = (
    "<w:docDefaults><w:rPrDefault><w:rPr>"
    "<w:rFonts w:ascii='Calibri' w:hAnsi='Calibri' w:cs='Calibri'/>"
    "<w:sz w:val='20'/><w:szCs w:val='20'/>"
    "</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>"
    "<w:spacing w:after='0' w:line='240' w:lineRule='auto'/>"
    "</w:pPr></w:pPrDefault></w:docDefaults>"
)


def build_document(blocks) -> str:
    body = "".join(paragraph(b) for b in blocks)
    sect = (
        f"<w:sectPr><w:pgSz w:w='{PAGE_W}' w:h='{PAGE_H}'/>"
        f"<w:pgMar w:top='{MARGIN}' w:right='{MARGIN}' w:bottom='{MARGIN}' "
        f"w:left='{MARGIN}' w:header='432' w:footer='432' w:gutter='0'/>"
        f"<w:cols w:space='720'/><w:docGrid w:linePitch='360'/></w:sectPr>"
    )
    return (
        "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}{sect}</w:body></w:document>"
    )


STYLES = (
    "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
    '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    + S_DEFAULTS
    + "</w:styles>"
)

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="word/styles.xml"/>
</Relationships>
"""

EPOCH = (1980, 1, 1, 0, 0, 0)


def pack(parts) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, payload in parts.items():
            info = zipfile.ZipInfo(name, date_time=EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o600 << 16
            zf.writestr(info, payload)
    return buf.getvalue()


# --------------------------------------------------------------------- driver


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    resume_txt = root / "docs" / "Devayan_Mandal-resume.txt"
    dest = root / "docs" / "Devayan_Mandal.docx"

    if not resume_txt.exists():
        print(f"render-resume-docx: missing {resume_txt}", file=sys.stderr)
        return 1

    data = parse_resume(resume_txt.read_text(encoding="utf-8"))
    if not data["entries"]:
        print("render-resume-docx: no merged entries found", file=sys.stderr)
        return 1

    fixed = None
    level = LEVELS[-1]
    for candidate_level in LEVELS:
        candidate = build_fixed(data, candidate_level)
        if total_height(candidate) + MIN_OSS <= GOAL:
            fixed, level = candidate, candidate_level
            break
    if fixed is None:
        ranked = sorted(
            ((total_height(build_fixed(data, lv)), i) for i, lv in enumerate(LEVELS))
        )
        level = LEVELS[ranked[0][1]]
        fixed = build_fixed(data, level)
        print(
            "::warning::master resume DOCX: content does not fit two pages even at "
            "the deepest condensation; trim docs/Devayan_Mandal-resume.txt",
            file=sys.stderr,
        )

    remaining = GOAL - total_height(fixed)
    lines = fit_oss(data, remaining)
    blocks = fixed + oss_blocks(data, lines)
    print(
        f"condensation: certs_compact={level[0]} skills_merge={level[1]} "
        f"experience_cap={level[2]}"
    )

    height = total_height(blocks)
    print(
        f"layout: {len(blocks)} blocks, {height:.0f}pt of {BUDGET:.0f}pt "
        f"({height / USABLE_H:.2f} pages), {len(data['entries'])} merged entries, "
        f"{len(lines)} published"
    )

    blob = pack({
        "[Content_Types].xml": CONTENT_TYPES,
        "_rels/.rels": RELS,
        "word/document.xml": build_document(blocks),
        "word/styles.xml": STYLES,
    })

    if dest.exists() and dest.read_bytes() == blob:
        print(f"unchanged {dest}")
        return 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(blob)
    print(f"wrote {dest} ({len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
