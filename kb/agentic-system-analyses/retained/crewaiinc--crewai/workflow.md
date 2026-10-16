---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "CrewAI workflow account: hierarchical Crew scheduling, coworker delegation, Task guardrail recovery and aggregate delivery."
run-id: AAS-2026-10-15-crewai-62e53db969a7-01
reviewed-boundary: "3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8"
---

# CrewAI workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a hierarchical Crew with multiple ordered, synchronous tasks, taking the branch where its manager delegates work to a configured coworker and a configured Task guardrail checks the manager's candidate. This selects connected branches of the shipped execution path, not an observed application run. It exposes the distinction between code scheduling, model delegation, output acceptance and delivery. Delegation is available to the manager, not guaranteed to occur; guardrails are configured checks, not an automatic universal review stage.

The frozen [boundary](boundary.md) supplies SRC-1 at the reviewed commit. The [runtime baseline](runtime.md) establishes invocation and model/tool execution. Additional inspection here covers hierarchical scheduling, manager recipient preparation and CrewOutput assembly in SRC-1, `lib/crewai/src/crewai/crew.py`; coworker dispatch in `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`; and synchronous Task execution and guardrail retries in `lib/crewai/src/crewai/task.py`. These are implementation evidence only. No successful delegation, accepted result, delivered artifact or improvement was observed. Async, conditional, standalone Agent and Flow execution are not the selected workflow; their runtime records remain separate rather than being joined into this trace.

### Request and scheduling

The caller supplies Crew configuration and kickoff inputs. Preparation interpolates inputs; the hierarchical process creates or uses a manager, then passes the task list to the same task scheduler used for ordered execution. [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff) supplies the invocation and context-selection evidence. The manager is not a separate scheduler that can freely replace the task graph: Crew code advances the configured list, while the manager model chooses intermediate actions inside each scheduled task (SRC-1, `lib/crewai/src/crewai/crew.py`).

> def _run_hierarchical_process(self) -> CrewOutput:
>     """Creates and assigns a manager agent to complete the tasks."""
>     self._create_manager_agent()
>     return self._execute_tasks(self.tasks)
> --- `lib/crewai/src/crewai/crew.py`

