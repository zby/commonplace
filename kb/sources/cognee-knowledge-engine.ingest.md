---
description: Pipeline-first knowledge engine with custom Pydantic schemas for LLM entity extraction, poly-store graph+vector design, and an undersized enrichment phase that concretely marks the boundary between automatable extraction and open enrichment problems
source_snapshot: cognee-knowledge-engine.md
ingested: 2026-03-09
type: tool-announcement
domains: [agent-memory, knowledge-graphs, pipeline-architecture, LLM-extraction]
---

# Ingest: Cognee: Knowledge Engine for AI Agent Memory

Source: cognee-knowledge-engine.md
Captured: 2026-03-05
From: https://github.com/topoteretes/cognee

## Classification

Type: tool-announcement — Cognee is an open-source knowledge engine (Apache 2.0, $7.5M seed) with a companion arxiv paper (2505.24478). The snapshot documents its three-phase pipeline architecture, storage backends, and API surface. It reads as a system description with design analysis, not a research methodology or practitioner experience report.

Domains: agent-memory, knowledge-graphs, pipeline-architecture, LLM-extraction

Author: Topoteretes team. Funded startup ($7.5M seed) with companion research paper on KG-LLM interface optimization. The architectural choices reflect a bet on pipeline composability and schema-driven extraction as the path to production-grade agent memory.

## Summary

Cognee is a knowledge engine that transforms raw data into persistent AI memory through a three-phase pipeline: add (ingest documents from 30+ sources), cognify (extract structure via LLM — classification, chunking, entity-relationship extraction into knowledge graph triplets, summarization, embedding), and memify (enrich the knowledge graph via rule associations and edge reweighting). Its distinctive architectural bet is pipeline-first composability — everything runs through `run_pipeline(tasks)` with sequential task execution, custom Pydantic schemas for domain-specific entity extraction, and a poly-store design where graph databases (Neo4j, FalkorDB, KuzuDB) and vector stores (Qdrant, Weaviate, LanceDB, pgvector) are co-equal first-class citizens. The memify phase is notably undersized relative to its described ambitions — current defaults handle rule associations rather than the full pruning/reweighting/strengthening capabilities described in documentation.

## Connections Found

The `/connect` discovery found 15 connections — 10 to KB notes, 4 to sibling memory system sources, and 1 to its own prior ingest report. The source is well-integrated: it is already analyzed in the [agentic-memory-systems-comparative-review](../notes/related-systems/agentic-memory-systems-comparative-review.md) across all six architectural dimensions, and the synthesis opportunity flagged during the original 2026-03-05 ingest (a comparative matrix across 5+ systems) has been realized.

**KB notes (10 connections):**

- [agentic-memory-systems-comparative-review](../notes/related-systems/agentic-memory-systems-comparative-review.md) (exemplifies) — Cognee fills the pipeline-first, schema-driven, graph+vector hybrid position across all six dimensions of the 11-system comparison. The review uses Cognee to illustrate extraction schema rigidity, the curation gap (memify ambitions vs implementation), and the developer-managed agency model.

- [files-not-database](../notes/files-not-database.md) (contradicts) — Cognee is the poly-store maximalist position (Neo4j + Qdrant + PostgreSQL), the strongest database-side counterexample to the files-first thesis. Databases are the primary substrate, not a derived layer.

- [sift-kg](../notes/related-systems/sift-kg.md) (extends) — Both are LLM-driven document-to-knowledge-graph pipelines with explicit stage boundaries, but they make opposite schema bets: sift-kg discovers schemas from corpus samples, Cognee requires custom Pydantic schemas upfront. This contrast sharpens the schema-discovery-vs-schema-definition axis. Strongest unlinked connection found.

- [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) (exemplifies) — Cognee's cognify automates narrow-scope operations (classification, chunking, entity extraction, summarization) but the memify gap concretely marks the boundary between automatable and open.

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (exemplifies) — Pipeline is an explicit context efficiency trade-off: invest multiple LLM calls at ingestion to produce structured knowledge cheaply queryable at retrieval time.

- [distillation](../notes/distillation.md) (exemplifies) — The cognify phase is automated distillation from unstructured documents to structured graph triplets, with Pydantic schemas shaping the extraction target. Distillation without medium change (stays machine-readable throughout).

