---
description: When decomposition creates child tasks with different tool surfaces, the parent must construct fresh calls for each child, so a framework-owned loop is no longer the right control surface
type: note
traits: []
tags: [computational-model, context-engineering, tool-loop]
status: seedling
---

# Subtasks that need different tools force loop exposure in agent frameworks

A framework-owned tool loop works well when one task runs against one stable set of tools. The constraint appears when a parent task decomposes into children that each need a different **capability surface** — a different set of actions exposed to the model.

A research child may need `{search, summarize}`. An implementation child may need `{read_file, patch_file, run_test}`. A review child may need `{read_file, compare, submit_review}`. The parent must dispatch each child with the right tools, collect its result, then decide what comes next.

This is not a bookkeeping problem that tool wrappers can absorb. Changing the capability surface changes the **action alphabet** of the next bounded call — what the model is allowed to do, not just what state surrounds it. That requires constructing a fresh call with a fresh prompt, a fresh tool set, and often a fresh stop condition.

A framework-owned loop has only awkward responses: one giant static tool set that leaks irrelevant affordances into every step, a meta-tool that becomes the real scheduler while the loop degrades to a message relay, or an escape back into direct API calls that abandons the framework's conveniences.

The clean response is to spawn a **sub-agent**: a fresh tool loop with its own prompt, capability surface, and stop condition. The parent delegates, the child runs its own loop, and the parent resumes when the child returns. That is what "loop exposure" means in practice — not that the programmer hand-writes every API call, but that the framework treats spawning a new loop as a first-class operation. A further complication: the child task may itself [exceed one context window](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md), requiring its own symbolic orchestration internally.

Sub-task dispatch is not the only case. A programmer may want to change the tool surface mid-task — adding tools as new capabilities become relevant, or removing them once a phase is complete. Adding tools is relatively clean: the model just sees new affordances. Removing tools that already appear in the conversation history is not. The model has memories of calling those tools; their absence creates incoherence. It may attempt to call them again, or lose coherent reasoning about its own prior actions. You cannot cleanly shrink a context's action alphabet — you can only start a fresh context where it was never larger. That asymmetry is why sub-agents keep winning over in-place tool mutation: they sidestep the removal problem entirely.

So loop exposure is the general property — the framework lets the application control what the next step can do. Sub-agents are the dominant mechanism because they provide the fresh context that dynamic tool removal cannot. The decisive question is not whether hidden state can be recovered inside one loop — a [stateful tool can recover quite a lot](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — but whether the framework treats spawning a new loop as a first-class operation.

---

Relevant Notes:

- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — concession: grants the strongest stateful-tool escape hatch without treating it as a clean recovery
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) — complements: some sub-goals require fresh calls not only because tools change but because the sub-goal itself exceeds one context window
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — background: each child task is naturally a fresh bounded call with its own selected context and tools
