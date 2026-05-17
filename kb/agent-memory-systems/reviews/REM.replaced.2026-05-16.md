---
description: Four-database episodic memory service (Postgres + Qdrant + Neo4j + Redis) where a Go API ingests agent episodes, a Python Celery worker LLM-clusters and compresses them into scored semantic facts, and retrieval widens via temporal graph hops
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: []
status: outdated
last-checked: "2026-04-12"
---

# REM is a database-heavy episodic memory service with single-pass LLM consolidation

> Replaced 2026-05-16. See [REM](./REM.md) for the current review.

REM (Recursive Episodic Memory) is an open-source memory service for AI agents that stores interaction episodes and periodically consolidates them into semantic facts. Built by satyammistari (MIT license), REM splits its runtime across a Go HTTP API (Fiber v2, the primary write/read surface), a Python worker (FastAPI + Celery) that owns every LLM-dependent step, and four backing datastores: PostgreSQL 16 (episodes, semantic memories, users, agents), Qdrant 1.7 (two 1536-dim collections, `episodes` and `semantic_memories`), Neo4j 5 (an Episode/SemanticMemory graph), and Redis 7 (embedding cache plus Celery broker). A Next.js 14 dashboard and a Python SDK (`rem-memory`, with a LangChain adapter) sit on top. The repo ships a `docker-compose.yml` for the four databases and a benchmarks directory harnessing LongMemEval, LoCoMo, and ConvoMem.

**Repository:** https://github.com/satyammistari/REM

## Core Ideas

**Write -> Consolidate -> Retrieve loop, split across Go and Python.** The Go `WriteService.WriteEpisode` handler is a single function that drives the whole write path: it calls the Python worker's `/parse` endpoint (best-effort, 8s timeout) to enrich the raw content, calls `/embed` (12s timeout) with a Redis MD5 cache around it, inserts the episode row in PostgreSQL, upserts the point in Qdrant's `episodes` collection, creates an `Episode` node in Neo4j with a `FOLLOWED_BY` edge to the previous episode for the same agent, and fires a Redis consolidation job as a goroutine. Consolidation runs as a Celery task (`consolidation.run_for_agent`) that fetches up to 50 unconsolidated episodes for the agent via the Go API, invokes `ConsolidationEngine.consolidate`, embeds each produced fact through `/embed`, POSTs each fact to `POST /api/v1/semantic` on the Go API, and PATCHes source episodes to `consolidated=true`. Retrieval (`RetrieveService.Retrieve`) embeds the query, launches parallel goroutines against `SearchEpisodes` and `SearchSemanticMemories`, expands the top 3 episode hits one hop through Neo4j, reranks, and renders a text block. The split is pragmatic (Python for OpenAI clients, Go for concurrency and HTTP) but expensive: every episode and every retrieval touches both services.

**Write-time LLM enrichment into a fixed five-field schema.** `ParseService.parse` in the Python worker sends the raw content to `gpt-4o-mini` with a system prompt instructing it to return JSON containing `intent` (<=100 chars), `entities` (<=10 strings), `domain` (one of seven categories: `coding, writing, research, planning, analysis, communication, general`), `emotion_signal` (one of six: `productive, frustrated, confused, satisfied, urgent, neutral`), and `importance_score` (0.0-1.0). The service has fallbacks for each field and defaults domain to `general` on failure. This metadata is then what consolidation clusters on. The taxonomy is narrow by design — `domain` has only seven values and `emotion_signal` has six — so the parse step delivers a coarse but predictable shape. It is a real transformation (raw content -> structured metadata) but its value depends entirely on how well those categories match the agent's actual domain.

**Clustering is domain-bucketing plus greedy keyword overlap.** `ConsolidationEngine.consolidate` (the path the Celery task actually invokes) groups episodes by `domain`, then within each domain does a greedy pass: for each unused episode, seed a cluster and absorb any other episode whose tokenized `intent` shares >=2 tokens. Clusters of >=3 episodes are kept. There is also a parallel `Clusterer` class (in `services/consolidation/clusterer.py`) that uses the same domain-first strategy but lowers the overlap threshold to any non-empty intersection (>=1 shared keyword, with 23 hardcoded stop words removed). The comment in `Clusterer` admits the design: "a vector-similarity clustering pass can be added later without changing the interface." The system already produces embeddings for every episode but does not use them for clustering — clustering is keyword-only, even though semantic clustering is the obvious upgrade.

