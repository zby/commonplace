---
description: "Distinguishes next-token probability from factual truth and inferential validity: confidence can support correctness decisions only after task-specific validation, and high-assurance acceptance still needs a separate check"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, failure-modes, llm-reliability]
---

# Generation confidence does not by itself certify soundness

*Mixed status. The no-certification claim is deductive. The direction and strength of any confidence–soundness association are empirical, and the possibility of a reliable internal probe remains open.*

Here, an autoregressive language model's generation confidence means the conditional probability it assigns to a possible next token. That probability measures how likely the continuation is under the model's distribution. Soundness is a different property: whether a factual claim is true or an inference is valid. Unless a relation between these properties has been established separately, high probability does not entail soundness.

Probability may nevertheless provide useful evidence. For example, a model may assign more probability to “Paris” than to “Lyon” after “The capital of France is.” Whether such differences discriminate sound from unsound answers well enough for a particular use depends on the model's observed performance on that task.

The distinction covers both factual and inferential soundness. A false fact can be fluent, and an unsupported inference can read smoothly. The inference case appears in [the composition-friction loss](./llm-generation-relaxes-goals-where-human-writing-stalls.md): a human may stall at a weak “because,” but next-token probability does not perform the missing validity check.

## Any association must be measured

Across a defined evaluation population, confidence and soundness may be positively associated, unassociated, or negatively associated. Where correct continuations are more strongly represented than errors, probability may rank them above incorrect alternatives. Where misconceptions or common fallacies are more strongly represented, the ranking can reverse. Neither regime follows from the next-token objective alone.

Anti-correlation is therefore a separate statistical hypothesis. For a declared population of contexts and paired alternatives, it predicts that unsound continuations outrank sound alternatives more often than the reverse. Equal or opposite ordering refutes the hypothesis for that population. The deductive claim in this note supplies no prevalence evidence for a general anti-correlation claim.

## Validated confidence can support triage

When task-specific evaluation establishes adequate calibration and discrimination, confidence can prioritize review or trigger abstention. Aggregate calibration alone does not show that confidence distinguishes which individual outputs are wrong, as [reliability dimensions map to oracle-hardening stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) explains. Any use of confidence as a correctness signal inherits the scope and limits of that validation.

## High-assurance acceptance needs another operation

High-assurance acceptance still needs a separately validated operation: a compiler, test, proof checker, source-grounding check, or another verifier appropriate to the claim. A verbal self-assessment is another generated judgment, not a direct reading of the probability that produced the original answer. A separately trained detector, internal probe, or adversarial re-derivation may recover a distinct signal, but each must itself be validated; none is an independent verifier by construction. Whether models contain a reliably probeable internal representation of soundness remains open.

The boundary of reliable automation therefore tracks the [availability of a verifier](./the-boundary-of-automation-is-the-boundary-of-verification.md), not generation confidence alone.
