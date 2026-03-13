---
description: Pipeline-first knowledge engine (add/cognify/memify/search) with Pydantic-schema graph extraction, poly-store backends, and multi-tenancy — the strongest database-side counterexample to files-first architecture, but treats knowledge as a data engineering problem rather than a curation problem
type: note
areas: [related-systems]
status: current
last-checked: 2026-03-13
---

# Cognee

A knowledge engine that transforms raw data into persistent AI memory through a pipeline architecture. Built by Topoteretes ($7.5M seed, Apache 2.0), cognee occupies the pipeline-first, schema-driven, graph+vector hybrid position in the agent memory landscape. Among reviewed systems, it is the purest example of treating memory construction as a data engineering problem — predictable, composable, debuggable — rather than an agent reasoning problem or a curation problem.

**Repository:** https://github.com/topoteretes/cognee

## Core Ideas

**Pipeline-first composability.** Everything runs through `run_pipeline(tasks)`. A `Task` wraps a callable (async function, generator, or sync function) with batch-size configuration. Tasks chain sequentially: each receives the previous task's output. The default cognify pipeline chains five tasks: classify documents → extract chunks → extract graph → summarise → add data points. Custom pipelines compose the same way — swap in a different chunker, add an ontology validator, change the graph model. The pipeline is aware of user permissions and dataset isolation, setting context variables at pipeline start to scope all database operations. This makes the processing deterministic and inspectable, at the cost of flexibility: the model cannot adapt mid-pipeline to what it discovers.

**Schema-driven entity extraction via Pydantic.** The `DataPoint` base class (Pydantic model with UUID, versioning, timestamps, provenance, and embeddable field declarations) is the atom of the system. Custom graph models extend `DataPoint` — e.g., a `ScientificPaper` with typed fields for authors, methods, findings. At cognify time, the LLM receives the Pydantic schema and extracts structured entities matching it, using the Instructor library for structured output. The default schema (`KnowledgeGraph` with `Node` and `Edge` lists) extracts generic entities and relationships. The schema shapes what the LLM can see — a genuinely useful constraining mechanism, but one that requires upfront ontology design. [sift-kg](./sift-kg.md) demonstrates the alternative: discover schemas from corpus samples rather than defining them.

**Poly-store with pluggable backends.** Three database layers (graph, vector, relational), each behind an abstract interface, mixed and matched at deployment:
- **Graph:** Kuzu (default, embedded), Neo4j, Neptune, NetworkX (prototype)
- **Vector:** LanceDB (default), ChromaDB, PGVector, Qdrant, Weaviate, Milvus
- **Relational:** SQLite (default), PostgreSQL

The interfaces (`GraphDBInterface`, `VectorDBInterface`) are genuinely abstract — switching backends requires only configuration, not code changes. This is the heaviest infrastructure among all reviewed systems, and the strongest counterexample to [files-not-database](../files-not-database.md). Databases are the primary substrate, not a derived layer.

**Multi-tenancy as first-class concern.** User-scoped datasets with ACL (read/write/delete/share), tenant-level isolation, and per-request context variables that scope all database operations. This is deeply integrated — pipeline execution checks permissions, search filters by ACL, missing permissions silently return empty results. Among reviewed systems, only [SAGE](./sage.md) has comparably structured access control (though SAGE uses cryptographic gates rather than relational ACLs).

**Fourteen search types spanning a wide retrieval spectrum.** The `SearchType` enum includes: GRAPH_COMPLETION (default — graph traversal + LLM reasoning), RAG_COMPLETION (traditional RAG), CHUNKS (pure vector similarity), TRIPLET_COMPLETION, GRAPH_SUMMARY_COMPLETION, GRAPH_COMPLETION_COT (chain-of-thought), CYPHER (raw graph queries), NATURAL_LANGUAGE (NL→Cypher), TEMPORAL, CHUNKS_LEXICAL (Jaccard), CODING_RULES, FEELING_LUCKY (auto-select), and two context extension variants. All retrievers implement a three-step pipeline: fetch from DB → format context → LLM completion. The breadth is impressive on paper; whether most are used in practice or GRAPH_COMPLETION dominates is unclear.

**Undersized enrichment phase.** Memify — the post-processing phase that should prune stale nodes, strengthen frequent connections, and reweight edges — ships three tasks: consolidate entity descriptions, create triplet embeddings, and persist conversation sessions. The documentation describes pruning/reweighting/strengthening capabilities that the code does not deliver. This gap is the most revealing data point in the system: even a well-funded team with explicit enrichment goals hits the same wall that [automating KB learning is an open problem](../automating-kb-learning-is-an-open-problem.md) predicts. Extraction is automatable; curation is not (yet).

