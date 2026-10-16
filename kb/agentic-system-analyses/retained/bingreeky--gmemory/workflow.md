---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "GMemory workflow account: ALFWorld AutoGen task execution, repetition-triggered delegation, environment verification and retention before result delivery."
run-id: AAS-2026-10-15-gmemory-a2192cc823f7-01
reviewed-boundary: "7b581c51d993bd600df14691d101d7e601040cc6"
---

# GMemory workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is one ALFWorld task in the shipped AutoGen runner with `g-memory` explicitly selected. It connects retained experience, solver action, conditional helper delegation, environment feedback, memory update and result recording in one implemented schedule. It is selected because its repetition branch exposes both a consequential handoff and the difference between attempted recovery and correctness verification. It is not a composite assembled from the three workflow implementations. The [boundary](boundary.md) fixes SRC-1 at the revision above; [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions) supplies the shared route identity.

This is an implementation account, not a reproduced episode. No target program or provider was run, and no authenticated trace establishing this selected workflow's execution is supplied. Source inspection here covers SRC-1, `tasks/run.py`, `tasks/mas_workflow/autogen/autogen.py`, `tasks/mas_workflow/autogen/autogen_prompt.py`, `tasks/mas_workflow/format.py`, `mas/agents/base.py`, `mas/memory/mas_memory/memory_base.py` and `tasks/envs/alfworld_env.py`. These provide implementation evidence; the helper and formatting prompt bodies provide declared instructions, not evidence of compliance. Memory internals below rely on the supplied runtime records rather than a new audit.

### Request and context handoff

