---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Agentic Local Brain memory: document/index divergence, mined representations, durable wiki synthesis, conversational reuse and reading-history selection."
run-id: AAS-2026-10-12-agentic-local-brain-f00cbd577178-01
source-identity: "https://github.com/agent-creativity/agentic-local-brain"
reviewed-boundary: "41ea0cb104686eb0d39f32c94c2b84d37cdff0e7"
---

# Agentic Local Brain memory report

## Boundary and evidence

This report covers retained user knowledge and the application's later consumers at SRC-1 commit `41ea0cb104686eb0d39f32c94c2b84d37cdff0e7`, as fixed by [boundary](boundary.md). It includes Markdown documents, SQLite metadata and mined state, Chroma chunk vectors, wiki files and article metadata, conversation turns, reading events, result caches and archive recovery. Configuration and shipped instructions influence these paths but are not accumulated experience by themselves. External provider weights/state remain opaque; the separately declared generation, expansion, reranking and embedding components in runtime retain that limit.

The development-agent hooks and Trellis journals remain excluded under boundary. Collection instructions for an external agent remain included as an afforded admission path, not proof of host compliance. Remote fetching/parsing details, complete graph/topic scoring, installers, frontend internals and test quality were not exhaustively inspected; these limits prevent universal coverage, quality, isolation and synchronization claims. No store, trace or observed run was supplied and no target code was executed.

Direct reads added to the supplied runtime include SRC-1 `kb/query/reading_history.py`, `kb/processors/recommendation.py`, `kb/web/routes/recommendations.py`, the item-deletion handler in `kb/web/routes/items.py`, relevant schemas and deletion in `kb/storage/sqlite_storage.py`, history formatting/cleanup in `kb/query/conversation.py`, both context builders in `kb/query/context_builder.py`, enrichment/builder selection in `kb/query/retrieval_pipeline.py`, staleness/prompt selection in `kb/processors/wiki_compiler.py`, and document-vector/entity/mining parts cited below. These supply implementation evidence only. The following inventory distinguishes that inspection from the provisional runtime account. Each row retains its admission and later-consumer boundary.

