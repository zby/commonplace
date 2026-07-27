---
description: "Formal symbolic systems assess explanatory-reach only after claimed generality is translated into causal or proof obligations inside a warranted model"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# Formal symbolic systems assess explanatory-reach only through causal and proof obligations

[Reach-assessment](./definitions/reach-assessment.md) is not intrinsically an LLM-only or natural-language-only capability. A formal symbolic system can contribute to it once the candidate commitment's claimed generality has been translated into an obligation the system can check — a causal mechanism that should survive interventions or environment shifts, an identifiable causal effect under stated assumptions, or a theorem over a formally specified domain.

The shift is from asking "does this sentence sound like a good generalization?" to asking "what formal consequence must hold if this generalization is genuine?" What such a check establishes is bounded by the translation that produced it, which the last section takes up.

## The causal route

Causal theories have explanatory-reach because they do not merely fit one observed distribution. A structural causal model states mechanisms whose implications extend to interventions and counterfactuals; [causal representation learning](../sources/towards-causal-representation-learning.ingest.md) frames this as the difference between statistical models of one distribution and causal models that represent distributions under possible interventions.

That is the route formal reach-assessment can use: a proposed commitment is accepted not because it predicts the training cases, but because the mechanism it asserts supports the intended intervention, counterfactual, or shift claims. [Invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) tests whether candidate predictors keep their predictive relation across environments — one that holds across environments A and B but breaks once C is included is flagged as non-invariant and excluded, rather than accepted on A/B fit alone. [Causal-learn](../sources/causal-learn-causal-discovery-in-python.ingest.md), a Python library for causal discovery, collects algorithms that infer causal structure from observational data under method-specific assumptions. [DoWhy](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md), a causal-inference library, makes the same boundary operational by requiring declared assumptions before identification, estimation, and partial validation or refutation tests.

So a system that learns by causal theories can have reach-assessment, but the warrant is assumption-relative. It must represent the candidate theory, the target intervention or counterfactual class, the discovery or identification assumptions, and the acceptance tests that distinguish mechanism from correlation. Three pieces of apparatus recur, and they are not the same kind of thing: causal sufficiency is an assumption (no relevant common causes go unobserved among the modeled variables), latent confounding is the failure mode when it does not hold, and do-calculus is the rule system for deriving intervention effects from a supplied graph. None of them justifies the graph and variables they range over.

## The proof route

Proof is a second route. If a candidate commitment can be expressed as a theorem, invariant, type property, model-checking obligation (exhaustively checking a property over the states or transitions of a formal model), or utility comparison over a specified domain, proof search can establish explanatory-reach across that domain. The result is genuine reach-assessment inside the model: the evaluator checks the claim's quantified consequence, not just sampled cases.

[Jürgen Schmidhuber's Gödel-machine proposal](../sources/goedel-machines-schmidhuber.ingest.md) is the useful placement example — a proof-gated host architecture in which a candidate self-rewrite is accepted only when the machine proves that switching now yields higher axiomatized utility than continuing proof search, under the current axioms and utility function.

So the [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) fits here conditionally. Were its axioms to include the relevant causal assumptions and its utility function to reward correct intervention or counterfactual generalization, the proof gate could license adopting a causal-theory learner, graph, or inference rule. Without them it supplies the acceptance rule and not the assessment.

## The formalization boundary

The formal routes move judgment upstream rather than abolishing it. A proof shows a theorem follows from axioms, not that the variables, domain, or utility function represent the original claim; causal inference gives assumption-relative warrant, not validation of causal truth from observations alone. So a theorem over the wrong variables can pass every obligation while missing the intended commitment, and an invariant relation selected from narrow environments can look stable while tracking an artifact of sampling. These are failures in the translation from the natural-language claim to the formal obligation rather than failures of proof or do-calculus, [which is why warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

The invariance case has been worked out formally. [Rosenfeld, Ravikumar, and Risteski](../sources/the-risks-of-invariant-risk-minimization.ingest.md) analyse the invariant risk minimization objective inside a Gaussian structural equation model and construct a predictor that is near-optimal under the penalized objective and near-identical to the invariant predictor on training data, yet reverts to plain empirical risk minimization once the test environment drifts far enough: the obligation is discharged and the wrong commitment is recovered. The mechanism generalizes past IRM. The penalty that construction pays scales with the mass of the region where it misbehaves, and that region is rare in training — so an acceptance criterion evaluated on the distribution that produced the candidate can price bad off-distribution behaviour at nearly nothing.

The same analysis says when the route pays. In the linear regime it establishes a threshold in the number of training environments `E` against the dimension `d_e` of the environment-varying features: above it, any feasible linear featurizer must discard those features and the invariant predictor is recovered; at or below it, a predictor using only environmental features is feasible and attains lower risk. The causal route is therefore worth taking where genuine environments are plentiful relative to the spurious-feature dimension and the model class is restricted enough for feasibility to bite. Where they are not, it returns an answer carrying no more warrant than fitting would have.

Two limits keep this from proving more than it does. The result bounds the IRM objective and close relatives, not invariance-based causal inference generally, so it leaves [invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) as used above intact: Peters and colleagues analyse a hypothesis-testing procedure with confidence bounds, while the evasion constructed here is what optimizing over a rich hypothesis class admits. And that construction is an existence proof about what the objective permits, not evidence that gradient training finds such a solution — enough to show the obligation underdetermines the commitment, not that practitioners land there.

The natural-language case remains different. A natural-language claim whose reach has not been reduced to causal or proof obligations still needs semantic judgment about what it means and where it breaks. Current LLM-mediated review appears to supply some of that judgment, and this note does not explain why. The narrower point is what stands: once explanatory-reach is represented as formal obligations, symbolic systems can assess it inside their modeled domain — and the edge of that domain is fixed by a translation they do not check.

---

Relevant Notes:

- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: vocabulary this note develops into causal and proof obligations
- [Representational form](./definitions/representational-form.md) — grounds: explains why natural-language, symbolic, and parametric commitments expose different review methods
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: proof-gated acceptance of a symbolic self-rewrite
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: puts the formal routes developed here alongside the natural-language route, as two ways of discharging the same assessment
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: formal guarantees remain bounded by the oracle or axiomatization that produces them
- [Schmidhuber, Gödel Machines](../sources/goedel-machines-schmidhuber.ingest.md) — evidence: proof-gated host architecture and its unprovable-improvement limitation
- [Causal inference using invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) — evidence: invariance across environments and interventions as a causal acceptance signal
- [The Risks of Invariant Risk Minimization](../sources/the-risks-of-invariant-risk-minimization.ingest.md) — evidence: the environment-count threshold, and a predictor that discharges the invariance obligation while recovering the wrong commitment
- [Towards Causal Representation Learning](../sources/towards-causal-representation-learning.ingest.md) — evidence: causal models support intervention and counterfactual generalization beyond one observed distribution
- [Causal-learn: Causal Discovery in Python](../sources/causal-learn-causal-discovery-in-python.ingest.md) — evidence: causal discovery under explicit method assumptions
- [DoWhy: Expressing and validating causal assumptions](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) — evidence: assumption declaration and partial validation
