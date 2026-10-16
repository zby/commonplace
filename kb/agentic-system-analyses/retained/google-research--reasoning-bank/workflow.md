---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ReasoningBank's shipped SWE-Bench workflow from instance scheduling through shell actions, prediction delivery and cross-task advice admission."
run-id: AAS-2026-10-14-reasoning-bank-f0bedcab086c-01
reviewed-boundary: ed80611788292ea739f1effd31f16c53823b8a0d
---

# ReasoningBank workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects the shipped SWE-Bench batch workflow because one driver connects task scheduling, retained-advice retrieval, iterative shell execution, prediction delivery, judging and new advice admission. It does not combine unrelated capabilities into an imagined workflow. The WebArena and scaling routes remain outside this selective trace, not outside the run's boundary. The principal baseline records are [RT-RTE-swe-task](runtime.md#rt-rte-swe-task) and [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission).

Evidence is SRC-1 implementation at the frozen commit, with no observed run or causal experiment. This member inspected `SWE-Bench/run.sh`, `third_party/src/minisweagent/run/extra/swebench.py` and `third_party/src/minisweagent/agents/default.py`, and added inspection of `third_party/src/minisweagent/run/utils/save.py` to establish what failure persistence contains. Code establishes coordination and return paths, not successful execution, correct patches or improved later performance. Provider services, dataset contents and deployed containers remain external evidence limits as stated in [the boundary](boundary.md#boundary-and-evidence).

### Request, scheduling and advice handoff

The operator's launcher selects Gemini Flash, verified/test instances and one worker. The batch driver loads the dataset, applies filtering/slicing and optional shuffle, and normally removes instances already represented in `preds.json`. It submits the remaining instances to a thread pool and waits for their futures. Thus the driver, not a foreground model, delegates instances and owns scheduling; a worker thread is not an independently planning sub-agent (SRC-1, `SWE-Bench/run.sh`, `third_party/src/minisweagent/run/extra/swebench.py`).

> with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
>     futures = {
>         executor.submit(process_instance, instance, output_path, config, progress_manager): instance[
>             "instance_id"
>         ]
>         for instance in instances
>     }
> --- `third_party/src/minisweagent/run/extra/swebench.py`

Each worker receives an instance, output directory, configuration and progress manager. `process_instance` removes the prior prediction and trajectory for that ID, creates the configured task model, reloads the model-named memory bank, and retrieves one prior query's record. It joins that record's memory-item strings and passes the resulting text with the problem statement to the task agent. The full bank does not enter the task-agent context. Retrieval and its cache effects are covered by [RT-RTE-swe-task](runtime.md#rt-rte-swe-task); selected advice enters the advisory system-message channel described by [RT-BAP-system-memory](runtime.md#rt-bap-system-memory). Delivery does not show that the model relied on it.

Environment startup and agent construction occur inside the worker's execution try block, but model creation and memory reload/selection precede it. This placement matters: retrieval/setup failure can escape without the trajectory/prediction recovery used for failures inside the block (SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`).

### Iterative actions and local rejection

`DefaultAgent.run` clears its messages, installs the system instruction plus selected advice, adds the task message and repeatedly calls `step`. The model proposes command text; the parser accepts exactly one bash block; the environment receives its contents for execution. Observations are added as user messages for the next query. The default Docker effect boundary and its deployment limits are supplied by [RT-RTE-swe-task](runtime.md#rt-rte-swe-task). The agent owns turn progression, while the executor owns shell effects.

The parser rejects malformed responses, not semantically wrong patches or unsafe shell operations. Timeout and format errors produce feedback in the same task context, after which the model can propose another command. The driver does not delegate these retries to a separate critic. [WF-RTE-action-recovery](#wf-rte-action-recovery) establishes this local failure path. It is implemented recovery capacity, not evidence that a retry succeeded.

Task completion is a protocol marker in shell output. It is not benchmark acceptance:

> lines = output.get("output", "").lstrip().splitlines(keepends=True)
> if lines and lines[0].strip() in ["MINI_SWE_AGENT_FINAL_OUTPUT", "COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT"]:
>     raise Submitted("".join(lines[1:]))
> --- `third_party/src/minisweagent/agents/default.py`

`Submitted` and `LimitsExceeded` both terminate the loop and return an exit-status/result tuple. Other exceptions inside the worker's try block are logged and converted to their class name and error text. A returned result therefore need not be a submitted patch (SRC-1, `third_party/src/minisweagent/agents/default.py`, `third_party/src/minisweagent/run/extra/swebench.py`).

### Delivery precedes judging and memory admission

The worker's finally block saves a trajectory, writes a prediction entry and marks instance progress ended before judging or generating advice. Prediction persistence defines delivery to the batch output file, not correctness or complete memory-loop success:

> output_data[instance_id] = {
>     "model_name_or_path": model_name,
>     "instance_id": instance_id,
>     "model_patch": result,
> }
> output_path.write_text(json.dumps(output_data, indent=2))
> --- `third_party/src/minisweagent/run/extra/swebench.py`

The writer stores `result` without requiring a `Submitted` exit status. `save_traj` stores exit status, submission, statistics and messages; when no agent exists, the initialized message list stays empty. Thus an environment-startup failure can persist an error result and an empty transcript rather than a performed task trajectory (SRC-1, `third_party/src/minisweagent/run/utils/save.py`, `third_party/src/minisweagent/run/extra/swebench.py`).

> "messages": [],
> "trajectory_format": "mini-swe-agent-1",
> --- `third_party/src/minisweagent/run/utils/save.py`

The worker then reloads the saved messages, removes all system messages, joins the remaining contents and supplies that transcript and the task to a separate direct GenAI judge. Consequently selected advice is excluded as a system-message body, though an assistant may have repeated or discussed it. A judge response containing `success` selects success induction instructions; other responses select failure instructions. This classification changes the generator's guidance, not whether advice is admitted. Both branches generate text and append the blank-line-split output to the bank. No external SWE-Bench grading result or human approval gates this route; the baseline record retains the judge predicate and admission evidence ([RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)).

These judge and generator calls have separate contexts and return only a label and advice to host processing. They are not a negotiation among persistent agents. Later instances reload the bank and may receive selected advice. That closes the implemented persistence/supply chain; it does not establish subsequent behavioral dependence, learning or improvement.

### Outer failure and continuation limits

The coordinator catches future exceptions and reports them through logging/progress. It does not automatically rerun the instance:

> except Exception as e:
>     instance_id = futures[future]
>     logger.error(f"Error in future for instance {instance_id}: {e}", exc_info=True)
>     progress_manager.on_uncaught_exception(instance_id, e)
> --- `third_party/src/minisweagent/run/extra/swebench.py`

A judge, generator or append failure after prediction persistence can therefore leave a delivered prediction and saved trajectory without new advice. On a later ordinary batch invocation, the existing prediction key can cause that instance to be skipped, regardless of whether its admission stage completed. Recovery requires an operator-selected redo or other external intervention, rather than a shipped automatic admission-resume step in this driver (SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`).

> if not redo_existing and (output_path / "preds.json").exists():
>     existing_instances = list(json.loads((output_path / "preds.json").read_text()).keys())
>     logger.info(f"Skipping {len(existing_instances)} existing instances")
>     instances = [instance for instance in instances if instance["instance_id"] not in existing_instances]
> --- `third_party/src/minisweagent/run/extra/swebench.py`

The shipped one-worker launcher serializes instance processing. The CLI also permits multiple workers; prediction writes have a lock, but bank/cache writes do not share that protection in the inspected driver. Accordingly the serial handoff account is not a universal concurrency guarantee ([RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-action-recovery
Label: Action rejection and same-context recovery

Part of: [RT-RTE-swe-task](runtime.md#rt-rte-swe-task)

This is the local parser/timeout recovery part of the supplied coding task loop, not a duplicate of its complete dataset-to-prediction route. Owner: `DefaultAgent.run`, with detection in `parse_action` and `execute_action`. Endpoints: malformed model response or execution timeout → nonterminating exception → user-message feedback → next step in the same agent. SRC-1 implementation, `third_party/src/minisweagent/agents/default.py`.

The model proposes the replacement action; code decides format acceptance and recognizes timeout exceptions. No human review or expected-answer oracle is involved. Operating mode is the bounded task loop. The predicate checks bash-block count, not action safety or task correctness. Timeout handling does not roll back shell effects already made before interruption; it requests another action.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rejected action or timeout becomes a rendered error message; the run loop proceeds rather than returning a task result.
- Later read-back: inapplicable — this recovery path does not write retained advice; separate finally-block admission can later consume the transcript.
- Delegated visibility: the task model receives the error as a user message alongside its existing task context; timeout feedback can include partial command output.
- Selection predicate: bash-block count differs from one, or environment execution raises a recognized timeout exception; terminating exceptions take the separate return branch.
- Invalidation or expiry: feedback remains in the current task message list until task context reset; no separate recovery state is persisted here.
- Activation or effect: rejected format does not reach the executor; timeout feedback reaches the next model query, but successful corrective behavior is unobserved.
- Evidence limits: source establishes feedback and continuation, not successful repair, semantic verification or rollback of prior shell effects.

> except NonTerminatingException as e:
>     self.add_message("user", str(e))
> except TerminatingException as e:
>     self.add_message("user", str(e))
>     return type(e).__name__, str(e)
> --- `third_party/src/minisweagent/agents/default.py`

> raise FormatError(self.render_template(self.config.format_error_template, actions=actions))
> --- `third_party/src/minisweagent/agents/default.py`

> except TimeoutError:
>     raise ExecutionTimeoutError(self.render_template(self.config.timeout_template, action=action, output=""))
> --- `third_party/src/minisweagent/agents/default.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-swe-task](runtime.md#rt-rte-swe-task)

Workflow delivery boundary: the finally block writes a trajectory and prediction before the post-task judge runs. The prediction's `model_patch` field receives the returned result without requiring submission status. Local recovery is isolated in [WF-RTE-action-recovery](#wf-rte-action-recovery); neither its parser acceptance nor the terminal output marker verifies patch correctness. The Workflow account retains the additional SRC-1 passages supporting these distinctions.

#### On [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)

Workflow continuation boundary: advice admission occurs after prediction persistence and progress-end reporting. A later ordinary invocation skips existing prediction keys, so a partially completed instance can be skipped without resuming its missing admission stage. The outer future handler reports errors but does not schedule a replacement attempt. The Workflow account retains SRC-1 implementation evidence for ordering and the skip/error predicates. No operation conclusion is promoted beyond the baseline's uninspected status.
