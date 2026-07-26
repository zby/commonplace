---
description: "Conjecture: learning that discovers, assesses, and revises addressable theories may need fewer target observations when a shift preserves the structure a theory names"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, discovery]
---

# Theory-mediated learning may improve sample efficiency under structured shifts

When a task changes, a learner can adapt by fitting new behavior directly to new observations. It can also infer a theory that explains the observations, then reuse or revise that theory when the task changes. Under shifts that preserve some underlying structure, the second route may need fewer target observations.

Call a pathway **theory-mediated** when it represents a candidate theory as an intermediate object and changes behavior by adopting, applying, rejecting, or revising it. The theory may be prose, a causal model, a program, or another representation. What matters is that the learning process can reason about what the theory says, not merely reproduce the behavior it induces.

The conjectured pathway is:

> **observations → theory search → assessment of explanatory-reach → retained addressable theory → reuse or targeted revision**

The expected gain depends on the whole pathway. Addressability alone only makes a theory available for operation; the leverage comes from finding a theory with genuine explanatory-reach, and the capability that selects for that rather than for adaptive fit is [reach-assessment](./definitions/reach-assessment.md), which no amount of retention machinery supplies on its own.

## Explanatory-reach supplies the leverage

A theory has [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) when it captures structure that supports correct conclusions beyond the observations that produced it. That structure may be a causal mechanism, invariant, modular decomposition, compositional rule, or reusable program.

A **structured shift** changes surface regularities while preserving enough of this structure for an earlier theory to remain useful. The learner may then need to identify only which premise, parameter, component, or applicability condition changed, rather than infer each target behavior independently. One theory-level revision can change many downstream predictions at once.

For example, a coding agent may observe that several documentation-only changes do not require integration tests. It could retain the correlation-shaped rule "documentation files are safe." Or it could infer the theory "a changed file cannot affect integration behavior when no executed process consumes it." If a build tool later begins reading one documentation file as configuration, one failure can support a precise revision: the exemption applies only to files not consumed by executable tooling. The correlation-shaped rule offers no such handle — it can only be deleted or narrowed by enumeration.

This is also the central risk. A broad but wrong theory produces broader negative transfer than a local association does, because it is wrong just as widely as it would have been useful — and [stating where a lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) is a judgment, not something the evidence hands over.

## The capability at issue is reasoning about theories

A collection of explicit rules is not enough. The learner must be able to construct candidate theories, derive their consequences, identify their assumptions, compare rival explanations, seek discriminating evidence, and revise a theory's content or scope. Search and assessment stay distinct stages, [since a proposal-selection loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md): a system can be starved by its search range while its evaluator is sound, or flooded with candidates its evaluator cannot rank.

LLMs make this pathway practical for theories that have not yet been formalized. They can operate on natural-language candidates: expose an assumption, compare mechanisms, propose a counterexample, or rewrite an applicability condition. How reliably they select theories with genuine explanatory-reach rather than plausible post-hoc stories is an open empirical question, and two recent benchmarks measure adjacent parts of it.

[DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) places agents in simulated worlds with non-standard laws, has them design experiments on trajectory data, and collects both a prose explanation and a Python implementation of the discovered law. Its most relevant result is not the pass rate but the dissociation: predictive accuracy and explanation quality come apart. That is the separation this conjecture depends on, measured directly rather than assumed. [FalsifyBench](../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) runs a Wason-style rule-discovery game across twelve models and reports that success is driven by test selection — models probing to falsify their current hypothesis outperform models probing to confirm it.

Both readings need care, and both captures are abstract-level. If DiscoverPhysics scored explanation quality with an LLM judge, its dissociation is a hard oracle disagreeing with a soft one rather than a measurement of understanding; and its worlds, while counterfactual as instances, are drawn from a space published physics already discusses. FalsifyBench's headline may be partly definitional: on 2-4-6, where the hidden rule is deliberately broader than the seed invites, probes outside the current hypothesis are also the only informative probes, so the correlation could be information gain rather than an epistemic disposition. Neither benchmark tests reuse of a retained theory across a controlled shift — which is exactly the gap the test design below proposes to fill — but together they establish that theory search and its assessment can be measured separately from predictive fit at all.

## Purely parametric retention exposes no scope

