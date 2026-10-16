---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Tendril runtime baseline: desktop-to-agent invocation, capability admission, Deno execution and alternate workspace controls."
run-id: AAS-2026-10-15-tendril-f560fb299a37-01
reviewed-boundary: "e671a4143d28de68289efd81580002041bb4cb6a"
---

# Tendril runtime report

## Runtime account

### Evidence and claimed work

Tendril accepts desktop chat requests and gives a model three bootstrap tools: list retained capabilities, register TypeScript capabilities and execute a capability by name. Its shipped instruction asks for tool construction rather than unsupported answers. The model chooses the work; the Strands SDK owns iteration; Tendril supplies persistence, subprocess execution and desktop presentation. This account uses implementation and doctrine/design from SRC-1 at the frozen revision in [boundary](boundary.md). No execution trace or experiment was supplied; wiring is not evidence of successful use or benefit.

> return `You are Tendril. You build tools.
> --- `tendril-agent/src/loop/prompt.ts`

> tools: [
>       listCapabilities(registry),
>       registerCapability(registry),
>       executeCode(registry, workspacePath, config),
>     ],
> --- `tendril-agent/src/agent.ts`

Added detailed implementation coverage within SRC-1 comprises the complete stream observer, React agent context, file editor, Rust configuration/event/capability readers, shell permission manifest and React agent hook. Agent construction, configuration, entry point, protocol, registry, prompt, sandbox, host lifecycle, workspace initialization and App were also read completely. Package metadata was inspected; Makefile packaging was searched for Deno version and bundling. Source text only was inspected. Dependency implementations and live provider behavior remain outside the frozen evidence.

### Ordinary shipped invocation

The user selects or initializes a workspace in the React application. Rust creates `tools/` and an empty index if necessary and persists the workspace in the application configuration. App loads configuration and credentials and requests sidecar connection. Rust resolves a Deno executable, injects `DENO_PATH` and available provider credentials, launches `tendril-agent`, sends `initialize`, then `new_session`. The initialization waiter times out after ten seconds but does not abort the subsequent session message. The Node entry point reads configuration once, writes a display copy of its prompt and constructs one agent and one shared registry. The actual model instruction comes from the shipped function, not a later read of `system-prompt.txt` (SRC-1, `tendril-ui/src/App.tsx`, `tendril-ui/src-tauri/src/workspace.rs`, `tendril-ui/src-tauri/src/acp.rs`, `tendril-agent/src/index.ts`, `tendril-agent/src/agent.ts`).

A chat submission runs [RT-RTE-prompt-stream](#rt-rte-prompt-stream). The React hook records the user message and invokes Rust; Rust writes JSON-RPC to sidecar stdin. The Node protocol acknowledges receipt before work finishes, serializes prompt requests and dispatches cancellation separately. `new_session` allocates a UUID, but the desktop sends `sessionId: "current"`; the callback ignores that parameter. A new protocol session does not itself construct a new agent. Thus session labels are not an inspected isolation boundary. Only the last submitted message's string or first usable text block reaches `agent.stream`; the desktop transcript is not replayed by this adapter (SRC-1, `tendril-ui/src/hooks/useAgent.ts`, `tendril-ui/src-tauri/src/acp.rs`, `tendril-agent/src/transport/protocol.ts`, `tendril-agent/src/index.ts`).

The model receives the natural-language system prompt, user text and SDK-managed conversation/tool context. It chooses tool calls or text. Listing returns all metadata summaries, not tool bodies; trigger/suppression interpretation is model judgment, not a fixed matcher. Registration is [RT-RTE-capability-admission](#rt-rte-capability-admission); execution is [RT-RTE-capability-execution](#rt-rte-capability-execution). Provider adapters are symbolic integration components around the distributed-parametric alternatives declared below. SDK-internal history retention, compaction and model-native tool behavior are uninspected. Tendril's inspected constructor sets no context-trimming, sub-agent or host-compaction mechanism; do not infer an SDK-level absence (SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`).

