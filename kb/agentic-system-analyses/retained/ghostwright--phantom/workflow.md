---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Phantom workflow: agent-authored scheduled work from request and durable handoff through execution, recovery and Slack delivery."
run-id: AAS-2026-10-15-phantom-cc566f03ac40-01
reviewed-boundary: "f8c7ab42d885936ee54abc785528000260f4acc5"
---

# Phantom workflow report

## Workflow account

### Selection and evidence

This account selects **agent-authored scheduled work**: a foreground request leads the agent to create a job; host code later invokes the agent on its stored instruction and delivers the result. This is representative because it crosses the main agent, an in-process tool, durable storage, a timer-owned dispatcher, a later SDK invocation and a channel transport. It exposes a consequential distinction between accepting a job, accepting an execution result and delivering that result. It is not an invented example task or an observed successful run. The source establishes the connected implementation, not whether a model actually created or completed a useful job. [SRC-1: `src/index.ts`, `src/scheduler/tool.ts`, `src/scheduler/service.ts`, `src/scheduler/executor.ts`]

All evidence is from SRC-1 at the boundary's pin. Additional inspection covers the scheduler's tool, types, creation validation, schedule calculations, service, executor, delivery and recovery implementations, plus startup factory and Slack wiring. Tool-description guidance is doctrine/design embedded in implementation; the branches below are implementation evidence. No target code, tests or providers were executed. SDK internals and deployed Slack behavior remain outside the inspected source. The supplied runtime records remain the baseline for foreground execution and dependency controls.

### Request to durable delegation

