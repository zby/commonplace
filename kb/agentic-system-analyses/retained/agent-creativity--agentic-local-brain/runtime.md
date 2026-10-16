---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Agentic Local Brain runtime baseline: collection, retrieval, mining, wiki admission and installation changes at the frozen source revision."
run-id: AAS-2026-10-12-agentic-local-brain-f00cbd577178-01
reviewed-boundary: "41ea0cb104686eb0d39f32c94c2b84d37cdff0e7"
---

# Agentic Local Brain runtime report

## Runtime account

### Evidence and consequential work

This is a source trace of the knowledge application defined in [the boundary](boundary.md). SRC-1 is the sole source. All implementation and instruction findings below concern commit `41ea0cb104686eb0d39f32c94c2b84d37cdff0e7`. No target code, examples, tests or providers were executed. Persistence, activation, model compliance, quality and performance in an installation remain unobserved. Code-grounded wiring is not a successful-run claim.

The application's consequential work is to admit collected material, derive metadata and numerical search representations, mine relations and topics, synthesize durable wiki articles, and return retained material or model-generated answers. The console aliases `localbrain` and `kb` enter `kb.cli:cli`; Click registers separate collection, search, mining, wiki, management, backup and self-update drivers. FastAPI registers HTTP drivers and serves the frontend and skill documentation. A desktop agent may instead follow the collection skill and invoke the CLI. These are different principals and entry paths, not one autonomous tool-using model loop (SRC-1 `pyproject.toml`, `kb/cli.py`, `kb/web/app.py`, `skills/localbrain-collect/SKILL.md`).

