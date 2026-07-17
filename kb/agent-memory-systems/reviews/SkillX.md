---
description: "SkillX review: trajectory-derived planning, functional, and atomic skill libraries with filtering, merging, and prompt-time retrieval"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
tags: [trace-learning]
---

# SkillX

SkillX, from the `zjunlp/SkillX` repository, is a framework for constructing reusable skill knowledge bases from tool-agent experience. At the reviewed commit, the implementation loads successful trajectories, extracts task plans and skills with LLM prompts, filters and merges skills, saves JSON skill libraries, and provides an inference service that retrieves plans and skills into benchmark-specific system prompts. The strongest implemented memory surface is not raw trajectory replay; it is a retained library of planning, functional, and atomic skill records distilled from successful traces.

**Repository:** https://github.com/zjunlp/SkillX

**Reviewed commit:** [0137cb8c2f9e69d5cc499e562dea789b2c5a8e35](https://github.com/zjunlp/SkillX/commit/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35)

**Source directory:** `related-systems/zjunlp--SkillX`

## Core Ideas

**Experience is distilled into a three-level skill library.** The README frames SkillX as a reusable skill KB with planning, functional, and atomic skills; the code implements corresponding `PlanSkill`, `Skill`, and `SkillLibrary` structures, with functional and atomic skills sharing `name`, `document`, `content`, `tools`, and `metadata` fields ([README.md](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/README.md), [core/skill.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/skill.py)). Planning skills are step plans keyed by task; functional skills are reusable multi-step tool procedures; atomic skills are tool-centric usage guidance.

**The write path starts from successful trajectories.** `IterativeSkillPipeline._run_epoch(...)` filters trajectories by reward, summarizes long tool responses, extracts or combines plans, prepares the shortest successful trajectory per task, extracts skills, filters, clusters, merges, updates the library, and saves checkpoints ([pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/pipeline.py)). The central evidence signal is therefore task execution history plus reward, not human-authored skill files alone.

**Functional and atomic extraction use different coverage logic.** Functional extraction asks for skills for plan steps containing API/tool work; atomic extraction collects tools from successful trajectories, detects missing tools against an existing skill map, and prompts for tool-specific skills. The hybrid extractor runs functional extraction first, then adds atomic skills for uncovered tools ([extraction/skill_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/skill_extractor.py), [core/trajectory.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/trajectory.py)). This makes "missing tool coverage" an explicit extraction criterion.

**Quality control is LLM-mediated plus embedding clustering.** The two-stage filter checks general skill quality and tool-schema alignment, while DBSCAN clustering over embedding text groups similar skills before an LLM merger consolidates clusters ([filtering/pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/filtering/pipeline.py), [filtering/base.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/filtering/base.py), [clustering/dbscan.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/dbscan.py), [clustering/merger.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/merger.py)). The filters are useful gates, but their correctness depends on LLM judgment unless backed by concrete tool schemas.

**Read-back is prompt-time retrieval, not autonomous execution.** `SkillUsageService.prepare_prompt(...)` retrieves similar plans and skills, optionally selects a subset with an LLM, formats them, and returns a system prompt for AppWorld, BFCL, or tau2-Bench adapters ([inference/skill_usage.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/skill_usage.py), [inference/retriever.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/retriever.py), [inference/prompt_formatters.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/prompt_formatters.py)). The skills advise and instruct the model through prompt context; the AppWorld formatter explicitly says the Skill Library provides reference implementations, not callable functions.

**Context efficiency comes from compression and retrieval.** SkillX reduces context volume by summarizing long tool outputs during extraction, compressing successful traces into compact plans and skill records, retrieving only top-k similar plans/skills, and optionally applying an LLM selector when candidates exceed `max_skills` ([extraction/tool_summary.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/tool_summary.py), [inference/skill_usage.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/skill_usage.py)). It does not implement a persistent vector store or progressive file disclosure; embeddings are rebuilt in memory from the loaded JSON library.

## Artifact analysis

- **Storage substrate:** `files` `repo` `in-memory` — Trajectories and final libraries are JSON/JSONL files, the repository includes example `skillx_db/appworld/...` skill and plan libraries, and runtime retrieval builds in-memory skill objects and embedding arrays from a loaded library.
- **Representational form:** `prose` `symbolic` `parametric` — Plans, descriptions, prompts, and tool-use notes are prose; JSON library records, Python orchestration code, tool schemas, filter metadata, and prompt templates are symbolic; embedding vectors used for clustering and retrieval are parametric access structures.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompts, schemas, code, and example libraries are authored; benchmark trajectories and tool schemas are imported inputs; planning, functional, and atomic skills are extracted from successful trajectories, tool calls, rewards, and LLM judgments.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Raw trajectories are evidence; skill descriptions and contents become prompt instruction/reference material; embedding retrieval and LLM selectors route and rank skill visibility; filters and schema checks validate candidate skills; accepted skill records teach later agents by entering their prompt context.

**Trajectory records.** Raw trajectory items contain task ids, user tasks, interaction histories, tool calls, rewards, and metadata ([core/trajectory.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/trajectory.py), [data/loaders.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/data/loaders.py)). They are knowledge artifacts for extraction and audit; they do not directly enter the later agent prompt unless converted into plans or skills.

**Plan library.** Planning skills are prose step plans keyed by task, saved inside the library and retrieved by embedding similarity against a new task. They have routing and instruction authority when `plan_only` or `plan_with_skill` mode formats them into the system prompt.

**Functional and atomic skill records.** Functional and atomic records combine prose documentation with symbolic pseudo-code or examples and explicit tool lists. The example `skillx_db/appworld/vanilla-iter3/func_atomic_skills.json` records generated skill objects with `filter_result` and `embedding_text` fields, showing the retained skill format used by the library ([skillx_db/appworld/vanilla-iter3/func_atomic_skills.json](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/skillx_db/appworld/vanilla-iter3/func_atomic_skills.json)). At consumption time, these are system-definition artifacts only through the prompt path: they guide tool use but are not executed as library functions.

**Filtering, clustering, and merge records.** Filter results, embedding text, cluster groupings, and merged skill outputs are derived views over candidate skills. They provide validation, ranking, and consolidation authority, but the inspected implementation does not retain a full provenance graph from a merged skill back to every source trajectory in the final `SkillLibrary` object.

**Embedding indices.** Retrieval and clustering both build embeddings over plan/skill text using a local HTTP embedding service. These vectors are behavior-shaping ranking artifacts while in memory; they are regenerated from the JSON library rather than stored as canonical durable memory ([inference/embedding_service.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/embedding_service.py), [clustering/embedding.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/embedding.py)).

**Promotion path.** SkillX promotes experience through: successful trajectory -> optional tool-output summary -> plan extraction -> functional/atomic skill extraction -> filtering -> embedding clustering -> LLM merge -> `SkillLibrary.merge(...)` -> checkpoint/final JSON -> prompt-time retrieval. This is a real trace-derived promotion path, but it has weaker lineage than Commonplace-style source reviews because accepted records do not preserve stable source ids, exact source spans, or explicit invalidation rules for changed tool schemas.

## Comparison with Our System

SkillX and Commonplace both treat prior agent work as material that should shape later behavior, but they promote different artifact shapes. SkillX compresses successful tool-agent trajectories into plans and reusable tool-use skills. Commonplace compresses source and operational evidence into typed Markdown notes, instructions, schemas, review records, and generated indexes. SkillX is stronger where the target is repeated tool use in benchmark environments; Commonplace is stronger where retained knowledge needs source-grounded claims, citation discipline, and reviewable lifecycle state.

The closest alignment is the raw-to-distilled boundary. SkillX does not ask later agents to read full trajectories by default. It filters successful traces, extracts reusable procedural records, and serves compact retrieved records. Commonplace similarly prefers promoted artifacts over raw logs, but Commonplace puts heavier weight on citations, type contracts, link semantics, validation, and replacement history.

The main divergence is governance. SkillX has quality filters, tool-schema filters, clustering, and merging, but many gates are LLM-mediated and the accepted skill can overwrite an existing same-name skill in `SkillLibrary.merge(...)`. Commonplace would need explicit lineage, replacement, invalidation, review status, and rollback before giving generated procedural records comparable authority.

The second divergence is read-back authority. SkillX pushes retrieved plans and skills into the receiving agent's prompt. Commonplace mostly relies on agents pulling files through `rg`, indexes, links, and skills. SkillX therefore tests an important context-engineering pattern: the context engine, not the acting agent, chooses relevant memory before the model call. The cost is that embedding/LLM relevance errors become hidden prompt-shaping decisions.

### Borrowable Ideas

**Three-level procedural memory.** Commonplace could distinguish task-level plans, reusable subroutines, and atomic tool constraints when documenting repeated KB operations. Ready for narrow workflows where repeated traces exist.

**Omission-based extraction.** SkillX's atomic extractor asks which tools appeared in successful traces but lack coverage. Commonplace could use the same idea for review gaps: which commands, link labels, or validation warnings appear in work logs but have no instruction or note coverage. Ready as a workshop analysis pattern.

**Filter before merge and optionally after merge.** The `filter_timing` switch is a useful lifecycle knob: reject bad candidates before consolidation, then recheck the merged artifact. Commonplace can borrow this for generated notes or skills. Ready where validators or review bundles produce actionable failures.

**Use retrieved plans as intermediate queries for skill retrieval.** The architecture of retrieving a similar plan, adapting it, and then retrieving skills against the plan is a good progressive narrowing pattern. Needs implementation cleanup in SkillX before direct borrowing, because the inspected `prepare_prompt()` call path passes `retrieved_plan=plan` while the rewriter API expects a `retrieved_plans` list of dictionaries.

**Do not borrow weak lineage for high-authority procedural memory.** SkillX's compact skill format is attractive, but Commonplace should retain exact source trajectories, source ids, and invalidation rules when promoting procedures from traces. Ready as a design constraint, not as a feature.

## Write side

**Write agency:** `manual` `automatic` — Operators choose inputs, settings, benchmark mode, output directory, epochs, and whether expansion is enabled, but the distinctive store changes are automatic: trajectory filtering, tool-output summarization, plan extraction, skill extraction, skill filtering, clustering, merging, library updates, checkpoint saves, and optional task expansion.

**Curation operations:** `consolidate` `dedup` `evolve` `promote` — Tool-output summarization and plan/skill distillation compact traces into shorter artifacts; DBSCAN groups similar skills before LLM merge; `SkillLibrary.merge(...)` can replace an existing same-name functional or atomic skill; filter results and successful extraction promote raw traces into reusable library entries. I did not find durable stale invalidation, decay, or synthesis across already stored memories beyond LLM-generated merged skill records.

### Trace-learning

**Trace source:** `trajectories` `tool-traces` `session-logs` — The qualifying traces are task histories with assistant/tool turns, tool calls, environment feedback, rewards, failed trajectories when available, and exploration trajectories in optional expansion mode.

**Extraction.** The extraction oracle is a pipeline of reward filtering, LLM plan extraction, LLM skill extraction, LLM quality filtering, tool-schema filtering, embedding similarity clustering, and LLM merging. Functional extraction uses successful trajectories and plan steps; atomic extraction collects tools used in a trajectory and asks for missing or updated tool-centric skills ([extraction/plan_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/plan_extractor.py), [extraction/skill_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/skill_extractor.py)).

**Learning scope:** `per-project` `cross-task` — The library is benchmark/domain scoped and output-directory scoped, but the retained plans and skills are meant to transfer across later tasks, base agents, and benchmark environments.

**Learning timing:** `offline` `staged` — The ordinary pipeline builds and saves libraries in batch epochs. Expansion can add new synthetic trajectories between epochs when configured, but the inspected inference service does not update the library during a live task prompt.

**Distilled form:** `prose` `symbolic` `parametric` — The durable distilled artifacts are prose plans/descriptions plus symbolic JSON/tool/pseudo-code records. Parametric embeddings are used for clustering and retrieval, but they are rebuilt access structures, not the canonical skill library.

**Survey placement.** SkillX belongs in the trace-to-readable-procedural-memory family. It strengthens the survey's distinction between raw trace retention and distilled behavior-shaping artifacts: raw trajectories are evidence, while accepted plans and skills are the durable operative memory that later prompts consume.

## Read-back

**Read-back:** `push` — Retained plans and skills reach the receiving agent because `SkillUsageService.prepare_prompt(...)` loads the library, retrieves relevant records, formats them, and returns a system prompt before the benchmark agent acts.

**Read-back signal:** `inferred / embedding` `inferred / judgment` — Plan and skill candidates are selected by embedding similarity over task, plan, or skill text; when an LLM selector is configured and candidates exceed `max_skills`, judgment further filters the retrieved skills. Tool allowlists can narrow candidates, but the distinctive instance selection is semantic retrieval.

**Faithfulness tested:** `no` — The repository contains benchmark adapters and metadata for retrieved/selected skills, but I did not find an implemented with/without-memory ablation, perturbation test, or post-action audit proving that pushed skills were faithfully used in a specific task.

**Direction edge case.** `SkillRetriever` exposes pull-style methods from the host's perspective, but the acting model receives the result as pushed prompt context. The model does not have to decide to search the library; the host service has already selected and injected the material.

**Selection, scope, and complexity.** Selection is bounded by `top_k` plan retrieval, `skills_per_step`, `max_skills`, tool filters, and similarity thresholds. Complexity is reduced relative to loading full trajectories, but selected skills still include full descriptions and content snippets. There is no persistent per-task budget optimizer beyond these top-k and maximum-count controls.

**Authority at consumption.** The prompt formatters present plans and skills as reference or guidance. AppWorld explicitly warns that skills are reference implementations rather than callable functions, BFCL says to follow provided tool specifications, and tau2-Bench frames skills as tool-use best practices ([inference/prompt_formatters.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/prompt_formatters.py)). That is instruction/advice authority, not hard execution authority.

**Other consumers.** Human operators can inspect JSON skill libraries, plan files, checkpoints, filter results, and example `skillx_db` artifacts. Pipeline components consume the same records for clustering, filtering, merging, export, and retrieval.

## Curiosity Pass

**The implementation is more file-backed than the "knowledge base" phrase suggests.** There is no database server or persistent vector index in the inspected code. The durable KB is JSON; retrieval-time embeddings are rebuilt in memory from that JSON.

**Plan rewriting looks architecturally important but call-path fragile.** `PlanRewriter.rewrite(...)` expects a `retrieved_plans` list of dictionaries, while `SkillUsageService.prepare_prompt(...)` calls it with `retrieved_plan=plan`. That makes the plan-rewrite path less verified than the retrieval-and-formatting path at this commit.

**Filtering can silently soften when schemas are missing.** `ToolSchemaFilter.filter(...)` returns true when no tool docs are available. That is pragmatic for heterogeneous benchmarks, but it means "passed filtering" does not always mean schema-grounded validation.

**Atomic skill omission is a useful measurable gap signal.** The missing-tool calculation is one of SkillX's clearest design ideas: coverage is not just "which skills did the LLM invent" but "which observed tools still lack retained guidance."

**The final skill library loses some provenance richness.** Extraction results and example files may carry `source`, `filter_result`, or `embedding_text`, but the normalized `SkillLibrary` schema centers the accepted skill fields and metadata. For high-authority use, source trajectory ids and merge ancestry would need to survive more explicitly.

## What to Watch

- Whether the plan-rewrite call path is fixed and benchmark-tested. If it works, SkillX becomes a stronger example of progressive retrieval through task -> plan -> skills.
- Whether accepted skills retain exact source trajectory ids, filter decisions, cluster ids, and merge ancestry in the final library. That determines whether generated procedural memory can be audited and invalidated.
- Whether filtering gains deterministic tool-call checks rather than LLM-only "correct" decisions. That would make procedural promotion safer to borrow.
- Whether retrieval stores reusable indices or calibrated thresholds across runs. That would change the storage-substrate classification from transient in-memory embeddings toward durable ranking artifacts.
- Whether evaluations add causal memory-use tests, such as no-skill, wrong-skill, retrieved-skill, and all-skill prompt variants. That would strengthen faithfulness claims for pushed read-back.

Relevant Notes:

- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: SkillX extracts durable plans and skills from successful agent trajectories.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: SkillX has an explicit prompt-time read-back path rather than passive storage.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the review separates JSON libraries, prose plans, symbolic tool records, transient embeddings, and raw trajectories.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: selected skills move from evidence to prompt instruction/routing authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: retrieved plans, skill records, filters, and prompt formatters shape future behavior through instruction, routing, validation, and ranking.
- [Codification](../../notes/definitions/codification.md) - applies: successful natural-language/tool traces are compressed into reusable symbolic/prose procedures.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) - applies: reward filters, LLM filters, schema checks, and benchmark outcomes have different verification strength.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - contrasts: SkillX uses semantic embedding/judgment signals when task-specific symbolic routing is not enough.