1. **A foreground agent receives a request.** The channel request path and its lack of a fixed task-correctness oracle are established in [RT-RTE-channel-work](runtime.md#rt-rte-channel-work). Startup supplies a fresh `phantom-scheduler` MCP wrapper for each query around one shared Scheduler. The main model decides whether to invoke `phantom_schedule`; the wrapper is not a planner that automatically converts every request into a job. [SRC-1: `src/index.ts`, `src/scheduler/tool.ts`]
2. **The agent supplies the handoff.** For `create`, it supplies name, schedule and task, with optional description and delivery. The tool instructs it to make the task self-contained. This is instruction guidance, not a check that every necessary URL or requirement was actually copied. The later call uses a different conversation key, `sched:<job.id>`, rather than forwarding the originating conversation. Subsequent fires of that same job can still resume their own SDK session under the runtime's session rules. [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/executor.ts`]; [RT-OBJ-session-store](runtime.md#rt-obj-session-store).
3. **Software admits or rejects the job.** [WF-RTE-job-creation](#wf-rte-job-creation) checks structure and schedulability, then retains [WF-OBJ-scheduled-job](#wf-obj-scheduled-job). Creation returns `created`, ID, schedule, next run time and delivery to the calling agent. That is acknowledgment of durable delegation, not the future task's answer. There is no compulsory per-job human approval in this tool path. [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/service.ts`, `src/scheduler/create-validation.ts`]

The handoff's intended context boundary is explicit:

> When creating a task, write the task prompt as a complete, self-contained instruction. Include every piece of context the scheduled run will need; it will NOT have access to the current conversation history.
> --- `src/scheduler/tool.ts`

This resembles an isolated work frame only in selecting the input to a later invocation. It is not a subordinate context popped on return: the durable job and its independent SDK session can survive and recur. The outer caller receives creation metadata immediately; the later execution returns through scheduler delivery, not by rejoining the originating model frame. [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/service.ts`, `src/scheduler/executor.ts`]

### Due job to result

4. **Code owns the next start.** Startup connects Slack when available and starts the Scheduler. Its timer selects enabled active rows ordered by due time; a single `executing` flag serializes scheduler execution within this instance. Each due job calls the executor, which checks whether that job's runtime session is already busy. A busy job returns an empty string without advancing its row. Neither guard is a distributed claim/lease. [SRC-1: `src/index.ts`, `src/scheduler/service.ts`, `src/scheduler/executor.ts`]
5. **The SDK/model owns task execution.** The executor calls `handleMessage("scheduler", "sched:<id>", job.task)`. The main runtime supplies its assembled prompt, available tools and session handling; the SDK/model chooses tool progression. Exact dependency subagent handoffs remain uninspected. Scheduled work goes directly to the runtime, not through the channel callback's learning submissions. These mechanisms belong to [RT-RTE-direct-work](runtime.md#rt-rte-direct-work), with workflow-specific annotations below. [SRC-1: `src/scheduler/executor.ts`]
6. **The executor accepts a conventional result, not verified task correctness.** It treats a thrown error or text beginning `Error:` as execution failure. Otherwise it marks the run `ok`; no independent review agent or expected-answer comparison is called by this executor. Thus an incorrect but ordinary-looking answer can pass, and an answer beginning with that prefix is classified as an error. This is a code-level interpretation of the convention, not an observed misclassification. [SRC-1: `src/scheduler/executor.ts`]

> if (responseText.startsWith("Error:")) {
> runStatus = "error";
> errorMsg = responseText;
> }
> --- `src/scheduler/executor.ts`

### Delivery, rejection and recovery

7. **Transport outcome is separate from run outcome.** Only an `ok` run with nonempty text calls `deliverResult`. Silent delivery returns `skipped:channel_none`; Slack delivery resolves `owner`, channel ID or user ID. Missing transport/owner produces a dropped outcome. Null Slack responses or exceptions produce an error outcome. `delivered` means the transport call returned a non-null value, not that a human read the answer or the task was correct. [SRC-1: `src/scheduler/delivery.ts`, `src/scheduler/executor.ts`]

> const ts = await ctx.slackChannel.postToChannel(target, text);
> if (ts === null) {
> console.error(
> `[scheduler] Delivery error for job "${job.name}" target=${target}: Slack postToChannel returned null (upstream API failure)`,
> );
> return "error:slack_returned_null";
> }
> return "delivered";
> --- `src/scheduler/delivery.ts`

8. **Run failures drive retries; delivery failures do not.** Error runs increment consecutive errors and choose backoff, capped at an hour; cron uses the earlier of backoff and its next regular fire. One-shots become failed after three consecutive errors; the general threshold is ten, with an owner-notification attempt. Success resets errors and advances recurrence or completes the one-shot. A successful `deleteAfterRun` job is deleted after the update even if Slack delivery dropped or failed. Therefore task completion does not guarantee delivery, and the inspected executor has no delivery-only retry. This is a bounded branch finding, not a claim about all possible agent-authored recovery tools. [SRC-1: `src/scheduler/executor.ts`, `src/scheduler/schedule.ts`, `src/scheduler/service.ts`]

> if (newStatus === "completed" && job.deleteAfterRun) {
> ctx.db.run("DELETE FROM scheduled_jobs WHERE id = ?", [job.id]);
> }
> --- `src/scheduler/executor.ts`

Creation rejection is earlier: validation runs before insertion, and the tool catches errors and returns `isError: true`. The proposing model can revise its call, but automatic repair is not implemented by the wrapper. At service restart, past-due active rows are staggered five seconds apart and re-enter ordinary dispatch. That recovers eligibility, not interrupted reasoning or exactly-once effects. Delivery precedes the row update; tool effects can precede both. The inspected sequence therefore does not supply an atomic transaction joining external effects, Slack send and completion bookkeeping. No generic rollback of completed task effects is present in this executor. [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/service.ts`, `src/scheduler/recovery.ts`, `src/scheduler/executor.ts`]

The narrow terminal conditions are consequently: creation acknowledgment for the originating agent; run result/status for the scheduler; and a separate transport outcome for the configured recipient. Their wiring is established, while successful execution, recovery effectiveness and delivery in a deployment remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

#### WF-OBJ-scheduled-job
Label: Scheduled job

Source-native identity: `ScheduledJob` / SQLite `scheduled_jobs`. The task is natural-language instruction consumed by a later main-agent invocation. Schedule, enabled/status fields, delivery target, counters and timestamps are symbolic values consumed by scheduler code. Storage substrate: a SQLite row, reconstructed into a transient typed object. Unlike [RT-OBJ-session-store](runtime.md#rt-obj-session-store), it retains a task and dispatch policy, not the mapping to an SDK conversation. It is neither the MCP `tasks` table discussed in [RT-ABS-task-executor](runtime.md#rt-abs-task-executor) nor [RT-OBJ-dynamic-tools](runtime.md#rt-obj-dynamic-tools): it schedules existing runtime capacity rather than registering executable handler code. [SRC-1: `src/scheduler/types.ts`, `src/scheduler/service.ts`, `src/scheduler/executor.ts`]

> task: row.task,
> --- `src/scheduler/row-mapper.ts`

### Routes

#### WF-RTE-job-creation
Label: Scheduled job creation

Endpoints/progression: main agent's `phantom_schedule` create call → required-field/schema checks → `validateCreateInput` → next-fire computation → SQLite insertion → timer rearm → metadata return. Owner: proposing model chooses instruction/schedule; tool and Scheduler decide structural admission. Context crossing the boundary is selected task text and job metadata, not the originating transcript. The durable result is [WF-OBJ-scheduled-job](#wf-obj-scheduled-job). This precedes the scheduler execution branch of [RT-RTE-direct-work](runtime.md#rt-rte-direct-work); it is not that existing execution route or the dynamic-handler registration route [RT-RTE-dynamic-tools](runtime.md#rt-rte-dynamic-tools). [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/service.ts`, `src/scheduler/create-validation.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON text containing created flag, job ID, name, schedule, next run and delivery; validation exceptions become tool errors.
- Later read-back: scheduler reloads stored instruction/schedule for future dispatch; list exposes status and delivery metadata to later calls.
- Delegated visibility: later runtime receives job.task under its separate scheduler conversation key, plus its own assembled prompt/session state; original request context must be copied deliberately.
- Selection predicate: create action with required name/schedule/task; job count below 1,000, task at most 32 KiB UTF-8, case-insensitively unique name, valid future schedule and valid Slack target when applicable.
- Invalidation or expiry: delete removes the job; pause excludes it from dispatch; successful one-shots created by this tool use deleteAfterRun; terminal failures and cleanup follow scheduler lifecycle.
- Activation or effect: insertion and timer rearm are wired; execution and usefulness of the generated instruction are unobserved.
- Evidence limits: shape/schedule validation does not establish context completeness, task safety or correctness; no per-content human approval or independent task-answer oracle is supplied by this create path.

Trigger/change: the model proposes future work in response to an open request. Tool description shapes the proposal by requesting a self-contained instruction and explaining schedules/delivery. Software can veto invalid inputs; it does not semantically evaluate the proposed task. What persists is the job instruction and dispatch metadata. Recovery from rejection is caller revision; delete/pause can withdraw future dispatch but do not undo past task effects. This admits future work, not necessarily a change to Phantom's own policy or capability. [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/create-validation.ts`, `src/scheduler/service.ts`]

> const scheduleError = validateSchedule(input.schedule);
> if (scheduleError) {
> throw new Error(`invalid schedule: ${scheduleError}`);
> }
> --- `src/scheduler/create-validation.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-direct-work](runtime.md#rt-rte-direct-work)

Workflow-specific scheduler finding: outer next-step ownership moves from the originating agent to timer code, then to SDK/model execution, then back to executor delivery/bookkeeping. The self-contained job instruction is the handoff contract, not enforced context completeness. Acceptance uses exception/`Error:` classification rather than an independent answer oracle. Delivery has its own success/drop/error outcome and does not veto completion or trigger execution retry. Run-error backoff and restart staggering are distinct recovery mechanisms; neither rolls back external task effects. Scheduler serialization is instance-local. [SRC-1: `src/scheduler/tool.ts`, `src/scheduler/service.ts`, `src/scheduler/executor.ts`, `src/scheduler/delivery.ts`, `src/scheduler/recovery.ts`]

The timer completion callback classifies returned text with the same prefix convention; a busy-session empty return is consequently reported as `completed` by that callback despite leaving the job row unchanged. Callback completion is therefore not stronger verification than the executor result. [SRC-1: `src/scheduler/service.ts`, `src/scheduler/executor.ts`]

> const result = await this.runExecutor(job);
> const status = result.startsWith("Error:") ? "error" : "completed";
> this.fireJobCompleteCallbacks(job.name, status);
> --- `src/scheduler/service.ts`
