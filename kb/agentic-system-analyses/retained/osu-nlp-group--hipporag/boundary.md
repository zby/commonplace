---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "HippoRAG's shipped document-memory system, Python drivers, MCP server and plugin at commit d5c8329422e0a0b834a15874545cb6a74b4f9b26."
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/OSU-NLP-Group/HippoRAG
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-hipporag/related-systems/OSU-NLP-Group--HippoRAG
  revision: d5c8329422e0a0b834a15874545cb6a74b4f9b26
  sha256: null
---

# HippoRAG boundary

## Boundary and evidence

The target is HippoRAG as shipped at the frozen commit: a document-memory system for indexing, retaining, retrieving and answering from passages. Intended use of this analysis is to explain its knowledge-state lifecycle and the model-mediated mechanisms that serve it. The target class is **memory/knowledge/context-engineering system**, not an enclosing general-purpose agent runtime. The boundary kind is **whole-system**: it includes the Python library, shipped experiment and example callers, optional MCP service, plugin configuration and agent-facing maintenance skills. These callers and instructions are part of the target rather than external merely because they invoke library or tool APIs. SRC-1: `README.md`, `main.py`, `examples/_shared.py`, `src/hipporag/mcp_server.py`, `plugins/hipporag/.claude-plugin/plugin.json`.

The classification is supported by both declared purpose and executable state flow:

> HippoRAG 2 is a memory framework for LLMs that recognizes and uses connections in new knowledge, mirroring a key function of human long-term memory.
> --- `README.md`

> self.chunk_embedding_store.insert_strings(chunk_texts)
> --- `src/hipporag/HippoRAG.py`

> self._openie_info = all_openie_info
> self._save_openie_state(all_openie_info)
> --- `src/hipporag/HippoRAG.py:499-594`

> retrieved_passages = query_solution.docs[:self.global_config.qa_top_k]
> --- `src/hipporag/HippoRAG.py`

> all_qa_results = [self.qa_llm.infer(qa_messages) for qa_messages in tqdm(all_qa_messages, desc="QA Reading")]
> --- `src/hipporag/HippoRAG.py`

The included functional loop starts with strings or provenance-bearing chunks, applies preprocessing, embeds passages, extracts entities and triples with model calls, and builds the retained graph and separate passage/entity/fact stores. It includes manifests and OpenIE provenance checks, graph and metadata reload, incremental indexing, deletion, retrieval preparation, fact filtering, graph search, dense fallback and passage-conditioned QA. Optional IRCoT reasoning/retrieval and the StandardRAG baseline remain inside the boundary. These are implementation paths, not evidence of a successful deployment. SRC-1: `src/hipporag/preprocessing.py`, `src/hipporag/HippoRAG.py`, `src/hipporag/StandardRAG.py`, `src/hipporag/embedding_store.py`, `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/rerank.py`.

The shipped consumers cover more than a single API invocation. `main.py` loads corpora and questions, indexes them and runs QA with gold labels. Examples exercise the same lifecycle; the shared integration caller closes an instance, opens another against retained state, consumes it, adds documents and deletes them. The MCP server owns a persistent instance and exposes index, delete, retrieval, QA and statistics tools. Its agent-facing instructions include document preparation, refresh and later use. SRC-1: `main.py`, `examples/_shared.py`, `tests/integration/_shared.py`, `src/hipporag/mcp_server.py`, `plugins/hipporag/skills/hipporag-memory/SKILL.md`, `plugins/hipporag/skills/index-folder/SKILL.md`.

> with HippoRAG(**kwargs) as reloaded_rag:
>     print(reloaded_rag.rag_qa(queries=QUERIES, gold_docs=GOLD_DOCS, gold_answers=ANSWERS)[-2:])
>     reloaded_rag.index(docs=EXTRA_DOCS)
> --- `tests/integration/_shared.py`

