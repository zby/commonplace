---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Voyager learning workflow from curriculum task through action execution, critic rejection or acceptance, retained skill delivery and caller return."
run-id: AAS-2026-10-14-voyager-f16a44a0cfe3-01
reviewed-boundary: "55e45a880755d0c8c66ca7fb5fe7962ac8974f89"
---

# Voyager workflow report

## Workflow account

### Selected workflow and evidence

This account selects one task episode inside `Voyager.learn()`, followed by delivery of its accepted program to the skill library and continuation to another task. This is representative because it connects the shipped exploration entry point, program generation, game execution, task judgment and later reuse in one driver-controlled sequence. The first automatic task, “Mine 1 wood log,” provides a concrete request without inventing a successful execution. The enclosing workflow is [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop), with task selection through [RT-RTE-task-selection](runtime.md#rt-rte-task-selection). Evidence: SRC-1, `voyager/voyager.py`, `voyager/agents/curriculum.py`; the supplied task-selection record retains the initial-task passage.

The evidence establishes implementation, not an observed task episode. No target execution, model calls or experimental results were supplied or produced. This member inspected the complete `voyager/voyager.py`, `voyager/agents/critic.py` and `voyager/agents/skill.py` at SRC-1's frozen commit; these checks revisit the runtime baseline rather than add a source or evidence layer. Curriculum selection and action parsing details below use the supplied runtime records. External game, model and dependency behavior remains bounded as stated in [boundary](boundary.md#boundary-and-evidence).

### Request, assignment and handoffs

The caller starts learning and controls connection, checkpoint, model, mode and retry configuration. Python resets the environment, preserving inventory on resume, and obtains an initial observation. It supplies the latest events and rendered chest state to curriculum selection. The selected task and context become the rollout inputs; the initial automatic task is code-selected, not a curriculum-model proposal. Later curriculum dispatch may involve a model or human, with inventory-pressure overrides preceding that dispatch. This is sequential coordination among role-specific calls, not a parent spawning autonomous workers. Evidence: SRC-1, `voyager/voyager.py`; [RT-RTE-task-selection](runtime.md#rt-rte-task-selection).

At rollout reset, Python clears task-local counters and diagnostic conversations, optionally soft-resets the bot, issues time/difficulty commands, and retrieves skills using the task context. It gives the action model a system message containing instructions, primitive context and retrieved code, plus a human message containing observations, task and context. The action role proposes code; the driver retains ownership of the next step. There is no model-owned scheduler or worker-to-worker conversation in this selected sequence. Evidence: SRC-1, `voyager/voyager.py`; [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance).

The parser turns an accepted response into function declarations and a call to the selected async main function. That output-shape check is not a semantic proof of task correctness or compliance with the prompt. Python sends these strings to the environment together with all loaded skills and primitives, not only the retrieved prompt subset. Node evaluates the combined program and returns observation events. The executor thus receives executable code while the action model receives a selected textual context. Node's game assistance also limits any interpretation of final state as the generated function's unaided achievement. Evidence: SRC-1, `voyager/voyager.py`; [RT-OBJ-program-code](runtime.md#rt-obj-program-code), [RT-RTE-environment-step](runtime.md#rt-rte-environment-step), [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution). Those records and the runtime account retain parser, executor and program-supply passages.

### Verification and rejection

After execution, Python records events and updates chest memory, then requests a critic judgment with task, context and rendered chest information. Automatic verification uses selected final-state observations, not the program or an independent expected-result artifact. It accepts a parsed success boolean and critique; it can reject execution errors before a model call, and malformed critic output is retried up to the supplied critic limit. Model judgment is the decision mechanism, not an independently established answer oracle. Evidence: SRC-1, `voyager/agents/critic.py`; [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment).

Consider an executed program whose returned events contain `onError`. The critic renderer returns `None`; automatic judgment then returns false and empty critique. This is a statically supported rejection path, not an observed incident. It does not imply a universal error veto: manual mode instead obtains human confirmation, as the supplied judgment record shows. The driver then handles a false judgment through its ordinary retry policy. Evidence: SRC-1, `voyager/agents/critic.py`, `voyager/voyager.py`.

After an executed attempt, Python refreshes skill retrieval using context and extracted chat requirements. It replaces the action messages with a new system message and a human message containing observations, last program and critique. Earlier turns remain in diagnostic `conversations`, not in an accumulating action transcript. Thus rejection guidance crosses back into the next action invocation, but the critic does not directly edit code or order execution. Evidence: SRC-1, `voyager/voyager.py`; [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance).

A completed step ends the rollout on success or after the configured action-attempt limit:

> done = (
>     self.action_agent_rollout_num_iter >= self.action_agent_task_max_retries
>     or success
> )
> --- `voyager/voyager.py`

This is a completed-step bound, not a wall-clock or universal termination guarantee. Parse rejection keeps the prior messages and tries to record an empty event list. The runtime's first-record countercase shows why that path is not unconditionally graceful. Optional failed-placement recovery restores selected placement-related state; it is not atomic world rollback. Evidence: SRC-1, `voyager/voyager.py`, `voyager/utils/record_utils.py`; [runtime recovery account](runtime.md#guarantees-and-recovery-envelope).

### Recovery ownership and continuation

If rollout raises, `learn()` catches the exception, waits three seconds, constructs failure information, and resets using inventory, equipment and position from `last_events`. The owner of recovery is Python, not the action or critic model. This resumes from remembered bot status rather than proving restoration of every world effect. The recovery reset can itself fail; curriculum proposal and skill admission are outside this rollout exception handler. Evidence: SRC-1, `voyager/voyager.py`.

> except Exception as e:
>     time.sleep(3)  # wait for mineflayer to exit
>     info = {
>         "task": task,
>         "success": False,
>     }
> --- `voyager/voyager.py`

Whether a rollout succeeds, exhausts its action attempts or is converted to failure by this handler, the normal continuation updates curriculum progress from `info` and requests another task. A failed task therefore ends that episode, not necessarily the enclosing learning run. The recorder iteration check limits the enclosing loop between episodes; it does not cancel a hanging action or guarantee that recovery returns. Evidence: SRC-1, `voyager/voyager.py`; [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop).

### What counts as delivery

Success returns the final parsed program name and code in rollout `info`. In learning, this success gates `add_new_skill`; the manager generates a description, adds its embedding/index entry, updates the active code/description map, writes code and description files and `skills.json`, and persists the vector store. Deposit-task programs are deliberately skipped. There is no additional per-program human approval or regression test in this path. Evidence: SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`; [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), which retains the admission gate and active-map passages.

Task acceptance, durable skill publication and later execution are distinct delivery boundaries. For a nonskipped program, completed manager writes make the retained capability available for later retrieval and execution supply. Same-name replacement updates the active entry while keeping version-suffixed text files; interruption of the multi-write sequence is not covered by a transaction or automatic rollback. Future prompt selection and executable supply are wired, but successful invocation and benefit are unobserved. Evidence: SRC-1, `voyager/agents/skill.py`; [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution).

The enclosing caller receives a mapping only when the learning loop reaches its iteration-limit exit:

> return {
>     "completed_tasks": self.curriculum_agent.completed_tasks,
>     "failed_tasks": self.curriculum_agent.failed_tasks,
>     "skills": self.skill_manager.skills,
> }
> --- `voyager/voyager.py`

That return reports accumulated accepted/failed tasks and active skills, not an independently verified accomplishment report. The inference alternate shares action and critic machinery but does not admit new skills and has different continuation/recovery limits; the learning delivery account must not be generalized to it. Evidence: SRC-1, `voyager/voyager.py`; [RT-RTE-task-inference](runtime.md#rt-rte-task-inference).

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

#### On [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop)

Workflow selection: a curriculum task episode is the representative unit; it sits inside exploration rather than constituting an independent worker job. Coordination responsibility remains with the Python driver across task assignment, rollout completion, recovery, admission and next-task selection. Delivery has two horizons: per-task capability publication and the enclosing run's eventual result mapping.

#### On [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment)

Workflow rejection consequence: false success keeps the current task eligible for another action attempt until its limit. Critique crosses the handoff as rendered guidance, not a patch or execution command. A completed false judgment differs from an exception, which transfers recovery to the enclosing learning handler.

#### On [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Workflow delivery consequence: critic acceptance does not itself complete durable publication. The manager's description generation and persistence follow acceptance, outside the rollout exception handler. A deposit task can be accepted and recorded without producing a retained skill. Availability to later consumers is not evidence of exercised reuse.
