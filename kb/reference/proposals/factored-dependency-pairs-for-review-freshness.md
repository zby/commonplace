---
description: "Proposal: admit new review dependencies as factored (note, dependency) pairs with the dependency as the gate — source-as-gate and a cohort-scoped ack remain; COLLECTION.md-as-gate adopted (ADR 041)"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, observability]
---

# Factored dependency pairs for review freshness

An accepted review is a build product and its inputs are prerequisites — [make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md). Review freshness realizes this for exactly two inputs per pair: note text and criterion text. Type-conformance pairs ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) showed the cheap way to admit a new dependency: do not widen one pair's input set to N — factor each dependency into its own two-input pair where the dependency document is the gate side. This proposal holds the not-yet-adopted remainder of that direction.

## Current state (as of 2026-07-08)

- Type-conformance pairs are shipped ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)): the selector derives `(note, type_spec)` pairs from note frontmatter, the type spec is the gate snapshot, and a type edit stales its cohort via the existing `criterion-changed` reason.
- `COLLECTION.md`-as-gate is shipped ([ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)): the selector derives `(note, collection_md)` pairs from note location under the `collection`/`collection/{path}` lens, again with no storage change. The factoring pattern is proven twice; this proposal now holds only the remainder — source-as-gate, the cohort-scoped ack, and the N-ary fallback.
- Freshness compares two hashes per pair against `accepted_note_hash` / `accepted_criterion_hash` ([ADR 032](../adr/032-review-freshness-uses-db-snapshots-not-git.md)). The snapshot table is role-neutral — keyed by path and content hash — so any repo document can sit on the criterion side.
- Acknowledgement (`commonplace-ack-review`) re-pins the current note and gate snapshots while carrying forward completed review evidence. It is per-note: acking a cohort of N notes after one shared-gate edit takes N invocations (one per note, batching only across gates).
- The selector emits JSON consumed by job creation; there is no cohort-scoped ack surface fed from selector output.
- No judgment has been identified that irreducibly reads three or more texts in one prompt; no N-ary input-set table exists.
- A fuller design for a general lineage model — lineage targets, append-only events, per-event input versions, typed resolvers — is in flight in the workshop layer at `kb/work/lineage-mechanisms/general-lineage-refresh-state-design.md` (cited by path, not linked, per the no-workshop-links convention); factoring-into-pairs narrows how much of it review freshness will ever need.

## The design: one pair per dependency edge

Each new review dependency becomes its own `(note_path, dependency_path)` pair with the dependency document as the gate:

- **`COLLECTION.md`-as-gate** — *adopted by [ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)*: a note's conformance to its collection's register and conventions. One pair per note, criterion side the collection's `COLLECTION.md`.
- **Source-as-gate** — a derived note's consistency with the source snapshot it distills. This is the multi-source invalidation case: one pair per `(note, source)` edge, so each source invalidates independently with its own diff.

Each factored pair reuses the entire freshness/ack/warn stack unchanged, exactly as type-conformance pairs do. Like the type spec, neither `COLLECTION.md` nor a source snapshot is written as a Failure mode / Test procedure, so each needs a mechanical wrapper (or an authored review section in the dependency document, which the hash then sees).

The N-ary input-set design — freshness baseline pinning a variable set of `(input_key, role, resolver, accepted_version)` records — remains the fallback for a judgment that irreducibly reads three or more texts in one prompt. No such judgment is identified yet, which is exactly why the input-set table stays unbuilt.

## Cohort-scoped ack

The force that factored pairs sharpen: cohort blast radius. A `COLLECTION.md` edit stales a whole collection; a type edit stales a whole type cohort — same shape as a wide gate edit. The answer is a cohort-scoped ack surface — an improvement to the existing ack command (by type, by gate, or fed from selector JSON) rather than new freshness semantics. The operator judges one gate-side diff and acknowledges the cohort in one decision instead of N per-note invocations.

## Forces that keep this at planning

- **Review cost.** Every factored dependency adds a pair per note; the corpus-times-dependencies product is real. Type-conformance stayed opt-in for the same reason; factored pairs should expect the same discipline.
- **No demand signal yet.** No type edit has yet staled more pairs than per-note acking comfortably clears, and no note has needed source-consistency review badly enough to pay its pair cost.

## Free choices

- **Gate id scheme per dependency kind.** Type pairs use a virtual `type/{name}` lens; `collection/{path}` and `source/{name}` lenses would keep the CLI uniform, but source snapshots may not have stable short names.
- **Wrapper prompt vs authored review section.** Same trade as for type specs, and the freshness boundary weighs the same way: criteria in the dependency document are hashed, wrapper text is not.
- **Cohort-ack input.** By gate path, by type, or by piping selector JSON into the ack command; selector JSON is the most general and adds no new selection logic.

## Adoption criteria

- Adopt cohort-scoped ack when the first real type or collection edit stales more pairs than per-note acking comfortably clears. `COLLECTION.md`-as-gate raises the odds: one contract edit stales a whole collection.
- Adopt source-as-gate when a note's consistency with a distilled source is first wanted as a reviewable judgment — a gate source plus a wrapper, no storage change. (`COLLECTION.md`-as-gate met its criterion and is adopted; see ADR 041.)
- Adopt the N-ary input-set model only if a judgment appears that genuinely needs a third text in one prompt; the default answer to a new dependency is a new factored pair, not a wider input set.

---

Relevant Notes:

- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the build-product/prerequisite model; factored two-input pairs are its cheapest review-side realization
- [038-type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — rationale: the shipped first instance of the factoring pattern this proposal generalizes
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why each dependency document must be the gate rather than be restated in one
- [review system](../README-REVIEW-SYSTEM.md) — part-of: the freshness, freshness baseline, and ack concepts every factored pair reuses unchanged
- [032-review freshness uses DB snapshots, not Git](../adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: the role-neutral snapshot substrate that lets any repo document sit on the criterion side