**Compression is a single-shot GPT-4o prompt asking for 1-5 facts.** Each cluster (capped at 15 episodes, each truncated to 500 chars) is formatted into a prompt asking `gpt-4o` to emit JSON facts with `fact` (<=200 chars), `confidence`, `fact_type` (`preference/rule/pattern/skill/fact`), and `domain`. The alternative `Compressor` class uses a slightly different schema (`content` up to 300 chars, `fact_type` in `preference/pattern/error/skill/context/relationship`, plus `importance_score`, `outcome`, `confidence_score`) but the engine-invoked path goes through the `_compress_cluster` variant. Every surviving fact is then embedded, stored in Qdrant's `semantic_memories` collection, and written back via `POST /api/v1/semantic`. Source episode IDs are attached but no graph edge is created between episodes and the new semantic memory — the Go semantic handler inserts into Postgres + Qdrant, but there is no call to `LinkEpisodeToSemantic` even though Neo4j has that function exposed.

**Temporal graph is a per-agent linear chain, not a causal graph.** In Neo4j, `CreateEpisodeNode` merges an `Episode` with `agent_id`, `domain`, and `created_at`. `CreateTemporalEdge` then adds a single `FOLLOWED_BY` edge from the previous episode for that agent to the new one. The neighbor query `GetTemporalNeighbors` does `MATCH (e)-[:FOLLOWED_BY*1..depth]-(n:Episode)`, with `depth=1` passed from the retriever. There are no causal edges, no cross-agent links, no semantic-memory hops during expansion, and no weighting on the edges. The README markets a "causal episode graph"; the code implements a per-agent succession list stored in Neo4j.

