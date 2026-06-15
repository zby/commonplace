---
description: "On a goal it can't satisfy, a human writer stalls at the unmet constraint; LLM generation returns a typicality-biased relaxation that hides the hard constraint, displacing the check onto the reader"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory]
status: seedling
---

# LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on

A vague goal is a conjunction of constraints. "A language as fast as C and as dynamic as Lisp" is C-speed ∧ Lisp-dynamism ∧ all the unstated rest. As a *direction* — climb toward fast and dynamic — the goal is perfectly meaningful; you really can make a language faster and more dynamic. The trouble is only the **reachability assumption**: that the conjunction names a point you can land on, not merely a gradient you can ascend. Concretization is what tests that assumption. Writing the design down is a bounded search for a **witness** — one concrete artifact that satisfies every conjunct at once.

That search is semi-decidable, and asymmetric. Finding the witness is conclusive: the artifact exists, the goal was reachable. Failing to find it is not — you cannot conclude the goal was unreachable, only that you did not reach it within the budget you spent. Maybe no point exists; maybe you lacked the trade-off, the abstraction, the insight. So composition does not sort ideas into meaningful and meaningless. It enforces a **burden of proof on an existential claim**: assert that a goal is reachable only once you hold the witness. (Borretti's "*ex falso* anything can be imagined" is the failure of those who skip the burden — the vague dream holds a thousand contradictory things at once precisely because nothing has yet forced it to exhibit one.)

What happens *at* the point of failure is where human and machine writing diverge, and it is the whole of the difference.

## The stall and the relaxation

When a human writer reaches a constraint that will not go — the joint where the goals genuinely pull apart — the pen stops. Weizenbaum's image, in *Computer Power and Human Reason* (p. 108):

> Our pen writes the word "because" and suddenly stops. We thought we understood the "why" of something, but discover that we don't. […] Sometimes we connect two clauses with the word "therefore," only to then see that our chain of reasoning is defective.

The stall is a **beacon at the fault**: failure reports itself, localized to the exact conjunct that could not be met. The writer now knows where their understanding ran out.

LLM generation has no such stop, because it is always running one operation: return the **argmax** — the most plausible artifact available. When a full witness exists, that argmax *is* the witness; every conjunct is met. When none exists, the argmax is simply a **relaxation** (here in the optimization sense — dropping a conjunct — not the KB's *relaxing*, which reopens a reader's interpretation space): a plausible witness for a weaker problem, returned with no change in behavior, no halt, no "unsatisfiable." The relaxed witness is just what plausibility-maximization yields whenever no full witness is in reach. (The MAX-SAT analogy is close but imperfect: the model maximizes *plausibility*, not the *number* of conjuncts satisfied — and the next section is precisely why those two come apart at the constraint that matters.) There is no discontinuity at the boundary, so the dropped conjunct is demoted from hard to soft in silence, and the output is not a beacon but **camouflage**: optimized to look maximally satisfied, its surface points *away* from the one place it failed. This is a counterfeit witness — a genuine witness for a weaker problem, presented exactly as a witness for the stated one, because nothing in returning the argmax marks whether it was total. The hidden delta is the dropped constraint.

## Why the relaxation lands on the crux

Two things make this worse than mere concealment.

**The relaxation is typicality-biased.** The model does not drop a random conjunct; it keeps the typical, well-trodden constraints and sheds the rare, hard, novel one — because the novel constraint is the least probable to render fluently. But the novel constraint is usually the *point* of the idea. So the relaxation preferentially sacrifices the load-bearing crux and preserves the boilerplate, gaining form without the idea gaining structure — the mechanism behind [reverse-compression](./reverse-compression-is-when-llm-output-expands-without-adding.md). This is [confidence tracks typicality, not soundness](./llm-generation-confidence-tracks-typicality-not-soundness.md) operating on constraints: what survives is what is typical, and the conjunct that made the idea worth having is the first thing typicality discards.

**Friction and fluency invert at the crux.** At the load-bearing joint, the human pen stalls *hardest* — the felt resistance bites where understanding is thinnest. At the same joint, the model is *smoothest* — it generates straight over the gap, because typicality stays high even where soundness fails. The exact place a human writer flags is the exact place the model flows. Felt difficulty and machine fluency are anti-correlated with truth at the one constraint that matters.

## The check moves to the reader, and gets harder

Two questions coincide in the human stall: whether a witness exists, and where the search is failing. One event reports both. The relaxation removes that event and reports neither. So the check does not vanish; it is displaced onto the reader, and made dramatically more expensive.

A human-flagged fault costs the reader O(1): inspect the joint the writer stalled at. A relaxation-hidden fault costs a search over an unknown, partly-implicit constraint set for the conjunct that was silently dropped — and every candidate check is real work, because the surrogate was built to be plausible at each one. This is Borretti's "weight every 'because' and 'therefore' with a logician's scale": the relaxation forces an exhaustive constraint-by-constraint audit precisely because it was engineered to be unlocalizable. Worse, a counterfeit witness is output-indistinguishable from a real one — the reader cannot tell from the prose whether the search terminated in a true witness or timed out into a relaxation, so the burden of proof arrives undischarged while looking discharged.

This is a claim that can be wrong. Holding the per-document gap-hiding rate roughly fixed, two things should move as frictionless generation spreads: the share of finished artifacts resting on goals whose witness was never found should rise, and a reader's ability to predict an artifact's soundness from its felt difficulty should fall toward chance. If under-witnessed throughput does not rise, or difficulty stays diagnostic of soundness, the mechanism is not doing the work claimed.

## A shared failure mode, but only one side searches for it

None of the mechanism is unique to machines. A human can also smooth over a constraint they failed to meet — reviewers get carried by fluent argument, papers ship with hidden gaps. So the *failure mode* — emitting a relaxation — is shared, and you meet it in human-authored text too.

What is not shared — this part is a hypothesis — is the **search** for it. A human relaxation is an unsearched slip: an oversight or a self-deception, whatever happened to get written at the joint they failed to notice. The LLM relaxation is the *argmax* of an objective that rewards surface plausibility — next-token and preference training optimize for text that *looks* satisfied, so when no full witness is available the model does not drop a constraint at random; it selects the relaxation that looks most solved. (Borretti names that objective from the inside: "if I don't turn this garbage into something presentable the RLHF device will shock me again.")

That search is what drives the observability gap. The human, not optimizing to hide the gap, leaves residue a reader can use — the hedge, the labored passage, the three-week silence, the abandoned draft. The model, optimizing for exactly the plausible surface, leaves as little as it can: its camouflage is *selected* to be undetectable, not incidentally smooth. The failure is the same in kind; the process that produces it is not — and that difference in process is why the machine relaxation is the harder one to catch. The model also relaxes by default, with no stall to clear, so more under-constrained ideas reach finished prose to begin with.

## Scope and boundary

The mechanism bites only where the prose is doing the thinking — composition as *discovery*, the search for a witness that may not be found. Where structure is already settled — reference documentation, mechanical restatement, a known result transcribed — there is no witness to search for and no stall to lose, and frictionless generation is a clean win.

The loss also shrinks wherever an external oracle re-imposes the burden downstream. Code has a verifier: a relaxation that drops a real constraint fails to compile or fails its tests, so the witness is checked after generation even when generation itself was frictionless — and training against that oracle plausibly makes generation in code more consistent too, a distinct effect the same oracle enables. Prose argument has no such oracle; the composition stall *was* the only check, so removing it leaves nothing behind it. The loss therefore bites hardest in the oracle-poor register this KB works in — [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

This locates which step must keep a human rather than prohibiting LLM prose outright: the concretization where the witness is searched for and the constraints are met, not the rendering afterward. A workflow where a human finds the witness and an LLM renders it keeps the stall; one that delegates the search loses it, however good the rendering.

## Relation to hallucination (hypothesis)

The relaxation may be the coherence-side sibling of hallucination. Hallucination fills a gap in *knowledge* with a fluent fact; the relaxation fills a gap in *reasoning* with a fluent "because" — a dropped entailment rather than a dropped fact (coherence vs. correspondence), plausibly two faces of one parent: confidence that tracks typicality rather than soundness, applied to fact and to inference. One sharp asymmetry if it holds — a hallucinated fact is retrievable, so grounding can repair it; a missing witness must be *constructed*, so only a separate constructive search recovers it.

## Training implication (speculative)

If the model camouflages the shortfall because the objective rewards surface plausibility, the stall-signal may be suppressed by that objective rather than absent — and an objective that instead rewarded the model for *flagging* the constraint it dropped (marking the output a relaxation, or refusing) could train the stall back in. The catch is the same boundary inverted: such a target is cheapest where a verifier can label solved-vs-relaxed — code, math — which is where the loss was already smallest, and hardest to build in the oracle-poor prose where the stall would help most.

## Open questions

- Can a separate operation reconstruct the stall? It cannot be read off the generator's own confidence (typicality, not soundness), but an adversarial reader or a soundness probe that recomputes each conjunct might recover it. Open whether such a pass is load-bearing — and whether a reconstructed stall carries the weight of an involuntary one, or whether the signal's value depends on being wrung out of you by the idea's failure to cohere rather than computed about you after the fact.
- Does this extend past prose to codification — committing to a schema, a type, a function signature? The conjunction-of-constraints framing is even more literal there, but whether cheap codegen relaxes it the same way is untested here.

---

Relevant Notes:

- [constraining](./definitions/constraining.md) — contrasts: concretization is the author's cost of searching for a witness; constraining is the reader's interpretive latitude in the finished artifact — orthogonal axes that vary independently
- [vibe-noting](./vibe-noting.md) — extends: names the operational failure mode — a seed rendered into an article — that follows when the witness search is skipped
- [Human Routers of Machine Words](../sources/borretti-human-routers-of-machine-words.md) — derived-from: Borretti's "writing is thinking" polemic, the C/Lisp example, and the Weizenbaum quote are the source this claim abstracts
- [Borretti ingest](../sources/borretti-human-routers-of-machine-words.ingest.md) — derived-from: the ingest analysis that flagged this synthesis claim and its boundaries
