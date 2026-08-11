---
description: "Recasts promotion from 'the consumer lacks this' to 'the consumer will not apply this unprompted', and requires delivery to have a root firing event independent of that prior activation"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [agent-memory, context-engineering, failure-modes]
---

# Promotion selects for unreliable activation, and the regress ends only at an external trigger

A **promotion theory** decides which candidate conclusions earn a durable place in retained memory: which observations become notes, which lessons become rules, and which conventions get written down. The obvious promotion criterion is absence. Project decisions, local conventions, and facts that postdate training are unavailable from the model's weights, so they must be stored somewhere.

Absence is a real reason to retain content, but as *the* criterion it ranks the wrong set. As [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), retained support can also help when a consumer can produce a conclusion on request but does not reliably raise and apply it unprompted. The [separation of generation, activation, and selection failure](./weakly-discriminated-qualities-tend-to-be-underselected.md) matters because each failure calls for a different intervention.

A conclusion has no activation value in isolation. That value belongs to a package: the conclusion, its delivery path, the consumer, and the occasions on which applying it should change the consumer's behavior. The relevant promotion question is therefore whether retaining and delivering the conclusion will make it more likely to be *applied on its occasion*.

Absence and activation are not competing scalar scores. Absence asks whether storage is necessary for availability. Activation asks whether a delivery intervention can close an application gap. When content is absent, baseline application may be zero, but storing it still does not determine how it will reach the occasion on which it matters.

## The two criteria rank candidates differently

| | Absence criterion | Activation criterion |
|---|---|---|
| Promotes for this reason | content that would otherwise be unavailable | support expected to improve unprompted application |
| Supplies no marginal value when | the content is already available | application already fires reliably, however obscure the conclusion |
| Value measured as | availability gained through storage | expected behavioral improvement, weighted by what rides on the occasion, less delivery cost |
| Model-upgrade implication | storage may become unnecessary once the content becomes available | support retires only when the application gap closes or the package's net value falls |

The criteria diverge at both ends. A conclusion that the consumer can produce when explicitly asked, but never raises first, has little absence value and potentially high activation value. This is the expert-witness case: the model answers the question asked but does not raise the concern nobody asked about. Conversely, an unavailable fact whose lookup already fires reliably has storage value but no additional activation value. A model upgrade therefore removes the storage rationale when it supplies missing content, but removes activation support only when unprompted application also improves or the delivery package no longer earns its cost.

This distinction sharpens the existing cost test rather than replacing it. [Promotion is already gated on future value exceeding maintenance cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md), with retrieval and activation named together as sources of value. An open-versus-probed performance gap—the difference between unprompted performance and performance after the relevant concern is explicitly raised—can estimate the activation value available to capture, as in [maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md). Whether promotion actually captures that value must be judged over the implemented content-and-delivery package.

## The promoted artifact inherits the activation dependency

When promotion is justified by an activation gap, the promoted artifact still needs a delivery path. A note reached only after the consumer independently surfaces the same concern does not close the gap: its delivery depends on the very condition it was meant to supply. Following these dependencies backward produces the **activation regress**.

[Retained-artifact](./definitions/retained-artifact.md) status does not stop the regress. A validator, always-loaded routing table, or trained disposition may itself be retained state. The relevant question is what makes its behavior fire on the occasion.

The delivery path can be represented as a graph of activation dependencies. A path remains unrooted when every step fires only after the consumer has already surfaced the target conclusion or the next routing instruction. It becomes rooted when a live event causes an evaluator, runtime, or human to act without that prior activation. Examples include [content loaded unconditionally at the start of every session](./always-loaded-context-mechanisms-in-agent-harnesses.md), discovery that scans descriptions without being requested, an event-fired hook, a validator invoked by the build, a naming convention interpreted by code, or a human invoking a procedure. These are instances of the broader [menu for firing behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md).

Externality here is causal and relative to the activation dependency, not informational or substrate-based. A description scanner, event classifier, or LLM-judged cue must still recognize the occasion. Rooting the path does not eliminate false negatives, false positives, or maintenance costs; selectivity, application, and net value must still be tested at the package level.

Chains are not the problem; unrooted chains are. A note reached through a tag index and routing table can work if a session-start event loads the routing table. What fails is a path intended to support unprompted application when every firing edge still depends on the consumer independently surfacing the topic or route.

**A retained conclusion's trigger is therefore load-bearing, not metadata.** Before effects have been measured, activation-based promotion needs both a plausible root firing event and an account of why that event should recognize the occasion. Direct package-level evidence can establish that the gap is closed even when the internal path is difficult to inspect. Without either a rooted path or evidence of effects, the claimed activation value remains unrealized except through explicit requests or incidental retrieval.

