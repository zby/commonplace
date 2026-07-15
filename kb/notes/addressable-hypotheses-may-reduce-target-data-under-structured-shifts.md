---
description: "Conjecture: an addressable hypothesis capturing structure stable across a task shift may cut the new target observations adaptation needs; the reflection-to-efficiency bridge is itself conjectural"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Addressable hypotheses may reduce target data under structured shifts

Among the expected advantages of a reflective improvement pathway — hypotheses to be tested against built systems, not definitional truths, [since reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — reuse and transfer is the one that promises a target-data payoff. The motivating vocabulary is David Deutsch's **reach**: in *The Beginning of Infinity*, a good explanation applies far beyond the problem that produced it. Reach motivates the conjecture; it is not evidence for it. Deutsch's claim is epistemological, and nothing in it settles the statistical comparison this note stakes out.

The conjecture, narrowed to what could be measured and could be wrong: **reflective routing can make retained structures addressable. Addressability can support explicit, reusable hypotheses whose assumptions, applicability, failures, and revisions are separately inspectable. When such a hypothesis captures structure that remains stable across a task shift, is retrieved successfully, and is applied and validated economically, it may reduce the new target evidence required for adaptation.** Each clause is a condition, and each can fail separately.

One scope line before the argument. The literature cited below supports the proposed transfer mechanism — reuse of causal, modular, compositional, or explicit structure — not computational reflection itself. The conjecture applies to reflective self-improvement only when the retained hypothesis participates in the [causally connected self-representation](./definitions/reflective-system.md) through which the system changes its own behavior; explicit domain knowledge may transfer without making an improvement pathway reflective. The bridge from explicit representation to reflection is Commonplace's own, and it is conjectural end to end.

## The condition is a structured shift, not "off-distribution"

Generic "off-distribution" is too broad to predict anything: some shifts destroy every regularity a system could have retained, explicit or not. The expected advantage arises under **structured shifts** — the target cases differ enough that the existing parametric behavior would otherwise require adaptation, while some mechanism, rule, modular structure, or invariant remains stable across the shift and the retained hypothesis captures it. The transfer literature supports exactly this conditional shape and no more: reusable causal mechanisms are proposed as what survives intervention-like change ([Schölkopf et al. 2021](https://arxiv.org/abs/2102.11107)), speed of adaptation to such change can be made a training signal ([Bengio et al. 2019](https://arxiv.org/abs/1901.10912)), and a growing library of explicit program components compounds across a task family ([Ellis et al., DreamCoder](https://arxiv.org/abs/2006.08381)). None of this establishes a general superiority of explicit representations — and generalization under shift stays difficult and assumption-dependent for every method: under the benchmarks and model-selection procedures studied by [Gulrajani and Lopez-Paz (2020)](https://arxiv.org/abs/2007.01434), the evaluated domain-generalization methods did not consistently outperform carefully implemented empirical risk minimization, and in the settings analyzed by [Rosenfeld, Ravikumar, and Risteski (2020)](https://arxiv.org/abs/2010.05761), IRM and related objectives can fail to recover the intended invariant predictor and need not improve over empirical risk minimization. Where no stable structure exists, or the hypothesis misses the structure that does, the conjectured advantage has nothing to bind to.

## Parametric transfer is real; what is distinct is addressability

An earlier formulation said samples do not transfer and theories do. That is false as stated. Learned parameters and representations transfer, generalize, and support few-shot adaptation — features learned in one network transfer to related tasks ([Yosinski et al. 2014](https://arxiv.org/abs/1411.1792)), and meta-learned initializations adapt from a handful of examples ([Finn, Abbeel, and Levine 2017](https://arxiv.org/abs/1703.03400)) — with the transfer depending on learned invariances, prior training, and source–target similarity. What an explicit hypothesis offers is not transfer where parametric systems have none, but stronger, first-class addressability of the transferred thing: its applicability conditions, assumptions, failure modes, and revisions can each be considered separately, where ordinary parametric transfer does not expose them by default as separately named, system-readable objects. And reach is not warrant: a hypothesis can be general without being justified, and justified while having narrow reach. Generality is a property of what it says; warrant, of how it was checked.

## Two efficiencies, one ledger

The conjecture makes a **primary statistical hypothesis**: an addressable-hypothesis pathway may need fewer new target observations to reach a fixed performance level. Distinct from it is the **economic qualification**: that target-data advantage may shrink or disappear once the full cost is counted. Frame the total as amortized cost across a task family, and keep the ledger symmetric. The explicit pathway's ledger runs: hypothesis discovery, codification, retrieval, applicability checking, validation, application, maintenance, and correction. The parametric ledger runs: pretraining, target adaptation data, optimization, and evaluation. Only the target-observation entries are the statistical hypothesis; the rest is economics, and calling every entry "sample efficiency" conflates the two.

Three ledger entries deserve emphasis. Retrieval is a real discount on the explicit side, [since retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md): a hypothesis nothing surfaces contributes nothing. Parametric retention avoids a separate artifact-retrieval step because it is resident in the operative substrate — which does not guarantee that the relevant learned behavior will activate, generalize, or remain accessible in the current context; its discount is differently shaped, not absent. The boundary must be drawn honestly: counting the historical evidence that produced the explicit theory as free, while charging the parametric learner for all its training data, biases the comparison before it starts. And validation has more routes than criticism — proof, simulation, model checking, causal analysis, counterexample generation, targeted experiments. Criticism is the judgment-heavy route whose reliability bounds unattended use, [since warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md); it is not the only one.

## Scaling laws, as illustration

Scaling-law models illustrate how an explicit retained model can guide allocation decisions without exhaustively training every candidate configuration ([Hoffmann et al. 2022](https://arxiv.org/abs/2203.15556)). Their immediate payoff is fewer exploratory experiments and better allocation of search and training compute — not necessarily fewer target examples — which is why they motivate the conjecture rather than evidence it. The law is itself inferred from experiments, applies within assumptions about the system family and regime, and may require revision when those assumptions change.

## What would test it

The comparison must isolate addressability, or it merely shows that one pathway received better prior knowledge. Where practical, encode equivalent prior structure in an explicit, addressable form and in a parametric or distilled form, matching informational content, acquisition data, and compute as closely as possible. Then, over task families with controlled structured shifts, compare:

- the explicit hypothesis with normal retrieval;
- the same hypothesis with impaired retrieval;
- a wrong but highly addressable hypothesis;
- parametric or meta-learned adaptation;
- a hybrid using retrieved hypotheses plus parametric adaptation.

Measure the new target observations required to reach a fixed performance level, alongside retrieval success, validation cost, correction cost, compute, and total amortized cost across the family.

The directional prediction: **for task families sharing a stable mechanism or compositional rule, a matched addressable-hypothesis pathway should reach a fixed target performance with fewer new target observations than a parametric adaptation baseline — an advantage that increases with the number of tasks across which the retained structure is reused, decreases with retrieval and applicability errors, and disappears or reverses when the hypothesis is wrong or no relevant stable structure exists.**

The sequence, each step at its own strength: reflection may supply addressability; addressability may support explicit reusable structure; correct reusable structure may lower marginal target-data requirements under structured shifts. Existing literature supports pieces of that mechanism. The full reflection-to-efficiency claim is Commonplace's hypothesis, and it remains to be tested.

## Open Questions

- Whether a task family with controlled structured shift can be exhibited where the matched explicit-hypothesis pathway measurably reaches fixed performance on fewer target observations — and one where it measurably fails to.
- Whether hybrid pathways — parametric adaptation guided by retrieved explicit hypotheses — dominate both pure pathways, which would turn the contest into an engineering question about composition.

---

Relevant Notes:

- [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — grounds: supplies the reuse-and-transfer affordance this note sharpens into a conditional target-data hypothesis
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: the retrieval entry in the explicit pathway's ledger
- [Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) — mechanism: why criticism, among the validation routes, is the one bounded by oracle reach
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: one architecture for evaluating, adopting, and correcting an explicit hypothesis
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the reflective/non-reflective distinction whose conjectured payoff this note makes falsifiable
- [Inductive bias splits into a generic level shared by all and a specific level where learners differ](./inductive-bias-splits-into-generic-and-specific-levels.md) — grounds: locates this conjecture at the specific inductive bias, the only level addressability and any differential advantage can touch
- [Reflective system](./definitions/reflective-system.md) — defined-in: the causally connected self-representation a retained hypothesis must participate in for the conjecture to bear on reflection
