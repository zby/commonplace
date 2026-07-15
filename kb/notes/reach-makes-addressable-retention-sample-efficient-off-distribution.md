---
description: "Conjecture: an explicit hypothesis capturing structure that stays stable across a distribution shift may reduce the marginal evidence adaptation needs — conditional on retrieval, economical validation, and the hypothesis being right; not a general advantage of explicit representations"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Reach makes addressable retention more sample-efficient off-distribution

Among the expected advantages of a reflective improvement pathway — hypotheses to be tested against built systems, not definitional truths, [since reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — reuse and transfer is the one that promises a data-efficiency payoff. The motivating vocabulary is David Deutsch's **reach**: in *The Beginning of Infinity*, a good explanation applies far beyond the problem that produced it. Reach motivates the conjecture; it is not evidence for it. Deutsch's claim is epistemological, and nothing in it settles the statistical comparison this note stakes out.

The conjecture, narrowed to what could be measured and could be wrong: **reflective addressability does not itself produce sample efficiency. What it does is make reusable structural hypotheses explicit, retrievable, criticizable, and selectively revisable. When such a hypothesis captures structure that remains stable across a distribution shift, is retrieved successfully, and can be validated economically, it may reduce the marginal new evidence adaptation requires.** Each clause is a condition, and each can fail separately.

## The condition is a structured shift, not "off-distribution"

Generic "off-distribution" is too broad to predict anything: some shifts destroy every regularity a system could have retained, explicit or not. The expected advantage arises under **structured shifts** — the target cases differ enough that the existing parametric behavior would otherwise require adaptation, while some mechanism, rule, modular structure, or invariant remains stable across the shift and the retained hypothesis captures it. The transfer literature supports exactly this conditional shape and no more: reusable causal mechanisms are proposed as what survives intervention-like change ([Schölkopf et al. 2021](https://arxiv.org/abs/2102.11107)), speed of adaptation to such change can be made a training signal ([Bengio et al. 2019](https://arxiv.org/abs/1901.10912)), and a growing library of explicit program components compounds across a task family ([Ellis et al., DreamCoder](https://arxiv.org/abs/2006.08381)). None of this establishes a general superiority of explicit representations — and generalization under shift stays difficult and assumption-dependent for every method: no domain-generalization algorithm reliably beat empirical risk minimization under fair model selection ([Gulrajani and Lopez-Paz 2020](https://arxiv.org/abs/2007.01434)), and a leading invariance objective provably fails outside its assumptions ([Rosenfeld, Ravikumar, and Risteski 2020](https://arxiv.org/abs/2010.05761)). Where no stable structure exists, or the hypothesis misses the structure that does, the conjectured advantage has nothing to bind to.

## Parametric transfer is real; what is distinct is addressability

An earlier formulation said samples do not transfer and theories do. That is false as stated. Learned parameters and representations transfer, generalize, and support few-shot adaptation — features learned in one network transfer to related tasks ([Yosinski et al. 2014](https://arxiv.org/abs/1411.1792)), and meta-learned initializations adapt from a handful of examples ([Finn, Abbeel, and Levine 2017](https://arxiv.org/abs/1703.03400)) — with the transfer depending on learned invariances, prior training, and source–target similarity. What an explicit hypothesis offers is not transfer where none was possible, but stronger addressability of the transferred thing: its applicability conditions, assumptions, failure modes, and revisions can each be considered separately, which parametric transfer does not expose. And reach is not warrant: a hypothesis can be general without being justified, and justified while having narrow reach. Generality is a property of what it says; warrant, of how it was checked.

## The ledger must be symmetric

Frame the comparison as marginal new evidence per target task, or as amortized total cost across a task family — never as "paid for once, costs nothing to apply." The explicit pathway's ledger runs: hypothesis discovery, codification, retrieval, applicability checking, validation, application, maintenance, and correction. The parametric ledger runs: pretraining, target adaptation data, optimization, and evaluation. Two entries deserve emphasis. Retrieval is a real discount, [since retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md): a hypothesis nothing surfaces contributes nothing, while parametric retention cannot fail to be found. And the boundary must be drawn honestly: counting the historical evidence that produced the explicit theory as free, while charging the parametric learner for all its training data, biases the comparison before it starts. Validation, finally, has more routes than criticism — proof, simulation, model checking, causal analysis, counterexample generation, targeted experiments. Criticism is the judgment-heavy route whose reliability bounds unattended use, [since warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md); it is not the only one.

## Scaling laws, as illustration

Scaling-law models illustrate how an explicit retained model can reduce the number of full experiments needed to choose configurations within a sufficiently stable system family: refitting the compute-optimal law moved a generation of allocation decisions without training every candidate ([Hoffmann et al. 2022](https://arxiv.org/abs/2203.15556)). The illustration carries its own qualifications, which is why it is motivation rather than strong evidence: what the law saves is experiments and human reasoning effort, not training data or compute per se; and the law is itself learned from experiments and can fail outside the regime it was fitted in — the refit corrected its predecessor.

## What would test it

- Construct task families with controlled structured shifts.
- Hold prior data, compute, and background information as equal as practical.
- Compare a parametric or meta-learned adaptation pathway, an explicit addressable-hypothesis pathway, and preferably a hybrid.
- Measure new target samples, target performance, retrieval success, validation cost, correction cost, compute, and total amortized evidence across the family.
- Include cases where the retained hypothesis is wrong, since correction is part of the ledger.

Final form: **an addressable pathway reduces marginal adaptation evidence only when reusable stable structure exists, the retained representation captures it, retrieval succeeds, and validating and applying the hypothesis costs less than relearning the relevant behavior from target data.** Reflection supplies addressability; addressability can hold explicit reusable structure; correct reusable structure may reduce marginal adaptation evidence under some shifts. Whether it actually does is an experimental question, not a consequence of the definitions.

## Open Questions

- Whether a task family with controlled structured shift can be exhibited where the explicit-hypothesis pathway measurably wins the amortized ledger — and one where it measurably loses.
- Whether hybrid pathways — parametric adaptation guided by retrieved explicit hypotheses — dominate both pure pathways, which would turn the contest into an engineering question about composition.

---

Relevant Notes:

- [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — grounds: supplies the reuse-and-transfer affordance this note sharpens into a conditional data-efficiency hypothesis
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: the retrieval entry in the explicit pathway's ledger
- [Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) — mechanism: why criticism, among the validation routes, is the one bounded by oracle reach
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the architecture through which an explicit hypothesis is adopted and later corrected
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the reflective/non-reflective distinction whose conjectured payoff this note makes falsifiable
