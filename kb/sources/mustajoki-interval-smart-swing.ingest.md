---
description: "Interval ratios bound trade-off weights in an additive model. A pairwise dominance test can settle a choice even when the alternatives’ overall score ranges overlap."
source: "https://sal.aalto.fi/publications/pdf-files/mmus03.pdf"
captured: "2026-11-21"
ingested: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
type: types/ingest-report.md
snapshot_sha256: c2f4adc693860e4b892e1ea124d1e2139ec468f3a83e4a56a6ca2589b0e870b7
occasion: "What can Commonplace conclude when a comparison leaves trade-off weights open?"
domains: [multicriteria decision analysis, interval weight ratios, pairwise dominance]
tags: [evaluation, robust-comparison]
---

# Ingest: Decision Support by Interval SMART/SWING

## Classification

Jyri Mustajoki, Raimo P. Hämäläinen and Ahti Salo of Helsinki University of Technology published this decision-analysis methods paper in *Decision Sciences* in 2005. They derive constraints on weights, simulate alternative ways to elicit those constraints and illustrate the method with a job choice.

## Summary

A decision maker chooses one attribute as a reference and gives an interval for the value of each other attribute’s worst-to-best improvement relative to the reference improvement. These judgments define a set of permissible weights for an additive value model. One alternative dominates another if its advantage is strictly positive throughout that set, allowing also for the stated ranges of attribute ratings. The choice of reference affects how many alternatives can be eliminated. In simulations that imposed the same proportional error on every ratio judgment, the most important reference attribute eliminated the most alternatives on average. A reference that permits more precise judgments can do better. A worked example in the authors’ WINPRE software illustrates how further judgments can narrow the remaining choice.

## Contribution assessment (our opinion)

The practical contribution appears to be a way to elicit incomplete preferences with one comparison per nonreference attribute. The authors adapt existing preference-programming mathematics and show that two equally short sets of questions can differ in how much they settle. The simulations isolate a consequence of choosing a reference under specified error assumptions. How precisely people can make those comparisons in practice remains open.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper gives a formal test for the worked trade-off in [On-balance judgments can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md). In that note, a revision helps on 90 tasks and hurts on 10. Under the note’s additive assumptions, a defensible upper bound below nine on the loss per harmed task relative to the gain per helped task establishes a strict preference for the revision. If the feasible ratios include nine, a tie is possible. If they extend to both sides of nine, the preferred option depends on the ratio. The judgment about which ratios deserve consideration still belongs to those deciding.

## Extractable Value

1. Compare both alternatives at the same weights. Separately computed score ranges can overlap because each extreme occurs at different weights. Minimizing the score difference over the shared feasible set can still establish dominance. [quick-win]
2. Direct further questions to comparisons that remain open. In the job example, B already dominates C and E. Establishing equal flexibility and equal enjoyment for A and D then allows A to dominate D. The remaining choice is between A and B. [quick-win]

## Limitations (our opinion)

The guarantee depends on the chosen attributes, their ranges, the additive representation and the credibility of the bounds. A consequence omitted from both alternatives’ scores cannot affect the test. Wide bounds can leave several alternatives undominated without establishing that they are equally good. The simulations impose error around generated weight ratios. They measure discrimination under that assumption and leave the accuracy and burden of real human elicitation untested.

## Recommended Next Action

Add a worked pairwise score-difference test to the 90-task/10-task example in the on-balance judgments note, showing exactly which admissible loss-to-gain ratios settle the comparison.
