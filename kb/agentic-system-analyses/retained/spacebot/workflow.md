---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Spacebot workflow account: task-bound built-in worker delegation, durable completion admission and conversational delivery."
run-id: AAS-2026-10-14-spacebot-6a954b400f95-01
reviewed-boundary: "5c2ee47b397e09c956dc15000ea576ecd28e92bb"
---

# Spacebot workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a user-channel request that the channel delegates to a **task-bound, noninteractive built-in worker**, followed by completion processing and a user-facing relay. It was selected because it exposes three distinct decisions: whether execution may begin, whether a completion event is authoritative, and what the user receives. This is an implemented conditional path, not a reconstruction of an observed task. No particular request, generated work product, external delivery receipt or successful execution was supplied. The [boundary](boundary.md#boundary-and-evidence) fixes SRC-1; implementation wiring does not establish reliability or model compliance.

The baseline records are [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn) and [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work). Additional inspection of SRC-1 covered selected bodies of `src/tools/spawn_worker.rs` (task-plan resolution and spawn preparation), `src/agent/channel_dispatch.rs` (completion classification, finalization and bounded commit retries), `src/agent/worker.rs` (wall-clock timeout), and `src/agent/channel.rs` (durable event validation, result queuing, retrigger construction and fallback delivery). These supply implementation evidence. Selected text in `prompts/en/worker.md.j2` supplies doctrine/design only. No new source or execution evidence is introduced.

### 1. Request becomes an execution proposal

Main resolves the inbound agent/conversation and sends the request to its channel. The channel owns the conversational loop; its model decides whether to reply directly or invoke delegation under the runtime's offered tools. The request, current conversation history and rendered task/skill context inform that choice. These inputs do not themselves approve a specific worker action ([RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn); SRC-1, `src/main.rs`, `src/agent/channel.rs`).

For the selected path, the model calls `spawn_worker` with `task_number`. Rust loads the authoritative task and resolves its project execution defaults. Ready and InProgress are admitted statuses; PendingApproval and Backlog are rejected, as are terminal tasks. A live attempt or a failure to inspect live attempts also blocks spawning. Required skill names must resolve before the worker can start. The task-bound plan's worker type wins over a conflicting tool argument (SRC-1, `src/tools/spawn_worker.rs`). The computational contribution is a work proposal and subsequent execution. The upstream task state represents approval; the source does not establish who approved a particular task or that every tool action receives human review. Reference-only and unbound spawns are different paths, as the runtime record establishes.

> "task #{number} is {} — it must be approved (ready) before work starts",
> --- `src/tools/spawn_worker.rs`

> // A required skill that doesn't resolve would be silently absent from
> // the worker's contract — fail the spawn instead.
> --- `src/tools/spawn_worker.rs`

This admission checks permission and input availability, not whether the proposed method will solve the user's problem. There is no expected-answer oracle in this open-request workflow ([RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work)).

### 2. Handoff supplies a private worker contract

