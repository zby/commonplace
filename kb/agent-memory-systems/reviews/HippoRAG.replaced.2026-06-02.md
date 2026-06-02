---
description: "HippoRAG review: graph-augmented RAG library that turns corpus documents into OpenIE triples, embeddings, igraph state, and PPR retrieval activation"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# HippoRAG

> Replaced 2026-06-02. See [HippoRAG](./HippoRAG.md) for the current review.

HippoRAG, from OSU-NLP-Group, is a Python graph-augmented RAG and "memory" library for LLM question answering. The implemented system indexes source documents into hashed passages, LLM-extracted entities and RDF-style triples, entity/fact/passage embeddings, an `igraph` graph, and cached model calls; query time activates this retained corpus-derived state through fact retrieval, LLM fact filtering, dense passage scoring, and personalized PageRank. It is memory in the non-parametric retrieval sense, not an agent-work trace or self-improving instruction system.

**Repository:** https://github.com/OSU-NLP-Group/HippoRAG

**Reviewed commit:** [d437bfb1805278b81e20c82357ed3f7d90f14901](https://github.com/OSU-NLP-Group/HippoRAG/commit/d437bfb1805278b81e20c82357ed3f7d90f14901)

**Last checked:** 2026-05-16

## Core Ideas

**The persistent memory boundary is the model-pair working directory.** A `HippoRAG` instance derives `working_dir` from `save_dir`, LLM name, and embedding model name, then places graph and vector-store state under that directory while OpenIE results and LLM caches live under the broader `save_dir` ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/utils/config_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/config_utils.py)). The storage substrate is therefore local files: JSON OpenIE results, parquet embedding stores, `graph.pickle`, SQLite LLM caches, and in-memory retrieval objects rebuilt from those files.

**Source documents become several derived retained artifacts.** `index()` first inserts input documents into a chunk embedding store, computes missing OpenIE rows, merges NER entities and extracted triples into a JSON file, embeds entity nodes and fact strings, and constructs graph edges from facts, passage-to-entity links, and synonymy KNN results ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/embedding_store.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/embedding_store.py), [src/hipporag/utils/misc_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/misc_utils.py)). The lineage is mechanically recoverable at chunk hash level: passage text hashes to `chunk-*`, entity text hashes to `entity-*`, fact content hashes into the fact store, and OpenIE rows retain the source passage.

**OpenIE is the symbolic bridge between prose documents and graph retrieval.** The OpenIE implementation runs NER, then conditions triple extraction on the named-entity list, expecting JSON outputs that are filtered into triples ([src/hipporag/information_extraction/openie_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/information_extraction/openie_openai.py), [src/hipporag/prompts/templates/triple_extraction.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/templates/triple_extraction.py)). Representational form is mixed: source passages are prose knowledge artifacts, OpenIE rows and triples are symbolic derived knowledge artifacts, and embeddings are distributed-parametric indexes over passages, entities, and facts.

**The graph is a derived activation surface, not the source of truth.** `initialize_graph()` loads `graph.pickle` when present; `save_igraph()` persists the constructed `igraph`; `prepare_retrieval_objects()` reloads stores, checks graph node counts, rebuilds missing nodes, reloads OpenIE results, and reconstructs entity-to-chunk mappings when needed ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)). The graph has ranking authority at query time, but its lineage points back to documents, extracted triples, embeddings, and configuration thresholds rather than to human-reviewed claims.

**Query-time retrieval combines recognition, dense retrieval, and graph diffusion.** `retrieve()` embeds the query for fact and passage matching, scores stored facts by dot product, asks `DSPyFilter` to filter candidate facts with the LLM, assigns weights to fact entities and dense passage hits, then runs personalized PageRank over the graph to rank passages ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/rerank.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/rerank.py), [src/hipporag/prompts/linking.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/linking.py)). The behavior-shaping artifact at this stage is transient activation state: query embeddings, selected facts, node weights, and PPR scores.

