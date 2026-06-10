---
description: Index for the tool-loop argument — the framework-owned tool loop is useful but should yield control when tasks need different tool surfaces, exceed one context window, or codify scheduling
type: kb/types/tag-readme.md
index_source: tag
index_key: tool-loop
tags: [computational-model, context-engineering, tool-loop]
status: current
---

# Tool loop

Many LLM applications share a common operational core: construct a task frame, give the model tools, and loop until it stops.

```
state = initial_task_frame()

while not done(state):
    turn = llm_call(state, tools=tools)
    if turn.type == "tool_request":
        result = execute_tool(turn.request)
        state = absorb(state, turn.request, result)
    else:
        state = absorb(state, turn.output)
```

Frameworks own this loop because the mechanics are repetitive protocol work — parsing tool requests, dispatching to handlers, serializing results, feeding them back, handling streaming and retries. Abstracting that away is good engineering, just as abstracting HTTP parsing is. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md) this loop is `select` frozen to a single policy — append the result, re-ask with the same tools — owned by the framework rather than the application. [Keeping that loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md) is the design stance these notes argue for.

Many useful interventions can stay hidden inside this loop without changing its structure: logging, approvals, budget checks, checkpoints, deterministic transforms on tool results. A [stateful singleton runtime](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) behind the tool boundary can go further, holding recursion state and branch records. The recovery is genuine — but the question is not whether the loop can absorb bookkeeping. It is who gets to decide what the next step *can do*.

## Forcing cases

Three cases where a single framework-owned loop becomes insufficient:

- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) — decomposition creates children that need different capability surfaces; the parent must construct fresh calls with different tool sets, which a fixed loop cannot express
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — some sub-goals require deterministic orchestration over smaller semantic judgments because the material doesn't fit in one bounded call
- [codified scheduling patterns can turn tools into hidden schedulers](./codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md) — as next-step policies stabilize into code, hiding them in tools collapses orchestration into covert runtime logic

## Resolution

The first and third cases call for **[sub-agents](./agent-is-a-tool-loop.md)** — fresh tool loops with their own prompt, capability surface, and stop condition. The second calls for something more: **symbolic composition** of agents — code-controlled iteration, filtering, and aggregation over multiple agent invocations. Sub-agents are the atomic unit; symbolic orchestration is what the application does with them.

The framework's job is therefore to [**keep the tool loop optional**](./llm-frameworks-should-keep-the-tool-loop-optional.md): run the frozen loop for the common case, but expose the bounded call beneath it so application code can spawn child loops and compose them. The mechanism is small — [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md): demote the loop to a returning, per-call-parameterized `agent()` call (plus one tool-execution hook), and ordinary host-language control flow becomes `select` while its variables hold `K`. ("Expose the loop" was the earlier name for this same move.) A further question, once orchestrators are written this way, is what to retain across runs: [run-state stays ephemeral while recurring strategies are the promotion target](./orchestration-strategies-and-run-state-have-opposite-persistence.md).

## Downstream consequences

- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — sub-tasks should start with constructed prompts, not inherit the parent's full conversation
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) — when the framework owns recovery, the parent cannot distinguish intended-path success from workaround success
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — applies the fallback/recovery problem to memory extraction: successful runs can still teach the system about broken primary paths and degraded guarantees
- [traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover.md) — programmers expect broken infrastructure to fail loudly; semantic recovery violates that, creating false confidence
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — the same observability problem for ambiguous specs rather than broken tools

- [conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — once sub-agents exist, the parent must choose how results come back: trace preservation, compression, or context forking

## Related approaches

- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — boundary case: the model writes an ephemeral symbolic orchestrator that composes agents via `recursive_llm()` — the loop is exposed to the model rather than the programmer, but discarded after each run

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: each sub-agent is a bounded call with its own `select(K)` in the scheduling model
- [llm-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: workarounds for hidden loops push scheduling into the conversational medium
- ["agent" is a tool loop](./agent-is-a-tool-loop.md) — convention: grounds the sub-agent mechanism by equating "agent" with "tool loop"
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — broader context: the tool loop is one dimension; scheduler placement, persistence, coordination form, and return artifacts vary independently
