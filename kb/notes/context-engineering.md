---
description: Definition — context engineering is the discipline of designing systems around bounded-context constraints; its operational core is routing, loading, scoping, and maintenance for each bounded call
type: note
traits: []
tags: [computational-model]
status: seedling
---

# Context engineering

Context engineering is the architectural discipline of designing systems around bounded-context computation. The immediate problem is getting the right knowledge into a bounded context at the right time, but the scope is wider than prompt assembly. If context is the governing constraint, the structures that determine what can be loaded, when, and what survives across boundaries also belong to context engineering.

Anthropic defines it as "strategies for curating and maintaining the optimal set of tokens during LLM inference" ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). This KB's treatment is consistent with that operational view but broader in architectural scope, because [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md): when bounded context is the scarce resource, whole-system structure must be designed around it.

The operational core decomposes into four components within a single bounded call:

**Routing** — deciding what knowledge is relevant before loading it. The [instruction-specificity/loading-frequency match](./instruction-specificity-should-match-loading-frequency.md) (always-loaded → on-reference → on-invoke → on-demand) is routing. [CLAUDE.md as a router](./agents-md-should-be-organized-as-a-control-plane.md) is routing. [Retrieval-oriented descriptions](./agents-navigate-by-deciding-what-to-read-next.md) that let agents decide "don't follow this" without loading the target are routing.

**Loading** — assembling the prompt from selected knowledge. The `select` function in the [bounded-context orchestration model](./bounded-context-orchestration-model.md) formalizes this: given state `K` and budget `M`, build prompt `P` with `|P| ≤ M`. Loading includes both what to include and how to frame it — the same knowledge under different framing has different [extractable value](./information-value-is-observer-relative.md).

**Scoping** — isolating what each consumer sees. [Sub-agents as lexically scoped frames](./llm-context-is-composed-without-scoping.md) is scoping. The flat context has no scoping; architecture must impose it.

**Maintenance** — keeping loaded context healthy over time. Compaction, observation masking, and the [workshop layer's](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) holistic-rewrite discipline are maintenance. Without maintenance, context accumulates debris that [degrades reasoning](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) even when token counts are low.

[Distillation](./distillation.md) — compressing knowledge for a specific task under a context budget — is the main operation these components perform, but not the only one. The [bounded-context orchestration model](./bounded-context-orchestration-model.md) formalizes the machinery: the `solve` loop where a symbolic scheduler drives routing, loading, and scoping decisions for each bounded LLM call.

## Architectural scope beyond a single call

The operational core succeeds or fails based on decisions made before and after prompt assembly:

**Storage format** — knowledge stored in forms that are cheap to retrieve selectively. Notes, descriptions, and indexes are context-engineering structures because they determine whether routing can happen before full loading.

**Knowledge lifecycle** — how raw interaction becomes reusable knowledge and how that knowledge is curated over time. A KB that only accumulates transcripts has already failed the context problem upstream.

**Session boundaries** — a system can inherit transcript history by default or treat each call as a fresh assembly problem. [Session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) is context engineering at the boundary level, not just the prompt level.

**Inter-agent communication** — when sub-agents return compressed artifacts instead of full transcripts, the boundary itself becomes a context-engineering primitive. Execution boundaries are natural sites for [distillation](./distillation.md).

**Tool and interface design** — tool descriptions, instruction surfaces, and generated interfaces consume context budget too. [Frontloading](./frontloading-spares-execution-context.md) and build-time generation shift interpretive cost out of the live context window.

A system with poor storage shape, transcript-oriented boundaries, or verbose tool surfaces cannot be rescued by a clever selector alone.

---

Relevant Notes:

- [distillation](./distillation.md) — the main operation context engineering performs: compressing knowledge for a task under a budget
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: if bounded context is the governing cost model, context engineering must be architectural rather than local to prompt assembly
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — formalisation: the select/call loop that structures context engineering decisions
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — mechanism: the routing hierarchy (always-loaded → on-demand)
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agents as the scoping component
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: routing through retrieval-oriented descriptions
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — extends: session-boundary design determines whether context is inherited as transcript or reassembled per call
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — extends: interface and instruction design can move interpretive cost out of the live context window
- [legal drafting solves the same problem as context engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallel: law's centuries of methodology for the same problem
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning only works when context engineering has selected the right knowledge; this makes context engineering a prerequisite, not just an optimization
- [a functioning KB needs a workshop layer not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: knowledge lifecycle and artifact shape are upstream determinants of what later becomes cheap to load
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — component view: the runtime's context engine is the operational core inside the broader architectural discipline named here
