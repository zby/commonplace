---
description: "How to elicit and test an LLM’s judgment of a proposed change: compare remedies for a misrouted request, identify what turns the choice, and test the forecast on later work."
type: types/note.md
traits: [has-comparison]
---

# On-balance judgment with an LLM

An agent asked to save quotations supporting a claim went to the skill for ingesting a source. Should we add a pointer to the right procedure in `AGENTS.md`? An LLM comparing the pointer with silence can give a sensible answer: the pointer would make the procedure easier to find. Yet that comparison misses a fact that changes the remedy. The ingest skill itself advertised quote retention. A reader could follow that invitation even with the pointer in place.

[Commonplace’s decision record](../reference/adr/076-source-claim-grounding-is-a-promoted-skill.md) gives the alternative: advertise the procedure for choosing supporting quotations as a skill in its own right, and stop advertising that operation under ingest. If the aim is one advertised route to the procedure that owns the decision, prefer that change to the pointer. The difference is not that one remedy has more benefits on a list. Only one removes the competing invitation while giving the request somewhere to go. If there were already a single entry and agents simply couldn't find it, that reason would disappear; a pointer would address the remaining difficulty.

## How to ask for the judgment

The [requirements for judging improvement](./defining-improvement-for-open-ended-work.md) start with consequences for the expected work. To elicit an on-balance judgment, give the LLM the request, the relevant descriptions as they stood at the time, and the commitments the remedy must preserve. Withhold the recorded decision if the point is to test the model. Ask: **What would you change, rather than what? Trace what would happen to the next such request under each option. Which difference matters enough to decide, and what would make that reason fail?**

The trace lets someone check the recommendation. In this case one can inspect whether both descriptions invite the request and whether the proposed edit leaves a route for ordinary source ingestion. Those are checks on the design. Whether agents will actually choose the right skill more often is a forecast. Test it with fresh requests under the old and new descriptions, including requests to ingest a new source as well as requests to support an existing claim. Matching the recorded choice does not establish either routing outcome.

Sometimes the obstacle is not a missing alternative but a genuine cost. Suppose a revised instruction saves a manual check on many tasks but causes rework on a few. Ask the model how bad the rework would have to be to erase the saving, and whether the work gives grounds for ruling that out. [Necessary preference across compatible measures](./necessary-preference-can-guide-improvement-without-a-global-measure.md) develops this approach: a choice can survive disagreement about the exact value of the saving. It does not follow that an LLM has checked every relevant loss merely because it can calculate a break-even point. If it cannot bound the rework, its useful answer may be the particular failure to investigate, not a winner.

## Testing the selector

The claim worth testing is that **using the model’s judgments leads to better work than a specified alternative**, not that the model can explain past decisions. For a routing trial, compare the changes selected with model assistance against those selected by the existing maintenance process on comparable requests. Fix what counts before seeing the results: did requests reach the procedure that could complete them, what errors required repair, and how much maintainer time did selection and repair take? Count rejected and reversed changes too. Otherwise an expensive judgment that leaves no change behind disappears from the comparison.

## Open research question

Which other comparison methods give an LLM useful questions to ask of a case? Leads for a literature search, not established sources for this note, are Pareto dominance, majorization, stochastic dominance, utility theory without complete preferences, supervaluation, Sen’s intersection orderings, dominance with partially known weights, and imprecise probability. For each, identify what alternatives or evaluations the rule ranges over, what justifies including them, and which comparisons remain unordered. Its value here would be a worked case showing what the model could distinguish or check by using it.
