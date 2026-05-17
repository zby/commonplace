---
description: "SkillX review: trajectory-derived plan, functional-skill, and atomic-skill KB construction with LLM extraction, filtering, merging, and partial inference support"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-04-27"
---

# SkillX

> Replaced 2026-05-16. See [SkillX](./SkillX.md) for the current review.

SkillX is a codebase from zjunlp for constructing reusable skill knowledge bases from agent trajectories. The inspected repository implements data models, loaders, LLM-based extractors, clustering/merging, filtering, exploration-guided task synthesis, and a small shipped AppWorld skill database. It is best read as a construction pipeline for skill artifacts rather than as a complete benchmark agent: the inference agents are stubs, the retriever is mostly placeholder logic, and the root `pipeline.py` is identical to `prompts/expansion_prompts.py`.

**Repository:** https://github.com/zjunlp/SkillX

**Reviewed commit:** eb30f8909cf4ba7dc2d94c5b236e6b522b26198c

**Commit URL:** https://github.com/zjunlp/SkillX/commit/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c

## Core Ideas

**The source trace is a benchmark task trajectory.** `Trajectory` stores task identity, user task, interaction steps, reward, metadata, assistant tool calls, and tool responses. Loaders accept JSON/JSONL traces and filter by reward, defaulting to `> 0.999`, so the construction path is explicitly success-gated before extraction. The code names SkillX throughout; there is no MemSkill module or package identity in the inspected checkout ([core/trajectory.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/core/trajectory.py), [data/loaders.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/data/loaders.py), [__init__.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/__init__.py)).

