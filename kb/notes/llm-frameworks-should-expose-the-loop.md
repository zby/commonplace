---
description: Agent frameworks that hide orchestration inside tool loops push applications toward degraded scheduling; stronger frameworks keep state progression inspectable at the application layer
type: note
traits: []
tags: [computational-model]
status: seedling
---

# LLM frameworks should expose the loop

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) needs only a raw LLM SDK — the application keeps state in code and calls the model for semantic judgment. The framework question appears one layer up. Many agent frameworks take tool calling and wrap it in a hidden **tool loop**: the library re-calls the model, executes tools, and manages intermediate progression inside its own runtime. Once that happens, the convenient primitive shifts from "bounded semantic call" to "framework-managed session," and the application programmer who wants an outer loop must fight the framework's hidden scheduler rather than compose with a simple call.

This is a framework pattern that often pushes systems toward the [degraded scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md). When the framework hides progression inside its own tool loop, conversation-mediated scheduling becomes the path of least resistance, and bookkeeping, branching, and partial progress are more likely to migrate into bounded stochastic context.

## What "exposing the loop" means

Exposing the loop does **not** require every user to hand-write an imperative `while` loop. The loop can be exposed through ordinary application code, a workflow DSL, a configurable state machine, or another explicit control surface. What matters is that state progression, recursion, and branching remain inspectable and controllable at the application layer, not buried inside a framework-owned conversational runtime.

Concretely, a well-designed framework stack should:

- expose bounded model calls and tool requests as composable primitives at the base layer
- offer workflow helpers or agent loops as optional higher layers, not as the only ergonomic path
- not require application programmers to surrender orchestration just to get access to tools, retries, or structured outputs

Once the loop is exposed, the application can also choose what symbolic state to persist between calls. In the minimal reading, that may be just source state and prior call results. In the more practical reading developed in the [bounded-context orchestration model](./bounded-context-orchestration-model.md), it can also include prior prompts, rankings, decompositions, retry decisions, and other deterministic projections that help later `select(K)` steps. Hiding the loop inside the framework runtime hides that state progression too, making prompt refinement and orchestration learning much harder.

When those conditions hold, better models improve the quality of individual semantic steps, and application code determines how those steps compound across time. When they do not, the stack keeps asking the model to simulate its own scheduler inside the same scarce medium it is meant to reason within.

## Examples

[`llm-do`](https://github.com/zby/llm-do) illustrates the distinction. It supports LLM-orchestrated `.agent` entrypoints, but also exposes code-entry and direct-Python patterns where application code owns the loop and calls agents only for bounded judgment steps. The [`pitchdeck_eval_code_entry`](https://github.com/zby/llm-do/tree/main/examples/pitchdeck_eval_code_entry) and [`pitchdeck_eval_direct`](https://github.com/zby/llm-do/tree/main/examples/pitchdeck_eval_direct) examples make the contrast explicit: agent orchestration is available when useful, but deterministic orchestration does not have to be routed through a framework-owned tool loop.

The [RLM architecture](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) is a boundary case. The decisive property is not that a human manually scripts every step, but that the loop runs on an exact substrate outside the conversation. In RLM, the model may author dispatch by writing scheduler code, but the REPL still owns recursion depth and intermediate state. The design lesson is the same: what matters is where the loop runs, not who authored it.

[Specification-level separation](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) is a partial step toward loop exposure. It names control flow and externalises some state, recovering scoping benefits before hard reliability. Tool-use frameworks harden interface contracts at the boundary. Both help, but neither yields the full gain if the recursive loop remains hidden inside the framework runtime.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: this note extracts the framework-design consequence of the model's symbolic-scheduler requirement
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: explains what happens when the conversation, rather than application code, owns the loop
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: loop exposure matters because bookkeeping and semantic work have different reliability properties
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — boundary case: partial separation helps before loop exposure is complete
- [context engineering](./context-engineering.md) — applies: routing, loading, and scoping become application responsibilities when the framework stack exposes the loop
- [RLM achieves the clean scheduler model but opts out of accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — boundary case: the model can author the loop, but the loop still has to run outside the conversation to recover the clean architecture
