---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "nao runtime baseline: analytics chat, delegated and scheduled execution, tool boundaries and context-change admission at the frozen commit."
run-id: AAS-2026-10-14-nao-f9d36a4b7276-01
reviewed-boundary: "0085625a8fd22e4f404b6a3971d153f6b6699479"
---

# nao runtime report

## Runtime account

### Evidence and consequential work

nao encloses an analytics conversation: it builds model instructions from project context, lets a selected model choose tools, executes those tools, streams a response and retains the chat. It also ships context production, scheduled analytics, an MCP interface and a recommendation-to-review-request path. This account uses SRC-1 at the revision in [the boundary](boundary.md). All findings below are implementation or attributed design findings; no target program, example, test or provider was executed. Activation, actual deployed grants, reliability, performance and improvement remain unobserved.

Added source coverage includes the tool resolver, SQL tool, Monty Python tool, Boxlite execution ranges, task tool and explore subagent runner; system-prompt overrides and user-rule loading; automation execution; MCP sub-agent registration; test-agent service and CLI comparison logic; recommendation execution, PR creation and live Git update ranges; CLI sync and Git refresh. These are additional paths in the existing SRC-1 repository, not new sources. Channel-specific policies, warehouse implementation internals, all provider internals and deployment isolation have not been exhaustively inspected.

### Ordinary invocation and next-step ownership

