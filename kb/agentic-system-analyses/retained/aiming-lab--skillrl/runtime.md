---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SkillRL runtime baseline: skill-conditioned environment rollouts, policy fitting, failure-triggered bank admission and offline data production."
run-id: AAS-2026-10-14-skillrl-0dba0e1c895e-01
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
---

# SkillRL runtime report

## Runtime account

### Evidence and consequential work

The frozen [boundary](boundary.md) classifies SkillRL as a builder or improvement plane. Its operational unit is a training run, not an interactive assistant session. The shipped ALFWorld driver prepares size/modality data, starts `verl.trainer.main_ppo`, loads a policy and skill bank, and enables dynamic skill updates. The trainer repeatedly collects environment interaction, assigns rewards, fits the policy, validates, and persists checkpoints and separately named banks. The source implements two behavior-changing outputs: numerical policy parameters and textual instructions selected for later model calls. Neither implementation nor README benefit claims establish observed improvement. No target execution, provider call, supplied trace or causal experiment supports this report.

Evidence is SRC-1 throughout, at the boundary revision. Added implementation coverage includes `agent_system/environments/env_package/alfworld/projection.py`, `agent_system/environments/env_package/alfworld/envs.py`, `agent_system/memory/memory.py`, `agent_system/reward_manager/episode.py`, `verl/workers/actor/dp_actor.py`, `verl/workers/fsdp_workers.py`, and scoped inspection of `verl/workers/sharding_manager/fsdp_vllm.py`. Offline additions include `examples/sft_data_generation/distillation/distill_alfworld.py` and searches of `examples/sft_data_generation/skill_memory/aggregate_skills.py` and `examples/sft_data_generation/skill_memory/generate_memory_alfworld.py`. These are executable-source evidence, not observed runs. Search/WebShop driver and generator searches establish alternate callers, not complete equivalence of their environments or offline transformations.

### Ordinary invocation and ownership

The run principal is the operator launching the shell driver. Configuration supplies model path, dataset paths, backend, environment, seeds, GPU resources and bank path. `TaskRunner` is a Ray actor; it creates separate training and validation environment managers, tokenization machinery, role workers, reward managers, data loaders and `TrajectoryCollector`, initializes workers, then calls `fit`. The default strategy is FSDP and default rollout mode is synchronous; the ALFWorld skills driver defaults its backend to vLLM. See SRC-1, `examples/grpo_trainer/run_alfworld_skills.sh`, `verl/trainer/main_ppo.py`, `verl/trainer/config/ppo_trainer.yaml`.

>         trainer.init_workers()
>         trainer.fit()
> --- `verl/trainer/main_ppo.py`

