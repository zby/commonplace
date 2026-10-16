---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Voiden runtime baseline: agent-facing MCP request execution, plugin admission and request-backed publishing at the frozen subsystem boundary."
run-id: AAS-2026-10-14-voiden-98188b4a2f55-01
reviewed-boundary: d7a0d05c40acb6cc483000643c700f17aecba0ef
---

# Voiden runtime report

## Runtime account

### Responsibility and evidence

Voiden supplies tools to an external agent, not the enclosing inference loop. The consequential work is executing project-defined network requests, returning their results, optionally recording them, and publishing selected request-backed tools. An external MCP host owns problem interpretation, tool choice, any approval UI, response interpretation and the next conversational step. Within this subsystem, ordinary execution decisions are symbolic TypeScript rules and plugin callbacks. No distributed-parametric component is invoked directly by the inspected core paths; the external host's model identity, weight changes, endpoint mutability and context policy remain outside the frozen boundary, not properties of Voiden. See [boundary](boundary.md#boundary-and-evidence), SRC-1, `apps/electron/src/voiden-cli.ts`, `packages/voiden-runner/src/mcpServing.ts` and `packages/voiden-mcp/src/lib.ts`.

All findings below use SRC-1 at the reviewed commit. Added implementation coverage includes shared orchestration, the CLI adapter, block-version classification, outgoing MCP execution, HTTP session storage, plugin path/store selection, publisher supervision/scheduling and OAuth's default authorization behavior. Added instruction-delivery coverage includes composition and installation of enabled-extension guides. These are implementation or doctrine/design evidence, never observed runs. No target, test, example or service was executed. Operation, activation in a model host and benefit remain unobserved.

### Ordinary invocation: an agent runs a project request

The operator runs `voiden agent [path]`, or uses the desktop Initialize MCP action. Registration points the host at `voiden mcp-stdio <absolute-project-path>`. The desktop action checks CLI availability in packaged builds, writes host registration and refreshes composed guidance; its disable action removes the project Claude registration, not the global Codex configuration. The runner's separate `mcp install` explicitly registers the installed runner version, or a supplied local server. Host launch/discovery is an external contract, not proved by a successful config write ([RT-RTE-host-registration](#rt-rte-host-registration); SRC-1, `apps/electron/src/main/ipc/mcp.ts`, `packages/voiden-runner/src/index.ts`, `packages/executors/src/mcpInstall.ts`).

On bundled stdio startup, Voiden loads enabled plugin factories into shared registries, allocates a process-local `runtimeVars` map and `selectedEnv`, registers six fixed tools plus three plugin-management tools, and connects the MCP stdio transport. Older comments saying it exposes only six tools do not describe the current registration call sites. This surface does not register `/tool` publications (SRC-1, `apps/electron/src/voiden-cli.ts`).

An external agent can discover files, list request sections, list environments and select a profile. Discovery is not execution. Selection persists actual resolved variables in this server's session but returns only keys/counts; it is independent of the desktop's selected environment. `run_request` resolves the requested file lexically under the project root, layers selected variables, an optional env file and explicit overrides, then calls `runVoidFile`. The fixed handler does not pass the publisher's base environment to this call. The external host chooses the file, label and overrides; code chooses the resulting section set. A supplied label filters only multi-section files: a single-section file executes its sole request even for a stale label (SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/runner.ts`).

