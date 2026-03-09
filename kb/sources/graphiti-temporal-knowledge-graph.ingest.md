---
description: Graph-first agent memory with bi-temporal edge invalidation — the strongest counterexample to files-first architecture in the surveyed memory systems
source_snapshot: graphiti-temporal-knowledge-graph.md
ingested: 2026-03-09
type: design-proposal
domains: [agent-memory, knowledge-graphs, temporal-data, retrieval-systems]
---

# Ingest: Graphiti: Temporal Knowledge Graph for AI Agents

Source: graphiti-temporal-knowledge-graph.md
Captured: 2026-03-05
From: https://github.com/getzep/graphiti

## Classification

Type: design-proposal — Graphiti is an open-source framework (Apache 2.0) by Zep that proposes and implements a specific architecture for agent memory: a temporally-aware knowledge graph with a defined node/edge schema, pluggable graph database backends, and an LLM-driven ingestion pipeline. It is not a paper (though an arXiv paper accompanies it), not a practitioner report (it does not narrate what worked/failed in deployment), and not a tool announcement (it is a substantial architectural design with clear trade-off rationale).

Domains: agent-memory, knowledge-graphs, temporal-data, retrieval-systems

Author: Zep (company building a commercial "context engineering platform" for AI agents). Graphiti is their open-source core. The team has production experience with enterprise conversational AI, which explains the episode-centric ingestion model. Credibility comes from the system being deployed commercially, not from academic credentials.

## Summary

Graphiti is a framework for building temporally-aware knowledge graphs that serve as memory for AI agents. Its core architectural bet is graph-first storage (Neo4j, FalkorDB, Kuzu, Neptune) where entities and relationships are first-class citizens with embeddings attached as attributes, rather than the more common vector-first approach. Its distinguishing feature is a bi-temporal model: every entity edge carries valid_at/invalid_at timestamps so contradictions are resolved through temporal invalidation rather than overwriting, enabling point-in-time queries. Data enters as "episodes" (conversation turns, JSON events, text chunks) and passes through an LLM-heavy pipeline that extracts entities, deduplicates them against existing graph nodes, extracts relationships, resolves contradictions, and runs community detection. Retrieval uses hybrid search (semantic + BM25 + graph traversal) with optional cross-encoder reranking. The system is explicitly designed for continuously streaming conversational data rather than static document corpora.

## Connections Found

The `/connect` discovery (2026-03-09) found 9 note connections and 5 source connections, rejected 6 candidates, and identified 1 synthesis opportunity.

**Strongest tension.** Graphiti directly **contradicts** [files-not-database](../notes/files-not-database.md). It is the most compelling counterexample to the files-first position because it requires graph database capabilities (temporal queries, edge invalidation, community detection) that files genuinely cannot replicate. The connection report flags this as a legitimate challenge to our KB's architectural stance.

**Comparative review grounding.** The [agentic-memory-systems-comparative-review](../notes/related-systems/agentic-memory-systems-comparative-review.md) already evaluates Graphiti across all six architectural dimensions (storage unit, agency model, link structure, temporal model, curation operations, extraction schema). The source snapshot provides the raw technical details that the review synthesises into comparative claims.