The manager executes the scheduled task even when that task names another agent. With unspecified context, the next synchronous task gets aggregated raw prior outputs; explicit context chooses named task outputs, while false context supplies an empty string. This passes result text, not every preceding conversation. The scheduler calls Task.execute_sync and appends its returned TaskOutput before advancing. Task-level pre-step interception can modify the supplied context (SRC-1, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/task.py`).

> def _get_agent_to_use(self, task: Task) -> BaseAgent | None:
>     if self.process == Process.hierarchical:
>         return self.manager_agent
>     return task.agent
> --- `lib/crewai/src/crewai/crew.py`

### Manager-to-coworker handoff

The manager receives delegation tools. Tool preparation narrows recipients to the task's assigned agent when one is present; otherwise it exposes the Crew agents. Thus a manager's choice is bounded by the tool's current recipient list, not just the model's knowledge of role names (SRC-1, `lib/crewai/src/crewai/crew.py`).

> if self.manager_agent:
>     if task.agent:
>         tools = self._inject_delegation_tools(tools, task.agent, [task.agent])
>     else:
>         tools = self._inject_delegation_tools(
>             tools, self.manager_agent, self.agents
>         )
> --- `lib/crewai/src/crewai/crew.py`

The manager model proposes coworker role, task text and context. Dispatch sanitizes roles and selects the first matching configured agent. The coworker receives a newly constructed Task with the proposed description and a shipped manager-request expected-output instruction, plus the separately supplied context. It executes with its own agent preparation, retrieval and tools. Its returned string becomes a tool observation for the manager, which can continue reasoning or produce a final candidate. [RT-RTE-agent-delegation](runtime.md#rt-rte-agent-delegation) supplies the dispatch/return evidence; [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) supplies the surrounding model/tool loop. Neither establishes that the manager follows or correctly evaluates the coworker's answer.

An important handoff limit is visible in SRC-1, `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`: the delegation helper directly calls selected_agent.execute_task rather than Task.execute_sync on the constructed Task. The constructed task therefore supplies task metadata, not an independent pass through the outer Task guardrail/callback/file-delivery stage.

> task_with_assigned_agent = Task(
>     description=task,
>     agent=selected_agent,
>     expected_output=I18N_DEFAULT.slice("manager_request"),
> )
> --- `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`

The minimum direct-call passage is retained by [RT-RTE-agent-delegation](runtime.md#rt-rte-agent-delegation). Separate frames limit transcript transfer, not process authority or persistent effects. Memory access can add context beyond what the manager explicitly delegated.

### Acceptance and recovery

The manager's executor returns its candidate to the scheduled Task. Task constructs TaskOutput and runs configured guardrails. A callable or model-backed check can accept or replace the output, or reject it and cause another agent execution with validation-error context. The Task runtime owns this retry decision and budget; the manager model chooses the new work. No expected-answer oracle is supplied by this workflow, and neither model approval nor successful structured export proves factual correctness. The mode is open task execution with bounded retries, not a controlled experiment. [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail) and [RT-CLM-output-validation](runtime.md#rt-clm-output-validation) supply the gate, ownership and enforcement limits.

Rejection re-enters agent execution with the original task and tools, but context now contains the validation error and rejected raw output. It is not simply an identical replay of the original upstream context. Successful checks can replace raw output or return a replacement TaskOutput. Multiple configured checks run in order; this synchronous loop does not show earlier checks being rerun after a later check revises the candidate (SRC-1, `lib/crewai/src/crewai/task.py`).

> context = I18N_DEFAULT.errors("validation_error").format(
>     guardrail_result_error=guardrail_result.error,
>     task_output=task_output.raw,
> )
> --- `lib/crewai/src/crewai/task.py:1400-1403`

On exhaustion, Task raises instead of advancing the Crew; its failure handler emits TaskFailedEvent and rethrows. This is bounded retry recovery, not guaranteed completion. Agent memory saving precedes the Task gate, so rejection neither retracts that save nor rolls back earlier tool effects; a retry can repeat them. The minimum save-before-return and exhaustion passages are in [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail).

A different failure occurs inside delegation: an unknown recipient returns an error observation, and an exception during coworker execution is converted to an execution-error string. The manager then has an opportunity to choose another action; code does not guarantee it recognizes the error or repairs the request. This is distinct from the outer Task's exception path (SRC-1, `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`).

> except Exception as e:
>     return I18N_DEFAULT.errors("agent_tool_execution_error").format(
>         agent_role=self.sanitize_agent_name(selected_agent.role), error=str(e)
>     )
> --- `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`

### Progression and delivery

After guardrails, a post-step hook can replace the Task payload. Task assigns its output, invokes configured task/Crew callbacks, optionally saves an output file, emits completion and returns. The scheduler supplies that result to later tasks according to their context selection. This is configured progression control, not an immutable certified artifact: hooks and callbacks remain trusted Python code (SRC-1, `lib/crewai/src/crewai/task.py`; [RT-CLM-output-validation](runtime.md#rt-clm-output-validation)).

At the end, Crew rejects an empty output list or one with no truthy raw output. Otherwise it chooses the last truthy raw TaskOutput, not necessarily the last list entry, as the top-level result. CrewOutput also contains the full task-output list and token usage. This is aggregation and selection, not an additional independent review or synthesis step (SRC-1, `lib/crewai/src/crewai/crew.py`).

> valid_outputs = [t for t in task_outputs if t.raw]
> if not valid_outputs:
>     raise ValueError("No valid task outputs available to create crew output.")
> final_task_output = valid_outputs[-1]
> --- `lib/crewai/src/crewai/crew.py`

Output and execution-end hooks can replace the aggregate payload. Crew then drains background memory writes and emits kickoff completion before returning the payload. In this selected nonstreaming path, API return is the delivery boundary; optional Task files are separate local artifacts, not evidence of external publication. Draining is an ordering mechanism, not evidence that every memory write succeeded or the response is correct. No supplied run establishes that this delivery path completed (SRC-1, `lib/crewai/src/crewai/crew.py`).

> self._drain_memory_writes()
> crewai_event_bus.flush()
> --- `lib/crewai/src/crewai/crew.py`

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

#### On [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)

Workflow role: enclosing request-to-delivery route. In the selected hierarchical synchronous branch, runtime code schedules tasks and the manager executes each task with bounded recipient tools. The terminal aggregate uses the last truthy raw output and preserves all TaskOutputs alongside it; output/end interception remains downstream of individual Task checks. Delivery means returning the aggregate payload, not verified external receipt. Implementation evidence and minimum passages are in the workflow account above; operation remains unobserved.

#### On [RT-RTE-agent-delegation](runtime.md#rt-rte-agent-delegation)

Workflow role: optional manager-to-coworker handoff within a scheduled task. A constructed Task is passed directly to agent execution, not independently run through the outer Task lifecycle. The manager receives either returned task text or an error observation and owns any model-selected follow-up; successful recovery is unobserved. The outer Task gate checks the manager's candidate, not every intermediate coworker result independently.

#### On [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail)

Workflow role: configured acceptance and bounded retry before scheduler progression. Validation-error context replaces the original supplied context on retry; retries may redo delegation or effects. Sequential checks do not establish a fixed point satisfying every earlier check after later replacement. Post-step and aggregate hooks are later mutation points. These limits prevent treating Task acceptance as transactional execution or final-artifact truth certification.
