# Sync is not a disconnect

**Repo:** brianc/node-postgres · **PR:** [#3772](https://github.com/brianc/node-postgres/pull/3772) · **Issue:** [#3769](https://github.com/brianc/node-postgres/issues/3769) · **Merged:** 11 Sep 2026 · **Language:** JavaScript

## The symptom

After the first parameterized query on a connection, socket level errors such as `ECONNRESET` and `EPIPE` stopped surfacing. They were not logged, not emitted, and not propagated to the caller.

## Root cause

`Connection` carries an `_ending` flag. `reportStreamError` uses it to decide that an `ECONNRESET` or `EPIPE` is expected and can safely be ignored, because the caller explicitly asked to disconnect.

`Connection.sync()` was setting `_ending = true` on every extended query Sync. Sync is the protocol barrier that follows Parse, Bind and Execute. It is not a disconnect. Once the first parameterized query set the flag, it stayed set for the remaining life of the connection, so every later socket error was silently dropped.

This matters more with `pipeline: true`. The normal error path is closed, so recovery depends only on the async `close` and `end` path, which can leave an in-flight query promise unsettled.

## Why the obvious fix is wrong

Clearing `_ending` after Sync returns looks right and is not. The flag means "we are tearing down", and on a pipelined connection Sync can interleave with a genuine `end()`. Resetting it after the barrier reintroduces the exact race the flag exists to prevent.

The correct change is narrower: never set it in `sync()` in the first place. It stays set only in `end()` (Terminate) and the connect timeout teardown path, which already sets `con._ending = true` before destroying the stream.

## The change

Two lines added and one removed in `packages/pg/lib/connection.js`.

## Verification

- Unit coverage asserting that Sync leaves `_ending` false, and that `ECONNRESET` after Sync still emits `error`.
- Integration coverage in `packages/pg/test/integration/gh-issues/3772-tests.js` (161 lines).
- Existing disconnect coverage still goes through `end()`, so the original behaviour stays pinned.
- Full `packages/pg` unit suite: 284 passing.
