#!/usr/bin/env python3
"""Render resume.txt into generated DOCX and PDF. No third-party deps."""
from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


def write_if_changed(dest: Path, data: bytes) -> bool:
    """Write only when the bytes differ.

    The sync runs hourly, so an unconditional rewrite commits an identical
    binary every hour and buries real ledger changes in the history.
    """
    if dest.exists() and dest.read_bytes() == data:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return True


def load_resume(root: Path) -> str:
    return (root / "docs" / "Devayan_Mandal-resume.txt").read_text(encoding="utf-8")


def write_docx(text: str, dest: Path) -> None:
    paragraphs = []
    for raw in text.splitlines():
        line = escape(raw) if raw else ""
        if not raw:
            paragraphs.append('<w:p/>')
            continue
        size = "22"
        bold = ""
        if raw == raw.upper() and len(raw) > 3 and not raw.startswith("http"):
            size = "24"
            bold = '<w:b/>'
        if raw.startswith("DEVAYAN"):
            size = "36"
            bold = '<w:b/>'
        paragraphs.append(
            "<w:p><w:pPr><w:spacing w:after='80'/></w:pPr>"
            f"<w:r><w:rPr>{bold}<w:sz w:val='{size}'/><w:szCs w:val='{size}'/>"
            "<w:rFonts w:ascii='Calibri' w:hAnsi='Calibri'/></w:rPr>"
            f"<w:t xml:space='preserve'>{line}</w:t></w:r></w:p>"
        )
    document = (
        "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        + "".join(paragraphs)
        + "<w:sectPr><w:pgSz w:w='12240' w:h='15840'/>"
        "<w:pgMar w:top='720' w:right='720' w:bottom='720' w:left='720'/></w:sectPr>"
        "</w:body></w:document>"
    )
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""
    buf = io.BytesIO()
    # Zip entries carry an mtime. Left at "now" the archive differs on every
    # run, so write_if_changed can never see a match. Pin it to the zip epoch.
    epoch = (1980, 1, 1, 0, 0, 0)
    parts = {
        "[Content_Types].xml": content_types,
        "_rels/.rels": rels,
        "word/document.xml": document,
    }
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, payload in parts.items():
            info = zipfile.ZipInfo(name, date_time=epoch)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o600 << 16
            zf.writestr(info, payload)
    return write_if_changed(dest, buf.getvalue())


def pdf_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_pdf(text: str, dest: Path) -> None:
    lines = []
    for raw in text.splitlines():
        chunk = raw if raw else " "
        while len(chunk) > 92:
            cut = chunk.rfind(" ", 0, 92)
            if cut < 40:
                cut = 92
            lines.append(chunk[:cut])
            chunk = chunk[cut:].lstrip()
        lines.append(chunk)
    y0 = 770
    leading = 11
    page_h = 792
    pages: list[list[str]] = []
    current: list[str] = []
    y = y0
    for line in lines:
        if y < 50:
            pages.append(current)
            current = []
            y = y0
        current.append(line)
        y -= leading
    if current:
        pages.append(current)

    objects: list[bytes] = []
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{3 + i * 2} 0 R" for i in range(len(pages)))
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode())
    content_ids = []
    for page in pages:
        stream_lines = ["BT /F1 10 Tf 48 770 Td 11 TL"]
        for line in page:
            stream_lines.append(f"({pdf_escape(line)}) Tj T*")
        stream_lines.append("ET")
        stream = "\n".join(stream_lines).encode("latin-1", "replace")
        content_ids.append(len(objects) + 2)  # placeholder, fixed below
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 {page_h}] "
            f"/Resources << /Font << /F1 {3 + len(pages) * 2} 0 R >> >> /Contents {3 + len(pages) * 2 - 1} 0 R >>".encode()
        )
        objects.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")

    # Rebuild page objects with correct content ids: pages start at obj 3
    rebuilt = objects[:2]
    font_id = 3 + len(pages) * 2
    for i, page in enumerate(pages):
        content_id = 4 + i * 2
        page_id_body = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 {page_h}] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>"
        ).encode()
        stream_lines = ["BT /F1 10 Tf 48 770 Td 11 TL"]
        for line in page:
            stream_lines.append(f"({pdf_escape(line)}) Tj T*")
        stream_lines.append("ET")
        stream = "\n".join(stream_lines).encode("latin-1", "replace")
        rebuilt.append(page_id_body)
        rebuilt.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")
    rebuilt.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects = rebuilt

    out = io.BytesIO()
    out.write(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(out.tell())
        out.write(f"{i} 0 obj\n".encode())
        out.write(obj)
        out.write(b"\nendobj\n")
    xref = out.tell()
    out.write(f"xref\n0 {len(objects) + 1}\n".encode())
    out.write(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.write(f"{off:010d} 00000 n \n".encode())
    out.write(
        f"trailer << /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    return write_if_changed(dest, out.getvalue())


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    text = load_resume(root)
    generated = root / "docs" / "generated"
    docx = generated / "Devayan_Mandal-resume.docx"
    pdf = generated / "Devayan_Mandal-resume.pdf"
    docx_changed = write_docx(text, docx)
    pdf_changed = write_pdf(text, pdf)
    print(f"{'wrote' if docx_changed else 'unchanged'} {docx} ({docx.stat().st_size} bytes)")
    print(f"{'wrote' if pdf_changed else 'unchanged'} {pdf} ({pdf.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
