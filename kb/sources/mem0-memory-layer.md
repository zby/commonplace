---
source: https://github.com/mem0ai/mem0
captured: 2026-03-05
capture: manual
type: github-repo
---

# Mem0: Universal Memory Layer for AI Agents

**Source:** https://github.com/mem0ai/mem0
**Paper:** https://arxiv.org/abs/2504.19413
**Type:** Open-source memory system (Apache 2.0), YC S24
**Retrieved:** 2026-03-05

## Overview

Mem0 ("mem-zero") is a memory layer for AI assistants and agents that extracts, stores, and retrieves facts from conversations. It supports multi-level memory scoped to users, agents, and runs. Production-oriented: claims +26% accuracy over OpenAI Memory on LOCOMO benchmark, 91% faster responses, 90% fewer tokens.

## Architecture

### Memory Model

Mem0 stores **facts** — short declarative statements extracted from conversations (e.g., "Name is John", "Favourite movies are Inception and Interstellar"). Each fact is embedded and stored in a vector store with metadata (user_id, agent_id, run_id, actor_id, timestamps).

Memory types:
- **Conversational/factual** (default) — personal preferences, details, plans, professional info
- **Procedural** — agent-specific procedural knowledge (requires agent_id)
- **Graph relations** (optional) — entity relationships stored in a graph database alongside vector memories

### Core Pipeline: Add

The `add()` operation follows a two-phase pipeline:

**Phase 1 — Fact Extraction:**
1. Parse messages (user/assistant conversation)
2. Send to LLM with a fact extraction prompt → get JSON list of facts
3. The prompt is specifically tuned: "Personal Information Organizer" that extracts preferences, details, plans, etc.
4. Separate prompts for user memory extraction vs agent memory extraction

**Phase 2 — Memory Update (the key innovation):**
1. For each extracted fact, embed it and search the vector store for existing similar memories (top 5)
2. Collect all retrieved old memories, deduplicate by ID
3. Send old memories + new facts to LLM with an update prompt
4. LLM returns a list of actions: ADD (new memory), UPDATE (modify existing), DELETE (remove), or NOOP
5. Execute each action against the vector store
6. Optionally, also add to graph store in parallel

This is the **accretion + curation** pattern — new facts don't just pile up, the LLM decides whether to add, merge, or delete.

### Storage Backends

**Vector stores** (20+ supported): Qdrant, Pinecone, Chroma, Milvus, Faiss, pgvector, Elasticsearch, OpenSearch, Weaviate, Redis, MongoDB, Supabase, Azure AI Search, LanceDB, Cassandra, S3 Vectors, Neptune Analytics, etc.

**Graph stores** (optional): Neo4j, Memgraph, Kuzu — used for entity relationship extraction alongside the vector store.

**Metadata store**: SQLite for memory history tracking.

### Search / Retrieval

`search(query, user_id, limit)` — embeds the query and does vector similarity search filtered by user/agent/run scope. Optional reranking via configurable reranker (Cohere, etc.).

### Memory Operations (MemoryBase interface)

- `add(messages)` — extract facts, reconcile with existing, store
- `get(memory_id)` — retrieve single memory
- `get_all(user_id)` — list all memories for a user
- `search(query, user_id)` — semantic search
- `update(memory_id, data)` — direct update
- `delete(memory_id)` — delete single memory
- `delete_all(user_id)` — delete all memories for a user
- `history(memory_id)` — get change history (ADD/UPDATE/DELETE events tracked in SQLite)
- `reset()` — clear everything

### Agent Integration

Simple API: `memory = Memory(); memory.add(messages, user_id="alice"); memories = memory.search("restaurants", user_id="alice")`. The memory layer sits outside the agent loop — memories are retrieved before LLM calls and injected into the system prompt, new memories are extracted after.

## Key Design Decisions

1. **Facts as unit of storage** — not raw messages, not summaries, but extracted declarative facts. This is opinionated: the LLM decides what matters.
2. **LLM-mediated CRUD** — the update step uses the LLM to decide ADD/UPDATE/DELETE, not just append. This prevents memory bloat but introduces LLM judgment into storage.
3. **Vector-first, graph-optional** — the primary store is vector (for semantic search); graph is an add-on for relationship tracking, not the core.
4. **Scoped by user/agent/run** — memories are namespaced by who they belong to. This is oriented toward personalization use cases.
5. **Stateless integration** — Mem0 doesn't manage the agent loop or conversation flow. It's a memory API you call from your agent.
6. **Massive backend flexibility** — 20+ vector stores, multiple graph stores. Integration-heavy, aimed at enterprise deployment.

## Limitations

- Fact extraction prompt is tuned for personal assistant use cases (preferences, details, plans). May not capture domain-specific knowledge well.
- The LLM-mediated update step adds latency and cost to every add operation (two LLM calls: extract + reconcile).
- No temporal model — memories don't have validity intervals or decay by default (despite "dynamic forgetting" claims in marketing).
- Graph store is bolted on, not deeply integrated with the vector store.
