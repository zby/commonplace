---
description: Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs
type: kb/types/note.md
traits: [has-external-sources]
tags: []
status: seedling
---

# Frontloading spares execution context

When instructing LLMs, parts of the instructions whose inputs are known before the LLM runs can be computed beforehand and the result inserted directly. This spares execution context (the prompt-and-reasoning budget inside a single call) — a primary bottleneck in LLM-based systems.

## The context saving

[Context is the central scarce resource in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), and executing a procedure inside an LLM call costs more context than inserting its result. The procedure text itself may be small — "search for X in `kb/notes/`" is a single line — but execution generates artifacts that persist in the context window: tool calls, search results, reasoning traces, interpretation. All of that competes with the work that needs the LLM's judgment, and the cost recurs on every invocation.

The saving extends to **discovery avoidance**: pre-resolving values like paths, endpoints, or configuration means the agent never spends tokens determining them at runtime. The resolution happens outside the agent — at installation, build, or session start — replacing what the agent would otherwise have to figure out with what is already known.

## The constitutive case

The most important argument for frontloading is **constitutive**: it shapes what fits in a consuming call's [effective context](./effective-context-is-task-relative-and-complexity-relative-not-a.md). Without it, operations that would otherwise overflow the bound don't happen — most starkly when a parent agent hands work to a sub-agent with no access to the parent's conversation, but also whenever discovery at runtime would cost more context than the consumer can spare for it.

In some cases, frontloading also has an **economic** benefit: when the pre-computation happens once at build-time, install-time, or session-start, the savings accumulate across many runtime calls that would otherwise redo the work. Broad scope amplifies this benefit, but the constitutive case is the load-bearing reason for the operation.

## What qualifies

The test: is this known before the consuming call runs?

**Static (frontloadable):**
- Variable resolution — paths, project names, configuration values known at setup time (the [indirection elimination](./indirection-is-costly-in-llm-instructions.md) case)
- File listings — "here are the files in `kb/notes/`" rather than "list the files in `kb/notes/`"
- Aggregations — counts, summaries of known datasets, pre-computed indexes
- Template expansion — [build-time generation](./generate-instructions-at-build-time.md) of skills and instructions
- Caller-resolved inputs — what a parent agent has discovered, decided, or framed at runtime, packaged into instructions for a sub-agent that doesn't see the parent's conversation

What counts as known-before-the-call depends on the consumer. State that is dynamic for a parent agent's LLM can be static for a sub-agent it spawns, since the parent can package its judgment as a self-contained instruction. Hybrid sub-procedures are common — frontload the known parts, instruct the rest.

A frontloaded artifact also needs a validity window — the span during which its pre-computed inputs remain accurate. When the inputs may change before the consuming call, the artifact must carry enough [lineage](./definitions/lineage.md) (what it depends on, and when it must be regenerated), timestamp, or regeneration instruction for a scheduler or callee to refresh it.

The test says when frontloading is possible. It does not by itself mean another frontloaded artifact is worth creating.

## Frontloading needs a stopping rule

Without a stopping rule, frontloading regresses: an ad hoc instruction can itself be prepared by another, until the system spends its context budget planning how to prepare the next LLM call instead of doing the semantic work. The practical rule:

> Frontload when the pre-step removes repeated discovery, runtime indirection, or task-specific ambiguity from a later LLM call. Do not frontload when the pre-step merely restates a stable skill contract already loaded by the callee.

## Frontloading vs codification

Frontloading can also be [constraining](./definitions/constraining.md) when it narrows the interpretations available to a later consumer, and [codification](./definitions/codification.md) when the result is consumed by a symbolic artifact with formal semantics or assigned consequences — schema, route table, validator input, executable function. Deterministic prose generation, by itself, is frontloading without being codification.

## Mechanism

The most common realization is inlining — the pre-computed result substituted directly into the instruction stream. See [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) for why this is more precisely partial evaluation than divide-and-conquer in a homoiconic medium. At the architecture level, the [symbolic scheduling model](./bounded-context-orchestration-model.md) treats frontloading as the single-step case of its separation between symbolic computation and LLM calls: pre-compute what can be known, reserve the LLM call for what requires judgment.

---

Relevant Notes:

- [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — overlaps: variable resolution is frontloading and constraining; it becomes codification only when a formal mechanism consumes the resolved value
- [Generate KB skills at build time, don't parameterise them](./generate-instructions-at-build-time.md) — overlaps: template expansion frontloads setup work and may codify generated fields when downstream tooling assigns them consequences
- [Effective context is task-relative and complexity-relative](./effective-context-is-task-relative-and-complexity-relative-not-a.md) — grounds: at narrow scopes, frontloading is constitutive rather than economic because effective context, not raw context window, is the binding constraint
- [Ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — application: ad hoc instruction artifacts frontload caller judgment at a clean context boundary, but should not merely duplicate stable skill contracts
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — motivates: the context loading hierarchy is one response to execution context being the bottleneck
- [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) — mechanism: the theoretical framing for why pre-compute-and-insert is precise, not metaphorical, in a homoiconic medium
