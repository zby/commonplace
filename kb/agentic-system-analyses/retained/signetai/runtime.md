---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Signet runtime baseline: Pi context delivery and capture, bounded Dreaming maintenance, and alternate admission and executor paths."
run-id: AAS-2026-10-14-signetai-64f703d83203-01
reviewed-boundary: "12dba1ce753babda735f2ba7b6f150c6c0b7f95e"
---

# Signet runtime report

## Runtime account

### Evidence and claimed work

Signet is a memory service with shipped host adapters and an internal model-driven maintenance loop, not the enclosing foreground agent. The frozen scope and source identity are in [boundary](boundary.md). All evidence below is SRC-1 at that revision: implementation unless explicitly labelled doctrine. No target execution, model call, test run, deployment inspection or experimental comparison was supplied or performed. Wired delivery is not observed model use, and a successful write is not demonstrated improvement.

The consequential work is to capture session evidence, maintain durable semantic state, and supply selected identity and memory context to later agent invocations. The runtime has two next-step owners: host callbacks and daemon rules handle capture/delivery; a routed model chooses maintenance tools and proposed changes. Their effects meet at the daemon and database, not at a shared agent conversation. See [RT-RTE-pi-lifecycle](#rt-rte-pi-lifecycle), [RT-RTE-dreaming-pass](#rt-rte-dreaming-pass), and [RT-CMP-inference-router](#rt-cmp-inference-router).

Added inspection beyond the boundary's initial mapping covered the Pi shared lifecycle, hook handlers, auth/global middleware, Dreaming tool wrapper/capabilities/operation validation, inference routing, Pi worker resource loading and ACPX MCP binding. Material anchors are retained below. This is a selected runtime trace, not exhaustive adapter equivalence or an audit of every repository path. Detailed transcript worker completion, import/source-provider transformations, every recall ranking branch, ontology recovery, generated identity files, plugin loading, deployment bind addresses, packaging and benchmark execution remain uninspected here. They remain included responsibilities for specialist coverage; none is declared absent.

### Ordinary invocation: Pi session to retained evidence to later context

The concrete shipped entry is Pi's `session_start` callback. It checks daemon health and calls shared lifecycle code; session switches/forks flush ends and refresh startup context, while shutdown submits an end. Principal identifiers include configured agent ID, host session ID/file, project, harness and runtime path. The client POSTs `/api/hooks/session-start`; daemon code resolves agent scope, claims the session/runtime combination (409 on conflicting claim), records presence and handles bypass/claim-only modes. The callback, not the model, owns this progression (SRC-1, `integrations/pi/extension/src/index.ts`, `integrations/pi/extension-base/src/lifecycle.ts`, `platform/daemon/src/routes/hooks-routes.ts`).

`handleSessionStart` constructs a stable Signet prompt and bounded dynamic context. Its inspected assembly reserves room for continuity, constraints, inherited material and recovery; trims the main dynamic body; applies an aggregate budget; and can remove continuity after budget checking or recall-claim suppression. Thus candidate retrieval alone does not establish delivery. The shared lifecycle selects `dynamicContext`, then legacy `inject`/`recentContext` fallbacks, combines it with the stable prompt for the first turn, and queues it. On timeout/offline it uses a configured static fallback instead. The extension's `context` callback appends consumed hidden messages to the host's messages. This establishes a model-input channel, not authority over host actions (SRC-1, `platform/daemon/src/hooks.ts`, `integrations/pi/extension-base/src/lifecycle.ts`, `integrations/pi/extension/src/index.ts`; [RT-BAP-host-context](#rt-bap-host-context)).

Input and `before_agent_start` callbacks settle prompt submissions before context delivery. On session end the shared lifecycle can supply a session-file snapshot or constructed transcript. The daemon's end handler distinguishes a clear boundary, an ordinary turn with no boundary reason, and a terminal boundary. A clear resets continuity/dedupe/recall epoch and returns zero memories; a non-boundary turn schedules deferred work without terminal capture. A terminal boundary normalizes the transcript and queues a durable transcript-capture job, returning `memoriesSaved: 0` and a queue flag/job ID. Therefore endpoint success is not synchronous semantic ingestion. Enqueue failures are logged; the return may say not queued. Checkpoint flush/write failures are nonfatal. Runtime claims and duplicate guards reduce competing capture, and the route releases a claimed session when end processing throws (SRC-1, `platform/daemon/src/hooks.ts`, `platform/daemon/src/routes/hooks-routes.ts`).

Subsequent Dreaming work can consume retained evidence and publish semantic state; a later startup or explicit recall can supply retained context. Precise memory lineage, all read selectors and revision semantics belong to the memory report. This trace does not treat an enqueue acknowledgment as proof of worker completion or claim that every adapter supplies the same transcript.

### Maintenance invocation and effect boundary

A daemon timer checks enablement, available capacity, inference availability, system/queue pressure and leased scopes. It probes backlog and attention, evaluates a trigger, selects a pass mode and admits work. These are symbolic code decisions. The worker limits concurrent passes against configured and LLM capacity, leases scopes and distinguishes exclusive passes. A user-request pass has a different scope grant: only the requested agent, rather than the install scopes supplied to scheduled maintenance (SRC-1, `platform/daemon/src/pipeline/dreaming-worker.ts`, `platform/daemon/src/pipeline/dreaming.ts`).

The pass builds natural-language maintenance guidance plus scoped history, pending attention and a clock. The routed model owns tool selection. Tools expose bounded evidence reads, graph lookups, proposal validation, runbook writes and audited mutations. The handler records tool inputs, outputs, success and latency; live events and provider attribution are separate from durable pass accounting. Semantic operations and head publication have different commit boundaries: ontology operations may commit in earlier batches, while a content pass stages a memory head for finalization. A content pass cannot finalize successfully without an accepted head commit. A failed pass is consequently not evidence that all earlier operation effects were rolled back (SRC-1, `platform/daemon/src/pipeline/dreaming.ts`, `platform/daemon/src/pipeline/dreaming-operations.ts`; [RT-RTE-dreaming-pass](#rt-rte-dreaming-pass)).

This is an open evidence-maintenance mode, not a curriculum with expected answers. The model proposes and selects content; schema, scope, provenance, write caps and commit rules can reject it. Starting scheduled work is not human approval of each change. Exact-quote checks validate a relation to a canonical source, not the truth of the resulting interpretation. The inspected route contains no independent expected-answer oracle. This conclusion is confined to these maintenance handlers, not the repository's separate evaluation machinery.

### Three forcing cases and guarantee coverage

**1. Off-scope tool input and extension exposure.** In the Pi executor, the worker disables discovery of external extensions, skills, templates, themes and context files, and explicitly lists the supplied tools plus optional codemode. Calls are forwarded to parent-side handlers. The wrapper recursively rejects an `agentId` outside the pass's allowed set; schemas alone are not the enforcement. Codemode exposes a selected lookup set while direct writes remain model-only. This is a source-configured capability boundary, not proof of OS sandboxing or dependency-internal isolation. Scheduled grants can intentionally cover several agents, whereas an explicit user task narrows them. See [RT-CLM-tool-boundary](#rt-clm-tool-boundary).

**2. Invalid provenance and partial completion.** Operation validation occurs before flag minting and write batches; evidence failures reject proposals, but structural operations have their own permitted no-citation branch and hygiene operations use attention provenance. It would be false to say that every write requires an episodic quote or that one failed operation undoes the whole pass. Batches return processed items and an uncommitted suffix retry marker. The selected enforcement is daemon-side, not merely prompt instruction (SRC-1, `platform/daemon/src/pipeline/dreaming-operations.ts`).

**3. Alternate executor and direct admission.** `runAgent` can use a non-Pi provider path and ACPX executor. ACPX requires a scoped Signet MCP binding; its temporary configuration carries agent/pass IDs, daemon URL and optionally a token. The router sends a prompt through `provider.generate` on the non-Pi branch instead of creating the inspected tool-only Pi session. The external agent's native tools, shell, extension environment and actual isolation are not established by this binding. Separately, direct `/api/memory/remember` and mutation routes admit caller content without running the Dreaming agent. Therefore “all writes use Dreaming's tools” is not a whole-system invariant. The same reasoning prevents extending Pi resource-loader controls to foreground hosts, ACPX or arbitrary SDK callers. See [RT-RTE-alternate-executor](#rt-rte-alternate-executor) and [RT-RTE-direct-remember](#rt-rte-direct-remember).

Authentication is mode-dependent. Global middleware installs authentication and request logging, but local mode explicitly passes through without claims and hybrid localhost has a permission bypass. Token scopes matter on credentialled paths. Actual grants, bind address, deployment exposure and host filesystem permissions are unobserved; source affordances do not establish a deployed isolation envelope (SRC-1, `platform/daemon/src/middleware.ts`, `platform/daemon/src/auth/middleware.ts`, `platform/daemon/src/routes/memory-routes.ts`).

### Working context and change admission

There are two distinct context controls. Foreground Pi appends selected hidden context; its compaction callbacks notify Signet before compaction and send a host-produced summary afterward. Signet does not choose the host's compaction policy in these callbacks. What verbatim tail survives is an external-host fact. Retained summary ingestion and context-epoch handling are separate daemon paths, not proof that the extension removed any turns. Internally, Dreaming starts an in-memory worker session with only supplied resources; history/attention are rendered into the prompt and a post-pass completer can compact maintenance history. That keeps prior full work out of a fresh model window while retaining selected history for later passes. This resembles a separate frame for one maintenance task, but durable database writes escape continuously, not only as one final return value (SRC-1, `integrations/pi/extension/src/index.ts`, `platform/daemon/src/pipeline/pi-agent-worker.ts`, `platform/daemon/src/pipeline/dreaming-worker.ts`). Detailed history summarizer selection and retained summary lineage were not inspected here.

Knowledge admission occurs through model/tool maintenance and direct API requests; their distinct veto and recovery points are recorded below. Configured targets and fallback references can change which model executes a later call. Pi workers also expose idle-session model reconfiguration, but do not train weights. Source does not establish immutable deployed model weights or stable remote alias resolution ([RT-CMP-inference-router](#rt-cmp-inference-router)). Product releases, dependency changes, skill installation, dynamic plugins and production-machinery update gates are not traced deeply enough here to attribute an autonomous improvement loop. No claim of learning, theory building or exercised self-improvement follows from this runtime account.

## Shared records

### Components

#### RT-CMP-inference-router
Label: Routed inference models

The source-native inference router resolves target/model references, credentials and fallback order. The model's operative form is distributed-parametric; configuration/selection is symbolic. Weights are stored by provider/native services outside the inspected repository, while target configuration and instantiated provider caches belong to Signet. Parameters changing during operation: uninspected provider internals; no weight-update mechanism is established by the inspected call/session code. Exact version pinned: not established by configured model names. Mutable endpoint resolving to another model: possible for remote endpoints/aliases; actual provider behavior uninspected. A later configuration selection can also choose a different target. SRC-1, `platform/daemon/src/inference-router.ts`, `platform/daemon/src/pipeline/pi-provider.ts`, `platform/daemon/src/pipeline/pi-agent-worker.ts`.

> for (const targetRef of [decision.value.targetRef, ...decision.value.fallbackTargetRefs]) {
> --- `platform/daemon/src/inference-router.ts:1175-1175`

> if (running) throw new Error("Cannot switch models during an active turn");
> --- `platform/daemon/src/pipeline/pi-agent-worker.ts`

The pass model proposes actions; the history completer is a separate routed call sharing this selection machinery, not necessarily the same realized provider. Provider reasoning and reliability remain opaque.

### Operative objects

#### RT-OBJ-pass-prompt
Label: Dreaming pass prompt

Source-native `passPrompt` is natural-language guidance rendered from the selected maintenance prompt, scoped history, pending attention and clock. Its substrate is an in-memory string passed into the routed executor; history and attention have database-backed inputs. This object is current invocation context, not itself evidence of durable memory or an updated theory. SRC-1, `platform/daemon/src/pipeline/dreaming.ts`.

> await renderDreamingHistoryForPass(accessor, agentId, historyScopes),
> await renderPendingDreamingAttention(accessor, historyScopes, mode),
> --- `platform/daemon/src/pipeline/dreaming.ts`

### Routes

#### RT-RTE-pi-lifecycle
Label: Pi capture and context delivery

Endpoints and progression: host lifecycle callbacks → shared client → daemon session-start/session-end hooks → queued hidden context or transcript capture → later host callbacks. Principal/identity: configured agent, session ID/file, project, harness and runtime path. Host events and daemon code decide progression; the foreground model does not authorize these callbacks. Context is natural-language text with symbolic lifecycle metadata. Capture acknowledgment returns to the host; subsequent worker processing is asynchronous. SRC-1, `integrations/pi/extension-base/src/lifecycle.ts`, `integrations/pi/extension/src/index.ts`, `platform/daemon/src/routes/hooks-routes.ts`, `platform/daemon/src/hooks.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: startup payload/hidden messages; terminal end returns zero saved memories plus queued flag and optional capture job ID.
- Later read-back: startup can supply retained continuity and recovery to a later session; queued capture enables later maintenance, but completion is not established by the end response.
- Delegated visibility: daemon sees submitted session data; Pi receives selected context, not all retained state. External host behavior after receipt is uninspected.
- Selection predicate: agent/session/runtime scope, lifecycle event, bypass/claim guards and startup budgets; dynamic context can be trimmed or claim-suppressed.
- Invalidation or expiry: clear resets continuity/dedupe and advances recall epoch; session switches refresh context; static fallback applies on unavailable startup response.
- Activation or effect: code appends hidden messages to host input and enqueues capture; model compliance or changed answers are unobserved.
- Evidence limits: inspected Pi path only; not proof of equivalent behavior in other shipped adapters or durable capture completion.

Admission: host callbacks automatically supply transcript material; identity does not establish human content approval. Daemon validation/session claims can reject or skip conflicting work. On errors the route releases its claim; it does not guarantee recovery of every lost transcript. Compaction is decided by the external host; Signet's adapter posts before/after notifications and the summary, not a compaction decision. No expected-answer oracle applies to lifecycle capture.

> messages: [...event.messages, ...hiddenMessages],
> --- `integrations/pi/extension/src/index.ts`

> memoriesSaved: 0,
> queued: Boolean(transcriptCaptureJobId),
> --- `platform/daemon/src/hooks.ts`

#### RT-RTE-dreaming-pass
Label: Dreaming maintenance pass

Endpoints: scheduler or scoped user request → pass builder → routed executor → capability handlers → daemon operations/head finalization. Worker rules admit passes and assign scopes; model decisions choose evidence reads, candidate operations and tool order. Symbolic schemas and database state constrain effects; natural-language instructions/history guide proposals. A pass is coordinated by scope leases, capacity checks and pass IDs. Source: SRC-1, `platform/daemon/src/pipeline/dreaming-worker.ts`, `platform/daemon/src/pipeline/dreaming.ts`, `platform/daemon/src/pipeline/dreaming-agent-tools.ts`, `platform/daemon/src/pipeline/dreaming-capabilities.ts`, `platform/daemon/src/pipeline/dreaming-operations.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tool results contain status/items/rejections; executor returns attribution/usage and a completion summary; pass records account for effects.
- Later read-back: semantic writes, attention/runbook state and rendered maintenance history can reach subsequent passes or context consumers; specialist analysis must establish each retained part's downstream selectors.
- Delegated visibility: executor receives selected prompt and available tool schemas; tool results expose bounded evidence. Scheduled passes can receive multiple agent scopes; explicit user requests narrow to one.
- Selection predicate: enablement, capacity, inference availability, pressure, halt state, backlog/attention trigger and selected mode; per-tool scopes and capabilities further constrain actions.
- Invalidation or expiry: evidence delivery has a half-timeout deadline; pass timeout/cancellation bounds work; unsuccessful content finalization does not publish its staged head. Earlier committed operation batches are not necessarily undone.
- Activation or effect: capability handlers can change retained semantic state; successful content head publication requires finalization. Subsequent behavioral use remains unobserved.
- Evidence limits: implementation establishes proposal and rejection machinery, not interpretation correctness, actual provider completion, improvement or all memory revision semantics.

Operating mode: open evidence maintenance, scheduled or user-requested. Trigger/proposed change: backlog, attention or explicit request prompts model-proposed graph/head/runbook changes. Proposer and computational decision maker: model; veto: scope/schema/provenance checks, configured caps, timeouts and finalization preconditions. Human contribution: can request/configure work, but the inspected loop does not wait for human approval of every proposal. No independent expected-answer oracle in the inspected maintenance seam; canonical source matching is a provenance check. Recovery: error accounting, later scheduler checks, evidence retry policy and returned uncommitted suffix; pass-wide atomic rollback is not established. Guidance persists as shipped prompts and maintained history/runbook, but this route does not establish formulated content-directed criticism of its own method.

> allowedAgentIds: liveOptions?.userRequest !== undefined ? [agentId] : scopes,
> --- `platform/daemon/src/pipeline/dreaming.ts`

> const validationError = validateRequestBeforeWrites(params);
> if (validationError !== null) return { ok: false, items: [], error: validationError };
> --- `platform/daemon/src/pipeline/dreaming-operations.ts`

> retryFrom: result.processed,
> retryable: true,
> --- `platform/daemon/src/pipeline/dreaming-operations.ts`

> "Content pass finalization requires a successful memory-head commit: the agent ended without calling memory_head_commit"
> --- `platform/daemon/src/pipeline/dreaming.ts:1984-1984`

#### RT-RTE-alternate-executor
Label: ACPX routed execution

Endpoints: inference router target selection → ACPX/non-Pi provider → scoped Signet MCP process → daemon. Provider/external agent owns internal next steps, unlike the inspected Pi worker. Prompt and MCP config are respectively natural-language and symbolic; the config is a temporary file with scoped environment and optional credential. SRC-1, `platform/daemon/src/inference-router.ts`, `platform/daemon/src/pipeline/acpx-dreaming-mcp.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: nonempty generated completion yields routed success/attribution; empty completion or provider failure rejects the attempt.
- Later read-back: uninspected — external agent persistence is not shown by the binding; daemon tool writes can share the retained maintenance effects described in the maintenance route.
- Delegated visibility: external executor receives the prompt and scoped MCP connection; its other tools/resources are uninspected.
- Selection predicate: selected/fallback target with ACPX executor requires supplied agent/pass/daemon binding; non-Pi providers take the generate branch.
- Invalidation or expiry: generated config has a disposal function deleting its temporary directory; timeout options are forwarded. Actual external termination/isolation is unobserved.
- Activation or effect: enables remote/subprocess tool access to daemon capabilities; not proof that the provider used them or lacks other effect channels.
- Evidence limits: scoped MCP binding does not establish OS sandboxing, tool exclusivity, external model context or host approval policy.

Admission: this is an executor selection within maintenance, not an additional human per-write gate. Model proposals using daemon tools remain subject to those handlers; any native external tool effects have uninspected admission/recovery. No expected-answer oracle established. Changes in target configuration/fallback can substitute execution machinery; model efficacy and exact resolved weights are not verified.

> throw new Error("ACPX agent target requires the scoped Signet MCP binding");
> --- `platform/daemon/src/inference-router.ts`

> const generated = await provider.generate(prompt, {
> timeoutMs: opts?.timeoutMs,
> maxTokens: opts?.maxTokens,
> });
> --- `platform/daemon/src/inference-router.ts`

#### RT-RTE-direct-remember
Label: Direct memory admission

Endpoints: CLI/SDK/adapter or other HTTP caller → `/api/memory/remember` → scoped memory admission. This route is distinct from the Dreaming pass: caller-supplied text, optional structured entities/aspects and metadata are not a maintenance model proposal. Owner: caller proposes; daemon rules accept/reject. Human identity/content review cannot be inferred from arbitrary HTTP origin. SRC-1, `platform/daemon/src/routes/memory-routes.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: malformed JSON, missing content, invalid temporal fields, scoped-token violations or frozen mutations yield errors; valid work continues into ingestion.
- Later read-back: admitted memory is intended for recall/maintenance; exact indexing, dedupe, storage and read visibility remain for the memory analyst rather than inferred from API success.
- Delegated visibility: caller controls supplied content/metadata; daemon resolves agent and visibility/project/scope. Token project/agent checks apply when claims exist.
- Selection predicate: nonempty content, valid fields, scoped credentials when present, dedupe scope and mutation configuration.
- Invalidation or expiry: mutations can be frozen; separate modify/forget/recover endpoints are registered. Their rollback semantics are uninspected here.
- Activation or effect: admits caller material without invoking Dreaming's model; downstream behavior remains unobserved.
- Evidence limits: partial handler trace establishes this alternate admission surface, not full storage/recovery semantics or a universal guarantee covering every import path.

Operating mode: open caller requests, no expected-answer oracle. Trigger/change: explicit request to retain content, not a benchmark intervention. Rejection: route validation and permission/config checks. Guidance: API fields and caller instructions, whose authorship is unresolved. Recovery is not an atomic undo guarantee in this trace. Other save/hook-remember and modify/forget routes demonstrate a wider material API surface; their equivalence must not be assumed.

> if (!raw) return c.json({ error: "content is required" }, 400);
> --- `platform/daemon/src/routes/memory-routes.ts`

> if (pipelineCfg.mutationsFrozen) {
> return c.json({ error: "Mutations are frozen (kill switch active)" }, 503);
> }
> --- `platform/daemon/src/routes/memory-routes.ts:1387-1389`

### Claims

#### RT-CLM-tool-boundary
Label: Bounded Pi maintenance tools

Claimed operation: Pi maintenance sessions may use only supplied daemon tools. Owner: Signet's Pi worker/client and parent capability wrappers. Strength: invariant for the explicit source configuration and off-scope wrapper rejection, not a deployment guarantee about all possible executors. Enforcement: disabled resource discovery, explicit tool names, recursive scope checking before capability invocation. Covered path: inspected Pi worker sessions. Alternate paths: ACPX/provider generate, host callbacks, direct HTTP clients, plugins and filesystem/shell authority outside this worker configuration are not covered by this claim. External contract: Pi dependency must honor supplied resource/tool configuration; worker isolation and external provider internals are not independently verified. Current installed tools, allowed scopes and OS permissions are not observed. SRC-1, `platform/daemon/src/pipeline/pi-provider.ts`, `platform/daemon/src/pipeline/pi-agent-worker.ts`, `platform/daemon/src/pipeline/dreaming-agent-tools.ts`.

- guarantee strength: invariant
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "You are a bounded Signet maintenance agent. You may use only the supplied daemon tools.",
> --- `platform/daemon/src/pipeline/pi-provider.ts`

> noExtensions: true,
> noSkills: true,
> noPromptTemplates: true,
> noThemes: true,
> noContextFiles: true,
> --- `platform/daemon/src/pipeline/pi-agent-worker.ts`

> tools: [...customTools.map((tool) => tool.name), ...(codemode ? ["codemode"] : [])],
> --- `platform/daemon/src/pipeline/pi-agent-worker.ts`

> if ("agentId" in value && (typeof value.agentId !== "string" || !allowed.has(value.agentId)))
> throw new Error("Tool agent scope must be one of this pass's agents");
> --- `platform/daemon/src/pipeline/dreaming-agent-tools.ts`

The prompt alone is a policy; the listed code is the stronger local enforcement. Neither entails whole-system write exclusivity.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-context
Label: Retained context to host model

Consumer: the foreground Pi model through host context callbacks. Channel: queued hidden natural-language messages assembled from stable and selected dynamic context. Force: advisory model input, not an executable permission grant; Signet does not control the enclosing host's tool policy. Horizon: later turns/sessions can receive retained context, with current submission dedupe and host compaction boundaries. Source: SRC-1, `integrations/pi/extension-base/src/lifecycle.ts`, `integrations/pi/extension/src/index.ts`, `platform/daemon/src/hooks.ts`; route [RT-RTE-pi-lifecycle](#rt-rte-pi-lifecycle). Delivery wiring is established; model uptake and demonstrated benefit are unobserved.

> deps.state.setPendingSessionContext(session.sessionId, firstTurnContext);
> --- `integrations/pi/extension-base/src/lifecycle.ts`

#### RT-BAP-maintenance-tools
Label: Model proposals to daemon effects

Consumer: parent capability handlers and ontology operation applicators. Channel: structured tool calls interpreted by fixed daemon rules. Force: executable mutation requests with scope/schema/provenance checks and possible rejection, rather than prompt text directly editing the database. Horizon: current tool invocation can create durable effects for later passes or host delivery. Source: SRC-1, `platform/daemon/src/pipeline/dreaming-agent-tools.ts`, `platform/daemon/src/pipeline/dreaming-capabilities.ts`, `platform/daemon/src/pipeline/dreaming-operations.ts`; route [RT-RTE-dreaming-pass](#rt-rte-dreaming-pass). The proposal's natural-language content and the symbolic admission envelope have different consumers; admission does not verify the content's truth.

> scopedInput(rawParams, allowed);
> const result = await capability.invoke(rawParams);
> --- `platform/daemon/src/pipeline/dreaming-agent-tools.ts`

## Annotations

none
