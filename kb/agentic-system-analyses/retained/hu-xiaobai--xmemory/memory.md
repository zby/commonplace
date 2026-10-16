---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "xMemory memory report: conversation-derived episodes and statements, mutable theme summaries, hierarchy selection and incomplete withdrawal."
run-id: AAS-2026-10-15-xmemory-b9a2b9f58eda-01
source-identity: "https://github.com/hu-xiaobai/xMemory"
reviewed-boundary: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
---

# xMemory memory report

## Boundary and evidence

The memory boundary includes construction, automatic extraction, hierarchy maintenance, alternate library search operations, the shipped reader and offline evaluation. The facade alone is not the system: construction explicitly invokes theme/graph updates, and the reader independently reloads files. The scope and exclusions remain those of [boundary](boundary.md#boundary-and-evidence). External model weights, embedding-service internals and release-hosted memories remain outside SRC-1. No run artifacts or intervention results were supplied. All new findings below are source implementation or prompt/design evidence, not observed operation.

I directly inspected the models, facade, repository alternatives, semantic storage, episode deletion, prediction-correction and per-episode extraction, semantic save/deduplication, theme persistence and split/merge paths, semantic-kNN updates, graph construction, adaptive reload/selection/hydration/rendering, and alternate original-message search implementations. I also searched the frozen CLI, hook/tool registration and cleanup surfaces. The runtime member supplies segmentation, episode generation/fallback, task completion, baseline/lightweight search and scoring findings where specifically cited. No target code, model or test was executed.

### Coverage inventory

Every row concerns SRC-1. A path is an inspection anchor, not a second source identity. Direct inspection is marked D; supplied runtime findings are marked R. Uninspected internals are not access failures.

| Entry or operation | Paths and evidence | Coverage and limits |
|---|---|---|
| Message admission, segmentation, flush and episode generation | D: `src/api/facade.py`, `src/models/episode.py`, save sequence in `src/core/memory_system.py`; R: detector/generator through [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) | [MEM-OBJ-original-messages](#mem-obj-original-messages), [MEM-OBJ-episode-content](#mem-obj-episode-content). Full original segments survive summarization; smart segmentation is not a hard token cap. |
| Existing-knowledge prediction and comparison, including cold start | D: `src/generation/prediction_correction_engine.py`, `src/core/memory_system.py` | [MEM-OBJ-semantic-content](#mem-obj-semantic-content), annotation on [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission). Cold start reads episode content; comparison reads originals; prior-statement retrieval has vector, sampled and error-fallback alternatives. |
| Alternative per-episode and batch extraction | D: dispatch and generation in `src/generation/semantic_generator.py` | Same semantic annotation. Single-episode input uses originals, falling back to content; multi-episode input uses formatted episodes. Public generator capability does not establish an additional deployed consumer. |
| Persistence, rejection and backend choice | D: `src/storage/semantic_storage.py`, `src/infrastructure/repositories.py`, `src/services/providers.py`, deduplication in `src/core/memory_system.py`; R: episode writes | [MEM-OBJ-memory-metadata](#mem-obj-memory-metadata), [MEM-OBJ-retrieval-vectors](#mem-obj-retrieval-vectors). Filesystem and in-memory repositories have different horizons. Injected repositories are opaque alternatives; consistency and migration across arbitrary injected implementations are unestablished. |
| Theme attachment, summary refresh, split, merge and micro-theme coalescence | D: `src/core/memory_hierarchy.py`, orchestration in `src/core/memory_system.py` | [MEM-OBJ-theme-summary](#mem-obj-theme-summary), [MEM-OBJ-theme-topology](#mem-obj-theme-topology); hierarchy annotation. Coalescence invocation/thresholds inspected; every internal objective term and numerical corner case not audited. Complete clustering correctness is not established. |
| Semantic-kNN and exported graph | D: `src/core/memory_system.py`, `src/core/memory_hierarchy.py`; searched reader in `evaluation/gexf_view.py` | [MEM-OBJ-semantic-knn](#mem-obj-semantic-knn), [MEM-OBJ-memory-graph](#mem-obj-memory-graph). Adaptive reader consumes separate JSON/NumPy files, not GEXF. Diagnostic rendering internals remain incompletely inspected. |
| Baseline, async facade and lightweight search; NOR-LIFT dispatch | D: facade, `src/search/chroma_search.py`, `src/search/unified_search.py`; R: [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search) | Baseline annotation distinguishes payload from metadata; NOR-LIFT wrapper falls back to ordinary Chroma search. Every BM25/vector implementation and rebuild equivalence remain uninspected. |
| Direct original-message search operations | D: `src/search/original_message_search.py`, `src/search/episode_original_message_search.py`; searched callers under `src/`, `evaluation/`, `xMemory/` | [MEM-OBJ-original-index](#mem-obj-original-index). These are callable selection capabilities. No shipped invocation linking them into final QA was found in that bounded search; do not substitute them for the reader's hydration route. |
| Adaptive reload, ranking, generation scoring, hydration and answer | D: `evaluation/locomo/xMemory_search_framework.py`; R: [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) | Adaptive annotation and read-back below. Prefix-KV implementation and all tokenizer/model variants not audited; numerical/cache equivalence and safe fit within model context remain unestablished. |
| User deletion, individual deletion, cache clear, buffer cleanup | D: `src/core/memory_system.py`, `src/storage/episode_storage.py`, `src/storage/semantic_storage.py`, `src/core/message_buffer.py` | [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). No cross-layer withdrawal guarantee follows from backend deletion. Cache-clear/rebuild names are not proof that all later readers refresh. |
| Evaluation artifacts and diagnostic consumers | R: [RT-RTE-offline-evaluation](runtime.md#rt-rte-offline-evaluation); D: reader result formatting; searched `evaluation/locomo/analysis_category.py`, `evaluation/locomo/generate_scores.py` | Offline result/metric consumers, not an admission loop. Metric internals, completed scores and full category-analysis logic uninspected; benchmark benefit and automatic feedback into memory unestablished. |
| CLI, events, hooks and tools | D: facade and searched `src/`, `xMemory/`, construction/reader CLI; R: [RT-ABS-action-dispatch](runtime.md#rt-abs-action-dispatch) | Episode-created event schedules extraction. Search CLI exposes hybrid/vector/BM25 and baseline/adaptive choice; Python additionally exposes vector_norlift. No additional registered memory tool/hook route was found by searches for `tool_calls`, `register_tool`, `hook` plus public definitions. This bounded inventory does not cover arbitrary host integrations. |
| Opaque model/provider state | R: [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client), [RT-RTE-provider-admission](runtime.md#rt-rte-provider-admission) | Parameters, version mutability and trust boundary remain as supplied. No provider-internal memory, training or cache horizon can be inferred from these clients. |

## Core ideas

1. **Summaries do not replace the retained trace.** Episode text and originals coexist. Semantic comparison and conditional answer hydration can return to originals; cold-start extraction instead starts from an already derived episode. These paths have different exposure to compression loss ([MEM-OBJ-original-messages](#mem-obj-original-messages), [MEM-OBJ-semantic-content](#mem-obj-semantic-content)).
2. **Prediction-correction appends statements rather than demonstrably repairing prior ones.** Prior knowledge shapes a predicted episode; comparison yields new statement strings. The save path rejects similar same-type statements and otherwise appends them. Reasons, prediction and contradiction targets are not fields of that converted result. This is trace-fed retention with later consumers, not demonstrated truth correction or improved capacity ([RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), memory annotation below).
3. **Text, membership and vectors have different consumers.** Theme membership limits semantic candidates; dense vectors rank; summaries enter scoring prompts. Themes are not included in the final answer prompt. Source links guide episode selection but do not automatically deliver supporting originals to the model ([MEM-OBJ-theme-summary](#mem-obj-theme-summary), [MEM-OBJ-theme-topology](#mem-obj-theme-topology), [MEM-OBJ-retrieval-vectors](#mem-obj-retrieval-vectors)).
4. **Selection is a soft, count-bounded context policy, not a truth or token-budget guarantee.** Adaptive thresholds operate on generated-token NLL differences, include negative thresholds and a fallback, and test summaries before deciding raw expansion. There is no established final-answer uncertainty reduction. The original-message setting limits episode blocks only when positive, not individual messages or tokens ([RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose), adaptive annotation below).
5. **Withdrawal is weaker than retention.** Independent files, indexes, instance caches and running semantic tasks need coordinated invalidation. The inspected user-delete method does not perform that coordination ([MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-original-messages
Label: Episode original_messages

Source-native identity: `Episode.original_messages`. Natural-language content consists of message role/content strings; symbolic envelope fields identify messages and times. Substrate: nested dictionaries in per-user episode JSONL, or instance RAM with the in-memory repository. Lineage: admitted messages converted with cleaned metadata, not an independent transcript authentication. Dataset ingestion can already incorporate image captions/search text, as supplied by [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission). This object is that route's retained trace output, not the route itself; no supplied operative-object counterpart exists.

Consumers: comparison extraction, single-episode semantic extraction, original-message search indexes, and flagged answer hydration. Message prose has model-interpreted force only; roles embedded in the final memory display are text, not privileged conversation-role messages. Access is selected by namespace/episode ID and expansion policy. These are raw relative to xMemory's summarization, not raw sensor data or proof of human authorship. SRC-1, `src/models/episode.py`, `src/generation/prediction_correction_engine.py`, `src/generation/semantic_generator.py`, `evaluation/locomo/xMemory_search_framework.py`.

> original_messages=[msg.to_dict(clean_metadata=True) for msg in messages],
> --- `src/models/episode.py`

#### MEM-OBJ-episode-content
Label: Episode title and content

Source-native identity: `Episode.title` and `Episode.content`, separately from originals and access fields. Form: natural-language title/summary; substrate: the same episode JSONL or in-memory repository. Lineage: model condensation or generator fallback of the segmented messages, with boundary reason retained separately. Later consumers: cold-start semantic extraction, vector/BM25 indexing, prediction query construction, adaptive scoring and answering. Authority: model-interpreted evidence/context, not a validated fact or executable rule. This is the derived output of [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission), distinct from its retained originals. The supplied route's generator passage and persistence account support production; SRC-1, `src/models/episode.py`, `src/generation/prediction_correction_engine.py`, `evaluation/locomo/xMemory_search_framework.py` support subsequent consumption. Lossless reconstruction from content alone is not established; originals remain separately reloadable.

> Episode Content: {episode.content}
> Episode Time: {episode.timestamp.strftime("%Y-%m-%d")}
> --- `src/generation/prediction_correction_engine.py`

#### MEM-OBJ-semantic-content
Label: SemanticMemory content

Source-native identity: `SemanticMemory.content`. Form: natural-language atomic statement strings, despite the name semantic. Substrate: per-user semantic JSONL; RAM alternative. Lineage: cold-start extraction from episode summary, original-versus-prediction comparison, or direct extraction. Later consumers: future prediction, theme summarization, vector/lexical retrieval, adaptive scoring and final answer. Model interpretation gives statements behavioral influence; code does not verify their truth. This retained output is distinct from [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), its producer/consumer route, with no supplied object counterpart.

The comparison conversion fixes generic type and confidence and keeps a source episode ID; it does not retain the predicted text, an explicit criticism or a superseded-statement target. It therefore preserves provenance reachability better than justification. SRC-1, `src/models/semantic.py`, `src/generation/prediction_correction_engine.py`, `src/generation/semantic_generator.py`, `src/core/memory_system.py`.

> memory = SemanticMemory(
>     user_id=user_id,
>     content=statement,
>     knowledge_type="knowledge",  # Use generic type
>     source_episodes=[source_episode.episode_id],
>     confidence=0.9,  # High confidence, learned from actual differences
>     created_at=source_episode.timestamp  # Use actual occurrence time of source episode
> )
> --- `src/generation/prediction_correction_engine.py`

#### MEM-OBJ-memory-metadata
Label: Memory identifiers and provenance fields

Source-native identity: episode/semantic IDs, `user_id`, timestamps, `source_episodes`, confidence, tags and revision counters. Form: symbolic fields with code-defined selection/serialization rules; free-text `boundary_reason` and generation metadata are descriptive rather than selectors unless a consumer explicitly reads them. Substrate: alongside prose in JSONL, indexes and result dictionaries. Lineage: UUID/code defaults, source timestamps, caller namespace, generator metadata. This cross-object access/provenance part spans [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) and [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission); it is not a duplicate of either route.

Actual authority: source episode IDs induce adaptive episode candidates; times are rendered to the answer model; user IDs address stores but do not authenticate users. Confidence is a generated constant, not measured confidence. A model's `update_content` method increments a revision counter in RAM, while filesystem `save` skips an existing ID: neither alone establishes durable revision. SRC-1, `src/models/episode.py`, `src/models/semantic.py`, `src/storage/semantic_storage.py`, `evaluation/locomo/xMemory_search_framework.py`.

> if memory_id in self._memory_index:
>     logger.debug(f"Semantic memory {memory_id} already exists, skipping")
>     return memory_id
> --- `src/storage/semantic_storage.py`

#### MEM-OBJ-theme-summary
Label: ThemeNode summary

Source-native identity: `ThemeNode.summary`. Form: natural-language high-level topic text, stored in theme JSONL separately from IDs and numerical vectors. Lineage: fixed summarization prompt over selected statement strings; updated during maintenance. Consumer: adaptive generation-scoring model; the final answer excludes the theme list. Authority is model-interpreted topical context at scoring, with indirect downstream influence through selection. This is a retained output of [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), not another hierarchy route. SRC-1, `src/core/memory_hierarchy.py`, `src/core/memory_system.py`, `evaluation/locomo/xMemory_search_framework.py`.

A consequential limit: small-theme refresh selects only member IDs present in the supplied current text dictionary. The orchestrator creates a fresh manager and passes the new batch. Thus summary refresh can describe only the current batch's intersection while membership still includes older statements. This is a source-level counterexample to assuming every saved summary abstracts every retained member; actual occurrence and answer impact are unobserved.

> texts = [all_semantic_texts[sid] for sid in theme.semantic_ids if sid in all_semantic_texts]
> if not texts:
>     return theme
> summary, emb = self._summarize_semantics(texts)
> --- `src/core/memory_hierarchy.py`

#### MEM-OBJ-theme-topology
Label: ThemeNode membership and neighbors

Source-native identity: `ThemeNode.semantic_ids`, member count, theme ID and neighbor IDs/similarities. Form: symbolic membership/adjacency consumed by deterministic candidate filtering, with scalar edge weights. Substrate: theme JSONL and in-memory theme dictionaries. Lineage: centroid attachment, split/merge/coalescence and recomputed theme-kNN. Distinct from summary prose and dense vectors; all are outputs of [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission). Consumer: adaptive selector constructs semantic-to-theme membership, picks theme representatives and restricts semantic candidates. This is actual selector authority rather than a claim that the final model reads a graph. SRC-1, `src/core/memory_hierarchy.py`, `evaluation/locomo/xMemory_search_framework.py`.

> for tid in selected_theme_ids:
>     tobj = themes[tid]
>     for sid in (tobj.get("semantic_ids") or []):
>         allowed_sem_from_theme.add(sid)
> sem_cand_ids = [sid for sid in S_pool_ids if sid in allowed_sem_from_theme]
> --- `evaluation/locomo/xMemory_search_framework.py`

#### MEM-OBJ-retrieval-vectors
Label: Retained embeddings and centroids

Source-native identity: episode/semantic search embeddings, theme summary embeddings and theme centroids. Form: distributed-parametric dense representations consumed by numerical similarity, not readable facts. Substrates: Chroma collections, process caches, theme JSONL and `themes/vector/` NumPy matrix with ID JSON. Lineage: embedding calls on text; centroids combine member vectors. Embedding provenance depends on [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client); storing a vector does not pin its producing model. Adaptive reload uses persisted theme vectors but recomputes episode/semantic vectors. Mixed old/new embedding compatibility is not checked by a pinned model revision on this inspected route.

Consumers: deduplication, theme attachment/split/merge and query ranking. Their force is numerical selection, not advisory text. The objects span outputs of [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) and [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search), not a duplicate component: provider model parameters and returned retained vectors differ. SRC-1, `src/search/chroma_search.py`, `src/core/memory_hierarchy.py`, `src/core/memory_system.py`, `evaluation/locomo/xMemory_search_framework.py`.

> np.save(emb_path, emb_mat)
> --- `src/core/memory_hierarchy.py`

#### MEM-OBJ-semantic-knn
Label: Semantic kNN adjacency

Source-native identity: per-user `semantic_knn` JSON mapping statement IDs to neighbor IDs and similarity scalars. Form: symbolic weighted adjacency, derived from dense embeddings rather than preserved prose reasoning. Substrate: `semantic_knn/` files and reader cache. Consumer: adaptive representative selection among semantic candidates. New saved statements obtain positive-similarity neighbors; the updater loads previous adjacency and assigns entries for new memories, not a guaranteed global recomputation of every old neighborhood. It therefore supports retained selection structure, not an invariant globally current kNN. Distinct retained output within [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), later read by [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader). SRC-1, `src/core/memory_system.py`, `evaluation/locomo/xMemory_search_framework.py`.

> adj[mid] = neigh
> --- `src/core/memory_system.py`

#### MEM-OBJ-memory-graph
Label: HierarchicalMemoryGraph export

Source-native identity: `HierarchicalMemoryGraph.G` and embedding matrix. This is an export container, with separately identifiable operative parts: symbolic level/raw-ID nodes and typed edges, natural-language copied node text, and dense embedding payloads. Substrates: NetworkX in RAM, GEXF and companion NumPy file. Lineage: incremental batches plus current theme dictionary. The shipped update passes no message nodes. Existing nodes can update text/embedding/extra fields; incremental edge creation links only endpoints present in the supplied batch maps. Export therefore is not proof of a complete, synchronized four-level provenance graph.

Consumer: later graph reload and operator-invoked `evaluation/gexf_view.py` diagnostics, not the inspected adaptive answer route. No delivered graph text-to-answer authority is established. Unlike the live theme files, old graph nodes/edges are kept through this incremental path; deleting/merging a theme in the theme manager does not itself remove the old graph node. This container is a diagnostic output of [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), not a duplicate of its live selector objects. SRC-1, `src/core/memory_hierarchy.py`, `src/core/memory_system.py`, `evaluation/gexf_view.py`.

> if ep_id in epi_nid_map:
>     self.add_edge(epi_nid_map[ep_id], sem_node_id, kind="supports")
> --- `src/core/memory_hierarchy.py`

#### MEM-OBJ-original-index
Label: Original-message lexical indexes

Source-native identity: `OriginalMessageSearch.message_indices` and `EpisodeOriginalMessageSearch.episode_indices`. Form: symbolic token/BM25 selection structures with retained message display payloads; the text is natural language when returned. Substrate: process-local dictionaries and BM25 objects. Lineage: originals supplied as episode objects, or directly read episode JSONL; empty/tokenless inputs filtered. APIs rank by query tokens, positive score and caller top-k, returning individual messages or whole episode original blocks respectively. Their clear methods remove instance indexes.

No supplied route counterpart: these are alternate callable selectors, unlike [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search)'s shipped dispatch and [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader)'s expansion policy. The bounded caller search reported in coverage found class definitions/export but no shipped QA invocation. Accordingly this record establishes capability, not an additional later model-consumer route. SRC-1, `src/search/original_message_search.py`, `src/search/episode_original_message_search.py`, `src/search/__init__.py`.

> self.message_indices[user_id] = bm25_index
> self.message_data[user_id] = valid_message_data
> self.message_tokenized_texts[user_id] = valid_tokenized_texts
> --- `src/search/original_message_search.py`

### Routes

#### MEM-RTE-memory-withdrawal
Label: Memory withdrawal and cleanup

Endpoints/progression: direct `MemorySystem.delete_user_data` call → buffer deletion → episode/optional semantic storage deletion → unified search-index clear → returned per-component flags. Owner: caller initiates; Python methods decide and perform deletion. Context: caller owner ID, existing files/indexes/caches, possibly running semantic futures. Action effects: backend deletion, index clearing and lock-map removal. This is distinct from the supplied admission/search routes: no supplied withdrawal record exists. SRC-1, `src/core/memory_system.py`, `src/storage/episode_storage.py`, `src/storage/semantic_storage.py`, `src/core/message_buffer.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: component boolean map; exceptions can leave a partially completed map and partial deletion.
- Later read-back: backend deletion can remove inputs of subsequent searches, but theme/graph/vector/kNN files, independent reader caches and unfinished semantic work are not coordinated here; reliable disappearance from every later consumer is unestablished.
- Delegated visibility: backend and index methods receive the owner ID; no model judgment is requested.
- Selection predicate: caller-selected owner namespace, with semantic deletion conditional on semantic enablement; no content-aware rejection policy.
- Invalidation or expiry: explicit deletion only on this route; related cache presence is checked with a `pass`, not invalidated. Separate buffer cleanup selects by last-update age and deletes without episode creation; it establishes a callable cleanup capability, not an automatically scheduled TTL.
- Activation or effect: file/index removal is wired; complete withdrawal, cancellation of running writers and absence from cached answers are not observed or guaranteed.
- Evidence limits: no transaction, cascade across all hierarchy artifacts or deployed cleanup policy established; storage deletion alone cannot prove final-consumer removal.

Admission/rejection control: generic caller decides the owner scope, so a human decision is unresolved; backend software can return false or raise. No answer oracle or benchmark trigger. Mode: explicit maintenance, not model-authored revision. Recovery/rollback: no cross-component rollback is implemented by this method. Separate individual episode deletion rewrites the episode file and local storage cache/index only; it does not cascade to semantic/theme/search state here. Individual semantic `delete` returns false. `SemanticMemory.update_content` changes an object, but `save` skips an existing ID, so it is not a durable correction protocol. None of these operations is exposed as a dedicated delete/edit method on the inspected facade.

> cache_key = f"user_data_loaded_{owner_id}"
> if self.performance_optimizer.cache.contains(cache_key):
>     # Simple cache cleanup (sharding system will automatically expire)
>     pass
> --- `src/core/memory_system.py`

> def delete(self, item_id: str) -> bool:
>     """Implementation of base delete method"""
>     return False  # Simplified for now
> --- `src/storage/semantic_storage.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission)

Trace-fed update: a conversation segment is condensed to episode content but originals remain available; existing statements are selected to predict a conversation; comparison reads original role/content/time strings and predicted prose; model returns statement strings; code converts, embeds, deduplicates and appends. The durable behavior-shaping result is [MEM-OBJ-semantic-content](#mem-obj-semantic-content), subsequently read by prediction, themes and answering. This is not merely raw logging. Input authorship is unresolved for generic callers; the shipped driver uses bundled conversation data, including derived captions/search text. Neither path establishes exclusively human-origin traces.

Read-back selection for prediction uses episode title plus content as vector query, searches twice the configured statement count, then filters only the first configured count by threshold. Without vector search it samples at most fifty and takes the final configured number; on error it takes the final configured number from the input list. That fallback is list-order-based, not an established chronological recency guarantee. Model-visible prediction receives title and selected statement contents, not provenance/rationale objects. Default maximum count is ten; generated prediction/comparison limits are 8192 output tokens, not input guarantees. SRC-1, `src/generation/prediction_correction_engine.py`.

Cold start sees derived episode content, while the alternative single-episode extractor formats originals or falls back to episode content. Its category-keyed response is flattened into generic `knowledge` objects, so profile/experience/other keys do not persist as distinct stored knowledge types. Source links and timestamps survive; the prediction, critique text and reasons for admission do not survive in the converted semantic object. The supplied route's comparison quote and [MEM-OBJ-semantic-content](#mem-obj-semantic-content)'s conversion quote establish that distinction. SRC-1, `src/generation/semantic_generator.py`.

Admission is software/model controlled, not per-statement human curation. Same-knowledge-type cosine similarity above the configured threshold causes rejection; errors in duplicate detection return false. Similarity rejection is not an entailment or contradiction test. Existing statements are not replaced by this save loop. Strongly similar corrections can be rejected; dissimilar contradictory statements can coexist. These are possible source-level cases, not measured frequencies. New accepted statements affect subsequent duplicate checks in the task, caches, indexing and incremental maintenance. Index failure does not roll back the repository save. SRC-1, `src/core/memory_system.py`.

> if similarity > self.config.semantic_similarity_threshold:
>     return True
> --- `src/core/memory_system.py`

#### On [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission)

Curation here is both structural and textual: statements attach by centroid, themes split through candidate partitions, merges require size limits and positive objective gain, and summaries are regenerated only after numerical decisions. Candidate scores are not answer oracles and do not persist as explanations of each accepted revision. Source statements remain separately retained. Summary text has a different lineage from topology, as recorded in [MEM-OBJ-theme-summary](#mem-obj-theme-summary) and [MEM-OBJ-theme-topology](#mem-obj-theme-topology).

The actual orchestrator constructs a fresh ThemeManager for each call. Its initializer reloads themes but initializes semantic text/vector caches empty; the provided new batch does not supply all old statement texts. Small-theme summary refresh can therefore omit old members even though membership keeps their IDs. Split paths can also skip members whose vectors/text cannot be recovered from the batch or local cache. Do not interpret successful maintenance statistics as proof of complete semantic coverage. SRC-1, `src/core/memory_hierarchy.py`, `src/core/memory_system.py`.

> self._semantic_text_cache = {}  # Dict[str, str]
> self._semantic_emb_cache = {}  # Dict[str, np.ndarray]
> self._proto_themes = {}  # Dict[str, ThemeNode] 仅在构建期用，收两条就晋升
> --- `src/core/memory_hierarchy.py`

Local theme JSONL/vector persistence is wired; optional Chroma upsert/delete helpers exist, but `assimilate_and_accommodate`'s inspected persistence tail calls the local save methods, not those helpers. No mandatory Chroma synchronization follows from their existence. Graph export retains old nodes/edges while live theme files are replaced; it has a diagnostic consumer rather than the adaptive selector's authority. SRC-1, `src/core/memory_hierarchy.py`.

#### On [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search)

Read direction is requested: caller supplies namespace/query/counts, code selects retained text, results return to that caller. The shipped baseline QA caller subsequently formats them; arbitrary facade callers have no established model consumption beyond result delivery. Chroma returns episode/semantic documents plus IDs, scores and metadata, without originals in its inspected result construction. Thus the positive original-message cap alone does not cause baseline hydration: `_hydrate_episode_results` first requires `expand_original`. Baseline Chroma results do not set that flag. Other backend result shapes remain bounded by the coverage limits, not a universal no-originals claim. SRC-1, `src/search/chroma_search.py`, `evaluation/locomo/xMemory_search_framework.py`.

The `vector_norlift` Python method is a name, not proof of its described aggregation: the unified implementation logs unsupported NOR-LIFT and returns ordinary Chroma episode search. This qualifies, rather than invalidates, the supplied route's dispatch inventory. SRC-1, `src/search/unified_search.py`.

> logger.warning("NOR-LIFT ranking not supported with ChromaDB, using normal ChromaDB search")
> return self.chroma_search.search_episodes(user_id, query, top_k)
> --- `src/search/unified_search.py`

#### On [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader)

Read-back is a requested question-driven chain, not an unsolicited push. Code reloads retained files by owner, embeds the question, ranks semantic content, uses membership/neighbors for representatives, follows source episode IDs and mixes in episode-vector candidates. Selection budgets are forty initial semantics, five themes, twenty semantic representatives, ten vector episode candidates and ten probes; positive caller episode count caps selected episodes, otherwise ten. These are counts, not maximum prompt tokens. The semantic count option is not the adaptive semantic cap. SRC-1, `evaluation/locomo/xMemory_search_framework.py`.

Scoring receives theme and statement prose plus one episode summary/content at a time against a fixed semantic-only baseline. Its optional full-message argument exists, but adaptive episode scoring does not pass it. Expansion therefore uses summary-level NLL difference, not a test of originals. Early stops can miss unprobed candidates. Final answering gets rendered semantic and episodic content, timestamps and any hydrated originals; it does not get theme prose, adjacency, vectors, confidence or a stored explanation for selection. This narrows [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) by actual consumer. The supplied runtime supplies the scoring-surrogate and final-prompt passages.

Original hydration's cap and final rendering's cap are conditional on being positive. Zero does not disable originals; once expansion is flagged, nonpositive values bypass these cap checks. Rendering loops through every message of each admitted block, not a top-k of individual messages. No active truncation of episode text was found in `_estimate_entropy`; its truncation lines are commented out. Final answer output is capped at 64 generated tokens, independent of input length. SRC-1, `evaluation/locomo/xMemory_search_framework.py`.

> if self.include_original_messages_top_k > 0 and expanded_count >= self.include_original_messages_top_k:
>     continue
> --- `evaluation/locomo/xMemory_search_framework.py`

> for msg in msgs:
>     lines.append(f"    • {msg.get('role', 'user')}: {msg.get('content', '')}")
> --- `evaluation/locomo/xMemory_search_framework.py`

Authority remains model interpretation. The answer prompt instructs recency preference for contradictions, but formatting alone does not enforce it, authenticate memories or establish compliance. Owner-level hierarchy cache has no file-change invalidation in this loader. Prefix-KV is per-thread, exact-prefix current computation state, not a persisted reasoning result or learned parameter update. Its failure/default behavior and surrogate mismatch remain runtime limitations.

> 4. If the memories contain contradictory information, prioritize the most recent memory
> --- `evaluation/locomo/xMemory_search_framework.py`

#### On [RT-RTE-offline-evaluation](runtime.md#rt-rte-offline-evaluation)

Retained QA JSON contains response, reference answer/evidence/category and flattened retrieved material; the reference is recorded after answering, not a memory truth-admission gate. Flattening preserves text, score, IDs, timestamp and any originals but not the whole hierarchy or the model's selection reasoning. Offline metrics and category/aggregate scripts consume saved result/metric data; no supplied route reads those scores back into extraction, hierarchy policy or the answer model. Consequently evaluation retention is an analysis trace, not demonstrated trace-fed memory improvement. This conclusion is bounded to the supplied evaluation record and the directly inspected reader formatter, with metric/category internals limited as in coverage. SRC-1, `evaluation/locomo/xMemory_search_framework.py`, `evaluation/locomo/evals.py`, `evaluation/locomo/generate_scores.py`, `evaluation/locomo/analysis_category.py`.

## Write side

The ordinary admission sequence and failure boundaries are retained in [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) and [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), with memory-specific differences above. Human initiation of the dataset command is not approval of each episode, statement or summary. Model authorship of prose is distinct from code's decision to save it and the backend's physical write. Caller-authored message truth and generic human approval remain unresolved.

The retained trace-to-derived-to-consumer chains are:

- Messages → episode summary plus retained originals → cold-start extraction or later answer context. Segmentation clears current buffers but does not erase saved originals; temporary detector exclusion removes a trailing message only from that detector invocation, as supplied in runtime.
- Originals + prediction from prior statements → new semantic strings → repository/indexes and subsequent prediction, themes and QA. Deduplication filters content by vector similarity, not by a retained criticism record.
- Statement strings/vectors → theme summary, membership and neighbors → later adaptive selection/scoring. Split/merge reshapes the index while raw episodes and statements remain elsewhere. Current-batch summary refresh and export drift qualify this chain.
- Accepted statement embeddings → semantic adjacency → later representative selection. Persisted graph export is a parallel diagnostic result, not the adaptive read substrate.

These chains retain subject-matter content and source IDs, not revised prompt policy or persistent prediction/comparison rationale. No alternate agent checkpoint or conversation-resume format is established by these inspected paths: in-memory buffers/caches are current state, repository alternatives change durability, and file reloads reconstruct memory for fresh calls rather than resume an agent's suspended reasoning. Unsupported hidden provider state remains opaque rather than presumed absent.

Maintenance admission uses numerical rules and fixed model prompts. It can reject duplicate statements, reject nonpositive-gain merges and choose split candidates; it does not establish that rejected content is false or accepted material is better. Filesystem semantic writes append and skip old IDs; episodes rewrite JSONL, as supplied by runtime. In-memory repositories append objects under locks and survive only with their owning process. User/episode deletion and local cleanup do not supply an atomic repair or rollback protocol ([MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal)).

## Read-back

Two update consumers and one answer consumer matter. Prediction receives selected prior statement contents; theme summarization receives statement strings; the final answer model receives selected rendered semantic/episodic text and possibly originals. The corresponding annotations establish what each receives after selection. A returned ID is not model-visible evidence unless some caller hydrates its content.

The foreground read is query initiated. Code selects on owner namespace, query embeddings/tokens, membership, source links, numerical adjacency and generated-token scores, then supplies text by value to fresh model calls. Semantic tasks are automatic after episode creation, but they are update invocations with an explicit selector, not independent unsolicited delivery to a foreground agent. No human edits or manual adoption gate intervene in the shipped read path. Static prompts frame source text as memories and instruct temporal reasoning; they do not grant it executable authority.

Working-context control is selected-input construction. Detector history exclusion, segment condensation, statement extraction, theme abstraction, query-time filtering and conditional original reload determine model visibility. Worker/model calls see their prepared inputs rather than an accumulating master transcript; software returns episodes, statements, scores or answers across those call boundaries. This resembles isolated call frames, but stored episode IDs are not model-dereferenceable pointers. Originals and summaries can remain outside the current window and return only through explicit code retrieval. The prefix-KV cache optimizes repeated scoring context, not evidence that an older reasoning trajectory was recalled. Budgets constrain counts/output tokens, not all model-visible input sizes.

The original-search helper APIs and arbitrary injected implementations remain capabilities with unspecified later callers, not additional established answer routes. Offline evaluation reads answer artifacts for scoring and diagnostics; it does not supply a model reader or automatic correction loop. Delivery, actual use, beneficial change and improved capacity remain separate, with only source wiring established here.

## Integration issues

1. **Qualify theme abstraction completeness.** [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) is correct about summary generation and structural maintenance, but must not imply all old member text reaches regeneration. [MEM-OBJ-theme-summary](#mem-obj-theme-summary) and the hierarchy annotation establish current-batch-only small-theme refresh and empty fresh caches (SRC-1, `src/core/memory_hierarchy.py`, `src/core/memory_system.py`). Consequence: persisted summary/membership alignment and complete provenance cannot be assumed. Occurrence/impact remain unobserved.
2. **Qualify NOR-LIFT as a dispatch name.** [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search) includes the method correctly, but the inspected unified route falls back to normal Chroma ranking (SRC-1, `src/search/unified_search.py`). Consequence: do not attribute Noisy-OR/LIFT aggregation to the shipped default wrapper.
3. **Clarify the original-message budget.** [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader)'s cap is a positive-only cap on episode blocks, not raw message count, tokens or a zero-disable switch. Baseline Chroma does not set the expansion flag. The adaptive and baseline annotations retain the witnesses (SRC-1, `evaluation/locomo/xMemory_search_framework.py`, `src/search/chroma_search.py`). Consequence: no universal bounded-input or universal original-message expansion conclusion.
4. **Withdrawal is not global invalidation.** [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) names leftover hierarchy files/caches and ongoing writers; [MEM-OBJ-memory-graph](#mem-obj-memory-graph) names stale export structure. SRC-1, `src/core/memory_system.py`, `src/core/memory_hierarchy.py`. Consequence: later query removal and cascade consistency remain unestablished even if backend flags are true. Exact deployed deletion practice is unavailable, not absent.
5. **Retained confidence/revision fields do not establish repair.** [MEM-OBJ-memory-metadata](#mem-obj-memory-metadata) and [MEM-OBJ-semantic-content](#mem-obj-semantic-content) qualify [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission): fixed confidence, append-only default save, no retained criticism target, and similarity rejection. SRC-1, `src/generation/prediction_correction_engine.py`, `src/storage/semantic_storage.py`, `src/core/memory_system.py`. Consequence: prediction-correction remains a source-native name, not verified statement correction, learning or epistemic warrant.
6. **Unresolved alternatives and version consistency.** [MEM-OBJ-retrieval-vectors](#mem-obj-retrieval-vectors), [MEM-OBJ-original-index](#mem-obj-original-index), and supplied provider/baseline records delimit mixed embedding versions, injected backend behavior, lexical/vector branch internals and unspecified helper consumers. The coverage table records missing facts and prevented conclusions. No inaccessible included component is silently treated as absent.

No possible duplicate declaration remains after comparison: the new operative objects are retained outputs or selector state distinct from supplied routes/components, and the new withdrawal route has no supplied counterpart. Existing route/authority referents are annotated rather than redeclared. No amendment or supersession is requested; the qualifications above can coexist with the supplied narrower facts.

## Limitations and checks

SRC-1 HEAD was rechecked as `1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608`; source identity and boundary fields match the supplied inputs. Only source reading/search and the prescribed Commonplace check were used. All consequential new passages retain verbatim witnesses or supplied-record evidence. Available but incompletely inspected branches and external access limits are named in coverage; no live successful construction, factual quality, provider reliability, global synchronization, benchmark gain or causal improvement follows from this report.

Validation: the invocation-specific deterministic output check passed. This establishes structural/reference/quotation checks, not semantic acceptance, observed activation or benefit.
