---
description: Starts from the standard prompted-agent tool loop, showing that the real control boundary appears when applications need to change the capability surface for later steps
type: note
traits: []
tags: [computational-model, context-engineering]
status: seedling
---

# Anatomy of an LLM application

Many LLM applications share a common operational core once you strip away product-specific wrappers: some caller constructs a task frame, gives the model access to tools, and a loop runs until the model stops or the runtime stops it.

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

This is the standard **prompted-agent tool loop**. The task frame may come from a chat message, an API request, a queue job, a coding task runner, or an evaluation harness. The caller gives the model a prompt and a tool surface; the model decides whether to answer directly or request another action; the runtime executes the action and feeds the result back into the next step.

That pattern exists for a good reason. It is the natural packaging of the common case where the application wants the model to pursue a local objective with available tools: inspect more context, call a helper, try another search, write a file, run a command, stop when satisfied. Most of the mechanics are repetitive protocol work:

- parse tool requests
- dispatch to registered handlers
- serialize results
- feed results back in the right format
- handle streaming, retries, and tool-call bookkeeping

Frameworks own this loop because abstracting that machinery away is good engineering. The programmer usually does not want to rewrite tool protocol glue any more than they want to hand-roll HTTP parsing.

## Where framework ownership helps

For many applications, framework ownership of the tool loop is exactly right. If the desired behavior is "give the model a task, let it use tools until it can finish," then the loop is mostly an execution substrate concern rather than application logic.

This is true whether the application is interactive or not. A chat assistant, a background research worker, a code-repair harness, and a document-processing pipeline can all use the same tool loop even though only one of them is literally a chat product.

Chat is therefore just one wrapper around the pattern, not the architecture itself. A chat UI supplies successive task frames from user messages and often chooses conversation history as the carried state. That is a common instantiation, but not the general case.

## What does not really require loop control

Not every intervention in a tool loop is equally important.

Many useful controls can be hidden behind wrapped tool execution or hidden runtime state:

- logging and observability
- approvals and budget checks
- retry counters and checkpointing
- stack bookkeeping
- deterministic transforms on tool results
- projection or summarization of returned state

Those may still be awkward when buried inside a framework-owned runtime, but they do not by themselves force loop exposure. A sufficiently programmable wrapper can often intercept ordinary tool calls, mutate hidden state, and feed back transformed results without changing the visible structure of the tool loop.

So the decisive issue is not "can the runtime do bookkeeping between iterations?" It often can.

## Where framework ownership becomes a constraint

The real boundary appears when the application needs to change the **capability surface** for the next step — the set of tools or actions exposed to the model at that point.

At each model call, the system is not only deciding what state to show. It is also deciding what actions are available. In simple uses that tool set can stay fixed across the whole run. But richer orchestration often wants that surface to change as the task changes.

Typical cases:

- after decomposition, a research subtask should see `{search, summarize}` while a coding subtask should see `{read_file, patch_file, run_test}`
- a merge step should get synthesis-oriented tools rather than the tools used to produce child results
- a risky subtask should have a narrower tool set or stronger approval boundary
- a deeper recursive level may need synthetic capabilities like `submit_subresult`, `resume_parent`, or `request_more_context`
- a retry step may need a different action surface from the original step rather than just a different prompt

This is different from hidden bookkeeping. Logging, checkpointing, and budget accounting can wrap existing calls. Capability changes alter the **action alphabet** of the next bounded call — the next scoped LLM step with its own prompt and tool surface.

Once the capability surface must change, the application no longer wants a runtime that simply keeps looping over one fixed tool set. It wants to construct a fresh step with a new prompt, a new tool set, and often a new stop condition.

Recursive decomposition is the clearest example. A linear tool loop assumes one current thread of work and one stable action surface. Decomposition creates a stack or tree of tasks whose children often need different capabilities than the parent. The problem is not only where the recursion stack lives. It is that each level may need a different interface to the world.

A framework-owned tool loop can still simulate this by keeping one giant static tool set, or by routing everything through a meta-tool that hides the real scheduler — the code deciding what happens next — behind one generic action. But that is exactly where the abstraction starts to feel wrong. Either irrelevant affordances leak into every step, or one controller tool becomes the real runtime while the framework loop merely transports messages to it.

