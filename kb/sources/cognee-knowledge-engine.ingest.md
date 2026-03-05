---
source_snapshot: cognee-knowledge-engine.md
ingested: 2026-03-05
type: tool-announcement
domains: [agent-memory, knowledge-graphs, pipeline-architecture, LLM-extraction]
---

# Ingest: Cognee: Knowledge Engine for AI Agent Memory

Source: cognee-knowledge-engine.md
Captured: 2026-03-05
From: https://github.com/topoteretes/cognee

## Classification

Type: tool-announcement — Cognee is an open-source knowledge engine (Apache 2.0, $7.5M seed) with a companion arxiv paper. The snapshot documents its three-phase pipeline architecture, storage backends, and API surface. It reads as a system description with design analysis, not a research methodology or practitioner experience report.

Domains: agent-memory, knowledge-graphs, pipeline-architecture, LLM-extraction

Author: Topoteretes team. Funded startup ($7.5M seed) with companion research paper (arxiv:2505.24478 on KG-LLM interface optimization). The architectural choices reflect a bet on pipeline composability and schema-driven extraction as the path to production-grade agent memory.

## Summary

Cognee is a knowledge engine that transforms raw data into persistent AI memory through a three-phase pipeline: add (ingest documents), cognify (extract structure via LLM — classification, chunking, entity-relationship extraction into knowledge graph triplets, summarization, embedding), and memify (enrich the knowledge graph via rule associations and edge reweighting). Its distinctive architectural bet is pipeline-first composability — everything runs through `run_pipeline(tasks)` with sequential task execution, custom Pydantic schemas for domain-specific entity extraction, and a poly-store design where graph databases and vector stores are co-equal first-class citizens. The system supports 30+ data sources, multiple graph backends (Neo4j, FalkorDB, KuzuDB), multiple vector stores (Qdrant, Weaviate, LanceDB, pgvector), and multi-tenant dataset scoping. The memify phase is notably undersized relative to its described ambitions — current defaults handle rule associations rather than the full pruning/reweighting/strengthening capabilities described in documentation.

## Connections Found

The `/connect` discovery found 11 connections — 4 to sibling memory system sources and 7 to KB notes.

**Sibling systems (all contradicts — each makes different architectural bets):**
- [mem0-memory-layer](mem0-memory-layer.md) — Cognee explicitly positions against Mem0's "free-form facts." Mem0 is vector-first with isolated declarative facts; Cognee treats graph and vector as co-equal, building knowledge graphs with entity-relationship triplets. Different bets on the atomic unit of memory and how much structure to impose at ingestion.
- [graphiti-temporal-knowledge-graph](graphiti-temporal-knowledge-graph.md) — Both are graph-first, but Graphiti has principled bi-temporal tracking (valid_at/invalid_at) while Cognee has optional temporal_cognify without temporal invalidation. Graphiti ingests episodes incrementally; Cognee ingests documents through batch pipelines. Cognee is more schema-customizable; Graphiti has deeper temporal reasoning.
- [a-mem-agentic-memory-for-llm-agents](a-mem-agentic-memory-for-llm-agents.md) — Opposite schema philosophies: A-MEM explicitly critiques predefined schemas and uses schema-free Zettelkasten-inspired notes with embedding-based linking. Cognee embraces predefined schemas through custom Pydantic graph models. A-MEM's links are untyped embedding similarity; Cognee's are extracted subject-predicate-object triplets.
- [letta-memgpt-stateful-agents](letta-memgpt-stateful-agents.md) — Different agency models: Letta gives the agent self-managed memory (OS analogy); Cognee is developer-managed with pipeline architecture. Letta's core memory is always in context; Cognee's knowledge graph is queried on demand.

