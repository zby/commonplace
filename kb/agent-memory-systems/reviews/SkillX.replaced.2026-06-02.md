---
description: "Trajectory-derived skill KB builder that distills successful task runs into plan, functional, and atomic prompt artifacts with partial retrieval support"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# SkillX

SkillX is zjunlp's framework for constructing reusable skill knowledge bases for tool-using LLM agents from benchmark experience. The inspected code implements the construction side: load successful trajectories, extract plans and skills with LLM prompts, filter and merge them, save a hierarchical library, and optionally expand the trajectory pool through exploration. Its consumption path exists, but is thinner and less polished than the extraction pipeline.

**Repository:** https://github.com/zjunlp/SkillX

**Reviewed revision:** 0137cb8c2f9e69d5cc499e562dea789b2c5a8e35

**Commit URL:** https://github.com/zjunlp/SkillX/commit/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35

## Core Ideas

**Raw trajectories are source evidence, not the memory product.** SkillX accepts JSON/JSONL task histories with user task, assistant/tool turns, reward, and metadata; loaders and adapters normalize benchmark formats and the main pipeline filters to reward `> 0.999` before extraction. The raw retained artifact is a trajectory knowledge artifact: it is evidence for what worked, but it is not what future agents are mainly supposed to consume ([core/trajectory.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/trajectory.py), [data/loaders.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/data/loaders.py), [preprocessing/trajectory_adapter.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/preprocessing/trajectory_adapter.py)).

