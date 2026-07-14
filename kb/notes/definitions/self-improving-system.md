---
description: "Definition — an adaptation loop run on the system itself, through its own writable self-representation, against an improvement objective; autonomy is a separate gradient"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Self-improving system

A **self-improving system** runs an [adaptation loop](../an-adaptation-loop-requires-search-evaluation-and-retention.md) — search, evaluation, operative retention — *on itself*, through its own writable, causally connected self-representation, evaluating candidate changes against an **improvement objective**.

The declared boundary may contain humans. A system whose search and evaluation are performed by people is still a self-improving system; it is simply not an autonomous one. **Autonomy is a separate and gradual property**, recorded per function, and **autonomous self-improving system** is reserved for a loop whose declared boundary contains no human component.

## What has to hold

- **Reflection.** A [causally connected self-representation](./reflective-system.md): a map of the system that is kept true and that steers.
- **Intercession.** Processes inside the boundary can *write* that representation, not only read it.
- **Search.** Something brings a candidate change into consideration — notices the problem, picks the target, generates the candidate.
- **Evaluation against an improvement objective.** Something can *reject* the candidate, on a standard that says what would make the system better. An unconditional trigger is not an evaluator.
- **Operative retention.** The accepted change acquires a consumer, a channel, and a force, in [behavioral authority](./behavioral-authority.md) terms.

The first two are the machinery; the last three are the loop. Reflection routes the loop through the self-representation, which is the difference between improving and merely adapting.

## The improvement objective, and what acceptance establishes

The improvement objective is the standard the evaluator applies: the criterion against which a candidate can *fail*. It is what separates an improvement loop from a mere change loop, and it need not be formal — a proof obligation, a test suite, a validator, a rubric, or a maintainer's judgment all qualify, so long as some possible result is rejection.

What acceptance establishes is narrower than it looks:

> Evaluator acceptance is an *improvement claim*, not evidence that improvement occurred.

The oracle certifies that the candidate met the criterion it applied. It does not certify that the system got better — the criterion may be wrong, partial, or measuring the wrong thing, and [oracles are graded precisely because they differ in what they can establish](../oracle-strength-spectrum.md). So a self-improving system is one that *aims* at improvement and can be wrong about it. The objective makes the loop improvement-directed; only outcomes make it improving.

## Why reflection and intercession are not the property

This is the standing confusion the term needs sharpening against: reflection and intercession are nearly free, and they deliver nothing on their own.

A Smalltalk image has both maximally — the compiler can be edited with the compiler — and left alone it improves nothing for a decade, because [nothing in it performs search or evaluation](./reflective-system.md). Put the programmer inside the declared boundary and Smalltalk-plus-programmer may well be a self-improving system: the loop closes, and it closes through a self-representation. That is the human-inclusive case, and the definition admits it.

## Why the loop must run *through* the self-representation

Adaptation alone is not enough either. [Ashby's Homeostat](../../sources/ashby-design-for-a-brain-ultrastability.md) runs a complete adaptation loop — search, evaluation, retention — with no self-representation anywhere in the mechanism, and it retains: the surviving configuration persists and steers later behavior. What it cannot do is *accumulate*. The thing retained is an opaque parameter setting rather than a representation, so no process in the mechanism can read it, say why it was good, criticize it, or carry it to the next problem. The loop runs indefinitely and nothing compounds.

Route the same loop through a self-representation and the accepted change lands in an artifact the system also *reads*. Each retained change becomes available to the next round of search and evaluation, as knowledge rather than as a setting. That is what the intersection buys, and it is why neither component alone is the object of interest.

## Autonomy is a separate gradient

Autonomy asks a different question: of search, evaluation, and retention, how much runs without a person? It is assessed function by function against the declared boundary, and it grades a self-improving system without deciding whether it is one. A maintained codebase with its dev team sits at the zero end and is genuinely a self-improving system, human-inclusive and fully un-autonomous — [which is cheap to satisfy, and why autonomy rather than the *self* is the discriminating axis](../human-inclusive-boundaries-make-reflection-cheap.md).

**Autonomous self-improving system** is reserved for the case where the declared boundary contains no human component: search, evaluation, and retention all run without a person. Moving the boundary moves the reading, which is why the boundary must be declared before the grading means anything.

Autonomy is the interesting direction, and it cannot be turned up at will. Automating an evaluation for which no adequate oracle exists retains changes nothing checked; evaluation that cannot reject is not evaluation, so the system does not advance along the gradient but drops out of the category, into plain self-modification. Taking autonomy therefore costs something, and [a stronger oracle buys autonomy and pays in reach](../a-stronger-oracle-buys-autonomy-and-pays-in-reach.md) prices it.

## Exclusions

**Self-improving is not self-modifying.** A blind, accidental, or unconditional rewrite changes later behavior without applying any criterion. It is self-modification, and it closes no loop.

**Self-improving is not autonomous.** The two are independent, and conflating them is what the reserved term exists to prevent. A human-inclusive loop is self-improving; only a boundary with no human in it is autonomously so.

**Self-improving is not improving.** The evaluator's acceptance is a claim about the objective it applied, not a demonstration that the system got better.

## Misuse Cases

- Calling a system self-improving because it can modify itself, without identifying what performs search and what could reject a candidate.
- Refusing the name to a loop that closes through a self-representation on the grounds that a human performs part of it — that is an autonomy reading, not a category one.
- Reporting an autonomy grade without declaring the boundary it was assessed against.
- Presenting an autonomy gain as an improvement when the evaluation it automated has no oracle behind it.
- Treating an evaluator's acceptance as evidence that the change improved the system.
- Treating reflection or intercession as the property, rather than as the machinery the property runs on.

---

Relevant Notes:

- [Reflective system](./reflective-system.md) — grounds: the causally connected self-representation, and the intercession capability, that supply the machinery
- [An adaptation loop requires search, evaluation, and operative retention](../an-adaptation-loop-requires-search-evaluation-and-retention.md) — grounds: the three functions the loop must accomplish, and why each is required
- [Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient](../human-inclusive-boundaries-make-reflection-cheap.md) — grounds: why the machinery is nearly free, and why autonomy is the gradient that discriminates
- [Search errors are filtered; evaluation errors are retained](../search-errors-are-filtered-evaluation-errors-are-retained.md) — extends: which function to make autonomous first, and why evaluation is the one that must be bought
- [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: the ceiling on autonomous evaluation
- [A stronger oracle buys autonomy and pays in reach](../a-stronger-oracle-buys-autonomy-and-pays-in-reach.md) — mechanism: the price of the autonomy the gradient grades, and why position on it is downstream of the oracle trade
- [Oracle strength spectrum](../oracle-strength-spectrum.md) — grounds: what an evaluator's acceptance can and cannot establish, which is why acceptance is only an improvement claim
- [Behavioral authority](./behavioral-authority.md) — defined-in: the consumer, channel, and force that operative retention requires
- [Gödel machines are a proof-governed case of reflective self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the autonomous corner, and what it costs
- [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — evidence: a human-inclusive occupant, with humans at search and the judgment-heavy evaluation
- [Ashby, Design for a Brain — ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) — contrasts: an adaptation loop with no self-representation, where what is retained is a setting rather than knowledge, so nothing accumulates
