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

Learned patterns (scan triage, implementation gotchas, repo-specific no-gos) live in `PATTERNS.md` next to this file, or in `references/PATTERNS.md` when this skill is packaged for Grok. Read it during scans and before implementing. Every pattern there is a lesson from a past PR or scan: re-verify it against current repo state, never assume it still holds.

## 0. Canonical location and cross-platform sync

This playbook is used from several agent platforms (WorkBuddy, grok.com, zcode, Codex/ChatGPT). Only one copy counts, and it lives in the ledger repo:

- `devtechedge/oss-contributions` → `docs/SKILL.md`
- `devtechedge/oss-contributions` → `docs/PATTERNS.md`

Raw URLs (no auth, no API quota):

```
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/SKILL.md
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/PATTERNS.md
```

1. **Edit only the GitHub copies.** Local mirrors (`~/.agents/skills/oss/`, a Grok upload, a Codex project file) are derivatives. A change made to a derivative is lost on the next sync.
2. **Refetch at the start of every PR session.** If the copy you are reading did not come from those URLs during this session, fetch them and follow what comes back. Working from a stale mirror is a real failure mode, not a hypothetical: a session on an older copy did not know section 13 existed and hand-edited publication targets.
3. Raw is a CDN cache. It can briefly serve a stale or empty body right after a push, so a fetch that comes back empty must be retried against the contents API. Never proceed on an empty or truncated file.
4. After editing either file, push to `docs/` in the same turn (section 8.4) and let the propagator rebuild the local mirrors.

Platform notes:

- **WorkBuddy / zcode**: run `~/.agents/skills/oss/sync-from-github.py` (or `.sh`) after any push. It rewrites canonical and rebuilds the Grok zip.
- **grok.com**: upload `dist/oss.zip` produced by that script (`oss/SKILL.md` + `oss/references/PATTERNS.md`). Re-upload after every change; Grok snapshots the upload and will not see later edits.
- **Codex / ChatGPT**: store the bootstrap snippet in project or memory instructions so it fetches both URLs before starting work.

Bootstrap snippet for any platform:

```
Before any upstream OSS PR work, fetch and follow:
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/SKILL.md
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/PATTERNS.md
These are the single source of truth and override any local or previously uploaded copy.
```

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
- **Copy-pastable comment block:** whenever you draft, post, or fail to post a PR comment, issue reply, or review, always include a copy-pastable fenced code block of the exact GitHub markdown. Preserve blank lines, inline code, and paragraph breaks so the user can paste it into GitHub without reformatting. Use a fence longer than any backtick run inside the comment (four backticks wrapping the body, or a `~~~~` fence) so inner backticks stay intact. Required even when the agent posts successfully.
- Commit signing: check the repository's contribution policy and sign commits accordingly (DCO `Signed-off-by` trailer and/or cryptographic GPG/SSH signature) before pushing. See section 6 for the passphrase-hang failure mode.

## 3. Voice (non-negotiable)

- Professional, respectful, and concise. Lead with what changed and why; no performative filler.
- Never use em dashes in maintainer-facing text. Use a normal hyphen `-` or split the sentence.
- Sound human, not generated. Warmth and a little personality belong in replies to maintainers and co-authors; the technical substance stays technical. Read a draft aloud, and if it sounds like a template, rewrite it before posting.
- Emojis are allowed and encouraged in moderation when replying to people: one or two per comment, varied and relevant to what is actually being said. **Never 🙏 or prayer hands** - that overuse is why emojis were banned outright once before. Do not stack emoji runs, and do not open or close with an emoji every time.
- Vary the opening across a batch. When several comments go to the same maintainer, they must not share an opening line or follow the same template. This applies to thank-you notes too: three notes all opening "Thanks for merging, @X." read as templated even when each one is sincere.
- **One sentence per line in comments.** For PR, issue, and review comments, write exactly one sentence per paragraph with a blank line between every sentence. This is the shape the user has had the best feedback on: it reads lighter and is easier on the eyes than two-sentence blocks. It does not license a longer comment; keep the whole thing short regardless. No wall-of-text blocks in issues, PRs, or reviews.
- Prefer `Fixes #N` / `Closes #N` when the change fully resolves the issue.
- Informal tone is reserved for private chat with the user; all public text follows this section.
- Enforcement note: some machines carry a PreToolUse hook (`~/.zcode/hooks/voice-gate.mjs`, registered in `~/.zcode/cli/config.json`) that hard-blocks `gh pr comment` / `gh issue comment` calls whose inline body contains emojis or em/en dashes. That hook predates this section and is stricter than it. If it fires on an emoji this section now permits, update the hook rather than stripping the voice back out. Bodies passed via `--body-file` are not checked, so this section still applies manually there.

