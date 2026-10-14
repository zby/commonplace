---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Cognee runtime baseline: ingestion, recall, session maintenance, decorated consumers and agentic tools at the frozen revision."
run-id: AAS-2026-10-14-cognee-d8839fe03c5b-01
reviewed-boundary: f154b32a9e544dac73e7ddf2010327cf9988edcd
---

# Cognee runtime report

## Runtime account

Cognee normally performs a returning memory computation, not an enclosing agent loop. A caller supplies content to `remember`, waits for a memory build, and later calls `recall`. An optional agentic retriever does own a bounded model/tool loop. A decorator can instead supply memory to a host function without deciding that function's actions. These are different control boundaries, represented by [RT-RTE-permanent-memory](#rt-rte-permanent-memory), [RT-RTE-recall-dispatch](#rt-rte-recall-dispatch), [RT-RTE-agentic-tools](#rt-rte-agentic-tools) and [RT-RTE-decorated-agent](#rt-rte-decorated-agent).

All source findings below use SRC-1 at the frozen revision. Added inspection covers the standard cognify task assembly, authorization helper, tool dispatcher and registry, agentic retriever, agent-memory runtime, improve registry/admission/locks, embedding configuration and skill proposal/apply implementation. These supply implementation evidence; docstrings supply design explanations, not demonstrated operation. No target, test, example, provider or database was executed. Operation, actual context activation, reliability and benefit remain unobserved. This extends inspection, not the boundary's `complete artifact, partial loop` classification.

### Ordinary invocation and shipped entry paths

For a local blocking `remember(text, dataset_name=...)`, code sets up the engine, resolves a default user if none was supplied, resolves a writable dataset, records an operation and invokes `add` followed by `cognify`. The latter assembles classification, chunk extraction, graph extraction/summarization and graph/vector loading; provenance, contradiction checks and temporal replacement tagging are conditional. Code owns progression; a model produces extraction content on the LLM path, but does not choose the pipeline's next task. Caller-supplied prompts and pipeline arguments can change the transformation. The terminal result contains pipeline status; blocking failures are re-raised, while background failures update the result object (SRC-1, `cognee/api/v1/remember/remember.py`, `cognee/api/v1/cognify/cognify.py`).

> # Permanent memory: add + cognify (+ optional improve)
> --- `cognee/api/v1/remember/remember.py`

> # LOAD: persist nodes, edges, and embeddings to graph/vector DBs
> --- `cognee/api/v1/cognify/cognify.py:622-622`

A later `recall(question, datasets=...)` resolves source lanes, chooses a search type, checks readable datasets and dispatches retrieval. Explicit search type overrides automatic routing. Without a usable LLM, the default graph lane selects chunks rather than generated completion. An automatically routed guess can retry the fallback type when unsupported or empty in selected cases; explicitly pinned types are not second-guessed. In auto-fallthrough mode a session hit can suppress graph retrieval. Thus an empty graph answer is not the only reason graph work may be skipped (SRC-1, `cognee/api/v1/recall/recall.py`).

> # Auto mode special case: session hit short-circuits graph.
> if auto_fallthrough and src == "graph" and merged:
>     break
> --- `cognee/api/v1/recall/recall.py`

