---
description: "FunSearch supplies bounded evidence for frozen-model search that selects and reuses localized programs while its evaluator and skeleton remain fixed."
source: https://www.nature.com/articles/s41586-023-06924-6
captured: "2026-08-29"
capture: user-supplied-pdf-to-markdown
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 641e90a266e4218ed7d4e1a618340650d10cb21121db9e280cf64b0cd24e54f6
ingested: "2026-08-29"
occasion: "determine whether each system supplies existence evidence for the register’s selected-localized cell, without borrowing its mechanism, and therefore whether the shared response is an `instance`"
type: kb/sources/types/ingest-report.md
domains: [program-search, agent-learning, scientific-discovery]
---

# Ingest: Mathematical discoveries from program search with large language models

## Classification

This is a peer-reviewed scientific paper reporting a program-search method, benchmark experiments, and new mathematical constructions. Author: researchers from Google DeepMind, the University of Wisconsin–Madison, and the University of Lyon, including specialists who analysed the cap-set results; the paper discloses that its authors planned a Google DeepMind patent application on related subject matter.

## Summary

FunSearch couples a frozen code-generating LLM with executable correctness and performance evaluation, an island-based program database, and prompts built from selected programs to evolve one function inside a user-supplied program skeleton. The paper reports a larger eight-dimensional cap set, improved asymptotic cap-set lower bounds obtained through discovered admissible-set structure, and online bin-packing heuristics that outperform first fit and best fit on the tested distributions. It is a strong record that this compound configuration can produce verifiable localized programs on efficiently scored problems, but it does not show that the fixed function boundary, evaluator, or search architecture is generally preferable.

## Quotes

No source quotes have been retained yet.

## Connections Found

As a primary empirical anchor, the paper supplies bounded existence evidence for [The bitter lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) and a concrete realization of [a proposal-selection improvement loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). For the supplied occasion, FunSearch warrants an `instance` response in the selected-localized cell: the pretrained LLM remains frozen while localized function programs are proposed, invalid candidates can be rejected, scored candidates are retained, and retained programs shape later proposals. This role does not transfer FunSearch's island model, prompt construction, evaluator, or program skeleton as the cell's mechanism. The paper also provides the primary case behind the fixed-weight symbolic-search example in [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md).

The experiment also illustrates the boundary in [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Proposal generation can condition on selected program implementations ordered by score and on the supplied function interface; selection can condition on execution validity and per-input scores. The response space consists of program bodies expressible through that isolated function under the available language, imports, primitives, and runtime limits. The LLM's effective hypothesis class maps this prompt context to such programs. Model weights, the problem specification, evaluator, skeleton, function boundary, training inputs, score aggregation, prompt format, and island-selection policy remain outside that update space. Improvement therefore supports the sufficiency of the compound setup on the tested problems, not the independent validity of those fixed choices.

## Extractable Value

1. **The occasion-specific classification is `instance`.** FunSearch directly realizes the selected-localized pattern through a frozen proposer, reject-capable evaluation, and operative retention of localized program functions; no FunSearch-specific search mechanism needs to be borrowed to make that existence claim. [quick-win]
2. **The programs database makes retention operational rather than archival.** Accepted programs are sampled into later prompts, so retained artifacts alter subsequent search instead of merely recording its history. This sharpens the proposal-selection loop with a non-reflective, experimentally used case. [quick-win]
3. **The result separates adaptation inside an update space from the design of that space.** Candidate functions can vary broadly, but the evaluator, skeleton, exposed function, and search policy are fixed. The gains show that the chosen decomposition was sufficient for these runs, not that excluded decompositions would be worse. [deep-dive]
4. **Searching over concise programs can expose human-usable structure.** Inspection of a discovered admissible-set program revealed symmetry that domain experts then used to restrict the search and improve the bound further. This is useful evidence that a localized symbolic artifact can mediate a human–search feedback loop, although the paper does not isolate concision as the cause. [just-a-reference]
5. **The working regime is sharply bounded by evaluator quality.** The authors identify efficient evaluation, rich graded feedback, and an isolatable function as favorable conditions, making FunSearch a useful case for [the verifiability gradient](../notes/verifiability-gradient.md), not evidence for the same response on weakly scored tasks. [just-a-reference]

## Limitations (our opinion)

The evidence is concentrated in cap-set construction and online bin packing, both of which permit repeated executable checks and informative scores. It should not be generalized to theorem proving, open-ended inquiry, or other domains without comparable evaluation. The direct eight-dimensional cap-set result was rare—four successes in 140 experiments—and the system used roughly one million LLM samples plus substantial distributed evaluation, so reported best results do not establish routine efficiency or robustness. First fit and best fit are useful bin-packing baselines but do not exhaust prior hyper-heuristic approaches discussed by the paper.

The experiments optimize only the isolated function exposed by a human-written specification and skeleton. Component comparisons can support only the choices they vary; they do not establish that the fixed evaluator captures the deployment objective, that the selected function boundary is the best decomposition, or that the LLM rather than the broader evolutionary system causes the discoveries. Claims about a low-Kolmogorov-complexity bias and general interpretability are plausible interpretations of the outputs, not isolated causal findings. The implementation and experiments were not independently executed for this ingest, and OCR and page-order artifacts in the Markdown conversion make the canonical article preferable for exact code, formulas, and figure details.

## Recommended Next Action

Record FunSearch's response in the register's selected-localized cell as `instance`, citing this ingest only for existence of the frozen-proposer, evaluator, and operative-retention configuration and excluding its skeleton, prompt, island, and scoring machinery from the shared mechanism.
