---
source_snapshot: graphiti-temporal-knowledge-graph.md
ingested: 2026-03-05
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

The `/connect` discovery found 13 connections (5 sibling source systems, 8 KB notes) and rejected 5 candidates. The key findings:

**Sibling memory systems.** Graphiti joins a growing roster of surveyed agent memory systems (Mem0, A-MEM, Letta, Cognee, Cludebot, Spacebot), each making different architectural bets. Graphiti occupies the graph-first, developer-managed, temporally-explicit end of the spectrum — contradicting Mem0 (vector-first, no temporal model), A-MEM (flat note network with evolution), and Letta (agent self-manages memory). It extends Spacebot's simpler typed-edge graph memory with principled temporal tracking.

**Strongest tension.** Graphiti directly contradicts [files-not-database](../notes/files-not-database.md). It is the most compelling counterexample to the files-first position because it requires graph database capabilities (temporal queries, edge invalidation, community detection) that files genuinely cannot replicate. The connection report flags this as a legitimate challenge to our KB's architectural stance.

**Three-space model mapping.** Graphiti partially validates the [three-space memory taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — its EntityNodes map to semantic space, EpisodicNodes to episodic space — but has no distinct procedural/operational space. This makes it a test case for the [predicted failure modes](../notes/three-space-memory-separation-predicts-measurable-failure-modes.md) of cross-contamination when operational content is ingested alongside knowledge content.

**Learning automation boundary.** Graphiti automates extraction, deduplication, and contradiction resolution (exemplifying [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md)), but does not automate synthesis, reformulation, or quality-gated pruning. This maps a concrete boundary of what production systems can automate today.

**Context efficiency trade-off.** The LLM-heavy pipeline (multiple calls per episode) grounds [context-efficiency-is-the-central-design-concern](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Graphiti explicitly invests context at ingestion time to save it at retrieval time.

**Retrieval-only scope.** Graphiti exemplifies [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) — it extracts entities and relationships for later retrieval but does not capture preferences, procedures, judgment precedents, or voice.

**Synthesis opportunity flagged.** An agent memory comparison matrix across 7 systems and 5 architectural dimensions (storage model, agency, temporal model, curation operations, link structure) was identified as a high-value note that would connect three existing KB notes through the lens of production system comparisons.

## Extractable Value

1. **Bi-temporal model as a contradiction resolution pattern.** Graphiti's valid_at/invalid_at approach to handling contradictory facts is a concrete alternative to overwriting (Mem0) or evolution (A-MEM). This pattern could inform how any KB handles conflicting information over time. [experiment]

2. **The strongest counterexample to files-first.** Graphiti's graph-database dependency is not incidental — temporal queries, edge invalidation, and community detection are capabilities that genuinely require database infrastructure. This should sharpen the files-not-database argument by delineating exactly where the trade-off tips. [quick-win]

3. **Agent memory comparison matrix.** With seven systems now surveyed across five clear architectural dimensions, there is enough material to write a structured comparison note. This was already flagged in the Mem0 ingestion and Graphiti completes the picture. [deep-dive]

4. **Concrete three-space test case.** Graphiti's single-graph architecture (no structural separation between knowledge and operational content) is a real system against which the three-space failure mode predictions can be evaluated. The source_type field on episodes is the closest thing to separation, and it is metadata rather than structural. [experiment]

5. **Community detection as automatic grouping.** Graphiti uses label propagation to discover entity clusters automatically. This is a different approach to the index/area organization problem — emergent grouping vs. curated indexes. Worth tracking as an alternative even if we do not adopt it. [just-a-reference]

6. **Episode-centric ingestion vs. document-centric ingestion.** Graphiti's design treats every piece of incoming data as an event with temporal context, not a static document. This framing matters for systems that process conversations or streaming data, and clarifies when the document-centric model (which our KB uses) is and is not appropriate. [just-a-reference]

## Recommended Next Action

Update [files-not-database](../notes/files-not-database.md): add a section acknowledging Graphiti as the legitimate counterexample where graph database capabilities (bi-temporal queries, edge invalidation, community detection) justify the infrastructure trade-off. The note currently references Cludebot's database stack as a counterpoint but dismisses it because its patterns "can all be implemented over files." Graphiti's temporal invalidation and community detection cannot be — and saying so sharpens the argument by delineating the actual boundary of the files-first position.
