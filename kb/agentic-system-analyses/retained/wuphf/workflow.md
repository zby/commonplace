---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Wuphf workflow account: scheduled app routine, tool authoring and verification, gated execution, and recorded delivery."
run-id: AAS-2026-10-15-wuphf-b246722f99c0-01
reviewed-boundary: "88023d4dac7491b6e71dbc1e86d274c435b9cb2c"
---

# Wuphf workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a scheduled custom-app routine: a due broker job delegates its prompt to the agent service, which selects or authors a saved tool, executes it, and returns a recorded outcome. This is selected because the shipped producer and consumer form one inspectable multi-step path, including code admission, an execution rejection branch and delivery back to the broker. It is not a hypothetical combination of unrelated office-agent features. Its canonical identity is [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool); the authoring and execution handoffs use [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring) and [RT-RTE-saved-call](runtime.md#rt-rte-saved-call). The latter records supply mechanisms, not an assertion that a routine traverses the manual HTTP endpoints.

All findings concern SRC-1 implementation at the boundary's frozen commit. The repository calls the product gawkbot. No workflow execution, test, model call or service was run, and no supplied execution trace establishes successful delivery or business benefit. The boundary remains complete artifact, partial loop. This account inspects `internal/team/scheduler_operator_routines.go`, `agent/src/routineRunner.ts`, `agent/src/sessions.ts`, and selected portions of `agent/src/service.ts`, `agent/src/tools.ts`, `agent/src/toolRuntime.ts`, `web/src/appdetail/bots/botStateClient.ts` and `web/src/appdetail/artifacts/ArtifactsTab.tsx`. These are implementation evidence, not observed operation. Full frontend orchestration, downstream human-approval execution and external capability implementations are not established by this selective trace.

### 1. The broker supplies the work and controls recurrence

The starting condition is a due custom-app scheduler job. The broker chooses the current live playbook prompt when available, otherwise the job payload, then the job label. A missing prompt yields a failed run without dispatch. App ID identifies the capability/data scope; routine slug identifies the schedule and session association; the label supplies the display name. These identities are not interchangeable with a saved tool name or returned session ID. SRC-1, `internal/team/scheduler_operator_routines.go`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).

The broker re-arms the next run before starting asynchronous HTTP dispatch. This avoids repeatedly firing the same due timestamp while the call is outstanding; it does not establish single-flight execution across later due times. The POST supplies schema version, app ID as `agent`, slug, name and prompt. The HTTP round trip has a 90-second deadline. The inspected caller does not attach the sidecar's optional bearer authorization, so authenticated sidecar configuration can reject the handoff before tool execution. That baseline limit is material: this source trace is not proof that the default supervised deployment completes routines. SRC-1, `internal/team/scheduler_operator_routines.go`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).

### 2. The service delegates selection to rules, and authorship to a model when configured

The service checks nonempty string slug, name and prompt, resolves the authoring backend and fetches the app's table schema before calling the routine runner. The runner first searches that app's saved tools. An exact mention of callable name or full title wins; otherwise the strongest title-word overlap needs at least two words. This is lexical selection, not model review of whether the saved tool implements the current prompt. A match goes directly to execution; a changed playbook prompt does not itself force re-authoring. SRC-1, `agent/src/service.ts`, `agent/src/routineRunner.ts`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).

