#!/usr/bin/env python3
"""Sync the master resume DOCX with the generated resume text.

Source of truth: docs/Devayan_Mandal-resume.txt, which the ledger workflow
rewrites on every merge. This script splices two things out of it and into the
hand-formatted DOCX at docs/Devayan_Mandal.docx:

  1. The "Merged N upstream pull requests across ... in ..." sentence inside
     the professional summary paragraph. Only that sentence is replaced, so
     hand-edited wording elsewhere in the summary survives.
  2. The whole body of the open-source contributions section: the intro line,
     one bullet per merged PR, the spacer, and the closing line.

Formatting is preserved by cloning the XML of the paragraphs already in the
file and swapping their text, rather than rebuilding the document. Nothing
outside those two places is touched, and the file is rewritten only when the
resulting document.xml actually differs, so an unchanged run leaves the DOCX
byte-identical and produces no commit.

No third-party dependencies: stdlib zipfile, re, io, copy.
"""
from __future__ import annotations

import copy
import io
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

DOC_PART = "word/document.xml"
START = "<<<LEDGER:MERGED_LIST>>>"
END = "<<<END:LEDGER:MERGED_LIST>>>"

# Heading text is matched loosely: "OPEN-SOURCE", "Open source" and a renamed
# section all still resolve to the same place.
HEADING_KEY = "OPENSOURCECONTRIBUTION"
BULLET = "\u2022 "
SUMMARY_SENTENCE = re.compile(r"Merged \d+ upstream pull requests across .*? in [^.]+\.")
SUMMARY_COUNT = re.compile(r"Merged \d+ upstream pull requests")
TRAILING_URL = re.compile(r"\s+(?:https?://)?(?:www\.)?github\.com/\S+\s*$")


def fail(message: str) -> "NoReturn":  # type: ignore[valid-type]
    print(f"render-resume-docx: {message}", file=sys.stderr)
    raise SystemExit(1)


# --------------------------------------------------------------------------- resume.txt


def parse_resume(text: str) -> dict:
    lines = text.splitlines()

    entries: list[str] = []
    if START in text and END in text:
        block = text.split(START, 1)[1].split(END, 1)[0]
        for raw in block.splitlines():
            line = raw.strip()
            if line.startswith("- "):
                line = line[2:].strip()
                if line:
                    entries.append(line)
    if not entries:
        fail(f"no merged entries found between {START} and {END} in the resume text")

    # Intro line sits immediately before the start marker, closing line is the
    # first non-empty line after the end marker.
    before = text.split(START, 1)[0].splitlines()
    label = next((l.strip() for l in reversed(before) if l.strip()), "Merged upstream:")

    after = text.split(END, 1)[1].splitlines()
    closing = ""
    for line in after:
        line = line.strip()
        if not line:
            continue
        # Guard against picking up the next all-caps section heading.
        if line == line.upper() and len(line) < 40:
            break
        closing = line
        break

    summary = ""
    for i, line in enumerate(lines):
        if line.strip().upper() == "PROFESSIONAL SUMMARY":
            summary = next((l.strip() for l in lines[i + 1:] if l.strip()), "")
            break

    return {
        "entries": entries,
        "label": label,
        "closing": closing,
        "summary": summary,
        "count": len(entries),
    }


def bullet_text(entry: str) -> str:
    """Resume bullets carry a trailing PR URL; the DOCX never has."""
    return BULLET + TRAILING_URL.sub("", entry).strip()


# --------------------------------------------------------------------------- document.xml


def split_blocks(body: str) -> list[str]:
    """Split a body into top-level runs of paragraphs, tables and loose nodes."""
    blocks: list[str] = []
    i, n = 0, len(body)
    empty = re.compile(r"<(w:p|w:tbl)(?:\s[^>]*)?/>")
    opener = re.compile(r"<(w:p|w:tbl)(?:\s[^>]*)?>")
    while i < n:
        m = empty.match(body, i)
        if m:
            blocks.append(body[i:m.end()])
            i = m.end()
            continue
        m = opener.match(body, i)
        if m:
            tag = m.group(1)
            close = body.find(f"</{tag}>", i)
            if close == -1:
                fail(f"malformed document.xml: unclosed <{tag}>")
            end = close + len(tag) + 3
            blocks.append(body[i:end])
            i = end
            continue
        nxt = re.compile(r"<(?:w:p|w:tbl)[ />]").search(body, i)
        j = nxt.start() if nxt else n
        blocks.append(body[i:j])
        i = j
    return blocks


def block_text(block: str) -> str:
    parts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", block, re.S)
    return "".join(parts).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def block_style(block: str) -> str:
    m = re.search(r'w:pStyle w:val="([^"]+)"', block)
    return m.group(1) if m else ""


def is_heading(block: str) -> bool:
    return block_style(block).lower().startswith("heading")


def norm(text: str) -> str:
    return re.sub(r"[^A-Z]", "", text.upper())


RUN = re.compile(r"<w:r(?:\s[^>]*)?>.*?</w:r>", re.S)


