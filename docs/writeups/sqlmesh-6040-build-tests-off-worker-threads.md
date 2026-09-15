# Build the tests before the workers race

**Repo:** SQLMesh/sqlmesh · **PR:** [#6040](https://github.com/SQLMesh/sqlmesh/pull/6040) · **Issue:** [#6039](https://github.com/SQLMesh/sqlmesh/issues/6039) · **Merged:** 10 Sep 2026 · **Language:** Python

## The symptom

`sqlmesh test` with `concurrent_tasks > 1` intermittently failed with `IndexError: list index out of range` while creating tests, but only when a unit test set `vars.execution_time`.

## Root cause

`ModelTest.create_test()` was running on pool worker threads. That path can call `to_datetime()`, which reaches `ttl_cache` and reads `time.time()`, while a different worker is starting or stopping a `time_machine` freeze. Two workers mutating and reading the frozen clock at the same time is what produced the IndexError.

## Why not add a lock

The shared state is process global time, not a sqlmesh object. Guarding it properly would mean holding a lock across every `to_datetime()` call in the creation path, including calls made inside dependencies the code does not control. Moving the work to a single thread removes the concurrency instead of serialising a call graph you cannot see.

## The change

`ModelTest.create_test()` now runs on the calling thread before any work is submitted to the pool. Workers only execute tests that are already built. Creation stays inside the same try/finally that closes engine adapters, so an invalid `create_test` still cleans up its connections. 24 added and 23 removed in `sqlmesh/core/test/runner.py`.

## Verification

`tests/core/test_test.py::test_freeze_time_concurrent` passed 20 consecutive times locally. A race needs repetition: a single pass proves nothing, so it was run twenty times rather than once.
