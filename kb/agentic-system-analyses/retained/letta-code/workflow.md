---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Letta Code workflow: a bidirectional parent delegates a local non-memory Task, receives completion, and resumes toward a delivered response."
run-id: AAS-2026-10-12-letta-code-be76afeab9b7-01
reviewed-boundary: "271f119dcf37d58649a18e6c733386b3c710a456"
---

# Letta Code workflow report

## Workflow account

### Selection and evidence boundary

The selected workflow is an open user request in bidirectional headless mode for which the parent model invokes a local, non-memory Task, then receives its completion as input to a subsequent turn. This is representative of asynchronous delegation: the launch receipt, child result, parent continuation and delivered answer have separate owners and completion criteria. It is a source-supported conditional path, not an observed coding episode or a guarantee that every request delegates. The foreground and task baselines are [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn) and [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task).

All additional inspection is implementation evidence from SRC-1 at the frozen commit: `src/tools/impl/task.ts` (spawn lifecycle, completion, launch checks and text adapter), `src/agent/subagents/manager.ts` (result interpretation and truncated-stream recovery), and `src/headless.ts` (notification conversion, bidirectional queue connection and next-turn input). No target, tests, examples or providers were executed. Child compliance, answer quality, successful delivery and recovery behavior remain unobserved. Remote computer deployment and memory/reflection integration are alternatives, not steps silently joined into this workflow.

### 1. Request, action proposal and admission