## Why the need for control grows over time

The capability-surface argument explains what you can't do with a hidden loop. But there is also a temporal dimension: the boundary between "needs LLM judgment" and "is now mechanical" shifts as the application matures.

Early in development, the model decides everything — what file to read, which tool to call next, when to retry, how to recover from errors. The tool loop is the right abstraction because these decisions genuinely require semantic judgment.

But after enough runs, patterns emerge. The model always runs tests after editing. When tests fail with a syntax error, the model always re-reads and fixes. After a successful test run, the model always formats the summary the same way. Each of these was once a judgment call — now it's a fixed pattern that the model re-discovers on every run, spending tokens on something deterministic.

These crystallized patterns are candidates for [codification](../../notes/codification.md) — moving from LLM judgment to code. The natural question is: where should the codified logic go?

**Many patterns can go into tools.** "Always format test output as a table" can be the tool's job. "Log every file read" is a tool wrapper. These don't require loop control — they're codification at the tool boundary, and frameworks handle them fine.

**But scheduling patterns can't go into tools without the tool becoming a hidden scheduler.** "After editing, run tests" is a sequencing decision — it's about *what to do next*, not *how to do any one thing*. Baking it into the edit tool conflates the tool's job (edit a file) with the orchestrator's job (decide what comes next). Worse, it's inflexible: sometimes you want to edit multiple files before running tests, or skip tests for a formatting change.

This is exactly the capability-surface problem in temporal form. The crystallized patterns that *matter* for loop control are scheduling patterns — decisions about what step comes next, with what tools, in what context. Those are the ones that can't cleanly go into tools, because they require constructing fresh bounded calls with different capability surfaces. Tool-level patterns codify just fine within the framework.

## The programmer's dilemma

The framework does not literally forbid any of this. The programmer can always bypass the framework-owned loop and write their own orchestration around direct LLM calls:

```
while not done:
    prompt = build_prompt(state)
    response = llm_call(prompt)
    state = update_state(state, response)
```

But that is a bad trade if the framework bundles tool infrastructure and loop ownership together. Once the programmer bypasses the loop, they may also lose the framework's tool dispatch, function-calling protocol handling, streaming, structured output parsing, retries, and whatever else the framework packaged into the same abstraction.

The programmer does not want to reimplement all of that. They want the framework's tool machinery with their own progression logic.

So the dilemma is not "frameworks forbid custom loops." It is: **use the framework and lose control of progression, or bypass the framework and lose the convenience that made the framework attractive**.

A well-designed framework resolves this by keeping the tool loop **optional**. It exposes tool execution, structured outputs, and bounded calls — single scoped LLM steps — as composable primitives, then offers a higher-level convenience loop on top rather than sealing everything inside one runtime-owned cycle.

## What the decomposition reveals

This tool-loop-first view makes several things visible:

**Tool registration and loop ownership are independent concerns.** A framework can provide tool dispatch, protocol handling, and structured output parsing without also owning the progression policy. These are bundled together by convention, not by necessity.

**Chat is one wrapper, not the essence.** The real recurring structure is the prompted-agent tool loop. Chat matters only as one way of sourcing task frames and one common default for carried state.

**The interesting architectural question is capability ownership.** Once the loop exists, the key design question is who decides what actions the next model step is allowed to take.

**The carried state is richer than a message list.** Real applications accumulate decompositions, rankings, retries, checkpoints, and partial products outside the conversation trace. But the sharper constraint is that different points in that state often imply different tool surfaces.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — foundation: the `select/call` loop this note's inner loop instantiates
- [tool loop](../../notes/tool-loop-index.md) — extends: argues for the framework design consequence of the dilemma identified here
- [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) — extends: the message-list-as-state default this note surfaces becomes a constraint when the framework owns progression
- [agent runtimes decompose into scheduler, context engine, and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — extends: the three-component decomposition that emerges when the inner loop is factored properly
- [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: what happens when the inner loop's scheduler stays inside the conversation
- [codification](../../notes/codification.md) — mechanism: crystallized scheduling patterns are codification candidates, but only scheduling-level patterns (not tool-level ones) require loop exposure
