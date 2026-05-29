---
description: Framework-owned tool loops package the common model/tool/retry pattern well, but strong frameworks keep the loop optional so applications can control state projection, branching, and re-entry
type: kb/types/note.md
traits: []
tags: [computational-model, tool-loop]
status: seedling
---

# LLM frameworks should keep the tool loop optional

A normal tool-using LLM application has a simple shape. It defines some tools, gives the model a task, and runs a loop: the model either answers directly or asks for a tool; the runtime executes the call, appends the result, and asks again until some stop condition is met.

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

This pattern exists for a good reason. It packages the common case where the application wants open-ended local progress: let the model decide whether to search again, inspect another file, call a helper, or stop. The framework factors out the repetitive mechanics — tool schema handling, tool-result reinjection, session continuity. For exploratory assistants, operator consoles, and "keep going until you can answer" workflows, that convenience is real.

That is exactly why frameworks tend to build a **framework-owned tool loop**. The mistake is not that the loop exists. The mistake is letting it become the only first-class control surface.

## The tool loop is a frozen `select`

In the [bounded-context orchestration model](./bounded-context-orchestration-model.md) the general shape is `while (P := select(K)) is not None: r = call(P); K = K + r`, where `select` assembles the next bounded prompt — including its tool surface and stop condition — from accumulated state `K`. The framework-owned tool loop is that loop with **`select` reified and frozen to a single policy: append the tool result to the running messages and re-ask with the same tools.**

This is the precise sense in which the loop is a convenience rather than a constraint on expressivity. The frozen policy is the right default for open-ended local progress, where "show the model everything so far and the same tools" is exactly what you want. But freezing `select` inside the framework means the framework, not the application, owns selection — what the next call sees, what it may do, and when to stop. "Keep the tool loop optional" is therefore the concrete form of **letting the application own `select`**: keep the frozen-`select` loop for the common case, but expose the underlying bounded call so application code can supply its own selection policy when one is needed.

The strongest version of the old argument is false: a framework-owned loop does **not** literally prevent the programmer from writing an outer loop around LLM calls. One can always drop to a lower-level SDK, wrap the framework in a coarser loop, or push orchestration into prompts and stateful tools. So the real question is not prohibition but **what the framework makes directly programmable without escaping the abstraction**.

That distinction matters because the control decisions an application needs fall into two classes, and the frozen loop blocks only one of them in a way no wrapper recovers cleanly.

The first class is **capability-surface changes** — moves that need a fresh call because they alter what the next call sees or may do:

- stop after a tool result and project only selected state into a fresh prompt
- branch into several bounded calls and merge them later
- retry with a different framing instead of continuing the same session

These are precisely the moves the frozen `select` forecloses: each one is a different selection policy, and the framework has fixed the policy to "same messages, same tools." Once any of them matters, the application no longer wants "please continue the session until done" as its primitive. It wants bounded semantic calls plus explicit state progression. If the framework exposes tools only through its hidden loop, the application has to fight the abstraction: smuggle scheduler state through prompts, hide control inside tools, or abandon the framework layer that made tools convenient in the first place.

The second class is **dispatch-side interventions** — moves that wrap a single call without changing what the next one may do:

- interleave deterministic transforms, ranking, filtering, or checkpointing around tool execution
- enforce budgets, log, or run observability checkpoints as calls execute

These do not require exposing the loop at all. A tool-execution hook can absorb them, because they operate inside one call rather than choosing the next one. Conflating them with the first class would overclaim — it would suggest every application concern demands loop exposure, when only the capability-surface changes do.

So the issue is not raw computability — a sufficiently capable escape hatch usually recovers that. The issue is that hidden tool loops make hybrid `tool -> program -> tool -> program -> llm` control flow non-first-class at the very layer where the application wants to express it. The convenience runtime quietly becomes the owner of recursion depth, re-entry policy, history inheritance, and intermediate state shape — the capability-surface decisions, not the dispatch-side ones.

That ownership also pushes the system toward the [LLM-mediated scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md). Instead of using the model for bounded semantic judgments inside an application-owned loop, the stack asks the model and the framework session to jointly simulate the scheduler. That is convenient at first, but it spends scarce bounded context on bookkeeping and makes [session history the default next context](./session-history-should-not-be-the-default-next-context.md) even when selective state projection would be the better control move.

So "keep the tool loop optional" is the practical version of "expose the loop" — and it does **not** mean every user should hand-write `while True`. The sharper form is to **make the loop a returning value and let the host language own `select` and `K`**. That resolves to a small practical surface: one returning, per-call-parameterized call primitive (with sub-agents as recursive calls), plus one tool-execution hook for the interventions that wrap a single call rather than change the next one. [The practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) develops that surface and argues why it is a better basis than a reified scheduler.

That hook is not a private invention of this argument. The [agent-harness survey](../sources/agent-harness-large-language-model-agents-survey.md) elevates **lifecycle hooks** — pre/post-invocation interception points — to a named, first-class component of its six-part harness definition, alongside the execution loop itself. This is independent convergence on the same mechanism: the place application code reclaims control is a hook around the call, not a rewrite of the loop.

The layering is also shippable in production, not just a design ideal. [iii](../sources/how-to-build-your-own-agent-harness-2060069083878408689.md) ships the turn loop as one swappable layer among ~13–15 others, each addressed through a uniform `trigger()` call over name-based function ids, so the loop can be replaced without disturbing its neighbours. That makes thin-vs-thick a **slider, not a fork**: a position on the "framework owns progression ⟷ application owns progression" axis becomes a reconfiguration rather than a one-time architectural commitment — exactly what "keep the loop optional" asks for.

Shaped this way, the framework still serves the common case well: most users can stay in the convenience loop. But once orchestration becomes mechanical, cost-sensitive, reliability-sensitive, or tightly coupled to application state, the programmer can peel back one layer without losing access to the same tools and call surfaces. That is the real architectural requirement.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the clean architecture is still a symbolic scheduler driving bounded semantic calls; the framework-owned loop is its `select` frozen to one policy
- [tool loop](./tool-loop-index.md) — prior framing: argues from expressivity loss; this draft restarts from why tool loops are a useful convenience layer in the first place
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: hidden tool loops push bookkeeping and progression back into the bounded conversational medium
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — extends: once the framework owns progression it also tends to decide what later calls inherit
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) — consequence: framework ownership of the loop also makes failure handling and degraded execution less visible to the application
- [Agent Harness for Large Language Model Agents: A Survey](../sources/agent-harness-large-language-model-agents-survey.md) — evidence: independently makes lifecycle hooks a first-class harness component, converging on the middle layer this note proposes
- [How to build your own agent harness (iii)](../sources/how-to-build-your-own-agent-harness-2060069083878408689.md) — evidence: production stack ships the loop as one swappable layer behind a uniform calling convention — thin-vs-thick as a slider, not a fork
- [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) — extends: sharpens "keep the loop optional" into a concrete minimal library surface (one returning primitive plus one hook) by declining to reify `select`/`K`
