---
type: kb/types/note.md
description: Explains why improving context selection within a fixed operation interface cannot establish that the interface admits every useful active-context projection.
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [context-engineering, computational-model, agent-memory]
---

# A context-operation interface bounds the projections its policy can realize

Retained state and active context are different runtime layers. Here, the retained substrate is projectable state available outside a bounded model input; retained controller state is tracked separately when it selects projections but is not itself projected into that input. Active context is what one bounded invocation actually receives. This follows the broader separation between [state retention and context assembly](./agent-runtime-analysis-should-separate-scheduling-context-state.md). A **context-operation interface** is the operations and permitted compositions through which a controller locates, materializes, transforms, and exposes retained state as active context. Its addressable units and exposure boundary are part of the interface. A controller or context policy chooses whether, when, and how to use that interface; it may be the receiving model, a learned controller, a host or proxy, or a mixed arrangement. Holding the retained substrate, model, and resource budget fixed, the interface bounds the projections that policy can realize.

Let `I` include the operation semantics, addressable units, composition rules, and the boundary where a view becomes model input. For retained state `S`, task and run signal `x`, fixed model or models `M`, and fixed budget `B`, define `Reach(I, S, x; M, B)` as the active-context views obtainable through legal interface traces. `B` includes the applicable active-context, model-call, time, and tool-use limits. A trace may locate, expand, transform, summarize, filter, delete, or expose retained material. It may also update retained state before exposure. “Projection” therefore means the task- and state-conditioned view delivered to the model, not a lossless or non-mutating mathematical projector. A required view lies outside `Reach` if producing it needs an unavailable operation, an unaddressable distinction, or a forbidden composition. In particular, [access and transformation impose distinct burdens](./access-burden-and-transformation-burden-are-distinct-query-dimensions.md): finding retained input does not imply that the interface can turn it into the view the call needs.

A policy selects legal traces, so it induces achieved coverage or a distribution within structural reach. A better policy may choose useful traces more often, sequence them more reliably, or reduce their cost. Those gains do not add a view outside `Reach`, nor do they show that excluded projections are unnecessary. This is the context-projection instance of the more general result that [learning inside a fixed decomposition inherits its omissions](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). If an intervention adds observations, external computation, tools, model capability, budget, or permission to change operation definitions, then a premise has changed. It is no longer only a better policy over the same interface.

## Architectural contrasts

Different composition languages make the interface variable concrete. A [practitioner account of recursive language models](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) describes model-authored programmatic exploration and transformation, with results exposed through printed output or a returned answer. The paper-described [lambda-RLM](../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) replaces arbitrary programs with a small typed combinator language. Paper-described [agentic context management](../sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md) fixes two memory operations and learns when to invoke or abstain from them. These interfaces permit different legal traces even though each constructs bounded model context. The comparison is between source-described architectures, not verified executions or a performance ranking.

Who selects a projection is a separate coordinate. In the RLM account the model selects its view; in agentic context management a learned controller chooses fixed operations. A host or proxy can instead assemble a view before the receiving model sees it, while a mixed push/pull arrangement can combine preloaded material with model-requested expansion. These placements can coexist with different operation vocabularies, so controller placement does not by itself determine structural reach. Within-run, cross-restart, and cross-task retained state instead describe how long prior state can condition selection. Changing a retained invocation policy is not by itself a change to operation semantics or composition rules.

## Evaluation consequence

An evaluation of controller improvement should report the retained substrate and addressable units; operation semantics and composition rules; controller placement and projection boundary; mutable policies or artifacts and their persistence horizon; model; and resource budget. It should identify which coordinates stayed fixed and which changed. Gains with one fixed operation set show that a policy was useful in the tested regime. They do not establish that excluded operations are unnecessary. Testing interface adequacy requires a rival operation/composition interface, another constraint-changing intervention, or an argument that projections excluded by the interface cannot improve the objective.

## Scope

Structural reach is not achieved use. Exact retained material can coexist with a lossy or missed active projection. A legal trace may never be discovered or produced reliably, and a delivered view may still fail to affect behavior. The claim here ends at exposure into active context; [storage, read-back, and contextual activation remain distinct](./knowledge-storage-does-not-imply-contextual-activation.md).

The claim does not rank interfaces. A restricted interface may trade admitted transformations for reliability, safety, inspectability, trainability, latency, or cost. An open-ended programming interface remains bounded by its primitives, sandbox, permitted compositions, model competence, and budget. The system contrasts show that these architecture coordinates vary across described systems. They do not estimate the causal performance effect of changing any one coordinate, and they leave open which interface is preferable under a given set of operational constraints.

---

Relevant Notes:

- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](./knowledge-access-architecture-must-be-evaluated-end-to-end.md) — extends: places structural projection reach inside the larger path from discovery through upkeep
- [Rule-based context selection needs a pre-existing signal](./rule-based-context-selection-needs-a-pre-existing-signal.md) — extends: characterizes when a fixed selector can choose a legal projection
- [RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) — extends: separates interface restriction from persistence horizon
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: explains why a fixed-interface evaluation cannot identify an unrun rival interface
- [Scroll](../agent-memory-systems/reviews/scroll.md) — evidenced-by: code-grounded mixed push/pull interface with structured and programmable recall
- [Virtual Context](../agent-memory-systems/reviews/virtual-context.md) — evidenced-by: code-grounded proxy-owned assembly and model paging over retained conversation state
