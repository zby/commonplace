---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Phantom runtime baseline: channel and durable chat execution, SDK controls, dynamic capabilities and reflection admission at the frozen revision."
run-id: AAS-2026-10-15-phantom-cc566f03ac40-01
reviewed-boundary: "f8c7ab42d885936ee54abc785528000260f4acc5"
---

# Phantom runtime report

## Runtime account

### Evidence and consequential work

Phantom owns the service around an SDK-controlled model/tool loop. It admits requests from channels, browser chat, MCP clients, HTTP triggers and scheduled jobs; constructs prompts; provisions tool servers; coordinates sessions; and retains results. Its declared work includes autonomous workstation tasks and improvement through retained configuration. The runtime can execute effects, not just return advice. That capability must be separated from the grants in any deployment and from successful task completion. [SRC-1: `src/agent/runtime.ts`, `src/index.ts`, `src/agent/prompt-assembler.ts`]; claim: [RT-CLM-autonomous-worker](#rt-clm-autonomous-worker).

The [boundary](boundary.md) supplies the sole source, SRC-1. All new inspection below is implementation evidence unless explicitly called doctrine/design. No target code was executed and no observed-run or causal-experiment evidence was supplied. Invocation, activation, recovery effectiveness and benefit therefore remain unobserved. This is not evidence that those behaviors never occur.

Added source coverage at the same pin comprises the ordinary runtime and permissions helper; chat query/writer/continuity/context transform; hooks and SDK loader; providers and session storage; scheduler executor and HTTP trigger; MCP authentication, ask/task tools, dynamic registry and subprocess handlers; dashboard configuration, plugins, skills, subagents and hook surfaces; and reflection runner, snapshot and selected invariant/engine/gate branches. Target architecture and reflection teaching text supply doctrine/design. This extends the boundary's initial inspection without adding a source identity. [SRC-1: `src/agent/permission-options.ts`, `src/agent/chat-query.ts`, `src/chat/writer.ts`, `src/chat/continuity-context.ts`, `src/agent/murph-context.ts`, `src/mcp/dynamic-handlers.ts`, `src/ui/api/phantom-config.ts`, `src/hooks/storage.ts`, `src/evolution/versioning.ts`, `docs/architecture.md`, `src/evolution/subprocess-prompt.ts`]

### Ordinary shipped invocation

The shipped CLI/start drivers reach `src/index.ts`, as established in the boundary. Startup loads configuration, opens and migrates SQLite, initializes memory, creates `AgentRuntime`, loads a role, and wires evolution and its cadence. A ready vector store enables context retrieval; failed evolution initialization leaves a service without that engine. Factories create session-associated in-process MCP servers for dynamic management, scheduling, reflective functions, pages, secrets, preview/browser and conditional email. Channels register with the router. [SRC-1: `src/index.ts`]; [RT-RTE-channel-work](#rt-rte-channel-work).

For a normal channel message, the channel adapter is the ingress principal; channel ID and conversation ID identify the runtime session, while sender ID belongs to the surrounding message and learning summary. The router invokes the startup callback, which accumulates user/assistant text, starts channel progress indicators, calls `handleMessage`, delivers its terminal text, then launches nonblocking vector consolidation and evolution submission. Those follow-up calls belong to this callback, not to every use of the runtime. [SRC-1: `src/channels/router.ts`, `src/index.ts`]

`handleMessage` rejects a second simultaneous call with the same key using an in-process Set, adds prompt-level security wrapping for channels other than `scheduler` and `trigger`, and releases the key in `finally`. It finds or creates a SQLite session; a stored SDK session ID enables resume. The prompt assembler appends identity, environment, security, role, optional onboarding, evolved configuration, memory-writing guidance, working-memory text and retrieved memory to the SDK's `claude_code` preset. Agent notes are deliberately not injected automatically. The model, not the TypeScript wrapper, chooses subsequent tool actions through the SDK loop. Natural-language guidance and numerical model inference interact with symbolic runtime options and tool schemas. [SRC-1: `src/agent/runtime.ts`, `src/agent/session-store.ts`, `src/agent/prompt-assembler.ts`]; [RT-BAP-prompt-guidance](#rt-bap-prompt-guidance).

The SDK receives project/user settings sources, persistent sessions, provider environment, optional budget, effort/thinking, timeout abort controller, pre-tool Bash blocker, post-tool Edit/Write tracker and freshly created MCP servers. It owns inner tool progression and dependency-level compaction/delegation. Phantom consumes system initialization, assistant and result events, records session IDs and cost, and returns final text/session ID/cost/duration. A stale SDK conversation gets one retry without resume. Other errors become `Error:` text on this channel path. The caller then delivers that text. Filesystem, shell, Docker, browser, email and service callbacks can have already caused effects; returning an error is not a transaction rollback. [SRC-1: `src/agent/runtime.ts`, `src/index.ts`]; component: [RT-CMP-main-model](#rt-cmp-main-model).

### Alternate work and context paths

Browser chat is a different driver, not a cosmetic channel wrapper. A cookie-authenticated API claims a session writer; the writer commits user messages and attachments, persists translated SDK events and a durable run timeline, and calls `runForChat` with `web:<sessionId>`. That query path emits partial messages and SDK progress, supports client abort, commits assistant text after successful execution, and emits durable error/aborted terminal frames otherwise. Reconnection replays event state; it does not prove an interrupted model invocation was resumed after a process restart. [SRC-1: `src/chat/http.ts`, `src/chat/http-handlers.ts`, `src/chat/writer.ts`, `src/agent/chat-query.ts`]; [RT-RTE-durable-chat](#rt-rte-durable-chat).

For chat, Phantom reconstructs a bounded continuity supplement from up to 5,000 recent events plus durable timeline artifact summaries. It extracts page artifacts, deduplicates them, retains at most eight, and includes at most three compaction checkpoints. It excludes authentication links from page artifacts and asks the agent to search the transcript when details are missing. The ordinary SDK gets this in the appended prompt. With configured Murph, a transform removes earlier tagged Phantom-context messages and injects a fresh one before the last user message, or at the end otherwise. It does not itself compact the transcript. The deciding agent for this selection/replacement is code; the SDK owns any actual transcript compaction. Removed supplements remain reconstructible from host stores, while omitted conversational details are not restored by this artifact-only supplement. Subagent frame inputs, tool restrictions, compaction thresholds and the exact text returned across SDK delegation remain dependency-internal and uninspected. Skills expose an `inline`/`fork` setting, but that schema alone does not establish execution of separate contexts. [SRC-1: `src/chat/continuity-context.ts`, `src/agent/murph-context.ts`, `src/agent/chat-query.ts`, `src/skills/frontmatter.ts`]; [RT-RTE-chat-context](#rt-rte-chat-context).

Scheduled jobs call `handleMessage("scheduler", "sched:<id>", task)`, update status/counters, advance recurrence or backoff, deliver results and optionally delete completed jobs. A busy session causes a skipped fire without advancing job state. HTTP `/trigger` requires operator-scoped bearer authentication and calls the same runtime under a fresh UUID key, optionally delivering to Slack and returning JSON. MCP `phantom_ask` and SWE review also call the runtime directly. These do not pass through the channel callback's consolidation/evolution wiring. MCP task creation, by contrast, is a queued-row insertion; the bounded search in [RT-ABS-task-executor](#rt-abs-task-executor) did not establish a task executor. [SRC-1: `src/scheduler/executor.ts`, `src/core/server.ts`, `src/mcp/tools-universal.ts`, `src/mcp/tools-swe.ts`]; [RT-RTE-direct-work](#rt-rte-direct-work).

### Guarantees and forcing cases

These are scoped controls, not one global safety guarantee. The capability surface includes workstation tools, in-process callbacks, external MCP clients, SDK settings/plugins/hooks and arbitrary registered script/shell handlers. The actual grant set depends on configured permissions, supplied credentials/settings and channel controls. The shipped full-stack Compose file runs a non-root application image but mounts the host Docker socket and persistent credentials/configuration. It sets memory/process resource limits, not a proof of hostile-code isolation. No deployed envelope was captured. [SRC-1: `src/agent/runtime.ts`, `src/agent/permission-options.ts`, `src/index.ts`, `src/mcp/dynamic-handlers.ts`, `Dockerfile`, `docker-compose.yaml`]

| Control and owner | Enforcement point and strength | Covered paths and contrary/alternate path | External contract and conclusion statuses |
|---|---|---|---|
| Session serialization, `AgentRuntime` | Set membership before query; **invariant** within one instance | Both foreground methods; independent keys still run concurrently; not a distributed lock or evolution/file-edit lock | Single service-instance coordination; implementation conclusion status: wired; operation conclusion status: uninspected |
| Operator tool grants, Phantom/SDK | Permission options passed to foreground queries; **policy** | Channel and chat query helpers; default is bypass, configurable allow/deny lists. Judge and reflection use separate fixed bypass options; host subprocess handlers do not traverse this helper | Selected SDK must implement option semantics; no claim that the dependency honors every option; implementation conclusion status: wired; operation conclusion status: uninspected |
| Destructive command screening, Phantom hook | PreToolUse matcher `Bash`; **best effort** | Direct matching Bash inputs only; dynamic MCP handlers spawn Bash outside this hook; encoding/indirect execution and other tools are not equivalent covered paths | SDK hook invocation; implementation conclusion status: wired; operation conclusion status: uninspected |
| External client grants, MCP server | Bearer hash lookup, rate limit and pretransport per-tool scope; **policy** | MCP HTTP requests, including batch calls; not the SDK's in-process tool factories. Dynamic unknown tool names default to read scope | Correct token provisioning and transport behavior; implementation conclusion status: wired; operation conclusion status: uninspected |
| Reflection file protection, evolution runner | Tool allowlist/settings plus post-state invariant check and snapshot restoration; **protocol** | Reflection ok admission, including compaction change actions, over snapshot-covered files; not main-agent or dashboard writes, and not every sentinel branch | SDK tool/permission semantics, accessible files and successful restoration; implementation conclusion status: wired; operation conclusion status: uninspected |

[SRC-1: `src/agent/runtime.ts`, `src/agent/chat-query.ts`, `src/agent/permission-options.ts`, `src/agent/hooks.ts`, `src/mcp/server.ts`, `src/mcp/auth.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/versioning.ts`]

Four forcing cases materially change the interpretation:

1. **A registered MCP tool runs shell outside the Bash hook.** Registration validates shape and persists code/path; invocation uses `Bun.spawn(["bash", "-c", command], ...)` or Bun script execution. A reduced environment is not a filesystem/network sandbox. The external admin requirement for registration also does not describe in-process agent registration. See [RT-RTE-dynamic-tools](#rt-rte-dynamic-tools). [SRC-1: `src/agent/in-process-tools.ts`, `src/mcp/dynamic-tools.ts`, `src/mcp/dynamic-handlers.ts`, `src/mcp/auth.ts`]
2. **Web continuity survives through host stores, not an identical transcript.** The artifact supplement and Murph replacement transform establish selective delivery; they establish neither complete recall nor successful model use. The channel callback's learning route cannot be assigned to web chat from a shared runtime name. See [RT-RTE-chat-context](#rt-rte-chat-context). [SRC-1: `src/chat/writer.ts`, `src/chat/continuity-context.ts`, `src/agent/murph-context.ts`, `src/index.ts`]
3. **Not every query uses foreground controls.** Judge queries use bypass mode, one maximum turn and no persistent session; omitting the preset is not an explicit empty tools allowlist. Reflection has a different allowlist and no project/user settings. An environment-selected SDK module only has its exported functions checked, not its security semantics. Thus configured foreground permissions are not a system-wide confinement argument. See [RT-RTE-judge-call](#rt-rte-judge-call). [SRC-1: `src/agent/judge-query.ts`, `src/evolution/reflection-subprocess.ts`, `src/agent/agent-sdk-loader.ts`]
4. **Reflection's post-check is branch-limited.** Error and escalation paths attempt restoration; ok executes invariants, including for compaction change actions. A `skip` sentinel returns without post-state checking or restoration. Malformed sentinels instead fall back to ok and run invariants. The snapshot excludes top-level `meta/` and `.staging/`; therefore invariant checks for changes there do not gain coverage merely by naming those directories. The sentinel parser accepts only `ok`, `skip` and `escalate`; compaction is a change action, not an admitted status. Committed compaction returns changed `ok`, so it follows `runDrainPipeline`'s live evolved-config refresh callback. The skip and snapshot weaknesses are source-supported qualifications, not executed exploit demonstrations. [SRC-1: `src/evolution/reflection-subprocess.ts`, `src/evolution/versioning.ts`, `src/evolution/invariant-check.ts`, `src/evolution/engine.ts`]; [RT-RTE-reflection-admission](#rt-rte-reflection-admission).

The minimum passages supporting these control limits are retained in the corresponding route records. No claim is made about all provider-native tool pathways, remote-worker internals, SDK manual control APIs or deployment firewall rules: these were not supplied or not inspected. Shipped caller options and callbacks are inspectable; dependency enforcement and live settings are not. Slack's owner check is conditional on an owner ID being configured, not a universal owner-only property of `AgentRuntime`. [SRC-1: `src/channels/slack.ts`, `src/agent/agent-sdk.ts`, `src/agent/agent-sdk-loader.ts`]

### Change admission and authority

There are several distinct change planes. Trace-fed evolution uses model selection and file edits plus software admission; foreground file/shell actions can directly change work products, persistent instructions and machinery under the process's actual rights; dynamic-tool registration retains executable capabilities; authenticated dashboard writes edit skills, subagents, hooks, plugins and YAML. They do not share one reviewer, answer oracle, rollback or consumption horizon. Browser preview instructions ask the main agent to validate pages; this is model-followed guidance, not an enforced success gate. [SRC-1: `src/agent/prompt-assembler.ts`, `src/evolution/reflection-subprocess.ts`, `src/agent/in-process-tools.ts`, `src/ui/serve.ts`]; [RT-RTE-operator-config](#rt-rte-operator-config), [RT-BAP-handler-execution](#rt-bap-handler-execution).

The operator configuration API writes YAML atomically per file and returns dirty keys. Its handler does not update the runtime's captured config object; the runtime and startup were inspected for reload wiring and none was established on this save path. Do not repeat the permissions helper comment's next-message activation claim as proven. By contrast, evolution has an explicit callback installing a newly loaded evolved-config snapshot after changed `ok` results, including admitted compaction. That snapshot selects constitution, persona, user profile, domain knowledge and three fixed strategy files; corrections/principles and arbitrary new strategy files require promotion into a selected file before automatic foreground evolved-section consumption. Detailed retained-memory revisions belong to the memory analyst; this member establishes runtime admission and consumers, not an independent memory inventory. [SRC-1: `src/ui/api/phantom-config.ts`, `src/index.ts`, `src/agent/runtime.ts`, `src/agent/permission-options.ts`, `src/evolution/engine.ts`]

## Shared records

### Components

#### RT-CMP-main-model
Label: Main agent model

Source-native identity: `config.model`, shipped example `claude-opus-4-7`, resolved by `resolveAgentRuntimeModel` and provider environment. Representational form: distributed-parametric inference; parameters reside in an external provider or local model service, not Phantom's SQLite/text stores. Used by channel, chat and direct work. No parameter-update operation is present in these inspected wrappers; whether provider parameters change is uninspected. Exact weights/version are not pinned by the repository's model string. Configurable base URLs, aliases/mappings and mutable provider endpoints can resolve differently. SDK/backend internals are outside SRC-1. [SRC-1: `config/phantom.yaml`, `src/config/providers.ts`, `src/agent/runtime.ts`, `src/agent/chat-query.ts`]

> const queryModel = resolveAgentRuntimeModel(this.config, this.config.model);
> --- `src/agent/runtime.ts`

#### RT-CMP-judge-model
Label: Judge model

Source-native identity: judge query model, including `JUDGE_MODEL_HAIKU` for the evolution gate. Representational form: distributed-parametric; substrate: external provider/service inference. Separate from the main component by role, call options and lifecycle, even if provider mappings collapse them to one backend. Phantom does not update its parameters in the inspected call; exact numerical version is not pinned, and configurable mappings/endpoints can change the resolved model. Provider-side mutation remains uninspected. [SRC-1: `src/agent/judge-query.ts`, `src/evolution/gate.ts`, `src/config/providers.ts`]

> const evolve = result.data.evolve === true;
> --- `src/evolution/gate.ts`

#### RT-CMP-reflection-model
Label: Reflection tier models

Source-native identity: `TIER_MODELS` at Haiku, Sonnet and Opus, remappable through provider configuration. Representational form: distributed-parametric; substrate: provider/local inference service. The same admission mechanism uses successively selected tiers, not inspected parameter training. No weight updates occur in the wrapper; exact weights are unpinned and endpoint resolution is mutable. Escalating model tier is not a change to model parameters. [SRC-1: `src/evolution/reflection-subprocess.ts`, `src/config/providers.ts`]

> return await runTier("haiku", null);
> --- `src/evolution/reflection-subprocess.ts`

#### RT-CMP-embedding-client
Label: Ollama embedding model

Source-native identity: embedding client using configured Ollama model, shipped `nomic-embed-text`. Representational form: distributed-parametric model and dense output vectors; substrate: external Ollama inference and memory-system vector storage. It embeds text for retrieval rather than choosing tool steps. The client performs inference, not parameter updates. Exact model digest is unpinned and the configured service/model name may resolve to a replacement. Internal model state and initial vector provenance are not established here. [SRC-1: `src/memory/embeddings.ts`, `config/memory.yaml`; memory consumer wiring: `src/index.ts`, `src/agent/runtime.ts`]

> body: JSON.stringify({ model: this.model, input: text }),
> --- `src/memory/embeddings.ts`

### Operative objects

#### RT-OBJ-session-store
Label: Runtime session rows

Source-native identity: `SessionStore` / SQLite `sessions`. Symbolic rows map channel/conversation keys to SDK IDs, status and timestamps; the SDK's own persisted conversation is a separate opaque dependency-owned object. The active-session Set is transient coordination, not durable memory. Rows expire after 24 hours of inactivity when looked up; reactivation clears the old SDK ID. SQL storage alone does not preserve the SDK transcript. [SRC-1: `src/agent/session-store.ts`, `src/agent/runtime.ts`]

> const STALE_HOURS = 24;
> --- `src/agent/session-store.ts`

#### RT-OBJ-dynamic-tools
Label: Dynamic tool definitions

Source-native identity: `DynamicToolRegistry`, SQLite `dynamic_tools` and an in-process Map. Operative parts: name/input-schema/type/path and executable shell/script code are symbolic at their consumers; natural-language descriptions guide model selection. Script file contents reside outside the row and can change independently of registration. Startup reloads definitions; new MCP server creation enumerates them. No model-quality approval is implied by registry insertion. [SRC-1: `src/mcp/dynamic-tools.ts`, `src/mcp/dynamic-handlers.ts`]

> this.tools.set(def.name, def);
> console.log(`[dynamic-tools] Registered tool: ${def.name}`);
> return def;
> --- `src/mcp/dynamic-tools.ts`

#### RT-OBJ-chat-context
Label: Phantom chat context supplement

Source-native identity: output of `buildChatContinuityContext`, computed from retained event-log and timeline-store content. Rendered natural language carries host facts and retrieval instructions to a model; symbolic extraction/filtering limits its contents. Substrate: transient prompt/transform string backed by durable chat stores. It is not a full conversation copy or itself a vector memory. [SRC-1: `src/chat/continuity-context.ts`, `src/chat/writer.ts`, `src/agent/murph-context.ts`]

> const MAX_ARTIFACTS = 8;
> const MAX_COMPACTIONS = 3;
> --- `src/chat/continuity-context.ts`

### Routes

#### RT-RTE-channel-work
Label: Channel message execution

Endpoints/progression: registered channel → router callback → `handleMessage` → SDK model/tool loop → caller delivery; callback then starts vector consolidation and evolution submission. Owner: service callback for outer progression, SDK/model for next tool decision. Context combines current input, resumed SDK history and assembled text. Effects can reach tools before any response. Runtime state is [RT-OBJ-session-store](#rt-obj-session-store); model is [RT-CMP-main-model](#rt-cmp-main-model). [SRC-1: `src/channels/router.ts`, `src/index.ts`, `src/agent/runtime.ts`, `src/agent/prompt-assembler.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AgentResponse, then channel-specific final delivery/progress update.
- Later read-back: SDK session resume and assembled retained context on subsequent invocations; channel callback also submits traces to distinct memory/evolution paths.
- Delegated visibility: SDK receives prompt, settings sources, environment and per-session MCP servers; SDK internal subagent context transfer is uninspected.
- Selection predicate: same channel/conversation key, active nonstale row; memory builder queries on incoming text; one active foreground execution per key.
- Invalidation or expiry: 24-hour inactivity check; missing SDK conversation clears its ID and retries once; active key released in finally.
- Activation or effect: query and tool invocation are wired; actual model compliance and task effects remain unobserved.
- Evidence limits: Source only; returning text or an Error prefix is not an independently checked task outcome. File tracker covers named Edit/Write outputs, not all filesystem effects.

Decision policy: model-generated actions under assembled natural-language instructions and SDK symbolic options. Operating mode: open-ended user requests. Answer oracle: no fixed expected answer in this path; users may later give feedback. For ordinary file/shell changes the foreground model proposes and acts, SDK permissions can reject under their external contract, and no per-content human approval is wired by this wrapper. Default permission mode is bypass. Persistent file changes and installed services can outlast the query; generic rollback is not implemented here. [SRC-1: `src/agent/runtime.ts`, `src/agent/permission-options.ts`, `src/agent/hooks.ts`]

> if (isResume && errorMsg.includes("No conversation found")) {
> --- `src/agent/runtime.ts`

> hooks: { PreToolUse: [commandBlocker], PostToolUse: [fileTracker.hook] },
> --- `src/agent/runtime.ts`

#### RT-RTE-durable-chat
Label: Durable browser chat execution

Endpoints/progression: authenticated chat stream request → claim writer → commit user message → `runForChat`/`executeChatQuery` → translate SDK events → event log/stream/timeline → assistant commit or terminal error. Owner: HTTP handler and writer for durable outer lifecycle; SDK/model for inner next step. Distinct from the channel callback's post-response learning. [SRC-1: `src/chat/http.ts`, `src/chat/http-handlers.ts`, `src/chat/writer.ts`, `src/agent/chat-query.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE response while writer runs asynchronously; SDK frames and eventual text/error/aborted state reach subscribers.
- Later read-back: message history, persisted event replay and timeline/artifact-based continuity supplement; SDK resume also requested.
- Delegated visibility: text/attachment message, continuity supplement, main prompt, project/user settings and session-aware tool factories; dependency delegation internals uninspected.
- Selection predicate: cookie authentication, existing session and no active writer; runtime separately checks session-key busy state.
- Invalidation or expiry: active-writer entry removed in finally; client abort forwarded to SDK controller; stale SDK ID retried without resume; ordinary runtime session expiry also applies.
- Activation or effect: persistence, event emission and SDK options are wired; no observed continuity success or model tool effects.
- Evidence limits: Durable UI transcript and SDK conversation are not identical. An aborted/error run can retain events without a committed assistant message; restart recovery does not establish automatic re-execution.

Open-request operating mode and foreground action admission match the main query, with separate chat persistence and external abort. No fixed answer oracle is supplied. Ordinary tool effects do not roll back with an aborted stream. [SRC-1: `src/chat/writer.ts`, `src/agent/chat-query.ts`]

> const sessionKey = `web:${this.deps.sessionId}`;
> --- `src/chat/writer.ts`

> options.signal.addEventListener("abort", () => controller.abort(), { once: true });
> --- `src/agent/chat-query.ts`

#### RT-RTE-chat-context
Label: Chat continuity reconstruction

Endpoints/progression: writer's context provider → bounded retained-event/timeline extraction → appended prompt or Murph transform → model. Owner/decider: code selects and replaces context; SDK owns compaction and model decides whether to follow retrieval guidance. Operative result: [RT-OBJ-chat-context](#rt-obj-chat-context). [SRC-1: `src/chat/writer.ts`, `src/chat/continuity-context.ts`, `src/agent/chat-query.ts`, `src/agent/murph-context.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rendered context string or transformed message array, not a user-visible answer.
- Later read-back: earlier page artifacts and compaction events feed subsequent query context; provider can rebuild during Murph callbacks.
- Delegated visibility: context injected as a tagged user-role message for configured Murph, otherwise appended system-prompt text; further SDK propagation uninspected.
- Selection predicate: session ID, recent event tail, supported page-tool identities, parseable artifact fields, URL/path filters, deduplication and artifact/checkpoint caps.
- Invalidation or expiry: Murph transform removes previous tagged context messages before adding fresh context; bounded extraction omits older/unselected material but does not delete source stores.
- Activation or effect: selective context delivery is wired; changed decisions and compaction recovery remain unobserved.
- Evidence limits: A page-artifact supplement cannot establish complete recall; transcript-search instruction is a requested reload route, not evidence it was used. Host compaction algorithm and subagent frame boundaries remain uninspected.

The stack-frame analogy applies only loosely: this transform replaces a host supplement, not a subordinate reasoning frame whose return value alone escapes. It leaves the rest of the SDK message array in place. External records are brought back by value as text, not dereferenceable pointers in model memory. [SRC-1: `src/agent/murph-context.ts`, `src/chat/continuity-context.ts`]

> const cleaned = messages.filter((message) => !isPhantomContextMessage(message));
> const trimmed = (await context())?.trim();
> if (!trimmed) return cleaned;
> return injectContext(cleaned, trimmed);
> --- `src/agent/murph-context.ts`

#### RT-RTE-direct-work
Label: Scheduled and direct runtime work

Endpoints/progression: scheduler job → runtime → delivery/status/backoff; authenticated HTTP trigger → runtime → optional Slack delivery/JSON; operator-scoped MCP ask or review → runtime → MCP text. Owners are their respective shipped callers, with the SDK/model retaining next-tool choice. They share foreground runtime effects, not the router callback. [SRC-1: `src/scheduler/executor.ts`, `src/core/server.ts`, `src/mcp/tools-universal.ts`, `src/mcp/tools-swe.ts`, `src/mcp/server.ts`, `src/mcp/auth.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: job result string and stored delivery/run outcome, HTTP JSON, or MCP content with response/cost/duration.
- Later read-back: recurring job task/schedule/status and SDK session keyed to the job; trigger UUIDs and timestamp-based MCP ask keys generally start distinct sessions; shared memory context still available through runtime wiring.
- Delegated visibility: same main runtime/tool surface; scheduler and trigger omit the extra message security wrapper but still receive assembled security guidance.
- Selection predicate: due or explicitly fired job and nonbusy job session; trigger operator token; MCP named-tool scope/rate checks.
- Invalidation or expiry: scheduler advances cadence/backoff, disables after configured error-count logic and can delete completed one-shots; runtime timeout/session rules remain in effect.
- Activation or effect: direct queries, response delivery and scheduler bookkeeping are wired; task success uses response/error conventions, not an external correctness oracle.
- Evidence limits: No supplied runs; these caller paths do not themselves show channel-style consolidation/evolution submission.

Operating modes: self-contained scheduled instructions and open external requests. No fixed answer oracle. For resulting product/capability/machinery changes, proposal/admission and lack of generic rollback are the same scoped foreground mechanism as [RT-RTE-channel-work](#rt-rte-channel-work), not a separate validated deployment pipeline. [SRC-1: `src/scheduler/executor.ts`, `src/agent/runtime.ts`]

> const response = await ctx.runtime.handleMessage("scheduler", `sched:${job.id}`, job.task);
> --- `src/scheduler/executor.ts`

#### RT-RTE-judge-call
Label: Short judge query and SDK selection

Endpoints/progression: caller (`decideGate`, auto-rename or other judge user) → `judgeQuery` → configured SDK query → text/JSON parsing → caller's decision. SDK selection is an enclosing execution alternative: module override, default Anthropic or optional Murph-compatible module. Owner: caller chooses question/schema; judge model proposes result; code parses and applies caller-specific decisions. [SRC-1: `src/agent/judge-query.ts`, `src/evolution/gate.ts`, `src/chat/auto-rename.ts`, `src/agent/agent-sdk-loader.ts`, `src/agent/agent-sdk.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed data/verdict/confidence/reasoning and cost, or structured subprocess error with partial cost.
- Later read-back: gate logs/statistics and queued session data can persist; judge query itself sets persistSession false. Retained gate outcome consumption is part of evolution, not SDK transcript resume.
- Delegated visibility: plain prompt when omitPreset is set, otherwise preset prompt; provider environment and JSON-schema instructions; no foreground MCP factories or command-blocker hook supplied here.
- Selection predicate: explicit caller invocation and requested model; module environment override takes priority; export checking only verifies function presence.
- Invalidation or expiry: one maximum turn and nonpersistent SDK session; parse/result/stream failures reject the judge call; gate catches failures and defaults to enqueue.
- Activation or effect: parsed evolve boolean controls queue eligibility; actual judgment validity and provider semantics unobserved.
- Evidence limits: maxTokens is a caller option but is not shown as an SDK max-output setting in the inspected query options. A plain system prompt is not an explicit no-tools restriction. Dependency compatibility/security is not proved by accepting an exported query function.

Operating mode: short bounded model evaluation, not a controlled causal experiment. Answer oracle: no supplied expected answer for durable-signal selection or title generation; model judgment is not an answer oracle. Human contribution: upstream user messages/corrections, not per-gate approval. Model can vote skip; code fail-opens on exceptions. [SRC-1: `src/evolution/gate.ts`, `src/agent/judge-query.ts`]

> permissionMode: "bypassPermissions",
> allowDangerouslySkipPermissions: true,
> systemPrompt,
> maxTurns: 1,
> --- `src/agent/judge-query.ts`

> if (typeof imported.query !== "function") {
> throw new Error(`${AGENT_SDK_MODULE_ENV} module must export a query function.`);
> }
> --- `src/agent/agent-sdk-loader.ts`

#### RT-RTE-dynamic-tools
Label: Dynamic capability admission and execution

Endpoints/progression: SDK in-process registration or externally scoped MCP management → schema checks → SQLite/Map replacement → later new MCP server registration → script/shell callback. Owner: proposing agent or external client supplies code/path; registry software admits syntactically valid definitions; OS subprocess executes. Code and schema have symbolic force, while description text informs model selection. [SRC-1: `src/agent/in-process-tools.ts`, `src/mcp/tools-dynamic.ts`, `src/mcp/dynamic-tools.ts`, `src/mcp/dynamic-handlers.ts`, `src/mcp/server.ts`, `src/mcp/auth.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registered definition metadata; eventual tool execution returns stdout or error content.
- Later read-back: database reload on registry construction and definition enumeration on new external MCP server construction; actual script contents read at execution can have changed independently.
- Delegated visibility: handler receives JSON TOOL_INPUT and a reduced environment; script additionally receives stdin. It runs as an OS child, not a separate model context.
- Selection predicate: valid name/schema/type and required handler code/path; later tool-name dispatch. External registration requires admin scope; unknown dynamic invocation names fall back to read scope.
- Invalidation or expiry: unregister deletes definition and Map entry; no automatic expiry or versioned rollback. Existing server registrations may retain already-created definitions; immediate revocation across existing transports was not established.
- Activation or effect: persisted executable capabilities and subprocess invocation are wired; no observed invocation, quality gain or safe isolation result.
- Evidence limits: sanitized environment limits direct inherited variables, not filesystem/network access or encoded commands. In-process server exposes management tools, not an automatic mirror of every dynamic executable tool in that same query.

Trigger/change: a caller requests registration or replacement. Rejection is schema/required-field based, plus HTTP scope for external management; no per-content human review or semantic safety evaluator appears in registry admission. Guidance comes from registration descriptions and the main environment prompt. Persistence is executable handler definition/path plus description. Recovery is unregister/re-register, not transactional rollback of handler effects. Operating mode is open capability creation; no fixed answer oracle. [SRC-1: `src/agent/prompt-assembler.ts`, `src/agent/in-process-tools.ts`, `src/mcp/dynamic-tools.ts`]

> const proc = Bun.spawn(["bash", "-c", command], {
> stdout: "pipe",
> stderr: "pipe",
> env: buildSafeEnv(input),
> });
> --- `src/mcp/dynamic-handlers.ts`

> return TOOL_SCOPES[toolName] ?? "read";
> --- `src/mcp/auth.ts`

> // Defense-in-depth command blocker. This is NOT a security boundary.
> --- `src/agent/hooks.ts`

#### RT-RTE-reflection-admission
Label: Queued reflection admission

Endpoints/progression: channel/feedback session summary → gate judge → persistent queue/cadence → reflection subprocess → direct file edits → sentinel and applicable invariant check → version/log write → status-dependent live-config callback. Owner: gate model selects traces; reflection model selects content and escalation; engine/software can veto structural violations on covered admission paths. Human messages/corrections supply evidence; no per-edit human approval is wired. [SRC-1: `src/index.ts`, `src/evolution/gate.ts`, `src/evolution/engine.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/invariant-check.ts`, `src/evolution/versioning.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: drain result with status, version, changes, invariant findings and cost; subprocess free text/sentinel does not become a foreground response.
- Later read-back: changed ok results, including admitted compaction, explicitly refresh the runtime snapshot. The loader selects constitution.md, persona.md, user-profile.md, domain-knowledge.md and only strategies/task-patterns.md, tool-preferences.md and error-recovery.md. Corrections/principles and arbitrary new strategy files are reflection context, not automatic foreground evolved sections; their content must first be promoted into a selected file. The formatter also requires more than one nonblank, nonheading content line for each nonconstitution section. Acceptance alone does not establish foreground delivery.
- Delegated visibility: separate reflection context gets teaching prompt, batch identity/file sizes, staged JSONL and permitted Read/Write/Edit/Glob/Grep tools; no Bash/Task/WebFetch, no inherited project/user settings. Returns sentinel/results rather than its full reasoning context.
- Selection predicate: gate evolve boolean or error failsafe; cadence drains eligible queue content; reflection enabled mode and credentials/provider affect spawning; reflection model can skip or escalate tiers.
- Invalidation or expiry: crash/timeout/escalation attempts snapshot restoration; invariant failure restores and flags retry; successful admission versions/logs changes; skip sentinel bypasses post-state checks/restoration. Snapshot excludes meta and staging except explicit version restoration.
- Activation or effect: direct file edits and a changed-ok refresh are wired, including for compaction change actions. Foreground evolved-section delivery is limited to the loader-selected files and formatter conditions above; other admitted content can shape later reflection or reach foreground sections through subsequent promotion. Runtime behavior depending on changed text remains unobserved.
- Evidence limits: No supplied reflection run. Snapshot comparison is not a semantic quality/safety proof or global filesystem boundary; restoration can fail and ignores some deletions. Skip and excluded-directory coverage prevent a universal no-unchecked-writes claim.

Trigger/change/guidance: accumulated user/assistant traces motivate long-lived file changes under the reflection teaching prompt. That prompt requests specific durable facts/preferences, suppression of routine/public facts, compaction, cross-file promotion, credential exclusion and constitution consistency. The model proposes and physically performs edits before admission; software snapshots/checks filesystem state rather than approving every proposed sentence. The sentinel can request skip/escalation; malformed sentinel falls back to ok with checks. Answer oracle: none for whether a retained lesson is true or helpful; byte comparisons and bounds are reference checks for structural constraints, not expected task answers. Operating mode: recurrent open trace batches, not an experimental curriculum. [SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/invariant-check.ts`]

> You are not a critic, a tester, or a
> judge. You are a memory manager.
> --- `src/evolution/subprocess-prompt.ts`

> if (effectiveSentinel.status === "skip") {
> stats.status_skip = (stats.status_skip ?? 0) + 1;
> cleanupStaging(batchPath);
> --- `src/evolution/reflection-subprocess.ts`

> if (!invariant.passed) {
> restoreSnapshot(input.config, snapshot);
> --- `src/evolution/reflection-subprocess.ts`

> if (result.status === "ok" && result.changes.length > 0) {
> updateAfterEvolution(this.config);
> this.notifyConfigApplied();
> }
> --- `src/evolution/engine.ts:188-191`

> const SNAPSHOT_EXCLUDED_DIRS = new Set(["meta", ".staging"]);
> --- `src/evolution/versioning.ts`

The parser, rather than the runner's “ok / compact” comment, defines emitted status branches. Compaction is recorded as a per-file change type. [SRC-1: `src/evolution/reflection-subprocess.ts`, `src/evolution/versioning.ts`]

> if (status !== "ok" && status !== "skip" && status !== "escalate") return false;
> --- `src/evolution/reflection-subprocess.ts`

> } else if (annotation?.action === "compact") {
> type = "compact";
> --- `src/evolution/versioning.ts`

Automatic foreground consumption and reflection-context consumption differ. These fixed loader and formatter rules bound the callback's downstream delivery, independently of admission scope. [SRC-1: `src/evolution/engine.ts`, `src/agent/prompt-blocks/evolved.ts`, `src/evolution/subprocess-prompt.ts`]

> taskPatterns: readConfigFile(join(dir, "strategies/task-patterns.md")),
> toolPreferences: readConfigFile(join(dir, "strategies/tool-preferences.md")),
> errorRecovery: readConfigFile(join(dir, "strategies/error-recovery.md")),
> --- `src/evolution/engine.ts`

> if (evolved.persona.trim() && countContentLines(evolved.persona) > 1) {
> parts.push(`# Communication Style\n\n${evolved.persona.trim()}`);
> --- `src/agent/prompt-blocks/evolved.ts`

> - memory/corrections.md: explicit operator corrections. Append carefully.
> - memory/principles.md: distilled strategic principles from repeated observations.
> --- `src/evolution/subprocess-prompt.ts`

Theory account, bounded to this admission machinery: the teaching prompt supplies explicit memory-management rules, including scope conditions for durable lessons and correction of obsolete entries. It is static guidance here; the model is asked to revise retained content under it, not to revise the teaching method. The whole teaching text is inspectable, but actual generated theories/criticisms are not supplied. What persists can include natural-language strategies, preferences and corrections, plus version/input/outcome metadata; this does not establish that every file is a formulated theory.

- theory-builder conditions 1–4: condition 1 conclusion status: afforded — explicit rules and whole-file replacement permit localized language content; actual retained theory candidates were not observed. Condition 2 conclusion status: claimed — prompt instructions ask models to decide using file contents; a content-sensitive decision trace is not supplied. Condition 3 conclusion status: uninspected — guidance mentions errors/contradictions but no supplied criticism identifies challenged claim, result, blame and resulting revision. Condition 4 conclusion status: wired — recurrent queue/file/read-back machinery can carry revisions forward; iteration of content-directed criticism remains unestablished independently.
- Addressability: files and named sections/bullets are individually inspectable/editable; no claim of finer theory-part structure in an unobserved output.
- Persistence: file changes can survive sessions through mounted storage. Selected files reach later config loading; corrections/principles and nonselected strategies instead remain reflection context unless promoted into selected files. Actual survival across deployment failures is unobserved.
- learning: future behavior-shaping capacity is afforded through retained instructions, but improved future-action capacity and attribution to a particular update are unestablished without output/behavior evidence.
- Reflection: session summaries represent selected prior agent work and are wired to a process capable of changing later prompts; exact fidelity and exercised two-way effect remain unobserved.
- Reflective theory builder: uninspected — no supplied criticism/revision of the method text against its own operation.
- Autonomous theory builder: uninspected — proposal and software admission need no per-edit human decision, but that does not establish all four theory-building operations computationally occurred.
- Self-improvement attribution: only a dispositional improvement-directed self-change path is supported, bounded to long-lived agent instructions across sessions. Independent objective: better retention/use of durable operator preferences and task strategies, as stated by the teaching prompt. Trace evidence can shape edits (link 1), edits can change persistent instruction files (link 2), and loader-selected evolved sections meeting formatter conditions can reach later model prompts (link 3). Corrections/principles and nonselected strategies require subsequent promotion to enter that foreground path; acceptance alone does not close link 3 for their text. Link 4, later operation causally depending on the particular change, is unestablished; successful improvement additionally lacks outcome/comparison evidence. No exercised or beneficial self-improvement is inferred.

[SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/engine.ts`, `src/index.ts`, `src/agent/prompt-assembler.ts`, `docker-compose.yaml`]

#### RT-RTE-operator-config
Label: Operator configuration and extension edits

Endpoints/progression: authenticated dashboard API → validate/persist skill/subagent Markdown, hook/plugin settings or runtime YAML → later SDK settings or startup consumer. Owner: authenticated caller chooses content; software performs shape/catalog/path checks and I/O. Cookie authentication does not independently establish a human rather than an automated caller for every request. [SRC-1: `src/ui/serve.ts`, `src/ui/api/skills.ts`, `src/ui/api/subagents.ts`, `src/ui/api/hooks.ts`, `src/ui/api/plugins.ts`, `src/ui/api/phantom-config.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved object/status and audit metadata or validation/I/O error; not a measured capability improvement.
- Later read-back: user/project settings requested by foreground SDK calls can expose skills/subagents/plugins/hooks; YAML is loaded by startup. Dashboard save does not itself establish immediate live-runtime configuration replacement.
- Delegated visibility: skill/subagent bodies are natural-language instruction content, frontmatter controls are symbolic; plugin/hook settings are symbolic selectors and executable callback configuration interpreted by the SDK. Exact dependency loading/activation remains uninspected.
- Selection predicate: cookie-authenticated API, valid name/frontmatter/body size and requested CRUD operation; plugin install additionally requires marketplace entry; HTTP-hook URL rules check the settings allowlist.
- Invalidation or expiry: delete/disable/rewrite APIs; files use temporary-write/rename patterns and last-write-wins. Each YAML write is individually atomic, not an all-files transaction. No semantic rollback or automatic expiry established.
- Activation or effect: edits persist; only requested dependency settings consumption/startup loading is established, not successful plugin installation/execution or immediate permissions activation.
- Evidence limits: Lint output, audit actor labels and path-check comments are not proof of semantic safety, human approval, symlink confinement or live activation. External marketplace/SDK internals are not frozen.

Trigger/proposed changes: caller explicitly creates/edits/deletes capability instructions and hooks or updates configuration. Admission/veto: schema/path/size checks, catalog lookup and HTTP-hook allowlist, not an independent model-quality evaluator. Skills/subagents expose lint feedback; those warnings do not themselves establish a rejection gate. Recovery: rewrite/delete/disable and per-file atomic replacement; no full prior-state restore is shown. Guidance is authored by caller or agent; dashboard schema shapes what can persist but supplies no task correctness oracle. Operating mode: open operator edits. No fixed answer oracle and no compulsory second human reviewer. [SRC-1: `src/skills/storage.ts`, `src/subagents/storage.ts`, `src/hooks/storage.ts`, `src/ui/api/plugins.ts`, `src/ui/api/phantom-config.ts`]

> // Each write is individually atomic; if the second one fails we STOP so
> // the DB audit row count matches what actually made it to disk.
> --- `src/ui/api/phantom-config.ts`

> // No file locking: last-write-wins per the Cardinal Rule. tmp+rename still
> // protects against torn files on a mid-write crash.
> --- `src/subagents/storage.ts`

> settingSources: ["project", "user"],
> --- `src/agent/chat-query.ts`

### Claims

#### RT-CLM-autonomous-worker
Label: Persistent autonomous co-worker claim

Claimed operation: the main identity prompt presents a persistent autonomous worker with workstation access and accumulating knowledge/capabilities. This is doctrine/design injected into the model, not evidence of actual comprehensive access or improvement. The implemented tool/runtime paths support capacity for consequential action; deployment grants and successful improvement remain separate questions. [SRC-1: `src/agent/prompt-assembler.ts`, `docs/architecture.md`]

> You run on your own machine with full access: filesystem, Docker, shell, network, scheduler, and a persistent memory that grows with every conversation. You are not ephemeral. Your workspace, your knowledge, and your capabilities persist and compound over time.
> --- `src/agent/prompt-assembler.ts`

### Evidenced absences

#### RT-ABS-task-executor
Label: MCP task-table executor not established in shipped source

- implementation conclusion status: absent

Bounded absence: at revision f8c7ab42d885936ee54abc785528000260f4acc5, searching non-test `src/` for `FROM tasks`, `UPDATE tasks` and `INSERT INTO tasks` found MCP task insertion, count/status queries and resource reads, but no task-state advancement/executor. The inspected task-create handler ends by returning queued status and queue position. This supports distinguishing queue-row creation from an established executable work loop; it is not a claim about arbitrary external clients or future upstream code. [SRC-1: `src/mcp/tools-universal.ts`, `src/mcp/resources.ts`]

> `INSERT INTO tasks (id, title, description, urgency, source_channel, status)
> VALUES (?, ?, ?, ?, 'mcp', 'queued')`,
> --- `src/mcp/tools-universal.ts`

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: Assembled instruction authority

Consumer: main SDK/model. Channel: appended system prompt, plus the dedicated Murph user-context transform. Force: natural-language behavioral guidance, not a code-enforced safety boundary. Horizon: current query and later queries that rebuild/reload retained configuration or context. Static role/security guidance, evolved text, working memory and retrieved content have different provenance and are not automatically equal authority merely because assembled together. [SRC-1: `src/agent/prompt-assembler.ts`, `src/agent/runtime.ts`, `src/agent/chat-query.ts`, `src/agent/murph-context.ts`]

> sections.push(buildAgentMemoryInstructions());
> --- `src/agent/prompt-assembler.ts`

#### RT-BAP-handler-execution
Label: Registered handler authority

Consumer: MCP server callback and OS subprocess. Channel: persisted symbolic handler definition and later tool dispatch. Force: executable authority under the Phantom process's rights; the reduced environment is a variable-supply restriction, not proven isolation. Horizon: across registry reloads/new MCP server creation until deletion/replacement, with separate script-file mutability. It does not inherit the direct SDK Bash matcher merely because the child is Bash. [SRC-1: `src/mcp/dynamic-tools.ts`, `src/mcp/dynamic-handlers.ts`, `src/agent/hooks.ts`]

> async (input): Promise<CallToolResult> => executeDynamicHandler(tool, input),
> --- `src/mcp/dynamic-tools.ts`

## Annotations

none
