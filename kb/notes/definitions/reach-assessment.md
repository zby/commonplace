---
description: "Definition — the capability to judge a candidate commitment's claimed reach as genuine; formal apparatus supplies it for symbolic claims, but only LLM evaluation is observed to for prose ones"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Reach assessment

**Reach assessment** is the capability of a system's evaluation process to judge whether a candidate commitment's claimed [reach](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — that the pattern it names holds beyond the evidence that produced it — is genuine, rather than adaptive fit dressed up as an explanation. This is a judgment about the *content* of a claim, not a check on its *form*.

[Reflectivity](./reflective-system.md) does not supply this for free. A reflective system can represent a commitment's stated applicability condition, read it, and rewrite it — [rejecting or rescoping a prior commitment](../reflection-makes-retained-lessons-second-order.md) is a structural operation reflection makes available. None of that requires judging whether the commitment's stated boundary is honest: a process can mechanically compare a new case against a stated condition and act on the match without ever assessing whether the underlying explanation actually captures an invariant, or is dressed-up curve-fitting that happened to generalize once.

## Scope

- Reach assessment operates on the *content* of a candidate commitment — its causal or explanatory structure — not on metadata about it. Checking that a new case satisfies a stated condition clause is boundary-matching, [the discriminator memory formation already uses](../abstract-an-experience-only-when-you-can-state-the-boundary.md); reach assessment is what would be needed to judge whether that stated condition is itself trustworthy.
- What it would need to do is apply something like [the four-part negative test](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — can a load-bearing premise be varied and the conclusion predictably change; does the claim reach into an untested domain; can it be criticized in a specific way; does it survive contact with observed fit — to a system's own candidate commitments, inside its own improvement loop, not to a human author's KB note.
- Which route is available depends on the candidate commitment's [representational form](./representational-form.md). Where a commitment is or can be expressed symbolically — a structural causal model, a typed claim, a formally specified invariant — traditional, non-LLM apparatus can assess reach rigorously: causal discovery and do-calculus test whether a claimed mechanism is causal rather than merely correlational, and proof search can establish that a claimed property holds across its stated domain. The [Gödel machine](../goedel-machines-are-a-proof-governed-case-of-self-modification.md)'s proof-gated acceptance is exactly this route: it accepts a rewrite only when it can prove, within its axiomatized model, that switching helps.
- Where a commitment is still in prose — a natural-language explanation not yet reduced to a checkable formal claim — no comparable formal apparatus exists yet. There, reach assessment is observed only in LLM-mediated evaluation: an agent asked to judge whether a proposed lesson generalizes correctly appears able to do so with some reliability, and Commonplace has no theory for why. See [Provenance and departures](#provenance-and-departures).

## Exclusions

- **Reach assessment is not reflectivity.** [Reflective system](./reflective-system.md)'s five requirements — boundary, represented aspects, self-representation, processes, causal connection — are purely structural. A reflective system built entirely on exact- or fuzzy-string matching against a stated condition clause has every one of those five properties and no reach assessment at all.
- **Reach assessment is not empirical testing alone.** A test suite that passes on every case it checks establishes that a candidate holds on those cases, not that it holds beyond them — the reach question stays unanswered by passing tests. A proof oracle is a different matter: proving a claim within an axiomatized model does establish that it holds across the model's stated domain, a genuine, non-semantic route to reach assessment (see Scope) — but only as far as the axiomatization reaches, [which is what warranted autonomy is bounded by](../warranted-autonomy-is-bounded-by-oracle-reach.md).
- **Reach assessment is not confidence.** A system reporting high confidence in a rescoped commitment is not evidence the rescoping was reach-assessed; confidence and correctness come apart exactly where reach assessment would matter most — a fluent, wrong generalization is the failure mode this capability exists to catch.

## Misuse Cases

- Assuming any reflective pathway automatically has reach assessment because it can represent and rewrite a commitment's scope — the operation being available says nothing about whether it is exercised well.
- Treating a match between a stated condition clause and a new case as evidence that the underlying commitment has genuine reach — that is boundary-matching, which presupposes the stated boundary is honest rather than testing it.
- Citing this note to claim reach assessment is unique to LLMs. It is not: causal inference, do-calculus, and proof search are traditional, formal routes to reach assessment for symbolic claims, and predate LLMs by decades. What is genuinely unexplained is narrower — semantic judgment of a claim still in prose, where LLM-mediated evaluation is the only route currently observed.

## Provenance and departures

This is Commonplace's own concept, without a single inherited definition to depart from, but its two routes have different provenance. The formal route — causal inference, do-calculus, and proof search assessing reach for symbolic claims — is established science, not Commonplace's own; the [Gödel machine](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) is the worked case already in this cluster. Commonplace's own gap is the prose route: the four-part negative test it builds on is adapted from Deutsch by [first-principles-reasoning-selects-for-explanatory-reach-over.md](../first-principles-reasoning-selects-for-explanatory-reach-over.md), and the observation that stating a boundary is itself a judgment — not a mechanical derivation — is already made by [abstract-an-experience-only-when-you-can-state-the-boundary.md](../abstract-an-experience-only-when-you-can-state-the-boundary.md), which leaves who or what can reliably make that judgment, for a claim still in prose, as an open problem. This note names the missing capability for that case; it does not close the open problem. Why LLM-mediated evaluators appear capable of it is not theorized here.

---

Relevant Notes:

- [Reflective system](./reflective-system.md) — contrasts: supplies the structural capacity to represent and rewrite scope; this note is the judgment reflectivity does not supply
- [Representational form](./representational-form.md) — grounds: the prose/symbolic axis that decides which reach-assessment route is available
- [Gödel machines are a proof-governed case of reflective self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) — evidence: the worked case of the formal route, proof search assessing reach for a symbolic claim
- [First-principles reasoning selects for explanatory reach over adaptive fit](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the four-part negative test this note asks a system's own evaluator to apply, not only a human author
- [Abstract an experience into a lesson only when you can state where the lesson stops](../abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: names stating a boundary as itself a judgment and leaves who can make it open; this note names the missing capability
- [Reflection buys addressability](../reflection-buys-addressability.md) — extends: addressability makes a bad change findable; reach assessment is what would make finding it as bad reliable
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../reflection-makes-retained-lessons-second-order.md) — extends: rejection and rescoping are structural operations reflection enables; reach assessment is what would make exercising them reliable
- [Reflection may improve sample efficiency under structured shifts](../reflection-may-improve-sample-efficiency-under-structured-shifts.md) — evidence: the conjecture's payoff additionally depends on this capability, which reflectivity alone does not supply