`runVoidFile` rereads the document on every call, parses it, resolves linked files then linked blocks, groups sections, normalizes schemas and constructs a headless editor object. It passes explicit environment and runtime-map references to plugin hooks. Registered request builders progressively construct a request; a missing URL produces an actionable failure. The section version gate runs before shared orchestration. The pipeline runs preprocessing, compilation and pre-send hooks; hooks can mutate request data or cancel sending. The CLI adapter substitutes variables and invokes shared network execution. HTTP uses fetch; protocol-specific branches and response hooks can own other exchanges. The runner maps the response into `RunResult`, captures configured request/response values into shared runtime variables for subsequent sections/calls, and returns section results. Per-section exceptions become failed results and execution continues; initial file/parse failures can escape to the MCP boundary. The fixed MCP handler returns full JSON and sets `isError` when a section explicitly reports failure ([RT-RTE-request-execution](#rt-rte-request-execution); SRC-1, `packages/voiden-runner/src/runner.ts`, `packages/executors/src/orchestrator.ts`, `packages/executors/src/pipeline/executor.ts`, `packages/voiden-runner/src/cliElectron.ts`).

This loop ends at a tool return, not a task-completion decision. The external agent decides whether to edit a request, rerun, or call `write_result`. That separate call accepts caller-supplied result fields, finds a matching block UID, inserts/replaces a response within the section and writes the document. It neither obtains the previous run from an authenticated result store nor proves that the supplied result actually happened. The response body is truncated at 20,000 characters in retained output, unlike the full immediate MCP result. Retention semantics and later use are left to the memory member; this report establishes the physical admission mechanism ([RT-RTE-result-write](#rt-rte-result-write); SRC-1, `packages/voiden-runner/src/resultBlock.ts`).

### Alternate routes and forcing cases

1. **A project path guard is not a filesystem sandbox.** Fixed `filePath` and `envFile` arguments have a lexical root check. Linked content uses `join(projectRoot, filePath)` without that check, and binary/multipart input supports genuinely absolute files. Symlink targets are not canonicalized by the fixed guard. Therefore its narrow owner/enforcement point cannot promise that request execution reads only project files. Loaded plugins are imported into the Node process and can register executors/hooks; the context API is not an isolation boundary. Actual OS permissions, credentials, hosts and installed plugin identities are uncaptured. See [RT-CLM-project-confinement](#rt-clm-project-confinement), [RT-CMP-plugin-runner](#rt-cmp-plugin-runner).

2. **Version gating is compatibility checking, not exact replay.** `checkBlockVersions` skips blocks lacking either tag, inspects the passed block list, and rejects missing/disabled/incompatible installations before executing each section. The classifier accepts newer versions within its caret-like compatibility range. Thus the runner comment promising the exact authored plugin version is stronger than the executable rule. Nor does the gate authenticate downloaded bytes, validate network outcomes or cover arbitrary plugin-internal calls. The general desktop path is not assigned the runner's gate. See [RT-CLM-version-gating](#rt-clm-version-gating).

3. **Publishing admission does not gate generic execution.** `voiden-runner mcp serve` serves six fixed tools plus plugin-planned tools; its decisions are computed once, even over HTTP. Its HTTP path creates a server per request but uses the same startup decisions. The separate `voiden-mcp` publisher registers only planned tools, with optional static/dynamic mode, periodic planning and restart supervision. Neither its planning nor its bearer middleware guards the bundled fixed `run_request` endpoint, CLI `run`, arbitrary loaded plugin code, or an external host's other tools. The unavailable `/tool` plugin owns discovery, validation, verification and binding semantics. The core cannot establish an end-to-end verified-tools-only invariant from the provider interface. See [RT-RTE-tool-publication](#rt-rte-tool-publication), [RT-CLM-publisher-access](#rt-clm-publisher-access).

4. **A request can itself be an MCP client.** Shared execution has an outgoing MCP branch, including tool calls, prompt/resource reads and discovery. It substitutes arguments, connects to the remote server, executes one operation and closes. Session IDs are reused by URL and authorization header; an unknown reused session triggers one fresh attempt. An RPC returning a tool-level `isError` still counts as successful transport/RPC execution. The outer runner success flag is consequently not an oracle that the remote tool accomplished its intended task. This route can reach remote capabilities without traversing local `/tool` publication admission. Remote implementation and any model/provider-native calls behind it are opaque. See [RT-RTE-remote-mcp](#rt-rte-remote-mcp).

These four cases were selected from source, not run as experiments. They challenge the breadth of isolation, reproducibility, verification and success claims. Full protocol correctness, malicious-plugin behavior, cross-platform packaged launches, deployed host confirmation rules and live network behavior remain unobserved.

### Change admission, coordination and recovery

Plugin-management tools are an explicit capability-changing channel on the bundled stdio surface, not part of every fixed-tool server. The caller chooses install/version or update scope; registry membership/version availability and download/load outcomes govern software admission. Core installation writes release assets into the user plugin cache and enables them. Reload clears shared registries and mutates the `activePlugins` array held by fixed-tool closures. There is no per-install human confirmation inside these handlers; whether a human approved the call is external. Downloads and imports occur with the server process's authority. Catching failures and reporting `active: false` is not transactional rollback. In particular the stable file import URL supplies no source-visible cache-busting mechanism: reloading registration does not establish that an updated module's bytes replace a module already imported by Node. Immediate adoption of an already-loaded plugin update remains unestablished, despite the tool description ([RT-RTE-plugin-admission](#rt-rte-plugin-admission); SRC-1, `packages/voiden-runner/src/plugins/managementTools.ts`, `packages/voiden-runner/src/plugins/loader.ts`, `packages/voiden-runner/src/plugins/registry.ts`).

Publishing's HTTP path uses new server/transport objects per request and mutable current decisions, so a later request receives the latest successful plan. A failed planning tick logs a warning rather than withdrawing all tools. The scheduler delegates per-entry cadence/cache interpretation to the provider. In supervised stdio, detected served-state changes cause exit 3 and restart, requiring client reconnection; unsupervised stdio stays startup-only. The comparison iterates currently non-excluded tools and requires an earlier state: it is not a complete detector of additions, deletions or description-only changes. The supervisor retries crashes after one second with a ten-per-minute window limit, does not retry clean/configuration exits and handles exit 3 separately. Restart loses process-local variables/cache; it does not undo completed remote effects (SRC-1, `packages/voiden-mcp/src/lib.ts`).

HTTP session state uses a client-echoed `mcp-session-id`, random when absent, with deletion and idle sweeping. It separates maps by session identifier, not authenticated identity; a client supplying the same ID selects the same map. There is no inspected locking/serialization across concurrent mutations of shared maps, global plugin registries or response documents. These are coordination limits, not evidence of a live collision (SRC-1, `packages/voiden-runner/src/mcpSessions.ts`, `packages/voiden-runner/src/plugins/loader.ts`, `packages/voiden-runner/src/resultBlock.ts`).

Auth and grants depend on the entry point. Runner HTTP has a loopback default and a warning on broader binds, not the publisher's optional bearer gate. Publisher HTTP without auth flags is open; with flags it gates the MCP handler but leaves health open. Local OAuth auto-approves authorization rather than identifying a user; SSO is a separately configured external identity contract. Even a bearer-gated endpoint does not supply per-tool or per-install approval. Capability exposure is source-visible; actual enabled plugins, credentials and deployed process/network isolation are not captured ([RT-CLM-publisher-access](#rt-clm-publisher-access)).

Instruction changes also matter. Enabled extension guides are copied into separate files and indexed in a base skill. Missing guides are skipped; refresh clears old guide files. This makes detailed guidance reachable on demand, but the host or foreground agent decides what to load and obey. It does not remove turns, summarize a conversation or isolate a model subtask. There is no source-visible model-window control in this composition route beyond packaging base/index versus optional guide reads. Broader host context controls are uninspected. Product edits to request documents, made through a host's editor/shell, are not admitted by a Voiden editing tool; Voiden subsequently rereads them ([RT-RTE-host-registration](#rt-rte-host-registration), [RT-BAP-agent-guidance](#rt-bap-agent-guidance)).

A durable alternate driver is standalone `voiden-runner run`: in session mode it loads saved runtime variables, shares them across files and writes them back after execution; `--no-session` instead uses fresh per-file maps and omits persistence. This differs materially from bundled `voiden run` and stdio MCP's process-local map, but is not a model-learning implementation ([RT-RTE-session-driver](#rt-rte-session-driver)).

## Shared records

### Components

#### RT-CMP-request-orchestrator
Label: RequestOrchestrator

Source-native shared singleton in SRC-1, `packages/executors/src/orchestrator.ts`. Representational form: symbolic TypeScript, with ordered builder and response callback arrays in process memory; source stored in Git. The executor consumes document JSON, passes a progressively built request between registered handlers, checks a URL exists, runs the pipeline and invokes response handlers. Response-handler exceptions are swallowed, so their intended effects are not guaranteed merely by a successful request.

> for (const handler of this.requestHandlers) {
>       request = await handler(request, editor)
>     }
> --- `packages/executors/src/orchestrator.ts`

#### RT-CMP-plugin-runner
Label: Plugin runner factories

Identity: runner modules selected by core/community registries and imported by the headless loader. Form: symbolic executable JavaScript with opaque external plugin internals, not model parameters. Storage: bundled files or `~/.voiden/extensions/<id>/runner.js`, enabled/version metadata in `~/.voiden/plugins.json`, callbacks in shared in-process registries. User cache takes priority over bundled core assets. Core plugins fall back to app-disabled state when no explicit runner record exists; community plugins require enabled installed records and catalogue recognition. Actual deployed set and release bytes are unavailable. Evidence: SRC-1, `packages/voiden-runner/src/plugins/loader.ts`, `packages/voiden-runner/src/plugins/registry.ts`, `packages/voiden-runner/src/plugins/store.ts`, `packages/voiden-runner/src/headlessContext.ts`.

> const mod = await import(pluginPath)
> --- `packages/voiden-runner/src/plugins/loader.ts`

> const ctx = createHeadlessPluginContext(pluginName, verbose)
>     await factory(ctx).onload()
> --- `packages/voiden-runner/src/plugins/loader.ts`

These imports are executable authority in the server process; the exposed context provides hooks, protocol executors and runner primitives, not a sandbox. No claim is made about the behavior of unavailable plugin implementations.

### Operative objects

#### RT-OBJ-runtime-vars
Label: runtimeVars and selectedEnv

Source-native symbolic key/value maps. Substrate: memory in bundled/runner stdio; maps keyed by HTTP session IDs for HTTP; standalone CLI can additionally serialize runtime variables to user-level JSON. `selectedEnv` resolves a profile into variables, then per-call overrides layer above it. Response captures and scripting callbacks can mutate runtime variables, which later sections/calls consume. These are execution-state objects, not evidence that an external model revised its method. Evidence: SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/runner.ts`, `packages/voiden-runner/src/mcpSessions.ts`, `packages/voiden-runner/src/index.ts`.

> ;(editor as any).__cliVars = runtimeVars   // shared reference — mutations propagate
> --- `packages/voiden-runner/src/runner.ts`

#### RT-OBJ-serve-decisions
Label: ServeDecision and verification entry cache

Symbolic tool/served/excluded/status/description structures plus an in-memory map of verification-entry records. Storage: publisher process memory. The publisher passes the map into planning and reuses current decisions for HTTP registration; the unavailable provider owns interpretation, verification and registration. This object is not proof of the truth of a `verified` status. Evidence: SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts`, `packages/voiden-mcp/src/lib.ts`.

> const entryCache: VerifyEntryCache = new Map()
>   let decisions = await planServedTools(projectRoot, baseEnv, activePlugins, { entryCache, now: Date.now() })
> --- `packages/voiden-mcp/src/lib.ts`

### Routes

#### RT-RTE-request-execution
Label: Fixed-tool request execution

Endpoints: external MCP caller → fixed `run_request` → `runVoidFile` → plugin builders/hooks → shared executor/remote endpoint → JSON result. Trigger/principal: tool invocation by host caller under server process authority. Owner of next step: code through the awaited pipeline, then external host. Decision representation: symbolic parsing, filtering, compatibility rules and registered callbacks; no runtime model decision inside this core route. Context comprises document/linked blocks, explicit variables, schemas and callbacks. State includes mutable runtime variables and selected environment. Effects include real network calls and plugin-defined effects. Evidence: SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/runner.ts`, `packages/executors/src/orchestrator.ts`, `packages/voiden-runner/src/cliElectron.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON section results and active plugins; explicit section failures set MCP isError.
- Later read-back: files are reread each invocation; values captured into runtimeVars can influence later sections/calls. Durable CLI variant is separate below.
- Delegated visibility: builders/hooks receive editor JSON; CLI hooks receive environment and map references; the external caller receives result bodies, status, headers and errors.
- Selection predicate: requested file; exact label matching only for multiple sections; enabled loaded plugins and their registered request-container definitions.
- Invalidation or expiry: document reread on each call; session variables last until replacement/session expiry/process exit; fixed stdio environment selection is session-local.
- Activation or effect: network dispatch and runtime captures are wired; actual network effects and subsequent model behavior are unobserved.
- Evidence limits: external protocol builders, scripting/auth/assertion internals and live endpoints are not frozen. Host approval and task-completion interpretation are external.

Recovery: per-section failures are converted to results and later sections continue. Missing files can throw before section handling. No core automatic request retry or transaction rollback is established for this route. Operating mode: open interactive requests, including potentially mutating APIs. Answer oracle: none supplied by the fixed handler; HTTP status rules are outcome classification, not a reference answer to the agent's task. Provider assertions could add checks but their implementation is unavailable.

> const result = await runVoidFile(resolved, { env, runtimeVars, sectionLabel, activePlugins, projectRoot })
> --- `packages/voiden-runner/src/mcpServing.ts`

> const sections    = (options.sectionLabel && allSections.length > 1)
>     ? allSections.filter(s => s.label === options.sectionLabel)
>     : allSections
> --- `packages/voiden-runner/src/runner.ts`

#### RT-RTE-result-write
Label: Caller-supplied response admission

Endpoints: MCP caller's `result`, file and UID → `upsertResponseBlock` → document write. Owner: caller proposes content, software finds placement and serializes it. Human authorship/approval of each result is unresolved; the handler requires no separate confirmation. This is a result-admission mechanism, not automatic capture from the previous execution. Evidence: SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/resultBlock.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: written true, supplied file path and UID if the write completes.
- Later read-back: the changed document is available to subsequent file readers, including runVoidFile; exact retained-content consumption belongs to the memory analysis.
- Delegated visibility: caller supplies the entire result record; filesystem readers receive serialized response attributes, with body truncation when required.
- Selection predicate: lexical project path check at MCP entry; first matching block UID, and prior matching response within the same separator-bounded section.
- Invalidation or expiry: matching prior response is replaced; concurrent file saves can overwrite it; no expiry is imposed here.
- Activation or effect: direct file write is implemented; truth of the recorded outcome and later decision influence are not established.
- Evidence limits: no provenance binding to an earlier run, content approval or lock; a syntactically accepted result can be caller-invented.

Admission/rejection: missing UID throws; caller object shape is broad (`z.record(z.any())`) and cast as RunResult. Code controls serialization, not factual admission. Recovery/rollback: no transactional or versioned rollback here; a later caller may replace content, while filesystem/Git recovery is external. Operating mode: optional interactive write after a run according to guidance. Answer oracle: none at admission. Guidance says never hand-author response blocks, but this is policy rather than enforced authenticity.

> upsertResponseBlock(resolved, requestUid, result as RunResult)
> --- `packages/voiden-runner/src/mcpServing.ts`

> const requestFence = fences.find(f => f.uid === requestUid)
> --- `packages/voiden-runner/src/resultBlock.ts`

> writeFileSync(filePath, newContent, 'utf-8')
> --- `packages/voiden-runner/src/resultBlock.ts`

#### RT-RTE-plugin-admission
Label: Agent-callable plugin admission

Endpoints: bundled stdio MCP install/update → registry lookup/release download → persistent runner/store → reload callbacks. Trigger: caller sees missing/incompatible plugin or available update. Caller proposes name/version or update set; software admits known registry entries with obtainable runner assets, enables and loads them. External registry maintainers determine offered successors. No internal model comparator, benchmark curriculum or answer oracle is shown. Guidance requests listing before installation/update; improvement trigger is capability availability/version mismatch, not demonstrated performance gain. Evidence: SRC-1, `apps/electron/src/voiden-cli.ts`, `packages/voiden-runner/src/plugins/managementTools.ts`, `packages/voiden-runner/src/plugins/loader.ts`, `packages/voiden-runner/src/plugins/registry.ts`, `packages/voiden-runner/src/plugins/store.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: installed/updated/failed records plus active state after reload; installed true and active false can coexist.
- Later read-back: cached runner files and installed/enabled metadata are consumed on later loads, including later processes.
- Delegated visibility: registry/release services receive asset requests; plugin factory receives the context; existing fixed handlers retain the mutated activePlugins array.
- Selection predicate: core registry first, community catalogue otherwise; optional exact release version; updates only from update-check candidates.
- Invalidation or expiry: cache files/version metadata can be overwritten; disabled/uninstalled state prevents selected later loading; registry arrays are cleared/rebuilt on reload.
- Activation or effect: executable callbacks are registered on successful loading; replacement of already imported bytes is not established by stable-URL reimport.
- Evidence limits: release bytes and registry versions are external; no exercised update, security isolation, performance gain or successful recovery is observed.

Rejection ability: unknown plugin/missing asset/download/load failure; a human veto exists only if the external host supplies one. The core downloader follows redirects and writes directly to the destination; no checksum/adversarial-byte verification or atomic rollback is established by this implementation. Failure catches report errors but do not restore old files/metadata. A pinned reinstall can request another version, not prove safe reversal of effects. Module caching is a separate limitation: the loader imports the same URL selected from a stable file path. Scope: three management tools are registered on bundled `mcp-stdio`, not the standalone runner's fixed-tool call sites or publisher.

> const fresh = await loadEnabledPlugins()
>   activePlugins.length = 0
>   activePlugins.push(...fresh)
> --- `packages/voiden-runner/src/plugins/managementTools.ts`

> if (isValidRunnerFile(getCoreRunnerPath(pluginId))) return pathToFileURL(getCoreRunnerPath(pluginId)).href
> --- `packages/voiden-runner/src/plugins/registry.ts`

#### RT-RTE-tool-publication
Label: Request-backed tool publication and refresh

Endpoints: runner serve or publisher startup → provider planning → served-tool registration → MCP caller; publisher scheduler → new decisions/restart. Principal: operator starts server; remote/local callers subsequently invoke exposed tools under its process authority. Owner: core controls transport/scheduling, provider controls discovery, validation, verification, registration, parameters and request binding. Decision representation: symbolic provider interface; underlying provider semantics are unavailable. Evidence: SRC-1, `packages/voiden-runner/src/index.ts`, `packages/voiden-runner/src/mcpToolCapability.ts`, `packages/voiden-mcp/src/lib.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: server tool lists/call results; --check prints decisions and exits failure for excluded/failing entries without starting a server.
- Later read-back: publisher reuses an in-process entry cache across planning ticks; restart reconstructs decisions from project/provider state. Persistent provider status writes are delegated, not established end to end here.
- Delegated visibility: provider receives project root, base environment, active plugins and cache; registered handlers receive per-session runtime maps and mode; callers receive provider-produced descriptions/results.
- Selection predicate: provider plan's served/excluded decisions; actual eligibility/verification predicates are uninspected in external plugin implementation.
- Invalidation or expiry: publisher HTTP uses later successful decisions on each request; runner serve is startup-only; supervised publisher stdio restarts for detected existing-tool served-state changes; unsupervised stdio stays stale until manual restart.
- Activation or effect: tool registration and refresh dispatch are wired; remote invocation and enforcement of provider annotations are unobserved.
- Evidence limits: missing provider returns no planned tools; core validation with no provider returns supplied tools as valid. This does not establish a fail-closed universal validation API or a verified-only execution invariant.

Admission conditions: operator supplies project/tools/environment; provider proposes/decides served set. Structural exclusion/status are protocol fields, not independently established checks. Human review of each tool is not required by the inspected core. Answer oracle: provider may execute declared verification cases, but expected values, coverage and interpretation are unavailable; labels are not oracles. Operating mode: serving with startup and optionally periodic checks, not a bounded improvement experiment. Rejection/recovery: excluded/withdrawn decisions, diagnostic output, warning on scheduler failure, crash supervision and reconnection; prior successful decision state can remain after failure. No rollback of network effects.

> if (!provider) return []
>   return provider.planServedTools(projectRoot, env, activePlugins, opts)
> --- `packages/voiden-runner/src/mcpToolCapability.ts`

> if (!provider) return { validTools: tools, issues: [] }
> --- `packages/voiden-runner/src/mcpToolCapability.ts`

> decisions = await planServedTools(projectRoot, baseEnv, activePlugins, { entryCache, now: Date.now() })
>           lastVerifiedAt = new Date()
> --- `packages/voiden-mcp/src/lib.ts`

#### RT-RTE-host-registration
Label: Host registration and guide installation

Endpoints: CLI agent/mcp install or desktop initialization/skill refresh → host config and skill files → external host/agent. Owner: operator initiates registration or skill enablement; code writes supplied command/configuration and copies/composes guides; external host controls launch, loading and obedience. Source inputs are symbolic launch settings and natural-language guidance, consumed separately. Evidence: SRC-1, `apps/electron/src/voiden-cli.ts`, `packages/executors/src/mcpInstall.ts`, `packages/executors/src/skillContent.ts`, `packages/voiden-runner/src/index.ts`, `apps/electron/src/main/ipc/mcp.ts`, `apps/electron/src/main/skillsComposer.ts`, `apps/electron/src/main/skillsInstaller.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: installation/status or desktop success/error; success of file writes is not host discovery.
- Later read-back: host launch config and home-directory skills persist across sessions; external host loading is required and unobserved.
- Delegated visibility: Claude receives project .mcp.json; Codex receives user config.toml; skill folders receive base guidance/index and enabled-extension guides.
- Selection predicate: selected host targets; desktop enabled extensions with readable guides; foreground agent/host selects guides at consumption.
- Invalidation or expiry: reinstallation replaces generated material; composed refresh removes old extension-guide directory; uninstall removes selected registrations/skills with project/global asymmetries.
- Activation or effect: configuration and instruction delivery are wired; host launch, instruction obedience and improved request quality are unobserved.
- Evidence limits: external host schema/skill discovery and actual installation paths are not runtime traces; extension guide content may come from uncaptured downloaded plugins.

Change admission: operator chooses target/project; code replaces this named registration and generated skill content without per-paragraph approval. Extension authors supply guide prose; composition skips missing guides and truncates index summaries to 240 characters but retains guide files separately. Rejection/recovery: packaged desktop initialization checks CLI presence, errors can be reported, unregister/uninstall is provided; composed skill writing catches errors silently and offers no transactional rollback. This is shipping/refreshing instructions, not software-generated criticism or theory revision. Operating mode: setup/refresh, with no answer oracle.

> const serverCommand: ServerCommand = { command: 'voiden', args: ['mcp-stdio', projectPath] }
> --- `apps/electron/src/voiden-cli.ts`

> const enabled = appState.extensions.filter((e) => e.enabled);
> --- `apps/electron/src/main/skillsComposer.ts`

> fs.rmSync(path.join(skillDir, EXTENSION_GUIDES_DIR), { recursive: true, force: true });
> --- `apps/electron/src/main/skillsInstaller.ts`

#### RT-RTE-remote-mcp
Label: Outgoing request-backed MCP operation

Endpoints: parsed MCP request state → shared secure executor → SDK StreamableHTTP client → remote tool/resource/prompt → response. Owner: request/plugin selects operation and arguments; code substitutes variables, uses explicit authorization or stored valid tokens, connects, dispatches and closes; remote server owns substantive effects. Source: SRC-1, `packages/executors/src/secureRequest.ts`, `packages/executors/src/mcp.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: successful RPC payload or structured connection/error/auth-required result; remote isError remains inside the payload.
- Later read-back: process-local session ID map is reused by URL and authorization header; stored OAuth credentials can be consumed from an earlier authorization flow, whose plugin implementation is unavailable.
- Delegated visibility: remote server receives resolved arguments/headers and owns remote effects; caller receives serialized operation/result or error.
- Selection predicate: request protocolType mcp, then operation enum, tool/resource/prompt name and authored arguments.
- Invalidation or expiry: close client per call; unknown reused session code 404 deletes cached ID and retries once; process exit clears map; valid-token store applies external credential lifetime.
- Activation or effect: actual remote invocation is wired but not observed; task-level outcome cannot be inferred from success true.
- Evidence limits: remote tool semantics, any nested model inference, provider-native tools and remote isolation are not frozen. Timeout races bound awaiting, not proof that remote work stops.

Per-operation await timeout is 15 seconds. A 401 returns an authorization-required signal and best-effort discovered login URL, rather than automatically opening a browser. This is a remote capability-consumption route, not local tool-publication approval or a theory-admission mechanism.

> return { success: true, result, durationMs: Date.now() - start }
> --- `packages/executors/src/mcp.ts`

#### RT-RTE-session-driver
Label: Standalone durable execution driver

Endpoints: standalone run command → optional persisted runtime-variable load → runVoidFile across files → saved variables/results. Owner: operator selects session mode and file list; code executes serial files and persists. Decision representation: symbolic command options and capture expressions. Evidence: SRC-1, `packages/voiden-runner/src/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI summary/JSON and exit status; stop-on-failure can omit later files.
- Later read-back: session mode reloads .process.env.json under the user store before execution and writes nonempty updated runtimeVars after the run.
- Delegated visibility: plugins/requests receive these variables; network endpoints can receive substituted values; no model host is required.
- Selection predicate: session option controls reload/share/save; no-session allocates a fresh map per file.
- Invalidation or expiry: stored map can be replaced/cleared through session management; malformed persisted JSON is ignored; no automatic TTL appears in this driver.
- Activation or effect: a retained value can affect a later substituted request; actual recurrent use is unobserved.
- Evidence limits: no trace-fed methodological revision, capacity improvement or cross-session model learning follows from variable persistence alone; detailed retention belongs to the memory member.

Recovery: file execution exceptions become failed results; variable-save errors are caught, with diagnostics only when verbose. This driver does not enforce the fixed MCP file-root check and is not covered by publisher authentication.

> const fileVars = opts.session ? runtimeVars : {}
> --- `packages/voiden-runner/src/index.ts`

### Claims

#### RT-CLM-project-confinement
Label: Narrow project-path refusal

Claimed operation: fixed tools refuse paths resolving outside the project. Owner/enforcement: `resolveInProject` in the fixed MCP registration module. Guarantee strength: invariant for the lexical argument check only; not a deployment guarantee or transitive filesystem sandbox. Covered paths: fixed tool primary document and optional env file. Alternate paths: linked-file resolver uses join without this guard, binary reads allow absolute files, symlinks are not resolved to physical targets, CLI and arbitrary plugin code do not inherit the fixed guard. Required external contract: trusted project content/plugins and OS access controls if broader isolation is desired. Evidence: SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/runner.ts`, `packages/voiden-runner/src/cliElectron.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (rel.startsWith('..') || isAbsolute(rel)) {
>     throw new Error(`"${filePath}" resolves outside the project root (${projectRoot})`)
>   }
> --- `packages/voiden-runner/src/mcpServing.ts`

> return join(projectRoot, filePath)
> --- `packages/voiden-runner/src/runner.ts`

#### RT-CLM-version-gating
Label: Tagged-block compatibility gate

Claimed operation: runner comments promise exact authored-version execution. Actual owner/enforcement: checkBlockVersions plus classifyBlockVersion before each section reaches the orchestrator. Guarantee strength: invariant of this checked compatibility predicate, not exact byte/version replay. Covered paths: sections executed by runVoidFile; blocks without both tags bypass the check. Compatible newer semver versions pass. Arbitrary plugin-owned or remote calls are not independently checked here. Required external contracts: accurate installed metadata and plugin adherence to compatibility assumptions. The guarantee does not authenticate bytes or freeze registry/release/network state. Evidence: SRC-1, `packages/voiden-runner/src/runner.ts`, `packages/executors/src/blockVersioning.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!pluginId || !pluginVersion) continue
> --- `packages/voiden-runner/src/runner.ts`

> if (cmp < 0) return 'too-old'
>   if (!sameCompatibilityRange(installed, declared)) return 'incompatible-newer'
>   return undefined
> --- `packages/executors/src/blockVersioning.ts`

#### RT-CLM-publisher-access
Label: Optional publisher bearer gate

Claimed operation: publisher HTTP can require bearer credentials when API-key/OAuth modes are enabled. Owner: publisher middleware before MCP dispatch, dependent on SDK verifier behavior and configured provider. Guarantee strength: protocol, not an unconditional identity or per-action approval guarantee. Covered path: this publisher's gated HTTP MCP handler. Health remains open; default unflagged HTTP, runner HTTP, bundled stdio and CLI execution do not pass this gate. Local OAuth auto-approves; SSO can delegate identity to an external IdP but its deployed behavior is unobserved. Credentials accepted by the combined verifier give access to the exposed surface, not separately approved actions. Source: SRC-1, `packages/voiden-mcp/src/lib.ts`, `packages/voiden-mcp/src/oauthProvider.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> app.use((req, res, next) => { bearerAuth(req, res, next) }, handleMcpRequest)
> --- `packages/voiden-mcp/src/lib.ts`

> res.status(200).type('html').send(renderAutoApprovePage(client.client_name ?? client.client_id, redirectUrl.toString()))
> --- `packages/voiden-mcp/src/oauthProvider.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-guidance
Label: Installed MCP and authoring guidance

Consumer: external model host/foreground agent. Channel: installed natural-language SKILL.md and separately indexed enabled-extension guides. Force: policy/request interpreted by the host/model, not enforced by the result or environment handlers. Horizon: files persist across sessions until overwritten/uninstalled; actual loading and compliance unobserved. The standalone guide requests discover → execute → inspect → optionally record, asks the user to disambiguate multiple environments, forbids speculative response blocks and warns about write collisions. This can shape proposals without becoming per-content approval. Distinct executable channels remain separate: host config is symbolic process-launch input; guide text is not code enforcement. Evidence: SRC-1, `packages/executors/src/skillContent.ts`, `apps/electron/src/main/skillsComposer.ts`, `apps/electron/src/main/skillsInstaller.ts`.

> A request block that merely looks well-formed can still be wrong (bad URL, wrong auth, malformed body). Don't stop at "this looks right" when you can check that it *is* right.
> --- `packages/executors/src/skillContent.ts`

No formulated-theory criticism/revision route is established by this packaging and delivery mechanism. Instructions are inspectable prose, but delivery alone does not show content-dependent model decisions, criticism or iterative method revision.

## Annotations

none