**The durable artifact is a three-part skill library.** `SkillLibrary` separates planning skills, functional skills, and atomic skills. Planning skills are task-to-plan strings; functional and atomic skills share a five-key object shape: `name`, `document`, `content`, `tools`, and `metadata`. The shipped `skillx_db/appworld/vanilla-iter*/` directories contain concrete AppWorld examples as `plan.json` plus `func_atomic_skills.json`, with code-like snippets and natural-language documents rather than executable package modules ([core/skill.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/core/skill.py), [skillx_db/appworld](https://github.com/zjunlp/SkillX/tree/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/skillx_db/appworld)).

**Plan extraction is a lossy distillation from successful interaction histories.** `PlanExtractor` prompts an LLM to turn a user task and task history into a `<plan>` block, while `PlanCombiner` merges multiple plans for the same task. The prompt instructs the model to omit exploration, debugging, and failed steps, and to preserve reusable subgoals plus key APIs. That makes the plan library closer to reusable workflow memory than raw replay memory ([extraction/plan_extractor.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/extraction/plan_extractor.py), [prompts/plan_prompts.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/prompts/plan_prompts.py)).

**Skill extraction is update-oriented, not append-only.** `FunctionalSkillExtractor` processes each extracted plan step against the successful trajectory and current skill library; `AtomicSkillExtractor` centers extraction on tools used in successful trajectories and can include a failed trajectory for contrast. Both prompts ask the LLM to choose `add`, `modify`, or `keep`, and the extractor updates its in-memory skill context as it goes, so the unit of learning is "revise the library" rather than "save this episode" ([extraction/skill_extractor.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/extraction/skill_extractor.py), [prompts/skill_prompts.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/prompts/skill_prompts.py)).

**Refinement is a stack of embedding clustering, LLM merging, and LLM filtering.** Extracted skills can be embedded, grouped by DBSCAN over cosine distance, merged by an LLM prompt, and filtered in two stages: a general quality filter and a tool-schema filter. The tool filter only runs meaningfully when schemas are supplied; otherwise skills can fall back to stage-one results. This gives SkillX a quality-control story, but the judges are mostly LLM prompts rather than replay or deterministic execution tests ([clustering/dbscan.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/clustering/dbscan.py), [clustering/merger.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/clustering/merger.py), [filtering/pipeline.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/filtering/pipeline.py), [filtering/base.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/filtering/base.py)).

**Expansion targets missing or failure-prone tools.** `ExperienceGuidedExplorer` compares APIs from successful and failed trajectories, treats failed-only or missing APIs as exploration targets, discourages already covered APIs, and can summarize exploration traces into new realistic tasks. This is the code-grounded version of the README's exploratory expansion claim, but it depends on an external `env_worker` and agent loop being supplied ([expansion/explorer.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/expansion/explorer.py), [expansion/task_generator.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/expansion/task_generator.py)).

**Consumption is less implemented than construction.** The retriever advertises embedding-based search, but `retrieve_plan(...)` currently returns the first plans with placeholder similarity `1.0`, and `retrieve_skills(...)` returns the first `top_k` skills. The benchmark agents raise `NotImplementedError`, and `PlanRewriter.rewrite(...)` returns the retrieved plan unchanged. The shipped code therefore demonstrates how to build and store the skill KB more concretely than how to plug it into a working agent ([inference/retriever.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/inference/retriever.py), [inference/benchmarks/appworld.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/inference/benchmarks/appworld.py), [inference/plan_rewriter.py](https://github.com/zjunlp/SkillX/blob/eb30f8909cf4ba7dc2d94c5b236e6b522b26198c/inference/plan_rewriter.py)).

## Comparison with Our System

| Dimension | SkillX | Commonplace |
|---|---|---|
| Primary substrate | JSON plans and skill objects with code-like snippets, documents, tools, metadata | Markdown notes, sources, reviews, ADRs, instructions, generated indexes |
| Source signal | Benchmark agent trajectories, rewards, successful/failed tool use, exploration rollouts | Human/agent-authored artifacts, source snapshots, reviews, validation signals |
| Distillation target | Prompt-injectable plans, functional subroutines, atomic tool usage guidance | Typed knowledge artifacts and stronger operational surfaces |
| Retrieval | Intended embedding retrieval; implemented retriever is placeholder | `rg`, indexes, frontmatter, authored links, reports |
| Verification | Reward filter plus LLM extraction, merging, and filtering; optional tool schemas | Structural validation, semantic review, source grounding, explicit links |
| Lifecycle | Iterative JSON directories and add/modify/keep extraction | Status, archival, validation, index regeneration, review workflows |

SkillX is closer to commonplace than systems that only keep vectorized episodes. It distinguishes artifact roles, compresses traces into reusable objects, and treats memory as a library that can be inspected and edited. Its plan/functional/atomic split is a real artifact contract: future agents are supposed to consume different surfaces depending on whether they need a workflow, a reusable subroutine, or tool-specific constraints.

Commonplace is stronger on provenance and maintenance. SkillX skill objects include metadata fields such as source tasks and extraction epoch, but the extractors mostly pass around raw dictionaries and the shipped JSON examples do not preserve a rich link back to the exact source trace, filter rationale, merge source, reviewer, or replay result. That makes the artifacts easy to inject but harder to audit.

The sharpest difference is activation. SkillX is designed for automatic prompt-time skill injection, but the inspected inference path has not caught up with the construction path. Commonplace has mature navigation and validation surfaces but less automatic "before action" activation. SkillX points at the missing middle: a KB artifact can be well structured and still need a robust retrieval/injection layer before it changes behavior reliably.

## Borrowable Ideas

**Separate plan, functional, and atomic memories.** Ready to borrow as vocabulary. Commonplace already separates notes, instructions, sources, and reviews; SkillX's split is useful for tool-agent KBs where a task plan, a reusable procedure, and a single-tool caution should not collapse into one memory type.

**Use add/modify/keep during extraction.** Ready for bounded review workflows. Asking an extractor to update a library rather than only append new memories is a useful guard against duplicate notes and stale guidance, provided provenance and review state are retained.

**Omission-based tool-skill extraction.** Worth borrowing for agent tool ecosystems. SkillX's atomic extractor looks for tools used in successful trajectories that are missing from the current library. The commonplace analogue would be "which commands, scripts, or APIs are repeatedly used successfully but have no instruction note?"

**Two-stage skill filtering.** Borrow the shape, not the exact oracle. A general quality screen followed by schema-aware validation is a good pipeline. Commonplace should prefer deterministic checks where available, then use LLM judgment for semantic criteria the schema cannot express.

**Experience-guided exploration from failure coverage.** Needs a concrete workshop. The explorer's failed-only and under-covered API targeting is a promising way to generate tasks that fill KB gaps, but it requires a real environment worker and clear evaluator.

**Do not borrow placeholder retrieval.** SkillX's construction-side artifact schema is more mature than its consumer-side retrieval implementation. Commonplace should not treat "embedding retrieval planned" as an implemented design until there is an index, ranking policy, provenance display, and evaluation loop.

## Trace-derived learning placement

**Trace source.** SkillX qualifies as trace-derived learning. The raw signal is benchmark task execution: user task, task history, assistant tool calls, tool responses, reward or `after_score`, and optional failed trajectories. The expansion path adds exploration rollouts from an environment worker, then summarizes those traces into candidate tasks.

**Extraction.** The extraction oracle is staged. Reward thresholding selects successful traces; `PlanExtractor` distills successful histories into step plans; `FunctionalSkillExtractor` turns plan steps plus successful trajectories into reusable skills; `AtomicSkillExtractor` extracts tool-centered skills and can use failed trajectories for contrast. DBSCAN and LLM merging consolidate similar skills, while LLM filters and optional tool schemas reject some low-quality skills.

**Representational form.** The distilled substrate is mixed prose and symbolic structure. Plans are natural-language step lists in JSON. Functional skills are code-like snippets plus documents and tool lists. Atomic skills are tool-centered usage documents and examples. The system does not update model weights.

**Behavioral authority.** The intended authority is system-definition-artifact use: plans and skills are meant to be injected into future agents and alter how they plan or call tools. In the inspected code, that authority is clearer in the artifact schema and shipped `skillx_db` than in the incomplete inference implementation.

**Scope.** Scope is benchmark and environment specific. The shipped database covers AppWorld iterations, and the code has benchmark-specific support for AppWorld, BFCL, and tau2-Bench. The artifacts are cross-task within a tool environment, not global conceptual knowledge.

**Timing.** Learning is offline or staged in iterations. Existing trajectories are loaded, filtered, distilled, merged, and exported; exploration can synthesize new tasks for a later epoch. There is no deploy-time online update path in the inference agents as shipped.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), SkillX belongs in the trajectory-to-symbolic/prose skill-library branch. It strengthens the claim that many high-leverage agent-memory systems learn by changing external artifacts rather than weights, and it splits the "skill" category into three levels: workflow plans, reusable subroutines, and atomic tool guidance. It also weakens any claim that a constructed skill KB automatically implies a complete agent memory system; the consumer path still has to be implemented and evaluated.

## Curiosity Pass

The README frames SkillX as an end-to-end automated framework, but the code at this commit is uneven. The construction components are concrete; the benchmark agents, plan rewriting, and embedding retrieval are mostly stubs or placeholders. The practical artifact to review is therefore the trajectory-to-skill-library machinery, not a full deployed agent.

The shipped `skillx_db` is more informative than the package surface. It shows the actual memory format and iteration outputs, including plans and many AppWorld skills, while the repository has no package manifest or dependency file and no obvious runnable top-level pipeline. There is also a root `pipeline.py` whose blob matches `prompts/expansion_prompts.py`, which looks like a mistaken or incomplete entrypoint.

The artifact schema is promising but under-proven on trust. Skills can say which tools they use, and filters can check quality or tool schemas, but there is no replay harness in this checkout that proves a skill still works after extraction, merge, or modification. For executable-looking snippets, that gap matters.

The strongest design move is not "skills" as a generic word; it is the explicit compression ladder from trajectory to plan to functional/atomic skill. That ladder gives the system multiple reuse granularities instead of forcing every remembered experience into either a raw episode or a single free-form reflection.

## What to Watch

- Whether a real end-to-end pipeline entrypoint replaces the duplicated root `pipeline.py`.
- Whether embedding retrieval and plan rewriting become implemented and evaluated rather than placeholder returns.
- Whether skill metadata starts preserving source trajectory IDs, filter decisions, merge sources, execution outcomes, and retirement state.
- Whether filters add deterministic replay or environment validation for code-like functional skills.
- Whether the AppWorld-only shipped database expands to BFCL and tau2-Bench with the same artifact contracts.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: SkillX is a trajectory-to-skill-library case with separate plan, functional, and atomic distilled artifacts.
- [AgentFly](./AgentFly.md) - compares-with: both distill benchmark runs into planner-facing artifacts, but AgentFly stores case examples while SkillX stores hierarchical skill objects.
- [OS-Copilot](./OS-Copilot.md) - compares-with: both promote task experience into reusable procedural memory, but OS-Copilot stores callable tools while SkillX stores prompt-injectable plans and code-like snippets.
- [ExpeL](./expel.md) - compares-with: both use trajectory-derived lessons, but ExpeL promotes reflective rules while SkillX promotes structured tool-use skills.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: SkillX has strong offline artifact learning but incomplete deploy-time activation in the inspected code.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: SkillX separates source traces, distilled artifacts, and intended retrieval/activation surfaces.
