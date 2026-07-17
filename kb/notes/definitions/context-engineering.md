---
description: Definition — context engineering is the discipline of designing systems around bounded-context constraints; its operational core is routing, loading, scoping, and maintenance for each bounded call
type: kb/types/definition.md
tags: [computational-model]
---

# Context engineering

Context engineering is the architectural discipline of designing systems around bounded-context computation. It asks how the right knowledge reaches the right bounded call at the right time, and how knowledge survives, changes, or stays out across call boundaries.

The immediate problem is prompt assembly, but the scope is wider: storage shape, routing surfaces, loading rules, scoping boundaries, compaction, and workshop/library lifecycle all determine what can become live context.

## Scope

Use the term context engineering when the design question is about routing, loading, scoping, or maintaining knowledge under bounded context. This includes single-call prompt construction and upstream structures that make useful loading possible.

The operational core decomposes into four components within a single bounded call:

**Routing** — deciding what knowledge is relevant before loading it. Examples include the [instruction-specificity/loading-frequency match](../instruction-specificity-should-match-loading-frequency.md), [CLAUDE.md as a router](../agents-md-should-be-organized-as-a-control-plane.md), and [retrieval-oriented descriptions](../agents-navigate-by-deciding-what-to-read-next.md) that let agents reject a target without loading it.

**Loading** — assembling and framing the prompt from selected knowledge. The `select` function in the [bounded-context orchestration model](../bounded-context-orchestration-model.md) formalizes this: given state and a token budget, build a prompt that fits. Framing matters because the same knowledge can have different [extractable value](../information-value-is-observer-relative.md) under different presentations.

**Scoping** — isolating what each consumer sees. [Sub-agents as lexically scoped frames](../llm-context-is-composed-without-scoping.md) is the main local example: flat context has no scope, so architecture must impose it.

**Maintenance** — keeping loaded context healthy over time. Compaction, observation masking, and the [workshop layer's](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) holistic-rewrite discipline prevent accumulated debris from [degrading reasoning](../context-efficiency-is-the-central-design-concern-in-agent-systems.md).

Reshaping recorded knowledge for a specific task and context budget — producing derived views, summaries, and handoff artifacts — is the main operation these components perform, but not the only one. The [bounded-context orchestration model](../bounded-context-orchestration-model.md) formalizes the machinery as a `solve` loop where a symbolic scheduler drives routing, loading, and scoping for each bounded LLM call.

## Architectural scope beyond a single call

The operational core depends on decisions made before and after prompt assembly:

**Storage format** — knowledge stored in forms that are cheap to retrieve selectively. Notes, descriptions, and indexes determine whether routing can happen before full loading.

**Knowledge lifecycle** — how raw interaction becomes reusable knowledge and how that knowledge is curated. A KB that only accumulates transcripts has already failed the context problem upstream.

**Session boundaries** — whether a system inherits transcript history by default or treats each call as a fresh assembly problem. [Session history should not be the default next context](../session-history-should-not-be-the-default-next-context.md) is context engineering at the boundary level.

**Inter-agent communication** — when sub-agents return compressed artifacts instead of full transcripts, the boundary itself becomes a context-engineering primitive. Execution boundaries are natural sites for producing derived handoff artifacts.

**Tool and interface design** — tool descriptions, instruction surfaces, and generated interfaces consume context budget too. [Frontloading](../frontloading-spares-execution-context.md) shifts interpretive cost out of the live context window.

A system with poor storage shape, transcript-oriented boundaries, or verbose tool surfaces cannot be rescued by a clever selector alone.

## Exclusions

Context engineering is not changing the model itself. Fine-tuning, RL, embedding-model improvement, and model architecture changes alter model behavior or representations, not the bounded context assembled for a call.

Context engineering is not the task work itself. Domain reasoning, feature implementation, command execution, and content authoring are outside the term unless they change what knowledge enters context, how it is framed, or which consumer sees it.

Context engineering is not observability. Observability can inform context-engineering changes, but it is a feedback surface, not a context operation.

## Misuse Cases

- Reducing context engineering to one mechanism, such as prompt writing, retrieval, or a larger context window. The term names the architecture around bounded context, not any single tactic.

---

Relevant Notes:

- [context efficiency is the central design concern](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: if bounded context is the governing cost model, context engineering must be architectural rather than local to prompt assembly
- [bounded-context orchestration model](../bounded-context-orchestration-model.md) — formalisation: the select/call loop that structures context engineering decisions
- [instruction specificity should match loading frequency](../instruction-specificity-should-match-loading-frequency.md) — mechanism: the routing hierarchy (always-loaded → on-demand)
- [LLM context is composed without scoping](../llm-context-is-composed-without-scoping.md) — mechanism: sub-agents as the scoping component
- [agents navigate by deciding what to read next](../agents-navigate-by-deciding-what-to-read-next.md) — mechanism: routing through retrieval-oriented descriptions
- [session history should not be the default next context](../session-history-should-not-be-the-default-next-context.md) — extends: session-boundary design determines whether context is inherited as transcript or reassembled per call
- [frontloading spares execution context](../frontloading-spares-execution-context.md) — extends: interface and instruction design can move interpretive cost out of the live context window
- [legal drafting solves the same problem as context engineering](../legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallel: law's centuries of methodology for the same problem
- [in-context learning presupposes context engineering](../in-context-learning-presupposes-context-engineering.md) — extends: in-context learning only works when context engineering has selected the right knowledge; this makes context engineering a prerequisite, not just an optimization
- [a functioning KB needs a workshop layer not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: knowledge lifecycle and artifact shape are upstream determinants of what later becomes cheap to load
- [agent runtimes decompose into scheduler context engine and execution substrate](../agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — component view: the runtime's context engine is the operational core inside the broader architectural discipline named here
