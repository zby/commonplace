---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MemPalace delegated coding workflow: approved task, controlled worker launch, patch delivery and requester verification at the frozen commit."
run-id: AAS-2026-10-14-mempalace-ed71875aea5a-01
reviewed-boundary: "1392e1810c3ca67776bd7fe3e198788a96dbd6d1"
---

# MemPalace workflow report

## Workflow account

### Selection and evidence

The representative workflow is a delegated coding task carried through the logstream. It was selected because the shipped task skill connects request creation, worker handoff, workspace checks, patch return, requester verification and failure reporting in one explicit lifecycle. This is not a workflow assembled from unrelated storage capabilities. It combines executable coordination with agent operating instructions; it does not establish an observed successful coding run. SRC-1: `skills/mempalace-task/SKILL.md`, `mempalace/tasks.py`, `mempalace/cli/cmd_coord.py`.

Added source inspection covers the complete task skill and task-envelope module, the controlled-launch section of `mempalace/cli/cmd_coord.py`, artifact/ack/patch/read functions in `mempalace/logstream.py`, and delegation/closure sections of `integrations/shared/coordination-protocol.md`. These are implementation and doctrine/design evidence within SRC-1 at the boundary pin. No runner, tool, test or provider was executed. External agent compliance, monitoring and product verification remain unobserved. The runtime records supply the starting-state and patch-storage baseline; workflow additions below identify task creation and acknowledgment separately.

### Request and handoff

