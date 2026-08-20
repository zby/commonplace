---
description: "Distinguishes ordinary tool implementation from scheduling by the decisions that code owns: internal procedure serves one invoked capability, while scheduling policy chooses progression across task goals even when exposed as a tool"
type: kb/types/note.md
traits: []
tags: [computational-model, context-engineering, tool-loop]
---

# Cross-task transition policy remains scheduling behind a tool interface

As agent applications mature, repeated decisions that once required open-ended judgment can be [codified](./definitions/codification.md) as explicit symbolic procedures.

Many such procedures belong inside ordinary tools: formatting, parsing, validation, and data transformation. Each describes how to perform one invoked capability, and moving it from prompt instructions into exact code makes its execution more consistent.

A deterministic implementation does not become a scheduler merely because it spans several steps. Its role depends on the decisions it owns. Code remains tool implementation when every step serves one invoked capability. It performs scheduling when it chooses progression among distinct task goals, changes the capability surface for the next call, or controls branching and stopping across those goals.

For example, scheduling policy can:

- Decompose feature work into research, implementation, and review, then choose the next goal.
- Choose between a narrower retry and escalation to a different goal after a task path fails.
- Construct a different tool surface for a child goal and decide when control returns to its parent.

A `run_feature_workflow` function that owns these choices has a scheduler role even when a model invokes it through a tool interface. The interface does not determine the role. The scheduler is *hidden* only when the interface presents it as an ordinary capability and obscures its progression state or transition authority. A workflow tool that names and exposes those controls is tool-shaped scheduling, but not concealed scheduling.

Once cross-task policy is stable enough to codify, preserving it requires explicit control logic to determine or constrain which transition executes. A framework without first-class progression makes placing that logic inside a tool attractive, but the same logic can live in an application-owned loop or lower-level runtime. The architectural question is whether a framework makes transition control directly programmable without forcing application code to escape its abstraction. This is one reason [LLM frameworks should keep the tool loop optional](./llm-frameworks-should-keep-the-tool-loop-optional.md).

---

Relevant Notes:

- [codification](./definitions/codification.md) — background: this note identifies a class of patterns that do not codify cleanly into ordinary tool implementations
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — related mechanism: codified scheduling hidden in a tool is another way a tool becomes a covert runtime
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) — consequence: codified next-step policy often needs to choose a fresh tool surface for the next child task
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — parallel case: scheduling forced by structural overflow rather than codified experience; same architectural consequence, different cause
- [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) — extends: shows how an application-owned loop can host codified transition policy without hiding it inside an ordinary tool
