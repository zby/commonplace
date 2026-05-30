---
description: Navigation hub for tool-loop notes — the LLM-in-a-loop execution model, when one framework-owned loop is insufficient, how to keep it optional, and the downstream consequences
type: kb/types/index.md
index_source: tag
index_key: tool-loop
tags: [computational-model, context-engineering, tool-loop]
status: current
---

# Tool loop

Notes on the tool loop — the LLM-in-a-loop-with-tools execution model that frameworks package by default. This cluster argues the framework-owned loop should stay optional; use the groups below to move from the model to the forcing cases, the mechanism, and the consequences.

## The model

- [agent is a tool loop](./agent-is-a-tool-loop.md) — the convention: an LLM in a loop with tools and a stop condition, which makes a sub-agent a sub-loop
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — the formal substrate: the loop is `select` frozen to one policy

## The design stance

- [LLM frameworks should keep the tool loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md) — the central argument this cluster develops

## When one loop is insufficient

- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) — decomposition spawns children needing different capability surfaces
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — material that does not fit one bounded call needs deterministic orchestration
- [codified scheduling patterns can turn tools into hidden schedulers](./codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md) — stabilized next-step policy hidden in tools becomes covert runtime logic
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — a stateful runtime behind the tool boundary regains control but cannot be inspected or composed

## The mechanism

- [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) — demote the loop to a returning `agent()` call so ordinary control flow plays `select`
- [orchestration strategies and run-state have opposite persistence](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — what to retain across runs once orchestrators are written this way

## Downstream consequences

- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — sub-tasks should start from constructed prompts, not inherited conversation
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) — hidden recovery hides the intended-path/workaround distinction
- [traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover.md) — semantic recovery violates fail-loud expectations
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — the same observability gap for ambiguous specs rather than broken tools
- [conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — how results return once sub-agents exist
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — applies the fallback/recovery problem to memory extraction

## Related approaches

- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — the model authors the symbolic orchestrator in a REPL tool, discarded after each run

## Broader context

- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — tool-loop framework design is one axis among scheduler placement, persistence, coordination form, and return artifacts

## Related indexes

- [Computational model](./computational-model-index.md) — the bounded-call substrate the loop runs on
- [Context engineering](./context-engineering-index.md) — when scheduling inside the loop must become explicit
- [Observability](./observability-index.md) — why inspectable orchestration is a precondition for seeing how a run progressed

## Other tagged notes <!-- generated -->

- [The chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation.md) - Chat history persists because appending messages preserves information and avoids interface design, but that convenience trades away selective loading under bounded context
