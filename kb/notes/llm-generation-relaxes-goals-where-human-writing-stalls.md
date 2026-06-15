---
description: "On a goal it can't satisfy, a human writer stalls at the unmet constraint; LLM generation returns a typicality-biased relaxation that hides the hard constraint, displacing the check onto the reader"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, llm-interpretation-errors]
status: speculative
---

# LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on

*Speculative. Modeling generation as an argmax over plausibility is a working hypothesis, not a literal account of decoding; the relaxation mechanism it supports is argued here, not established.*

A vague goal is a conjunction of constraints. Fernando Borretti's example, "a language as fast as C and as dynamic as Lisp," wants C-speed and Lisp-dynamism and all the unstated rest at once. As a *direction* — climb toward fast and dynamic — the goal is perfectly meaningful; you really can make a language faster and more dynamic. The trouble is only the **reachability assumption**: that the conjunction names a point you can land on, not merely a gradient you can ascend. Concretization tests that assumption: writing the design down is a bounded search for a **witness** — one concrete artifact that satisfies every conjunct at once.

That search is **semi-decidable**: success is conclusive, failure is not. Finding the witness proves the goal reachable; failing to find it does not prove the goal unreachable — only that you did not reach it within the budget you spent. Maybe no point exists; maybe you lacked the trade-off, the abstraction, the insight. So the search certifies only one direction: it can confirm a goal is reachable but never that it is not. That is a **burden of proof on an existential claim** — assert reachability only once you hold the witness. (Borretti's "*ex falso* anything can be imagined" is the failure of those who skip the burden — the vague dream holds a thousand contradictory things at once precisely because nothing has yet forced it to exhibit one.)

What happens *at* the point of failure is where human and machine writing diverge, and it is the whole of the difference.

## The stall and the relaxation

When a human writer reaches a constraint that will not go — the joint where the goals genuinely pull apart — the pen stops. Josef Weizenbaum's image, in *Computer Power and Human Reason* (p. 108):

> Our pen writes the word "because" and suddenly stops. We thought we understood the "why" of something, but discover that we don't. […] Sometimes we connect two clauses with the word "therefore," only to then see that our chain of reasoning is defective.

The stall is a **beacon at the fault**: failure reports itself, localized to the exact conjunct that could not be met. The writer now knows where their understanding ran out.

LLM generation has no such stop. Give it a goal it cannot fully satisfy and it neither stalls nor refuses: it returns fluent, confident prose that looks like the goal was met. Nothing on the surface marks where it fell short — no hedge at the unmet constraint, no halt, no "this part doesn't work." The output reads as solved whether or not it is, so a reader cannot tell from it which constraint, if any, went unmet. The surface is **camouflage** that points *away* from wherever it failed.

What would produce that? Model generation as an **argmax over plausibility** — the most plausible-looking artifact the trained policy can produce. When that artifact satisfies every conjunct, it *is* a witness; the goal was reached. When it does not, it is a **relaxation**: a plausible witness for a weaker problem with one conjunct dropped. Because the policy emits its argmax either way, there is no discontinuity at the boundary — the dropped conjunct is demoted from hard to soft in silence. The result is a **counterfeit witness**: a real witness for the weaker problem, read as one for the stated problem. The hidden delta is the dropped constraint.

## Why the relaxation lands on the crux

Two things make this worse than mere concealment.

**The relaxation is typicality-biased.** Where the novel constraint is also the least probable to render fluently, it is the one most likely to be shed — the typical, well-trodden constraints surviving. That condition usually holds, since novelty is what makes a constraint rare. And the novel constraint is usually the *point* of the idea. So the relaxation tends to sacrifice the load-bearing crux and preserve the boilerplate, gaining form without the idea gaining structure — the mechanism behind [reverse-compression](./reverse-compression-is-when-llm-output-expands-without-adding.md). This is [confidence tracks typicality, not soundness](./llm-generation-confidence-tracks-typicality-not-soundness.md) operating on constraints: what survives is what is typical, and the conjunct that made the idea worth having is the first thing typicality discards.

**Friction and fluency invert at the crux.** At the load-bearing joint, the human pen stalls *hardest* — the felt resistance bites where understanding is thinnest. At the same joint, the model is *smoothest* — it generates straight over the gap, because typicality stays high even where soundness fails. The exact place a human writer flags is the exact place the model flows. Felt difficulty and machine fluency are anti-correlated with truth at the one constraint that matters — the stronger claim that decoupling alone does not license, holding only where the fluent move over the gap is itself typical.

## The check moves to the reader, and gets harder

Two questions coincide in the human stall: whether a witness exists, and where the search is failing. One event reports both. The relaxation removes that event and reports neither. So the check does not vanish; it is displaced onto the reader, and made dramatically more expensive.

A human-flagged fault gives the reader one localized joint to inspect. A relaxation-hidden fault forces a search over an unknown, partly-implicit constraint set for the conjunct that was silently dropped. Every candidate check is real work, because the surrogate looks plausible at each one. This is Borretti's "weight every 'because' and 'therefore' with a logician's scale": the relaxation forces an exhaustive constraint-by-constraint audit precisely because nothing in the surface localizes the gap. Worse, the counterfeit witness is output-indistinguishable from a real one: the reader cannot tell whether the search terminated in a true witness or timed out into a relaxation. The burden of proof arrives undischarged while looking discharged.

This is a claim that can be wrong. Holding the per-document gap-hiding rate roughly fixed, two things should move as frictionless generation spreads. The share of finished artifacts resting on goals whose witness was never found should rise; and a reader's ability to predict an artifact's soundness from its felt difficulty should fall toward chance. If under-witnessed throughput does not rise, or difficulty stays diagnostic of soundness, the mechanism is not doing the work claimed.

## Scope and boundary

The mechanism bites only where the prose is doing the thinking — composition as *discovery*, the search for a witness that may not be found. Where structure is already settled — reference documentation, mechanical restatement, a known result transcribed — there is no witness to search for and no stall to lose, and frictionless generation is a clean win.

The loss also shrinks wherever an external oracle — an automatic verifier — re-imposes the burden downstream. Code has one: a relaxation that drops a real constraint fails to compile or fails its tests, so the witness is checked after generation even when generation was frictionless. Training against that oracle plausibly makes code generation itself more consistent too — a distinct effect the same oracle enables. Prose argument has no such oracle; the composition stall *was* the only check, so removing it leaves nothing behind it. The loss therefore bites hardest in the oracle-poor register this KB works in — [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

This locates which step must keep a human rather than prohibiting LLM prose outright: the concretization where the witness is searched for and the constraints are met, not the rendering afterward. A workflow where a human finds the witness and an LLM renders it keeps the stall; one that delegates the search loses it, however good the rendering.

## Relation to hallucination (hypothesis)

The relaxation may be the coherence-side sibling of hallucination. Hallucination fills a gap in *knowledge* with a fluent fact; the relaxation fills a gap in *reasoning* with a fluent "because" — a dropped entailment rather than a dropped fact (coherence vs. correspondence). Both are plausibly [two faces of one parent](./llm-generation-confidence-tracks-typicality-not-soundness.md) — confidence that tracks typicality rather than soundness, applied to fact and to inference — the correspondence/coherence split that note sets out directly. One sharp asymmetry if it holds — a hallucinated fact is retrievable, so grounding can repair it; a missing witness must be *constructed*, so only a separate constructive search recovers it.

## Open questions

- Can a separate operation reconstruct the stall? It cannot be read off the generator's own confidence (typicality, not soundness), but an adversarial reader or a soundness probe that recomputes each conjunct might recover it — whether such a pass is load-bearing is open.
- Would a reconstructed stall carry the weight of an involuntary one — or does the signal's value depend on being wrung out of you by the idea's failure to cohere, rather than computed about you after the fact?
- Does this extend past prose to [codification](./definitions/codification.md) — committing to a schema, a type, a function signature? The conjunction-of-constraints framing is even more literal there, but whether cheap codegen relaxes it the same way is untested here.

---

Relevant Notes:

- [The machine searches for the camouflage a human writer usually slips into](./machine-searches-for-camouflage-human-writer-slips-into.md) — extends: the human-vs-machine asymmetry (the machine *searches* for the camouflage) and the training corollary that follows from it
- [constraining](./definitions/constraining.md) — contrasts: concretization is the author's cost of searching for a witness, while constraining is the reader's interpretive latitude — orthogonal axes. (This note's *relaxation* is the optimization sense — dropping a conjunct — not the KB's *relaxing* defined there, which reopens interpretation space.)
- [vibe-noting](./vibe-noting.md) — extends: names the operational failure mode — a seed rendered into an article — that follows when the witness search is skipped
- [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: the open question asks whether a separate operation can reconstruct the stall; this gives the conditions under which a recomputing check actually recovers it
- [Human Routers of Machine Words](../sources/borretti-human-routers-of-machine-words.md) — derived-from: Borretti's "writing is thinking" polemic, the C/Lisp example, and the Weizenbaum quote are the source this claim abstracts
- [Borretti ingest](../sources/borretti-human-routers-of-machine-words.ingest.md) — derived-from: the ingest analysis that flagged this synthesis claim and its boundaries
