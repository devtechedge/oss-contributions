# ⚙️ OSS contributions

Public ledger of **upstream open-source contributions**.

![Merged](https://img.shields.io/badge/merged-10-brightgreen?logo=git&logoColor=white) ![License](https://img.shields.io/github/license/devtechedge/oss-contributions) ![Last commit](https://img.shields.io/github/last-commit/devtechedge/oss-contributions) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white) ![TanStack](https://img.shields.io/badge/TanStack-FF4154?logo=tanstack&logoColor=white) ![Web3](https://img.shields.io/badge/Web3-000000?logo=web3.js&logoColor=white)

**Latest update:** 14 Sep 2026

This repository serves as the canonical record of upstream contribution activity: identifying worthwhile issues, tracking claims and active pull requests, preserving implementation and review outcomes, and maintaining an auditable history of merged, closed, and declined work.

## ✅ Merged pull requests

| Repo | PR | What | Merged |
| --- | --- | --- | --- |
| <img src="https://github.com/recharts.png?size=40" width="18" /> [recharts/recharts](https://github.com/recharts/recharts) | [#7805](https://github.com/recharts/recharts/pull/7805) | Removed `tabIndex={-1}` from z-index portal `<g>` layers so empty SVG groups are not pointer-focusable, preventing WebKit geometry-traced focus rings; added regression coverage asserting no rendered layer carries a `tabindex` attribute. | 13 Sep 2026 |
| <img src="https://github.com/brianc.png?size=40" width="18" /> [brianc/node-postgres](https://github.com/brianc/node-postgres) | [#3772](https://github.com/brianc/node-postgres/pull/3772) | `Connection.sync()` no longer permanently sets `_ending`, so later `ECONNRESET` / `EPIPE` errors are not swallowed. Regression and integration coverage protects the behavior. | 11 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14753](https://github.com/pnpm/pnpm/pull/14753) | `lockfile: false` is respected with `devEngines.packageManager.onFail: download`; package-manager download/switch still works without project lockfile synchronization. | 10 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14756](https://github.com/pnpm/pnpm/pull/14756) | `pnpm update pkg@x.y.z` preserves existing `^` / `~` range operators and supported `npm:` / `jsr:` prefixes. | 10 Sep 2026 |
| <img src="https://github.com/pnpm.png?size=40" width="18" /> [pnpm/pnpm](https://github.com/pnpm/pnpm) | [#14754](https://github.com/pnpm/pnpm/pull/14754) | Non-recursive `pnpm run "/pattern/" --no-bail` no longer terminates sibling scripts after the first failure. | 10 Sep 2026 |
| <img src="https://github.com/SQLMesh.png?size=40" width="18" /> [SQLMesh/sqlmesh](https://github.com/SQLMesh/sqlmesh) | [#6040](https://github.com/SQLMesh/sqlmesh/pull/6040) | `ModelTest.create_test()` runs on the calling thread, eliminating a race around shared `execution_time` / `time_machine` state. | 10 Sep 2026 |
| <img src="https://github.com/better-auth.png?size=40" width="18" /> [better-auth/better-auth](https://github.com/better-auth/better-auth) | [#11208](https://github.com/better-auth/better-auth/pull/11208) | Regression coverage locks the `/phone-number/verify` OpenAPI `requestBody` contract after a Zod intersection issue. | 9 Sep 2026 |
| <img src="https://github.com/biomejs.png?size=40" width="18" /> [biomejs/biome](https://github.com/biomejs/biome) | [#11667](https://github.com/biomejs/biome/pull/11667) | Added the `useBetterDomTraversing` nursery lint rule, ported from `eslint-plugin-unicorn`, with fixtures and release integration. | 8 Sep 2026 |
| <img src="https://github.com/anza-xyz.png?size=40" width="18" /> [anza-xyz/kit](https://github.com/anza-xyz/kit) | [#2032](https://github.com/anza-xyz/kit/pull/2032) | Restored `number` predicates in the `getPatternMatchCodec` documentation examples so they match the actual codec typing. | 9 Sep 2026 |
| <img src="https://github.com/thirdweb-dev.png?size=40" width="18" /> [thirdweb-dev/js](https://github.com/thirdweb-dev/js) | [#8938](https://github.com/thirdweb-dev/js/pull/8938) | Genuine `useTokenQuery` request failures are rethrown instead of being converted into `Token Not Supported`; added regression tests and changeset. | 7 Sep 2026 |

## 🔀 Open pull requests

The repository currently tracks active upstream contributions across application libraries, infrastructure, frameworks, developer tooling, testing, security, accessibility, wallets, SDKs, and blockchain-related software. These contributions are maintained directly in their respective upstream repositories, and this ledger records the substantive work and its current state.

| Repo | PR | What | Opened |
| --- | --- | --- | --- |
| <img src="https://github.com/pypa.png?size=40" width="18" /> [pypa/hatch](https://github.com/pypa/hatch) | [#2422](https://github.com/pypa/hatch/pull/2422) | Replaced the German word `verboten` with `forbidden` in the dynamic metadata how-to (`docs/how-to/config/dynamic-metadata.md`), fixing #2420. One-word docs change; first-contribution workflow runs pending maintainer approval. | 14 Sep 2026 |

## 🧭 Engineering focus

TypeScript · JavaScript · Python · Rust · frameworks · developer tooling · infrastructure · concurrency · portability · security · accessibility · testing · wallets · SDKs · blockchain infrastructure

## 📄 License

MIT
