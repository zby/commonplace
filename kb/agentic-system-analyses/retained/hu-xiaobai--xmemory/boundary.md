---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "xMemory's shipped memory construction, hierarchy maintenance, retrieval, answer consumption and evaluation at commit 1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608."
run-id: AAS-2026-10-15-xmemory-b9a2b9f58eda-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/hu-xiaobai/xMemory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/xmemory-b9a2b9f58eda/related-systems/hu-xiaobai--xMemory
  revision: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
  sha256: null
---

# xMemory boundary

## Boundary and evidence

This run analyses xMemory as a **memory/knowledge/context-engineering system**, not as a general agent runtime. Its intended use is retaining conversation information and retrieving it for later questions. The **whole-system** boundary includes the Python library and the shipped LoCoMo drivers: those drivers coordinate hierarchy maintenance, reload retained content and turn retrieved memories into model answers. Restricting the target to its public facade would omit material responsibilities shipped in this repository (SRC-1, `xMemory/__init__.py`, `src/api/facade.py`, `evaluation/locomo/add.py`, `evaluation/locomo/xMemory_search_framework.py`).

The classification is code-grounded. The facade delegates message ingestion, episode flushing, semantic completion and search to the memory system. Episode creation invokes a generator and saves its output; prompts define model-dependent extraction. These are memory operations serving subsequent model calls, not merely a static document collection (SRC-1, `src/api/facade.py`, `src/core/memory_system.py`, `src/generation/prompts.py`).

