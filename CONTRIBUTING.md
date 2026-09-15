# OSS Contributions Operating Guide

## Purpose

This repository is the canonical ledger of upstream open-source contribution activity. It records worthwhile issues, contribution status, implementation and validation work, PR outcomes, and the technical impact of merged or otherwise concluded work. The goal is an **auditable record of real upstream engineering**, not simply a list of portfolio projects.

## Core Principles

1. **Upstream value first** - prioritize real bugs, regressions, compatibility problems, portability issues, missing tests, and clearly useful bounded improvements.
2. **Evidence before implementation** - understand the issue, reproduce it where practical, identify root cause, then change code.
3. **Respect upstream contributors** - check existing PRs, discussions, commits, and signs of competing work before claiming an issue.
4. **Minimal correct change** - make the smallest change that fully fixes the verified problem; avoid unrelated refactoring, formatting, or dependency changes.
5. **Technical correctness over volume** - quality, validation, and mergeability matter more than contribution count.
6. **Record outcomes honestly** - never describe work as merged, tested, or accepted unless the upstream evidence supports it.

## Contribution Priorities

### Tier 1 - High-value targeted fixes
Regressions, deterministic correctness bugs, compatibility failures, platform issues, state/data consistency problems, silent corruption, and missing regression coverage.

### Tier 2 - Meaningful bounded contributions
Scoped features, dependency compatibility, CLI/API fixes, portability improvements, parser/dialect support, documentation, typing, and substantive tests.

### Tier 3 - Selective deeper work
Larger features, architectural changes, performance redesigns, or substantial new abstractions where the scope and upstream merge path are clear.

## Standard Workflow

**Identify → Inspect → Reproduce → Diagnose → Implement → Test → Validate → Review diff → Recheck upstream → Open PR → Monitor → Update ledger**

Before coding, inspect `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, PR templates, generated-file rules, testing requirements, and relevant upstream policies. Follow the most specific applicable instructions.

Reproduce the problem first whenever practical. Prefer a regression test that fails before the fix and passes afterward. Tests should verify behavior or invariants rather than implementation details.

Validation should include the most relevant focused tests and, where practical, subsystem/full-suite tests, static checks, or differential validation. Clearly document environmental limitations.

## AI-Assisted Development

AI coding agents may perform implementation work, but they are **tools, not substitutes for engineering judgment**. Every contribution remains subject to repository instructions, scope discipline, reproducibility, testing, diff review, and upstream etiquette.

Agents should be instructed with:
- target issue and exact scope
- repository constraints
- expected behavior
- required validation
- GitHub/PR hygiene

An agent should stop rather than invent architecture or maintainer intent when requirements are ambiguous.

Do not claim human review, testing, or validation that did not occur. Check the upstream repository's policy before making any AI-related disclosure.

## GitHub / PR Hygiene

Before working, search for open and closed PRs, related issues, commits, and discussions. A contributor expressing interest may indicate competing work.

Keep one issue focused on one coherent upstream objective. PR descriptions should clearly state the problem, root cause, fix, tests, validation, and scope.

Do not equate approval with merge. Track CI, review, revisions, and the final GitHub state.

Possible ledger states include:

`candidate → selected → implementation → PR → review/CI → merged / closed / superseded / declined / abandoned`

Closed or rejected work may still represent meaningful engineering and should be recorded accurately.

## Technical Focus Areas

For concurrency or state bugs, define the invariant and create deterministic tests rather than relying on probabilistic stress loops.

For portability, identify affected OS, architecture, runtime, dependency, and toolchain assumptions.

For dependency compatibility, understand why a version constraint exists, test the proposed range, and avoid blindly removing bounds.

For parsers, compilers, or transformers, validate the full relevant path such as parse → transform → generate, including semantics or round-tripping where appropriate.

For accessibility, validate actual user-facing behavior such as DOM structure, keyboard interaction, focus behavior, and the accessibility tree.

Security-sensitive work must follow upstream disclosure requirements and must not expose sensitive details.

## Ledger Standards

For every tracked contribution, preserve useful evidence such as:

**Repository · Issue/PR · Title · Tier · Category · Status · Competition · Branch/Agent · Validation · Outcome · Technical Notes**

Distinguish clearly between:
- **Facts** - directly supported by GitHub or repository evidence.
- **Current state** - what is true now.
- **Interpretation** - analysis or assessment.

A contribution is only **merged** when GitHub confirms it as merged. Avoid misleading language such as “fixed upstream” before merge or “fully tested” without evidence.

## Stop Criteria

Stop or reconsider work when the issue is already owned, superseded, unreproducible, architecturally ambiguous, too large for the intended scope, likely to create compatibility risk, or conflicts with upstream policy.

## Final Checklist

Before submission:

**Issue understood · Competition checked · Root cause verified · Minimal fix implemented · Regression/focused tests added · Validation completed · Diff reviewed · PR prepared accurately · Ledger updated**

After merge or closure:

**Confirm final GitHub status · Record date/PR · Summarize engineering impact · Record validation/review outcome · Update ledger state**

## Guiding Philosophy

> Find a real upstream problem, prove that it exists, make the smallest technically sound change, prove that the change works, respect the upstream community, and record the result honestly.
