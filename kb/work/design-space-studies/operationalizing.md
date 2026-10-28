# Operationalizing design-space studies: initial thoughts

Agent proposal, 2026-10-28. It awaits the operator's direction; nothing here is
adopted.

## The gap is a composing procedure, not theory

Most of what the exploration proposes already exists in the library as
separate pieces:

- The map, its falsifiability and rival maps are in [first-principles analysis](../../theory/first-principles-analysis-maps-design-space-before-selection.md).
- Demoting a supposed constraint is in [boundary-preserving rival](../../theory/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md).
- Deferral postures are in [productive deferral](../../theory/productive-deferral-requires-option-evidence-and-convergence.md).
- Framing a request is in [invert solution-shaped requests](../../instructions/invert-solution-shaped-requests.md).
- The belief/selection boundary is in [ADR 070](../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md).

What is missing is one procedure that runs these in order on a real decision.
What is also missing is any evidence that doing so changes the decision. The
first job is therefore to produce that evidence cheaply, not to build a type,
validator or role pipeline.

This reverses the exploration's first increment, which was a type plus a
validator before any study had been run. Following [progressive
constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md),
the schema should be read off the fields that pilots actually used.

## What the ingested sources change

- **Compatibility rules need a typed warrant.** A pruned cell is only as good
  as the reason it was pruned. Ritchey types exclusions as logical, empirical
  or normative. Build Systems à la Carte prunes by execution. ATAM records an
  expert judgment together with the assumptions that would reopen it. A study
  should record which kind each rule is, because each kind reopens under a
  different condition.
- **Settle what is possible before what is desirable.** Ritchey holds
  normative exclusions back until the possible space is mapped. This cleanly
  separates the map (feasibility) from selection (preference). It also
  suggests that preference-based pruning belongs at the commitment gate, not
  in the map.
- **Hard exclusion versus weighted preference is unresolved.** Ritchey's
  rules are mostly binary. Lane found hard rules rare and weighted preferences
  dominant. A pilot should record which kind it actually needed.
- **Pairwise, not a full cross-product.** Pairwise consistency checks grow
  quadratically while configurations grow exponentially. Start from pairwise
  rules and enumerate only the surviving regions that a decision touches.
- **Test a map against decisions it was not built from.** Lane checked his
  rules against designers outside his sample. The analogue here is checking a
  map against past ADRs: does it place the choice that was made, and does it
  name the alternatives that were rejected? This is the clearest available
  test of map adequacy, and it is cheap.
- **Scenarios are the unit of consequence.** ATAM turns quality goals into
  scenarios before judging anything. An axis earns its place when changing its
  value changes the outcome of a named scenario. This makes the exploration's
  "predicts a distinct consequence" test checkable.

## Where I would push back on the exploration

- **Its status table mixes two properties.** `witnessed-feasible`,
  `impossible`, `dominated` and `unresolved` describe a region's feasibility.
  `selected`, `deferred` and `superseded` describe Commonplace's commitment to
  it. That is the ADR 070 distinction between belief and selection. They
  should be two fields; otherwise a selected region seems to stop needing a
  feasibility warrant.
- **The priority formula is false precision.** Multiplying five ordinal
  ratings invites arithmetic on labels. The NASA rule it cites is enough on
  its own: an unknown is decision-critical only if some possible answer would
  change the ranking, the timing or the migration plan. That is already the
  "discriminating evidence" condition of productive deferral.
- **Seven LLM roles is premature.** The one role whose value is argued is the
  rival mapper. It has to be independent of the first mapper: a fresh
  context, given the frame but not the first map. Start with mapper, rival
  mapper and operator. Add roles only when a pilot shows a gap that a role
  would fill.
- **Maps that survive commitment clash with the workshop lifecycle.** The
  exploration wants maps kept and revised after the ADR. Workshops are
  consumed and deleted. Where a map lives after commitment is exactly the
  question [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md)
  owns, so this workshop should not answer it.
- **The "distinctive Commonplace contribution" claim is untested.** Whether
  combining these methods beats using any one of them is what the pilots
  should find out, not something to assert up front.

## A first sequence

1. **Draft a study template as a plain workshop file.** Sections: frame;
   constraint ledger, with each entry's provenance (boundary commitment,
   selected convention, requirement, earlier choice) and a boundary-preserving
   rival where one exists; axes, each with the scenario outcome it changes;
   pairwise compatibility rules with their warrant kind; surviving regions;
   unknowns, each with the action a possible answer would change; and the
   posture of each open choice. No type and no validator.
2. **Retrospective pilot: Windows command delivery.** The outcome is known.
   The signed-Python prerequisite was adopted on 2026-10-28 after field
   failures, as recorded in [windows-install](../windows-install/README.md)
   and the ADR 064 Windows amendment. Give the mapper only artifacts from
   before the first Smart App Control failure (cut off by commit date). Then
   check whether the map, its rival map or its unknowns ledger would have
   surfaced the interpreter-signing axis before the field did.
   - If no route could have, that is a finding too: environment axes may only
     be discoverable by probes, and the procedure should then prioritize cheap
     environment probes over analysis.
   - Hindsight bias is the main risk. The rival mapper must not see the
     outcome.
3. **Prospective pilot: one live decision.** Pick a consequential choice that
   is still open. One candidate is a choice left open in
   [review-on-workjig](../review-on-workjig/README.md) after its storage
   direction was set; the operator picks.
   Run the study before the decision and record what it changed.
4. **Held-out check.** Take two or three past ADRs that list alternatives.
   Test whether a map built from their pre-decision state places the chosen
   option and names the rejected ones.
5. **Decide what to promote.** Record which template fields the pilots used,
   which they left empty and what they lacked. Only then draft an instruction,
   and a type if the instruction's consumers need one.

## What the pilots should measure

For each pilot, record what it found, what it cost and whether anything
changed:

- **Findings:** constraints demoted, alternatives or axes exposed, and unknowns
  whose answer changed the next action.
- **Cost:** operator time, and template fields filled but never consulted.
- **Effect:** whether the decision differed from what the existing route
  (inverting the request, then a proposal, then an ADR) produced or would have
  produced.

A larger map is not a better one. Content that no decision consumed counts
against the method.

## Open questions

- Can a rival map be made independent enough to expose a shared hidden
  premise, or do two LLM mappers given the same frame converge on the same
  decomposition?
- Which decisions are worth a study? A threshold based on irreversibility or
  coupling needs examples before it can be stated.
- Does the study replace inverting the request for architectural decisions,
  or follow it?