**KB notes:**
- [three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (grounds) — Cognee's architecture partially maps to the three-space model (cognify produces semantic knowledge, temporal_cognify edges toward episodic) but has no structural separation between memory types. The three-space model predicts cross-contamination when operational and durable content share the same stores.
- [three-space-memory-separation-predicts-measurable-failure-modes](../notes/three-space-memory-separation-predicts-measurable-failure-modes.md) (exemplifies) — Cognee is a concrete system with no three-space separation, making it a candidate for observing predicted failure modes (search pollution, identity scatter) as data volume grows.
- [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) (exemplifies) — Cognee's cognify pipeline automates narrow-scope operations (extraction, classification, summarization) but not synthesis, reformulation, or quality-gated pruning. Maps a concrete boundary between what automation handles and what remains open.
- [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) (exemplifies) — Cognee optimizes for retrieval accuracy (SearchType enum: GRAPH_COMPLETION, CHUNKS, GRAPH_SUMMARY_COMPLETION) rather than contextual competence. Does not capture preferences, procedures, judgment precedents, or voice.
- [files-not-database](../notes/files-not-database.md) (contradicts) — Cognee is firmly database-side (poly-store requiring Neo4j/Qdrant/PostgreSQL), though a weaker counterexample than Graphiti since the pipeline machinery could theoretically run over files with derived indexes.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (exemplifies) — Cognee's pipeline is an explicit context efficiency trade-off: invest multiple LLM calls at ingestion time (classify, extract, summarize, embed) to produce structured knowledge queryable cheaply at retrieval time.
- [distillation](../notes/distillation.md) (exemplifies) — The cognify phase is automated distillation from unstructured documents to structured graph triplets, with custom Pydantic schemas shaping the extraction target. Distillation without medium change (stays machine-readable throughout).

**Synthesis opportunity:** An agent memory comparison matrix across 5+ systems (Mem0, A-MEM, Letta, Graphiti, Cognee) is now ready to write. Cognee fills the pipeline-first, schema-driven, graph+vector hybrid position. This was independently flagged by both the Mem0 and Graphiti ingests.

## Extractable Value

1. **Pipeline-first composability as an architectural pattern for agent memory.** Cognee's `run_pipeline(tasks)` model — sequential tasks with output chaining, incremental loading, caching, batching — is the most explicitly pipeline-oriented design among the five documented memory systems. This names a distinct architectural approach: memory construction as data pipeline, not as agent behavior or API call. [just-a-reference]

2. **Custom Pydantic schemas for domain-specific entity extraction.** Cognee is the only documented system that lets you define typed graph models (e.g., `ScientificPaper` with specific fields) to control what entities and relationships the LLM extracts. This is a concrete mechanism for the "schema rigidity" dimension in the emerging comparison matrix — and a pattern potentially borrowable for structured note extraction in claws. [experiment]

3. **The memify gap: enrichment ambitions vs. implementation reality.** Cognee's memify phase promises pruning, reweighting, and strengthening of memory structures, but current defaults only handle rule associations. This is a data point for the "automating KB learning is an open problem" thesis — even well-funded systems with explicit enrichment goals ship simpler implementations than they describe. [quick-win]

4. **Three-phase separation (ingest/structure/enrich) as a memory lifecycle model.** The add/cognify/memify distinction names three phases that other systems collapse: ingestion, knowledge construction, and memory refinement. Whether these should be separate phases or a single loop is a design question worth naming. Letta collapses all three into agent behavior; Mem0 collapses construction and refinement into a single add() call. [just-a-reference]

5. **Poly-store design as the database-maximalist position.** Cognee mixes graph (Neo4j/FalkorDB/KuzuDB), vector (Qdrant/Weaviate/LanceDB/pgvector), and relational (SQLite/PostgreSQL) stores. This is the strongest counterposition to files-not-database in the documented systems — and the most infrastructure-heavy. Worth tracking whether poly-store produces capabilities that justify the operational cost. [just-a-reference]

6. **Agent memory comparison matrix is now ready to write.** Five systems documented with clear architectural dimensions. Cognee adds the pipeline-first, schema-driven position and introduces a sixth dimension (extraction schema rigidity) not present in the other four. This was independently flagged by Mem0, Graphiti, and now Cognee ingests. [deep-dive]

## Recommended Next Action

Write a note titled "Agent memory systems vary along five architectural dimensions" in `kb/notes/`, connecting to [three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md), [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md), and [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md). It would argue that five production memory systems (Mem0, A-MEM, Letta, Graphiti, Cognee) reveal a design space defined by: (1) storage unit (facts vs notes vs entities vs graph triplets), (2) agency model (external API vs self-managed vs developer pipeline), (3) link structure (none vs untyped embedding vs typed extracted), (4) temporal model (none vs optional vs bi-temporal), (5) curation operations (CRUD vs evolution vs invalidation vs enrichment), with a sixth dimension contributed by Cognee: (6) extraction schema rigidity (free-form vs generic types vs custom Pydantic schemas). This synthesis has been independently flagged by three separate ingests and has sufficient source material.
