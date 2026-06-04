---
description: "Beever Atlas review: wiki-first team-chat memory with trace-derived facts, graph links, generated pages, QA tools, and MCP pull surfaces"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# beever-atlas

> Replaced 2026-06-04. See [beever-atlas](./beever-atlas.md) for the current review.

Beever Atlas, from Beever-AI, is an open-source wiki-first RAG system for team chat and file-import knowledge. At the reviewed commit, it ingests platform-normalized messages, extracts atomic facts and entities through a Google ADK pipeline, stores semantic facts in Weaviate and graph entities in Neo4j, distills them into per-channel wiki pages, and exposes read surfaces through a dashboard QA agent and an MCP server.

**Repository:** https://github.com/Beever-AI/beever-atlas

**Reviewed commit:** [582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba](https://github.com/Beever-AI/beever-atlas/commit/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba)

**Last checked:** 2026-06-03

## Core Ideas

**The primary memory source is team trace material, not authored notes.** The durable source stream is normalized channel messages and file/import events stored in MongoDB's `channel_messages` collection with source, channel, message id, timestamp, author, content, attachments, and extraction state ([models/persistence.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/models/persistence.py), [mongodb_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/mongodb_store.py)). The README frames the product as turning Slack, Discord, Teams, Mattermost, and file-import conversations into an automatically maintained wiki, but the reviewed mechanism is the source-normalized message queue plus extraction pipeline ([README.md](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/README.md)).

**Ingestion is an ADK workflow that produces two memory substrates.** The workflow runs preprocessor -> fact/entity extraction -> join -> embedder/cross-batch validator -> join -> persister ([pipeline.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/agents/ingestion/pipeline.py)). The persister writes extracted `AtomicFact` rows to Weaviate, entities and relationships to Neo4j, and a MongoDB `WriteIntent` outbox for recovery; it also creates episodic links from entities to Weaviate fact ids ([persister.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/agents/ingestion/persister.py), [weaviate_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/weaviate_store.py), [neo4j_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/neo4j_store.py)).

**Atomic facts are not raw message snippets.** `AtomicFact` keeps distilled `memory_text`, quality, tier, cluster id, channel/platform/author fields, source message id, topic/entity/action tags, importance, graph ids, media/link provenance, validity/supersession fields, fact type, language, and optional decision/glossary/tension enrichments ([domain.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/models/domain.py)). Deterministic ids are content-derived from fact text plus entity names, which makes retries idempotent but also means the durable fact is an extracted claim, not the original trace itself.

**The wiki is a generated read surface, not just a cached answer.** Consolidation clusters facts by vector similarity, generates cluster and channel summaries, and notifies the wiki maintainer about touched fact ids ([consolidation.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/services/consolidation.py)). `WikiBuilder` gathers Weaviate facts/clusters plus Neo4j entities and decisions, compiles pages, and skips rebuilds when the build-input hash is unchanged ([data_gatherer.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/wiki/data_gatherer.py), [builder.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/wiki/builder.py)). Per-page wiki documents carry title, slug, sections, kind, kind schema, cross-links, dirty state, version, tensions, and `last_facts_seen` ([models/persistence.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/models/persistence.py), [page_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/wiki/page_store.py)).

**Context efficiency is frontloaded into distillation and bounded retrieval.** Atlas spends LLM and embedding work at ingestion/consolidation time so later queries can read facts, topic summaries, wiki pages, modules, or graph neighborhoods instead of full chat logs. Query paths also clamp limits: Weaviate hybrid search is filtered by channel/tier and limit, MCP `search_memory` clamps `limit` to 1-50 and fans out only over accessible channels, and the dashboard QA path injects only the last 10 retained conversation messages ([weaviate_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/weaviate_store.py), [memory_tools.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/agents/tools/memory_tools.py), [MCP retrieval tools](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/api/mcp_server/_tools_retrieval.py), [chat_history_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/chat_history_store.py)). Complexity is still substantial: returned wiki pages and generated summaries can be dense, so the system controls volume more strongly than semantic complexity.

**MCP exposes memory as tools with authorization, not as automatic agent context.** The MCP server offers discovery, retrieval, graph, session, and orchestration tools, with bearer-key principals, channel access checks, and per-tool structured errors ([docs/mcp-server.md](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/docs/mcp-server.md), [mcp_server/__init__.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/api/mcp_server/__init__.py), [MCP retrieval tools](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/api/mcp_server/_tools_retrieval.py)). From the external agent's perspective, the core team memory surface is pull: call `list_channels`, `search_memory`, `read_wiki_page`, or `ask_channel`.

## Artifact analysis

- **Storage substrate:** `vector` — Atlas's central queryable memory is Weaviate `MemoryFact`, with Neo4j graph state and MongoDB document collections as peer stores rather than a single canonical file substrate.
- **Representational form:** `prose` `symbolic` `parametric` — retained behavior-shaping artifacts combine prose facts/wiki sections, symbolic metadata/schemas/ACLs, graph relationships, and distributed-parametric embeddings.
- **Lineage:** `authored` `imported` `trace-extracted` — authored tools/prompts/policies operate over imported channel/file events and trace-extracted facts, graph state, summaries, wiki pages, and QA/session history.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — returned facts, pages, graph rows, and histories advise later answers; prompts/tools instruct; ACLs enforce; routing, validation, and ranking fields shape retrieval and distillation.

**Raw channel messages and file/import events.** Storage substrate: MongoDB document collections, especially `channel_messages`, sync jobs, external sources, and idempotency keys. Representational form: symbolic records plus raw text, attachments, links, and platform metadata. Lineage: imported from platform bridges, file imports, or push sources and then advanced through extraction states. Behavioral authority: knowledge artifacts as source evidence; extraction status and idempotency keys also have routing/enforcement authority over which traces are processed.

**Atomic facts, topic clusters, and channel summaries.** Storage substrate: Weaviate `MemoryFact` objects across `atomic`, topic, summary, and entity-card tiers. Representational form: mixed natural-language fact text and summaries, symbolic tags/status/supersession/source fields, and vectors. Lineage: LLM-extracted or consolidation-derived from channel messages, with deterministic ids, source message ids, and optional invalidation/supersession metadata. Behavioral authority: knowledge artifacts when returned as evidence or context; vector/BM25 scores, MMR, tiers, invalidation fields, and cluster ids have ranking and filtering authority.

**Graph entities, relationships, events, media, and wiki-page graph nodes.** Storage substrate: Neo4j. Representational form: symbolic graph nodes/edges plus prose relationship context and event/media metadata. Lineage: entity/relationship extraction, deterministic validation, persister writes, episodic links to Weaviate fact ids, and wiki-page cross-link upserts. Behavioral authority: knowledge artifacts for graph traversal and QA context; relationship types, endpoint stubs, entity status, and graph scoping become routing and retrieval system-definition artifacts.

**Wiki pages and kind schemas.** Storage substrate: MongoDB `wiki_pages` plus optional Neo4j wiki-page graph nodes. Representational form: mixed Markdown/prose sections, symbolic page ids/slugs/kinds/kind schemas/cross-links, dirty state, versioning, and `last_facts_seen`. Lineage: generated by `WikiBuilder` from consolidated facts and graph context, then incrementally maintained from touched fact ids; the build-input hash and dirty queue determine regeneration. Behavioral authority: knowledge artifacts for humans and MCP/QA agents; kind schemas and module/section tools give agents structured, token-efficient read paths.

**QA history and dashboard chat history.** Storage substrate: Weaviate `QAHistory` plus MongoDB `chat_history`. Representational form: prose questions/answers, citation envelopes, tool traces, and session metadata. Lineage: produced by dashboard QA turns after an answer is generated; MongoDB chat history expires after 90 days by TTL. Behavioral authority: knowledge artifacts for later dashboard QA continuity and `search_qa_history`; session history has push-like advisory authority when automatically prepended to the next dashboard ask prompt.

**QA/MCP tools, prompts, policies, and access checks.** Storage substrate: repository code and service configuration. Representational form: symbolic tool definitions, Pydantic models, config flags, access-control checks, prompt text, and LLM assignments. Lineage: authored system-definition artifacts. Behavioral authority: instruction, routing, validation, access control, ranking, and tool availability.

The main promotion path is trace -> extracted fact/entity -> clustered summary -> wiki page/module -> QA/MCP context. Atlas does not promote trace-derived content into executable rules or validators by default; its promotion mostly strengthens knowledge-artifact quality and retrieval shape.

## Comparison with Our System

| Dimension | Beever Atlas | Commonplace |
|---|---|---|
| Primary purpose | Turn team communication traces into searchable, cited wiki and QA memory | Maintain a git-native methodology KB for agents and maintainers |
| Canonical retained artifact | Atomic facts, graph entities/relationships, generated wiki pages, QA history | Typed Markdown notes, instructions, reviews, ADRs, source snapshots, indexes |
| Storage substrate | Weaviate, Neo4j, MongoDB, Redis, service state | Repository files plus deterministic indexes and reports |
| Representational form | Mixed prose, symbolic metadata, graphs, embeddings, generated pages | Mostly prose/frontmatter plus schemas, scripts, links, and validation |
| Lineage | Source message ids, citations, write intents, fact ids, `last_facts_seen`, supersession fields | Source-pinned citations, git history, replacement archives, type contracts, review gates |
| Activation | Pull tools/search/wiki/QA, plus dashboard session-history preload | Mostly deliberate pull through `rg`, indexes, links, skills, instructions, validators |
| Governance | Auth, channel ACLs, outbox, idempotency, dirty state, quality gates | Collection contracts, type specs, validation, semantic gates, review status |

Atlas and Commonplace share the conviction that useful agent memory needs a distilled read surface, not only raw logs or vector chunks. Atlas makes that surface a continuously maintained team wiki backed by semantic and graph stores. Commonplace makes it typed, source-pinned Markdown with explicit collection contracts and validation.

Atlas is stronger as a live operational memory service. It can ingest chat streams, handle attachments, maintain channel state, answer via MCP, and regenerate wiki pages as new facts arrive. Commonplace is stronger as an auditable methodology corpus: durable claims are inspectable in git, linked by explicit semantics, and reviewed before acquiring higher authority.

The biggest tradeoff is authority visibility. Atlas has rich lineage fields and citations, but many behavior-shaping choices live inside service state, prompt policy, embeddings, and generated wiki documents. Commonplace's slower promotion model is less automatic but clearer about when a trace, source, note, instruction, or validator becomes authoritative.

**Read-back:** `both` — team knowledge mostly reaches agents by pull through dashboard/API/MCP tools, while the dashboard QA path also pushes retained session chat history into the next ask prompt when a session id is reused.

### Borrowable Ideas

**Wiki as a promoted read substrate.** Ready conceptually. Atlas's best idea is not "RAG over chat"; it is "distill chat into wiki-shaped context before query time." Commonplace already uses library artifacts as the promoted surface, but Atlas reinforces making generated summaries browsable and citable rather than treating them as hidden retrieval glue.

**Attach source-message lineage to every distilled fact.** Ready for trace-heavy workflows. Commonplace source snapshots already pin external material; a trace-ingestion workflow should keep the raw trace artifact separate from the extracted fact and carry fact-to-source ids forward.

**Per-page dirty routing.** Needs a concrete generated-index or workshop use case. Atlas routes touched fact ids to affected pages instead of rebuilding everything. A Commonplace analogue could route changed sources to affected reviews or generated indexes, but it should stay deterministic and reviewable.

**Expose structured read slices, not only whole documents.** Ready as a design pattern. Atlas's `read_wiki_module` and `read_wiki_section` surfaces are useful because agents can request one bounded slice. Commonplace could give more generated indexes stable section anchors or machine-readable summaries without replacing the Markdown source.

**Discovery-first MCP tool flow.** Ready where Commonplace exposes services. Atlas's `whoami` -> `list_connections` -> `list_channels` -> retrieval sequence is a good authorization and orientation pattern for agent tools.

**Do not borrow service-state authority drift.** Atlas has many hidden authority surfaces: embeddings, generated wiki pages, dirty queues, LLM prompts, feedback/history stores, and ACL state. Commonplace should borrow the pipeline shape only where resulting artifacts remain visible, cited, and reviewable.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `event-streams` — platform-normalized channel/file/import events and retained dashboard QA sessions are the review's trace sources.

**Learning scope:** `per-project` `cross-task` — scope is organized by channel, connection, principal, session, and language, and the generated wiki/fact surfaces carry knowledge across later asks.

**Learning timing:** `online` `staged` — sync jobs and background extraction advance message status, while consolidation and wiki maintenance run after extraction settles.

**Distilled form:** `prose` `symbolic` `parametric` — Atlas distills traces into prose facts/summaries/wiki pages, symbolic graph/schema/status fields, and vector-indexed fact representations.

**Trace source.** Atlas qualifies as trace-derived. The raw signal is platform-normalized channel messages, file/import events, attachments, links, and later dashboard QA turns. Message traces are keyed by source, channel, and message id; QA traces are retained as chat history and QA history ([models/persistence.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/models/persistence.py), [chat_history_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/chat_history_store.py), [qa_history_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/qa_history_store.py)).

**Extraction.** The main extraction loop is staged: preprocessing cleans and enriches messages; fact/entity extractors produce memory facts and graph candidates; embedding and deterministic cross-batch validation enrich them; the persister writes Weaviate and Neo4j state; consolidation clusters and summarizes; wiki generation/maintenance produces pages and kind schemas ([pipeline.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/agents/ingestion/pipeline.py), [fact_extractor.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/agents/ingestion/fact_extractor.py), [persister.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/agents/ingestion/persister.py), [consolidation.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/services/consolidation.py), [wiki_maintainer.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/services/wiki_maintainer.py)). The oracles are mixed: LLM extraction/summarization, deterministic validators, embeddings, quality thresholds, contradiction checks, and operator policies.

**Four fields.** The raw stage is MongoDB-stored messages and QA turns: mixed trace content plus symbolic metadata, imported/recorded lineage, and knowledge-artifact authority as evidence. The distilled stage is Weaviate facts/clusters/summaries, Neo4j graph state, and MongoDB wiki pages: mixed prose-symbolic-parametric representation, LLM/code-derived lineage from traces, and advisory/ranking/filtering behavioral authority at retrieval time.

**Scope and timing.** Scope is primarily channel, connection, principal, session, and language. Timing is online or queued: sync jobs and background extraction advance message status; consolidation runs after extraction settles; wiki maintenance can mark pages dirty or apply updates depending on mode. QA/chat history retention is session-scoped and TTL-bound.

**Survey placement.** Atlas belongs in the trace-to-distilled-wiki family, with a dual vector/graph memory substrate underneath. It strengthens the survey claim that trace-derived memory often needs a curated read surface before it becomes useful to agents. It does not strengthen claims about automatic rule learning, validator generation, or high-authority instruction promotion.

## Read-back placement

**Direction.** Both, with an important split. Team knowledge read-back is mostly pull: a dashboard user, QA agent, MCP client, or external coding assistant calls search/wiki/QA tools to retrieve facts or pages. Dashboard QA conversation history is push: prior session turns are loaded from `chat_history`, formatted under `<prior_conversation>`, and prepended to the next prompt automatically when `session_id` is reused ([ask.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/api/ask.py), [chat_history_store.py](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/stores/chat_history_store.py)). MCP `ask_channel` explicitly does not persist or reload chat history, so this push path is dashboard-specific ([MCP ask runner](https://github.com/Beever-AI/beever-atlas/blob/582d156ffd23bbbb1834ac8a2d69cb6aa99e73ba/src/beever_atlas/api/mcp_server/_ask_runner.py)).

**Read-back signal:** `identifier` — the push path is dashboard-specific and keyed by the reused `session_id` that selects retained conversation turns.

**Faithfulness tested:** `no` — the review found no with/without ablation or post-action faithfulness audit proving that retrieved memory changed behavior correctly.

**Targeting and signal.** Pull retrieval uses both identifiers and inferred signals: channel id, connection/principal ACLs, page slug, page kind, session id, and fact ids are identifiers; BM25, vector search, MMR, graph traversal, and LLM QA are inferred selection. The push path is `instance / identifier`: the reused `session_id` selects the last retained conversation turns for that session. Precision and usefulness of the returned team memory are runtime qualities, not verified from code.

**Injection point.** Search/wiki/MCP calls run during an ask or external-agent turn and can affect the answer after the tool returns. Dashboard chat-history preload happens before the QA agent sees the new ask, so it can shape the next answer. Post-answer persistence to QAHistory and chat_history affects later turns only.

**Selection, scope, and complexity.** Atlas has several explicit bounds: MCP question/query length, retrieval limits, per-channel ACLs, Weaviate `tier` filters, top-k style tool limits, wiki module/section reads, and `MAX_CONTEXT_TURNS = 10` for dashboard session history. The remaining complexity risk is qualitative: generated wiki pages, graph neighborhoods, and fact lists can still be semantically broad even when their item count is bounded.

**Authority at consumption.** Retrieved facts, wiki pages, graph rows, and chat history are advisory context for the QA model or external MCP client. MCP/auth/channel policies have hard enforcement authority before retrieval. The system does not appear to run a with/without ablation or post-action faithfulness audit proving that retrieved memory changed the model's behavior correctly.

**Other consumers.** Human operators consume the dashboard, wiki, lint, health, sync status, merge proposals, and runbooks. Services consume write intents, dirty queues, sync state, policy records, and graph indexes as operational control artifacts.

## Curiosity Pass

**The generated wiki is the product's real memory interface.** Weaviate and Neo4j hold the substrate, but Atlas's distinctive claim is that agents and people should read distilled pages instead of raw chat. That makes wiki quality, freshness, and citation fidelity more important than vector recall alone.

**The source lineage is useful but not span-level.** Atomic facts carry source message ids, timestamps, authors, media/link fields, and citations, but the reviewed code does not make each generated wiki sentence a source-span-preserving claim in the way a code-grounded review note does.

**MCP and dashboard QA are not identical.** The dashboard path loads chat history, uses decomposition, streams events, persists turns, and can use citation-registry rewriting. The MCP ask runner intentionally omits chat-history loading and persistence, so "Atlas QA" has different memory behavior depending on surface.

**The wiki-maintainer persistence story deserves parent QA attention.** The maintainer docstring still describes an in-memory dirty set, while the MongoDB store now includes a `wiki_dirty_queue` collection and indexes. The code may have moved beyond the prose; a follow-up review should resolve which mechanism is authoritative.

**The storage-substrate vocabulary fits awkwardly.** Atlas is document + vector + graph + cache + service state. The controlled token in this review leads with `vector` because Weaviate facts are the central retrieval substrate, but that under-describes the wiki and graph surfaces.

## What to Watch

- Whether wiki pages gain sentence-level source spans, prompt/model versions, and extraction audit records for each generated claim.
- Whether the MCP surface grows an automatic pre-action read-back hook for external agents rather than relying on explicit tool calls.
- Whether the dirty-queue/wiki-maintainer implementation and docs converge; this affects how durable incremental page maintenance really is.
- Whether proposed wiki edits become active; `wiki_proposed_edits` is currently provisioned as a reserved collection, which could become a promotion path from trace-derived memory to operator-approved edits.
- Whether contradiction, supersession, and tension handling become visible in generated pages with enough evidence for a user to audit why an older fact was invalidated.

## Bottom Line

Beever Atlas is a real trace-derived team-memory system whose distinctive move is frontloading chat distillation into a browsable, cited wiki before query time. It is useful evidence for wiki-shaped agent memory over noisy communication traces, but less useful as a governance model for Commonplace unless its generated artifacts get stronger source-span lineage and review/promotion controls.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Atlas turns chat/file/QA traces into extracted facts, graph state, generated wiki pages, and cited answer history.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Atlas has rich stored memory, but most team knowledge reaches agents only when a tool or UI path pulls it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Atlas requires separating raw messages, facts, graph nodes, wiki pages, prompts, tools, history, and ACLs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw traces, extracted facts, graph context, wiki pages, and returned QA evidence mainly advise future behavior.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: tool definitions, ACL checks, extraction prompts, validators, retrieval filters, dirty queues, and service policies constrain or route behavior.
