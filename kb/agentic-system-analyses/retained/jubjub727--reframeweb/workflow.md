---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ReframeWeb workflow account tracing a routed request through selected-context Codex delegation, completion review, bounded recovery and host return."
run-id: AAS-2026-10-14-reframeweb-cff918d7eb1e-01
reviewed-boundary: 318987dcde9a016f8e3db819ed9a73abf6b3ad81
---

# ReframeWeb workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is one accepted request whose selected catalog task has an agent configuration: the host prepares a workspace, delegates execution to Codex, checks the result, and either retries, reselects a task or returns the newest bounded result. This branch was selected because a single shipped orchestrator connects context selection, delegated effects, verification and recovery. It is not a hypothetical combination of unrelated capabilities. Its parent is [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle), with execution through [RT-RTE-codex-task](runtime.md#rt-rte-codex-task).

All findings concern implementation or requested model behavior at SRC-1's frozen commit, not an observed request. The [boundary](boundary.md#boundary-and-evidence) excludes Codex/provider internals and deployment state. This inspection covers `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/baml_src/ns_voice_turn/agent_routing.baml`, `agent-host/baml_src/ns_voice_turn/request_state.baml`, `agent-host/baml_src/ns_task/execution/agent_prompts.baml`, `agent-host/baml_src/ns_task/refusal/flow.baml`, `agent-host/baml_src/ns_task/ns_internal/failure_resolution.baml`, `agent-host/src/reframe_agent_host/voice/agent_task_callbacks.py`, `agent-host/src/reframe_agent_host/agent_execution/tasks.py`, `agent-host/src/reframe_agent_host/agent_execution/summary.py`, `agent-host/src/reframe_agent_host/voice/agent_turn.py`, and the output-recording section of `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`. These supply implementation evidence; embedded prompts supply doctrine/design. The failure-resolution and request-state helpers add detail beyond the runtime baseline. No target execution or experiment was performed.

### Request, selection and delegation

