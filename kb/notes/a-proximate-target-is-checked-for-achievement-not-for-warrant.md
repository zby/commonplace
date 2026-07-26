---
description: "Between an improvement objective and its oracles sits a target level — a property pursued because it is held to serve the objective — whose linking claim no check in the loop evaluates"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, evaluation]
---

# A proximate target is checked for achievement, not for warrant

An improvement pathway rarely steers on the thing it is for. Between what ultimately counts as better and the machinery that fires, four things get called the objective, and only two of them are ever the same:

- **The improvement objective** — what counts as better, [declared as a parameter of the analysis](./self-improvement-is-relative-to-a-declared-objective.md).
- **The proximate target** — a property pursued because it is *held to serve* that objective. Retain commitments addressably. Keep coupling low. Widen reflective coverage.
- **The operational criterion** — what the pathway can actually score. Notes carry rationale, scope, and review evidence.
- **The oracle** — the mechanism and evidence that applies the criterion.

Two of these levels are proxies, and the theory covers only one of them. The criterion-to-objective relation is the well-worked case: an oracle is [already a stand-in graded by how reliably it discriminates](./oracle-strength-spectrum.md), and the consequences of getting it wrong are understood down to the selection pressure it exerts. The target-to-objective relation carries a claim of the same shape — *this property produces that outcome* — and nothing in the ordinary machinery is arranged to evaluate it.

## The daylight between a target and an oracle

Both stand in for something they are not, which is why the two levels collapse so easily. What separates them is position.

An oracle is a proxy in the **verdict position**. Candidates arrive; it emits accept or reject. Being a bad proxy therefore means mis-ranking, and mis-ranking leaves a trace: accepted candidates that later disappoint. That trace is what makes the check improvable — a composite oracle [is calibrated by asking whether the code became easier to change or the note supported a better decision](./weakly-discriminated-qualities-tend-to-be-underselected.md), which is only possible because there is a verdict stream to compare against outcomes.

A proximate target is a proxy in the **goal position**. Nothing is submitted to it. It acts earlier, by shaping which candidates get generated and which designs get built at all, and it is wrong in a different way: not by ranking two things incorrectly, but by the linking claim being false — the property is achieved and the objective does not move.

This is not the bottom of the oracle spectrum. A no-oracle quality is one where verdicts are wanted and unavailable; a proximate target is not in the verdict position to begin with.

## Achievement checks make targets look verified

The trap is that a target usually *does* admit a check — of the wrong proposition. Whether artifacts carry rationale is mechanically decidable. Whether carrying rationale makes later reasoning better is the claim that licensed the target, and it is not what the validator ran.

So a strengthened achievement check delivers exactly the signature of a verified property: a green gate, a rising number, a policy the system enforces. It supplies no evidence for the linking claim, and by supplying that signature it removes the pressure to look for any. The pathway's own selection dynamics then finish the job — a target with a strong achievement check outcompetes the delayed objective it was adopted to serve, for the same reason any strongly discriminated quality outcompetes a weakly discriminated one. The mechanism is not new; the level it operates on is. Underselection was stated over qualities of candidates, and it applies one level up, over what the loop is aiming at.

## How a mistaken target is found

The tell is composition failure, transposed. For an artifact it is components that are individually sound and do not add up to the capability, [which is what marks a spec as a proxy theory rather than a definition](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md). For a target it is the property achieved, its check passing, and the objective sitting where it was.

Reading that signal requires two things the pathway does not supply by default.

**The linking claim has to be stated.** An unrecorded justification cannot be found false; the target simply persists as a settled commitment whose reason nobody holds. This is a design-rationale problem before it is an evaluation problem, and the rationale surfaces where the reason would live [do not enforce continuity from a shipped commitment back to what justified it](../reference/design-rationale-management.md).

**The objective needs a reading independent of the target.** Where the only available measure of artifact quality is that artifacts carry rationale, the linking claim is unfalsifiable by construction — the proxy has been substituted for the thing, and the substitution is invisible because both are called the objective.

## Why the levels collapse

A proximate target is a design choice justified by a claim, not [a constraint inherited from a consumer or a substrate](./first-principles-are-inherited-constraints-not-design-choices.md) — but it presents like one. Structural properties are stable, statable, and cheap to check for achievement, and those are the same properties that make something look like a settled goal rather than a contestable bet.

The consequence runs back into how architectures get compared. A profile of structural properties selects no ordering by itself; that much is a claim about the descriptive space. But a declared objective does not repair this on its own either, because an objective stated over outcomes cannot rank architectures without some claim connecting structure to outcome. The linking claim is doing that work wherever architectures are being ranked, whether or not anyone has written it down.

## Scope

- The claim needs the objective and the target to be different things. Where the property *is* what is wanted — a compliance requirement that artifacts carry provenance, full stop — it is terminal rather than proximate, and there is no linking claim available to be wrong.
- Nothing here says proximate targets are a mistake. When the objective is delayed, contested, or unmeasurable at the moment of decision, a structural property may be the only thing there is to steer on. The claim is about what the resulting green gate does and does not establish.
- The four levels are a reading, not a fixed depth. A target can stand in for another target, and the chain terminates wherever the analysis declares its objective.

## Open Questions

- What makes a structural property a good proximate target *before* the outcome evidence arrives. Linking claims with [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — ones that say why the property produces the outcome, and so predict where it would stop — are the obvious candidate, and that is a conjecture rather than a result.
- Whether calibration against delayed outcomes can reach the linking claim, or only ever reaches the criterion. Asking whether notes carrying rationale were the ones that supported better decisions is an ordinary empirical question; whether any pathway can afford to run it is a different one.
- Whether a reflective pathway can hold its own linking claims addressably, which would make them revisable like any other retained theory rather than settled by the absence of a check.

---

Relevant Notes:

- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: the declared objective the target level stands in for, and the indexing this note adds a level below
- [Fixed artifacts split into exact specs and proxy theories](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — grounds: the proxy-theory relation and composition failure as its tell, stated for artifacts and transposed here to targets
- [Weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — mechanism: the selection pressure that makes a strongly checked target outcompete the objective it serves
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — contrasts: the graded proxy relation for checks, which a target sits outside rather than at the bottom of
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: warrant as what a check establishes, the property an achievement check does not supply for its target
- [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — contrasts: the inherited constraint a proximate target is mistaken for
- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: the worked instance — addressability is pursued for expected advantages, which is a linking claim of exactly this shape
- [Design rationale management in Commonplace](../reference/design-rationale-management.md) — evidence: distributed rationale surfaces that retain justifications without enforcing continuity from a commitment back to them
