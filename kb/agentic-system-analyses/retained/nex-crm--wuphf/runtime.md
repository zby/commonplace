---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Wuphf runtime baseline: broker-driven office turns, scheduled tools, model authoring and route-local approval boundaries."
run-id: AAS-2026-10-15-wuphf-b246722f99c0-01
reviewed-boundary: "88023d4dac7491b6e71dbc1e86d274c435b9cb2c"
---

# Wuphf runtime report

## Runtime account

### Scope and consequential work

The frozen repository calls the product gawkbot. Its claimed work is to turn described workflows into local microapps with tools, schedules, knowledge and human approval for external actions. The runtime has two materially different execution families: broker-driven office agents, often executing through installed coding CLIs; and a Bun sidecar that authors and runs persisted JavaScript tools or deterministic workflow specifications. The latter is not a general conversational agent loop: tool matching, capability invocation and scheduler progression have substantial fixed-rule ownership. See [RT-CLM-external-approval](#rt-clm-external-approval), [RT-RTE-office-turn](#rt-rte-office-turn), [RT-RTE-scheduled-tool](#rt-rte-scheduled-tool) and [RT-RTE-spec-replay](#rt-rte-spec-replay).

Evidence is SRC-1 implementation and attributed design at the boundary's frozen commit. Newly inspected implementation includes `internal/team/notifier_loops.go`, `internal/team/notifier_delivery.go`, `internal/team/headless_codex_queue.go`, `internal/team/headless_codex.go`, `internal/team/headless_claude.go`, `internal/team/headless_codex_runner.go`, `internal/team/headless_openai_compat.go`, `internal/team/prompts.go`, `internal/team/broker_plan_approval.go`, `internal/team/bot_service_supervisor.go`, `internal/team/broker_apps_integrations.go`, `internal/team/broker_apps.go`, `internal/teammcp/app_tools.go`, and `agent/src/{service,serviceAuthor,model,tools,toolRuntime,toolSandboxWorker,capabilities,executor,store}.ts` (the brace notation here is a coverage summary, not a citation anchor). Individual findings below cite real paths. Initial boundary sources were also revisited. No target, tests, examples, model calls or services were executed. No supplied observed run or experiment establishes activation, deployment isolation, reliability or benefit.

The boundary remains **complete artifact, partial loop**. This report traces selected consequential paths, not all frontend callers, adopted CLI templates, computer backends, MCP tools, knowledge maintenance, app-store internals or release machinery. Their availability is not an access gap. Those limits prevent universal approval, exhaustive extension-admission and complete recovery claims. Knowledge revision belongs to the memory analyst; context delivery inspected here does not establish its correctness or behavioral uptake.

### Ordinary office invocation

The shipped CLI reaches `LaunchWeb`, which prepares MCP configuration, starts the broker and web server, resumes in-flight work and launches message, task-action, roster-change and scheduler loops. The broker separately supervises the sidecar, passing its broker address and bearer credential unless the environment supplies alternatives. An externally supplied `WUPHF_AGENT_URL` disables local spawning. SRC-1, `cmd/wuphf/main.go`, `internal/team/launcher_web.go`, `internal/team/broker.go`, `internal/team/bot_service_supervisor.go`.

> go l.notifyBotsLoop()
> go l.notifyTaskActionsLoop()
> go l.notifyOfficeChangesLoop()
> go l.watchdogSchedulerLoop()
> --- `internal/team/launcher_web.go`

Take an ordinary post-onboarding human message to an office bot. The broker message subscription delivers it to notification targeting. Deterministic onboarding has a separate no-model branch. Targeting and per-recipient/sender/channel cooldown rules run before delivery; a pending interview parks only its asking bot. Delivery constructs a work packet, truncates the new message to 1,000 characters in the notification and attaches a human-priority instruction and reply channel/message identifiers. Headless dispatch carries slug, task ID, channel, origin and injected-context manifest into the queue. These are separate identities: the bot slug names the member; a task ID scopes work and ledger entries; a channel/message ID scopes the reply. SRC-1, `internal/team/notifier_loops.go`, `internal/team/notifier_delivery.go`; [RT-RTE-office-turn](#rt-rte-office-turn).

The queue selects a lane: taskless chat uses the bot lane; assigned worktrees serialize by path; other task turns use task lanes. Its governor checkpoint precedes starting a fresh turn. A task-aware context supplies provider/model/posture choices. In the default Claude route, the model receives the assembled bot prompt, computer hint if mounted, notification and a separately fenced memory brief fetched under a two-second deadline. The installed CLI owns model/tool next-step selection. Wuphf owns subprocess setup, working directory, stream processing, process cancellation and broker effects mediated by its MCP server. Coding work can use task worktrees; otherwise the process starts in a bot scratch directory. A working directory is not filesystem or network containment. SRC-1, `internal/team/headless_codex_queue.go`, `internal/team/headless_claude.go`.

The model can post directly through a broker tool; stream text is also relayed live. At completion the launcher emits terminal/manifest events, records usage and posts final text only if necessary. Planning turns raise a separate approval request. The queue checks applicable task durability, records a task ledger entry, clears its active slot even on panic, and can wake the lead after specialists settle. Failure branches distinguish timeout, cancellation, durability failure and transient provider retry. Recovery may repeat work; no exactly-once external-effect guarantee follows. SRC-1, `internal/team/headless_claude.go`, `internal/team/headless_codex_queue.go`; [RT-RTE-plan-approval](#rt-rte-plan-approval).

### Alternate routes and forcing cases

Four forcing comparisons bound the result:

1. **Scheduled versus manual saved-tool execution.** The scheduler selects the current live playbook prompt when present, not merely the frozen payload. `runRoutine` always supplies `approved: false`; manual `/tools/call` instead accepts the caller's Boolean approval assertion. The host gate therefore enforces a run flag on named capabilities, not independently authenticated human consent. Moreover, `integrations.call` can return a held-for-approval string as an ordinary result, allowing overall tool status `ok` while an integration action remains pending. Scheduler success is not proof an external mutation completed. [RT-RTE-scheduled-tool](#rt-rte-scheduled-tool), [RT-RTE-saved-call](#rt-rte-saved-call).
2. **Authored tools versus deterministic HTTP replay.** Worker tools reach the host capability table by RPC; `/run` accepts a supplied spec and gates only steps whose own `gated` field is true. An ungated step with an API descriptor goes to `fetch` without passing the capability gate or broker's integration classifier. These are not equivalent enforcement paths. [RT-RTE-spec-replay](#rt-rte-spec-replay).
3. **Planning versus execution and provider changes.** Claude planning passes native plan permission mode, whereas ordinary execution requests permission bypass. Codex planning requests read-only; execution can request sandbox bypass or workspace-write. Native CLI enforcement is an external contract, and Codex's source explicitly permits MCP notebook/channel writes during read-only planning. The OpenAI-compatible route has its own eight-iteration tool loop and text-only fallback if the MCP bridge fails; gateway providers may operate an additional upstream loop. It is unsound to transfer a Claude or worker guarantee to all providers. [RT-RTE-office-turn](#rt-rte-office-turn), [RT-RTE-compatible-turn](#rt-rte-compatible-turn), [RT-RTE-plan-approval](#rt-rte-plan-approval).
4. **Manual authoring versus routine-triggered admission.** `/tools/build` persists only model-authored results. `runRoutine` persists any non-null authored tool, including a deterministic fallback returned by `buildTool`. This counterexample prevents describing stub rejection as a system-wide admission invariant. The smoke check is simulated and rejects selected crash patterns, not arbitrary wrong behavior. [RT-RTE-tool-authoring](#rt-rte-tool-authoring), [RT-RTE-scheduled-tool](#rt-rte-scheduled-tool).

These cases are source inspections, not attempted exploits or demonstrated failures. Exact deployed grants, native CLI tool catalogs and actual host isolation are unobserved. Available but untraced alternatives include interactive panes, generic adopted CLIs, OpenCode, Slack relay execution, owner-resumed terminal sessions and remote computer implementations. Dispatch source establishes that these alternatives exist, not that their enforcement matches an inspected path. SRC-1, `internal/team/headless_codex.go`, `internal/team/headless_session_runner.go`, `internal/team/pane_dispatch.go`.

### Load-bearing guarantees and change admission

| Guarantee and owner | Enforcement point and strength | Covered paths, alternate paths and external contract | Conclusion statuses |
|---|---|---|---|
| Routine run approval flag; sidecar | `runRoutine` passes false; invariant of this caller | Named host-gated capabilities; not all effects, arbitrary replay or CLI actions. Broker integration mutations use another gate. Requires host capability implementation and correct dispatch. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Named capability send/browser gate; host runtime | `hostCaps.invoke`, fixed path membership plus run flag; invariant of RPC dispatch | Injected capability trees remain gated at those names. Local data writes are not on the list. Manual caller may set approval true. Worker ambient authority is only partially reduced, not proven absent. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Integration mutation deferral; broker | `ActionIsReadOnly` classification followed by approval creation rather than `ExecuteAction`; protocol | `/apps/integrations/call`; correctness depends on action classification and later human-request machinery. Does not cover arbitrary HTTP replay or native CLI shell/network work. Approved-action execution was not traced here. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Worker deadline; sidecar | timer terminates Worker and aborts run signal; best effort across external effects | Bounds worker execution and signals cooperating host capabilities. Does not undo a completed write or prove upstream cancellation. Bun worker termination and provider abort behavior are external contracts. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Structured plan before selected task execution; broker plus native CLI | Planning state, permission flags and approval transition; protocol | Selected top-level issues; excludes subissues, internal actors, app-builder tasks and disabled default. Native plan/read-only restrictions do not imply all MCP effects are read-only. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Sidecar network access; service | reject non-loopback binding without token; invariant of startup configuration | Open `/health`; other routes require bearer only when configured. Tokenless loopback remains accessible to local clients. Actual proxy/network exposure and local-user trust are unobserved. | implementation conclusion status: wired; operation conclusion status: uninspected |

The table's semicolon-separated text reports two separate layer fields in prose, not composite status values. Supporting route records below retain the actual controlled fields and evidence. No deployment guarantee is established.

Product/capability change admission is concrete: model or fallback tool proposals pass software checks and can be persisted for later execution; app-building-enabled agents or humans may publish app bytes and restore versions. Starting a build is not per-content human approval. The app registration handler checks capability/actor, not a proof of correct behavior. The inspected tool authoring prompt supplies capability semantics, string-input constraints, draft-first sends and output quality requirements; its acceptance loop checks a narrower set of properties. No traced route here modifies model parameters or the framework's production machinery. Available source for other extension and upgrade paths remains uninspected; that is not a finding of absence. [RT-RTE-tool-authoring](#rt-rte-tool-authoring), [RT-RTE-app-publication](#rt-rte-app-publication).

## Shared records

### Components

#### RT-CMP-office-model
Label: Office provider inference

Source-native identity: the model selected by task provider/model, member binding and runtime defaults in the headless office runners. Representational form: distributed-parametric inference supplied by external CLI or compatible HTTP provider; local Go selectors and messages are symbolic and natural-language inputs, not its parameters. Storage substrate: provider-managed or locally served weights, not captured in SRC-1. Parameters changing during operation: uninspected provider internals; the inspected caller requests inference, not weight updates. Exact parameter version pinned: no; configurable identifiers and native defaults do not pin weights. Mutable endpoint resolving another model: possible through configuration, CLI defaults, aliases or provider service; actual provider resolution uninspected. Evidence: SRC-1, `internal/team/headless_codex.go`, `internal/team/headless_claude.go`, `internal/team/headless_openai_compat.go`.

> // Per-task provider wins over the bot binding (then global default).
> kind := l.effectiveProviderKindForBot(ctx, slug)
> --- `internal/team/headless_codex.go`

#### RT-CMP-author-model
Label: Tool and workflow authoring model

Source-native identity: `resolveToolAuthoring`, `authorToolWithModel`, `buildWorkflow`. Representational form: distributed-parametric inference, consuming schema instructions and a user description. Storage substrate: external provider or local Ollama model; only descriptors live in the service. Parameters changing during operation: no update requested by these inspected calls; provider changes uninspected. Exact version pinned: no weight digest; API path names `claude-sonnet-4-6`, CLI uses alias `sonnet`, Ollama defaults to `qwen2.5-coder:1.5b` or configured ID. Mutable endpoint resolving another model: yes, configuration and alias resolution permit change; actual version unobserved. Direct BUILD uses core `resolveModel` rather than the full service tool-author resolver. Evidence: SRC-1, `agent/src/serviceAuthor.ts`, `agent/src/model.ts`, `agent/src/buildAgent.ts`, `agent/src/tools.ts`.

> const CLAUDE_CLI_MODEL = "sonnet";
> --- `agent/src/serviceAuthor.ts`

> const model = opts.model ?? resolveModel();
> --- `agent/src/buildAgent.ts`

#### RT-CMP-runtime-ai
Label: nex.ai capability inference

Source-native identity: `aiComplete` and `realAI`. This is a separate consumption role from tool authoring, even though it reuses that resolver. Representational form: distributed-parametric computation behind symbolic score/summarize/write capabilities. Storage substrate: provider-managed/local model weights. Parameters changing during operation: no training requested by the inspected capability call; provider internals uninspected. Exact parameter version pinned: no; the same configurable descriptors/CLI alias as the authoring resolver apply. Mutable endpoint resolving another model: permitted by resolver and provider configuration. Calls create fresh system/user contexts; tool execution cannot assume an earlier capability's conversational history. Failure can yield hash scores or simulated text rather than an execution error. Evidence: SRC-1, `agent/src/capabilities.ts`, `agent/src/serviceAuthor.ts`.

> } catch {
> return hashScore(subject);
> }
> --- `agent/src/capabilities.ts`

### Operative objects

#### RT-OBJ-stored-tool
Label: StoredTool executable capability

Source-native identity: `StoredTool`, keyed by sanitized agent ID and tool name. Operative representational form: symbolic JavaScript function and input declaration; title/purpose are natural-language selection and presentation metadata. Storage substrate: per-agent JSON file in `WUPHF_AGENT_DATA_DIR` or package-default `.wuphf-agent-data`. Same-named upsert replaces code and increments version; the inspected store does not retain the replaced tool body as version history. Writes use unique temporary files and rename, but no multiwriter transaction is established. Corrupt JSON can be quarantined and loaded as empty. Later consumers are manual name lookup and routine prompt matching. Evidence: SRC-1, `agent/src/store.ts`, `agent/src/routineRunner.ts`, `agent/src/service.ts`.

> const stored: StoredTool = { ...tool, version: existing ? existing.version + 1 : 1 };
> --- `agent/src/store.ts`

#### RT-OBJ-tool-schema
Label: TOOL_SCHEMA_PROMPT authoring guidance

Source-native identity: `TOOL_SCHEMA_PROMPT`, augmented with current app table schema. Representational form: natural-language instructions plus symbolic JSON examples; interpreted by the author model, not a proof checker. Storage substrate: static TypeScript source string; app schema fetched at runtime. It describes permitted capabilities, string inputs, clock use, defensive field access, explicit-send requirements and structured returns. Later tool execution consumes the resulting code, not necessarily the original rationale. Static shipped guidance is not itself use-accumulated memory. Evidence: SRC-1, `agent/src/tools.ts`.

> - Sends are drafts first: build the content, return it in the result, and call nex.send only when the described workflow explicitly says to send. Subject lines are part of the send target/metadata, not pasted into the body.
> --- `agent/src/tools.ts`

### Routes

#### RT-RTE-office-turn
Label: Broker-driven office turn

Endpoints and progression: broker message/task notifications → target work packet → lane queue → provider-selected runner → broker effects, stream and ledger. Owner: launcher rules select target/lane/provider; external model chooses work and tool steps; broker owns shared office mutation. Context/state: bot slug, task/channel/message identifiers, bot prompt, bounded notification and selected knowledge packet; task state and worktree/scratch cwd are separate. Executor/effect boundary: native CLI subprocess plus MCP broker and any native tools the CLI grants. A cwd and MCP filter do not exhaust that capability surface. Operating mode: open human/bot requests, not a fixed curriculum; no answer oracle identified in this invocation. Human priority and model delegation are mixed computational/human contributions, not approval of each effect.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed activity/text, broker tool effects and final-message fallback; queue records completion/error and ledger state.
- Later read-back: future work packets and ledger consumers can receive retained office state; exact knowledge update/reload paths are left to the memory member.
- Delegated visibility: selected prompt, notification, scoped MCP configuration and mounted computer reach the runner; unrelated task frames are not supplied as accumulated conversation by this launcher.
- Selection predicate: notification targeting, per-target interview/cooldown rules, lane resource identity and task/member provider choice.
- Invalidation or expiry: task turn deadline and cancellation, lane cleanup, fresh headless process; persistent task/artifact expiry uninspected.
- Activation or effect: wired to CLI work and broker changes; actual model compliance, completed work and benefit unobserved.
- Evidence limits: native CLI internals, exact effective native tool grants and deployed isolation are external/unobserved; available pane and generic-CLI variants not fully traced.

Evidence: SRC-1, `internal/team/notifier_delivery.go`, `internal/team/headless_codex_queue.go`, `internal/team/headless_claude.go`, `internal/team/headless_codex_runner.go`; component [RT-CMP-office-model](#rt-cmp-office-model).

> args = append(args, strings.Fields(l.resolvePermissionFlags(ctx, slug))...)
> --- `internal/team/headless_claude.go`

> return "--permission-mode bypassPermissions --dangerously-skip-permissions"
> --- `internal/team/prompts.go`

> case planning:
> args = append(args, "-a", "never", "-s", "read-only")
> case l.unsafe || l.headlessCodexNeedsDangerousBypass(ctx, slug):
> args = append(args, "--dangerously-bypass-approvals-and-sandbox")
> default:
> args = append(args, "-a", "never", "-s", "workspace-write")
> --- `internal/team/headless_codex_runner.go`

#### RT-RTE-compatible-turn
Label: OpenAI-compatible office loop

Endpoints: selected office provider → MCP bridge and HTTP stream → local tool dispatch → next model invocation → final/partial message. Owner: launcher constructs tool catalog and bounds iterations; model proposes calls; local loop dispatches named tools; some gateway upstreams run their own loop. Representational form: natural-language system/notification plus symbolic tool schema, calls and results. State is current-turn message history, not a demonstrated cross-run provider memory. Mode: open request. Proposer/decider: model plus fixed dispatch/parser rules; human enters via ordinary request and downstream broker approvals. Answer oracle: none identified. Host bridge failure causes text-only mode, not successful tool execution.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: live text/tool events, terminal manifest and final or partial broker post; errors propagate to queue recovery.
- Later read-back: uninspected — route inspection establishes current-turn tool messages and broker effects, not a distinct retained transcript reload path.
- Delegated visibility: prompt, user notification and bridge tools; Hermes/OpenClaw receive prompted tool syntax where native tools may be ignored upstream.
- Selection predicate: effective provider kind, task/member model override, successful bridge discovery and parsed tool name.
- Invalidation or expiry: eight-iteration local cap, 90-second configured tool timeout, enclosing turn cancellation and bridge cleanup.
- Activation or effect: tool calls wired through local map to MCP; actual upstream/native loop behavior and successful actions unobserved.
- Evidence limits: cannot infer native CLI plan enforcement or sidecar worker isolation on this route; upstream gateway behavior is not independently frozen.

Evidence: SRC-1, `internal/team/headless_openai_compat.go`; [RT-CMP-office-model](#rt-cmp-office-model).

> const maxOpenAICompatToolIterations = 8
> --- `internal/team/headless_openai_compat.go`

> tools = nil
> --- `internal/team/headless_openai_compat.go`

#### RT-RTE-plan-approval
Label: Structured plan admission

Endpoints: selected top-level issue → Planning posture → model plan → broker interview → approved Running state and dispatch. Owner: broker state and answer rules; model proposes plan; human can approve, reject or request more information. Mode: open work request with a bounded plan gate, not an answer-oracle test. Answer oracle: no reference outcome; a human decision is authorization, not evidence of correctness. Admission concerns task execution; guidance is the selected task and planning prompt/native posture. Plan content is retained in the human request/task machinery, not model parameters. Recovery: worktree synchronization failure leaves Planning; non-approval leaves Planning for revision. No automatic rollback of already performed effects is established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: plan stream/channel content and pending approval; approval schedules execution after worktree sync.
- Later read-back: approved task state controls subsequent provider posture; exact reconstruction of plan text in all next packets uninspected.
- Delegated visibility: planning runner gets task prompt and native plan/read-only flags, not a grant for ordinary execute posture.
- Selection predicate: top-level issue without exempt parent/internal actor/app-builder owner, with plan-first enabled; task lifecycle determines posture.
- Invalidation or expiry: state transition replaces planning posture; rejected requests leave task Planning; request expiry not inspected.
- Activation or effect: broker answer can transition Planning to Running and schedule owner work; actual human judgment and subsequent execution unobserved.
- Evidence limits: guarantee covers selected task lifecycle and external native enforcement, not all MCP effects, chat turns or exempt tasks.

Evidence: SRC-1, `internal/team/broker_plan_approval.go`, `internal/team/prompts.go`, `internal/team/headless_codex_runner.go`.

> if !strings.HasPrefix(strings.TrimSpace(answer.ChoiceID), "approve") {
> return
> }
> --- `internal/team/broker_plan_approval.go`

> if b.disablePlanFirstDefault {
> return false
> }
> --- `internal/team/broker_plan_approval.go`

#### RT-RTE-tool-authoring
Label: Tool proposal and software admission

Endpoints: `/tools/build` description/app ID → resolver/model or deterministic fallback → schema coercion/static capability scan/simulated smoke run → at most one model repair → response and conditional persistence. Owner: code resolves engine and admits; model proposes code; caller supplies workflow/schema context. No per-tool human content approval in the inspected handler. Human may decline to call a returned tool, but that is not a storage veto. Mode: open workflow authoring with a bounded software-check/repair subloop. Answer oracle: no expected business answer; simulated capability shapes and selected crash strings are a limited runtime check, not a semantic correctness oracle. Trigger: teaching/build request; proposed change: durable executable tool; admission: software checks plus `authored_by === "model"` for this endpoint. Recovery: fallback response; same-name writes replace previous code with incremented version, without retained old code in the inspected store.

Guidance comes from [RT-OBJ-tool-schema](#rt-obj-tool-schema) plus current app schema; a smoke failure adds error text to a new authoring request, not the complete prior code or runtime transcript. What persists is tool code/metadata, not a demonstrated formulated theory or criticism archive. This route supports executable capability construction and repair, not an established theory-builder, learning or self-improvement outcome. Those are independent properties; a crash-directed retry alone does not establish a theory's content-directed criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tool and narration with model/stub provenance; model-authored app tools are persisted with a version.
- Later read-back: saved tool enters name lookup or prompt matcher and subsequent worker execution.
- Delegated visibility: author model receives brief and table schema; smoke worker receives code and placeholder string args against simulated capabilities, not live business integrations.
- Selection predicate: host resolver availability/override; static recognized capability paths, selected crash patterns and provenance-dependent persistence.
- Invalidation or expiry: one repair attempt, author-call deadlines, same-name replacement; no automatic tool expiry shown by inspected store.
- Activation or effect: durable code can change later tool execution; correct workflow behavior and real benefit unobserved.
- Evidence limits: simulated smoke success does not cover real table shapes, all branches or business outcomes; routine fallback persistence differs from this endpoint.

Evidence: SRC-1, `agent/src/tools.ts`, `agent/src/service.ts`, `agent/src/store.ts`; [RT-CMP-author-model](#rt-cmp-author-model), [RT-OBJ-stored-tool](#rt-obj-stored-tool).

> if (app && outcome.tool && outcome.authored_by === "model") {
> return json({ ...outcome, via, tool: store.upsertTool(app, outcome.tool) });
> }
> --- `agent/src/service.ts`

> if (/is not a function|is not defined|undefined is not|Cannot read|SyntaxError|ReferenceError|TypeError/.test(d)) {
> return d.slice(0, 240);
> }
> --- `agent/src/tools.ts`

#### RT-RTE-scheduled-tool
Label: Broker routine to persisted tool execution

Endpoints: due custom-app scheduler job → sidecar `/routines/run` → persisted tool matcher or author/upsert → worker run → session/artifact → broker run ring and playbook execution log. Principal identities: app ID, routine slug/name, tool name and returned session ID. Owner: broker chooses timing/live prompt and next run; sidecar matches by exact mention or at least two title-word overlaps; model authors only if needed, and generated code owns capability sequencing. Current playbook text can override frozen job payload. Mode: recurrent scheduled open prompt, not curriculum. Proposer/decider for new capability: model/fallback proposes, software persists; no per-content human admission. No business answer oracle. Authoring guidance/checks are those in [RT-RTE-tool-authoring](#rt-rte-tool-authoring), but routine admission stores any non-null returned tool, including fallback. Rejection/recovery: author/check fallback or error outcome; later same-name replacement; no demonstrated automatic rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: status, digest and session ID; writes prompt/outcome transcript and Markdown artifact on normal completion; broker maps needs_approval to an ok fire with partial outcome.
- Later read-back: next routine reads saved tools and current live playbook; transcript/artifacts are exposed through GET routes, not fed as conversation history into the inspected author call.
- Delegated visibility: worker gets matched/authored code and routine prompt as input; app-scoped capabilities bind data.* to that app. Full historical session is not supplied by this executor.
- Selection predicate: valid custom-app target, due scheduler job and prompt fallback chain; exact tool mention wins over title overlap.
- Invalidation or expiry: scheduler re-arms before async HTTP dispatch; caller timeout is 90 seconds, ordinary worker default 120 seconds; next-run scheduling is not proof prior effects ended.
- Activation or effect: unapproved worker can still perform permitted app data changes; named send/browser calls halt, integration mutations are separately deferred by broker.
- Evidence limits: no execution supplied; an exception before transcript/artifact writes can prevent them despite the source's ALWAYS comment. Caller timeout/auth failure can precede a completed sidecar outcome. No exactly-once guarantee.

Evidence: SRC-1, `internal/team/scheduler.go`, `internal/team/scheduler_operator_routines.go`, `agent/src/service.ts`, `agent/src/routineRunner.ts`, `agent/src/toolRuntime.ts`.

> tool = authored ? store.upsertTool(agent, authored) : null;
> --- `agent/src/routineRunner.ts`

> const r = await execute(tool, { input: routine.prompt }, { approved: false, capabilities, timeoutMs });
> --- `agent/src/routineRunner.ts`

> req.Header.Set("Content-Type", "application/json")
> resp, err := http.DefaultClient.Do(req)
> --- `internal/team/scheduler_operator_routines.go`

The inspected broker POST does not attach an Authorization header, while a configured sidecar token protects this endpoint. Thus these paths do not establish successful scheduled operation with sidecar token authentication enabled. The supervisor passes broker credentials to capabilities; that is a different credential direction. SRC-1, `internal/team/bot_service_supervisor.go`, `agent/src/service.ts`.

#### RT-RTE-saved-call
Label: Saved-tool host capability dispatch

Endpoints: `/tools/call` agent/name/args → stored code → isolated worker → RPC capability host → result/gate/error. Owner: caller selects saved name and approval Boolean; code resolves saved bytes and gates fixed capability paths; generated code chooses calls; capability implementations own broker/model effects. Model-dependent capability calls use [RT-CMP-runtime-ai](#rt-cmp-runtime-ai). Representational form: symbolic JavaScript, RPC paths/args and wire status; natural-language model inputs/results within selected capabilities. Mode: open invocation, no business answer oracle. Human approval's provenance is unresolved at this API: it tests a Boolean, not a human-decision token. Grant set depends on configured capability tree; the full capability surface exceeds send/browser.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: result string, traced capability actions and ok/needs_approval/error status; worker final objects are JSON-serialized and capped at 200,000 characters.
- Later read-back: saved code is loaded on each invocation; app data mutations can reach later calls; this endpoint itself does not append routine transcript/artifact history.
- Delegated visibility: worker receives proxy paths rather than host implementations/credentials; capability calls receive arguments and return JSON-safe values; AI calls use fresh request contexts.
- Selection predicate: stored agent/name, identifier/code scans, known capability path and named gate plus approved flag.
- Invalidation or expiry: default 120-second worker deadline, termination and host AbortSignal; code updates replace saved tool; completed upstream effects are not undone.
- Activation or effect: data.upsert can write app state without send-gate approval; nex.send/nex.browser gate before invoking their registered host function; integrations.call uses broker action classification independently.
- Evidence limits: Worker thread is not a proven adversarial security sandbox. Parameter shadowing and import/eval scans leave residual ambient authority explicitly acknowledged in source. Simulated/hash AI fallback can return ok without successful model inference.

Evidence: SRC-1, `agent/src/service.ts`, `agent/src/toolRuntime.ts`, `agent/src/toolSandboxWorker.ts`, `agent/src/capabilities.ts`, `internal/team/broker_apps_integrations.go`.

> approved: body.approved === true,
> --- `agent/src/service.ts`

> if (GATED_CAPABILITIES.has(path) && !ctx.approved) throw new GateError(path, gateDetail(path, args));
> return await fn(...args);
> --- `agent/src/toolRuntime.ts`

> export const GATED_CAPABILITIES: ReadonlySet<string> = new Set(["nex.send", "nex.browser"]);
> --- `agent/src/capabilities.ts`

> if !readOnly {
> requestID := b.raiseAppActionApproval(r, platform, actionID, req.Params)
> --- `internal/team/broker_apps_integrations.go`

> return `Held for your approval in WUPHF (request ${body.request_id ?? "pending"}) — nothing was sent yet.`;
> --- `agent/src/capabilities.ts`

> // Residual ambient authority (fetch etc. exist in a worker) is still reduced by
> // strict-mode parameter shadowing + the host's code scan — same defense-in-depth
> // as before; the hard containment this file adds is TERMINATION + no shared state
> // with the service. TODO(security): a permissioned runtime for full authority
> // stripping.
> --- `agent/src/toolSandboxWorker.ts`

#### RT-RTE-spec-replay
Label: Supplied workflow specification replay

Endpoints: optional `/build/stream` single model compilation → validated WorkflowSpec; independently, `/run` supplied spec → ordered deterministic steps → HTTP replay or simulation. Owner: author model proposes spec; caller supplies final spec/input; executor decides progression by fixed step fields and HTTP result. State: steps, input.approved IDs and current result list. The public run handler does not require prior build identity or resolve through stored tool code. Mode: open compilation/execution, not an experiment. Answer oracle: HTTP success is transport acceptance, not correctness of the requested workflow. Admission: caller-controlled symbolic spec; rejection: parse/shape/schema-version guards and gated-step checks; recovery: stop on failed API, client rerun; no compensation/rollback is implemented in the inspected executor.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: done/needs_approval/error with step list and digest; build SSE reveals assembled steps after the single compilation returns.
- Later read-back: inapplicable — the inspected run handler/executor do not persist or reload the spec; callers may do so outside this traced segment.
- Delegated visibility: BUILD model sees schema prompt and description; replay sees supplied API URL/method/headers/body and optional credentials; no tool worker frame.
- Selection predicate: declared step order; step.gated plus approved IDs; step.api selects fetch versus simulated success.
- Invalidation or expiry: API timeout defaults to 30 seconds; redirects are not followed; failure stops remaining steps; client reruns can repeat earlier successful steps.
- Activation or effect: real fetch can produce external effects; absent api yields simulated ok; ungated descriptors bypass the capability gate and broker integration classifier.
- Evidence limits: caller-supplied gated field is not server-derived action classification; HTTP outcome does not show human authorization or business success. Effective outbound network envelope unobserved.

Evidence: SRC-1, `agent/src/service.ts`, `agent/src/buildAgent.ts`, `agent/src/executor.ts`; [RT-CMP-author-model](#rt-cmp-author-model).

> return json(await runWorkflow(body.spec, body.input ?? {}));
> --- `agent/src/service.ts`

> if (step.gated && !approved.has(step.id)) {
> --- `agent/src/executor.ts`

> if (step.api) {
> const r = await replay(step.api, opts);
> --- `agent/src/executor.ts`

#### RT-RTE-app-publication
Label: App byte publication and restoration

Endpoints: enabled agent `register_app` → broker `/apps` → appStore.Save; alternate authorized human POST; restore endpoint → appStore.Rollback. Owner: model/human proposes bytes; MCP checks app-building skill; broker authenticates writer and checks appWriterAllowed; store admits or rejects. Mode: open requested build/improvement or proposal-authorized build; no answer oracle established by registration. Guidance: caller's build description and app-building instructions; the complete prompt/build verification procedure is uninspected here. Rejection ability: capability/authentication and store errors; no per-build human content approval in these handlers. Rollback: authenticated allowed writer can request retained version. Exact store validation, retained-version pruning and executable app sandbox remain uninspected, preventing a full product-admission guarantee.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: published app or error; publication schedules workflow precompile and starter-routine creation in background.
- Later read-back: app store and version routes expose retained builds; next app execution/compiled workflow consumption is only partly traced.
- Delegated visibility: register_app sends resolved HTML/files and metadata to broker; end-user UI execution context uninspected.
- Selection predicate: app-building system skill or human session, authenticated actor, optional existing app ID; rollback chooses version.
- Invalidation or expiry: replacement/publication and explicit version restoration; pruning and cache invalidation uninspected.
- Activation or effect: admits bytes to product app registry and schedules downstream routines/compilation; actual successful rendering and routine behavior unobserved.
- Evidence limits: handler admission is not semantic validation, observed human review or successful production deployment. App-store internals and full app-client controls not traced.

Evidence: SRC-1, `internal/teammcp/app_tools.go`, `internal/team/broker_apps.go`.

> if !systemSkillEnabledFor(ctx, systemSkillAppBuilding, slug) {
> return toolError(systemSkillDisabledError(systemSkillAppBuilding, slug)), nil, nil
> }
> --- `internal/teammcp/app_tools.go:261-263`

> app, err := b.appStore().Save(body, time.Now())
> --- `internal/team/broker_apps.go`

> app, err := b.appStore().Rollback(id, body.Version, actor, time.Now())
> --- `internal/team/broker_apps.go`

### Claims

#### RT-CLM-external-approval
Label: Human approval of external actions

Claimed operation: local agents build microapps and wait for a human click for every send, commit, purchase and delete. Evidence layer: doctrine/design, not observed operation. Source: SRC-1, `README.md`.

> | Approvals | Bots act on your accounts around the clock | Every send, commit, purchase, and delete waits for your click |
> --- `README.md`

- claim conclusion status: claimed

The inspected implementation provides several route-local gates, not this universal property: native execution permission bypass, caller-supplied approval and direct API replay require separate trust/enforcement assumptions. See [RT-RTE-office-turn](#rt-rte-office-turn), [RT-RTE-saved-call](#rt-rte-saved-call), [RT-RTE-spec-replay](#rt-rte-spec-replay). This challenges the broad claim without asserting that an unauthorized action was observed.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-tool-execution
Label: Stored code to worker behavior

Consumer: tool worker and host capability dispatcher. Channel: stored tool lookup or routine matching → code compiled by `new Function` → capability RPC. Force: symbolic executable control of step sequence and arguments, bounded by host table/gates and imperfect worker isolation; not merely advisory prose. Horizon: later calls and scheduled runs across sessions until replacement/file loss. Evidence: SRC-1, `agent/src/store.ts`, `agent/src/routineRunner.ts`, `agent/src/toolRuntime.ts`, `agent/src/toolSandboxWorker.ts`; [RT-OBJ-stored-tool](#rt-obj-stored-tool), [RT-RTE-saved-call](#rt-rte-saved-call).

> const value: unknown = await compiled(
> ...capRoots.map((n) => caps[n]),
> ...msg.argValues,
> ...msg.shadowedGlobals.map(() => undefined),
> );
> --- `agent/src/toolSandboxWorker.ts`

#### RT-BAP-author-guidance
Label: Authoring instructions to executable proposal

Consumer: author model, followed by software admission and later worker. Channel: TOOL_SCHEMA_PROMPT plus fetched app schema and user brief → model result → checked tool. Force: natural-language guidance at proposal generation, not guaranteed compliance; accepted code later has executable force through [RT-BAP-tool-execution](#rt-bap-tool-execution). Horizon: current author call, with effects persisting in saved code rather than retained prompt rationale. Evidence: SRC-1, `agent/src/tools.ts`; [RT-OBJ-tool-schema](#rt-obj-tool-schema), [RT-RTE-tool-authoring](#rt-rte-tool-authoring).

> systemPrompt: TOOL_SCHEMA_PROMPT + appSchemaBlock(opts.appSchema),
> --- `agent/src/tools.ts`

## Annotations

none
