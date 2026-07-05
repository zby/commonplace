---
description: "Type-conformance review pairs put the note's type spec on the gate side of the existing (note, gate) freshness key, so a type edit stales exactly its cohort with no new storage semantics"
type: ../types/adr.md
tags: []
status: accepted
---

# 038-Type-conformance reviews use the type spec as the gate

**Status:** accepted
**Date:** 2026-07-04

## Context

A note's type binds it twice: structurally through the schema, which the deterministic validator checks, and semantically through the type spec's authoring instructions, which nothing checked. Editing a type's authoring bar could silently invalidate every note of that type with no mechanism that noticed.

The check could not be an ordinary review gate. A gate that restates the type contract is a derived copy that drifts; a gate that leans on the type spec carries a dependency the freshness hash never sees — review freshness compares exactly two snapshots, note text and gate text ([ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md)), so a type edit changes neither and every acceptance stays falsely fresh.

The design was worked out in the proposal `type-change-invalidation-via-type-spec-as-gate`, which this ADR supersedes; its unadopted remainder — the factored-pairs generalization and a cohort-scoped ack — continues as [factored dependency pairs for review freshness](../proposals/factored-dependency-pairs-for-review-freshness.md). The rejected alternative — watching the type spec as a third input on other gates' pairs — required a third acceptance column, taught ack a new input shape, and left the trivial-ack path to be rebuilt.

## Decision

Stop treating the type contract as an input to some other gate and make it the gate. For each note, one *type-conformance pair* `(note_path, type_spec_path)` is derivable, whose gate side is the type spec named by the note's `type:` frontmatter.

- **Pairs derive from note frontmatter, not the gate catalog.** Type-conformance pairs enter through a second gate source: the selector accepts `type` (all typed notes in scope) and `type/{name}` (one type's cohort) alongside catalog gate ids and derives one pair per note from its resolved `type:` path. `requires-type` filtering is not involved.
- **The gate id is the virtual `type/{name}` lens; the persisted identity is the type-spec repo path.** Acceptance stays path-keyed; the shorthand is derived for display and CLI input, uniform with `{lens}/{name}` catalog ids. `type/{name}` resolves to the global `kb/types/{name}.md` when present, else to a unique collection-local `kb/**/types/{name}.md`.
- **Everything downstream of pair derivation is the existing machinery, unchanged.** The role-neutral snapshot table stores type-spec text like any gate text; a type edit flips `gate-changed` for exactly the cohort of notes of that type; a note edit flips `note-changed`; `commonplace-ack-gate-review` re-pins the current type-spec snapshot for trivial type edits. No new selector reason, no new acceptance semantics, no storage change.
- **A mechanical wrapper renders type specs as gates.** Type specs are authoring instructions plus a template, not a Failure mode / Test procedure, so the prompt renderer prepends a fixed conformance wrapper: judge whether the note does what the authoring instructions ask, PASS/WARN/FAIL semantics, structural checks excluded as the validator's job. The wrapper is prompt scaffolding outside the freshness hash and must stay mechanical — conformance criteria that need sharpening go into an authored `## Review` section of the type spec, where the hash sees them (the wrapper directs reviewers to treat such a section as the operative test).
- **The cohort is opt-in.** Type-conformance pairs are selected only when explicitly requested; `--all-gates` remains catalog-only. Early review cost stays proportional to the types whose authoring instructions carry real semantic bars.
- **Existing gates must stay self-contained.** A gate's operative test must be inlined in gate text; if it needs contract language, it quotes it, converting the dependency into hashed gate text. The type-conformance pair owns "does the note satisfy the contract"; type-scoped gates own their sharper, named failure modes, and state the boundary in gate text to avoid double-flagging.

## Consequences

Easier:

- Type-contract edits are no longer silent: editing a type spec stales exactly its cohort through the existing `gate-changed` path, with the gate-side diff available for triviality judgment.
- The missing semantic-conformance check exists at all: notes can be reviewed against what their type's authoring instructions actually ask.
- Trivial type edits are absorbed by the existing ack command with no new mechanism, because the type spec *is* the gate snapshot being re-pinned.
- The pattern generalizes by factoring: a new review dependency becomes a new two-input pair with the dependency document on the gate side (`COLLECTION.md`-as-gate, source-as-gate), reusing the whole freshness/ack/warn stack, instead of widening one pair's input set to N.

Harder / accepted costs:

- Cohort blast radius: one type-spec edit stales every note of that type, and acking is per-note; a cohort-scoped ack surface is deliberately deferred until a real type edit makes per-note acking painful.
- Conformance reviews may be vague until a type spec carries an authored `## Review` section; the wrapper-prompted reviewer sets its own bar, and cross-model consistency may be poor. Model partitioning contains this but does not fix it.
- The wrapper joins the prompt scaffolding that is outside the freshness hash. The compensating rule (judgment-bearing criteria live only in hashed inputs) now carries more weight and is marked in the prompt and freshness modules.
- Gate self-containment is a discipline, not an enforcement: nothing stops a future gate from leaning on unhashed contract text. The guard is the review-gate authoring rule.
- Double-flagging between the conformance pair and type-scoped gates (a definition failing explication also fails its contract) is managed by boundary statements in gate text, which must be written as type cohorts opt in.

---

Relevant Notes:

- [032-review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) — extends: the role-neutral snapshot substrate that lets a type spec sit on the gate side without schema change
- [012-types for structure, traits for review](./012-types-for-structure-traits-for-review.md) — extends: the type/trait boundary, making the type contract itself reviewable
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why the gate must be the type spec rather than restate it
- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the build-product/prerequisite model; factored two-input pairs are its cheapest review-side realization
- [review system](../README-REVIEW-SYSTEM.md) — part-of: the operator-facing concepts the conformance pair reuses unchanged
- [review architecture](../review-architecture.md) — part-of: the code architecture carrying the second gate source and the wrapper's freshness-boundary rule
