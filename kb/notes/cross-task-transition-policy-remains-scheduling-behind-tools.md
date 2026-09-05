---
description: "Classifies code by authority over interceptable transitions among independently steerable goals, separating scheduler role from its tool-shaped interface and audience-relative concealment"
type: kb/types/note.md
traits: []
tags: [computational-model, context-engineering, tool-loop]
---

# Cross-task transition policy remains scheduling behind a tool interface

As agent applications mature, repeated decisions that once required open-ended judgment can be [codified](./definitions/codification.md) — turned into explicit symbolic procedures.

Many such procedures belong inside ordinary tools: formatting, parsing, validation, and data transformation. Moving them from prompt instructions into exact code makes execution more consistent. Calling the result a tool describes how it is invoked, but not which transitions it controls.

A deterministic implementation does not become a scheduler merely because it spans several steps. The boundary is an **externally meaningful transition**: a point where a supervising caller could inspect the result, stop, or redirect work to another independently steerable goal without violating the current operation's integrity. Re-entry is **interceptable** when the runtime returns control or exposes a transition hook before the next goal begins. Retries, branches, and stopping rules remain ordinary implementation when they only preserve the current operation's contract and expose no such transition.

Code performs a scheduling role when it owns the choice at an externally meaningful boundary: which goal becomes active next, which cross-goal branch executes, or whether and when the supervising caller regains control. Goal progression and cross-goal branching are sufficient tests only when the named goals are independently steerable and the code owns their transition; otherwise those labels are merely diagnostic. A capability-surface change is never sufficient by itself: an authorization interceptor can change the next call's tools without choosing task progression. It indicates scheduling only when it implements a cross-goal transition.

For example, scheduling policy can:

- After research, choose whether to return control, start implementation, or branch into review.
- After a task path fails, choose between another attempt at the same goal and escalation to a different goal.
- Dispatch a selected child goal with a different tool surface, then decide when its parent regains control.

A `run_feature_workflow` function that owns these choices has a scheduler role even when a model invokes it through a tool interface. The interface does not determine the role. Concealment is audience-relative: the scheduler is hidden from an audience only when that audience sees an ordinary capability while its interface obscures the progression state and transition controls. The same workflow can be opaque to the calling model but explicit to an operator or application programmer who can inspect and intervene in its transitions. A workflow tool that exposes those controls to its intended controller is tool-shaped scheduling, not concealed scheduling for that controller.

Once cross-task policy is stable enough to codify, preserving it requires explicit control logic to determine or constrain which transition executes. That logic can live in a workflow tool, an application-owned loop, or a lower-level runtime. The architectural requirement is a directly programmable transition boundary: an interceptable return or hook where the responsible controller can observe, change, or veto the next cross-goal transition without escaping the framework's abstraction. A mandatory loop can satisfy this requirement if it exposes such a boundary; making the loop optional is one implementation, not the requirement itself.

---

Relevant Notes:

- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — mechanism: shows how cross-goal transition authority can move behind a tool boundary
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) — extends: develops the narrower case where a cross-goal transition requires a fresh capability surface
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — contrasts: derives scheduling from structural overflow rather than codified transition policy
- [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) — extends: shows how an application-owned loop can host codified transition policy without hiding it inside an ordinary tool
- [Claude Code dynamic workflows](../agentic-systems/reviews/claude-code-dynamic-workflows.md) — evidenced-by: its model-authored JavaScript visibly selects sub-agent transitions even though the harness exposes workflow invocation through a callable interface
