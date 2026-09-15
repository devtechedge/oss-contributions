# pnpm update ate your caret

**Repo:** pnpm/pnpm · **PR:** [#14756](https://github.com/pnpm/pnpm/pull/14756) · **Issue:** [#14745](https://github.com/pnpm/pnpm/issues/14745) · **Merged:** 10 Sep 2026 · **Language:** Rust, TypeScript

## The symptom

`pnpm update react@19.3.0` against a manifest declaring `"react": "^19.2.8"` rewrote the entry to `19.3.0`, dropping the caret. pnpm 11 wrote `^19.3.0`. A routine version bump silently changed the dependency's upgrade policy.

## Root cause

`pnpm update <name>@<version>` rewrites `package.json` before the install, in `matched_direct_rewrite` in `update.rs`. That path wrote the requested text verbatim, so the operator already declared in the manifest was lost.

## Why not fix it in the resolver

The resolver never sees the original operator on this path. `update` writes the specifier before resolution starts, so by the time any `calc_specifier` logic runs, the caret is already gone. The rewrite has to happen where the text is written.

## The change

The version is now recorded through `calc_version_range` under the operator the manifest already pins, so `^` stays `^`, `~` stays `~`, and an exact pin stays exact. The npm alias splitter is reused so an `npm:` or `jsr:` aliased entry keeps its prefix.

Two details that are easy to miss:

- The requested version is seeded into the resolution keyed by the name the entry resolves under rather than its alias, so the lockfile records it even when the kept range admits a newer version.
- The npm resolver's `calc_specifier` and `calc_prefixed_specifier` now prefer the previous specifier's operator over the requested one, matching the TypeScript `calcVersionRange`. That path only runs under `update --latest`, which now passes the manifest entry as the previous specifier. Without it, a prerelease range such as `^3.0.0-rc.0` lost its operator.

207 lines added and 55 removed across six source files, plus a changeset.

pnpm 11 was unaffected: `parseWantedDependencies` supplies `prevSpecifier` from the manifest and the resolver computes the importer specifier.

## Verification

New CLI test suites `update.rs` (111 lines) and `update_jsr.rs` (72 lines), plus unit tests in `manifest_spec_bumps` (35 added) and `calc_specifier` (68 added).
