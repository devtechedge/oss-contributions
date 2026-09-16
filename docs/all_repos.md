# Complete Repository Portfolio for @devtechedge

Total Repositories: 93

---

## 1. zenith-canvas
- **URL:** https://github.com/devtechedge/zenith-canvas
- **Language:** TypeScript
- **Topics:** canvas, interactive, neo-brutalist, nextjs, productivity, react, tailwindcss, web-audio-api, localstorage, playwright, portfolio, typescript
- **Description:** Zenith Canvas is a neo-brutalist family workspace: drag-and-drop bento cards, checklists, sketches, guest passes, Web Audio chimes, and a 4-digit PIN vault. Next.js 14, React, TypeScript, Tailwind. Everything lives in localStorage - no backend, no accounts, no database. Fresh Start reset and architecture-blueprint modal.

### README.md

# Zenith Canvas

Neo-brutalist family canvas workspace - drag-and-drop bento cards, client-side persistence, Web Audio chimes, and a 4-digit PIN vault.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://zenith-workspace-ten.vercel.app)
[![CI](https://github.com/devtechedge/zenith-canvas/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/zenith-canvas/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3-06b6d4?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://zenith-workspace-ten.vercel.app**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://zenith-workspace-ten.vercel.app)

Do **not** use https://zenith-canvas.vercel.app or https://zenith-workspace.vercel.app - those hostnames are not this project.

> **Status:** Client-side only. Canvases, checklists, sketches, guest passes and the vault PIN live in `localStorage`. There is no account system, no database, and no production backend. Do not store secrets on the board.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="Zenith Canvas" width="800">
</p>

| Workspace | Control Deck |
|-----------|----------------|
| ![Workspace](docs/screenshots/01-workspace.png) | ![Control Deck](docs/screenshots/02-control-deck.png) |

---

## Features

- Absolute-positioned family canvas with drag, resize, and multi-canvas switching
- Checklist, note, sketch, countdown, and ambient-sound cards
- Direct-DOM drag/resize so pointer moves do not re-render the React tree
- Web Audio chimes and a client-side 4-digit PIN vault (Control Deck)
- CSV / text drop import with formula-injection sanitization (`= + - @` → quoted)
- Demo “Fresh Start” reset in Control Deck → Automations

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS 3, Lucide |
| Data | Browser `localStorage` (no database) |
| Auth | None. Demo PIN is a client-side UX gate - see [SECURITY.md](SECURITY.md) |
| Audio | Native Web Audio API |
| Hosting | Vercel (import this repo; do not use `output: "standalone"`) |
| CI | GitHub Actions (unit + typecheck + Playwright) |

---

## Quick Start

```bash
npm install
npm run dev
```

Open http://localhost:3000

```bash
npm test            # unit (CSV sanitizer, PIN, stars, guest passes)
npm run typecheck
npm run test:e2e    # Playwright Chromium smokes (shell, Control Deck, check-off, Fresh Start)
```

---

## License

MIT. See [LICENSE](LICENSE).


---

## 2. veritas-engine
- **URL:** https://github.com/devtechedge/veritas-engine
- **Language:** TypeScript
- **Topics:** ai-research-agent, gemini-api, langchain, langgraph-js, multi-agent-systems, nextjs, tavily-api, typescript, serverless-agent, portfolio, sse, vercel
- **Description:** Self-correcting multi-agent research engine for technical briefs. Planner drafts queries, Tavily retrieves in parallel, a critic grades 1-10 and loops until >=8 or max depth, then a synthesizer writes Markdown. Next.js 14, LangGraph.js, Gemini 2.5 Flash, SSE. Public Vercel is Demo mode (simulated). Live needs GEMINI_API_KEY and TAVILY_API_KEY. MIT.

### README.md

# Veritas Engine

Self-correcting multi-agent research console. Plan queries, retrieve in parallel, grade the evidence, loop until the critic passes, then synthesize a Markdown brief.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://veritas-engine-woad.vercel.app/)
[![CI](https://github.com/devtechedge/veritas-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/veritas-engine/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)](https://nextjs.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph.js-1-1C3C3C)](https://js.langchain.com/docs/langgraph)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://veritas-engine-woad.vercel.app/**

> **Status:** The public site defaults to **Demo** mode (simulated). Keys alone do not enable spend - set `LIVE_MODE=true` (optional `PUBLIC_RUN_TOKEN` / `x-run-token`). There is no login.

This is the **only** public repo for the project.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="Veritas Engine" width="800">
</p>

| Console | Cycle |
|---------|-------|
| ![Dark orchestration panel and graph](docs/screenshots/01-overview.png) | ![Live logstream and graph during a demo run](docs/screenshots/02-cycle-running.png) |

| Brief | Quality audit |
|-------|----------------|
| ![Synthesized Markdown brief](docs/screenshots/03-synthesized-brief.png) | ![Critic score ring and auditor notes](docs/screenshots/04-quality-audit.png) |

---

## Features

- LangGraph.js cycle: **Planner → Retrieval → Critic → (loop or) Synthesizer**
- Critic scores 1–10 and reroutes below 8 until max iteration depth
- Parallel Tavily searches on Live; mock hits on Demo
- SSE stream of node updates into the logstream and graph visualizer
- Custom zero-dependency Markdown renderer (headings, tables, lists, code)
- Copy brief or export `.md`
- Dark / light console; Demo / Live toggle

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14 App Router, React 18, TypeScript, Tailwind 3 |
| Agents | LangGraph.js + LangChain.js (`Annotation.Root`) |
| LLM (Live) | Gemini 2.5 Flash via `@langchain/google-genai` |
| Search (Live) | Tavily Search API |
| Streaming | Server-Sent Events from `POST /api/research` |
| Data on Vercel | Demo repository (simulated retrieval + canned brief) |
| Auth | None |
| Hosting | Vercel |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Architecture

```
Start → Planner → Retrieval (parallel) → Critic
                      ↑                    │
                      └── score < 8 ───────┤
                                           ▼
                                    Synthesizer → Markdown UI
```

---

## Quick Start

```bash
git clone https://github.com/devtechedge/veritas-engine.git
cd veritas-engine
npm install
cp .env.example .env.local
npm run dev
```

Open **http://localhost:3000**. Demo mode runs without keys.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: **no login**. Demo is forced unless `LIVE_MODE=true` (and optional run token). Headers, origin checks, rate limits: see SECURITY.md. Live keys stay on the server.

Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 3. synthesis
- **URL:** https://github.com/devtechedge/synthesis
- **Language:** TypeScript
- **Topics:** agentic, drizzle, hitl, langgraph, multi-agent, nextjs, observability, postgres, rag, react, sse, typescript
- **Description:** Autonomous multi-agent research: plan ΓåÆ research ΓåÆ synthesize ΓåÆ critique ΓåÆ finalize. Live agent graph, HITL approval, RAG, Reflexion, streaming SSE, eval gate. Next.js 16, Drizzle, Postgres. Groq llama-3.3-70b + Tavily when keys are set; otherwise a deterministic grounded simulator with the same UI. Free-tier Vercel demo. OpenAI-compatible keys.

### README.md

# Synthesis - Autonomous Multi-Agent Research Platform

[![Live Demo](https://img.shields.io/badge/Live%20Demo-synthesis--gold.vercel.app-black?style=for-the-badge&logo=vercel)](https://synthesis-gold.vercel.app/)
[![CI](https://github.com/devtechedge/synthesis/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/synthesis/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-16-black?style=flat-square&logo=nextdotjs)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph.js-agent%20graph-1C3C3C?style=flat-square)](https://langchain-ai.github.io/langgraphjs/)
[![Drizzle](https://img.shields.io/badge/Drizzle-Postgres-C5F74F?style=flat-square&logo=drizzle)](https://orm.drizzle.team/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](./LICENSE)

> Plan → research → synthesize → critique → finalize. A free-tier Vercel demo of senior agentic-loop engineering: live agent graph, HITL approval, RAG, Reflexion, streaming SSE, and an eval gate.

---

## Live Demo

**https://synthesis-gold.vercel.app/**

- **Real LLM path is live** - Groq (`llama-3.3-70b-versatile`) + Tavily web search. Full multi-agent runs with cited reports, Reflexion, and telemetry.
- **Demo / simulated mode is the default** - works with or without keys. Real LLM/search only when LIVE_MODE=true and keys are set (optional PUBLIC_RUN_TOKEN).
- Any OpenAI-compatible provider works via `OPENAI_API_KEY` + `OPENAI_BASE_URL` + `OPENAI_MODEL`.

---

## Screenshots

| Plan approval (HITL) | Run complete |
|---|---|
| ![Plan approval](docs/screenshots/plan-approval.png) | ![Complete](docs/screenshots/run-complete.png) |

| Cited report | Evidence (11 sources) |
|---|---|
| ![Report](docs/screenshots/report-view.png) | ![Evidence](docs/screenshots/evidence-gathered.png) |

---

## What it does

1. **Brief** - enter a complex research question.
2. **Planner** - decomposes into research vectors; run **pauses for human-in-the-loop approval**.
3. **Research crew (parallel fan-out)** - tools (`web_search`, `read_url`), typed evidence, RAG ingest.
4. **Synthesizer** - cited Markdown report, streamed.
5. **Critic (Reflexion)** - faithfulness score; bounded revision loop if below threshold.
6. **Fact-checker** - source credibility audit.
7. **Finalizer** - confidence + cost/latency dashboard.

Every event is persisted - any past run is replayable.

---

## Agentic-loop principles (enforced)

| Principle | Implementation |
|---|---|
| **Loop is a graph, not a `while`** | `StateGraph` executor - nodes, conditional edges, explicit `END`. |
| **Plan → Act → Observe → Reflect** | ReAct tools + Reflexion critic with bounded revisions. |
| **Bounded autonomy + budget** | Max steps / tokens / cost / wall-clock → graceful finalize. |
| **Human-in-the-loop** | Planner checkpoint → `awaiting_approval` → resume on approve. |
| **Resumable state** | Full checkpoint to Postgres after every node. |
| **Structured I/O** | Zod-validated agent protocol; LLMs forced to JSON. |
| **Streaming-first** | SSE token + state events drive live graph & timeline. |
| **Observe before optimize** | Traced spans (latency / tokens / cost). |
| **Eval-driven** | `/api/eval` golden set + CI gate. |
| **Fail safe, fail cheap** | Retry/backoff, tool isolation, simulated fallback, partial results. |

---

## Architecture

```
Browser ──SSE──▶ Next.js (App Router) ──▶ Orchestration (StateGraph)
                                              │
        ┌──────────────┬──────────────────────┼───────────────────────┐
        ▼              ▼                      ▼                       ▼
   Agent crew      Tools / MCP bus        RAG / Memory           Observability
   planner         web_search, read_url,  JSONB embeddings,      event store +
   researcher      compute, query_memory  cosine retrieval,      cost/token/lat
   synthesizer                            long-term memory        spans
   critic
   fact_checker
   finalizer
        │
        ▼
   Postgres: runs · checkpoints · events · documents · evidence · memories · eval_runs
```

**Portability:** embeddings as JSONB float arrays (no pgvector required) - runs on any Neon / Vercel Postgres free DB.

---

## Key source

```
src/
├─ db/schema.ts                 # Drizzle schema
├─ lib/agent/
│  ├─ schemas.ts                # Zod state + AgentEvent protocol
│  ├─ llm.ts                    # OpenAI-compatible client + simulated mode
│  ├─ tools.ts                  # web_search / read_url / compute
│  ├─ rag.ts                    # embeddings, ingest, cosine retrieve
│  ├─ graph.ts                  # StateGraph executor
│  ├─ agents.ts                 # planner → finalizer crew
│  ├─ engine.ts                 # planResearch (HITL) + runResearch (stream)
│  └─ tracer.ts                 # SSE + durable events + cost spans
├─ app/api/run/...              # create, approve (SSE), detail, eval
└─ components/synthesis/        # App, AgentGraph, Timeline, ReportView
```

---

## Local dev

```bash
npm install
cp .env.example .env          # DATABASE_URL required; LLM/search keys optional
npx drizzle-kit push
npm run dev
```

Open http://localhost:3000.

### Demo mode (no keys)
Deterministic grounded engine - full graph, HITL, telemetry, eval. **Deployed demo always works.**

### Real mode
```
OPENAI_API_KEY=gsk_...                    # Groq (or any OpenAI-compatible key)
OPENAI_BASE_URL=https://api.groq.com/openai/v1
OPENAI_MODEL=llama-3.3-70b-versatile
TAVILY_API_KEY=...                        # live web search
```

---

## Evaluation & CI

[![CI](https://github.com/devtechedge/synthesis/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/synthesis/actions/workflows/ci.yml)

- **Unit tests** - Zod schemas, token/cost math, cosine, tool allow-lists, StateGraph termination, Reflexion routing (`npm test`)
- **Typecheck** - `tsc --noEmit`
- **Playwright** - Chromium smokes for idle chrome + HITL plan pause (`npm run test:e2e`)
- **Eval gate** - `GET /api/eval?limit=2` golden set (simulated engine, Postgres service)

```bash
npm ci
npm test
npm run typecheck
npm run test:e2e    # needs DATABASE_URL for the HITL path; UI smokes skip it
```

Threat model: [SECURITY.md](./SECURITY.md).

---

## Deploy (Vercel free tier)

1. Import the GitHub repo on Vercel.
2. Add Neon Postgres (Storage → Create Database → Neon) - `DATABASE_URL` is injected automatically.
3. Optional: Groq + Tavily env vars. Real spend also needs LIVE_MODE=true (keep false on public demos).
4. Optional: PUBLIC_RUN_TOKEN - live calls must send matching x-run-token.
5. Redeploy and open the live URL.

---

## Environment

See [`.env.example`](./.env.example). Only `DATABASE_URL` is required. Provider keys alone do not enable live spend - set LIVE_MODE=true (and optionally PUBLIC_RUN_TOKEN). Details: [SECURITY.md](./SECURITY.md).

---

## Roadmap

- CrewAI / AutoGen reference engines behind the same contract
- pgvector + ANN for larger corpora
- MCP tool-server exposure
- Langfuse-hosted tracing

---

## License

MIT - see [LICENSE](./LICENSE).

See also [SECURITY.md](./SECURITY.md).

Built as a senior-portfolio demonstration of agentic-loop engineering.


---

## 4. oss-contributions
- **URL:** https://github.com/devtechedge/oss-contributions
- **Language:** JavaScript
- **Topics:** tanstack, typescript, javascript, oss, vitest, better-auth, biome, drizzle, rust, blockchain, ethereum, rainbowkit, safe, stellar, ethers, solana, thirdweb, wagmi, walletconnect, web3
- **Description:** Public ledger of upstream open-source contributions across Web3 and non-Web3 projects. 19 merged contributions across Anza Kit, Better Auth, Biome, node-postgres, pnpm, pytest-env, Recharts, Rspress, SQLMesh, stellar-docs, thirdweb JS, and tracelens, spanning TypeScript, Rust, Python, developer tooling, frameworks, databases, concurrency, portabili

### README.md

# ⚙️ OSS contributions

Public ledger of **upstream open-source contributions**.

![Merged](https://img.shields.io/badge/merged-19-brightgreen?logo=git&logoColor=white) ![License](https://img.shields.io/github/license/devtechedge/oss-contributions) ![Last commit](https://img.shields.io/github/last-commit/devtechedge/oss-contributions) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white) ![TanStack](https://img.shields.io/badge/TanStack-FF4154?logo=tanstack&logoColor=white) ![Web3](https://img.shields.io/badge/Web3-000000?logo=web3.js&logoColor=white)

**Latest update:** 15 Sep 2026

This repository serves as the canonical record of upstream contribution activity: identifying worthwhile issues, tracking claims and active pull requests, preserving implementation and review outcomes, and maintaining an auditable history of merged, closed, and declined work.

## ✅ Merged pull requests

<!-- ledger:merged-table:start -->
| Repo | PR | What | Merged |
| --- | --- | --- | --- |
| <img src="https://github.com/stellar.png?size=40" width="18" /> [stellar/stellar-docs](https://github.com/stellar/stellar-docs) | [#2859](https://github.com/stellar/stellar-docs/pull/2859) | Added the --enable-core-manual-close flag to the Local section of the Network Modes page, so the parameter list no longer omits a flag the quickstart container ships, with a cross-link to the Manual close mode section noting that only the local configuration sets NODE_IS_VALIDATOR. | 15 Sep 2026 |
| <img src="https://github.com/stellar.png?size=40" width="18" /> [stellar/stellar-docs](https://github.com/stellar/stellar-docs) | [#2850](https://github.com/stellar/stellar-docs/pull/2850) | Documented Quickstart's undocumented `--enable-core-manual-close` flag in the advanced usage docs. The Operation Modes page now covers the flag, the `MANUAL_CLOSE` setting it writes into the generated `etc/stellar-core.cfg`, and triggering a close through the `manualclose` endpoint on port 11626, while Run Commands adds macOS, Linux, and Windows startup examples that bind the admin port to loopback. The new section also records two limits readers hit in practice: the flag is accepted on every network but only usable on local, because stellar-core checks `NODE_IS_VALIDATOR` when `manualclose` is invoked and only the local config sets it, and each invocation advances exactly one ledger. | 15 Sep 2026 |
| <img src="https://github.com/ssf0409.png?size=40" width="18" /> [ssf0409/tracelens](https://github.com/ssf0409/tracelens) | [#140](https://github.com/ssf0409/tracelens/pull/140) | Markdown table cells in the report generator are now escaped with html.escape in addition to pipe and newline handling. Task ids or gate values containing pipes, line breaks, or HTML metacharacters no longer break the per-task and baseline-gate tables piped into $GITHUB_STEP_SUMMARY, and no cell can open a raw HTML element. | 15 Sep 2026 |
| <img src="https://github.com/stellar.png?size=40" width="18" /> [stellar/stellar-docs](https://github.com/stellar/stellar-docs) | [#2849](https://github.com/stellar/stellar-docs/pull/2849) | Reworked the Soroban address conversion example to propagate the fallible `Result<Address, ConversionError>` from `Address::from_xdr()` instead of calling `.unwrap()`, which panics on malformed XDR. Added prose noting that contracts consuming XDR from untrusted sources must handle the error instead of aborting. | 14 Sep 2026 |
| <img src="https://github.com/stellar.png?size=40" width="18" /> [stellar/stellar-docs](https://github.com/stellar/stellar-docs) | [#2853](https://github.com/stellar/stellar-docs/pull/2853) | Reconciled contradictory memo guidance in the pooled accounts guide: the intro framed memos as obsolete while later sections still required supporting them. Reworked the intro and opening note so memos read as the legacy mechanism still in active use and muxed accounts as preferred going forward, with the guide covering both. | 14 Sep 2026 |
| <img src="https://github.com/stellar.png?size=40" width="18" /> [stellar/stellar-docs](https://github.com/stellar/stellar-docs) | [#2851](https://github.com/stellar/stellar-docs/pull/2851) | Qualified the dapp frontend guide's blanket claim that Freighter requires HTTPS. `http://localhost` and `http://127.0.0.1` are already Potentially Trustworthy origins under the W3C Secure Contexts specification, so plain HTTP on loopback satisfies Freighter's secure-context requirement and readers no longer need to provision TLS for local development. | 14 Sep 2026 |
| <img src="https://github.com/pytest-dev.png?size=40" width="18" /> [pytest-dev/pytest-env](https://github.com/pytest-dev/pytest-env) | [#262](https://github.com/pytest-dev/pytest-env/pull/262) | Documented that pytest.toml and .pytest.toml accept the native [pytest] env table, not only the plugin-specific [pytest_env] section. | 14 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14863](https://github.com/pnpm/pnpm/pull/14863) | Fixed startup crashes on FreeBSD and other non-Windows Unix-like platforms by making default_store_dir use the Unix fallback path; added platform-specific regression coverage. | 14 Sep 2026 |
| <img src="https://github.com/web-infra-dev.png?size=40" width="18" /> [web-infra-dev/rspress](https://github.com/web-infra-dev/rspress) | [#3678](https://github.com/web-infra-dev/rspress/pull/3678) | Awaited FlexSearch `addAsync()` indexing before search initialization completes, preventing early queries from incorrectly returning no results on larger sites; focused change preserves existing behavior. | 14 Sep 2026 |
| <img src="https://github.com/recharts.png?size=40" width="18" /> [recharts/recharts](https://github.com/recharts/recharts) | [#7805](https://github.com/recharts/recharts/pull/7805) | Removed `tabIndex={-1}` from z-index portal `<g>` layers so empty SVG groups are not pointer-focusable, preventing WebKit geometry-traced focus rings; added regression coverage asserting no rendered layer carries a `tabindex` attribute. | 13 Sep 2026 |
| <img src="https://github.com/brianc.png?size=40" width="18" /> [brianc/node-postgres](https://github.com/brianc/node-postgres) | [#3772](https://github.com/brianc/node-postgres/pull/3772) | `Connection.sync()` no longer permanently sets `_ending`, so later `ECONNRESET` / `EPIPE` errors are not swallowed. Regression and integration coverage protects the behavior. | 11 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14756](https://github.com/pnpm/pnpm/pull/14756) | `pnpm update pkg@x.y.z` preserves existing `^` / `~` range operators and supported `npm:` / `jsr:` prefixes. | 10 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14754](https://github.com/pnpm/pnpm/pull/14754) | Non-recursive `pnpm run "/pattern/" --no-bail` no longer terminates sibling scripts after the first failure. | 10 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14753](https://github.com/pnpm/pnpm/pull/14753) | `lockfile: false` is respected with `devEngines.packageManager.onFail: download`; package-manager download/switch still works without project lockfile synchronization. | 10 Sep 2026 |
| <img src="https://github.com/SQLMesh.png?size=40" width="18" /> [SQLMesh/sqlmesh](https://github.com/SQLMesh/sqlmesh) | [#6040](https://github.com/SQLMesh/sqlmesh/pull/6040) | `ModelTest.create_test()` runs on the calling thread, eliminating a race around shared `execution_time` / `time_machine` state. | 10 Sep 2026 |
| <img src="https://github.com/anza-xyz.png?size=40" width="18" /> [anza-xyz/kit](https://github.com/anza-xyz/kit) | [#2032](https://github.com/anza-xyz/kit/pull/2032) | Restored `number` predicates in the `getPatternMatchCodec` documentation examples so they match the actual codec typing. | 9 Sep 2026 |
| <img src="https://github.com/better-auth.png?size=40" width="18" /> [better-auth/better-auth](https://github.com/better-auth/better-auth) | [#11208](https://github.com/better-auth/better-auth/pull/11208) | Regression coverage locks the `/phone-number/verify` OpenAPI `requestBody` contract after a Zod intersection issue. | 9 Sep 2026 |
| <img src="https://github.com/biomejs.png?size=40" width="18" /> [biomejs/biome](https://github.com/biomejs/biome) | [#11667](https://github.com/biomejs/biome/pull/11667) | Added the `useBetterDomTraversing` nursery lint rule, ported from `eslint-plugin-unicorn`, with fixtures and release integration. | 8 Sep 2026 |
| <img src="https://github.com/thirdweb-dev.png?size=40" width="18" /> [thirdweb-dev/js](https://github.com/thirdweb-dev/js) | [#8938](https://github.com/thirdweb-dev/js/pull/8938) | Genuine `useTokenQuery` request failures are rethrown instead of being converted into `Token Not Supported`; added regression tests and changeset. | 7 Sep 2026 |
<!-- ledger:merged-table:end -->

## ✍️ Selected write-ups

Short technical notes on eight of the merged contributions, covering the root cause, why the obvious fix was wrong, and how each change was verified.

- [Sync is not a disconnect](docs/writeups/node-postgres-3772-sync-is-not-a-disconnect.md) - node-postgres #3772
- [A package manager that cannot print its own version](docs/writeups/pnpm-14863-store-dir-panic-on-unix.md) - pnpm #14863
- [pnpm update ate your caret](docs/writeups/pnpm-14756-update-ate-the-caret.md) - pnpm #14756
- [A focus ring that traced the shape of a bar](docs/writeups/recharts-7805-pointer-focus-rings.md) - recharts #7805
- [A catch block that returned nothing](docs/writeups/thirdweb-js-8938-catch-block-returned-nothing.md) - thirdweb-dev/js #8938
- [Search that says "no results" while it is still indexing](docs/writeups/rspress-3678-await-search-indexing.md) - rspress #3678
- [Build the tests before the workers race](docs/writeups/sqlmesh-6040-build-tests-off-worker-threads.md) - SQLMesh #6040
- [useBetterDomTraversing, and knowing what not to autofix](docs/writeups/biome-11667-use-better-dom-traversing.md) - Biome #11667

Full index: [docs/writeups](docs/writeups/README.md).

## 🔀 Open pull requests

Open work is not enumerated here. Contributions are reviewed upstream on their own timelines, and a long-running PR says more about the upstream queue than about the change. This ledger lists merged contributions only; work in flight is visible on my GitHub profile and in each upstream repository.

## 🧭 Engineering focus

TypeScript · JavaScript · Python · Rust · frameworks · developer tooling · infrastructure · concurrency · portability · security · accessibility · testing · wallets · SDKs · blockchain infrastructure

## 📄 License

MIT


---

## 5. milkywayathome_client
- **URL:** https://github.com/devtechedge/milkywayathome_client
- **Language:** C
- **Topics:** None
- **Description:** milkway@home client

### README.md

# Milkyway@Home Client

[![Linux Build](https://travis-ci.org/Milkyway-at-home/milkywayathome_client.svg?branch=master)](https://travis-ci.org/Milkyway-at-home/milkywayathome_client)
[![MinGW Build](https://travis-ci.org/Milkyway-at-home/milkywayathome_client.svg?branch=travis-xcompile)](https://travis-ci.org/Milkyway-at-home/milkywayathome_client)

> **Note:** CMake version 4.0 and later are **not currently supported**.

---

## Table of Contents

- [N-body](#n-body)
- [Compiling N-body](#instructions-for-compiling-nbody)
- [Running N-body](#running-n-body-options)
- [Input Lua File Dwarf Model Options](#input-lua-file-dwarf-model-options)
- [N-Body CMAKE Flags](#n-body-cmake-flags)
- [Tests](#tests)
- [Separation](#separation)
- [TAO](#tao)
- [Random Notes](#random-notes)

N-body
---
- Simulations are described with Lua input files which can be used
  to produce an arbitrary initial configuration of particles. 

- Number of particles can be indicated in the Lua input file as 
  a total number of bodies where half will be baryons and half 
  will be dark matter particles or as the total number of bodies
  with the number of baryons as an extra parameter  

- Various options are available for applying external potentials
  to a system.

- Graphics can be run separately and attach to existing simulations,
  or can be launched at the same time with the --visualizer argument
  to the main process.

- N-body videos can be produced by using a separate program to
  record OpenGL. A wrapper script that uses this can be used as
  the --visualizer-bin argument to record a video of the
  visualization. An example script is at tools/RecordNBodyVideo.sh

- Consistent N-body results between different systems require crlibm
  and SSE2 (at least on x86, not sure about other architectures)

- Returning nil from makePotential() for N-body will run the
  simulation without an external potential

- Device information is exposed to the workunit through the
  deviceInfo table if it is used.

- **Checkpoint test does not always pass. Do not be concerned with an occasional failure**


Instructions for Compiling Nbody
---
Step 0.  Ensure proper packages are installed

    (For Ubuntu) sudo apt-get install mingw-w64 cmake
    (OpenGL)     sudo apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev
    (NCurses)    sudo apt-get install libncurses5-dev libncursesw5-dev
    (OpenSSL)    sudo apt-get install libssl-dev

Step 1.  Download all necessary files (Only need to git submodule if cross compiling with BOINC)
```
git clone https://github.com/Milkyway-at-home/milkywayathome_client.git
cd milkywayathome_client
git submodule update --init --recursive
```
NOTE: If you are running on WSL (Windows Subsystem Linux), you may need to run the following commands
```
git submodule sync
git submodule init
git submodule update
```
Step 2.  Compile Nbody
```
./build_client
```
Step 3.  Run a Nbody Simulation
```
./run_nbody
```

Running N-Body Options
---
The type of run is set by setting one of the following flags to `true`:  
`run`, `run_compare`, `compare_only`, or `get_flag_list`.

### Command-Line Options

| Option | Description |
|--------|-------------|
| `-f`   | Path to input LUA file |
| `-o`   | Path to bodies output file |
| `-z`   | Path to histogram output file |
| `-h`   | Path to histogram input file (used with `run_compare` only) |
| `-e`   | Seed |
| `-n`   | Number of threads to use for simulation |
| `-P`   | Print the percentage of progress of the simulation to standard output |
| `-u`   | Runs the visualizer (may require additional packages and compilation with OpenGL) |
| `-p`   | Simulation paramters list (6, 7, 8, 12, 13 or 14 arguments)

#### `-p` Options

- **Required 6 arguments:**  
  `[1] Forward Time, [2] Time Ratio, [3] Baryon Scale Radius, [4] Radius Ratio, [5] Baryon Mass, [6] Mass Ratio`
- **If 7 arguments:**  
  - If `manual_bodies = true`: `[7] Manual Bodies Input File`  
  - Else: `[7] LMC_mass`
- **If 8 arguments:**  
  `[7] LMC Mass, [8] Manual Bodies Input File`
- **If 12 arguments:**  
  `[7] l, [8] b, [9] r, [10] vx, [11] vy, [12] vz`
- **If 13 arguments:**  
  - If `manual_bodies = true`: `[13] Manual Bodies Input File`  
  - Else: `[13] LMC_mass`
- **If 14 arguments:**  
  `[13] LMC Mass, [14] Manual Bodies Input File`

For the ratio arguments `[4]` and `[6]`, ratios are `baryons/(baryons + dark matter)`.

#### Likelihood Comparison Flags

| Flag | Description |
|------|-------------|
| `-s` | Histogram to input for comparison. Will compare with EMD and cost components by default |
| `-S` | Adds beta dispersion to comparison |
| `-V` | Adds velocity dispersion to comparison |
| `-B` | Adds beta average to comparison |
| `-Q` | Adds line of sight velocity to comparison |
| `-U` | Adds proper motions to comparsion |
| `-L` | Adds momentum to comparison |

---

## Input Lua File Dwarf Model Options

### Double Component Model

- **Plummer:** `{mass, scaleLength}`
- **NFW:** `{mass, scaleLength[, rcut]}`  # rcut is an optional cutoff radius; ignored if not set
- **General Hernquist:** `{mass, scaleLength}`
- **Cored:** `{mass, scaleLength, r1, rc[, rcut]}` # rcut is an optional cutoff radius; ignored if not set
- **Single component King** `{mass, scaleLength, W0}` #scaleLength is the model's tidal radius (where density vanishes)

**The double component mixed dwarf code can be used as a single component dwarf generator.** 
To do this set the number of baryons equal to the total number of particles in your `.lua`, set the mass ratio to 1.0 in `run_nbody.sh`, set radius ratio to any number between but not including 0.0 and 1.0.
The parameters used will be that of the baryons. 

King model only works as single component for now since the density and potentials must be solved numerically and the current methods are too computationally expensive to allow double component. A future update will allow double component functionality for this model after it is made more efficient.

### Single Component Model

- **Plummer:** `{nbody, mass, scaleRadius, position, velocity, ignore, prng}`
- **NFW:** `{nbody, mass, rho_0, scaleRadius, position, velocity, ignore, prng}`
- **Hernquist:** `{nbody, mass, radius, a, position, velocity, ignore, prng}`

Only the plummer model is really useful since it can be calculated analytically. 

---

## N-Body CMAKE Flags

| Flag | Values | Description |
|------|--------|-------------|
| `DCMAKE_BUILD_TYPE`      | Debug, Release, RelWithDebInfo, MinSizeRel | Set to `Release` for a normal build. Other options include debugging information. |
| `DNBODY_DEV_OPTIONS`     | ON, OFF | Set to `ON` for developer options. `OFF` to use client-side parameter files. |
| `DNBODY_GL`              | ON, OFF | Builds the visualizer. Requires additional OpenGL packages. |
| `DBOINC_APPLICATION`     | ON, OFF | Cross-compile with BOINC. |
| `DSEPARATION`            | ON, OFF | Option for building the Separation code. Defaults to `OFF`. |
| `DDOUBLEPREC`            | ON, OFF | Enable double-precision floating point calculation. |
| `DNBODY_OPENMP`          | ON, OFF | Build the algorithm single-threaded (`OFF`) or multithreaded (`ON`). |
| `DNBODY_OPENCL`          | ON, OFF | Build with OpenCL libraries to support running N-Body on GPUs. |

## N-Body Units 

- Mass: Structure Mass Units (SMU)
- Distance: kiloparsec (kpc) 
- Time: Gigayear (Gyr)
- Velocity: kpc/Gyr
- Acceleration: kpc/Gyr<sup>2</sup>

Units Choosen such that:
- G = 1 kpc<sup>3</sup> · SMU<sup>-1</sup> · Gyr<sup>-2</sup>

Unit Conversions:
- 1 SMU = 222288.47 M<sub>☉</sub> 
- 1 kpc/Gyr = 0.97789439 km/s

Tests
---
  After building the client run
  ```
  $ ./build_test_env
  ```
  Tests can be run by running:
  ```
  $ make test
  ```
  However this runs all of the tests, which takes forever. You can run
  (from the tests directory) some core functionality tests with:
  ```
  $ make check
  ```
  Other tests  can be run with a certain number of bodies depending on
  how long you want to wait with:
  ```
  $ make test_${n}
  ```
  Currently n = 100, 1024, 10000 are available, but only n = 10000 are used.

  Single tests can be run with:
  ```
  $ ctest -R <Test_Name> 
  ```
  Get a more versbose output with:
  ```
  $ ctest -R <Test_Name> -VV
  ```
  If only 21  tests are running instead of 53 tests, you are missing libraries (check Step 0 for compiling N-body)

  **NOTE**: all `make` and `ctest` commands must be done under the `test_env` directory to work.

  Test results can be seen either in the terminal or under `test_env/Testing/Temporary/LastTest.log`. A consise list of failed test names can be seen under `test_env/Testing/Temporary/LastTestsFailed.log`.

Separation
---
- separation will do a separation after the integration if given an
  output file. There is also an argument to set the random number seed.

TAO
---
TODO: update for latest tao version

- Maximum Likelihood Evaluation Code for running milkyway separation program

- Note: Lua files for TAO searches are different from those used by the separation code.

- The terminal output from this program appears confusing since it mixes the output of each separation run with that of TAO.  Using the linux ">" operator to port output to a file only takes the TAO output, making it much clearer.

To run call:
```
  $ ./TAO <options>

  General required options:
    --separation "<path/to/separation_binary>"
    --stars "<path/to/stars_file>"
    --params "<path/to/search_paramaters_file>"
    --search_type <options>
      search type options:
        de    - differential evolution
        ps    - particle swarm
        snm   - synchronous newton method
        gd    - gradient descent
        cgd   - conjugate gradient descent
        sweep - paramater sweep

  Search Specific Options:
    de:
      optional:
        --population_size <int>         (default:200)
        --maximum_iterations <int>        (default:will run forever - Ctrl-C to kill)
        --maximum_created <int>         (default:will run forever - Ctrl-C to kill)
        --maximum_reported <int>        (default:will run forever - Ctrl-C to kill)
        --parent_scaling_factor <float>     (default:1.0)
        --differential_scaling_factor <float> (default:1.0)
        --crossover_rate <float>        (default:0.5)
        --int_pairs <int>           (default:1)
        --parent_selection <option>       (defualt:best)
          options:
            best
            random
            current-to-best
            current-to-random
        --recombination_selection <option>    (default:binary)
          options:
            binary
            exponential
            sum
            none
    ps:
      optional:
        --population_size <int>       (default:200)
        --maximum_iterations <int>      (default:will run forever - Ctrl-C to kill)
        --maximum_created <int>       (default:will run forever - Ctrl-C to kill)
        --maximum_reported <int>      (default:will run forever - Ctrl-C to kill)
        --inertia <float>         (default:0.75)
        --global_best_weight <float>    (default:1.5)
        --local_best_weight <float>     (default:1.5)
        --initial_velocity_scale <float>  (default:0.25)
    snm:
      required:
        --iterations <int>
      optional:
        --rand <double>     (randomizes the search parameters by +- the given percent)
    gd:
      required:
        --iterations <int>
      optional:
        --loop1_max <int>   (default:300 iterations)
        --loop2_max <int>   (default:300 iterations)
        --nquad <int>     (default:4 iterations for loop 3)
        --tol <double>      (default:1e-6 for tolerance of dstar in loop 3)
        --min_threshold <double_1, double_2, ... , double_n>
                    (default:line search will not quit if the input direction is very small)
        --rand <double>     (randomizes the search parameters by +- the given percent)

    gd:
      required:
        --iterations <int>
        --cgd_reset <int> **roughly speaking this should be the number of paramaters...
      optional:
        --loop1_max <int>   (default:300 iterations)
        --loop2_max <int>   (default:300 iterations)
        --nquad <int>     (default:4 iterations for loop 3)
        --tol <double>      (default:1e-6 for tolerance of dstar in loop 3)
        --min_threshold <double_1, double_2, ... , double_n>
                    (default:line search will not quit if the input direction is very small)
        --rand <double>     (randomizes the search parameters by +- the given percent)
```

Random notes:
---

 - All give usage with --help/-? arguments

make nbody_release and make separation_release will produce release
tarballs if git and xz are installed and found.

- Make sure when building with MSVC to set built to use Multithreaded
  (/MT) for the builds of the various libraries


---

## 6. wanderlodge
- **URL:** https://github.com/devtechedge/wanderlodge
- **Language:** TypeScript
- **Topics:** airbnb-clone, dark-mode, gemini, lodging, marketplace, nextjs, peer-to-peer, portfolio, react, tailwindcss, travel, typescript
- **Description:** Peer-to-peer lodge marketplace for subalpine cabins. Search sensory-scored stays, book as a traveler or host as a provider, then run a trip workspace with group expenses, cabin controls, and a wilderness log. Next.js 15, React, TypeScript. Vercel uses an in-memory JSON store (writes reset). Gemini optional. Demo marcus@wanderlodge.com / password123

### README.md

# WanderLodge

Peer-to-peer marketplace for subalpine cabins and lodges. Search sensory-scored stays, book as a traveler or host as a provider, then run a trip workspace with group expenses, in-stay cabin controls, and a wilderness log.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://wanderlodge-taupe.vercel.app)
[![CI](https://github.com/devtechedge/wanderlodge/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/wanderlodge/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://wanderlodge-taupe.vercel.app**

> **Status:** Portfolio demo. Listings and bookings live in an in-memory JSON store (`/tmp` on Vercel, so writes reset). Gemini herb/Q&A/adventure calls fall back to canned payloads when `GEMINI_API_KEY` is unset. Auth is an unsigned demo cookie, not JWT or NextAuth. Payments are simulated.

Demo accounts (password `password123`):

| Role | Email |
|------|-------|
| Traveler | `marcus@wanderlodge.com` |
| Provider | `evelyn@wanderlodge.com` |

This is the **only** public repo for the project.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="WanderLodge" width="800">
</p>

| Explore | Property |
|---------|----------|
| ![Lodge grid on the explore home](docs/screenshots/01-explore-lodges.png) | ![Property detail and booking card](docs/screenshots/02-property-detail.png) |

| Search | Trip workspace |
|--------|----------------|
| ![Search results with map](docs/screenshots/03-search-map.png) | ![Group coordination hub](docs/screenshots/04-trip-workspace.png) |

---

## Features

- Curated lodge grid with category chips, eco-score, and EV badges
- Search + map with amenity, price, guest, and sensory filters (decibel, astrophotography, solitude, fragrance-free)
- Traveler / provider demo auth with a one-click role switch
- Booking card: nights, 50% day-retreat, pantry upgrades, 30/70 deposit split
- Trip workspace: host chat, co-traveler expense split, in-stay cabin controls, wilderness log
- Optional Gemini botanist / concierge - mocked on the public demo

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 15 (App Router), React 19, TypeScript, Tailwind 4 |
| Motion | Motion (`motion/react`) |
| Data | JSON file store in `lib/db.ts` (not Prisma, not Mongo) |
| Auth | HttpOnly user-id cookie (`lib/session.ts`) - demo only |
| AI | Optional `@google/genai` with canned fallback |
| Hosting | Vercel |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/wanderlodge.git
cd wanderlodge
npm install
cp .env.example .env
npm run dev
```

Open **http://localhost:3000**. Gemini is optional.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: public passwords, unsigned session cookie, ephemeral JSON on Vercel. Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 7. vivid-pulse
- **URL:** https://github.com/devtechedge/vivid-pulse
- **Language:** TypeScript
- **Topics:** app-router, dark-theme, instagram-clone, nextjs, playwright, portfolio, react, social-network, tailwindcss, typescript, vercel, vitest
- **Description:** Neo-noir visual social network for digital creators. Photo feed with carousels, likes, bookmarks and threaded comments; 24-hour stories; discover search; DMs; and a cozy neighbors board. Next.js 15 App Router, TypeScript, Tailwind. In-memory Vercel demo (resets on cold start)ΓÇönot JWT or NextAuth. Demo login alex_vivid / password123. MIT licensed.

### README.md

# VividPulse

Neo-noir visual social network. A seeded photo feed, 24-hour stories, DMs, and a cozy neighbors board - built with Next.js 15.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://vividpulse-social.vercel.app)
[![CI](https://github.com/devtechedge/vivid-pulse/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/vivid-pulse/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://vividpulse-social.vercel.app**

Do **not** use https://vividpulse.vercel.app - that hostname is a different AI-automation product.

> **Status:** The public site is a **demo**. Auth is a signed `vp_session` cookie (not JWT / NextAuth). Posts, stories, and DMs live in **process memory** and reset on cold start. Seeded login: `alex_vivid` / `password123` (or the one-click ports on the login screen).

This is the **only** public repo for the project.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="Vivid Pulse" width="800">
</p>

| Login | Feed |
|-------|------|
| ![Sign in with seeded demo ports](docs/screenshots/01-login.png) | ![Stories tray and photo feed](docs/screenshots/02-feed.png) |

| Neighbors | Discover |
|-----------|----------|
| ![Cozy neighbors hub](docs/screenshots/03-neighbors.png) | ![Discover grid](docs/screenshots/04-discover.jpg) |

![Private chats](docs/screenshots/05-messages.png)

---

## Features

- Seeded creator network with one-click demo login
- Photo feed with carousels, likes, bookmarks, and threaded comments
- 24-hour stories tray and viewer
- Discover search over captions and locations
- Direct messages with polling
- Cozy Neighbors hub - vibes, bulletin notes, strolls, treats
- Session cookie is httpOnly + `SameSite=lax` (`secure` in production)

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| App | Next.js 15 (App Router), React 19, TypeScript |
| UI | Tailwind 4, Lucide, Motion |
| Data | In-memory store (`lib/db.ts`). SQL shape in `docs/schema.sql` |
| Auth | SHA-256 password hash + signed session cookie |
| Media | Mock `/api/upload` (data URLs). Feed images from picsum.photos |
| Hosting | Vercel |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/vivid-pulse.git
cd vivid-pulse
npm install
npm run dev
```

Open **http://localhost:3000** and sign in as `alex_vivid` / `password123`. No environment variables required.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: public password, committed fallback session secret, in-memory store. Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 8. pulse-work
- **URL:** https://github.com/devtechedge/pulse-work
- **Language:** TypeScript
- **Topics:** block-editor, dark-mode, focus-timer, kanban, nextjs, notion-clone, portfolio, productivity, react, tailwindcss, typescript, workspace
- **Description:** Pulse Workspace is a block-based notes and collections OS for students and makers: slash-command editor, Kanban/table/calendar/Gantt views, ΓîÿK spotlight, flashcards, habits, and a 25-minute timer with procedural ambient noise. Next.js 15, React 19, Tailwind 4, Fira Code. Client-side demo ΓÇö in-memory state, no auth; billing screens simulated. MIT.

### README.md

# Pulse Workspace

Block-based workspace for notes, collections, and deep work. A slash-command editor, Kanban / table / calendar / Gantt views, ⌘K spotlight, flashcards, habits, and a focus timer with procedural ambient noise.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://pulse-work-indol.vercel.app)
[![CI](https://github.com/devtechedge/pulse-work/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/pulse-work/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://pulse-work-indol.vercel.app**

> **Status:** Portfolio demo. Notebooks, collections, habits, and the timer live in **React client memory** and reset on refresh. There is no auth backend. Billing screens are simulated (`alert()`). No Gemini key is required.

This is the **only** public repo for Pulse Workspace.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="Pulse Workspace" width="800">
</p>

| Launchpad | Editor |
|-----------|--------|
| ![Dark launchpad with pinned pages](docs/screenshots/01-launchpad.png) | ![Slash-command notebook editor](docs/screenshots/02-editor.png) |

| Collections | Focus timer |
|-------------|-------------|
| ![Kanban board of deliverables](docs/screenshots/03-kanban.png) | ![Pomodoro timer with ambient noise](docs/screenshots/04-focus.png) |

---

## Features

- Launchpad with pinned pages, deliverables, and habit chips
- Block editor with slash commands, covers, and version-history chrome
- Collections that share one dataset across Kanban, table, calendar, Gantt, and gallery
- ⌘K spotlight search over notebook titles
- Focus timer (25 / 5 / 15) with Web Audio white / pink / brown noise
- Flashcards, habit week grid, mind map, templates, trash
- Light / dark Fira Code shell

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| App | Next.js 15 (App Router), React 19, TypeScript |
| UI | Tailwind 4, Lucide, Fira Code |
| Data | In-memory React context (`context/WorkspaceContext.tsx`) |
| Audio | Web Audio API (procedural noise, no samples) |
| Hosting | Vercel |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/pulse-work.git
cd pulse-work
npm install
npm run dev
```

Open **http://localhost:3000**. No environment variables required.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: no auth, in-memory client store, simulated billing. Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 9. polygot
- **URL:** https://github.com/devtechedge/polygot
- **Language:** TypeScript
- **Topics:** ai, gemini, language-learning, nextjs, portfolio, pronunciation, react, roleplay, spanish, speech-recognition, typescript, vercel
- **Description:** PolyGlot Live is a Spanish speaking lab for learners who want live roleplay, not flashcards. Pick a Madrid tapas bar, a Barcelona bike rental, or a Tokyo tech interview. Talk via mic or type, then get IPA, grammar toasts, vocab chips, and a fluency scorecard. Next.js 15, React 19, Gemini with canned demo fallback. Browser speech; no accounts. MIT.

### README.md

# PolyGlot Live

Spanish speaking lab for learners who want live roleplay, not flashcards. Order tapas in Madrid, rent a bike in Barcelona, or sit a tech interview - then get IPA, grammar toasts, and a fluency scorecard.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://polygot-snowy.vercel.app)
[![CI](https://github.com/devtechedge/polygot/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/polygot/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Gemini](https://img.shields.io/badge/Gemini-optional-4285F4?logo=google)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://polygot-snowy.vercel.app**

> **Status:** Portfolio demo. Scenario copy, hosts, and vocab ship in `lib/scenarios.ts`. `POST /api/chat` uses canned host replies unless `GEMINI_API_KEY` is set on the server. Speech uses the browser Web Speech API (Chrome / Edge). Type mode is the fallback. No accounts.

This is the **only** public repo for the project.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="PolyGlot Live" width="800">
</p>

| Passport hub | Briefing |
|--------------|----------|
| ![Mobile passport hub with three Spanish scenarios](docs/screenshots/01-passport-hub.png) | ![Tapas briefing with objectives and vocab](docs/screenshots/02-scenario-briefing.png) |

| Live HUD | Desktop studio |
|----------|----------------|
| ![In-call HUD with host avatar and transcript](docs/screenshots/03-live-hud.png) | ![Desktop marketing landing and studio CTA](docs/screenshots/04-desktop-landing.png) |

---

## Features

- Three Spanish roleplays: El Sol tapas (beginner), Barcelona bike rental (intermediate), Tokyo tech interview (advanced)
- Live HUD with host avatar, transcript, IPA line, and English gloss
- Grammar toasts on gender / conjugation slips (`un copa` → `una copa` in demo mode)
- Vocab chips, hint sheet, flashcards, and a post-call fluency scorecard
- Madrid vs Latin American dialect + 0.8× / 1.0× / 1.2× speech rate
- Mic or type. Public demo does not require a Gemini key

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 15 (App Router), React 19, TypeScript, Tailwind 4, Motion |
| Speech | Web Speech API (`SpeechRecognition` + `speechSynthesis`) |
| AI | Optional `@google/genai` (`gemini-2.5-flash`). Canned fallback in `lib/demo-chat.ts` |
| Data | Static scenario catalog - not Prisma, not a database |
| Auth | None |
| Hosting | Vercel |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/polygot.git
cd polygot
npm install
cp .env.example .env.local
npm run dev
```

Open **http://localhost:3000**. Gemini is optional.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: unauthenticated chat route, canned replies without a key, browser speech. Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 10. ai-news-agent
- **URL:** https://github.com/devtechedge/ai-news-agent
- **Language:** Python
- **Topics:** ai-agent, cron, feedparser, gemini, github-actions, google-gemini, llm, news-aggregator, python, rss, serverless, telegram-bot
- **Description:** Serverless daily AI news agent. GitHub Actions at 19:30 UTC fetches HN, arXiv cs.AI, Reddit r/MachineLearning, Google AI Blog, OpenAI News, and Hugging Face RSS, dedupes in-repo memory, summarizes with Gemini, and sends one Telegram executive brief. Python 3.11. No public web UI. Fork, add three Actions secrets, and the next run is yours.

### README.md

# <img src="docs/favicon.svg" width="36" height="36" alt="" /> AI News Agent

Serverless daily AI digest - GitHub Actions pulls public RSS, Gemini writes the brief, Telegram delivers it.

[![Live run](https://img.shields.io/badge/Live%20run-GitHub%20Actions-black?logo=githubactions&logoColor=white)](https://github.com/devtechedge/ai-news-agent/actions/workflows/daily_news.yml)
[![Daily agent](https://github.com/devtechedge/ai-news-agent/actions/workflows/daily_news.yml/badge.svg)](https://github.com/devtechedge/ai-news-agent/actions/workflows/daily_news.yml)
[![CI](https://github.com/devtechedge/ai-news-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/ai-news-agent/actions/workflows/ci.yml)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Live Demo

**[Daily workflow on GitHub Actions](https://github.com/devtechedge/ai-news-agent/actions/workflows/daily_news.yml)** - scheduled 19:30 UTC, plus manual `workflow_dispatch`.

> **Status:** This is a real scheduled backend, not a client-side mock. There is **no public web UI**. Gemini reads public RSS and writes one short daily brief of the important developments, sent to a **private Telegram chat**. Fork the repo, add three Actions secrets, and the next run is yours. `memory.json` in this public copy stores article hashes only.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.jpg" alt="AI News Agent" width="800">
</p>

| Pipeline | Telegram brief (sample layout) |
|----------|--------------------------------|
| ![Pipeline](docs/screenshots/01-pipeline.png) | ![Telegram brief](docs/screenshots/02-telegram-brief.png) |

| Schedule + memory |
|-------------------|
| ![Schedule](docs/screenshots/03-schedule-memory.png) |

---

## Features

- **Zero laptop, zero bill** - GitHub Actions + Gemini free tier + Telegram Bot API
- **Six public feeds** - HN (AI query), arXiv cs.AI, Reddit r/MachineLearning, Google AI Blog, OpenAI News, Hugging Face Blog
- **In-repo memory** - MD5 of `title|link|source` in `memory.json` so reruns skip duplicates
- **Important-only brief** - Gemini keeps models, launches, landmark research, policy, and big deals; skips recaps and noise
- **One Telegram message** - hard-capped under the Bot API length limit, never split into a thread
- **Rate-limit safe** - one Gemini call per run, 10 RPM cap, exponential backoff on 429, 50-article candidate ceiling
- **Fail-closed** - a Gemini or Telegram miss does **not** commit empty memory and does **not** report success

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Runtime | Python 3.11 on GitHub Actions |
| Feeds | `feedparser` + `requests` |
| Summarizer | `google-genai` · `gemini-3.6-flash` · thinking level `high` |
| Delivery | Telegram Bot API (plain text) |
| Memory | `memory.json` committed back to `main` |
| CI | GitHub Actions (`compileall` + pytest) |
| License | MIT |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/ai-news-agent.git
cd ai-news-agent
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python -m pytest
```

### Run locally (optional)

```bash
export GEMINI_API_KEY=...
export TELEGRAM_BOT_TOKEN=...
export TELEGRAM_CHAT_ID=...
python agent.py
# Telegram-only smoke:
TEST_TELEGRAM_ONLY=true python agent.py
```

### Wire the daily job

1. Create a Telegram bot via [@BotFather](https://t.me/BotFather) and note the token + chat id.
2. Create a Gemini key in [Google AI Studio](https://aistudio.google.com/app/apikey).
3. Repo **Settings → Secrets and variables → Actions** - add `GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
4. **Actions → Daily AI News Agent → Run workflow**. Cron is `30 19 * * *` (19:30 UTC).

Schedule, feeds, and RPM caps live in `.github/workflows/daily_news.yml` and `agent.py`.

---

## How it works

```
RSS feeds ──► filter / dedupe ──► Gemini (one brief) ──► one Telegram message
                    │                                        │
                    └──────── memory.json ◄──── commit ──────┘
```

Memory is written only after a non-empty summary **and** a successful Telegram send. CI never calls Gemini.

Threat model: [`SECURITY.md`](SECURITY.md).

---

## License

MIT. See [LICENSE](LICENSE).


---

## 11. devtechedge
- **URL:** https://github.com/devtechedge/devtechedge
- **Language:** Not specified
- **Topics:** None
- **Description:** GitHub profile landing for Devayan Mandal (DevTechEdge): AI/ML and full-stack work across agentic systems, marketplaces, and polished Next.js demos. Index of public repos with live Vercel and GitHub Pages links. Python, TypeScript, React, Next.js, LangGraph, Postgres, Supabase. Portfolio README onlyΓÇöno app, no API keys, no backend. Account home. v1

### README.md

# Hi, I'm Dev 👋

### Full Stack AI Native Engineer · Open Source Contributor

I build production-grade AI and full-stack systems and contribute fixes upstream across AI, developer tooling, distributed systems, and Web3 infrastructure.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178B9?style=for-the-badge&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Docker](https://img.shields.io/badge/Docker-2496DB?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF6E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org)
[![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai)
[![ChatGPT 5.6](https://img.shields.io/badge/ChatGPT_5.6-74AA9C?style=for-the-badge&logo=openai&logoColor=white)](https://chatgpt.com)
[![Grok 4.6](https://img.shields.io/badge/Grok_4.6-111111?style=for-the-badge&logo=x&logoColor=white)](https://x.ai/)
[![GLM 5.3](https://img.shields.io/badge/GLM_5.3-4C6FFF?style=for-the-badge&logo=zhipu&logoColor=white)](https://z.ai/)
[![Kimi K3](https://img.shields.io/badge/Kimi_K3-111111?style=for-the-badge&logo=moonshot&logoColor=white)](https://www.moonshot.ai/)

---

## 🌍 Open Source Engineering

**[OSS Contributions](https://github.com/devtechedge/oss-contributions)** tracks my upstream open-source contributions across developer tooling, databases, infrastructure, SDKs, and Web3, with clear provenance.

### Merged:

<!-- ledger:profile-merged:start -->
<img src="https://github.com/anza-xyz.png?size=48" width="32" height="32" alt="Anza" align="left" /> **[Anza Kit #2032](https://github.com/anza-xyz/kit/pull/2032)** - corrected the `getPatternMatchCodec` advanced guide to match current codec typing.

<img src="https://github.com/better-auth.png?size=48" width="32" height="32" alt="Better Auth" align="left" /> **[Better Auth #11208](https://github.com/better-auth/better-auth/pull/11208)** - added regression coverage for missing OpenAPI `requestBody` generation after a Zod intersection.

<img src="https://github.com/biomejs.png?size=48" width="32" height="32" alt="Biome" align="left" /> **[Biome #11667](https://github.com/biomejs/biome/pull/11667)** - added the `useBetterDomTraversing` nursery lint rule with safe transformations where semantics permit.

<img src="https://cdn.simpleicons.org/node.js/339933" width="32" height="32" alt="Node.js" /> **[node-postgres #3772](https://github.com/brianc/node-postgres/pull/3772)** - fixed `Connection.sync()` incorrectly setting the internal `_ending` flag, preventing false suppression of subsequent socket errors.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14753](https://github.com/pnpm/pnpm/pull/14753)** - fixed `lockfile: false` being ignored during automatic package-manager switching.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14754](https://github.com/pnpm/pnpm/pull/14754)** - fixed non-recursive pattern runs with `--no-bail` so matching scripts continue executing and failures are aggregated correctly.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14756](https://github.com/pnpm/pnpm/pull/14756)** - preserved existing dependency range operators and protocol prefixes during `pnpm update`.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14863](https://github.com/pnpm/pnpm/pull/14863)** - fixed startup crashes on FreeBSD and other non-Windows Unix-like platforms by making default_store_dir use the Unix fallback path, with platform-specific regression coverage.

<img src="https://github.com/pytest-dev.png?size=48" width="32" height="32" alt="pytest-env" align="left" /> **[pytest-env #262](https://github.com/pytest-dev/pytest-env/pull/262)** - documented that pytest.toml and .pytest.toml accept the native [pytest] env table, not only the plugin-specific [pytest_env] section.

<img src="https://github.com/recharts.png?size=48" width="32" height="32" alt="Recharts" align="left" /> **[Recharts #7805](https://github.com/recharts/recharts/pull/7805)** - removed `tabIndex={-1}` from z-index portal SVG `<g>` layers so empty groups are not pointer-focusable and WebKit does not draw geometry-traced focus rings; added regression coverage asserting no layer carries a `tabindex` attribute.

<img src="https://github.com/web-infra-dev.png?size=48" width="32" height="32" alt="Rspress" align="left" /> **[Rspress #3678](https://github.com/web-infra-dev/rspress/pull/3678)** - fixed search initialization racing ahead of asynchronous FlexSearch indexing by awaiting all `addAsync()` operations before initialization resolves, preventing early queries from incorrectly returning no results on larger sites.

<img src="https://github.com/SQLMesh.png?size=48" width="32" height="32" alt="SQLMesh" align="left" /> **[SQLMesh #6040](https://github.com/SQLMesh/sqlmesh/pull/6040)** - fixed a concurrency race in `sqlmesh test` involving `time_machine` and worker threads.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2849](https://github.com/stellar/stellar-docs/pull/2849)** - reworked the Soroban address conversion example to propagate the fallible `Result<Address, ConversionError>` from `Address::from_xdr()` instead of calling `.unwrap()`, which panics on malformed XDR, and noted that contracts consuming XDR from untrusted sources must handle the error instead of aborting.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2850](https://github.com/stellar/stellar-docs/pull/2850)** - documented Quickstart's undocumented `--enable-core-manual-close` flag in the advanced usage docs. The Operation Modes page now covers the flag, the `MANUAL_CLOSE` setting it writes into the generated `etc/stellar-core.cfg`, and triggering a close through the `manualclose` endpoint on port 11626, while Run Commands adds macOS, Linux, and Windows startup examples that bind the admin port to loopback. The new section also records two limits readers hit in practice: the flag is accepted on every network but only usable on local, because stellar-core checks `NODE_IS_VALIDATOR` when `manualclose` is invoked and only the local config sets it, and each invocation advances exactly one ledger.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2851](https://github.com/stellar/stellar-docs/pull/2851)** - qualified the dapp frontend guide's blanket claim that Freighter requires HTTPS; `http://localhost` and `http://127.0.0.1` are already Potentially Trustworthy origins under the W3C Secure Contexts specification, so plain HTTP on loopback satisfies the requirement and local development needs no TLS.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2853](https://github.com/stellar/stellar-docs/pull/2853)** - reconciled contradictory memo guidance in the pooled accounts guide: the intro framed memos as obsolete while later sections still required supporting them, so memos now read as the legacy mechanism still in active use and muxed accounts as preferred going forward.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2859](https://github.com/stellar/stellar-docs/pull/2859)** - added the --enable-core-manual-close flag to the Local section of the Network Modes page, so the parameter list no longer omits a flag the quickstart container ships, with a cross-link to the Manual close mode section noting that only the local configuration sets NODE_IS_VALIDATOR.

<img src="https://github.com/thirdweb-dev.png?size=48" width="32" height="32" alt="thirdweb" align="left" /> **[thirdweb JS #8938](https://github.com/thirdweb-dev/js/pull/8938)** - fixed `useTokenQuery` collapsing real token lookup failures into `unsupported_token` instead of using the existing error/retry path.

<img src="https://github.com/ssf0409.png?size=48" width="32" height="32" alt="tracelens" align="left" /> **[tracelens #140](https://github.com/ssf0409/tracelens/pull/140)** - markdown table cells in the report generator are now escaped with html.escape in addition to pipe and newline handling. Task ids or gate values containing pipes, line breaks, or HTML metacharacters no longer break the per-task and baseline-gate tables piped into $GITHUB_STEP_SUMMARY, and no cell can open a raw HTML element.
<!-- ledger:profile-merged:end -->



---

## 🚀 Flagship Architectures & Projects

- 🔬 **[Synthesis](https://synthesis-gold.vercel.app/)** - autonomous multi-agent research with planning, research, synthesis, critique, HITL gates, RAG, Reflexion, and live SSE agent graphs ([repo](https://github.com/devtechedge/synthesis)).
- 💼 **[Jobrow](https://jobrow.vercel.app)** - live register of still-open US tech roles sourced from employer ATS boards, with search, filters, closed-role tracking, and a public JSON API ([repo](https://github.com/devtechedge/job-board)).
- ⛓️ **[Lattice](https://lattice-devtechedge1.vercel.app)** - Web3 jobs platform aggregating blockchain and crypto roles with salary observatory, talent directory, gigs, and hiring intelligence ([repo](https://github.com/devtechedge/lattice)).
- 🪐 **[Pulsar](https://devtechedge.github.io/pulsar/)** - decentralized AI compute protocol interface with Base smart contracts, staking flows, wallet connectivity, 3D visualization, tokenomics, and Foundry-tested contracts ([repo](https://github.com/devtechedge/pulsar)).
- 🧠 **[AAROP](https://aarop.vercel.app)** - explicit Perceive → Plan → Act → Observe → Reflect → Adapt loop with self-verification, bounded autonomy, and replayable traces ([repo](https://github.com/devtechedge/aarop)).
- ⚖️ **[RegTrace](https://regtrace-ai.vercel.app)** - HITL Web3 compliance copilot mapping packs onto MiCA/VARA with retrieval-bounded findings and article citations ([repo](https://github.com/devtechedge/regulatory_compliance)).
- 🏥 **[Cadence](https://cadence-healthcare.vercel.app/)** - deep-memory healthcare agent lab with layered patient memory, journey stages, and consent-scoped clinician briefs ([repo](https://github.com/devtechedge/healthcare-deep-memory-agents)).
- 🔎 **[Veritas](https://veritas-engine-woad.vercel.app)** - LangGraph research agent with SSE streaming, grounded demo mode, and external retrieval when configured ([repo](https://github.com/devtechedge/veritas-engine)).
- 🔥 **[Chaos Simulator](https://chaos-simulation.vercel.app)** - real-time chaos engineering dashboard with fault injection, self-healing services, animated service topology, scenario orchestration, telemetry, and recovery analysis ([repo](https://github.com/devtechedge/chaos-simulator)).

---

## 🛠️ Tech Stack

| Category | Tooling, Frameworks & Architecture |
| :--- | :--- |
| **AI systems & agents** | Python, LangGraph, LangChain, LangServe, FastAPI, explicit agentic state machines, multi-agent supervisors, HITL interrupts, bounded autonomy, Reflexion / critique loops, tool-use / ReAct, durable checkpoints |
| **RAG, memory & evaluation** | Hybrid RAG, pgvector, BM25, TF-IDF, JSONB embeddings, cosine retrieval, sentence-transformers, long-term memory, retrieval-bounded generation, eval gates, LLM-as-judge, LangSmith |
| **LLMs, tools & integrations** | Gemini, OpenAI-compatible providers, Groq, Ollama / local LLMs, Tavily, Telegram Bot API, MCP-oriented tool buses, Google Workspace integrations |
| **Frontend & product** | TypeScript, React, Next.js, TanStack Start, Vite, Tailwind CSS, shadcn/ui, Lucide, Motion / Framer Motion, Recharts, Three.js, React Three Fiber, HTML5 Canvas, SVG |
| **Data, auth & backend** | PostgreSQL, Supabase, Neon, PGLite, SQLite, Prisma, Drizzle ORM, SQLAlchemy, Pydantic, Zod, Better Auth, REST, Server Actions, API routes |
| **Realtime & observability** | SSE, WebSockets, Socket.io, replayable traces, structured telemetry, OpenTelemetry-shaped tracing, live/demo provider switching |
| **Web3 & smart contracts** | Solidity, OpenZeppelin, Foundry, Base, viem, wagmi, RainbowKit, ethers.js, wallet SDKs, blockchain / wallet infrastructure |
| **Infrastructure & testing** | Node.js, Bun, Express, Docker, Vercel, GitHub Actions, Vitest, pytest, Playwright, TypeScript compiler, Biome, security hardening and threat-model documentation |

---

## 🎯 Engineering Philosophy

Bounded, observable AI systems with validated retrieval, explicit state, cost-aware routing, and human oversight.  
Improve infrastructure upstream, with reproducible engineering and strict OSS provenance.

---

## 🌐 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dev-ma/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/devtechedge)

---


---

## 12. chaos-simulator
- **URL:** https://github.com/devtechedge/chaos-simulator
- **Language:** TypeScript
- **Topics:** bun, chaos-engineering, dashboard, framer-motion, full-stack, microservices, nextjs, observability, realtime, recharts, self-healing, socket-io, typescript
- **Description:** Chaos Simulator is a real-time chaos-engineering dashboard: self-healing microservices, animated SVG topology, particle effects, scenario builder, and live telemetry charts. Next.js 16, Bun, TypeScript, Framer Motion, Recharts. Public Vercel is client-side simulationΓÇöno backend. Chaos injection, healing, latency, and event stream run in-browser.

### README.md

# 🔥 Chaos Simulator

Real-time chaos engineering dashboard with self-healing microservices, animated SVG topology, particle effects, scenario builder, and live telemetry.

[![CI](https://github.com/devtechedge/chaos-simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/chaos-simulator/actions/workflows/ci.yml)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://chaos-simulation.vercel.app)
[![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Bun](https://img.shields.io/badge/Bun-1.x-fbf0df?logo=bun)](https://bun.sh/)
[![Socket.io](https://img.shields.io/badge/Socket.io-4.8-black?logo=socket.io)](https://socket.io/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-06b6d4?logo=tailwindcss)](https://tailwindcss.com/)
[![Framer Motion](https://img.shields.io/badge/Framer%20Motion-12-black)](https://www.framer.com/motion/)
[![Recharts](https://img.shields.io/badge/Recharts-2-orange)](https://recharts.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://chaos-simulation.vercel.app**

> **Status:** The live site is a full **client-side simulation** (no backend, no paid host). Chaos injection, self-healing, scenarios, latency charts, and the event stream all run in the browser. A Bun + Socket.io engine lives in this repo for **local** use only - it is not exposed on Vercel.

This is the **only** public repo for the project.

---

## Screenshots

### Dashboard Overview
![Dashboard with live topology, latency chart and toast notifications](docs/screenshots/01-dashboard-overview.png)

### Chaos Scenario Builder
![Multi-step Scenario Builder with presets](docs/screenshots/02-scenario-builder.png)

### Live Controls & Event Stream
![Disaster controls, targeted injection and live event stream](docs/screenshots/03-controls-and-stream.png)

### Anomaly Timeline
![Filterable anomaly history with recovery times](docs/screenshots/04-anomaly-timeline.png)

---

## Features

- **3 mock microservices** (Auth, Payment, Inventory) with live health, latency, and request volume
- **Automated chaos injector** - 500 errors, latency spikes, and service crashes every 30 s
- **Self-healing recovery** - services restore themselves within 8–15 seconds
- **Animated SVG topology** with particle data flow and health-based pulse rings
- **Canvas particle bursts + synthesized sound** on every critical event
- **Multi-step Scenario Builder** with presets (Black Friday, Cascading Failure, etc.)
- **Real-time latency chart** (60 s window) and filterable anomaly timeline
- **Manual injection controls** and a network-partition button

---

## Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | Next.js 16, React 19, TypeScript, Tailwind 4, shadcn/ui |
| Animation    | Framer Motion 12, Canvas particles |
| Charts       | Recharts |
| Demo mode    | Client-side simulation on Vercel |
| Local engine | Bun + Socket.io (not public) |
| CI           | GitHub Actions - unit, `tsc`, Playwright |
| Package mgr  | Bun |

---

## Architecture

**Public demo (Vercel)** uses `useChaosEngine` in the browser. No paid backend.


```
Vercel / Demo                         Local only
┌─────────────────────────┐         ┌──────────────────────────┐
│ Next.js dashboard       │         │ Chaos Engine (Bun :3030) │
│ + useChaosEngine        │         │ + 3 mock services        │
│ (client simulation)     │         └──────────────────────────┘
└─────────────────────────┘
```

---

## Quality

| Check | How |
|-------|-----|
| Unit tests | Validation, simulation transitions, Scenario Builder presets |
| Types | `ignoreBuildErrors` is **off** - `bun run typecheck` |
| E2E | Playwright: dashboard, Scenario Builder, 500 inject, partition |
| CI | [GitHub Actions](https://github.com/devtechedge/chaos-simulator/actions) on every push to `main` |
| Supply chain | Unused template packages removed; Dependabot weekly (**patch/minor only** - do not merge majors blindly) |

```bash
bun install
bun run test
bun run typecheck
bunx playwright install chromium
bun run test:e2e
```

---

## Security

Portfolio demo: **no user login** on the public site. The browser simulation cannot reach other users.

The local Bun engine allow-lists service names and anomaly types, caps scenario payloads, and reads `CORS_ORIGIN` from the environment. **Do not bind port 3030 to the internet** without auth and a locked origin.

Details: **[SECURITY.md](SECURITY.md)**.

---

## Quick Start (demo - same as Vercel)

```bash
bun install
bun run dev
```

Open **http://localhost:3000**.

---


## License

MIT License. See [LICENSE](LICENSE).


---

## 13. luxe-tracker
- **URL:** https://github.com/devtechedge/luxe-tracker
- **Language:** TypeScript
- **Topics:** arbitrage, client-side, dashboard, editorial-ui, fashion-tech, luxury-retail, nextjs, portfolio, recharts, tailwindcss, typescript, price-disparity
- **Description:** Luxe Tracker is a high-fashion global launch and price-disparity dashboard for Prada, Gucci, Balenciaga, Louis Vuitton, and Versace. 17 intelligence panels, 5 maisons, 5 regions, 11k+ price rows: arbitrage, FX hedge, landed-cost optimizer, brand pulse. Next.js 15, Tailwind 4, Recharts. Pure client-side deterministic snapshotΓÇöno env vars, no backend

### README.md

# Luxe Tracker

High-fashion global launch & price disparity tracker for Prada, Gucci, Balenciaga, Louis Vuitton and Versace. 17 intelligence panels across 5 regions with arbitrage detection, FX hedge calculator, landed-cost optimizer and brand pulse.

![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)
![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-06b6d4?logo=tailwindcss)
![Recharts](https://img.shields.io/badge/Recharts-2-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Live Demo

**https://luxe-disparity-tracker.vercel.app/**

Pure client-side deterministic snapshot (seeded PRNG). Zero environment variables, always green. Data shape matches a full Prisma + Supabase backend but runs entirely in the browser.

## Screenshots

### Overview - Live Telemetry
![Overview](docs/screenshots/01-overview.png)

### Price Disparity Matrix
![Price Matrix](docs/screenshots/02-price-matrix.png)

### Arbitrage Opportunity Finder
![Arbitrage](docs/screenshots/03-arbitrage.png)

### Competitive Brand Comparison
![Competitive Matrix](docs/screenshots/04-competitive-matrix.png)

### Sustainability Scores
![Sustainability](docs/screenshots/05-sustainability.png)

## Features

- **Live Telemetry Overview** - editorial hero number, 8-column KPI strip, FX rates, region & brand markup charts
- **Price Disparity Matrix** - sortable 5-region matrix with EUR baseline, duties, taxes and landed cost
- **Launch Calendar** - 90-day rolling grid of regional drops with status badges
- **Arbitrage Opportunity Detector** - net profit after duties, taxes and shipping per region pair
- **Landed-Cost Optimizer** - cheapest buying region recommendation per SKU
- **Price History & Anomaly Flags** - 90-day time series with >3 % daily move detection
- **FX Volatility Hedge Calculator** - 90-day FX history + what-if revaluation
- **Brand Pulse Radar** - 5-dimensional prestige / hype / scarcity / FX risk / resale score
- **Stock-Out Risk Index** - sell-out probability from inventory × hype × days-to-launch
- **Competitive Matrix, Runway Tracker, VIP Tier Simulator, Sustainability, Trend Forecast, Drop Queue, Watchlist & Alerts**

## Tech Stack

| Layer | Choice |
|-------|--------|
| Framework | Next.js 15 (App Router) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 4 (CSS-first `@theme`) |
| Charts | Recharts 2 |
| Icons | Lucide React |
| Theme | Custom dark / light with zero-FOUC bootstrap |
| Data | Deterministic in-browser snapshot (mulberry32 PRNG) |

## Quick Start

```bash
git clone https://github.com/devtechedge/luxe-tracker.git
cd luxe-tracker
bun install          # or: npm install
bun run dev          # → http://localhost:3000
```

No environment variables required.

## Tests & CI

```bash
bun test              # unit: snapshot counts, telemetry, price-history key split, VIP, validation
bun run typecheck
bun run test:e2e      # Playwright Chromium - overview, Price Matrix nav, theme toggle
```

GitHub Actions runs unit + typecheck + e2e on every push to `main`. Dependabot opens weekly PRs for patch/minor npm and Actions updates (majors ignored).

## Security

See [SECURITY.md](./SECURITY.md). Public demo has no backend, no env vars, and no auth boundary. Watchlist / alerts / spend in `localStorage` are allow-listed on read.

## Architecture

Single Vercel deployment. All analytics are pure functions over a seeded in-memory snapshot (`src/lib/data-snapshot.ts` + `src/lib/analytics.ts`). Watchlist and alerts persist in `localStorage`. Dark/light theme is controlled by a no-flash inline script + CSS variables.

The same data shape was previously backed by Prisma + Supabase; the client-side version keeps the full panel surface while guaranteeing a permanent green live demo.

## License

MIT License. See [LICENSE](./LICENSE) for details.

---

Brand names and prices are synthetic and used for demonstration only. Trademarks belong to their respective owners.


---

## 14. pulsar
- **URL:** https://github.com/devtechedge/pulsar
- **Language:** TypeScript
- **Topics:** base-chain, decentralized-ai, erc20, foundry, framer-motion, nextjs, rainbowkit, recharts, solidity, staking, typescript, web3
- **Description:** Decentralized AI compute marketplace on Base. Pay $PULSAR for inference; earn by supplying GPU. Next.js site with a 3D neutron-star hero, staking UI, tokenomics, RainbowKit wallet connect, plus Foundry ERC-20 and staking contracts. GitHub Pages uses mock dataΓÇöcontracts are audit-ready but not deployed to Base (pre-TGE). TypeScript, Framer Motion.

### README.md

<div align="center">

# <img src="public/pulsar.svg" width="48" height="48" alt="Pulsar logo" /> PULSAR

**The signal layer for decentralized AI compute**

Pay `$PULSAR` to run AI inference. Earn by supplying GPU power. Deflationary by design.

[![CI](https://github.com/devtechedge/pulsar/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/pulsar/actions/workflows/ci.yml)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-black?logo=github)](https://devtechedge.github.io/pulsar/)
[![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Solidity](https://img.shields.io/badge/Solidity-0.8.24-363636?logo=solidity)](https://soliditylang.org/)
[![Base](https://img.shields.io/badge/Base-8453-0052FF?logo=coinbase)](https://base.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

</div>

## Live Demo

**https://devtechedge.github.io/pulsar/**

> **Status:** Frontend + client-side Web3 is live. Smart contracts are audit-ready but not yet deployed to Base (pre-TGE). The UI uses realistic mock data and wallet-connect flows so the product experience is fully reviewable today.

## Screenshots

| Hero + 3D neutron star | How it works |
|:---:|:---:|
| ![Hero](docs/screenshots/Screenshot%202026-07-27%20042906.png) | ![How it works](docs/screenshots/Screenshot%202026-07-27%20042925.png) |

| Tokenomics | Live network pulse |
|:---:|:---:|
| ![Tokenomics](docs/screenshots/Screenshot%202026-07-27%20042931.png) | ![Network](docs/screenshots/Screenshot%202026-07-27%20042955.png) |

## Features

- **3D hero** - React Three Fiber neutron star with polar jets, accretion disk, and animated pulse rings
- **Wallet connect** - wagmi v3 + RainbowKit on Base (mainnet + Sepolia fallback)
- **Staking dashboard** - full approve → stake → unstake → claim flow with live APY reads
- **Tokenomics visuals** - Recharts allocation donut, vesting bars, animated burned-supply counter
- **Live network pulse** - simulated job feed, supplier map, latency & volume KPIs
- **Trust primitives** - Basescan verification hooks, UNCX lock proof, Gnosis Safe, KYC badge
- **Smart contracts** - `Pulsar.sol` (fixed 1B supply, tax + burn) + `PulsarStaking.sol` (Foundry + 14 tests)

## Tech Stack

| Layer | Tech |
|-------|------|
| Framework | Next.js 16 (App Router) + TypeScript |
| Styling | Tailwind CSS 4 + shadcn/ui |
| 3D / Motion | three.js + @react-three/fiber + Framer Motion |
| Charts | Recharts |
| Web3 | wagmi v3 + viem + RainbowKit |
| Contracts | Solidity 0.8.24 + OpenZeppelin + Foundry |
| Chain | Base (8453) |

## Quick Start

```bash
bun install
bun run dev          # → http://localhost:3000

# Optional - contracts
cd contracts
forge install OpenZeppelin/openzeppelin-contracts --no-commit
forge build && forge test -vv
```

Copy `.env.example` → `.env.local` and fill the four public vars when you are ready to point the UI at a live contract address.

```bash
bun run test          # unit tests (format, mock data, address guards)
bun run typecheck
bun run test:e2e      # Playwright Chromium smokes
```

See [`SECURITY.md`](./SECURITY.md) for the threat model.

## Smart Contracts

See [`contracts/`](./contracts) for the full Foundry project, ABIs, deployment scripts, and audit notes. Deployment guide: [`DEPLOY.md`](./DEPLOY.md).

## License

MIT - see [LICENSE](./LICENSE).


---

## 15. unit-fix
- **URL:** https://github.com/devtechedge/unit-fix
- **Language:** Python
- **Topics:** None
- **Description:** Single-turn Python repair RL environment: patch a small function so hidden unit tests pass. Sandboxed exec grader for Prime Intellect Environments Hub.

### README.md

# unit-fix

Single-turn **Python repair** for RLVR / evals on the [Prime Intellect Environments Hub](https://app.primeintellect.ai/dashboard/environments).

Hub: [devtechedge/unit-fix](https://app.primeintellect.ai/dashboard/environments/devtechedge/unit-fix) · Source: [github.com/devtechedge/unit-fix](https://github.com/devtechedge/unit-fix)

A third environment next to [calendar-math](https://github.com/devtechedge/calendar-math) (datetime gold) and [meeting-slot](https://github.com/devtechedge/meeting-slot) (multi-turn tools). This one is **code**: a small broken function plus a failing unit test. The model puts a patched function in `<answer>` tags. The grader execs the tests in a stdlib sandbox - no LLM-as-judge, no source-string match on the main reward.

| Family | Bug the eval edge exists to catch |
| --- | --- |
| `nth_item` | 1-based indexing, uses `items[n]` |
| `sum_through` | `range` exclusive of `hi` |
| `mean_or_none` | empty list divides by zero |
| `codepoint_count` | UTF-8 bytes, not code points |
| `with_item` | mutates the input list |
| `closed_slice` | Python slice drops the end index |
| `rotate_left` | `n % len([])` crashes |
| `safe_ratio` | no zero-denominator guard |
| `window_count` | fencepost: `n-k` instead of `n-k+1` |
| `same_letters` | `str.lower` misses `ß → ss` |
| `field_count` | `split(" ")` misses NBSP / unicode whitespace |
| `unique_keep_order` | `sorted(set)` loses first-seen order |
| `clamp` | closed interval treated as `hi-1` |
| `chunks` | drops the remainder chunk |
| `first_index` | returns last match, not first |

## Why this design

- **Verifiable.** Gold answers are in-repo repairs. Dataset construction **executes** gold (must pass) and the original function (must fail).
- **Behavioral exact, not AST match.** Any repair that passes the hidden tests scores 1.0 on the main term. Hardcoding the visible example does not.
- **Hard where it matters.** Eval is 15 curated edges: off-by-one, empty list, unicode, mutation vs copy, inclusive/exclusive slice.
- **Not gameable by format alone.** Format is a 0.2 bonus. Exact match is the 1.0 term (all tests pass).
- **Shaping, not noise.** Visible tests pass but a hidden test still fails → 0.5 partial credit. Naive echo of the original function never gets there.
- **Sandbox.** AST gate (no imports, no dunders, no I/O), capped `range`/`sum`, `sys.settrace` step + wall-clock limit. No subprocess, so Hub CI does not fork.
- **Configurable.** `num_train_examples`, `num_eval_examples`, `seed`, optional `family` / `difficulty` pin.

## Reward

```
reward = 1.0 * exact_match + 0.2 * format + 0.2 * partial_credit
```

| Term | 1.0 when | Notes |
| --- | --- | --- |
| `exact_match` | every test (visible + hidden) passes | behavioral; source need not match gold |
| `format` | `<answer>...</answer>` present with a body | extra prose outside the tags is ignored; markdown fences inside are stripped |
| `partial_credit` | every **visible** test passes, a hidden test fails | 0.5; 0 when exact already fired, so a perfect answer is **1.2** not 1.4 |

## Eval

15 curated edge cases (`num_eval_examples=15`, 1 rollout each).

| Policy | avg reward | exact | format | partial |
| --- | --- | --- | --- | --- |
| Gold repair (ceiling) | **1.200** | 1.000 | 1.000 | 0.000 |
| Naive (echo original function) | **0.200** | 0.000 | 1.000 | 0.000 |

The gold policy is a harness check: install, `load_environment`, the sandbox, and the rubric all fire 1.2. The naive policy is a discrimination check: returning the prompt's broken function does not rubber-stamp 1.2 - it fails a visible test on every eval edge, so it never collects partial credit either.

Model row pending a fresh OpenRouter key (`minimax/minimax-m2.7`, T=0, 2048 tok, `--max-concurrent 1`).

```bash
uv run vf-eval unit-fix -n 15 -r 1 -p openrouter \
  -m minimax/minimax-m2.7 --max-tokens 2048 \
  --temperature 0 --max-concurrent 1 --disable-tui --disable-env-server
```

## Installation

```bash
uv pip install -e .
python -m pytest tests/test_unit_fix.py -q
```

From the Hub:

```bash
prime env install devtechedge/unit-fix
```

```python
import verifiers as vf

env = vf.load_environment("unit-fix")
```

Requires `verifiers>=0.1.14,<0.2`.

## `load_environment` arguments

| Arg | Default | Meaning |
| --- | --- | --- |
| `num_train_examples` | `500` | train split size |
| `num_eval_examples` | `100` | eval split size (15 edges prepended) |
| `seed` | `42` | train RNG; eval uses `seed + 1` |
| `family` | `None` | pin to one bug family, or mixed |
| `difficulty` | `None` | `"easy"` \| `"medium"` \| `"hard"` \| mixed |

```bash
uv run vf-eval unit-fix -n 20
uv run vf-eval unit-fix -a '{"family": "with_item", "num_eval_examples": 40}'
```

Dataset rows never use a column named `task`. Verifiers ≥0.1 treats `info["task"]` as a nested rollout payload. Nested tests are JSON-stringified before `Dataset.from_list`.

## Gold solution

Dataset construction **is** the gold solver. Each family has a buggy body and a repair in `FAMILY_IMPL`. `example_from_spec` runs both through the sandbox: gold must pass every test; the original must fail a visible test (so naive cannot farm partial).

```python
from unit_fix import run_tests, gold_completion, naive_completion, grade

run_tests(info["gold_code"], info["func_name"], info["tests"]).all_passed  # True
run_tests(info["buggy_code"], info["func_name"], info["tests"]).all_passed  # False

grade(gold_completion(info["gold_code"]), info["gold_code"], info)["reward"]  # 1.2
grade(naive_completion(info), info["gold_code"], info)["reward"]              # 0.2
```

`tests/test_unit_fix.py` asserts the 15 edges, the sandbox rejects `import os` / dunder escapes / `while True`, and a function that hardcodes the visible expected value scores 0.3 not 1.2.

## Files

```
unit_fix.py                 # generator, sandbox, grader, load_environment
pyproject.toml
README.md
LICENSE
tests/test_unit_fix.py
```

## What this is not

- Not a wrap of HumanEval, MBPP, or any public coding dataset.
- Not LLM-judged.
- Not multi-turn / tool-using (that's meeting-slot).
- Not calendar arithmetic (that's calendar-math).
- Not source-diff matching. Hidden tests are the spec.

## License

MIT


---

## 16. meeting-slot
- **URL:** https://github.com/devtechedge/meeting-slot
- **Language:** Python
- **Topics:** calendar, evaluation, llm-evaluation, prime-intellect, python, reinforcement-learning, rl, rlvr, scheduling, timezone, tool-use, verifiers
- **Description:** Multi-turn tool-using meeting scheduler RL environment for Prime Intellect: hidden calendars, timezone gold solver, exact+format+partial grader.

### README.md

# meeting-slot

Multi-turn **tool-using meeting scheduler** for RLVR / evals on the [Prime Intellect Environments Hub](https://app.primeintellect.ai/dashboard/environments).

Hub: [devtechedge/meeting-slot](https://app.primeintellect.ai/dashboard/environments/devtechedge/meeting-slot) · Source: [github.com/devtechedge/meeting-slot](https://github.com/devtechedge/meeting-slot)

A sequel to [calendar-math](https://github.com/devtechedge/calendar-math): same calendar domain, but the model has to **query tools** instead of reading the calendar out of the prompt.

The task is to find the **earliest valid UTC start** that works for every attendee. Busy intervals, working hours, and timezones are hidden. The final answer goes in `<answer>` tags as a UTC ISO-8601 timestamp, e.g. `2024-03-11T15:00:00Z`. If no slot exists, `NONE`.

The grader is a UTC sweep-line over `zoneinfo` - no LLM-as-judge, no fuzzy string match on the main reward.

| Tool | Returns |
| --- | --- |
| `list_attendees()` | JSON names |
| `get_timezone(name)` | IANA timezone |
| `get_working_hours(name)` | local `HH:MM` hours + weekdays (`0=Monday`) |
| `get_busy(name, date)` | local half-open busy intervals for that **local** date |

## Why this design

- **Verifiable.** Gold answers are produced by interval intersection in UTC. The same functions are the reference solver.
- **Tool use is load-bearing.** The world is not in the prompt. A model that does not call tools cannot solve the task.
- **Hard where it matters.** Eval always includes curated edge cases: US/EU DST, NY↔Kolkata no-overlap, Friday 16:30 vs Monday 09:00, 30 vs 60 minute gaps, four-person summer overlap, inclusive-busy traps.
- **Not gameable by format alone.** Format is a 0.2 bonus. Exact match is the 1.0 term.
- **Shaping, not noise.** A conflict-free in-hours start that is not the earliest scores 0.5 partial credit. Invalid overlap / wrong duration / outside hours score 0 on the main terms.
- **Configurable.** `num_train_examples`, `num_eval_examples`, `seed`, `max_turns`, optional `difficulty` pin.

## Reward

```
reward = 1.0 * exact_match + 0.2 * format + 0.2 * partial_credit
```

| Term | 1.0 when | Notes |
| --- | --- | --- |
| `exact_match` | parsed `<answer>` equals gold | UTC ISO with `Z`, or `NONE` |
| `format` | `<answer>...</answer>` present | extra prose outside the tags is ignored |
| `partial_credit` | valid-but-not-earliest | 0.5; 0 when exact match already fired, so a perfect answer is **1.2** not 1.4 |

Intervals are half-open `[start, end)`. A busy block ending at 11:00 means 11:00 is free.

## Eval

15 curated edge cases (`num_eval_examples=15`, 1 rollout each).

| Policy | avg reward | exact | format | partial |
| --- | --- | --- | --- | --- |
| Gold sweep-line via tools (ceiling) | **1.200** | 1.000 | 1.000 | 0.000 |
| Naive (ignore TZ; busy end inclusive) | **0.293** | 0.067 | 1.000 | 0.133 |
| `minimax/minimax-m2.7` (OpenRouter, T=0, 2048 tok) | **0.993** | 0.800 | 0.933 | 0.033 |

The gold policy is a harness check: tools leak enough to rebuild the world, and the rubric fires 1.2. The naive policy is a discrimination check: DST offsets, NY/Kolkata non-overlap, and inclusive busy do not rubber-stamp 1.2. Naive is exact on only the fully-booked `NONE` row.

MiniMax is exact on **12/15**. The three misses are the ones the env is supposed to catch:

- `sydney_ny_none` - format only (0.2). Claimed a 13:00Z overlap between Sydney and New York that does not exist.
- `dst_eu_monday` - valid-not-earliest (0.3). Answered 10:00Z after the EU spring-forward; gold is 08:00Z.
- `no_slot_fully_booked` - 0.0. Truncated before `</answer>` at 2048 tokens.

```bash
uv run vf-eval meeting-slot -n 15 -r 1 -p openrouter \
  -m minimax/minimax-m2.7 --max-tokens 2048 \
  --temperature 0 --max-concurrent 1 --disable-tui --disable-env-server
```

`--max-concurrent 1` keeps OpenRouter in-flight budget from aborting mid-rollout. Budget ≥2048 max tokens. Reasoning models spend the window on tool calls before `</answer>`; truncation looks like a grader bug.

## Installation

```bash
uv pip install -e .
python -m pytest tests/test_meeting_slot.py -q
```

From the Hub:

```bash
prime env install devtechedge/meeting-slot
```

```python
import verifiers as vf

env = vf.load_environment("meeting-slot")
```

Requires `verifiers>=0.1.14,<0.2`.

## `load_environment` arguments

| Arg | Default | Meaning |
| --- | --- | --- |
| `num_train_examples` | `500` | train split size |
| `num_eval_examples` | `100` | eval split size (edge cases prepended) |
| `seed` | `42` | train RNG; eval uses `seed + 1` |
| `max_turns` | `40` | tool-call turns before stop |
| `difficulty` | `None` | `"easy"` \| `"medium"` \| `"hard"` \| mixed |

```bash
uv run vf-eval meeting-slot -n 20
uv run vf-eval meeting-slot -a '{"difficulty": "hard", "num_eval_examples": 40}'
```

Dataset rows never use a column named `task`. Verifiers ≥0.1 treats `info["task"]` as a nested rollout payload.

## Gold solution

Dataset construction **is** the gold solver. For each attendee, working hours minus busy are converted to UTC with `zoneinfo` (both DST folds, skipping spring-forward gaps). The UTC free intervals are intersected; the earliest start `s` with `s + duration` inside the intersection and inside the search window is gold.

```python
from meeting_slot import gold_earliest, solve_from_tools

gold_earliest(world, duration_minutes, window_start, window_days)
# identical, but only using the four public tools:
solve_from_tools(world, duration_minutes, window_start, window_days)
```

`tests/test_meeting_slot.py` asserts the solver against a hand-checked fixture list (US/EU DST, 30 vs 60 minute gaps, NY–Kolkata NONE, inclusive busy).

## Files

```
meeting_slot.py                 # generator, gold, tools, grader, load_environment
pyproject.toml
README.md
LICENSE
tests/test_meeting_slot.py
```

## What this is not

- Not a wrap of a public calendar dataset.
- Not LLM-judged.
- Not single-turn. The calendars are behind tools on purpose.
- Not a dump of the whole calendar into the prompt.

## License

MIT


---

## 17. calendar-math
- **URL:** https://github.com/devtechedge/calendar-math
- **Language:** Python
- **Topics:** calendar, evaluation, python, reinforcement-learning, rl, rlvr, verifiers, llm-evaluation, prime-intellect
- **Description:** Single-turn calendar arithmetic RL environment for Prime Intellect: datetime gold solver, exact+format+partial grader, vf-eval ready.

### README.md

# calendar-math

Single-turn **calendar arithmetic** for RLVR / evals on the [Prime Intellect Environments Hub](https://app.primeintellect.ai/dashboard/environments).

Hub: [devtechedge/calendar-math](https://app.primeintellect.ai/dashboard/environments/devtechedge/calendar-math) · Source: [github.com/devtechedge/calendar-math](https://github.com/devtechedge/calendar-math)

The model is given one of three question types, reasons, and puts a final answer in `<answer>` tags. The grader is pure `datetime` - no LLM-as-judge, no fuzzy string matching on the main reward.

| Task | Example prompt | Gold answer |
| --- | --- | --- |
| `add_days` | What date is 1 day after 2024-02-28? | `2024-02-29` |
| `days_between` | How many days after 2024-02-28 is 2024-03-01? | `2` |
| `weekday` | What day of the week is 2024-02-29? | `Thursday` |

This is intentionally **not** reverse-text or word-count. Calendar reasoning is a documented LLM failure mode (leap years, century years, month lengths, weekday). The environment turns that into a dense, automatically-graded RL signal.

## Why this design

- **Verifiable.** Gold answers are produced by Python `datetime.date`. The same functions are the reference solver.
- **Hard where it matters.** Eval always includes curated edge cases: 1900-02-28 (century, not leap), 2000-02-28 (century, leap), 2024-02-29, year boundaries.
- **Not gameable by format alone.** Format is a 0.2 bonus. Exact match is the 1.0 term.
- **Shaping, not noise.** Off-by-one dates / day-counts score 0.5 partial credit - models routinely confuse inclusive vs exclusive counting. Adjacent weekdays score 0.3.
- **Configurable.** `num_train_examples`, `num_eval_examples`, `seed`, and an optional `task` pin.

## Reward

```
reward = 1.0 * exact_match + 0.2 * format + 0.2 * partial_credit
```

| Term | 1.0 when | Notes |
| --- | --- | --- |
| `exact_match` | parsed `<answer>` equals gold | dates ISO, weekdays canonical English, counts decimal integers |
| `format` | `<answer>...</answer>` present | extra prose outside the tags is ignored |
| `partial_credit` | near-miss as above | 0 when exact match already fired, so a perfect answer is **1.2** not 1.4 |

## Eval

`vf-eval` on the 15 curated edge cases (`num_eval_examples=15`, 1 rollout):

| Policy | avg reward | exact | format | partial |
| --- | --- | --- | --- | --- |
| Gold datetime solver (ceiling) | **1.200** | 1.000 | 1.000 | 0.000 |
| Naive calendar (year%4 leaps, inclusive counts) | **0.768** | 0.533 | 1.000 | 0.173 |

The gold policy is a harness check: install, `load_environment`, rollouts, and the rubric all fire. The naive policy is a discrimination check: century non-leaps and inclusive day-counts do not rubber-stamp 1.2.

Against an API model (needs `OPENAI_API_KEY` or `--provider prime`):

```bash
uv run vf-eval calendar-math -n 20 -r 1 -m gpt-4.1-mini
```

## Installation

```bash
uv pip install -e .
python -m pytest tests/test_calendar_math.py -q
```

From the Hub:

```bash
prime env install devtechedge/calendar-math
```

```python
import verifiers as vf

env = vf.load_environment("calendar-math")
```

## `load_environment` arguments

| Arg | Default | Meaning |
| --- | --- | --- |
| `num_train_examples` | `500` | train split size |
| `num_eval_examples` | `100` | eval split size (edge cases prepended) |
| `seed` | `42` | train RNG; eval uses `seed + 1` |
| `task` | `None` | `"add_days"` \| `"days_between"` \| `"weekday"` \| mixed |

```bash
uv run vf-eval calendar-math -n 20
uv run vf-eval calendar-math -a '{"task": "weekday", "num_eval_examples": 40}'
```

Requires `verifiers>=0.1.14`. Dataset rows use `task_type` (not `task`): current verifiers treat `info["task"]` as a nested rollout payload.

## Gold solution

Dataset construction **is** the gold solver. For a row `info`:

```python
from datetime import date, timedelta

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

def gold(info):
    if info["task_type"] == "add_days":
        return (date.fromisoformat(info["start"]) + timedelta(days=info["n"])).isoformat()
    if info["task_type"] == "days_between":
        a = date.fromisoformat(info["start"])
        b = date.fromisoformat(info["end"])
        return str((b - a).days)          # midnights that pass; same day = 0
    return WEEKDAYS[date.fromisoformat(info["start"]).weekday()]
```

`tests/test_calendar_math.py` asserts the solver against a hand-checked fixture list (leap years, century years, negative offsets, same-day diffs).

## Files

```
calendar_math.py              # generator, gold, grader, load_environment
pyproject.toml
README.md
LICENSE
tests/test_calendar_math.py
```

## What this is not

- Not a wrap of GSM8K or any public dataset.
- Not LLM-judged.
- Not multi-turn / tool-using. Those are the right shape for a **second** environment (meeting-conflict scheduler, timezone conversion with a tz database, etc.).

## License

MIT


---

## 18. jobsearch-private
- **URL:** https://github.com/devtechedge/jobsearch-private
- **Language:** HTML
- **Topics:** None
- **Description:** Private job-search workspace. Contains PII - never make public.

### README.md

*No standard README.md found.*

---

## 19. notion-clone
- **URL:** https://github.com/devtechedge/notion-clone
- **Language:** HTML
- **Topics:** nextjs, pixel-perfect, react, typescript, visual-regression, animation, app-router, component-architecture, css, frontend-architecture, frontend-engineering, frontend-testing, github-actions, html, lighthouse, playwright, rendering, responsive-design, ui-engineering, web-performance
- **Description:** Pixel-perfect Next.js App Router recreation of the Notion marketing homepage. Source-backed DOM, CSS, fonts, and inline artwork from the original capture, not a restyle. Playwright visual QA and pixel-diff overlays. TypeScript, React 18, Lighthouse. Live on Vercel as a visual engineering exercise; no Notion auth, no database, no editor backend. MIT

### README.md

# Notion Homepage Clone

<p align="center">
  <strong>A source-backed, pixel-focused recreation of the Notion homepage.</strong>
</p>

<p align="center">
  <a href="https://notion-clone-devtechedge1.vercel.app/">Live demo →</a>
</p>

<p align="center">
  <a href="https://nextjs.org/"><img src="https://img.shields.io/badge/Next.js-14.2.30-000000?style=flat-square&logo=next.js&logoColor=white" alt="Next.js 14.2.30"></a>
  <a href="https://notion-clone-devtechedge1.vercel.app/"><img src="https://img.shields.io/badge/Vercel-production-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel production deployment"></a>
  <a href="https://github.com/devtechedge/notion-clone/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/devtechedge/notion-clone/ci.yml?style=flat-square&label=build" alt="Build status"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square" alt="MIT license"></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/Node.js-20%2B-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js 20 or newer"></a>
  <a href="https://react.dev/"><img src="https://img.shields.io/badge/React-18.3.1-149eca?style=flat-square&logo=react&logoColor=white" alt="React 18.3.1"></a>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-5.5.4-3178c6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript 5.5.4"></a>
  <a href="https://github.com/devtechedge/notion-clone/stargazers"><img src="https://img.shields.io/github/stars/devtechedge/notion-clone?style=flat-square" alt="GitHub stars"></a>
  <a href="https://github.com/devtechedge/notion-clone/network/members"><img src="https://img.shields.io/github/forks/devtechedge/notion-clone?style=flat-square" alt="GitHub forks"></a>
  <a href="https://github.com/devtechedge/notion-clone/commits/main"><img src="https://img.shields.io/github/last-commit/devtechedge/notion-clone?style=flat-square" alt="Last commit"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/devtechedge/notion-clone?style=flat-square" alt="MIT license"></a>
  <img src="https://img.shields.io/github/repo-size/devtechedge/notion-clone?style=flat-square" alt="Repository size">
</p>

<p align="center">
  <img src="./docs/screenshots/desktop-reference.png" alt="Notion homepage reference preview" width="920">
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#getting-started">Getting started</a> ·
  <a href="#visual-qa">Visual QA</a> ·
  <a href="#roadmap">Roadmap</a>
</p>

## Overview

This repository is a high-fidelity recreation of the supplied Notion homepage
reference. It exists as a visual engineering exercise: the goal is to preserve
the original page’s coordinates, typography, artwork, spacing, and responsive
behavior rather than reinterpret the design.

The supplied `reference.html` is treated as the visual source of truth. Its
captured DOM, CSS, inline artwork, SVGs, fonts, and design tokens are retained
so the result stays source-backed and reproducible.

## Key Features

| Area | What is included |
| --- | --- |
| Hero | Headline, Build pill, avatar rail, artwork, floating illustrations, and CTAs |
| Navigation | Desktop navigation, product links, login, and primary action |
| Logo wall | Trusted-by statement and company logo arrangement |
| Bento cards | Source artwork for meetings, dashboards, agents, and quick links |
| Testimonials | Gradient quote cards, attribution, and statistics strip |
| CTA | Get-started section with matching actions and spacing |
| Footer | Brand block, language selector, resource columns, and legal details |
| Responsive layout | Reference-driven behavior across viewport sizes |
| Source-backed rendering | Supplied DOM and inline assets preserved instead of redrawn |
| Deterministic image loading | Native eager loading and synchronous decoding for Bento artwork |
| Pixel verification | Full-page captures, overlays, and difference images |
| Visual QA | Chromium checks at a controlled desktop viewport |

## Technology Stack

| Layer | Choice |
| --- | --- |
| Framework | Next.js 14 App Router |
| UI runtime | React 18 |
| Language | TypeScript |
| Styling | Captured reference CSS with CSS variables and design tokens |
| Tooling | npm, TypeScript compiler, Next.js build pipeline |
| Rendering | Static App Router shell redirecting to the reference document |
| Assets | Supplied inline WebP, SVG, font, and HTML assets |
| Verification | Chromium screenshots and source-level image inspection |

See [the architecture notes](./docs/architecture.md) for the rendering
pipeline and image lifecycle decisions.

## Repository Structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── app/
│   ├── layout.tsx       # App Router metadata and document shell
│   └── page.tsx         # Root redirect to the source-backed homepage
├── docs/
│   ├── screenshots/     # Committed reference and visual QA captures
│   └── visual-qa.md     # Rendering and parity notes
├── public/
│   ├── favicon.ico
│   └── reference.html   # Supplied single-file homepage capture
├── .editorconfig
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── next-env.d.ts
├── package-lock.json
├── package.json
└── tsconfig.json
```

The reference page is intentionally kept as a single source-backed document.
The thin Next.js shell provides a conventional project entrypoint without
rebuilding the captured page into visually divergent components.

## Getting Started

### Prerequisites

- Node.js 18.17 or newer
- npm 9 or newer
- Chromium for visual QA

### Installation

```bash
git clone https://github.com/devtechedge/notion-clone.git
cd notion-clone
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

### Build

```bash
npm run build
```

### Production

```bash
npm run build
npm run start
```

## Visual QA

Visual parity is evaluated against the supplied reference screenshot and saved
HTML. The workflow uses:

1. A controlled Chromium viewport.
2. Full-page screenshots of the reference and localhost pages.
3. A blended overlay to reveal alignment drift.
4. A pixel-difference image to locate high-contrast mismatches.
5. Browser inspection of image source, dimensions, visibility, and paint state.

| Artifact | Purpose |
| --- | --- |
| [Reference](./docs/screenshots/desktop-reference.png) | Supplied visual baseline |
| [Local desktop](./docs/screenshots/desktop-local.png) | Current localhost render |
| [Overlay](./docs/screenshots/visual-qa-overlay.png) | Blended alignment comparison |
| [Pixel difference](./docs/screenshots/pixel-difference.png) | Amplified visual delta |

## Rendering Decisions

### Why the supplied HTML is used

The reference document contains the exact DOM hierarchy, CSS, font declarations,
inline assets, and design-token values needed for fidelity. Recreating those
details manually would introduce unnecessary visual drift.

### Image lifecycle handling

The saved document uses lazy and asynchronous image behavior. That lifecycle
can leave below-the-fold Bento artwork unpainted during an immediate full-page
capture even though the data URI and natural dimensions are valid.

The eight Bento images therefore use native eager loading and synchronous
decoding. This is a browser rendering decision, not a screenshot-time script:
there is no artificial scrolling, timeout-based painting, or placeholder art.

### Artwork preservation

Existing WebP, SVG, canvas-like compositions, logos, and font assets remain
source-backed. Artwork is preserved rather than redrawn so the implementation
can be audited against the supplied reference.

## Project Goals

- High visual fidelity to the supplied reference.
- Pixel-accurate coordinates, typography, spacing, and composition.
- Deterministic rendering in Chromium.
- No placeholder or generically recreated artwork.
- A maintainable project shell around the source-backed page.

## Challenges Solved

<details>
<summary>Lazy loading</summary>

Below-the-fold images can remain unloaded during automated full-page capture.
The Bento assets are promoted to native eager loading while preserving their
original source data.
</details>

<details>
<summary>Image decoding</summary>

Asynchronous decoding can complete after layout and capture have already begun.
Synchronous decoding makes the critical Bento artwork available for the first
stable render.
</details>

<details>
<summary>Render lifecycle and viewport activation</summary>

The page must render correctly without synthetic scroll events or delayed
capture logic. The final approach moves the fix into standard image loading
semantics rather than manipulating viewport state.
</details>

<details>
<summary>Full-page capture</summary>

Reference and localhost captures are normalized to the same dimensions before
overlay and difference generation, making section-level drift easier to find.
</details>

## Performance

- Next.js provides a small App Router shell and production build pipeline.
- Inline source assets avoid network dependency for the captured page.
- Bento images use deterministic native loading instead of runtime polling.
- `npm run build` performs compilation, type checking, and static generation.
- Visual fidelity is prioritized before secondary Lighthouse tuning.

## FAQ

### Why is the homepage served from `reference.html`?

The supplied saved DOM is the parity contract. Serving it directly preserves
the original structure, inline artwork, and browser behavior under review.

### Can the artwork be replaced with new components?

No. Existing source-backed artwork is intentionally preserved; changes should
be validated against the committed reference evidence first.

## Known limitations

- Lighthouse JSON generation on the current Windows environment is blocked by
  Chrome Launcher temporary-profile cleanup (`EPERM`); the reproducible command
  is documented under `docs/lighthouse/`.
- The visual baseline is intentionally desktop-first, with responsive smoke
  coverage in Playwright.

## Roadmap

- [x] Preserve the supplied HTML and inline artwork.
- [x] Add native deterministic Bento image loading.
- [x] Add Chromium visual QA captures and comparison artifacts.
- [x] Add repository documentation and contribution policy.
- [x] Add GitHub Actions build validation.
- [x] Add Playwright-based screenshot regression automation.
- [x] Run visual regression checks on every pull request.
- [ ] Add Lighthouse reporting to CI.
- [ ] Add a responsive viewport comparison matrix.

## Repository Statistics

| Property | Value |
| --- | --- |
| Languages | TypeScript, CSS, HTML, inline SVG/WebP |
| Framework | Next.js App Router |
| Architecture | Static source-backed reference document with a Next.js shell |
| Project type | Frontend visual recreation / portfolio case study |
| License | MIT |

## Screenshots

### Desktop

![Desktop local render](./docs/screenshots/desktop-local.png)

### Reference

![Supplied desktop reference](./docs/screenshots/desktop-reference.png)

### Visual QA Overlay

![Visual QA overlay](./docs/screenshots/visual-qa-overlay.png)

### Pixel Difference

![Pixel difference](./docs/screenshots/pixel-difference.png)

The gallery intentionally keeps the reference, local render, overlay, and
difference captures together so visual review can be repeated from a clean
clone.

## Acknowledgements

Thanks to the supplied visual reference, saved HTML capture, design tokens, and
network asset archive that make source-backed parity work possible.

## License

Distributed under the MIT License. See [LICENSE](./LICENSE).

## Author

Built by [Devtechedge](https://github.com/devtechedge).

Repository: [github.com/devtechedge/notion-clone](https://github.com/devtechedge/notion-clone)


---

## 20. job-board
- **URL:** https://github.com/devtechedge/job-board
- **Language:** TypeScript
- **Topics:** ats, greenhouse, job-board, postgres, tanstack, typescript, vercel, ashby, job-search, lever, public-api, react
- **Description:** Jobrow indexes still-open US tech roles from public Greenhouse, Ashby, and Lever board APIs. 50 companies, 5,000+ open roles. Table-first search, same-day close when a board drops a posting. TanStack Start, TypeScript, Neon Postgres. Independent index ΓÇö not an employer or agency.

### README.md

# Jobrow

Public register of **still-open US tech roles**, read from employer ATS JSON - not from another job site.

Tagline: **Still open.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://jobrow.vercel.app)
[![Boards](https://img.shields.io/badge/Boards-50-1F6B4A)](https://jobrow.vercel.app/companies)
[![TanStack Start](https://img.shields.io/badge/TanStack%20Start-black)](https://tanstack.com/start)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live demo

**https://jobrow.vercel.app**

Production is **Neon Postgres** on Vercel Hobby. The board currently holds **5,000+ open US tech roles across 50 companies**. Apply always leaves Jobrow for the employer ATS. Public listings - not an employer, recruiter, or agency.

`GET /api/health` reports `{ db, openJobs, pendingBoards, staleBoards, lastOkAt }`.

### Public JSON API

Unauthenticated read API for the same US-tech slice Jobs shows (`status=open`, `us_eligible`, `tech_eligible`). Native apps and other clients can call these without going through server functions:

- `GET /api/jobs` - `JobQuery` as querystring (`q`, `fn`, `seniority`, `workplace`, `location`, `salaryMin`, `posted`, `ats`, `company`, `sort`, `page`). Page size 40.
- `GET /api/jobs/:id` - one role, with sanitized `description_html` plus `description_text`
- `GET /api/companies` - boards
- `GET /api/companies/:slug` - board plus open roles
- `GET /api/home` - register KPIs (open count, boards, first-seen 24h, last crawl, functions, boards) plus a latest page
- `GET /api/closed` - roles closed after a successful crawl

`/api/health`, `/api/desk`, cron, and admin are unchanged. Product auth stays off. Apply URLs are employer ATS https links. Discovery helpers: [`/sitemap.xml`](https://jobrow.vercel.app/sitemap.xml), [`/llms.txt`](https://jobrow.vercel.app/llms.txt).

### Native app

An Expo (Android + iOS) client lives in [`mobile/`](mobile/). It is a separate package so the Vercel web build does not compile it. See [mobile/README.md](mobile/README.md) to run it in the iOS simulator or Android emulator.

---

## Sister product

**[Lattice](https://lattice-devtechedge1.vercel.app)** - free board for **blockchain, crypto, and Web3 jobs** from live employer ATS boards (Coinbase, Binance, Ripple, and more). Jobrow stays US tech; Lattice covers Web3 careers. Source: [devtechedge/lattice](https://github.com/devtechedge/lattice).

---

## Screenshots

| Jobs | Search |
|----------|--------|
| ![Jobs](docs/screenshots/01-register.png) | ![Search](docs/screenshots/05-index.png) |

| Role | Companies |
|------|-----------|
| ![Job detail](docs/screenshots/03-job-detail.png) | ![Companies](docs/screenshots/04-companies.png) |

| About | Pricing |
|-------|--------|
| ![About](docs/screenshots/02-about.png) | ![Pricing](docs/screenshots/06-rates.png) |

Share card: [docs/screenshots/social-preview.png](docs/screenshots/social-preview.png)

---

## What you can do

- **Jobs** (`/`) - Latest (8 roles, one company per row), filters, KPIs, Companies strip (8)
- **Closed** (`/closed`) - roles removed after a successful crawl (filled or pulled)
- Company marks next to every listing (site icon, initials if the icon fails)
- **Search** (`/jobs`) - full paginated table of the US tech slice
- **Companies** (`/companies`) - 50 boards, US-tech count vs listed count, last successful fetch
- **Saved** - browser watchlist count in the header (nav: Jobs · Search · Companies · About · Saved · Closed)
- **Role** (`/jobs/:id`) - summary, pay, workplace, posting HTML, Apply (leaves the site)
- **Contact** (`/contact`) - corrections and legal notes (not applications)
- **Add a board** (`/employers`) - public Greenhouse / Ashby / Lever / Workable token
- **Pricing** (`/pricing`) - Bound pass waitlist (`$11` / 28 days). No live checkout
- **Promote** (`/placements`) - Ruled pin `$120` / masthead line `$55`. Waitlist only
- **Watchlist** - local to the browser (`localStorage` key `jobrow:watchlist`, max 200). No account. No resume upload
- **JSON API** (`/api/jobs`, `/api/companies`, `/api/home`) - public register contract for native apps
- **iOS / Android** - Expo app in `mobile/`. Apply opens the employer ATS. Saved jobs use local AsyncStorage.
- **Admin** (`/admin`) - password-gated crawl and board edits

A role **drops when a successful crawl no longer sees it**. A failed fetch does not close that board.

---

## Registry (50)

Seeded from [data/companies.csv](data/companies.csv) and [src/lib/seed-companies.ts](src/lib/seed-companies.ts). Tokens were confirmed against live public board JSON.

| ATS | Companies |
|-----|-----------|
| Greenhouse (36) | Stripe, Anthropic, Airbnb, Coinbase, Discord, Figma, Cloudflare, Databricks, Vercel, Dropbox, Robinhood, Block, Lyft, Pinterest, Reddit, Twilio, Datadog, MongoDB, Instacart, Roblox, GitLab, Grafana Labs, Asana, Okta, Alpaca, Affirm, Brex, Scale AI, Anduril, HubSpot, DoorDash, Elastic, Glean, Chime, Flexport, Samsara |
| Ashby (11) | OpenAI, Ramp, Linear, Notion, Cursor, Perplexity, Supabase, Plaid, Snowflake, Confluent, Sentry |
| Lever (3) | Palantir, Wealthfront, Spotify |

US-eligible **tech** titles stay on Jobs. Sales, finance, and non-US postings on the same board are ignored. The companies table shows both **US tech** and **listed** (raw JSON rows on the last good fetch).

### Add another company

1. Confirm the public board JSON exists:
   - Greenhouse: `https://boards-api.greenhouse.io/v1/boards/{token}/jobs`
   - Ashby: `https://api.ashbyhq.com/posting-api/job-board/{token}?includeCompensation=true`
   - Lever: `https://api.lever.co/v0/postings/{token}?mode=json`
2. `/admin` → unlock with `ADMIN_PASSWORD` → name / slug / ATS / board token / careers URL → crawl that row.
3. Or append a line to `data/companies.csv` and a matching object in `SEED_COMPANIES`.

Do not scrape career marketing HTML when the board JSON exists. Do not scrape other job aggregators.

---

## Stack

| Layer | Technology |
|-------|------------|
| App | TanStack Start, React 19, TypeScript, Tailwind v4 |
| Data | Neon Postgres in production; embedded PGLite when `DATABASE_URL` is omitted (local) |
| Sources | Greenhouse, Ashby, Lever public JSON (Workable adapter ready) |
| Host | Vercel Hobby |
| Crawl | GitHub Action, 4× daily (8 shards, retry on a flaky board), `POST /api/cron/crawl` with `Authorization: Bearer` |
| Security | CSP and related headers in [vercel.json](vercel.json); see [SECURITY.md](SECURITY.md) |

---

## Quick start

```bash
npm install
npm run dev
```

Without `DATABASE_URL` the app uses embedded PGLite and seeds the 50 boards on first load.

```bash
npm test
npm run typecheck
```

Env template: [.env.example](.env.example). Never commit secrets.

| Variable | Where | Purpose |
|----------|--------|---------|
| `DATABASE_URL` | Vercel | Neon pooled URI (`sslmode=require`) |
| `ADMIN_PASSWORD` | Vercel | `/admin` |
| `CRON_SECRET` | Vercel + GitHub Actions | Cron bearer token |
| `APP_URL` | GitHub Actions | Origin the Action calls |
| `VITE_SITE_URL` | Vercel | Sitemap / JSON-LD origin |

Production already has Neon attached. Local demos can omit `DATABASE_URL`.

---

## Security

See [SECURITY.md](SECURITY.md). Report vulnerabilities with GitHub private advisory, not a public issue.

Hardening in this tree: parameterized SQL, escaped job HTML, script-safe JSON-LD, fail-closed admin/cron secrets in production, IP-limited admin unlock, public API rate limits, ATS host allowlist, no `?secret=` on cron, desk size cap, HTTPS-only Apply links, HSTS + CSP headers. Details: [SECURITY.md](SECURITY.md).

---

## Discovery (SEO)

| Item | Status |
|------|--------|
| Crawlable pages + `robots.txt` + sitemap (`lastmod`) | Live |
| `/llms.txt`, OG/canonical, long-tail titles | Live |
| Google Search Console + Bing Webmaster | Verified / imported |
| Crawl freshness | GitHub Action **4× daily**, 8 shards; retry + warn on one flaky board |
| Earn links (X / Indie Hackers / Discord) | Operator posts; HN gated for new accounts |
| Patience | New hosts often need weeks–months for competitive queries |

## Remaining

| Item | Status |
|------|--------|
| Custom domain / final brand | Working name is Jobrow. Buy later. |
| Neon | Live. |
| GitHub Action `APP_URL` + `CRON_SECRET` | Set on the repo. |
| Counsel | Terms / privacy / sourcing are drafts. |
| Bound pass / ruled pins | Rate card exists. Checkout is not live. |
| Private GitHub repo | Optional. Does not replace Vercel secrets - see [SECURITY.md](SECURITY.md). |

---

## License

MIT. See [LICENSE](LICENSE).


---

## 21. remix-render-to-string-navigation
- **URL:** https://github.com/devtechedge/remix-render-to-string-navigation
- **Language:** TypeScript
- **Topics:** None
- **Description:** No description

### README.md

# renderToString output cannot be navigated by the client runtime

Minimal reproduction for [remix-run/remix#11808](https://github.com/remix-run/remix/issues/11808).

`renderToString` strips the `<!-- rmx:flush document -->` marker from its output. The client
runtime only takes the full-document-reload path when it sees that marker, so a link click
between two `renderToString` pages updates the URL and then silently leaves the old document in
place.

## Run it

Requires Node 24.3 or newer.

```sh
npm install
npm run dev
```

Open http://localhost:44100.

Page A carries a client entry (the click counter), so the Remix runtime is active and intercepts
same-document link clicks. Two links leave A:

- `/stream`, rendered with `context.render()` (`renderToStream`) - **navigates**
- `/string`, rendered with `renderToString()` - **URL changes, document does not**

## Automated check

```sh
npx playwright install chromium
npm run verify
```

`verify.mjs` opens the app in Chromium, clicks each link, and prints the URL, document title, and
`#heading` text before and after the click.

Current output against `@remix-run/ui` 0.9.0:

```json
--- clicked #link-stream ---
{ "before": { "url": "/", "title": "A", "heading": "A" },
  "after":  { "url": "/stream", "title": "B", "heading": "B" },
  "navigated": true }

--- clicked #link-string ---
{ "before": { "url": "/", "title": "A", "heading": "A" },
  "after":  { "url": "/string", "title": "A", "heading": "A" },
  "navigated": false }
```

Note that `navigated: false` comes with no console output and no `pageerror`. The failure is only
observable through `navigation.addEventListener('navigateerror', ...)` or the `error` event on the
runtime returned by `run()`.

## Where the marker goes missing

```sh
curl -s localhost:44100/stream | tail -c 60
# </body></html><!-- rmx:flush document -->

curl -s localhost:44100/string | tail -c 60
# </body></html>
```

Both responses are `200` and both are complete documents. Only one carries the marker.

## Layout

| File | Purpose |
| --- | --- |
| `app/actions/controller.tsx` | Serves `/` and `/stream` with `context.render()`, `/string` with `renderToString()` |
| `app/actions/home-page.tsx` | Page A, with a client entry and both links |
| `app/actions/destination-page.tsx` | Page B, identical for both destinations |
| `app/actions/public/click-counter.tsx` | Client entry that puts the runtime on page A |
| `verify.mjs` | Playwright script that clicks both links and reports the result |


---

## 22. blockchain_expert
- **URL:** https://github.com/devtechedge/blockchain_expert
- **Language:** TypeScript
- **Topics:** agents, hitl, llm, mcp, nextjs, security, smart-contracts, solidity, static-analysis, swc, typescript, web3
- **Description:** Argus is an agentic smart-contract security copilot for auditors. Deterministic static analysis, SWC-mapped retrieval, false-positive filtering, remediation diffs, and human-in-the-loop triage. TypeScript engine, Next.js workbench, MCP tool host. Educational samples only; never connects to a chain. Vercel is demo-mode (no API key required).

### README.md

# ARGUS

Agentic smart-contract security copilot: deterministic static analysis, SWC-mapped retrieval, and a human-in-the-loop triage board.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://argus-copilot.vercel.app)
[![CI](https://github.com/devtechedge/blockchain_expert/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/blockchain_expert/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://argus-copilot.vercel.app**

> **Status:** Vercel demo-mode. The analyzer, SWC retrieval, MCP tool host, and HITL board run in the browser. No API key. No chain RPC. Educational fixtures only - do not deploy the samples.

---

## Screenshots

| Workbench | HITL triage |
|-----------|-------------|
| ![Overview](docs/screenshots/01-overview.png) | ![Triage](docs/screenshots/02-triage.png) |

| Agent protocol |
|----------------|
| ![Protocol](docs/screenshots/03-protocol.png) |

---

## Features

- Deterministic Solidity static analysis (CEI / reentrancy, `tx.origin`, delegatecall, unchecked calls, unprotected withdraw, SELFDESTRUCT, weak seeds, floating pragma)
- SWC registry mapping with offline TF-IDF retrieval
- Heuristic false-positive filter (guards demote CEI smells)
- Remediation diff drafts
- Human-in-the-loop accept / dismiss / mark patched
- Markdown audit memo export
- MCP-shaped local tool host (`tools/list`, `tools/call`)
- CLI: `npm run scan -- path.sol`

This is a defensive review aid, not a professional audit and not a chain client.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Workbench | Next.js 15 App Router, TypeScript, React 19 |
| Engine | Local TypeScript parser + detectors + TF-IDF SWC corpus |
| Agent | Explicit nine-phase state machine with trace events |
| Tools | JSON-RPC 2.0 subset (MCP-shaped, read-only) |
| Data | Educational Solidity fixtures in-repo |
| Hosting | Vercel demo-mode (client-side analyzer) |
| CI | GitHub Actions - `npm ci`, unit tests, typecheck. No RPC. |

---

## Quick Start

```bash
npm install
npm test
npm run scan -- benchmarks/educational_samples/reentrancy_vault.sol
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). Pick a fixture, run **Static scan**, then Accept / Dismiss on the board.

Optional local LLM review uses `XAI_API_KEY` from `.env.example`. The public demo does not.

---

## Agent protocol

```
INGEST → PARSE → STATIC_SCAN → RAG_ENRICH → FP_FILTER
       → SEVERITY_RANK → PATCH_DRAFT → HITL_GATE → REPORT
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Educational samples live in `benchmarks/educational_samples/` and are labeled do-not-deploy.

---

## License

MIT. See [LICENSE](LICENSE).

## Security

Threat model, residual risk, and operator secrets: see [SECURITY.md](SECURITY.md).
This public deploy is a portfolio / demo surface; the GitHub repo may go private
after review without changing the live site’s required env hygiene.


---

## 23. holdslot
- **URL:** https://github.com/devtechedge/holdslot
- **Language:** JavaScript
- **Topics:** hackathon, openai, webmcp
- **Description:** HoldSlot ΓÇö agent can search and hold a slot; only the human can confirm. OpenAI WebMCP Challenge 2026.

### README.md

# HoldSlot

OpenAI [WebMCP Challenge](https://webmcp.devpost.com/) 2026.

A booking desk where an **in-browser agent can search and hold a slot**, and **only the human can confirm**. The hold is visible on the same page. Confirm is a button, not a WebMCP tool.

Live: https://holdslot-cyan.vercel.app

## Why WebMCP

Agents are bad at calendars. They click the wrong cell, double-book, or submit while the person looks away. HoldSlot exposes **page-owned tools** so the agent does real work on the live board, then stops at the commitment.

## Tools (`document.modelContext.registerTool`)

| Tool | Who | What |
| --- | --- | --- |
| `search_slots` | Agent | Open slots by day and duration |
| `hold_slot` | Agent | Hold an open slot (expires in 3 minutes) |
| `list_holds` | Agent | Current holds and remaining time |
| `release_hold` | Agent | Drop a hold |
| `get_board` | Agent | Full board snapshot |
| `request_confirm` | Agent | Ask the human to confirm. **Does not confirm.** |

**Not a tool:** `Confirm booking`. Only the person on the page can press it.

## Test (judges)

1. Open the live URL in **ChatGPT’s in-app browser**, or Chrome with `chrome://flags/#enable-webmcp-testing` enabled.
2. Ask: *Search next available 30-minute slots, hold one, then stop. Do not confirm.*
3. You should see a **hold** with a timer. Confirm stays a human button.
4. If WebMCP is missing, the banner on the page says so.

No login. Simulated clinic / interview slots only. No real payments.

## Run locally

Serve the folder over HTTP (WebMCP needs a page context; file:// is unreliable):

```bash
npx serve .
```

Open the URL, enable the Chrome WebMCP flag, reload.

## Stack

Static HTML / CSS / JS. No backend. State is in the page so the human and the agent share one board.

## License

MIT. See [LICENSE](LICENSE).

## Security

Threat model, residual risk, and operator secrets: see [SECURITY.md](SECURITY.md).
This public deploy is a portfolio / demo surface; the GitHub repo may go private
after review without changing the live site’s required env hygiene.


---

## 24. github-repo-presentation
- **URL:** https://github.com/devtechedge/github-repo-presentation
- **Language:** Not specified
- **Topics:** None
- **Description:** Private skill archive. Not a product repo.

### README.md

# github-repo-presentation

Private skill archive. **Revision 11 - 2026-09-01.** Not a product repo.

## Download

**[github-repo-presentation-revision-11.zip](https://github.com/devtechedge/github-repo-presentation/raw/main/github-repo-presentation-revision-11.zip)** - click to download.

Or clone with GitHub Desktop into `Documents\GitHub\github-repo-presentation`.

## Layout

```
github-repo-presentation-revision-11.zip
github-repo-presentation/
  SKILL.md
  HANDOFF.md
  readme-skeleton.md
  mit-license.txt
  references/mit-license.txt
  references/chrome-and-data.md
```

Revision 11 adds general chrome and data-path traps that apply to **every** public repo (cool silver light, native `<select>` vs leftover CSS transform, WASM copy on serverless, `DATABASE_URL` vs vendor `STORAGE_URL`, README matching the live store, CSP for remote images, cron Bearer on host and Actions). Re-upload the zip at grok.com/skills-and-connectors.

Keep this repository private. Do not copy the zip into public product repos.


---

## 25. collabspace
- **URL:** https://github.com/devtechedge/collabspace
- **Language:** TypeScript
- **Topics:** collaborative-whiteboard, framer-motion, infinite-canvas, multiplayer, presence, react, realtime, supabase, typescript, vercel, vite, websocket-alternative
- **Description:** CollabSpace is a real-time multiplayer whiteboard: infinite canvas, presence, chat, reactions, and a laser pointer. React 18, Vite, TypeScript, Framer Motion, Supabase Realtime. Dark/light, responsive. Public Vercel currently shows a Supabase-not-configured shell; full multiplayer needs a Supabase project. Local path is Docker + npx supabase start.

### README.md

# CollabSpace

Real-time multiplayer collaborative whiteboard with infinite canvas, presence, chat, reactions, and a laser pointer.

![CI](https://github.com/devtechedge/collabspace/actions/workflows/ci.yml/badge.svg)
![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)
![React](https://img.shields.io/badge/React-18-61dafb?logo=react)
![Vite](https://img.shields.io/badge/Vite-5-646cff?logo=vite)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![Supabase](https://img.shields.io/badge/Supabase-Realtime-3ecf8e?logo=supabase)
![Framer Motion](https://img.shields.io/badge/Framer%20Motion-11-black)
![License](https://img.shields.io/badge/License-MIT-green)

## Live Demo

**https://collabspace-mauve.vercel.app**

> **Status:** The production deploy currently shows a clean “Supabase not configured” shell. Full multiplayer collaboration requires a Supabase project; the free tier is limited to 2 active projects and those slots are already used by other portfolio apps.  
> Locally the project runs fully: Docker + local Supabase (`npx supabase start`) + `npm run dev`. Schema is idempotent - paste `supabase/migrations/0001_init.sql` into any free Supabase project (or use the local stack) for a working realtime demo.

## Screenshots

### Dark mode - Rooms
![Dark mode Rooms view](docs/screenshots/Screenshot%202026-07-27%20082946.png)

### Light mode - Chat
![Light mode Chat view](docs/screenshots/Screenshot%202026-07-27%20082952.png)

### Dark mode - Users
![Dark mode Users view](docs/screenshots/Screenshot%202026-07-27%20082958.png)

## Features

- **Infinite canvas** - pan (Shift-drag / middle-click), zoom (scroll), minimap
- **Drawing tools** - Pencil, Line, Rectangle, Circle, Text, Sticky note, Eraser, Select, Laser pointer
- **Real-time multiplayer** - live cursors with name labels via Supabase Presence
- **Persistent elements & chat** - Postgres Changes fan-out (no custom Socket server)
- **Ephemeral signals** - floating emoji reactions + laser pointer via Realtime Broadcast
- **Undo / Redo** with full history stack (`⌘Z` / `⌘⇧Z`)
- **Dark / light theme** with system preference + anti-flash
- **Responsive** - 5 breakpoints, mobile bottom-drawer sidebar, 44 px touch targets
- **Accessible** - focus-visible rings, ARIA tablist, prefers-reduced-motion, prefers-contrast
- **Anonymous identity** - random user stored in `localStorage` (auth-ready later)

## Related

Sibling demo: [collabspace-express](https://github.com/devtechedge/collabspace-express) - Express + Vite whiteboard without the Supabase realtime stack.

## Tech Stack

| Layer        | Tech                                              |
|--------------|---------------------------------------------------|
| Frontend     | React 18 · Vite 5 · TypeScript · Framer Motion   |
| Backend      | Supabase (Postgres + Realtime Presence / Broadcast / Postgres Changes) |
| Deploy       | Vercel (SPA rewrite via `vercel.json`)            |
| Identity     | Client-side random (localStorage)                 |

## Quick Start

```bash
# 1. Install
npm install

# 2. Env
cp client/.env.example client/.env
# Add VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY

# 3. Schema (paste supabase/migrations/0001_init.sql into Supabase SQL Editor)
# Idempotent - safe to re-run

# 4. Dev server
npm run dev
# → http://localhost:5173
```

## Architecture (v1 → v2)

Original v1 used Express + Socket.io + Prisma + SQLite.  
v2 is fully client-side against Supabase - no custom backend process.

| Concern              | v2 implementation                          |
|----------------------|--------------------------------------------|
| Boards / elements    | `boardSync.ts` / `canvasSync.ts` → Supabase REST + Postgres Changes |
| Chat                 | `chatSync.ts` → Supabase insert + Postgres Changes |
| Cursors / presence   | Supabase Realtime Presence                 |
| Reactions / laser    | Realtime Broadcast (ephemeral)             |
| Identity             | `identity.ts` → localStorage               |

See `client/src/lib/realtime.ts` for the single `joinBoard()` session that wires all four channels.


## Engineering

Phase B hardening: [`SECURITY.md`](SECURITY.md) (open RLS, no auth, payload allow-lists), `npm test` (node:test), `npm run typecheck`, Playwright smokes of the unconfigured Vercel shell, GitHub Actions CI, Dependabot (patch/minor only).

## License

MIT License. See [LICENSE](LICENSE) for details.


---

## 26. astra-marketplace
- **URL:** https://github.com/devtechedge/astra-marketplace
- **Language:** TypeScript
- **Topics:** ecommerce, marketplace, nextjs, postgresql, prisma, react, tailwindcss, typescript, admin-dashboard, full-stack, portfolio, seller-portal
- **Description:** AstraMart: paper-and-copper marketplace demo. 18-SKU catalog, HMAC demo sessions, seller and admin portals. Next.js 14. Live Vercel is seeded demo data with mock payments. customer@demo.com / Demo123!

### README.md

# AstraMart

Independent paper-and-copper marketplace demo with a customer storefront, seller portal, admin back-office, HMAC demo sessions, cart/checkout, returns, recommendations, and a Prisma schema for local production mode. Built as a portfolio demo.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://astra-marketplace.vercel.app/)
[![CI](https://github.com/devtechedge/astra-marketplace/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/astra-marketplace/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Prisma](https://img.shields.io/badge/Prisma-5-2D3748?logo=prisma)](https://www.prisma.io/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3-06b6d4?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Live Demo

**https://astra-marketplace.vercel.app/**

> **Demo-mode status:** The live Vercel site uses seeded in-memory demo data and mock payments - not Prisma. Catalog browse, search, product photos, health, and coupon GET are public. **Checkout, account, orders, seller, and admin require sign-in.** Full Prisma/PostgreSQL schema + Docker Compose remain the local production foundation. No real payment capture, carrier labels, or object storage.

### Demo credentials

| Role     | Email              | Password  |
|----------|--------------------|-----------|
| Customer | `customer@demo.com` | `Demo123!` |
| Seller   | `seller@demo.com`   | `Demo123!` |
| Admin    | `admin@demo.com`    | `Demo123!` |

Shown on `/login` and this README on purpose for portfolio DX. Passwords are bcrypt-hashed in a server-only module (`src/lib/server/demoUsers.ts`) and are never shipped in the client bundle.

## Screenshots

| Storefront | Account |
|------------|---------|
| ![Storefront](docs/screenshots/01-storefront.png) | ![Account](docs/screenshots/02-account.png) |

| Orders | Seller dashboard |
|--------|------------------|
| ![Orders](docs/screenshots/03-orders.png) | ![Seller](docs/screenshots/04-seller-dashboard.png) |

| Admin operations |
|------------------|
| ![Admin](docs/screenshots/05-admin-ops.png) |

## Features

- **Design system** - paper `#F4EFE6` / surface `#FFFCF7` / ink `#1A1612` / copper `#C45C26` tokens; Fraunces (display) + IBM Plex Sans via `next/font`; Fraunces wordmark with a 4-point copper star; Account menu holds Seller/Admin; overlay scrollbars hidden until overflow + hover/focus
- **Customer storefront** - merchandising hero (not a GMV/SLA pitch), search, deals, product detail, cart, 6-step checkout (login required), orders, tracking, returns, wishlist, gift-card SKUs, AstraPlus membership
- **18-SKU catalog** - real JPEGs in `public/products` (not SVG placeholders) across Electronics, Home & Kitchen, Fashion, Books, Beauty, Sports, Toys, Grocery, Automotive, Pet Supplies, and Gift cards. Header lists Gift cards once via `/gift-cards`
- **Seller portal** - KPI dashboard, listings/inventory, product listing wizard, promotions, payouts, ads, support (signed session)
- **Admin command center** - GMV/orders/refund/SLA metrics, seller & product moderation, support tickets, audit, CMS, feature flags, analytics, search merchandising (signed session)
- **Commerce core** - coupons, tax/shipping calculation, mock payment intents, RMA-style returns, recommendation rows (buy again / trending / recently viewed)
- **Platform services** - HMAC session middleware, API RBAC, origin checks, auth rate limits, webhook secret, CSP without `unsafe-eval`, health API, notifications, review/Q&A endpoints
- **Production foundation** - Prisma schema, Docker Compose, GitHub Actions (unit + typecheck + Playwright), Dependabot, [SECURITY.md](SECURITY.md)

Playwright testids kept: `site-header`, `home-hero`, `add-to-cart`, `shopping-cart`, `login-page`, `seller-dashboard`, `admin-command-center`.

## Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | Next.js 14 (App Router), TypeScript, Tailwind CSS, Fraunces + IBM Plex Sans via next/font, Lucide |
| Backend      | Next.js API routes, Zod validation |
| Data         | Prisma 5 + PostgreSQL schema (local foundation); seeded demo repository on Vercel |
| Auth         | HMAC cookie sessions + bcrypt demo users (server-only) |
| Tooling      | Vitest, Playwright, ESLint, GitHub Actions |
| Deploy       | Vercel - https://astra-marketplace.vercel.app/ |


## Quick Start

```bash
npm install
npm run dev
```

Open http://localhost:3000

```bash
npm test            # unit - 26 passed (commerce, rbac, validation, session, origin)
npm run typecheck
npm run test:e2e    # Playwright Chromium smokes (signed session cookies)
```

Optional local database (not used by the Vercel demo):

```bash
cp .env.example .env
docker compose up -d
npm run db:generate && npm run db:push && npm run db:seed
```

Set `APP_SECRET` before treating sessions as real. The code has a demo HMAC fallback if it is unset.

## Architecture notes

- Service/repository split for auth, catalog, cart, checkout, fulfillment, returns, seller and admin
- HMAC-SHA256 `astra-session` cookie (httpOnly, SameSite=lax, Secure on Vercel/production, 8h). Missing/invalid session is **GUEST**, never CUSTOMER. `astra-role` is ignored and cleared.
- API RBAC via `requireSession` in `src/lib/security/api.ts`; origin check on mutating `/api` except the payment webhook; auth rate limit 10/10min/IP in memory
- Middleware gates `/admin*`, `/seller*`, `/checkout*`, `/account*`, `/orders*`
- Demo repository powers the live Vercel deploy; swap to Prisma client for real persistence. **Prisma is not live on Vercel.**
- Threat model: [SECURITY.md](SECURITY.md). Deeper docs under `docs/` (ARCHITECTURE, API_SPEC, DEPLOYMENT)

## License

MIT License. See [LICENSE](LICENSE) for details.


---

## 27. collabspace-express
- **URL:** https://github.com/devtechedge/collabspace-express
- **Language:** TypeScript
- **Topics:** canvas, collaborative-whiteboard, express, prisma, react, socketio, typescript, vite, websocket, multiplayer, realtime, vercel
- **Description:** CollabSpace Express is a real-time multiplayer whiteboard: infinite canvas, live cursors, rooms, and Prisma persistence. React 19, Vite, Express, Socket.io, TypeScript. Vercel hosts the client only; the Node/Socket server is local, and the public URL falls back to a solo canvas if the API is down. Anonymous localStorage name. No accounts, MIT. OSS.

### README.md

# CollabSpace Express

Real-time multiplayer whiteboard - infinite canvas, live cursors, and Prisma-backed rooms.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://collabspace-express.vercel.app)
[![CI](https://github.com/devtechedge/collabspace-express/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/collabspace-express/actions/workflows/ci.yml)
[![React](https://img.shields.io/badge/React-19-61dafb?logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-8-646cff?logo=vite)](https://vite.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Express](https://img.shields.io/badge/Express-4-black?logo=express)](https://expressjs.com/)
[![Socket.io](https://img.shields.io/badge/Socket.io-4-black?logo=socket.io)](https://socket.io/)
[![Prisma](https://img.shields.io/badge/Prisma-5-2D3748?logo=prisma)](https://www.prisma.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://collabspace-express.vercel.app**

> **Status:** Vercel hosts the **Vite client**. There is no public Express/Socket.io process on that URL. When the API is unreachable the client falls back to **localStorage boards** so the live demo is still drawable. Clone and `npm run dev` for real multiplayer (two browser windows on the same room ID).
>
> This is not a production auth or payment product. Identity is an anonymous display name in `localStorage`.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.jpg" alt="CollabSpace" width="800">
</p>

### Dark canvas
![Dark-mode whiteboard with drawings, sidebar and tool rail](docs/screenshots/01-dark-canvas.png)

### Light canvas
![Light-mode whiteboard with rooms and collaborators](docs/screenshots/02-light-canvas.png)

### Empty board
![Dark UI after load - sidebar, infinite canvas, start-drawing hint](docs/screenshots/03-toolbar.png)

---

## Features

- **11 drawing tools** - pencil, highlighter, line, rectangle, circle, text, sticky note, eraser, select, image, laser pointer
- **Live collaboration** - Socket.io rooms, color-coded cursors, laser trails, presence list
- **Infinite canvas** - scroll zoom, Shift-drag / middle-click pan, grid overlay
- **Undo / redo** - local history, broadcast to peers
- **Shareable rooms** - UUID in the URL (`?room=`), join-by-ID in the sidebar
- **Persistence** - boards and elements in SQLite via Prisma (local backend)
- **PNG export**, dark / light theme, keyboard shortcuts (`V` `P` `E` `L` `R` `O` `T`)

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 19, Vite 8, TypeScript, HTML5 Canvas, Lucide |
| Realtime | Socket.io 4 |
| API | Express 4 |
| Data | Prisma 5 + SQLite (swap the provider for Postgres locally) |
| Hosting | Vercel (client). Express is **local** |
| CI | GitHub Actions |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/collabspace-express.git
cd collabspace-express
npm install

cp client/.env.example client/.env
cp server/.env.example server/.env

cd server && npx prisma migrate dev && npx prisma generate && cd ..

npm run dev
```

| Service | URL |
|---------|-----|
| Client | http://localhost:5173 |
| API + WebSocket | http://localhost:5000 |

Open two windows, create a board, paste the room ID in the second - strokes sync live.

---

## Project shape

```
client/                 Vite + React UI (Vercel)
  public/favicon.svg
  src/components/       DrawingBoard, Toolbar, Sidebar
server/                 Express + Socket.io + Prisma
  prisma/schema.prisma
  src/index.ts
```

Prisma is the local production path, not leftover template. The public Vercel alias does not run this server.

---

## Quality

| Check | How |
|-------|-----|
| Unit | Allow-lists, payload sanitizer, board-name rules, element upsert (`npm test`) |
| Types | `npm run typecheck` - server `tsc --noEmit`, client `tsc -b` |
| E2E | Playwright Chromium: shell, create board, pencil tool, theme toggle |
| CI | GitHub Actions - install → Prisma generate → unit → typecheck → e2e |
| Supply chain | Unused Testing Library removed; Dependabot weekly (patch/minor only - do not merge majors blindly) |

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: **no login**. Vercel cannot reach other users' boards.

The local Express engine allow-lists element types, clamps strokes, caps payload size, and reads `CORS_ORIGIN`. **Do not bind port 5000 to the internet** without auth and a locked origin.

Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 28. regulatory_compliance
- **URL:** https://github.com/devtechedge/regulatory_compliance
- **Language:** Python
- **Topics:** compliance, fastapi, hitl, mica, nextjs, rag, vara, web3, docker, postgresql, typescript, vasp
- **Description:** HITL Web3 compliance copilot for VASP licensing reviewers. Maps project packs onto MiCA and VARA with retrieval-bounded findings, article citations, hallucination flags, split-screen accept/edit/reject, and markdown gap exports. Next.js, FastAPI, Postgres. Live Vercel demo-mode (seeded Aurum Custody, no API key). Compose is the full backend.

### README.md

﻿# RegTrace-AI

HITL Web3 compliance copilot for VASP licensing: source-traced MiCA / VARA mapping, hallucination flags, and a human review dashboard.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://regtrace-ai.vercel.app)
[![CI](https://github.com/devtechedge/regulatory_compliance/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/regulatory_compliance/actions/workflows/ci.yml)
[![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-teal?logo=fastapi)](https://fastapi.tiangolo.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

[https://regtrace-ai.vercel.app](https://regtrace-ai.vercel.app)

> **Status:** Vercel demo-mode (Next.js API routes, seeded Aurum Custody, HITL reviews in-memory / reset on cold start). Local Compose remains the full FastAPI + Postgres path. Deterministic retrieval-bounded generator; no API key. Findings are not legal advice. CI on `main` is green (pytest, typecheck, Playwright).
>
> **Demo password (HITL / eval mutations):** `Demo123!` - sent as `x-demo-token` (see [SECURITY.md](SECURITY.md)). Public GET of the seeded pack stays open.

Vercel project Root Directory is `frontend` (Next.js App Router demo API; FastAPI is not part of the Vercel build).

### Demo auth (mutations)

| Item | Value |
|------|--------|
| Header | `x-demo-token` |
| Default password | `Demo123!` |
| Env override | `DEMO_TOKEN` (server), `NEXT_PUBLIC_DEMO_TOKEN` or `localStorage.regtrace_demo_token` (client) |
| Gated routes | `POST /api/projects/{id}/evaluate`, `POST /api/findings/{id}/review` |

Threat model: [SECURITY.md](SECURITY.md).

```bash
cp .env.example .env
docker compose up --build
```

Then http://localhost:3000 (web) and http://localhost:8000/docs (API).

---

## Screenshots

| Overview | HITL workspace |
|----------|----------------|
| ![Dashboard](docs/screenshots/01-overview.png) | ![Split-screen review](docs/screenshots/02-hitl-workspace.png) |

| Gap analysis |
|--------|
| ![Licensing readiness](docs/screenshots/03-gap-analysis.png) |

---

## Features

- HITL accept/edit/reject with logged eval cases
- Source-traced MiCA article and VARA rule citations
- Hallucination flags via citation validator
- 12 MiCA + 12 VARA VASP licensing modules
- Markdown gap export for the licence file

This is compliance engineering, not a smart-contract auditor.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js App Router, TypeScript, Tailwind |
| API | FastAPI, SQLAlchemy 2, pydantic v2 (Compose / local); Next.js App Router demo routes on Vercel |
| Retrieval | BM25 + TF-IDF (no embedding API) |
| Data | Postgres in Compose; SQLite locally; seeded demo JSON on Vercel |
| Generator | Deterministic writer; optional OpenAI |
| Hosting | Vercel demo-mode (same-origin `/api`); Docker Compose for FastAPI + Postgres |

---

## Quick Start

### Vercel demo-mode (same-origin `/api`)

Leave `NEXT_PUBLIC_API_URL` empty. The Next.js app serves seeded Aurum Custody, framework JSON, and a snapshot evaluation from `frontend/app/api/*`. HITL reviews are in-memory and reset on cold start.

### Docker Compose (full FastAPI + Postgres)

Copy `.env.example` to `.env`, set `NEXT_PUBLIC_API_URL=http://localhost:8000`, then start postgres, api, and web with compose.

- API: http://localhost:8000/docs and GET /api/health
- Web: http://localhost:3000
- Postgres: localhost:5432 (user/password/db: regtrace)

No OpenAI key required.

### Local (no Docker)

Postgres is optional. The API defaults to SQLite if DATABASE_URL is unset.

From `backend/`, create a virtualenv, install the Python requirements file, export `DATA_DIR=../frontend/data` and a sqlite `DATABASE_URL`, then start uvicorn on `app.main:app` port 8000.

From `frontend/`, install Node dependencies. Leave `NEXT_PUBLIC_API_URL` empty to use the Next demo API, or export `NEXT_PUBLIC_API_URL=http://localhost:8000` to use FastAPI, then start the Next.js dev server.

Seed runs on API startup. To re-seed after wiping the DB, from backend/: `python -m app.seed`.

### Smoke

```
GET  /api/health
GET  /api/frameworks
POST /api/projects/aurum-custody/evaluate   {"frameworks":["MiCA","VARA"]}
```

## Tests

pytest backend/tests; frontend typecheck; Playwright from frontend/.

## License

MIT. See [LICENSE](LICENSE).



---

## 29. aarop
- **URL:** https://github.com/devtechedge/aarop
- **Language:** TypeScript
- **Topics:** agentic-ai, ai-agents, llm, machine-learning, multi-agent-systems, nextjs, orchestration, python, agentic-loop, observability, state-machine, typescript, vercel
- **Description:** AAROP is a multi-agent system on an explicit PerceiveΓåÆPlanΓåÆActΓåÆObserveΓåÆReflectΓåÆAdapt loop: orchestration, self-verification, resilient recovery, bounded autonomy, replayable traces. Python core with 24 tests and 99% coverage plus a live Next.js demo. Public Vercel is a client-side TypeScript port with a deterministic mock providerΓÇöno API keys. MIT.

### README.md

# 🧠 AAROP - Autonomous Agentic Reasoning & Orchestration Platform

> A reference implementation of a **multi-agent AI system built on agentic-loop engineering principles**: `Perceive → Plan → Act → Observe → Reflect → Adapt`. The loop is an **explicit, inspectable state machine** - not a hidden prompt chain - with bounded autonomy, self-verification, durable checkpointing, and full trace replay.

<p align="left">
  <a href="https://aarop.vercel.app/"><img alt="live demo" src="https://img.shields.io/badge/live%20demo-online-brightgreen"></a>
  <a href="https://github.com/devtechedge/aarop/actions"><img alt="ci" src="https://github.com/devtechedge/aarop/actions/workflows/ci.yml/badge.svg"></a>
  <img alt="python" src="https://img.shields.io/badge/python-3.10%2B-blue">
  <img alt="next" src="https://img.shields.io/badge/Next.js-14-black">
  <img alt="tests" src="https://img.shields.io/badge/tests-24%20passing-brightgreen">
  <img alt="coverage" src="https://img.shields.io/badge/coverage-99%25-brightgreen">
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MIT-black"></a>
</p>

### 🌐 [**▶ Try the Live Demo →**](https://aarop.vercel.app/)
Watch an objective flow through the full agentic loop in real time - no install, no API keys, no sign-up.

> **Live demo status:** 100% client-side TypeScript port with a deterministic mock provider - always online on Vercel. The Python `core/` engine runs offline with the same loop semantics (24 tests, 99% coverage).

**Built by [Devayan Mandal](https://github.com/devtechedge)** - AI / ML Engineer.

---

## Screenshots

| Live agentic loop | Multi-agent orchestration |
|-------------------|---------------------------|
| ![Agentic loop](docs/screenshots/01-agentic-loop.png) | ![Multi-agent](docs/screenshots/02-multi-agent.png) |

| System architecture + engineering rigor |
|-----------------------------------------|
| ![Architecture](docs/screenshots/03-architecture.png) |

---

## What's in this repository

| Path | What it is |
|---|---|
| **[`core/`](core/)** | The Python reference engine - the agentic loop, agents, tool registry, memory, model router, observability. **24 tests, 99% coverage. Runs offline, no API keys.** |
| **[`web-demo/`](web-demo/)** | A **Next.js live demo** ([aarop.vercel.app](https://aarop.vercel.app/)) that animates the full agentic loop in the browser. |
| **[`docs/AAROP_Case_Study.pdf`](docs/AAROP_Case_Study.pdf)** | A polished 4-page case study (problem → architecture → results → ADRs). |
| **[`core/docs/ARCHITECTURE.md`](core/docs/ARCHITECTURE.md)** | C4 diagrams, production reference stack, and 5 ADRs. |
| **[`core/docs/PROJECT_SPEC.md`](core/docs/PROJECT_SPEC.md)** | The full chief-architect-level system specification. |

## The Agentic Loop

```
PERCEIVE → PLAN → ACT → OBSERVE → REFLECT ──accept──► DONE
   ▲                                  │
   └──────────── ADAPT ◄──────reject──┘   (budget exhausted → ESCALATE)
```

| Phase | Responsibility |
|---|---|
| **Perceive** | Normalize input + retrieve relevant context / memory (RAG) |
| **Plan** | Build a cost-aware hierarchical task graph |
| **Act** | Invoke schema-validated, sandboxed tools / sub-agents |
| **Observe** | Capture structured results + detect anomalies |
| **Reflect** | Critic verifies output against acceptance criteria |
| **Adapt** | Replan / retry with backoff / escalate to a human |

Every phase transition emits a structured trace event, so any run is fully reconstructable and replayable. Every run respects step / cost / time budgets and escalates instead of looping forever.

## Repository layout

```
aarop/
├── core/                       # Python reference engine (runs offline, 99% tested)
│   ├── src/aarop/
│   │   ├── core/loop.py        # agentic loop state machine + Budget guardrails
│   │   ├── agents/agents.py    # Planner · Actor · Verifier (critic)
│   │   ├── tools/registry.py   # schema-validated tools, scopes, circuit breaker
│   │   ├── memory/store.py     # working / episodic / semantic memory + RAG
│   │   ├── routing/            # cost-aware model router
│   │   └── observability/      # structured tracing + replay
│   ├── examples/run_demo.py
│   ├── tests/test_loop.py
│   └── docs/                   # ARCHITECTURE.md, PROJECT_SPEC.md
├── web-demo/                   # Next.js 14 live demo (Vercel)
│   ├── app/
│   ├── lib/aarop.ts            # TS port + node:test helpers
│   ├── e2e/                    # Playwright Chromium smokes
│   └── public/favicon.svg
├── docs/
│   ├── AAROP_Case_Study.pdf
│   └── screenshots/
├── SECURITY.md
├── LICENSE
└── README.md
```

## Quickstart

**Core engine (Python):**
```bash
cd core
pip install -e ".[dev]"
python examples/run_demo.py --objective "calculate 21*2 + 8" --verbose
pytest --cov=aarop          # 24 passed · 99% coverage
```

**Live demo (Next.js):**
```bash
cd web-demo
npm ci
npm test                    # node:test helpers (calculator, planner, loop)
npm run typecheck
npm run dev                 # http://localhost:3000
```

## Architecture & engineering rigor

- **Explicit loop state machine** - observable, replayable, crash-recoverable
- **Bounded autonomy** - step / cost / time budgets with human escalation
- **Self-verification** - a critic agent gates every result before commit
- **Resilient tooling** - schema-validated, permission-scoped, retries + circuit breaker + audit log
- **Cost-aware model routing** - cloud + self-hosted, pluggable
- **Observability** - structured trace per run (OpenTelemetry-shaped)
- **99% test coverage** on core orchestration; CI across Python 3.10–3.12, plus web unit tests, `tsc --noEmit`, and Playwright smokes

See **[`core/docs/ARCHITECTURE.md`](core/docs/ARCHITECTURE.md)** for C4 diagrams, the production reference stack (Temporal, FastAPI, pgvector, vLLM, Kubernetes, OpenTelemetry), and **5 Architecture Decision Records**.

## Live demo

The [`web-demo/`](web-demo/) ports the exact loop logic to TypeScript and runs **100% client-side** with a deterministic mock provider - instant, free, and always online. Deployed on Vercel: **[aarop.vercel.app](https://aarop.vercel.app/)**. See [`web-demo/README.md`](web-demo/README.md) for deploy steps.

Threat model for both surfaces: **[`SECURITY.md`](SECURITY.md)**.

## Roadmap

- [ ] Pluggable real LLM provider (OpenAI / Anthropic / self-hosted vLLM)
- [ ] Persistent memory backend (pgvector / Qdrant) + cross-encoder reranker
- [ ] Durable workflow execution via Temporal
- [ ] OpenTelemetry exporter + Grafana dashboards
- [ ] "Bring your own API key" toggle in the live demo

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Issues and PRs welcome.

## License

MIT © 2026 Devayan Mandal - see [`LICENSE`](LICENSE).


---

## 30. aether-flow
- **URL:** https://github.com/devtechedge/aether-flow
- **Language:** TypeScript
- **Topics:** canvas, flowchart, gemini, local-first, portfolio, react, state-machine, tailwindcss, typescript, visual-programming, vite, workflow
- **Description:** AetherFlow is a local-first visual flowchart IDE. Drag nodes on a pan/zoom canvas, compile the graph, and run a sandboxed step simulator with time-travel snapshots. Optional Gemini plus mock Gmail/Drive/Docs nodes. Public Vercel stores graphs in localStorage and uses mock Workspace payloads. React, Vite, TypeScript, Tailwind. No accounts. MIT. OSS.

### README.md

# AetherFlow

Local-first visual flowchart IDE. Drag nodes onto a custom pan/zoom canvas, compile the graph, and run a step simulator with time-travel snapshots.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://aetherflow-ide.vercel.app)
[![CI](https://github.com/devtechedge/aether-flow/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/aether-flow/actions/workflows/ci.yml)
[![React](https://img.shields.io/badge/React-19-0052CC?logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6-646CFF?logo=vite)](https://vitejs.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://aetherflow-ide.vercel.app**

Do **not** use https://aether-flow.vercel.app - that hostname is paused and is not this project.

> **Status:** The live site is a **client-side demo**. Graphs persist in `localStorage`. Gmail / Drive / Docs nodes use mock payloads unless you sign in locally with Firebase env vars. Gemini calls hit `/api/gemini/generate` and fall back to a canned reply when `GEMINI_API_KEY` is unset.

This is the **only** public repo for the project.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.png" alt="AetherFlow" width="800">
</p>

| Canvas | Run |
|--------|-----|
| ![Default pipeline on the canvas](docs/screenshots/01-canvas-overview.png) | ![Compile & run with live console](docs/screenshots/02-pipeline-run.png) |

| Inspector | Version control |
|-----------|-----------------|
| ![Node inspector](docs/screenshots/03-inspector.png) | ![Local git ledger](docs/screenshots/04-version-control.png) |

---

## Features

- Custom SVG canvas (no React Flow / GoJS) with pan, wheel-zoom, 8px snap, and cubic-bezier links
- Quadtree viewport culling so off-screen cards skip DOM work
- Node palette: Start, End, Delay, Logic, Gmail, Drive, Docs, Gemini
- Graph compiler: start/end checks, dangling edges, self-loop reject
- Step simulator with VCR controls and snapshot scrubber
- Local branch / commit ledger on `localStorage` plus a visual added / modified / ghost-deleted overlay
- Optional Gemini proxy and Google Workspace nodes; public demo stays mock

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 19, Vite 6, TypeScript, Tailwind 4 |
| Canvas | SVG + DOM cards, quadtree cull |
| Persistence | `localStorage` (not IndexedDB) |
| Auth | Optional Firebase Google popup - mock mode by default |
| AI | Optional `POST /api/gemini/generate` (Gemini 2.5). Mock fallback on Vercel |
| Local server | Express + Vite middleware (`tsx server.ts`) |
| Hosting | Vercel (static Vite + serverless `/api`) |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/aether-flow.git
cd aether-flow
npm install
cp .env.example .env
npm run dev
```

Open **http://localhost:3000**. Gemini and Google sign-in are optional - the default pipeline runs on mock data.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Security

Portfolio demo: **no login** on the public site. Logic nodes evaluate short expressions with `Function` in the visitor's own browser. The Gemini key, when present, stays on the server.

Details: **[SECURITY.md](SECURITY.md)**.

---

## License

MIT. See [LICENSE](LICENSE).


---

## 31. drizzle-orm
- **URL:** https://github.com/devtechedge/drizzle-orm
- **Language:** TypeScript
- **Topics:** None
- **Description:** ORM

### README.md

<div align="center">
  <img src="./misc/readme/logo-github-sq-dark.svg#gh-dark-mode-only" />
  <img src="./misc/readme/logo-github-sq-light.svg#gh-light-mode-only" />
</div>

<br/>
<div align="center">
  <h3>Headless ORM for NodeJS, TypeScript and JavaScript 🚀</h3>
  <a href="https://orm.drizzle.team">Website</a> •
  <a href="https://orm.drizzle.team/docs/overview">Documentation</a> •
  <a href="https://x.com/drizzleorm">Twitter</a> •
  <a href="https://driz.link/discord">Discord</a>
</div>

<br/>
<br/>

### What's Drizzle?
Drizzle is a modern TypeScript ORM developers [wanna use in their next project](https://stateofdb.com/tools/drizzle). 
It is [lightweight](https://bundlephobia.com/package/drizzle-orm) at only ~7.4kb minified+gzipped, and it's tree shakeable with exactly 0 dependencies. 

**Drizzle supports every PostgreSQL, MySQL and SQLite database**, including serverless ones like [Turso](https://orm.drizzle.team/docs/get-started-sqlite#turso), [Neon](https://orm.drizzle.team/docs/get-started-postgresql#neon), [Xata](https://orm.drizzle.team/docs/connect-xata), [PlanetScale](https://orm.drizzle.team/docs/get-started-mysql#planetscale), [Cloudflare D1](https://orm.drizzle.team/docs/get-started-sqlite#cloudflare-d1), [FlyIO LiteFS](https://fly.io/docs/litefs/), [Vercel Postgres](https://orm.drizzle.team/docs/get-started-postgresql#vercel-postgres), [Supabase](https://orm.drizzle.team/docs/get-started-postgresql#supabase) and [AWS Data API](https://orm.drizzle.team/docs/get-started-postgresql#aws-data-api). No bells and whistles, no Rust binaries, no serverless adapters, everything just works out of the box.

**Drizzle is serverless-ready by design**. It works in every major JavaScript runtime like NodeJS, Bun, Deno, Cloudflare Workers, Supabase functions, any Edge runtime, and even in browsers.  
With Drizzle you can be [**fast out of the box**](https://orm.drizzle.team/benchmarks) and save time and costs while never introducing any data proxies into your infrastructure. 

While you can use Drizzle as a JavaScript library, it shines with TypeScript. It lets you [**declare SQL schemas**](https://orm.drizzle.team/docs/sql-schema-declaration) and build both [**relational**](https://orm.drizzle.team/docs/rqb) and [**SQL-like queries**](https://orm.drizzle.team/docs/select), while keeping the balance between type-safety and extensibility for toolmakers to build on top.  

### Ecosystem
While Drizzle ORM remains a thin typed layer on top of SQL, we made a set of tools for people to have best possible developer experience.  
  
Drizzle comes with a powerful [**Drizzle Kit**](https://orm.drizzle.team/kit-docs/overview) CLI companion for you to have hassle-free migrations. It can generate SQL migration files for you or apply schema changes directly to the database.  
  
We also have [**Drizzle Studio**](https://orm.drizzle.team/drizzle-studio/overview) for you to effortlessly browse and manipulate data in your database of choice.

### Documentation
Check out the full documentation on [the website](https://orm.drizzle.team/docs/overview).

### Our sponsors ❤️
<p align="center">
<a href="https://drizzle.team" target="_blank">
<img src='https://api.drizzle.team/v2/sponsors/svg'/>
</a>
</p>


---

## 32. kit
- **URL:** https://github.com/devtechedge/kit
- **Language:** TypeScript
- **Topics:** None
- **Description:** Solana JavaScript SDK

### README.md

[![npm][npm-image]][npm-url]
[![npm-downloads][npm-downloads-image]][npm-url]
<br />
[![code-style-prettier][code-style-prettier-image]][code-style-prettier-url]

[code-style-prettier-image]: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square
[code-style-prettier-url]: https://github.com/prettier/prettier
[npm-downloads-image]: https://img.shields.io/npm/dm/@solana/kit?style=flat
[npm-image]: https://img.shields.io/npm/v/@solana/kit?style=flat
[npm-url]: https://www.npmjs.com/package/@solana/kit

# Kit

This is the JavaScript SDK for building Solana apps for Node, web, and React Native.

> [!NOTE]
> Did you expect to find `@solana/web3.js` here? You're in the right place! We have renamed the 2.x line of `@solana/web3.js` to `@solana/kit`.
>
> The code for the 1.x line of `@solana/web3.js` can be found [here](https://github.com/solana-labs/solana-web3.js/tree/maintenance/v1.x) and the documentation [here](https://solana-foundation.github.io/solana-web3.js/).

# Installation

For use in a Node.js or web application:

```shell
npm install --save @solana/kit
```

For use in a browser, without a build system:

```html
<!-- Development (debug mode, unminified) -->
<script src="https://unpkg.com/@solana/kit/dist/index.development.js"></script>

<!-- Production (minified) -->
<script src="https://unpkg.com/@solana/kit/dist/index.production.min.js"></script>
```

# Quick Start

To get a feel for the API, run and modify the live examples in the `examples/` directory. There, you will find a series of single-purpose Node scripts that demonstrate a specific feature or use case. You will also find a React application that you can run in a browser, that demonstrates being able to create, sign, and send transactions using browser wallets.

For a fully baked intro, see: [Getting started with Solana kit](https://www.solanakit.com/docs/getting-started)

# What's New in Kit

Kit is a response to many of the pain points you have communicated to us when developing Solana applications with web3.js.

## Tree-Shakability

The object-oriented design of the web3.js (1.x) API prevents optimizing compilers from being able to ‘tree-shake’ unused code from your production builds. No matter how much of the web3.js API you use in your application, you have until now been forced to package all of it.

Read more about tree-shaking here:

- [Mozilla Developer Docs: Tree Shaking](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking)
- [WebPack Docs: Tree Shaking](https://webpack.js.org/guides/tree-shaking/)
- [Web.Dev Blog Article: Reduce JavaScript Payloads with Tree Shaking](https://web.dev/articles/reduce-javascript-payloads-with-tree-shaking)

One example of an API that can’t be tree-shaken is the `Connection` class. It has dozens of methods, but because it’s a _class_ you have no choice but to include every method in your application’s final bundle, no matter how many you _actually_ use.

Needlessly large JavaScript bundles can cause issues with deployments to cloud compute providers like Cloudflare or AWS Lambda. They also impact webapp startup performance because of longer download and JavaScript parse times.

Kit is fully tree-shakable and will remain so, enforced by build-time checks. Optimizing compilers can now eliminate those parts of the library that your application does not use.

Kit is comprised of several smaller, modular packages under the `@solana` organization, including:

- `@solana/accounts`: For fetching and decoding accounts
- `@solana/codecs`: For composing data (de)serializers from a set of primitives or building custom ones
- `@solana/errors`: For identifying and refining coded errors thrown in the `@solana` namespace
- `@solana/rpc`: For sending RPC requests
- `@solana/rpc-subscriptions`: For subscribing to RPC notifications
- `@solana/signers`: For building message and/or transaction signer objects
- `@solana/sysvars`: For fetching and decoding sysvar accounts
- `@solana/transaction-messages`: For building and transforming Solana transaction message objects
- `@solana/transactions`: For compiling and signing transactions for submission to the network
- And many more!

Some of these packages are themselves composed of smaller packages. For instance, `@solana/rpc` is composed of `@solana/rpc-spec` (for core JSON RPC specification types), `@solana/rpc-api` (for the Solana-specific RPC methods), `@solana/rpc-transport-http` (for the default HTTP transport) and so on.

Developers can use the default configurations within the main library (`@solana/kit`) or import any of its subpackages where customization-through-composition is desired.

## Composable Internals

Depending on your use case and your tolerance for certain application behaviours, you may wish to configure your application to make a different set of tradeoffs than another developer. The web3.js (1.x) API imposed a rigid set of common-case defaults on _all_ developers, some of which were impossible to change.

The inability to customize web3.js up until now has been a source of frustration:

- The Mango team wanted to customize the transaction confirmation strategy, but all of that functionality is hidden away behind `confirmTransaction` – a static method of `Connection`. [Here’s the code for `confirmTransaction` on GitHub](https://github.com/solana-labs/solana-web3.js/blob/69a8ad25ef09f9e6d5bff1ffa8428d9be0bd32ac/packages/library-legacy/src/connection.ts#L3734).
- Solana developer ‘mPaella’ [wanted us to add a feature in the RPC](https://github.com/solana-labs/solana-web3.js/issues/1143#issuecomment-1435927152) that would failover to a set of backup URLs in case the primary one failed.
- Solana developer ‘epicfaace’ wanted first-class support for automatic time-windowed batching in the RPC transport. [Here’s their pull request](https://github.com/solana-labs/solana/pull/23628).
- Multiple folks have expressed the need for custom retry logic for failed requests or transactions. [Here’s a pull request from ‘dafyddd’](https://github.com/solana-labs/solana/pull/11811) and [another from ‘abrkn’](https://github.com/solana-labs/solana-web3.js/issues/1041) attempting to modify retry logic to suit their individual use cases.

Kit exposes far more of its internals, particularly where communication with an RPC is concerned, and allows willing developers the ability to compose new implementations from the default ones that manifest a nearly limitless array of customizations.

The individual modules that make up Kit are assembled in a **default** configuration reminiscent of the legacy library as part of the npm package `@solana/kit`, but those who wish to assemble them in different configurations may do so.

Generic types are offered in numerous places, allowing you to specify new functionality, to make extensions to each API via composition and supertypes, and to encourage you to create higher-level opinionated abstractions of your own.

In fact, we expect you to do so, and to open source some of those for use by others with similar needs.

## Modern JavaScript; Zero-Dependency

The advance of modern JavaScript features presents an opportunity to developers of crypto applications, such as the ability to use native Ed25519 keys and to express large values as native `bigint`.

The Web Incubator Community Group has advocated for the addition of Ed25519 support to the [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API), and support has already landed in _most_ modern JavaScript runtimes.

Engine support for `bigint` values has also become commonplace. The older `number` primitive in JavaScript has a maximum value of 2^53 - 1, whereas Rust’s `u64` can represent values up to 2^64.

Kit eliminates userspace implementations of Ed25519 cryptography, large number polyfills, and more, in favour of custom implementations or the use of native JavaScript features, reducing the size of the library. It has no third-party dependencies.

## Functional Architecture

The object oriented, class-based architecture of web3.js (1.x) causes unnecessary bundle bloat. Your application has no choice but to bundle _all_ of the functionality and dependencies of a class no matter how many methods you actually use at runtime.

Class-based architecture also presents unique risks to developers who trigger the dual-package hazard. This describes a situation you can find yourself in if you build for both CommonJS and ES modules. It arises when two copies of the same class are present in the dependency tree, causing checks like `instanceof` to fail. This introduces aggravating and difficult to debug problems.

Read more about dual-package hazard:

- [NodeJS: Dual Package Hazard](https://nodejs.org/api/packages.html#dual-package-hazard)

Kit implements no classes (with the notable exception of the `SolanaError` class) and implements the thinnest possible interfaces at function boundaries.

## Statistics

Consider these statistical comparisons between Kit and the legacy web3.js 1.x.

|                                                                                                        | 1.x (Legacy) | Kit        | +/- % |
| ------------------------------------------------------------------------------------------------------ | ------------ | ---------- | ----- |
| Total minified size of library                                                                         | 81 KB        | 57.5 KB    | -29%  |
| Total minified size of library (when runtime supports Ed25519)                                         | 81 KB        | 53 KB      | -33%  |
| Bundled size of a web application that executes a transfer of lamports                                 | 111 KB       | 23.9 KB    | -78%  |
| Bundled size of a web application that executes a transfer of lamports (when runtime supports Ed25519) | 111 KB       | 18.2 KB    | -83%  |
| Performance of key generation, signing, and verifying signatures (Brave with Experimental API flag)    | 700 ops/s    | 7000 ops/s | +900% |
| First-load size for Solana Explorer                                                                    | 311 KB       | 228 KB     | -26%  |

The re-engineered library achieves these speedups and reductions in bundle size in large part through use of modern JavaScript APIs.

To validate our work, we replaced the legacy 1.x library with Kit on the homepage of the Solana Explorer. Total first-load bundle size dropped by 26% without removing a single feature. [Here’s an X thread](https://twitter.com/callum_codes/status/1679124485218226176) by Callum McIntyre if you would like to dig deeper.

# A Tour of the Kit API

Here’s an overview of how to use the new library to interact with the RPC, configure network transports, work with Ed25519 keys, and to serialize data.

## RPC

Kit ships with an implementation of the [JSON RPC specification](https://www.jsonrpc.org/specification) and a type spec for the [Solana JSON RPC](https://solana.com/docs/rpc).

The main package responsible for managing communication with an RPC is `@solana/rpc`. However, this package makes use of more granular packages to break down the RPC logic into smaller pieces. Namely, these packages are:

- `@solana/rpc`: Contains all logic related to sending Solana RPC calls.
- `@solana/rpc-api`: Describes all Solana RPC methods using types.
- `@solana/rpc-transport-http`: Provides a concrete implementation of an RPC transport using HTTP requests.
- `@solana/rpc-spec`: Defines the JSON RPC spec for sending RPC requests.
- `@solana/rpc-spec-types`: Shared JSON RPC specifications types and helpers that are used by both `@solana/rpc` and `@solana/rpc-subscriptions` (described in the next section).
- `@solana/rpc-types`: Shared Solana RPC types and helpers that are used by both `@solana/rpc` and `@solana/rpc-subscriptions`.

The main `@solana/kit` package re-exports the `@solana/rpc` package so, going forward, we will import RPC types and functions from the library directly.

### RPC Calls

You can use the `createSolanaRpc` function by providing the URL of a Solana JSON RPC server. This will create a default client for interacting with the Solana JSON RPC API.

```ts
import { createSolanaRpc } from '@solana/kit';

// Create an RPC client.
const rpc = createSolanaRpc('http://127.0.0.1:8899');
//    ^? Rpc<SolanaRpcApi>

// Send a request.
const slot = await rpc.getSlot().send();
```

### Custom RPC Transports

The `createSolanaRpc` function communicates with the RPC server using a default HTTP transport that should satisfy most use cases. You can provide your own transport or wrap an existing one to communicate with RPC servers in any way you see fit. In the example below, we explicitly create a transport and use it to create a new RPC client via the `createSolanaRpcFromTransport` function.

```ts
import { createSolanaRpcFromTransport, createDefaultRpcTransport } from '@solana/kit';

// Create an HTTP transport or any custom transport of your choice.
const transport = createDefaultRpcTransport({ url: 'https://api.devnet.solana.com' });

// Create an RPC client using that transport.
const rpc = createSolanaRpcFromTransport(transport);
//    ^? Rpc<SolanaRpcApi>

// Send a request.
const slot = await rpc.getSlot().send();
```

A custom transport can implement specialized functionality such as coordinating multiple transports, implementing retries, and more. Let's take a look at some concrete examples.

#### Round Robin

A ‘round robin’ transport is one that distributes requests to a list of endpoints in sequence.

```ts
import { createDefaultRpcTransport, createSolanaRpcFromTransport, type RpcTransport } from '@solana/kit';

// Create an HTTP transport for each RPC server.
const transports = [
    createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-1.com' }),
    createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-2.com' }),
    createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-3.com' }),
];

// Set up the round-robin transport.
let nextTransport = 0;
async function roundRobinTransport<TResponse>(...args: Parameters<RpcTransport>): Promise<TResponse> {
    const transport = transports[nextTransport];
    nextTransport = (nextTransport + 1) % transports.length;
    return await transport(...args);
}

// Create an RPC client using the round-robin transport.
const rpc = createSolanaRpcFromTransport(roundRobinTransport);
```

#### Sharding

A sharding transport is a kind of distributing transport that sends requests to a particular server based on something about the request itself. Here’s an example that sends requests to different servers depending on the name of the method:

```ts
import { createDefaultRpcTransport, createSolanaRpcFromTransport, type RpcTransport } from '@solana/kit';

// Create multiple transports.
const transportA = createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-1.com' });
const transportB = createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-2.com' });
const transportC = createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-3.com' });
const transportD = createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-4.com' });

// Function to determine which shard to use based on the request method.
function selectShard(method: string): RpcTransport {
    switch (method) {
        case 'getAccountInfo':
        case 'getBalance':
            return transportA;
        case 'getLatestBlockhash':
        case 'getTransaction':
            return transportB;
        case 'sendTransaction':
            return transportC;
        default:
            return transportD;
    }
}

// Create a transport that selects the correct transport given the request method name.
async function shardingTransport<TResponse>(...args: Parameters<RpcTransport>): Promise<TResponse> {
    const payload = args[0].payload as { method: string };
    const selectedTransport = selectShard(payload.method);
    return (await selectedTransport(...args)) as TResponse;
}

// Create an RPC client using the sharding transport.
const rpc = createSolanaRpcFromTransport(shardingTransport);
```

#### Retry

A custom transport is a good place to implement global retry logic for every request:

```ts
import { createDefaultRpcTransport, createSolanaRpcFromTransport, type RpcTransport } from '@solana/kit';

// Set the maximum number of attempts to retry a request.
const MAX_ATTEMPTS = 4;

// Create the default transport.
const defaultTransport = createDefaultRpcTransport({ url: 'https://mainnet-beta.my-server-1.com' });

// Sleep function to wait for a given number of milliseconds.
function sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Calculate the delay for a given attempt.
function calculateRetryDelay(attempt: number): number {
    // Exponential backoff with a maximum of 1.5 seconds.
    return Math.min(100 * Math.pow(2, attempt), 1500);
}

// A retrying transport that will retry up to MAX_ATTEMPTS times before failing.
async function retryingTransport<TResponse>(...args: Parameters<RpcTransport>): Promise<TResponse> {
    let requestError;
    for (let attempts = 0; attempts < MAX_ATTEMPTS; attempts++) {
        try {
            return await defaultTransport(...args);
        } catch (err) {
            requestError = err;
            // Only sleep if we have more attempts remaining.
            if (attempts < MAX_ATTEMPTS - 1) {
                const retryDelay = calculateRetryDelay(attempts);
                await sleep(retryDelay);
            }
        }
    }
    throw requestError;
}

// Create the RPC client using the retrying transport.
const rpc = createSolanaRpcFromTransport(retryingTransport);
```

#### Failover

Support for handling network failures can be implemented in the transport itself. Here’s an example of some failover logic integrated into a transport:

```ts
import { createDefaultRpcTransport, createSolanaRpcFromTransport, type RpcTransport } from '@solana/kit';

// List of RPC endpoints for failover.
const rpcEndpoints = [
    'https://mainnet-beta.my-server-1.com',
    'https://mainnet-beta.my-server-2.com',
    'https://mainnet-beta.my-server-3.com',
    'https://mainnet-beta.my-server-3.com',
];

// Create an array of transports from the endpoints.
const transports = rpcEndpoints.map(url => createDefaultRpcTransport({ url }));

// A failover transport that switches to the next transport on failure.
async function failoverTransport<TResponse>(...args: Parameters<RpcTransport>): Promise<TResponse> {
    let lastError;
    for (const transport of transports) {
        try {
            return await transport(...args);
        } catch (err) {
            lastError = err;
            console.warn(`Transport failed: ${err}. Trying next transport...`);
        }
    }
    // If all transports fail, throw the last error.
    throw lastError;
}

// Create the RPC client using the failover transport.
const rpc = createSolanaRpcFromTransport(failoverTransport);
```

### Augmenting/Constraining the RPC API

Using the `createSolanaRpc` or `createSolanaRpcFromTransport` methods, we always get the same API that includes the Solana RPC API methods. Since the RPC API is described using types only, it is possible to augment those types to add your own methods.

When constraining the API scope, keep in mind that types don’t affect bundle size. You may still like to constrain the type-spec for a variety of reasons, including reducing TypeScript noise.

#### Constraining by Cluster

If you're using a specific cluster, you may wrap your RPC URL inside a helper function like `mainnet` or `devnet` to inject that information into the RPC type system.

```ts
import { createSolanaRpc, mainnet, devnet } from '@solana/kit';

const mainnetRpc = createSolanaRpc(mainnet('https://api.mainnet-beta.solana.com'));
//    ^? RpcMainnet<SolanaRpcApiMainnet>

const devnetRpc = createSolanaRpc(devnet('https://api.devnet.solana.com'));
//    ^? RpcDevnet<SolanaRpcApiDevnet>
```

In the example above, `devnetRpc.requestAirdrop(..)` will work, but `mainnetRpc.requestAirdrop(..)` will raise a TypeScript error since `requestAirdrop` is not a valid method of the mainnet cluster.

#### Cherry-Picking API Methods

You can constrain the API’s type-spec even further so you are left only with the methods you need. The simplest way to do this is to cast the created RPC client to a type that only includes the required methods.

```ts
import { createSolanaRpc, type Rpc, type GetAccountInfoApi, type GetMultipleAccountsApi } from '@solana/kit';

const rpc = createSolanaRpc('http://127.0.0.1:8899') as Rpc<GetAccountInfoApi & GetMultipleAccountsApi>;
```

Alternatively, you can explicitly create the RPC API using the `createSolanaRpcApi` function. You will need to create your own transport and bind the two together using the `createRpc` function.

```ts
import {
    createDefaultRpcTransport,
    createRpc,
    createSolanaRpcApi,
    DEFAULT_RPC_CONFIG,
    type GetAccountInfoApi,
    type GetMultipleAccountsApi,
} from '@solana/kit';

const api = createSolanaRpcApi<GetAccountInfoApi & GetMultipleAccountsApi>(DEFAULT_RPC_CONFIG);
const transport = createDefaultRpcTransport({ url: 'http://127.0.0.1:8899' });

const rpc = createRpc({ api, transport });
```

Note that the `createSolanaRpcApi` function is a wrapper on top of the `createJsonRpcApi` function which adds some Solana-specific transformers such as setting a default commitment on all methods or throwing an error when an integer overflow is detected.

#### Creating Your Own API Methods

The new library’s RPC specification supports an _infinite_ number of JSON-RPC methods with **zero increase** in bundle size.

This means the library can support future additions to the official [Solana JSON RPC](https://docs.solana.com/api), or [custom RPC methods](https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api/get-asset) defined by some RPC provider.

Here’s an example of how a developer at might build a custom RPC type-spec for an RPC provider's implementation of the Metaplex Digital Asset Standard's `getAsset` method:

```ts
// Define the method's response payload.
type GetAssetApiResponse = Readonly<{
    interface: DasApiAssetInterface;
    id: Address;
    content: Readonly<{
        files?: readonly {
            mime?: string;
            uri?: string;
            [key: string]: unknown;
        }[];
        json_uri: string;
        links?: readonly {
            [key: string]: unknown;
        }[];
        metadata: DasApiMetadata;
    }>;
    /* ...etc... */
}>;

// Set up a type spec for the request method.
type GetAssetApi = {
    // Define the method's name, parameters and response type
    getAsset(args: { id: Address }): GetAssetApiResponse;
};

// Export the type spec for downstream users.
export type MetaplexDASApi = GetAssetApi;
```

Here’s how a developer might use it:

```ts
import { createDefaultRpcTransport, createRpc, createJsonRpcApi } from '@solana/kit';

// Create the custom API.
const api = createJsonRpcApi<MetaplexDASApi>();

// Set up an HTTP transport to a server that supports the custom API.
const transport = createDefaultRpcTransport({
    url: 'https://mainnet.helius-rpc.com/?api-key=<api_key>',
});

// Create the RPC client.
const metaplexDASRpc = createRpc({ api, transport });
//    ^? Rpc<MetaplexDASApi>
```

As long as a particular JSON RPC method adheres to the [official JSON RPC specification](https://www.jsonrpc.org/specification), it will be supported by Kit.

### Aborting RPC Requests

RPC requests are now abortable with modern `AbortControllers`. When calling an RPC method such as `getSlot`, it will return a `PendingRpcRequest` proxy object that contains a `send` method to send the request to the server.

```ts
const pendingRequest: PendingRpcRequest<Slot> = rpc.getSlot();

const slot: Slot = await pendingRequest.send();
```

The arguments of the `getSlot` method are reserved for the request payload, but the `send` method is where additional arguments such as an `AbortSignal` can be accepted in the context of the request.

Aborting RPC requests can be useful for a variety of things such as setting a timeout on a request or cancelling a request when a user navigates away from a page.

```ts
import { createSolanaRpc } from '@solana/kit';

const rpc = createSolanaRpc('http://127.0.0.1:8900');

// Create a new AbortController.
const abortController = new AbortController();

// Abort the request when the user navigates away from the current page.
function onUserNavigateAway() {
    abortController.abort();
}

// The request will be aborted if and only if the user navigates away from the page.
const slot = await rpc.getSlot().send({ abortSignal: abortController.signal });
```

Read more about `AbortController` here:

- [Mozilla Developer Docs: `AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
- [Mozilla Developer Docs: `AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)
- [JavaScript.info: Fetch: Abort](https://javascript.info/fetch-abort)

## RPC Subscriptions

Subscriptions in the legacy library do not allow custom retry logic and do not allow you to recover from potentially missed messages. The new version does away with silent retries, surfaces transport errors to your application, and gives you the opportunity to recover from gap events.

The main package responsible for managing communication with RPC subscriptions is `@solana/rpc-subscriptions`. However, similarly to `@solana/rpc`, this package also makes use of more granular packages. These packages are:

- `@solana/rpc-subscriptions`: Contains all logic related to subscribing to Solana RPC notifications.
- `@solana/rpc-subscriptions-api`: Describes all Solana RPC subscriptions using types.
- `@solana/rpc-subscriptions-channel-websocket`: Provides a concrete implementation of an RPC Subscriptions channel using WebSockets.
- `@solana/rpc-subscriptions-spec`: Defines the JSON RPC spec for subscribing to RPC notifications.
- `@solana/rpc-spec-types`: Shared JSON RPC specifications types and helpers that are used by both `@solana/rpc` and `@solana/rpc-subscriptions`.
- `@solana/rpc-types`: Shared Solana RPC types and helpers that are used by both `@solana/rpc` and `@solana/rpc-subscriptions`.

Since the main `@solana/kit` library also re-exports the `@solana/rpc-subscriptions` package we will import RPC Subscriptions types and functions directly from the main library going forward.

### Getting Started with RPC Subscriptions

To get started with RPC Subscriptions, you may use the `createSolanaRpcSubscriptions` function by providing the WebSocket URL of a Solana JSON RPC server. This will create a default client for interacting with Solana RPC Subscriptions.

```ts
import { createSolanaRpcSubscriptions } from '@solana/kit';

// Create an RPC Subscriptions client.
const rpcSubscriptions = createSolanaRpcSubscriptions('ws://127.0.0.1:8900');
//    ^? RpcSubscriptions<SolanaRpcSubscriptionsApi>
```

### Subscriptions as `AsyncIterators`

The new subscriptions API vends subscription notifications as an `AsyncIterator`. The `AsyncIterator` conforms to the [async iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols), which allows developers to consume messages using a `for await...of` loop.

Here’s an example of working with a subscription in the new library:

```ts
import { address, createSolanaRpcSubscriptions, createDefaultRpcSubscriptionsTransport } from '@solana/kit';

// Create the RPC Subscriptions client.
const rpcSubscriptions = createSolanaRpcSubscriptions('ws://127.0.0.1:8900');

// Set up an abort controller.
const abortController = new AbortController();

// Subscribe to account notifications.
const accountNotifications = await rpcSubscriptions
    .accountNotifications(address('AxZfZWeqztBCL37Mkjkd4b8Hf6J13WCcfozrBY6vZzv3'), { commitment: 'confirmed' })
    .subscribe({ abortSignal: abortController.signal });

try {
    // Consume messages.
    for await (const notification of accountNotifications) {
        console.log('New balance', notification.value.lamports);
    }
} catch (e) {
    // The subscription went down.
    // Retry it and then recover from potentially having missed
    // a balance update, here (eg. by making a `getBalance()` call).
}
```

You can read more about `AsyncIterator` at the following links:

- [Mozilla Developer Docs: `AsyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)
- [Luciano Mammino (Blog): JavaScript Async Iterators](https://www.nodejsdesignpatterns.com/blog/javascript-async-iterators/)

### Aborting RPC Subscriptions

Similarly to RPC calls, applications can terminate active subscriptions using an `AbortController` attribute on the `subscribe` method. In fact, this parameter is _required_ for subscriptions to encourage you to clean up subscriptions that your application no longer needs.

Let's take a look at some concrete examples that demonstrate how to abort subscriptions.

#### Subscription Timeout

Here's an example of an `AbortController` used to abort a subscription after a 5-second timeout:

```ts
import { createSolanaRpcSubscriptions } from '@solana/kit';

const rpcSubscriptions = createSolanaRpcSubscriptions('ws://127.0.0.1:8900');

// Subscribe for slot notifications using an AbortSignal that times out after 5 seconds.
const slotNotifications = await rpcSubscriptions
    .slotNotifications()
    .subscribe({ abortSignal: AbortSignal.timeout(5000) });

// Log slot notifications.
for await (const notification of slotNotifications) {
    console.log('Slot notification', notification);
}

console.log('Done.');
```

Read more about `AbortController` at the following links:

- [Mozilla Developer Docs: `AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
- [Mozilla Developer Docs: `AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)
- [JavaScript.info: Fetch: Abort](https://javascript.info/fetch-abort)

#### Cancelling Subscriptions

It is also possible to abort a subscription inside the `for await...of` loop. This enables us to cancel a subscription based on some condition, such as a change in the state of an account. For instance, the following example cancels a subscription when the owner of an account changes:

```ts
// Subscribe to account notifications.
const accountNotifications = await rpc
    .accountNotifications(address('AxZfZWeqztBCL37Mkjkd4b8Hf6J13WCcfozrBY6vZzv3'), { commitment: 'confirmed' })
    .subscribe({ abortSignal });

// Consume messages.
let previousOwner = null;
for await (const notification of accountNotifications) {
    const {
        value: { owner },
    } = notification;
    // Check the owner to see if it has changed
    if (previousOwner && owner !== previousOwner) {
        // If so, abort the subscription
        abortController.abort();
    } else {
        console.log(notification);
    }
    previousOwner = owner;
}
```

### Failed vs. Aborted Subscriptions

It is important to note that a subscription failure behaves differently from a subscription abort. A subscription failure occurs when the subscription goes down and will throw an error that can be intercepted in a `try/catch`. However, an aborted subscription will not throw an error, but will instead exit the `for await...of` loop.

```ts
try {
    for await (const notification of notifications) {
        // Consume messages.
    }
    // [ABORTED] Reaching this line means the subscription was aborted — i.e. unsubscribed.
} catch (e) {
    // [FAILED] Reaching this line means the subscription went down.
    // Retry it, then recover from potential missed messages.
} finally {
    // [ABORTED or FAILED] Whether the subscription failed or was aborted, you can run cleanup code here.
}
```

### Message Gap Recovery

One of the most crucial aspects of any subscription API is managing potential missed messages. Missing messages, such as account state updates, could be catastrophic for an application. That’s why the new library provides native support for recovering missed messages using the `AsyncIterator`.

When a connection fails unexpectedly, any messages you miss while disconnected can result in your UI falling behind or becoming corrupt. Because subscription failure is now made explicit in the new API, you can implement ‘catch-up’ logic after re-establishing the subscription.

Here’s an example of such logic:

```ts
try {
    for await (const notif of accountNotifications) {
        updateAccountBalance(notif.lamports);
    }
} catch (e) {
    // The subscription failed.
    // First, re-establish the subscription.
    await setupAccountBalanceSubscription(address);
    // Then make a one-shot request to 'catch up' on any missed balance changes.
    const { value: lamports } = await rpc.getBalance(address).send();
    updateAccountBalance(lamports);
}
```

### Using Custom RPC Subscriptions Transports

The `createSolanaRpcSubscriptions` function communicates with the RPC server using a default `WebSocket` channel that should satisfy most use cases. However, you may here as well provide your own channel creator or decorate existing ones to communicate with RPC servers in any way you see fit. In the example below, we supply a custom `WebSocket` channel creator and use it to create a new RPC Subscriptions client via the `createSolanaRpcSubscriptionsFromTransport` function.

```ts
import { createDefaultRpcSubscriptionsTransport, createSolanaRpcSubscriptionsFromTransport } from '@solana/kit';

// Create a transport with a custom channel creator of your choice.
const transport = createDefaultRpcSubscriptionsTransport({
    createChannel({ abortSignal }) {
        return createWebSocketChannel({
            maxSubscriptionsPerChannel: 100,
            minChannels: 25,
            sendBufferHighWatermark: 32_768,
            signal: abortSignal,
            url: 'ws://127.0.0.1:8900',
        });
    },
});

// Create an RPC client using that transport.
const rpcSubscriptions = createSolanaRpcSubscriptionsFromTransport(transport);
//    ^? RpcSubscriptions<SolanaRpcSubscriptionsApi>
```

### Augmenting/Constraining the RPC Subscriptions API

Using the `createSolanaRpcSubscriptions` or `createSolanaRpcSubscriptionsFromTransport` functions, we always get the same RPC Subscriptions API, including all Solana RPC stable subscriptions. However, since the RPC Subscriptions API is described using types only, it is possible to constrain the API to a specific set of subscriptions or even add your own custom subscriptions.

#### Constraining by Cluster

If you're using a specific cluster, you may wrap your RPC URL inside a helper function like `mainnet` or `devnet` to inject that information into the RPC type system.

```ts
import { createSolanaRpcSubscriptions, mainnet, devnet } from '@solana/kit';

const mainnetRpc = createSolanaRpcSubscriptions(mainnet('https://api.mainnet-beta.solana.com'));
//    ^? RpcSubscriptionsMainnet<SolanaRpcSubscriptionsApi>

const devnetRpc = createSolanaRpcSubscriptions(devnet('https://api.devnet.solana.com'));
//    ^? RpcSubscriptionsDevnet<SolanaRpcSubscriptionsApi>
```

#### Including Unstable Subscriptions

If your app needs access to [unstable RPC Subscriptions](https://solana.com/docs/rpc/websocket/blocksubscribe) — e.g. `BlockNotificationsApi` or `SlotsUpdatesNotificationsApi` — and your RPC server supports them, you may use the `createSolanaRpcSubscriptions_UNSTABLE` and `createSolanaRpcSubscriptionsFromTransport_UNSTABLE` functions to create an RPC Subscriptions client that includes those subscriptions.

```ts
import {
    createDefaultSolanaRpcSubscriptionsChannelCreator,
    createDefaultRpcSubscriptionsTransport,
    createSolanaRpcSubscriptions_UNSTABLE,
    createSolanaRpcSubscriptionsFromTransport_UNSTABLE,
} from '@solana/kit';

// Using the default WebSocket channel.
const rpcSubscriptions = createSolanaRpcSubscriptions_UNSTABLE('ws://127.0.0.1:8900');
//    ^? RpcSubscriptions<SolanaRpcSubscriptionsApi & SolanaRpcSubscriptionsApiUnstable>

// Using a custom transport.
const transport = createDefaultRpcSubscriptionsTransport({
    createChannel: createDefaultSolanaRpcSubscriptionsChannelCreator({
        url: 'ws://127.0.0.1:8900',
    }),
});
const rpcSubscriptions = createSolanaRpcSubscriptionsFromTransport_UNSTABLE(transport);
//    ^? RpcSubscriptions<SolanaRpcSubscriptionsApi & SolanaRpcSubscriptionsApiUnstable>
```

#### Cherry-Picking API Methods

You may constrain the scope of the Subscription API even further so you are left only with the subscriptions you need. The simplest way to do this is to cast the created RPC client to a type that only includes the methods you need.

```ts
import {
    createSolanaRpcSubscriptions,
    type RpcSubscriptions,
    type AccountNotificationsApi,
    type SlotNotificationsApi,
} from '@solana/kit';

const rpc = createSolanaRpcSubscriptions('ws://127.0.0.1:8900') as RpcSubscriptions<
    AccountNotificationsApi & SlotNotificationsApi
>;
```

Alternatively, you may explicitly create the RPC Subscriptions API using the `createSolanaRpcSubscriptionsApi` function. You will then need to create your own transport explicitly and bind the two together using the `createSubscriptionRpc` function.

```ts
import {
    createDefaultSolanaRpcSubscriptionsChannelCreator,
    createDefaultRpcSubscriptionsTransport,
    createSubscriptionRpc,
    createSolanaRpcSubscriptionsApi,
    DEFAULT_RPC_CONFIG,
    type AccountNotificationsApi,
    type SlotNotificationsApi,
} from '@solana/kit';

const api = createSolanaRpcSubscriptionsApi<AccountNotificationsApi & SlotNotificationsApi>(DEFAULT_RPC_CONFIG);
const transport = createDefaultRpcSubscriptionsTransport({
    createChannel: createDefaultSolanaRpcSubscriptionsChannelCreator({
        url: 'ws://127.0.0.1:8900',
    }),
});
const rpcSubscriptions = createSubscriptionRpc({ api, transport });
```

Note that the `createSolanaRpcSubscriptionsApi` function is a wrapper on top of the `createRpcSubscriptionsApi` function which adds some Solana-specific transformers such as setting a default commitment on all methods or throwing an error when an integer overflow is detected.

## Keys

The new library takes a brand-new approach to Solana key pairs and addresses, which will feel quite different from the classes `PublicKey` and `Keypair` from version 1.x.

### Web Crypto API

All key operations now use the native Ed25519 implementation in JavaScript’s Web Crypto API.

The API itself is designed to be a more reliably secure way to manage highly sensitive secret key information, but **developers should still use extreme caution when dealing with secret key bytes in their applications**.

One thing to note is that many operations from Web Crypto – such as importing, generating, signing, and verifying are now **asynchronous**.

Here’s an example of generating a `CryptoKeyPair` using the Web Crypto API and signing a message:

```ts
import { generateKeyPair, signBytes, verifySignature } from '@solana/kit';

const keyPair: CryptoKeyPair = await generateKeyPair();

const message = new Uint8Array(8).fill(0);

const signedMessage = await signBytes(keyPair.privateKey, message);
//    ^? Signature

const verified = await verifySignature(keyPair.publicKey, signedMessage, message);
```

### Web Crypto Polyfill

Wherever Ed25519 is not supported, we offer a polyfill for Web Crypto’s Ed25519 API.

This polyfill can be found at `@solana/webcrypto-ed25519-polyfill` and mimics the functionality of the Web Crypto API for Ed25519 key pairs using the same userspace implementation we used in web3.js 1.x. It does not polyfill other algorithms.

Determine if your target runtime supports Ed25519, and install the polyfill if it does not:

```ts
import { install } from '@solana/webcrypto-ed25519-polyfill';
import { generateKeyPair, signBytes, verifySignature } from '@solana/kit';

install();
const keyPair: CryptoKeyPair = await generateKeyPair();

/* Remaining logic */
```

You can see where Ed25519 is currently supported in [this GitHub issue](https://github.com/WICG/webcrypto-secure-curves/issues/20) on the Web Crypto repository. Consider sniffing the user-agent when deciding whether or not to deliver the polyfill to browsers.

Operations on `CryptoKey` objects using the Web Crypto API _or_ the polyfill are mostly handled by the `@solana/keys` package.

### String Addresses

All addresses are now JavaScript strings. They are represented by the opaque type `Address`, which describes exactly what a Solana address actually is.

Consequently, that means no more `PublicKey`.

Here’s what they look like in development:

```ts
import { Address, address, getAddressFromPublicKey, generateKeyPair } from '@solana/kit';

// Coerce a string to an `Address`
const myOtherAddress = address('AxZfZWeqztBCL37Mkjkd4b8Hf6J13WCcfozrBY6vZzv3');

// Typecast it instead
const myAddress =
    'AxZfZWeqztBCL37Mkjkd4b8Hf6J13WCcfozrBY6vZzv3' as Address<'AxZfZWeqztBCL37Mkjkd4b8Hf6J13WCcfozrBY6vZzv3'>;

// From CryptoKey
const keyPair = await generateKeyPair();
const myPublicKeyAsAddress = await getAddressFromPublicKey(keyPair.publicKey);
```

Some tooling for working with base58-encoded addresses can be found in the `@solana/addresses` package.

## Transactions

### Creating Transaction Messages

Like many other familiar aspects of the 1.0 library, transactions have received a makeover.

For starters, all transaction messages are now version-aware, so there’s no longer a need to juggle two different types (eg. `Transaction` vs. `VersionedTransaction`).

Address lookups are now completely described inside transaction message instructions, so you don’t have to materialize `addressTableLookups` anymore.

Here’s a simple example of creating a transaction message &ndash; notice how its type is refined at each step of the process:

```ts
import {
    address,
    createTransactionMessage,
    setTransactionMessageFeePayer,
    setTransactionMessageLifetimeUsingBlockhash,
    Blockhash,
} from '@solana/kit';

const recentBlockhash = {
    blockhash: '4uhcVJyU9pJkvQyS88uRDiswHXSCkY3zQawwpjk2NsNY' as Blockhash,
    lastValidBlockHeight: 196055492n,
};
const feePayer = address('AxZfZWeqztBCL37Mkjkd4b8Hf6J13WCcfozrBY6vZzv3');

// Create a new transaction message
const transactionMessage = createTransactionMessage({ version: 0 });
//    ^? V0TransactionMessage

// Set the fee payer
const transactionMessageWithFeePayer = setTransactionMessageFeePayer(feePayer, transactionMessage);
//    ^? V0TransactionMessage & TransactionMessageWithFeePayer

const transactionMessageWithFeePayerAndLifetime = setTransactionMessageLifetimeUsingBlockhash(
    // ^? V0TransactionMessage & TransactionMessageWithFeePayer & TransactionMessageWithBlockhashLifetime
    recentBlockhash,
    transactionMessageWithFeePayer,
);
```

As you can see, each time a transaction message is modified, the type reflects its new shape. If you add a fee payer, you’ll get a type representing a transaction message with a fee payer, and so on.

Transaction message objects are also **frozen by these functions** to prevent them from being mutated in place.

### Signing Transaction Messages

The `signTransaction(..)` function will raise a type error if your transaction message is not already equipped with a fee payer and a lifetime. This helps you catch errors at author-time instead of runtime.

```ts
const feePayer = await generateKeyPair();
const feePayerAddress = await getAddressFromPublicKey(feePayer.publicKey);

const transactionMessage = createTransactionMessage({ version: 'legacy' });
const transactionMessageWithFeePayer = setTransactionMessageFeePayer(feePayerAddress, transactionMessage);

// Attempting to sign the transaction message without a lifetime will throw a type error
const signedTransaction = await signTransaction([signer], transactionMessageWithFeePayer);
// => "Property 'lifetimeConstraint' is missing in type"
```

### Calibrating a Transaction Message's Compute Unit Budget

Correctly budgeting a compute unit limit for your transaction message can increase the probability that your transaction will be accepted for processing. If you don't declare a compute unit limit on your transaction, validators will assume an upper limit of 200K compute units (CU) per instruction.

Since validators have an incentive to pack as many transactions into each block as possible, they may choose to include transactions that they know will fit into the remaining compute budget for the current block over transactions that might not. For this reason, you should set a compute unit limit on each of your transaction messages, whenever possible.

Use these utilities to estimate the actual compute unit cost of a given transaction message and set it on the message.

```ts
import { createSolanaRpc, estimateComputeUnitLimitFactory, setTransactionMessageComputeUnitLimit } from '@solana/kit';

// Create an estimator function.
const rpc = createSolanaRpc('http://127.0.0.1:8899');
const estimateComputeUnitLimit = estimateComputeUnitLimitFactory({ rpc });

// Create your transaction message.
const transactionMessage = pipe(
    createTransactionMessage({ version: 'legacy' }),
    /* ... */
);

// Request an estimate of the actual compute units this message will consume.
const computeUnitsEstimate = await estimateComputeUnitLimit(transactionMessage);

// Set the transaction message's compute unit budget.
const transactionMessageWithComputeUnitLimit = setTransactionMessageComputeUnitLimit(
    computeUnitsEstimate,
    transactionMessage,
);
```

> [!NOTE]
> For legacy and v0 transactions, if the transaction message does not already have a `SetComputeUnitLimit` instruction, the estimator will add one before simulation. This ensures that the compute unit consumption of the instruction itself is included in the estimate.

Alternatively, use `estimateAndSetComputeUnitLimitFactory` to estimate and set the compute unit limit in a single step. Pair it with `fillTransactionMessageProvisoryComputeUnitLimit` during transaction construction to reserve space for the limit that will later be estimated.

```ts
import {
    estimateAndSetComputeUnitLimitFactory,
    estimateComputeUnitLimitFactory,
    fillTransactionMessageProvisoryComputeUnitLimit,
} from '@solana/kit';

// During construction, reserve space for the compute unit limit.
const messageWithProvisoryLimit = fillTransactionMessageProvisoryComputeUnitLimit(transactionMessage);

// Later, estimate and replace the provisory limit.
const estimator = estimateComputeUnitLimitFactory({ rpc });
const estimateAndSet = estimateAndSetComputeUnitLimitFactory(estimator);
const updatedMessage = await estimateAndSet(messageWithProvisoryLimit);
```

> [!WARNING]
> The compute unit estimate is just that &ndash; an estimate. The compute unit consumption of the actual transaction might be higher or lower than what was observed in simulation. Unless you are confident that your particular transaction message will consume the same or fewer compute units as was estimated, you might like to augment the estimate by either a fixed number of CUs or a multiplier.

> [!NOTE]
> If you are preparing an _unsigned_ transaction, destined to be signed and submitted to the network by a wallet, you might like to leave it up to the wallet to determine the compute unit limit. Consider that the wallet might have a more global view of how many compute units certain types of transactions consume, and might be able to make better estimates of an appropriate compute unit budget.

### Helpers For Building Transaction Messages

Building transaction messages in this manner might feel different from what you’re used to. Also, we certainly wouldn’t want you to have to bind transformed transaction messages to a new variable at each step, so we have released a functional programming library dubbed `@solana/functional` that lets you build transaction messages in **pipelines**. Here’s how it can be used:

```ts
import { pipe } from '@solana/functional';
import {
    address,
    createTransactionMessage,
    setTransactionMessageFeePayer,
    setTransactionMessageLifetimeUsingBlockhash,
    Blockhash,
} from '@solana/kit';

// Use `pipe(..)` to create a pipeline of transaction message transformation operations
const transactionMessage = pipe(
    createTransactionMessage({ version: 0 }),
    tx => setTransactionMessageFeePayer(feePayer, tx),
    tx => setTransactionMessageLifetimeUsingBlockhash(recentBlockhash, tx),
);
```

Note that `pipe(..)` is general-purpose, so it can be used to pipeline any functional transforms.

## Codecs

We have taken steps to make it easier to write data (de)serializers, especially as they pertain to Rust datatypes and byte buffers.

Solana’s codecs libraries are broken up into modular components so you only need to import the ones you need. They are:

- `@solana/codecs-core`: The core codecs library for working with codecs serializers and creating custom ones
- `@solana/codecs-numbers`: Used for serialization of numbers (little-endian and big-endian bytes, etc.)
- `@solana/codecs-strings`: Used for serialization of strings
- `@solana/codecs-data-structures`: Codecs and serializers for structs
- `@solana/options`: Designed to build codecs and serializers for types that mimic Rust’s enums, which can include embedded data within their variants such as values, tuples, and structs

These packages are included in the main `@solana/kit` library but you may also import them from `@solana/codecs` if you only need the codecs.

Here’s an example of encoding and decoding a custom struct with some strings and numbers:

```ts
import { addCodecSizePrefix } from '@solana/codecs-core';
import { getStructCodec } from '@solana/codecs-data-structures';
import { getU32Codec, getU64Codec, getU8Codec } from '@solana/codecs-numbers';
import { getUtf8Codec } from '@solana/codecs-strings';

// Equivalent in Rust:
// struct {
//     amount: u64,
//     decimals: u8,
//     name: String,
// }
const structCodec = getStructCodec([
    ['amount', getU64Codec()],
    ['decimals', getU8Codec()],
    ['name', addCodecSizePrefix(getUtf8Codec(), getU32Codec())],
]);

const myToken = {
    amount: 1000000000000000n, // `bigint` or `number` is supported
    decimals: 2,
    name: 'My Token',
};

const myEncodedToken: Uint8Array = structCodec.encode(myToken);
const myDecodedToken = structCodec.decode(myEncodedToken);

myDecodedToken satisfies {
    amount: bigint;
    decimals: number;
    name: string;
};
```

You may only need to encode or decode data, but not both. Importing one or the other allows your optimizing compiler to tree-shake the other implementation away:

```ts
import { Codec, combineCodec, Decoder, Encoder, addDecoderSizePrefix, addEncoderSizePrefix } from '@solana/codecs-core';
import { getStructDecoder, getStructEncoder } from '@solana/codecs-data-structures';
import {
    getU8Decoder,
    getU8Encoder,
    getU32Decoder,
    getU32Encoder,
    getU64Decoder,
    getU64Encoder,
} from '@solana/codecs-numbers';
import { getUtf8Decoder, getUtf8Encoder } from '@solana/codecs-strings';

export type MyToken = {
    amount: bigint;
    decimals: number;
    name: string;
};

export type MyTokenArgs = {
    amount: number | bigint;
    decimals: number;
    name: string;
};

export const getMyTokenEncoder = (): Encoder<MyTokenArgs> =>
    getStructEncoder([
        ['amount', getU64Encoder()],
        ['decimals', getU8Encoder()],
        ['name', addEncoderSizePrefix(getUtf8Encoder(), getU32Encoder())],
    ]);

export const getMyTokenDecoder = (): Decoder<MyToken> =>
    getStructDecoder([
        ['amount', getU64Decoder()],
        ['decimals', getU8Decoder()],
        ['name', addDecoderSizePrefix(getUtf8Decoder(), getU32Decoder())],
    ]);

export const getMyTokenCodec = (): Codec<MyTokenArgs, MyToken> =>
    combineCodec(getMyTokenEncoder(), getMyTokenDecoder());
```

You can read more about codecs in [the official Codec documentation](https://github.com/anza-xyz/kit/blob/main/packages/codecs/README.md).

## Type-Safety

The new library makes use of some advanced TypeScript features, including generic types, conditional types, `Parameters<..>`, `ReturnType<..>` and more.

We’ve described the RPC API in detail so that TypeScript can determine the _exact_ type of the result you will receive from the server given a particular input. Change the type of the input, and you will see the return type reflect that change.

### RPC Types

The RPC methods – both HTTP and subscriptions – are built with multiple overloads and conditional types. The expected HTTP response payload or subscription message format will be reflected in the return type of the function you’re working with when you provide the inputs in your code.

Here’s an example of this in action:

```ts
// Provide one set of parameters, get a certain type
// These parameters resolve to return type:
// {
//     blockhash: Blockhash;
//     blockHeight: bigint;
//     blockTime: UnixTimestamp;
//     parentSlot: bigint;
//     previousBlockhash: Blockhash;
// }
const blockResponse = await rpc
    .getBlock(0n, {
        rewards: false,
        transactionDetails: 'none',
    })
    .send();

// Switch `rewards` to `true`, get `rewards` in the return type
// {
//     /* ... Previous response */
//     rewards: Reward[];
// }
const blockWithRewardsResponse = await rpc
    .getBlock(0n, {
        rewards: true,
        transactionDetails: 'none',
    })
    .send();

// Switch `transactionDetails` to `full`, get `transactions` in the return type
// {
//     /* ... Previous response */
//     transactions: TransactionResponse[];
// }
const blockWithRewardsAndTransactionsResponse = await rpc
    .getBlock(0n, {
        rewards: true,
        transactionDetails: 'full',
    })
    .send();
```

### Catching Compile-Time Bugs with TypeScript

As previously mentioned, the type coverage in Kit allows developers to catch common bugs at compile time, rather than runtime.

In the example below, a transaction message is created and then attempted to be signed without setting the fee payer. This would result in a runtime error from the RPC, but instead you will see a type error from TypeScript as you type:

```ts
const transactionMessage = pipe(createTransactionMessage({ version: 0 }), tx =>
    setTransactionMessageLifetimeUsingBlockhash(recentBlockhash, tx),
);
const signedTransaction = await signTransaction([keyPair], transactionMessage); // ERROR: Property 'feePayer' is missing in type
```

Consider another example where a developer is attempting to send a transaction that has not been fully signed. Again, the TypeScript compiler will throw a type error:

```ts
const transactionMessage = pipe(
    createTransactionMessage({ version: 0 }),
    tx => setTransactionMessageFeePayer(feePayerAddress, tx),
    tx => setTransactionMessageLifetimeUsingBlockhash(recentBlockhash, tx),
);

const signedTransaction = await signTransaction([], transactionMessage);

// Asserts the transaction is a `FullySignedTransaction`
// Throws an error if any signatures are missing!
assertIsFullySignedTransaction(signedTransaction);

await sendAndConfirmTransaction(signedTransaction);
```

Are you building a nonce transaction and forgot to make `AdvanceNonce` the first instruction? That’s a type error:

```ts
const feePayer = await generateKeyPair();
const feePayerAddress = await getAddressFromPublicKey(feePayer.publicKey);

const notNonceTransactionMessage = pipe(createTransactionMessage({ version: 0 }), tx =>
    setTransactionMessageFeePayer(feePayerAddress, tx),
);

notNonceTransactionMessage satisfies TransactionMessageWithDurableNonceLifetime;
// => Property 'lifetimeConstraint' is missing in type

const nonceConfig = {
    nonce: 'nonce' as Nonce,
    nonceAccountAddress: address('5tLU66bxQ35so2bReGcyf3GfMMAAauZdNA1N4uRnKQu4'),
    nonceAuthorityAddress: address('GDhj8paPg8woUzp9n8fj7eAMocN5P7Ej3A7T9F5gotTX'),
};

const stillNotNonceTransactionMessage = {
    lifetimeConstraint: nonceConfig,
    ...notNonceTransactionMessage,
};

stillNotNonceTransactionMessage satisfies TransactionMessageWithDurableNonceLifetime;
// => 'readonly Instruction<string>[]' is not assignable to type 'readonly [AdvanceNonceAccountInstruction<string, string>, ...Instruction<string>[]]'

const validNonceTransactionMessage = pipe(
    createTransactionMessage({ version: 0 }),
    tx => setTransactionMessageFeePayer(feePayerAddress, tx),
    tx => setTransactionMessageLifetimeUsingDurableNonce(nonceConfig, tx), // Adds the instruction!
);

validNonceTransactionMessage satisfies TransactionMessageWithDurableNonceLifetime; // OK
```

The library’s type-checking can even catch you using lamports instead of SOL for a value:

```ts
const airdropAmount = 1n; // SOL
const signature = rpc.requestAirdrop(myAddress, airdropAmount).send();
```

It will force you to cast the numerical value for your airdrop (or transfer, etc.) amount using `lamports()`, which should be a good reminder!

```ts
const airdropAmount = lamports(1000000000n);
const signature = rpc.requestAirdrop(myAddress, airdropAmount).send();
```

## Compatibility Layer

You will have noticed by now that Kit is a complete and total breaking change from the web3.js 1.x line. We want to provide you with a strategy for interacting with web3.js 1.x APIs while building your application using Kit. You need a tool for converting between web3.js 1.x and Kit data types.

The `@solana/compat` library allows for interoperability between functions and class objects from the legacy library - such as `VersionedTransaction`, `PublicKey`, and `Keypair` - and functions and types of the new library - such as `Address`, `Transaction`, and `CryptoKeyPair`.

Here’s how you can use `@solana/compat` to convert from a legacy `PublicKey` to an `Address`:

```ts
import { fromLegacyPublicKey } from '@solana/compat';

const publicKey = new PublicKey('B3piXWBQLLRuk56XG5VihxR4oe2PSsDM8nTF6s1DeVF5');
const address: Address = fromLegacyPublicKey(publicKey);
```

Here’s how to convert from a legacy `Keypair` to a `CryptoKeyPair`:

```ts
import { fromLegacyKeypair } from '@solana/compat';

const keypairLegacy = Keypair.generate();
const cryptoKeyPair: CryptoKeyPair = fromLegacyKeypair(keypair);
```

Here’s how to convert legacy transaction objects to the new library’s transaction types:

```ts
// Note that you can only convert `VersionedTransaction` objects
const modernTransaction = fromVersionedTransaction(classicTransaction);
```

To see more conversions supported by `@solana/compat`, you can check out the package’s [README on GitHub](https://github.com/anza-xyz/kit/blob/main/packages/compat/README.md).

## Program Clients

Writing JavaScript clients for on-chain programs has been done manually up until now. Without an IDL for some of the native programs, this process has been necessarily manual and has resulted in clients that lag behind the actual capabilities of the programs themselves.

We think that program clients should be _generated_ rather than written. Developers should be able to write Rust programs, compile the program code, and generate all of the JavaScript client-side code to interact with the program.

We use [Codama](https://github.com/codama-idl/codama) to represent Solana programs and generate clients for them. This includes a JavaScript client compatible with this library. For instance, here is how you’d construct a transaction message composed of instructions from three different core programs.

```ts
import { appendTransactionMessageInstructions, createTransactionMessage, pipe } from '@solana/kit';
import { getAddMemoInstruction } from '@solana-program/memo';
import { getSetComputeUnitLimitInstruction } from '@solana-program/compute-budget';
import { getTransferSolInstruction } from '@solana-program/system';

const instructions = [
    getSetComputeUnitLimitInstruction({ units: 600_000 }),
    getTransferSolInstruction({ source, destination, amount: 1_000_000_000 }),
    getAddMemoInstruction({ memo: "I'm transferring some SOL!" }),
];

// Creates a V0 transaction message with 3 instructions inside.
const transactionMessage = pipe(createTransactionMessage({ version: 0 }), tx =>
    appendTransactionMessageInstructions(instructions, tx),
);
```

As you can see, each program now generates its own library allowing you to cherry-pick your dependencies.

Note that asynchronous versions may be available for some instructions which allows them to resolve more inputs on your behalf — such as PDA derivation. For instance, the `CreateLookupTable` instruction offers an asynchronous builder that derives the `address` account and the `bump` argument for us.

```ts
const rpc = createSolanaRpc('http://127.0.0.1:8899');
const [authority, recentSlot] = await Promise.all([
    generateKeyPairSigner(),
    rpc.getSlot({ commitment: 'finalized' }).send(),
]);

const instruction = await getCreateLookupTableInstructionAsync({
    authority,
    recentSlot,
});
```

Alternatively, you may use the synchronous builder if you already have all the required inputs at hand.

```ts
const [address, bump] = await findAddressLookupTablePda({
    authority: authority.address,
    recentSlot,
});

const instruction = getCreateLookupTableInstruction({
    address,
    authority,
    bump,
    recentSlot,
});
```

On top of instruction builders, these clients offer a variety of utilities such as:

- Instruction codecs — e.g. `getTransferSolInstructionDataCodec`.
- Account types — e.g. `AddressLookupTable`.
- Account codecs — e.g. `getAddressLookupTableAccountDataCodec`.
- Account helpers — e.g. `fetchAddressLookupTable`.
- PDA helpers — e.g. `findAddressLookupTablePda`, `fetchAddressLookupTableFromSeeds`.
- Defined types and their codecs — e.g. `NonceState`, `getNonceStateCodec`.
- Program helpers — e.g. `SYSTEM_PROGRAM_ADDRESS`, `SystemAccount` enum, `identifySystemInstruction`.
- And much more!

Here’s another example that fetches an `AddressLookupTable` PDA from its seeds.

```ts
const account = await fetchAddressLookupTableFromSeeds(rpc, {
    authority: authority.address,
    recentSlot,
});

account.address; // Address
account.lamports; // Lamports
account.data.addresses; // Address[]
account.data.authority; // Some<Address>
account.data.deactivationSlot; // Slot
account.data.lastExtendedSlot; // Slot
account.data.lastExtendedSlotStartIndex; // number
```

### How Does This Work?

All of this code is 100% auto-generated by Codama from a tree of standardized nodes that represent our programs. It contains obvious nodes such as `AccountNode` but also more specified nodes such as `ConditionalValueNode` that allows us to resolve account or argument default values conditionally.

Codama allows us to hydrate our tree of nodes from IDLs which are typically generated by program frameworks such as [Anchor](https://github.com/coral-xyz/anchor) or [Shank](https://github.com/metaplex-foundation/shank). Additionally, visitors can be used on our nodes to expand the knowledge of our programs since the IDL itself doesn’t yet contain that level of information. Finally, special visitors called ‘renderers’ visit our tree to generate clients such as this JavaScript client.

Currently, there is one other renderer that generates Rust clients but this is only the beginning. In the future, you can expect renderers for auto-generated Python clients, documentation, CLIs, etc.

## Create Solana Program

We believe the whole ecosystem could benefit from generated program clients. That’s why we introduced a new NPM binary that allows you to create your Solana program — and generate clients for it — in no time. Simply run the following and follow the prompts to get started.

```sh
pnpm create solana-program
```

This [`create-solana-program`](https://github.com/solana-program/create-solana-program) installer will create a new repository including:

- An example program using the framework of your choice (Anchor coming soon).
- Generated clients for any of the selected clients.
- A set of scripts that allows you to:
    - Start a local validator including all programs and accounts you depend on.
    - Build, lint and test your programs.
    - Generate IDLs from your programs.
    - Generate clients from the generated IDLs.
    - Build and test each of your clients.
- GitHub Actions pipelines to test your program, test your clients, and even manually publish new packages or crates for your clients. (Coming soon).

When selecting the JavaScript client, you will get a fully generated library compatible with Kit much like the `@solana-program` packages showcased above.

## GraphQL

Though not directly related to web3.js, we wanted to hijack your attention to show you something else that we’re working on, of particular interest to frontend developers. It’s a new API for interacting with the RPC: a GraphQL API.

The `@solana/rpc-graphql` package can be used to make GraphQL queries to Solana RPC endpoints, using the same transports described above (including any customizations).

Here’s an example of retrieving account data with GraphQL:

```ts
const source = `
    query myQuery($address: String!) {
        account(address: $address) {
            dataBase58: data(encoding: BASE_58)
            dataBase64: data(encoding: BASE_64)
            lamports
        }
    }
`;

const variableValues = {
    address: 'AyGCwnwxQMCqaU4ixReHt8h5W4dwmxU7eM3BEQBdWVca',
};

const result = await rpcGraphQL.query(source, variableValues);

expect(result).toMatchObject({
    data: {
        account: {
            dataBase58: '2Uw1bpnsXxu3e',
            dataBase64: 'dGVzdCBkYXRh',
            lamports: 10290815n,
        },
    },
});
```

Using GraphQL allows developers to only specify which fields they _actually_ need, and do away with the rest of the response.

However, GraphQL is also extremely powerful for **nesting queries**, which can be particularly useful if you want to, say, get the **sum** of every lamports balance of every **owner of the owner** of each token account, while discarding any mint accounts.

```ts
const source = `
    query getLamportsOfOwnersOfOwnersOfTokenAccounts {
        programAccounts(programAddress: "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA") {
            ... on TokenAccount {
                owner {
                    ownerProgram {
                        lamports
                    }
                }
            }
        }
    }
`;

const result = await rpcGraphQL.query(source);

const sumOfAllLamportsOfOwnersOfOwnersOfTokenAccounts = result
    .map(o => o.account.owner.ownerProgram.lamports)
    .reduce((acc, lamports) => acc + lamports, 0);
```

The new GraphQL package supports this same style of nested querying on transactions and blocks.

```ts
const source = `
    query myQuery($signature: String!, $commitment: Commitment) {
        transaction(signature: $signature, commitment: $commitment) {
            message {
                instructions {
                    ... on CreateAccountInstruction {
                        lamports
                        programId
                        space
                    }
                }
            }
        }
    }
`;

const variableValues = {
    signature: '63zkpxATgAwXRGFQZPDESTw2m4uZQ99sX338ibgKtTcgG6v34E3MSS3zckCwJHrimS71cvei6h1Bn1K1De53BNWC',
    commitment: 'confirmed',
};

const result = await rpcGraphQL.query(source, variableValues);

expect(result).toMatchObject({
    data: {
        transaction: {
            message: {
                instructions: expect.arrayContaining([
                    {
                        lamports: expect.any(BigInt),
                        programId: '11111111111111111111111111111111',
                        space: expect.any(BigInt),
                    },
                ]),
            },
        },
    },
});
```

See more in the package’s [README on GitHub](https://github.com/anza-xyz/kit/tree/main/packages/rpc-graphql).

## Development

You can see all development of this library and associated GraphQL tooling in the Kit repository on GitHub.

- https://github.com/anza-xyz/kit

You can follow along with program client generator development in the `@solana-program` org and the `@codama-idl/codama` repository.

- https://github.com/solana-program/
- https://github.com/codama-idl/codama

Solana Labs develops these tools in public, as open source. We encourage any and all developers who would like to work on these tools to contribute to the codebase.

## Thank you

We’re grateful that you have read this far. If you are interested in migrating an existing application to Kit to take advantage of some of the benefits we’ve demonstrated, we want to give you some direct support. Reach out to [@steveluscher](https://t.me/steveluscher/) on Telegram to start a conversation.


---

## 33. safe-core-sdk
- **URL:** https://github.com/devtechedge/safe-core-sdk
- **Language:** TypeScript
- **Topics:** None
- **Description:** The Safe{Core} SDK allows builders to add account abstraction functionality into their apps.

### README.md

![license](https://img.shields.io/github/license/safe-global/safe-core-sdk) [![Coverage Status](https://coveralls.io/repos/github/safe-global/safe-core-sdk/badge.svg?branch=main)](https://coveralls.io/github/safe-global/safe-core-sdk?branch=main)

![Safe_Logos_Core_SDK_Black](https://github.com/safe-global/safe-core-sdk/assets/6764315/7202a24a-2981-4b31-9cf5-ace1c3b2c4fa)

## Table of contents

- [About](#about)
- [Documentation](#documentation)
- [Packages](#packages)
- [Guides](#guides)
- [Need Help or Have Questions?](#need-help-or-have-questions)
- [Contributing](#contributing)
- [Playground](#playground)
- [License](#license)

## About

This is a mono-repository containing Javascript/Typescript software developer tools that facilitate the interaction with [Safe Smart Accounts](https://github.com/safe-global/safe-smart-account), [Safe Transaction Service API](https://github.com/safe-global/safe-transaction-service), and enabling uses like ERC-4337 compatibility.

## Documentation

If you want to develop using Safe Smart Accounts in a Javascript/Typescript app, we recommend that you visit [our documentation site](https://docs.safe.global/sdk/overview).

## Packages

| Package | Release | Description |
| ------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol-kit](https://github.com/safe-global/safe-core-sdk/tree/main/packages/protocol-kit)                 | [![npm Version](https://badge.fury.io/js/%40safe-global%2Fprotocol-kit.svg)](https://badge.fury.io/js/%40safe-global%2Fprotocol-kit)       | TypeScript library that facilitates the interaction with [Safe Smart Accounts](https://github.com/safe-global/safe-smart-account). Can be used to create new Safe accounts, update the configuration of existing Safes, create and execute transactions, among other features.                                              |
| [api-kit](https://github.com/safe-global/safe-core-sdk/tree/main/packages/api-kit)                           | [![npm Version](https://badge.fury.io/js/%40safe-global%2Fapi-kit.svg)](https://badge.fury.io/js/%40safe-global%2Fapi-kit)                 | [Safe Transaction Service API](https://github.com/safe-global/safe-transaction-service) typescript library. Allows to propose and share transactions with the other signers of a Safe, sending the signatures to the service to collect them, and getting information about a Safe, among other features.                                                                       |
| [relay-kit](https://github.com/safe-global/safe-core-sdk/tree/main/packages/relay-kit)                       | ​​​[​![npm Version](https://badge.fury.io/js/%40safe-global%2Frelay-kit.svg)​](https://badge.fury.io/js/%40safe-global%2Frelay-kit)​             | Typescript library that enables ERC-4337 with Safe and allows users to pay for the transaction fees from their Safe account balance using the blockchain native token or ERC-20 tokens, or to get their transactions sponsored.                                                                            |
| [types-kit](https://github.com/safe-global/safe-core-sdk/tree/main/packages/types-kit)   | [![npm Version](https://badge.fury.io/js/%40safe-global%2Ftypes-kit.svg)](https://badge.fury.io/js/%40safe-global%2Ftypes-kit)  | Common types used in the [Safe Core SDK](https://github.com/safe-global/safe-core-sdk/tree/main/packages) packages.                                                  |

## Guides

| Title | Description |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Integrating the Safe{Core} SDK](https://github.com/safe-global/safe-core-sdk/blob/main/guides/integrating-the-safe-core-sdk.md) | This guide shows how to use the [Protocol Kit](https://github.com/safe-global/safe-core-sdk/tree/main/packages/protocol-kit) and [API Kit](https://github.com/safe-global/safe-core-sdk/tree/main/packages/api-kit). |

## Need Help or Have Questions?

If you have any doubts, questions, or need assistance, feel free to reach out! [Here you will find how to get support.](https://github.com/safe-global/safe-core-sdk/tree/main/SUPPORT.md)

## Contributing

If you are interested in contributing, please read the [Contributing Guidelines](https://github.com/safe-global/safe-core-sdk/tree/main/CONTRIBUTING.md) **before opening an issue or submitting a pull request**.

## Playground

This project includes a [playground](https://github.com/safe-global/safe-core-sdk/tree/main/playground/README.md) with a few scripts that can be used as a starting point to use the Safe{Core} SDK. These scripts contain valuable snippets that demonstrate various Safe features. They serve as a useful learning tool or starting point for implementing these features in your application.

## License

This library is released under [MIT](https://github.com/safe-global/safe-core-sdk/tree/main/LICENSE.md).


---

## 34. smart-waitlist
- **URL:** https://github.com/devtechedge/smart-waitlist
- **Language:** TypeScript
- **Topics:** drizzle-orm, full-stack, nextjs, referral-system, saas, server-actions, shadcn-ui, stripe, supabase, tailwindcss, typescript, waitlist
- **Description:** Smart Waitlist is a SaaS waitlist and referral engine: viral growth loops, live queue position, admin analytics, Stripe tiers, and Postgres RLS. Next.js 16, Supabase Auth + Postgres, Drizzle, shadcn/ui, Tailwind. Public Vercel is full-stack liveΓÇösign up, grab a referral link, climb the queue, open the admin dashboard. TypeScript. Not a toy form.

### README.md

# Smart Waitlist & Referral Engine

Production-ready SaaS waitlist with viral referral loops, live position tracking, admin analytics, Stripe tiers, and full RLS. Built with Next.js 16, Supabase, Drizzle ORM, and shadcn/ui.

[![CI](https://github.com/devtechedge/smart-waitlist/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/smart-waitlist/actions/workflows/ci.yml)
![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)
![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![Supabase](https://img.shields.io/badge/Supabase-Postgres-3ecf8e?logo=supabase)
![Drizzle](https://img.shields.io/badge/Drizzle-ORM-c5f74f)
![Stripe](https://img.shields.io/badge/Stripe-Payments-635bff?logo=stripe)
![License](https://img.shields.io/badge/License-MIT-green)

## Live Demo

**https://smart-waitlist-engine.vercel.app/**

> Full-stack live. Supabase (Auth + Postgres + RLS) is healthy. Sign up, get a referral link, climb the queue, and explore the admin dashboard.

## Screenshots

| Landing / Hero | How it works |
|---------------|--------------|
| ![Landing](docs/screenshots/Screenshot%202026-07-27%20051317.png) | ![How it works](docs/screenshots/work.png) |

| Dashboard | Admin / Analytics |
|-----------|-------------------|
| ![Dashboard](docs/screenshots/Screenshot%202026-07-27%20053200.png) | ![Admin](docs/screenshots/Screenshot%202026-07-27%20053209.png) |

## Features

- **Viral referral engine** - unique referral codes, position leapfrogging, live leaderboard
- **Real-time position tracking** - dashboard shows rank, referrals, and shareable link
- **Admin analytics** - waitlist table, conversion funnel, geo heatmap, CSV export
- **Stripe tiers** - paid upgrades and promo codes
- **Secure by default** - Supabase RLS, Zod validation, admin allow-list, webhook signatures. See [SECURITY.md](SECURITY.md).
- **Modern stack** - Next.js 16 App Router + Server Actions, Drizzle ORM, Tailwind v4 + shadcn/ui, strict TypeScript

## Tech Stack

| Layer | Choice |
|-------|--------|
| Framework | Next.js 16 (App Router, RSC, Server Actions) |
| Language | TypeScript (strict) |
| Styling | Tailwind CSS v4 + shadcn/ui |
| Database | Supabase Postgres + RLS |
| Auth | Supabase Auth + `@supabase/ssr` |
| ORM | Drizzle ORM |
| Payments | Stripe |
| Validation | Zod |
| Deploy | Vercel + Supabase Cloud |

## Quick Start

```bash
git clone https://github.com/devtechedge/smart-waitlist.git
cd smart-waitlist
npm install
cp .env.example .env.local   # fill Supabase + Stripe keys
npm run db:push              # or apply supabase/migrations
npm run dev
```

Open http://localhost:3000.

See `.env.example` for the full list of required variables.

## Tests

```bash
npm test            # unit (pure helpers: ranking, auth, fraud email, CSV, redirects)
npm run typecheck
npm run test:e2e    # Playwright Chromium smokes (landing, sign-in, auth gate, 404)
```

CI runs all three on every push to `main`. Dependabot opens weekly patch/minor PRs only (majors ignored).

## License

MIT. See [LICENSE](LICENSE) for details.


---

## 35. obsidian
- **URL:** https://github.com/devtechedge/obsidian
- **Language:** HTML
- **Topics:** creative-coding, frontend, generative-art, github-pages, lenis, no-build, portfolio, react, single-file, tailwindcss, threejs, web-audio
- **Description:** The Obsidian Archive is a single-file immersive portfolio for a fictional generative sculpture studio. Twenty frontend features: Three.js crystal, Web Audio drone, command palette, pinned horizontal gallery. React 18 UMD, Tailwind Play CDN, Lenis, Three.jsΓÇözero build, GitHub Pages, SRI-pinned CDNs. Open index.html anywhere. Client-side only. MIT.

### README.md

# The Obsidian Archive

Single-file immersive portfolio for a fictional generative digital sculpture studio. Twenty complex frontend features, Three.js crystal, Web Audio drone, command palette, and pinned horizontal gallery - all with zero build step.

[![CI](https://github.com/devtechedge/obsidian/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/obsidian/actions/workflows/ci.yml)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-black?logo=github)](https://devtechedge.github.io/obsidian/)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![Three.js](https://img.shields.io/badge/Three.js-0.160-black?logo=threedotjs)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-Play%20CDN-06b6d4?logo=tailwindcss)
![Lenis](https://img.shields.io/badge/Lenis-Smooth%20Scroll-black)
![License](https://img.shields.io/badge/License-MIT-green)

## Live Demo

**https://devtechedge.github.io/obsidian/**

> **Status:** Client-side only on GitHub Pages. Zero backend. Open `index.html` anywhere. CDNs (React / Three / Lenis) are version-pinned with SRI. Tailwind Play CDN remains a runtime compiler by design.

Client-side only · zero build · fully self-contained (React UMD + Tailwind Play CDN + Three.js + Lenis + Web Audio).

## Screenshots

![Hero with 3D crystal](docs/screenshots/01-hero.jpg)

*Hero - Three.js crystal + particle field*

![Archive grid](docs/screenshots/02-archive.jpg)

*Archive - generative sculpture grid*

![Philosophy section](docs/screenshots/03-philosophy.jpg)

*Philosophy - live-drawing mandala + stats*

![Dark contact](docs/screenshots/04-contact-dark.jpg)

*Contact - dark theme*

## Features

- **One file, zero build** - entire experience ships as a single `index.html` (~140 KB)
- **Three.js hero crystal** with custom GLSL shader + mouse-drag rotation
- **Six generative SVG sculptures** (Vortex, Grid, Waves, Facets, Rings, Hex)
- **Pinned horizontal-scroll gallery** driven by vertical scroll
- **Web Audio ambient drone** (opt-in, four-oscillator with LFO filter)
- **⌘K command palette** with fuzzy search across sections, actions, and sculptures
- **Editorial light + gallery dark themes** with localStorage persistence and no FOUC
- **Accessible lightbox**, magnetic buttons, particle bursts, cursor trail, scroll progress, Konami easter egg, and more

## Tech Stack

| Layer | Choice |
|-------|--------|
| UI | React 18 (UMD) |
| Styling | Tailwind CSS (Play CDN) |
| 3D | Three.js 0.160 |
| Scroll | Lenis |
| Audio | Web Audio API |
| Fonts | Inter (variable) |
| Hosting | GitHub Pages |

No bundler. No package manager. The file is the project.

## Quick Start

```bash
# Clone and open locally
git clone https://github.com/devtechedge/obsidian.git
cd obsidian
# Just open index.html in a browser - there is no build step

# Optional: CI tooling only
npm ci
npm test
npx playwright install --with-deps chromium
npm run test:e2e
```

## Security

Threat model, CDN pinning, CSP, and XSS notes: [SECURITY.md](SECURITY.md).

## License

MIT License. See [LICENSE](LICENSE) for details.


---

## 36. nexus-bazaar
- **URL:** https://github.com/devtechedge/nexus-bazaar
- **Language:** TypeScript
- **Topics:** b2b, checkout, ecommerce, local-first, marketplace, multi-role, portfolio, react, spa, tailwindcss, typescript, vite
- **Description:** NexusBazaar is a client-side multi-role marketplace for buyers, sellers, and admins. Browse a seeded catalog, run cart and promo checkout, switch into seller or admin hubs, and walk B2B RFQ plus Net-30 credit. React 19, Vite, TypeScript, Tailwind. Data lives in localStorage ΓÇö no production payments, JWT, or backend. Optional Gemini concierge. MIT.

### README.md

# NexusBazaar

Client-side multi-role marketplace for buyers, sellers, and admins - storefront, promo checkout, B2B RFQ, and localStorage persistence.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://nexusbazaar-market.vercel.app)
[![CI](https://github.com/devtechedge/nexus-bazaar/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/nexus-bazaar/actions/workflows/ci.yml)
[![React](https://img.shields.io/badge/React-19-0052CC?logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-8-646CFF?logo=vite)](https://vitejs.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://nexusbazaar-market.vercel.app**

> **Status:** Public deploy is a **client-side demo**. Catalog, cart, orders, loyalty, and B2B ledgers persist in `localStorage`. There is no production payment backend, JWT, or NextAuth. Switch Buyer / Seller / Admin from the header avatar. `NEXUS10` is a public promo; `ELITEPRO` needs Elite (crown toggle). NexusBot falls back to a mock reply unless `GEMINI_API_KEY` is set locally.

Do **not** use [nexus-bazaar.vercel.app](https://nexus-bazaar.vercel.app) - that hostname is a different lifestyle-blog project.

This is the **only** public repo for the marketplace.

---

## Screenshots

<p align="center">
  <img src="docs/social-preview.jpg" alt="NexusBazaar" width="800">
</p>

| Storefront | Cart |
|------------|------|
| ![Storefront](docs/screenshots/01-storefront.png) | ![Cart](docs/screenshots/02-cart.png) |

| Seller hub | B2B wholesale |
|------------|---------------|
| ![Seller hub](docs/screenshots/03-seller-hub.png) | ![B2B wholesale](docs/screenshots/04-b2b.png) |

---

## Features

- Buyer storefront with search, product details, wishlist, live-auction tiles, and promo checkout (`NEXUS10`, `ELITEPRO`, `BIGSAVER`)
- Header identity switcher for Buyer, Seller, and Admin - seller/admin chrome is role-gated
- Seller hub: listings, inventory, vouchers, broadcast tiles
- Admin workspace: user flags, promo ledger, marketplace metrics
- B2B desk: RFQ, Net-30 credit, team budget, pallet calculator
- Loyalty, guilds, curations, security-vault UI - all `localStorage`
- Optional Gemini concierge at `POST /api/gemini/chat` (mock without a key)

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 19, Vite 8, TypeScript, Tailwind 4 |
| Data | Seeded in-memory catalog + `localStorage` (not a SQL backend) |
| Auth | Demo role switcher - not JWT, not NextAuth |
| Payments | Simulated checkout only |
| AI | Optional `POST /api/gemini/chat` - mock fallback on Vercel |
| Hosting | Vercel (static Vite + `/api` function) |
| CI | GitHub Actions - Vitest, `tsc`, Playwright |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/nexus-bazaar.git
cd nexus-bazaar
npm install
npm run dev
```

Open **http://localhost:3000**. Gemini is optional.

```bash
npm test
npm run typecheck
npx playwright install chromium
npm run test:e2e
```

---

## Demo notes

| Identity | How |
|----------|-----|
| Eager Buyer | Default. Cart, wishlist, orders, loyalty. |
| Elite Tech Seller | Header avatar → Seller Hub |
| Platform Admin | Header avatar → Admin Panel |

Promo codes: `NEXUS10` (10%), `ELITEPRO` (20%, Elite only), `BIGSAVER` (15% over $200).

---

## License

MIT. See [LICENSE](LICENSE).

## Security

Threat model, residual risk, and operator secrets: see [SECURITY.md](SECURITY.md).
This public deploy is a portfolio / demo surface; the GitHub repo may go private
after review without changing the live site’s required env hygiene.


---

## 37. lattice
- **URL:** https://github.com/devtechedge/lattice
- **Language:** TypeScript
- **Topics:** blockchain, crypto, freelance, job-board, react, salaries, tailwindcss, talent, tanstack, typescript, vercel, web3
- **Description:** Web3 career lattice: live roles from twenty crypto teamsΓÇÖ public Greenhouse, Lever, and Ashby boards, plus gigs, talent, and a salary observatory. Apply on the employerΓÇÖs site. Pay only when the board publishes it. Public listings. Not an employer.

### README.md

# Lattice

**Web3 jobs, crypto careers, blockchain roles** - live from employer ATS boards. Roles, gigs, talent, salaries, and companies - without five tabs and a paywall.

<p align="left">
  <img src="public/favicon.svg" width="48" height="48" alt="Lattice mark" />
</p>

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://lattice-devtechedge1.vercel.app)
[![CI](https://github.com/devtechedge/lattice/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/lattice/actions/workflows/ci.yml)
[![TanStack Start](https://img.shields.io/badge/TanStack%20Start-black)](https://tanstack.com/start)
[![React](https://img.shields.io/badge/React-19-0052CC?logo=react)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Live Demo

**https://lattice-devtechedge1.vercel.app**

> **Status:** Production is a **live job board**. Roles come from twenty crypto teams’ public Greenhouse, Lever, and Ashby boards (Coinbase, Binance, OKX, Bybit, Ripple, Kraken, Fireblocks, Crypto.com, Chainalysis, Blockchain.com, BitGo, Gemini, Alchemy, Phantom, Circle, Uniswap Labs, Ledger, Consensys, Ethereum Foundation, Solana Labs). Apply on the employer’s site. **Pay is only shown when the board publishes it** (posted metadata or inferred from the posting, marked `~`). Lattice does not invent a band. Talent, gigs, and learn remain a small editorial catalog. Posted listings, applications, bookmarks, and salary submissions persist in Postgres when `DATABASE_URL` is set. Without it the app uses embedded PGLite and reseeds on cold start. Sign-in is optional (bookmarks, applications, and talent profiles). Public listings. Not an employer. Not an offering. No wallet connect.

This is the **only** public repo for the product.

### Sister product

**[Jobrow](https://jobrow.vercel.app)** indexes still-open **US tech** roles from public ATS boards. Lattice stays on **blockchain / crypto / Web3**. Source: [devtechedge/job-board](https://github.com/devtechedge/job-board).

### Fresh openings

**[Companies hiring this week](https://lattice-devtechedge1.vercel.app/hiring)** - live roundup of crypto/Web3 employers that posted in the last seven days. Also: [job hubs](https://lattice-devtechedge1.vercel.app/jobs) (Solidity, DeFi, Ethereum, remote) and the [salary observatory](https://lattice-devtechedge1.vercel.app/salaries).

---

## Screenshots

| Home | Roles |
|------|-------|
| ![Editorial homepage](docs/screenshots/01-home.png) | ![Roles index with filters](docs/screenshots/02-roles.png) |

| Role | Salaries |
|------|----------|
| ![Role detail](docs/screenshots/03-role-detail.png) | ![Salary observatory](docs/screenshots/04-salaries.png) |

| Talent |
|--------|
| ![Talent directory](docs/screenshots/05-talent.png) |

Share card: [docs/screenshots/social-preview.png](docs/screenshots/social-preview.png)

---

## Features

- Editorial homepage: latest live role, twenty-team strip, new-this-week, companies hiring, manifesto
- [Companies hiring this week](https://lattice-devtechedge1.vercel.app/hiring) - shareable 7-day roundup from live ATS crawls
- Roles index with table and card views, persisted locally
- Live openings from twenty first-party ATS boards (Greenhouse, Lever, Ashby). Apply on the employer’s site; pay is posted or inferred (`~`), never invented
- Filters for chain, scene, department, seniority, remote region, benefits, pay-in-crypto
- Compensation as cash + token + equity, with vesting and cliff on the card
- Gigs marketplace and simulated digital contracts
- Public talent directory plus a privacy-flagged talent collective
- Salary observatory (mean / min / max, seniority, region, language sparkline)
- Anonymous salary submit, alerts / RSS view, market pulse, learn hub
- Free employer post (Markdown, preview, no account required)
- Apply flow with screening questions; studio desk for inbound applications
- Light / dark theme (persisted), command palette, hover-reveal scrollbars

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| App | TanStack Start, React 19, TypeScript, Tailwind v4 |
| Data | Live ATS fetch in `src/lib/server/live.ts`. Talent / gigs / learn in `src/lib/catalog`. Postgres when `DATABASE_URL` is set; embedded PGLite otherwise |
| Auth | Optional Better Auth session for bookmarks, applications, and profiles |
| Hosting | Vercel |
| License | MIT |

---

## Quick Start

```bash
git clone https://github.com/devtechedge/lattice.git
cd lattice
npm install
npm run dev
```

Without `DATABASE_URL` the app uses embedded PGLite and seeds the catalog on first load.

```bash
npm run typecheck
npm test
npm run test:e2e
npm run build
```

Env template: [.env.example](.env.example). Never commit secrets.

| Variable | Where | Purpose |
|----------|--------|---------|
| `DATABASE_URL` | Vercel | Neon pooled URI (`sslmode=require`). Omit locally. |

See [SECURITY.md](SECURITY.md) for the threat model, reporting, and residual risk (guest posting, anonymous salary submit).

---

## Security

Lattice is hardened for a public Vercel deploy (parameterized SQL, same-site auth guards, CSP/HSTS headers, Markdown URL allow-lists, guest-post rate limits). **No public site is unhackable** - see [SECURITY.md](SECURITY.md) for the threat model, residual risk, and how to make this GitHub repo private later. SEO checklist: [docs/SEO.md](docs/SEO.md).

## License

MIT. See [LICENSE](LICENSE).


---

## 38. healthcare-deep-memory-agents
- **URL:** https://github.com/devtechedge/healthcare-deep-memory-agents
- **Language:** Python
- **Topics:** ai-agents, clinical-memory, consent, deep-memory, groq, healthcare, ollama, patient-journey, python, sentence-transformers, sqlite, vertical-agents
- **Description:** Cadence is a pure-Python deep-memory healthcare agent lab: multi-layer patient memory, journey stages, and consent-scoped clinician briefs. No LangChain. Local path is Ollama + SQLite + sentence-transformers. Public Vercel UI is a companion + share-code brief with Groq llama-3.3-70b (demo fallback without a key). Educational prototype, not real PHI

### README.md

# <img src="web/favicon.svg" width="40" height="40" alt="" /> Cadence

**Deep-memory vertical agents for healthcare** - pure Python, fully local, zero agentic frameworks.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://cadence-healthcare.vercel.app/)
[![CI](https://github.com/devtechedge/healthcare-deep-memory-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/devtechedge/healthcare-deep-memory-agents/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v0.2.0-brightgreen.svg)](https://github.com/devtechedge/healthcare-deep-memory-agents/releases/tag/v0.2.0)

> **Disclaimer**: Educational / research prototype only. Never use for real medical decisions. Always consult qualified clinicians.

## Live Demo

https://cadence-healthcare.vercel.app/

> **Status:** Public UI is a client-side companion + share-code clinician brief. Live chat uses Groq `llama-3.3-70b-versatile` (env `OPENAI_API_KEY` on Vercel). If the key is missing or Groq errors, the badge switches to **demo fallback**. Full multi-layer memory + consent grants run locally (`python run_patient.py` / `python run_clinician.py` + Ollama). Do not enter real PHI.

## Screenshots

<p align="center">
  <img src="docs/social-preview.jpg" alt="Cadence Healthcare" width="800">
</p>

| Overview | Companion |
| --- | --- |
| ![Overview](docs/screenshots/01-overview.png) | ![Companion](docs/screenshots/02-companion-timeline.png) |

| Share code | Clinician brief |
| --- | --- |
| ![Share](docs/screenshots/03-share-code.png) | ![Brief](docs/screenshots/04-clinician-brief.png) |

---

## What it is

Vertical AI agents that remember - symptoms, history, preferences - across sessions.

- Multi-layer deep memory (session · episodic · semantic · knowledge · insights)
- Pure Python only (no LangChain, CrewAI, AutoGen, Mem0…)
- Fully local & free (Ollama + SQLite + sentence-transformers)
- Consent-scoped clinician brief / note draft
- **Patient journey first**: Baseline → Triage → Visit Prep → Care → Pattern → Recovery

---

## Tech stack

| Layer | Choice |
|-------|--------|
| Agents | Pure Python (no LangChain / CrewAI / Mem0) |
| Local LLM | Ollama (`llama3.1`) |
| Live UI chat | Groq `llama-3.3-70b-versatile` via Vercel `/api/chat` |
| Memory | SQLite + sentence-transformers (injectable embedder) |
| Consent | Scope-gated grants + audit table |
| UI | Static HTML / Tailwind CDN on Vercel |

---

## Quick Start

```bash
# 1. Ollama
ollama pull llama3.1

# 2. Python
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3a. Patient journey (recommended)
python run_patient.py

# 3b. Single triage agent
python run_agent.py

# 3c. Clinician grant / brief / note
python run_clinician.py grant --patient demo --clinician dr_lee --hours 48
```

Force a stage:

```bash
python run_patient.py --stage VISIT_PREP
```

In-session: type `/stage CARE` to switch.

Memory lives in `data/` and survives restarts (gitignored).

### Tests

```bash
pip install -r requirements-dev.txt
python -m pytest -q
npm ci && npx playwright install chromium && npm run test:e2e
```

---

## Patient journey stages

| Stage | Agent | Role |
|-------|-------|------|
| BASELINE | Baseline | Profile, allergies, meds, goals |
| TRIAGE | Triage | Symptom structure + cautious red flags |
| VISIT_PREP | VisitPrep | Questions + brief for the clinician visit |
| CARE | CareCompanion | Adherence, side effects, care-plan tasks |
| PATTERN | Pattern | Hypothesis correlations from memory |
| RECOVERY | Recovery | Milestones and “what better looks like” |

Spec: [`docs/PATIENT_JOURNEY.md`](docs/PATIENT_JOURNEY.md)

---

## Architecture

### Memory Layers
1. **Session / Working** – recent turns  
2. **Episodic** – timestamped events, symptoms, visits  
3. **Semantic** – vector long-term facts  
4. **Knowledge** – local RAG over guidelines  
5. **Insights** – synthesized patterns (human-verified)

---

## Project Structure

```
healthcare-deep-memory-agents/
├── docs/screenshots/        ← product screenshots
├── run_patient.py           ← patient journey CLI
├── run_clinician.py         ← grant / brief / note CLI
├── src/memory/              ← DeepMemory + ConsentStore
├── src/agents/
├── web/                     ← Cadence UI (Vercel)
├── tests/                   ← pytest (no torch / Ollama)
├── e2e/                     ← Playwright smokes
└── data/                    ← local DB (gitignored)
```

---

## Security

See [`SECURITY.md`](SECURITY.md). Educational prototype. Public chat messages go to Groq when live mode is on.

---

## License

MIT (code). Any medical content you add keeps its original license.


---

## 39. aegis_vercel
- **URL:** https://github.com/devtechedge/aegis_vercel
- **Language:** Python
- **Topics:** fastapi, langchain, langgraph, python, serverless, vercel, ai-agents, langserve, langsmith, multi-agent, pgvector, rag, autonomous-agents, hitl, human-in-the-loop, mermaid, sre, sse, streaming
- **Description:** AEGIS is a multi-agent operations cortex with a live dashboard. Supervisor plus specialist agents (SRE, knowledge, coder, evaluator, communicator), Hybrid RAG, HITL gates, streaming SSE, and a real-time Mermaid LangGraph. FastAPI, LangChain, LangGraph, LangSmith. Open /ui, toggle Demo vs Live. Demo is instant simulation; Live needs API keys. MIT.

### README.md

# AEGIS - Autonomous Enterprise Graph Intelligence System

**A self-hosted, auditable alternative to Glean + Devin + PagerDuty Autopilot, built 100% on LangChain.**

> **Try it live:** [aegis-agent-api.vercel.app/ui](https://aegis-agent-api.vercel.app/ui) - toggle between Demo and Live inference, watch the LangGraph supervisor route specialists in real time, and approve/reject HITL gates.

AEGIS takes a natural language operational request - _"Why is checkout latency spiking in us-east?"_ - and autonomously plans, delegates to specialist sub-agents, retrieves from hybrid knowledge bases, executes tools, hits human-in-the-loop gates, and posts a fully traced, evaluated, and auditable result.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?logo=vercel)](https://aegis-agent-api.vercel.app/ui)
[![CI](https://img.shields.io/github/actions/workflow/status/devtechedge/aegis_vercel/ci.yml?branch=main)](https://github.com/devtechedge/aegis_vercel/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![LangChain](https://img.shields.io/badge/LangChain-0.3-orange)]()
[![Security](https://img.shields.io/badge/Security-threat%20model-informational)](SECURITY.md)

---

## Live Demo

Open [aegis-agent-api.vercel.app/ui](https://aegis-agent-api.vercel.app/ui) and click **Run AEGIS**.

**What you'll see:**

- **Real-time Mermaid graph** animating the execution path: Supervisor → SRE Analyst → Knowledge → Coder → [HITL] → Evaluator → Communicator
- **Streaming agent output** - each specialist's findings appear as they execute, with confidence scores and artifact counts
- **Human-in-the-Loop gate** - the Coder produces a patch, pauses for your approval, then the Evaluator and Communicator complete the flow
- **Demo / Live toggle** - Demo mode runs an instant simulation; Live mode connects to the real LangGraph with your API keys
- **Live info panel** - step count, confidence %, artifact count, and elapsed time update in real time
- **LangSmith traces** - one-click link to the full trace for every run

### Screenshots

![Live run with specialist streaming](docs/screenshots/01-live-run-streaming.png)

![Demo mode HITL approval gate](docs/screenshots/02-demo-hitl-gate.png)

![Demo completed with confidence chips](docs/screenshots/03-demo-completed.png)

Public demo threat model: [SECURITY.md](SECURITY.md). Demo/sim is public by default; live LLM path requires `LIVE_MODE` (optional `PUBLIC_RUN_TOKEN`). Rate-limited. Not bank-grade.

---

## Architecture

```
[Next.js UI / LangGraph Studio] <-SSE-> [LangServe FastAPI /api]
                                        |
                              [LangGraph Supervisor]
                   /     |      |       |       |      \
            Researcher Coder  SRE   Knowledge Comm  Evaluator
               |         |     |        |
         Tavily/Arxiv  E2B  Prometheus  PGVector Hybrid RAG
                                        |
                                [Postgres + PGVector + Redis]
                                        |
                              [LangSmith Traces / Evals / Prompt Hub]
```

## Feature Matrix - Full LangChain Ecosystem

| Product | Used For |
|---|---|
| **langchain-core** | LCEL everywhere, structured output Pydantic v2, fallback LLM router |
| **langgraph** | Supervisor + 6 subgraphs, PostgresSaver, `interrupt()` HITL, `astream_events` |
| **langsmith** | Tracing, Prompt Hub (`aegis/supervisor_router`), Evals, Feedback API |
| **langserve** | FastAPI `/invoke`, `/stream`, `/threads/{id}/resume`, OpenAPI playground |
| **RAG** | MultiQuery → Cohere Rerank → LLM Grader → HyDE, PGVector + BM25 hybrid |
| **Tools (14)** | Tavily, Code Executor, Postgres, GitHub, Slack, Browser, Prometheus, Runbook, Arxiv, Wikipedia, Email, Calendar, FS, Memory |

## 7 Agentic Loops - All Implemented

1. Perception-Plan-Act-Reflect
2. Supervisor-Worker Hierarchical
3. RAG Self-Correction
4. Tool-Use ReAct + Self-Heal
5. Human-in-the-Loop Interrupt
6. Evaluation-Driven Self-Improvement
7. Memory Consolidation

All visible in LangSmith with custom metadata.

---

## Quickstart

### Vercel (recommended - zero config)

1. Fork this repo
2. Import into [Vercel](https://vercel.com)
3. Set root directory to `apps/api`
4. Add `GOOGLE_API_KEY` (or `OPENAI_API_KEY`) as an environment variable
5. Deploy - visit `/ui` for the live dashboard, `/docs` for the API playground

Without API keys the UI gracefully falls back to **Demo mode** (instant simulation).

### Docker (local / self-hosted)

```bash
cp .env.example .env
docker-compose -f infra/docker-compose.yml up --build
```

- Dashboard: http://localhost:8000/ui
- API playground: http://localhost:8000/docs
- LangGraph Studio: `langgraph dev`

### API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/ui` | GET | Live dashboard (SSE, Mermaid, HITL) |
| `/stream` | POST | Streaming inference (SSE) |
| `/invoke` | POST | Single-shot inference (JSON) |
| `/threads/{id}/resume` | POST | Resume after HITL (JSON) |
| `/threads/{id}/resume/stream` | POST | Resume after HITL (SSE) |
| `/health` | GET | Graph status, key availability |
| `/docs` | GET | OpenAPI / Swagger playground |

---

## Why This Proves Senior+ AI Engineering

- **Agentic Loops**: 7 explicit loops, not chains
- **LangGraph HITL**: `interrupt()` / `Command(resume=...)`, PostgresSaver
- **LangSmith Evals/Prompt Hub**: 3 datasets, LLM-as-judge, CI gating faithfulness > 0.82
- **Hybrid RAG**: MultiQuery + Compression + Grader + HyDE
- **Multi-agent Supervisor**: 6 specialists, tool-use ReAct
- **Production Observability**: OpenTelemetry → LangSmith, run metadata
- **Vercel Serverless**: graceful degradation, SSE streaming, version-agnostic chunk handling

## Repo Structure

```
aegis/
├── apps/api/              # LangServe FastAPI + live UI
├── packages/aegis_graph/  # Supervisor + 6 subgraphs
├── packages/tools/        # 14 production tools
├── packages/rag/          # Ingestion / retriever / vectorstore
├── packages/memory/
├── packages/evals/
├── infra/docker-compose.yml
├── tests/
└── scripts/run_evals.py
```

## Evals

```bash
python scripts/run_evals.py
```

Writes `evals/reports/latest.md`. Public CI has no `LANGCHAIN_API_KEY`, so that job writes a **mock** report and exits 0 - it does not measure live LangSmith faithfulness. With the key set, datasets `aegis_rag_qa`, `aegis_tool_use`, and `aegis_incident_triage` run against project `aegis-production`; the intended production threshold is faithfulness ≥ 0.82.

CI itself fails on ruff (real errors), mypy on tools/evals/tests, and pytest (graph compile, RAG loop, tool guards, `/health` `/ui` `/stream` smokes). `pip-audit` is informational and does not fail the job on LangChain majors.

## Environment Variables

| Var | Purpose |
|---|---|
| `GOOGLE_API_KEY` | Gemini LLM (primary) |
| `OPENAI_API_KEY` | OpenAI fallback |
| `ANTHROPIC_API_KEY` | Coding fallback |
| `LANGCHAIN_API_KEY` | LangSmith tracing |
| `LANGCHAIN_TRACING_V2=true` | Enable tracing |
| `DATABASE_URL` | Postgres + PGVector |
| `REDIS_URL` | Short-term memory |
| `TAVILY_API_KEY` | Web search |

All optional - fake models/fallbacks keep Vercel deploy green even without keys.

---

MIT License - Built with LangChain, LangGraph, LangSmith


---

## 40. js-stellar-sdk
- **URL:** https://github.com/devtechedge/js-stellar-sdk
- **Language:** TypeScript
- **Topics:** None
- **Description:** Main Stellar client library for the JavaScript language.

### README.md

# Stellar JS SDK (js-stellar-sdk)

<p class="badges">
  <a href="https://badge.fury.io/js/@stellar%2Fstellar-sdk"><img src="https://badge.fury.io/js/@stellar%2Fstellar-sdk.svg" alt="npm version" height="18"></a>
  <a href="https://www.npmjs.com/package/@stellar/stellar-sdk"><img alt="Weekly Downloads" src="https://img.shields.io/npm/dw/@stellar/stellar-sdk" /></a>
  <a href="https://github.com/stellar/js-stellar-sdk/actions/workflows/tests.yml"><img alt="Test Status" src="https://github.com/stellar/js-stellar-sdk/actions/workflows/tests.yml/badge.svg" /></a>
  <a href="https://deepwiki.com/stellar/js-stellar-sdk"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" /></a>
</p>

`js-stellar-sdk` is a JavaScript library for communicating with a
[Stellar Horizon server](https://developers.stellar.org/docs/data/apis/horizon)
and [Stellar RPC](https://developers.stellar.org/docs/data/apis/rpc). While
primarily intended for applications built on Node.js or in the browser, it can
be adapted for use in other environments with some tinkering.

The library provides:

- a networking layer API for Horizon endpoints (REST-based),
- a networking layer for Soroban RPC (JSONRPC-based).
- facilities for building and signing transactions, for communicating with a
  Stellar Horizon instance, and for submitting transactions or querying network
  history.

**Jump to:**

- [Installation](#installation): details on hitting the ground running
- [Usage](#usage): links to documentation and a variety of workarounds for
  non-traditional JavaScript environments
  - [...with React Native](#usage-with-react-native)
  - [...with Expo](#usage-with-expo-managed-workflows)
  - [...with CloudFlare Workers](#usage-with-cloudflare-workers)
  - [...with Deno](#usage-with-deno)
- [CLI](#cli): generate TypeScript bindings for Stellar smart contracts
- [Migrating](#migrating): migration guides for breaking changes
- [Developing](#developing): contribute to the project!
- [License](#license)

## Installation

Using npm, pnpm, or yarn to include `stellar-sdk` in your own project:

```shell
npm install --save @stellar/stellar-sdk
# or
pnpm add @stellar/stellar-sdk
# or
yarn add @stellar/stellar-sdk
# or
deno add npm:@stellar/stellar-sdk
```

Then, require or import it in your JavaScript code:

```js
var StellarSdk = require("@stellar/stellar-sdk");
// or
import * as StellarSdk from "@stellar/stellar-sdk";
```

(Preferably, you would only import the pieces you need to enable tree-shaking
and lower your final bundle sizes.)

### Browsers

You can use a CDN:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/stellar-sdk/{version}/stellar-sdk.js"></script>
```

> **Note:** Always make sure that you are using the latest version number. They can be found on the [releases page](https://github.com/stellar/js-stellar-sdk/releases) in GitHub.

### Custom Installation

The default bundle uses a native-fetch HTTP client with no axios dependency. If
you need the axios transport (for example, to match the behavior of older SDK
versions), set the `USE_AXIOS` environment variable to `true` when building.

#### Build with Axios

```
pnpm run build:lib:axios
```

This will create `stellar-sdk-axios.js` in `dist/`. Consumers can also import
the axios-backed entry from Node via `@stellar/stellar-sdk/axios`.

### Migrating from @stellar/stellar-base

`@stellar/stellar-base` is now folded into `@stellar/stellar-sdk`. Its classes
and functions are bundled in and re-exported from the top level, so the SDK is
the only package you need.

This only matters if you import `@stellar/stellar-base` directly. If you depend
on `@stellar/stellar-sdk` and never installed the base package separately, skip
this section. The fold-in landed in `@stellar/stellar-sdk` v16.0.0; on earlier
versions the SDK still depends on the separate base package, so don't remove it
there.

To migrate:

1. Install `@stellar/stellar-sdk` if you don't already (see
   [Installation](#installation)).

2. Update your imports. The symbols you import keep their names, so a
   project-wide find and replace of `"@stellar/stellar-base"` with
   `"@stellar/stellar-sdk"` usually does it:

   ```js
   // before
   import { Keypair, TransactionBuilder, Asset } from "@stellar/stellar-base";

   // after
   import { Keypair, TransactionBuilder, Asset } from "@stellar/stellar-sdk";
   ```

3. Uninstall the base package:

   ```shell
   npm uninstall @stellar/stellar-base
   ```

Don't keep both packages installed. Two copies of the base library cause
confusing runtime errors, such as `instanceof` checks failing on values that
look correct.

If you only use the offline primitives (`StrKey`, `Keypair`,
`TransactionBuilder`, `xdr`, and friends), you can import them from the `/base`
subpath instead of the package root:

```js
import { StrKey, Keypair } from "@stellar/stellar-sdk/base";
```

This loads only the former stellar-base modules, skipping Horizon, RPC, and the
SEP helpers (federation, web auth, stellar.toml) and their networking
dependencies. In CommonJS environments — where `require()` can't tree-shake the
root barrel — this is noticeably leaner and avoids pulling in dependencies like
`axios`, `eventsource`, and `smol-toml`.

## Versioning and compatibility

Always use the latest `@stellar/stellar-sdk`. The Stellar network upgrades its
protocol periodically, and an older SDK may fail to decode newer data (for
example, newer XDR). You can check the protocol a network currently runs in the
`current_protocol_version` field of its Horizon root (for example
[horizon.stellar.org](https://horizon.stellar.org/) for Mainnet; Testnet and
Futurenet expose their own).

These docs and the API reference cover the latest version only. To read docs for
an older version, find its Git tag on the
[releases page](https://github.com/stellar/js-stellar-sdk/releases) and browse
the `docs/` directory at that ref on GitHub. The release notes there mark the
breaking changes in each version.

## Usage

The usage documentation for this library lives in a handful of places:

- across the [Stellar Developer Docs](https://developers.stellar.org), which
  includes tutorials and examples, and
- on the generated [API doc site](https://stellar.github.io/js-stellar-sdk/) —
  which also publishes
  [agent-friendly bundles, raw markdown siblings, and a crawler policy](https://stellar.github.io/js-stellar-sdk/agents/)
  for AI tools. The site's URL, base path, and AI policy values live in
  [`config/site.ts`](https://github.com/stellar/js-stellar-sdk/blob/main/config/site.ts).

### AI agent documentation

Agents can use the documentation bundles published on the website:

- [`llms.txt`](https://stellar.github.io/js-stellar-sdk/llms.txt) — an index of
  the guides, reference pages, and other agent-facing docs.
- [`llms-full.txt`](https://stellar.github.io/js-stellar-sdk/llms-full.txt) —
  the full documentation corpus plus the changelog in one text file.

These generated bundles are not committed to the repo. To inspect bundles for a
local branch, run `pnpm docs:llms`; the generated files are written under
`public/` for the website build.

You can also refer to:

- the [documentation](https://developers.stellar.org/docs/data/horizon) for the
  Horizon REST API (if using the `Horizon` module) and
- the [documentation](https://developers.stellar.org/docs/data/rpc) for Soroban
  RPC's API (if using the `rpc` module)

### Usage with Jest

Some of the SDK's dependencies (`@noble/hashes`, `@noble/ed25519`,
`uint8array-extras`, `@exodus/bytes`) ship only ES modules. Node itself handles
this (`require(esm)` is unflagged from Node 22.12.0, the minimum this SDK
supports), but Jest's default transform pipeline does not: tests that load the
SDK fail with
`SyntaxError: Cannot use import statement outside a module` coming from inside
`node_modules`.

Tell Jest to transform those packages instead of skipping them:

```js
// jest.config.js
module.exports = {
  transformIgnorePatterns: [
    "node_modules/(?!(\\.pnpm|@noble|@exodus|uint8array-extras)/)",
  ],
};
```

`.pnpm` belongs in that list even though it is not a package. Under pnpm the
real path is `node_modules/.pnpm/<pkg>@<version>/node_modules/<pkg>/…`, so
without it the pattern matches at the first `node_modules/` segment and the
package is skipped before the name is ever compared.

If you compile tests with ts-jest or Babel, also make sure the compilation
target is `es2020` or later — the SDK and its crypto dependencies use native
`BigInt`, and downleveling below `es2020` breaks it at runtime (for example
`TypeError: Cannot convert a BigInt value to a number`).

### Usage with React Native

The SDK works in React Native, and as of v17 it no longer needs a `Buffer`
polyfill. The one thing you still need to provide in your app's entry file:

- **A Web Crypto random source.** `Keypair.random()` and SEP-10 challenge
  generation call `crypto.getRandomValues()`, which React Native doesn't
  provide out of the box. Add a polyfill that registers it on the global scope,
  imported once before any SDK code runs.

Modern React Native uses Metro with autolinking, so beyond adding the polyfill
above, no manual native linking or custom resolver config is required.

If you use Horizon streaming (`server.…().stream()`), be aware it depends on an
`EventSource`, which is now an included dependency and will work in any runtimes
that support [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch),
[ReadableStream](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream),
[TextDecoder](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder),
[URL](https://developer.mozilla.org/en-US/docs/Web/API/URL),
[Event](https://developer.mozilla.org/en-US/docs/Web/API/Event),
[MessageEvent](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent),
[EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget).

React Native apps using the Hermes engine may need to polyfill broken typed
array methods such as `subarray`, since this compatibility is no longer
provided by `@stellar/js-xdr`. If you run into issues, consider a polyfill such
as `@exodus/patch-broken-hermes-typed-arrays`.

#### Usage with Expo managed workflows

Expo has the same requirement as React Native above — a
`crypto.getRandomValues()` source. Install a polyfill for it (use
`npx expo install` so versions are matched to your Expo SDK) and import it at
the top of your entry point (by default `App.js`) before any SDK code.

Once `crypto.getRandomValues()` is available, `Keypair.random()` works normally
— the manual `expo-random` workaround from older Expo SDKs is no longer needed.

#### Usage with CloudFlare Workers

The SDK defaults to a native-`fetch` HTTP client, so Horizon and RPC requests
work in the Workers runtime without an HTTP adapter. As of v17 the SDK no
longer uses `Buffer`, so the
[`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
flag is no longer required for it. The one thing to watch for:

- **Streaming.** Horizon's `.stream()` depends on `EventSource`; long-lived
  streaming connections don't fit the Workers request model well, so prefer
  polling (`.call()` / `.cursor()`) for Horizon data in a Worker.

### Usage with Deno

Deno pulls the SDK in through its npm compatibility layer. Add it to your
`deno.json` (see [Installation](#installation)) and import the bare specifier,
or skip that step and import the `npm:` specifier directly:

```js
import * as StellarSdk from "@stellar/stellar-sdk";
// or, without adding it to deno.json
import * as StellarSdk from "npm:@stellar/stellar-sdk";
```

Two Deno-specific things to keep in mind:

- **Permissions.** Horizon and RPC calls need network access, so run with
  `--allow-net` (or scope it, e.g.
  `--allow-net=horizon-testnet.stellar.org,soroban-testnet.stellar.org`).
- **The CLI.** Run it without installing anything:
  `deno run -A npm:@stellar/stellar-sdk` (see [CLI](#cli)).

## CLI

The SDK includes a command-line tool for generating TypeScript bindings from
Stellar smart contracts. These bindings provide fully-typed client code with IDE
autocompletion and compile-time type checking.

### Running the CLI

```shell
# Using npx (no installation required)
npx @stellar/stellar-sdk generate [options]

# Or if installed globally
stellar-js generate [options]
```

### Generating Bindings

You can generate bindings from three different sources:

#### From a local WASM file

```shell
npx @stellar/stellar-sdk generate \
  --wasm ./path/to/wasm_file/my_contract.wasm \
  --output-dir ./my-contract-client \
  --contract-name my-contract
```

#### From a WASM hash on the network

```shell
# testnet, futurenet, and localnet have default RPC URLs
npx @stellar/stellar-sdk generate \
  --wasm-hash <hex-encoded-hash> \
  --network testnet \
  --output-dir ./my-contract-client \
  --contract-name my-contract
```

#### From a deployed contract ID

```shell
npx @stellar/stellar-sdk generate \
  --contract-id CABC...XYZ \
  --network testnet \
  --output-dir ./my-contract-client
```

#### With custom RPC server options

For mainnet or when connecting to RPC servers that require authentication:

```shell
# Mainnet requires --rpc-url (no default)
npx @stellar/stellar-sdk generate \
  --contract-id CABC...XYZ \
  --rpc-url https://my-rpc-provider.com \
  --network mainnet \
  --output-dir ./my-contract-client

# With custom timeout and headers for authenticated RPC servers
npx @stellar/stellar-sdk generate \
  --contract-id CABC...XYZ \
  --rpc-url https://my-rpc-server.com \
  --network mainnet \
  --output-dir ./my-contract-client \
  --timeout 30000 \
  --headers '{"Authorization": "Bearer my-token"}'

# localnet with default RPC URL auto-enables --allow-http
npx @stellar/stellar-sdk generate \
  --contract-id CABC...XYZ \
  --network localnet \
  --output-dir ./my-contract-client

# When overriding the default URL, you must specify --allow-http if using HTTP
npx @stellar/stellar-sdk generate \
  --contract-id CABC...XYZ \
  --rpc-url http://my-local-server:8000/rpc \
  --network localnet \
  --output-dir ./my-contract-client \
  --allow-http
```

### CLI Options

| Option                   | Description                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| `--wasm <path>`          | Path to a local WASM file                                                                       |
| `--wasm-hash <hash>`     | Hex-encoded hash of WASM blob on the network                                                    |
| `--contract-id <id>`     | Contract ID of a deployed contract                                                              |
| `--rpc-url <url>`        | Stellar RPC server URL (has defaults for testnet/futurenet/localnet, required for mainnet)      |
| `--network <network>`    | Network to use: `testnet`, `mainnet`, `futurenet`, or `localnet` (required for network sources) |
| `--output-dir <dir>`     | Output directory for generated bindings (required)                                              |
| `--contract-name <name>` | Name for the generated package (derived from filename if not provided)                          |
| `--overwrite`            | Overwrite existing files in the output directory                                                |
| `--allow-http`           | Allow insecure HTTP connections to RPC server (default: false)                                  |
| `--timeout <ms>`         | RPC request timeout in milliseconds                                                             |
| `--headers <json>`       | Custom headers as JSON object (e.g., `'{"Authorization": "Bearer token"}'`)                     |

#### Default RPC URLs

When using `--network`, the CLI provides default RPC URLs for most networks:

| Network     | Default RPC URL                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------ |
| `testnet`   | `https://soroban-testnet.stellar.org`                                                                              |
| `futurenet` | `https://rpc-futurenet.stellar.org`                                                                                |
| `localnet`  | `http://localhost:8000/rpc` (auto-enables `--allow-http` only when using default URL)                              |
| `mainnet`   | None - you must provide `--rpc-url` ([find providers](https://developers.stellar.org/docs/data/rpc/rpc-providers)) |

### Generated Output

The CLI generates a complete npm package structure:

```
my-contract-client/
├── src/
│   ├── index.ts      # Barrel exports
│   ├── client.ts     # Typed Client class with contract methods
│   └── types.ts      # TypeScript interfaces for contract types
├── package.json
├── tsconfig.json
├── README.md
└── .gitignore
```

### Using Generated Bindings

After generating, you can use the bindings in your project:

```typescript
import { Client } from "./my-contract-client";

const client = new Client({
  contractId: "CABC...XYZ",
  networkPassphrase: Networks.TESTNET,
  rpcUrl: "https://soroban-testnet.stellar.org",
  publicKey: keypair.publicKey(),
  ...basicNodeSigner(keypair, Networks.TESTNET),
});

// Fully typed method calls with IDE autocompletion
const result = await client.transfer({
  from: "GABC...",
  to: "GDEF...",
  amount: 1000n,
});
```

## Migrating

Upgrading from an earlier version? The
[Migration Guide](https://stellar.github.io/js-stellar-sdk/guides/00-migration/)
lists every breaking change by SDK version, newest first, and links to the
deep-dive guides for the largest ones.

## Developing

So you want to contribute to the library: welcome! Whether you're working on a
fork or want to make an upstream request, the dev-test loop is pretty
straightforward.

1. Clone the repo:

```shell
git clone https://github.com/stellar/js-stellar-sdk.git
```

2. Install Node

Because we support the oldest maintenance version of Node, please install and
develop on the version pinned in
[`.nvmrc`](https://github.com/stellar/js-stellar-sdk/blob/main/.nvmrc)
(currently Node 22; the minimum supported is 22.12.0) so you don't get
surprised when your code works locally but breaks in CI.

Here's how to install `nvm` if you haven't: https://github.com/creationix/nvm

```shell
nvm install
```

If you work on several projects that use different Node versions, you might it
helpful to install this automatic version manager:
https://github.com/wbyoung/avn

3. Enable Corepack

```shell
corepack enable
```

4. Install dependencies inside js-stellar-sdk folder:

```shell
cd js-stellar-sdk
pnpm install
```

5. Observe the project's code style

While you're making changes, make sure to run the linter to catch any linting
errors (in addition to making sure your text editor supports ESLint) and conform
to the project's code style.

```shell
pnpm run fmt
```

### Building

You can build the developer version (unoptimized, commented, with source maps,
etc.) or the production bundles:

```shell
pnpm run build
# or
pnpm run build:prod
```

### Testing

To run all tests:

```shell
pnpm run test
```

To run a specific set of tests:

```shell
pnpm run test:node
pnpm run test:browser
pnpm run test:integration
```

To generate and check the documentation site:

```shell
# generate the docs site (reference pages, llms bundles, and the Astro site under dist/site)
pnpm run docs

# preview the built site in a browser
pnpm docs:preview

# the preview server prints the local URL (default http://localhost:4321)

# for a live-reloading dev server instead, use:
pnpm docs:dev
```

### Publishing

For information on how to contribute or publish new versions of this software to
`npm`, please refer to our
[contribution guide](https://github.com/stellar/js-stellar-sdk/blob/main/CONTRIBUTING.md).

## Miscellaneous

### License

js-stellar-sdk is licensed under an Apache-2.0 license. See the
[LICENSE](https://github.com/stellar/js-stellar-sdk/blob/main/LICENSE) file
for details.


---

## 41. agents
- **URL:** https://github.com/devtechedge/agents
- **Language:** Python
- **Topics:** None
- **Description:** A framework for building realtime voice AI agents ≡ƒñû≡ƒÄÖ∩╕Å≡ƒô╣ 

### README.md

<!--BEGIN_BANNER_IMAGE-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/.github/banner_dark.png">
  <source media="(prefers-color-scheme: light)" srcset="/.github/banner_light.png">
  <img style="width:100%;" alt="The LiveKit icon, the name of the repository and some sample code in the background." src="https://raw.githubusercontent.com/livekit/agents/main/.github/banner_light.png">
</picture>

<!--END_BANNER_IMAGE-->
<br />

![PyPI - Version](https://img.shields.io/pypi/v/livekit-agents)
[![PyPI Downloads](https://static.pepy.tech/badge/livekit-agents/month)](https://pepy.tech/projects/livekit-agents)
[![Slack community](https://img.shields.io/endpoint?url=https%3A%2F%2Flivekit.io%2Fbadges%2Fslack)](https://livekit.io/join-slack)
[![Twitter Follow](https://img.shields.io/twitter/follow/livekit)](https://twitter.com/livekit)
[![Ask DeepWiki for understanding the codebase](https://deepwiki.com/badge.svg)](https://deepwiki.com/livekit/agents)
[![License](https://img.shields.io/github/license/livekit/livekit)](https://github.com/livekit/livekit/blob/master/LICENSE)

<br />

Looking for the JS/TS library? Check out [AgentsJS](https://github.com/livekit/agents-js)

## What is Agents?

<!--BEGIN_DESCRIPTION-->

The Agent Framework is designed for building realtime, programmable participants
that run on servers. Use it to create conversational, multi-modal voice
agents that can see, hear, and understand.

<!--END_DESCRIPTION-->

## Features

- **Flexible integrations**: A comprehensive ecosystem to mix and match the right STT, LLM, TTS, and Realtime API to suit your use case.
- **Integrated job scheduling**: Built-in task scheduling and distribution with [dispatch APIs](https://docs.livekit.io/agents/build/dispatch/) to connect end users to agents.
- **Extensive WebRTC clients**: Build client applications using LiveKit's open-source SDK ecosystem, supporting all major platforms.
- **Telephony integration**: Works seamlessly with LiveKit's [telephony stack](https://docs.livekit.io/sip/), allowing your agent to make calls to or receive calls from phones.
- **Exchange data with clients**: Use [RPCs](https://docs.livekit.io/home/client/data/rpc/) and other [Data APIs](https://docs.livekit.io/home/client/data/) to seamlessly exchange data with clients.
- **Semantic turn detection**: Uses a transformer model to detect when a user is done with their turn, helps to reduce interruptions.
- **MCP support**: Native support for MCP. Integrate tools provided by MCP servers with one line of code.
- **Builtin test framework**: Write tests and use judges to ensure your agent is performing as expected.
- **Open-source**: Fully open-source, allowing you to run the entire stack on your own servers, including [LiveKit server](https://github.com/livekit/livekit), one of the most widely used WebRTC media servers.

## Installation

To install the core Agents library, along with plugins for popular model providers:

```bash
pip install "livekit-agents[openai,deepgram,cartesia]"
```

## Docs and guides

Documentation on the framework and how to use it can be found [here](https://docs.livekit.io/agents/)

### Building with AI coding agents

If you're using an AI coding assistant to build with LiveKit Agents, we recommend the following setup for the best results:

1. **Install the [LiveKit Docs MCP server](https://docs.livekit.io/mcp)** — Gives your coding agent access to up-to-date LiveKit documentation, code search across LiveKit repositories, and working examples.

2. **Install the [LiveKit Agent Skill](https://github.com/livekit/agent-skills)** — Provides your coding agent with architectural guidance and best practices for building voice AI applications, including workflow design, handoffs, tasks, and testing patterns.

   ```shell
   npx skills add livekit/agent-skills --skill livekit-agents
   ```

The Agent Skill works best alongside the MCP server: the skill teaches your agent *how to approach* building with LiveKit, while the MCP server provides the *current API details* to implement it correctly.

## Core concepts

- Agent: An LLM-based application with defined instructions.
- AgentSession: A container for agents that manages interactions with end users.
- entrypoint: The starting point for an interactive session, similar to a request handler in a web server.
- AgentServer: The main process that coordinates job scheduling and launches agents for user sessions.

## Usage

### Simple voice agent

---

```python
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    RunContext,
    cli,
    function_tool,
    inference,
)


@function_tool
async def lookup_weather(
    context: RunContext,
    location: str,
):
    """Used to look up weather information."""

    return {"weather": "sunny", "temperature": 70}


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    session = AgentSession(
        vad=inference.VAD(),
        # any combination of STT, LLM, TTS, or realtime API can be used
        # this example shows LiveKit Inference, a unified API to access different models via LiveKit Cloud
        # to use model provider keys directly, replace with the following:
        # from livekit.plugins import deepgram, openai, cartesia
        # stt=deepgram.STT(model="nova-3"),
        # llm=openai.LLM(model="gpt-4.1-mini"),
        # tts=cartesia.TTS(model="sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc"),
        stt=inference.STT("deepgram/nova-3", language="multi"),
        llm=inference.LLM("google/gemma-4-31b-it"),  # low-latency gemma, hosted on LiveKit
        tts=inference.TTS("cartesia/sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc"),
    )

    agent = Agent(
        instructions="You are a friendly voice assistant built by LiveKit.",
        tools=[lookup_weather],
    )

    await session.start(agent=agent, room=ctx.room)
    await session.generate_reply(instructions="greet the user and ask about their day")


if __name__ == "__main__":
    cli.run_app(server)
```

You'll need the following environment variables for this example:

- LIVEKIT_URL
- LIVEKIT_API_KEY
- LIVEKIT_API_SECRET

### Multi-agent handoff

---

This code snippet is abbreviated. For the full example, see the [LiveKit docs](https://docs.livekit.io/agents/handoffs/)

```python
...
class IntroAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=f"You are a story teller. Your goal is to gather a few pieces of information from the user to make the story personalized and engaging."
            "Ask the user for their name and where they are from"
        )

    async def on_enter(self):
        self.session.generate_reply(instructions="greet the user and gather information")

    @function_tool
    async def information_gathered(
        self,
        context: RunContext,
        name: str,
        location: str,
    ):
        """Called when the user has provided the information needed to make the story personalized and engaging.

        Args:
            name: The name of the user
            location: The location of the user
        """

        context.userdata.name = name
        context.userdata.location = location

        story_agent = StoryAgent(name, location)
        return story_agent, "Let's start the story!"


class StoryAgent(Agent):
    def __init__(self, name: str, location: str) -> None:
        super().__init__(
            instructions=f"You are a storyteller. Use the user's information in order to make the story personalized."
            f"The user's name is {name}, from {location}",
            # override the default model, switching to Realtime API from standard LLMs
            llm=openai.realtime.RealtimeModel(voice="echo"),
            chat_ctx=chat_ctx,
        )

    async def on_enter(self):
        self.session.generate_reply()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    userdata = StoryData()
    session = AgentSession[StoryData](
        vad=inference.VAD(),
        stt="deepgram/nova-3",
        llm="google/gemma-4-31b-it",  # low-latency gemma, hosted on LiveKit
        tts="cartesia/sonic-3:9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
        userdata=userdata,
    )

    await session.start(
        agent=IntroAgent(),
        room=ctx.room,
    )
...
```

### Testing

Automated tests are essential for building reliable agents, especially with the non-deterministic behavior of LLMs. LiveKit Agents include native test integration to help you create dependable agents.

```python
@pytest.mark.asyncio
async def test_no_availability() -> None:
    llm = google.LLM()
    async with AgentSession(llm=llm) as sess:
        await sess.start(MyAgent())
        result = await sess.run(
            user_input="Hello, I need to place an order."
        )
        result.expect.skip_next_event_if(type="message", role="assistant")
        result.expect.next_event().is_function_call(name="start_order")
        result.expect.next_event().is_function_call_output()
        await (
            result.expect.next_event()
            .is_message(role="assistant")
            .judge(llm, intent="assistant should be asking the user what they would like")
        )

```

## Examples

For more examples and detailed setup instructions, see the [examples directory](examples/). For even more examples, see the [python-agents-examples](https://github.com/livekit-examples/python-agents-examples) repository.

<table>
<tr>
<td width="50%">
<h3>🎙️ Starter Agent</h3>
<p>A starter agent optimized for voice conversations.</p>
<p>
<a href="examples/voice_agents/basic_agent.py">Code</a>
</p>
</td>
<td width="50%">
<h3>☎️ Outbound caller</h3>
<p>Agent that makes outbound phone calls</p>
<p>
<a href="https://github.com/livekit-examples/outbound-caller-python">Code</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>🔌 MCP support</h3>
<p>Use tools from MCP servers</p>
<p>
<a href="examples/voice_agents/mcp">Code</a>
</p>
</td>
<td width="50%">
<h3>📝 Multi-user transcriber</h3>
<p>Produce transcriptions from all users in the room</p>
<p>
<a href="examples/other/transcription/multi-user-transcriber.py">Code</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>🎥 Video avatars</h3>
<p>Add an AI avatar with Tavus, Bithuman, LemonSlice, and more</p>
<p>
<a href="examples/avatar/">Code</a>
</p>
</td>
<td width="50%">
<h3>👁️ Gemini Live vision</h3>
<p>Full example (including iOS app) of Gemini Live agent that can see.</p>
<p>
<a href="https://github.com/livekit-examples/vision-demo">Code</a>
</p>
</td>
</tr>

</table>

## Running your agent

### Testing in terminal

```shell
python myagent.py console
```

Runs your agent in terminal mode, enabling local audio input and output for testing.
This mode doesn't require external servers or dependencies and is useful for quickly validating behavior.

### Developing with LiveKit clients

```shell
python myagent.py dev
```

Starts the agent server and enables hot reloading when files change. This mode allows each process to host multiple concurrent agents efficiently.

The agent connects to LiveKit Cloud or your self-hosted server. Set the following environment variables:
- LIVEKIT_URL
- LIVEKIT_API_KEY
- LIVEKIT_API_SECRET

You can connect using any LiveKit client SDK or telephony integration.
To get started quickly, try the [Agents Playground](https://agents-playground.livekit.io/).

### Running for production

```shell
python myagent.py start
```

Runs the agent with production-ready optimizations.

## License

The Agents framework is licensed under [Apache-2.0](LICENSE). The LiveKit turn detection models are licensed under the [LiveKit Model License](MODEL_LICENSE).

## Contributing

The Agents framework is under active development in a rapidly evolving field. We welcome and appreciate contributions of any kind, be it feedback, bugfixes, features, new plugins and tools, or better documentation. You can file issues under this repo, open a PR, or chat with us in the [LiveKit community](https://docs.livekit.io/intro/community/).

### Development setup

This project uses [uv](https://docs.astral.sh/uv/) for package management. To install dependencies for development:

```shell
uv sync --all-extras --dev
```

### Examples

This project includes many examples in the [`examples`](examples/) directory. To run them, create the file `examples/.env` with credentials for LiveKit Server and any necessary model providers (see `examples/.env.example`), then run:

```shell
uv run examples/voice_agents/basic_agent.py dev
```

For more information, see the [examples README](examples/README.md).

### Tests

Unit tests are in the `tests` directory and can be run with:

```shell
uv run pytest --unit
```

Integration tests for each plugin require various API credentials and run automatically in GitHub CI for PRs submitted by project maintainers. See the [tests workflow](.github/workflows/tests.yml) for details.

### Formatting

This project uses [ruff](https://github.com/astral-sh/ruff) for formatting and linting:

```shell
uv run ruff format
uv run ruff check --fix
```

### Documentation

To generate docs locally with [pdoc](https://github.com/pdoc3/pdoc):

```shell
uv sync --all-extras --group docs
uv run --active pdoc --skip-errors --html --output-dir=docs livekit
```

<!--BEGIN_REPO_NAV-->
<br/><table>
<thead><tr><th colspan="2">LiveKit Ecosystem</th></tr></thead>
<tbody>
<tr><td>Agents SDKs</td><td><b>Python</b> · <a href="https://github.com/livekit/agents-js">Node.js</a></td></tr><tr></tr>
<tr><td>LiveKit SDKs</td><td><a href="https://github.com/livekit/client-sdk-js">Browser</a> · <a href="https://github.com/livekit/client-sdk-swift">Swift</a> · <a href="https://github.com/livekit/client-sdk-android">Android</a> · <a href="https://github.com/livekit/client-sdk-flutter">Flutter</a> · <a href="https://github.com/livekit/client-sdk-react-native">React Native</a> · <a href="https://github.com/livekit/rust-sdks">Rust</a> · <a href="https://github.com/livekit/node-sdks">Node.js</a> · <a href="https://github.com/livekit/python-sdks">Python</a> · <a href="https://github.com/livekit/client-sdk-unity">Unity</a> · <a href="https://github.com/livekit/client-sdk-unity-web">Unity (WebGL)</a> · <a href="https://github.com/livekit/client-sdk-esp32">ESP32</a> · <a href="https://github.com/livekit/client-sdk-cpp">C++</a></td></tr><tr></tr>
<tr><td>Starter Apps</td><td><a href="https://github.com/livekit-examples/agent-starter-python">Python Agent</a> · <a href="https://github.com/livekit-examples/agent-starter-node">TypeScript Agent</a> · <a href="https://github.com/livekit-examples/agent-starter-react">React App</a> · <a href="https://github.com/livekit-examples/agent-starter-swift">SwiftUI App</a> · <a href="https://github.com/livekit-examples/agent-starter-android">Android App</a> · <a href="https://github.com/livekit-examples/agent-starter-flutter">Flutter App</a> · <a href="https://github.com/livekit-examples/agent-starter-react-native">React Native App</a> · <a href="https://github.com/livekit-examples/agent-starter-embed">Web Embed</a></td></tr><tr></tr>
<tr><td>UI Components</td><td><a href="https://github.com/livekit/components-js">React</a> · <a href="https://github.com/livekit/components-android">Android Compose</a> · <a href="https://github.com/livekit/components-swift">SwiftUI</a> · <a href="https://github.com/livekit/components-flutter">Flutter</a></td></tr><tr></tr>
<tr><td>Server APIs</td><td><a href="https://github.com/livekit/node-sdks">Node.js</a> · <a href="https://github.com/livekit/server-sdk-go">Golang</a> · <a href="https://github.com/livekit/server-sdk-ruby">Ruby</a> · <a href="https://github.com/livekit/server-sdk-kotlin">Java/Kotlin</a> · <a href="https://github.com/livekit/python-sdks">Python</a> · <a href="https://github.com/livekit/rust-sdks">Rust</a> · <a href="https://github.com/agence104/livekit-server-sdk-php">PHP (community)</a> · <a href="https://github.com/pabloFuente/livekit-server-sdk-dotnet">.NET (community)</a></td></tr><tr></tr>
<tr><td>Resources</td><td><a href="https://docs.livekit.io">Docs</a> · <a href="https://docs.livekit.io/mcp">Docs MCP Server</a> · <a href="https://github.com/livekit/livekit-cli">CLI</a> · <a href="https://cloud.livekit.io">LiveKit Cloud</a></td></tr><tr></tr>
<tr><td>LiveKit Server OSS</td><td><a href="https://github.com/livekit/livekit">LiveKit server</a> · <a href="https://github.com/livekit/egress">Egress</a> · <a href="https://github.com/livekit/ingress">Ingress</a> · <a href="https://github.com/livekit/sip">SIP</a></td></tr><tr></tr>
<tr><td>Community</td><td><a href="https://community.livekit.io">Developer Community</a> · <a href="https://livekit.io/join-slack">Slack</a> · <a href="https://x.com/livekit">X</a> · <a href="https://www.youtube.com/@livekit_io">YouTube</a></td></tr>
</tbody>
</table>
<!--END_REPO_NAV-->


---

## 42. remix
- **URL:** https://github.com/devtechedge/remix
- **Language:** TypeScript
- **Topics:** None
- **Description:** The fully-stacked web framework

### README.md

<br />
<br />

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/remix-wordmark-racing-darkmode.svg">
    <img alt="Remix" src=".github/assets/remix-wordmark-racing-lightmode.svg" width="400">
  </picture>
</p>

<br />
<br />

# Welcome to Remix 3!

This is the source repository for Remix 3. It is under active development.

We published [a blog post](https://remix.run/blog/wake-up-remix) earlier this year with some of our thoughts around Remix 3. It explains our philosophy for web development and why we think the time is right for something new. When working on Remix 3, we follow these principles:

1. **Model-First Development**. AI fundamentally shifts the human-computer interaction model for both user experience and developer workflows. Optimize the source code, documentation, tooling, and abstractions for LLMs. Additionally, develop abstractions for applications to use models in the product itself, not just as a tool to develop it.
2. **Build on Web APIs**. Sharing abstractions across the stack greatly reduces the amount of context switching, both for humans and machines. Build on the foundation of Web APIs and JavaScript because it is the only full stack ecosystem.
3. **Religiously Runtime**. Designing for bundlers/compilers/typegen (and any pre-runtime static analysis) leads to poor API design that eventually pollutes the entire system. All packages must be designed with no expectation of static analysis and all tests must run without bundling. Because browsers are involved, `--import` loaders for simple transformations like TypeScript and JSX are permissible.
4. **Avoid Dependencies**. Dependencies lock you into somebody else's roadmap. Choose them wisely, wrap them completely, and expect to replace most of them with our own package eventually. The goal is zero.
5. **Demand Composition**. Abstractions should be single-purpose and replaceable. A composable abstraction is easy to add and remove from an existing program. Every package must be useful and documented independent of any other context. New features should first be attempted as a new package. If impossible, attempt to break up the existing package to make it more composable. However, tightly coupled modules that almost always change together in both directions should be moved to the same package.
6. **Distribute Cohesively**. Extremely composable ecosystems are difficult to learn and use. Remix will be distributed as a single `remix` package for both distribution and documentation.

## Goals

Although we recommend the `remix` package for ease of use, all packages that make up Remix should be usable standalone as well. This forces us to consider package boundaries and helps us define public interfaces that are portable and interoperable.

Each package in Remix:

- Has a [single responsibility](https://en.wikipedia.org/wiki/Single-responsibility_principle)
- Prioritizes web standards to ensure maximum interoperability and portability across JavaScript runtimes
- Augments standards unobtrusively where they are missing or incomplete, minimizing incompatibility risks

This means Remix code is **portable by default**. Remix packages work seamlessly across [Node.js](https://nodejs.org/), [Bun](https://bun.sh/), [Deno](https://deno.com/), [Cloudflare Workers](https://workers.cloudflare.com/), and other environments.

We leverage server-side web APIs when they are available:

- [The Web Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API) instead of `node:stream`
- [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instead of Node.js `Buffer`s
- [The Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) instead of `node:crypto`
- [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) and [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File) instead of some bespoke runtime-specific API

The benefit is code that's not just reusable, but **future-proof**.

## Packages

Most packages in this repository are standalone JavaScript/TypeScript tools. The `remix` package composes them under one umbrella for distribution and documentation.

- [assert](packages/assert): Node assert-compatible utilities for any JavaScript environment
- [assets](packages/assets): Fetch-based server for compiling browser JS/TS and CSS assets on demand
- [async-context-middleware](packages/async-context-middleware): Middleware for storing request context in AsyncLocalStorage
- [auth](packages/auth): Browser login, OAuth, and OIDC helpers for Remix
- [auth-middleware](packages/auth-middleware): Pluggable authentication middleware for Remix
- [cli](packages/cli): Command-line interface for Remix
- [compression-middleware](packages/compression-middleware): Middleware for compressing HTTP responses
- [cookie](packages/cookie): A toolkit for working with cookies in JavaScript
- [cop-middleware](packages/cop-middleware): Middleware for tokenless cross-origin protection in Fetch API servers
- [cors-middleware](packages/cors-middleware): Middleware for handling CORS in Fetch API servers
- [csrf-middleware](packages/csrf-middleware): Middleware for CSRF protection in Fetch API servers
- [data-schema](packages/data-schema): Tiny, standards-aligned schema validation
- [data-table](packages/data-table): A typed, relational query toolkit for JavaScript
- [data-table-mysql](packages/data-table-mysql): MySQL database implementation for remix/data-table
- [data-table-postgres](packages/data-table-postgres): PostgreSQL database implementation for remix/data-table
- [data-table-sqlite](packages/data-table-sqlite): SQLite database implementation for remix/data-table
- [fetch-proxy](packages/fetch-proxy): An HTTP proxy for the web Fetch API
- [fetch-router](packages/fetch-router): A minimal, composable router for the web Fetch API
- [file-storage](packages/file-storage): Key/value storage for JavaScript File objects
- [file-storage-s3](packages/file-storage-s3): S3 backend for remix/file-storage
- [form-data-middleware](packages/form-data-middleware): Middleware for parsing FormData from request bodies
- [form-data-parser](packages/form-data-parser): A request.formData() wrapper with streaming file upload handling
- [fs](packages/fs): Filesystem utilities using the Web File API
- [headers](packages/headers): A toolkit for working with HTTP headers in JavaScript
- [html-template](packages/html-template): HTML template tag with auto-escaping for JavaScript
- [lazy-file](packages/lazy-file): Lazy, streaming files for JavaScript
- [logger-middleware](packages/logger-middleware): Middleware for logging HTTP requests and responses
- [method-override-middleware](packages/method-override-middleware): Middleware for overriding HTTP request methods from form data
- [mime](packages/mime): Utilities for working with MIME types
- [multipart-parser](packages/multipart-parser): A fast, efficient parser for multipart streams in any JavaScript environment
- [node-fetch-server](packages/node-fetch-server): Build servers for Node.js using the web fetch API
- [node-hmr](packages/node-hmr): Run Node.js applications with hot module reloading
- [node-tsx](packages/node-tsx): Run Node.js with TypeScript and JSX syntax support
- [remix](packages/remix): The Remix web framework
- [response](packages/response): Response helpers for the web Fetch API
- [route-pattern](packages/route-pattern): Match and generate URLs with strong typing
- [session](packages/session): Session management for JavaScript
- [session-middleware](packages/session-middleware): Middleware for managing sessions with cookie-based storage
- [session-storage-memcache](packages/session-storage-memcache): Memcache session storage for remix/session
- [session-storage-redis](packages/session-storage-redis): Redis session storage for remix/session
- [static-middleware](packages/static-middleware): Middleware for serving static files from the filesystem
- [tar-parser](packages/tar-parser): A fast, efficient parser for tar streams in any JavaScript environment
- [terminal](packages/terminal): Terminal output utilities for JavaScript libraries and CLIs
- [test](packages/test): A test framework for JavaScript and TypeScript projects
- [ui](packages/ui): View layer with reconciler, component model, and first-party UI components
- [ui-hmr](packages/ui-hmr): Hot module replacement runtime and transforms for Remix UI components

## Installation

To try the current Remix beta, install the `next` dist-tag:

```sh
npm install remix@next
```

To create a new Remix app with the CLI, use `npx remix@next new`:

```sh
npx remix@next new my-remix-app
```

If you want to play around with the bleeding edge, we also build the latest `main` branch into a `preview/main` branch which can be [installed directly](https://pnpm.io/package-sources#install-from-a-git-repository-combining-different-parameters) with `pnpm` (version 9+):

```sh
pnpm install "remix-run/remix#preview/main&path:packages/remix"
```

Or, just install a single package:

```
pnpm install "remix-run/remix#preview/main&path:packages/fetch-router"
```

## Agent Skills For Building Apps

Agents that are starting a Remix 3 app from this repository should use the [`remix` app skill](./.agents/skills/remix/SKILL.md). The CLI prepack step copies this skill into the app template so generated apps can use the same guidance.

## Contributing

We welcome contributions! If you'd like to contribute, please feel free to open an issue or submit a pull request. See [CONTRIBUTING](https://github.com/remix-run/remix/blob/main/CONTRIBUTING.md) for more information.

## License

See [LICENSE](https://github.com/remix-run/remix/blob/main/LICENSE)


---

## 43. reviewgate
- **URL:** https://github.com/devtechedge/reviewgate
- **Language:** Python
- **Topics:** None
- **Description:** Make pull requests reviewable before humans waste time on them

### README.md

# ReviewGate

> Make pull requests reviewable before humans waste time on them.

[![CI](https://github.com/leo-aa88/reviewgate/actions/workflows/ci.yml/badge.svg)](https://github.com/leo-aa88/reviewgate/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-brightgreen.svg)](#testing)
[![Status: beta](https://img.shields.io/badge/status-beta-orange.svg)](#status)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://www.conventionalcommits.org)

ReviewGate is a deterministic **pull-request intake gate**. It checks
whether a PR is *reviewable* (size, scope, missing context, risky
paths, splitability) before humans spend time on it. It does **not**
review code correctness, security, or merge safety — that's a
deliberate, narrow scope. See [`docs/DESIGN.md`](docs/DESIGN.md) for
the full design and product thesis.

This repository is the **open-source** home for ReviewGate under
Apache 2.0:

* [`reviewgate-core`](src/reviewgate/core/) — the deterministic
  reviewability engine (`reviewgate.core`, pure Python, no I/O).
* [`src/reviewgate_action/`](src/reviewgate_action/) — the GitHub Action
  wrapper that runs the engine on every PR.

The **hosted GitHub App** and **LLM-augmented report layer** are also
open source in this repository under [`src/reviewgate/app/`](src/reviewgate/app/).
The public PR URL analyzer remains future work, tracked openly on the
[issue tracker](https://github.com/leo-aa88/reviewgate/issues); any
future packaging split is for deployment only, not a proprietary fork.
See [`docs/DESIGN.md` §19](docs/DESIGN.md).

---

## Table of contents

- [Why ReviewGate?](#why-reviewgate)
- [What ReviewGate is — and is not](#what-reviewgate-is--and-is-not)
- [Quickstart (5 minutes)](#quickstart-5-minutes)
- [How it works](#how-it-works)
- [Configuration](#configuration)
- [The deterministic engine](#the-deterministic-engine)
- [GitHub Action](#github-action)
- [CLI usage](#cli-usage)
- [Onboarding](#onboarding)
- [Docker image](#docker-image)
- [Hosted stack (local)](docs/HOSTED_LOCAL.md)
- [Makefile (local development)](#makefile-local-development)
- [Project layout](#project-layout)
- [Status](#status)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Governance](GOVERNANCE.md)
- [Security](#security)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Why ReviewGate?

AI-assisted coding raised PR volume. It did not raise human review
capacity. Teams now see more PRs, larger diffs, weaker descriptions,
mixed concerns, and review fatigue.

ReviewGate doesn't try to compete with AI code review. It owns the
step *before* review:

> **Is this PR shaped well enough for a human reviewer to spend time
> on it?**

A senior engineer may already know a PR is unreviewable, but saying
so manually creates social friction. ReviewGate turns subjective
reviewer frustration into neutral workflow enforcement.

```text
PR opened or updated
→ ReviewGate analyzes reviewability
→ comment + labels + status check
→ author fixes PR before reviewers waste time
```

---

## What ReviewGate is — and is not

| ReviewGate **is** | ReviewGate **is not** |
| --- | --- |
| A PR intake checker | An AI code reviewer |
| A reviewability gate | A security or vulnerability scanner |
| Pre-review quality tooling | A bug finder |
| Reviewer-time protection | A Copilot replacement |
| A GitHub workflow enforcement tool | A CI optimizer or a linter for code style |
| An open-source rules engine with optional hosted enforcement | An "AI-origin" or "AI slop" detector |

**Language rule.** ReviewGate does not accuse authors of using AI and
does not label PRs as AI-generated. It evaluates observable PR shape
only — it should never care whether a PR came from a human, Copilot,
Cursor, Claude, Devin, or an internal agent.

---

## Quickstart (5 minutes)

The full step-by-step is in [`docs/QUICKSTART.md`](docs/QUICKSTART.md).
The short version:

```yaml
# .github/workflows/reviewgate.yml
name: ReviewGate

on:
  pull_request:
    types: [opened, synchronize, edited, reopened]

jobs:
  reviewgate:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      # Pre-release docs use @main until the first public tag is cut.
      # After v0.1.0, pin a release tag instead.
      - uses: leo-aa88/reviewgate@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          fail-on: FAIL
          post-comment: true
          mode: action
```

`mode: action` makes the Action own comments and `fail-on` enforcement;
the hosted App uses the `.reviewgate.yml` default `mode: app` instead.
That workflow gives you the §10 deterministic verdict on every PR, a
Markdown summary in the workflow run, and a single PR comment that
updates in place on each push (using the `<!-- reviewgate-report -->`
marker). To make the gate **block merges**, mark the workflow as a
required status check in branch protection (Settings → Branches).
[`docs/QUICKSTART.md`](docs/QUICKSTART.md) walks through that and the
recommended `.reviewgate.yml` starter.

---

## How it works

```text
                   ┌─────────────────────────────────────────────────┐
                   │  open-source `reviewgate-core` (this repo)       │
                   │                                                 │
   GitHub PR ───►  │  EngineInput  ──►  analyze()  ──►  Reviewability │
                   │  (§10.1 JSON)        │            Report (§10.2) │
                   │                       └── pure, no I/O (§4.1)   │
                   └────────────────────────────┬────────────────────┘
                                                │
              ┌─────────────────────────────────┼─────────────────────────────┐
              │                                 │                             │
   ┌──────────▼───────────┐         ┌───────────▼────────────┐   ┌────────────▼───────────┐
   │  reviewgate-action   │         │  Hosted ReviewGate App │   │  Local CLI             │
   │  (this repo)         │         │  (this repo; app extra)│   │  reviewgate-core       │
   │  GitHub Action       │         │  webhooks + LLM layer  │   │  → fixture JSON in     │
   │  fetches PR, runs    │         │  + status check        │   │    report JSON out     │
   │  engine, comments,   │         │  (§4.3, §11)           │   │  (§5.1)                │
   │  applies fail-on     │         │                        │   │                        │
   │  policy (§14)        │         │                        │   │                        │
   └──────────────────────┘         └────────────────────────┘   └────────────────────────┘
```

The deterministic engine has a **hard purity boundary** (§4.1):

* no GitHub API calls,
* no network I/O,
* no filesystem writes,
* no database access,
* no LLM calls,
* no comments, labels, or status checks,
* no side effects.

CI enforces the boundary via [`tests/test_core_purity.py`](tests/test_core_purity.py),
which parses every `.py` file under `src/reviewgate/core/` with `ast`
and fails any change that imports a forbidden module. The same test
asserts `pyproject.toml` does not pull a forbidden runtime dependency.

---

## Configuration

Drop a `.reviewgate.yml` at the repo root on the default branch. Every
key has a documented default; an empty file is valid.

```yaml
version: 1
mode: app                           # §14.1 coexistence: app | action | both
llm_reports: false                  # §21.3 — hosted-App-only, opt-in

thresholds:                          # §10.3
  warn:
    files_changed: 25
    human_loc_changed: 800
  fail:
    files_changed: 75
    human_loc_changed: 2500

policy:                              # §10.10
  require_linked_issue: true
  require_human_summary: true
  fail_on_risky_paths_without_context: true

risky_paths:                         # §10.6 — defaults already cover migrations,
  - "**/migrations/**"               #         auth, billing, payments, infra,
  - "infra/**"                       #         terraform, .github/workflows.
  - "src/payments/**"

labels:                              # §13.9 — applied by the hosted App
  pass: reviewability-pass
  warn: reviewability-warn
  fail: reviewability-fail

status_check:                        # §13.10
  name: reviewgate/reviewability
  fail_on: FAIL
```

Strict by design:

* Unknown top-level keys fail validation with the offending key name.
* A malformed file never crashes analysis (§12). The engine emits a
  `config_invalid` warning and runs against defaults so you don't get
  a green CI on a typo by accident.

---

## The deterministic engine

Implemented in [`src/reviewgate/core/`](src/reviewgate/core/). Every
module ties back to a §-numbered section of `docs/DESIGN.md`:

| Module | Purpose | Design § |
| ------ | ------- | -------- |
| [`engine.py`](src/reviewgate/core/engine.py) | Public entry point: `analyze(EngineInput) -> ReviewabilityReport` | §4.1, §10 |
| [`schemas.py`](src/reviewgate/core/schemas.py) | Strict Pydantic models for §10.1 input and §10.2 output | §10.1, §10.2 |
| [`config.py`](src/reviewgate/core/config.py) | `.reviewgate.yml` schema, defaults, malformed-config recovery | §12 |
| [`paths.py`](src/reviewgate/core/paths.py) | Pure gitignore-style glob matcher | §10.6–§10.9 |
| [`categorizer.py`](src/reviewgate/core/categorizer.py) | Per-file categorization across 16 closed labels | §10.5 |
| [`size.py`](src/reviewgate/core/size.py) | Raw LOC, ``human_loc_changed``, size warnings; [`automation_pr.py`](src/reviewgate/core/automation_pr.py) §10.4.1–§10.4.2 (``pr_author_kind``) | §10.3, §10.4 |
| [`ignored_paths.py`](src/reviewgate/core/ignored_paths.py) | Applies `ignored_paths` before categorisation | §12 |
| [`count_warnings.py`](src/reviewgate/core/count_warnings.py) | Warn-tier risky / dependency / config file counts | §10.3 |
| [`tests_coverage.py`](src/reviewgate/core/tests_coverage.py) | Source changes without test files (bounded heuristic) | §9, §13.9 |
| [`pr_body.py`](src/reviewgate/core/pr_body.py) | Weak-PR-body detection | §10.10 |
| [`linked_issue.py`](src/reviewgate/core/linked_issue.py) | Linked-issue / ticket reference detection | §10.10 |
| [`risky_paths.py`](src/reviewgate/core/risky_paths.py) | Risky-paths-without-rationale heuristic | §10.6, §10.10 |
| [`mixed_concern.py`](src/reviewgate/core/mixed_concern.py) | Mixed-concern category clusters | §10.11 |
| [`aggregate.py`](src/reviewgate/core/aggregate.py) | PASS / WARN / FAIL aggregation | §10.13 |
| [`report.py`](src/reviewgate/core/report.py) | Suggested-label assembly from warnings + config | §13.9, §12 |
| [`cli.py`](src/reviewgate/core/cli.py) | `reviewgate-core` console script for fixture-driven runs | §5.1, §25 M1 |

### Heuristics in one table

| Warning code | Severity | Trigger | Section |
| ------------ | -------- | ------- | ------- |
| `too_many_files_changed` | medium / high | `files_changed > thresholds.warn / fail.files_changed` | §10.3 |
| `too_large_human_loc` | medium / high | `human_loc_changed > thresholds.warn / fail.human_loc_changed` | §10.3 / §10.4 |
| `weak_pr_body` | medium | empty / whitespace / template-only / < 80 meaningful chars | §10.10 |
| `missing_linked_issue` | medium | no `#123`, `GH-123`, `fixes #…`, external tracker URL, or `ABC-123` | §10.10 |
| `risky_paths_without_rationale` | high | risky paths touched and PR body has no justification | §10.10 |
| `mixed_concerns` | medium | suspicious category cluster (billing + auth + infra, etc.) | §10.11 |
| `config_invalid` | low | `.reviewgate.yml` failed to parse; engine ran with defaults | §12 |

Verdict aggregation (§10.13):

```python
def baseline_reviewability(warnings):
    high = sum(1 for w in warnings if w.severity == "high")
    medium = sum(1 for w in warnings if w.severity == "medium")
    if high >= 2: return "FAIL"
    if high == 1 and medium >= 1: return "FAIL"
    if high == 1 or medium >= 2: return "WARN"
    return "PASS"
```

---

## GitHub Action

The Action wrapper in [`src/reviewgate_action/`](src/reviewgate_action/)
implements [`docs/DESIGN.md` §14](docs/DESIGN.md). The §14 reference
workflow:

```yaml
name: ReviewGate

on:
  pull_request:
    types: [opened, synchronize, edited, reopened]

jobs:
  reviewgate:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - uses: leo-aa88/reviewgate@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          fail-on: FAIL
          post-comment: true
          mode: action
```

| Input | Default | Purpose |
| ----- | ------- | ------- |
| `github-token` | — | Token to fetch PR data and (when allowed) post the §13 comment. `pull-requests: read` minimum, `write` for posting. |
| `fail-on` | `FAIL` | Verdict at or above which the workflow exits non-zero. One of `PASS`, `WARN`, `FAIL`, `never`. |
| `post-comment` | `"true"` | Whether to upsert the §13 marker comment when §14.1 coexistence allows. |
| `mode` | `auto` | §14.1 coexistence with the hosted App. `auto` defers to `.reviewgate.yml`; `action` forces the Action to post; `quiet` mutes it (logs only). |
| `python-version` | `3.12` | Pin handed to `actions/setup-python`. |
| `working-directory` | `$GITHUB_WORKSPACE` | Where to look up `.reviewgate.yml`. Override only for non-standard checkouts. |

| Output | Description |
| ------ | ----------- |
| `reviewability` | The §10.13 verdict (`PASS` / `WARN` / `FAIL`); empty when the run failed before producing a report. |
| `report-json` | The full §10.2 report as a single-line JSON document; **always valid JSON** (`{}` on failure). |

See [`src/reviewgate_action/README.md`](src/reviewgate_action/README.md) for
the full input/output reference and the §14.1 coexistence rules.

---

## CLI usage

The package installs a `reviewgate-core` console script (§5.1, §25 M1):

```bash
pip install reviewgate
reviewgate-core --input pr.json
cat pr.json | reviewgate-core
```

The CLI reads a §10.1 `EngineInput` JSON document from `--input` (or
stdin) and prints the §10.2 `ReviewabilityReport` to stdout. It is the
canonical local-fixture path; the GitHub Action and the hosted App
both call the same `analyze()` function.

Fourteen golden fixtures live under
[`tests/fixtures/m2_golden/`](tests/fixtures/m2_golden/) covering every
PR shape from §24.2:

```bash
reviewgate-core --input tests/fixtures/m2_golden/06_risky_migration_pr.json | jq .reviewability
# "FAIL"
```

---

## Onboarding

Already running ReviewGate or want the operator-facing setup walkthrough
(hosted App install, repo selection, `.reviewgate.yml`, §14.1
coexistence, required-status-check setup, LLM opt-in policy)? Read
[`docs/ONBOARDING.md`](docs/ONBOARDING.md). It is the discoverability
landing page for new beta teams.

For a hands-on five-minute tutorial that takes you from "clone the
repo" to "merging on a green ReviewGate verdict", read
[`docs/QUICKSTART.md`](docs/QUICKSTART.md).

---

## Docker image

The [`Dockerfile`](Dockerfile) packages the **hosted app** path: `reviewgate-api`
(FastAPI + uvicorn) and `reviewgate-worker` (Dramatiq), with optional extras from
`pyproject.toml`’s `[app]` group (PostgreSQL, Redis, Alembic, etc.). The
deterministic engine alone does not require this image; for local fixture runs
use `pip install reviewgate` / `reviewgate-core` as described in [CLI usage](#cli-usage).

**Build** (from the repository root):

```bash
docker build -t reviewgate:local .
```

Or: `make docker-build` (image name defaults to `reviewgate:local`; override with
`make docker-build IMAGE=myregistry/reviewgate:dev`).

**Run the HTTP API** on port 8000 (bind address is `0.0.0.0` inside the
container). Configure the process via `REVIEWGATE_*` environment variables
(see [`src/reviewgate/app/settings.py`](src/reviewgate/app/settings.py)).
Typical values for a real deployment include:

* `REVIEWGATE_DATABASE_URL` — PostgreSQL DSN for SQLAlchemy (same variable
  Alembic uses for migrations).
* `REVIEWGATE_REDIS_URL` — Redis for Dramatiq and related features.
* `REVIEWGATE_HTTP_PORT` — listening port (default `8000`; the image `EXPOSE`s
  8000).

Example (placeholders only):

```bash
docker run --rm -p 8000:8000 \
  -e REVIEWGATE_DATABASE_URL='postgresql+psycopg://user:pass@host:5432/db' \
  -e REVIEWGATE_REDIS_URL='redis://host:6379/0' \
  reviewgate:local
```

`make docker-run-api` runs the same shape but passes through `REVIEWGATE_DATABASE_URL`
and `REVIEWGATE_REDIS_URL` from your shell if they are already exported.

**Run the worker** by overriding the container command (the default `CMD` is
`reviewgate-api`):

```bash
docker run --rm \
  -e REVIEWGATE_REDIS_URL='redis://host:6379/0' \
  -e REVIEWGATE_DATABASE_URL='postgresql+psycopg://…' \
  reviewgate:local reviewgate-worker
```

Or: `make docker-run-worker` (expects those variables in your environment).

**Migrations** are not run automatically at container start. Apply them with
Alembic using the same `REVIEWGATE_DATABASE_URL`, for example from a one-off
container:

```bash
docker run --rm \
  -e REVIEWGATE_DATABASE_URL='postgresql+psycopg://…' \
  reviewgate:local python -m alembic upgrade head
```

The build context is trimmed by [`.dockerignore`](.dockerignore) (tests, docs,
virtualenvs, and caches are omitted). The image runs as a non-root `reviewgate`
user (UID 1000).

For a **copy-paste local stack** (venv, Postgres + Redis, env vars,
`alembic upgrade head`, `reviewgate-api` + `reviewgate-worker`, and a
`curl /health` check), use **[`docs/HOSTED_LOCAL.md`](docs/HOSTED_LOCAL.md)**.

---

## Makefile (local development)

The [`Makefile`](Makefile) documents itself: run **`make help`** (or plain
`make`) to list targets and short descriptions.

Common workflows:

| Target | Purpose |
| ------ | ------- |
| `make install-dev` | Editable install with `[dev,app]` extras (matches CI). |
| `make test` | Full `pytest` suite. |
| `make check` | Tests plus Ruff lint (`make install-dev` installs Ruff). |
| `make format` | Ruff format on `src/` and `tests/`. |
| `make docker-build` | Build the Docker image (`IMAGE=…` to tag). |
| `make alembic-upgrade` | `alembic upgrade head` (requires `REVIEWGATE_DATABASE_URL`). |

`make lock-uv` / `make sync-uv` are optional helpers for [uv](https://docs.astral.sh/uv/).
`uv.lock` is listed in [`.gitignore`](.gitignore) so local lockfiles do not
pollute the repository; generate one locally if you use uv.

---

## Project layout

```text
reviewgate/
├── action.yml                    # canonical public GitHub Action entry point
├── src/
│   ├── reviewgate/             # PyPI `reviewgate` top-level package
│   │   ├── __init__.py
│   │   └── core/               # `reviewgate.core` deterministic engine (§4.1)
│   │   ├── engine.py           # public analyze() entry point
│   │   ├── schemas.py          # §10.1 / §10.2 Pydantic models
│   │   ├── config.py           # §12 .reviewgate.yml schema
│   │   ├── categorizer.py      # §10.5 file categorization
│   │   ├── size.py             # §10.3 / §10.4 LOC stats
│   │   ├── pr_body.py          # §10.10 weak-body
│   │   ├── linked_issue.py     # §10.10 linked-issue
│   │   ├── risky_paths.py      # §10.10 risky-paths
│   │   ├── mixed_concern.py    # §10.11 mixed-concern
│   │   ├── aggregate.py        # §10.13 PASS/WARN/FAIL
│   │   ├── report.py           # §13.9 label assembly
│   │   ├── paths.py            # gitignore-style matcher
│   │   └── cli.py              # `reviewgate-core` console script
│   └── reviewgate_action/      # GitHub Action wrapper (§14)
│       ├── action.yml          # legacy alpha subdirectory action path
│       ├── README.md
│       └── reviewgate_action/  # Python package (import ``reviewgate_action``)
│           ├── fetch_pr.py     # PR + paginated files fetch
│           ├── run_core.py     # config + engine + fail-on + comment
│           ├── coexistence.py  # §14.1 mode resolver
│           └── post_comment.py # §13 marker-comment upsert
├── tests/                       # pytest suite; see CI matrix
│   ├── fixtures/m2_golden/     # 14 §24.2 golden PR fixtures
│   ├── test_core_purity.py     # §4.1 boundary enforcement (AST scan)
│   └── …
├── docs/
│   ├── DESIGN.md               # full product design
│   ├── ONBOARDING.md           # private-beta operator walkthrough
│   └── QUICKSTART.md           # 5-minute tutorial
├── .github/
│   ├── workflows/              # CI + dogfooding LLM PR review
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile                  # hosted app image (API + worker)
├── Makefile                    # local dev, tests, Docker, optional uv
├── .dockerignore
├── LICENSE                      # Apache 2.0
├── NOTICE
├── README.md
├── SECURITY.md
├── SUPPORT.md
└── pyproject.toml
```

---

## Status

* **`reviewgate-core` (deterministic engine):** runtime complete.
  All §10 heuristics from `docs/DESIGN.md` are implemented and
  covered by the pytest suite on Python 3.12 and 3.13 (see CI matrix).
* **`reviewgate-action` (GitHub Action):** runtime complete (issues
  #24, #25, #26 landed). Fetches PR metadata, loads `.reviewgate.yml`,
  runs the engine, applies the §14 `fail-on` policy, and (when §14.1
  coexistence allows) upserts the §13 PR comment.
* **Hosted ReviewGate App:** shipped in this tree under
  [`src/reviewgate/app/`](src/reviewgate/app/) and installed with the
  optional `app` extra (`pip install "reviewgate[app]"`). It includes
  the FastAPI surface, webhook receiver, worker, persistence, GitHub
  outputs, and hosted-only LLM report path. Paid ReviewGate Cloud (if
  offered) is a **hosting and operations** layer on top of this code,
  not a closed-source fork. See [`docs/DESIGN.md` §19](docs/DESIGN.md).
* **Public release:** this repository is being prepared for public
  open-source release under Apache 2.0. Until the first signed
  release tag, treat the public API as stable but additive.

---

## Roadmap

The MVP implementation is in beta hardening: core, Action, hosted App,
and hosted LLM paths are in-tree, while public release still depends on
operational beta evidence and a signed release tag. Near-term priorities:

* First public release (`v0.1.0`) on PyPI and GitHub Releases, then
  update Action snippets from `@main` to the signed release tag.
* `pre-commit` hook configuration so the engine can run locally on
  staged changes.
* Optional Action input for status-check name customisation (so a
  team can publish multiple ReviewGate checks side by side).
* Additional heuristics driven by beta feedback (test-coverage delta,
  formatting-only churn detection, dependency-update + behavior-change
  separation per §10.11 examples).

The remaining non-MVP item is the **public PR URL analyzer** (see
[`docs/DESIGN.md` §4.4](docs/DESIGN.md) and
[§28 Future Public PR Analyzer](docs/DESIGN.md)). Hosted App and hosted
LLM implementation live in this repository.

---

## Contributing

Contributions are welcome. Before opening a PR:

1. Project norms and maintainer expectations are summarized in
   [`GOVERNANCE.md`](GOVERNANCE.md). Dependency updates are automated via
   Dependabot — see [`.github/dependabot.yml`](.github/dependabot.yml).
2. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) — the §4.1 purity
   boundary is enforced in CI; any new dependency on a forbidden
   module (network, DB, LLM, GitHub SDK, `subprocess`, …) will fail
   the build.
3. Anchor your change to a §-numbered section of
   [`docs/DESIGN.md`](docs/DESIGN.md) or to an existing issue.
4. Add at least one fixture under
   [`tests/fixtures/m2_golden/`](tests/fixtures/m2_golden/) when you
   add a new heuristic, or a unit test next to an existing one.
5. Run the full suite locally (`pytest`) on Python 3.12+.
6. Follow [Conventional Commits](https://www.conventionalcommits.org)
   for the commit message; PR titles are merged verbatim.

This project follows the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md).
By participating you agree to abide by its terms.

### Testing

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,app]"
pytest
```

Equivalent shortcuts: `make venv` then activate, `make install-dev`, and
`make test`. See [Makefile (local development)](#makefile-local-development).

CI runs ``pytest`` on Python **3.12** and **3.13**, Ruff lint checks,
Alembic upgrade/downgrade smoke tests, and package build verification (see
the matrix in [`.github/workflows/ci.yml`](.github/workflows/ci.yml)). This repo
also includes
[`pr-llm-review.yml`](https://github.com/leo-aa88/reviewgate/blob/main/.github/workflows/pr-llm-review.yml),
which can post an LLM-backed PR review when secrets are configured (see the workflow file; fork PRs are skipped).

---

## Security

To report a security vulnerability, please follow [`SECURITY.md`](SECURITY.md).
**Do not open a public issue** for vulnerabilities — use GitHub's
private vulnerability reporting flow or email the maintainer.

---

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
See [`NOTICE`](NOTICE) for required attributions and third-party
dependency licenses. The full `docs/DESIGN.md` and supporting
documentation are also covered by this license.

```text
Copyright 2025 Leonardo Araujo and ReviewGate contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
```

---

## Acknowledgements

ReviewGate stands on the shoulders of:

* [`pydantic`](https://github.com/pydantic/pydantic) — strict schema
  validation for the §10 engine contract.
* [`PyYAML`](https://pyyaml.org) — `.reviewgate.yml` parsing.
* [`pathspec`](https://github.com/cpburnz/python-pathspec) — pure
  gitignore-style glob matching for the §10.6–§10.9 path patterns.
* [Conventional Commits](https://www.conventionalcommits.org) and
  [Keep a Changelog](https://keepachangelog.com) for project hygiene.

The product thesis owes a lot to every senior engineer who has ever
clicked **Approve** on a PR they were too tired to actually review.


---

## 44. narwhals
- **URL:** https://github.com/devtechedge/narwhals
- **Language:** Python
- **Topics:** None
- **Description:** Lightweight and extensible compatibility layer between dataframe libraries!

### README.md

# Narwhals

<h1 align="center">
	<img
		width="400"
		alt="narwhals_small"
		src="https://github.com/user-attachments/assets/968545af-ea0f-48bb-8377-144e93f7abf8">
</h1>

[![PyPI version](https://badge.fury.io/py/narwhals.svg)](https://badge.fury.io/py/narwhals)
[![Downloads](https://static.pepy.tech/badge/narwhals/month)](https://pepy.tech/project/narwhals)
[![Trusted publishing](https://img.shields.io/badge/Trusted_publishing-Provides_attestations-bright_green)](https://peps.python.org/pep-0740/)
[![PYPI - Types](https://img.shields.io/pypi/types/narwhals)](https://pypi.org/project/narwhals)
[![LFX Health Score](https://insights.linuxfoundation.org/api/badge/health-score?project=narwhals-dev-narwhals)](https://insights.linuxfoundation.org/project/narwhals-dev-narwhals)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/narwhals-dev/narwhals/badge)](https://securityscorecards.dev/viewer/?uri=github.com/narwhals-dev/narwhals)

Extremely lightweight and extensible compatibility layer between dataframe libraries!

- **Full API support**: cuDF, Modin, pandas, Polars, PyArrow.
- **Lazy-only support**: Dask, DuckDB, Ibis, PySpark, SQLFrame, Daft via the
  [narwhals-daft](https://github.com/narwhals-dev/narwhals-daft) plugin, and Apache DataFusion via the
  [narwhals-datafusion](https://github.com/s5dsn-eqee/narwhals-datafusion) plugin.

Seamlessly support all, without depending on any!

- ✅ **Just use** [a subset of **the Polars API**](https://narwhals-dev.github.io/narwhals/api-reference/), no need to learn anything new
- ✅ **Zero dependencies**, Narwhals only uses what
  the user passes in so your library can stay lightweight
- ✅ Separate **lazy** and eager APIs, use **expressions**
- ✅ Support pandas' complicated type system and index, without
  either getting in the way
- ✅ **100% branch coverage**, tested against pandas and Polars nightly builds
- ✅ **Negligible overhead**, see [overhead](https://narwhals-dev.github.io/narwhals/overhead/)
- ✅ Let your IDE help you thanks to **full static typing**, see [typing](https://narwhals-dev.github.io/narwhals/api-reference/typing/)
- ✅ **Perfect backwards compatibility policy**,
  see [stable api](https://narwhals-dev.github.io/narwhals/backcompat/) for how to opt-in

Get started!

- [Read the documentation](https://narwhals-dev.github.io/narwhals/)
- [Chat with us on Discord!](https://discord.gg/V3PqtB4VA4)
- [Join our community call](https://calendar.google.com/calendar/embed?src=27ff6dc5f598c1d94c1f6e627a1aaae680e2fac88f848bda1f2c7946ae74d5ab%40group.calendar.google.com)
- [Read the contributing guide](https://github.com/narwhals-dev/narwhals/blob/main/CONTRIBUTING.md)

<details>
<summary>Table of contents</summary>

- [Narwhals](#narwhals)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
  - [Scope](#scope)
  - [Roadmap](#roadmap)
  - [Used by](#used-by)
  - [Sponsors and institutional partners](#sponsors-and-institutional-partners)
  - [Support](#support)
  - [Appears on](#appears-on)
  - [Why "Narwhals"?](#why-narwhals)

</details>

## Installation

- pip (recommended, as it's the most up-to-date)
  ```
  pip install narwhals
  ```
- conda-forge (also fine, but the latest version may take longer to appear)
  ```
  conda install -c conda-forge narwhals
  ```

## Usage

There are three steps to writing dataframe-agnostic code using Narwhals:

1. use `narwhals.from_native` to wrap a pandas/Polars/Modin/cuDF/PyArrow
   DataFrame/LazyFrame in a Narwhals class
2. use the [subset of the Polars API supported by Narwhals](https://narwhals-dev.github.io/narwhals/api-reference/)
3. use `narwhals.to_native` to return an object to the user in its original
   dataframe flavour. For example:

   - if you started with pandas, you'll get pandas back
   - if you started with Polars, you'll get Polars back
   - if you started with Modin, you'll get Modin back (and compute will be distributed)
   - if you started with cuDF, you'll get cuDF back (and compute will happen on GPU)
   - if you started with PyArrow, you'll get PyArrow back

<h1 align="left">
	<img
		width="600"
		alt="narwhals_gif"
		src="https://github.com/user-attachments/assets/88292d3c-6359-4155-973d-d0f8e3fbf5ac">

</h1>

## Example

Narwhals allows you to define dataframe-agnostic functions. For example:

```python
import narwhals as nw
from narwhals.typing import IntoFrameT


def agnostic_function(df_native: IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df_native)
        .with_columns(
            category=nw.when(nw.col("animal").str.contains("whale"))
            .then(nw.lit("whale"))
            .otherwise(nw.lit("other"))
        )
        .to_native()
    )
```

You can then pass `pandas.DataFrame`, `polars.DataFrame`, `polars.LazyFrame`, `duckdb.DuckDBPyRelation`,
`pyspark.sql.DataFrame`, `pyarrow.Table`, and more, to `agnostic_function`. In each case, no additional
dependencies will be required, and computation will stay native to the input library:

```python
import duckdb
import polars as pl
import pandas as pd

data = {
    "animal": ["blue whale", "orca", "dolphin", "humpback whale", "seal"],
    "length_m": [30.0, 8, 2.5, 17, 2.2],
    "weight_kg": [150000, 4000, 200, 30000, 85],
}

print("Polars result")
df_pl = pl.DataFrame(data)
print(agnostic_function(df_pl))

print("DuckDB result")
print(agnostic_function(duckdb.sql("select * from df_pl")))

print("pandas result")
df_pd = pd.DataFrame(data)
print(agnostic_function(df_pd))
```

```terminal
Polars result
shape: (5, 4)
┌────────────────┬──────────┬───────────┬──────────┐
│ animal         ┆ length_m ┆ weight_kg ┆ category │
│ ---            ┆ ---      ┆ ---       ┆ ---      │
│ str            ┆ f64      ┆ i64       ┆ str      │
╞════════════════╪══════════╪═══════════╪══════════╡
│ blue whale     ┆ 30.0     ┆ 150000    ┆ whale    │
│ orca           ┆ 8.0      ┆ 4000      ┆ other    │
│ dolphin        ┆ 2.5      ┆ 200       ┆ other    │
│ humpback whale ┆ 17.0     ┆ 30000     ┆ whale    │
│ seal           ┆ 2.2      ┆ 85        ┆ other    │
└────────────────┴──────────┴───────────┴──────────┘
DuckDB result
┌────────────────┬──────────┬───────────┬──────────┐
│     animal     │ length_m │ weight_kg │ category │
│    varchar     │  double  │   int64   │ varchar  │
├────────────────┼──────────┼───────────┼──────────┤
│ blue whale     │     30.0 │    150000 │ whale    │
│ orca           │      8.0 │      4000 │ other    │
│ dolphin        │      2.5 │       200 │ other    │
│ humpback whale │     17.0 │     30000 │ whale    │
│ seal           │      2.2 │        85 │ other    │
└────────────────┴──────────┴───────────┴──────────┘

pandas result
           animal  length_m  weight_kg category
0      blue whale      30.0     150000    whale
1            orca       8.0       4000    other
2         dolphin       2.5        200    other
3  humpback whale      17.0      30000    whale
4            seal       2.2         85    other
```

See the [tutorial](https://narwhals-dev.github.io/narwhals/basics/dataframe/) for several examples!

## Scope

- Do you maintain a dataframe-consuming library?
- Do you have a specific Polars function in mind that you would like Narwhals to have in order to make your work easier?

If you said yes to both, we'd love to hear from you!

## Roadmap

See [roadmap discussion on GitHub](https://github.com/narwhals-dev/narwhals/discussions/1370)
for an up-to-date plan of future work.

## Used by

Join the party!

- [altair](https://github.com/vega/altair/)
- [bokeh](https://github.com/bokeh/bokeh)
- [darts](https://github.com/unit8co/darts)
- [fairlearn](https://github.com/fairlearn/fairlearn)
- [formulaic](https://github.com/matthewwardrop/formulaic)
- [gt-extras](https://github.com/posit-dev/gt-extras)
- [hierarchicalforecast](https://github.com/Nixtla/hierarchicalforecast)
- [lightgbm](https://github.com/lightgbm-org/LightGBM)
- [marimo](https://github.com/marimo-team/marimo)
- [metalearners](https://github.com/Quantco/metalearners)
- [mosaic](https://github.com/uwdata/mosaic)
- [pandera](https://github.com/pandera-dev/pandera)
- [panel-graphic-walker](https://github.com/panel-extensions/panel-graphic-walker)
- [plotly](https://plotly.com)
- [pointblank](https://github.com/posit-dev/pointblank)
- [pymarginaleffects](https://github.com/vincentarelbundock/pymarginaleffects)
- [pyreadstat](https://github.com/Roche/pyreadstat)
- [py-shiny](https://github.com/posit-dev/py-shiny)
- [pysummaries](https://github.com/Genentech/pysummaries)
- [rio](https://github.com/rio-labs/rio)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [scikit-lego](https://github.com/koaning/scikit-lego)
- [scikit-playtime](https://github.com/koaning/scikit-playtime)
- [tabmat](https://github.com/Quantco/tabmat)
- [tea-tasting](https://github.com/e10v/tea-tasting)
- [timebasedcv](https://github.com/FBruzzesi/timebasedcv)
- [tubular](https://github.com/lvgig/tubular)
- [Validoopsie](https://github.com/akmalsoliev/Validoopsie)
- [vegafusion](https://github.com/vega/vegafusion)
- [wimsey](https://github.com/benrutter/wimsey)

Feel free to add your project to the list if it's missing, and/or
[chat with us on Discord](https://discord.gg/V3PqtB4VA4) if you'd like any support.

## Sponsors and institutional partners

Narwhals is 100% independent, community-driven, and community-owned.
We are extremely grateful to the following organisations for having
provided some funding / development time:

- [Quansight Labs](https://labs.quansight.org)
- [Quansight Futures](https://www.qi.ventures)
- [OpenTeams](https://www.openteams.com)
- [POSSEE initiative](https://possee.org)
- [BYU-Idaho](https://www.byui.edu)
- [Intella](https://www.intella.tech/)

If you contribute to Narwhals on your organization's time, please let us know. We'd be happy to add your employer
to this list!

## Support

If you'd like to say "thank you", please give us a ⭐ star ⭐.

Please contact [hello_narwhals@proton.me](mailto:hello_narwhals@proton.me) if you would like to:

- Receive professional support (e.g., if you're using or would like to use Narwhals at your company).
- Have any Narwhals fixes / features prioritised.
- Commission any Narwhals plugins for new backends.

## Appears on

Narwhals has been featured in several talks, podcasts, and blog posts:

- [Inspiring Computing Podcast](https://www.inspiringcomputing.com/2107763/episodes/16702460-the-rise-of-narwhals-in-open-source)
  The Rise of Narwhals in Open-Source

- [PyCon DE & PyData 2025](https://youtu.be/DJk782DWcss)
  How Narwhals is silently bringing pandas, Polars, DuckDB, PyArrow, and more together

- [The Python Exchange March 2025](https://youtu.be/TvFWFlK-2po)
  What Can Narwhals Do for You?

- [PyData London 2025](https://youtu.be/r2PxJlO7_QA)
  How Narwhals brings Polars, DuckDB, PyArrow, & pandas together

- [Talk Python to me Podcast](https://youtu.be/FSH7BZ0tuE0)
  Ahoy, Narwhals are bridging the data science APIs

- [Python Bytes Podcast](https://www.youtube.com/live/N7w_ESVW40I?si=y-wN1uCsAuJOKlOT&t=382)
  Episode 402, topic #2

- [Super Data Science: ML & AI Podcast](https://www.youtube.com/watch?v=TeG4U8R0U8U)
  Narwhals: For Pandas-to-Polars DataFrame Compatibility

- [Sample Space Podcast | probabl](https://youtu.be/8hYdq4sWbbQ?si=WG0QP1CZ6gkFf18b)
  How Narwhals has many end users ... that never use it directly. - Marco Gorelli

- [The Real Python Podcast](https://www.youtube.com/watch?v=w5DFZbFYzCM)
  Narwhals: Expanding DataFrame Compatibility Between Libraries

- [Pycon Lithuania 2024](https://www.youtube.com/watch?v=-mdx7Cn6_6E)
  Marco Gorelli - DataFrame interoperatiblity - what's been achieved, and what comes next?

- [Pycon Italy 2024](https://www.youtube.com/watch?v=3IqUli9XsmQ)
  How you can write a dataframe-agnostic library - Marco Gorelli

- [Polars Blog Post](https://pola.rs/posts/lightweight_plotting/)
  Polars has a new lightweight plotting backend

- [Quansight Labs blog post (w/ Scikit-Lego)](https://labs.quansight.org/blog/scikit-lego-narwhals)
  How Narwhals and scikit-lego came together to achieve dataframe-agnosticism

## Why "Narwhals"?

[Coz they are so awesome](https://youtu.be/ykwqXuMPsoc?si=A-i8LdR38teYsos4).

Thanks to [Olha Urdeichuk](https://www.fiverr.com/olhaurdeichuk) for the illustration!


---

## 45. HackRPI-Website-2026
- **URL:** https://github.com/devtechedge/HackRPI-Website-2026
- **Language:** TypeScript
- **Topics:** None
- **Description:** No description

### README.md

# HackRPI 2026 Website

https://hackrpi.com/

The Official Website for HackRPI 2026!

## Tech Stack

Languages used:
* [Next.js](https://nextjs.org/)
* [React](https://react.dev/)
* [TailwindCSS](https://tailwindcss.com/)
* [TypeScript](https://www.typescriptlang.org/)

External packages used:
* [Daisy UI](https://daisyui.com/)
* [Lenis](https://lenis.darkroom.engineering/)
* [GreenSock Animation Platform](https://gsap.com/)
* [Three.js](https://threejs.org/)

## Instructions for Development

1.  Install the dependencies with npm

        npm i

2.  Run the development server with npm

        npm run dev

## Contributions

We are always looking for contributions! If you're wondering where to start, check out our issues pages for work that still needs to be done.

Before contributing please take a look at our [contributing guidelines](./CONTRIBUTING.md). Thank you!

---

## 46. signalpost-citation-validator
- **URL:** https://github.com/devtechedge/signalpost-citation-validator
- **Language:** Python
- **Topics:** None
- **Description:** Public offline validator for Signalpost evidence references

### README.md

# Signalpost citation validator

An offline tool project that helps builders catch broken evidence references before submitting to the [Signalpost challenge](https://builderr.ai/challenges/signalpost?utm_source=github&utm_medium=open_contribution&utm_campaign=signalpost_citation_validator).

The first contribution is a citation validator. It checks whether a claim points to a captured source file and whether the file matches its recorded SHA-256 digest. It does **not** decide whether the claim is true, whether the source belongs to the correct company, whether collecting the source was permitted, or how a competition entry should score.

This is a small public contribution project from [Builderr](https://builderr.ai/?utm_source=github&utm_medium=open_contribution&utm_campaign=signalpost_citation_validator&utm_content=readme_about), where companies pay for verified outcomes and builders compete with working solutions.

## Why this is public

The checks in this repository are safe to share with every builder. They use synthetic fixtures and contain no participant submission, private company record, credential, hidden evaluation case or competition answer.

Public acceptance tests help contributors understand exactly what a small tool must do. Passing them does not reveal or replace Builderr's independent assessment.

## First contribution

Read [the citation-validator issue](docs/citation-validator-issue.md). The task is deliberately narrow: Python 3.11, offline, deterministic output and standard-library-only unless a dependency is approved first.

The supplied fixture pack lives in `fixtures/`. Run its black-box verifier like this after implementing the CLI:

```sh
python3 verify_acceptance.py -- python3 -m signalpost_citation_validator
```

A contributor will add the validator implementation and focused tests in a pull request.

## Licence

Code and documentation in this repository are available under the [MIT License](LICENSE). Contributors retain copyright in their work and license submitted contributions under the same terms. No copyright assignment or CLA is required.

Contributing does not affect Signalpost judging, prizes or leaderboard position. There is no cash bounty for the first pilot.


---

## 47. trash-cli
- **URL:** https://github.com/devtechedge/trash-cli
- **Language:** Python
- **Topics:** None
- **Description:** Command line interface to the freedesktop.org trashcan.

### README.md

trash-cli - Command Line Interface to FreeDesktop.org Trash
============================================================

|Downloads|

|Donate|_

`简体中文`_

trash-cli trashes files recording the original path, deletion date, and 
permissions. It uses the same trashcan used by KDE, GNOME, and XFCE, but you 
can invoke it from the command line (and scripts).

It provides these commands::

    trash-put           trash files and directories. 
    trash-empty         empty the trashcan(s).
    trash-list          list trashed files.
    trash-restore       restore a trashed file.
    trash-rm            remove individual files from the trashcan.

Usage
-----

Trash a file::

    $ trash-put foo

List trashed files::

    $ trash-list
    2008-06-01 10:30:48 /home/andrea/bar
    2008-06-02 21:50:41 /home/andrea/bar
    2008-06-23 21:50:49 /home/andrea/foo

Search for a file in the trashcan::

    $ trash-list | grep foo
    2007-08-30 12:36:00 /home/andrea/foo
    2007-08-30 12:39:41 /home/andrea/foo

Restore a trashed file::
    
    $ trash-restore
    0 2007-08-30 12:36:00 /home/andrea/foo
    1 2007-08-30 12:39:41 /home/andrea/bar
    2 2007-08-30 12:39:41 /home/andrea/bar2
    3 2007-08-30 12:39:41 /home/andrea/foo2
    4 2007-08-30 12:39:41 /home/andrea/foo
    What file to restore [0..4]: 4
    $ ls foo
    foo
    
Restore a trashed file while overwriting existing files::
    
    $ echo "original">foo
    $ ls
    foo
    $ trash-put foo
    $ echo "new">foo
    $ trash-restore --overwrite
    0 2022-11-01 22:15:00 /home/andrea/foo
    What file to restore [0..0]: 0
    $ cat foo
    original

Restore multiple trashed files separated by ',', also support range::

    $ trash-restore
    0 2007-08-30 12:36:00 /home/andrea/foo
    1 2007-08-30 12:39:41 /home/andrea/bar
    2 2007-08-30 12:39:41 /home/andrea/bar2
    3 2007-08-30 12:39:41 /home/andrea/foo2
    What file to restore [0..3]: 0-2, 3
    $ ls foo bar bar2 foo2
    foo bar bar2 foo2

Remove all files from the trashcan::

    $ trash-empty

Remove only the files that have been deleted more than <days> ago::
    
    $ trash-empty <days>

Example::

    $ date
    Tue Feb 19 20:26:52 CET 2008
    $ trash-list
    2008-02-19 20:11:34 /home/einar/today
    2008-02-18 20:11:34 /home/einar/yesterday
    2008-02-10 20:11:34 /home/einar/last_week
    $ trash-empty 7
    $ trash-list
    2008-02-19 20:11:34 /home/einar/today
    2008-02-18 20:11:34 /home/einar/yesterday
    $ trash-empty 1
    $ trash-list
    2008-02-19 20:11:34 /home/einar/today

Remove only files matching a pattern::

    $ trash-rm \*.o

Note: you need to use quotes in order to protect the pattern from shell expansion.

FAQ
---

How to create a top level .Trash dir?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Steps ::

    sudo mkdir --parent /.Trash
    sudo chmod a+rw /.Trash
    sudo chmod +t /.Trash

Can I alias `rm` to `trash-put`?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can but you shouldn't. In the early days I thought it was a good idea to do
that but now I changed my mind. 

Although the interface of `trash-put` seems to be compatible with `rm`, it has
different semantics which will cause you problems. For example, while `rm`
requires `-R` for deleting directories `trash-put` does not.

But sometimes I forget to use `trash-put`, really can't I?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You could alias `rm` to something that will remind you to not use it::

    alias rm='echo "This is not the command you are looking for."; false'

Then, if you really want to use `rm`, simply prepend a backslash to bypass the
alias::

    \rm file-without-hope

Note that Bash aliases are used only in interactive shells, so using 
this alias should not interfere with scripts that expect to use `rm`.

Where do the trashed files go?
~~~~~~~~~~~~~~~~~~~~~~~~~~~
File trashed from the home partition will be moved here::

    ~/.local/share/Trash/

How to auto delete files older than 30 days?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run this::

    (crontab -l ; echo "@daily $(which trash-empty) 30") | crontab -

This will update your crontab file with a `trash-empty` command that runs daily
and removes files older than 30 days. To review your crontab use: `crontab -l`

Installation
------------

The easy way
~~~~~~~~~~~~

Requirements:
 * Python 3 (Python 2.7 also works)
 * pipx_ (optional, to install in a clean environment)

If pipx is available::

    pipx install trash-cli

Alternatively, install with vanilla pip::

    pip install trash-cli

Note: you may want to add ~/.local/bin to the PATH::

    echo 'export PATH="$PATH":~/.local/bin' >> ~/.bashrc
    source ~/.bashrc # reload .bashrc

For uninstalling use::

    pipx uninstall trash-cli

or::

    pip uninstall trash-cli

Bleeding Edge (from sources)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all you need to uninstall any previous version of trash-cli::

    $ [sudo] pip uninstall trash-cli # remove the previous version (with pip)
    $ [sudo] apt-get remove trash-cli # remove the previous version (with apt)
    $ [sudo] yum uninstall trash-cli # remove the previous version (with yum)
    $ ... # refer to the package manager of your distribution

Then install the latest version from git::

    $ [sudo] pip install git+https://github.com/andreafrancia/trash-cli

After the user installation you may want to add this line to your .bashrc/.zshrc::

    export PATH=~/.local/bin:"$PATH"

From package manager
~~~~~~~~~~~~~~~~~~~~

Debian/Ubuntu (apt)::

    sudo apt install trash-cli

Arch Linux (pacman)::

    sudo pacman -S trash-cli

Fedora (dnf)::

    sudo dnf install trash-cli

MacOS (Homebrew)::

    brew install trash-cli
    echo 'export PATH="~/homebrew/opt/trash-cli/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc

Install shell completions
~~~~~~~~~~~~~~~~~~~~~~~~~

You need to install by::

    pipx install 'trash-cli[completion]'

or::

    pip install 'trash-cli[completion]'

Then::

    cmds=(trash-empty trash-list trash-restore trash-put trash)
    for cmd in ${cmds[@]}; do
      $cmd --print-completion bash | sudo tee /usr/share/bash-completion/completions/$cmd
      $cmd --print-completion zsh | sudo tee /usr/share/zsh/site-functions/_$cmd
      $cmd --print-completion tcsh | sudo tee /etc/profile.d/$cmd.completion.csh
    done

Missing support for Btrfs volumes
---------------------------------
trash-cli does not support Btrfs volumes.
I don't have any system nor time and/or knowledge to implement this kind of support.

If you need a trash implementation, you can check out the `rmw`_ project.

.. _rmw: https://github.com/theimpossibleastronaut/rmw

If you want to, and can, and know how to add support for Btrfs with sensible automation tests, please send a pull request.

Bugs
----

If you discover a bug please report it here:

    https://github.com/andreafrancia/trash-cli/issues

Feedback
--------

You can send me an email using andrea@andreafrancia.it.

Development
-----------

Environment setup::

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt -r requirements.txt

Running tests::

    pytest -m 'not slow'        # run only fast tests
    pytest -m 'slow'            # run slow tests
    pytest                      # run all tests

Thanks
------
Thanks to Paypal donors.

Thanks to `project contributors`_.

Thanks to `JetBrains`_ for their license for Open Source Development

.. |Downloads| image:: https://img.shields.io/pypi/dm/trash-cli
.. |Donate| image:: https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif
.. _Donate: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=93L6PYT4WBN5A
.. _简体中文: https://github.com/andreafrancia/trash-cli/blob/master/README_zh-CN.rst
.. _project contributors: https://github.com/andreafrancia/trash-cli/graphs/contributors
.. _JetBrains: https://jb.gg/OpenSource
.. _pipx: https://pypa.github.io/pipx/


---

## 48. wxt
- **URL:** https://github.com/devtechedge/wxt
- **Language:** TypeScript
- **Topics:** None
- **Description:** ΓÜí Next-gen Web Extension Framework

### README.md

<div align="center">

# <img align="top" width="44" src="https://raw.githubusercontent.com/wxt-dev/wxt/HEAD/docs/public/hero-logo.svg" alt="WXT Logo"> WXT

[![npm version](https://img.shields.io/npm/v/wxt?labelColor=black&color=%234fa048)](https://www.npmjs.com/package/wxt)
[![downloads](https://img.shields.io/npm/dm/wxt?labelColor=black&color=%234fa048)](https://www.npmjs.com/package/wxt)
[![license | MIT](https://img.shields.io/npm/l/wxt?labelColor=black&color=%234fa048)](https://github.com/wxt-dev/wxt/blob/main/LICENSE)
[![coverage](https://img.shields.io/codecov/c/github/wxt-dev/wxt?labelColor=black&color=%234fa048)](https://codecov.io/github/wxt-dev/wxt)

Next-gen framework for developing web extensions.<br/>⚡<br/><q><i>It's like Nuxt, but for Web Extensions</i></q>

[Get Started](https://wxt.dev/guide/installation.html) •
[Configuration](https://wxt.dev/api/config.html) •
[Examples](https://wxt.dev/examples.html) •
[Changelog](https://github.com/wxt-dev/wxt/blob/main/packages/wxt/CHANGELOG.md) •
[Discord](https://discord.gg/ZFsZqGery9)

</div>

![Example CLI Output](https://raw.githubusercontent.com/wxt-dev/wxt/HEAD/docs/assets/cli-output.png)

## Demo

<https://github.com/wxt-dev/wxt/assets/10101283/4d678939-1bdb-495c-9c36-3aa281d84c94>

## Quick Start

Bootstrap a new project:

```sh
# npm
npx wxt@latest init

# pnpm
pnpm dlx wxt@latest init

# bun
bunx wxt@latest init
```

Or see the [installation guide](https://wxt.dev/guide/installation.html) to get started with WXT.

## Features

- 🌐 Supports all browsers
- ✅ Supports both MV2 and MV3
- ⚡ Dev mode with HMR & fast reload
- 📂 File based entrypoints
- 🚔 TypeScript
- 🦾 Auto-imports
- 🤖 Automated publishing
- 🎨 Frontend framework agnostic: works with Vue, React, Svelte, etc
- 📦 [Module system](https://wxt.dev/guide/essentials/wxt-modules.html#overview) for reusing code between extensions
- 🖍️ Quickly bootstrap a new project
- 📏 Bundle analysis

## Sponsors

WXT is a [MIT-licensed](https://github.com/wxt-dev/wxt/blob/main/LICENSE) open source project with its ongoing development made possible entirely by the support of these awesome backers. If you'd like to join them, please consider [sponsoring WXT's development](https://github.com/sponsors/wxt-dev).

[![WXT Sponsors](https://raw.githubusercontent.com/wxt-dev/static/refs/heads/main/sponsorkit/sponsors.svg)](https://github.com/sponsors/wxt-dev)

## Contributors

Published under the [MIT](https://github.com/wxt-dev/wxt/blob/main/LICENSE) license.
Made by [@aklinker1](https://github.com/aklinker1) and [community](https://github.com/wxt-dev/wxt/graphs/contributors) 💛

[![WXT contributors](https://contrib.rocks/image?repo=wxt-dev/wxt)](https://github.com/wxt-dev/wxt/graphs/contributors)


---

## 49. git-js
- **URL:** https://github.com/devtechedge/git-js
- **Language:** TypeScript
- **Topics:** None
- **Description:** A light weight interface for running git commands in any node.js application.

### README.md

# Simple Git

[![NPM version](https://img.shields.io/npm/v/simple-git.svg)](https://www.npmjs.com/package/simple-git)

A lightweight interface for running `git` commands in any [node.js](https://nodejs.org) application.

# Installation

Use your favourite package manager:

-  [npm](https://npmjs.org): `npm install simple-git`
-  [yarn](https://yarnpkg.com/): `yarn add simple-git`

# System Dependencies

Requires [git](https://git-scm.com/downloads) to be installed and that it can be called using the command `git`.

# Usage

Include into your JavaScript app using common js:

```javascript
// require the library, main export is a function
const simpleGit = require('simple-git');
simpleGit().clean(simpleGit.CleanOptions.FORCE);

// or use named properties
const { simpleGit, CleanOptions } = require('simple-git');
simpleGit().clean(CleanOptions.FORCE);
```

Include into your JavaScript app as an ES Module:

```javascript
import { simpleGit, CleanOptions } from 'simple-git';

simpleGit().clean(CleanOptions.FORCE);
```

Include in a TypeScript app using the bundled type definitions:

```typescript
import { simpleGit, SimpleGit, CleanOptions } from 'simple-git';

const git: SimpleGit = simpleGit().clean(CleanOptions.FORCE);
```

## Configuration

Configure each `simple-git` instance with a properties object passed to the main `simpleGit` function:

```typescript
import { simpleGit, SimpleGit, SimpleGitOptions } from 'simple-git';

const options: Partial<SimpleGitOptions> = {
   baseDir: process.cwd(),
   binary: 'git',
   maxConcurrentProcesses: 6,
   trimmed: false,
};

// when setting all options in a single object
const git: SimpleGit = simpleGit(options);

// or split out the baseDir, supported for backward compatibility
const git: SimpleGit = simpleGit('/some/path', { binary: 'git' });
```

The first argument can be either a string (representing the working directory for `git` commands to run in),
`SimpleGitOptions` object or `undefined`, the second parameter is an optional `SimpleGitOptions` object.

All configuration properties are optional, the default values are shown in the example above.

## Per-command Configuration

To prefix the commands run by `simple-git` with custom configuration not saved in the git config (ie: using the
`-c` command) supply a `config` option to the instance builder:

```typescript
// configure the instance with a custom configuration property
const git: SimpleGit = simpleGit('/some/path', { config: ['http.proxy=someproxy'] });

// any command executed will be prefixed with this config
// runs: git -c http.proxy=someproxy pull
await git.pull();
```

## Configuring Plugins

- [AbortController](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-ABORT-CONTROLLER.md)
   Terminate pending and future tasks in a `simple-git` instance (requires node >= 16).

- [Custom Binary](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-CUSTOM-BINARY.md)
   Customise the `git` binary `simple-git` uses when spawning `git` child processes. 

- [Completion Detection](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-COMPLETION-DETECTION.md)
   Customise how `simple-git` detects the end of a `git` process.

- [Error Detection](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-ERRORS.md)
   Customise the detection of errors from the underlying `git` process.

- [Progress Events](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-PROGRESS-EVENTS.md)
   Receive progress events as `git` works through long-running processes.

- [Spawned Process Ownership](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-SPAWN-OPTIONS.md)
   Configure the system `uid` / `gid` to use for spawned `git` processes.

- [Timeout](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-TIMEOUT.md)
   Automatically kill the wrapped `git` process after a rolling timeout.

- [Unsafe](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-UNSAFE-ACTIONS.md)
   Selectively opt out of `simple-git` safety precautions - for advanced users and use cases.

## Using Task Promises

Each task in the API returns the `simpleGit` instance for chaining together multiple tasks, and each
step in the chain is also a `Promise` that can be `await` ed in an `async` function or returned in a
`Promise` chain.

```javascript
const git = simpleGit();

// chain together tasks to await final result
await git.init().addRemote('origin', '...remote.git');

// or await each step individually
await git.init();
await git.addRemote('origin', '...remote.git');
```

### Catching errors in async code

To catch errors in async code, either wrap the whole chain in a try/catch:

```javascript
const git = simpleGit();
try {
   await git.init();
   await git.addRemote(name, repoUrl);
} catch (e) {
   /* handle all errors here */
}
```

or catch individual steps to permit the main chain to carry on executing rather than
jumping to the final `catch` on the first error:

```javascript
const git = simpleGit();
try {
   await git.init().catch(ignoreError);
   await git.addRemote(name, repoUrl);
} catch (e) {
   /* handle all errors here */
}

function ignoreError() {}
```

## Using Task Callbacks

In addition to returning a promise, each method can also be called with a trailing callback argument
to handle the result of the task.

```javascript
const git = simpleGit();
git.init(onInit).addRemote('origin', 'git@github.com:steveukx/git-js.git', onRemoteAdd);

function onInit(err, initResult) {}
function onRemoteAdd(err, addRemoteResult) {}
```

If any of the steps in the chain result in an error, all pending steps will be cancelled, see the
[parallel tasks](<(#concurrent--parallel-requests)>) section for more information on how to run tasks in parallel rather than in series .

## Task Responses

Whether using a trailing callback or a Promise, tasks either return the raw `string` or `Buffer` response from the
`git` binary, or where possible a parsed interpretation of the response.

For type details of the response for each of the tasks, please see the [TypeScript definitions](https://github.com/steveukx/git-js/blob/main/simple-git/typings/simple-git.d.ts).

# Upgrading from Version 2

From v3 of `simple-git` you can now import as an ES module, Common JS module or as TypeScript with bundled type
definitions. Upgrading from v2 will be seamless for any application not relying on APIs that were marked as deprecated
in v2 (deprecation notices were logged to `stdout` as `console.warn` in v2).

# API

| API                                                  | What it does                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `.add([fileA, ...], handlerFn)`                      | adds one or more files to be under source control                                                                                                                                                                                                                                                                                                                                                                            |
| `.addAnnotatedTag(tagName, tagMessage, handlerFn)`   | adds an annotated tag to the head of the current branch                                                                                                                                                                                                                                                                                                                                                                      |
| `.addTag(name, handlerFn)`                           | adds a lightweight tag to the head of the current branch                                                                                                                                                                                                                                                                                                                                                                     |
| `.catFile(options, [handlerFn])`                     | generate `cat-file` detail, `options` should be an array of strings as supported arguments to the [cat-file](https://git-scm.com/docs/git-cat-file) command                                                                                                                                                                                                                                                                  |
| `.checkIgnore([filepath, ...], handlerFn)`           | checks if filepath excluded by .gitignore rules                                                                                                                                                                                                                                                                                                                                                                              |
| `.commit(message, handlerFn)`                        | commits changes in the current working directory with the supplied message where the message can be either a single string or array of strings to be passed as separate arguments (the `git` command line interface converts these to be separated by double line breaks)                                                                                                                                                    |
| `.commit(message, [fileA, ...], options, handlerFn)` | commits changes on the named files with the supplied message, when supplied, the optional options object can contain any other parameters to pass to the commit command, setting the value of the property to be a string will add `name=value` to the command string, setting any other type of value will result in just the key from the object being passed (ie: just `name`), an example of setting the author is below |
| `.customBinary(gitPath)`                             | sets the command to use to reference git, allows for using a git binary not available on the path environment variable [docs](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-CUSTOM-BINARY.md)                                                                                                                                                                                                                     |
| `.env(name, value)`                                  | Set environment variables to be passed to the spawned child processes, [see usage in detail below](#environment-variables).                                                                                                                                                                                                                                                                                                  |
| `.exec(handlerFn)`                                   | calls a simple function in the current step                                                                                                                                                                                                                                                                                                                                                                                  |
| `.fetch([options, ] handlerFn)`                      | update the local working copy database with changes from the default remote repo and branch, when supplied the options argument can be a standard [options object](#how-to-specify-options) either an array of string commands as supported by the [git fetch](https://git-scm.com/docs/git-fetch).                                                                                                                          |
| `.fetch(remote, branch, handlerFn)`                  | update the local working copy database with changes from a remote repo                                                                                                                                                                                                                                                                                                                                                       |
| `.fetch(handlerFn)`                                  | update the local working copy database with changes from the default remote repo and branch                                                                                                                                                                                                                                                                                                                                  |
| `.outputHandler(handlerFn)`                          | attaches a handler that will be called with the name of the command being run and the `stdout` and `stderr` [readable streams](https://nodejs.org/api/stream.html#stream_class_stream_readable) created by the [child process](https://nodejs.org/api/child_process.html#child_process_class_childprocess) running that command, see [examples](https://github.com/steveukx/git-js/blob/main/examples/git-output-handler.md) |
| `.raw(args, [handlerFn])`                            | Execute any arbitrary array of commands supported by the underlying git binary. When the git process returns a non-zero signal on exit and it printed something to `stderr`, the command will be treated as an error, otherwise treated as a success.                                                                                                                                                                        |
| `.rebase([options,] handlerFn)`                      | Rebases the repo, `options` should be supplied as an array of string parameters supported by the [git rebase](https://git-scm.com/docs/git-rebase) command, or an object of options (see details below for option formats).                                                                                                                                                                                                  |
| `.revert(commit , [options , [handlerFn]])`          | reverts one or more commits in the working copy. The commit can be any regular commit-ish value (hash, name or offset such as `HEAD~2`) or a range of commits (eg: `master~5..master~2`). When supplied the [options](#how-to-specify-options) argument contain any options accepted by [git-revert](https://git-scm.com/docs/git-revert).                                                                                   |
| `.rm([fileA, ...], handlerFn)`                       | removes any number of files from source control                                                                                                                                                                                                                                                                                                                                                                              |
| `.rmKeepLocal([fileA, ...], handlerFn)`              | removes files from source control but leaves them on disk                                                                                                                                                                                                                                                                                                                                                                    |
| `.tag(args[], handlerFn)`                            | Runs any supported [git tag](https://git-scm.com/docs/git-tag) commands with arguments passed as an array of strings .                                                                                                                                                                                                                                                                                                       |
| `.tags([options, ] handlerFn)`                       | list all tags, use the optional [options](#how-to-specify-options) object to set any options allows by the [git tag](https://git-scm.com/docs/git-tag) command. Tags will be sorted by semantic version number by default, for git versions 2.7 and above, use the `--sort` option to set a custom sort.                                                                                                                     |

## git apply

-  `.applyPatch(patch, [options])` applies a single string patch (as generated by `git diff`), optionally configured with the supplied [options](#how-to-specify-options) to set any arguments supported by the [apply](https://git-scm.com/docs/git-apply) command. Returns the unmodified string response from `stdout` of the `git` binary.
-  `.applyPatch(patches, [options])` applies an array of string patches (as generated by `git diff`), optionally configured with the supplied [options](#how-to-specify-options) to set any arguments supported by the [apply](https://git-scm.com/docs/git-apply) command. Returns the unmodified string response from `stdout` of the `git` binary.

## git branch

-  `.branch([options])` uses the supplied [options](#how-to-specify-options) to run any arguments supported by the [branch](https://git-scm.com/docs/git-branch) command. Either returns a [BranchSummaryResult](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/responses/BranchSummary.ts) instance when listing branches, or a [BranchSingleDeleteResult](https://github.com/steveukx/git-js/blob/main/simple-git/typings/response.d.ts) type object when the options included `-d`, `-D` or `--delete` which cause it to delete a named branch rather than list existing branches.
-  `.branchLocal()` gets a list of local branches as a [BranchSummaryResult](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/responses/BranchSummary.ts) instance
-  `.deleteLocalBranch(branchName)` deletes a local branch - treats a failed attempt as an error
-  `.deleteLocalBranch(branchName, forceDelete)` deletes a local branch, optionally explicitly setting forceDelete to true - treats a failed attempt as an error
-  `.deleteLocalBranches(branchNames)` deletes multiple local branches
-  `.deleteLocalBranches(branchNames, forceDelete)` deletes multiple local branches, optionally explicitly setting forceDelete to true

## git clean

-  `.clean(mode)` clean the working tree. Mode should be "n" - dry run or "f" - force
-  `.clean(cleanSwitches [,options])` set `cleanSwitches` to a string containing any number of the supported single character options, optionally with a standard [options](#how-to-specify-options) object

## git checkout

-  `.checkout(checkoutWhat , [options])` - checks out the supplied tag, revision or branch when supplied as a string,
   additional arguments supported by [git checkout](https://git-scm.com/docs/git-checkout) can be supplied as an
   [options](#how-to-specify-options) object/array.

-  `.checkout(options)` - check out a tag or revision using the supplied [options](#how-to-specify-options)

-  `.checkoutBranch(branchName, startPoint)` - checks out a new branch from the supplied start point.

-  `.checkoutLocalBranch(branchName)` - checks out a new local branch

## git clone

-  `.clone(repoPath, [localPath, [options]])` clone a remote repo at `repoPath` to a local directory at `localPath`, optionally with a standard [options](#how-to-specify-options) object of additional arguments to include between `git clone` and the trailing `repo local` arguments
-  `.clone(repoPath, [options])` clone a remote repo at `repoPath` to a directory in the current working directory with the same name as the repo

-  `mirror(repoPath, [localPath, [options]])` behaves the same as the `.clone` interface with the [`--mirror` flag](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---mirror) enabled.

Note: as of version 3.33.0, `repoPath` and `localPath` are passed to `git` as "pathspec" arguments so are less open to unexpected unsafe behaviour when passing unsanitised data into the command.

## git config

-  `.addConfig(key, value, append = false, scope = 'local')` add a local configuration property, when `append` is set to
   `true` the configuration setting is appended to rather than overwritten in the local config. Use the `scope` argument
   to pick where to save the new configuration setting (use the exported `GitConfigScope` enum, or equivalent string
   values - `worktree | local | global | system`).
-  `.getConfig(key)` get the value(s) for a named key as a [ConfigGetResult](https://github.com/steveukx/git-js/blob/main/simple-git/typings/response.d.ts)
-  `.getConfig(key, scope)` get the value(s) for a named key as a [ConfigGetResult](https://github.com/steveukx/git-js/blob/main/simple-git/typings/response.d.ts) but limit the
   scope of the properties searched to a single specified scope (use the exported `GitConfigScope` enum, or equivalent
   string values - `worktree | local | global | system`)

-  `.listConfig()` reads the current configuration and returns a [ConfigListSummary](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/responses/ConfigList.ts)
-  `.listConfig(scope: GitConfigScope)` as with `listConfig` but returns only those items in a specified scope (note that configuration values are overlaid on top of each other to build the config `git` will actually use - to resolve the configuration you are using use `(await listConfig()).all` without the scope argument)

## git count-objects

- `.countObjects()` queries the pack and disk usage properties of the local repository and returns a [CountObjectsResult](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/tasks/count-objects.ts). All disk sizes are reported in Kb, see https://git-scm.com/docs/git-count-objects for full description of properties.

## git diff

-  `.diff([ options ])` get the diff of the current repo compared to the last commit, optionally including
   any number of other arguments supported by [git diff](https://git-scm.com/docs/git-diff) supplied as an
   [options](#how-to-specify-options) object/array. Returns the raw `diff` output as a string.

-  `.diffSummary([ options ])` creates a [DiffResult](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/responses/DiffSummary.ts)
   to summarise the diff for files in the repo. Uses the `--stat` format by default which can be overridden
   by passing in any of the log format commands (eg: `--numstat` or `--name-stat`) as part of the optional
   [options](#how-to-specify-options) object/array.

## git grep [examples](https://github.com/steveukx/git-js/blob/main/examples/git-grep.md)

-  `.grep(searchTerm)` searches for a single search term across all files in the working tree, optionally passing a standard [options](#how-to-specify-options) object of additional arguments
-  `.grep(grepQueryBuilder(...))` use the `grepQueryBuilder` to create a complex query to search for, optionally passing a standard [options](#how-to-specify-options) object of additional arguments

## git hash-object

-  `.hashObject(filePath, write = false)` computes the object ID value for the contents of the named file (which can be
   outside of the work tree), optionally writing the resulting value to the object database.

## git init

-  `.init(bare , [options])` initialize a repository using the boolean `bare` parameter to intialise a bare repository.
   Any number of other arguments supported by [git init](https://git-scm.com/docs/git-init) can be supplied as an
   [options](#how-to-specify-options) object/array.

-  `.init([options])` initialize a repository using any arguments supported by
   [git init](https://git-scm.com/docs/git-init) supplied as an [options](#how-to-specify-options) object/array.

## git log

-  `.log([options])` list commits between `options.from` and `options.to` tags or branch (if not specified will
   show all history). Use the `options` object to set any [options](#how-to-specify-options) supported by the
   [git log](https://git-scm.com/docs/git-log) command or any of the following:

   -  `options.file` - the path to a file in your repository to only consider this path.
   -  `options.format` - custom log format object, keys are the property names used on the returned object, values are the format string from [pretty formats](https://git-scm.com/docs/pretty-formats#Documentation/pretty-formats.txt)
   -  `options.from` - sets the oldest commit in the range to return, use along with `options.to` to set a bounded range
   -  `options.mailMap` - defaults to true, enables the use of [mail map](https://git-scm.com/docs/gitmailmap) in returned values for email and name from the default format
   -  `options.maxCount` - equivalent to setting the `--max-count` option
   -  `options.multiLine` - enables multiline body values in the default format (disabled by default)
   -  `options.splitter` - the character sequence to use as a delimiter between fields in the log, should be a value that doesn't appear in any log message (defaults to `ò`)
   -  `options.strictDate` - switches the authored date value from an ISO 8601-like format to be strict ISO 8601 format
   -  `options.symmetric` - defaults to true, enables [symmetric revision range](https://git-scm.com/docs/gitrevisions#_dotted_range_notations) rather than a two-dot range
   -  `options.to` - sets the newset commit in the range to return, use along with `options.from` to set a bounded range
   
   When only one of `options.from` and `options.to` is supplied, the default value of the omitted option is equivalent to `HEAD`. For any other commit, explicitly supply both from and to commits (for example use `await git.firstCommit()` as the default value of `from` to log since the first commit of the repo). 

## git merge

-  `.merge(options)` runs a merge using any configuration [options](#how-to-specify-options) supported
   by [git merge](https://git-scm.com/docs/git-merge).
   Conflicts during the merge result in an error response, the response is an instance of
   [MergeSummary](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/responses/MergeSummary.ts) whether it was an error or success.
   When successful, the MergeSummary has all detail from a the [PullSummary](https://github.com/steveukx/git-js/blob/main/simple-git/src/lib/responses/PullSummary.ts)
   along with summary detail for the merge.
   When the merge failed, the MergeSummary contains summary detail for why the merge failed and which files
   prevented the merge.

-  `.mergeFromTo(remote, branch , [options])` - merge from the specified branch into the currently checked out branch,
   similar to `.merge` but with the `remote` and `branch` supplied as strings separately to any additional
   [options](#how-to-specify-options).

## git mv

-  `.mv(from, to)` rename or move a single file at `from` to `to`

-  `.mv(from, to)` move all files in the `from` array to the `to` directory

## git pull

-  `.pull([options])` pulls all updates from the default tracked remote, any arguments supported by
   [git pull](https://git-scm.com/docs/git-pull) can be supplied as an [options](#how-to-specify-options) object/array.

-  `.pull(remote, branch, [options])` pulls all updates from the specified remote branch (eg 'origin'/'master') along
   with any custom [options](#how-to-specify-options) object/array

## git push

-  `.push([options])` pushes to a named remote/branch using any supported [options](#how-to-specify-options)
   from the [git push](https://git-scm.com/docs/git-push) command. Note that `simple-git` enforces the use of
   `--verbose --porcelain` options in order to parse the response. You don't need to supply these options.

-  `.push(remote, branch, [options])` pushes to a named remote/branch, supports additional
   [options](#how-to-specify-options) from the [git push](https://git-scm.com/docs/git-push) command.

-  `.pushTags(remote, [options])` pushes local tags to a named remote (equivalent to using `.push([remote, '--tags'])`)

## git remote

-  `.addRemote(name, repo, [options])` adds a new named remote to be tracked as `name` at the path `repo`, optionally with any supported [options](#how-to-specify-options) for the [git add](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emaddem) call.
-  `.getRemotes([verbose])` gets a list of the named remotes, supply the optional `verbose` option as `true` to include the URLs and purpose of each ref
-  `.listRemote([options])` lists remote repositories - there are so many optional arguments in the underlying `git ls-remote` call, just supply any you want to use as the optional [options](#how-to-specify-options) eg: `git.listRemote(['--heads', '--tags'], console.log)`
-  `.remote([options])` runs a `git remote` command with any number of [options](#how-to-specify-options)
-  `.removeRemote(name)` removes the named remote

## git reset

-  `.reset(resetMode, [resetOptions])` resets the repository, sets the reset mode to one of the supported types (use a constant from
   the exported `ResetMode` enum, or a string equivalent: `mixed`, `soft`, `hard`, `merge`, `keep`). Any number of other arguments
   supported by [git reset](https://git-scm.com/docs/git-reset) can be supplied as an [options](#how-to-specify-options) object/array.

-  `.reset(resetOptions)` resets the repository with the supplied [options](#how-to-specify-options)

-  `.reset()` resets the repository in `soft` mode.

## git rev-parse / repo properties

-  `.revparse([options])` sends the supplied [options](#how-to-specify-options) to [git rev-parse](https://git-scm.com/docs/git-rev-parse) and returns the string response from `git`.

-  `.checkIsRepo()` gets whether the current working directory is a descendent of a git repository.
-  `.checkIsRepo('bare')` gets whether the current working directory is within a bare git repo (see either [git clone --bare](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---bare) or [git init --bare](https://git-scm.com/docs/git-init#Documentation/git-init.txt---bare)).
-  `.checkIsRepo('root')` gets whether the current working directory is the root directory for a repo (sub-directories will return false).

-  `.firstCommit()` gets the commit hash of the first commit made to the current repo.

## git show

- `.show(options)` show various types of objects for example the file content at a certain commit. `options` is the single value string or any [options](#how-to-specify-options) supported by the [git show](https://git-scm.com/docs/git-show) command.
- `.showBuffer(options)` same as the `.show` API, but returns the Buffer content directly to allow for showing binary file content.

## git status

-  `.status([options])` gets the status of the current repo, resulting in a [StatusResult](https://github.com/steveukx/git-js/blob/main/simple-git/typings/response.d.ts). Additional arguments
   supported by [git status](https://git-scm.com/docs/git-status) can be supplied as an [options](#how-to-specify-options) object/array.

## git submodule

-  `.subModule(options)` Run a `git submodule` command with on or more arguments passed in as an [options](#how-to-specify-options) array or object
-  `.submoduleAdd(repo, path)` Adds a new sub module
-  `.submoduleInit([options]` Initialises sub modules, the optional [options](#how-to-specify-options) argument can be used to pass extra options to the `git submodule init` command.
-  `.submoduleUpdate(subModuleName, [options])` Updates sub modules, can be called with a sub module name and [options](#how-to-specify-options), just the options or with no arguments

## git stash

- `.stash([ options ])` Stash the working directory, optional first argument can be an array of string arguments or [options](#how-to-specify-options) object to pass to the [git stash](https://git-scm.com/docs/git-stash) command.

- `.stashList([ options ])` Retrieves the stash list, optional first argument can be an object in the same format as used in [git log](#git-log).

## git version [examples](https://github.com/steveukx/git-js/blob/main/examples/git-version.md)

- `.version()` retrieve the major, minor and patch for the currently installed `git`. Use the `.installed` property of the result to determine whether `git` is accessible on the path.

## changing the working directory [examples](https://github.com/steveukx/git-js/blob/main/examples/git-change-working-directory.md)

-  `.cwd(workingDirectory)` Sets the working directory for all future commands - note, this will change the working for the root instance, any chain created from the root will also be changed.
-  `.cwd({ path, root = false })` Sets the working directory for all future commands either in the current chain of commands (where `root` is omitted or set to `false`) or in the main instance (where `root` is `true`).

## How to Specify Options

Where the task accepts custom options (eg: `pull` or `commit`), these can be supplied as an object, the keys of which
will all be merged as trailing arguments in the command string, or as a simple array of strings.

### Options as an Object

When the value of the property in the options object is a `string`, that name value
pair will be included in the command string as `name=value`. For example:

```javascript
// results in 'git pull origin master --no-rebase'
git.pull('origin', 'master', { '--no-rebase': null });

// results in 'git pull origin master --rebase=true'
git.pull('origin', 'master', { '--rebase': 'true' });
```

When the value of the property is an array of `string`s or `number`s, each element will be 
included as separate `name=value` pairs:

```javascript
// results in 'git log --grep=bug --grep=fix --grep=feature'
git.log({ '--grep': ['bug', 'fix', 'feature'] });
```

### Options as an Array

Options can also be supplied as an array of strings to be merged into the task's commands
in the same way as when an object is used:

```javascript
// results in 'git pull origin master --no-rebase'
git.pull('origin', 'master', ['--no-rebase']);
```

# Release History

Major release 3.x changes the packaging of the library, making it consumable as a CommonJS module, ES module as well as
with TypeScript (see [usage](#usage) above). The library is now published as a single file, so please ensure your
application hasn't been making use of non-documented APIs by importing from a sub-directory path.

See also:

- [release notes v3](https://github.com/steveukx/git-js/blob/main/simple-git/CHANGELOG.md)
- [release notes v2](https://github.com/steveukx/git-js/blob/main/docs/RELEASE-NOTES-V2.md)

# Concurrent / Parallel Requests

When the methods of `simple-git` are chained together, they create an execution chain that will run in series, useful
for when the tasks themselves are order-dependent, eg:

```typescript
simpleGit().init().addRemote('origin', 'https://some-repo.git').fetch();
```

Each task requires that the one before it has been run successfully before it is called, any errors in a
step of the chain should prevent later steps from being attempted.

When the methods of `simple-git` are called on the root instance (ie: `git = simpleGit()`) rather than chained
off another task, it starts a new chain and will not be affected failures in tasks already being run. Useful
for when the tasks are independent of each other, eg:

```typescript
const git = simpleGit();
const results = await Promise.all([
   git.raw('rev-parse', '--show-cdup').catch(swallow),
   git.raw('rev-parse', '--show-prefix').catch(swallow),
]);
function swallow(err) {
   return null;
}
```

Each `simple-git` instance limits the number of spawned child processes that can be run simultaneously and
manages the queue of pending tasks for you. Configure this value by passing an options object to the
`simpleGit` function, eg:

```typescript
const git = simpleGit({ maxConcurrentProcesses: 10 });
```

Treating tasks called on the root instance as the start of separate chains is a change to the behaviour of
`simple-git` and was added in version `2.11.0`.

# Complex Requests

When no suitable wrapper exists in the interface for creating a request, run the command directly
using `git.raw([...], handler)`. The array of commands are passed directly to the `git` binary:

```javascript
const path = '/path/to/repo';
const commands = ['config', '--global', 'advice.pushNonFastForward', 'false'];

// using an array of commands and node-style callback
simpleGit(path).raw(commands, (err, result) => {
   // err is null unless this command failed
   // result is the raw output of this command
});

// using a var-args of strings and awaiting rather than using the callback
const result = await simpleGit(path).raw(...commands);

// automatically trim trailing white-space in responses
const result = await simpleGit(path, { trimmed: true }).raw(...commands);
```

# Authentication

The easiest way to supply a username / password to the remote host is to include it in the URL, for example:

```javascript
const USER = 'something';
const PASS = 'somewhere';
const REPO = 'github.com/username/private-repo';

const remote = `https://${USER}:${PASS}@${REPO}`;

simpleGit()
   .clone(remote)
   .then(() => console.log('finished'))
   .catch((err) => console.error('failed: ', err));
```

Be sure to not enable debug logging when using this mechanism for authentication
to ensure passwords aren't logged to stdout.

# Environment Variables

Pass one or more environment variables to the child processes spawned by `simple-git` with the `.env` method which
supports passing either an object of name=value pairs or setting a single variable at a time:

```javascript
const GIT_SSH_COMMAND = 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no';

simpleGit()
   .env('GIT_SSH_COMMAND', GIT_SSH_COMMAND)
   .status((err, status) => {
      /*  */
   });

simpleGit()
   .env({ ...process.env, GIT_SSH_COMMAND })
   .status()
   .then((status) => {})
   .catch((err) => {});
```

Note - when passing environment variables into the child process, these will replace the standard `process.env`
variables, the example above creates a new object based on `process.env` but with the `GIT_SSH_COMMAND` property added.

# Exception Handling

When the `git` process exits with a non-zero status (or in some cases like `merge` the git process exits with a
successful zero code but there are conflicts in the merge) the task will reject with a `GitError` when there is no
available parser to handle the error or a
`GitResponseError` for when there is.

See the `err` property of the callback:

```javascript
git.merge((err, mergeSummary) => {
   if (err.git) {
      mergeSummary = err.git; // the failed mergeSummary
   }
});
```

Catch errors with try/catch in async code:

```javascript
try {
   const mergeSummary = await git.merge();
   console.log(`Merged ${mergeSummary.merges.length} files`);
} catch (err) {
   // err.message - the string summary of the error
   // err.stack - some stack trace detail
   // err.git - where a parser was able to run, this is the parsed content

   console.error(`Merge resulted in ${err.git.conflicts.length} conflicts`);
}
```

Catch errors with a `.catch` on the promise:

```javascript
const mergeSummary = await git.merge().catch((err) => {
   if (err.git) {
      return err.git;
   } // the unsuccessful mergeSummary
   throw err; // some other error, so throw
});

if (mergeSummary.failed) {
   console.error(`Merge resulted in ${mergeSummary.conflicts.length} conflicts`);
}
```

With typed errors available in TypeScript

```typescript
import { simpleGit, MergeSummary, GitResponseError } from 'simple-git';
try {
   const mergeSummary = await simpleGit().merge();
   console.log(`Merged ${mergeSummary.merges.length} files`);
} catch (err) {
   // err.message - the string summary of the error
   // err.stack - some stack trace detail
   // err.git - where a parser was able to run, this is the parsed content
   const mergeSummary: MergeSummary = (err as GitResponseError<MergeSummary>).git;
   const conflicts = mergeSummary?.conflicts || [];

   console.error(`Merge resulted in ${conflicts.length} conflicts`);
}
```

# Troubleshooting / FAQ

### Enable logging

See the [debug logging guide](https://github.com/steveukx/git-js/blob/main/docs/DEBUG-LOGGING-GUIDE.md) for logging examples and how to
make use of the [debug](https://www.npmjs.com/package/debug) library's programmatic interface
in your application.

### Enable Verbose Logging

See the [debug logging guide](https://github.com/steveukx/git-js/blob/main/docs/DEBUG-LOGGING-GUIDE.md#verbose-logging-options) for
the full list of verbose logging options to use with the
[debug](https://www.npmjs.com/package/debug) library.

### Every command returns ENOENT error message

There are a few potential reasons:

-  `git` isn't available as a binary for the user running the main `node` process, custom paths to the binary can be used
   with the `.customBinary(...)` API option.

-  the working directory passed in to the main `simple-git` function isn't accessible, check it is read/write accessible
   by the user running the `node` process. This library uses
   [@kwsites/file-exists](https://www.npmjs.com/package/@kwsites/file-exists) to validate the working directory exists,
   to output its logs add `@kwsites/file-exists` to your `DEBUG` environment variable. eg:

   `DEBUG=@kwsites/file-exists,simple-git node ./your-app.js`

### Log format fails

The properties of `git log` are fetched using the `--pretty=format` argument which supports different tokens depending
on the version of `git` - for example the `%D` token used to show the refs was added in git `2.2.3`, for any version
before that please ensure you are supplying your own format object with properties supported by the version of git you
are using.

For more details of the supported tokens, please see the
[official `git log` documentation](https://git-scm.com/docs/git-log#_pretty_formats)

### Log response properties are out of order

The properties of `git.log` are fetched using the character sequence `ò` as a delimiter. If your commit messages
use this sequence, supply a custom `splitter` in the options, for example: `git.log({ splitter: '💻' })`

### Pull / Diff / Merge summary responses don't recognise any files

-  Enable verbose logs with the environment variable `DEBUG=simple-git:task:*,simple-git:output:*`
-  Check the output (for example: `simple-git:output:diff:1 [stdOut] 1 file changed, 1 insertion(+)`)
-  Check the `stdOut` output is the same as you would expect to see when running the command directly in terminal
-  Check the language used in the response is english locale

In some cases `git` will show progress messages or additional detail on error states in the output for
`stdErr` that will help debug your issue, these messages are also included in the verbose log.

### Legacy Node Versions

From `v3.x`, `simple-git` will drop support for `node.js` version 10 or below, to use in a lower version of node will
result in errors such as:

-  `Object.fromEntries is not a function`
-  `Object.entries is not a function`
-  `message.flatMap is not a function`

To resolve these issues, either upgrade to a newer version of node.js or ensure you are using the necessary polyfills
from `core-js` - see [Legacy Node Versions](https://github.com/steveukx/git-js/blob/main/docs/LEGACY_NODE_VERSIONS.md).

# Examples

### using a pathspec to limit the scope of the task

If the `simple-git` API doesn't explicitly limit the scope of the task being run (ie: `git.add()` requires the files to
be added, but `git.status()` will run against the entire repo), add a `pathspec` to the command using trailing options:

```typescript
import { simpleGit, pathspec } from "simple-git";

const git = simpleGit();
const wholeRepoStatus = await git.status();
const subDirStatusUsingOptArray = await git.status([pathspec('sub-dir')]);
const subDirStatusUsingOptObject = await git.status({ 'sub-dir': pathspec('sub-dir') });
```

### async await

```javascript
async function status(workingDir) {
   let statusSummary = null;
   try {
      statusSummary = await simpleGit(workingDir).status();
   } catch (e) {
      // handle the error
   }

   return statusSummary;
}

// using the async function
status(__dirname + '/some-repo').then((status) => console.log(status));
```

### Initialise a git repo if necessary

```javascript
const git = simpleGit(__dirname);

git.checkIsRepo()
   .then((isRepo) => !isRepo && initialiseRepo(git))
   .then(() => git.fetch());

function initialiseRepo(git) {
   return git.init().then(() => git.addRemote('origin', 'https://some.git.repo'));
}
```

### Update repo and get a list of tags

```javascript
simpleGit(__dirname + '/some-repo')
   .pull()
   .tags((err, tags) => console.log('Latest available tag: %s', tags.latest));

// update repo and when there are changes, restart the app
simpleGit().pull((err, update) => {
   if (update && update.summary.changes) {
      require('child_process').exec('npm restart');
   }
});
```

### Starting a new repo

```javascript
simpleGit()
   .init()
   .add('./*')
   .commit('first commit!')
   .addRemote('origin', 'https://github.com/user/repo.git')
   .push('origin', 'master');
```

### push with `-u`

```javascript
simpleGit()
   .add('./*')
   .commit('first commit!')
   .addRemote('origin', 'some-repo-url')
   .push(['-u', 'origin', 'master'], () => console.log('done'));
```

### Piping to the console for long-running tasks

See [progress events](https://github.com/steveukx/git-js/blob/main/docs/PLUGIN-PROGRESS-EVENTS.md) for more details on
logging progress updates.

```javascript
const git = simpleGit({
   progress({ method, stage, progress }) {
      console.log(`git.${method} ${stage} stage ${progress}% complete`);
   },
});
git.checkout('https://github.com/user/repo.git');
```

### Update repo and print messages when there are changes, restart the app

```javascript
// when using a chain
simpleGit()
   .exec(() => console.log('Starting pull...'))
   .pull((err, update) => {
      if (update && update.summary.changes) {
         require('child_process').exec('npm restart');
      }
   })
   .exec(() => console.log('pull done.'));

// when using async and optional chaining
const git = simpleGit();
console.log('Starting pull...');
if ((await git.pull())?.summary.changes) {
   require('child_process').exec('npm restart');
}
console.log('pull done.');
```

### Get a full commits list, and then only between 0.11.0 and 0.12.0 tags

```javascript
console.log(await simpleGit().log());
console.log(await simpleGit().log('0.11.0', '0.12.0'));
```

### Set the local configuration for author, then author for an individual commit

```javascript
simpleGit()
   .addConfig('user.name', 'Some One')
   .addConfig('user.email', 'some@one.com')
   .commit('committed as "Some One"', 'file-one')
   .commit('committed as "Another Person"', 'file-two', {
      '--author': '"Another Person <another@person.com>"',
   });
```

### Get remote repositories

```javascript
simpleGit().listRemote(['--get-url'], (err, data) => {
   if (!err) {
      console.log('Remote url for repository at ' + __dirname + ':');
      console.log(data);
   }
});
```


---

## 50. pygments
- **URL:** https://github.com/devtechedge/pygments
- **Language:** Python
- **Topics:** None
- **Description:** Pygments is a generic syntax highlighter written in Python

### README.md

Welcome to Pygments
===================

This is the source of Pygments.  It is a **generic syntax highlighter** written
in Python that supports over 500 languages and text formats, for use in code
hosting, forums, wikis or other applications that need to prettify source code.

Installing
----------

... works as usual, use ``pip install Pygments`` to get published versions,
or ``pip install -e .`` to install from a checkout in editable mode.

Documentation
-------------

... can be found online at https://pygments.org/ or created with Sphinx by ::

   tox -e doc

By default, the documentation does not include the demo page, as it requires
having Docker installed for building Pyodide. To build the documentation with
the demo page, use ::

   tox -e web-doc

The initial build might take some time, but subsequent ones should be instant
because of Docker caching.

To view the generated documentation, serve it using Python's ``http.server``
module (this step is required for the demo to work) ::

   python3 -m http.server --directory doc/_build/html


Development
-----------

... takes place on `GitHub <https://github.com/pygments/pygments>`_, where the
Git repository, tickets and pull requests can be viewed.

Continuous testing runs on GitHub workflows:

.. image:: https://github.com/pygments/pygments/workflows/Pygments/badge.svg
   :target: https://github.com/pygments/pygments/actions?query=workflow%3APygments

Please read our `Contributing instructions <https://pygments.org/docs/contributing>`_.

Security considerations
-----------------------

Pygments provides no guarantees on execution time, which needs to be taken
into consideration when using Pygments to process arbitrary user inputs. For
example, if you have a web service which uses Pygments for highlighting, there
may be inputs which will cause the Pygments process to run "forever" and/or use
significant amounts of memory. This can subsequently be used to perform a
remote denial-of-service attack on the server if the processes are not
terminated quickly.

Unfortunately, it's practically impossible to harden Pygments itself against
those issues: Some regular expressions can result in "catastrophic
backtracking", but other bugs like incorrect matchers can also
cause similar problems, and there is no way to find them in an automated fashion
(short of solving the halting problem.) Pygments has extensive unit tests,
automated randomized testing, and is also tested by `OSS-Fuzz <https://github.com/google/oss-fuzz/tree/master/projects/pygments>`_,
but we will never be able to eliminate all bugs in this area.

Our recommendations are:

* Ensure that the Pygments process is *terminated* after a reasonably short
  timeout. In general Pygments should take seconds at most for reasonably-sized
  input.
* *Limit* the number of concurrent Pygments processes to avoid oversubscription
  of resources.

The Pygments authors will treat any bug resulting in long processing times with
high priority -- it's one of those things that will be fixed in a patch release.
When reporting a bug where you suspect super-linear execution times, please make
sure to attach an input to reproduce it.

The authors
-----------

Pygments is maintained by **Georg Brandl**, e-mail address *georg*\ *@*\ *python.org*, **Matthäus Chajdas** and **Jean Abou-Samra**.

Many lexers and fixes have been contributed by **Armin Ronacher**, the rest of
the `Pocoo <https://www.pocoo.org/>`_ team and **Tim Hatch**.

The code is distributed under the BSD 2-clause license.  Contributors making pull
requests must agree that they are able and willing to put their contributions
under that license.


---

## 51. python
- **URL:** https://github.com/devtechedge/python
- **Language:** HTML
- **Topics:** None
- **Description:** A Python handler for mkdocstrings.

### README.md

<h1 align="center">mkdocstrings-python</h1>

<p align="center">A Python handler for <a href="https://github.com/mkdocstrings/mkdocstrings"><i>mkdocstrings</i></a>.</p>

[![ci](https://github.com/mkdocstrings/python/workflows/ci/badge.svg)](https://github.com/mkdocstrings/python/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/python/)
[![pypi version](https://img.shields.io/pypi/v/mkdocstrings-python.svg)](https://pypi.org/project/mkdocstrings-python/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#mkdocstrings_python:gitter.im)

---

<p align="center"><img src="logo.png"></p>

The Python handler uses [Griffe](https://mkdocstrings.github.io/griffe)
to collect documentation from Python source code.
The word "griffe" can sometimes be used instead of "signature" in French.
Griffe is able to visit the Abstract Syntax Tree (AST) of the source code to extract useful information.
It is also able to execute the code (by importing it) and introspect objects in memory
when source code is not available. Finally, it can parse docstrings following different styles.

## Installation

You can install this handler as a *mkdocstrings* extra:

```toml title="pyproject.toml"
# PEP 621 dependencies declaration
# adapt to your dependencies manager
[project]
dependencies = [
    "mkdocstrings[python]>=0.18",
]
```

You can also explicitly depend on the handler:

```toml title="pyproject.toml"
# PEP 621 dependencies declaration
# adapt to your dependencies manager
[project]
dependencies = [
    "mkdocstrings-python",
]
```

## Preview

<!-- TODO: update the GIF with a more recent screen capture. Maybe use mp4 instead -->
![mkdocstrings_python_gif](https://user-images.githubusercontent.com/3999221/77157838-7184db80-6aa2-11ea-9f9a-fe77405202de.gif)

## Features

- **Data collection from source code**: collection of the object-tree and the docstrings is done thanks to
  [Griffe](https://github.com/mkdocstrings/griffe).

- **Support for type annotations:** Griffe collects your type annotations and *mkdocstrings* uses them
  to display parameter types or return types. It is even able to automatically add cross-references
  to other objects from your API, from the standard library or third-party libraries!
  See [how to load inventories](https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories) to enable it.

- **Recursive documentation of Python objects:** just use the module dotted-path as an identifier, and you get the full
  module docs. You don't need to inject documentation for each class, function, etc.

- **Support for documented attributes:** attributes (variables) followed by a docstring (triple-quoted string) will
  be recognized by Griffe in modules, classes and even in `__init__` methods.

- **Multiple docstring-styles support:** common support for Google-style, Numpydoc-style,
  and Sphinx-style docstrings. See [Griffe's documentation](https://mkdocstrings.github.io/griffe/docstrings/) on docstrings support.

- **Admonition support in Google docstrings:** blocks like `Note:` or `Warning:` will be transformed
  to their [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) equivalent.
  *We do not support nested admonitions in docstrings!*

- **Every object has a TOC entry:** we render a heading for each object, meaning *MkDocs* picks them into the Table
  of Contents, which is nicely displayed by the Material theme. Thanks to *mkdocstrings* cross-reference ability,
  you can reference other objects within your docstrings, with the classic Markdown syntax:
  `[this object][package.module.object]` or directly with `[package.module.object][]`

- **Source code display:** *mkdocstrings* can add a collapsible div containing the highlighted source code
  of the Python object.

## Sponsors

<!-- sponsors-start -->

<div id="premium-sponsors" style="text-align: center;">

<div id="silver-sponsors"><b>Silver sponsors</b><p>
<a href="https://fastapi.tiangolo.com/"><img alt="FastAPI" src="https://raw.githubusercontent.com/tiangolo/fastapi/master/docs/en/docs/img/logo-margin/logo-teal.png" style="height: 200px; "></a><br>
</p></div>

<div id="bronze-sponsors"><b>Bronze sponsors</b><p>
<a href="https://www.nixtla.io/"><picture><source media="(prefers-color-scheme: light)" srcset="https://www.nixtla.io/img/logo/full-black.svg"><source media="(prefers-color-scheme: dark)" srcset="https://www.nixtla.io/img/logo/full-white.svg"><img alt="Nixtla" src="https://www.nixtla.io/img/logo/full-black.svg" style="height: 60px; "></picture></a><br>
</p></div>
</div>

---

<div id="sponsors"><p>
<a href="https://github.com/ofek"><img alt="ofek" src="https://avatars.githubusercontent.com/u/9677399?u=386c330f212ce467ce7119d9615c75d0e9b9f1ce&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/samuelcolvin"><img alt="samuelcolvin" src="https://avatars.githubusercontent.com/u/4039449?u=42eb3b833047c8c4b4f647a031eaef148c16d93f&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/tlambert03"><img alt="tlambert03" src="https://avatars.githubusercontent.com/u/1609449?u=922abf0524b47739b37095e553c99488814b05db&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/ssbarnea"><img alt="ssbarnea" src="https://avatars.githubusercontent.com/u/102495?u=c7bd9ddf127785286fc939dd18cb02db0a453bce&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/femtomc"><img alt="femtomc" src="https://avatars.githubusercontent.com/u/34410036?u=f13a71daf2a9f0d2da189beaa94250daa629e2d8&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/cmarqu"><img alt="cmarqu" src="https://avatars.githubusercontent.com/u/360986?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/kolenaIO"><img alt="kolenaIO" src="https://avatars.githubusercontent.com/u/77010818?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/ramnes"><img alt="ramnes" src="https://avatars.githubusercontent.com/u/835072?u=3fca03c3ba0051e2eb652b1def2188a94d1e1dc2&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/machow"><img alt="machow" src="https://avatars.githubusercontent.com/u/2574498?u=c41e3d2f758a05102d8075e38d67b9c17d4189d7&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/BenHammersley"><img alt="BenHammersley" src="https://avatars.githubusercontent.com/u/99436?u=4499a7b507541045222ee28ae122dbe3c8d08ab5&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/trevorWieland"><img alt="trevorWieland" src="https://avatars.githubusercontent.com/u/28811461?u=74cc0e3756c1d4e3d66b5c396e1d131ea8a10472&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/MarcoGorelli"><img alt="MarcoGorelli" src="https://avatars.githubusercontent.com/u/33491632?u=7de3a749cac76a60baca9777baf71d043a4f884d&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/analog-cbarber"><img alt="analog-cbarber" src="https://avatars.githubusercontent.com/u/7408243?u=fe0e7bf2882d1c9c901a341c2502e1518466527a&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/OdinManiac"><img alt="OdinManiac" src="https://avatars.githubusercontent.com/u/22727172?u=36ab20970f7f52ae8e7eb67b7fcf491fee01ac22&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/rstudio-sponsorship"><img alt="rstudio-sponsorship" src="https://avatars.githubusercontent.com/u/58949051?u=0c471515dd18111be30dfb7669ed5e778970959b&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/schlich"><img alt="schlich" src="https://avatars.githubusercontent.com/u/21191435?u=6f1240adb68f21614d809ae52d66509f46b1e877&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/butterlyn"><img alt="butterlyn" src="https://avatars.githubusercontent.com/u/53323535?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/livingbio"><img alt="livingbio" src="https://avatars.githubusercontent.com/u/10329983?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/NemetschekAllplan"><img alt="NemetschekAllplan" src="https://avatars.githubusercontent.com/u/912034?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/EricJayHartman"><img alt="EricJayHartman" src="https://avatars.githubusercontent.com/u/9259499?u=7e58cc7ec0cd3e85b27aec33656aa0f6612706dd&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/15r10nk"><img alt="15r10nk" src="https://avatars.githubusercontent.com/u/44680962?u=f04826446ff165742efa81e314bd03bf1724d50e&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/activeloopai"><img alt="activeloopai" src="https://avatars.githubusercontent.com/u/34816118?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/roboflow"><img alt="roboflow" src="https://avatars.githubusercontent.com/u/53104118?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/cmclaughlin"><img alt="cmclaughlin" src="https://avatars.githubusercontent.com/u/1061109?u=ddf6eec0edd2d11c980f8c3aa96e3d044d4e0468&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/RapidataAI"><img alt="RapidataAI" src="https://avatars.githubusercontent.com/u/104209891?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/rodolphebarbanneau"><img alt="rodolphebarbanneau" src="https://avatars.githubusercontent.com/u/46493454?u=6c405452a40c231cdf0b68e97544e07ee956a733&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/theSymbolSyndicate"><img alt="theSymbolSyndicate" src="https://avatars.githubusercontent.com/u/111542255?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/blakeNaccarato"><img alt="blakeNaccarato" src="https://avatars.githubusercontent.com/u/20692450?u=bb919218be30cfa994514f4cf39bb2f7cf952df4&v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/ChargeStorm"><img alt="ChargeStorm" src="https://avatars.githubusercontent.com/u/26000165?v=4" style="height: 32px; border-radius: 100%;"></a>
<a href="https://github.com/Cusp-AI"><img alt="Cusp-AI" src="https://avatars.githubusercontent.com/u/178170649?v=4" style="height: 32px; border-radius: 100%;"></a>
</p></div>


*And 4 more private sponsor(s).*

<!-- sponsors-end -->


---

## 52. toml
- **URL:** https://github.com/devtechedge/toml
- **Language:** Rust
- **Topics:** None
- **Description:** Rust TOML Parser

### README.md

This repo contains:
- [`toml` crate](./crates/toml) for serde support
- [`toml_edit` crate](./crates/toml_edit) for format-preserving editing of TOML
- [`toml_datetime` crate](./crates/toml_datetime) for a common type definition between `toml` and `toml_edit`
- [`serde_spanned` crate](./crates/serde_spanned) for capturing spans when deserializing keys and values
- [`toml_parser` crate](./crates/toml_parser): a low-level format-preserving TOML lexer and parser
- [`toml_writer` crate](./crates/toml_writer): a low-level interface for writing out TOML


---

## 53. difftastic
- **URL:** https://github.com/devtechedge/difftastic
- **Language:** Rust
- **Topics:** None
- **Description:** a structural diff that understands syntax ≡ƒƒÑ≡ƒƒ⌐

### README.md

<p align="center">
  <a href="#readme"><img src="img/logo.png" alt="it's difftastic!"/></a>
  <br>
  <a href="https://difftastic.wilfred.me.uk/introduction.html"><img src="https://img.shields.io/badge/manual-en-brightgreen?style=plastic" alt="English manual"></a>
  <a href="https://difftastic.wilfred.me.uk/zh-CN/"><img src="https://img.shields.io/badge/manual-zh--CN-brightgreen?style=plastic" alt="Chinese manual"></a>
  <a href="https://crates.io/crates/difftastic"><img src="https://img.shields.io/crates/v/difftastic.svg?style=plastic" alt="crates.io"></a>
  <a href="https://codecov.io/gh/Wilfred/difftastic"><img src="https://img.shields.io/codecov/c/github/Wilfred/difftastic?style=plastic&token=dZzAZtQT2S" alt="codecov.io"></a>
</p>

Difftastic is a structural diff tool that compares files based on
their syntax.

**For installation instructions, see
[Installation](https://difftastic.wilfred.me.uk/installation.html) in
[the manual](https://difftastic.wilfred.me.uk/).**

## Examples

![Screenshot of difftastic and Rust](img/wrap_expr.png)

^ Difftastic understands exactly which pieces of syntax have changed,
and can highlight them in context.

![Screenshot of difftastic and HTML](img/html.png)

^ Difftastic understands when whitespace matters, and when it's just
an indentation change.

![Screenshot of difftastic and JS](img/reformat.png)

^ Difftastic is not line-oriented. If you reformat your code and it's
now split over multiple lines, difftastic will show you what's
actually changed.

![Screenshot of difftastic and git](img/git.png)

^ Difftastic is compatible with git (see [the configuration
instructions](https://difftastic.wilfred.me.uk/git.html)), as well as
many other version control systems.

## Languages Supported

Difftastic supports over 30 programming languages, see [the
manual](https://difftastic.wilfred.me.uk/languages_supported.html) for the full list.

If a file has an unrecognised extension, difftastic uses a
line-oriented diff with word highlighting.

## Known Issues

Performance. Difftastic scales relatively poorly on files with a large
number of changes, and can use a lot of memory.

Display. Difftastic has a side-by-side display which usually works well, but can
be confusing.

Robustness. Difftastic regularly has releases that fix crashes.

## Non-goals

Patching. Difftastic output is intended for human consumption, and it
does not generate patches that you can apply later. Use `diff` if you
need a patch.

(Patch files are also line-oriented, which is too limited for
difftastic. Difftastic might find additions and removals on the same
line, and it tracks the relationship between line numbers in the old
and new file.)

Merging. AST merging is a hard problem that difftastic does not
address. You might be interested in the [mergiraf
tool](https://mergiraf.org/) ("merge giraffe"), which does do AST
merging.

## FAQ

### Can I use difftastic with git?

You can! The difftastic manual [includes instructions for git
usage](https://difftastic.wilfred.me.uk/git.html). You can also use it
[with mercurial](https://difftastic.wilfred.me.uk/mercurial.html).

If you're an Emacs user, check out [this blog
post](https://tsdh.org/posts/2022-08-01-difftastic-diffing-with-magit.html)
showing one way to use difftastic with magit, as well as
[difftastic.el](https://github.com/pkryger/difftastic.el).

### Does difftastic integrate with my favourite tool?

Probably not. Difftastic is young. Consider writing a plugin for your
favourite tool, and I will link it in the README!

### What about parse errors?

By default, difftastic falls back to a line-oriented diff whenever
parse errors are encountered.

This is a conservative choice to ensure that difftastic never claims
that two syntactically different files are the same.

Parse errors can occur if the file uses language features that the
parser does not understand, if the language relies on a preprocessor
before parsing (e.g. C++), or if the file has genuine syntactic
mistakes.

In practice, difftastic virtually always produces a good result when
there are a few minor parse errors. Consider allowing a small number
of parse errors when using difftastic.

```
$ export DFT_PARSE_ERROR_LIMIT=20
$ difft foo1.c foo2.c
```

### Can difftastic help me with merge conflicts?

Yes! As of version 0.50 (released 2023-08-16), difftastic understands merge conflict markers
(i.e. `<<<<<<<`, `=======` and `>>>>>>>`).

Pass your file with conflicts as a single argument to
difftastic. Difftastic will construct the two conflicting files and
diff those.

```
$ difft file_with_conflicts.js
```

### Can difftastic do merges?

No. AST merging is a hard problem that difftastic does not address.

AST diffing is a lossy process from the perspective of a text
diff. Difftastic will ignore whitespace that isn't syntactically
significant, but merging requires tracking whitespace.

The [mergiraf](https://mergiraf.org/) tool does offer merges based on
a tree-sitter AST however.

### Can difftastic ignore reordering?

No. Difftastic always considers order to be important, so diffing
e.g. `set(1, 2)` and `set(2, 1)` will show changes.

If you're diffing JSON, consider sorting the keys before passing them
to difftastic.

```
$ difft <(jq --sort-keys < file_1.json) <(jq --sort-keys < file_2.json)
```

See also [Tricky Cases: Unordered Data
Types](https://difftastic.wilfred.me.uk/tricky_cases.html#unordered-data-types)
in the manual.

### Can I use difftastic to check for syntactic changes without diffing?

Yes. Difftastic can check if the two files have the same AST, without
calculating a diff. This is much faster than normal diffing, and
useful for building tools that check for changes.

For example:

```
$ difft --check-only --exit-code before.js after.js
```

This will set the exit code to 0 if there are no syntactic changes, or
1 if there are changes found.

### Why aren't colours appearing in my terminal?

Difftastic uses ANSI bright colours by default, but some terminal
themes show bright colours as grey. Solarized is a popular theme that
does this.

If you're a Solarized user, use `export DFT_BACKGROUND=light` to
disable bright colours, or try a different terminal colour scheme.

### How does it work?

Difftastic treats structural diffing as a graph problem, and uses
Dijkstra's algorithm.

My [blog
post](https://www.wilfred.me.uk/blog/2022/09/06/difftastic-the-fantastic-diff/)
describes the design, and there is also an [internals section in the
manual](https://difftastic.wilfred.me.uk/diffing.html).

## Translation

+ [Chinese](./translation/zh-CN/README-zh-CN.md)

## License

Difftastic is open source under the MIT license, see LICENSE for more
details.

This repository also includes tree-sitter parsers by other authors in
the `vendored_parsers/` directory. These are a mix of the MIT license and the
Apache license. See `vendored_parsers/*/LICENSE` for more details.

Files in `sample_files/` are also under the MIT license unless stated
otherwise in their headers.


---

## 54. hatch
- **URL:** https://github.com/devtechedge/hatch
- **Language:** Python
- **Topics:** None
- **Description:** Modern, extensible Python project management

### README.md

# Hatch

<div align="center">

<img src="https://raw.githubusercontent.com/pypa/hatch/master/docs/assets/images/logo.svg" alt="Hatch logo" width="500" role="img">

| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/pypa/hatch/actions/workflows/test.yml/badge.svg)](https://github.com/pypa/hatch/actions/workflows/test.yml) [![CD - Build Hatch](https://github.com/pypa/hatch/actions/workflows/build-hatch.yml/badge.svg)](https://github.com/pypa/hatch/actions/workflows/build-hatch.yml) [![CD - Build Hatchling](https://github.com/pypa/hatch/actions/workflows/build-hatchling.yml/badge.svg)](https://github.com/pypa/hatch/actions/workflows/build-hatchling.yml) |
| Docs | [![Docs - Release](https://github.com/pypa/hatch/actions/workflows/docs-release.yml/badge.svg)](https://github.com/pypa/hatch/actions/workflows/docs-release.yml) [![Docs - Dev](https://github.com/pypa/hatch/actions/workflows/docs-dev.yml/badge.svg)](https://github.com/pypa/hatch/actions/workflows/docs-dev.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/hatch.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/hatch/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/hatch/) [![PyPI - Installs](https://img.shields.io/pypi/dm/hatchling.svg?color=blue&label=Installs&logo=pypi&logoColor=gold)](https://pypi.org/project/hatch/) [![Release - Downloads](https://img.shields.io/github/downloads/pypa/hatch/total?label=Downloads)](https://github.com/pypa/hatch/releases) |
| Meta | [![Hatch project](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pypa/hatch/master/docs/assets/badge/v0.json)](https://github.com/pypa/hatch) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/ofek?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/ofek) |

</div>

-----

Hatch is a modern, extensible Python project manager.

## Features

- Standardized [build system](https://hatch.pypa.io/latest/config/build/#build-system) with reproducible builds by default
- Robust [environment management](https://hatch.pypa.io/latest/environment/) with support for custom scripts and UV
- Configurable [Python distribution management](https://hatch.pypa.io/latest/tutorials/python/manage/)
- [Test execution](https://hatch.pypa.io/latest/tutorials/testing/overview/) with known best practices
- [Static analysis](https://hatch.pypa.io/latest/config/static-analysis/) with sane defaults
- Built-in Python [script runner](https://hatch.pypa.io/latest/how-to/run/python-scripts/)
- Easy [publishing](https://hatch.pypa.io/latest/publish/) to PyPI or other indices
- [Version](https://hatch.pypa.io/latest/version/) management
- Best practice [project generation](https://hatch.pypa.io/latest/config/project-templates/)
- Responsive [CLI](https://hatch.pypa.io/latest/cli/about/), ~2-3x [faster](https://github.com/pypa/hatch/actions/workflows/cli.yml) than equivalent tools

See the [Why Hatch?](https://hatch.pypa.io/latest/why/) page for more information.

## Documentation

The [documentation](https://hatch.pypa.io/) is made with [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) and is hosted by [GitHub Pages](https://docs.github.com/en/pages).

## License

Hatch is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


---

## 55. pydantic-ai
- **URL:** https://github.com/devtechedge/pydantic-ai
- **Language:** Python
- **Topics:** None
- **Description:** How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.

### README.md

<div align="center">
  <a href="https://pydantic.dev/docs/ai/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://pydantic.dev/docs/ai/img/pydantic-ai-dark.svg">
      <img src="https://pydantic.dev/docs/ai/img/pydantic-ai-light.svg" alt="Pydantic AI">
    </picture>
  </a>
</div>
<div align="center">
  <h3>How Python does AI</h3>
</div>
<div align="center">
  <a href="https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml/badge.svg?event=push" alt="CI"></a>
  <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/pydantic/pydantic-ai"><img src="https://img.shields.io/badge/coverage-100%25-brightgreen.svg" alt="Coverage"></a>
  <a href="https://pypi.python.org/pypi/pydantic-ai"><img src="https://img.shields.io/pypi/v/pydantic-ai.svg" alt="PyPI"></a>
  <a href="https://github.com/pydantic/pydantic-ai"><img src="https://img.shields.io/pypi/pyversions/pydantic-ai.svg" alt="versions"></a>
  <a href="https://github.com/pydantic/pydantic-ai/blob/main/LICENSE"><img src="https://img.shields.io/github/license/pydantic/pydantic-ai.svg?v" alt="license"></a>
  <a href="https://logfire.pydantic.dev/docs/join-slack/"><img src="https://img.shields.io/badge/Slack-Join%20Slack-4A154B?logo=slack" alt="Join Slack" /></a>
</div>
<p align="center">
  Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.
</p>

---

**Pydantic AI** is the Python AI SDK: a typed, [extensible](https://pydantic.dev/docs/ai/guides/extensibility/) agent loop with [every model](https://pydantic.dev/docs/ai/models/overview/) a string swap away. The same agent [runs everywhere you need it](https://pydantic.dev/docs/ai/overview/interfaces/): behind a [web frontend](https://pydantic.dev/docs/ai/integrations/ui/overview/), in the [terminal](https://pydantic.dev/docs/ai/integrations/cli/), on a [voice call](https://pydantic.dev/docs/ai/realtime/overview/), on a [durable background queue](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/), or as a plain object you call [`run()`](https://pydantic.dev/docs/ai/core-concepts/agent/#running-agents) on. [Image generation](https://pydantic.dev/docs/ai/guides/image-generation/) and [embeddings](https://pydantic.dev/docs/ai/guides/embeddings/) come in the same box.

**[Pydantic AI Harness](https://github.com/pydantic/pydantic-ai-harness)** has everything an agent needs for complex, long-running work, snapped on as [capabilities](https://pydantic.dev/docs/ai/capabilities/overview/), from [memory](https://pydantic.dev/docs/ai/harness/memory/), [sub-agents](https://pydantic.dev/docs/ai/harness/subagents/), and [context management](https://pydantic.dev/docs/ai/harness/compaction/) to a complete [coding agent](https://pydantic.dev/docs/ai/harness/coder/).

View the complete documentation at [pydantic.dev/docs/ai](https://pydantic.dev/docs/ai/).

## What are you building?

From simple typed data extraction to complex, long-running multi-agent collaboration, Pydantic AI and [Pydantic AI Harness](https://github.com/pydantic/pydantic-ai-harness) have got you covered.

### Coding agent

A complete coding agent in your terminal: workspace-rooted [file access](https://pydantic.dev/docs/ai/harness/filesystem/), allowlisted [shell](https://pydantic.dev/docs/ai/harness/shell/), [repo orientation](https://pydantic.dev/docs/ai/harness/repo-context/), [planning](https://pydantic.dev/docs/ai/harness/planning/), and [context management](https://pydantic.dev/docs/ai/harness/compaction/) that survives long sessions. Here with [web search](https://pydantic.dev/docs/ai/capabilities/web-search/) and a second-opinion [advisor](https://pydantic.dev/docs/ai/harness/advisor/) snapped on alongside:

```bash
uv add pydantic-ai pydantic-ai-harness
```

```python
from pydantic_ai import Agent
from pydantic_ai.capabilities import WebSearch
from pydantic_ai_harness import Advisor, Coder

agent = Agent(
    'anthropic:claude-fable-5',
    capabilities=[
        Coder(),  # files, shell, repo context, planning, sub-agents, context management
        WebSearch(),  # look up docs and error messages on the web
        Advisor('openai:gpt-5.6-sol'),  # a second opinion from another model when stuck
    ],
)
agent.to_cli_sync()
```

[`Coder`](https://pydantic.dev/docs/ai/harness/coder/) is a regular [combined capability](https://pydantic.dev/docs/ai/capabilities/custom/#composition-and-middleware-semantics), not a black box: use it whole, or use the blocks it bundles directly; the two are equivalent:

```python
capabilities = [
    FileSystem('.'), Shell(cwd='.'), RepoContext(), Planning(), SubAgents(...),
    ClearToolResults(), WarnNearLimits(), ToolOutputLimits(),
]
```

Run the file and you're chatting with the agent in your terminal. To try it before writing any code, run the exported [`coder_agent`](https://pydantic.dev/docs/ai/harness/coder/) with [`clai`](https://pydantic.dev/docs/ai/integrations/cli/#custom-agents) (the Pydantic AI CLI), via [`uvx`](https://docs.astral.sh/uv/guides/tools/):

```bash
uvx --with pydantic-ai-harness clai -a pydantic_ai_harness.coder:coder_agent -m anthropic:claude-fable-5
```

**Build this →** [Coder](https://pydantic.dev/docs/ai/harness/coder/), from the [Harness](https://pydantic.dev/docs/ai/harness/)

### Data extraction

Give the agent an [output type](https://pydantic.dev/docs/ai/core-concepts/output/) and [tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/), and every run comes back validated and typed:

```bash
uv add pydantic-ai
```

```python
from typing import Literal

from pydantic import BaseModel, Field

from pydantic_ai import Agent, RunContext


class Sentiment(BaseModel):
    label: Literal['positive', 'negative', 'neutral']
    score: float = Field(ge=-1, le=1)


agent = Agent('openai:gpt-5.6-sol', output_type=Sentiment)


@agent.tool
def recent_reviews(ctx: RunContext[None], product: str) -> list[str]:
    """Fetch recent review snippets for a product."""
    return ['The new release fixed everything I complained about!']


result = agent.run_sync('How are people feeling about the Extract app?')
print(result.output)
#> label='positive' score=0.9
```

The [`@agent.tool`](https://pydantic.dev/docs/ai/tools-toolsets/tools/) function receives a [`RunContext`](https://pydantic.dev/docs/ai/core-concepts/dependencies/) that carries your dependencies in; the rest of its signature and its docstring become the tool schema, arguments are validated before your code runs, and the run is guaranteed to return a `Sentiment`, so your IDE, type checker, and the LLM all agree on the returned type.

**Build this →** [Agents](https://pydantic.dev/docs/ai/core-concepts/agent/), [Function Tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/), and [Structured Output](https://pydantic.dev/docs/ai/core-concepts/output/)

### Durable workflow

Attach [`TemporalDurability`](https://pydantic.dev/docs/ai/capabilities/durable_execution/temporal/) and the same agent runs inside a [Temporal](https://pydantic.dev/docs/ai/capabilities/durable_execution/temporal/) workflow under [durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/): every model and tool call becomes a durable activity, so a run working through a background queue survives restarts, failures, and long waits:

```bash
uv add "pydantic-ai[temporal]"
```

```python
from temporalio import workflow

from pydantic_ai import Agent
from pydantic_ai.capabilities import WebFetch, WebSearch
from pydantic_ai.durable_exec.temporal import PydanticAIWorkflow, TemporalDurability

agent = Agent(
    'openai:gpt-5.6-sol',
    instructions='Research the topic and write a structured brief.',
    name='researcher',
    capabilities=[WebSearch(), WebFetch(), TemporalDurability()],
)


@workflow.defn
class ResearchWorkflow(PydanticAIWorkflow):
    __pydantic_ai_agents__ = [agent]

    @workflow.run
    async def run(self, topic: str) -> str:
        result = await agent.run(f'Write a brief on: {topic}')
        return result.output
```

[DBOS](https://pydantic.dev/docs/ai/capabilities/durable_execution/dbos/) and [Prefect](https://pydantic.dev/docs/ai/capabilities/durable_execution/prefect/) attach the same way, first-party and co-maintained, with [Restate, Kitaru, and Airflow](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) integrations besides.

**Build this →** [Durable Execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/)

### Realtime voice

Put the same agent on a live voice session, [tools](https://pydantic.dev/docs/ai/realtime/tools/) and [capabilities](https://pydantic.dev/docs/ai/realtime/capabilities/) included:

```bash
uv add "pydantic-ai[openai-realtime]"
```

```python
import asyncio

from pydantic_ai import Agent
from pydantic_ai.capabilities import MCP

agent = Agent(
    instructions='You are a helpful voice assistant.',
    capabilities=[MCP('https://internal.example.com/mcp')],  # capabilities work in voice too
)

@agent.tool_plain
def order_status(order_id: str) -> str:
    """Look up the status of an order."""
    return f'Order {order_id}: shipped, arriving Thursday.'

async with agent.realtime('openai:gpt-realtime-2.1').session() as session:
    microphone = asyncio.create_task(session.send_audio(microphone_chunks()))  # your microphone → the model
    speaker = asyncio.create_task(play_audio(session.stream_audio()))  # model audio → your speaker
    async for part in session.stream_transcripts():
        print(f'{part.speaker}: {part.transcript}')
```

The model calls your tools mid-conversation while it keeps talking, and every session is [instrumented](https://pydantic.dev/docs/ai/integrations/logfire/); voice is just another frontend, on OpenAI Realtime, Gemini Live, Azure, and xAI Grok Voice.

**Build this →** [Realtime Voice](https://pydantic.dev/docs/ai/realtime/overview/)

### Image generation

Generate an image with a dedicated image model, no agent run required:

```bash
uv add pydantic-ai
```

```python
from pathlib import Path

from pydantic_ai import ImageGenerator

generator = ImageGenerator('openai:gpt-image-2')
result = generator.generate_sync('A minimalist logo for a coffee shop called Extract.')
Path('logo.png').write_bytes(result.image.data)
```

That [standalone image API](https://pydantic.dev/docs/ai/guides/image-generation/) is for when your application decides; when an agent run decides, there is [provider-native generation](https://pydantic.dev/docs/ai/tools-toolsets/native-tools/#image-generation-tool) with `output_type=BinaryImage` for a typed image [output](https://pydantic.dev/docs/ai/core-concepts/output/#image-output), and the [`ImageGeneration` capability](https://pydantic.dev/docs/ai/capabilities/image-generation/) with its fallbacks for models that generate no images of their own.

**Build this →** [Image Generation](https://pydantic.dev/docs/ai/guides/image-generation/)

## Why Pydantic AI

- **Any model, one Python API.** [Virtually every model and provider](https://pydantic.dev/docs/ai/models/overview/) (OpenAI, Anthropic, Google, Bedrock, Azure AI Foundry, Groq, Mistral, xAI, Ollama, and dozens more), swappable with a string, or through the [Pydantic AI Gateway](https://pydantic.dev/docs/ai/overview/gateway/): one key for all of them, with failover and cost monitoring built in. No flagship feature is locked to one vendor.

- **Typed end to end.** [Structured outputs](https://pydantic.dev/docs/ai/core-concepts/output/), typed [dependency injection](https://pydantic.dev/docs/ai/core-concepts/dependencies/), [typed tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/): your IDE, type checker, and coding agent all know what your agent returns, moving whole classes of errors from runtime to write-time. When plain control flow isn't enough, [Pydantic Graph](https://pydantic.dev/docs/ai/graph/graph/) brings the same typing to graph-based workflows.

- **Measured, not vibes.** OpenTelemetry-native [instrumentation](https://pydantic.dev/docs/ai/integrations/logfire/) works with any OTel backend; one line lights up [Pydantic Logfire](https://pydantic.dev/logfire/llm-observability?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai) for real-time debugging, tracing, and cost tracking backed by [genai-prices](https://github.com/pydantic/genai-prices). [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) tests agent behavior the way pytest tests code.

- **Batteries, composably.** One primitive, the [capability](https://pydantic.dev/docs/ai/capabilities/overview/), bundles [tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/), [instructions](https://pydantic.dev/docs/ai/core-concepts/agent/#instructions), [hooks](https://pydantic.dev/docs/ai/core-concepts/hooks/), and [model settings](https://pydantic.dev/docs/ai/core-concepts/agent/#model-run-settings) into reusable units. Core ships fundamentals like [MCP](https://pydantic.dev/docs/ai/capabilities/mcp/) and [web search](https://pydantic.dev/docs/ai/capabilities/web-search/), the [Harness](https://github.com/pydantic/pydantic-ai-harness) ships everything else, and complete agents like [Coder](https://pydantic.dev/docs/ai/harness/coder/) and [Researcher](https://pydantic.dev/docs/ai/harness/researcher/) are just capabilities composed: they come apart the way they went together. Or skip code entirely with [YAML/JSON agent specs](https://pydantic.dev/docs/ai/core-concepts/agent-spec/).

- **[Every interface](https://pydantic.dev/docs/ai/overview/interfaces/).** One agent definition runs as a [CLI](https://pydantic.dev/docs/ai/integrations/cli/), a [built-in web chat](https://pydantic.dev/docs/ai/guides/web/), or [realtime speech](https://pydantic.dev/docs/ai/realtime/overview/) (OpenAI Realtime, Gemini Live, Azure, xAI Grok Voice); [UI event streams](https://pydantic.dev/docs/ai/integrations/ui/overview/) (AG-UI, Vercel AI) connect it to your own frontend or anything else; and [ACP](https://pydantic.dev/docs/ai/harness/acp/) *(experimental)* serves it as an editor agent.

- **Durable execution.** First-party, co-maintained [durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) on Temporal, DBOS, Prefect, and Restate, plus external SDK integrations for Kitaru and Airflow. Agents survive restarts and run for days on the engine you already operate, with [human-in-the-loop approval](https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools/#human-in-the-loop-tool-approval) built in.

Built by the [Pydantic](https://docs.pydantic.dev) team: [Pydantic Validation](https://pydantic.dev/docs/) is the validation layer of the OpenAI SDK, the Anthropic SDK, the Google ADK, LangChain, and most of the AI ecosystem (and the foundation FastAPI was built on). Pydantic AI brings that same feeling to agents.

## Putting it together: a bank support agent

A typed support agent showing several features working together: [dependency injection](https://pydantic.dev/docs/ai/core-concepts/dependencies/), [function tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/), [structured output](https://pydantic.dev/docs/ai/core-concepts/output/), a reusable [capability](https://pydantic.dev/docs/ai/capabilities/overview/) bundling the customer context, and an [on-demand capability](https://pydantic.dev/docs/ai/capabilities/on-demand/) the model loads only when the conversation calls for it:

```python
from dataclasses import dataclass

from pydantic import BaseModel, Field

from pydantic_ai import Agent, Capability, RunContext

from bank_database import DatabaseConn


@dataclass
class SupportDependencies:  # inject any client: DB pools, HTTP APIs, user info
    customer_id: int
    db: DatabaseConn


class SupportOutput(BaseModel):
    support_advice: str = Field(description='Advice returned to the customer')
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description='Risk level of query', ge=0, le=10)


customer_context = Capability[SupportDependencies](  # a reusable unit of tools + instructions
    id='customer-context',
    description="Who the customer is and what's on their account.",
)


@customer_context.instructions
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
    return f"The customer's name is {customer_name!r}"


@customer_context.tool  # signature and docstring become the tool schema the LLM sees
async def customer_balance(
    ctx: RunContext[SupportDependencies], include_pending: bool
) -> float:
    """Returns the customer's current account balance."""
    return await ctx.deps.db.customer_balance(
        id=ctx.deps.customer_id,
        include_pending=include_pending,
    )


refunds = Capability[SupportDependencies](  # deferred: loads on demand, like a skill
    id='refunds',
    description='Refund eligibility and refund status.',
    defer_loading=True,
)


@refunds.tool
async def refund_status(ctx: RunContext[SupportDependencies]) -> str:
    """Look up the refund status for the customer's most recent charge."""
    return await ctx.deps.db.refund_status(id=ctx.deps.customer_id)


support_agent = Agent(
    'openai:gpt-5.6-sol',
    deps_type=SupportDependencies,
    output_type=SupportOutput,  # the run returns a validated SupportOutput, typed as such
    instructions=(
        'You are a support agent in our bank, give the '
        'customer support and judge the risk level of their query.'
    ),
    capabilities=[customer_context, refunds],
)


...  # in a real use case: more tools, longer instructions


async def main():
    deps = SupportDependencies(customer_id=123, db=DatabaseConn())
    result = await support_agent.run('What is my balance?', deps=deps)
    print(result.output)
    """
    support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1
    """

    result = await support_agent.run('I just lost my card!', deps=deps)
    print(result.output)
    """
    support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
    """

    result = await support_agent.run(  # the model loads `refunds` on demand, then answers
        'Was I refunded for the duplicate charge on my last statement?', deps=deps
    )
    print(result.output)
    """
    support_advice='Good news, John: the duplicate charge on your last statement was refunded on 2026-05-01.' block_card=False risk=1
    """
```

For the annotated walkthrough and Logfire tracing, see the [same example in the docs](https://pydantic.dev/docs/ai/overview/#putting-it-together-a-bank-support-agent).

## Next Steps

- [Install Pydantic AI](https://pydantic.dev/docs/ai/overview/install/) and put your own coding agent to work: install the [Pydantic AI skill](https://pydantic.dev/docs/ai/overview/coding-agent-skills/), point it at the [examples](https://pydantic.dev/docs/ai/examples/setup/) and the [Harness index](https://pydantic.dev/docs/ai/harness/), and tell it what you'd like to build. No API key needed to start (there's a built-in [`'test'` model](https://pydantic.dev/docs/ai/guides/testing/#unit-testing-with-testmodel)).
- Read the [docs](https://pydantic.dev/docs/ai/core-concepts/agent/) and the [API reference](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/).
- Give your agent its batteries: [Pydantic AI Harness](https://github.com/pydantic/pydantic-ai-harness).
- Join [Slack](https://logfire.pydantic.dev/docs/join-slack/) or file an issue on [GitHub](https://github.com/pydantic/pydantic-ai/issues).

## Part of the Pydantic Stack

Everything you need to ship production-grade AI agents:

- [Pydantic AI](https://pydantic.dev/pydantic-ai?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai): the type-safe AI SDK
- [Pydantic AI Harness](https://github.com/pydantic/pydantic-ai-harness): the official capability library and harness, from single capabilities to complete agents
- [Pydantic Logfire](https://pydantic.dev/logfire?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai): AI-first, full-stack observability
- [Logfire AI Gateway](https://pydantic.dev/ai-gateway?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai): unified LLM proxy
- [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/): evaluate any Python function, agents included, with [production evals on Logfire](https://pydantic.dev/logfire/evals?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai)
- [Pydantic Graph](https://pydantic.dev/docs/ai/graph/graph/): typed graph control flow
- [genai-prices](https://github.com/pydantic/genai-prices): model pricing data, kept current


---

## 56. maturin
- **URL:** https://github.com/devtechedge/maturin
- **Language:** Rust
- **Topics:** None
- **Description:** Build and publish crates with pyo3, cffi and uniffi bindings as well as rust binaries as python packages

### README.md

# Maturin

_formerly pyo3-pack_

[![Maturin User Guide](https://img.shields.io/badge/user-guide-brightgreen?logo=readthedocs&style=flat-square)](https://maturin.rs)
[![Crates.io](https://img.shields.io/crates/v/maturin.svg?logo=rust&style=flat-square)](https://crates.io/crates/maturin)
[![PyPI](https://img.shields.io/pypi/v/maturin.svg?logo=python&style=flat-square)](https://pypi.org/project/maturin)
[![discord server](https://img.shields.io/discord/1209263839632424990?logo=discord&style=flat-square)](https://discord.gg/33kcChzH7f)

Build and publish crates with [pyo3, cffi and uniffi bindings](https://maturin.rs/bindings) as well as rust binaries as python packages with minimal configuration.
It supports building wheels for python 3.8+ on Windows, Linux, macOS and FreeBSD, can upload them to [pypi](https://pypi.org/) and has basic PyPy and GraalPy support.

Check out the [User Guide](https://maturin.rs/)!

## Usage

You can either download binaries from the [latest release](https://github.com/PyO3/maturin/releases/latest) or install it with [pipx](https://pypa.github.io/pipx/) or [uv](https://github.com/astral-sh/uv):

```shell
# pipx
pipx install maturin
# uv
uv tool install maturin
```

> [!NOTE]
>
> `pip install maturin` should also work if you don't want to use pipx.

There are three main commands:

- `maturin new` creates a new cargo project with maturin configured.
- `maturin build` builds the wheels and stores them in a folder (`target/wheels` by default), but doesn't upload them. It's recommended to publish packages with [uv](https://github.com/astral-sh/uv) using `uv publish`.
- `maturin develop` builds the crate and installs it as a python module directly in the current virtualenv. Note that while `maturin develop` is faster, it doesn't support all the feature that running `pip install` after `maturin build` supports.

maturin doesn't need extra configuration files and doesn't clash with an existing setuptools-rust configuration.
You can even integrate it with testing tools such as [tox](https://tox.readthedocs.io/en/latest/).
There are examples for the different bindings in the `test-crates` folder.

The name of the package will be the name of the cargo project, i.e. the name field in the `[package]` section of `Cargo.toml`.
The name of the module, which you are using when importing, will be the `name` value in the `[lib]` section (which defaults to the name of the package). For binaries, it's simply the name of the binary generated by cargo.

When using `maturin build` and `maturin develop` commands, you can compile a performance-optimized program by adding the `-r` or `--release` flag.

## Python packaging basics

Python packages come in two formats:
A built form called wheel and source distributions (sdist), both of which are archives.
A wheel can be compatible with any python version, interpreter (cpython and pypy, mainly), operating system and hardware architecture (for pure python wheels),
can be limited to a specific platform and architecture (e.g. when using ctypes or cffi) or to a specific python interpreter and version on a specific architecture and operating system (e.g. with pyo3).

When using `pip install` on a package, pip tries to find a matching wheel and install that. If it doesn't find one, it downloads the source distribution and builds a wheel for the current platform,
which requires the right compilers to be installed. Installing a wheel is much faster than installing a source distribution as building wheels is generally slow.

When you publish a package to be installable with `pip install`, you upload it to [pypi](https://pypi.org/), the official package repository.
For testing, you can use [test pypi](https://test.pypi.org/) instead, which you can use with `pip install --index-url https://test.pypi.org/simple/`.
Note that for [publishing for linux](#manylinux-and-auditwheel), you need to use the manylinux docker container or zig, while for publishing from your repository you can use the [PyO3/maturin-action](https://github.com/PyO3/maturin-action) github action.

## Mixed rust/python projects

To create a mixed rust/python project, create a folder with your module name (i.e. [`lib.name` in Cargo.toml](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#the-name-field)) next to your Cargo.toml and add your python sources there:

```
my-project
├── Cargo.toml
├── my_project
│   ├── __init__.py
│   └── bar.py
├── pyproject.toml
├── README.md
└── src
    └── lib.rs
```

You can specify a different python source directory in `pyproject.toml` by setting `tool.maturin.python-source`, for example

**pyproject.toml**

```toml
[tool.maturin]
python-source = "python"
module-name = "my_project._lib_name"
```

then the project structure would look like this:

```
my-project
├── Cargo.toml
├── python
│   └── my_project
│       ├── __init__.py
│       └── bar.py
├── pyproject.toml
├── README.md
└── src
    └── lib.rs
```

> [!NOTE]
>
> This structure is recommended to avoid [a common `ImportError` pitfall](https://github.com/PyO3/maturin/issues/490)

maturin will add the native extension as a module in your python folder. When using develop, maturin will copy the native library and for cffi also the glue code to your python folder. You should add those files to your gitignore.

With cffi you can do `from .my_project import lib` and then use `lib.my_native_function`, with pyo3 you can directly `from .my_project import my_native_function`.

Example layout with pyo3 after `maturin develop`:

```
my-project
├── Cargo.toml
├── my_project
│   ├── __init__.py
│   ├── bar.py
│   └── _lib_name.cpython-36m-x86_64-linux-gnu.so
├── README.md
└── src
    └── lib.rs
```

When doing this also be sure to set the module name in your code to match the last part of `module-name` (don't include the package path):

```rust
#[pymodule]
#[pyo3(name="_lib_name")]
fn my_lib_name(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<MyPythonRustClass>()?;
    Ok(())
}
```

## Python metadata

maturin supports [PEP 621](https://www.python.org/dev/peps/pep-0621/), you can specify python package metadata in `pyproject.toml`.
maturin merges metadata from `Cargo.toml` and `pyproject.toml`, `pyproject.toml` takes precedence over `Cargo.toml`.

To specify python dependencies, add a list `dependencies` in a `[project]` section in the `pyproject.toml`. This list is equivalent to `install_requires` in setuptools:

```toml
[project]
name = "my-project"
dependencies = ["flask~=1.1.0", "toml>=0.10.2,<0.11.0"]
```

You can add so called console scripts, which are shell commands that execute some function in your program in the `[project.scripts]` section.
The keys are the script names while the values are the path to the function in the format `some.module.path:class.function`, where the `class` part is optional. The function is called with no arguments. Example:

```toml
[project.scripts]
get_42 = "my_project:DummyClass.get_42"
```

You can also specify [trove classifiers](https://pypi.org/classifiers/) in your `pyproject.toml` under `project.classifiers`:

```toml
[project]
name = "my-project"
classifiers = ["Programming Language :: Python"]
```

## Source distribution

maturin supports building through `pyproject.toml`. To use it, create a `pyproject.toml` next to your `Cargo.toml` with the following content:

```toml
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"
```

If a `pyproject.toml` with a `[build-system]` entry is present, maturin can build a source distribution of your package when `--sdist` is specified.
The source distribution will contain the same files as `cargo package`. To only build a source distribution, pass `--interpreter` without any values.

You can then e.g. install your package with `pip install .`. With `pip install . -v` you can see the output of cargo and maturin.

You can use the options `compatibility`, `skip-auditwheel`, `bindings`, `strip` and common Cargo build options such as `features` under `[tool.maturin]` the same way you would when running maturin directly.
The `bindings` key is required for cffi and bin projects as those can't be automatically detected. Currently, all builds are in release mode (see [this thread](https://discuss.python.org/t/pep-517-debug-vs-release-builds/1924) for details).

For a non-manylinux build with cffi bindings you could use the following:

```toml
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"

[tool.maturin]
bindings = "cffi"
compatibility = "linux"
```

`manylinux` option is also accepted as an alias of `compatibility` for backward compatibility with old version of maturin.

To include arbitrary files in the sdist for use during compilation specify `include` as an array of `path` globs with `format` set to `sdist`:

```toml
[tool.maturin]
include = [{ path = "path/**/*", format = "sdist" }]
```

There's a `maturin sdist` command for only building a source distribution as workaround for [pypa/pip#6041](https://github.com/pypa/pip/issues/6041).

## Manylinux and auditwheel

For portability reasons, native python modules on linux must only dynamically link a set of very few libraries which are installed basically everywhere, hence the name manylinux.
The pypa offers special docker images and a tool called [auditwheel](https://github.com/pypa/auditwheel/) to ensure compliance with the [manylinux rules](https://peps.python.org/pep-0599/#the-manylinux2014-policy).
If you want to publish widely usable wheels for linux pypi, **you need to use a manylinux docker image or build with zig**.

The Rust compiler since version 1.64 [requires at least glibc 2.17](https://blog.rust-lang.org/2022/08/01/Increasing-glibc-kernel-requirements.html), so you need to use at least manylinux2014.
For publishing, we recommend enforcing the same manylinux version as the image with the manylinux flag, e.g. use `--manylinux 2014` if you are building in `quay.io/pypa/manylinux2014_x86_64`.
The [PyO3/maturin-action](https://github.com/PyO3/maturin-action) github action already takes care of this if you set e.g. `manylinux: 2014`.

maturin contains a reimplementation of auditwheel automatically checks the generated library and gives the wheel the proper platform tag.
If your system's glibc is too new or you link other shared libraries, it will assign the `linux` tag.
You can also manually disable those checks and directly use native linux target with `--manylinux off`.

For full manylinux compliance you need to compile in a CentOS docker container. The [pyo3/maturin](https://ghcr.io/pyo3/maturin) image is based on the manylinux2014 image,
and passes arguments to the `maturin` binary. You can use it like this:

```
docker run --rm -v $(pwd):/io ghcr.io/pyo3/maturin build --release  # or other maturin arguments
```

Note that this image is very basic and only contains python, maturin and stable rust. If you need additional tools, you can run commands inside the manylinux container.
See [konstin/complex-manylinux-maturin-docker](https://github.com/konstin/complex-manylinux-maturin-docker) for a small educational example or [nanoporetech/fast-ctc-decode](https://github.com/nanoporetech/fast-ctc-decode/blob/b226ea0f2b2f4f474eff47349703d57d2ea4801b/.github/workflows/publish.yml) for a real world setup.

maturin itself is manylinux compliant when compiled for the musl target.

## Examples

- [agg-python-bindings](https://pypi.org/project/agg-python-bindings) - A Python Library that binds to Asciinema Agg terminal record renderer and Avt terminal emulator
- [ballista-python](https://github.com/apache/arrow-ballista-python) - A Python library that binds to Apache Arrow distributed query engine Ballista
- [bleuscore](https://github.com/shenxiangzhuang/bleuscore) - A BLEU score calculation library, written in pure Rust
- [chardetng-py](https://github.com/john-parton/chardetng-py) - Python binding for the chardetng character encoding detector.
- [connector-x](https://github.com/sfu-db/connector-x/tree/main/connectorx-python) - ConnectorX enables you to load data from databases into Python in the fastest and most memory efficient way
- [datafusion-python](https://github.com/apache/arrow-datafusion-python) - a Python library that binds to Apache Arrow in-memory query engine DataFusion
- [deltalake-python](https://github.com/delta-io/delta-rs/tree/main/python) - Native Delta Lake Python binding based on delta-rs with Pandas integration
- [opendal](https://github.com/apache/incubator-opendal/tree/main/bindings/python) - OpenDAL Python Binding to access data freely
- [orjson](https://github.com/ijl/orjson) - A fast, correct JSON library for Python
- [pdfcrate](https://github.com/ratazzi/pdfcrate) - An ergonomic, high-level PDF generation library for Rust and Python — a Prawn-style layout API for composing documents, not low-level PDF plumbing
- [polars](https://github.com/pola-rs/polars/tree/master/py-polars) - Fast multi-threaded DataFrame library in Rust | Python | Node.js
- [pydantic-core](https://github.com/pydantic/pydantic-core) - Core validation logic for pydantic written in Rust
- [pyrus-cramjam](https://github.com/milesgranger/pyrus-cramjam) - Thin Python wrapper to de/compression algorithms in Rust
- [pyxel](https://github.com/kitao/pyxel) - A retro game engine for Python
- [quebec](https://github.com/ratazzi/quebec) - A database-backed background job queue for Python, inspired by Rails' Solid Queue
- [roapi](https://github.com/roapi/roapi) - ROAPI automatically spins up read-only APIs for static datasets without requiring you to write a single line of code
- [robyn](https://github.com/sansyrox/robyn) - A fast and extensible async python web server with a Rust runtime
- [ruff](https://github.com/charliermarsh/ruff) - An extremely fast Python linter, written in Rust
- [rnet](https://github.com/0x676e67/rnet) - Asynchronous Python HTTP Client with Black Magic
- [rustpy-xlsxwriter](https://github.com/rahmadafandi/rustpy-xlsxwriter): A high-performance Python library for generating Excel files, utilizing the [rust_xlsxwriter](https://github.com/jmcnamara/rust_xlsxwriter) crate for efficient data handling.
- [tantivy-py](https://github.com/quickwit-oss/tantivy-py) - Python bindings for Tantivy
- [tpchgen-cli](https://github.com/clflushopt/tpchgen-rs/tree/main/tpchgen-cli) - Python CLI binding for `tpchgen`, a blazing fast TPC-H benchmark data generator built in pure Rust with zero dependencies.
- [watchfiles](https://github.com/samuelcolvin/watchfiles) - Simple, modern and high performance file watching and code reload in python
- [wonnx](https://github.com/webonnx/wonnx/tree/master/wonnx-py) - Wonnx is a GPU-accelerated ONNX inference run-time written 100% in Rust

## Contributing

Everyone is welcomed to contribute to maturin! There are many ways to support the project, such as:

- help maturin users with issues on GitHub and Gitter
- improve documentation
- write features and bugfixes
- publish blogs and examples of how to use maturin

Our [contributing notes](https://github.com/PyO3/maturin/blob/main/guide/src/contributing.md) have more resources if you wish to volunteer time for maturin and are searching where to start.

If you don't have time to contribute yourself but still wish to support the project's future success, some of our maintainers have GitHub sponsorship pages:

- [messense](https://github.com/sponsors/messense)

## License

Licensed under either of:

- Apache License, Version 2.0, ([LICENSE-APACHE](https://github.com/PyO3/maturin/blob/main/license-apache) or http://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](https://github.com/PyO3/maturin/blob/main/license-mit) or http://opensource.org/licenses/MIT)

at your option.


---

## 57. ratatui
- **URL:** https://github.com/devtechedge/ratatui
- **Language:** Rust
- **Topics:** None
- **Description:** A Rust crate for cooking up terminal user interfaces (TUIs) ≡ƒæ¿ΓÇì≡ƒì│≡ƒÉÇ https://ratatui.rs

### README.md

<details>
<summary>Table of Contents</summary>

- [Quickstart](#quickstart)
- [Documentation](#documentation)
- [Templates](#templates)
- [Built with Ratatui](#built-with-ratatui)
- [Alternatives](#alternatives)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

</details>

![Release header](https://github.com/ratatui/ratatui/blob/b23480adfa9430697071c906c7ba4d4f9bd37a73/assets/release-header.png?raw=true)

<div align="center">

[![Crate Badge]][Crate] [![Repo Badge]][Repo] [![Docs Badge]][Docs] [![License Badge]][License]  \
[![CI Badge]][CI] [![Deps Badge]][Deps] [![Codecov Badge]][Codecov] [![Sponsors Badge]][Sponsors]  \
[Ratatui Website] · [Docs] · [Widget Examples] · [App Examples] · [Changelog]  \
[Breaking Changes] · [Contributing] · [Report a bug] · [Request a Feature]

</div>

[Ratatui][Ratatui Website] (_ˌræ.təˈtu.i_) is a Rust crate for cooking up terminal user interfaces
(TUIs). It provides a simple and flexible way to create text-based user interfaces in the terminal,
which can be used for command-line applications, dashboards, and other interactive console programs.

## Quickstart

Ratatui has [templates] available to help you get started quickly. You can use the
[`cargo-generate`] command to create a new project with Ratatui:

```shell
cargo install --locked cargo-generate
cargo generate ratatui/templates
```

Selecting the Hello World template produces the following application:

```rust
use color_eyre::Result;
use crossterm::event::{self, Event};
use ratatui::{DefaultTerminal, Frame};

fn main() -> Result<()> {
    color_eyre::install()?;
    let terminal = ratatui::init();
    let result = run(terminal);
    ratatui::restore();
    result
}

fn run(mut terminal: DefaultTerminal) -> Result<()> {
    loop {
        terminal.draw(render)?;
        if matches!(event::read()?, Event::Key(_)) {
            break Ok(());
        }
    }
}

fn render(frame: &mut Frame) {
    frame.render_widget("hello world", frame.area());
}
```

## Documentation

- [Docs] - the full API documentation for the library on docs.rs.
- [Ratatui Website] - explains the library's concepts and provides step-by-step tutorials.
- [Ratatui Forum] - a place to ask questions and discuss the library.
- [Widget Examples] - a collection of examples that demonstrate how to use the library.
- [App Examples] - a collection of more complex examples that demonstrate how to build apps.
- [ARCHITECTURE.md] - explains the crate organization and modular workspace structure.
- [Changelog] - generated by [git-cliff] utilizing [Conventional Commits].
- [Breaking Changes] - a list of breaking changes in the library.

You can also watch the [EuroRust 2024 talk] to learn about common concepts in Ratatui and what's
possible to build with it.

## Templates

If you're looking to get started quickly, you can use one of the available templates from the
[templates] repository using [`cargo-generate`]:

```shell
cargo generate ratatui/templates
```

## Built with Ratatui

[![Awesome](https://awesome.re/badge-flat2.svg)][awesome-ratatui]

Check out the [showcase] section of the website, or the [awesome-ratatui] repository for a curated
list of awesome apps and libraries built with Ratatui!

## Alternatives

- [Cursive](https://crates.io/crates/cursive) - a ncurses-based TUI library.
- [iocraft](https://crates.io/crates/iocraft) - a declarative TUI library.

## Contributing

[![Discord Badge]][Discord Server] [![Matrix Badge]][Matrix] [![Forum Badge]][Ratatui Forum]

Feel free to join our [Discord server](https://discord.gg/pMCEU9hNEj) for discussions and questions!
There is also a [Matrix](https://matrix.org/) bridge available at
[#ratatui:matrix.org](https://matrix.to/#/#ratatui:matrix.org). We have also recently launched the
[Ratatui Forum].

We rely on GitHub for [bugs][Report a bug] and [feature requests][Request a Feature].

Please make sure you read the [contributing](./CONTRIBUTING.md) guidelines before [creating a pull
request][Create a Pull Request]. We accept AI generated code, but please read the [AI Contributions]
guidelines to ensure compliance.

If you'd like to show your support, you can add the Ratatui badge to your project's README:

```md
[![Built With Ratatui](https://img.shields.io/badge/Built_With_Ratatui-000?logo=ratatui&logoColor=fff)](https://ratatui.rs/)
```

[![Built With Ratatui](https://img.shields.io/badge/Built_With_Ratatui-000?logo=ratatui&logoColor=fff)](https://ratatui.rs/)

## Acknowledgements

Ratatui was forked from the [tui-rs] crate in 2023 in order to continue its development. None of
this could be possible without [Florian Dehau] who originally created [tui-rs] which inspired many
Rust TUIs.

Special thanks to [Pavel Fomchenkov] for his work in designing an awesome logo for the Ratatui
project and organization.

## License

This project is licensed under the [MIT License][License].

[Repo]: https://github.com/ratatui/ratatui
[Ratatui Website]: https://ratatui.rs/
[Ratatui Forum]: https://forum.ratatui.rs
[Docs]: https://docs.rs/ratatui
[Widget Examples]: https://github.com/ratatui/ratatui/tree/main/ratatui-widgets/examples
[App Examples]: https://github.com/ratatui/ratatui/tree/main/examples
[ARCHITECTURE.md]: https://github.com/ratatui/ratatui/blob/main/ARCHITECTURE.md
[Changelog]: https://github.com/ratatui/ratatui/blob/main/CHANGELOG.md
[git-cliff]: https://git-cliff.org
[Conventional Commits]: https://www.conventionalcommits.org
[Breaking Changes]: https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md
[EuroRust 2024 talk]: https://www.youtube.com/watch?v=hWG51Mc1DlM
[Report a bug]: https://github.com/ratatui/ratatui/issues/new?labels=bug&projects=&template=bug_report.md
[Request a Feature]: https://github.com/ratatui/ratatui/issues/new?labels=enhancement&projects=&template=feature_request.md
[Create a Pull Request]: https://github.com/ratatui/ratatui/compare
[Contributing]: https://github.com/ratatui/ratatui/blob/main/CONTRIBUTING.md
[AI Contributions]: https://github.com/ratatui/ratatui/blob/main/CONTRIBUTING.md#ai-generated-content
[Crate]: https://crates.io/crates/ratatui
[tui-rs]: https://crates.io/crates/tui
[Sponsors]: https://github.com/sponsors/ratatui
[Crate Badge]: https://img.shields.io/crates/v/ratatui?logo=rust&style=flat-square&color=E05D44
[Repo Badge]: https://img.shields.io/badge/repo-ratatui/ratatui-1370D3?style=flat-square&logo=github
[License Badge]: https://img.shields.io/crates/l/ratatui?style=flat-square&color=1370D3
[CI Badge]: https://img.shields.io/github/actions/workflow/status/ratatui/ratatui/ci.yml?style=flat-square&logo=github
[CI]: https://github.com/ratatui/ratatui/actions/workflows/ci.yml
[Codecov Badge]: https://img.shields.io/codecov/c/github/ratatui/ratatui?logo=codecov&style=flat-square&token=BAQ8SOKEST&color=C43AC3
[Codecov]: https://app.codecov.io/gh/ratatui/ratatui
[Deps Badge]: https://deps.rs/repo/github/ratatui/ratatui/status.svg?path=ratatui&style=flat-square
[Deps]: https://deps.rs/repo/github/ratatui/ratatui?path=ratatui
[Discord Badge]: https://img.shields.io/discord/1070692720437383208?label=discord&logo=discord&style=flat-square&color=1370D3&logoColor=1370D3
[Discord Server]: https://discord.gg/pMCEU9hNEj
[Docs Badge]: https://img.shields.io/badge/docs-ratatui-1370D3?style=flat-square&logo=rust
[Matrix Badge]: https://img.shields.io/matrix/ratatui-general%3Amatrix.org?style=flat-square&logo=matrix&label=Matrix&color=C43AC3
[Matrix]: https://matrix.to/#/#ratatui:matrix.org
[Forum Badge]: https://img.shields.io/discourse/likes?server=https%3A%2F%2Fforum.ratatui.rs&style=flat-square&logo=discourse&label=forum&color=C43AC3
[Sponsors Badge]: https://img.shields.io/github/sponsors/ratatui?logo=github&style=flat-square&color=1370D3
[templates]: https://github.com/ratatui/templates/
[showcase]: https://ratatui.rs/showcase/
[awesome-ratatui]: https://github.com/ratatui/awesome-ratatui
[Pavel Fomchenkov]: https://github.com/nawok
[Florian Dehau]: https://github.com/fdehau
[`cargo-generate`]: https://crates.io/crates/cargo-generate
[License]: ./LICENSE


---

## 58. sqlmesh
- **URL:** https://github.com/devtechedge/sqlmesh
- **Language:** Python
- **Topics:** None
- **Description:** Scalable and efficient data transformation framework - backwards compatible with dbt.

### README.md

<p align="center">
  <img src="docs/readme/sqlmesh.png" alt="SQLMesh logo" width="50%" height="50%">
</p>
<p align="center">SQLMesh is a project of the <a href="https://www.linuxfoundation.org/">Linux Foundation</a>.</p>

SQLMesh is a next-generation data transformation framework designed to ship data quickly, efficiently, and without error. Data teams can run and deploy data transformations written in SQL or Python with visibility and control at any size.

It is more than just a [dbt alternative](https://tobikodata.com/reduce_costs_with_cron_and_partitions.html).

<p align="center">
  <img src="docs/readme/architecture_diagram.png" alt="Architecture Diagram" width="100%" height="100%">
</p>

## Core Features

<img src="https://github.com/SQLMesh/sqlmesh-public-assets/blob/main/vscode.gif?raw=true" alt="SQLMesh Plan Mode">

> Get instant SQL impact and context of your changes, both in the CLI and in the [SQLMesh VSCode Extension](https://sqlmesh.readthedocs.io/en/latest/guides/vscode/?h=vs+cod)

  <details>
  <summary><b>Virtual Data Environments</b></summary>

  * See a full diagram of how [Virtual Data Environments](https://whimsical.com/virtual-data-environments-MCT8ngSxFHict4wiL48ymz) work
  * [Watch this video to learn more](https://www.youtube.com/watch?v=weJH3eM0rzc)

  </details>

  * Create isolated development environments without data warehouse costs
  * Plan / Apply workflow like [Terraform](https://www.terraform.io/) to understand potential impact of changes
  * Easy to use [CI/CD bot](https://sqlmesh.readthedocs.io/en/stable/integrations/github/) for true blue-green deployments

<details>
<summary><b>Efficiency and Testing</b></summary>

Running this command will generate a unit test file in the `tests/` folder: `test_stg_payments.yaml`

Runs a live query to generate the expected output of the model

```bash
sqlmesh create_test tcloud_demo.stg_payments --query tcloud_demo.seed_raw_payments "select * from tcloud_demo.seed_raw_payments limit 5"

# run the unit test
sqlmesh test
```

```sql
MODEL (
  name tcloud_demo.stg_payments,
  cron '@daily',
  grain payment_id,
  audits (UNIQUE_VALUES(columns = (
      payment_id
  )), NOT_NULL(columns = (
      payment_id
  )))
);

SELECT
    id AS payment_id,
    order_id,
    payment_method,
    amount / 100 AS amount, /* `amount` is currently stored in cents, so we convert it to dollars */
    'new_column' AS new_column, /* non-breaking change example  */
FROM tcloud_demo.seed_raw_payments
```

```yaml
test_stg_payments:
model: tcloud_demo.stg_payments
inputs:
    tcloud_demo.seed_raw_payments:
      - id: 66
        order_id: 58
        payment_method: coupon
        amount: 1800
      - id: 27
        order_id: 24
        payment_method: coupon
        amount: 2600
      - id: 30
        order_id: 25
        payment_method: coupon
        amount: 1600
      - id: 109
        order_id: 95
        payment_method: coupon
        amount: 2400
      - id: 3
        order_id: 3
        payment_method: coupon
        amount: 100
outputs:
    query:
      - payment_id: 66
        order_id: 58
        payment_method: coupon
        amount: 18.0
        new_column: new_column
      - payment_id: 27
        order_id: 24
        payment_method: coupon
        amount: 26.0
        new_column: new_column
      - payment_id: 30
        order_id: 25
        payment_method: coupon
        amount: 16.0
        new_column: new_column
      - payment_id: 109
        order_id: 95
        payment_method: coupon
        amount: 24.0
        new_column: new_column
      - payment_id: 3
        order_id: 3
        payment_method: coupon
        amount: 1.0
        new_column: new_column
```
</details>

* Never build a table [more than once](https://tobikodata.com/simplicity-or-efficiency-how-dbt-makes-you-choose.html)
* Track what data’s been modified and run only the necessary transformations for [incremental models](https://tobikodata.com/correctly-loading-incremental-data-at-scale.html)
* Run [unit tests](https://tobikodata.com/we-need-even-greater-expectations.html) for free and configure automated audits
* Run [table diffs](https://sqlmesh.readthedocs.io/en/stable/examples/sqlmesh_cli_crash_course/?h=crash#run-data-diff-against-prod) between prod and dev based on tables/views impacted by a change

<details>
<summary><b>Level Up Your SQL</b></summary>
Write SQL in any dialect and SQLMesh will transpile it to your target SQL dialect on the fly before sending it to the warehouse.
<img src="https://github.com/SQLMesh/sqlmesh/blob/main/docs/readme/transpile_example.png?raw=true" alt="Transpile Example">
</details>

* Debug transformation errors *before* you run them in your warehouse in [10+ different SQL dialects](https://sqlmesh.readthedocs.io/en/stable/integrations/overview/#execution-engines)
* Definitions using [simply SQL](https://sqlmesh.readthedocs.io/en/stable/concepts/models/sql_models/#sql-based-definition) (no need for redundant and confusing `Jinja` + `YAML`)
* See impact of changes before you run them in your warehouse with column-level lineage

For more information, check out the [documentation](https://sqlmesh.readthedocs.io/en/stable/).

## Getting Started
Install SQLMesh through [pypi](https://pypi.org/project/sqlmesh/) by running:

```bash
mkdir sqlmesh-example
cd sqlmesh-example
python -m venv .venv
source .venv/bin/activate
pip install 'sqlmesh[lsp]' # install the sqlmesh package with extensions to work with VSCode
source .venv/bin/activate # reactivate the venv to ensure you're using the right installation
sqlmesh init # follow the prompts to get started (choose DuckDB)
```

</details>

> Note: You may need to run `python3` or `pip3` instead of `python` or `pip`, depending on your python installation.

<details>
<summary><b>Windows Installation</b></summary>

```bash
mkdir sqlmesh-example
cd sqlmesh-example
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install 'sqlmesh[lsp]' # install the sqlmesh package with extensions to work with VSCode
.\.venv\Scripts\Activate.ps1 # reactivate the venv to ensure you're using the right installation
sqlmesh init # follow the prompts to get started (choose DuckDB)
```
</details>


Follow the [quickstart guide](https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/) to learn how to use SQLMesh. You already have a head start!

Follow the [crash course](https://sqlmesh.readthedocs.io/en/stable/examples/sqlmesh_cli_crash_course/) to learn the core movesets and use the easy to reference cheat sheet.

Follow this [example](https://sqlmesh.readthedocs.io/en/stable/examples/incremental_time_full_walkthrough/) to learn how to use SQLMesh in a full walkthrough.

## Join Our Community
Connect with us in the following ways:

* Join the [Tobiko Slack Community](https://tobikodata.com/slack) to ask questions, or just to say hi!
* File an issue on our [GitHub](https://github.com/SQLMesh/sqlmesh/issues/new)
* Send us an email at [hello@tobikodata.com](mailto:hello@tobikodata.com) with your questions or feedback
* Read our [blog](https://tobikodata.com/blog)

## Contributing
We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute, including our DCO sign-off requirement.

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) and [Governance](GOVERNANCE.md) documents.

[Read more](https://sqlmesh.readthedocs.io/en/stable/development/) on how to set up your development environment.

## License
This project is licensed under the [Apache License 2.0](LICENSE). Documentation is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).


---

## 59. akri
- **URL:** https://github.com/devtechedge/akri
- **Language:** Rust
- **Topics:** None
- **Description:** A Kubernetes Resource Interface for the Edge

### README.md

<p align="center"><img src="https://github.com/project-akri/akri-docs/blob/main/art/logo-horizontal/akri-logo-horizontal-light.svg" alt="Akri Logo" width="300"></p>

[![Slack channel #akri](https://img.shields.io/badge/slack-akri-blueviolet.svg?logo=slack)](https://kubernetes.slack.com/messages/akri)
[![Rust Version](https://img.shields.io/badge/rustc-1.88.0-blue.svg)](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)
[![Kubernetes Version](https://img.shields.io/badge/kubernetes-≥%201.33-blue.svg)](https://kubernetes.io/)
[![codecov](https://codecov.io/gh/project-akri/akri/branch/main/graph/badge.svg?token=V468HO7CDE)](https://codecov.io/gh/project-akri/akri)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/5339/badge)](https://bestpractices.coreinfrastructure.org/projects/5339)

[![Check Rust](https://github.com/project-akri/akri/workflows/Check%20Rust/badge.svg?branch=main&event=push)](https://github.com/project-akri/akri/actions?query=workflow%3A%22Check+Rust%22)
[![Tarpaulin Code Coverage](https://github.com/project-akri/akri/workflows/Tarpaulin%20Code%20Coverage/badge.svg?branch=main&event=push)](https://github.com/project-akri/akri/actions?query=workflow%3A%22Tarpaulin+Code+Coverage%22)
[![Test K3s, Kubernetes, and MicroK8s](https://github.com/project-akri/akri/workflows/Test%20K3s,%20Kubernetes,%20and%20MicroK8s/badge.svg?branch=main&event=push)](https://github.com/project-akri/akri/actions?query=workflow%3A%22Test+K3s%2C+Kubernetes%2C+and+MicroK8s%22)

---

Akri is a [Cloud Native Computing Foundation (CNCF) Sandbox project](https://www.cncf.io/sandbox-projects/).

Akri lets you easily expose heterogeneous leaf devices (such as IP cameras and USB devices) as resources in a Kubernetes cluster, while also supporting the exposure of embedded hardware resources such as GPUs and FPGAs.
Akri continually detects nodes that have access to these devices and schedules workloads based on them.

Simply put: you name it, Akri finds it, you use it.

---

## Why Akri

At the edge, there are a variety of sensors, controllers, and MCU class devices that are producing data and performing actions.
For Kubernetes to be a viable edge computing solution, these heterogeneous “leaf devices” need to be easily utilized by Kubernetes clusters.
However, many of these leaf devices are too small to run Kubernetes themselves. Akri is an open source project that exposes these leaf devices as resources in a Kubernetes cluster.
It leverages and extends the Kubernetes [device plugin framework](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/), which was created with the cloud in mind and focuses on advertising static resources such as GPUs and other system hardware.
Akri took this framework and applied it to the edge, where there is a diverse set of leaf devices with unique communication protocols and intermittent availability.

Akri is made for the edge, **handling the dynamic appearance and disappearance of leaf devices**.
Akri provides an abstraction layer similar to [CNI](https://github.com/containernetworking/cni), but instead of abstracting the underlying network details, it is removing the work of finding, utilizing, and monitoring the availability of the leaf device.
An operator simply has to apply a Akri Configuration to a cluster, specifying the Discovery Handler (say ONVIF) that should be used to discover the devices and the Pod that should be deployed upon discovery (say a video frame server).
Then, Akri does the rest.
An operator can also allow multiple nodes to utilize a leaf device, thereby **providing high availability** in the case where a node goes offline.
Furthermore, Akri will automatically create a Kubernetes service for each type of leaf device (or Akri Configuration), removing the need for an application to track the state of pods or nodes.

Most importantly, Akri **was built to be extensible**.
Akri currently ships ONVIF, udev, OPC UA, and debug-echo Discovery Handlers, but more can be easily added by community members like you.
The more protocols Akri can support, the wider an array of leaf devices Akri can discover.
We are excited to work with you to build a more connected edge.

## How Akri Works

Akri’s architecture is made up of five key components: two custom resources, Discovery Handlers, an Agent (device plugin implementation), and a custom Controller.
The first custom resource, the Akri Configuration, is where **you name it**.
This tells Akri what kind of device it should look for.
At this point, **Akri finds it**! Akri's Discovery Handlers look for the device and inform the Agent of discovered devices.
The Agent then creates Akri's second custom resource, the Akri Instance, to track the availability and usage of the device.
Having found your device, the Akri Controller helps **you use it**.
It sees each Akri Instance (which represents a leaf device) and deploys a ("broker") Pod that knows how to connect to the resource and utilize it.

<img src="https://github.com/project-akri/akri-docs/blob/main/media/akri-architecture.svg" alt="Akri Architecture" style="padding-bottom: 10px; padding-top: 10px;
margin-right: auto; display: block; margin-left: auto;"/>

## Quick Start with a Demo

Try the [end to end demo](https://docs.akri.sh/demos/usb-camera-demo) of Akri to see Akri discover mock video cameras and a streaming app display the footage from those cameras.
It includes instructions on K8s cluster setup.
If you would like to perform the demo on a cluster of Raspberry Pi 4's, see the [Raspberry Pi 4 demo](https://docs.akri.sh/demos/usb-camera-demo-rpi4).

## Documentation

See Akri's [documentation site](https://docs.akri.sh/), which includes:

- [User guide for deploying Akri using Helm](https://docs.akri.sh/user-guide/getting-started)
- [Akri architecture](https://docs.akri.sh/architecture/architecture-overview)
- [How to build Akri](https://docs.akri.sh/development/building)
- [How to extend Akri for protocols that haven't been supported yet](https://docs.akri.sh/development/handler-development).
- [How to create a broker to leverage discovered devices](https://docs.akri.sh/development/broker-development).

To contribute to Akri's documentation, visit Akri's [docs repository](https://github.com/project-akri/akri-docs).

## Roadmap

Akri is built to be extensible.
We currently have ONVIF, udev, OPC UA, and debug-echo Discovery Handlers, but as a community, we hope to continuously support more protocols.
We have created a [Discovery Handler implementation roadmap](https://docs.akri.sh/community/roadmap#implement-additional-discovery-handlers) in order to prioritize development of Discovery Handlers.
If there is a protocol you feel we should prioritize, please [create an issue](https://github.com/project-akri/akri/issues/new/choose), or better yet, contribute the implementation!

To see what else is in store for Akri, reference our [roadmap](https://docs.akri.sh/community/roadmap).

## Community, Contributing, and Support

You can reach the Akri community via the [#akri](https://kubernetes.slack.com/messages/akri) channel in [Kubernetes Slack](https://kubernetes.slack.com) and/or join our [community calls](https://hackmd.io/@akri/S1GKJidJd) on the first Tuesday of the month from 8:00 AM to 9:00 AM PT.

Akri welcomes contributions, whether by [creating new issues](https://github.com/project-akri/akri/issues/new/choose) or pull requests.
See our [contributing document](https://docs.akri.sh/community/contributing) on how to get started!

## Licensing

This project is released under the [Apache 2.0 license](./LICENSE).


---

## 60. agave-sdk
- **URL:** https://github.com/devtechedge/agave-sdk
- **Language:** Rust
- **Topics:** None
- **Description:** No description

### README.md

# agave-sdk

[![Main](https://github.com/anza-xyz/agave-sdk/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/anza-xyz/agave-sdk/actions/workflows/main.yml?query=branch%3Amaster)

Rust libraries and interfaces for Solana core development.

This repository is for core-development-facing components that are useful
outside the agave validator codebase. For general Solana SDK types and on-chain
program interfaces, see [`solana-sdk`](https://github.com/anza-xyz/solana-sdk).

## License

Licensed under the [Apache License 2.0](LICENSE).


---

## 61. v5-token-pricing
- **URL:** https://github.com/devtechedge/v5-token-pricing
- **Language:** TypeScript
- **Topics:** None
- **Description:** Timestamped multi-source USD token pricing for v5. Pure resolver: keys injected per call, no cache, no env reads.

### README.md

# v5-token-pricing

What was this token worth at this instant?

One function, three upstreams, no state. It answers with the datapoint an upstream
actually holds — and tells you when that datapoint is from.

## Install

```sh
pnpm add github:across-protocol/v5-token-pricing
```

The package builds itself on install (`prepare`) and ships compiled ESM plus
`.d.ts`.

This repo is developed and built with **Node and pnpm only** — there is no Bun
in its toolchain. Bun appears here for exactly one reason: the first consumer is
a Bun service, so `dist/` is checked to load under **both Node >= 20 and Bun**
before release. That check is not ceremony — a sibling package is unusable from
Bun because a transitive dependency crashes its loader, which is why this package
keeps its dependency surface to one.

## Use

```ts
import { getTokenPriceAt } from "@across-protocol/v5-token-pricing";

const result = await getTokenPriceAt({
  chainId: 8453,
  tokenAddress: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
  timestamp: Date.now() - 86_400_000,
  apiKeys: { coingecko: cgKey, alchemy: alchemyKey }, // both optional
});

if (result.priceUsd === null) {
  // nothing could price it — result.attempts says why
} else {
  store(result.priceUsd, { observedAt: result.observedAt, source: result.source });
}
```

## Types

Everything below is exported from the package root.

### Input

```ts
getTokenPriceAt(input: {
  chainId: number;        // numeric chain id, e.g. 8453
  tokenAddress: string;   // contract address; 0x-hex on EVM, base58 on Tron
  timestamp: number;      // the instant you want a price for, UNIX MILLISECONDS
  apiKeys?: ApiKeys;      // omitted entirely => DefiLlama only
}): Promise<TokenPriceResult>

type ApiKeys = {
  coingecko?: string;     // absent => CoinGecko's free host is used
  alchemy?: string;       // absent => Alchemy is skipped (skipped_no_key)
};
```

### Return

`TokenPriceResult` is a discriminated union. Narrow on `priceUsd`:

```ts
type TokenPriceResult =
  | {
      priceUsd: number;        // USD per WHOLE token (not per base unit)
      observedAt: number;      // UNIX MILLISECONDS of the upstream's datapoint
      source: PriceSource;     // which upstream answered
      confidence?: number;     // 0..1, only when the upstream supplies one
      attempts: PriceAttempt[];
    }
  | {
      priceUsd: null;          // nothing could price it
      observedAt: null;
      source: null;
      attempts: PriceAttempt[];
    };

type PriceSource = "defillama" | "coingecko" | "alchemy";

type PriceAttempt = { source: PriceSource; outcome: AttemptOutcome };

type AttemptOutcome =
  | "ok"
  | "no_data"
  | "implausible"
  | "error"
  | "skipped_no_key"
  | "skipped_unmapped_chain";
```

`attempts` is present on **both** members — which is why unpriced is
`priceUsd === null` rather than a bare `null` return. A `null` on its own cannot
say whether the token is unknown everywhere, the chain was unmapped, a key was
missing, or every upstream was down, and those want different responses.

The function does not reject on upstream failure: a source that throws becomes an
`error` attempt, not an exception. It can still throw on programmer error
(a malformed argument).

### Also exported

`LLAMA_SLUG_BY_CHAIN`, `CG_PLATFORM_BY_CHAIN`, `ALCHEMY_NETWORK_BY_CHAIN` —
`Record<number, string>`, keyed by numeric chain id.

### observedAt is not the timestamp you asked for

**`observedAt` is the instant of the datapoint the upstream returned.** It is
never the requested `timestamp` and never the wall clock. Upstreams answer with
the observation they have, which is near your instant, not on it — and how near
depends on the token's liquidity.

Measured: for one requested instant, DefiLlama answered for USDC on Base and
WETH on Arbitrum with observations roughly **7 minutes apart from each other**.
Same request, two different observed instants.

This library will not pretend it hit your instant exactly, and it takes no
position on what you do about that. Both policies are legitimate and the choice
is yours:

- **File under the instant you asked for** and treat the answer as good enough.
  Reasonable, because the upstream was *asked about* that instant — unlike a spot
  price, which knows nothing about the past. Keep `observedAt` anyway so the
  distance stays auditable later.
- **File under `observedAt`'s own bucket** and decide per lookup whether an
  observation that landed nearby is close enough.

What you must not do is discard `observedAt`. It is the only evidence of how far
the answer sat from the question.

### Never invented

`priceUsd: null` means no source could price this token at this instant. The
library does not interpolate between datapoints, extrapolate from the present,
or substitute a similar token.

### attempts

One entry per source that was tried, in the order tried. Sources after the one
that answered are not tried and so do not appear.

| outcome | meaning |
| --- | --- |
| `ok` | returned a plausible datapoint |
| `no_data` | answered, but had nothing for this token/instant |
| `implausible` | returned a value that failed the sanity rules below |
| `error` | threw, timed out, or returned a bad status / body |
| `skipped_no_key` | needs a credential that this call did not supply |
| `skipped_unmapped_chain` | has no identifier for this chain id |

This is the package's only concession to observability. It emits nothing — no
logs, no spans, no metrics, not even on error paths. You decide what to record.

## Resolution order

1. **DefiLlama** — free, no key, address-native. Always tried when the chain maps.
2. **CoinGecko** — `market_chart/range`, nearest datapoint wins. Uses the pro
   host and the `x-cg-pro-api-key` header when `apiKeys.coingecko` is present,
   the free host otherwise.
3. **Alchemy** — historical prices, nearest datapoint wins. Skipped entirely
   without `apiKeys.alchemy`.

A source that throws, times out, or returns an implausible value is a **miss**,
not a failure: the next source still gets its turn.

### Implausible means

- non-finite, `<= 0`, or `> $10,000,000` per whole token; or
- the token's symbol marks it a USD stablecoin and the price is outside
  `[0.50, 2.00]`.

The stablecoin band exists because it caught real bad upstream data.

## Deliberate non-features

- **No cache.** Not an LRU, not a memo, not a module-level Map. Callers already
  have their own tiers in front of this, and per-call key injection makes
  cross-call reuse wrong.
- **No credentials held anywhere.** The library never reads `process.env`, has no
  config singleton, and keeps no key between calls. Keys arrive on the call and
  are used only for that call's requests.
- **No telemetry, no logging, no callbacks.** See `attempts`.

## Chains

Each source has its own chain identifier map. A chain missing from one map means
that source is skipped for the call (`skipped_unmapped_chain`) — never an error,
and the other sources still get their turn.

## Development

Node >= 20 and pnpm. No Bun, no other runtime.

```sh
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

The live DefiLlama test is skipped unless `LIVE_PRICE_TESTS=1` is set. It needs
no credential. No test in this repo requires a key to run.

Runtime dependencies: `@across-protocol/constants` (token symbols) and global
`fetch`. That is all.


---

## 62. safe-wallet-monorepo
- **URL:** https://github.com/devtechedge/safe-wallet-monorepo
- **Language:** TypeScript
- **Topics:** None
- **Description:** Safe{Wallet} ΓÇô smart account wallet

### README.md

# <img src="https://github.com/user-attachments/assets/b8249113-d515-4c91-a12a-f134813614e8" height="60" valign="middle" alt="Safe{Wallet}" style="background: #fff; padding: 20px; margin: 0 -20px" />

# Safe{Wallet} monorepo

🌐 [Safe{Wallet} web app](/apps/web/README.md) ・ 📱 [Safe{Wallet} mobile app](/apps/mobile/README.md)

## Overview

Welcome to the Safe{Wallet} monorepo! Safe (formerly Gnosis Safe) is a multi-signature smart contract wallet for Ethereum and other EVM chains, requiring multiple signatures to execute transactions.

This repository houses both web and mobile applications along with shared packages, managed under a unified structure using Yarn Workspaces. The monorepo setup simplifies dependency management and ensures consistent development practices across projects.

### Key components

- **apps/web** - Next.js web application ([detailed documentation](/apps/web/README.md))
- **apps/mobile** - Expo/React Native mobile application ([detailed documentation](/apps/mobile/README.md))
- **packages/store** - Shared Redux store used by both platforms
- **packages/utils** - Shared utilities and TypeScript types
- **config/** - Shared configuration files

> [!IMPORTANT]
>
> For detailed setup instructions and platform-specific development guides, please refer to the dedicated README files:
>
> - **[Web App Documentation](/apps/web/README.md)** - Complete guide for the Next.js web application
> - **[Mobile App Documentation](/apps/mobile/README.md)** - Complete guide for the mobile application, including iOS/Android setup

## Getting started

To get started, ensure you have the required tools installed and follow these steps:

### Prerequisites

- **Node.js**: Install the latest stable version from [Node.js](https://nodejs.org/).
- **Yarn**: Use Yarn version 4.5.3 or later

to install it with the latest node version you can simply do

```bash
corepack enable
```

and then just run

```bash
yarn
```

This will install the required version of yarn and resolve all dependencies.

> [!NOTE]
>
> Corepack is a tool to help with managing versions of your package managers. It exposes binary proxies for each supported package manager that, when called, will identify whatever package manager is
> configured for the current project, download it if needed, and finally run it.

### Initial setup

1. Clone the repository:

```bash
git clone <repo-url>
cd monorepo
```

2. Install dependencies:

```bash
yarn install
```

### Quick start commands

```bash
# Run web app in development mode
yarn workspace @safe-global/web dev

# Run mobile app in development mode
yarn workspace @safe-global/mobile start

# Run tests for web
yarn workspace @safe-global/web test

# Run Storybook for web
yarn workspace @safe-global/web storybook
```

> [!TIP]
>
> For comprehensive setup instructions, environment variables, testing, and platform-specific workflows, see:
>
> - **[Web App README](/apps/web/README.md)** - Environment setup, Cypress E2E tests, Storybook, and more
> - **[Mobile App README](/apps/mobile/README.md)** - iOS/Android setup, Maestro E2E tests, Expo configuration, and more

## Monorepo commands

Here are some essential commands to help you navigate the monorepo:

### Workspace management

- **Run a script in a specific workspace:**

```bash
yarn workspace <workspace-name> <script>
```

Example:

```bash
yarn workspace @safe-global/web dev
```

- **Add a dependency to a specific workspace:**

```bash
yarn workspace <workspace-name> add <package-name>
```

- **Remove a dependency from a specific workspace:**

```bash
yarn workspace <workspace-name> remove <package-name>
```

> [!Note]
>
> Yarn treats commands that contain a colon as global commands. For example if you have a
> command in a workspace that has a colon and there isn't another workspace that has the same command,
> you can run the command without specifying the workspace name. For example:
>
> ```bash
> yarn cypress:open
> ```
>
> is equivalent to:
>
> ```bash
> yarn workspace @safe-global/web cypress:open
> ```

### Linting, formatting, and type-checking

- **Run ESLint across all workspaces:**

```bash
yarn lint
```

- **Run Prettier to check formatting:**

```bash
yarn prettier
```

- **Run type-check for a workspace:**

```bash
yarn workspace @safe-global/web type-check
yarn workspace @safe-global/mobile type-check
```

### Testing

- **Run unit tests across all workspaces:**

```bash
yarn test
```

- **Run E2E tests (web only):**

```bash
yarn workspace @safe-global/web cypress:open  # Interactive mode
yarn workspace @safe-global/web cypress:run   # Headless mode
```

## Contributing

### Adding a new workspace

1. Create a new directory under `apps/` or `packages/`.
2. Add a `package.json` file with the appropriate configuration.
3. Run:

```bash
yarn install
```

### Best practices

- Use Yarn Workspaces commands for managing dependencies.
- Ensure type-check, lint, prettier, and tests pass before pushing changes.
- Follow the [semantic commit message guidelines](https://www.conventionalcommits.org/).
- For AI contributors, see [AGENTS.md](AGENTS.md) for detailed guidelines.

### Tools & configurations

- **Husky**: Pre-commit hooks for linting, formatting, and type-checking.
- **ESLint & Prettier**: Enforce coding standards and formatting.
- **Jest**: Unit testing framework.
- **Cypress**: E2E testing for the web app.
- **Storybook**: Component documentation and development for the web app.
- **Expo**: Mobile app framework for the `mobile` workspace.
- **Next.js**: React framework for the `web` workspace.
- **Tamagui**: UI component library for the mobile app.

## Release process

For information on releasing the web app, see the [Automated Release Procedure](apps/web/docs/release-procedure-automated.md).

## Useful links

- [Yarn Workspaces Documentation](https://yarnpkg.com/features/workspaces)
- [Expo Documentation](https://docs.expo.dev/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Storybook Documentation](https://storybook.js.org/docs)
- [Jest Documentation](https://jestjs.io/)
- [ESLint Documentation](https://eslint.org/)
- [Prettier Documentation](https://prettier.io/)
- [Safe Developer Docs](https://docs.safe.global/)

## Ode to the repo

```
In ages past when Gnosis laid the founding stone,
A vault was wrought that no single key could own.
Where signatures must gather ere the gate will yield,
M-of-N doth guard the treasure, sworn and sealed.

Now Yarn doth wind its threads through hall and bower,
Binding web and mobile in a single tower.
Redux keeps the ledger, RTK Query rides afar,
Returning with the fetched gold beneath the evening star.

Chain by chain the watchers set their vigil wide,
Across th' EVM kingdoms, ever at the Safe's own side.
Storybook doth chronicle each component's tale,
And Cypress walks the paths where lesser tests would fail.

No `any` types shall darken these well-guarded lands —
That ancient law doth hold by Prettier's own hands.
Feature flags like waypoints mark what lies ahead,
And lazy loads awaken only where the road doth tread.

Long the name hath wandered — Gnosis once, now Safe it stands,
Yet still the vow endureth, written into typed commands:
That what you hold stays guarded, deep beyond all theft or flame,
For this the codebase liveth — and security its name.
```

---

If you have any questions or run into issues, feel free to open a discussion or contact the maintainers. Happy coding!
🚀


---

## 63. viem
- **URL:** https://github.com/devtechedge/viem
- **Language:** TypeScript
- **Topics:** None
- **Description:** TypeScript Interface for Ethereum

### README.md

<!-- > [!IMPORTANT] -->
<!-- > Viem is participating in Gitcoin Grants round 21. Consider <a href="https://explorer.gitcoin.co/#/round/42161/389/73">supporting the project</a>. Thank you. 🙏 -->

<br/>

<p align="center">
  <a href="https://viem.sh">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/viem/main/.github/gh-logo-dark.svg">
        <img alt="viem logo" src="https://raw.githubusercontent.com/wevm/viem/main/.github/gh-logo-light.svg" width="auto" height="60">
      </picture>
</a>
</p>

<p align="center">
  TypeScript Interface for Ethereum
<p>

<p align="center">
  <a href="https://www.npmjs.com/package/viem">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/v/viem?colorA=21262d&colorB=21262d&style=flat">
      <img src="https://img.shields.io/npm/v/viem?colorA=f6f8fa&colorB=f6f8fa&style=flat" alt="Version">
    </picture>
  </a>
  <a href="https://app.codecov.io/gh/wevm/viem">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/codecov/c/github/wevm/viem?colorA=21262d&colorB=21262d&style=flat">
      <img src="https://img.shields.io/codecov/c/github/wevm/viem?colorA=f6f8fa&colorB=f6f8fa&style=flat" alt="Code coverage">
    </picture>
  </a>
  <a href="https://github.com/wevm/viem/blob/main/LICENSE">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/l/viem?colorA=21262d&colorB=21262d&style=flat">
      <img src="https://img.shields.io/npm/l/viem?colorA=f6f8fa&colorB=f6f8fa&style=flat" alt="MIT License">
    </picture>
  </a>
  <a href="https://www.npmjs.com/package/viem">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/dm/viem?colorA=21262d&colorB=21262d&style=flat">
      <img src="https://img.shields.io/npm/dm/viem?colorA=f6f8fa&colorB=f6f8fa&style=flat" alt="Downloads per month">
    </picture>
  </a>
  <a href="https://bestofjs.org/projects/viem">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/endpoint?colorA=21262d&colorB=21262d&style=flat&url=https://bestofjs-serverless.now.sh/api/project-badge?fullName=wevm%2Fviem%26since=daily">
      <img src="https://img.shields.io/endpoint?colorA=f6f8fa&colorB=f6f8fa&style=flat&url=https://bestofjs-serverless.now.sh/api/project-badge?fullName=wevm%2Fviem%26since=daily" alt="Best of JS">
    </picture>
  </a>
</p>

<br>

## Features

- Abstractions over the [JSON-RPC API](https://ethereum.org/en/developers/docs/apis/json-rpc/) to make your life easier
- First-class APIs for interacting with [Smart Contracts](https://ethereum.org/en/glossary/#smart-contract)
- Language closely aligned to official [Ethereum terminology](https://ethereum.org/en/glossary/)
- Import your Browser Extension, WalletConnect or Private Key Wallet
- Browser native [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt), instead of large BigNumber libraries
- Utilities for working with [ABIs](https://ethereum.org/en/glossary/#abi) (encoding/decoding/inspection)
- TypeScript ready ([infer types](https://viem.sh/docs/typescript) from ABIs and EIP-712 Typed Data)
- First-class support for [Anvil](https://book.getfoundry.sh/), [Hardhat](https://hardhat.org/) & [Ganache](https://trufflesuite.com/ganache/)
- Test suite running against [forked](https://ethereum.org/en/glossary/#fork) Ethereum network

... and a lot more.

## Overview

```ts
// 1. Import modules.
import { createPublicClient, http } from 'viem';
import { mainnet } from 'viem/chains';

// 2. Set up your client with desired chain & transport.
const client = createPublicClient({
  chain: mainnet,
  transport: http(),
});

// 3. Consume an action!
const blockNumber = await client.getBlockNumber();
```

## Documentation

[Head to the documentation](https://viem.sh/docs/getting-started) to read and learn more about viem.

## Community

Check out the following places for more viem-related content:

- Follow [@wevm_dev](https://twitter.com/wevm_dev), [@_jxom](https://twitter.com/_jxom), and [@awkweb](https://twitter.com/awkweb) on Twitter for project updates
- Join the [discussions on GitHub](https://github.com/wevm/viem/discussions)
- [Share your project/organization](https://github.com/wevm/viem/discussions/104) that uses viem

## Support

- [GitHub Sponsors](https://github.com/sponsors/wevm?metadata_campaign=docs_support)
- [Gitcoin Grant](https://wagmi.sh/gitcoin)
- [wevm.eth](https://etherscan.io/name-lookup-search?id=wevm.eth)

## Sponsors

<a href="https://paradigm.xyz">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/paradigm-dark.svg">
    <img alt="paradigm logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/paradigm-light.svg" width="auto" height="70">
  </picture>
</a>
<a href="https://tempo.xyz">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/tempo-dark.svg">
    <img alt="tempo logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/tempo-light.svg" width="auto" height="70">
  </picture>
</a>

<br>

<a href="https://twitter.com/family">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/family-dark.svg">
    <img alt="family logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/family-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://twitter.com/context">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/context-dark.svg">
    <img alt="context logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/context-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://twitter.com/prtyDAO">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/partydao-dark.svg">
    <img alt="PartyDAO logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/partydao-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://dynamic.xyz">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/dynamic-dark.svg">
    <img alt="Dynamic logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/dynamic-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://sushi.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sushi-dark.svg">
    <img alt="Sushi logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sushi-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://stripe.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/stripe-dark.svg">
    <img alt="Stripe logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/stripe-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://privy.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/privy-dark.svg">
    <img alt="Privy logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/privy-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://pancakeswap.finance">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pancake-dark.svg">
    <img alt="pancake logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pancake-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://pimlico.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pimlico-dark.svg">
    <img alt="pimlico logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pimlico-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://zora.co">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/zora-dark.svg">
    <img alt="zora logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/zora-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://syndicate.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/syndicate-dark.svg">
    <img alt="syndicate logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/syndicate-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://relay.link">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/relay-dark.svg">
    <img alt="relay logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/relay-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://polymarket.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/polymarket-dark.svg">
    <img alt="polymarket logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/polymarket-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://sequence.xyz">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sequence-dark.svg">
    <img alt="sequence logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sequence-light.svg" width="auto" height="50">
  </picture>
</a>
<a href="https://web3auth.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/web3auth-dark.svg">
    <img alt="web3auth logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/web3auth-light.svg" width="auto" height="50">
  </picture>
</a>

## Contributing

If you're interested in contributing, please read the [contributing docs](/.github/CONTRIBUTING.md) **before submitting a pull request**.

## Authors

- [@jxom](https://github.com/jxom) (jxom.eth, [Twitter](https://twitter.com/_jxom))
- [@tmm](https://github.com/tmm) (awkweb.eth, [Twitter](https://twitter.com/awkweb))

## License

[MIT](/LICENSE) License


<br />
<br />

<a href="https://vercel.com/?utm_source=wevm&utm_campaign=oss">
  <img src="https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg" alt="Powered by Vercel" height="35">
</a>


---

## 64. wormhole-connect
- **URL:** https://github.com/devtechedge/wormhole-connect
- **Language:** TypeScript
- **Topics:** None
- **Description:** Wormhole Connect brings all the functionality and utility of Wormhole right into your application and removes all of the complexity.

### README.md

# Wormhole Connect [![Documentation](https://img.shields.io/badge/Documentation-2a67c9)](https://docs.wormhole.com/wormhole/wormhole-connect/overview) [![npm version](https://img.shields.io/npm/v/@wormhole-foundation/wormhole-connect.svg)](https://www.npmjs.com/package/@wormhole-foundation/wormhole-connect) ![CI build](https://github.com/wormhole-foundation/wormhole-connect/actions/workflows/build.yml/badge.svg)

Wormhole Connect is a customizable React widget for cross-chain asset transfers powered by Wormhole.

[![Wormhole Connect running on Portal Bridge](https://i.imgur.com/U7ZB8y5.png)](https://portalbridge.com/)

Connect is powered by the [Wormhole TypeScript SDK](https://github.com/wormhole-foundation/wormhole-sdk-ts). Developers interested in building their
own interface for Wormhole bridging functionality are encouraged to explore the SDK!

## Demo

Wormhole Connect is deployed live in several production apps. Here are a few:

- [Portal Bridge](https://portalbridge.com/)
- [Jupiter](https://jup.ag/onboard/cctp)
- [PancakeSwap](https://bridge.pancakeswap.finance/wormhole)


## Getting Started

### Via package manager for React apps (Recommended)

If you're using React, you can import the `<WormholeConnect />` component directly into your JSX:

#### Installation

```bash
# Using bun (recommended)
bun add @wormhole-foundation/wormhole-connect

# Using npm
npm i @wormhole-foundation/wormhole-connect
```

#### Using the component

```javascript
import WormholeConnect from '@wormhole-foundation/wormhole-connect';

function App() {
  return (
    <WormholeConnect />
  );
}
```

### Alternative: hosted version via CDN (for any website)

If you're not using React, you can still embed Connect on your website by using the hosted version:

```ts
import {
  wormholeConnectHosted,
} from '@wormhole-foundation/wormhole-connect';

const container = document.getElementById('connect')!;

wormholeConnectHosted(container);
```


You can provide `config` and `theme` parameters in a second function argument:

```ts
import {
  wormholeConnectHosted,
} from '@wormhole-foundation/wormhole-connect';

const container = document.getElementById('connect')!;

wormholeConnectHosted(container, {
  config: {
    rpcs: {
      ...
    }
  },
  theme: {
    background: {
      default: '#004547',
    }
  }
});
```

## Configuration

Wormhole Connect is highly customizable via two props: `config` and `theme`. Here is an example which
limits it to two chains and customizes the background color:

```tsx
import WormholeConnect, {
  WormholeConnectConfig, WormholeConnectPartialTheme
} from '@wormhole-foundation/wormhole-connect';

const config: WormholeConnectConfig = {
  chains: ['Ethereum', 'Solana']
};

const theme: WormholeConnectPartialTheme = {
  background: {
    default: '#212b4a'
  }
};

function App() {
  return (
    <WormholeConnect config={config} theme={theme} />
  )
}
```

If using the hosted version, provide `config` and `theme` as JSON-serialized strings on the mount point:

```html
<div id="wormhole-connect" data-config="{...}" data-theme="{...}"></div>
```

Below are some of the more commonly used config options. See
[the full Connect docs](https://docs.wormhole.com/wormhole/wormhole-connect/overview) for more complete
documentation and examples of the different config options.

### Network (`network`):

Values: `Mainnet` | `Testnet` | `Devnet`

Connect renders in Mainnet mode by default, but you can switch it to testnet by setting `network` to `Testnet`:

```ts
const config: WormholeConnectConfig = {
  network: 'Testnet'
}
```

### Choosing Chains (`chains`):

You can provide a whitelist of chains to limit which ones Connect offers.

```ts
const config: WormholeConnectConfig = {
  chains: ['Ethereum', 'Solana']
}
```

See [`chains.ts`](https://github.com/wormhole-foundation/wormhole-sdk-ts/blob/main/core/base/src/constants/chains.ts) in the SDK. By default, Connect offers a subset of chains for both `mainnet` and `testnet`:

| `mainnet` | `testnet` |
| ---------- | ------------- |
| Ethereum | Sepolia |
| Polygon | |
| Bsc | Bsc |
| Avalanche | Avalanche |
| Fantom | Fantom |
| Celo | Celo |
| Moonbeam | Moonbeam |
| Solana | Solana |
| Sui | Sui |
| Aptos | Aptos |
| Base | BaseSepolia |
| Arbitrum | ArbitrumSepolia |
| Optimism | OptimismSepolia |
| Klaytn | Klaytn |
| Scroll | Scroll |
| Xlayer | Xlayer |
| Mantle | Mantle |
| Worldchain | Worldchain |
| Unichain | Unichain |
| Berachain | |
| Ink | |
| Linea | Linea |
| Sonic | Sonic |
| Mezo | Mezo |
| Seievm | Seievm |
| Plume | Plume |
| HyperEVM | |
| HyperCore | |
| XRPLEVM | XRPLEVM |
| Creditcoin | |
| Fogo | Fogo |
| | Monad |
| | Moca |

### RPC Endpoints (`rpcs`):

We strongly recommend that you configure your own custom RPC endpoints for each network your application needs. The default public RPCs may be throttled or rate limited.

```ts
const config: WormholeConnectConfig = {
  rpcs: {
    Solana: 'https://mainnet.helius-rpc.com/?api-key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    Ethereum: 'https://rpc.ankr.com/eth/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  }
}
```

### Custom Tokens (`tokensConfig`)

You can add arbitrary tokens to the Connect tokens menu by providing a `tokensConfig` key.

```ts
const config: WormholeConnectConfig = {
  tokensConfig: {
    ...
  }
}
```

See the "Arbitrary Token" example in [the config docs](https://docs.wormhole.com/wormhole/wormhole-connect/configuration#arbitrary-token).

Please note you have to [register a token](https://portalbridge.com/advanced-tools/#/register) with the token bridge before you can use it in Connect.

### Configuring Custom NTT (Native Token Transfer) Tokens

To configure a custom NTT token, pass your NTT config to the `nttRoutes` helper function, which will add the NTT routes to the `routes` array. You can find the definition for the NTT config [here](https://github.com/wormhole-foundation/example-native-token-transfers/blob/6a1a3d9e6d1a2045fb1688c2b53c9ac145cb40bc/sdk/route/src/types.ts#L34).

```ts
const config: WormholeConnectConfig = {
  routes: [
    ...nttRoutes({
      tokens: {
        // Your custom NTT configs go here
        // See: https://github.com/wormhole-foundation/wormhole-connect/blob/9548507ca68dfd249bf84057889dc61553b17b5f/wormhole-connect/src/components/DemoApp/consts.ts#L3 for an example NTT config
      }
    })
    // other routes
  ]
}
```

Each `token` address specified in the NTT config must have a corresponding entry in `tokensConfig`, whether it is a built-in or custom token.

### Custom Theme

You can also customize Connect's color scheme by providing a `WormholeConnectTheme` as the `theme` prop.
By default, Connect renders using the `dark` theme.

```jsx
import WormholeConnect, {
  dark,
  WormholeConnectTheme,
} from "@wormhole-foundation/wormhole-connect";

// alters the `dark` theme
const customized: WormholeConnectTheme = dark;
customized.success = '#212b4a';
customized.background.default = "navy";
customized.button.action = "#81c784";
customized.button.actionText = "#000000";

export default function App() {
  return <WormholeConnect theme={customized} />;
}
```

You can change the `theme` prop to dynamically change Connect's colors, for example when your application
switches from light to dark mode.

See the definitions of `WormholeConnectTheme` and `dark` in [theme.ts](https://github.com/wormhole-foundation/wormhole-connect/blob/development/wormhole-connect/src/theme.ts) for type definitions.

### Learn More

Please read [the full Connect documentation](https://docs.wormhole.com/wormhole/wormhole-connect/overview) to see what else is possible!

## Contributing

We welcome contributions and bug fixes. Please see [CONTRIBUTING.md](https://github.com/wormhole-foundation/wormhole-connect/blob/development/CONTRIBUTING.md)


## Disclaimer

This SDK is an open source software SDK that leverages the Wormhole protocol, a cross chain messaging protocol. The SDK does not process payments. THIS SDK AND THE WORMHOLE PROTOCOL ARE PROVIDED "AS IS", AT YOUR OWN RISK, AND WITHOUT WARRANTIES OF ANY KIND. By using or accessing this SDK or Wormhole, you agree that no developer or entity involved in creating, deploying, maintaining, operating this SDK or Wormhole, or causing or supporting any of the foregoing, will be liable in any manner for any claims or damages whatsoever associated with your use, inability to use, or your interaction with other users of, this SDK or Wormhole, or this SDK or Wormhole themselves, including any direct, indirect, incidental, special, exemplary, punitive or consequential damages, or loss of profits, cryptocurrencies, tokens, or anything else of value. By using or accessing this SDK, you represent that you are not subject to sanctions or otherwise designated on any list of prohibited or restricted parties or excluded or denied persons, including but not limited to the lists maintained by the United States' Department of Treasury's Office of Foreign Assets Control, the United Nations Security Council, the European Union or its Member States, or any other government authority.

Wormhole Connect is an NPM package that interacts with the Wormhole protocol. You assume all risks associated with using the SDK, the Wormhole Connect NPM package, the Wormhole protocol, and digital assets and decentralized systems generally, including but not limited to, that: (a) digital assets are highly volatile; (b) using digital assets is inherently risky due to both features of such assets and the potential unauthorized acts of third parties; (c) you may not have ready access to assets; and (d) you may lose some or all of your tokens or other assets. You agree that you will have no recourse against anyone else for any losses due to the use of the SDK or Wormhole. For example, these losses may arise from or relate to: (i) incorrect information; (ii) software or network failures; (iii) corrupted cryptocurrency wallet files; (iv) unauthorized access; (v) errors, mistakes, or inaccuracies; or (vi) third-party activities.



---

## 65. next.js
- **URL:** https://github.com/devtechedge/next.js
- **Language:** JavaScript
- **Topics:** None
- **Description:** The React Framework

### README.md

<div align="center">
  <a href="https://nextjs.org">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://assets.vercel.com/image/upload/v1662130559/nextjs/Icon_dark_background.png">
      <img alt="Next.js logo" src="https://assets.vercel.com/image/upload/v1662130559/nextjs/Icon_light_background.png" height="128">
    </picture>
  </a>
  <h1>Next.js</h1>

<a href="https://vercel.com"><img alt="Vercel logo" src="https://img.shields.io/badge/MADE%20BY%20Vercel-000000.svg?style=for-the-badge&logo=Vercel&labelColor=000"></a>
<a href="https://www.npmjs.com/package/next"><img alt="NPM version" src="https://img.shields.io/npm/v/next.svg?style=for-the-badge&labelColor=000000"></a>
<a href="https://github.com/vercel/next.js/blob/canary/license.md"><img alt="License" src="https://img.shields.io/npm/l/next.svg?style=for-the-badge&labelColor=000000"></a>
<a href="https://github.com/vercel/next.js/discussions"><img alt="Join the community on GitHub" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?style=for-the-badge&logo=Next.js&labelColor=000000&logoWidth=20"></a>

</div>

## Getting Started

Used by some of the world's largest companies, Next.js enables you to create full-stack web applications by extending the latest React features, and integrating powerful Rust-based JavaScript tooling for the fastest builds.

- Visit our [Learn Next.js](https://nextjs.org/learn) course to get started with Next.js.
- Visit the [Next.js Showcase](https://nextjs.org/showcase) to see more sites built with Next.js.

## Documentation

Visit [https://nextjs.org/docs](https://nextjs.org/docs) to view the full documentation.

## Community

The Next.js community can be found on [GitHub Discussions](https://github.com/vercel/next.js/discussions) where you can ask questions, voice ideas, and share your projects with other people.

To chat with other community members, you can join the Next.js [Discord](https://nextjs.org/discord) server.

Do note that our [Code of Conduct](https://github.com/vercel/next.js/blob/canary/CODE_OF_CONDUCT.md) applies to all Next.js community channels. Users are **highly encouraged** to read and adhere to it to avoid repercussions.

## Contributing

Contributions to Next.js are welcome and highly appreciated. However, before you jump right into it, we would like you to review our [Contribution Guidelines](/contributing.md) to make sure you have a smooth experience contributing to Next.js.

### Good First Issues:

We have a list of **[good first issues](https://github.com/vercel/next.js/labels/good%20first%20issue)** that contain bugs that have a relatively limited scope. This is a great place for newcomers and beginners alike to get started, gain experience, and get familiar with our contribution process.

---
## Security

If you believe you have found a security vulnerability in Next.js, we encourage you to **_responsibly disclose this and NOT open a public issue_**.

To participate in our Open Source Software Bug Bounty program, please email [responsible.disclosure@vercel.com](mailto:responsible.disclosure@vercel.com). We will add you to the program and provide further instructions for submitting your report.


---

## 66. freighter
- **URL:** https://github.com/devtechedge/freighter
- **Language:** TypeScript
- **Topics:** None
- **Description:** Stellar browser extension

### README.md

# Freighter

Freighter is a non-custodial wallet extension that enables you to sign Stellar
transactions via your browser. Learn more at
[freighter.app](https://www.freighter.app/).

## Yarn Workspaces

This repo is constructed using yarn workspaces and consists of the 4 sections:

- the browser extension (`/extension`)
- the client-facing SDK (`/@stellar/freighter-api`)
- the docs (`/docs`)
- some shared files that the above use (`/@shared/*`)

## Prerequisites

- Node (>= 22): https://nodejs.org/en/download/ (use `nvm use` — the repo has
  `.nvmrc`)
- Yarn 4.10.0: `corepack enable && corepack prepare yarn@4.10.0 --activate`

For a complete setup guide including LLM-assisted quick setup, see
[CONTRIBUTING.MD](CONTRIBUTING.MD).

## Build the extension

To simply build a production version of the extension, install the prerequisites
then navigate to this root folder (`/freighter`) in your command line and run
these 2 steps:

```
yarn install
yarn setup
```

followed by

```
yarn build:extension:production
```

This will generate the files that make up the extension in `extension/build`

## Configure environment variables

Before starting the dev server, you need to configure the backend URLs. Create a
file `extension/.env` with the following variables:

```
INDEXER_URL=your_backend_v1_prod_url_here
INDEXER_V2_URL=your_backend_v2_prod_url_here

```

These URLs should point to your deployment of Freighter backend. For more
details on backend configuration, see
[extension/README.md](extension/README.md#configure-the-backend).

If you're running the backends locally, follow the setup instructions in
[stellar/freighter-backend](https://github.com/stellar/freighter-backend) (V1)
and
[stellar/freighter-backend-v2](https://github.com/stellar/freighter-backend-v2)
(V2).

## Starting a dev environment

```
yarn setup
yarn start
```

This will start up multiple watching builds in parallel:

- The `@stellar/freighter-api` npm module
- The docs, serving on `localhost:3000`
- A dev server with the webapp running in the extension, serving on
  `localhost:9000`
- The actual built extension, able to be installed in Chrome or Firefox, in
  `build/`

Each of these will build in response to editing their source.

These can be started individually with `yarn start:\<workspace name\>` where
`\<workspace name\>` is one of:

- `freighter-api`
- `docs`
- `extension`

```
yarn build
```

This will produce final output for the docs, the `@stellar/freighter` npm
module, and the extension.

`yarn build:\<workspace name\>`, like the equivalent start commands, will build
an individual workspace.

### Testing for Safari

First you should allow unsigned extension in your safari session. This resets
every time Safari shuts down.
https://developer.apple.com/documentation/safariservices/safari_web_extensions/running_your_safari_web_extension#3744467

Next, run the Safari Extension Converter locally to convert Freighter to an
xcode project. Example from the project root -
`xcrun safari-web-extension-converter freighter/extension/build --project-location freighter-safari`

That should launch your project in xcode. You should run the project, with a
target of macos. If you have not allowed unsigned extensions, you will see a
related warning but otherwise you should see Freighter launched on your Safari
instance.

### Useful URLs:

[Configure the backend](https://github.com/stellar/freighter/blob/master/extension/README.md#configure-the-backend)

[Build the extension and install it on your machine](https://github.com/stellar/freighter/blob/master/extension/README.md#build-the-extension-and-install-it-on-your-machine)

[The popup webapp](http://localhost:9000/#/)

[The `setAllowed` playground](http://localhost:3000/docs/playground/setAllowed)

[The `requestAccess` playground](http://localhost:3000/docs/playground/requestAccess)

[The `getAddress` playground](http://localhost:3000/docs/playground/getAddress)

[The `signTransaction` playground](http://localhost:3000/docs/playground/signTransaction)

[The `addToken` playground](http://localhost:3000/docs/playground/addToken)

It's important to note that these last functions won't interact with the _dev
server_ popup UI on `localhost:9000` — you'll need to re-install the unpacked
extension each time you make a change.

### Importing a workspace

In some cases, you will want to import a workspace into another. For example, in
`extension` we need to import `@shared/constants`. To do this, simply add
`@shared/constants` to the dependencies list in package.json in `extension`.
Yarn symlinks all the workspaces, so doing so will allow you to import files
from the `@shared/constants` workspace as if it were a published npm package.

### Dependencies

Many dev dependencies (such as Typescript, linters, Webpack, etc.) have been
moved to the root `package.json` to allow devs to upgrade these libraries all in
one place.

### Pushing to repo

This repo will run a pre-push hook before pushing. This hook will run the cmd
`yarn build:extension:translations` to check if any strings in the extension
need to be added to the translations JSON. If there is no need to update the
translations JSON, the push will go through. If there is a need to update, the
changes will be automatically committed to your branch and the push will be
aborted. You will need to run `git push` again.

NOTE: If you're using nvm and run into an error where the git hook is using an
incompatible version of node, create a file `~/.huskryc` on your system and
added the following:

```
# This loads nvm.sh, sets the correct PATH before running hook, and ensures the project version of Node
export NVM_DIR="$HOME/.nvm"

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# If you have an .nvmrc file, we use the relevant node version
if [[ -f ".nvmrc" ]]; then
  nvm use
fi
```

This will instruct the git hook to use the .nvmrc found in this repo.


---

## 67. wallet-core
- **URL:** https://github.com/devtechedge/wallet-core
- **Language:** C++
- **Topics:** None
- **Description:** Cross-platform, cross-blockchain wallet library.

### README.md

<img src="docs/banner.png" align="center" title="Trust logo">

Trust Wallet Core is an open-source, cross-platform, mobile-focused library
implementing low-level cryptographic wallet functionality for a high number of blockchains.
It is a core part of the popular [Trust Wallet](https://trustwallet.com), and some other projects.
Most of the code is C++ with a set of strict C interfaces, and idiomatic interfaces for supported languages:
Swift for iOS and Java (Kotlin) for Android.

[![iOS CI](https://github.com/trustwallet/wallet-core/actions/workflows/ios-ci.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/ios-ci.yml)
[![Android CI](https://github.com/trustwallet/wallet-core/actions/workflows/android-ci.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/android-ci.yml)
[![Linux CI](https://github.com/trustwallet/wallet-core/actions/workflows/linux-ci.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/linux-ci.yml)
[![Rust CI](https://github.com/trustwallet/wallet-core/actions/workflows/linux-ci-rust.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/linux-ci-rust.yml)
[![Wasm CI](https://github.com/trustwallet/wallet-core/actions/workflows/wasm-ci.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/wasm-ci.yml)
[![Kotlin CI](https://github.com/trustwallet/wallet-core/actions/workflows/kotlin-ci.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/kotlin-ci.yml)
[![Docker CI](https://github.com/trustwallet/wallet-core/actions/workflows/docker.yml/badge.svg)](https://github.com/trustwallet/wallet-core/actions/workflows/docker.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=TrustWallet_wallet-core&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=TrustWallet_wallet-core)

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/trustwallet/wallet-core)
![GitHub](https://img.shields.io/github/license/TrustWallet/wallet-core.svg)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/trustwallet/wallet-core)
![SPM](https://img.shields.io/badge/SPM-ready-blue)
![Cocoapods](https://img.shields.io/cocoapods/v/TrustWalletCore.svg)

# Documentation

For comprehensive documentation, see [developer.trustwallet.com](https://developer.trustwallet.com/wallet-core).

# Audit Reports

Security Audit reports can be found in the [audit](audit) directory.

# Supported Blockchains

Wallet Core supports more than **130** blockchains: Bitcoin, Ethereum, BNB, Cosmos, Solana, and most major blockchain platforms.
The full list is [here](docs/registry.md).

# Building

For build instructions, see [developer.trustwallet.com/wallet-core/building](https://developer.trustwallet.com/wallet-core/building).


# Using from your project

If you want to use wallet core in your project follow these instructions.

## Android

Android releases are hosted on [GitHub packages](https://github.com/trustwallet/wallet-core/packages/700258), you need to add GitHub access token to install it. Please check out [this installation guide](https://developer.trustwallet.com/wallet-core/integration-guide/android-guide#adding-library-dependency) or `build.gradle` from our [android sample](https://github.com/trustwallet/wallet-core/blob/master/samples/android/build.gradle)

Don't forget replacing the version in the code with latest: ![GitHub release (latest by date)](https://img.shields.io/github/v/release/trustwallet/wallet-core)

## iOS

We currently support Swift Package Manager and CocoaPods (will discontinue in the future).

### SPM

Download latest `Package.swift` from [GitHub Releases](https://github.com/trustwallet/wallet-core/releases) and put it in a local `WalletCore` folder.

Add this line to the `dependencies` parameter in your `Package.swift`:

```swift
.package(name: "WalletCore", path: "../WalletCore"),
```

Or add remote url + `master` branch, it points to recent (not always latest) binary release.

```swift
.package(name: "WalletCore", url: "https://github.com/trustwallet/wallet-core", .branchItem("master")),
```

Then add libraries to target's `dependencies`:

```swift
.product(name: "WalletCore", package: "WalletCore"),
.product(name: "WalletCoreSwiftProtobuf", package: "WalletCore"),
```

### CocoaPods

Add this line to your Podfile and run `pod install`:

```ruby
pod 'TrustWalletCore'
```

## NPM (beta)

```js
npm install @trustwallet/wallet-core
```

## Go (beta)

Please check out the [Go integration sample](https://github.com/trustwallet/wallet-core/tree/master/samples/go).

## Kotlin Multipleplatform (beta)

Please check out the [Kotlin Multiplatform sample](https://github.com/trustwallet/wallet-core/tree/master/samples/kmp)

# Projects

Projects using Trust Wallet Core. Add yours too!

[<img src="https://trustwallet.com/icon.svg" alt="Trust Wallet"/>](https://trustwallet.com)

[Coinpaprika](https://coinpaprika.com/)
| [crypto.com](https://crypto.com)
| [Frontier](https://frontier.xyz/)
| [Tokenary](https://tokenary.io/)
| [MemesWallet](https://planetmemes.com/)
| [xPortal](https://xportal.com/)
| [Slingshot](https://slingshot.finance/)
| [ECOIN Wallet](https://play.google.com/store/apps/details?id=org.ecoinwallet&pcampaignid=web_share)

# Community

There are a few community-maintained projects that extend Wallet Core to some additional platforms and languages. Note this is not an endorsement, please do your own research before using them:

- Flutter binding https://github.com/weishirongzhen/flutter_trust_wallet_core
- Python binding https://github.com/phuang/wallet-core-python
- Wallet Core on Windows https://github.com/kaetemi/wallet-core-windows

# Contributing

The best way to submit feedback and report bugs related to WalletCore is to [open a GitHub issue](https://github.com/trustwallet/wallet-core/issues/new).
If the bug is not related to WalletCore but to the TrustWallet app, please [create a Customer Support ticket](https://support.trustwallet.com/en/support/tickets/new).
If you want to contribute code please see [Contributing](https://developer.trustwallet.com/wallet-core/contributing).
If you want to add support for a new blockchain also see [Adding Support for a New Blockchain](https://developer.trustwallet.com/wallet-core/newblockchain), make sure you have read the [requirements](https://developer.trustwallet.com/wallet-core/newblockchain#requirements) section.

Thanks to all the people who contribute.
<a href="https://github.com/trustwallet/wallet-core/graphs/contributors"><img src="https://opencollective.com/wallet-core/contributors.svg?width=890&button=false" /></a>

# Disclaimer

The Wallet Core project is led and managed by Trust Wallet with a large contributor community and actively used in several projects.  Our goal at Wallet Core is to give other wallets an easy way to add chain support.

Trust Wallet products leverage wallet core, however, they may or may not leverage all the capabilities, features, and assets available in wallet core due to their own product requirements.

# License

Trust Wallet Core is available under the Apache 2.0 license. See the [LICENSE](LICENSE) file for more info.


---

## 68. program-examples
- **URL:** https://github.com/devtechedge/program-examples
- **Language:** TypeScript
- **Topics:** None
- **Description:** A repository of Solana program examples

### README.md

# Program Examples

## Onchain program examples for ⚓ Anchor, 🤥 Pinocchio, and 🦀 Native Rust.

[![Anchor](https://github.com/solana-developers/program-examples/actions/workflows/anchor.yml/badge.svg?event=schedule)](https://github.com/solana-developers/program-examples/actions/workflows/anchor.yml) [![Pinocchio](https://github.com/solana-developers/program-examples/actions/workflows/solana-pinocchio.yml/badge.svg?event=schedule)](https://github.com/solana-developers/program-examples/actions/workflows/solana-pinocchio.yml) [![Native](https://github.com/solana-developers/program-examples/actions/workflows/solana-native.yml/badge.svg?event=schedule)](https://github.com/solana-developers/program-examples/actions/workflows/solana-native.yml)

This repo contains Solana onchain programs (referred to as 'Smart Contracts' in other blockchains).

> [!NOTE]
> If you're new to Solana, you don't need to create your own programs to perform basic things like making accounts, creating tokens, sending tokens, or minting NFTs. These common tasks are handled with existing programs, for example the System Program (for making account or transferring SOL) or the token program (for creating tokens and NFTs). See the [Solana Developer site](https://solana.com/developers) to learn more.

> ⚠️ This repository uses **pnpm** as the default package manager.  
> Ensure pnpm is installed before running any examples.

Each folder includes examples for one or more of the following:

- `anchor` - Written using [Anchor](https://www.anchor-lang.com/), the most popular framework for Solana development, which uses Rust.
  Use `anchor build` and `anchor deploy` to build and deploy the program.
  Tests should be executed using `pnpm test` as defined in the `Anchor.toml` scripts section.

- `pinocchio` - Written using [Pinocchio](https://github.com/febo/pinocchio), a zero-copy, zero-allocation library for Solana programs.
  Build and test commands are the same as native examples.
  Run `pnpm test` to execute tests.

- `native` - Written using Solana's native Rust crates and vanilla Rust.
  Build and test commands are defined via pnpm scripts and use `litesvm` for testing.
  Run `pnpm test` to execute tests.

**If a given example is missing, please send us a PR to add it!** Our aim is to have every example available in every option. We'd also love to see more programs involving staking, wrapped tokens, oracles, compression and VRF. Follow the [contributing guidelines](./CONTRIBUTING.md) to keep things consistent.

## The example programs

## Basics

### Hello world

[Hello World on Solana! A minimal program that logs a greeting.](./basics/hello-solana/README.md)

[anchor](./basics/hello-solana/anchor) [pinocchio](./basics/hello-solana/pinocchio) [native](./basics/hello-solana/native)

### Account-data

Store and retrieve data using Solana accounts.

[anchor](./basics/account-data/anchor) [pinocchio](./basics/account-data/pinocchio) [native](./basics/account-data/native)

### Storing global state - Counter

[Store global state in an account, making a counter that increments when called.](./basics/counter/README.md)

[anchor](./basics/counter/anchor) [pinocchio](./basics/counter/pinocchio) [native](./basics/counter/native)

### Saving per-user state - Favorites

Save and update per-user state on the blockchain, ensuring users can only update their own information.

[anchor](./basics/favorites/anchor) [pinocchio](./basics/favorites/pinocchio) [native](./basics/favorites/native)

### Checking Instruction Accounts

[Check that the accounts provided in incoming instructions meet particular criteria.](./basics/checking-accounts/README.md)

[anchor](./basics/checking-accounts/anchor) [pinocchio](./basics/checking-accounts/pinocchio) [native](./basics/checking-accounts/native)

### Closing Accounts

Close an account and get the Lamports back.

[anchor](./basics/close-account/anchor) [pinocchio](./basics/close-account/pinocchio) [native](./basics/close-account/native)

### Creating Accounts

[Make new accounts on the blockchain, calculating the necessary minimum rent from the account's size.](./basics/create-account/README.md)

[anchor](./basics/create-account/anchor) [pinocchio](./basics/create-account/pinocchio) [native](./basics/create-account/native)

### Cross program invocations

[Invoke an instruction handler from one onchain program in another onchain program.](./basics/cross-program-invocation/README.md)

[anchor](./basics/cross-program-invocation/anchor) [native](./basics/cross-program-invocation/native)

### PDA rent-payer

[Use a PDA to pay the rent for the creation of a new account.](./basics/pda-rent-payer/README.md)

[anchor](./basics/pda-rent-payer/anchor) [pinocchio](./basics/pda-rent-payer/pinocchio) [native](./basics/pda-rent-payer/native)

### Processing instructions

[Add parameters to an instruction handler and use them.](./basics/processing-instructions/README.md)

[anchor](./basics/processing-instructions/anchor) [pinocchio](./basics/processing-instructions/pinocchio) [native](./basics/processing-instructions/native)

### Storing date in program derived addresses

Store and retrieve state in Solana.

[anchor](./basics/program-derived-addresses/anchor) [pinocchio](./basics/program-derived-addresses/pinocchio) [native](./basics/program-derived-addresses/native)

### Handling accounts that expand in size

How to store state that changes size in Solana.

[anchor](./basics/realloc/anchor) [pinocchio](./basics/realloc/pinocchio) [native](./basics/realloc/native)

### Laying out larger programs

[Layout larger Solana onchain programs.](./basics/repository-layout/README.md)

[anchor](./basics/repository-layout/anchor) [native](./basics/repository-layout/native)

### Transferring SOL

[Send SOL between two accounts.](./basics/transfer-sol/README.md)

[anchor](./basics/transfer-sol/anchor) [pinocchio](./basics/transfer-sol/pinocchio) [native](./basics/transfer-sol/native)

## Tokens

### Creating tokens

[Create a token on Solana with a token symbol and icon.](./tokens/create-token/README.md)

[anchor](./tokens/create-token/anchor) [pinocchio](./tokens/create-token/pinocchio) [native](./tokens/create-token/native)

### NFT operations

Create an NFT collection, mint NFTs, and verify NFTs as part of a collection using Metaplex Token Metadata. Reminder: you don't need your own program just to mint an NFT, see the note at the top of this README.

[anchor](./tokens/nft-operations/anchor) [pinocchio](./tokens/nft-operations/pinocchio)

### Transferring Tokens

[Create a token mint, mint tokens, and transfer tokens between accounts.](./tokens/transfer-tokens/README.md)

[anchor](./tokens/transfer-tokens/anchor) [pinocchio](./tokens/transfer-tokens/pinocchio) [native](./tokens/transfer-tokens/native)

### Allowing users to swap digital assets - Escrow

Allow two users to swap digital assets with each other, each getting 100% of what the other has offered due to the power of decentralization!

[anchor](./tokens/escrow/anchor) [pinocchio](./tokens/escrow/pinocchio) [native](./tokens/escrow/native)

### Fundraising with SPL Tokens

Create a fundraiser account specifying a target mint and amount, allowing contributors to deposit tokens until the goal is reached.

[anchor](./tokens/token-fundraiser/anchor)

### Distributing tokens with Merkle-proof claims

[Fund a vault once, publish a Merkle root of a balance snapshot, and let each holder claim their allocation with a proof](./tokens/merkle-tree-token-claimer/README.md) — the claim pattern behind large airdrops and chain migrations.

[anchor](./tokens/merkle-tree-token-claimer/anchor)

### Minting a token from inside a program with a PDA as the mint authority

[Mint a Token from inside your own onchain program using the Token program.](./tokens/pda-mint-authority/README.md) Reminder: you don't need your own program just to mint an NFT, see the note at the top of this README.

[anchor](./tokens/pda-mint-authority/anchor) [native](./tokens/pda-mint-authority/native) [pinocchio](./tokens/pda-mint-authority/pinocchio)

### Creating an Automated Market Maker

[Create liquidity pools to allow trading of new digital assets and allows users that provide liquidity to be rewarded by creating an Automated Market Maker.](./tokens/token-swap/README.md)

[anchor](./tokens/token-swap/anchor)

### External delegate token master

Control token transfers using an external secp256k1 delegate signature.

[anchor](./tokens/external-delegate-token-master/anchor)

## Token Extensions

### Basics - create token mints, mint tokens, and transfer tokens with Token Extensions

Create token mints, mint tokens, and transfer tokens using Token Extensions.

[anchor](./tokens/token-2022/basics/anchor)

### Preventing CPIs with CPI guard

Enable CPI guard to prevents certain token action from occurring within CPI (Cross-Program Invocation).

[anchor](./tokens/token-2022/cpi-guard/anchor)

### Using default account state

Create new token accounts that are frozen by default.

[anchor](./tokens/token-2022/default-account-state/anchor) [native](./tokens/token-2022/default-account-state/native)

### Grouping tokens

Create tokens that belong to larger groups of tokens using the Group Pointer extension.

[anchor](./tokens/token-2022/group/anchor)

### Creating token accounts whose owner cannot be changed

Create tokens whose owning program cannot be changed.

[anchor](./tokens/token-2022/immutable-owner/anchor)

### Interest bearing tokens

Create tokens that show an 'interest' calculation.

[anchor](./tokens/token-2022/interest-bearing/anchor)

### Requiring transactions to include descriptive memos

Create tokens where transfers must have a memo describing the transaction attached.

[anchor](./tokens/token-2022/memo-transfer/anchor)

### Adding on-chain metadata to the token mint

Create tokens that store their onchain metadata inside the token mint, without needing to use or pay for additional programs.

[anchor](./tokens/token-2022/metadata/anchor)

### Storing NFT metadata using the metadata pointer extension

Create an NFT using the Token Extensions metadata pointer, storing onchain metadata (including custom fields) inside the mint account itself.

[anchor](./tokens/token-2022/nft-meta-data-pointer/anchor)

### Allow a designated account to close a mint

Allow a designated account to close a Mint.

[anchor](./tokens/token-2022/mint-close-authority/anchor) [native](./tokens/token-2022/mint-close-authority/native) [pinocchio](./tokens/token-2022/mint-close-authority/pinocchio)

### Using multiple token extensions

Use multiple Token Extensions at once.

[native](./tokens/token-2022/multiple-extensions/native)

### Non-transferrable - create tokens that can't be transferred.

Create tokens that cannot be transferred.

[anchor](./tokens/token-2022/non-transferable/anchor) [native](./tokens/token-2022/non-transferable/native) [pinocchio](./tokens/token-2022/non-transferable/pinocchio)

### Permanent Delegate - Create tokens permanently under the control of a particular account

Create tokens that remain under the control of an account, even when transferred elsewhere.

[anchor](./tokens/token-2022/permanent-delegate/anchor)

### Create tokens with a transfer-fee.

Create tokens with an inbuilt transfer fee.

[anchor](./tokens/token-2022/transfer-fee/anchor) [native](./tokens/token-2022/transfer-fee/native)

### Transfer hook - hello world

A minimal transfer hook program that executes custom logic on every token transfer.

[anchor](./tokens/token-2022/transfer-hook/hello-world/anchor)

### Transfer hook - counter

Count how many times tokens have been transferred using a transfer hook.

[anchor](./tokens/token-2022/transfer-hook/counter/anchor)

### Transfer hook - using account data as seed

Use token account owner data as seeds to derive extra accounts in a transfer hook.

[anchor](./tokens/token-2022/transfer-hook/account-data-as-seed/anchor)

### Transfer hook - allow/block list

Restrict or allow token transfers using an on-chain allow/block list managed by a list authority.

[anchor](./tokens/token-2022/transfer-hook/allow-block-list-token/anchor)

### Transfer hook - block list with Codama clients

A block-list transfer hook as a full project: Pinocchio program, Codama-generated Rust and TypeScript clients, and a CLI.

[pinocchio](./tokens/token-2022/transfer-hook/block-list/pinocchio)

### Transfer hook - transfer cost

Charge an additional cost or fee on every token transfer using a transfer hook.

[anchor](./tokens/token-2022/transfer-hook/transfer-cost/anchor)

### Transfer hook - transfer switch

Enable or disable token transfers with an on-chain switch using a transfer hook.

[anchor](./tokens/token-2022/transfer-hook/transfer-switch/anchor)

## Compression

### Cnft-burn

Burn compressed NFTs.

[anchor](./compression/cnft-burn/anchor)

### Cnft-vault

Store Metaplex compressed NFTs inside a PDA.

[anchor](./compression/cnft-vault/anchor)

### Cutils

Work with Metaplex compressed NFTs.

[anchor](./compression/cutils/anchor)

## Cryptography

One stateless program per curve, wrapping the raw cryptographic syscalls. These run in LiteSVM today but only work on public clusters once their feature gates activate. Applied examples (multisig, key registry, encrypted ballot) live in the [crypto-primitives-examples](https://github.com/solana-foundation/crypto-primitives-examples) reference repo.

### BN254 (alt_bn128) operations

Add and scalar-multiply G2 points (SIMD-0302) and verify aggregate BLS signatures with a single pairing check, via the `sol_alt_bn128_group_op` syscall.

[pinocchio](./cryptography/bn254/pinocchio)

### BLS12-381 curve operations

Add, subtract, and scalar-multiply BLS12-381 G1 and G2 points with the `sol_curve_group_op` syscall.

[pinocchio](./cryptography/bls12-381/pinocchio)

## Oracles

### pyth

Use a data source for offchain data (called an Oracle) to perform activities onchain.

[anchor](./oracles/pyth/anchor)

## Games

### World Cup bracket prediction

A bracket-prediction game: entrants pay a fee to submit a 32-game bracket, an oracle posts results, scores are tallied on-chain, and the unique winner sweeps the pot. A full Pinocchio + Codama project with a TypeScript client and a webapp.

[pinocchio](./games/world-cup/pinocchio)

### Gacha (provably-fair pack pulls)

A provably-fair gacha / loot-box game — the on-chain mechanic behind RWA pack platforms like Collector Crypt and Phygitals. Buyers open pulls revealed with an RFC 9381 ECVRF anchored in the deployed [`cc-vrf`](https://vrf.collectorcrypt.com) registry by CPI; the VRF input binds buyer entropy, reveals are publicly verifiable off-chain, unsettled pulls are refundable, and prizes are minted as Token-2022 NFTs carrying a `rarity` metadata field. A full Pinocchio + Codama project with TypeScript + Rust clients.

[pinocchio](./games/gacha/pinocchio)

---


---

## 69. safe-docs
- **URL:** https://github.com/devtechedge/safe-docs
- **Language:** MDX
- **Topics:** None
- **Description:** Developer Docs for building on Safe.

### README.md

# Safe Documentation

[![License](https://img.shields.io/github/license/safe-global/safe-docs)](https://github.com/safe-global/safe-docs/blob/main/LICENSE.md)
![GitHub package.json version (branch)](https://img.shields.io/github/package-json/v/safe-global/safe-docs)

This repository hosts [Safe](https://safe.global) documentation.

The documentation is built with [Nextra](https://nextra.site) and is live at [docs.safe.global](https://docs.safe.global).

## Installation

Install the dependencies using [pnpm](https://pnpm.io):

```
pnpm install
```

## Development

Git hooks are set up to run tests and linting checks before every `git push`. These hooks can be executed locally by running the following command:

```
pnpm prepush
```

All links in the documentation are checked for validity on every pull request. These checks can be executed locally by running the following command:

```
pnpm linkcheck
```

## Execution

The project can be run with a server that's executed in development and production mode.

### Development mode

Run the server in development mode using the following command:

```
pnpm dev
```

### Production mode

Build the project:

```
pnpm build
```

Run the server in production mode using the following command:

```
pnpm start
```

## Testing

Create an environment file in the root of the project and copy the content from the `.env.example` file using the following command:

```
cp .env.example .env
```

Remember to update the environment variables once the `.env` file is created.

Run the tests using the following command:

```
pnpm test
```

## License

This project is licensed under the [MIT License](./LICENSE.md).

## Contributing

Contributions are more than welcome! Please open an issue or create a pull request by following our [contributions guidelines](./CONTRIBUTING.md).


---

## 70. ruff
- **URL:** https://github.com/devtechedge/ruff
- **Language:** Rust
- **Topics:** None
- **Description:** An extremely fast Python linter and code formatter, written in Rust.

### README.md

<!-- Begin section: Overview -->

# Ruff

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/v/ruff.svg)](https://pypi.python.org/pypi/ruff)
[![image](https://img.shields.io/pypi/l/ruff.svg)](https://github.com/astral-sh/ruff/blob/main/LICENSE)
[![image](https://img.shields.io/pypi/pyversions/ruff.svg)](https://pypi.python.org/pypi/ruff)
[![Actions status](https://github.com/astral-sh/ruff/workflows/CI/badge.svg)](https://github.com/astral-sh/ruff/actions)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.com/invite/astral-sh)

[**Docs**](https://docs.astral.sh/ruff/) | [**Playground**](https://play.ruff.rs/)

An extremely fast Python linter and code formatter, written in Rust.

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg">
    <img alt="Shows a bar chart with benchmark results." src="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg">
  </picture>
</p>

<p align="center">
  <i>Linting the CPython codebase from scratch.</i>
</p>

- ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
- 🐍 Installable via `pip`
- 🛠️ `pyproject.toml` support
- 🤝 Python 3.14 compatibility
- ⚖️ Drop-in parity with [Flake8](https://docs.astral.sh/ruff/faq/#how-does-ruffs-linter-compare-to-flake8), [isort](https://docs.astral.sh/ruff/faq/#how-does-ruffs-import-sorting-compare-to-isort), and [Black](https://docs.astral.sh/ruff/faq/#how-does-ruffs-formatter-compare-to-black)
- 📦 Built-in caching, to avoid re-analyzing unchanged files
- 🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
- 📏 Over [900 built-in rules](https://docs.astral.sh/ruff/rules/), with native re-implementations
    of popular Flake8 plugins, like flake8-bugbear
- ⌨️ First-party [editor integrations](https://docs.astral.sh/ruff/editors) for [VS Code](https://github.com/astral-sh/ruff-vscode) and [more](https://docs.astral.sh/ruff/editors/setup)
- 🌎 Monorepo-friendly, with [hierarchical and cascading configuration](https://docs.astral.sh/ruff/configuration/#config-file-discovery)

Ruff aims to be orders of magnitude faster than alternative tools while integrating more
functionality behind a single, common interface.

Ruff can be used to replace [Flake8](https://pypi.org/project/flake8/) (plus dozens of plugins),
[Black](https://github.com/psf/black), [isort](https://pypi.org/project/isort/),
[pydocstyle](https://pypi.org/project/pydocstyle/), [pyupgrade](https://pypi.org/project/pyupgrade/),
[autoflake](https://pypi.org/project/autoflake/), and more, all while executing tens or hundreds of
times faster than any individual tool.

Ruff is extremely actively developed and used in major open-source projects like:

- [Apache Airflow](https://github.com/apache/airflow)
- [Apache Superset](https://github.com/apache/superset)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Hugging Face](https://github.com/huggingface/transformers)
- [Pandas](https://github.com/pandas-dev/pandas)
- [SciPy](https://github.com/scipy/scipy)

Ruff is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [ty](https://github.com/astral-sh/ty).

Read the [launch
post](https://astral.sh/blog/announcing-astral-the-company-behind-ruff), or the
original [project
announcement](https://notes.crmarsh.com/python-tooling-could-be-much-much-faster).

## Testimonials

[**Sebastián Ramírez**](https://twitter.com/tiangolo/status/1591912354882764802), creator
of [FastAPI](https://github.com/tiangolo/fastapi):

> Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually
> running and checking the code.

[**Nick Schrock**](https://twitter.com/schrockn/status/1612615862904827904), founder of [Elementl](https://www.elementl.com/),
co-creator of [GraphQL](https://graphql.org/):

> Why is Ruff a gamechanger? Primarily because it is nearly 1000x faster. Literally. Not a typo. On
> our largest module (dagster itself, 250k LOC) pylint takes about 2.5 minutes, parallelized across 4
> cores on my M1. Running ruff against our _entire_ codebase takes .4 seconds.

[**Bryan Van de Ven**](https://github.com/bokeh/bokeh/pull/12605), co-creator
of [Bokeh](https://github.com/bokeh/bokeh/), original author
of [Conda](https://docs.conda.io/en/latest/):

> Ruff is ~150-200x faster than flake8 on my machine, scanning the whole repo takes ~0.2s instead of
> ~20s. This is an enormous quality of life improvement for local dev. It's fast enough that I added
> it as an actual commit hook, which is terrific.

[**Timothy Crosley**](https://twitter.com/timothycrosley/status/1606420868514877440),
creator of [isort](https://github.com/PyCQA/isort):

> Just switched my first project to Ruff. Only one downside so far: it's so fast I couldn't believe
> it was working till I intentionally introduced some errors.

[**Tim Abbott**](https://github.com/zulip/zulip/pull/23431#issuecomment-1302557034), lead developer of [Zulip](https://github.com/zulip/zulip) (also [here](https://github.com/astral-sh/ruff/issues/465#issuecomment-1317400028)):

> This is just ridiculously fast... `ruff` is amazing.

<!-- End section: Overview -->

## Table of Contents

For more, see the [documentation](https://docs.astral.sh/ruff/).

1. [Getting Started](#getting-started)
1. [Configuration](#configuration)
1. [Rules](#rules)
1. [Contributing](#contributing)
1. [Support](#support)
1. [Acknowledgements](#acknowledgements)
1. [Show Your Support](#show-your-support)
1. [License](#license)

## Getting Started<a id="getting-started"></a>

For more, see the [documentation](https://docs.astral.sh/ruff/).

### Installation

Ruff is available as [`ruff`](https://pypi.org/project/ruff/) on PyPI.

Invoke Ruff directly with [`uvx`](https://docs.astral.sh/uv/):

```shell
uvx ruff@0.16.7 check   # Lint all files in the current directory.
uvx ruff@0.16.7 format  # Format all files in the current directory.
```

Or install Ruff with `uv` (recommended), `pip`, or `pipx`:

```shell
# With uv.
uv tool install ruff@latest  # Install Ruff globally.
uv add --dev ruff            # Or add Ruff to your project.

# With pip.
pip install ruff

# With pipx.
pipx install ruff
```

Starting with version `0.5.0`, Ruff can be installed with our standalone installers:

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/ruff/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/ruff/install.ps1 | iex"

# For a specific version.
curl -LsSf https://astral.sh/ruff/0.16.7/install.sh | sh
powershell -c "irm https://astral.sh/ruff/0.16.7/install.ps1 | iex"
```

You can also install Ruff via [Homebrew](https://formulae.brew.sh/formula/ruff), [Conda](https://anaconda.org/conda-forge/ruff),
and with [a variety of other package managers](https://docs.astral.sh/ruff/installation/).

### Usage

To run Ruff as a linter, try any of the following:

```shell
ruff check                          # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.
ruff check @arguments.txt           # Lint using an input file, treating its contents as newline-delimited command-line arguments.
```

Or, to run Ruff as a formatter:

```shell
ruff format                          # Format all files in the current directory (and any subdirectories).
ruff format path/to/code/            # Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/*.py        # Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py  # Format `file.py`.
ruff format @arguments.txt           # Format using an input file, treating its contents as newline-delimited command-line arguments.
```

Ruff can also be used as a [pre-commit](https://pre-commit.com/) hook via [`ruff-pre-commit`](https://github.com/astral-sh/ruff-pre-commit):

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.16.7
  hooks:
    # Run the linter.
    - id: ruff-check
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
```

Ruff can also be used as a [VS Code extension](https://github.com/astral-sh/ruff-vscode) or with [various other editors](https://docs.astral.sh/ruff/editors/setup).

Ruff can also be used as a [GitHub Action](https://github.com/features/actions) via
[`ruff-action`](https://github.com/astral-sh/ruff-action):

```yaml
name: Ruff
on: [ push, pull_request ]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/ruff-action@v3
```

### Configuration<a id="configuration"></a>

Ruff can be configured through a `pyproject.toml`, `ruff.toml`, or `.ruff.toml` file (see:
[_Configuration_](https://docs.astral.sh/ruff/configuration/), or [_Settings_](https://docs.astral.sh/ruff/settings/)
for a complete list of all configuration options).

For the complete list of enabled rules, see [_Default Rules_](https://docs.astral.sh/ruff/default-rules/).

If left unspecified, Ruff's default configuration is equivalent to the following `ruff.toml` file:

```toml
# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

# Same as Black.
line-length = 88
indent-width = 4

# Assume Python 3.10
target-version = "py310"

[lint]
# select = [...]  # See the Default Rules page for the full listing.
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"
```

Note that, in a `pyproject.toml`, each section header should be prefixed with `tool.ruff`. For
example, `[lint]` should be replaced with `[tool.ruff.lint]`.

Some configuration options can be provided via dedicated command-line arguments, such as those
related to rule enablement and disablement, file discovery, and logging level:

```shell
ruff check --select F401 --select F403 --quiet
```

The remaining configuration options can be provided through a catch-all `--config` argument:

```shell
ruff check --config "lint.per-file-ignores = {'some_file.py' = ['F841']}"
```

To opt in to the latest lint rules, formatter style changes, interface updates, and more, enable
[preview mode](https://docs.astral.sh/ruff/preview/) by setting `preview = true` in your configuration
file or passing `--preview` on the command line. Preview mode enables a collection of unstable
features that may change prior to stabilization.

See `ruff help` for more on Ruff's top-level commands, or `ruff help check` and `ruff help format`
for more on the linting and formatting commands, respectively.

## Rules<a id="rules"></a>

<!-- Begin section: Rules -->

**Ruff supports over 900 lint rules**, many of which are inspired by popular tools like Flake8,
isort, pyupgrade, and others. Regardless of the rule's origin, Ruff re-implements every rule in
Rust as a first-party feature.

By default, Ruff enables rules from the `F`, `E`, `B`, `UP`, and `RUF` categories,
as well as many more, omitting any stylistic rules that overlap with the use of a formatter, like
`ruff format` or [Black](https://github.com/psf/black).

If you're just getting started with Ruff, **the default rule set is a great place to start**: it
catches a wide variety of common errors (like unused imports) with zero configuration. See
[_Default Rules_](https://docs.astral.sh/ruff/default-rules/) for the complete list.

<!-- End section: Rules -->

Beyond the defaults, Ruff re-implements some of the most popular Flake8 plugins and related code
quality tools, including:

- [autoflake](https://pypi.org/project/autoflake/)
- [eradicate](https://pypi.org/project/eradicate/)
- [flake8-2020](https://pypi.org/project/flake8-2020/)
- [flake8-annotations](https://pypi.org/project/flake8-annotations/)
- [flake8-async](https://pypi.org/project/flake8-async)
- [flake8-bandit](https://pypi.org/project/flake8-bandit/) ([#1646](https://github.com/astral-sh/ruff/issues/1646))
- [flake8-blind-except](https://pypi.org/project/flake8-blind-except/)
- [flake8-boolean-trap](https://pypi.org/project/flake8-boolean-trap/)
- [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
- [flake8-builtins](https://pypi.org/project/flake8-builtins/)
- [flake8-commas](https://pypi.org/project/flake8-commas/)
- [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/)
- [flake8-copyright](https://pypi.org/project/flake8-copyright/)
- [flake8-datetimez](https://pypi.org/project/flake8-datetimez/)
- [flake8-debugger](https://pypi.org/project/flake8-debugger/)
- [flake8-django](https://pypi.org/project/flake8-django/)
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
- [flake8-eradicate](https://pypi.org/project/flake8-eradicate/)
- [flake8-errmsg](https://pypi.org/project/flake8-errmsg/)
- [flake8-executable](https://pypi.org/project/flake8-executable/)
- [flake8-future-annotations](https://pypi.org/project/flake8-future-annotations/)
- [flake8-gettext](https://pypi.org/project/flake8-gettext/)
- [flake8-implicit-str-concat](https://pypi.org/project/flake8-implicit-str-concat/)
- [flake8-import-conventions](https://github.com/joaopalmeiro/flake8-import-conventions)
- [flake8-logging](https://pypi.org/project/flake8-logging/)
- [flake8-logging-format](https://pypi.org/project/flake8-logging-format/)
- [flake8-no-pep420](https://pypi.org/project/flake8-no-pep420)
- [flake8-pie](https://pypi.org/project/flake8-pie/)
- [flake8-print](https://pypi.org/project/flake8-print/)
- [flake8-pyi](https://pypi.org/project/flake8-pyi/)
- [flake8-pytest-style](https://pypi.org/project/flake8-pytest-style/)
- [flake8-quotes](https://pypi.org/project/flake8-quotes/)
- [flake8-raise](https://pypi.org/project/flake8-raise/)
- [flake8-return](https://pypi.org/project/flake8-return/)
- [flake8-self](https://pypi.org/project/flake8-self/)
- [flake8-simplify](https://pypi.org/project/flake8-simplify/)
- [flake8-slots](https://pypi.org/project/flake8-slots/)
- [flake8-super](https://pypi.org/project/flake8-super/)
- [flake8-tidy-imports](https://pypi.org/project/flake8-tidy-imports/)
- [flake8-todos](https://pypi.org/project/flake8-todos/)
- [flake8-type-checking](https://pypi.org/project/flake8-type-checking/)
- [flake8-use-pathlib](https://pypi.org/project/flake8-use-pathlib/)
- [flynt](https://pypi.org/project/flynt/) ([#2102](https://github.com/astral-sh/ruff/issues/2102))
- [isort](https://pypi.org/project/isort/)
- [mccabe](https://pypi.org/project/mccabe/)
- [pandas-vet](https://pypi.org/project/pandas-vet/)
- [pep8-naming](https://pypi.org/project/pep8-naming/)
- [pydocstyle](https://pypi.org/project/pydocstyle/)
- [pygrep-hooks](https://github.com/pre-commit/pygrep-hooks)
- [pylint-airflow](https://pypi.org/project/pylint-airflow/)
- [pyupgrade](https://pypi.org/project/pyupgrade/)
- [tryceratops](https://pypi.org/project/tryceratops/)
- [yesqa](https://pypi.org/project/yesqa/)

For a complete enumeration of the supported rules, see [_Rules_](https://docs.astral.sh/ruff/rules/).

## Contributing<a id="contributing"></a>

Contributions are welcome and highly appreciated. To get started, check out the
[**contributing guidelines**](https://docs.astral.sh/ruff/contributing/).

You can also join us on [**Discord**](https://discord.com/invite/astral-sh).

## Support<a id="support"></a>

Having trouble? Check out the existing issues on [**GitHub**](https://github.com/astral-sh/ruff/issues),
or feel free to [**open a new one**](https://github.com/astral-sh/ruff/issues/new).

You can also ask for help on [**Discord**](https://discord.com/invite/astral-sh).

## Acknowledgements<a id="acknowledgements"></a>

Ruff's linter draws on both the APIs and implementation details of many other
tools in the Python ecosystem, especially [Flake8](https://github.com/PyCQA/flake8), [Pyflakes](https://github.com/PyCQA/pyflakes),
[pycodestyle](https://github.com/PyCQA/pycodestyle), [pydocstyle](https://github.com/PyCQA/pydocstyle),
[pyupgrade](https://github.com/asottile/pyupgrade), and [isort](https://github.com/PyCQA/isort).

In some cases, Ruff includes a "direct" Rust port of the corresponding tool.
We're grateful to the maintainers of these tools for their work, and for all
the value they've provided to the Python community.

Ruff's formatter is built on a fork of Rome's [`rome_formatter`](https://github.com/rome/tools/tree/main/crates/rome_formatter),
and again draws on both API and implementation details from [Rome](https://github.com/rome/tools),
[Prettier](https://github.com/prettier/prettier), and [Black](https://github.com/psf/black).

Ruff's import resolver is based on the import resolution algorithm from [Pyright](https://github.com/microsoft/pyright).

Ruff is also influenced by a number of tools outside the Python ecosystem, like
[Clippy](https://github.com/rust-lang/rust-clippy) and [ESLint](https://github.com/eslint/eslint).

Ruff is the beneficiary of a large number of [contributors](https://github.com/astral-sh/ruff/graphs/contributors).

Ruff is released under the MIT license.

## Show Your Support

If you're using Ruff, consider adding the Ruff badge to your project's `README.md`:

```md
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
```

...or `README.rst`:

```rst
.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff
```

...or, as HTML:

```html
<a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;"></a>
```

## License<a id="license"></a>

This repository is licensed under the [MIT License](https://github.com/astral-sh/ruff/blob/main/LICENSE)

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>


---

## 71. better-auth
- **URL:** https://github.com/devtechedge/better-auth
- **Language:** TypeScript
- **Topics:** None
- **Description:** The most comprehensive authentication framework

### README.md

<div align="center">
  <picture>
    <source srcset="./banner-dark.png" media="(prefers-color-scheme: dark)"/>
    <source srcset="./banner-light.png" media="(prefers-color-scheme: light)"/>
    <img src="./banner-light.png" alt="Better Auth Logo"/>
  </picture>

  [![npm](https://img.shields.io/npm/dm/better-auth?style=flat&colorA=000000&colorB=000000)](https://npm.chart.dev/better-auth?primary=neutral&gray=neutral&theme=dark)
  [![npm version](https://img.shields.io/npm/v/better-auth.svg?style=flat&colorA=000000&colorB=000000)](https://www.npmjs.com/package/better-auth)
  [![GitHub stars](https://img.shields.io/github/stars/better-auth/better-auth?style=flat&colorA=000000&colorB=000000)](https://github.com/better-auth/better-auth/stargazers)

  <p>
    <a href="https://discord.gg/better-auth">Discord</a>
    ·
    <a href="https://better-auth.com">Website</a>
    ·
    <a href="https://github.com/better-auth/better-auth/issues">Issues</a>
  </p>
</div>

## Better Auth

Better Auth is a framework-agnostic authentication (and authorization) framework for TypeScript. It provides a comprehensive set of features out of the box and includes a plugin ecosystem that simplifies adding advanced functionalities with minimal code in a short amount of time. Whether you need 2FA, multi-tenant support, or other complex features, it lets you focus on building your actual application instead of reinventing the wheel.

### Why Better Auth

Authentication in the TypeScript ecosystem is a half-solved problem. Other open-source libraries often require a lot of additional code for anything beyond basic authentication. Rather than just pushing third-party services as the solution, I believe we can do better as a community—hence, Better Auth.

## Contribution

Better Auth is a free and open source project licensed under the [MIT License](./LICENSE.md). You are free to do whatever you want with it.

You could help continuing its development by:

- [Contribute to the source code](./CONTRIBUTING.md)
- [Suggest new features and report issues](https://github.com/better-auth/better-auth/issues)

## Security
If you discover a security vulnerability within Better Auth, please report it via [GitHub Security Advisories](https://github.com/better-auth/better-auth/security/advisories/new).

All reports will be promptly addressed, and you'll be credited accordingly.


---

## 72. sdk-1
- **URL:** https://github.com/devtechedge/sdk-1
- **Language:** TypeScript
- **Topics:** None
- **Description:** Turnkey TypeScript SDK

### README.md

---
title: "Turnkey SDK"
---

# Turnkey SDK

[![js-build](https://github.com/tkhq/sdk/actions/workflows/js-build.yml/badge.svg)](https://github.com/tkhq/sdk/actions/workflows/js-build.yml)

## Overview

The Turnkey SDK includes functionality to interact with Turnkey in various contexts and ecosystems. It consists of three main NPM package groups.

- the [Primary Turnkey SDK Packages](#primary-turnkey-sdk-packages) which expose the main functionality required to build Turnkey-powered applications in different web and mobile environments
- the [Chain/Ecosystem-Specific Signing Packages](#chainecosystem-specific-signing-sdk-packages) which expose signers with support for specific ecosystems, built on top of our SDK packages
- the [Advanced Functionality SDK Packages](#advanced-functionality-sdk-packages) which exposes lower level functionality that is leveraged by our Primary SDK Packages for those with highly-specific implementations looking to use them.

The diagram below helps visualize the packages in our SDK organized by the functionality they expose.

<img src="./img/sdk-map.png" alt="homepage screenshot" width="1000px" />

## Primary Turnkey SDK Packages

The following packages expose the main functionality required to build Turnkey-powered applications. Each package exposes functions, and/or client classes with methods that manage the process of authenticating requests to the Turnkey API in the contexts of a generic browser environment or react client environment, or a server environment.

While these higher level packages are the main points of reference to be used while designing and building Turnkey applications, they wrap other packages with lower level functionality which we also expose separately for those who would like to explore them for more specialized use cases. These packages are listed and described below in the [Advanced Functionality SDK Packages](#advanced-functionality-sdk-packages) section.

Our main web SDK packages are as follows:

| Package                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | NPM                                                                                                                                                     | Changelog                                                   | Docs                                                        |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| [@turnkey/react-wallet-kit](https://github.com/tkhq/sdk/tree/main/packages/react-wallet-kit)               | `@turnkey/react-wallet-kit` is the easiest way to integrate Turnkey’s Embedded Wallets into React applications. It works without requiring you to run your own backend, using Turnkey’s managed Auth Proxy, while still supporting backend-based architectures if needed. Built on @turnkey/core, it provides UI components and ergonomic hooks for quickly building secure embedded wallet experiences. This package supersedes `@turnkey/sdk-react`.                                                                                                                                                                                                                                                                                                                                 | [![npm](https://img.shields.io/npm/v/@turnkey/react-wallet-kit?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/react-wallet-kit)               | [CHANGELOG](/packages/react-wallet-kit/CHANGELOG.md)        | [Docs](https://docs.turnkey.com/sdks/react)                 |
| [@turnkey/react-native-wallet-kit](https://github.com/tkhq/sdk/tree/main/packages/react-native-wallet-kit) | `@turnkey/react-native-wallet-kit` is the easiest way to integrate Turnkey’s Embedded Wallets into React Native applications. It works without requiring you to run your own backend, using Turnkey’s managed Auth Proxy, while still supporting backend-based architectures if needed. Built on @turnkey/core, it provides ergonomic hooks and utilities for quickly building secure embedded wallet experiences. This package supersedes `@turnkey/sdk-react-native`.                                                                                                                                                                                                                                                                                                                | [![npm](https://img.shields.io/npm/v/@turnkey/react-native-wallet-kit?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/react-native-wallet-kit) | [CHANGELOG](/packages/react-native-wallet-kit/CHANGELOG.md) | [Docs](https://docs.turnkey.com/sdks/react-native/overview) |
| [@turnkey/core](/packages/core)                                                                            | `@turnkey/core` is a low-level TypeScript client SDK that provides the foundational building blocks used by Turnkey’s higher-level wallet kits. It includes primitives for interacting with Turnkey’s APIs, session management, stampers, and a raw HTTP client for advanced or custom integrations. This package is primarily intended for framework environments that do not yet have an official Turnkey wallet kit, such as Angular, Vue, or Svelte, or for advanced use cases that require direct access to Turnkey’s lower-level APIs. In most cases you shouldn’t use @turnkey/core directly, React and React Native apps should use the dedicated wallet kits instead. This package supersedes `@turnkey/sdk-browser`.                                                         | [![npm](https://img.shields.io/npm/v/@turnkey/http?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/core)                                       | [CHANGELOG](/packages/core/CHANGELOG.md)                    | [Docs](https://docs.turnkey.com/sdks/typescript-frontend)   |
| [@turnkey/sdk-server](https://github.com/tkhq/sdk/tree/main/packages/sdk-server)                           | The `@turnkey/sdk-server` package exposes functionality that lets developers build server-side functionality for applications that interact with the Turnkey API with different types of authentication – allowing applications to authenticate users, manage sessions, and perform organizational operations securely and efficiently. It consists of an API Client and API Proxies that enable requests to the Turnkey API to be authenticated with the appropriate credentials. Specifically, the API Client manages requests signed by the user's authentication details, and the API proxies handle requests signed by the parent organization's authentication details. Use this package to handle server-side interactions for applications that interact with the Turnkey API. | [![npm](https://img.shields.io/npm/v/@turnkey/sdk-server?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/sdk-server)                           | [CHANGELOG](/packages/sdk-server/CHANGELOG.md)              | [Docs](https://docs.turnkey.com/sdks/javascript-server)     |

The diagram below helps visualize how each package can be used to devlop the appropriate service in your Turnkey Powered Application, and how Turnkey requests would flow between those services.

<img src="./img/sdk-diagram.png" alt="homepage screenshot" width="1000px" />

## Chain/Ecosystem-Specific Signing SDK Packages

The following packages contain chain or ecosystem specific signers that take some of our [Primary Turnkey SDK Packages](#primary-turnkey-sdk-packages) and add additional support based on the signing process or transaction structure relevant to that specific chain or ecosystem.

| Package                                                     | NPM                                                                                                                                         | Description                                                                                       | Changelog                                             |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [`@turnkey/ethers`](/packages/ethers)                       | [![npm](https://img.shields.io/npm/v/@turnkey/ethers?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/ethers)                       | Turnkey Signer for Ethers                                                                         | [CHANGELOG](/packages/ethers/CHANGELOG.md)            |
| [`@turnkey/viem`](/packages/viem)                           | [![npm](https://img.shields.io/npm/v/@turnkey/viem?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/viem)                           | Turnkey Signer for Viem                                                                           | [CHANGELOG](/packages/viem/CHANGELOG.md)              |
| [`@turnkey/cosmjs`](/packages/cosmjs)                       | [![npm](https://img.shields.io/npm/v/@turnkey/cosmjs?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/cosmjs)                       | Turnkey Signer for CosmJS                                                                         | [CHANGELOG](/packages/cosmjs/CHANGELOG.md)            |
| [`@turnkey/solana`](/packages/solana)                       | [![npm](https://img.shields.io/npm/v/@turnkey/solana?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/solana)                       | Turnkey Signer for Solana                                                                         | [CHANGELOG](/packages/solana/CHANGELOG.md)            |
| [`@turnkey/eip-1193-provider`](/packages/eip-1193-provider) | [![npm](https://img.shields.io/npm/v/@turnkey/eip-1193-provider?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/eip-1193-provider) | Turnkey-compatible EIP-1193 Provider                                                              | [CHANGELOG](/packages/eip-1193-provider/CHANGELOG.md) |
| [`@turnkey/gas-station`](/packages/gas-station)             | [![npm](https://img.shields.io/npm/v/@turnkey/gas-station?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/gas-station)             | Implement gasless transactions using EIP-7702, Turnkey wallet management, and your own paymaster. | [CHANGELOG](/packages/gas-station/CHANGELOG.md)       |

## Advanced Functionality SDK Packages

For those with more specialized use cases, Turnkey exposes it's lower level-libraries stamping and encryption libraries to be used directly. Note: for most use-cases, these libraries are not meant to be used directly and we encourage working on designing your application mainly using our [Primary Turnkey SDK Packages](#primary-turnkey-sdk-packages) along with our [Chain and Ecosystem Specific SDK Packages](#chainecosystem-specific-signing-sdk-packages) as per your use case!

### Request Stamping

| Package                                                                                 | NPM                                                                                                                                                                   | Description                                                                                             | Changelog                                                          | Docs                                                                                  |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| [`@turnkey/http`](/packages/http)                                                       | [![npm](https://img.shields.io/npm/v/@turnkey/http?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/http)                                                     | Lower-level, fully typed HTTP client for interacting with Turnkey API                                   | [CHANGELOG](/packages/http/CHANGELOG.md)                           | [Docs](https://docs.turnkey.com/sdks/advanced/turnkey-client)                         |
| [`@turnkey/api-key-stamper`](/packages/api-key-stamper)                                 | [![npm](https://img.shields.io/npm/v/@turnkey/api-key-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/api-key-stamper)                               | Provide API key signatures over Turnkey requests                                                        | [CHANGELOG](/packages/api-key-stamper/CHANGELOG.md)                | [Docs](https://docs.turnkey.com/sdks/advanced/api-key-stamper)                        |
| [`@turnkey/iframe-stamper`](/packages/iframe-stamper)                                   | [![npm](https://img.shields.io/npm/v/@turnkey/iframe-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/iframe-stamper)                                 | Provide API key signatures over Turnkey requests within iframe contexts                                 | [CHANGELOG](/packages/iframe-stamper/CHANGELOG.md)                 | [Docs](https://docs.turnkey.com/sdks/advanced/iframe-stamper)                         |
| [`@turnkey/webauthn-stamper`](/packages/webauthn-stamper)                               | [![npm](https://img.shields.io/npm/v/@turnkey/webauthn-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/webauthn-stamper)                             | Provide Webauthn signatures over Turnkey requests                                                       | [CHANGELOG](/packages/webauthn-stamper/CHANGELOG.md)               | [Docs](https://docs.turnkey.com/sdks/advanced/webauthn-stamper)                       |
| [`@turnkey/wallet-stamper`](/packages/wallet-stamper)                                   | [![npm](https://img.shields.io/npm/v/@turnkey/wallet-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/wallet-stamper)                                 | Provide wallet signatures over Turnkey requests                                                         | [CHANGELOG](/packages/wallet-stamper/CHANGELOG.md)                 | [Docs](https://docs.turnkey.com/sdks/advanced/wallet-stamper)                         |
| [`@turnkey/sdk-react-native-passkey-stamper`](/packages/react-native-passkey-stamper/)  | [![npm](https://img.shields.io/npm/v/@turnkey/react-native-passkey-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/react-native-passkey-stamper)     | Provide Passkey signatures over Turnkey requests in a React Native context                              | [CHANGELOG](/packages/react-native-passkey-stamper/CHANGELOG.md)   | [Docs](https://docs.turnkey.com/sdks/react-native)                                    |
| [`@turnkey/indexed-db-stamper/`](/packages/indexed-db-stamper/)                         | [![npm](https://img.shields.io/npm/v/@turnkey/indexed-db-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/indexed-db-stamper)                         | Enables secure request stamping using an unextractable P-256 keypair stored in the browser’s IndexedDB. | [CHANGELOG](/packages/indexed-db-stamper/CHANGELOG.md)             | [Docs](https://docs.turnkey.com/authentication/sessions#indexeddb-web-only-:)         |
| [`@turnkey/telegram-cloud-storage-stamper/`](/packages/telegram-cloud-storage-stamper/) | [![npm](https://img.shields.io/npm/v/@turnkey/telegram-cloud-storage-stamper?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/telegram-cloud-storage-stamper) | Handles stamping a Turnkey request with an API key stored within Telegram Cloud Storage.                | [CHANGELOG](/packages/telegram-cloud-storage-stamper/CHANGELOG.md) | [Docs](https://github.com/tkhq/sdk/tree/main/packages/telegram-cloud-storage-stamper) |

### Utilities

| Package                                   | NPM                                                                                                                       | Description                                                       | Changelog                                    |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------- |
| [`@turnkey/encoding`](/packages/encoding) | [![npm](https://img.shields.io/npm/v/@turnkey/encoding?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/encoding) | Encoding and decoding utilities, primarily for internal usage     | [CHANGELOG](/packages/encoding/CHANGELOG.md) |
| [`@turnkey/crypto`](/packages/crypto)     | [![npm](https://img.shields.io/npm/v/@turnkey/crypto?color=%234C48FF)](https://www.npmjs.com/package/@turnkey/crypto)     | Cryptographic utilities for P256 keys, encryption, and decryption | [CHANGELOG](/packages/crypto/CHANGELOG.md)   |

## Code Examples

### Instant examples (powered by Stackblitz)

The following code examples have been loaded into Stackblitz web environments so you can test them out immediately

| Example                                                                          | Description                                                                                                                             | Stackblitz Link                                                                      |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [`email-auth-local-storage`](/examples/authentication/email-auth-local-storage/) | A NextJS app demonstrating a complete email auth flow using a locally stored target embedded key                                        | [Test it out on Stackblitz!](https://stackblitz.com/edit/stackblitz-starters-pyyw59) |
| [`with-eth-passkeys-galore`](/examples/demos/with-eth-passkeys-galore/)          | A NextJS app powering users to create suborgs and sign messages via Viem or Ethers                                                      | [Test it out on Stackblitz!](https://stackblitz.com/edit/stackblitz-starters-2psu3g) |
| [`with-solana`](/examples/chain-integrations/with-solana/)                       | Create a new Solana address, then sign and broadcast a transaction on Solana's devnet                                                   | [Test it out on Stackblitz!](https://stackblitz.com/edit/stackblitz-starters-xeb93i) |
| [`with-solana-passkeys`](/examples/authentication/with-solana-passkeys/)         | A NextJS app powering users to create suborgs, sign messages, and create transactions sponsored by the parent org using @turnkey/solana | [Test it out on Stackblitz!](https://stackblitz.com/edit/stackblitz-starters-h5pmnu) |

### Other Code Examples

The below examples will require a local installation of `node.js`. Follow the specific instructions in the respective README's of each examples to run them!

| Example                                                                                            | Description                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`demo-consumer-wallet`](https://github.com/tkhq/demo-consumer-wallet)                             | A minimal consumer wallet app powered by Turnkey and WalletConnect                                                                                                                       |
| [`demo-passkey-wallet`](https://github.com/tkhq/demo-passkey-wallet)                               | A minimal consumer wallet app powered by Turnkey and passkeys                                                                                                                            |
| [`demo-ethers-passkeys`](https://github.com/tkhq/demo-ethers-passkeys)                             | A NextJS app that demonstrates how to use `@turnkey/ethers` to build a passkey-powered application                                                                                       |
| [`demo-viem-passkeys`](https://github.com/tkhq/demo-viem-passkeys)                                 | A NextJS app that demonstrates how to use `@turnkey/viem` to build a passkey-powered application                                                                                         |
| [`react-native-demo-wallet`](https://github.com/tkhq/react-native-demo-wallet)                     | A React Native app that demonstrates how to use the Turnkey's JavaScript packages in a mobile environment to authenticate users, create wallets, export wallets, sign messages, and more |
| [`flutter-demo-app`](https://github.com/tkhq/dart-sdk/tree/main/examples/flutter-demo-app)         | A Flutter app that demonstrates how to use the Turnkey's Flutter packages to authenticate users, create wallets, export wallets, sign messages, and more                                 |
| [`deployer`](/examples/advanced/deployer/)                                                         | Compile and deploy a smart contract                                                                                                                                                      |
| [`email-auth`](/examples/authentication/email-auth/)                                               | A NextJS app demonstrating a complete email auth flow using Turnkey iframes                                                                                                              |
| [`import-export-with-iframe-stamper`](/examples/key-management/import-export-with-iframe-stamper/) | A NextJS app demonstrating wallet import, export, and retrieval using iframes                                                                                                            |
| [`import-export-with-rwk`](/examples/key-management/import-export-with-rwk/)                       | A NextJS app demonstrating wallet and private key import and export using React Wallet Kit                                                                                               |
| [`wallet-export-sign`](/examples/key-management/wallet-export-sign/)                               | A NextJS app demonstrating wallet and wallet account export, and signing with the exported key                                                                                           |
| [`rebalancer`](/examples/transaction-management/rebalancer/)                                       | A demo application which showcases an example of how to use Turnkey for managing multiple types of keys & users                                                                          |
| [`solana-cctp-bridge`](/examples/transaction-management/solana-cctp-bridge/)                       | Bridge USDC from Solana to Base through Circle CCTP using three Turnkey-managed Solana signers (owner, MessageSent event account, rent payer)                                            |
| [`sweeper`](/examples/transaction-management/sweeper/)                                             | Sweep funds from one address to a different address                                                                                                                                      |
| [`trading-runner`](/examples/defi/trading-runner/)                                                 | A sample application demonstrating a trading operation, using various private keys, users, and policies, powered by Uniswap                                                              |
| [`with-ethers`](/examples/chain-integrations/with-ethers/)                                         | Create a new Ethereum address, then sign and broadcast a transaction using the Ethers signer with Infura                                                                                 |
| [`with-viem`](/examples/chain-integrations/with-viem/)                                             | Sign and broadcast a transaction using the Turnkey Custom Account and Infura                                                                                                             |
| [`with-cosmjs`](/examples/chain-integrations/with-cosmjs/)                                         | Create a new Cosmos address, then sign and broadcast a transaction on Celestia testnet using the CosmJS signer                                                                           |
| [`with-bitcoin`](/examples/chain-integrations/with-bitcoin/)                                       | Create a new wallet, derive a BTC address, create, sign, and broadcast a transaction using BitcoinJS and other external APIs                                                             |
| [`with-biconomy-aa`](/examples/account-abstraction/with-biconomy-aa/)                              | Create a new wallet, connect a Turnkey wallet client to Biconomy Nexus, and create, sign, and broadcast an EIP-1559 transaction                                                          |
| [`with-zerodev-aa`](/examples/account-abstraction/with-zerodev-aa/)                                | Create a new wallet, instantiate a Turnkey signer, create a ZeroDev kernel account and client, and broadcast a UserOp                                                                    |
| [`with-gnosis`](/examples/account-abstraction/with-gnosis/)                                        | Create new Ethereum addresses, configure a 3/3 Gnosis safe, and create + execute a transaction from it                                                                                   |
| [`with-uniswap`](/examples/defi/with-uniswap/)                                                     | Sign and broadcast a Uniswap v3 trade using the Ethers signer with Infura                                                                                                                |
| [`solana-usdc-swap`](/examples/defi/solana-usdc-swap/)                                             | Swap SOL to USDC through Jupiter using Turnkey Solana sponsorship with rent-safe token account handling                                                                                  |
| [`with-nonce-manager`](/examples/transaction-management/with-nonce-manager/)                       | Create a new Ethereum address, then sign and broadcast multiple transactions in a sequential or optimistic manner                                                                        |
| [`with-offline`](/examples/advanced/with-offline/)                                                 | Sign a Turnkey request in offline context                                                                                                                                                |
| [`with-federated-passkeys`](/examples/authentication/with-federated-passkeys/)                     | A NextJS app that demonstrates how to use Turnkey to build a federated, webauthn powered authentication flow                                                                             |
| [`with-eip-1193-provider`](/examples/chain-integrations/with-eip-1193-provider/)                   | A NextJS app that demonstrates how to use Turnkey the `@turnkey/eip-1193-provider` in your app                                                                                           |
| [`with-wallet-stamper`](/examples/authentication/with-wallet-stamper/)                             | A NextJS app that demonstrates how to use Turnkey the `@turnkey/wallet-stamper` in your app                                                                                              |

## Demos built with Turnkey

### Demo Consumer Wallet ([code](https://github.com/tkhq/demo-consumer-wallet))

A minimal consumer wallet app powered by Turnkey. Behind the scenes, it uses [`@turnkey/ethers`](https://www.npmjs.com/package/@turnkey/ethers) for signing and WalletConnect (v1) for accessing dapps.

https://github.com/tkhq/demo-consumer-wallet/assets/127255904/2c3409df-2d7c-4ec3-9aa8-e2944a0b0e0a

See https://github.com/tkhq/demo-consumer-wallet for the code.

### Demo Passkey Wallet ([code](https://github.com/tkhq/demo-passkey-wallet), [live link](https://wallet.tx.xyz))

A wallet application showing how users can register and authenticate using passkeys.
This demo uses the Turnkey API to create a new [Turnkey Sub-Organization](https://docs.turnkey.com/concepts/sub-organizations) for each user, create a testnet Ethereum address and send a transaction on Sepolia (ETH testnet).

<img src="./img/demo-passkey-wallet.png" alt="homepage screenshot" width="800px" />

See https://wallet.tx.xyz (and https://github.com/tkhq/demo-passkey-wallet for the code).

### Demo Ethers Passkeys ([code](https://github.com/tkhq/demo-ethers-passkeys))

A simple application demonstrating how to create sub-organizations, create private keys, and sign with the [`@turnkey/ethers`](https://github.com/tkhq/sdk/tree/main/packages/ethers) signer, using passkeys.

<img src="./img/ethers-ui-screenshot.png" alt="homepage screenshot" width="800px" />

See https://github.com/tkhq/demo-ethers-passkeys for the code.

### Demo Viem Passkeys ([code](https://github.com/tkhq/demo-viem-passkeys))

A similar, simple application demonstrating how to create sub-organizations, create private keys, and sign with the [`@turnkey/viem`](https://github.com/tkhq/sdk/tree/main/packages/viem) signer, using passkeys.

<img src="./img/viem-ui-screenshot.png" alt="homepage screenshot" width="800px" />

See https://github.com/tkhq/demo-viem-passkeys for the code.

### React Native Demo App ([code](https://github.com/tkhq/react-native-demo-wallet))

A React Native app that demonstrates how to use the Turnkey's JavaScript packages in a mobile environment to authenticate users, create wallets, export wallets, sign messages, and more

https://github.com/user-attachments/assets/e4cff012-11e9-4636-b67a-5dbf75355832

See https://github.com/tkhq/react-native-demo-wallet for the code.

### Flutter Demo App ([code](https://github.com/tkhq/dart-sdk/tree/main/examples/flutter-demo-app))

A Flutter app that demonstrates how to use the Turnkey's Flutter packages to authenticate users, create wallets, export wallets, sign messages, and more

https://github.com/user-attachments/assets/3d583ed8-1eff-4101-ae43-3c76c655e635

See https://github.com/tkhq/dart-sdk/tree/main/examples/flutter-demo-app for the code


---

## 73. toolkit
- **URL:** https://github.com/devtechedge/toolkit
- **Language:** TypeScript
- **Topics:** None
- **Description:** No description

### README.md

<br/>

<p align="center">
  <a href="https://across.to">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/across-protocol/toolkit/refs/heads/master/.github/across-logo-dark.png">
        <img alt="across logo" src="https://raw.githubusercontent.com/across-protocol/toolkit/refs/heads/master/.github/across-logo-light.png" width="auto" height="60">
      </picture>
</a>
</p>

<p align="center">
  Toolkit  🛠️ for building on top of the <a href="https://across.to">Across Protocol</a> 
<p>
<p align="center">
  Fastest and lowest-cost bridging for end-users. Streamlined interoperability for developers.
</p>

<p align="center">
  <a href="https://discord.across.to" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/Chat%20on-Discord-%235766f2" />
  </a>
  <a href="https://github.com/across-protocol/toolkit/blob/master/LICENSE">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/license-AGPL-21262d?style=flat">
      <img src="https://img.shields.io/badge/license-AGPL-f6f8fa?style=flat" alt="MIT License">
    </picture>
  </a>
  <a href="https://twitter.com/AcrossProtocol/" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/twitter/follow/AcrossProtocol?style=social"/>
  </a>
</p>

<br>

## Overview

Quickly integrate with a few lines of code. See [here](./packages/sdk/README.md) for more details.

```ts
import { createAcrossClient } from "@across-protocol/app-sdk";
import { mainnet, optimism, arbitrum } from "viem/chains";
import { useWalletClient } from "wagmi";

const wallet = useWalletClient();

// 1. Create client
const client = createAcrossClient({
  integratorId: "0xdead", // 2-byte hex string
  chains: [mainnet, optimism, arbitrum],
});

// 2. Retrieve quote for USDC from Arbitrum -> ETH on Optimism
const route = {
  originChainId: arbitrum.id,
  destinationChainId: optimism.id,
  inputToken: "0xaf88d065e77c8cC2239327C5EDb3A432268e5831", // USDC
  outputToken: "0x0000000000000000000000000000000000000000", // Native ETH
};
const swapQuote = await client.getSwapQuote({
  route,
  amount: parseUnit("10", 6), // USDC decimals
});

// 3. Execute quote
await client.executeSwapQuote({
  walletClient: wallet,
  swapQuote,
  onProgress: (progress) => {
    // handle progress
  },
});
```

## Tools

| Package                                                | Description                                                                                |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| [`@across-protocol/app-sdk`](./packages/sdk/README.md) | TypeScript package for building on top of Across Protocol's Smart Contracts and Quotes API |

## Examples

| App                                | Description                          |
| ---------------------------------- | ------------------------------------ |
| [using viem](./apps/example/app)   | Example Next.js app using [viem]()   |
| [using ethers](./apps/example/app) | Example Next.js app using [ethers]() |

## Links

- Website: <https://across.to>
- App: <https://app.across.to>
- Docs: <https://docs.across.to>
- X/Twitter: <https://x.com/AcrossProtocol>
- Medium: <https://medium.com/across-protocol>


---

## 74. jinja
- **URL:** https://github.com/devtechedge/jinja
- **Language:** Python
- **Topics:** None
- **Description:** A very fast and expressive template engine.

### README.md

<div align="center"><img src="https://raw.githubusercontent.com/pallets/jinja/refs/heads/stable/docs/_static/jinja-name.svg" alt="" height="150"></div>

# Jinja

Jinja is a fast, expressive, extensible templating engine. Special
placeholders in the template allow writing code similar to Python
syntax. Then the template is passed data to render the final document.

It includes:

-   Template inheritance and inclusion.
-   Define and import macros within templates.
-   HTML templates can use autoescaping to prevent XSS from untrusted
    user input.
-   A sandboxed environment can safely render untrusted templates.
-   AsyncIO support for generating templates and calling async
    functions.
-   I18N support with Babel.
-   Templates are compiled to optimized Python code just-in-time and
    cached, or can be compiled ahead-of-time.
-   Exceptions point to the correct line in templates to make debugging
    easier.
-   Extensible filters, tests, functions, and even syntax.

Jinja's philosophy is that while application logic belongs in Python if
possible, it shouldn't make the template designer's job difficult by
restricting functionality too much.


## In A Nutshell

```jinja
{% extends "base.html" %}
{% block title %}Members{% endblock %}
{% block content %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}
```

## Donate

The Pallets organization develops and supports Jinja and other popular
packages. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today][].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/


---

## 75. undici
- **URL:** https://github.com/devtechedge/undici
- **Language:** JavaScript
- **Topics:** None
- **Description:** An HTTP/1.1 client, written from scratch for Node.js

### README.md

# undici

[![Node CI](https://github.com/nodejs/undici/actions/workflows/ci.yml/badge.svg)](https://github.com/nodejs/undici/actions/workflows/nodejs.yml) [![neostandard javascript style](https://img.shields.io/badge/neo-standard-7fffff?style=flat\&labelColor=ff80ff)](https://github.com/neostandard/neostandard) [![npm version](https://badge.fury.io/js/undici.svg)](https://badge.fury.io/js/undici) [![codecov](https://codecov.io/gh/nodejs/undici/branch/main/graph/badge.svg?token=yZL6LtXkOA)](https://codecov.io/gh/nodejs/undici)

An HTTP/1.1 client, written from scratch for Node.js.

> Undici means eleven in Italian. 1.1 -> 11 -> Eleven -> Undici.
It is also a Stranger Things reference.

## How to get involved

Have a question about using Undici? Open a [Q&A Discussion](https://github.com/nodejs/undici/discussions/new) or join our official OpenJS [Slack](https://openjs-foundation.slack.com/archives/C01QF9Q31QD) channel.

Looking to contribute? Start by reading the [contributing guide](./CONTRIBUTING.md)

## Install

```
npm i undici
```

## Benchmarks

The benchmark is a simple getting data [example](https://github.com/nodejs/undici/blob/main/benchmarks/benchmark.js) using
50 TCP connections with a pipelining depth of 10 running on Node 24.14.1.

### HTTP/1.1

```
┌────────────────────────┬─────────┬────────────────────┬────────────┬─────────────────────────┐
│  Tests                 │ Samples │ Result             │ Tolerance  │ Difference with slowest │
├────────────────────────┼─────────┼────────────────────┼────────────┼─────────────────────────┤
│  'node-fetch'          │ 50      │ '4711.86 req/sec'  │ '± 2.92 %' │ '-'                     │
│  'undici - fetch'      │ 75      │ '5438.50 req/sec'  │ '± 2.97 %' │ '+ 15.42 %'             │
│  'axios'               │ 45      │ '5448.08 req/sec'  │ '± 2.98 %' │ '+ 15.62 %'             │
│  'request'             │ 65      │ '5809.63 req/sec'  │ '± 2.90 %' │ '+ 23.30 %'             │
│  'http - no keepalive' │ 35      │ '5910.77 req/sec'  │ '± 2.87 %' │ '+ 25.44 %'             │
│  'got'                 │ 50      │ '6047.80 req/sec'  │ '± 2.91 %' │ '+ 28.35 %'             │
│  'superagent'          │ 60      │ '7534.53 req/sec'  │ '± 2.97 %' │ '+ 59.91 %'             │
│  'http - keepalive'    │ 75      │ '9343.41 req/sec'  │ '± 2.90 %' │ '+ 98.30 %'             │
│  'undici - pipeline'   │ 65      │ '13470.70 req/sec' │ '± 2.93 %' │ '+ 185.89 %'            │
│  'undici - request'    │ 80      │ '16850.87 req/sec' │ '± 2.93 %' │ '+ 257.63 %'            │
│  'undici - stream'     │ 101     │ '18488.56 req/sec' │ '± 3.81 %' │ '+ 292.38 %'            │
│  'undici - dispatch'   │ 101     │ '20786.44 req/sec' │ '± 3.08 %' │ '+ 341.15 %'            │
└────────────────────────┴─────────┴────────────────────┴────────────┴─────────────────────────┘
```

### HTTP/1.1 over HTTPS

Using [benchmark-https.js](https://github.com/nodejs/undici/blob/main/benchmarks/benchmark-https.js) against an h1-over-TLS server (50 connections, pipelining depth 10, Node 24.14.1).

```
┌────────────────────────┬─────────┬───────────────────┬────────────┬─────────────────────────┐
│  Tests                 │ Samples │ Result            │ Tolerance  │ Difference with slowest │
├────────────────────────┼─────────┼───────────────────┼────────────┼─────────────────────────┤
│  'https - no keepalive'│ 10      │ '1358.40 req/sec' │ '± 1.99 %' │ '-'                     │
│  'undici - fetch'      │ 30      │ '3721.76 req/sec' │ '± 2.97 %' │ '+ 173.98 %'            │
│  'https - keepalive'   │ 35      │ '5633.91 req/sec' │ '± 2.84 %' │ '+ 314.75 %'            │
│  'undici - pipeline'   │ 15      │ '6254.05 req/sec' │ '± 2.80 %' │ '+ 360.40 %'            │
│  'undici - request'    │ 25      │ '6669.80 req/sec' │ '± 2.73 %' │ '+ 391.01 %'            │
│  'undici - stream'     │ 25      │ '7019.04 req/sec' │ '± 2.77 %' │ '+ 416.71 %'            │
│  'undici - dispatch'   │ 20      │ '7361.85 req/sec' │ '± 2.90 %' │ '+ 441.95 %'            │
└────────────────────────┴─────────┴───────────────────┴────────────┴─────────────────────────┘
```

### HTTP/2

Using [benchmark-http2.js](https://github.com/nodejs/undici/blob/main/benchmarks/benchmark-http2.js) against an h2 server (50 connections, pipelining depth 10, Node 24.14.1).

```
┌────────────────────────┬─────────┬───────────────────┬────────────┬─────────────────────────┐
│  Tests                 │ Samples │ Result            │ Tolerance  │ Difference with slowest │
├────────────────────────┼─────────┼───────────────────┼────────────┼─────────────────────────┤
│  'undici - fetch'      │ 45      │ '3499.03 req/sec' │ '± 2.93 %' │ '-'                     │
│  'native - http2'      │ 25      │ '4904.58 req/sec' │ '± 2.81 %' │ '+ 40.17 %'             │
│  'undici - pipeline'   │ 60      │ '5836.82 req/sec' │ '± 2.99 %' │ '+ 66.81 %'             │
│  'undici - request'    │ 65      │ '6831.25 req/sec' │ '± 2.83 %' │ '+ 95.23 %'             │
│  'undici - stream'     │ 55      │ '6874.30 req/sec' │ '± 2.91 %' │ '+ 96.46 %'             │
│  'undici - dispatch'   │ 55      │ '7791.23 req/sec' │ '± 2.96 %' │ '+ 122.67 %'            │
└────────────────────────┴─────────┴───────────────────┴────────────┴─────────────────────────┘
```

## Undici vs. Fetch

### Overview

Node.js includes a built-in `fetch()` implementation powered by undici starting from Node.js v18. However, there are important differences between using the built-in fetch and installing undici as a separate module.

### Built-in Fetch (Node.js v18+)

Node.js's built-in fetch is powered by a bundled version of undici:

```js
// Available globally in Node.js v18+
const response = await fetch('https://api.example.com/data');
const data = await response.json();

// Check the bundled undici version
console.log(process.versions.undici); // e.g., "5.28.4"
```

**Pros:**
- No additional dependencies required
- Works across different JavaScript runtimes
- Automatic compression handling (gzip, deflate, br)
- Built-in caching support (in development)

**Cons:**
- Limited to the undici version bundled with your Node.js version
- Less control over connection pooling and advanced features
- Error handling follows Web API standards (errors wrapped in `TypeError`)
- Performance overhead due to Web Streams implementation

### Undici Module

Installing undici as a separate module gives you access to the latest features and APIs:

```bash
npm install undici
```

```js
import { request, fetch, Agent, setGlobalDispatcher } from 'undici';

// Use undici.request for maximum performance
const { statusCode, headers, body } = await request('https://api.example.com/data');
const data = await body.json();

// Or use undici.fetch with custom configuration
const agent = new Agent({ keepAliveTimeout: 10000 });
setGlobalDispatcher(agent);
const response = await fetch('https://api.example.com/data');
```

**Pros:**
- Latest undici features and bug fixes
- Access to advanced APIs (`request`, `stream`, `pipeline`)
- Fine-grained control over connection pooling
- Better error handling with clearer error messages
- Superior performance, especially with `undici.request`
- HTTP/1.1 pipelining support
- Custom interceptors and middleware
- Advanced features like `ProxyAgent`, `Socks5Agent`, `MockAgent`

**Cons:**
- Additional dependency to manage
- Larger bundle size

### When to Use Each

#### Use Built-in Fetch When:
- You want zero dependencies
- Building isomorphic code that runs in browsers and Node.js
- Publishing to npm and want to maximize compatibility with JS runtimes
- Simple HTTP requests without advanced configuration
- You're publishing to npm and you want to maximize compatiblity
- You don't depend on features from a specific version of undici

#### Use Undici Module When:
- You need the latest undici features and performance improvements
- You require advanced connection pooling configuration
- You need APIs not available in the built-in fetch (`ProxyAgent`, `Socks5Agent`, `MockAgent`, etc.)
- Performance is critical (use `undici.request` for maximum speed)
- You want better error handling and debugging capabilities
- You need HTTP/1.1 pipelining or advanced interceptors
- You prefer decoupled protocol and API interfaces

### Performance Comparison

Based on benchmarks, here's the typical performance hierarchy:

1. **`undici.request()`** - Fastest, most efficient
2. **`undici.fetch()`** - Good performance, standard compliance
3. **Node.js `http`/`https`** - Baseline performance

### Migration Guide

If you're currently using built-in fetch and want to migrate to undici:

```js
// Before: Built-in fetch
const response = await fetch('https://api.example.com/data');

// After: Undici fetch (drop-in replacement)
import { fetch } from 'undici';
const response = await fetch('https://api.example.com/data');

// Or: Undici request (better performance)
import { request } from 'undici';
const { statusCode, body } = await request('https://api.example.com/data');
const data = await body.json();
```

### Keep `fetch` and `FormData` together

When you send a `FormData` body, keep `fetch` and `FormData` from the same
implementation.

Use one of these patterns:

```js
// Built-in globals
const body = new FormData()
body.set('name', 'some')
await fetch('https://example.com', {
  method: 'POST',
  body
})
```

```js
// undici module imports
import { fetch, FormData } from 'undici'

const body = new FormData()
body.set('name', 'some')
await fetch('https://example.com', {
  method: 'POST',
  body
})
```

If you want the installed `undici` package to provide the globals, call
`install()` first:

```js
import { install } from 'undici'

install()

const body = new FormData()
body.set('name', 'some')
await fetch('https://example.com', {
  method: 'POST',
  body
})
```

`install()` replaces the global `fetch`, `Headers`, `Response`, `Request`, and
`FormData` implementations with undici's versions, so they all match. It also
installs undici's `WebSocket`, `CloseEvent`, `ErrorEvent`, `MessageEvent`, and
`EventSource` globals.

Avoid mixing a global `FormData` with `undici.fetch()`, or `undici.FormData`
with the built-in global `fetch()`.

### Version Compatibility

You can check which version of undici is bundled with your Node.js version:

```js
console.log(process.versions.undici);
```

Installing undici as a module allows you to use a newer version than what's bundled with Node.js, giving you access to the latest features and performance improvements.

## Quick Start

### Basic Request

```js
import { request } from 'undici'

const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://localhost:3000/foo')

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) { console.log('data', data) }

console.log('trailers', trailers)
```

### Using Cache Interceptor

Undici provides a powerful HTTP caching interceptor that follows HTTP caching best practices. Here's how to use it:

```js
import { fetch, Agent, interceptors, cacheStores } from 'undici';

// Create a client with cache interceptor
const client = new Agent().compose(interceptors.cache({
  // Optional: Configure cache store (defaults to MemoryCacheStore)
  store: new cacheStores.MemoryCacheStore({
    maxSize: 100 * 1024 * 1024, // 100MB
    maxCount: 1000,
    maxEntrySize: 5 * 1024 * 1024 // 5MB
  }),
  
  // Optional: Specify which HTTP methods to cache (default: ['GET', 'HEAD'])
  methods: ['GET', 'HEAD']
}));

// Set the global dispatcher to use our caching client
setGlobalDispatcher(client);

// Now all fetch requests will use the cache
async function getData() {
  const response = await fetch('https://api.example.com/data');
  // The server should set appropriate Cache-Control headers in the response
  // which the cache will respect based on the cache policy
  return response.json();
}

// First request - fetches from origin
const data1 = await getData();

// Second request - served from cache if within max-age
const data2 = await getData();
```

#### Key Features:
- **Automatic Caching**: Respects `Cache-Control` and `Expires` headers
- **Validation**: Supports `ETag` and `Last-Modified` validation
- **Storage Options**: In-memory or persistent SQLite storage
- **Flexible**: Configure cache size, TTL, and more

## Global Installation

Undici provides an `install()` function to add fetch-related and other web API classes to `globalThis`, making them available globally:

```js
import { install } from 'undici'

// Install undici's global web APIs
install()

// Now you can use fetch classes globally without importing
const response = await fetch('https://api.example.com/data')
const data = await response.json()

// All classes are available globally:
const headers = new Headers([['content-type', 'application/json']])
const request = new Request('https://example.com')
const formData = new FormData()
const ws = new WebSocket('wss://example.com')
const eventSource = new EventSource('https://example.com/events')
```

The `install()` function adds the following classes to `globalThis`:

- `fetch` - The fetch function
- `Headers` - HTTP headers management
- `Response` - HTTP response representation
- `Request` - HTTP request representation
- `FormData` - Form data handling
- `WebSocket` - WebSocket client
- `CloseEvent`, `ErrorEvent`, `MessageEvent` - WebSocket events
- `EventSource` - Server-sent events client

When you call `install()`, these globals come from the same undici
implementation. For example, global `fetch` and global `FormData` will both be
undici's versions, and `WebSocket` and `EventSource` will also come from
undici, which is the recommended setup if you want to use undici through
globals.

This is useful for:
- Polyfilling environments that don't have fetch
- Ensuring consistent fetch behavior across different Node.js versions
- Making undici's implementations available globally for libraries that expect them

## Body Mixins

The `body` mixins are the most common way to format the request/response body. Mixins include:

- [`.arrayBuffer()`](https://fetch.spec.whatwg.org/#dom-body-arraybuffer)
- [`.blob()`](https://fetch.spec.whatwg.org/#dom-body-blob)
- [`.bytes()`](https://fetch.spec.whatwg.org/#dom-body-bytes)
- [`.json()`](https://fetch.spec.whatwg.org/#dom-body-json)
- [`.text()`](https://fetch.spec.whatwg.org/#dom-body-text)

> [!NOTE]
> The body returned from `undici.request` does not implement `.formData()`.

> [!WARNING]
> Calling `body.formData()` on a fetch response causes undici to buffer and parse the entire body. Since this is dictated by the spec, `body.formData()` must only be called on responses from trusted servers.

Example usage:

```js
import { request } from 'undici'

const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://localhost:3000/foo')

console.log('response received', statusCode)
console.log('headers', headers)
console.log('data', await body.json())
console.log('trailers', trailers)
```

_Note: Once a mixin has been called then the body cannot be reused, thus calling additional mixins on `.body`, e.g. `.body.json(); .body.text()` will result in an error `TypeError: unusable` being thrown and returned through the `Promise` rejection._

Should you need to access the `body` in plain-text after using a mixin, the best practice is to use the `.text()` mixin first and then manually parse the text to the desired format.

For more information about their behavior, please reference the body mixin from the [Fetch Standard](https://fetch.spec.whatwg.org/#body-mixin).

## Common API Methods

This section documents our most commonly used API methods. Additional APIs are documented in their own files within the [docs](./docs/) folder and are accessible via the navigation list on the left side of the docs site.

For the top-level APIs below, the `url` argument supplies the request origin and
path. Do not pass `origin` or `path` in the second `options` argument. The linked
`Dispatcher` option types include those fields because dispatcher methods are
lower-level APIs that do not receive a separate `url` argument.

### `undici.request([url, options]): Promise`

Arguments:

* **url** `string | URL | UrlObject`
* **options** [`RequestOptions`](./docs/docs/api/Dispatcher.md#parameter-requestoptions)
  * **dispatcher** `Dispatcher` - Default: [getGlobalDispatcher](#undicigetglobaldispatcher)
  * **method** `String` - Default: `PUT` if `options.body`, otherwise `GET`

Returns a promise with the result of the `Dispatcher.request` method.

Calls `options.dispatcher.request(options)`.

See [Dispatcher.request](./docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback) for more details, and [request examples](./docs/examples/README.md) for examples.

### `undici.stream([url, options, ]factory): Promise`

Arguments:

* **url** `string | URL | UrlObject`
* **options** [`StreamOptions`](./docs/docs/api/Dispatcher.md#parameter-streamoptions)
  * **dispatcher** `Dispatcher` - Default: [getGlobalDispatcher](#undicigetglobaldispatcher)
  * **method** `String` - Default: `PUT` if `options.body`, otherwise `GET`
* **factory** `Dispatcher.stream.factory`

Returns a promise with the result of the `Dispatcher.stream` method.

Calls `options.dispatcher.stream(options, factory)`.

See [Dispatcher.stream](./docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback) for more details.

### `undici.pipeline([url, options, ]handler): Duplex`

Arguments:

* **url** `string | URL | UrlObject`
* **options** [`PipelineOptions`](./docs/docs/api/Dispatcher.md#parameter-pipelineoptions)
  * **dispatcher** `Dispatcher` - Default: [getGlobalDispatcher](#undicigetglobaldispatcher)
  * **method** `String` - Default: `PUT` if `options.body`, otherwise `GET`
* **handler** `Dispatcher.pipeline.handler`

Returns: `stream.Duplex`

Calls `options.dispatch.pipeline(options, handler)`.

See [Dispatcher.pipeline](./docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler) for more details.

### `undici.connect([url, options]): Promise`

Starts two-way communications with the requested resource using [HTTP CONNECT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT).

Arguments:

* **url** `string | URL | UrlObject`
* **options** [`ConnectOptions`](./docs/docs/api/Dispatcher.md#parameter-connectoptions)
  * **dispatcher** `Dispatcher` - Default: [getGlobalDispatcher](#undicigetglobaldispatcher)
* **callback** `(err: Error | null, data: ConnectData | null) => void` (optional)

Returns a promise with the result of the `Dispatcher.connect` method.

Calls `options.dispatch.connect(options)`.

See [Dispatcher.connect](./docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback) for more details.

### `undici.fetch(input[, init]): Promise`

Implements [fetch](https://fetch.spec.whatwg.org/#fetch-method).

* https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch
* https://fetch.spec.whatwg.org/#fetch-method

Basic usage example:

```js
import { fetch } from 'undici'


const res = await fetch('https://example.com')
const json = await res.json()
console.log(json)
```

You can pass an optional dispatcher to `fetch` as:

```js
import { fetch, Agent } from 'undici'

const res = await fetch('https://example.com', {
  // Mocks are also supported
  dispatcher: new Agent({
    keepAliveTimeout: 10,
    keepAliveMaxTimeout: 10
  })
})
const json = await res.json()
console.log(json)
```

#### `request.body`

A body can be of the following types:

- ArrayBuffer
- ArrayBufferView
- AsyncIterables
- Blob
- Iterables
- String
- URLSearchParams
- FormData

In this implementation of fetch, ```request.body``` now accepts ```Async Iterables```. It is not present in the [Fetch Standard](https://fetch.spec.whatwg.org).

```js
import { fetch } from 'undici'

const data = {
  async *[Symbol.asyncIterator]() {
    yield 'hello'
    yield 'world'
  },
}

await fetch('https://example.com', { body: data, method: 'POST', duplex: 'half' })
```

[FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) besides text data and buffers can also utilize streams via [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) objects:

```js
import { openAsBlob } from 'node:fs'

const file = await openAsBlob('./big.csv')
const body = new FormData()
body.set('file', file, 'big.csv')

await fetch('http://example.com', { method: 'POST', body })
```

#### `request.duplex`

- `'half'`

In this implementation of fetch, `request.duplex` must be set if `request.body` is `ReadableStream` or `Async Iterables`, however, even though the value must be set to `'half'`, it is actually a _full_ duplex. For more detail refer to the [Fetch Standard](https://fetch.spec.whatwg.org/#dom-requestinit-duplex).

#### `response.body`

Nodejs has two kinds of streams: [web streams](https://nodejs.org/api/webstreams.html), which follow the API of the WHATWG web standard found in browsers, and an older Node-specific [streams API](https://nodejs.org/api/stream.html). `response.body` returns a readable web stream. If you would prefer to work with a Node stream you can convert a web stream using `.fromWeb()`.

```js
import { fetch } from 'undici'
import { Readable } from 'node:stream'

const response = await fetch('https://example.com')
const readableWebStream = response.body
const readableNodeStream = Readable.fromWeb(readableWebStream)
```

## Specification Compliance

This section documents parts of the [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9110.html) and [Fetch Standard](https://fetch.spec.whatwg.org) that Undici does
not support or does not fully implement.

#### CORS

Unlike browsers, Undici does not implement CORS (Cross-Origin Resource Sharing) checks by default. This means:

- No preflight requests are automatically sent for cross-origin requests
- No validation of `Access-Control-Allow-Origin` headers is performed
- Requests to any origin are allowed regardless of the source

This behavior is intentional for server-side environments where CORS restrictions are typically unnecessary. If your application requires CORS-like protections, you will need to implement these checks manually.

#### Garbage Collection

* https://fetch.spec.whatwg.org/#garbage-collection

The [Fetch Standard](https://fetch.spec.whatwg.org) allows users to skip consuming the response body by relying on
[garbage collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management#garbage_collection) to release connection resources.

Garbage collection in Node is less aggressive and deterministic
(due to the lack of clear idle periods that browsers have through the rendering refresh rate)
which means that leaving the release of connection resources to the garbage collector can lead
to excessive connection usage, reduced performance (due to less connection re-use), and even
stalls or deadlocks when running out of connections.
Therefore, __it is important to always either consume or cancel the response body anyway__.

```js
// Do
const { body, headers } = await fetch(url);
for await (const chunk of body) {
  // force consumption of body
}

// Do not
const { headers } = await fetch(url);
```

However, if you want to get only headers, it might be better to use `HEAD` request method. Usage of this method will obviate the need for consumption or cancelling of the response body. See [MDN - HTTP - HTTP request methods - HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) for more details.

```js
const headers = await fetch(url, { method: 'HEAD' })
  .then(res => res.headers)
```

Note that consuming the response body is _mandatory_ for `request`:

```js
// Do
const { body, headers } = await request(url);
await body.dump(); // force consumption of body

// Do not
const { headers } = await request(url);
```

#### Forbidden and Safelisted Header Names

* https://fetch.spec.whatwg.org/#cors-safelisted-response-header-name
* https://fetch.spec.whatwg.org/#forbidden-header-name
* https://fetch.spec.whatwg.org/#forbidden-response-header-name
* https://github.com/wintercg/fetch/issues/6

The [Fetch Standard](https://fetch.spec.whatwg.org) requires implementations to exclude certain headers from requests and responses. In browser environments, some headers are forbidden so the user agent remains in full control over them. In Undici, these constraints are removed to give more control to the user.

#### Content-Encoding

* https://www.rfc-editor.org/rfc/rfc9110#field.content-encoding

Undici limits the number of `Content-Encoding` layers in a response to **5** to prevent resource exhaustion attacks. If a server responds with more than 5 content-encodings (e.g., `Content-Encoding: gzip, gzip, gzip, gzip, gzip, gzip`), the fetch will be rejected with an error. This limit matches the approach taken by [curl](https://curl.se/docs/CVE-2022-32206.html) and [urllib3](https://github.com/advisories/GHSA-gm62-xv2j-4rw9).

#### `undici.upgrade([url, options]): Promise`

Upgrade to a different protocol. See [MDN - HTTP - Protocol upgrade mechanism](https://developer.mozilla.org/en-US/docs/Web/HTTP/Protocol_upgrade_mechanism) for more details.

Arguments:

* **url** `string | URL | UrlObject`
* **options** [`UpgradeOptions`](./docs/docs/api/Dispatcher.md#parameter-upgradeoptions)
  * **dispatcher** `Dispatcher` - Default: [getGlobalDispatcher](#undicigetglobaldispatcher)
* **callback** `(error: Error | null, data: UpgradeData) => void` (optional)

Returns a promise with the result of the `Dispatcher.upgrade` method.

Calls `options.dispatcher.upgrade(options)`.

See [Dispatcher.upgrade](./docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback) for more details.

### `undici.setGlobalDispatcher(dispatcher)`

* dispatcher `Dispatcher`

Sets the global dispatcher used by Common API Methods. Global dispatcher is shared among compatible undici modules,
including undici that is bundled internally with node.js.

Undici stores this dispatcher under `Symbol.for('undici.globalDispatcher.2')`.

`setGlobalDispatcher()` also mirrors the configured dispatcher to
`Symbol.for('undici.globalDispatcher.1')` using `Dispatcher1Wrapper`, so Node.js built-in `fetch`
can keep using the legacy handler contract while Undici uses the new handler API.

### `undici.getGlobalDispatcher()`

Gets the global dispatcher used by Common API Methods.

Returns: `Dispatcher`

### `undici.setGlobalOrigin(origin)`

* origin `string | URL | undefined`

Sets the global origin used in `fetch`.

If `undefined` is passed, the global origin will be reset. This will cause `Response.redirect`, `new Request()`, and `fetch` to throw an error when a relative path is passed.

```js
setGlobalOrigin('http://localhost:3000')

const response = await fetch('/api/ping')

console.log(response.url) // http://localhost:3000/api/ping
```

### `undici.getGlobalOrigin()`

Gets the global origin used in `fetch`.

Returns: `URL`

### `UrlObject`

* **port** `string | number` (optional)
* **path** `string` (optional)
* **pathname** `string` (optional)
* **hostname** `string` (optional)
* **origin** `string` (optional)
* **protocol** `string` (optional)
* **search** `string` (optional)

#### Expect

Undici does not support the `Expect` request header field. The request
body is  always immediately sent and the `100 Continue` response will be
ignored.

Refs: https://tools.ietf.org/html/rfc7231#section-5.1.1

#### Pipelining

Undici will only use pipelining if configured with a `pipelining` factor
greater than `1`. Only enable pipelining when the remote server is trusted.
Also it is important to pass `blocking: false` to the request options to
properly pipeline requests.

Undici always assumes that connections are persistent and will immediately
pipeline requests, without checking whether the connection is persistent.
Hence, automatic fallback to HTTP/1.0 or HTTP/1.1 without pipelining is
not supported.

Undici will immediately pipeline when retrying requests after a failed
connection. However, Undici will not retry the first remaining requests in
the prior pipeline and instead error the corresponding callback/promise/stream.

Undici will abort all running requests in the pipeline when any of them are
aborted.

* Refs: https://tools.ietf.org/html/rfc2616#section-8.1.2.2
* Refs: https://tools.ietf.org/html/rfc7230#section-6.3.2

#### Manual Redirect

Since it is not possible to manually follow an HTTP redirect on the server-side,
Undici returns the actual response instead of an `opaqueredirect` filtered one
when invoked with a `manual` redirect. This aligns `fetch()` with the other
implementations in Deno and Cloudflare Workers.

Refs: https://fetch.spec.whatwg.org/#atomic-http-redirect-handling

### Workarounds

#### Network address family autoselection.

If you experience problem when connecting to a remote server that is resolved by your DNS servers to a IPv6 (AAAA record)
first, there are chances that your local router or ISP might have problem connecting to IPv6 networks. In that case
undici will throw an error with code `UND_ERR_CONNECT_TIMEOUT`.

If the target server resolves to both a IPv6 and IPv4 (A records) address and you are using a compatible Node version
(18.3.0 and above), you can fix the problem by providing the `autoSelectFamily` option (support by both `undici.request`
and `undici.Agent`) which will enable the family autoselection algorithm when establishing the connection.

## Collaborators

* [__Daniele Belardi__](https://github.com/dnlup), <https://www.npmjs.com/~dnlup>
* [__Ethan Arrowood__](https://github.com/ethan-arrowood), <https://www.npmjs.com/~ethan_arrowood>
* [__Matteo Collina__](https://github.com/mcollina), <https://www.npmjs.com/~matteo.collina>
* [__Matthew Aitken__](https://github.com/KhafraDev), <https://www.npmjs.com/~khaf>
* [__Robert Nagy__](https://github.com/ronag), <https://www.npmjs.com/~ronag>
* [__Szymon Marczak__](https://github.com/szmarczak), <https://www.npmjs.com/~szmarczak>

## Past Collaborators
* [__Tomas Della Vedova__](https://github.com/delvedor), <https://www.npmjs.com/~delvedor>

### Releasers

* [__Ethan Arrowood__](https://github.com/ethan-arrowood), <https://www.npmjs.com/~ethan_arrowood>
* [__Matteo Collina__](https://github.com/mcollina), <https://www.npmjs.com/~matteo.collina>
* [__Robert Nagy__](https://github.com/ronag), <https://www.npmjs.com/~ronag>
* [__Matthew Aitken__](https://github.com/KhafraDev), <https://www.npmjs.com/~khaf>

## Long Term Support

Undici aligns with the Node.js LTS schedule. The following table shows the supported versions:

| Undici Version | Bundled in Node.js | Node.js Versions Supported | End of Life |
|----------------|--------------------|----------------------------|-------------|
| 5.x            | 18.x               | ≥14.0 (tested: 14, 16, 18) | 2024-04-30  |
| 6.x            | 20.x, 22.x         | ≥18.17 (tested: 18, 20, 21, 22) | 2027-04-30  |
| 7.x            | 24.x               | ≥20.18.1 (tested: 20, 22, 24) | 2028-04-30  |
| 8.x            | 26.x               | ≥22.19.0 (tested: 22, 24, 26) | 2029-04-30  |

## License

MIT


---

## 76. typescript-eslint
- **URL:** https://github.com/devtechedge/typescript-eslint
- **Language:** TypeScript
- **Topics:** None
- **Description:** :sparkles: Monorepo for all the tooling which enables ESLint to support TypeScript

### README.md

<h1 align="center">typescript-eslint</h1>

<p align="center">Monorepo for typescript-eslint: powerful static analysis for JavaScript and TypeScript</p>

<p align="center">
    <img src="https://github.com/typescript-eslint/typescript-eslint/workflows/CI/badge.svg" alt="CI" />
    <a href="https://opencollective.com/typescript-eslint"><img src="https://opencollective.com/typescript-eslint/all/badge.svg?label=financial+contributors&style=flat-square" alt="Financial Contributors on Open Collective" /></a>
    <a href="https://www.npmjs.com/package/@typescript-eslint/typescript-estree"><img src="https://img.shields.io/npm/dm/@typescript-eslint/typescript-estree.svg?style=flat-square" alt="NPM Downloads" /></a>
    <a href="https://codecov.io/gh/typescript-eslint/typescript-eslint"><img alt="Codecov" src="https://img.shields.io/codecov/c/github/typescript-eslint/typescript-eslint.svg?style=flat-square"></a>
</p>

<!-- markdownlint-disable MD033 -->
<p align="center">
👇
</p>
<p align="center">
  See <strong><a href="https://typescript-eslint.io">typescript-eslint.io</a></strong> for documentation on the latest released version.
</p>
<p align="center">
<small>
  See <strong><a href="https://main--typescript-eslint.netlify.app">main--typescript-eslint.netlify.app</a></strong> for documentation on the latest <a href="https://main--typescript-eslint.netlify.app/users/versioning">canary release</a>.
</small>
</p>
<p align="center">
👆
</p>
<!-- markdownlint-enable MD033 -->

## Code Contributors

This project exists thanks to the awesome people who contribute code and documentation:

<a href="https://github.com/typescript-eslint/typescript-eslint/graphs/contributors"><img alt="Gallery of all contributors' profile photos" src="https://opencollective.com/typescript-eslint/contributors.svg?width=890&button=false" /></a>

🙏 An extra special thanks goes out to the wonderful people listed in <https://github.com/typescript-eslint/typescript-eslint/graphs/contributors>.

## Financial Contributors

In addition to submitting code and documentation updates, you can help us sustain our community by becoming a financial contributor [[Click here to contribute - every little bit helps!](https://opencollective.com/typescript-eslint/contribute)]

<a href="https://www.netlify.com">
  <img src="https://www.netlify.com/img/global/badges/netlify-light.svg" alt="Deploys by Netlify" />
</a>

## License

typescript-eslint inherits is licensed under a permissive MIT license.


---

## 77. starlette
- **URL:** https://github.com/devtechedge/starlette
- **Language:** Python
- **Topics:** None
- **Description:** The little ASGI framework that shines. ≡ƒîƒ

### README.md

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette_dark.svg" width="420px">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg" width="420px">
    <img alt="starlette-logo" src="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg">
  </picture>
</p>

<p align="center">
    <em>✨ The little ASGI framework that shines. ✨</em>
</p>

---

[![Build Status](https://github.com/Kludex/starlette/workflows/Test%20Suite/badge.svg)](https://github.com/Kludex/starlette/actions)
[![Package version](https://badge.fury.io/py/starlette.svg)](https://pypi.python.org/pypi/starlette)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/starlette.svg?color=%2334D058)](https://pypi.org/project/starlette)
[![Discord](https://img.shields.io/discord/1051468649518616576?logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/RxKUF5JuHs)

---

**Documentation**: <a href="https://starlette.dev/" target="_blank">https://starlette.dev</a>

**Source Code**: <a href="https://github.com/Kludex/starlette" target="_blank">https://github.com/Kludex/starlette</a>

---

# Starlette

Starlette is a lightweight [ASGI][asgi] framework/toolkit,
which is ideal for building async web services in Python.

It is production-ready, and gives you the following:

* A lightweight, low-complexity HTTP web framework.
* WebSocket support.
* In-process background tasks.
* Startup and shutdown events.
* Test client built on `httpx2`.
* CORS, GZip, Static Files, Streaming responses.
* Session and Cookie support.
* 100% test coverage.
* 100% type annotated codebase.
* Few hard dependencies.
* Compatible with `asyncio` and `trio` backends.
* Great overall performance [against independent benchmarks][techempower].

## Installation

```shell
$ pip install starlette
```

You'll also want to install an ASGI server, such as [uvicorn](https://uvicorn.dev) or any of the [other ASGI server implementations](https://asgi.readthedocs.io/en/latest/implementations.html#servers).

```shell
$ pip install uvicorn
```

## Example

```python title="main.py"
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(debug=True, routes=routes)
```

Then run the application using Uvicorn:

```shell
$ uvicorn main:app
```

## Dependencies

Starlette only requires `anyio`, and the following are optional:

* [`httpx2`][httpx2] - Required if you want to use the `TestClient`.
* [`jinja2`][jinja2] - Required if you want to use `Jinja2Templates`.
* [`opentelemetry-api`][opentelemetry-api] - Required for `OpenTelemetryMiddleware`.
* [`python-multipart`][python-multipart] - Required if you want to support form parsing, with `request.form()`.
* [`itsdangerous`][itsdangerous] - Required for `SessionMiddleware` support.
* [`pyyaml`][pyyaml] - Required for `SchemaGenerator` support.

You can install all of these with `pip install starlette[full]`.

## Framework or Toolkit

Starlette is designed to be used either as a complete framework, or as
an ASGI toolkit. You can use any of its components independently.

```python
from starlette.responses import PlainTextResponse


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)
```

Run the `app` application in `example.py`:

```shell
$ uvicorn example:app
INFO: Started server process [11509]
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Run uvicorn with `--reload` to enable auto-reloading on code changes.

## Modularity

The modularity that Starlette is designed on promotes building reusable
components that can be shared between any ASGI framework. This should enable
an ecosystem of shared middleware and mountable applications.

The clean API separation also means it's easier to understand each component
in isolation.

---

<p align="center"><i>Starlette is <a href="https://github.com/Kludex/starlette/blob/main/LICENSE.md">BSD licensed</a> code.<br/>Designed & crafted with care.</i></br>&mdash; ⭐️ &mdash;</p>

[asgi]: https://asgi.readthedocs.io/en/latest/
[httpx2]: https://pypi.org/project/httpx2/
[jinja2]: https://jinja.palletsprojects.com/
[opentelemetry-api]: https://opentelemetry.io/docs/languages/python/api/
[python-multipart]: https://multipart.fastapiexpert.com/
[itsdangerous]: https://itsdangerous.palletsprojects.com/
[sqlalchemy]: https://www.sqlalchemy.org
[pyyaml]: https://pyyaml.org/wiki/PyYAMLDocumentation
[techempower]: https://github.com/TechEmpower/FrameworkBenchmarks


---

## 78. coinbase-wallet-sdk
- **URL:** https://github.com/devtechedge/coinbase-wallet-sdk
- **Language:** TypeScript
- **Topics:** None
- **Description:** An open protocol that lets users connect their mobile wallets to your DApp

### README.md

# Coinbase Wallet SDK

[![npm](https://img.shields.io/npm/v/@coinbase/wallet-sdk.svg)](https://www.npmjs.com/package/@coinbase/wallet-sdk)

## Coinbase Wallet SDK allows dapps to connect to Coinbase Wallet

1. [Coinbase Smart Wallet](https://keys.coinbase.com/onboarding)
   - [Docs](https://www.smartwallet.dev/)
1. Coinbase Wallet mobile for [Android](https://play.google.com/store/apps/details?id=org.toshi&referrer=utm_source%3DWallet_LP) and [iOS](https://apps.apple.com/app/apple-store/id1278383455?pt=118788940&ct=Wallet_LP&mt=8)
   - Desktop: Users can connect to your dapp by scanning a QR code
   - Mobile: Users can connect to your mobile dapp through a deeplink to the dapp browser
1. Coinbase Wallet extension for [Chrome](https://chrome.google.com/webstore/detail/coinbase-wallet-extension/hnfanknocfeofbddgcijnmhnfnkdnaad?hl=en) and [Brave](https://chromewebstore.google.com/detail/coinbase-wallet-extension/hnfanknocfeofbddgcijnmhnfnkdnaad?hl=en)
   - Desktop: Users can connect by clicking the connect with an extension option.

### Installing Wallet SDK

1. Check available versions:

   ```shell
     # yarn
     yarn info @coinbase/wallet-sdk versions

     # npm
     npm view @coinbase/wallet-sdk versions
   ```

2. Install latest version:

   ```shell
   # yarn
   yarn add @coinbase/wallet-sdk

   # npm
   npm install @coinbase/wallet-sdk
   ```

3. Check installed version:

   ```shell
   # yarn
   yarn list @coinbase/wallet-sdk

   # npm
   npm list @coinbase/wallet-sdk
   ```

### Upgrading Wallet SDK

> Migrating from v3 to v4? Please see our [v4 migration guide](https://www.smartwallet.dev/sdk/v3-to-v4-changes) for a full list of breaking changes.

1. Compare the installed version with the latest:

   ```shell
   # yarn
   yarn outdated @coinbase/wallet-sdk

   # npm
   npm outdated @coinbase/wallet-sdk
   ```

2. Update to latest:

   ```shell
   # yarn
   yarn upgrade @coinbase/wallet-sdk --latest

   # npm
   npm update @coinbase/wallet-sdk
   ```

### Basic Usage

1. Initialize SDK

   ```js
   const sdk = new CoinbaseWalletSDK({
     appName: 'SDK Playground',
   });
   ```

2. Make web3 Provider

   ```js
   const provider = sdk.makeWeb3Provider();
   ```

3. Request accounts to initialize a connection to wallet

   ```js
   const addresses = provider.request({
     method: 'eth_requestAccounts',
   });
   ```

4. Make more requests

   ```js
   provider.request('personal_sign', [
     `0x${Buffer.from('test message', 'utf8').toString('hex')}`,
     addresses[0],
   ]);
   ```

5. Handle provider events

   ```js
   provider.on('connect', (info) => {
     setConnect(info);
   });

   provider.on('disconnect', (error) => {
     setDisconnect({ code: error.code, message: error.message });
   });

   provider.on('accountsChanged', (accounts) => {
     setAccountsChanged(accounts);
   });

   provider.on('chainChanged', (chainId) => {
     setChainChanged(chainId);
   });

   provider.on('message', (message) => {
     setMessage(message);
   });
   ```

### Developing locally and running the test dapp

- The Coinbase Wallet SDK test dapp can be viewed here https://coinbase.github.io/coinbase-wallet-sdk/.
- To run it locally follow these steps:

  1. Fork this repo and clone it
  1. From the root dir run `yarn install`
  1. From the root dir run `yarn dev`


---

## 79. router
- **URL:** https://github.com/devtechedge/router
- **Language:** TypeScript
- **Topics:** None
- **Description:** ≡ƒñû A client-first, server-capable, fully type-safe router and full-stack framework for the web (React and more).

### README.md

<img src="https://static.scarf.sh/a.png?x-pxid=d988eb79-b0fc-4a2b-8514-6a1ab932d188" />

<table>
<tr>
<td>

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://tanstack.com/api/readme/router.png?theme=dark"
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://tanstack.com/api/readme/router.png"
  />
  <img
    src="https://tanstack.com/api/readme/router.png"
    alt="TanStack Router"
  />
</picture>

## TanStack Router

A modern router designed for type safety, data‑driven navigation, and seamless developer experience.

- End‑to-end type safety (routes, params, loaders)
- Schema‑driven search params with validation
- Built‑in caching, prefetching & invalidation
- Nested layouts, transitions & error boundaries

### [Read the Router Docs →](https://tanstack.com/router)

</td>
<td>

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://tanstack.com/api/readme/start.png?theme=dark"
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://tanstack.com/api/readme/start.png"
  />
  <img
    src="https://tanstack.com/api/readme/start.png"
    alt="TanStack Start"
  />
</picture>

## TanStack Start

A full‑stack framework built on Router, designed for server rendering, streaming, and production‑ready deployments.

- Full‑document SSR & streaming
- Server functions & end‑to‑end type safety
- Deployment‑ready bundling & builds
- All the power of TanStack Router, plus full‑stack features

### [Read the Start Docs →](https://tanstack.com/start)

</td>
</tr>
</table>

<br />

<p align="center">
  <a href="https://npmjs.com/package/@tanstack/react-router"><img src="https://img.shields.io/npm/dm/@tanstack/react-router.svg" alt="npm downloads" /></a> <a href="https://github.com/tanstack/router"><img src="https://img.shields.io/github/stars/tanstack/router.svg?style=social&label=Star" alt="GitHub stars" /></a> <a href="https://bundlephobia.com/result?p=@tanstack/react-router"><img src="https://badgen.net/bundlephobia/minzip/@tanstack/react-router" alt="Bundle size" /></a>
</p>
<p align="center">
  <a href="#badge"><img alt="semantic-release" src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg"></a> <a href="https://bestofjs.org/projects/tanstack-router"><img alt="Best of JS" src="https://img.shields.io/endpoint?url=https://bestofjs-serverless.now.sh/api/project-badge?fullName=TanStack%2Frouter%26since=daily" /></a> <a href="https://twitter.com/tan_stack"><img src="https://img.shields.io/twitter/follow/tan_stack.svg?style=social" alt="Follow @TanStack"/></a>
</p>

<div align="center">

### [Become a Sponsor!](https://github.com/sponsors/tannerlinsley/)

</div>

## Get Involved

- We welcome issues and pull requests!
- Participate in [GitHub discussions](https://github.com/TanStack/router/discussions)
- Chat with the community on [Discord](https://discord.com/invite/WrRKjPJ)
- See [CONTRIBUTING.md](./CONTRIBUTING.md) for setup instructions

## Partners

<table align="center">
  <tr>
        <td>
      <a href="https://www.coderabbit.ai/?via=tanstack&dub_id=aCcEEdAOqqutX6OS" >
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/coderabbit-dark-D643Zkrv.svg" />
          <source media="(prefers-color-scheme: light)" srcset="https://tanstack.com/assets/coderabbit-light-CIzGLYU_.svg" />
          <img src="https://tanstack.com/assets/coderabbit-light-CIzGLYU_.svg" height="40" alt="CodeRabbit" />
        </picture>
      </a>
    </td>
    <td>
      <a href="https://www.cloudflare.com?utm_source=tanstack">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/cloudflare-white-Co-Tyjbl.svg" />
          <source media="(prefers-color-scheme: light)" srcset="https://tanstack.com/assets/cloudflare-black-6Ojsn8yh.svg" />
          <img src="https://tanstack.com/assets/cloudflare-white-Co-Tyjbl.svg" height="60" alt="Cloudflare" />
        </picture>
      </a>
    </td>
    <td>
      <a href="https://netlify.com?utm_source=tanstack">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tanstack/tanstack.com/main/src/images/netlify-dark.svg" height="70"/>
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/netlify.svg" height="70"/>
        <img src="https://raw.githubusercontent.com/tanstack/tanstack.com/main/src/images/netlify-dark.svg" height="70" alt="Netlify" />
      </picture>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://neon.tech?utm_source=tanstack">
		  <picture>
	        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tanstack/tanstack.com/main/src/images/neon-dark.svg" height="50"/>
	        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/neon.svg" height="50"/>
	        <img src="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/neon.svg" height="50" alt="Neon" />
		  </picture>
	  </a>
    </td>
    <td>
      <a href="https://go.clerk.com/wOwHtuJ">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/clerk-logo-dark-CRE22T_2.svg" height="40"/>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/clerk.svg" height="40"/>
          <img src="https://tanstack.com/assets/clerk-logo-dark-CRE22T_2.svg" height="40" alt="Clerk" />
        </picture>
      </a>
    </td>
    <td>
      <a href="https://convex.dev?utm_source=tanstack">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tanstack/tanstack.com/main/src/images/convex-white.svg" height="30"/>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/convex.svg" height="30"/>
          <img src="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/convex.svg" height="30" alt="Convex" />
        </picture>
      </a>
    </td>
  </tr>
    <tr>
    <td>
      <a href="https://sentry.io?utm_source=tanstack">
        <picture>
           <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tanstack/tanstack.com/main/src/images/sentry-wordmark-light.svg" height="50"/>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/sentry.svg" height="50"/>
          <img src="https://raw.githubusercontent.com/tannerlinsley/files/master/partners/sentry.svg" height="50" alt="Sentry" />
        </picture>
      </a>
    </td>
    <td>
      <a href="https://www.prisma.io?utm_source=tanstack&via=tanstack">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/prisma-dark-DwgDxLwn.svg" height="50"/>
          <source media="(prefers-color-scheme: light)" srcset="https://tanstack.com/assets/prisma-light-Cloa3Onm.svg" height="50"/>
          <img src="https://tanstack.com/assets/prisma-dark-DwgDxLwn.svg" height="50" alt="Prisma" />
        </picture>
      </a>
    </td>
    <td>
      <a href="https://strapi.link/tanstack-start">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/strapi-dark-CQ84tQTk.svg" height="40"/>
          <source media="(prefers-color-scheme: light)" srcset="https://tanstack.com/assets/strapi-light-6x7linao.svg" height="40"/>
          <img src="https://tanstack.com/assets/strapi-dark-CQ84tQTk.svg" height="40" alt="Strapi" />
        </picture>
      </a>
    </td>
  </tr>
</table>

<div align="center">
<img src="./media/partner_logo.svg" alt="Router & you?" height="65">
<p>
We're looking for TanStack Router & Start Partners to join our mission! Partner with us to push the boundaries of TanStack Router & Start and build amazing things together.
</p>
<a href="mailto:partners@tanstack.com?subject=TanStack Router & Start Partnership"><b>LET'S CHAT</b></a>
</div>

## Explore the TanStack Ecosystem

- <a href="https://github.com/tanstack/config"><b>TanStack Config</b></a> – Tooling for JS/TS packages
- <a href="https://github.com/tanstack/db"><b>TanStack DB</b></a> – Reactive sync client store
- <a href="https://github.com/tanstack/devtools"><b>TanStack DevTools</b></a> – Unified devtools panel
- <a href="https://github.com/tanstack/form"><b>TanStack Form</b></a> – Type‑safe form state
- <a href="https://github.com/tanstack/pacer"><b>TanStack Pacer</b></a> – Debouncing, throttling, batching <br/>
- <a href="https://github.com/tanstack/query"><b>TanStack Query</b></a> – Async state & caching
- <a href="https://github.com/tanstack/ranger"><b>TanStack Ranger</b></a> – Range & slider primitives
- <a href="https://github.com/tanstack/store"><b>TanStack Store</b></a> – Reactive data store
- <a href="https://github.com/tanstack/table"><b>TanStack Table</b></a> – Headless datagrids
- <a href="https://github.com/tanstack/virtual"><b>TanStack Virtual</b></a> – Virtualized rendering

… and more at <a href="https://tanstack.com"><b>TanStack.com »</b></a>

<!-- Use the force, Luke!!! -->


---

## 80. miniapps
- **URL:** https://github.com/devtechedge/miniapps
- **Language:** TypeScript
- **Topics:** None
- **Description:** No description

### README.md

<br />

<p align="center">
  <a href="https://miniapps.farcaster.xyz">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/farcasterxyz/miniapps/main/.github/gh-logo-dark.svg">
        <img alt="farcaster mini apps logo" src="https://raw.githubusercontent.com/farcasterxyz/miniapps/main/.github/gh-logo-light.svg" width="auto" height="30">
      </picture>
  </a>
</p>

<p align="center">
  Build onchain social apps
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@farcaster/frame-sdk">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/v/@farcaster/frame-sdk?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/npm/v/@farcaster/frame-sdk?colorA=f6f8fa&colorB=f6f8fa" alt="Version">
    </picture>
  </a>
  <a href="https://github.com/farcasterxyz/miniapps/blob/main/LICENSE">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/l/@farcaster/frame-sdk?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/npm/l/@farcaster/frame-sdk?colorA=f6f8fa&colorB=f6f8fa" alt="MIT License">
    </picture>
  </a>
  <a href="https://www.npmjs.com/package/@farcaster/frame-sdk">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/dm/@farcaster/frame-sdk?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/npm/dm/@farcaster/frame-sdk?colorA=f6f8fa&colorB=f6f8fa" alt="Downloads per month">
    </picture>
  </a>
</p>

---

## Documentation

For documentation and guides, visit [miniapps.farcaster.xyz](https://miniapps.farcaster.xyz).

## Community

For fast, casual conversations:

[Join the Mini Apps Developer Chat on Warpcast](https://farcaster.xyz/~/group/X2P7HNc4PHTriCssYHNcmQ)

For slow, formal conversations that would benefit from being searchable:

[Discuss Mini Apps on GitHub](https://github.com/farcasterxyz/miniapps/discussions)

## Contributing

Contributions are greatly appreciated! If you're interested in contributing to the Mini Apps monorepo, please read the [Contributing Guide](https://github.com/farcasterxyz/miniapps/blob/main/.github/CONTRIBUTING.md) **before submitting a pull request**.



---

## 81. alchemy-sdk-js
- **URL:** https://github.com/devtechedge/alchemy-sdk-js
- **Language:** TypeScript
- **Topics:** None
- **Description:** The easiest way to connect your dApp to the blockchain.

### README.md

> [!WARNING]
> The Alchemy SDK JS has been deprecated and will be archived **January 2026**. The software will only receive minimal support until then. New and existing users are encourage to use the following tools instead:
> - [Alchemy Smart Wallets SDK](https://github.com/alchemyplatform/aa-sdk) for transacting applications (includes support for the [Portfolio Data APIs](https://www.alchemy.com/docs/reference/portfolio-apis)).
> - [Viem](https://github.com/wevm/viem/) for JS based Ethereum development.
> - [Solana Web3JS](https://www.npmjs.com/package/@solana/web3.js) for JS based Solana development.

# Alchemy SDK for Javascript

The Alchemy SDK is the most comprehensive, stable, and powerful Javascript SDK available today to interact with the blockchain.

It supports the exact same syntax and functionality of the Ethers.js `AlchemyProvider` and `WebSocketProvider`, making it a 1:1 mapping for anyone using the Ethers.js `Provider`. However, it adds a significant amount of improved functionality on top of Ethers, such as easy access to Alchemy’s Enhanced and NFT APIs, robust WebSockets, and quality-of-life improvements such as automated retries.

The SDK currently supports the following chains (chains with '(d)' after are deprecated):

- **Ethereum**: Mainnet, Goerli (d), Sepolia, Holesky, Hoodi
- **Polygon**: Mainnet, Mumbai (d), Amoy
- **Optimism**: Mainnet, Goerli (d), Sepolia
- **Arbitrum**: Mainnet, Goerli (d), Sepolia
- **Astar**: Mainnet
- **PolygonZKEVM**: Mainnet, Testnet(d), Cardona
- **Base**: Mainnet, Goerli (d), Sepolia
- **Zksync**: Mainnet, Sepolia
- **Shape**: Mainnet, Sepolia
- **Linea**: Mainnet, Sepolia
- **Fantom**: Mainnet, Testnet
- **Zetachain**: Mainnet, Testnet
- **Arbnova**: Mainnet
- **Blast**: Mainnet, Sepolia
- **Mantle**: Mainnet, Sepolia
- **Scroll**: Mainnet, Sepolia
- **Gnosis**: Mainnet, Chiado
- **BNB**: Mainnet, Testnet
- **Avalanche**: Mainnet, Fuji
- **Celo**: Mainnet, Alfajores, Baklava
- **Metis**: Mainnet
- **OpBNB**: Mainnet, Testnet
- **Berachain**: Mainnet, Bartio, Bepolia
- **Soneium**: Mainnet, Minato
- **Worldchain**: Mainnet, Sepolia
- **Rootstock**: Mainnet, Testnet
- **Flow**: Mainnet, Testnet
- **Zora**: Mainnet, Sepolia
- **Frax**: Mainnet, Sepolia
- **Polynomial**: Mainnet, Sepolia
- **Crossfi**: Mainnet, Testnet
- **Apechain**: Mainnet, Curtis
- **Lens**: Mainnet, Sepolia
- **Geist**: Mainnet, Polter
- **Lumia**: Prism, Testnet
- **Unichain**: Mainnet, Sepolia
- **Sonic**: Mainnet, Blaze
- **XMTP**: Testnet
- **Abstract**: Mainnet, Testnet
- **Degen**: Mainnet
- **Ink**: Mainnet, Sepolia
- **Sei**: Mainnet, Testnet
- **Ronin**: Mainnet, Saigon
- **Monad**: Testnet
- **Settlus**: Mainnet, Testnet (Sepolia)
- **Gensyn**: Testnet
- **Superseed**: Mainnet, Sepolia
- **Tea**: Sepolia
- **Anime**: Mainnet, Sepolia
- **Story**: Mainnet, Aeneid
- **Megaeth**: Testnet
- **Botanix**: Mainnet, Testnet
- **Humanity**: Mainnet
- **Rise**: Testnet
- **Hyperliquid**: Mainnet, Testnet
- **Plasma**: Mainnet, Testnet

You can find per-method documentation of the Alchemy SDK endpoints at the [Alchemy Docs linked in the sidebar](https://docs.alchemy.com/reference/alchemy-sdk-quickstart).

## Getting started

```
npm install alchemy-sdk
```

After installing the app, you can then import and use the SDK:

```ts
import { Alchemy, Network } from 'alchemy-sdk';

// Optional config object, but defaults to the API key 'demo' and Network 'eth-mainnet'.
const settings = {
  apiKey: 'demo', // Replace with your Alchemy API key.
  network: Network.ETH_MAINNET // Replace with your network.
};

const alchemy = new Alchemy(settings);
```

> **ℹ️ Creating a unique Alchemy API Key**
>
> The public "demo" API key may be rate limited based on traffic. To create your own API key, **[sign up for an Alchemy account here](https://alchemy.com/?a=SDKquickstart)** and use the key created on your dashboard for the first app.

The `Alchemy` object returned by `new Alchemy()` provides access to the Alchemy API. An optional config object can be passed in when initializing to set your API key, change the network, or specify the max number of retries.

## Using the Alchemy SDK

The Alchemy SDK currently supports the following namespaces:

- `core`: All commonly-used Ethers.js Provider methods and Alchemy Enhanced API methods
- `nft`: All Alchemy NFT API methods
- `ws`: All WebSockets methods
- `transact`: All Alchemy Transaction API methods
- `notify`: CRUD endpoints for modifying Alchemy Notify Webhooks
- `debug`: Methods to inspect and replay transactions and blocks

If you are already using Ethers.js, you should be simply able to replace the Ethers.js Provider object with `alchemy.core` and it should work properly.

> **ℹ️ ENS Name Resolution**
>
> The Alchemy SDK now supports ENS names (e.g. `vitalik.eth`) for every parameter where you can pass in a Externally Owned Address, or user address (e.g. `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045`).

```ts
import { Alchemy, AlchemySubscription } from 'alchemy-sdk';

// Using default settings - pass in a settings object to specify your API key and network
const alchemy = new Alchemy();

// Access standard Ethers.js JSON-RPC node request
alchemy.core.getBlockNumber().then(console.log);

// Access Alchemy Enhanced API requests
alchemy.core
  .getTokenBalances('0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE')
  .then(console.log);

// Access the Alchemy NFT API
alchemy.nft.getNftsForOwner('vitalik.eth').then(console.log);

// Access WebSockets and Alchemy-specific WS methods
alchemy.ws.on(
  {
    method: AlchemySubscription.PENDING_TRANSACTIONS
  },
  res => console.log(res)
);
```

The Alchemy SDK also supports a number of Ethers.js objects that streamline the development process:

- [`Utils`](https://docs.ethers.io/v5/api/utils/): Equivalent to `ethers.utils`, this provides a number of common Ethers.js utility methods for developers.
  - [`Interface`](https://docs.ethers.io/v5/api/utils/abi/interface/): Found in `Utils.Interface`, this class abstracts the encoding and decoding required to interact with contracts on the Ethereum network.
- [`Contract`](https://docs.ethers.io/v5/api/contract/contract/): An abstraction for smart contract code deployed to the blockchain.
- [`ContractFactory`](https://docs.ethers.io/v5/api/contract/contract-factory/): Allows developers to build a `Contract` object.
- [`Wallet`](https://docs.ethers.io/v5/api/signer/#Wallet): An implementation of `Signer` that can sign transactions and messages using a private key as a standard Externally Owned Account.

## Alchemy Settings

An `AlchemySettings` object can be passed on instantiation to the Alchemy object, with the following optional parameters:

- `apiKey`: API key that can be found in the Alchemy dashboard. Defaults to `demo`: a rate-limited public key.
- `network`: Name of the network. Defaults to `Network.ETH_MAINNET`
- `maxRetries`: The maximum number of retries to attempt if a request fails. Defaults to 5.
- `url`: Optional URL endpoint to use for all requests. Setting this field will override the URL generated by the `network` and`apiKey` fields.
- `authToken`: Alchemy auth token required to use the Notify API. This token can be found in the Alchemy Dashboard on the Notify tab.
- `batchRequests`: Optional setting that automatically batches and sends json-rpc requests for higher throughput and reduced network IO. Defaults to false.
- `requestTimeout`: Optional setting that sets the timeout for requests in milliseconds for the NFT and Notify namespaces. Defaults to no timeout.

## Alchemy Core

The core namespace contains all commonly-used [Ethers.js Provider](https://docs.ethers.io/v5/api/providers/api-providers/#AlchemyProvider) methods. If you are already using Ethers.js, you should be simply able to replace the Ethers.js Provider object with `alchemy.core` when accessing provider methods and it should just work.

It also includes the majority of Alchemy Enhanced APIs, including:

- `getTokenMetadata()`: Get the metadata for a token contract address.
- `getTokenBalances()`: Gets the token balances for an owner given a list of contracts.
- `getAssetTransfers()`: Get transactions for specific addresses.
- `getTransactionReceipts()`: Gets all transaction receipts for a given block.

You will also find the following utility methods:

- `findContractDeployer()`: Find the contract deployer and block number for a given contract address.
- `getTokensForOwner()`: Get all token balances and metadata for a given owner address

### Accessing the full Ethers.js Provider

To keep the package clean, we don't support certain uncommonly-used Ethers.js Provider methods as top-level methods in the Alchemy `core` namespace - for example, `provider.formatter`. If you'd like to access these methods, simply use the `alchemy.config.getProvider()` function to configure the
Ethers.js Provider [AlchemyProvider](https://docs.ethers.io/v5/api/providers/api-providers/#AlchemyProvider) and return it.

```ts
import { Alchemy } from 'alchemy-sdk';

const alchemy = new Alchemy();

async function runAlchemy() {
  const ethersProvider = await alchemy.config.getProvider();
  console.log(ethersProvider.formatter);
}
runAlchemy();
```

## Alchemy WebSockets

In addition to the built-in Ethers.js listeners, the Alchemy SDK includes support for [Alchemy's Subscription API](https://docs.alchemy.com/alchemy/enhanced-apis/subscription-api-websockets). This allows you to subscribe to events and receive updates as they occur.

The `alchemy.ws` instance can be used like the standard Ethers.js [WebSocketProvider](https://docs.ethers.io/v5/api/providers/other/#WebSocketProvider) to add listeners for Alchemy events:

```ts
import { Alchemy, AlchemySubscription } from 'alchemy-sdk';

const alchemy = new Alchemy();

// Listen to all new pending transactions.
alchemy.ws.on('block', res => console.log(res));

// Listen to only the next transaction on the USDC contract.
alchemy.ws.once(
  {
    method: AlchemySubscription.PENDING_TRANSACTIONS,
    toAddress: 'vitalik.eth'
  },
  res => console.log(res)
);

// Remove all listeners.
alchemy.ws.removeAllListeners();
```

The SDK brings multiple improvements to ensure correct WebSocket behavior in cases of temporary network failure or
dropped connections. As with any network connection, you should not assume that a WebSocket will remain open forever
without interruption, but correctly handling dropped connections and reconnection by hand can be challenging to get
right. The Alchemy SDK automatically handles these failures with no configuration necessary. The main benefits are:

- Resilient event delivery: Unlike standard Web3.js or Ethers.js, you will not permanently miss events which arrive
  while the backing WebSocket is temporarily down. Instead, you will receive these events as soon as the connection
  is reopened. Note that if the connection is down for more than 120 blocks (approximately 20 minutes), you may
  still miss some events that were not part of the most recent 120 blocks.
- Lowered rate of failure: Compared to standard Web3.js or Ethers.js, there are fewer failures when sending requests
  over the WebSocket while the connection is down. The Alchemy SDK will attempt to send the requests once the connection
  is reopened. Note that it is still possible, with a lower likelihood, for outgoing requests to be lost,
  so you should still have error handling as with any network request.

## Alchemy Transact

The `transact` namespace contains methods used for simulating and sending transactions. The unique methods to the `transact` namespace are:

- `sendPrivateTransaction()`: Send a private transaction through Flashbots.
- `cancelPrivateTransaction()`: Cancel a private transaction sent with Flashbots.
- `simulateAssetChanges()`: Simulate a transaction and get a list of asset changes.
- `simulateExecution()`: Simulate a transaction and get a full list of internal transactions, logs, ABI decoded results and more.
- `simulateAssetChangesBundle()`: Simulate a list of transactions in sequence and get a list of asset changes.
- `simulateExecutionBundle()`: Simulate a list of transactions in sequence and get a full list of internal transactions, logs, ABI decoded results and more.

The `transact` namespace also aliases over several commonly used methods from the `core` namespace for convenience:

- `getTransaction()`: Returns the transaction for the given transaction hash.
- `sendTransaction()`: Sends a standard transaction to the network to be mined.
- `waitForTransaction()`: Waits for a transaction to be mined and returns the transaction receipt.

## Alchemy NFT API

The SDK currently supports the following [NFT API](https://docs.alchemy.com/alchemy/enhanced-apis/nft-api) endpoints
under the `alchemy.nft` namespace:

- `getNftMetadata()`: Get the NFT metadata for an NFT contract address and tokenId.
- `getNftMetadataBatch()`: Get the NFT metadata for multiple NFT contract addresses/token id pairs.
- `getContractMetadata()`: Get the metadata associated with an NFT contract
- `getContractMetadataBatch()`: Get the metadata associated with multiple NFT contracts in a single request.
- `getContractsForOwner()`: Get all NFT contracts that the provided owner address owns.
- `getNftsForOwner()`: Get NFTs for an owner address.
- `getNftsForOwnerIterator()`: Get NFTs for an owner address as an async iterator (handles paging automatically).
- `getNftsForContract()`: Get all NFTs for a contract address.
- `getNftsForContractIterator()`: Get all NFTs for a contract address as an async iterator (handles paging
  automatically).
- `getOwnersForNft()`: Get all the owners for a given NFT contract address and a particular token ID.
- `getOwnersForContract()`: Get all the owners for a given NFT contract address.
- `getMintedNfts()`: Get all the NFTs minted by the owner address.
- `getTransfersForOwner()`: Get all the NFT transfers for a given owner address.
- `getTransfersForContract()`: Get all the NFT transfers for a given NFT contract address.
- `verifyNftOwnership()`: Check whether the provided owner address owns the provided NFT contract addresses.
- `isSpamContract()`: Check whether the given NFT contract address is a spam contract as defined by Alchemy (see the [NFT API FAQ](https://docs.alchemy.com/alchemy/enhanced-apis/nft-api/nft-api-faq#nft-spam-classification))
- `getSpamContracts()`: Returns a list of all spam contracts marked by Alchemy.
- `reportSpam()`: Report feedback that a given NFT contract address is a spam contract as defined by Alchemy.
- `isAirdropNft()`: Check whether the given NFT token is marked as an airdrop or not. Airdrops are defined as NFTs that were minted to a user address in a transaction sent by a different address.
- `refreshNftMetadata()`: Refresh the cached NFT metadata for a contract address and a single tokenId.
- `refreshContract()`: Enqueues the specified contract address to have all token ids' metadata refreshed.
- `getFloorPrice()`: Return the floor prices of a NFT contract by marketplace.
- `computeRarity()`: Get the rarity of each attribute of an NFT.
- `getNftSales()`: Returns NFT sales that have happened through on-chain marketplaces.
- `summarizeNftAttributes()`: Get the summary of attribute prevalence for all NFTs in a contract.
- `searchContractMetadata()`: Search for a keyword across metadata of all ERC-721 and ERC-1155 smart contracts.

### Pagination

The Alchemy NFT endpoints return 100 results per page. To get the next page, you can pass in the `pageKey` returned by
the
previous call. To simplify paginating through all results, the SDK provides the `getNftsIterator()`
and `getNftsForContractIterator()` functions that automatically paginate through all NFTs and yields them via
an `AsyncIterable`.

Here's an example of how to paginate through all the NFTs in Vitalik's ENS address:

```ts
import { Alchemy } from 'alchemy-sdk';

const alchemy = new Alchemy();

async function main() {
  const ownerAddress = 'vitalik.eth';
  for await (const nft of alchemy.nft.getNftsForOwnerIterator(ownerAddress)) {
    console.log('ownedNft:', nft);
  }
}

main();
```

### SDK vs API Differences

The NFT API in the SDK standardizes response types to reduce developer friction, but note this results in some
differences compared to the Alchemy REST endpoints:

- Methods referencing `Collection` have been renamed to use the name `Contract` for greater accuracy: e.g. `getNftsForContract`.
- Some methods have different naming that the REST API counterparts in order to provide a consistent API interface (
  e.g. `getNftsForOwner()` is `alchemy_getNfts`, `getOwnersForNft()` is `alchemy_getOwnersForToken`).
- SDK standardizes to `omitMetadata` parameter (vs. `withMetadata`).
- Standardization to `pageKey` parameter for pagination (vs. `nextToken`/`startToken`)
- Empty `TokenUri` fields are omitted.
- Token ID is always normalized to an integer string on `BaseNft` and `Nft`.
- Some fields omitted in the REST response are included in the SDK response in order to return an `Nft` object.
- Some fields in the SDK's `Nft` object are named differently than the REST response.

## Alchemy Portfolio API

The [Alchemy Portfolio APIs](https://www.alchemy.com/docs/reference/portfolio-apis) include everything you need to build a view of a user’s assets: fungibles, NFTs, and their transactions.

Methods on the `PortfolioNamespace` can be accessed via `alchemy.portfolio`. To use the methods, you must include your team's auth token in the `authToken` field of `AlchemySettings` when instantiating the SDK. The auth token can be found on the Alchemy Dashboard.

Methods include:

- `getTokensByWallet()`: Fetches fungible tokens (native and ERC-20) for multiple wallet addresses and networks.
- `getTokenBalancesByWallet()`: Fetches fungible tokens (native and ERC-20) for multiple wallet addresses and networks.
- `getNftsByWallet()`: Fetches NFTs for multiple wallet addresses and networks.
- `getNftCollectionsByWallet()`: Fetches NFT collections (contracts) for multiple wallet addresses and networks.
- `getTransactionsByWallet()`: Fetches all historical transactions (internal & external) for multiple wallet addresses and networks.

## Alchemy Notify

The [Alchemy Notify API](https://docs.alchemy.com/reference/notify-api-quickstart) helps developers set up webhooks in their apps. The namespace provides methods to programmatically create, read, update, and delete your webhooks along with typings for the different webhooks. To learn more about Webhooks, please refer to the [Alchemy documentation](https://docs.alchemy.com/reference/notify-api-quickstart#what-are-webhooks).

Methods on the `NotifyNamespace` can be accessed via `alchemy.notify`. To use the methods, you must include your team's auth token in the `authToken` field of `AlchemySettings` when instantiating the SDK. The auth token can be found on the Alchemy Dashboard in the Notify Tab.

Methods include:

- `getAllWebhooks()`: Get all webhooks on your team.
- `getAddresses()`: Get all addresses tracked for the provided Address Activity Webhook.
- `getNftFilters()`: Get all NFT filters tracked for the provided NFT Activity Webhook.
- `createWebhook()`: Create a new webhook.
- `updateWebhook()`: Update an existing webhook's active status or tracked addresses and NFT filters.
- `deleteWebhook()`: Delete the provided webhook.

## Alchemy Debug

Methods on the `DebugNamespace` can be accessed via `alchemy.debug`. These methods are used for inspecting and debugging transactions.

Methods include:

- `traceCall()`: Run an `eth_call` with the context of the provided block execution using the final state of the parent block as the base.
- `traceTransaction()`: Run the transaction in the exact same manner as it was executed on the network. It will replay any transaction that may have been executed prior to this one before it and will then attempt to execute the transaction that corresponds to the given hash.
- `traceBlock()`: Replay a block that has already been mined.

## Documentation

The SDK is documented via `tsdoc` comments in the source code. The generated types and documentation are included when
using an IDE. To browse the documentation separately, you can view the generated API interfaces
in `etc/alchemy-sdk.api.md`. You can view generated Markdown files for each endpoint in the `docs-md` directory,
or as a webpage by opening `docs/index.html` in your browser.

## Usage Examples

Below are a few usage examples.

> **ℹ️ More Examples **
>
> You can also go here: [Examples Using the Alchemy SDK](https://docs.alchemy.com/reference/using-the-alchemy-sdk).

### Getting the NFTs owned by an address

```ts
import { Alchemy, NftExcludeFilters } from 'alchemy-sdk';

const alchemy = new Alchemy();

// Get how many NFTs an address owns.
alchemy.nft.getNftsForOwner('vitalik.eth').then(nfts => {
  console.log(nfts.totalCount);
});

// Get all the image urls for all the NFTs an address owns.
async function main() {
  for await (const nft of alchemy.nft.getNftsForOwnerIterator('vitalik.eth')) {
    console.log(nft.media);
  }
}

main();

// Filter out spam NFTs.
alchemy.nft
  .getNftsForOwner('vitalik.eth', {
    excludeFilters: [NftExcludeFilters.SPAM]
  })
  .then(console.log);
```

### Getting all the owners of the BAYC NFT

```ts
import { Alchemy } from 'alchemy-sdk';

const alchemy = new Alchemy();

// Bored Ape Yacht Club contract address.
const baycAddress = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D';

async function main() {
  for await (const nft of alchemy.nft.getNftsForContractIterator(baycAddress, {
    // Omit the NFT metadata for smaller payloads.
    omitMetadata: true
  })) {
    await alchemy.nft
      .getOwnersForNft(nft.contract.address, nft.tokenId)
      .then(response =>
        console.log('owners:', response.owners, 'tokenId:', nft.tokenId)
      );
  }
}

main();
```

### Get all outbound transfers for a provided address

```ts
import { Alchemy } from 'alchemy-sdk';

const alchemy = new Alchemy();

alchemy.core.getTokenBalances('vitalik.eth').then(console.log);
```

## Questions and Feedback

If you have any questions, issues, or feedback, please file an issue
on [GitHub](https://github.com/alchemyplatform/alchemy-sdk-js/issues), or drop us a message on
our [Discord](https://discord.com/invite/alchemyplatform) channel for the SDK.


---

## 82. metamask-sdk-1
- **URL:** https://github.com/devtechedge/metamask-sdk-1
- **Language:** TypeScript
- **Topics:** None
- **Description:** The simplest yet most secure way to connect your blockchain-based applications to millions of MetaMask Wallet users.

### README.md

# MetaMask SDK (Deprecated)

> **⚠️ DEPRECATED**
>
> This repository is deprecated and no longer actively maintained. MetaMask SDK has been superseded by **MetaMask Connect**, a ground-up rewrite with a streamlined API, direct wallet communication (no relay server), and multichain support out of the box.
>
> **Migrate to:**
>
> - [`@metamask/connect-evm`](https://www.npmjs.com/package/@metamask/connect-evm) — drop-in EVM dapp integration (browser, Node.js, React Native)
> - [`@metamask/connect-multichain`](https://www.npmjs.com/package/@metamask/connect-multichain) — multichain dapp integration (EVM + non-EVM)
>
> **Migration guide & docs:** <https://docs.metamask.io/metamask-connect>
>
> **New repo:** <https://github.com/MetaMask/connect-monorepo>

---

[![codecov](https://codecov.io/gh/MetaMask/metamask-sdk/graph/badge.svg?token=6B3Z3724OO)](https://codecov.io/gh/MetaMask/metamask-sdk)

MetaMask SDK enables developers to seamlessly connect their dapps to the MetaMask extension and mobile app.

You can use the SDK via the following platforms and libraries:

- [Wagmi](https://docs.metamask.io/sdk/connect/javascript-wagmi/) (recommended)
- [JavaScript](https://docs.metamask.io/sdk/connect/javascript/)
- [Dynamic SDK](https://docs.metamask.io/sdk/connect/javascript-dynamic/)
- [Web3Auth SDK](https://docs.metamask.io/sdk/connect/javascript-web3auth/)
- [React Native](https://docs.metamask.io/sdk/connect/react-native/)
- [Web3-Onboard](https://onboard.blocknative.com/)

See the [MetaMask SDK documentation](https://docs.metamask.io/sdk/) for more information.

## Features

- Session persistence
- Multi MetaMask provider (let user choose between browser extension and mobile wallet)
- Batch RPC calls (send multiple requests to your wallet at once)
- Read-only RPC calls and Infura integration
- Wagmi hook integration (alpha)
- i18n
- Full modal UI customization
- Smart contract library (coming soon)

## Get started

Install the SDK:

```bash
yarn add @metamask/sdk
```

or

```bash
npm i @metamask/sdk
```

## SDK options

See the full list of [JavaScript SDK options](https://docs.metamask.io/sdk/reference/sdk-options/).

## Contributing

To contribute to MetaMask SDK, see the [contribution guidelines](./docs/contributing.md).

## Contacts

Fill out [this form](https://fq1an8d8ib2.typeform.com/to/sC7eK5F1) for a complimentary design
optimization workshop.


---

## 83. sdk
- **URL:** https://github.com/devtechedge/sdk
- **Language:** TypeScript
- **Topics:** None
- **Description:** Repository for shared logic and useful utilities

### README.md

# Across SDK

Across is a system that quickly moves tokens across chains. This repository contains shareable code and libraries for Across.

## Modules
| Name | Description | README | Source Code |
|---|---|---|---|
| **LP Fee Calculator** | Calculate LP fee for transfers | [README](./src/lpFeeCalculator/README.md) | [Source Code](./src/lpFeeCalculator/) |
| **Merkle Distributor** | ACX token distribution | [README](./src/merkleDistributor/README.md) | [Source Code](./src/merkleDistributor/) |

## TSDX User Guide

**This project was bootstrapped with [tsdx](https://github.com/jaredpalmer/tsdx). Read below for more instructions or check out the [repository](https://github.com/jaredpalmer/tsdx)**

Congrats! You just saved yourself hours of work by bootstrapping this project with TSDX. Let’s get you oriented with what’s here and how to use it.

> This TSDX setup is meant for developing libraries (not apps!) that can be published to NPM. If you’re looking to build a Node app, you could use `ts-node-dev`, plain `ts-node`, or simple `tsc`.

> If you’re new to TypeScript, checkout [this handy cheatsheet](https://devhints.io/typescript)

## Commands

TSDX scaffolds your new library inside `/src`.

To run TSDX, use:

```bash
npm start # or yarn start
```

This builds to `/dist` and runs the project in watch mode so any edits you save inside `src` causes a rebuild to `/dist`.

To do a one-off build, use `npm run build` or `yarn build`.

To run tests, use `npm test` or `yarn test`.

## Configuration

Code quality is set up for you with `prettier`, `husky`, and `lint-staged`. Adjust the respective fields in `package.json` accordingly.

### Jest

Jest tests are set up to run with `npm test` or `yarn test`.

### Bundle Analysis

[`size-limit`](https://github.com/ai/size-limit) is set up to calculate the real cost of your library with `npm run size` and visualize the bundle with `npm run analyze`.

#### Setup Files

This is the folder structure we set up for you:

```txt
/src
  index.tsx       # EDIT THIS
/test
  blah.test.tsx   # EDIT THIS
.gitignore
package.json
README.md         # EDIT THIS
tsconfig.json
```

### Rollup

TSDX uses [Rollup](https://rollupjs.org) as a bundler and generates multiple rollup configs for various module formats and build settings. See [Optimizations](#optimizations) for details.

### TypeScript

`tsconfig.json` is set up to interpret `dom` and `esnext` types, as well as `react` for `jsx`. Adjust according to your needs.

## Continuous Integration

### GitHub Actions

Two actions are added by default:

- `main` which installs deps w/ cache, lints, tests, and builds on all pushes against a Node and OS matrix
- `size` which comments cost comparison of your library on every pull request using [`size-limit`](https://github.com/ai/size-limit)

## Optimizations

Please see the main `tsdx` [optimizations docs](https://github.com/palmerhq/tsdx#optimizations). In particular, know that you can take advantage of development-only optimizations:

```js
// ./types/index.d.ts
declare var __DEV__: boolean;

// inside your code...
if (__DEV__) {
  console.log('foo');
}
```

You can also choose to install and use [invariant](https://github.com/palmerhq/tsdx#invariant) and [warning](https://github.com/palmerhq/tsdx#warning) functions.

## Module Formats

CJS, ESModules, and UMD module formats are supported.

The appropriate paths are configured in `package.json` and `dist/index.js` accordingly. Please report if any issues are found.

## Named Exports

Per Palmer Group guidelines, [always use named exports.](https://github.com/palmerhq/typescript#exports) Code split inside your React app instead of your React library.

## Including Styles

There are many ways to ship styles, including with CSS-in-JS. TSDX has no opinion on this, configure how you like.

For vanilla CSS, you can include it at the root directory and add it to the `files` section in your `package.json`, so that it can be imported separately by your users and run through their bundler's loader.

## Publishing a new version
1. Bump version in package.json and merge to master. Example: https://github.com/across-protocol/sdk/pull/67
2. Create a new release with a new tag (version number should be incremented): https://github.com/across-protocol/sdk/releases
3. Update any upstream repos/binaries that depend on the sdk such as https://github.com/across-protocol/frontend. Example: https://github.com/across-protocol/frontend/pull/202


---

## 84. metamask-sdk-empty-placeholder
- **URL:** https://github.com/devtechedge/metamask-sdk-empty-placeholder
- **Language:** Not specified
- **Topics:** None
- **Description:** No description

### README.md

*No standard README.md found.*

---

## 85. crewAI
- **URL:** https://github.com/devtechedge/crewAI
- **Language:** Python
- **Topics:** None
- **Description:** Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

### README.md

<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="docs/images/crewai_logo.png" width="600px" alt="Open source Multi-AI Agent orchestration framework">
  </a>
</p>
<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/11239" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/11239" alt="crewAIInc%2FcrewAI | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <a href="https://crewai.com">Homepage</a>
  ·
  <a href="https://crewai.com/open-source">Open Source</a>
  ·
  <a href="https://docs.crewai.com">Docs</a>
  ·
  <a href="https://app.crewai.com">Start Cloud Trial</a>
  ·
  <a href="https://blog.crewai.com">Blog</a>
  ·
  <a href="https://community.crewai.com">Forum</a>
</p>

<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="https://img.shields.io/github/stars/crewAIInc/crewAI" alt="GitHub Repo stars">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/network/members">
    <img src="https://img.shields.io/github/forks/crewAIInc/crewAI" alt="GitHub forks">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/issues">
    <img src="https://img.shields.io/github/issues/crewAIInc/crewAI" alt="GitHub issues">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/pulls">
    <img src="https://img.shields.io/github/issues-pr/crewAIInc/crewAI" alt="GitHub pull requests">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  </a>
</p>

<p align="center">
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/v/crewai" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/dm/crewai" alt="PyPI downloads">
  </a>
  <a href="https://twitter.com/crewAIInc">
    <img src="https://img.shields.io/twitter/follow/crewAIInc?style=social" alt="Twitter Follow">
  </a>
</p>

### Fast and Flexible Multi-Agent Automation Framework

> CrewAI is an open-source Python framework with high-level abstractions and low-level APIs for building production-ready multi-agent workflows.
> It gives developers autonomous agent collaboration through Crews and precise, event-driven control through Flows.

- **CrewAI Crews**: Optimize for autonomy and collaborative intelligence with role-based AI agents.
- **CrewAI Flows**: Build event-driven automations that combine precise workflow control, single LLM calls, and native support for Crews.

With over 100,000 developers certified through our community courses at [learn.crewai.com](https://learn.crewai.com), CrewAI is rapidly becoming the
standard for production-ready agentic automation.

# CrewAI AMP Suite

For organizations that need a commercial control plane around CrewAI, [CrewAI AMP Suite](https://crewai.com/amp) adds managed deployment, observability, governance, security, and enterprise support.

You can try one part of the suite, the [Crew Control Plane, for free](https://app.crewai.com).

## Crew Control Plane Key Features:

- **Tracing & Observability**: Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces.
- **Unified Control Plane**: A centralized platform for managing, monitoring, and scaling your AI agents and workflows.
- **Seamless Integrations**: Easily connect with existing enterprise systems, data sources, and cloud infrastructure.
- **Advanced Security**: Built-in robust security and compliance measures ensuring safe deployment and management.
- **Actionable Insights**: Real-time analytics and reporting to optimize performance and decision-making.
- **24/7 Support**: Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues.
- **On-premise and Cloud Deployment Options**: Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements.

CrewAI AMP is designed for enterprises seeking a powerful, reliable solution to transform complex business processes into efficient,
intelligent automations.

## Table of contents

- [Build with AI](#build-with-ai)
- [Why CrewAI?](#why-crewai)
- [Getting Started](#getting-started)
  - [Learning Resources](#learning-resources)
  - [Understanding Flows and Crews](#understanding-flows-and-crews)
  - [Installation](#1-installation)
  - [Setting Up Your Crew](#2-setting-up-your-crew)
  - [Running Your Crew](#3-running-your-crew)
- [Key Features](#key-features)
- [Examples](#examples)
  - [Quick Tutorial](#quick-tutorial)
  - [Write Job Descriptions](#write-job-descriptions)
  - [Trip Planner](#trip-planner)
  - [Stock Analysis](#stock-analysis)
  - [Using Crews and Flows Together](#using-crews-and-flows-together)
- [Connecting Your Crew to a Model](#connecting-your-crew-to-a-model)
- [When to Use CrewAI](#when-to-use-crewai)
- [Contribution](#contribution)
- [Telemetry](#telemetry)
- [License](#license)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)

## Build with AI

Using an AI coding agent? Teach it CrewAI best practices in one command:

**Claude Code:**
```shell
/plugin marketplace add crewAIInc/skills
/plugin install crewai-skills@crewai-plugins
/reload-plugins
```
Four skills that activate automatically when you ask relevant CrewAI questions:

| Skill | When it runs |
|-------|--------------|
| `getting-started` | Scaffolding new projects, choosing between `LLM.call()` / `Agent` / `Crew` / `Flow`, wiring `crew.jsonc` / `main.py` |
| `design-agent` | Configuring agents — role, goal, backstory, tools, LLMs, memory, guardrails |
| `design-task` | Writing task descriptions, dependencies, structured output (`output_pydantic`, `output_json`), human review |
| `ask-docs` | Querying the live [CrewAI docs MCP server](https://docs.crewai.com/mcp) for up-to-date API details |

**Cursor, Codex, Windsurf, and others ([skills.sh](https://skills.sh/crewaiinc/skills)):**
```shell
npx skills add crewaiinc/skills
```

This installs the official [CrewAI Skills](https://github.com/crewAIInc/skills) — structured instructions that teach coding agents how to scaffold Flows, configure Crews, design agents and tasks, and follow CrewAI patterns.

## Why CrewAI?

<div align="center" style="margin-bottom: 30px;">
  <img src="docs/images/asset.png" alt="CrewAI Logo" width="100%">
</div>

CrewAI unlocks the true potential of multi-agent automation, delivering speed, flexibility, and control through Crews of AI agents and event-driven Flows:

- **Purpose-built architecture**: Designed specifically for agent orchestration, with a lightweight Python core and clean primitives for real-world automation.
- **High Performance**: Optimized for speed and minimal resource usage, enabling faster execution.
- **Flexible Low-Level Customization**: Complete freedom to customize everything from workflows and system architecture to agent behaviors, internal prompts, and execution logic.
- **Ideal for Every Use Case**: Proven effective for simple tasks, complex workflows, and production-grade automation.
- **Robust Community**: Backed by a rapidly growing community of over **100,000 certified** developers offering comprehensive support and resources.

CrewAI empowers developers and teams to build intelligent automations that balance simplicity, flexibility, and production-grade control.

## Getting Started

Setup and run your first CrewAI agents by following this tutorial.

[![CrewAI Getting Started Tutorial](https://img.youtube.com/vi/-kSOTtYzgEw/hqdefault.jpg)](https://www.youtube.com/watch?v=-kSOTtYzgEw "CrewAI Getting Started Tutorial")

### Learning Resources

Learn CrewAI through our comprehensive courses:

- [Multi AI Agent Systems with CrewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - Master the fundamentals of multi-agent systems
- [Practical Multi AI Agents and Advanced Use Cases](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/) - Deep dive into advanced implementations

### Understanding Flows and Crews

CrewAI offers two powerful, complementary approaches that work seamlessly together to build sophisticated AI applications:

1. **Crews**: Teams of AI agents with true autonomy and agency, working together to accomplish complex tasks through role-based collaboration. Crews enable:

   - Natural, autonomous decision-making between agents
   - Dynamic task delegation and collaboration
   - Specialized roles with defined goals and expertise
   - Flexible problem-solving approaches

2. **Flows**: Production-ready, event-driven workflows that deliver precise control over complex automations. Flows provide:

   - Fine-grained control over execution paths for real-world scenarios
   - Secure, consistent state management between tasks
   - Clean integration of AI agents with production Python code
   - Conditional branching for complex business logic

The true power of CrewAI emerges when combining Crews and Flows. This synergy allows you to:

- Build complex, production-grade applications
- Balance autonomy with precise control
- Handle sophisticated real-world scenarios
- Maintain clean, maintainable code structure

### Getting Started with Installation

To get started with CrewAI, follow these simple steps. The full walkthrough lives in the [installation guide](https://docs.crewai.com/en/installation).

### 1. Installation

CrewAI requires `Python >=3.10 and <3.14`. Check your version with:

```bash
python3 --version
```

CrewAI uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling. If you haven't installed `uv` yet, install it first.

**macOS/Linux:**

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If your system doesn't have `curl`, you can use `wget`:

```shell
wget -qO- https://astral.sh/uv/install.sh | sh
```

**Windows:**

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

If you run into any issues, refer to [UV's installation guide](https://docs.astral.sh/uv/getting-started/installation/).

Then install the CrewAI CLI:

```shell
uv tool install crewai
```

If you encounter a `PATH` warning, run:

```shell
uv tool update-shell
```

If you encounter the `chroma-hnswlib==0.7.6` build error (`fatal error C1083: Cannot open include file: 'float.h'`) on Windows, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) with *Desktop development with C++*.

Verify the install:

```shell
uv tool list
```

You should see something like:

```shell
crewai v0.102.0
- crewai
```

To upgrade the global CLI later:

```shell
uv tool install crewai --upgrade
```

This upgrades the **global `crewai` CLI tool** only. To upgrade the `crewai` version inside a project's virtual environment, see [Upgrading CrewAI in a project](https://docs.crewai.com/en/guides/migration/upgrading-crewai).

### 2. Setting Up Your Crew

`crewai create crew` creates a JSON-first crew project. Agents live in `agents/*.jsonc`, tasks and crew-level settings live in `crew.jsonc`, and `crewai run` loads that JSON definition directly.

```shell
crewai create crew <project_name>
```

This command creates a new project folder with the following structure:

```
my_project/
├── .gitignore
├── .env
├── agents/
│   └── researcher.jsonc
├── crew.jsonc
├── knowledge/
├── pyproject.toml
├── README.md
├── skills/
└── tools/
```

If you need the older Python/YAML scaffold with `crew.py`, `config/agents.yaml`, and `config/tasks.yaml`, run:

```shell
crewai create crew <project_name> --classic
```

See [Using Annotations](https://docs.crewai.com/en/learn/using-annotations) for the classic pattern.

#### To customize your project, you can:

- Modify `agents/*.jsonc` to define each agent's role, goal, backstory, LLM, tools, and behavior.
- Modify `crew.jsonc` to define tasks, process, and input defaults.
- Add custom tools in `tools/` and reference them as `"custom:<name>"`.
- Add optional knowledge files in `knowledge/` and skill files in `skills/`.
- Add your environment variables into the `.env` file.

Use `{placeholder}` values in agent and task text, then set defaults in `crew.jsonc` under `inputs`. When you run `crewai run`, the CLI prompts for any missing values.

#### Example of a simple crew with a sequential process:

```shell
crewai create crew latest-ai-development
cd latest_ai_development
```

Then edit the generated files:

**agents/researcher.jsonc**

```jsonc
{
  "role": "{topic} Senior Data Researcher",
  "goal": "Uncover cutting-edge developments in {topic}",
  "backstory": "You're a seasoned researcher who finds relevant information and presents it clearly.",
  "llm": "openai/gpt-4o",
  "tools": ["SerperDevTool"],
  "settings": {
    "verbose": true
  }
}
```

**agents/reporting_analyst.jsonc**

```jsonc
{
  "role": "{topic} Reporting Analyst",
  "goal": "Create detailed reports based on {topic} data analysis and research findings",
  "backstory": "You're a meticulous analyst who turns complex data into clear, concise reports.",
  "llm": "openai/gpt-4o",
  "settings": {
    "verbose": true
  }
}
```

**crew.jsonc**

```jsonc
{
  "name": "Latest AI Development",
  "agents": ["researcher", "reporting_analyst"],
  "tasks": [
    {
      "name": "research_task",
      "description": "Conduct thorough research about {topic}. Find recent, relevant information.",
      "expected_output": "A list with 10 bullet points of the most relevant information about {topic}.",
      "agent": "researcher"
    },
    {
      "name": "reporting_task",
      "description": "Review the research and expand each topic into a full section for a report.",
      "expected_output": "A markdown report with the main topics, each with a full section of information. No fenced code blocks around the whole document.",
      "agent": "reporting_analyst",
      "context": ["research_task"],
      "output_file": "output/report.md",
      "markdown": true
    }
  ],
  "process": "sequential",
  "verbose": true,
  "inputs": {
    "topic": "AI Agents"
  }
}
```

### 3. Running Your Crew

Before running your crew, set the required keys in your `.env` file:

- Your model provider API key — see [LLM setup](https://docs.crewai.com/en/concepts/llms#setting-up-your-llm)
- A [Serper.dev](https://serper.dev/) API key if you use web search: `SERPER_API_KEY=YOUR_KEY_HERE`

Then install dependencies and run from the project directory:

```shell
crewai install
crewai run
```

If you need additional packages, use `uv add <package-name>`.

You should see the output in the console, and `output/report.md` should be created in the project root.

In addition to the sequential process, you can use the hierarchical process, which automatically assigns a manager to the defined crew to properly coordinate the planning and execution of tasks through delegation and validation of results. [See more about the processes here](https://docs.crewai.com/en/concepts/processes).

For a Flow-first walkthrough, see the [Quickstart](https://docs.crewai.com/en/quickstart).

## Key Features

CrewAI gives developers a practical foundation for building agentic systems that move from prototype to production: autonomous collaboration where it helps, explicit workflow control where it matters, and Python-native customization throughout.

- **Crews for autonomy**: Model teams of specialized AI agents with roles, goals, tools, and tasks.
- **Flows for control**: Build event-driven workflows with state, branching, routing, and production logic.
- **Seamless integration**: Combine Crews and Flows to create complex, real-world automations.
- **Python-native customization**: Customize prompts, tools, execution paths, state, and integrations without fighting the framework.
- **Agent-ready capabilities**: Use tools, memory, knowledge, checkpointing, async execution, and MCP/A2A support for more capable production agents.
- **Production-ready patterns**: Add deterministic steps, human input, structured outputs, and checkpointing as your system grows.
- **Thriving community**: Backed by robust documentation and over 100,000 certified developers, providing exceptional support and guidance.

Choose CrewAI to build powerful, adaptable, and production-ready AI automations.

## Examples

You can test different real life examples of AI crews in the [CrewAI-examples repo](https://github.com/crewAIInc/crewAI-examples?tab=readme-ov-file):

- [Landing Page Generator](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator)
- [Having Human input on the execution](https://docs.crewai.com/en/learn/human-input-on-execution)
- [Trip Planner](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner)
- [Stock Analysis](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis)

### Quick Tutorial

[![CrewAI Tutorial](https://img.youtube.com/vi/tnejrr-0a94/maxresdefault.jpg)](https://www.youtube.com/watch?v=tnejrr-0a94 "CrewAI Tutorial")

### Write Job Descriptions

[Check out code for this example](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting) or watch a video below:

[![Jobs postings](https://img.youtube.com/vi/u98wEMz-9to/maxresdefault.jpg)](https://www.youtube.com/watch?v=u98wEMz-9to "Jobs postings")

### Trip Planner

[Check out code for this example](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner) or watch a video below:

[![Trip Planner](https://img.youtube.com/vi/xis7rWp-hjs/maxresdefault.jpg)](https://www.youtube.com/watch?v=xis7rWp-hjs "Trip Planner")

### Stock Analysis

[Check out code for this example](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis) or watch a video below:

[![Stock Analysis](https://img.youtube.com/vi/e0Uj4yWdaAg/maxresdefault.jpg)](https://www.youtube.com/watch?v=e0Uj4yWdaAg "Stock Analysis")

### Using Crews and Flows Together

CrewAI's power truly shines when combining Crews with Flows to create sophisticated automation pipelines.
CrewAI flows support logical operators like `or_` and `and_` to combine multiple conditions. This can be used with `@start`, `@listen`, or `@router` decorators to create complex triggering conditions.

- `or_`: Triggers when any of the specified conditions are met.
- `and_`: Triggers when all of the specified conditions are met.

Here's how you can orchestrate multiple Crews within a Flow:

```python
from crewai.flow.flow import Flow, listen, start, router, or_
from crewai import Crew, Agent, Task, Process
from pydantic import BaseModel

# Define structured state for precise control
class MarketState(BaseModel):
    sentiment: str = "neutral"
    confidence: float = 0.0
    recommendations: list = []

class AdvancedAnalysisFlow(Flow[MarketState]):
    @start()
    def fetch_market_data(self):
        # Demonstrate low-level control with structured state
        self.state.sentiment = "analyzing"
        return {"sector": "tech", "timeframe": "1W"}  # These parameters match the task description template

    @listen(fetch_market_data)
    def analyze_with_crew(self, market_data):
        # Show crew agency through specialized roles
        analyst = Agent(
            role="Senior Market Analyst",
            goal="Conduct deep market analysis with expert insight",
            backstory="You're a veteran analyst known for identifying subtle market patterns"
        )
        researcher = Agent(
            role="Data Researcher",
            goal="Gather and validate supporting market data",
            backstory="You excel at finding and correlating multiple data sources"
        )

        analysis_task = Task(
            description="Analyze {sector} sector data for the past {timeframe}",
            expected_output="Detailed market analysis with confidence score",
            agent=analyst
        )
        research_task = Task(
            description="Find supporting data to validate the analysis",
            expected_output="Corroborating evidence and potential contradictions",
            agent=researcher
        )

        # Demonstrate crew autonomy
        analysis_crew = Crew(
            agents=[analyst, researcher],
            tasks=[analysis_task, research_task],
            process=Process.sequential,
            verbose=True
        )
        return analysis_crew.kickoff(inputs=market_data)  # Pass market_data as named inputs

    @router(analyze_with_crew)
    def determine_next_steps(self):
        # Show flow control with conditional routing
        if self.state.confidence > 0.8:
            return "high_confidence"
        elif self.state.confidence > 0.5:
            return "medium_confidence"
        return "low_confidence"

    @listen("high_confidence")
    def execute_strategy(self):
        # Demonstrate complex decision making
        strategy_crew = Crew(
            agents=[
                Agent(role="Strategy Expert",
                      goal="Develop optimal market strategy")
            ],
            tasks=[
                Task(description="Create detailed strategy based on analysis",
                     expected_output="Step-by-step action plan")
            ]
        )
        return strategy_crew.kickoff()

    @listen(or_("medium_confidence", "low_confidence"))
    def request_additional_analysis(self):
        self.state.recommendations.append("Gather more data")
        return "Additional analysis required"
```

This example demonstrates how to:

1. Use Python code for basic data operations
2. Create and execute Crews as steps in your workflow
3. Use Flow decorators to manage the sequence of operations
4. Implement conditional branching based on Crew results

## Connecting Your Crew to a Model

CrewAI supports using various LLMs through a variety of connection options. By default your agents will use the OpenAI API when querying the model. However, there are several other ways to allow your agents to connect to models. For example, you can configure your agents to use a local model via the Ollama tool.

Please refer to the [Connect CrewAI to LLMs](https://docs.crewai.com/en/learn/llm-connections) page for details on configuring your agents' connections to models.

## When to Use CrewAI

Use CrewAI when you need more than a single prompt or chatbot: multi-step work, specialized agents, tool use, structured outputs, human review, or workflows that combine autonomous reasoning with explicit business logic.

CrewAI is especially useful when you want to:

- Coordinate multiple agents with clear roles and tasks.
- Wrap agent work in deterministic, event-driven workflows.
- Keep application logic in regular Python.
- Move from experiment to production without changing frameworks.
- Add tools, memory, checkpointing, and async execution as your system grows.

## Contribution

CrewAI is open-source and we welcome contributions. See
[`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md) for the full setup guide,
branching conventions, and PR checklist.

Quick start:

```bash
git clone https://github.com/crewAIInc/crewAI.git
cd crewAI
uv sync --all-groups --all-extras
uv run pre-commit install
```

```bash
# Tests
uv run pytest lib/crewai/tests/ -x -q

# Type checks
uv run mypy lib/
```

### Contributing to the docs

The site at [docs.crewai.com](https://docs.crewai.com) is published from
`docs/` by [Mintlify](https://www.mintlify.com/). The docs use directory-based
versioning: edits to `docs/edge/<lang>/...` (e.g.
`docs/edge/en/concepts/agents.mdx`) land under the **Edge** version selector
immediately and are frozen into a new versioned snapshot under
`docs/v<X.Y.Z>/` at the next release cut. Frozen snapshots are immutable — CI
rejects PRs that modify them without a `[docs-freeze]` title prefix. The
release CLI (`devtools release`) handles the freeze automatically; see
[`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md) for contributor guidance and
[`lib/devtools/README.md`](lib/devtools/README.md) for release tooling.

## Telemetry

CrewAI uses anonymous telemetry to collect usage data with the main purpose of helping us improve the library by focusing our efforts on the most used features, integrations and tools.

It's pivotal to understand that **NO data is collected** concerning prompts, task descriptions, agents' backstories or goals, usage of tools, API calls, responses, any data processed by the agents, or secrets and environment variables, with the exception of the conditions mentioned. When the `share_crew` feature is enabled, detailed data including task descriptions, agents' backstories or goals, and other specific attributes are collected to provide deeper insights while respecting user privacy. Users can disable telemetry by setting the environment variable OTEL_SDK_DISABLED to true.

Data collected includes:

- Version of CrewAI
  - So we can understand how many users are using the latest version
- Version of Python
  - So we can decide on what versions to better support
- General OS (e.g. number of CPUs, macOS/Windows/Linux)
  - So we know what OS we should focus on and if we could build specific OS related features
- Number of agents and tasks in a crew
  - So we make sure we are testing internally with similar use cases and educate people on the best practices
- Crew Process being used
  - Understand where we should focus our efforts
- If Agents are using memory or allowing delegation
  - Understand if we improved the features or maybe even drop them
- If Tasks are being executed in parallel or sequentially
  - Understand if we should focus more on parallel execution
- Language model being used
  - Improved support on most used languages
- Roles of agents in a crew
  - Understand high level use cases so we can build better tools, integrations and examples about it
- Tools names available
  - Understand out of the publicly available tools, which ones are being used the most so we can improve them

Users can opt-in to Further Telemetry, sharing the complete telemetry data by setting the `share_crew` attribute to `True` on their Crews. Enabling `share_crew` results in the collection of detailed crew and task execution data, including `goal`, `backstory`, `context`, and `output` of tasks. This enables a deeper insight into usage patterns while respecting the user's choice to share.

## License

CrewAI is released under the [MIT License](https://github.com/crewAIInc/crewAI/blob/main/LICENSE).

## Frequently Asked Questions (FAQ)

### General

- [What exactly is CrewAI?](#q-what-exactly-is-crewai)
- [How do I install CrewAI?](#q-how-do-i-install-crewai)
- [Is CrewAI a standalone framework?](#q-is-crewai-a-standalone-framework)
- [Is CrewAI open-source?](#q-is-crewai-open-source)
- [Does CrewAI collect data from users?](#q-does-crewai-collect-data-from-users)

### Features and Capabilities

- [Can CrewAI handle complex use cases?](#q-can-crewai-handle-complex-use-cases)
- [Can I use CrewAI with local AI models?](#q-can-i-use-crewai-with-local-ai-models)
- [What makes Crews different from Flows?](#q-what-makes-crews-different-from-flows)
- [Does CrewAI support fine-tuning or training custom models?](#q-does-crewai-support-fine-tuning-or-training-custom-models)

### Resources and Community

- [Where can I find real-world CrewAI examples?](#q-where-can-i-find-real-world-crewai-examples)
- [How can I contribute to CrewAI?](#q-how-can-i-contribute-to-crewai)

### Enterprise Features

- [What additional features does CrewAI AMP offer?](#q-what-additional-features-does-crewai-amp-offer)
- [Is CrewAI AMP available for cloud and on-premise deployments?](#q-is-crewai-amp-available-for-cloud-and-on-premise-deployments)
- [Can I try CrewAI AMP for free?](#q-can-i-try-crewai-amp-for-free)

### Q: What exactly is CrewAI?

A: CrewAI is a lean, fast Python framework built specifically for orchestrating autonomous AI agents and production-ready agentic workflows.

### Q: How do I install CrewAI?

A: Install the CrewAI CLI with [UV](https://docs.astral.sh/uv/):

```shell
uv tool install crewai
```

Then create a project with `crewai create crew <project_name>`, run `crewai install`, and start it with `crewai run`. See the [installation guide](https://docs.crewai.com/en/installation) for details.

### Q: Is CrewAI a standalone framework?

A: Yes. CrewAI is a standalone Python framework with its own primitives for agents, tasks, crews, flows, tools, and orchestration.

### Q: Can CrewAI handle complex use cases?

A: Yes. CrewAI excels at both simple and highly complex real-world scenarios, offering deep customization options at both high and low levels, from internal prompts to sophisticated workflow orchestration.

### Q: Can I use CrewAI with local AI models?

A: Absolutely! CrewAI supports various language models, including local ones. Tools like Ollama and LM Studio allow seamless integration. Check the [LLM Connections documentation](https://docs.crewai.com/en/learn/llm-connections) for more details.

### Q: What makes Crews different from Flows?

A: Crews provide autonomous agent collaboration, ideal for tasks requiring flexible decision-making and dynamic interaction. Flows offer precise, event-driven control, ideal for managing detailed execution paths and secure state management. You can seamlessly combine both for maximum effectiveness.

### Q: Is CrewAI open-source?

A: Yes, CrewAI is open-source and actively encourages community contributions and collaboration.

### Q: Does CrewAI collect data from users?

A: CrewAI collects anonymous telemetry data strictly for improvement purposes. Sensitive data such as prompts, tasks, or API responses are never collected unless explicitly enabled by the user.

### Q: Where can I find real-world CrewAI examples?

A: Check out practical examples in the [CrewAI-examples repository](https://github.com/crewAIInc/crewAI-examples), covering use cases like trip planners, stock analysis, and job postings.

### Q: How can I contribute to CrewAI?

A: Contributions are warmly welcomed! Fork the repository, create your branch, implement your changes, and submit a pull request. See [`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md) for detailed guidelines.

### Q: What additional features does CrewAI AMP offer?

A: CrewAI AMP provides advanced features such as a unified control plane, real-time observability, secure integrations, advanced security, actionable insights, and dedicated 24/7 enterprise support.

### Q: Is CrewAI AMP available for cloud and on-premise deployments?

A: Yes, CrewAI AMP supports both cloud-based and on-premise deployment options, allowing enterprises to meet their specific security and compliance requirements.

### Q: Can I try CrewAI AMP for free?

A: Yes, you can explore part of the CrewAI AMP Suite by accessing the [Crew Control Plane](https://app.crewai.com) for free.

### Q: Does CrewAI support fine-tuning or training custom models?

A: Yes, CrewAI can integrate with custom-trained or fine-tuned models, allowing you to enhance your agents with domain-specific knowledge and accuracy.

### Q: Can CrewAI agents interact with external tools and APIs?

A: Absolutely! CrewAI agents can easily integrate with external tools, APIs, and databases, empowering them to leverage real-world data and resources.

### Q: Is CrewAI suitable for production environments?

A: Yes, CrewAI is designed with production-grade patterns that support reliable, stable, and scalable agentic workflows.

### Q: How scalable is CrewAI?

A: CrewAI is highly scalable, supporting simple automations and large-scale workflows involving numerous agents and complex tasks simultaneously.

### Q: Does CrewAI offer debugging and monitoring tools?

A: Yes, CrewAI AMP includes advanced debugging, tracing, and real-time observability features, simplifying the management and troubleshooting of your automations.

### Q: What programming languages does CrewAI support?

A: CrewAI is primarily Python-based but easily integrates with services and APIs written in any programming language through its flexible API integration capabilities.

### Q: Does CrewAI offer educational resources for beginners?

A: Yes, CrewAI provides extensive beginner-friendly tutorials, courses, and documentation through learn.crewai.com, supporting developers at all skill levels.

### Q: Can CrewAI automate human-in-the-loop workflows?

A: Yes, CrewAI fully supports human-in-the-loop workflows, allowing seamless collaboration between human experts and AI agents for enhanced decision-making.


---

## 86. extension
- **URL:** https://github.com/devtechedge/extension
- **Language:** TypeScript
- **Topics:** None
- **Description:** Your Web3 Wallet that just works. EIP-7702 ready.

### README.md

# Ambire Wallet

<div align="center">
  <a href="https://chromewebstore.google.com/detail/ambire-wallet/ehgjhhccekdedpbkifaojjaefeohnoea" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./mockups/mockup-dashboard-dark-v6.png">
      <source media="(prefers-color-scheme: light)" srcset="./mockups/mockup-dashboard-light-v6.png">
      <img src="./mockups/mockup-dashboard-light-v6.png" alt="Ambire Wallet Dashboard" width="528" height="648" />
    </picture>
  </a>

  <p>
    Your Web3 wallet that just works. EIP-7702 ready.<br>
    <em>A self-custodial browser wallet extension built for Ethereum and EVM networks.</em><br />
    <a href="https://www.ambire.com/get-extension" target="_blank">
      <strong>Download Ambire extension 🔥</strong>
    </a>
    <br />
    <em>(Chrome, Firefox, Brave, Opera, Edge, Arc)</em>
    <br /><br />
    👥 Join the community:
    <a href="https://discord.com/invite/Ambire" target="_blank">Discord</a> |
    <a href="https://t.me/AmbireOfficial" target="_blank">Telegram</a>
    <br />
    🐞
    <a href="https://github.com/AmbireTech/extension/issues">Report a Bug</a> ·
    <a href="https://help.ambire.com/en" target="_blank">Get help</a>
  </p>
</div>

## Environment Setup

Built in a hybrid approach (with React Native and React Native Web) so that in a single codebase we can support building cross-browser extensions, mobile apps and web apps.

This project is built with Expo's bare workflow, allowing us to extend the default Vanilla React Native with additional expo modules in the form of installable expo libraries.

More about the environment setup and prerequisites [here](https://reactnative.dev/docs/environment-setup).

Toolchain versions are pinned in the repo, so use a version manager that reads them (nvm, rbenv, jenv, etc.)

| Tool      | File             | Target   |
| --------- | ---------------- | -------- |
| Node      | `.nvmrc`         | All apps |
| Yarn      | `package.json`   | All apps |
| Ruby      | `.ruby-version`  | iOS      |
| Xcode     | `.xcode-version` | iOS      |
| CocoaPods | `Gemfile`        | iOS      |
| JDK       | `.java-version`  | Android  |

Yarn and CocoaPods are not picked up by a version manager: Yarn is pinned via `packageManager`/`engines` in `package.json`, CocoaPods via the `Gemfile` (run it through `bundle exec`, see "Mobile Apps").

## Install

Install all dependencies:

```bash
yarn setup
```

Install the [ambire-common](https://github.com/AmbireTech/ambire-common) submodule, a common ground for the Ambire apps, run:

```bash
git submodule init
git submodule update
```

## Environment Variables

Create ".env" file in the root directory and fill in all variables, see ".env-sample" for a reference.

## Editor Config

Make sure your code editor has plugins that support the following configuration files: `.editorconfig`, `.prettierrc`, `tsconfig.json`, `eslintrc.js`, [`import-sorter.json`](https://github.com/SoominHan/import-sorter).

## Browser Extensions

### Development-optimized Builds

- Start the browser extension for webkit browsers (tested mostly on Chrome and Brave):

  ```bash
  yarn web:webkit
  ```

  Then follow the instructions to load an unpacked extension [here](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked).

- Start the browser extension for gecko browsers (tested mostly on Firefox):

  ```bash
  yarn web:gecko
  ```

  Then follow the instructions to temporarily install an extension in Firefox [here](https://extensionworkshop.com/documentation/develop/temporary-installation-in-firefox/).

- Start the browser extension for the Safari browser:

  ```bash
  yarn web:safari
  ```

  Two new folders will be created:

  - build/safari-dev (dev build folder)
  - safari-extension/wallet-dev (Xcode project)

  then in the Safari browser:

  - Developer -> Developer settings...
  - Check the “Allow unsigned extensions” option. (Note: This setting may not persist after Safari is restarted.)​
  - Then the extension should be automatically added and pinned in the browser.

  NOTE: You can manage the available extensions from: Safari -> Settings... -> Extensions

  NOTE: The development script for Safari relies on the fswatch tool to automatically reload the Safari build when the development server is reloaded. If fswatch is not already installed on your system, you can install it using Homebrew with the following command:

  ```bash
  brew install fswatch
  ```

### Production-optimized Builds

- For webkit browsers:

  ```bash
  yarn build:web:webkit
  ```

  And find the resulting build in the "build/webkit-prod" folder.

- For gecko browsers:

  ```bash
  yarn build:web:gecko
  ```

  And find the resulting build in the "build/gecko-prod" folder.

- For the Safari browser:

  ```bash
  yarn build:web:safari
  ```

  Two new folders will be created:

  - "build/safari-prod" (production build folder)
  - "safari-extension/wallet" (the Xcode project)

  Then, in xCode manually do (TODO: automate these steps, it turned out to be a huge challenge):

  - Delete "walletTests" and "walletUITests" targets.
  - For both targets (macOS and extension): Signing & Capabilities: Team: "Ambire Tech Ltd", Signing Certificate: Development
  - For both targets (macOS and extension): General - Identity - Version: X.X (should match the version in the app.json file, example: `4.36`) and Build: X (integer, bump up on every next build submitted to the App Store Connect, example: `3`)
  - For the macOS target: General - App Category: "Utilities"
  - For the extension target: General - Identity - Bundle Identifier: `com.ambire.app.wallet.extension`

### LavaMoat Policy Generation

The extension uses [LavaMoat](https://github.com/LavaMoat/LavaMoat) with SES (Secure EcmaScript) to harden the background service worker. LavaMoat uses a policy file (`lavamoat/webpack/policy.json`) to control which packages can import what and access which globals.

#### When to Regenerate Policy

Regenerate the policy when:

- Adding/removing dependencies
- Updating dependencies that change their import patterns
- Runtime errors: "Policy does not allow importing X from Y"
- Runtime errors: "Policy does not allow accessing global X"

Do NOT regenerate for:

- Every build (policy is stable and should be version-controlled)
- Code changes that don't affect dependencies
- UI changes (UI chunks are unlocked and don't use policy)

#### Policy Generation Workflow

1. **Generate policy:**

   ```bash
   yarn build:extensions:generate-policy
   ```

2. **Review generated policy:**

   - Check `lavamoat/webpack/policy.json` for any unexpected entries
   - Review package dependencies and global access patterns

3. **Update policy overrides:**

   - Manually edit `lavamoat/webpack/policy-override.json` for custom overrides
   - Common overrides: primordial mutations, font packages, reflect-metadata globals

4. **Commit policy files:**

   - Both `policy.json` and `policy-override.json` should be version-controlled
   - This ensures consistent builds across environments

**Note:** The same policy works for both gecko and webkit builds since they share the same dependencies and only differ in entry points (which are mostly unlocked).

### Extract Source Maps

The production-optimized builds come with source maps files included. When preparing a production build for a browser store release, run the following commands to extract the source maps in separate directories:

- For the webkit build:

  ```bash
  yarn export:web:webkit:sourcemaps
  ```

  As a result, build/webkit-prod will no longer include the source map files (as before). Instead, a new folder, build/webkit-prod-source-maps, will be created to hold only the source maps. This folder should also be included in the GitHub release tag we create.

- For the gecko build:

  ```bash
  yarn export:web:gecko:sourcemaps
  ```

  Same as for the webkit build, but for the gecko build.

- For the Safari build: not implemented yet.

For more details, including how to trace /deminify a production reported error, see [#3191](https://github.com/AmbireTech/ambire-app/pull/3191).

### Store-prepared Builds

Automates the steps before every extension extension store release that could be otherwise done manually:

- Makes webkit and gecko extension production builds
- Exports source maps to "clean" the builds (and to prepare for upload those source maps in the GitHub release)
- Zips the "clean" builds (stores accept zips only) and the source maps

```bash
yarn build:extensions
```

And find the resulting zips in the "build" folder as `ambire-extension-<VERSION>-<TYPE>.zip`

### Verifying a Downloaded Release

Releases live at [AmbireTech/extension/releases](https://github.com/AmbireTech/extension/releases). Installing from the [official download page](https://www.ambire.com/get-extension) is the recommended way, because the stores handle signing and updates for you. If you install a `.zip` by hand instead, verify it first.

Applies to **v6.19.2 and later**.

#### Check the signature (recommended)

GitHub signs every release and everything attached to it, so this proves the file is exactly what we published and that nobody changed it afterwards. Needs [GitHub CLI](https://cli.github.com/) 2.81 or newer:

```bash
gh release verify-asset v6.19.2 ./ambire-extension-v6.19.2-webkit.zip -R AmbireTech/extension
```

Success looks like `✓ Verification succeeded!`. Anything else means the file does not match the release - do not install it.

#### Or check the hash

If you would rather not install anything, download the `SHA256SUMS` file from the same release, put it next to the `.zip` files, and run:

```bash
sha256sum -c SHA256SUMS --ignore-missing   # macOS: shasum -a 256 -c SHA256SUMS --ignore-missing
```

Every file must print `OK`. This catches a corrupted or swapped download, but only the signature check above proves the file came from us.

Releases before v6.19.2 have neither a signature nor a `SHA256SUMS` file.

## Mobile Apps

The mobile apps share the same codebase, but the business logic (the `background`) runs inside a WebView worker (`src/mobile/modules/webview/services/`) instead of a service worker. That's why every mobile build needs the webview bundle built (or the webview dev server running).

### Install

- For iOS: Make sure you have Xcode + CocoaPods via bundler (see the "Environment Setup" section), then install the pods:

  ```bash
  cd ios && bundle install && bundle exec pod install
  ```

- For Android: Make sure you have Android Studio with the Android SDK and the NDK required by React Native (see "Environment Setup" section).

### Development-optimized Builds

Run the webview dev server in one terminal (the app shows an explicit error screen if it isn't running):

```bash
yarn dev:webview
```

Then, in another terminal, compile a new native build and run it on a simulator/emulator or a connected device:

```bash
yarn ios
# or
yarn android
```

These recompile the native app every time, which is slow. If the app is already installed, only the Metro bundler is needed - start it with a cleared cache and launch the app from the device:

```bash
yarn start:clean
```

A new native build is only needed after changing native code or native dependencies.

#### Webview dev server

It listens on port `8182` and is separate from the Metro bundler (port `8081`), which `yarn ios`/`yarn android` start on their own. The app resolves its host automatically:

| Target           | Host                           |
| ---------------- | ------------------------------ |
| iOS simulator    | `localhost`                    |
| Android emulator | `10.0.2.2`                     |
| Physical device  | `WEBVIEW_DEV_HOST` from `.env` |

On a physical device, set `WEBVIEW_DEV_HOST` to the LAN IP of the machine running the dev server and keep both on the same network.

The error screen prints the exact URL the app expects. The app also keeps re-probing the server and remounts the webview by itself once it is back up, so starting the dev server late doesn't require restarting the app.

### Production-optimized Builds

Both platforms run `yarn build:inject:mobile-ota-config` (seeds the Stallion OTA config into `Info.plist`/`strings.xml`) and `yarn build:webview` before the native build, so no manual prep is needed.

Local production builds are normally **not** OTA-capable: without the `STALLION_*` variables in ".env" the injection is skipped, the committed placeholders stay, and the app never pulls an OTA update. That is fine for testing. Fill them in (see "Over-the-Air (OTA) Updates") only if you specifically need to test the OTA flow locally. In CI they are mandatory - a missing one fails the build instead of shipping an app that silently cannot update.

- iOS, for a simulator (unsigned `.app`, useful for sharing test builds):

  ```bash
  yarn build:ios:simulator
  ```

  Find the result in "ios/build/Build/Products/Release-iphonesimulator/Ambire.app", and install it on the booted simulator with:

  ```bash
  yarn build:ios:simulator:install
  ```

- iOS, for the App Store (signed `.ipa`):

  ```bash
  yarn build:ios:production
  ```

  This archives the app and exports it with "ios/ExportOptions.plist". Find the result in the "ios/build/ipa" folder.

  Requires the Ambire distribution certificate in your keychain and the matching provisioning profile installed.

  For an ad-hoc/development `.ipa` (installable on registered test devices) use `yarn build:ios:production-for-testing`, which exports with "ios/ExportOptions-Development.plist" into "ios/build/ipa-for-testing".

- Android, APK (for testing, easiest to install directly on a device):

  ```bash
  yarn build:android:production:apk
  ```

  Find the result in the "android/app/build/outputs/apk/release" folder. To build, reinstall and restart on a connected device in one go:

  ```bash
  yarn build:android:production:apk:install
  ```

- Android, AAB (for the Play Store):

  ```bash
  yarn build:android:production:aab
  ```

  Find the result in the "android/app/build/outputs/bundle/release" folder.

  NOTE: Locally, release builds are signed with the debug keystore unless a "credentials.json" file with the release keystore details exists in the root directory. That's fine for testing, but a Play Store upload requires the real upload keystore, so use the CI build for store releases.

### CI Builds (GitHub Actions)

Store-ready artifacts are built in CI, so nobody has to keep signing material locally. All four are manually triggered (`workflow_dispatch`) and upload a zipped artifact named `ambire-<platform>-v<VERSION>-<TYPE>`, where the version is read from "app.json":

| Workflow                      | Yarn command                        | Artifact                     | Signed |
| ----------------------------- | ----------------------------------- | ---------------------------- | ------ |
| 🍎 Build · iOS Simulator      | `yarn build:ios:simulator`          | `Ambire.app`                 | No     |
| 🍎 Build · iOS App Store      | `yarn build:ios:production`         | `Ambire.ipa`                 | Yes    |
| 🤖 Build · Android APK        | `yarn build:android:production:apk` | `Ambire.apk` (arm64-v8a)     | No     |
| 🤖 Build · Android Play Store | `yarn build:android:production:aab` | `Ambire.aab` (+ armeabi-v7a) | Yes    |

The shared steps live in `.github/workflows/_build-ios.yml` and `.github/workflows/_build-android.yml`. The signing material (Apple certificate and provisioning profile, Android upload keystore), the Stallion OTA credentials and all API keys come from the GitHub environment.

### Over-the-Air (OTA) Updates

JS-only changes can be shipped to already installed apps without a store release, via [Stallion](https://stalliontech.io/). Both the React Native bundle and the webview worker bundle (the `background`) ride the OTA, so the core business logic can be updated too.

A build can only receive OTA updates if it was made with the Stallion credentials in place: `yarn build:inject:mobile-ota-config` swaps the placeholders in "Info.plist"/"strings.xml" for `STALLION_PROJECT_ID`, `STALLION_APP_TOKEN` and `STALLION_PUBLIC_SIGNING_KEY`. CI always has them, a local ".env" usually doesn't.

NOTE: that injection rewrites the committed "Info.plist" and "strings.xml" in place. Never commit the result - restore them with `git checkout` first.

OTA bundles are signed (RS256), so a tampered bundle cannot reach a device: the app verifies every incoming bundle against the `STALLION_PUBLIC_SIGNING_KEY` embedded into it at build time.

Once an OTA is downloaded, the app shows an "Update Available" banner. The active OTA version and build are listed in Settings - About.

#### Two copies of the webview worker bundle

Every build has the webview worker bundle (the `background`) baked into the app binary. An OTA can only replace JS, never a file inside the binary, so that copy on its own would keep the wallet's core logic frozen at whatever the store build shipped.

That is why the same bundle now travels inside the OTA JS bundle as well. On the first launch after an install or an update, the app writes it out into its own private folder and the WebView loads it from there via `file://`; later launches reuse what is already on disk. If that write ever fails, the app falls back to the copy baked into the binary, so it always has a working bundle to boot from.

Loading from disk keeps the protections the baked-in copy had: the page may only run scripts from `file://` (CSP), and its HTML carries a SHA-384 hash (SRI) pinning the exact JS file it loads, so the two can never drift apart. That hash only proves the HTML and the JS belong together, though - what makes OTA'd code trustworthy in the first place is the signature check above.

## Explorer (Old name: Benzin)

Ambire's transaction explorer, that makes human readable ERC-4337 transactions and contract interactions.

Comes not only as integrated module in the Ambire extension(s), but as a standalone web app also.

### Development-optimized Build

```bash
yarn web:benzin
```

And find the resulting build in the "build/benzin-dev" folder.

### Production-optimized Build

```bash
yarn build:web:benzin
```

And find the resulting build in the "build/benzin-prod" folder.

## Ambire Rewards

Ambire Rewards is a gamified testing web3 app for the Ambire browser extensions. It is designed to users you discover the power of Smart Accounts via an epic onchain adventure. [Read more](https://rewards.ambire.com/).

### Development-optimized Build

```bash
yarn web:legends
```

And find the resulting build in the "build/legends-dev" folder.

```bash
yarn build:web:legends
```

And find the resulting build in the "build/legends-prod" folder.

## Others

### Starting the Ledger Emulator Locally

You can run the Ledger emulator locally for testing purposes. Make sure **Docker** is installed on your machine before proceeding.

#### Steps

1. **Navigate to the emulator folder**:

```bash
cd e2e-playwright-tests/ledger-emulator
```

2. **Start the emulator**:

```bash
$LEDGER_EMULATOR_SEED='<LEDGER-SEED-PHRASE>' ./start-emulator.sh
```

**Note:** Make sure port `5000` is available before starting the emulator.

1. **Check if port 5000 is in use:**

```bash
lsof -i :5000
```

If nothing is returned, the port is free.
If you see a process listed, the port is occupied.

2. **macOS specific context**

On macOS, port 5000 is commonly taken by AirPlay Receiver (enabled by default on newer macOS versions).
To check:

System Settings → General → AirDrop & Handoff → AirPlay Receiver

If enabled, it may bind to port 5000.

You can either:

- Disable AirPlay Receiver, or
- Kill the process manually:

```bash
kill -9 $(lsof -t -i :5000)
```

### Browser Extensions E2E Tests

#### Configuration

We've migrated from Puppeteer to Playwright (./e2e-playwright-tests/). Documentation will follow soon.


---

## 87. vitest
- **URL:** https://github.com/devtechedge/vitest
- **Language:** TypeScript
- **Topics:** None
- **Description:** Next generation testing framework powered by Vite.

### README.md

<p align="center">
  <br>
  <br>
  <a href="https://vitest.dev" target="_blank" rel="noopener noreferrer">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://vitest.dev/vitest-light.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://vitest.dev/vitest-dark.svg">
      <img alt="Vitest logo" src="https://vitest.dev/vitest-dark.svg" height="60">
    </picture>
  </a>
  <br>
  <br>
  <br>
</p>

<h1 align="center">
Vitest
</h1>
<p align="center">
Next generation testing framework powered by Vite.
<p>
<p align="center">
  <a href="https://npmx.dev/package/vitest"><img src="https://img.shields.io/npm/v/vitest?color=729B1B&label=" alt="current vitest version badge"></a>
<p>

<p align="center">
<a href="https://chat.vitest.dev"><b>Get involved!</b></a>
</p>
<p align="center">
 <a href="https://vitest.dev">Documentation</a> | <a href="https://vitest.dev/guide/">Getting Started</a> | <a href="https://vitest.dev/guide/#examples">Examples</a> | <a href="https://vitest.dev/guide/why">Why Vitest?</a>
</p>
<p align="center">
<a href="https://cn.vitest.dev">中文文档</a>
</p>

<h4 align="center">

</h4>
<br>
<br>

## Features

- [Vite](https://vitejs.dev/)'s config, transformers, resolvers, and plugins. Use the same setup from your app!
- [Jest Snapshot](https://jestjs.io/docs/snapshot-testing)
- [Chai](https://www.chaijs.com/) built-in for assertions, with [Jest expect](https://jestjs.io/docs/expect) compatible APIs
- [Smart & instant watch mode](https://vitest.dev/guide/features.html#watch-mode), like HMR for tests!
- [Native code coverage](https://vitest.dev/guide/features.html#coverage) via [`v8`](https://v8.dev/blog/javascript-code-coverage) or [`istanbul`](https://istanbul.js.org/).
- Jest-compatible mocking, stubbing, and spies.
- [JSDOM](https://github.com/jsdom/jsdom) and [happy-dom](https://github.com/capricorn86/happy-dom) for DOM and browser API mocking
- [Browser Mode](https://vitest.dev/guide/browser/) for running component tests in the browser
- Components testing ([Vue](https://github.com/vitest-tests/browser-examples/tree/main/examples/vue), [React](https://github.com/vitest-tests/browser-examples/tree/main/examples/react), [Svelte](https://github.com/vitest-tests/browser-examples/tree/main/examples/svelte), [Lit](./examples/lit), [Marko](https://github.com/marko-js/examples/tree/master/examples/library-ts))
- Benchmarking support with [Tinybench](https://github.com/tinylibs/tinybench)
- [Projects](https://vitest.dev/guide/projects) support
- [expect-type](https://github.com/mmkal/expect-type) for type-level testing
- ESM first, top level await
- Out-of-box TypeScript / JSX support
- Filtering, timeouts, concurrent for suite and tests
- Sharding support
- Reporting Uncaught Errors
- Run your tests in the browser natively

> Vitest requires Vite >=v6.4.0 and Node >=v22.12.0

```ts
import { assert, describe, expect, it } from 'vitest'

describe('suite name', () => {
  it('foo', () => {
    expect(1 + 1).toEqual(2)
    expect(true).to.be.true
  })

  it('bar', () => {
    assert.equal(Math.sqrt(4), 2)
  })

  it('snapshot', () => {
    expect({ foo: 'bar' }).toMatchSnapshot()
  })
})
```

```bash
$ npx vitest
```

## Sponsors

<p align="center">
  <a href="https://cdn.jsdelivr.net/gh/sheremet-va/static/vitest/sponsors.svg">
    <img src='https://cdn.jsdelivr.net/gh/sheremet-va/static/vitest/sponsors.svg' alt="vitest's sponsors"/>
  </a>
</p>

## Credits

Thanks to:

- [The Jest team and community](https://jestjs.io/) for creating a delightful testing API
- [@lukeed](https://github.com/lukeed) for the work on [uvu](https://github.com/lukeed/uvu) where we are inspired a lot from.
- [@pi0](https://github.com/pi0) for the idea and implementation of using Vite to transform and bundle the server code.
- [The Vite team](https://github.com/vitejs/vite) for brainstorming the initial idea.
- [@patak-dev](https://github.com/patak-dev) for the awesome package name!

## Contribution

See [Contributing Guide](https://github.com/vitest-dev/vitest/blob/main/CONTRIBUTING.md).

## License

[MIT](./LICENSE) License © 2021-Present VoidZero Inc. and Vitest contributors


---

## 88. langgraphjs
- **URL:** https://github.com/devtechedge/langgraphjs
- **Language:** TypeScript
- **Topics:** None
- **Description:** Framework to build resilient language agents as graphs.

### README.md

<div align="center">
  <a href="https://www.langchain.com/langgraph">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/langchain-ai/langgraphjs/HEAD/.github/images/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/langchain-ai/langgraphjs/HEAD/.github/images/logo-light.svg">
      <img alt="LangGraph Logo" src="https://raw.githubusercontent.com/langchain-ai/langgraphjs/HEAD/.github/images/logo-dark.svg" width="50%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>Low-level orchestration framework for building stateful agents.</h3>
</div>

<div align="center">
  <a href="https://docs.langchain.com/oss/javascript/langgraph/overview" target="_blank"><img src="https://img.shields.io/badge/docs-latest-blue" alt="Docs"></a>
  <a href="https://www.npmjs.com/package/@langchain/langgraph" target="_blank"><img src="https://img.shields.io/npm/v/@langchain/langgraph?logo=npm" alt="Version"></a>
  <a href="https://www.npmjs.com/package/@langchain/langgraph" target="_blank"><img src="https://img.shields.io/npm/dm/@langchain/langgraph" alt="npm - Downloads"></a>
  <a href="https://github.com/langchain-ai/langgraphjs/issues" target="_blank"><img src="https://img.shields.io/github/issues-raw/langchain-ai/langgraphjs" alt="Open Issues"></a>
</div>

LangGraph — used by Replit, Uber, LinkedIn, GitLab and more — is a low-level orchestration framework for building controllable agents. While langchain provides integrations and composable components to streamline LLM application development, the LangGraph library enables agent orchestration — offering customizable architectures, long-term memory, and human-in-the-loop to reliably handle complex tasks.

```bash
npm install @langchain/langgraph @langchain/core
```

> [!TIP]
> If you're looking to quickly build agents, check out **[Deep Agents](https://docs.langchain.com/oss/javascript/deepagents/overview)** — a higher-level package built on LangGraph for agents that can plan, use subagents, and leverage file systems for complex tasks.

For an equivalent Python library, check out [LangGraph](https://github.com/langchain-ai/langgraph) and the [Python docs](https://docs.langchain.com/oss/python/langgraph/overview).

## Why use LangGraph?

LangGraph provides low-level supporting infrastructure for *any* long-running, stateful workflow or agent:

- **[Durable execution](https://docs.langchain.com/oss/javascript/langgraph/durable-execution)** — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off.
- **[Human-in-the-loop](https://docs.langchain.com/oss/javascript/langgraph/interrupts)** — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution.
- **[Comprehensive memory](https://docs.langchain.com/oss/javascript/langgraph/memory)** — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions.
- **[Debugging with LangSmith](https://www.langchain.com/langsmith)** — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
- **[Production-ready deployment](https://docs.langchain.com/langsmith/deployments)** — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.

> [!TIP]
> For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home).

## LangGraph’s ecosystem

While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with:

- [Deep Agents (JS)](https://docs.langchain.com/oss/javascript/deepagents/overview) — Build agents that can plan, use subagents, and leverage file systems for complex tasks. A higher-level package built on top of LangGraph.
- [LangChain](https://docs.langchain.com/oss/javascript/langchain/overview) – Provides integrations and composable components to streamline LLM application development.
- [LangSmith](http://www.langchain.com/langsmith) — Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time.

## Additional resources

- [LangChain Forum](https://forum.langchain.com/): Connect with the community and share all of your technical questions, ideas, and feedback.
- [LangChain Academy](https://academy.langchain.com/courses/intro-to-langgraph): Learn the basics of LangGraph in our free, structured course.
- [Streaming Cookbook](https://github.com/langchain-ai/streaming-cookbook): Documentation and examples around LangGraphs's streaming capabilities.
- [API Reference](https://reference.langchain.com/javascript/langchain-langgraph): Detailed reference on core classes, methods, how to use the graph and checkpointing APIs, and higher-level prebuilt components.
- [Built with LangGraph](https://www.langchain.com/built-with-langgraph): Hear how industry leaders use LangGraph to ship powerful, production-ready AI applications.

## Acknowledgements

LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.


---

## 89. appkit
- **URL:** https://github.com/devtechedge/appkit
- **Language:** TypeScript
- **Topics:** None
- **Description:** The full stack toolkit to build onchain app UX

### README.md

# AppKit

The full stack toolkit to build onchain app UX.

Onboard millions of users to your app in minutes with social & email embedded wallets, web3 wallet login, crypto swaps, on-ramp and more.

🛝 [Demo](https://demo.reown.com) ・🧪 [Laboratory](https://appkit-lab.reown.com) ・📚 [Documentation](https://docs.reown.com/appkit/overview) ・💻 [AppKit Web Examples](https://github.com/reown-com/appkit-web-examples) ・🔗 [Website](https://reown.com/appkit) ・🛟 [Contact us on Discord](https://discord.gg/reown)

<p align="center">
  <img src="https://github.com/reown-com/appkit/blob/HEAD/.github/assets/header.png" alt="" border="0">
</p>

## Features

Refer to the "Features" section of the [AppKit docs](https://docs.reown.com/appkit/features).

- Swaps
- On-Ramp
- Multi Chain
- Multi Wallets
- Smart Accounts
- Telegram Mini Apps
- Sponsored Transactions
- Networks: EVM Chains, Solana, Bitcoin
- AppKit Core: Chain Agnostic
- Authentication: Email & Social Login, One-Click Auth & Sign with X (SIWX)

## AppKit Available SDKs

- [React](https://docs.reown.com/appkit/react/core/installation)
- [Next](https://docs.reown.com/appkit/next/core/installation)
- [Vue](https://docs.reown.com/appkit/vue/core/installation)
- [Nuxt](https://docs.reown.com/appkit/nuxt/core/installation)
- [Svelte](https://docs.reown.com/appkit/svelte/core/installation)
- [Javascript](https://docs.reown.com/appkit/javascript/core/installation)
- [React Native](https://docs.reown.com/appkit/react-native/core/installation)
- [Flutter](https://docs.reown.com/appkit/flutter/core/installation)
- [Android](https://docs.reown.com/appkit/android/core/installation)
- [iOS](https://docs.reown.com/appkit/ios/core/installation)
- [Unity](https://docs.reown.com/appkit/unity/core/installation)

> [!NOTE]
> If you are using Web3Modal v1–v5, please use our [migration guides](https://docs.reown.com/appkit/upgrade/to-reown-appkit-web#migrate-from-web3modal-v5-to-reown-appkit).

## License and Use

This SDK is provided under the **[Reown AppKit] Community License** (“Community License”), that governs, among other things:

- Permitted non-commercial use
- RPC and MAU thresholds for commercial licensing
- Required connection to Reown's proprietary infrastructure
- Redistribution and attribution obligations
- Ownership of modifications
- Mandatory binding arbitration for disputes

**Downloading, installation, integration and use of this SDK constitutes acceptance of the [Reown AppKit Community License](./LICENSE.md).**


---

## 90. rainbowkit
- **URL:** https://github.com/devtechedge/rainbowkit
- **Language:** MDX
- **Topics:** None
- **Description:** The best way to connect a wallet ≡ƒîê ≡ƒº░

### README.md

<a href="https://rainbowkit.com">
  <img alt="rainbowkit" src="https://user-images.githubusercontent.com/372831/168174718-685980e0-391e-4621-94a1-29bf83979fa5.png" />
</a>

# RainbowKit &nbsp; [![Version](https://img.shields.io/npm/v/@rainbow-me/rainbowkit?colorA=1f2937&colorB=3b82f6&labelColor=1f2937)](https://www.npmjs.com/package/@rainbow-me/rainbowkit) [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/rainbow-me/rainbowkit)

**The best way to connect a wallet 🌈**

RainbowKit is a [React](https://reactjs.org/) library that makes it easy to add wallet connection to your dapp.

- 🔥 Out-of-the-box wallet management
- ✅ Easily customizable
- 🦄 Built on top of [wagmi](https://wagmi.sh) and [viem](https://viem.sh)

## Quick start

You can scaffold a new RainbowKit + [wagmi](https://wagmi.sh) + [Next.js](https://nextjs.org) app with one of the following commands, using your package manager of choice:

```bash
npm init @rainbow-me/rainbowkit@latest
# or
pnpm create @rainbow-me/rainbowkit@latest
# or
yarn create @rainbow-me/rainbowkit
```

## Documentation

For full documentation, visit [rainbowkit.com](https://rainbowkit.com).

### Try it out

You can use the CodeSandbox links below to try out RainbowKit:

- with [Create React App](https://codesandbox.io/p/sandbox/github/rainbow-me/rainbowkit/tree/main/examples/with-create-react-app)
- with [Next.js](https://codesandbox.io/p/sandbox/github/rainbow-me/rainbowkit/tree/main/examples/with-next)
- with [Next.js App Router](https://codesandbox.io/p/sandbox/github/rainbow-me/rainbowkit/tree/main/examples/with-next-app)
- with [Remix](https://codesandbox.io/p/sandbox/github/rainbow-me/rainbowkit/tree/main/examples/with-remix)
- with [Vite](https://codesandbox.io/p/sandbox/github/rainbow-me/rainbowkit/tree/main/examples/with-vite)
- with [React Router](https://codesandbox.io/p/sandbox/github/rainbow-me/rainbowkit/tree/main/examples/with-react-router)

## Examples

The following examples are provided in the [examples](./examples/) folder of this repo.

- `with-create-react-app`
- `with-next`
- `with-next-app`
- `with-next-custom-button`
- `with-next-mint-nft`
- `with-next-siwe-next-auth`
- `with-next-siwe-iron-session`
- `with-remix`
- `with-vite`
- `with-react-router`

### Running examples

To run an example locally, install dependencies.

```bash
pnpm install
```

Then go into an example directory, eg: `with-next`.

```bash
cd examples/with-next
```

Then run the dev script.

```bash
pnpm run dev
```

## Contributing

Please follow our [contributing guidelines](/.github/CONTRIBUTING.md).

## License

Licensed under the MIT License, Copyright © 2022-present [Rainbow](https://rainbow.me).

See [LICENSE](/LICENSE) for more information.


---

## 91. wagmi
- **URL:** https://github.com/devtechedge/wagmi
- **Language:** TypeScript
- **Topics:** None
- **Description:** Reactive primitives for Ethereum apps

### README.md

<!-- > [!IMPORTANT] -->
<!-- > Wagmi is participating in Gitcoin Grants round 21. Consider <a href="https://explorer.gitcoin.co/#/round/42161/389/74">supporting the project</a>. Thank you. 🙏 -->

<br>

<p align="center">
  <a href="https://wagmi.sh">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/wagmi/main/.github/logo-dark.svg">
      <img alt="wagmi logo" src="https://raw.githubusercontent.com/wevm/wagmi/main/.github/logo-light.svg" width="auto" height="60">
    </picture>
  </a>
</p>

<p align="center">
  Reactive primitives for Ethereum apps
<p>

<p align="center">
  <a href="https://www.npmjs.com/package/wagmi">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/v/wagmi?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/npm/v/wagmi?colorA=f6f8fa&colorB=f6f8fa" alt="Version">
    </picture>
  </a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/ossf/scorecard">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/ossf-scorecard/github.com/wevm/wagmi?label=openssf+scorecard&style=flat&color=21262d&labelColor=21262d">
      <img src="https://img.shields.io/ossf-scorecard/github.com/wevm/wagmi?label=openssf+scorecard&style=flat&color=f6f8fa&labelColor=f6f8fa" alt="OpenSSF Best Practices">
    </picture>
  </a>
  <a href="https://www.bestpractices.dev/en/projects/11233">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/openssf_best_practices-passing-21262d?labelColor=21262d">
      <img src="https://img.shields.io/badge/openssf_best_practices-passing-f6f8fa?labelColor=f6f8fa" alt="OpenSSF Best Practices">
    </picture>
  </a>
  <br />
  <a href="https://github.com/wevm/wagmi/blob/main/LICENSE">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/l/wagmi?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/npm/l/wagmi?colorA=f6f8fa&colorB=f6f8fa" alt="MIT License">
    </picture>
  </a>
  <a href="https://www.npmjs.com/package/wagmi">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/npm/dm/@wagmi/core?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/npm/dm/@wagmi/core?colorA=f6f8fa&colorB=f6f8fa" alt="Downloads per month">
    </picture>
  </a>
  <a href="https://bestofjs.org/projects/wagmi">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/endpoint?colorA=21262d&colorB=21262d&url=https://bestofjs-serverless.now.sh/api/project-badge?fullName=wevm%2Fviem%26since=daily">
      <img src="https://img.shields.io/endpoint?colorA=f6f8fa&colorB=f6f8fa&url=https://bestofjs-serverless.now.sh/api/project-badge?fullName=wevm%2Fviem%26since=daily" alt="Best of JS">
    </picture>
  </a>
  <a href="https://app.codecov.io/gh/wevm/wagmi">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/codecov/c/github/wevm/wagmi?colorA=21262d&colorB=21262d">
      <img src="https://img.shields.io/codecov/c/github/wevm/wagmi?colorA=f6f8fa&colorB=f6f8fa" alt="Code coverage">
    </picture>
  </a>
</p>

---

## Documentation

For documentation and guides, visit [wagmi.sh](https://wagmi.sh).

## Community

For help, discussion about best practices, or any other conversation that would benefit from being searchable:

[Discuss Wagmi on GitHub](https://github.com/wevm/wagmi/discussions)

For casual chit-chat with others using the framework:

[Join the Wagmi Discord](https://discord.gg/SghfWBKexF)

## Contributing

Contributions to Wagmi are greatly appreciated! If you're interested in contributing to Wagmi, please read the [Contributing Guide](https://wagmi.sh/dev/contributing) **before submitting a pull request**.

## Sponsors

If you find Wagmi useful or use it for work, please consider [sponsoring Wagmi](https://github.com/sponsors/wevm?metadata_campaign=gh_readme_support). Thank you 🙏

<p>
  <a href="https://paradigm.xyz">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/paradigm-dark.svg">
      <img alt="paradigm logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/paradigm-light.svg" width="auto" height="70">
    </picture>
  </a>
  <a href="https://tempo.xyz">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/tempo-dark.svg">
      <img alt="tempo logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/tempo-light.svg" width="auto" height="70">
    </picture>
  </a>
</p>

<p>
  <a href="https://twitter.com/family">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/family-dark.svg">
      <img alt="family logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/family-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://twitter.com/context">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/context-dark.svg">
      <img alt="context logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/context-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://dynamic.xyz">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/dynamic-dark.svg">
      <img alt="Dynamic logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/dynamic-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://sushi.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sushi-dark.svg">
      <img alt="Sushi logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sushi-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://stripe.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/stripe-dark.svg">
      <img alt="Stripe logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/stripe-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://www.privy.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/privy-dark.svg">
      <img alt="Privy logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/privy-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://pancakeswap.finance">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pancake-dark.svg">
      <img alt="pancake logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pancake-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://pimlico.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pimlico-dark.svg">
      <img alt="pimlico logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/pimlico-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://zora.co">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/zora-dark.svg">
      <img alt="zora logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/zora-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://syndicate.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/syndicate-dark.svg">
      <img alt="syndicate logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/syndicate-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://relay.link">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/relay-dark.svg">
      <img alt="relay logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/relay-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://polymarket.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/polymarket-dark.svg">
      <img alt="polymarket logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/polymarket-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://sequence.xyz">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sequence-dark.svg">
      <img alt="sequence logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/sequence-light.svg" width="auto" height="50">
    </picture>
  </a>
  <a href="https://web3auth.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/web3auth-dark.svg">
      <img alt="web3auth logo" src="https://raw.githubusercontent.com/wevm/.github/main/content/sponsors/web3auth-light.svg" width="auto" height="50">
    </picture>
  </a>
</p>

[Sponsor Wagmi](https://github.com/sponsors/wevm?metadata_campaign=gh_readme_support_bottom)

<br />
<br />

<a href="https://vercel.com/?utm_source=wevm&utm_campaign=oss">
  <img src="https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg" alt="Powered by Vercel" height="35">
</a>




---

## 92. ethers.js
- **URL:** https://github.com/devtechedge/ethers.js
- **Language:** TypeScript
- **Topics:** None
- **Description:** Complete Ethereum library and wallet implementation in JavaScript.

### README.md

The Ethers Project
==================

[![npm (tag)](https://img.shields.io/npm/v/ethers)](https://www.npmjs.com/package/ethers)
[![CI Tests](https://github.com/ethers-io/ethers.js/actions/workflows/test-ci.yml/badge.svg?branch=main)](https://github.com/ethers-io/ethers.js/actions/workflows/test-ci.yml)
![npm bundle size (version)](https://img.shields.io/bundlephobia/minzip/ethers)
![npm (downloads)](https://img.shields.io/npm/dm/ethers)
[![GitPOAP Badge](https://public-api.gitpoap.io/v1/repo/ethers-io/ethers.js/badge)](https://www.gitpoap.io/gh/ethers-io/ethers.js)
[![Twitter Follow](https://img.shields.io/twitter/follow/ricmoo?style=social)](https://twitter.com/ricmoo)

-----

A complete, compact and simple library for Ethereum and ilk, written
in [TypeScript](https://www.typescriptlang.org).

**Features**

- Keep your private keys in your client, **safe** and sound
- Import and export **JSON wallets** (Geth, Parity and crowdsale)
- Import and export BIP 39 **mnemonic phrases** (12 word backup phrases) and **HD Wallets** (English as well as Czech, French, Italian, Japanese, Korean, Simplified Chinese, Spanish, Traditional Chinese)
- Meta-classes create JavaScript objects from any contract ABI, including **ABIv2** and **Human-Readable ABI**
- Connect to Ethereum nodes over [JSON-RPC](https://ethereum.org/en/developers/docs/apis/json-rpc/), [INFURA](https://infura.io), [Etherscan](https://etherscan.io), [Alchemy](https://alchemyapi.io), [Ankr](https://ankr.com) or [MetaMask](https://metamask.io)
- **ENS names** are first-class citizens; they can be used anywhere an Ethereum addresses can be used
- **Small** (~144kb compressed; 460kb uncompressed)
- **Tree-shaking** focused; include only what you need during bundling
- **Complete** functionality for all your Ethereum desires
- Extensive [documentation](https://docs.ethers.org/v6/)
- Large collection of **test cases** which are maintained and added to
- Fully written in **TypeScript**, with strict types for security and safety
- **MIT License** (including ALL dependencies); completely open source to do with as you please


Keep Updated
------------

For advisories and important notices, follow [@ethersproject](https://twitter.com/ethersproject)
on Twitter (low-traffic, non-marketing, important information only) as well as watch this GitHub project.

For more general news, discussions, and feedback, follow or DM me,
[@ricmoo](https://twitter.com/ricmoo) on Twitter or on the
[Ethers Discord](https://discord.gg/qYtSscGYYc).


For the latest changes, see the
[CHANGELOG](https://github.com/ethers-io/ethers.js/blob/main/CHANGELOG.md).


**Summaries**

- [August 2023](https://blog.ricmoo.com/highlights-ethers-js-august-2023-fb68354c576c)
- [September 2022](https://blog.ricmoo.com/highlights-ethers-js-september-2022-d7bda0fc37ed)
- [June 2022](https://blog.ricmoo.com/highlights-ethers-js-june-2022-f5328932e35d)
- [March 2022](https://blog.ricmoo.com/highlights-ethers-js-march-2022-f511fe1e88a1)
- [December 2021](https://blog.ricmoo.com/highlights-ethers-js-december-2021-dc1adb779d1a)
- [September 2021](https://blog.ricmoo.com/highlights-ethers-js-september-2021-1bf7cb47d348)
- [May 2021](https://blog.ricmoo.com/highlights-ethers-js-may-2021-2826e858277d)
- [March 2021](https://blog.ricmoo.com/highlights-ethers-js-march-2021-173d3a545b8d)
- [December 2020](https://blog.ricmoo.com/highlights-ethers-js-december-2020-2e2db8bc800a)



Installing
----------

**NodeJS**

```
/home/ricmoo/some_project> npm install ethers
```

**Browser (ESM)**

The bundled library is available in the `./dist/` folder in this repo.

```
<script type="module">
    import { ethers } from "./dist/ethers.min.js";
</script>
```


Documentation
-------------

Browse the [documentation](https://docs.ethers.org) online:

- [Getting Started](https://docs.ethers.org/v6/getting-started/)
- [Full API Documentation](https://docs.ethers.org/v6/api/)
- [Various Ethereum Articles](https://blog.ricmoo.com/)



Providers
---------

Ethers works closely with an ever-growing list of third-party providers
to ensure getting started is quick and easy, by providing default keys
to each service.

These built-in keys mean you can use `ethers.getDefaultProvider()` and
start developing right away.

However, the API keys provided to ethers are also shared and are
intentionally throttled to encourage developers to eventually get
their own keys, which unlock many other features, such as faster
responses, more capacity, analytics and other features like archival
data.

When you are ready to sign up and start using for your own keys, please
check out the [Provider API Keys](https://docs.ethers.org/v5/api-keys/) in
the documentation.

A special thanks to these services for providing community resources:

- [Ankr](https://www.ankr.com/)
- [QuickNode](https://www.quicknode.com/)
- [Etherscan](https://etherscan.io/)
- [INFURA](https://infura.io/)
- [Alchemy](https://dashboard.alchemyapi.io/signup?referral=55a35117-028e-4b7c-9e47-e275ad0acc6d)


Extension Packages
------------------

The `ethers` package only includes the most common and most core
functionality to interact with Ethereum. There are many other
packages designed to further enhance the functionality and experience.

- [MulticallProvider](https://github.com/ethers-io/ext-provider-multicall) - A Provider which bundles multiple call requests into a single `call` to reduce latency and backend request capacity
- [MulticoinPlugin](https://github.com/ethers-io/ext-provider-plugin-multicoin) - A Provider plugin to expand the support of ENS coin types
- [GanaceProvider](https://github.com/ethers-io/ext-provider-ganache) - A Provider for in-memory node instances, for fast debugging, testing and simulating blockchain operations
- [Optimism Utilities](https://github.com/ethers-io/ext-utils-optimism) - A collection of Optimism utilities
- [LedgerSigner](https://github.com/ethers-io/ext-signer-ledger) - A Signer to interact directly with Ledger Hardware Wallets


License
-------

MIT License (including **all** dependencies).



---

## 93. solana-web3.js
- **URL:** https://github.com/devtechedge/solana-web3.js
- **Language:** TypeScript
- **Topics:** None
- **Description:** Solana JavaScript SDK

### README.md

[![npm][npm-image]][npm-url]
[![npm-downloads][npm-downloads-image]][npm-url]
[![semantic-release][semantic-release-image]][semantic-release-url]
<br />
[![code-style-prettier][code-style-prettier-image]][code-style-prettier-url]

[code-style-prettier-image]: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square
[code-style-prettier-url]: https://github.com/prettier/prettier
[npm-downloads-image]: https://img.shields.io/npm/dm/@solana/web3.js.svg?style=flat
[npm-image]: https://img.shields.io/npm/v/@solana/web3.js.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@solana/web3.js
[semantic-release-image]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg
[semantic-release-url]: https://github.com/semantic-release/semantic-release

> [!NOTE]
> This is the maintenance branch for the 1.x line of `@solana/web3.js`. You can find the successor to this library here: [`@solana/kit`](https://l.anza.xyz/s/js-sdk-repo).

# Solana JavaScript SDK (v1.x)

Use this to interact with accounts and programs on the Solana network through the Solana [JSON RPC API](https://solana.com/docs/rpc).

## Installation

### For use in Node.js or a web application

```
$ npm install --save @solana/web3.js
```

### For use in a browser, without a build system

```html
<!-- Development (un-minified) -->
<script src="https://unpkg.com/@solana/web3.js@latest/lib/index.iife.js"></script>

<!-- Production (minified) -->
<script src="https://unpkg.com/@solana/web3.js@latest/lib/index.iife.min.js"></script>
```

## Documentation and examples

- [The Solana Cookbook](https://solanacookbook.com/) has extensive task-based documentation using this library.
- For more detail on individual functions, see the [latest API Documentation](https://solana-foundation.github.io/solana-web3.js)

## Getting help

Have a question or a problem? Check the [Solana Stack Exchange](https://solana.stackexchange.com) to see if anyone else is having the same one. If not, [post a new question](https://solana.stackexchange.com/questions/ask).

Include:

- A detailed description of what you're trying to achieve
- Source code, if possible
- The text of any errors you encountered, with stacktraces if available

## Compatibility

This library requires a JavaScript runtime that supports [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt) and the [exponentiation operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation). Both are supported in the following runtimes:

- Browsers, by [release date](https://caniuse.com/bigint):
  - Chrome: May 2018
  - Firefox: July 2019
  - Safari: September 2020
  - Mobile Safari: September 2020
  - Edge: January 2020
  - Opera: June 2018
  - Samsung Internet: April 2019
- Runtimes, [by version](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt):
  - Deno: >=1.0
  - Node: >=10.4.0
- React Native:
  - \>=0.7.0 using the [Hermes](https://reactnative.dev/blog/2022/07/08/hermes-as-the-default) engine ([integration guide](https://solanacookbook.com/integrations/react-native.html#how-to-use-solana-web3-js-in-a-react-native-app)):

## Development environment setup

### Testing

#### Unit tests

To run the full suite of unit tests, execute the following in the root:

```shell
$ npm test
```

#### Integration tests

Integration tests require a validator client running on your machine.

To install a test validator:

```shell
$ npm run test:live-with-test-validator:setup
```

To start the test validator and run all of the integration tests in live mode:

```shell
$ cd packages/library-legacy
$ npm run test:live-with-test-validator
```

## Contributing

If you found a bug or would like to request a feature, please [file an issue](https://github.com/solana-foundation/solana-web3.js/issues/new). If, based on the discussion on an issue you would like to offer a code change, please make a [pull request](https://github.com/solana-foundation/solana-web3.js/compare). If neither of these describes what you would like to contribute, read the [getting help](#getting-help) section above.

## Disclaimer

All claims, content, designs, algorithms, estimates, roadmaps,
specifications, and performance measurements described in this project
are done with the Solana Foundation's ("SF") best efforts. It is up to
the reader to check and validate their accuracy and truthfulness.
Furthermore nothing in this project constitutes a solicitation for
investment.

Any content produced by SF or developer resources that SF provides, are
for educational and inspiration purposes only. SF does not encourage,
induce or sanction the deployment, integration or use of any such
applications (including the code comprising the Solana blockchain
protocol) in violation of applicable laws or regulations and hereby
prohibits any such deployment, integration or use. This includes use of
any such applications by the reader (a) in violation of export control
or sanctions laws of the United States or any other applicable
jurisdiction, (b) if the reader is located in or ordinarily resident in
a country or territory subject to comprehensive sanctions administered
by the U.S. Office of Foreign Assets Control (OFAC), or (c) if the
reader is or is working on behalf of a Specially Designated National
(SDN) or a person subject to similar blocking or denied party
prohibitions.

The reader should be aware that U.S. export control and sanctions laws
prohibit U.S. persons (and other persons that are subject to such laws)
from transacting with persons in certain countries and territories or
that are on the SDN list. As a project based primarily on open-source
software, it is possible that such sanctioned persons may nevertheless
bypass prohibitions, obtain the code comprising the Solana blockchain
protocol (or other project code or applications) and deploy, integrate,
or otherwise use it. Accordingly, there is a risk to individuals that
other persons using the Solana blockchain protocol may be sanctioned
persons and that transactions with such persons would be a violation of
U.S. export controls and sanctions law. This risk applies to
individuals, organizations, and other ecosystem participants that
deploy, integrate, or use the Solana blockchain protocol code directly
(e.g., as a node operator), and individuals that transact on the Solana
blockchain through light clients, third party interfaces, and/or wallet
software.


---


