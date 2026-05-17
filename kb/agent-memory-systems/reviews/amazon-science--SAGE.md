---
description: "Amazon Science SAGE review: AppWorld traces, generated Python skills, skill-integrated rewards, SFT data, and GRPO checkpoints as distinct memory artifacts"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# Amazon Science SAGE

Amazon Science SAGE is the code release for "Skill Augmented GRPO for self-Evolution." It is not a general-purpose note memory system; it is an AppWorld training and evaluation stack where agents generate Python helper functions during rollouts, reuse those functions on later subtasks, receive skill-integrated rewards, and ultimately compile behavior into model checkpoints through SFT and GRPO.

**Repository:** https://github.com/amazon-science/SAGE

**Reviewed commit:** [3c9244e82244abb1adc5467ee601a03ba0f433a0](https://github.com/amazon-science/SAGE/commit/3c9244e82244abb1adc5467ee601a03ba0f433a0)

## Core Ideas

**The skill library is Python code extracted from agent turns.** The patched AppWorld agents parse generated code with `ast`, pull out top-level function definitions plus imports, and store records with `task_id`, `name`, and `function`. The evaluation agent can load `./predefined_skill_library/skill_library_functions.jsonl`; optional sidecars hold skill embeddings, query embeddings, and query lists for alternative retrieval modes ([patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py)).

**Rollout-time skills are transient system-definition artifacts.** During GRPO generation, `AppWorldLLMGenerationManager.run_llm_loop(...)` runs each sampled scenario in two subtask iterations. Iteration 0 extracts generated Python functions into an in-memory `skill_libraries` list. Iteration 1 injects those functions into the prompt, executes them in AppWorld before task solving, and counts a skill use when generated code calls one of the stored function names without redefining it ([sage/llm_agent/appworld_generation.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/appworld_generation.py), [sage/llm_agent/app_world/app_world_env.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/app_world/app_world_env.py)).

**The skill-integrated reward rewards both task success and reusable skill use.** AppWorld subprocesses return task-completion rewards from environment evaluation. SAGE then adjusts the two-round rewards: the first subtask gets an extra point only when the first and second subtasks succeed and at least one skill is used; the second subtask gets an extra point when it succeeds and a skill is used. GRPO/loop advantage computation groups outcome rewards by prompt index, so the behavior-changing signal is a scalar outcome reward over multi-agent rollouts, not a retrieved memory at deployment ([sage/llm_agent/app_world/app_world_env.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/app_world/app_world_env.py), [sage/llm_agent/appworld_generation.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/appworld_generation.py), [sage/verl/trainer/ppo/core_algos.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/core_algos.py)).

**SFT is a separate trace-to-dataset path.** The expert-data script runs a Claude-backed rollout agent over AppWorld scenarios and logs model calls. `extract_expert_dataset.py` reads the last `lm_calls.jsonl` record for successful or partially successful scenarios, normalizes the assistant code block, filters failed "No code available" traces, and writes `appworld_expert_dataset.json` for LLaMA-Factory. The patched LLaMA-Factory processor adds `prompt_turn_idx`, masking targets before a configured turn so training focuses on later assistant behavior ([patches/appworld/expert_dataset_generation_claude.sh](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/expert_dataset_generation_claude.sh), [patches/appworld/extract_expert_dataset.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/extract_expert_dataset.py), [patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py)).

**The durable learning target is model state.** The README requires an SFT model path before GRPO, the SFT patch writes full fine-tuning outputs under LLaMA-Factory, and the PPO trainer periodically saves actor checkpoints under `verl_checkpoints/{experiment}/global_step_{n}/actor`. The final retained behavior is therefore distributed-parametric model state, with dataloader state and logs as operational sidecars ([README.md](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/README.md), [patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml), [sage/run_sage_2nodes.sh](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/run_sage_2nodes.sh), [sage/verl/trainer/ppo/ray_trainer.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/ray_trainer.py)).

**Evaluation can use a file-backed skill library.** The AppWorld evaluation config names the deployed model `sage`, enables `use_skill_library`, and uses default retrieval. Default retrieval does not embed or learn; it selects skills whose task IDs match the current scenario's `_1` and `_2` tasks, executes the concatenated skill definitions, and clears them if execution fails ([patches/appworld/experiments/configs/sage_test_normal.jsonnet](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/configs/sage_test_normal.jsonnet), [patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py)).

## Comparison with Our System

SAGE is a trace-derived training system; commonplace is a files-first knowledge base for inspectable, maintainable behavior. The overlap is not "memory storage" in the ordinary retrieval sense, but artifact promotion across authority levels.

| Dimension | Amazon Science SAGE | Commonplace |
|---|---|---|
| Raw signal | AppWorld task rollouts, model-call logs, code executions, environment rewards | Source snapshots, notes, reviews, validation output, agent work traces |
| Intermediate artifact | Python function skills, `skill_library_functions.jsonl`, embeddings/query sidecars, SFT JSON | Markdown notes, instructions, ADRs, indexes, review reports |
| Main operative form | Symbolic Python during rollout; distributed-parametric checkpoints after SFT/GRPO | Prose and structured markdown, with scripts and validators where codified |
| Activation | Prompt injection and Python execution for skills; learned policy weights for final behavior | `rg`, indexes, links, instructions, validation, review gates |
| Reward/evaluation | AppWorld success plus skill-use reward; GRPO outcome advantage | Structural validation, semantic review, source-grounded maintenance |
| Lineage | Logs and JSONL datasets exist, but checkpoints are not linked back to individual skill functions by a formal manifest | Frontmatter, source links, archival status, generated indexes, validation reports |

Using [behavioral authority](../../notes/definitions/behavioral-authority.md) (who consumes a retained artifact, through which channel, and with what force), SAGE has a strong authority split. Raw AppWorld logs are [knowledge artifacts](../../notes/definitions/knowledge-artifact.md) when inspected as evidence. Generated Python functions become [system-definition artifacts](../../notes/definitions/system-definition-artifact.md) when injected and executed in the environment, because they directly constrain and enable action. SFT datasets and GRPO batches become system-definition artifacts for a learning consumer; checkpoints then carry the behavior with distributed-parametric authority.

Compared with commonplace, SAGE is stronger when the domain supplies many repeatable scored tasks. It can turn successful interaction traces into training signal without asking a maintainer to write a durable note. It is weaker on governance: a generated skill can affect training rewards or evaluation behavior without a review status, provenance bundle, expiration rule, or human-readable contract beyond its Python body and task ID.

## Borrowable Ideas

**Treat executable skills as a temporary authority surface.** SAGE's rollout library is useful because it exists only long enough to test whether generated functions help a neighboring subtask. A commonplace analogue would be workshop-local scripts or candidate skills that must prove value before promotion to durable instructions.

**Reward reuse, not just success.** The extra reward for solving the second subtask with a stored skill is a concrete way to make reusable procedure formation visible to the learner. Commonplace could borrow the metric framing for evaluations: a workflow should get credit for producing future-useful artifacts, not only for finishing the immediate task.

**Keep SFT data and RL rollouts separate.** SAGE has a cleaner story when expert Claude traces, extracted SFT JSON, rollout-time skill functions, rewards, and checkpoints are separate artifacts with separate consumers. That separation is directly borrowable for review language and future trace-derived workflows.

**Use scenario-local retrieval as a baseline before semantic retrieval.** The default AppWorld evaluation retrieves skills by scenario prefix, which is crude but inspectable. For commonplace, this reinforces starting with obvious lexical or structural routing before adding hidden embedding behavior.

**Mask non-operative history during learning.** The `prompt_turn_idx` addition in the SFT processor is a narrow but useful idea: not every earlier turn in a trajectory should receive equal learning authority. A commonplace analogue would be explicitly marking which part of a trace is evidence and which part is the promoted lesson.

## Trace-derived learning placement

**Trace source.** SAGE qualifies as trace-derived learning. It consumes AppWorld task trajectories: prompts, assistant code blocks, environment observations, execution success/failure, task completion, evaluation rewards, language-model call logs, and generated helper functions.

**Extraction.** There are three extraction paths. The SFT path extracts final successful expert conversations from `lm_calls.jsonl` into JSON training examples. The offline AppWorld skill-library path extracts Python functions from successful task code and can persist them in `skill_library_functions.jsonl` plus embedding/query sidecars. The GRPO path extracts functions from first-subtask generated code into an in-memory library, then rewards second-subtask success and skill use.

**Storage substrate.** Raw expert traces live in AppWorld experiment output directories and `lm_calls.jsonl`. SFT data is JSON consumed by LLaMA-Factory. File-backed skills live in JSONL and optional `.pt` embedding files. GRPO rollout skills live in process memory during `run_llm_loop(...)`. Learned behavior persists in SFT output directories and `verl_checkpoints/.../actor` model checkpoints; dataloader state and `latest_checkpointed_iteration.txt` are checkpoint sidecars.

**Representational form.** Raw traces are mixed: prose chat messages, symbolic Python code, execution outputs, scalar rewards, and environment metadata. Extracted skills are symbolic Python with prose names/task IDs. SFT examples are prose/symbolic conversation supervision. GRPO rewards and advantages are numeric training signals. Checkpoints are distributed-parametric retained artifacts.

**Lineage.** The lineage chain is AppWorld scenario/task -> rollout conversation and code execution -> extracted skill or SFT row -> reward/advantage batch -> model checkpoint. The code preserves task IDs in skill records and dataset rows, and checkpoint paths preserve global step. It does not build a formal manifest linking a checkpoint back to the exact generated functions, trajectories, reward events, SFT rows, and source commit that shaped it.

**Behavioral authority.** Raw logs are knowledge artifacts when used for audit or dataset construction. Extracted functions have system-definition authority when executed as AppWorld code or injected into a prompt as available procedures. SFT JSON and GRPO batches have system-definition authority as learning input. Actor checkpoints have the strongest authority because they carry the final policy used for future generation.

**Scope.** Scope is AppWorld- and scenario-local. The skill functions are not general KB entries; they encode API sequences for specific task families. The weights may generalize across AppWorld tasks, but the implementation evidence is benchmark-centered.

**Timing.** Learning is staged. Expert rollouts produce SFT data offline, SFT produces an initial model, GRPO generates two-subtask rollouts online during training, and checkpoints are saved periodically. Evaluation uses a deployed model and optional predefined skill library rather than updating memory in place.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), SAGE is a split case: it has a trajectory-to-executable-skill branch during rollouts and a trajectory-to-weights branch through SFT/GRPO. It strengthens the survey claim that one system can carry several retained artifacts with different storage substrates, representational forms, lineage, and behavioral authority.

