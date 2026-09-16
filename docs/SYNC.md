# Merge cascade

When an upstream PR merges, one workflow updates every publication target. Do not hand-edit the scoreboard, resume, LinkedIn source, profile README, or repository About text.

```
GitHub merge (source of truth)
        ↓
docs/triage/triage.json          operational record
        ↓
docs/triage/publications.json    curated prose (never overwritten if curated=true)
        ↓
   generator (scripts/sync-merged-oss.mjs)
 ┌──────┼──────────┬──────────────┬──────────────────┐
 ↓      ↓          ↓              ↓                  ↓
README  resume.txt LinkedIn src   profile fragment   About description
                       ↓
           ┌──────────┴───────────┐
           ↓                      ↓
     master resume DOCX    docs/generated
  (docs/Devayan_Mandal.docx)  html / DOCX / PDF
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
| Operational ledger | `docs/triage/triage.json` | GitHub merge state, merge date, merge commit, last_checked, issue closure, repo contribution list |
| Publication copy | `docs/triage/publications.json` | Create a stub for new merged PRs. Never overwrite `curated: true` |
| Public scoreboard | `README.md` | Merged count badge, latest date, merged table (date desc) |
| Resume master | `docs/Devayan_Mandal-resume.txt` | Count + generated merged list |
| LinkedIn master | `docs/linkedin-all-details.txt` | Count + generated list + representative bullets |
| Profile fragment | `docs/generated/profile-merged.md` | Alphabetical by repo, PR number ascending |
| Master resume DOCX | `docs/Devayan_Mandal.docx` | Rendered from resume.txt by `scripts/render-resume-docx.py`. Fixed rules: exactly two pages, 0.4 inch margins, nothing below 10pt |
| Resume HTML / DOCX / PDF | `docs/generated/` | Printable derived artifacts regenerated from resume.txt |
| Repository About | GitHub metadata | Count + repo names, 350-char cap |

The GitHub profile README is spliced from `docs/generated/profile-merged.md` by the workflow in `devtechedge/devtechedge`.

## The two-page rule

`docs/Devayan_Mandal.docx` is not spliced, it is rendered. `docs/Devayan_Mandal-resume.txt` is the master, so edit the text file, never the DOCX.

Every run the renderer measures the content with real Calibri metrics and fits it to a two-page budget:

1. The open-source section is the shock absorber. It tries full bullets, then condensed one-liners, then a subset plus a `+N more merged upstream PRs across ...` roll-up line.
2. Only if the hand-written sections still leave no room are they condensed, cheapest first: certifications to one line, small skill categories folded together, then long experience bullets trimmed at clause boundaries.
3. Everything is measured as if it were 12% larger before it is compared to the budget (`RENDER_SAFETY`). Word paginates the result at two pages, but viewers that substitute a wider font for Calibri, or apply their own line spacing, need that room or they spill onto a third page.
4. It then targets 95% of the budget. Calibration against Word: 0.98 fits, 1.00 spills to three pages, so the last 5% is the error margin.

Font sizes: name 16pt, section headings 10.5pt bold, body 10pt. Margins are 0.4 inch on all four sides.

## What it does not touch

GitHub profile bio, `docs/PATTERNS.md`, `docs/SKILL.md`, `docs/all_repos.md`, `docs/releases/*`, social preview image, contribution graph.

## Invariants

Running the workflow once or ten times must produce the same files, no duplicate rows, and no commit when nothing changed.

Merged count in `triage.json` == README badge == resume == LinkedIn == master DOCX == publication records. Every merged PR has a triage row, a publication record, a README row, a resume bullet, a LinkedIn bullet, and a profile entry. If one is missing, the workflow repairs it.

Binary targets are written only when the bytes change. A zip entry's mtime differs on every run, so `render-resume-artifacts.py` pins it to the zip epoch; without that the hourly cron commits an identical DOCX every hour.

## Curated copy

Machine metadata (merge SHA, dates, URLs) comes from GitHub. Human-quality impact sentences live in `publications.json` with `curated: true`. Pass `--summary` on first ingest, or edit the record once. Later runs leave that prose alone.