SDK events become streamed text, tool-call announcements, tool outputs and usage notifications. Rust routes these to typed Tauri events; React appends them to in-memory messages. The stream observer labels tool results `completed` without inspecting success semantics; it ignores duplicate `afterToolCallEvent` and unknown events. Usage assignment retains the latest metadata object rather than explicitly summing model calls. At turn end the entry point emits cost/usage and `prompt_complete` with `end_turn`, including after its exception handler emits an error. These are presentation/completion signals, not answer-validity oracles (SRC-1, `tendril-agent/src/transport/stream.ts`, `tendril-agent/src/index.ts`, `tendril-ui/src-tauri/src/events.rs`, `tendril-ui/src/context/AgentContext.tsx`).

> status: 'completed',
>     rawOutput: typeof rawOutput === 'string' ? rawOutput : JSON.stringify(rawOutput),
> --- `tendril-agent/src/transport/stream.ts`

### Guarantees, grants and forcing cases

The nominal capability surface is open-ended TypeScript using Deno APIs, fetch and imported packages. The actual grant set is workspace read/write plus network access, optionally domain-limited. No run, environment or FFI permission flag is passed. The deployed envelope depends on the resolved Deno binary, operating system and dependency contracts, none experimentally checked. Desktop/Node host operations are not inside the generated-code Deno boundary (SRC-1, `tendril-agent/src/loop/sandbox.ts`, `tendril-ui/src-tauri/src/acp.rs`).

