---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SkillRL workflow: ALFWorld training, validation-triggered skill admission, later prompt delivery and separately persisted policy and bank outputs."
run-id: AAS-2026-10-14-skillrl-0dba0e1c895e-01
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
---

# SkillRL workflow report

## Workflow account

### Selected workflow and evidence

This account follows the shipped ALFWorld skills driver through environment rollouts, policy fitting, validation-driven skill generation, bank admission, later consumption and persistence. It is representative because the driver enables dynamic updates and exercises both behavior-changing products: actor parameters and textual skills. It is not a generic assistant task or a collaboration among autonomous specialist agents. The operator requests a configured training run; software schedules work, the actor chooses environment actions, and a separate remote model proposes skills. The distributed environment workers are executors, not prompted collaborators. See [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) and [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission).

Evidence is SRC-1 at the [boundary](boundary.md)'s frozen commit. Direct implementation inspection for this account covers `examples/grpo_trainer/run_alfworld_skills.sh`, `verl/trainer/ppo/ray_trainer.py` validation, failure reconstruction, checkpoint and fitting sections, `agent_system/memory/skill_updater.py`, `agent_system/environments/env_manager.py` ALFWorld manager and `agent_system/memory/skills_only_memory.py` admission/save methods. Failure reconstruction and fitting order add detail to the supplied runtime coverage. These are source-level handoffs, not an observed successful run. No target code or model services were executed.

### 1. Operator request becomes scheduled work

The shell driver supplies the initial model path, ALFWorld environment, initial JSON bank, GRPO settings and resources. It requests 50-step episodes, six general retrieval slots, at most three new skills per update, a success threshold of 0.4, testing every five steps and checkpointing every ten. It disables validation before training. The trainer's validation admission guard defaults the unset `update_skills_from_train` flag to false, so this driver selects validation-driven rather than training-driven additions. Those values are configuration, not evidence of attained run length or available services. SRC-1, `examples/grpo_trainer/run_alfworld_skills.sh`, `verl/trainer/ppo/ray_trainer.py`; the admission guard and proposal route are recorded in [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission).

>     trainer.save_freq=10 \
>     trainer.test_freq=5 \
>     trainer.total_epochs=150 \
>     trainer.val_before_train=False $@
> --- `examples/grpo_trainer/run_alfworld_skills.sh`

