---
description: "Conjecture: writing a provisional claim first and reading only passages likely to overturn it may build a better-warranted synthesis note at lower context cost than reading everything first — motivated by Karnofsky, untested here."
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: []
---

# Claim-routed reading may beat reading-first for synthesis notes

**Status: conjecture.** Motivated by one practitioner account ([Learning By Writing](https://www.cold-takes.com/learning-by-writing/)); untested in this KB. Treat it as a hypothesis with a named test, not a finding.

The default multistage path reads the sources, then synthesizes: gather everything relevant, then find the claim. Karnofsky's inversion is to write a provisional bottom-line claim *first* — before being "qualified" — and let that claim decide what to read next: identify the subquestion most likely to change the claim, read narrowly toward it, revise, repeat. Reading is in service of writing, not the reverse.

The conjecture is that, for a note synthesizing several sources, claim-routed reading produces a better-warranted note at lower context cost than read-then-synthesize.

## Mechanism: the claim is a selection pressure

A written claim names what would overturn it. That turns an open-ended "read the sources" into a targeted search: read the passage that could move the claim, skip the passages that could not. [Warranted reader update is the objective](./warranted-reader-update-is-the-objective-of-substantive-writing.md), and a committed provisional claim supplies the selection pressure that an open gathering pass lacks — [a bare writing prompt does not determine the contribution](./a-bare-writing-prompt-does-not-determine-its-intended-contribution.md), but a provisional claim does, provisionally.

Two benefits are hypothesized. First, context economy: comprehensively reading every source spends bounded context on material that never bears on the claim, while routing reads only what could change it — relevant where [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). Second, warrant: a note built by surviving a sequence of claim-changing challenges retains the reasoning that selected it, rather than a pile of gathered facts whose relevance to the claim was never tested.

## Failure mode: anchoring

The same claim that routes reading can bias it. If the provisional claim only ever selects confirming passages, the loop launders a first guess into a fake conclusion. Karnofsky's countermeasure is to route toward the *disconfirming* subquestion on purpose, and to periodically flip the hypothesis and argue the other side even when unconvinced. Without that, claim-routing is worse than reading-first, not better: it is passive assent dressed as inquiry. So the conjecture holds only for a routing loop that spends its selection budget on what could break the claim.

## Scope

The claim is about multi-source synthesis notes — the ingest-and-multistage register where a note's value is the selected relation among sources. It does not apply to single-source capture, faithful transcription, or a note whose contribution is already determined before any reading.

## How this could be wrong

The discriminating test is a comparison, not an intuition: build the same synthesis note both ways — claim-routed and read-then-synthesize — and compare the warranted update and the context cost. If routed reading yields the same note, it bought only a feeling of focus. If it yields an anchored note that never seriously read against its first claim, the failure mode dominates and reading-first is safer. The conjecture is that a disconfirmation-routed loop beats reading-first on warrant per unit of context; anything less refutes it.

## Open questions

- Can an agent reliably pick "the subquestion most likely to change the claim," or does that judgment need the comprehensive read the routing is trying to avoid?
- Does routing belong as a replacement for the multistage workflow's reading stage, or only as a heuristic inside it?

---

Relevant Notes:

- [Warranted reader update is the objective of substantive writing](./warranted-reader-update-is-the-objective-of-substantive-writing.md) — grounds: routing is a search strategy for the update, and the provisional claim is what exerts the selection pressure
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: reading only claim-relevant passages spares bounded context
- [A bare writing prompt does not determine its intended contribution](./a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) — contrasts: a provisional claim supplies, provisionally, the contribution direction a bare prompt leaves open
- [Learning By Writing](https://www.cold-takes.com/learning-by-writing/) — abstracted-from: Karnofsky's hypothesis-first investigation loop that motivates this conjecture
