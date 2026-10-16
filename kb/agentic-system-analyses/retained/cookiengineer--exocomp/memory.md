---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Exocomp memory: restored conversations, contractor report selection, project records and afforded instruction loading."
run-id: AAS-2026-10-14-exocomp-692bb27c35f9-01
source-identity: https://github.com/cookiengineer/exocomp
reviewed-boundary: b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251
---

# Exocomp memory report

## Boundary and evidence

This report covers retained project/session state and working-context selection in Exocomp at the boundary's frozen commit. SRC-1 is the repository registered in [boundary](boundary.md#source-register). Evidence is implementation and doctrine/design, not a new observed run. No target executable, test, provider or example was run. Historical session artifacts registered by the boundary are not used here to infer current-revision operation.

The supplied runtime establishes command dispatch and effect routes. Direct reads below trace recovery, admission, withdrawal and the intervening selections that determine what later consumers actually receive. Included surfaces are session and agent JSON; contractor transcripts, Quit reports and Inquire projection; requirements, bug and changelog stores; local role YAML; skill discovery/loading/removal; diagnostic snapshots; and terminal/web/debug consumers. Product files and program output enter through the runtime's file/program routes. External model parameters, provider caches and arbitrary project authorship remain opaque. Generated browser assets and external GUI dependencies remain excluded evidence, preventing a deployment-success claim rather than excluding the authored browser consumer.