**Retrieval reranking and injection prompt.** After Qdrant returns candidates and Neo4j adds one-hop temporal neighbors (each neighbor inherits the seed's score multiplied by 0.8), every surviving episode is rescored as `0.6*similarity + 0.25 * 1/(1 + days_since * 0.1) + 0.15 * min(retrieval_count * 0.05, 0.3)`. Top-K is clamped to 20. Retrieval counts are incremented fire-and-forget. The final `buildInjectionPrompt` emits a fixed text block framed with `=== RELEVANT MEMORY CONTEXT ===` containing per-episode lines `[Memory i] (domain, outcome, N days ago): raw_content` and per-fact lines `[Learned Fact]: fact (confidence: XX%)`. The consuming agent receives `InjectionPrompt` as a string in the response, alongside the structured `Episodes` and `SemanticMemories` arrays.

**Embedding cache as the only cross-service state.** Redis holds two things: embedding values keyed by `md5(content)` with a 24h TTL (used by both the Go write/retrieve path and the Python `EmbedService`), and a consolidation job stream. Both services use the same `text-embedding-3-large` model at `1536` dimensions. Embedding normalization differs: the Python `EmbedService` lowercases and strips before hashing, while the Go `WriteService` hashes the raw content. The two caches are effectively separate keyspaces even though they share a Redis instance.

## Comparison with Our System

| Dimension | REM | Commonplace |
|---|---|---|
| Storage | PostgreSQL + Qdrant + Neo4j + Redis, four containers plus Go API plus Python worker | Markdown files in a git repository |
| Knowledge unit | `Episode` (raw string + parsed metadata) and `SemanticMemory` (short fact + confidence + type) | Typed note with frontmatter, prose body, articulated links |
| Write path | HTTP POST into Go API, automatic parse+embed+store+enqueue | Human or agent edits a markdown file, commits |
| Learning | Background Celery compresses clusters into short facts; no revision | Maturation (seedling -> current -> superseded), editing, restructuring |
| Retrieval | Vector search + 1-hop temporal expansion + weighted rerank + fixed injection prompt | Ripgrep + index scanning + agent-driven progressive loading |
| Temporal model | `FOLLOWED_BY` edges forming a per-agent succession chain | `last-checked` fields, status lifecycle, git history |
| Contradiction handling | Columns `contradicted_by` and `superseded` exist in Postgres but no code writes them | Explicit `contradicts` links between notes, human curation |
| Integration surface | HTTP API + SDK + LangChain adapter | CLI (`commonplace-*`) + skills loaded into the Claude harness |
| Operational cost | Four databases, two services, OpenAI quota | Editor + ripgrep + git |

**Where REM is stronger.** The retrieval side has genuine mechanism that commonplace lacks: parallel vector searches across two independent collections, one-hop temporal widening, and a scored rerank that weighs recency and retrieval frequency alongside similarity. The injection-prompt output is ergonomic — a consuming agent gets a ready-to-paste block with no assembly. The write path is fully automatic: send content, get enrichment and clustering for free. For high-volume user-preference capture across many lightweight sessions, this is the kind of turn-key solution commonplace does not offer.

**Where commonplace is stronger.** Knowledge has internal structure. A commonplace note holds multi-paragraph reasoning, explicit evidence, and typed links; a REM `SemanticMemory` holds a <=200-char string with a confidence float. Notes mature through editing; semantic memories are write-once (the domain struct has `Active`, `ContradictedBy`, `Superseded`, `UpdatedAt` columns but no code path updates them). Infrastructure cost is trivial. The artifacts are inspectable and version-controlled — a human or agent can read, critique, and rewrite any note directly, which cannot be done inside Qdrant payloads or Postgres rows.

**The deepest divergence** is learning granularity. REM optimizes for cheap automatic extraction at scale — one raw string in, a handful of short facts out, per agent, per burst. Commonplace optimizes for depth: fewer, richer artifacts that carry argument and evidence. These serve different populations of use cases, and picking one is a commitment about what the consuming agent needs.

## Borrowable Ideas

**Pre-formatted injection prompt as a first-class output of retrieval.** REM's `buildInjectionPrompt` delivers a text block framed with explicit delimiters, containing both episodes (context) and facts (learned patterns), each with metadata (domain, outcome, age, confidence). For commonplace, a `commonplace-context` command that assembles ranked notes into a similar fenced block would reduce load on consuming agents. *Ready to borrow as a pattern — the format is trivial; the interesting design choice is what metadata to surface.*

**Parallel retrieval across complementary collections.** REM runs Qdrant episode search and semantic memory search as goroutines and merges. For commonplace, a retrieval skill could run description-scan, tag-scan, and link-proximity passes in parallel and merge. *Reference value only — our retrieval is single-channel ripgrep; adding parallelism would need a use case.*

**Recency+frequency rerank over a similarity base.** The scoring formula `0.6*sim + 0.25*recency + 0.15*freq_bonus` is a reasonable default when all three signals are cheap. For commonplace, `last-checked` and git-log frequency could play the recency/freq roles once we have retrieval tracking. *Not yet — we do not track retrieval counts; this needs a use case first.*

**One-hop neighbor widening at retrieval time.** The pattern "find vector matches, then widen one graph hop with a score discount" is clean and simple. For commonplace, after a ripgrep hit, also surface notes that link in or out one hop with a score discount. *Worth prototyping — link graph already exists; this just needs a retrieval skill that follows links from seed hits.*

**Confidence and fact_type as part of the schema.** Even when the system lacks mechanisms to update or retire facts, attaching `confidence` and `fact_type` makes later sorting, filtering, and rerank possible. Commonplace frontmatter already carries `status`; adding an explicit confidence field for structured-claim notes would let retrieval weight claims differently. *Candidate, but requires thinking about whether confidence is meaningful when humans author the claims.*

## Curiosity Pass

**The "recursive" in Recursive Episodic Memory refers to nothing in code.** The name suggests facts consolidate into higher-order facts over multiple passes. The consolidation path runs once: raw episodes -> semantic memories. Semantic memories are never re-clustered or re-compressed. There is no loop, no recursion depth, no second-order memory. The name is aspirational.

**The "causal" in "causal episode graph" refers to nothing in code either.** The only edge types the Neo4j client creates are `FOLLOWED_BY` (temporal, per-agent) and `COMPRESSED_INTO` (provenance from episode to semantic memory — and this one is defined in `neo4j/client.go` but never called from the consolidation path; searching the write and Celery paths shows no caller). The actual Neo4j contents after a long run would be: one linear chain of `Episode` nodes per agent, no semantic memories, no causal relations.

**The forgetting policy the README marks as "first-class" does not exist.** There is no TTL on episodes, no decay on semantic memories, no code that checks the `active` or `superseded` flags anywhere after insertion, no pruning job in `celery_app.py`. The roadmap section lists "Fine-grained forgetting and redaction policies" as a future item. The README's comparison table oversells this.

**"Self-evolving memories" are write-once records with evolution columns.** The semantic memory Postgres schema has `active BOOLEAN DEFAULT TRUE`, `contradicted_by VARCHAR(36) DEFAULT ''`, `superseded BOOLEAN DEFAULT FALSE`, and an updated_at trigger. No code path ever updates these columns. No code path ever merges two facts, detects redundancy against existing facts before inserting, or marks an older fact stale when a new one contradicts it. The schema is forward-looking; the pipeline is not.

**`GetAgentGraphData` is a stub that returns empty.** The Cypher it builds looks plausible (collects all episode nodes, their outgoing edges, and linked nodes) but the function literally discards the fetched record and returns `&GraphData{Nodes: []GraphNode{}, Edges: []GraphEdge{}}` with a comment `"Minimal graph: we'll expand/normalize in Day 3+."` The dashboard's graph visualization is a feature placeholder until someone finishes that function.

**Four databases is heavy for what the system actually does.** PostgreSQL is authoritative, Qdrant is similarity, Neo4j stores a linear chain per agent (a materialized view over Postgres could replicate it), Redis is an embedding cache and job broker. Among reviewed systems, [Hindsight](./hindsight.replaced.2026-04-12.md) achieves similar retrieval behavior with pgvector on a single Postgres, and [Cognee](./cognee.md) defaults to embedded Kuzu + LanceDB + SQLite (three embedded stores, zero containers). REM's operational complexity buys clean service separation and little else; the mechanisms the extra stores enable (causal graph, self-evolving memories, forgetting) are not implemented.

**Cluster quality is bottlenecked by keyword overlap even though embeddings are free.** Both cluster implementations group by domain (7 buckets) and then do token-set intersection on intent strings. An episode with `intent="build the authentication flow"` and another with `intent="implement the login page"` would not cluster (no shared non-stop tokens), but two episodes both mentioning "typescript" would. The embeddings that are already computed and already in Qdrant could drive semantic clustering at no extra OpenAI cost; the system does not use them.

**Two parallel consolidation paths with different schemas.** `ConsolidationEngine` (invoked by the Celery task) produces facts with keys `fact, confidence, fact_type, domain`; `Compressor` (unused in the active path) produces facts with keys `content, fact_type, importance_score, outcome, confidence_score`. If someone wires the `Clusterer` + `Compressor` pair in later and the Go semantic handler does not match, writes will silently lose fields. This is a live maintenance risk.

**Benchmarks target conversational memory, not agent-memory outcomes.** The three benchmark harnesses (LongMemEval, LoCoMo, ConvoMem) measure recall from multi-turn conversations. The README pitches REM as agent infrastructure — "learn user preferences over time", "remember task outcomes" — but these benchmarks do not test that loop. There are no published scores in the repo either; `benchmarks/results/` is not committed and `run_all.py` assumes a running stack.

## Trace-derived learning placement

REM is a **service-owned trace backend** on axis 1 of the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md) and a **symbolic-artifact learner** on axis 2.

