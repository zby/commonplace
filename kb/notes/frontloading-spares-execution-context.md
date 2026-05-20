---
description: Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs
type: kb/types/note.md
traits: [has-external-sources]
tags: []
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, parts of the instructions whose inputs are known before the LLM runs can be computed beforehand and the result inserted directly. This spares execution context — the primary bottleneck in LLM-based systems — when the pre-step removes work the LLM would otherwise repeat. The stopping rule below distinguishes the cases worth frontloading from candidates that look frontloadable but shouldn't be.

## The context saving

[Context is the central scarce resource in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). Frontloading addresses the complexity dimension of that scarcity: executing a procedure inside an LLM call costs more context than inserting its result. The procedure text itself may be small — "search for X in `kb/notes/`" is a single line — but execution generates artifacts that persist in the context window: tool calls, search results, reasoning traces, interpretation. All of that competes with the work that actually needs the LLM's judgment. A pre-computed listing costs only the bytes of the listing itself; the same listing produced at runtime costs the instruction, the tool call, the full output, and the LLM's interpretation of it — on every invocation.

The saving extends beyond procedure execution to **discovery avoidance**. When values like paths, endpoints, or configuration are pre-resolved, the agent never spends tokens determining them at runtime — no searching, no trial-and-error, no asking the user. The resolution can happen entirely outside the agent: at installation time, build time, or session start. This is the most basic form of frontloading — replacing what the agent would have to figure out with what is already known.

## What qualifies for frontloading

The test: can this be computed without the LLM's runtime state (the conversation, the user's query, the evolving task)?

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Aggregations — counts, summaries of known datasets, pre-computed indexes
- Template expansion — [build-time generation](./generate-instructions-at-build-time.md) of skills and instructions

Anything that depends on the consuming call's runtime state — the user's current request, the conversation state, the evolving task — is dynamic relative to that call and not frontloadable into it. But static and dynamic are relative to the consumer, not absolute, and frontloading happens along a gradient of scopes. At broader scopes (build-time, install-time, session-start), pre-computed results frontload economically — the same work would otherwise be repeated across many calls. At narrower scopes — a parent agent computing instructions for a sub-agent it spawns — the parent's judgment is dynamic for itself but static for the sub-agent, and frontloading it is often constitutive rather than economic: without it, the sub-agent's [effective context](./effective-context-is-task-relative-and-complexity-relative-not-a.md) wouldn't fit the operation at all. Hybrid sub-procedures are common; frontload the known parts and leave the runtime-dependent parts as instructions.

A frontloaded artifact also needs a validity window. File listings, search results, resolved paths, and configuration are safe to insert only when their inputs remain stable for the consuming LLM call, or when the artifact carries enough [lineage](./definitions/lineage.md), timestamp, or regeneration instruction for a scheduler or callee to refresh it.

That test says when frontloading is possible. It does not by itself mean another frontloaded artifact is worth creating.

## Frontloading needs a stopping rule

Without a stopping rule, frontloading regresses: an ad hoc instruction can itself be prepared by another, until the system spends its context budget planning how to prepare the next LLM call instead of doing the semantic work. The practical rule:

> Frontload when the pre-step removes repeated discovery, runtime indirection, or task-specific ambiguity from a later LLM call. Do not frontload when the pre-step merely restates a stable skill contract already loaded by the callee.

## Frontloading vs codification

Frontloading can also be [constraining](./definitions/constraining.md) when it narrows the interpretations available to a later consumer. It becomes [codification](./definitions/codification.md) only when the pre-computed result is consumed by a symbolic artifact with formal semantics or assigned consequences, such as a schema, route table, validator input, or executable function. Deterministic prose generation by itself is frontloading and possibly constraining, but not automatically codification.

## Mechanism

The substitution is more precisely partial evaluation than divide-and-conquer because LLM context is a homoiconic medium — the pre-computed result re-enters the instruction stream as a residual program in the same medium. See [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) for the developed argument, the PE concept table, and where the analogy stretches.

## Relationship to the scheduling model

The [symbolic scheduling model](./bounded-context-orchestration-model.md) models frontloading as the single-step case of its separation between symbolic computation and LLM calls: pre-compute what can be known, reserve the LLM call for what requires judgment.

---

Relevant Notes:

- [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is frontloading and constraining; it becomes codification only when a formal mechanism consumes the resolved value
- [Generate KB skills at build time, don't parameterise them](./generate-instructions-at-build-time.md) — overlaps: template expansion frontloads setup work and may codify generated fields when downstream tooling assigns them consequences
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: frontloading addresses the complexity dimension of context scarcity
- [Effective context is task-relative and complexity-relative](./effective-context-is-task-relative-and-complexity-relative-not-a.md) — grounds: at narrow scopes, frontloading is constitutive rather than economic because effective context, not raw context window, is the binding constraint
- [Ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — application: ad hoc instruction artifacts frontload caller judgment at a clean context boundary, but should not merely duplicate stable skill contracts
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) — mechanism: the theoretical framing for why pre-compute-and-insert is precise, not metaphorical, in a homoiconic medium
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — models: frontloading is the single-step case of the scheduling model's separation between symbolic computation and LLM calls
