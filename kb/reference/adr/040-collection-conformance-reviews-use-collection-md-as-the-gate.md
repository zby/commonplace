---
description: "Collection-conformance pairs put the note's COLLECTION.md on the gate side of the existing (note, gate) freshness key, matching the enforcement type contracts got in ADR 038"
type: ../types/adr.md
tags: []
status: accepted
---

# 040-Collection-conformance reviews use COLLECTION.md as the gate

**Status:** accepted
**Date:** 2026-07-08

## Context

A note is bound by two authored contracts: its type spec and its collection's `COLLECTION.md` ([ADR 017](./017-collection-md-is-the-register-convention-boundary.md)). [ADR 038](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) made the type contract semantically enforceable by putting the type spec on the gate side of the existing `(note, gate)` freshness pair. The collection contract had no equivalent: ADR 017 conceded that "register correctness is not a deterministic validation check" and left it as an unenforced writing concern, and editing a `COLLECTION.md` invalidated nothing.

The asymmetry is not just a coverage gap; it distorts contract design. When the type surface is the only prose contract with enforcement, clauses migrate to where the machinery is rather than where their scope says they belong — a convention that binds *everything in a collection* gets pushed into a type spec so that something checks it. Symmetric enforcement is what lets the collection/type split be decided by scope (what set of artifacts a clause binds) instead of by which surface happens to have teeth.

The mechanism was already designed: [factored dependency pairs](../proposals/factored-dependency-pairs-for-review-freshness.md) names `COLLECTION.md`-as-gate as the next factored pair, and ADR 038's consequences list it as the generalization path. The snapshot table is role-neutral ([ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md)), so any repo document can sit on the gate side with no storage change.

## Decision

For each note, one *collection-conformance pair* `(note_path, collection_md_path)` is derivable, whose gate side is the `COLLECTION.md` of the nearest collection containing the note.

- **Pairs derive from note location, not the gate catalog.** The selector accepts `collection` (all notes in scope that live in a collection) and `collection/{path}` (one collection's cohort) alongside catalog gate ids and the `type` lens, and derives one pair per note from its position in the collection tree. A note outside any collection has no pair; a `COLLECTION.md` is contract, not content, and never pairs with itself.
- **The gate id is the virtual `collection/{path}` lens; the persisted identity is the COLLECTION.md repo path.** `{path}` is the collection directory relative to `kb/`, so collections under a non-collection namespace stay unambiguous: `collection/notes` names `kb/notes/COLLECTION.md`, `collection/commonplace/notes` names `kb/commonplace/notes/COLLECTION.md`. Collections do not nest — a `COLLECTION.md` inside another collection is invalid and the validator rejects it — so in a valid repo the nearest contract above a note is the only one. Acceptance stays path-keyed; the shorthand is derived for display and CLI input.
- **Everything downstream of pair derivation is the existing machinery, unchanged.** The role-neutral snapshot table stores the contract text like any gate text; a `COLLECTION.md` edit flips `gate-changed` for exactly the notes in that collection; a note edit flips `note-changed`; `commonplace-ack-gate-review` re-pins the current contract snapshot for trivial edits. No new selector reason, no new acceptance semantics, no storage change.
- **A mechanical wrapper renders the contract as a gate, referencing rather than embedding it.** A `COLLECTION.md` is authoring conventions and routing rules, not a Failure mode / Test procedure, so the prompt renderer emits a fixed conformance wrapper: judge whether the note follows the collection's authoring conventions (placement, title and description conventions, quality goal, outbound linking rules), PASS/WARN/FAIL semantics, structural checks excluded as the validator's job. The wrapper names the contract's repo path and the worker reads it from disk, exactly as ADR 038's amended wrapper does for type specs. Conformance criteria that need sharpening go into an authored `## Review` section of the `COLLECTION.md`, where the freshness hash sees them; the wrapper directs reviewers to treat such a section as the operative test.
- **Boundary against the type-conformance pair.** The wrapper instructs the reviewer to judge only what the collection contract asks beyond the type contract; the type spec is the type-conformance pair's gate. This is the double-flagging boundary ADR 038 required stated in gate-side text, placed in the wrapper because the split is mechanical scope, not judgment criteria.
- **`--all-gates` includes the cohort.** The flag keeps its ADR 038 meaning — "every applicable review criterion for the selected notes" — expanded by the one shared helper: all catalog gates plus the virtual `type` and `collection` requests. Auto-ack of trivial note changes selects collection pairs under the same flag but never acks one, by that command's own rule: a `COLLECTION.md` declares no `watches:`, so it watches the whole note and no change is trivial against it.

## Consequences

Easier:

- Collection-contract edits are no longer silent: editing a `COLLECTION.md` stales exactly its collection's notes through the existing `gate-changed` path, with the gate-side diff available for triviality judgment.
- The register/conventions check ADR 017 deferred ("unless future review gates are added") exists: a note can be reviewed against what its collection's contract actually asks.
- Enforcement is symmetric across the two contract surfaces, so where a clause lives can be decided by its scope — collection for location-bound clauses, type for kind-bound clauses — rather than by which surface is enforced.
- The factored-pairs pattern is proven twice with zero storage change, strengthening the default answer to the next review dependency (source-as-gate) being another two-input pair.

Harder / accepted costs:

- Cohort blast radius exceeds the type case: one `COLLECTION.md` edit stales every note in the collection, and acking is per-note. This sharpens the [cohort-scoped ack](../proposals/factored-dependency-pairs-for-review-freshness.md) case; it stays deferred until a real edit makes per-note acking painful.
- Conformance reviews may be vague until a `COLLECTION.md` carries an authored `## Review` section; the wrapper-prompted reviewer sets its own bar. Same containment as ADR 038: model partitioning limits but does not fix this.
- `COLLECTION.md` files carry no frontmatter, so unlike catalog gates they cannot declare `watches:` or gate metadata; all filtering is positional. Accepted — the contract is collection-shaped by construction, and `requires_trait`/`requires_type` filtering has no meaning for it.
- The overlap between a collection contract and the type specs it hosts (a collection-local type restating a collection convention) is managed by the wrapper's boundary statement plus the existing derived-copy rule: contract language lives in exactly one of the two documents and the other references it.

---

Relevant Notes:

- [038-type-conformance reviews use the type spec as the gate](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — extends: the factored-pair mechanism this ADR instantiates for the second contract surface
- [017-COLLECTION.md is the register convention boundary](./017-collection-md-is-the-register-convention-boundary.md) — extends: the collection contract this ADR makes reviewable; its deferred register-correctness check now exists
- [012-types for structure, traits for review](./012-types-for-structure-traits-for-review.md) — extends: with both conformance pairs shipped, semantic enforcement attaches to contract surfaces generally, not to traits alone
- [factored dependency pairs for review freshness](../proposals/factored-dependency-pairs-for-review-freshness.md) — part-of: the proposal whose COLLECTION.md-as-gate item this ADR adopts; source-as-gate and cohort-scoped ack remain open there
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why the gate must be the COLLECTION.md rather than a catalog gate restating it
- [review architecture](../review-architecture.md) — part-of: the code architecture carrying the collection gate source and the shared wrapper rules
