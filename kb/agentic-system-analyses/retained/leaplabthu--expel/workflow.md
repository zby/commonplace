---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ExpeL workflow tracing HotpotQA experience gathering through acting, failure reflection, trajectory admission and checkpoint delivery."
run-id: AAS-2026-10-14-expel-efd908f05069-01
reviewed-boundary: e41ec9a24823e7b560c561ab191441b56d9bcefc
---

# ExpeL workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the README's HotpotQA experience-gathering command, with `testing=false` and `resume=false`. It covers a training task through acting, an optional failed-attempt retry, experience retention and delivery of the training batch's files. It was selected because it exercises the shipped scheduling, verification and recovery mechanisms that produce inputs for later insight extraction. It is not an invented chain of independent capabilities. Insight extraction and held-out evaluation are later, separately invoked workflows, not automatic continuations of this command ([RT-RTE-training-loop](runtime.md#rt-rte-training-loop), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission); SRC-1: `README.md`, `train.py`).

> python train.py benchmark=hotpotqa run_name=<train-run-name> testing=false resume=false
> --- `README.md`

All findings concern static implementation or source-native design at the frozen revision. No completed task, reflection, saved checkpoint or execution trace was supplied. Additional focused inspection covers `train.py`, `configs/train.yaml`, `configs/agent/expel.yaml`, `agent/expel.py`, `agent/reflect.py`, `agent/react.py`, `envs/hotpotqa/hotpotqa.py` and `utils.py`; the README supplies the invocation's doctrine/design evidence. These are existing SRC-1 paths, not new sources. This selective trace does not certify other benchmarks or every branch.

### Request and consequential handoffs

**1. Operator to driver.** The operator supplies benchmark, run name and mode overrides. Hydra defaults select HotpotQA and ExpeL, but `configs/train.yaml` has `testing: true`; the selected README command explicitly overrides that value. Without this override the model-call sites ask for response text through `input()`. For the selected non-testing path, the driver obtains the provider credential, loads configured tasks, and constructs the agent with benchmark prompts/examples, adapter and limits. A fresh run can ask permission to overwrite an existing checkpoint. This is run-level authorization, not approval of individual experiences (SRC-1: `train.py`, `configs/train.yaml`, `agent/react.py`; [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore)).

**2. Driver to actor to adapter.** While tasks remain, the driver calls training mode. `ExpelAgent.run` dispatches to `ReflectAgent.run`, which invokes the ReAct loop. The driver owns task scheduling; Python agent code owns trial progression. The actor receives the task, shipped instructions/examples and accumulated observations, plus formatted reflections on retries. It proposes text; the benchmark parser obtains an action; `env.step` executes Search, Lookup or Finish. Provider and Wikipedia calls return responses rather than taking ownership of the task. There is no independently scheduled worker delegation in this inspected workflow ([RT-RTE-training-loop](runtime.md#rt-rte-training-loop); SRC-1: `train.py`, `agent/expel.py`, `agent/react.py`, `envs/hotpotqa/hotpotqa.py`).

**3. Adapter verdict to retry controller.** Finish stores the proposed answer and terminates the attempt whether correct or incorrect. HotpotQA's success oracle compares that answer with the supplied key using normalized exact match. It judges the answer, not the reasoning or reflection. An incorrect finished attempt is therefore a concrete supported rejection path, not a hypothetical reviewer veto (SRC-1: `envs/hotpotqa/hotpotqa.py`, `utils.py`).

> if self.success_fn():
>     observation = 'Answer is CORRECT'
> else:
>     observation = f'Answer is INCORRECT'
> self.terminated = True
> --- `envs/hotpotqa/hotpotqa.py`

> return normalize_answer(answer) == normalize_answer(key)
> --- `utils.py`

**4. Failed trial to reflection and another attempt.** The existing training-route record retains the failure-sensitive reflection dispatch passage. If the attempt fails and reflection depth remains, `next_task` keeps the same task, marks reflection due and increments the counter. The next training call asks the model for a reflection before restarting ReAct. Reflection receives the previous trial, task and reflection-specific instructions/examples, rather than an unrestricted copy of all agent state. Long trial lines can be reduced to a label plus ellipsis to fit the reflection scratchpad target. Returned reflection text is retained and formatted into the retry's acting prompt. The model proposes a new plan; code decides whether another trial is allowed. There is no independent acceptance test of the reflection itself ([RT-RTE-training-loop](runtime.md#rt-rte-training-loop); SRC-1: `agent/reflect.py`, `agent/react.py`).

Success or exhausted reflection depth sets the task-advance flag. Exhaustion delivers a failed or halted result rather than guaranteeing eventual correctness. The configured reflection depth is three. Acting context resets between attempts; selected reflection text crosses the reset, while retained trajectories remain available outside the acting window. This is a per-attempt frame with selected text escaping, not live references that the model can dereference (SRC-1: `agent/reflect.py`, `configs/agent/expel.yaml`; [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)).

### Retention, recovery and delivery

Before resetting or advancing, `ExpelAgent.next_task` constructs a trajectory from the current task/history/reflections. It admits successes or failures into separate dictionaries according to the outcome and task-advance flag; failed retries are retained too. These outcome-classified experiences feed later extraction and retrieval. Software performs this admission without per-trajectory human approval; the outcome oracle does not validate every statement in a trajectory (SRC-1: `agent/expel.py`; [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)).

The driver updates statistics, appends ordinary and full logs, invokes `next_task`, snapshots selected simple-valued attributes and writes files after each attempt. Delivery is not an answer object returned from `run`: it is accumulated logs and checkpoint state, followed by printed/serialized batch summaries once the task list is exhausted. The default output location is `logs/hotpotqa/expel`, keyed by run name (SRC-1: `train.py`, `README.md`; [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore)).

> with open(f'{path}/{run_name}.pkl', 'wb') as f:
>     pickle.dump(dicts, f)
> --- `utils.py`

With `resume=true`, the driver instead reloads saved logs and the last dictionary and restores agent fields. This supports continuing a saved workflow; it does not establish exact replay or crash consistency. Separate text/pickle writes can fail between files, and no recovery trace is supplied. Acting can fall back to a long-context model after an invalid-request error, with an interactive acknowledgment; reflection has its own fallback. HotpotQA Search retries exceptions indefinitely, so step and reflection limits are not a wall-clock delivery guarantee ([RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore); SRC-1: `train.py`, `utils.py`, `agent/react.py`, `agent/reflect.py`, `envs/hotpotqa/hotpotqa.py`).

The implemented workflow can therefore produce classified training experience after either success or bounded unsuccessful trials. Static wiring establishes neither successful file delivery in a real run nor that reflection improves the next answer.

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

#### On [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)

Workflow selection: README HotpotQA experience gathering with testing disabled. The consequential acceptance point is the adapter's answer verdict; trial recovery is controlled by the reflection-depth/task-advance state. Delivery is outcome-classified experience and logs, including unsuccessful experience, rather than a guaranteed correct answer. The foreground driver retains scheduling responsibility throughout. No delegated worker has a separate delivery obligation.

#### On [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore)

Workflow delivery boundary: the training driver saves after logging an attempt and calling `next_task`. The snapshot therefore includes progression state intended for later continuation as well as retained experience. Batch completion adds summaries and another save. Resume is a caller-selected continuation path, not an automatic rollback after semantic failure.