## Curiosity Pass

**The "skill library" is not one artifact.** In evaluation, it can be a file-backed JSONL library with retrieval sidecars. In GRPO, it is a per-batch in-memory dictionary. In SFT, useful behavior is not loaded as a skill library at all; it is compiled into model weights.

**Skill validation is execution-shaped, not review-shaped.** SAGE checks whether concatenated function definitions execute and whether downstream tasks succeed. It does not validate function schemas, preconditions, source trace links, or stale API assumptions the way a durable skill library would need to.

**The reward teaches a preference for reusable procedure, but indirectly.** The actor is not trained to emit a canonical skill artifact for a permanent store. It is rewarded when first-round generated functions can be reused on a second task and the tasks succeed. That is enough to shape policy, but not enough to create a maintained external memory.

**The SFT dataset keeps less lineage than the logs.** `extract_expert_dataset.py` pulls the final model-call messages into a compact JSON file. That is practical for training, but the compact dataset loses much of the experiment-output context unless the original AppWorld directories are retained.

## What to Watch

- Whether future releases add a manifest linking checkpoints to AppWorld scenarios, SFT rows, generated functions, reward outcomes, and source revision.
- Whether the rollout skill library becomes a durable reviewed artifact or remains a transient training scaffold.
- Whether retrieval moves beyond scenario-prefix matching in the evaluation path, and whether embedding retrieval receives explicit governance.
- Whether skill-use reward improves general task performance or mainly teaches benchmark-local function naming and reuse.
- Whether later checkpoints expose enough audit data to separate behavior learned from expert SFT from behavior learned through skill-integrated GRPO.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: SAGE combines trajectory-to-executable-skill rollout memory with trajectory-to-weight learning through SFT and GRPO.
- [SkillWeaver](./SkillWeaver.md) - compares-with: both extract Python skill functions from AppWorld/web rollouts, but SAGE uses transient skill reuse as an RL reward signal while SkillWeaver promotes a file-backed executable library.
- [Agent-R](./agent-r.md) - compares-with: both convert environment traces into learning input, but Agent-R produces revision conversations while SAGE adds generated skills and reward shaping before checkpointing.
- [representational form](../../notes/definitions/representational-form.md) - exemplifies: SAGE moves between prose traces, symbolic Python functions, numeric rewards, and distributed-parametric checkpoints.
- [lineage](../../notes/definitions/lineage.md) - sharpens: the implementation preserves task IDs and checkpoint steps, but not a full checkpoint-to-trace derivation manifest.
