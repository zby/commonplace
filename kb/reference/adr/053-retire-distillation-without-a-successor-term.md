---
description: "Distillation is retired with no successor term: theory lives in the two-layer structure note, lineage labels carry the derived/abstracted boundary, the discovery lifecycle owns ampliative traffic"
type: ../types/adr.md
tags: []
status: accepted
---

# 053-Retire distillation without a successor term

**Status:** accepted
**Date:** 2026-07-17

## Context

`Distillation` was a load-bearing vocabulary term — in the AGENTS.md vocabulary, a definition note, a tag in `learning-theory`'s `covered_by`, note titles, and the `Distilled into:` link label. A corpus audit (2026-07-17, recorded in `kb/work/theory-methodology-derivation/distillation-usage-audit.md`) classified 464 occurrences and found the word covering operations with opposite maintenance semantics: entailment-preserving reshaping (methodology → skill; the output is re-derivable from the retained source) and evidence-to-rule generalization (traces → preference rule; the output must earn authority through testing). The definition note's own instance list spanned the boundary, and the KB's most theoretically load-bearing "distill" usage — the trace→rule ladder — was on the ampliative side. Because the word did not mark which control regime governed an artifact, use-shaped artifacts could borrow the recomputable-copy maintenance story without holding its checkability.

Two theory results shaped the remedy. [Vocabulary collisions are prevented at write time, not resolved at read time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md): prose gives an unqualified technical sense no reliable namespace, co-loaded notes merge colliding senses silently, and a definition note binds too weakly to prevent drift — the `distillation` definition existed throughout the drift it failed to stop. And a minimality constraint: a technical term that is also a common English word taxes every future occurrence with a which-sense resolution, so a word earns a definition only when its operational consequences cannot be carried by plain prose with a citation. Applied strictly, a successor term `derivation` fails that bar — ordinary "derive" is close enough, and the strong sense can cite its theory directly.

## Decision

Retire `distillation` as KB vocabulary with **no successor technical term**.

- **"Derive" stays ordinary English.** No definition note, no vocabulary entry. A passage that needs the strong sense — entailment-preserving reshaping with matching, fallback, and cache/staleness semantics — cites the theory's home: [the two-layer execution system note](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md), which states those maintenance regimes as citable claims.
- **The link grammar carries the boundary.** `derived-from` / `Derived into:` asserts the artifact adds no substantive claims beyond its source and receives recomputable-copy or managed-staleness maintenance; `abstracted-from` / `Abstracted into:` asserts the claims exceed the instances and authority is earned by testing. Semantics are specified in [link-vocabulary.md](../link-vocabulary.md). An entangled artifact is classified by its dominant regime as an explicit, falsifiable bet.
- **Ampliative traffic routes to the discovery lifecycle.** The coined compound [discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) is the technical term for staged ampliative acceptance; traffic enters at its conjecture phase and never inherits accepted status from the sentence that states it. Bare "discovery" is ordinary English — completed by retitling the insight note to [conjecture is seeing the particular as an instance of the general](../../notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md), which removed the last title-level capture of the bare word.
- **`Distillation` survives only in** external systems' own command names, the machine-learning knowledge-distillation sense inside captured sources, and historical ADR text.

Implemented worked-case-first, per the wave plan in `kb/work/theory-methodology-derivation/migration-plan.md`: the receiving surfaces were promoted first (structure note, label semantics, lifecycle definition — all ten audit hard cases classifying cleanly against them), then the entangled usages were split (the trace→rule ladder renamed to abstraction vocabulary, `distillation-is-transformation-not-selection` retired, the tradeoff/lineage/rewrite trio retitled, ~16 mislabeled lineage edges flipped to `abstracted-from`), with the affected notes taken through full review-gate sweeps.

## Consequences

- **Easier:** an artifact's maintenance regime is readable off its lineage label instead of inferred from an overloaded word; the incoming technical term is a greppable multi-word coinage, so the write-time uniqueness check is a lexical search rather than the multi-agent semantic classification the 464-hit audit required; the derived/abstracted boundary is policed by labels and review gates, which prose demonstrably could not do.
- **Harder:** the KB's most common composite operation — consumer-directed selection plus reshaping — no longer has a one-word name and must be described in plain language with a citation where the strong sense matters. The resonance with ML knowledge distillation is lost deliberately: that sense is statistical fitting, and the borrowed intuition sat on the wrong side of the exact boundary the KB sense needed to hold. **Amended by [ADR 054](./054-add-adapted-from-and-operationalized-from-lineage-relations.md):** this gap proved real, not hypothetical — writers filled it with unauthorized ad-hoc synonyms ("condense," "Extraction") inside the same migration that retired `distillation` for exactly this failure mode. ADR 054 names the operation `adapted-from`/`operationalized-from`; this decision's other three bullets are unchanged.
- **Remaining churn, tracked not blocking:** the mechanical rewording of the remaining derivation/selection-shaped instances; the META surfaces — the AGENTS.md vocabulary entry, deletion of `kb/notes/definitions/distillation.md` with its salvage map (28 inbound links, including the `undefined-terms` gate's worked example), retirement of the `distillation` tag from `learning-theory`'s `covered_by`, the remaining `distill*` filenames, and this collection's own residue (ADR 011's hardcoded "directed context compression" gloss and the review-gate examples citing it). The `kb/agent-memory-systems` type-spec's `Distilled form:` field migrates on its own schedule.
- **Risk:** the control trap can recur under any future attractive label. The guard is the promoted invariant — load-bearing senses ride on schema positions, rare compounds, or link-required clausal binding, never on capturing a common word — and the label semantics that force every lineage edge to declare its regime.