The application owns the next step in its model-dependent pipelines. Models return text or structured suggestions; Python parses results, selects documents, writes files/databases and produces responses. The inspected completion calls do not implement a provider-tool execution dispatcher. A keyword-search subprocess runs a constructed `rg` argument list, while update and web-launch subprocesses perform explicit application operations. Host browser/shell grants belong to the excluded desktop agent, not to Local Brain ([RT-ABS-tool-dispatch](#rt-abs-tool-dispatch); SRC-1 `kb/query/keyword_search.py`, `kb/commands/utils.py`, `kb/self_update.py`).

### Ordinary invocation: collect a file, then ask about retained knowledge

1. An operator or external agent invokes `localbrain collect file add <path>`. Click requires an existing path and supplies extraction and duplicate-check options. The driver resolves the source path, creates a `FileCollector` and metadata storage, and calls `collect`. The collector checks the suffix, optionally checks an existing source through storage, extracts content, generates metadata and a destination filename, and writes Markdown with YAML frontmatter. Its return carries saved path, title, word count, metadata ID and content hash (SRC-1 `kb/commands/collect.py`, `kb/collectors/file_collector.py`, `kb/collectors/base.py`; [RT-RTE-file-admission](#rt-rte-file-admission)).
2. When extraction is enabled, the driver reloads the saved file. Caller-supplied nonempty tags/summary take priority; missing values come from the configured model, then built-in extraction. It updates frontmatter and saves the knowledge row and tags. This is automatic per-content admission, not an approval queue. Starting collection does not mean a human reviewed its generated summary (SRC-1 `kb/processors/tag_extractor.py`, `kb/commands/collect.py`).
3. The indexing helper chunks the reloaded material, embeds chunk text, constructs IDs `<item-id>_chunk_<index>`, writes Chroma documents/vectors, then writes SQLite chunk records. These effects are sequential rather than one transaction across all substrates. Collection can report success without indexing success (SRC-1 `kb/commands/utils.py`, `kb/commands/collect.py`).
4. For a later web question, `POST /api/rag/chat` constructs or reuses the application-owned `RetrievalPipeline`. Dependency construction attempts semantic and keyword search, LLM expansion/reranking, graph/topic enrichment, reading history and conversation storage independently; unavailable components degrade to no-op or missing components. The request supplies question, optional session ID, tags, top-k and options. The endpoint returns the pipeline result as JSON and schedules reading-history recording (SRC-1 `kb/web/routes/search.py`, `kb/web/dependencies.py`; [RT-RTE-chat-query](#rt-rte-chat-query)).
5. Except for a cache hit, the pipeline creates or reuses a session, formats recent conversation turns, expands the question, combines semantic, graph and keyword retrieval with reciprocal-rank fusion, reranks, enriches, constructs a budgeted context and requests an answer. Fusion is keyed by knowledge ID and chooses one result's content per document; context construction may truncate or omit candidates. Returned source metadata is therefore not proof that every source's full content reached the answer model. Graph retrieval is an additional route and does not receive the tags argument at its call site; tags are not a demonstrated end-to-end isolation rule (SRC-1 `kb/query/retrieval_pipeline.py`, `kb/query/context_builder.py`).
6. The answer model receives system/user messages, assembled context and formatted history. Python constructs a result with answer, sources, context, confidence, fired-stage labels and session/turn metadata. Before returning it, Python attempts to save user and assistant turns with source dictionaries. Save failures are logged and do not prevent returning the answer. Subsequent calls with the session ID can reload those turns. Model failure can instead produce a source-title list. An empty retrieval returns before turn saving; a cache hit returns before session creation/history loading. There is no universal “every question becomes a persisted conversation” guarantee (SRC-1 `kb/query/retrieval_pipeline.py`, `kb/query/conversation.py`).

### Material alternatives and forcing cases

Four cases challenge the tempting stronger account:

- **Indexing failure after file admission.** `file_add` catches indexing exceptions, and the helper itself returns false on failure. This defeats interpreting a collection-success message as proof of semantic-search availability or coordinated durability. It leaves the collection mechanism intact ([RT-RTE-file-admission](#rt-rte-file-admission)).
- **Legacy RAG and host-assisted admission.** CLI search and `POST /api/rag` use the separate `RAGQuery` path; its fallback can use unfiltered keyword search, rather than the enhanced pipeline. A restricted webpage can be fetched by the host, saved temporarily and collected as a file. Neither the enhanced context/session policy nor the direct webpage fetch boundary covers these alternatives ([RT-RTE-legacy-query](#rt-rte-legacy-query), [RT-RTE-host-fallback](#rt-rte-host-fallback)).
- **Full mining outside the web gate.** The web route requires `confirm=true` for full mode and rejects a reported concurrent run; CLI `mine run --full` has its own driver without that confirmation. The web check occurs before executor scheduling, while the running flag is set in the runner. It is not an atomic cross-process admission lock. Per-document mining uses a different process-local lock and three stages, not global topics/wiki ([RT-RTE-mining-run](#rt-rte-mining-run)).
- **Update verification exceptions.** Binary installation rejects a mismatching valid checksum but accepts missing/invalid expected checksums. Python installation invokes pip on a remotely selected wheel without this checksum function. Windows binary replacement writes a pending marker; Unix performs two moves with attempted recovery. This defeats a universal authenticated/atomic-update claim ([RT-RTE-product-update](#rt-rte-product-update)).

These are inspected branch/control cases, not runtime experiments. Provider-native behavior, external callbacks, real concurrent requests, host permissions, deployment isolation and actual recovery results remain unobserved. The bounded dispatcher search below does not exclude arbitrary changes introduced by newly installed code.

### Controls, change admission and guarantee envelope

The capability surface includes local input/output files, SQLite/Chroma state, content/model network requests, configurable providers/endpoints, background threads, web serving, archives/cloud uploads and installing replacement code. The actual grant set—credentials, filesystem access, network policy and host tools—is not supplied. The default web bind is loopback, but an operator can override it. No deployed isolation envelope can be inferred from that default or from CORS configuration (SRC-1 `kb/commands/manage.py`, `kb/web/app.py`, `kb/config-template.yaml`).

| Scoped guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths / external contract | Conclusion statuses |
|---|---|---|---|---|
| Full web mining requires an explicit confirmation field | FastAPI mining handler, before scheduling | invariant for handler calls satisfying its branch; this is caller acknowledgement, not authenticated human approval | CLI and direct runner calls do not pass this check; deployed access control is external/unestablished | implementation conclusion status: wired; operation conclusion status: uninspected |
| Search indexing failure need not abort collection | Index helper and collection driver's catch | best effort; inspected file-admission path | metadata/file errors outside that catch can still fail; other collectors and installations require their own path checks | implementation conclusion status: wired; operation conclusion status: uninspected |
| Answer generation degrades to document titles on model failure | Enhanced pipeline `_generate_answer` | best effort for its model generation block | retrieval/construction failures can propagate; legacy RAG has separate degradation; depends on usable retrieved context | implementation conclusion status: wired; operation conclusion status: uninspected |
| Binary checksum mismatch blocks replacement when a valid expected hash is supplied | `verify_checksum`, called by binary updater | invariant for equality comparison, not authenticity of the hash | missing hash bypasses checking; Python wheel path bypasses this function; trust in release metadata, transport and pip remains external | implementation conclusion status: wired; operation conclusion status: uninspected |
| Single mining progress record describes a running job | Process-local runner state and locks | best effort observability, not a global exclusion invariant | check/schedule gap, CLI driver, per-document worker and multiple server processes lie outside a single atomic reservation | implementation conclusion status: wired; operation conclusion status: uninspected |

The inspectable guarantees above are bounded control mechanisms, not claims of answer truth, source completeness, synchronization, crash consistency or safe deployed authorization. Relevant support is retained in the route passages below. No universal guarantee was found or inferred from product naming.

Knowledge changes enter through collection, generated wiki admission and direct metadata editing. Configuration changes select provider/model/prompt behavior. Product changes enter through self-update and shipped installation scripts. Backups provide a retention/recovery route rather than validating any generated claim. These admission roles and recovery limits are in [RT-RTE-file-admission](#rt-rte-file-admission), [RT-RTE-wiki-compile](#rt-rte-wiki-compile), [RT-RTE-item-update](#rt-rte-item-update), [RT-RTE-settings-update](#rt-rte-settings-update), [RT-RTE-product-update](#rt-rte-product-update) and [RT-RTE-backup-restore](#rt-rte-backup-restore). Memory revision semantics belong to the memory member.

### Added inspection coverage and unresolved detail

Beyond the boundary's initial trace, this member inspected bounded implementations in SRC-1 `kb/collectors/file_collector.py`, `kb/collectors/base.py`, `kb/commands/utils.py`, `kb/processors/tag_extractor.py`, `kb/processors/embedder.py`, `kb/query/query_expander.py`, `kb/query/reranker.py`, `kb/query/context_builder.py`, `kb/query/conversation.py`, `kb/web/routes/settings.py`, `kb/commands/self_update.py`, `kb/self_update.py`, `kb/query/keyword_search.py` and the specific collection, retrieval, mining, wiki, backup and item branches cited below. Instruction evidence adds the restricted-URL fallback in `skills/localbrain-collect/SKILL.md`; prompt evidence adds `kb/query/prompt_templates.py` and wiki templates. These supply implementation or doctrine/design only, not new source identities or run evidence.

Remaining included detail is not absent: individual remote collectors/parsers, recommendation scoring, graph/topic algorithms, provider/library internals, all installer platform variants, restore destination handling, deletion/export cascades, frontend behavior and test quality have not been fully traced here. This prevents comprehensive security, data-consistency, quality and packaging claims. The minimum loops and counterpaths above can be established without those broader claims. In particular, archive extraction into `target_dir.parent` and archive member naming warrant further inspection before trusting the restore message as an isolated destination guarantee.

## Shared records

### Components

#### RT-CMP-litellm-provider
Label: Configured generative LLM through LiteLLMProvider and direct completion callers

Source-native identity: `LiteLLMProvider` is used by tag/entity extraction and wiki compilation; `RAGQuery` and `RetrievalPipeline` separately build completion arguments from configuration. Representational form: distributed-parametric model, interpreted through natural-language messages. Storage substrate: provider-side model weights and service state, not acquired; local objects retain model name, endpoint and credentials. Parameters are not updated by the inspected generation paths; provider-side changes are uninspected. Exact model version is not pinned by this source: configurable aliases such as `dashscope/qwen-plus` resolve through mutable services. A mutable endpoint may resolve to another model. This component identifies the configured generation service role, not proof that all calls use identical provider weights. SRC-1 `kb/processors/tag_extractor.py`, `kb/processors/entity_extractor.py`, `kb/processors/wiki_compiler.py`, `kb/query/rag.py`, `kb/query/retrieval_pipeline.py`, `kb/config-template.yaml`.

> response = litellm.completion(
>     model=self.model,
>     messages=[{"role": "user", "content": prompt}],
>     api_key=self.api_key,
>     num_retries=0,
>     **{**self.extra_kwargs, **kwargs}
> )
> return response.choices[0].message.content
> --- `kb/processors/tag_extractor.py`

The provider wrapper retries exceptions with backoff. That is transport-level recovery, not independent verification of returned content.

#### RT-CMP-query-expander
Label: LLMQueryExpander model-dependent selector input

Source-native identity: `LLMQueryExpander`. Representational form: distributed-parametric model interpreting text; returned rewrites/entities/intent become symbolic retrieval arguments and natural-language queries. Storage substrate: remote/configurable model service; local configuration and current invocation response. Parameters do not change in the inspected `expand`/completion route. Exact version is not pinned; configuration selects an alias/base URL and a mutable endpoint can serve another model. Provider internals remain uninspected. Separate from answer generation because its output changes what is retrieved. SRC-1 `kb/query/query_expander.py`, `kb/web/dependencies.py`.

> return ExpandedQuery(
>     original=question,
>     rewrites=expansion_data.get("rewrites", []),
>     entities=expansion_data.get("entities", []),
>     intent=expansion_data.get("intent"),
> )
> --- `kb/query/query_expander.py`

#### RT-CMP-llm-reranker
Label: LLMReranker relevance-scoring component

Source-native identity: `LLMReranker`. Representational form: distributed-parametric model followed by symbolic weighted-score sorting. Storage substrate: configured external model service and ephemeral score lists/chunk objects. No parameter training occurs in the inspected scoring path; external mutability is uninspected. Exact model version is not pinned and mutable configuration/endpoints may resolve to other models. This is a separate selection component, not an answer oracle. SRC-1 `kb/query/reranker.py`, `kb/web/dependencies.py`.

> final_score = (
>     self.weight_retrieval * chunk.retrieval_score
>     + self.weight_rerank * rerank_score
> )
> --- `kb/query/reranker.py`

Batch failure attempts individual scoring; failure there supplies neutral scores. Model judgment and these fallbacks do not demonstrate relevance quality.

#### RT-CMP-embedding-provider
Label: Embedder's configured embedding model

Source-native identity: `Embedder` with `LiteLLMEmbeddingProvider`, DashScope or OpenAI-compatible adapters. Representational form: distributed-parametric model producing dense numerical vectors. Storage substrate: model weights behind provider endpoints; derived vectors enter Chroma for chunk search and document embeddings enter SQLite through `DocEmbeddingService`. Model parameters are not updated by inspected embedding calls. Exact model version is not pinned by configuration aliases. A mutable endpoint can resolve to another model; inaccessible provider internals remain uninspected. Persisted derived vectors are not evidence of trained model weights. SRC-1 `kb/processors/embedder.py`, `kb/processors/doc_embedding.py`, `kb/commands/utils.py`, `kb/config-template.yaml`.

> call_kwargs = {
>     "model": self.model,
>     "input": texts,
>     "api_key": self.api_key,
>     **self.extra_kwargs,
>     **kwargs,
> }
> if self.api_base:
>     call_kwargs["api_base"] = self.api_base
> --- `kb/processors/embedder.py`

### Operative objects

#### RT-OBJ-config
Label: Local Brain configuration and provider selection

Source-native identity: `config.yaml` loaded through `Config`, with CLI `CONFIG_FILE` under `~/.localbrain`. Representational form: symbolic YAML fields for paths, providers, model names, budgets and scheduling; natural-language prompt strings are a separate consumed part. Storage substrate: local YAML file plus process-local cached configuration/component instances. SRC-1 `kb/config.py`, `kb/config-template.yaml`, `kb/commands/utils.py`, `kb/web/routes/settings.py`, `kb/web/dependencies.py`. A config save can change future construction without replacing an already cached pipeline; see [RT-RTE-settings-update](#rt-rte-settings-update).

#### RT-OBJ-prompt-templates
Label: RAG and wiki task guidance

Source-native identity: `BUILTIN_TEMPLATES`, configured custom templates and `WikiCompiler` prompt templates. Representational form: natural-language instructions with symbolic formatting variables. Storage substrate: shipped Python strings or configuration, rendered into transient model messages. SRC-1 `kb/query/prompt_templates.py`, `kb/processors/wiki_compiler.py`, `kb/query/retrieval_pipeline.py`. They direct citation, contextual answering and synthesis; they are not validators or an expected-answer reference.

> "If the context doesn't contain enough information, say so honestly. "
> "Always cite your sources using [Source N] notation when referencing specific information.\n\n"
> --- `kb/query/prompt_templates.py`

### Routes

#### RT-RTE-file-admission
Label: File collection and automatic metadata/index admission

Endpoints and progression: CLI `file_add` → `FileCollector.collect` → Markdown write → optional smart extraction/frontmatter write → SQLite knowledge/tags → chunk embedding/Chroma → SQLite chunks. Owner: application driver under the caller's OS principal. Context: source path, supplied title/tags/summary, extracted file text and configuration. Identities: source path, generated metadata item ID, saved file path, content hash and derived chunk IDs. Executor/effects: parser, model/built-in extractor, filesystem and storage APIs; no model-controlled shell dispatcher.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed success/title/word count/path/tags/summary or duplicate/failure; collector returns a CollectResult to the driver.
- Later read-back: Saved text/metadata/chunks can reach keyword, semantic and mining consumers on later calls.
- Delegated visibility: Configured extraction and embedding services receive document-derived text; external agent receives command output, not automatically the complete saved content.
- Selection predicate: Explicit source path and supported suffix; duplicate checking is conditional on skip_existing and supplied storage; user values override missing-field extraction.
- Invalidation or expiry: No cross-store atomic invalidation is established by this driver; later management/reindex operations are separate paths.
- Activation or effect: Python wires persistence and indexing; actual later retrieval and resulting behavior are unobserved.
- Evidence limits: Only the file branch and shared helper are traced end to end here; other collector-specific fetching/parsing is not asserted equivalent.

Admission roles/mode: open collection requests; caller supplies source and optional values or disables auto extraction. Model/built-in extraction proposes missing values; Python admits them without per-result approval. No independent answer oracle is used. Caller can stop/avoid the request or later edit/delete retained material; no coordinated rollback is implemented in the inspected sequence. Guidance is the extraction prompt and supplied metadata; admitted text, tags, summary and vectors persist. SRC-1 `kb/commands/collect.py`, `kb/collectors/file_collector.py`, `kb/collectors/base.py`, `kb/processors/tag_extractor.py`, `kb/commands/utils.py`.

> if result_tags and result_summary:
>     logger.info("Using user-provided tags and summary, skipping extraction.")
>     return {"tags": result_tags, "summary": result_summary}
> --- `kb/processors/tag_extractor.py`

> except Exception:
>     pass  # Indexing failure shouldn't break collection
> --- `kb/commands/collect.py:150-151`

> file_path = target_dir / filename
> file_path.write_text(full_content, encoding="utf-8")
> --- `kb/collectors/base.py`

#### RT-RTE-chat-query
Label: Enhanced web retrieval and conversation reuse

Endpoints/progression: `POST /api/rag/chat` → cached dependency construction → `RetrievalPipeline.run` → expansion/hybrid retrieval/reranking/enrichment/context/answer → attempted turn writes → JSON. Principal: HTTP caller; application owns all stage scheduling, while models propose rewrites, scores and answer text. Context/state: request options, selected stored material, reading history, session ID, recent turns and in-process result cache. Executor/effects: model and storage adapters; SQLite conversation persistence and reading-history background task. Decision roles: model relevance proposals plus software fusion/sorting/budget selection; caller chooses request and template/options, but does not approve each generated turn. Operating mode: open questions, not a curriculum or bounded improvement experiment. Answer oracle: none established; confidence is computed metadata, not comparison with a known answer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: EnhancedRAGResult JSON with answer, selected sources/context, confidence, strategy and session metadata; cached results and fallback document-title responses are alternatives.
- Later read-back: Successful turn writes reach later session prompts; reading events can reach later personalization; cache returns prior result objects during their process-local TTL.
- Delegated visibility: Provider receives question and selected/rendered context/history, not the entire knowledge store; no remote worker/delegated-agent route is established.
- Selection predicate: Semantic query variants with tags, optional entity-linked graph retrieval, keyword query plus entities, document-keyed RRF, weighted reranking, optional recent-view boost and budgeted context construction; graph and keyword branches do not establish universal tag filtering.
- Invalidation or expiry: Cache expires by monotonic TTL and mining invalidators clear it; history formatting limits recent turns and 4000 characters, not a demonstrated universal retention expiry.
- Activation or effect: Retained material is wired into model input and turn storage; compliance, exercised reuse and benefit remain unobserved.
- Evidence limits: Cache hits, empty retrieval and failed saves prevent a universal conversation-write claim; returned source records and model-delivered truncated content need not match in extent.

Persistence admission: application accepts question and generated answer as conversation turns without a per-turn approval gate; logging failure does not veto returning an answer. Recovery: history-read/save failures are logged, unavailable components degrade, generation failure returns titles, outer execution errors propagate to HTTP error handling. SRC-1 `kb/web/routes/search.py`, `kb/web/dependencies.py`, `kb/query/retrieval_pipeline.py`, `kb/query/context_builder.py`, `kb/query/conversation.py`, `kb/query/reranker.py`, `kb/query/query_expander.py`.

> use_cache = not session_id and not conversation_context
> cache_key = ""
> if use_cache:
>     tags_key = tuple(sorted(tags)) if tags else ()
>     cache_key = f"pipeline:{question}:{tags_key}:{effective_top_k}"
> --- `kb/query/retrieval_pipeline.py`

The cache key also omits options, so a cached single-turn result does not demonstrate that a newly requested temperature/template/personalization option was applied.

> except Exception as e:
>     logger.warning(f"Failed to save conversation turns: {e}")
> --- `kb/query/retrieval_pipeline.py`

#### RT-RTE-legacy-query
Label: Legacy semantic RAG and progressive fallback

Endpoints/progression: CLI search RAG and `POST /api/rag` → `RAGQuery.query_with_fallback` → semantic retrieval/context/answer, or semantic-only, keyword-only, or error-text result. Owner: application, using the configured generative/embedding components. Context/state: current question, tags/top-k and retained search material; no enhanced conversation-manager stage in this inspected route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RAGResult answer/source/context fields, including explicit unavailable-service or no-information responses.
- Later read-back: Existing retained knowledge is consumed; web handler optionally records the question as a reading-history event, not an enhanced session turn.
- Delegated visibility: Answer provider receives built context and question; fallback keyword subprocess sees search arguments and local data directory.
- Selection predicate: Semantic search receives tags and top-k; keyword fallback passes keywords and limit without tags.
- Invalidation or expiry: inapplicable — this route is not the enhanced pipeline result cache or conversation session mechanism.
- Activation or effect: Contextual generation or retrieval-only results are wired; actual quality and activation are unobserved.
- Evidence limits: A fallback result is not an AI-generated grounded answer; endpoint-level import/configuration/other errors can still produce HTTP errors despite the inner method's result-return design.

Operating mode: open questions; model proposes answer, software chooses fallback level. No independent answer oracle or per-answer approval is established. SRC-1 `kb/commands/search.py`, `kb/web/routes/search.py`, `kb/query/rag.py`, `kb/query/keyword_search.py`.

> kw_search = KeywordSearch(data_dir=str(self.config.data_dir))
> search_results = kw_search.search(keywords=question, limit=effective_top_k)
> --- `kb/query/rag.py`

#### RT-RTE-host-fallback
Label: Host-assisted restricted-page collection

Endpoints/progression: collection skill instructs host agent to try webpage admission, then use its browser/fetch capability, save temporary Markdown and invoke file admission; ask the user for content if automated methods fail. Owner/next step: external agent interpreting the skill, then Local Brain CLI. Context/state: user collection intent, external content and temporary file; application identities become file-admission identities rather than proof of original webpage lineage.

- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested command result or request for user-provided content.
- Later read-back: If executed, host-produced file content enters later knowledge consumers through file admission.
- Delegated visibility: Host tools may see the URL/content; their credentials, access and isolation are external and uninspected.
- Selection predicate: Direct webpage collection failed on a restricted URL and host browser/fetch capability is available.
- Invalidation or expiry: uninspected — temporary-file cleanup and host retention are not established by this instruction.
- Activation or effect: Instruction affords alternate admission, not observed host compliance or fetch success.
- Evidence limits: This is doctrine/design, not a Local Brain browser capability or runtime tool grant.

Admission roles/mode: open collection intent; host proposes/obtains text and invokes file write admission; user can supply content when asked. No independent oracle authenticates the fetched text in this instruction. Rollback follows separate application/host management, not the fallback procedure. SRC-1 `skills/localbrain-collect/SKILL.md`.

> 3. **Ask the user to provide the content**: If all automated methods fail, ask the user to paste the article text, then save it as a note or file.
> --- `skills/localbrain-collect/SKILL.md`

#### RT-RTE-mining-run
Label: Batch and per-document derived-state mining

Endpoints/progression: web mining route validates mode/workers/confirmation → executor thread → `run_mining` → entities, document embeddings, relations, topics, wiki → history/state finalization. CLI `mine_run` is an alternate driver with its own extraction thread pool and sequential SQLite saves. `mine_document_async` is a separate daemon-thread route for entities/embeddings/relations, not topic/wiki compilation. Owners: callers select mode/steps; application schedules models and transformations. State: knowledge IDs, files/summaries, process-local progress/locks, durable derived tables and JSONL history. Effects are staged writes, not one atomic rebuild.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Web returns started/run ID after scheduling, clients poll progress/history; runner returns completed/partial/failed summary; CLI prints per-stage results; per-document scheduling returns without results.
- Later read-back: Derived entities/vectors/relations/topics reach graph/retrieval/wiki consumers; JSONL history reaches the history endpoint.
- Delegated visibility: Model providers receive extraction/synthesis content; thread workers are local execution, not separate agent identities or sandbox boundaries.
- Selection predicate: Caller mode/selected steps, runner knowledge inventory and stage-specific incremental/full rules; CLI extraction reads up to 3000 characters of available files with summary/title fallback.
- Invalidation or expiry: Batch runner and per-document worker attempt graph/pipeline cache invalidation; these do not establish universal cache coherence across CLI, processes or every writer.
- Activation or effect: Software wires derived-state persistence and subsequent consumers; no supplied runs demonstrate activation or improved retrieval.
- Evidence limits: Per-document implementation presence does not establish invocation on every collection; per-stage skipping/failure and alternate drivers prevent an all-stages-success interpretation.

Admission roles/mode: maintenance over retained documents, incremental or full mode rather than an improvement experiment. Models propose entities/wiki content; software admits stage results. Web full confirmation is a caller flag, not per-content human veto. CLI flags can skip stages. There is no independent answer oracle. Stage failure reporting and rerunning are recovery mechanisms; no batch-wide rollback is established. Guidance consists of shipped extraction/synthesis prompts and algorithm/configuration settings; derived state persists, not proof that method guidance was revised. SRC-1 `kb/web/routes/mining.py`, `kb/processors/mining_runner.py`, `kb/processors/mining_worker.py`, `kb/commands/mine.py`.

> if request.mode == "full" and not request.confirm:
>     raise HTTPException(
>         status_code=422,
>         detail="Full rebuild requires confirm=true. This will clear and rebuild all mining data.",
>     )
> --- `kb/web/routes/mining.py`

> if full:
>     result = builder.rebuild_all_relations()
> --- `kb/commands/mine.py`

#### RT-RTE-wiki-compile
Label: Durable wiki synthesis and later article browsing

Endpoints/progression: wiki CLI/mining calls `WikiCompiler.compile_all`; selected topic/category calls `compile_topic`, filters source documents, builds/truncates prompt, generates/parses text, renders Markdown, writes file, saves SQLite article metadata; later wiki HTTP route looks up article ID and reloads the file with related source/entity metadata. Owner: application compiler; model proposes title/sections/references, Python admits the parsed/rendered result. Context/state: topics/categories, source documents and entities, configured provider, article ID/slug/path and source IDs.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Article metadata/compilation summary; later GET returns stored Markdown plus source_documents/entity_details or an HTTP error.
- Later read-back: Wiki consumer reads previously written article files; compilation also reads existing category/article state to select future work.
- Delegated visibility: Provider receives bounded document content and at most the prompt-selected entities, not all retained source text.
- Selection predicate: Topic/category and compiler eligibility rules; compile_topic falls back to all source_docs if category filtering produces no matches; prompt token approximation may omit/truncate selected sources.
- Invalidation or expiry: Recompilation uses compiler category/staleness/force mechanisms; exact invalidation coverage across all edits/deletions is not established here.
- Activation or effect: Durable synthesis and later browsing are wired; factual correctness, faithful contradiction handling and successful reuse are unobserved.
- Evidence limits: source_doc_ids are built from filtered_docs even where prompt-budget construction omitted material; source linkage is not proof of complete model consumption or statement-level evidence.

Admission roles/mode: maintenance synthesis over retained content. Model proposes text and organizational subcategories; software parses and writes without a per-article human approval gate in the inspected compile path. Caller can withhold/reinvoke compilation; no article-wide file/database transaction or content-validation oracle is established. Guidance requests standalone articles and notation of contradictions. What persists is article text and metadata, not a demonstrated criticism/revision of the compiler's method. Generated articles may contain theories, but no particular formulated-theory builder loop is established from unknown model output; that uncertainty does not imply absent theories. SRC-1 `kb/processors/wiki_compiler.py`, `kb/web/routes/wiki.py`, `kb/commands/wiki.py`.

> 3. When sources provide complementary information, merge them naturally
> 4. When sources contradict, note both perspectives
> 5. Reference related entities using [[entity-slug]] wiki-link syntax
> --- `kb/processors/wiki_compiler.py`

> file_path.parent.mkdir(parents=True, exist_ok=True)
> file_path.write_text(markdown, encoding="utf-8")
> --- `kb/processors/wiki_compiler.py:567-568`

#### RT-RTE-item-update
Label: Direct HTTP metadata editing

Endpoints/progression: item-update handler loads item ID, rejects nonexistent item, writes supplied title/summary/user_notes and adds supplied tags, then returns reloaded metadata. Owner/principal: HTTP caller requests values; application writes SQLite. Context/state: existing knowledge row and ItemUpdate values. These writes differ from model-generated extraction and do not prove edits reached Markdown/Chroma.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated knowledge row/tags or HTTP error.
- Later read-back: Stored metadata is available to later metadata/retrieval consumers; synchronization to other representations is unestablished.
- Delegated visibility: inapplicable — this handler does not delegate the edit to a model or worker.
- Selection predicate: Exact item ID and non-None requested fields.
- Invalidation or expiry: No Markdown rewrite, reembedding or pipeline-cache invalidation appears in the inspected handler.
- Activation or effect: SQLite writes are wired; downstream effect and consistency are unobserved.
- Evidence limits: Actual caller identity/human authorship is unresolved; adding tags is not replacing the prior tag set.

Admission roles/mode: direct caller-provided metadata; application rejects missing item or failed update, not semantic inadequacy. No model proposal, answer oracle or approval stage. Later editing/deletion is separate recovery; no rollback of the multi-field/tag sequence is established. SRC-1 `kb/web/routes/items.py`.

> current_tags = storage.get_tags(item_id)
> for tag in current_tags:
>     # We need to manually remove tags (there's no direct method)
>     # For now, we'll just add the new tags
>     pass
> --- `kb/web/routes/items.py`

#### RT-RTE-settings-update
Label: Provider configuration admission

Endpoints/progression: web LLM/embedding settings handlers transform UI provider/model fields, preserve masked keys, save raw YAML and clear cached Config. Application admits caller-supplied settings; models do not propose them. Context/state: current config, supplied model/key/base URL and cached application dependencies. Executor/effects: local YAML write and config-cache clearing.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: UI-format settings with masked key and success/error response.
- Later read-back: Future Config loads and component construction can consume changed provider settings.
- Delegated visibility: New endpoints may receive future model text/embedding requests; this write does not itself establish a provider call.
- Selection predicate: Requested provider/model values and key masking/preservation rules.
- Invalidation or expiry: Handlers clear get_config cache; already constructed singleton pipeline/other components are not reset in these inspected update blocks.
- Activation or effect: YAML admission is wired; immediate change of a running cached component is not established.
- Evidence limits: Credentials, deployed grants, provider availability and actual newly selected weights remain unobserved.

Admission roles/mode: open configuration edits; caller selects values and application writes them after syntactic/provider handling. Human identity and per-content approval are unresolved. No expected-answer oracle or quality-based successor selection. Restore/edit config and restart/reconstruction are potential recovery actions, not demonstrated automatic rollback. SRC-1 `kb/web/routes/settings.py`, `kb/web/dependencies.py`, `kb/config.py`.

> raw["llm"] = llm_config
> _save_raw_config(raw)
> --- `kb/web/routes/settings.py`

#### RT-RTE-product-update
Label: Operator-triggered binary or Python package replacement

Endpoints/progression: `self-update` reads update server/current version → forced latest update unless check/rollback selected → install-type dispatch → fetch release metadata → pip wheel install or binary download/hash check/replacement → install-info write. Owner: caller initiates; release server supplies successor/version/platform path; application installs. Context/state: installation type/path, version metadata, platform, remote wheel/binary and local previous binary.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed success/failure and exit status; --check reports metadata without installation; Windows may report pending update.
- Later read-back: Later processes can run installed replacement code; install metadata is retained locally.
- Delegated visibility: Update server and pip receive URLs/network requests; subprocess installation executes external package machinery under existing OS permissions.
- Selection predicate: Latest release metadata and platform/install type; CLI force=True permits same-version replacement, not quality comparison.
- Invalidation or expiry: Unix preserves one .old binary and overwrites prior backup; Windows writes a pending marker; Python package update has no equivalent package rollback in this inspected route.
- Activation or effect: Installation/replacement machinery is wired; loading and exercising changed code is unobserved.
- Evidence limits: Remote artifacts and server authenticity are not acquired; optional checksum equality is not authenticated provenance; a pending marker is not completed replacement.

Admission roles/mode: operator-triggered maintenance, not evidence-responsive self-improvement. Release machinery proposes code; application accepts installation-type/platform-compatible successor subject to transport/hash/install success. Binary mismatch can reject; missing hash passes. Unix replacement failure attempts to move backup back; explicit rollback swaps available binaries. Python rollback coverage is not established. No answer oracle, evaluation curriculum or objective-based improvement comparison. Guidance consists of release metadata/configuration; package/code and install-info persist. SRC-1 `kb/commands/self_update.py`, `kb/self_update.py`.

> if not expected or not expected.startswith("sha256:"):
>     logger.warning("No valid checksum provided, skipping verification")
>     return True
> --- `kb/self_update.py`

> result = subprocess.run(
>     [str(pip_path), "install", "--upgrade", wheel_url],
>     capture_output=True,
>     text=True,
> )
> --- `kb/self_update.py`

#### RT-RTE-backup-restore
Label: Archive retention and manual restore admission

Endpoints/progression: CLI/web/scheduler initiate backup task → background archive walk → optional cloud upload → metadata completion; CLI restore selects stored backup ID/local path → extracts archive → prints manual replacement instructions. Owner: caller or configured schedule, application archive code; operator remains responsible for the advised service stop and move. Context/state: backup metadata/task IDs, archive members and local target argument.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Task/status/backup metadata or restore messages; cloud-only restore reports not implemented when no local file exists.
- Later read-back: Metadata supports backup listings and later archive selection; restored material reaches application consumers only after actual placement/configuration.
- Delegated visibility: Optional OSS/S3 upload exposes archive bytes to configured external storage; success is unobserved.
- Selection predicate: Backup directory walk excluding backups; restore chooses exact backup ID and requires local file and nonexisting requested target.
- Invalidation or expiry: Automatic backup retention cleanup is configured; live-store/cache invalidation after manual placement is not established.
- Activation or effect: Archive writes/extraction are wired; restart reconstruction, coordinated snapshots and successful isolated restoration are unobserved.
- Evidence limits: Backup can skip unreadable files; extraction goes to target_dir.parent using archive member names, not proven target isolation or full consistency.

Admission roles/mode: retention/recovery maintenance; archive content is mechanically selected, not model proposed. Caller can choose backup/target and decline manual adoption. Rejection covers missing local backup/existing target and raised exceptions, not semantic correctness. No independent oracle verifies restored state; backup completeness and rollback remain unobserved. SRC-1 `kb/commands/backup.py`, `kb/scheduler/backup_scheduler.py`, `kb/web/routes/backup.py`.

> with zipfile.ZipFile(backup_file, "r") as zipf:
>     zipf.extractall(target_dir.parent)
> --- `kb/commands/backup.py`

### Claims

#### RT-CLM-context-answer
Label: Contextual answering with citation instructions

Claimed operation: built-in general RAG template requests answers based on the personal KB context, honesty when insufficient, and `[Source N]` citations. Its source is SRC-1 `kb/query/prompt_templates.py`; the minimum passage is retained in [RT-OBJ-prompt-templates](#rt-obj-prompt-templates). This is doctrine/design delivered by [RT-RTE-chat-query](#rt-rte-chat-query), not enforcement of factual correctness, citation validity or complete source consumption. Different templates and legacy RAG are separate guidance paths.

### Evidenced absences

#### RT-ABS-tool-dispatch
Label: No application model-tool dispatcher in the inspected retrieval/mining roots

- implementation conclusion status: absent

Searched roots/files: SRC-1 `kb/query/`, `kb/processors/`, `kb/web/app.py`, `kb/web/routes/search.py`, `kb/web/routes/mining.py` at the reviewed revision. Query: `tools|tool_calls|exec\(|eval\(|subprocess|importlib|fine.?tun|backward\(|optimizer`, followed by inspection of completion construction and keyword subprocess handling. Additional query `train|fit\(|fine.?tun|backward\(|optimizer|tool_calls|tools=` found prose uses of constraints but no training/dispatcher implementation in those roots. The inspected generative calls supply messages and return message content; the actual subprocess witness is fixed ripgrep search, not execution of model-returned tool calls.

> result = subprocess.run(
>     cmd,
>     capture_output=True,
>     text=True,
>     timeout=30,
> )
> --- `kb/query/keyword_search.py`

This supports the bounded absence of a model-tool execution loop in these inspected application paths. It does not establish absence of shell capability elsewhere: web launch and package update have explicit subprocesses; the host-assisted skill supplies external tools; provider/library internals and installed successors are outside this absence boundary. It also does not establish absent learning through retained text or vectors.

### Behavioral-authority paths

#### RT-BAP-template-guidance
Label: Prompt guidance enters answer generation

Consumer: configured answer model. Channel: rendered user prompt with template instructions, selected context and history, or fallback system/user prompt construction. Force: natural-language request interpreted by model, not a software invariant or guaranteed compliance. Horizon: every noncached applicable generation invocation using the current constructed prompt manager/configuration. Evidence: SRC-1 `kb/query/retrieval_pipeline.py`, `kb/query/prompt_templates.py`; [RT-RTE-chat-query](#rt-rte-chat-query) and [RT-OBJ-prompt-templates](#rt-obj-prompt-templates).

> user_prompt = self.prompt_template_manager.render(
>     template_name=effective_template,
>     context=context_text,
>     question=question,
>     conversation_history=conversation_history or "",
>     entity_context=entity_context_str,
>     topic_context=context.topic_context or "",
> )
> --- `kb/query/retrieval_pipeline.py`

#### RT-BAP-config-selection
Label: Configuration selects model and pipeline controls

Consumer: Config readers and application component constructors. Channel: YAML/provider/model/base-URL/budget fields into symbolic argument construction. Force: software selection of adapter/endpoint and stage controls; service's actual resolved weights remain external. Horizon: later configuration loads/component construction; existing singleton instances can delay application of an edit. Evidence: SRC-1 `kb/web/dependencies.py`, `kb/web/routes/settings.py`, `kb/query/query_expander.py`, `kb/query/retrieval_pipeline.py`; [RT-RTE-settings-update](#rt-rte-settings-update).

## Annotations

none