| Entry point or operation | SRC-1 paths and inspection basis | Record coverage or limit |
|---|---|---|
| CLI terminal/web/webview/agent; agimus connect; shutdown | Dispatch supplied by runtime; direct `source/ui/tty/Client.go`, `source/ui/jsonl/Client.go`, `source/engine/Session.go`, `source/utils/engine/RestoreSession.go`; web setup supplied by runtime | [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat), [MEM-RTE-session-recovery](#mem-rte-session-recovery). JSONL NewClient starts fresh; terminal/web reload. Debug relocation supplied by runtime, utility directly checked. |
| Session backup, agent enumeration and restoration | Direct `source/engine/Recovery.go`, `source/types/Agent.go`, `source/tools/Agents.go` | [MEM-OBJ-agent-messages](#mem-obj-agent-messages), [MEM-RTE-session-recovery](#mem-rte-session-recovery); parse success is not authenticated content admission. |
| Contractor frame, Await, Quit and Inquire | Supplied runtime plus direct Hire/Await/SetAgent and `source/tools/getAgentWorkReport.go`, JSONL QuitHook | Annotations on [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work), [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire); no default Inquire grant or summary-fidelity observation. |
| Requirements Define*, Signoff, List/Search, JSON display | Direct `source/tools/Requirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`, `source/tools/writeRequirements.go`, `source/utils/ast/GetPackageSymbols.go`; correction reads `source/tools/Toolset.go`, `source/schemas/ToolCall.go`, `source/agents/architect.yaml` | [MEM-RTE-requirement-update](#mem-rte-requirement-update), [MEM-OBJ-requirement-behavior](#mem-obj-requirement-behavior), [MEM-OBJ-requirement-declaration](#mem-obj-requirement-declaration); ordinary Define* dispatch is blocked by method-name mismatch; direct definition methods exist. Signoff/read reconstruction remain wired; source-derived records override same-key authored behavior. |
| Bugs Add/Fix/List/Search and JSON display | Direct `source/tools/Bugs.go`, `source/tools/readBugs.go`, `source/tools/writeBugs.go` | [MEM-RTE-project-records](#mem-rte-project-records), [MEM-OBJ-bug-description](#mem-obj-bug-description), [MEM-OBJ-bug-status](#mem-obj-bug-status). Fix hides reports from tool lists, not from JSON. |
| Changelog Add/Change/Fix/Deprecate/Remove, List/Search and JSON | Direct createEntry/List/MarshalJSON/Remove; Search shape supplied by scoped source search; direct read/write helpers | [MEM-OBJ-changelog-entry](#mem-obj-changelog-entry), [MEM-RTE-project-records](#mem-rte-project-records). Remove appends an event; no deletion conclusion. |
| HTTP and browser read-back | Direct `source/ui/web/routes/session/Requirements.go`, `Bugs.go`, `Changelog.go`, `Agents.go`, `Messages.go`; direct `app/controllers/Requirements.go`, `app/controllers/Bugs.go`; scoped search of `app/controllers/Changelog.go` | [MEM-RTE-operator-display](#mem-rte-operator-display). Changelog rendering details not fully inspected; successful browser operation unobserved. |
| Local roles and subsequent template lookup | Direct `source/tools/readAgents.go`, `source/agents/SetRole.go`, `source/agents/NewAgent.go`, `source/agents/Roles.go`, `source/cmds/exocomp-agent/main.go` | [MEM-RTE-role-discovery](#mem-rte-role-discovery). Role registration is not proof that a new contractor process executes that registered template. |
| Skill catalog refresh, loaded objects, separate instruction helpers and scripts | Direct `source/tools/readSkills.go`; correction reads `source/tools/Skills.go` List/Load/Unload, `source/engine/Session.go` LoadSkill/UnloadSkill/CallTool, `source/schemas/ToolCall.go`, `source/types/Command.go`, `source/ui/web/routes/session/CallTool.go`; parser-chain evidence also supplied by runtime | Annotation on [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading); construction/List refresh discovery, qualified Load/Unload change loaded objects and append generic notices, not body insertion/removal. Helpers or bare-name API separately afford system-body changes. Default embedded grants absent per [RT-ABS-skill-grants](runtime.md#rt-abs-skill-grants). No actual project skills supplied. |
| Debug snapshots, usage counters, console and human questions | Direct Recovery/Session/Agent and `source/tools/Humans.go`; correction reads qualified-name parser/command/web chain above; supplied console recovery | [MEM-OBJ-debug-snapshot](#mem-obj-debug-snapshot), [MEM-RTE-session-recovery](#mem-rte-session-recovery). Qualified humans.Answer appends a generic answer/error tool message; Ask/Choose can separately append their Await return. Only bare-name humans/Answer enters the out-of-bounds special branch. Pending wait-state restoration remains unestablished. |
| File/program effects; compilation/installation | Supplied [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-program-execution](runtime.md#rt-rte-program-execution), [RT-RTE-build-install](runtime.md#rt-rte-build-install) | Persistent external product/production material, not automatic memory curation. Arbitrary program-created memory is uninspected. |
| Destructive startup cleanup | Direct `quickstart-exocomp.sh` | [MEM-RTE-session-recovery](#mem-rte-session-recovery). Deletes source-local `.exocomp`, not all project-local roles/skills or product files. |
| Tests and historical artifacts | Runtime/boundary supply source-test and retained-artifact limits; not independently used for memory efficacy | No learned-capacity, fidelity, reliability or causal-benefit conclusion. Available test cases not run or comprehensively audited. |

## Core ideas

1. **Recovery reuses conversation content, not running workers.** A planner's accumulated messages survive JSON backup and reach later inference. Recovered child records support report extraction and inspection without reviving their processes. Distinct contractor contexts keep child turns out of the parent's request; shared files and collected transcripts outlive those contexts. See [MEM-RTE-session-recovery](#mem-rte-session-recovery) and the contractor annotation.
2. **Project records have different truth and retirement rules.** Bug Fix records a caller's assertion and suppresses tool-visible open reports. Changelog Remove records an event. Requirements combine authored behavior with source-derived declarations; implemented entries are excluded from persisted requirements JSON and source-derived entries win on reload. Signoff does not preserve an immutable implemented specification. See [MEM-RTE-project-records](#mem-rte-project-records), [MEM-RTE-requirement-update](#mem-rte-requirement-update).
3. **Loaded skills, instruction bodies and grants have separate consumers.** Qualified Skills.Load changes the loaded object and appends a generic tool notice, not the skill body. Separate Session helpers or bare-name API use afford system-priority body delivery/removal; ordinary qualified Unload does not withdraw an injected body. Methods/programs are symbolic execution grants. Project role loading can replace the process's template map, but ordinary child creation precedes that child's tool construction. Do not equate the parent's registered role or bookkeeping Agent with the child's effective prompt/grants. See [MEM-RTE-role-discovery](#mem-rte-role-discovery) and the skill annotation.
4. **There is selective delivery, not demonstrated learning.** Await extracts a report; Inquire requests a lossy prose summary; List/Search select stored project records. Ordinary inference sends accumulated messages without an inspected budget-driven compaction rule. Counters and raw snapshots do not establish improved future capacity. See [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire), [MEM-OBJ-debug-snapshot](#mem-obj-debug-snapshot) and [MEM-BAP-retained-content](#mem-bap-retained-content).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-agent-messages
Label: Agent messages

Part of: [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work)

This part is the parent-collected contractor message sequence, not the entire process route. Source-native identity: `types.Agent.Messages`. Storage substrate: in-memory Agent and `.exocomp/agents/<name>.json`; planner Agent.Messages additionally reside in session JSON. Natural-language Content/ReasoningContent are distinct from symbolic Role, ToolCalls, ToolCallID and tool-name routing fields. The sequence is a raw conversation record, not an evaluated knowledge store; each nested tool result may itself contain derived material. Agent status, timestamps and ContextUsage are access/lifecycle metadata, not evidence that the work report is true. Lineage: child stdout records appended to the parent's bookkeeping Agent; planner turns appended by Session. Non-debug bookkeeping can include a parent-rendered system message rather than the child's emitted prompt. Later consumers are Await's report extractor, Inquire's projection, operator JSON inspection and restored planner inference for the planner variant. Reasons persist only insofar as message content supplied them; complete private model processing is not accessible. This material part complements, rather than replaces, the supplied contractor route and role-grant object. SRC-1: `source/types/Agent.go`, `source/tools/Agents.go`, `source/engine/Session.go`, `source/engine/Recovery.go`.

> Messages        []*schemas.Message `json:"messages" yaml:"messages"`
> --- `source/types/Agent.go`

#### MEM-OBJ-requirement-behavior
Label: Requirement behavior

Source-native identity: `Requirement.Behavior` in the contents map and `.exocomp/requirements.json`. Representational form: natural-language specification accepted by direct Define* methods or imported JSON; storage: JSON plus in-memory map. Ordinary shipped Define* tool dispatch is blocked by method-name mismatch, as established in [MEM-RTE-requirement-update](#mem-rte-requirement-update); the direct-method capacity does not establish granted-tool acquisition. Authorship can be human or computational; the API does not establish origin. Caller-selected path/symbol identifies the specification, not its evidence source. Requirements.List/Search and the operator UI expose it for model/human interpretation. Source-derived requirements instead set Behavior empty and take precedence at the same file/symbol key. Define* may replace a unit; there is no separate retained criticism/reason field in the inspected write transformation. No exact supplied object counterpart: [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff) operates on this content's surrounding record, rather than being the content itself. SRC-1: `source/tools/Requirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`, `source/tools/writeRequirements.go`.

> Behavior:      "",
> IsImplemented: true,
> --- `source/tools/readImplementedRequirements.go`

#### MEM-OBJ-requirement-declaration
Label: Requirement declaration and status

Source-native identity: requirement File/Symbol/Type/Declaration/IsImplemented fields. Representational form: symbolic Go declaration plus identity/status metadata. Storage: source files for reconstructed declarations, JSON for unimplemented specifications, and the freshly merged in-memory map. Direct-method authored declaration text is admitted through Go parsing; ordinary Define* tool reachability is blocked as described in [MEM-RTE-requirement-update](#mem-rte-requirement-update). reconstructed content comes from GetPackageSymbols with `with_private=false`. The status consumer is writeRequirements' filtering rule and UI/model display; HasSymbol is Signoff's structural check, not a behavior oracle. The declaration does not preserve the original behavior merely because it has the same symbol. Distinct from [RT-OBJ-role-grants](runtime.md#rt-obj-role-grants), which admits execution; closest supplied route is [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff). SRC-1: `source/tools/readImplementedRequirements.go`, `source/utils/ast/GetPackageSymbols.go`, `source/tools/writeRequirements.go`, `source/tools/Requirements.go`.

> if specification.IsImplemented == false {
> --- `source/tools/writeRequirements.go`

#### MEM-OBJ-bug-description
Label: Bug description

Source-native identity: `types.Bug.Description`, keyed by project-relative file and symbol. Representational form: natural-language report. Storage: `.exocomp/bugs.json` and Bugs.contents. Lineage: explicit Add arguments, single-line formatting on Call, replacement at an existing key; no automatic extraction from tests is established. Consumers: requested tool List/Search and operator JSON/UI. Description may include a reason but the tool does not demand evidence or attach a test trace. Distinct from runtime's product-file object/routes: this is a report about a product. No supplied exact counterpart after comparison with [RT-RTE-file-admission](runtime.md#rt-rte-file-admission). SRC-1: `source/tools/Bugs.go`, `source/tools/readBugs.go`, `source/tools/writeBugs.go`.

> bug_report.Description = description
> bug_report.IsFixed = false
> --- `source/tools/Bugs.go`

#### MEM-OBJ-bug-status
Label: Bug identity and fixed status

Source-native identity: Bug.File/Symbol/IsFixed. Representational form: symbolic key and boolean consumed by fixed rules. Storage: same JSON/map as description, but authority differs: status controls List/Search visibility, while description is interpreted. Fix sets true without reading or testing product code; Add resets false at an existing key. Fixed entries are serialized, not deleted. Operator JSON marshaling reloads the whole map, so the status suppresses one consumer route rather than withdrawing the underlying description everywhere. Distinct from [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff): bug retirement has no AST gate. SRC-1: `source/tools/Bugs.go`, `source/tools/writeBugs.go`.

> bug_report.IsFixed = true
> tool.contents[internal_path][symbol] = bug_report
> --- `source/tools/Bugs.go`

#### MEM-OBJ-changelog-entry
Label: Changelog entry

Source-native identity: `types.ChangelogEntry` in Changelog.contents. Storage: `.exocomp/changelog.json` and per-file/symbol entry arrays. Operative parts: Description is natural-language reported change; Date/Type/File/Symbol are symbolic indexing/display and duplicate-detection metadata. Their different consumption rules are retained here; they share append admission and persistence. Origin is explicit method arguments, not a verified diff. createEntry suppresses a duplicate matching type/file/symbol/description, without comparing date; otherwise it appends with today's date. Remove adds a Type=Remove entry rather than erasing history. Later consumers are tool List/Search and JSON/UI, with model/human interpretation rather than executable instruction force. No supplied exact counterpart after comparison with [RT-RTE-file-admission](runtime.md#rt-rte-file-admission); the event does not establish the file effect occurred. SRC-1: `source/tools/Changelog.go`, `source/tools/readChangelog.go`, `source/tools/writeChangelog.go`.

> return tool.createEntry("Remove", path, symbol, description)
> --- `source/tools/Changelog.go`

> if entry.Type == method && entry.File == internal_path && entry.Symbol == symbol && entry.Description == description {
> --- `source/tools/Changelog.go`

#### MEM-OBJ-debug-snapshot
Label: Debug snapshot

Source-native identity: Recovery.Snapshot/SnapshotBytes outputs, notably `.exocomp/debug/request.json` and `response.json`. Storage: filesystem JSON. Representational form: symbolic request/response envelopes containing natural-language payloads; external numerical/model state is not captured. Lineage: marshaled request after adapter transformation, response payload before response adaptation. This is diagnostic raw I/O, overwritten at the same names, not derived memory. There is no opaque checkpoint decoding claim. Supplied [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) already distinguishes diagnostics from inference read-back; this object complements that route and may expose richer request content than prose summaries. The inspected recovery path reads session/agent JSON, not these snapshots. A diagnostic external caller could read them, but none is established here as an automatic future model consumer. SRC-1: `source/engine/Session.go`, `source/engine/Recovery.go`.

> session.Recovery.SnapshotBytes("request", request_payload)
> --- `source/engine/Session.go`

### Routes

#### MEM-RTE-session-recovery
Label: Session recovery

Planner response handling or client destruction → Recovery JSON serialization → later terminal/web construction → parsed/restored Session and child Agent map → later inference/report request. Owner: Recovery and client setup code. This is a memory-specific route overlapping the later-read-back portions of [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) and [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work), not a replacement for either invocation loop. No exact supplied recovery-route declaration exists.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Backup returns an I/O/serialization error or nil; inspected planner response calls ignore that return. Constructors return a recovered session or a fresh fallback.
- Later read-back: session.json supplies planner messages/configuration; agents/*.json supplies recorded contractors to SetAgent. Later inference receives accumulated planner messages, while Await extracts a stored child report. JSONL NewClient does not load prior session JSON.
- Delegated visibility: Parent backup enumerates contractors via installed agents.List capability and serializes their Agents. Restore supplies metadata/transcripts, not original process handles or restored OS effects.
- Selection predicate: HasBackup existence check, fixed project-relative session path, JSON parsing, .json agent enumeration and sanitized names; later Await is caller-selected by recorded name. No relevance-ranking/token selection is applied to the restored planner transcript.
- Invalidation or expiry: Next backup overwrites files; no atomic session-plus-agent transaction or TTL is established. quickstart-exocomp deletes source-local .exocomp before launching; ordinary restarts need not delete it.
- Activation or effect: Restored planner content is available to subsequent model requests; reconstructed process/tool infrastructure differs from persisted content. Model compliance and successful restoration were not observed.
- Evidence limits: No execution or backup-integrity experiment. Missing/invalid JSON can yield nil/fallback; nested contractor backup errors are not propagated. Serialized content trust is filesystem trust, not independently authenticated provenance.

Admission: runtime proposes unchanged accumulated state; serialization, names and filesystem I/O decide physical admission. Later JSON parsing admits recovery without human per-content approval or semantic oracle. Starting/restarting is operator control of the workflow, not evidence of approval of each stored turn. No content-revision experiment or correctness gate accompanies this checkpoint. Existing product effects are not rolled back. SRC-1: `source/engine/Recovery.go`, `source/engine/Session.go`, `source/ui/tty/Client.go`, `source/ui/jsonl/Client.go`, `source/tools/Agents.go`, `source/utils/engine/RestoreSession.go`, `quickstart-exocomp.sh`; web constructor coverage from supplied runtime.

> Agent:    backup.Agent,
> Config:   backup.Config,
> --- `source/engine/Session.go`

> session = recovery.RestoreSession()
> --- `source/ui/tty/Client.go`

> rm -rf "${ROOT}/source/.exocomp";
> --- `quickstart-exocomp.sh`

#### MEM-RTE-requirement-update
Label: Requirement update

Direct Define* method invocation or shipped Signoff request → path/AST checks → map update → writeRequirements → later readRequirements source reconstruction and JSON merge → List/Search/UI. Owner: Requirements and AST helper code; caller proposes declaration/behavior or symbol signoff. Ordinary model and parsed client Define* calls do not reach definition: Toolset turns architect's DefineFunc grant into Definefunc, whereas ToolCall parses DefineFunc and Requirements.Call requires that spelling after HasMethod. The same mismatch applies to DefineInterface/DefineStruct/DefineType and prevents matching definition schemas in Schemas. Direct public methods remain available but bypass this dispatch gate. Distinct admission route from product writes; overlaps [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff) in the valid Signoff branch only.

- signoff and reconstruction implementation conclusion status: wired
- direct definition implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Ordinary parsed Define* dispatch returns tool-not-allowed errors; a directly invoked Define* method can yield success/error notices. Signoff yields marked-implemented notice after symbol check and persistence attempt.
- Later read-back: readRequirements rebuilds the map from source declarations first and admits JSON specifications only at missing keys. List/Search/MarshalJSON expose the merged view; only unimplemented map entries are serialized by writeRequirements.
- Delegated visibility: Contractors and planner can read the same project records where their assigned sandbox permits display; child-owned source changes can alter subsequent planner requirements views independently of the child report.
- Selection predicate: Shipped Define* dispatch fails the mismatched method-membership check before declaration parsing. Direct Define* methods parse the requested Go declaration; Signoff tests expected symbol/type existence. Source reconstruction scans .go files under the sandbox with private-symbol inclusion false; source-derived entries win file/symbol collisions. List is sandbox-visible inventory; Search uses path-prefix plus optional case-insensitive symbol substring, not semantic retrieval.
- Invalidation or expiry: A successful direct Define* method replaces a key; an ordinary blocked definition call does not. On reread an existing source symbol can replace authored behavior with an empty Behavior field; Signoff excludes the implemented unit from persisted JSON. Source deletion/change may remove reconstructed units without recovering discarded authored behavior.
- Activation or effect: Model/human readers see fresh declaration/status material and any surviving authored behavior. Status means structural implementation, not demonstrated satisfaction of the behavior.
- Evidence limits: No execution; direct-method definition capacity is not shipped tool reachability. Private/exported symbol details beyond helper selection and no behavioral oracle validated here. Automatic refresh is source-fed reconstruction, not trace-fed model improvement. Original rationale can be lost at source collisions.

Admission is computational path/parse/I/O checking; caller identity leaves human authorship/veto unresolved. Direct Define* replaces content after syntax admission without a behavior test; ordinary tool calls cannot pass the preceding mismatched grant check. Signoff's structural check is not an expected-answer oracle. Guidance can come from current conversation and role prompt, but the API does not require retaining the reason for revision. There is no automatic versioned rollback. Open specification management, not a bounded experiment. SRC-1: `source/tools/Requirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`, `source/tools/writeRequirements.go`, `source/utils/ast/GetPackageSymbols.go`, `source/tools/Toolset.go`, `source/schemas/ToolCall.go`, `source/agents/architect.yaml`.

> method := strings.ToUpper(tmp2[0:1]) + strings.ToLower(tmp2[1:])
> --- `source/tools/Toolset.go`

> return "Define" + strings.ToUpper(tmp2[0:1]) + strings.ToLower(tmp2[1:])
> --- `source/schemas/ToolCall.go`

> } else if method == "DefineFunc" {
> --- `source/tools/Requirements.go`

> - requirements.DefineFunc
> - requirements.DefineInterface
> - requirements.DefineStruct
> - requirements.DefineType
> --- `source/agents/architect.yaml`

> _, exists := tool.contents[file][symbol]
>
> if exists == false {
> tool.contents[file][symbol] = specification
> }
> --- `source/tools/readRequirements.go`

#### MEM-RTE-project-records
Label: Project record maintenance

Granted/direct Bugs.Add/Fix or Changelog event request → path/key checks → reload/map edit → JSON overwrite → later List/Search or operator fetch. Owner: tool code; model/direct caller proposes report text or retirement/event type. No supplied exact counterpart after comparison with [RT-RTE-client-tools](runtime.md#rt-rte-client-tools): that record describes admission into tool dispatch, not these specific report transformations.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Written/updated/fixed/event notice, duplicate-entry notice, or path/I/O/missing-report error.
- Later read-back: Bugs List/Search return only unfixed descriptions; whole-map JSON still carries fixed entries. Changelog List returns event descriptions ordered by date; Search affords file/symbol filtering. JSON is reread before the examined tool/HTTP serialization paths.
- Delegated visibility: Shared project-relative stores can carry contractor reports to planner and operator without copying the contractor's full context; path/sandbox selection constrains display.
- Selection predicate: Bugs uses file/symbol keys; Search's specified symbol is an exact key and List filters IsFixed=false. Changelog admission deduplicates type/file/symbol/description; its List groups dates. No automatic relevance or quality-ranking model selects these records.
- Invalidation or expiry: Add replaces bug text and reopens it; Fix changes a flag without removing stored text. Changelog Remove adds an event. Subsequent JSON overwrites persist the current map, without a versioned rollback/expiry mechanism in these helpers.
- Activation or effect: Requested records become tool-message context or operator display; reports can influence later proposals but truth, actual defect resolution and behavior change were not observed.
- Evidence limits: No test/output oracle in the examined Add/Fix/createEntry methods; their names do not establish successful product changes. Authorship and evidence origin are caller-dependent, not established by persistence.

Admission is symbolic path/key checking, duplicate handling and serialization/I/O. Fix has no verification gate; callers can retire a report without supplying corrected code. No human per-report approval is enforced by these methods. Role guidance shapes model proposals but is separate from runtime admission. A failure may leave edited in-memory state before persistent I/O succeeds. SRC-1: `source/tools/Bugs.go`, `source/tools/Changelog.go`, `source/tools/readBugs.go`, `source/tools/readChangelog.go`, `source/tools/writeBugs.go`, `source/tools/writeChangelog.go`.

> bytes, err1 := json.MarshalIndent(tool.contents, "", "\t")
> --- `source/tools/writeBugs.go`

> if bug_report.IsFixed == false {
> --- `source/tools/Bugs.go:277-335`

#### MEM-RTE-operator-display
Label: Operator retained-state display

Operator/browser GET → session API → messages/agents or tool MarshalJSON with reload → parsed browser report objects → filtered display. Owner: server handlers and browser controllers. Distinct read-only consumption from [RT-RTE-client-tools](runtime.md#rt-rte-client-tools), which performs direct tool calls rather than GET display.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON response or handler error; browser fetch failures leave without replacing its report list.
- Later read-back: Later requests expose restored conversations/contractor Agents and freshly read project records. Browser bug/requirement controllers flatten map entries, retaining description/behavior and metadata for display/filtering.
- Delegated visibility: Agents endpoint includes planner plus recorded contractors, not only the work report. Messages returns planner messages; contractor context can be inspected via the agent records rather than being automatically injected into planner inference.
- Selection predicate: Server selects installed tools and complete map/message arrays; browser bug/requirement filters match lowercased textual fields against an operator query. These are display selectors, not model-input budgets or semantic retrieval.
- Invalidation or expiry: Later fetch replaces browser report lists; a changed disk store affects tool serialization on the next GET. There is no evidence this UI itself retracts prior model context.
- Activation or effect: Human inspection channel, not model instruction injection. Actual browser rendering, operator judgments or subsequent action remain unobserved.
- Evidence limits: Generated frontend distribution/dependency gap retained from boundary. Changelog fetch route is inspected by scoped search, but detailed rendering/filter semantics are not generalized from Bugs/Requirements.

SRC-1: `source/ui/web/routes/session/Requirements.go`, `source/ui/web/routes/session/Bugs.go`, `source/ui/web/routes/session/Changelog.go`, `source/ui/web/routes/session/Agents.go`, `source/ui/web/routes/session/Messages.go`, `app/controllers/Requirements.go`, `app/controllers/Bugs.go`, `app/controllers/Changelog.go`.

> messages := session.GetMessages(0)
> --- `source/ui/web/routes/session/Messages.go`

> response, err := bugs.Main.Client.Read("/api/session/bugs")
> --- `app/controllers/Bugs.go`

#### MEM-RTE-role-discovery
Label: Project role discovery

Agents tool construction → read `<playground>/agents/*.yaml` → ParseAgent/IsValid → SetRole replaces process-global template → subsequent NewAgent lookup. Owner: boot-time discovery/template code. Distinct from [RT-BAP-role-prompt](runtime.md#rt-bap-role-prompt): this is project-local admission into the template map, not merely static prompt delivery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: readAgents returns collected parse/read errors or success; NewAgents ignores that return. SetRole reports true on matching role/non-nil template.
- Later read-back: Durable project YAML is re-read when a new Agents tool is constructed; later same-process NewAgent reads the replaced template's prompt and grants. Ordinary Hire creates parent bookkeeping Agents after this registration.
- Delegated visibility: The child receives role/task/path arguments, not serialized replacement template content. Its initial NewAgent occurs before its own tool construction; successful parent registration alone does not prove child execution of the local template.
- Selection predicate: .yaml file extension, parse success, IsValid formatting tests, role match; files can replace an embedded role by key. Agent.IsValid does not establish a semantic/security approval of AllowedTools/AllowedPrograms.
- Invalidation or expiry: Boot-only discovery; changed files are not automatically refreshed in the existing tool. SetRole overwrites the map with no recorded prior-template rollback. Existing Agents are not rewritten by registration.
- Activation or effect: Registration changes later same-process template selection and parent-side metadata. Instructional execution in an ordinary fresh child is not established for this route.
- Evidence limits: Arbitrary project YAML authorship/provenance unknown. No target run; no claim that this makes skills/Inquire default grants or updates live workers.

Admission is software parse/format/role matching, not per-content human approval. External file editing can propose prompt/grant changes; no automatic trace-fed role authoring is shown. This is explicit project customization, not a measured improvement experiment. SRC-1: `source/tools/readAgents.go`, `source/tools/Agents.go`, `source/agents/SetRole.go`, `source/agents/NewAgent.go`, `source/cmds/exocomp-agent/main.go`.

> if agent.IsValid() == true {
> agents.SetRole(agent.Role, agent)
> }
> --- `source/tools/readAgents.go`

> Roles[role] = agent
> --- `source/agents/SetRole.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-content
Label: Retained conversation and report authority

Consumer: configured foreground model on a later completion. Channel: recovered Agent.Messages or tool-message delivery of requested reports/specifications. Force: interpreted conversational evidence/instructions; persisted system-role content retains its message role, while tool results are not automatically promoted to system instructions. Horizon: later invocations within one project and across successful backups/restores. Content delivery establishes possible influence, not compliance, truth or benefit. Symbolic bug/status/write filters decide what reaches the channel before model interpretation. This path complements [RT-BAP-role-prompt](runtime.md#rt-bap-role-prompt): static role prompt authority is distinct from accumulated report/transcript authority. SRC-1: `source/engine/Session.go`, `source/engine/Recovery.go`, `source/tools/Bugs.go`, `source/tools/Requirements.go`; see [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) for the quoted request-message selection.

## Annotations

#### On [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work)

Memory selection: the foreground caller picks the role/task/sandbox, not a full parent transcript. Child messages remain outside the parent model window; code collects stdout into the parent Agent map and recovery can retain that map. Await selects a recorded name and extracts the latest matching tool-message work report, not all child messages or tests. There is no token budget in this extraction. This resembles a separate conversational frame whose selected return value escapes, but not an isolated disposable filesystem: shared files and the parent's transcript remain reachable. Parent-side system-message lineage depends on debug mode and can differ from child execution. Reasons remain only if emitted in retained text; the report label is not evidence preservation or evaluation. SRC-1: `source/tools/Agents.go`, `source/tools/getAgentWorkReport.go`, `source/ui/jsonl/Client.go`, `source/engine/Recovery.go`.

> if message.Role == "tool" && strings.HasPrefix(message.Content, "agents.Quit: Work Report\n") {
> return strings.TrimSpace(strings.TrimPrefix(message.Content, "agents.Quit: Work Report\n"))
> }
> --- `source/tools/getAgentWorkReport.go`

#### On [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire)

Raw-to-derived chain: recorded child messages → user/assistant prose-only single-line projection → new summarizer conversation → last parsed stdout message Content → tool result → later caller inference/backup if called through Session. This summary supplements, rather than replaces, the child transcript. The supplied route's quotations establish its selection/parse logic; model and invocation facts stay there. No reference-summary comparison validates lost tool evidence or retained reasoning. No inspected explicit token budget governs projection, and the caller's requested agent is the targeting input. The summary may carry reasons present in selected prose but omitted system/tool messages cannot be reconstructed by this projection. Derived context delivery is not learned capacity or automatic transcript compaction. SRC-1: `source/tools/Agents.go`, `source/utils/chat/SummarizeMessages.go`; supporting passages are in the supplied route.

#### On [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading)

Retained substrate: project-local SKILL.md and .go files; natural-language body, symbolic dependency/script metadata and executable Go source have different consumers. Discovery occurs at tool construction and explicit Skills.List. List invokes readSkills, which clears and rebuilds the catalog from disk; the constructor's boot-only comment is contradicted by this operative call. Catalog refresh neither replaces loaded_skills entries nor updates injected system bodies. File authorship and initial approval remain unknown. Qualified model, terminal and web Load requests choose a named discovered skill and test wrapper dependencies, but only change loaded_skills and append the generic success/error tool notice. ToolCall.GetName and Command.Name preserve qualified names; Session's special branches require the bare name skills. Later inference therefore sees a notice, not the body, on these ordinary routes. Qualified Unload removes loaded bookkeeping and appends a notice without removing injected system text. Load can replace the same-name loaded object from the current catalog; later Execute consumes its scripts independently of instruction delivery. Separate Session.LoadSkill/UnloadSkill calls, or an embedding using bare-name Session.CallTool, afford insertion/removal of a system body. The bare-name route performs the underlying tool call first and then selects the catalog object for the helper; helper failure does not roll back loaded-state changes. Session checks duplicate bodies by text, not name: changed text can append a second system body without removing the old one. Helper Unload removes only matching text while preserving other turns, source files and prior effects; catalog refresh and loaded/body divergence prevent a general same-name withdrawal guarantee. Disk instructions can be rediscovered through List within the same process or on restart, and successfully backed-up messages can retain an injected body; restoration of the tool's loaded_skills bookkeeping is not established merely by restoring Agent.Messages. Direct Session.LoadSkill has the weaker program gate recorded by runtime. No embedded skill grant is inferred from available code or local-role registration. SRC-1: `source/tools/readSkills.go`, `source/tools/Skills.go`, `source/engine/Session.go`; supplied route quotations support insertion and admission. The supplied runtime now distinguishes catalog refresh, qualified bookkeeping and separate helper/bare-name body delivery. Its parser and branch quotations support that distinction.

> func (tool *Skills) List() (string, error) {
>
> readSkills(tool)
> --- `source/tools/Skills.go`

> for name, _ := range tool.contents {
> delete(tool.contents, name)
> }
> --- `source/tools/readSkills.go`

#### On [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff)

Persistence correction: writeRequirements does not serialize an implemented specification/status. It serializes only entries whose IsImplemented is false. The later read clears/reconstructs the map from source and merges JSON only at missing file/symbol keys. Thus the retained product source, not an immutable signoff record, supplies subsequent implemented declarations with empty Behavior. Same-key authored behavior can disappear even before explicit Signoff, because source precedence occurs on read. The quoted filtering and empty-body evidence resides in [MEM-OBJ-requirement-declaration](#mem-obj-requirement-declaration) and [MEM-OBJ-requirement-behavior](#mem-obj-requirement-behavior). SRC-1: `source/tools/writeRequirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`.

## Write side

### Acquisition and admission

Recovery automatically retains raw turns and contractor records under [MEM-RTE-session-recovery](#mem-rte-session-recovery); it does not derive revised instructions from their evaluation. The raw transcript may contain model reasoning or external program output, with that provenance retained only through the message envelope/content. Provider-private memory remains opaque. Debug snapshots preserve another raw representation at fixed filenames, not a chronological evidence archive. Humans stores questions/answers in its current-run map; Answer writes the answer and releases a matching pending wait before Session handles delivery. Ordinary model and web parsers produce humans.Answer, and terminal commands preserve that qualified name. Those calls bypass Session's bare-name humans/Answer branch and append the formatted answer or error as a generic tool message. That message can reach later inference and backup/restore through [MEM-RTE-session-recovery](#mem-rte-session-recovery); a direct client tool call does not itself start inference or guarantee backup. Ask/Choose separately call Await: a stored nonempty answer can return to their waiting call and enter a generic message associated with that original call. This is conditional implemented delivery, not observed operation or a correctness check. Only an embedding using bare name humans and method Answer enters the special reverse scan at len(Messages), which is out of bounds before its intended message append and leaves the Session mutex locked. Tool-local mutation happens first even on that defective alternative. The new Humans tool has no demonstrated reload of pending waits; restored answer-bearing messages do not recreate the question map or waiter. These are current-run coordination and raw transcript retention, not an automatically curated reusable question store. SRC-1: `source/tools/Humans.go`, `source/engine/Recovery.go`, `source/engine/Session.go`, `source/schemas/ToolCall.go`, `source/types/Command.go`, `source/ui/web/routes/session/CallTool.go`; see [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) for qualified client dispatch.

> if name == "humans" && method == "Answer" {
> --- `source/engine/Session.go`

> for m := len(session.Agent.Messages); m >= 0; m-- {
>
> message := session.Agent.Messages[m]
> --- `source/engine/Session.go`

> return tool + "." + method, nil
> --- `source/schemas/ToolCall.go`

> command.Name = strings.TrimSpace(name)
> command.Method = strings.TrimSpace(command.Name[strings.LastIndex(command.Name, ".")+1:])
> --- `source/types/Command.go`

> if question.Answer != "" {
> return fmt.Sprintf("humans.%s: Answer for Question \"%s\":\n===\n%s\n===", question.Type, question.Question, question.Answer), nil
> --- `source/tools/Humans.go`

> if err0 == nil {
> content = strings.TrimSpace(result)
> } else {
> content = fmt.Sprintf("Error: %s", strings.TrimSpace(err0.Error()))
> }
>
> session.mutex.Lock()
> tmp := &schemas.Message{
> Role:       "tool",
> Content:    content,
> ToolCallID: id,
> ToolName:   name,
> Created:    schemas.NewDatetime(),
> }
> session.Agent.Messages = append(session.Agent.Messages, tmp)
> session.mutex.Unlock()
> --- `source/engine/Session.go:365-380`

> other.Answer = answer
> --- `source/tools/Humans.go`

> delete(tool.states, question)
> state.cancel()
> close(state.done)
> --- `source/tools/Humans.go`

Project report updates have software admission and caller-dependent authorship. Bugs and changelog accept textual reports after method/path checks, not after test success. Direct Requirements definition methods check declaration syntax, while shipped Define* dispatch is obstructed by the method-name mismatch. Valid Signoff checks symbol presence; persistence/reconstruction applies separately. The source-derived requirement view is automatic transformation of project code, not a trace-learning result. Local roles and skills admit externally authored instruction material, but neither discovery routine determines whether that content was human-written, model-written or approved. Role discovery is construction-only in the inspected route; Skills.List explicitly refreshes its catalog during the same process. That refresh does not replace loaded objects or injected instruction bodies. Ordinary qualified Load/Unload changes loaded bookkeeping, with generic notices as the model-visible result; only separate helper/bare-name invocation affords body insertion/removal. Product file/process writes can alter those files outside the narrow tool's maintenance protocol. See [MEM-RTE-project-records](#mem-rte-project-records), [MEM-RTE-requirement-update](#mem-rte-requirement-update), [MEM-RTE-role-discovery](#mem-rte-role-discovery), [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-program-execution](runtime.md#rt-rte-program-execution).

### Maintenance, rejection and withdrawal

Bug Fix retires only tool-list visibility; JSON/operator access still reaches the stored description. Changelog Remove is not withdrawal. Requirement source precedence and unimplemented-only persistence can withdraw authored behavioral content without keeping a criticism or original rationale. Skill List rebuilds the discovery catalog without withdrawing loaded objects or injected bodies. Qualified Load adopts the refreshed object for script selection without injecting its text; qualified Unload removes loaded state without withdrawing any system body. The separate helper/bare-name route can insert refreshed text while an older differing body remains; helper Unload's text match does not guarantee removal of every same-name historical body. None of these actions rolls back prior script effects or deletes skill files. Session overwrite/quickstart cleanup affects checkpoints, not a rollback of product work. Parse/path/I/O rejection is not rejection of a claim as false. These distinct rules are evidenced in their records; neither labels nor successful returns imply semantic evaluation.

The Inquire chain is the inspected trace-fed derivation: child prose becomes a summary for later caller inference. Its runtime route is afforded, not default-wired through current embedded grants. The original child transcript remains retained; this is not checkpoint replacement. Backup/session JSON and debug snapshots are alternative raw retention forms, not competing compressed checkpoints. No causal benefit, reflective revision or improved future capacity is established by any of these storage/summary mechanisms.

## Read-back

- **Automatic restored-context supply:** startup chooses fixed session JSON and parsed backup content. A later inference includes accumulated messages wholesale before provider adaptation. This is checkpoint selection, not a semantic request query or independent proactive knowledge recommender. Source construction has Options nil; usage measurement does not here implement eviction. SRC-1: `source/engine/Session.go`, `source/ui/tty/Client.go`; [MEM-RTE-session-recovery](#mem-rte-session-recovery).
- **Requested record delivery:** foreground tool calls choose Await/Inquire agent, List inventory or Search file/symbol inputs. The selected material enters a tool message for later inference; direct client CallTool does not itself initiate that inference. Bugs suppression, requirements reconstruction and Inquire omission constrain what reaches the consumer. See [MEM-RTE-project-records](#mem-rte-project-records), [MEM-RTE-requirement-update](#mem-rte-requirement-update), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) and annotations.
- **Skill adoption versus instruction injection/removal:** construction or explicit Skills.List supplies the discovery catalog; List refreshes disk metadata/text, not loaded objects or injected bodies. Qualified Load/Unload updates loaded objects and delivers generic notices, not instruction bodies or their withdrawal. Separate helpers or bare-name API use select a body for system-priority insertion/removal; body-text matching can retain differing historical versions. Backups can retain such separately injected bodies, and qualified Unload does not retract them. The source files remain reachable after unload. Distinct child frames avoid copying accumulated parent context and return requested report/summary material, without a classical heap-reference/liveness protocol. See skill and contractor annotations.
- **Operator read-back:** GET paths return richer objects than model report extraction, including fixed bug entries and contractor records. Browser filtering is human-facing display, not automatic inclusion into the model window. See [MEM-RTE-operator-display](#mem-rte-operator-display).
- **Storage without established read-back:** debug snapshots have a storage capability but no inspected automatic next-inference consumer. Provider caching/opaque retention, pending human wait restoration, arbitrary program stores and live child loaded-skill-state recovery remain unestablished. These limits do not erase the known transcript/project-record paths.

No observed activation or benefit follows from delivery. Instructions have model-interpreted force; status/key filters and installed method grants have code-enforced force within their respective consumers, not a universal source-trust guarantee.

## Integration issues

1. **Signoff persistence correction is already reflected in supplied runtime.** [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff) now distinguishes omitted implemented entries and source-derived status. [MEM-RTE-requirement-update](#mem-rte-requirement-update) retains the same memory consequence: implemented units are excluded from JSON, source-derived declarations win collisions and Behavior is empty. Do not integrate this as a durable signed-off behavioral specification. Evidence: SRC-1 `source/tools/writeRequirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`.
2. **Identity overlap, not exact duplicate:** [MEM-RTE-session-recovery](#mem-rte-session-recovery) spans later read-back portions of [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) and [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work). [MEM-RTE-requirement-update](#mem-rte-requirement-update) includes the supplied Signoff branch but also Define* and reconstruction. Their route boundaries differ; Define* is direct-method capacity, not wired ordinary dispatch. Do not silently supersede the supplied records. Agent.Messages is explicitly a material part of the contractor route. Other objects have no exact supplied counterpart.
3. **Local role registration has limited execution reach.** [MEM-RTE-role-discovery](#mem-rte-role-discovery) adds a shipped project-local template path. Parent bookkeeping after registration can differ from the ordinary child initialized before tool discovery. This reinforces runtime's parent/child model-identity limit and prevents treating local grants as default execution. No change to [RT-ABS-skill-grants](runtime.md#rt-abs-skill-grants)' bounded embedded-YAML absence is needed. Evidence: SRC-1 `source/tools/readAgents.go`, `source/tools/Agents.go`, `source/cmds/exocomp-agent/main.go`.
4. **Restored skill body versus loaded-tool state remains unresolved.** The skill annotation and [MEM-RTE-session-recovery](#mem-rte-session-recovery) establish persisted message bodies and newly constructed tools, not restored loaded_skills bookkeeping or reliable later Unload. Consequence: do not claim complete cross-restart extension-state recovery from transcript persistence. Source files and tests are available but no run was authorized; evidence: SRC-1 `source/engine/Session.go`, `source/ui/tty/Client.go`, supplied [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading).
5. **Skill delivery correction.** The skill annotation, coverage, Core ideas, acquisition, maintenance and read-back distinguish construction/List catalog refresh, qualified Load/Unload bookkeeping with generic notices, and separate helper/bare-name system-body insertion/removal. This agrees with the supplied revised [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading), rather than the older fragment in the refusal. SRC-1 `source/tools/Skills.go`, `source/tools/readSkills.go`, `source/engine/Session.go`, `source/schemas/ToolCall.go`, `source/types/Command.go`, `source/ui/web/routes/session/CallTool.go`. Granting a skill method alone does not fix body delivery. Refresh does not resolve cross-restart loaded-state uncertainty or change absent embedded grants.
6. **Definition dispatch obstruction.** [MEM-RTE-requirement-update](#mem-rte-requirement-update) preserves direct Define* capacity and valid Signoff/reconstruction but withdraws wired ordinary definition dispatch. Toolset's Definefunc conflicts with ToolCall/Requirements' DefineFunc; the other Define* names have the same mismatch. SRC-1 `source/tools/Toolset.go`, `source/schemas/ToolCall.go`, `source/tools/Requirements.go`, `source/agents/architect.yaml`. Definition prompts/grants alone therefore cannot establish tool-mediated authored-spec acquisition.
7. **Answer retention correction and peer conflict.** Qualified humans.Answer takes generic Session message admission, not the defective bare-name scan. Its answer/error message can reach later inference and [MEM-RTE-session-recovery](#mem-rte-session-recovery); Ask/Choose separately can append a nonempty Await answer under the original call. Bare-name humans/Answer still mutates tool-local state before the out-of-bounds scan and locked-mutex failure. This corrects the predecessor's normal-delivery exclusion and conflicts with the supplied refusal fragment of [EPI-RTE-human-answers](epistemic.md#epi-rte-human-answers), which attributes the bare-name failure to the browser/normal route. The epistemic owner must correct that route's downstream fields; this report does not change its declaration. SRC-1 `source/engine/Session.go`, `source/tools/Humans.go`, `source/schemas/ToolCall.go`, `source/types/Command.go`, `source/ui/web/routes/session/CallTool.go`. Implemented transcript admission is distinct from observed delivery, successful backup and pending-wait restoration.
8. **Observation and provenance limits remain.** Registered historical artifacts were not used to resolve memory efficacy; arbitrary project report/instruction authorship, provider state and external process stores are unknown. The report supports implementation-level delivery/admission distinctions, not learning or comprehensive reliability. Changelog detailed browser filtering and pending human coordination-state restoration remain uninspected, without preventing the narrower records above.

## Limitations and checks

The checkout HEAD was rechecked as b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251 and git status was clean. Source identity equals the supplied run identity; source evidence stays under SRC-1 and the same commit. Supplied job, member types, collection, worker rules and complete record contract were read, recovering terminal blank ranges after bounded input reads. No peer attempt, prior analysis or external source was inspected; no target execution occurred.

Counterexamples used before settling claims: fixed bugs survive JSON display despite List withdrawal; Remove appends rather than deletes; requirements source reconstruction overrides authored behavior; backup returns are ignored in the response loop; fresh JSONL and template-registration ordering differ from terminal recovery and parent bookkeeping. These qualify broad labels without claiming observed failures. Available but unread helpers/rendering/test details are inspection limits, not access gaps or evidenced absences. No standalone absence record is inferred from a search miss.

This correction directly rechecked Skills.List/Load/Unload, Session.CallTool/LoadSkill/UnloadSkill, ToolCall.GetName, Command.Parse and the web CallTool handler, plus Humans.Answer/Ask/Choose/Await. Qualified-name dispatch is the source-supported counterexample to the predecessor's body-delivery and Answer-obstruction claims. Earlier requirement/role/project-record findings are preserved from the supplied baseline. The supplied runtime's qualified-skill distinction and corrected Signoff persistence are incorporated without changing its records. All predecessor MEM IDs remain declared.

Validation: deterministic validate-output passed for this invocation. It checks structure, citations and quotation occurrence, not semantic acceptance, execution or benefit.