The operator selects the benchmark, workflow, model, memory and step/retrieval settings. `build_mas` creates the shared reasoning and memory modules once. `run_task` iterates dataset tasks, asks the environment for the task description, supplies static few-shot examples, and installs dataset instructions on both hired agents before calling `schedule`. Thus delegation stays within one Python process and shared reasoning backend, not independently authorized remote workers (SRC-1, `tasks/run.py`, `tasks/mas_workflow/autogen/autogen.py`; [RT-CMP-gpt-chat](runtime.md#rt-cmp-gpt-chat)).

The schedule rejects missing task-main or task-description fields, resets the environment and creates a new task context. Retrieval occurs once at task start. Successful records become description, key steps and detailed trajectory; the failed-record return is discarded. Rules are optionally projected to each role and truncated. Solver calls then receive static examples, selected retained examples, role-specific rules and the current description/trajectory. The selection and persistence mechanism is [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), not a guarantee that agents follow memory (SRC-1, `tasks/mas_workflow/autogen/autogen.py`, `tasks/mas_workflow/format.py`).

Each `Agent.response` constructs a fresh system/user message pair. The previous provider conversation is not passed through that adapter. However, the task's accumulated action/observation text is copied into subsequent user prompts: `summarize` concatenates description and trajectory rather than compacting them. This separates call frames without removing the selected task history. Only returned action text escapes the helper call into scheduling; private model processing is not visible. Persistent retrieval supplies the separate later-task reload path (SRC-1, `mas/agents/base.py`, `mas/memory/mas_memory/memory_base.py`; [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)).

### Action proposal and conditional delegation

For each environment step, the solver proposes one text action, which the environment adapter normalizes. Code checks whether that action equals both preceding executed actions. If so, it calls the `ground_truth` persona instead, rebuilding the user prompt with that role's rules and the same accumulated task trajectory. The helper does not receive an explicitly appended, unexecuted current solver proposal. It sees the earlier repeated actions through trajectory text. The helper's returned action replaces the solver proposal; the schedule does not require agreement or send the replacement back to the solver for approval (SRC-1, `tasks/mas_workflow/autogen/autogen.py`; [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)).

The helper prompt asserts that the earlier approach is wrong:

> NOTE: ** Your approach must avoid being consistent with the previous output's approach (as the previous output comes from a solver agent that has already fallen into a misconception, making it definitely wrong). **
> --- `tasks/mas_workflow/autogen/autogen_prompt.py`

That assertion is stronger than the repetition predicate. Neither the trigger nor the helper persona establishes an answer oracle. A wrong but varying proposal avoids this handoff; a repeated valid proposal can trigger it. The scheduler owns escalation, the models propose alternatives, and no per-action human approval is wired in this path. The selected agent's prompt/action is recorded, then the action reaches `env.step`. Observation, reward and action are appended to the task context for the next step (SRC-1, `tasks/mas_workflow/autogen/autogen.py`; [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)).

### Verification and failure handling

For ALFWorld, the adapter derives observations and `done` from the simulator. It marks `think:` actions and `Nothing happens.` observations with negative step reward. That feedback is returned to the next model prompt; it is not a gate rejecting an action before execution or an automatic trigger for the helper. The schedule ends environment interaction on `done` or outer-step exhaustion, conditional on each inner call returning (SRC-1, `tasks/envs/alfworld_env.py`, `tasks/mas_workflow/autogen/autogen.py`).

Final task acceptance is operationally the adapter's `done` flag, not the helper's opinion:

> success = self.done
> reward = 1.0 if success else 0.0
> message = "You successfully finished this task!" if success else "You failed the task."
> --- `tasks/envs/alfworld_env.py`

This establishes how the shipped adapter labels success, not independent simulator correctness. A nonterminal task at exhaustion receives failure feedback. There is no task restart in this schedule: failure proceeds to retention like success. Retry handling is narrower than end-to-end recovery. Solver/helper exceptions have local counters, but empty strings retry before advancing those counters; provider attempts and outer steps do not establish a finite task deadline. Exhausted exceptions also do not enforce a clean failed-action return. These limits and their minimum source passages are retained in [RT-CLM-bounded-recovery](runtime.md#rt-clm-bounded-recovery) (SRC-1, `tasks/mas_workflow/autogen/autogen.py`, `mas/llm.py`).

### Retention and delivery

After final feedback, AutoGen saves the task with the environment label and feedback, then calls `backward(final_done)`. Both successful and failed completed schedules therefore feed retention. [RT-RTE-task-retention](runtime.md#rt-rte-task-retention) supplies the extraction/admission mechanism; [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) supplies count-triggered rule revision and retrieved-rule score adjustment. Those records distinguish software/model admission from semantic verification and state the nontransactional persistence limits. Saving or adjusting guidance does not demonstrate that the helper recovered the task or that later solving improves (SRC-1, `tasks/mas_workflow/autogen/autogen.py`, `mas/memory/mas_memory/GMemory.py`).

The task's delivered product is a benchmark reward/success tuple followed by recorder output, not a separate prose answer to a user. Delivery to the runner occurs only after synchronous save and backward complete. The runner then records the result and advances:

> reward, done = task_manager.mas.schedule(task_config)
>
> task_manager.recorder.task_end(reward, done)
> --- `tasks/run.py`

For ALFWorld, `task_end` updates category counts and logs completion and cumulative rates. A save/maintenance exception can therefore prevent result delivery even after the environment has finished; no rollback or reporting fallback is established by the inspected schedule/runner. This ordering is part of the workflow contract, not observed reliability (SRC-1, `tasks/mas_workflow/autogen/autogen.py`, `tasks/run.py`, `tasks/envs/alfworld_env.py`; [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)).

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

#### On [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)

Workflow handoff: repetition substitutes a helper-generated action directly; it is neither a correctness review nor a return-to-solver revision cycle. The helper receives role-selected memory and existing trajectory, not an explicitly appended current rejected proposal. Local call frames expose selected task context and return action text, not an independent worker execution environment.

Workflow verification: in the selected ALFWorld mode, environment `done` supplies the final success label. Negative step reward informs later context but does not itself invoke helper delegation. Step exhaustion delivers failure through normal retention rather than automatic task restart.

#### On [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

Workflow delivery dependency: AutoGen's save and backward occur before the tuple returns to `run_task`; result recording is downstream of both. Environment completion alone is therefore insufficient for runner-visible delivery when synchronous memory work fails.