**Incremental update and deletion are implemented, but governance is corpus-local.** The tests exercise indexing, graph loading, incremental indexing, and document deletion ([README.md](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/README.md), [tests_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/tests_openai.py)). `delete()` removes selected chunks, drops triples/entities only when they no longer appear in remaining chunks, rewrites OpenIE JSON, updates embedding stores, deletes graph vertices, and saves the graph ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)). There is no review status, claim-level invalidation, or promotion path into instructions.

## Comparison with Our System

| Dimension | HippoRAG | Commonplace |
|---|---|---|
| Primary purpose | Non-parametric corpus memory for retrieval and QA | Agent-operated methodology KB for durable knowledge and procedures |
| Storage substrate | JSON OpenIE results, parquet embedding stores, `igraph` pickle, SQLite LLM caches, runtime arrays | Git-tracked Markdown notes, sources, instructions, reviews, ADRs, schemas, generated indexes |
| Representational form | Mixed prose passages, symbolic triples/config/code, embeddings, graph topology, PPR scores | Mostly prose with structured frontmatter, links, schemas, scripts, and validation code |
| Lineage | Strong chunk/passages-to-derived-store lineage; weak semantic provenance for extracted triples beyond source passage and model cache | Source snapshots, commit-pinned reviews, authored links, frontmatter status, archive/replacement lifecycle |
| Activation | Query embeddings, LLM fact filtering, dense retrieval, graph node weighting, PPR ranking | `rg`, indexes, descriptions, authored links, skills, validation and review workflows |
| Behavioral authority | Ranking and answer-context authority for QA | Advice, instruction, validation, review, routing, and methodology governance authority |

HippoRAG and commonplace share the idea that memory is useful only when it activates later behavior. HippoRAG's activation is algorithmic: a question touches fact embeddings, entity nodes, passage nodes, and graph diffusion before it shapes the QA prompt. Commonplace's activation is agentic and textual: a later worker reads notes, instructions, indexes, and reviews before deciding what to do.

The most important difference is artifact authority. HippoRAG's source documents and OpenIE outputs are knowledge artifacts when inspected as evidence, but the decisive system-definition artifacts are embeddings, graph edges, reranker prompts, configuration thresholds, and PPR weights because they rank what context the LLM sees. Commonplace puts more authority in reviewable prose and symbolic contracts: notes, type specs, skills, validation scripts, and instruction files.

HippoRAG has stronger automatic associative retrieval over a document corpus. It can turn unstructured passages into a graph and use entity/fact links to recover multi-hop context without a maintainer authoring links. Commonplace has stronger governance: links are intentional, claims are reviewable, source citations are explicit, and lifecycle states can mark artifacts current, outdated, replaced, or invalid.

HippoRAG does not qualify as trace-derived learning in the current review sense. Its durable state is derived from indexed corpus documents, LLM extraction calls, embeddings, and graph construction. The code does not show learning from agent sessions, tool traces, repeated task trajectories, or feedback loops into durable lessons, instructions, policies, or rankers.

**Read-back:** pull — callers invoke query-time retrieval over the graph and stores; push integration is left to the host.

## Borrowable Ideas

**Treat query activation as a first-class artifact boundary.** Ready to borrow conceptually. HippoRAG cleanly separates retained corpus state from transient query-time activation: query embeddings, selected facts, node weights, and PPR scores matter because they decide which retained artifacts reach the answer prompt.

**Use derived graph state as an index, not as the canonical memory.** Ready now as a design rule. The graph can be regenerated from documents, OpenIE rows, embeddings, and config, so it should be governed as a compiled view rather than as primary evidence.

**Preserve source passages beside extracted structure.** Ready now. HippoRAG keeps original passage text in chunk stores and OpenIE rows, which is the minimum needed to audit extracted triples when they look suspicious.