**MCP server and distributed mode.** The MCP server (`cognee-mcp/`) exposes the full pipeline as tools via FastMCP — add, cognify, search, memify, delete, visualise. This makes cognee usable as a memory backend for any MCP-compatible agent. The distributed mode (`distributed/`) uses Modal for offloading expensive database writes to dedicated workers via task queues — meaningful for production scale.

**Provenance tracking.** Every `DataPoint` records `source_pipeline`, `source_task`, `source_node_set`, and `source_user`. This is built into the base class, not bolted on — all graph nodes are traceable to their origin. Among reviewed systems, this is the strongest provenance model. Our system tracks provenance through git history and source citations, which is equivalent in capability but different in mechanism.

## Comparison with Our System

| Dimension | Cognee | Commonplace |
|---|---|---|
| Storage | Poly-store (graph + vector + relational) with pluggable backends | Markdown files in git |
| Knowledge unit | DataPoint (Pydantic model) with embeddings and graph edges | Typed note with frontmatter, prose body, and semantic links |
| Entity modeling | LLM extraction with Pydantic schemas (automated) | Manual note authoring with type templates (human+agent) |
| Link structure | Subject-predicate-object triplets; relationship types constrained by extraction schema | Markdown links with articulated relationship semantics (extends, grounds, contradicts) |
| Search | 14 search types: graph traversal, vector similarity, LLM completion, Cypher, temporal | Structured grep + semantic search + area indexes + description scanning |
| Knowledge evolution | Versioned DataPoints with timestamps; no maturation path | Status field (seedling → current → superseded), type transitions (text → note → structured-claim) |
| Context engineering | None — builds memory infrastructure for other agents to use | Core concern — routing, loading, scoping, maintenance for bounded context |
| Learning theory | None explicit | Constraining, distillation, codification framework |
| Agency model | Developer-managed pipeline | Human+agent collaborative |
| Multi-tenancy | First-class with ACLs, tenant isolation, per-request scoping | Single-user (agent per session) |
| Curation | Memify phase (undersized) | Manual connection, progressive formalization, link articulation |
| Provenance | Built into DataPoint base class (pipeline, task, user) | Git history + explicit source citations |

**Where cognee is stronger.** Multi-tenancy is deeply integrated where we have none. The poly-store gives genuine retrieval flexibility — graph traversal, vector similarity, and lexical search are co-equal citizens. Pipeline composability makes processing predictable and debuggable. The MCP server makes cognee immediately usable as a memory backend for any agent. Provenance is structural (every node knows its origin) rather than reconstructed (git blame).

**Where commonplace is stronger.** Knowledge has a lifecycle — notes mature through status transitions, link semantics articulate *why* notes relate (not just that they do), descriptions serve as retrieval filters for agents deciding what to load. Cognee's triplets carry relationship types but these are extracted automatically without the elaborative encoding that produces [navigable connections](../links.md). Our [progressive disclosure](../agents-navigate-by-deciding-what-to-read-next.md) addresses [context efficiency](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) proactively rather than building infrastructure for efficient retrieval after the fact. Most importantly: cognee automates extraction but has no story for curation, synthesis, or knowledge maturation — the operations that make a knowledge base improve over time rather than just grow.

