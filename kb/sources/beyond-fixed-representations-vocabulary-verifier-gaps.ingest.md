---
description: "Conceptual paper separates primitive invention from adaptive evaluation, sharpening Commonplace's fixed-decomposition analysis while leaving its autonomy ladder untested."
source: https://arxiv.org/abs/2607.09560
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 49bab5cb066cc69477c5c30b6c45fd24d0fa5256f267d17b2c9311df1060e31a
ingested: "2026-08-31"
type: kb/sources/types/ingest-report.md
domains: [open-ended-ai, representation, verification, agent-memory]
---

# Ingest: Beyond Fixed Representations: Vocabulary and Verifier Gaps

## Classification

This is a conceptual essay presented as an arXiv preprint: it synthesizes prior theories and systems into a taxonomy and a set of architecture directions, but reports no original intervention, benchmark, or controlled evaluation. Author: Yuan Cao and Haiqian Yang are identified authors; Yang's MIT email address and the paper's extensive bibliography provide limited credibility signals, while the source names no publication venue or peer-review status.

## Summary

The paper argues that stronger search, reasoning, and tool use do not by themselves produce open-ended innovation because current systems usually inherit both the primitives in which candidates are expressed and the criteria by which candidates are judged. It names two obstacles: a vocabulary gap in inventing, stabilizing, and reusing new primitives, and a verifier gap in valuing primitives whose payoff is delayed or cannot yet be expressed by the current evaluator. It formalizes primitive usefulness through amortized compression and bounded feasibility extension, classifies systems on a four-level ladder of vocabulary and verifier autonomy, and proposes representation-revision objectives, invention trajectories, persistent primitive stores, surrogate verifiers, and self-extending evaluation. The paper is useful as a diagnostic and design agenda, not as evidence that these mechanisms work.

## Quotes

- **Source extract (verbatim):** The ladder is organized in three dimensions: 1) Search pattern: is the system searching within a fixed representational space, or can it modify the space being searched? 2) Vocabulary autonomy: can it create and reuse new conceptual primitives? 3) Verifier autonomy: does it own the verifier and evolve it as needed, or is the success criteria supplied and fixed from outside?
  - **Source location:** Section 4, “Levels of Innovation Autonomy,” opening taxonomy paragraph

## Connections Found

The source is a conceptual framing and limitation for claims about open-ended agents. Its distinction between within-frame performance and frame change rests on [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), while its verifier gap gives a more specific account of why [open-ended improvement must allocate search before decisive evaluation is available](../notes/open-ended-improvement-allocates-search-before-evaluation.md). Its proposal for self-extending evaluation must also be bounded by [Revising an improvement objective is licensed from outside it or is not improvement](../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md), which distinguishes changing a verifier from changing the objective that licenses the change. The persistent-primitive lifecycle is a design companion to the [Commonplace agent memory gap plan](../reference/commonplace-agent-memory-gap-plan.md), and [DreamCoder](dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) supplies the clearest bounded comparison: its vocabulary grows inside a supplied task family, meta-language, and evaluator.

## Extractable Value

1. **Separate vocabulary autonomy from verifier autonomy** -- This two-gap diagnostic prevents strong search, self-rewrite, or library growth from being mistaken for control over what can be represented and how new representations are valued. It gives system reviews a higher-reach comparison axis than a single autonomy score. [quick-win]
2. **Value a primitive through amortized reuse and bounded feasibility extension** -- The proposed test asks whether a primitive repays its own representation cost across a task family and makes previously unreachable tasks reachable within a budget. It is a useful candidate criterion for durable abstractions, provided the externally chosen language, task family, and budget remain explicit. [deep-dive]
3. **Split verification delay from evaluator inexpressibility** -- Slow or expensive feedback is a credit-assignment problem with an eventual standard, whereas a primitive that changes what can be asked or measured may require a new standard. This distinction sharpens where surrogate verification suffices and where the evaluation frame itself is at issue. [quick-win]
4. **Measure innovation autonomy on multiple dimensions** -- Search-loop autonomy, vocabulary autonomy, and verifier autonomy can move independently. The ladder is not yet a measurement instrument, but its dimensions can improve case-by-case comparisons of systems such as DreamCoder, Voyager, and self-rewriting agents. [experiment]
5. **Treat invented primitives as revisable lifecycle candidates** -- The proposed store connects creation, retrieval, cross-task reuse, pruning, removal tests, and eventual consolidation. That sequence usefully specifies what persistent agent memory would need beyond merely accepting writes. [experiment]

## Limitations (our opinion)

The central contribution is a position and taxonomy, not an empirical result. The four-level ladder hand-classifies heterogeneous systems without a scoring procedure, controlled comparisons, or evidence that vocabulary and verifier autonomy are the decisive missing variables. Historical examples of concepts that later became useful illustrate delayed value but do not establish an implementable mechanism for inventing or selecting primitives. The formal criteria also take the language, task family, search budget, regularizer, and higher-level objective as supplied, so they may relocate rather than remove the fixed-decomposition problem identified in [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Finally, self-extending evaluation is underspecified: the paper acknowledges evaluator gaming, objective drift, and harmful primitives, but it does not provide a governance rule that distinguishes revising a proxy under a retained objective from revising the terminal objective itself.

## Recommended Next Action

Revise [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) with a bounded worked distinction between vocabulary autonomy and verifier autonomy, using DreamCoder as the scaffolded case and preserving the note's warning that the task family, meta-language, and objective remain externally fixed.
