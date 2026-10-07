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

Learned patterns live in `PATTERNS.md`. Read the matching section on demand, not the whole file. Every pattern is a hypothesis: re-verify it, never assume it still holds.

How to read this playbook: rules are stated here, once. Case evidence and machine traps are in `PATTERNS.md`. Queue state is in `docs/triage/triage.json`. If a rule appears twice, this file wins and the longer copy is stale. Dated counts rot. Re-check GitHub before quoting one.

## 0. Canonical location and cross-platform sync

This playbook is used from several agent platforms (WorkBuddy, zcode, Codex/ChatGPT). Only one copy counts, and it lives in the ledger repo:

- `devtechedge/oss-contributions` → `docs/SKILL.md`
- `devtechedge/oss-contributions` → `docs/PATTERNS.md`

Raw URLs (no auth, no API quota):

```
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/SKILL.md
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/PATTERNS.md
```

1. **Edit only the GitHub copies.** Local mirrors (`~/.agents/skills/oss/`, a Codex project file) are derivatives. A change made to a derivative is lost on the next sync.
2. **Refetch at the start of every PR session.** If the copy you are reading did not come from those URLs during this session, fetch them and follow what comes back. Working from a stale mirror is a real failure mode, not a hypothetical: a session on an older copy did not know section 13 existed and hand-edited publication targets.
3. Raw is a CDN cache. It can serve a stale or truncated body with a 200 and no error, so an empty-body check is not enough: compare the fetched byte count against `gh api repos/devtechedge/oss-contributions/contents/<path> --jq .size` and refetch through the contents API when they differ (16 Sep 2026: raw served PATTERNS.md at 46,510 bytes while the API reported 60,916, a 24 percent silent truncation). Never proceed on an empty or truncated file.
4. After editing either file, push to `docs/` in the same turn (section 8.4), then run `~/.agents/skills/oss/sync-from-github.py` in the same turn so the local mirror matches canonical.

Platform notes:

- **WorkBuddy / zcode**: run `~/.agents/skills/oss/sync-from-github.py` (or `.sh`) after any push. It rewrites canonical. It also still builds `dist/oss.zip`, which existed only for grok.com and is now optional and unused.
- grok.com retired for OSS work (7 Oct 2026): no oss.zip upload step.
- **Codex / ChatGPT**: store the bootstrap snippet in project or memory instructions so it fetches both URLs before starting work.

Bootstrap snippet for any platform:

```
Before any upstream OSS PR work, fetch and follow:
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/SKILL.md
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/PATTERNS.md
https://raw.githubusercontent.com/devtechedge/oss-contributions/main/docs/triage/triage.json
These are the single source of truth and override any local copy.
```

SKILL.md and PATTERNS.md carry the rules. `triage.json` carries the state: every open, merged,
closed and no-go attempt, competing PRs, and the ping dates the close rules measure from. Read it
with `gh api repos/devtechedge/oss-contributions/contents/docs/triage/triage.json` and write it back
with a contents PUT in the same turn. A platform that fetches only the two docs knows the rules but
not the queue.

**Portability:** the rules travel in the skill, the state travels on GitHub. Moving to another
platform costs one fetch and nothing else, because no PR state lives on any single machine. Workspace
memory files and `~/osswork` scratch scripts are convenience only and are never load-bearing.

## 1. Unified OSS workflow

| | **Unified OSS ledger** |
| --- | --- |
| Scope | All upstream OSS work, including TS/JS/Python/Rust libraries, tooling, infrastructure, wallets, SDKs, blockchain software, frameworks, testing, concurrency, portability, security, and accessibility |
| Ledger | `oss-contributions` |
| Ledger writes | Update after every open, merge, no-go, closure, or other meaningful attempt outcome, same turn |
| Targeting | Rank all candidates together using the same eligibility, fit, scope, maintainer, freshness, validation, and merge-potential criteria |
| Account | The user's OSS account, typically `@devtechedge` |

Upstream PR work is recorded on the unified ledger repo. The README lists merged pull requests only; open, closed, no-go, and all other attempt state lives in docs/triage/triage.json. Work in the user's own repositories is never listed on the ledger.

**Co-authored merges (standing rule, 6 Oct 2026):** a merged PR opened by someone else counts as co-authored only when Dev's `Co-authored-by` trailer survives in the merged commit on the upstream default branch (check the merge or squash commit message, not the PR body). Record it in `triage.json` `pull_requests` with `role: "co-author"`, `primary_author`, and `adapted_from` when it carries our closed PR forward, and put its curated publication record in `publications.json` `co_authored`, never in `records`. The README lists it in its own Co-authored section. It is never part of any headline merged count: README badge, About `{count}` and `{names}`, resume, LinkedIn, Wellfound, DOCX, or the local snapshot. A missing `role` means author. An absorbed change with no surviving trailer gets no credit at all: note it in triage only (langgraphjs 2828 counts as co-authored; git-js 1193 absorbed our closed 1194 without a trailer and does not).

**Own / internal repos (standing rule, 20 Sep 2026):** for repositories the user owns or controls internally (e.g. `aether-flow`, the ledger itself, any `devtechedge/*` product repo that is not an upstream contribution target), land changes as a **direct commit on the default branch**. Do not open a pull request, do not ask to merge a PR, and do not leave a feature-branch PR hanging. If a PR was opened by mistake, put the commit on the default branch (fast-forward or cherry-pick), then close or delete the PR and its branch. Pull requests exist only for **upstream / external** repositories under this playbook. Cloud Agent defaults that open a PR are wrong for internal repos: override them and commit to the default branch instead.

## 2. Permissions and approvals

