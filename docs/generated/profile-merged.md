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

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2851](https://github.com/stellar/stellar-docs/pull/2851)** — qualified the dapp frontend guide's blanket claim that Freighter requires HTTPS; `http://localhost` and `http://127.0.0.1` are already Potentially Trustworthy origins under the W3C Secure Contexts specification, so plain HTTP on loopback satisfies the requirement and local development needs no TLS.

<img src="https://github.com/stellar.png?size=48" width="32" height="32" alt="Stellar" align="left" /> **[stellar-docs #2853](https://github.com/stellar/stellar-docs/pull/2853)** — reconciled contradictory memo guidance in the pooled accounts guide: the intro framed memos as obsolete while later sections still required supporting them, so memos now read as the legacy mechanism still in active use and muxed accounts as preferred going forward.

<img src="https://github.com/thirdweb-dev.png?size=48" width="32" height="32" alt="thirdweb" align="left" /> **[thirdweb JS #8938](https://github.com/thirdweb-dev/js/pull/8938)** — fixed `useTokenQuery` collapsing real token lookup failures into `unsupported_token` instead of using the existing error/retry path.
<!-- ledger:profile-merged:end -->
