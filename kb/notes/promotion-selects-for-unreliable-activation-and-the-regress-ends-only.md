---
description: "Recasts the retention criterion from 'the consumer lacks this' to 'the consumer will not apply this unprompted', and argues a promoted conclusion stays unfinished until its trigger bottoms out outside the retained-artifact chain"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [agent-memory, context-engineering, failure-modes]
---

# Promotion selects for unreliable activation, and the regress ends only at an external trigger

A **promotion theory** is the rule deciding which candidate conclusions earn a durable place in retained memory — which observations become notes, which lessons become rules, which conventions get written down. The obvious criterion is absence: retain what the consumer does not already know. Project decisions, local conventions, and facts postdating training are absent from the weights, so they must be stored.

Absence is a real reason, but taken as *the* criterion it selects the wrong set. The failure a retained conclusion prevents is not only "the consumer lacked it" — since [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), the more common failure is that the consumer held the conclusion and did not bring it to bear. What promotion buys is a gain in the probability that the conclusion is *applied on its occasion*, not in the probability that it can be *produced on request*. Absence is the special case where that probability is zero for lack of content. Unreliable activation is the general case, and in a domain the model already knows well it is the only case left.

The [three-way separation of generation, activation, and selection failure](./weakly-discriminated-qualities-tend-to-be-underselected.md) makes the same point diagnostically: "the model lacks the knowledge" is sufficient to explain a bad outcome but not necessary, and the remedies diverge. A promotion theory is one of those remedies, and it should be aimed at the failure it can actually fix.

## The two criteria rank candidates differently

| | Absence criterion | Activation criterion |
|---|---|---|
| Promotes | what the consumer does not know | what the consumer will not raise unprompted |
| Rejects | the obvious | the self-triggering, however obscure |
| Value measured as | novelty of the content | change in probability of application, times what rides on the occasion |
| Predicted trend | shrinks as models learn more | does not shrink with model knowledge, and may grow as more knowledge competes for the same attention |

The rankings invert at both ends. A conclusion the consumer agrees with the moment it is stated, but never states first, scores zero under absence and high under activation — the expert-witness case, where the model answers the question asked and does not raise the concern nobody asked about. Conversely, an obscure fact the consumer reliably looks up when the occasion arises earns a high absence score and nothing under activation: the lookup already fires.

That yields a difference someone could observe. An absence theory predicts a stronger model retires much of a KB, because the retained content was standing in for missing knowledge. An activation theory predicts model upgrades retire the reference material and leave the activation-carrying material standing, because knowing more does not make a conclusion self-raising.

This sharpens rather than replaces the existing cost test. [Promotion is already gated on future value exceeding maintenance cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md), with retrieval and activation named together as sources of that value. Separating them matters because they behave differently: retrieval value decays as models improve, activation value does not, and only activation value imposes the trigger obligation argued below.

## The promoted artifact inherits the problem it was promoted to solve

If promotion is justified by making activation reliable, the promoted artifact needs its own activation. A note read only when the consumer already has the topic in mind reproduces the original failure one level up: the consumer must now remember to remember. Ask what surfaces the note, and the same question applies to whatever answers. That chain is the **activation regress**.

The regress cannot close inside the [retained-artifact](./definitions/retained-artifact.md) chain. Every candidate terminator of the form "the agent will consult the index", "the agent will search first", "the agent will recall the convention" re-asserts exactly the reliability the promotion assumed absent. It closes only at a step whose firing does not depend on the promoted content being recalled — a **trigger external to the chain**: [content loaded unconditionally every session](./always-loaded-context-mechanisms-in-agent-harnesses.md), harness-level discovery that scans artifact descriptions unbidden, an event-fired hook, a validator the build runs, a naming convention read by code, or a human who invokes the procedure.

[The methods available for firing behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md) are already catalogued as a design menu; the regress argument says why the menu has to be drawn from outside the artifact chain rather than from within it, and why picking an item from it is part of promotion rather than a later refinement.