- [three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (grounds) — Cognee partially maps to the three-space model (cognify produces semantic knowledge, temporal_cognify edges toward episodic) but has no structural separation between memory types.

- [three-space-memory-separation-predicts-measurable-failure-modes](../notes/three-space-memory-separation-predicts-measurable-failure-modes.md) (exemplifies) — Concrete system with no three-space separation, a candidate for observing predicted failure modes (search pollution, identity scatter) as data volume grows.

- [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) (exemplifies) — Optimizes for retrieval accuracy (SearchType enum: GRAPH_COMPLETION, CHUNKS, GRAPH_SUMMARY_COMPLETION) rather than contextual competence. Does not capture preferences, procedures, judgment precedents, or voice.

- [a-good-agentic-kb-maximizes-contextual-competence](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) (contrasts) — Knowledge is discoverable (search types, embeddings) but not composable in the KB sense (no link semantics, no claim structure, no resolution-switching) and only structurally trustworthy (schema-validated but not epistemically grounded).

**Sibling sources (4 connections, all contradicts — different architectural bets):**

- [mem0-memory-layer](mem0-memory-layer.md) — Opposite memory units: Mem0 extracts isolated declarative facts with no schema; Cognee extracts schema-driven entity-relationship triplets via custom Pydantic models.
- [graphiti-temporal-knowledge-graph](graphiti-temporal-knowledge-graph.md) — Both graph-first, but Graphiti has principled bi-temporal tracking while Cognee has optional temporal_cognify without temporal invalidation. Graphiti ingests episodes incrementally; Cognee ingests documents through batch pipelines.
- [a-mem-agentic-memory-for-llm-agents](a-mem-agentic-memory-for-llm-agents.md) — Opposite schema philosophies: A-MEM avoids predefined schemas using Zettelkasten-inspired notes; Cognee embraces custom Pydantic schemas.
- [letta-memgpt-stateful-agents](letta-memgpt-stateful-agents.md) — Different agency models: Letta gives agents self-managed memory; Cognee is developer-managed with pipeline architecture.

## Extractable Value

Based on the comparative review now being written, the focus is on what remains NEW — what the review did not already capture.

1. **Cognee vs sift-kg: schema-definition vs schema-discovery as a design axis.** Both systems solve document-to-knowledge-graph via LLM extraction with pipeline-first architecture, but Cognee requires Pydantic schemas upfront while sift-kg discovers schemas from corpus samples. This names a design choice not yet articulated as a standalone axis in the KB: whether extraction schemas should be given or learned. [quick-win]

2. **Custom Pydantic schemas as a borrowable pattern for structured note extraction.** Cognee's typed graph models (e.g., `ScientificPaper` with specific fields) control what entities and relationships the LLM extracts. This is a concrete mechanism that could inform how commonplace's `/ingest` skill structures its extraction — defining Pydantic-style schemas for what to extract from different source types. [experiment]

3. **The memify gap as evidence for the automation boundary thesis.** Cognee's memify phase promises pruning, reweighting, and strengthening of memory structures, but ships only rule associations. Even a well-funded team with explicit enrichment goals hits the same wall that [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) predicts. This data point is captured in the comparative review's curation dimension but could strengthen the automation boundary note directly. [quick-win]

4. **Pipeline-first composability vs agent-driven memory management as a concrete trade-off.** Cognee's `run_pipeline(tasks)` model is the purest example of treating memory construction as a data engineering problem rather than an agent reasoning problem. The comparative review covers this under agency models, but the trade-off — predictability and debuggability vs contextual sensitivity — deserves explicit naming. [just-a-reference]

5. **Poly-store as a complexity escalation pattern.** Cognee requires Neo4j + Qdrant + PostgreSQL (or equivalents) in production, the heaviest infrastructure among all documented systems. Worth tracking as evidence about whether capability complexity correlates with operational complexity, and whether simpler architectures (files, single vector store) achieve comparable outcomes for knowledge-management use cases. [just-a-reference]

## Limitations (our opinion)

**What is not shown:**

- **Vendor framing of the memify phase.** The documentation describes pruning, reweighting, and strengthening capabilities that the actual implementation does not deliver. The snapshot correctly notes this gap, but the marketing-to-implementation ratio should temper trust in other architectural claims that are harder to verify (e.g., "30+ data sources" — how deep is each integration?).

- **No independent evaluation of extraction quality.** The companion paper (arxiv:2505.24478) focuses on KG-LLM interface optimization, but the snapshot provides no data on extraction precision, recall, or entity resolution quality. How often does cognify produce incorrect triplets? How does quality vary across Pydantic schema complexity? These are unanswered.

- **Pipeline-first may be pipeline-only.** The architecture assumes batch document processing. There is no clear story for incremental, conversation-derived knowledge (the kind Letta and CrewAI Memory handle natively). The `temporal_cognify` mode is described but its maturity relative to the core pipeline is unclear.

- **No failure mode data at scale.** The [three-space-memory-separation-predicts-measurable-failure-modes](../notes/three-space-memory-separation-predicts-measurable-failure-modes.md) note predicts search pollution and identity scatter for systems without memory type separation. Cognee has no structural separation, but the snapshot provides no evidence about whether these failure modes manifest in practice, or at what data volume they would emerge.

- **Schema rigidity cuts both ways.** Custom Pydantic schemas are presented as a strength (domain-specific extraction), but they require upfront ontology design. [sift-kg](../notes/related-systems/sift-kg.md) demonstrates that schema discovery is a viable alternative that avoids the cold-start problem of "what entities and relationships should I define?" The snapshot does not address how users handle schema evolution as their domain understanding changes.

## Recommended Next Action

Update [sift-kg](../notes/related-systems/sift-kg.md): add a "Comparison with Cognee" subsection noting that both systems are LLM-driven document-to-knowledge-graph pipelines with explicit stage boundaries, but they make opposite schema bets (discovery vs definition). This sharpens the schema-discovery-vs-schema-definition axis that the comparative review names as a dimension but does not explore in depth. The sift-kg note already has a "Comparison with Our System" section, so adding a peer-system comparison follows the established pattern.