`TaskRunner` constructs training and validation environments, workers, reward functions and the collector, then initializes workers and calls `fit`. Human control supplies the launch/configuration, not approval of each action, parameter update or skill. The configured actor and remote updater are distinct components: [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout) and [RT-CMP-skill-updater](runtime.md#rt-cmp-skill-updater). SRC-1, `verl/trainer/main_ppo.py`, `agent_system/memory/skill_updater.py`.

### 2. Collector delegates action choice, not workflow control

At reset the environment manager obtains tasks, clears episode history and caches retrieved skills. The initial prompt omits them; later positive-history prompts render the cached selections alongside recent actions and current observation. The collector sends rendered observation tokens to the actor, decodes its response and gives action text to the manager. The manager projects that text and submits it to simulator workers, then stores observation/action history and builds the next prompt. Neither simulator workers nor the policy receive authority to schedule bank updates or checkpointing. See [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout), with its retained rollout and prompt-branch passages; SRC-1, `agent_system/environments/env_manager.py`, `agent_system/multi_turn_rollout/rollout_loop.py`.

This handoff does not verify that the actor follows a skill. Projection can flag malformed action text without vetoing submission; the simulator owns effects and supplies outcome feedback. The collector stops at all-done or the step bound and returns active-step rows and episode statistics to the trainer. The rows are not each a complete conversation. These limits matter downstream when validation calls them failure examples. The outcome oracle is simulator success/reward, not a reference corrective action or an oracle for skill truth. See [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) and [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch); SRC-1, `agent_system/environments/env_package/alfworld/projection.py`, `agent_system/environments/env_package/alfworld/envs.py`.

### 3. Fitting precedes scheduled validation

The trainer computes rewards and advantages and delegates numerical fitting to worker groups. The actor update precedes the scheduled validation call. Validation then collects fresh rollouts in the separate validation manager and computes scores and task success rates. It is outcome measurement plus a possible source of training-bank changes, not an acceptance gate that rolls back the just-fitted actor. See [RT-RTE-policy-update](runtime.md#rt-rte-policy-update); SRC-1, `verl/trainer/ppo/ray_trainer.py`.

>                             actor_output = self.actor_rollout_wg.update_actor(batch)
> --- `verl/trainer/ppo/ray_trainer.py`

>                     if self.val_reward_fn is not None and self.config.trainer.test_freq > 0 and (is_last_step or self.global_steps % self.config.trainer.test_freq == 0):
>                         with _timer("testing", timing_raw):
>                             val_metrics: dict = self._validate()
> --- `verl/trainer/ppo/ray_trainer.py`

For skill generation, validation reduces outputs/scores to first occurrence of each trajectory UUID before pairing them with original dataset inputs. The helper filters score <= 0 and caps collection at ten. Parsing recognizes conversation markers or falls back to original input as context plus one output action. First-occurrence deduplication repairs row-count alignment; it does not reconstruct all environment steps. Consequently the updater may receive only a limited reconstruction, not the full failed episode. SRC-1, `verl/trainer/ppo/ray_trainer.py`; [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission).

>         # --- Fallback: treat full inp as initial context ---------------------
>         steps.append({'action': '', 'observation': inp[:3000]})
>         steps.append({'action': out[:2000], 'observation': ''})
>         return steps
> --- `verl/trainer/ppo/ray_trainer.py`

### 4. Low success delegates bounded proposal generation

If any task success rate is below 0.4, the trainer collects failures. Low-success labels trigger collection but do not restrict it to those task categories. It lazily constructs `SkillUpdater`, checks required retrieval memories and passes reconstructed failures plus the current training bank. The updater's request includes only the first five examples, last five parsed steps each, observation prefixes of 200 characters and existing skill titles. Existing principles are not supplied. This is a bounded proposal context, not inspection of the entire bank or complete run. SRC-1, `verl/trainer/ppo/ray_trainer.py`, `agent_system/memory/skill_updater.py`; [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission).

The remote model is asked for new concise skills avoiding those failures and existing titles. Software then extracts a JSON array, requires `skill_id`, `title` and `principle`, reassigns dynamic IDs based on current IDs and caps proposals. Although the prompt asks for `when_to_apply`, the parser does not require that key. These are formatting/identity checks, not tests of relevance, novelty of meaning or improved task performance. Human review does not intervene in this traced admission chain. SRC-1, `agent_system/memory/skill_updater.py`.

>                 return [
>                     s for s in skills
>                     if all(k in s for k in ['skill_id', 'title', 'principle'])
>                 ]
> --- `agent_system/memory/skill_updater.py`

### 5. Admission, later delivery and terminal outputs

For a nonempty proposal list the trainer appends to the training bank's general skills, not the validation bank, and saves a step-labelled JSON. `add_skills` skips IDs already present and invalidates the embedding cache after additions. This separation does not isolate training from validation evidence: validation failures have just determined training instructions. SRC-1, `verl/trainer/ppo/ray_trainer.py`, `agent_system/memory/skills_only_memory.py`; [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission).

At a later training reset, selection sees the changed bank. Under the driver's default template mode dynamic general skills are included before static ones and can exceed `top_k`. Delivery still waits for a positive-history noninitial prompt; cached episode selections are not refreshed by addition alone. General rendering supplies principles but omits `when_to_apply`. This establishes a wired later consumer, not compliance or benefit. See [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) and [RT-BAP-skill-conditioning](runtime.md#rt-bap-skill-conditioning); SRC-1, `agent_system/memory/skills_only_memory.py`, `agent_system/environments/env_manager.py`.

The terminal product is run artifacts and metrics, not a user-facing answer. `fit` validates/checkpoints on its last step when those frequencies are positive, logs metrics, prints final validation metrics and returns. Actor/optional critic and loader checkpoints are distinct from the separately saved bank. Bank file delivery means a JSON write; deployment to another run still requires configuring that path. No transaction linking checkpoint and bank saves, or successful end-to-end execution, is established. SRC-1, `verl/trainer/ppo/ray_trainer.py`; [RT-RTE-policy-update](runtime.md#rt-rte-policy-update).

### Rejection and recovery are narrower than verification

The checked rejection path preserves the existing bank when there are no success metrics, no below-threshold rate, no collected failures, missing memories, or no valid parsed proposals. A provider/parsing exception inside `analyze_failures` returns an empty list; the trainer reports no new skills and proceeds without that addition. Missing credentials instead raise during lazy constructor initialization, outside that catch and before the retrieval-memory guards. Thus provider-call failure recovery does not guarantee that dynamic-update setup cannot abort training. SRC-1, `verl/trainer/ppo/ray_trainer.py`, `agent_system/memory/skill_updater.py`; retained exception passage in [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission).

No comparative candidate rollout or automatic content-quality rollback occurs between returned proposals and this bank append/save. The trainer mutates memory before saving; the inspected save uses direct JSON writing, without a surrounding trainer recovery handler for save failure. These observations concern this call chain, not every possible external recovery measure. SRC-1, `verl/trainer/ppo/ray_trainer.py`, `agent_system/memory/skills_only_memory.py`.

>         with open(path, 'w') as f:
>             json.dump(self.skills, f, indent=2)
> --- `agent_system/memory/skills_only_memory.py`

Local checkpoint resume restores actor/optional critic, global step and available loader state, but `_load_checkpoint` does not restore dynamic bank JSON. The operator must separately select a matching bank to recover coupled instruction/policy state; no exercised procedure for doing so is supplied. HDFS loading explicitly raises. This is resumable numerical training with separate bank persistence, not demonstrated exact workflow recovery. SRC-1, `verl/trainer/ppo/ray_trainer.py`; [RT-RTE-policy-update](runtime.md#rt-rte-policy-update). Actual generated skill quality, successful later consumption and any improvement remain unobserved.

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

#### On [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission)

Workflow position: follows actor fitting at scheduled testing steps in the selected driver. Accepted proposals change the training bank before the next training rollout, not the validation bank used for this measurement. Verification boundary: success metrics trigger proposals; parser/ID checks admit them without a candidate performance veto. Delivery boundary: in-memory append and JSON persistence are separate from later reset-time selection and positive-history rendering. Recovery boundary: an empty updater result leaves the existing bank in use; constructor and save failures are not covered by the updater-call catch. Evidence and minimal passages are retained in the workflow account.

#### On [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Workflow delivery: configured final-step validation precedes final-step checkpointing and return. The saved actor/loader state and separately saved textual bank do not form an established coupled recovery artifact. Resume alone therefore does not establish restoration of the instruction state that conditioned prior fitting. This is an implementation limit, not an observed failed recovery; evidence is retained in the workflow account.
