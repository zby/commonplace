---
description: "Amazon SAGE review: AppWorld rollouts become reusable Python skills, retrieval state, SFT data, and GRPO reward signal"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# Amazon Science SAGE

Amazon Science SAGE is the `amazon-science/SAGE` implementation of Skill Augmented GRPO for self-evolving AppWorld agents. At the reviewed commit, its memory system is a benchmark-specific skill loop: AppWorld trajectories produce Python helper functions, selected functions are inserted into later prompts, expert logs become supervised fine-tuning data, and GRPO rewards successful reuse of generated skills.

**Repository:** https://github.com/amazon-science/SAGE

**Reviewed commit:** [3c9244e82244abb1adc5467ee601a03ba0f433a0](https://github.com/amazon-science/SAGE/commit/3c9244e82244abb1adc5467ee601a03ba0f433a0)

**Last checked:** 2026-06-04

## Core Ideas

**The explicit memory unit is executable Python function text.** The AppWorld skill-library agent parses generated code with `ast`, keeps import lines plus top-level function definitions, records task id, function name, and function body, and writes the result to `skill_library_functions.jsonl` ([skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/agent.py)). The rollout variant keeps a per-scenario in-memory library, verifies generated skills in the next AppWorld world, and merges records by function name ([skill_library_agent_rollout.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py), [agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/agent.py)).

**Skill read-back is prompt insertion after an execution check.** At task initialization, the skill-library agent selects functions, concatenates them into `retrieved_skills_prompt`, executes that block in AppWorld, clears it on failure, and renders it into the prompt's `{{ retrieved_skills }}` slot ([skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [skill_library_agent.txt](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/prompts/skill_library_agent.txt)). The normal evaluation config enables `use_skill_library` and uses the `default` retrieval method ([sage_test_normal.jsonnet](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/configs/sage_test_normal.jsonnet)).

**Retrieval policy is swappable but the deployed evaluation path is scenario keyed.** The default selector loads skills from earlier tasks in the same scenario group, using task-id prefixes. Optional modes rank function text by SentenceTransformer skill embeddings, rank prior task queries by query embeddings, or match prior queries by n-gram overlap before joining back to skill task ids ([skill_library_agent.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py)). This is not a general user-memory API; it is an AppWorld scenario and task-selection harness.

**The training path turns traces into model behavior.** `extract_expert_dataset.py` reads `lm_calls.jsonl` logs from successful or partial expert-data runs, keeps final assistant code messages, filters no-code examples, and writes `appworld_expert_dataset.json` for LLaMA-Factory ([extract_expert_dataset.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/extract_expert_dataset.py)). The patched supervised processor masks target turns before `prompt_turn_idx`, and the SFT config trains Qwen2.5-32B on that AppWorld dataset ([supervised.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py), [qwen2_5_32B_appworld.yaml](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml)).

**GRPO stages first-subtask skills into a second subtask and rewards use.** The SAGE generation manager samples two subtasks per scenario, stores first-subtask function definitions in per-environment skill libraries, inserts them into second-subtask prompts, counts later calls to prior skill names, and adds reward when successful runs use those skills ([ray_trainer.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/ray_trainer.py), [appworld_generation.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/appworld_generation.py), [app_world_env.py](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/app_world/app_world_env.py)).

**Context efficiency is selection plus viability filtering, not summarization.** The agent does not load the whole skill library by default. Scenario-keyed retrieval selects earlier same-scenario functions; embedding and n-gram modes cap selected functions or query groups; retrieved code is executed before insertion. The inserted unit is still full function source, so complexity is bounded by selector limits and prompt truncation rather than by a provenance-aware compression policy.

## Artifact analysis

- **Storage substrate:** `files` `in-memory` `model-weights` — durable skill libraries, embedding files, query lists, expert datasets, logs, and checkpoints live as local files; GRPO uses per-batch in-memory skill dictionaries; learned behavior persists in SFT and veRL checkpoint directories.
- **Representational form:** `prose` `symbolic` `parametric` — prompts and task instructions are prose; JSONL records, Python function bodies, configs, and reward code are symbolic; embeddings and trained model weights are distributed-parametric state.
- **Lineage:** `authored` `imported` `trace-extracted` — prompts, configs, and reward code are authored; modified AppWorld, LLaMA-Factory, veRL, and vLLM code are imported/adapted; skills, query records, expert datasets, embeddings, and checkpoints derive from AppWorld rollouts and LLM-call logs.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — retained artifacts serve as experiment evidence, prompt instructions, executable code, scenario/query selectors, execution checks, similarity rankers, and SFT/GRPO learning signal.

**Skill-library JSONL.** The central inspectable memory is a JSONL list of `task_id`, `name`, and `function` records. At rest it is a knowledge artifact and reusable code corpus; at read-back it becomes system-definition context because selected functions are executed in AppWorld and inserted into the prompt before the next task.

**Embedding and query files.** `skill_embeddings.pt`, `query_embeddings.pt`, and `query_list.jsonl` are derived access structures over function text or prior task instructions. They do not replace the skill records, but they have ranking authority when the selected retrieval mode uses similarity rather than scenario ids.

**In-rollout GRPO skill dictionaries.** During SAGE training, the skill store can be an in-memory dictionary scoped to a scenario batch. Functions generated in subtask iteration 0 are available to subtask iteration 1, and their later name-level use changes the final reward calculation.

**Expert transcript dataset and model checkpoints.** `lm_calls.jsonl` traces become an AppWorld SFT dataset, and SFT/GRPO outputs become model weights. These are less inspectable than JSONL skill functions but have stronger behavioral authority because they alter the policy that writes code and decides whether to use supplied skills.

**Prompt templates, configs, and reward code.** The prompt templates define how skill text appears to the agent, configs select the retrieval method, and reward code decides when skill use contributes to training. These authored system-definition artifacts control how trace-extracted memory gains future force.

Promotion path: AppWorld execution trace -> parsed function definition -> JSONL or in-memory skill record -> prompt insertion after execution check -> later skill call -> reward or evaluation signal -> SFT/GRPO model state. The path crosses from readable symbolic memory into distributed-parametric policy learning, while source-log provenance remains weak: function records do not preserve a source span, model version, verifier output, or prompt version beside each retained skill.

## Comparison with Our System

| Dimension | Amazon Science SAGE | Commonplace |
|---|---|---|
| Primary purpose | Improve AppWorld benchmark agents with extracted skills, SFT, and GRPO | Maintain a typed methodology KB for future agents and maintainers |
| Canonical retained unit | Python helper functions, embedding/query files, transcript datasets, model checkpoints | Git-tracked Markdown artifacts, schemas, links, indexes, reviews, and reports |
| Learning source | AppWorld trajectories, LLM-call logs, task rewards, and skill-use counts | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Selected skills are inserted into prompts before action | Mostly deliberate pull through search, indexes, links, skills, and review gates |
| Governance | Execution check, task success, skill-use reward, SFT/RL metrics | Collection contracts, schemas, deterministic validation, semantic review, git history |

SAGE is a useful contrast because its retained artifact is executable procedure, not explanatory knowledge. A helper function can immediately call AppWorld APIs, normalize data, or encode a repeated workflow. Commonplace artifacts usually carry weaker direct authority but stronger provenance, reviewability, and replacement history.

The sharp tradeoff is speed of authority. SAGE can turn a successful generated function into prompt context or model behavior quickly. Commonplace delays that transition until the artifact is typed, cited, connected, validated, and reviewed.

### Borrowable Ideas

**Treat repeated helper code as a promotable artifact.** Ready for bounded workshops. Commonplace could let repeated local maintenance functions graduate into scripts, but only with source task, validation result, scope, and owner metadata.

**Run executable retained context before injecting it.** Ready wherever the artifact is code. SAGE's execution check is shallow, but a parse/import/smoke-test gate would still catch broken generated utilities before they enter a task packet.

**Keep retrieval policy swappable behind one insertion point.** Ready for evaluation harnesses. Commonplace could compare path/tag, lexical, and embedding selectors for the same generated context target without changing the downstream workflow.

**Separate inspectable skills from learned policy state.** Ready as a design constraint. If Commonplace ever trains or tunes a selector, the learned layer should remain an activation aid beside readable source artifacts, not the only carrier of the knowledge.

**Reward reuse separately from success.** Needs anti-gaming design. SAGE's skill-use bonus is a useful measurement idea, but Commonplace would need evidence that reuse was relevant, not merely present.

## Write side

**Write agency:** `automatic` `manual` — AppWorld runs automatically extract and append skills, embeddings, query records, expert datasets, and checkpoints; operators manually choose configs, predefined libraries, data-generation scripts, and training/evaluation runs.

**Curation operations:** `dedup` `promote` — function-name replacement removes duplicate retained skills during extraction/merge, and successful traces can be promoted into reusable skill records, read-back indexes, SFT data, and model checkpoints.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — raw signal includes AppWorld code-generation turns, environment execution outputs, task success/evaluation, `lm_calls.jsonl` message logs, and paired-subtask skill-use traces.

**Learning scope:** `per-task` `cross-task` — traces are captured around individual AppWorld tasks or subtasks, then retained skills, datasets, and weights can influence later tasks within the benchmark distribution.

**Learning timing:** `offline` `staged` — expert-data extraction and SFT are offline; the GRPO loop stages first-subtask skills into the second subtask within a training rollout before policy updates.

**Distilled form:** `prose` `symbolic` `parametric` — retained outputs include prompt-visible code/prose, JSONL function records, embedding vectors, transcript datasets, and trained model checkpoints.

Extraction is mostly syntactic plus outcome-gated. Function extraction parses generated Python and keeps top-level definitions; expert-data extraction reads final logged model calls from successful or partial scenario runs; GRPO uses task reward plus a skill-use bonus as the oracle for policy updates. The raw trace remains evidence, while extracted functions and learned weights gain future behavior-shaping authority.

Survey placement: SAGE belongs in both trace-to-tool and trace-to-policy territory on the [trace-learning survey](../trace-learning-techniques-in-related-systems.md). It strengthens the survey's raw/distilled split: logs and rollouts are not the memory that later acts; extracted functions, retrieval state, and policy weights are.

## Read-back

**Read-back:** `push` — From the acting AppWorld agent's perspective, selected retained functions arrive in the initial prompt before code generation; the agent does not choose a separate memory-search action.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — The normal path keys by scenario/task identifiers, while optional n-gram and embedding modes infer relevance from task text, query text, or function text.

**Faithfulness tested:** `no` — SAGE checks whether retrieved code executes, counts later name-level skill use, and makes use reward-relevant, but I did not find a code-level with/without memory ablation or perturbation audit proving that a selected skill caused correct behavior.

**Direction edge cases.** The evaluation agent performs retrieval inside `initialize()`, before the model begins solving the task. The GRPO path similarly assembles initial prompts with first-subtask skills before the second subtask. Those are push reads for the receiving agent even though the harness performs the lookup.

**Targeting and signal.** Default evaluation uses an identifier signal: current task id prefix selects skills from earlier same-scenario tasks. GRPO uses the rollout schedule and per-environment skill dictionary as an instance-scoped identifier. Optional skill-embedding retrieval compares the current instruction to function embeddings; optional query-embedding retrieval compares current instruction to prior query embeddings and then joins to skill task ids; optional n-gram retrieval uses lexical overlap over prior query text.

**Selection, scope, and complexity.** Default retrieval loops through retained functions from two prior same-scenario task ids and deduplicates by function name. Skill-embedding retrieval stops after roughly six ranked entries; query-embedding and n-gram retrieval select up to two prior query groups over threshold. Retrieved code is full Python source, so prompt complexity can still be high even when count is bounded.

**Authority at consumption.** Pushed functions are advisory prompt context and executable environment definitions. The prompt tells the agent to prioritize suitable high-level functions but still judge applicability. In training, later use of a pushed skill affects reward, giving the read-back path learning authority in addition to prompt authority.

**Other consumers.** Human researchers can inspect skill JSONL, prompt files, logs, expert datasets, embedding files, and checkpoints. Those surfaces are useful evidence, but the agent-facing behavior comes from prompt insertion and learned policy state.

## Curiosity Pass

**The most durable memory may be the model, not the skill file.** JSONL skills are readable, but SFT and GRPO checkpoints absorb behavior into weights where provenance and inspection are much weaker.

**The default selector is simpler than the retrieval menu.** Embedding and n-gram selectors are implemented, but the normal evaluation config uses same-scenario task ids. The most reproducible read-back path is structured benchmark grouping, not general semantic memory.

**Execution checks are necessary but narrow.** Executing concatenated functions catches broken definitions, but it does not prove relevance, safety, freshness, or causal contribution.

**Skill-use reward is name-based.** Counting a function name in generated code is cheap, but it can overstate contribution if the call is incidental, redundant, or only correlated with task success.

**Skill records have little governance metadata.** The stored record carries task id, name, and function text, but not source log span, acceptance rationale, verifier output, model version, prompt version, expiry, or reviewer status.

## What to Watch

- Whether skill records gain source spans, verifier results, model/prompt version, and task reward metadata; that would make generated code more auditable as retained behavior.
- Whether evaluation distinguishes explicit skill-library read-back gains from absorbed policy-learning gains; that would clarify which memory surface is doing the work.
- Whether relevance selection moves from same-scenario keys to embedding or lexical modes in the default configs; that would change the system from benchmark-group reuse to a more general context selector.
- Whether skill-use credit moves beyond function-name matching to execution-level contribution tests; that would make the reward less gameable.
- Whether the library adds pruning, invalidation, or review for stale generated functions as the corpus grows.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: SAGE turns AppWorld trajectories into skill functions, SFT data, reward signal, and policy weights.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: SAGE's skill library matters because the runner inserts selected functions into prompts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: SAGE spans JSONL skills, embeddings, datasets, prompts, reward code, and checkpoints.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: logs, datasets, and retained skill records are evidence until consumed by selectors, prompts, or training.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skill functions, retrieval indexes, reward code, prompts, and checkpoints shape later behavior.
- [Use trace extraction](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: SAGE extracts reusable helper functions and learned policy state from agent trajectories.
