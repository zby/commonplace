---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "WeKnora runtime baseline tracing agent turns, RAG, tool controls and skill-image admission at the frozen Git revision."
run-id: AAS-2026-10-15-weknora-7adf8a01c381-01
reviewed-boundary: "234aa948db29c10f5ed4b7939285c7b3711c5d4c"
---

# WeKnora runtime report

## Runtime account

### Work and evidence basis

WeKnora ships a knowledge application, not only an inner agent loop. RAG answers, agent tasks and wiki organization consume the same knowledge bases; document processing and background maintenance produce their usable state. This is the declared work in SRC-1, `README.md`, as retained in [boundary](boundary.md#boundary-and-evidence). This report inspects implementation at the boundary's pin. There are no supplied execution traces or experiments. Every implemented route below has uninspected operation; delivery does not establish model compliance, activation or benefit.

The ordinary invocation selected here is an authenticated HTTP agent turn. The shipped HTTP alternatives are knowledge chat and retrieval without answer generation (SRC-1, `internal/router/routes_chat.go`). Server and desktop entry points, frontend, CLI, Go client, mini-program, IM/embed callers, Python MCP bridge and DeepSeek Harness plugin are in the boundary. Their initial entry-path coverage is in [boundary](boundary.md#top-level-coverage). Their distinct external host scheduling and every UI/client transport branch were not traced here. The bridge and plugin expose application operations; they do not establish that an external host runs WeKnora's engine. The server router also places embed, workspace MCP, browser-extension and terminal-ticket surfaces before global authentication; these have separate authentication responsibilities, not coverage automatically supplied by the normal chat middleware (SRC-1, `internal/router/router.go`). Exhaustive authorization of these surfaces remains uninspected.

New implementation coverage in this member includes bounded passages of `internal/agent/engine.go`, `internal/agent/act.go`, `internal/agent/think.go`, `internal/agent/observe.go`, `internal/agent/compaction/compactor.go`, the tool registry/MCP catalog/MCP execution code, approval gate, chat routes and handler, agent construction and caller, RAG event dispatcher, four model factories, document admission, evaluator and tenant skill installer/verifiers. All are SRC-1 implementation evidence; comments and prompt constants separately describe contracts. Searches located model factories, tools, routes and admission branches. No source was added and no target code was executed.

### Ordinary agent turn

[RT-RTE-agent-turn](#rt-rte-agent-turn) follows `/api/v1/agent-chat/:session_id` through request validation, owner-scoped session lookup, shared-agent resolution, message persistence, live-run coordination, asynchronous execution, event streaming and assistant completion. The initiating principal is an authenticated tenant user or authorized API-key principal. Session ID, user/assistant message IDs, request ID, agent ID and tenant scopes have different roles; a shared agent can supply a different retrieval/model tenant while session storage remains the caller's. The agent service requires a custom agent and resolves its model, effective knowledge scopes and tool registry. It reconstructs stored history, stages durable attachments into the selected workspace, recalls long-term memory and calls the engine. History loading failure degrades to empty history rather than proving no persistence.

At each ReAct round the engine refreshes MCP definitions, manages context, drains user steering, streams a model call and interprets its answer/tool-call structure. The model proposes the next action; Go code decides execution eligibility, stopping, context rewriting and error handling. Tools can execute sequentially or, when configured, in parallel. Tool results return to subsequent rounds. Natural stop without tool calls supplies the final answer; empty/repeated or repeatedly truncated output has guard paths. Exhausting the ordinary budget can invoke answer synthesis. Cancellation preserves partial steps through completion handling rather than guaranteeing a complete answer. SSE events and optional Langfuse spans expose intermediate work; they are machinery for observability, not observed runs (SRC-1, `internal/agent/engine.go`, `internal/agent/act.go`, `internal/handler/session/qa.go`).

The inner engine is turn-local, but the application is not. Assistant content and AgentSteps are persisted by handler completion; multi-turn calls reload them, and eligible compactions persist checkpoints. Memory extraction and wiki revisions belong to the specialist accounts; the runtime establishes their caller/consumer placement rather than revising their records. The direct installer caller is materially different: it calls the engine without normal chat history and requires an error/completion result before switching an image, whereas AgentQA emits an execution-error event and returns through its application error path (SRC-1, `internal/application/service/tenant_skill_install.go`, `internal/application/service/session_agent_qa.go`).

### Forcing cases and controls

Four forcing cases bound the conclusions rather than turning one path into a system-wide guarantee:

1. **MCP direct versus catalog call.** [RT-RTE-mcp-call](#rt-rte-mcp-call) shows both reaching shared registry execution and MCPTool policy checks. Per-tool approval is conditional, not a universal effect gate. Missing checker, missing execution metadata/EventBus and the configurable fail-open behavior limit the guarantee. A reconnect retry can repeat an external call, so local completion tracking is not remote exactly-once execution.
2. **Host shell versus remote shell.** [RT-RTE-sandbox-execution](#rt-rte-sandbox-execution) shows host shell registration need not satisfy the remote SkillsEnabled entitlement. Built-in AllowedTools is not the complete capability grant: shell/files, MCP and native browser operations have separate registration conditions. External providers and host configuration determine actual isolation.
3. **Context overflow and oversized tool result.** [RT-RTE-context-rewrite](#rt-rte-context-rewrite) shows model summarization, a raw-archive fallback, checkpoints and lossy tool-result previews. Context management is not a guarantee of complete evidence preservation or provider acceptance.
4. **Installation success claim versus verifier rejection.** [RT-RTE-skill-install](#rt-rte-skill-install) requires checks before the snapshot pointer moves and feeds repairable findings into another installer turn. The gate checks declared commands, source/script structure and dependency availability; it is not a functional oracle for everything the skill promises. The model discovers prose-only prerequisites, so omitted declarations remain a coverage limit.

Load-bearing guarantees have distinct owners and coverage:

| Guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths and external contract | Status |
|---|---|---|---|---|
| Owner-scoped ordinary chat admission | Router guards plus parseQARequest/GetOwnedSession | policy; inspected HTTP knowledge/agent chat routes | Direct service callers, embed/IM, terminal and MCP endpoint authentication are not established by this check; relies on auth/principal and repository contracts | implementation conclusion status: wired; operation conclusion status: uninspected |
| Validate selected tool arguments before execution | ToolRegistry.execute; engine additionally rejects known truncated arguments and unresolved handles | protocol; built-ins and inspected direct/catalog MCP execution | Direct external operations and installer verification executors are separate; depends on schema fidelity and tools honoring arguments | implementation conclusion status: wired; operation conclusion status: uninspected |
| MCP disable/approval policy | MCPTool.Execute and approval.Gate | policy; registered MCP tools including catalog-resolved execution, with configured gate and execution metadata | Shell, native browser, direct model calls and knowledge admission do not pass this gate; nil checker disables gating, checker errors can be configured fail-open; remote effects require provider fidelity | implementation conclusion status: wired; operation conclusion status: uninspected |
| One completion emission per executeLoop exit | Local completionEmitted flag and deferred emitCompletion | invariant at local emission control; normal, error and cancellation returns from that function | Not a durable exactly-once delivery/write guarantee, not crashes or exits before entering the loop; EventBus and DB must independently succeed | implementation conclusion status: wired; operation conclusion status: uninspected |
| Do not switch installed image before verification | TenantSkillService verification, ownership/lock checks, ledger and switchImagePointer | protocol; inspected remote snapshot installation path | Host install path and provider snapshot implementation not traced to equivalence; DB/lock/provider contracts required; no all-skill correctness guarantee | implementation conclusion status: wired; operation conclusion status: uninspected |

The completion invariant's implementation witness is SRC-1, `internal/agent/engine.go`:

> completionEmitted := false
> emitCompletion := func() {
> if completionEmitted {
> return
> }
> completionEmitted = true
> e.emitCompletionEvent(context.WithoutCancel(ctx), state, sessionID, messageID, startTime)
> }
> defer emitCompletion()
> --- `internal/agent/engine.go`

An iteration limit is also not unconditional: SRC-1, `internal/agent/engine.go`, implements unlimited configuration, and loop-end steering can admit a bounded extra round:

> if e.config.UnlimitedIterations() {
> return true
> }
> return round < e.config.MaxIterations
> --- `internal/agent/engine.go`

### Alternate work and change admission

[RT-RTE-rag-answer](#rt-rte-rag-answer) is a code-directed event pipeline, not a foreground agent selecting every retrieval step. Its evaluator uses a different fixed pipeline and supplied QA pairs, as described in [RT-RTE-dataset-evaluation](#rt-rte-dataset-evaluation). Reranking and retrieval selection do not become truth oracles merely because they produce scores.

[RT-RTE-knowledge-admission](#rt-rte-knowledge-admission) distinguishes source storage, asynchronous queueing and indexed enablement from enrichment completion. Wiki ingestion separately calls a chat model through prompt templates and bounded transient-error retries (SRC-1, `internal/application/service/wiki_ingest.go`); the boundary retains the pending-task recovery path. These direct model calls do not run through the foreground tool approval gate. Wiki content admission/revision details, connector synchronization, parser internals, multimodal enrichment, graph construction, alternate indexing backends and memory extraction are included responsibilities but not fully traced in this runtime member. Their missing details prevent exhaustive admission, recovery or knowledge-quality conclusions, not a bounded positive account of the selected paths.

The product's source and shipped prompts change through repository/deployment replacement; this report does not infer an agent-admitted product-code update. Runtime customization can select models, tool grants and prompt text. The inspected installer does admit capability/production changes: checked dependencies and files become a durable snapshot used by later sessions. [RT-BAP-skill-image](#rt-bap-skill-image) names that behavioral channel. Host-specific installation/removal, full rollback APIs, release automation and migrations remain uninspected for equivalent guarantees. No learning, theory-building or exercised self-improvement conclusion is derived from installation, persistence or a repair loop alone.

## Shared records

### Components

#### RT-CMP-chat-model
Label: Configured chat model

Source-native identity: chat.Chat selected from the agent's effective model ID, also used by compaction and resolved separately for the installer. Form: distributed-parametric model; symbolic connection/configuration is not its weights. Substrate: external provider or local Ollama service; Go holds an adapter, not inspectable parameters. SRC-1, `internal/models/chat/chat.go`, maps stored model configuration and dispatches local/remote protocols; `internal/application/service/session_agent_qa.go` resolves the agent model.

> ModelName: m.Name,
> Source: m.Source,
> Provider: m.Parameters.Provider,
> --- `internal/models/chat/chat.go`

Parameters during operation: inspected factories expose inference, not a weight-update step; provider-internal mutability is uninspected. Exact parameter version pinned: no exact weight identity established by model ID/name/configuration. Mutable endpoint can resolve to another model: afforded by configurable BaseURL/name and external endpoint ownership; actual switching unobserved. The repository pin freezes the adapter, not the selected model. This applies to foreground, summary, wiki and installer chat roles; actual deployments may choose different models.

#### RT-CMP-embedding-model
Label: Configured embedding model

Source-native identity: embedding.Embedder selected by KB EmbeddingModelID. Form: distributed-parametric; returns numerical vectors. Substrate: provider/Ollama parameters outside the Go process; vectors enter retrieval/index state, distinct from weights. SRC-1, `internal/models/embedding/embedder.go`, and query consumer `internal/application/service/knowledgebase_search.go`.

> ModelName: m.Name,
> Dimensions: m.Parameters.EmbeddingParameters.Dimension,
> --- `internal/models/embedding/embedder.go`

Parameters during operation: inference calls inspected, provider weight changes uninspected. Exact parameter version pinned: not established; name/ID/dimensions are not parameter digests. Mutable endpoint can resolve another model: afforded by BaseURL/name configuration; actual drift unobserved. Query dimension validation can catch dimension mismatch, not all semantic model drift. Full document-vector provenance is left to the memory account.

#### RT-CMP-rerank-model
Label: Configured rerank model

Source-native identity: rerank.Reranker resolved from agent RerankModelID when knowledge_search is effective. Form: distributed-parametric scoring; symbolic thresholds and ordering rules are separate. Substrate: external protocol endpoint. SRC-1, `internal/models/rerank/reranker.go`, `internal/application/service/session_agent_qa.go`, `internal/agent/tools/search_knowledge.go`.

> Model: config.ModelName,
> BaseURL: config.BaseURL,
> ModelType: types.ModelTypeRerank,
> --- `internal/models/rerank/reranker.go`

Parameters during operation: no weight update exposed in the inspected factory/tool path; provider internals uninspected. Exact version pinned: not established. Mutable endpoint can resolve another model: afforded by configurable model/URL, not observed. Rerank failure can use raw retrieval order, so model scoring is not an invariant prerequisite to every returned search result.

#### RT-CMP-vlm-model
Label: Configured VLM model

Source-native identity: configured VLMModelID image describer, distinct from vision-capable foreground chat. Form: distributed-parametric; output descriptions are natural-language content. Substrate: remote provider or local model service. SRC-1, `internal/models/vlm/vlm.go`, `internal/application/service/agent_service.go`.

> ModelName: m.Name,
> Source: m.Source,
> InterfaceType: ifType,
> --- `internal/models/vlm/vlm.go`

Parameters during operation: inference wired; provider changes uninspected. Exact version pinned: not established by model name/ID. Mutable endpoint can resolve another model: afforded by configurable BaseURL/name. Agent service supplies original images to vision chat or a VLM description fallback; this does not establish description fidelity. Other optional models/backends are not exhaustively enumerated here.

### Operative objects

#### RT-OBJ-agent-config
Label: AgentConfig execution configuration

Source-native identity: types.AgentConfig built from CustomAgent and per-request scope. Form: symbolic fields for allowed tools, MCP selection, context/iteration limits, search targets and workspace selection. Substrate: caller-owned Go structure, populated from persisted agent configuration and request resolution. Natural-language system-prompt text is assessed separately. SRC-1, `internal/application/service/session_agent_qa.go`, `internal/application/service/agent_service.go`.

> allowedTools := tools.EffectiveAllowedTools(config.AllowedTools)
> --- `internal/application/service/agent_service.go`

This is a built-in tool grant input, not a complete isolation boundary. The same construction adds separately conditioned MCP, sandbox, attachment and browser capabilities. SharedAgentReadOnly removes wiki writes, and WritableKBIDs narrows writable wiki scope in the inspected registration path; exhaustive downstream write authorization is not established.

#### RT-OBJ-system-prompt
Label: Agent system prompt

Source-native identity: resolved systemPromptTemplate, default prompt templates and runtime-injected instructions. Form: natural-language instructions interpreted by the model, distinct from symbolic schema/tool controls. Substrate: shipped YAML and configured text, composed into current Go chat messages. SRC-1, `internal/application/service/agent_service.go`, `internal/agent/engine.go`, `config/prompt_templates/agent_system_prompt.yaml`.

> systemPromptTemplate = config.ResolveSystemPrompt(config.WebSearchEnabled)
> --- `internal/application/service/agent_service.go`

The caller also supplies recalled memory, attachment manifests and quoted context. Scope envelopes are injected at model calls rather than persisted onto user messages. The shipped evidence-verification instruction quoted in boundary is a policy request, not executable verification of answer truth.

### Routes

#### RT-RTE-agent-turn
Label: HTTP agent turn

Endpoints/progression: chat POST → handler parse/persist/live run → AgentQA → constructed engine Execute or Resume → round/model/tool loop → EventBus/SSE → assistant completion. Owner: handler owns turn storage/coordination; session service resolves context and grants; engine owns round transitions; model proposes content/actions. SRC-1, `internal/router/routes_chat.go`, `internal/handler/session/qa.go`, `internal/application/service/session_agent_qa.go`, `internal/agent/engine.go`.

> session, err := h.sessionService.GetOwnedSession(ctx, sessionID)
> --- `internal/handler/session/qa.go`

> _, err = engine.Execute(ctx, sessionID, req.AssistantMessageID, agentQuery, llmContext, agentImageURLs)
> --- `internal/application/service/session_agent_qa.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE thought/tool/answer events and application error events; HTTP request admission is distinct from asynchronous completion.
- Later read-back: stored assistant/user messages and AgentSteps rebuild multi-turn history; eligible checkpoints replace covered earlier history; memory recall is separately application-owned.
- Delegated visibility: selected messages, instructions, tool definitions, images/descriptions and results reach the provider; selected attachments reach the workspace. No complete DB is sent merely by owning a session.
- Selection predicate: owner-scoped session, resolved agent and search targets; MultiTurnEnabled enables history; memory preference controls recall; vision capability selects image versus description supply.
- Invalidation or expiry: new turns supersede waiting suspended runs; cancellation stops work and drops queued follow-ups; exact distributed lease/queue TTL guarantees are uninspected.
- Activation or effect: tool execution and message writes are implemented effects; prompt delivery does not establish model obedience or correct answers.
- Evidence limits: no live turn observed; handler guards do not automatically establish all direct service/client authorization.

Decision roles: user supplies an open task and may steer/stop; model proposes tools/answer; code enforces selection, validation and loop termination. Answer oracle: no expected answer in the inspected ordinary turn. Operating mode: open requests, not a fixed curriculum. Terminal output may be answer, partial stopped content, suspended prompt, fallback or error. Completion is not successful task fulfillment.

#### RT-RTE-context-rewrite
Label: Context compaction and trimming

Endpoints/progression: estimated context threshold or one-time overflow recovery → compactor → summary plus recent tail → optional tool previews → next model call; eligible summary checkpoint → message repository → later history reload. Owner: engine code triggers/selects; separate chat model proposes summary; code chooses whether reduction is sufficient. SRC-1, `internal/agent/engine.go`, `internal/agent/observe.go`, `internal/agent/compaction/compactor.go`, `internal/application/service/session_agent_qa.go`.

> engine.SetContextCheckpointSink(messageCheckpointSink{repo: s.messageRepo, sessionID: sessionID})
> --- `internal/application/service/session_agent_qa.go`

> // Spend the remaining budget newest-first. A result that cannot fit in
> // full receives the largest head/tail preview that does fit.
> --- `internal/agent/observe.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rewritten chat message list, summary/recent tail and optional previews; not a user answer.
- Later read-back: a checkpoint ending on a stored turn is persisted when the caller installed the sink; later turns can start from it. Trimming alone rewrites model messages without mutating ToolResult objects used for persistence.
- Delegated visibility: summarizer gets selected older history, previous summary and summarization instructions; foreground gets transformed messages rather than all original content.
- Selection predicate: token estimate exceeds threshold; overflow recovery is capped once per turn; keep-recent policy selects what remains; tool-result fallback allocates budget newest-first.
- Invalidation or expiry: exhausted compaction is suppressed at the same message count; new accumulation can enable another attempt. Checkpoint invalidation beyond the inspected caller contract is uninspected.
- Activation or effect: implemented replacement changes later model input; behavioral preservation and quality unobserved.
- Evidence limits: summarizer input may omit oldest messages, fallback is a coarse raw archive, previews are lossy, token estimates can be wrong and provider limits differ.

Context is not a sub-agent work frame: summarization uses a separate model request, returns text and discards its temporary request context. The foreground keeps a summary and recent tail, not live references to everything removed. Trimming keeps call/result pairing and a request to rerun tools; it is not automatic reload. Guidance requests factual summarization. Admission: code admits the returned summary, falls back after failures and saves an eligible checkpoint even when foreground reduction is insufficient. No per-summary human approval or expected-answer oracle is present in the inspected path. These are context transformations, not an attributed formulated-theory revision.

#### RT-RTE-mcp-call
Label: MCP discovery and execution

Endpoints/progression: enabled selected/all tenant services → cached discovery/describe → advertised definitions or catalog reference → direct registered tool/catalog proxy → registry execution → MCPTool policy/approval/OAuth → remote or stdio CallTool → result. Owners: service/config chooses eligible services; catalog binds identities; model selects target/arguments; gate and user decide required approval; external server executes. SRC-1, `internal/application/service/agent_service.go`, `internal/agent/tools/mcp_catalog.go`, `internal/agent/tools/registry.go`, `internal/agent/tools/mcp_tool.go`, `internal/agent/approval/gate.go`.

> return t.registry.execute(ctx, tool, args)
> --- `internal/agent/tools/mcp_catalog.go`

> if policyErr != nil || !enabled {
> return disabledMCPToolResult(policyErr), nil
> }
> --- `internal/agent/tools/mcp_tool.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: discovered metadata/schema or remote tool result, refusal/error, OAuth prompt or approval suspension.
- Later read-back: cached service metadata and persisted approval/run machinery support later discovery/resume; full durability semantics of every broker backend are uninspected.
- Delegated visibility: remote MCP receives resolved target arguments and credentials through its connection, not the whole foreground history; stdio service executes as an external process.
- Selection predicate: tenant-enabled service, agent MCP mode/scope, catalog authorization and live enabled policy; required approval additionally needs configured gate and execution metadata.
- Invalidation or expiry: call-time enabled recheck handles toggles; round-boundary refresh updates definitions; approval wait is bounded or suspends with a snapshot; exact deployment recovery remains unobserved.
- Activation or effect: external tool can act after local eligibility/approval; external transactional effects and actual compliance uninspected.
- Evidence limits: optional checker disables gating; approval branch requires metadata/EventBus; fail-open can be configured; remote reconnect retry lacks a demonstrated idempotency contract.

Admission roles: model proposes call, configured policy can veto, user can reject or replace arguments when approval is required. Replacement arguments are validated again. Guidance: service descriptions/schemas and foreground instructions; approved call records and result can persist in turn history. Operating mode: open agent task with conditional human decision, not an improvement experiment. Answer oracle: schema/policy are execution constraints, not expected task outcome. Recovery: suspended calls resume from answered prompts; completed approval is marked executed, but this does not undo external effects or prove remote exactly-once execution.

#### RT-RTE-sandbox-execution
Label: Workspace shell and file execution

Endpoints/progression: workspace resolution/capabilities → conditional shell/files registration → model tool call → registry → sandbox executor/store; attachment staging precedes shell access. Owners: agent service decides registration, workspace manager supplies capability and isolation, model selects operation. SRC-1, `internal/application/service/agent_service.go`, `internal/application/service/session_agent_qa.go`, `internal/agent/act.go`, `internal/agent/tools/registry.go`.

> if sandboxMgr.GetType() != sandbox.SandboxTypeHost &&
> !config.SkillsEnabled && !config.SkillInstallMode() {
> return
> }
> --- `internal/application/service/agent_service.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: command/file result or failure through the tool pipeline.
- Later read-back: session workspace and durable attachments may be staged/reused; provider persistence and full artifact lifecycle are uninspected. Installer snapshots use the separate admission route below.
- Delegated visibility: workspace gets staged files and selected command/env; it does not automatically receive model conversation. Optional image describer receives tool images.
- Selection predicate: effective workspace backend, advertised executor/store capabilities, remote skills/install entitlement or host exception, selected install directory/environment.
- Invalidation or expiry: turn lease prevents rebuild between calls; stale sandboxes are resolved on subsequent turns after image changes; all backend timeout/destruction guarantees uninspected.
- Activation or effect: executable commands and file writes are available effects, outside the MCP approval path.
- Evidence limits: deployed isolation envelope not established; host, session MicroVM and other remote providers cannot be treated as equivalent merely because they implement a manager interface.

Capability surface differs from current grant set: ordinary remote shell requires entitlement and backend support, host shell has a different gate, and install mode uses a distinct executor. The native browser is registered separately when enabled and not installing, independent of shell/sandbox. Its RPC implementation and callback authorization were not traced. Generic file writes/shell commands are not automatically persistent capability updates; only the inspected installation admission establishes a later image channel. No rollback of arbitrary shell/external effects is established.

#### RT-RTE-rag-answer
Label: Knowledge QA event pipeline

Endpoints/progression: knowledge-chat handler → KnowledgeQA → event list/ChatManage → eventManager.Trigger per stage → references and answer streaming or fallback. Owner: application code chooses stage sequence; retrieval/reranking adapters select evidence; chat model generates answer. SRC-1, `internal/router/routes_chat.go`, `internal/application/service/session_knowledge_qa.go`, `internal/types/chat_manage.go`.

> err := s.eventManager.Trigger(stageCtx, eventType, chatManage)
> --- `internal/application/service/session_knowledge_qa.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: references, reasoning/answer events, fixed/model fallback or stage error; knowledge-search instead returns retrieval results without LLM summarization.
- Later read-back: handler stores turn content and timeline; later session history is available through the application. Detailed RAG history filtering is uninspected here.
- Delegated visibility: each stage receives ChatManage; model receives assembled messages rather than all indexed state; exact evidence transformations in every stage remain uninspected.
- Selection predicate: request/agent search scopes, selected event list and retrieval configuration; ErrSearchNothing selects fallback unless cancellation takes precedence.
- Invalidation or expiry: cancellation returns before empty-search fallback; stale index/content invalidation is left to the memory report.
- Activation or effect: retrieval and message generation wired; relevance, answer grounding and actual citations unobserved.
- Evidence limits: static rag/rag_stream lists differ and do not establish every dynamically composed production sequence; no quality measurements supplied.

Open QA mode has no expected-answer oracle. Code controls stage progression, unlike ReAct's model-selected tool succession. Direct completion/fallback calls are not governed by MCP approval. The evaluator's fixed rag sequence is not evidence of foreground agent behavior.

#### RT-RTE-knowledge-admission
Label: Document knowledge admission

Endpoints/progression: file creation → source storage/knowledge record → processing queue payload → processing/indexing → enabled knowledge, with enrichment possibly pending. Owner: application services and workers; caller supplies source, parser/index machinery transforms it. SRC-1, `internal/application/service/knowledge_create.go`, `internal/application/service/knowledge_process.go`.

> knowledge.EnableStatus = "enabled"
> knowledge.StorageSize = totalStorageSize
> knowledge.ProcessedAt = &now
> knowledge.UpdatedAt = now
> --- `internal/application/service/knowledge_process.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: knowledge row can be returned even after enqueue failure; a stored source is not evidence of successful retrieval admission.
- Later read-back: indexed enabled content becomes eligible for application retrieval; detailed index/backend consumer checks belong to memory analysis.
- Delegated visibility: processing worker receives tenant/KB/knowledge IDs, source path and enrichment flags; parser/provider payload details not fully traced.
- Selection predicate: effective KB processing configuration and worker outcome; indexed enablement is distinct from enrichment completion.
- Invalidation or expiry: enqueue failures mark the row failed; document queue has configured options including bounded retries; all reindex/delete races uninspected.
- Activation or effect: software admits retrieval state without an inspected per-chunk human approval step; actual retrieval benefit unobserved.
- Evidence limits: inspected file queue/finalization path does not prove identical guarantees for manual, URL, connector, graph and multimodal alternatives.

Change admission: caller proposes source content; code stores, parses/indexes and changes availability. Caller identity alone does not establish human authorship or per-content approval. Rejection is possible on processing failure; unchanged source retention differs from usable indexing. Guidance is processing/enrichment configuration, not an expected semantic answer. Mode: open source ingestion. Recovery includes queue retries/failure state; exhaustive rollback is not established. The important countercase is that hasPendingMultimodal or textChunkCount can keep ParseStatusProcessing while EnableStatus becomes enabled. Completion of enrichment therefore cannot be inferred from retrieval availability.

#### RT-RTE-skill-install
Label: Skill dependency installation and image admission

Endpoints/progression: supplied/stored/catalog skill archive → tenant/config install row → maintenance session and isolated install workspace → seeded bundle → installer engine → verification and optional repair → ledger/snapshot → image pointer switch → ready state/stale session marking. Owner: TenantSkillService coordinates; model proposes dependency commands/report; code verifies and admits snapshot. SRC-1, `internal/application/service/tenant_skill_install.go`, `internal/application/service/tenant_skill_verify.go`, `internal/application/service/tenant_skill_runtime_verify.go`.

> notes, verifyErr := s.verifySkill(ctx, job.mgr, job.sess.ID, job.skillDir, job.bundle)
> --- `internal/application/service/tenant_skill_install.go`

> prompt = buildRepairPrompt(job.skillDir, gate)
> --- `internal/application/service/tenant_skill_install.go`

> if err := s.switchImagePointer(ctx, tenantID, configID, ref.ID, generation, builtFingerprint); err != nil {
> s.abandonSnapshot(cleanupBase, tenantID, mgr, installRowID, ref.ID)
> return err
> }
> pointerSwitched = true
> --- `internal/application/service/tenant_skill_install.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: initial skill ID/progress; background installation produces done/failed state, retained transcript and verifier notes.
- Later read-back: snapshot pointer changes later workspace startup; skill files, install report and declared environment requirements persist; maintenance transcript remains for diagnosis.
- Delegated visibility: installer gets seeded files, platform instructions, administrator guidance and verification failures; repair turn receives gate findings without replaying full conversation history.
- Selection predicate: tenant/config/archive ownership and serialized config lock; verification success plus renewed ownership/lock checks precede snapshot/pointer admission.
- Invalidation or expiry: newer row ownership or lost lock prevents admission; terminal ready writes retried; image changes mark sessions stale; provider-account fingerprint mismatch blocks growing an unusable image.
- Activation or effect: snapshot switch is an implemented capability/production-state change reaching later sessions; actual successful skill execution and improvement unobserved.
- Evidence limits: remote snapshot path inspected; host install path not established equivalent; declared CLI checks do not prove all required capabilities or meaningful end-to-end skill behavior.

Trigger/proposal: an upload/catalog install/retry initiates dependency installation; model performs setup within supplied scope, rather than reconstructing the source bundle. Guidance includes skill documentation/manifests, platform runtime prerequisites and administrator instructions preserved in repair. Code first checks tree, declared dependencies, script parsing and runtime prerequisites. Explicit blockers reject admission; required commands are checked with command -v. Repairable findings feed another installer turn within the bounded verification-round budget. Unrepairable failure or exhausted budget vetoes pointer movement; human initiation is not approval of every proposed change. Expected outcome/oracle: executable/tree/dependency checks, partially specified by bundle and model report; no complete functional oracle. Mode: bounded setup/repair, not open-ended optimization.

Recovery/rollback: pre-switch failures leave the prior pointer; unpublished snapshots can be abandoned; prior snapshots remain in a ledger and are superseded rather than automatically deleted. Post-switch bookkeeping failure is distinct from failed installation. Full explicit rollback selection APIs are uninspected. Retained output changes dependencies/environment and future skill availability; it does not by itself establish learning or self-improvement. The loop uses specific verification failures, but no formulated explanatory theory and content-directed theory criticism are established by these setup records.

#### RT-RTE-dataset-evaluation
Label: Dataset QA evaluation

Endpoints/progression: evaluation request → evaluation-specific KB/dataset → background parallel QA pairs → fixed rag pipeline → retrieval/rerank/response metrics → in-process evaluation result. Owner: EvaluationService and HookMetric; code supplies question/reference pair, models produce responses. SRC-1, `internal/application/service/evaluation.go`, `internal/types/chat_manage.go`.

> metricHook.recordQaPair(i, qaPair)
> metricHook.recordSearchResult(i, chatManage.SearchResult)
> metricHook.recordRerankResult(i, chatManage.RerankResult)
> metricHook.recordChatResponse(i, chatManage.ChatResponse)
> metricHook.recordFinish(i)
> --- `internal/application/service/evaluation.go`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: task/progress and evaluation detail with computed metrics.
- Later read-back: in-process task map supports later result lookup; durable cross-restart evaluation retention not established.
- Delegated visibility: each worker gets cloned ChatManage, dataset question and evaluation KB; normal rag stages see their selected state.
- Selection predicate: caller dataset/KB/model choices; fixed rag event list, CPU-based bounded worker concurrency.
- Invalidation or expiry: evaluation KB cleanup and error returns implemented; task-map lifecycle beyond inspected storage uninspected.
- Activation or effect: metrics are computed and exposed, not automatically an admitted model/prompt/product successor in this inspected path.
- Evidence limits: metric formulas/reference fidelity and actual results uninspected; wiring is not a measured quality or causal benefit claim.

Answer oracle: supplied QAPair/dataset provides reference material to the metric hook, not a model-generated judgment alone; precise matching criteria remain uninspected. Mode: bounded dataset evaluation. Computation proposes no successor here; caller chooses candidate models/KB and can use results externally. No per-metric admission or automatic improvement trigger established by this route.

### Claims

#### RT-CLM-evidence-verification
Label: Verify underlying evidence

Claimed operation: agent instructions ask the model to verify exact quotations, numbers and code against underlying passages rather than generated overview/metadata. Source: SRC-1, `config/prompt_templates/agent_system_prompt.yaml`; passage retained in [boundary](boundary.md#boundary-and-evidence). Conclusion status: claimed. Runtime affords document/search tools but does not implement a universal independent truth check on generated answers. The MCP approval gate and skill prerequisite verifier are different checks with different consumers.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-instructions
Label: Prompt instructions to foreground model

Consumer: configured chat model. Channel: composed system/user messages, recalled memory, quoted context, scope envelope and tool descriptions. Force: natural-language policy interpreted by the model; tool schemas/execution eligibility have separate symbolic consumers. Horizon: current and subsequent rounds of a turn; static/configured instructions are rebuilt each turn, stored conversation and checkpoints can carry changed context across turns. SRC-1, `internal/agent/engine.go`, `internal/agent/think.go`, `internal/application/service/session_agent_qa.go`; [RT-OBJ-system-prompt](#rt-obj-system-prompt) and [RT-RTE-context-rewrite](#rt-rte-context-rewrite) supply witnesses. Delivery is wired; obedience/activation unobserved.

#### RT-BAP-skill-image
Label: Installed skill image to later execution

Consumer: workspace resolver/session sandbox and foreground skill/shell execution. Channel: durable snapshot pointer and seeded skill files/dependencies; symbolic configuration selects image, executable material determines available effects, natural-language skill instructions guide model use. Force: executable capability plus model-interpreted instructions, not mere archival text. Horizon: later sessions/turns after stale sandbox resolution. SRC-1, `internal/application/service/tenant_skill_install.go`, `internal/application/service/agent_service.go`, `internal/application/service/session_agent_qa.go`; [RT-RTE-skill-install](#rt-rte-skill-install) supplies admission witness. Image switch and later resolution are wired, but live exercise and causal improvement are unobserved; provider snapshot durability/isolation are external contracts.

## Annotations

none