Chains are fine — the regress only has to be finite. A note reached from a tag index reached from a routing table in an always-loaded file terminates externally in three hops. What fails is the open end and the cycle.

**So a retained conclusion's trigger is load-bearing, not metadata.** Promotion is incomplete until the trigger is named and checked to bottom out. That check charges a cost the absence criterion never does: an untriggered artifact is not merely inert, it consumes scarce context and maintenance budget and dilutes the cues serving artifacts that do fire. Where no external trigger exists, the honest options are to build one or to decline the promotion.

The neglect this check corrects is empirical, not hypothetical: a [comparative review of agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) finds most surveyed systems push memory into context, mostly through coarse always-loading, and almost none test whether the pushed memory changes behavior.

The argumentative shape is borrowed. [Revising an improvement objective is licensed only from outside it](./revising-an-improvement-objective-is-licensed-from-outside-it.md) dissolves a parallel regress by observing that the chain ends at a *declaration*, because the objective is declared rather than derived. Here the chain ends at a *mechanism*, because firing is caused rather than chosen. Both refuse to let the system supply its own terminus; they differ in what the outside contributes — a stipulation there, an event here.

### Two kinds of terminator, only one of them engineerable

A trained disposition also terminates the regress: a model that reliably searches the repository before editing supplies a trigger that is not itself a retained artifact. This is a genuine terminator, and treating it as unavailable would overstate the claim. It differs from a mechanical one in what the author controls. The harness, the hook, and the build fire on conditions the author sets and can watch failing; a disposition fires on conditions the author neither sets nor sees, and its reliability is inherited from the model rather than designed.

Ranking terminators by that control is what the instruction → skill → hook → script gradient in [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) measures — each rung moves the firing decision further out of the consumer's discretion, and codification is the limit where no activation decision remains. [Frontloading](./frontloading-spares-execution-context.md) is the degenerate case at the far end: pre-compute the conclusion into the consuming context and nothing needs triggering at all. [Periodic hygiene is the clearest worked instance](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) — work that cannot be triggered from task-serving routing at all, so its trigger has to come from a user, a heartbeat, or CI.

Statelessness is why this bites harder for agents than for people. A human operator accumulates the navigational intuition that serves as a partial internal terminator; [an agent starts every session without it](./agent-statelessness-makes-routing-architectural-not-learned.md), so the routing that fires the artifact is permanent architecture rather than scaffolding to be outgrown. The same statelessness is why [the context engine should inject context rather than wait to be asked](./agent-statelessness-means-the-context-engine-should-inject-context.md).

## The resulting promotion test

1. Is there an occasion where this conclusion changes what gets done?
2. On that occasion, would it be applied *without* the artifact? If yes, decline — however non-obvious the content is.
3. What outside the retained-artifact chain puts the artifact on that occasion? If nothing, build a trigger or decline.

Step 2 is the selection criterion; step 3 is the completion condition. A conclusion passing 2 and failing 3 is a correct promotion decision with no delivery mechanism, which is indistinguishable in effect from not having promoted it.

Delivery is a different kind of gate from the two already in use — [validity and learning value](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) and [a statable applicability boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md). Those judge the conclusion's content; this one judges its path to the occasion, and a candidate can clear both content gates while having no path at all.

## Scope

Absence remains a genuine promotion reason. Content no trigger can conjure — a decision made last week, a local convention — has to be stored before it can be surfaced. The two criteria answer different questions: absence says whether the conclusion must be *stored*, unreliable activation says whether storing it *helps*. Neither subsumes the other. The claim is that a theory using absence alone under-promotes the known-but-unraised and over-promotes the obscure-but-self-triggering.

Externality is necessary for termination, not sufficient for value. A stale index fires perfectly reliably and routes to nothing — [worse than no index](./stale-indexes-are-worse-than-no-indexes.md), because a trigger that satisfies the navigation need suppresses the fallback search that would have worked.