The code scheduler owns progression between training, validation and checkpointing. The policy model owns action choice inside each rollout; it does not choose when to fit, admit skills or stop the outer training run. Group UUIDs identify related rollout samples; independent trajectory UUIDs distinguish episodes, while global step indexes training and persistence. Environment workers hold individual simulator state and return observations, rewards, done flags and information through Ray futures. These are distributed executors, not independently prompted sub-agents. The collector batches model generation, decodes text, and calls the environment manager. Route [RT-RTE-environment-rollout](#rt-rte-environment-rollout) records that loop; [RT-RTE-policy-update](#rt-rte-policy-update) records its numerical successor production.

>             text_actions = self.tokenizer.batch_decode(batch.batch['responses'], skip_special_tokens=True)
>             
>             next_obs, rewards, dones, infos = envs.step(text_actions)
> --- `agent_system/multi_turn_rollout/rollout_loop.py`

At reset, ALFWorld loads the task from the observation and selects skills for each episode. Selection is cached until another reset. Importantly, reset-time retrieval does **not** mean first-call delivery: the initial observation uses the no-history template. Subsequent calls include selected skills only on the positive-history branch. `history_length <= 0` also chooses the no-history template. Each policy request is rebuilt as a single user message from the environment manager's current observation; it is not an ever-growing chat transcript. `SimpleMemory.fetch` includes only a recent suffix, default two steps, while the full episode buffer remains in process until reset. The collector separately tokenizes to a configured maximum; the shipped ALFWorld driver chooses truncation `error`, so oversize context can terminate processing rather than silently preserve skills. SRC-1, `agent_system/environments/env_manager.py`, `agent_system/memory/memory.py`, `agent_system/multi_turn_rollout/rollout_loop.py`.

>             if init or self.config.env.history_length <= 0:
>                 obs = ALFWORLD_TEMPLATE_NO_HIS.format(
>                     current_observation=text_obs[i],
>                     admissible_actions=reformatted_admissible_actions
>                 )
> --- `agent_system/environments/env_manager.py`

>             recent = self._data[env_idx][-history_length:]
> --- `agent_system/memory/memory.py:84-84`

This working-context mechanism filters old turns by code rule, not model summarization. Old records remain reachable to host code, but this inspected path has no foreground-model tool for requesting arbitrary older records. Skill content is selected from a separate store, copied into the request, and refreshed at reset; it is not a pointer whose lifetime the model manages. A per-environment buffer resembles an isolated task frame, but no child-model frame is spawned and no ownership/liveness inference follows from the analogy.

The ordinary loop stops at all-done or configured maximum steps (50 in the driver). It accumulates rewards and lengths only for active trajectories, then emits active step rows with episode statistics for fitting. Generation and environment stepping still receive the batch, including already-done members until the whole batch stops; active masks do not themselves prevent those calls. The terminal result is a training batch, metrics and ultimately saved run artifacts, not a user-facing answer. SRC-1, `agent_system/multi_turn_rollout/rollout_loop.py`, `verl/trainer/ppo/ray_trainer.py`.

### Forcing cases and qualified guarantees

Four selected forcing cases challenge an uncomplicated reading of the ordinary path:

1. **Malformed or non-admissible ALFWorld action.** Projection checks textual tags and some formatting, but its `action_pools` argument is unused. Missing action tags produce a last-30-character fallback that still reaches the environment. Invalidity becomes feedback/penalty; it is not an execution veto. The simulator, not the projection, determines game effects. This refutes a source-level guarantee that only listed admissible commands execute. SRC-1, `agent_system/environments/env_package/alfworld/projection.py`, `agent_system/environments/env_manager.py`.
2. **Too many dynamic skills or a different selector.** Template mode always includes every `dyn_` general skill, potentially exceeding `top_k`. Embedding mode instead ranks general and cross-category task skills and can omit dynamic entries. Both still feed the same prompt branch. Thus neither a strict six-skill cap nor universal delivery of newly admitted skills is justified. SRC-1, `agent_system/memory/skills_only_memory.py`.
3. **Validation-driven versus training-driven admission.** The driver enables updates without setting `update_skills_from_train`, whose lookup defaults false. Validation can therefore inform additions to the training bank. Writing only to training memory does not make validation causally isolated from training. The alternate true setting uses training batch failures and disables the validation update branch. See [RT-RTE-validation-admission](#rt-rte-validation-admission) and [RT-RTE-training-admission](#rt-rte-training-admission).
4. **Filtered retries and asynchronous generation.** With group filtering enabled, `dynamic_multi_turn_loop` repeats ordinary reset/rollout until enough effective samples or a maximum number of generation batches. It does not grant another action channel. Separately, main selects an async worker for async mode, but that worker's synchronous `generate_sequences` raises `NotImplementedError`; the inspected collector calls that method. This prevents treating the synchronous trace as proof of working async compatibility. SRC-1, `agent_system/multi_turn_rollout/rollout_loop.py`, `verl/trainer/main_ppo.py`, `verl/workers/fsdp_workers.py`.

>             if start_idx == -1 or end_idx == -1:
>                 # If we can't find a valid <action>...</action> block, mark as invalid
>                 actions[i] = actions[i][-30:]  # 0 is invalid action for Sokoban
>                 continue
> --- `agent_system/environments/env_package/alfworld/projection.py`

>         dynamic_skills = [s for s in all_general if s.get('skill_id', '').startswith('dyn_')]
>         static_skills = [s for s in all_general if not s.get('skill_id', '').startswith('dyn_')]
>         n_static = max(0, top_k - len(dynamic_skills))
>         general_skills = dynamic_skills + static_skills[:n_static]
> --- `agent_system/memory/skills_only_memory.py`

>         raise NotImplementedError("AsyncActorRolloutRefWorker does not support generate_sequences")
> --- `verl/workers/fsdp_workers.py`

The load-bearing controls have separate scope and strength:

| Control and owner | Enforcement point, coverage and external contract | Strength | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|
| Rollout bound; collector | Bounded `range(max_steps)` plus all-done break covers ordinary loop and each filtered retry. Backend calls must return; this is not a wall-clock timeout. | invariant | wired | uninspected |
| Action formatting; projection | Flags format errors on ALFWorld manager path but forwards actions. Direct simulator calls bypass projection. Requires simulator command semantics; no safety isolation contract established. | best effort | wired | uninspected |
| Dynamic ID reassignment; updater | Scans current general/task skill IDs and reassigns model outputs before returning them. Covers updater-mediated serial proposals, not arbitrary `add_skills` calls, concurrent writers or manual bank edits. | invariant | wired | uninspected |
| Validation bank separation; trainer | Validation update writes training bank only. Distinct managers are separately constructed, but validation evidence can still shape policy fitting through training skills. Requires no external mutation of validation files. | protocol | wired | uninspected |
| Numerical update guard; actor | FSDP actor optimizer skips non-finite gradient norms and clips gradients; does not compare policy quality or cover unaudited alternate optimizer implementations. | invariant | wired | uninspected |
| Recovery; trainer | Saves actor/optional critic and loader state and resumes local checkpoint paths. Updated skills are separately saved and not reloaded by this checkpoint function; exact coupled recovery is not guaranteed. HDFS load explicitly unsupported. | best effort | wired | uninspected |

SRC-1 anchors for the table: `agent_system/multi_turn_rollout/rollout_loop.py`, `agent_system/environments/env_package/alfworld/projection.py`, `agent_system/memory/skill_updater.py`, `agent_system/environments/env_manager.py`, `verl/workers/actor/dp_actor.py`, `verl/trainer/ppo/ray_trainer.py`.

>         # if grad_norm is not finite, skip the update
>         if not torch.isfinite(grad_norm):
>             print(f"WARN: rank {torch.distributed.get_rank()} grad_norm is not finite: {grad_norm}")
>             self.actor_optimizer.zero_grad()
>         else:
>             self.actor_optimizer.step()
> --- `verl/workers/actor/dp_actor.py`

>         if self.config.trainer.default_hdfs_dir is not None:
>             raise NotImplementedError("load from hdfs is not implemented yet")
> --- `verl/trainer/ppo/ray_trainer.py`

### Other material paths, authority and limits

Offline production is not the same route as online failure admission. `skill_generation/alfworld.py` reads supplied memories, categorizes success/failure, asks a remote model for general/task-specific skills and common mistakes, and overwrites a JSON bank. Its client contains empty credential/endpoint/version literals, so its source does not establish usable deployment configuration. The newer SFT-data shell pipeline parses supplied rollout dumps, deduplicates loops, generates memories, aggregates a bank, distills reasoning, then emits training pairs. Distillation supplies a recorded successful trajectory to the model and inserts generated reasoning around recorded actions; it is not an independent execution verifying those actions. [RT-RTE-offline-production](#rt-rte-offline-production) and [RT-RTE-sft-production](#rt-rte-sft-production) separate these admission mechanisms. External SFT fitting remains outside the frozen source.

The policy capability surface here is environment action text, not generic shell access. The ALFWorld driver currently grants a household simulator path; model/backend choice and other environment families are operator configuration. `make_envs` also dispatches Search, WebShop, card, Sokoban and AppWorld adapters; this inspection does not extend ALFWorld's command/effect conclusions to them. Search manager inspection confirms a different projection and search/information history channel. WebShop and Search skills drivers call the same main trainer, but their service isolation and full action semantics remain uninspected. SRC-1, `agent_system/environments/env_manager.py`, `examples/grpo_trainer/run_search_skills.sh`, `examples/grpo_trainer/run_webshop_skills.sh`.

Host Python, Ray actors, filesystem writes and model-service credentials execute with deployment authority. They are not a demonstrated sandbox. Configurable custom dataset classes are imported into the host; tokenizer loading exposes a `trust_remote_code` option defaulting false. These are operator-selected executable-code channels, not equivalent policy-model actions and not governed by ALFWorld projection. No inspected per-action human approval or per-skill human content approval mediates the ordinary paths. This is a bounded finding about the traced call chains, not an absence claim across all bundled infrastructure. SRC-1, `verl/trainer/main_ppo.py`.

Policy model, updater/producer services and optional embedding model are distinct numerical components below. The bank's detailed semantic revisions and theory assessments belong to the memory/epistemic specialists; this report establishes runtime admission, consumers and enforcement limits. It does not infer reliable compliance, learning, reflective theory construction or exercised self-improvement from storage, delivery or gradient updates alone.

## Shared records

### Components

#### RT-CMP-actor-rollout
Label: Actor rollout policy

Source-native identity: configured `actor_rollout_ref.model.path`, loaded into actor/rollout workers. Form: distributed-parametric weights, tensor storage in accelerator/host memory and checkpoints. Parameters change during training through optimizer steps; policy generation consumes the resulting parameters through rollout worker/sharding machinery. Exact initial version is not pinned by the shipped driver (`$MODEL_PATH`); resolution of that supplied path is deployment-dependent. This is not the Azure endpoint. Mutable path contents can supply a different initial model. SRC-1, `examples/grpo_trainer/run_alfworld_skills.sh`, `verl/trainer/main_ppo.py`, `verl/workers/fsdp_workers.py`, `verl/workers/actor/dp_actor.py`; scoped synchronization evidence in `verl/workers/sharding_manager/fsdp_vllm.py` includes `sync_model_weights`. No exact instantiated weights or successful synchronization run is supplied.

#### RT-CMP-skill-updater
Label: Remote skill updater model

Source-native identity: Azure deployment/model string `o3` in `SkillUpdater`; distributed-parametric service behind chat completions. Storage and provider internals are opaque. Client code performs inference, not parameter training. Exact weights/version are not pinned; the environment-selected endpoint and deployment name can resolve to changed service models. Separate offline generators also default to `o3`; SFT aggregation defaults to `gpt-4o` and per-trajectory memory generation has its own model option. These are independent service calls, not one shared policy instance. Those remote models likewise have no inspected fitting or immutable weight pin. SRC-1, `agent_system/memory/skill_updater.py`, `skill_generation/alfworld.py`, `skill_generation/search.py`, `skill_generation/webshop.py`, `examples/sft_data_generation/skill_memory/aggregate_skills.py`, `examples/sft_data_generation/skill_memory/generate_memory_alfworld.py`, `examples/sft_data_generation/distillation/distill_alfworld.py`.

>         self.model = "o3"
> --- `agent_system/memory/skill_updater.py`

#### RT-CMP-embedding-model
Label: Optional SentenceTransformer selector

Source-native identity: `embedding_model_path`, default `Qwen/Qwen3-Embedding-0.6B`. Form: distributed-parametric encoder weights plus derived dense vectors; storage: loaded model and NumPy cache in process. Inspected route encodes but does not train parameters. Exact version is not pinned; a supplied path/HF identifier may resolve to different model contents. No remote inference endpoint is specified here; external model loading internals remain uninspected. The cache is invalidated on bank addition/removal. SRC-1, `agent_system/memory/skills_only_memory.py`.

>             self._embedding_model = SentenceTransformer(self.embedding_model_path)
> --- `agent_system/memory/skills_only_memory.py`

### Operative objects

#### RT-OBJ-trajectory-batch
Label: Collected rollout batch

Source-native identity: `DataProto` emitted by `TrajectoryCollector`; symbolic tensor/array structure in process and Ray transport, with natural-language prompts/responses encoded as tokens, identifiers, masks, rewards and episode statistics. Source: SRC-1, `agent_system/multi_turn_rollout/rollout_loop.py`. It is current-run training state, not itself a durable bank. Active step entries carry the episode reward; this matters when interpreting failure rows as if each were a whole trajectory. Optional rollout dumps and checkpoints persist different projections of this state, SRC-1, `verl/trainer/ppo/ray_trainer.py`.

### Routes

#### RT-RTE-environment-rollout
Label: Skill-conditioned environment rollout

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Environment observations, rewards, done flags and infos on each step; final active-step DataProto batch and episode statistics to the trainer.
- Later read-back: Skills added during earlier training can be selected at a subsequent reset and delivered on later positive-history calls; unchanged shipped skills and ordinary current-episode history are distinct from that accumulated bank state.
- Delegated visibility: Policy workers receive rendered observation tokens; Ray simulator actors receive projected actions, not the entire skill bank or policy prompt.
- Selection predicate: Template category detection plus dynamic-first general selection, or optional embedding ranking; reset caches selections. Positive history and noninitial observation gate skill rendering. Training groups repeat input rows; optional filtering retries invoke the same loop.
- Invalidation or expiry: Episode buffers and cached episode selections reset per episode; no mid-episode automatic reselection is shown. Token maximum can truncate or error according to config.
- Activation or effect: Decoded policy output is projected and submitted to the simulator; model compliance with skills and behavioral change due to skills remain unobserved.
- Evidence limits: ALFWorld step/projection/executor traced; other dispatched environments, backend internals and actual generation success are not fully established.

Endpoints/progression: operator-configured trainer → manager reset/retrieval → collector chat rendering → policy workers → projection → Ray environment → next observation; code owns iteration/termination, policy owns the next action. Context is rebuilt current observation plus selected history and skills. Environment state and per-environment memory are separate from trajectory/group IDs. Return and recovery are described in the account; model/backend exceptions have no inspected collector-level retry policy. Mode: bounded benchmark episodes. Answer oracle: ALFWorld `won` supplied by simulator, translated to `10.0 * won` in text mode; manager separately collects task success rates. This is outcome feedback, not an expected action oracle or proof that a skill is correct. SRC-1, `agent_system/multi_turn_rollout/rollout_loop.py`, `agent_system/environments/env_manager.py`, `agent_system/environments/env_package/alfworld/envs.py`, `agent_system/memory/skills_only_memory.py`.

>         reward = 10.0 * float(info['won'])
> --- `agent_system/environments/env_package/alfworld/envs.py:52-52`

#### RT-RTE-validation-admission
Label: Validation-triggered skill admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Validation metrics plus side effects on the training skill bank, and a saved `updated_skills_step{global_steps}.json` when new skills are returned.
- Later read-back: Training manager's next reset selects from its changed in-memory bank; cross-run use requires configuring a saved bank path, not checkpoint resume alone.
- Delegated visibility: Azure updater sees at most five selected failure examples, each last five parsed steps with observation prefixes limited to 200 characters, plus existing titles, not the full bank principles.
- Selection predicate: Dynamic update enabled and training-source flag false; any success-rate metric below threshold triggers collection of score <= 0 examples. Collection caps ten; updater prompt uses first five. Low-performing task labels do not themselves restrict the failure list to those categories.
- Invalidation or expiry: Added skills invalidate embedding cache; episode selections refresh only at reset. No automatic expiry or post-admission quality rejection appears in this path.
- Activation or effect: Model proposals with required keys are reassigned IDs, capped and appended to general skills; later selection/rendering is wired, changed model behavior is unobserved.
- Evidence limits: Validation stores original dataset inputs but obtains outputs from environment rollouts; first-output-per-trajectory deduplication aligns counts, not necessarily a complete environment conversation. Failure reconstruction is therefore not established as a full trajectory transcript.

Trigger/owner: validation scheduling belongs to `fit`; metrics and guards decide whether to request proposals. Model proposes textual instructions; code admits them after JSON/key parsing, ID reassignment and existing-ID checks. No human content approval is requested. The updater guidance says to generate NEW skills avoiding existing titles and failures. It persists new instructions, not a verified causal diagnosis. Model judgment supplies no answer oracle; the episode reward and simulator success metrics are the outcome feedback in bounded benchmark mode. Existing bank principles are not supplied to this proposal model, so title hints do not establish content-directed criticism of them. Rejection abilities: missing metrics, sufficient success, empty failure collection, missing memory, empty/invalid parsed response or existing IDs. API/parse exceptions inside `analyze_failures` return empty; missing credentials during constructor initialization can raise outside that catch. No automatic bank rollback or comparative candidate test is shown; separate bank files and manual reconfiguration afford recovery, not an exercised rollback protocol. SRC-1, `verl/trainer/ppo/ray_trainer.py`, `agent_system/memory/skill_updater.py`, `agent_system/memory/skills_only_memory.py`.

>             current_skills=self.envs.retrieval_memory.skills,
> --- `verl/trainer/ppo/ray_trainer.py`

>             self.envs.retrieval_memory.add_skills(new_skills, category='general')
> --- `verl/trainer/ppo/ray_trainer.py`

>         for inp, out, score in zip(inputs, outputs, scores):
>             if score <= 0:
> --- `verl/trainer/ppo/ray_trainer.py`

>         except Exception as e:
>             print(f"[SkillUpdater] Error calling o3: {e}")
>             return []
> --- `agent_system/memory/skill_updater.py`

#### RT-RTE-training-admission
Label: Training-triggered skill admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Side effects on training retrieval memory and step-labelled JSON, with console reporting; no replacement policy is returned.
- Later read-back: Same next-reset training consumer as validation-driven admission; this branch disables the validation update trigger.
- Delegated visibility: Updater sees the same bounded formatted failures and title list, now reconstructed from decoded training batch prompts/responses and summed token-level scores.
- Selection predicate: Dynamic update and `update_skills_from_train` true, positive global step divisible by configured skill frequency, and some averaged success metric below threshold. Score <= 0 filters failed rows; no trajectory-ID deduplication appears in this training branch.
- Invalidation or expiry: Bank addition clears embedding cache; existing episode selections are unchanged until reset. No content expiry is implemented here.
- Activation or effect: New general instructions become eligible for future prompts; training rows are not independently demonstrated complete failure episodes or successful fixes.
- Evidence limits: This is an alternate source of updater inputs, not an observed leakage-free experiment or demonstrated skill benefit. Negative rewards can include configured invalid-action penalties rather than only simulator failure.

Owner, proposal guidance, computational admission, vetoes and error limits follow the same updater/parser/add path as [RT-RTE-validation-admission](#rt-rte-validation-admission), but the source selection and scheduling checks above differ. Human contributes launch/configuration, not per-content approval. Mode is bounded training episodes; outcome feedback is reward/success, not a reference corrective action. Code fits the actor after this update branch; saved skill state remains separate from model checkpoints. No automatic rollback or post-admission comparative test is shown. SRC-1, `verl/trainer/ppo/ray_trainer.py`, `agent_system/memory/skill_updater.py`.

>                     if (self.config.env.get('skills_only_memory', {}).get('enable_dynamic_update', False)
>                             and self.config.env.get('skills_only_memory', {}).get('update_skills_from_train', False)):
> --- `verl/trainer/ppo/ray_trainer.py`

#### RT-RTE-policy-update
Label: Reward-driven policy update

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Actor update metrics; changed actor parameters, optional critic updates, and periodically checkpoint artifacts.
- Later read-back: Subsequent generation enters rollout sharding machinery with actor parameters; checkpoints support later local training resume. Saved skills are not automatically restored by the inspected resume function.
- Delegated visibility: Training workers receive batched prompts/responses, old/reference log probabilities as configured, rewards and advantages; not a human-authored textual diagnosis of each update.
- Selection predicate: Training batch available and actor warmup condition met; algorithm configuration chooses advantage computation. The ALFWorld skills driver requests GRPO with actor KL loss.
- Invalidation or expiry: Each fitting step changes live weights; checkpoint retention is configurable. Non-finite gradient norms cause skipped optimizer steps on the inspected FSDP actor path.
- Activation or effect: Optimizer can change the deployed-in-run policy parameters; no evidence here establishes better later actions or successful weight synchronization in an actual run.
- Evidence limits: FSDP source path traced; Megatron, SGLang and alternate algorithms are not audited for equivalent guarantees. Numerical optimization is not a textual theory revision.

Admission: code computes rewards/advantages and applies optimizer changes; it does not choose among policies by a held-out quality veto. Human supplies model/config and can stop/restart a run, not approve each update. Oracle/operating mode: bounded task episodes with simulator feedback; `EpisodeRewardManager` normally copies episode reward to the final valid response token, but returns supplied `rm_scores` directly when present. This alternate return prevents attributing all possible reward paths to simulator outcomes. Update objective is reward-oriented configured loss with regularization; guidance is symbolic algorithm code/config, result persists as distributed weights. Recovery is local checkpoint resume, not automatic quality rollback. SRC-1, `agent_system/reward_manager/episode.py`, `verl/trainer/ppo/ray_trainer.py`, `verl/workers/fsdp_workers.py`, `verl/workers/actor/dp_actor.py`, `verl/workers/sharding_manager/fsdp_vllm.py`.

>                 score = episode_rewards
>             reward_tensor[i, valid_response_length - 1] = torch.tensor(score, dtype=torch.float32, device=prompt_ids.device)
> --- `agent_system/reward_manager/episode.py`

#### RT-RTE-offline-production
Label: Offline skill bank production

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ALFWorld script overwrites the configured bank JSON and prints generated counts/examples.
- Later read-back: A later configured `SkillsOnlyMemory` loads that JSON; generating it does not automatically change a live trainer instance.
- Delegated visibility: Generator sends bounded extracted goal/action/reasoning/planning/mistake patterns from supplied memories, not all raw interactions.
- Selection predicate: Goal-keyword categorization and stored outcome labels; limited category samples feed general, task-specific and common-mistake calls.
- Invalidation or expiry: File overwrite replaces previous output. No versioned rollback or automatic subsequent verification is shown in this script.
- Activation or effect: New bank content can condition later training prompts once configured and selected; actual generation and consumption are unobserved.
- Evidence limits: Empty literal Azure configuration prevents assuming usable credentials. Supplied memory provenance and equivalent detailed transformations in Search/WebShop generators remain unestablished.

Operator starts a fixed batch job. Model proposes skill text; software parses JSON and writes results, without per-skill human approval or a held-out outcome veto. Prompt guidance requests concise transferable failure-aware rules. Outcome labels are supplied data, not an independently verified answer oracle; model judgment is not an oracle. Rejection is JSON parsing/fallback; generation call failure is not shown as a robust resumed batch protocol. Existing file preservation requires external backup. SRC-1, `skill_generation/alfworld.py`; alternate generator presence and `o3` calls: `skill_generation/search.py`, `skill_generation/webshop.py`.

>     with open(output_path, 'w') as f:
>         json.dump(output, f, indent=2)
> --- `skill_generation/alfworld.py`

#### RT-RTE-sft-production
Label: Offline SFT pair production

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Shell pipeline emits intermediate trajectory/memory/bank/distillation JSON and final `alfworld_sft_data.json` training pairs.
- Later read-back: Distillation loads the generated bank in this pipeline; final pairs are for an external SFT trainer, whose fitting behavior is not frozen.
- Delegated visibility: Distillation model receives task, rendered selected skill block and recorded step summaries; recorded actions are preserved while generated reasoning is inserted.
- Selection predicate: Operator provides rollout directory; scripts parse/dedupe and choose category skills; distillation constructs conversations from successful recorded steps including synthetic terminal `done`.
- Invalidation or expiry: Intermediate and final files are regenerated at specified work paths. No automatic outcome-based rollback is shown.
- Activation or effect: Produces behavior-shaping training material, not a demonstrated new policy; final impact depends on external fitting and later operation.
- Evidence limits: Driver and distillation transformation inspected; exact semantics of all parsing, memory generation, aggregation and flattening stages are not fully audited. This route does not authenticate original rollouts or validate invented reasoning.

Mode is batch data production. Human chooses rollout inputs and model names; remote models propose memories/skills/reasoning and code persists or assembles outputs. Admission here is data construction, not deployment approval. Recorded successful actions supply a reference action sequence for reasoning generation, not an independent new-environment outcome test. The distillation guidance requests reasoning for supplied actions; rejection/recovery includes parser failures and shell fail-fast (`set -euo pipefail`), not semantic verification or rollback. SRC-1, `examples/sft_data_generation/run_alfworld.sh`, `examples/sft_data_generation/distillation/distill_alfworld.py`.

>             think = reason_by_idx.get(idx, "")
>             c["value"] = f"<think>{think}</think>\n{c['value']}"
> --- `examples/sft_data_generation/distillation/distill_alfworld.py`

### Claims

#### RT-CLM-reusable-patterns
Label: Reusable behavior pattern claim

SkillRL declares that it abstracts experience into reusable hierarchical skills. That is a declared purpose, not a measured runtime conclusion here. SRC-1, `README.md`, as retained in [boundary](boundary.md). The routes above establish software capable of producing and later supplying rules; they do not establish reliable transfer, improved capacity or causal gains.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-conditioning
Label: Skill text conditions policy

Consumer: actor policy model. Channel: rendered titles/principles, task-specific applicability text and common-mistake instructions copied into the environment observation's user message. Force: model-interpreted guidance, not an executor invariant or hard action permission. Horizon: later calls of a reset episode; dynamically accumulated instructions can reach subsequent episodes and, if saved/reconfigured, later runs. General skill rendering omits `when_to_apply`, while task-specific rendering includes it; delivery is not complete preservation of all bank fields. SRC-1, `agent_system/memory/skills_only_memory.py`, `agent_system/environments/env_manager.py`, `agent_system/multi_turn_rollout/rollout_loop.py`. Connected route: [RT-RTE-environment-rollout](#rt-rte-environment-rollout).

#### RT-BAP-policy-parameters
Label: Trained parameters determine generation

Consumer: rollout inference model. Channel: numerical actor state through worker/sharding synchronization, with checkpoint persistence. Force: distributed-parametric generation policy; sampling and environment state also affect outcomes. Horizon: subsequent in-run rollouts and resumed checkpoints; exact successful synchronization and later causal dependence are unobserved. SRC-1, `verl/workers/fsdp_workers.py`, `verl/workers/sharding_manager/fsdp_vllm.py`, `verl/trainer/ppo/ray_trainer.py`. Connected route: [RT-RTE-policy-update](#rt-rte-policy-update).

## Annotations

none
