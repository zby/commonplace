---
description: "Why the expressiveness argument between state machines and programs is empty, which control structure each representation shows natively versus encodes as data, and how that decides whether a workflow reads better as a chart or as code"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [computational-model]
---

# Statecharts and programs differ in what they show, not in what they can compute

Two arguments about how to represent a workflow talk past each other. One says state machines compute less than programs. The other says a statechart is more readable than the equivalent conditionals. Neither decides the choice between them. A statechart pairs drawn states and transitions with variables and arbitrary actions, so it computes whatever its host language computes. A program can hold a state variable and dispatch on it. Each representation can encode the other. They differ in which control structure each shows natively, drawn or written where a reader recovers it, and which it encodes, kept in variables where the reader no longer sees it. The choice therefore follows the control structure that dominates the workflow. Steps that run to completion, with recursion, data-dependent fan-out or plans produced at run time, read better as a program. Reactive control over a fixed finite set of states, where the question is what each state does on each event, reads better as a chart.

## The expressiveness argument is empty

A finite-state machine in the strict sense cannot do what a pushdown automaton does. Adding one stack lets a machine recognize languages that are not regular. That comparison concerns unbounded machines, and practical computers are finite. Every program on a finite computer is a finite-state machine over its whole memory. A statechart as David Harel defined it pairs its drawn states with variables (its extended state), guards and actions. The actions are arbitrary code. So a statechart runtime computes whatever its host language computes, and a program can carry an explicit state variable and dispatch on it. The two sides have equal computational power, so the useful comparison is what each representation makes visible.

The [conversion lemma](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md) is this encoding made deliberately. It stores the stack, pending work and control position as explicit state `K` so that any barrier-delimited program becomes one select/call loop. The lemma states why that is useful: it determines the LLM-call projection for analysis. It also states that the source program may stay in its natural form. The loop is the analytic state machine, and the program is what someone reads.

## What each representation shows natively

| Control structure | Statechart | Program |
|---|---|---|
| Which events each state handles, and what each does | native: every transition out of a state is visible together | encoded: a state variable plus a dispatch over events |
| Run one step to completion, then the next | encoded: one state per step plus a done event | native: statement order |
| Recursion with resumption | encoded: a stack of frames in the chart's variables; nesting depth is fixed at design time | native: the call stack |
| Fan-out whose width is decided by data | encoded: a counter or collection in the chart's variables; orthogonal regions are fixed in number | native: a comprehension over the data plus a join |
| Control structure produced at run time, such as a plan | encoded: the chart becomes an interpreter inside one state | native: execute the plan |

Each encoded cell has the same shape. The control flow moves into variables, and the drawn or written structure no longer shows it.

## Encoding in either direction hides the control structure

Take a recursive planner:

```python
async def solve(task):
    if is_leaf(task):
        return await llm(task)
    subtasks = await llm_plan(task)                        # width decided at run time
    results = await gather(*[solve(t) for t in subtasks])  # dynamic fan-out, unbounded depth
    return await llm_merge(task, results)
```

A statechart for this has three states (planning, waiting on children, merging) plus a stack of frames in its variables. The frames hold the task, the pending children and the collected results. The chart is a three-node loop. The recursion and the fan-out are hidden in the frame stack. The function shows both.

The same chart-direction encoding explains a common difficulty with event-based modelling of sequential work. When a workflow is a sequence of steps that wait on results, modelling it as event handlers makes the author maintain the continuation by hand. Which step comes next and what was pending are kept in variables, split across handlers. That is the call stack stored as data by hand, without the language's help. Coroutines and async/await remove this cost: they store the continuation as data automatically, so code that waits on events can still be written in statement order. The per-state event table stays encoded, so they remove the cost of the chart-direction encoding only.

The reverse encoding is the challenge "show me your statechart as conditionals". A reactive controller with a dozen states and a handful of events becomes a state variable and nested dispatch. Every transition is still present, but the reader can no longer see all exits from one state together. In the table a missing case is a blank cell; in the dispatch it surfaces at run time.

## Choosing by the dominant structure

Run-to-completion workflows with recursion, data-dependent width or plans produced at run time read better as programs. Reactive control with a fixed finite state set, where the question is what happens on each event in each state, reads better as a chart. An agent system can contain both, for example a finite lifecycle such as queued, running, completed and failed around a sequential job. The lifecycle suits a chart and the job suits a program. Writing either in the other's representation produces the encodings above.

This is the same boundary the [bounded-context orchestration model](./bounded-context-orchestration-model.md) sets on its own scope. Barriered run-to-completion calls fit the select/call form. Streaming interaction and independently mutable environments need an event-driven extension. This note adds that the readable representation changes at that boundary.

## Scope

- Readability here means that a reader recovers the control structure from the representation. A finite chart has a second value this note does not assess: model checking and exhaustive transition testing need the finite part explicit, which can justify a chart where a program would read better.
- Statechart runtimes with dynamic actor spawning can express recursion and data-dependent fan-out. The control flow then lives in the actor system, so the chart no longer shows it.
- The claim concerns the choice of representation. It does not rank the architectures the representations describe.

## Open Questions

- Is any representation native to both structures? Structured concurrency and process calculi support both sequencing and event handling. Whether either reads well for both is untested here.
- Graph-based agent frameworks appear to have added dynamic fan-out and subgraph constructs after starting from fixed graphs. If confirmed, that is the encoding cost being paid in practice.

---

Relevant Notes:

- [Any barrier-delimited symbolic program with LLM calls is a batched select/call program](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — mechanism: stores control as explicit state deliberately, for analysis; the source program stays the form a reader reads
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — contrasts: its run-to-completion boundary is where the readable representation also changes
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — exemplifies: the graph-DSL versus imperative-scheduler comparison is one instance of this choice
