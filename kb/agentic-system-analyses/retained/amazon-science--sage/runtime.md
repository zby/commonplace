---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SAGE runtime baseline: paired AppWorld rollouts, skill execution, reward-fed policy updates, evaluation and expert-to-SFT admission."
run-id: AAS-2026-10-15-sage-d0de15ae5730-01
reviewed-boundary: "3c9244e82244abb1adc5467ee601a03ba0f433a0"
---

# SAGE runtime report

## Runtime account

### Boundary and work

SAGE's consequential work is training a task-solving model using sequential AppWorld tasks, generated Python functions and skill-integrated rewards. Its evaluation agent also accumulates functions while solving tasks. Expert rollouts supply a separate supervised-training path. This account uses SRC-1 at the boundary's frozen commit; all source findings below are implementation evidence unless explicitly marked doctrine/design. No target execution, supplied trace or causal experiment establishes activation, successful installation, quality or benefit.

The shipped training entry is the operator-edited `sage/run_sage_2nodes.sh`: a Ray job invokes `verl.trainer.main_ppo` with a local SFT-model path, scenario lists, eight agent samples, vLLM rollout and the `loop` advantage estimator. Its project-name setting selects an incompatible dataset reader, so supplying model/data/resource placeholders alone does not make this launcher reach paired training; the internal rollout and update mechanisms below are conditional capacities. The four-node launcher is another shipped configuration, not independently audited here. The evaluation entry documented in `README.md` is `appworld run sage_test_normal`; the shipped runner builds one configured agent and calls `solve_tasks`. Expert generation instead invokes `run_rollout.py`, and SFT invokes the Slurm/Accelerate launcher. See [RT-RTE-paired-rollout](#rt-rte-paired-rollout), [RT-RTE-policy-update](#rt-rte-policy-update), [RT-RTE-evaluation-loop](#rt-rte-evaluation-loop), [RT-RTE-expert-admission](#rt-rte-expert-admission) and [RT-RTE-sft-admission](#rt-rte-sft-admission). Sources: SRC-1, `README.md`, `sage/run_sage_2nodes.sh`, `patches/appworld/experiments/code/skill_library_agent/run.py`.

### Ordinary training invocation, end to end

The operator supplies model, data and Ray resources, but the shipped two-node configuration has an additional reachability defect. It sets `WAND_PROJECT='AppWorld_SAGE'` and passes that value as `trainer.project_name`. `RayPPOTrainer._create_dataloader` chooses the scenario-text `AppworldDataset` and `StatefulDataLoader` only for the exact value `AppWorld`; otherwise it constructs `RLHFDataset`, which calls `pd.read_parquet` on the input. The shipped `patches/appworld/train_scenario.txt` contains plain scenario IDs, not Parquet data. `main_ppo.py` resolves and passes the configuration into trainer construction without repairing this value. Dataloader construction occurs before `init_workers` and `fit`. Thus, even after model/resource setup, this configuration directs the shipped scenario list to an incompatible reader before scenario sampling. This is an implementation-level mismatch, not merely an unobserved-run caveat (SRC-1, `sage/run_sage_2nodes.sh`, `sage/verl/trainer/ppo/ray_trainer.py`, `sage/verl/utils/dataset/rl_dataset.py`, `sage/verl/trainer/main_ppo.py`, `patches/appworld/train_scenario.txt`).

> WAND_PROJECT='AppWorld_SAGE'
> --- `sage/run_sage_2nodes.sh`

> trainer.project_name=$WAND_PROJECT \
> --- `sage/run_sage_2nodes.sh`

> if self.config.trainer.project_name == 'AppWorld':
> --- `sage/verl/trainer/ppo/ray_trainer.py`

> self.train_dataset = RLHFDataset(parquet_files=self.config.data.train_files,
> --- `sage/verl/trainer/ppo/ray_trainer.py`

> dataframe = pd.read_parquet(parquet_file)
> --- `sage/verl/utils/dataset/rl_dataset.py`

The following end-to-end account describes the internal capacity conditional on selecting the AppWorld scenario loader, for example by correcting the project-name value to `AppWorld`, as well as satisfying the remaining model/data/resource prerequisites. That configuration correction is not a demonstrated successful run. Once reached, `RayPPOTrainer.fit` samples two of each scenario's three subtasks, assigns turn IDs and repeats them for separate agent IDs. The generation manager owns progression across two subtask iterations. Each task/agent UID has an AppWorld subprocess with command and response queues. These are execution workers, not independently prompted delegate agents. Their externally supplied task instruction, supervisor, API metadata and environment state bound the task; the generated Python is the action representation. The model chooses the next chunk from rendered prompt plus previous responses and observations. The manager extracts fenced Python, sends it for execution, appends the returned observation and updates active masks. Completion, prompt overflow, maximum turns and configured early stopping can terminate progression. The conditional rollout's terminal training output is tokenized trajectories plus shaped rewards, not merely a user-facing answer (SRC-1, `sage/verl/trainer/ppo/ray_trainer.py`, `sage/llm_agent/appworld_generation.py`, `sage/llm_agent/app_world/app_world_env.py`).

Function dictionaries start empty for each `run_llm_loop`. Non-failing first-subtask output permits AST-extracted functions and imports to enter the paired library. Before the second task's first model call, code executes the retained definitions in its fresh world and renders them into the prompt. The second task receives functions, not the first task's entire conversation or world. This resembles a per-task frame whose selected function output escapes to the next frame; it is not shared live Python-variable state. Name-substring counting supplies the reuse signal. AppWorld completion triggers evaluation; the pass fraction supplies the task reward, and success plus counted reuse modifies it. `RewardManager` puts the scalar on the last valid response token; driver-side advantage computation and worker-side actor update consume it. Checkpoints and the next training iterations provide the longer behavioral horizon. See the route records and [RT-CMP-actor-rollout](#rt-cmp-actor-rollout).

### Controls, guarantees and forcing cases

The capability surface is model-generated Python executed by AppWorld, including Python definitions and API calls, plus operator-controlled training, provider configuration and model loading. The task's allowed-app/API metadata is context, not evidence here of a SAGE-owned permission boundary. The current grant set consists of the AppWorld world and whatever its API/execution implementation permits. The deployed isolation envelope is uninspected: separate subprocesses establish coordination boundaries, not OS/network containment. Upstream AppWorld is outside the frozen source contents. No sandbox-security guarantee follows from the inspected wrappers.

Four forcing cases qualify load-bearing claims:

1. **The function prompt is not an execution gate.** It says no package imports and no calls to previous functions. Both training and evaluation still send extracted Python directly to `world.execute`, and extraction explicitly preserves imports. Even the prompt allows a single API call when appropriate. Thus modularity, self-containment and reuse are model guidance, not validated invariants. Owner: prompt author and model; enforcement point: model interpretation; guarantee strength: policy; implementation conclusion status: wired; operation conclusion status: uninspected. Covered path: prompted generation. Alternate paths: predefined definitions execute before generation; direct caller-supplied worlds and generated top-level code do not acquire structural validation from this prompt. Required external contract: AppWorld execution restrictions. Evidence: [RT-CLM-function-rules](#rt-clm-function-rules), [RT-RTE-skill-install](#rt-rte-skill-install).
2. **Execution success is weaker than skill correctness.** Training's admission gate searches output for absence of `Execution failed.`; it does not require full task success or test each extracted function against a reference. The later install gate also executes code before deciding whether to show it in the prompt. Removing prompt text after an unsuccessful install is not rollback of effects already attempted. Owner: batch environment / evaluation initializer; enforcement point: output-string checks; guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. Covered paths differ: training extraction, training install, evaluation install and expert verification use different checks. The expert path additionally requires benchmark success and fresh-world definition execution, so it must not be conflated with ordinary evaluation admission. Required external contract: accurate AppWorld output markers and evaluator results.
3. **Evaluation label gating is not current-task-success gating.** `solve_tasks` carries the previous task's success into `solve_task`; with `use_label`, extraction depends on that previous result. The shipped normal config instead enables skills without `use_label`, permitting unconditional extraction after task evaluation. Owner: base agent; enforcement point: post-task branch; guarantee strength: invariant only for the inspected branch's literal predicate, not for library quality; implementation conclusion status: wired; operation conclusion status: uninspected. Expert generation and RL admission follow other predicates. See [RT-RTE-evaluation-loop](#rt-rte-evaluation-loop).
4. **Context limits do not mean common history compaction.** RL truncates each observation, can deactivate an overlength rollout and slices rolling token input to a bounded suffix. Evaluation stores `max_prompt_length` but its inspected next-step method does not apply a corresponding history trim; it truncates the observation to 12,000 characters and appends a reminder. A provider adapter has a token-limit check, but it is not equivalent to the RL manager's control. Owner: each caller and adapter; enforcement points: observation processing / request generation; guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. No general full-context-preservation or automatic recovery guarantee is claimed. Sources: SRC-1, `sage/llm_agent/appworld_generation.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`, `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.

Reliability is similarly path-specific. RL retries queue-timeout initialization up to the coded retry bound, skips a batch on an escaping `queue.Empty`, and closes task processes after the rollout. Some execution-response reads have no timeout. Evaluation provider retries are configured, but a broad agent exception handler substitutes `apis.supervisor.complete_task()` rather than proving task completion. Task evaluation remains separate. Logs, LM calls, costs and trainer metrics expose attempted operation; none supplied here establish observed operation. Checkpoint resume restores actor and optional critic/dataloader state, not an interrupted AppWorld conversation or paired function dictionary (SRC-1, `sage/llm_agent/app_world/app_world_env.py`, `sage/llm_agent/appworld_generation.py`, `sage/verl/trainer/ppo/ray_trainer.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`).

Alternate model-call paths are training worker generation and evaluation's OpenAI-compatible or LiteLLM adapter. Provider-native tools can be passed by the adapter API, but the inspected task caller supplies messages only and extracts code, not tool-call dispatch. Retained definitions are a separate execution path before the first model action. Expert verification uses another fresh world. Shell launch and Ray/Slurm authority belong to the operator/production plane, not to an observed model-granted shell. Manual graph control and callback extension behavior were not established in the inspected paths; this is not a repository-wide absence claim.

Additional coverage beyond the boundary's initial reads includes the evaluation model adapter, rollout runner and subclass, SFT supervised processor, trainer reward manager, advantage dispatch, checkpoint save/resume and FSDP update wrapper. Correction inspection also traced project-name dispatch, `RLHFDataset` construction and its Parquet reader in `sage/verl/utils/dataset/rl_dataset.py`, resolved-config forwarding in `sage/verl/trainer/main_ppo.py`, and the scenario-ID input in `patches/appworld/train_scenario.txt`. These are SRC-1 implementation evidence. Remaining integration limits include upstream environment enforcement and SFT training machinery, uninspected alternate workers/backend details, actual model versions and artifacts, and the four-node launch configuration. The SFT launcher's shell completeness and full patched-install compatibility are not demonstrated by this source trace.

## Shared records

### Components

#### RT-CMP-actor-rollout
Label: Actor rollout model

Source-native identity: actor/rollout model supplied through `actor_rollout_ref.model.path`; representational form: distributed-parametric weights; substrate: local model files, worker memory and saved actor checkpoints. Parameters change during RL operation through `update_actor`; exact starting weights are not pinned by the source, because the launcher uses `PATH_TO_SFT_MODEL`. There is no remote endpoint in this inspected training path; a changed local path or checkpoint can select different weights. Later generation uses the worker's rollout/sharding integration; backend synchronization correctness remains untested. SRC-1, `sage/run_sage_2nodes.sh`, `sage/verl/workers/fsdp_workers.py`, `sage/verl/trainer/ppo/ray_trainer.py`.

> metrics = self.actor.update_policy(data=data)
> --- `sage/verl/workers/fsdp_workers.py`

#### RT-CMP-language-model
Label: Evaluation language model

Source-native identity: `LiteLLMGenerator`, configured as `sage` for normal evaluation. Representational form: distributed-parametric model behind an inference endpoint; substrate: external server/provider memory, not frozen weights. The inspected evaluation caller makes no parameter update. Exact model version is not pinned; the OpenAI adapter targets localhost port 2638 and the operator serves a chosen `MODEL_PATH`. A mutable endpoint can resolve the same name to different weights. Provider internals remain uninspected. Expert generation uses the same adapter mechanism with a separately configured model; README attribution to Claude is reported setup intent, not frozen response evidence. SRC-1, `README.md`, `patches/appworld/experiments/configs/sage_test_normal.jsonnet`, `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.

> "openai": lambda: OpenAI(api_key="anything", base_url="http://localhost:2638/v1").chat.completions.create,
> --- `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`

#### RT-CMP-retrieval-model
Label: Retrieval model alternatives

Source-native identities: `Qwen/Qwen3-Embedding-0.6B` for skill embeddings and `sentence-transformers/all-MiniLM-L6-v2` for query embeddings. Representational form: distributed-parametric encoders; substrate: downloaded model weights and CPU memory. Each alternative encodes text and ranks similarity; neither is trained by the inspected evaluation path. Neither exact revision is pinned. They are named local loads rather than mutable inference endpoints, but resolving the unpinned model names can change the acquired artifact. `trust_remote_code=True` delegates model-loading behavior to externally acquired code; the frozen source does not establish its isolation. These alternatives do not run in the shipped default scenario-ID retrieval configuration. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> self.retrieval_model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B", trust_remote_code=True, device=self.device)
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

> self.retrieval_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", trust_remote_code=True, device=self.device)
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

#### RT-CMP-sft-model
Label: Supervised model

Source-native identity: `Qwen/Qwen2.5-32B-Instruct` in the SFT YAML. Representational form: distributed-parametric weights; substrate: external starting artifact, training memory and model-output directory. Full fine-tuning requests parameter changes; the exact starting model revision is not pinned. There is no inference endpoint here, but unpinned model resolution and `trust_remote_code: true` leave artifact and loading code unresolved. SFT output is intended as the RL starting model; automatic selection of the SFT output into the placeholder RL path is not wired in these launchers. SRC-1, `patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml`, `sage/run_sage_2nodes.sh`.

> stage: sft
> do_train: true
> finetuning_type: full
> --- `patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml`

### Operative objects

#### RT-OBJ-skill-libraries
Label: Paired rollout skill libraries

Source-native identity: `skill_libraries`, a list of per-pair dictionaries keyed by function name. Representational form: symbolic Python source consumed by AST extraction and AppWorld execution. Substrate: generation-manager process memory, reinitialized for each rollout call. Imports and top-level function bodies are retained; duplicate names overwrite within a dictionary. Function docstrings also reach a model as interpreted guidance, but correctness of that interpretation is separate from code execution. Training does not establish a disk library or cross-batch dictionary recovery. SRC-1, `sage/llm_agent/appworld_generation.py`, `sage/llm_agent/app_world/app_world_env.py`.

> skill_libraries = [{} for _ in range(len(gen_batch["task_ids"])//2)]
> --- `sage/llm_agent/appworld_generation.py`

#### RT-OBJ-skill-library-functions
Label: Evaluation function records

Source-native identity: `skill_library_functions`, records containing task ID, name and function source. Representational form: symbolic JSON records carrying executable Python; substrate: agent list, append-only output JSONL and optional separately loaded predefined-library JSONL. Embedding arrays are distinct numerical selection material, not the executed function bodies. This record establishes the execution-facing object; detailed retention/curation analysis is left to the memory member. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> skill_jsonl = {"task_id":world.task_id, "name":names_list[i], "function":functions_list[i]}
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

### Routes

#### RT-RTE-paired-rollout
Label: Paired training rollout

Reachability: this is an internal training capacity conditional on selecting the AppWorld scenario loader. The shipped two-node launcher's `AppWorld_SAGE` project value instead selects the Parquet reader for plain scenario text, preventing the described launch-to-loop progression; see the ordinary-invocation account above.

Endpoints/progression: scenario batch → sampled subtask/agent IDs → generation manager → per-UID subprocess worlds → token trajectories and scalar rewards. Owner: trainer for sampling, manager for turns, model for next Python action, AppWorld for execution and task outcome. Context is rendered task/API/skill prompt and accumulated turns; state includes world, active masks, function dictionaries and token tensors. Operating mode: bounded two-task curriculum with sampled scenario subtasks, not open-ended self-directed problem selection. No human per-action veto is wired; the operator controls launch/configuration. Answer oracle: external AppWorld evaluator's pass fraction when the world reports completion. SRC-1, `sage/verl/trainer/ppo/ray_trainer.py`, `sage/llm_agent/appworld_generation.py`, `sage/llm_agent/app_world/app_world_env.py`.

- Immediate return: batched trajectories, masks and skill-integrated rewards to the trainer.
- Later read-back: first-task functions enter the second task through [RT-RTE-skill-install](#rt-rte-skill-install); actor changes have a separate update route.
- Delegated visibility: subprocess workers receive code; model samples have task-local contexts and agent IDs, not other samples' conversations.
- Selection predicate: sampled subtasks and active masks; completion, maximum turns, token budget and configured sparse-active early stopping control continuation.
- Invalidation or expiry: worlds close after each subtask iteration; libraries are recreated at the next rollout call.
- Activation or effect: code is wired to AppWorld execution; actual API effects and successful reuse are unobserved.
- Evidence limits: shipped two-node configuration does not select the required scenario loader; this wired internal route is not an end-to-end working-launch claim. Evaluator internals and benchmark adequacy are external; source supplies no observed trajectory.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for subtask_iter in range(2):
> --- `sage/llm_agent/appworld_generation.py`

> output = world.execute(code)
> task_completed = world.task_completed()
> --- `sage/llm_agent/app_world/app_world_env.py`

Reward shaping uses a positive substring-count indicator, not an execution trace of function invocation:

> if name in codes[world_index] and "def "+name not in codes[world_index]:
>     skill_counts[world_index] += 1
> --- `sage/llm_agent/app_world/app_world_env.py`

> reward1 = final_output["rewards"][0] + reward_skill_count * reward2_success_mask * reward1_success_mask.int()
> reward2 = final_output["rewards"][1] + reward_skill_count * reward2_success_mask.int()
> --- `sage/llm_agent/appworld_generation.py`

#### RT-RTE-skill-install
Label: Skill extraction and installation

Endpoints/progression: generated first-task Python → AST-extracted imports/functions → paired dictionary → execution in second-task world and prompt rendering. Owner: model proposes code; batch environment admits and later installs it. Trigger: first-subtask execution without the failure marker. Proposed change: add or replace named reusable Python definitions. Admission: string check plus parseability, not reference-outcome validation. Software can reject parse failures; no human content approval is wired. Guidance is the shipped skill-library prompt: generic parameters, self-contained multistep functions, type hints/docstrings, no imports or calls to other functions. What persists is extracted code, not a structured criticism or rationale ledger. Operating mode: paired curriculum; oracle: execution status for admission, not an expected answer. Recovery: later definitions overwrite names, fresh worlds end task state, and failed install can suppress prompt delivery; transactional undo is not established. SRC-1, `sage/llm_agent/app_world/app_world_env.py`, `patches/appworld/experiments/prompts/skill_library_agent.txt`.

- Immediate return: updated dictionaries to the generation manager; later initializer returns prompts.
- Later read-back: second-subtask initializer executes retained source and supplies it to the model.
- Delegated visibility: matching pair's library only; no demonstrated cross-agent sharing.
- Selection predicate: first subtask, output lacks failure marker, AST top-level FunctionDef; second subtask reads the matching dictionary's values.
- Invalidation or expiry: same-name replacement within the pair and whole-library reset per rollout call.
- Activation or effect: definitions are wired into the execution environment before prompting; model reliance and actual invocation are unobserved.
- Evidence limits: imports are copied by source line; no proof of semantic self-containment, effect safety or useful abstraction follows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if "Execution failed." not in output:
> --- `sage/llm_agent/app_world/app_world_env.py`

> skill_libraries[world_index][name] = func
> --- `sage/llm_agent/app_world/app_world_env.py`

> world_proxy.command_queue.put({"action": "execute", "code": retrieved_skills_prompt})
> response = world_proxy.response_queue.get()
> --- `sage/llm_agent/app_world/app_world_env.py`

#### RT-RTE-policy-update
Label: Reward-fed actor update

Reachability: this update capacity depends on reaching the paired rollout and producing training batches. The shipped two-node launcher's dataset-reader mismatch prevents that progression with the supplied scenario text; correcting the loader selection is necessary, not evidence that training succeeds.

Endpoints/progression: shaped rollout rewards → final response-token scores → loop/GRPO advantages → worker actor update → later rollout/checkpoint. Owner: RewardManager, trainer and actor worker. Trigger: successful batch generation and configured critic-warmup threshold. Proposed change: numerical policy update. Admission: optimizer-driven training, not a semantic candidate-review gate. The model proposes task code, while the training algorithm determines parameter changes; the operator supplies hyperparameters and can stop/restart, with no per-update human approval in the loop. Answer oracle: AppWorld outcomes upstream, modified by reuse counting; optional reward-model scores bypass ordinary reward placement. Operating mode: bounded RL curriculum. Guidance is task/skill prompting plus configured optimization objective; retained products are weights and checkpoint state, not formulated revisions to method text. Recovery: checkpoint save/resume supports earlier numerical state, without a quality-based automatic rollback. SRC-1, `sage/verl/trainer/main_ppo.py`, `sage/verl/trainer/ppo/ray_trainer.py`, `sage/verl/workers/fsdp_workers.py`.

- Immediate return: actor update metrics to the driver.
- Later read-back: later generations use the actor/rollout integration; saved actor, optional critic and dataloader state can be loaded on resume.
- Delegated visibility: distributed workers receive training batches; rollout sharding coordinates generation separately from AppWorld subprocesses.
- Selection predicate: training batches, configured advantage estimator, masks and warmup; this is not best-candidate deployment selection.
- Invalidation or expiry: repeated updates replace numerical state; checkpoint retention is configured, remote HDFS resume is explicitly unsupported.
- Activation or effect: parameter-changing calls and later generation are wired; actual learned behavior and benefit remain unobserved.
- Evidence limits: shipped two-node configuration is blocked upstream by dataset-reader selection; internal update wiring does not establish launcher reachability. No causal training comparison, exact initial weights or successful resume trace is supplied; dormant wiring does not prove exercised self-improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> score = data_item.batch['rewards']
> 
> reward_tensor[i, valid_response_length - 1] = score
> --- `sage/verl/trainer/main_ppo.py`

> actor_output = self.actor_rollout_wg.update_actor(batch)
> --- `sage/verl/trainer/ppo/ray_trainer.py`

The objective is task success with rewarded reuse, specified independently of a particular parameter update. Conditional on reaching training after correcting the launcher mismatch, this supports an improvement-directed self-change mechanism over later training iterations, not observed success: outcome-to-update, changed-weights-to-generation wiring are inspected, but subsequent behavior causally depending on a particular change is unobserved. No learning-benefit or exercised self-improvement attribution is made.

#### RT-RTE-evaluation-loop
Label: Evaluation task loop

Endpoints/progression: configured runner → one agent → sequential task worlds → model responses → extracted Python → evaluation → function extraction/output. Owner: runner partitions task IDs, agent controls steps, model chooses Python, external evaluator determines task success. Trigger: operator's evaluation command. Operating mode: bounded dataset/task execution with optional library accumulation. Model-call exception recovery substitutes a completion API call; cost and step limits can also stop the loop. Proposed library changes are generated/retrieved definitions parsed from code history; no human per-function approval is wired. Default admission runs after evaluation without requiring success. With `use_label`, the previous task's success controls extraction. Oracle is the current task's AppWorld pass fraction for the returned success value, but not the default library-admission predicate. Source guidance is [RT-CLM-function-rules](#rt-clm-function-rules). Appended definitions persist; extraction merges duplicate names within the collected task content. SRC-1, `patches/appworld/experiments/code/skill_library_agent/run.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

- Immediate return: task-success Boolean to the sequential caller; generated code effects occur in AppWorld; logger writes task artifacts.
- Later read-back: agent-level function list is available to later task initialization; constructor optionally reads a separately located predefined library, not automatically its output JSONL.
- Delegated visibility: separate process chunks have separate agent lists; no shared-library coordination is established in this runner.
- Selection predicate: default retrieval matches scenario `_1` then `_2` task identifiers and deduplicates names; alternatives rank skill embeddings (up to six ranked entries), threshold top-two query matches or n-grams.
- Invalidation or expiry: messages reset per task while function list survives within the agent; failed-definition execution clears prompt text, not a transactional world rollback.
- Activation or effect: selected definitions execute before first model call and are rendered as guidance; useful model reliance remains unobserved.
- Evidence limits: retrieval methods have different gates, generated output is not proof of correctness, and restart recovery from output is not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.use_skill_library:
>     if self.use_label:
>         if last_task_success:
>             self.extract_and_save_skills(world)
>     else:
>         self.extract_and_save_skills(world)
> --- `patches/appworld/experiments/code/skill_library_agent/agent.py`

> retrieval_execution_output = world.execute(self.retrieved_skills_prompt),
> if retrieval_execution_output[0]!='Execution successful.':
>     self.retrieved_skills_prompt = ""
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

#### RT-RTE-expert-admission
Label: Expert scenario admission

Endpoints/progression: rollout runner → three sequential scenario tasks with retries → evaluator → fresh verification world → merged function records and logged LM calls. Owner: rollout agent and base `rollout_scenarios`; model proposes Python, evaluator and string gate decide acceptance. Trigger: expert-generation launch and next scenario task. Change: accumulate functions for later tasks and admit successful trajectories for subsequent dataset extraction. Software vetoes failed evaluation, first-task empty function extraction and failed fresh-world definition execution. No human per-trajectory admission is wired. Oracle: AppWorld `evaluate_task` success, followed by execution-status check; verification does not establish that each function computes the correct result on new inputs. Operating mode: bounded three-task scenario curriculum, up to 20 retries per task. Guidance: rollout prompt and available prior functions; retained result: functions and logs, not an explicit criticism of a proposed theory. Recovery: retry, then record failed task and continue; library resets per scenario. SRC-1, `patches/appworld/experiments/code/skill_library_agent/run_rollout.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`.

- Immediate return: accepted scenario progression and task logs; failures append task IDs.
- Later read-back: accumulated functions execute and enter prompts of later scenario tasks; LM-call logs are consumed by [RT-RTE-sft-admission](#rt-rte-sft-admission).
- Delegated visibility: each temperature launcher has its own process/output; verification world gets extracted definitions, not the original runtime variables.
- Selection predicate: benchmark success, nonempty functions on first task, and no failure marker when definitions execute in verification.
- Invalidation or expiry: retry discards the attempted task context; per-scenario function list resets; admitted records merge by the code's name-derived key.
- Activation or effect: later task initialization is wired to the retained definitions; execution evidence is not supplied.
- Evidence limits: testing definitions is weaker than testing their calls; concurrency and extractor readiness are not enforced by the shell launcher.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> while not success_rollout and retry_num < 20:
> --- `patches/appworld/experiments/code/skill_library_agent/agent.py`

> retrieval_execution_output = world_verify.execute(retrieved_skills_prompt)
> if "Execution failed." in retrieval_execution_output:
>     continue
> --- `patches/appworld/experiments/code/skill_library_agent/agent.py`

#### RT-RTE-sft-admission
Label: Expert traces to SFT

Endpoints/progression: output logs/failure lists → selected final LM-call messages → normalized JSON dataset → supervised processor labels → configured full fine-tuning. Owner: extraction script, SFT processor and external training machinery. Trigger: explicit extraction and SFT launch. Proposed change: model weights from accepted trajectory data. Admission: script selects complete scenarios and first two tasks of scenarios failing task three, excludes any message carrying the no-code marker, normalizes assistant code fences and user/assistant whitespace, then writes dataset JSON. Human operator initiates/configures; software performs content selection without per-example human veto. Oracle: prior rollout outcomes, not a fresh reference answer in the extractor; YAML additionally names a dev dataset whose contents are not frozen. Operating mode: offline supervised training. Prompt-turn masking and length cutoff determine which token targets survive; not every logged token trains the model. Recovery: model saves are configured, resume is null in this YAML; no automatic quality-based rollback is established. SRC-1, `patches/appworld/extract_expert_dataset.py`, `patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py`, `patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml`, `patches/LLaMA-Factory/run_sft.sh`.

- Immediate return: expert dataset JSON; configured training outputs model artifacts and metrics if the external machinery executes successfully.
- Later read-back: SFT consumes the dataset; RL can consume a selected SFT model only after operator fills its model path.
- Delegated visibility: Accelerate/Slurm distributes training; this is computational coordination, not independent agent judgment.
- Selection predicate: hard-coded scenarios/temperature directories and failure-list logic, no-code filtering, then supervised cutoff and prompt-turn mask.
- Invalidation or expiry: extractor overwrites output JSON; training config allows output overwrite; prior artifact retention is not a correctness gate.
- Activation or effect: trace-to-weight production is configured; actual updated weights and downstream behavior are unobserved.
- Evidence limits: expert shell starts background generators then immediately extracts without a wait; its temperature range also differs from the extractor's expected list. A successful unattended generation-to-training run is not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> elif turn_idx < self.data_args.prompt_turn_idx:
>     target_label = [IGNORE_INDEX] * target_len
> else:
>     target_label = target_ids
> --- `patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py`

The extractor's defined `make_map_fn` is not its executed dataset-building route; the live route reads the last JSONL LM-call record and appends its assistant response. Thus the unused `messages[0:21]` slice cannot establish actual exported context truncation (SRC-1, `patches/appworld/extract_expert_dataset.py`).

### Claims

#### RT-CLM-function-rules
Label: Reusable function rules

Claimed operation: the model should create reusable, parameterized, typed, documented, self-contained multistep functions and prioritize applicable retained functions. Source is doctrine/design, not enforced validity. The executor and extractor do not implement these content requirements as structural checks. SRC-1, `patches/appworld/experiments/prompts/skill_library_agent.txt`, `sage/llm_agent/app_world/app_world_env.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> (6) Never call other functions from the skill library or any previously defined functions.
> 
> (7) Do not import any Python packages.
> --- `patches/appworld/experiments/prompts/skill_library_agent.txt`

> if isinstance(node, (ast.Import, ast.ImportFrom)):
>     import_lines.append(lines[node.lineno - 1])
> --- `sage/llm_agent/app_world/app_world_env.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-function-execution
Label: Retained function execution

Consumer: AppWorld interpreter. Channel: source strings from paired dictionaries or evaluation function records. Force: executable definitions/imports run before the model's first task step; later generated calls can use them. Horizon: paired second task in RL; later tasks in the evaluation agent, and separately loaded predefined libraries where supplied. Prompt suppression is not execution rollback. Evidence and scope: [RT-RTE-skill-install](#rt-rte-skill-install), [RT-RTE-evaluation-loop](#rt-rte-evaluation-loop); SRC-1, `sage/llm_agent/app_world/app_world_env.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

#### RT-BAP-function-guidance
Label: Retained function guidance

Consumer: task-solving language model. Channel: rendered `retrieved_skills` inside task prompt. Force: interpreted guidance, not mandatory call dispatch; includes source and descriptions, subject to initializer gates and context controls. Horizon: subsequent subtask/task model calls. Delivery is wired; compliance, invocation and benefit remain unobserved. Evidence: [RT-RTE-skill-install](#rt-rte-skill-install), [RT-RTE-evaluation-loop](#rt-rte-evaluation-loop); SRC-1, `patches/appworld/experiments/prompts/skill_library_agent.txt`, `sage/llm_agent/app_world/app_world_env.py`.

#### RT-BAP-policy-weights
Label: Updated policy authority

Consumer: later model inference. Channel: actor/rollout numerical parameters and explicitly selected checkpoints/models. Force: distributed-parametric determination of next-token probabilities, distinct from prompt advice and executable definitions. Horizon: later training iterations and resumed/selected model use. Actual causal dependence on a particular update is unobserved. Evidence: [RT-CMP-actor-rollout](#rt-cmp-actor-rollout), [RT-RTE-policy-update](#rt-rte-policy-update), [RT-RTE-sft-admission](#rt-rte-sft-admission); SRC-1, `sage/verl/workers/fsdp_workers.py`, `sage/verl/trainer/ppo/ray_trainer.py`.

## Annotations

none
