---
description: "How to elicit and test an LLM’s judgment: trace rival remedies for misleading directions, then compare options when the obstacle is a genuine trade-off."
type: types/note.md
traits: [has-comparison]
---

# On-balance judgment with an LLM

Suppose a library moves its pickup desk upstairs, but visitors keep lining up at the old desk. Should the librarian add a sign at the entrance? An LLM comparing a new sign with no sign can give a sensible answer: the sign would help visitors find the new desk. Now walk the route. At the foot of the stairs, an arrow still points to the old desk and says “Pick up reserved books here.” Correcting that arrow addresses a problem the entrance sign leaves in place. If the arrow is already correct but visitors never see it from the entrance, the case for the entrance sign gets stronger.

A [recorded Commonplace decision](../reference/adr/076-source-claim-grounding-is-a-promoted-skill.md) has the same structure. An agent looking to save quotations followed the advertised procedure for ingesting a source. Adding a pointer to the right procedure would have left the competing invitation intact. Advertising quotation selection separately and removing it from the source-ingestion description left one advertised route instead of two.

## How to ask for the judgment

The [requirements for judging improvement](./defining-improvement-for-open-ended-work.md) start with consequences for the expected work. Give the LLM the problem, the alternatives it can inspect, and the commitments a remedy must preserve. Withhold the recorded decision if the point is to test the model. Ask: **What would you change, rather than what? Trace what happens under each option. Which difference matters enough to decide, and what would make that reason fail?**

In the library example, someone can check where each arrow points and whether either sign is visible from the entrance. Those are facts about the design. Whether more visitors will reach the right desk without asking for help is a forecast. Observing visitors unfamiliar with the building tests that forecast; agreeing with the librarian does not.

## Which comparison fits the case?

Sometimes the obstacle is a genuine trade-off rather than a missing alternative. Suppose a commuter could park at a different station. The new trip is quicker and cheaper overall, but the commuter gets to work late more often. This list of ways to compare the options is **preliminary**:

- [Necessary preference](./necessary-preference-can-guide-improvement-without-a-global-measure.md): How costly would an extra late arrival have to be to erase the savings? If every valuation the commuter can defend still favors switching, there is no need to pick an exact price for lateness. If the valuations disagree, say where the choice turns.
- [Dominance cones](./a-dominance-cone-can-allow-some-offsets-but-not-others.md): Which losses may offset which gains? A lower fare can cover higher parking fees dollar for dollar. If punctuality must not decline for one trip to dominate another, no dollar saving offsets more late arrivals.
- [Outranking with a veto](./a-veto-can-block-outranking-without-deciding-the-reverse.md): Are lower cost and shorter travel time enough to favor the new trip? A commuter might accept one extra late arrival in 100 journeys but refuse three, however cheap the trip. Refusing that loss does not by itself establish that the old trip is better.

None of these rules tells us why the commuter is late, just as none would discover the misleading arrow. Tracing what happens can reveal a third option that avoids the trade-off.

## Does using the model lead to better choices?

The claim worth testing is that **using the model’s judgments leads to better work than a specified alternative**, not that the model can explain past decisions. For example, compare signage changes selected with model assistance against changes selected by the usual maintenance process at comparable library branches. Fix what counts before seeing the results: did visitors find the desk, how often did staff have to redirect them, and how much staff time did selection and repair take? Count rejected and reversed changes too. Otherwise an expensive judgment that leaves no change behind disappears from the comparison.
