# A catch block that returned nothing

**Repo:** thirdweb-dev/js · **PR:** [#8938](https://github.com/thirdweb-dev/js/pull/8938) · **Issue:** [#8937](https://github.com/thirdweb-dev/js/issues/8937) · **Merged:** 7 Sep 2026 · **Language:** TypeScript

## The symptom

Every failed destination token lookup in `useTokenQuery` rendered the dead end "Token Not Supported" screen, whether the actual cause was a 401, a 429, a timeout, or a non-Error abort.

## Root cause

The `.catch` in `useTokenQuery` used a block body and never returned, so `Promise.reject(err)` was evaluated and then discarded. Every rejection fell through to the same fallback, `{ type: "unsupported_token" }`.

The compounding part is React Query. It cached that fallback as a success, and with `refetchOnMount: false` the wrong result stuck. CheckoutWidget and TransactionWidget then rendered the unsupported token screen instead of the ErrorBanner retry path that already existed in the codebase.

## Why the obvious fix is wrong

Deleting the `.catch` entirely would let genuine "not supported" responses reach the UI as errors, when the unsupported token screen is the correct outcome for exactly those. The fix has to distinguish, not either swallow everything or swallow nothing.

## The change

The catch now returns `undefined` only for genuine `Error`s whose message includes `"not supported"`, and rethrows everything else, including non-Error rejections. 4 added and 1 removed in `packages/thirdweb/src/react/web/ui/Bridge/common/token-query.ts`.

`UnsupportedTokenScreen` and `onError` were deliberately left alone. Changing them is a separate UX decision, and the widget already renders `ErrorBanner` the moment the query actually errors.

## Verification

Unit tests cover success, a `"Token not supported"` rejection, a 401, and a non-Error `"timeout"` rejection (117 lines). Manual check: render `<CheckoutWidget>` with a supported token and block `bridge.thirdweb.com` in DevTools, which should show ErrorBanner with Try Again rather than Token Not Supported.
