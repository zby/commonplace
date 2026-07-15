---
description: "Definition — an adaptation loop run on the system itself against an improvement objective; reflective and autonomous name the loop's two independent gradings, each reserved for its boundary case"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Self-improving system

A **self-improving system** runs an [adaptation loop](../an-adaptation-loop-requires-search-evaluation-and-retention.md) — search, evaluation, operative retention — *on itself*, evaluating candidate changes against an **improvement objective**.

*On itself* means the object of change is the system's own behavior-determining structure — its organization, its artifacts, its rules — not an external work product. A compiler that optimizes programs is not self-improving; a compiler pipeline that rewrites its own optimizer is. This is Ashby's two-loop distinction: operating a system is one loop, modifying the system that operates is another.

Two independent properties grade the category without deciding membership, and each has a reserved boundary term:

- **Reflection** — does the loop run *through* a causally connected self-representation? **Reflective self-improving system** is reserved for a loop whose retained changes land in a representation the system also reads.
- **Autonomy** — how much of the loop runs without a person? **Autonomous self-improving system** is reserved for a declared boundary containing no human component.

The declared boundary may contain humans. A system whose search and evaluation are performed by people is still a self-improving system; it is simply not an autonomous one. And a system that retains improvement in an opaque substrate — a parameter setting, model weights — is still a self-improving system; it is simply not a reflective one.

## What has to hold

- **Search.** Something brings a candidate change into consideration — notices the problem, picks the target, generates the candidate.
- **Evaluation against an improvement objective.** Something can *reject* the candidate, on a standard that says what would make the system better. An unconditional trigger is not an evaluator.
- **Operative retention.** The accepted change acquires a consumer, a channel, and a force, in [behavioral authority](./behavioral-authority.md) terms.

