---
description: "SAGE review: AppWorld skill-library agent whose trace-extracted Python skills are pushed into later tasks and rewarded during GRPO"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# SAGE

SAGE, from `amazon-science/SAGE`, is a research implementation of Skill Augmented GRPO for self-evolving AppWorld agents. Its memory mechanism is not a general personal-memory store. It is a task-skill loop: successful AppWorld trajectories are mined for Python helper functions, those functions are retained as a skill library or as model-training signal, and later rollouts receive selected skills in their prompt or learn to generate and use them through SFT and GRPO.

**Repository:** https://github.com/amazon-science/SAGE

**Reviewed commit:** [3c9244e82244abb1adc5467ee601a03ba0f433a0](https://github.com/amazon-science/SAGE/commit/3c9244e82244abb1adc5467ee601a03ba0f433a0)

**Last checked:** 2026-06-01

## Core Ideas

**The retained unit is executable Python function text.** The AppWorld patch extracts top-level function definitions from generated code, preserves import lines, records each function with a task id and function name, and writes the result to `skill_library_functions.jsonl`. The same mechanism deduplicates by function name and can append new skills after normal evaluation runs ([skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [skill_library_agent_rollout.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py)).

**Skill read-back is prompt injection after an execution check.** Before an AppWorld task starts, the agent builds `retrieved_skills_prompt`, executes the concatenated functions in the environment, drops them if execution fails, and renders them into the prompt as `retrieved_skills`. In the normal config this is enabled with `use_skill_library: true` and `retrieval_method: "default"` ([skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [sage_test_normal.jsonnet](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/configs/sage_test_normal.jsonnet), [skill_library_agent.txt](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/prompts/skill_library_agent.txt)).

**The repository contains several activation policies, not one memory API.** The deployed evaluation config uses same-scenario retrieval: for task group `x`, it loads skills from `x_1` and `x_2`. The code also implements skill-embedding retrieval over function text, query-embedding retrieval over task instructions, and n-gram retrieval over prior queries with thresholds and top-k limits ([skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py)).

**SFT turns successful expert rollouts into model weights.** The data extraction script reads AppWorld `lm_calls.jsonl` logs from successful scenario rollouts, keeps the final assistant message after code extraction, filters examples with missing code, and writes `appworld_expert_dataset.json` for LLaMA-Factory. The patched supervised processor adds `prompt_turn_idx`, so early turns can be masked out of the training target ([extract_expert_dataset.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/extract_expert_dataset.py), [supervised.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py), [qwen2_5_32B_appworld.yaml](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml)).

**GRPO makes skill use part of the reward surface.** During SAGE training, each scenario produces two sampled subtasks. In subtask iteration 0, generated functions are stored in an in-memory skill library. In subtask iteration 1, those skills are inserted into the next prompt, calls to prior skill names are counted, and the final reward is boosted when the first and second subtasks succeed and at least one skill is used ([ray_trainer.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/ray_trainer.py), [appworld_generation.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/appworld_generation.py), [app_world_env.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/app_world/app_world_env.py)).

**The training stack is a modified veRL/AppWorld pipeline.** The `sage/` package is packaged as `verl`, run through Ray, vLLM, PPO/GRPO trainers, and AppWorld subprocesses. The memory-specific code is concentrated in `sage/llm_agent/` and the AppWorld patches; most of `sage/verl/` is training infrastructure rather than a standalone memory substrate ([sage](https://github.com/amazon-science/SAGE/tree/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage), [patches/appworld](https://github.com/amazon-science/SAGE/tree/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld), [run_sage_2nodes.sh](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/run_sage_2nodes.sh)).

**Context cost is bounded by selection, not store size.** Retrieval (same-scenario, embedding, query, or n-gram with top-k and thresholds) picks a few skills, executes them, and drops failures before inserting the rest, so the agent sees a small vetted skill block rather than the whole library — though each inserted skill is full function source.

## Artifact analysis

- **Storage substrate:** `files` — Filesystem JSONL under `predefined_skill_library/skill_library_functions.jsonl` when present, plus generated `skill_library_functions.jsonl` files in AppWorld output directories
- **Representational form:** `prose` `symbolic` `parametric` — prose task ids, prompts, and assistant code text; symbolic JSON records, Python functions, configs, reward code, and metadata; and distributed-parametric embeddings and model weights
- **Lineage:** `authored` `imported` `trace-extracted` — authored templates/configs/reward code, imported predefined skill libraries when present, and trace-extracted skills, datasets, embeddings, and checkpoints from AppWorld rollouts and logs
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — retained artifacts serve as experiment evidence, prompt instructions, execution-checked code, selector inputs, viability checks, retrieval/ranking state, and SFT/GRPO learning signal

**Predefined skill-library JSONL.** Storage substrate: filesystem JSONL under `predefined_skill_library/skill_library_functions.jsonl` when present, plus generated `skill_library_functions.jsonl` files in AppWorld output directories. Representational form: symbolic JSON records carrying prose task ids and executable Python function text. Lineage: extracted from successful or accepted agent trajectories by AST parsing generated code; imported predefined libraries have weaker visible provenance in this repo. Behavioral authority: system-definition artifact at read-back time because selected functions are inserted into the prompt and executed in the AppWorld environment before the next task.

**Skill and query embedding files.** Storage substrate: PyTorch `.pt` files such as `skill_embeddings.pt` and `query_embeddings.pt`, with `query_list.jsonl` for task ids and instructions. Representational form: distributed-parametric embeddings plus symbolic query/task metadata. Lineage: derived from extracted skill function text or AppWorld task instructions through a SentenceTransformer model. Behavioral authority: ranking system-definition artifact because embedding similarity determines which skills enter the agent context under the embedding retrieval modes.

**In-rollout skill libraries.** Storage substrate: Python dictionaries inside the SAGE AppWorld generation loop, scoped to a scenario batch rather than durable files. Representational form: symbolic function-name-to-code mappings. Lineage: extracted from the first sampled subtask's generated code and filtered only by execution success/failure handling. Behavioral authority: system-definition artifact for the second subtask because the functions are pushed into the next initial prompt and their later use changes reward.

**Expert transcript dataset.** Storage substrate: JSON written to `../LLaMA-Factory/data/appworld_expert_dataset.json`. Representational form: symbolic chat-message records with assistant code responses. Lineage: trace-extracted from `lm_calls.jsonl` logs of successful AppWorld expert-data runs, then filtered for missing executable code and processed by the SFT pipeline. Behavioral authority: learning input, producing distributed-parametric model state rather than a readable runtime memory.

**SFT and GRPO model checkpoints.** Storage substrate: model output directories under LLaMA-Factory and veRL checkpoint directories such as `saves/.../sft` and `verl_checkpoints/$EXPERIMENT_NAME`. Representational form: distributed-parametric weights. Lineage: SFT weights derive from expert transcripts; SAGE RL weights derive from AppWorld rollouts, environment rewards, skill-use bonuses, masks, and GRPO/PPO updates. Behavioral authority: system-definition artifact with the strongest force in the system, because it changes the policy that writes code, defines reusable functions, and decides whether to call pushed skills.

**Prompt templates and reward code.** Storage substrate: repo files in `patches/appworld/experiments/prompts/`, AppWorld configs, and `sage/llm_agent/appworld_generation.py`. Representational form: mixed prose templates and symbolic Python reward logic. Lineage: authored framework code. Behavioral authority: system-definition artifacts: they define what the agent sees, when skills are inserted, how observations are truncated, how skill usage is counted, and how success plus skill use becomes training reward.

The promotion path is trajectory -> extracted function -> skill library -> prompt insertion -> successful skill use -> reward update, with a second path from successful expert traces -> SFT dataset -> model weights. The system can cross representational forms: executable prose/symbolic skill text can either remain inspectable as JSONL or be absorbed into distributed-parametric weights. The weakest lineage point is reviewability: generated skills store task id, name, and function text, but not a durable pointer to the source log span, verifier result, model version, prompt version, or human acceptance status.

## Comparison with Our System

| Dimension | SAGE | Commonplace |
|---|---|---|
| Primary purpose | Improve AppWorld agents through skill extraction, skill-conditioned rollouts, SFT, and GRPO | Maintain a typed methodology KB for future agents and maintainers |
| Canonical retained unit | Python helper functions, embeddings, transcript datasets, model checkpoints | Git-tracked markdown artifacts, schemas, links, indexes, reviews, and reports |
| Learning loop | Agent trajectories become skills, datasets, rewards, and weights | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Selected or staged skills are pushed into prompts before action | Mostly pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | Execution check, task reward, skill-use reward, SFT/RL metrics | Collection contracts, schemas, deterministic validation, semantic review, git history |

SAGE is a useful contrast case because it treats "memory" as reusable executable procedure rather than explanatory knowledge. A generated helper function has high operational leverage: it can immediately log in, query APIs, normalize data, or complete a repeated AppWorld pattern. Commonplace's artifacts are slower and more inspectable: a note can explain when a procedure is valid, cite sources, and survive outside the task distribution that produced it.

The biggest divergence is authority. In SAGE, retained skill code crosses into the environment and model weights quickly. Once a skill is pushed into context or learned into the policy, it can change behavior without a prose review layer. Commonplace intentionally keeps most retained knowledge as readable evidence or typed guidance until validation or instruction machinery gives it stronger force.

**Read-back:** `push` — With engineered memory selection. From the acting AppWorld agent's perspective, retained skill functions arrive in the initial prompt before it asks for them; the deployed evaluation path is same-scenario identifier selection, while optional modes use embedding or lexical inference and the GRPO loop stages first-subtask skills into the second subtask.

### Borrowable Ideas

**Treat code snippets as promotable memory, but require provenance.** A Commonplace analogue would let repeated agent-written helper functions become retained artifacts only when they carry source task, validation result, owning collection, and intended authority. Ready as a workshop experiment; not ready for automatic promotion.

**Use an execution check before pushing code into context.** SAGE executes retrieved functions and drops the skill block if it fails. Commonplace could add a lightweight "import/parse/run smoke test" gate for generated scripts before they are included in a task packet. Ready where the artifact is executable.

**Reward reuse separately from success.** SAGE's reward code distinguishes task success from use of an earlier skill. A Commonplace analogue would track when prior notes, scripts, or review decisions were actually used in a successful maintenance task. Needs a careful anti-gaming design before becoming a metric.

**Keep activation policy swappable.** Same-scenario, embedding, query-embedding, and n-gram retrieval are simple alternatives behind one insertion point. Commonplace generated context could expose multiple selectors for the same packet target and compare them without changing the consuming workflow. Ready for evaluation harnesses, not general authoring.

**Separate inspectable skills from absorbed policy learning.** SAGE keeps skill JSONL and also trains model weights. Commonplace should preserve any learned selector or policy beside readable source artifacts, so the learned layer is an activation aid rather than the only copy of the knowledge. Ready as a design constraint.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` `trajectories` — AppWorld rollouts include generated code, environment outputs, completion/reward signals, `lm_calls.jsonl` conversation logs, and paired-subtask skill-use traces.

**Learning scope:** `per-task` `cross-task` — traces are task/scenario-scoped during extraction and rollout, then can become cross-task skill libraries, datasets, and policy weights.

**Learning timing:** `offline` `staged` — expert-data/SFT and persisted skill-library paths run offline, while the GRPO loop stages first-subtask skills into the second subtask before reward updates.

**Distilled form:** `prose` `symbolic` `parametric` — distilled outputs include assistant/code text, executable function records and activation metadata, embeddings, and trained model checkpoints.

**Trace source.** SAGE qualifies as trace-derived learning. The raw signals are AppWorld agent trajectories: generated code snippets, environment execution output, task completion status, evaluator rewards, `lm_calls.jsonl` conversation logs, and rollout-level skill-use counts. In SAGE training, paired subtasks within a scenario also provide a local trace source: functions generated in the first subtask can be tested through use in the second.

**Extraction.** Extraction is mostly syntactic and reward-gated. The skill code parses generated Python with `ast`, keeps function definitions and imports, deduplicates by function name, and writes function records when runs are accepted. Expert-data extraction reads final LLM-call records from successful rollouts and converts them into SFT conversations. GRPO then uses task reward plus a skill-use bonus as the oracle for updating model weights.

**Scope and timing.** Scope is AppWorld scenario/task-level, not project-level user memory. Offline expert-data generation produces durable transcript datasets and SFT weights. Evaluation-time skill libraries can be loaded from disk and appended after tasks. RL-time skill libraries are staged within a rollout batch: first subtask generates functions, second subtask receives them, and the final reward updates the policy.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), SAGE sits in both trace-to-tool and trace-to-policy territory. It strengthens the survey's raw/distilled distinction: functions are readable distilled artifacts, embeddings are activation artifacts, and SFT/GRPO checkpoints are distributed-parametric system-definition artifacts derived from the same behavioral traces.

## Read-back placement

**Direction.** SAGE uses push from the acting agent's perspective. Retrieved or staged retained functions are inserted into the initial prompt before code generation; the agent does not choose a separate memory-search action.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — default and GRPO paths key on scenario/task or rollout slots, while optional n-gram and embedding modes infer relevance from task text, query text, or function text.

**Read-back timing:** `pre-action` — retained functions are inserted before the acting AppWorld agent's first code action for the task or paired subtask.

**Faithfulness tested:** `yes` — SAGE executes retrieved skill blocks, counts later function-name use, and makes skill use reward-relevant, while still not proving causal contribution to task success.

**Targeting and signal.** The push is instance-targeted. In the deployed evaluation config, the selector matches the current task's scenario group to retained skill `task_id` values, so the signal is `identifier`. Optional skill-embedding retrieval uses `inferred / embedding` over the current instruction and retained function text; optional query-embedding retrieval uses `inferred / embedding` to select prior query ids and then joins skills by `task_id`; optional n-gram retrieval is `inferred / lexical` followed by the same task-id join. In the GRPO loop, first-subtask skills are carried to the paired second subtask through the rollout's subtask schedule and per-environment skill-library slot, an instance-scoped identifier/schedule signal. The code gives thresholds and top-k limits for some modes, but precision and recall are not verified from code.

**Timing relative to action.** Read-back happens before the agent's first code action for the task or subtask. That means a pushed function can change the first plan, first API call, and subsequent execution path.

**Selection, scope, and complexity.** Evaluation-time default retrieval loads functions from earlier tasks in the same scenario group. Embedding and n-gram modes cap retrieved query groups or functions. RL-time read-back is narrower: only functions generated in the first subtask's in-memory library are available to the second subtask. Complexity is bounded by prompt length and observation truncation, but actual context dilution is not verified from code, and the system does not deeply summarize or cite source traces behind each function.

**Authority at consumption.** Pushed skills are advisory prompt context and executable environment definitions. They are stronger than examples because the environment receives function definitions before later code can call them, but weaker than hard constraints because the model may ignore them. In RL training, use of a skill becomes reward-relevant, increasing authority through the learning loop.

**Faithfulness.** SAGE checks syntactic/execution viability by running the retrieved skill block and counts whether function names appear in later generated code without being redefined. It does not prove that a function's body caused task success, and name-based usage can overstate behavioral contribution.

**Other consumers.** Human researchers can inspect JSONL skills, prompt templates, logs, datasets, and checkpoints. The same artifacts serve as experiment evidence, reusable runtime code, activation state, and model-training input.

## Curiosity Pass

**The strongest memory is not the skill file, but the trained policy.** The JSONL library is readable, but SFT and GRPO weights eventually carry much of the behavioral change. That makes SAGE less inspectable than a pure skill-library system even though it begins with explicit functions.

**Default retrieval is simpler than the paper-level framing may suggest.** The evaluation config uses same-scenario retrieval, while embedding and n-gram matchers exist as options in code. The most reproducible path is therefore structured task grouping, not a general semantic memory service.

**The execution check is valuable but shallow.** Running the concatenated functions catches broken definitions, but it does not verify that a function is safe, relevant, non-stale, or faithful to the trajectory that produced it.

**Skill-use reward has noisy credit assignment.** Counting a function name in generated code is an inexpensive signal, but it does not distinguish a decisive helper from a harmless call, dead code, or a copied name.

**There is little artifact governance around generated skills.** Function records have task ids and names, but no typed status, owner, review result, source span, or invalidation rule. That is acceptable for a benchmark loop and risky as a durable agent-memory practice.

## What to Watch

- Whether SAGE adds provenance fields to skill records; that would make extracted functions auditable instead of merely reusable.
- Whether skill-use credit moves from name matching to execution-level contribution tests; that would make the reward less gameable and more useful as a Commonplace evaluation analogue.
- Whether embedding retrieval becomes the default evaluation path; that would turn SAGE from scenario-keyed reuse into a more general relevance-gated memory system.
- Whether extracted skills get pruning, review, or versioning; that would show whether the library can remain useful as it grows beyond a benchmark run.
- Whether future code separates skill activation metrics from policy-learning metrics; that would clarify how much improvement comes from explicit read-back versus absorbed model weights.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: SAGE turns AppWorld traces into skill functions, SFT data, reward signal, and policy weights.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: SAGE spans JSONL skills, embeddings, datasets, prompts, reward code, and model checkpoints.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: SAGE's skills matter because the runner actively inserts selected functions into prompts.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: SAGE extracts reusable helper functions from prior agent behavior.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - exemplifies: SAGE preloads task-relevant functions before the agent starts acting.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: skill functions, reward logic, and checkpoints directly shape later behavior.
