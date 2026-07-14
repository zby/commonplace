---
description: "Definition — self-improving to the degree a governed adaptation loop runs through the system's own self-representation without a human; reflection and intercession are machinery, not the property"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Self-improving system

A **self-improving system** runs a [governed adaptation loop](../governed-adaptation-requires-search-evaluation-and-retention.md) — search, evaluation, operative retention — whose changes are made through its own causally connected self-representation. It is self-improving **to the degree that** those functions run without human mediation.

The gradient is not decoration. It is what the word *self* is doing.

## What has to hold

- **Reflection.** A [causally connected self-representation](./reflective-system.md): a map of the system that is kept true and that steers.
- **Intercession.** Processes inside the boundary can *write* that representation, not only read it.
- **Search.** Something brings a candidate change into consideration — notices the problem, picks the target, generates the candidate.
- **Evaluation.** Something can *reject* it. An unconditional trigger is not an evaluator.
- **Operative retention.** The accepted change acquires a consumer, a channel, and a force, in [behavioral authority](./behavioral-authority.md) terms.
- **Autonomy**, which grades the whole thing: of search, evaluation, and retention, how much runs without a person? Assessed function by function against the declared boundary.

The first two are the machinery. The next three are the loop. The last is what earns the name.

## Why the first two are not the property

This is the standing confusion the term needs sharpening against. Reflection and intercession are nearly free, and they deliver nothing on their own.

A Smalltalk image has both maximally — the compiler can be edited with the compiler — and left alone it improves nothing for a decade, because [nothing in it performs search or evaluation](./reflective-system.md). Remove the programmer and the loop is not weakened; it is absent.

The same trap opens from the other side. Declare a maintainer inside the boundary and essentially every maintained codebase satisfies all five conditions — developers notice what to change, review and tests reject candidates, merge retains them, and the source is a causally connected self-representation they can write. All five hold, and nobody calls it a self-improving system. They are right not to: the improving is done by people. Only the autonomy gradient separates that case from the one the term is reaching for, [since human-inclusive boundaries make reflection cheap](../human-inclusive-boundaries-make-reflection-cheap.md).

## Why the loop must run *through* the self-representation

Governed adaptation alone is not enough either, and the negative case is real rather than constructed: [Ashby's Homeostat runs a complete loop — search, evaluation, retention — with no self-representation anywhere in the mechanism](../governed-adaptation-requires-search-evaluation-and-retention.md). It adapts, and nothing accumulates. Its improvements are opaque parameter settings that no process can read, criticize, or reuse.

Route the same loop through a self-representation and the accepted change lands in an artifact the system also *reads*. Improvement becomes legible, criticizable, and compounding: each retained change is available to the next round of search and evaluation, as knowledge rather than as a setting. That is what the intersection buys, and it is why neither component alone is the object of interest.

## Autonomy is bought with an oracle

Autonomy is the goal, and there is no reason to want less of it. It simply cannot be turned up at will. Automating an evaluation for which no adequate oracle exists does not produce a *more* self-improving system — it produces a *less governed* one, retaining changes nothing checked. That is self-modification, which governed adaptation is narrower than: the system drops out of the category rather than advancing within it.

So autonomy in evaluation extends only as far as an oracle reaches, and taking it costs something: [a stronger oracle buys autonomy and pays in reach](../a-stronger-oracle-buys-autonomy-and-pays-in-reach.md). A system's place on this gradient is therefore downstream of where it settled that trade, which is why the useful question is never *how autonomous is it* but *what does its oracle reach, and what does that cost*.

## Exclusions

**Self-improving is not self-modifying.** A blind, accidental, or unconditional rewrite changes later behavior without applying any criterion. It is self-modification, and it completes no loop.

**Self-improving is not a binary.** There is no threshold at which a system becomes one. The conditions are met or not; the *degree* is the autonomy profile, and it is read per function against a declared boundary. Moving the boundary moves the reading.

## Misuse Cases

- Calling a system self-improving because it can modify itself, without identifying what performs search and what could reject a candidate.
- Calling a system self-improving because an agent edits its own instruction files, when a human decides every edit and approves every one — that is a maintained codebase with a faster editor.
- Presenting an autonomy gain as an improvement when the evaluation it automated has no oracle behind it.
- Treating reflection or intercession as the property, rather than as the machinery the property runs on.

---

Relevant Notes:

- [Reflective system](./reflective-system.md) — grounds: the causally connected self-representation, and the intercession capability, that supply the machinery
- [Governed adaptation requires search, evaluation, and operative retention](../governed-adaptation-requires-search-evaluation-and-retention.md) — grounds: the loop, and the Homeostat case establishing it does not require reflection
- [Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient](../human-inclusive-boundaries-make-reflection-cheap.md) — grounds: why the machinery is nearly free, and why autonomy is the gradient that discriminates
- [Search errors are filtered; evaluation errors are retained](../search-errors-are-filtered-evaluation-errors-are-retained.md) — extends: which function to make autonomous first, and why evaluation is the one that must be bought
- [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: the ceiling on autonomous evaluation
- [A stronger oracle buys autonomy and pays in reach](../a-stronger-oracle-buys-autonomy-and-pays-in-reach.md) — mechanism: the price of the autonomy the gradient grades, and why position on it is downstream of the oracle trade
- [Behavioral authority](./behavioral-authority.md) — defined-in: the consumer, channel, and force that operative retention requires
- [Gödel machines are a proof-governed case of reflective self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the full-autonomy corner, and what it costs
- [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — evidence: a mid-gradient occupant, with humans at search and the judgment-heavy evaluation
