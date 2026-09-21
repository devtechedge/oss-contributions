#!/usr/bin/env python3
"""Auto-patch jobsearch-private Devayan_Mandal.docx from oss publications.

Wraps scripts/patch-resume-docx.py: for every merged publication record missing
from the DOCX, adds it in IMPORTANCE significance order. Idempotent, writes
only when bytes change. Fails loudly on patch errors so the ledger never
silently drifts from the DOCX.
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_patch(patch: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(patch), *args],
        capture_output=True, text=True,
    )


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

    pubs = json.loads(pubs_path.read_text(encoding="utf-8"))
    records = pubs.get("records", [])

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
