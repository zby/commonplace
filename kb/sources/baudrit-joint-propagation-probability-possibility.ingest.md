---
description: "Event-probability bounds for mixed random and imprecise inputs depend on whether one unknown value holds across trials and how the observations are related."
source: "https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.329.4285&rep=rep1&type=pdf"
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 337f7ef2a9d1ec82900d77864ce17c760218892d0cde317f8cca7d5b0e59a36a
ingested: "2026-11-21"
occasion: "How can a comparison handle both stochastic outcomes and imprecise inputs?"
type: types/ingest-report.md
domains: [imprecise probability, possibility distributions, random sets, risk analysis]
---

# Ingest: Joint Propagation of Probability and Possibility in Risk Analysis

## Classification

Cédric Baudrit, Inés Couso and Didier Dubois present a theoretical paper in risk analysis. The authors, affiliated with the universities of Toulouse and Oviedo, derive event-probability bounds and illustrate their assumptions with a two-stage game.

## Summary

A player picks one of two keys with equal probability. One pays €1,000. An additional reward is known only through nested ranges. The same ranges give different information about the total payout depending on how the reward is set. A fixed additional reward must take the same value whichever key is drawn. An unknown reward that can vary with the draw allows more possibilities. When the draw itself determines which range applies, its joint occurrence with that range supplies information lost from the separate input descriptions. The paper derives lower and upper probabilities for output events under these assumptions. For the independent-information and fixed-parameter models, it shows how to recover the probability interval by averaging the lower and upper endpoints of the level sets of a fuzzy event probability.

## Contribution assessment (our opinion)

The strongest result is an explanation of why existing propagation methods can disagree even when analysts give them identical marginal inputs. The game isolates the effect of fixing an unknown across draws. Its upper probabilities for cumulative payouts agree with those of the more permissive model, yet the upper probabilities for particular payouts can differ. The proofs also specify what survives when a graded assessment of event probability is reduced to one interval. These are reasons to choose a calculation on substantive grounds. Their practical impact depends on whether analysts can identify the observation process in an application.

## Quotes

No source quotes have been retained yet.

## Connections Found

The routing-line example in [On-balance judgments](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) asks how often a new instruction might cause costly rework. The paper supplies a calculation for one part of that judgment. Given a task distribution and credible ranges for rework, an evaluator can bound the probability that the cost exceeds a specified threshold. Whether one uncertain cost applies to every task or the range depends on the task changes which outcomes can contribute to the bound. Choosing what cost is tolerable remains an operator judgment.

## Extractable Value

1. **Hold a shared parameter fixed across outcomes.** For each admissible value, first compute the event probability over random outcomes. Within each nested input range, take the smallest and largest such probabilities, then average the endpoints using the masses assigned to the ranges. Allowing a different value for every outcome can widen the bounds by admitting combinations the fixed parameter rules out. [experiment]
2. **Identify what the observations share.** When a single occurrence determines both the random outcome and the range observed for another input, use their joint frequencies if known. Multiplying the marginal frequencies assumes independence of the observation processes and can change the result. [quick-win]

## Limitations (our opinion)

The proofs establish consequences of specified input descriptions. The worked game supplies its probability law and nested ranges by construction. It offers no empirical test of how well an expert can supply such ranges or how accurately the resulting bounds predict risk in practice. Marginal observations alone can leave the joint frequencies unresolved. Applying the formulas to an instruction change would require evidence for the task mix, cost ranges and their dependence.

## Recommended Next Action

Work through one hypothetical rework threshold in the routing-line example in [On-balance judgments](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md), comparing the bounds for a shared unknown cost with those for a cost that can vary by task.
