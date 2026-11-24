---
description: "Boyd and Vandenberghe define cone-induced partial orders and Pareto minimality, giving Commonplace a way to screen routing remedies without forcing a winner."
source: https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
captured: "2026-11-24"
capture: pdftotext
capture_scope: excerpt
genre: textbook
snapshot_sha256: 3577749434d7d57007ee467608d876b13882bc17a5ee3d4f9639129a773251d6
ingested: "2026-11-24"
occasion: "Which comparisons between routing changes can a cone settle and when must the choice remain open?"
type: types/ingest-report.md
domains: [convex optimization, proper cones, partial orders, Pareto optimality]
---

# Ingest: Convex Optimization

## Classification

The [2004 textbook](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) develops mathematical definitions, properties, and worked examples rather than reporting an empirical study. The excerpts come from the corrected seventh printing (2009).

Author: Stephen Boyd and Lieven Vandenberghe, researchers in convex optimization and its applications.

## Summary

Section 2.4.1 defines a proper cone (convex, closed, with nonempty interior and no line) and uses it to order vectors: `x` is at most `y` when `y − x` lies in the cone. The strict inequality defined in the text requires the difference to lie in the interior. The nonnegative orthant gives ordinary componentwise comparison; other examples compare matrices or polynomials. Section 4.7.3 uses the nonstrict order to characterize Pareto optimality: a feasible outcome is minimal if no distinct feasible outcome is at least as good. A set can have several minimal outcomes and no minimum that is at least as good as every feasible outcome.

## Quotes

> Similarly, we define an associated strict partial ordering by
> x ≺K y ⇐⇒ y − x ∈ int K,
> --- `kb/sources/.snapshots/boyd-vandenberghe-convex-optimization.md` @ `sha256:3577749434d7d57007ee467608d876b13882bc17a5ee3d4f9639129a773251d6` — §2.4.1, p. 43

> The set f0 (x) − K can be interpreted as the set of values that are
> better than or equal to f0 (x), so the condition (4.59) states that the only achievable
> value better than or equal to f0 (x) is f0 (x) itself.
> --- `kb/sources/.snapshots/boyd-vandenberghe-convex-optimization.md` @ `sha256:3577749434d7d57007ee467608d876b13882bc17a5ee3d4f9639129a773251d6` — §4.7.3, p. 177

## Connections Found

The textbook supplies the mathematical basis for the cone comparison in [On-balance judgment with an LLM](../theory/on-balance-judgment-with-an-llm.md). With routing outcomes expressed as costs (lower is better), remedy A is no worse than B when the difference `B − A` between their cost vectors lies in the declared cone. This checks whether the difference is admissible under a stated rule; it does not establish which offsets to admit or predict how agents will route requests. [Necessary preference across compatible measures](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) also leaves comparisons open, but asks whether every admitted measure agrees on a direction. Neither rule supplies missing outcome evidence, and the excerpt does not establish that the two rules give the same verdicts.

## Extractable Value

1. **Separate dominance, ties, and incomparability.** With known outcome vectors and a fixed proper cone, a nonzero difference in the cone settles the comparison in one direction, even on the boundary where the textbook's strict inequality does not hold. Identical vectors tie on the declared criteria; distinct vectors are incomparable if neither direction passes. With the nonnegative orthant, better quotation routing and worse ordinary ingestion leave the choice open. A different cone can settle a mixed comparison only if it admits the relevant offset. [quick-win]
2. **Screen feasible remedies without ranking the survivors.** Apply any hard eligibility requirement before comparing outcomes. Then remove remedies with a distinct feasible outcome at least as good under the declared cone. A minimal outcome among the remedies considered is not necessarily a minimum, and several remedies can yield the same minimal outcome. [quick-win]

## Limitations (our opinion)

The result is conditional on the feasible set, the outcome representation, and the cone. The excerpt gives no basis for deciding whether ordinary ingestion reliability is a hard requirement, a loss that cannot be offset, or a cost that other gains can justify. The routing note distinguishes design checks from observed routing effects; the textbook provides neither those observations nor a way to infer them. Better measurement can establish an unknown difference, but cannot order a known difference that falls outside the cone in both directions. The capture is limited to §§2.4.1 and 4.7.3 and does not establish what the rest of the book offers for computing or selecting among efficient outcomes. Some order glyphs are damaged in extraction, and the drawing for Figure 4.8 is not reproduced.

## Recommended Next Action

Add one worked comparison to [On-balance judgment with an LLM](../theory/on-balance-judgment-with-an-llm.md) showing when the pointer and separate-skill remedies would be tied, ordered, or incomparable under a stated cone on quotation-routing and ordinary-ingestion outcomes.