The requesting agent gathers project, requester/worker identities, goal, branch, hexadecimal base commit and definition of done. The skill requires approval of the exact normalized task before append, unless already explicitly approved in the current turn. This is agent-mediated human approval doctrine, not a confirmation enforced by `create_task`. That function structurally validates fields, generates a correlation ID, formats goal/done/delivery text, and appends an open request with project stream, delegation room and addressed worker. See [WF-RTE-task-create](#wf-rte-task-create) and [RT-OBJ-task-request](runtime.md#rt-obj-task-request). SRC-1: `skills/mempalace-task/SKILL.md`, `mempalace/tasks.py`.

The portable default is a pasteable pointer, not process launch. It asks the destination to open the stored task, claim it and follow its exact definition of done. The requester is instructed to return that line unchanged; an event alone cannot wake a non-monitoring turn-based agent. Remote MCP creation writes to the shared hub; the skill forbids silently replacing a failed remote call with local task creation. These are intended handoff and recovery policies, not demonstrated destination activity. SRC-1: `skills/mempalace-task/SKILL.md`; [RT-BAP-task-handoff](runtime.md#rt-bap-task-handoff).

### Worker entry, rejection and execution

On receipt, the worker is instructed to fetch the exact request by correlation ID, check its addressed identity and workspace, claim it, then execute and run the stated verification. Claim acknowledgment records coordination state; it does not itself execute the task. The skill asks sibling sessions to check for an existing claim from their own stable identity and uses lowest-HLC as the simultaneous-claim convention. The inspected acknowledgment implementation appends an event, not an exclusive execution lock. Therefore this evidence supports a cooperative duplicate-work avoidance policy, not a proven exactly-one-worker guarantee. SRC-1: `skills/mempalace-task/SKILL.md`, `mempalace/logstream.py`; [WF-RTE-event-ack](#wf-rte-event-ack).

Explicitly requested headless launch adds software checks. The CLI selects one stored request or accepts a transported JSON event, verifies concrete destination and compatible known runner suffix, checks directory/branch/resolved base commit/clean Git state, then starts Codex or Claude through an argument list. It closes its logstream handle before the child connects. The child receives the pointer and workspace, not the requester's conversation. The external runner owns model context, execution steps and permissions. Source text does not show child reload or successful definition-of-done compliance. See [RT-RTE-task-launch](runtime.md#rt-rte-task-launch). SRC-1: `mempalace/cli/cmd_coord.py`.

A consequential rejection path is a base-commit mismatch: validation raises before spawning the worker. The skill says not to edit and to ask the requester to supersede the task with a corrected request. The launcher does not repair the workspace or rewrite the task. Missing/duplicated requests and incompatible addressed identities also fail rather than guessing. Spawn errors surface; nonzero child exit propagates, but the launcher does not automatically convert it into a logstream failure reply. SRC-1: `mempalace/cli/cmd_coord.py`, `skills/mempalace-task/SKILL.md`; launch evidence is retained in [RT-RTE-task-launch](runtime.md#rt-rte-task-launch).

> - **Base commit mismatch:** do not edit; ask the requester to supersede the
>   task with a corrected request.
> --- `skills/mempalace-task/SKILL.md`

### Patch return, verification and closure

The worker is instructed to deliver through patch submission with correlation, branch and base commit; merely pushing a branch is not the handoff. If blocked or unable to produce a patch, the prescribed return is a verbatim `task.reply` with blocked/failed status. Requester and worker are instructed to monitor for replies and feedback, with a local watcher or MCP-backed waiting on a remote-only client. Actual attention and watcher activity were not supplied. SRC-1: `integrations/shared/coordination-protocol.md`, `skills/mempalace-task/SKILL.md`.

Patch submission stores content and then a linked ready event, while artifact retrieval returns content plus hash. This establishes recoverable proposal delivery into coordination state, not application. Patch-content warnings can accompany storage instead of vetoing it. Hash matching verifies content identity, not whether the patch meets the task. See [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery) and [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact). SRC-1: `mempalace/logstream.py`.

The requester is instructed to retrieve the artifact, verify its hash, apply with explicit user-visible intent, run the stated verification, and acknowledge applied or failed. The human/agent requester owns application and acceptance; the submitter's ready label is not acceptance. No reference-answer comparator is established by this workflow. Its task-specific definition of done and verification commands may constrain judgment, but their contents and results were not supplied. See [WF-CLM-review-closure](#wf-clm-review-closure). SRC-1: `skills/mempalace-task/SKILL.md`, `integrations/shared/coordination-protocol.md`.

Thus there are two delivery boundaries: the implementation returns a stored artifact/event to the submitter; the operating protocol closes the delegated work only when the requester reports applied/failed, or the worker reports blocked/failed. These statuses are appended reports, not proof of filesystem effects or passing tests. A failed review requires evidence in the reply; who performs further repair remains coordinated by subsequent human/agent action rather than an automatic patch rollback established here. SRC-1: `mempalace/logstream.py`, `integrations/shared/coordination-protocol.md`.

The protocol also asks the agent to file one outcome drawer so the result can be searched without replaying the event trail. This is a prescribed transition from active coordination to retained memory, not a write automatically performed by `submit_patch` or `ack_event`. No resulting drawer or later use was observed. SRC-1: `integrations/shared/coordination-protocol.md`.

> - **File the outcome.** When a delegation concludes, write one drawer
>   (`mempalace_add_drawer`) recording what was decided/learned, so the
>   result is searchable without replaying the event trail.
> --- `integrations/shared/coordination-protocol.md`

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-task-create
Label: Canonical task creation

Endpoints/progression: requester-supplied fields → high-level task constructor → open task.request event → task and portable handoff returned. Owner: `create_task` software; requester supplies goal and completion criterion. Context/state/effects: a generated correlation ID and project stream route the addressed request; goal/done/delivery text persists in logstream coordination storage. This is the producer of [RT-OBJ-task-request](runtime.md#rt-obj-task-request), distinct from the later execution route [RT-RTE-task-launch](runtime.md#rt-rte-task-launch) and result route [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery); no counterpart creation route is declared in the supplied runtime. SRC-1: `mempalace/tasks.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored task event plus pointer handoff.
- Later read-back: worker can retrieve the persisted task by correlation ID for a later invocation.
- Delegated visibility: addressed worker receives a pointer requiring full-task reload; creation itself launches no worker.
- Selection predicate: nonempty required text, nonempty goal/done and hexadecimal base commit; addressed project/agent routing fields determine the destination.
- Invalidation or expiry: inapplicable — this constructor establishes no task expiry or automatic cancellation; correction by superseding requests is instructed separately.
- Activation or effect: append of an open coordination request is wired; worker execution and obedience are unobserved.
- Evidence limits: no creation/reload trace; structural checks and a returned handoff do not establish user approval, notification or task completion.

Admission: requester proposes exact task content; software can reject malformed fields. Human approval of normalized content is required by the task skill but not checked by the constructor. Mode: open delegated work. No answer oracle is used in creation. Delivery guidance persists inside the request body. Recovery doctrine asks for corrected superseding requests rather than mutating the original; actual recovery was not supplied. SRC-1: `skills/mempalace-task/SKILL.md`, `mempalace/tasks.py`.

>     body = (
>         f"Goal:\n{goal}\n\n"
>         f"Definition of done:\n{done}\n\n"
>         "Delivery:\n"
>         "Close the loop through MemPalace: claim the request, then submit a patch "
>         "with mempalace_patch_submit or reply with blocked/failed evidence."
>     )
> --- `mempalace/tasks.py`

#### WF-RTE-event-ack
Label: Linked event acknowledgment

Endpoints/progression: agent supplies target event ID/status/body → target lookup → append routed event.ack → returned acknowledgment. Owner: logstream code for linkage, calling agent for claimed outcome. Context/state/effects: the new event inherits stream/room/topic, correlates with the target and routes back to its author; the target remains unchanged. This is distinct from [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery): it records a response to an existing event rather than a patch artifact proposal. The supplied runtime declares no acknowledgment counterpart. SRC-1: `mempalace/logstream.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: new acknowledgment event or error for missing target/invalid fields.
- Later read-back: appended acknowledgment remains available to later coordination readers with correlation and ack_of linkage.
- Delegated visibility: response is addressed to the original event's author; no process or isolated agent context is created.
- Selection predicate: exact target event ID lookup and validated append fields; caller supplies status and body.
- Invalidation or expiry: inapplicable — the acknowledgment function neither mutates the target nor establishes acknowledgment expiry.
- Activation or effect: append of a linked response is wired; status does not prove execution, acceptance or exclusive ownership.
- Evidence limits: no claim race, reader or acceptance trace; inspected function establishes linkage, not duplicate-worker exclusion or verification of outcome assertions.

Admission: calling agent proposes status/evidence; software validates and links the event, not the truth of claimed/applied/failed outcomes. Mode: open coordination; no answer oracle. The task skill supplies claim and closure guidance. A missing target rejects the append; product rollback is not an effect of this acknowledgment function. SRC-1: `mempalace/logstream.py`, `skills/mempalace-task/SKILL.md`.

>         The target event is never mutated. The ack copies the target's
>         stream/room/topic, copies its ``correlation_id`` (falling back to the
>         target's id so request/ack stay tied together), and routes back
>         to the target's ``from_agent``.
> --- `mempalace/logstream.py`

### Claims

#### WF-CLM-review-closure
Label: Requester review and closure

Claimed operation: requester retrieves and verifies the proposed artifact, applies with explicit user-visible intent, runs verification and acknowledges applied/failed. Worker failure instead returns blocked/failed evidence. Source: SRC-1 `skills/mempalace-task/SKILL.md`, `integrations/shared/coordination-protocol.md`; doctrine/design. This lifecycle claim is distinct from implementation-only proposal persistence in [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery). Owner/enforcement: participating requester/worker under loaded instructions. Guarantee strength: policy. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. Acceptance and actual application are external to the inspected patch-submission function.

> 6. The requester fetches and verifies the artifact, applies it with explicit
>    user-visible intent, runs verification, then acknowledges `applied` or
>    `failed`.
> --- `skills/mempalace-task/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-launch](runtime.md#rt-rte-task-launch)

Workflow role: optional controlled adapter after task creation, not the portable default. It enforces starting workspace checks before delegating execution; agent instructions separately require full-request reload and stated verification. The base-mismatch recovery owner is the requester asked to supersede the request. Child process exit is not the workflow's acceptance signal. These distinctions follow SRC-1 `skills/mempalace-task/SKILL.md`, `mempalace/cli/cmd_coord.py`.

#### On [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery)

Workflow role: proposal handoff preceding requester acceptance. The review/closure policy in [WF-CLM-review-closure](#wf-clm-review-closure) supplies the missing downstream decision owner, not a new built-in acceptance gate. Artifact retrieval exposes content and hash; bad-format warnings can accompany a stored patch. Ready delivery must therefore not be equated with applicability or passing verification. SRC-1: `mempalace/logstream.py`, `skills/mempalace-task/SKILL.md`.

>         For ``kind=patch``, a ``warnings`` list is included when the diff
>         looks unappliable (missing trailing newline, CRLF endings); the
>         content itself is still stored verbatim.
> --- `mempalace/logstream.py`
