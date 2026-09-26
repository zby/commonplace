---
description: "Curated head for the evaluation tag — how claims, changes, and agent outputs are judged and tested: oracles and LLM judges, warrant versus theory fit, experiment and benchmark design, and evidence records from Commonplace review runs"
type: types/tag-readme.md
---

# Evaluation

This tag gathers how claims, changes, and agent outputs are judged and tested: oracles and LLM judges, what an evaluation warrants, the difference between a claim's warrant and its fit in a working theory, experiment, ablation, and benchmark design, and evidence records from Commonplace's own review and rewrite runs. No single defining note anchors it; [warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) states the constraint most members work under: an evaluation licenses action only over the candidates its oracle can assess. Members span notes, evidence records, reference docs and proposals, and system analyses. Nearby but different: [llm-reliability](./llm-reliability-README.md) covers why LLM output deviates from intent and how to correct it; a note belongs here when its question is what a check, judge, or experiment can establish. This head is selective; use a scoped tag search for full membership.

## Oracles and judges

- [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — autonomy is free, but warranted evaluation autonomy extends only as far as a confident oracle reaches
- [Evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — error analysis and demonstrated judge discrimination come before an automated loop can improve behavior rather than just score
- [Weakly discriminated qualities tend to be underselected](../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — conjecture: unequal oracle discrimination yields unequal enrichment under proposal selection
- [Reasoning production is not reasoning evaluation](../notes/reasoning-production-is-not-reasoning-evaluation.md) — a critic can reconstruct the answer instead of checking the reasoning, so process validity needs its own check
- [Review automation should target verifiable subroles before reviewer identity](../notes/verifiable-subroles-before-reviewer-identity.md) — decompose reviewer work into separately checkable parts before granting reviewer-level authority
- [A search controller is tested by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — provisional judgments route candidates to stronger checks; they are not acceptance claims
- [Brainstorming: pairwise comparison and soft oracles](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — a staged plan for testing whether pairwise judges improve discrimination, stability, and calibration

## Warrant and theory fit

- [A claim's warrant does not determine its fit in a working theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md) — warrant and fit answer different questions; either can hold without the other
- [System use provides evidence of theory fit, not independent warrant](../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) — live use tests integration and usefulness; factual, source, or scope evidence is still needed for warrant
- [System use is an initial selection environment when theory fit lacks a fixed oracle](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md) — distributed consequences of use can select claims where no fixed oracle exists
- [Disconnected witnesses do not establish a causal path through theory](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md) — evidence of learning through theory must join one causal path
- [Mixed epistemic status must be preserved below the document level](../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md) — observations, deductions, and plausible explanations keep their separate warrant inside one document

## Experiment and benchmark design

- [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — missing comparisons and bundle-to-component attribution overstate causal conclusions
- [A retained-theory intervention isolates one surface](../notes/retained-theory-intervention-isolates-one-explicit-surface.md) — intervening on retained theory estimates that surface's contribution, not whole-program theory possession
- [A benchmark that holds the client fixed exports the least-warrantable decisions](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) — fixed-client benchmarks measure worker capability and leave closure untested
- [Prompt ablation converts human insight into deployable framing](../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — controlled variation against a human-verified finding picks the framing agents can execute
- [Systematic prompt variation serves verification and diagnosis](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — varying prompts decorrelates checks or measures brittleness; it does not test explanatory-reach
- [Ablation baselines for the declared objective](../reference/proposals/ablation-baselines-for-the-declared-objective.md) — proposal: matched repository tasks with curated theory, review, or episodes removed
- [Trajectory-aware evaluation of transforming agent workflows](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — proposal: compare blinded output-only and trajectory-aware judges before adding trajectory checks

## Review evidence

- [Full improvement pass closure](../reference/full-improvement-pass-closure.md) — how the shipped workflow reassays final note bytes and stops without claiming convergence
- [A five-link cap missed four grounding findings in twelve reviews](../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — paired assay: fuller reading of linked artifacts surfaced findings the cap hid
- [An independent pass tightened three of four Pirolli grounding verdicts](../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md) — separating source reconstruction from claim judgment changed verdicts; a candidate control, not a proven cause
- [Single-artifact review bundles still cut Claude costs substantially](../notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md) — cache-weighted telemetry for the single-artifact bundle refactor
- [Three simplification passes exposed different clarity–precision tradeoffs](../notes/evidence/three-simplification-passes-exposed-different-tradeoffs.md) — broad style guidance, a compact cue, and exhaustive local review compared on one article

## Related Tags

- [llm-reliability](./llm-reliability-README.md) — why LLM output deviates and the correction machinery; oracle hardening sits on the boundary and many notes carry both tags
- [review-system](./review-system-README.md) — the shipped assay pipeline whose gates, verdicts, and runs several evidence records here measure
- [claims-and-grounding](./claims-and-grounding-README.md) — whether a claim is supported by its sources; the grounding-verdict evidence records belong to both
- [learning-theory](./learning-theory-README.md) — the parent area for how systems learn; warrant and fit notes feed it
- [self-improving-systems](./self-improving-systems-README.md) — improvement loops need oracles and evidence of improvement; warranted autonomy and theory-fit notes are shared