The web path is [RT-RTE-web-chat](#rt-rte-web-chat). An authenticated user submits a message through the web endpoint. Code checks the project role and billing access; the handler checks the budget, creates a chat or verifies ownership before adding/editing a message, reloads the chat and initializes MCP and skills. The service resolves a provider/model and constructs a ToolContext containing user, project and chat identities, context access, environment variables, Azure token, query-result map and artifact accumulators. These are runtime capabilities and state, not just prompt text. SRC-1: `apps/backend/src/routes/agent.ts`, `apps/backend/src/handlers/agent.ts`, `apps/backend/src/services/agent.ts`.

Code owns admission and setup. The remote model owns ordinary next-tool selection and response composition within the exposed tool schema. The AI SDK owns tool-loop progression using nao's supplied tools, stop conditions and callbacks. nao owns tool implementations and effect adapters. A warehouse, external MCP server or sandbox performs the eventual external operation. Successful adapter return is not an independent answer oracle.

> this._agent = new ToolLoopAgent({
> --- `apps/backend/src/services/agent.ts`

The model-visible invocation is not the raw stored transcript. nao settles tool parts, makes web-tool history portable across providers, marks superseded SQL outputs, reloads latest story content and suppresses older duplicate story bodies. It expands a selected skill, citation and table mentions, applies stored compaction, resolves attachments, strips system-role messages from conversation input, converts to model messages and sanitizes tool-call IDs. The standard system prompt combines rules, active memories, context inventories, skills, tool names and connection information. A complete prompt override can bypass this standard composition; user-group restrictions are appended afterward. [RT-OBJ-system-prompt](#rt-obj-system-prompt) and [RT-BAP-project-guidance](#rt-bap-project-guidance) distinguish natural-language direction from executable access controls. SRC-1: `apps/backend/src/services/agent.ts`.

> const selectedSystemPrompt =
> this._systemPromptOverride ?? (await this._buildSystemPrompt(provider, timezone, chatUrl));
> --- `apps/backend/src/services/agent.ts`

The stream supplies an AbortSignal and persists the settled assistant message on completion, including stop reason, error, usage and provider/model identity. Memory extraction is scheduled after sending the agent request, not after proving the response correct; its revision semantics belong to the memory member. New-chat title generation is another asynchronous model call. A map keyed by chat ID tracks live managers in this process; creating another manager for that ID stops the prior manager. This is local coordination, not a demonstrated distributed lock or exactly-once execution contract. SRC-1: `apps/backend/src/services/agent.ts`.

### Working-context control

The main loop calls compaction before each step. Code estimates message tokens plus tool tokens plus reserved output tokens against 75% of the configured context window. Code selects an eligible prefix from the first non-system message up to, but excluding, the last user message. Before the separate model receives it, CompactionLLM strips images and selects messages backward under its own context-window budget, reserving 16,000 output tokens and prompt overhead. Selection stops when the next message or assistant/tool pair does not fit. The whole eligible prefix is replaced even when older material never reached the summarizer. The system instructions and current user-and-following tail remain. The replacement is an assistant summary of selected input, not a reversible compression. A stored compaction marker later reconstructs summary plus recent turns. Compaction failure reports an error event and continues without establishing that the remaining context fits. Before sending a step, nao prunes old reasoning and all suggest-follow-up tool calls and removes empty messages. SRC-1: `apps/backend/src/services/compaction.ts`, `apps/backend/src/agents/compaction/compaction-llm.ts`, `apps/backend/src/utils/ai.ts`, `apps/backend/src/services/agent.ts`.

> const textOnlyMessages = stripImageParts(messages);
> const selectedMessages = selectMessagesInBudget(textOnlyMessages, budget, this._tc);
> --- `apps/backend/src/agents/compaction/compaction-llm.ts`

> const threshold = contextWindow * CONTEXT_WINDOW_COMPACTION_THRESHOLD;
> --- `apps/backend/src/services/compaction.ts`

> const selectedMessages = messages.slice(userMessageBeforeCompactionIdx);
> return [this._createSummaryUIMessage(compactionSummary), ...selectedMessages];
> --- `apps/backend/src/services/compaction.ts`

Documents remain outside the window as named storage paths; images are loaded for inline model delivery. Skill expansion truncates the body to 16,000 characters. These are separate selective-delivery mechanisms, not memory learning. [RT-RTE-explore-task](#rt-rte-explore-task) is a fresh-context frame: only an explicit task prompt and its own system instructions enter, and only its report reaches the parent's model-visible tool result. This resembles a stack frame in context visibility, but it shares ToolContext and access adapters; it is not a separate process or permission principal. Compaction resembles eviction with a lossy retained summary. Paths can support explicit reload, but there is no automatic pointer-following semantics for text omitted from a model window. SRC-1: `apps/backend/src/agents/subagents/run.ts`, `apps/backend/src/agents/tools/task.ts`, `apps/backend/src/services/agent.ts`.

### Forcing routes and limits of guarantees

Four forcing cases qualify the ordinary path: (1) admin-mode and nonstreaming test runs replace important parts of normal context/persistence; (2) MCP offers both an enclosed background chat and host-driven direct tools; (3) task subagents, provider-native web tools and two different Python/code executors widen the execution surface; (4) automations and context recommendations supply noninteractive callers with different stopping and admission rules. These are source inspections, not executed adversarial tests.

**Web access.** Owner: web route/handler. Enforcement points: auth pre-handler, role check and existing-chat owner check. Strength: protocol for this endpoint, not a deployment guarantee. Covered paths: web message creation and editing; admin mode additionally requires admin/context-admin role. Alternate paths: MCP, messaging, automation and tests have their own callers; web checks cannot be projected onto them. External contract: trustworthy authentication/project identity and query semantics. implementation conclusion status: wired. operation conclusion status: uninspected. Evidence: SRC-1, `apps/backend/src/routes/agent.ts`, `apps/backend/src/handlers/agent.ts`.

> if (!userRole || userRole === 'viewer') {
> return reply.status(403).send({ error: 'Viewers cannot send messages' });
> }
> --- `apps/backend/src/routes/agent.ts`

**SQL writes.** Owner: executeQuery. Enforcement point: effective SQL validation before choosing admin, local or warehouse execution. Strength: policy implemented as a rejecting code gate, not an SQL-safety invariant. The dangerous-write setting deliberately changes the grant. Passthrough calls are blocked independently of that setting. Semantic-layer compilation has a special raw-SQL-mode exception; warehouse calls receive table/row/excluded-column enforcement inputs. This does not prove the validators or downstream enforcement correct. Alternate paths include remote MCP tools, networked shell code, direct MCP SQL tools, semantic queries and host/API callers. The inspected gate only warrants conclusions about executeQuery calls, not all possible data mutations. External contract: parser behavior, warehouse permissions and adapter enforcement. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1: `apps/backend/src/agents/tools/execute-sql.ts`.

> const writePermEnabled = context.agentSettings?.sql?.dangerouslyWritePermEnabled ?? false;
> if (!writePermEnabled && !(await isReadOnlySqlQuery(effectiveSql))) {
> --- `apps/backend/src/agents/tools/execute-sql.ts`

**Context files versus writable outputs.** Owner: built-in write tool. Enforcement point: dispatch accepts storage/story mounts and rejects other paths. Strength: protocol for that tool. It cannot establish immutability of the context across deployment, synchronization, recommendations, external editors or remote tools. Ordinary chat can write output files/custom-story drafts without thereby gaining an edit-to-RULES capability. External contract: mount and storage scoping helpers. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1: `apps/backend/src/agents/tools/write.ts`, `apps/backend/src/agents/tools/index.ts`.

> throw new Error(`Cannot write '${file_path}': ${writableTargetsHint()}. Project context files are read-only.`);
> --- `apps/backend/src/agents/tools/write.ts`

**Execution envelope.** Capability surface and current grant differ. getTools enables task only behind BETA_SUBAGENTS_ENABLED, Python and sandbox execution only when available and enabled in project experimental settings, MCP only for configured/allowed servers, semantic queries according to semantic-layer mode, and maps/stories according to flags and features. Resolver allowlists filter built-ins but deliberately preserve extraTools. These are caller-configurable surfaces; no universal human confirmation barrier is established. SRC-1: `apps/backend/src/agents/tools/index.ts`.

Monty execute_python runs with resource limits and a filtered virtual filesystem, exposing only declared external functions. Boxlite execute_sandboxed_code instead accepts Python or shell, optional packages, input data and saved output files. It creates a network-enabled box, turns jailer off when the host is detected as Docker, injects the user's/project's secrets and redacts returned stdout/stderr. Timeout evicts a box. These adapters are materially different isolation claims. Redacting returned strings is not a proof against network or encoded-secret exfiltration. Owner: tool implementation plus Boxlite/Monty. Strength: best effort at the inspected adapter boundary; deployed VM/container isolation is uninspected. External contract: those runtimes' enforcement and deployment configuration. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1: `apps/backend/src/agents/tools/execute-python.ts`, `apps/backend/src/agents/tools/execute-sandboxed-code.ts`.

> networkEnabled: true,
> jailerEnabled: !isDocker,
> --- `apps/backend/src/agents/tools/execute-sandboxed-code.ts`

> const [command, args] = language === 'python' ? [PYTHON_BIN, ['-c', code]] : ['sh', ['-c', code]];
> --- `apps/backend/src/agents/tools/execute-sandboxed-code.ts`

### Alternate callers, evaluation and change admission

[RT-RTE-mcp-chat](#rt-rte-mcp-chat) drains a persisted chat in the background and returns either an answer or a polling handle. This is distinct from the task subagent: it has a durable chat and can be continued. The same MCP source describes a host-driven direct-tool alternative without chat retention. Full direct-tool authorization and remote tool internals remain uninspected; claims of chat persistence or web approval do not extend to it. Messaging callers also create agents: located creation sites in Slack, Teams, Telegram, WhatsApp and Mattermost reuse the enclosing service, but transport identity and channel-specific policy require separate inspection. SRC-1: `apps/backend/src/mcp/tools/sub-agent.ts`, `apps/backend/src/services/slack.ts`, `apps/backend/src/services/teams.ts`, `apps/backend/src/services/telegram.ts`, `apps/backend/src/services/whatsapp.ts`, `apps/backend/src/services/mattermost.ts`.

[RT-RTE-automation-run](#rt-rte-automation-run) runs as the automation owner, adds configured outbound integration tools and validates that required tools were called. Calling an integration is not a reference answer or a guarantee that the remote action happened exactly once. The standard service has model, budget and billing checks, but different callers can supply preverified billing/budget options. The interactive stop conditions are follow-up/clarification calls; excludeFollowUps switches to a step budget (20 by default). This prevents treating the interactive policy as universal. SRC-1: `apps/backend/src/services/agent.ts`, `apps/backend/src/handlers/automation.handler.ts`.

[RT-RTE-test-answer](#rt-rte-test-answer) uses the generate path, which returns structured run results without the streaming message-persistence callback. Verification is a separate direct generateText call producing SQL over already-fetched rows. It can repair a failed SQL statement once. The CLI checks tool assertions and compares verification rows with expected rows; model judgment alone is not the answer oracle. No benchmark was run here. SRC-1: `apps/backend/src/services/test-agent.service.ts`, `apps/backend/src/services/agent.ts`, `cli/nao_core/commands/test/runner.py`.

[RT-RTE-context-recommendation](#rt-rte-context-recommendation) examines retained usage/feedback and context costs with a restricted agent, then reconciles and retains recommendations. Optional automatic PR creation is not live admission: it works in a disposable clone and sets status applied after opening a PR. Reconciliation also writes applied for a resolve action without establishing a PR. Thus applied alone establishes neither a review request nor deployment. [RT-RTE-context-delivery](#rt-rte-context-delivery) distinguishes the actual live-refresh mechanisms: UI live pull uses fast-forward-only merge, Python refresh and container startup can hard-reset to fetched content, and CLI sync writes configured provider outputs and renders templates. Thus a universal non-destructive-update claim is false. Content quality approval, remote repository merge policy and any downstream benefit are unestablished. Source-native instruction/knowledge revisions are left to the relevant specialists; this runtime account locates the executable admission points. SRC-1: `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/services/context-pr.service.ts`, `apps/backend/src/services/context-explorer-git/live-context.service.ts`, `cli/nao_core/context/git.py`, `docker/entrypoint.sh`, `cli/nao_core/commands/sync/__init__.py`.

## Shared records

### Components

#### RT-CMP-agent-model
Label: Selected analytics agent model

Source-native identity: modelConfig.model and modelSelection passed to AgentManager and reused by agent callers. Form: distributed-parametric; storage substrate: provider-hosted model weights, not stored in this repository. Parameters changing during operation: no nao-side training/update step appears in the inspected invocation and provider-resolution path; provider-side changes are uninspected. Exact weight version pinned: not established; nao stores a configurable provider/modelId and optional baseURL, not a weight digest. Mutable endpoint resolving to another model: afforded by configurable endpoints and provider-controlled IDs; actual endpoint behavior uninspected. This includes independently selected explore models; they have the same unresolved provider fixity, not necessarily the same model identity. SRC-1: `apps/backend/src/services/agent.ts`, `apps/backend/src/utils/llm.ts`, `apps/backend/src/agents/subagents/run.ts`.

> ...(config.baseUrl && { baseURL: config.baseUrl }),
> --- `apps/backend/src/utils/llm.ts:145-157`

#### RT-CMP-compaction-model
Label: Compaction model

Source-native identity: resolved CompactionLLM, selected from the configured compaction model or an annotation-model fallback. Form: distributed-parametric; substrate: external provider weights. Parameters changing during operation: no update operation is wired in the inspected compaction service; provider internals uninspected. Exact version pinned: no weight-level pin established. Mutable endpoint resolving to another model: possible through the shared provider resolver; deployment/provider alias state uninspected. Its lossy text output, not changed weights, replaces the eligible history prefix. Its input is image-stripped and budget-selected, so replacement does not imply the whole replaced prefix reached this model. SRC-1: `apps/backend/src/services/compaction.ts`, `apps/backend/src/agents/compaction/compaction-llm.ts`, `apps/backend/src/utils/ai.ts`, `apps/backend/src/utils/llm.ts`.

> const pinned = await resolveDefaultModelSelection(projectId, 'compaction');
> --- `apps/backend/src/services/compaction.ts`

#### RT-CMP-verification-model
Label: Test verification model

Source-native identity: modelConfig resolved inside runVerification, which can use a selected or project-default provider/model. Form: distributed-parametric; substrate: provider weights. Parameters changing during operation: no local training mechanism in the inspected evaluator; provider internals uninspected. Exact weight version pinned: unestablished; modelId configuration is not proof of immutable weights. Mutable endpoint resolution: afforded by the shared configurable provider resolver. Separate from the agent's judgment role even when selected IDs coincide. SRC-1: `apps/backend/src/services/test-agent.service.ts`, `apps/backend/src/utils/llm.ts`.

### Operative objects

#### RT-OBJ-tool-context
Label: ToolContext

Source-native identity: per-manager ToolContext built by buildToolContext/_buildContextBase. Form: symbolic identifiers, grants and maps with fixed code consumers; contains separately interpreted text/data values. Substrate: process memory, initialized from project queries and context-access resolution. Carries userId, projectId, chatId, projectFolder, agentSettings, context grants, credentials, query results and generated artifacts. It is shared with explore subagents, so conversation isolation does not create a different authority principal. Evidence: SRC-1, `apps/backend/src/services/agent.ts`, `apps/backend/src/agents/subagents/run.ts`.

> experimental_context: context,
> --- `apps/backend/src/agents/subagents/run.ts`

#### RT-OBJ-system-prompt
Label: Project system prompt

Source-native identity: AgentManager._systemPrompt, standard SystemPrompt or project override from agent/prompts. Form: natural language interpreted by the model; the placeholder substitution and provider/file selection are symbolic rules, not semantic enforcement. Substrate: project filesystem plus assembled process string and model request. RULES.md, memories and inventories feed the default composition; a non-placeholder override replaces it. Restrictions are appended separately. SRC-1: `apps/backend/src/agents/system-prompts.ts`, `apps/backend/src/agents/user-rules.ts`, `apps/backend/src/services/agent.ts`.

> if (override && !hasNaoPromptPlaceholder(override)) {
> return override;
> }
> --- `apps/backend/src/services/agent.ts`

### Routes

#### RT-RTE-web-chat
Label: Web analytics chat

Endpoints/progression: POST agent route → handler → AgentService.create → AgentManager.stream → model/tool loop → settled-message upsert. Owner: authenticated requesting user for intent; nao for admission, orchestration, execution dispatch and persistence. Model decision role: next tool, SQL/artifact arguments and final text. Code decides grants, context transformations, budget and stop conditions. Mode: open analytics request; answer oracle: none supplied by this ordinary route. User can stop or edit and supersede messages; this is not per-tool approval. Form: natural-language instructions/questions, symbolic tool schemas/calls and structured transcript parts. Context/state/effects: project guidance and history, scoped ToolContext, warehouse/local operations and generated outputs.

- Immediate return: SSE/UI message chunks and terminal answer/tool parts; new-chat and user-message identity events.
- Later read-back: handler reloads stored chat; latest compaction and current project guidance transform the next invocation. Memory extraction is scheduled separately.
- Delegated visibility: task receives an explicit prompt and fresh model context, not the full parent transcript; remote tools receive arguments through their adapters.
- Selection predicate: caller's chat or new chat; configured/selected model; resolved project toolset and access; latest stored transcript with mentioned skill/table expansion.
- Invalidation or expiry: edited messages supersede a suffix; compaction replaces the eligible old model-visible prefix with a summary of image-stripped, budget-selected input, potentially dropping older material before summarization; old reasoning/follow-up calls are pruned. Process manager is disposed on finish/replacement.
- Activation or effect: code dispatches model-selected exposed tools and upserts the settled response; reliable model compliance and successful external effects are not observed.
- Evidence limits: implementation inspected, no execution traces; downstream warehouse/provider behavior and full alternate-channel authorization remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/routes/agent.ts`, `apps/backend/src/handlers/agent.ts`, `apps/backend/src/services/agent.ts`, `apps/backend/src/services/compaction.ts`.

> const [settledMessage] = await settleToolParts([e.responseMessage]);
> await chatQueries.upsertMessage({
> ...settledMessage,
> --- `apps/backend/src/services/agent.ts`

#### RT-RTE-explore-task
Label: Explore task frame

Endpoints/progression: foreground task tool → resolve definition/model → streamText with fresh messages and explore read/list/grep/search → report tool output. Owner: foreground model proposes task and explicit inputs; code selects definition and enforces its toolset and 15-step cap; child model chooses context lookup and report. Mode: bounded delegated investigation within an open request. Answer oracle: none. A narrower code-defined toolset replaces the parent surface, but ToolContext is shared.

- Immediate return: streamed progress snapshots and final report; toModelOutput exposes output.report as text.
- Later read-back: report can persist as a parent tool result and enter subsequent parent history; child transcript is not supplied to the parent model by this tool output.
- Delegated visibility: own system prompt plus explicit prompt only; project inventories and truncated rules are constructed for explore; shared ToolContext gives access adapters, not parent conversation visibility.
- Selection predicate: foreground-supplied subagent_type, prompt and optional model_id; task availability requires the beta flag.
- Invalidation or expiry: frame ends at return, abort or step budget; no child replay route established in the inspected runner.
- Activation or effect: child executes context-reading tools and returns a report; parent reliance on its content is requested/afforded, not observed.
- Evidence limits: no executed delegation or demonstrated context/cost benefit; shared-context grants and user-rule rendering deserve separate security review.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/agents/tools/task.ts`, `apps/backend/src/agents/subagents/run.ts`, `apps/backend/src/agents/subagents/explore.ts`, `apps/backend/src/agents/tools/index.ts`.

> return [systemMessage, { role: 'user', content: prompt }];
> --- `apps/backend/src/agents/subagents/run.ts`

> toModelOutput: ({ output }) => ({ type: 'text', value: output.report }),
> --- `apps/backend/src/agents/tools/task.ts`

#### RT-RTE-mcp-chat
Label: MCP analytics background chat

Endpoints/progression: ask_nao → initialize MCP/skills → buildChatContext → create agent → start background stream → race completion against 45-second response budget → get_nao_answer polling. Owner: MCP caller supplies question; ctx supplies project/user; nao runs and retains enclosed chat. Child model owns ordinary next steps as in the web loop. Mode: open request, optionally continued clarification; answer oracle: none. This is not the ephemeral explore frame.

- Immediate return: complete/needs_clarification answer or running status with chatId and URL; complete payload includes text, query summaries and stories.
- Later read-back: chatId continuation and polling; chat is retained for UI use. Full restart recovery of live background bookkeeping is uninspected.
- Delegated visibility: calling host receives answer payload rather than the entire internal reasoning/tool transcript; the durable chat is separately visible in nao.
- Selection predicate: supplied/new chat and ctx principal; configured sub-agent model or project chat default; default tools except display_map.
- Invalidation or expiry: sync budget returns a handle rather than stopping the run; retention/expiry of background-run bookkeeping is uninspected in this account.
- Activation or effect: same enclosed tools may query and author outputs; no execution supplied.
- Evidence limits: direct MCP tools are a material host-driven alternative; their whole authorization/effect chain was not traced, and chat-persistence conclusions do not cover them.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/mcp/tools/sub-agent.ts`, `apps/backend/src/agents/tools/index.ts`.

> const ASK_NAO_SYNC_BUDGET_MS = 45_000;
> --- `apps/backend/src/mcp/tools/sub-agent.ts`

> const runPromise = runAskNaoInBackground(agent, uiMessages, chat.id, naoChatUrl);
> --- `apps/backend/src/mcp/tools/sub-agent.ts`

#### RT-RTE-automation-run
Label: Scheduled automation execution

Endpoints/progression: finishAutomationRun → create owner chat → initialize configured MCP/skills → create agent with outbound integration tools → drain/persist stream → inspect expected integration calls → complete/fail run. Owner: automation.userId; code supplies stored prompt/integrations and judges required-call presence; model chooses calls/content. Mode: repeated configured analytics task, not an optimization experiment. Answer oracle: no answer reference; required-tool names are a structural completion check. Admission of external effects occurs through configured integration tools; a separate per-call human decision is not established here. Trigger is a run of the configured automation; guidance is the rendered stored prompt. Rollback of outbound effects is uninspected; marking a run failed does not imply undoing an action.

- Immediate return: retained automation-run status and integration results, with partial UI messages persisted while draining.
- Later read-back: run chat/status and stored automation configuration remain available; recurrent task output influencing later model decisions is not established by retention alone.
- Delegated visibility: provider/tool adapters receive selected arguments; the web UI can show partial persisted chat snapshots.
- Selection predicate: automation owner/project, configured model or default, enabled MCP server list and configured integrations.
- Invalidation or expiry: manager finishes/disposes; failure records an error; external-effect expiry/reversal is uninspected.
- Activation or effect: integration tools can perform outbound actions; completion checks their recorded presence, not answer truth or exactly-once delivery.
- Evidence limits: scheduler admission and every integration body are not inspected here; no observed scheduled run.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/handlers/automation.handler.ts`, `apps/backend/src/services/agent.ts`.

> const missingTools = expectedTools.filter((tool) => !calledTools.has(tool));
> --- `apps/backend/src/handlers/automation.handler.ts`

#### RT-RTE-context-recommendation
Label: Context recommendation and review request

Endpoints/progression: manual/scheduled run → retained usage/feedback/cost inputs → restricted model run and collectors → trigger-reference repair/reconciliation → DB transaction → optional automatic PR opening. Owner: project configuration and first project admin identity for runtime principal; model proposes recommendations/edits; deterministic reconciliation selects persisted actions. Conditional autoCreatePrs supplies software admission to PR creation without per-content human approval. Remote repository reviewers can reject/close the proposal; live admission is a different route. Guidance: dedicated recommendation prompt, existing findings, expensive context files and optional custom instructions; ordinary default system guidance is replaced because it is the object being examined. Mode: bounded diagnostic pass over a time window. Answer oracle: no expected correct patch; usage/feedback are evidence inputs, not independent truth labels. Rollback/recovery: failed run recorded; disposable PR clone removed; branch/PR reversal and rejected content handling are not fully traced.

- Immediate return: runId and retained completion/failure state; recommendation records and optional PR links.
- Later read-back: future passes load reconcilable recommendations and dismissed fingerprints; PR content can only become live context through separate repository/admission paths.
- Delegated visibility: restricted agent sees the diagnostic prompt and read/query tools, not ordinary memories/rules as authoritative default instructions; remote Git receives proposed file changes in a branch.
- Selection predicate: period, configured recommendation model, existing recommendations, cost flags and repository availability; auto-PR eligibility requires patch edits, no existing PR and supported repository targets.
- Invalidation or expiry: reconciliation handles recorded/resolved/dismissed findings; failed PR creation is logged and skipped; live context is not mutated by the PR clone.
- Activation or effect: DB recommendation changes and PR creation are wired. Reconciliation resolve actions write status applied; automatic PR creation separately writes applied after opening a PR. The status alone therefore establishes neither PR creation nor merge, deployment, model reliance or better answers.
- Evidence limits: no run or beneficial update observed; content-level criticism and theory-builder assessments are left to specialists rather than inferred from the diagnostic label.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/services/context-pr.service.ts`.

> { excludeFollowUps: true, builtinToolAllowlist: ['read', 'grep', 'list', 'search'] },
> --- `apps/backend/src/services/context-recommendations.service.ts`

> } else if (action.kind === 'resolve') {
> await crQueries.updateRecommendation(
> action.id,
> { status: 'applied', statusChangedAt: new Date() },
> executor,
> );
> }
> --- `apps/backend/src/services/context-recommendations.service.ts`

> await crQueries.setRecommendationStatus({ id: rec.id, projectId, status: 'applied', userId });
> --- `apps/backend/src/services/context-pr.service.ts`

#### RT-RTE-context-delivery
Label: Context synchronization and live delivery

Endpoints/progression: CLI sync writes configured provider outputs and renders Jinja templates; deployment admits local/Git/API context; scheduled Python refresh fetches Git content; UI live-update service fetches and fast-forwards. Owner: operator/configuration chooses source/provider; software admits resulting bytes under that mechanism; human authorship/review of each remote change is unresolved. Proposal: metadata/docs/templates or repository revision. Rejection ability: configuration/provider checks and Git guards can fail; no semantic answer-quality gate established. Recovery: sync records per-provider failure and continues, refresh raises/logs failures, UI reports Git failures; old/new commit reporting aids diagnosis but does not establish automatic semantic rollback. Guidance persists as project files consumed by later prompt construction and read tools. Mode: refresh/build rather than candidate-quality comparison. Answer oracle: none established.

- Immediate return: sync summary, refresh changed flag or live-update result with commit/file differences.
- Later read-back: subsequent agent construction rereads project guidance/inventories; tool reads consume delivered context. Current managers are not proven to hot-rebuild their already constructed system strings.
- Delegated visibility: remote Git supplies selected branch content; configured sync providers supply their outputs; semantic correctness remains outside these byte-admission checks.
- Selection predicate: configured source, repository/branch/subpath or selected provider/connection/schema/table; sync --select scopes databases without deleting the unselected remainder by its declared contract.
- Invalidation or expiry: live pull fast-forwards; Python Git refresh hard-resets when fetched content differs; container startup can reset to FETCH_HEAD. These are different replacement policies, not one non-destructive guarantee.
- Activation or effect: live filesystem context changes can reach subsequent model inputs; successful deployment, subsequent behavioral dependence and quality improvement are unobserved.
- Evidence limits: provider-specific synchronization and API-context delivery are not fully traced; no operational refresh supplied; Git governance and source trust remain external contracts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `cli/nao_core/commands/sync/__init__.py`, `cli/nao_core/context/git.py`, `apps/backend/fastapi/main.py`, `docker/entrypoint.sh`, `apps/backend/src/services/context-explorer-git/live-context.service.ts`, `apps/backend/src/services/agent.ts`.

> runGit(repository.repositoryRoot, ['merge', '--ff-only', 'FETCH_HEAD'], GIT_OPERATION_TIMEOUT_MS);
> --- `apps/backend/src/services/context-explorer-git/live-context.service.ts`

> ["git", "reset", "--hard", "FETCH_HEAD"],
> --- `cli/nao_core/context/git.py`

#### RT-RTE-test-answer
Label: Test answer extraction and comparison

Endpoints/progression: TestAgentService.runTest → temporary chat structure → agent.generate → model verification SQL over collected query results → DuckDB execution with one repair opportunity → CLI assertions/data comparison. Owner: test author supplies prompt, expected SQL/data contract and tool assertions; analytics model generates answer; verifier model extracts SQL; deterministic code compares returned data. Mode: bounded evaluation, not ordinary open chat. Answer oracle: caller/test expected rows and columns used by CLI; the verifier model is not itself the oracle. No product change is automatically admitted by this inspected path.

- Immediate return: answer/steps/queryResults/usage/cost/duration; verification data/sql/error and CLI pass/fail comparison.
- Later read-back: inapplicable — this runTest path intentionally uses generate without streaming chat upsert; retention of evaluator reports is outside the inspected route.
- Delegated visibility: verifier receives built verification messages and query-result descriptions; actual answer extraction runs against already fetched result tables rather than requerying the warehouse.
- Selection predicate: test prompt/model selection, expected columns, available queryResults; no results produces a verification error.
- Invalidation or expiry: temporary manager disposed in finally; failed verification SQL prompts a correction up to two attempts; no successful SQL yields a data/error result.
- Activation or effect: verification SQL executes over stored rows and CLI comparison applies expected-column, row-count, normalization, sorting and tolerance rules; no execution or test success established here.
- Evidence limits: provenance/quality of test expectations and evaluation coverage unestablished; model extraction may distort an answer, so comparison is conditional on that extraction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/services/test-agent.service.ts`, `apps/backend/src/services/agent.ts`, `cli/nao_core/commands/test/runner.py`.

> const MAX_VERIFICATION_ATTEMPTS = 2;
> --- `apps/backend/src/services/test-agent.service.ts`

> passed = assertions_passed and data_passed
> --- `cli/nao_core/commands/test/runner.py`

### Claims

#### RT-CLM-context-readonly
Label: Project context read-only claim

Claimed operation: the ordinary write tool says everything outside writable storage/story mounts is read-only. This is a scoped tool contract, not repository-wide context immutability: separate synchronization and Git admission mechanisms change project context. SRC-1: `apps/backend/src/agents/tools/write.ts`; compare [RT-RTE-context-delivery](#rt-rte-context-delivery).

> Everything else in the tree is read-only.
> --- `apps/backend/src/agents/tools/write.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-project-guidance
Label: Project guidance to analytics model

Consumer: selected analytics model in AgentManager. Channel: assembled system instructions plus explicit skill/table/citation expansion and context-read tool results. Force: natural-language direction/knowledge, not guaranteed compliance; separate symbolic code gates control tools and effects. Horizon: files and retained inputs can cross sessions, while a constructed manager's system string is per invocation. Delivery may change when rules, override files, skills or context repositories change. A complete system override omits standard instructions/memories/connections; appendAgentUserGroupRestrictions still appends restrictions. This path supplies a mechanism by which admitted guidance can affect later behavior, but no exercised dependence or improvement is demonstrated. SRC-1: `apps/backend/src/services/agent.ts`, `apps/backend/src/agents/system-prompts.ts`, `apps/backend/src/agents/user-rules.ts`.

> instructions: cachedSystemInstructions(this._systemPrompt, this._modelSelection),
> --- `apps/backend/src/services/agent.ts`

## Annotations

none