A [comparative review of agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) finds that most surveyed systems push memory into context, usually through coarse always-loading, while almost none test whether the injected memory changes behavior. This observation does not by itself diagnose an unrooted chain. It shows instead why presence or injection alone cannot establish activation value.

### A disposition can root the path without making it engineered

A trained disposition can also supply the root firing edge. A model that responds to an editing task by reliably searching the repository need not first have the missing conclusion active. The learned numerical state carrying this disposition may itself be a retained artifact; the live task cue is what makes its behavior fire.

The difference is control. An author can set the firing conditions for a harness, hook, or build step and observe failures of that mechanism. The author can observe a disposition's effects but cannot directly set or inspect its firing conditions. Both can root the activation path; only the mechanical path is engineered.

## The resulting promotion test

1. Is there an occasion on which this conclusion would change what gets done?
2. On that occasion, what is the baseline gap between produce-on-request capability and unprompted application? If application is already reliable, activation supplies no marginal reason to retain the conclusion; exactness, provenance, coordination, or unavailable content may still supply a storage reason.
3. What delivery path puts the artifact on that occasion, and what live event makes the path fire without the conclusion or its next routing instruction already being active? If no such root is available, explicit requests and incidental retrieval may still work, but the identified unprompted-application gap remains unaddressed unless direct package testing already shows otherwise.
4. Does the implemented content-and-delivery package improve behavior enough to exceed its maintenance, retrieval, context, and error costs? [Evaluate memory by effects, not existence](./agent-memory-requirements/evaluate-memory-by-effects.md).

Delivery is a different gate from [validity and learning value](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) and [a statable applicability boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md). Those gates ask whether the conclusion deserves retention in principle. Delivery asks whether the intervention can reach the occasion on which the conclusion matters. A candidate can clear every content gate while still lacking a path to use.

## Scope

Rooting is necessary for an intended unprompted delivery path, but it is not sufficient for value. A stale index can fire perfectly and route to nothing. It is [worse than no index](./stale-indexes-are-worse-than-no-indexes.md) when satisfying the navigation cue suppresses a fallback search that would have worked.

Termination can also be priced out. Unconditional loading is reliable but costly, and a shared terminator has finite capacity. [ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) retired always-loaded generated indexes when their unconditional cost grew with the collection. A path can therefore terminate correctly and still fail step 4.

Building a trigger is not always feasible. [Rule-based selection can react only after a distinguishing signal exists](./rule-based-context-selection-needs-a-pre-existing-signal.md), so an occasion that nothing in the workflow names forces a choice between a costlier always-loaded slot and a probabilistic classifier. These are not two ways to remove the recognition judgment but two places to put it: the always-loaded slot loads a bounded superset and leaves recognition to the consumer's own in-context attention; the classifier makes the recognition call out of band, sparing that context at the cost of a separate evaluation. Only a rule-ready signal — a live event that itself distinguishes the occasion — removes the judgment instead of relocating it. A consumer that surfaces the concern on its own is nearly free because it performs this recognition inside its own reasoning; a promoted delivery path exists precisely for the occasions where it will not.

The `curl`/`wget` lesson shows the fork concretely. A hook on the `curl` invocation is a rule-ready signal that fires deterministically; a network-issues FAQ loaded into every session is the always-loaded slot; a side model scanning the transcript for network trouble is the classifier. Only the hook escapes a semantic recognition call.

Causal independence and recognition are separate axes: a fallback can root its path yet still misread the occasion. Failure to find a viable package is then a legitimate outcome, not a defect in the candidate conclusion.

Measurement remains the weak point because activation reliability is difficult to estimate in advance. Evidence can come from recorded operational misses or controlled open-versus-probed trials. [A channel that records misses](./diagnostic-richness-constrains-outer-loop-learning-quality.md) enables learning from failures during normal operation; planned trials can generate measurements without such a channel. Without either source, activation-based selection degrades into guessing which conclusions the consumer is unlikely to raise.

## Open Questions

- What is the cheapest instrument that estimates an activation gap for a candidate conclusion *before* promotion rather than after an observed miss?
- What minimum evidence distinguishes a genuine root firing edge from model behavior that happens to retrieve the conclusion during a test?
- When many artifacts share one external terminator—a single always-loaded routing file—does that terminator's capacity become the binding constraint on how much a KB can usefully retain?

---

Relevant Notes:

- [Only explicit retention is durable, writable, and addressable](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: why a parametric disposition's firing conditions sit outside author control
