---
description: "Weco's evaluation guidance makes benchmarks revisable against user outcomes, but supplies no evidence that its automated systems perform that criticism."
source: https://www.weco.ai/blog/eval-is-not-a-tool-you-install
captured: "2026-09-27"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 29e6c1a11a3015bb2f0c733a7a2835cca42d00a2f6bc34f83d737adeffcc58dd
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [evaluation, agent-development, learning]
learning_claims: true
---

# Ingest: How to Build a Good Eval

## Classification

A conceptual essay giving evaluation design advice, illustrated with hypothetical failure cases rather than reported experiments. Zhengyao Jiang writes on Weco's company blog; the source establishes his stated evaluation philosophy, not independent evidence of Weco product behavior.

## Summary

The [essay](https://www.weco.ai/blog/eval-is-not-a-tool-you-install) treats evaluation as constructing an offline proxy for real utility and revising it through experience. It separates fidelity to the intended outcome, signal sufficient to discriminate candidate solutions, and execution cost. To limit overfitting, it recommends frequent optimization against validation data and rare checks against held-out test data; a widening gap should prompt broader validation coverage. Consistently solved cases move to a cheap regression suite, while disagreement between high scores and user experience prompts review of the metric or sample. These are methodological recommendations without reported outcome measurements.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the prospective Weco/AIDE² case, this source supplies a stated position on criticizing evaluation assumptions. Compared with the [theory-builder definition](../notes/definitions/theory-builder.md), that position identifies a possible object of reflective criticism but does not establish an implemented criticism process. It also gives a concrete application of [the distinction between implementing a requirement and validating it against the objective](../notes/exact-implementation-does-not-validate-a-requirement.md): an accurately computed score can remain a poor guide to user benefit. Its value is this boundary on interpretation, rather than evidence of autonomous reflection.

## Learning Claims (our opinion)

The proposed mechanism is an engineering loop in which developers compare agent variants using a benchmark, check generalization with separate data, and revise the benchmark when its signal or fidelity fails. In our terms, candidate improvement occurs inside one evaluation arrangement, while developers can also change that arrangement. This bears on [learning within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): optimizing an agent against a fixed metric cannot itself validate the metric's connection to utility. The essay advocates making that connection open to criticism, but does not report a comparison between fixed and revisable evaluators.

Against the four theory-builder conditions, **localized content** is plausible in explicit metrics, datasets, and prompts, but the essay supplies no retained theory artifact from a working system. **Consumption** is prescribed through using scores to decide between variants, without an observed decision trace. **Content-directed criticism** appears in the instruction to reconsider metric and data assumptions when user experience disagrees; it is advice to practitioners, not demonstrated automated criticism of an identified assumption. **Iteration** is explicitly recommended through revising validation data and benchmark design, but no run shows a particular criticism shaping a later revision. The intended persistence spans repeated development and release cycles; storage, later retrieval, and transfer across problems are unspecified.

The declared boundary therefore matters: humans perform the proposed diagnosis and evaluator revision. The article does not establish whether Weco's automated systems do so. It reports neither improved capacity for future action nor compounding improvement. It also leaves model-weight changes unspecified, so it cannot establish fixed-model learning. These limits leave membership open without counting missing evidence as absence.

## Extractable Value

1. **Separate evaluation philosophy from implemented reflection.** The essay supports attributing revisable evaluation standards to Weco's published guidance; it cannot establish that AIDE² performs the corresponding criticism. This distinction directly limits the proposed case study. [quick-win]
2. **Keep two revision targets visible.** Candidate quality and evaluator validity require different evidence. Held-out checks address generalization under the scoring setup; disagreement with users can question that setup itself. This is a reusable diagnosis for an improvement loop whose scores rise without corresponding benefit. [quick-win]
3. **Preserve regression coverage while changing the improvement benchmark.** Moving saturated cases to cheaper regression checks retains a check on old capabilities while shifting expensive evaluation toward discriminating examples. This is an untested operational recommendation here. [just-a-reference]

## Limitations (our opinion)

There are no experiments, sample sizes, evaluation artifacts, or runtime traces. The three-way tradeoff among fidelity, signal, and cost is a useful design frame, not an experimentally validated optimization method. Separate test data can expose overfitting to validation cases, but the same unsuitable metric on both sets can still miss real utility. User dissatisfaction is a reason to investigate the proxy, not proof that only the metric or data caused failure.

The sharp contrast between inspectable software and opaque models simplifies both: readable software can still rest on wrong requirements, and empirical checks do not resolve every ambiguity in intended outcomes. The company-blog context favors the author's evaluation framing; it provides no comparative evidence about the named evaluation platforms. Nothing in this article establishes AIDE²'s implementation, autonomy, retained learning, or compounding.

## Recommended Next Action

Use this source in the Weco/AIDE² addition to `kb/articles/which-existing-self-improving-systems-are-theory-builders.md` to attribute the published recommendation to criticize evaluation assumptions, keeping any claim that AIDE² implements that process dependent on separate implementation evidence.