def set_text(block: str, text: str, seed: int) -> str:
    """Return a copy of `block` whose visible text is exactly `text`."""
    body = escape(text)
    runs = RUN.findall(block)
    if runs:
        first = runs[0]
        if "<w:t" in first:
            replaced = re.sub(
                r"(<w:t[^>]*>).*?(</w:t>)",
                lambda m: m.group(1) + body + m.group(2),
                first,
                count=1,
                flags=re.S,
            )
        else:
            replaced = first.replace("</w:r>", f"<w:t xml:space='preserve'>{body}</w:t></w:r>")
        out = block.replace(first, replaced, 1)
        for extra in runs[1:]:
            out = out.replace(extra, "", 1)
    elif "</w:p>" in block:
        out = block.replace(
            "</w:p>", f"<w:r><w:t xml:space='preserve'>{body}</w:t></w:r></w:p>"
        )
    else:
        fail(f"cannot place text in block: {block[:120]}")
    return fresh_ids(out, seed)


def fresh_ids(block: str, seed: int) -> str:
    """Word wants unique w14:paraId values; keep them deterministic per run."""
    pid = f"{seed:08X}"
    out = re.sub(r'w14:paraId="[^"]*"', f'w14:paraId="{pid}"', block)
    out = re.sub(r'w14:textId="[^"]*"', f'w14:textId="77777777"', out)
    return out


def find_summary(blocks: list[str]) -> int:
    """The summary paragraph, not the tagline under the name.

    Both start with "Full Stack AI Native", so prefer the one that actually
    carries the merged-count sentence, and require real paragraph length.
    """
    for i, b in enumerate(blocks):
        t = block_text(b)
        if len(t) > 200 and "upstream pull requests" in t:
            return i
    for i, b in enumerate(blocks):
        t = block_text(b)
        if len(t) > 200 and t.startswith("Full Stack AI Native"):
            return i
    return -1


def find_section(blocks: list[str]) -> tuple[int, int]:
    start = -1
    for i, b in enumerate(blocks):
        if is_heading(b) and HEADING_KEY in norm(block_text(b)):
            start = i
            break
    if start == -1:
        return -1, -1
    for j in range(start + 1, len(blocks)):
        if is_heading(blocks[j]):
            return start, j
    return start, len(blocks)


# --------------------------------------------------------------------------- driver


def update_document(xml: str, data: dict) -> str:
    head, sep, after = xml.partition("<w:body>")
    body, marker, rest = after.partition("</w:body>")
    if not sep or not marker:
        fail("document.xml has no w:body")

    blocks = split_blocks(body)
    changed = False

    # 1. Summary sentence.
    si = find_summary(blocks)
    if si == -1:
        print("render-resume-docx: summary paragraph not found; count left as is")
    else:
        text = block_text(blocks[si])
        sentence = SUMMARY_SENTENCE.search(data["summary"])
        if sentence:
            new_text, hits = SUMMARY_SENTENCE.subn(
                lambda _: sentence.group(0), text, count=1
            )
        else:
            new_text, hits = SUMMARY_COUNT.subn(
                f"Merged {data['count']} upstream pull requests", text, count=1
            )
        if hits and new_text != text:
            blocks[si] = set_text(blocks[si], new_text, 1000 + si)
            changed = True

    # 2. Open-source contributions section.
    start, end = find_section(blocks)
    if start == -1:
        fail("could not find the open-source contributions heading in the DOCX")
    section = blocks[start + 1:end]

    label_tpl = next((b for b in section if block_text(b) == data["label"]), None)
    bullet_tpl = next((b for b in section if block_text(b).startswith(BULLET.strip())), None)
    spacer_tpl = next((b for b in section if not block_text(b)), None)
    closing_tpl = next((b for b in section if block_text(b).startswith("Active upstream")), None)
    if bullet_tpl is None:
        bullet_tpl = next((b for b in section if block_text(b)), None)
    if bullet_tpl is None:
        fail("the contributions section has no paragraph to clone formatting from")

    new_section: list[str] = []
    new_section.append(set_text(label_tpl or bullet_tpl, data["label"], 2000))
    for i, entry in enumerate(data["entries"]):
        new_section.append(set_text(bullet_tpl, bullet_text(entry), 3000 + i))
    if data["closing"]:
        new_section.append(set_text(spacer_tpl or bullet_tpl, "", 2500))
        new_section.append(set_text(closing_tpl or bullet_tpl, data["closing"], 2600))

    if new_section != section:
        blocks[start + 1:end] = new_section
        changed = True

    if not changed:
        return xml
    return head + "<w:body>" + "".join(blocks) + "</w:body>" + rest


def rewrite_docx(path: Path, new_xml: str) -> None:
    with zipfile.ZipFile(path) as zin:
        infos = zin.infolist()
        payload = {zi.filename: zin.read(zi.filename) for zi in infos}
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zout:
        for zi in infos:
            data = new_xml.encode("utf-8") if zi.filename == DOC_PART else payload[zi.filename]
            zout.writestr(copy.copy(zi), data)
    path.write_bytes(buf.getvalue())


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    resume_txt = root / "docs" / "Devayan_Mandal-resume.txt"
    docx = root / "docs" / "Devayan_Mandal.docx"

    if not resume_txt.exists():
        fail(f"missing {resume_txt}")
    if not docx.exists():
        fail(f"missing {docx}")

    data = parse_resume(resume_txt.read_text(encoding="utf-8"))
    with zipfile.ZipFile(docx) as zin:
        if DOC_PART not in zin.namelist():
            fail(f"{docx} has no {DOC_PART}")
        old_xml = zin.read(DOC_PART).decode("utf-8")

    new_xml = update_document(old_xml, data)
    if new_xml == old_xml:
        print(f"unchanged {docx}")
        return 0

    rewrite_docx(docx, new_xml)
    print(f"wrote {docx} ({docx.stat().st_size} bytes, {data['count']} merged entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