**The durable library has three behavior-facing levels.** `SkillLibrary` separates `planning`, `functional`, and `atomic` stores. Planning skills map task text to stepwise plans. Functional and atomic skills share `name`, `document`, `content`, `tools`, and metadata; functional skills are multi-step code-like subroutines, while atomic skills are tool-centered usage guidance and examples. The shipped AppWorld library shows this as JSON plans plus `func_atomic_skills.json` examples, not Python modules ([core/skill.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/skill.py), [skillx_db/appworld](https://github.com/zjunlp/SkillX/tree/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/skillx_db/appworld)).

**Extraction is an LLM-mediated distillation chain.** `PlanExtractor` turns a successful interaction history into a `<plan>` block and `PlanCombiner` can merge multiple plans for one task. `FunctionalSkillExtractor` then extracts a reusable skill for each plan step, while `AtomicSkillExtractor` centers extraction on tools used in the trajectory. The hybrid extractor runs functional extraction first, detects tools used but not covered by functional skills, then emits atomic skills for those omissions unless configured to extract atomic skills for all tools ([extraction/plan_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/plan_extractor.py), [extraction/skill_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/skill_extractor.py), [prompts/skill_prompts.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/prompts/skill_prompts.py)).

**Refinement artifacts are operational, but mostly not retained as audit objects.** The pipeline summarizes long tool responses, extracts skills, runs optional pre/post filtering, embeds skills for DBSCAN clustering, merges clusters through another LLM prompt, and overwrites or appends skills in the library. These stages create judgments and intermediate groupings, but the final `SkillLibrary` mostly retains the distilled artifact and coarse metadata such as extraction epoch; it does not preserve a rich filter rationale, merge proof, or exact source-span lineage ([pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/pipeline.py), [filtering/pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/filtering/pipeline.py), [clustering/dbscan.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/dbscan.py), [clustering/merger.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/merger.py)).

**Filtering is prompt-based quality control, not replay validation.** The general filter asks an LLM to classify a skill as good or bad based on domain specificity, over-wrapping, imports, hard-coded parameters, and return-style code. The tool-schema filter asks another LLM whether invocations match available tool specifications. If no schemas are available, Stage 2 can effectively fall back, so the implemented oracle is weaker than an execution test even though it is useful as a sanity check ([filtering/base.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/filtering/base.py), [prompts/filter_prompts.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/prompts/filter_prompts.py)).

**Expansion is implemented as a hook around missing and failed tool coverage.** `ExperienceGuidedExplorer` compares successful and failed trajectories, identifies failed-only or missing APIs, discourages already successful/covered APIs, and can summarize exploration traces into new tasks. The main pipeline supports this after each epoch, but it requires a supplied environment worker or task manager; SkillX is not a standalone rollout system by itself ([expansion/explorer.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/expansion/explorer.py), [expansion/task_generator.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/expansion/task_generator.py), [expansion/task_manager.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/expansion/task_manager.py)).

**Retrieval and inference are present but uneven.** `SkillRetriever` builds embeddings for plans and skills and can retrieve by task, plan step, skill type, and available tools. `SkillUsageService` formats selected plans and skills into benchmark-specific prompts, making the distilled library a system-definition artifact when injected. But this path has rough edges: embeddings depend on an external HTTP service with zero-vector fallback, and `prepare_prompt` calls `PlanRewriter.rewrite` with a mismatched `retrieved_plan` keyword even though the rewriter expects `retrieved_plans`. The implemented construction path is therefore more reliable than the activation path ([inference/retriever.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/retriever.py), [inference/embedding_service.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/embedding_service.py), [inference/skill_usage.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/skill_usage.py), [inference/plan_rewriter.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/plan_rewriter.py)).

## Comparison with Our System

| Dimension | SkillX | Commonplace |
|---|---|---|
| Source signal | Successful and failed tool-agent trajectories | Authored notes, reviews, sources, instructions, and work artifacts |
| Primary retained artifact | JSON skill library: plans, functional skills, atomic skills | Markdown knowledge artifacts with type contracts, links, status, and validation |
| Representational form | Mixed prose and symbolic/code-like snippets; embeddings for retrieval | Mostly prose and structured frontmatter, with scripts for validation/indexing |
| Lineage | Source tasks and epochs in metadata; weak source-span and merge lineage | Git history, source links, review bundles, explicit supersession |
| Behavioral authority | Prompt injection and plan/skill guidance for acting agents | Advisory notes, prescriptive instructions, validation-enforced structure |
| Activation | Embedding retrieval plus LLM selection/formatting, partially implemented | Human/agent navigation through indexes, links, `rg`, and skills |
| Evaluation | Reward-gated source traces plus prompt filters | Validation commands, review system, human judgment, semantic checks |

SkillX and commonplace share the belief that memory should become an inspectable artifact rather than remain as raw episode replay. SkillX is more aggressive about trace-derived distillation: a successful benchmark run can become a plan, a functional subroutine, or atomic tool guidance with no human editor in the loop. Commonplace is more conservative: it preserves provenance and review state better, but it does not yet have a comparable automated trajectory-to-artifact promotion path.

The largest design divergence is behavioral authority. SkillX artifacts are designed to be injected into the acting agent's prompt before or during task execution, so they can directly shape tool use. In commonplace, most notes are knowledge artifacts until a maintainer promotes a procedure into an instruction, skill, validation rule, or CLI command. SkillX collapses that promotion distance for benchmark tool agents; commonplace keeps it explicit because its domain has softer verification.

The second divergence is lifecycle. SkillX can add, modify, keep, cluster, merge, filter, and overwrite skills, but the final artifact does not explain why a merge happened, which traces were invalidated, or when a skill should retire. Commonplace's status and link model is heavier, but it is better suited to long-lived review and maintenance.

**Read-back:** push — retrieved plans and skills are formatted into the acting agent's prompt before task execution.

## Borrowable Ideas

**Plan, functional, and atomic levels as separate artifact contracts.** Ready to borrow for tool-agent KBs. A task workflow, reusable multi-step procedure, and one-tool caution have different retrieval and authority needs; forcing them into one note type loses useful structure.

**Omission-based atomic skill extraction.** Ready as a design pattern, not necessarily as code. SkillX asks which tools appear in successful traces but are not covered by functional skills. A commonplace analogue would ask which commands, APIs, or note operations repeatedly succeed without a corresponding instruction or reference entry.

**Prompt filters as cheap pre-review gates.** Useful but should stay subordinate to stronger checks. SkillX's general and tool-schema filters are inexpensive ways to reject obvious garbage before a human or replay test sees it. For commonplace, that maps to review-bundle findings and deterministic validators rather than replacing them.

**Keep activation separate from construction.** SkillX shows the cost of building a good library before the consumer path is equally mature. Commonplace should treat retrieval/injection as its own artifact contract with evaluation, not as an automatic consequence of having good notes.

**Record merge and filter lineage if borrowing the pipeline.** SkillX's extraction/refinement stages are powerful, but their judgments mostly disappear into the final library. If commonplace adopts trace-derived skill construction, the merge source, filter result, source traces, and invalidation rule should be retained or reproducibly regenerated.

## Trace-derived learning placement

**Trace source.** SkillX qualifies as trace-derived learning. The raw signal is benchmark task trajectories: user task, task history, assistant actions, tool calls, tool responses, reward/after-score, metadata, and optional failed trajectories for contrast. Expansion can add exploration trajectories synthesized through an environment worker or task manager.

**Extraction.** The main extraction chain success-filters trajectories, summarizes long tool outputs, extracts plans from successful histories, extracts functional skills from plan steps, detects missing tools, extracts atomic skills for uncovered tools, filters the proposed skills, clusters near-duplicates, and LLM-merges clusters. The oracle is mixed: numeric task reward gates source traces, while most artifact quality judgments are LLM prompts.

**Storage substrate.** Raw trajectories are input JSON/JSONL files and in-memory dictionaries. Distilled state persists as JSON skill libraries and checkpoints under the configured output directory, with shipped examples under `skillx_db/appworld`. Embedding state is computed by an HTTP embedding service and held in process arrays in the retriever rather than committed as a durable index in the reviewed code.

**Representational form.** Plans are prose instructions with API labels. Functional skills are mixed artifacts: natural-language documentation plus code-like symbolic snippets. Atomic skills are tool-centered prose/examples with symbolic tool calls. Embeddings are distributed-parametric retrieval aids, but the operative behavior-shaping content is the symbolic/prose skill object.

**Lineage.** Lineage runs from successful trajectory to plan, plan step to functional skill, uncovered tool to atomic skill, and similar skills to merged skill. Metadata records source tasks, extraction epoch, cluster id, and timestamps in the data model, but exact source-span evidence, filter rationale, merge rationale, and replay result are not first-class retained lineage.

**Behavioral authority.** Raw trajectories are knowledge artifacts: evidence for extraction and optional contrast. Plans, functional skills, and atomic skills become system-definition artifacts when `SkillUsageService` retrieves and formats them into system prompts, because they influence task planning, tool choice, and execution style. During review or debugging, the same JSON library can also be read as a knowledge artifact.

**Scope.** Scope is per benchmark/domain library: AppWorld, BFCL, and tau2-bench are the named targets. The README claims strong-to-weak and cross-environment transfer, but the implemented code stores benchmark-specific prompt formatters, schemas, adapters, and example libraries rather than a domain-neutral memory system.

**Timing.** Construction is offline or epoch-staged over collected trajectories. Expansion can run between epochs if external rollout machinery is supplied. Inference-time use is prompt-time retrieval and selection, not online learning during a live task.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), SkillX belongs in the trajectory-to-symbolic/prose skill-library branch. It strengthens the survey claim that high-value agent memory often changes external artifacts instead of weights, and it usefully splits "skill" memory into planning, functional, and atomic authority surfaces. It also weakens any simple claim that skill KB construction alone solves memory: activation and lifecycle remain separate hard problems.

## Curiosity Pass

**The README overstates end-to-end maturity.** The construction path is real and fairly detailed. The inference path is less ready: the plan rewrite call mismatch, external embedding dependency, and prompt-only selection mean SkillX should be reviewed primarily as a skill-KB builder, not as a complete memory-using agent.

**The three-level hierarchy is stronger than the artifact governance.** The plan/functional/atomic split is crisp, but the library does not retain enough evidence to audit a generated skill without returning to the source traces and prompts. That is acceptable for benchmark experimentation; it is thin for a long-lived operational KB.

**Functional skills are not exactly executable functions.** They are code-like prompt artifacts. The AppWorld formatter explicitly tells the agent the skill library provides reference implementations and that actual API documentation should still be verified. That makes them system-definition artifacts with advisory execution force, not callable tools.

**The most interesting atomic mechanism is omission detection.** Atomic extraction is not just "make one note per tool"; in hybrid mode it asks which tools were used in the trajectory but not covered by functional skills. That makes atomic skills a gap-filling layer rather than a parallel dump of every tool observation.

**The evaluation loop stops before downstream behavioral proof.** Reward gates successful source trajectories, but after extraction the filters judge artifact shape and tool-schema consistency. The reviewed code does not replay generated skills to prove that downstream agents improve because of each retained item.

## What to Watch

- Whether SkillX fixes the inference path so plan retrieval, rewriting, skill retrieval, and prompt formatting compose without interface mismatches.
- Whether future versions retain source-trace, filter, merge, and replay lineage alongside each skill.
- Whether filtering moves from LLM prompt judgment toward deterministic replay or benchmark ablation per retained skill.
- Whether the expansion hooks become a complete online exploration loop or remain adapters around external environment workers.
- Whether the hierarchy generalizes outside benchmark tool environments, where reward signals and schemas are weaker.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: SkillX is a trajectory-to-skill-library system with separate plan, functional, and atomic distilled artifacts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: SkillX makes storage substrate, representational form, lineage, and behavioral authority separable in the reviewed artifact.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: SkillX performs offline artifact learning and points toward prompt-time activation, but the deploy-time consumer path is not yet as mature as extraction.
- [Codification](../../notes/definitions/codification.md) - contextualizes: functional skills push trajectory lessons toward symbolic code-like procedures without making them fully callable tools.
- [SkillWeaver](./SkillWeaver.md) - compares-with: both distill trajectories into skill libraries, but SkillX stores prompt-facing plan/skill artifacts while SkillWeaver stores executable Playwright functions.
- [AgentFly](./AgentFly.md) - compares-with: both derive reusable artifacts from benchmark experience, but AgentFly is case/planner oriented while SkillX exposes a three-level skill hierarchy.
