---
description: "Causal and proof obligations demonstrate two ways formal symbolic systems can assess explanatory-reach inside a warranted model"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# Causal and proof obligations are two formal routes to assessing explanatory-reach

[Reach-assessment](./definitions/reach-assessment.md) is not intrinsically an LLM-only or natural-language-only capability. Two demonstrated formal routes translate a candidate commitment's claimed generality into an obligation a symbolic system can check: a causal mechanism that should survive interventions or environment shifts, an identifiable causal effect under stated assumptions, or a theorem over a formally specified domain. These examples do not establish an exhaustive taxonomy of formal routes.

The shift is from asking "does this sentence sound like a good generalization?" to asking "what formal consequence must hold if this generalization is genuine?" What such a check establishes is bounded by the translation that produced it, which the last section takes up.

## The causal route

Causal theories have explanatory-reach because they do not merely fit one observed distribution. A structural causal model states mechanisms whose implications extend to interventions and counterfactuals: "While a statistical model specifies a single probability distribution, a causal model represents a set of distributions, one for each possible intervention" ([Towards Causal Representation Learning, Figure 1 caption](../sources/towards-causal-representation-learning.ingest.md), verbatim).

That is the route formal reach-assessment can use: a proposed commitment is accepted not because it predicts the training cases, but because the mechanism it asserts supports the intended intervention, counterfactual, or shift claims. [Invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) applies setwise tests to candidate predictor sets for an invariant conditional relation across observed environments. Under the paper's assumptions and valid tests, "The confidence sets thus have the correct (conservative) coverage" and "In the worst case, the set Ŝ(E) might be empty but the error control is valid nonetheless" ([Peters, Bühlmann, and Meinshausen, Section 3, following Theorem 1](../sources/causal-inference-using-invariant-prediction.ingest.md), verbatim).

[Causal-learn](../sources/causal-learn-causal-discovery-in-python.ingest.md), a Python library for causal discovery, collects algorithms that infer causal structure from observational data under method-specific assumptions. [DoWhy](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md), a causal-inference library, makes the same boundary operational by requiring declared assumptions before identification, estimation, and partial validation.

So a system that learns by causal theories can have reach-assessment, but the warrant is assumption-relative. It must represent the candidate theory, the target intervention or counterfactual class, the discovery or identification assumptions, and the acceptance tests that distinguish mechanism from correlation. Three pieces of apparatus recur, and they are not the same kind of thing: causal sufficiency is an assumption (no relevant common causes go unobserved among the modeled variables), latent confounding is the failure mode when it does not hold, and do-calculus is the rule system for deriving intervention effects from a supplied graph. None of them justifies the graph and variables they range over.

## The proof route

Proof is a second route. If a candidate commitment can be expressed as a theorem, invariant, type property, model-checking obligation (exhaustively checking a property over the states or transitions of a formal model), or utility comparison over a specified domain, proof search can establish explanatory-reach across that domain. The result is genuine reach-assessment inside the model: the evaluator checks the claim's quantified consequence, not just sampled cases.

