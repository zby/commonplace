---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Tendril memory: retained capability selection text, executable source, alternate workspace writes and non-durable conversation displays."
run-id: AAS-2026-10-15-tendril-f560fb299a37-01
source-identity: "https://github.com/serverless-dna/tendril"
reviewed-boundary: "e671a4143d28de68289efd81580002041bb4cb6a"
---

# Tendril memory report

## Boundary and evidence

The memory boundary includes capability registration, the on-disk index and TypeScript files, their model and Deno consumers, human browsing/editing, workspace initialization, transient execution artifacts and working conversation/display state. It follows the whole-system boundary in [boundary](boundary.md), not merely the registry class. Configuration restart is included as a retained runtime-control surface through [RT-RTE-settings-restart](runtime.md#rt-rte-settings-restart), not treated as experience-derived memory. Developer skills and specification scaffolding remain excluded as in boundary; they do not establish product memory behavior.

All source evidence is SRC-1 at e671a4143d28de68289efd81580002041bb4cb6a. Direct reads added here cover complete `tendril-agent/src/{agent,index,types}.ts`, `tendril-agent/src/loop/{registry,tools,prompt,sandbox}.ts`, `tendril-agent/tests/registry.test.ts`, `tendril-ui/src/hooks/{useCapabilities,useAgent}.ts`, `tendril-ui/src/components/{CapabilityBrowser,FileExplorer}.tsx`, `tendril-ui/src/context/AgentContext.tsx`, and `tendril-ui/src-tauri/src/{capabilities,workspace,files}.rs`. These provide implementation evidence; prompt text also provides doctrine/design. Source searches inventoried `tendril-agent/src`, desktop source and test names for persistence, deletion, hooks, history, compaction and checkpoint paths. No target, test or example was executed. Host process recovery, configuration and transport details not reread here rely on the cited supplied runtime records.

| Operation or included part | Source path in SRC-1 | Coverage and limit |
|---|---|---|
| Initialize or preserve an existing workspace index | `tendril-ui/src-tauri/src/workspace.rs` | Direct read; [MEM-OBJ-index-metadata](#mem-obj-index-metadata). Existing corpus authorship remains unknown. |
| Bootstrap tool dispatch and model registration | `tendril-agent/src/agent.ts`, `tendril-agent/src/loop/tools.ts` | Direct reads corroborate [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission); annotation adds admission/lineage limits. |
| Index selection text versus access metadata | `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/types.ts` | Direct reads; [MEM-OBJ-selection-text](#mem-obj-selection-text), [MEM-OBJ-index-metadata](#mem-obj-index-metadata), [MEM-RTE-capability-list](#mem-rte-capability-list). |
| Named executable reload and subprocess cleanup | `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts` | Direct reads; [MEM-OBJ-tool-source](#mem-obj-tool-source); supplied [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) annotated. |
| Generated program changes registry or other workspace files | `tendril-agent/src/loop/sandbox.ts` | Grant inspected directly; [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation) annotated. Arbitrary generated program contents and non-registry payload formats unavailable; prevents enumeration of actual application-memory schemas. |
| Capability browser and cached source display | `tendril-ui/src/hooks/useCapabilities.ts`, `tendril-ui/src/components/CapabilityBrowser.tsx`, `tendril-ui/src-tauri/src/capabilities.rs` | Direct reads; [MEM-RTE-capability-browser](#mem-rte-capability-browser). Human inspection, not model context injection. |
| File read/edit and overwrite confirmation | `tendril-ui/src/components/FileExplorer.tsx`, `tendril-ui/src-tauri/src/files.rs` | Direct reads; [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation) annotation. Backend path checks are not semantic approval. |
| Instruction generation and display copy | `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/agent.ts`, `tendril-ui/src-tauri/src/capabilities.rs` | Direct reads; [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) annotated. Static shipped instruction, not experience-derived read-back. |
| Conversation, tool results, debug display and turn extraction | `tendril-agent/src/index.ts`, `tendril-ui/src/context/AgentContext.tsx`, `tendril-ui/src/hooks/useAgent.ts` | Direct reads; [MEM-OBJ-agent-display](#mem-obj-agent-display), [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream) annotation. SDK history/compaction internals outside frozen source. |
| Settings, credentials and restart | `tendril-agent/src/config.ts`, `tendril-ui/src-tauri/src/config.rs`, `tendril-ui/src-tauri/src/acp.rs` | Supplied runtime coverage, not fresh full reads; [RT-RTE-settings-restart](runtime.md#rt-rte-settings-restart). No claim about credential-vault security or actual deployment settings. |
| Evaluators, repair and withdrawal | `tendril-agent/tests/registry.test.ts`, `tendril-agent/src/loop/{prompt,registry,tools,sandbox}.ts` | Registry tests read directly; other test names searched. Registration/replacement assertions are test source, not observed success or a runtime evaluator. Withdrawal and cleanup limits traced below. |
| Provider parameters and SDK-owned working state | `tendril-agent/src/agent.ts` | Constructor read directly; provider identities remain supplied runtime components. No frozen dependency implementation or accumulated workspace; prevents conclusions about SDK checkpoint alternatives or actual trace-derived learning. |

## Core ideas

1. Retention has two different consumers. Natural-language capability descriptions guide the model's choice; TypeScript source determines Deno behavior. The index is not the execution whitelist. A valid-named file can execute without an index entry, and an index entry can advertise a missing file. See [MEM-OBJ-selection-text](#mem-obj-selection-text), [MEM-OBJ-tool-source](#mem-obj-tool-source) and [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution).
2. Listing is an exhaustive metadata projection, not a retrieval ranker. The model receives all four selection fields for every entry and interprets the conversational triggers. Source bodies stay out of that listing. No listing-specific token, count or relevance budget is imposed by the inspected code. See [MEM-RTE-capability-list](#mem-rte-capability-list).
3. Registration admits a replacement before observing its execution. Failure feedback can guide a later model-authored overwrite, but the registry preserves neither a prior version nor structured test evidence/rationale. The human editor and workspace-writable generated code can bypass this registration path. See the annotations on [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) and [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation).
4. Chat/debug display is not durable experience memory. The desktop retains in-memory traces for people; the adapter forwards the new user text, not a reconstructed transcript. Opaque SDK history must not be confused with either the display or the persistent tool library. See [MEM-OBJ-agent-display](#mem-obj-agent-display) and the annotation on [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-selection-text
Label: Capability selection text

Natural-language `capability`, `triggers` and `suppression` fields live in `tools/index.json` beside the symbolic name. They describe when a tool should be selected or avoided, not fixed dispatch predicates. Model-authored registration supplies these strings; existing or manually edited files have unresolved provenance. There is no supplied corpus from which to judge their truth or completeness. The foreground model interprets these fields after [MEM-RTE-capability-list](#mem-rte-capability-list); the human browser displays them through [MEM-RTE-capability-browser](#mem-rte-capability-browser). Neither delivery establishes compliance. They survive process restart until overwritten or removed from disk; there is no expiry check in the registry.

No supplied object has this referent. Closest supplied records are the encompassing write route [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) and executable authority [RT-BAP-capability-source](runtime.md#rt-bap-capability-source); this object is selection text, not the route or executable body. Source: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/prompt.ts`.

> Triggers are observable conversational moments — describe the situation, not a keyword.
> Suppression conditions are moments that resemble a trigger but should NOT fire the tool.
> --- `tendril-agent/src/loop/prompt.ts`

#### MEM-OBJ-index-metadata
Label: Capability index metadata

Symbolic JSON names, `tool_path`, creation date, attribution and version occupy the same filesystem index as selection text but have different consumers. `register` derives path from name, stamps the current date, hardcodes `created_by: 'model'` and `version: '1.0.0'`, and replaces by exact name. This is bookkeeping, not retained source history, tested quality or trustworthy provenance after alternative writers modify the file. Node listing omits the latter metadata; execution derives a path from the requested name rather than consulting `tool_path`. Rust browser returns full index entries and displays date/path. Initialization creates an empty versioned index only if absent; it does not re-author or attest a preexisting corpus.

Distinct from [MEM-OBJ-selection-text](#mem-obj-selection-text): these fields have fixed parsing/lookup/display rules, not conversational meanings. Closest supplied record [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) is a writer rather than an object. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/types.ts`, `tendril-ui/src-tauri/src/workspace.rs`, `tendril-ui/src-tauri/src/capabilities.rs`, `tendril-ui/src/components/CapabilityBrowser.tsx`.

> tool_path: `${definition.name}.ts`,
>       created: new Date().toISOString().split('T')[0],
>       created_by: 'model',
>       version: '1.0.0',
> --- `tendril-agent/src/loop/registry.ts`

#### MEM-OBJ-tool-source
Label: Capability TypeScript source

Symbolic executable TypeScript is retained as UTF-8 `tools/{name}.ts`. Registration stores the model-supplied code string unchanged. Same-name writes replace it. Source may also come from existing files, human edits or workspace-authorized programs; actual accumulated contents and initial provenance are unknown. It is derived task machinery, not an automatically retained raw execution trace. Comments or explanations may occur inside arbitrary code, but the API mandates no rationale field. Deno receives source with a JSON-argument/workspace prelude, not the selection text or index history. The model does not receive the body through list; a generated read-file capability could expose it, but no such accumulated capability is supplied.

This object is the source payload of [RT-BAP-capability-source](runtime.md#rt-bap-capability-source), not a second authority-path declaration. [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) remains the canonical execution route. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/sandbox.ts`; the supplied execution record retains the exact `load` and permission passages.

> const prelude = `const args = ${JSON.stringify(args)};\nconst __workspace = ${JSON.stringify(workspacePath)};\n`;
>   const script = `${prelude}\n${code}`;
> --- `tendril-agent/src/loop/sandbox.ts`

#### MEM-OBJ-agent-display
Label: Agent messages and debug log

React process memory holds messages, tool-call inputs, outputs and usage as symbolic records with natural-language/code payloads. Debug records coalesce text chunks, filter stdout-guard noise and trim older entries with an entry-count slice; these are human-display transformations, not semantic summary memory for the model. `MAX_DEBUG_LOG_ENTRIES` is 500, but slicing the previous list then appending can produce 501 entries, and text within a chunk group can keep growing. It is not a byte/token bound. Tool results and traces have no durable serialization or reload route in the inspected provider/hook. They can remain visible during a sidecar reconnect while its agent state is reconstructed; they are not proof of that agent's remembered conversation.

The closest supplied record is [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream), a transport route rather than the desktop state object. SDK conversation state is a separate opaque dependency responsibility, not this object. Evidence: SRC-1, `tendril-ui/src/context/AgentContext.tsx`, `tendril-ui/src/hooks/useAgent.ts`, `tendril-agent/src/index.ts`.

> const [state, dispatch] = useReducer(agentReducer, initialState);
>   const [debugLog, setDebugLog] = useState<DebugEntry[]>([]);
> --- `tendril-ui/src/context/AgentContext.tsx`

### Routes

#### MEM-RTE-capability-list
Label: Model capability listing

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pretty-printed JSON of all names and selection text, or an instruction to register a tool if empty/failing.
- Later read-back: Each tool invocation reloads the persisted index; later model invocations can receive entries written during prior turns or process lifetimes.
- Delegated visibility: Foreground model receives name, capability, triggers and suppression through a tool result; bodies, dates, attribution, paths and versions are omitted.
- Selection predicate: Model calls listCapabilities with an empty input object; Node loads every index entry and projects the four fields. The foreground model then judges semantic fit against its task/context.
- Invalidation or expiry: Next call rereads changed disk bytes; no age/quality expiry or source-existence reconciliation. Missing/corrupt index can look empty.
- Activation or effect: The returned text can influence the model's later tool selection. Actual use, compliance and benefit are unobserved.
- Evidence limits: No corpus or run trace; SDK serialization, full working context and any SDK truncation are uninspected.

Endpoints: persisted index → registry projection → bootstrap tool callback → SDK model context. The request is model-pulled, not unsolicited automatic supply. No ranker, query embedding, per-task filter, top-k or listing token budget is implemented here. Omitting bodies is a fixed payload boundary; it does not prove the whole model window remains bounded. Empty/failing listing text requests creation; it is not a factual determination that no executable file exists.

This is the read operation mentioned by [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), not that write route itself; closest other supplied record [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence) is the guiding policy. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`.

> return index.capabilities.map(({ name, capability, triggers, suppression }) => ({
>       name,
>       capability,
>       triggers,
>       suppression,
>     }));
> --- `tendril-agent/src/loop/registry.ts`

> return JSON.stringify(results, null, 2);
> --- `tendril-agent/src/loop/tools.ts`

#### MEM-RTE-capability-browser
Label: Human capability browsing

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rust returns full capability entries to React; expanding a card fetches named source and displays it read-only.
- Later read-back: Mount/refresh reads the persisted index; first card expansion reads the current named source. Both can expose material from prior sessions to a human.
- Delegated visibility: Human sees selection text, date and displayed path, and source on expansion. These calls do not inject content into the model.
- Selection predicate: Browser loads all capabilities without relevance ranking; human chooses a card by name. A card fetches source only while its local source cache is null; subsequent toggles reuse cached bytes.
- Invalidation or expiry: Refresh replaces index state; existing same-key cards do not explicitly invalidate source caches on a source edit. Unmount/remount can clear local state; no TTL.
- Activation or effect: Supports inspection and copying; does not execute or approve registration. Human decisions following inspection are not supplied.
- Evidence limits: No observed UI session; source preview freshness is not guaranteed. Backend source reading checks name characters but does not validate the workspace root, as the supplied runtime notes.

Endpoints and owner: human/React mount or refresh → useCapabilities → Rust index reader → cards; human expansion → Rust source reader → CodeEditor. This differs from [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation), the editor write route, and [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution), which loads for Deno. The generic FileExplorer offers a separate human file read/editor path with a 1 MiB read limit; the specialized source reader has no corresponding explicit cap. Evidence: SRC-1, `tendril-ui/src/hooks/useCapabilities.ts`, `tendril-ui/src/components/CapabilityBrowser.tsx`, `tendril-ui/src-tauri/src/capabilities.rs`, `tendril-ui/src-tauri/src/files.rs`.

> if (!expanded && source === null) {
>       setLoading(true);
>       try {
>         const code = await invoke<string>('read_tool_source', {
>           workspace: workspacePath,
>           name: cap.name,
>         });
>         setSource(code);
> --- `tendril-ui/src/components/CapabilityBrowser.tsx`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-selection-guidance
Label: Selection text guidance

Consumer: foreground configured model. Channel: JSON-formatted tool result containing [MEM-OBJ-selection-text](#mem-obj-selection-text) through [MEM-RTE-capability-list](#mem-rte-capability-list). Force: natural-language guidance about capability fit, not a deterministic suppression gate, source verification or enforced authorization. Horizon: persisted index across tasks/sessions until modified, and model context after delivery subject to uninspected SDK history handling. Origin may be model, human or program; listing conveys no trust attestation. This is distinct from [RT-BAP-capability-source](runtime.md#rt-bap-capability-source), whose consumer is Deno, and [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance), whose content is the static system instruction. Evidence: SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/prompt.ts`; minimum passages retained in the selection object and listing route above.

## Annotations

#### On [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)

Memory lineage and admission: task/context → foreground model authors selection text and code → schema/name checks → Node writes index then source. Starting chat is not per-capability human approval. Human veto is not present in this callback; schema/name/I/O failure can stop admission, not reject based on correctness. Same-name registration stamps a new date and the same fixed version, so it retains no prior lineage or structured reason for replacement. The open-request prompt requests repair on failure, but the write callback neither executes the candidate first nor compares it with an answer oracle. Subsequent execution can fail after the changed bytes are already retained. Full replacement makes repair possible, not demonstrated learning. Evidence: SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/prompt.ts`; supplied route passages establish sequencing and repair instruction.

Reasons/outcomes: retained fields are code, descriptions, conversational conditions and bookkeeping. A model could encode reasons in these arbitrary strings or comments; absent corpus prevents judging actual content. The API does not retain an outcome-to-revision log, original prompt or failure trace alongside a registration. A possible trace-fed repair chain is subprocess error → SDK/model context → model replacement → disk → later listing/Deno. Only the requested repair behavior and write/read capabilities are established, not an exercised automatic trace-derived update. Code-preserved theory content, criticism and improved capacity remain uninspected, not disproved by the missing rationale schema.

#### On [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)

Read-back consumption: a model-requested name selects the entire current UTF-8 source file; Node constructs a temporary script and Deno consumes it as executable symbolic content. Name is an address, not evidence of content-targeted retrieval. There is no source-size limit or source trust/admission verification in `load`; subprocess output has a combined 1 MiB cap and execution timeout, not a registry-context budget. Index text is not delivered to Deno. Return stdout is model-visible current-run feedback, not a separately saved memory record. The temporary script includes source/args and is unlinked best-effort in finally; no checkpoint or later reload uses that temporary path. Its removal does not withdraw the durable tool or undo filesystem/network effects. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/sandbox.ts`; supplied execution route retains load/permissions passages.

#### On [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation)

Admission remains separate for its two mechanisms. A generated program can write registry or arbitrary workspace bytes through the Deno workspace grant without a second approval. A human editor chooses content and confirms replacement; Rust enforces path containment and performs I/O without capability semantic validation. That confirmation governs the editor, not registration, generated programs or direct backend callers. Program writes are afforded; the shipped editor commands are wired. Initial/preexisting file control is unknown, but that does not hide these known subsequent writers. Evidence: SRC-1, `tendril-agent/src/loop/sandbox.ts`, `tendril-ui/src/components/FileExplorer.tsx`, `tendril-ui/src-tauri/src/files.rs`, with confirmation/grant passages in the supplied records.

Curation can replace executable machinery or selection text independently. The index can be emptied without disabling a known source name; removing source can break execution while leaving an advertised entry. The registry exposes no coupled remove/revoke operation in the completely inspected `registry.ts`/`tools.ts`. A workspace-authorized program can use filesystem removal; what any actual generated program removes is unknown. Withdrawal therefore needs attention to both read paths, and overwrite is not versioned rollback. Arbitrary workspace retention/readers are afforded by code authority, but a hypothetical generated reader is not a shipped consumer route. No accumulated `record_decision` implementation was supplied; the prompt's example definition is not an installed memory tool. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/sandbox.ts`.

#### On [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)

Working context: Tendril constructs one Agent at startup and forwards extracted current user text to it; no per-protocol-session reconstruction is performed here. Previous desktop messages/tool traces are display state, not replay input. Plain SDK turn/tool accumulation is distinct from inspectable context management; actual SDK persistence, eviction, compaction summaries, checkpoint alternatives and reload are uninspected because dependency internals are outside SRC-1. `createAgent` configures no Tendril summarizer, sub-agent frame or trimming hook. This bounded constructor fact does not establish absence of such mechanisms inside Strands.

The listing projection keeps source bodies and access metadata out of that model-facing tool result, leaving names and conversational summaries reachable; full source can still be selected by execute for a different consumer. The prompt also asks generated programs to filter/reshape results before logging. That is a model-authored payload policy, not an enforced summarizer or guaranteed semantic retention. At the SDK call boundary there is no inspected summary/raw-tail substitute or durable conversation checkpoint. A sidecar rebuild discards its process state while disk tools survive. Thus a stack-frame analogy is limited: Deno has temporary execution state and returns stdout, but filesystem writes escape too; it is not an isolated sub-agent model context. Evidence: SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/index.ts`, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/sandbox.ts`, `tendril-ui/src/hooks/useAgent.ts`; lifecycle support also comes from the supplied route.

> - Return ONLY the data the user needs — filter and reshape before logging.
> --- `tendril-agent/src/loop/prompt.ts`

#### On [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt)

The display file is a derived UTF-8 copy of shipped instructions generated at startup, not a retained adaptation read by the agent. Rust `get_system_prompt` reads it for human settings display; editing the workspace copy can change that display until the next write, not the constructor's instruction. This is a material distinction between readable representation and actual instruction authority. Evidence: SRC-1, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/agent.ts`, `tendril-ui/src-tauri/src/capabilities.rs`; the supplied object retains the constructor passage.

## Write side

Acquisition begins with a human-chosen workspace. Rust preserves an existing index and otherwise creates an empty one, so the code establishes initialization mechanics but not authorship/trust of preexisting contents. Model registration subsequently authors and admits [MEM-OBJ-selection-text](#mem-obj-selection-text) and [MEM-OBJ-tool-source](#mem-obj-tool-source), with Node-derived [MEM-OBJ-index-metadata](#mem-obj-index-metadata). None is automatically a record of a successful action. The registration callback can save an implementation that has never run; a failed execution does not undo admission. Source: SRC-1, `tendril-ui/src-tauri/src/workspace.rs`, `tendril-agent/src/loop/registry.ts`, and the annotation on [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission).

Maintenance is replacement, not a retained revision chain. The model is instructed to repair code after failure; no observed repair episode or mandatory evaluator gate is supplied. Registry tests assert register/list/load/replacement properties and the selection projection, not longitudinal improvement or runtime admission decisions (SRC-1, `tendril-agent/tests/registry.test.ts`). There is no witnessed raw-trace → derived-memory → changed-future-behavior chain. A failure-mediated model repair is an intended possibility whose derivation and success remain unobserved. Alternative program and human writes retain their different admission controls as annotated on [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation).

Cleanup of an execution script affects only an ephemeral copy. Corrupt-index fallback can hide retained source without deleting it; a subsequent registration starting from the empty fallback can replace the index without restoring its former entries. Same-name overwrite and corrective manual edits are available recovery, not rollback. Removing an index entry alone is insufficient revocation because execute reads files independently. These limits follow directly from SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts` and the supplied execution route.

## Read-back

The model pulls the whole projected index through [MEM-RTE-capability-list](#mem-rte-capability-list), then chooses a name by interpreting descriptions in its current context. No independent selector pushes chosen memories or binds triggers to callbacks. [MEM-BAP-selection-guidance](#mem-bap-selection-guidance) is guidance authority, whereas [RT-BAP-capability-source](runtime.md#rt-bap-capability-source) is executable authority. Named execution reloads complete source into Deno, not model context. There is no established body-inspection step before the model requests execution. Evidence: SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/sandbox.ts`.

The human browser has its own index refresh and source-expansion chain; its cached source may differ from the next execution's freshly reloaded bytes. Generic file reads let humans inspect and then edit retained content under a separate UI confirmation flow. These are explicit later consumers, not hypothetical callers inferred from a storage method. See [MEM-RTE-capability-browser](#mem-rte-capability-browser) and [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation).

Raw desktop traces remain human-visible process state. The prompt adapter does not use them to reconstruct an agent after restart; the SDK's actual in-process history rules are not available. Settings reload affects model/execution controls through [RT-RTE-settings-restart](runtime.md#rt-rte-settings-restart), not a trace-based learning route. No observed reuse or outcome improvement follows merely from these wired read paths.

## Integration issues

- No correction to the supplied runtime facts is required. Its mixed alternate-mutation route contains two different admission owners; the annotation separates human-confirmed editing from program-authorized writes without changing that route's identity. Reconciliation should retain that distinction when using [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation).
- No duplicate declaration is intended. [MEM-OBJ-tool-source](#mem-obj-tool-source) is the payload of supplied [RT-BAP-capability-source](runtime.md#rt-bap-capability-source), not a competing authority record. [MEM-RTE-capability-list](#mem-rte-capability-list) expands the later read-back named in [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission); it is distinct from the write operation. Other closest-record comparisons occur beside each new declaration.
- SDK-owned history, compaction/checkpoint alternatives and context bounds remain unresolved. The inspected constructor supplies no Tendril mechanism and the dependency implementation is outside the frozen evidence. This prevents a complete claim about model working-context management or durable conversation memory; it does not invalidate the wired capability store. Concerns [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream), [MEM-OBJ-agent-display](#mem-obj-agent-display).
- Actual corpus provenance, rationale content and generated file readers/writers remain unknown without a supplied workspace. Prompt examples are not installed capabilities. This prevents schema enumeration for arbitrary workspace memory, provenance attestation and an exercised trace-learning claim. Concerns [MEM-OBJ-tool-source](#mem-obj-tool-source), [MEM-OBJ-selection-text](#mem-obj-selection-text), [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation).
- No traces or controlled comparisons establish activation, successful repair, longitudinal learning or benefit. Operation remains uninspected for the declared routes. This is an evidence limit, not a claim that retention cannot change behavior.

## Limitations and checks

The source HEAD was rechecked as e671a4143d28de68289efd81580002041bb4cb6a; repository identity and scope remain SRC-1 as registered in boundary. The supplied job, member contracts, collection contract and shared records contract were read completely, including bounded continuation reads. Direct source and supplied runtime findings are distinguished in the coverage table. No other revision, prior system review, target execution or model-provider call was used.

The analysis establishes implemented retention, transformations, admission and consumer boundaries. No actual retained corpus or run validates metadata truth, generated code correctness, repair behavior, context-budget sufficiency or improvement. Available but uninspected configuration/host details are not access gaps or evidenced absences. Dependency opacity remains local to SDK/provider conclusions.

Deterministic validation: the required validate-output command passed its member content check. It reported that invocation residue was not checked. This establishes neither job acceptance nor claim support.
