---
description: "Graphiti review: temporal context graph with episode provenance, LLM extraction, bi-temporal fact edges, graph backends, and pull-only retrieval"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-30"
---

# Graphiti

Graphiti, from Zep, is an open-source Python engine for building temporal context graphs for AI agents. Its central bet is that evolving agent memory should be stored as graph state: raw episodes become entity nodes, fact edges, temporal validity windows, provenance links, optional communities, embeddings, and search indexes. Compared with commonplace, it is the strongest database-backed counterexample in this review set because its useful properties depend on graph-native storage and queries rather than on reviewed, file-native artifacts.

**Repository:** https://github.com/getzep/graphiti

**Reviewed commit:** [34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6](https://github.com/getzep/graphiti/commit/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6)

**Last checked:** 2026-05-30

## Core Ideas

**Episodes are the source layer.** The public `Graphiti.add_episode()` API accepts an episode name, body, source description, source type, group partition, reference time, optional UUID, entity/edge type schemas, custom extraction instructions, and saga linkage ([graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py)). `EpisodicNode` stores source type, source description, raw content, `created_at`, `valid_at`, and the entity-edge UUIDs referenced by the episode ([nodes.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/nodes.py)). That makes episodes the raw knowledge artifacts and lineage anchors; derived graph objects point back through `MENTIONS` edges and edge `episodes` lists.

**Fact edges carry two time axes.** `EntityEdge` stores `created_at` as graph insertion time, `valid_at` and `invalid_at` as event-time validity, `reference_time` from the producing episode, and `expired_at` as the processing-time moment when an edge was invalidated ([edges.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/edges.py)). Range indexes cover episodic `valid_at` and edge `created_at`/`expired_at`/`valid_at`/`invalid_at`, so the temporal model is part of the stored graph schema, not just display metadata ([graph_queries.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graph_queries.py)).

**Contradiction handling invalidates rather than overwrites.** Edge extraction asks the LLM for relation triples and temporal bounds, then `resolve_extracted_edges()` searches for duplicate and contradiction candidates. `resolve_extracted_edge()` has the LLM classify duplicate and contradicted facts, extracts missing timestamps, sets `expired_at` when a new edge is itself no longer current, and calls `resolve_edge_contradictions()` to set older contradictory edges' `invalid_at` to the newer edge's `valid_at` ([edge_operations.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/edge_operations.py), [dedupe edge prompt](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/prompts/dedupe_edges.py)). Old facts remain inspectable as historical graph edges.

**The ingestion pipeline is LLM-driven and schema-constrained.** Node extraction builds entity-type context from optional Pydantic models, calls source-specific prompts for messages, JSON, or text, collapses exact duplicate extractions, then resolves candidates with embedding similarity and LLM deduplication ([node_operations.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/node_operations.py)). Edge extraction similarly constrains relation names by optional edge type signatures, validates that the LLM used known entity names, preserves episode attribution, and can extract typed edge attributes ([extract edge prompt](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/prompts/extract_edges.py)). The schemas are system-definition artifacts because they constrain extraction and storage behavior.

**Storage is pluggable graph infrastructure, with provider-specific compromises.** `GraphDriver` defines Neo4j, FalkorDB, Kuzu, and Neptune providers plus operation interfaces for node, edge, search, saga, and maintenance operations ([driver.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/driver/driver.py)). The package dependencies and extras mirror that backend split ([pyproject.toml](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/pyproject.toml)). Kuzu stores entity edges as intermediate `RelatesToNode_` nodes, while Neo4j/FalkorDB/Neptune use relationship properties, so the common data model is implemented through adapter-specific query code rather than one uniform substrate ([edges.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/edges.py)).

**Retrieval is hybrid graph search, but activation is pull-only.** `Graphiti.search()` returns relevant fact edges through BM25 plus embedding search, optionally reranked by node distance; `search_()` exposes configurable edge, node, episode, and community searches with BM25, cosine similarity, BFS, RRF, MMR, and cross-encoder options ([search.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search.py), [search config recipes](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_config_recipes.py)). Date filters can express `valid_at`, `invalid_at`, `created_at`, and `expired_at` constraints for point-in-time retrieval, but the basic search path does not automatically package a "facts true at T" query; callers must supply filters ([search_filters.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_filters.py), [search filter tests](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/tests/test_graphiti_mock.py)).

**The MCP server wraps ingestion and retrieval as agent tools.** The MCP service initializes Graphiti with configured LLM, embedder, and graph database clients, queues `add_memory` writes by `group_id` to avoid same-partition races, and exposes search, get, delete, clear, and status tools ([MCP server](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/graphiti_mcp_server.py), [queue service](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/services/queue_service.py)). This is an integration surface, not an activation mechanism: memory reaches an agent when the host or agent calls a search tool.

## Comparison with Our System

| Dimension | Graphiti | Commonplace |
|---|---|---|
| Primary substrate | Graph database with full-text, vector, temporal, and traversal indexes | Git-tracked Markdown, source snapshots, type specs, scripts, generated indexes |
| Raw source layer | Episodic nodes containing message/text/JSON events | Sources, logs, work artifacts, notes, review evidence |
| Derived memory | Entity nodes, fact edges, communities, embeddings, temporal windows | Typed notes, reviews, ADRs, instructions, reports, indexes |
| Lineage | Episode UUIDs, `MENTIONS` edges, edge `episodes`, reference time, ingestion time | Citations, source snapshots, git history, authored links, status/replacement lifecycle |
| Retrieval | BM25, embeddings, BFS, cross-encoder/MMR/RRF, date filters | `rg`, descriptions, curated indexes, authored links, validation/review commands |
| Authority | Extraction schemas, prompts, dedupe/invalidation logic, search configs, graph indexes | Collection contracts, type specs, AGENTS.md, skills, validators, reviewed prose |

Graphiti is stronger than commonplace for high-volume, evolving event streams where facts need queryable validity windows. Its event time versus ingestion time split is more expressive than git history: a backfilled episode can be ingested today while producing facts that became true in the past. Commonplace can record that distinction in prose, but Graphiti can index and query it as first-class graph state.

Commonplace is stronger where memory needs governance as a human-readable artifact. Graphiti preserves provenance to episodes and keeps old edges when facts change, but a derived edge is not a reviewed claim with a status, link contract, replacement note, or explicit retirement rationale. The LLM extraction and contradiction paths are operationally useful but epistemically thin: they create and invalidate knowledge artifacts without a review queue.

The systems also differ in where behavioral authority lives. In Graphiti, system-definition authority sits in prompts, schemas, graph adapter queries, search configs, embeddings, and invalidation rules. The resulting nodes and edges are knowledge artifacts when retrieved as context, but they also participate in ranking and invalidation once search and maintenance code consumes them. In commonplace, the strongest authority usually lives in explicit files: instructions, schemas, validators, and reviewed notes.

Graphiti's read-back direction verdict is pull-only from the agent's perspective. Search can retrieve highly structured temporal memory, and MCP makes that retrieval tool-friendly, but the repository does not implement a relevance-gated pre-action hook, automatic context injection policy, or faithfulness test showing that surfaced graph facts changed agent behavior.

## Borrowable Ideas

**Bi-temporal fact records.** Ready to borrow as a pattern for any future database-backed operational layer. `created_at`, `valid_at`, `invalid_at`, `expired_at`, and `reference_time` separate "when we learned this" from "when it was true" and "when the system marked it superseded."

**Invalidate instead of overwrite.** Useful for contradiction handling in notes and reviews. Commonplace should keep explicit supersession and replacement trails rather than silently editing old claims out of existence; Graphiti shows the database-native form of that pattern.

**Episode provenance as the raw trace contract.** Worth borrowing if we build session ingestion. Each derived fact should retain source episode pointers and reference time. For file-native commonplace, that likely means source snapshots plus explicit derived-from links, not graph edges.

**Schema-constrained extraction with fallback learned ontology.** Useful only with strong review. Graphiti's Pydantic entity/edge types are a practical constraint on LLM extraction, but automatic extraction should remain candidate memory until reviewed when it would affect durable doctrine.

**Graph search as a derived layer, not the primary KB.** Graphiti is evidence that graph infrastructure earns its cost for temporal facts and traversal. It is not evidence that authored methodology notes should move into opaque graph records; for commonplace, graph search would be a compiled/index layer over reviewed sources.

**Do not borrow automatic edge invalidation as epistemic authority.** Graphiti's LLM contradiction classifier can maintain a useful runtime graph, but a contradiction mark is not the same as a reviewed decision. In commonplace terms it should create a review candidate, not silently settle the claim.

## Trace-derived learning placement

**Trace source.** Graphiti qualifies as trace-derived learning when episodes are conversation turns, user interactions, JSON events, or text events. `EpisodeType` explicitly covers message, JSON, text, and fact triples; `add_episode()` stores each episode with a reference time and then derives graph memory from it ([nodes.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/nodes.py), [graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py)). Fact-triple episodes are an adjacent direct-fact import mode rather than the canonical trace-derived path; they still enter the same temporal graph machinery, but they start from already-structured symbolic input rather than raw traces.

**Extraction.** Extraction is LLM-heavy: node prompts identify entities, edge prompts extract fact triples and temporal bounds, dedupe prompts resolve entity identity and fact contradictions, and attribute prompts fill typed fields. Embedding similarity narrows candidates, but the oracle for many semantic decisions is the configured LLM client ([node operations](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/node_operations.py), [edge operations](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/edge_operations.py), [LLM client](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/llm_client/client.py)).

**Storage substrate.** Raw and derived state lives in the selected graph database: episodic nodes, entity nodes, entity edges, community nodes, provenance edges, embeddings, and full-text/vector/range indexes. LLM cache and telemetry are auxiliary; they are not the canonical memory substrate.

**Representational form.** Raw episodes are prose or structured JSON wrapped in symbolic graph records. Entity and edge schemas are symbolic. Entity summaries and edge facts are prose. Embeddings and vector scores are distributed-parametric retrieval state. The operative memory is mixed: prose facts become behavior-shaping only through symbolic graph fields, temporal filters, embeddings, and search/reranking code.

**Lineage.** Lineage is better than ordinary vector memory but weaker than reviewed file artifacts. Edges keep episode UUIDs, episodes keep raw content unless `store_raw_episode_content` is disabled, and `MENTIONS` links connect episodes to entities. The system does not store a full derivation package for each LLM judgment: extraction prompt version, model version, confidence, reviewer, or approval state are not durable per-fact fields.

**Behavioral authority.** Episodes are source knowledge artifacts. Entity nodes, fact edges, and communities advise later agents when retrieved. Extraction prompts, Pydantic schemas, adapter queries, date filters, graph indexes, dedupe prompts, invalidation code, and search configs are system-definition artifacts because they create, constrain, rank, invalidate, and select memory.

**Scope and timing.** Scope is primarily `group_id`/database partition, with optional saga sequencing for ordered episode streams. Timing is online or queue-backed: the MCP server queues episode ingestion by group, while the core API warns that web applications should process episode addition sequentially or through background tasks.

**Survey placement.** Graphiti belongs in the trace-to-temporal-knowledge-graph family. It strengthens the survey claim that trace-derived systems should preserve raw traces separately from distilled memory, and it adds a distinctive temporal-invalidation mechanism. It does not strengthen the stronger artifact-learning claim where traces become reviewed rules, skills, tests, validators, or prompt policies.

## Curiosity Pass

**The temporal story is real, but default read-back is less temporal than the model.** The code stores and indexes temporal fields and exposes date filters. The simplest `search()` call, however, passes an empty `SearchFilters()` unless the caller supplies one. A host that wants "what was true at T" needs to build that filter discipline itself.

**Graphiti is graph-first but still LLM-dependent at the hard semantic points.** The graph database stores the result, but entity extraction, dedupe, relation extraction, timestamp interpretation, attribute extraction, and contradiction classification all depend on model output quality.

**Provider abstraction has real surface area.** Kuzu's edge-as-node representation shows that "pluggable graph backend" is not free. The adapters preserve the API but change the physical representation and query implementation, which matters for debugging and performance.

**Communities are optional derived views.** Community detection uses label propagation over entity relationships and LLM summarization of clusters ([community operations](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/community_operations.py)). That is a useful grouping mechanism, but it is a generated view, not a curated index.

**MCP improves access, not governance.** The MCP server gives agents a convenient add/search/delete interface, but it does not add permission modeling, review, approval, or activation tests around the memory it exposes.

## What to Watch

- Whether Graphiti packages point-in-time search as a first-class API rather than a caller-authored `SearchFilters` pattern.
- Whether edge provenance gains extraction prompt/model/version, confidence, source offsets, and review state.
- Whether Zep or Graphiti adds governance around automatic contradiction invalidation, especially for high-stakes facts.
- Whether MCP clients build relevance-gated pre-action read-back over Graphiti search, which would shift the read-back classification from pull-only capability to engineered push activation.
- Whether community detection proves useful enough to justify its ingestion-time overhead outside dense enterprise graphs.
- Whether backend adapters converge on the same semantics for temporal filtering, vector search, and traversal as graph sizes grow.

## Bottom Line

Graphiti is a serious temporal graph memory engine, not a thin vector-store wrapper. Its strongest contribution is the combination of episodes as raw trace provenance, LLM extraction into typed entity/fact graph objects, bi-temporal edge invalidation, and hybrid graph search over pluggable graph backends. Commonplace should not copy its database substrate for authored methodology, but it should treat Graphiti as the boundary case where graph infrastructure is justified: evolving event streams with contradictions, temporal validity, and traversal-heavy retrieval.

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - contradicts: Graphiti is the explicit boundary case where graph database capabilities earn their infrastructure cost.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - frames: its family distinctions suggest placing Graphiti as trace-to-temporal-knowledge-graph, not trace-to-rule or trace-to-skill.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Graphiti extracts durable memory from traces but lacks review-grade signal quality and promotion controls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Graphiti's episodes, fact edges, embeddings, schemas, prompts, filters, and graph indexes need separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: episodes, retrieved facts, entity summaries, and communities advise later agents as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: schemas, prompts, search configs, adapter queries, and invalidation logic create, route, rank, or constrain memory.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - cautions: Graphiti stores and retrieves temporal memory, but the inspected repo does not implement push activation or behavior-change tests.
- [Graphiti temporal knowledge graph ingest](../../sources/graphiti-temporal-knowledge-graph.ingest.md) - derived-from: earlier source ingest that this code-grounded review verifies and narrows.
