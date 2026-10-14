---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Enoch workflow account: queued repository implementation, bounded validation repair, captured review handoff and terminal reporting."
run-id: AAS-2026-10-13-enoch-a73695a57e3b-01
reviewed-boundary: "0934ad59bd253adfffb8263c65e4bf0f4e2d7a9f"
---

# Enoch workflow report

## Workflow account

### Selected workflow and evidence

The selected workflow is a chat `/task <request>` that produces new repository changes for review. It is representative because it connects user intent, conversation-to-task delegation, owned background execution, model editing, verification, recovery and a delivered artifact in one shipped caller chain. It is not a reconstruction joining unrelated capabilities. The enclosing route is [RT-RTE-task-work](runtime.md#rt-rte-task-work); this member adds its review-publication part, [WF-RTE-review-handoff](#wf-rte-review-handoff), and workflow annotations rather than redeclaring the task route.

All findings use SRC-1 at the [frozen boundary](boundary.md#source-register). Additional implementation inspection covers the task command, snapshot producer/parser, task worker, terminal reporting and session-sync methods in `src/enoch/app/core.py`; ordinary work, publication/resume and captured-copy checks in `src/enoch/app/task_workflow.py`; complete `src/enoch/app/validation_repair.py` and `src/enoch/app/review_publication.py`; and task-prompt/handoff-note construction in `src/enoch/prompt_append.py`. These are implementation and model-facing policy evidence, not an observed execution. No successful edit, doctor pass, provider delivery, merge or restart is established.

### Request to owned work

The application admits the chat event under the conversation and action controls described by [RT-RTE-chat-actions](runtime.md#rt-rte-chat-actions). The task command first asks the conversation runtime for a task brief. It can return a clarification rather than queueing, report a context-generation error, or queue a paused request when runtime access is unavailable. Otherwise it queues the original request, thread, selected context, context-source label, event idempotency key and profile task options. Initial delivery is a queued-status message, not the work product (SRC-1, `src/enoch/app/core.py`).

The snapshot call uses the conversation session; the worker uses a distinct session key ending in `:task:<id>`. Thus the host delegates to another model invocation, not to a separately launched autonomous agent with the full chat transcript. The model is asked to select relevant prior conversation material, and code normalizes and clips the resulting brief to 3,000 characters. That clip can remove information; the brief's completeness and accuracy are not independently checked. The prompt states the selection objective:

> "Include the intended outcome, relevant decisions, constraints, target files or systems, and anything explicitly ruled out.",
> "Return only the task brief.",
> --- `src/enoch/app/core.py`

The worker loop selects a queued job and obtains a claim with a generated worker identity and process ID. Failure to claim returns without executing. It installs task-local identifiers, deadline and cancellation state, supplies request/attempt identity, task session and progress callback, and authorizes the task before invoking work. Workspace preparation separately requires that the task remain running under the same worker; recording the workspace can reject a lost lease (SRC-1, `src/enoch/app/core.py`, `src/enoch/app/task_workflow.py`). This is host-owned scheduling and cooperative ownership, not model scheduling or a demonstrated distributed exactly-once guarantee.

### Editing to validation

For a new-change request, the workflow preflights provider features and capabilities, prepares an isolated workspace from the authoritative revision, and invokes the selected runtime with the request plus task context, task-profile prompt, workspace cwd and execution controls. The model proposes and performs edits; the application inspects changed paths rather than treating its completion text as sufficient evidence. Final model text is also parsed for memory/regression requests, but their admission and future effects are outside this selective workflow account (SRC-1, `src/enoch/app/task_workflow.py`, `src/enoch/prompt_append.py`). The task runtime and provider-specific access limits remain those of [RT-RTE-task-work](runtime.md#rt-rte-task-work): a separate workspace is not filesystem confinement.

If no paths changed, the workflow attempts workspace cleanup and returns completed with only the edited stage. This means completion can be a no-change response, not a review or proof that the requested outcome was achieved. If files changed, doctor checks are the publication gate and the limited answer oracle: they supply repository/environment predicates, not a reference answer for arbitrary user intent (SRC-1, `src/enoch/app/task_workflow.py`; [RT-RTE-task-work](runtime.md#rt-rte-task-work)).

A failed doctor can trigger automatic repair only for nonskipped failed checks in the code-health or environment-readiness categories, within the configured limit (default two, permitted zero through five). Each repair receives the original request/context and failed-check JSON, with diagnostic head/tail truncation, in the same workspace and task session. Only the request ID changes; the original deadline and cancellation controls remain. Doctor then runs again. The model-facing policy explicitly forbids weakening validation:

> "Reuse the existing changes and preserve the original requirements. "
> "Do not remove tests, weaken assertions, skip checks, change ENOCH_TEST_COMMAND, "
> "or disable doctor to obtain a pass. Do not discard the requested implementation. "
> --- `src/enoch/app/validation_repair.py`

This is guidance to the editing model, not enforced test immutability. The runtime's retained doctor-failure passage in [RT-RTE-task-work](runtime.md#rt-rte-task-work) supports the rejection branch: final validation failure preserves the workspace, returns `validation_failed`, and does not enter ordinary review publication. The outcome is permanent and nonretryable for the automatic task runner. A later explicit task retry can inspect/reconcile previous publication evidence and create linked work; it is not evidence that every failed task automatically retries (SRC-1, `src/enoch/app/core.py`, `src/enoch/app/task_workflow.py`). A passing repair that leaves no changes is also rejected for publication.

### Validated change to result

On a pass with remaining changes, the host records validated state and performs [WF-RTE-review-handoff](#wf-rte-review-handoff). This handoff supplies the review adapter with the immutable captured revision, base revision, title, compact doctor evidence and task/workspace metadata. The provider returns review identity, state and optional URL; the host checks these receipts under its remote-review policy. A provider's unconfirmed or local-only result cannot silently satisfy a required remote review. A local capture can be an allowed result when remote review is not required; local capture, published review and landed code are distinct outcomes (SRC-1, `src/enoch/app/review_publication.py`, `src/enoch/app/task_workflow.py`).

Delivery has two boundaries. Artifact delivery means the permitted capture/review handoff has completed and the workflow returns its IDs/stages. Operator reporting means the worker finalizes authoritative task state, updates the status message and calls chat delivery with a task-specific final notification key and attachments. The worker checks authoritative status before reporting and logs the turn. It also calls automatic learning-artifact recording on completed tasks, without this account establishing any improvement from that artifact (SRC-1, `src/enoch/app/core.py`). Neither a completed task nor a chat-send call proves receipt by a live user.

For transient failures, the runner schedules retry only when the failure is retryable and the attempt budget remains. Runtime-access failures pause; timeout fails; non-timeout cancellation cancels. Publication-stage retries differ from editing retries: captured/review-published state selects publication resume rather than another model implementation turn. Some already-recorded result/review branches return completion directly. Consequently the ordinary doctor gate does not establish fresh validation on every resumed or reconciled completion (SRC-1, `src/enoch/app/core.py`, `src/enoch/app/task_workflow.py`).

A remote handoff queues a repository-state note and a clipped activity summary for synchronization to the conversation session. The pending queue is in-process; its flush dispatches the notes with the conversation session key. This gives the foreground conversation selected results, not the worker's complete transcript, diagnostics or file contents. This member inspected that dispatch but not the synchronization helper's internal processing or provider retention, so durable receipt across a crash and later model use remain unestablished (SRC-1, `src/enoch/app/core.py`, `src/enoch/app/task_workflow.py`). The note's policy is explicit:

> "Do not assume the review was landed.",
> f"Do not assume `{resident_workspace}` contains those changes.",
> "Inspect current local state before repository-dependent work.",
> --- `src/enoch/prompt_append.py`

Landing and runtime activation require separate operations, [RT-RTE-software-update](runtime.md#rt-rte-software-update). The selected workflow delivers reviewable work, not automatically deployed self-change.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-review-handoff
Label: Captured revision review handoff

Part of: [RT-RTE-task-work](runtime.md#rt-rte-task-work)

This is the publication/recovery segment of the supplied task route, not a second identity for that whole route. It has separate acceptance checks and a repository-to-review consumer boundary. SRC-1, `src/enoch/app/task_workflow.py`, `src/enoch/app/review_publication.py` supply implementation evidence.

Endpoints/progression: validated workspace → changed-path allowlist check → repository capture → clean captured-revision check → ReviewSubmission → review receipt check → recorded publication stage → workspace/resident handoff → WorkOutcome. Resume enters with retained task publication state and resolves the captured revision rather than recapturing the edit. Owner: TaskWorkflowService/application; repository and review adapters execute covered effects under capability/epoch checks. Context/state: task request, allowed paths, workspace and base revision, captured revision, review ID/URL, task provenance, doctor summary and publication stage. Operating mode: requested product publication with deterministic receipt admission, not a comparative experiment. Proposer: earlier editing model; decider/veto: host predicates and adapter outcomes; human review/landing is later, not implicit in starting this task. Answer oracle: expected review receipt fields for handoff completion; none for overall change quality.

- Immediate return: WorkOutcome with message, completed stages and revision/workspace/review identifiers, or failed/publish-incomplete outcome.
- Later read-back: retained task stage and revision/review identifiers select publication resume on a later attempt; queued activity/handoff notes are dispatched to the conversation session, whose actual retention/use is uninspected.
- Delegated visibility: review adapter receives title, empty body, captured/base revisions, compact doctor evidence and task/workspace/evolution metadata; it does not receive the full editing transcript or raw failed-check history.
- Selection predicate: ordinary new-change branch requires doctor pass and remaining changes; capture requires no unexpected paths; remote-review-required paths require an open/published receipt with identity and URL; resume requires workspace metadata and available clean captured revision.
- Invalidation or expiry: dirty or wrong-revision working copy rejects capture verification/resume; missing captured revision rejects resume; a stored published stage lacking a required URL is downgraded to captured; claim loss while recording publication raises an error.
- Activation or effect: repository capture and review-provider invocation are wired; completed publication does not land code or activate it in the resident agent.
- Evidence limits: implementation only, with no observed provider success; resumed publication relies on stored state and does not rerun doctor here; adapter idempotency, external review availability and eventual chat receipt are not demonstrated.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission rejects unexpected capture paths and verifies the captured revision and clean working copy. These checks govern artifact capture, not earlier model filesystem effects. Review admission rejects a required remote handoff without confirmed publication. The receipt predicate is explicit:

> if not review_was_published(review) or not review.identity.url:
>     return "The review provider did not confirm an open or published review with a review URL."
> --- `src/enoch/app/review_publication.py`

Recovery retains captured state and workspace for publication retry rather than undoing the captured edit. A local-only provider under a remote requirement returns permanent/nonretryable failure; an unconfirmed remote result is transient/retryable. Publication exceptions after stages have completed are classified for retry. Stage recording supplies revision/workspace/review identities for the later attempt, but there is no demonstrated atomic transaction encompassing the remote provider effect and local record. Thus this is staged recovery, not a proved exactly-once review guarantee. SRC-1, `src/enoch/app/task_workflow.py`:

> f"{app.display_name} captured the change but publication is incomplete. "
> f"{problem} The workspace was preserved for publication retry."
> --- `src/enoch/app/task_workflow.py`

What persists is the captured artifact and recorded task publication metadata. Guidance shapes the preceding editing request and later conversation handoff; the publication predicates themselves are executable rules. Remote handoff cleanup does not merge the review. The unchanged resident checkout is a return boundary, not a rollback of all possible model effects.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-work](runtime.md#rt-rte-task-work)

Workflow-specific delegation: a conversation-session snapshot precedes the task-specific runtime session. The selecting model writes the brief, code normalizes/clips it, and the task model sees that selected context plus the original request. Repair retains the task frame and reuses its session; the original conversation frame is not automatically shared. Publication returns explicit artifact receipts and clipped activity/state notes, not a full worker transcript. The account above retains the snapshot and handoff policy passages (SRC-1, `src/enoch/app/core.py`, `src/enoch/app/task_workflow.py`, `src/enoch/prompt_append.py`). This resembles selected inputs entering a separate frame and selected results escaping it, but the analogy does not imply that the provider discards the persistent task session or supports reference-following into its context.

Workflow-specific recovery: doctor rejection is a terminal validation result for automatic retry; repair remains bounded under the same task deadline. Transient publication failures can instead resume from recorded stages through [WF-RTE-review-handoff](#wf-rte-review-handoff). The host separates task-state completion, chat notification, review landing and runtime activation. Existing-review/result reconciliation branches qualify any assertion that every completion performs a fresh doctor run. No supplied trace establishes successful recovery or faithful execution of the repair policy (SRC-1, `src/enoch/app/core.py`, `src/enoch/app/validation_repair.py`, `src/enoch/app/task_workflow.py`).
