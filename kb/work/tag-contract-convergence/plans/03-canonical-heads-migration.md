# Phase 3 — Move canonical heads and migrate projections

**State:** waits for consumer convergence and the I1/I2 mechanisms.

## Outcome

Add `kb/tags/` as the canonical head collection only after consumers can find
heads in their current locations through the resolver. Relocate the corpus and
installed projection as a breaking representation migration, not as part of
the semantic foundation patch.

## Work

1. Add the `kb/tags/` collection contract and landing. Define its introduction
   quality goal, common meaning/use/boundary/route/stopping prefix, and
   cross-library link grammar.
2. Move the existing per-tag heads to direct children of `kb/tags/` and add the
   required `trace-learning` head. Derive the execution inventory rather than
   freezing today's count.
3. Let filenames supply canonical tag identity. Remove `index_source: tag`,
   `index_key`, the legacy `tags-README.md` hub, and
   `index_source: tag-indexes` after moving useful hub prose to the landing.
4. Update footer routing, generated augmentation, review-sweep scope, redirects,
   and every path-constructing consumer without retaining a legacy fallback.
5. Give every projection-sensitive head link an explicit I2 disposition.
   Scaffold an empty host tag collection and project eligible Commonplace heads
   under the vendored logical root without merging namespaces.
6. Supply the move map, obsolete paths, and sentinel user content to I1's
   ownership-aware upgrade mechanism. Do not create a tag-specific updater.
7. Retire both adopted proposals and annotate prior tag ADRs forward after all
   source and installed fixtures pass.

## Acceptance

- Every eligible artifact reaches its own root's canonical head when one
  exists.
- Host and vendored heads, marks, and generated listings remain independent.
- No live duplicate head identity or legacy hub identity remains.
- Every shipped head link resolves in the selected installed edition.
- Fresh and upgraded fixtures converge on framework-owned paths while
  preserving user additions.
- Resolver, validation, ProperDocs, connect, relocation, upgrade, site-build,
  and full-suite checks pass in their appropriate packets.
