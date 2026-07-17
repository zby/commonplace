# Workshop: Theory–Methodology Derivation

## Question

What is the general structure behind "a theory ships with a derived, action-shaped methodology" — and should **derivation** become a KB vocabulary term, possibly restructuring what we now call distillation?

## Provenance

Started 2026-07-17 from a conversation that began as a terminology check: an external passage used "crystallization" / "progressive crystallization", which is not current vocabulary ([source-passage.md](./source-passage.md) preserves it with the mapping to current terms). Unpacking the passage surfaced several connected threads that are explored here in separate files so each can move at its own pace.

## Status (2026-07-17)

The audit is done, the direction is decided (retire the term, no successor), and the first semantic wave — the obvious discovery/abstraction cluster, the original mistake — is applied and committed; see the [execution status](./migration-plan.md#execution-status-2026-07-17). The scope/collision reflection this workshop triggered has been promoted to the library as `kb/notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md`. **Wave 0 is complete**: the two-layer structure note is promoted (`kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md`, all ten hard-case rows classifying cleanly against it), the derived/abstracted lineage semantics are in the link grammar (`kb/reference/link-vocabulary.md`, with `cp-skill-write` updated), and the discovery lifecycle is defined (`kb/notes/definitions/discovery-lifecycle.md`). The draft's six pre-Wave-1 acceptance tests pass. The open front is Wave 1: the entangled semantic cases and legacy lineage-edge classification — see the [execution status](./migration-plan.md#execution-status-2026-07-17).

## Threads

- [two-layer-theory-methodology.md](./two-layer-theory-methodology.md) — the core structure: a general theory and a derived methodology form a two-layer execution system with fallback and promotion semantics; spec mining and the maturation trajectory are its symbolic-crossing special cases
- [derivation-selection-vocabulary.md](./derivation-selection-vocabulary.md) — the vocabulary proposal: derivation as entailment-preserving distillation; decompose distillation into consumer-directed selection + derivation, forcing the ampliative residue out to discovery; migration audit plan
- [learning-as-derivation-caching.md](./learning-as-derivation-caching.md) — the learning framing: promotion is caching derivations (amortization, not capability acquisition); proceduralization in cognitive architectures is the exact analogue
- [methodology-as-inductive-bias.md](./methodology-as-inductive-bias.md) — the ML framing: the methodology is a learned inductive bias; the exact-spec/proxy-theory split predicts which promotions are durable
- [effective-theory-borrowing.md](./effective-theory-borrowing.md) — the philosophy-of-science framing: the physics term cluster around effective theories (matching, cutoff, correspondence, UV completion) maps piecewise onto the two-layer structure; candidate hand-off to the [philosophy-borrowing](../philosophy-borrowing/README.md) workshop
- [polation-structure-of-generalization.md](./polation-structure-of-generalization.md) — Ord's interpolation/extrapolation/hyperpolation triple as the grading of the derivation/induction/discovery split; formalizes the bet doctrine and merges with the abduction borrowing
- [distillation-control-trap.md](./distillation-control-trap.md) — the migration warning: use-shaped artifacts feel controlled, but `distillation` hid whether the artifact is controlled by provenance, matching, discovery testing, or authored commitment
- [obvious-distillation-cases.md](./obvious-distillation-cases.md) — first staging pass over `kb/notes/` and `kb/reference/`: obvious discovery/abstraction fixes, obvious derivation/selection rewrites, deferred META surfaces, and mixed notes to hold back
- [distillation-usage-audit.md](./distillation-usage-audit.md) — evidence: 464 classified `distill*` instances across the KB; tallies, collisions, and migration mechanics
- [migration-plan.md](./migration-plan.md) — the decided direction (retire distillation with no successor term; theory in citable notes, boundary in link-label grammar) sequenced into waves: receiving surfaces, split entangled usages, mechanical rewording, infrastructure
- [receiving-vocabulary-draft.md](./receiving-vocabulary-draft.md) — Wave 0 working draft: candidate definitions for derivation and selection, the discovery amendment, the classification bet, and hard-case checks before semantic rewrites
- [prose-has-no-scope.md](../vocabulary-governance/prose-has-no-scope.md) (moved to the vocabulary-governance workshop; promoted 2026-07-17 to [vocabulary collisions are prevented at write time, not resolved at read time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md)) — the reflection thread: prose technical terms are unscoped globals and context assembly is concatenation without a linker, so sense collisions merge silently at composition; the remedy is prevention (one term, one sense, corpus-wide), not symbolic disambiguation — the mechanism behind this workshop's minimality constraint and no-successor-term end state

The threads connect through the first one: the structure note is the likely primary durable artifact, with the three framings feeding its argument and links, and the vocabulary thread deciding what terms the note is written in.

## What closes this workshop

1. A structure note in `kb/notes/` stating the two-layer theory–methodology pattern (generator, derived fast path, fallback, promotion-by-matching) in settled vocabulary.
2. The vocabulary migration executed or handed off: the direction is decided (retire `distillation` with no successor term — "derive" stays ordinary English, the theory lives in the structure note, the DER/AMP boundary lives in link-label grammar and gates; ampliative traffic to the polation-graded **discovery lifecycle**, the compound being the technical term with bare "discovery" ordinary; mixed cases carry a dominance bet) — see [migration-plan.md](./migration-plan.md). Closure requires Wave 0 (structure note, label semantics, and discovery amendment promoted) and Wave 1 (entangled usages split) done, with the mechanical waves either done or turned into a tracked instruction.
3. The effective-theory borrowing either promoted into the philosophy-borrowing workshop's candidate list or dropped.
4. The learning and inductive-bias framings either absorbed into the structure note's argument and Relevant Notes or extracted as their own notes if they carry independent claims.

## Bookkeeping

Working files are plain markdown, workshop register. Positions attributed to "current position" are where the originating conversation landed; open questions are genuinely open.
