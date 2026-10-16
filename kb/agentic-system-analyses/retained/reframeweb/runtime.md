---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ReframeWeb runtime baseline tracing bound user input, BAML and Codex execution, task-scoped effects and saved Store admission at the frozen commit."
run-id: AAS-2026-10-14-reframeweb-cff918d7eb1e-01
reviewed-boundary: 318987dcde9a016f8e3db819ed9a73abf6b3ad81
---

# ReframeWeb runtime report

## Runtime account

### Evidence and consequential work

ReframeWeb surrounds model decisions with a host-owned interaction and effect loop. The shipped CLI starts a voice pipeline; native Store/UI callbacks can also submit text. BAML selects a catalog task, plans and filters graph retrieval, composes task input, chooses between a native model tool runner and a Codex subprocess, checks completion and bounds retries. Work can change conversation state, workspace files, browser/panel resources and saved executable Store configuration. These are implementation findings from SRC-1, not a supplied successful run. The frozen boundary and dependency exclusions remain those of [the boundary](boundary.md#boundary-and-evidence).

The source inspection added in this member covers the Python voice pipeline/processor and callback adapters; BAML task execution, candidate tools and review transformations; tool catalog, attempt ledger and transport configuration; Codex process and sandbox adapters; workspace publication; Store metadata publication/startup/live activation; application task publication; and the Store runtime's typed panel host boundary. Paths are cited beside findings below. All added evidence is **implementation**, except quoted model instructions, which establish requested behavior. No target command, test, provider request or experiment was run. Actual grants, retained database contents, model outputs and deployment isolation are unobserved.

### One ordinary invocation, from admission to return

1. `reframe-agent-host voice-turn` reaches `run_voice_turn_loop` with `VoiceTurnPipeline`; the driver collects results and maps interruption, transcription, memory and other errors to CLI statuses. Audio is transcribed and trigger-routed; text bypasses transcription but enters the same routed-input processor. A mode-switch or ignored utterance can terminate before task selection (SRC-1, `agent-host/pyproject.toml`, `agent-host/src/reframe_agent_host/cli.py`, `agent-host/src/reframe_agent_host/commands/voice_turn.py`, `agent-host/src/reframe_agent_host/voice/turn_processor.py`).
2. For routed input, the pipeline requires the acceptance-time session/conversation binding. Text submission obtains it with `observations.pin()`. Each processor gets a replaced configuration carrying that binding and an observation run ID; a later UI selection does not rewrite that configuration. Store callback authority is tied to a current Store revision, not merely possession of a Store ID (SRC-1, `agent-host/src/reframe_agent_host/voice/pipeline.py`, `agent-host/src/reframe_agent_host/store_host_boundary.py`; [RT-BAP-store-callback](#rt-bap-store-callback)).
3. The processor records the human reply, constructs `VoiceTaskFlowHost`, and calls generated `RunVoiceTurn_async` with callbacks. BAML owns next-step selection, while Python callbacks own database access, retrieval, tools and external processes. Host callback bridging uses `run_coroutine_threadsafe(...).result()` and cancellation registration; it is not an independent model agent (SRC-1, `agent-host/src/reframe_agent_host/voice/turn_processor.py`, `agent-host/src/reframe_agent_host/voice/agent_turn.py`, `agent-host/src/reframe_agent_host/agent_flow/voice_turn_flow.py`, `agent-host/src/reframe_agent_host/voice/task_flow_host.py`).
4. Each BAML cycle loads conversation/session/preferences, available tasks, guidance and machine state. Models choose a task, search hints and search depths. Python returns a retrieved graph; a further model selects memory IDs; `SelectedGraph` and `PromptContexts` intervene before composition. Delivery to the composer therefore is not delivery of the entire retrieved graph. The composed prompt is then passed to the selected execution route. A `magic:do-nothing` task avoids execution altogether (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`; [RT-RTE-request-cycle](#rt-rte-request-cycle)).
5. Without `agent_config`, the host reloads task/provider and task-linked instructions, appends those instructions and invokes BAML's 64-step native tool runner. With `agent_config`, it prepares or reuses an identity-checked workspace and launches a fresh ephemeral Codex execution with task-scoped MCP plus Codex's native tools. These are materially different effect paths, not two names for the same runner ([RT-RTE-model-task](#rt-rte-model-task), [RT-RTE-codex-task](#rt-rte-codex-task)).
6. The host records output data and tool history, then obtains a summary. Normal execution summarizes action history. Agent execution uses the executor's required summary item; it does **not** launch the second model conversation suggested by the comment in `RouteTaskSummary`. The executable `summarize_attempt` and agent prompt agree on this distinction (SRC-1, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`, `agent-host/src/reframe_agent_host/agent_execution/summary.py`, `agent-host/baml_src/ns_voice_turn/agent_routing.baml`, `agent-host/baml_src/ns_task/execution/agent_prompts.baml`).
7. A completion model compares the selected task's output requirement with the summary and current request/conversation. PASS also requires no execution or summary failure. A failure resolver can refine the prompt and retry, or return to task selection. A separate request-completion check can request another cycle. The newest bounded result is returned at the global bound, even if the overall request remains unsatisfied. Candidate guidance is reviewed before the result returns. The Python driver receives a typed no-action or task-flow result with timings, completion/failure reviews and task artifacts; CLI success by itself is not proof of task success (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/baml_src/ns_voice_turn/agent_routing.baml`, `agent-host/src/reframe_agent_host/voice/agent_turn.py`, `agent-host/src/reframe_agent_host/commands/voice_turn.py`).

### Working context and effect boundaries

Context control is explicit at several levels. `TaskConversation` removes validation replies and preferentially excludes other active human replies from the task frame, retaining the current human reply. Graph relevance selection keeps selected IDs before composition. Normal tasks append linked instructions after composition. Each Codex execution is ephemeral, but retries reuse its prepared filesystem workspace; its conversation is not resumed by this adapter. Only final data, tool receipts and bounded executor feedback cross back to completion checking. The agent feedback is capped at 16,000 characters and overlength is also marked failure, not silently accepted success. These mechanisms resemble separate selected-input frames, but workspace and graph state outlive the frame; they are not references inside a shared model window. No claim about opaque BAML/provider/Codex internal compaction is established (SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/src/reframe_agent_host/agent_flow/task_execution.py`, `agent-host/src/reframe_agent_host/agent_execution/tasks.py`, `agent-host/src/reframe_agent_host/agent_execution/sandbox.py`, `agent-host/src/reframe_agent_host/agent_execution/summary.py`).

The capability surface is larger than any one task's grants. `ToolCatalog` contains possible operations; `task.content.tool_ids` supplies the actual attempt allowlist, validated against that catalog. The normal runner receives only those host tools. Codex receives the same allowlist over MCP **and** native shell/file tools. Host-internal `NativeBoundary` composition validates operations without passing through public task assignment. Store guests also have activation-bound callbacks and a native panel import. Consequently neither task tool IDs nor the Codex filesystem profile is a universal monitor for all host/Store effects (SRC-1, `agent-host/src/reframe_agent_host/task_tools/catalog.py`, `agent-host/src/reframe_agent_host/voice/task_tool_session.py`, `agent-host/src/reframe_agent_host/task_tools/native_boundary.py`, `agent-host/baml_src/ns_task/execution/agent_prompts.baml`, `semantic-store/crates/store-runtime/src/panel/host.rs`).

For the native panel import, `wit::Host::request` validates request/result limits, maps operation to required capability, checks the invocation context and requires a manager before dispatch. Stream resources and returned data are separately bounded. This is a local typed boundary, not evidence of platform-browser security or of which native grants a deployment installed. Store startup and callback permissions are separately described in [RT-RTE-saved-store](#rt-rte-saved-store). Available panel-manager backend and workspace-daemon storage leaves were not exhaustively audited; crash durability, cross-platform containment, website acceptance and native policy completeness remain unestablished (SRC-1, `semantic-store/crates/store-runtime/src/panel/host.rs`, `semantic-store/crates/store-runtime/src/panel/boundary.rs`; boundary exclusions).

### Selected forcing cases and guarantee scope

The four cases below were source-traced counterexamples to stronger readings, not executed tests.

| Case and challenged inference | Enforcement owner, point and strength | Covered paths, alternate paths and required contract | Separate conclusions |
| --- | --- | --- | --- |
| Unassigned Reframe call, then native shell: “task assignment confines every action.” | Host `ToolAttempt.call` rejects unassigned operations and foreign/closed bindings. Strength: invariant at this entry. | Covers normal BAML callbacks and task MCP using this attempt. Does not cover native Codex shell/files, trusted internal composition or Store callbacks. OS/Codex must enforce the supplied sandbox for native tools. | implementation conclusion status: wired; operation conclusion status: uninspected |
| PASS with execution failure, then exhaustion: “completion or bounded return proves success.” | `TaskAttemptSucceeded` requires PASS and null failure fields. BAML's positive cycle/attempt checks and loop tests bound orchestration. Strength: invariant for this control flow. | Covers `RunVoiceTurn`; standalone execution APIs do not inherit its completion/retry loop. Native runner has its own step limit; a provider/callback must return or fail for wall-clock termination. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Mutating timeout then retry: “tools are exactly once.” | Host fingerprints calls and records uncertainty; repeated call ID in one attempt returns the same future, and uncertain mutating fingerprint is rejected across the shared cycle ledger. Strength: best effort for effects. | Covers `ToolAttempt` operations. A new argument fingerprint, fresh cycle/ledger, native shell or remote action is not a distributed transaction. Depends on handler error reporting and observation of actual live state. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Publish with claimed tests or stale metadata, then failed live apply: “all admitted changes have passed acceptance and activate atomically.” | Store publication has expected-content CAS and reference checks; activation has revision checking and recovery. Application initial publication separately checks matching receipt fields. Strength: protocol. | Host publication's nonempty `verification` is recorded text, not an automatically checked acceptance receipt. Explicit testing, startup membership and live activation are separate operations. Recovery can itself fail and leaves the saved candidate unchanged. Requires database transaction semantics and native replacement/rebind behavior. | implementation conclusion status: wired; operation conclusion status: uninspected |

The requested Codex profile denies root access except minimal reads, permits workspace writes and resolved tool-directory reads, disables network, ignores user config and requests no interactive approvals. These flags establish supplied policy, not a measured deployed isolation envelope. In particular, host tools can intentionally produce effects outside the Codex filesystem/network boundary. The process owner kills a Unix process group or closes a Windows job when host input closes; this is an implemented cleanup mechanism, not evidence that arbitrary escaped descendants or platform sandbox implementations were tested (SRC-1, `agent-host/src/reframe_agent_host/agent_execution/sandbox.py`, `agent-host/src/reframe_agent_host/agent_execution/codex.py`, `agent-host/src/reframe_agent_host/agent_execution/process_owner.py`).

### Change admission and retained authority

The runtime admits several different kinds of change. Optional model proposals become layer-specific guidance only after model review ([RT-RTE-guidance-review](#rt-rte-guidance-review)); detailed memory revision findings belong to the memory analyst. Workspace persistence supports recovery, whereas explicit `filesystem_memory` publication checkpoints selected paths and can link the result to future task executions. Saved Store metadata can then reference checkpointed code/UI, instructions and startup parameters; publication, next-launch membership and live activation have distinct gates ([RT-RTE-saved-store](#rt-rte-saved-store)). The shipped application publisher also edits existing task prompts/tool grants and instruction links, so it changes later agent behavior, not merely UI files ([RT-RTE-application-publish](#rt-rte-application-publish)). None of these source paths by itself proves improved capacity or exercised self-improvement.

## Shared records

### Components

#### RT-CMP-model-transport
Label: BAML model transports

Source-native identity: `ModelTransport`, `ModelClient` and provider-selected compiled clients. Representational form: distributed-parametric inference behind symbolic client/model identifiers; model input is natural-language and structured prompt content. Storage substrate: remote provider weights/state, outside the frozen checkout; local BAML definitions and graph provider records select clients. Parameter changes during operation: provider-internal changes uninspected; inspected adapters perform inference, not parameter updates. Exact version pinned: no immutable weight/version digest in the inspected transport; model names are request identifiers. Mutable endpoint can resolve another model: possible; no frozen provider resolution contract establishes immutable mapping. These limits also apply to routing, review and completion calls, not just task execution (SRC-1, `agent-host/baml_src/ns_opencode_go/model_client.baml`, `agent-host/baml_src/ns_opencode_go/direct_clients.baml`, `agent-host/src/reframe_agent_host/agent_flow/provider_clients.py`).

> return openai.ResponsesClient.new(
>     model = model,
>     base_url = "https://opencode.ai/zen/go/v1",
>     api_key = env.OPENCODE_GO_API_KEY,
> --- `agent-host/baml_src/ns_opencode_go/model_client.baml`

#### RT-CMP-codex-model
Label: Codex delegated model selection

Source-native identity: `CodexExecutor` invokes `codex exec` with `config.model_id` and optional reasoning effort. Representational form: distributed-parametric model behind a symbolic subprocess/configuration boundary. Storage substrate: delegated runtime/provider, not included weights. Parameter changes during operation: uninspected inside Codex/provider; this adapter supplies prompt/configuration and parses results. Exact version pinned: no; executable is environment/PATH selectable and model is supplied by task configuration. Mutable endpoint can resolve another model: uninspected delegated provider resolution, with no immutable model contract exposed here. Separate from the direct BAML transport because executable, tools, approval and isolation owners differ (SRC-1, `agent-host/src/reframe_agent_host/agent_execution/codex.py`).

> self.executable = executable or os.environ.get("REFRAME_CODEX_EXECUTABLE", "codex")
> --- `agent-host/src/reframe_agent_host/agent_execution/codex.py`

#### RT-CMP-whisper-transcriber
Label: Voice transcription model

Source-native identity: `WhisperTranscriberConfig` selects `WhisperCppTranscriber` or `FasterWhisperTranscriber`; default model name is `large-v3`. Representational form: distributed-parametric speech inference, with natural-language initial prompt and symbolic backend configuration. Storage substrate: configured local model file or backend-resolved model assets, not frozen weights. Parameter changes during operation: the inspected configuration/factory exposes inference, not an update mechanism; backend internals remain uninspected. Exact version pinned: no model-content digest established by these files. Mutable endpoint resolving another model: not a direct remote inference endpoint here; a configured path/asset name can identify different local content across installations. Text entry bypasses this component. Voice quality and model download provenance remain unobserved (SRC-1, `agent-host/src/reframe_agent_host/speech/transcription.py`, `agent-host/src/reframe_agent_host/speech/transcription_types.py`).

> DEFAULT_WHISPER_MODEL = "large-v3"
> --- `agent-host/src/reframe_agent_host/speech/transcription_types.py`

### Operative objects

#### RT-OBJ-tool-attempt
Label: Task tool attempt and uncertainty ledger

Source-native identity: `ToolAttempt`, `ToolBinding`, `EffectLedger`. Representational form: symbolic task/attempt/conversation/workspace binding, resolved operation map, call-ID map and uncertain fingerprint set. Storage substrate: Python in-process objects; tool receipts separately reach `ToolHistory` backed by the memory database. Lifetime is one attempt, with a shared ledger across retries of one cycle; it is not a global durable idempotency service. The object governs tool authority and replay risk rather than model interpretation (SRC-1, `agent-host/src/reframe_agent_host/task_tools/attempt.py`, `agent-host/src/reframe_agent_host/voice/task_tool_session.py`, `agent-host/src/reframe_agent_host/voice/agent_task_callbacks.py`).

> if name not in self.operations:
>     raise PermissionError(f"tool is not assigned to this task: {name}")
> --- `agent-host/src/reframe_agent_host/task_tools/attempt.py`

> if operation.mutating and fingerprint in self.ledger.uncertain:
>     raise ValueError("effect outcome is uncertain; inspect live state before a new action")
> --- `agent-host/src/reframe_agent_host/task_tools/attempt.py`

### Routes

#### RT-RTE-request-cycle
Label: Routed request cycle and completion control

Endpoints and progression: accepted text/transcript → context callbacks → task/search/relevance/composition models → selected execution → dispatch/summary → task and request completion → typed result. Owner: BAML orchestration with Python I/O callbacks. Decision roles: models choose task, context and retry/refinement; code enforces bounds, no-action branch and failure conjunction. Human supplies the open request; no per-step human approval appears in this path. Answer oracle: task output specification and request are comparison criteria, not an independently supplied expected answer; model judgment is not an answer oracle. Operating mode: open requests with bounded attempts/cycles, not an experimental curriculum. Improvement trigger: task failure prompts refinement, without establishing a persistent improvement.

- Immediate return: `VoiceTaskFlowResult` or `VoiceTaskNoActionResult`, carrying the latest bounded result and review/timing data; outer Python assembles `VoiceTurnResult`.
- Later read-back: context reload and request-conversation callbacks can read recorded interaction state; the transient retry context carries earlier replies/refusals within this invocation. Memory-specific provenance and durable consumers are left to the memory report.
- Delegated visibility: execution receives composed prompt and selected context, not all routing state; completion receives summary plus failure text and scoped conversation.
- Selection predicate: chosen task ID resolves against available tasks; `agent_config` selects executor; model-kept memory IDs determine composition inputs; success requires PASS and null execution/summary failure.
- Invalidation or expiry: task-cycle and attempt counts bound the run; task frames filter validation replies and other active human requests; callbacks reload context on another cycle.
- Activation or effect: execution callbacks can cause external effects before completion review; a failed review cannot undo those effects. Behavioral adequacy of model choices is unobserved.
- Evidence limits: source-traced control flow, without observed model choices, task success, wall-clock liveness or causal benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`, `agent-host/baml_src/ns_voice_turn/agent_routing.baml`, `agent-host/src/reframe_agent_host/voice/task_flow_host.py`, `agent-host/src/reframe_agent_host/voice/agent_turn.py`.

> max_task_cycles: int = 2,
> max_task_attempts: int = 2,
> --- `agent-host/baml_src/ns_voice_turn/task_flow.baml`

> completion == root.task.CompletionResult.PASS
>     && execution_failure == null
>     && summary_failure == null
> --- `agent-host/baml_src/ns_voice_turn/agent_routing.baml`

#### RT-RTE-model-task
Label: Direct model task with Host-owned tools

Endpoints and progression: host task/provider reload → task-linked instruction append → BAML `CallPerformTask` → native agent tool loop → validated final data → host output recording and action-history summary. Owner: BAML agent chooses next call and final data; Python ToolAttempt owns execution and receipts. State effects are dispatched during tool calls, not deferred from final text. Models use [RT-CMP-model-transport](#rt-cmp-model-transport) and tool enforcement uses [RT-OBJ-tool-attempt](#rt-obj-tool-attempt).

- Immediate return: validated `TaskExecutionResult`; exceptions become an outer typed failure boundary while completed tool receipts remain available.
- Later read-back: tool/action history can feed summarization; task-linked retained instructions are appended on subsequent execution. Static prompt code is not itself use-derived read-back.
- Delegated visibility: normal model receives composed prompt, appended instruction bodies and assigned Host tool schemas/results; assignment is resolved from stored task tool IDs.
- Selection predicate: selected task has no agent configuration; provider record chooses compiled model/reasoning client; catalog resolution rejects unknown assigned tools.
- Invalidation or expiry: native runner max_steps is 64; tool attempt closes at session exit, cancels active calls and runs cleanup. Uncertainty ledger survives only the selected cycle's retries.
- Activation or effect: Host operation handlers execute validated calls and record outcomes. This establishes an effect-capable path, not evidence that any inspected grant or instruction was actually used.
- Evidence limits: BAML runtime and provider internals are external; generated binding correctness and actual tool effects were not tested. The tool allowlist does not cover other executors or host-internal composition.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/src/reframe_agent_host/agent_flow/task_execution.py`, `agent-host/baml_src/ns_task/execution/flow_host.baml`, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`, `agent-host/src/reframe_agent_host/voice/task_tool_session.py`, `agent-host/src/reframe_agent_host/task_tools/catalog.py`.

> spec.toolbox = HostToolbox(host_tools, dispatch_tool);
> --- `agent-host/baml_src/ns_task/execution/flow_host.baml`

> max_steps = 64,
> --- `agent-host/baml_src/ns_task/execution/flow_host.baml`

#### RT-RTE-codex-task
Label: Prepared-workspace Codex execution

Endpoints and progression: selected agent configuration → workspace preparation/retry identity check → task MCP session → process owner → Codex → parsed final data → workspace persistence → compact executor feedback. Python owns process lifetime, workspace binding and effect adapters; Codex owns opaque internal model/tool continuation. It uses [RT-CMP-codex-model](#rt-cmp-codex-model). No interactive approval is requested by the supplied profile; task assignment is the Reframe MCP grant, not evidence of human approval of each action.

- Immediate return: `AgentAttempt` with run/error/result and tool history; summary returns exactly one executor feedback item or marks missing/overlength feedback as failure.
- Later read-back: retries reuse prepared workspace content; explicit filesystem publication can retain selected paths and link them to future executions. Ordinary `persist_workspace` is recovery, not by itself publication as guidance.
- Delegated visibility: Codex receives wrapped task prompt, root workspace AGENTS instructions by request, task-scoped MCP and native tools. Caller receives final data, errors/events and feedback, not the full opaque inner context.
- Selection predicate: nonnull `agent_config`; prepared task identity and configuration must match on retry; selected Store project IDs participate in workspace preparation.
- Invalidation or expiry: ephemeral invocation, configured execution timeout and process-owner EOF cleanup; same task workspace survives attempts. Actual OS/Codex sandbox enforcement is an external contract.
- Activation or effect: native shell/files act inside requested sandbox; MCP handlers can act through Host capabilities outside it. Workspace is persisted before output dispatch. Actual confinement and successful effects are unobserved.
- Evidence limits: neither Codex internals nor deployed model/configuration are frozen; no cancellation, sandbox escape or process-cleanup experiment was supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/src/reframe_agent_host/agent_execution/tasks.py`, `agent-host/src/reframe_agent_host/agent_execution/codex.py`, `agent-host/src/reframe_agent_host/agent_execution/sandbox.py`, `agent-host/src/reframe_agent_host/agent_execution/process_owner.py`, `agent-host/src/reframe_agent_host/agent_execution/mcp_config.py`, `agent-host/src/reframe_agent_host/agent_execution/summary.py`, `agent-host/src/reframe_agent_host/voice/agent_task_callbacks.py`.

> if workspace.prepared.task_id != selected.id or workspace.config != selected.agent_config:
>     raise ValueError("agent retry changed its task identity or configuration")
> --- `agent-host/src/reframe_agent_host/agent_execution/tasks.py`

> "--ignore-user-config",
> "--ephemeral",
> --- `agent-host/src/reframe_agent_host/agent_execution/sandbox.py`

> The Host uses this as the task's feedback without launching a second model conversation.
> --- `agent-host/baml_src/ns_task/execution/agent_prompts.baml`

#### RT-RTE-guidance-review
Label: Optional decision guidance admission

Endpoints and progression: optional `propose_candidate_memory` calls during routing/search/depth/relevance/composition → layer-bound candidate groups → parallel nonempty-group review → kept-ID intersection → Python write batch. Proposer: the decision model; admission decision: review model; veto: review can keep no candidates, code rejects empty title/description and filters to actual candidate IDs. Host performs persistence without an intervening human approval in this route. Operating mode: optional guidance proposed during open requests; no expected-answer oracle. Trigger/objective: reusable decision-layer guidance, explicitly not user facts/preferences or direct writes. This is a proposal/admission mechanism, not proof of reliable criticism or better decisions.

- Immediate return: proposal tool acknowledges staging; review returns a write batch and host callback returns completion.
- Later read-back: writes title/description to five guidance collections; those collections enter later decision context through loaders identified in the boundary. Memory revision semantics belong to the memory analyst.
- Delegated visibility: review receives purpose, candidates and stored memories; execution model need not see rejected candidates. Reviewer input is not a full independent execution test.
- Selection predicate: only nonempty candidate groups are reviewed; kept candidate IDs filter the staged entries before layer-specific writes.
- Invalidation or expiry: transient proposals end with the request; admitted records persist in database collections. No rollback/expiry mechanism was established by this narrow write adapter; memory maintenance is not assessed here.
- Activation or effect: admitted text is wired for later prompt supply; content-specific compliance, correction and benefit remain unobserved.
- Evidence limits: no concrete candidate/output trace; no inferred theory-building, reflection, learning or autonomous improvement from the existence of review. Provider processing is opaque rather than evidenced absent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/baml_src/ns_memory/candidate_tools.baml`, `agent-host/baml_src/ns_task/routing/flow_host.baml`, `agent-host/baml_src/ns_voice_turn/memory_review_flow.baml`, `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`, `agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py`; later loaders are source-grounded in [the boundary](boundary.md#boundary-and-evidence).

> "Candidate staged for review, not published. Continue with the decision."
> --- `agent-host/baml_src/ns_memory/candidate_tools.baml`

> decision.kept_candidate_ids.includes(candidate.id)
> --- `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`

#### RT-RTE-saved-store
Label: Checkpoint-backed saved Store admission and activation

Endpoints and progression: explicit path retention/checkpoint publication → saved Store source/artifact/instruction references → expected-content metadata publication → separately selected startup membership or live activation. CheckpointPublisher reconciles a daemon outbox into graph memory and acknowledges publication only after the graph write. Host tools can propose metadata; code validates references and stale edits. A model/caller supplies `verification` text; the tool records it without making it an automatic acceptance condition. `test_store_candidate` is a separate operation. Human approval of each metadata change is not established by the generic caller. Operating mode: open maintenance, with an available isolated candidate-test mechanism rather than a required experiment at every publication. Oracle: reported verification is not an expected-answer oracle; candidate testing implementation is not characterized here.

Admission and recovery: publication requires existing checkpoint/instruction references and expected prior content in a database transaction. At next launch, startup snapshots membership, loads all packages/binds callbacks before startup invocation, then requires a designated selection authority and valid session/conversation before accepting input. Live activation checks expected revision, serializes application, may pause selection admission, replaces package/binding and reconnects panels without replaying startup. Failure attempts old-artifact/binding/panel recovery, reports recovery failure and leaves saved metadata unchanged. Proposal guidance is the tool descriptions and shipped application maintenance guidance: inspect prior state, test privately, publish deliberately and activate only when requested. Persisted results include checkpoint references, metadata, instruction associations and startup membership (SRC-1, cited paths below).

- Immediate return: retention memory/path IDs; publication says saved_for_next_launch and applied_live false; membership says next Host launch; activation reports applied/recovery fields.
- Later read-back: startup loads the published checkpoint artifacts, binds graph grants and invokes saved startup parameters; future task executions may import explicitly linked filesystem memory.
- Delegated visibility: workspace retention requires a matching task-bound workspace; saved source/artifact references are resolved by host services; guest callbacks receive revision-bound authority rather than raw database access.
- Selection predicate: explicit relative retained paths, logical Store identity, expected old metadata and live revision; startup membership designates exactly one selection Store. Package identity must match saved Store ID.
- Invalidation or expiry: stale metadata/revision is rejected; membership takes effect next launch, not immediately; live recovery can fail and does not undo saved candidate metadata.
- Activation or effect: saved metadata can select future executable/UI artifacts; explicit live activation can change current machinery. No supplied trace establishes which candidate was activated or its downstream behavior.
- Evidence limits: graph/database/daemon atomicity and native replacement require external implementation contracts; no measured crash recovery or test-quality conclusion. The automatic initial application gate in the next route is stronger than generic host publication.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/src/reframe_agent_host/task_tools/workspace.py`, `agent-host/src/reframe_agent_host/agent_execution/retention.py`, `agent-host/src/reframe_agent_host/workspace/publication_service.py`, `agent-host/src/reframe_agent_host/task_tools/store_publication.py`, `agent-host/src/reframe_memory/store_memories.py`, `agent-host/src/reframe_agent_host/startup_stores.py`, `agent-host/src/reframe_agent_host/startup_activation.py`.

> description='Actual candidate build/test evidence, including isolated startup, React and Store behavior. This is recorded evidence, not an automatic test claim.')
> --- `agent-host/src/reframe_agent_host/task_tools/store_publication.py`

> IF $old != NONE AND $old.content != $expected {{
> --- `agent-host/src/reframe_memory/store_memories.py`

> 'recovery_error':recovery, 'saved_candidate_unchanged':True}
> --- `agent-host/src/reframe_agent_host/startup_activation.py`

#### RT-RTE-application-publish
Label: Session-management application initial publication

Endpoints and progression: supplied build/acceptance JSON → receipt-field gate → checkpoint and instruction publication → Store metadata CAS → existing task prompt/tool updates and instruction links → startup membership. Principal: script caller, whose human/computational identity is not fixed by source. Code decides the receipt predicate; author/caller supplies artifact content. Rejection ability: mismatched or failed receipts, ambiguous instructions/tasks and stale edits fail. Operating mode: explicit initial publication with matching acceptance requirements, distinct from the open host tool. Oracle: receipt status/manifest correspondence is an admission predicate, not independent proof of the tested application's correctness. Test execution and receipt authenticity remain outside this inspected driver.

Change and guidance: application instructions are read from `instructions.md`; task publication appends guidance directing isolated source/instruction use, fixture testing, separate publication/membership/live apply and reporting partial recovery. The driver can expand tool grants on existing authoring tasks. It does not require human review of each content edit. Publication spans several writes: it emits partial status on failure, rather than implementing a single global rollback of all prior writes.

- Immediate return: JSON output reports partial/published state, memory IDs and task records; receipt is marked published only after success.
- Later read-back: startup consumes saved Store membership; task chooser/executor can consume edited prompts, tool grants and linked instructions in future turns.
- Delegated visibility: stored instructions are linked to existing tasks and Store metadata; this driver does not itself send their full bodies to a model.
- Selection predicate: built/passed/restart/candidate receipt fields and matching checkpoint manifest; known existing task names and expected prior task content constrain edits.
- Invalidation or expiry: concurrent task edit fails read-back verification; Store publication has CAS; no global rollback across checkpoint/instruction/task/membership writes. Repaired rerun must account for partial publication.
- Activation or effect: changes next-launch production selection/UI and future agent capability/prompt inputs; actual subsequent consumption is unobserved.
- Evidence limits: acceptance-program presence or receipt labels do not prove an observed passing run. No inference of successful improvement or human-controlled per-content admission.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `applications/session-management/publish.py`, `applications/session-management/session_task_publication.py`, `agent-host/src/reframe_memory/store_memories.py`.

> raise ValueError('publication requires matching real recovered Store/React/CEF acceptance')
> --- `applications/session-management/publish.py`

> proposed[name] = replace(old, prompt=prompt, tool_ids=tuple(dict.fromkeys(
>     (*old.tool_ids, *TOOLS, 'save_semantic_store', 'save_visual_panel', 'filesystem_memory'))))
> --- `applications/session-management/session_task_publication.py`

### Claims

#### RT-CLM-agent-output
Label: Agent output is data rather than deferred actions

Claimed operation: agent instructions require actual Reframe actions through assigned tools, with final data limited to evidence/paths/runtime IDs and exactly one summary. This is doctrine inside an executable prompt, not reliable model compliance. Host implementation records outputs and uses executor feedback, so earlier effects precede completion. It does not follow that all returned data is truthful or every native action is authorized by task tools (SRC-1, `agent-host/baml_src/ns_task/execution/agent_prompts.baml`, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`, `agent-host/src/reframe_agent_host/agent_execution/summary.py`).

> Shell commands and file changes you perform are already executed; never return them as actions to repeat.
> --- `agent-host/baml_src/ns_task/execution/agent_prompts.baml`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-store-callback
Label: Activation-bound Store Host authority

Consumer: `StoreHostBoundary.request`. Channel: typed guest callback message containing Store ID, revision and operation, interpreted against the host's activation map. Force: symbolic checks reject missing/stale activation; graph reads require their own grant, while selection/observation/input/cancellation operations require the designated selection authority. `open_default_panel` has its own early path. Horizon: one bound live revision until startup close or managed rebind; saved configuration can establish the next launch's map. This is distinct from the task tool allowlist and is not unrestricted graph mutation. Evidence: SRC-1, `agent-host/src/reframe_agent_host/store_host_boundary.py`, `agent-host/src/reframe_agent_host/startup_stores.py`, `agent-host/src/reframe_agent_host/startup_activation.py`.

> if binding is None or binding[0] != message["revision"]:
>     raise PermissionError("Host callback has no current Store activation binding")
> --- `agent-host/src/reframe_agent_host/store_host_boundary.py`

> if not binding[2]:
>     raise PermissionError("graph selection and execution observations require the designated selection Store")
> --- `agent-host/src/reframe_agent_host/store_host_boundary.py`

#### RT-BAP-panel-import
Label: Store guest native panel import

Consumer: Store runtime `wit::Host::request`. Channel: typed WIT operation plus requested result byte limit, invocation capabilities and configured PanelManagerHost. Force: code checks input size, required capability and manager availability before native dispatch, then bounds unary/stream returns. Horizon: active invocation and its stream resources; installed grants come from host configuration, not from a model's request. Actual installed grant values and backend enforcement were not observed. This is an alternate effect path to task tools, with its own checks rather than inheritance of a Codex sandbox. Evidence: SRC-1, `semantic-store/crates/store-runtime/src/panel/host.rs`, `semantic-store/crates/store-runtime/src/panel/boundary.rs`.

> .filter(|context| context.capabilities().contains(capability))
> --- `semantic-store/crates/store-runtime/src/panel/host.rs`

## Annotations

none
