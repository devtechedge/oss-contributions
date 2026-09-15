# Search that says "no results" while it is still indexing

**Repo:** web-infra-dev/rspress · **PR:** [#3678](https://github.com/web-infra-dev/rspress/pull/3678) · **Issue:** [#3658](https://github.com/web-infra-dev/rspress/issues/3658) · **Merged:** 14 Sep 2026 · **Language:** TypeScript

## The symptom

On a medium site, a query typed shortly after opening search rendered "No matching results". Retyping the same query returned the right results. Reproduced at 952 documents per locale.

## Root cause

`LocalProvider.init()` called `addAsync()` on the three FlexSearch indexes for every page and never awaited the returned promises. `SearchPanel.initSearch()` awaited `init()` and set `initStatus` to `'inited'` while indexing was still running, so the panel reported ready before the index was ready and ran the first query against a partially built index.

## Why the obvious fix is wrong

The tempting fix is to make the panel retry the pending query, or to poll on `initStatus`. Both paper over it. The panel would still report ready before the index is ready, and any timing based retry is a guess about how long 952 documents take to index, which varies by machine. The dropped promise is the bug, so the fix belongs where the promise is dropped.

## The change

Collect the `addAsync()` promises for each page's three indexes into a pending array and `await Promise.all(pending)` before `init()` resolves. The panel keeps its loading state until the index is ready, then runs the pending query. 7 added and 3 removed in `packages/core/src/theme/components/Search/logic/providers/LocalProvider.ts`. No other behaviour changes.

## Verification

`tsc --noEmit` on `packages/core` passes. Repo build and diff checks pass.
