# Connection Report: Graphiti: Temporal Knowledge Graph for AI Agents

**Source:** [Graphiti: Temporal Knowledge Graph for AI Agents](kb/sources/graphiti-temporal-knowledge-graph.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (145 entries) — flagged candidates:
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — already mentions Graphiti by name across all six dimensions
  - [related-systems-index](kb/notes/related-systems/related-systems-index.md) — mentions Graphiti in paragraph text but has no dedicated entry
  - [files-not-database](kb/notes/files-not-database.md) — Graphiti requires graph database infrastructure, directly challenges files-first thesis
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — Graphiti automates extraction/dedup/resolution, maps the automation boundary
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Graphiti's ingestion-time LLM investment is the trade-off this note describes
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — EntityNode = semantic, EpisodicNode = episodic, no procedural space
  - [three-space-memory-separation-predicts-measurable-failure-modes](kb/notes/three-space-memory-separation-predicts-measurable-failure-modes.md) — Graphiti's single graph is a test case for cross-contamination predictions
  - [claw-learning-is-broader-than-retrieval](kb/notes/claw-learning-is-broader-than-retrieval.md) — Graphiti is retrieval-only, no action capacity
  - [ephemeral-computation-prevents-accumulation](kb/notes/ephemeral-computation-prevents-accumulation.md) — Graphiti is maximally accumulating, opposite of ephemeral
  - [sift-kg](kb/notes/related-systems/sift-kg.md) — both are LLM-driven knowledge graph systems with entity extraction and deduplication
  - [crewai-memory](kb/notes/related-systems/crewai-memory.md) — both are database-backed agent memory systems; diverge on graph vs vector
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — Graphiti has hardcoded curation policy (extract/dedup/invalidate) not learned
  - [learning-theory](kb/notes/learning-theory.md) — Graphiti's temporal model is a concrete memory architecture reference

- Read kb/sources/index.md — flagged candidates:
  - [graphiti-temporal-knowledge-graph.ingest.md](kb/sources/graphiti-temporal-knowledge-graph.ingest.md) — the ingest report already done for this source
  - [mem0-memory-layer.md](kb/sources/mem0-memory-layer.md) — sibling: vector-first, no temporal model (opposite end of spectrum)
  - [letta-memgpt-stateful-agents.md](kb/sources/letta-memgpt-stateful-agents.md) — sibling: agent-self-managed memory (different agency model)
  - [cognee-knowledge-engine.md](kb/sources/cognee-knowledge-engine.md) — sibling: pipeline-first graph+vector poly-store (closest architecture)
  - [a-mem-agentic-memory-for-llm-agents.md](kb/sources/a-mem-agentic-memory-for-llm-agents.md) — sibling: flat note network (different storage unit)
  - [spacedriveapp-spacebot-ai-agent.md](kb/sources/spacedriveapp-spacebot-ai-agent.md) — sibling: typed-edge graph memory (simpler version of Graphiti's graph)

**Topic indexes:**
- Read [related-systems-index](kb/notes/related-systems/related-systems-index.md) — confirmed: Graphiti is mentioned in body text (two-tier coverage paragraph) but has no dedicated Systems list entry. No additional candidates found beyond index scan.
- Read [learning-theory](kb/notes/learning-theory.md) — additional candidate: [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (already flagged). The Memory & Architecture section lists three-space notes and A-MEM but does not reference the Graphiti source.

**Semantic search:** (via qmd)
- query "temporal knowledge graph agent memory entity resolution deduplication" on notes — top hits:
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) (93%) — strong, already flagged
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (54%) — already flagged
  - [related-systems-index](kb/notes/related-systems/related-systems-index.md) (45%) — already flagged
  - [llm-context-is-a-homoiconic-medium](kb/notes/llm-context-is-a-homoiconic-medium.md) (38%) — skip, surface vocabulary overlap only (both discuss "medium" but mean different things)
  - [crewai-memory](kb/notes/related-systems/crewai-memory.md) (34%) — already flagged
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) (34%) — already flagged
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (33%) — already flagged
  - [notes-need-quality-scores-to-scale-curation](kb/notes/notes-need-quality-scores-to-scale-curation.md) (33%) — weak, about note scoring not knowledge graph scoring
  - Remaining hits below 33% — no new candidates

- query "temporal knowledge graph agent memory entity resolution deduplication" on sources — top hits:
  - [graphiti-temporal-knowledge-graph.ingest.md](kb/sources/graphiti-temporal-knowledge-graph.ingest.md) (93%) — self
  - [graphiti-temporal-knowledge-graph.md](kb/sources/graphiti-temporal-knowledge-graph.md) (55%) — target itself
  - [mem0-memory-layer.ingest.md](kb/sources/mem0-memory-layer.ingest.md) (44%) — already flagged
  - [a-mem-agentic-memory-for-llm-agents.md](kb/sources/a-mem-agentic-memory-for-llm-agents.md) (42%) — already flagged
  - [mem0-memory-layer.md](kb/sources/mem0-memory-layer.md) (38%) — already flagged
  - [cognee-knowledge-engine.md](kb/sources/cognee-knowledge-engine.md) (37%) — already flagged

- query "graph-first architecture hybrid search community detection incremental updates" on notes — top hits:
  - [link-graph-plus-timestamps-enables-make-like-staleness-detection](kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) (88%) — skip, about KB link graph staleness, not knowledge graphs; surface vocabulary overlap ("graph + timestamps")
  - [siftly](kb/notes/related-systems/siftly.md) (44%) — weak, SQLite-based ingestion, different architecture
  - [sift-kg](kb/notes/related-systems/sift-kg.md) (36%) — already flagged

**Keyword search:**
- grep "graphiti" kb/ — found 11 files. Confirmed all relevant matches are already in candidate set. Most references are in the comparative review, ingest, and sibling source ingests.

## Connections Found

### Notes

- [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — **grounds**: the comparative review is the primary analytical note that evaluates Graphiti across all six architectural dimensions (storage unit, agency model, link structure, temporal model, curation operations, extraction schema); the source snapshot provides the raw technical details that the review synthesises into comparative claims

- [files-not-database](kb/notes/files-not-database.md) — **contradicts**: Graphiti is the strongest counterexample to the files-first thesis in the KB, because its core capabilities (bi-temporal queries, edge invalidation, community detection, graph traversal) genuinely require database infrastructure and cannot be replicated over flat files. The ingest report already identifies this as the most important connection.

- [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — **partially exemplifies**: EntityNodes map to semantic space (knowledge), EpisodicNodes map to episodic space (experience), but Graphiti has no distinct procedural/operational space. The single-graph architecture makes it a test case for whether the three-space separation matters.

- [three-space-memory-separation-predicts-measurable-failure-modes](kb/notes/three-space-memory-separation-predicts-measurable-failure-modes.md) — **enables**: Graphiti's single-graph design (no structural separation between knowledge and operational content) is a concrete system against which the predicted cross-contamination failure modes could be tested. The `source_type` field on episodes is metadata rather than structural separation.

- [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — **exemplifies**: Graphiti automates extraction, deduplication, and contradiction resolution (three of the "boiling cauldron" mutations) but does not automate synthesis, reformulation, or quality-gated pruning. This maps a concrete boundary: production systems can automate the narrow-scope operations but not the judgment-heavy ones.

- [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **exemplifies**: Graphiti's LLM-heavy ingestion pipeline (multiple calls per episode for extraction, deduplication, resolution) is an explicit instance of investing context at ingestion time to reduce it at retrieval time — the context efficiency trade-off between upfront and downstream cost.

- [claw-learning-is-broader-than-retrieval](kb/notes/claw-learning-is-broader-than-retrieval.md) — **exemplifies**: Graphiti extracts entities and relationships for retrieval but captures no preferences, procedures, judgment precedents, or voice. It demonstrates a retrieval-optimised system that does not address the broader action-capacity learning this note argues is needed.

- [sift-kg](kb/notes/related-systems/sift-kg.md) — **extends**: both are LLM-driven knowledge graph systems with entity extraction and deduplication, but Graphiti adds temporal tracking (valid_at/invalid_at), episode-centric streaming ingestion, community detection, and graph database infrastructure. sift-kg is batch/document-oriented with human-gated entity resolution; Graphiti is streaming/episode-oriented with automated resolution. The contrast clarifies when batch vs streaming graph construction is appropriate.

- [crewai-memory](kb/notes/related-systems/crewai-memory.md) — **contrasts**: both are database-backed agent memory systems with LLM-driven ingestion, but they diverge on the fundamental data model. CrewAI uses a flat vector store with composite scoring; Graphiti uses a typed knowledge graph with temporal edges. CrewAI's consolidation (merge/replace near-duplicates) is structurally simpler than Graphiti's temporal invalidation (old facts survive with timestamps). The comparison illuminates the graph-vs-vector trade-off within the database-first camp.

**Bidirectional candidates** (reverse link also worth adding):
- [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) <-> source — bidirectional: the review already references Graphiti extensively; the source provides the detailed technical architecture that grounds the review's dimensional analysis
- [files-not-database](kb/notes/files-not-database.md) <-> source — bidirectional: the source is the counterexample the note should acknowledge; the note provides the thesis the source challenges

### Sources

- [graphiti-temporal-knowledge-graph.ingest.md](kb/sources/graphiti-temporal-knowledge-graph.ingest.md) — **extends**: the ingest report analyses the source snapshot, identifying 13 connections, extractable value, and recommended next actions. The source snapshot provides the raw architecture details the ingest synthesises.

- [mem0-memory-layer.md](kb/sources/mem0-memory-layer.md) — **contrasts**: opposite ends of the agent memory spectrum. Mem0 is vector-first with no temporal model; Graphiti is graph-first with bi-temporal tracking. Mem0 overwrites on contradiction; Graphiti invalidates with timestamps.

- [cognee-knowledge-engine.md](kb/sources/cognee-knowledge-engine.md) — **extends**: closest architectural sibling. Both use graph+vector approaches with LLM extraction pipelines. Graphiti adds bi-temporal tracking and community detection; Cognee uses Pydantic schemas for domain-customisable extraction. Both require database infrastructure.

- [letta-memgpt-stateful-agents.md](kb/sources/letta-memgpt-stateful-agents.md) — **contrasts**: different agency models. Graphiti is developer-managed (external service handles memory); Letta is agent-self-managed (agent decides what to write/archive). The ingest notes that Letta is converging toward git-backed memory, moving away from database-first.

- [a-mem-agentic-memory-for-llm-agents.md](kb/sources/a-mem-agentic-memory-for-llm-agents.md) — **contrasts**: different storage units and link models. A-MEM uses flat seven-field notes with untyped embedding-similarity links; Graphiti uses typed entity nodes and relationship edges in a property graph. A-MEM's memory evolution (updating neighbouring notes) has no equivalent in Graphiti.

## Rejected Candidates

- [llm-context-is-a-homoiconic-medium](kb/notes/llm-context-is-a-homoiconic-medium.md) — qmd returned at 38%; surface vocabulary overlap ("medium" appears in both). The notes are about fundamentally different things: Graphiti is a storage/retrieval system, homoiconicity is about the nature of LLM context. No genuine conceptual connection.

- [link-graph-plus-timestamps-enables-make-like-staleness-detection](kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — qmd returned at 88% on second query; high score due to "graph + timestamps" vocabulary overlap. But this note is about detecting staleness in the KB's own link graph using file modification timestamps, not about temporal knowledge graphs for agent memory. The mechanisms are entirely different.

- [notes-need-quality-scores-to-scale-curation](kb/notes/notes-need-quality-scores-to-scale-curation.md) — qmd returned at 33%; both involve scoring/filtering but Graphiti scores for retrieval relevance while this note scores for curation priority. The connection is too abstract to be useful for an agent following the link.

- [ephemeral-computation-prevents-accumulation](kb/notes/ephemeral-computation-prevents-accumulation.md) — Graphiti is maximally accumulating (nothing is discarded, old facts are invalidated but preserved). This makes it the opposite of ephemeral computation, but the opposition is too obvious to add navigational value. An agent reading about ephemeral computation does not gain insight from being pointed at a database-backed knowledge graph.

- [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — Graphiti has a hardcoded curation policy (extract, deduplicate, invalidate) rather than a learned one. The contrast with AgeMem's RL-trained policy is interesting but the connection between the source and this note is indirect — it would need to go through the comparative review rather than being a direct link.

- [siftly](kb/notes/related-systems/siftly.md) — both are ingestion systems, but Siftly processes social media bookmarks into SQLite while Graphiti processes episodes into a knowledge graph. The architectures are too different for a useful comparison; sift-kg is the more relevant sibling.

## Index Membership

- [related-systems-index](kb/notes/related-systems/related-systems-index.md) — Graphiti is mentioned in the two-tier coverage paragraph but has no dedicated entry in the Systems list. It should have a lightweight entry pointing to the ingest report, consistent with how Fintool is listed.
- [learning-theory](kb/notes/learning-theory.md) — the Memory & Architecture section references A-MEM and AgeMem sources but not Graphiti. Graphiti's bi-temporal model is the strongest concrete temporal memory architecture in the surveyed systems and should be referenced as a sibling to the other memory system sources.

## Synthesis Opportunities

**Temporal models across memory systems.** Graphiti's bi-temporal model (valid_at/invalid_at with point-in-time queries), commonplace's git history + status field, A-MEM's timestamps with evolution, ClawVault's session timestamps with promotion-by-recurrence, and CrewAI's recency decay all represent different theories of how knowledge changes over time. No note synthesises across these approaches to identify what a good temporal model for agent memory would look like. The comparative review's Section 4 (temporal model) provides the data; the synthesis would argue what properties a temporal model must have and when each approach is appropriate.

## Flags

- The [related-systems-index](kb/notes/related-systems/related-systems-index.md) mentions Graphiti in paragraph text but has no Systems list entry — inconsistent with how other lightweight-coverage systems (Fintool) are listed. (Already noted in log.md for Mem0 and Letta, same issue applies to Graphiti.)
- The [graphiti-temporal-knowledge-graph.ingest.md](kb/sources/graphiti-temporal-knowledge-graph.ingest.md) recommended next action (update files-not-database to acknowledge Graphiti as legitimate counterexample) has not been executed.
