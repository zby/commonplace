---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "oh-my-pi workflow: a blocking delegated coding task, child completion checks and bounded return to the parent at the frozen commit"
run-id: AAS-2026-10-14-oh-my-pi-c0ffc54ff768-01
reviewed-boundary: "2431e8a8716a4da73ae327a412f6d54c22f681e5"
---

# oh-my-pi workflow report

## Workflow account

### Selection and evidence boundary

This account selects an ordinary coding request whose foreground agent delegates a **blocking, non-isolated child task with structured completion enabled**. It is representative of an explicitly shipped task-tool path, not a claim about the most frequent user configuration. It exposes a consequential boundary: the child can do multi-step work in its own conversation, but the parent receives a finalized result, not every child turn. The task tool, structured-subagent facade and executor form a connected implementation chain (SRC-1, `packages/coding-agent/src/task/index.ts`, `packages/coding-agent/src/task/structured-subagent.ts`, `packages/coding-agent/src/task/executor.ts`). No particular task, target run or successful patch was observed.

The [boundary](boundary.md) remains complete artifact, partial loop. This member adds implementation inspection of task spawn arguments, executor completion/reminder/quiescence branches, output finalization and artifacts, the structured-subagent facade, result summary renderer and its shipped template. All are SRC-1 at the shared commit. It does not establish full isolation/merge behavior, speculative task launch, every async task-delivery mode, persisted revival, provider reliability or deployment policy.

### Request and delegation

