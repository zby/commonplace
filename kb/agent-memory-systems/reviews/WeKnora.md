---
description: "WeKnora review: enterprise RAG with hybrid/vector retrieval, Wiki Mode distillation, ReAct tools, skills, and optional Neo4j trace memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-03"
tags: [trace-derived, push-activation]
---

# WeKnora

WeKnora, from Tencent's `Tencent/WeKnora` repository, is an enterprise RAG and agent platform for turning uploaded documents, URLs, FAQs, data-source imports, and chat interactions into queryable knowledge bases. At the reviewed commit, its memory story is not one mechanism: it combines document/FAQ chunk storage, vector plus keyword retrieval, optional graph extraction, ReAct agent tools, agent skills, generated Wiki pages, durable chat history, and an opt-in conversation-memory graph.

**Repository:** https://github.com/Tencent/WeKnora

**Reviewed commit:** [e9980c6011c7cf71501cf500b820168f51fec4b4](https://github.com/Tencent/WeKnora/commit/e9980c6011c7cf71501cf500b820168f51fec4b4)

**Last checked:** 2026-06-03

## Core Ideas

**Knowledge bases are configured retrieval scopes.** A `KnowledgeBase` records type (`document`, `faq`, or `wiki`), tenant ownership, chunking config, embedding model, storage provider, vector-store binding, wiki config, FAQ config, extraction config, and indexing strategy ([internal/types/knowledgebase.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/knowledgebase.go)). This makes a KB both a user-facing collection and a system-definition artifact controlling which indexing and retrieval pipelines exist.

**The standing memory unit is the chunk, not the source file.** Uploaded or manual knowledge rows preserve source metadata and processing status, but query-time memory mostly acts through `Chunk` rows with content, positions, parent/child links, chunk type, relation chunk references, metadata, and enable/status flags ([internal/types/knowledge.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/knowledge.go), [internal/types/chunk.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/chunk.go)). Parent-child chunking stores large parent chunks for context while embedding smaller child chunks; heading-aware chunking can prepend a transient `ContextHeader` to the embedding text.

**Retrieval is hybrid and store-aware.** `HybridSearch()` validates multi-KB authorization, checks embedding-model compatibility, over-retrieves up to a bounded cap, computes one query embedding, groups KBs by backing store, fans out retrieval, then separates vector and keyword results for deduplication or reciprocal-rank fusion ([internal/application/service/knowledgebase_search.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/knowledgebase_search.go), [internal/application/service/knowledgebase_search_fusion.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/knowledgebase_search_fusion.go)). The retriever abstraction supports Postgres, Elasticsearch, Qdrant, Milvus, Weaviate, Doris, SQLite, Tencent VectorDB, and related engines ([internal/types/retriever.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/retriever.go)).

**Context efficiency is layered, but not fully token-budgeted at every boundary.** Ingestion chunks and indexes documents instead of loading whole files; adaptive chunking and parent-child mode reduce retrieval mismatch; hybrid search over-retrieves then caps final results; chat pipeline stages rerank, merge, filter top-k, and render only selected contexts into the LLM prompt ([docs/CHUNKING.md](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/docs/CHUNKING.md), [internal/application/service/chat_pipeline/filter_top_k.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/chat_pipeline/filter_top_k.go), [internal/application/service/chat_pipeline/into_chat_message.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/chat_pipeline/into_chat_message.go)). Agent mode also has a max tool-output character setting and a context-window consolidator for long ReAct histories ([internal/types/agent.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/agent.go), [internal/agent/memory/consolidator.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/agent/memory/consolidator.go)). The main RAG path still depends on configured top-k/template sizes rather than a single end-to-end context budget.

**Agent mode exposes memory as tools and scoped prompt metadata.** The ReAct engine builds a system prompt with bound KB metadata, selected documents, optional skills metadata, web-search status, and current time, then lets the model call tools such as `knowledge_search`, wiki tools, graph query, MCP tools, web fetch/search, and skill tools ([internal/agent/engine.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/agent/engine.go), [internal/agent/prompts.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/agent/prompts.go), [internal/agent/tools/knowledge_search.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/agent/tools/knowledge_search.go)). This is a pull model inside the agent loop: the agent has to decide which retrieval tool to call.

**Wiki Mode is document-derived distillation into durable Markdown pages.** Wiki ingest queues per-document operations, uses LLM prompts to generate summaries, candidate entity/concept pages, chunk citations, and cross-links, and stores pages with slugs, summaries, aliases, source refs, chunk refs, in/out links, metadata, and versioning ([internal/application/service/wiki_ingest.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/wiki_ingest.go), [internal/agent/prompts_wiki.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/agent/prompts_wiki.go), [internal/types/wiki_page.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/wiki_page.go)). The wiki index tool deliberately caps index-overview output for agent consumption ([internal/agent/tools/wiki_tools.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/agent/tools/wiki_tools.go)).

**There is a separate opt-in conversation-memory graph.** When `enable_memory` is true, a chat pipeline plugin retrieves related episode summaries before completion and stores the completed user/assistant exchange afterward. The memory service prompts an LLM to extract a summary, entities, and relationships from the conversation, stores them in Neo4j, and later extracts keywords from the next query to find related episodes ([internal/application/service/chat_pipeline/memory.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/chat_pipeline/memory.go), [internal/application/service/memory/service.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/service/memory/service.go), [internal/application/repository/memory/neo4j/repository.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/application/repository/memory/neo4j/repository.go)). The handler resolves this switch from a per-request override or user preference, defaulting false ([internal/handler/session/qa.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/handler/session/qa.go)).

## Artifact analysis

- **Storage substrate:** `rdbms` - The dominant retained memory lives in relational tables for knowledge bases, knowledge rows, chunks, wiki pages, sessions, messages, task queues, and configuration, with adjunct object storage for original files, vector/keyword stores for retrieval indexes, Neo4j for optional memory/graph features, and Redis for transient wiki locks.
- **Representational form:** `prose` `symbolic` `parametric` - WeKnora combines prose documents and generated Markdown, symbolic rows/configs/tasks/API contracts, vector embeddings and sparse indexes, and graph entities/relationships.
- **Lineage:** `authored` `imported` `trace-extracted` - Operators author KB configs, agents, skills, prompts, and some manual content; uploads, URLs, FAQs, external data-source imports, and source documents are imported; optional conversation memory is extracted from completed chat traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Retrieved chunks, wiki pages, and memory episodes advise answers; KB configs, prompts, skills, tools, RBAC, MCP approvals, parse/index states, ranking stages, and memory extraction shape instruction, enforcement, routing, validation, ranking, and learning paths.

**Knowledge base configuration.** Storage substrate: relational database rows with JSON columns. Representational form: symbolic config with prose name/description fields. Lineage: authored through UI/API/CLI and updated by operators; invalidates retrieval behavior when chunking, indexing strategy, model, storage, or graph/wiki settings change. Behavioral authority: system-definition artifact because it controls parser choice, embedding model, vector-store binding, indexing pipelines, RBAC scope, and which tools/search paths can see a corpus.

**Knowledge rows and source objects.** Storage substrate: relational `Knowledge` records plus provider-backed file/object storage paths. Representational form: mixed source metadata, status flags, hashes, storage paths, manual Markdown payloads, and imported file content. Lineage: imported from uploads, URLs, browser extension, IM channels, Feishu/Notion/Yuque, API, or manual authoring; parse status tracks processing/finalization/failure/cancellation. Behavioral authority: knowledge artifacts until chunked/indexed or distilled; they are evidence and source-of-truth records.

**Chunks and retrieval indexes.** Storage substrate: relational `Chunk` rows plus vector/keyword backend index records. Representational form: mixed prose chunk content, symbolic chunk metadata/links/status, and distributed-parametric embeddings. Lineage: derived from parsed source content through splitters, parent-child chunking, OCR/caption extraction, FAQ import, summary/question/graph/wiki enrichment, and embedding/indexing. Behavioral authority: ranking and context-selection system-definition artifacts because they decide what text reaches the LLM in quick Q&A, RAG chat, and agent retrieval tools.

**Chat sessions and messages.** Storage substrate: relational session/message rows. Representational form: prose message content plus symbolic attachments, mentioned items, images, knowledge references, rendered RAG content, and agent-step traces. Lineage: generated by users, assistants, IM integrations, and agent executions. Behavioral authority: ordinary multi-turn history is a knowledge artifact pushed back into later context when history is enabled; `RenderedContent` preserves the RAG-augmented user message for later turns, while `AgentSteps` are stored for display/history and are explicitly not included in LLM context ([internal/types/message.go](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/internal/types/message.go)).

**Wiki pages.** Storage substrate: relational `wiki_pages` rows, plus synchronized wiki-page chunks for retrieval. Representational form: prose Markdown with symbolic slug, type, source refs, chunk refs, aliases, links, metadata, and version. Lineage: LLM-distilled from source-document chunks and later maintained by ingest/retract/linking code or agent wiki tools; source-document changes can update pages, refs, links, and indexes. Behavioral authority: mixed knowledge and system-definition artifact: pages are knowledge for humans/agents, while their slugs, links, summaries, and index overview route later agent reads.

**Agent configuration, skills, and tools.** Storage substrate: relational/custom-agent config, preloaded skill directories, external skill dirs, MCP service records, and code-level tool definitions. Representational form: mixed symbolic options plus prose system prompts and skill instructions. Lineage: authored by operators, shipped with the app, or loaded from configured skill directories. Behavioral authority: system-definition artifacts that instruct, route, constrain, or extend ReAct behavior through system prompts, allowed tools, skills metadata, sandboxed skill execution, and MCP approval gates.

**Optional conversation-memory graph.** Storage substrate: Neo4j nodes and relationships for episodes, entities, and `RELATED_TO` relationships. Representational form: mixed symbolic graph plus prose summaries/entity descriptions. Lineage: trace-extracted from completed chat exchanges by an LLM when memory is enabled; retrieval uses another LLM prompt to extract query keywords before graph lookup. Behavioral authority: knowledge artifacts pushed as "Relevant Memory" into later chat context; not a hard instruction or validator.

**Agent context-window summaries.** Storage substrate: transient in-memory message arrays during an agent execution. Representational form: prose system summary messages. Lineage: LLM-summarized from older messages when the estimated context exceeds a threshold, with fallback raw archiving. Behavioral authority: temporary context-compression system-definition artifact for the current ReAct run only; it is not persisted as durable memory.

**Promotion path.** The strongest path is source document -> chunks/index -> retrieved context or wiki page -> agent/human action. A separate trace path is chat exchange -> episode graph -> relevant-memory prompt text. WeKnora can promote source-derived content into higher-authority retrieval and navigation surfaces, but it does not show a governed note-to-validator path like Commonplace.

## Comparison with Our System

| Dimension | WeKnora | Commonplace |
|---|---|---|
| Primary purpose | Enterprise self-hosted RAG, agent Q&A, Wiki Mode, IM/API/CLI/MCP access | Git-native methodology KB for agents and maintainers |
| Main substrate | RDBMS rows, object storage, vector/keyword stores, Neo4j, Redis, generated Markdown wiki pages | Git-tracked Markdown collections, type specs, indexes, source snapshots, review reports |
| Retrieval/read-back | Server-side RAG push, ReAct pull tools, optional memory graph push, wiki tools, MCP/CLI | Mostly pull through `rg`, indexes, links, skills, reports, validation/review commands |
| Context efficiency | Chunking, parent-child retrieval, over-retrieve/cap, rerank/merge/top-k, wiki index top-k, tool-output truncation, context consolidation | Human/agent-directed search and loading, generated indexes, collection contracts, validation and review |
| Governance | Tenant RBAC, parse/index states, task queues/DLQs, credentials encryption, MCP approval, retrieval configs | Collection contracts, schemas, deterministic validation, semantic review, git history, archive/replacement workflow |
| Learning loop | Optional conversation-to-episode graph; Wiki Mode distills documents, not traces | Deliberate source-grounded writing, review, validation, and promotion |

WeKnora is much more of an application platform than Commonplace. It solves ingestion, multi-tenant access control, model/provider integration, storage backends, UI, IM channels, APIs, and agent tools. Commonplace is narrower and stronger where durable claims need to be inspectable as files with explicit type contracts, review states, and git diffs.

The closest design overlap is progressive context assembly. WeKnora does this operationally through chunking, retrieval, RRF fusion, rerank/merge/top-k stages, agent tools, and wiki index summaries. Commonplace does it through repository navigation, indexes, link contracts, and review/validation workflows. WeKnora is stronger at automatic activation; Commonplace is stronger at making the authority and lineage of each retained artifact reviewable.

**Read-back:** `both` - Quick Q&A and opt-in memory push retrieved content into the LLM's context before response generation, while ReAct agent mode exposes knowledge, wiki, graph, MCP, and skill tools that the agent deliberately pulls.

### Borrowable Ideas

**Treat retrieval configuration as part of the artifact contract.** WeKnora's KB config binds chunking, embedding, indexing, and storage behavior to the collection. Commonplace could make per-collection retrieval/indexing assumptions more explicit if it adds non-`rg` indexes. Ready when a new index layer exists.

**Separate source chunks from synthesized wiki pages.** Wiki Mode keeps source refs and chunk refs on generated pages. A Commonplace analogue would keep source snapshots, extracted candidate notes, and promoted notes distinct, with citations surviving promotion. Ready as a pattern for future source-ingest workflows.

**Use bounded overview tools for generated wiki navigation.** The wiki index overview caps per-type entries for agent reads. Commonplace generated indexes could expose similarly bounded agent-facing summaries when collections get too large. Needs a concrete index-consumption command.

**Do not treat conversation memory as automatically authoritative.** WeKnora's episode graph is useful as soft context, but it is not reviewed. Commonplace should keep trace-derived observations in a candidate/report lane until promoted by review and validation. Ready as a governance rule.

**Agent-facing CLI and MCP surfaces deserve contracts.** WeKnora's CLI `AGENTS.md` documents JSON envelopes, error hints, retry fields, and streaming event boundaries for agent consumers ([cli/AGENTS.md](https://github.com/Tencent/WeKnora/blob/e9980c6011c7cf71501cf500b820168f51fec4b4/cli/AGENTS.md)). Commonplace command docs could use this level of wire-contract clarity where agents parse command output. Ready now for high-use commands.

**Borrow retrieval fan-out carefully.** Multi-store fan-out plus score normalization is useful for shared/tenant contexts, but Commonplace's file-first repo does not yet need that machinery. Keep it as a future pattern, not an immediate feature.

## Write-side placement

**Write agency:** `manual` `automatic` — operators author KB configuration, agents, skills, prompts, manual content, and request-scoped settings, while ingestion, chunking/indexing, Wiki Mode, task queues, optional memory extraction, and context-window consolidation mutate retained stores.

**Curation operations:** `consolidate` `evolve` `synthesize` — ingestion/chunking/wiki/context summaries compress source and conversation material, wiki ingest/retract/linking updates retained pages and refs over time, and Wiki Mode plus optional conversation-memory extraction generate new pages, episode summaries, entities, and relationships.

### Trace-derived learning

- **Trace source:** `session-logs` `event-streams` - The memory pipeline consumes completed user/assistant session exchanges and is triggered from final-answer or non-streaming chat events.
- **Learning scope:** `per-task` `cross-task` - Memory is scoped by user and session, can affect later turns in the same session, and can be recalled in later sessions for that user.
- **Learning timing:** `online` - Episode extraction runs after a live response completes, and retrieval runs before later chat completion when memory is enabled.
- **Distilled form:** `prose` `symbolic` - The durable memory graph stores prose episode summaries/entity descriptions plus symbolic episode, entity, and relationship nodes and edges.

**Trace source.** WeKnora qualifies as trace-derived learning through the opt-in chat memory pipeline. The raw trace is the completed user/assistant exchange from a session, represented as `types.Message` values and stored separately as normal session history. The memory plugin sees the final answer event or non-streaming response, then calls `AddEpisode()` with a user message and assistant message.

**Extraction.** The extraction oracle is an LLM prompted to produce JSON with a conversation summary, entities, and relationships. The Neo4j repository stores an `Episode` node, `Entity` nodes, `MENTIONS` edges from episode to entity, and `RELATED_TO` edges between entities. Retrieval uses a second LLM prompt to extract keywords from the current query, then finds recent episodes whose mentioned entity names match those keywords.

**Scope and timing.** Scope is per user and per session. Storage happens after the response is complete, so it can only affect later turns or later sessions. Retrieval happens before chat completion when `EnableMemory` is true. The handler resolves the flag from a request override or user preference and defaults false.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), WeKnora belongs in the conversation-to-graph-memory family. It strengthens the survey split between raw traces, distilled knowledge artifacts, and system-definition authority: the episode graph is distilled from traces, but read-back is soft context, not a promoted instruction or validated rule. Wiki Mode is not trace-derived under this rule; it distills source documents into Markdown pages and indexes.

