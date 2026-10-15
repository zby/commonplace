---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenSage's DevOps-Gym task workflow from environment setup through optional specialist delegation, agent verification, post-run grading and artifact delivery."
run-id: AAS-2026-10-14-opensage-291d1ed79d37-01
reviewed-boundary: "54d64702e18d195c8f0fed711c6db5dc1d62ab29"
---

# OpenSage workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects the shipped DevOps-Gym driver and its root agent, focusing on an issue-resolution task: inspect a supplied issue, change the repository, verify it, optionally delegate a bounded investigation when stuck, then export and grade the result. This is a representative implemented workflow, not a reconstructed successful task. It was selected because one shipped driver connects the task input, agent policy, manager execution, independent post-run test invocation and retained outputs. Delegation is a conditional branch, not a mandatory stage or an observed action.

The evidence is SRC-1, implementation and doctrine/design at the frozen revision. Added inspection covers `agent_library/agents/devops_gym_agent/agent.py` and `config.toml`; task loading, environment hooks, grading and aggregation in `benchmarks/devopsgym/devops_gym.py`; setup/run/collection and continuation selection in `src/opensage/evaluation/base.py`; `src/opensage/toolbox/finish_task/finish_task.py`; and directed-call/error branches in `src/opensage/toolbox/general/orchestration_tools.py` and `src/opensage/orchestration/manager.py`. No target code, tests or examples were executed. The external DevOps-Gym dataset, task images and grading-script bodies are not frozen evidence here. Thus the report establishes the OpenSage-side coordination and grading contract, not any actual issue, test correctness, successful patch or measured pass rate.

### 1. Driver supplies the task and environment

The operator starts the benchmark with dataset/category/configuration choices. The driver loads an instruction and image selector from each external task's `task.yaml`; it rejects samples lacking an instruction or resolvable image. The first user message is that instruction, not an independently authored agent plan. The driver supplies the task image through template variables and exports `/workspace`. It does not mount the task directory as initial shared data, specifically to avoid exposing `run-tests.sh`. This is a data-supply decision, not proof that every image or other path excludes grader material (SRC-1, `benchmarks/devopsgym/devops_gym.py`, `agent_library/agents/devops_gym_agent/config.toml`).

> def _get_first_user_message(self, sample: dict) -> str:
>     return sample["instruction"]
> --- `benchmarks/devopsgym/devops_gym.py`

The base evaluator registers the OpenSage session, prepares resources, creates the agent and saves the used configuration before running it. Environment initialization permits some initialization failures to continue; a running container alone therefore does not certify a correctly prepared task (SRC-1, `src/opensage/evaluation/base.py`).

> await opensage_session.sandboxes.initialize_all_sandboxes(
>     continue_on_error=True
> )
> --- `src/opensage/evaluation/base.py`

### 2. Manager hands the request to the root model