Shipped Python exports and the separate saved-memory Company Brain driver are established in [boundary](boundary.md#boundary-and-evidence). CLI remember/recall call sites resolve into these APIs (SRC-1, `cognee/cli/commands/remember_command.py`, `cognee/cli/commands/recall_command.py`; call-site search only). The MCP client supports local Python and HTTP modes. Its HTTP bare recall first lists accessible datasets when neither datasets nor session is supplied, whereas the local branch forwards an unscoped call. Transport equivalence is therefore not assumed (SRC-1, `cognee-mcp/src/cognee_client.py`). The central APIs also test for a configured remote client before local work; remote result semantics require the server contract. HTTP authentication middleware, frontend, connectors, distributed workers and all CLI options were not traced here; their behavior remains an included inspection limit.

### Four forcing cases

1. **Session storage with failed improvement.** `remember(..., session_id=...)` writes session data first and returns `session_stored`. Automatic improvement runs in a separately scheduled task, subject to configuration, host admission and debounce. An improvement exception does not retroactively mark that storage as failed. This falsifies the stronger inference that a successful remember implies permanent graph admission. See [RT-RTE-session-improve](#rt-rte-session-improve).
2. **Explicit maintenance versus automatic host admission.** A host callback can skip automatic improves but errors and malformed callback returns allow them. Direct `improve()` bypasses this callback. The callback is a work-saving policy, not a universal budget or authorization gate. See [RT-CLM-auto-admission](#rt-clm-auto-admission).
3. **Tool dispatch versus arbitrary handler execution.** Agentic retrieval narrows the manifest, then dispatch checks scope and dataset permission. A dotted handler reference imports Python code in-process. No isolation boundary is established by those ACL checks; they govern dispatcher entry, not every effect a handler can produce. Direct host calls to handlers or providers do not inherit this dispatcher merely because it exists. See [RT-RTE-agentic-tools](#rt-rte-agentic-tools).
4. **Contending improves versus multi-worker operation.** Session/dataset claims suppress overlapping in-process runs; session losers can request another holder pass. The pass bound can leave a pending request for a future claimant, and the registry is process-local. This is neither cross-worker exclusion nor guaranteed eventual processing. See [RT-CLM-improve-coordination](#rt-clm-improve-coordination).

These cases inspect implemented branch behavior, not observed executions. Native provider tools, shell/subprocess handlers, manual graph writes, custom memify tasks, durable worker variants, connector scheduling and deployment-level enforcement remain uninspected. The current grant set and deployed isolation envelope were not supplied. Capability surface, configured grants and exercised capability are not interchangeable.

### Context and effect boundaries

The agent-memory decorator creates a per-invocation ContextVar frame, retrieves bounded memory, calls the wrapped coroutine, resets the frame, then attempts trace persistence. The gateway injects that memory only into its structured-output input. A host using an unrelated provider call need not receive it. Graph-memory retrieval errors produce empty memory; trace persistence errors are logged. `only_context` retrieval uses the bare `context_result`, rather than pasting Cognee's own question framing into the host input (SRC-1, `cognee/modules/agent_memory/runtime.py`, `cognee/infrastructure/llm/LLMGateway.py`). This frame resembles a selected-input call frame, but its accumulated external stores survive it and the arbitrary function return escapes; it does not create an isolated provider context or sandbox the function.

The agentic retriever initially exposes skill names/descriptions, not full procedures. It intersects ambient tools with a caller filter and the union of skill-declared tools. Full skill bodies can then arrive through `load_skill`; tool outputs longer than 8,000 characters are truncated before appending to the loop context, while stored tool traces retain at most 1,000 output characters per call. Session history and optional active guidance also enter this loop. The iteration limit bounds tool turns but is followed by an extra best-effort completion request. There is no total token-window bound established by the inspected loop (SRC-1, `cognee/modules/retrieval/agentic_retriever.py`).

Model and embedding selection are separate configurable distributed-parametric components, [RT-CMP-llm-gateway](#rt-cmp-llm-gateway) and [RT-CMP-embedding-config](#rt-cmp-embedding-config). Source-level dispatch and named models do not freeze provider weights or establish local training. Revisions to retained content are not weight updates.

## Shared records

### Components

#### RT-CMP-llm-gateway
Label: LLMGateway provider dispatch

Source-native identity: `LLMGateway` and the configured LLM adapter. Representational form: symbolic dispatch over external distributed-parametric inference. Storage substrate: Python module/configuration plus provider-hosted or locally served model weights; provider internals uninspected. SRC-1, `cognee/infrastructure/llm/LLMGateway.py`, `cognee/infrastructure/llm/config.py`.

Parameters changing during operation: no parameter-update operation is established in the inspected gateway; external endpoint internals are uninspected. Exact model version pinned: no weight digest or immutable provider revision is established by its model string. Mutable endpoint resolving to another model: possible through configured endpoint/provider/model overrides; actual resolution uninspected. Native LiteLLM, legacy instructor and BAML structured-output branches are dispatched separately. Transcription calls do not pass through the structured-output memory/usage wrapper.

> text_input = _inject_agent_memory(text_input)
> llm_config = get_llm_config()
> framework = resolve_structured_output_framework(llm_config)
> --- `cognee/infrastructure/llm/LLMGateway.py`

#### RT-CMP-embedding-config
Label: EmbeddingConfig inference selection

Source-native identity: `EmbeddingConfig`. Representational form: symbolic provider configuration selecting distributed-parametric text embedding inference; resulting dense vectors are numerical representations, not the provider's weights. Storage substrate: environment/settings, local downloaded model or remote service; vectors subsequently go to configured storage. SRC-1, `cognee/infrastructure/databases/vector/embeddings/config.py`.

Parameters changing during operation: not established in this configuration/ingestion path; external service internals uninspected. Exact version pinned: model names are present, immutable weight revisions are not established. Mutable endpoint resolving to another model: configurable endpoint and model allow it; deployment resolution uninspected. The local keyless alternative does not eliminate the embedding component.

> DEFAULT_LOCAL_EMBEDDING_PROVIDER = "fastembed"
> DEFAULT_LOCAL_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
> --- `cognee/infrastructure/databases/vector/embeddings/config.py`

### Operative objects

#### RT-OBJ-agent-step
Label: AgentStep action decision

Source-native identity: `AgentStep` with `thought`, optional `tool_call` and optional `final_answer`. Representational form: symbolic Pydantic fields choosing dispatch, alongside natural-language thought/answer interpreted by model or caller. Storage substrate: per-turn Python object; selected tool-call material can later be copied into SkillRun traces. SRC-1, `cognee/modules/retrieval/agentic_retriever.py`. Schema shape is not answer correctness and does not require exactly one action: executable code prioritizes a non-empty final answer, otherwise tries the tool call, otherwise stops and forces completion.

> if step.final_answer is not None and step.final_answer.strip():
>     return step.final_answer
> --- `cognee/modules/retrieval/agentic_retriever.py`

#### RT-OBJ-skill-proposal
Label: SkillImprovementProposal admission payload

Source-native identity: `SkillImprovementProposal`, containing old/proposed procedures, runs used, rationale, confidence and status. Representational form: natural-language procedure/rationale plus symbolic target IDs, dataset scope and status. Storage substrate: graph DataPoint written through `add_data_points`; full storage guarantees remain adapter-dependent. SRC-1, `cognee/modules/memify/skill_improvement.py`. The runtime declares the proposal/apply control mechanism, leaving detailed memory lineage and content revision to the memory analyst.

> old_procedure=skill.procedure,
> proposed_procedure=_format_skill_procedure(skill.name, draft.proposed_procedure),
> --- `cognee/modules/memify/skill_improvement.py`

### Routes

#### RT-RTE-permanent-memory
Label: Permanent remember pipeline

Endpoints/progression: caller content → local setup/user/dataset resolution → `add` → blocking `cognify` → result → later recall. Owner: API code and pipeline executor, with model extraction as a bounded transformation. State identities are user, dataset and pipeline run; executor effects cross raw-data and graph/vector storage interfaces. Standard task assembly classifies and chunks documents, extracts/summarizes and loads DataPoints. Optional improve follows rather than controlling basic ingestion. SRC-1, `cognee/api/v1/remember/remember.py`, `cognee/api/v1/cognify/cognify.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RememberResult after blocking processing, or a running result backed by an asyncio task in background mode; foreground processing errors can raise.
- Later read-back: Cognified content is intended for dataset-scoped search/recall on later invocations; successful adapter persistence is not observed.
- Delegated visibility: Extraction receives selected chunks and configured prompts; database adapters receive generated DataPoints. Remote configuration delegates the API operation to its remote client instead.
- Selection predicate: Caller dataset/content and cognify configuration determine task inputs; later retrieval has its own selector.
- Invalidation or expiry: Conditional temporal replacement/provenance tasks exist; full delete/expiry lifecycle uninspected in this route.
- Activation or effect: Executable storage dispatch is wired; later answer/action change is unobserved.
- Evidence limits: Standard local assembly and remember wrapper inspected, not every extractor, storage adapter, custom pipeline or durable execution mode.

Admission: caller supplies content and may supply extraction guidance; software/model output flows into storage without a per-item human approval in this inspected assembly. Caller identity does not establish human authorship. This is an open ingestion request, not a controlled experiment; no expected-answer oracle is used in the inspected assembly. Blocking errors propagate; background errors mark the result. Atomic rollback across stores is not established here.

#### RT-RTE-recall-dispatch
Label: Recall source and search dispatch

Endpoints/progression: question → remote delegation or local source runners → session/trace/context/graph/tool/code/skill lanes → normalized merged responses. Owner: recall code chooses lanes, caller pins options, rule routing selects an unpinned graph search type. Dataset authorization precedes graph retrieval; warm-up markers can replace graph work. SRC-1, `cognee/api/v1/recall/recall.py`, `cognee/modules/search/methods/search.py`, `cognee/modules/data/methods/get_authorized_existing_datasets.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Merged RecallResponse entries, a readiness marker, an empty list or a propagated error.
- Later read-back: Reads accumulated session/graph content; logs search history for possible later consumers, whose maintenance use is not traced here.
- Delegated visibility: Selected query/context goes to the retriever/provider; remote mode forwards caller arguments under a server contract not verified here.
- Selection predicate: Resolved scope, session identity, dataset grants, top_k, explicit search type or no-LLM/rule/default routing; session success can suppress graph in auto mode.
- Invalidation or expiry: uninspected — session and graph expiry/deletion are separate lifecycle mechanisms.
- Activation or effect: Retrieves and optionally generates answer content; downstream host compliance is unobserved.
- Evidence limits: Central dispatch inspected; every lane's transformation and authorization path is not characterized, so no uniform all-source ACL conclusion follows.

Operating mode: open query answering. Runtime routing is code policy, not answer-oracle comparison. Caller can veto automatic routing by pinning a type. Unsupported/empty routed guesses have conditional retries; pinned types preserve their error/empty semantics. Graph authorization's owner is the user-permission helper, not the model.

> search_datasets = await get_authorized_existing_datasets(
>     datasets=dataset_ids, permission_type="read", user=user
> )
> --- `cognee/modules/search/methods/search.py`

#### RT-RTE-session-improve
Label: Session storage and maintenance continuation

Endpoints/progression: session remember → session cache write → optional background improve → frozen run inputs → lock claim → ordered gated stages → recorded stage results and release. Owner: remember/improve code; host callback can decline only the automatic start; individual stages own transformations. User/session/dataset identities govern the claims. Registry stages cover feedback weights, QA/traces, agent context, distillation, preferences, truth subspace, enrichment and global context index. SRC-1, `cognee/api/v1/remember/remember.py`, `cognee/api/v1/improve/improve.py`, `cognee/modules/improve/registry.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Session-stored RememberResult with optional task; explicit background improve returns a running ImproveResult that can be awaited.
- Later read-back: Stages admit graph/session-derived material for future recall; exact candidate transformations and revision semantics are left to specialist tracing.
- Delegated visibility: Stage inputs carry authorized user/dataset, sessions, config and graph capabilities; model-facing stage prompts are not all inspected here.
- Selection predicate: self_improvement flag plus auto-enabled config, host admission and debounce; explicit improve bypasses automatic admission; registry gates and watermarks select stage work.
- Invalidation or expiry: Operation outcome/stamps distinguish failed/no-op/finished runs; detailed stage watermark and retained-content invalidation uninspected.
- Activation or effect: Storage/maintenance calls are wired; actual graph admission and subsequent behavioral dependence are unobserved.
- Evidence limits: Orchestration and admission inspected, not all nine stage bodies; the method name does not establish successful improvement.

Trigger and admission: new session data, explicit improve, or a post-ingestion auto continuation. Code starts stages; model transformations may propose knowledge, but a host start check is not per-content approval. Direct stage APIs/custom memify paths are not covered by the orchestration claims. No expected-answer oracle is established at this orchestration layer. Operating mode is open maintenance over available state, not an experimental curriculum. Guidance is stage-specific; only registry order and configuration are established here. Fatal QA persistence failure aborts; budget exhaustion skips remaining stages; other errors are recorded while later stages continue. Lock release is in finally. A failed bridge leaves already-written session data intact. No cross-store transaction or automatic content rollback is established.

> if stage.fatal and stage_result.status == "errored":
>     raise _abort_run(
> --- `cognee/api/v1/improve/improve.py`

#### RT-RTE-decorated-agent
Label: Agent-memory wrapped host invocation

Endpoints/progression: configured async function call → resolved user/dataset scope → ContextVar frame → session/graph retrieval → arbitrary wrapped function → reset frame → trace persistence and optional periodic graph persistence. Owner: wrapper controls preparation/cleanup; host function owns next actions. SRC-1, `cognee/modules/agent_memory/decorator.py`, `cognee/modules/agent_memory/runtime.py`, `cognee/infrastructure/llm/LLMGateway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Wrapped function's result, or its raised exception; finally attempts trace persistence.
- Later read-back: Enabled trace feedback can feed recent-session retrieval; graph memory can reach future calls; periodic persistence depends on configured trace-count divisibility.
- Delegated visibility: Only structured-output gateway calls inside the active frame automatically receive the added memory text; arbitrary external model calls are not covered.
- Selection predicate: Enabled sources, derived/fixed query, configured graph top_k, recent trace last_n and bounded serialization/context length.
- Invalidation or expiry: Frame reset on exit removes invocation-local injection; persistent store expiry uninspected.
- Activation or effect: Gateway input rewriting is wired; host behavior depending on the injected material is unobserved.
- Evidence limits: Arbitrary wrapped function and external integrations excluded from attributed Cognee behavior; registration metadata is not an execution grant.

Trace admission is software-controlled when saving is enabled; returned host values are sanitized before storage. Starting the decorated call is not a human approval of each trace. Error logging and empty-memory fallbacks preserve host progress for the inspected retrieval/persistence helpers, not a guarantee that every cleanup operation cannot raise. The gateway text is natural-language context, not executable instruction enforcement.

> return f"Additional Memory Context:\n{context.memory_context}\n\nOriginal Input:\n{text_input}"
> --- `cognee/infrastructure/llm/LLMGateway.py`

#### RT-RTE-agentic-tools
Label: Agentic retrieval and tool execution

Endpoints/progression: authorized dataset retriever → triplets/skill catalog/tool manifest → model AgentStep → final answer or execute_tool → output appended to context → next model turn → bounded fallback completion. Owner: model selects next action within manifest; code enforces dispatch and iteration bounds. SRC-1, `cognee/modules/retrieval/agentic_retriever.py`, `cognee/modules/tools/execute_tool.py`, `cognee/modules/tools/registry.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer list from agentic completion, or error; after max_iter/no-action it requests a best-effort final string.
- Later read-back: Opened skills yield stored SkillRuns; caching can store QA and supply history/guidance on later invocations.
- Delegated visibility: Model sees formatted memory, names/descriptions, manifest and progressively loaded bodies/tool outputs; handlers receive args, dataset, user and Tool object.
- Selection predicate: Caller tool filter intersected with ambient tools and skill-declared union; only opened skills are recorded as used.
- Invalidation or expiry: ContextVars for active/opened skills reset after loop; retained runs/QA expiry uninspected.
- Activation or effect: Code invokes the chosen permitted handler; effects can exceed memory reads according to handler code. Model compliance and actual execution are unobserved.
- Evidence limits: Dispatcher enforcement inspected, not all handlers or deployed host isolation; opaque model reasoning is not evidence of criticism or correctness.

Capability versus grants: registry can resolve built-in and graph Tool records; current exposed names are filtered by caller/skills; execution uses the user's required dataset verb. With dataset_id absent the generic dispatcher skips its dataset authorization branch, though this retriever requires an explicit dataset. Python handler import is not sandboxing. Scope/permission/invocation errors become tool-result text; not every exception class is caught by the safe wrapper. No answer oracle or per-action human approval is established in this loop. Operating mode is open query-driven work. Dynamic handler references admit capability linkage through registry data; authorship, vetting and rollback of all graph-backed Tool producers remain uninspected.

> if allowed_tools is not None and tool_name not in allowed_tools:
>     raise ToolScopeError(f"Tool {tool_name!r} is not in the active skill/tool scope")
> --- `cognee/modules/tools/execute_tool.py`

> module = importlib.import_module(module_path)
> --- `cognee/modules/tools/registry.py`

#### RT-RTE-skill-revision
Label: Proposal-first skill procedure replacement

Endpoints/progression: opt-in remember skill_improvement config → low-score/error runs → model draft → stored proposal; later apply with proposal_id → target check → whole procedure replacement → graph write. Owner: code selects evidence and verifies target; model drafts; caller decides whether to request apply. SRC-1, `cognee/modules/memify/skill_improvement.py`. Operative payload is [RT-OBJ-skill-proposal](#rt-obj-skill-proposal); future procedure visibility belongs to [RT-RTE-agentic-tools](#rt-rte-agentic-tools).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored proposal, applied proposal, None when no qualifying runs, or validation error.
- Later read-back: Proposal can be fetched for review; applied procedure replaces Skill text used by later resolution/loading.
- Delegated visibility: Drafting model receives current skill, selected run IDs/scores/errors/result summaries, not the full unabridged execution trace.
- Selection predicate: Explicit dataset/skill, errored or score below threshold, newest started_at_ms up to max_runs; application requires proposal_id and matching target name.
- Invalidation or expiry: Apply overwrites procedure/search text and marks proposal applied; old_procedure persists in proposal. No stale-base comparison or automatic rollback is shown in inspected apply function.
- Activation or effect: Graph replacement wired; actual later loaded skill changing actions remains unobserved.
- Evidence limits: A draft instruction request and score filter establish neither successful learning nor reliable content-directed criticism.

Trigger/proposal/admission: caller opts in; model supplies the proposed complete procedure/rationale/confidence; default apply=False separates proposal from installation. Caller can withhold apply; human versus computational caller is unresolved. Apply validates dataset/proposal/skill identity, not a tested performance improvement. Stored old text affords a recovery reference, not a shipped rollback guarantee. Guidance requests direct complete instructions with no state mutation by the drafting model. Operating mode is open revision of failures, not bounded comparative experimentation. Scores are selection inputs; their evaluator/reference-answer provenance is uninspected, so no answer oracle is established.

> apply = bool(config.get("apply", False))
> --- `cognee/modules/memify/skill_improvement.py`

> skill.procedure = _format_skill_procedure(skill.name, proposal.proposed_procedure)
> --- `cognee/modules/memify/skill_improvement.py`

Theory account, scoped to this proposal mechanism: procedures are localized natural-language operational guidance; their contents may express a theory, but no actual procedure/proposal run is supplied. Whole replacement is addressable at the procedure level; independently revisable assumptions/scope conditions are not established. Current procedures and selected outcome summaries shape drafting; proposed instructions and rationale persist, but a later rationale consumer is not established.

Theory-builder conditions 1–4:

- condition 1 conclusion status: afforded

Whole localized guidance is representable; whether a particular procedure formulates a theory is uninspected.

- condition 2 conclusion status: afforded

Progressive procedure delivery is wired, but content-dependent decisions are unobserved.

- condition 3 conclusion status: uninspected

Failure evidence and requested revision do not themselves state a challenged claim and placement of blame; model internals and actual drafts are not supplied.

- condition 4 conclusion status: afforded

Applied guidance and future runs can enter another revision request; retention and use of actual criticism remain unobserved.

- learning conclusion status: uninspected

No capacity improvement or attribution evidence supplied.

- reflection conclusion status: afforded

Stored skill procedures and skill-run outcomes represent selected runtime guidance/operation and can mediate its revision; actual bidirectional operation is unobserved.

- reflective theory builder conclusion status: uninspected

No demonstrated method-text criticism satisfying all four conditions.

- autonomous theory builder conclusion status: uninspected

Internal application is caller-selected and caller role is unresolved; computational drafting alone cannot establish all internal roles.

- self-improvement conclusion status: afforded

Within Cognee's skill-guided retriever, failure-fed replacement can change later instruction supply; the independent objective is better skill task performance. Update evidence selection, replacement and a possible later load path are wired, but subsequent behavior causally depending on the change is unobserved. Successful improvement is not established.

### Claims

#### RT-CLM-auto-admission
Label: Automatic improvement host policy

Claimed operation: a host can decline automatic improvement without blocking stored content. Owner/enforcement: registered callback consumed by remember before session debounce and on the permanent route. Guarantee strength: policy, explicitly fail-open. Covered paths: automatic remember continuations only. Alternate paths: explicit improve never gated, stage/custom memify entry paths uninspected. Required external contract: host registers an async check and returns a non-empty reason string; provider budgets still require their own enforcement. SRC-1, `cognee/modules/improve/admission.py`, `cognee/api/v1/remember/remember.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> The check can never break ``remember()``: nothing registered, a check that
> raises, and an answer that is neither ``None`` nor a reason string all mean
> "allow".
> --- `cognee/modules/improve/admission.py`

This is supported by the helper's try/except/return behavior, not a security guarantee about arbitrary host callback side effects. Explicit improve and malformed configuration are consequential counterpaths to a stronger universal admission claim.

#### RT-CLM-improve-coordination
Label: Process-local improve exclusion and recovery

Claimed operation: overlapping improve runs claim all session/dataset keys atomically or skip; session losers may request a holder rerun. Owner/enforcement: asyncio-held set plus registry lock and orchestration finally/release. Guarantee strength: protocol. Covered paths: this local improve orchestrator in one process. Alternate paths: multi-process workers, direct maintenance tasks and graph writes are not protected by this set. Required external contract: cross-worker deployment must supply shared advisory/Redis-style locking; database atomicity and eventual retries are separate. SRC-1, `cognee/infrastructure/locks/session_lock.py`, `cognee/api/v1/improve/improve.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> _improving_sessions: set[str] = set()
> --- `cognee/infrastructure/locks/session_lock.py`

> Scope: single-worker FastAPI. For multi-worker deployments, layer a
> row-level SQL advisory lock or Redis SETNX on top — the call sites
> are factored so that's a local change.
> --- `cognee/infrastructure/locks/session_lock.py`

The orchestration warns when its pass limit leaves a rerun pending. Neither a rerun request nor background launch is proof that all session data reached durable graph storage. Stage result/error tracking and operation stamps improve diagnosability; no observed recovery reliability follows.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-memory-injection
Label: Retrieved memory to structured-output input

Consumer: provider adapter called through LLMGateway inside an active decorated invocation. Channel: Additional Memory Context prepended to text_input. Force: natural-language information/guidance interpreted by the model, not mandatory code execution. Horizon: invocation-local frame, with possible cross-invocation retrieval from retained graph/session state. SRC-1, `cognee/infrastructure/llm/LLMGateway.py`, `cognee/modules/agent_memory/runtime.py`; implementation witness quoted under [RT-RTE-decorated-agent](#rt-rte-decorated-agent). Delivery is wired; obedience or changed output is unobserved. Direct unrelated provider calls are outside this path.

#### RT-BAP-skill-guidance
Label: Loaded skill procedure to agentic decisions

Consumer: model producing AgentStep in agentic retrieval. Channel: progressive load_skill tool results appended to loop_context, followed by generate_completion; skill metadata is supplied before procedure loading. Force: interpreted natural-language guidance, while code scope/ACL rules still govern tool dispatch. Horizon: current tool loop and later invocations that resolve retained Skill data. SRC-1, `cognee/modules/retrieval/agentic_retriever.py`; delivery policy is source-declared and loop append is inspected, but full load_skill body transformation was not inspected here, preventing a completeness claim about delivered procedure content.

> Skill procedure bodies are not loaded into the system prompt up-front. Only
> their names and descriptions are shown in the catalog; the LLM calls the
> load_skill tool to fetch a body on demand (progressive disclosure).
> --- `cognee/modules/retrieval/agentic_retriever.py`

## Annotations

none
