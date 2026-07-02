---
description: "Proposal: widen review freshness from the leaf gate file to the full review contract — including the type-spec a note is judged against — so type-definition changes emit contract-changed"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Review freshness should track the full review contract, not just the leaf gate

A note is reviewed *against a contract*: the gate (one quality lens) and the type the note claims — its type-spec doc, which supplies both a schema and authoring guidance. Review freshness today pins only two of those inputs: the note text and the gate text. The type-spec is invisible to freshness. So when a type definition is revised — the exact case where existing notes of that type most need another look — no acceptance goes stale and the review system reports every note as fresh against a contract that changed underneath it. This proposal holds the design for closing that gap: model the type-spec a note is judged against as a review-freshness input, so a type-definition change emits a `contract-changed` staleness reason through the machinery that already exists.

## Current state (as of 2026-07-02)

- **Freshness pins the note and the gate, nothing else.** `classify_staleness` (in `commonplace/review/freshness.py`) compares the current SHA-256 of the note text and the gate text against the accepted snapshots and returns `missing-review`, `gate-changed`, or `note-changed`. Acceptance is keyed `(note_path, gate_path, model_partition)`; the accepted snapshots pin exactly those two files. Editing the gate file invalidates via `gate-changed`.
- **The type-spec is a real input to the judgment but an unmodeled one.** A note declares its type as a path to a type-spec doc ([ADR 018](../adr/018-types-are-path-references-to-instruction-docs.md)); that doc carries the schema *and* the prose authoring guidance a reviewer judges the note against. A gate can target a type via `requires-type`, but the gate text does not embed the type-spec content — so editing the type-spec changes no gate hash and invalidates no acceptance.
- **The schema half is already covered — mechanically, for free.** `commonplace-validate` is stateless and always-current: it re-resolves the type-spec and re-validates against whatever the schema says *now*. Tighten a `.schema.yaml` (new required heading, narrower enum, new required field) and the next validation run flags every existing note of that type. This needs no freshness state; the only thing missing there is a trigger to run the sweep, which is a smaller, separate concern.
- **The architecture doc already names the fix.** [review-architecture.md](../review-architecture.md) says the freshness comparison "should widen to an effective review-contract hash rather than a leaf gate-file hash." A note's type-spec is part of that contract.

## The design

Add the note's **resolved type-spec** to the set of files a `(note, gate)` review's freshness depends on. The accepted baseline pins a type-spec snapshot alongside the note and gate snapshots; a change to it yields a new staleness reason, `contract-changed`. No new storage substrate: reuse `review_file_snapshots` and the same hash-compare — only the input set and the staleness enum grow.

**Keep the mechanical/judgmental split.** The schema stays owned by `commonplace-validate` (mechanical, always-current); the review contract widens over the *judgmental* surface only — the type-spec's prose guidance (authoring instructions, register expectations, template). Folding the schema file into the freshness hash would re-review notes on schema-only edits the validator already caught — paying twice for one change. Body-only hashing of the type-spec keeps the two regimes disjoint; the `watches`-style part split already implemented in `ack_trivial_note_changes.py` is the precedent for hashing one region of a file rather than the whole.

## Free choices

- **What counts as the contract.** Type-spec prose guidance only; the whole type-spec file; or the type-spec plus its transitively `$ref`'d schemas. Body-only avoids double-counting with the validator but needs part-hashing; whole-file is simplest but re-reviews on schema-only edits validate already fails.
- **Whether the base contract counts.** A change to a root spec (`note.md`, `note-base.schema.yaml`) touches almost every note. Including it is correct but high-reach; excluding it avoids mass invalidation at the cost of missing genuine base-contract shifts.
- **Reason granularity.** One `contract-changed` reason, or split `type-changed` from `gate-changed`. One reason is simpler; splitting gives the selector a sharper triage signal and a targeted diff.
- **Scope of who re-reviews.** All reviewed notes of the type, or only pairs whose gate is type-specific (`requires-type` set). A generic prose gate may not care that the type's guidance changed; scoping to type-dependent gates cuts re-review fatigue.

## Adoption criteria

Adopt when:

- editing a type-spec's authoring guidance marks exactly the notes of that type stale, for exactly the gates whose judgment depends on the type — and nothing else;
- a schema-only tightening the validator already fails does **not** also trigger a redundant judgmental re-review;
- the new reason surfaces in the selector with an actionable diff of what in the contract changed, the way `note-changed` reconstructs a note diff today;
- a high-reach base-contract edit has a deliberate, bounded blast radius rather than silently invalidating the whole corpus.

## Risks

- **High-reach invalidation.** A widely-used type-spec — or a root contract — floods the review queue on one edit. Mitigation: scope to type-dependent gates; treat base-contract edits as a deliberate, acknowledged sweep.
- **Double-counting with validation.** Hashing schema files into the contract re-reviews changes the validator already enforces. Keep the split: schema → validate, prose guidance → review.
- **Contract creep.** If "contract" grows to every transitively-referenced file, freshness turns noisy and readers learn to ignore `contract-changed`. Bound it to the judgmental surface.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the mechanical/judgmental split is why schema changes stay with the validator (checked-or-absent) and only the judgmental part of the contract widens review freshness
- [The link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: a type-spec edit is the high-reach, low-file-count revision this note warns about, and modeling it as a freshness input is the make-like invalidation edge that catches it
- [Distilled artifacts need source tracking](../../notes/distilled-artifacts-need-source-tracking.md) — rationale: a reviewed note is judged against its type contract, and that dependency must be recorded somewhere that fires when the contract changes, or the change names nothing
- [Lineage](../../notes/definitions/lineage.md) — defined-in: the type-spec→note dependency this proposal models is a lineage edge — a review-relevant source dependency that must invalidate on change