- Act (comment, open PRs, request review) only as the authorized OSS account. Never post as any other account.
- Never comment, open a PR, or request review without permission in that turn, or a batch authorization covering those exact targets. A batch such as "open N uncontested PRs" covers uncontested in-scope targets only: no contested pile-ons, no tracker edits unless named.
- **Comment approval gate:** always ask before posting any PR comment, issue reply, or review: show the full text to the user as a draft and wait for explicit approval of that exact text, every time, no exceptions. A general go-ahead such as "work on this" authorizes the work, not the post; the draft still needs its own approval in the turn it would be posted. Post the approved text verbatim. Never ask for posting approval before the draft exists and is shown: a "yes" to a blind should-I-post question is not approval of any text.
- **The opening description is not a comment.** GitHub anchors it as `#issue-<id>`. A comment is `#issuecomment-`. Never tell the user "no comment posted" when that is the link they are looking at. Confirm with `issues/N/comments` and `pulls/N/comments` both empty. A follow-up rewrite of the description still needs the full draft shown and approved before `gh pr edit`. Case (dtolnay/typetag #107, 29 Sep 2026).
- **Copy-pastable comment block:** whenever you draft, post, or fail to post a PR comment, issue reply, or review, always include a copy-pastable fenced code block of the exact GitHub markdown. Preserve blank lines, inline code, and paragraph breaks so the user can paste it into GitHub without reformatting. Use a fence longer than any backtick run inside the comment (four backticks wrapping the body, or a `~~~~` fence) so inner backticks stay intact. Required even when the agent posts successfully.

- **Verify after posting:** fetch the posted comment back from the API in the same turn and diff it against the approved text. A mis-built body posts successfully and returns 201 while carrying the wrong content, so a success response proves nothing about what landed. Case (stellar/stellar-docs#2768, 16 Sep 2026): a claim comment went out containing only a local temp file path, and the thread read as bot noise for days before it was caught and rewritten. Never report a comment as posted until the fetched body matches, and treat a body that is a path, empty, or truncated as a failed post to redo. The same check applies to a PR body written with `gh pr create --body-file` or `gh pr edit --body-file`. On Windows, write that file with Python `newline='\n'`; PowerShell `Set-Content` emits CRLF, GitHub stores the `\r`, and the fetched body will not match. A fetched body that contains `\r` is a failed post to redo. Case (sveltejs/devalue #214, 29 Sep 2026).
- Commit signing: check the repository's contribution policy and sign commits accordingly (DCO `Signed-off-by` trailer and/or cryptographic GPG/SSH signature) before pushing. See section 6 for the passphrase-hang failure mode.
- **Playbook edits need no approval round (standing user directive, 28 Sep 2026).** Dev prefers agents decide the details of SKILL.md and PATTERNS.md edits themselves (wording, placement, merging with or trimming against existing entries) and push them directly after the usual read-back and sync. Ask first only before public upstream posts: comments, PRs, reviews, and anything else maintainers will see.

## 3. Voice (non-negotiable)

- Professional, respectful, and concise. Lead with what changed and why; no performative filler.
- Never use em dashes in maintainer-facing text. Use a normal hyphen `-` or split the sentence.
- **Write as Dev, a person, not as a model.** PR descriptions, issue replies, and review comments must sound like he typed them. If a draft could be swapped onto another PR by changing the names, rewrite it. Read it aloud. Parallel sentences, a checklist of "left unchanged" lines, and a model id glued onto a template question all failed this test (getzola/zola #3293, 29 Sep 2026).
- Emojis are allowed and encouraged in moderation when replying to people: one or two per comment, varied and relevant to what is actually being said. **Never 🙏 or prayer hands** - that overuse is why emojis were banned outright once before. Do not stack emoji runs, and do not open or close with an emoji every time.
- Vary the opening across a batch. When several comments go to the same maintainer, they must not share an opening line or follow the same template. This applies to thank-you notes too: three notes all opening "Thanks for merging, @X." read as templated even when each one is sincere.
- **One sentence per line in comments.** For PR, issue, and review comments, write exactly one sentence per paragraph with a blank line between every sentence. This is the shape the user has had the best feedback on: it reads lighter and is easier on the eyes than two-sentence blocks. It does not license an essay. No wall-of-text blocks in issues, PRs, or reviews.
- **A bit detailed, not an essay.** Explain the change the way a person would if they had looked at it carefully: the function, what went wrong, what you changed, and how you checked it. A body that only names the mismatch and `Fixes #N` is too thin (dtolnay/typetag #107, 29 Sep 2026). A long draft that walks every side path is too much. Dev cut one of those in half, and that length was right (getzola/zola #3293, 29 Sep 2026). Do not paste struck-through template sections that do not apply.
- Prefer `Fixes #N` / `Closes #N` when the change fully resolves the issue.
- When the PR covers only part of the issue (one subcommand of several, a follow-up left open), write `Partially addresses #N` or `Part of #N`, never a closing keyword: a closing keyword auto-closes the issue on merge, so the maintainer has to edit the body to stop it. Ledger copy (`triage.json` summary, publication fields) follows the final upstream body, so re-read the body at merge and correct any drift in the same turn.
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

**Check order matters: read `.github/workflows/` before you evaluate any issue.** A repo-level auto-close or account scanner nullifies an otherwise perfect target, and it is invisible in the issue timeline, in CONTRIBUTING.md, and in the pin or code you would be fixing (16 Sep 2026 sqlfluff lesson: issue #8433 passed every issue-level gate and only died on the workflow, discovered after the go decision had been made). Two API calls at scan time cost nothing; hours of implementation spent on a PR that closes in 20 seconds do.

Hard gates:

- Open issue, no owning assignee, no competing open fix PR. Check the issue **timeline's** `cross-referenced` events for linked PRs, not just the body and comments - fresh bugs can have competing PRs before any triage comment lands (0 comments is not a clear field). Check the **author** of any open fix PR too: if it is our own account, another platform already ran the same brief in parallel, so stop, open nothing, and report the existing PR instead. Two PRs from one account on one issue is the worst possible outcome and no amount of care in the diff justifies it.
- No prior closed-unmerged PR on the same issue, or a clear reason why the earlier approach failed and the new one differs.
- The fix is owned by the repo being targeted; confirm companion packages (e.g. a `fastapi-users` bug may live in `fastapi-users-db-sqlalchemy`) before claiming.
- Reproducible or source-verifiable on the current default branch, and not already fixed on main even if the issue is still open.
- Bounded patch: small file count, plus tests where the repo has them.
- Outside contributions allowed: the repo must accept PRs from external contributors outright. If its CONTRIBUTING.md (or observed maintainer behavior) reserves PRs for maintainer-invited contributors - "open a PR only when a maintainer invites you", "help wanted" + approved approach, members-only, etc. - the repo is off-limits until such an invite exists on a specific issue. Do not code first and hope; leave at the scan stage.
- Submission path open (verify before any heavy implementation work - 13 Sep 2026 casey/just lesson): the maintainer or issue author may have blocked the account, or applied hard filters (PRs disabled repo-wide, collaborator-only PRs, interaction limits) that silently stop PR creation and comments, while reads, forking, and pushing to the fork still succeed. These restrictions fail with misleading REST 404 / GraphQL FORBIDDEN on PR creation and do not appear in CONTRIBUTING.md. Before the heavy lifting: search the repo for "pull requests are disabled" issues and maintainer statements about PRs or AI contributions, and confirm the repo still merges outside authors (`author_association` OWNER/MEMBER on all recent merged PRs means the repo is effectively maintainer-only). Also read the repo's `.github/workflows/` for auto-close or claim-enforcement bots (13 Sep 2026 pydantic-ai lesson): a bot that closes PRs whose linked issue is unassigned to the PR author defeats every pre-open probe - fork push and even PR creation succeed - so issues that will never be assigned (bot-filed sweep issues) are not claimable; check how issues in the repo ever get assigned before investing. Then probe: push a working branch to the fork and attempt actual PR creation as soon as possible - a bare branch with no commits already works, since a `No commits between` validation error proves the creation endpoint processes the account's requests. 404/FORBIDDEN on creation means the submission path is closed - stop, record the no-go in triage, preserve the branch, and report. Do not polish tests, run full suites, or draft PR copy for a PR that cannot be opened.
- No account-level scanner or auto-close workflow in `.github/workflows/` (16 Sep 2026 sqlfluff/sqlfluff lesson). This is a stronger version of the workflow check above, because it fires on the account rather than on the issue, so no amount of issue-level care avoids it. List the workflow files (`gh api repos/OWNER/REPO/contents/.github/workflows --jq '.[] | .name'`), then grep the bodies for `pull_request_target`, `types: [opened]`, `pulls.update` with `state: closed`, and named scanners such as AgentScan. A workflow that runs on `pull_request_target` at PR open with a write-capable token can label and close a fork PR before any maintainer reads it, and it usually exempts only `owner` and `member` associations. Confirm it has actually fired: list the issues carrying the label it applies and compare `created_at` to `closed_at`; a 10 to 20 second gap across a dozen PRs is a bot, never a human. Treat it as a repo-level no-go, not an issue-level one: record it against the repo in triage, delete any fork already made for it, and hunt elsewhere. AI disclosure in the PR body does not prevent this class of close, because the decision is made on account signals at open rather than on anything written in the body. Note the trap on the way out: such a bot often invites a reopen, and the scan frequently does not re-fire on `reopened`, but section 7 says never refile an auto-closed issue from the same account and never reply to the auto-close bot, so both branches end badly. Do not spend implementation effort to find out which one applies.
- Stellar org default no-go: stellar/* repos are no-go unless an explicit maintainer invite exists on that specific issue. Only exception: stellar/stellar-docs, whose CONTRIBUTING.md accepts direct outside PRs for small fixes (typos, broken links, copy corrections) without an invite - re-verify its policy each cycle before relying on the exception. stellar/js-stellar-sdk remains invite-gated, and the wording is not soft: its CONTRIBUTING.md was tightened on 2026-09-11 (#1728) to "Open a pull request only when a maintainer invites you to" and "Unsolicited pull requests will be closed without explanation and may be reported as spam", so an uninvited PR there risks a spam report, not only a close. Our #1725 predates that policy and was approved anyway; that is not a precedent for a second uninvited PR in the repo.
- Contribution policy satisfied: CLA, signed commits, required labels, repo accepting PRs. Also check the repo root for a dedicated AI policy file (e.g. `AI_POLICY.md`): a policy that bans agent-created PRs or mandates AI disclosure is an account-integrity hard gate (beetbox/beets, 14 Sep 2026) - stop and record a no-go rather than hiding AI usage; the only compliant path is the human opening the PR personally with the required disclosure. Read `AGENTS.md` / `CLAUDE.md` at the repo root too: they can carry GitHub-facing rules such as an explicit ban on agent attribution or a required branch naming convention (remix-run/remix, 15 Sep 2026). The policy can also sit at org level in a separate repo: `open-telemetry/community` `policies/genai.md` asks for an `Assisted-by:` trailer while opentelemetry-rust itself is silent (28 Sep 2026), so search the org's `community` or `.github` repo too.
- **AI disclosure is mandatory-only, never volunteered.** When the repo has no policy requiring disclosure, say nothing about AI assistance anywhere: not in the PR body, not in issue or PR comments, not in commit messages or trailers. Offering it unprompted is not extra honesty; it invites the repo to apply a policy it never asked for, marks the account, and buys nothing. Before opening or updating a PR, grep the body and draft comments for any mention of AI assistance and remove it. Disclose only when a policy explicitly requires it, and then disclose exactly what that policy asks for. Case (livekit/agents #7199, 15 Sep 2026): the repo has no AI policy, only an `AGENTS.md` of build commands, so the "AI-assisted implementation" note was stripped from the PR body after the fact. The converse still holds: an actual ban is a hard no-go to record, never something to route around. A PR template with its own AI Disclosure section (checkboxes, a Tools line, a prompt block) counts as the repo asking, so it is neither silence nor a ban: leave the section as an explicit placeholder in the draft and let the user choose the wording before opening, then use exactly the template's shape (prefix-dev/pixi #7109, 28 Sep 2026: `.github/pull_request_template.md` carries the section; the user filled it before open). A model id glued onto the question is not an answer. If the template asks what the model was used for, the line must say what it drafted and that a human reviewed the diff, ran the test, and stands by the change. The user writes that sentence before open or before `gh pr edit` (getzola/zola #3293, 29 Sep 2026). A model id inside a full human sentence is fine and is Dev's preferred shape where disclosure is required: the sentence says what the assistant drafted and that he reviewed, tested, and stands by it, with the model and effort in parentheses (for example `(Grok 4.7, effort: xHigh)`), as Dev added after open (7 Oct 2026, apache/datafusion-sqlparser-rs PR 2618). A policy that allows LLM code but requires comments and PR descriptions in a human's own words (rust-lang/rustup) makes the agent's draft a starting point only: Dev rewrites it or approves the exact text as his own before anything is posted.
- No design or policy gate pending. If semantics need maintainer agreement, comment the proposed approach and wait. Never code through the gate.

Freshness and aliveness:

- Repo is alive: pushed within the last ~3 months (`pushed_at`, not just `archived`). Uncontested issues in dormant repos (fuels-ts, alchemy-sdk-js, create-solana-program) are not targets.
- Repo merges outsiders, not just pushes. One GraphQL call, `pullRequests(first:30, states:MERGED, orderBy:{field:UPDATED_AT, direction:DESC})` with `authorAssociation`, `createdAt` and `mergedAt`: require at least one non-bot outside merge in the last 30 days that went through a normal review (a merge within the hour is usually staff), and a median open-to-merge time in days, not months. The ledger's merges landed within 9 days of opening, so a repo that cannot answer an outsider inside a week is not a target. Named misses are in PATTERNS.md, not repeated here.
- Issue is recent: opened within the past few days or the last few weeks (rough rule: 6 weeks or less). Treat age as a first-pass filter at discovery time (sort by newest), not a late check - months- or years-old issues are routinely closed on triage or already fixed.

Sizing and tilt:

- Always skip: contested issues, archived repositories, vague features needing design, and repeat AgentScan auto-close targets from the same account on the same issue.
- Repo size: prefer small and mid-size. When two repos offer a comparable fix, pick the smaller one. Judge the open-PR queue against outside-merge throughput, not by itself. Tiny repos (under ~50 stars) qualify only when the owner filed the issue and has merged an outside PR recently. Skip event, hackathon, bounty, and never-merged-an-outsider repos. Named cases are in PATTERNS.md.
- Unsolicited size and new API are a tilt against. Merged PRs have a median of about 50 changed lines. Without a maintainer asking on the issue, keep the diff under about 150 lines and prefer bug fixes to new surface.
- Saturation cap: 1 open PR in a repo is fine, 2-3 only for an exceptional fix, 4+ skip the repo for the cycle. Count per org too. Until an org has replied to one of ours, cap it at one open PR. Non-Stellar corporate web3 SDK orgs are cold (32 closed, 2 merged as of 28 Sep 2026). Burst evidence is in PATTERNS.md.

Scan mechanics (when asked to scan for N targets):

- Run read-only scan agents in parallel over disjoint repo groups; if the harness rejects parallel agents, retry one at a time. Each agent verifies per candidate: no assignee, no maintainer claim in comments, no cross-referenced or open PR (issue `timeline` plus PR keyword search), repo pushed recently. Agents never post anything.
- Bulk issue discovery uses the core `repos/{owner}/{repo}/issues?labels=bug` endpoint, not the search API: the search endpoint trips its secondary rate limit after ~2 rapid calls and kills the sweep; the core endpoint does not. Follow up with one `issues/{n}/timeline` call per shortlisted candidate for cross-referenced PRs.
- **Raced-target rule (pre-claim only):** if the issue timeline or keyword search reveals a competing open PR for the same issue/behavior *before we have opened anything*, classify the candidate as **contested/raced**, stop evaluating it for GO, and move to the next candidate. Do not spend implementation effort there unless the competing PR later closes or upstream state materially changes.
- **Never yield a PR we opened first (standing user directive, 16 Sep 2026).** Contribution is competitive, and a later PR from another contributor is not a reason to withdraw ours. When a competing PR appears *after* ours is already open: do not close, do not offer to close, and do not concede priority. Keep our branch rebased on the current base and `mergeable: true`, because a conflicted PR is an unreviewable one. Post one short, respectful note stating as fact that ours has been open on the issue since its date, what view it takes, and that it is rebased and ready; never volunteer to step aside. Offering to fold in anything the other PR covers that ours does not is fine, because incorporating is not withdrawing. Two PRs on one issue can end with the maintainer merging neither, and that risk belongs to the user, not to the agent, so never pre-empt it by standing down. Closing a live PR in favour of a competitor needs an explicit decision from the user in that turn.
- **Persistent tracker rule for raced targets:** when a raced/contested target is discovered, record it in the canonical `docs/triage/triage.json` in the existing format with the issue, related competing PR number(s), current status, verification date, and `do_not_duplicate: true`. This prevents future scans from rediscovering and re-evaluating the same race. Update the triage record if the competing PR closes, merges, or the issue changes materially.
- Race-check the sibling issues too. When the issue body names a related issue ("might be related to #N"), read that issue's timeline and open PRs as well: a PR aimed at the same root cause under a sibling number is a competitor even though it never cross-references our issue. Read the actor on each `cross-referenced` event, not only the PR author: a maintainer linking a core-team PR into the issue means the fix is being handled in-house, so the issue is owned even with no assignee (TanStack/router #8306, 6 Oct 2026).
- A `cross-referenced` event pointing at a foreign repo (issue numbers out of range for the repo, PR fetch returns 404) is noise, not an open competitor.
- An open refactor that rewrites the same line only as a side effect (not linked to the issue, not a fix for it) is not a competitor either: proceed, keep the diff minimal so either merge order stays trivial, and record the overlap in triage.
- Every scan re-verifies the existing candidate queue before adding new names. Candidates go stale in predictable ways: fixed on main, repo went dormant, a maintainer steered the design in comments (semi-contested, follow their stated direction exactly or skip), or a linked PR appeared. Stamp every candidate row with its verification date.
- A `Potential AI issue` label on an issue we claimed means maintainers are filtering AI-authored reports; any follow-up there must be extra precise and human.

## 6. Shipping steps

0. **Internal vs upstream:** if the target is an own/internal repo (section 1), skip this entire PR flow. Commit to the default branch and stop. The steps below apply only to upstream external repositories.

1. Default to fork, branch, and PR via `gh` when Cloud Agents are unavailable.
2. Probe the submission path before heavy work. The full gate is in section 5. A `No commits between` error proves the account can open PRs. 404 or FORBIDDEN means stop, record the no-go, keep the branch, and do not polish a PR that cannot be opened (casey/just #3227). When the user has not yet approved opening, skip the probe, because it is itself a PR-create call: rely on account-level evidence (a recent merge by this account in the same org, the repo merging first-time outsiders) and report the probe as skipped.
3. Treat a brief or hand-off as leads, not a spec: re-verify its root cause, test recipe, and environment claims (a missing package, "cannot build here") before following them, since a false "cannot run" silently drops a check CI will run. Minimal root-cause fix matching repo style. No drive-by refactors. An unreported bug that reproducing the issue in the repo's own test harness turns up on the same code path is not a drive-by: land it as its own first commit, name it in the claim or PR text, and offer it as a separate PR at the maintainer's choice, because a silently bundled fix reads as scope creep. When a just-merged PR of the same shape exists (same maintainer, the same change on a sibling subcommand), use it as the template for structure and naming, and read its review thread for what that maintainer pushed back on. Treat written rules in CONTRIBUTING.md (file LOC caps, required module layout, doc targets, and the development branch) as review gates even when CI does not enforce them: a new module over the stated cap gets flagged every round, and splitting it along its existing seams early is cheaper than defending it (reviewgate #144, 16 Sep 2026). Open against the branch CONTRIBUTING and recent outside code merges agree on, not blindly against the default branch. Confirm the bug on both when they differ (getzola/zola: default is `master`, code fixes land on `next`).
4. Add a focused regression that fails before and passes after, when tests exist. When recent history splits test and fix (`test:` then the fix), mirror it, so the test commit is itself the fail-before proof. If the failing call is not injectable, test the shared error arm both call sites use. Do not exhaust process limits, and do not add a test-only feature just to pause time (metrics-rs/metrics #718, see PATTERNS.md). Copy a neighbouring test's idiom only after checking it does something here, since a helper the harness already applies by default is a no-op line a reviewer will question. When the change is a commit series (fix, refactor, feature), every commit must pass fmt, CI's exact lint command and the full tests on its own so each one bisects cleanly, a refactor commit adds nothing that only a later commit uses, and a refactor that changes no existing snapshot or expected output is the proof it is behavior-neutral.
5. Add a changeset when the repo uses changesets. Write CHANGELOG or changeset entries so they need no PR number, or add the link as a second commit once the PR exists; never amend and force-push an open PR only to add its own link, since that rewrites the head SHA reviewers and CI already saw (cargo-about #325, 28 Sep 2026).
6. Use distinct branch names when multiple PRs target the same repo.
7. Sign commits per repo policy before pushing. Add `Signed-off-by` only when recent history uses it. Do not invent a trailer. Unattended SSH signing on this Windows box is solved: commit with `-c commit.gpgsign=false`, then `~/osswork/sign_commit.py`. Do not hand the re-sign to the user. Procedure is in PATTERNS.md under Signing commits. Confirm with `pulls/N/commits` -> `commit.verification.verified`, not `%G?`. The shared Linux box has no signing key, so commits made there are unsigned: push them only when the repo requires no verified signatures, otherwise sign on the Windows box.
8. Fix actionable bot review findings on your own code (e.g. Greptile P1) on the same branch. Ignore noise.
9. Leave non-actionable checks alone: Vercel "authorize deploy", team-only checks, and first-contribution `action_required` workflow approvals.
10. All GitHub Actions and CI checks must be green before a PR is reported done. After each push, wait for checks to settle and confirm every check passes (or is non-actionable per step 9). A red check caused by your own change is actionable: read the failed job log, fix, push, confirm green. Never report a PR as done without confirming its checks passed; when a maintainer must manually approve the workflow run (`action_required`), say so explicitly instead of claiming green. When main itself is red at the base commit, compare the PR's failing check set to the base commit's (`commits/{sha}/check-runs`, conclusion==failure): a PR whose failing set equals main's, and whose every check that passes on main also passes, introduces no new red - report that standard, not "green". Some workflows trigger only on `pull_request`, so the base commit has no check-runs at all; an empty base set is not a green base. Read the workflow's `on:` block and, when there is no push trigger, compare against sibling PRs' runs of the same workflow instead (see PATTERNS.md). CI that reports through the commit status API (CircleCI and similar) never shows up in `check-runs`: read `commits/{sha}/status` or `gh pr view N --json statusCheckRollup` instead, and never read an empty `check-runs` list as green or as nothing running. A rollup that shows only a green DCO check, or a null entry, is not the workflow result: read `actions/runs?head_sha=` and treat `conclusion: action_required` as the CI state.
11. Report the PR URL, plus the scoreboard when batching.

## 7. Maintainer responses (user-driven; no babysitting)

No babysitting: never set up a watch, cron job, event listener, or polling loop on a PR, old or new. GitHub already emails the user for every maintainer review, comment, and merge, and that email is the trigger. Standing watches burn background tokens for signal the user already has.

- When the user relays PR activity (an email, a comment, a review), act on it then: read the current PR state once, and treat bots as no-ops - CodeRabbit, Greptile, Copilot, Vercel, Changeset, Dependabot, Qodo, github-actions, CLA assistant, and `*[bot]` accounts generally. A bot comment may be worth surfacing to the user, but never act on it.
- Act only on human maintainer or collaborator responses: if a safe fix is clear, push it to the same branch while the change stays within the PR's scope, and reply in the approved voice through the comment approval gate.
- "Please sign your commit" asks (e.g. Safe repos): check `gh api repos/OWNER/REPO/pulls/N/commits` for `.commit.verification`. If `verified: true` with reason `valid`, the ask is already satisfied; update the ledger status and wait for merge, no reply needed. If not signed, only the user can re-sign locally with their key; the agent prepares the branch, the user signs and pushes.
- Closing our own open PR is a last resort, and never for an approved one. Before closing anything, re-read `reviewDecision`, the last comments and reviews, and the repo's recent merge history from the API, because a hand-off or older note claiming "no human contact" is the most rot-prone field in any summary and can be stale by minutes (16 Sep 2026: a hand-off recorded two `stellar/js-stellar-sdk` PRs as bot-only when a maintainer had closed one and approved the other minutes earlier). For a green, mergeable PR with no maintainer contact after about a week, prefer one polite nudge per thread over closing, and get per-PR approval before any close.
- Auto-close: if a PR is auto-closed shortly after opening, mark it Closed (not merged) when writing the ledger, never refile that issue from the same account, and never reply to the auto-close bot. Prefer quieter mid-size repositories when auto-closes keep happening.

- **Silence and dormancy (7 days, decided 2026-09-16, ping window cut to 7 days on 2026-09-20):** activity is a human other than us, or a code-review bot (CodeRabbit, Greptile, Copilot, Qodo, Devin, cubic-dev-ai). CI, deploy, changeset, codecov, CLA, Vercel, and Netlify do not count, and our own comments do not reset the clock. After 7 days with no activity, post one ping through the comment approval gate. After 7 more days of silence, close with one short sentence, also through the gate, not silently and not in a same-day burst. Two exemptions, both absolute: already approved and only waiting on merge (stellar/js-stellar-sdk#1725, safe-global/safe-docs#902 as of 2026-09-16), or a human maintainer still actively reviewing. One follow-up per PR is the ceiling.
- **Ping craft (2026-09-22):** a dormancy ping is not a one-liner. At least five sentences, gentle, concrete about files, root cause, tests, and the linked issue. One sentence per paragraph, blank line between, inline `` `code` ``, hyphen never an em dash. Post the approved text via `--body-file`, then fetch it back. Space a batch about one minute apart (20 Sep 2026: six pings in 40 seconds had no fallout; 22 Sep: five at one minute apart had none). Log `last_ping` in `docs/triage/triage.json` the same turn.

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
5. Close the loop with the user: end the conversation by asking whether they picked up any learnings or improvements to this playbook from the run, and write anything they offer per step 3 in the turn it is offered.
6. Only then retire the session. The next PR run starts from the updated playbook.

## 9. Email triage (OSS inbox)

- Confirm with the user whether flagged mail is actionable before acting.
- A GitHub email about an issue or PR we have no stake in (no PR, comment, or triage row of ours) is a scan lead, not a task. Check our involvement first, then run the section 5 gates. The email fires on new activity, so the thread is usually already raced by the time it arrives; report skip-or-go with the reasons and post nothing.
- CLA emails: the user signs in the browser. Confirm only after the `license/cla` check succeeds. A passing recheck alone does not sign.
- Keep: human approvals, reviews, merges, security alerts, anything from real people.
- Discard or ignore: bot-only noise such as Copilot, Vercel authorize, Changeset, CodeRabbit, Qodo "paused for this user" notices (usually the repository's Qodo plan, not a GitHub ban), surveys, and sales.
- Use the correct existing Gmail labels for the OSS accounts. Never invent vague labels.

## 10. Ledger and own-repo writes

The user's own unified ledger repo is `oss-contributions`; its README is the public product. Everything in this section lands on GitHub in the same turn it is decided - never leave such changes unwritten, and pushing needs no separate confirmation.

**How to write:** prefer direct GitHub CLI/API writes (`gh api` contents PUT / edit endpoints) for spot edits - do not clone-edit-push when a direct write does the same job faster. The user pulls via GitHub Desktop when needed. For whole-file transformations (styling sweeps across every table row), a scripted local rewrite is acceptable: `git pull --ff-only` first, re-read the file after any fetch, push the same turn, and rebase on origin if the push is rejected.

**Ledger commit messages must not contain `owner/repo#N`.** GitHub turns that into a cross-reference on the upstream issue, and the commit stays reachable by sha even after an amend. Write `owner/repo <N>` with no hash, or name the repo only. If one leaks, do not comment on the upstream thread to explain it. Full case is in PATTERNS.md under Ledger writes.

**Temp payload hygiene (hard rule):** `gh api --input body.json` is the correct way to pass large PUT bodies, but the payload file is disposable. Write it under the OS temp directory (`$TMPDIR`/`%TEMP%`), never in the user's workspace, and delete it in the same turn it is used. **On Windows, pass `--input` a `C:\...` path:** `gh` is a native binary and cannot open a Git Bash path, so a `/c/Users/...` argument fails with "cannot find the file specified" even when the file exists, and the PUT silently writes nothing. Where `%TEMP%` resolves somewhere native tools cannot reach, use a scratch directory such as `~/osswork` instead and delete the file in the same turn. At session end the workspace must contain zero ledger-related files: no `triage_*.json`, no `*_body.json`, no `patterns_*.md`, no `.triage-tmp/` dirs. A leftover payload or snapshot in the workspace is a cleanup miss, not a checkpoint.

**Skill mirror:** PUT the edit to `docs/SKILL.md` or `docs/PATTERNS.md`, then run the sync in section 0. A local-only edit is lost on the next sync. Do not restate the sync steps here.


## 11. Single source of truth: the GitHub repo, not the local disk

The ledger exists in exactly one place: `oss-contributions` on GitHub. The local machine is a workspace, not a mirror. This section exists because past sessions accumulated `triage_snapshot.json`, `triage_latest.json`, `triage_latest2.json`, `triage_final.json`, `triage_2588.json`, `triage_body.json`, `patterns_body.json`, and `patterns_mirror.md` in the working folder - parallel stale copies of state that already lived on GitHub. That is a defect, never a pattern.

- **Read state from GitHub.** To read triage or ledger state, fetch `docs/triage/triage.json` (and `docs/SKILL.md` / `docs/PATTERNS.md` when relevant) directly: `gh api repos/devtechedge/oss-contributions/contents/<path>` and decode. Do not assume a local copy is current - every local copy ever created has gone stale within a session.
- **Write state to GitHub.** After every meaningful outcome (section 1 table), construct the updated JSON from the fetched current content and PUT it to GitHub in the same turn. One PUT per file with the final content; no intermediate local saves on the way.
- **Never create local ledger files.** No snapshots, no date-stamped copies, no `_latest`/`_final`/`_backup` variants, no local working copies "just for this session", no copies of `triage.json` or the PATTERNS/SKILL mirrors anywhere in the user's workspace. If you need to inspect or transform the JSON, do it in memory (or in a temp file under the OS temp directory, deleted the same turn). Workspace-root scratch files like `words.csv`, `scan_*.txt`, `touched_repos.txt` from a PR's local verification work go to that PR's temp workspace and are deleted before session end, never left at the workspace root.
- **Stale-copy rule:** if a local `triage_*.json` is encountered, treat it as a fossil. The remote file is truth; never restore, merge from, or push a local copy over the remote. If it differs, the local one is old.
- **Skill mirrors:** after the PUT to `docs/SKILL.md` or `docs/PATTERNS.md`, run `~/.agents/skills/oss/sync-from-github.py` (section 0). The PUT alone is not the sync. Do not keep a third working copy in the workspace.

### 11.1 Local clones are disposable (added 16 Sep 2026)

A clone exists to produce one PR, not to archive one. On 16 Sep 2026 the working folder held 25
clones at **25.3 GB**, about 95 percent of it build output that the repos' own `.gitignore` files
already ignored: Rust `target/` trees at 19 GB, plus `node_modules`, `.venv`, and type-test caches.
Nothing in this playbook ever said to delete a clone, so none ever was.

- **Retire the clone when the PR is open, checks are green, and triage is updated.** The branch is
  pushed, the PR lives upstream, the state is in `triage.json`. Keep the clone only while it holds
  unpushed commits or you are actively iterating on review.
- **Confirm before deleting: `git check-ignore -v <path>`.** Name lists fail in both directions.
  `maturin/src/target/` is 2,177 lines of real Rust, not build output, while maturin's actual build
  dirs are `test-crates/targets` and `venvs` (plural), which a `target`/`venv` glob skips.
- **Check for unpushed work first** (`git status --porcelain`, `rev-list @{u}..HEAD`). A fork can be
  deleted upstream while the clone still holds the only copy: `devtechedge/just` was gone from
  GitHub while `just/tests/format.rs` still carried two uncommitted tests. Export a patch before
  deleting a clone in that state.
- **An oversized `.git` is worth a shallow re-clone** (`--depth 1 --branch <b>`), which took one
  clone from 1.63 GB to 11 MB at the same pushed commit. Shallow clones push normally but need
  `git fetch --unshallow` before any history-dependent work.

## 12. Unified ledger schema discipline

- Canonical triage memory is `docs/triage/triage.json` in `oss-contributions`, and only there (see section 11).
- Keep all records in the same arrays and schema. Do not create separate domain-specific queue files - on GitHub or on disk.
- Preserve existing field names and conventions. Update only affected records and keep dates/state accurate.
- Historical portfolio documents are informational and must not override canonical triage state.
- Diff stats in ledger copy (`+N/-M`, file count) come from `gh api repos/OWNER/REPO/pulls/N --jq '[.additions,.deletions,.changed_files]'` after the last push, never hand-summed from local commits: a follow-up commit that edits a line the PR itself added nets out against the base, so per-commit sums overcount (proptest #672, 7 Oct 2026).

## 13. Merge cascade (do not hand-edit publication targets)

When an upstream PR merges, do not independently edit README, resume, LinkedIn source, profile README, Wellfound source, or the repository About text. Trigger the ledger workflow instead. Resume, LinkedIn, Wellfound and the paste file live in `devtechedge/jobsearch-private` repo root since 21 Sep 2026 (PII, never in this public repo). The master resume DOCX lives there too: hand-maintained and decoupled from resume.txt (19 Sep 2026), auto-patched in CI via `scripts/sync-docx-to-private.py`, still editable in Word or via `scripts/patch-resume-docx.py --root <private-checkout>`.

One-click: Actions → **Sync merged OSS** → Run workflow. Optional input `pr` is `owner/repo#number` (example: `pnpm/pnpm#14863`). Optional input `summary` is curated impact copy, used only when creating a new publication record.

The workflow:

1. Treats GitHub merge state as fact
2. Updates `docs/triage/triage.json` (status, merge date, merge commit, last_checked, issue closure, repo contribution list)
3. Upserts `docs/triage/publications.json` without overwriting `curated: true` copy
4. Regenerates README in this repo plus professional docs in `devtechedge/jobsearch-private` repo root via `--private-root private`: `Devayan_Mandal-resume.txt`, `linkedin-all-details.txt`, `wellfound.txt`, `linkedin-experience-paste.txt`, and `devayan-all-details.txt` (counts, date, and MERGED_LIST, 30 Sep 2026; all other prose stays Dev's) (moved from `docs/generated/` 21 Sep 2026; `docs/generated/` no longer exists in this repo. The profile README sync renders its fragment in-memory.)
4d. Carries the same facts into the LOCAL career-ops user layer on Windows. The GitHub targets above
cannot reach `C:\Users\Devayan Mandal\Desktop\jobs\career-ops`, so that checkout drifts on its own.
`scripts/sync-local-snapshot.mjs --target <career-ops root>` reads the ledger plus the private details
file (two API calls) and patches only machine-known tokens in `cv.md`, `config/profile.yml`,
`modes/_brief.md`, `modes/_profile.md`, `article-digest.md`, and `documents/devayan-all-details.txt`
(count, as-of date, and the MERGED_LIST block spliced between its markers). It never overwrites a file
and never touches prose: all six paths sit in career-ops' own `USER_PATHS`, so `node update-system.mjs`
does not revert them. `--check` reports drift and exits 1 without writing. Scheduled by Windows Task
Scheduler task `DevTechEdge-OssLocalSnapshot` (logon + every 4h, logs to
`C:\Users\Devayan Mandal\osswork\logs\sync-local-snapshot.log`), wrapper
`~/osswork/scripts/sync-local-snapshot.ps1`, which sets `APPDATA` for `gh` and exits non-zero on
failure. Rule for this script: a replace callback rebuilds the match from its CAPTURE GROUPS, never by
indexing the match string, and every rule set must be a fixed point (a non-idempotent rule silently
eats text on the second run). Both mistakes happened once on 30 Sep 2026 and corrupted six files before
an idempotence guard caught them; keep that guard.

4b. Auto-patches the master resume DOCX `Devayan_Mandal.docx` in `jobsearch-private` root (moved 21 Sep 2026, decoupled 19 Sep 2026): the node sync never renders it and `validate()` does not check it, so Dev can audit and edit it in Word freely. The workflow step `scripts/sync-docx-to-private.py` (wrapping `scripts/patch-resume-docx.py --root private --lib-dir scripts/`) adds each newly merged PR in `IMPORTANCE`/`REPO_TIER` significance order with PR hyperlinks while every other byte passes through untouched. `scripts/render-resume-docx.py` stays as the ranking/condensing reference library but is never executed by the sync. Rule for future targets: same decoupling applies to any new hand-maintained binary, never wire it into the node render path.

5. Updates repository About description. This only works when the `LEDGER_SYNC_TOKEN` secret exists: PATCHing a repo description is admin-level, so `secrets.GITHUB_TOKEN` fails with 403 "Resource not accessible by integration". The run still reports success and About silently goes stale (it sat at 13 while the README already said 17), so after every sync confirm the About count matches the README. Without that secret the profile README step is skipped too.
Both public writes run only after `validate()` passes (since 4 Oct 2026, `dc29763`): a red run logs `about_skipped: "validate failed"` and `profile_readme.skipped: "validate failed"` and publishes nothing public. That skip is expected, so fix the red cause and re-run the workflow; never hand-patch About for it.
**If the run log shows About or the profile README skipped, repair both by hand the same turn.** The run still reports success. The signal is the About count lagging the README badge, or a null `about` in the log. If the log shows a non-null `about`, do not hand-patch (the token was present on the 15 Sep 2026 check; re-verify the log, do not assume either state).

1. About: fetch the current description, then `gh api -X PATCH repos/devtechedge/oss-contributions -f description=<new>`. The user's own `gh` credentials are admin on the repo, so this succeeds where `secrets.GITHUB_TOKEN` fails. **HARD RULE: the finished description MUST be <= 340 chars, re-derived whole from the template below on every merge, never a substring patch, never cut mid-word.** GitHub caps the field at 350 and truncates silently with no error (17 Sep 2026: the live copy hit exactly 350 and rendered cut off at "databa"), so 340 is the cap and 350 is never the target - 10 chars of breathing room for a count digit flip or a longer repo name. Measure the exact length before every PATCH and refuse to push anything over 340. This is a public field: never mention `docs/triage/triage.json` or any internal path or filename in it, because the tracker is agent-only.

   Template (HARD CAP 340 chars - fill as close to 340 as fits without exceeding):

   ```
   Public ledger of upstream open-source contributions: {count} merged pull requests across TypeScript, Rust and Python. Merged into {names}, covering SDKs, tooling, frameworks, databases, docs and concurrency fixes.
   ```

   `{count}` is the authored merged total (co-authored merges excluded, section 1). `{names}` is the distinct authored merged repos sorted alphabetically, joined with ", " and a final " and ". Re-summarise on every merge so the string lists as many merged repos as fit within 340: shed in this fixed order whenever the result exceeds 340 - first drop the ", covering ..." clause entirely (never trim it halfway), then drop names from the end of the sorted list and append " and more". Never `slice(0, 350)` or otherwise hard-cut the string to fit: a cut that lands mid-word is a failed write, rebuild via the shed order instead. The single enforcement point is `aboutDescription()` in `scripts/sync-merged-oss.mjs` (`ABOUT_HARD_CAP = 340`, throws on overflow) - if this template changes, update that function in the same turn, and vice versa. The manual fallback in this step follows the same template and the same length check. Snapshot only, not the live set (17 Sep 2026, 22 merged across 15 repos; live names come from `publications.json`): Anza Kit, Better Auth, Biome, maturin, node-postgres, pnpm, pytest-env, Recharts, reviewgate, Rspress, ruff, SQLMesh, stellar-docs, thirdweb JS, tracelens.
2. Profile README: restore the token and re-run the workflow, which renders the fragment in-memory and pushes it. No fragment file exists on disk since 18 Sep 2026, so there is nothing to fetch and no copy to recreate.

4c. Regenerates `Devayan_Mandal-resume.txt`, `linkedin-all-details.txt`, `wellfound.txt`, `linkedin-experience-paste.txt` in `jobsearch-private` root (moved 21 Sep 2026). Wellfound details follow (wired in 19 Sep 2026 after the file sat stale at 19 merged for three days: created by hand, never added here). It is the paste source for wellfound.com/profile/edit. Wellfound exposes no candidate-profile write API (only recruiter-side OAuth scopes), so manual paste stays the only path. Generated regions: the BIO line (hard cap 160 chars, flagship names shed from the end when over), the contributor-experience count line (`{n} pull requests merged into {m} projects`), the MERGED list grouped by repo most-recent-first from `repos[].linkedin_representative` (or the newest record's representative line), and the achievements count (`Getting {n} pull requests merged`). Static regions stay verbatim: the Full Stack Engineer experience (except its repo count), skills, Method, Stack, Q&A (answers trimmed to 250 chars and frozen 19 Sep 2026), the achievements spotlight narrative (currently pnpm #14863), and contact details. The Full Stack experience repo count is `open-sourced {k} repositories`, from the live own-repo feed. The Q&A block is not touched: answers were trimmed to 250 characters each on 19 Sep 2026 and frozen the same day per explicit request. Own-repo feed: `GET users/devtechedge/repos`, newest non-fork non-archived by created_at with a description (profile, ledger and github.io repos excluded), cached in `publications.json` under `wellfound_cache` with fallback to cache on fetch failure. `validate()` fails the run red when BIO exceeds 160, achievements exceed 1000, the count mismatches, any merged PR number is missing, or template leakage (`undefined`) appears. Rule for future targets: a new publication file gets its render step plus validate checks in the same turn it is created, never as a follow-up.

6. Validates merged counts across every publication target
7. Commits only when something actually changed

The sync updates repo text only. Live LinkedIn (About and the OSS Experience entry) and the live Wellfound profile (bio, OSS experience, achievements) never update themselves: after every green merge run, paste them from the regenerated `jobsearch-private` files (`linkedin-experience-paste.txt`, the ABOUT block of `linkedin-all-details.txt`, `wellfound.txt`), newest merge first, and confirm the live count matches the README badge. Frozen sections (Wellfound Q&A) stay untouched unless Dev decides otherwise.

Canonical operational record: `docs/triage/triage.json`
Canonical publication copy: `docs/triage/publications.json`
Human-only: GitHub profile bio, PATTERNS.md (unless a new generalizable lesson exists), social preview. `all_repos.md` moved to `jobsearch-private` root 21 Sep 2026, still human-only and never synced.

## 14. Publication copy quality (merged entries must explain the change)

Every merged PR gets real impact prose, never a one-line restatement of its title. A reader of the README, resume, or profile should be able to tell what changed and why it mattered without opening the PR.

- Write the change in concrete technical terms: name the function, flag, config key, or API surface touched, then the observable consequence. Example: "`Connection.sync()` no longer permanently sets `_ending`, so later `ECONNRESET` errors surface" beats "fix sync ending flag".
- One to three sentences, starting with what changed. No em dashes or emojis in this copy.
- **Set `curated: true` when writing it.** A record left at `curated: false` keeps whatever title-derived stub the reconciler generated, and no later run will improve it. Check the `curated` flag on every newly merged record as part of the merge cascade.
- Fill all four prose fields consistently: `ledger_what` (sentence case, README), `profile_line` (lowercase first letter, profile block), `resume_bullet`, `linkedin_bullet`.
- `profile_logo_alt` must not repeat the visible title. Alt text is what renders when the avatar fails to load, so `alt="stellar-docs"` beside a `stellar-docs #2849` heading reads as one run-on string. Use the org or product name (`Stellar`).
- **No em dashes anywhere in generated copy.** The separator between a PR title and its impact line is a plain hyphen, in `linkedin_bullet`, `profile_block`, the profile fragment template, and the LinkedIn representative bullets. Check the whole `publications.json` tree, not just `records`: the representative bullets come from `repos[].linkedin_representative`, a curated override map, and all 10 of them survived a records-only sweep on 15 Sep 2026.

- After any sync, check the new record's `languages` field. An empty one makes the reconciler fall back to a wrong language in the resume bullet (a pure-Python repo was published as TypeScript until it was corrected by hand). Better: pre-seed the full curated record before the first dispatch, because the DOCX step adds each new bullet once from `languages` and `ledger_what` and never rewrites it (PATTERNS.md, Ledger publication).
- **After hand-fixing a record, re-run the Sync merged OSS workflow.** README, `resume.txt`, the master DOCX and the profile fragment are rendered from `publications.json` at sync time, so a correction written straight into the JSON does not reach them until the next run. The run leaves `curated: true` copy alone, so re-running is safe. (PyO3/maturin#3302, 16 Sep 2026: fixing `languages` to Rust without a re-run left the resume bullet reading TypeScript for a Rust-only change.)

## 15. Gratitude to maintainers after a merge

When a human maintainer merges one of our PRs, send a short thank-you note on the PR thread. Maintainers are volunteers reviewing unpaid work, and a specific note is worth more than silence.

- Goes through the **comment approval gate** (section 2): draft the full text, get explicit approval in that turn, then post verbatim.
- Personalize with real first names. Before drafting, fetch each reviewer's GitHub profile (`gh api users/<login> --jq .name`) and address them by first name only, no @-mention (js-stellar-sdk#1725: quietbits is Iveta, Ryang-21 is Ryan). Never guess a name from a handle; if the profile name is blank, fall back to the handle.
- Name the review chain when one is visible (who requested whose review, who approved, who merged). It proves a human read the thread and gives every reviewer their moment.
- Warm, enthusiastic, collaborative: "thanks" never "thank yous". Enthusiasm lives in the words ("so much", "genuinely fun", "a ton", "spot on"), not in punctuation: a single exclamation mark on the closing line, at most three content-tied emojis, and not every paragraph needs one. Calibrated against Dev's hand edit of the #1725 note (18 Sep 2026), which kept my words but cut nearly every ! and emoji. Say plainly the process was fun and taught us a lot. The old flat no-emoji rule for these notes is retired by standing user directive (18 Sep 2026).
- Name the specific thing the change or the review taught us, so the note cannot read as a template.
- Three or four sentences, one sentence per paragraph. No em dashes, no ask, no follow-up question, no residue of the submission. Do not request anything.
- One note per merged PR, posted once. Never bump a merged thread a second time.
- Skip it when the merge came from a bot, an auto-merge queue, or was self-merged.
- When several merges land at once, post the notes across separate turns rather than in one burst; a sudden cluster of comments on old threads reads as automation.

- **Never publish maintainer praise.** Do not quote maintainers by name in the ledger README, the
  resume, the LinkedIn copy, or any other generated or public artifact, and do not add a "kind
  words" section to a public repo. The user judged that too exposed on 2026-09-16: a public page
  naming volunteers who reviewed our work reads as leverage, not gratitude. Keep such a list
  privately on disk instead if it is worth keeping.

See `docs/SYNC.md`.

## 16. Fork hygiene (a fork lives only as long as its PR)

- Rule: a fork exists to serve one PR. Delete it when that PR merges or is finally closed, so the fork count tracks live PRs instead of accumulating.
- Never delete a fork that has an open PR upstream. The PR's head branch lives on the fork, and deletion is permanent (GitHub offers only a best-effort restore for some repositories, within 90 days).
- Never edit upstream prose inside a fork. Changing a fork's text creates divergence on branches nobody reviews, and the next upstream sync fights it. Deletion is the right lever, editing is not.
- Account-wide text sweeps cover owned repositories only. Forks of upstream projects are out of scope.
- Before deleting, three checks: no open PR from that fork, no branch holding our own work, and no local clone that depends on the fork's remote.
- `compare` `ahead_by > 0` does not prove a branch is ours, because a fork carries every branch that existed upstream at fork time and a stale upstream branch reads as ahead. Check the branch tip's `author.login` instead, and keep the fork when the work is ours and no local clone has it.
- That `author.login` check does not actually work (16 Sep 2026): `repos/<fork>/branches` returns an empty author name and email for every branch, including branches we pushed ourselves. Use the fork's `created_at` against its `pushed_at` instead. A gap after creation means we pushed to the fork; a gap of a few seconds is noise from the fork itself. For any fork with a real gap, confirm in `triage.json` that the repo is a recorded dead end (auto-closed, no-go, superseded, maintainer-rejected) before deleting.
- Deleting a fork does not lose work that was already pushed as a PR, because upstream keeps the commits of an open or closed PR after the fork is gone. Work that was pushed to a fork but never opened as a PR is the only kind that is actually lost, so that is the case to check for a local clone before deleting.
- Delete in batches of about ten with a repo count check after each batch (`gh api user --jq .public_repos`), then confirm the open PR count is unchanged.
- `gh repo delete` needs the `delete_repo` scope; without it the call 403s. Add it with `gh auth refresh -s delete_repo`, which requires an interactive device flow.
- Pruning also blunts the "bulk forks" pattern that got the account flagged, and it stops 74 forks from burying the owned repositories on the profile.
