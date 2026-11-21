---
description: "Hoeffding bounds deviations of bounded sums, giving on-balance comparisons a reversal test when consequences share a scale and their dependence is understood."
type: types/ingest-report.md
source: https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf
captured: "2026-11-21"
ingested: "2026-11-21"
capture: indexed-pdf-text
capture_scope: full-source
doi: "10.1080/01621459.1963.10500830"
genre: scientific-paper
snapshot_sha256: 7610ab2bb4950e237af2cbf0f08c8baa9a7b1dec1e2815a27e8b6a6dc2b7ee6b
occasion: "When can many uncertain effects reverse an improvement judgment?"
domains: [concentration inequalities, bounded random variables, sampling without replacement]
---

# Ingest: Probability Inequalities for Sums of Bounded Random Variables

## Classification

Wassily Hoeffding's 1963 paper in the *Journal of the American Statistical Association* proves finite-sample probability inequalities and compares them with earlier bounds.

## Summary

Hoeffding gives upper bounds on the probability that a sum exceeds its expectation by a specified amount. For independent summands with known finite ranges, one bound uses only the sum of the squared range widths and the size of the deviation. The summands may have different distributions. Information about means or variances can sharpen the bounds. Separate arguments extend them to particular dependent sums, including U statistics, and to random sampling without replacement from a finite population.

## Contribution assessment (our opinion)

The paper makes a finite-sample tail guarantee calculable even when the individual distributions are unknown. Its comparison with earlier variance-sensitive bounds shows what precision the simpler range-only formula can cost. The proof for sampling without replacement seems especially valuable because it identifies when the independent-draw guarantee survives a change in sampling design.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the [on-balance judgment](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md), Theorem 2 supplies a test for the special case where consequences can be added on a common scale. Several individually small effects might together erase a gain. The theorem bounds that risk once their ranges, independence, and a positive expected margin have independent justification.

## Extractable Value

1. **Test the aggregate reversal.** Let the net gain equal a fixed gain plus independent random effects. If its expectation is at least $m>0$ and effect $i$ has range width $w_i$, applying Theorem 2 to the negated effects gives $P(\text{net gain}\le 0)\le\exp(-2m^2/\sum_i w_i^2)$ for a positive denominator. A small upper bound can settle a decision with a stated risk tolerance. A large upper bound leaves the risk unresolved. [quick-win]
2. **Identify shared errors before counting effects.** If every task is exposed to the same failure, its occurrence can change all outcomes together. Counting affected tasks as independent can make the reversal look arbitrarily unlikely. The paper's dependent cases require a specific sampling or dependence structure. [quick-win]

## Limitations (our opinion)

The inequalities bound departures from a true expectation. An omitted systematic loss can move that expectation across the decision threshold even when deviations around it are small. The theorem supplies neither a positive expected margin nor a way to weigh consequences measured in different units.

## Recommended Next Action

Add a worked example to the on-balance note showing how a fixed expected gain and known ranges bound reversal risk, with a shared-failure case to expose the role of independence.
