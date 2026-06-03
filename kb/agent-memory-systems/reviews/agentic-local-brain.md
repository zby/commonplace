---
description: "Agentic Local Brain review: local PKM with Markdown capture, SQLite metadata/graph state, Chroma vectors, enhanced RAG, wiki synthesis, and usage-trace personalization"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
tags: [trace-derived, push-activation]
---

# Agentic Local Brain

Agentic Local Brain, from `agent-creativity/agentic-local-brain`, is a personal knowledge management system for collecting files, webpages, papers, email, bookmarks, and notes into a local searchable "brain." At the reviewed commit, it is a Python package with a Click CLI, FastAPI web API, agent-installable collection skill, Markdown capture files, SQLite metadata/mining state, ChromaDB vector storage, hybrid RAG, knowledge mining, recommendations, backup scheduling, and LLM-generated wiki articles.

**Repository:** https://github.com/agent-creativity/agentic-local-brain

**Reviewed commit:** [d1e5f846351a8433edea54053ddb5fc3158229c6](https://github.com/agent-creativity/agentic-local-brain/commit/d1e5f846351a8433edea54053ddb5fc3158229c6)

**Last checked:** 2026-06-03

## Core Ideas

**The collection skill makes the agent the front door.** The README's first install path asks a desktop agent to install or update the `localbrain-collect` skill, and the skill gives the agent intent-recognition rules for whether a user request should become a file, webpage, paper, bookmark, or note collection ([README.md](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/README.md), [skills/localbrain-collect/SKILL.md](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/skills/localbrain-collect/SKILL.md)). The skill is not the memory store itself; it is an agent-facing operating manual for feeding the store correctly.

**Captured content is retained as Markdown, but the operational memory lives in databases.** Collectors write Markdown files with YAML frontmatter under the configured data directory, while `SQLiteStorage` maintains knowledge items, tags, chunks, entities, relations, document embeddings, topic clusters, reading history, and wiki registries ([kb/collectors/base.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/collectors/base.py), [kb/storage/sqlite_storage.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/storage/sqlite_storage.py)). ChromaDB stores chunk embeddings and source metadata for semantic retrieval ([kb/storage/chroma_storage.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/storage/chroma_storage.py), [kb/commands/utils.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/commands/utils.py)).

**Context efficiency is implemented as retrieval and assembly policy, not progressive file navigation.** The basic semantic path embeds the query, asks Chroma for `top_k` chunks, filters by tags/page metadata, and falls back to keyword search if embedding fails ([kb/query/semantic_search.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/semantic_search.py)). The enhanced pipeline expands queries, fuses semantic and keyword results with reciprocal-rank fusion, optionally reranks, enriches with graph/topic/history context, and builds a token-budgeted prompt with default budgets of 4000 context tokens and five reranked sources ([kb/query/retrieval_pipeline.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/retrieval_pipeline.py), [kb/query/context_builder.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/context_builder.py), [kb/config-template.yaml](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/config-template.yaml)). Volume is bounded; complexity is higher than a simple note graph because chunks, entities, topics, conversation turns, and recommendations can all influence a response.

**Extraction degrades from LLM to built-in heuristics.** Tag and summary extraction first respects user-supplied metadata, then uses a LiteLLM-backed provider, then falls back to a local TF-IDF-like tagger and extractive summarizer ([kb/processors/tag_extractor.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/tag_extractor.py), [kb/processors/builtin_extractor.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/builtin_extractor.py)). That is a strong adoption affordance: capture can continue without a configured model, though semantic search, entity extraction, wiki synthesis, and answer generation degrade or disappear when model services are absent.

**Knowledge mining turns collected documents into derived structure.** New knowledge rows start an asynchronous mining thread that attempts entity extraction, document embedding, and cross-document relation building without blocking collection ([kb/storage/sqlite_storage.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/storage/sqlite_storage.py), [kb/processors/mining_worker.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/mining_worker.py)). Batch mining adds topic clustering and wiki compilation; entity/relation extraction and wiki compilation use LLM prompts, while document relations can come from embedding similarity and shared entities ([kb/processors/entity_extractor.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/entity_extractor.py), [kb/processors/doc_relation_builder.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/doc_relation_builder.py), [kb/processors/mining_runner.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/mining_runner.py)).

**Usage traces feed later ranking and recommendations.** The web API records item views, searches, and RAG queries in `reading_history`; the enhanced RAG pipeline can boost recently viewed documents, and the recommendation engine builds a time-decayed embedding profile from recent reads ([kb/query/reading_history.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/reading_history.py), [kb/web/routes/items.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/web/routes/items.py), [kb/web/routes/search.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/web/routes/search.py), [kb/processors/recommendation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/recommendation.py)). Multi-turn RAG conversations are stored separately in SQLite and injected into later prompts for the same session ([kb/query/conversation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/conversation.py)).

## Artifact analysis

- **Storage substrate:** `sqlite` - The central operational memory is SQLite: knowledge metadata, tags, chunk records, entity graph tables, document relations, topic clusters, reading history, wiki registries, and RAG conversation databases. Markdown files and Chroma vectors are important side substrates, but SQLite is where the system composes most behavior-shaping state.
- **Representational form:** `mixed` - LocalBrain combines prose Markdown captures, symbolic SQLite rows/frontmatter/config/tool schemas, graph and topic tables, JSONL run logs, executable Python pipelines, and distributed-parametric embeddings in ChromaDB and SQLite BLOBs.

**Collected Markdown files.** Storage substrate: files under the configured data directory, especially collection subdirectories such as files, URLs, papers, bookmarks, emails, and notes. Representational form: prose Markdown with YAML frontmatter. Lineage: imported from user files, fetched webpages, email/bookmark/paper sources, or direct notes; invalidated by source edits, duplicate hashes, refetches, or manual file changes that are not automatically reconciled into every derived projection. Behavioral authority: knowledge artifacts for later search, reading, RAG context, and wiki synthesis.

**SQLite metadata and graph state.** Storage substrate: `metadata.db` under the configured data directory. Representational form: symbolic relational rows for knowledge items, tags, chunk metadata, entities, entity mentions, entity relations, document embeddings, document relations, topic clusters, topic membership, reading history, wiki articles, and wiki categories. Lineage: partly authored/imported during collection, partly derived by chunking, LLM extraction, embedding, clustering, relation mining, web interaction tracking, and wiki compilation. Behavioral authority: system-definition artifact for routing, filtering, ranking, topic enrichment, graph enrichment, recommendations, dashboards, and backup/restore accounting.

**Chroma vector collection.** Storage substrate: persistent ChromaDB under the configured `storage.persist_directory`. Representational form: distributed-parametric vectors plus symbolic metadata and stored chunk text. Lineage: derived from current collected Markdown chunks by the configured embedder; collection failures do not block capture, and embeddings can drift from source files if content changes without re-indexing. Behavioral authority: ranking and selection authority for semantic retrieval and RAG context.

**Enhanced retrieval pipeline state.** Storage substrate: repository Python code plus runtime in-memory cache and configured services. Representational form: symbolic retrieval policy, prompt templates, cache keys, ranking scores, and optional LLM-generated query expansions/rerank scores. Lineage: authored code/config plus transient derivations from queries, conversations, search results, graph rows, topic rows, and reading-history rows. Behavioral authority: strong system-definition artifact because it decides which retained content reaches the LLM, in what order, with what token budget and prompt framing.

**Knowledge mining outputs.** Storage substrate: SQLite entity/relation/topic/wiki tables, optional wiki Markdown files, document embedding BLOBs, and mining JSONL history. Representational form: mixed symbolic graph/topic rows, prose/wiki articles, and parametric document embeddings. Lineage: derived from collected documents by LLM extraction, embedding similarity, shared-entity matching, HDBSCAN clustering, subcategory generation, and LLM wiki synthesis. Behavioral authority: ranking, recommendation, enrichment, and reference authority; quality of extracted entities, relations, topics, and wiki prose is not verified by an implemented review gate.

**Agent skill and CLI/API contracts.** Storage substrate: `skills/localbrain-collect/SKILL.md`, Click command modules, FastAPI route modules, config template, and package metadata. Representational form: prose instructions plus symbolic command/API schemas. Lineage: authored repository artifacts. Behavioral authority: system-definition artifacts for agents and users; they define allowed collection operations, intent routing, background server controls, search/RAG endpoints, and model/provider configuration.

**Usage traces and conversations.** Storage substrate: `reading_history` in SQLite and `conversations.db` tables for RAG sessions. Representational form: symbolic event rows and prose conversation turns, with source snapshots serialized as JSON. Lineage: trace-extracted from user views, searches, RAG queries, and generated RAG turns. Behavioral authority: read-back and ranking influence: recent views can boost chunks, recommendations derive a profile from reading history, and conversation turns are pushed into later RAG prompts for the same session.

**Promotion path.** LocalBrain's main path is source -> Markdown capture -> SQLite metadata/chunks/tags -> Chroma vectors -> retrieval/RAG; a second path is captured documents -> entity/document/topic mining -> wiki articles and recommendations. A usage-trace path records views/searches/RAG turns -> reading-history or conversation rows -> ranking boosts, recommendations, or session-context injection. The system has no Commonplace-like promotion from candidate claim to reviewed library artifact; authority increases by being indexed, mined, clustered, retrieved, or injected, not by passing a validation/review lifecycle.

## Comparison with Our System

| Dimension | Agentic Local Brain | Commonplace |
|---|---|---|
| Primary purpose | Personal/local knowledge collection, search, RAG, mining, wiki, and web UI | Git-native methodology KB with typed artifacts, validation, reviews, source snapshots, and indexes |
| Main substrate | SQLite metadata/graph/history, Chroma vectors, Markdown capture files | Git-tracked Markdown collections, type specs, reports, generated indexes |
| Agent-facing surface | Agent collection skill, CLI, FastAPI web API, background server | Repository instructions, skills, deterministic commands, search, validation/review workflows |
| Context strategy | Semantic/keyword/hybrid retrieval, reranking, graph/topic/history enrichment, token-budgeted prompt assembly | `rg`, authored links/indexes, collection contracts, type specs, review reports, targeted skill workflows |
| Trace use | Reading/search/RAG history and conversation turns affect recommendations, ranking, and session prompts | Trace-derived learning is mostly explicit source/review/workshop practice, not an automatic runtime personalization loop |
| Governance | Config, command/API boundaries, graceful degradation, diagnostics, backup/restore | Collection contracts, schemas, validation, semantic review gates, replacement archives |
| Read-back | Both: explicit search/RAG pulls plus session-history/history-personalized prompt assembly | Mostly pull through search, links, skills, reports, and validation/review procedures |

LocalBrain is farther from Commonplace than the file-first Markdown systems. It keeps captured content inspectable as Markdown, but its practical memory architecture is a service database plus vector index plus web/CLI/RAG application. That makes it better at product workflows - ingesting heterogeneous sources, answering questions, running a local web UI, backing up state, recommending unread material - and weaker as a methodology KB where every durable claim needs a typed role, review surface, and maintainable citation path.

The most relevant Commonplace contrast is lineage authority. LocalBrain derives many useful projections from source material: tags, summaries, entities, relations, topics, wiki pages, rankings, and recommendations. The code usually records enough row-level source ids to navigate back to documents, but it does not have a review gate that distinguishes "LLM extracted this" from "this claim is validated enough to shape future work." Commonplace should treat that as the governance cost of adopting mining and synthesis layers.

LocalBrain's context assembly is more automated than Commonplace's current search/navigation path. The enhanced pipeline is a concrete example of a context-engineering service: query expansion, hybrid fusion, reranking, enrichment, budgeting, answer generation, and conversation persistence are all in one runtime loop. The tradeoff is opacity and dependency: once ranking, topic context, entity extraction, reading history, and conversation turns enter the prompt together, a reviewer needs tooling to explain why a particular answer saw a particular context bundle.

**Read-back:** `both` - Users and agents can pull memory through CLI/API search and RAG, while the web enhanced-RAG path pushes retained conversation history and usage-personalized retrieval state into the answering LLM without the model first requesting those memories.

### Borrowable Ideas

**Treat degraded capture as a first-class mode.** LocalBrain's tag/summary path can fall back from LLM extraction to built-in heuristics. A Commonplace capture/workshop lane could borrow this: preserve the source and create a low-authority seed artifact even when expensive extraction or semantic review is unavailable. Ready for capture workflows, not for library promotion.

**Separate capture success from indexing success.** LocalBrain generally lets collection succeed even if semantic indexing or mining fails. Commonplace could use the same principle for snapshot/ingest: retain source first, then make derived indexes/reports explicitly stale or missing. Ready now as an operational stance.

**Make context packs explainable.** The enhanced retrieval pipeline exposes stages and structured results. A Commonplace context-pack command should similarly report which search, link, type, review, or index stage selected each artifact. Needs a concrete consumer before implementation.

**Use interaction traces cautiously for ranking, not authority.** LocalBrain's reading-history boost and recommendation profile are useful low-stakes personalization. Commonplace could borrow usage traces for "recently useful" suggestions, but not for promoting notes to instructions or validators. Needs policy before use.

**Do not borrow database opacity for core library artifacts.** SQLite and Chroma are productive operational substrates, but Commonplace's durable methodology knowledge should remain reviewable as Git-tracked Markdown. A database layer would be better as a derived index, queue, cache, or telemetry store.

**Wiki synthesis needs a review lane before it can become knowledge.** LocalBrain's LLM wiki compiler is a plausible synthesis interface. In Commonplace, generated synthesis should land in workshop/report space until citations, lineage, and review status are explicit.

## Trace-derived learning placement

**Trace source.** LocalBrain qualifies as trace-derived through usage and conversation traces, not through autonomous agent skill learning. The implemented traces are item view events, search queries, RAG query events, RAG conversation turns, and mining-run history records ([kb/query/reading_history.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/reading_history.py), [kb/query/conversation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/conversation.py), [kb/processors/mining_runner.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/mining_runner.py)). It does not appear to mine Claude/Codex tool transcripts into rules or patches.

**Extraction.** The strongest trace-to-behavior path is lightweight and mostly deterministic. Web routes record events; `ReadingHistory` stores them; the enhanced retrieval pipeline uses recent views to boost matching retrieved chunks; the recommendation engine computes a time-decayed average embedding over recently read documents to recommend similar unread documents; the conversation manager stores user/assistant turns and formats recent turns into the next prompt for the same session ([kb/web/routes/search.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/web/routes/search.py), [kb/processors/recommendation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/processors/recommendation.py), [kb/query/retrieval_pipeline.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/retrieval_pipeline.py)). The oracle is user behavior plus recency/similarity heuristics, not an LLM judge deciding that a trace should become a validated rule.

**Scope and timing.** Reading-history personalization is local to the user's database and recent interaction window. Conversation read-back is per RAG session and bounded by a configured recent-turn limit and 4000-character history formatter. Mining-run history is operational telemetry for the system, not direct behavioral memory for answers. Timing is online for view/search/RAG event recording and prompt injection, but offline/batch for mining and wiki compilation.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), LocalBrain belongs in the usage-trace personalization family. It strengthens the survey split between raw trace preservation and distilled behavior-shaping artifacts: conversation rows are raw-ish transcript memory, reading-history rows are symbolic trace facts, recommendation profiles are transient parametric summaries, and ranking boosts are read-time system-definition effects. It does not strengthen the stronger "trace -> durable skill/rule/validator" pattern.

## Read-back placement

**Direction.** Both. Explicit CLI/API searches and RAG queries are pull. Enhanced RAG also pushes retained session history into the LLM prompt and lets recent reading history influence retrieval ranking without the answering model issuing a separate memory lookup.

**Targeting and signal.** Conversation read-back is `instance`-targeted by `session_id`; the relevant identifier already exists in the chat request. Reading-history ranking boost is coarser: it favors documents recently viewed by the user if they also appear in the current retrieved chunk set. Retrieval itself is inferred lexical/vector relevance from the question plus optional tags.

**Timing relative to action.** Conversation history and retrieved context are assembled before the answer-generation LLM call, so they can change the next answer. Reading-history events are recorded after views/searches/RAG calls and can only affect later recommendations or RAG runs.

**Selection, scope, and complexity.** Selection is bounded by `top_k`, RRF candidate counts, rerank top-k, context budget, conversation history turn limits, and a hard 4000-character cap in `format_history_for_prompt` ([kb/query/conversation.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/conversation.py), [kb/query/retrieval_pipeline.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/query/retrieval_pipeline.py)). Complexity remains high because a final answer may reflect original chunks, query rewrites, semantic scores, keyword matches, graph entities, topic labels, recent views, prior conversation, and prompt-template choice.

**Authority at consumption.** Search results, collected files, wiki articles, and conversation turns are knowledge artifacts when used as context. Retrieval policy, ranking boosts, prompt templates, and conversation injection are system-definition artifacts because they select and format what the LLM sees. None is a hard gate on user action.

**Faithfulness.** I found no implemented with/without ablation, perturbation test, or post-answer audit proving that reading-history boosts, topic/entity enrichment, or conversation-history injection improve or control model behavior. The read-back mechanism is code-grounded; behavioral uptake is not verified from static source.

**Other consumers.** Humans consume the same memory through the web dashboard, item pages, tags, graph/topic/wiki routes, recommendations, backup UI, and CLI. Those are real consumer surfaces, but the read-back classification above is specifically about retained memory entering a future answer/action context.

## Curiosity Pass

**The project name says "local brain," but default configuration assumes cloud model services.** Capture and keyword search degrade locally, but the default embedding and LLM settings point to DashScope/LiteLLM-compatible services ([kb/config.py](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/config.py), [kb/config-template.yaml](https://github.com/agent-creativity/agentic-local-brain/blob/d1e5f846351a8433edea54053ddb5fc3158229c6/kb/config-template.yaml)). The system is local in storage/control more than in model execution.

**There are two "knowledge bases" in one package.** One is the user content store and RAG system. The other is the installed agent skill that instructs external agents how to collect content. They interact, but the skill is a behavior-shaping front end rather than retained user memory.

**The wiki compiler is synthesis, not validation.** It produces standalone articles, entity cards, wiki links, categories, source doc ids, and versions, but I did not find a review/check step that verifies generated claims against sources before they become browseable memory.

**The graph is document-derived and bounded by extraction quality.** Entity and relation rows can improve context, but relation types are from a small controlled set and extraction is LLM-prompted over truncated content. That is useful for navigation, weaker for factual authority.

**Reading history is a small but real authority path.** A recent view can change chunk order, and recent reads can define recommendation output. That is not "learning a rule," but it is retained behavior changing later behavior.

**The backup system is part of memory governance.** Backup/restore, retention, and cloud targets do not make retrieval smarter, but they determine rollback and survivability of the retained artifacts. For a database-first memory system, this is more central than it would be in a Git-first system.

## What to Watch

- Whether LocalBrain adds review or provenance checks for LLM wiki articles. That would decide whether wiki synthesis is just a convenience view or a trustworthy knowledge artifact.
- Whether derived indexes are automatically invalidated when Markdown capture files change outside the collectors. Without that, files, SQLite, and Chroma can diverge.
- Whether reading-history personalization expands from small ranking boosts to stronger routing or prompt policy. That would make usage traces a more consequential behavioral authority.
- Whether the agent skill gains retrieval/read-back operations, not only collection operations. That would turn LocalBrain from "agent feeds memory" toward "agent consults memory" in the same skill surface.
- Whether graph/topic mining receives quality metrics or confidence thresholds visible to users. Low-quality extracted entities can pollute context enrichment quietly.
- Whether the system supports local-only model defaults as a first-class profile. That would change the adoption and privacy story for a "local brain."

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: LocalBrain stores many artifacts, but only retrieval, RAG, recommendations, and conversation-history injection activate them.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: LocalBrain requires separating Markdown captures, SQLite graph rows, Chroma vectors, wiki articles, skill instructions, and trace rows by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - lightly applies: LocalBrain uses traces for personalization and session continuity, not for durable rule or skill learning.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: collected documents, wiki articles, conversation turns, and search results usually advise as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: retrieval policy, database schemas, vector indexes, CLI/API contracts, skill instructions, and ranking boosts shape future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: LocalBrain's main design contribution is routing selected slices of a large local store into bounded RAG contexts.