| Load-bearing proposition | Owner, enforcement and strength | Coverage, counter-route and external contract | Separate conclusions |
|---|---|---|---|
| Every action lists first and creates only when needed | Model; shipped prompt and tool descriptions; policy | No callback checks sequencing or semantic match. Direct selection of `execute` or replacement registration remains possible. SDK must deliver instruction; model compliance is not proven. See [RT-CLM-action-sequence](#rt-clm-action-sequence). | implementation conclusion status: wired; operation conclusion status: uninspected |
| Execution accepts a name, not inline code | Tendril callback schema and `registry.load`; invariant at this API, conditional on SDK schema handling | Covers `execute` callback. It proves filename-based loading, not prior index admission: a valid-named source file need not appear in the index. The host/editor and previously executed code can supply it. See [RT-RTE-capability-execution](#rt-rte-capability-execution). | implementation conclusion status: wired; operation conclusion status: uninspected |
| Generated code is permission-restricted | Tendril constructs Deno flags; Deno enforces; deployment guarantee conditional on Deno | Workspace includes the registry itself; default network is unrestricted. Host commands and Node callbacks have separate authority. Remote imports add unfrozen behavior. No actual deployment/attack result supplied. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Execution is bounded and cancelable | Tendril subprocess timeout, output counter, kill and abort listener; best effort | Each execution subprocess has configured timeout and combined stdout/stderr cap. Does not bound all SDK/model work or reverse completed external effects; OS/process and SDK cancellation contracts required. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Workspace checks cover desktop file access | Rust canonicalizes targets for generic file commands; invariant at the inspected validation point, not an app-wide guarantee | Existing files and new-file parents are checked. `read_tool_source` accepts a workspace argument without calling this validator; its safe-name check alone does not constrain the workspace. The browser's intended workspace argument is not backend enforcement. Filesystem races were not experimentally assessed. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence for the last distinction (SRC-1, `tendril-ui/src-tauri/src/workspace.rs`, `tendril-ui/src-tauri/src/files.rs`, `tendril-ui/src-tauri/src/capabilities.rs`):

> if !target_canonical.starts_with(&workspace_canonical) {
>         return Err("Access denied: path is outside workspace".to_string());
>     }
> --- `tendril-ui/src-tauri/src/workspace.rs`

> let expanded = expand_tilde(&workspace);
>     let tool_path = Path::new(&expanded)
>         .join("tools")
>         .join(format!("{name}.ts"));
>
>     tokio::fs::read_to_string(&tool_path).await.map_err(|e| {
> --- `tendril-ui/src-tauri/src/capabilities.rs`

Four source-forced cases delimit the ordinary account; these are inspected branches, not executed tests:

1. **Source file without index membership.** `load(name)` validates syntax and reads `tools/{name}.ts`; it never consults the index. This falsifies the stronger interpretation of “only registered tools can run.” An index entry without its source conversely lists but fails execution (SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`).
2. **Capability code changes the capability store.** Deno can write throughout the workspace, including `tools/`. Such writes bypass `registerCapability` metadata construction, name validation and replacement bookkeeping. This is a second capability-admission mechanism, not shell access or permission escape; see [RT-RTE-workspace-mutation](#rt-rte-workspace-mutation) (SRC-1, `tendril-agent/src/loop/sandbox.ts`).
3. **Human editor replaces the same source.** The shipped editor confirms an overwrite then invokes generic Rust file writing. It can change TypeScript or index content independently of model registration. Confirmation covers this UI action only, not model writes or arbitrary command callers (SRC-1, `tendril-ui/src/components/FileExplorer.tsx`, `tendril-ui/src-tauri/src/files.rs`).
4. **Cancel, timeout or sidecar crash.** Cancellation calls `agent.cancel`; Deno execution listens to an SDK-provided abort signal. A timeout or output overflow kills the subprocess but cannot undo writes/network calls already made. Sidecar termination clears process state and requests reconnect until three rapid crashes in thirty seconds stop retries. React triggers reconnect; a manual restart resets the tracker. No pending-prompt replay or conversation restoration is implemented in these inspected lifecycle paths; retained files survive, but in-memory agent state is rebuilt (SRC-1, `tendril-agent/src/index.ts`, `tendril-agent/src/loop/sandbox.ts`, `tendril-ui/src-tauri/src/acp.rs`, `tendril-ui/src/context/AgentContext.tsx`).

The direct stdin protocol path uses the same callbacks but bypasses the desktop view. No provider-native tool, remote worker, manual graph-control or durable agent variant is wired by the inspected constructor/entry/protocol files; SDK-internal alternatives remain uninspected. Tauri permits spawning/writing to the named sidecar, while Rust itself also spawns file/browser reveal helpers. These host subprocesses are not capabilities exposed to the model (SRC-1, `tendril-ui/src-tauri/capabilities/default.json`, `tendril-ui/src-tauri/src/files.rs`). Searches for `maxTurns` and `maxCapabilities` in `tendril-agent/src` found only configuration declarations; the inspected constructor and registry do not consume them. Therefore the configured defaults of 100 and 500 are not established enforcement bounds (SRC-1, `tendril-agent/src/config.ts`, `tendril-agent/src/agent.ts`, `tendril-agent/src/loop/registry.ts`).

### Change and recovery boundary

Capability source/metadata admission is model-authored and automatically written by Node. The prompt asks for code repair after failure but no test, approval, oracle, semantic validation or versioned rollback gates these writes. Same-name registration replaces the definition and source; the index is saved before the code, so a failure between writes can leave inconsistent state. Corrupt index reads degrade to empty with a warning, potentially hiding capabilities rather than repairing their source. These are concrete bounded admission/recovery findings, not evidence that repair is ineffective in practice (SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/prompt.ts`).

Human settings changes use a separate route, [RT-RTE-settings-restart](#rt-rte-settings-restart), to change provider, timeout and network configuration then restart the agent. The application configuration is outside the default workspace and thus outside the generated-code file grant under the intended layout. Workspace nesting can change that relationship; it is not an independent secret-isolation guarantee. Packaging searches show a Deno 2.7.12 download target, but runtime resolution can fall back to PATH and `DENO_PATH` overrides configuration. The installed binary/version and live grant settings are not supplied (SRC-1, `Makefile`, `tendril-agent/src/config.ts`, `tendril-ui/src-tauri/src/acp.rs`, `tendril-ui/src-tauri/src/config.rs`). Memory content and later revision assessment are left to the memory member; no learning or self-improvement benefit is inferred here.

## Shared records

### Components

#### RT-CMP-bedrock-model
Label: BedrockModel

Source-native provider adapter consumes configured model ID/region and optional AWS profile. Adapter configuration is symbolic, held in Node memory; the remote model is distributed-parametric, stored by the provider outside this repository. Tendril supplies no operational weight-update API. Whether provider parameters change internally is uninspected; the exact deployed weights are not pinned by the Git revision or a model-ID string. The remote endpoint may resolve to another implementation; immutability is not established. Evidence: SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/config.ts`.

> model: new BedrockModel({
>           modelId: bc.modelId,
>           region: bc.region,
>         }),
> --- `tendril-agent/src/agent.ts`

#### RT-CMP-openai-model
Label: OpenAIModel

OpenAI branch uses a symbolic SDK adapter in Node and remote distributed-parametric inference. API key is supplied through the host environment; weights/storage are external. No Tendril weight mutation is wired. Provider-side mutation is uninspected, exact weights are not pinned, and a mutable service/model identifier can resolve differently across invocations. Evidence: SRC-1, `tendril-agent/src/agent.ts`.

> model: new OpenAIModel({
>           api: 'chat',
>           modelId: oac.modelId,
>         }),
> --- `tendril-agent/src/agent.ts`

#### RT-CMP-anthropic-model
Label: AnthropicModel

Anthropic branch is a symbolic Node adapter around externally stored distributed-parametric weights. No parameter update is requested by Tendril; provider-internal changes are uninspected. Configuration supplies a model ID rather than a frozen weight artifact, so exact version is not established and mutable endpoint resolution remains possible. Evidence: SRC-1, `tendril-agent/src/agent.ts`.

> model: new AnthropicModel({
>           modelId: ac.modelId,
>         }),
> --- `tendril-agent/src/agent.ts`

#### RT-CMP-ollama-model
Label: Ollama OpenAIModel

Ollama uses the same SDK class as the OpenAI branch but a distinct configurable host with an OpenAI-compatible URL. Its symbolic Node configuration selects a distributed-parametric model whose storage belongs to the endpoint operator, not this checkout. Tendril wires no weight updates; endpoint changes during operation are uninspected. Neither exact weights nor endpoint-to-model mapping is immutable, and the operator can change what the configured host/model resolves to. Evidence: SRC-1, `tendril-agent/src/agent.ts`.

> apiKey: 'ollama', // Ollama ignores auth; dummy value satisfies SDK validation
>           clientConfig: { baseURL: `${oc.host.replace(/\/$/, '')}/v1` },
> --- `tendril-agent/src/agent.ts`

### Operative objects

#### RT-OBJ-system-prompt
Label: TENDRIL_SYSTEM_PROMPT

Natural-language instructions generated from a shipped TypeScript template and workspace path, supplied directly to the agent in process memory. A UTF-8 `system-prompt.txt` copy is written for display. Editing that copy does not replace the constructor's instruction. The text asks for listing, semantic matching, new code when needed and repair after failure; see [RT-BAP-prompt-guidance](#rt-bap-prompt-guidance). Evidence: SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/loop/prompt.ts`.

> systemPrompt: TENDRIL_SYSTEM_PROMPT(workspacePath),
> --- `tendril-agent/src/agent.ts`

### Routes

#### RT-RTE-prompt-stream
Label: Desktop prompt stream

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON-RPC acknowledgement precedes work; later updates stream text/tool events and completion to the desktop.
- Later read-back: inapplicable — this route does not persist or replay the desktop transcript; retained capability consumption is separately traced below.
- Delegated visibility: provider/SDK receive the generated instruction and extracted user text; SDK tool results feed its loop. SDK-managed history and exact remote serialization are uninspected.
- Selection predicate: protocol method `prompt`, nonempty extracted last-message text; one active prompt allowed per process. Model selects next actions under natural-language guidance.
- Invalidation or expiry: turn ends on stream completion/error; process restart rebuilds the agent. Protocol session changes alone do not replace it.
- Activation or effect: `agent.stream(userText)` invokes model/tool iteration; event adapters update in-memory desktop messages. Actual run activation is unobserved.
- Evidence limits: no traces; SDK-internal context control, provider behavior and outcomes uninspected.

Endpoints and owner: human desktop principal → React hook → Rust stdin writer → Node protocol → shared Strands Agent → model/tool loop → Rust event router → React reducer. Request IDs, protocol UUID and tool-use IDs provide transport/display correlation, not demonstrated multi-agent coordination. The model decides work; the SDK owns next-step execution; symbolic adapters transform events without evaluating answers. Operating mode is open user requests, not a bounded curriculum; no answer oracle is supplied here. Evidence: SRC-1, `tendril-ui/src/hooks/useAgent.ts`, `tendril-ui/src-tauri/src/acp.rs`, `tendril-agent/src/index.ts`, `tendril-agent/src/transport/protocol.ts`, `tendril-agent/src/transport/stream.ts`, `tendril-ui/src-tauri/src/events.rs`, `tendril-ui/src/context/AgentContext.tsx`.

> for await (const event of agent.stream(userText)) {
> --- `tendril-agent/src/index.ts`

> if (promptInFlight) {
>             emitError(req.id, -32000, 'Prompt already in progress');
>             return;
>           }
> --- `tendril-agent/src/transport/protocol.ts`

#### RT-RTE-capability-admission
Label: Model capability registration

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registration success string after metadata and source writes, or a thrown error.
- Later read-back: list reloads index summaries and execute reloads the named source from disk on later calls, including after restart.
- Delegated visibility: metadata summaries reach the foreground model; source reaches Deno through the execution callback. No separate critic or worker is constructed.
- Selection predicate: model judges available summaries against user need; callback accepts a definition and code, validates name syntax, and replaces by exact name or appends.
- Invalidation or expiry: same-name write replaces current source/definition; no expiry. Corrupt/missing index becomes empty. No automatic previous-version rollback in this implementation.
- Activation or effect: callback changes disk state immediately; subsequent listing/execution can consume it. Effective behavior change in a real run is unobserved.
- Evidence limits: no corpus or execution results; string/schema validation is not TypeScript checking, test success or behavioral approval.

Admission: model proposes code and natural-language metadata; Node performs physical I/O and syntactic name validation. A human supplies the task but does not approve each generated capability. No answer oracle, candidate experiment or semantic veto is wired in this callback. Trigger is a model tool call, guided by the shipped instruction to create missing capabilities and repair failures. It persists source plus an index entry with model attribution, date and fixed version. Rejection is schema/name/I/O failure, not outcome-based selection. Index and source writes are sequential, not transactional. Recovery is a later replacement or external/manual edit, not restoration of a retained previous version. Evidence: SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/prompt.ts`.

> await this.saveIndex(index);
>
>     await fs.writeFile(path.join(this.toolsPath, `${definition.name}.ts`), code);
> --- `tendril-agent/src/loop/registry.ts`

> - On failure: fix the code and retry. Do not fall back to memory.
> --- `tendril-agent/src/loop/prompt.ts`

This route establishes program admission, not a formulated-theory criticism loop. Generated contents are not supplied, so their theoretical content and any content-directed criticism remain uninspected rather than absent. No theory-builder or improvement classification is inferred from the act of registration.

#### RT-RTE-capability-execution
Label: Named capability execution

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: trimmed subprocess stdout or `(no output)` on zero exit; stderr/exit, timeout, output-limit, spawn or cancellation errors otherwise.
- Later read-back: source is reloaded from `tools/{name}.ts` for each invocation; separate registry metadata is not checked by this loading path.
- Delegated visibility: Deno receives JSON-serialized arguments and workspace binding plus loaded source. Remote resources receive only what that code sends; exact content is uninspected.
- Selection predicate: model-supplied safe name and optional JSON args string; successful file read, not index membership, permits execution.
- Invalidation or expiry: source replacement affects the next load; temp script removed in finally on a best-effort basis. Timeout and cancellation kill the current process, not prior effects.
- Activation or effect: Deno executes TypeScript with workspace read/write and configured network permission; arbitrary results/effects depend on code. Actual execution is unobserved.
- Evidence limits: Deno and imported package internals are outside source; no deployment/test execution supplied; no guarantee of undoing effects or valid answers.

Owner and control: model requests; Node loads code, parses args and spawns Deno; Deno enforces permissions. The prelude and script are symbolic code on a random OS-temp filename. Default timeout is 45 seconds and combined stdout/stderr cap is 1 MiB. Empty allowedDomains means unrestricted network, not no network. No shell execution grant is passed. Open-ended request execution has no reference-answer oracle and no per-run human approval. Evidence: SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts`, `tendril-agent/src/config.ts`.

> async load(name: string): Promise<string> {
>     this.validateName(name);
>     const filePath = path.join(this.toolsPath, `${name}.ts`);
>     return fs.readFile(filePath, 'utf-8');
>   }
> --- `tendril-agent/src/loop/registry.ts`

> const netFlag = allowedDomains.length > 0
>         ? `--allow-net=${allowedDomains.join(',')}`
>         : '--allow-net';
> --- `tendril-agent/src/loop/sandbox.ts`

> const proc = spawn(denoPath, [
>         'run',
>         `--allow-read=${workspacePath}`,
>         `--allow-write=${workspacePath}`,
>         netFlag,
>         '--no-prompt',
>         '--quiet',
>         tmpFile,
>       ]);
> --- `tendril-agent/src/loop/sandbox.ts`

#### RT-RTE-workspace-mutation
Label: Alternate workspace mutation

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: capability code returns through its subprocess result; editor writes return command success/error.
- Later read-back: a changed tool file can be loaded by execute; changed index content can be listed independently. No automatic reconciliation couples these parts.
- Delegated visibility: capability implementation has workspace file authority; human editor can view and replace source/index; later consumers receive the changed material through their normal paths.
- Selection predicate: generated program chooses paths within its grant; human chooses a file and edited content. Generic file backend checks workspace containment, not capability semantics.
- Invalidation or expiry: overwrite supersedes bytes; no per-file revision store or automatic rollback in these inspected mechanisms.
- Activation or effect: filesystem write can change later executable code or model-visible selection metadata, bypassing register's definition construction; no supplied run demonstrates this exercise.
- Evidence limits: capacity follows from workspace write grant and shipped editor, not a witnessed adversarial update or demonstrated improvement.

This container groups two separately assessed admission mechanisms: [RT-RTE-program-mutation](#rt-rte-program-mutation) is afforded by the generated program's grant; [RT-RTE-editor-mutation](#rt-rte-editor-mutation) is a wired human decision/veto route. The container's afforded status denotes their shared write-side bypass capacity, not a uniform implementation status or approval policy for its parts. Two distinct admission owners share the same writable substrate: a model-authored program can write registry files under its existing grant, while the human editor explicitly supplies and confirms changed content. The UI confirmation can reject an editor overwrite; it is not present in generated-code execution or the generic backend command. Guided proposal for generated code comes from the task/prompt; editor rationale is unspecified. Neither mechanism supplies an answer oracle or semantic test gate. Recovery requires another write; this account does not establish versioned rollback. Evidence: SRC-1, `tendril-agent/src/loop/sandbox.ts`, `tendril-ui/src/components/FileExplorer.tsx`, `tendril-ui/src-tauri/src/files.rs`, and loading behavior in [RT-RTE-capability-execution](#rt-rte-capability-execution).

> if (!window.confirm(`Save changes to ${selectedFile.name}?`)) return;
>     const content = editorContentRef.current;
>     setSaving(true);
>     try {
>       await invoke('write_file_content', { filePath: selectedFile.path, content });
> --- `tendril-ui/src/components/FileExplorer.tsx`

#### RT-RTE-program-mutation
Label: Generated program workspace mutation

Part of: [RT-RTE-workspace-mutation](#rt-rte-workspace-mutation)

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: file-write results remain within the executing program unless it emits them; subprocess stdout/errors return through [RT-RTE-capability-execution](#rt-rte-capability-execution), not a dedicated mutation acknowledgement.
- Later read-back: changed `tools/{name}.ts` bytes can reach later execute calls; changed index content can reach later listings independently. No automatic reconciliation of the files is supplied by this grant.
- Delegated visibility: Deno receives loaded code, arguments and the workspace binding; subsequent model listing and Deno loading expose only what their respective readers consume.
- Selection predicate: executing program chooses paths and content within its workspace write grant; no registry membership or per-write approval is required by the sandbox launcher.
- Invalidation or expiry: another write can replace bytes; timeout/cancellation terminates the process without reversing prior writes. No versioned rollback or expiry is supplied by this mechanism.
- Activation or effect: the grant permits executable-source and index mutation bypassing registration's definition construction, name check and replacement bookkeeping; no actual generated write is evidenced.
- Evidence limits: source demonstrates permission capacity, not a supplied mutating program, execution trace, successful update or improved behavior; Deno enforcement remains an external contract.

Endpoints and owner: model-authored capability → executing Deno program → workspace files → later registry readers. The model can propose executable content under the task and shipped prompt; the program decides individual writes, and Deno supplies permission enforcement. This is an open-request operating mode, not an experiment/curriculum. Admission is the already-granted workspace write authority, not a second Node registration or human decision. Deno/path/I/O failures can reject writes; there is no per-content semantic veto or answer oracle in the launcher. Recovery is another write or manual edit; the launcher does not retain old file versions. What persists is whichever source/index/workspace bytes the program writes. Generated contents and their rationale are not supplied, so no formulated-theory criticism or improvement conclusion follows. Evidence: SRC-1, `tendril-agent/src/loop/sandbox.ts`; grant passage in [RT-RTE-capability-execution](#rt-rte-capability-execution). This part is distinct from the human-confirmed editor route by executor, decision owner and checks, while sharing the container's writable substrate.

#### RT-RTE-editor-mutation
Label: Human workspace editor mutation

Part of: [RT-RTE-workspace-mutation](#rt-rte-workspace-mutation)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rust write command returns success/error; on success the editor updates its selected-file content and clears dirty state, otherwise it displays an error.
- Later read-back: saved source/index bytes can reach subsequent execute/list calls; reopening a file uses the generic file reader. The save handler does not automatically synchronize registry parts.
- Delegated visibility: human sees selected file text; Rust receives the selected path and edited content. Later registry consumers receive the relevant saved parts, not an editor rationale or approval record.
- Selection predicate: human selects a file, edits content and confirms Save; Rust checks workspace containment for the existing target or new-file parent and then writes bytes.
- Invalidation or expiry: overwrite replaces saved content; no expiry or retained previous-version rollback is implemented in the inspected save/backend path.
- Activation or effect: confirmed content is written by the backend, potentially replacing tool source or index independently of registration. Actual saving and downstream behavioral activation are unobserved.
- Evidence limits: UI confirmation is a wired veto on this editor action only; the generic backend command does not itself require confirmation and the generated-program route does not traverse it. No deployment trace, semantic validity or benefit is established.

Endpoints and owner: human editor selection/change → `handleSave` confirmation → Tauri `write_file_content` → workspace filesystem → later readers. The human proposes the particular bytes and can veto this overwrite by declining confirmation. Rust performs physical I/O and rejects path/I/O failures, not semantically bad capabilities. The trigger is an explicit save action under human-directed maintenance, not an automatic model repair or bounded experiment. Guidance/rationale shaping the human edit is unspecified; saved bytes persist, not a required rationale. No answer oracle or semantic test gate is supplied. Recovery requires another edit/write; neither this handler nor backend provides version restoration. Evidence: SRC-1, `tendril-ui/src/components/FileExplorer.tsx`, `tendril-ui/src-tauri/src/files.rs`; confirmation passage in [RT-RTE-workspace-mutation](#rt-rte-workspace-mutation). Distinct from program mutation by its human content decision, explicit veto and path-checked backend, this part does not extend those checks to the container's other path.

> if tokio::fs::try_exists(path).await.unwrap_or(false) {
>         validate_within_workspace(path).await?;
>     } else if let Some(parent) = path.parent() {
>         validate_within_workspace(parent).await?;
>     }
>
>     tokio::fs::write(path, content)
>         .await
>         .map_err(|e| e.to_string())
> --- `tendril-ui/src-tauri/src/files.rs`

#### RT-RTE-settings-restart
Label: Human settings restart

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: write_config and restart command success/error; App catches errors and attempts config reread.
- Later read-back: sidecar startup reloads `~/.tendril/config.json`; generated agent is constructed from parsed settings, so provider and execution controls can change after restart.
- Delegated visibility: Rust and Node receive configuration; selected provider receives its adapter settings and host-injected credential environment. UI display is not model context.
- Selection predicate: user-selected settings merged by App, lightweight Rust validation before persistence, Zod validation at sidecar startup; DENO_PATH overrides configured binary.
- Invalidation or expiry: latest saved config replaces earlier bytes; restart discards old process state. Manual restart resets crash tracker; no automatic config rollback after startup failure.
- Activation or effect: new process constructs provider/agent and sandbox settings; actual activation after a particular user change is unobserved.
- Evidence limits: no supplied config or deployment; validation differs across Rust and Node; declared maxTurns/maxCapabilities are not shown to control runtime loops.

Human proposes/selects configuration in the shipped settings flow; software admits schema-valid values, writes JSON and restarts. There is no model-driven production-code deployment in this route and no task-answer oracle. Validation can veto malformed input but is not a quality comparison. Recovery after invalid startup is a corrective edit/restart rather than transactional restoration. Evidence: SRC-1, `tendril-ui/src/App.tsx`, `tendril-ui/src-tauri/src/config.rs`, `tendril-ui/src-tauri/src/acp.rs`, `tendril-agent/src/config.ts`, `tendril-agent/src/agent.ts`.

> await invoke('write_config', { config: merged });
>       setConfig(merged);
>       const envVars = await getAgentEnvVars(merged.model?.provider ?? 'bedrock');
>       await invoke('restart_agent', { envVars: envVars.length > 0 ? envVars : null });
> --- `tendril-ui/src/App.tsx`

### Claims

#### RT-CLM-action-sequence
Label: List create execute policy

The source claims every action lists first, executes a match, or creates then executes. This is natural-language guidance delivered to the model, not a callback state machine. Callback schemas restrict input shapes but do not enforce semantic matching or ordering. Evidence: SRC-1, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/agent.ts`; forcing routes above bound the claim.

> 1. listCapabilities() — always list first. Read the results.
> 2. Match found? → execute(name, args)
> 3. No match? → registerCapability(definition, code) then execute(name, args)
> --- `tendril-agent/src/loop/prompt.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: System prompt guidance

Consumer: configured model through Strands Agent. Channel: natural-language systemPrompt generated at agent construction. Force: instruction/policy, not an execution gate; it requests reuse, construction and repair while the actual tool callbacks retain separate symbolic powers. Horizon: agent lifetime, reconstructed from shipped template after restart. Display-copy edits do not change this consumer. Evidence: SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/loop/prompt.ts`, [RT-OBJ-system-prompt](#rt-obj-system-prompt), [RT-CLM-action-sequence](#rt-clm-action-sequence).

#### RT-BAP-capability-source
Label: Capability source execution

Consumer: Deno subprocess. Channel: source bytes loaded by name, appended to argument/workspace prelude and written to temporary script. Force: executable symbolic content under the subprocess permission grant; replacement bytes can determine later program behavior without changing model weights or tool callback definitions. Horizon: retained file across sessions until overwritten; no expiry enforced. This establishes an operative behavioral-authority path, not actual reuse, correct code or improved outcomes. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts`, [RT-RTE-capability-execution](#rt-rte-capability-execution), [RT-RTE-workspace-mutation](#rt-rte-workspace-mutation).

## Annotations

none
