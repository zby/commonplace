---
description: "WeKnora review: enterprise RAG and agent platform with document chunks, wiki pages, graph memory, ReAct tools, and push plus pull read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-05"
---

# WeKnora

WeKnora, from Tencent, is an enterprise RAG and agent framework for ingesting documents, building searchable knowledge bases, running ReAct-style agents, and generating wiki pages from source material. At reviewed commit `4bb8906520a9e16ccbf3312a1b65ba36210dbd9e`, the source contains the main Go server, a web UI, a CLI, an MCP server, document parsing services, multiple vector backends, wiki generation, and a separate conversation-memory graph path.

**Repository:** https://github.com/Tencent/WeKnora

**Reviewed commit:** [4bb8906520a9e16ccbf3312a1b65ba36210dbd9e](https://github.com/Tencent/WeKnora/commit/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e)

**Source directory:** `related-systems/Tencent--WeKnora`

## Core Ideas

**The primary memory object is a knowledge base, not an agent-local note.** Knowledge bases, knowledge rows, chunks, wiki pages, sessions, and messages are first-class database objects; chunks carry source, KB, type, positional, parent/neighbor, relation, tag, status, and metadata fields ([internal/types/knowledgebase.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/types/knowledgebase.go), [internal/types/knowledge.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/types/knowledge.go), [internal/types/chunk.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/types/chunk.go)). This makes WeKnora closer to a multi-tenant knowledge service than to a single-agent memory library.

**Retrieval is a layered RAG pipeline.** The chat pipeline can run query understanding, chunk/entity search, reranking, merging, top-k filtering, optional data analysis, and prompt rendering before chat completion ([internal/types/chat_manage.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/types/chat_manage.go), [internal/application/service/session_knowledge_qa.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/session_knowledge_qa.go)). Hybrid retrieval fuses vector and keyword hits with RRF, can fan out across KB scopes, and then reranks and applies MMR before prompt injection ([internal/application/service/knowledgebase_search_fusion.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/knowledgebase_search_fusion.go), [internal/application/service/chat_pipeline/rerank.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/chat_pipeline/rerank.go), [internal/application/service/chat_pipeline/merge.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/chat_pipeline/merge.go)).

**Agent mode exposes knowledge as tools rather than only as preloaded context.** The custom-agent service registers knowledge search, chunk grep/listing, knowledge-graph query, database/data-analysis, wiki, web-search, skill, and MCP tools according to configured scope and capabilities ([internal/application/service/agent_service.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/agent_service.go)). Tool outputs are schema-validated and truncated before being fed back into the ReAct loop ([internal/agent/tools/registry.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/agent/tools/registry.go)).

**Wiki mode is a derived, interlinked Markdown knowledge layer.** Wiki pages persist as DB rows with slug, type, Markdown content, summary, aliases, source refs, chunk refs, in-links, out-links, metadata, and version ([internal/types/wiki_page.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/types/wiki_page.go)). The ingest worker batches source-document ops, extracts entities/concepts/summaries, deduplicates against existing pages, writes or updates pages, injects cross-links, cleans dead links, logs operations, and dead-letters repeated failures ([internal/application/service/wiki_ingest.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/wiki_ingest.go), [internal/application/service/wiki_ingest_dedup.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/wiki_ingest_dedup.go), [internal/application/service/wiki_linkify.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/wiki_linkify.go)).

**A separate conversation-memory path extracts traces into Neo4j.** When memory is enabled for pure chat, the pipeline retrieves related memory before chat completion and stores the finished user/assistant turn afterward. `MemoryService.AddEpisode()` asks an LLM to extract a summary, entities, and relationships from messages, then saves an episode/entity/relation graph; `RetrieveMemory()` asks an LLM for search keywords and pulls up to five related episodes by entity name ([internal/application/service/chat_pipeline/memory.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/chat_pipeline/memory.go), [internal/application/service/memory/service.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/memory/service.go), [internal/application/repository/memory/neo4j/repository.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/repository/memory/neo4j/repository.go)).

**Context efficiency is multi-layered but service-shaped.** WeKnora bounds context by search scopes, top-k parameters, thresholds, rerank top-k, MMR, chunk merge/parent expansion, wiki index top-k summaries, seen-page omission in wiki tools, tool-output truncation, and an agent conversation consolidator that summarizes older messages when token usage crosses a configured threshold ([internal/agent/tools/wiki_tools.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/agent/tools/wiki_tools.go), [internal/agent/memory/consolidator.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/agent/memory/consolidator.go), [internal/agent/observe.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/agent/observe.go)). It does not make context assembly inspectable as files; most state and policy live in DB rows, service config, and runtime traces.

## Artifact analysis

- **Storage substrate:** `rdbms` `vector` `graph` `service-object` `files` - The canonical application state lives in SQL tables for knowledge bases, knowledges, chunks, sessions, messages, wiki pages, audit logs, and task queues; retrieval indexes live in pluggable vector/keyword engines; conversation memory can live in Neo4j; MCP/agent/tool state is a runtime service object; source files/object storage hold uploaded documents ([migrations/sqlite/000000_init.up.sql](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/migrations/sqlite/000000_init.up.sql), [internal/application/service/retriever/composite.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/retriever/composite.go), [internal/application/repository/memory/neo4j/repository.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/repository/memory/neo4j/repository.go)).
- **Representational form:** `prose` `symbolic` `parametric` - Document text, chunk text, wiki Markdown, summaries, prompts, episodes, and tool outputs are prose; schemas, slugs, IDs, scopes, roles, tool definitions, graph edges, links, statuses, RBAC, and pipeline stages are symbolic; embeddings, vector distances, reranker scores, and some LLM extraction/ranking judgments are parametric.
- **Lineage:** `authored` `imported` `trace-extracted` - Users and agents author manual knowledge, wiki edits, custom agents, skills, settings, and tool calls; documents, URLs, IM sources, data-source connectors, browser extension captures, and files are imported; chat turns can be trace-extracted into memory episodes and the agent consolidator summarizes prior conversation/tool history.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Retrieved chunks, wiki pages, graph facts, and memory summaries advise as knowledge; prompts, CLI `AGENTS.md`, skills, and tool descriptions instruct agents; RBAC, destructive-action confirmation, MCP approval gates, and tool allowlists enforce; KB scopes, search targets, wiki slugs, links, and MCP/tool registries route; JSON schemas, parameter validation, parse statuses, migrations, tests, and linting validate; RRF/vector/rerank/MMR and wiki search rank; wiki ingest and memory extraction learn derived state from documents or traces.

**Knowledge bases, knowledge rows, and chunks.** Storage substrate: SQL rows plus object/file storage and derived retrieval indexes. Representational form: prose content with symbolic metadata, chunk topology, tags, statuses, source IDs, and indexing strategy; parametric embeddings are derived. Lineage: imported documents/URLs/manual entries. Behavioral authority: knowledge when read, ranking when indexed, routing when scoped by KB, knowledge ID, tenant, tag, or chunk type.

**Wiki pages.** Storage substrate: `wiki_pages` rows and synced `wiki_page` chunks. Representational form: Markdown prose plus symbolic slugs, page types, aliases, source refs, chunk refs, in/out links, metadata, and versions. Lineage: LLM-derived from imported documents, then automatically deduplicated, linkified, updated, or retracted. Behavioral authority: knowledge and routing for agents and users; page links and index overviews become a navigation layer over source material.

**Conversation memory graph.** Storage substrate: Neo4j episode/entity/relation graph. Representational form: prose summaries/descriptions plus symbolic graph nodes, `MENTIONS`, `RELATED_TO`, user IDs, session IDs, and timestamps. Lineage: trace-extracted from user/assistant messages. Behavioral authority: knowledge when injected as "Relevant Memory"; routing when entity names select related episodes; learning because new turns become future retrievable graph state.

**Agent tools, CLI, and MCP surfaces.** Storage substrate: repository code, database-configured services, runtime tool registries, and client profile/secret stores. Representational form: symbolic command/tool schemas plus prose descriptions and outputs. Lineage: authored integration contracts and runtime service configuration. Behavioral authority: instruction, routing, validation, and enforcement for agent access; the CLI explicitly treats JSON/error shapes as agent-facing API ([cli/AGENTS.md](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/cli/AGENTS.md), [internal/agent/tools/mcp_tool.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/agent/tools/mcp_tool.go)).

Promotion path: imported documents can be chunked, embedded, summarized, graph-extracted, and elevated into wiki pages with links and citations; conversation turns can become graph episodes and later prompt context; agent turns can be compacted into an in-context memory summary. These promotions strengthen retrieval and context authority, but most generated judgments remain service state rather than reviewer-visible source artifacts.

## Comparison with Our System

| Dimension | WeKnora | Commonplace |
|---|---|---|
| Primary purpose | Multi-tenant RAG, agent, wiki, and integration platform | Git-native methodology KB for agents and maintainers |
| Canonical artifact | SQL/service rows: KBs, chunks, wiki pages, sessions, tool configs, graph episodes | Typed Markdown files with frontmatter, citations, links, validation, and git history |
| Write path | Upload/import, async parsing, indexing, wiki generation, agent wiki tools, trace-memory extraction | Authored edits, snapshots, review gates, validation, source-grounded replacement |
| Read-back | Automatic RAG/memory prompt injection plus explicit agent/CLI/MCP tools | Mostly pull through `rg`, indexes, links, skills, and explicit instructions |
| Governance | RBAC, ownership, audit logs, task queues/dead letters, schema validation, MCP approval, tests | Collection contracts, type specs, deterministic validation, semantic review, git diffs |
| Context efficiency | Top-k/thresholds/rerank/MMR, chunk merging, wiki top-k overviews, tool truncation, history consolidation | Human-readable indexes, links, type contracts, file search, generated indexes, review reports |

WeKnora is stronger as an application substrate. It provides user accounts, tenants, RBAC, connectors, UI, IM channels, agent loops, web search, model/provider abstraction, vector backends, and operational task machinery. Commonplace is stronger as an inspectable knowledge substrate: its durable behavior-shaping artifacts are plain files with local contracts, citations, and reviewable diffs.

The key design divergence is authority visibility. WeKnora lets LLM extraction, reranking, wiki generation, link injection, and memory extraction immediately shape later context. That is appropriate for an interactive service, but it hides many epistemic moves inside database rows and background workers. Commonplace usually requires those moves to surface as source-grounded Markdown, validation output, or review notes.

### Borrowable Ideas

**Scoped push memory with an explicit user switch.** WeKnora's `EnableMemory` path is a concrete example of optional push read-back. A Commonplace analogue would be a per-workshop/session opt-in that injects a compact "recent relevant working memory" block before generation. Needs a strong audit trail before it should touch durable library behavior.

**Derived wiki pages with source and chunk refs.** Commonplace could use generated, explicitly derived topic pages or indexes for large source batches, with source refs preserved. Ready as a workshop artifact pattern; not ready as automatic library mutation without review.

**Bounded index overviews for agent navigation.** The wiki tool's top-k index overview is a useful progressive-disclosure move: show shape first, then require search/read for depth. Ready now for generated index serving and large directory summaries.

**Agent-facing CLI contracts.** WeKnora's CLI documentation treats stdout/stderr, JSON envelopes, retry commands, and destructive-action exits as an agent API. Commonplace command docs could adopt that discipline where CLI output is meant to be parsed by agents. Ready now.

**Human approval gates for external tools.** MCP approval before dangerous tool calls is a useful governance mechanism. Commonplace should borrow the pattern only for tools with real mutation or exfiltration risk; read-only KB search does not need that ceremony.

**Do not borrow silent promotion into durable authority.** WeKnora's automatic wiki and memory extraction are powerful, but Commonplace should keep generated material in workshop/derived layers until source grounding and review accept it.

## Write side

**Write agency:** `manual` `automatic` - Humans and agents manually create, upload, edit, delete, and query knowledge through the UI, API, CLI, MCP/ClawHub-like surfaces, and wiki tools; the system automatically parses documents, chunks text, generates embeddings, builds graph/wiki-derived artifacts, deduplicates pending wiki ops and wiki pages, injects links, records sessions/messages, extracts conversation memory, and compacts overlong agent context.

**Curation operations:** `consolidate` `dedup` `evolve` `invalidate` - Agent history consolidation summarizes older messages into a compact memory block; wiki summary/index pages and source-derived pages consolidate source documents; wiki pending ops and extracted entity/concept pages are deduplicated; wiki page content, links, source refs, chunk refs, versions, and memory graph relations evolve as documents or conversations arrive; delete/retract handling, archived wiki pages, tombstones, dead-link cleanup, and task dead letters invalidate stale derived surfaces while retaining operational history.

### Trace-learning

**Trace source:** `session-logs` `event-streams` `tool-traces` - The durable conversation-memory path consumes user and assistant messages after a chat turn; streaming final-answer events trigger storage; the agent consolidator's prompt preserves tool execution results, although its summary is an in-context compaction rather than a durable graph write.

**Learning scope:** `per-project` `cross-task` - Conversation memory is scoped by `user_id` and `session_id`, and retrieved by user for later pure-chat turns; KB/wiki memory is scoped by tenant, knowledge base, knowledge IDs, and search targets.

**Learning timing:** `online` `offline` `staged` - Pure-chat memory is retrieved online before completion and stored asynchronously after completion; wiki ingest is staged through task queues, per-KB locks, retries, and dead letters; document parsing/indexing can run asynchronously after upload.

**Distilled form:** `prose` `symbolic` `parametric` - Conversation traces become prose episode summaries and symbolic graph entities/relationships; document/wiki pipelines create prose Markdown, symbolic links/refs/slugs, and parametric embeddings or reranker-ready retrieval state.

**Extraction.** The durable trace oracle is the configured chat model: `AddEpisode()` formats the conversation and requests JSON with summary, entities, and relationships; `RetrieveMemory()` asks the model for query keywords before Neo4j lookup. There is schema-shaped JSON parsing, but no evidence in the inspected code of behavioral ablation tests proving that injected memory improves answer faithfulness.

**Scope and timing.** The memory graph is user-scoped and session-labeled; the wiki/task machinery is KB-scoped. The trace-learning loop is not a general tool-trace learner: tool results are summarized for context-window management, but I found no durable per-tool lesson, rule, skill, or validator generated from tool trajectories.

**Survey fit.** WeKnora fits a hybrid service pattern: runtime traces can become a lightweight graph memory for later prompt injection, while imported documents become a heavier RAG/wiki substrate. It strengthens the survey distinction between durable trace memory and in-turn compaction: both use summaries, but only the Neo4j episode path persists across turns.

## Read-back

**Read-back:** `both` - WeKnora pushes retained material into model context in pipeline paths such as RAG prompt rendering and enabled pure-chat memory retrieval, and it also exposes pull tools and commands for agents/users to search chunks, wiki pages, graph relations, documents, sessions, and KBs.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` `inferred / judgment` - Identifier scopes include tenant, KB, knowledge ID, selected document, wiki slug, tag, user ID, and session; lexical signals include keyword/BM25/wiki regex search and memory entity-name matches; embedding signals drive vector search; judgment signals include query understanding, LLM keyword extraction for memory, reranking, and agent tool choice.

**Faithfulness tested:** `no` - The repository includes tests for services, tools, retrievers, wiki behavior, CLI contracts, and metrics, but I did not find a with/without read-back ablation or post-action audit proving that pushed RAG/memory context changes downstream model behavior faithfully.

Push read-back occurs before a model call. In the RAG path, retrieved and merged contexts are rendered into `chatManage.UserContent` by `PluginIntoChatMessage` before chat completion, and that rendered content is persisted back onto the user message for later history use ([internal/application/service/chat_pipeline/into_chat_message.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/chat_pipeline/into_chat_message.go)). In the pure-chat path, `MEMORY_RETRIEVAL` runs before `CHAT_COMPLETION_STREAM` when memory is enabled; it appends a "Relevant Memory" block to user content ([internal/application/service/session_knowledge_qa.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/session_knowledge_qa.go), [internal/application/service/chat_pipeline/memory.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/chat_pipeline/memory.go)).

Pull read-back is broad. The ReAct agent can call `knowledge_search`, `grep_chunks`, `list_knowledge_chunks`, `query_knowledge_graph`, wiki tools, web tools, data-analysis tools, skills, and wrapped MCP tools, while the CLI exposes agent-friendly commands and a curated read-only MCP server surface ([internal/application/service/agent_service.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/application/service/agent_service.go), [internal/agent/tools/knowledge_search.go](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/internal/agent/tools/knowledge_search.go), [cli/AGENTS.md](https://github.com/Tencent/WeKnora/blob/4bb8906520a9e16ccbf3312a1b65ba36210dbd9e/cli/AGENTS.md)).

Context complexity is actively managed but still high. The system combines retrieved document chunks, generated wiki pages, relation chunks, image OCR/captions, parent-child expansion, history references, memory summaries, tool outputs, web fetches, and data-analysis outputs. The implementation has many bounding mechanisms; it does not make the final context package as inspectable as a file-native KB artifact.

## Curiosity Pass

**"Memory" means several different things in this codebase.** There is durable Neo4j conversation memory, agent context-window consolidation, chat history loading, persisted rendered RAG context, wiki pages, and document chunks. Only the Neo4j episode path clearly qualifies as trace-learning durable memory; the others are RAG state, context compaction, or imported knowledge.

**The memory graph is narrower than the wiki/RAG platform.** It only retrieves for pure chat in the inspected pipeline assembly, not for the RAG path, and it retrieves summaries by LLM-extracted keywords matched against entity names. The richer document/wiki retrieval stack is separate.

**Wiki Mode is closer to a derived KB than a source-preserving Markdown repo.** Pages are Markdown, but they live as database rows with source/chunk refs. That gives the UI and services fast control, but it loses the git-diff and local-file affordances that Commonplace relies on.

**Tool safety is unusually explicit for an agent-facing product.** The CLI and MCP wrapper include structured errors, destructive-action confirmation, approval gates, first-wins tool registration, parameter validation, and output truncation. These are system-definition artifacts, not just convenience code.

**The automatic write side is powerful but epistemically soft.** Deduplication, extraction, reranking, link insertion, and retraction are implemented, but many judgments depend on LLM output and service logs rather than retained reviewable rationales.

## What to Watch

- Whether memory retrieval is added to the RAG pipeline, not only pure chat. That would make the trace-memory layer more central to WeKnora's answer behavior.
- Whether wiki generation gains reviewer-visible rationale, diff, or approval artifacts before updating durable pages. That would make it more borrowable for Commonplace.
- Whether the CLI/MCP surfaces add versioned machine-readable schemas for all streamed events and retry commands. That would strengthen the agent-facing contract.
- Whether trace memory starts retaining tool/action trajectories as durable lessons, skills, or validators. That would move WeKnora beyond conversation-episode recall into trace-learning system improvement.
- Whether read-back faithfulness gains explicit ablation or audit tests. Without that, context injection remains structurally implemented but behaviorally unproven.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: WeKnora stores several knowledge surfaces, and only some are automatically pushed into model context.
- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: WeKnora extracts conversation episodes into a durable graph memory and separately compacts agent history.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: WeKnora's DB rows, vector indexes, graph memory, wiki pages, tools, and task queues differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: chunks, wiki pages, graph episodes, and retrieved search results mostly advise later action as knowledge.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: pipelines, schemas, RBAC, tool registries, approval gates, prompts, and ranking configs route, validate, or enforce behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: WeKnora's main value is routing, ranking, compressing, and injecting retained knowledge into bounded model contexts.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - compares: WeKnora has strong discovery and context-serving machinery, with trust mediated mostly by service governance rather than file-native review.
