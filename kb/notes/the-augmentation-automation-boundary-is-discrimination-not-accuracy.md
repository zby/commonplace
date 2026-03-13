---
description: Crossing from augmentation to automation requires per-instance discrimination, not aggregate accuracy — discrimination is empirically stagnant, so scaling capability alone cannot cross the boundary
type: note
traits: [has-external-sources]
tags: [llm-interpretation-errors]
status: seedling
---

# The augmentation-automation boundary is discrimination not accuracy

A 90%-accurate agent with poor discrimination is fine as augmentation — the human catches the 10%. The same agent is dangerous as automation — nobody catches it. **The boundary between augmentation and automation is not accuracy but discrimination — the ability to know, per instance, whether this particular output is likely wrong.**

This distinction matters because accuracy and discrimination improve on different tracks. Scaling model capability reliably improves aggregate accuracy. It does not reliably improve per-instance discrimination ([Rabanser et al.](../sources/towards-a-science-of-ai-agent-reliability.md) confirm this empirically; see below). If the boundary depends on the dimension that isn't improving, then capability scaling alone cannot cross it.

## Accuracy vs discrimination

The [error correction note](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) makes this distinction precise. An oracle has discriminative power when TPR > FPR — it is more likely to accept correct outputs than incorrect ones. Aggregate accuracy can be high with zero discriminative power: an oracle that always says "accept" has 90% accuracy when 90% of outputs are correct, but TPR = FPR = 1.0, and no amount of repetition helps.

This maps directly onto the augmentation/automation boundary:
- **Augmentation** requires only aggregate accuracy. The human provides the discrimination — reviewing outputs, catching errors, deciding when to trust.
- **Automation** requires per-instance discrimination. Since no human is checking, the system must either (a) self-assess — use its own confidence as an oracle to flag uncertain outputs — or (b) be verified by an external oracle with discriminative power (test suites, schema validation, formal checks).

These two routes have very different scaling properties, and the empirical evidence on discrimination determines which is viable.

## Discrimination is empirically stagnant

The [Rabanser et al. study](../sources/towards-a-science-of-ai-agent-reliability.md) evaluated 14 models across 18 months of releases and found a striking asymmetry: **calibration improves but discrimination does not.** Calibration is aggregate alignment — when a model says "80% confident," it is right roughly 80% of the time. Discrimination is per-instance separation — whether the model assigns higher confidence to its correct outputs than to its incorrect ones. These are independent properties: a model can be perfectly calibrated yet assign the same confidence to every output, providing zero signal about which specific outputs are wrong.

This asymmetry closes off route (a). Even with improving calibration, the model's confidence score cannot reliably separate correct from incorrect outputs at the individual level. An approval gate based on confidence thresholds produces better-calibrated aggregate rejection rates but does not get better at catching the specific outputs that are wrong.

The implication extends to error correction. The [TPR > FPR condition](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) for oracle amplification depends on discrimination, not calibration. If discrimination stagnates, confidence-based voting plateaus — no amount of repetition overcomes an oracle with TPR ≈ FPR, regardless of how well-calibrated the aggregate distribution is.

## External oracles bypass the discrimination bottleneck

In the [oracle-strength vocabulary](./oracle-strength-spectrum.md), discrimination maps directly to self-assessment oracle strength. A model with high discrimination has a soft oracle for its own correctness — it can flag uncertain outputs for human review or automated re-checking. A model with low discrimination has no oracle for its own correctness — its confidence scores are noise, regardless of calibration.

This explains why automation already works in narrow domains despite poor general discrimination: **route (b) — external hard oracles — bypasses self-assessment entirely.** Code execution has test suites. Arithmetic has exact verification. Structured data has schema validation. In each case, the oracle is constructed externally rather than derived from the model's self-knowledge. The [MAKER paper](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) achieves zero errors over a million steps precisely because every sub-task has a deterministic oracle — the system never needs the model to know when it is wrong.

The augmentation/automation boundary is therefore not a fixed accuracy threshold but a function of available oracle strength:
- **External hard oracle available** → automation is viable regardless of model discrimination (route b)
- **Only self-assessment available, high discrimination** → automation with confidence-gated escalation (route a)
- **Only self-assessment available, low discrimination** → augmentation is the ceiling; the human IS the oracle

The practical consequence follows from the asymmetry. Discrimination is stagnant (Rabanser et al.), so route (a) has a ceiling that capability scaling does not lift. External oracle construction, by contrast, is an engineering activity — spec mining, test suites, structural validation, [behavioral contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md). The path to automation runs through route (b): building better external oracles, not waiting for models to develop self-knowledge.

## Open questions

- **Does discrimination improve with scale within a model family?** Rabanser et al. tested across releases, not within a single architecture at different scales. If discrimination is an emergent capability at sufficient scale, the stagnation finding may be temporary.
- **Is cooperative verification a third route?** One model checking another's output might achieve discrimination gains through diversity even when individual models cannot self-assess. The [decorrelation strategies](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) point in this direction, but the discrimination ceiling applies to each individual checker — diversity helps only if the checkers' errors are sufficiently decorrelated.

---

Relevant Notes:

- [reliability-dimensions-map-to-oracle-hardening-stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — deepens: this note extracts and develops the "predictability gap" paragraph from that note into a standalone claim about the augmentation/automation boundary
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — foundation: discrimination is oracle strength applied to self-assessment; the spectrum explains why narrow automation works (hard external oracles) while general automation stalls (no self-assessment oracle)
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: the TPR > FPR condition for amplification depends on discrimination, not calibration; stagnant discrimination means a plateau for confidence-based voting
- [Rabanser et al. reliability study](../sources/towards-a-science-of-ai-agent-reliability.md) — primary evidence: calibration improves but discrimination does not across 14 models and 18 months; the empirical basis for the stagnation claim
- [MAKER: million-step zero errors](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — exemplifies route (b): zero errors achieved not through self-assessment but through external hard oracles (deterministic per-step verification)
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — complements: (p,δ,k)-satisfaction parameterises oracle strength per constraint, providing a vocabulary for specifying the discrimination threshold required for automated recovery
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: unifies this note's discrimination mechanism with labor-economics and capability-timeline evidence into a general principle