> def add_messages(self, user_id: str, messages: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
>         """Append messages to the memory buffer for a given user."""
>         return self._memory_system.add_messages(user_id, list(messages))
> --- `src/api/facade.py`

> You are an episodic memory generation expert. Please convert the following conversation into an episodic memory.
> --- `src/generation/prompts.py`

The included loop covers input formatting and admission, buffering and episode boundaries, episode and semantic generation, prediction/correction extraction, persistence and indexing, theme split/merge maintenance, graph export, baseline and adaptive retrieval, original-message hydration, answer generation and evaluation. This is a boundary declaration, not a finding that all these paths execute successfully. In particular, the construction driver explicitly coordinates themes and graph updates; these responsibilities are not assigned to an excluded host (SRC-1, `evaluation/locomo/add.py`, `src/core/memory_system.py`, `src/core/memory_hierarchy.py`).

> new_eps, new_sems = memory.fetch_incremental_batches(user_id)
>
>         result["stage"] = "updating_themes"
>         theme_info = memory.update_themes(user_id, new_sems)
> --- `evaluation/locomo/add.py`

The retrieval driver is likewise included, rather than treated as an external example. It reloads persisted hierarchy files and supplies retrieved content to its answer model (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).

> storage_root = Path(self.config.storage_path)
>         themes_path = storage_root / "themes" / f"{user_id}_themes.jsonl"
> --- `evaluation/locomo/xMemory_search_framework.py`

> memories = self.search(memory, user_id, question)
>                     self._hydrate_episode_results(memory, user_id, memories.get("episodic", []))
>                     self._hydrate_semantic_results(memories.get("semantic", []))
>                     response = self.answer(question, memories)
> --- `evaluation/locomo/xMemory_search_framework.py`

### Tracked top-level coverage

The tracked tree has six top-level entries. All functional shipped paths are included. “Not yet inspected” below describes initial inspection depth, not an access gap or a functional exclusion. Later jobs may inspect any file at the same pin under SRC-1.

| Top-level entry | Classification | Material paths, role and initial inspection | Exclusion or inspection limit |
|---|---|---|---|
| `LICENSE` | Excluded from functional analysis | Legal terms; tree presence inspected. | No conclusion about license obligations or redistribution rights. |
| `README.md` | Included | Inspected in full: declared purpose, construction/retrieval/evaluation commands and external links. | Its research-performance statements remain attributed claims, not observed results. |
| `environment.yml` | Included | Inspected dependency declarations: Python environment, model/data libraries and storage tooling. | Complete dependency compatibility and reproducibility not established; remaining package pins not yet inspected. |
| `xMemory/` | Included | `xMemory/__init__.py` inspected in full: exports the facade and configuration. | No excluded responsibility. |
| `src/` | Included | `src/api/facade.py` and `src/config.py` inspected in full; `src/core/memory_system.py` episode persistence, asynchronous semantic scheduling and hierarchy-update sections inspected; `src/core/memory_hierarchy.py` theme-maintenance orchestration and graph reload inspected; `src/core/lightweight_search_system.py` reload/search entry points searched. `src/core/boundary_detector.py`, `src/generation/episode_generator.py`, `src/generation/semantic_generator.py`, `src/generation/prediction_correction_engine.py`, `src/storage/episode_storage.py`, `src/storage/semantic_storage.py` searched for model calls and persistence entry points. `src/generation/prompts.py` inspected in full. `src/utils/__init__.py` inspected; model/embedding adapters searched. Included supporting `src/domain/`, `src/models/`, `src/infrastructure/`, `src/search/`, `src/services/`, remaining storage and utilities supply contracts, representations, repositories, indexes, scheduling, caching and providers. | Supporting module internals and alternative branches not yet exhaustively inspected. No inference of correctness, safety or complete branch coverage follows from initial inspection. No material functional path deliberately excluded. |
| `evaluation/` | Included | `evaluation/locomo/add.py` inspected in full for dataset admission, maintenance and closure. `evaluation/locomo/xMemory_search_framework.py` inspected at prompts, hierarchy reload, answer generation, adaptive-search entry, question processing, result persistence and CLI. `evaluation/locomo/evals.py` and `evaluation/locomo/generate_scores.py` inspected in full. `evaluation/locomo/analysis_category.py` and `evaluation/gexf_view.py` entry points searched. `evaluation/locomo/config.json`, `evaluation/dataset/locomo10.json` and `evaluation/locomo/metrics/` included as configuration, evaluation input and scoring support. | Dataset contents, metric internals, detailed adaptive branches and diagnostic internals not yet fully inspected. Their presence is not evidence of measured performance or a completed evaluation. |

All coverage statements refer to SRC-1 at the frozen commit. The inspected construction, persistence, maintenance, reload and answer-consumption paths establish the whole-system scope; the table does not claim a whole-repository line-by-line review.

### Dependencies, exclusions and evidence limits

External dependencies include model weights and inference libraries, embedding-provider services, Chroma and local filesystem storage. The source configuration names a Llama model, an embedding model and filesystem/vector backends; the utility export selects the local-model adapter, while the embedding adapter contains OpenAI/Azure client paths (SRC-1, `src/config.py`, `src/utils/__init__.py`, `src/utils/embedding_client.py`, `environment.yml`). Their external implementations, live service behavior and downloaded model artifacts are outside this frozen source. This prevents claims about provider reliability, model quality or exact reproducibility from repository text alone.

The paper, project website, linked upstream systems, external PerLTQA dataset and release-hosted prebuilt memories are not frozen sources. They are excluded even when linked by the README; this prevents verification of their contents, paper-wide results, upstream behavior and prebuilt-memory quality. The bundled LoCoMo input and shipped evaluation code remain included (SRC-1, `README.md`, `evaluation/locomo/evals.py`). No live host application outside this repository is included; the run cannot characterize deployment integration or autonomous agent behavior beyond the shipped memory/QA workflow.

The applicability cutoff is **2026-10-15**. The evidence is the acquired Git revision **1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608**, not a moving branch or the README's publication dates. No execution traces, completed result artifacts or causal experiments were supplied as frozen evidence. Source inspection supports implementation and declared design; it does not establish successful execution, benchmark gains or operational durability. Available files left for later inspection are not access failures.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/hu-xiaobai/xMemory` | 1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/xmemory-b9a2b9f58eda/related-systems/hu-xiaobai--xMemory`. Implementation: exported facade, configuration, construction driver, episode persistence/scheduling, theme/graph orchestration, hierarchy reload, adaptive entry, answer consumption and evaluation scripts; additional generator/storage/provider entry-point searches as listed above. Doctrine/design: README and shipped generation/answer prompts. Reported operation: README's experiment and hardware statements only. Listed paths record initial inspection, not an allowlist. | Implementation: [facade](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/src/api/facade.py), [construction](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/evaluation/locomo/add.py), [memory system](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/src/core/memory_system.py), [hierarchy](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/src/core/memory_hierarchy.py), [retrieval and reader](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/evaluation/locomo/xMemory_search_framework.py), [evaluation](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/evaluation/locomo/evals.py). Doctrine/design: [prompts](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/src/generation/prompts.py). Doctrine/design and reported operation: [README](https://github.com/hu-xiaobai/xMemory/blob/1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608/README.md). | No access gap in the inspected checkout. No registered observed-run or causal-experiment evidence: successful operation and performance gains remain unverified. External linked material, service internals, model artifacts and release memories are not captured; conclusions depending on them are outside scope. |
