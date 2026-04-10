---
description: Four-database episodic memory service (Postgres+Qdrant+Neo4j+Redis) with LLM consolidation from episodes to scored semantic facts and temporal graph expansion; heaviest infra, thinnest transformation
type: related-system
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-03-28"
---

# REM is a database-heavy episodic memory service with LLM consolidation

REM (Recursive Episodic Memory) is an open-source memory service for AI agents that stores interaction episodes and periodically consolidates them into semantic facts. Built by satyammistari (MIT license), the system uses a Go API (Fiber v2) as the primary HTTP surface, a Python worker (FastAPI) for LLM-dependent tasks (parsing, embedding, consolidation), and four backing databases: PostgreSQL 16 (episodes, users, agents, semantic memories), Qdrant 1.7 (vector search), Neo4j 5 (temporal episode graph), and Redis 7 (cache, queues). A Next.js 14 dashboard provides visualization. A Python SDK (`rem-memory`) wraps the API with sync and async methods plus a LangChain integration adapter.

**Repository:** https://github.com/satyammistari/REM

## Core Ideas

**Write-Consolidate-Retrieve as the core loop.** The system's central pipeline has three phases. Write: after a task, the agent sends a content string, agent ID, user ID, and outcome; the Go API calls the Python worker to parse the content into structured metadata (intent, entities, domain, emotion signal, importance score) via GPT-4o-mini, embeds the content via `text-embedding-3-large`, stores the episode in PostgreSQL, upserts the embedding in Qdrant, creates an Episode node in Neo4j with a FOLLOWED_BY temporal edge to the previous episode, and publishes a consolidation job to Redis. Consolidate: a Celery task fetches unconsolidated episodes from the Go API, groups them by domain and intent-keyword overlap, sends each cluster to GPT-4o which extracts 1-5 "semantic memory" facts per cluster, embeds each fact, stores the fact in Qdrant's `semantic_memories` collection, creates a SemanticMemory node in Neo4j linked to source episodes, and marks source episodes as consolidated. Retrieve: the Go API embeds the query, searches Qdrant for nearest episodes and semantic memories in parallel, expands the top 3 episode results through Neo4j temporal neighbors (depth 1, discounted 0.8x), reranks by a weighted combination of similarity (0.6), recency (0.25), and retrieval frequency (0.15), and assembles a plain-text injection prompt containing episode summaries and learned facts with confidence percentages.

**Four-database architecture for separation of concerns.** PostgreSQL holds the relational data model (episodes, agents, users, semantic memories with full field sets including Active, ContradictedBy, Superseded flags). Qdrant provides vector similarity search with two collections (`episodes` at 1536 dimensions, `semantic_memories` at 1536 dimensions). Neo4j stores the temporal episode graph (Episode nodes linked by FOLLOWED_BY edges, SemanticMemory nodes linked by COMPRESSED_INTO edges from source episodes). Redis caches embeddings (24h TTL) and carries Celery task queues. The database separation is genuine architectural partitioning: PostgreSQL is the system of record, Qdrant is the retrieval engine, Neo4j adds temporal traversal, and Redis is the cache/queue layer. But the operational cost is high: four databases that must be running, consistent, and coordinated.

**LLM-driven episode parsing enriches raw content at write time.** Every episode is parsed by GPT-4o-mini into five fields: intent (one sentence, max 100 chars), entities (list of strings), domain (one of seven fixed categories: coding, writing, research, planning, analysis, communication, general), emotion signal (one of six: productive, frustrated, confused, satisfied, urgent, neutral), and importance score (0.0-1.0). This metadata then drives clustering during consolidation (grouping by domain and intent keywords). The parse step adds genuine structure that raw content does not have, but the seven-domain taxonomy is quite coarse and the emotion signal is of unclear utility for memory retrieval.

**Consolidation is keyword clustering plus LLM compression.** The consolidation engine groups episodes first by domain, then by intent keyword overlap (greedy set-intersection requiring 2+ shared tokens in the engine, or 1+ in the standalone Clusterer). Clusters of 3+ episodes are sent to GPT-4o with a prompt asking for 1-5 "durable, reusable facts" as JSON with confidence, fact_type (preference/rule/pattern/skill/fact), and domain. The resulting semantic memories are short strings (max 200-300 chars) with confidence scores. This is the system's learning mechanism: raw episodes become scored facts. There is no update, contradiction detection, or revision of existing semantic memories - each consolidation run produces new facts and marks source episodes as consolidated.

