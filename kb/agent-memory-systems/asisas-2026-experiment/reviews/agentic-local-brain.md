---
description: "Agentic Local Brain review: local PKM capture into Markdown, SQLite, Chroma vectors, mining tables, RAG chat traces, and recommendation ranking"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# Agentic Local Brain

Agentic Local Brain, from `agent-creativity/agentic-local-brain`, is a local personal knowledge-base application for collecting files, webpages, bookmarks, papers, emails, and notes, then querying them through CLI search, a FastAPI web UI, semantic search, keyword search, and enhanced RAG chat. The implementation is a PKM/RAG system more than an autonomous agent framework: it stores user-provided knowledge, derives search/mining structures, persists RAG conversations and reading history, and uses those retained surfaces to assemble future answers and recommendations.

**Repository:** https://github.com/agent-creativity/agentic-local-brain

**Reviewed commit:** [d1e5f846351a8433edea54053ddb5fc3158229c6](https://github.com/agent-creativity/agentic-local-brain/commit/d1e5f846351a8433edea54053ddb5fc3158229c6)

**Last checked:** 2026-06-04

## Core Ideas

**Collected knowledge is retained twice: Markdown as the inspectable source, SQLite as the index of record.** Collectors write Markdown files with YAML frontmatter under the configured data directory, while collection commands add a `knowledge` row, tags, chunks, and file paths to SQLite ([kb/collectors/base.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/collectors/base.py), [kb/commands/collect.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/commands/collect.py), [kb/storage/sqlite_storage.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/storage/sqlite_storage.py)). The Markdown is adoption-friendly because it remains readable and editable; the SQLite rows carry the behavior-shaping metadata and relations the app uses.

**Semantic recall is a Chroma chunk index beside the SQLite metadata store.** `_index_content_for_search()` chunks collected content, embeds each chunk, writes embeddings and documents to Chroma, then saves chunk metadata in SQLite ([kb/commands/utils.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/commands/utils.py), [kb/storage/chroma_storage.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/storage/chroma_storage.py)). Semantic search embeds the query, applies optional tag/page filters, queries Chroma, and falls back to keyword search when embeddings fail ([kb/query/semantic_search.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/semantic_search.py)).

**Mining converts collected documents into graph, relation, topic, and wiki views.** After a knowledge row is inserted, a background mining worker can extract entities, generate document-level embeddings, and build cross-document relations; topic clustering and wiki compilation are batch/global operations that write topic clusters, document-topic assignments, wiki categories, and wiki articles ([kb/storage/sqlite_storage.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/storage/sqlite_storage.py), [kb/processors/mining_worker.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/mining_worker.py), [kb/processors/topic_clusterer.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/topic_clusterer.py), [kb/processors/wiki_compiler.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/wiki_compiler.py)).

**Enhanced RAG is a pipeline with graceful degradation.** The web dependency layer wires semantic search, keyword search, LLM query expansion, LLM reranking, graph context, topic context, reading-history personalization, conversation history, prompt templates, and a hierarchical context builder, replacing unavailable LLM services with no-op components where possible ([kb/web/dependencies.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/web/dependencies.py), [kb/query/retrieval_pipeline.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/retrieval_pipeline.py)).

**Context efficiency is explicit but heuristic.** Retrieval limits candidates with top-k, score thresholds, tag/page filters, RRF fusion, rerank caps, graph/topic enrichment toggles, and a token-budgeted context builder that truncates topic/entity/source sections ([kb/query/semantic_search.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/semantic_search.py), [kb/query/retrieval_pipeline.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/retrieval_pipeline.py), [kb/query/context_builder.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/context_builder.py)). This controls volume; it does not prove that the selected material is faithful, complete, or non-diluting.

**The trace surface is session-local and recommendation-oriented.** RAG chat persists conversation turns in a separate SQLite database and injects recent turns back into later questions in the same session; web reads/searches/RAG queries also write `reading_history`, which can boost retrieved chunks and generate recommendations from recent views ([kb/query/conversation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/conversation.py), [kb/query/reading_history.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/reading_history.py), [kb/processors/recommendation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/recommendation.py), [kb/web/routes/search.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/web/routes/search.py), [kb/web/routes/items.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/web/routes/items.py)).

## Artifact analysis

- **Storage substrate:** `sqlite` — Markdown captures live in the filesystem and chunk embeddings live in persistent Chroma, but the operational source for most behavior-shaping metadata, mining state, conversations, and reading history is SQLite.
- **Representational form:** `prose` `symbolic` `parametric` — captured Markdown and generated summaries/wiki articles are prose, SQLite/frontmatter/config/tool schemas are symbolic, and Chroma/document embeddings are distributed-parametric state.
- **Lineage:** `authored` `imported` `trace-extracted` — users author notes/tags/summaries and import external sources; the system derives summaries, chunks, embeddings, entities, relations, topics, wiki articles, conversation logs, and reading-history records from those inputs and interactions.
- **Behavioral authority:** `knowledge` `routing` `ranking` `learning` — stored items and generated views supply evidence/context; tags, topics, entities, and query expansion route retrieval; vector/keyword/RRF/rerank/reading-history scores rank context; mining, recommendation, and conversation-history paths learn from prior content or traces. I did not find hard enforcement or validation authority over agent behavior.

**Collected Markdown files.** Storage substrate: files under `~/.knowledge-base/1_collect/...` by default. Representational form: prose body plus YAML frontmatter. Lineage: imported from local files, webpages, bookmarks, papers, emails, or authored notes. Behavioral authority: knowledge artifacts; they become RAG context only after indexing or lexical search.

**SQLite metadata and mining tables.** Storage substrate: `metadata.db`, with `knowledge`, `tags`, `chunks`, FTS, entity graph, document relations, document embeddings, topic clusters, reading history, and wiki tables. Representational form: symbolic rows with prose fields and some serialized embeddings. Lineage: partly authored/imported via collection and partly derived by extraction, mining, clustering, and usage tracking. Behavioral authority: routing and ranking input for search, graph/topic enrichment, recommendations, and web views.

**Chroma chunk index.** Storage substrate: persistent Chroma under the configured storage path. Representational form: parametric embeddings plus stored chunk text and symbolic metadata. Lineage: derived from collected Markdown by chunking and embedding. Behavioral authority: ranking input and knowledge-context supplier for semantic search and RAG.

**Conversation sessions.** Storage substrate: SQLite `conversations.db` with `rag_conversations` and `rag_conversation_turns`. Representational form: symbolic rows containing prose user/assistant turns and source metadata. Lineage: trace-extracted from RAG chat requests and answers. Behavioral authority: push context within the same RAG session, because recent turns are formatted and injected before later answers.

**Reading history.** Storage substrate: SQLite `reading_history`. Representational form: symbolic event rows with action type, query, document id, and timestamp. Lineage: trace-extracted from web item views, searches, and RAG queries. Behavioral authority: ranking and recommendation input; the enhanced RAG pipeline can boost recently viewed documents, while the recommendation engine builds a decayed user profile from recently viewed document embeddings.

**Generated wiki articles and categories.** Storage substrate: Markdown files under the wiki directory plus SQLite `wiki_articles` and `wiki_categories` rows. Representational form: prose articles/cards plus symbolic source-doc/entity/category metadata. Lineage: synthesized from topic clusters, source documents, and entity graphs. Behavioral authority: knowledge artifacts and navigation surfaces; they are stronger summaries than raw search hits but not automatically validated as true.

**Promotion path.** Local Brain promotes imported/authored material into Markdown captures, then into SQLite rows, chunks, embeddings, mined graph/topic views, and optional wiki articles. The trace-derived path promotes interaction traces into conversation context or reading-history ranking, but not into durable agent instructions.

## Comparison with Our System

| Dimension | Agentic Local Brain | Commonplace |
|---|---|---|
| Primary purpose | Personal local PKM and RAG over collected material | Git-tracked methodology KB for agents and maintainers |
| Main substrate | Markdown captures, SQLite metadata/mining tables, Chroma vectors, web/API state | Typed Markdown collections, schemas, indexes, source snapshots, validation and review reports |
| Retained unit | Knowledge item plus chunks, tags, embeddings, graph/topic/wiki derivatives | Typed artifact with frontmatter, links, status, citations, and validation rules |
| Write path | CLI/web/user collection plus automatic extraction, indexing, mining, wiki compilation, trace logging | Deliberate writing/review/promotion with deterministic validation and semantic review gates |
| Read-back | Search/RAG pull plus session-history and reading-history push into web RAG/recommendations | Mostly pull via `rg`, indexes, links, skills, and explicit review workflows |
| Governance | Duplicate hashes, foreign keys, graceful degradation, retention/backup features; weak claim-level review | Collection contracts, schemas, git history, validation, review comments, and source-pinned claims |

Local Brain is more runtime-oriented than Commonplace. It gives a user a practical ingestion and RAG surface with vectors, graph/topic enrichment, and a web UI. Commonplace gives agents a reviewable methodology library where claims are source-pinned, typed, and validated. The systems share an appreciation for plain files, but Local Brain treats files as an ingestion/search substrate, while Commonplace treats files as the durable authority surface.

The biggest divergence is authority discipline. Local Brain will synthesize tags, summaries, topic labels, wiki articles, and answer context automatically; the code has fallbacks and budgets, but the generated claims do not carry per-claim citations, reviewer status, or invalidation contracts. That is reasonable for a personal tool where retrieval usefulness matters. It is not enough for Commonplace's promoted methodology notes.

### Borrowable Ideas

**Keep inspectable captures beside machine indexes.** Ready now as a design criterion. Local Brain's Markdown-plus-SQLite/Chroma split is a useful reminder that vector indexes should be rebuildable access structures, not the only place knowledge exists.

**Use graceful degradation as an adoption affordance.** Ready where it does not hide quality loss. Local Brain falls back from LLM/embedding paths to keyword or no-op components, which keeps the app usable; Commonplace could be explicit when a workflow is running in degraded mode.

**Separate conversation history from durable knowledge.** Ready now. Conversation turns are useful short-horizon context, but Local Brain keeps them in a session database rather than promoting them straight into the knowledge collection.

**Mine graph/topic views as derived navigation, not truth.** Needs a concrete Commonplace use case. Entity/topic relations could help exploration, but they should remain generated views until reviewed.

**Use reading traces for recommendations, not instruction promotion.** Ready as a cautious experiment. View/query history can rank "what to inspect next" without becoming behavioral policy.

## Write side

**Write agency:** `manual` `automatic` — humans add notes and collect/import sources through CLI/web commands, while the system automatically extracts tags/summaries, updates Markdown frontmatter, writes SQLite rows, chunks and embeds content, indexes Chroma, mines entities/relations/topics, compiles wiki artifacts, records conversations, and records reading/search/RAG events.

**Curation operations:** `consolidate` `dedup` `synthesize` `evolve` — smart extraction compresses documents into summaries/tags; duplicate hashes can skip already-collected content; topic/wiki compilation synthesizes derived articles/categories from multiple documents; topic centroid/document-count updates evolve existing topic records during incremental classification. Index/embedding rebuilds are access-structure upkeep, not counted as curation.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — RAG chat turns are stored as session conversations, and web item views/searches/RAG queries are stored as reading-history events.

**Learning scope:** `per-project` — the retained traces are scoped to the local knowledge base and RAG session, not a cross-repository user profile.

**Learning timing:** `online` — chat turns and reading-history events are recorded during web/API interactions and can affect later calls or recommendations.

**Distilled form:** `prose` `symbolic` `parametric` — conversation history is re-served as prose with symbolic turn metadata; recommendation builds a decayed profile from recently viewed document embeddings; reading-history boosts are symbolic ranking adjustments.

**Extraction.** The conversation loop writes the user question and assistant answer after a pipeline run, then later formats recent turns into prompt text for the same session. The reading-history loop records `view`, `search`, and `rag_query` events; the enhanced RAG pipeline can boost recently viewed documents by `+0.1`, while the recommendation engine computes a time-decayed weighted average of recent document embeddings and ranks similar unread documents. The oracle is mechanical, not reflective: there is no LLM judge deciding that a trace should become a durable rule.

**Survey placement.** Local Brain belongs in the trace-to-session-context and trace-to-ranking families, not the trace-to-instruction family. It weakens any broad claim that trace-derived systems must produce new prose rules: here the durable trace mostly changes prompt continuity and ranking/recommendation behavior.

## Read-back

**Read-back:** `both` — users and agents can pull memory through semantic search, keyword search, tag search, RAG, graph/topic/wiki endpoints, and recommendations; retained conversation history and reading-history signals are also pushed into enhanced RAG/recommendation paths without a separate agent lookup.

**Read-back signal:** `coarse` `inferred / embedding` `inferred / lexical` `inferred / judgment` — conversation history is coarse session recall, semantic search and recommendations use embeddings, keyword fallback uses lexical search, and query expansion/reranking can use LLM judgment when configured.

**Faithfulness tested:** `no` — the code assembles and injects context, but this review did not find a with/without ablation or post-answer audit proving the model used the pushed memory faithfully.

**Direction edge cases.** Ordinary CLI search and RAG are pull from the user's perspective: a query asks the store for results. Enhanced RAG conversation history is push to the answering model: when a session id is present or created, recent retained turns are formatted and included before answer generation. Reading-history personalization is also push-like for the model and user because recent views can alter ranking without being requested in the current question.

**Targeting and signal.** Conversation read-back is `coarse`: it loads recent turns from the current session, capped by configured history turns and a 4000-character approximation in `format_history_for_prompt()`. Retrieval is instance-targeted by inferred signals: Chroma embedding similarity, keyword search, optional LLM query expansion, optional LLM reranking, graph/entity matches, topic assignments, and reading-history boosts.

**Injection point.** The enhanced pipeline loads conversation history before query expansion, retrieval, and answer generation, then prompt templates render previous conversation, topic context, entity context, and retrieved chunks before the LLM call. New turns and reading-history events are written after the request, so they affect later interactions.

**Selection, scope, and complexity.** Default RAG retrieves a small top-k; enhanced retrieval fetches more candidates, fuses keyword and semantic results, reranks to a smaller set, adds graph/topic context, and uses a token-budgeted context builder. The selection policy is implemented, but runtime precision, recall, and context dilution are not established by code alone.

**Authority at consumption.** Retrieved chunks, generated topic/entity context, and conversation history are advisory context for answer generation. Reading history has ranking influence. None of these paths is an enforcement gate; the model can ignore or misuse the supplied context.

**Other consumers.** Humans consume the same state through CLI commands, FastAPI routes, the web UI, dashboard statistics, recommendation endpoints, wiki views, backup/restore, and direct Markdown files.

## Curiosity Pass

The implementation's default storage paths are split between `~/.localbrain` for config/runtime state and `~/.knowledge-base` for data. That split helps packaging but makes the retained artifact boundary less obvious than a single repo-root knowledge base.

The README's "agent" installation path is mostly an adoption route. The inspected code does not expose a Claude/Codex-style memory hook that pushes Local Brain content into arbitrary coding-agent sessions; the implemented push path is inside Local Brain's own RAG/web pipeline.

The mining worker uses `summary or ""` as the content passed after `add_knowledge()`, so per-document entity extraction after collection may depend on the extracted/provided summary rather than the full saved Markdown. That is a context-efficiency choice, but it may lower graph recall for long documents.

Generated wiki articles are the most knowledge-like derived artifacts. They could become a strong personal reference layer, but without claim-level citations or validation they remain convenience summaries rather than reviewed knowledge.

## What to Watch

- Whether Local Brain grows an MCP/server or assistant-memory integration that injects retrieved context into external coding agents. That would change read-back from app-local RAG to broader agent push.
- Whether wiki articles gain source-span citations or staleness-driven invalidation tied to source document changes. That would make synthesized artifacts more reviewable.
- Whether reading-history personalization moves from simple boosts/recommendations into durable preference models. That would strengthen the trace-derived classification and raise governance concerns.
- Whether mining reads full document content instead of summaries for entity extraction. That would improve graph coverage but increase cost and noise.
- Whether the system adds faithfulness tests for RAG answers, such as source-grounding audits or with/without context checks.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Local Brain's stored Markdown/SQLite/vector state from the specific RAG and conversation-history paths that activate it.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts with Local Brain's trace use: traces affect session context and ranking, not durable instructions.
- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places Local Brain in trace-to-ranking/session-context rather than trace-to-policy.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - helps separate Local Brain's knowledge artifacts from ranking, routing, and learning surfaces.
- [Behavioral authority](../../../notes/definitions/behavioral-authority.md) - applies to the difference between advisory RAG context, retrieval ranking, and generated derived views.
