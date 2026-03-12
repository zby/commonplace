# Connection Report: Cognee: Knowledge Engine for AI Agent Memory

**Source:** [Cognee: Knowledge Engine for AI Agent Memory](kb/sources/cognee-knowledge-engine.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — flagged candidates:
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — comparative analysis of 11 memory systems including Cognee
  - [related-systems-index](kb/notes/related-systems/related-systems-index.md) — master index referencing Cognee
  - [crewai-memory](kb/notes/related-systems/crewai-memory.md) — peer agent memory system
  - [sift-kg](kb/notes/related-systems/sift-kg.md) — LLM-driven document-to-knowledge-graph pipeline, very close to cognify phase
  - [siftly](kb/notes/related-systems/siftly.md) — deterministic-first enrichment pipeline, comparable pipeline architecture
  - [files-not-database](kb/notes/files-not-database.md) — Cognee makes the opposite architectural choice (database)
  - [codification](kb/notes/codification.md) — cognify phase as medium change
  - [distillation](kb/notes/distillation.md) — cognify as automated distillation
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — memify touches policy territory
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — cognify automates narrow operations only
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — pipeline as upfront context efficiency trade-off
  - [a-good-agentic-kb-maximizes-contextual-competence](kb/notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — Cognee as counterexample (retrieval-optimized, not competence-optimized)
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — Cognee has no three-space separation

**Topic indexes:**
- Read [related-systems-index](kb/notes/related-systems/related-systems-index.md) — Cognee already listed in the Systems section and mentioned in Patterns Across Systems. No additional candidates beyond index scan.
- Read [learning-theory](kb/notes/learning-theory.md) — confirmed candidates: distillation, memory architecture notes, automating-kb-learning. No new candidates.
- Read [kb-design](kb/notes/kb-design.md) — confirmed candidates: files-not-database, context-efficiency, automating-kb-learning. No new candidates.

**Semantic search:** (via qmd)
- query "knowledge graph pipeline memory agent vector hybrid entity extraction" on notes — top hits:
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) (93%) — already flagged, strong match
  - [crewai-memory](kb/notes/related-systems/crewai-memory.md) (55%) — already flagged, peer system
  - [sift-kg](kb/notes/related-systems/sift-kg.md) (47%) — already flagged, closest pipeline parallel
  - [arscontexta](kb/notes/related-systems/arscontexta.md) (46%) — peer system in memory comparison, but no direct Cognee-specific connection beyond what comparative review covers
  - [siftly](kb/notes/related-systems/siftly.md) (41%) — already flagged
  - [clawvault](kb/notes/related-systems/clawvault.md) (41%) — peer system, connection is through the comparative review
  - [a-good-agentic-kb](kb/notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) (41%) — already flagged
  - [learning-theory](kb/notes/learning-theory.md) (38%) — index, not a direct connection target
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (34%) — already flagged
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (34%) — already flagged

- query "knowledge graph pipeline memory agent vector hybrid entity extraction" on sources — top hits:
  - [cognee-knowledge-engine](kb/sources/cognee-knowledge-engine.md) (93%) — self-match
  - [cognee-knowledge-engine.ingest](kb/sources/cognee-knowledge-engine.ingest.md) (56%) — the ingest report for this same source
  - [graphiti-temporal-knowledge-graph](kb/sources/graphiti-temporal-knowledge-graph.md) (44%) — sibling system
  - [mem0-memory-layer](kb/sources/mem0-memory-layer.md) (43%) — sibling system
  - [koylanai-personal-brain-os](kb/sources/koylanai-personal-brain-os.md) (40%) — filesystem-first counterpoint
  - [a-mem-agentic-memory-for-llm-agents](kb/sources/a-mem-agentic-memory-for-llm-agents.md) (36%) — sibling system

**Keyword search:**
- grep "cognee" kb/ — found 10 files, all already in candidate set (the source itself, its ingest, mem0/graphiti/letta ingest reports, comparative review, crewai-memory, related-systems-index, sources/index, log.md)
- grep "pipeline.*architecture|poly.store|graph.*vector" kb/notes/ — no new candidates beyond already-flagged
- grep "entity.extraction|knowledge.graph|Pydantic.*schema" kb/notes/ — found [sift-kg](kb/notes/related-systems/sift-kg.md) (already flagged), others are references within already-flagged notes

**Link following:**
- From [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md): links to all sibling memory system notes and memory architecture notes — no new candidates beyond what's already covered
- From [cognee-knowledge-engine.ingest](kb/sources/cognee-knowledge-engine.ingest.md): links to 4 sibling sources + 7 KB notes — these are the connections found during the original ingest

## Connections Found

Note: The Cognee source is a `text` file (no frontmatter) in `kb/sources/`. Its ingest file (`cognee-knowledge-engine.ingest.md`) already documents 11 connections found during ingestion. The comparative review note has since been written, incorporating Cognee into the full 11-system comparison. I evaluate which connections are genuine for the source snapshot itself.

**To KB notes:**

- [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — **exemplifies**: Cognee is one of 11 systems analyzed in this comparative review and fills the pipeline-first, schema-driven, graph+vector hybrid position; the review uses Cognee's architecture to illustrate dimensions like extraction schema rigidity, curation gap (memify ambitions vs implementation), and developer-managed agency model

- [files-not-database](kb/notes/files-not-database.md) — **contradicts**: Cognee is the poly-store maximalist position (Neo4j + Qdrant + PostgreSQL), the strongest database-side counterexample to the files-first thesis; though the note argues derived indexes are the pattern, Cognee treats databases as the primary substrate, not a derived layer

- [sift-kg](kb/notes/related-systems/sift-kg.md) — **extends**: Cognee's cognify pipeline and sift-kg's extraction pipeline solve the same problem (document-to-knowledge-graph via LLM extraction) with different design bets — sift-kg uses schema discovery and human-gated entity resolution, Cognee uses custom Pydantic schemas and automated extraction; both are pipeline-first with explicit stage boundaries

- [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — **exemplifies**: Cognee's cognify automates narrow-scope operations (classification, chunking, entity extraction, summarization) but the memify gap — promising enrichment/pruning/reweighting that ships as simple rule associations — concretely marks the boundary between automatable and open

- [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **exemplifies**: Cognee's pipeline is an explicit context efficiency trade-off: invest multiple LLM calls at ingestion (classify, extract, summarize, embed) to produce structured knowledge cheaply queryable at retrieval time

- [distillation](kb/notes/distillation.md) — **exemplifies**: the cognify phase is automated distillation from unstructured documents to structured graph triplets, with Pydantic schemas shaping the extraction target; distillation without medium change (stays machine-readable throughout)

- [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — **grounds**: Cognee's architecture partially maps to the three-space model (cognify produces semantic knowledge, temporal_cognify edges toward episodic) but has no structural separation between memory types, making it a test case for the three-space thesis

- [three-space-memory-separation-predicts-measurable-failure-modes](kb/notes/three-space-memory-separation-predicts-measurable-failure-modes.md) — **exemplifies**: Cognee is a concrete system with no three-space separation, making it a candidate for observing predicted failure modes (search pollution, identity scatter) as data volume grows

- [claw-learning-is-broader-than-retrieval](kb/notes/claw-learning-is-broader-than-retrieval.md) — **exemplifies**: Cognee optimizes for retrieval accuracy (SearchType enum: GRAPH_COMPLETION, CHUNKS, GRAPH_SUMMARY_COMPLETION) rather than contextual competence; does not capture preferences, procedures, judgment precedents, or voice

- [a-good-agentic-kb-maximizes-contextual-competence](kb/notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — **contrasts**: Cognee's knowledge is discoverable (search types, embeddings) but not composable in the sense this note means (no link semantics, no claim structure, no resolution-switching) and only structurally trustworthy (schema-validated but not epistemically grounded)

**To sibling sources:**

- [mem0-memory-layer](kb/sources/mem0-memory-layer.md) — **contradicts**: opposite approaches to memory units — Mem0 extracts isolated declarative facts with no schema; Cognee extracts schema-driven entity-relationship triplets via custom Pydantic models

- [graphiti-temporal-knowledge-graph](kb/sources/graphiti-temporal-knowledge-graph.md) — **contradicts**: both graph-first but Graphiti has principled bi-temporal tracking (valid_at/invalid_at) while Cognee has optional temporal_cognify without temporal invalidation; Graphiti ingests episodes incrementally, Cognee ingests documents through batch pipelines

- [a-mem-agentic-memory-for-llm-agents](kb/sources/a-mem-agentic-memory-for-llm-agents.md) — **contradicts**: opposite schema philosophies — A-MEM explicitly avoids predefined schemas using Zettelkasten-inspired notes with embedding similarity; Cognee embraces custom Pydantic schemas

- [letta-memgpt-stateful-agents](kb/sources/letta-memgpt-stateful-agents.md) — **contradicts**: different agency models — Letta gives agents self-managed memory; Cognee is developer-managed with pipeline architecture

**To its own ingest:**

- [cognee-knowledge-engine.ingest](kb/sources/cognee-knowledge-engine.ingest.md) — **grounds**: the ingest report analyzes the source snapshot's architectural decisions, classifies it, and documents extractable value

**Bidirectional candidates** (reverse link also worth adding):

- [sift-kg](kb/notes/related-systems/sift-kg.md) <-> source — both directions useful: sift-kg's review would benefit from noting Cognee as a parallel pipeline approach with different schema design (custom Pydantic vs discovered schema), and the comparison sharpens the schema-discovery-vs-schema-definition axis
- [crewai-memory](kb/notes/related-systems/crewai-memory.md) <-> source — CrewAI Memory already references Cognee through the comparative review; a direct link adds nothing the review doesn't already provide

## Rejected Candidates

- [codification](kb/notes/codification.md) — while Cognee's cognify phase changes representation (text -> graph), it does not cross a medium boundary in the codification sense (natural language -> executable code). The output stays machine-readable data, not a different verification regime. The ingest report correctly labels this as distillation, not codification.

- [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — Cognee's memify phase is about graph enrichment operations, not about learning a policy for when to use memory operations (which is AgeMem's contribution). The connection is too indirect.

- [siftly](kb/notes/related-systems/siftly.md) — both have pipeline architectures, but Siftly is a bookmark ingestion system with deterministic-first enrichment for a narrow artifact type. The pipeline parallel is real but generic (all data processing uses pipelines). No specific architectural insight flows from comparing them.

- [arscontexta](kb/notes/related-systems/arscontexta.md) — Ars Contexta's 6 Rs pipeline is superficially similar to Cognee's add/cognify/memify, but they operate at different levels (knowledge management methodology vs. data processing pipeline). The connection exists only through the comparative review.

- [clawvault](kb/notes/related-systems/clawvault.md) — connection is only through the comparative review; no direct architectural overlap with Cognee's pipeline-first approach.

- [constraining](kb/notes/constraining.md) — Cognee's pipeline doesn't narrow interpretation of underspecified instructions; it processes data. The term constraining as defined in this KB does not describe what Cognee does.

## Index Membership

- [related-systems-index](kb/notes/related-systems/related-systems-index.md) — Cognee is already listed in the Systems section (lightweight coverage via ingest report)
- [sources/index.md](kb/sources/index.md) — already listed
- Already referenced by: [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) which is the main analytical coverage

## Synthesis Opportunities

**None new.** The synthesis opportunity flagged in the Cognee ingest report — an agent memory comparison matrix across 5+ systems — has already been realized as [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md), which covers all 11 systems including Cognee across six architectural dimensions.

## Flags

- **Coverage gap:** The Cognee source snapshot (`cognee-knowledge-engine.md`) is a `text` file with no frontmatter. It has an ingest report but no full review note in `kb/notes/related-systems/`. The related-systems-index notes that "Database-backed memory systems (Mem0, Graphiti, Cognee, Letta, A-MEM, AgeMem) currently have only lightweight coverage via ingest reports in `kb/sources/`." If deeper coverage is desired, a full review note like those written for sift-kg or CrewAI Memory would be the next step.

- **Existing coverage is strong.** The ingest report already documents 11 connections with well-articulated relationship semantics, and the comparative review integrates Cognee's architecture across all six analytical dimensions. The source is well-connected despite being lightweight-tier coverage.