**Trace source.** Opaque content strings submitted by consuming agents via `POST /api/v1/episodes`. Unlike OpenViking (typed `role + parts` messages) or cass-memory (session-log discovery), REM accepts whatever string the agent sends and enriches it at write time via GPT-4o-mini into five fields (intent, entities, domain, emotion_signal, importance_score). Trigger boundaries are per-episode (write queues a Celery job via Redis) plus a periodic `run_scheduled_consolidation` task that enumerates agents with >=3 unconsolidated episodes.

**Extraction.** Domain bucketing (7 categories) then greedy intent-token overlap clustering (>=2 shared tokens in the engine path), then a single GPT-4o prompt per cluster asking for 1-5 "durable, reusable facts" with confidence and fact_type. No judge, no quality gate — whatever GPT-4o emits and validates as JSON becomes a semantic memory. Fact strings are capped at 200 chars; each episode is truncated to 500 chars in the prompt.

**Promotion target.** Append-only symbolic artifacts: fact strings stored in Postgres (`semantic_memories` table) and Qdrant (`semantic_memories` collection). No weight promotion, no training data export. The lifecycle columns (`active`, `contradicted_by`, `superseded`) exist but are not written.

**Scope.** Per-agent, multi-session. Each agent's episodes cluster independently; no cross-agent mining or shared knowledge store. The `user_id` FK on both tables means facts are also per-user within the agent.

