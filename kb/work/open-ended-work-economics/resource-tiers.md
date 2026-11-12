# Three resource tiers and two feasibility frontiers

Operator's framing, 2026-11-05, recorded as workshop analysis. The current [workshop framing](./README.md) places it under the question of
what should guide automatic search. This file retains the earlier candidate
model for criticism; its proposed maximand and refuters are not adopted.
Moving work between tiers is one possible return on search, not the assumed
objective. Nothing here is adopted vocabulary; "tier" and "frontier" are
workshop-local words.

## The tiers

Commonplace spends three kinds of resource, and they differ in kind, not
only in price:

| Tier | Resource | Can it be bought? | Reliability |
|---|---|---|---|
| 1 | Operator attention: judgment, authority, objective choice | No | High, scarce, slow |
| 2 | LLM work: interpretation, judgment without authority, generation | Yes | Fallible; needs verification |
| 3 | Classical compute: enforcement of defined transitions, checks, bookkeeping | Yes, cheaply | High within what it can express |

Tier 1 is the binding constraint. The library already measures improvement
in its units: [improvements are measured per human judgment, not human
time](../../theory/increasing-computational-autonomy-relocates-human-effort.md),
and progress in a self-improving system is [which decision-bearing
functions humans still supply](../../theory/computationally-directed-self-improvement-is-a-reallocation.md).

## The two boundaries are feasibility lines first

Economic thinking treats a boundary as a price comparison. The two tier
boundaries are not. Each is a condition that must hold before any price
applies.

**LLM to compute.** Code can take a transition only when the rule is
defined and a reference settles what it permits: the symbolic criterion in
[representational form](../../theory/definitions/representational-form.md)
as revised by [ADR 124](../../reference/adr/124-retire-unique-operational-semantics-as-the-form-criterion.md).
Below that line the [error-correction asymmetry](../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
prices the move: avoided model checking and repair against implementation
and maintenance, compared at a required end-to-end reliability. Above the
line no price makes code feasible. The asymmetry note's own scope says so:
the argument applies to explicit state and sufficiently specified
transitions. The [codify-versus-LLM heuristics](../../theory/codify-versus-llm-decision-heuristics.md)
hold the economic part, including this workshop's stake-and-odds section.

**Operator to LLM.** A model can take a judgment only when the result can
be verified at the required level by something other than the operator:
[the boundary of automation is the boundary of verification](../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md),
and [error correction works only with above-chance oracles and
decorrelated checks](../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md).
Objective choice stays on the operator side by construction:
[objective revision is licensed from outside the objective](../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md),
which is the epistemic-layer note's stated weak point for role 1.

Epistemic work is what moves both lines. Finding that a choice is stable
enough to commit makes a transition codifiable
([progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md)).
Finding that a judgment is checkable makes it delegable. This is the
README's "convert into routine" reading stated per tier: conversion is the
movement of work downward across a frontier.

## Where economics operates

Only inside a tier, and in choosing which frontier move to invest in:

1. **Within tier 2.** Which investigations to run, how much self-checking
   to buy, when to stop. The library grounds this structurally
   ([search allocated before evaluation](../../theory/open-ended-improvement-allocates-search-before-evaluation.md);
   [a controller is tested by what it brings to stronger evaluation](../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md)).
   The context bound gives tier 2 its own internal cost structure
   ([two context boundaries, three regimes](../../theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md)),
   which is the step-shaped cost measure the reconciliation adopted.
2. **Between frontier moves.** Which bookkeeping to codify first; which
   operator judgment to delegate first. Priced by stake, odds and exposure,
   and by how much of the scarcer tier the move frees.
3. **Verification purchase.** Whether a check runs in code, in a second
   model call, or in front of the operator. The asymmetry note's test form
   is the comparison: total cost at a required end-to-end reliability.

The exchange rate between tiers is asymmetric because tier 1 cannot be
bought. A move that frees one operator judgment is worth much tier-2 work.
A move that saves compute is worth little unless it also moves a frontier.

## The maximand, stated per tier

Candidate, not adopted: Commonplace allocates to maximize work moved
downward across the two frontiers at the required reliability, measured
per operator judgment. The README's weak points become the objections:
the frontier does not shrink by itself, since
[each conversion leaves the remaining work harder](../../theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md);
"solved" is graded; goals are not beliefs. Rival maximands to keep beside
it: explanatory reach, defeated claims repaired, user value delivered.

## Consequences for an agent choosing what to do next

An agent sits in tier 2. Under this maximand its highest-value choices
touch a frontier:

- Produce a decision in a form the operator can accept with one judgment
  rather than a reading.
- Prefer work that leaves a settled transition behind, as a candidate for
  the compute frontier.
- Do not spend tier-2 work re-interpreting what code could enforce.

Everything else is ordinary search allocation under the existing structural
rules. Whether the agent's individual return guesses must be recorded to
make this allocation criticizable, or testing the controller is enough,
remains the open question from direction 1.

## What would refute the framing

- A frontier move that is feasible but never pays: feasibility would then
  be insufficient as the first gate, and the price comparison would govern
  earlier than claimed.
- A case where buying more tier-2 work substitutes for an operator
  judgment without a verifier: the operator-to-LLM line would be a price,
  not a feasibility condition.
- Conversions that move work downward and still raise operator judgments
  per unit of work over time: the maximand would be measuring the wrong
  thing, and the "frontier does not shrink" objection would be decisive.