Spawn preparation creates a worker identity and supplies the task string, authoritative task context, required skill bodies, suggested skill hints and the configured clean or forked history. Required instruction delivery is not obedience. Clean history keeps channel turns out; forked history is a copy under the worker's own preamble and can be reduced before inference. The worker receives its own ToolServer rather than the caller's full capability set ([RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work), [RT-CLM-required-skills](runtime.md#rt-clm-required-skills), [RT-RTE-context-control](runtime.md#rt-rte-context-control); SRC-1, `src/tools/spawn_worker.rs`, `src/agent/channel_dispatch.rs`).

Before binding the task, code checks that the prepared worker is still starting and records a task attempt keyed by worker ID. Failure to claim that attempt fails the prepared worker before start. Cancellation after the claim attempts to close the attempt as Interrupted. Thus a model's spawn request is not sufficient to launch the task; preparation, durable claim and binding can reject it (SRC-1, `src/tools/spawn_worker.rs`).

> .fail_before_start("task attempt could not be claimed")
> --- `src/tools/spawn_worker.rs`

The worker prompt asks the worker to execute all task steps and report a terminal outcome only when complete. That is an instruction to the executing model, not an independent inspection of its work product (SRC-1, `prompts/en/worker.md.j2`).

> **CRITICAL: Do not signal an outcome until every step of the task is actually complete.** If the task has multiple steps, you must finish ALL of them before calling `set_status(kind: "outcome")`. Signaling an outcome after completing only some steps is a failure — it tells the channel the work is done when it isn't. Review your original task description and verify every requirement has been met before signaling.
> --- `prompts/en/worker.md.j2`

### 3. Worker execution and bounded recovery

The worker owns its private model/tool loop while dispatch supervision owns lifecycle completion. Its granted tools can affect files, subprocesses or external services; a final response is not a transaction that rolls those effects back. Tool topology and configured containment have the limits retained in [RT-CLM-role-grants](runtime.md#rt-clm-role-grants). The private transcript is not wholesale merged into the channel ([RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work)).

Worker segmentation can yield a partial result rather than full completion. On wall-clock expiry, the wrapper recovers available output through hook/transcript handles and returns a Timeout outcome with segment count. It does not restart the task or establish restoration of external effects. A first-segment timeout can lack useful recovered content; successful recovery of a particular task remains unobserved (SRC-1, `src/agent/worker.rs`; [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work)).

> let result = recover_timed_out_result(&hook, &transcript_tracker);
> --- `src/agent/worker.rs`

Dispatch classifies Success, Partial, Cancelled, Timeout, Blocked and Failed outcomes separately. A partial result includes its segment-limit warning rather than being rewritten into a complete answer (SRC-1, `src/agent/channel_dispatch.rs`). These terminal categories are runtime outcomes, not independently verified correctness judgments.

### 4. Commit precedes authoritative completion consumption

The dispatch finalizer attempts a bounded durable terminal commit before emitting its normal WorkerComplete event. It also attempts to record the task-attempt outcome, removes the matching live registration and wakes terminal waiters. Task-attempt persistence can fail independently. If terminal commit remains unavailable or errors after retries, it logs that failure and does not emit the normal completion event. Even the successful event send discards its send error. This is an ordering protocol, not guaranteed eventual notification ([RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work); SRC-1, `src/agent/channel_dispatch.rs`).

The channel does not simply trust event text. It rereads the durable terminal result and checks outcome version, transcript version, outcome kind and terminal owner. Already-consumed versions are ignored. Missing or mismatching durable outcomes are rejected before result queuing. [WF-RTE-completion-admission](#wf-rte-completion-admission) records this distinct consumer-side admission step. This verifies identity and consistency, not the substantive truth of a worker's answer.

### 5. Result becomes a new channel decision, then outbound text

With `notify` enabled, the accepted durable result enters `pending_results` with process ID and success flag. The channel builds a synthetic system retrigger containing those results. The result is therefore supplied to another model invocation for follow-up or relay, not returned directly as the full private transcript. Template-render failures and a full self-queue retain pending results and schedule retries. A missing conversation ID or closed queue drops pending results. Queue acceptance clears them; it is not a user delivery receipt (SRC-1, `src/agent/channel.rs`; [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn)).

> /// Results are drained only after the synthetic message is queued
> /// successfully. On transient failures, retrigger state is kept and retried
> /// so background results are not silently lost.
> --- `src/agent/channel.rs`

The channel model decides what to say or do next. Explicit reply tools and guarded plaintext fallback can send user-facing text. Fallback checks can reject structured/tool syntax or secret patterns; some adapters require an explicit reply. A skipped retrigger with no text can leave the result unrelayed. The local delivery step is outbound routing, not worker termination, durable commitment or retrigger enqueue. Main's adapter/SSE forwarding is a further boundary; no supplied platform receipt establishes actual user receipt ([RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn); SRC-1, `src/agent/channel.rs`, `src/main.rs`).

> "LLM skipped on retrigger with no text — worker/branch result may not have been relayed"
> --- `src/agent/channel.rs`

The workflow therefore ends in a conditionally routed result, not a guaranteed verified product. The task admission gate, durable-completion check and outbound filters each reject different things. None is an answer oracle, and none establishes that all user requirements were met. Failures are owned locally: spawn preparation refuses admission, the worker wrapper preserves available timeout output, dispatch retries terminal persistence, and the channel retries some retrigger failures. A universal automatic repair/re-execution or rollback of work effects is not established by this selected trace.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-completion-admission
Label: Worker completion admission

Part of: [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work)

This is the consumer-side completion admission subroute of the runtime's broader delegation/return route, not a duplicate declaration of the worker loop. Endpoints/progression: WorkerComplete event → channel deduplication → durable terminal read → version/kind/owner agreement → consumed-version marker → optional pending-result queue. The channel's Rust handler owns this decision. Context is symbolic worker IDs and terminal metadata in the event and process-run store; the natural-language result becomes eligible for later model relay only after admission (SRC-1, `src/agent/channel.rs`).

The producer proposes a completion notification; code accepts or rejects it. No human decision or expected-answer oracle participates in this check. Mode is open-work lifecycle handling. Trigger is a worker completion event; the admitted material is the committed terminal result, not a validated revision of the external work product. Rejection ability covers duplicates, unavailable durable outcomes and inconsistent metadata. A read error propagates. This body does not establish automatic repair of mismatches or rollback of work effects.

- Immediate return: duplicate, missing or mismatching events return without queuing a result; a matching event marks its outcome version consumed and queues the durable result when notify is enabled.
- Later read-back: the channel rereads the terminal result retained by dispatch; subsequent retrigger inference receives the admitted result, while process logging separately retains transcripts for later inspection.
- Delegated visibility: the parent receives terminal result text and metadata, not the worker's full private model/tool history.
- Selection predicate: worker ID, not-yet-consumed outcome version, and agreement on outcome version, transcript version, outcome kind and terminal owner.
- Invalidation or expiry: an already-consumed version cannot be queued twice through this handler; disagreement with the durable terminal prevents admission. No retention expiry is established by this body.
- Activation or effect: symbolic checks govern result queuing; the result can then influence a channel retrigger, but content-dependent behavior and user receipt are unobserved.
- Evidence limits: implementation only; no duplicated event, storage failure, mismatch, model relay or platform receipt was observed. Consistency is not semantic correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if terminal.outcome_version != *outcome_version
>     || terminal.transcript_version != *transcript_version
>     || terminal.outcome_kind != *outcome_kind
>     || terminal.terminal_owner != *terminal_owner
> --- `src/agent/channel.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work)

Workflow-specific acceptance distinction: task-bound execution permission is checked before work; terminal persistence and [WF-RTE-completion-admission](#wf-rte-completion-admission) check lifecycle authority afterward. Neither accepts the work product against the user's substantive requirements. The parent channel remains responsible for interpretation and possible relay. The selected noninteractive built-in path does not establish the behavior of interactive resumption, OpenCode, autonomous epochs or branch-to-worker delegation.

#### On [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn)

Workflow-specific delivery distinction: worker completion, admission into pending results and successful synthetic-message enqueue are intermediate states. A later channel turn must produce permitted user-facing output and route it outward. Guarded fallback can help relay a result but cannot guarantee it; local routing success is also distinct from adapter delivery and user receipt. No supplied execution evidence closes those boundaries.
