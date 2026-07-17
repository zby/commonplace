---
description: "SkillRL review: trajectory-derived SkillBank JSON, prompt-time skill push, dynamic failed-trajectory updates, and SFT/RL policy learning"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-30"
tags: [trace-learning]
---

# SkillRL

SkillRL, from `aiming-lab/SkillRL`, is a VERL-derived reinforcement-learning stack for agents in ALFWorld, WebShop, and search environments. At the reviewed commit, its memory system is a trace-extracted SkillBank: generated memories and concise JSON skills are distilled from rollout trajectories, rendered into "Retrieved Relevant Experience" prompt blocks at SFT and RL time, and optionally extended during training from failed trajectories. The README's broader framing about recursive skill-augmented RL is partly implemented; the code-grounded memory surface is the JSON SkillBank plus prompt injection and failure-triggered append-only skill updates.

**Repository:** https://github.com/aiming-lab/SkillRL

**Reviewed commit:** [8e66726ed866a4e0a7f053586a41022798192e6c](https://github.com/aiming-lab/SkillRL/commit/8e66726ed866a4e0a7f053586a41022798192e6c)

**Source directory:** `related-systems/aiming-lab--SkillRL`

## Core Ideas

**Trajectory memories are intermediate, not the final serving format.** The retained `memory_data/*/generated_memories*.json` records hold task metadata, success/failure outcome, refined trajectories, planning patterns, and mistakes; `skill_generation/*.py` and the newer SFT pipeline aggregate those records into `claude_style_skills*.json` SkillBanks ([memory_data/alfworld/generated_memories_alfworld_total.json](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/memory_data/alfworld/generated_memories_alfworld_total.json), [skill_generation/alfworld.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/skill_generation/alfworld.py), [examples/sft_data_generation/skill_memory/aggregate_skills.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/examples/sft_data_generation/skill_memory/aggregate_skills.py)). The durable prompt-facing memory is therefore compact skill prose, not raw trajectory replay.

**SkillBank records are prose rules in symbolic JSON.** The advertised format has `general_skills`, task- or query-specific skills, and `common_mistakes`; shipped ALFWorld/Search files follow that shape, though the runtime `SkillsOnlyMemory` only reads `task_specific_skills`, so Search's `query_type_skills` are used by the SFT distillation helper but not by the skill-enabled search RL script at this commit ([README.md](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/README.md), [memory_data/search/claude_style_skills_search.json](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/memory_data/search/claude_style_skills_search.json), [agent_system/memory/skills_only_memory.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/memory/skills_only_memory.py), [examples/sft_data_generation/distillation/skill_retrieval.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/examples/sft_data_generation/distillation/skill_retrieval.py)).

**Read-back is host-pushed prompt context.** Environment managers retrieve skills once at reset, cache the result per task, and inject a formatted "Retrieved Relevant Experience" block into later step prompts when history is present ([agent_system/environments/env_manager.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/environments/env_manager.py), [agent_system/environments/prompts/alfworld.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/environments/prompts/alfworld.py), [agent_system/environments/prompts/webshop.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/environments/prompts/webshop.py), [agent_system/environments/prompts/search.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/environments/prompts/search.py)). The acting model does not decide to search memory; the harness places selected skills in its context.

**Dynamic update is implemented as failed-trajectory skill acquisition.** `ray_trainer.py` can trigger skill updates when validation or training success rates fall below a threshold, parse failed prompt/response trajectories, ask `SkillUpdater` to generate new `dyn_NNN` skills with Azure OpenAI `o3`, append them to the training environment's general skills, and save `updated_skills_step*.json` under the trainer output directory ([verl/trainer/ppo/ray_trainer.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/verl/trainer/ppo/ray_trainer.py), [agent_system/memory/skill_updater.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/memory/skill_updater.py)). It appends new general skills rather than revising or invalidating existing skill records.

**Context efficiency is top-k/category compression, not a full budgeter.** Template mode injects dynamic general skills plus the first static general skills and all or capped task-specific category skills; embedding mode precomputes skill embeddings and ranks general and task-specific skills by cosine similarity. WebShop has a hard fallback that drops to a no-memory prompt if the assembled observation exceeds 13,000 characters, but there is no general token-budget optimizer, provenance-aware progressive disclosure, or per-step retrieval refresh ([agent_system/memory/skills_only_memory.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/memory/skills_only_memory.py), [agent_system/environments/env_manager.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/agent_system/environments/env_manager.py)). The README's 10-20% compression claim is not independently verified by these code paths.

**The SkillBank also trains into model weights.** The SFT data-generation pipeline parses rollout text, creates per-trajectory memories, aggregates a skill bank, renders skills into a system prompt, asks `o3` for reasoning, and writes ShareGPT/Alpaca-style examples; RL scripts then train with skill prompts enabled ([examples/sft_data_generation/README.md](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/examples/sft_data_generation/README.md), [examples/sft_data_generation/run_alfworld.sh](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/examples/sft_data_generation/run_alfworld.sh), [examples/sft_data_generation/distillation/distill_alfworld.py](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/examples/sft_data_generation/distillation/distill_alfworld.py), [examples/grpo_trainer/run_alfworld_skills.sh](https://github.com/aiming-lab/SkillRL/blob/8e66726ed866a4e0a7f053586a41022798192e6c/examples/grpo_trainer/run_alfworld_skills.sh)). That gives SkillRL both explicit prompt memory and a parametric downstream product.

## Artifact analysis

- **Storage substrate:** `files` `repo` `in-memory` `model-weights` — Durable memories and SkillBanks are JSON files in the repo or output directories, active retrieval lives in Python objects and optional embedding arrays, and SFT/RL turns skill-conditioned traces into model checkpoints.
- **Representational form:** `prose` `symbolic` `parametric` — Skills, mistakes, planning patterns, prompts, and generated reasoning are prose; JSON schemas-by-convention, category keys, ids, scripts, Hydra flags, prompt templates, and trainer gates are symbolic; embedding vectors and trained policy weights are parametric.
- **Lineage:** `authored` `imported` `trace-extracted` — Environment managers, prompts, generators, and scripts are authored; base models, benchmark environments, rollout dumps, and pretrained embedding models are imported; generated memories, SkillBanks, distilled SFT examples, dynamic `dyn_*` skills, and trained policies are extracted from successful or failed agent trajectories.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Raw/generated memories are evidence; selected skills become prompt instructions; category detection and retrieval mode route visibility; success-rate thresholds and postprocess validators gate updates/data; embedding similarity ranks skills; skill-updated training and SFT/RL learn from retained traces.

**Generated memory records.** Storage substrate: JSON under `memory_data/*/generated_memories*.json` or SFT pipeline outputs. Representational form: prose descriptions, refined trajectory summaries, planning patterns, and mistake records inside symbolic JSON. Lineage: trace-extracted from rollout text or generated memory data. Behavioral authority: knowledge artifact for aggregation, SFT construction, and optional legacy retrieval; by itself it does not instruct the live agent until rendered or summarized.

**SkillBank JSON.** Storage substrate: `memory_data/alfworld/claude_style_skills.json`, `memory_data/webshop/claude_style_skills.json`, `memory_data/search/claude_style_skills_search.json`, and `updated_skills_step*.json` outputs. Representational form: prose rules and mistakes under symbolic ids/categories. Lineage: trace-extracted through LLM aggregation, with authored schema conventions. Behavioral authority: instruction and routing authority when `SkillsOnlyMemory.format_for_prompt(...)` renders selected entries into prompts.

**Retrieval surfaces.** Storage substrate: in-memory loaded JSON plus optional in-memory embedding cache. Representational form: symbolic keyword/category rules, prose skill text, and parametric embeddings. Lineage: assembled from the current SkillBank at environment startup. Behavioral authority: routing/ranking authority over which skills reach the model; quality of relevance is not verified from code.

**Dynamic update artifacts.** Storage substrate: training-env memory object plus saved `updated_skills_step*.json`. Representational form: prose general skills with symbolic `dyn_NNN` ids. Lineage: trace-extracted from failed validation or training trajectories. Behavioral authority: learning/instruction authority for later training rollouts, but validation-based updates intentionally avoid writing into `val_envs`.

**Distilled SFT examples and checkpoints.** Storage substrate: generated ShareGPT/Alpaca JSON files and external model checkpoints. Representational form: prose prompts/reasoning, symbolic action tags, and parametric policy weights after SFT/RL. Lineage: trace-extracted from successful rollouts plus LLM-generated reasoning. Behavioral authority: learning authority; the SkillBank can become implicit policy behavior rather than explicit prompt text.

**Promotion path.** SkillRL promotes experience through: rollout text -> structured trajectory JSON -> generated memory record -> aggregated SkillBank -> prompt-injected runtime memory and/or SFT examples -> trained policy weights. The online/dynamic branch is shorter: failed trajectory -> `SkillUpdater` prompt -> appended general skill -> saved updated SkillBank -> later training prompts. Provenance is mostly coarse; final skills do not keep stable source trajectory ids or invalidation rules.

## Comparison with Our System

SkillRL and Commonplace both reject raw logs as the final memory surface. SkillRL distills trajectories into short procedural rules and mistakes, then pushes them into future prompts or model weights. Commonplace distills sources and work traces into typed Markdown notes, reviews, instructions, schemas, generated indexes, and validation records. SkillRL is stronger at automatically turning repeated task experience into behavioral guidance; Commonplace is stronger at source retention, explicit review state, link semantics, and deterministic validation before artifacts gain authority.

The closest alignment is the raw-to-promoted boundary. SkillRL's `generated_memories` are like workshop/evidence artifacts: useful but not the main action surface. The SkillBank is the promoted surface. Commonplace should preserve that distinction if it mines agent traces, but it would need stronger citations, source ids, and replacement/invalidation policy before a generated rule becomes instruction-level context.

The main divergence is read-back direction. SkillRL pushes selected skills into the model prompt, while Commonplace mostly expects agents to pull relevant files through `rg`, indexes, skills, and links. Push avoids making the acting agent search, but it hides relevance mistakes inside the prompt assembly layer.

Another divergence is parametric absorption. SkillRL's SFT/RL path can turn trace-extracted skills into model behavior. Commonplace treats retained knowledge as inspectable artifacts; using model weights as memory would weaken reviewability unless paired with evaluation probes and retained training lineage.

### Borrowable Ideas

**Use a two-stage trace distillation layer.** Commonplace could mine work logs into low-authority generated memories first, then aggregate only reviewed candidates into instructions or notes. Ready as a workshop pattern.

**Separate generated memory from served memory.** SkillRL keeps raw/generated trajectory abstractions distinct from compact SkillBank entries. Commonplace should keep trace evidence, candidate insights, and promoted artifacts as separate file types. Ready now.

**Treat dynamic skills as append-only candidates by default.** SkillRL appends `dyn_*` skills and saves snapshots instead of silently rewriting the base bank. Commonplace could use the same stance for mined procedural advice, but with review gates before activation. Ready with governance added.

**Do not borrow weak provenance for high-authority prompts.** SkillRL's final skills are concise, but they lose exact source trajectory ids and merge ancestry. Commonplace should retain source links and invalidation triggers before pushing generated advice. Ready as a design constraint, not a feature.

**Use skill prompts as an SFT data ingredient only with ablations.** Skill-conditioned examples are an interesting path for teaching common workflows, but Commonplace would need with/without-skill training or evaluation evidence before treating parametric absorption as memory improvement. Needs a concrete use case.

## Write side

**Write agency:** `manual` `automatic` — Operators choose rollout inputs, skill JSON paths, retrieval mode, model paths, update thresholds, and scripts, while the distinctive writes are automatic: trajectory parsing, LLM memory generation, skill aggregation, SFT example construction, training checkpoints, dynamic failed-trajectory skill creation, in-memory skill append, and saved updated SkillBanks.

**Curation operations:** `consolidate` `promote` — Aggregation compacts many generated memory records and planning patterns into fewer general/category skills and common mistakes; generated memories and failure traces are promoted into prompt-facing SkillBank entries, SFT examples, and possibly policy weights. I did not find semantic deduplication, in-place skill evolution, stale invalidation, decay, or durable cross-skill synthesis over already accepted skills.

### Trace-learning

**Trace source:** `trajectories` `tool-traces` `session-logs` — The qualifying traces are environment rollouts: observations, actions, admissible actions, search/information turns, rewards, success/failure labels, decoded prompts/responses, and per-task success metrics.

**Extraction.** Offline scripts parse rollout text into structured trajectories, use LLM prompts to produce contextual descriptions, refined trajectories, planning patterns, mistakes, aggregate skills, and distilled reasoning. Runtime dynamic update collects failed decoded prompt/response trajectories from validation or training, asks `SkillUpdater` for new skills, reassigns unique `dyn_NNN` ids, and appends accepted JSON entries.

**Learning scope:** `per-project` `cross-task` — Skill JSON files are environment/domain scoped, while general and category skills are meant to transfer across later tasks in ALFWorld, WebShop, or Search. The SFT/RL output can transfer across tasks covered by the trained checkpoint.

**Learning timing:** `offline` `staged` — The SFT pipeline and shipped SkillBanks are batch-generated. During RL, dynamic update can run at validation/test frequency or configured training update frequency, but new skills affect later training prompts rather than the already-running failed episode.

**Distilled form:** `prose` `symbolic` `parametric` — Distilled artifacts include prose skills/mistakes/reasoning, symbolic JSON ids/categories/action tags/configs, transient embeddings, and trained policy weights.

**Survey placement.** SkillRL belongs in the trace-to-procedural-skill and trace-to-policy branch. It strengthens the survey's raw/distilled split: raw rollouts are not the intended future context; compact skills and trained weights are. It also shows a split governance problem: prompt-facing JSON remains inspectable, while learned policy behavior becomes harder to audit.

## Read-back

**Read-back:** `push` — Retained skills reach the acting model because environment managers retrieve them at reset and inject formatted skill text into subsequent prompts; the SFT pipeline likewise places the SkillBank block in each training example's system prompt.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — Template mode always includes general skills, always includes dynamic general skills, and selects category skills by keyword rules over the task text; embedding mode ranks all loaded skills by cosine similarity to the task description. Search query-type skills are not read by the runtime `SkillsOnlyMemory` template path at this commit.

**Faithfulness tested:** `no` — The repository has skill-enabled training/evaluation scripts and success metrics, but I did not find a built-in causal memory-use test such as no-skill, wrong-skill, retrieved-skill, and all-skill ablations tied to individual read-back events.

**Direction edge case.** From the environment manager's perspective `retrieve(...)` is a pull call, but from the receiving model's perspective it is push: the model receives the memory block as part of the prompt and is not asked whether to query the SkillBank. The first initial observation uses the no-history template, so SkillBank push starts on later steps when history is present.

**Selection, scope, and complexity.** Scope is the loaded skills file and environment instance. Template mode is simple and cheap but coarse: first static general skills plus all or capped category skills. Embedding mode adds semantic ranking but keeps embeddings in memory. WebShop's length guard drops back to a no-history/no-memory prompt when assembled text is too long, so context efficiency is handled by rough caps and fallback rather than a general budget policy.

**Authority at consumption.** Skill text is advisory/instructional prompt context, not executable tools. The policy can still internalize skills through SFT/RL, where the authority becomes parametric behavior rather than visible prompt guidance.

**Other consumers.** Human operators inspect JSON memory/skill files, rollout dumps, distilled data, training logs, and saved updated skill banks. Training code consumes skill-conditioned prompts as learning data; the update loop consumes success-rate metrics and failed trajectory parses.

## Curiosity Pass

**The README's recursive-evolution story is narrower in code.** The dynamic path does analyze failures and append skills, but it does not revise existing skill content, attach source provenance, or update validation environments in the default validation-triggered path.

**Search has a schema split.** Search SFT distillation supports `query_type_skills`, but the live `SkillsOnlyMemory` template path looks for `task_specific_skills`, so the search RL script appears to get general skills and common mistakes but not query-type-specific skills.

**The older `RetrievalMemory` is a second memory system.** It can retrieve similar successful/failure trajectories with FAISS and format examples, but the advertised SkillBank scripts use `use_skills_only_memory=True`. Reviews should not treat the trajectory retriever as the main SkillRL read-back path unless a run enables `use_retrieval_memory`.

**Generation scripts are unevenly productionized.** The older `skill_generation/*.py` Azure clients are constructed with blank credentials in source, while the SFT-generation pipeline uses `OPENAI_API_KEY`. That makes the newer `examples/sft_data_generation/` path easier to reproduce from code.

**Prompt memory can disappear under length pressure.** WebShop drops to the no-history template when the assembled prompt exceeds 13,000 characters, which prevents blowups but also means memory activation is not monotonic.

## What to Watch

- Whether `SkillsOnlyMemory` gains first-class support for Search `query_type_skills`; that would change the runtime read-back surface for search tasks.
- Whether dynamic updates retain source trajectory ids, update reasons, and validation outcomes next to each `dyn_*` skill; that would make generated skills auditable enough for higher authority.
- Whether skill updates start revising, merging, retiring, or invalidating accepted skills; that would turn the current append/promote mechanism into real memory lifecycle management.
- Whether retrieval gets a stable budget policy beyond `top_k`, `task_specific_top_k`, and WebShop's length fallback; that determines whether the context-efficiency claim is an implementation property or only an evaluation result.
- Whether evaluations add causal read-back ablations and perturbation tests; that would strengthen claims that pushed skills, not only training setup, changed behavior.

Relevant Notes:

- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - applies: SkillRL distills rollout traces into durable skills and training examples.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: SkillRL has an explicit push path from SkillBank storage into prompt context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the review separates raw memories, SkillBank JSON, retrieval state, SFT examples, and model weights.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: skills move from evidence to prompt instruction and learning authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt templates, retrieval rules, trainer update gates, and SkillBank entries shape later behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - compares: template retrieval depends on detectable task/category symbols, while embedding mode falls back to inferred similarity.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) - applies: reward labels, LLM extraction, validation success rates, and policy improvements provide different strengths of evidence.
- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: SkillRL is a trace-to-skill and trace-to-policy system.
