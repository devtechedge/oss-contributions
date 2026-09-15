# useBetterDomTraversing, and knowing what not to autofix

**Repo:** biomejs/biome · **PR:** [#11667](https://github.com/biomejs/biome/pull/11667) · **Issue:** [#11641](https://github.com/biomejs/biome/issues/11641) · **Merged:** 8 Sep 2026 · **Language:** Rust

This one is a feature rather than a fix: a nursery lint rule ported from `eslint-plugin-unicorn`'s `better-dom-traversing`.

## What it flags

- `element.childNodes[0]` becomes `.firstChild`
- `element.children[0]` becomes `.firstElementChild`
- `element.children[n]` for n > 0 suggests `.querySelector()`, with no autofix
- chained `.parentElement` suggests `.closest()`, with no autofix
- chained static `.querySelector()` calls that can be merged, using `:scope` on elements but never on `document`
- `props.children` is ignored

## The interesting part is what it refuses to fix

Every autofix here is unsafe, and each one is unsafe for a different reason. An empty collection is `undefined` where the traversal property returns `null`. `.closest()` is not an exact hop count, so rewriting a two hop chain silently changes semantics. A combined selector is not equivalent to nested `querySelector` calls.

So the rule reports all of them but only rewrites the two cases where the transformation is exact. It declines to rewrite when the selector contains a comma or `:scope`, and when the node contains comments. Choosing where to stop is most of the work in a rule like this.

## The change

702 lines in the rule source, plus wiring through six other crates: configuration, the generated linter options check, diagnostics categories, rule options, a syntax `expr_ext` helper, and the CLI's eslint migration mapping. Spec tests and snapshots cover both JS and JSX.

## Verification

`cargo test -p biome_js_analyze --test spec_tests nursery::use_better_dom_traversing`, 3 passing. The specs port the unicorn cases, including optional chaining, non-DOM receivers, computed member names and JSX `props.children`.
