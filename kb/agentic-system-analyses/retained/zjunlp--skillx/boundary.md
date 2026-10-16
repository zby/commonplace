---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SkillX's shipped skill-library construction, persistence, exploration and inference integration at commit b0047c848dbbcf019363d6d56eef8c558f69aefc."
run-id: AAS-2026-10-14-skillx-61e3fc8f9aa5-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: b0047c848dbbcf019363d6d56eef8c558f69aefc
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/zjunlp/SkillX
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/skillx-61e3fc8f9aa5/related-systems/zjunlp--SkillX
  revision: b0047c848dbbcf019363d6d56eef8c558f69aefc
  sha256: null
---

# SkillX boundary

## Boundary and evidence

This run analyses how SkillX constructs reusable skill libraries from agent experience, maintains and persists them, and prepares their later use in agent prompts. It covers the complete shipped repository, not only its extraction API. The target class is **memory/knowledge/context-engineering system**: its retained state comprises planning, functional and atomic skills, and its construction and consumption paths issue model calls. Its construction pipeline also supplies a builder or improvement plane, while its exploration workers supply narrower agent loops. These are included responsibilities, not separately frozen targets (SRC-1, `core/skill.py`, `pipeline.py`, `inference/skill_usage.py`, `expansion/env_worker.py`).

The source-native intent is explicit:

> **SkillX** is a fully automated framework that constructs a **reusable, plug-and-play skill knowledge base** for LLM agents from experience.
> --- `README.md`

The boundary includes trajectory loading and normalization; model-driven plan and skill extraction; quality and tool-schema filtering; embedding-based clustering and model-driven merging; library updates and JSON persistence; exploration, task synthesis and task-generation checkpointing; retrieval, selection, plan rewriting and prompt formatting; shipped benchmark-facing consumers; schema acquisition scripts; sample libraries; and retained experimental result artifacts. These inclusions follow shipped imports and callers, including the command-line branch in `pipeline.py`, the library factory in `inference/skill_usage.py`, and all three agent wrappers in `inference/benchmarks/` (SRC-1).

The initial trace reaches retained-state production and later consumption. The pipeline updates a `SkillLibrary`, saves per-epoch checkpoints and final results; the library implements save/load; the inference factory reloads it and constructs a retrieval service; benchmark wrappers call that service to prepare prompts (SRC-1, `pipeline.py`, `core/skill.py`, `inference/skill_usage.py`, `inference/benchmarks/appworld.py`, `inference/benchmarks/bfcl.py`, `inference/benchmarks/tau2bench.py`). This establishes shipped responsibilities, not successful execution or artifact-format compatibility across every path.

> checkpoint_path = checkpoint_dir / f"skill_library_epoch_{epoch}.json"
> skill_library.save(str(checkpoint_path))
> --- `pipeline.py`

> library = SkillLibrary.load(library_path)
> embedding_service = EmbeddingService(base_url=embedding_url)
> --- `inference/skill_usage.py`

Maintenance instructions are part of the target. The extraction prompt asks for modifications, additions or retention of existing skills; the pipeline separately filters, merges and updates library state. These prompt instructions are design evidence, not proof that model outputs obey them (SRC-1, `prompts/skill_prompts.py`, `prompts/registry.py`, `filtering/pipeline.py`, `pipeline.py`).

> You have three options: **[modify, add, keep]**
> - **modify**: revise an existing skill to make it more effective (e.g., improving documents). Only change `content` when necessary, and ensure the resulting skill remains broadly reusable/general-purpose.
> - **add**: introduce a new skill only when existing skills cannot support a critical step, in order to improve future performance.
> - **keep**: Preserve the skill unchanged when there are no clear issues.
> --- `prompts/skill_prompts.py`

**Whole-system** means all material shipped responsibilities are within scope. It does not mean the repository supplies a complete benchmark deployment. The inference wrappers prepare prompts but leave task execution unimplemented. The expansion workers do contain model/environment interaction loops and evaluator calls; those shipped loops remain included rather than being mistaken for external callers (SRC-1, `inference/benchmarks/appworld.py`, `inference/benchmarks/bfcl.py`, `inference/benchmarks/tau2bench.py`, `expansion/env_worker.py`, `expansion/env_explorer.py`).

> async def run(self, task: str) -> Dict:
>     """Run agent on a task."""
>     raise NotImplementedError("AppWorld execution requires environment integration")
> --- `inference/benchmarks/appworld.py`

External dependencies are outside this frozen source: model-provider implementations and live responses; the embedding server; benchmark environments, their tools, policies, simulators and evaluator internals; supplied environment clients and callbacks; and external data directories used by schema scripts. Their SkillX-side adapters and calls are included. The exclusion prevents conclusions about those dependencies' internal behavior, actual service availability, benchmark correctness or a runnable end-to-end deployment from this repository alone. Dependencies are visible in SRC-1, `llm/client.py`, `clustering/embedding.py`, `inference/embedding_service.py`, `expansion/env_worker.py`, `expansion/env_explorer.py`, `scripts/extract_appworld_schemas.py` and `scripts/load_bfcl_schemas.py`. No external dependency was separately acquired or executed.