> - To **update** a changed source, first `delete` its `source_id`, then `index` the new passages. Otherwise the stale passages remain.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`

That skill's claims about call counts and retrieval costs are declared guidance, not automatically implementation facts. In particular, executable extraction has separate NER and triple-inference paths, and the retrieval path invokes a model-backed fact filter. Later analysis must distinguish these layers. SRC-1: `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/rerank.py`, `src/hipporag/HippoRAG.py`.

### Repository coverage

Every top-level tracked item is classified below. “Included” fixes functional scope; it does not claim every file has already been read. Initial inspection traced the material state-producing and state-consuming entry points. Inventory-only assets and implementation details still requiring focused reading are identified separately from unavailable evidence.

| Top-level tracked item | Scope and role | Initial inspection and limits |
| --- | --- | --- |
| `.claude-plugin/` | Included: `marketplace.json` discovers the shipped plugin. | Manifest inspected; no host installation observed. |
| `.gitignore` | Excluded: developer ignore policy. | Tree inventory only; no conclusion about repository hygiene. |
| `CONTRIBUTING.md` | Excluded: contributor process, not document-memory maintenance. | Tree inventory only; no conclusion about development governance. |
| `LICENSE` | Excluded: legal terms. | Tree inventory only; no licensing assessment. |
| `README.md` | Included: declared purpose, setup, index migration, server/plugin use, backend and evaluation guidance. | Read completely; reported performance remains an attributed claim. |
| `examples/` | Included: `_shared.py` and provider-specific `demo_*.py` callers. | Shared index-to-QA caller inspected; provider wrappers inventoried/searched, not all read in detail. |
| `images/` | Excluded: presentation diagrams and branding (`brain.png`, `hippo_brain.png`, `icon_hippo.png`, `intro.png`, `methodology.png`). | Inventory only; no inference from figures or plotted results. |
| `main.py` | Included: corpus/query loading, HippoRAG or StandardRAG selection, indexing, QA and gold-label evaluation. | Entire driver inspected; not treated as an external application. |
| `outputs/` | Included as shipped retained-data fixtures: two `musique/openie_results_ner_*.json` files. | Inventory and README description only; contents not yet inspected. Their presence supplies neither verified provenance nor observed successful operation at this revision. |
| `plugins/` | Included: `hipporag/.claude-plugin/plugin.json` launches MCP; `skills/hipporag-memory/SKILL.md` and `skills/index-folder/SKILL.md` guide admission, refresh, deletion and consumption. | Manifest and both skills read completely. Host compliance is not observed. |
| `pyproject.toml` | Included: dependencies, optional backends, package discovery and `hipporag-mcp` executable registration. | Read completely. |
| `reproduce/` | Included: README and `dataset/*` corpora/questions feeding `main.py`. | README and data inventory inspected; bulk dataset contents not yet inspected. No benchmark reproduction or dataset-quality conclusion. |
| `requirements.txt` | Included: dependency declaration alongside package metadata. | Inventoried, not yet inspected in detail; installed-environment consistency is not established. |
| `setup.py` | Included: package discovery, prompt-data packaging and MCP console entry point. | Read completely; successful packaging not observed. |
| `src/` | Included: `hipporag/HippoRAG.py`, `StandardRAG.py`, `mcp_server.py`, `preprocessing.py`, `embedding_store.py`; extraction, embedding/LLM adapters, vector stores, prompts, reranking, configuration/state helpers and evaluators. | Traced core index/delete/reload/retrieve/QA/IRCoT methods, MCP entry point and tool handlers, preprocessing, Parquet persistence, online extraction, reranking, triple prompt and retrieval/QA evaluators. Other templates, offline extractors, provider adapters, backend implementations and state-helper internals remain available for focused analysis, not access gaps. |
| `tests/` | Included as executable specifications: `test_*.py`, provider `integration/run_*.py`, `_shared.py` reload/update/delete caller and vector-store checks. | Shared lifecycle caller read; integration call sites searched and unit-test files inventoried. No tests executed and no pass-rate claim. |

### External dependencies and evidence limits

The source revision is **d5c8329422e0a0b834a15874545cb6a74b4f9b26**, verified against the acquired checkout. The applicability cutoff is **2026-10-16**, the supplied run date; it is not a claim that remote providers or plugin installations were inspected on that date. Overall evidence is **code-grounded**, with source-native doctrine/design distinguished from executable implementation. No execution trace or causal experiment has been supplied or generated.

Model weights, hosted inference/embedding services, external vector-store servers, third-party libraries and MCP/Claude Code client implementations are outside the frozen source. Their adapters and the shipped plugin launcher are included, but the external systems' internals and actual behavior are not attributed to HippoRAG. This prevents conclusions about provider reliability, actual answer quality, measured latency, cross-process deployment correctness and host compliance with the skills. Dependency declarations identify dependencies without freezing their deployed versions or service state. SRC-1: `pyproject.toml`, `setup.py`, `README.md`, `plugins/hipporag/.claude-plugin/plugin.json`.

The plugin launch specification references an unpinned Git installation. This run analyzes that specification at the reviewed commit, not whatever revision a later `uvx` invocation might resolve. Linked papers, external datasets, the legacy branch and live documentation are not additional sources. This prevents extrapolating the analysis to HippoRAG 1, paper-era revisions, or current remote installations. There is no known source-access failure in the acquired checkout; uninspected available files above are not access gaps. SRC-1: `README.md`, `plugins/hipporag/.claude-plugin/plugin.json`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/OSU-NLP-Group/HippoRAG` | d5c8329422e0a0b834a15874545cb6a74b4f9b26 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-hipporag/related-systems/OSU-NLP-Group--HippoRAG`. Implementation: `main.py`, `examples/_shared.py`, `tests/integration/_shared.py`, `src/hipporag/HippoRAG.py` lifecycle/retrieval/QA ranges, `src/hipporag/StandardRAG.py` mutation range, `src/hipporag/mcp_server.py`, `src/hipporag/preprocessing.py`, `src/hipporag/embedding_store.py` persistence range, `src/hipporag/information_extraction/openie_openai.py` NER/triples, `src/hipporag/rerank.py`, retrieval and QA evaluators, package/marketplace/plugin manifests. Doctrine/design: full README, both plugin skills, triple-extraction prompt, `reproduce/README.md`. Tracked tree and integration call sites inventoried/searched. | Implementation: [core lifecycle](https://github.com/OSU-NLP-Group/HippoRAG/blob/d5c8329422e0a0b834a15874545cb6a74b4f9b26/src/hipporag/HippoRAG.py), [server](https://github.com/OSU-NLP-Group/HippoRAG/blob/d5c8329422e0a0b834a15874545cb6a74b4f9b26/src/hipporag/mcp_server.py), [shipped reload caller](https://github.com/OSU-NLP-Group/HippoRAG/blob/d5c8329422e0a0b834a15874545cb6a74b4f9b26/tests/integration/_shared.py). Doctrine/design: [README](https://github.com/OSU-NLP-Group/HippoRAG/blob/d5c8329422e0a0b834a15874545cb6a74b4f9b26/README.md), [memory skill](https://github.com/OSU-NLP-Group/HippoRAG/blob/d5c8329422e0a0b834a15874545cb6a74b4f9b26/plugins/hipporag/skills/hipporag-memory/SKILL.md). | No known checkout access gap. Implementation supports source-level behavior, not successful execution. Doctrine/design supports attributed intent, not adherence or empirical performance. No registered observed-run or causal-experiment evidence; no conclusions about real deployment performance or comparative effectiveness. |
