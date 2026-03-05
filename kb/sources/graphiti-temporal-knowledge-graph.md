# Graphiti: Temporal Knowledge Graph for AI Agents

**Source:** https://github.com/getzep/graphiti
**Paper:** https://arxiv.org/abs/2501.13956
**Type:** Open-source knowledge graph framework (Apache 2.0), by Zep
**Retrieved:** 2026-03-05

## Overview

Graphiti is a framework for building and querying temporally-aware knowledge graphs for AI agents. Unlike batch-oriented RAG or GraphRAG, Graphiti continuously integrates user interactions, structured and unstructured data into a coherent, queryable graph with incremental updates and bi-temporal tracking. Powers Zep's commercial context engineering platform.

## Architecture

### Graph Model

The graph has four types of nodes and five types of edges:

**Nodes:**
- **EntityNode** — extracted entities (people, places, concepts) with name, summary, attributes, and embeddings
- **EpisodicNode** — represents an ingestion event ("episode") with content, source type, timestamps
- **CommunityNode** — groups of related entities discovered via community detection (label propagation)
- **SagaNode** — sequences of related episodes (e.g., a conversation thread)

**Edges:**
- **EntityEdge** — relationships between entities with fact text, embeddings, and temporal validity intervals
- **EpisodicEdge** — links episodes to the entities they mention
- **CommunityEdge** — membership edges between entities and communities
- **HasEpisodeEdge** — links sagas to their episodes
- **NextEpisodeEdge** — temporal ordering within a saga

### Bi-Temporal Model

Every entity edge has explicit temporal fields:
- **valid_at** — when the relationship became true in the real world
- **invalid_at** — when it ceased being true (null if still valid)
- **created_at** — when it was ingested into the graph

This enables point-in-time queries: "What was true as of date X?" Old facts aren't deleted — they're invalidated with a timestamp.

### Core Pipeline: add_episode()

When you add an episode (a piece of text, JSON data, or message), Graphiti runs:

1. **Retrieve context** — fetch previous episodes from the same group and saga
2. **Extract nodes** — use LLM to identify entities mentioned in the episode
3. **Resolve nodes** — deduplicate against existing entities in the graph (merge or create new)
4. **Extract edges** — use LLM to identify relationships between extracted entities
5. **Resolve edges** — compare with existing edges; handle contradictions via temporal invalidation
6. **Build episodic edges** — link the episode to all entities it mentions
7. **Save everything** — bulk write nodes, edges, and episodic links
8. **Update communities** — run community detection to update entity groupings

Each step uses LLM calls for extraction and deduplication decisions. Concurrency is controlled by SEMAPHORE_LIMIT.

### Storage Backends

**Graph databases:** Neo4j (primary), FalkorDB, Kuzu (embedded), Amazon Neptune

All database operations go through a pluggable driver architecture:
- `GraphDriver` ABC with 11 operations interfaces (entity nodes, episode nodes, community nodes, saga nodes, entity edges, episodic edges, community edges, has-episode edges, next-episode edges, search, maintenance)
- Each backend provides concrete implementations
- Query dialect differences handled by `match/case` on GraphProvider enum

### Search / Retrieval

Hybrid search combining three strategies:
- **Semantic search** — embedding similarity on entity nodes and entity edges
- **Keyword search** — BM25 full-text search
- **Graph traversal** — follow edges from result nodes to discover connected information

Search is configured via `SearchConfig` with pre-built recipes:
- `EDGE_HYBRID_SEARCH_RRF` — reciprocal rank fusion of semantic + keyword on edges
- `EDGE_HYBRID_SEARCH_NODE_DISTANCE` — hybrid search with graph distance reranking
- `COMBINED_HYBRID_SEARCH_CROSS_ENCODER` — search both nodes and edges, rerank with cross-encoder

Results can be reranked using a cross-encoder (OpenAI-based by default, Gemini also supported).

### Custom Entity Types

Developers can define custom entity types as Pydantic models. During extraction, the LLM uses these schemas to produce typed entities with structured attributes.

### MCP Server

Ships with a Model Context Protocol server for integration with Claude, Cursor, and other MCP clients. Exposes episode management, entity management, search, and graph maintenance as MCP tools.

## Key Design Decisions

1. **Graph-first, not vector-first** — the primary data structure is a knowledge graph (nodes + edges), not a vector store. Embeddings are attributes on nodes/edges, used for semantic search within the graph.
2. **Temporal edge invalidation** — contradictions don't overwrite; old edges are invalidated with timestamps. This preserves history and enables point-in-time queries.
3. **Episode-centric ingestion** — data comes in as "episodes" (events), not as static documents. This fits conversational and streaming data well.
4. **LLM-heavy pipeline** — extraction, deduplication, and edge resolution all use LLM calls. High quality but expensive per ingestion.
5. **Community detection** — automatic grouping of related entities via label propagation, enabling hierarchical retrieval.
6. **No memory decay** — facts are valid or invalid, not weighted by recency. The temporal model is about historical accuracy, not relevance scoring.

## Limitations

- Requires a graph database (Neo4j, FalkorDB, Kuzu, or Neptune) — not just a vector store
- LLM-intensive: multiple calls per episode for extraction, deduplication, resolution
- Oriented toward enterprise/conversational data; less suited for static document corpora
- Community detection adds overhead; utility depends on graph density
