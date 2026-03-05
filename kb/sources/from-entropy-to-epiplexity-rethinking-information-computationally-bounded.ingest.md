---
source_snapshot: from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md
ingested: 2026-03-05
type: scientific-paper
domains: [information-theory, machine-learning, computational-complexity, learning-theory]
---

# Ingest: From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence

Source: from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md
Captured: 2026-03-05
From: https://arxiv.org/html/2601.03220v1

## Classification

Type: scientific-paper -- Peer-reviewed preprint from CMU/NYU researchers with formal definitions, theorems, proofs, and empirical measurements. Introduces a new information-theoretic quantity with mathematical rigor.

Domains: information-theory, machine-learning, computational-complexity, learning-theory

Author: Marc Finzi, Shikai Qiu, Yiding Jiang, Pavel Izmailov, J. Zico Kolter, Andrew Gordon Wilson (Carnegie Mellon University, New York University). Strong ML theory group; Wilson's lab is well-known for work on generalization and Bayesian deep learning. Kolter has significant contributions to optimization and robust ML.

## Summary

The paper introduces "epiplexity" (epistemic complexity), a new information measure that quantifies structural information extractable by computationally bounded observers. Classical information theory (Shannon entropy, Kolmogorov complexity) assumes unbounded computation and thus cannot explain why synthetic data improves capabilities, why data ordering affects learning, or how AlphaZero extracts strategy from simple rules. Epiplexity resolves these paradoxes by separating information into two components: time-bounded entropy (irreducible randomness given computational constraints) and epiplexity (learnable structural patterns visible within those constraints). The key insight is that the same data can appear structured or random depending on the observer's computational budget -- information is observer-relative. The authors provide both theoretical results (CSPRNGs have zero epiplexity; high-epiplexity distributions provably exist) and practical measurement methods (prequential and requential coding) that consistently rank datasets by extractable structure.

## Connections Found

The `/connect` phase discovered 7 connections across the knowledge base, revealing that epiplexity provides theoretical grounding for several concepts the KB already discusses operationally:

1. **[context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** -- grounds: Epiplexity formalizes the complexity dimension of context cost. The note already identifies two cost axes (volume and complexity); epiplexity provides the theory for why growing context windows don't solve the complexity axis -- more tokens don't make computationally inaccessible structure extractable.

2. **[learning-is-not-only-about-generality](../notes/learning-is-not-only-about-generality.md)** -- extends: Epiplexity adds a prior dimension to capacity decomposition. Before trading generality for compound gains, you need to know how much learnable structure the data actually contains for a given observer.

3. **[distillation](../notes/distillation.md)** -- grounds: Distillation is operationally what epiplexity measures theoretically. The context budget shaping a distillation IS a computational bound; epiplexity explains why tighter budgets extract less.

4. **[bitter-lesson-boundary](../notes/bitter-lesson-boundary.md)** -- extends: Epiplexity predicts where on the bitter lesson gradient a problem sits. High epiplexity = much hidden structure = will eventually be bitter-lessoned. Low epiplexity = structure already captured = won't.

5. **[discovery-is-seeing-the-particular-as-an-instance-of-the-general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)** -- grounds: The note's claim that recognition cost scales with abstraction depth is formalized by epiplexity -- more computation reveals deeper structural patterns.

6. **[structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md)** -- grounds: Epiplexity explains WHY structured templates improve generation. Structured context has higher epiplexity for a bounded LLM. The paper's finding that data ordering affects learning directly supports this.

7. **[induction-bias-sequence-models-ebrahimi-2026](./induction-bias-sequence-models-ebrahimi-2026.md)** (source-to-source) -- extends: The induction bias paper's finding that different architectures extract dramatically different amounts of structure from the same data is exactly what epiplexity predicts.

A synthesis opportunity was flagged: several KB notes independently discuss observer-dependent information extraction (context efficiency, distillation, discovery, bitter lesson boundary). Epiplexity could be the theoretical anchor unifying them under the theme "information value is observer-relative because extraction requires computation."

## Extractable Value

1. **Formal measure for "complexity cost" of context** -- The KB's context-efficiency note identifies complexity as a cost dimension but lacks a formal measure. Epiplexity provides one: time-bounded MDL decomposition. This could sharpen the note's argument from intuitive to precise. [deep-dive]

2. **"Deterministic transformations create information for bounded observers"** -- This resolves a real tension in how the KB talks about distillation and structure. If structure is a deterministic transformation of raw content, classical theory says it adds no information. Epiplexity says it does, for bounded observers. This reframes distillation as information creation, not just compression. [quick-win]

3. **Prequential coding as a practical measurement method** -- Area under the loss curve above final loss estimates epiplexity. This is computationally cheap and could be used to compare context-loading strategies, distillation quality, or note structures by measurable extractability rather than intuition. [experiment]

4. **Epiplexity as a predictor of bitter-lessoning** -- High epiplexity problems have hidden structure that better compute will extract, so they'll eventually be automated. Low epiplexity problems are already fully captured. This gives the bitter-lesson-boundary note a concrete predictive tool. [quick-win]

5. **Data ordering effects have theoretical explanation** -- The paper's Paradox 2 (factorization dependence) explains why curriculum design, structured prompts, and note ordering in context windows matter. The same content in different arrangements has different epiplexity for a given model. This grounds the KB's structure-activates-higher-quality-training note in theory. [just-a-reference]

6. **Synthesis note: "Information value is observer-relative"** -- The connection report flagged that context-efficiency, distillation, discovery, and bitter-lesson-boundary all independently discuss bounded-observer phenomena. Epiplexity provides the formal framework to unify them. This is the highest-value extraction: a note that ties four existing threads together with a theoretical anchor. [deep-dive]

## Recommended Next Action

Write a note titled "Information value is observer-relative because extraction requires computation" connecting to [context-efficiency-is-the-central-design-concern-in-agent-systems.md](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [distillation.md](../notes/distillation.md), [bitter-lesson-boundary.md](../notes/bitter-lesson-boundary.md), and [discovery-is-seeing-the-particular-as-an-instance-of-the-general.md](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md). It would argue that these four notes describe the same underlying phenomenon -- computational boundedness determines what information is usable -- and that epiplexity (from this paper) provides the formal framework unifying them. The note would ground the KB's operational intuitions in information theory and make the "complexity dimension" of context cost precise rather than hand-wavy.
