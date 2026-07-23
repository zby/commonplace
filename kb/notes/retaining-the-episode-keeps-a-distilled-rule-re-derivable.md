---
description: "The episode a lesson was learned in and the rule distilled from it are complementary retention layers: with the episode retained and lineage recorded the rule stays evidence-backed and re-derivable; without it the rule hardens into a bare commitment"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, synthesis]
tags: [agent-memory, learning-theory, context-engineering]
---

# Retaining the episode keeps a distilled rule re-derivable

A lesson learned in operation admits two explicit retention forms. The **episode** is the trace of the situation the lesson came from — a session transcript, an execution trace, a worked case. The **rule** is the distilled statement of the lesson, separated from its occasion. Memory designs tend to treat these as rivals — episodic stores versus extracted facts — but they are layers of one system, and the choice that matters is not which to keep but whether the pair stays linked.

Linked, the pair instantiates a [two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) at artifact scale: the rule is the derived fast path — action-shaped, cheap to load, strictly narrower than what the episode contains — and the episode is the generator-side evidence a consumer drops back to when the rule's coverage fails or its scope is contested. That fallback is what the title names. A challenged rule with its episode retained and lineage recorded can be re-derived: read the episode again, judge whether the generalization survives, revise its scope from evidence. This is semantic re-derivation under the managed-staleness regime, not deterministic recomputation — but it is real recourse. A rule whose episode is gone has none: it can be trusted or discarded, never re-examined against what taught it. Discarding the episode converts the rule from an evidence-backed derivation into a bare commitment, and [an upstream change can then name no downstream worklist](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) because the dependency record died with the source.

## Distillation is earned by recurrence

The timing of distillation is a lifecycle question, not a storage preference. A rule distilled from a single episode is a conjecture that has skipped its test: the [discovery lifecycle](./definitions/discovery-lifecycle.md) places one surprising case at observation and the posited generalization at conjecture, with acceptance gated on accumulated cases. Retaining the episode first and distilling on recurrence respects those phases — the episode store is where candidate generalizations wait for their second and third occurrence, and recurrence is the same promotion signal the two-layer architecture uses to grow a fast path. Distill-on-first-occurrence fixes a generalization exactly when the evidence for its scope is thinnest.

## What distillation sheds, and where each layer wins

Distillation keeps the articulable part of a lesson and sheds the rest. The residue — calibration, situational feel, what a counterpart means by their words — is competence the episode still carries latently, because replaying an episode into context partially re-induces the conditioned state that held the lesson, while no statement of the rule can. The episode is the explicit trace of a tacit state, and the loss direction follows from [only explicit retention being durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md): the rule is the more addressable object, the episode preserves more of what resisted articulation. The practical familiar form of this asymmetry is that worked examples routinely outperform stated instructions for style- and calibration-shaped competence.

Governability runs the other way. Rules collide detectably — two contradictory statements can be noticed at write time — and are individually citable, revisable, and retirable. Episodes teaching opposite lessons coexist silently, and no lesson inside an episode can be revised; it can only be annotated or re-distilled. So governance lives at the rule layer, evidence and residue at the episode layer — a division of labor, not a contest. Between the raw trace and the bare rule sits a spectrum of intermediate forms — the cleaned worked trace, the rule with its attached example — and the residue share of a lesson's value is a guide to where on that spectrum it should be retained.

## Costs the pair must manage

- **Loading.** Retaining episodes is a capture posture, not a context posture: [persistence and loading are separate decisions](./session-history-should-not-be-the-default-next-context.md), and [evidence can be preserved without becoming the next context](./agent-memory-requirements/preserve-evidence-without-loading-history.md). Rules load by default because [a fast path should carry answers, not work](./frontloading-spares-execution-context.md); episodes load on demand — scope disputes, re-derivation, residue-heavy tasks.
- **Model relativity.** An episode's lesson is a joint product of the trace and the model that reads it; replay under different weights re-conditions differently. Episode retention therefore carries a quiet selection-grade dependency on the parametric form — faithful replay pins the reader — while a rule is comparatively model-portable. The [operation-profile vocabulary](./reflective-coverage-is-graded-across-representational-forms.md) makes the dependency statable.

## Scope

- Which episodes to keep at all is the inclusion question, and it belongs to the [declared output spec](./open-domain-memory-retention-needs-a-declared-output-spec.md); this note owns the form question — given a lesson worth keeping, in which layer its value survives.
- Nothing here claims raw transcripts are the right episode form; the claim is that some episode-grade record must survive distillation for the rule to remain re-derivable.

## Open Questions

- Eviction: episodes accumulate linearly with operation; what retires one — the promotion of its lesson, a staleness horizon, or contradiction by later episodes?
- Recall: the rule layer is findable by statement; what routing lets an agent find the episode it needs when the rule's scope fails?
- How much residue actually survives replay, and how it degrades across model versions, is measurable and unmeasured.

---

Relevant Notes:

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — exemplifies: the episode/rule pair as a generator/fast-path instance at artifact scale, with recurrence as the shared promotion signal
- [Only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: the tacit-residue direction that decides what distillation sheds and which lessons belong nearer the episode end
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — grounds: the dependency record that keeps the pair a pair
- [Discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: the phase model that places a single-episode rule at conjecture rather than acceptance
- [Session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — grounds: the persistence/loading split that makes episode retention affordable
- [Preserve evidence without making history the next context](./agent-memory-requirements/preserve-evidence-without-loading-history.md) — extends: the capture-side practice this claim supplies the re-derivability rationale for
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: why the rule layer carries answers and loads by default
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: the profile vocabulary that states episode replay's selection-grade dependency on the reader model
- [Open-domain memory retention needs a declared output spec](./open-domain-memory-retention-needs-a-declared-output-spec.md) — contrasts: owns the inclusion criterion; this note owns the form question
