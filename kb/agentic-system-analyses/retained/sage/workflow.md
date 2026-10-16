---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SAGE workflow account: sequential normal-evaluation tasks, skill handoffs, execution-feedback rejection and bounded delivery."
run-id: AAS-2026-10-15-sage-d0de15ae5730-01
reviewed-boundary: "3c9244e82244abb1adc5467ee601a03ba0f433a0"
---

# SAGE workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped normal-evaluation workflow: a configured agent solves a sequence of AppWorld tasks and carries extracted functions into later tasks. It exposes request routing, iterative model/executor handoffs, task evaluation, skill admission and later consumption in one connected path. It is not a reconstruction joining the RL trainer to the expert-generation path. The baseline is [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop); the training and expert routes remain distinct.

All source findings use SRC-1 at the boundary's frozen commit. Evidence is implementation, except where the prompt supplies doctrine/design. No supplied execution trace establishes that these handoffs occurred successfully. This inspection covers `patches/appworld/experiments/configs/sage_test_normal.jsonnet`, `patches/appworld/experiments/code/skill_library_agent/run.py`, the normal-task methods in `patches/appworld/experiments/code/skill_library_agent/agent.py`, and `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`. Additional coverage includes the full `patches/appworld/experiments/code/skill_library_agent/logger.py` for delivery/progress semantics and the full `patches/appworld/experiments/prompts/skill_library_agent.txt` for the requested terminal action. Upstream AppWorld execution and evaluator internals remain outside the frozen source set; no environment-isolation or benchmark-adequacy guarantee follows.

### 1. Operator request becomes a bounded task sequence

