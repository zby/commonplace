---
description: Framework-owned tool loops may preserve raw computability, but they are less expressive as hybrid orchestration interfaces when re-entry, branching, and state projection are hidden inside the runtime
type: note
traits: []
tags: [computational-model, observability]
status: seedling
---

# LLM frameworks should expose the loop

Every agent system has a loop. Some component owns symbolic state, some mechanism selects what enters the next bounded call, some runtime decides how results feed into later steps. The [bounded-context orchestration model](./bounded-context-orchestration-model.md) names this structure. The question for framework design is **who owns the loop, and who can program it**.

The intuition is simple: hiding the loop feels weaker than exposing it. The obvious version of that claim — hidden loops reduce what the system can compute — is wrong. A sufficiently stateful tool can compute anything. The real loss is narrower and more specific.

Many agent frameworks wrap tool calling in a hidden **tool loop** where the library re-calls the model, executes tools, and manages progression inside its own runtime — making the framework, rather than the application, the owner of progression.

The relevant question is not raw computability — it is **what hybrid LLM/program control flows the interface lets the application express directly**.

On that dimension, a hidden tool loop is often **less expressive** than an application-owned loop. The primitive shifts from "bounded semantic call" to "framework-managed session." If the framework exposes only the control moves it anticipated, then many useful programs are no longer first-class operations at the application layer: call a tool, project only selected state into a fresh prompt, branch into multiple bounded calls, merge results, retry with altered framing, or interleave deterministic transforms with fresh semantic judgments. Those programs may still be approximable, but not directly composable.

That difference matters because recursion depth, branching policy, retry rules, state projection, and intermediate transforms are often part of the application's logic rather than incidental runtime detail. If those moves are not first-class at the application layer, they have to be smuggled into tool internals, prompt conventions, or conversation history. The framework still owns the official loop; the application can only steer it indirectly.

The main workaround is to move orchestration into a stateful tool, paired with instructions that tell the model when to call it again and how to interpret its intermediate results. That can work, but it does **not** remove the boundary above. A stateful tool can recover arbitrary deterministic computation, but it does **not** by itself recover arbitrary hybrid `tool -> LLM -> tool -> LLM` programs. To express those directly, some layer still has to expose re-entry, state projection, and branching semantics. If it does not, the application is left steering the hidden scheduler through prompt convention rather than programming the loop directly.

Even when that workaround succeeds, it is a poor programming model. Once the scheduler collapses into the tool, the framework loop has been hollowed out rather than vindicated. The tool becomes the real scheduler, the model becomes a relay that re-triggers it, observability migrates into tool internals and prompt discipline, and each iteration spends a full model call to re-enter deterministic code the application could have owned directly.

This does not make such frameworks useless. It locates them in the design space: a specific instantiation where the scheduler is partly buried inside a conversational runtime. That pattern pushes systems toward the [degraded scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — conversation-mediated progression becomes the path of least resistance, and bookkeeping, branching, and partial progress migrate into bounded stochastic context.

## What "exposing the loop" means

Exposing the loop does **not** require every user to hand-write an imperative `while` loop. The loop can live in ordinary application code, a workflow DSL, a configurable state machine, or any other explicit control surface. What matters is that state progression, recursion, branching, re-entry, and state updates remain inspectable and controllable at the application layer.

The point is also not that every application should start with maximum manual control. Higher-level agent loops can be useful defaults. The stronger claim is that a good framework must preserve the more expressive control surface underneath, because serious systems often need to reclaim it once orchestration becomes mechanical, cost-sensitive, reliability-sensitive, or deeply entangled with application state.

Concretely, a well-designed framework stack should:

- expose bounded model calls and tool requests as composable primitives at the base layer
- offer workflow helpers or agent loops as optional higher layers, not as the only ergonomic path
- not require application programmers to surrender orchestration just to get access to tools, retries, or structured outputs
- let application code decide when to keep a higher-level agent loop and when to replace part of it with exact symbolic control
- expose enough control to express fresh re-entry, branching, and explicit state projection without abusing session history

When the loop is exposed, the application also chooses what symbolic state persists between calls — prior prompts, rankings, decompositions, retry decisions, and other deterministic projections that help later selection steps. Hiding the loop hides that state progression too, locking the application programmer out of the scheduler's effective state.

Framework-owned loops reinforce a related problem: [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md). Once a framework owns the loop, it often also decides what later calls inherit — and the default shifts from "select the next prompt from symbolic state" to "continue the session," convenient for chat UX but the wrong default for most orchestration.

When these conditions hold, better models improve individual semantic steps and application code determines how those steps compound. When they do not, the stack asks the model to simulate its own scheduler inside the same scarce medium it is meant to reason within, while shrinking the space of hybrid control flows the application can express directly.

## Examples

[`llm-do`](https://github.com/zby/llm-do) illustrates the distinction directly. It supports LLM-orchestrated `.agent` entrypoints, but it also supports manifest-selected code entrypoints and direct-Python patterns where application code owns the orchestration loop and calls agents only for bounded judgment steps. In the `pitchdeck_eval` example, an LLM orchestrator lists files, calls the evaluator, and writes outputs. In `pitchdeck_eval_code_entry`, Python performs the same mechanical loop and uses `runtime.call_agent(...)` only for the deck evaluation step. In `pitchdeck_eval_direct`, the same spectrum is exposed programmatically: one script gives Python the loop, another gives the loop to an LLM entry agent, and a third bypasses the framework entirely. The point is not that higher-level loops disappear; it is that the framework does not force every application through one hidden conversational loop.

The [RLM architecture](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) is a boundary case. The decisive property is not that a human scripts every step, but that the loop runs on an exact substrate outside the conversation. The model may author dispatch by writing scheduler code, but the REPL still owns recursion depth and intermediate state. What matters is where the loop runs, not who authored it.

[Specification-level separation](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) is a partial step toward loop exposure. It names control flow and externalises some state, recovering scoping benefits before full scheduler separation. This helps, but does not recover the full orchestration expressivity if re-entry and recursive progression remain hidden inside the framework runtime.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: this note extracts the framework-design consequence of the model's symbolic-scheduler requirement
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: explains what happens when the conversation, rather than application code, owns the loop
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — extends: once the framework owns progression it also tends to decide what later calls inherit
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — extends: once the framework owns the loop it also controls whether successful outcomes preserve evidence that part of the intended path failed
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: loop exposure matters because bookkeeping and semantic work have different reliability properties
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — boundary case: partial separation helps before loop exposure is complete
- [context engineering](./context-engineering.md) — applies: routing, loading, and scoping become application responsibilities when the framework stack exposes the loop
- [RLM achieves the clean scheduler model but opts out of accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — boundary case: the model can author the loop, but the loop still has to run outside the conversation to recover the clean architecture
