---
description: "Proposal: keep review dependencies factored as two-input pairs where that shape fits; type and collection pairs are shipped while a review target with more than two inputs remains"
type: reference/types/design-proposal.md
tags: [kb-maintenance, observability, review-system]
---

# Factored dependency pairs for review freshness

An accepted review is a build product and its inputs are prerequisites — [make-like staleness detection](../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md). Review freshness realizes this for exactly two inputs per pair: note text and criterion text. Type-conformance pairs ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) showed the cheap way to admit a new dependency: do not widen one pair's input set to N — factor each dependency into its own two-input pair where the dependency document is the gate side. This proposal holds the not-yet-adopted remainder of that direction: whether a review target may ever take more than two inputs.

## Current state (as of 2026-09-22)

- Type-conformance pairs are shipped ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)): criterion selection derives `(note, type_spec)` pairs from note frontmatter, the type spec is the criterion, and a type edit stales its cohort through the criterion hash.
- `COLLECTION.md`-as-gate is shipped ([ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)): criterion selection derives `(note, collection_md)` pairs from note location under the `collection`/`collection/{path}` lens, again with no storage change.
- Source-as-gate was shipped and then removed by the ADR 073 revision. It
  factored each direct ingest link into a separate pair, but its criterion was
  an interpreted Claims ledger. Direct source alignment now belongs to the
  standard `semantic/grounding-alignment` pair, which reads retained quotes or
  a declared snapshot through the note's links. The factoring pattern remains
  proven for type and collection dependencies.
- (2026-11-10) [ADR 127](../adr/127-review-runs-as-workflows-over-result-files.md) replaced the general freshness store ([ADR 052](../adr/052-general-freshness-store-review-first-migration.md)), whose role-labelled input rows admitted any number of inputs per target. A review result is now one file per pair that records exactly two hashes, the note's (over the parts the criterion watches) and the criterion's ([review architecture](../review-architecture.md)). Any markdown file can be the criterion, so any repo document can sit on the criterion side.
- Cohort-scoped acknowledgement, adopted under ADR 052 as this proposal's preferred cohort-ack input, was dropped by ADR 127: a pair whose input changed is re-reviewed.
- No judgment has been identified that irreducibly reads three or more texts in one prompt; no review target registers a third input.
- A fuller design for a general lineage model — lineage targets, append-only events, per-event input versions, typed resolvers — is in flight in the workshop layer at `kb/work/lineage-mechanisms/general-lineage-refresh-state-design.md` (cited by path, not linked, per the no-workshop-links convention); factoring-into-pairs narrows how much of it review freshness will ever need.

## The design: one pair per dependency edge

Each new review dependency becomes its own `(note_path, dependency_path)` pair with the dependency document as the gate:

- **`COLLECTION.md`-as-gate** — *adopted by [ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)*: a note's conformance to its collection's text contract. One pair per note, criterion side the collection's `COLLECTION.md`.
Each factored pair reuses the entire freshness, status and fix stack unchanged, exactly as type-conformance pairs do. Like the type spec, `COLLECTION.md` is not written as a Failure mode / Test procedure, so it needs a mechanical wrapper (or an authored review section in the dependency document, which the hash then sees).

A review target with three or more inputs remains the fallback for a judgment that irreducibly reads three or more texts in one prompt. Such a target needs a result shape that records a third hash, and the selection and prompt behavior that would read it; none is built. No such judgment is identified yet, which is exactly why that target stays unbuilt.

## Forces that keep the remainder at planning

- **Review cost.** Every factored dependency adds a pair per note; the
  corpus-times-dependencies product is real. The retired source case showed how
  a multi-link artifact can multiply pairs even when one standard semantic gate
  already owns the judgment.

## Free choices

- **Wrapper prompt vs authored review section.** Same trade as for type specs, and the freshness boundary weighs the same way: criteria in the dependency document are hashed, wrapper text is not.

## Adoption criteria

- Adopt a review target with more than two inputs only if a judgment appears that genuinely needs a third text in one prompt; the default answer to a new dependency is a new factored pair, not a wider input set.

---

Relevant Notes:

- [link graph plus timestamps enables make-like staleness detection](../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rests-on: the build-product/prerequisite model; factored two-input pairs are its cheapest review-side realization
- [038-type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — evidenced-by: the shipped first instance of the factoring pattern this proposal generalizes
- [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why each dependency document must be the gate rather than be restated in one
- [review system](../README-REVIEW-SYSTEM.md) — part-of: the result-file freshness every factored pair reuses unchanged
- [032-review freshness uses DB snapshots, not Git](../adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: the role-neutral snapshot substrate that lets any repo document sit on the criterion side