[Jürgen Schmidhuber's Gödel-machine proposal](../sources/goedel-machines-schmidhuber.ingest.md) is the useful placement example — a proof-gated host architecture in which a candidate self-rewrite is accepted only when the machine proves, under the current axioms and utility function, that "the utility of a switch from p to the current switchprog would be higher than the utility of continuing the execution of p" ([Schmidhuber, Gödel Machines, Section 3.2](../sources/goedel-machines-schmidhuber.ingest.md), verbatim).

So the [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) fits here conditionally. Were its axioms to include the relevant causal assumptions and its utility function to reward correct intervention or counterfactual generalization, the proof gate could license adopting a causal-theory learner, graph, or inference rule. Without them it supplies the acceptance rule and not the assessment.

## The formalization boundary

The formal routes move judgment upstream rather than abolishing it. For an externally interpreted claim, [codification](./definitions/codification.md) relocates interpretation to the correspondence boundary: someone must still decide which variables, domain, axioms, obligations, or utility function preserve the original commitment, because [semantic work can be relocated but not eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md). A proof shows a theorem follows from axioms, not that those choices represent the original claim; causal inference gives assumption-relative warrant, not validation of causal truth from observations alone. So a theorem over the wrong variables can pass every obligation while missing the intended commitment, and an invariant relation selected from narrow environments can look stable while tracking an artifact of sampling. These are failures in the translation from the natural-language claim to the formal obligation rather than failures of proof or do-calculus, [which is why warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

When natural language is only an informal presentation of an authoritative formal definition, no model-to-world observational claim lies beyond the formal object. The correspondence argument here therefore applies to empirical and otherwise externally interpreted theories, not to every formalization.

The invariance case has been worked out formally. [Rosenfeld, Ravikumar, and Risteski](../sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md) analyse the invariant risk minimization objective inside a Gaussian structural equation model and construct a predictor that is near-optimal under the penalized objective and near-identical to the invariant predictor on the training distribution, yet reverts to plain empirical risk minimization on most test points once the test environment's mean drifts far enough. Within that construction, the penalty scales with the squared probability mass of the rare region where the predictor changes behavior and is exponentially small in the environmental-feature dimension. The broader gate-design lesson is target-side: an acceptance criterion evaluated where failure behavior is rare can assign that behavior almost no cost.

The same analysis gives a threshold for its linear IRM setting. When the number of training environments `E` exceeds the dimension `d_e` of the environment-varying features, any feasible linear featurizer must discard those features and the invariant predictor is recovered. When `E <= d_e`, an environmental-only predictor is feasible and attains lower risk. This is a limitation of that IRM formulation under the paper's assumptions. It does not say that every feasible IRM result below the threshold lacks warrant, and it does not set a threshold for causal approaches generally.

Two limits keep this from proving more than it does. The result bounds the IRM objective analyzed in the paper, not invariance-based causal inference generally, so it leaves [invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) as used above intact: Peters and colleagues analyse a hypothesis-testing procedure with confidence bounds, while the evasion constructed here is what optimizing over a rich hypothesis class admits. The nonlinear counterexample is a formal existence result. The paper also reports synthetic fits from its own data model that confirm its theoretical predictions, but those experiments do not establish how often practical gradient training reaches the constructed failure outside that setting.

The natural-language case remains different. A natural-language claim whose reach has not been reduced to causal or proof obligations still needs semantic judgment about what it means and where it breaks. Current LLM-mediated review appears to supply some of that judgment, and this note does not explain why. The narrower point is what stands: once explanatory-reach is represented as formal obligations, symbolic systems can assess it inside their modeled domain — and the edge of that domain is fixed by a translation they do not check.

---

Relevant Notes:

- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: vocabulary this note develops into causal and proof obligations
- [Representational form](./definitions/representational-form.md) — grounds: explains why natural-language, symbolic, and parametric commitments expose different review methods
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: proof-gated acceptance of a symbolic self-rewrite
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: puts the formal routes developed here alongside the natural-language route, as two ways of discharging the same assessment
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: formal guarantees remain bounded by the oracle or axiomatization that produces them
- [Schmidhuber, Gödel Machines](../sources/goedel-machines-schmidhuber.ingest.md) — evidenced-by: proof-gated host architecture and its unprovable-improvement limitation
- [Causal inference using invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) — evidenced-by: invariance across environments and interventions as a causal acceptance signal
- [The Risks of Invariant Risk Minimization](../sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md) — evidenced-by: the environment-count threshold, and a predictor that discharges the invariance obligation while recovering the wrong commitment
- [Towards Causal Representation Learning](../sources/towards-causal-representation-learning.ingest.md) — evidenced-by: causal models support intervention and counterfactual generalization beyond one observed distribution
- [Causal-learn: Causal Discovery in Python](../sources/causal-learn-causal-discovery-in-python.ingest.md) — evidenced-by: causal discovery under explicit method assumptions
- [DoWhy: Expressing and validating causal assumptions](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) — evidenced-by: assumption declaration and partial validation
- [Eigenius](../agentic-systems/eigenius.md) — evidenced-by: its Lean path establishes proof validity under a fixed axiom allowlist, while correspondence to a graph claim is checked only when optional anchors are present and pass
- [DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — evidenced-by: its abstract-page record separates a natural-language explanation from a Python implementation and reports that predictive accuracy does not guarantee explanation quality
