---
description: "HippoRAG review: document-ingest memory framework using OpenIE triples, parquet embedding stores, igraph PageRank retrieval, and RAG QA"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# HippoRAG

HippoRAG, from OSU NLP Group, is a Python RAG and non-parametric memory framework for multi-hop question answering. At the reviewed commit it ingests caller-supplied documents, extracts named entities and triples with an LLM, persists passages/entities/facts as parquet embedding stores plus OpenIE JSON and an igraph graph, then retrieves passages by query-to-fact scoring, LLM fact filtering, dense passage scoring, and Personalized PageRank before optional QA generation.

**Repository:** https://github.com/OSU-NLP-Group/HippoRAG

**Reviewed commit:** [d437bfb1805278b81e20c82357ed3f7d90f14901](https://github.com/OSU-NLP-Group/HippoRAG/commit/d437bfb1805278b81e20c82357ed3f7d90f14901)

**Source directory:** `related-systems/OSU-NLP-Group--HippoRAG`

## Core Ideas

**The retained memory is built from documents, not interaction traces.** `index(docs)` embeds document chunks, runs OpenIE over missing chunks, saves extraction results when configured, extracts entity nodes and fact triples, embeds entities/facts, and builds a graph from fact edges, passage-to-entity edges, and synonymy edges ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/information_extraction/openie_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/information_extraction/openie_openai.py)). I did not find code that learns durable behavior-shaping artifacts from session logs, tool traces, event streams, or trajectories.

**Storage is local and model-specific.** Each `HippoRAG` instance writes under `save_dir/<llm>_<embedding>/`, with separate `chunk_embeddings`, `entity_embeddings`, and `fact_embeddings` parquet stores, a `graph.pickle`, and an OpenIE results JSON keyed by LLM name ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/embedding_store.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/embedding_store.py), [src/hipporag/utils/config_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/config_utils.py)).

**Retrieval is graph-mediated recognition, not only dense passage search.** For each query, HippoRAG embeds the query for facts and passages, scores fact embeddings, filters candidate facts with a DSPy-style LLM prompt, assigns weights to selected entity and passage nodes, then runs Personalized PageRank over the graph to rank passage nodes. If no facts survive filtering, it falls back to dense passage retrieval ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/rerank.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/rerank.py)).

**Context efficiency is top-k retrieval plus QA-time truncation.** The framework does not load the whole document store into the answer prompt. `retrieve` returns `retrieval_top_k` ranked passages by default, while `qa` feeds only `qa_top_k` retrieved passages into the RAG prompt. Complexity is controlled by fact filtering, graph diffusion, dense fallback, and passage limits rather than by review state or progressive disclosure metadata ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/utils/config_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/config_utils.py)).

**The public surface is a library and experiment runner, not an autonomous agent harness.** The README and demos show callers constructing `HippoRAG`, calling `index`, then explicitly calling `retrieve`, `rag_qa`, or evaluation scripts. There is no MCP server, provider hook, background session capture, or always-on prompt injector in the inspected code ([README.md](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/README.md), [demo.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/demo.py), [tests_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/tests_openai.py)).

**Quality evidence is benchmark and test oriented.** The repository includes dataset runners, retrieval/QA metrics, and tests for indexing, reload, incremental update, deletion, retrieval, and QA, but I did not find a governance layer that reviews extracted triples before they become retrieval state ([README.md](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/README.md), [tests_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/tests_openai.py), [src/hipporag/evaluation/retrieval_eval.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/evaluation/retrieval_eval.py), [src/hipporag/evaluation/qa_eval.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/evaluation/qa_eval.py)).

## Artifact analysis

- **Storage substrate:** `files` — The retained store is local filesystem state: parquet files for chunk/entity/fact embeddings, OpenIE JSON results, a pickled igraph graph, prompts/config in the repository, and experiment outputs under `outputs`.
- **Representational form:** `prose` `symbolic` `parametric` — Source passages and QA prompts are prose; hash ids, triples, graph nodes/edges, config values, retrieval metrics, and JSON/parquet schemas are symbolic; embeddings and LLM-mediated reranking outputs provide parametric selection state.
- **Lineage:** `authored` `imported` — Prompts, code, configs, and demos are authored; passages, OpenIE extractions, graph edges, embeddings, and evaluation results derive from imported document corpora and caller-supplied docs. I did not find trace-extracted retained artifacts.
- **Behavioral authority:** `knowledge` `routing` `ranking` `validation` — Retrieved passages and extracted facts advise QA as knowledge; query-to-fact and query-to-passage embedding instructions plus top-k settings route selection; dense scores, LLM fact filtering, graph weights, and PageRank rank retrieved documents; tests and evaluation metrics validate retrieval/QA behavior at the experiment level.

