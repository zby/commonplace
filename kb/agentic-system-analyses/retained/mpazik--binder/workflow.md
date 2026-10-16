---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Binder workflow account: task investigation, collaborative decisions, test preparation and implementation at the frozen revision."
run-id: AAS-2026-10-15-binder-a35c41531d40-01
reviewed-boundary: e4066d750ac5c6918706f44b12daa261b261106e
---

# Binder workflow report

## Workflow account

### Selection and evidence

The representative workflow is the shipped `implement-task` skill, already identified by [RT-RTE-task-guide](runtime.md#rt-rte-task-guide). It is selected because one entry procedure explicitly joins task selection, investigation, discussion, design, tests and implementation through rereading stored task state. These are conditional branches, not a claim that every task visits every guide. A fix task with no root cause provides a concrete starting case. The analysis extends the runtime's inspection to all five current guides under `examples/workflow/skills/implement-task/guides/`. All are SRC-1 doctrine/design evidence. No execution trace establishes guide loading, model compliance, successful tests or delivery. The [boundary](boundary.md) fixes the source and external-host limits.

### Request and routing

A user requests work on a task, optionally supplying its key. The foreground agent is instructed to read that task as YAML; without a key it selects from active/pending search results and reads the selected task. Missing keys stop the workflow. Draft, complete and cancelled status produce a message rather than implementation; pending, active and paused may proceed. The skill supplies task-schema expansion and a prioritized guide table. A fix with empty `rootCause` selects investigation before any other matching guide, unless the user directs otherwise. This is agent-interpreted routing, not a Binder scheduler. SRC-1, `examples/workflow/skills/implement-task/SKILL.md`; [RT-RTE-task-guide](runtime.md#rt-rte-task-guide).

### Investigation and the retained handoff

The same foreground agent receives the investigation guide, the task and any listed source paths. It is asked to reproduce the failure, trace code and history, identify the triggering condition, and store `rootCause`, `stepsToReproduce` and relevant `sourceFiles`; it may also store a fix direction in `potentialSolution`. Investigation explicitly excludes fixing the bug and requires removal of temporary debug/scratch changes. Its output is therefore an explanatory task update rather than production code. The entry skill then requests a fresh task read and guide selection. This creates an intended handoff through retained fields, without requiring a separate worker or transferring an isolated context. SRC-1, `examples/workflow/skills/implement-task/guides/investigate.md`, `examples/workflow/skills/implement-task/SKILL.md`.

The guide requests `binder update`; its storage mechanism is the existing [RT-RTE-graph-update](runtime.md#rt-rte-graph-update). That mechanism can reject structurally invalid mutations and roll back failed database work. It does not verify that a recorded root cause is true. Post-commit derived effects retain the limits in [RT-CLM-derived-effects](runtime.md#rt-clm-derived-effects). The prompts request later consumption of the updated fields; no supplied run demonstrates the write/read-back sequence.

### Human decisions and design

On reread, linked Problem records may select discussion. The agent receives the task's links and reads each Problem with a nested deliberation tree. It researches and proposes options, records agreed options and arguments, and creates a Decision only with user agreement. Smaller task-scoped answers go into a Decisions section of task `details`. This is a collaborative handoff: the agent proposes and records; the user supplies agreement at the prescribed decision points. It is not automatic software approval. SRC-1, `examples/workflow/skills/implement-task/guides/discuss.md`.

If the task lacks a specification and meets the entry table's size/type condition, design is next. The agent reads task/source/linked records, presents alternatives with tradeoffs, and discusses a proposal before writing the specification. The persisted contract contains Approach, Contracts, File Plan, Validation and Steps. User agreement is a completion condition. A rejected design is not ready under this policy; discussion must continue, although the guide gives no bounded retry count or automated rejection handler. SRC-1, `examples/workflow/skills/implement-task/guides/design.md`.

### Verification, repair and delivery

For a fix that still needs tests, the testing guide asks for a reproduction test derived from task requirements and the root cause. Before implementation it should fail; after implementation it should pass. Feature tests similarly distinguish pre/post implementation, while refactor behavior-locking tests should pass before the refactor. Expected failure is thus evidence of reaching a pre-implementation checkpoint, not workflow rejection. Test code and its results are handed to the same agent's subsequent implementation step, with another task reread requested by the entry skill. SRC-1, `examples/workflow/skills/implement-task/guides/write-tests.md`, `examples/workflow/skills/implement-task/SKILL.md`.

Implementation receives the task, source files, tests, constraints and any specification. Its priority order is existing passing tests, specification, acceptance criteria, then potential solution. The existing tests are a conditional project-provided reference, not independently established truth. The agent implements within scope, runs tests and checks each acceptance criterion. Failing final tests or unmet criteria prevent completion under the prompt policy; the agent owns fixing failures. No inspected executable gate rejects an agent's completion report on this basis. SRC-1, `examples/workflow/skills/implement-task/guides/implement.md`; [RT-RTE-task-guide](runtime.md#rt-rte-task-guide).

Delivery here means code satisfying acceptance criteria, passing tests and no unrelated changes, accompanied by mention of discovered issues or improvements for possible separate draft tasks. The inspected entry and five guides do not prescribe marking the Task complete, committing, merging, releasing or obtaining final human acceptance of the implemented code. Those events cannot be inferred from the completion checklist. Nor is termination mechanically ensured: the entry table matches linked Problems without an explicit unresolved-status condition, whereas the discussion guide's completion check concerns unresolved Problems; deciding that the task no longer needs discussion or tests remains agent judgment. SRC-1, `examples/workflow/skills/implement-task/SKILL.md`, `examples/workflow/skills/implement-task/guides/discuss.md`, `examples/workflow/skills/implement-task/guides/implement.md`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-guide](runtime.md#rt-rte-task-guide)

Workflow-specific elaboration: investigation, discussion, design, tests and implementation are successive conditional phases of this existing route, not separate autonomous delegates. The foreground agent owns next-guide selection and repair. The user can override guide selection and must agree to formal decisions and the design. Binder owns structural state admission, not semantic approval. The operating mode is open requested product work, not an experiment or curriculum. The additional inspected coverage is SRC-1, `examples/workflow/skills/implement-task/guides/investigate.md`, `examples/workflow/skills/implement-task/guides/discuss.md`, `examples/workflow/skills/implement-task/guides/design.md`, `examples/workflow/skills/implement-task/guides/write-tests.md`, together with rereading the entry and implementation guide. These supply doctrine/design only.

The cross-phase handoff is explicit:

> After completing a guide, re-read the task and check the table again. If another condition applies, load that guide next. If no conditions match, go to implement.
> --- `examples/workflow/skills/implement-task/SKILL.md`

Investigation requests durable findings and cleanup rather than a fix:

> Find the root cause of a bug. Don't fix it.
> --- `examples/workflow/skills/implement-task/guides/investigate.md`

> Remove any temporary changes you made during investigation (debug prints, scratch files). The goal is findings, not code changes.
> --- `examples/workflow/skills/implement-task/guides/investigate.md`

The discussion guide supplies a human decision gate and a bounded completion criterion:

> 5. **Decide.** Only when the user agrees. Create a Decision record.
> --- `examples/workflow/skills/implement-task/guides/discuss.md`

> - All linked Problems with status != complete have been addressed
> --- `examples/workflow/skills/implement-task/guides/discuss.md`

The design gate applies before recording the contract:

> This is a collaborative guide — propose the design and discuss with the user before writing it.
> --- `examples/workflow/skills/implement-task/guides/design.md`

Tests use mode-dependent expected outcomes, which must not be mistaken for a universal pass-at-every-step rule:

> - **Pre-implementation**: no production code for this change exists yet. Tests should fail now and pass after implementation.
> - **Post-implementation**: production code already exists. Tests should pass now.
> --- `examples/workflow/skills/implement-task/guides/write-tests.md`

Final delivery criteria are narrower than release or task-status transition:

> ## Done when
>
> - `acceptanceCriteria` are met (if defined)
> - Tests pass
> - No unrelated changes
> --- `examples/workflow/skills/implement-task/guides/implement.md`

The existing runtime record supplies the final verify/fix instruction and priority evidence. Recovery in these guides consists of continued discussion, correcting code/test failures, and cleaning investigation artifacts. They specify no general rollback of production edits or rejected design writes. Actual repair, agreement, verification and completion remain unobserved.

#### On [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance)

Workflow-specific context limit: the entry procedure requests loading only the currently selected guide and rereading external task state. It does not specify a sub-agent, isolated per-guide frame, removal of previous guides, compaction or context-window eviction. The added guide inspection establishes requested staged context delivery, not a guarantee that the external host keeps unrelated context out or discards earlier material. Investigation findings and an agreed specification can shape later choices through task reads; this is not evidence of improved capacity or exercised self-improvement. SRC-1, `examples/workflow/skills/implement-task/SKILL.md`; the handoff passage above supplies the source instruction.