**Borrow automatic link suggestion only with provenance.** Worth exploring for commonplace indexes. Entity/fact extraction and synonymy KNN could suggest candidate links, but promotion into authored KB links would need source evidence, confidence, and review status.

**Do not borrow opaque ranking as governance.** HippoRAG's ranking pipeline is appropriate for retrieval, but commonplace should not let embedding similarity or graph diffusion silently promote claims into durable authority.

## Takeaways

**HippoRAG is a strong corpus-memory system, not an agent-memory governance system.** It stores and activates indexed knowledge so a model can answer better, but it does not manage the lifecycle of agent lessons, instructions, or operational rules.

**The artifact stack is a useful decomposition.** Source documents, OpenIE JSON, embeddings, graph pickle, model caches, and query activation each have different substrates, forms, lineage, and authority. Calling all of them "memory" hides the important design choices.

**Lineage is practical but not epistemic.** Hash IDs and stored passages make it possible to trace a triple back to a chunk, but the system does not attach review judgments, extraction confidence beyond model metadata, contradiction handling, or retirement rules for individual facts.

**The graph is behaviorally authoritative even when it is derived.** At query time, graph topology and weights decide what context the LLM sees. That makes the graph a system-definition artifact despite being regenerated from knowledge artifacts.

**Continual indexing is different from trace-derived learning.** Incrementally adding and deleting documents changes the retained corpus memory, but it is not the same as distilling agent experience into reusable behavior-changing artifacts.

## Curiosity Pass

The strongest mechanism is the separation between fact recognition and graph diffusion. HippoRAG does not simply retrieve top passages; it first identifies candidate facts, lets an LLM filter them, maps their entities into the graph, blends dense passage scores, and then diffuses attention through PPR.

The implementation's weakest point for KB comparison is not retrieval quality; it is governance. Extracted triples can have large downstream ranking effects, but they are not typed claims with explicit source citations, review status, or invalidation rules.

The system's "memory" framing is accurate for non-parametric corpus retention, but it should not be conflated with agent memory. No inspected path turns prior agent actions or feedback into stronger future instructions.

## Open Questions

- How often do OpenIE extraction errors create high-authority graph paths that retrieve misleading passages?
- Should OpenIE rows store richer extraction metadata, confidence, prompt/model version, and source offsets for fact-level audit?
- Can incremental deletion leave stale synonymy or edge effects in long-lived graphs, especially when only some triples/entities are removed?
- Would a generated explanation of the PPR path help users audit why a passage was retrieved?
- Can the graph construction support document versioning, contradiction handling, and stale-fact retirement without rebuilding from scratch?
- Is LLM fact filtering stable enough to serve as a recognition-memory gate across model versions?

## What to Watch

- Whether HippoRAG adds provenance and confidence fields for individual extracted triples.
- Whether graph updates gain stronger invalidation and rebuild semantics for changed corpora.
- Whether retrieval explanations expose selected facts, linked entities, dense passage weights, and PPR contribution.
- Whether future versions learn rankers or extraction policies from user/agent feedback; that would change the trace-derived classification.
- Whether the package separates canonical corpus state from compiled graph/vector views more explicitly.

## Bottom Line

HippoRAG is best read as a graph-augmented non-parametric memory layer for RAG: corpus documents become extracted triples, embeddings, graph state, and query-time activation that decide which passages reach the LLM. Its lesson for commonplace is the value of separating source evidence, derived symbolic structure, distributed-parametric indexes, compiled graph views, and transient activation; its limitation is that these artifacts rank context without the review, lifecycle, and authority controls expected from a durable agent-operated KB.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: HippoRAG requires separating source passages, OpenIE triples, embeddings, graph pickle state, and query-time PPR activation by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: indexed passages and OpenIE rows serve as evidence and answer context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: embeddings, graph topology, reranker prompts, thresholds, and PPR weights carry ranking and context-selection authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - illustrates: HippoRAG's value comes from activation mechanisms over retained corpus state, not storage alone.