## 4. Cadence and API hygiene

1. Open one new PR at a time. A second may run only with explicit user permission. Complete the full cycle per PR - claim, implement, test, open, ledger update - before hunting the next target. Follow-up pushes to an existing open PR (human review, actionable bot P1) are fine while the next hunt is queued.
2. Run one agent session per PR lifecycle (hunt, ship) and retire it once the PR is open, the ledger is updated, and the post-run retrospective (section 8) is done. No session stays open to watch the PR: the user gets GitHub email notifications for maintainer activity and relays what needs action. The SKILL.md playbook and the GitHub ledger (`docs/triage/triage.json` in `oss-contributions`) carry the persistent state, so every fresh session stays small and bounded. Use long-running threads only for meta-discussion, never for PR work.
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
- Submission path open (verify before any heavy implementation work - 13 Sep 2026 casey/just lesson): the maintainer or issue author may have blocked the account, or applied hard filters (PRs disabled repo-wide, collaborator-only PRs, interaction limits) that silently stop PR creation and comments, while reads, forking, and pushing to the fork still succeed. These restrictions fail with misleading REST 404 / GraphQL FORBIDDEN on PR creation and do not appear in CONTRIBUTING.md. Before the heavy lifting: search the repo for "pull requests are disabled" issues and maintainer statements about PRs or AI contributions, and confirm the repo still merges outside authors (`author_association` OWNER/MEMBER on all recent merged PRs means the repo is effectively maintainer-only). Also read the repo's `.github/workflows/` for auto-close or claim-enforcement bots (13 Sep 2026 pydantic-ai lesson): a bot that closes PRs whose linked issue is unassigned to the PR author defeats every pre-open probe - fork push and even PR creation succeed - so issues that will never be assigned (bot-filed sweep issues) are not claimable; check how issues in the repo ever get assigned before investing. Then probe: push a working branch to the fork and attempt actual PR creation as soon as possible - a bare branch with no commits already works, since a `No commits between` validation error proves the creation endpoint processes the account's requests. 404/FORBIDDEN on creation means the submission path is closed - stop, record the no-go in triage, preserve the branch, and report. Do not polish tests, run full suites, or draft PR copy for a PR that cannot be opened.
- Stellar org default no-go: stellar/* repos are no-go unless an explicit maintainer invite exists on that specific issue. Only exception: stellar/stellar-docs, whose CONTRIBUTING.md accepts direct outside PRs for small fixes (typos, broken links, copy corrections) without an invite - re-verify its policy each cycle before relying on the exception. stellar/js-stellar-sdk remains invite-gated.
- Contribution policy satisfied: CLA, signed commits, required labels, repo accepting PRs. Also check the repo root for a dedicated AI policy file (e.g. `AI_POLICY.md`): a policy that bans agent-created PRs or mandates AI disclosure is an account-integrity hard gate (beetbox/beets, 14 Sep 2026) - stop and record a no-go rather than hiding AI usage; the only compliant path is the human opening the PR personally with the required disclosure. Read `AGENTS.md` / `CLAUDE.md` at the repo root too: they can carry GitHub-facing rules such as an explicit ban on agent attribution or a required branch naming convention (remix-run/remix, 15 Sep 2026).
- **AI disclosure is mandatory-only, never volunteered.** When the repo has no policy requiring disclosure, say nothing about AI assistance anywhere: not in the PR body, not in issue or PR comments, not in commit messages or trailers. Offering it unprompted is not extra honesty; it invites the repo to apply a policy it never asked for, marks the account, and buys nothing. Before opening or updating a PR, grep the body and draft comments for any mention of AI assistance and remove it. Disclose only when a policy explicitly requires it, and then disclose exactly what that policy asks for. Case (livekit/agents #7199, 15 Sep 2026): the repo has no AI policy, only an `AGENTS.md` of build commands, so the "AI-assisted implementation" note was stripped from the PR body after the fact. The converse still holds: an actual ban is a hard no-go to record, never something to route around.
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
10. All GitHub Actions and CI checks must be green before a PR is reported done. After each push, wait for checks to settle and confirm every check passes (or is non-actionable per step 9). A red check caused by your own change is actionable: read the failed job log, fix, push, confirm green. Never report a PR as done without confirming its checks passed; when a maintainer must manually approve the workflow run (`action_required`), say so explicitly instead of claiming green. When main itself is red at the base commit, compare the PR's failing check set to the base commit's (`commits/{sha}/check-runs`, conclusion==failure): a PR whose failing set equals main's, and whose every check that passes on main also passes, introduces no new red - report that standard, not "green".
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
4. Sync the ledger mirrors: after editing SKILL.md or PATTERNS.md, push the updated copies to `docs/SKILL.md` / `docs/PATTERNS.md` in `oss-contributions` (see sections 10 and 11; temp payloads deleted the same turn, nothing else written locally) so portable agent context stays accurate.
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

**Temp payload hygiene (hard rule):** `gh api --input body.json` is the correct way to pass large PUT bodies, but the payload file is disposable. Write it under the OS temp directory (`$TMPDIR`/`%TEMP%`), never in the user's workspace, and delete it in the same turn it is used. At session end the workspace must contain zero ledger-related files: no `triage_*.json`, no `*_body.json`, no `patterns_*.md`, no `.triage-tmp/` dirs. A leftover payload or snapshot in the workspace is a cleanup miss, not a checkpoint.

**Skill mirror:** the canonical playbook is `~/.agents/skills/oss/SKILL.md` plus its companion `PATTERNS.md`; never edit the copies in the ledger repo directly. The ledger repo carries mirrors at `docs/SKILL.md` and `docs/PATTERNS.md`, which exist for portable agent context.

**Grok packaging:** grok.com Skills import requires YAML frontmatter (`name` + `description`) and rejects a companion file uploaded on its own. Do not upload `PATTERNS.md` as a skill. Package the pair as a zip whose top folder matches `name:`:

```
oss/
  SKILL.md
  references/PATTERNS.md
```

zcode keeps `PATTERNS.md` beside `SKILL.md`. Grok loads the same file from `references/` on demand. The ledger mirrors stay side-by-side at `docs/SKILL.md` and `docs/PATTERNS.md`.


## 11. Single source of truth: the GitHub repo, not the local disk

The ledger exists in exactly one place: `oss-contributions` on GitHub. The local machine is a workspace, not a mirror. This section exists because past sessions accumulated `triage_snapshot.json`, `triage_latest.json`, `triage_latest2.json`, `triage_final.json`, `triage_2588.json`, `triage_body.json`, `patterns_body.json`, and `patterns_mirror.md` in the working folder - parallel stale copies of state that already lived on GitHub. That is a defect, never a pattern.

- **Read state from GitHub.** To read triage or ledger state, fetch `docs/triage/triage.json` (and `docs/SKILL.md` / `docs/PATTERNS.md` when relevant) directly: `gh api repos/devtechedge/oss-contributions/contents/<path>` and decode. Do not assume a local copy is current - every local copy ever created has gone stale within a session.
- **Write state to GitHub.** After every meaningful outcome (section 1 table), construct the updated JSON from the fetched current content and PUT it to GitHub in the same turn. One PUT per file with the final content; no intermediate local saves on the way.
- **Never create local ledger files.** No snapshots, no date-stamped copies, no `_latest`/`_final`/`_backup` variants, no local working copies "just for this session", no copies of `triage.json` or the PATTERNS/SKILL mirrors anywhere in the user's workspace. If you need to inspect or transform the JSON, do it in memory (or in a temp file under the OS temp directory, deleted the same turn). Workspace-root scratch files like `words.csv`, `scan_*.txt`, `touched_repos.txt` from a PR's local verification work go to that PR's temp workspace and are deleted before session end, never left at the workspace root.
- **Stale-copy rule:** if a local `triage_*.json` is encountered, treat it as a fossil. The remote file is truth; never restore, merge from, or push a local copy over the remote. If it differs, the local one is old.
- **Skill mirrors:** the canonical playbook is `~/.agents/skills/oss/SKILL.md` + `PATTERNS.md`. After editing either, PUT the updated copy to `docs/SKILL.md` / `docs/PATTERNS.md` in `oss-contributions` (temp payload deleted same turn). That push is the sync - there is no other sync step, and no third copy is created anywhere.

## 12. Unified ledger schema discipline

- Canonical triage memory is `docs/triage/triage.json` in `oss-contributions`, and only there (see section 11).
- Keep all records in the same arrays and schema. Do not create separate domain-specific queue files - on GitHub or on disk.
- Preserve existing field names and conventions. Update only affected records and keep dates/state accurate.
- Historical portfolio documents are informational and must not override canonical triage state.

## 13. Merge cascade (do not hand-edit publication targets)

When an upstream PR merges, do not independently edit README, resume, LinkedIn source, profile README, or the repository About text. Trigger the ledger workflow instead.

One-click: Actions → **Sync merged OSS** → Run workflow. Optional input `pr` is `owner/repo#number` (example: `pnpm/pnpm#14863`). Optional input `summary` is curated impact copy, used only when creating a new publication record.

The workflow:

1. Treats GitHub merge state as fact
2. Updates `docs/triage/triage.json` (status, merge date, merge commit, last_checked, issue closure, repo contribution list)
3. Upserts `docs/triage/publications.json` without overwriting `curated: true` copy
4. Regenerates README, resume.txt, linkedin-all-details.txt, and `docs/generated/`
5. Updates repository About description. This only works when the `LEDGER_SYNC_TOKEN` secret exists: PATCHing a repo description is admin-level, so `secrets.GITHUB_TOKEN` fails with 403 "Resource not accessible by integration". The run still reports success and About silently goes stale (it sat at 13 while the README already said 17), so after every sync confirm the About count matches the README. Without that secret the profile README step is skipped too.
6. Validates merged counts across every publication target
7. Commits only when something actually changed

Canonical operational record: `docs/triage/triage.json`
Canonical publication copy: `docs/triage/publications.json`
Human-only: GitHub profile bio, PATTERNS.md (unless a new generalizable lesson exists), social preview, `docs/all_repos.md`.

## 14. Publication copy quality (merged entries must explain the change)

Every merged PR gets real impact prose, never a one-line restatement of its title. A reader of the README, resume, or profile should be able to tell what changed and why it mattered without opening the PR.

- Write the change in concrete technical terms: name the function, flag, config key, or API surface touched, then the observable consequence. Example: "`Connection.sync()` no longer permanently sets `_ending`, so later `ECONNRESET` errors surface" beats "fix sync ending flag".
- One to three sentences, starting with what changed. No em dashes or emojis in this copy.
- **Set `curated: true` when writing it.** A record left at `curated: false` keeps whatever title-derived stub the reconciler generated, and no later run will improve it. Check the `curated` flag on every newly merged record as part of the merge cascade.
- Fill all four prose fields consistently: `ledger_what` (sentence case, README), `profile_line` (lowercase first letter, profile block), `resume_bullet`, `linkedin_bullet`.
- `profile_logo_alt` must not repeat the visible title. Alt text is what renders when the avatar fails to load, so `alt="stellar-docs"` beside a `stellar-docs #2849` heading reads as one run-on string. Use the org or product name (`Stellar`).
- After any sync, check the new record's `languages` field. An empty one makes the reconciler fall back to a wrong language in the resume bullet (a pure-Python repo was published as TypeScript until it was corrected by hand).

## 15. Gratitude to maintainers after a merge

When a human maintainer merges one of our PRs, send a short thank-you note on the PR thread. Maintainers are volunteers reviewing unpaid work, and a specific note is worth more than silence.

- Goes through the **comment approval gate** (section 2): draft the full text, get explicit approval in that turn, then post verbatim.
- Address the maintainer by handle. Name the specific thing the change or the review taught us, so the note cannot read as a template.
- Three or four sentences. No em dashes, no emojis, no ask, no follow-up question, no residue of the submission. Do not request anything.
- One note per merged PR, posted once. Never bump a merged thread a second time.
- Skip it when the merge came from a bot, an auto-merge queue, or was self-merged.
- When several merges land at once, post the notes across separate turns rather than in one burst; a sudden cluster of comments on old threads reads as automation.

See `docs/SYNC.md`.