**Timing.** Online post-write (Celery job fires per episode) plus offline periodic (scheduled Celery task across all agents with backlog >=3).

**Axis placement.** On axis 1 (ingestion pattern), REM sits alongside OpenViking and OpenClaw-RL as a service-owned backend, distinguished by accepting opaque strings rather than typed messages. On axis 2 (promotion target), pure artifact learning. REM reinforces the survey's finding that extraction is concrete but maintenance remains the open problem: the extraction pipeline is fully implemented (clustering, compression, embedding, storage), but the maintenance pipeline the schema anticipates (contradiction, supersession, deduplication, decay) is entirely missing. It does not split or weaken any existing survey claim, and no new subtype is warranted.

## What to Watch

- Whether the consolidation loop gains a second pass that actually justifies the "recursive" name — either clustering semantic memories into higher-order facts, or re-running over time with contradiction detection.
- Whether the embedding-based clustering path (already hinted in `Clusterer`'s comment) gets wired up, which would immediately improve cluster quality at no OpenAI cost.
- Whether `LinkEpisodeToSemantic` finally gets called and the graph gains provenance edges, enabling real graph queries beyond the linear temporal chain.
- Whether the `active` / `contradicted_by` / `superseded` columns get wired to retrieval filters and an update path — the difference between aspirational schema and an actually-evolving knowledge base.
- Whether the benchmark harness produces published numbers in `benchmarks/results/` that let REM be positioned against Mem0, Zep, or Hindsight.
- Whether the four-database footprint survives a v0.2 — the most natural simplification is PostgreSQL + pgvector with a materialized view for temporal adjacency, dropping Neo4j and shrinking the deployment.

---

Relevant Notes:

- [agentic-memory-systems-comparative-review](../agentic-memory-systems-comparative-review.md) — extends: the comparative review grounds the general retrieval-vs-knowledge-system framing, while the trace-derived survey grounds REM's placement as a service-owned artifact learner.
- [trace-derived-learning-techniques-in-related-systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: REM is a service-owned, artifact-learning trace backend whose append-only consolidation with unimplemented lifecycle columns reinforces the survey's finding that extraction is tractable but maintenance is the open problem.
- [cognee](./cognee.md) — compares: both are database-first rather than filesystem-first, but cognee runs a pipeline with Pydantic schemas and multi-tenant ACLs while REM's extraction is a keyword-clustered LLM compression into short fact strings.
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — exemplifies: REM's gap between schema (contradiction, supersession, active flags) and implementation (append-only, no merge, no retire) is a direct instance of the survey's central finding that curation resists automation even when candidate generation is solved.
- [distillation](../../notes/definitions/distillation.md) — exemplifies: consolidation is a distillation operation (episodes compressed into shorter facts under a context budget) but the transformation is shallow — a single LLM prompt asking for "durable facts" from keyword-clustered episodes, with no quality gate or revision.
