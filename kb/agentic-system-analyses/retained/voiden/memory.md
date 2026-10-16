---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Voiden memory mechanisms: recorded responses, captured execution variables, CLI history, installed guidance and opaque verification retention."
run-id: AAS-2026-10-14-voiden-98188b4a2f55-01
source-identity: "https://github.com/voidenhq/voiden"
reviewed-boundary: d7a0d05c40acb6cc483000643c700f17aecba0ef
---

# Voiden memory report

## Boundary and evidence

This report covers retained material and working-context controls in Voiden's agent-facing MCP integration subsystem, at SRC-1 commit **d7a0d05c40acb6cc483000643c700f17aecba0ef**. It inherits the subsystem-only boundary, source register and exclusions of [boundary](boundary.md#boundary-and-evidence). The external model host owns conversation history, context assembly, tool choice and any decision to reuse returned results. General desktop storage is not silently included merely because a runner comment mentions it.

Evidence is inspected implementation and source-native guidance, not observed operation. Direct reads add the parser, schema normalization, capture/substitution implementation, session history helpers and CLI consumers to the supplied runtime account. HEAD was checked against the frozen revision. No target, test, service, provider or example was executed. The supplied runtime remains evidence for registration, plugin admission and outgoing MCP behavior where noted; it is not a substitute for a demonstrated model-consumer route.

