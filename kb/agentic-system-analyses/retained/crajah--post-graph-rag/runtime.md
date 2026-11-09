---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "post-graph-rag runtime baseline: document admission, retrieval and synthesis, derived reports, caller extensions and release controls."
run-id: AAS-2026-11-08-post-graph-rag-448d75e4222d-01
reviewed-boundary: "bce4146a7dc4684e9b66806915c29b0eed57ba23"
---

# post-graph-rag runtime report

## Runtime account

### Work and ordinary invocation

post-graph-rag is a caller-driven knowledge-system library, not an agent scheduler. A caller supplies documents and questions; Python fixes the next operation while models extract records, identify query terms, optionally decompose questions, summarize communities and synthesize answers. The enclosing exploration loop belongs to the application, as established in [boundary](boundary.md#boundary-and-evidence). This report uses SRC-1 implementation and embedded doctrine at the frozen revision. It adds inspection of the quickstart and helper, model wrapper, extraction branches, report renderer, retrieval/store filters, retention and release configuration. No target execution, tests, provider calls or tracked result artifacts were exercised or assessed as run evidence. All operation and benefit conclusions below remain uninspected.

The shipped `examples/01_quickstart.py` creates a fresh realm through `_shared.py`, initializes GraphRAG, indexes three named documents sequentially with `index_document`, asks a cross-document question, prints the answer and selected triples, and closes in `finally`. The helper sets schema-per-realm and reads router/database/model settings from the environment. This example makes the caller the indexing and question principal; it does not show an independent worker or planner. SRC-1, `examples/01_quickstart.py`, `examples/_shared.py`:

> res = await rag.index_document(text, metadata={"source": source})
> --- `examples/01_quickstart.py`

GraphRAG construction wires configurable model service, extractor, chunker, detector, reporter and database connection. Initialization connects and initializes schema. [RT-RTE-document-admission](#rt-rte-document-admission) traces passage preparation and ordered writes. The returned identity is a database chunk ID, with counts and degradation flags; document identity additionally uses source/title and a content hash. Entity aliases resolve to vertices; relation endpoints reference those vertices. Realm and space scope database operations, not provider contexts. A caller may retain the realm and reconnect later; the fresh quickstart realm is demonstration isolation rather than automatic production retention policy. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/models.py`, `post_graph_rag/graph_store.py`.

An ordinary default `query` runs `query_data`, which derives keywords if neither keyword list is supplied, embeds the question and optionally keyword-enriched text, searches documents/entities, walks outward relations, optionally searches relation vectors and full text, merges/reranks and formats results. Mix/local use entity and document channels; global uses reports and graph-wide relations; hybrid combines them; naive uses the document channel. Mix is not the community-report mode. Optional subqueries expand entity and lexical seeds. RRF uses per-channel ranks; quota interleaves traversal and vector-seeded relations and omits lexical results. Query assembly then renders retrieved material into one user message, appends supplied conversation history before it and calls the synthesis model. The terminal output is either structured context, a dictionary with answer/retrieval metadata, or an async text stream. [RT-RTE-question-answer](#rt-rte-question-answer) and [RT-RTE-direct-answer](#rt-rte-direct-answer) distinguish those endpoints. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/models.py`.

### Guarantees and forcing cases

**Passage-first recovery is bounded, not atomic ingestion.** The engine owns a best-effort recovery policy: passage embedding and extraction precede `add_document`; derived embeddings can degrade to no structure on `EmbeddingError`; `ExtractionError` becomes empty structure; other extraction failures still cost the chunk. After passage insertion, structural database operations and supersession blocks catch ordinary exceptions and count them. Batch preparation gathers exceptions, skips bad chunks and raises the first failure when no chunk succeeds. Direct `index_document` instead propagates preparation failure. The external contract is that store insertion and provider calls behave as their APIs report; database transaction internals are not inspected. Implementation conclusion status: wired. Operation conclusion status: uninspected. This is no crash-atomic or cancellation-safe invariant. `index_text` deletes prior chunks before replacement preparation, whereas `index_documents` and `index_document` do not perform that whole-document replacement check. Consequently “re-index restores structure” is an available recovery action, not an unconditional automatic guarantee: unchanged-document skipping can suppress it unless disabled. See [RT-RTE-document-admission](#rt-rte-document-admission). SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/config.py`.

**Extraction validation covers the default model branch, not all supported admission.** Forcing case one follows actual supported callback shapes, not a hypothetical malformed caller: external results may be an ExtractionResult, entity/triple mapping or bare triple sequence; `_extract_external` can return the coerced result without `_validate`; replace returns it directly and merge gates each source separately before union. A fully injected extractor also replaces the default object. Thus confidence, negation, validity stripping and name/predicate gates are configurable admission policies, not universal graph constraints. Guarantee owner: GraphExtractor; enforcement point: `_validate` on branches that invoke it; strength: policy; implementation conclusion status: wired; operation conclusion status: uninspected. Schema coercion remains different from semantic filtering. See [RT-RTE-extractor-extension](#rt-rte-extractor-extension). SRC-1, `post_graph_rag/extractor.py`, `post_graph_rag/engine.py`.

**Temporal filtering is channel-specific, not reproducible historical answering.** Forcing case two follows traversal, independent vector/lexical relations, documents, entities and reports through the consumer. Engine `_filter_temporal` applies supersession, validity and belief time to all three relation lists after retrieval. The multi-hop store call additionally passes validity and null-key supersession filtering into dependency traversal, but does not pass belief time. The one-hop branch returns neighbors without validity/supersession filtering; engine filtering still removes inappropriate returned relations, but direct store callers do not receive that same guarantee. Missing validity matches all dates; missing creation timestamps are retained. Documents are filtered by `created_at` only for parseable belief instants. Entity descriptions and community reports are not filtered by belief time or validity in query_data, and report staleness only emits a warning. The synthesis consumer receives all selected channels, not only filtered triples. Moreover superseded relations remain excluded unless `include_superseded` is enabled even when asking about earlier belief time. Owner: engine/store; enforcement points: walk arguments and `_filter_temporal`; strength: policy for these relation paths, not deployment guarantee; implementation conclusion status: wired; operation conclusion status: uninspected. Dependency traversal correctness and historical state preservation are external/unestablished contracts. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`, `post_graph_rag/models.py`; see [RT-RTE-question-answer](#rt-rte-question-answer).

**Context budgeting is not a hard total-window limit.** Forcing case three follows raw context, normal synthesis, bypass and conversation history. `only_need_context` returns query_data before rendering. Normal synthesis clips document text against half `max_total_tokens`, community reports against a third, and entities/relations against separate budgets. The estimator is character count divided by four; reference lists, prompt overhead, question and history are outside those allocations. All budgets default to unlimited. Bypass supplies history/question without retrieval or these budgets. Owner: engine; enforcement: `_truncate_by_tokens` at rendering; strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. It requires caller/provider window management, not merely setting a total budget. No sub-agent frame is created: network batch concurrency isolates no autonomous agent context. Indexing snapshots known names per batch, evicts older names beyond a configured tail and renders at most the first 40 of the retained names; full source text remains in passages, not a pointer automatically dereferenced by the model. These are concrete context selection controls, not evidence of summaries learning better behavior. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/extractor.py`, `post_graph_rag/models.py`.

**Provider fallback is explicit but not one stable model.** Forcing case four follows structured parse, plain completion, embedding fallback and streaming. Structured completion catches failure or absent parsed output and retries unstructured; extraction/reporter then parse and validate the resulting text. Completion roles share ordered fallbacks; success increments an in-process served-model counter. Embeddings retry only the configured remote embedding model, but opt-in fallback tries local transformer loaders and then a deterministic hash vector. Dimension checks do not establish common vector geometry. Streaming failover covers opening only; mid-stream failures propagate rather than duplicating output. Owner: LLMService; enforcement: `_with_failover`, `_retry_same`, embedding checks and streaming wrapper; strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. A retry deadline checks between failed attempts, not a separately proven wall-clock bound on an active provider call. Provider behavior/versioning remains external. See model component records. SRC-1, `post_graph_rag/llm.py`, `post_graph_rag/config.py`.

### Effects, extension and change admission

GraphRAG executes database effects using its configured credential or caller-supplied connection/pool and sends content to the configured OpenAI-compatible endpoint. The capability surface includes direct store/client access and arbitrary injected Python callbacks. This is not a model tool authorization system: inspected model calls supply messages/schema/stream settings, not a shell or native tool grant. Models return content; Python chooses writes. Callbacks execute in the host process with host authority, not within a documented sandbox. Current deployed grants and isolation are uninspected; realm/space filters alone are not proof of authorization. Store documentation makes session-role setup a caller responsibility and leaves injected connection ownership with the caller. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/llm.py`, `post_graph_rag/graph_store.py`.

Community generation is caller-triggered derived-state replacement, with model-produced reports, deterministic clustering and optional parent summaries. It clears old reports before building replacements; partial recovery is not rollback. [RT-RTE-community-build](#rt-rte-community-build) records its admission policy. Retrieval telemetry and caller-triggered retention demotion form [RT-RTE-retention-control](#rt-rte-retention-control). Archiving excludes entity seeds and snapshot members, but relation-vector/lexical retrieval resolves endpoints without an archived-entity check; exclusion of archived seeds is not proof that the corresponding facts disappear from every answer channel. Previously built community reports also persist until rebuilt. Memory specialists own the fuller object/revision account; these are runtime consumption limits. SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`, `post_graph_rag/retention.py`.

Prompt/configuration and callback changes enter through caller construction, not an online self-modifying planner. Document order and optional model contradiction selection can supersede retained relations. The contradiction selector returns only offered IDs and returns none on failure; this bounds identity selection, not truth. Product release admission is a separate maintainer/tag/CI path, [RT-RTE-package-release](#rt-rte-package-release). Shipped evaluators can guide human configuration choices; this report does not treat benchmark scores as a runtime answer oracle or prove automatic product improvement. No broader universal absence claim about extensions or external applications follows. SRC-1, `post_graph_rag/extractor.py`, `post_graph_rag/engine.py`, `.github/workflows/publish.yml`, `.github/workflows/ci.yml`.

## Shared records

### Components

#### RT-CMP-extraction-model
Label: Extraction model

Source-native `extraction_model` (else `model`) serves extraction, gleaning and contradiction decisions. Distributed-parametric model parameters reside behind the API; this repository sends messages, not parameter updates. No inspected route trains those parameters. Exact weight version is not pinned by the configurable model-name string; a mutable configured endpoint can resolve it to different weights or fallbacks. Provider internals remain uninspected. SRC-1, `post_graph_rag/config.py`, `post_graph_rag/llm.py`, `post_graph_rag/extractor.py`.

> "extraction": "extraction_model",
> --- `post_graph_rag/config.py`

#### RT-CMP-community-model
Label: Community model

Source-native `community_model` (else `model`) produces cluster/parent reports. Distributed-parametric, externally hosted, no parameter update in inspected calls; exact weights unpinned and mutable endpoint/fallback resolution possible. Report texts, not model weights, persist in this system. SRC-1, `post_graph_rag/config.py`, `post_graph_rag/llm.py`, `post_graph_rag/reporting.py`.

> result = await self.llm_service.chat_completion(
>     messages, response_format=CommunityReport, role="community")
> --- `post_graph_rag/reporting.py`

#### RT-CMP-auxiliary-model
Label: Auxiliary model

Source-native `auxiliary_model` (else `model`) supplies keywords and optional decomposition. Distributed-parametric API component; no inspected parameter changes; exact version unpinned; mutable endpoint and shared fallback names can select another model. Responses affect current retrieval, not a parameter update. SRC-1, `post_graph_rag/config.py`, `post_graph_rag/llm.py`, `post_graph_rag/engine.py`, `post_graph_rag/extractor.py`.

> "auxiliary": "auxiliary_model",
> --- `post_graph_rag/config.py`

#### RT-CMP-synthesis-model
Label: Synthesis model

Source-native `synthesis_model` (else `model`) produces answer text or streamed deltas. Distributed-parametric, API-hosted; inspected calls do not mutate parameters. Exact version unpinned; endpoint/fallback resolution can change it. Caller-injected services can implement different behavior, not assessed here. SRC-1, `post_graph_rag/config.py`, `post_graph_rag/llm.py`, `post_graph_rag/engine.py`.

> "synthesis": "synthesis_model",
> --- `post_graph_rag/config.py`

#### RT-CMP-embedding-model
Label: Embedding model

Source-native `embedding_model` produces dense vectors used in document/entity/relation/report searches. Distributed-parametric provider component; vectors are stored numerical representations in database vector columns, not weight updates. No inspected remote parameter update; exact weights unpinned; mutable endpoint can change the model behind the name. No configured cross-model remote failover, but explicit local fallback can change the embedding mechanism. Provider internals and initial training provenance uninspected. SRC-1, `post_graph_rag/llm.py`, `post_graph_rag/config.py`.

> # Embedding models are not interchangeable across vector spaces, so
> # only the configured one is retried — never failed over.
> --- `post_graph_rag/llm.py`

#### RT-CMP-local-embedding
Label: Local embedding alternatives

The optional local component tries `fastembed.TextEmbedding()` then `SentenceTransformer("all-MiniLM-L6-v2")` before term hashing. The first two are distributed-parametric, locally loaded via optional packages, with no training call here and no exact artifact revision pin; installed package/default model resolution may vary. Endpoint mutation is inapplicable to these local loaders, but package/model cache identity is uninspected. Term hashing is a separate symbolic algorithm, not a learned fallback; dimension equality permits return but proves no compatibility with remote vectors. SRC-1, `post_graph_rag/llm.py`.

> for loader in (self._try_fastembed, self._try_sentence_transformers):
> --- `post_graph_rag/llm.py`

### Operative objects

#### RT-OBJ-query-param
Label: QueryParam and current request

Source-native dataclass `QueryParam` is symbolic process-local configuration: mode, top-k, keyword lists, subqueries, temporal selectors, budgets and flags. Its `conversation_history` is natural-language message content with symbolic role/channel wrappers. The caller supplies history; query does not itself append answers to a persistent conversation store. Query_data can mutate the param's keywords/subqueries for this or a caller-reused invocation. SRC-1, `post_graph_rag/models.py`, `post_graph_rag/engine.py`.

> if self.config.auto_decompose and p.subqueries is None:
>     p.subqueries = await self._decompose_question(question)
> --- `post_graph_rag/engine.py`

### Routes

#### RT-RTE-document-admission
Label: Document admission and replacement

Caller → GraphRAG preparation → store passage → derived graph writes → result counts. Python owns progression; model proposes extracted content, configured gates and database writes admit it without per-record human approval. Open document ingestion, not a bounded experiment; no expected-answer oracle in this route. Guidance is extraction prompt/context plus configured predicate aliases, confidence and name rules. What persists is passage/vector and admitted graph structure, not the extraction conversation. Human authorship of the supplied document is unresolved from API identity. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/extractor.py`, `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Chunk ID, extracted/written counts, extraction-empty, embedding-degraded and structure-error flags; document batches return successful chunk results.
- Later read-back: Stored passages and derived structure reach query_data and community building through the configured realm/space.
- Delegated visibility: Text/context goes to extraction service and text representations to embedding service; no agent delegation is involved.
- Selection predicate: Chunker for index_text, explicit chunks for other APIs; semantic extraction gates depend on selected extractor branch.
- Invalidation or expiry: index_text compares document hashes, skips unchanged content by default, otherwise deletes previous chunks before replacement; direct chunk APIs do not apply this replacement policy.
- Activation or effect: Passage insertion precedes structural writes; aliases/upserts combine entities, relation admission may supersede earlier relations; changed answers are not observed.
- Evidence limits: Source wiring only; dependency atomicity, cancellation behavior and provider truthfulness are not proven.

Rejection can occur before passage insertion; ExtractionError alone becomes an empty extraction. EmbeddingError for derived structure drops that structure. Later structural failures are counted rather than undoing the passage. Recovery is caller re-indexing, potentially with skip-unchanged disabled, not an automatic rollback of the deleted prior document. Batches run network preparation concurrently and serialize writes within the invocation, not a global lock over all caller instances.

> doc_emb, extraction = await asyncio.gather(
>     self.llm.get_embedding(text),
>     self._extract_or_empty(text, context),
> )
> --- `post_graph_rag/engine.py`

> doc_vertex = await self.store.add_document(
>     prepared["text"], prepared["doc_emb"], stamped, space=target_space
> )
> --- `post_graph_rag/engine.py`

> if unchanged and self.config.skip_unchanged_documents:
> --- `post_graph_rag/engine.py`

#### RT-RTE-extractor-extension
Label: External extractor admission

Caller-provided callback → coercion → optional validation → replace or merge → normal engine write path. Owner: caller selects implementation/mode, GraphExtractor executes policy. Supports synchronous or awaitable callbacks. Proposal authorship may be human-coded rules, another model or unknown software; API does not establish it. Admission/rejection uses configured validation and merge rules, not an answer oracle; mode is open ingestion. Changing callback/config changes future admission; prior graph state requires re-indexing rather than callback rollback alone. SRC-1, `post_graph_rag/extractor.py`, `post_graph_rag/engine.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Coerced ExtractionResult or ExtractionError; model extraction is skipped in replace mode.
- Later read-back: Admitted output is persisted by the same document/graph writer as default extraction.
- Delegated visibility: Callback receives text and DocumentContext in the host process; its further effects are outside inspected implementation.
- Selection predicate: extraction_fn presence and replace/merge mode; accepts model instances, mappings or triple sequences.
- Invalidation or expiry: inapplicable — no independent callback-result cache is implemented in this route; retained graph lifecycle is downstream.
- Activation or effect: validate_external=False forwards coerced content without semantic gates; merge does not revalidate the union; caller-injected whole extractor can replace this mechanism entirely.
- Evidence limits: Supported shapes and direct consumers establish reachability, not observed misuse or a sandbox escape.

> return self._validate(result) if self.validate_external else result
> --- `post_graph_rag/extractor.py`

> if self.extraction_fn is not None and self.extraction_fn_mode == "replace":
>     if external is None or not (external.entities or external.triples):
>         raise ExtractionError(
>             "The configured extraction_fn returned no usable entities or triples. "
>             "Refusing to write placeholder structure into the graph."
>         )
>     return external
> --- `post_graph_rag/extractor.py`

#### RT-RTE-question-answer
Label: Retrieved question answering

Caller question/QueryParam → keyword/decomposition calls → embeddings and store searches → relation filtering/fusion/reranking → raw context or synthesis. Engine owns the next step. Auxiliary model proposes retrieval terms, deterministic code selects context, synthesis model proposes the final answer; no correctness veto or expected-answer oracle is wired into this query route. Operating mode is open questions, with caller-selected retrieval modes rather than autonomous task planning. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/models.py`, `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: query_data gives entities, relations, passages, references and communities; query gives answer metadata unless streaming or context-only.
- Later read-back: Reads corpus retained by earlier ingestion/build calls; optional telemetry is later consumed by coverage/retention, not a retained answer cache.
- Delegated visibility: Model endpoints receive selected request material; raw context API lets the caller choose a different answer consumer.
- Selection predicate: Mode/channel membership, top-k, keywords/subqueries, relation temporal predicates, RRF or quota and optional distance/MMR; reports also rank by rating and size.
- Invalidation or expiry: Temporal relation filtering and parseable document belief cutoff; stale reports warn, not expire; context clipping discards rendered suffixes when configured.
- Activation or effect: Selected text enters synthesis user-message content; delivery is wired, factual compliance and causal answer benefit unobserved.
- Evidence limits: No universal historical-answer or total-token guarantee; entity descriptions, reports, history and independent channels prevent that inference.

> traversed = self._filter_temporal(self._dedupe_triples(graph_triples), p)
> seeded = self._filter_temporal(relation_seeded, p, sort=False)
> lexical = self._filter_temporal(relation_lexical, p, sort=False)
> --- `post_graph_rag/engine.py`

> if p.only_need_context:
>     return await self.query_data(question, param=p)
> --- `post_graph_rag/engine.py`

> 3. If the retrieved context does not answer the question, say so plainly instead of guessing.
> --- `post_graph_rag/engine.py`

The last passage is a model instruction, not an enforced truth criterion. Likewise the relation history filter removes superseded records before belief-time checking; asking an earlier belief instant alone does not override the superseded setting.

#### RT-RTE-direct-answer
Label: Bypass and streaming return

Caller → query_data bypass empty result → direct synthesis, or ordinary synthesis → streamed deltas. Engine owns branching; LLMService owns provider failover. This is open answering with no answer oracle or content-admission gate. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/llm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bypass nonstream returns answer and empty retrieval arrays; streaming returns an async iterator rather than the answer dictionary; bypass context-only returns empty structured data.
- Later read-back: inapplicable — neither bypass nor stream wrapper persists its output as knowledge.
- Delegated visibility: Supplied history/question go to synthesis provider; bypass sends no retrieved corpus context.
- Selection predicate: QueryParam.mode=bypass, stream flag and only_need_context precedence.
- Invalidation or expiry: inapplicable — caller owns supplied history and iterator lifetime.
- Activation or effect: Direct model generation or incremental text emission; no graph write except ordinary retrieval telemetry before non-bypass streaming.
- Evidence limits: Failover retries stream opening only; no observed stream trace or token-window enforcement.

> # Failover applies to opening the stream. Once tokens have been yielded a
> # retry would duplicate output, so mid-stream failures propagate.
> --- `post_graph_rag/llm.py`

#### RT-RTE-community-build
Label: Derived community report admission

Caller → graph snapshot → configurable clustering → size/cap selection → clear old communities → model reports/embeddings → stored reports and membership, optionally repeated on supergraphs. Code selects clusters and admits nonempty parsed summaries; model supplies report findings/rating, not a correctness oracle. Human chooses trigger, prompt and detector, not necessarily each report. Mode: caller-triggered derived-state build. Guidance asks grounded reporting; persistence is generated summaries and report links, not revised method instructions. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/reporting.py`, `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Community counts, hierarchy levels and skipped counts, or no-entity reason; total report failure raises.
- Later read-back: Global/hybrid queries retrieve report summaries/findings; upper levels consume lower-level reports during the same build.
- Delegated visibility: Reporter sends clipped member descriptions/relations to community model; parent synthesis uses child report projections rather than full original documents.
- Selection predicate: Snapshot excludes archived entities and optionally dormant entities, excludes dormant relations; engine keeps internal edges, minimum group size and largest capped clusters; renderer defaults to 60 entities/80 relations, 400 characters per rendered line.
- Invalidation or expiry: Rebuild clears previous communities; subsequent graph writes only trigger a staleness warning on report retrieval.
- Activation or effect: Stored reports become answer context; generated rating affects later report ranking; faithful summaries or improved broad answers remain unobserved.
- Evidence limits: No transactionally atomic rebuild/rollback shown; snapshot carries supersession metadata but build does not filter it before report generation; report prompt is not a semantic proof.

> await self.store.clear_communities(space=target_space)
> --- `post_graph_rag/engine.py`

> if not result.summary.strip():
>     raise ExtractionError("Community report had an empty summary.")
> --- `post_graph_rag/reporting.py`

Rejection is schema/nonempty-summary failure or downstream embedding/write error. Selected RAGError failures skip a cluster; other exceptions can abort. Recovery is another build, not restoration of the previous report set.

#### RT-RTE-retention-control
Label: Retrieval telemetry and archiving

Enabled query → best-effort event row → caller invokes retention → importance score → preview or archived timestamps → later seed/build exclusion. Store records selected IDs and a query hash; RetentionManager owns scoring. Caller chooses invocation/threshold/dry_run, algorithm selects entities without per-entity human approval; no correctness oracle or measured quality feedback in this route. Guidance is fixed recency/frequency/degree/age scoring with weights 0.35/0.25/0.20/0.20. It persists demotion state, not an improved theory of retrieval. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/retention.py`, `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RetentionReport includes scored/selected IDs, score range and dry_run; restore returns count; telemetry failure logs without failing query.
- Later read-back: Event statistics affect later archiving; archived entity fields affect entity vector search and graph snapshots.
- Delegated visibility: inapplicable — retention score and archive writes are local/database code, not another agent call.
- Selection predicate: Requires telemetry config, skips already dormant/archived entities, archives scores strictly below threshold when dry_run=False.
- Invalidation or expiry: restore clears archive fields; caller can purge events before a timestamp; no automatic recurring schedule established here.
- Activation or effect: Withholds archived entity seeds and snapshot members; other relation/document/report channels are not universally suppressed.
- Evidence limits: Source proves a trace-fed selection path, not better future answers or comprehensive removal from all context; events record retrieval exposure, not answer correctness.

> if not dry_run and to_archive:
>     await self.store.set_entities_archived(to_archive, now.isoformat(),
>                                            space=space)
> --- `post_graph_rag/retention.py`

#### RT-RTE-package-release
Label: Maintainer-triggered package release

Maintainer tag push → GitHub workflow checkout → version rewrite → uv build → PyPI publication. Proposal and tag authorization are repository/maintainer responsibilities; workflow executes release without a model decision. Admission policy is tag-triggered automation and external GitHub/PyPI permissions, not runtime feedback or an answer oracle. CI tests/lint run separately on main pushes/PRs/manual invocation; publish has no explicit needs dependency on CI in the inspected file. SRC-1, `.github/workflows/publish.yml`, `.github/workflows/ci.yml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Workflow build/publish outcome; no inspected release execution supplied.
- Later read-back: Published package can be installed by consumers; no automatic live upgrade route established by these files.
- Delegated visibility: GitHub runner executes build; PyPI action receives publication credentials/artifacts.
- Selection predicate: Matching version-like/v-prefixed tags trigger publication; actual tag permissions and branch protections uninspected.
- Invalidation or expiry: skip-existing prevents republishing existing versions through that action setting; package rollback/deployment recovery is outside inspected workflow.
- Activation or effect: Builds changed version metadata into package; whether any deployment adopts it is uninspected.
- Evidence limits: Configuration is not a successful release trace or proof that tests gated every release; no automatic source- or machinery-revision model loop shown by this route.

> - name: Publish to PyPI
>   uses: pypa/gh-action-pypi-publish@release/v1
>   with:
>     password: ${{ secrets.PYPI_API_TOKEN }}
>     skip-existing: true
> --- `.github/workflows/publish.yml`

### Claims

#### RT-CLM-passage-priority
Label: Passage-first invariant claim

Source doctrine prioritizes passage/vector preservation over derived structure. The bounded implementation and countercases are retained in [RT-RTE-document-admission](#rt-rte-document-admission), not treated as atomic successful ingestion on all branches. SRC-1, `post_graph_rag/engine.py`.

> #   A chunk's passage and its own vector are the irreducible unit.
> #   Extraction, entity embeddings, relation embeddings, supersession,
> #   mentions and community membership are all DERIVED -- recoverable by
> #   re-indexing -- and none of them may take the passage with it.
> --- `post_graph_rag/engine.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-extraction-guidance
Label: Extraction guidance authority

Consumer: extraction/gleaning model. Channel: system prompt plus user document/context; force: requested model interpretation, followed by symbolic gates on the default path; horizon: current extraction and derived graph consumed by later queries. Custom system prompt replaces default guidance; external replace bypasses model interpretation. SRC-1, `post_graph_rag/extractor.py`; [RT-RTE-extractor-extension](#rt-rte-extractor-extension) bounds enforcement.

> if self._system_prompt is not None:
>     return self._system_prompt
> --- `post_graph_rag/extractor.py`

#### RT-BAP-answer-context
Label: Retrieved context authority

Consumer: synthesis model. Channel: rendered retrieved facts and explicit instructions together in a user message, with separate system role and preceding caller history. Force: natural-language evidence/instruction, not a code-enforced answer oracle; horizon: current answer, and only caller-retained history if supplied later. Stored report ratings separately have symbolic force in report ranking. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/models.py`.

> messages = [{"role": "system", "content": "You are a helpful Knowledge Graph RAG assistant."}]
> if p.conversation_history:
>     messages.extend(p.conversation_history)
> messages.append({"role": "user", "content": prompt})
> --- `post_graph_rag/engine.py`

## Annotations

none
