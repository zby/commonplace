---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Agent S S3 workflow from an opted-in local desktop request through coding delegation, GUI verification policy and terminal delivery."
run-id: AAS-2026-10-16-agent-s-db6fee212353-01
reviewed-boundary: "15776a8dc659658b1963816ea006f7af1978e595"
---

# Agent S workflow report

## Workflow account

### Selection and evidence boundary

This account selects the installed S3 desktop workflow with local coding enabled. It combines the ordinary screenshot/action loop with a shipped, opt-in delegation branch, making the handoff, feedback, verification and delivery boundaries visible within one connected workflow. It does not invent a particular spreadsheet task or claim that a session succeeded. Without coding enabled, the ordinary GUI route remains the baseline. The governing routes are [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop) and [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation). SRC-1: `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s3/agents/grounding.py`.

All evidence is implementation or doctrine/design from SRC-1 at the revision in [boundary](boundary.md). This inspection reread the S3 CLI task loop and construction, AgentS3 prediction/reset, Worker generation and return handling, ACI coding/terminal methods, and CodeAgent's complete execution and summary logic. It extends the provisional runtime account's workflow detail, not the source boundary. No execution trace, actual modified artifact or provider response was supplied. Successful delegation, GUI verification and task correctness remain unobserved. Historical S1/S2 planning and offline rollout selection are not appended to this workflow: they are distinct routes, not automatic successors of this CLI session.

### 1. Admit the request and assign next-step ownership

A human supplies `--task` or an interactive query and model/grounding configuration. `--enable_local_env` defaults to false; opting in constructs LocalEnv and passes it into OSWorldACI. The CLI resets AgentS3, which constructs a fresh Worker, then starts the bounded desktop loop. This is capability opt-in, not human review of each script. SRC-1: `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/agent_s.py`; [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation).

> local_env = None
> if args.enable_local_env:
>     print(
>         "⚠️  WARNING: Local coding environment enabled. This will execute arbitrary code locally!"
>     )
>     local_env = LocalEnv()
> --- `gui_agents/s3/cli_app.py`

For each of at most 15 outer iterations the driver acquires a resized PNG screenshot and calls predict with the original instruction and observation. AgentS3 forwards these to Worker.generate_next_action. Worker sets ACI's current screenshot and task, inserts the task into its initial system prompt, and constructs model context from screenshot, text buffer, available reflection and any prior coding result. The generator model owns the next substantive action choice; the driver owns execution and stopping. Reflection is advice, not a separate acceptance authority. SRC-1: `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s3/agents/worker.py`; [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop), [RT-BAP-worker-policy](runtime.md#rt-bap-worker-policy).

### 2. Delegate coding with a selected task frame

If the worker chooses `agent.call_code_agent()`, ACI uses the original task. If a task argument is non-None, ACI uses that argument instead. The method's instructions reserve explicit arguments for specific subtasks and warn against rephrasing the full task, but the implementation tests only non-None, not task fidelity. There is no manager allocating parallel workers in this S3 path. Delegation is synchronous. SRC-1: `gui_agents/s3/agents/grounding.py`; [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation).

ACI supplies the selected instruction, current screenshot and environment controller. CodeAgent resets its model context, retaining neither the outer worker's full dialogue nor a previous coding session. It starts a fresh dialogue under CODE_AGENT_PROMPT. The default budget is 20 coding rounds. The coding model selects Python/Bash or a terminal signal; controller results then enter its next user message. This isolates detailed execution feedback from the outer dialogue, but not external file effects. SRC-1: `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/grounding.py`; [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation).

