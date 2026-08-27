---
description: Explains why retrieval measures and storage-substrate labels cannot proxy for task-relative quality across discovery, loading, transformation, activation, and upkeep
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, context-engineering]
---

# Knowledge-access architecture must be evaluated end to end, not by retrieval alone

For a specified task, knowledge-access architecture must be evaluated across the path from identifying candidate material to producing and sustaining the outcome being evaluated. That path includes finding relevant material, constructing a usable task-facing context, turning inputs into the requested result, getting the material to affect the agent's behavior, and keeping the access route current. Each boundary can fail separately. Success at one therefore does not establish success at another.

A retrieval evaluation observes a particular event or property, such as candidate coverage, ordering, a relevance decision, payload return, or read-back. None alone establishes that the returned material stays within the amount of context the task can use reliably, supports the required transformation, changes the agent's behavior, improves the outcome being evaluated, or stays valid as the knowledge base changes. A storage substrate likewise shapes available operations and their costs, but is not itself an outcome measure.

## Discovery is not a task-facing context

Stored material becomes a candidate only when the consumer can identify it as relevant through an affordable route and a sufficiently discriminating cue. This is the task-relative discoverability requirement in [agent memory needs discoverable, composable, trusted knowledge under a context budget](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md), while [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) explains why the cue must justify the cost of following it. Storage can therefore succeed while candidate discovery fails.

Discovery can also succeed while loading or composition fails. The remembered-knowledge tests linked above separate these properties. A discovered artifact can lack a decision-relevant representation that fits without displacing more valuable task material. A fitting representation can still lack the scope, relationships, or conditions that it needs to combine with task context. Separately, a provider can accept more text than the model can use reliably for the task because [performance can degrade before the hard context-window cap](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md). Nor is delivery enough. The same selected material can support different results when it is framed around a different relation to test or resolve, so [selection and framing cannot generally be evaluated independently](./bounded-context-orchestration-model.md).

## Access is not the requested result

Even affordable, well-framed material can leave required work undone. [Access burden and transformation burden are distinct](./access-burden-and-transformation-burden-are-distinct-query-dimensions.md): locating inputs can be easy while deriving an explanation, judgment, synthesis, or other accepted result remains hard. The two burdens are relative to the current evidence, available operators and representations, and the conditions that make an answer acceptable. They can also alternate when transformation exposes another evidence need.

Presence in context is a further checkpoint, not proof of use. [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md): retained material can be read back without changing which information the agent selects, which plan or check it produces, which output it gives, or which action it takes. A behavioral change, in turn, does not by itself establish improvement in the downstream outcome. Evaluation must therefore name whether it claims exposure, uptake, an action, a validated artifact, or task success, and observe that outcome rather than substitute an upstream event for it.

## Upkeep is part of access

A route that works once may not keep working. Fixed pointers can drift when their targets change, while query-time pointers depend on their producing machinery remaining available and accurate, as described in [pointer design tradeoffs in progressive disclosure](./pointer-design-tradeoffs-in-progressive-disclosure.md). An index can become misleading when source membership changes and the index's apparent completeness suppresses a fallback search; that conditional failure is developed in [indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md). Views whose inputs have already been reconciled have their own refresh boundary because [evolving understanding can require holistic rewrite](./evolving-understanding-needs-holistic-rewrite-not-composition.md).

These mechanisms make maintenance part of [context engineering](./definitions/context-engineering.md)—getting the right knowledge into a bounded context at the right time and keeping that route healthy—not aftercare. A design may reduce work in the consuming call by assigning relevance judgment, reconciliation, or checking to an author or another runtime process, but it then depends on that work remaining current and available. The improvement must be evaluated together with the burden and dependency it introduces.

## Compare remaining burdens, not substrate names

A storage choice matters through the operations it makes available for the task and the burdens that remain around those operations. Its label does not specify how the surrounding architecture routes, loads, frames, transforms, activates, or maintains knowledge.

Before comparing designs, fix the task, consumer or model, evidence state, available operators and representations, amount of context the task can use reliably, conditions that make an answer acceptable, and outcome being evaluated. Then ask:

- What relevant candidate coverage does the design realize, and at what navigation or decision cost?
- Can the selected material be loaded and framed within the amount of context this task can use reliably?
- What transformation or reconciliation remains, including any further access that the work reveals?
- Does the material change behavior in the intended direction, and does the named downstream outcome improve?
- What authoring, checking, regeneration, and refresh work keeps the route and representation valid?

Interpret each question's importance relative to the named task and outcome. Exact lookup can leave little transformation, while synthesis can be dominated by reconciliation and context feasibility. Keeping the diagnostics separate shows which burden a design reduces and which ones remain without inventing a total score.

## Scope

This is an architectural synthesis of established component distinctions, not a directly tested end-to-end empirical result. Its checkpoints are a non-exhaustive diagnostic: they can recur or overlap, and maintenance conditions several of them rather than forming the last step of a linear pipeline. The note supplies no aggregate score, universal stage weights, or evidence about which failure usually dominates. It also supplies no validated benchmark for agent pointer decisions, causal instrumentation for activation, or maintenance-adjusted cost comparison. Where a task requires calibrated reliance, trust remains an additional condition of usable knowledge rather than a mandatory sixth stage.

---

Relevant Notes:

- [A context-operation interface bounds the projections its policy can realize](./context-operation-interface-bounds-context-policy.md) — mechanism: formalizes how available operators and compositions bound the task-facing views an access architecture can construct