## Read-back placement

**Direction.** Both push and pull. Server-side quick Q&A/RAG retrieves chunks and renders them into the user message before completion. The opt-in memory plugin appends related episode summaries as "Relevant Memory" before completion. ReAct agents can also pull through `knowledge_search`, wiki, graph, web, MCP, and skill tools.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` `inferred / judgment` - RAG push is scoped by selected KBs/documents/tags and tenant/RBAC identifiers, then selected by lexical/keyword and embedding retrieval; memory-graph push uses LLM judgment to extract query keywords for entity lookup.

**Faithfulness tested:** `no` - The review notes Langfuse tracing and evaluation metrics, but no with/without memory ablation showing retrieved memory changes behavior.

**Targeting and signal.** RAG push is `instance` targeting by the current query, selected KBs/documents/tags, tenant/RBAC scope, and retrieval thresholds. The signal is mostly `inferred / embedding` plus lexical/keyword matching and optional reranking. Memory-graph push is `instance` targeting by LLM-extracted query keywords matched against entity names, so it is `inferred / judgment` followed by exact graph lookup. Agent-tool retrieval is pull from the acting model.

**Selection, scope, and complexity.** Selection is governed by KB scope, search targets, over-retrieval caps, vector/keyword thresholds, RRF fusion, rerank/merge/top-k stages, wiki index caps, and tool-output truncation. Context complexity can still be high because retrieved contexts, document headers, FAQ priority blocks, wiki pages, attachments, image descriptions, quoted context, and history can all enter the prompt if enabled.

**Authority at consumption.** Retrieved chunks, wiki pages, and memory episodes are advisory context. Agent configs, allowed tools, skills metadata, MCP approval gates, and system prompts have stronger system-definition authority. Effective faithfulness is not verified from static code; Langfuse tracing and evaluation metrics exist, but I did not find a Synapptic-style with/without memory ablation for whether a retrieved memory changes behavior.

**Other consumers.** Humans consume the same retained state through the web UI, wiki browser/graph, REST API, CLI, MCP server, Chrome extension, mini program, IM integrations, and Langfuse traces. This makes WeKnora a multi-consumer knowledge platform, not just an agent memory backend.

## Curiosity Pass

**The optional memory graph is easy to miss.** The headline product is RAG/Wiki/Agent, but the code includes a classic conversation-to-episode graph memory. It is opt-in, defaults false, and appears wired into pure-chat dynamic pipelines, not the main RAG pipeline assembled in `session_knowledge_qa.go`.

**`RenderedContent` is an understated memory artifact.** WeKnora persists the full RAG-augmented user content back to the message row so later turns can see prior retrieval context. That is not learning, but it is durable read-back of retrieved context across turns.

**Wiki pages are more auditable than many LLM-generated summaries.** `SourceRefs` and `ChunkRefs` make generated pages traceable back to source documents/chunks, while version increments skip pure bookkeeping writes. That is a good lineage discipline even though the pages remain LLM-generated.

**Graph search appears to reuse hybrid search.** `query_knowledge_graph` checks graph config, then calls `HybridSearch()` and formats results with graph-config metadata. That is less graph-native than the README's broad GraphRAG wording might suggest, unless the backing retrieval/indexing path has graph chunks enabled for the KB.

**Skills follow progressive disclosure, but the generated prompt is very forceful.** Skill metadata is always loaded when enabled, and the prompt says skill use is mandatory when applicable. This creates a strong system-definition surface; a poor skill description could over-trigger.

## What to Watch

- Whether `MEMORY_RETRIEVAL` and `MEMORY_STORAGE` become part of RAG/agent pipelines, not only pure-chat paths. That would make trace-derived memory interact with document retrieval and agent tools.
- Whether conversation-memory graph retrieval moves beyond keyword-extracted entity-name matching. Embedding, graph expansion, or faithfulness evaluation would change the read-back classification.
- Whether Wiki Mode gains stronger review, conflict, or citation-validation workflows. Source refs exist, but generated Markdown can still become stale or overconfident.
- Whether graph extraction and graph query become a distinct graph traversal path rather than hybrid search over graph-related chunks. That would make the graph substrate more behavior-shaping.
- Whether the CLI's reserved `_notice`, schema/version fields, and agent-help surfaces become fully wired. That would make WeKnora's agent-facing command contract more mature.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: WeKnora's optional memory graph extracts episode summaries/entities/relations from chat traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: WeKnora couples storage to automatic RAG/memory push in some paths and pull tools in agent mode.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: WeKnora's KB configs, chunks, indexes, wiki pages, sessions, skills, and episode graph differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: source documents, chunks, wiki pages, retrieved contexts, and episode summaries mostly advise answers as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: KB config, retrieval indexes, prompts, tools, skills, RBAC, and approval gates shape or constrain future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: WeKnora's central architecture is routing, filtering, and injecting the right retained knowledge into bounded model context.