**Three-space model mapping.** Graphiti partially validates the [three-space memory taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — its EntityNodes map to semantic space, EpisodicNodes to episodic space — but has no distinct procedural/operational space. Its single-graph architecture makes it a test case for the [predicted failure modes](../notes/three-space-memory-separation-predicts-measurable-failure-modes.md) of cross-contamination when operational content is ingested alongside knowledge content. The source_type field on episodes is metadata rather than structural separation.

**Learning automation boundary.** Graphiti automates extraction, deduplication, and contradiction resolution (exemplifying [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md)), but does not automate synthesis, reformulation, or quality-gated pruning. This maps a concrete boundary of what production systems can automate today.

**Context efficiency trade-off.** The LLM-heavy pipeline (multiple calls per episode) grounds [context-efficiency-is-the-central-design-concern](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Graphiti explicitly invests context at ingestion time to save it at retrieval time.

**Retrieval-only scope.** Graphiti exemplifies [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) — it extracts entities and relationships for later retrieval but does not capture preferences, procedures, judgment precedents, or voice.

**Graph-vs-vector contrast with CrewAI.** Graphiti **contrasts** with [CrewAI Memory](../notes/related-systems/crewai-memory.md) — both are database-backed agent memory systems with LLM-driven ingestion, but they diverge on the fundamental data model. CrewAI uses a flat vector store with composite scoring and consolidation (merge/replace near-duplicates); Graphiti uses a typed knowledge graph with temporal edge invalidation (old facts survive with timestamps). The comparison illuminates the graph-vs-vector trade-off within the database-first camp.

**Sibling memory systems.** Graphiti joins a roster of surveyed agent memory systems (Mem0, A-MEM, Letta, Cognee, CrewAI, Spacebot), each making different architectural bets. Graphiti occupies the graph-first, developer-managed, temporally-explicit end of the spectrum — contrasting with Mem0 (vector-first, no temporal model), A-MEM (flat note network with evolution), CrewAI (vector-first with composite scoring), and Letta (agent self-manages memory). Cognee is the closest sibling (graph+vector with LLM extraction), but Graphiti adds bi-temporal tracking and community detection.

**Synthesis opportunity.** A note synthesising temporal models across all surveyed memory systems does not yet exist: Graphiti's bi-temporal model (valid_at/invalid_at with point-in-time queries), commonplace's git history + status field, A-MEM's timestamps with evolution, ClawVault's session timestamps with promotion-by-recurrence, and CrewAI's recency decay all represent different theories of how knowledge changes over time. The comparative review's Section 4 provides the data; the synthesis would argue what properties a good temporal model for agent memory requires and when each approach is appropriate.

**Index gaps.** The [related-systems-index](../notes/related-systems/related-systems-index.md) mentions Graphiti in paragraph text but has no dedicated Systems list entry. The [learning-theory](../notes/learning-theory.md) Memory & Architecture section references A-MEM and AgeMem but not Graphiti.

## Extractable Value

1. **Bi-temporal model as a contradiction resolution pattern.** Graphiti's valid_at/invalid_at approach to handling contradictory facts is a concrete alternative to overwriting (Mem0), evolution (A-MEM), and recency decay (CrewAI). This pattern could inform how any KB handles conflicting information over time. [experiment]

2. **The strongest counterexample to files-first.** Graphiti's graph-database dependency is not incidental — temporal queries, edge invalidation, and community detection are capabilities that genuinely require database infrastructure. This should sharpen the files-not-database argument by delineating exactly where the trade-off tips. [quick-win]

3. **Temporal model synthesis across memory systems.** With Graphiti, CrewAI, A-MEM, ClawVault, and commonplace's own git-based model now documented, there is enough material to synthesise what properties a good temporal model for agent memory requires. Each system embodies a different theory: bi-temporal tracking vs. recency decay vs. promotion-by-recurrence vs. explicit status transitions. [deep-dive]

4. **Concrete three-space test case.** Graphiti's single-graph architecture (no structural separation between knowledge and operational content) is a real system against which the three-space failure mode predictions can be evaluated. The source_type field on episodes is the closest thing to separation, and it is metadata rather than structural. [experiment]

5. **Community detection as automatic grouping.** Graphiti uses label propagation to discover entity clusters automatically. This is a different approach to the index/area organization problem — emergent grouping vs. curated indexes. Worth tracking as an alternative even if we do not adopt it. [just-a-reference]

6. **Episode-centric vs. document-centric ingestion.** Graphiti treats every piece of incoming data as an event with temporal context, not a static document. This framing matters for systems that process conversations or streaming data, and clarifies when the document-centric model (which our KB uses) is and is not appropriate. [just-a-reference]

7. **Graph-vs-vector trade-off within database-first systems.** Graphiti (typed knowledge graph) vs. CrewAI (flat vector store with composite scoring) represent two poles of how to organise agent memory when you've already committed to database infrastructure. The trade-off is expressiveness of relationships vs. simplicity of operations. [just-a-reference]

## Limitations (our opinion)

**No independent evaluation of the graph advantage.** Graphiti's documentation asserts that graph-first storage is superior to vector-first for agent memory, but provides no comparative benchmarks. The hybrid search recipes (semantic + BM25 + graph traversal) sound compelling, but there is no evidence that graph traversal actually improves retrieval quality over a well-tuned vector search with metadata filtering. The cross-encoder reranking may be doing most of the work.

**LLM-dependent extraction quality is unexamined.** The entire pipeline — entity extraction, deduplication, edge resolution, contradiction detection — relies on LLM judgment calls. No error rates, false positive/negative analyses, or human evaluation results are presented. The `SEMAPHORE_LIMIT` controls concurrency but there is no discussion of when the LLM makes wrong deduplication decisions (merging distinct entities or failing to merge identical ones). This is the same gap identified in our [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) note — production systems automate these operations without measuring whether the automation is correct.

**No evidence for temporal query utility.** The bi-temporal model is architecturally elegant, but the README provides no use cases where point-in-time queries actually changed agent behaviour or retrieval quality. "What was true on date X?" is a capability — but when does an agent actually need this? The design assumes temporal queries are valuable without demonstrating the value. Conversational AI (their stated domain) may benefit from tracking that "the user's address changed," but it is unclear whether the full bi-temporal machinery is needed versus a simpler "current/superseded" flag.

**Community detection overhead vs. utility.** Label propagation runs after every episode ingestion to update entity groupings. The source acknowledges this "adds overhead" and that "utility depends on graph density." No guidance is provided on when community detection actually helps retrieval — a sparse graph with few cross-entity paths will produce trivial communities. The feature appears designed for densely connected enterprise knowledge graphs, not general-purpose agent memory.

**Vendor context.** Graphiti is the open-source core of Zep's commercial platform. The architecture decisions (graph database requirement, LLM-heavy pipeline, MCP server integration) serve commercial positioning as much as technical merit. The supported backends (Neo4j, FalkorDB, Kuzu, Neptune) are all graph databases that Zep's enterprise customers would run — the architecture shapes the market.

## Recommended Next Action

Update [files-not-database](../notes/files-not-database.md): add a section acknowledging Graphiti as the legitimate counterexample where graph database capabilities (bi-temporal queries, edge invalidation, community detection) justify the infrastructure trade-off. The note currently references Cludebot's database stack as a counterpoint but dismisses it because its patterns "can all be implemented over files." Graphiti's temporal invalidation and community detection cannot be — and saying so sharpens the argument by delineating the actual boundary of the files-first position. This was already flagged in the prior ingest (2026-03-05) and has not yet been executed.
