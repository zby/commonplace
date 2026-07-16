---
description: "Formal symbolic systems can assess reach when a claim's claimed generality is encoded as causal mechanisms, invariants, or proof obligations"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# Formal systems can assess reach through causal and proof obligations

[Reach assessment](./definitions/reach-assessment.md) is not intrinsically an LLM-only or prose-only capability. A formal symbolic system can assess reach when the candidate commitment's claimed generality is represented as an obligation the system can check: a causal mechanism that should survive interventions or environment shifts, an identifiable causal effect under stated assumptions, or a theorem over a formally specified domain.

The shift is from asking "does this sentence sound like a good generalization?" to asking "what formal consequence must hold if this generalization is genuine?" Once the consequence is explicit, ordinary formal machinery can carry part of the reach judgment.

## The causal route

Causal theories have reach because they do not merely fit one observed distribution. A structural causal model states mechanisms whose implications extend to interventions and counterfactuals; [causal representation learning](../sources/towards-causal-representation-learning.ingest.md) frames this as the difference between statistical models of one distribution and causal models that represent distributions under possible interventions. This is the exact shape reach assessment needs: a proposed commitment is accepted not because it predicts the training cases, but because the mechanism it asserts supports the intended intervention, counterfactual, or shift claims.

Several existing systems and methods instantiate pieces of that route. [Invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) tests whether candidate predictors keep their predictive relation across environments and interventions, using invariance as the causal signal. [Causal-learn](../sources/causal-learn-causal-discovery-in-python.ingest.md) collects causal-discovery algorithms that infer causal structure from observational data under method-specific assumptions such as conditional independence, causal sufficiency, latent-confounder handling, or functional/noise constraints. [DoWhy's assumptions work](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) makes the same boundary operational: causal inference begins by declaring assumptions, then identifies and estimates effects while running only partial validation or refutation tests. There is no global validator for causal truth from observations alone.

So a system that learns by causal theories can have reach assessment, but the warrant is assumption-relative. It must represent the candidate theory, the target intervention or counterfactual class, the discovery or identification assumptions, and the acceptance tests that distinguish mechanism from correlation. Causal vocabulary in stored prose is not enough.

## The proof route

Proof is a second formal route. If a candidate commitment can be expressed as a theorem, invariant, type property, model-checking obligation, or utility comparison over a specified domain, proof search can establish reach across that domain. The result is genuine reach assessment inside the formal model: the evaluator checks not just sampled cases, but the claim's quantified consequence.

The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) is the useful placement example. It is not evidence for causal discovery and not evidence that theorem provers can judge arbitrary prose. It is a proof-gated host architecture: a candidate self-rewrite is accepted only when the machine proves the target theorem that switching now yields higher axiomatized utility than continuing proof search, under the current axioms and utility function ([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md)).

That means the Gödel machine fits the reach-assessment story conditionally. If its axiom set included a causal calculus, causal-discovery assumptions, and a utility function rewarding correct intervention or counterfactual generalization, then a proof technique could in principle prove that adopting some causal-theory learner, graph, or inference rule improves expected utility. In that setup, the proof gate would license causal-theory learning or adoption. Without those causal axioms and objectives, the Gödel machine contributes only the proof-gated acceptance rule.

## Boundaries

The formal routes move judgment upstream rather than abolishing it. Causal inference depends on graph, mechanism, sampling, and confounding assumptions; wrong assumptions can produce a formally clean but false warrant. Proof depends on axioms, domain specification, and utility formalization; a proof is only as faithful as the formal model it proves within, [which is why warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

Observational causal discovery deserves special care. It can infer causal theories from observations, but not by extracting causality from raw correlation alone. The inference works through assumptions and discovery criteria. Likewise, do-calculus identifies causal effects from a supplied causal graph; by itself it does not discover that graph. A full formal reach-assessment system needs the graph-learning, assumption-declaration, identification, and validation surfaces to be explicit.

The prose case remains different. A natural-language claim whose reach has not been reduced to causal or proof obligations still needs semantic judgment about what the claim means and where it breaks. Current LLM-mediated review appears to supply some of that judgment, but this note does not explain why. The point is narrower: once reach is represented as formal obligations, traditional symbolic systems can assess it within their modeled domain.

---

Relevant Notes:

- [Reach assessment](./definitions/reach-assessment.md) — defined-in: vocabulary this note develops into the formal causal/proof route
- [Representational form](./definitions/representational-form.md) — grounds: explains why prose, symbolic, and parametric commitments expose different review methods
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: proof-gated acceptance of a symbolic self-rewrite utility claim
- [Reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) — evidence: connects reusable causal mechanisms to transfer under structured shifts
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: formal guarantees remain bounded by the oracle or axiomatization that produces them
- [Schmidhuber, Gödel Machines](../sources/goedel-machines-schmidhuber.ingest.md) — evidence: primary grounding for the proof-gated host architecture and its unprovable-improvement limitation
- [Causal inference using invariant prediction](../sources/causal-inference-using-invariant-prediction.ingest.md) — evidence: invariance across environments and interventions as a causal acceptance signal
- [Towards Causal Representation Learning](../sources/towards-causal-representation-learning.ingest.md) — evidence: causal models support intervention and counterfactual generalization beyond one observed distribution
- [Causal-learn: Causal Discovery in Python](../sources/causal-learn-causal-discovery-in-python.ingest.md) — evidence: causal discovery from observational data under explicit method assumptions
- [DoWhy: Expressing and validating causal assumptions](../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) — evidence: causal effects require declared assumptions and only partial validation is available