**Document chunks.** Input documents become hashed chunk records in the chunk embedding store, with prose content plus embeddings. They are the answerable knowledge source and the nodes eventually returned to the QA prompt ([src/hipporag/embedding_store.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/embedding_store.py), [src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)).

**OpenIE extractions and fact store.** The extraction path stores named entities and triples per chunk, then flattens triples into fact embeddings. These facts have ranking and routing authority during retrieval, but they are not exposed as reviewed claims with source spans or acceptance state ([src/hipporag/information_extraction/openie_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/information_extraction/openie_openai.py), [src/hipporag/utils/misc_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/misc_utils.py)).

**Graph state.** The igraph graph contains passage nodes, entity nodes, extracted fact edges, passage-to-entity edges, and synonymy edges derived by entity embedding nearest-neighbor search. It is a retrieval access structure rather than a human-facing knowledge graph, because its main consumption path is PageRank ranking for passages ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)).

**Prompt and config policies.** OpenIE prompts, QA templates, linking instructions, DSPy filter prompts, and `BaseConfig` values are authored system-definition artifacts. They decide extraction format, query embedding instructions, fact-filtering candidates, retrieval limits, graph damping, passage weighting, and QA context size ([src/hipporag/prompts/templates/triple_extraction.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/templates/triple_extraction.py), [src/hipporag/prompts/linking.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/linking.py), [src/hipporag/prompts/filter_default_prompt.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/filter_default_prompt.py), [src/hipporag/utils/config_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/config_utils.py)).

**Evaluation artifacts.** Retrieval and QA metrics are experiment evidence rather than runtime memory. They can validate a retrieval setup against gold documents and answers, but they do not promote or reject individual extracted facts during normal indexing ([src/hipporag/evaluation/retrieval_eval.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/evaluation/retrieval_eval.py), [src/hipporag/evaluation/qa_eval.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/evaluation/qa_eval.py)).

**Promotion path.** HippoRAG promotes imported prose documents into embeddings, OpenIE triples, entity/fact nodes, graph edges, and ranked passage contexts. The promotion path is optimized for retrieval quality, not for governance: extracted facts become ranking state without an explicit review gate, typed claim record, or invalidation lifecycle.

## Comparison with Our System

| Dimension | HippoRAG | Commonplace |
|---|---|---|
| Primary purpose | Multi-hop document retrieval and RAG QA | Agent-operated methodology KB with typed durable artifacts |
| Canonical memory | Imported documents plus extracted triples, embeddings, and graph state | Git-tracked notes, reviews, instructions, ADRs, sources, indexes, and validation reports |
| Write path | Library indexing over caller-supplied docs, OpenIE extraction, embedding, graph construction, delete/update tests | Human/agent-authored Markdown under collection contracts, validation, source discipline, and review gates |
| Read-back | Explicit `retrieve`/`rag_qa` calls returning top-k passages | Explicit pull via `rg`, indexes, links, skills, source snapshots, and generated reports |
| Governance | Retrieval/QA metrics and mechanical tests | Type schemas, collection routing, semantic review, validation, git diffs, and replacement lifecycle |

HippoRAG is stronger than Commonplace as a retrieval algorithm for associating facts across a document corpus. Its graph-and-PPR path gives an agent a compact set of likely supporting passages without requiring manually authored links or indexes. Commonplace is stronger where the retained artifact itself needs durable authority: HippoRAG's extracted triples and graph edges are not reviewed claims, while Commonplace artifacts carry type, status, source discipline, and validation.

The biggest design divergence is that HippoRAG treats extracted structure as an access layer over imported text. Commonplace treats structure as part of the governed library: links, type specs, tags, and indexes can become behavior-shaping artifacts with auditability. That makes HippoRAG attractive as a retrieval front door but insufficient as a replacement for Commonplace's promotion and review model.

### Borrowable Ideas

**Graph-mediated retrieval over source documents.** Ready as an experimental read-only layer. Commonplace could use extracted entities and graph diffusion to find candidate notes or sources, while keeping Markdown artifacts and validation as the authority source.

**Separate fact retrieval from passage retrieval.** Ready for search design. HippoRAG's query-to-fact selection followed by passage ranking is a useful pattern for multi-hop source discovery where the final context should still be original prose passages.

