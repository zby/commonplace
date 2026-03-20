---
description: Granting the strongest stateful-tool escape hatch shows that recovered control comes from relocating the scheduler into an exceptional tool or runtime, not from the framework loop itself
type: note
traits: []
tags: [computational-model, context-engineering, tool-loop]
status: seedling
---

# Stateful tools recover control by becoming hidden schedulers

A naive version of the "expose the loop" argument claims that a framework-owned tool loop cannot express what application-owned orchestration requires. That version is false. If we allow a sufficiently stateful tool — a singleton runtime behind the tool boundary — a hidden loop can recover substantial control.

The recovery is genuine. Such a runtime can hold retries, checkpoints, branch records, and recursion state — enough orchestration logic that the model never has to invoke a visible scheduler. From the model's perspective nothing has changed; from the application's perspective, the tool is quietly running the show.

But notice what happened. The scheduler — the code deciding what happens next — has been relocated into a special tool. The framework loop is still running, but it is no longer the locus of control. A tool became a covert orchestration runtime.

That reframes the question. The hard problem is not whether hidden loops *can* recover expressivity — they can. It is where the scheduler lives and whether the framework exposes it or forces it to masquerade as tool implementation. And even this recovery has limits: [changing the action alphabet between sub-tasks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) and [sub-goals that exceed one context window](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) are the strongest cases where a hidden scheduler starts to buckle.

---

Relevant Notes:

- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) — consequence: changing the next step's capability surface is where hidden-scheduler recovery becomes awkward
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) — consequence: large semantic sub-goals require explicit orchestration over many smaller semantic calls
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — background: explains why orchestration is naturally modeled as symbolic scheduling over bounded calls