| Entry point or memory operation | SRC-1 paths and inspection basis | Records, unresolved part and conclusion limit |
| --- | --- | --- |
| Fixed MCP discovery, execution, optional response write | Direct: `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/resultBlock.ts` | [MEM-OBJ-response](#mem-obj-response); annotations on [RT-RTE-result-write](runtime.md#rt-rte-result-write). Listing requests returns previews, not stored response bodies. |
| Document reload, linked content, plugin-visible document | Direct: `packages/voiden-runner/src/runner.ts`, `packages/executors/src/voidParser.ts`, `packages/voiden-runner/src/blockSchemaRegistry.ts`; linked resolver call sequence inspected, shared expansion internals not reread | [MEM-RTE-response-reload](#mem-rte-response-reload). Normalized blocks reach callbacks, but external plugins' treatment of historical responses is unavailable. |
| Capture, script mutation, substitution | Direct: `packages/voiden-runner/src/runtimeVars.ts`, `packages/voiden-runner/src/runner.ts`, `packages/voiden-runner/src/cliElectron.ts` | [MEM-RTE-runtime-capture](#mem-rte-runtime-capture); [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars). Script implementation is external; core exposes the shared map. |
| Standalone run persistence and cleanup | Direct dispatch ranges: `packages/voiden-runner/src/index.ts`; direct helpers: `packages/voiden-runner/src/session.ts`, `packages/voiden-runner/src/plugins/store.ts` | [MEM-OBJ-process-env](#mem-obj-process-env), [MEM-OBJ-session-results](#mem-obj-session-results), [MEM-RTE-history-report](#mem-rte-history-report); [RT-RTE-session-driver](runtime.md#rt-rte-session-driver). User-level retention is not project-isolated. |
| Selected environment and HTTP session lifecycle | Direct: fixed handlers and `packages/voiden-runner/src/mcpSessions.ts`; supplied runtime for caller wiring | Annotation on [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars). Profile resolver internals and actual secret provenance not independently traced; cannot establish all environment acquisition rules. |
| Installed authoring and MCP guides, refresh and removal | Direct: `apps/electron/src/main/skillsComposer.ts`, `apps/electron/src/main/skillsInstaller.ts`, opening guidance of `apps/electron/skills/base.skill.md`; supplied runtime for host registration and standalone MCP guide | Annotations on [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance), [RT-RTE-host-registration](runtime.md#rt-rte-host-registration). External host loading and downloaded guide bodies unavailable. |
| Plugin files, metadata and registry reload | Direct store helpers; supplied runtime for download/import/management wiring | Annotation on [RT-CMP-plugin-runner](runtime.md#rt-cmp-plugin-runner). External runner bytes and Node replacement behavior remain unresolved, not learned memory inferred from plugin labels. |
| Publisher startup, refresh, rejection, withdrawal and dynamic mode | Direct interface: `packages/voiden-runner/src/mcpToolCapability.ts`; selected scheduler/flag passages: `packages/voiden-mcp/src/lib.ts`; supplied runtime for HTTP/stdio wiring | [MEM-OBJ-verify-entry-cache](#mem-obj-verify-entry-cache); annotation on [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions). Provider owns actual cache mutation, cadence, dynamic selection and descriptions; these semantics are unavailable. |
| CLI tool verification with optional write-back | Direct dispatch: `packages/voiden-runner/src/index.ts`; provider dispatcher/interface direct | [MEM-OBJ-tool-status-record](#mem-obj-tool-status-record), [MEM-RTE-status-write](#mem-rte-status-write). Known invocation does not establish physical provider storage or later status read-back. |
| Outgoing MCP session/token reuse | Supplied runtime at `packages/executors/src/mcp.ts`, `packages/executors/src/secureRequest.ts` | [RT-RTE-remote-mcp](runtime.md#rt-rte-remote-mcp); session IDs are access metadata, not retained request knowledge. Authorization-plugin persistence and remote stores remain opaque. |

## Core ideas

1. **Recorded outcomes and executable carry-over are different.** A response block is a caller-proposed, truncated record in a project document. Captured runtime variables are automatically extracted values with a concrete later substitution consumer. The first is not authenticated by its timestamp; the second can change later request arguments without conveying an explanation. See [MEM-OBJ-response](#mem-obj-response), [MEM-RTE-runtime-capture](#mem-rte-runtime-capture).
2. **Persistence depends on the driver.** MCP maps persist between calls in a process/session. Standalone CLI session mode additionally loads and saves a user-global variable file and appends result history. This contradicts a stale capture-module comment saying every run resets the map; executable dispatch is the counterexample. History is later consumed by reporting, not automatically as a model prompt. See [MEM-OBJ-process-env](#mem-obj-process-env), [MEM-RTE-history-report](#mem-rte-history-report).
3. **Guidance packaging controls what is initially reachable, not the host's window.** Composition retains full enabled-extension guides separately and puts short descriptions in the base skill. The foreground agent is instructed to load the needed guide. That is an on-demand affordance with an opaque external context owner, not implemented conversation compaction or a model subtask frame. See the annotation on [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance).
4. **Verification retention is only partly visible.** The core passes a reusable cache to a provider and later registers provider decisions. It also exposes explicit status write-back. Cache entries, readable description notes and persistent status summaries are different operative parts; none independently proves that the provider verified a tool or reread a written status. See [MEM-OBJ-verify-entry-cache](#mem-obj-verify-entry-cache), [MEM-OBJ-tool-status-record](#mem-obj-tool-status-record).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-response
Label: response

Source-native fenced YAML `type: response` in the same `.void` document as the identified request. Symbolic fields include generated UID, requestUid, capturedAt, supplied success/status/timing, selected headers/body and error. Body and error strings are opaque payloads to serialization, potentially natural-language evidence to an external reader; they are not automatically instructions. The plain Markdown heading is only a readable marker. Source: SRC-1, `packages/voiden-runner/src/resultBlock.ts`.

Lineage: caller-supplied `RunResult`-shaped object → selected attributes → YAML → insertion/replacement. String body length is limited to 20,000 characters; an added flag indicates truncation, without preserving the omitted suffix. Protocol, method, URL and reportEntries from the immediate result are not copied by this builder. capturedAt records serialization time, not authenticated execution time. No structured criticism or rationale field is generated. A supplied error can carry a reason, but its truth is not established.

Distinct from the write route [RT-RTE-result-write](runtime.md#rt-rte-result-write): this is its retained output object, not another admission route; no supplied object counterpart after comparison. Later core consumption is [MEM-RTE-response-reload](#mem-rte-response-reload); human/agent file inspection is afforded but its occurrence is unobserved.

> const MAX_BODY_CHARS = 20_000
> --- `packages/voiden-runner/src/resultBlock.ts`

> if (typeof body === 'string' && body.length > MAX_BODY_CHARS) {
>     body = body.slice(0, MAX_BODY_CHARS)
>     truncated = true
>   }
> --- `packages/voiden-runner/src/resultBlock.ts`

> const attrs: Record<string, any> = {
>     uid: randomUUID(),
>     requestUid,
>     capturedAt: new Date().toISOString(),
>     success: result.success,
>   }
> --- `packages/voiden-runner/src/resultBlock.ts`

#### MEM-OBJ-process-env
Label: .process.env.json

Part of: [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars)

The durable standalone-CLI part of the runtime variable container. Symbolic JSON key/value state stored at `join(STORE_DIR, '.process.env.json')`, where STORE_DIR is `~/.voiden`, not the selected project. Values may themselves contain structured objects or strings. Source: SRC-1, `packages/voiden-runner/src/index.ts`, `packages/voiden-runner/src/plugins/store.ts`.

Lineage is mixed: previously loaded JSON, configured request/response captures and plugin script writes to the shared map. Actual initial content and external edits are uncaptured. The CLI loads the whole JSON into runtimeVars without per-key approval and writes the nonempty final map after execution in session mode. The later consumer is the next session-mode CLI run, followed by substitution and plugin callbacks; `session vars` separately displays actual values. It retains values, not capture expressions, source-run IDs or reasons. Authored capture configuration remains in the request document, but is not embedded as provenance in this file. Explicit `session clear` deletes it. No TTL or per-project partition appears in this inspected driver.

> const data = JSON.parse(readFileSync(VARS_PATH, 'utf-8'))
>         Object.assign(runtimeVars, data)
> --- `packages/voiden-runner/src/index.ts`

> export const STORE_DIR = join(homedir(), '.voiden')
> --- `packages/voiden-runner/src/plugins/store.ts`

#### MEM-OBJ-session-results
Label: SessionResult history

Source-native array of `{file, result}` in `~/.voiden/results.json`, symbolic JSON containing request/response strings, status and other `RunResult` fields. Source: SRC-1, `packages/voiden-runner/src/session.ts`, `packages/voiden-runner/src/index.ts`. This is a distinct output of [RT-RTE-session-driver](runtime.md#rt-rte-session-driver), not the variable-map referent [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars).

Lineage: section results, or driver-generated failure results for file exceptions, appended to old parsed history. It is an execution-outcome history, not a derived method or summary. `loadSessionResults` treats missing/malformed data as an empty array. The report and export commands are concrete later consumers, detailed in [MEM-RTE-history-report](#mem-rte-history-report). No core path traced here loads this array into future request substitution or a model prompt. That bounded finding does not rule out external consumers.

> export function appendSessionResults(results: SessionResult[]): void {
>   const existing = loadSessionResults()
>   saveSessionResults([...existing, ...results])
> }
> --- `packages/voiden-runner/src/session.ts`

#### MEM-OBJ-verify-entry-cache
Label: VerifyEntryCache

Part of: [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions)

The separately assessed cache part of the supplied combined object. Source-native symbolic Map of records with passed, optional reason/runResult and verifiedAt, in publisher process memory. SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts` defines the shape and cadence intent; [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication) supplies the startup and repeated-plan passages at `packages/voiden-mcp/src/lib.ts`.

Lineage is provider-owned and uninspected: core creates the map and supplies it to later planning calls, but the missing provider performs writes, invalidation and actual cached-result selection. Passing a mutable map is wired; the claimed per-entry cadence behavior is not established by the interface alone. A reason field permits retention of auth/contract-failure categories, and runResult can carry more evidence; neither establishes an explanatory rationale or that a later plan actually reads it. Restart discards this core-owned map. Tool-list changes are not a proved complete invalidation scheme merely because a comment describes index-based cache keys.

> export interface VerifyEntryCacheRecord {
>   passed: boolean
>   reason?: 'auth-failure' | 'contract-failure'
>   runResult?: any
>   verifiedAt: number
> }
> export type VerifyEntryCache = Map<string, VerifyEntryCacheRecord>
> --- `packages/voiden-runner/src/mcpToolCapability.ts`

#### MEM-OBJ-tool-status-record
Label: ToolStatusRecord

Symbolic protocol shape declaring state, lastCheckedAt and optional note, distinct from the process-local cache/decisions in [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions). SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts`. The actual status write API accepts only state/note plus file/UID; timestamp construction and serialized location are delegated to the external provider. Thus the declared type does not prove an actual persisted timestamp or substrate. The CLI requests project-file write-back, but exact file representation and later consumer remain uninspected beyond the dispatch in [MEM-RTE-status-write](#mem-rte-status-write).

State is symbolic, note is potentially natural-language display text. Compared with full ToolStatus results, this is a reduced requested summary: the CLI passes no per-entry results/runResult to upsert. Whether the provider retains other reasons or separately reconstructs them is unknown. It is not the response block and is not a verified historical fact merely because state says verified.

> export interface ToolStatusRecord {
>   state: ToolState
>   lastCheckedAt: string
>   note?: string
> }
> --- `packages/voiden-runner/src/mcpToolCapability.ts`

### Routes

#### MEM-RTE-response-reload
Label: Recorded response reload

Part of: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)

The document-input segment of the execution route, specifically carrying retained response blocks. Trigger: later runVoidFile invocation after a write. Owner/selector: core rereads the named file, parses all valid void fences, resolves linked content, groups sections and normalizes selected blocks, then exposes them through editor.getJSON to registered builders/hooks. Context and state: current project document and plugin schemas, not a model-selected memory search. Sources: SRC-1, `packages/voiden-runner/src/runner.ts`, `packages/executors/src/voidParser.ts`, `packages/voiden-runner/src/blockSchemaRegistry.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: document blocks to callbacks within execution; outer route returns newly executed results, not a stored-response retrieval response.
- Later read-back: [MEM-OBJ-response](#mem-obj-response) is parsed as a block on a subsequent invocation and included in the selected section's callback-visible document; plain Markdown heading is not a parsed block.
- Delegated visibility: registered builders/hooks receive normalized document JSON; the external model receives new execution results unless it separately reads the document.
- Selection predicate: named file and section rules of [RT-RTE-request-execution](runtime.md#rt-rte-request-execution), not response relevance; parser admits syntactically parseable fences without a response-specific truth check.
- Invalidation or expiry: current disk content replaces prior content on each reread; malformed fences are omitted; linked content follows the resolver sequence; no stored-response TTL.
- Activation or effect: delivery to callback-visible JSON is wired; whether a plugin uses a stored response to change behavior is uninspected because those implementations are unavailable.
- Evidence limits: shared block delivery proves neither prompt injection into an external model nor use as an oracle for future execution. Normalization supplies defaults without validating factual authenticity.

> const content  = readFileSync(filePath, 'utf-8')
>   const resolver = createLinkedBlockResolver(options.projectRoot ?? process.cwd())
> --- `packages/voiden-runner/src/runner.ts`

> const doc    = blocksToDoc(normalizedBlocks)
>     const editor = { getJSON: () => doc }
> --- `packages/voiden-runner/src/runner.ts`

> const block = parseVoidBlockText(match[1])
>     if (block) {
>       blocks.push(block)
>     }
> --- `packages/executors/src/voidParser.ts`

#### MEM-RTE-runtime-capture
Label: Runtime value capture

Part of: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)

Automatic extraction segment: configured runtime-variables rows plus current request/response → shared runtimeVars → later request substitution. Sources: SRC-1, `packages/voiden-runner/src/runner.ts`, `packages/voiden-runner/src/runtimeVars.ts`, `packages/voiden-runner/src/cliElectron.ts`. This updates [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars); standalone persistence is separately owned by [RT-RTE-session-driver](runtime.md#rt-rte-session-driver).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: in-place variable-map mutation after a section response is mapped; outer route returns the section result.
- Later read-back: later sections/calls use process-variable paths through applyProcessVarsToState; standalone session mode reloads [MEM-OBJ-process-env](#mem-obj-process-env) for later CLI runs.
- Delegated visibility: core resolves request/response fields, plugins receive the shared map, and network or outgoing MCP endpoints can receive substituted values; external model need not see the map.
- Selection predicate: enabled authored capture rows; $req/$res field expressions select values, including structured body paths and duplicate-cookie-aware response headers. Later request templates select named process-variable paths, rather than semantically searching history.
- Invalidation or expiry: successful extraction overwrites the named key; null/undefined single-expression extraction leaves the old key unchanged; mixed interpolation writes a string with missing pieces empty. Lifetime follows map/session/durable-driver cleanup.
- Activation or effect: later request fields are programmatically substituted from retained values; recurrent operation and benefit are unobserved.
- Evidence limits: captures are values, not methods. Core response handling can capture after a failed status response; a thrown section exception continues before capture. Script mutations and their meanings belong to external plugins.

Admission: the document author proposes capture keys/expressions; software decides which extracted values to retain without a separate human decision per value. Actual human versus model authorship of the configuration is uncaptured. Disabling a row prevents this capture, not deletion of a previously stored key. There is no correctness oracle or performance comparison in this transformation; mode is ordinary request execution, triggered by completion rather than an improvement experiment. Recovery is overwrite or session clear, not restoration of prior request effects. Raw request/response → selected typed value → later substitution is a trace-fed behavior-shaping chain, but it retains no generated reason for adopting the value and establishes no capacity improvement.

> const captured = evalExpr(expr, req, res)
>       if (captured !== undefined && captured !== null) vars[row.key] = captured
> --- `packages/voiden-runner/src/runtimeVars.ts`

> preSendProcess: (state: RestApiRequestState) =>
>         Promise.resolve(applyProcessVarsToState(state, runtimeVars) as RestApiRequestState),
> --- `packages/voiden-runner/src/cliElectron.ts`

#### MEM-RTE-history-report
Label: Session history reporting

Endpoints: standalone session-mode run → appendSessionResults → results.json → later report/status/export command. Distinct from [RT-RTE-session-driver](runtime.md#rt-rte-session-driver): it spans that driver's history output and the separately invoked reporting consumers. Sources: SRC-1, `packages/voiden-runner/src/index.ts`, `packages/voiden-runner/src/session.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: initial run emits its summary; later report prints stored entries and aggregate duration/summary, while status reports counts.
- Later read-back: report and report generate call loadSessionResults; generate offers CSV/JSON/email delivery of accumulated results. These are concrete CLI consumers, not hypothetical storage API callers.
- Delegated visibility: terminal reader receives selected printed request/response details according to flags; export/report consumers can receive retained results. No automatic model-context delivery is shown.
- Selection predicate: all stored entries, with detail/report-format flags; no semantic relevance selection or per-project history filter in the inspected load call.
- Invalidation or expiry: report clear deletes results.json while preserving variables; session clear also deletes variables and env.json. Missing/malformed results load empty; future append can replace malformed history with only new entries.
- Activation or effect: retained history is used to render later output; interpretation, debugging benefit and future request changes are unobserved.
- Evidence limits: print/format internals and final mail execution were not independently audited; full history loading does not establish external model consumption or method learning.

Admission is automatic append when CLI session mode is enabled, not separate approval of each result. The user selects the workflow and report command; computation supplies result content and file I/O. No acceptance comparator or answer oracle governs history retention. Cleanup discards records rather than withdrawing the remote effects recorded by them. This route creates raw outcome history and presentation aggregates, not a retained explanatory theory.

> if (opts.session) {
>       appendSessionResults(allResults)
>     }
> --- `packages/voiden-runner/src/index.ts`

> const results = loadSessionResults()
>     if (results.length === 0) {
>       console.error(chalk.red('  ✗  No results found in session. Run some .void files first.'))
>       return
>     }
> --- `packages/voiden-runner/src/index.ts`

#### MEM-RTE-status-write
Label: Verification status write-back

Endpoints: CLI tool verify --write → discover/validate/verify provider calls → state/note dispatch → provider upsertToolStatus. Caller chooses paths, environment and optional cadence; provider owns results and storage semantics. Distinct from [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication): this CLI does not start serving or schedule refresh. Sources: SRC-1, `packages/voiden-runner/src/index.ts`, `packages/voiden-runner/src/mcpToolCapability.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: status/issue output and per-write errors; provider dispatcher throws if no capability provider exists.
- Later read-back: uninspected — the provider implementation that might read written status is unavailable; core CLI help says verification recomputes rather than trusting stale write-back.
- Delegated visibility: provider receives file path, tool block UID, state and optional note; terminal/JSON output can contain per-entry results, unlike the reduced upsert payload.
- Selection predicate: discovered tools from supplied paths; validTools from provider validation; optional cadence passed to verifyTools; --write admits each returned status without individual confirmation.
- Invalidation or expiry: uninspected — physical replacement, timestamping and later invalidation belong to provider code. Core catches individual write failures and continues.
- Activation or effect: provider call is wired; successful file persistence and downstream reliance are not established from the core interface.
- Evidence limits: no pinned verification plugin; no end-to-end expected-outcome oracle, storage representation or recovery can be reconstructed from these types.

Admission: operator selects --write globally; provider proposes computed state; CLI forwards it without per-tool human approval. Actual input authorship is unresolved. Provider validation can exclude tools; its verification can return failures, but truth of those decisions and rejection/rollback semantics are uninspected. Mode is an explicit one-shot verification run; cadence here is a selection tag, not a scheduler. This is a supported automatic summary-dispatch transformation with unresolved physical retention, not a reason to suppress the known dispatch or to assert an exercised learning route.

> if (opts.write) {
>       for (const status of statuses) {
>         try {
>           upsertToolStatus(status.tool.filePath, status.tool.toolBlockUid, { state: status.state, note: status.note })
> --- `packages/voiden-runner/src/index.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars)

Memory horizon depends on the caller. Direct inspection of SRC-1, `packages/voiden-runner/src/mcpSessions.ts` confirms mutable state keyed by client-supplied session ID, a one-hour default idle threshold swept every five minutes, explicit deletion on DELETE and loss on process exit. This is access/lifecycle metadata, not a derived knowledge object or authenticated user partition. `close` stops the timer; it does not itself clear the map. SelectedEnv stores resolved values for later requests, but returns only key names/counts to the caller in `packages/voiden-runner/src/mcpServing.ts`. A profile identifier is a lookup selector, not evidence of relevance-ranked selection.

> const DEFAULT_IDLE_TTL_MS = 60 * 60 * 1000
> const SWEEP_INTERVAL_MS = 5 * 60 * 1000
> --- `packages/voiden-runner/src/mcpSessions.ts`

Current-run variables are ordinary execution state until a later section/call consumes the changed map; durable cross-invocation state is the separately declared [MEM-OBJ-process-env](#mem-obj-process-env). Capture rows and plugin scripting can both write it, so origin cannot be reduced to response traces alone. No source truth filter follows from hiding selected-environment values in a tool return.

#### On [RT-RTE-result-write](runtime.md#rt-rte-result-write)

The retained content is [MEM-OBJ-response](#mem-obj-response), and the demonstrated later code reader is [MEM-RTE-response-reload](#mem-rte-response-reload). Caller-supplied content is software-serialized, not automatically fetched from the preceding run. Exact UID matching admits placement, not authenticity or claim validation. The fixed `list_requests` consumer selects label/UID/method/URL previews, not retained bodies. Source: direct SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/resultBlock.ts`.

Replacement is latest-record retention for the same UID in the bounded section, not an append-only execution history. No response-specific deletion tool was found among the six inspected fixed registrations; external document editing can remove content, with later readers seeing the changed file. This statement is bounded to those registrations, not a system-wide absence of deletion. The truncation limit is a storage/display budget, not a model-token budget. The immediate full result is not replaced or compacted in the host conversation by this write.

#### On [RT-RTE-session-driver](runtime.md#rt-rte-session-driver)

The driver's two retained outputs have different consumers: [MEM-OBJ-process-env](#mem-obj-process-env) affects later request substitution; [MEM-OBJ-session-results](#mem-obj-session-results) feeds reports. `--no-session` omits load/share/save across files, but a per-file map can still chain sections within that file. Source: direct SRC-1, `packages/voiden-runner/src/index.ts`, plus the capture path [MEM-RTE-runtime-capture](#mem-rte-runtime-capture). Nonempty-map-only saving means an empty final map does not by itself overwrite an old variable file; explicit clear is the dependable deletion path shown here.

#### On [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions)

The symbolic served/excluded/status fields and optional natural-language descriptionNote have different consumers. Core uses decision fields for counts and served-state comparison; registration delegates the full decisions to the external provider. DescriptionNote is a readable warning channel intended for an external model, not the opaque runResult itself. The provider's actual formatting/filtering and model interpretation remain uninspected. The separate cache part is [MEM-OBJ-verify-entry-cache](#mem-obj-verify-entry-cache). Source: direct SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts`, selected scheduler code in `packages/voiden-mcp/src/lib.ts`, and supplied [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication).

Core replanning can change what a subsequent HTTP request exposes; failure before decision assignment leaves the prior decision set, not a proved fail-closed withdrawal. Supervised stdio detection only compares currently non-excluded names with earlier values; addition/deletion/description-only updates are not fully covered. Restart discards core in-memory cache and variables without undoing request effects. Dynamic mode is passed to registration; the command flag describes search_tools/call_tool as reducing tool-list context, but the external provider's targeting predicate, result budget and delivery are unavailable. No stronger context-selection route is inferred from the flag.

#### On [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance)

Direct SRC-1, `apps/electron/src/main/skillsComposer.ts` and `apps/electron/src/main/skillsInstaller.ts` show a mixed delivery object split by consumption: natural-language base/extension guides, symbolic guide paths/index membership, and substituted application-version text. Guide origin is bundled, OTA cache or installed community extension; actual downloaded prose is not frozen. Compose reads every enabled readable guide, normalizes whitespace in index summaries and caps summaries at 240 characters while retaining each full guide separately. This is deterministic packaging, not trace-derived criticism.

> summary = summary.replace(/\s+/g, " ").trim();
>   if (summary.length > 240) summary = `${summary.slice(0, 237).trimEnd()}...`;
>   return { title, summary };
> --- `apps/electron/src/main/skillsComposer.ts`

Working-context control: setup/refresh writes a base guide plus pointers; the foreground agent, following prose, chooses a guide before authoring the corresponding block. The code does not evict old turns or injected instructions, fork an isolated task, or guarantee the base is the only content in the window. Full guides remain reachable on disk after the initial base read. This resembles demand loading, not a popped subtask frame: there is no isolated frame, automatic return boundary or token-liveness rule in the inspected route. Source-native policy is explicit:

> Before you write a block, open the guide that documents it and read it in full. Do not write a block from memory, from an example in another guide, or by copying an existing `.void` file in the project.
> --- `apps/electron/skills/base.skill.md`

Refresh removes the prior extension-guide folder first; missing guides are skipped, so withdrawal affects future file reads. An already loaded host copy is not withdrawn by filesystem deletion. Existing matching copies under ~/.agents/skills are synchronized, but none is newly created there; uninstall helpers remove primary Claude/Codex copies and do not show removal of those shared copies. Thus uninstall cannot establish universal instruction revocation. Silent catches and nontransactional writes also prevent an all-or-nothing refresh guarantee.

#### On [RT-RTE-host-registration](runtime.md#rt-rte-host-registration)

Launch configuration is symbolic access metadata consumed by the host; guide bodies are behavior-shaping prose only if the host loads and interprets them. Their horizons and refresh/removal differ. Operator setup and extension enablement do not establish per-paragraph approval of guide content. Direct SRC-1, `apps/electron/src/main/skillsInstaller.ts` additionally shows updateComposedSkillOnly does not install the separate MCP skill, whereas recomposeAndInstall does. This limits assumptions about which guide is present after a particular desktop action; it does not establish actual installation state.

#### On [RT-CMP-plugin-runner](runtime.md#rt-cmp-plugin-runner)

Persistent runner bytes are symbolic executable capability; plugins.json is separate symbolic access/version metadata. Direct SRC-1, `packages/voiden-runner/src/plugins/store.ts` shows uninstall retains a tombstone to distinguish explicitly unavailable from never-touched core defaults. It sets enabled false and uninstalled true, removes the recorded version, and later enable/install can reverse availability metadata. These store changes are not semantic curation of knowledge. Actual subsequent executable replacement remains bounded by the loading/module-cache limits in [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission). A disabled file can remain physically present without being selected on the next load; the tombstone is not erasure of its bytes or rollback of earlier effects.

## Write side

The write mechanisms have different admission controls. Starting a command is not human approval of every generated value. Unless stated, source inspection does not identify whether an external caller is a human or model.

| Mechanism | Proposed content, authorship and admission | Transformation, rejection and withdrawal |
| --- | --- | --- |
| write_result | Caller supplies result; code checks project argument/UID placement and serializes; no per-result confirmation or execution provenance binding. [RT-RTE-result-write](runtime.md#rt-rte-result-write) | Selected fields, timestamp, truncation, replace-or-insert. Missing UID rejects; concurrent edits can overwrite; external editing removes. [MEM-OBJ-response](#mem-obj-response) |
| Runtime capture and script writes | Authored rows select request/response values; software admits non-null extractions and enabled interpolations; plugin callbacks can write the map. Human control of initial configuration unresolved. | Typed extraction and substitution, not explanation synthesis. Stale values can survive a failed extraction; explicit clears discard persisted values. [MEM-RTE-runtime-capture](#mem-rte-runtime-capture) |
| CLI map save/history append | Session-mode option selects automatic software load/write; no per-key/result veto in driver. | JSON snapshot for variables, append history for outcomes. Malformed input fallback can discard prior history on later append. No prior-version rollback here. [MEM-OBJ-process-env](#mem-obj-process-env), [MEM-RTE-history-report](#mem-rte-history-report) |
| Environment selection | Caller selects profile/name; software resolves and replaces session env values, not individually approved secrets. | Session-local snapshot; later selection replaces it. Actual profile-file authorship and full resolver semantics remain untraced. [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars) |
| Guide refresh | Operator enables target/extensions; source authors provide prose; software selects/copies guides, with no per-paragraph approval. | Summary extraction and version substitution retain full separate bodies; missing guides skipped, old folder removed, shared copies conditionally refreshed. [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance) |
| Verification summary/cache | CLI --write forwards provider state/note; publisher passes persistent-in-process map to provider. Per-content provider admission and oracle unresolved. | Known reduction in upsert payload; actual cache curation/write-back format opaque. Failed planning may leave old served decisions. [MEM-RTE-status-write](#mem-rte-status-write), [MEM-OBJ-verify-entry-cache](#mem-obj-verify-entry-cache) |
| Plugin installation/enabling | Caller selects plugin/version; registry/download/load rules admit capability, not human inspection of bytes. | Persistent files/store plus registry rebuild; disable/uninstall metadata and reload limits differ from byte erasure. [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) |
| Request/guidance edits outside these handlers | External host/editor or extension author supplies changed material; no Voiden model-authorship or per-edit approval mechanism is established. | Later file reads can consume edits; actual authoring and review policies remain outside captured state. [RT-RTE-request-execution](runtime.md#rt-rte-request-execution), [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance) |

No compaction/checkpoint alternative is established by the inspected result/capture routes: the retained forms actually shown are a response snapshot, value map, history array and provider-defined summaries/cache. This is a limit of these routes, not a claim about external host compaction. Capture is the concrete automatic trace-to-later-action transformation; history alone is not. Provider verification may provide another such chain, but its origin, derivation and later use are only partly visible. Reasons are not silently inferred from labels such as success or verified.

## Read-back

The principal directional distinction is between an externally requested read and automatic carry-over. A caller requests a document execution; core pushes the selected section's blocks into callbacks. A configured capture automatically updates variables after a request; a later request template selects named values from that map. Standalone session mode automatically reloads all saved variables; report commands request all accumulated history. These mechanisms do not implement semantic retrieval of an agent's past reasoning. See [MEM-RTE-response-reload](#mem-rte-response-reload), [MEM-RTE-runtime-capture](#mem-rte-runtime-capture), [MEM-RTE-history-report](#mem-rte-history-report).

Selection budgets are also distinct: response storage has a 20,000-character string-body cap; preview listing excludes response bodies; guide index summaries have a 240-character cap but full files remain reachable. None is a token-window policy. Publisher dynamic mode advertises a smaller listing interface, but its provider's search inputs, result count limits and description admission cannot be inspected. The external host may independently retain full immediate tool results or read project documents; that host behavior is not supplied evidence. Sources: SRC-1, `packages/voiden-runner/src/resultBlock.ts`, `packages/voiden-runner/src/mcpServing.ts`, `apps/electron/src/main/skillsComposer.ts`, `packages/voiden-mcp/src/lib.ts`.

Later-consumer authority ranges from symbolic substitution into real requests to advisory prose interpreted by an external agent. Stored results do not acquire instruction authority merely because a model could read them. Provider descriptions can carry warnings, but core flags and model interpretation are separate. Session identifiers select access state rather than knowledge content. Outgoing MCP session/token reuse similarly enables connection/authentication, not a demonstrated route that learns from remote returns; the substantive remote memory boundary remains opaque in [RT-RTE-remote-mcp](runtime.md#rt-rte-remote-mcp).

## Integration issues

- **No correction to a supplied runtime record is required.** The response reload annotation narrows the supplied statement that documents are reread: parsed responses reach callback JSON, but list_requests returns only previews and fixed execution returns new outcomes. Retention must not be generalized to observed model reuse. Records: [RT-RTE-result-write](runtime.md#rt-rte-result-write), [MEM-RTE-response-reload](#mem-rte-response-reload). Evidence: SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/executors/src/voidParser.ts`, `packages/voiden-runner/src/runner.ts`.
- **Source comment contradicted by a shipped driver.** `packages/voiden-runner/src/runtimeVars.ts` says the map resets every run and stays purely in memory, but `packages/voiden-runner/src/index.ts` reloads/saves it in default session mode. Likewise an adapter comment says identity while executable preSendProcess substitutes variables. These are not runtime corrections: [RT-RTE-session-driver](runtime.md#rt-rte-session-driver) already identifies persistence. [MEM-OBJ-process-env](#mem-obj-process-env) and [MEM-RTE-runtime-capture](#mem-rte-runtime-capture) retain the executable account.
- **Record identity.** New contained parts explicitly name their parent. No possible replacement duplicate is identified: response/history/status objects are different retained outputs, and [MEM-RTE-history-report](#mem-rte-history-report) includes a later reporting invocation beyond the execution driver. [MEM-RTE-status-write](#mem-rte-status-write) is an explicit CLI route, not publication. Existing referents receive annotations instead of new IDs.
- **Opaque verification integration.** Cache mutation, per-entry reuse and invalidation, verification oracle, persistent status format, rationale retention and downstream status read-back cannot be established without the unavailable provider. Core scheduling and upsert dispatch are known and remain positive findings. Records: [MEM-OBJ-verify-entry-cache](#mem-obj-verify-entry-cache), [MEM-OBJ-tool-status-record](#mem-obj-tool-status-record), [MEM-RTE-status-write](#mem-rte-status-write), [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication). SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts`, `packages/voiden-mcp/src/lib.ts`, `packages/voiden-runner/src/index.ts`.
- **Context and revocation limits.** External guide loading, dynamic-mode targeting/budget, and removal of already loaded instructions are unresolved. Shared ~/.agents skill copies are refreshed conditionally, but not shown deleted by uninstall helpers; a universal withdrawal claim would therefore be false. Records: [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance), [RT-RTE-host-registration](runtime.md#rt-rte-host-registration), [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions). SRC-1, `apps/electron/src/main/skillsInstaller.ts`, `packages/voiden-mcp/src/lib.ts`.
- **Other bounded inspection limits.** Environment resolver internals, shared linked-expansion internals, export-format internals and external credential-store semantics were not fully traced here. These prevent universal acquisition, report fidelity and credential lifecycle claims, not the demonstrated named consumers. Relevant supplied routes: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution), [RT-RTE-remote-mcp](runtime.md#rt-rte-remote-mcp); report route: [MEM-RTE-history-report](#mem-rte-history-report).

## Limitations and checks

The report establishes source-visible storage, transformations, interface dispatch and later code consumers, not successful operation or causal benefit. There is no supplied host trace showing model reuse, no pinned plugin source establishing verification semantics and no live project state identifying actual retained values. Learning, reflective revision and self-improvement do not follow from persistence or plugin acquisition alone; this report makes no system-wide negative claims about those independent properties.

Identity was rechecked through repository HEAD, the supplied boundary and runtime identity fields, and the supplied job/type/records contracts. All added evidence is SRC-1 at the same commit, with no new source identity or execution evidence. Validation: the required validate-output check passed; this establishes deterministic form and quotation occurrence, not analytical acceptance.