**Temporal graph expansion at retrieval.** After vector search returns candidate episodes, the retrieve service expands the top 3 hits through Neo4j's FOLLOWED_BY graph (depth 1, matching both directions). Temporal neighbors are added to the result set with an 0.8x score discount. This addresses a real problem: episodes that are temporally adjacent to a relevant episode may be relevant even if their embeddings are not similar to the query. The mechanism is simple but sound. However, FOLLOWED_BY edges only connect consecutive episodes for the same agent, so the graph is a linear chain per agent, not a rich causal graph. The README's claim of a "causal episode graph" is not supported by the implementation - there are no causal edges, only temporal succession.

**Injection prompt builder as the integration surface.** The retrieve endpoint produces a pre-formatted text block (`=== RELEVANT MEMORY CONTEXT ===`) containing memory summaries with domain, outcome, days-ago, and content, plus learned facts with confidence percentages. This is the system's output to the consuming agent. The prompt format is fixed and opinionated - agents get a single text block to inject, not structured data they can reason over. This simplifies integration but limits how agents can use the memory.

## Comparison with Our System

| Dimension | REM | Commonplace |
|---|---|---|
| Storage | PostgreSQL + Qdrant + Neo4j + Redis (four databases) | Markdown files in git |
| Knowledge unit | Episode (raw content + LLM-parsed metadata) and SemanticMemory (short fact string + confidence + type) | Typed note with frontmatter, prose body, and semantic links |
| Learning loop | Write episodes -> cluster by domain/keyword -> LLM-extract facts -> store as semantic memories | Human+agent write -> connect -> validate -> mature |
| Update model | Append-only: new facts created per consolidation run, no revision of existing facts | Progressive formalization: notes evolve through editing, restructuring, and status changes |
| Retrieval | Vector search + temporal graph expansion + weighted reranking -> injection prompt | Keyword/ripgrep search -> agent loads relevant notes progressively |
| Knowledge depth | Short fact strings (200-300 chars) with confidence floats | Multi-paragraph arguments with evidence, caveats, and articulated links |
| Infrastructure | Four databases + Go API + Python worker + Redis queue + OpenAI API | Git + text editor + ripgrep |
| Temporal model | FOLLOWED_BY edges in Neo4j (linear chain per agent) | Manual dating, `last-checked` fields, `status: outdated` |
| Contradiction handling | SemanticMemory has `ContradictedBy` and `Superseded` fields in the domain struct, but no code populates them | Link semantics (contradicts), human judgment |

**Where REM is stronger.** The temporal graph expansion during retrieval is a mechanism commonplace lacks entirely - adjacent episodes can surface without matching the query embedding. The automated consolidation pipeline requires no human intervention; it just runs. The injection prompt builder provides a turn-key integration that requires no agent sophistication. The multi-database architecture gives clean separation of concerns for different access patterns (relational queries, vector search, graph traversal, caching).

**Where commonplace is stronger.** Knowledge has internal structure: notes contain arguments, evidence, caveats, and articulated relationships, not just fact strings with confidence floats. The maturation path (text -> note -> structured-claim) produces deeper knowledge over time rather than accumulating short facts. Link semantics capture *why* notes relate (extends, grounds, contradicts), not just *that* they were derived from the same episode cluster. Infrastructure cost is minimal - no databases to run, no API servers to maintain, no LLM calls for basic operations. Most importantly: the knowledge artifacts are inspectable, editable, and version-controlled - a human or agent can read, critique, and improve any note directly.

**The deepest divergence** is the learning granularity. REM's semantic memories are one-liner facts: "User prefers TypeScript over JavaScript" with a confidence score. Commonplace notes are multi-paragraph explorations with evidence, reasoning, and explicit links to other knowledge. REM optimizes for automated extraction at scale; commonplace optimizes for understanding depth. These serve genuinely different use cases: REM is better for capturing user preferences and recurring patterns across many lightweight interactions, commonplace is better for building durable understanding of complex domains.

## Borrowable Ideas

**Temporal graph expansion for retrieval widening.** The mechanism of finding vector-similar items and then expanding through temporal neighbors is simple and sound. For commonplace, a lighter version could be: after finding relevant notes, also load notes that were edited in the same session or that share the same edit-date cluster. *Needs a use case first - requires session tracking that we do not currently have.*

**Injection prompt as a first-class output.** The idea of the memory system producing a ready-to-inject text block rather than just returning ranked results is ergonomically clean. For commonplace, a `/context` skill that produces a pre-formatted context block from relevant notes would reduce the cognitive load on consuming agents. *Ready to borrow as a pattern - the format itself is trivial to implement.*

