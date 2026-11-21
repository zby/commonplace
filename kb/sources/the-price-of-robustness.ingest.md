---
description: "Bertsimas and Sim bound simultaneous adverse deviations in a linear constraint, giving a reversal test for judgments with a measurable margin."
source: https://web.mit.edu/~dbertsim/www/papers/melvyn/The-Price-Of-Robustness-OR52.pdf
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
doi: "10.1287/opre.1030.0065"
genre: scientific-paper
snapshot_sha256: 8ca923fa2f1de560247f67b93355973040dd882a77a33a57d8cacbfdef3032cd
ingested: "2026-11-21"
occasion: "When can many uncertain effects reverse an improvement judgment?"
type: types/ingest-report.md
domains: [robust optimization, budgeted uncertainty, constraint violation]
---

# Ingest: The Price of Robustness

## Classification

Dimitris Bertsimas and Melvyn Sim, researchers at MIT, published this paper in *Operations Research* in 2004. They prove properties of a robust optimization model and examine its cost on numerical examples.

## Summary

Bertsimas and Sim give each linear constraint its own budget for uncertainty. Each coefficient can move within a stated interval, and the budget caps the sum of the fractions of maximum deviation used in that row. For a fixed decision, the worst case spends the budget on the coefficients whose movement has the greatest adverse effect. The authors show how to optimize against that worst case with a linear formulation that also accommodates integer decisions. Separately, they bound the probability of violating a row when its coefficient deviations are independent, bounded and symmetric. In their knapsack example, increasing protection while holding the item set and weight uncertainty model fixed costs 1.54% of nominal objective value for a violation probability bound of 0.57%. In the Netlib PILOT4 example, many rows contain few uncertain coefficients, and stringent probability bounds cost nearly as much as full protection.

## Contribution assessment (our opinion)

The paper solves a practical difficulty with protecting every coefficient against its worst value at once. An adjustable budget lets a modeler trace the cost of progressively stronger guarantees while retaining linear constraints. The proof establishes that formulation for the stated uncertainty set. The numerical examples suggest that partial protection can yield a worthwhile saving, but its size depends on the problem.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies a quantitative case for the reversal question in [On-balance judgments can guide improvement without a global measure](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md). When a change has a measurable advantage and uncertain effects add in the same units, a reviewer can ask how much simultaneous adverse movement would erase it. The paper supplies the calculation. Evidence about the work must establish which joint movements are plausible.

## Extractable Value

1. **Find the budget that erases the advantage.** For a fixed choice, rank each effect by the loss its maximum deviation could cause. Add losses from the top down, using a fraction of the next loss if needed. The budget at which their sum equals the nominal advantage permits a tie. A larger attainable loss permits reversal. This gives a test even when each effect alone looks too small to investigate. [quick-win]
2. **Identify shared causes before assigning probabilities.** The deterministic budget calculation needs bounds on joint movement. A probability bound additionally needs a model of dependence. The paper treats correlated coefficients driven by independent, bounded, symmetric factors by applying protection to the underlying factors. A single shared cause can then move several coefficients together. [experiment]

## Limitations (our opinion)

The protection covers effects represented in the constraint and deviations admitted by its budget. Choosing comparable units, identifying omitted effects, and estimating bounds all require evidence outside the optimization. The examples vary protection within specified models. They do not establish that the chosen intervals or dependence assumptions describe future observations. A per-row probability bound alone also leaves open the probability that any of several rows will fail.

## Recommended Next Action

Add a worked budget calculation to the instruction-revision example in [On-balance judgments can guide improvement without a global measure](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md), showing when several individually tolerable losses together erase the measured gain.