The caller supplies the problem and keeps the bidirectional session available. The parent receives effective instructions, history, skills and tools; its model proposes whether to delegate and what assignment to give. The foreground caller, rather than the model, classifies client-tool approval and executes admitted calls. A denial is returned into continuation instead of launching the action. These ownership and permission distinctions are supplied by [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn) and [RT-CLM-approval-policy](runtime.md#rt-clm-approval-policy), grounded in SRC-1: `src/headless.ts`, `src/permissions/checker.ts`, `src/agent/approval-execution.ts`. A caller's consent is not an answer oracle or proof of correctness.

Task admission has additional structural checks. A prepared child cannot reuse the parent conversation; an explicit agent must own the child conversation. A configuration requesting a fork cannot also specify agent/conversation IDs. Failure to create a fork returns an error without proceeding to task spawn. These are scope/identity checks, not tests of the assignment's merit. SRC-1: `src/tools/impl/task.ts`.

> if (effectiveConversationId === resolvedParentScope?.conversationId) {
>       return {
>         success: false,
>         error: "A subagent cannot run in its parent conversation",
>       };
>     }
> --- `src/tools/impl/task.ts`

### 2. Handoff and asynchronous ownership

The Task caller supplies assignment text, description, subagent type/configuration, optional model and turn limit, tool-call linkage, and selected child identity or forked context. Spawn captures parent agent/conversation scope synchronously, registers a task and subagent, creates an output file and abort controller, and starts child execution. This capture prevents later asynchronous work from routing by a drifted global parent identity. The handoff is not an unconditional copy of all parent state. SRC-1: `src/tools/impl/task.ts`; the grant/configuration distinctions are [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task).

The non-memory launch waits for the subagent link and checks startup error state before returning IDs and output location. This receipt establishes launch/linkage, not completion. Thereafter the background lifecycle owns settlement; the parent can continue other work. SRC-1: `src/tools/impl/task.ts`.

> // Intentionally fire-and-forget: background tasks own their lifecycle and
>   // capture failures in task state/transcripts instead of surfacing a promise
>   // back to the caller.
> --- `src/tools/impl/task.ts`

The child runs its own headless conversation and tool continuations. Child defaults use unrestricted permission mode with inherited disallows and configured filters/allows, not the parent's live approval dialog. This is delegation of execution authority, not merely a request for prose, and does not establish kernel isolation or human review of every child action. [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task), [RT-CLM-shell-isolation](runtime.md#rt-clm-shell-isolation). SRC-1: `src/agent/subagents/manager.ts`, `src/tools/impl/shell-sandbox.ts`.

### 3. Child completion is protocol verification, not product verification

The manager distinguishes captured result, captured error, and a clean exit without a captured result. For an ordinary non-reflection child with a final result, success depends on the absence of a completion error. The inspected branch does not compare the report against an expected answer, run an independent correctness judge, or require parent acceptance of the work product. Such task-specific verification may be requested by an assignment, but successful execution of that request is not established here. SRC-1: `src/agent/subagents/manager.ts`.

> const completionError = state.finalError ?? toolFailureError;
>       return withModel({
>         agentId: state.agentId || "",
>         conversationId: state.conversationId || undefined,
>         report: state.finalResult,
>         success: !completionError,
> --- `src/agent/subagents/manager.ts`

The lifecycle sets task status from `result.success`, writes the result transcript, records completion and schedules cleanup. An optional completion callback is separate: callback errors are appended to the output file. The ordinary Task invocation inspected does not install a product-verification callback. Thus “completed” is a lifecycle result, not a verified solution. SRC-1: `src/tools/impl/task.ts`.

### 4. Failure and bounded recovery

A rejected parent-conversation target returns an error through the Task adapter. An execution result carrying an error becomes failed task state and an error notification. A thrown execution/lifecycle exception is caught, appended to the output transcript and also reported as failed. The host publishes the failure; the subsequent parent model may propose another task or revise its answer. This inspected path does not impose a universal parent retry policy or undo prior child effects. SRC-1: `src/tools/impl/task.ts`.

The manager has one narrower automatic recovery: when no result/error was captured, it parses stdout. If parsing fails and the clean stream is recognizably truncated mid-line, it can respawn once. Other parse failures do not trigger that retry. This distinction matters because a clean process exit alone is insufficient to deliver a report, and repeating work may repeat effects. This is source implementation, not an independently observed reproduction of the incident mentioned in the comment. SRC-1: `src/agent/subagents/manager.ts`.

> if (!isRetry && looksLikeTruncatedStreamJson(stdout)) {
> --- `src/agent/subagents/manager.ts`

> true, // Mark as retry to prevent infinite loops
> --- `src/agent/subagents/manager.ts:712-712`

No exactly-once or transactional rollback conclusion follows. The listener-specific durable fence in [RT-CLM-effect-checkpoint](runtime.md#rt-clm-effect-checkpoint) is not imported into this headless child workflow merely because both paths execute tools.

### 5. Result transport, parent consumption and delivery

On ordinary non-memory completion, the lifecycle constructs a success report or error, truncates successful completion text to the Task output character limit, wraps status/summary/result/output-file/usage in a notification, and routes it to the captured parent scope. The parent therefore receives selected completion text and a file reference, not necessarily the complete child report. SRC-1: `src/tools/impl/task.ts`.

> const { content: truncatedResult } = truncateByChars(
>           fullResult,
>           LIMITS.TASK_OUTPUT_CHARS,
>           "Task",
>           { workingDirectory: userCwd },
>         );
> --- `src/tools/impl/task.ts`

Bidirectional headless connects these background notifications to its input queue. It serializes notification text as a synthetic user line while retaining the task-notification kind; it either resolves a waiting reader or stores the line. The coalescing path tracks and consumes queued inputs, merges their content, and starts another turn when merged content is non-null. This establishes transport into subsequent parent-turn input, not that the parent obeys the notification or inspects the full output file. SRC-1: `src/headless.ts`.

> // Connect Task/subagent background notifications to the same queueing path
>   // used by user input so bidirectional mode inherits TUI-style queue behavior.
>   setMessageQueueAdder((queuedMessage) => {
> --- `src/headless.ts`

> const userContent = mergeBidirectionalQueuedInput(queuedInputs);
> --- `src/headless.ts`

The resumed parent retains responsibility for further action and the caller-facing response. A child completion notification and Task launch receipt are intermediate outputs, not final user delivery. The foreground stream/result output supplies the terminal response for a parent turn, with stop/error information, as described in [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), SRC-1: `src/headless.ts`. The inspected wiring does not require the parent to wait for every child before ending its current turn, or require a user to accept the result. Session termination before consumption and arbitrary assignment-specific verification are not established end to end. Keeping the input session live is consequential to this selected asynchronous path; one-shot headless delivery is not inferred from the bidirectional queue bridge.

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

#### On [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task)

Workflow role: asynchronous assignment and child-result handoff. Launch/link receipt, child protocol success and parent product acceptance are distinct milestones. The selected local non-memory path rejects parent-conversation reuse, interprets captured result/error envelopes, and retries recognizable truncated result transport once. Its completion notification carries bounded report text plus output location. Those workflow findings and new implementation passages are established above, from SRC-1: `src/tools/impl/task.ts`, `src/agent/subagents/manager.ts`.

#### On [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)

Workflow role: parent proposal, admission, result consumption and caller-facing delivery. The selected bidirectional variant routes Task completion through synthetic user input and queued-turn merging; it does not turn the child launch receipt into a final answer. The parent model remains the next content-decision owner, with no independently specified answer oracle in the inspected generic delegation path. Source scope: SRC-1: `src/headless.ts`, `src/tools/impl/task.ts`.
