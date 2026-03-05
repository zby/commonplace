# Cognee: Knowledge Engine for AI Agent Memory

**Source:** https://github.com/topoteretes/cognee
**Paper:** https://arxiv.org/abs/2505.24478 (Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning)
**Type:** Open-source knowledge engine (Apache 2.0), $7.5M seed
**Retrieved:** 2026-03-05

## Overview

Cognee is a knowledge engine that transforms raw data into persistent, dynamic AI memory. It combines vector search and graph databases with a pipeline architecture (add → cognify → memify → search). The core idea: data goes through progressive refinement — from raw documents to chunked text to knowledge graphs to enriched memory structures.

## Architecture

### Three-Phase Pipeline

**Phase 1: add()** — Ingest raw data (text, files, images, audio transcriptions) into the system. Supports 30+ data sources. Data is stored as documents in datasets with user-scoped permissions.

**Phase 2: cognify()** — The core processing step. A pipeline with 5 default tasks:
1. `classify_documents` — identify document types and structures
2. `extract_chunks_from_documents` — break content into semantically meaningful segments using TextChunker or LangchainChunker
3. `extract_graph_from_data` — use LLM to extract entities and relationships from chunks → build knowledge graph (subject-predicate-object triplets)
4. `summarize_text` — create hierarchical summaries
5. `add_data_points` — embed everything and commit to vector store + graph database

Supports custom graph models via Pydantic (e.g., `ScientificPaper` with typed fields), ontology integration, and custom extraction prompts.

Also supports a `temporal_cognify` mode that extracts events with timestamps and builds a temporal knowledge graph.

**Phase 3: memify()** — Enrichment pipeline that works on the existing knowledge graph. Default tasks:
1. `extract_subgraph_chunks` — pull subgraphs from the knowledge graph
2. `add_rule_associations` — apply coding rules or domain rules to nodes

Memify is designed as a post-processing layer: prune stale nodes, strengthen frequent connections, reweight edges based on usage. However, the current default implementation is simpler than the documentation suggests — it focuses on rule associations rather than the full pruning/reweighting described in marketing materials.

### Pipeline Architecture

Everything runs through `run_pipeline(tasks, ...)`. Tasks are composable: each task is a `Task` wrapping a function. Tasks run sequentially, each receiving output from the previous. Pipeline supports:
- Incremental loading (skip already-processed data)
- Pipeline caching
- Background execution
- Batching (configurable batch sizes per task)
- Per-user dataset authorization

### Storage Backends

**Graph databases:** Neo4j, FalkorDB, KuzuDB, NetworkX (in-memory)
**Vector stores:** Qdrant, Weaviate, LanceDB, pgvector, Redis
**Relational metadata:** SQLite, PostgreSQL

The poly-store design means graph, vector, and relational stores can be mixed and matched.

### Search / Retrieval

Multiple search types (SearchType enum):
- `GRAPH_COMPLETION` — natural language completion with graph context
- `CHUNKS` — find relevant document chunks by embedding similarity
- `GRAPH_SUMMARY_COMPLETION` — completion using graph summaries
- Various retriever implementations: RAG completion, graph completion, triplet retriever, chunks retriever, description-to-code search

### API Surface

Simple top-level API:
```python
await cognee.add("text or file path")
await cognee.cognify()  # build knowledge graph
await cognee.memify()   # enrich memory
results = await cognee.search("query", query_type=SearchType.GRAPH_COMPLETION)
await cognee.delete()   # cleanup
```

Also has a CLI (`cognee-cli add/cognify/search/delete`) and REST API via FastAPI.

## Key Design Decisions

1. **Pipeline-first architecture** — everything is a composable pipeline of tasks. This makes the system highly customizable but means you need to understand the pipeline model to extend it.
2. **Three distinct phases** — add (ingest), cognify (extract structure), memify (enrich). This separates data ingestion from knowledge construction from memory refinement.
3. **Graph + vector hybrid** — knowledge graph for relationships, vector store for semantic search. Both are first-class citizens, not one bolted onto the other.
4. **Custom graph models** — domain-specific Pydantic schemas for entity extraction. More structured than Mem0's free-form facts or Graphiti's generic entity types.
5. **Multi-tenant by design** — user-scoped datasets with authorization checks at every pipeline step.
6. **Incremental processing** — cognify can skip already-processed data, important for large datasets.

## Limitations

- The memify phase is undersized relative to its ambitions — current defaults are simpler than the described pruning/reweighting/strengthening capabilities
- Heavy pipeline machinery for what could be simpler operations
- Many backends but integration depth varies
- Less focused than competitors: tries to be both a knowledge graph builder and a memory system