If nothing matches, the service's author callback invokes `buildTool` with the routine prompt, app schema and resolved model configuration. The model receives capability/schema guidance and proposes executable tool code; fixed software rules own acceptance. It is an open requested workflow, not a curriculum with expected business answers. The human's earlier routine definition is not per-code approval. Author-model identity and mutability are recorded in [RT-CMP-author-model](runtime.md#rt-cmp-author-model); guidance in [RT-OBJ-tool-schema](runtime.md#rt-obj-tool-schema).

### 3. Verification can reject code, but does not verify the business result

For newly model-authored code, a static capability-reference check precedes one simulated smoke execution with placeholder arguments. Selected crash strings trigger one model repair request containing the original brief and the crash message. A second detected crash causes fallback; model/parse/validation failure can also fall through to a deterministic stub. Neither smoke success nor fallback establishes that the user's workflow is correctly implemented. The smoke check has no reference business outcome, and successful saved-tool matching bypasses this fresh authoring loop. SRC-1, `agent/src/tools.ts`; [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).

The routine runner persists any returned non-null tool. This differs from the manual build endpoint's model-provenance admission condition: a fallback tool can become durable routine behavior. The code, metadata and version persist, not the smoke transcript or model rationale. Subsequent calls can select the saved code; the authoring repair loop is not a demonstrated trace-driven improvement loop across routine runs. SRC-1, `agent/src/routineRunner.ts`; [RT-OBJ-stored-tool](runtime.md#rt-obj-stored-tool), [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).

### 4. Execution delegates capability sequencing to code, not to a conversational planner

The runner invokes the selected tool with the routine prompt under the argument name `input`, app-scoped capabilities, and `approved: false`. Tools declaring other parameter names do not thereby receive extracted values for those names. The worker's generated JavaScript owns capability sequence and arguments; the host dispatcher owns the available functions and named approval checks. Model-dependent capability calls are separate invocations rather than continuation of an authoring conversation. The stored routine session is an output transcript, not the history supplied to this executor. SRC-1, `agent/src/routineRunner.ts`, `agent/src/toolRuntime.ts`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool), [RT-RTE-saved-call](runtime.md#rt-rte-saved-call), [RT-CMP-runtime-ai](runtime.md#rt-cmp-runtime-ai).

The host gate covers named send/browser capabilities, not every possible state change. Permitted app data changes may occur first; integration mutation deferral uses a separate broker path. Worker termination and abort signaling cannot undo effects already completed. These restrictions prevent equating `approved: false` with a general read-only transaction or universal human authorization. SRC-1, `agent/src/toolRuntime.ts`; [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).

### 5. Rejection terminates the worker; “paused” is an outcome, not a saved continuation

The inspected send-gate rejection is consequential. A `GateError` settles the execution as `needs_approval`. The common settlement function aborts the host signal, terminates the worker and resolves the result. Thus the runner's later phrase “paused for your approval” does not establish a suspended program counter that can resume after approval. The inspected routine runner has no approval-answer/resume input. A downstream human action or manual rerun is outside this traced segment; it must not be invented as the next guaranteed step. SRC-1, `agent/src/toolRuntime.ts`, `agent/src/routineRunner.ts`.

> if (e instanceof GateError) {
> finish({ status: "needs_approval", gate: { capability: e.capability, detail: e.detail }, actions: ctx.actions });
> return;
> }
> --- `agent/src/toolRuntime.ts`

> runCtrl.abort(new Error(`tool run settled (${r.status})`));
> worker.terminate();
> resolve(r);
> --- `agent/src/toolRuntime.ts`

Timeout and worker errors also settle execution. The broker records transport failures and explicit error outcomes as failed runs, but keeps the recurring job scheduled. This is continued scheduling, not compensation, automatic repair of the saved tool or exactly-once recovery. A 90-second caller timeout can precede the ordinary worker's 120-second default deadline. SRC-1, `internal/team/scheduler_operator_routines.go`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool), [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).

### 6. Delivery means a retained outcome and broker acknowledgement, not necessarily a completed action

After an ordinary returned execution result, the runner ensures an app/routine-slug session, appends the scheduled prompt and outcome, writes a Markdown artifact and returns status, outcome and session. The service projects these to `status`, `digest` and `session_id`. The transcript stores outcome text, not the entire worker capability trace. An exception before these writes can bypass them; the header's “ALWAYS” comment is not an unconditional durability guarantee. SRC-1, `agent/src/routineRunner.ts`, `agent/src/service.ts`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).

The session adapter appends the tool-produced outcome as an assistant message labelled `model: "tool-runner"`, with zero usage. That label does not show another model checked or composed the final answer. Its reader converts retained user/assistant entries back into frontend messages. The service exposes session and artifact GET routes; the frontend client requests those routes, and the artifact viewer can display Markdown content as text. This establishes a shipped retrieval and presentation path, not that a human opened the result. SRC-1, `agent/src/sessions.ts`, `agent/src/service.ts`, `web/src/appdetail/bots/botStateClient.ts`, `web/src/appdetail/artifacts/ArtifactsTab.tsx`.

> return { session: meta, messages: sm.getEntries().flatMap(entryToMessage) };
> --- `agent/src/sessions.ts`

> <pre className="opr-artifact-md">
> <code>{artifact.content ?? ""}</code>
> </pre>
> --- `web/src/appdetail/artifacts/ArtifactsTab.tsx`

The broker maps `needs_approval` to an `ok` scheduler fire with a paused summary, while recording a partial playbook outcome. Other successful responses get a success outcome; transport and explicit execution errors get an aborted outcome. The recurrence stays scheduled. Therefore delivery has separate meanings: an outcome can be recorded and returned successfully while the requested send remains unperformed. Integration deferral can even be ordinary tool result text rather than `needs_approval`, so overall success is not a business-completion oracle. SRC-1, `internal/team/scheduler_operator_routines.go`; [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool), [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).

> if strings.HasPrefix(run.OutputSummary, "Paused for approval") {
> outcome = PlaybookOutcomePartial
> } else {
> outcome = PlaybookOutcomeSuccess
> }
> --- `internal/team/scheduler_operator_routines.go`

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

#### On [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool)

Workflow delivery criterion: the sidecar records an ordinary returned outcome in the routine session and Markdown artifact and supplies the broker with status/digest/session ID. The broker's run ring and partial/success/aborted playbook result distinguish dispatch completion from requested-action completion. Retrieval routes and frontend presentation support operator access, not observed receipt. The account above retains the additional source evidence for that distinction.

Workflow recovery limit: a later scheduled fire can reuse the persisted tool without fresh authoring verification. Re-arming the schedule does not resume a terminated worker, compensate earlier effects or prove non-overlap with the next due time.

#### On [RT-RTE-saved-call](runtime.md#rt-rte-saved-call)

Workflow rejection semantics: the shared worker executor's gate rejection terminates the worker through the common settlement function. The routine's “paused” narration is a terminal returned status for that invocation, not evidence of a resumable worker continuation. The account above retains the gate and settlement passages. This concerns the executor reused by routines; it does not assert a scheduled call traverses the manual saved-call HTTP handler.