That is the whole membership criterion: the loop, aimed. Each function has a weakest viable form, and the floor is occupied. [Ashby's Homeostat](../../sources/ashby-design-for-a-brain-ultrastability.md) searches by random draw, evaluates with a one-bit viability test, and retains by equilibrium — and it modifies its own organization against a standard that can reject, so on this definition it is a self-improving system: minimal, non-reflective, and fully autonomous. What it conspicuously lacks — accumulation — is what the reflective reserved term marks, not what membership requires.

## The improvement objective, and what acceptance establishes

The improvement objective is the standard the evaluator applies: the criterion against which a candidate can *fail*. It is what separates an improvement loop from a mere change loop, and it need not be formal — a proof obligation, a test suite, a validator, a rubric, or a maintainer's judgment all qualify, so long as some possible result is rejection.

What acceptance establishes is narrower than it looks:

> Evaluator acceptance is an *improvement claim*, not evidence that improvement occurred.

The oracle certifies that the candidate met the criterion it applied. It does not certify that the system got better — the criterion may be wrong, partial, or measuring the wrong thing, and [oracles are graded precisely because they differ in what they can establish](../oracle-strength-spectrum.md). So a self-improving system is one that *aims* at improvement and can be wrong about it. The objective makes the loop improvement-directed; only outcomes make it improving.

## Reflective self-improving system

The reserved term for a loop that runs *through* the system's own self-representation: retention lands in an artifact the system also reads, so each accepted change is available to later rounds of search and evaluation as knowledge rather than as a setting.

The machinery is [reflection plus intercession](./reflective-system.md): a causally connected self-representation that processes inside the boundary can write, not only read. The machinery alone delivers nothing — a Smalltalk image has it maximally, the compiler editable with the compiler, and left alone it improves nothing for a decade, because nothing in it performs search or evaluation. Put the programmer inside the declared boundary and Smalltalk-plus-programmer may well be a reflective self-improving system: the loop closes, and it closes through a self-representation.

Reflection is deliberately *not* part of the membership criterion, for two reasons. First, similarity: the field's central cases include loops that retain improvement in weights — a policy improved by self-play, an agent fine-tuned on its own trajectories — and a definition that excludes them by construction would fight every source that uses the term. Second, honesty about what is claim and what is stipulation: the argument for caring about reflection — that only retention through a readable representation is inspectable, criticizable, and transferable — is a thesis with content, and it should stay contestable rather than become true by definition. It lives in [reflection buys addressability, not compounding](../reflection-buys-addressability-not-compounding.md).

## Autonomous self-improving system

Autonomy asks a different question: of search, evaluation, and retention, how much runs without a person? It is assessed function by function against the declared boundary, and it grades a self-improving system without deciding whether it is one. A maintained codebase with its dev team sits at the zero end and is genuinely a self-improving system, human-inclusive and fully un-autonomous — [which is cheap to satisfy, and why bare classification discriminates little](../human-inclusive-boundaries-make-reflection-cheap.md).

**Autonomous self-improving system** is reserved for the case where the declared boundary contains no human component: search, evaluation, and retention all run without a person. Moving the boundary moves the reading, which is why the boundary must be declared before the grading means anything. Note that bare autonomy is also cheap at the floor — the Homeostat runs unattended — so the attribution that discriminates is not autonomy but *warranted* autonomy, and the interesting occupants are composites: the Gödel machine is reflective and autonomous under the strongest available oracle; Commonplace is reflective and human-inclusive.

Autonomy *can* be turned up at will — which is the trap. Two ways of automating an evaluation look alike and are not.

Remove the evaluator, replacing it with an unconditional accept, and there is no evaluator: nothing can be rejected, the loop does not close, and the system drops out of the category into plain self-modification. That is a **category** failure.

Weaken the evaluator — a soft rubric, a model judge, a shallow test — and the loop closes exactly as before. A fallible evaluator still rejects some candidates, so it evaluates; the system is fully autonomous at that gate and fully self-improving. It is simply wrong more often, and its errors are the ones that survive, [since false-positive acceptance becomes operative](../false-positive-generation-is-filtered-before-retention.md). That is a **quality** failure, and it leaves the system inside the category, degrading.

So what an oracle bounds is not autonomy but **warranted autonomy**: how far the loop can run unattended and still be trusted. [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) marks that ceiling, while [warranted autonomy is bounded by oracle reach](../warranted-autonomy-is-bounded-by-oracle-reach.md). Unwarranted autonomy is always available and always cheap.

## Exclusions

**Self-improving is not self-modifying.** A blind, accidental, or unconditional rewrite changes later behavior without applying any criterion. It is self-modification, and it closes no loop.

**Self-improving is not reflective.** A loop that retains improvement in an opaque substrate is inside the category; the reserved term marks the case where retention is also readable. Refusing the name to a weight-level learner is a reflection reading, not a category one.

**Self-improving is not autonomous.** The two are independent, and conflating them is what the reserved term exists to prevent. A human-inclusive loop is self-improving; only a boundary with no human in it is autonomously so.

**Self-improving names the loop, not the outcome.** Membership is earned by how the system is built — a loop, aimed at an objective, running on the system itself. Nothing in that guarantees the objective was the right one, or that the oracle could tell. A system can run its loop faithfully for years and decline.

**A weak oracle is not a broken loop.** An inadequate evaluator still rejects things, so the loop still closes. What it costs is trust, not membership.

## Misuse Cases

- Calling a system self-improving because it can modify itself, without identifying what performs search and what could reject a candidate.
- Refusing the name to a loop because a human performs part of it — that is an autonomy reading, not a category one.
- Refusing the name to a loop because what it retains is opaque — that is a reflection reading, not a category one.
- Treating **reflective self-improving system** as the definition rather than the reserved boundary term, which re-smuggles the addressability thesis into membership.
- Reporting an autonomy grade without declaring the boundary it was assessed against.
- Reading a weak oracle as a broken loop, or a broken loop as a weak oracle: the first is still self-improving and less trustworthy, the second is not self-improving at all.
- Presenting an autonomy gain as an improvement, when what was automated was the *judgment* and not the verification behind it.
- Treating an evaluator's acceptance as evidence that the change improved the system.
- Treating reflection or intercession as the property, rather than as the machinery one grading of the property runs on.

## Provenance and departures

An earlier revision of this definition built the self-representation requirement into membership — "runs an adaptation loop on itself, *through its own writable, causally connected self-representation*." That narrowing was retired in favor of the reserved term, on explication grounds: it failed the similarity criterion (the literature's central cases — parametric self-improvers — fell outside it by construction), and it immunized a substantive thesis by making it definitional. The thesis survives as a claim, where it can be argued with: [reflection buys addressability, not compounding](../reflection-buys-addressability-not-compounding.md). The move mirrors how this definition already treated autonomy: grade the property, reserve a compound term for its boundary case, and keep membership broad.

---

Relevant Notes:

- [An adaptation loop requires search, evaluation, and operative retention](../an-adaptation-loop-requires-search-evaluation-and-retention.md) — grounds: the three functions the loop must accomplish, and why each is required
- [Reflection buys addressability, not compounding](../reflection-buys-addressability-not-compounding.md) — extends: the thesis the reflective reserved term marks — what retention through a readable self-representation adds, and what compounds without it
- [Reflective system](./reflective-system.md) — grounds: the causally connected self-representation, and the intercession capability, that the reflective reserved term requires
- [Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient](../human-inclusive-boundaries-make-reflection-cheap.md) — grounds: why the machinery is nearly free, and why bare classification discriminates little
- [False-positive generation is filtered; false-positive acceptance becomes operative](../false-positive-generation-is-filtered-before-retention.md) — extends: why false-positive acceptance is the dangerous evaluation failure
- [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: the ceiling on autonomous evaluation
- [Warranted autonomy is bounded by oracle reach](../warranted-autonomy-is-bounded-by-oracle-reach.md) — mechanism: the oracle limit on unattended evaluation that remains trustworthy
- [Oracle strength spectrum](../oracle-strength-spectrum.md) — grounds: what an evaluator's acceptance can and cannot establish, which is why acceptance is only an improvement claim
- [Behavioral authority](./behavioral-authority.md) — defined-in: the consumer, channel, and force that operative retention requires
- [Gödel machines are a proof-governed case of reflective self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the reflective and autonomous corner, and what the proof gate costs
- [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — evidence: a reflective, human-inclusive occupant, with humans at search and the judgment-heavy evaluation
- [Ashby, Design for a Brain — ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) — exemplifies: the floor of the category — a minimal, non-reflective, autonomous occupant that retains without accumulating
