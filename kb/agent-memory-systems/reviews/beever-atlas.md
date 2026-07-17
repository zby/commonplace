---
description: "Beever Atlas review: chat-ingestion knowledge base with Weaviate facts, Neo4j graph memory, MongoDB wiki pages, MCP retrieval, and trace-learning wiki synthesis"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# Beever Atlas

Beever Atlas, from Beever-AI, is a team-chat knowledge base that ingests Slack, Discord, Microsoft Teams, Mattermost-style bridge data, Telegram/file imports, and related media; extracts atomic facts, entities, and relationships; stores those derived memories in Weaviate, Neo4j, and MongoDB; and serves them through a dashboard, QA agent, wiki, and MCP server. At the reviewed commit it is not just a retriever over raw transcripts: the distinctive move is to frontload chat-to-wiki distillation so later agents query cleaner facts, topic summaries, graph relationships, and generated wiki pages instead of re-reading chat logs.

**Repository:** https://github.com/Beever-AI/beever-atlas

**Reviewed commit:** [74a8dbc6d7a382d4d592a762bdc8230305c869c8](https://github.com/Beever-AI/beever-atlas/commit/74a8dbc6d7a382d4d592a762bdc8230305c869c8)

**Source directory:** `related-systems/Beever-AI--beever-atlas`

## Core Ideas

**The memory source is operational conversation, not authored notes.** The README describes Atlas as pulling conversations from team chat platforms, extracting atomic facts, deduplicating them, clustering them into topic pages, and citing answers back to source messages ([README.md](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/README.md)). The pipeline docs make the source boundary explicit: platform-specific messages are normalized into `NormalizedMessage` records before entering the Python ingestion pipeline ([docs/pipeline-architecture.md](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/docs/pipeline-architecture.md), [src/beever_atlas/adapters/base.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/adapters/base.py)). That makes Atlas a trace-derived organizational memory system: its durable knowledge starts as message transcripts and platform event records.

**Ingestion is a staged ADK workflow with deterministic fan-in guards.** `create_ingestion_pipeline()` wires preprocessing, parallel fact/entity extraction, embedding, deterministic cross-batch validation, and persistence through explicit `JoinNode`s so the persister runs once after both enrich stages complete ([src/beever_atlas/agents/ingestion/pipeline.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/agents/ingestion/pipeline.py)). The pipeline therefore separates trace cleanup, LLM extraction, vectorization, entity reconciliation, and durable writes rather than making each query summarize raw chat from scratch.

**The retained memory is multi-surface but fact-centered.** `AtomicFact` carries source message identity, channel/platform metadata, topic/entity/action tags, importance, vector, contradiction/supersession fields, media/link provenance, fact type, source language, and decision-enrichment fields ([src/beever_atlas/models/domain.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/models/domain.py)). Weaviate persists those facts plus topic clusters and channel summaries in the `MemoryFact` collection, while Neo4j persists entities, relationships, episodic links, media nodes, and wiki page graph nodes ([src/beever_atlas/stores/weaviate_store.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/stores/weaviate_store.py), [src/beever_atlas/stores/neo4j_store.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/stores/neo4j_store.py)).

**Atlas frontloads context work into topic summaries and wiki pages.** The consolidation service clusters unclustered facts by embedding similarity, then summarizes dirty clusters and channel-level state after memory settles ([src/beever_atlas/services/consolidation.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/services/consolidation.py)). The wiki maintainer routes touched fact ids to specific pages and can rewrite affected sections rather than regenerating everything ([src/beever_atlas/services/wiki_maintainer.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/services/wiki_maintainer.py)). Context efficiency comes from this pre-digestion: later QA can read cached wiki pages, topic summaries, graph traversals, and ranked fact rows instead of filling context with whole channels.

**Read surfaces are broad and bounded by tool contracts.** The QA agent is an ADK `LlmAgent` with wiki, memory, graph, history, media, activity, and external-search tools, and each answer mode limits available tools and maximum tool calls ([src/beever_atlas/agents/query/qa_agent.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/agents/query/qa_agent.py), [src/beever_atlas/agents/tools/__init__.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/agents/tools/__init__.py)). MCP exposes read-oriented tools such as `ask_channel`, `search_channel_facts`, `search_memory`, and wiki readers with principal/channel checks and result caps ([src/beever_atlas/api/mcp_server/_tools_retrieval.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/api/mcp_server/_tools_retrieval.py)).

**Trust comes mostly from provenance, typed stores, and operational checks, not from behavioral ablations.** Facts retain source message ids, timestamps, authors, channels, media/link provenance, and citation decorator handles; write intents journal persistence before dispatching to Weaviate and Neo4j ([src/beever_atlas/agents/ingestion/persister.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/agents/ingestion/persister.py), [src/beever_atlas/agents/tools/_citation_decorator.py](https://github.com/Beever-AI/beever-atlas/blob/74a8dbc6d7a382d4d592a762bdc8230305c869c8/src/beever_atlas/agents/tools/_citation_decorator.py)). I found tests for store behavior, API tools, graph protocols, citations, wiki generation, and retrieval plumbing, but not a read-back faithfulness test showing that a retrieved wiki/fact/graph item changed a downstream agent answer.

## Artifact analysis

- **Storage substrate:** `vector` — The primary answer-facing memory substrate is Weaviate's `MemoryFact` collection for atomic facts, topic clusters, channel summaries, entity cards, and vectors. Secondary retained substrates are Neo4j graph state and MongoDB service documents such as raw channel messages, write intents, QA history, wiki pages, dirty queues, and platform connection state.
- **Representational form:** `prose` `symbolic` `parametric` — Chat facts, wiki pages, summaries, prompts, and answers are prose; message ids, channels, entities, relationships, fact types, schemas, page ids, policies, write intents, and tool contracts are symbolic; embeddings, HNSW vector search, similarity clustering, and name vectors are parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — Operators author config, policies, credentials, page edits, and prompts; imports can come from platform bridges and file adapters; the central facts, entities, relationships, topic clusters, summaries, wiki pages, QA-history entries, and citations are derived from message traces and later query traces.
- **Behavioral authority:** `knowledge` `routing` `validation` `ranking` `learning` — Stored facts/wiki/graph rows advise agents and humans as knowledge; channel ids, page ids, entity tags, graph relationships, policies, and tool descriptors route reads; schemas, validators, access checks, quality gates, and linting constrain what is accepted; vector/BM25/MMR/graph scoring ranks what is served; ingestion/consolidation/wiki-maintenance loops learn derived artifacts from trace streams.

**Atomic facts.** Storage substrate: Weaviate `MemoryFact` objects. Representational form: prose `memory_text` plus symbolic metadata and parametric vectors. Lineage: extracted from normalized messages, enriched by extraction/classification/embedder stages, then persisted with source message identity and provenance fields. Behavioral authority: knowledge artifacts when surfaced to QA/MCP/humans; ranking artifacts when embeddings, BM25, topic tags, quality scores, importance, and MMR select the context served.

**Topic clusters and channel summaries.** Storage substrate: Weaviate objects with `tier="topic"` or `tier="summary"`. Representational form: prose summaries and symbolic member ids, tags, counts, graph highlights, dirty flags, and centroid vectors. Lineage: derived from atomic facts and graph context; invalidated by new fact membership through `summary_dirty`. Behavioral authority: knowledge artifacts and context-compression artifacts for QA/wiki readers; routing artifacts when page generation and topic lookup use cluster ids/tags.

**Graph entities and relationships.** Storage substrate: Neo4j, with optional Nebula/null graph abstraction behind the graph protocol. Representational form: symbolic nodes/edges with prose relationship context and optional name vectors. Lineage: extracted from message batches, validated/deduplicated across batches, normalized, healed with stub entities, and linked back to fact/message provenance. Behavioral authority: graph traversal, decision-history, and expert-finding tools use this as structured knowledge and routing/ranking input.

**Wiki pages.** Storage substrate: MongoDB `wiki_pages` and legacy wiki cache documents, with Neo4j wiki-page graph nodes for some navigation surfaces. Representational form: prose sections plus symbolic page ids, slugs, kind schemas, sections, versions, redirects, dirty flags, and cross-links. Lineage: generated from facts, clusters, entities, wiki prompts, and page-maintainer updates; page versions change on user-visible content differences. Behavioral authority: knowledge artifacts for users and QA agents, and a frontloaded context surface that can displace raw transcript retrieval.

**Write intents, dirty queues, sync state, and policies.** Storage substrate: MongoDB service collections. Representational form: symbolic documents and timestamps. Lineage: generated by sync, extraction, persistence, purge, and wiki-maintenance operations. Behavioral authority: validation/enforcement/routing for durability, retries, deletion, queue recovery, per-channel policies, and which pages/facts are eligible for maintenance.

**QA/MCP tools and citation registry.** Storage substrate: authored Python/FastMCP code plus runtime service state. Representational form: symbolic tool schemas/docstrings and prose prompts; citation outputs carry symbolic source handles and prose excerpts. Lineage: authored implementation that consumes trace-derived memory at runtime. Behavioral authority: routing and knowledge authority for callers; tools choose which retained memory can enter an answer and under which principal/channel access checks.

The main promotion path is trace -> atomic facts/entities -> topic clusters/channel summaries -> wiki pages and graph-aware QA. Atlas does have stronger governance than a raw chat-RAG stack because source ids, citations, write intents, indexes, and page versions survive the distillation path. It does not have a library-style promotion gate that asks whether a generated wiki claim deserves durable authority before future agents read it.

## Comparison with Our System

| Dimension | Beever Atlas | Commonplace |
|---|---|---|
| Primary purpose | Turn team communication streams into a queryable, cited, auto-maintained wiki and QA memory | Maintain a durable methodology KB for agents and maintainers |
| Main retained unit | Atomic facts, graph entities/relationships, topic summaries, wiki pages, QA history | Typed Markdown notes, instructions, reviews, sources, reports, schemas, indexes |
| Write path | Automatic trace ingestion, extraction, persistence, clustering, wiki maintenance, plus operator/manual controls | Mostly authored artifacts, explicit source snapshots, validation, review, version history |
| Read path | Dashboard/API/MCP/QA tools over vector, graph, wiki, and history stores | `rg`, links, indexes, collection contracts, skills, validation/review workflows |
| Context efficiency | Frontloaded distillation into facts, clusters, summaries, and wiki pages; tool-call limits and result caps | Hand-authored compression, typed indexes, link vocabulary, search-first navigation, scoped skills |
| Governance | Store schemas, access checks, write intents, source ids, citations, linting, tests | Git history, collection contracts, schemas, deterministic validation, semantic review, curated indexes |

Atlas is the mirror image of Commonplace on authorship. Commonplace starts with explicit artifacts written for future agents and treats validation/review as the route to durable authority. Atlas starts from messy operational traces and tries to distill them into a wiki automatically enough that the team need not author the KB first. That makes Atlas stronger as a live organizational memory extractor and weaker as a deliberate methodology library.

The most useful design contrast is the timing of compression. Commonplace compresses at writing time through note structure, type specs, summaries, and indexes. Atlas compresses after capture and before query: facts, clusters, and wiki pages are generated once and reused. That is a real context-efficiency strategy, but it shifts risk into lineage and maintenance: if a wiki page overgeneralizes a message thread, downstream agents may read a clean-looking statement whose source confidence is weaker than the prose suggests.

Atlas is also more complete as an application surface. It has auth, per-channel access, sync jobs, platform connections, dashboard UX, MCP tools, vector search, graph traversal, and wiki pages. Commonplace is intentionally repo-native and agent-operated; it offers stronger inspectability and review at the artifact level but far less live ingestion infrastructure.

### Borrowable Ideas

**Frontload raw traces into readable wiki artifacts.** Commonplace already snapshots sources and writes reviews, but Atlas shows a stronger product pattern: raw traces become browsable pages before a later question arrives. Ready for workshop reports and source-heavy investigations, but library notes still need review before promotion.

**Keep source-message citations attached to distilled facts.** Atlas's facts preserve source message ids, author/channel/time fields, media/link provenance, and citation handles. Commonplace should keep pushing generated artifacts toward explicit source pointers rather than only prose summaries. Ready now for review outputs and ingest reports.

**Use dirty queues for incremental regeneration.** The wiki maintainer routes touched fact ids to affected pages instead of rebuilding every page. A Commonplace analogue could route changed sources or validation findings to affected indexes/reviews. Useful when regeneration volume grows; not needed for small manual edits.

**Use graph memory for relational questions, not as a universal substrate.** Atlas's graph tools are valuable for "who/what is connected" questions while Weaviate/wiki remain the prose/fact surfaces. Commonplace could borrow a derived relationship index only where authored links and frontmatter are insufficient.

**Do not borrow automatic wiki authority without review.** Atlas can generate clean pages from noisy traces, but that does not prove each claim should become durable instruction or methodology. In Commonplace, generated pages should land in `kb/work/` or source reports until validation/review promotes them.

## Write side

**Write agency:** `manual` `automatic` — Operators configure connections, policies, imports, page maintenance, and sync/refresh actions, while Atlas automatically normalizes messages, extracts facts/entities, embeds, validates, persists, clusters, summarizes, rewrites wiki pages, records QA history, and manages retry/dirty queues.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `promote` — Atlas consolidates atomic facts into clusters, channel summaries, and wiki pages; deduplicates/reconciles entities and deterministic fact ids; evolves dirty wiki pages and cluster summaries when new facts arrive; synthesizes new topic/wiki/summary artifacts; carries contradiction/supersession fields and stale/dirty states; and promotes pending graph entities once relationships support them.

### Trace-learning

**Trace source:** `session-logs` `event-streams` — The qualifying trace is team communication and imported content: platform messages, threads, attachments, links, sync events, file imports, and later QA history. The reviewed code does not show agent tool/action traces as the primary source.

**Learning scope:** `per-project` `cross-task` — Memory is scoped by channel, platform connection, principal access, language, page, entity, and topic, but the retained wiki/graph/fact store is meant to support future questions across many later tasks.

**Learning timing:** `online` `staged` — Sync/extraction/persistence happen during ingestion jobs, while settled-memory summarization and wiki maintenance are staged behind dirty flags, queues, debounces, and manual/auto modes.

**Distilled form:** `prose` `symbolic` `parametric` — Raw chat becomes prose facts, summaries, and wiki sections; symbolic entities, relationships, tags, page schemas, write intents, and citations; and parametric embeddings/name vectors used for ranking, clustering, and matching.

**Extraction.** The extraction oracle is a mix of LLM schema prompts, deterministic filters, similarity checks, source-message joins, and operator-visible tests. Fact extraction asks whether a new teammate would need the fact months later, then attaches quality/importance/topic/entity fields; entity extraction and validation reconcile names and relationships; persistence writes only typed models and carries retry state through MongoDB write intents.

**Raw and distilled stages.** Raw messages and platform metadata persist in MongoDB channel-message/import/sync collections. Distilled artifacts persist as Weaviate facts/clusters/summaries, Neo4j entities/relationships/media/episodic links, MongoDB wiki pages, and QA-history entries. The raw stage is mostly a knowledge artifact and queue substrate; the distilled stage becomes the behavior-shaping memory served to QA agents, MCP clients, dashboards, and human readers.

**Scope and timing.** The loop is project/team scoped rather than single-agent scoped. A channel can ingest many batches; the per-batch path clusters and routes touched facts, while `memory_settled` triggers LLM summary work only after the extraction queue drains. Wiki maintenance can run automatically after a debounce or mark pages dirty for manual draining.

**Survey relation.** Atlas sits in the trace-to-readable-artifact family, closer to an organizational wiki builder than a personal agent-memory library. It strengthens the claim that trace-learning need not fine-tune a model: durable value can come from fact extraction, graph construction, and wiki synthesis. It also exposes the review problem for trace-derived wikis: polished generated prose needs source-aware governance or readers may over-trust it.

## Read-back

**Read-back:** `pull` — Retained Atlas memory reaches an agent or user when a caller invokes the dashboard ask endpoint, the QA agent's tools, MCP tools such as `ask_channel`/`search_channel_facts`/`read_wiki_page`, or direct API/wiki/search endpoints. I did not find an unsolicited pre-invocation memory injector that pushes retained memory into a future agent turn without a user, host agent, scheduler, or QA tool call asking for it.

Atlas's pull path is still substantial. `search_channel_facts()` performs hybrid vector/BM25 retrieval with fallback and MMR reranking; `get_wiki_page()` and `get_topic_overview()` read cached wiki or summary surfaces; graph tools traverse relationships, decisions, and experts; MCP `search_memory()` fans retrieval across accessible channels and re-ranks merged hits. These reads are bounded by channel/principal checks, mode-specific tool sets, result caps, and documented tool contracts.

From the external agent's perspective, MCP access is pull: Claude Code, Cursor, or another MCP client must call an Atlas tool. From Atlas's internal QA agent's perspective, tool calls are also pull: the prompt says which channel/question is in scope, and the agent chooses retrieval tools during the run. Static tool descriptions and QA prompts are baseline system surfaces, not read-back from accumulated memory.

Quality and faithfulness are not established by code inspection. The code can show schemas, citations, access checks, result caps, and ranking mechanisms; it cannot show that a particular retrieved fact or wiki page changed the final answer unless the system runs an ablation or post-answer audit. I did not find that kind of read-back faithfulness test in the reviewed implementation.

## Curiosity Pass

**Atlas is wiki-first RAG with an unusually explicit write side.** Many RAG systems emphasize retrieval but leave the memory-making path vague. Atlas has a real ingestion and maintenance architecture: outbox write intents, deterministic ids, graph reconciliation, cluster dirty flags, per-page wiki documents, and dirty queues.

**The clean wiki is both the main strength and the main epistemic risk.** A wiki page is much easier for an LLM to use than a transcript, but the page can hide uncertainty introduced during extraction, clustering, or synthesis. Citations mitigate this only if readers and agents actually inspect them.

**MongoDB is the quiet control plane.** Weaviate and Neo4j are the advertised memory stores, but MongoDB carries platform credentials, channel messages, write intents, sync state, wiki pages, dirty queues, proposed edits, QA history, and policies. Much of Atlas's reliability depends on those service documents, even when the answer-facing memory is vector/graph/wiki.

**The read side is broad but not self-triggering.** Atlas has many ways to retrieve memory, including MCP, but the reviewed code does not make memory arrive unasked at an external agent's next turn. It is a strong memory server, not an unsolicited memory layer by itself.

**Some authority is deliberately withheld from MCP.** The MCP retrieval docs repeatedly mark key tools read-only, while sync/refresh/write-like operations are separated or guarded. That is a useful authority split for agent-facing memory services.

## What to Watch

- Whether the v2 `wiki_proposed_edits` path becomes a real agent write-through surface. That would add a stronger manual/automatic promotion and review question for generated wiki changes.
- Whether Atlas adds faithfulness or ablation tests for wiki/fact/graph read-back. That would materially improve confidence that retrieved memory changes answers rather than merely appearing in context.
- Whether contradiction handling moves from fact fields and detector services into visible wiki invalidation. That would clarify how stale or superseded trace-extracted claims are retired.
- Whether MCP gains write tools beyond guarded sync/refresh. That would change the behavioral-authority analysis from read-only memory service toward agent-editable KB.
- Whether wiki pages expose source-confidence and extraction lineage more directly. That would make generated pages safer as long-lived organizational memory.

Relevant Notes:

- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Atlas turns communication traces into facts, graph structures, topic summaries, and wiki pages.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: Atlas stores rich memory but still relies on explicit ask/search/wiki/MCP calls for read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Atlas needs separate treatment for vector facts, graph relationships, wiki pages, service queues, and tool contracts.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - aligns: Atlas precomputes facts, clusters, summaries, and wiki pages before later QA calls.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved facts, wiki sections, graph rows, and citations mostly advise later reasoning as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: schemas, tool contracts, policies, write intents, queues, validators, and ranking paths carry stronger operational authority.