Termination can also be priced out. The most reliable terminator — unconditional loading — is the costliest, and a shared terminator has finite capacity: [ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) retired always-loaded generated indexes when their unconditional cost grew with the collection. Step 3 can be satisfiable and still not worth paying.

"Build a trigger" is not always available. [Symbolic routing can react only after a usable symbol exists](./symbolic-context-engineering-is-bounded-by-symbol-availability.md), so an occasion nothing in the workflow names cannot be triggered on symbolically, and the fallback is a costlier always-loaded slot or an LLM-judged cue. Step 3 can therefore fail for reasons that are not the author's fault, and declining the promotion is a legitimate outcome rather than a defeat.

The weak point is measurement. Activation reliability is not cheaply observable in advance: the estimate comes from watching the conclusion fail to fire, which is why a first occurrence belongs in a log and a note waits for the mechanism to be understood. A promotion theory selecting on unreliable activation therefore presupposes [a channel that records misses](./diagnostic-richness-constrains-outer-loop-learning-quality.md). Without one it degrades into guessing which conclusions the consumer probably will not think of — a guess an absence criterion at least does not pretend to make.

## Open Questions

- What is the cheapest instrument that estimates activation reliability for a candidate conclusion *before* promoting it, rather than after observing the miss?
- Is trigger externality binary or graded? Harness-level description scanning is external to the artifact chain and still probabilistic, which suggests the ladder measures a continuum rather than a threshold.
- When many artifacts share one external terminator — a single always-loaded routing file — does that terminator's capacity become the binding constraint on how much a KB can usefully retain?

---

Relevant Notes:

- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: supplies the storage/context/activation separation the selection criterion is defined over
- [weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — grounds: the generation/activation/selection trichotomy that makes "the model lacks it" an inadequate default diagnosis
- [Promote only when future value exceeds maintenance cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — extends: splits that note's combined "retrieval or activation value" term and adds the trigger check as a promotion obligation
- [Activate behavior-changing memory before the mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) — mechanism: the catalogue of firing methods this note argues must be selected from at promotion time
- [revising an improvement objective is licensed from outside it](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — contrasts: the same refusal to let a system supply its own terminus, closing at a declaration rather than at a mechanism
- [agent statelessness makes routing architectural, not learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — grounds: why a stateless consumer cannot supply an internal terminator
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — mechanism: the instruction → skill → hook → script gradient measures how far a trigger's firing sits outside the consumer's discretion
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the limiting move where the conclusion is pre-inserted and no activation decision remains
- [periodic KB hygiene should be externally triggered, not embedded in routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) — evidenced-by: a work class whose trigger demonstrably cannot come from the agent's own routing
- [symbolic context engineering is bounded by symbol availability](./symbolic-context-engineering-is-bounded-by-symbol-availability.md) — grounds: the availability limit that can make "build a trigger" unavailable and force a decline
- [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — evidenced-by: a trigger that fires reliably and still destroys value, bounding externality to necessary rather than sufficient
- [retained artifact](./definitions/retained-artifact.md) — defined-in: the artifact class whose chain the regress runs through
- [always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) — evidenced-by: survey of which unconditional-load terminators real harnesses actually provide
- [agentic memory systems comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — evidenced-by: most surveyed systems push memory via coarse always-loading and almost none test behavioral effect
- [ADR 025: complete generated indexes are build-time only](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — evidenced-by: a shared always-loaded terminator whose unconditional cost became binding and forced discovery to build time
- [agent statelessness means the context engine should inject context](./agent-statelessness-means-the-context-engine-should-inject-context.md) — extends: closes the trigger-mechanism question that note's injection claim leaves open
- [choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — extends: adds delivery as a third gate, structurally different from both content gates
- [abstract an experience only when you can state the boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — contrasts: sibling promotion gate that judges the conclusion's content where this one judges its path to the occasion
- [diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: the general result behind why a missing miss-recording channel degrades activation-based selection
- [only explicit retention is durable, writable, and addressable](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: why a parametric disposition's firing conditions sit outside author control
