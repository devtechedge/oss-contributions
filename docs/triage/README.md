# Unified OSS Triage Memory

Canonical conversational gateway and operational memory for autonomous agents scanning, triaging, implementing, and tracking **all upstream OSS contributions**.

## Single source of truth

- `triage.json` is the canonical agent context for all upstream OSS contribution workflows.
- Read `triage.json` before proposing, claiming, implementing, or submitting a new target.
- Use `do_not_duplicate` and `do_not_refile` as hard exclusion signals unless new upstream information materially changes the decision.
- Re-check live GitHub state before acting because issue state, reviews, CI, mergeability, assignees, and competing work can change.
- Update `triage.json` after every meaningful outcome so future agents inherit the result.

## Unified queue

All upstream OSS work is intentionally handled through one queue and one set of selection criteria. Do not create separate domain-specific queues or ledgers.

The goal is to reduce context switching and evaluate every OSS opportunity on the same dimensions: upstream eligibility, maintainer posture, competing work, reproducibility, scope, contributor fit, validation, and merge potential.

## What `triage.json` contains

- Agent operating rules and unified selection criteria.
- Pre-flight checks and scan mechanics.
- Complete merged/open/closed contribution history from both former ledgers.
- Issue-level history and relationships to pull requests.
- Refile, duplication, raced-target, and no-go exclusions.
- Repository-level contribution history and focus areas.

This directory is operational rather than portfolio-facing. The root `README.md` remains the public unified contribution ledger.

## Publication cascade

`triage.json` remains the operational record. Curated public copy lives in `publications.json` in this directory. After an upstream merge, run the **Sync merged OSS** workflow rather than editing README, resume, LinkedIn, or the profile README by hand. Details: [`docs/SYNC.md`](../SYNC.md).
