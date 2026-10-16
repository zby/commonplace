---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Agent Workflow Memory workflow account: WebArena task execution, evaluated trace admission and workflow delivery to the next task."
run-id: AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01
reviewed-boundary: "8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1"
---

# Agent Workflow Memory workflow report

## Workflow account

### Selected workflow and evidence limit

The representative workflow is the shipped WebArena pipeline: select a website's tasks, run one task, evaluate its trajectory, induce reusable workflow text, and supply that text to a later task agent. It was selected because one driver explicitly connects task execution to retained guidance and its subsequent consumption. This is a source-supported coordination design, not a reconstructed successful episode. The frozen evidence contains no observed execution; BrowserGym's environment loop and persistence are external responsibilities ([boundary](boundary.md#boundary-and-evidence); SRC-1, `webarena/pipeline.py`, `webarena/run.py`). The trace below follows that driver, not the independent Mind2Web benchmark or auxiliary basic agent.

### Request and stage ownership

The operator supplies `--website` and optionally a task-index range. The driver loads numeric JSON task configurations, sorts them by filename, selects configurations whose first site matches the requested website, and launches the corresponding task IDs sequentially. It passes a task identity and `workflow/{website}.txt` to `run.py`; it does not hand off a free-form objective to another autonomous planner. The task objective comes from the task environment/configuration. The parent owns stage scheduling, while each child owns its stage's computation ([WF-RTE-pipeline-handoff](#wf-rte-pipeline-handoff); SRC-1, `webarena/pipeline.py`, `webarena/run.py`).

`run.py` constructs a legacy agent and BrowserGym experiment with model configuration, observation/history flags and a default ten-step budget. It creates an empty workflow file if the selected file does not exist. BrowserGym receives the experiment configuration and agent factory through `ExpArgs`, owns observation/action scheduling and browser effects, and supplies experiment artifacts. After `exp_args.run()`, AWM renames the experiment directory to `results/{task_name}`. The browser host's implementation and terminal-success semantics are not frozen here; an AWM action return is therefore a handoff to the host, not proof that the task is delivered (SRC-1, `webarena/run.py`; [RT-RTE-browser-action](runtime.md#rt-rte-browser-action)).

### Within-task decisions and local recovery

For each host observation, the legacy agent builds a main prompt from the current observation and episode histories. It separately rereads the selected workflow file and appends its text to the system message. The model receives these messages and proposes an action; the local answer parser can reject malformed output and action-conversion failures. This consumer interprets workflow prose through the model, rather than dispatching an executable workflow graph ([RT-RTE-browser-action](runtime.md#rt-rte-browser-action), [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system); SRC-1, `webarena/agents/legacy/agent.py`). Workflow delivery is wired, but dependence on its content is unobserved. Main-prompt fitting does not cover the later workflow addition ([RT-CLM-context-budget](runtime.md#rt-clm-context-budget)).

The retry helper supplies a rejected answer and parser feedback to the same model. Valid output returns to the agent; exhausted parsing raises `ValueError`, which the agent converts to a null action plus error and message diagnostics. The default agent retry count is four. The agent also appends the selected action and returned thoughts to episode history. This is local model correction, not delegation to a critic agent or verification of task success (SRC-1, `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/utils/llm_utils.py`; [RT-RTE-browser-action](runtime.md#rt-rte-browser-action)).

> value, valid, retry_message = parser(answer.content)
> if valid:
>     return value
> --- `webarena/agents/legacy/utils/llm_utils.py`

> messages.append(HumanMessage(content=retry_message))
> --- `webarena/agents/legacy/utils/llm_utils.py`

The inspected helper also catches provider rate-limit errors and waits before retrying, with a default cumulative wait limit of thirty minutes; reaching that limit rethrows the provider error. The agent's shown catch is for `ValueError`, so the null-action recovery must not be generalized to all provider failures. No execution establishes whether the external host resumes or terminates after these outcomes (SRC-1, `webarena/agents/legacy/utils/llm_utils.py`, `webarena/agents/legacy/agent.py`).

> if rate_limit_total_delay >= rate_limit_max_wait_time:
>     logging.warning(
>         f"Total wait time for rate limit exceeded. Waited {rate_limit_total_delay}s > {rate_limit_max_wait_time}s."
>     )
>     raise
> --- `webarena/agents/legacy/utils/llm_utils.py`

### Trajectory verification and induction handoff

After the inference subprocess exits, the parent launches the evaluator with the task result directory. The evaluator reads the task intent, experiment log, final response if recognized, screenshots and summary reward. Text evaluation sends the last thought/caption, intent, response and action history to a model. Vision evaluation uses the last screenshot with intent, response and actions. It does not independently replay the browser state. A returned status equal to `success` becomes `rm: true`; other statuses become false. Thus the model can reject a trajectory for induction, but this is neither an independent expected-answer oracle nor a test of the workflow text later generated ([RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission); SRC-1, `webarena/autoeval/evaluate_trajectory.py`, `webarena/autoeval/evaluator.py`).

The next child receives the whole `results` root and the website-specific output path, not only the current task's trajectory. Under the default autoeval criterion it selects existing model-named evaluation files with a true first-record `rm`. It reloads intent/template metadata from task configurations, extracts thoughts and actions from admitted logs, removes some invalid or irrelevant actions, groups by intent template and randomly samples at most one trajectory per template by default. These transformations mean the induction model receives formatted query/thought/action examples, not complete host observations, screenshots, evaluator reasons or all admitted trajectories. There is no website predicate in this scan, so existing admitted results from other sites can reach the website-named output (SRC-1, `webarena/induce_prompt.py`; [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)).

The induction model receives the shipped instruction, a one-shot example and selected trajectories. The instruction asks for repeated, non-overlapping subroutines of at least two steps, variable abstraction and retention of invariant element values. This establishes requested abstraction, not that a returned workflow satisfies it. The writer appends fixed action reminders and overwrites the selected file without per-content human approval or a generated-workflow verification stage. The previous workflow is not an input to the proposal. Rejected or unparseable trajectories are skipped; there is no rollback transaction in the shown write path (SRC-1, `webarena/prompt/instruction.txt`, `webarena/induce_prompt.py`; [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)).

### Rejection, broken handoff and delivery boundaries

The default evaluator writes `gpt-3.5-turbo_autoeval.json`, while the default inducer looks for `gpt-4o_autoeval.json`. The parent passes neither child a model override. A newly evaluated task is consequently not selected through that default filename handoff; old matching files can still be selected. Even with zero selected examples, the inducer calls the model and can replace the workflow file. This is a static obstacle to the intended evidence-fed update, not an observed failed run (SRC-1, `webarena/pipeline.py`, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`; [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)).

A separate error branch inside `process_sample` returns a dictionary rather than the normal list. That dictionary is serialized to the evaluation file, whereas the inducer reads `record[0]["rm"]` without guarding that read. If the failed evaluator and inducer use a matching model name, this shape mismatch can abort induction instead of cleanly rejecting the trace. Earlier log/configuration failures are outside this evaluator try block. The parent only waits for child exit and proceeds; it neither retries failed stages nor verifies artifact existence before launching the next stage (SRC-1, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`, `webarena/pipeline.py`).

> except Exception as e:
>     print(f"Error on {idx}, {e}")
>     print(traceback.format_exc())
>     return {
>         "idx": idx,
>         "gt": traj_info["eval"],
>         "rm": None,
>         "thoughts": None,
>         "uid": traj_info["traj_name"],
>     }
> --- `webarena/autoeval/evaluate_trajectory.py`

The intended delivered artifacts have two boundaries. A task agent hands an action or user-message action to BrowserGym; actual browser execution and task completion remain host-dependent. The induction child delivers a rewritten local workflow file; the next task's legacy agent rereads it into a system message. A persisted file and that message supply establish neither task success nor beneficial workflow use. No pipeline-wide acceptance receipt, successful run trace or causal comparison is supplied (SRC-1, `webarena/run.py`, `webarena/agents/legacy/agent.py`, `webarena/induce_prompt.py`; [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system)).

Inspection here covers the complete WebArena driver, caller, legacy agent, evaluator, neural inducer and extraction instruction, plus the sequential `retry` helper in `webarena/agents/legacy/utils/llm_utils.py`. These are implementation and doctrine/design evidence under SRC-1, not new observed-run evidence. The account adds workflow-level inspection of parent return handling, the evaluator-error result shape and provider retry ownership beyond the provisional runtime account.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-pipeline-handoff
Label: WebArena pipeline stage handoff

Source-native progression: operator website/range → sorted task IDs → inference child → evaluation child → induction child → next task. Owner: `webarena/pipeline.py`; each child owns its own computation and the external BrowserGym host owns browser effects. The state passed between stages is task/path arguments and local files, not an in-memory conversation between subagents (SRC-1, `webarena/pipeline.py`).

Distinct identity: this record describes the scheduling edge across [RT-RTE-browser-action](runtime.md#rt-rte-browser-action) and [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), not either model/action or admission route itself. It spans those routes and is not a material part of exactly one of them.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Each child exit releases the parent's wait; the parent then launches the next stage or task without checking the return code.
- Later read-back: The parent passes the same website workflow path to subsequent inference children; the legacy agent reads the rewritten file. Evaluation files and stored trajectories are read by later induction calls.
- Delegated visibility: Inference receives task identity and workflow path; evaluation receives the task result directory; induction receives the full results root and website output path. Each child independently opens the files it needs.
- Selection predicate: Numeric task configurations sorted by filename, first-site equality to the operator's website, and the requested start/end slice; child selection rules remain with the cited admission route.
- Invalidation or expiry: No stage freshness or success check in this driver; workflow replacement is performed by induction and existing result directories remain candidates.
- Activation or effect: Sequential subprocess orchestration and file/path handoffs are wired; completion of these stages and successful evidence-fed updating are unobserved.
- Evidence limits: External host and provider behavior are not frozen; default model-filename mismatch interrupts intended evaluation-to-induction selection; no supplied execution artifacts.

Trigger and control: the human chooses website/range and starts the run, not individual workflow approval. The parent schedules software/model stages; the evaluator can reject trajectory candidates, and the induction writer admits replacement text. Operating mode is a bounded benchmark sequence. The parent consults no answer oracle, tests no generated workflow and supplies no retry or rollback. Guidance and content admission belong to [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), not the scheduler.

> process = Popen([
>     "python", "induce_prompt.py",
>     "--result_dir", "results",
>     "--output_path", f"workflow/{args.website}.txt",
> ])
> process.wait()
> --- `webarena/pipeline.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-browser-action](runtime.md#rt-rte-browser-action)

Workflow recovery boundary: parser feedback returns to the same action model. Parse exhaustion returns diagnostics and a null action; provider rate-limit exhaustion instead propagates from the sequential retry helper. BrowserGym's reaction is uninspected. This adds recovery ownership, not task-success verification (SRC-1, `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/utils/llm_utils.py`).

#### On [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)

Workflow handoff check: parent stage completion is not artifact acceptance. Besides the default filename mismatch, a caught evaluator exception serializes a dictionary where induction expects a list, so the error signal is not a reliable clean-rejection handoff. Induction scans the accumulated results root rather than only the just-completed task, and a zero-example selection still reaches model generation and whole-file writing (SRC-1, `webarena/pipeline.py`, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`).