The handoff is not safely deferred until the driver executes a returned GUI string. Action formatting trial-evaluates the call against the live ACI, and Worker evaluates again to construct its action. Consequently coding can execute during checking and again during conversion. ACI returns a sleep string only after the delegated session has run. The number of sessions depends on formatting attempts and failures; this is not a claim of a fixed execution count. The passages and enforcement limits are in [RT-RTE-action-check](runtime.md#rt-rte-action-check). SRC-1: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/utils/formatters.py`, `gui_agents/s3/utils/common_utils.py`.

### 3. Execute, reject locally and recover

Recognized fenced Python/Bash reaches the controller without per-script human approval. Bash is passed a 30-second timeout; the Python call has no corresponding timeout argument. Controller status, return code, output and error are feedback for the coding model, not proof of task completion. The model may revise its next script. Controller exceptions become error dictionaries. Missing code produces a skipped result; an unknown code type produces an error result. Both enter subsequent coding context rather than an automatic rollback. SRC-1: `gui_agents/s3/agents/code_agent.py`; [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation).

A checked failure path is an unsuccessful coding session: model FAIL breaks the loop; exhaustion yields a distinct budget completion reason. Neither automatically declares the outer desktop task failed. Both proceed to summary creation and a cached return for the outer worker, which can choose GUI recovery. By contrast an empty coding response raises RuntimeError rather than producing this normal return; the Worker's final conversion try/except can convert conversion errors to a sleep action. This does not undo any earlier writes. Formatter/provider retries are separately bounded and do not establish eventual recovery. SRC-1: `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/worker.py`; [RT-RTE-action-check](runtime.md#rt-rte-action-check).

> result_context = format_result(result, step_count)
> self.agent.add_message(result_context, role="user")
> --- `gui_agents/s3/agents/code_agent.py`

> completion_reason = f"BUDGET_EXHAUSTED_AFTER_{step_count}_STEPS"
> --- `gui_agents/s3/agents/code_agent.py`

### 4. Return evidence to the worker and request GUI verification

The normal coding return contains task instruction, completion reason, summary, action/thought history and budget counters. The dedicated summary model receives the task and recorded actions/thoughts, not the controller-result messages. Therefore even a summary requested to describe outputs is not an independent execution report. On the next prediction Worker delivers the summary, reason and formatted actions with a fresh screenshot, then clears the cached return. It does not include the stored thoughts as a separate history field or transfer the full code-agent dialogue. This loss of detailed feedback matters to what the outer verifier can know. SRC-1: `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/worker.py`; [RT-BAP-code-return](runtime.md#rt-bap-code-return).

Worker policy requires GUI verification before done, including closing and reopening applications whose open views may not reflect changed files. If coding or verification fails, policy directs GUI completion instead. The worker model must decide whether observations meet the original request; no independent answer oracle is supplied in this open-request mode. This is a requested acceptance test, not an enforced postcondition. The policy passage is supplied by [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory), and its guarantee limit by [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification). SRC-1: `gui_agents/s3/memory/procedural_memory.py`, `gui_agents/s3/agents/grounding.py`.

### 5. Deliver or stop without a correctness certificate

After any GUI continuation the worker can choose done or fail. The ACI methods return DONE or FAIL directly; neither checks verification history. CLI substring handling stops on either and uses the same completion dialog. Ordinary action strings instead reach local exec and the next screenshot. The permission comment beside exec does not request approval. The loop can also exhaust 15 iterations without a terminal success signal. Thus delivery consists of changed desktop/files, streamed plans and termination of the driver workflow, not a separately validated result object or guaranteed successful work product. SRC-1: `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/cli_app.py`; [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop).

The consequential separation is between controller feedback, model-declared coding completion, requested GUI verification and outer driver termination. None alone certifies the next. Code establishes their wiring and the possibility of local recovery; without a supplied run it establishes neither exercised verification nor successful delivery.

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

#### On [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

Workflow role: owns request admission, observation acquisition, outer action execution and terminal delivery. Its 15-iteration bound does not count or bound synchronous coding rounds. The terminal dialog is shared by done and fail, so it must not be interpreted as an acceptance verdict. Source detail and evidence limits are traced in steps 1 and 5 above.

#### On [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation)

Workflow role: synchronous subtask frame whose controller effects escape before return. Normal FAIL and budget exhaustion return control to the worker for a possible GUI recovery decision; they do not automatically become outer task failure. Detailed result messages remain in the coding frame, while summary and formatted actions cross back. Steps 2–4 identify the actual recovery owner and reduced verification context.

#### On [RT-RTE-action-check](runtime.md#rt-rte-action-check)

Workflow role: a formatting/convertibility check, not a task acceptance gate. Because validation invokes ACI, this boundary can perform the delegated work before the outer driver receives its sleep action. It supplies neither rollback nor a guarantee that exactly one delegated session occurs.

#### On [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification)

Workflow acceptance role: asks the worker to compare a reopened application's GUI with the task after coding. The final decision remains model-owned, with no external expected-answer oracle and no guard on done. An actual verification and its result are unobserved.
