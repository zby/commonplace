---
description: "Conjecture: one theory with reach covers future cases each parametric round would pay samples for — but only off-distribution, discounted by retrieval, with the saved samples reappearing at evaluation"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Reach makes addressable retention more sample-efficient off-distribution

Among the expected advantages of a reflective improvement pathway — hypotheses to be tested against built systems, not definitional truths, [since reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — reuse and transfer is the one with a sample-efficiency payoff. Transfer is what David Deutsch calls **reach**: in *The Beginning of Infinity*, a good explanation applies far beyond the problem that produced it. Read in the cluster's terms, an addressable theory with reach is retention that later situations can consume without being re-derived.

That yields a conjecture worth stating sharply, because it is the kind of claim that could be measured and could be wrong. **Addressable retention promises better sample efficiency than non-reflective parametric learning, because one retained theory with reach covers future situations that would each otherwise cost gradient samples.** A parametric learner meets each new situation by paying for it in data; a theory with reach is paid for once and spends nothing further to apply.

## The prediction is located, not global

The conjecture does not say addressable retention is more sample-efficient everywhere. On-distribution, against a single-gradient objective, parametric compounding should win outright: the wire is the substrate itself, so nothing has to be retrieved, and the loss amortizes every past example into the weights automatically. There is no advantage for reach to exploit where the next situation is drawn from the same distribution the gradient already climbed.

The reflective advantage appears **off-distribution**, where samples do not transfer but theories do. A new region the training data never covered costs the parametric learner fresh gradient samples to fit; a theory whose reach already spans that region costs nothing new to apply. This is the located complement of the open question left standing in [reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — whether cumulative-but-opaque loops systematically outrun addressable ones on single-gradient objectives. The conjecture concedes that terrain to parametric learning and predicts the advantage flips exactly where the objective stops being single-gradient and on-distribution.

## Three qualifications, each sharpening the claim

**Weights have reach too; the differentiator is holding it criticizably.** Generalization *is* implicit reach — a network that classifies inputs it never saw has extended beyond its training set. So the reflective edge is not having reach but holding it in a form that can be *criticized*. An addressable theory's reach can be assessed by argument before it is deployed, extended to a new case without new samples, and corrected selectively at the point of failure — [selective revision](./reflection-buys-addressability-not-compounding.md) of the retained change *as an object*, where a bad weight update offers only indirect handles: train over it, roll it back wholesale, probe it from outside. The sample efficiency is not reach as such; it is *error-correcting* reach without paying for the corrections in samples.

**The gain is discounted by the wire.** Addressable retention compounds only best-effort, [since retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md). A theory with reach that no later search surfaces contributes nothing, while parametric retention cannot fail to be found — it is the substrate the next round runs on. The conjectured advantage is therefore an upper bound, and retrieval quality is the factor it is discounted by. A KB whose search reliably misses its most general note captures little of the sample efficiency its reach in principle promises.

**The saved samples reappear at the gate.** In a direct-determination pathway the evidence is samples by construction — gradients and rewards computed from data, spent directly by the update rule — so the sample cost is the price of the evidence channel itself. A theory whose reach outruns the available data cannot be adopted on that channel: no gradient reaches where there is no data. Adopting it is proposal-selection work, [since such a loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md), and the only oracle that can assess reach beyond the data is criticism — the judgment-heavy gate where [warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) and where, in a human-inclusive pathway, the human sits. A reflective pathway can skip the gate — an agent that unconditionally appends each failure's lesson writes addressably with no evaluator anywhere — but a gateless append carries no warrant beyond the episode that produced it, which is no reach at all. So the conjectured sample efficiency is bought at the oracle: it is warranted only as far as criticism is a reliable evaluator of claims the data cannot yet check.

## The dominant paradigm already relies on its reflective tier

The strongest evidence sits inside gradient descent's own world. The field's *meta-level* sample efficiency — the efficiency of the research loop that produces models, not of any one training run — is delivered by its reflective tier, not by its weights. Scaling laws are a theory with reach, retained in an addressable form (papers, plots, recipes), and they are precisely what lets a lab *not* train every candidate model to find out how it would have done. The compounding-as-knowledge that lets the field move faster than brute search happens in the literature and the recipes, in artifacts practitioners read, criticize, and extend — not in any model's parameters. The paradigm that wins on-distribution by parametric compounding buys its own off-distribution reach the reflective way.

## Open Questions

- Is the off-distribution crossover point measurable — can one exhibit a task family where an addressable theory demonstrably covers held-out regions at lower marginal sample cost than a parametric learner, holding retrieval fixed?
- How much of the conjectured advantage survives realistic retrieval? The discount is real; whether it leaves a usable margin is empirical.
- Does criticism-as-oracle actually evaluate reach that outruns data, or does it merely defer the sample cost to whenever the theory is finally tested against a case it was wrong about?

---

Relevant Notes:

- [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — grounds: supplies the transfer consequence this sharpens into a sample-efficiency claim, and the single-gradient open question this locates the complement of
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: why the conjectured advantage is an upper bound the retrieval wire discounts
- [Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) — mechanism: the evaluation gate the saved search-samples reappear at, warranted only as far as its oracle reaches
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the subtype architecture theory-adoption runs on, and the evaluation gate where the saved samples reappear
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the reflective/non-reflective central distinction, and the direct-determination arm whose evidence channel is samples by construction
