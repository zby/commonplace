---
description: "Recasts the retention criterion from 'the consumer lacks this' to 'the consumer will not apply this unprompted', and argues a promoted conclusion stays unfinished until its trigger bottoms out outside the retained-artifact chain"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [agent-memory, context-engineering, failure-modes]
---

# Promotion selects for unreliable activation, and the regress ends only at an external trigger

A **promotion theory** decides which candidate conclusions earn a durable place in retained memory: which observations become notes, which lessons become rules, and which conventions get written down. The obvious criterion is absence. Project decisions, local conventions, and facts postdating training are unavailable from the model's weights, so they must be stored somewhere.

Absence is a real reason, but taken as *the* criterion it ranks the wrong set. Since [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), retained support can also help when the consumer can produce a conclusion on request but does not reliably raise and apply it unprompted. The [separation of generation, activation, and selection failure](./weakly-discriminated-qualities-tend-to-be-underselected.md) matters because those diagnoses call for different interventions.

A conclusion has no activation value in isolation. That value belongs to a package comprising the conclusion, its delivery path, the consumer, and the occasions on which it should change behavior. The promotion question is whether retaining and delivering the conclusion will increase the probability that it is *applied on its occasion*.

Absence and activation are not competing scalar scores. Absence asks whether storage is necessary for availability; activation asks whether a delivery intervention can close an application gap. When content is absent, baseline application may be zero, but storing it still does not determine how it will reach its occasion.

## The two criteria rank candidates differently

| | Absence criterion | Activation criterion |
|---|---|---|
| Promotes for this reason | content that would otherwise be unavailable | support expected to improve unprompted application |
| Supplies no marginal value when | the content is already available | application already fires reliably, however obscure the conclusion |
| Value measured as | availability gained through storage | expected behavioral improvement, weighted by what rides on the occasion, less delivery cost |
| Model-upgrade implication | storage may become unnecessary once the content becomes available | support retires only when the application gap or the package's net value also falls |

The criteria diverge at both ends. A conclusion the consumer endorses when stated but never raises first has little absence value and potentially high activation value. This is the expert-witness case: the model answers the question asked but does not raise the concern nobody asked about. Conversely, an unavailable fact whose lookup already fires reliably has storage value but no additional activation value. The fact must exist somewhere, but its delivery problem is already solved.

That yields a difference someone could observe. An absence theory predicts that a model upgrade retires retained material once the model can produce the content. An activation theory makes no such prediction from produce-on-request capability alone: the material should retire only if unprompted application also improves, or if the delivery package no longer earns its cost.

This distinction sharpens rather than replaces the existing cost test. [Promotion is already gated on future value exceeding maintenance cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md), with retrieval and activation named together as sources of value. An open-versus-probed performance gap can estimate the activation value available to capture, as in [maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md). Whether promotion captures that value must be judged over the implemented content-and-delivery package.

## The promoted artifact inherits the problem it was promoted to solve

When promotion is justified by an activation gap, the promoted artifact must itself be activated. A note read only when the consumer already has the topic in mind reproduces the original failure one level up: the consumer must remember to remember. Following the delivery dependencies backward produces the **activation regress**.

The regress cannot terminate in another [retained artifact](./definitions/retained-artifact.md), a durable, addressable stored item. An instruction to consult an index, search first, or recall a convention still depends on retained content being raised. The chain terminates only when it reaches a mechanism whose firing does not itself depend on recalling another retained artifact: [content loaded unconditionally every session](./always-loaded-context-mechanisms-in-agent-harnesses.md), discovery that scans descriptions unbidden, an event-fired hook, a validator invoked by the build, a naming convention interpreted by code, or a human who invokes the procedure. These are instances of the broader [menu for firing behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md).

Externality here is causal, not informational. A description scanner, event classifier, or LLM-judged cue must still recognize the occasion. Moving that judgment outside the artifact chain does not eliminate false negatives, false positives, or maintenance. It ends only the regress in which activation depends on recalling another retained artifact. Selectivity, application, and net value must still be tested at the package level.

Chains are not the problem; unterminated chains are. A note reached through a tag index and a routing table can terminate in a harness that always loads the routing table. What fails is a path whose firing is explained only by another retained artifact, whether the path remains open or loops back on itself.

**A retained conclusion's trigger is therefore load-bearing, not metadata.** Promotion for activation is incomplete until the trigger is named and shown to terminate outside the retained-artifact chain. Every artifact creates maintenance cost, and loading or indexing it also consumes context or routing capacity. Without an external terminator, the available activation value remains unrealized except through explicit requests or incidental retrieval.

This is an observed failure mode, not merely a theoretical possibility. A [comparative review of agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) finds that most surveyed systems push memory into context, usually through coarse always-loading, while almost none test whether the injected memory changes behavior.

### A disposition can terminate the regress without making the path engineered

