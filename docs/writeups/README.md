# Selected write-ups

Short technical notes on individual merged upstream pull requests. Each one covers the symptom, the root cause, why the obvious fix was wrong, and how the change was verified.

The ledger README lists every merged contribution. These go deeper on eight of them.

| Write-up | Repo | Language | What it is about |
| --- | --- | --- | --- |
| [Sync is not a disconnect](node-postgres-3772-sync-is-not-a-disconnect.md) | node-postgres #3772 | JavaScript | A connection state flag set on every query barrier silently swallowed socket errors |
| [A package manager that cannot print its own version](pnpm-14863-store-dir-panic-on-unix.md) | pnpm #14863 | Rust | One resolver panicking instead of using the crate's own non-Windows fallback |
| [pnpm update ate your caret](pnpm-14756-update-ate-the-caret.md) | pnpm #14756 | Rust, TypeScript | A versioned update rewrote the manifest and dropped the declared range operator |
| [A focus ring that traced the shape of a bar](recharts-7805-pointer-focus-rings.md) | recharts #7805 | TypeScript | `tabindex="-1"` on SVG layer groups made charts pointer focusable |
| [A catch block that returned nothing](thirdweb-js-8938-catch-block-returned-nothing.md) | thirdweb-dev/js #8938 | TypeScript | A `.catch` with a block body turned every token lookup failure into "unsupported" |
| [Search that says "no results" while it is still indexing](rspress-3678-await-search-indexing.md) | rspress #3678 | TypeScript | An unawaited FlexSearch `addAsync()` let the panel report ready too early |
| [Build the tests before the workers race](sqlmesh-6040-build-tests-off-worker-threads.md) | SQLMesh #6040 | Python | Moving test construction off pool workers instead of locking global time |
| [useBetterDomTraversing, and knowing what not to autofix](biome-11667-use-better-dom-traversing.md) | Biome #11667 | Rust | A new nursery lint rule, and why most of its fixes stay unsafe |
