---
description: "Formal symbolic systems assess explanatory-reach only after claimed generality is translated into causal or proof obligations inside a warranted model"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# Formal symbolic systems assess explanatory-reach only through causal and proof obligations

[Reach-assessment](./definitions/reach-assessment.md) is not intrinsically an LLM-only or prose-only capability. A formal symbolic system can contribute to reach-assessment only when the candidate commitment's claimed generality has been translated into an obligation the system can check. That obligation might be a causal mechanism that should survive interventions or environment shifts, an identifiable causal effect under stated assumptions, or a theorem over a formally specified domain.

The shift is from asking "does this sentence sound like a good generalization?" to asking "what formal consequence must hold if this generalization is genuine?" Formal machinery can then check modeled consequences. It does not by itself prove that the model faithfully captures the original prose claim.

## The causal route

Causal theories have explanatory-reach because they do not merely fit one observed distribution. A structural causal model states mechanisms whose implications extend to interventions and counterfactuals. [Causal representation learning](../sources/towards-causal-representation-learning.ingest.md) frames this as the difference between statistical models of one distribution and causal models that represent distributions under possible interventions.

That is the route formal reach-assessment can use: a proposed commitment is accepted not because it predicts the training cases, but because the mechanism it asserts supports the intended intervention, counterfactual, or shift claims. [Invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) tests whether candidate predictors keep their predictive relation across environments and interventions — a predictor that holds across environments A and B but breaks once environment C is included gets flagged as non-invariant and excluded from retention, rather than accepted on A/B fit alone. [Causal-learn](../sources/causal-learn-causal-discovery-in-python.ingest.md), a Python library for causal discovery, collects algorithms that infer causal structure from observational data under method-specific assumptions. [DoWhy](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md), a causal-inference library, makes the same boundary operational by requiring declared assumptions before identification, estimation, and partial validation or refutation tests.

So a system that learns by causal theories can have reach-assessment, but the warrant is assumption-relative. It must represent the candidate theory, the target intervention or counterfactual class, the discovery or identification assumptions, and the acceptance tests that distinguish mechanism from correlation. Three of those assumptions recur across the literature: causal sufficiency (no relevant unobserved common causes among the modeled variables), latent confounding (the failure mode where hidden common causes remain), and do-calculus (the rule system for deriving intervention effects from a supplied causal graph). Naming them does not remove the need to justify the graph, variables, and assumptions they depend on.

## The proof route

Proof is a second formal route. If a candidate commitment can be expressed as a theorem, invariant, type property, model-checking obligation, or utility comparison over a specified domain, proof search can establish explanatory-reach across that domain. Model checking means exhaustively checking a property over the states or transitions of a formal model. The result is genuine reach-assessment inside that model: the evaluator checks not just sampled cases, but the claim's quantified consequence.

[Jürgen Schmidhuber's Gödel-machine proposal](../sources/goedel-machines-schmidhuber.ingest.md) is the useful placement example. It is not evidence for causal discovery and not evidence that theorem provers can judge arbitrary prose. It is a proof-gated host architecture: a candidate self-rewrite is accepted only when the machine proves the target theorem that switching now yields higher axiomatized utility than continuing proof search, under the current axioms and utility function.

That means the [Gödel machine note](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) fits the reach-assessment story conditionally. If its axioms included the relevant causal assumptions and its utility function rewarded correct intervention or counterfactual generalization, the proof gate could in principle license adopting a causal-theory learner, graph, or inference rule. Without those causal axioms and objectives, the Gödel machine contributes only the proof-gated acceptance rule.

## The formalization boundary

The formal routes move judgment upstream rather than abolishing it. A proof shows that a theorem follows from axioms; it does not show that the variables, domain, or utility function are the right representation of the original claim. Causal inference gives assumption-relative warrant; it does not globally validate causal truth from observations alone.

A theorem over the wrong variables can pass every proof obligation while missing the intended commitment. An invariant relation selected from narrow environments can look stable while tracking an artifact of sampling rather than a causal mechanism. Those are not failures of proof or do-calculus; they are failures in the translation from the prose explanatory-reach claim to the formal obligation, [which is why warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

The prose case remains different. A natural-language claim whose explanatory-reach has not been reduced to causal or proof obligations still needs semantic judgment about what the claim means and where it breaks. Current LLM-mediated review appears to supply some of that judgment, but this note does not explain why. The point is narrower: once explanatory-reach is represented as formal obligations, traditional symbolic systems can assess it within their modeled domain.

---

Relevant Notes:

- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: vocabulary this note develops into causal and proof obligations
- [Representational form](./definitions/representational-form.md) — grounds: explains why prose, symbolic, and parametric commitments expose different review methods
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: proof-gated acceptance of a symbolic self-rewrite
- [Reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) — evidence: connects reusable causal mechanisms to transfer under structured shifts
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: formal guarantees remain bounded by the oracle or axiomatization that produces them
- [Schmidhuber, Gödel Machines](../sources/goedel-machines-schmidhuber.ingest.md) — evidence: proof-gated host architecture and its unprovable-improvement limitation
- [Causal inference using invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) — evidence: invariance across environments and interventions as a causal acceptance signal
- [Towards Causal Representation Learning](../sources/towards-causal-representation-learning.ingest.md) — evidence: causal models support intervention and counterfactual generalization beyond one observed distribution
- [Causal-learn: Causal Discovery in Python](../sources/causal-learn-causal-discovery-in-python.ingest.md) — evidence: causal discovery under explicit method assumptions
- [DoWhy: Expressing and validating causal assumptions](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) — evidence: assumption declaration and partial validation
