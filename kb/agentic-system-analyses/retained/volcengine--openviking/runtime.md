---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OpenViking runtime baseline: scoped retrieval, context assembly, durable session processing and conditional skill/config admission at the frozen revision."
run-id: AAS-2026-10-14-openviking-7b5b57541af5-01
reviewed-boundary: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
---

# OpenViking runtime report

## Runtime account

### Work and evidence boundary

OpenViking returns stored agent context and performs model-dependent processing of session traces. It is not, on the inspected database paths, the enclosing agent that answers the user's task. The frozen boundary includes shipped consumers, but remains a complete artifact with partial loop coverage. All findings below use SRC-1 implementation or attributed design text at the boundary revision. No target code, tests, examples, providers or services were executed. Activation, reliable recovery, production isolation and benefit remain unobserved.

The shipped command surfaces are `ov`, `openviking`, `openviking-server`, `openviking-gateway` and `vikingbot` (SRC-1, `pyproject.toml`). The boundary already identifies startup assembly. This report adds inspection of the HTTP search router, VikingFS semantic/access mixins, retriever and vector scope construction, context assembler, account model/config providers, session archive/recovery, extraction loop and selected skill admission, plus the OpenCode recall adapter and shared recall selection. These newly inspected paths are part of SRC-1, not new sources.

The ordinary invocation traced here is HTTP list-mode search with a session. Context-mode search is a materially different pipeline, not just another serialization of that search. Session commit is a separate asynchronous production loop. The records below identify these distinctions rather than treating the advertised filesystem abstraction as a uniform executor.

### Ordinary invocation: session-aware list search

An HTTP caller supplies query, optional session ID, target, filters, count/threshold, levels and optional content-read/provenance flags. The search router resolves identity through the active authentication plugin into a RequestContext carrying account/user, role, groups and optional actor-peer view (SRC-1, `openviking/server/auth/__init__.py`; `openviking/server/routers/search.py`). This is caller identity, not proof a human supplied or approved the request. The router owns the next step and, when intent is enabled, loads the requested session.

SearchService collects search context only for a session with intent enabled and no resolved image. VikingFS starts with a raw-query plan, checks target scope and optionally reads a target abstract. If a summary or messages exist, it resolves the account query planner and calls IntentAnalyzer under the configured timeout. The model sees a truncated compression summary, at most five recent messages, current query, optional category constraint and target abstract. Its natural-language judgment is parsed into symbolic TypedQueries. Invalid categories fall back to resource; non-dictionary entries are skipped. Code resets target directories after planning and constrains categories to the caller's requested types. The model proposes queries; code controls scope and dispatch. See [RT-RTE-session-search](#rt-rte-session-search), [RT-CMP-query-planner](#rt-cmp-query-planner) and [RT-OBJ-query-plan](#rt-obj-query-plan).

The retriever executes a global vector search per TypedQuery, not a recursively descending directory walk in the inspected implementation. It embeds each semantic query, uses the account-bound vector proxy and scope filter, deduplicates candidate URIs, optionally reranks their abstracts, applies threshold and count, then converts records into MatchedContexts. The default retriever mode is THINKING when a reranker is available, otherwise QUICK. Keyword retrieval is another dispatch branch; image queries use multimodal input, default to level 2 and avoid reranking. Concurrent query results are collected into memory/resource/skill buckets. The router optionally reads bodies, converts to dictionaries, sanitizes floats and returns a status/result/telemetry envelope (SRC-1, `openviking/storage/viking_fs/_semantic.py`; `openviking/retrieve/hierarchical_retriever.py`; `openviking/storage/viking_vector_index_backend.py`; `openviking/server/routers/search.py`).

Terminal output is selected context, not a task answer. Semantic relevance is model/vector judgment, not an answer oracle. List search itself does not admit new knowledge. Session content supplied to planning can include retained archive overview; delivery to an enclosing agent and its behavioral use are separate steps.

### Material alternates and forcing cases

Four forcing cases were inspected to challenge uniform claims:

