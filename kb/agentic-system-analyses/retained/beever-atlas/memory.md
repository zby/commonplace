---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Beever Atlas memory: message-derived facts, graph and summaries, dual wiki representations, QA recall and selective withdrawal."
run-id: AAS-2026-10-15-beever-atlas-10a3512c094c-01
source-identity: https://github.com/Beever-AI/beever-atlas
reviewed-boundary: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
---

# Beever Atlas memory report

## Boundary and evidence

This report covers retained messages, extracted facts and graph data, topic/channel summaries, wiki content and controls, QA histories, ingestion checkpoints, and maintenance/evaluation state within [the whole-system boundary](boundary.md). SRC-1 is the only source. HEAD was rechecked as `7d791af27ef4aa19644cb385c7ca24619bc4f848`. Direct inspection below adds implementation evidence at that pin; supplied runtime findings are identified separately. No target program, tests, providers or services were executed. Actual activation, answer quality and benefit remain unobserved.

External model parameters and external clients' memory policies are outside inspectable implementation. Static shipped prompts are guidance, not accumulated memory. Current-run ADK state is working context except where checkpoints or later MCP turns consume it. Screenshots and other boundary exclusions remain excluded. Available but uninspected alternatives below are not access failures or absent mechanisms.

| Entry point / operation | Source path under SRC-1 | Coverage and limits |
|---|---|---|
| Platform sync, signed push, background/inline extraction | `src/beever_atlas/services/sync_runner.py`; `src/beever_atlas/api/sources.py`; `src/beever_atlas/services/extraction_worker.py` | Supplied [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion); not independently exhaustively read. |
| File-import commit | `src/beever_atlas/api/imports.py`; `src/beever_atlas/services/file_importer.py` | Direct commit and parsing searches; [MEM-CLM-import-admission](#mem-clm-import-admission). Preview/parser breadth uninspected; no claim of equivalent format fidelity. |
| Fact admission, provenance and graph dedup | `src/beever_atlas/agents/callbacks/quality_gates.py`; `src/beever_atlas/agents/ingestion/cross_batch_validator.py`; `src/beever_atlas/agents/ingestion/persister.py`; `src/beever_atlas/models/domain.py` | Direct reads of gates, validator and persister construction; [MEM-OBJ-atomic-fact](#mem-obj-atomic-fact), [MEM-OBJ-fact-metadata](#mem-obj-fact-metadata), [MEM-OBJ-text-vector](#mem-obj-text-vector), [MEM-OBJ-graph-entity](#mem-obj-graph-entity). Full entity-registry/adapter algorithms uninspected. |
| Retry checkpoint save/reload | `src/beever_atlas/services/batch_processor.py`; `src/beever_atlas/agents/callbacks/checkpoint_skip.py` | Direct save/key reads and reload/cleanup searches, supplied ingestion route; annotation below. No assertion of checkpoint serialization fidelity under every provider variant. |
| Topic and channel consolidation | `src/beever_atlas/services/consolidation.py`; `src/beever_atlas/agents/consolidation/summarizer.py` | Direct context/summary/save/model reads; [MEM-RTE-summary-retention](#mem-rte-summary-retention). Full reconsolidation is located but not exhaustively audited. |
| Temporal supersession and search fallback | `src/beever_atlas/services/contradiction_detector.py`; `src/beever_atlas/stores/weaviate_store.py`; `src/beever_atlas/server/app.py` | Direct detector/store excerpts and app wiring searches; [MEM-RTE-fact-supersession](#mem-rte-fact-supersession). |
| Incremental wiki and curation | `src/beever_atlas/services/wiki_maintainer.py`; `src/beever_atlas/api/wiki.py` | Supplied [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-RTE-page-curation](runtime.md#rt-rte-page-curation); memory annotations. |
| Full refresh/reorganize/rebuild; dual-store read | `src/beever_atlas/api/wiki.py`; `src/beever_atlas/wiki/builder.py`; `src/beever_atlas/wiki/cache.py`; `src/beever_atlas/wiki/data_gatherer.py` | Direct refresh, frozen override and cache reads, gatherer searches; [MEM-RTE-wiki-refresh](#mem-rte-wiki-refresh), [MEM-OBJ-wiki-page](#mem-obj-wiki-page). Compiler modules, structure planner, auto-builder and migrations remain partially inspected or uninspected; no universal admission/quality guarantee. |
| QA tools, search API and MCP granular reads | `src/beever_atlas/agents/tools/memory_tools.py`; `src/beever_atlas/agents/tools/wiki_tools.py`; `src/beever_atlas/api/search.py`; `src/beever_atlas/api/mcp_server/_tools_retrieval.py` | Direct fact/overview/wiki/search/provenance reads and MCP catalog search; [MEM-RTE-knowledge-retrieval](#mem-rte-knowledge-retrieval). Granular module/section/decision/tension/fact tools located; full selector implementations not all inspected. |
| HTTP/MCP conversation memory, skills, web/bot delivery | `src/beever_atlas/api/ask.py`; `src/beever_atlas/stores/chat_history_store.py`; `src/beever_atlas/agents/query/qa_agent.py`; `src/beever_atlas/api/mcp_server/_ask_runner.py`; `web/src/hooks/useAskSession.ts`; `bot/src/index.ts` | Direct HTTP history/generation persistence and skill construction reads; supplied [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask), [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) for enclosing loop and consumers. Web/bot not independently reread; no uniform cross-client context claim. |
| Lint, drift, feedback, offline evaluation | `src/beever_atlas/services/wiki_lint.py`; `src/beever_atlas/services/wiki_drift_comparator.py`; `src/beever_atlas/api/wiki.py`; `src/beever_atlas/api/ask.py`; `scripts/qa_test_harness.py`; `scripts/wiki_bench.py`; `tests/integration/test_sim_memory_then_wiki.py` | Direct lint/comparator reads, feedback searches; [MEM-CLM-evaluation-authority](#mem-clm-evaluation-authority). Harnesses/tests only supplied boundary coverage: not executed or fully read, preventing claims about measured quality or automatic corrective learning. |
| Hard purge versus reset | `src/beever_atlas/services/channel_deletion.py`; `src/beever_atlas/api/channels.py` | Direct purge/fanout excerpts, reset and endpoint searches; [MEM-RTE-channel-withdrawal](#mem-rte-channel-withdrawal). Cross-process races, version archives and reaper operation not exhaustively audited. |
| Provider routing, outbox recovery, embedding migration, alternate stores | `src/beever_atlas/api/assignments.py`; `src/beever_atlas/services/reconciler.py`; `src/beever_atlas/api/embedding_migration.py`; `src/beever_atlas/api/embedding_settings.py`; `src/beever_atlas/stores/__init__.py` | Supplied [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment), [RT-CLM-write-completion](runtime.md#rt-clm-write-completion); migration route/store method searches only. Numerical lineage, restart recovery and parity of all backends remain unresolved. |

## Core ideas

1. **Derived knowledge is layered rather than simply replayed.** Raw messages support extraction; quality-gated fact prose and symbolic provenance feed graph enrichment and selected summaries; those feed wiki construction. Consumers can bypass the wiki and request facts or a channel/topic summary. Thus wiki freshness is not equivalent to freshness of every answer path. See [MEM-RTE-summary-retention](#mem-rte-summary-retention), [MEM-RTE-knowledge-retrieval](#mem-rte-knowledge-retrieval).
2. **The persisted wiki is not one authoritative text blob.** The compatibility cache combines per-page maintenance metadata with legacy render fields. A successful incremental page save need not establish that a compatibility QA read sees its new sections as content. Slug-keyed MCP reads use the page store directly. This is an integration question, not an observed stale-answer incident: [MEM-OBJ-wiki-page](#mem-obj-wiki-page).
3. **Retention and retrieval apply different rejection rules.** High-confidence contradiction judgments mark old facts invalid; semantic/hybrid search excludes invalid facts by default. The BM25 fallback does not perform that same invalidation filter. Therefore automatic supersession does not establish universal withdrawal: [MEM-RTE-fact-supersession](#mem-rte-fact-supersession).
4. **Conversation memory is a separate feedback source.** HTTP answer text becomes both session-tail context and searchable past QA. The later model can therefore receive its own prior outputs, not just independent conversation evidence. Thumbs ratings and lint/drift results do not by themselves establish a route revising knowledge or instructions: [MEM-OBJ-chat-history](#mem-obj-chat-history), [MEM-CLM-evaluation-authority](#mem-clm-evaluation-authority).

## Shared records

### Components

#### MEM-CMP-topic-summarizer
Label: Topic and channel summarizer models

Source-native identities: `topic_summarizer` and `channel_summarizer`, both resolving provider consumer `summarizer`. These are separate model calls with the same assignment family, not another name for [RT-CMP-wiki-maintainer](runtime.md#rt-cmp-wiki-maintainer). Distributed-parametric endpoint parameters reside with the provider. The inspected constructors request structured outputs; they do not update weights. Exact weights/version are not pinned by the application commit; overrides and mutable provider assignments/endpoints can resolve differently. Provider internals and deployed identity are uninspected. SRC-1: `src/beever_atlas/agents/consolidation/summarizer.py`.

> name="topic_summarizer",
> model=model or get_llm_provider().resolve_model("summarizer"),
> --- `src/beever_atlas/agents/consolidation/summarizer.py`

#### MEM-CMP-contradiction-detector
Label: Contradiction detector model

Source-native identity: `contradiction_detector`, distinct from extraction models [RT-CMP-fact-extractor](runtime.md#rt-cmp-fact-extractor) and [RT-CMP-entity-extractor](runtime.md#rt-cmp-entity-extractor). Distributed-parametric model with provider-owned storage. The constructor supplies shipped instructions, `ContradictionReport` schema and recovery wrapper. No parameter update occurs in this inspected route. Exact version is not pinned; explicit override and mutable provider resolution can change it. Provider-internal behavior is uninspected. SRC-1: `src/beever_atlas/agents/ingestion/contradiction_detector.py`.

> name="contradiction_detector",
> model=model or get_llm_provider().resolve_model("contradiction_detector"),
> --- `src/beever_atlas/agents/ingestion/contradiction_detector.py`

### Operative objects

#### MEM-OBJ-channel-messages
Label: Durable normalized source messages

Source-native identity: MongoDB `channel_messages`, with legacy `imported_messages` for optional dual file-import writes. Natural-language content is source evidence; symbolic identifiers, source/channel fields and extraction status control scheduling and provenance lookup. These are raw normalized inputs, not extracted claims. Authorship can be human, bot, imported or mixed; platform/source labels do not establish the ultimate author. Distinct from process-local [RT-OBJ-session-state](runtime.md#rt-obj-session-state): the batch consumes selected durable rows. SRC-1: `src/beever_atlas/api/imports.py`; supplied [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion). Later `read_provenance` can reload raw message content by a fact's channel/message identifier; missing raw text is allowed, so a citation is not proof the raw evidence remains available ([MEM-RTE-knowledge-retrieval](#mem-rte-knowledge-retrieval)).

#### MEM-OBJ-atomic-fact
Label: Extracted fact prose

Source-native identity: `AtomicFact.memory_text`, plus optional natural-language `thread_context_summary`, `rationale`, alternatives and open consequences. Stored through the vector store's `MemoryFact` records. Derived from message batches and preprocessing, not a verbatim event log. Prose affects QA through model interpretation and affects later summarization/wiki generation. Quality gates may rewrite narration and reject low model-scored outputs before persistence. Existing raw messages do not guarantee that extraction preserved reasons. The schema can retain decision rationale when present; the generic fact search result does not deliver that field separately. No counterpart object was declared in runtime: [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) describes the producer, not the retained fact. SRC-1: `src/beever_atlas/models/domain.py`, `src/beever_atlas/agents/callbacks/quality_gates.py`, `src/beever_atlas/agents/tools/memory_tools.py`.

> filtered = [f for f in facts_dicts if f.get("quality_score", 0.0) >= threshold]
> after_count = len(filtered)
> --- `src/beever_atlas/agents/callbacks/quality_gates.py`

#### MEM-OBJ-fact-metadata
Label: Fact access, provenance and lifecycle metadata

Source-native identity: the identifiers, channel/source fields, tags, `quality_score`, `invalid_at`, `superseded_by` and `potential_contradiction` accompanying `AtomicFact`. Symbolic fields in vector-store records, distinct from the prose they index. Consumers use them for filtering, grouping, ordering, citations and invalidation. Model-generated quality is not independent truth evidence. The persister uses content/entity-derived IDs and attaches source metadata by exact reference, URL match or word-overlap fallback; the latter records `derived_from="heuristic_word_overlap"`. Thus provenance can be inferred rather than authenticated. These fields are not another referent for [RT-OBJ-session-state](runtime.md#rt-obj-session-state). SRC-1: `src/beever_atlas/models/domain.py`, `src/beever_atlas/agents/ingestion/persister.py`.

> if heuristic_match:
>     fact_data["derived_from"] = "heuristic_word_overlap"
> --- `src/beever_atlas/agents/ingestion/persister.py`

#### MEM-OBJ-text-vector
Label: Retained text and entity-name vectors

Source-native identities: fact `text_vector` and graph/entity-registry `name_vector`. Distributed numerical representations stored beside symbolic/prose records; not model weights. Fact embeddings derive from text through [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model); entity registry name-embedding generation is visible in the persister, but its full provider/version lineage was not traced. Consumers use fact vectors for similarity retrieval and name vectors for dedup candidates. Mutable embedding configuration and re-embedding can change representation independently of prose. Migration endpoints and snapshot/reinsert store operations were located, not fully audited; exact existing vector provenance is unresolved. Distinct from the model producing the vectors. SRC-1: `src/beever_atlas/models/domain.py`, `src/beever_atlas/agents/ingestion/persister.py`, `src/beever_atlas/stores/weaviate_store.py`, `src/beever_atlas/api/embedding_migration.py`.

#### MEM-OBJ-graph-entity
Label: Retained entities and graph relationships

Source-native identities: `GraphEntity`, `GraphRelationship`, graph store and entity registry. Symbolic node/edge identities and types have fixed query semantics; names/descriptions/properties can carry natural-language content. Name vectors are separately covered above. Extractor proposals pass confidence filtering and deterministic name/embedding dedup before graph persistence; registry absence degrades to exact-match-only handling rather than proving no graph admission. Consumers include consolidation's decision/person/technology/project enrichment and wiki data gathering. Graph storage alternatives are within scope but adapter parity is uninspected. Distinct from [RT-CMP-entity-extractor](runtime.md#rt-cmp-entity-extractor), the model producer. SRC-1: `src/beever_atlas/models/domain.py`, `src/beever_atlas/agents/ingestion/cross_batch_validator.py`, `src/beever_atlas/agents/callbacks/quality_gates.py`, `src/beever_atlas/services/consolidation.py`, `src/beever_atlas/wiki/data_gatherer.py`.

> logger.warning(
>     "DeterministicCrossBatchValidator: entity_registry unavailable "
>     "— running in exact-match-only mode (job_id=%s batch=%s)",
> --- `src/beever_atlas/agents/ingestion/cross_batch_validator.py`

#### MEM-OBJ-topic-cluster
Label: Topic and channel derived summaries

Source-native identities: retained `TopicCluster` and `ChannelSummary` in Weaviate. Natural-language summaries, title, current state, open questions and FAQ candidates derive from selected member facts and graph enrichment. Symbolic member IDs, tags and `summary_dirty` determine membership/refresh; they are access/update metadata rather than the summary's knowledge content. Numerical staleness and vectors are not proof of truth. Later overview tools return summary text; wiki gathering also consumes clusters and channel summaries. Their curation and lifetime differ from atomic facts. No counterpart in runtime beyond the producer/consumer routes [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) and [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask). SRC-1: `src/beever_atlas/services/consolidation.py`, `src/beever_atlas/agents/tools/wiki_tools.py`.

#### MEM-OBJ-wiki-page
Label: Wiki persistence content and compatibility rendering

Source-native identities: MongoDB `wiki_pages` and legacy `wiki_cache`, plus version snapshots accessed through `WikiVersionStore`. Natural-language section markdown and rendered `content` are different retained content surfaces; structured `kind_schema`, module payloads and links are symbolic/display data. Controls and maintenance metadata belong to the persisted page, with curation authority already declared in [RT-BAP-page-curation](runtime.md#rt-bap-page-curation). This object is distinct from that authority path and from [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance).

The compatibility `get_page` reader can merge both stores: persisted version/curation/dirty state remains authoritative, but explicitly selected render-only keys, including `content` and `summary`, come from the cache. Slug MCP reads instead return the serialized page-store record. A record's successful update is not enough to prove every consumer receives the rewritten text. Wiki archives support history reads; no universal automatic rollback or complete restore route was established. SRC-1: `src/beever_atlas/wiki/cache.py`, `src/beever_atlas/api/mcp_server/_tools_retrieval.py`, `src/beever_atlas/agents/tools/wiki_tools.py`.

> merged: dict = dict(per_page_row)
> for k in _RENDER_ONLY_KEYS:
>     if k in cache_row:
>         merged[k] = cache_row[k]
> return merged
> --- `src/beever_atlas/wiki/cache.py`

#### MEM-OBJ-chat-history
Label: Conversation and searchable QA history

Source-native identities: MongoDB `chat_history` and Weaviate QA history. Natural-language user/assistant text is retained as prior dialogue; symbolic ownership/channel/session metadata controls lookup. Thinking text, tool traces, citations and attachment metadata are separately retained display/trace fields, not all reintroduced to the model. The HTTP context loader creates model parts from message `content` only. Searchable QA is selected by channel/query rather than session tail; it can deliver earlier generated answers as evidence, with an optional refusal filter. No external truth check is established. Distinct from ephemeral [RT-OBJ-session-state](runtime.md#rt-obj-session-state); [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) produces/consumes this object rather than being its identity. SRC-1: `src/beever_atlas/api/ask.py`, `src/beever_atlas/stores/chat_history_store.py`, `src/beever_atlas/agents/tools/memory_tools.py`.

> if settings.qa_history_negative_filter:
>     results = [r for r in results if r.get("answer_kind", "answered") != "refused"]
> return results
> --- `src/beever_atlas/agents/tools/memory_tools.py`

### Routes

#### MEM-RTE-summary-retention
Label: Selected facts become retained summaries

Distinct successor route to [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion), not a duplicate ingestion pipeline. Code owns cluster selection and persistence; the summarizer proposes title/prose/structured fields. Settlement and incremental consolidation can trigger it. SRC-1: `src/beever_atlas/services/consolidation.py`, `src/beever_atlas/agents/consolidation/summarizer.py`, `src/beever_atlas/server/app.py`.

- Immediate return: summary counts, errors and touched fact IDs after cluster upserts.
- Later read-back: overview tools reload cluster/channel summary text; wiki data gathering reads summaries and member facts for later compilation.
- Delegated visibility: up to 50 fetched members per cluster, with active fact prose ranked by quality and top 20 used in cluster context; graph/tag aggregates accompany the selected content. Channel summarization derives from cluster summaries rather than all raw messages.
- Selection predicate: dirty or missing summary and touched clusters; member quality and supersession govern context; requested topic overview matches tags and otherwise falls back to the first cluster.
- Invalidation or expiry: persisted `summary_dirty` is cleared before successful upsert; future membership changes can dirty again. No content TTL established.
- Activation or effect: stored summaries become available knowledge and affect later compiler/model input; actual changed answers are unobserved.
- Evidence limits: member caps and model derivation prevent claims of complete evidence/rationale preservation; no observed summary quality or benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software/model controlled, with no per-summary human approval established. Shipped topic/channel guidance asks for narrative and structured summaries; returned fields are applied to clusters. Empty topic title triggers one retry at temperature 0.3; a second empty title falls back to the original result for later compiler synthesis. Exceptions append errors; only successfully written summaries add member IDs to the downstream touched set. This is ongoing knowledge transformation, not an expected-answer experiment; no answer oracle is established. Raw-to-derived-to-consumer chain: message → gated fact → selected cluster context → persisted summary → overview tool or wiki compiler. Retained key facts include IDs and source fields, but the model's full derivation reasons are not thereby retained.

> active = [f for f in members if f.superseded_by is None]
> # Sort by quality_score descending, take top 20
> active.sort(key=lambda f: f.quality_score, reverse=True)
> top_facts = active[:20]
> --- `src/beever_atlas/services/consolidation.py`

> cluster.summary_dirty = False
> await self._weaviate.upsert_cluster(cluster)
> result.summaries_generated += 1
> --- `src/beever_atlas/services/consolidation.py`

#### MEM-RTE-knowledge-retrieval
Label: Requested knowledge read-back

A family of requested read operations subordinate to the tool-selection loop in [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) or called directly through MCP/API; not a replacement for either enclosing QA route. The model/caller chooses a tool/query; code and backing stores choose retained records. SRC-1: `src/beever_atlas/agents/tools/memory_tools.py`, `src/beever_atlas/agents/tools/wiki_tools.py`, `src/beever_atlas/api/search.py`, `src/beever_atlas/api/mcp_server/_tools_retrieval.py`.

- Immediate return: selected facts, wiki/summary text, prior QA or provenance dictionaries; failures generally produce empty/structured errors, while search API uses HTTP errors.
- Later read-back: a later request retrieves knowledge accumulated by ingestion, summary/wiki maintenance or prior QA; source IDs can support a further provenance request.
- Delegated visibility: QA receives returned tool payloads, not entire stores. Fact search delivers prose plus selected metadata, not separately retained decision rationale/alternatives. `read_provenance` can return original raw message content; a missing message yields an empty string with structured source metadata.
- Selection predicate: channel/query/tier and requested limits; fact search tries native hybrid with query embeddings, overfetches `min(limit * 3, 30)`, then token-overlap MMR with lambda 0.6; optional recent filter is 30 days. Search API instead uses `pseudo_hybrid_search`, default limit 20 (1–100) and threshold 0.7. Wiki selectors differ: fixed page type, topic tag, or explicit slug/language.
- Invalidation or expiry: query selection is repeated per call; store invalidation applies unevenly across hybrid/BM25 paths. No universal retrieval TTL; errors can be cold/empty results.
- Activation or effect: returned prose is evidence for model/human interpretation, not an executable instruction grant or proven answer change. Symbolic scope checks and selectors constrain covered reads.
- Evidence limits: granular MCP module/section/decision/tension/fact selectors were located but not fully traced; no parity or complete authorization claim across all read surfaces.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is pull read-back, even when the server automatically builds an embedding or reranks after receiving the request. A fixed page ID is addressing, not semantic targeting. Topic lookup is only a tag-substring match, with first-cluster fallback, so a positive return need not be the requested topic. The activity wiki reader has a specific stale-sentinel fallback to live recent facts. Direct MCP `read_wiki_page` honors hidden-page scope and returns page-store data; compatibility QA `get_wiki_page` returns `content`, `summary` and a short grounding excerpt. Read roles are established by shipped tools and QA wiring, not by inventing a caller for a storage API.

> fetch_limit = min(limit * 3, 30)
> try:
>     query_vector = await _embed_query(query)
> --- `src/beever_atlas/agents/tools/memory_tools.py`

> if best is None and clusters:
>     best = clusters[0]
> if best is None:
>     return None
> --- `src/beever_atlas/agents/tools/wiki_tools.py`

#### MEM-RTE-fact-supersession
Label: Contradiction judgment changes retrieval eligibility

Distinct lifecycle transformation after [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion). New-fact checks and a channel settlement/watermark path call contradiction detection; app subscription wiring is configuration/startup dependent. Model proposes existing-fact IDs/confidence/reasons; code applies thresholds. SRC-1: `src/beever_atlas/services/contradiction_detector.py`, `src/beever_atlas/stores/weaviate_store.py`, `src/beever_atlas/server/app.py`.

- Immediate return: best-effort check completion/count; per-fact exceptions are logged rather than propagated as universal failure.
- Later read-back: semantic/hybrid default retrieval excludes records with `invalid_at`; consolidation context excludes `superseded_by`. Old facts remain stored and addressable.
- Delegated visibility: detector sees new-fact text/tags and up to ten existing candidates; not every fact or original message.
- Selection predicate: first entity tag selects existing facts; self, duplicates and already invalid candidates are removed. A topic-tag-only fact can enter the check but the inspected candidate population uses entity tags, so no candidates are guaranteed.
- Invalidation or expiry: high confidence sets old `invalid_at`/`superseded_by` and new `supersedes`; intermediate confidence flags the new fact. No automatic restoration of a wrongly superseded fact established.
- Activation or effect: symbolic lifecycle fields change participating selectors; BM25 fallback can still return invalid facts. No observed correctness of supersession.
- Evidence limits: model confidence is not an oracle; ordering and swallowed per-fact failures bound settlement/watermark guarantees. Universal withdrawal is false for the inspected BM25 branch.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Software admits changes automatically at configured thresholds; no per-fact human veto is established. Guidance is the shipped contradiction instruction and schema, not a retained revision of extraction policy. The report's reason is produced in working state, but the inspected mutation writes lifecycle fields rather than a durable criticism record linked to later readers. Open ongoing knowledge maintenance has no supplied expected-answer oracle. Recovery is best effort, not transactional rollback. The implementation contradicts a reading of the docstring as exhaustive entity/topic candidate search.

> if confidence >= settings.contradiction_confidence_threshold:
>     await stores.weaviate.supersede_fact(
>         old_fact_id=fact_id,
>         new_fact_id=new_fact.id,
>     )
> --- `src/beever_atlas/services/contradiction_detector.py`

> result = collection.query.bm25(
>     query=query,
>     query_properties=self._BM25_QUERY_PROPERTIES,
>     limit=limit,
>     filters=combined,
> )
> return [self._obj_to_fact(obj) for obj in result.objects]
> --- `src/beever_atlas/stores/weaviate_store.py`

#### MEM-RTE-wiki-refresh
Label: Full wiki refresh and destructive rebuild

Alternative writer to incremental [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), not the same route. An authenticated, channel-authorized request selects update/reorganize/rebuild and optional force; the backend schedules `WikiBuilder.refresh_wiki`. SRC-1: `src/beever_atlas/api/wiki.py`, `src/beever_atlas/wiki/builder.py`, `src/beever_atlas/wiki/cache.py`, `src/beever_atlas/wiki/data_gatherer.py`.

- Immediate return: accepted status/mode and force-recompile flag before generation finishes.
- Later read-back: builder output is saved to cache and per-page seed records; later API/QA/MCP readers consume their respective representations. Existing cache versions are archived best effort.
- Delegated visibility: compiler gathers channel summary, clusters, recent/media facts and graph enrichment; individual modules/planner context budgets were not fully inspected.
- Selection predicate: channel/language and mode; build-input hash can skip recompilation unless forced; frozen pages are looked up before compile and restored afterward where matching IDs exist.
- Invalidation or expiry: rebuild wipes current cache/per-page state before generation; update/reorganize retain different structure behavior. Snapshot cleanup applies, but archive retention policy was not independently audited.
- Activation or effect: replaces generated wiki output and can reset curation/structure on rebuild; no measured knowledge improvement established.
- Evidence limits: frozen lookup is best effort and can fail open to compilation; full module validation/admission parity with incremental maintenance is uninspected. Snapshot failure does not block destructive rebuild.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The caller admits workflow/mode, not every generated claim; the compiler/model proposes knowledge under shipped guidance. Generic authentication does not establish human authorship. Unknown modes default to update. Rebuild attempts an archive before scheduling wipe, but catches archive errors; therefore the comment promising an always-present rollback point is stronger than enforcement. Generation failures/status handling are recovery, not guaranteed automatic restoration. No expected-answer oracle is established; this is a production refresh workflow.

> except Exception as exc:  # noqa: BLE001 — never block rebuild on archive failure
>     logger.exception(
>         "wiki_rebuild_snapshot_failed channel=%s lang=%s err=%s",
> --- `src/beever_atlas/api/wiki.py`

> except Exception:  # noqa: BLE001 — frozen detection is best-effort
>     pass
> --- `src/beever_atlas/wiki/builder.py`

#### MEM-RTE-channel-withdrawal
Label: Hard purge removes later knowledge and history inputs

Distinct destructive lifecycle route, compared with operator page controls [RT-RTE-page-curation](runtime.md#rt-rte-page-curation). Shipped channel deletion calls a purge service; reset is an alternative with deliberately different retention. SRC-1: `src/beever_atlas/services/channel_deletion.py`, `src/beever_atlas/api/channels.py`.

- Immediate return: counts/errors, audit/run identity and completed/partial/already-in-progress result.
- Later read-back: successful deletion removes facts, graph/wiki and QA/chat inputs from covered stores; retained purge lock and audit guide retry/reaper handling. This is deletion authority, not learned guidance.
- Delegated visibility: ordered store fanout operates on channel identity; no model sees or approves each removed record.
- Selection predicate: requested channel and CAS purge-lock claim; full purge differs from reset, which keeps source messages and chat history while resetting extraction state.
- Invalidation or expiry: hard delete targets graph, facts, QA history, page-store pages in all languages, render cache/status, chat history, Mongo channel data and media. Errors retain lock for recovery.
- Activation or effect: covered future reads lose the deleted content after successful effects; partial errors can leave readable remnants. Cancellation is best effort and process-local.
- Evidence limits: complete cross-process non-resurrection, every archived/shared copy and exercised reaper convergence were not established. No transactional all-store deletion guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Explicit caller request and software checks admit deletion; no model proposal/oracle is involved. The service can refuse a concurrent lock claim, continues after individual stage failures, records audit, and retains the lock on errors. Recovery is retry toward convergence, not undo; provenance and raw evidence may disappear along with knowledge. This route prevents equating a fact tombstone, hidden wiki page or reset with full erasure.

> status = "completed" if not errors else "partial"
> if not errors:
>     try:
>         await stores.mongodb.release_purge(channel_id)
> --- `src/beever_atlas/services/channel_deletion.py`

### Claims

#### MEM-CLM-import-admission
Label: File import commit is retention, not extraction completion

Claimed operation: import documentation describes background ingestion, but the inspected current commit path normalizes/upload-selects messages, upserts durable `channel_messages`, optionally dual-writes legacy rows, records sync state and waits for manual sync. The durable upsert catches errors as non-fatal. A commit response is therefore not evidence of knowledge extraction or universally successful new-store admission. Caller-selected upload/commit is content supply, while later model/software stages admit derived facts; no per-fact approval follows. Compare [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion), whose unresolved manual-import variant this refines rather than corrects. SRC-1: `src/beever_atlas/api/imports.py`.

> # Register sync_state so the channel shows as "ready" (0 processed / N total)
> # in the sidebar. Do NOT run BatchProcessor here — matching the platform
> # flow, extraction runs when the user clicks "Sync Channel".
> --- `src/beever_atlas/api/imports.py`

#### MEM-CLM-evaluation-authority
Label: Evaluation records do not establish automatic corrective learning

Claimed operation: lint documentation promises a bounded LLM coherence pass, but the API passes `llm_provider=None`; implementation supplies structural empty-section findings in that case. Even with a provider the inspected function returns findings without a model invocation. Orphan/stale/duplicate checks produce an explicit report; they are not source-truth validation. Drift comparator runs supplied incremental/regenerate factories, computes a report, logs and optionally persists it. Its body does not select the winning page or revise guidance. Feedback endpoints store thumbs ratings in `qa_feedback`. A scoped search over `agents`, `services` and `stores` found no `qa_feedback` reader; this is a bounded unresolved consumer question, not a global evidenced absence. No automatic rating-to-policy/knowledge update is established. Distinct from [RT-CLM-write-completion](runtime.md#rt-clm-write-completion), which concerns persistence recovery, not evaluation. SRC-1: `src/beever_atlas/services/wiki_lint.py`, `src/beever_atlas/api/wiki.py`, `src/beever_atlas/services/wiki_drift_comparator.py`, `src/beever_atlas/api/ask.py`.

> run_coherence_check=run_coherence_check,
> llm_provider=None,  # Production wires LLMProvider here
> --- `src/beever_atlas/api/wiki.py`

> # Production LLM path is wired by the API handler — this function
> # is kept pure-async so unit tests can stub the provider easily.
> return findings
> --- `src/beever_atlas/services/wiki_lint.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-fact-lifecycle
Label: Retained lifecycle fields govern later selection

Consumer: semantic/hybrid retrieval and consolidation context builder. Channel: persisted `invalid_at` and `superseded_by` fields. Force: deterministic exclusion by covered selectors; not a textual request to the QA model. Horizon: later reads/summary rounds until fields or records change. BM25 does not share this force. Distinct from [RT-BAP-page-curation](runtime.md#rt-bap-page-curation), which gates wiki updates rather than fact reads. Evidence and scope: [MEM-RTE-fact-supersession](#mem-rte-fact-supersession), SRC-1: `src/beever_atlas/stores/weaviate_store.py`, `src/beever_atlas/services/consolidation.py`.

## Annotations

#### On [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Checkpointed state is a retained recovery part, distinct from an entire ADK conversation. MongoDB stores whitelisted snapshots of `preprocessed_messages`, `extracted_facts`, `extracted_entities`, `classified_facts`, `embedded_facts` and `validated_entities`, with stage identity/timing. A later retry reloads keys into a new session and skips restored stages. The snapshot contains symbolic payloads, derived prose and potentially vectors; it is not a generated compact narrative. Final successful completion deletes the checkpoint. It preserves intermediate artifacts, not a complete rationale trace. Alternative stages and retry-provider variants were not exhaustively audited. SRC-1: `src/beever_atlas/services/batch_processor.py`, `src/beever_atlas/agents/callbacks/checkpoint_skip.py`.

> _cp_snapshot = {
>     k: _cp_state[k]
>     for k in _ALL_CHECKPOINT_KEYS
>     if k in _cp_state
> }
> --- `src/beever_atlas/services/batch_processor.py`

#### On [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask)

Memory consumers have unequal budgets and visibility. The durable context store selects the last ten **messages**, despite the `MAX_CONTEXT_TURNS` name and loader docstring saying turns. `_load_chat_history_parts` requires known user/channel provenance when supplied and returns cold start on lookup errors. It converts only `content` to role/text parts; thinking, full tool traces and attachment bodies are not reconstructed by that loader. The request builds a fresh working context, with prior dialogue as a text prefix and optional recall hint. Persisted thinking is capped at 20 KiB, but this is a storage/display budget, not model-context compaction. Earlier dialogue beyond the tail remains reachable through history/search surfaces, not automatically summarized by this loader. This resembles frame replacement with explicit replay, not a pointer-bearing heap or a complete resumed HTTP execution frame. SRC-1: `src/beever_atlas/stores/chat_history_store.py`, `src/beever_atlas/api/ask.py`.

> async def get_context_messages(self, session_id: str) -> list[dict]:
>     """Return the last MAX_CONTEXT_TURNS messages for agent context window."""
>     doc = await self._collection.find_one(
>         {"session_id": session_id},
>         {"_id": 0, "messages": {"$slice": -MAX_CONTEXT_TURNS}},
>     )
> --- `src/beever_atlas/stores/chat_history_store.py`

Mode/tool filtering and optional ADK skills affect reachable external context. SkillToolset is added alongside underlying tools, not a child-agent isolation boundary; exact dependency-owned skill loading/eviction and context budgets remain uninspected. No host compaction algorithm was established by this inspected HTTP loader. QA retention gives later requests access to previous model outputs; that is a trace-fed write/read chain, not demonstrated improved capacity. The prompt's grounding/untrusted rules remain requests rather than guaranteed model compliance; [RT-CLM-untrusted-tools](runtime.md#rt-clm-untrusted-tools) retains the effect-boundary caveat.

#### On [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask)

The supplied runner inspection establishes process-memory session reuse, unlike HTTP durable-tail replay. It does not establish a durable cross-restart QA history write from this wrapper. Provider/dependency-internal compaction is uninspected, so HTTP's ten-message budget must not be attributed to this path. Principal-namespaced selection and context lifetime are retained as supplied runtime findings, not independently reverified source reads here.

#### On [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

New fact IDs, current page and curation state select retained material for a new completion. This is automatic push from the event chain into the maintainer, not unsolicited push into the later QA model. The maintainer proposes affected sections under shipped prompts and persists merged output; reasons may survive in fact prose or page content but no complete derivation trace is guaranteed. `last_facts_seen`/dirty state are selector metadata, not learned claims. The downstream read distinction in [MEM-OBJ-wiki-page](#mem-obj-wiki-page) prevents assuming persistence-row sections become compatibility-tool content. Source passages for actual merge/save and schema degradation are supplied in the runtime record; no duplicate route is declared.

#### On [RT-BAP-page-curation](runtime.md#rt-bap-page-curation)

Stored auto/manual/frozen eligibility differs from hidden/pinned presentation controls. Explicit pending-update application temporarily switches eligible manual pages to auto and restores manual afterward, as supplied in [RT-RTE-page-curation](runtime.md#rt-rte-page-curation). Full builder frozen detection is best effort, and rebuild can wipe controls ([MEM-RTE-wiki-refresh](#mem-rte-wiki-refresh)); the incremental invariant does not become a universal persistence invariant.

## Write side

Admission is not equivalent to authorship or successful physical I/O. Platform/push/file callers supply raw content; authentication and payload checks admit acquisition, not truth. Extraction models propose fact/entity representations, quality callbacks normalize/reject, deterministic dedup reconciles entities and persister code attaches provenance and writes stores. None of these establishes per-content human approval. Initial origins can be mixed or unknown even when adapter/source identity is known. The post-acquisition transformations remain inspectable despite that uncertainty ([MEM-OBJ-channel-messages](#mem-obj-channel-messages), [MEM-CLM-import-admission](#mem-clm-import-admission)).

Quality gates use scores emitted in derived payloads, not independently validated reference answers. Narration filtering can fail back to original facts. Entity/relationship confidence gates and dedup are different checks, not universal semantic validation. Persisted numerical vectors are derived selectors, not changes to the extractor's weights. Partial vector/graph writes and unestablished reconciler scheduling remain as [RT-CLM-write-completion](runtime.md#rt-clm-write-completion) states.

The principal automatic trace-fed transformations are message→fact/graph→summary→wiki and question/answer→QA/session history→later context. Checkpoints add a different raw/derived-to-retry chain without semantic summarization. Model-generated summaries/pages can retain decisions and reasons as content; that is weaker than retaining every reason the model used. Supersession does not durably link its reported reason to later readers in the inspected code. None of these chains alone demonstrates improved capacity, reflection or revised method theory.

Maintenance has several admission mechanisms: incremental parser/curation rules, full-build compiler rules, caller-directed mode/structure changes, and threshold-directed fact supersession. They have different veto and recovery semantics. Lint/drift/ratings retain diagnostics without an established automatic repair/adoption path. Purge removes data with partial-failure reporting; reset retains source material for reprocessing. See the route records instead of treating all of these as one generic 'memory update'.

## Read-back

Later consumers are concrete: extraction workers/retries consume durable message/checkpoint state; summarizers consume selected facts/graph; compiler/maintainer consumes derived knowledge/current pages; QA models receive selected tool results and a bounded conversation tail; API/MCP/web users receive persisted render/page data. Actual external client adoption is not established.

Demand retrieval is driven by question/query, channel, topic or explicit page/fact identity. Summary production and wiki event maintenance are automatic successor deliveries, but they do not imply proactive knowledge insertion into every future QA request. Tool mode grants and natural-language tool-call budgets bound intended context acquisition differently; the latter are not enforced context-token counters. Stored content reaches model/human interpretation as evidence. Only symbolic selectors/control fields have the specific deterministic authority shown in the records; delivered prose is not thereby an instruction override or proof of compliance.

Compatibility wiki reads may overlay stale render fields, granular slug reads bypass that overlay, and hybrid/BM25 invalidation differs. Searchable old QA can reintroduce a prior generated answer even when newer source facts exist; no synchronizing correction path from supersession to every historical answer was established. These route distinctions prevent a system-wide freshness or complete-forgetting conclusion.

## Integration issues

- **HTTP budget clarification:** [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) is not materially contradicted, but any 'ten turns' rendering should say ten stored messages. `ChatHistoryStore.get_context_messages` uses a message-array slice (annotation above). This changes the claimed working-context horizon.
- **Dual wiki representations:** [MEM-OBJ-wiki-page](#mem-obj-wiki-page) and the annotation on [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) identify a consumer ambiguity. `WikiCache.get_page` overlays legacy render content while preserving newer metadata. The missing fact is whether every incremental update also synchronizes the relevant render keys; the supplied save passage alone cannot prove it. Retain per-consumer uncertainty rather than infer fresh QA text from new version metadata.
- **Frozen/rollback scope extension:** [MEM-RTE-wiki-refresh](#mem-rte-wiki-refresh) supplements, not supersedes, [RT-BAP-page-curation](runtime.md#rt-bap-page-curation). Full builds try to preserve frozen pages, but lookup exceptions are swallowed; rebuild can remove controls and proceeds after archive failure. Universal frozen protection and always-available rollback would be unsupported.
- **Invalidation exception:** [MEM-RTE-fact-supersession](#mem-rte-fact-supersession) and [MEM-BAP-fact-lifecycle](#mem-bap-fact-lifecycle) show semantic/hybrid exclusion but no BM25 invalidation filter. This limits all retrieval freshness/withdrawal claims. New-topic-only candidate selection also remains narrower than the detector's entity/topic wording.
- **Evaluation labels:** [MEM-CLM-evaluation-authority](#mem-clm-evaluation-authority) contradicts source comments promising an LLM lint pass. Drift deployment wiring, feedback later consumers, evaluator-induced updates and benchmark outcomes are unresolved; do not connect retained diagnostics to automatic learning without that route.
- **Coverage limits retained:** granular MCP selectors, compiler modules/structure planning/auto-building, all import formats, entity registry algorithms, alternate storage adapters, full reconsolidation, embedding migration/checkpoint lineage, archive/shared-copy erasure and reaper convergence are not fully audited. The table names their available evidence; no uniform quality, security, provider-provenance or deletion conclusion is supported.
- **Identity comparison:** no new declaration intentionally replaces a supplied record. New objects are persisted artifacts rather than runtime's model/session referents; summary, supersession, full refresh and withdrawal are distinct successor/alternative operations, while requested retrieval is the tool-operation family inside HTTP/MCP invocation. Existing session/QA/incremental/curation referents receive annotations, not redeclarations. Reconciliation can retain these distinctions without inventing duplicate IDs.

## Limitations and checks

All positive operational descriptions are implementation wiring or affordances, not observed use. No supplied trace or intervention supports activation, causal benefit, measured learning or successful self-improvement. Selection caps, inferred provenance, model-generated quality, degraded validation and alternate consumers prevent stronger reliability claims. The frozen source identity/revision and supplied method/type/record contracts were rechecked for this member; no new source ID or changed boundary was introduced.

Validation: the required `validate-output` command passed with “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes the reported content-check result, not analytical correctness or coordinator acceptance.
