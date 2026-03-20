---
description: Framework-owned tool loops package the common model/tool/retry pattern well, but strong frameworks keep the loop optional so applications can control state projection, branching, and re-entry
type: note
traits: []
tags: [computational-model]
status: seedling
---

# LLM frameworks should keep the tool loop optional

A normal tool-using LLM application has a simple shape. The application defines some tools, gives the model a task, and runs a loop: the model either answers directly or asks for a tool; the runtime executes the tool call, appends the result, and asks again until some stop condition is met.

```python
state = initial_task()

while True:
    turn = llm_call(state, tools=tools)
    if turn.type == "tool_request":
        result = run_tool(turn.request)
        state = absorb(state, turn.request, result)
        continue
    return turn.output
```

This pattern exists for a good reason. It is a convenient packaging of the common case where the application wants open-ended local progress: let the model decide whether to search again, inspect another file, call a helper, or stop. The framework factors out repetitive mechanics such as tool schema handling, tool-result reinjection, and session continuity. For exploratory assistants, operator consoles, and "keep going until you can answer" workflows, that convenience is real.

That is exactly why frameworks tend to build a **framework-owned tool loop**. The mistake is not that such a loop exists. The mistake is when the loop becomes the only first-class control surface.

The strongest version of the old argument is false: a framework-owned loop does **not** literally prevent the application programmer from writing an outer loop around LLM calls. The programmer can always drop to a lower-level SDK, wrap the framework in a coarser loop, or push more orchestration into prompts and stateful tools. So the real question is not prohibition. It is **what the framework makes directly programmable without escaping the abstraction**.

That distinction matters because many important control decisions belong to the application rather than to the convenience runtime:

- stop after a tool result and project only selected state into a fresh prompt
- branch into several bounded calls and merge them later
- retry with a different framing instead of continuing the same session
- interleave deterministic transforms, ranking, filtering, or checkpointing between semantic calls
- enforce budgets, human approvals, or observability checkpoints between iterations

Once those moves matter, the application no longer wants "please continue the session until done" as its primitive. It wants bounded semantic calls plus explicit state progression. If the framework exposes tools only through its hidden loop, the application has to fight the abstraction: smuggle scheduler state through prompts, hide control inside tools, or abandon the framework layer that made tools convenient in the first place.

This is why the issue is not raw computability. A sufficiently capable escape hatch usually recovers that. The issue is that hidden tool loops make hybrid `tool -> program -> tool -> program -> llm` control flow non-first-class at the layer where the application actually wants to express it. The framework's convenience runtime quietly becomes the owner of recursion depth, re-entry policy, history inheritance, and intermediate state shape.

That ownership also pushes the system toward the [LLM-mediated scheduler](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md). Instead of using the model for bounded semantic judgments inside an application-owned loop, the stack asks the model and the framework session to jointly simulate the scheduler. That is convenient at first, but it spends scarce bounded context on bookkeeping and makes [session history the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) even when selective state projection would be the better control move.

So "keep the tool loop optional" is the practical version of "expose the loop." It does **not** mean every user should hand-write `while True`. It means a strong framework stack has layers:

- a base bounded-call interface that can return semantic outputs or tool requests
- explicit hooks where application code can inspect results and decide whether to continue
- higher-level tool loops and agent sessions as convenience layers on top, not as the only way to get tools

When the stack is shaped that way, the framework still serves the common case well. Most users can stay in the convenience loop. But once orchestration becomes mechanical, cost-sensitive, reliability-sensitive, or tightly coupled to application state, the programmer can peel back one layer without losing access to the same tools and call surfaces. That is the real architectural requirement.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — foundation: the clean architecture is still a symbolic scheduler driving bounded semantic calls, even when some calls return tool requests
- [tool loop](../../notes/tool-loop-index.md) — prior framing: argues from expressivity loss; this draft restarts from why tool loops are a useful convenience layer in the first place
- [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: hidden tool loops push bookkeeping and progression back into the bounded conversational medium
- [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) — extends: once the framework owns progression it also tends to decide what later calls inherit
- [apparent success is an unreliable health signal in framework-owned tool loops](../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — consequence: framework ownership of the loop also makes failure handling and degraded execution less visible to the application
