---
description: "Curated head for the failure-modes tag — recurring ways knowledge and claims in an agent-operated KB fail to do their job: stored but never activated, promoted without authority, over-generalized, or escaping review by widening or narrowing"
type: types/tag-readme.md
complete: true
---

# Failure modes

This tag gathers recurring failure modes of an agent-operated KB: ways knowledge and claims fail to do their job even though they exist on disk or have passed review. The anchor is [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), the distinction between knowledge existing, being loaded, and affecting behavior. The members cover four kinds of failure: activation failures (stored knowledge not discovered, loaded, or acted on), authority failures (content gaining binding force it was never granted), claim-repair escapes (a claim survives review by becoming vaguer, analytic, or immune to refutation), and lessons generalized past their evidence. Nearby but different: [llm-reliability](./llm-reliability-README.md) covers how a model deviates from instructions and evidence and how those deviations are corrected; a failure belongs here when the fault lies in how the KB stores, delivers, or states knowledge.

## Activation and delivery

- [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) — core distinction between knowledge existing, being loaded, and actually affecting behavior
- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) — content is promoted because the consumer will not apply it unprompted, so delivery needs a firing event that does not depend on that activation
- [A consumption channel delivers force without the history that earned it](../notes/a-consumption-channel-delivers-force-without-the-history-that.md) — a consumption path can raise content into a higher-force role without checking that an authorization covers that content, version, and use
- [Elicitation requires maintained question-generation systems](../notes/elicitation-requires-maintained-question-generation-systems.md) — inquiry processes decay when prompts stop generating discriminating questions

## Claim-repair escapes

- [Generality bought to avoid counterexamples is paid for in precision](../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — the widening escape from counterexamples: vocabulary abstracts, content stays flat, prose becomes unreadable
- [Narrowing bought to survive review is paid for in content](../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — the narrowing escape: shrinking a defeated claim's subject into its own predicate yields an analytic title that passes every gate
- [Domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) — names post-hoc immunization as the idealization escape's degenerate form and states the adequacy commitments that keep an idealized claim refutable

## Over-generalization and false assurance

- [Abstract an experience into a lesson only when you can state where the lesson stops](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — an over-generalized lesson is one that drops its condition clause; without a statable boundary, keep the instance
- [Generation confidence does not by itself certify soundness](../notes/generation-confidence-does-not-by-itself-certify-soundness.md) — next-token probability is not factual truth or inferential validity; high-assurance acceptance needs a separate check

## Related Tags

- [LLM reliability](./llm-reliability-README.md) — adjacent area: the deviation taxonomy and correction machinery for failures in how models interpret instructions and evidence
- [Evaluation](./evaluation-README.md) — methods for detecting whether failures are real and whether interventions improve behavior
