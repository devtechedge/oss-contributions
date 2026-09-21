# Merge cascade

When an upstream PR merges, one workflow updates every publication target. Do not hand-edit the scoreboard, resume, LinkedIn source, profile README, Wellfound source, or repository About text.

Split 21 Sep 2026: public OSS targets stay in this repo. Professional docs
(resume, LinkedIn, Wellfound, paste, DOCX, all_repos) live in
`devtechedge/jobsearch-private` repo root (PII, never public).

```
GitHub merge (source of truth)
        |
docs/triage/triage.json          operational record (oss-contributions)
        |
docs/triage/publications.json    curated prose, never overwritten if curated=true
        |
   generator (scripts/sync-merged-oss.mjs --private-root private)
   |-- oss-contributions --+-- jobsearch-private (root) --+
   |                       |                              |
 README                  About/profile              resume.txt
 triage.json             (remote API)               linkedin-all-details.txt
 publications.json                                  wellfound.txt
                                                    linkedin-experience-paste.txt
                                                    Devayan_Mandal.docx (via sync-docx-to-private.py)
```

## One-click

1. Open [Sync merged OSS](https://github.com/devtechedge/oss-contributions/actions/workflows/sync-merged-oss.yml).
2. Run workflow.
3. Optional input `pr`: `owner/repo#number` (example: `pnpm/pnpm#14863`).
4. Optional input `summary`: curated one-sentence impact, used only when creating a new publication record.

The same workflow also runs hourly against PRs already tracked as `open` in `triage.json`, and accepts `repository_dispatch` type `upstream-merged`.

## What it updates

| Target | Path | Rule |
| --- | --- | --- |
| Operational ledger | `docs/triage/triage.json` (oss) | GitHub merge state, merge date, merge commit, last_checked, issue closure, repo contribution list |
| Publication copy | `docs/triage/publications.json` (oss) | Create a stub for new merged PRs. Never overwrite `curated: true` |
| Public scoreboard | `README.md` (oss) | Merged count badge, latest date, merged table (date desc) |
| Resume master | `Devayan_Mandal-resume.txt` (private root) | Count + generated merged list |
| LinkedIn master | `linkedin-all-details.txt` (private root) | Count + generated list + representative bullets |
| Experience paste | `linkedin-experience-paste.txt` (private root) | Derived from LinkedIn Experience block, markers stripped |
| Wellfound master | `wellfound.txt` (private root) | BIO 160 cap, count line, MERGED list, achievements |
| Master resume DOCX | `Devayan_Mandal.docx` (private root) | Auto-patched by `scripts/sync-docx-to-private.py` wrapping `patch-resume-docx.py`. Hand-maintained, decoupled from txt, exactly two pages, 0.4 inch margins, nothing below 10pt. Ranked by significance, not merge date |
| Repository About | GitHub metadata (oss) | Count + repo names, 340-char cap |
| Profile README | `devtechedge/devtechedge` (remote API) | In-memory fragment splice, no file on disk |

`all_repos.md` moved to private root 21 Sep 2026, human-only, never synced.

The GitHub profile README is spliced from the in-memory fragment by the workflow using `LEDGER_SYNC_TOKEN`.

## DOCX auto-patch

The node sync never renders the DOCX. The workflow step `python scripts/sync-docx-to-private.py --oss-root . --private-root private` reads `publications.json` and adds each missing merged PR via `patch-resume-docx.py --add` in `IMPORTANCE`/`REPO_TIER` order. Dev may still edit in Word freely; `patch --check` reconciles drift.

Ranking reference is `scripts/render-resume-docx.py` (`IMPORTANCE` + `REPO_TIER`). Extending `IMPORTANCE` is optional.

## What it does not touch

GitHub profile bio, `docs/PATTERNS.md`, `docs/SKILL.md`, `docs/releases/*`, social preview image, contribution graph, `all_repos.md`.

## Invariants

Running the workflow once or ten times must produce the same files, no duplicate rows, and no commit when nothing changed.

Merged count in `triage.json` == README badge == private resume == private LinkedIn == publications records. Every merged PR has a triage row, a publication record, a README row, a resume bullet, a LinkedIn bullet, a Wellfound entry, and a profile entry. If one is missing, the workflow repairs it. DOCX is validated by `patch --check`, not by count equality.

Binary targets are written only when the bytes change. DOCX zip mtimes are preserved except the two rewritten parts; `write_if_changed` stops the hourly cron committing identical binaries.

## Curated copy

Machine metadata (merge SHA, dates, URLs) comes from GitHub. Human-quality impact sentences live in `publications.json` with `curated: true`. Pass `--summary` on first ingest, or edit the record once. Later runs leave that prose alone.
