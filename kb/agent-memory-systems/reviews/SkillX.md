---
description: "SkillX review: trajectory-derived hierarchical skill KB with plan extraction, skill filtering/merging, expansion, and prompt-time retrieval"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# SkillX

SkillX, from `zjunlp/SkillX`, is a framework for constructing reusable skill knowledge bases for tool-using LLM agents. At the reviewed commit it implements an offline pipeline that loads agent trajectories, extracts planning, functional, and atomic skills, filters and merges candidates, saves checkpointed skill libraries, optionally expands coverage through exploration, and exposes inference-time retrieval/formatting services that inject selected plans and skills into benchmark prompts.

**Repository:** https://github.com/zjunlp/SkillX

**Reviewed commit:** [0137cb8c2f9e69d5cc499e562dea789b2c5a8e35](https://github.com/zjunlp/SkillX/commit/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35)

**Last checked:** 2026-06-02

## Core Ideas

**The core retained unit is a three-part skill library.** `SkillLibrary` stores task plans, functional skills, atomic skills, and embedding configuration; each functional or atomic skill has `name`, `document`, `content`, `tools`, and metadata fields, while planning skills map a task to a reusable step plan ([core/skill.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/skill.py), [core/skill_schema.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/core/skill_schema.py)). This is not a transcript store. The intended memory artifact is a compact, reusable representation distilled from prior execution.

**Construction starts from successful trajectories, with failures used more selectively.** `IterativeSkillPipeline.run()` filters trajectories by reward, summarizes long tool feedback, extracts plans from successful trajectories, prepares one shortest successful trajectory per task for skill extraction, and can add a failed trajectory for atomic extraction context ([pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/pipeline.py), [extraction/tool_summary.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/tool_summary.py)). The pipeline's default oracle is benchmark reward above `0.999`, not human review.

**The hierarchy separates task-level plans from reusable tool procedures.** `PlanExtractor` distills an interaction history into `# step` plans; `FunctionalSkillExtractor` extracts reusable multi-step procedures from plan steps; `AtomicSkillExtractor` detects tools used in a trajectory but missing from the existing skill library and extracts tool-centered usage examples ([extraction/plan_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/plan_extractor.py), [extraction/skill_extractor.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/extraction/skill_extractor.py)). That gives SkillX a stronger artifact structure than single-blob reflection memories.

**Quality control is mostly LLM-mediated, with some symbolic structure checks.** The two-stage filter runs a general LLM quality check for functional skills, then a tool-schema validation filter when schemas are available; clustering groups similar skills by embedding distance and merges clusters through another LLM prompt ([filtering/pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/filtering/pipeline.py), [filtering/base.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/filtering/base.py), [clustering/dbscan.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/dbscan.py), [clustering/merger.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/clustering/merger.py)). The schema exists, but most semantic validity depends on prompts and model judgment rather than deterministic proof.

**Context efficiency comes from distillation, retrieval, and prompt formatting.** The construction pipeline compresses verbose traces into plans and skills; the inference path builds plan and skill embedding indexes, retrieves top-k plans/skills above a similarity threshold, can LLM-select from candidates, and formats only selected artifacts into benchmark prompts ([inference/retriever.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/retriever.py), [inference/skill_selector.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/skill_selector.py), [inference/skill_usage.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/skill_usage.py), [inference/prompt_formatters.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/inference/prompt_formatters.py)). It is a prompt-time context assembler, not an always-load memory file.

**Expansion tries to make the library less seed-bound.** Optional expansion analyzes successful and failed trajectories for API coverage, guides exploration toward failed or unexplored APIs, synthesizes new tasks from exploration trajectories, and feeds those synthetic tasks back into later epochs ([pipeline.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/pipeline.py), [expansion/explorer.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/expansion/explorer.py), [expansion/task_manager.py](https://github.com/zjunlp/SkillX/blob/0137cb8c2f9e69d5cc499e562dea789b2c5a8e35/expansion/task_manager.py)). That makes the library a staged learning artifact rather than a one-pass extraction output.

## Artifact analysis

- **Storage substrate:** `in-memory` — JSON or JSONL files loaded by `TrajectoryLoader`, plus in-memory dictionaries during pipeline execution
- **Representational form:** `mixed` — Symbolic/prose interaction histories with roles, tool calls, user task, reward, task id, and metadata

**Trajectory records.** Storage substrate: JSON or JSONL files loaded by `TrajectoryLoader`, plus in-memory dictionaries during pipeline execution. Representational form: symbolic/prose interaction histories with roles, tool calls, user task, reward, task id, and metadata. Lineage: imported benchmark or exploration traces; long tool responses may be summarized into derived trace views before extraction. Behavioral authority: knowledge artifacts during construction, because they provide evidence for extraction; evaluation authority comes from reward filtering. They are not the prompt artifact consumed by future agents unless a host separately loads them.

**Planning skills.** Storage substrate: `SkillLibrary.planning`, checkpoint JSON under `output/checkpoints/`, and exported plan JSON when requested. Representational form: concise prose plans with symbolic `# step` markers. Lineage: LLM-distilled from successful trajectories, optionally combined across multiple plans for the same task. Behavioral authority: advisory system-definition artifacts when retrieved and inserted into an agent prompt as a reference plan; knowledge artifacts when inspected as examples of prior task structure.

**Functional skills.** Storage substrate: `SkillLibrary.functional` and exported skill/library JSON. Representational form: mixed prose documentation plus Python-like implementation snippets and a symbolic tool list. Lineage: LLM-extracted from successful trajectory segments and plan steps, then optionally filtered, clustered, merged, and updated across epochs. Behavioral authority: advisory system-definition artifacts when formatted into the system prompt; validation/ranking authority comes from filters, embeddings, and LLM selection. Their effective correctness is not guaranteed by code.

**Atomic skills.** Storage substrate: `SkillLibrary.atomic` and exported JSON. Representational form: tool-centered prose documentation, usage examples, and tool lists. Lineage: derived from tools observed in trajectories, especially tools missing from the current atomic library; failed trajectories can provide contrast for extraction. Behavioral authority: prompt advice for future tool use, especially in tau2-bench style settings. The merge logic drops atomic skills whose focal tool is already covered by functional skills, which gives functional skills precedence in the retained library.

**Embeddings, indexes, and retrieval metadata.** Storage substrate: in-memory NumPy arrays built by `SkillRetriever`, with model/index config retained in the library metadata. Representational form: distributed-parametric vectors plus symbolic result metadata such as similarity, matched query, and selected skill names. Lineage: derived from plan text and skill text through an OpenAI-compatible embedding service. Behavioral authority: ranking and routing system-definition artifacts because they decide which retained skills enter the prompt. Precision/recall is not verified from code.

**Prompt templates and formatters.** Storage substrate: Python prompt modules and formatter classes. Representational form: prescriptive prose templates plus symbolic output contracts. Lineage: authored framework code. Behavioral authority: system-definition artifacts with extraction, filtering, merging, selection, and final prompt-assembly force. These templates are higher-authority than the skills they generate because they define what counts as a valid retained skill.

**Expansion artifacts.** Storage substrate: generated task dictionaries, synthetic trajectory stubs, optional checkpoints, and exploration trajectories returned by environment workers. Representational form: mixed symbolic task metadata, prose task descriptions, confidence scores, action sequences, and traces. Lineage: derived from seed tasks, exploration prompts, environment rollouts, and summarization. Behavioral authority: construction-time learning inputs; they become future system-definition artifacts only after extraction/refinement promotes them into plans or skills.

The main promotion path is trace to compressed trace to plan/skill candidate to filtered/merged library item to retrieved prompt context. That crosses all four axes: storage moves from raw files or rollout dictionaries into library JSON; form moves from verbose trace to compact prose/symbolic artifacts and embeddings; lineage becomes derived and epoch-marked; authority rises from evidence to prompt-shaping instruction.

## Comparison with Our System

| Dimension | SkillX | Commonplace |
|---|---|---|
| Primary purpose | Build reusable tool-use skill libraries from agent trajectories | Maintain a typed methodology KB for future agents and maintainers |
| Main artifacts | Plans, functional skills, atomic skills, embeddings, checkpoints | Typed Markdown notes, reviews, source snapshots, instructions, ADRs, indexes |
| Learning loop | Reward-filtered trajectory distillation, LLM filtering, clustering, merging, expansion | Source-grounded writing, validation, semantic review, workshop-to-library promotion |
| Read-back | Embedding/LLM-selected plans and skills formatted into prompts | Mostly explicit pull through search, indexes, links, and skills, with instructions loaded where configured |
| Governance | Prompt rules, reward threshold, tool-schema checks, LLM filters, clustering | Collection contracts, schemas, deterministic validation, git history, semantic review |

SkillX is a clean example of trace-derived artifact learning: it does not ask the future agent to replay raw trajectories, and it does not update model weights. It distills successful experience into named, reusable, inspectable prompt artifacts, then retrieves a small subset for a new task. Commonplace shares the belief that behavior-shaping artifacts should be retained in readable form, but Commonplace gives those artifacts stronger source lineage, review state, validation, and rollback through Git.

The important divergence is the quality oracle. SkillX uses benchmark reward and LLM judges to decide what to extract, keep, merge, or filter. Commonplace normally treats semantic quality as reviewable and source-grounded, not only benchmark-success-derived. That difference matters because a task-successful trajectory can still produce overfit, stale, or misleading advice.

**Read-back:** `both` — The retrieval service is pull machinery internally, but from the receiving agent's perspective selected trajectory-derived plans and skills are pushed into the system prompt before action through `SkillUsageService.prepare_prompt()`

### Borrowable Ideas

**Separate plan memory from procedure memory.** Ready with adaptation. Commonplace could distinguish task-level run plans from reusable operational procedures when capturing review or validation experience, instead of forcing both into one lesson format.

**Use omission detection for low-level gaps.** Worth borrowing for tool and command coverage. SkillX's atomic path asks which tools were used but lack retained guidance. A Commonplace analogue could detect commands, validators, or source types that appear in successful work but lack instructions. Ready for reports; promotion into instructions should remain reviewed.

**Treat embeddings as routing artifacts, not knowledge.** Ready now as terminology. SkillX's embeddings are behavior-shaping because they choose which skills are loaded, but the readable skill text remains the review target. Commonplace should keep the same split if it adds semantic search layers.

**Cluster-before-merge for trace-derived lessons.** Needs a concrete high-volume trace source. SkillX's DBSCAN then LLM-merge pattern is a reasonable first pass when many candidate lessons are redundant. It should not replace source lineage or review, but it can reduce review load.

**Keep read-back formatters benchmark-specific.** Ready where consumers differ. SkillX's AppWorld, BFCL, and tau2-bench formatters show that the same retained artifact may need different prompt authority and wording by runtime. Commonplace could use that pattern for planner, writer, reviewer, and validator consumers.

**Do not borrow automatic authority escalation.** SkillX can take a trajectory-derived candidate through filtering and directly into prompt injection. For Commonplace methodology knowledge, trace-derived candidates should land in a workshop/source layer first, then be reviewed before they become instructions, validators, or high-authority notes.

## Trace-derived learning placement

**Trace source.** SkillX qualifies as trace-derived learning. The qualifying traces are agent interaction histories with user task, role/content messages, tool calls, tool responses, rewards, and metadata; expansion can add environment exploration trajectories and synthetic task stubs. The default extraction boundary is successful trajectories with reward above the configured threshold, with failed trajectories used for contrast in atomic extraction and expansion analysis.

**Extraction.** Extraction is staged and mostly LLM-mediated. Long tool feedback is summarized; successful trajectories become reusable plans; plan steps become functional skills; missing observed tools become atomic skills; filters reject low-quality or schema-invalid skills; DBSCAN clusters similar skill texts; an LLM merger consolidates redundant clusters. The oracle is a mixture of reward threshold, prompt compliance, tool schema availability, embedding similarity, and LLM judgment.

**Scope and timing.** The loop is offline and epoch-based. It can run one or more extraction epochs, checkpoint after each epoch, and optionally expand between epochs by exploring under-used or failure-prone API regions. The resulting library is benchmark/domain scoped rather than a universal model memory.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), SkillX belongs in the trajectory-run / symbolic-artifact learning family. It sits near ExpeL-style rule extraction and Agent-S-style experience summarization, but its distinctive contribution is the three-tier retained artifact structure: planning skills, functional skills, and atomic tool skills. It strengthens the survey claim that trace-derived learning should be classified by the promoted artifact and consumption path, not only by the fact that trajectories were used.

## Read-back placement

**Direction.** SkillX uses both pull and push. The host or service pulls from a skill library through retrieval APIs, but the selected artifacts are retained memory, not shipped baseline documentation, and they are pushed into the receiving agent's prompt before it acts.

**Targeting and signal.** The memory push is `instance`-targeted. Plans are retrieved by embedding similarity to the current task, and skills are retrieved by embedding similarity to the retrieved plan steps or directly to the task, so the primary signal is `inferred / embedding`. Available-tool filtering can narrow candidates by tool-name identifiers, and the optional `SkillSelector` can apply an LLM relevance `judgment` when the candidate set exceeds `max_skills`; precision, recall, and context dilution are not verified from code.

**Timing relative to action.** `prepare_prompt()` builds a system prompt before task execution. That makes selected plans and skills pre-action context, not after-action reflection.

**Selection, scope, and complexity.** Plan retrieval defaults to `top_k=3`; skill retrieval uses top-k per plan step or a larger task query pool before truncating or LLM-selecting. The implementation has fixed thresholds and maxima, but no token-budget accounting or source-freshness check. It reduces context volume, while the complexity of multi-skill snippets can still dilute the final prompt.

**Authority at consumption.** The formatted artifacts are advisory prompt context. The formatters explicitly say skills are references and tools must still follow actual API specs, so the authority is softer than a hard validator or executable controller. Even so, they are system-definition artifacts because they are placed into the system prompt and can change the next action.

**Faithfulness.** I did not find a code-grounded ablation or perturbation test that proves retrieved skills caused the reported behavior changes. The repo includes retrieval and formatting machinery, but effective use by the agent remains an empirical benchmark claim.

**Other consumers.** Humans can inspect exported JSON libraries, checkpoints, prompts, and source trajectories. Construction-time components consume the same artifacts as evaluation, filtering, ranking, and merge inputs.

## Curiosity Pass

**The README says "plug-and-play", but the strongest implementation surface is a service, not a turnkey agent.** `SkillUsageService` can prepare prompts, but end-to-end benchmark agents live mostly as interfaces and helpers. A host still has to wire the prompt into execution.

**There is a likely API mismatch in the plan rewriting path.** `SkillUsageService.prepare_prompt()` calls `self.rewriter.rewrite(task=task, retrieved_plan=plan)`, while `PlanRewriter.rewrite()` expects `retrieved_plans` as a list of dictionaries. The separate `PlanRewriteService` uses the expected shape. That makes the prompt-time rewrite path less reliable than the architecture suggests.

**The skill schema is readable but permissive.** It requires name, document, content, and tools, but does not encode source trajectory ids, success scores, prompt/model versions, or review state. That is enough for retrieval, not enough for strong invalidation.

**The system distinguishes functional and atomic skills, then partly collapses authority at read-back.** Once formatted into a prompt, both become advisory text. The hierarchy improves construction and retrieval, but the receiving model still sees prose/code examples, not typed executable capabilities.

**Expansion is conceptually important but operationally host-dependent.** The repository defines exploration and task synthesis machinery, but real usefulness depends on the environment worker, LLM backend, reward signal, and generated-task quality.

## What to Watch

- Whether the plan rewriting API mismatch is fixed; that determines whether pseudo-plan retrieval is a reliable part of prompt-time read-back.
- Whether skill records gain source trajectory ids, reward, model/prompt version, extraction epoch, and validation provenance; that would make stale or harmful skills easier to audit and retire.
- Whether filters move beyond LLM text judgments into executable replay or tool-call simulation; that would make functional skills more trustworthy as system-definition artifacts.
- Whether expansion artifacts are promoted only after real rollout success, not just task synthesis confidence; that determines whether expansion improves coverage or manufactures noise.
- Whether inference gains token budgets, diversity controls, and skill conflict handling; that would turn top-k retrieval into governed context assembly.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: SkillX distills reward-filtered agent trajectories into planning, functional, and atomic skill artifacts.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: SkillX learns from after-the-fact execution traces without updating model weights.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: SkillX requires separate treatment for raw trajectories, plans, functional skills, atomic skills, embeddings, filters, and prompt templates.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: SkillX implements a concrete read-back path from retained skills into prompt context.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - applies: SkillX's main design move is reducing raw traces into retrieved prompt snippets.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: trajectories and checkpoints start as evidence/reference surfaces before promotion.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: selected plans, selected skills, embeddings, filters, prompts, and formatters shape future agent behavior.
