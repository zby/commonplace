# Phase 3 — Move canonical heads and migrate host projects

**State:** waits for consumer convergence in Phase 2.

## Outcome

Add `kb/tags/` as the canonical head collection only after consumers find heads
in their current locations through the resolver. Relocate the source corpus,
ship the new layout, and migrate host projects as a breaking representation
change, not as part of the semantic foundation.

## Work

1. Add the `kb/tags/` collection contract and landing, declared
   `non-participating`. Define its introduction quality goal, common
   meaning/use/boundary/route/stopping prefix, and link grammar.
2. Re-derive all transitional heads and participating tags. Move every source
   head to a direct child of `kb/tags/` with `commonplace-relocate-note`. Never
   freeze a head count in migration code or acceptance.
3. Let filenames supply canonical tag identity. Remove `index_source: tag`,
   `index_key`, the legacy `tags-README.md` hub, and
   `index_source: tag-indexes` after moving useful hub prose to the landing.
4. Update footer routing, generated augmentation, review-sweep scope, redirects,
   and every path-constructing consumer. Switch `resolve_tag_head` from legacy
   metadata lookup to direct canonical construction without retaining a legacy
   fallback.
5. Add `tags` to the shipped library in `hatch_build.py` and repoint the
   navigation entry point that `library.md` lists.
6. Scaffold an empty host `kb/tags/` collection. Add a `commonplace-init`
   migration that moves a host project's existing heads there, alongside the
   existing type-pointer and legacy-copy migrations. Do not create a separate
   tag updater.
7. Retire both adopted proposals and annotate prior tag ADRs forward after the
   source, build, and init fixtures pass.

## Acceptance

- Every tag on an eligible artifact reaches its KB's canonical head.
- Host and library heads, marks, and generated listings remain independent.
- No live duplicate head identity or legacy hub identity remains.
- Every shipped head link resolves or is rewritten by the build.
- Fresh and pre-move host fixtures converge on the same layout while
  preserving user additions.
- Resolver, validation, ProperDocs, connect, relocation, build, init, and
  full-suite checks pass.