The evaluation route [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout) registers the agent tree, starts the manager, spawns the task session and sends `task.first_user_message` as `__user__`. The manager owns scheduling; ADK owns the inner model/tool progression. The root model owns task interpretation and action selection under [WF-BAP-devops-workflow](#wf-bap-devops-workflow). This is software-delivered task input, not a human approving each proposed edit (SRC-1, `src/opensage/evaluation/base.py`, `agent_library/agents/devops_gym_agent/agent.py`).

The factory grants terminal execution, file viewing/editing, reasoning, completion and dynamic-agent tools. Its default endpoint is `openai/gpt-4o-mini` unless a model object is supplied. Endpoint fixity and mutability limits remain those of [RT-CMP-base-llm](runtime.md#rt-cmp-base-llm); this selector does not pin weights. The supplied configuration enables history and tool-response summarizers and a doom-loop detector. Their selection does not establish successful compaction, preserved evidence or automatic recovery; the runtime's inspected history mechanism is [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) (SRC-1, `agent_library/agents/devops_gym_agent/agent.py`, `agent_library/agents/devops_gym_agent/config.toml`).

### 3. Root explores, edits and optionally delegates

For an issue-resolution task the root is instructed to find the relevant files, reproduce the bug if possible, fix it and verify with available tests. Terminal tools and file tools execute the root's chosen operations; they do not decide whether the patch solves the issue. Shell-effect and containment limits are those of [RT-RTE-terminal-extension](runtime.md#rt-rte-terminal-extension) (SRC-1, `agent_library/agents/devops_gym_agent/agent.py`).

When several attempts leave the root stuck, its policy asks for a fresh bounded specialist. The root proposes the specialist's instruction, model and tools through [RT-RTE-create-subagent](runtime.md#rt-rte-create-subagent), then can invoke it through [RT-RTE-directed-child](runtime.md#rt-rte-directed-child). Creation admits a template; it does not execute a task. The API can reject invalid names, unavailable models or invalid tool requests, but its checks do not assess the specialist's competence. Unconditional baseline-tool injection also means that a requested short tool list is not a least-privilege guarantee. The parent must choose the actual request and what evidence to include; the DevOps prompt does not prescribe a structured handoff or acceptance rubric (SRC-1, `agent_library/agents/devops_gym_agent/agent.py`, `src/opensage/toolbox/general/orchestration_tools.py`).

In the default synchronous mode, a fresh child receives the request plus its own instruction and session state, without copied parent history. Explicit `use_parent_history=True` changes that boundary. The caller waits for extracted final text and a session ID, not the complete trajectory. Asynchronous mode instead acknowledges a running child and later posts text or error into the parent's inbox. Inline delivery may truncate messages and attempt a full-text file save. Consequently, the parent cannot infer that it has seen every child test result or tool effect simply because the child returned success. These selection and delivery mechanisms are already evidenced in [RT-RTE-directed-child](runtime.md#rt-rte-directed-child); no new identity is declared here (SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/orchestration/manager.py`, `src/opensage/orchestration/plugins/inbox_delivery.py`).

The child keeps its session after return, and both agents can have access to shared sandbox resources. This is a separate model context with a selected return, not a popped disposable frame or independent workspace. There is no inspected automatic patch merge or reconciliation step; the root must interpret returned advice and account for shared-file effects before proceeding.

### 4. Verification is requested; completion is a state flag

The agent-side verification is model-directed execution of available tests or inspection of effects. The root is instructed to verify before finishing, but `finish_task` sets a Boolean without inspecting tests, changed files or the child result. It is a completion declaration, not an acceptance certificate (SRC-1, `agent_library/agents/devops_gym_agent/agent.py`, `src/opensage/toolbox/finish_task/finish_task.py`).

> tool_context.state["task_finished"] = True
> return "Task finished"
> --- `src/opensage/toolbox/finish_task/finish_task.py`

The benchmark defaults `run_until_explicit_finish` to false. In the base evaluator, a programmatic or configured fake-user callback takes precedence; otherwise this default supplies no automatic continuation. Consequently the ordinary selected mode waits for manager idleness, not necessarily for a verified `finish_task` call. Enabling explicit-finish continuation changes that stopping policy but still does not turn the Boolean into a test oracle (SRC-1, `benchmarks/devopsgym/devops_gym.py`, `src/opensage/evaluation/base.py`; [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch)).

> run_until_explicit_finish: bool = False
> --- `benchmarks/devopsgym/devops_gym.py`

### 5. Driver grades the stopped work, then collects it

After the agent run returns, [WF-RTE-devops-grading](#wf-rte-devops-grading) copies the task's host grading script into the still-live container and executes it. The driver parses process exit and stdout rather than asking a model whether its work is correct. This is a concrete reference-outcome-provider interface within [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout), but the external script's assertions and expected outcomes remain uninspected. A zero exit with no `FAILED` token suffices; there need not be a `PASSED` line. This bounds what the result means.

Grading is a post-run classification, not a veto on exporting the product. The driver grades first, then delegates to base collection, attaches the grade and writes `automated_grade.json`. Base collection attempts to copy `/workspace` into `sandbox_output`, exports the session trace and writes metadata. Cleanup occurs after collection. Aggregate evaluation later reads grades into `results/evaluation_results.json`. These retained files make the result available to the benchmark consumer; model prose or idleness alone is not the delivered benchmark result (SRC-1, `benchmarks/devopsgym/devops_gym.py`, `src/opensage/evaluation/base.py`).

> grade_result = await self._run_grading(task)
>
> # Now let the base class collect /workspace and session trace
> info = await super()._collect_outputs(task, session)
> info["grade"] = grade_result
> --- `benchmarks/devopsgym/devops_gym.py`

Delivery is best effort for workspace contents: base collection logs a failed directory copy and continues. Trace export skips unavailable/empty sessions. A returned result and grade file therefore need not contain every expected artifact. Successful execution and complete export are unobserved here (SRC-1, `src/opensage/evaluation/base.py`).

### 6. Failure owners and recovery limits

A child runner exception is converted into `invocation_error` with partial text in the synchronous route, or an error inbox message in the asynchronous route. The manager releases instance state; the parent receives evidence of failure and must decide what to do. The chosen DevOps policy delegates when stuck but does not prescribe retries, rollback, or an alternative specialist on API rejection. Existing runtime records retain these branches and busy admission checks ([RT-RTE-directed-child](runtime.md#rt-rte-directed-child), [RT-RTE-create-subagent](runtime.md#rt-rte-create-subagent); SRC-1, `src/opensage/orchestration/manager.py`, `src/opensage/toolbox/general/orchestration_tools.py`).

The evaluator requests `stop_on_timeout=True` while waiting for idleness. A timeout marks `task.run_timed_out` and returns current session state for collection, so partial work can still be graded and exported. The inspected default timeout is 7200 seconds; the task loader's optional timing fields alone do not show that they override this base method (SRC-1, `src/opensage/evaluation/base.py`, `benchmarks/devopsgym/devops_gym.py`).

> completed = await manager.wait_until_idle(
>     task.session_id,
>     timeout=timeout_s,
>     stop_on_timeout=True,
> )
> --- `src/opensage/evaluation/base.py`

A missing grading script or copy failure produces an unknown grade; an execution exception produces false with exit code -1. A failed test produces false under the parser. The inspected grading and aggregation paths retain these classifications; they do not send the grade back to the root, reopen the task or restore pre-edit files. This is a bounded finding about these methods, not a claim that no external caller can rerun a task. An outer setup/run/collection exception instead causes the base evaluator to write `error.json`, attempt cleanup and re-raise. None of these cleanup/error-reporting paths establishes rollback of repository edits or exactly-once tool effects (SRC-1, `benchmarks/devopsgym/devops_gym.py`, `src/opensage/evaluation/base.py`).

> error_file = output_path / "error.json"
> --- `src/opensage/evaluation/base.py`

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-devops-grading
Label: DevOps post-run grading

Part of: [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout)

This is the benchmark-specific grading stage inside the supplied evaluation container route, not a second declaration of evaluation execution. Endpoints: stopped agent's live task container and external host `run-tests.sh` → copied `/tmp/opensage_run_tests.sh` → sandbox execution → fixed parser → task grade and later aggregate evaluation. Owner: `DevOpsGym._run_grading` invokes the sandbox, `_parse_pytest_result` decides pass/fail, and `_collect_outputs`/`evaluate` retain and consume the result. Context is the task sample, current modified workspace, sandbox and configured grading timeout. The grading script executes shell effects; it is not guaranteed read-only.

- Immediate return: grade mapping with passed true/false/null, exit code, stdout, stderr and timestamp; collection attaches it to returned task information.
- Later read-back: `automated_grade.json` is read by `evaluate()` into pass/fail/unknown lists and the retained aggregate `results/evaluation_results.json`.
- Delegated visibility: the benchmark driver receives test output; this stage does not deliver the grade back into the completed root or child invocation.
- Selection predicate: the current task sample selects its host `task_dir/run-tests.sh`; invocation follows agent return and precedes base artifact collection. Timeout and partial work can reach this same stage.
- Invalidation or expiry: the live container is cleaned up after collection; persisted grade files remain available to later aggregation, while reruns/file replacement can change their contents. No script/version pin or grade expiry rule is supplied by this path.
- Activation or effect: grading and report retention are wired; later aggregation uses the Boolean/null classification. Correct task assessment, successful grading and any resulting improvement in agent behavior are unobserved.
- Evidence limits: external grading-script assertions and task image contents are outside SRC-1; exit status and the absence of `FAILED` do not establish complete tests, patch correctness or leak-proof grading. No observed run is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: the model proposes workspace changes upstream; driver code invokes the externally supplied script and makes the final reported classification through its parser. Human contribution is upstream task/script/configuration supply, not per-product approval. Answer oracle: the external task script supplies the task-specific outcome-checking interface; OpenSage consumes its exit code and stdout. The oracle's internal reference criteria remain uninspected. Operating mode: bounded benchmark task, distinct from open CLI use. Improvement trigger: none wired in this inspected grading/aggregation stage; failure is reported rather than used to select a successor patch.

Admission/recovery: the trigger is completion or timeout return of agent execution. The proposed external product is the modified workspace. Grading can label it failed or unknown but does not prevent its export. It does not admit knowledge, instructions or changed runtime machinery. Agent guidance is [WF-BAP-devops-workflow](#wf-bap-devops-workflow); the grade, session trace and exported files persist, not a revised agent policy. Recovery is error classification/reporting; no automatic rework or rollback appears in the inspected methods.

Evidence: SRC-1 implementation, `benchmarks/devopsgym/devops_gym.py`, with sequencing in `src/opensage/evaluation/base.py`.

> if exit_code != 0:
>     return False
> lines = stdout.splitlines()
> for line in lines:
>     if re.search(r"\bFAILED\b", line):
>         return False
> # Must have at least one PASSED line, or simply trust exit_code == 0
> return True
> --- `benchmarks/devopsgym/devops_gym.py`

> passed_ids = [tid for tid, g in results.items() if g.get("passed") is True]
> failed_ids = [tid for tid, g in results.items() if g.get("passed") is False]
> unknown_ids = [tid for tid, g in results.items() if g.get("passed") is None]
> --- `benchmarks/devopsgym/devops_gym.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### WF-BAP-devops-workflow
Label: DevOps root workflow policy

Consumer: the `devops_gym_agent` root model. Channel: shipped natural-language `_SYSTEM_PROMPT`, supplied as the agent instruction by its factory. Force: model-interpreted workflow and verification policy, not a programmatic gate on `finish_task`. Horizon: invocations using this factory/instruction; no trace-directed policy update is established. Its general sequence is explore, plan, act, verify, finish; issue tasks add reproduction and available-test verification; stuck attempts request bounded delegation.

Closest supplied paths are [RT-BAP-tool-guidance](runtime.md#rt-bap-tool-guidance), concerning constructor skill/edit guidance, and [RT-BAP-dynamic-instruction](runtime.md#rt-bap-dynamic-instruction), concerning caller-created child instructions. This is distinct shipped root task-method guidance, not either retained referent. It does not establish successful compliance or mandatory specialist use.

Evidence: SRC-1 doctrine/design in executable factory source, `agent_library/agents/devops_gym_agent/agent.py`; `src/opensage/toolbox/finish_task/finish_task.py` establishes the weaker completion check.

> - Always verify your work before calling `finish_task`.
> - If you are stuck after several attempts, use `create_subagent` to delegate a
>   bounded subtask to a fresh agent.
> --- `agent_library/agents/devops_gym_agent/agent.py`

> ### Issue Resolving tasks
> - Locate the relevant source files referenced in the issue description.
> - Reproduce the bug if possible, then fix it.
> - Verify the fix with available tests (`mvn test`, `go test ./...`, etc.).
> --- `agent_library/agents/devops_gym_agent/agent.py`

## Annotations

#### On [RT-RTE-directed-child](runtime.md#rt-rte-directed-child)

Workflow role: optional fresh-perspective investigation after the DevOps root gets stuck, rather than a mandatory child phase. The root chooses the bounded request, interprets the selected return and decides whether to edit or verify again. API success means an invocation completed without a reported runner exception; it does not mean the child solution passed task tests. Parent acceptance remains model judgment, distinct from the driver's later grading stage.

#### On [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout)

Workflow-specific stopping and delivery: the DevOps-Gym default is single invocation without explicit-finish continuation unless another fake-user callback is supplied. Manager idleness or timeout return leads to benchmark-specific grading, followed by workspace/trace/metadata collection and cleanup. Grade rejection does not veto export; copy failures can leave incomplete artifacts. The concrete task-specific oracle interface is [WF-RTE-devops-grading](#wf-rte-devops-grading), whose external script criteria remain uninspected. This refinement does not extend the oracle to ordinary CLI tasks or other benchmarks.
