---
name: oss
description: Use when scanning, claiming, opening, or tracker-updating upstream OSS PRs, or when editing the user's own unified OSS ledger (README, badges, About). Covers serial shipping, shared voice, comment approval, commit signing, and ledger upkeep.
---

# OSS PR Playbook

One playbook for contributing pull requests to upstream open-source repositories. Work is handled through one unified OSS ledger and one operational queue covering all upstream projects. Never split a PR or scoreboard row by domain. Apply on every new PR unless the user overrides that turn.

Core goals, in priority order:

1. Quality over quantity: small, uncontested, mergeable fixes
2. A credible human voice with maintainers
3. One well-run PR at a time beats a spray of contested ones

Learned patterns (scan triage, implementation gotchas, repo-specific no-gos) live in `PATTERNS.md` next to this file. Read it during scans and before implementing. Every pattern there is a lesson from a past PR or scan: re-verify it against current repo state, never assume it still holds.

## 1. Unified OSS workflow

| | **Unified OSS ledger** |
| --- | --- |
| Scope | All upstream OSS work, including TS/JS/Python/Rust libraries, tooling, infrastructure, wallets, SDKs, blockchain software, frameworks, testing, concurrency, portability, security, and accessibility |
| Ledger | `oss-contributions` |
| Ledger writes | Update after every open, merge, no-go, closure, or other meaningful attempt outcome, same turn |
| Targeting | Rank all candidates together using the same eligibility, fit, scope, maintainer, freshness, validation, and merge-potential criteria |
| Account | The user's OSS account, typically `@devtechedge` |

Upstream PR work is recorded on the unified ledger repo. The README lists merged pull requests only; open, closed, no-go, and all other attempt state lives in docs/triage/triage.json. Work in the user's own repositories is never listed on the ledger.

## 2. Permissions and approvals

- Act (comment, open PRs, request review) only as the authorized OSS account. Never post as any other account.
- Never comment, open a PR, or request review without permission in that turn, or a batch authorization covering those exact targets. A batch such as "open N uncontested PRs" covers uncontested in-scope targets only: no contested pile-ons, no tracker edits unless named.
- **Comment approval gate:** always ask before posting any PR comment, issue reply, or review: show the full text to the user as a draft and wait for explicit approval of that exact text, every time, no exceptions. A general go-ahead such as "work on this" authorizes the work, not the post; the draft still needs its own approval in the turn it would be posted. Post the approved text verbatim.
- Commit signing: check the repository's contribution policy and sign commits accordingly (DCO `Signed-off-by` trailer and/or cryptographic GPG/SSH signature) before pushing. See section 6 for the passphrase-hang failure mode.

## 3. Voice (non-negotiable)

- Professional, respectful, and concise. Lead with what changed and why; no performative filler.
- Never use em dashes in maintainer-facing text. Use a normal hyphen `-` or split the sentence.
- Never use emojis in PR comments, issue replies, reviews, or any maintainer-facing text. Plain text only, no exceptions (no 🙏, 👍, 🎉, etc.). This rule governs upstream interaction only - the user's own ledger README deliberately uses emojis and logos.
- Keep comments short-paragraphed: one to two sentences per paragraph with a blank line between them. No wall-of-text blocks in issues, PRs, or reviews.
- Prefer `Fixes #N` / `Closes #N` when the change fully resolves the issue.
- Informal tone is reserved for private chat with the user; all public text follows this section.
- Enforcement: a local PreToolUse hook (`~/.zcode/hooks/voice-gate.mjs`, registered in `~/.zcode/cli/config.json`) hard-blocks any `gh pr comment` / `gh issue comment` tool call whose inline body contains emojis or em/en dashes. If it fires, strip the offending characters and retry; never bypass or work around it. Inline `--body` text is checked; bodies passed via `--body-file` are not, so apply the same rules manually there.

## 4. Cadence and API hygiene

1. Open one new PR at a time. A second may run only with explicit user permission. Complete the full cycle per PR - claim, implement, test, open, ledger update - before hunting the next target. Follow-up pushes to an existing open PR (human review, actionable bot P1) are fine while the next hunt is queued.
2. Run one agent session per PR lifecycle (hunt, ship) and retire it once the PR is open, the ledger is updated, and the post-run retrospective (section 8) is done. No session stays open to watch the PR: the user gets GitHub email notifications for maintainer activity and relays what needs action. The SKILL.md playbook and tracker files carry the persistent state, so every fresh session stays small and bounded. Use long-running threads only for meta-discussion, never for PR work.
3. Keep GitHub API volume low; GitHub support warned the account about request volume (Sep 2026). One consolidated call over several narrow ones, reuse data already fetched instead of refetching, no `--paginate` on large collections, no parallel API fan-out, and poll at most every 60 seconds while waiting on CI. Check `gh api rate_limit` before heavy scans and stop well before the limit.
4. On `resource_exhausted`: stop parallel work, wait, then resume serially. If GitHub is the blocker, check `gh api rate_limit` separately. Do not thrash retries.
5. Stuck handling: if a step stays blocked for a long time - a hung command, a command that never returns, repeated identical failures, a wait that outlives any plausible runtime - assume something on the other end has failed: a dropped connection, a missing password, passphrase, or key, or a tool waiting on input that will never come. Stop hitting the wall. Report what is blocked and the evidence, then either move on to other queued work and revisit the blocker later, or ask the user a clarification question if only they can unblock it (credentials, auth, interactive prompts). Do not burn the session looping on one blocking step.

