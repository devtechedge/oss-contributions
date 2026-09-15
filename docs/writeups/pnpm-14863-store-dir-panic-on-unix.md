# A package manager that cannot print its own version

**Repo:** pnpm/pnpm · **PR:** [#14863](https://github.com/pnpm/pnpm/pull/14863) · **Issue:** [#14859](https://github.com/pnpm/pnpm/issues/14859) · **Merged:** 14 Sep 2026 · **Language:** Rust

## The symptom

On FreeBSD, every pnpm command aborted. The Rust config crate panicked at `crates/config/src/defaults.rs:107` with `unsupported operating system: freebsd`, so even `pnpm --version` exited with SIGABRT after upgrading to pnpm 12.4.1. A package manager that cannot print its own version is a total outage on that platform.

## Root cause

`default_store_dir` matched on specific OS strings and panicked on anything it did not recognise. FreeBSD is not in the list.

What makes this interesting is that every other resolver in the same file already handles unknown platforms. `default_pnpm_home_dir` falls through to `~/.local/share/pnpm` for all non-Windows platforms, with an explicit comment stating that policy. `default_cache_dir` falls through to `~/.cache/pnpm`. The shared config dir and state dir resolvers in `pnpm-config-dir` also degrade gracefully. `default_store_dir` was the only one that panicked instead of falling back, which is why one platform broke at startup while nothing else did.

## Why not just add a freebsd arm

Adding `freebsd` fixes one string and leaves NetBSD, OpenBSD and whatever comes next panicking again. The convention in this crate is that non-Windows means Unix, so the fix makes that fallthrough the actual behaviour instead of enumerating platforms. macOS keeps `~/Library/pnpm/store`; everything else Unix resolves to `~/.local/share/pnpm/store`.

## The change

17 added and 4 removed in `pnpm/crates/config/src/defaults.rs`. The OS dependent tail was factored into a small `store_dir_for_os` helper taking the home directory and OS string, mirroring the crate's existing `EnvVar` and `GetHomeDir` test seams. That seam is what makes the new branch testable at all, since there is no FreeBSD runner in CI.

## Verification

Unit tests for the Unix fallback on `freebsd` and `netbsd`, the unchanged `macos` arm, and a `linux` case (19 added, 3 removed). Changeset included with a patch bump.
