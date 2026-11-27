---
description: "When comparing commutes, pooling fares and parking fees while keeping punctuality separate distinguishes a gain from a trade-off that neither route wins."
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [evaluation, robust-comparison]
---

# A dominance cone can allow some offsets but not others

When two costs draw on the same budget at the same rate, comparing their sum lets a saving in one offset an increase in the other. A dominance cone can allow that offset without letting the saving compensate for a loss on a protected outcome. The rule settles only the comparisons licensed by those choices.

A dominance cone is a set of differences that count as no worse. With outcomes oriented so higher is better, one option is no worse than another if the change from the second to the first lies in the cone. This is the generalized order in [Boyd and Vandenberghe, *Convex Optimization*, §§2.4.1 and 4.7.3](../sources/boyd-vandenberghe-convex-optimization.ingest.md). Their strict cone inequality requires an interior difference. A **strict Pareto gain** here is a nonzero difference in the cone: one outcome improves and none worsens. It need not be an interior difference.

## Is a cheaper commute a better commute?

Suppose a commuter compares two stations over the same 100 workdays. Let `s` be the change in the number of on-time arrivals, and let `a` and `b` be the dollars saved on fares and parking. A higher bill counts as a negative saving. For this comparison hold other features fixed. The commuter pays both bills from the same budget but will not call a less reliable trip an improvement on the strength of the savings alone. The textbook supplies the comparison rule; the commuter supplies the reason to pool these particular costs.

Compare the pair `(s, a + b)` with zero using the nonnegative quadrant: the new trip is no worse if neither coordinate is negative. The same test on the raw differences is `s ≥ 0` and `a + b ≥ 0`.

| Change in on-time arrivals | Fare dollars saved | Parking dollars saved | Verdict on the new trip |
|---:|---:|---:|---|
| 0 | 8 | −3 | **Gain.** Eight dollars off the fare covers three dollars more for parking, leaving five dollars saved without a decline in punctuality. This is a strict Pareto gain on the cone boundary, not an interior gain. |
| 0 | 8 | −8 | **Tie.** Both compared coordinates are unchanged. |
| −1 | 8 | −3 | **Incomparable.** The new trip has one more late arrival; the old trip costs five dollars more. Neither dominates, so the cone leaves the choice open. |
| 0 | −8 | 3 | **Loss.** The new trip costs five dollars more for the same punctuality. The old trip dominates. |

The tie in the second row need not mean identical bills. Moving any amount from fares to parking leaves total cost unchanged. In raw coordinates, the cone therefore contains a whole line of changes `(0, t, −t)` that count as no worse in **both** directions. Pooling maps that line to zero. The cone on the two compared outcomes is **pointed**: only zero ties in both directions.

## Scope

A protected outcome may improve; it need not stay fixed. If punctuality is an eligibility requirement instead, a trip with more late arrivals is ruled out, not left incomparable. If an employer reimburses fares but not parking, pooling the posted prices misstates the cost to the commuter. [Necessary preference across compatible measures](./necessary-preference-can-guide-improvement-without-a-global-measure.md) addresses the case where more than one valuation remains defensible. Missing outcome evidence is a different reason to leave a choice open: measurement can resolve it, but cannot settle an already known difference that the declared cone leaves incomparable.

---

Relevant Notes:

- [On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md) — exemplifies: the commute makes the comparison rule explicit without replacing the causal checks that establish its inputs
