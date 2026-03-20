---
description: Shows how a framework-owned tool loop can recover branching, recursive decomposition, and state projection by moving the control stack into a singleton runtime/tool instead of application code
type: note
traits: []
tags: [computational-model, context-engineering]
status: seedling
---

# A framework-owned tool loop can simulate explicit orchestration by externalizing control state

The claim that frameworks should expose the loop becomes sharper if the opposing case is stated in its strongest form. A framework-owned tool loop does **not** eliminate the ability to express richer control. If tool calls are general programming actions, then the loop can recover much of that expressivity by moving control state out of the visible application layer and into a singleton runtime or stateful tool.

This note sketches that construction.

## The basic move

Start with the normal framework-owned loop:

```python
messages = [task_prompt]

while True:
    response = llm_call(messages, tools=tools)
    if response.has_tool_calls():
        results = execute_tools(response.tool_calls)
        messages.append(assistant_message(response))
        messages.append(tool_results(results))
    else:
        return response
```

Now add one distinguished tool that owns orchestration state:

```python
class ControlRuntime:
    def __init__(self):
        self.task_stack = []
        self.branches = {}
        self.checkpoints = {}
        self.budgets = {}
        self.trace = []

    def handle(self, command, payload):
        ...

control_runtime = ControlRuntime()
tools = ordinary_tools + [control_runtime_tool(control_runtime)]
```

Instead of keeping recursion state, branch state, retry counters, and projection policy in application code, the system stores them inside `control_runtime`. The model can then call that tool to create subgoals, suspend work, resume parents, checkpoint state, prune context, or ask which task should run next.

The application still sees a single framework-owned tool loop. The richer control structure has been pushed behind the tool boundary.

## Two kinds of recovered control

This construction works best when we distinguish two different kinds of intervention.

The first kind is **dispatch-side control**. These interventions can happen around tool execution without changing the tool vocabulary the model sees:

- logging and observability
- approvals and budget checks
- retry counters and checkpointing
- stack bookkeeping
- projection or summarization of returned state
- deterministic transforms on tool results

These can often be hidden from the model entirely. The runtime can wrap ordinary tools, intercept calls, mutate hidden state, and rewrite results before they are fed back into the framework-owned loop.

The second kind is **capability-surface control**. These interventions change what actions are available to the next bounded call:

- adding a new synthetic tool
- removing tools that are irrelevant or unsafe in a subtask
- narrowing the tool set per child task
- changing the stop condition or return protocol for a particular subgoal

This second class is much harder to hide. Once orchestration needs to mutate the available capability surface, the system is no longer just wrapping execution. It is deciding what action alphabet the next model step may act over.

## What the singleton runtime can hold

The singleton runtime can encode most of the control structures that seem to require loop ownership:

- a **recursion stack** of parent and child tasks
- a **task tree** for recursive decomposition
- **branch records** for alternative framings or alternative solution paths
- **retry counts** and policy state
- **budgets** for tokens, time, tools, or money
- **checkpoints** for partial outputs and resumability
- **projection rules** that decide which parts of prior state should be surfaced next
- **approval flags** and deferred work queues

At that point the framework-owned loop is still linear at the surface level, but each iteration can consult and mutate a much richer external control state.

## How interventions can be encoded

The interventions discussed in the other notes can all be re-expressed through this runtime.

**State projection.** The model calls `control_runtime.project(...)`, which returns only the selected subset or summary of prior state that should be reintroduced into the next turn.

**Branching.** The model calls `control_runtime.fork(...)` to create multiple candidate branches, then later calls `control_runtime.merge(...)` or `control_runtime.compare(...)` to reconcile them.

**Fresh context.** The runtime can keep canonical state outside the conversation and return a compact restatement instead of the full raw trace, giving the next turn a pseudo-fresh view of the task.

**Retry with altered framing.** The runtime can remember prior failures and surface an alternate prompt fragment or control instruction for the next attempt.

**Deterministic interleaving.** The runtime can perform ranking, filtering, aggregation, serialization, or budget checks in ordinary code before handing something back to the model.

**Observability and approvals.** The runtime can log every step, mark runs as degraded, block continuation pending approval, or emit status artifacts for operators.

None of this requires the visible application layer to own the loop directly. The control logic lives in the singleton runtime and is accessed through tool calls.

Many of these moves can also be made invisible to the model. Instead of asking the model to call an explicit control tool, the runtime can wrap ordinary tools and treat each call as a trigger for hidden bookkeeping. From that angle, the dependency on "the model must remember to call the extra orchestration tool" is weaker than it first appears.

## How recursive decomposition can be encoded

Recursive decomposition can be expressed the same way. The model asks the runtime to create child tasks, push them onto a stack, and later resume the parent:

```python
control_runtime.handle("push_subtasks", {
    "parent": current_task,
    "children": subtasks,
})

next_task = control_runtime.handle("next_task", {})
context = control_runtime.handle("project_for_task", {"task": next_task})
```

Inside the runtime, ordinary code can maintain:

- the stack or queue of pending tasks
- parent/child relationships
- partial results per subtask
- merge conditions for returning to the parent
- policies for depth limits, breadth limits, and early stopping

From the framework's point of view, nothing special happened. The tool loop remained linear: the model called a tool, got a result, and continued. But the tool it called was effectively a hidden scheduler.

This is also where the construction starts to strain. Recursive decomposition often wants more than hidden stack state. Child tasks frequently need different prompts, different stop conditions, and different tool sets. A research child may need `{search, summarize}` while a coding child needs `{read_file, patch_file, run_test}`. A merge step may need a synthetic tool like `submit_subresult` or `resume_parent`.

That is a capability-surface change, not just hidden bookkeeping. If the framework-owned loop keeps one fixed tool set, the runtime has only awkward options:

- keep one giant static tool set and simulate scoping through prompt instructions
- add a generic meta-tool that multiplexes all child-task actions through one controller
- or force a fresh bounded call outside the loop so application code can choose a new tool surface

The first leaks irrelevant affordances into every step. The second turns the controller tool into the real runtime. The third is already a partial escape from framework-owned progression. So decomposition is the clearest place where "the hidden scheduler in a tool" stops feeling like a clean recovery and starts revealing the underlying control problem.

## The constructive conclusion

This construction matters because it blocks a weak version of the "expose the loop" argument. It is not enough to say that a framework-owned tool loop cannot express branching, recursive decomposition, or richer state management. In practice it often can, provided the tool surface is general enough and some singleton runtime is allowed to hold the hidden control state.

So the real dispute is not about bare expressibility. It is about where the scheduler lives, how directly it can be programmed, and what costs appear once orchestration is recovered through a stateful tool rather than exposed as an application-level control surface.

That further analysis belongs in a separate note. This note only establishes the constructive possibility.

---

Relevant Notes:

- [anatomy of an LLM application](./anatomy-of-an-llm-application.md) — setup: this note answers the strongest counterposition to the tool-loop-first decomposition
- [llm frameworks should keep the tool loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md) — target: sharpens the argument by ruling out the naive claim that hidden loops simply cannot express richer control
- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — background: the hidden runtime/tool effectively becomes a scheduler over bounded calls
- [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — next step: the question becomes what degrades when the scheduler is recovered through the tool loop rather than exposed directly
