# A focus ring that traced the shape of a bar

**Repo:** recharts/recharts · **PR:** [#7805](https://github.com/recharts/recharts/pull/7805) · **Issue:** [#7799](https://github.com/recharts/recharts/issues/7799) · **Merged:** 13 Sep 2026 · **Language:** TypeScript

## The symptom

Clicking anywhere in a chart painted a focus ring. In an application with a global `:focus-visible` rule, the ring looked like a selected bar or a highlighted ReferenceArea.

## Root cause

The z-index layer `<g>` elements carried `tabindex="-1"`. That attribute does not make an element tabbable, but it does make it pointer focusable, so a click focuses it. In WebKit, an outline on an SVG element traces the element's geometry rather than drawing a rectangle, which is why the ring took the shape of the chart content.

## Why not fix it in CSS

Two reasons. The `:focus-visible` rule belongs to the consuming application, not the library, so a library cannot fix it from its own stylesheet. And reaching for `outline: none` is the wrong kind of fix, because it removes a real accessibility affordance that keyboard users depend on.

The attribute was also unnecessary. It was added in PR #6687 to prevent extraneous focusable surfaces, but a bare SVG `<g>` is neither tabbable nor pointer focusable, so removing it preserves the documented intent.

## The change

Two lines added and two removed in `src/zIndex/ZIndexPortal.tsx`.

## Verification

The AllZIndexPortals spec now selects layer groups by their `recharts-zIndex-layer_` class instead of by tabindex, and asserts that no rendered layer group carries a `tabindex` attribute. That assertion fails on main and passes with the change, so it is a real regression guard rather than a test written after the fix.