**The deepest divergence** is what "knowledge" means. Cognee treats knowledge as structured data extracted from documents — triplets, entities, embeddings — optimised for retrieval accuracy. Commonplace treats knowledge as claims with evidence, linked by articulated relationships, optimised for [contextual competence](../a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — the ability to act well, not just find things. This is the same split the [comparative review](./agentic-memory-systems-comparative-review.md) identifies: the difference between a search index and a knowledge system.

## Borrowable Ideas

**Pydantic schemas for extraction shaping.** Cognee's pattern — define a typed schema, pass it to the LLM, get structured output matching the schema — is a borrowable constraining mechanism. For commonplace, this could inform how `/ingest` structures its extraction: rather than free-form analysis, define what to extract per source type (claims from papers, practices from practitioner reports, patterns from tool announcements). The Instructor library integration is a concrete implementation path. *Needs a use case first — current ingest quality is acceptable, and adding schema rigidity risks losing the curiosity-driven value extraction that makes ingests useful.*

**Provenance as a first-class field.** Every DataPoint knowing its `source_pipeline` and `source_task` is cleaner than reconstructing provenance from git history. For commonplace, frontmatter fields like `created-by: ingest` or `created-by: connect` would make artifact lineage queryable without git. *Ready to borrow — low cost, high information value.*

**Ontology grounding for entity validation.** Cognee's optional ontology resolver validates extracted entities against an OWL ontology using fuzzy matching. For knowledge systems, this pattern generalises: validate new knowledge against existing knowledge at write time, not just at search time. Our `/connect` skill does something analogous (find related notes before writing), but cognee's mechanism is more structural — the validation is programmatic, not judgment-based. *Just a reference — our system validates through link articulation, which is more expensive but produces higher-quality connections.*

**MCP as a universal memory interface.** Exposing add/cognify/search/memify as MCP tools makes cognee usable as a backend for any agent. If commonplace exposed its operations (search, read, connect, ingest) as MCP tools, it could serve as a knowledge backend for agents outside the Claude Code harness. *Needs a use case first — currently single-harness.*

## Curiosity Pass

**Does the graph actually improve retrieval over plain vector search?** The system offers both GRAPH_COMPLETION and CHUNKS search types, but the codebase provides no evidence that graph-augmented retrieval outperforms vector-only retrieval. The GraphCompletionRetriever uses `brute_force_triplet_search()` — the name itself reveals the graph traversal is unsophisticated. The companion paper (arxiv:2505.24478) focuses on KG-LLM interface optimisation but the repo has no A/B comparison showing the graph's marginal value. This matters because the graph infrastructure (Kuzu/Neo4j, entity extraction, edge management) is the system's heaviest cost. If CHUNKS retrieval achieves 90% of GRAPH_COMPLETION quality, the graph is expensive decoration.

**The "ECL" framing relocates rather than transforms.** Cognee brands its pipeline as "ECL" (Extract, Cognify, Load) replacing traditional RAG. But mechanistically: Extract chunks text (standard), Cognify calls an LLM to produce triplets from chunks (standard extraction), Load stores in databases (standard). The Pydantic schema is the only genuinely novel mechanism — it constrains what the LLM extracts. The rest is a well-engineered but standard document-to-graph pipeline. The claimed transformation (raw data → "AI memory") is naming the output differently, not processing it differently.

**Pipeline-first is pipeline-only.** The architecture assumes batch document processing. There is no clear mechanism for incremental, conversation-derived knowledge — the kind agents generate during work. Letta handles this natively (the agent writes to its own memory mid-conversation). ClawVault handles this through observation capture. Cognee's `persist_sessions_in_knowledge_graph` task in memify is the closest equivalent, but it stores session transcripts as graph nodes rather than extracting knowledge from them. For an "AI memory" system, the inability to learn from conversations is a notable gap.

**Fourteen search types suggest unclear product focus.** When a system offers GRAPH_COMPLETION, GRAPH_SUMMARY_COMPLETION, GRAPH_COMPLETION_COT, GRAPH_COMPLETION_CONTEXT_EXTENSION, RAG_COMPLETION, CHUNKS, CHUNKS_LEXICAL, TRIPLET_COMPLETION, SUMMARIES, CYPHER, NATURAL_LANGUAGE, TEMPORAL, CODING_RULES, and FEELING_LUCKY — it's either serving very diverse use cases or hasn't converged on what works. The FEELING_LUCKY type (auto-select) suggests even the developers aren't sure which to recommend. Compare with Graphiti (one search API with configurable parameters) or commonplace (grep + semantic search + index browsing, each for a clear purpose).

## What to Watch

- Whether memify matures into genuine curation — pruning, contradiction detection, edge reweighting — or remains an enrichment stub. This would be the first system to close the automation gap that the [comparative review](./agentic-memory-systems-comparative-review.md) identifies.
- Whether the graph demonstrably outperforms vector-only retrieval on their own benchmarks. The `evals/` directory has HotpotQA comparisons against Graphiti, LightRAG, and Mem0 — published results would settle the question.
- Whether the Pydantic schema approach proves more effective than schema discovery (sift-kg) or schema-free extraction (Mem0) at scale. The schema-definition-vs-schema-discovery axis is an open design question across the field.
- Whether the MCP server adoption pattern validates "knowledge engine as service" as a viable architecture for agent memory.

---

Relevant Notes:

- [files-not-database](../files-not-database.md) — contradicts: cognee is the strongest poly-store counterexample to the files-first thesis; databases are the primary substrate
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) — exemplifies: the memify gap concretely marks the boundary between automatable extraction and open curation problems
- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: cognee occupies the pipeline-first, developer-managed, schema-driven position across all six dimensions
- [sift-kg](./sift-kg.md) — contrasts: same problem (document-to-knowledge-graph) with opposite schema bets (definition vs discovery)
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: the pipeline invests multiple LLM calls at ingestion to make retrieval cheap; a specific context efficiency trade-off
- [distillation](../distillation.md) — exemplifies: cognify is automated distillation from unstructured documents to structured graph triplets, with Pydantic schemas shaping the extraction target
- [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — contrasts: knowledge is discoverable (search types, embeddings) but not composable in the KB sense (no claim structure, no resolution-switching) and only structurally trustworthy

Topics:

- [related-systems-index](./related-systems-index.md)
