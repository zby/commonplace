---
description: As agent behavior matures, deterministic next-step policies need explicit control logic; if the framework offers only tools, scheduling patterns end up there and the tools become hidden schedulers
type: note
traits: []
tags: [computational-model, context-engineering, tool-loop]
status: seedling
---

# Codified scheduling patterns can turn tools into hidden schedulers

As agent applications mature, some repeated decisions stop needing open-ended judgment and [codify](./codification.md) into deterministic procedure.

Many codified patterns fit naturally inside ordinary tools — formatting, parsing, validation, data transformation. These patterns describe *how to perform a single capability*, and they improve when they move from prompt instructions into exact code.

A deterministic multi-step implementation can still be an ordinary tool when those steps remain internal to one coherent capability rather than choosing what broader task step should happen next.

Scheduling patterns are different. They describe *what should happen next*:

- after editing, always run tests before summarizing
- decompose feature work into research, implementation, and review
- after a failed tool path, retry once with narrower context and then escalate
- after collecting search results, deduplicate and re-rank before presenting

When a tool embeds next-step policy across subtasks, retries, recursion, or tool-surface selection, it stops acting like an ordinary capability and starts acting like a hidden scheduler. A `run_feature_workflow` tool that decides which subtask to run, which tool surface to expose, when to recurse, and when to stop is not a tool — it is an orchestration runtime behind a tool-shaped facade.

This works, but it is not where codified scheduling wants to live. Once next-step policy has stabilized enough to become code, the application needs to replace model-chosen transitions with explicit control logic. When codified policy needs to choose the next subtask, alter the next tool surface, or manage retries and stopping conditions across task boundaries, a framework that exposes tools but not progression forces that control logic to masquerade as tool implementation.

---

Relevant Notes:

- [codification](./codification.md) — background: this note identifies a class of patterns that do not codify cleanly into ordinary tool implementations
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — related mechanism: codified scheduling hidden in a tool is another way a tool becomes a covert runtime
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) — consequence: codified next-step policy often needs to choose a fresh tool surface for the next child task
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) — parallel case: scheduling forced by structural overflow rather than codified experience; same architectural consequence, different cause