| Entry point or memory operation | Source paths in SRC-1 | Coverage and admission control | Missing fact / prevented conclusion |
|---|---|---|---|
| CLI file admission and shared indexing | `kb/cli.py`, `kb/commands/collect.py`, `kb/commands/utils.py`, `kb/collectors/base.py` | Supplied [RT-RTE-file-admission](runtime.md#rt-rte-file-admission); [MEM-OBJ-knowledge](#mem-obj-knowledge), [MEM-OBJ-chunks](#mem-obj-chunks). Caller selects input; software admits extracted metadata/vectors without per-result approval. | Collector/parser variants not all directly traced; no uniform acquisition guarantee. |
| Webpage, paper, email, bookmark/import, note alternatives | `kb/commands/collect.py`, `skills/localbrain-collect/SKILL.md` | Dispatch/call-site search plus direct note-driver read; [MEM-RTE-note-admission](#mem-rte-note-admission), supplied [RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback). Host/caller supplies material; driver controls admission. | Remote provenance/authentication and every parser branch uninspected. Shipped examples are alternative API callers under boundary, not evidence of a CLI-equivalent persistence loop. |
| Batch/CLI/per-document mining | `kb/commands/mine.py`, `kb/processors/mining_runner.py`, `kb/processors/mining_worker.py`, `kb/web/routes/mining.py` | Supplied [RT-RTE-mining-run](runtime.md#rt-rte-mining-run); direct worker read; derived parts below. Caller chooses maintenance; software/model admission is not per-content approval. | Invocation of worker on each collection unestablished; stage histories are not a single consistent rebuild. |
| Entity and relation retention | `kb/processors/entity_extractor.py`, `kb/processors/doc_relation_builder.py`, `kb/storage/sqlite_storage.py` | Direct save/schema reads; [MEM-OBJ-entities](#mem-obj-entities), [MEM-OBJ-document-relations](#mem-obj-document-relations). Type/name/end-point checks reject malformed units, not false claims. | Full graph consumer algorithms uninspected; aggregate counters need not be reversible evidence counts. |
| Document embeddings and topics | `kb/processors/doc_embedding.py`, `kb/processors/doc_relation_builder.py`, `kb/processors/topic_clusterer.py` | Direct embedding writers/decoders; scoped topic source search/schema read; [MEM-OBJ-document-embeddings](#mem-obj-document-embeddings), [MEM-OBJ-topic-clusters](#mem-obj-topic-clusters). Algorithmic/model derivation is automatically retained. | Alternative vector encoding compatibility is not universal; complete clustering/label-quality checks uninspected. |
| Wiki compilation, categories, entity-card alternative and browsing | `kb/processors/wiki_compiler.py`, `kb/web/routes/wiki.py`, `kb/commands/wiki.py` | Supplied [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile); direct staleness/prompt read and entity-card call-site search; [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles). Model proposes; compiler writes. | Entity-card body and active caller not traced; cannot extend topic-article lineage/account to that alternative. |
| Enhanced chat, context selection, conversation reuse | `kb/query/retrieval_pipeline.py`, `kb/query/context_builder.py`, `kb/query/conversation.py`, `kb/web/routes/search.py` | Supplied [RT-RTE-chat-query](runtime.md#rt-rte-chat-query); direct budget/history reads; [MEM-OBJ-rag-conversations](#mem-obj-rag-conversations). Turns are automatically admitted on applicable successful paths. | No trace establishes exercised reuse, true answers, or a universal prompt budget. |
| Legacy RAG, direct keyword/semantic reads | `kb/query/rag.py`, `kb/query/keyword_search.py`, `kb/web/routes/search.py`, `kb/commands/search.py` | Supplied [RT-RTE-legacy-query](runtime.md#rt-rte-legacy-query); direct HTTP keyword/semantic read. FTS metadata, ripgrep files and vectors are different read surfaces. | They are not all conversation routes and tags are not demonstrated end-to-end isolation. |
| Item viewing, reading history, recommendations | `kb/web/routes/items.py`, `kb/query/reading_history.py`, `kb/processors/recommendation.py`, `kb/web/routes/recommendations.py` | Direct reads/search; [MEM-OBJ-reading-history](#mem-obj-reading-history), [MEM-RTE-history-selection](#mem-rte-history-selection). Automatic event write; no semantic approval. | History is not a human-authenticated preference statement; benefit and display activation unobserved. |
| Editing, withdrawal, tag merge/delete/export | `kb/web/routes/items.py`, `kb/storage/sqlite_storage.py`, `kb/commands/manage.py` | Supplied [RT-RTE-item-update](runtime.md#rt-rte-item-update); direct deletion read plus tag/export dispatch search; [MEM-RTE-item-withdrawal](#mem-rte-item-withdrawal). Caller supplies edit/deletion; software checks existence, not truth. | Tag/export bodies not fully traced; no coordinated purge/reindex guarantee. |
| Conversation deletion and cleanup | `kb/query/conversation.py`, `kb/web/routes/search.py` | Direct manager read and handler search; annotation on [RT-RTE-chat-query](runtime.md#rt-rte-chat-query). Explicit session/all-session endpoints, optional expiry API. | No scheduler/caller for expiry established by inspected paths; no default automatic expiry claim. |
| Cache, mining history, archive retention | `kb/query/retrieval_pipeline.py`, `kb/processors/mining_runner.py`, `kb/commands/backup.py`, `kb/scheduler/backup_scheduler.py` | Supplied [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-mining-run](runtime.md#rt-rte-mining-run), [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore). TTL/invalidation, mechanical history and archive writes. | Cache is process-local, mining history serves status rather than a demonstrated revision learner, restore still requires placement. No coherent snapshot/purge guarantee. |
| Configuration, static prompts, provider state | `kb/config.py`, `kb/config-template.yaml`, `kb/query/prompt_templates.py`, `kb/web/dependencies.py` | Supplied [RT-OBJ-config](runtime.md#rt-obj-config), [RT-OBJ-prompt-templates](runtime.md#rt-obj-prompt-templates) and model components. Caller edits settings; constructed components consume them. | Provider internals and actual resolved weights unavailable; static prompts alone are not read-back. |

## Core ideas

1. **Several retained representations can disagree.** Files contain collected text; SQLite holds metadata and associations; Chroma holds chunk text/vectors. Item metadata edits do not establish file/index updates, and withdrawal can leave files or vectors behind. The substrates have different later consumers, not one authoritative document store ([MEM-OBJ-knowledge](#mem-obj-knowledge), [MEM-OBJ-chunks](#mem-obj-chunks), [MEM-RTE-item-withdrawal](#mem-rte-item-withdrawal)).
2. **Derived material changes selection and presentation, not model weights.** Entities, document vectors, relations and topics select/enrich later knowledge. Wiki synthesis creates durable prose for human browsing. Numerical document-vector payloads are distinct from their title/reason displays. The configured model components' own parameter mutability remains as scoped in runtime ([MEM-OBJ-document-embeddings](#mem-obj-document-embeddings), [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles), [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider)).
3. **Conversation and access traces have different authority.** Prior user/assistant text enters future prompts. Reading events instead become score inputs and an ephemeral interest vector for recommendations. Recommendation explanations are display summaries, not retained criticisms or proof of causal relevance ([MEM-OBJ-rag-conversations](#mem-obj-rag-conversations), [MEM-RTE-history-selection](#mem-rte-history-selection)).
4. **Context limits are route-specific.** Hierarchical construction truncates/omits content; the flat alternative estimates tokens but does not enforce the supplied budget. History has a separate character limit and wiki has another source budget. None is a whole-request tokenizer guarantee ([MEM-CLM-budget-scope](#mem-clm-budget-scope)). Source trust is a prompt request rather than a verified property: runtime's citation guidance does not authenticate collected text or validate citations ([RT-CLM-context-answer](runtime.md#rt-clm-context-answer)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-knowledge
Label: Collected Markdown and SQLite knowledge metadata

Source-native identity: collected files and SQLite `knowledge`, `tags`, `knowledge_tags`. Storage substrate: local Markdown/YAML files and SQLite. Representational form: natural-language source text, summaries and user notes; symbolic IDs, paths, hashes, content types, timestamps and tag associations. The mixed container is split from chunk vectors below because write/withdrawal and consumers differ. Lineage: caller-selected content through collection/parser, optional model/built-in metadata extraction; authorship of a generic caller or remote source is not necessarily human. Consumers: file-based keyword search and mining read text; SQLite metadata/FTS, browsing and retrieval enrichment read metadata. Authority is evidence/context for human/model interpretation and fixed filtering/lookup for symbolic fields, not an independent truth oracle.

Closest supplied records are [RT-RTE-file-admission](runtime.md#rt-rte-file-admission) and [RT-RTE-item-update](runtime.md#rt-rte-item-update): these are write routes, not duplicate objects. Admission/recovery evidence and the minimum file-write passage are retained there. SRC-1 `kb/commands/collect.py`, `kb/collectors/base.py`, `kb/storage/sqlite_storage.py`, `kb/web/routes/items.py`. Subsequent SQLite-only edits can change metadata without changing the raw file or vectors. The exact contribution of user_notes to each downstream answer route is uninspected; a stored editable field alone is not demonstrated answer authority.

#### MEM-OBJ-chunks
Label: Search chunks and Chroma numerical representations

Source-native identity: SQLite `chunks` and Chroma indexed documents/embeddings keyed by generated chunk IDs. Storage substrate: SQLite plus persistent Chroma. Representational form: natural-language chunk text; symbolic item/chunk IDs, index and embedding references; distributed-parametric dense embeddings consumed by similarity search. Lineage: collected content through chunking and configured embedding provider; vectors are derived representations, not model parameters or model-version pins. Later semantic retrieval selects text using vector proximity; selected text then has model-input authority, subject to fusion and truncation. Storage/indexing passage support comes from [RT-RTE-file-admission](runtime.md#rt-rte-file-admission); direct withdrawal evidence is [MEM-RTE-item-withdrawal](#mem-rte-item-withdrawal). SRC-1 `kb/commands/utils.py`, `kb/storage/chroma_storage.py`, `kb/storage/sqlite_storage.py`. No supplied object counterpart; route/component overlap is with [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) and [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), not identity. Cross-substrate rollback and automatic reembedding after every edit are not established.

#### MEM-OBJ-entities
Label: Extracted entities, mentions and entity relations

Source-native identity: SQLite `entities`, `entity_mentions`, `entity_relations`, `entity_relation_sources`. Storage substrate: SQLite. Representational form: natural-language names/descriptions/context snippets plus symbolic entity IDs, type vocabularies, directed relation types, source links and counters. These are derived claims and associations rather than untouched source text. Lineage: title/content through configured model, parser/normalizer and saver. Consumer: graph retrieval/enrichment and wiki source/entity construction; type and link structures have fixed selection authority, while descriptions enter interpretation. Material output of [RT-RTE-mining-run](runtime.md#rt-rte-mining-run), not that route's identity. SRC-1 `kb/processors/entity_extractor.py`, `kb/storage/sqlite_storage.py`.

> if not name or entity_type not in self.ENTITY_TYPES:
>     continue
> --- `kb/processors/entity_extractor.py`

> INSERT OR IGNORE INTO entity_relation_sources (relation_id, knowledge_id, context)
> VALUES (?, ?, ?)
> --- `kb/processors/entity_extractor.py`

The retained relation context is truncated to 200 characters by save; description also supplies mention context. This preserves some source-associated explanation, not the provider's reasoning or a statement-level verification history. Upsert increments relation weights and entity mention counts; it does not update an existing entity description in the inspected conflict clause. Repeated extraction can increase counters without adding a distinct source association. Source deletion cascades source/mention links but the entity/relation rows have their own endpoint foreign keys; removal of all supporting documents is not demonstrated automatic retraction of the surviving claim or counter.

#### MEM-OBJ-document-embeddings
Label: Document embedding cache with alternative encodings

Source-native identity: `document_embeddings.embedding` generated by `DocEmbeddingService` or `DocRelationBuilder.generate_doc_embedding`. Storage substrate: SQLite declared BLOB column; actual payload can be JSON text or packed float bytes. Representational form: distributed-parametric dense document vectors; symbolic knowledge ID and timestamp are access metadata. Lineage: title plus bounded summary/content through configured embedding service. Models' exact versions are not pinned by these rows. Consumers: relation builder, topic clustering and recommendation; numerical similarities affect candidate selection, not explicit reasons. Different from chunk embeddings and from [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider)'s model; closest route is [RT-RTE-mining-run](runtime.md#rt-rte-mining-run). SRC-1 `kb/processors/doc_embedding.py`, `kb/processors/doc_relation_builder.py`, `kb/processors/topic_clusterer.py`, `kb/processors/recommendation.py`.

> embedding_json = json.dumps(embedding)
> --- `kb/processors/doc_embedding.py`

> def _serialize_embedding(embedding: List[float]) -> bytes:
>     """Serialize embedding to bytes for SQLite BLOB storage."""
>     return struct.pack(f"{len(embedding)}f", *embedding)
> --- `kb/processors/doc_relation_builder.py`

Relation decoding explicitly accepts JSON or binary. Recommendation's inspected reader instead uses `json.loads` and skips JSONDecodeError/TypeError; it does not implement the packed-float fallback. Batch DocEmbeddingService derives from title/summary and skips IDs already embedded in incremental mode; the per-document worker supplies content[:500]. An exposed alternate builder writes packed vectors from title plus summary[:500]. These writers need not carry identical input provenance or compatible downstream decoding. Arbitrary packed bytes may also raise decoding errors outside recommendation's named catch. This is a source-level interoperability limit, not an observed failure or a claim that binary rows occur in every deployed store.

#### MEM-OBJ-document-relations
Label: Cross-document similarity and shared-entity relations

Source-native identity: SQLite `document_relations`, built by `DocRelationBuilder`. Storage substrate: SQLite. Representational form: symbolic source/target IDs and relation-type labels with numerical similarity scores and serialized shared entities. Lineage: cached document vectors through cosine thresholding or existing entity mentions through shared-entity matching. Consumers: relation/graph browsing and retrieval-adjacent graph operations described in supplied mining account; complete use of each relation type by the enhanced answer selector is uninspected. No separate formulated rationale for similarity is established by a score; shared entities expose a narrower inspectable association. Distinct output object from [RT-RTE-mining-run](runtime.md#rt-rte-mining-run). SRC-1 `kb/processors/doc_relation_builder.py`, `kb/storage/sqlite_storage.py`.

> INSERT OR REPLACE INTO document_relations
> (source_knowledge_id, target_knowledge_id, relation_type, score, shared_entities)
> --- `kb/processors/doc_relation_builder.py`

The schema cascades relations when a knowledge endpoint is deleted. That differs from free-standing extracted entity relation rows. Full relation rebuilding clears and recomputes state; quality-based successor comparison is not established by a threshold or a rebuild flag.

#### MEM-OBJ-topic-clusters
Label: Topic assignments, labels and centroids

Source-native identity: SQLite `topic_clusters` and `knowledge_topics`. Storage substrate: SQLite with serialized numerical centroid payload. Representational form: distributed-parametric centroids; symbolic cluster/document membership and confidence; natural-language labels/descriptions. Lineage: document embeddings through clustering/assignment and label generation, rather than interaction transcripts. Consumers: topic browsing, retrieval enrichment and wiki organization, plus recommendation topic bonus. Closest supplied route [RT-RTE-mining-run](runtime.md#rt-rte-mining-run) describes production but is not this object. SRC-1 `kb/processors/topic_clusterer.py`, `kb/storage/sqlite_storage.py`, `kb/processors/recommendation.py`.

> CREATE TABLE IF NOT EXISTS knowledge_topics (
>     knowledge_id TEXT NOT NULL,
>     cluster_id INTEGER NOT NULL,
>     confidence REAL DEFAULT 1.0,
>     PRIMARY KEY (knowledge_id, cluster_id),
>     FOREIGN KEY (knowledge_id) REFERENCES knowledge(id) ON DELETE CASCADE,
>     FOREIGN KEY (cluster_id) REFERENCES topic_clusters(id) ON DELETE CASCADE
> )
> --- `kb/storage/sqlite_storage.py`

Assignment membership has deletion links; the topic label/centroid need not be recomputed by deleting one member. Complete clustering, label-provider and centroid revision semantics were not directly read; schema/search establish these parts and supplied runtime establishes the production/consumer loop, not a guarantee that all labels track every source change.

#### MEM-OBJ-wiki-articles
Label: Durable wiki prose and source/category metadata

Source-native identity: generated Markdown plus SQLite `wiki_articles` and `wiki_categories`. Storage substrate: files and SQLite. Representational form: natural-language article sections, titles and model-derived category descriptions; symbolic article/category IDs, path, version, compiled time, document/entity references. Lineage: selected retained documents/entities through bounded prompt, model generation, parsing and rendering. Authority: article prose is a durable human-readable synthesis on later wiki GET; source/category metadata selects compilation and resolves display links. It is not established as an enhanced-RAG answer corpus merely because it persists. Closest supplied [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile) owns the route and write passage, not this object. SRC-1 `kb/processors/wiki_compiler.py`, `kb/web/routes/wiki.py`, `kb/storage/sqlite_storage.py`.

> elif current_doc_ids != compiled_doc_ids:
>     # Doc IDs have changed (new docs added or removed)
>     categories_needing_compilation.append(category)
> --- `kb/processors/wiki_compiler.py`

This category selector can detect removals as well as additions, but equal ID sets do not detect changed source text/summary. Force is an alternate trigger. Source IDs are assembled from filtered documents, while prompt construction can stop or truncate before delivering all of them; metadata is not evidence of full model consumption. It retains source associations and generated prose, not an inspectable critique/revision rationale. The schema stores article source IDs as text, not a knowledge foreign-key cascade. Entity-card compilation is an exposed alternative with empty source-document lists in searched call sites; its body, active caller and detailed lineage remain uninspected, preventing uniform source-link conclusions.

#### MEM-OBJ-rag-conversations
Label: Persistent RAG conversation turns and source metadata

Source-native identity: `ConversationManager` sessions/turns, including `rag_conversations`, in a separate SQLite database as supplied runtime traces. Storage substrate: conversation SQLite; representational form: natural-language user question and assistant answer, symbolic session/role/order/time and serialized source dictionaries. Lineage: interactions and generated answers, not raw model reasoning. Later query expansion and answer generation receive selected recent turn text; source dictionaries are not included by the inspected history formatter. Closest [RT-RTE-chat-query](runtime.md#rt-rte-chat-query) supplies the write/reuse route and save-failure passage. SRC-1 `kb/query/conversation.py`, `kb/query/retrieval_pipeline.py`.

> turns = self.get_recent_turns(session_id, limit=max_turns)
> --- `kb/query/conversation.py`

> turn_text = f"{role_label}: {turn.content}\n\n"
> --- `kb/query/conversation.py`

The formatter limits history to 4000 characters with a partially truncated last turn. It is selection/truncation, not an automatically authored summary or compressed replacement checkpoint. Prior answers can influence a later model even though factual verification and retained reasoning are unestablished. Session/all-session deletion is separate from knowledge-item deletion; source dictionaries or turn text are not shown purged by removing a knowledge row.

#### MEM-OBJ-reading-history
Label: Reading, search and RAG interaction events

Source-native identity: SQLite `reading_history` through `ReadingHistory` and the exposed `RecommendationEngine.record_action`. Storage substrate: main SQLite. Representational form: symbolic action/time/knowledge-ID fields and natural-language query text. Lineage: automatic HTTP view/search/RAG handlers and possible callers of record_action; original query/interaction content is not necessarily a human-authenticated statement. This is access metadata, not source-document content or explicit criticism. Later recommendation and retrieval-personalization use document IDs/times; history endpoints display queries/statistics. Distinct material part of the broad chat state, spanning more than [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), since item views and direct search also produce it. SRC-1 `kb/query/reading_history.py`, `kb/processors/recommendation.py`, `kb/web/routes/items.py`, `kb/web/routes/search.py`.

> "INSERT INTO reading_history (knowledge_id, query, action_type) "
> "VALUES (?, ?, ?)",
> --- `kb/query/reading_history.py`

The schema uses ON DELETE SET NULL for the knowledge link. Queries/action/time can remain after item withdrawal; selectors requiring nonnull IDs stop using those orphaned events. An event row is not itself a durable generated preference theory or recommendation explanation.

### Routes

#### MEM-RTE-note-admission
Label: Direct text-note admission

Endpoints/progression: CLI `collect note add` → NoteCollector → Markdown → optional extraction/frontmatter → SQLite metadata/tags → shared index helper. Owner: application under caller OS principal. Context/effects: text, optional title/tags/summary, extraction flag, duplicate flag and generated ID; saved files, metadata and vectors. Distinct alternative to [RT-RTE-file-admission](runtime.md#rt-rte-file-admission): source is manual_input and index helper receives the direct text rather than a reloaded saved file. SRC-1 `kb/commands/collect.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed note result including path and extracted metadata, duplicate/failure alternative.
- Later read-back: Note text, metadata and chunks can reach later file, metadata and semantic consumers.
- Delegated visibility: Configured extraction/embedding services receive note-derived text; no agent delegation is implemented by this driver.
- Selection predicate: Caller supplies direct text and optional fields; user tags/summary precede extraction; indexing uses original text.
- Invalidation or expiry: No coordinated file/metadata/vector rollback or automatic retention expiry established in this driver.
- Activation or effect: Automatic writes/indexing wired; actual later use unobserved.
- Evidence limits: Driver does not establish caller authorship, semantic validity, or all collector equivalence.

Caller initiates and can disable extraction or provide values; software admits missing generated fields without a per-content approval queue. Collection success gates later metadata/index writes; false collector result follows duplicate/failure branch. Recovery is separate edit/delete/rerun, not transactional rollback. Extraction guidance and persisted results are the shared metadata mechanism traced in runtime, not revised method instructions. No answer oracle or bounded improvement experiment is established.

> source="manual_input",
> --- `kb/commands/collect.py:843-855`

#### MEM-RTE-history-selection
Label: Reading-history-driven recommendation and retrieval personalization

Endpoints/progression: item/search/RAG handlers record events → main SQLite → later GET /api/recommendations builds RecommendationEngine → recent event IDs/times and stored document vectors → decayed average → similarity/topic bonus → top results with titles/reasons → HTTP/display consumer. Independent later enhanced query enrichment loads recent views and conditionally boosts already selected chunks. Owner: application; caller requests recommendation or query, software owns event admission and derived selection. Context/effects: persisted events/vectors/topics and transient profile/scores; no persistent user-profile write is established in recommend. Distinct route from [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), with an overlapping enrichment subpath. SRC-1 `kb/query/reading_history.py`, `kb/processors/recommendation.py`, `kb/web/routes/recommendations.py`, `kb/query/retrieval_pipeline.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recommendation list with knowledge ID/title/reason/score, or latest-document fallback; enrichment returns potentially reordered chunks to context construction.
- Later read-back: Prior event IDs/times select stored document vectors and topic bonuses in a later recommendation call; recent views supply later query score inputs.
- Delegated visibility: Recommendation arithmetic and reasons are local; later answer provider receives selected context, not the entire event database.
- Selection predicate: Recent nonnull knowledge IDs, configured history count/decay/top limit and candidate vectors; excludes only IDs in the selected recent window, not all documents ever read. Enrichment loads 20 recent views and compares chunk.source to viewed knowledge IDs.
- Invalidation or expiry: Recommendation profile recomputed per call; event expiry unestablished; enhanced result-cache hits can bypass fresh personalization.
- Activation or effect: Persisted traces are wired to later arithmetic and selection; actual ranking changes and better recommendations unobserved.
- Evidence limits: Human intent, source-ID matching on every search branch and vector-decoder compatibility are not guaranteed; query-only events do not supply nonnull document IDs to this recommendation selector.

Automatic event write is software admission, not explicit preference approval. No model authors the arithmetic profile or reason strings. Caller can request/decline the displayed recommendations and disable reading-history enrichment; no expected-answer oracle or capacity-improvement comparison is established. Raw events remain durable; their numerical profile and readable reasons are regenerated, not retained criticisms. The trace-to-later-selection chain is a behavioral-memory path without evidence of training model parameters or improved capacity.

> user_profile = weighted_sum / weight_total
> --- `kb/processors/recommendation.py`

> if chunk.source in recently_viewed_ids:
>     # Boost the chunk's final_score by +0.1 (cap at 1.0)
>     chunk.final_score = min(1.0, chunk.final_score + 0.1)
> --- `kb/query/retrieval_pipeline.py`

Recommendation's recent-event query lacks an action-type filter; the separate enrichment selector explicitly requests views. Reason strings use topic labels or recent titles rather than exposing vector dimensions or validating why a document is relevant.

#### MEM-RTE-item-withdrawal
Label: Metadata-led item withdrawal with best-effort vector/file deletion

Endpoints/progression: DELETE /api/items/{item_id} → existence check → capture chunk IDs/file path → SQLite deletion → attempted Chroma deletion → optional file removal → success. Owner: HTTP caller requests withdrawal; application enforces existence and chooses sequence. Context/effects: exact knowledge ID, delete_file flag and captured chunk IDs; different deletion effects on linked records, vectors, files and surviving derived state. Distinct from [RT-RTE-item-update](runtime.md#rt-rte-item-update), which edits metadata rather than withdrawing it. SRC-1 `kb/web/routes/items.py`, `kb/storage/sqlite_storage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success after SQLite deletion even if Chroma/file cleanup fails; missing item or SQLite failure yields HTTP error.
- Later read-back: SQLite consumers lose the knowledge row and schema-linked associations; retained file-based search, stale cache, prior conversation text or wiki prose are not demonstrated purged.
- Delegated visibility: inapplicable — no model or delegated worker receives this operation.
- Selection predicate: Exact item ID, captured chunk IDs, optional delete_file=true; default leaves document file.
- Invalidation or expiry: No pipeline-cache invalidation or wiki regeneration appears in this handler; vector/file deletion is best effort, not coordinated rollback.
- Activation or effect: Software withdrawal is wired at metadata consumer; universal downstream retraction unestablished.
- Evidence limits: Source-only trace; deletion message is not proof of complete erasure across retained representations or backups.

Caller supplies/vetoes the request, with human identity unresolved. Software rejects nonexistent items and false SQLite result; it does not evaluate the withdrawn claim. No answer oracle, model proposal or semantic replacement selection applies. Recovery is separate recollection/backup adoption, not an implemented rollback of this sequence. What persists can include derived article prose, source IDs in article metadata, prior turns, orphaned history queries, caches, default-retained files and archives; later availability depends on each independent consumer, not this operation's label.

> if chunk_ids:
>     try:
>         chroma = get_chroma_storage()
>         chroma.delete(ids=chunk_ids)
>     except Exception as e:
>         # Log but don't fail - SQLite deletion was successful
>         pass
> --- `kb/web/routes/items.py`

> if delete_file and file_path and os.path.exists(file_path):
> --- `kb/web/routes/items.py`

### Claims

#### MEM-CLM-budget-scope
Label: Context budget is not uniformly enforced by alternative builders

Claimed operation: hierarchical context building applies progressive truncation, while SimpleContextBuilder merely estimates a budget for flat concatenation. This narrows the supplied runtime's general budgeted-context description in [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), not its normal hierarchical behavior. SRC-1 `kb/query/context_builder.py`, `kb/query/retrieval_pipeline.py`.

> # Add chunks in order
> for i, chunk in enumerate(chunks):
>     source_info = f"[Source {i + 1}] - {chunk.source}"
>     context_parts.append(f"{source_info}\n{chunk.content}\n")
> --- `kb/query/context_builder.py`

> if context_format == "flat":
>     builder = SimpleContextBuilder()
> --- `kb/query/retrieval_pipeline.py`

Hierarchical source selection can truncate a chunk into a new RankedChunk and omit later chunks; flat builder returns all chunks. Approximate word/character estimates are not provider tokenizer enforcement. History, system/task prompts, question and output generation have separate budgets/settings. No whole-message hard cap is established here.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-context
Label: Retained content and prior turns enter later interpretation

Consumer: configured expansion/answer models and human wiki reader. Channel: selected chunk/entity/topic text and formatted prior turn text in model messages; stored article Markdown via wiki GET for human browsing. Force: interpretation of natural-language content, not verified obedience or truth; symbolic selectors separately constrain what is delivered. Horizon: subsequent queries/session turns/article requests after successful writes and reads. SRC-1 `kb/query/retrieval_pipeline.py`, `kb/query/conversation.py`, `kb/web/routes/wiki.py`; write/delivery passages in [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile), [MEM-OBJ-rag-conversations](#mem-obj-rag-conversations). Distinct from [RT-BAP-template-guidance](runtime.md#rt-bap-template-guidance), whose referent is static task guidance rather than accumulated content. Delivery is wired, activation and benefit unobserved.

#### MEM-BAP-event-selection
Label: Retained interaction metadata controls later candidate scores

Consumer: RecommendationEngine arithmetic and RetrievalPipeline enrichment. Channel: SQLite event IDs/timestamps plus stored vectors/topic memberships into score computation; recent-view IDs into a conditional chunk-score boost. Force: fixed software rules changing candidate order when their predicates hold, not authoritative factual content. Horizon: subsequent noncached applicable recommendation/query calls. SRC-1 `kb/processors/recommendation.py`, `kb/query/retrieval_pipeline.py`; minimum passages and qualified matching/decoding boundaries in [MEM-RTE-history-selection](#mem-rte-history-selection). No supplied behavioral-authority counterpart after comparison with runtime's configuration/template paths. The persistent result is the event trace; derived profile is transient, and reason strings are display summaries.

## Annotations

#### On [RT-RTE-file-admission](runtime.md#rt-rte-file-admission)

Retained parts separate by consumer: raw collected Markdown versus extracted summary/tags, chunks and numerical vectors. Caller-selected input and extraction defaults are admission initiation, not human approval of missing generated values. Sequential file/frontmatter/SQLite/Chroma writes admit representations with different recovery boundaries. Read-back is later request-driven keyword/semantic/mining selection; command output does not itself deliver the entire store to the external host. SRC-1 `kb/commands/collect.py`, `kb/commands/utils.py`; supplied route's verbatim passage supports best-effort indexing. Source-specific initial provenance remains uninspected outside the traced file/note/fallback paths.

#### On [RT-RTE-chat-query](runtime.md#rt-rte-chat-query)

Conversation retention is automatic interaction logging, with generated answers among the raw turn contents. The later formatter consumes content/role only, not saved source dictionaries or full model reasons ([MEM-OBJ-rag-conversations](#mem-obj-rag-conversations)). A cache hit instead reads a process-local prior result, bypassing fresh history/selection; its key omits options as runtime states. Hierarchical/flat construction must be distinguished ([MEM-CLM-budget-scope](#mem-clm-budget-scope)). Reading traces condition scores only when retrieved chunk.source matches a viewed ID ([MEM-RTE-history-selection](#mem-rte-history-selection)). SRC-1 `kb/query/conversation.py`, `kb/query/retrieval_pipeline.py`, `kb/query/context_builder.py`.

Conversation cleanup APIs include exact-session deletion, all-session deletion/vacuum and inactive-session expiry. The shipped HTTP search module exposes exact/all deletion; source search did not establish an expiry invocation in the inspected CLI/web roots. Expiry method presence is a maintenance capability, not a timer guarantee.

> DELETE FROM rag_conversations
> WHERE updated_at < datetime('now', '-{} minutes')
> --- `kb/query/conversation.py`

#### On [RT-RTE-mining-run](runtime.md#rt-rte-mining-run)

Document embeddings, entity claims and relations have different provenance and rollback. Entity admission filters types and preserves short source-associated contexts; document vectors may be JSON or packed numerical bytes; relation selection and topics are further derived parts ([MEM-OBJ-entities](#mem-obj-entities), [MEM-OBJ-document-embeddings](#mem-obj-document-embeddings), [MEM-OBJ-document-relations](#mem-obj-document-relations), [MEM-OBJ-topic-clusters](#mem-obj-topic-clusters)). The direct worker supplies content[:3000] for entities and content[:500] for its document embedding, distinct from batch summary-based generation. SRC-1 `kb/processors/mining_worker.py`, `kb/processors/doc_embedding.py`.

> summary = content[:500] if content else ""
> emb = emb_svc.generate_for_document(knowledge_id, title or "", summary)
> --- `kb/processors/mining_worker.py`

JSONL mining history is retained status evidence for the supplied history endpoint, not a demonstrated automatic trace-to-method revision. Worker cache invalidation is best effort and does not cover all independent writers/processes. No universal all-documents worker invocation follows from its name/docstring.

#### On [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile)

Raw document text is transformed into durable article prose; associated source IDs do not prove every input reached generation. Category ID-set change can trigger compilation, including removals, but same-ID content edits alone do not satisfy that predicate. Article metadata does not implement source-document foreign-key deletion. The retained article/source associations supply human browsing and future compilation selection, not an established closed critique loop or universal answer-model reuse. SRC-1 `kb/processors/wiki_compiler.py`, `kb/storage/sqlite_storage.py`; [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles).

#### On [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore)

Archive bytes mechanically preserve selected filesystem material. This is retention/recovery, not semantic validation, source trust elevation or a coherent live-store snapshot guarantee. Later adoption requires manual placement/configuration; extraction alone is not live behavioral authority. Backups can preserve content withdrawn from current metadata and are not shown purged by item deletion. SRC-1 `kb/commands/backup.py`, `kb/web/routes/items.py`; extraction passage and target limits remain in the supplied route.

## Write side

Acquisition enters by caller-selected file/remote source, manual note text, or an external host's fetched fallback file. Source identity and hashes aid addressing/duplicates but do not authenticate content truth. Caller-provided missing-field overrides and extraction-disable flags give content control distinct from starting collection. Model/built-in transformations author tags/summaries; Python admits them and numerical indices without per-result approval ([RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [MEM-RTE-note-admission](#mem-rte-note-admission), [RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback)). Remote-specific fetching/parsing remains unresolved rather than equivalent by assumption.

Mining produces claims/links, document vectors, relations, topics and articles under software-controlled maintenance. Type/name checks and parseability reject some outputs; they are not factual evaluation. Full-mode confirmation is a workflow acknowledgement on one web route, not article/entity approval or an expected-answer oracle. Entity contexts retain a short explanation linked to source IDs; vectors retain no readable rationale; relations expose scores/shared-entity metadata; article prose/source links do not retain the model's derivation or a systematic criticism record. Full rebuild/recompile changes derived products under existing guidance, not demonstrated revisions of the method ([RT-RTE-mining-run](runtime.md#rt-rte-mining-run), [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile), object records above).

Conversation writes keep questions and generated answers on applicable chat paths. Later history truncates rather than summarizes them. No replacement/summary checkpoint was established by the inspected formatter. Reading events automatically retain raw access traces; later recommendation computes a numerical profile without storing it, and enrichment changes scores without writing a revised instruction. Thus raw-to-derived-to-later-consumer is events → transient profile/score selection → later display/model context, not durable profile training. The event result itself persists across requests; actual improved capacity is not established ([MEM-RTE-history-selection](#mem-rte-history-selection)).

Direct metadata editing admits supplied fields and adds tags without demonstrated file/reembedding/cache updates. Item withdrawal has separate SQLite, Chroma and optional file effects; derived prose, transcripts and archives can survive. Conversation deletion is separately available. Tag merge/delete, exports and storage reset are present API/CLI maintenance surfaces in the scoped search, but their complete synchronization effects remain uninspected. Backup adoption requires a distinct manual decision. These are correction/recovery affordances, not a semantic rejection system ([RT-RTE-item-update](runtime.md#rt-rte-item-update), [MEM-RTE-item-withdrawal](#mem-rte-item-withdrawal), [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore)).

## Read-back

- **Requested document retrieval:** current query/tags/top-k select metadata/files/vectors; semantic and keyword branches select different retained representations. Enhanced expansion/fusion/reranking further selects document-keyed candidates and delivered context. Graph/topic enrichment adds derived descriptions/links. Later model input is selected, not the complete corpus ([RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-legacy-query](runtime.md#rt-rte-legacy-query)). Direct HTTP FTS searches SQLite metadata, while runtime's keyword subprocess searches files (SRC-1 `kb/web/routes/search.py`, `kb/query/keyword_search.py`).
- **Requested conversational reuse:** session ID selects recent turns; role/content text is formatted with its separate 4000-character limit and supplied to expansion/answer generation. Saved citations/source metadata are not themselves history prompt evidence. Cache hits and empty retrieval are counterpaths to universal turn saving/reuse ([MEM-OBJ-rag-conversations](#mem-obj-rag-conversations), [RT-RTE-chat-query](runtime.md#rt-rte-chat-query)).
- **Requested recommendation with automatic contextual enrichment:** requesting recommendations independently selects recent event IDs/times, vectors and topics; output reasons and title/score displays reach the caller. Enhanced query enrichment supplies recent-view boosts without an explicit request for those particular events, but occurs inside the requested query and uses its enable flag. No independent unsolicited push scheduler was established; neither route is made a push merely because its internal selector is automatic ([MEM-RTE-history-selection](#mem-rte-history-selection)).
- **Requested wiki browsing and maintenance:** article ID selects stored file and associated metadata; compilation selects category/topic sources and previously compiled ID sets. Articles are a human-readable derived memory; an identifier-based GET is addressing, not evidence of semantic targeted search. Compilation can omit source text while retaining its source ID ([RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile), [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles)).
- **Recovery/status reads:** mining history reaches progress/history display; backups reach listing/selection and only later manual placement can restore live state. A Chroma/SQLite get API alone is not another agent consumer. Provider-side memories and library internals remain outside acquired evidence ([RT-RTE-mining-run](runtime.md#rt-rte-mining-run), [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore)).

## Integration issues

1. **Correction to a broad supplied budget claim:** [MEM-CLM-budget-scope](#mem-clm-budget-scope) qualifies [RT-RTE-chat-query](runtime.md#rt-rte-chat-query)'s budgeted-context account. Direct flat-builder/pipeline source shows an allowed alternative estimates but does not truncate. Preserve normal hierarchical truncation; do not infer a universal hard prompt bound.
2. **Additional vector compatibility limit:** [MEM-OBJ-document-embeddings](#mem-obj-document-embeddings) adds an exposed binary writer to [RT-RTE-mining-run](runtime.md#rt-rte-mining-run)'s account. Relation builder accepts both encodings while recommendation/topic readers use JSON in inspected reads/search. Whether the binary writer is invoked by an active installation is unresolved; universal compatibility and uniform lineage are prevented, not all document embedding use.
3. **Withdrawal is not universal rejection:** [MEM-RTE-item-withdrawal](#mem-rte-item-withdrawal), [MEM-OBJ-entities](#mem-obj-entities), [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles) add the retained-result consequences of direct deletion. Supporting documents can disappear while claims/prose/transcripts/archive content remain. Reconciliation should not treat successful item deletion as claim retraction from every consumer.
4. **Wiki update scope:** the ID-set selector in [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles) refines [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile)'s unresolved invalidation scope. It supports category recompilation on additions/removals, not equal-ID content changes. Entity-card generation body/caller remains uninspected and should not inherit topic source-document lineage.
5. **Personalization remains conditional:** [MEM-RTE-history-selection](#mem-rte-history-selection) overlaps the enrichment subpath of [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), but also covers a separate recommendation endpoint. Matching uses chunk.source versus knowledge IDs; benefit or successful matching across every retrieval branch is unresolved. Recommendation excludes recent-window IDs rather than all ever-read documents, narrowing its native "unread" label.
6. **Distinct identity comparison:** no new declaration is a duplicate of a supplied object/component. Knowledge/chunks/mined/wiki/turn/event objects are retained outputs/state, not their supplied producer routes or remote provider models. New note and withdrawal routes are distinct entry/control paths; history selection spans a separate endpoint plus the named chat subpath. [MEM-BAP-retained-context](#mem-bap-retained-context) concerns accumulated content rather than [RT-BAP-template-guidance](runtime.md#rt-bap-template-guidance)'s shipped guidance. These overlaps require connection, not silently replacing supplied records.
7. **Remaining included uncertainty:** complete remote parsers, tag/export synchronization, entity-card body/caller, topic/relation consumer scoring, every exposed storage API's active caller, and automatic conversation expiry wiring are not fully traced. The coverage table identifies their limits. None authorizes a universal store, retention, quality or runtime-use claim. No unavailable input or boundary expansion was needed.

## Limitations and checks

The frozen checkout HEAD was rechecked against the full boundary revision before source inspection. Method identity is the supplied job, member type, worker rules and record contract, read in full; no prior characterization or other attempt was read. One exploratory search used two nonexistent guessed paths and returned exit 2; directory inspection corrected the paths to `kb/processors/doc_relation_builder.py` and conversation handlers within `kb/web/routes/search.py` before claims were made. No source change or target execution was performed.

Positive witnesses establish these mechanisms, not complete enumeration. Provider weights/version resolution, actual store contents, restart durability, decoding failures in deployed data, answer fidelity, exercised personalization and improvement remain unobserved. Source-registered implementation supports wiring; generated material's labels, scores, citations and presence do not establish truth or learning benefit. Opaque model reasoning does not establish absence of formulated criticism; no blanket theory-builder or self-improvement conclusion is drawn.

Deterministic validation: the invocation's validate-output command passed the member content check. Its complete result states that invocation residue was not checked and that the pass is not job acceptance or claim support.