## 5. Target selection and GO criteria

A target is GO only when every item below holds. Re-check the timeline with `gh` immediately before claiming.

Hard gates:

- Open issue, no owning assignee, no competing open fix PR. Check the issue **timeline's** `cross-referenced` events for linked PRs, not just the body and comments - fresh bugs can have competing PRs before any triage comment lands (0 comments is not a clear field).
- No prior closed-unmerged PR on the same issue, or a clear reason why the earlier approach failed and the new one differs.
- The fix is owned by the repo being targeted; confirm companion packages (e.g. a `fastapi-users` bug may live in `fastapi-users-db-sqlalchemy`) before claiming.
- Reproducible or source-verifiable on the current default branch, and not already fixed on main even if the issue is still open.
- Bounded patch: small file count, plus tests where the repo has them.
- Outside contributions allowed: the repo must accept PRs from external contributors outright. If its CONTRIBUTING.md (or observed maintainer behavior) reserves PRs for maintainer-invited contributors - "open a PR only when a maintainer invites you", "help wanted" + approved approach, members-only, etc. - the repo is off-limits until such an invite exists on a specific issue. Do not code first and hope; leave at the scan stage.
- Submission path open (verify before any heavy implementation work - 13 Sep 2026 casey/just lesson): the maintainer or issue author may have blocked the account, or applied hard filters (PRs disabled repo-wide, collaborator-only PRs, interaction limits) that silently stop PR creation and comments, while reads, forking, and pushing to the fork still succeed. These restrictions fail with misleading REST 404 / GraphQL FORBIDDEN on PR creation and do not appear in CONTRIBUTING.md. Before the heavy lifting: search the repo for "pull requests are disabled" issues and maintainer statements about PRs or AI contributions, and confirm the repo still merges outside authors (`author_association` OWNER/MEMBER on all recent merged PRs means the repo is effectively maintainer-only). Also read the repo's `.github/workflows/` for auto-close or claim-enforcement bots (13 Sep 2026 pydantic-ai lesson): a bot that closes PRs whose linked issue is unassigned to the PR author defeats every pre-open probe - fork push and even PR creation succeed - so issues that will never be assigned (bot-filed sweep issues) are not claimable; check how issues in the repo ever get assigned before investing. Then probe: as soon as the core fix compiles, push a working branch to the fork and attempt actual PR creation. 404/FORBIDDEN on creation means the submission path is closed - stop, record the no-go in triage, preserve the branch, and report. Do not polish tests, run full suites, or draft PR copy for a PR that cannot be opened.
- Stellar org default no-go: stellar/* repos are no-go unless an explicit maintainer invite exists on that specific issue. Only exception: stellar/stellar-docs, whose CONTRIBUTING.md accepts direct outside PRs for small fixes (typos, broken links, copy corrections) without an invite - re-verify its policy each cycle before relying on the exception. stellar/js-stellar-sdk remains invite-gated.
- Contribution policy satisfied: CLA, signed commits, required labels, repo accepting PRs.
- No design or policy gate pending. If semantics need maintainer agreement, comment the proposed approach and wait. Never code through the gate.

Freshness and aliveness:

- Repo is alive: pushed within the last ~3 months (`pushed_at`, not just `archived`). Uncontested issues in dormant repos (fuels-ts, alchemy-sdk-js, create-solana-program) are not targets.
- Issue is recent: opened within the past few days or the last few weeks (rough rule: 6 weeks or less). Treat age as a first-pass filter at discovery time (sort by newest), not a late check - months- or years-old issues are routinely closed on triage or already fixed.

Sizing and tilt:

- Always skip: contested issues, archived repositories, vague features needing design, and repeat AgentScan auto-close targets from the same account on the same issue.
- Repo size: aim for small and mid-size repos; mega-repos are last-resort even when a target looks clean on paper. When two repos offer a comparable fix, pick the smaller one.
- Prefer reputable mid-size projects and bounded fixes. Avoid crowded maintainer-only cores, repeated outsider closes, and invasive changes without maintainer direction.
- Saturation cap: before adding a target from a repo, count the open PRs the account already has there. 1: fine. 2-3: only exceptional fixes. 4+: skip that repo for the cycle and hunt in fresh repos. Current per-repo counts are recorded in the canonical triage tracker.

Scan mechanics (when asked to scan for N targets):

- Run read-only scan agents in parallel over disjoint repo groups; if the harness rejects parallel agents, retry one at a time. Each agent verifies per candidate: no assignee, no maintainer claim in comments, no cross-referenced or open PR (issue `timeline` plus PR keyword search), repo pushed recently. Agents never post anything.
- Bulk issue discovery uses the core `repos/{owner}/{repo}/issues?labels=bug` endpoint, not the search API: the search endpoint trips its secondary rate limit after ~2 rapid calls and kills the sweep; the core endpoint does not. Follow up with one `issues/{n}/timeline` call per shortlisted candidate for cross-referenced PRs.
- **Raced-target rule:** if the issue timeline or keyword search reveals a competing open PR for the same issue/behavior, immediately classify the candidate as **contested/raced**, stop evaluating it for GO, and move to the next candidate. Do not spend additional implementation effort, policy analysis, or deep testing on a raced target unless the competing PR later closes or upstream state materially changes.
- **Persistent tracker rule for raced targets:** when a raced/contested target is discovered, record it in the canonical `docs/triage/triage.json` in the existing format with the issue, related competing PR number(s), current status, verification date, and `do_not_duplicate: true`. This prevents future scans from rediscovering and re-evaluating the same race. Update the triage record if the competing PR closes, merges, or the issue changes materially.
- A `cross-referenced` event pointing at a foreign repo (issue numbers out of range for the repo, PR fetch returns 404) is noise, not an open competitor.
- Every scan re-verifies the existing candidate queue before adding new names. Candidates go stale in predictable ways: fixed on main, repo went dormant, a maintainer steered the design in comments (semi-contested, follow their stated direction exactly or skip), or a linked PR appeared. Stamp every candidate row with its verification date.
- A `Potential AI issue` label on an issue we claimed means maintainers are filtering AI-authored reports; any follow-up there must be extra precise and human.

## 6. Shipping steps

1. Default to fork, branch, and PR via `gh` when Cloud Agents are unavailable.
2. Probe the submission path before the heavy implementation work (see the submission-path hard gate in section 5): confirm the maintainer has not blocked the account and the repo has no hard filter (PRs disabled repo-wide, collaborator-only PRs, interaction limits) that would stop committing or PR/issue comments. Cheap checks first - search the repo for "pull requests are disabled" issues, check recent merged PRs for outside authors - then the definitive probe: push the working branch early and attempt PR creation once the fix compiles. A 404/FORBIDDEN on creation means stop: record the no-go, keep the branch, report. Never discover this after the full test-and-polish cycle (casey/just #3227).
3. Minimal root-cause fix matching repo style. No drive-by refactors.
4. Add a focused regression that fails before and passes after, when tests exist.
5. Add a changeset when the repo uses changesets.
6. Use distinct branch names when multiple PRs target the same repo.
7. Sign commits per repo policy (DCO and/or cryptographic signature) before pushing. DCO sign-off (`-s`) needs no key; a passphrase-protected GPG/SSH key hangs background commits - if the hang happens, either retry with `-c commit.gpgsign=false` where the repo policy and history accept unsigned commits (own ledger repos), or prepare the branch and hand it to the user to sign and push (upstream repos requiring signatures). Only the user can enter the passphrase.
8. Fix actionable bot review findings on your own code (e.g. Greptile P1) on the same branch. Ignore noise.
9. Leave non-actionable checks alone: Vercel "authorize deploy", team-only checks, and first-contribution `action_required` workflow approvals.
10. All GitHub Actions and CI checks must be green before a PR is reported done. After each push, wait for checks to settle and confirm every check passes (or is non-actionable per step 9). A red check caused by your own change is actionable: read the failed job log, fix, push, confirm green. Never report a PR as done without confirming its checks passed; when a maintainer must manually approve the workflow run (`action_required`), say so explicitly instead of claiming green.
11. Report the PR URL, plus the scoreboard when batching.

## 7. Maintainer responses (user-driven; no babysitting)

No babysitting: never set up a watch, cron job, event listener, or polling loop on a PR, old or new. GitHub already emails the user for every maintainer review, comment, and merge, and that email is the trigger. Standing watches burn background tokens for signal the user already has.

- When the user relays PR activity (an email, a comment, a review), act on it then: read the current PR state once, and treat bots as no-ops - CodeRabbit, Greptile, Copilot, Vercel, Changeset, Dependabot, Qodo, github-actions, CLA assistant, and `*[bot]` accounts generally. A bot comment may be worth surfacing to the user, but never act on it.
- Act only on human maintainer or collaborator responses: if a safe fix is clear, push it to the same branch while the change stays within the PR's scope, and reply in the approved voice through the comment approval gate.
- "Please sign your commit" asks (e.g. Safe repos): check `gh api repos/OWNER/REPO/pulls/N/commits` for `.commit.verification`. If `verified: true` with reason `valid`, the ask is already satisfied; update the ledger status and wait for merge, no reply needed. If not signed, only the user can re-sign locally with their key; the agent prepares the branch, the user signs and pushes.
- Auto-close: if a PR is auto-closed shortly after opening, mark it Closed (not merged) when writing the ledger, never refile that issue from the same account, and never reply to the auto-close bot. Prefer quieter mid-size repositories when auto-closes keep happening.

## 8. Post-run retrospective (mandatory before retiring a PR session)

Every PR run ends with a retrospective when the session's active work is done - after the PR is opened and the ledger updated, or on a no-go, a closure the user reports, or an abandonment (see section 4.2). Do not skip it on a bad outcome; a closed PR that yields no learned pattern is a wasted run.

1. Revisit the full run end to end: the scan/claim decision, the gates you checked, the implementation, test and lint loop, the submission path, PR copy, and the terminal outcome. Walk the actual commands and outputs, not your memory of the plan.
2. Extract what generalized. A finding is worth recording when it would change behavior on a future PR in a different repo, not just this one: a new hard gate, a repo-policy surprise that dodged the existing checks, a toolchain or typechecker pitfall, a faster fail-before loop, a repo convention worth mirroring. Anything repo-specific and point-in-time goes to the triage tracker instead.
3. Write the findings the same turn:
   - Generalizable lessons go to `PATTERNS.md` (next to this file), under the matching heading (scan-time, implementation, or a new one), written as a caution a fresh session can apply without this run's context.
   - If a lesson invalidates or tightens a hard gate in section 5 or a shipping step in section 6, edit this SKILL.md too - the gate text should name the failure mode it encodes.
   - Repo-specific facts (no-gos, saturation, gate evidence, branch names worth preserving) go to the canonical `docs/triage/triage.json` in the ledger repo, never to PATTERNS.md.
   - Keep entries terse and dated where rot is possible; every pattern is a hypothesis to re-verify, not a permanent truth.
4. Sync the ledger mirrors: after editing SKILL.md or PATTERNS.md, push the updated copies to `docs/SKILL.md` / `docs/PATTERNS.md` in `oss-contributions` (see section 10) so portable agent context stays accurate.
5. Only then retire the session. The next PR run starts from the updated playbook.

## 9. Email triage (OSS inbox)

- Confirm with the user whether flagged mail is actionable before acting.
- CLA emails: the user signs in the browser. Confirm only after the `license/cla` check succeeds. A passing recheck alone does not sign.
- Keep: human approvals, reviews, merges, security alerts, anything from real people.
- Discard or ignore: bot-only noise such as Copilot, Vercel authorize, Changeset, CodeRabbit, Qodo "paused for this user" notices (usually the repository's Qodo plan, not a GitHub ban), surveys, and sales.
- Use the correct existing Gmail labels for the OSS accounts. Never invent vague labels.

## 10. Ledger and own-repo writes

The user's own unified ledger repo is `oss-contributions`; its README is the public product. Everything in this section lands on GitHub in the same turn it is decided - never leave such changes unwritten, and pushing needs no separate confirmation.

**How to write:** prefer direct GitHub CLI/API writes (`gh api` contents PUT / edit endpoints) for spot edits - do not clone-edit-push when a direct write does the same job faster. The user pulls via GitHub Desktop when needed. For whole-file transformations (styling sweeps across every table row), a scripted local rewrite is acceptable: `git pull --ff-only` first, re-read the file after any fetch, push the same turn, and rebase on origin if the push is rejected.

**Skill mirror:** the canonical playbook is `~/.agents/skills/oss/SKILL.md` plus its companion `PATTERNS.md`; never edit the copies in the ledger repo directly. The ledger repo carries mirrors at `docs/SKILL.md` and `docs/PATTERNS.md`, which exist for portable agent context.

## 11. Unified ledger schema discipline

- Canonical triage memory is `docs/triage/triage.json`.
- Keep all records in the same arrays and schema. Do not create separate domain-specific queue files.
- Preserve existing field names and conventions. Update only affected records and keep dates/state accurate.
- Historical portfolio documents are informational and must not override canonical triage state.
