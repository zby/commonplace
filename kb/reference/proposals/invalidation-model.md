---
description: "Proposal: unify Commonplace's mechanical (validate) and judgmental (review-freshness) invalidation into one model that says which regime owns a given definition change and its full contract"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# An invalidation model with two regimes

When a definition changes — a type-spec, a gate, a schema — artifacts written under the old definition may no longer conform. Commonplace already handles this piecemeal: the validator re-checks schemas, review freshness re-checks gates, and nothing re-checks a type-spec's prose guidance. There is no named model that says, for a given definition change, *which mechanism should carry it* and *what the full set of artifacts and inputs is that the change should invalidate*. This proposal holds a design object: one invalidation model with two regimes, split by whether staleness is cheaply checkable, plus a placement rule that assigns each definition change to a regime and names its contract. The concrete review-freshness widening is the first instance decided against it.

## Current state (as of 2026-07-02)

- **Mechanical regime — validation.** `commonplace-validate` is stateless and always-current: each run re-resolves a note's type contract and re-validates against the current schema. No baseline is stored, so nothing goes stale — a tightened `.schema.yaml` fails every non-conforming note on the next run. The only missing piece is a *trigger* to run the sweep after a type is edited.
- **Judgmental regime — review freshness.** The review subsystem stores an accepted baseline and detects staleness by SHA-256. Each accepted `(note, gate)` review pins the note and gate text, keyed `(note_path, gate_path, model_partition)`, and the selector reports `missing-review`, `gate-changed`, or `note-changed`. Editing a gate invalidates via `gate-changed`. Described in [review-architecture.md](../review-architecture.md).
- **The two are disjoint but unnamed.** They cover different definition changes and never overlap, but nothing states the model. A maintainer editing a type-spec has no rule that tells them the schema half propagates for free while the guidance half propagates through nothing.
- **The general model is under exploration.** The lineage workshop owns the general derived-artifact model and already lists the narrow-contract gap as open tension 13. This proposal promotes just the invalidation slice into a decidable design object.

## The design

**Two regimes, split on checkability.**

| regime | mechanism | staleness state | owns |
|---|---|---|---|
| Mechanical | `commonplace-validate` | none — recomputed every run ([checked-or-absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)) | definition changes a machine can verify: required fields, enums, `type` const, required-section headings |
| Judgmental | review freshness | stored accepted baseline + hash compare | definition changes needing a reviewer: gate lenses, and the semantic authoring guidance a type-spec carries |

**Placement rule.** A definition change is owned by the regime that can verify conformance. Schema-checkable → mechanical (propagates for free, no state). Semantic/guidance → judgmental (needs a stored baseline and a re-review). Splitting this way keeps one edit from being double-counted as both a validation failure and a re-review.

**Each judgmental review has a contract.** The contract is the full set of inputs whose change should invalidate the review — today only the note and the leaf gate. A note is also judged against its resolved type-spec, so a type-definition change *should* invalidate but does not. Closing that specific gap is [review freshness should track the full review contract](./review-freshness-tracks-the-full-contract.md); this proposal is the frame it sits in.

## Free choices

- **Whether to name/unify at all.** Leave the two subsystems separate and undocumented, or ship the model as reference so definition-editors can reason about propagation. Naming has value only if edits to definitions are frequent enough to need the rule.
- **How much contract to model per class.** The judgmental contract could stay `{note, gate}`, grow to include the type-spec guidance, or grow further to base specs and transitively-referenced files. More is more correct but higher-reach.
- **Whether the mechanical trigger belongs here.** Auto-running validation after a type-spec edit (so the mechanical half does not wait for a manual sweep) could be part of this model or a separate tooling concern.
- **Relationship to the lineage workshop.** This can promote out of the workshop as a standalone invalidation model, or stay a sub-case of the general derived-artifact lineage model until that converges.

## Adoption criteria

Adopt when:

- someone editing any definition can tell from the model which regime carries the change, and what it will and will not invalidate, without reading source;
- the mechanical/judgmental split is explicit enough that no single edit is counted in both regimes;
- the model accommodates the concrete review-freshness widening as its first worked instance rather than contradicting it;
- if promoted to shipped reference later, it describes behavior that actually ships (the contract-widening must land first, or be marked as not-yet-shipped).

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the mechanical/judgmental split is this note's claim applied — mechanical staleness is checked for free, judgmental staleness needs a stored baseline
- [The link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the judgmental regime is make-like — a stored baseline plus a change signal that flags what to re-review rather than auto-rewriting it
- [Lineage](../../notes/definitions/lineage.md) — defined-in: both regimes track the review-relevant dependency edges a definition change must invalidate