**Parallel retrieval across different storage backends.** The retrieve service runs Qdrant episode search and semantic memory search in parallel goroutines, then merges results. This is a sound pattern for any system with multiple retrieval channels. *Just a reference - we have a single retrieval channel (ripgrep).*

**Recency-weighted reranking with retrieval frequency.** The scoring formula (0.6 similarity + 0.25 recency + 0.15 retrieval frequency) is a reasonable default for balancing relevance, freshness, and proven utility. *Needs a use case first - requires retrieval tracking that we do not have.*

## Curiosity Pass

**Does the "recursive" in Recursive Episodic Memory refer to an actual mechanism?** The name suggests episodes recursively consolidate - facts from one round of consolidation feed into the next round, building higher-order abstractions. In the code, consolidation runs once: raw episodes -> semantic facts. Semantic memories are never reconsolidated into higher-order memories. The consolidation is single-pass, not recursive. "Recursive" is naming, not mechanism.

**The "causal episode graph" is a temporal succession chain.** The README claims a "causal graph of episodes and facts your agent can traverse." In Neo4j, episodes are linked by FOLLOWED_BY (temporal succession) and episodes are linked to semantic memories by COMPRESSED_INTO (provenance). There are no causal edges - no representation of "episode X caused episode Y" or "fact X explains fact Y." The graph is a simple timeline with consolidation provenance, not a causal model. GetAgentGraphData, which would return the full graph for visualization, has a stub implementation that returns empty nodes and edges with a comment "Minimal graph: we'll expand/normalize in Day 3+."

**The forgetting policy is a roadmap item, not a feature.** The README's comparison table marks "Forgetting policy" as "First-class" with a bold checkmark. In the code, there is no forgetting mechanism - no TTL on episodes, no decay on semantic memories, no pruning of low-confidence facts. The roadmap section lists "Fine-grained forgetting and redaction policies" as a future item. The `ContradictedBy` and `Superseded` fields exist on the SemanticMemory domain struct but no code populates or acts on them. The forgetting claim is purely aspirational.

**The "self-evolving memories" claim has no implementation.** The README checks "Self-evolving memories" as a feature. In the code, semantic memories are created once and never updated. There is no mechanism to revise a fact's confidence based on new evidence, merge overlapping facts, or evolve a fact as more episodes arrive. The domain struct has `Active`, `ContradictedBy`, `Superseded`, and `UpdatedAt` fields that suggest lifecycle management was planned, but the consolidation pipeline only creates, never updates.

**Four databases is high infrastructure cost for what the system actually does.** The write path touches all four databases sequentially. The consolidation path reads from the Go API (PostgreSQL), writes to the Go API (PostgreSQL + Qdrant + Neo4j). The retrieve path reads from Qdrant and Neo4j. The question is whether the architectural separation justifies the operational complexity. A simpler alternative: PostgreSQL with pgvector (vector search built in), a materialized view for temporal adjacency (replacing Neo4j), and in-process caching (replacing Redis for embedding cache). This would achieve the same behavior with one database. Among reviewed systems, [Hindsight](./hindsight.md) uses PostgreSQL+pgvector for both relational and vector storage and achieves SOTA retrieval benchmarks.

**The clustering mechanism is extremely coarse.** Consolidation groups episodes by domain (7 categories) and intent keyword overlap (2+ shared tokens after removing 28 stop words). This means episodes about "TypeScript migration" and "TypeScript linting" would cluster together (shared token: "typescript"), but "building React components" and "writing JSX code" would not (no shared tokens despite being about the same thing). The system acknowledges this: the Clusterer class comments "a vector-similarity clustering pass can be added later without changing the interface." For now, the clustering quality is bottlenecked by keyword overlap, which is well below the semantic similarity that the system already computes via embeddings.

**The benchmark suite targets conversational memory benchmarks, not agent memory.** The three benchmarks (LongMemEval, LoCoMo, ConvoMem) test whether the system can recall facts from multi-turn conversations. These are meaningful tests for conversational memory but do not test the agent-memory use case the README emphasizes - remembering task outcomes, learning user preferences over time, or improving agent behavior through accumulated knowledge. The benchmark harness exists but results are not published in the repo.

## Trace-derived learning placement

REM fits the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md) as a **service-owned trace backend** on axis 1 and **symbolic artifact learning** on axis 2.

