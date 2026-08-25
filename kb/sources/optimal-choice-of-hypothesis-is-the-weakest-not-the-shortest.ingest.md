---
description: "Bennett's extension-size alternative to minimum description length, bounded by its uniform task prior and fixed representational decomposition"
source: https://arxiv.org/pdf/2301.12987v4
captured: "2026-08-04"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 9afff9545a5a9aab03d98b9c115b06cf0c50f52759b73934b22f30763ba0b621
ingested: "2026-08-04"
type: kb/sources/types/ingest-report.md
domains: [learning-theory, inductive-bias, generalisation, formal-methods]
---

# Ingest: The Optimal Choice of Hypothesis Is the Weakest, Not the Shortest

## Classification

A formal induction paper that states three propositions and supplements them with binary-addition and binary-multiplication experiments; the captured version is an arXiv preprint rather than an identified peer-reviewed publication.
Author: Michael Timothy Bennett (Australian National University). The paper provides an explicit formalism, proofs, quantitative tables, and a code-appendix reference, which makes its assumptions inspectable; it is a sole-author preprint, and this ingest did not independently verify the proof or reproduce the code.

## Summary

Bennett defines a finite implementable language whose statements denote sets of possible decisions, then calls a hypothesis's extension cardinality its **weakness**: a weaker statement excludes fewer possibilities. Assuming a uniform distribution over tasks in that language and induction from a child task to an unknown parent, the paper argues that choosing the valid hypothesis with the largest extension is necessary and sufficient to maximize generalisation probability, while minimum description length (MDL) is neither. In toy 8-bit addition and multiplication tasks, weakest-hypothesis selection attains 1.1–5 times the exact-generalisation rate of MDL and 1.03–1.56 times its average extent, depending on training-set size. The paper reads this as a challenge to compression-as-intelligence and as a possible explanation for the Apperception Engine's generalisation.

## Quotes

No source quotes have been retained yet.

## Connections Found

This source is most useful as a **bounded technical counterpoint** to the KB's DreamCoder and No Free Lunch material. DreamCoder shows a curated symbolic domain where a description-length gate participates in successful transfer, while No Free Lunch makes every strategy's advantage conditional on a problem distribution; Bennett supplies the missing constructive case where a different proxy wins after both the representation and distribution are fixed. Its proper theoretical home is therefore the boundary established by [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), not an unqualified replacement of MDL. It is also a clean worked example for the proof route in [formal symbolic systems assess explanatory-reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md): the theorem establishes reach inside its formal model while leaving the model-to-world translation outside the proof.

## Extractable Value

1. **Proxy optimality is relative to both a task distribution and a representational decomposition** -- Bennett's proof chooses a uniform prior over `Γᵥ` only after a finite vocabulary `v`, statement language, task definition, and parent/child relation determine what counts as a hypothesis and a success. Read with [No Free Lunch](./no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) and [DreamCoder](./dreamcoder-wake-sleep-bayesian-program-learning.ingest.md), this yields a higher-reach claim the KB does not yet state directly: “weakness versus description length” cannot be settled without naming both axes. [deep-dive]

2. **Weakness separates semantic permissiveness from syntactic brevity** -- Extension size measures how many decisions a statement admits; description length measures how the statement is written. The counterexample where a two-symbol model is weaker than a one-symbol model gives the KB a precise formal instance of why a shorter representation need not be a less specific commitment. This distinction is useful wherever compression is proposed as a proxy for transfer rather than merely for context cost. [quick-win]

3. **The paper is a compact proof-route case for assumption-relative reach** -- Unlike sampled held-out accuracy alone, the proposition quantifies over the modeled task space and therefore establishes a real within-model generalisation result if the proof holds. Its explicit uniform prior and finite vocabulary simultaneously expose the formalization boundary, making it unusually well-shaped evidence for the KB's existing formal reach-assessment note. [quick-win]

4. **DreamCoder's MDL gate now has a concrete rival worth isolating experimentally** -- The DreamCoder ingest already observes that its held-out transfer does not isolate description length from search and representation. Bennett suggests a sharper ablation: hold a symbolic hypothesis space and search procedure fixed, then compare a description-length gate with extension-size weakness on held-out tasks drawn from declared non-uniform as well as uniform distributions. [experiment]

5. **Generalisation is only one capacity objective** -- The paper's proxy is optimized for probability of task generalisation and inherits the cited equation of intelligence with generalisation. For Commonplace, [learning is not only about generality](../notes/learning-is-not-only-about-generality.md): reliability, speed, cost, and capacity-to-learn also matter. Weakness could therefore be the correct proxy for the paper's formal objective without being the right retention or design objective for an agent-operated KB. [just-a-reference]

## Limitations (our opinion)

The theorem's strongest language is conditional on the assumption doing most of the normative work: tasks are uniformly distributed over the paper's `Γᵥ`. Real task families are structured and non-uniform, which is why [No Free Lunch](./no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) treats useful inductive bias as distribution matching. The paper proves neither that its task measure reflects deployed problems nor that weakness remains optimal under a different prior. Its “necessary and sufficient” conclusion should be quoted with the language, task construction, and prior attached.

The experiments improve only inside a fixed decomposition. The conditioning signal is a static child task containing sampled situations and correct decisions; there is no additional interaction history. The available responses are decisions generated from statements in the finite propositional language, and the selectable mappings are exactly the models expressible in that language. Fixed outside the update space are the 256 eight-bit states, propositional representation and vocabulary, addition/multiplication task construction, child/parent relation, model-generation machinery, reconstruction rule, and choice to compare only weakness with MDL. Varying the proxy and number of examples shows which proxy performed better within that space. It does not validate the vocabulary, uniform-child sampling, binary-arithmetic decomposition, or the decomposition as a whole, exactly as [the fixed-decomposition lens](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts.

Empirically, the evidence is narrow: two operations over eight-bit strings, 75–256 trials per sample-size setting, and no comparison with other priors or complexity-aware proxies. Some headline relative gains start from very low absolute exact-generalisation rates (for multiplication at six examples, 0.05 versus 0.01), and Wald intervals are a fragile choice near zero. Computing extension cardinality is also tractable in this tiny finite domain; the paper does not show that weakness can be estimated cheaply enough to compete with description length in realistic hypothesis spaces.

The Apperception Engine explanation is plausible but not isolated: its universally quantified rules and task-tailored language change together, so the paper does not show that weakness rather than representation fit causes its performance. The closing claims about LLM fabrication, loss minimization, and grokking are research suggestions, not results tested by either the proof or experiments. Finally, the linked technical appendices and code were not part of this snapshot, so reproducibility and proof details beyond the ten-page paper remain unchecked.

## Recommended Next Action

Write a theoretical note under `kb/notes/` titled **“A hypothesis-selection proxy is optimal only relative to a task distribution and representational decomposition”**, using Bennett as the constructive weakness-over-MDL case, [No Free Lunch](./no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) as the distribution boundary, [DreamCoder](./dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) as the domain where MDL is useful, and the fixed-decomposition note to keep unvaried representation choices outside the evidential claim.
