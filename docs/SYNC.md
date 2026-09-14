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
                               resume.html / DOCX / PDF
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
| Resume HTML / DOCX / PDF | `docs/generated/` | Printable derived artifacts regenerated from resume.txt |
| Repository About | GitHub metadata | Count + repo names, 350-char cap |

The GitHub profile README is spliced from `docs/generated/profile-merged.md` by the workflow in `devtechedge/devtechedge`.

## What it does not touch

GitHub profile bio, `docs/PATTERNS.md`, `docs/SKILL.md`, `docs/all_repos.md`, `docs/releases/*`, social preview image, contribution graph.

## Invariants

Running the workflow once or ten times must produce the same files, no duplicate rows, and no commit when nothing changed.

Merged count in `triage.json` == README badge == resume == LinkedIn == publication records. Every merged PR has a triage row, a publication record, a README row, a resume bullet, a LinkedIn bullet, and a profile entry. If one is missing, the workflow repairs it.

## Curated copy

Machine metadata (merge SHA, dates, URLs) comes from GitHub. Human-quality impact sentences live in `publications.json` with `curated: true`. Pass `--summary` on first ingest, or edit the record once. Later runs leave that prose alone.