1. **No planner, failed planner, or image query.** Disabled intent and absent session context retain the raw query; image search bypasses text intent. Exceptions/timeouts inside intent analysis fall back to raw query. This is not a universal availability guarantee: embedding, backend search and result gathering can still fail. A successfully parsed empty query list also replaces the raw query with no planned queries. See [RT-RTE-session-search](#rt-rte-session-search).
2. **Direct find and filter-only lookup.** Find uses QUICK retrieval without session planning or model reranking. An empty text query with a filter goes through a metadata-only path with score zero and no similarity ranking. It shares scope-filter construction with vector and keyword retrieval, rather than inventing a second tenant filter. See [RT-RTE-direct-find](#rt-rte-direct-find).
3. **Context assembly and downstream omission.** Context mode gathers per-category or flat candidates, excludes cooled/request-excluded URIs, reads selected bodies, degrades detail under a token estimate and can rewrite them. A `no_relevant` rewrite blanks rendered content and prevents cooling those entries, although entries remain in the response. The shared client selector also returns nothing for that status and otherwise prefers digest over rendered text. Thus a hit or response entry is not equivalent to host-visible recall. See [RT-RTE-context-assembly](#rt-rte-context-assembly), [RT-RTE-plugin-recall](#rt-rte-plugin-recall).
4. **Durable commit and terminal failures.** Commit publishes a task acceptance after archive preparation/enqueue, not after extraction completes. Resume checks done/failed/ready markers and archive ordering; malformed or empty archived messages can terminate as failure. This challenges both the claim that commit is merely an in-process background task and the stronger claim that acceptance means memory extraction succeeded. See [RT-RTE-session-commit](#rt-rte-session-commit).

### Controls and guarantee boundaries

**Scope control.** The owner is VikingFS plus the vector-index backend. Enforcement consists of required request context for semantic search/find, URI checks, target scope checks, caller-scope restoration after planning, and `_build_scope_filter` for semantic, keyword and metadata lookup. Strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. The external contract is that configured backends enforce supplied filter expressions and account backend selection. ROOT has a distinct filter path; bypass ACL still retains an account equality predicate. Consequently this report establishes scoped query construction, not a deployment-wide noninterference invariant. The currently deployed grant set, effective auth mode, groups and ACL contents are uninspected. See [RT-CLM-scoped-retrieval](#rt-clm-scoped-retrieval).

**Optional model degradation.** Owner: semantic search and retriever. Intent exceptions/timeouts preserve a raw query; rerank exceptions, empty results or wrong-length scores preserve vector scores. Strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. Coverage is the local optional model stages, not every provider/backend failure, empty valid plan or application path. External contracts are model-response interfaces and functioning embedding/storage. See [RT-RTE-session-search](#rt-rte-session-search).

**Restart-oriented session processing.** Owner: Session/QueueFS and archive/tracker machinery. Phase-one exact filesystem lock, persistent intent/archive, queue item, root publication and ready marker establish the inspected protocol. Resume distinguishes terminal done/failed markers from runnable work. Strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. It requires backend durability/lock semantics and queue-worker servicing. Crash/retry behavior, complete phase-two idempotence and exactly-once effects are not established by these reads. See [RT-RTE-session-commit](#rt-rte-session-commit).

**Admission is not universal approval or atomicity.** Extraction asks a model for operations; software submits them to an updater. Conditional session-skill work routes through a model-dependent patch plan and SkillPolicyUpdater. Starting commit or enabling extraction is not per-item human approval. A provider instruction calls for a “single atomic plan,” but this is an instruction, not an observed transaction guarantee. SkillPolicyUpdater catches individual deletion errors and returns written/deleted URIs and errors; restoring the old in-memory policy snapshot on error is not proof persisted writes were rolled back. See [RT-RTE-skill-admission](#rt-rte-skill-admission).

The capability surface includes database read/write APIs and model-driven extraction tools. The inspected ExtractLoop advertises only a context-provider-selected subset of MEMORY_TOOLS_REGISTRY, executes provider callbacks and requests final operations. Python-shaped output is a separate restricted DSL path, not ordinary shell execution; its security implementation is only partly inspected. No inference of a fixed three-iteration invariant is warranted: the run loop can extend its limit for tools/refetch/repair (SRC-1, `openviking/session/memory/extract_loop.py`; `openviking/session/memory/extraction_output_protocol/python_protocol.py`). Host tool grants, direct filesystem access, provider-native behavior, subprocess isolation, remote workers and arbitrary extensions were not exhaustively traced. Local-dev authentication explicitly returns ROOT without credentials; its validation requires a localhost host. That is a configuration policy, not an established network isolation envelope (SRC-1, `openviking/server/auth/plugins/dev.py`).

### Change admission and remaining coverage

Retained-knowledge change enters through commit-driven extraction; conditional session skills also admit reusable instruction content. Runtime config accepts validated/persisted patches and publishes change notifications that retire/reselect model resources. See [RT-RTE-session-commit](#rt-rte-session-commit), [RT-RTE-skill-admission](#rt-rte-skill-admission), [RT-RTE-config-patch](#rt-rte-config-patch). The model proxies do not imply immutable deployed models or local weight training. “Semantic gradients” in the inspected optimizer are inputs to text/operation patch planning, not evidence of numerical weight optimization.

ResourceService additionally exposes durable resource jobs with task tracking, enqueue and lock handoff; selected source-preparation and execution paths were inspected, but parsing, privacy, semantic/index maintenance, watch refresh and full admission were not traced end to end (SRC-1, `openviking/service/resource_service.py`). Manual skill upload/update, account extraction templates, extraction output JSON/Python equivalence, memory-updater conflict resolution, training/experience criticism, resource deletion maintenance, direct extraction and native storage internals remain unresolved included mechanisms. Their limits prevent a claim of uniform admission, atomicity or memory lifecycle coverage. Memory revisions are left to the memory analyst rather than inferred from the runtime submission point.

Gateway internals, bot execution/persistence, other plugins, native/Rust CLI semantics, evaluator internals and product/build admission remain incompletely inspected as already allowed by the partial-loop boundary. Available but uninspected evidence is not absence. Repository/product change control and provider-side weight changes are not established. The shipped OpenCode adapter demonstrates a source-wired consumption path; it does not establish how every host handles context or optional callbacks. No learning, autonomous theory-building or exercised self-improvement result follows from the presence of these routes.

## Shared records

### Components

#### RT-CMP-query-planner
Label: Account query planner

Source-native identity: account-resolved VLMHandle from `get_query_planner`; a dedicated account planner, account VLM, cluster planner or cluster VLM can be selected. Representational form: distributed-parametric model computation; the handle/config is a symbolic selector, not the weights. Substrate: external configured provider/service or model implementation, with process-local cached resources. SRC-1, `openviking/config/vlm.py`; `openviking/retrieve/intent_analyzer.py`.

Parameter mutation during operation: uninspected in provider internals; the inspected client calls inference, not weight-update methods. Exact weight/version pin: not established by a configured model string. Mutable endpoint can resolve to another model: provider-side resolution is uninspected; locally, config invalidation can reselect resources behind a long-lived handle.

> """Long-lived Account proxy; every model call uses the current resource."""
> --- `openviking/config/vlm.py`

#### RT-CMP-account-vlm
Label: Account extraction VLM

Source-native identity: account VLM resolved by SessionCompressorV3 and PatchMergePolicyOptimizer. Representational form: distributed-parametric. Substrate: configured provider/model implementation behind AccountBoundVLM, not repository-stored weights. SRC-1, `openviking/session/compressor_v3.py`; `openviking/session/train/components/policy_optimizer.py`; `openviking/config/vlm.py`.

Parameter mutation: provider internals uninspected; inspected extraction uses completion calls. Exact version pin: not established. Mutable endpoint resolution: uninspected externally; config changes can replace local resources. Distinct role from the planner, though the resolver can select the same underlying account VLM for both.

> vlm_config = await self.vlm_resolver.get_vlm(ctx.account_id)
> --- `openviking/session/compressor_v3.py`

#### RT-CMP-account-embedder
Label: Account embedding model

Source-native identity: AccountEmbeddingProvider/AccountBoundEmbedder. Representational form: distributed-parametric; output dense/sparse vectors are numerical representations distinct from the model. Substrate: configured embedder resource/provider, process-local cache and vector backend output. SRC-1, `openviking/config/embedding.py`; `openviking/retrieve/hierarchical_retriever.py`.

Parameter mutation: not established inside external models; inspected route embeds inputs. Exact version pin: not established by serialized config fingerprint. Mutable endpoint: external resolution uninspected; account config invalidation retires cached resources and newly resolved settings select an embedder.

> settings = await self._resolver.resolve(account_id)
> fingerprint = hashlib.sha256(
>     settings.embedding.model_dump_json().encode()
> ).hexdigest()
> --- `openviking/config/embedding.py`

#### RT-CMP-rerank-client
Label: Optional reranker

Source-native identity: RerankClient dispatched from rerank config. Representational form: distributed-parametric scoring model behind symbolic client/config. Substrate: configured external service/client resource. SRC-1, `openviking/models/rerank/__init__.py`; `openviking/models/rerank/volcengine_rerank.py`; `openviking/retrieve/hierarchical_retriever.py`.

Parameter mutation: provider internals uninspected; inspected method requests scores. Exact version pin: not established across configurable providers. The Volcano client accepts model name/version, but that does not establish immutable weights for all clients. Mutable endpoint can resolve differently: external resolution uninspected; config can select another provider/model. Reranking is disabled on QUICK and image routes.

> use_rerank = (
>     mode == RetrieverMode.THINKING and self._rerank_client is not None and not image_query
> )
> --- `openviking/retrieve/hierarchical_retriever.py`

### Operative objects

#### RT-OBJ-query-plan
Label: QueryPlan and TypedQueries

Source-native identity: transient QueryPlan returned by IntentAnalyzer and consumed by VikingFS.search. Representational form: symbolic query/category/priority fields, with natural-language query/intent/reasoning strings interpreted by models or readers. Substrate: process memory and optional serialized response; not a retained update in this route. SRC-1, `openviking/retrieve/intent_analyzer.py`; `openviking/storage/viking_fs/_semantic.py`.

> # Caller scope is authoritative even when the planner ignores its prompt.
> if context_types and len(context_types) == 1:
>     tq.context_type = context_types[0]
> --- `openviking/storage/viking_fs/_semantic.py`

#### RT-OBJ-session-commit
Label: Session commit archive and queue message

Source-native identity: SessionCommitMsg plus per-archive phase-one/terminal markers, `messages.jsonl` and session metadata. Representational form: symbolic task/policy/identity/phase metadata and natural-language message content; separate consumers use them as scheduling controls versus model input. Substrate: VikingFS/AGFS archive files and persistent QueueFS; task tracker stores progress. SRC-1, `openviking/session/session.py`.

> phase1_stage = "queue_enqueue"
> await get_queue_manager().enqueue(
>     QueueManager.SESSION_COMMIT,
>     queue_msg.to_dict(),
> )
> --- `openviking/session/session.py`

#### RT-OBJ-config-settings
Label: Cluster and account settings

Source-native identity: ConfigManager persisted scope settings and published effective candidates. Representational form: symbolic fields selecting model/provider and runtime behavior. Substrate: injected config source plus process-local copy-on-write publication; the source's concrete durability is not established here. SRC-1, `openviking/config/manager.py`.

> persisted_settings = await self._source.update(scope, mutate)
> if prepared is None:
>     raise RuntimeError("config source update did not invoke its mutate callback")
> --- `openviking/config/manager.py`

### Routes

#### RT-RTE-session-search
Label: Session-aware list search

Endpoints/progression/owner: HTTP search router → SearchService → VikingFS.search → optional IntentAnalyzer → concurrent HierarchicalRetriever calls → FindResult → HTTP envelope. Principal is RequestContext; account planner supplies query proposals, code controls scope and executor. Effects are retrieval/model calls, telemetry and return, not knowledge admission. SRC-1, `openviking/server/routers/search.py`; `openviking/service/search_service.py`; `openviking/storage/viking_fs/_semantic.py`; `openviking/retrieve/intent_analyzer.py`; `openviking/retrieve/hierarchical_retriever.py`.

- Immediate return: memory/resource/skill buckets, optional query plan/provenance/content and telemetry.
- Later read-back: optional stored archive overview and current session messages reach planning; this route does not write retained knowledge.
- Delegated visibility: planner receives truncated summary and recent-message slice; optional reranker receives query and candidate abstracts, not necessarily full bodies.
- Selection predicate: caller targets/filters/types/levels, optional model query expansion, vector or keyword scores, deduplication, optional rerank, threshold and limit.
- Invalidation or expiry: transient plan ends with invocation; stored/indexed content freshness and deletion propagation are uninspected here.
- Activation or effect: wired retrieval and response construction; host behavioral use is unobserved.
- Evidence limits: source inspection only; no proof of relevance, model compliance, latency or backend isolation in a deployment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: planner proposes; parser can reject malformed structure; code restores targets/categories and dispatches. No per-query human veto is part of these inspected stages. Answer oracle: inapplicable — relevance judgments are not a supplied expected answer. Operating mode: open caller request, with bounded context and configured timeout, not an experimental curriculum.

> except Exception as exc:
>     logger.warning(
>         "Intent analysis failed (%s); using original query: %s",
>         type(exc).__name__,
>         exc,
>     )
> --- `openviking/storage/viking_fs/_semantic.py`

A successful parsed plan can contain zero queries; the else branch replaces raw TypedQueries with `query_plan.queries`. The fallback therefore covers exceptions, not every unusable semantic proposal. Rerank failure separately returns fallback vector scores (SRC-1, `openviking/retrieve/hierarchical_retriever.py`).

#### RT-RTE-direct-find
Label: Direct and metadata-only find

Endpoints/progression/owner: HTTP find or direct SearchService.find → VikingFS.find → QUICK retriever, or `_find_by_filter` → account-bound metadata filter → FindResult. Code owns progression; no session planner. SRC-1, `openviking/service/search_service.py`; `openviking/storage/viking_fs/_semantic.py`; `openviking/storage/viking_vector_index_backend.py`.

- Immediate return: typed hit buckets; filter-only records have no similarity ranking and score zero.
- Later read-back: existing indexed context is selected; no new retained write is performed.
- Delegated visibility: semantic query reaches embedder; filter-only path needs no query embedding; returned preview/body access is caller-controlled.
- Selection predicate: caller query/image or mandatory filter; scoped metadata/URI/level predicates, count and semantic threshold where applicable.
- Invalidation or expiry: inapplicable — no new durable artifact is admitted; backend/index freshness is a separate unresolved mechanism.
- Activation or effect: scoped retrieval result construction is wired; downstream use unobserved.
- Evidence limits: exact-match lookup and semantic retrieval are materially different; backend filter enforcement is not execution-tested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = await retriever.retrieve(
>     typed_query,
>     ctx=real_ctx,
>     limit=limit,
>     mode=RetrieverMode.QUICK,
> --- `openviking/storage/viking_fs/_semantic.py`

#### RT-RTE-context-assembly
Label: Injection-ready context assembly

Endpoints/progression/owner: HTTP context-mode search or deprecated recall → assemble_context → optional expansion → gather → detail budgeting/body reads → render → optional rewrite → ledger record → entries/rendered/digest/stats. RequestContext and optional session coordinate account/peer scope and cooling. Code owns assembly; account planner proposes expansion/rewrite, not backend permissions. SRC-1, `openviking/server/routers/search.py`; `openviking/retrieve/context_assembler/pipeline.py`; `openviking/retrieve/context_assembler/gather.py`.

- Immediate return: budgeted entries, rendered context, optional digest and stats, including partial gather errors and rewrite status.
- Later read-back: session context can influence expansion; the session recall ledger cools served URIs across turns. Full ledger durability/expiry internals are uninspected.
- Delegated visibility: rewrite sees rendered selected entries, not the entire store; it can further omit information before host delivery.
- Selection predicate: quotas/purpose, query expansion, score thresholds, peer penalties, request exclusions, cooled URIs and detail/token planning.
- Invalidation or expiry: cooling is parameterized by dedup_turns; exact persisted ledger cleanup is uninspected. Input changes are selected afresh per request.
- Activation or effect: returned context and ledger record wiring; actual host injection and changed behavior require separate evidence.
- Evidence limits: token budgeting is an implementation plan, not established compliance with every provider tokenizer/window; rewrite correctness and relevance remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: caller sets controls; model proposes expansion/digest; code budgets and records only served entries. Answer oracle: inapplicable — no expected-answer reference is supplied. Operating mode: open query-driven recall. Recoverable scope failures become stats; InvalidArgumentError propagates. Context is not a guaranteed complete rendition of hits.

> if rewrite_status == "no_relevant":
>     rendered = ""
> --- `openviking/retrieve/context_assembler/pipeline.py`

> served = plan.entries if rewrite_status != "no_relevant" else []
> --- `openviking/retrieve/context_assembler/pipeline.py`

This is working-context control by code/model selection and optional compaction. Removed or omitted content remains addressable in the external store and can be recalled again, subject to scope/dedup/exclusions. It is not an isolated agent stack frame: assembly returns content by value and URIs require explicit later reads rather than automatic dereferencing.

#### RT-RTE-session-commit
Label: Durable archive and extraction submission

Endpoints/progression/owner: caller/session service commit → path-locked authoritative session snapshot and retention split → raw archive/intent → QueueFS message → retained root/meta/ready publication → task acceptance; worker resume → archive readiness/order checks → `_run_memory_extraction` → compressor/extraction loop/updater submission. Principal is session RequestContext; task/archive IDs coordinate work across workers. SRC-1, `openviking/service/session_service.py`; `openviking/session/session.py`; `openviking/session/compressor_v3.py`; `openviking/session/memory/extract_loop.py`.

- Immediate return: status accepted, task_id, archive_uri and retention-related fields; not completed memory extraction.
- Later read-back: archived messages feed phase two; archive overview/current messages can later feed search. Compressor submits model-generated operations to retained-memory updater; exact revision/admission internals are left unresolved here.
- Delegated visibility: extraction gets prepared messages, existing memory context, schema/role scope and selected tools; future consumers see retained results, not necessarily the full original trace.
- Selection predicate: retention policy splits live/archive messages; extraction policy and allowed memory/peer types constrain processing; earlier archive readiness can defer resume.
- Invalidation or expiry: done/failed markers terminate resume; reset_context can insert a boundary stopping later session context/summaries. Full deletion/retention lifecycle is uninspected.
- Activation or effect: archive publication, queue dispatch and updater submission are wired; successful persisted revision and later behavioral use are unobserved.
- Evidence limits: no crash/restart experiments; full queue retry, updater conflict/rollback and phase-two exactly-once semantics are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission account: caller triggers archive and may set retention/memory policy; model proposes memory operations using schemas/provider instructions; parser/resolution/isolation and downstream updater mediate application. Computational contributions are distinct from initiating user approval. Per-content human approval is not established. Answer oracle: uninspected — this runtime submission trace supplies no reference-outcome evaluator. Operating mode: open trace-fed maintenance with configurable policy. Rejection/recovery: exceptions, terminal failure markers, readiness/order checks and strict-error options; no proven all-or-nothing rollback. Guidance persists as shipped provider/schema/protocol text and account registry; raw trace, metadata and admitted memory results are distinct retained parts.

> result = await updater.submit(
>     MemoryUpdateRequest(
>         operations=operations,
>         messages=list(messages),
>         ctx=ctx,
> --- `openviking/session/compressor_v3.py`

The inner ExtractLoop owns successive model/tool steps. Its schemas are generated from the context provider; advertised tools are registry entries filtered by `allowed_tools`. Provider callbacks execute tool calls concurrently and append rendered results to local messages. Final operations undergo resolution/repair. The mutable iteration bound makes this a repair-oriented loop, not a strict fixed-step guarantee. This model context is separate from the foreground host transcript; the updater receives operations/messages rather than returning all intermediate tool deliberation to the host. No general subprocess isolation follows (SRC-1, `openviking/session/memory/extract_loop.py`).

#### RT-RTE-skill-admission
Label: Conditional trace-to-skill admission

Endpoints/progression/owner: compressor session-skill extraction → rollout analyzer skill gradients → streaming trainer with existing SkillSet → PatchMergePolicyOptimizer/ExtractLoop → SkillPolicyUpdater → SkillOperationUpdater/SkillProcessor; deletes call VikingFS.rm on the skill root. SRC-1, `openviking/session/compressor_v3.py`; `openviking/session/train/components/policy_optimizer.py`; `openviking/session/train/components/skill_policy_updater.py`.

- Immediate return: submitted/skill_submitted counts and written skill URIs, or disabled/missing-input/error reasons.
- Later read-back: existing skills are loaded into future policy sets; retrieval supports the skill bucket and host recall can select it. Actual later invocation of a newly written skill is unobserved.
- Delegated visibility: model optimizer receives gradients and prefetched required files under memory-type isolation; admitted instruction content is separate from internal optimizer messages.
- Selection predicate: session_skill_extraction_enabled plus available processor; gradients filtered to memory_type skills; patch optimizer maps operations to plan items.
- Invalidation or expiry: delete removes whole skill subdirectory; update uses the processing pipeline. Persisted rollback for partial effects is uninspected.
- Activation or effect: reusable skill-content admission is wired, not proof of new executable permissions or improved task performance.
- Evidence limits: trajectory judgment, complete processor guarantees and live use/benefit are unobserved; only selected optimizer/updater stages inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/change/admission: session traces cause model-derived skill proposals; software plans and applies upserts/deletes. The caller can disable this path; individual deletion/application errors can reject effects. No per-content human veto is established. Recovery reports errors and may keep the prior in-memory policy set; it does not prove physical rollback. Guidance includes loaded skill policy set, registry schemas and patch-merge output contract; the persisted product is skill text/processed index material, not numerical model parameters. Answer oracle: uninspected — the inspected stages do not expose an expected-answer/reference-outcome protocol. Operating mode: conditional trace-fed maintenance, not a demonstrated bounded experiment.

> training_result = await skill_trainer.submit_gradients(skill_gradients)
> --- `openviking/session/compressor_v3.py`

> updated_policy_set=updated_policy_set if not all_errors else policy_set,
> written_uris=list(result.written_uris + result.edited_uris),
> deleted_uris=deleted_uris,
> errors=all_errors,
> --- `openviking/session/train/components/skill_policy_updater.py`

Theory assessment: source-native policy/gradient names alone do not identify a formulated explanatory theory. The route merges instruction content, but the actual candidate content and criticism are not supplied. Guidance application is wired; derivation, criticism/replacement and retained rationale are uninspected. theory-builder conditions 1–4: condition 1 conclusion status: uninspected (no actual whole theory candidate); condition 2 conclusion status: uninspected (model-mediated dependence on that theory not shown); condition 3 conclusion status: uninspected (no inspected criticism allocating blame); condition 4 conclusion status: uninspected (no traced criticism-dependent next round). Addressability: file/field edits are afforded, actual theory parts unresolved. Persistence: admitted skill files can outlive a session; later causal consumption unresolved. learning: uninspected — no future-capacity or attribution evidence. Reflection, reflective theory builder and autonomous theory builder: uninspected — selected plumbing does not establish the independent definitional conditions. No exercised self-improvement attribution is made.

#### RT-RTE-config-patch
Label: Runtime settings admission

Endpoints/progression/owner: ConfigManager.patch_cluster/patch_account → request validation → per-scope serialization → source read/merge/candidate validation/persist → copy-on-write publication → ordered consumer notification; account VLM/embedding providers invalidate resources. SRC-1, `openviking/config/manager.py`; `openviking/config/vlm.py`; `openviking/config/embedding.py`.

- Immediate return: ConfigChangeEvent after ordered notification.
- Later read-back: persisted settings and published candidates affect later model resolution and resource acquisition.
- Delegated visibility: consumers receive config events; old borrowed model resources can remain separate from newly selected resources. Exact notification failure behavior is uninspected.
- Selection predicate: scope and patch fields, current document merge, configured validators and consumer matching.
- Invalidation or expiry: config events retire/reselect cached model resources; account deletion evicts manager-owned state.
- Activation or effect: settings publication and consumer invalidation are wired; live provider behavior change is unobserved.
- Evidence limits: HTTP management permission paths, concrete config-source durability, deployment authorization and failure rollback are not fully traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/decider: caller supplies symbolic settings; manager validation and persistence admit them. Human versus computational caller is unresolved. Validator can reject; caller authorization is outside this inspected manager stage. Rollback/recovery: refresh keeps last effective state on reload failures according to its source contract, but persisted/publication/notification failure compensation is not established here. Guidance is schema/validator/merge rules; explicit settings persist. Answer oracle: inapplicable — settings validation is not expected-answer evaluation. Operating mode: administrative updates and refresh, not autonomous weight optimization or product-code improvement.

> # Phase 4: consumers run outside write locks, in publication order.
> await self._notify_in_order(notification)
> return event
> --- `openviking/config/manager.py`

#### RT-RTE-plugin-recall
Label: OpenCode automatic recall delivery

Endpoints/progression/owner: shipped OpenCode chat.message hook → memory-recall adapter → health/request/assembled context → shared recall selection → synthetic text part in host output. Compaction/dispose hooks separately request session flushing/commit. Host schedules hooks; plugin owns callback transformation, database owns retrieval, external OpenCode owns model invocation. SRC-1, `examples/opencode-plugin/index.mjs`; `examples/opencode-plugin/lib/memory-recall.mjs`; `examples/memory-plugin-shared/lib/recall-core.mjs`; `examples/opencode-plugin/package.json`.

- Immediate return: hook output gains a synthetic text part when a nonempty block and session ID exist; absent/failed/disabled recall can return without injection.
- Later read-back: stored context is queried on later chat messages; mapped OpenViking session enables server expansion/dedup. Full plugin trace-flush/persist/reload internals remain uninspected.
- Delegated visibility: host receives selected digest or rendered text, not necessarily all entries or source messages. Shared helper supports optional host compression callbacks, whose deployed use is uninspected.
- Selection predicate: recall enabled, user text present and long enough, session/cwd not bypassed, healthy service, server selection plus client no_relevant/digest precedence.
- Invalidation or expiry: server dedup and client config affect subsequent selection; exact client cache lifetime is uninspected.
- Activation or effect: output.parts injection is wired; actual host model consumption/compliance and useful effect are unobserved.
- Evidence limits: source only; shared module is generated/copied by prepack, not present at the imported path in this checkout. Canonical shared implementation was inspected, not packaged execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (String(result.stats?.rewrite || "").toLowerCase() === "no_relevant") return "";
> return String(result.digest || "").trim() || String(result.rendered || "").trim();
> --- `examples/memory-plugin-shared/lib/recall-core.mjs`

> output.parts.unshift({
>     id: `prt-ov-recall-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
>     type: "text",
>     text: injection,
>     synthetic: true,
>     sessionID,
>     messageID,
>   })
> --- `examples/opencode-plugin/lib/memory-recall.mjs`

This supplies context automatically under a host hook, unlike the boundary's instruction-driven MCP client. It is not a universal automatic-recall claim.

### Claims

#### RT-CLM-scoped-retrieval
Label: Scoped retrieval construction

Claimed operation: account/user-visible query scope is constructed in software before backend retrieval. Owner/enforcement: VikingFS required context and target checks, caller-scope reset, VikingVectorIndexBackend scope construction. Guarantee strength: protocol. Covered paths: semantic, keyword and filter-only lookup. Alternate paths: ROOT, bypass ACL, direct filesystem/internal calls, native storage and other consumers are not interchangeable with ordinary user retrieval. External contract: backend filter semantics/account selection and valid auth/ACL configuration. SRC-1, `openviking/storage/viking_fs/_access.py`; `openviking/storage/viking_fs/_semantic.py`; `openviking/storage/viking_vector_index_backend.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if ctx.bypass_acl:
>     return Eq("account_id", ctx.account_id)
> if ctx.role == Role.ROOT:
>     return None
> --- `openviking/storage/viking_vector_index_backend.py`

This is positive evidence for role-dependent scope, not a vulnerability finding or proof of deployed cross-account access. Configuration, backend selection and network envelope remain unobserved.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-planner-dispatch
Label: Planner response to retrieval dispatch

Consumer: VikingFS.search and retriever. Channel: parsed TypedQueries carrying model-produced query text/category/priority with code-restored target/type constraints. Force: symbolic dispatch invokes retrieval for the admitted queries; model interpretation selects wording, code limits scope. Horizon: one invocation. Evidence: [RT-RTE-session-search](#rt-rte-session-search), SRC-1, `openviking/storage/viking_fs/_semantic.py`. Does not grant host-shell authority.

#### RT-BAP-recall-context
Label: Selected context to host input

Consumer: OpenCode host callback output and, conditionally, its next model invocation. Channel: synthetic text part, selected from digest/rendered recall; natural-language content requires model interpretation. Force: plugin modifies host input structure, not a hard instruction-compliance invariant. Horizon: current chat invocation with later recall possible. Evidence: [RT-RTE-plugin-recall](#rt-rte-plugin-recall), SRC-1, `examples/opencode-plugin/lib/memory-recall.mjs`. Delivery wiring is established; activation and benefit are not.

#### RT-BAP-config-model
Label: Published settings to model resource selection

Consumer: account VLM/embedding providers. Channel: ConfigChangeEvent and symbolic config fields; force: resource invalidation and subsequent selection, not inferred training. Horizon: later calls until replaced/evicted. Evidence: [RT-RTE-config-patch](#rt-rte-config-patch), SRC-1, `openviking/config/vlm.py`; `openviking/config/embedding.py`. Exact external model identity and production effect remain uninspected.

## Annotations

none