A parametric learner can acquire reusable structure. Features learned in one network transfer to related tasks ([Yosinski et al. 2014](https://arxiv.org/abs/1411.1792)), meta-learned initializations adapt from a handful of examples ([Finn, Abbeel, and Levine 2017](https://arxiv.org/abs/1703.03400)), and gradient updates can produce behavior equivalent to revising a theory. The claim cannot be that weights contain only correlations or that they cannot encode theories.

The distinction is narrower and architectural. Where retention is purely parametric and the learning pathway exposes no semantic interface to what was retained, an individual theory is not a first-class update target. The system may acquire equivalent behavior, but it cannot deliberately retrieve one theory, compare it with a rival, replace one of its premises, or narrow its scope while preserving unrelated commitments; the extent and collateral effects of an update have to be discovered behaviorally. A theory is **addressable** when the system can identify it as a stable semantic unit and inspect or revise its relevant parts — and addressability comes in degrees, since a theory addressable only as an indivisible document can be replaced or deleted but not rescoped by one premise, which requires its content, assumptions, and applicability conditions to be separately reachable.

Two lines of work show this is a claim about a default rather than an impossibility, and the shape of their shortfall is more informative than the fact that they exist. [ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) edits particular factual associations inside transformer weights, recovering an interface after training. What it delivers is content-addressability without scope-addressability: a rank-one edit revises a stored association but carries no applicability boundary, so rescoping remains unavailable. [Concept bottleneck models](../sources/concept-bottleneck-models.ingest.md) take the other route, supervising a legible concept layer into existence before training so it can be intervened on — but the intervention is per-inference and nothing is retained, and where the concept loss is weighted too low the layer stays readable and competitive while interventions on it make predictions worse.

So the contrast is not neural versus symbolic, nor computational expressivity. It is **purely parametric adaptation versus learning that can operate on theories as theories**, and the axis it runs along is [representational form](./definitions/representational-form.md). An LLM using retained prose is a hybrid on that axis: the weights supply the semantic interpreter, the prose supplies persistent identity and selective revisability.

## Formalization buys a mechanical acceptance test

Symbolic systems implement the same pathway wherever the theory space and acceptance criteria are formalized: causal discovery searches for structure whose consequences survive specified interventions, and [DreamCoder](../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) grows a library of reusable program abstractions that compound across a task family.

DreamCoder also shows what formalization buys, and it is the acceptance test rather than the search. Its retention gate is statistical — an abstraction is kept when it reduces description length — so the decision to retain is mechanical. Nothing plays that role for a theory still in prose, where stating where the theory stops remains a judgment, which is why the prose route's advantage rests on a capability with no formal proxy. The cost of the formal route is a supplied language, variables, primitives, search procedure, and acceptance test, [worked out in the causal and proof obligations that formal systems check](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md). LLMs take the opposite trade: a far more open-ended theory space before formalization, with weaker guarantees.

## What the negative results actually bound

Generic "off-distribution" predicts nothing, since some shifts destroy every regularity any system could have retained. The conjecture is conditional on structured shifts, and the transfer literature supports that conditional shape and no more: reusable causal mechanisms are proposed as what survives intervention-like change ([Schölkopf et al. 2021](../sources/towards-causal-representation-learning.ingest.md)), cross-environment stability is proposed as evidence for causal predictors ([Peters, Bühlmann, and Meinshausen 2016](../sources/causal-inference-using-invariant-prediction.ingest.md)), and speed of adaptation to such change can be made a training signal ([Bengio et al. 2019](https://arxiv.org/abs/1901.10912)).

Generalization under shift is hard and assumption-dependent for every method. Under the benchmarks and model-selection procedures studied in [DomainBed](../sources/in-search-of-lost-domain-generalization.ingest.md), the evaluated domain-generalization methods did not consistently beat carefully implemented empirical risk minimization. [Rosenfeld, Ravikumar, and Risteski](../sources/the-risks-of-invariant-risk-minimization.ingest.md) bound invariant risk minimization specifically: in the linear regime it needs more environments than the spurious-feature dimension, and outside it the objective *permits* a predictor that mimics the invariant one on training data and reverts to ERM at test, with a penalty exponentially small in that dimension. That second result is an existence proof about what the objective allows, not evidence that gradient training finds such a solution — a distinction the paper's abstract invites readers to lose, and one that keeps this result compatible with invariance-as-hypothesis-test rather than contradicting it.

The bitter lesson is often read as a third objection here, and it is not one — [what scale selects against is unearned reach, not structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md), so a system that searches theory space and tests its candidates is running the general method rather than supplying a prior. That clearance is conditional on the acceptance test doing real work, which is the condition this whole note turns on. What survives is a narrower objection aimed at the retention layer: a sufficiently scaled system might run the same search implicitly in activations, with no externalized addressable object anywhere, making the artifact scaffolding rather than a load-bearing part of the pathway. Nothing here rebuts that, and [where the artifact has to earn its place against a longer context](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) is where the objection bites hardest.

## Cost can erase the gain

The sample-efficiency hypothesis concerns new target observations only. Distinct from it is whether the advantage survives full accounting: theory discovery, [codification](./definitions/codification.md), retrieval, applicability checking, validation, application, maintenance, and correction on one side; pretraining, adaptation data, optimization, and evaluation on the other. Folding every entry into "sample efficiency" conflates the two.

The boundary must be drawn symmetrically. Counting the historical evidence that produced an explicit theory as free, while charging the parametric learner for all its training data, biases the comparison before it starts. Retrieval deserves separate emphasis: a theory nothing surfaces at the moment of need contributes nothing however good it is, while parametric retention avoids a separate retrieval step by residing in the operative substrate — which does not guarantee the relevant behavior activates or generalizes in context. Its discount is differently shaped, not absent. And validation has more routes than criticism: proof, simulation, model checking, causal analysis, counterexample generation, targeted experiment. Criticism is the judgment-heavy route whose reliability bounds unattended use, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

## What would test the conjecture

Matching "informational content" between an explicit arm and a separately trained parametric arm is probably not operationalizable, and is not needed. Hold the **same base model, the same source observations, and the same inference budget** fixed, and vary only the pathway:

- an explicit theory with stated assumptions and scope, revisable at the theory level;
- raw episodic memory of the same source observations, with no synthesized theory;
- an explicit theory that may only be appended to, never rejected or rescoped;
- the same pathway with the evaluator ablated to surface matching, removing reach-assessment;
- parametric adaptation from the same observations;
- a formal causal-discovery or program-synthesis baseline.

Then apply controlled shifts of distinct kinds: surface change preserving the mechanism; intervention preserving some causal modules; change invalidating exactly one applicability condition; change invalidating the theory entirely; and a deceptive correlation that held across every source observation. Target accuracy alone will not separate the arms. Measure target observations needed to recover performance, whether the correct mechanism was identified, scope calibration, whether one counterexample triggers proportionate rescoping rather than wholesale replacement, collateral damage to unaffected cases, false transfer from an overbroad theory, and the cost of discovery and validation.

The decisive prediction is an interaction, not a level:

> **A correct explicit theory should reduce target observations when the shift preserves the structure it names, while producing less collateral change outside that theory's scope. The advantage should disappear or reverse when the theory is wrong, when the shift breaks the structure, and — the sharpest arm — when the evaluator is ablated, since that arm keeps addressability and loses only reach-assessment.**

A generic accuracy gain would not establish the mechanism. Every arm is a retention pathway wrapped around a fixed base model on an ordinary domain task, so the design needs no special architecture — only controlled shifts and honest measurement.

## Open Questions

- Whether a task family with controlled structured shift can be exhibited where the theory-mediated pathway measurably reaches fixed performance on fewer target observations — and whether one can be exhibited where it measurably fails to.
- Whether the evaluator-ablation arm separates cleanly, or whether a base model capable enough to apply a theory also reach-assesses it implicitly and cannot be ablated without crippling the other arms.
- Whether hybrid pathways — parametric adaptation guided by retrieved explicit theories — dominate both pure pathways, turning the contest into an engineering question about composition.
- Whether a theory's explanatory-reach can be estimated from its addressable form before any shift tests it, or whether legibility supplies only a handle on reach established some other way.
- Whether validating a theory's reach against an informally specified shift is itself target-data-free, or quietly consumes the observations the conjecture claims to save.
- Whether discovery, codification, validation, and maintenance cost for a *library* of many theories grows faster than the smooth cost curve of parametric scaling as task families accumulate.
- Why LLM-mediated evaluators appear able to reach-assess claims still in prose, which no current theory explains and on which this pathway's advantage rests.

---

Relevant Notes:

- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the capability that selects the theory whose reach could pay, and which retention does not supply
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the property that carries the conjectured gain, and the negative test that judges it
- [Conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — grounds: theory search posits a general structure and recognizes prior observations as instances of it
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: stating applicability conditions is a judgment, not a derivation from the evidence
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the search/evaluation split that keeps theory generation distinct from reach-assessment
- [Representational form](./definitions/representational-form.md) — defined-in: the prose, symbolic, and distributed-parametric axis the parametric contrast runs along
- [Codification](./definitions/codification.md) — defined-in: the prose-to-symbolic crossing the cost ledger names
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — extends: develops the formal routes and their dependence on a supplied language
- [World models assess explanatory-reach through action-conditioned prediction](./world-models-assess-explanatory-reach-through-action-conditioned.md) — contrasts: a distributed-parametric route to the same assessment
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — mechanism: why criticism, among validation routes, is the one bounded by oracle domain
- [DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — evidence: predictive accuracy and explanation quality measured separately, and coming apart
- [FALSIFYBENCH](../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) — evidence: falsification-seeking test selection predicts rule-discovery success across models
- [ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) — evidence: parametric editing delivers content-addressability without scope-addressability
- [Concept bottleneck models](../sources/concept-bottleneck-models.ingest.md) — evidence: a legible interface installed by architecture before training, correctable per inference but not retained
- [DreamCoder](../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) — evidence: a compounding library of explicit abstractions, retained by a mechanical description-length gate
- [In search of lost domain generalization](../sources/in-search-of-lost-domain-generalization.ingest.md) — evidence: specialized generalization methods did not consistently beat tuned ERM under a fixed protocol
- [The risks of invariant risk minimization](../sources/the-risks-of-invariant-risk-minimization.ingest.md) — evidence: bounds the IRM objective specifically, in the linear regime by environment count and outside it by an existence proof
