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
<img src="https://github.com/anza-xyz.png?size=48" width="32" height="32" alt="Anza" align="left" /> **[Anza Kit #2032](https://github.com/anza-xyz/kit/pull/2032)** — corrected the `getPatternMatchCodec` advanced guide to match current codec typing.

<img src="https://github.com/better-auth.png?size=48" width="32" height="32" alt="Better Auth" align="left" /> **[Better Auth #11208](https://github.com/better-auth/better-auth/pull/11208)** — added regression coverage for missing OpenAPI `requestBody` generation after a Zod intersection.

<img src="https://github.com/biomejs.png?size=48" width="32" height="32" alt="Biome" align="left" /> **[Biome #11667](https://github.com/biomejs/biome/pull/11667)** — added the `useBetterDomTraversing` nursery lint rule with safe transformations where semantics permit.

<img src="https://cdn.simpleicons.org/node.js/339933" width="32" height="32" alt="Node.js" /> **[node-postgres #3772](https://github.com/brianc/node-postgres/pull/3772)** — fixed `Connection.sync()` incorrectly setting the internal `_ending` flag, preventing false suppression of subsequent socket errors.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14753](https://github.com/pnpm/pnpm/pull/14753)** — fixed `lockfile: false` being ignored during automatic package-manager switching.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14754](https://github.com/pnpm/pnpm/pull/14754)** — fixed non-recursive pattern runs with `--no-bail` so matching scripts continue executing and failures are aggregated correctly.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14756](https://github.com/pnpm/pnpm/pull/14756)** — preserved existing dependency range operators and protocol prefixes during `pnpm update`.

<img src="https://github.com/pnpm.png?size=48" width="32" height="32" alt="pnpm" align="left" /> **[pnpm #14863](https://github.com/pnpm/pnpm/pull/14863)** — fixed startup crashes on FreeBSD and other non-Windows Unix-like platforms by making default_store_dir use the Unix fallback path, with platform-specific regression coverage.

<img src="https://github.com/pytest-dev.png?size=48" width="32" height="32" alt="pytest-env" align="left" /> **[pytest-env #262](https://github.com/pytest-dev/pytest-env/pull/262)** — documented that pytest.toml and .pytest.toml accept the native [pytest] env table, not only the plugin-specific [pytest_env] section.

<img src="https://github.com/recharts.png?size=48" width="32" height="32" alt="Recharts" align="left" /> **[Recharts #7805](https://github.com/recharts/recharts/pull/7805)** — removed `tabIndex={-1}` from z-index portal SVG `<g>` layers so empty groups are not pointer-focusable and WebKit does not draw geometry-traced focus rings; added regression coverage asserting no layer carries a `tabindex` attribute.

<img src="https://github.com/web-infra-dev.png?size=48" width="32" height="32" alt="Rspress" align="left" /> **[Rspress #3678](https://github.com/web-infra-dev/rspress/pull/3678)** — fixed search initialization racing ahead of asynchronous FlexSearch indexing by awaiting all `addAsync()` operations before initialization resolves, preventing early queries from incorrectly returning no results on larger sites.

<img src="https://github.com/SQLMesh.png?size=48" width="32" height="32" alt="SQLMesh" align="left" /> **[SQLMesh #6040](https://github.com/SQLMesh/sqlmesh/pull/6040)** — fixed a concurrency race in `sqlmesh test` involving `time_machine` and worker threads.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2849](https://github.com/stellar/stellar-docs/pull/2849)** — reworked the Soroban address conversion example to propagate the fallible `Result<Address, ConversionError>` from `Address::from_xdr()` instead of calling `.unwrap()`, which panics on malformed XDR, and noted that contracts consuming XDR from untrusted sources must handle the error instead of aborting.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2850](https://github.com/stellar/stellar-docs/pull/2850)** — documented Quickstart's undocumented `--enable-core-manual-close` flag in the advanced usage docs. The Operation Modes page now covers the flag, the `MANUAL_CLOSE` setting it writes into the generated `etc/stellar-core.cfg`, and triggering a close through the `manualclose` endpoint on port 11626, while Run Commands adds macOS, Linux, and Windows startup examples that bind the admin port to loopback. The new section also records two limits readers hit in practice: the flag is accepted on every network but only usable on local, because stellar-core checks `NODE_IS_VALIDATOR` when `manualclose` is invoked and only the local config sets it, and each invocation advances exactly one ledger.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2851](https://github.com/stellar/stellar-docs/pull/2851)** — qualified the dapp frontend guide's blanket claim that Freighter requires HTTPS; `http://localhost` and `http://127.0.0.1` are already Potentially Trustworthy origins under the W3C Secure Contexts specification, so plain HTTP on loopback satisfies the requirement and local development needs no TLS.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2853](https://github.com/stellar/stellar-docs/pull/2853)** — reconciled contradictory memo guidance in the pooled accounts guide: the intro framed memos as obsolete while later sections still required supporting them, so memos now read as the legacy mechanism still in active use and muxed accounts as preferred going forward.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="stellar-docs" align="left" /> **[stellar-docs #2859](https://github.com/stellar/stellar-docs/pull/2859)** — added the --enable-core-manual-close flag to the Local section of the Network Modes page, so the parameter list no longer omits a flag the quickstart container ships, with a cross-link to the Manual close mode section noting that only the local configuration sets NODE_IS_VALIDATOR.

<img src="https://github.com/thirdweb-dev.png?size=48" width="32" height="32" alt="thirdweb" align="left" /> **[thirdweb JS #8938](https://github.com/thirdweb-dev/js/pull/8938)** — fixed `useTokenQuery` collapsing real token lookup failures into `unsupported_token` instead of using the existing error/retry path.

<img src="https://github.com/ssf0409.png?size=48" width="32" height="32" alt="tracelens" align="left" /> **[tracelens #140](https://github.com/ssf0409/tracelens/pull/140)** — markdown table cells in the report generator are now escaped with html.escape in addition to pipe and newline handling. Task ids or gate values containing pipes, line breaks, or HTML metacharacters no longer break the per-task and baseline-gate tables piped into $GITHUB_STEP_SUMMARY, and no cell can open a raw HTML element.
<!-- ledger:profile-merged:end -->
---

## 🚀 Flagship Architectures & Projects

- 🔬 **[Synthesis](https://synthesis-gold.vercel.app/)** — autonomous multi-agent research with planning, research, synthesis, critique, HITL gates, RAG, Reflexion, and live SSE agent graphs ([repo](https://github.com/devtechedge/synthesis)).
- 💼 **[Jobrow](https://jobrow.vercel.app)** — live register of still-open US tech roles sourced from employer ATS boards, with search, filters, closed-role tracking, and a public JSON API ([repo](https://github.com/devtechedge/job-board)).
- ⛓️ **[Lattice](https://lattice-devtechedge1.vercel.app)** — Web3 jobs platform aggregating blockchain and crypto roles with salary observatory, talent directory, gigs, and hiring intelligence ([repo](https://github.com/devtechedge/lattice)).
- 🪐 **[Pulsar](https://devtechedge.github.io/pulsar/)** — decentralized AI compute protocol interface with Base smart contracts, staking flows, wallet connectivity, 3D visualization, tokenomics, and Foundry-tested contracts ([repo](https://github.com/devtechedge/pulsar)).
- 🧠 **[AAROP](https://aarop.vercel.app)** — explicit Perceive → Plan → Act → Observe → Reflect → Adapt loop with self-verification, bounded autonomy, and replayable traces ([repo](https://github.com/devtechedge/aarop)).
- ⚖️ **[RegTrace](https://regtrace-ai.vercel.app)** — HITL Web3 compliance copilot mapping packs onto MiCA/VARA with retrieval-bounded findings and article citations ([repo](https://github.com/devtechedge/regulatory_compliance)).
- 🏥 **[Cadence](https://cadence-healthcare.vercel.app/)** — deep-memory healthcare agent lab with layered patient memory, journey stages, and consent-scoped clinician briefs ([repo](https://github.com/devtechedge/healthcare-deep-memory-agents)).
- 🔎 **[Veritas](https://veritas-engine-woad.vercel.app)** — LangGraph research agent with SSE streaming, grounded demo mode, and external retrieval when configured ([repo](https://github.com/devtechedge/veritas-engine)).
- 🔥 **[Chaos Simulator](https://chaos-simulation.vercel.app)** — real-time chaos engineering dashboard with fault injection, self-healing services, animated service topology, scenario orchestration, telemetry, and recovery analysis ([repo](https://github.com/devtechedge/chaos-simulator)).

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
