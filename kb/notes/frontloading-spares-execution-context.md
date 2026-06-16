---
description: Pre-computing known instruction inputs and inserting their results spares execution-context budget inside a later LLM call
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, frontloading means computing instruction inputs whose values are already known before the consuming call, then inserting the result directly. Because [context is the central scarce resource in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), frontloading spares execution context: it keeps the prompt, tool-output, interpretation, reasoning, and follow-up-call budget for work whose result is not already available.

## The context saving

Doing a procedure inside an LLM call costs more context than inserting its result. The procedure text itself may be small: "search for X in `kb/notes/`" is a single line. Carrying it out can still produce tool calls, search results, reasoning traces, interpretation work, and sometimes additional LLM calls whose outputs then occupy the context window. All of that competes with the call's real task, and the cost recurs on every invocation.

The comparison that matters is the *realized* execution context, not the instruction's size. A pointer can be shorter than the result yet cost more: "read file X" is one line, but executing it pulls the whole of file X into the window. So frontloading's saving is largest on the operation and complexity dimensions — the discovery, derivation, and indirection the call no longer performs. On raw volume it saves only when the inserted result is *smaller* than the material it replaces; inlining content the call would have loaded anyway only defers those tokens, it does not remove them — and a pointer that gets followed regardless is just [indirection](./indirection-is-costly-in-llm-instructions.md).

The saving matters before any hard token limit is reached. Frontloading can be constitutive because it shapes what fits in a consuming call's effective context: without the pre-step, the call may become less reliable through missed instructions, shallow reasoning, stale material treated as live, or budget spent interpreting setup. This follows from the broader point that [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). Frontloading is also economic when one build-time, install-time, or session-start computation saves many runtime calls from repeating the same work.

Discovery avoidance is the practical version of the same pattern. Pre-resolving paths, endpoints, or configuration means the agent never spends runtime context determining them. The resolution happens outside the consuming call, replacing what the agent would otherwise have to figure out with what is already known.

## What to frontload

The basic test is whether the value is known before the consuming call runs.

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Aggregations — counts, summaries of known datasets, pre-computed indexes
- Template expansion — [build-time generation](./generate-instructions-at-build-time.md) of skills and instructions
- Caller-resolved inputs — what a parent agent has discovered, decided, or framed at runtime, packaged into instructions for a sub-agent that doesn't see the parent's conversation

What counts as known-before-the-call depends on the consumer. State that is dynamic for a parent agent's LLM can be static for a sub-agent it spawns, because the parent can package its judgment as a self-contained instruction. Hybrid sub-procedures are common: frontload the known parts and instruct the rest.

A frontloaded artifact also needs a validity window: the span during which its pre-computed inputs remain accurate. If inputs may change before the consuming call, include enough [lineage](./definitions/lineage.md) (what it depends on, and when it must be regenerated), timestamp, or regeneration instruction for refresh.

Possibility is not enough, and context saving is not the only cost in play. Frontload when the pre-step removes repeated discovery, runtime indirection, or task-specific ambiguity from a later LLM call. Stop when the pre-step merely restates a stable skill contract — an interface the callee already has loaded. Stop, too, when [the value is one the executor would be better placed to choose](./fix-what-the-executor-cant-determine-not-what-it-will.md): freezing a situation-dependent detail can save context and still be wrong, because it commits a guess the executor could have read off the live state. Saving context and forfeiting that runtime advantage are two pulls in the same decision.

## Frontloading vs codification

Frontloading can also be [constraining](./definitions/constraining.md) when it narrows the interpretations available to a later consumer. It becomes [codification](./definitions/codification.md) when the result is consumed by a symbolic artifact with formal semantics or assigned consequences, such as a schema, route table, validator input, or executable function. Deterministic prose generation, by itself, is frontloading without being codification.

## Mechanism

The most common realization is inlining: the pre-computed result is substituted directly into the instruction stream. See [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) for a more theoretical discussion of the mechanism. At the architecture level, the [symbolic scheduling model](./bounded-context-orchestration-model.md) treats frontloading as the single-step case of its separation between symbolic computation and LLM calls: pre-compute what can be known, reserve the LLM call for what requires judgment.

---

Relevant Notes:

- [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is frontloading and constraining; it becomes codification only when a formal mechanism consumes the resolved value
- [Generate KB skills at build time, don't parameterise them](./generate-instructions-at-build-time.md) — overlaps: template expansion frontloads setup work and may codify generated fields when downstream tooling assigns them consequences
- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: frontloading avoids degradation across volume, complexity, and interference rather than only avoiding hard token overflow
- [Ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — application: ad hoc instruction artifacts frontload caller judgment at a clean context boundary, but should not merely duplicate stable skill contracts
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) — mechanism: the theoretical framing for why pre-compute-and-insert is precise, not metaphorical, in a homoiconic medium
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: a second cost the frontload-or-not decision must weigh — freezing a situation-dependent value forfeits the executor's runtime advantage even when it saves context