Acceptance and session/conversation binding precede this workflow, as established by [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle). Python constructs the callback host and awaits the BAML turn result. BAML owns the orchestration rather than delegating the entire request lifecycle to Codex. Each cycle reloads context; models choose the catalog task, search hints, search depths and relevant memory IDs. Python retrieves the graph. `SelectedGraph` and `PromptContexts` transform that graph before the composition model receives context. The executor therefore receives composed task input, not the complete retrieved graph or all routing deliberation (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`).

`TaskConversation` excludes validation replies and other active human requests while keeping the current human request. This is a code-selected task frame, not evidence of provider-internal context compaction. The no-action task bypasses execution; an ordinary task without agent configuration takes the separate direct-model route [RT-RTE-model-task](runtime.md#rt-rte-model-task). The selected workflow takes the other branch:

> if (selected.agent_config != null) {
>         //# Execute in prepared agent workspace
>         agent(cycle_id, choice, root.task.AgentTaskPrompt(prompt), continuation)
> --- `agent-host/baml_src/ns_voice_turn/agent_routing.baml`

The wrapped prompt requests root workspace instructions, actual tool execution and exactly one summary in final data. This establishes requested conduct, not truthful feedback or compliance. Codex receives native shell/file tools as well as task-scoped MCP. The task allowlist is consequently not a universal effect boundary; its checks and the uncertainty ledger are established by [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt). The delegated process and supplied sandbox policy are described in [RT-RTE-codex-task](runtime.md#rt-rte-codex-task) (SRC-1, `agent-host/baml_src/ns_task/execution/agent_prompts.baml`).

The host allocates an attempt ID, passes selected Store project IDs and prepares or reuses the cycle's workspace. `AgentTasks.execute` rejects a changed task identity/configuration on reuse. The callback supplies a task tool session using the cycle ledger, then stores the returned workspace for another attempt. Thus a retry has a fresh delegated execution but retained filesystem work; it is not an independent clean-slate trial (SRC-1, `agent-host/src/reframe_agent_host/voice/agent_task_callbacks.py`, `agent-host/src/reframe_agent_host/agent_execution/tasks.py`; [RT-RTE-codex-task](runtime.md#rt-rte-codex-task)).

### Effects, feedback and acceptance

Tools can change state before verification. The host persists workspace contents before dispatching returned paths; an exception in execution or persistence becomes an error-bearing attempt. Cancellation is re-raised instead of being converted into ordinary result data. Final data is not a deferred action program: the output stage records it and tool history rather than replaying model-specified actions (SRC-1, `agent-host/src/reframe_agent_host/agent_execution/tasks.py`, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`; [RT-CLM-agent-output](runtime.md#rt-clm-agent-output)).

> result = await record_outputs(execution, history)
>         return result, 0.0, time.perf_counter() - post_vad_started_at
> --- `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`

For this branch, summary processing records execution evidence and extracts the executor's own required summary. It does not launch a separate verifier conversation in the workspace, despite a contrary routing comment. Missing feedback is failure; overlength feedback is truncated and also marked failure (SRC-1, `agent-host/src/reframe_agent_host/agent_execution/summary.py`; [RT-RTE-codex-task](runtime.md#rt-rte-codex-task)).

> if text is None:
>         text = "Task failed before it produced feedback." if failure else "Task completed without executor feedback."
>         failure = failure or "agent execution omitted its required summary item"
>     elif len(text) > SUMMARY_LIMIT:
>         text = text[:SUMMARY_LIMIT]
>         failure = failure or "agent execution summary exceeds the bounded summary limit"
> --- `agent-host/src/reframe_agent_host/agent_execution/summary.py`

The completion model sees the selected task's output requirement, summary plus execution/summary failure text, active request and scoped conversation. Acceptance requires both model PASS and null execution/summary failures, as quoted in [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle). The host can therefore reject an apparent PASS with missing feedback or an execution error. This gate is not an independent test of the workspace artifact: no build/test run is automatically imposed by this orchestration. Verification evidence may be reported by the executor, but source wiring does not authenticate it. No fixed expected answer is supplied; task and request requirements are criteria interpreted by models (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/baml_src/ns_voice_turn/agent_routing.baml`).

### Failure, recovery and delivery

On rejection, a failure model proposes validation guidance and decides whether the same selected task can sensibly be refined. Its prompt requests a concrete substantive mismatch and guidance without a replacement solution. This is an instruction to the model, not an established guarantee against answer leakage (SRC-1, `agent-host/baml_src/ns_task/refusal/flow.baml`).

> validation_reply must state the supported reason the result failed at
>         useful specificity, identify what requirement, content, or action needs
>         correction, and give concrete guidance about what should be checked or
>         changed.
> --- `agent-host/baml_src/ns_task/refusal/flow.baml`

Code appends the recorded outcome and validation reply to retry context, then builds another prompt from the original base prompt and accumulated feedback. Although `ResolveTaskFailure` accepts `failed_execution`, its body does not pass that object into the guidance model; the model receives the output summary and earlier refusal text instead. The feedback channel is therefore narrower than the typed function signature might suggest (SRC-1, `agent-host/baml_src/ns_task/refusal/flow.baml`, `agent-host/baml_src/ns_task/ns_internal/failure_resolution.baml`).

> retry_prompt: root.task.PromptWithRetryContext(
>             base_task_prompt,
>             next_context.previous_replies,
>             next_context.refusal_replies,
>         ),
> --- `agent-host/baml_src/ns_task/ns_internal/failure_resolution.baml`

If refinement is permitted and an attempt remains, BAML retries in the same cycle. Otherwise it ends that cycle with failure evidence. A separate request-completion model can lead to another task-selection cycle; successful tasks are accumulated for that check. The default bounds are two attempts per cycle and two cycles. Three consecutive no-action selections also terminate when configured bounds allow that threshold; with the default two-cycle bound, that threshold cannot be reached. Neither retry nor failed review rolls back earlier effects. The shared tool ledger reduces uncertain replay on covered tools, not native shell effects or all cross-cycle actions (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/baml_src/ns_voice_turn/request_state.baml`; [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt)).

Bound exhaustion returns the newest concrete result, even if request completion has not passed. It is a delivery bound, not a success guarantee. Before normal return, optional guidance proposals undergo model review and selected candidates are written through the host; this admission route is [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review), not a human approval checkpoint (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`).

> // Keep the newest bounded result even if request validation asks for
>             // another task cycle. Hitting the global cycle limit then returns
>             // concrete failure evidence instead of spinning forever.
>             request_result = cycle_result;
> --- `agent-host/baml_src/ns_voice_turn/task_flow.baml`

The Python caller then selects the returned cycle and attempt and assembles the turn result with execution data, output recording, summary, completion and timing fields. Delivery here means return to the host caller, with effects already attempted and workspace recovery state persisted on the normal execution path. It does not establish that a user saw an answer, that an artifact passed acceptance, or that the overall request succeeded. Callbacks and providers must themselves return or fail for bounded iteration to imply termination in time (SRC-1, `agent-host/src/reframe_agent_host/voice/agent_turn.py`; [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)).

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

#### On [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

Workflow-specific recovery: failure guidance is produced from summary-level outcome information rather than the accepted but unused `failed_execution` parameter. Code accumulates outcomes and refusal replies into a new prompt; refinement and task reselection remain distinct decisions. The workflow account supplies the inspected helper evidence. Completion can reject execution/summary failure but does not reverse effects or independently test artifacts. The request-state no-action threshold is reachable only with a sufficiently large cycle bound.

#### On [RT-RTE-codex-task](runtime.md#rt-rte-codex-task)

Workflow-specific handoff: the callback passes selected Store projects, retains the cycle workspace for another attempt and shares its tool uncertainty ledger across attempts. The return channel is final data, execution failure and bounded executor feedback, not a second independent workspace reviewer. Missing or oversized feedback can prevent acceptance even when the completion model would PASS. These fields refine the same supplied route rather than declare another workflow identity.