The normal config selects the skill-library agent, the `dev` dataset, default retrieval, a 40-step cap and skill accumulation. It does not enable `use_label`; the base constructor defaults that flag to false. The runner accepts an optional single task ID, otherwise loads dataset task IDs. It first loads each task to check loadability, constructs one agent, then invokes `solve_tasks`. That method partitions task IDs for a process and visits its assigned IDs sequentially. This is task dispatch to one continuing agent, not delegation to independent reasoning agents. Separate process partitions do not establish a shared mutable skill library. SRC-1, `patches/appworld/experiments/configs/sage_test_normal.jsonnet`, `patches/appworld/experiments/code/skill_library_agent/run.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).

### 2. A fresh task world receives selected functions, not the previous conversation

For each task, `solve_task` opens an AppWorld context. Base initialization resets messages, step count and task logging. The subclass renders task instruction, supervisor identity, date, app descriptions and required APIs into its prompt. Its agent-level function list survives this reset. Default retrieval first matches task IDs containing the scenario's `_1` identifier, then `_2`, retaining the first encountered definition for each name. This selection is identifier-based, not a semantic applicability test. The selected source is executed before the first model call. Unless execution returns exactly `Execution successful.`, its prompt text is cleared. This suppresses guidance; it does not prove removal of already executed effects. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`; [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [RT-BAP-function-execution](runtime.md#rt-bap-function-execution).

The boundary between tasks therefore discards conversational and live-world context while selected Python source crosses it. The next model sees a newly rendered task prompt, not the previous task's full observations or variable bindings. Constructor loading from a separate predefined-library path is another possible input; output JSONL is not automatically reloaded as restart recovery. Source wiring supports this handoff, not correct selection or useful reuse.

### 3. Model and executor alternate until a stop predicate holds

The model receives messages and chooses Python. With the normal config's `ignore_multiple_calls`, extraction returns the first complete fenced Python block; other text or later blocks do not automatically become actions. A partial terminal block can also supply code. The base agent sends the returned `ExecutionIO` content to `world.execute`. Execution output returns to the same agent, which appends it as a user message for the next model call. Long observations are cut to their first 12,000 characters and followed by a reminder. This is observation truncation, not a summary or a demonstrated full-history compactor. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).

The prompt requests API inspection, small code chunks, applicable skill reuse and function creation. These instructions do not constitute executable admission checks; [RT-CLM-function-rules](runtime.md#rt-clm-function-rules) distinguishes requested structure from enforcement. The executor receives code, not a separate request for a human's approval. AppWorld owns API effects and task-completion reporting; the agent owns step progression and cost checks. A reported completion or exceeded cost stops the loop, as does exhausting the step range. None of those predicates alone establishes a correct answer.

### 4. Failure feedback filters future skill candidates, with a final-step gap

The inspected rejection path is [WF-RTE-failed-code-filter](#wf-rte-failed-code-filter), a material part of the evaluation loop. When another step begins after an execution output containing `Execution failed.`, the agent removes its latest code candidate from `code_list`. It still delivers the failure observation to the model, which may choose a repair. Deleting the candidate is not undoing its world effects or erasing its assistant message. Nor does this handler run on the final output when the base loop terminates before another call to the next-step method. Consequently, the code does not establish that every execution-failing chunk is excluded from later extraction.

A different fallback handles exceptions during generation or response processing: it substitutes `apis.supervisor.complete_task()`. This asks the environment to mark completion rather than diagnosing or repairing the underlying failure. The base agent still evaluates the task separately. There is no normal-task retry loop comparable to expert generation's retry route. These are bounded implementation findings, not evidence that provider failure, model repair or successful recovery occurred. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).

### 5. Delivery has separate environment, evaluation and retention outcomes

The prompt asks the model to complete through the supervisor API and pass any requested informational answer there:

> (5) Once you have completed the task, make sure to call apis.supervisor.complete_task(). If the task asked for some information, return it as the answer argument, i.e. call apis.supervisor.complete_task(answer=<answer>). Many tasks do not require an answer, so in those cases, just call apis.supervisor.complete_task() i.e. do not pass any argument.
> --- `patches/appworld/experiments/prompts/skill_library_agent.txt`

This is the requested user-result channel, not evidence that a final answer was actually delivered. After stopping, the base agent calls `world.evaluate`, computes passed tests divided by total tests and returns true only for a fraction of one. Thus completion signaling and benchmark acceptance are separate. The enclosing `solve_tasks` uses the Boolean as the next call's previous-success argument; the experiment runner itself returns no aggregate answer. SRC-1, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/run.py`; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).

In the normal configuration, post-task extraction is not vetoed by a failed evaluator result. It combines retrieved definitions with functions parsed from the surviving code list, replaces duplicate names within that extraction, appends records to the continuing agent list and writes output JSONL. A later task may select those records. This is software admission without per-function human approval, not a guarantee that accepted functions solved the task. The alternate `use_label` branch depends on the previous task's result, not the current one. SRC-1, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).

Finally, logging marks a task processed rather than benchmark-correct:

> def complete_task(self):
>     self.num_tasks_completed += 1
> --- `patches/appworld/experiments/code/skill_library_agent/logger.py`

The call has no success argument, and the base agent invokes it after extraction independently of `task_success`. Progress display therefore cannot substitute for evaluator acceptance. Execution effects, an informational supervisor answer, a returned success Boolean and retained skill records are different workflow products; this frozen source demonstrates their wiring, not their quality or successful production.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-failed-code-filter
Label: Failed code filtering

Part of: [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)

This record isolates the next-step execution-feedback filter, rather than redeclaring the whole task loop or its function store. Endpoints: previous execution output and latest code candidate → string check in `next_execution_inputs_and_cost` → candidate removal and model-visible failure feedback → possible next model action. Owner: `SkillLibraryAgent`; context/state: `code_list`, messages and the current task world. The model proposed the code; software removes the latest candidate when the failure marker is present, without a human veto or semantic reference answer. Operating mode is bounded normal evaluation. Trigger is a subsequent next-step call with nonempty execution outputs; proposed change is removing a chunk from the material later scanned for skills. Guidance for replacement remains the task prompt and returned execution observation. What persists after task extraction is parsed function source, not a criticism ledger. There is no world rollback in this filter.

- Immediate return: a shortened candidate list, then the next generated code action; the failure observation is appended to messages.
- Later read-back: post-task extraction scans surviving code chunks for function records; later task initialization can consume those records through the parent route.
- Delegated visibility: the same task model receives the stripped, possibly truncated observation plus reminder; no independent repair agent is invoked.
- Selection predicate: nonempty execution outputs, `Execution failed.` in their content and a nonempty code list; deletion selects the last list entry.
- Invalidation or expiry: the deleted candidate is unavailable to this extraction list; task initialization resets the list. The assistant message and already attempted effects are not removed by this deletion.
- Activation or effect: list deletion and feedback delivery are wired; successful repair and exclusion of every failing final chunk are not established.
- Evidence limits: a final output may never enter this handler after completion, cost stopping or step exhaustion. The marker is execution feedback, not a reference test for every function's correctness. No run evidence is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`.

> if "Execution failed." in last_execution_output_content and len(self.code_list)!=0:
>     del self.code_list[-1]
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

> self.messages.append({"role": "user", "content": last_execution_output_content})
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)

Workflow-specific acceptance distinction: the supervisor completion request is the prompt's result channel; loop termination is a control decision; `world.evaluate` determines benchmark acceptance; library extraction and logger completion proceed without requiring current-task success in the normal configuration. Only the last of these indicates that a task was processed by the loop. None establishes observed delivery. Failure recovery has two distinct owners: the next model call can respond to execution feedback, whereas the exception handler substitutes a completion request. The next-step filter has its separately scoped route above.

#### On [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions)

Workflow handoff consequence: resetting task messages does not reset the continuing agent's function list. The boundary transfers selected source definitions, not the previous task's conversation or Python variable values. A failed install clears model-visible skill text but does not constitute transactional recovery of the task world.
