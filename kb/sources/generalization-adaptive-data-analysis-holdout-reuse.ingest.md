---
description: "Adaptive evaluation makes later candidates depend on reused holdout data; limited-information interfaces can preserve statistical validity under explicit budgets."
source: https://arxiv.org/abs/1506.02629
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 212221a3e55a960383c30a21646344fff69b16be99ecbec74447db96bd28518f
ingested: "2026-09-17"
occasion: "Why a sequence of evaluations that each guides the next revision invalidates ordinary generalization arguments; what protocols restore it; what this implies for reusing review criteria across revisions."
learning_claims: true
type: kb/sources/types/ingest-report.md
domains: [adaptive-data-analysis, generalization, evaluation, theory-refinement]
---

# Ingest: Generalization in Adaptive Data Analysis and Holdout Reuse

## Classification

This is a theoretical computer science paper with formal definitions, generalization theorems, two reusable-holdout algorithms, and a synthetic experiment illustrating their practical motivation. Author: Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Aaron Roth, researchers affiliated at publication with Microsoft Research, IBM Almaden, Google Research, the University of Toronto, Samsung Research America, and the University of Pennsylvania.

## Summary

Ordinary generalization guarantees for an analysis procedure assume that the procedure, including the choices supplied to it, is fixed independently of the sample on which it is evaluated. In an adaptive sequence, each evaluation result can shape the next hypothesis or analysis, so later procedures indirectly depend on the reused data and their individual guarantees no longer compose. The paper shows that controlling how much information evaluation releases can restore guarantees: differential privacy supplies stability under adaptive composition, short output descriptions bound the number of possible transcripts, and approximate max-information unifies these routes. Its Thresholdout and SparseValidate protocols reuse a holdout by revealing little when validation succeeds and spending a bounded failure budget when it does not. A synthetic variable-selection experiment illustrates both severe overfitting to an ordinary reused holdout and its prevention by Thresholdout.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical basis for the statement in [A complete theory path does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md#interpretation-is-not-reach-assessment) that a critic's independence is an evidence question: an evaluation can be independent in authorship yet lose statistical independence when its outputs repeatedly guide revisions tested on the same evidence. It also supplies a statistical limit for the review workflow described in [Review system architecture](../reference/review-architecture.md). Freshness of a note-criterion pair records whether inputs changed, but does not by itself preserve generalization when outcomes from repeated reviews guide later versions. Reusing a criterion's text is not alone the paper's failure mode; the relevant dependence arises when revisions adapt to outputs drawn from the same finite evaluation evidence or holdout.

## Learning Claims (our opinion)

On the paper's terms, the adaptive mechanism is a transcript: each procedure receives earlier outputs, chooses its next analysis accordingly, and thereby acquires dependence on the fixed dataset. The remedy does not prohibit adaptation. It constrains the information that the transcript can reveal, using stability, description length, or their common max-information account, so later adaptive choices can retain population-level guarantees.

For Commonplace, this qualifies how empirical cases can guide a [theory builder's](../notes/definitions/theory-builder.md) criticism (condition 3). A sequence of revisions may fit every observed review outcome while losing warrant beyond the repeatedly consulted evidence. Independent criticism therefore needs an exposure protocol as well as a separately authored evaluator: fresh held-out cases, a validity-preserving limited-information interface, or a final untouched evaluation can keep the revision path from consuming its own test. This supports the separation between interpretation and reach-assessment in [A complete theory path does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md#interpretation-is-not-reach-assessment). The paper proves results for randomized algorithms over datasets, however, so applying its guarantees to semantic LLM review requires a new formalization rather than a direct transfer.

## Extractable Value

1. **State the exact invalidation mechanism for iterative review.** Once an evaluation result guides the next revision, the later candidate depends on the reused evaluation data through the result transcript; a one-shot generalization argument that fixes the candidate independently of those data no longer applies. [quick-win]
2. **Distinguish criterion reuse from evidence reuse.** Reapplying the same criterion text is not by itself adaptive holdout reuse. The hazard appears when the criterion repeatedly exposes judgments based on the same finite cases, judge state, or other evaluation evidence and those judgments guide later candidates. [quick-win]
3. **Treat evaluation feedback as an information budget.** Binary pass/fail or thresholded feedback can support more adaptive rounds than unrestricted scores or detailed diagnostics because it exposes fewer distinctions about held-out evidence; failures that disclose corrections consume a bounded budget. [deep-dive]
4. **Add protocol options for revision sequences.** Fresh evidence per round, a reusable-holdout mechanism with explicit assumptions and budgets, or an untouched final evaluation can restore a defensible generalization claim; ordinary cross-validation does not solve dependence when the same data serve adaptive selection and final validation. [deep-dive]
5. **Preserve the fixed-decomposition boundary of the experiment.** The synthetic study varies ordinary holdout access versus Thresholdout within a fixed data distribution, train/holdout split, variable-selection routine, linear-threshold hypothesis class, and feedback interface. Its gains support the tested access protocol in that setup, not the general optimality of those fixed choices. [just-a-reference]

## Limitations (our opinion)

The strongest results are mathematical guarantees under explicit probabilistic assumptions, privacy or transcript-size bounds, parameter budgets, and usually sampled data. They do not directly establish validity for qualitative criteria, stateful language-model judges, non-i.i.d. cases, changing tasks, or a review corpus without a defined population. The experiment is synthetic and uses a modified Thresholdout configuration whose parameter choices are described as sufficient for the demonstration rather than covered directly by the stated proof; it illustrates the mechanism but is narrow empirical evidence. Its available signals are training data and prior validation responses, its operations select variables and compose a linear threshold classifier, and its hypothesis class and data-generating regimes are fixed. The comparison therefore tests holdout-access protocols inside that effective update space, not alternative representations, revision operators, judges, or task decompositions. The authors also identify practical deployment and stronger bounds as open work.

## Recommended Next Action

Update [A complete theory path does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md) to distinguish evaluator independence from validity under adaptive reuse, and state that repeated outcome-guided revision needs fresh held-out evidence, a bounded-information reuse protocol, or an untouched final evaluation.
