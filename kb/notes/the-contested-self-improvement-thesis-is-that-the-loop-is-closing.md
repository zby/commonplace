---
description: "The cluster's real bet isn't that a closed reflective loop pays off — that's intuitive — but that the loop is closing at all; and autonomy gains spent as scope at fixed human time hide the trajectory"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# The contested self-improvement thesis is that the loop is closing, not that a closed loop pays off

The self-improving-systems cluster is organized around a payoff conjecture: that a reflective improvement loop, once it reuses addressable structure across a shift, needs fewer new target observations — [reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md). That conjecture is carefully falsifiable and worth stating, but its *direction* is comparatively intuitive. Conditional on the loop actually closing — on a system genuinely retaining structure and reusing it unattended — reduced target data is roughly what you would expect; the argument's care goes into the conditions and the cost ledger, not into overturning an expectation. The genuinely contestable claim sits one step earlier, in the antecedent that the payoff conjecture grants in passing: **that the loop is closing at all — that the human share of the improvement pathway is shrinking over time.**

That antecedent is asserted, not demonstrated. Autonomy is the fraction of the [improvement pathway](./definitions/self-improving-system.md) that runs without a person; "the loop is closing" is the claim that this fraction rises across a system's history. But every instance close enough to complete to check has an *open* loop: the Gödel machine is unimplemented, and Commonplace's pathways are still mostly human-inclusive. A system could just as well plateau at a fixed, human-heavy mix — automating the cheap functions early and stalling wherever [warrant runs out](./warranted-autonomy-is-bounded-by-oracle-domain.md). Whether real systems trend toward closure or toward a stable plateau is exactly the empirical question the payoff conjecture quietly presupposes, and it is the one worth contesting.

## The closing trajectory is spent as scope, not banked as free human time

Even granting that the loop is closing, the trajectory resists direct observation, because the gains are not returned as reduced human involvement — they are **spent as expanded scope at roughly fixed human time.** When a function moves from human to machine, the freed human capacity is characteristically reinvested rather than banked: more collections, more checks, a larger KB, a noticing channel that did not exist before. Human wall-clock stays about constant; what changes is the fraction of a now-larger pathway that runs unattended.

This confounds the obvious proxy. You cannot read closure off total human effort, because the denominator grew with the numerator — a Jevons-like dynamic in which the more-automated pathway is simply run over more ground, not run with fewer people. It compounds the problem that [measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) rather than escaping it: that note shows there is no commensurable decomposition to compare a profile against its own earlier self, because the function list itself grows; this note adds that even the crude "how much human time" proxy is confounded whenever scope is not held fixed — and a growing system never holds it fixed. To watch the loop close you would have to fix the scope and watch the human share of *that fixed scope* fall, which is precisely the observation no ambient look at a healthy, expanding system supplies.

## Scope

- The claim is about which thesis is contested, not that closure is false. Closure may well be happening; the point is that it is the load-bearing empirical bet and the hard-to-observe one, while the payoff it would enable is the comparatively safe part.
- "Autonomy gains spent as scope" is the design-time behavior of maintainers reinvesting freed capacity, not a statement that autonomy cannot in principle be banked. A system deliberately held at fixed scope would expose the trajectory; the point is that useful systems are not run that way.

## Open Questions

- Whether any system exhibits closing at fixed scope — the controlled observation the confound demands — or whether the trajectory is only ever inferred indirectly.
- Whether "fixed human time, expanding scope" is a contingent fact about how maintainers behave or a near-law of self-improving systems operated under a human-capacity constraint.

---

Relevant Notes:

- [Reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) — contrasts: the payoff conjecture this note names as the comparatively intuitive half, relocating the contest to its antecedent
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — grounds: the measurement problem this note adds the fixed-human-time scope confound to
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why a plateau is plausible — closure stalls wherever no oracle warrants handing the gate over
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: autonomy as the human share of the improvement pathway, the quantity the closing thesis claims moves
- [Where change candidates come from in Commonplace](../reference/where-change-candidates-come-from-in-commonplace.md) — evidence: freed capacity reinvested as a new noticing function (`commonplace-freshness-status`), scope expanding rather than human time falling
