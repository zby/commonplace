---
description: "A human writer stalls at the constraint they can't satisfy; an LLM instead ships fluent output that looks solved but silently drops it — hiding the error, so the check falls on the reader"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, llm-interpretation-errors]
---

# LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on

*Mechanistic hypothesis. The observed human/LLM contrast motivates this account, but the proposed plausibility-driven relaxation mechanism remains conjectural.*

A vague goal is a conjunction of constraints. Fernando Borretti's example, "a language as fast as C and as dynamic as Lisp," wants C-speed and Lisp-dynamism and all the unstated rest at once. As a *direction* — climb toward fast and dynamic — the goal is perfectly meaningful; you really can make a language faster and more dynamic. The trouble is only the **reachability assumption**: that the conjunction names a point you can land on, not merely a gradient you can ascend. Concretization tests that assumption: writing the design down is a bounded search for a **witness** — one concrete artifact that satisfies every conjunct at once.

That search is **semi-decidable**: finding a witness proves the goal reachable, but failing to find one proves nothing — maybe no such point exists, maybe you just lacked the trade-off or the insight. (Borretti's "*ex falso* anything can be imagined": the vague dream holds a thousand contradictory things at once precisely because nothing has yet forced it to exhibit one.)

What happens *at* the point of failure is where human and machine writing diverge, and it is the whole of the difference.

## The stall and the relaxation

When a human writer reaches a constraint that will not go — the joint where the goals genuinely pull apart — the pen stops. Josef Weizenbaum's image, in *Computer Power and Human Reason* (p. 108):

> Our pen writes the word "because" and suddenly stops. We thought we understood the "why" of something, but discover that we don't. […] Sometimes we connect two clauses with the word "therefore," only to then see that our chain of reasoning is defective.

The stall is a **beacon at the fault**: failure reports itself, localized to the exact conjunct that could not be met. The writer now knows where their understanding ran out. Stopping is the honest default: most writers halt rather than ship a broken inference. Some paper over the gap, and some ship a mistake they never caught — but for a human those are the exceptions.

LLM generation has no such stop. Give it a goal it cannot fully satisfy and it neither stalls nor refuses: it returns fluent, confident prose that looks like the goal was met. Nothing on the surface marks where it fell short — no hedge at the unmet constraint, no halt, no "this part doesn't work." The output reads as solved whether or not it is, so a reader cannot tell from it which constraint, if any, went unmet. The surface is **camouflage** that points *away* from wherever it failed.

What would produce that? Our hypothesis: generation behaves like an **argmax over plausibility** — the most plausible-looking artifact the trained policy can produce. When that artifact satisfies every conjunct, it *is* a witness; the goal was reached. When it does not, it is a **relaxation**: a plausible witness for a weaker problem with one conjunct dropped. Because the policy emits its argmax either way, there is no discontinuity at the boundary — the dropped conjunct is demoted from hard to soft in silence. The result is a **counterfeit witness**: a real witness for the weaker problem, read as one for the stated problem. The hidden delta is the dropped constraint.

## The cost falls on the reader

The hidden gap can't be read off the surface — fluency tracks [typicality, not soundness](./llm-generation-confidence-tracks-typicality-not-soundness.md), so a fluent passage looks the same whether its constraint was met or dropped. The check can't be offloaded to the output: finding the gap means re-deriving, constraint by constraint, what the surface no longer shows.

## Scope and boundary

The mechanism bites only where the prose is doing the thinking — composition as *discovery*, the search for a witness that may not be found. Where structure is already settled — reference documentation, mechanical restatement, a known result transcribed — there is no witness to search for and no stall to lose, and frictionless generation is a clean win.

The loss also shrinks wherever an external oracle — an automatic verifier — re-imposes the burden downstream. Code has one: a relaxation that drops a real constraint fails to compile or fails its tests, so the witness is checked after generation even when generation was frictionless. Training against that oracle plausibly makes code generation itself more consistent too — a distinct effect the same oracle enables. Prose argument has no such oracle; the composition stall *was* the only check, so removing it leaves nothing behind it. The loss therefore bites hardest in the oracle-poor register this KB works in — [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

This locates which step must keep a human rather than prohibiting LLM prose outright: the concretization where the witness is searched for and the constraints are met, not the rendering afterward. A workflow where a human finds the witness and an LLM renders it keeps the stall; one that delegates the search loses it, however good the rendering.

## Open questions

- Can a separate operation recover the hidden error — an external oracle, a soundness probe, or an adversarial reader that recomputes the dropped constraint instead of reading the fluent surface? Whether such a pass is load-bearing is open.
- Does this extend past prose to [codification](./definitions/codification.md) — committing to a schema, a type, a function signature — where a verifier may change the picture?

---

Relevant Notes:

- [constraining](./definitions/constraining.md) — contrasts: concretization is the author's cost of searching for a witness, while constraining is the reader's interpretive latitude — orthogonal axes. (This note's *relaxation* is the optimization sense — dropping a conjunct — not the KB's *relaxing* defined there, which reopens interpretation space.)
- [vibe-noting](./vibe-noting.md) — extends: names the operational failure mode — a seed rendered into an article — that follows when the witness search is skipped
- [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: the open question asks whether a separate operation can recover the hidden error; this gives the conditions under which a recomputing check actually does
- [Human Routers of Machine Words](../sources/borretti-human-routers-of-machine-words.md) — derived-from: Borretti's "writing is thinking" polemic, the C/Lisp example, and the Weizenbaum quote are the source this claim abstracts
- [Borretti ingest](../sources/borretti-human-routers-of-machine-words.ingest.md) — derived-from: the ingest analysis that flagged this synthesis claim and its boundaries
