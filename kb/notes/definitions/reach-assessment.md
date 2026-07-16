---
description: "Definition — the capability to judge a candidate commitment's claimed reach as genuine, not adaptive fit; reflectivity does not supply it, and no theory explains why LLM evaluators have it"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Reach assessment

**Reach assessment** is the capability of a system's evaluation process to judge whether a candidate commitment's claimed [reach](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — that the pattern it names holds beyond the evidence that produced it — is genuine, rather than adaptive fit dressed up as an explanation. This is a judgment about the *content* of a claim, not a check on its *form*.

[Reflectivity](./reflective-system.md) does not supply this for free. A reflective system can represent a commitment's stated applicability condition, read it, and rewrite it — [rejecting or rescoping a prior commitment](../reflection-makes-retained-lessons-second-order.md) is a structural operation reflection makes available. None of that requires judging whether the commitment's stated boundary is honest: a process can mechanically compare a new case against a stated condition and act on the match without ever assessing whether the underlying explanation actually captures an invariant, or is dressed-up curve-fitting that happened to generalize once.

## Scope

- Reach assessment operates on the *content* of a candidate commitment — its causal or explanatory structure — not on metadata about it. Checking that a new case satisfies a stated condition clause is boundary-matching, [the discriminator memory formation already uses](../abstract-an-experience-only-when-you-can-state-the-boundary.md); reach assessment is what would be needed to judge whether that stated condition is itself trustworthy.
- What it would need to do is apply something like [the four-part negative test](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — can a load-bearing premise be varied and the conclusion predictably change; does the claim reach into an untested domain; can it be criticized in a specific way; does it survive contact with observed fit — to a system's own candidate commitments, inside its own improvement loop, not to a human author's KB note.
- In current practice this capability is observed in LLM-mediated evaluation: an agent asked to judge whether a proposed lesson generalizes correctly appears able to do so with some reliability. Commonplace has no theory for why; see [Provenance and departures](#provenance-and-departures).

## Exclusions

- **Reach assessment is not reflectivity.** [Reflective system](./reflective-system.md)'s five requirements — boundary, represented aspects, self-representation, processes, causal connection — are purely structural. A reflective system built entirely on exact- or fuzzy-string matching against a stated condition clause has every one of those five properties and no reach assessment at all.
- **Reach assessment is not oracle strength in general.** An oracle can verify a candidate against a fixed spec without ever judging whether the reasoning behind a retained commitment generalizes. Reach assessment is one specific, narrower judgment a strong oracle might supply, not a restatement of oracle strength.
- **Reach assessment is not confidence.** A system reporting high confidence in a rescoped commitment is not evidence the rescoping was reach-assessed; confidence and correctness come apart exactly where reach assessment would matter most — a fluent, wrong generalization is the failure mode this capability exists to catch.

## Misuse Cases

- Assuming any reflective pathway automatically has reach assessment because it can represent and rewrite a commitment's scope — the operation being available says nothing about whether it is exercised well.
- Treating a match between a stated condition clause and a new case as evidence that the underlying commitment has genuine reach — that is boundary-matching, which presupposes the stated boundary is honest rather than testing it.
- Citing this note to claim reach assessment is unique to LLMs by necessity. The claim is narrower: it is observed in LLM-mediated evaluation and unexplained, not derived from anything specific to that architecture.

## Provenance and departures

This is Commonplace's own concept, without an inherited definition to depart from. The four-part negative test it builds on is adapted from Deutsch by [first-principles-reasoning-selects-for-explanatory-reach-over.md](../first-principles-reasoning-selects-for-explanatory-reach-over.md), and the observation that stating a boundary is itself a judgment — not a mechanical derivation — is already made by [abstract-an-experience-only-when-you-can-state-the-boundary.md](../abstract-an-experience-only-when-you-can-state-the-boundary.md), which leaves who or what can reliably make that judgment as an open problem. This note names the missing capability; it does not close the open problem. Why LLM-mediated evaluators appear capable of it is not theorized here.

---

Relevant Notes:

- [Reflective system](./reflective-system.md) — contrasts: supplies the structural capacity to represent and rewrite scope; this note is the semantic judgment reflectivity does not supply
- [First-principles reasoning selects for explanatory reach over adaptive fit](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the four-part negative test this note asks a system's own evaluator to apply, not only a human author
- [Abstract an experience into a lesson only when you can state where the lesson stops](../abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: names stating a boundary as itself a judgment and leaves who can make it open; this note names the missing capability
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../reflection-makes-retained-lessons-second-order.md) — extends: rejection and rescoping are structural operations reflection enables; reach assessment is what would make exercising them reliable
- [Reflection may improve sample efficiency under structured shifts](../reflection-may-improve-sample-efficiency-under-structured-shifts.md) — evidence: the conjecture's payoff additionally depends on this capability, which reflectivity alone does not supply
