---
description: "The effort of turning a vague idea into committed prose does double duty — it filters out ideas that cannot survive concretization and it signals where understanding is weakest; current LLM inference removes the filter (the unsound idea ships anyway) and hides the signal (the model's confidence tracks typicality, not soundness, so there is no faithful stall to read off generation). Both losses are intrinsic to the generated output but reconstructable downstream by a separate check; the gap-hiding itself is shared with human writing — the difference is rate and observability, not kind"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining]
status: current
---

# Current LLM inference removes composition friction's filter and hides its signal

Turning a vague mental state into committed prose is costly, and that cost is not waste. The effort of composition does two jobs at once. As a **filter**, it rejects ideas that cannot survive being made concrete: an idea that was "a thousand beautiful, contradictory things at once" has to become one thing, and some ideas have no consistent one-thing to become — they die at the keyboard rather than in print. As a **signal**, the friction is localized — it bites hardest exactly where understanding is thinnest. Weizenbaum's image of a pen that "writes the word 'because' and suddenly stops" (*Computer Power and Human Reason*) is the signal firing: the stall marks the unsupported inference, the place the author thought they understood and did not.

This is the cognitive-side instance of [constraining](./definitions/constraining.md) — narrowing the space of valid interpretations an artifact admits. Composition narrows a nebulous mental state down to one committed interpretation, and the resistance felt while doing it is the artifact pushing back as the narrowing proceeds. Filter and signal are not one event seen twice: the filter is about whether a consistent single interpretation *exists*; the signal is about where committing to it is *hard*. They come apart in both directions. You can stall at a joint and then find the missing link — the signal fires, but the idea survives the filter. And you can smooth over a contradiction and never feel the stall — the filter should have fired and the signal did not, which is how a human ships a hidden bug. Removing both is therefore two losses, not one.

## What cheap inference changes

An LLM that denoises bullet points into fluent paragraphs makes composition nearly frictionless. Both jobs the friction was doing are lost:

- **The filter is removed.** An idea that could not survive concretization now ships anyway, because the model will manufacture a plausible "one thing" from contradictory inputs. The bad node that human search would have pruned early gets expanded instead. This is why frictionless generation correlates with [reverse-compression](./reverse-compression-is-when-llm-output-expands-without-adding.md): the output gains form without the idea gaining structure, because the step that would have killed an empty idea has been skipped.
- **The signal is hidden.** When the model writes "because" smoothly over a gap the author never resolved, there is no stall, no felt resistance at the weak point, and the author loses the map of their own ignorance. It is tempting to say the signal still exists inside the model and merely needs surfacing — but that conflates two different quantities. The human stall fires where an inference *will not hold*; a model's next-token confidence tracks where text is *typical*, and a fluent "because" followed by a plausible clause is exactly what typical prose looks like whether or not the inference is sound. So reading off the model's generation confidence recovers a signal that is *uninformative* about soundness — confidence and validity are decoupled. (It may be worse than uninformative: if clichéd or fallacious moves are themselves high-probability text, confidence would *peak* exactly at the unsound joint. But that anti-correlation needs the added premise that unsound moves are typical ones; decoupling alone does not establish it.) Whether a *separate* internal representation of soundness exists that a probe could read is genuinely open — but it is not the next-token signal. Sycophancy compounds the problem: a model tuned to please would suppress an inconvenient signal even if it had one, because buyers prefer "you're absolutely right."

Both losses are therefore intrinsic to the generated output — present in what the model emits, not a knob that current inference happens to leave off. But they are **reconstructable downstream by a separate operation with teeth** — an external verifier, or an adversarial pass that recomputes soundness rather than reading off fluency (the oracle case below is one instance). The recovery is real, but it is a second check bolted on, not the generator volunteering it.

The two failures compose. Removing the filter lets unsound work through; hiding the signal means neither the author nor a casual reader can locate where it went wrong. The verification cost does not disappear; at best it is borne elsewhere — sometimes the idea is abandoned unread, sometimes a separate tool recomputes the check. But the default recipient is the reader, who must now reweigh every "because" and "therefore" with a logician's scale to reconstruct the signal the author was spared.

