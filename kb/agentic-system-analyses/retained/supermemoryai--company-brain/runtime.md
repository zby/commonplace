---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Company Brain's Slack turn loop, alternate execution paths, local controls and change admission at the frozen worker revision."
run-id: AAS-2026-10-14-company-brain-30a9e8cfaeca-01
reviewed-boundary: ef8a45ef3aed97b32599c7d8007edefab6d14e9a
---

# Company Brain runtime report

## Runtime account

Company Brain owns the application-level model/tool loop. Slack delivers events to the worker; the worker resolves a workspace and dispatches to its organization-named Durable Object. The agent assembles context and tools, runs a model, intercepts approvals, settles live updates, and returns a reply to the Slack caller. Memory and scheduled work are part of this application, not an excluded host. The frozen scope and external-service limits are in [boundary](boundary.md#boundary-and-evidence). All source findings below use SRC-1 at that boundary. Implementation wiring is inspected; no supplied execution trace establishes activation, successful delivery, reliability or benefit.

### Ordinary invocation

An explicit DM, mention, name wake or eligible thread message enters [RT-RTE-slack-turn](#rt-rte-slack-turn). The HTTP event path verifies Slack's signature, parses the envelope, resolves the workspace, checks event/turn keys and invokes the organization's agent through `waitUntil`. The HTTP acknowledgment is not the answer. Slack identity is resolved into an organization member; the ordinary actor uses that member's personal connections, and memory scope derives from the Slack surface. Thread coordination uses a thread key, turn ID and revision. The caller supplies thread conversation, attachments, directory, participants, bot identity and a deadline/abort signal (SRC-1, `src/routes/slack/index.ts`, `src/brain/slack/turn.ts`).

`computeTurn` creates turn state, optionally reloads a principal-scoped thread-investigation checkpoint, and assembles the current actor's tools. It loads company context, ambient memory and interaction style concurrently. Workspace instructions and a visible skill index enter runtime context; skill bodies are loaded on demand. System policy, runtime context, conversation, current request and structured turn state become model messages. The main model chooses the next tool or terminal proposal; host code determines availability, budget, suspension and finalization. The model is [RT-CMP-brain-main](#rt-cmp-brain-main), not a fixed weight artifact pinned by this analysis (SRC-1, `src/brain/turn/compute.ts`, `src/brain/turn/loop.ts`).

The model-visible tool set is smaller than the assembled capability surface. Sandbox and scheduler families require `enable_tool_family`; unlocking changes the next step's active tools, not credentials or operating-system permissions. Connected applications normally use discovery plus Code Mode, but setup failure or no ready Code Mode apps selects direct MCP. These are materially different control paths: [RT-RTE-app-code](#rt-rte-app-code) and [RT-RTE-direct-mcp](#rt-rte-direct-mcp). A tool result becomes model context; it is not an answer oracle. On normal completion, terminal selection and `settleTurn` reconcile pending updates before publication. The Slack caller fences delivery, falls back to posting when streaming did not deliver, writes eligible memory, completes the turn, and may arm delayed observation (SRC-1, `src/brain/turn/tools.ts`, `src/brain/turn/compute.ts`, `src/brain/slack/turn.ts`).

### Forcing routes and guarantee limits

Four forcing cases were inspected rather than treating the ordinary path as universal.

1. **Code Mode unavailable.** Direct MCP is a shipped fallback. Its classifier and approval predicate differ from Code Mode. In direct personal access, an unknown name is classified as a write for read-only filtering, yet `mcpToolNeedsApproval` only checks destructive annotations and listed write tokens. A name with neither token nor annotation can therefore reach personal `callTool` without this predicate requesting approval. Dangerous raw-query/code names also are not categorically approval-required by that predicate. This is a source-supported countercase to “every possible external write requires approval,” not evidence that any deployed server performed such a write (SRC-1, `src/brain/tools/mcp/runtime-tools.ts`, `src/brain/tools/mcp/tool-policy.ts`; [RT-CLM-write-approval](#rt-clm-write-approval)).
2. **Shell instead of connected-app method.** [RT-RTE-sandbox-work](#rt-rte-sandbox-work) executes commands through a separately configured sandbox client. Both local provider adapters apply command validation, but the validator uses regex denials rather than a complete effect allowlist. The shell path has no MCP approval classifier. An ordinary program that makes a network request is not excluded by the inspected deny patterns. This prevents extending MCP's approval or read-only policy to all shell effects; it does not establish a successful escape or deployed network access (SRC-1, `src/brain/tools/sandbox/guards.ts`, `src/brain/tools/sandbox/cloudflare-client.ts`, `src/brain/tools/sandbox/daytona-client.ts`).
3. **Passive and scheduled callers.** Passive investigation sets an actor read-only flag, suppresses approval requests and omits interactive write families; scheduled turns omit scheduling, leases and reachout. Yet `scheduledRun` is not itself a universal read-only grant: the scheduled caller forwards `payload.readOnly`. Sandbox tools remain assembled when configured, with Slack artifact upload disabled for scheduled/passive turns. Draft research explicitly sets `readOnly: true` and `ephemeral: true`. These are scoped modes, not a global “background work cannot change anything” invariant (SRC-1, `src/brain/turn/tools.ts`, `src/brain/tools/scheduling.ts`, `src/brain/auto-research/draft.ts`; [RT-RTE-scheduled-task](#rt-rte-scheduled-task), [RT-RTE-research-draft](#rt-rte-research-draft)).
4. **Suspension, newer input and later resume.** [RT-RTE-approval-resume](#rt-rte-approval-resume) persists a bounded conversation and assembly snapshot. Before resuming, Slack approval processing verifies team, requester, pending status, expiry, current turn, workspace binding and membership. This is not a permanent grant or replay of an unrestricted live context. Finalization claims wait for pending/classifying updates. The current-turn check treats an absent control snapshot as current, so callers without thread coordination do not inherit the Slack revision fence (SRC-1, `src/brain/slack/turn.ts`, `src/brain/slack/turn-control.ts`).

**Load-bearing controls.** The application owns signature admission at the Slack HTTP route (policy), actor/scope-dependent tool assembly (policy), Code Mode's classified native-call deny/pause rule (policy plus approval protocol), requester-bound approval consumption (protocol), and SQL turn/revision finalization (protocol). Implementation conclusion status: wired. Operation conclusion status: uninspected. These controls cover their named local paths, not arbitrary remote behavior. They require Slack identity/signature semantics, SDK approval/stop semantics, Durable Object SQL behavior, and remote tools honoring the meanings used in classification. Their exact guarantees are not physical containment or transactionality over external actions. Event KV get/put dedup is best effort, not an atomic exactly-once guarantee; errors are swallowed and the check/write are separate (SRC-1, `src/routes/slack/index.ts`).

Step stopping is host-configured: initial profile limit is 60, continuation 30 and live-update 12 unless overridden. Wrap-up removes regular tools while retaining protocol tools. `maxRetries: 3` is a model-call retry setting, not a global effect retry guarantee. Direct MCP requests timeout retries only for tools classified read-only; Code Mode keeps a native-call ledger and refuses repeated identical failures after two. Provider compliance, lost remote replies and remote exactly-once behavior remain unobserved. A fiber declares one recovery attempt and checkpoint phases, but this report does not establish deployed recovery success (SRC-1, `src/brain/turn/loop.ts`, `src/brain/turn/model-profile.ts`, `src/brain/tools/mcp/runtime-tools.ts`, `src/brain/tools/mcp/connector.ts`, `src/brain/turn/slack-turn-fiber.ts`).

### Context, persistence and change admission

[RT-RTE-context-boundary](#rt-rte-context-boundary) is deterministic context control at suspension and continuation. It removes old turn-state messages, replaces skill bodies with reload-required stubs, preserves active app discovery and preferentially keeps recent tool results. Older results become bounded heads plus argument summaries/digests. This resembles discarding parts of a frame, but the retained conversation is by value: a digest is not a dereferenceable pointer to the omitted original. `load_skill` supplies a current skill body on request. Research drafts isolate work in independent ephemeral turns, returning draft text and tool traces instead of attaching their full transcripts to the foreground turn (SRC-1, `src/brain/turn/context.ts`, `src/brain/skills/tools.ts`, `src/brain/auto-research/draft.ts`).

[RT-RTE-instruction-admission](#rt-rte-instruction-admission) covers human-approved skill creation and authorized workspace/model settings edits. Persisted text changes later context; symbolic model settings change model selection. Neither constitutes parameter training. [RT-RTE-knowledge-handoff](#rt-rte-knowledge-handoff) identifies the runtime's automatic memory-write and later context consumers, leaving memory transformations and revisions to the memory analyst. Signup research also has direct fast-model summary/enrichment calls and reset-epoch-checked memory writes; it is not entirely under the foreground tool loop. Entity resolution has a provider-native web-search call, separately recorded as [RT-RTE-entity-web](#rt-rte-entity-web). These calls constrain any assertion that all inference or external access passes through the main loop (SRC-1, `src/brain/turn/research.ts`, `src/brain/memory/entities.ts`).

No source finding here establishes agent-initiated modification of the deployed worker, provider weights or sandbox machinery. Those mechanisms were not exhaustively searched, so this is a limit, not an evidenced absence. Inspected positive change-admission paths concern instructions, configuration, connected-app grants, retained knowledge, scheduled work and research drafts. Product packaging, local SDK patches, detailed lease decision machinery, all HTTP/UI permission equivalences, memory splitting/profile transformations and every observability evaluator remain available but not fully inspected by this member. They cannot inherit the narrower guarantee assessments above.

**Added source coverage.** Beyond boundary's initial inspection, this member inspected implementation passages in `src/brain/turn/{brain-model,context,approval,model-profile}.ts`, `src/brain/settings/models.ts`, `src/routes/models.ts`, `src/config/index.ts`, `src/brain/tools/mcp/{runtime-tools,tool-policy,policy,connector,execute,preflight,operation-queue}.ts`, `src/brain/tools/sandbox/{tools,client,guards}.ts`, both sandbox adapters' validation call sites, `src/brain/tools/scheduler.ts`, `src/brain/skills/{store,tools,slack-interactions}.ts`, `src/brain/slack/turn-control.ts`, and `src/brain/memory/entities.ts`. Bounded searches inspected approval-classifier call sites, fiber declarations and auto-research send/run storage guards. All are SRC-1 implementation evidence, not observed runs. Searches that named nonexistent files were corrected to the actual tracked paths; no negative finding rests on those misses.

## Shared records

### Components

#### RT-CMP-brain-main
Label: Main brain model selection

Source-native identity: `getBrainModel` selected through `resolveBrainMainProfile`; default `grok-4.5`, organization-selectable supported models and provider-dependent fallback. Representational form: distributed-parametric provider model. Storage substrate: remote provider weights; only symbolic names/options live locally in source and organization metadata. Parameters changing during operation: uninspected — provider internals are outside SRC-1; no inspected client request trains weights. Exact model version pinned: no weight/version pin; shipped names are not immutable weight identities. Mutable endpoint may resolve another model: yes, local provider reachability substitution and gateway fallback can select a different candidate; remote alias resolution remains uninspected. SRC-1, `src/brain/turn/brain-model.ts`, `src/brain/turn/model-profile.ts`.

> if (canReach(provider, env)) return modelName
> --- `src/brain/turn/brain-model.ts`

> if (!config) return primary
> --- `src/brain/turn/brain-model.ts`

Thus a configured fallback candidate is not necessarily executed: without a gateway the first candidate is returned.

#### RT-CMP-triage-model
Label: Triage and fast model calls

Source-native identity: `TRIAGE_MODEL` defaults to `claude-haiku-4.5`; organization triage profile is used by Slack triage and Code Mode approval classification. `fastModel()` uses the default constant for small summary/observation calls rather than reading that organization's override. Form: distributed-parametric. Substrate: remote provider weights reached by the same `getBrainModel` provider/gateway resolver. Parameters changing during operation: uninspected — provider internals unavailable, and inspected calls are inference. Exact version pinned: no immutable weight pin. Mutable endpoint may resolve another model: yes, reachability and gateway substitution apply, and remote alias behavior is uninspected. This component is distinct from the foreground model role even when configuration chooses the same provider. SRC-1, `src/config/index.ts`, `src/brain/turn/model-profile.ts`, `src/brain/slack/triage.ts`, `src/brain/tools/mcp/approval-classifier.ts`.

> return getBrainModel(TRIAGE_MODEL, currentEnv)
> --- `src/config/index.ts`

#### RT-CMP-research-model
Label: Entity research model

Source-native identity: `RESEARCH_MODEL` (`grok-4.5`) passed to xAI responses through `wrapBrainGateway` in entity web resolution. Form: distributed-parametric. Substrate: remote xAI weights. Parameters changing during operation: uninspected — only inference request is visible. Exact version pinned: no immutable weight identity. Mutable endpoint may resolve another model: provider alias behavior is uninspected; this call locally supplies one gateway candidate, unlike foreground provider fallback. SRC-1, `src/brain/memory/entities.ts`, `src/brain/turn/model-profile.ts`.

> model: wrapBrainGateway(env, [xai.responses(RESEARCH_MODEL)]),
> --- `src/brain/memory/entities.ts`

### Operative objects

#### RT-OBJ-turn-state
Label: TurnState coordination data

Source-native identity: `TurnState` and `ApprovalResumeState`. Representational form: symbolic IDs, revisions, counters, app/skill records and statuses interpreted by host code; their rendered text also informs model decisions. Storage substrate: live TypeScript objects, serialized pending-approval state in Durable Object SQL, and thread-control SQL records. Current-run state is distinct from later principal-scoped investigation checkpoint recall. SRC-1, `src/brain/turn/compute.ts`, `src/brain/turn/approval.ts`, `src/brain/slack/turn-control.ts`.

> state_json TEXT NOT NULL,
> --- `src/brain/turn/approval.ts`

#### RT-OBJ-brain-skill
Label: Persisted skill body

Source-native identity: `brain_skill.body` exposed as a `RuntimeSkill`. Form: natural-language Markdown interpreted by the model; source-native identity/version/scope/status metadata is symbolic and controls visibility. Substrate: Durable Object SQL; static system skills also exist in shipped source. The mutable stored skill body, not its usage counter, is the behavior-shaping content. SRC-1, `src/brain/skills/store.ts`, `src/brain/skills/tools.ts`.

> return { name: loaded.name, body: loaded.body, version: loaded.version }
> --- `src/brain/skills/tools.ts`

#### RT-OBJ-workspace-prompt
Label: Standing workspace instructions

Source-native identity: `workspacePrompt`. Form: natural-language instructions interpreted in runtime context. Substrate: organization agent Durable Object, accessed through workspace-prompt methods. It is distinct from source-shipped system policy and from symbolic organization model settings. SRC-1, `src/routes/workspace-prompt.ts`, `src/brain/turn/compute.ts`.

> workspacePrompt: workspacePrompt ?? undefined,
> --- `src/brain/turn/compute.ts`

### Routes

#### RT-RTE-slack-turn
Label: Explicit Slack invocation

Endpoints/progression: signed Slack HTTP event → workspace/org agent → member actor and thread scope → context/tools → model steps → terminal settlement → Slack stream/fallback → eligible writeback. Owner: HTTP code admits; foreground model selects actions; host loop and Slack caller own stopping, coordination and delivery. Operating mode: open user requests, not a curriculum or controlled experiment. No expected-answer/reference-outcome oracle is wired in the inspected turn; tool evidence is not an oracle. Human supplies the problem, model proposes actions/answer, host can abort or supersede, and requester can veto gated actions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP acknowledgment, then a Slack reply/progress or an approval card; the compute API returns completed/suspended state.
- Later read-back: eligible interactive writeback and delayed observation can enter future ambient/search context; principal-scoped investigation checkpoints can enter later thread turns.
- Delegated visibility: selected messages and tools go to the chosen provider; remote app providers receive their call arguments, not a guaranteed whole transcript.
- Selection predicate: explicit-address routing and member/surface scope; tool selection by the model within host activeTools.
- Invalidation or expiry: abort/deadline, revision supersession, pending-update finalization checks; approval expires separately.
- Activation or effect: local wiring can publish Slack text, invoke remote tools and request memory writes; actual deployed effects unobserved.
- Evidence limits: no run trace; external services and SDK behavior are not implementation evidence in SRC-1.

SRC-1, `src/routes/slack/index.ts`, `src/brain/slack/turn.ts`, `src/brain/turn/compute.ts`, `src/brain/turn/loop.ts`.

> personalConnectionsOnly: true,
> readOnly: Boolean(passiveInvestigation),
> memberLookup: "found",
> --- `src/brain/slack/turn.ts`

#### RT-RTE-app-code
Label: Connected-app Code Mode

Endpoints/progression: `discover_app_methods` → catalog-selected executable methods → `run_app_code` → isolated JavaScript executor → native connector callbacks → remote provider → compact result/approval pause. Owner: foreground model proposes code; local discovery/preflight and connector policy decide admissibility; triage classifier resolves effects not already supplied by contracts/annotations/verb rules. Requester can veto paused calls. Operating mode: task-directed program execution, not an improvement experiment; no answer oracle. Capability grant is actor connection/lease selection, separate from program method discovery and executor isolation. Parameters: [RT-CMP-triage-model](#rt-cmp-triage-model).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: structured execution result, error or pending-approval output to the main loop.
- Later read-back: selected method/evidence checkpoints can persist through the enclosing turn; external app effects persist according to that app's contract.
- Delegated visibility: selected app methods and arguments reach provider handles; selected JavaScript receives exposed connectors, not unrestricted worker API authority.
- Selection predicate: app availability plus discovered methods and preflight input contracts; native classification uses contract override, trusted annotation, deterministic verb or classifier.
- Invalidation or expiry: lease revalidation, per-turn ledger and approval state; reset/retry mechanisms do not prove remote rollback.
- Activation or effect: read/metadata classified calls allowed; non-read access denied for read-only references or paused for approval otherwise.
- Evidence limits: classification can be wrong about a remote method's actual effect; SDK isolation and approval protocol are external contracts, not observed containment.

SRC-1, `src/brain/tools/mcp/execute.ts`, `src/brain/tools/mcp/connector.ts`, `src/brain/tools/mcp/policy.ts`, `src/brain/tools/mcp/preflight.ts`.

> if (operationIsRead(args.effect)) {
> return { decision: "allow", effect: args.effect }
> }
> --- `src/brain/tools/mcp/policy.ts`

> return evaluated.decision.decision === "pause"
> --- `src/brain/tools/mcp/connector.ts`

#### RT-RTE-direct-mcp
Label: Direct MCP fallback

Endpoints/progression: Code Mode unavailable/no apps → connect actor/leased servers → searchable index → search/describe/execute meta-tools → provider `callTool`. Owner: model selects ID/arguments; runtime-tools host filters grants and supplies SDK `needsApproval`. Operating mode: same open task, different execution surface. No answer oracle. Human requester can deny calls for which the predicate actually requests approval; connection owner/lease machinery determines borrowed grant.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: provider result or error in the tool loop.
- Later read-back: external app effects can outlive the turn; enclosing investigation state can retain selected evidence, not every raw result.
- Delegated visibility: call arguments go to the selected provider handle using personal, shared or leased credentials.
- Selection predicate: token/annotation tool classification; read-only actors and shared connections expose/execute only positively read tools; leases have an additional mode check.
- Invalidation or expiry: leased tools revalidate access at execution; transports are closed; non-leased remote credential revocation behavior is external.
- Activation or effect: provider call after local checks; personal unknown/dangerous names need not trigger approval unless the separate predicate matches.
- Evidence limits: direct and Code Mode do not have equivalent effect classifiers; remote action semantics and SDK approval enforcement remain external.

SRC-1, `src/brain/turn/tools.ts`, `src/brain/tools/mcp/runtime-tools.ts`, `src/brain/tools/mcp/tool-policy.ts`.

> if (annotations?.destructiveHint === true) return true
> return tokenizeToolName(toolName).some((tok) => WRITE_VERBS.has(tok))
> --- `src/brain/tools/mcp/tool-policy.ts`

> if (t.lease) return runLeasedTool(t, t.lease, id, args)
> --- `src/brain/tools/mcp/runtime-tools.ts`

#### RT-RTE-approval-resume
Label: Requester approval and continuation

Endpoints/progression: suspension → SQL pending approval/conversation/assembly snapshot → Slack card → signed interaction dispatch → team/requester/status/expiry/current-turn/member verification → resume turn. Owner: host persists/validates; requester approves or denies; model continues with restored context and tools. Operating mode: continuation of open request. No answer oracle; approval is permission, not a correctness test. Proposed change is the specific gated action, not arbitrary future actions. Rejection prevents that approval from being consumed as permission; expiry/supersession cancels it. Recovery restores serialized state and can request a new approval; external effects have no general transactional rollback in the inspected path.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: card and suspended compute result, then continued reply or another suspension.
- Later read-back: stored resume messages/state reach a subsequent invocation; later interactive memory writeback is handled by the caller.
- Delegated visibility: bounded serialized conversation returns to the model; app pause reference identifies connected-app continuation.
- Selection predicate: exact approval ID, team and requester, pending state, expiry and current turn.
- Invalidation or expiry: 15 minutes; newer thread revision, terminal approval status and rebound workspace can prevent resumption.
- Activation or effect: approval response/connected-app resolution enables the specified continuation; successful remote execution unobserved.
- Evidence limits: source shows verification and resume wiring, not provider/SDK compliance or idempotence under every failure.

SRC-1, `src/brain/turn/approval.ts`, `src/brain/slack/turn.ts`, `src/brain/turn/resume.ts`.

> if (approval.askerUser !== decision.userId) {
> --- `src/brain/slack/turn.ts`

> export const APPROVAL_EXPIRY_MS = 15 * 60 * 1000
> --- `src/brain/turn/approval.ts`

#### RT-RTE-context-boundary
Label: Continuation context compaction

Endpoints/progression: approval suspension/live-update continuation → `compactMessagesAtBoundary` → bounded serialized/rebased messages → resumed model. Owner: deterministic code rules, not a summarizing model. This is working-context control and, when restored into a later invocation, retained conversation memory. It does not critique or revise a theory. SRC-1, `src/brain/turn/context.ts`, `src/brain/turn/compute.ts`, `src/brain/turn/resume.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: transformed message array, preserving message/tool-call structure.
- Later read-back: approval resume and continuation consume compacted results; `load_skill` reloads current content on demand.
- Delegated visibility: the next model receives retained heads, summaries/digests/stubs instead of every original tool body.
- Selection predicate: old turn-state removed; loaded skills stubbed unless explicitly preserved; active app discovery preserved; recent results preferentially kept/bounded.
- Invalidation or expiry: repeated compaction skips already compacted/bounded values; skill stub version records provenance but does not freeze a later reload.
- Activation or effect: changes model-visible context and reduces raw result visibility; quality or token savings unmeasured.
- Evidence limits: removed raw content is not recoverable from its digest; not a complete semantic summary or evidence-preservation guarantee.

> reloadRequired: true,
> resultDigest: stableDigest(serialized),
> originalChars: serialized.length,
> --- `src/brain/turn/context.ts`

#### RT-RTE-sandbox-work
Label: Sandbox command and artifact work

Endpoints/progression: enable family → start/reuse scoped session → bounded command/file/artifact tools → Cloudflare or Daytona client → results; interactive artifact output may upload to Slack. Owner: model selects commands; host normalizes/validates; external sandbox executes. Operating mode: task work, not a product-improvement curriculum. No answer oracle. Commands propose local workspace changes; regex command rules can reject selected forms. Session deletion/recreation handles stale or changed repository scope, not general command rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: exit status/output or file/artifact data, bounded by tool/provider adapters.
- Later read-back: active scoped session may be reused; actual workspace persistence depends on provider lifetime; model context retains returned results through enclosing turn rules.
- Delegated visibility: sandbox receives command/cwd and optional public repository URL; Slack upload receives selected artifact, not the whole workspace.
- Selection predicate: deployment configured sandbox; actor/thread/turn session key and same repository scope; model unlocks optional family.
- Invalidation or expiry: stale/not-running or changed-repository session is dropped; expiry tracked; command execution clears artifact upload cache.
- Activation or effect: executes shell and filesystem work; interactive sharing additionally checks abort/current-turn status.
- Evidence limits: command regexes are not full effect mediation; deployed sandbox isolation, credentials and network envelope are not supplied.

SRC-1, `src/brain/tools/sandbox/tools.ts`, `src/brain/tools/sandbox/client.ts`, `src/brain/tools/sandbox/guards.ts`, `src/brain/tools/sandbox/cloudflare-client.ts`, `src/brain/tools/sandbox/daytona-client.ts`.

> if (env.DAYTONA_API_KEY) return createDaytonaSandboxClient(env)
> return createCloudflareSandboxClient(env)
> --- `src/brain/tools/sandbox/client.ts`

> for (const blocked of BLOCKED_COMMAND_PATTERNS) {
> if (blocked.pattern.test(trimmed))
> return { ok: false, error: blocked.reason }
> }
> return { ok: true, command: trimmed }
> --- `src/brain/tools/sandbox/guards.ts`

#### RT-RTE-scheduled-task
Label: Schedule admission and later delivery

Endpoints/progression: model-selected scheduler tool → normalized time/destination/participants → `agent.schedule` retained payload → alarm callback → workspace/org/entitlement checks → fresh compute turn → Slack post. Owner: model proposes payload; software validates/adopts it; creator can update, creator/eligible related user can cancel. Trigger: user-directed reminder/digest creation, then stored time/cron. Change: durable instruction and future production invocation. Guidance is tool schema plus caller request/destination rules; payload persists. No per-content human approval gate appears in the inspected schedule tool. Rejection is software validation; recovery includes failed creation errors, cancellation and replace operations. Operating mode: recurring/delayed open tasks, not experiments. No answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: schedule ID/type/timing or validation error to current turn.
- Later read-back: stored instruction, scope, creator and destination are consumed by an independent scheduled model invocation.
- Delegated visibility: selected context/tools reach model; completed text is automatically delivered to destination.
- Selection predicate: timing and destination validation; callback belongs to current workspace/org and entitlement; actor flags are derived from payload.
- Invalidation or expiry: cancellable schedule relationships; missing/rebound workspace cancels; entitlement or missing target prevents run/delivery.
- Activation or effect: fresh model answer and automatic Slack delivery; suspended/noncompleted result is dropped rather than interactively resumed here.
- Evidence limits: `scheduledRun` omits tool families but is not identical to `actor.readOnly`; actual scheduling/service delivery unobserved.

SRC-1, `src/brain/tools/scheduler.ts`, `src/brain/tools/scheduling.ts`.

> readOnly: payload.readOnly,
> --- `src/brain/tools/scheduling.ts`

> if (out.status !== "completed") {
> --- `src/brain/tools/scheduling.ts`

#### RT-RTE-research-draft
Label: Operator research drafts

Endpoints/progression: manual research run → model plan → batched independent ephemeral draft turns → local draft storage → separate send operation. Owner: operator triggers/steers; models propose jobs/text; software stores only under current ownership; reviewer selects delivery. Operating mode: bounded drafting round with operator focus and previous sent/drafted material, not a controlled experiment. No expected-answer oracle. Proposed production output is a draft, not an automatically sent Slack reply. Rejection can occur through empty/noncompleted draft, reset/ownership loss, or human withholding send; send failure releases its claim for retry. Storage/send code paths were inspected at bounded call sites, not every console endpoint or permission gate.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: draft text, tool trace/flags and round outcome; draft work does not itself post to Slack.
- Later read-back: previous sent/drafted bodies guide planning/drafting; stored draft is consumed by a separate send operation.
- Delegated visibility: person draft uses recipient personal context; channel draft uses org-shared context; each returns selected text/trace, not its full transcript to a parent model.
- Selection predicate: operator focus/steer and model-planned jobs; actor readOnly plus scheduledRun; ephemeral mode avoids thread-investigation persistence.
- Invalidation or expiry: reset/ownership checks before inserting draft; send claim and release on failure; finer draft lifecycle uninspected.
- Activation or effect: draft enters local review state; separate explicit send can deliver stored body.
- Evidence limits: no run evidence of content quality, review decisions or successful sends; text flags are authored evaluation logic, not tested outcomes.

SRC-1, `src/brain/auto-research/run.ts`, `src/brain/auto-research/draft.ts`, `src/brain/auto-research/send.ts`.

> ephemeral: true,
> --- `src/brain/auto-research/draft.ts`

> insertAutoResearchDraft(agent, result.draft)
> drafted++
> --- `src/brain/auto-research/run.ts`

#### RT-RTE-instruction-admission
Label: Skills and standing configuration admission

Endpoints/progression: explicit save request → model-authored pending skill draft → requester scope/approval → validated active SQL skill → visible index/load; independently, authorized HTTP workspace prompt/model settings edits → stored prompt/organization metadata → subsequent context/model selection. Owner: model proposes Slack skill text; verified creator approves and selects scope, with admin requirement for organization scope; human API editor supplies standing prompt/config, role gate admits. Software validates length/schema/scope and can reject. Operating mode: open human-directed editing, not comparative experimentation. No answer oracle. Proposed changes concern localized instructions or configuration, not provider parameter updates. Guidance includes source-native “skills hold how” and request/scope instructions; persisted body is a playbook. Rollback/recovery: authorized skill update/delete/disable and prompt replacement/null; failed draft claims return errors. No historical-version rollback guarantee is established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: skill confirmation card/save response, or workspace/model settings API response.
- Later read-back: visible skill metadata is listed in runtime context, body loaded by name; workspace prompt is loaded automatically; model configuration resolves future profiles.
- Delegated visibility: selected bodies/instructions reach model; personal skill visibility and org-scope management have separate checks.
- Selection predicate: creator identity for Slack draft, admin for org scope, active/visible skill load; admin role gate for standing prompt/model edits.
- Invalidation or expiry: pending draft expires/cancels; updates increment skill version; deletion/disable changes visibility; null settings remove overrides.
- Activation or effect: changes later model input or symbolic model selection; reliable following and improved action are unobserved.
- Evidence limits: API/Slack are distinct admission surfaces; no exhaustive audit of every configuration tool/UI editor or theory-directed criticism is claimed.

SRC-1, `src/brain/skills/tools.ts`, `src/brain/skills/slack-interactions.ts`, `src/brain/skills/store.ts`, `src/routes/workspace-prompt.ts`, `src/routes/models.ts`, `src/brain/settings/models.ts`, `src/brain/turn/compute.ts`.

> if (scope === "org" && !verified.actor.isAdmin) {
> --- `src/brain/skills/slack-interactions.ts`

> roleGate({ minimum: ROLE_ADMIN }),
> validator("json", WorkspacePromptSchema),
> --- `src/routes/workspace-prompt.ts`

#### RT-RTE-knowledge-handoff
Label: Runtime memory admission and recall

Endpoints/progression: interactive terminal memory capture → eligible current-turn writeback → memory adapter; separately delayed human-evidence style observation → agent-self memory; later ambient profile/interaction style/search consumes retained content. Owner: model proposes retained text, software admits subject to caller/scope/reset checks; no per-document human approval in these inspected paths. Trigger: completed interactive work or delayed fresh Slack observations. Proposed change: retained facts or team operating/style notes. Guidance constrains style observation to HUMAN evidence and excludes access/policy instructions; note/cursor state persists. Rejection includes passive/stale generation/non-note/adapter failure. Recovery retries nonaccepted writes and deletes stale-generation documents; full memory revision rules belong to the memory member. Operating mode: continuous background observation and task writeback, not experiments; no answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: asynchronous write/observe result and cursor state; not a second user answer.
- Later read-back: future `computeTurn` loads ambient and style context and exposes memory search.
- Delegated visibility: model-selected documents go to hosted memory service; observer receives bounded labeled Slack messages and prior carried state.
- Selection predicate: nonpassive current turn with eligible writer/documents; observer fresh batch, generation checks and non-note filtering; downstream scope selection matters independently.
- Invalidation or expiry: turn supersession and memory reset generation guards; service-level invalidation/supersession is opaque here.
- Activation or effect: durable behavior-shaping text is delivered to later context consumers; actual changed behavior/benefit unobserved.
- Evidence limits: source request to learn preferences is not reliable human-evidence compliance; hosted extraction/ranking and specialist revision semantics are not established by this record.

SRC-1, `src/brain/slack/turn.ts`, `src/brain/turn/interaction-observe.ts`, `src/brain/turn/compute.ts`.

> if (result.status !== "queued" && result.status !== "done") {
> return "retry"
> }
> --- `src/brain/turn/interaction-observe.ts`

#### RT-RTE-entity-web
Label: Provider-native entity lookup

Endpoints/progression: reference normalization → current-generation shared entity lookup → xAI model/native web search fallback → JSON parse → optional shared-memory cache. Owner: host decides cache/web route; research model proposes canonical entity; software parses/adopts it, no per-entity human approval. Trigger: unresolved entity reference. Guidance asks identification and JSON fields; retained result is canonical entity/aliases/domain, not a retained rationale. Rejection: unavailable xAI, missing/invalid JSON or empty canonical. The generation check after `findEntity` rejects a lookup overtaken by reset; `writeEntity` separately skips stale-generation writes and requests deletion of accepted late writes. There is no generation check after `resolveViaWeb` or before `return web`: reset during provider inference can still yield an old-generation result to a read-only caller, or to a writable caller after its cache write is skipped or stale-deleted. Operating mode: open lookup, not experiment; existing memory is evidence, not an answer oracle. This is distinct from `search_web`'s host-side context.dev/Firecrawl snippet path.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resolved entity or null to calling tool; web results are returned without a post-inference generation check, even when persistence is disabled or a stale write is skipped/deleted.
- Later read-back: persisted entity can answer a later matching reference within current generation.
- Delegated visibility: reference reaches xAI and provider-native web tool; hosted search internals uninspected.
- Selection predicate: known entity first; web only with xAI availability; persist flag controls caching, and read-only caller disables persistence.
- Invalidation or expiry: reset-epoch-filtered lookup with a post-lookup generation check; generation-scoped cache IDs, pre-write guard and stale late write cleanup. These guards do not fence delivery of web results after a reset during inference.
- Activation or effect: optional shared cache write, plus external provider search outside main-loop MCP mediation.
- Evidence limits: JSON parsing and cache admission do not validate real-world identification accuracy or establish return freshness across resets; native tool execution and successful stale-write cleanup not observed.

SRC-1, `src/brain/memory/entities.ts`, `src/brain/turn/tools.ts`.

> tools: { web_search: xai.tools.webSearch() },
> --- `src/brain/memory/entities.ts`

The lookup guard precedes provider inference; the resolver tail does not repeat it before returning the web result:

> if (!isBrainMemoryResetEpochCurrent(agent, resetEpoch)) return null
> if (known) return known
> const web = await resolveViaWeb(env, ref, costLedger)
> if (!web) return null
> if (persist) {
> await writeEntity(env, org, userId, web, agent, resetEpoch).catch((err) =>
> captureException(err instanceof Error ? err : new Error(String(err)), {
> tags: { component: "entities" },
> }),
> )
> }
> return web
> --- `src/brain/memory/entities.ts`

The cache writer guards persistence independently:

> if (!isBrainMemoryResetEpochCurrent(agent, resetEpoch)) return
> const key = entity.domain || entity.canonical
> --- `src/brain/memory/entities.ts`

> (result.status === "queued" || result.status === "done") &&
> !isBrainMemoryResetEpochCurrent(agent, resetEpoch)
> ) {
> await deleteStaleBrainMemoryDocument({
> env,
> orgId: org.id,
> documentId: result.id,
> })
> }
> --- `src/brain/memory/entities.ts`

### Claims

#### RT-CLM-write-approval
Label: Connected-app writes pause for approval

Claimed operation: Code Mode tool description promises automatic user approval for writes. Source: SRC-1, `src/brain/tools/mcp/execute.ts`. Scope supported: policy-classified non-read native calls pause on writable Code Mode references; read-only references deny. Scope not supported: all equivalent external-effect paths, especially direct personal MCP predicate and shell execution. See [RT-RTE-app-code](#rt-rte-app-code), [RT-RTE-direct-mcp](#rt-rte-direct-mcp), [RT-RTE-sandbox-work](#rt-rte-sandbox-work).

> Writes pause for user approval automatically.
> --- `src/brain/tools/mcp/execute.ts`

Guarantee owner: application connector/approval host. Enforcement point: native classification and approval callback, or distinct direct SDK predicate. Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: remote method semantics must match classification; SDK executor must honor approval pause. No global external-write invariant follows.

#### RT-CLM-turn-fencing
Label: Current-thread delivery fencing

Claimed operation: current turn/revision owns publication and pending updates prevent finalization. Source: SRC-1, `src/brain/slack/turn-control.ts`, `src/brain/turn/compute.ts`, `src/brain/slack/turn.ts`. Guarantee owner: SQL coordination plus caller delivery fences. Enforcement point: conditional finalization claim and `isThreadTurnCurrent`. Guarantee strength: protocol. Covered paths: coordinated Slack turn/approval continuations. Alternate paths: scheduled/draft/debug computation without that control do not inherit the same fence. Required external contract: Durable Object SQL and caller delivery behavior; already-performed remote tool effects cannot be undone by dropping a reply. Implementation conclusion status: wired. Operation conclusion status: uninspected.

> if (!control) return true
> --- `src/brain/slack/turn-control.ts`

> AND status IN (${"classifying"}, ${"pending"})
> --- `src/brain/slack/turn-control.ts:480-480`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-standing-instructions
Label: Standing text reaches model decisions

Consumer: later foreground model invocation. Channel: runtime context supplies workspace prompt and skill index; `load_skill` returns selected body. Force: natural-language guidance interpreted by model, not executable policy or proven compliance. Horizon: later problems/sessions while stored instruction remains active. [RT-OBJ-workspace-prompt](#rt-obj-workspace-prompt), [RT-OBJ-brain-skill](#rt-obj-brain-skill) and [RT-RTE-instruction-admission](#rt-rte-instruction-admission) supply identity/admission. Evidence: SRC-1, `src/brain/turn/compute.ts`, `src/brain/skills/tools.ts`.

#### RT-BAP-tool-policy
Label: Symbolic grants constrain execution

Consumer: host assembler and native/direct tool executor. Channel: actor flags, connections, lease scope, activeTools and effect-policy decision. Force: executable availability/deny/pause rule at named local enforcement points; remote semantics remain external. Horizon: current invocation and approval continuation, with revalidated durable grants. [RT-RTE-app-code](#rt-rte-app-code) and [RT-RTE-direct-mcp](#rt-rte-direct-mcp) are distinct consumers/policies, not interchangeable security guarantees. Evidence: SRC-1, `src/brain/turn/tools.ts`, `src/brain/tools/mcp/policy.ts`, `src/brain/tools/mcp/runtime-tools.ts`.

## Annotations

none