**Axis 1 — ingestion pattern.** REM owns the episode schema and accepts structured traffic over an HTTP API (`POST /api/v1/episodes`). The Go API parses, embeds, stores, and queues consolidation jobs. This is the service-owned backend pattern alongside OpenViking and OpenClaw-RL, not a session extension or trajectory-run system. Unlike OpenViking, REM does not define a typed message schema with role/parts — the source is an opaque content string that the service parses into metadata (intent, entities, domain, emotion, importance) via GPT-4o-mini. Unlike cass-memory, it does not discover or normalize session logs from external agents.

**Axis 2 — promotion target.** Purely artifact-learning. Consolidation produces short fact strings (max 200-300 chars) with confidence scores, stored in PostgreSQL and Qdrant. No weight promotion, no training export. The SemanticMemory domain struct has `Active`, `ContradictedBy`, and `Superseded` fields, but no code populates them — consolidation is single-pass and append-only.

**What REM adds to the survey.** REM reinforces the service-owned backend category without introducing a new pattern. Its distinguishing trait is the widest gap between aspirational lifecycle management (domain fields for contradiction, supersession, and active status) and actual implementation (append-only, no deduplication, no revision). It also demonstrates the coarsest clustering mechanism in the survey: domain grouping plus intent keyword overlap, well below the semantic similarity its own embeddings could support. This strengthens the survey's finding that extraction is concrete but maintenance remains the open problem.

**Five-stage entry:**

- **Trigger.** Consolidation queued on every episode write via Redis (fire-and-forget), plus a periodic Celery task. Requires 3+ unconsolidated episodes to proceed.
- **Source format.** Agent-submitted content strings via HTTP API, enriched at write time by GPT-4o-mini into intent, entities, domain (7 categories), emotion signal, and importance score. Not a session log or conversation transcript — an opaque content field that the service parses.
- **Extraction.** Two-step: keyword clustering (group by domain, then greedy intent-token overlap requiring 2+ shared tokens), then GPT-4o compression asking for 1-5 "durable, reusable facts" per cluster as JSON with confidence, fact_type, and domain. Episode content is truncated to 500 chars per episode in the prompt.
- **Promotion.** Append-only semantic memories in PostgreSQL and Qdrant. Each fact is a short string with confidence score, fact type (preference/rule/pattern/skill/fact), domain, and source episode IDs. No deduplication, no revision, no lifecycle management despite domain fields for it.
- **Scope.** Per-agent, multi-session. Each agent's episodes consolidate independently. No cross-agent mining, no shared knowledge store across agents.

## What to Watch

- Whether recursive consolidation (facts consolidating into higher-order abstractions) is actually implemented, fulfilling the system's name
- Whether the forgetting policy materializes and what mechanism it uses (decay, TTL, explicit pruning, or some combination)
- Whether the four-database architecture persists or is simplified as the system matures - the PostgreSQL+pgvector path would be a natural consolidation
- Whether the SemanticMemory lifecycle fields (ContradictedBy, Superseded, Active) get wired up, enabling actual memory evolution
- Whether the dashboard's graph visualization (currently stubbed) becomes a useful tool for inspecting memory state

---

Relevant Notes:

- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: REM adds a database-heavy, infrastructure-first case to the broader survey; its four-database architecture is the heaviest infrastructure footprint among reviewed systems
- [Hindsight](./hindsight.md) — contrasts: both use vector search + graph expansion for retrieval, but Hindsight achieves SOTA benchmarks with PostgreSQL+pgvector alone while REM requires four databases; Hindsight's consolidation is richer (four-way parallel retrieval, reflection cycles)
- [Cognee](./cognee.md) — compares: both are database-first rather than filesystem-first, but Cognee has a richer extraction pipeline (Pydantic-schema graph extraction) while REM has a simpler keyword-clustered LLM compression
- [cass-memory](./cass_memory_system.md) — compares: both consolidate raw interactions into scored facts, but cass-memory has confidence decay (90-day half-life), anti-pattern inversion, and cross-agent mining where REM has append-only facts with no lifecycle management
- [distillation](../definitions/distillation.md) — exemplifies: the consolidation pipeline is a distillation operation (episodes compressed into shorter facts under a context budget), though the transformation is shallow (LLM prompt asking for "durable facts" from clustered episodes)
- [trace-derived-learning-techniques-in-related-systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: REM is a code-inspected trace-derived artifact-learning system placed in the service-owned backend category alongside OpenViking; its append-only consolidation with unimplemented lifecycle fields reinforces the survey's finding that extraction is concrete but maintenance remains open
