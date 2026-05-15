---
description: "Amazon Science SAGE review: AppWorld skill-library rollouts, executable function reuse, skill-integrated rewards, and GRPO training"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-27"
---

# Amazon Science SAGE

Amazon Science SAGE is not the already reviewed `l33tdawg/sage` system. This SAGE is Amazon Science's Skill Augmented GRPO for self-Evolution codebase: a patched AppWorld agent, a VERL-based RL training loop, and a small LLaMA-Factory patch set for SFT data generated from AppWorld expert rollouts. The memory mechanism is not a general note store; it is a transient executable skill library built from generated Python functions, reused inside paired AppWorld subtasks, and converted into model-weight updates through skill-integrated GRPO training.

**Repository:** https://github.com/amazon-science/SAGE

**Reviewed commit:** 3c9244e82244abb1adc5467ee601a03ba0f433a0

**Commit URL:** https://github.com/amazon-science/SAGE/commit/3c9244e82244abb1adc5467ee601a03ba0f433a0

## Core Ideas

**The durable product is an RL-trained agent, not a persistent KB.** The root README frames SAGE as Skill Augmented GRPO and points users to `sage/` for RL, patched AppWorld for evaluation, and patched LLaMA-Factory for SFT. The install scripts launch `verl.trainer.main_ppo` with AppWorld scenario files, a skill-library prompt, `algorithm.adv_estimator=loop`, eight rollout agents, state masking, and checkpoint output under `verl_checkpoints/`. The code therefore treats skills as rollout-time scaffolding for training rather than as a maintained external memory repository ([README.md](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/README.md), [sage/run_sage_2nodes.sh](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/run_sage_2nodes.sh)).

