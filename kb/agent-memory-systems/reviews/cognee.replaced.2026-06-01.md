---
description: "Cognee review: pipeline-first memory engine with add/cognify/memify/search flows, DataPoint schemas, poly-store backends, ACLs, and trace-to-graph improvement"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Cognee

> Replaced 2026-06-01. See [cognee](./cognee.md) for the current review.

Cognee, from topoteretes, is a Python memory and knowledge-graph engine for AI agents. Its core shape is a pipeline system: raw inputs are added to datasets, cognified into Pydantic-derived graph objects and summaries, stored across graph/vector/relational/cache substrates, then queried through search/recall surfaces. Compared with commonplace, Cognee is the strongest database-side counterexample in this collection: it treats memory as an operational data platform with pluggable stores, API/MCP surfaces, tenant-aware permissions, session cache, trace capture, and ranking weights rather than as reviewed files.

**Repository:** https://github.com/topoteretes/cognee

**Reviewed commit:** [4ca1d0c2bbbb46924acb1f5f6cd805214805ca16](https://github.com/topoteretes/cognee/commit/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16)

**Last checked:** 2026-05-16

## Core Ideas

**The public workflow is add, cognify, improve/memify, search/recall.** The package exports the older `add`, `cognify`, `memify`, and `search` API plus the newer memory-oriented `remember`, `recall`, `improve`, and `forget` surface from `cognee/__init__.py` ([package API](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/__init__.py)). `add()` resolves data, runs setup, authorizes or creates a dataset, and executes an ingestion pipeline that stores normalized text files and relational `Data` rows ([add API](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/add/add.py), [ingestion task](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/tasks/ingestion/ingest_data.py)). `cognify()` classifies documents, chunks them, extracts graph structure, summarizes chunks, persists nodes/edges/embeddings, and optionally runs temporal extraction ([cognify API](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/cognify/cognify.py)).

**Raw documents, extracted DataPoints, and pipeline definitions are different retained artifacts.** The relational `Data` model keeps source file locations, raw and normalized content hashes, loader engine, node set, owner, tenant, pipeline status, external metadata, and importance weight ([data model](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/data/models/Data.py)). The behavior-shaping graph objects inherit from `DataPoint`, which adds identity generation, embeddable-field metadata, ontology validity, source pipeline/task/user/node-set/content-hash fields, feedback weight, and importance weight ([DataPoint](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/infrastructure/engine/models/DataPoint.py)). The pipeline runner stamps DataPoints with source pipeline, task, user, node set, and content hash as they flow between tasks ([pipeline provenance](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/pipelines/operations/run_tasks_base.py)). That makes the raw file row a knowledge artifact, the pipeline task list a system-definition artifact, and the DataPoint/edge layer a mixed derived artifact with both evidence and ranking roles.

**Pydantic models are schema and extraction contract.** The default `KnowledgeGraph` model defines nodes and edges, while `cognify()` accepts a custom `graph_model` and the API can build one from a submitted graph schema ([shared graph model](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/shared/data_models.py), [cognify router](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/cognify/routers/get_cognify_router.py)). `extract_graph_from_data()` runs LLM extraction over chunks, filters invalid edges, resolves ontology configuration, and integrates extracted graphs into chunk DataPoints ([graph extraction](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/tasks/graph/extract_graph_from_data.py)). The schema is therefore not just documentation; it constrains what the LLM may produce and what downstream storage/search can index.

**Storage is deliberately poly-store.** The package ships graph adapters for Ladybug, Kuzu, Neo4j, Neptune, and Postgres; vector adapters for LanceDB, ChromaDB, and pgvector; a relational SQLAlchemy layer; cache adapters including Redis and filesystem cache; and a unified engine that chooses graph/vector/hybrid paths ([database adapters](https://github.com/topoteretes/cognee/tree/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/infrastructure/databases), [storage task](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/tasks/storage/add_data_points.py)). `add_data_points()` writes graph nodes and edges, indexes DataPoint fields into the vector engine, optionally embeds graph triplets, and mirrors nodes/edges into relational tables when user/dataset/data context exists. The store boundary is explicit but not human-inspectable in the way a markdown KB is.

**Search is a retriever registry plus graph/vector ranking.** `SearchType` includes chunks, summaries, RAG completion, graph completion variants, Cypher, natural language, temporal, coding rules, lexical chunks, and feeling-lucky routing ([search types](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/search/types/SearchType.py), [retriever factory](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/search/methods/get_search_type_retriever_instance.py)). Graph completion embeds the query, searches DataPoint and edge collections, projects a graph fragment, maps vector distances to graph nodes/edges, applies triplet distance and feedback influence, resolves selected edges to text, and optionally asks the LLM for a completion ([graph completion retriever](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/retrieval/graph_completion_retriever.py), [triplet search](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/retrieval/utils/brute_force_triplet_search.py)). Retrieved graph state is a knowledge artifact when shown as context, but vector distances, graph projection, feedback weights, prompts, and retriever selection carry system-definition authority over what reaches the model.

**Access control is relational and tenant-scoped.** Datasets, users, tenants, roles, principals, permissions, ACL rows, and dataset databases live in SQLAlchemy models; permission types are `read`, `write`, `delete`, and `share` ([ACL model](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/users/models/ACL.py), [tenant model](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/users/models/Tenant.py), [permission types](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/users/permissions/permission_types.py)). Search resolves readable datasets before querying and runs each search inside the selected dataset's database context ([search authorization](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/search/methods/search.py)). FastAPI exposes dataset permission, role, and tenant endpoints ([permissions router](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/permissions/routers/get_permissions_router.py)). This is more operationally serious than most reviewed systems, though the graph `Node` and `Edge` models show commented-out RLS policy stubs rather than database-enforced row-level security ([node model](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/graph/models/Node.py), [edge model](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/graph/models/Edge.py)).

**Agent surfaces are API, CLI, MCP, and decorators.** The FastAPI routers expose add/cognify/search/permissions; the CLI wraps the same workflow; the MCP server can run Cognee directly or through HTTP and exposes tool-style cognify/search/delete/graph operations ([add router](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/add/routers/get_add_router.py), [search router](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/search/routers/get_search_router.py), [MCP server](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee-mcp/src/server.py), [MCP client](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee-mcp/src/cognee_client.py)). The `@agent_memory` decorator can fetch relevant graph memory before an async agent function runs, optionally read recent session feedback, and persist a trace step after the call ([agent-memory decorator](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/agent_memory/decorator.py), [agent-memory runtime](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/agent_memory/runtime.py)).

## Comparison with Our System

| Dimension | Cognee | Commonplace |
|---|---|---|
| Primary artifact | Dataset records, DataPoints, graph edges, vector indexes, pipeline definitions, cache sessions | Typed markdown notes, sources, instructions, reviews, ADRs, schemas, generated indexes |
| Storage substrate | Relational DB plus graph DB plus vector DB plus cache; filesystem only for stored raw/normalized files | Git-tracked files plus generated reports/indexes |
| Representational form | Mixed prose documents, Pydantic symbolic schemas, graph topology, embeddings, SQL rows, cache entries, feedback weights | Mostly prose with frontmatter, links, schemas, scripts, validation reports |
| Lineage | Content hashes, raw/normalized file locations, pipeline status, DataPoint source fields, dataset/user/tenant IDs | Source snapshots, commit-pinned reviews, authored links, git history, archive/replacement lifecycle |
| Activation | Retriever registry, vector search, graph projection, LLM completions, session cache, MCP/API calls | `rg`, descriptions, indexes, authored links, skills, review/validation commands |
| Authority | Pipelines, schemas, retrievers, ACLs, feedback weights, prompts, cache policy | Type specs, collection contracts, AGENTS.md, skills, validation/review commands |

Cognee is better than commonplace at high-volume ingestion and operational serving. It can ingest files, URLs, DLT-shaped data, sessions, and traces; maintain graph/vector/relational projections; serve remote APIs and MCP tools; and isolate datasets by tenant/ACL. Those are real product/runtime concerns that a files-first KB mostly leaves to the surrounding environment.

Commonplace is stronger where retained knowledge needs to be read, disputed, reviewed, retired, or promoted into instructions. A Cognee node, edge, embedding row, or retrieved triplet may have source fields and hashes, but it is not a reviewed claim with link semantics, status, replacement history, or a collection-local quality contract. Cognee's strongest authority surfaces are system-definition artifacts: pipeline code, Pydantic schemas, retriever selection, database context, ACL checks, and feedback-weight updates. Its extracted graph objects are knowledge artifacts until they are used by retrieval/ranking paths, at which point the same stored object also participates in system-definition authority.

The systems also disagree about what "memory" should feel like to an agent. Cognee presents a service: call remember/recall/search, and the runtime assembles context. Commonplace presents an environment: search files, read conventions, follow links, and edit durable artifacts. Cognee's approach is easier to integrate into arbitrary applications; commonplace's approach is easier to audit and evolve as methodology.

The most important split is source-of-truth status. In Cognee, raw documents, session traces, and feedback are sources; DataPoints, graph edges, embeddings, summaries, graph-context snapshots, and triplet embeddings are derived projections; pipelines and retrievers decide how they behave. In commonplace, the note or instruction is often the canonical retained artifact, while generated indexes and reports are secondary views.

**Read-back:** both — agents can call recall/search tools, and `@agent_memory` fetches graph memory before agent functions run.

## Borrowable Ideas

**Separate raw ingestion state from behavior-shaping projections.** Ready to borrow as vocabulary, not architecture. Cognee's `Data` rows, `DataPoint` fields, graph edges, vector collections, and search payloads make it hard to pretend that all retained state has one authority level.

**Pipeline provenance fields on derived artifacts.** Useful if commonplace grows heavier generated views. `source_pipeline`, `source_task`, `source_user`, `source_node_set`, and `source_content_hash` are a compact lineage pattern for derived objects. For current notes, git history and citations are enough.

**Feedback weights as retrieval influence, not claim truth.** Worth tracking. Cognee updates graph node/edge `feedback_weight` from session feedback and lets retrieval use `feedback_influence`. In commonplace, analogous signals should rank candidates for review or retrieval, not silently change whether a claim is treated as true.

**MCP/API wrapper around existing memory operations.** Useful later for consumer projects. Cognee shows the ergonomic value of wrapping add/cognify/search behind MCP and HTTP while keeping direct Python calls available. Commonplace can borrow the packaging idea without moving canonical knowledge out of files.

**Tenant and ACL modeling for shared agent memory.** Ready as a design reference, not an immediate need. If commonplace ever supports hosted or team-shared memory, dataset-level `read/write/delete/share` and tenant membership are a clearer starting point than ad hoc file permissions alone.

**Do not borrow opaque graph memory as the primary KB.** Cognee's graph/vector stack is appropriate for retrieval infrastructure, but it would be a poor replacement for reviewed methodology notes. It should remain a compiled or auxiliary layer unless a future use case genuinely needs database-native operations.

## Trace-derived learning placement

Cognee qualifies as trace-derived learning in a narrow implemented path, not in its default document ingestion path.

**Trace source.** The raw trace source is session-backed agent and Q&A activity. `SessionManager` stores QA entries with optional feedback and used graph element IDs, and it stores agent trace steps with origin function, status, method params, method return value, memory query, memory context, error message, and generated/fallback session feedback ([session manager](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/infrastructure/session/session_manager.py), [memory entry types](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/memory/entries.py)). The `@agent_memory` decorator can write those trace steps automatically around async function calls and can periodically persist recent trace feedback into the permanent graph ([agent-memory runtime](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/modules/agent_memory/runtime.py)).

**Extraction.** The extraction oracle is mixed. Agent trace feedback can be generated by an LLM summary of a method return value, or fall back to deterministic success/failure text ([session manager](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/infrastructure/session/session_manager.py)). `improve(session_ids=...)` applies feedback weights, persists session Q&A, persists agent trace feedbacks, runs default memify enrichment, and syncs graph knowledge back to sessions ([improve API](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/api/v1/improve/improve.py)). The trace-feedback pipeline extracts either `session_feedback` or raw method return values, concatenates non-empty entries per session, and cognifies them into the graph under an `agent_trace_feedbacks` node set ([trace persistence pipeline](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/memify_pipelines/persist_agent_trace_feedbacks_in_knowledge_graph.py), [trace extraction task](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/tasks/memify/extract_agent_trace_feedbacks.py), [trace cognify task](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/tasks/memify/cognify_agent_trace_feedback.py)).

**Storage substrate.** Raw QA and trace entries live in the configured cache backend, with relational session lifecycle rows as auxiliary state. Persisted Q&A and trace feedback are re-ingested through Cognee's normal add/cognify path into dataset files, relational `Data` records, graph nodes/edges, vector indexes, and optional triplet embeddings. Feedback scores update graph-node and graph-edge weights rather than creating a separate prose lesson file ([feedback weights](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/tasks/memify/apply_feedback_weights.py), [session persistence pipeline](https://github.com/topoteretes/cognee/blob/4ca1d0c2bbbb46924acb1f5f6cd805214805ca16/cognee/memify_pipelines/persist_sessions_in_knowledge_graph.py)).

**Representational form.** Raw traces are structured JSON/cache records with prose fields. Session feedback is prose; persisted trace/session blobs become prose inputs to LLM graph extraction; extracted DataPoints and edges are symbolic; embeddings and vector distances are distributed-parametric; feedback weights are numeric ranking state. The operative part depends on the consumer: a trace feedback string advises future retrieval as a knowledge artifact, while a changed `feedback_weight` influences ranking as a system-definition artifact.

**Lineage.** Lineage is good at the dataset and pipeline level but weak at the distilled-lesson level. Persisted trace feedback keeps session ID text and node-set naming, then inherits content hashes, pipeline provenance, and dataset/user fields. It does not preserve a reviewable derivation chain from a specific trace step to a specific durable lesson, nor does it attach a human approval state before the extracted graph influences future retrieval.

**Behavioral authority.** Session and trace entries have advisory authority when recalled as context. Persisted graph nodes/edges advise the agent as evidence or memory. Feedback weights, retriever settings, used graph-element IDs, and graph-to-session sync have ranking and context-selection authority. The system does not promote traces into explicit instructions, validators, skills, or code patches.

**Scope and timing.** The scope is per user/session/dataset, with optional tenant sharing through ACLs. Timing can be online around decorated agent calls, on-demand through `improve(session_ids=...)`, or periodic through `persist_session_trace_after`.

**Survey placement.** Cognee strengthens the survey's "trace-derived retrieval/ranking memory" axis: traces become retrievable graph knowledge and feedback-weighted ranking state. It does not strengthen the stronger artifact-learning claim where traces become reviewed rules, playbooks, tests, or executable skills. It is closest to a trace-to-knowledge-graph and trace-to-ranking-signal system.

## Curiosity Pass

**Cognee is more serious about operations than curation.** The system has migration files, FastAPI routers, pipeline run status, telemetry, cache/session state, remote clients, API keys, dataset permissions, and multiple stores. It has much less machinery for epistemic review of extracted claims.

**The "memory control plane" claim is partly accurate.** Cognee really does coordinate ingestion, graph extraction, retrieval, sessions, feedback, APIs, and ACLs. But the durable memory is mostly database state and extracted graph structure; it is not a curated body of agent-readable doctrine.

**Provenance exists, but audit still requires tooling.** The source hashes and pipeline stamps are useful, yet a future agent cannot inspect a plain file and see why a particular extracted edge exists, whether it was reviewed, whether it supersedes another edge, or whether it should be retired.

**Trace-derived status should not be overgeneralized.** Most Cognee usage is document ingestion and indexing. The trace-derived classification comes from implemented session/agent-memory/improve paths, not from the baseline add/cognify pipeline.

**Access control is real but partly application-layer.** Dataset permissions and tenant membership are checked in service code. The relational graph node/edge models include tenant/user/dataset fields, but row-level security snippets are commented out, so enforcement depends on Cognee's access paths and selected backend handlers.

## What to Watch

- Whether Cognee adds review/approval states for extracted DataPoints, graph edges, trace-derived feedback, and feedback-weight updates.
- Whether trace-derived persistence starts producing explicit lessons, rules, skills, validators, or prompt edits instead of graph knowledge and ranking weights only.
- Whether graph/vector records expose stronger per-edge lineage: source chunk offsets, extraction prompt/model version, confidence, and invalidation status.
- Whether access control moves deeper into graph/vector backends with enforced row-level or dataset-level isolation.
- Whether MCP and API clients become the dominant agent surface, and whether they expose enough provenance for agents to debug retrieved context.
- Whether custom Pydantic schemas and ontology matching become stable enough to serve as durable system-definition artifacts rather than per-run extraction hints.

---

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Cognee needs separate treatment for raw files, relational rows, DataPoints, graph edges, embeddings, pipeline tasks, cache traces, and feedback weights.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw documents, extracted graph context, session Q&A, and trace feedback advise later agents when retrieved.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: pipeline definitions, schemas, ACL checks, retrievers, prompts, and feedback weights instruct, route, enforce, or rank later behavior.
- [Lineage](../../notes/definitions/lineage.md) - clarifies: Cognee has hashes and provenance fields, but not a full reviewable derivation chain for every extracted claim.
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Cognee is trace-derived only through session/agent-memory improvement paths, not ordinary document cognification.
