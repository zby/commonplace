# T1 plan — Scope tag membership claims to one collection

**State:** open; the active tag-scope proposal remains unadopted and the live
cross-collection `learning-theory` witness is unchanged.

## Resolution selected

Adopt the proposal's formal collection-scope option. A tag-README's `complete`
and `covered_by` marks quantify over artifacts in its owning collection. The
same tag string in another collection denotes another membership set. A mark
may license skipping only that collection's sweep.

This matches the current validator, generated tail, and connect behavior without
introducing an unused scope field or repository-wide tag governance.

## Work

1. Record an ADR extending ADRs 025 and 026 with the collection-scoped
   semantics, skip right, same-string rule, and tag-link routing boundary.
2. Qualify every operative statement of the marks, including:
   `kb/types/tag-readme.md`, `navigation.md`, source and generated AGENTS files,
   `maintain-curated-indexes.md`, and `cp-skill-connect`.
3. Standardize the search recipe as one explicit collection sweep. A
   cross-collection query is a union of independent sweeps; no one collection's
   mark suppresses the others.
4. Bound ProperDocs `_find_tag_index` to the note's nearest collection root. A
   tag without a landing in that collection renders as plain text rather than
   linking to another collection's incomplete-for-this-reader tail.
5. Keep generated tag tails and validation collection-scoped. The external
   `learning-theory` note needs no child tag under this decision because it is
   outside the notes collection claim; the repaired scope and routing make that
   fact visible.
6. Adopt and archive the proposal only after the ADR, contracts, code, and tests
   land.

## Verification

- A nested note links to its collection-root tag landing.
- A same-string tag in another collection does not link across the boundary.
- Generated tails exclude other collections.
- `complete` and `covered_by` ignore same-string members outside the owner
  collection, and their messages name the checked scope.
- Focused tag-readme and ProperDocs tests, the full test suite, lint, and a site
  build pass.

T1 closes when every stated skip right equals the validator's exact membership
set and routing never lands a reader on a tail that excludes the source note.