**The skill atom is a Python function extracted from agent code.** Both AppWorld evaluation and RL rollout paths parse generated Python with `ast`, keep top-level imports, and extract `FunctionDef` bodies by name. The prompt explicitly asks the model to define abstract, reusable, typed, multi-step functions and to avoid duplicating existing functions. This makes the memory unit executable code plus an implicit natural-language docstring, not an embedding-only episode or free-form reflection ([patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [patches/appworld/experiments/prompts/skill_library_agent.txt](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/prompts/skill_library_agent.txt)).

**Evaluation has a file-backed skill library, but training uses in-memory paired tasks.** `SkillLibraryAgent` can load `./predefined_skill_library/skill_library_functions.jsonl`, optional skill/query embeddings, retrieve by same scenario, n-gram, skill embedding, or query embedding, execute retrieved functions to ensure they import/run, and append newly extracted functions plus optional embedding files to `world.base_output_directory`. In contrast, `AppWorldLLMGenerationManager` initializes `skill_libraries = [{} ...]`, runs two sampled subtasks per scenario, extracts functions during `subtask_iter == 0`, then injects that in-memory library only when `subtask_iter == 1` ([patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [sage/llm_agent/appworld_generation.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/appworld_generation.py)).

**Skill reuse is rewarded, not merely observed.** The AppWorld batch environment executes retrieved skills before prompting and drops them if execution fails. During the second subtask, it counts a skill use when generated code references an existing skill name without redefining that function. Final reward adds skill-use bonuses only when both rounds succeed, so the training signal favors skills that survive execution and contribute to a successful follow-on task ([sage/llm_agent/app_world/app_world_env.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/app_world/app_world_env.py), [sage/llm_agent/appworld_generation.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/appworld_generation.py)).

**GRPO integration is implemented as group-relative outcome learning over AppWorld rollouts.** The trainer converts scenario IDs into two random AppWorld subtasks, repeats each batch by `n_agent`, runs the custom AppWorld generation loop, stores environment rewards on the final response token, and computes advantages with the `loop`/GRPO branch. In `loop` mode the advantage subtracts the per-prompt group mean without dividing by group standard deviation; actor loss can mask environment-state tokens before updating the model ([sage/verl/trainer/ppo/ray_trainer.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/ray_trainer.py), [sage/verl/trainer/ppo/core_algos.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/core_algos.py), [sage/verl/trainer/main_ppo.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/main_ppo.py)).

**SFT data generation is a separate trace pipeline.** The AppWorld patch can run Claude-powered rollouts across temperature sweeps, collect successful scenario logs, take the last `lm_calls.jsonl` entry for each task, normalize final code blocks, filter "No code available to execute" traces, and write `appworld_expert_dataset.json` for LLaMA-Factory. The LLaMA-Factory patch adds `prompt_turn_idx`, allowing earlier turns to be prompt context while later target turns train the model ([patches/appworld/expert_dataset_generation_claude.sh](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/expert_dataset_generation_claude.sh), [patches/appworld/extract_expert_dataset.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/extract_expert_dataset.py), [patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py)).

## Comparison with Our System

| Dimension | Amazon Science SAGE | Commonplace |
|---|---|---|
| Primary substrate | Generated Python functions during AppWorld rollouts, then model checkpoints | Markdown notes, sources, reviews, ADRs, instructions, generated indexes |
| Memory atom | Executable helper function extracted from generated code | Typed artifact with frontmatter, prose, links, and validation |
| Learning trigger | Paired scenario rollout success, skill reuse, GRPO/SFT training | Deliberate authoring, ingest, review, validation, and promotion |
| Retrieval | Same-scenario lookup, optional embeddings or n-gram for evaluation; in-memory handoff during RL | `rg`, indexes, frontmatter, authored links, reports |
| Verification | AppWorld execution, task completion reward, retrieved-skill smoke execution | Structural validation, semantic review, source grounding, explicit lifecycle |
| Promotion target | Model weights and optional AppWorld output JSONL/embedding files | Stronger external artifacts: notes, instructions, checks, indexes |
| Lifecycle | Append/overwrite function names inside run outputs; checkpoints retain learned policy | Status, archive, replacement, validation, regeneration, review workflows |

SAGE is closer to OS-Copilot than to a prose memory system: both promote generated code from task experience into future action capacity. The difference is that OS-Copilot's generated tools are the durable memory product, while SAGE uses functions as an intermediate training scaffold and expects the final policy checkpoint to internalize the behavior.

Compared with SkillX, SAGE is less explicit about a maintained skill-library schema. SkillX stores plan, functional, and atomic skill objects with metadata. SAGE stores functions in JSONL in evaluation/data-generation paths and plain dictionaries in RL rollouts; there is no versioned skill object, merge rationale, source trajectory pointer, or retirement state. Its distinctive contribution is not artifact management but the reward design that makes reuse of self-generated functions part of the RL objective.

Commonplace is stronger for provenance, audit, and maintenance. SAGE is stronger as evidence that an external symbolic artifact can be part of a training loop: the function library changes the second task's prompt and action surface, then the outcome is compiled into weights. For a KB methodology, the interesting pattern is the scaffold-to-compiled-policy path, not the particular AppWorld prompt.

## Borrowable Ideas

**Reward reuse only when the reused artifact survives execution.** Ready to borrow as an evaluation pattern. Commonplace should not count a generated helper, instruction, or skill as useful merely because it was retrieved; it should count use under a downstream success condition.

**Use paired tasks to test whether a skill generalizes.** Worth borrowing for workshops. SAGE's two-subtask scenario setup gives a concrete way to ask whether a procedure learned in one local context helps a related but distinct task.

**Smoke-execute retrieved executable memories before injection.** Ready for code-bearing artifacts. SAGE executes retrieved functions before presenting them; the commonplace analogue would be validating scripts, examples, or generated helpers before including them in an agent prompt.

**Compile temporary scaffold memory into a stronger substrate.** Needs a specific training or rule-promotion use case. SAGE uses transient skills to shape model weights. Commonplace could use a less opaque version of this pattern by turning temporary workshop artifacts into checked instructions, tests, or scripts after they prove downstream value.

**Do not borrow the artifact lifecycle as-is.** SAGE's skill dictionaries and JSONL outputs are enough for experiments, but not for a KB. They lack source trace IDs, review status, duplicate policy, supersession, provenance display, and deterministic regeneration.

## Trace-derived learning placement

**Trace source.** SAGE qualifies as trace-derived learning. The raw signals are AppWorld task trajectories: generated code blocks, environment observations, execution success or failure, task-completion rewards, scenario/subtask identity, and the functions extracted from generated code. The SFT path also consumes Claude rollout logs from `lm_calls.jsonl`.

**Extraction.** Extraction is mostly syntactic plus environment-gated. Python `FunctionDef` nodes are pulled from generated code, imports are preserved, duplicate names overwrite earlier bodies, retrieved functions are executed as a smoke test, and the second subtask counts skill use when generated code calls an existing function name without redefining it. SFT extraction takes successful rollout messages and normalizes the final code block.

**Representational form.** The intermediate form is symbolic executable code: Python functions embedded into prompts and executed in AppWorld. The final learned form is distributed-parametric model weights produced by SFT and GRPO. The system does not maintain a prose skill library as the primary artifact.

**Behavioral authority.** The function library is a system-definition artifact during rollout because it changes the agent's action surface and the prompt's expected behavior. The checkpoint is also system-definition-artifact use, but distributed-parametric: after training, the learned disposition is inside the model rather than in inspectable KB artifacts.

**Scope.** Scope is AppWorld-specific and scenario-local during RL. Evaluation retrieval can use predefined libraries and optional embeddings, but the core SAGE training loop passes skills from one sampled subtask to another within the same rollout scenario.

**Timing.** Learning is staged offline. Rollouts create and reuse functions during training episodes; rewards are computed from paired outcomes and skill counts; GRPO/SFT then update model weights. There is no deploy-time durable skill promotion loop in the inspected training code.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), SAGE belongs in a hybrid symbolic-to-opaque branch: traces first create executable symbolic skills, then successful reuse becomes a reward signal for weight updates. It strengthens the survey claim that external artifacts can be training scaffolds, and it splits executable-skill systems into two cases: durable tool libraries and transient skill libraries compiled into policy.

## Curiosity Pass

The name collision matters. This is not a personal/local "sage" memory manager; it is an AppWorld RL system built from patched dependencies and large-scale training scripts. Reviewing it as a general memory repository would overstate what the code implements.

The strongest mechanism is the second-round dependency. SAGE does not merely ask the model to write helper functions; it creates a paired situation where a helper from one task can be injected into a related next task, counted, and rewarded. That is a sharper learning signal than appending every generated function to a global library.

The weakest mechanism is lifecycle. A function can be syntactically extracted, smoke-executed, counted by name, and rewarded, but the repository does not expose a stable skill review process. There is no clear artifact contract for provenance, merge history, last successful use, deprecation, or human inspection beyond experiment outputs.

The GRPO implementation is code-grounded but tightly coupled to AppWorld. The trainer rewrites scenario IDs into two subtasks, assumes AppWorld rewards, and uses the skill-integrated reward formula in the generation manager. That makes SAGE useful evidence for environment-specific skill learning, not a drop-in general agent-memory layer.

## What to Watch

- Whether future releases persist skill libraries as first-class artifacts rather than transient dictionaries and experiment JSONL.
- Whether skill metadata gains source trajectory IDs, execution outcomes, reuse counts, and retirement state.
- Whether the reward design is evaluated outside AppWorld or remains benchmark-specific.
- Whether retrieved-skill execution becomes a stronger validator than "Execution successful." before prompt injection.
- Whether checkpoint learning is compared against an external durable skill library at deployment time.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: SAGE is a symbolic-to-opaque case where rollout-generated functions become GRPO/SFT training signal.
- [SkillX](./SkillX.md) - compares-with: both learn skill artifacts from AppWorld-style trajectories, but SkillX preserves a more explicit library while SAGE compiles reuse into policy.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both use executable generated functions as memory, but OS-Copilot keeps a durable tool repository while SAGE uses functions as training scaffolds.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: SAGE learns from deployment-like rollouts, but the durable result is offline checkpoint training rather than live KB promotion.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: SAGE separates raw traces, extracted symbolic functions, reward signals, and compiled model checkpoints.