**Use generated triples as candidate routing state, not accepted claims.** Ready now as a governance rule. In Commonplace, automatically extracted triples should point reviewers toward related notes or sources; they should not become durable methodology claims without review.

**Keep retrieval evaluation separate from artifact promotion.** Ready now. HippoRAG shows that benchmark success can justify a retrieval path without justifying automatic promotion of extracted facts into authoritative KB artifacts.

**Do not borrow opaque deletion semantics.** HippoRAG deletes chunks and removes triples/entities only when no undeleted chunk still supports them, but it does not maintain a human-readable invalidation history. Commonplace should keep replacement archives and explicit stale/superseded state for durable claims.

## Write side

**Write agency:** `automatic` — Callers explicitly supply documents, but the store-changing work is automatic indexing: chunk hashing, embedding upserts, OpenIE extraction, fact/entity embedding, graph edge construction, synonymy edge construction, graph persistence, OpenIE JSON persistence, and document deletion.

**Curation operations:** `not-determinable` — I found automatic acquisition and access-structure construction, plus delete/update support, but not implemented consolidation, deduplication, in-place evolution, synthesis across existing memories, staleness invalidation, decay, or content salience promotion over already stored memory. Index and embedding rebuilds are retrieval upkeep rather than content curation.

## Read-back

**Read-back:** `pull` — Retained memory reaches a model or caller only when application code explicitly calls `retrieve`, `rag_qa`, `retrieve_dpr`, or `rag_qa_dpr`. The inspected code does not wire a provider hook, session-start load, event-triggered memory injection, or unsolicited agent-facing recall.

Pull retrieval is still substantial. `retrieve` prepares in-memory graph and embedding objects, embeds the query, scores facts, asks an LLM filter to keep relevant candidate triples, runs graph search when facts survive, and returns top-k passage texts. `rag_qa` then feeds the top `qa_top_k` passages into a QA prompt. A host application could push those retrieved passages into an agent, but that behavior would belong to the host, not to HippoRAG's deployed loop.

Effective context use is not proven by the structural code alone. The repository evaluates retrieval recall and answer exact-match/F1 against datasets, but I did not find a with/without test showing that a downstream autonomous agent faithfully uses retrieved HippoRAG context in future actions.

## Curiosity Pass

**"Memory" here mostly means non-parametric document memory.** The implementation resembles a strong document-ingest retrieval memory, not a system that learns from agent experience or maintains preferences, procedures, or task outcomes across sessions.

**The graph is an access structure, not a governed knowledge graph.** Triples influence ranking, but the final read-back surface is usually source passage text. That is a useful safety property: the answer prompt can still see original passages rather than only extracted triples.

**The LLM reranker is both powerful and hard to audit.** It can discard or keep facts based on a prompt, but the default path records only candidate facts before/after reranking, not a stable explanation or reviewer decision.

**Incremental indexing is practical but not full truth maintenance.** The tests exercise reload, adding new documents, and deleting documents. Deletion filters facts/entities still supported by undeleted chunks, but there is no durable invalidation record explaining why a fact disappeared.

**StandardRAG looks less production-ready than HippoRAG.** The `StandardRAG` constructor contains an `ipdb.set_trace()` call at the reviewed commit, so the main comparable implementation is the `HippoRAG` class rather than that baseline wrapper ([src/hipporag/StandardRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/StandardRAG.py)).

## What to Watch

- Whether the planned vector database integration lands; that would change the storage substrate from local files only to a database-backed retrieval layer.
- Whether extracted triples gain source spans, confidence, or reviewer state; that would make the graph more useful as auditable knowledge rather than only ranking state.
- Whether HippoRAG adds agent integrations or provider hooks that automatically inject retrieved passages into future calls; that would change the read-back verdict from pull-only.
- Whether incremental updates grow into explicit invalidation or contradiction handling; that would matter for long-lived corpora where extracted facts can become stale.
- Whether retrieval evaluation adds ablations for graph/PPR/fact-filtering decisions on user-defined corpora, not only benchmark datasets; that would clarify which parts of the memory path are worth borrowing.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: HippoRAG stores document memory and graph state, but read-back is explicit pull unless a host wraps it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: HippoRAG's passages, triples, graph, embeddings, prompts, and metrics carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved passages, extracted facts, and evaluation outputs mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, configs, embedding instructions, rerank filters, and retrieval limits configure future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: HippoRAG's central contribution is selecting a bounded set of source passages from a larger retained corpus.