A trained disposition can also terminate the regress. A model that reliably searches the repository before editing supplies a trigger that is not itself a durable, addressable retained artifact.

The difference is control. An author can set the conditions for a harness, hook, or build step and observe when it fails. The author can observe the effects of a disposition but cannot directly set or inspect its firing conditions. Both can terminate the causal regress; only the mechanical path is engineered.

## The resulting promotion test

1. Is there an occasion on which this conclusion would change what gets done?
2. On that occasion, what is the baseline gap between produce-on-request capability and unprompted application? If application is already reliable, activation supplies no marginal reason to retain the conclusion; exactness, provenance, coordination, or unavailable content may still supply a storage reason.
3. What delivery path puts the artifact on that occasion, and what outside the retained-artifact chain makes that path fire? If nothing does, build a terminator or treat the activation value as unavailable.
4. Does the implemented content-and-delivery package improve behavior enough to exceed its maintenance, retrieval, context, and error costs? [Evaluate memory by effects, not existence](./agent-memory-requirements/evaluate-memory-by-effects.md).

Steps 1 and 2 identify the opportunity that activation support might capture. Step 3 supplies the termination condition. Step 4 tests whether the complete intervention captures enough value to justify its cost. Passing step 2 but failing step 3 does not make every effect impossible — explicit requests and incidental retrieval can still work — but it leaves the identified activation gap without a reliable delivery path.

Delivery is a different gate from [validity and learning value](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) and [a statable applicability boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md). Those gates ask whether the conclusion deserves retention in principle. Delivery asks whether the intervention can reach the occasion on which that conclusion matters. A candidate can clear every content gate while having no path to use.

## Scope

Absence remains a genuine storage reason. No trigger can conjure a decision made last week or a local convention that was never retained. Absence asks whether content must be stored; activation asks whether a retained-and-delivered package improves application. Neither test replaces the other.

Externality is necessary for terminating the recall regress, not sufficient for value. A stale index can fire perfectly and route to nothing. It is [worse than no index](./stale-indexes-are-worse-than-no-indexes.md) when satisfying the navigation cue suppresses a fallback search that would have worked.

Termination can also be priced out. Unconditional loading is reliable but costly, and a shared terminator has finite capacity. [ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) retired always-loaded generated indexes when their unconditional cost grew with the collection. A path can therefore terminate correctly and still fail step 4.

Building a trigger is not always feasible. [Symbolic routing can react only after a usable symbol exists](./symbolic-context-engineering-is-bounded-by-symbol-availability.md), so an occasion that nothing in the workflow names requires a costlier always-loaded slot or a probabilistic classifier. Failure to find a viable package is a legitimate outcome, not a defect in the candidate conclusion.

Measurement remains the weak point. Activation reliability is difficult to estimate in advance. Evidence usually comes from recorded misses or repeated open-versus-probed trials, so the method presupposes [a channel that records misses](./diagnostic-richness-constrains-outer-loop-learning-quality.md). Without one, activation-based selection degrades into guessing which conclusions the consumer is unlikely to raise.

## Open Questions

- What is the cheapest instrument that estimates an activation gap for a candidate conclusion *before* promotion rather than after an observed miss?
- Is trigger externality binary or graded? Harness-level description scanning is external to the artifact chain and still probabilistic, which suggests the ladder measures a continuum rather than a threshold.
- When many artifacts share one external terminator — a single always-loaded routing file — does that terminator's capacity become the binding constraint on how much a KB can usefully retain?

---

Relevant Notes:

- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: supplies the storage/context/activation separation the selection criterion is defined over
- [weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — grounds: the generation/activation/selection trichotomy that makes "the model lacks it" an inadequate default diagnosis
- [Promote only when future value exceeds maintenance cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — extends: splits that note's combined "retrieval or activation value" term and adds the trigger check as a promotion obligation
- [Activate behavior-changing memory before the mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) — mechanism: the catalogue of firing methods this note argues must be selected from at promotion time
- [symbolic context engineering is bounded by symbol availability](./symbolic-context-engineering-is-bounded-by-symbol-availability.md) — grounds: the availability limit that can make "build a trigger" unavailable and force a decline
- [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — evidenced-by: a trigger that fires reliably and still destroys value, bounding externality to necessary rather than sufficient
- [retained artifact](./definitions/retained-artifact.md) — defined-in: the artifact class whose chain the regress runs through
- [choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — extends: adds delivery as a third gate, structurally different from both content gates
- [diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: the general result behind why a missing miss-recording channel degrades activation-based selection
- [elicitation requires maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md) — mechanism: open-versus-probed performance estimates the activation gap the promotion package could capture
- [Evaluate Memory By Effects, Not By Existence](./agent-memory-requirements/evaluate-memory-by-effects.md) — grounds: evaluates the retained content and delivery mechanism by their behavioral effect as one package
- [only explicit retention is durable, writable, and addressable](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: why a parametric disposition's firing conditions sit outside author control