The caller gives the foreground session a coding request. The shipped print/session/model/tool loop admits it and returns tool results for further model decisions; its terminal text or JSON surface is described in [RT-RTE-session-turn](runtime.md#rt-rte-session-turn). The foreground model may propose a task call. Ordinary dispatch validation and approval can reject that call before the executor runs; those are executable-admissibility checks, not a task-correctness oracle ([RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch)). Starting the session does not establish human approval of each child instruction or edit.

The task tool hands the structured-subagent facade an assignment, optional batch context, agent selection, result parameters, effort, parent call ID, runtime limit and signal. Shared `context` is forwarded only with batch mode enabled. The facade resolves policy and an artifact lease, allocates the child ID, and builds executor options. Its options pass selected context files, skills, rules, prompt templates and extension resources rather than copying the entire parent transcript. In particular the forwarded context-file list filters out files named `agents.md`; this is a forwarding rule, not a claim that no other child instruction-discovery path can supply such instructions (SRC-1, `packages/coding-agent/src/task/index.ts`, `packages/coding-agent/src/task/structured-subagent.ts`).

> contextFiles: session.contextFiles?.filter(file => path.basename(file.path).toLowerCase() !== "agents.md"),
> --- `packages/coding-agent/src/task/structured-subagent.ts`

The executor creates a child AgentSession with agent instructions, selected context, optional plan reference, worktree field and schema information. The runtime baseline establishes this separate-session construction in [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn). For the selected non-isolated path, the facade directly calls the executor, rather than invoking isolation preparation and automatic merge:

> if (!isolationContext) {
> result = await runSubprocess(baseOptions);
> onSubprocessResult?.(result);
> } else {
> --- `packages/coding-agent/src/task/structured-subagent.ts`

The child model chooses intermediate actions within its granted tools. The parent need not ingest the child's complete working history. This separates conversations, not filesystem effects: the selected path does not place child edits in a disposable worktree. Generic reversal of those edits is not supplied by task-result rejection ([RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn), [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch)).

### Completion is a scheduling and format decision

Child completion has two distinct checks. First the executor drives the child prompt and waits for it to settle. If structured work stops without a yield, code sends bounded reminders, with a named yield tool choice on the final attempt where supported. A model terminal error stops this reminder ladder rather than multiplying the failing request. Prompt drops before provider dispatch have their own bounded retries; a busy session can use a caller-supplied recovery hook. These recover scheduling and submission, not arbitrary project mutations (SRC-1, `packages/coding-agent/src/task/executor.ts`; [WF-RTE-completion-barrier](#wf-rte-completion-barrier)).

A yield is not automatically terminal when owner background work is pending. Code settles that work; newly delivered results can invalidate the old yield and require a refreshed one. If no refresh arrives, the executor returns failure while preserving salvage output. This is stronger than merely waiting for a child to print a completion marker, but does not show that the refreshed answer semantically accounts for all results.

Second, output finalization assembles yield data and applies the selected schema policy. Strict mode turns schema failure into a nonzero exit. Permissive mode is not synonymous with unconditional acceptance: validation failures can still reject, while an explicitly schema-overridden submission can be accepted with a warning. Without a yield, valid JSON fallback may supply completion; missing required structured completion can fail. These checks distinguish runnable/deliverable structure from correct code or a verified solution (SRC-1, `packages/coding-agent/src/task/executor.ts`; [WF-RTE-output-finalization](#wf-rte-output-finalization)).

### Return, delivery and recovery owner

The executor finalizes before tail truncation and artifact writing. It can write the untruncated output and structured sidecar, while the returned `SingleResult` has bounded output. The task tool renders a model-facing envelope with status, preview or output, error/abort information and, where available, an `agent://` pointer. The summary has a second inline budget of 5,000 characters; larger results with an output path use a head preview of the already-returned output. Therefore the parent is not guaranteed a verbatim prefix of the raw child artifact or the full child's reasoning (SRC-1, `packages/coding-agent/src/task/executor.ts`, `packages/coding-agent/src/task/result-summary.ts`; [WF-RTE-result-delivery](#wf-rte-result-delivery)).

The facade can remove temporary artifacts after completion. A pointer-shaped envelope alone is not evidence of durable accessibility; artifact lease and retention conditions matter. The selected blocking path does not automatically retain temporary artifacts merely because a child completed. Actual later retrieval was not inspected or observed (SRC-1, `packages/coding-agent/src/task/structured-subagent.ts`).

The parent receives the tool result into its model/tool loop and can decide what to do next; the loop, not the child, delivers the caller's eventual answer ([RT-RTE-session-turn](runtime.md#rt-rte-session-turn)). Child completion is delivery to the parent, not semantic acceptance of a patch by the user. The inspected task path wires no expected-answer comparison or mandatory test-success gate. Tests, review or further delegation may be proposed by a model, but no observed or universally required verification sequence is established here. The parent/caller owns any subsequent semantic recovery after a failed result; the executor owns its bounded dispatch/reminder/barrier recovery. No general rollback of non-isolated child effects follows from either.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-completion-barrier
Label: Completion barrier

Part of: [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn)

This is the executor's run-to-completion scheduling part, not a second declaration of child construction. Endpoints: assignment dispatch → idle/reminder ladder → owner async-work settlement → fresh terminal yield or failed run. Owner: executor run driver and its monitor; child model proposes yield, code decides whether pending work allows termination. Context/state: child session, yield state, abort/budget flags and owner job results. SRC-1, `packages/coding-agent/src/task/executor.ts`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: run termination state, exit/error and monitor output for finalization; stale yields can remain salvage on failure.
- Later read-back: inapplicable — this scheduling check itself produces current-run control state, not a retained content write; downstream artifacts belong to result delivery.
- Delegated visibility: owner job results are settled into the child before a fresh completion is sought; parent sees the finalized result, not barrier internals.
- Selection predicate: structured child without accepted current yield enters reminders; pending owner work triggers settlement rather than treating an earlier yield as terminal.
- Invalidation or expiry: async-result delivery can invalidate yield; abort and budget controls curtail further work; terminal model errors and exhausted reminders end recovery.
- Activation or effect: code can dispatch synthetic reminders and await async work before returning; exercised behavior and latency are unobserved.
- Evidence limits: inspected executor driver, not a proof of every AsyncJobManager/monitor interleaving or model compliance with refreshed-result instructions.

The child proposes completion; code can withhold it. A prompted human veto is not shown at this scheduling stage. Operating mode: open delegated work. Answer oracle: none; the check concerns pending work and current submission state. It is not a theory-criticism or product-correctness test.

> if (!session.hasPendingAsyncWork()) {
> if (monitor.yieldCalled()) break;
> continue;
> }
> --- `packages/coding-agent/src/task/executor.ts`

> if (monitor.yieldInvalidatedByAsync() && !abortSignal.aborted) {
> exitCode = 1;
> error ??=
> "Background job results arrived after the subagent's last yield; it did not submit a refreshed yield covering them.";
> }
> --- `packages/coding-agent/src/task/executor.ts`

Guarantee owner/enforcement: executor termination loop and monitor state. Guarantee strength: protocol. It depends on session pending-work and invalidation reporting; this member inspected the driver, not a complete lower-layer race proof. The failed result exposes the reason instead of certifying stale output as completed. It does not undo earlier child actions.

#### WF-RTE-output-finalization
Label: Output finalization

Part of: [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn)

Distinct from the completion barrier: this part consumes collected yield/raw data and run status, assembles output, and accepts or rejects its format. Owner: `finalizeSubprocessOutput`, invoked by `finalizeRunResult`. State: selected schema, mode/source, yield items, abort state and last report text. SRC-1, `packages/coding-agent/src/task/executor.ts`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: finalized raw output, exit code, stderr and optional structured-output metadata.
- Later read-back: inapplicable — this function shapes current-run output; artifact persistence is a downstream result-delivery step.
- Delegated visibility: assembled data or an error payload replaces raw child output before parent delivery; not all original narration crosses back.
- Selection predicate: yielded output is assembled/validated; non-yield output may use JSON fallback; strict/permissive policy and schema source affect acceptance.
- Invalidation or expiry: schema failure can force exit 1; strict mode rejects overridden/invalid output rather than treating warning-decorated output as success; abort status bounds fallback.
- Activation or effect: finalization rewrites the returned content/status; no observed success or schema-compliance rate.
- Evidence limits: format validity supplies no reference answer or semantic code oracle; complete yield-tool retry policy was not inspected.

The child model proposes content. Code assembles and validates; no human content-review step is established here. Mode: open delegated work with format enforcement, not a bounded improvement experiment. The schema says what output shape is admissible, not what solution is correct. Strict format failure is a rejection ability; the function itself performs no repair of child project edits. Upstream reminders can seek submission, and the parent receives failure/salvage for further recovery.

> const mustReject =
> failure !== undefined && (mode === "strict" || (!assembled.schemaOverridden && !schemaError));
> if (mustReject && failure) {
> const outcome = buildSchemaViolationOutcome(failure, completeData);
> rawOutput = outcome.rawOutput;
> stderr = outcome.stderr;
> exitCode = outcome.exitCode;
> --- `packages/coding-agent/src/task/executor.ts`

> return { rawOutput, stderr: headline, exitCode: 1 };
> --- `packages/coding-agent/src/task/executor.ts`

Guarantee strength: policy. Owner/enforcement: output finalizer over the selected schema/mode, contingent on upstream supplying those values and collected output. Implementation wiring is established; actual enforcement in a target run is unobserved.

#### WF-RTE-result-delivery
Label: Result delivery

Part of: [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn)

This part is the finalized-output-to-parent boundary, distinct from construction and acceptance checks. Endpoints: finalized child output → optional artifact/sidecar writes and tail truncation → `SingleResult` → task summary envelope and details → parent tool return. Owners: executor finalizer, structured-subagent lease cleanup and task-tool result renderer. Effects: optional files and model-facing result text. SRC-1, `packages/coding-agent/src/task/executor.ts`, `packages/coding-agent/src/task/structured-subagent.ts`, `packages/coding-agent/src/task/index.ts`, `packages/coding-agent/src/task/result-summary.ts`, implementation; `packages/coding-agent/src/prompts/tools/task-summary.md` supplies the consumed template.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: status-labelled summary, bounded output/preview, result details, usage and optional output path; facade exceptions produce an error tool result with settled-work metadata when available.
- Later read-back: full finalized raw output may be written as an artifact and structured data as a sidecar; temporary lease cleanup can remove them. Actual retrieval and attained persistence horizon are uninspected.
- Delegated visibility: parent receives escaped summary content, not full child context; an output pointer can represent omitted material when an artifact path exists.
- Selection predicate: finalization precedes truncation; summary uses output then stderr fallback, and previews above 5,000 characters only when an output path is available.
- Invalidation or expiry: republished output removes stale sidecars when no replacement data is available; artifact-write failure may omit a path; facade retention/cleanup conditions govern continued access.
- Activation or effect: returned text enters the parent loop and can guide next decisions; actual reliance or beneficial recovery is unobserved.
- Evidence limits: pointer rendering does not prove durable availability; internal URL resolver and persisted revival were not traced here; status is not semantic acceptance.

> await writeArtifact(candidatePath, rawOutput);
> outputPath = candidatePath;
> --- `packages/coding-agent/src/task/executor.ts`

> const truncated = outputCharCount > FULL_OUTPUT_THRESHOLD && result.outputPath !== undefined;
> const preview = truncated ? previewHead(output) : output;
> --- `packages/coding-agent/src/task/result-summary.ts`

> const shouldCleanup = lease.temporary && !shouldRetainArtifacts;
> --- `packages/coding-agent/src/task/structured-subagent.ts`

Result persistence records the finalized child return, not the entire model context or a correctness certificate. Artifact failure is logged; the task result can still return without an output path. A facade failure after the child settled retains its metadata for salvage instead of silently treating a zero exit as an accepted end-to-end result (SRC-1, `packages/coding-agent/src/task/index.ts`). The parent can use returned failures to plan recovery, but no mandatory parent repair loop was established.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn)

Workflow role: separate child working conversation with selected assignment/context inputs and bounded return to the parent. The foreground model proposes delegation; task policy/facade select execution configuration; the child model chooses intermediate actions. Completion scheduling, format acceptance and parent-facing delivery are separately declared above because they have different checks and consumers. The parent retains next-step ownership after the task result. No universal semantic verification or rollback follows from child completion.

#### On [RT-RTE-session-turn](runtime.md#rt-rte-session-turn)

Workflow delivery boundary: the child return is an intermediate tool result. Caller delivery belongs to the foreground session's eventual terminal output; it must not be inferred from the child's yield or artifact alone. This account does not establish what a particular foreground model does with a failed or truncated child return.
