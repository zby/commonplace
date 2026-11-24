---
description: "Two commutes differ in cost, travel time, and punctuality. A worked comparison distinguishes a veto on lost punctuality from a minimum service level."
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
---

# A veto can block outranking without deciding the reverse

Most criteria can favor a cheaper, faster commute while one unacceptable loss of punctuality blocks the claim that it is at least as good as the old trip. To prefer the old trip, the commuter must also test the reverse claim.

Figueira, Mousseau and Roy distinguish two conditions in [*ELECTRE Methods*](../sources/electre-methods.ingest.md): enough criteria must support the claim (**concordance**), and none may oppose it too strongly. To see how the conditions work together, consider a simple rule: add the weights of the criteria on which the new trip is no worse. It **outranks** the alternative if that sum reaches the agreed cutoff and no loss exceeds its veto threshold. Here a weight counts toward support; it does not say how many dollars an on-time arrival is worth.

## How often would the commuter be late?

Suppose a commuter considers parking at a different station. Over 100 comparable journeys, the new trip costs less in total and takes less time on average. The commuter has a fixed start time, so reaching work on time matters separately from average journey time. The old trip gets them there on time on 98 of the 100 days.

Give cost, average journey time, and punctuality one vote each. Require two votes and let a loss of **more than two on-time arrivals** veto the claim. Set no other veto. These numbers illustrate a preference; they are neither measured outcomes nor recommended thresholds.

| On-time arrivals with the new trip | Does the new trip outrank the old? | Does the old trip outrank the new? |
|---|---|---|
| 97 | Yes. Cost and travel time supply two votes; one more late arrival does not veto. | No. Only punctuality favors the old trip. |
| 95 | No. Cost and travel time still supply two votes, but three more late arrivals veto the claim. | No. The old trip still has only one vote. |

The second row is **incomparability**, not indifference: neither claim passes. Under the same rule, if the trips perform identically on all three criteria, both claims pass. The judge therefore needs to report both directions, not just announce that the new trip failed the test.

## Scope

A veto compares two options. A trip with 95 on-time arrivals faces a veto against 98, but not against 96. An absolute requirement of at least 97 on-time arrivals would reject it in either comparison. A [dominance cone that protects punctuality](./a-dominance-cone-can-allow-some-offsets-but-not-others.md) differs again: even the one additional late arrival in the first row would block dominance.

For an [on-balance judgment](./on-balance-judgment-with-an-llm.md), the useful question is whether the work justifies that distinction between a tolerable loss and a decisive objection. If the veto threshold cannot be defended, report which threshold changes the verdict. If instead the threshold is agreed but the loss is uncertain, compare arrival times on further comparable workdays. More observations can improve the estimate of the loss; they cannot decide how much loss to accept.