The immutable evidence revision is **b0047c848dbbcf019363d6d56eef8c558f69aefc**, verified against the acquired checkout. The applicability cutoff is **2026-10-14**, the supplied run date, not an assertion about when every bundled artifact was generated. Overall evidence is **code-grounded**: source inspection supports executable structure; source-native documentation and prompts support intent. No new target execution or causal experiment was performed. README performance claims remain attributed reports, not established gains (SRC-1, `README.md`).

The repository also freezes historical result summaries under `exp_log/`. Initial inspection of one telecom SkillX result found configuration and reward records but an unknown producing commit. These artifacts are eligible evidence of recorded results under their own stated conditions; they do not establish that this reviewed implementation produced them or isolate SkillX's causal contribution (SRC-1, `exp_log/tau2-bench/skillx/2026-01-18T23_23_15.297811_telecom_llm_agent_Qwen3-32B_user_simulator_gpt-4.1-2025-04-14_test.json`).

> "info": {
>   "git_commit": "unknown",
>   "num_trials": 4,
>   "max_steps": 200,
>   "max_errors": 10,
>   "seed": 300,
> --- `exp_log/tau2-bench/skillx/2026-01-18T23_23_15.297811_telecom_llm_agent_Qwen3-32B_user_simulator_gpt-4.1-2025-04-14_test.json`

### Top-level coverage

Every top-level tracked file or directory is classified below. All rows refer to SRC-1. “Included” fixes functional scope, not a claim that every line has already been read. Initial inspection traced the principal production, maintenance, persistence and consumption paths and searched shipped Python callers and evaluation hooks. Available files awaiting deeper inspection are not access gaps. No material shipped path was inaccessible.

| Top-level path | Treatment | Material paths and role | Initial inspection and limit / conclusion prevented |
|---|---|---|---|
| `LICENSE` | Excluded from operational analysis | Licensing text | Deliberate non-operational exclusion; no licensing assessment. |
| `README.md` | Included | Intended system, skill hierarchy, usage and performance reports | Read completely; claims are doctrine/design or reported operation, not verified outcomes. |
| `__init__.py` | Included | Package identity and public data-model exports | Read completely; no deployment guarantee. |
| `assets/` | Included | `assets/overview.png`, source-native architectural illustration | Tree inspected; image not yet inspected. No image-specific conclusion is drawn. |
| `pipeline.py` | Included | `IterativeSkillPipeline`, `run_pipeline`, CLI branch, epoch update, checkpoint and final-output paths | Read completely; construction and expansion handoff traced, not executed. |
| `core/` | Included | `core/skill.py`, `core/trajectory.py`, `core/skill_schema.py`, exports | Skill state, merge, serialization and save/load read; trajectory/schema details remain for deeper inspection. |
| `data/` | Included | `data/loaders.py`, `data/exporters.py`, `data/schemas.py` | Loaders and exporters read; schema validation details not yet inspected. Includes import/export compatibility questions. |
| `preprocessing/` | Included | `preprocessing/trajectory_adapter.py`, benchmark normalization and reward extraction | Definitions searched; tau2-bench adapter read. Other adapter bodies not yet inspected. |
| `extraction/` | Included | `extraction/base.py`, `extraction/plan_extractor.py`, `extraction/skill_extractor.py`, `extraction/tool_summary.py`, `extraction/benchmarks/` | Pipeline consumers and definitions searched; functional extractor read; remaining extraction and summary branches await deeper inspection. |
| `filtering/` | Included | `filtering/pipeline.py`, `filtering/base.py`, `filtering/general_filter.py`, `filtering/tool_filter.py` | Two-stage admission flow read; filter implementations searched and remain in scope. |
| `clustering/` | Included | `clustering/dbscan.py`, `clustering/embedding.py`, `clustering/merger.py` | DBSCAN implementation and embedding-service use read; merger and embedding definitions searched. |
| `expansion/` | Included | `expansion/explorer.py`, `expansion/env_worker.py`, `expansion/env_explorer.py`, `expansion/task_manager.py`, `expansion/task_generator.py`, `expansion/base.py`, `expansion/strategies/` | Workers read; real explorer interaction and evaluator path read; task-manager synthesis, checkpoint/reload and trajectory conversion read; alternate strategies and generator paths searched, not yet fully inspected. |
| `inference/` | Included | `inference/skill_usage.py`, `inference/retriever.py`, `inference/embedding_service.py`, `inference/skill_selector.py`, `inference/plan_rewriter.py`, `inference/prompt_formatters.py`, `inference/base.py`, `inference/benchmarks/` | Usage service, formatters and all benchmark wrappers read; retriever index building and plan retrieval read; remaining retrieval/selection/rewrite details await deeper inspection. Includes shipped callers, not merely library APIs. |
| `llm/` | Included | `llm/client.py` and exports | Client configuration and provider construction read; retry/invocation bodies not yet inspected. Live provider behavior is external. |
| `prompts/` | Included | `prompts/registry.py`, `prompts/plan_prompts.py`, `prompts/skill_prompts.py`, `prompts/filter_prompts.py`, `prompts/merge_prompts.py`, `prompts/expansion_prompts.py` | Registry read; functional skill contract and update instructions read; other templates remain included for deeper inspection. |
| `config/` | Included | `config/settings.py`, `config/tool_schemas.py`, `config/schemas/appworld/`, `config/schemas/bfcl/`, `config/schemas/tau2bench/` | Settings and registry entry methods read; schema tree inspected. Individual tool schemas and registry initialization not yet fully inspected. Schemas are retained tool contracts, not implementations of those tools. |
| `scripts/` | Included | `scripts/extract_appworld_schemas.py`, `scripts/load_bfcl_schemas.py` | AppWorld acquisition script read; BFCL input and conversion paths read and output definitions searched. External acquisition directories are not frozen evidence. |
| `skillx_db/` | Included | `skillx_db/appworld/vanilla-iter1/`, `skillx_db/appworld/vanilla-iter2/`, `skillx_db/appworld/vanilla-iter3/`, each containing `func_atomic_skills.json` and `plan.json` | Iteration tree inspected; initial iter1 skill and plan entries read. Other entries are available, not yet inspected. Samples do not establish that every file is directly accepted by the unified library loader. |
| `exp_log/` | Included | `exp_log/tau2-bench/vanilla/` and `exp_log/tau2-bench/skillx/`, benchmark result JSONs | Tree inspected and one SkillX telecom summary sampled. Other summaries not yet inspected; no aggregate comparison or causal gain established. Evaluator implementation remains external. |
| `utils/` | Included | `utils/async_utils.py`, `utils/logging.py`, exports | Async batch processor read; logging not yet inspected. Operational support rather than retained knowledge. |

Tracked `__pycache__/` files within included directories are excluded as duplicate compiled artifacts. Their exclusion prevents bytecode-specific or Python-version compatibility conclusions; the authored Python paths remain included. Directory inventories and caller searches establish their location, not behavioral equivalence with the reviewed source.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/zjunlp/SkillX` | b0047c848dbbcf019363d6d56eef8c558f69aefc | implementation; doctrine/design; reported operation; observed run | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/skillx-61e3fc8f9aa5/related-systems/zjunlp--SkillX`. Implementation: tracked top-level tree, shipped Python callers and evaluator hooks; complete `pipeline.py`, `core/skill.py`, data loaders/exporters, usage service, prompt formatters, benchmark wrappers, environment workers, DBSCAN, settings and async processor; bounded reads of extraction, retrieval, real exploration, task checkpointing, tool registry and acquisition scripts. Doctrine/design: complete README and prompt registry, functional extraction/update contract, formatter instructions. Reported operation: README performance claims. Observed run: initial configuration/reward-summary sample from one bundled telecom result, plus initial shipped skill/plan artifact samples; no new execution, independent provenance verification or causal experiment. Coverage table distinguishes remaining available material. | Implementation: [pipeline](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/pipeline.py), [state and persistence](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/core/skill.py), [reload and prompt service](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/inference/skill_usage.py), [shipped inference consumer](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/inference/benchmarks/appworld.py), [exploration worker and evaluator call](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/expansion/env_worker.py). Doctrine/design and reported operation: [README](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/README.md); doctrine/design: [skill maintenance prompt](https://github.com/zjunlp/SkillX/blob/b0047c848dbbcf019363d6d56eef8c558f69aefc/prompts/skill_prompts.py). Observed artifact: `exp_log/tau2-bench/skillx/2026-01-18T23_23_15.297811_telecom_llm_agent_Qwen3-32B_user_simulator_gpt-4.1-2025-04-14_test.json`, `skillx_db/appworld/vanilla-iter1/func_atomic_skills.json`, `skillx_db/appworld/vanilla-iter1/plan.json`. | No inaccessible material shipped path. External providers, embedding server, benchmark hosts/evaluator internals and script acquisition directories are not acquired: their internals and end-to-end availability cannot be established. Benchmark wrapper execution stubs prevent treating prompt preparation as a complete inference deployment. Bundled result provenance does not tie the sampled run to this commit; samples and README reports do not establish reproducible or causal performance gains. Uninspected available files are initial-coverage limits, not access gaps or exclusions. |