None of this is unique to machines. Humans force prose onto unsound ideas too, and hide the gaps just as well: reviewers get carried by fluent argument, and human papers clear review with hidden bugs constantly. The gap-hiding is shared. What current LLM inference changes is the population and the instrument. With the filter gone, far more ideas that would never have survived concretization reach finished prose. A reviewer's hidden bugs at least cleared *one* human's friction-filter; LLM prose lets through ideas that cleared few such filters or none, since the model's manufacture of a plausible "one thing" is at most a weak filter. And with the signal hidden, the difficulty cue a reader could once read off human writing — the hedge, the labored passage, the three-week silence, the draft abandoned — is stripped, and nothing is spent reconstructing it. The difference is rate and observability, not kind.

This is a claim that can be wrong. Its falsifiable commitment: holding the per-document gap-hiding rate roughly fixed, two things should move with the spread of frictionless generation — the share of finished artifacts resting on ideas that never survived a concretization step rises, and a reader's ability to predict an artifact's soundness from its felt difficulty falls toward chance. If unsound-idea throughput does not rise, or if difficulty stays diagnostic of soundness, the mechanism is not doing the work claimed.

## Scope and boundary

The claim is about composition as *discovery*, not composition as *transcription*. Where structure is already settled — reference documentation, mechanical restatement, a known result written down — there is little to filter and no signal to lose, and frictionless generation is a clean win. The mechanism bites only where the prose is doing the thinking: where committing to concrete form is what surfaces the contradiction.

The loss also shrinks where an external oracle re-imposes the friction downstream. Code has a verifier: an inconsistent program fails to compile or fails its tests, so the filter is reconstructed after generation even when generation itself was frictionless. Training against that verifier plausibly also makes generation itself more consistent in code than in prose — a distinct mechanism from the downstream check, but one the same oracle enables. Prose argument has no such oracle; the composition friction *was* the only check, so removing it leaves nothing behind it. The loss therefore bites hardest precisely in the oracle-poor register this KB works in (see [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md)).

This does not license a blanket prohibition on LLM-assisted prose. It locates *which* step must keep a human: the concretization where vague ideas are committed and de-contradicted, not the polishing afterward. A workflow that has a human do the concretizing and an LLM the rendering keeps both the filter and the signal; one that delegates the concretizing loses both regardless of how good the rendering is.

## Relation to hallucination (hypothesis)

A hypothesis: the friction-loss may be the coherence-side sibling of hallucination. Hallucination fills a gap in *knowledge* with fluent content; the friction-loss fills a gap in *reasoning* with a fluent "because" — a fabricated entailment rather than a fabricated fact (coherence vs. correspondence), plausibly two faces of one parent: confident generation decoupled from the warrant the surface marker used to carry. One sharp asymmetry if it holds — a hallucinated fact is retrievable, so grounding can fix it; coherence must be *constructed*, so only a separate constructive check recovers it.

> TODO: expand into a fuller account of this warrant-collapse family (fact, inference, understanding) and consider rehoming to a dedicated hallucination note that this one links to.

## Open Questions

- The signal cannot be recovered by reading off the generator's own confidence (that tracks typicality, not soundness). It may be reconstructable by a *separate* operation — an external oracle, a trained soundness probe, or an adversarial reader that recomputes the inference rather than smoothing it. Open: can such a pass reconstruct enough of the signal to be load-bearing, and would a reconstructed stall carry the weight of an involuntary human one — or does the signal's value depend on its being wrung out of you by the idea's failure to cohere, rather than computed about you after the fact?
- Does this generalize to non-prose constraining (committing to a schema, a type, a function signature)? Codification has the same filter-and-signal structure; whether cheap codegen erodes it the same way is untested here.

---

Relevant Notes:

- [constraining](./definitions/constraining.md) — mechanism: composition friction is the constraining operation paid in real time as a vague mental state narrows to one committed interpretation
- [reverse-compression is when LLM output expands without adding information](./reverse-compression-is-when-llm-output-expands-without-adding.md) — extends: removing the filter is why frictionless generation produces form without added structure
- [vibe-noting](./vibe-noting.md) — extends: names the operational failure mode — a seed inflated into an article — that follows from removing the composition filter
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — modulates: an external oracle (tests) reconstructs the filter downstream, so the loss is smallest in code and largest in oracle-poor prose
- [Human Routers of Machine Words](../sources/borretti-human-routers-of-machine-words.md) — derived-from: Borretti's "writing is thinking" polemic, including the Weizenbaum quote, is the source this claim abstracts
- [Borretti ingest](../sources/borretti-human-routers-of-machine-words.ingest.md) — derived-from: the ingest analysis that flagged this synthesis claim and its boundaries
