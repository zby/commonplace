---
type: types/agentic-system-analysis-result.md
description: arsumbris release-wide analysis of typed graph memory, adapter-specific controls and instructed
  knowledge/improvement workflows
run-id: AAS-2026-09-23-arsumbris-02
system: arsumbris
run-date: '2026-09-23'
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: arsumbris-0.0.1-alpha-release-bundle-2026-09-23
analysis-cutoff: '2026-09-23'
evidence-tier: code-grounded
memory-comparison:
  scope: Accumulated or revised workspace graph content and schemas, derived access structures and launch artifacts,
    correction-derived guidance, and retained session continuity facts in the 22 pinned release repositories.
    Ordinary current-run read/served hashes and freshness notices are auxiliary context controls outside this
    normalized memory scope. Shipped unchanged instructions are delivery machinery, not accumulated memory.
    External harness/model storage and compaction internals are excluded.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - files
      - graph
      - in-memory
      - repo
      records:
      - OBJ-3
      - OBJ-5
      - OBJ-7
      note: Files and Git history retain content; the engine holds the typed graph; recovered governance logs
        are held in memory with file recovery. Current-run read/served maps are excluded.
    representational_form:
      assessment: known
      basis: afforded
      values:
      - natural-language
      - symbolic
      records:
      - OBJ-3
      - OBJ-5
      - OBJ-6
      - OBJ-7
      note: Prose plus typed fields, references, schemas, generated structures and procedural code; external
        opaque harness payloads excluded.
    lineage:
      assessment: known
      basis: afforded
      values:
      - authored
      - imported
      - other-compiled
      - trace-extracted
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-12
      - RTE-13
      note: Human/agent authoring, source import, deterministic graph and delivery compilation, and afforded
        extraction of corrections from work.
    behavioral_authority:
      assessment: known
      basis: afforded
      values:
      - instruction
      - knowledge
      - routing
      - validation
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-13
      note: Knowledge is advisory; selected rules/skills instruct; maps and descriptions route; revised schemas
        validate. Current-run read-hash enforcement is outside the memory scope. Learning is the derivation
        process, not a further consumer authority here.
    write_agency:
      assessment: known
      basis: afforded
      values:
      - automatic
      - manual
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-12
      - RTE-13
      note: Human editing and machine transformations coexist; agent-executed procedures are afforded automatic
        production, not autonomous enforced scheduling.
    curation_operations:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-7
      - RTE-8
      - RTE-10
      note: Bounded support for consolidation, deduplication, evolution, invalidation, decay and synthesis
        is described below. The open remedy workflow does not establish an exhaustive union, especially whether
        adoption should count as promote.
    read_back_direction:
      assessment: known
      basis: wired
      values:
      - pull
      - push
      records:
      - RTE-6
      - RTE-9
      note: Agent graph/file requests pull; launch selection automatically supplies retained rule bodies and
        workspace overview. Session-local freshness notices are excluded.
    read_back_signal:
      assessment: known
      basis: wired
      values:
      - coarse
      - identifier
      records:
      - RTE-9
      note: Launch role/default-set and size budgeting are coarse; explicit owner:name matches and graph references
        select parts by identity. Lexical agent queries remain pull; current-run freshness notices are excluded.
    trace_learning:
      assessment: known
      basis: afforded
      values:
      - 'yes'
      records:
      - RTE-8
      note: A selected correction rule asks an agent to derive durable feedback records from interaction; improve
        and skill/rule authoring reuse them for later guidance. This is afforded instruction-following, not
        a kernel learning loop.
    trace_source:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-8
      note: Live behavior corrections are interaction-derived; skill maintenance also names selection traces
        and observed task results without fixing their recorded format. No complete controlled source set follows.
    learning_scope:
      assessment: known
      basis: afforded
      values:
      - cross-task
      - per-project
      records:
      - RTE-8
      note: Reusable corrections and workspace skill/rule revisions target future callers and workspace capabilities.
        Session identity supplies no additional task-horizon classification.
    learning_timing:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-8
      note: Correction capture is online and remedy adoption is staged; selection-trace authoring may use prior
        results. No exhaustive timing set is prescribed across these alternatives.
    distilled_form:
      assessment: known
      basis: afforded
      values:
      - natural-language
      - symbolic
      records:
      - RTE-8
      note: Corrections retain prose and typed recurrence/remedy links; remedies include rules and skills,
        with executable implementations explicitly afforded.
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: []
      note: Inspected material supplies evaluation instructions, not retained execution evidence of recall
        dependence. No sufficiently comprehensive retained-evidence search was performed to establish a bounded
        negative.
---

# arsumbris agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/arsumbris.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/memory-report.md`
**Memory analysis report SHA-256:** 36c972988a0b3efba6c11953cb66c2c4dfdccdfb33aa56d437ab851f7b705c7d

Run AAS-2026-09-23-arsumbris-02 opened 2026-09-23; system name is arsumbris. The retained exact result is intended for `kb/reports/retained/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/result.md`. Only the complete run state declares successful publication. No prior review or substantive prior analysis was read. Fresh memory and epistemic specialists received only this frozen source boundary and source-checkable seeds. Specialist model identity is unknown; instruction and input byte identities are retained with the local report.

## Boundary and evidence

Evidence basis: static code and doctrine inspection of the 0.0.1-alpha release, captured 2026-09-23; no product execution or causal experiment. This review is for understanding what the system wires, where its controls apply, and what its memory and knowledge workflows warrant.

arsumbris is a typed-knowledge IDE and agent operating layer: au-engine derives a graph from repositories, au-host supplies UI and launch control, and au-mcp exposes tools/hooks/context to external harnesses. The selected class is memory/knowledge/context-engineering system, with a whole-system boundary across the 22 first-party release repositories. This does not claim an exhaustive audit of every function. Included are graph/file mutation, discovery, session/context delivery, the two adapters and material knowledge/revision workflows, including their human and instructed-agent roles.

External harness/model internals are excluded, preventing claims about complete scheduling, weight changes, compaction, hidden reasoning or model compliance. Third-party libraries/converters and OS/Electron internals are excluded, preventing full semantic fidelity and isolation claims. Optional au-provenance/au-workflow packages and unrelated example repositories are not in the release manifest; references to them do not establish installed mechanisms. Full UI projection behavior and code generation are not audited; their performance or general safety cannot be concluded. Human decisions described by procedures are included as roles, not observed actions. No active user deployment, grant set or completed knowledge artifact was supplied.

The frozen boundary is SRC-23, an immutable bundle of the manifest-pinned source blobs the 22 Git sources in the Source register. Every component URL below retains its own full commit rather than borrowing the entry repository's revision. Binary images/assets are excluded. Source identity for workflow publication remains `https://github.com/arsumbris/arsumbris`.

## Source register

Every component's root is `/home/zby/llm/commonplace/related-systems/arsumbris--<repository>`. Each component commit was resolved from the entry repository's release manifest and checked against tag `0.0.1-alpha`. Git worktrees were not evidence. The entry repository is pinned separately; its manifest fixes the release, not current component branch heads. Each exact quote is attributable to its own full-commit blob, also retained in the frozen text bundle. Snapshot inclusion alone is not substantive inspection.

| Source ID | Kind | Identity/location | Revision/capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | frozen Git text in bundle | `https://github.com/arsumbris/arsumbris` | `a9f6cceedb191b8504443222d55d3106f9f36ba9` | doctrine/design or snapshot inventory only | README.md, INSTALL.md, VERSION.md, SAFETY.md — release boundary and claims | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-2 | frozen Git text in bundle | `https://github.com/arsumbris/au-engine` | `46f12389d4d4833fed51640a48cf938516433106` | implementation; doctrine/design (separately quoted) | crates/au-engine/src/mutate.rs, serve.rs, build.rs; README.md — held graph and writes | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-3 | frozen Git text in bundle | `https://github.com/arsumbris/au-engine-sdk` | `ffeca7a745af6f8069d5d2151fc96bae964825dd` | doctrine/design or snapshot inventory only | snapshot/access contract only; no separate semantic finding | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-4 | frozen Git text in bundle | `https://github.com/arsumbris/au-type-system` | `066fd06b224bc46358273ebfbc82b6b8863e9885` | doctrine/design or snapshot inventory only | snapshot/type-language dependency only; full language semantics uninspected | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-5 | frozen Git text in bundle | `https://github.com/arsumbris/au-host` | `0e85fb1731fdef2d6196618aff5a2a567e621866` | implementation; doctrine/design (separately quoted) | app/src/main/agent-launch.ts, terminal.ts, engine-connections.ts — launch, shell and write interfaces | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-6 | frozen Git text in bundle | `https://github.com/arsumbris/au-mcp` | `3ddc3b62ed0b339a89a57f11026676df18d3b2eb` | implementation; doctrine/design (separately quoted) | src/daemon/, src/inject/, src/skills/ — mediation, discovery, context, session retention | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-7 | frozen Git text in bundle | `https://github.com/arsumbris/au-mcp-sdk` | `91209bb00cebde36e6454207a89e257f20573577` | doctrine/design or snapshot inventory only | contract dependency; full SDK implementation uninspected | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-8 | frozen Git text in bundle | `https://github.com/arsumbris/au-mcp-core` | `25e0625e553c237671bba9a3a8c173a889dddf02` | implementation; doctrine/design (separately quoted) | src/file-tools.ts, read-guard.ts, native-tool-redirect.ts, repo-overview.ts — baseline tools and gates | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-9 | frozen Git text in bundle | `https://github.com/arsumbris/au-mcp-adapter-cc` | `333b2117f338cd4815eeeb9ab7b3932b29fa7d62` | implementation; doctrine/design (separately quoted) | src/launch-cc.ts, bridge.ts, mcp-server.ts, inject-cc.ts; hooks/ — invocation/context | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-10 | frozen Git text in bundle | `https://github.com/arsumbris/au-mcp-adapter-codex` | `3b0e3a3cf67b3143819c61c590efc85d36c23bc5` | implementation; doctrine/design (separately quoted) | src/bridge.ts, lift.ts, inject-codex.ts; hooks/ — mediation, capture and context | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-11 | frozen Git text in bundle | `https://github.com/arsumbris/au-type-codegen` | `e3c63da4afc77c2979ea06763c8c1045bcd93644` | doctrine/design or snapshot inventory only | snapshot/code-generation dependency only; no independent efficacy finding | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-12 | frozen Git text in bundle | `https://github.com/arsumbris/au-defaults` | `0879c5ef432b468b9fa0e4a3e52d2fb58d2ec504` | doctrine/design or snapshot inventory only | bundle/default composition inventory; deployed selection uninspected | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-13 | frozen Git text in bundle | `https://github.com/arsumbris/au-base-types` | `0a0c9770ffd2672b3e9937046721811c99d1d178` | doctrine/design or snapshot inventory only | type/supersede.type.yaml and base contracts | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-14 | frozen Git text in bundle | `https://github.com/arsumbris/au-weave` | `24320734e2436e8c75d44a7ff9afb6a330569840` | doctrine/design or snapshot inventory only | skills/, type/, guides/ — extraction, admission, grounding, maintenance; map coverage implementation excluded | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-15 | frozen Git text in bundle | `https://github.com/arsumbris/au-agent-guides` | `ddc33339c73278ed2b9a178030d9d94924e43224` | doctrine/design or snapshot inventory only | guides/base-layer/supersede.md — successor-chain interpretation | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-16 | frozen Git text in bundle | `https://github.com/arsumbris/au-rules` | `4be3274a4ed5b1d197652285ea253c651b50e484` | doctrine/design or snapshot inventory only | rule/inject contract inventory; independent learned content not assumed | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-17 | frozen Git text in bundle | `https://github.com/arsumbris/au-writing-style` | `163b5597583364649b0bd896575ae4167e436719` | doctrine/design or snapshot inventory only | skills/write-a-rule.md — authoring and activation | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-18 | frozen Git text in bundle | `https://github.com/arsumbris/au-skills` | `d32336d25b6ad2513976cba15ed69f30d6d1b38f` | doctrine/design or snapshot inventory only | skills/write-a-skill.md, guides/ — maintenance and evaluation guidance | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-19 | frozen Git text in bundle | `https://github.com/arsumbris/au-govern` | `8bf899b90a80081f328caacb0102ed47145b242d` | doctrine/design or snapshot inventory only | skills/check.md, fix.md, correction rule, profiles/, type/ — findings and corrections | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-20 | frozen Git text in bundle | `https://github.com/arsumbris/au-competency` | `6f23713425b2ba58b7361471badd58f63ca0642b` | doctrine/design or snapshot inventory only | skills/derive.md, propose.md, improve.md, self-research.md; type/proposal.type.yaml — improvement procedure | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-21 | frozen Git text in bundle | `https://github.com/arsumbris/au-ingest` | `5b3c22f930231ed12c964dce0144a35b5562ef9d` | implementation; doctrine/design (separately quoted) | ingest.mjs, converters/document.convert.mjs, converters/pdf.convert.mjs — import checks | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-22 | frozen Git text in bundle | `https://github.com/arsumbris/au-tree-research` | `65faf72fc107bb8eef84675e01bda18513d8b49a` | implementation; doctrine/design (separately quoted) | refresh-research-map.mjs, skills/, type/ — research and computed navigation | full-path quote URLs below | No product run; unlisted implementation uninspected |
| SRC-23 | immutable UTF-8 capture | `https://github.com/arsumbris/arsumbris` | `arsumbris-0.0.1-alpha-release-bundle-2026-09-23` | exact copy of primary implementation/doctrine; no observed-run evidence | All UTF-8 non-NUL blobs of SRC-1, SRC-2, SRC-3, SRC-4, SRC-5, SRC-6, SRC-7, SRC-8, SRC-9, SRC-10, SRC-11, SRC-12, SRC-13, SRC-14, SRC-15, SRC-16, SRC-17, SRC-18, SRC-19, SRC-20, SRC-21, SRC-22 | named frozen bundle and per-blob full-commit URLs | 15 binary blobs excluded; third-party dependencies and external harness/provider internals excluded |

The capture is 19,207,189 bytes, SHA-256 `b64f3d37b0259ec2e6d116a885c4287c99f69575763f6372ce639d597b533b8a`, at `/home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/source-bundle.txt`. Its header embeds all full commit identities and binary exclusions. This is a combined immutable evidence boundary, not a synthesized secondary source. No observed-run or causal-experiment source is asserted.

## Shared records

### Components

CMP-1 — au-engine: Rust graph, type checks and mutation daemon over workspace member files; symbolic executable implementation. Implementation conclusion status: wired. SRC-2 `crates/au-engine/src/mutate.rs:1-145` and `crates/au-engine/src/serve.rs:3950-4020`. The disk substrate and graph views are detailed by the memory records. Validation checks structural contracts, not general truth.

CMP-2 — au-mcp with au-mcp-core: workspace-scoped TypeScript daemon, registry, profile controls, plugin tools and hooks. Implementation conclusion status: wired. SRC-6 `src/daemon/daemon.ts:603-942`; SRC-8 `src/file-tools.ts:180-320`. No particular deployed profile is supplied, so a capability catalogue is not the current grant set.

CMP-3 — au-host and harness adapters: Electron launch/control surface and Claude Code/Codex translation, including session identity, hooks, generated context and MCP transport. Implementation conclusion status: wired. SRC-5 `app/src/main/agent-launch.ts:1-87`; SRC-9 `src/launch-cc.ts:48-77`; SRC-10 `src/bridge.ts:1-130`. Host UI projection internals are not exhaustively inspected. Model scheduling and agent delegation decisions belong to the external harness, not the graph engine.

CMP-4 — external harness-selected LLMs: distributed-parametric components invoked through Claude Code or Codex rather than a model owned by these release components. Integration conclusion status: wired (launching configured harness binaries); exact model/version pinning conclusion status: uninspected; parameter changes during operation conclusion status: uninspected. SRC-5 `app/src/main/agent-launch.ts:31-57` resolves an agent executable, and SRC-9 `src/launch-cc.ts:59-76` constructs its command. Neither identifies deployed model weights. Provider routing, model-internal criticism and external training are excluded; no fixed-weights assertion follows.


> const binary = resolveAgentBinary(agentBinary)
> --- [pinned source](https://github.com/arsumbris/au-host/blob/0e85fb1731fdef2d6196618aff5a2a567e621866/app/src/main/agent-launch.ts)

### Operative objects

OBJ-1 — requested tool action and candidate file content. A symbolic tool name/input envelope can carry natural-language or symbolic content. Transient before execution; accepted file bytes persist through RTE-2. Producers are the external agent or direct client; consumers are mediation, plugin and engine operations. Implementation conclusion status: wired. SRC-6 `src/daemon/daemon.ts:754-920`; SRC-8 `src/file-tools.ts:239-306`. A schema-valid request is not a warranted assertion.

OBJ-2 — plugin/type metadata and agent-profile configuration. Editable symbolic graph files declare runtime entry, contract version, tools/nativeTools and hook configuration; metadata is consumed by discovery and session scope. Implementation conclusion status: wired. SRC-6 `src/daemon/discovery.ts:307-355`, `src/daemon/daemon.ts:691-722`. They are addressable fields with operational authority; edits are not evidence that a better successor has been selected.

#### OBJ-3 — Typed workspace knowledge and mutable contracts

Evidence: SRC-2 `crates/au-engine/src/build.rs:1206-1220`; SRC-2 `crates/au-engine/src/mutate.rs:102-142`; SRC-13 `type/supersede.type.yaml:1-9`; SRC-14 `README.md:18-24,105-122`. Markdown/YAML files hold sources, nodes, extracts, maps, schemas and rules/skills. Text bodies are natural language; declared field/reference/type relations are symbolic. Git provides history where configured; the held engine graph and reference indexes are derived access structures, not an independent source of truth. Human and agent editing are both supported. The object's authority depends on RTE-6, RTE-7, RTE-8 and RTE-9. Implementation conclusion status: wired. The executable assembly below constructs the held catalog, graphs, resolved instances and backlink index. SRC-2 `README.md:3-17,54-77` separately describes their architectural role.

>     Ok(KnowledgeBase {
>         catalog,
>         graphs: Arc::new(graphs),
>         resolution_graphs,
>         indexes,
>         instances,
>         backlinks: backlinks.into_iter().collect(),
> --- [crates/au-engine/src/build.rs](https://github.com/arsumbris/au-engine/blob/46f12389d4d4833fed51640a48cf938516433106/crates/au-engine/src/build.rs#L1206)

#### OBJ-4 — Auxiliary current-run read/served hashes (outside memory profile)

Evidence: SRC-6 `src/daemon/session.ts:18-50`; SRC-6 `src/daemon/freshness.ts:45-97`; SRC-8 `src/read-guard.ts:77-96`. In-memory path-to-hash maps record access metadata, not remembered content or evidence of comprehension. A served file can satisfy a knowledge precondition, but does not count as an exact read for overwrite protection. Views are session-local and cleared on close, without replay restoring read credit. They are ordinary current-run control state, not memory read-back. The engine graph, navigation indexes and generated descriptions remain included reconstructible access derivatives under OBJ-3 and OBJ-7. Implementation conclusion status: wired.

>    * The served-view: canonical absolute paths of files a tool SERVED this session (e.g.
>    * `au_guide {scenario}` served its guide), computed at observe from the observed tool
>    * name + input + the tool's typed `serves-files-meta` contract ([[decision - 2607030037
>    * - au_guide satisfies a read-precondition via a declarative typed serves-contract, not a
>    * text sentinel::au-harness]]). SEPARATE from `readView`: a served VIEW satisfies a read-
>    * PRECONDITION (a knowledge gate) but must NOT satisfy read-before-WRITE (a safety gate on
>    * the exact current bytes) — so the write floor consults `readView` only. Reaped on close.
> --- [src/daemon/session.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/session.ts#L29)

#### OBJ-5 — Raw session facts and continuity record

Evidence: SRC-6 `src/daemon/crash-recovery.ts:25-55,70-104,237-263`; SRC-6 `src/daemon/session.ts:163-220`; SRC-6 `src/daemon/daemon.ts:624-675,738-742`. Raw stamped events live in a memory log; mediator-emitted governance events also append to hashed-session NDJSON recovery files under the device directory. A separate JSON record retains run, dormancy, harness, profile and an opaque resume reference. The reference is a relaunch locator, not an opaque memory payload consumed by this release. Visible transcript text can be replayed, without asserting access to encrypted reasoning. No model-generated distillation is implemented by this record. Implementation conclusion status: wired.

> export function appendRecovery(workspace: string, sessionId: string, event: SessionEvent): void {
>   try {
>     mkdirSync(recoveryDir(workspace), { recursive: true })
>     appendFileSync(recoveryFile(workspace, sessionId), JSON.stringify(event) + '\n')
>   } catch {
>     /* best-effort */
>   }
> --- [src/daemon/crash-recovery.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/crash-recovery.ts#L52)

#### OBJ-6 — Corrections, dispositions and their remedies

Evidence: SRC-19 `type/correction.type.yaml:1-17`; SRC-19 `type/correction.forged.type.yaml:1-14`; SRC-20 `skills/improve.md:17-29,38-90`. Corrections are derived records of interaction, distinct from raw transcript events. Their prose retains the original behavior and requested behavior; recurrence links preserve roots, and forged_into points to a demonstrated remedy. Later procedures read these records as evidence and proposed guidance. Remedies can be instructions, contracts or executable capabilities. Procedure conclusion status: afforded; observed completion is uninspected.

> #: A correction with a demonstrated remedy.
> #: Preserve the original feedback in the inherited body.
> #: An accepted write proves neither a valid record nor a working remedy.
> extends: correction
> fields:
>   #: The remedy shown to address this correction's friction.
>   forged_into: any*
>   #: The forged original occurrence.
>   #: Omit for a first occurrence.
>   #: Forge the root before a recurrence.
>   #: An incompatible root produces a diagnostic.
>   recurs?: correction.forged*
> --- [type/correction.forged.type.yaml](https://github.com/arsumbris/au-govern/blob/8bf899b90a80081f328caacb0102ed47145b242d/type/correction.forged.type.yaml#L1)

#### OBJ-7 — Generated launch and navigation material

Evidence: SRC-6 `src/skills/materialize.ts:1-16,33-43`; SRC-6 `src/inject/materialize.ts:175-205`; SRC-22 `type/map.computed-index.type.yaml:1-25`. Launch copies are generated files under the device's au-mcp gen tree, derived from graph instances and selection. They are not evidence of a second learned store. Research map indexes similarly compile retained article/question relations; rebuilding an index alone is not consolidation or synthesis. Implementation conclusion status: wired for launch; map contract is afforded, with its code inspected selectively.

> // Skills are launch-time-STATIC, the mirror of runtime-dynamic tools: a harness scans
> // its skill folders once at startup, so skills are written to DISK before launch rather
> // than riding the live MCP wire. See [[c - skills are launch-time-static the mirror of
> --- [src/skills/materialize.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/skills/materialize.ts#L3)

The research-map branch is the computed Index consumed by research/mediation; it reorganizes stored question/article relations, not the truth of their answers (SRC-22 `refresh-research-map.mjs`).

Additional parts of the retained graph (OBJ-3) separate content with different warrants. Their schemas/procedures are afforded; no produced instance is observed. All persist as typed files when authored.

| Object | Source-native part / form | Lineage; producer and consumer | Candidate truth-apt content / role | Evidence and limit |
|---|---|---|---|---|
| OBJ-8 | Imported `document` or `pdf` source note; natural-language conversion with typed capture/original metadata | Local raw bytes → converter wrapper → source readers and downstream extraction | Acquired document statements; metadata records capture date supplied by caller and original link | SRC-21 `converters/document.convert.mjs`, `converters/pdf.convert.mjs`, `ingest.mjs`; converter library fidelity uninspected, source truth unknown |
| OBJ-9 | Per-source extraction candidate (`note`, `surface`, `salience`, `passages`); natural-language interpretation plus typed fields | One source → mining agent → cut and weave agents; `of` and later passage links establish intended lineage | A statement of what this source says and how it treats a referent; faithful extraction is intended | SRC-14 `skills/mine.md`, `type/candidate.type.yaml`; semantic preservation depends on reading, not field presence |
| OBJ-10 | Woven `claim` and supporting/tension prose; natural-language proposition with graph links | Checked candidates across sources → weave/reweave agents → downstream graph consumers | Proposition with source grounds, qualified to evidence; deliberately no standing or contradiction adjudication | SRC-14 `type/claim.type.yaml`, `skills/weave.md`, `guides/the-argument-edge.md`; attribution can be removed in prose while lineage remains in extractions |
| OBJ-11 | Research `article` answer; natural-language synthesis and live `answers` relation | Question, external evidence and provisional model outline → research agent → readers, mediation, weave, competency design | Sourced findings, interpretations, arguments and author inferences must be distinguished; some possible inferences are ampliative | SRC-22 `skills/research.md`, `type/article.type.yaml`; no actual article instance inspected |
| OBJ-12 | Semantic `finding` body; natural-language defect claim with `subject`, `breaks`, optional `caught_by` | Independent reader catch checked against subject/doctrine → check agent → fix agent/human | “This subject violates this doctrine” plus evidence; verified defect claim, not merely a raw critic output | SRC-19 `skills/check.md`, `type/finding.type.yaml`; independent context and accuracy unobserved |
| OBJ-13 | Proposal's predicted remedy / causal rationale; natural-language “The change” and “Why,” linked `grounds` | Findings, corrections, research, contracts → propose agent → human and improve agent | Prediction that proposed mechanisms satisfy a requirement; possible ampliative mechanism/transfer claim | SRC-20 `skills/propose.md`, `type/proposal.type.yaml`; expected checks must be separate from observations |
| OBJ-14 | Operational requirements and dispositions: premise, question prompt, competency requirement, proposal ruling, lifecycle leaf, candidate verdict | Human/agent scope and judgments → typed records → workflow agents and graph query consumers | No truth-apt output in the state marker or normative requirement itself; operational scope, work selection and completion declarations | SRC-14 `skills/cut.md`; SRC-19 `type/finding.type.yaml`; SRC-20 `skills/derive.md`, `skills/improve.md`; SRC-22 `type/question.researched.type.yaml`; markers do not prove their declared history |
| OBJ-15 | Revised skill/rule/capability and its completion evidence; instructional or executable artifact plus separately interpreted observations | Approved proposal and checks → owning authoring capability/improve agent → intended future consumer | Policy update is not itself a truth-apt claim; completion evidence may support narrower behavior claims | SRC-20 `skills/improve.md`; SRC-18 `guides/eval-driven-authoring.md`, `guides/guarantee-vs-guidance.md`; no updated capability or trial observed |

### Routes

RTE-1 — ordinary host-launched agent invocation. Implementation conclusion status: wired. A human chooses workspace, adapter, profile and optional skill/inject selection; au-host resolves the configured executable and invokes the adapter launcher. The adapter materializes capabilities and returns a launch command. The external harness owns successive model calls, tool choices, delegation and final conversational output. In the Claude Code branch, PreToolUse asks the kernel to mediate, the MCP shim calls invoke, and PostToolUse reports effects. The kernel binds a launch handle to session identity, validates tool input, runs a plugin, records events and returns result content. Session profiles determine grants; absent restrictions mean broader availability, not an observed grant set. Sources: SRC-5 `app/src/main/agent-launch.ts:22-87`; SRC-9 `src/launch-cc.ts:59-77`, `hooks/pre-tool-use.ts:1-73`, `src/mcp-server.ts:177-201`; SRC-6 `src/daemon/daemon.ts:603-942`. Context/read-back and persistence are delegated to the integrated memory routes.

Immediate return: launch JSON or error, then tool result/error to the harness. Later read-back: retained workspace content and session recovery through the memory records; the final answer is not stored by this launcher. Delegated visibility: CC reports agent attribution within its session, whereas Codex uses child identity in its bridge; internal harness context inheritance remains uninspected. Selection: caller selections and profile; expiry: per launch/open, regenerated on later launch. Activation: tool effects are wired; influence on the model's final choices remains uninspected. Recovery: launcher failure returns error; tool reconnect and session recovery are separate routes. Operating mode: open user requests, with optional bounded procedures supplied as skills. There is no supplied expected-answer oracle for arbitrary requests; model judgment does not establish one.


> const child = spawn(paths.node, args, { cwd: adapter.dir, env: process.env })
> --- [pinned source](https://github.com/arsumbris/au-host/blob/0e85fb1731fdef2d6196618aff5a2a567e621866/app/src/main/agent-launch.ts)

> const { result, isError } = await client.invoke(handle, `mcp.${name}`, args)
>       return ok(result, isError)
> --- [pinned source](https://github.com/arsumbris/au-mcp-adapter-cc/blob/333b2117f338cd4815eeeb9ab7b3932b29fa7d62/src/mcp-server.ts)

RTE-2 — ordinary file change admission. Implementation conclusion status: wired. Trigger: a write/edit/delete request proposed by an agent, human-driven client or plugin. Admission is split: profile/continuity and input schema in invoke; read-before-write and native redirects in separately requested mediation; path guards in file tools; optional content-hash comparison and exact replacement in engine mutation. SRC-6 `src/daemon/daemon.ts:830-920`; SRC-8 `src/read-guard.ts:76-100`, `src/file-tools.ts:239-319`; SRC-2 `crates/au-engine/src/mutate.rs:45-145`, `crates/au-engine/src/serve.rs:3970-4020`.

The engine performs the filesystem effect, folds metadata, commits or compensates through its saga wrapper and rebuilds the graph. An expected hash guards only callers supplying it; the pre-call read check is not a universal atomic protection against outside writers. Wrong shape, disallowed path or stale supplied hash can reject a request. Validation diagnostics about resulting knowledge remain advisory. Immediate return: mutation result/hash/commit or refusal. Persistence: file bytes and eligible Git history. Read-back: subsequent graph/content consumers (memory routes). Delegation sees shared files through its own reads. Selection: explicit target path; invalidation: later edit/delete plus graph rebuild. Recovery: re-read/retry after stale rejection; compensation route on mutation commit failure, with crash-recovery completeness uninspected. Guarantee owner: plugin/kernel/engine at their respective seams; strength: protocol within these channels, no deployment isolation guarantee.

Guidance is current prompt/skill/rule content plus symbolic API conditions, not a hardcoded universal improvement objective. Proposal and semantic evaluation belong to the invoking agent or human; the code can veto malformed operations but does not select a semantically better candidate. Answer oracle: input schema and current hash for structural/consistency checks, supplied by type declarations and live disk; no reference answer for content truth. Formulated theory, operative application, content-directed criticism, resulting revision and improved capacity each have conclusion status: uninspected for an arbitrary write. The knowledge-workflow records assess the narrower routes where guidance is inspectable. Generic storage retains what was written, not necessarily a reason or criticism.


> //! Rejection is for malformed requests only (path escape, hash mismatch,
> //! missing `old_string`); a mutation never rejects because the result has
> //! validation errors — diagnostics stay advisory.
> --- [pinned source](https://github.com/arsumbris/au-engine/blob/46f12389d4d4833fed51640a48cf938516433106/crates/au-engine/src/mutate.rs)

> if let Some(expected) = expected_hash {
>         match std::fs::read(target) {
>             Ok(current) => {
>                 let current_hex = hash_hex(ContentHash::of(&current));
>                 if current_hex != expected {
> --- [pinned source](https://github.com/arsumbris/au-engine/blob/46f12389d4d4833fed51640a48cf938516433106/crates/au-engine/src/mutate.rs)

> blocking_handle.rebuild_paths(saga_dirty_set(&plan));
> --- [pinned source](https://github.com/arsumbris/au-engine/blob/46f12389d4d4833fed51640a48cf938516433106/crates/au-engine/src/serve.rs)

RTE-3 — admit executable extensions and operational configuration. Implementation conclusion status: wired. Mounted type definitions name a module entry and declare contract version and broker access. Discovery checks contract equality, imports the module in-process and requires createPlugin. A failed critical plugin prevents serving or poisons the daemon; noncritical version/load failures are skipped. Profiles then select which registered tools and hooks apply. SRC-6 `src/daemon/discovery.ts:307-400`, `src/daemon/daemon.ts:603-616,691-722`; `src/daemon/broker.ts:105-135`. The proposer is the package author or editing agent/human; the loader makes structural admission decisions, while the operator controls mounting. Its oracle is a required contract integer/export shape, not a behavioral reference result. Guidance includes SDK contracts and editable metadata, symbolic and inspectable by field; no evidence-responsive code improvement follows merely from passing these checks.

Immediate return: registered capability or refusal/warning. Persistence: package source and configuration; registry is live daemon state. Later consumers: tool listing, invoke and phase hooks; reloading a changed package in an already running daemon is not established by this inspection. Delegated visibility: profile- and session-dependent. Selection: discovered typed definitions; invalidation/recovery: corrected package/configuration and fresh discovery/restart, automatic rollback to a previously good plugin is uninspected. Runtime-entry metadata represents the system's own available operations and changes its later callable behavior, supporting reflection relative to this aspect, with refresh timing bounded as above.

Broker scoping is an API grant, not an OS sandbox: imported module code has ambient process privileges. Native shell tools (when the profile allows them), direct engine clients and host edits are alternate effect paths. The first-party mcp.bash callable is a stub, so it does not itself execute shell commands (SRC-8 `src/file-tools.ts:560-567`). The host separately launches an actual terminal process (SRC-5 `app/src/main/terminal.ts:99-114`). Source claims of arbitrary code execution and absent sandboxing are explicit in SRC-1 `SAFETY.md:5-27`; the import confirms in-process extension loading. Guarantee strength: contract protocol and policy, not deployment isolation.


> const module = (await import(pathToFileURL(entryPath).href)) as Partial<PluginModule>
> --- [pinned source](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/discovery.ts)

> if (derived.manifest.contractVersion !== PLUGIN_CONTRACT_VERSION) {
>       const msg = `plugin contract v${derived.manifest.contractVersion} != kernel-expected v${PLUGIN_CONTRACT_VERSION}`
>       if (derived.manifest.critical) failedCritical.push({ id: derived.manifest.id, error: msg })
>       else process.stderr.write(`au-mcp: skipping ${derived.manifest.id}: ${msg}\n`)
>       continue
>     }
> --- [pinned source](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/discovery.ts)

> This is an early alpha. There is **no security hardening or sandboxing** in place.
> --- [pinned source](https://github.com/arsumbris/arsumbris/blob/a9f6cceedb191b8504443222d55d3106f9f36ba9/SAFETY.md)

> const bashTool = callable('mcp.bash', 'Bash', async (_input) => ok(BASH_STUB_MESSAGE))
> --- [pinned source](https://github.com/arsumbris/au-mcp-core/blob/25e0625e553c237671bba9a3a8c173a889dddf02/src/file-tools.ts)

RTE-4 — Claude Code mediation failure and direct-invoke alternative. Implementation conclusion status: wired. The ordinary hook runs a separate mediate request, returning an allow fallback when its connection/session operation fails. The typed MCP call still needs a reachable daemon, but native actions do not gain a fail-closed guarantee from that typed-tool dependency. A direct daemon invoke independently checks tool visibility, continuity and input shape; its inspected branch does not execute the separate mediator chain. Session-less invokes have no profile allowlist. This limits the otherwise broad “every state-touching action” framing in the MCP instructions. SRC-9 `src/bridge.ts:130-153,218-233`, `hooks/pre-tool-use.ts:1-73`, `src/mcp-server.ts:40-45`; SRC-6 `src/daemon/daemon.ts:754-778,830-920`.

Next-step owner: external harness or direct client. Immediate return: allow/deny/ask/inject for hook or invoked result for direct client. Effects: those of the selected native or plugin operation; persistence and read-back depend on that operation. Delegated visibility: CC passes agent IDs as event attribution, not evidence of isolated child grants. Selector: native allowlist is inert when absent; no expiry beyond current session. Activation: protocol response is wired, deployed harness compliance unobserved. Recovery: restore daemon and retry; fallback intentionally favors continuing the CC session. Guarantee strength: best effort for hook mediation across outages, protocol for the checks inside invoke. Required external contract: correctly installed/executed harness hooks. No epistemic license or answer oracle is conferred.


> return withSession(payload, (client, session) => client.mediate(session, action), { kind: 'allow' })
> --- [pinned source](https://github.com/arsumbris/au-mcp-adapter-cc/blob/333b2117f338cd4815eeeb9ab7b3932b29fa7d62/src/bridge.ts)

> if (!isAllowed(invSession?.toolAllowlist, request.tool)) {
> --- [pinned source](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/daemon.ts)

> if (allowlist === undefined) return { kind: 'allow' } // no allowlist -> inert (all native allowed)
> --- [pinned source](https://github.com/arsumbris/au-mcp-core/blob/25e0625e553c237671bba9a3a8c173a889dddf02/src/native-tool-redirect.ts)

RTE-5 — Codex mediation and child identity alternative. Implementation conclusion status: wired. The Codex bridge resolves agent_id before session_id, asserts a launch session, opens the kernel session and denies when mediation fails. Startup delivery has explicit readiness tracking. SRC-10 `src/bridge.ts:30-67,108-130,159-165`. This is an implemented difference from RTE-4; it does not establish provider- or machine-wide isolation. The external Codex process still owns model turns, subagent scheduling and whether the registered hooks run. Trigger: tool hook/startup event; policy: symbolic session and connection guards; context: launch/profile and kernel context. Immediate return: decision or error guidance. Persistence/read-back: session bookkeeping and generated context in memory records; no new knowledge is produced by denying a tool. Delegated visibility: separate child IDs, not proven separate model memory. Selection: launch handle/thread identity; expiry: readiness/connection lifecycle. Recovery: restore daemon/session then retry. Guarantee owner: adapter error handler, protocol strength within this hooked route. Answer oracle and learning assessment are inapplicable to transport failure handling.


> catch (error) { report(error); return { kind: 'deny', reason: 'Arsumbris mediation could not complete. The action was blocked; restore the daemon/session connection before retrying.' } }
> --- [pinned source](https://github.com/arsumbris/au-mcp-adapter-codex/blob/3b0e3a3cf67b3143819c61c590efc85d36c23bc5/src/bridge.ts)

#### RTE-6 — Author and request graph content

A human editor or agent supplies text; the host and MCP tool call the engine mutation channel, which writes files and rebuilds its view. An agent later requests read_file_pinned or typed graph tools; the consumer receives requested text/structured results. Pinned reads return the content hash and current commit so a subsequent write can preserve an anchor; the read itself does not save a citation. SRC-5 `app/src/main/engine-connections.ts:140-157`; SRC-8 `src/file-tools.ts:184-264`; SRC-8 `src/tool-au-neighborhood.ts:1-6`. Read requests support range limits and clipping, so a delivered excerpt need not be the complete file. Implementation conclusion status: wired.

>       // The engine anchors the read: `commit` is the repo HEAD the working-tree
>       // read was taken at, `hash` the content hash. Surfacing them lets the caller
>       // pin the exact version it read as [[path::@commit]] — via a SUBSEQUENT write;
>       // the read itself records nothing.
>       if (typeof result.commit === 'string') anchorCommit = result.commit
>       if (typeof result.hash === 'string') contentHash = result.hash
> --- [src/file-tools.ts](https://github.com/arsumbris/au-mcp-core/blob/25e0625e553c237671bba9a3a8c173a889dddf02/src/file-tools.ts#L209)

>   async writeFile(
>     entryPath: string,
>     filePath: string,
>     content: string,
>     expectedHash?: string,
>   ): Promise<FileWriteResult> {
>     return this.mutate(entryPath, (client) => client.writeFile(filePath, content, { expectedHash }))
> --- [app/src/main/engine-connections.ts](https://github.com/arsumbris/au-host/blob/0e85fb1731fdef2d6196618aff5a2a567e621866/app/src/main/engine-connections.ts#L151)

#### RTE-7 — Source-grounded graph growth and maintenance

The external agent following mine/cut/weave/reweave/tend turns sources into candidates, reuses or authors canonical nodes, enriches existing nodes, and builds maps. Source passages, the cut's reasons and candidate dispositions remain separately addressable. Later reweave reads the retained reason as well as source and candidate. Risky merges, pruning and retirement are held for human review; successors preserve the older identity and require consumers to interpret the chain. SRC-14 `skills/weave.md:18-87`; SRC-14 `skills/reweave.md:33-74,97-108`; SRC-14 `skills/tend.md:55-128`; SRC-15 `guides/base-layer/supersede.md:28-60`; SRC-22 `skills/research.md:84-121`. Procedure conclusion status: afforded. Manual supersession withdraws reliance semantically; the engine does not automatically redirect old references.

> Read each selected node in full.
> For an enrichment, compare its content with:
> 
> - The source
> - The candidate note
> - The cut's reason
> 
> Read the target kind's fields and writing guidance.
> Fold related facets into one revision serving the premise and target's purpose.
> Use the cut's target.
> Preserve its required structure and accurate prose.
> --- [skills/reweave.md](https://github.com/arsumbris/au-weave/blob/24320734e2436e8c75d44a7ff9afb6a330569840/skills/reweave.md#L35)

> **Interpret the chain explicitly**
> 
> Existing inbound links still reach the old note.
> The engine neither redirects them nor follows the successor chain automatically.
> A reader or consumer must interpret the relation.
> 
> To find the current version, query within the intended versioned family and check the chain.
> A missing successor field alone does not make every node current.
> --- [guides/base-layer/supersede.md](https://github.com/arsumbris/au-agent-guides/blob/ddc33339c73278ed2b9a178030d9d94924e43224/guides/base-layer/supersede.md#L28)

> A successful write or clean diagnostics alone cannot establish this.
> Save checked, distinct links in `passages` before writing the node.
> If an anchor cannot be created or checked, leave the candidate pending and report why.
> --- [pinned source](https://github.com/arsumbris/au-weave/blob/24320734e2436e8c75d44a7ff9afb6a330569840/skills/weave.md)

> #: sharpened no further than the evidence reaches, so it records the claim without judging its truth. Grounded IN
> #: its sources (the grounds edge + free backlinks), not narrated FROM them. Every link in the sentence that says why,
> #: no relation stronger than the sources show.
> --- [pinned source](https://github.com/arsumbris/au-weave/blob/24320734e2436e8c75d44a7ff9afb6a330569840/type/claim.type.yaml)

> #: Standing and contradiction-resolution are downstream, not here.
> --- [pinned source](https://github.com/arsumbris/au-weave/blob/24320734e2436e8c75d44a7ff9afb6a330569840/type/claim.type.yaml)

> Mark `weave` when the candidate earns a distinct node of its intended kind that the graph lacks.
> A facet with its own use and query earns a sibling.
> --- [pinned source](https://github.com/arsumbris/au-weave/blob/24320734e2436e8c75d44a7ff9afb6a330569840/skills/cut.md)

#### RTE-8 — Interaction feedback to later guidance

A selected capture-correction inject supplies the correction rule (SRC-19 `profiles/capture-correction.md:2-14`). During work, the instructed agent creates OBJ-6 from feedback. A later improve/derive task pulls relevant corrections, groups recurrence, retains dispositions and reasons, and chooses an approved remedy. Skill/rule authorship then saves guidance, checks discovery and requires profile bundling or launch refresh before later callers can consume it. This chain is an afforded automatic trace-fed write route with human adoption decisions, not a daemon-enforced loop. SRC-20 `skills/improve.md:17-29,38-90`; SRC-18 `skills/write-a-skill.md:18-44`; SRC-18 `guides/gotchas-first.md:9-18`; SRC-17 `skills/write-a-rule.md:33-68`. A second afforded branch revises skills using selection traces and representative tasks. Its trace format and timing are unspecified.

> Start from the caller's scope and existing work.
> Read relevant findings and corrections, including reviewed corrections that establish recurrence.
> Reuse current evidence until relevant state changes or freshness is uncertain.
> Use qualified family queries when discovery is needed.
> Page completely before claiming coverage or absence.
> 
> Group findings by breaks.
> Follow recurs to the original correction.
> Set a missing recurs link when a return is recognized.
> A backlink count alone does not establish recurrence.
> 
> Mark an assessed correction reviewed when no action is pending.
> Preserve the feedback and record the reason there.
> --- [skills/improve.md](https://github.com/arsumbris/au-competency/blob/6f23713425b2ba58b7361471badd58f63ca0642b/skills/improve.md#L17)

> When a run exposes a mistake in the procedure, revise the step that led to it.
> Give the next caller enough information to recognize the situation and choose the correct action.
> Label an anticipated problem as a possibility until it has been observed.
> --- [guides/gotchas-first.md](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/gotchas-first.md#L9)

> **Trim from evidence**
> 
> Use available selection traces and representative tasks to identify redundant guidance.
> Low usage alone does not establish that a skill is useless.
> Check whether the task is rare or the description prevents it from being selected.
> 
> A self-authored skill needs the same evidence as a borrowed one.
> Use [[when-a-skill-helps]] to identify its contribution.
> Use [[eval-driven-authoring]] when that contribution needs measurement.
> --- [guides/curate-dont-accumulate.md](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/curate-dont-accumulate.md#L29)

The correction retains reasons for the requested change, and improve explicitly reads them. Gotcha guidance retains the symptom and mistaken action beside the corrected step. A writing-rule body must explain the move, but the contract does not require copying the original correction's full rationale or making the future runtime read its provenance. Reason retention therefore differs between the correction record, the adopted rule and a code remedy.

> goal: Place advice about a known mistake at the decision where it can prevent a repeat.
> rule: Describe the symptom, the mistaken action and the correction beside the affected step.
> --- [guides/gotchas-first.md](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/gotchas-first.md#L3)

> **Check delivery**
> 
> Check the profile's diagnostics and generated launch output.
> An unbundled rule stays inert.
> --- [skills/write-a-rule.md](https://github.com/arsumbris/au-writing-style/blob/163b5597583364649b0bd896575ae4167e436719/skills/write-a-rule.md#L65)

> Capture a recurring correction as one reusable `writing-rule`.
> 
> The title names the move.
> The body explains how to make it.
> 
> A rule becomes active when a profile's `rules` field names it.
> Writing and bundling are separate steps.
> --- [skills/write-a-rule.md](https://github.com/arsumbris/au-writing-style/blob/163b5597583364649b0bd896575ae4167e436719/skills/write-a-rule.md#L9)


> Capture feedback that changes how the agent should work as a `correction.open`.
> Keep ordinary task choices and changes of scope in the current work.
> 
> Record the behavior that drew the correction under `What I did`.
> Record the desired behavior under `What they wanted`, using the person's words where useful.
> 
> When the friction repeats a known correction, set `recurs` to its original occurrence.
> Follow an existing recurrence chain to its root.
> The relation preserves which friction returned.
> 
> A useful correction lets a future agent recognize the situation and choose the better behavior.
> --- [rules/capture a correction when the human redirects you.md](https://github.com/arsumbris/au-govern/blob/8bf899b90a80081f328caacb0102ed47145b242d/rules/capture%20a%20correction%20when%20the%20human%20redirects%20you.md#L9)


#### RTE-9 — Automatic launch selection and delivery

At launch, au-mcp discovers typed injects with member ownership and role. Exact owner:name selections override the default entry/edit set; dependency/discovery members require opt-in. Selected graph seeds expand through outgoing references to configured depth/kinds; node bodies or full files become blocks. This automatically pushes accumulated/revised content to a later agent without its content request. Static unchanged shipped injects are excluded from the memory comparison even though they use the same machinery. SRC-6 `src/inject/discover.ts:104-169`; SRC-6 `src/inject/materialize.ts:175-205`; SRC-6 `src/inject/expand.ts:49-76`; SRC-9 `src/inject-cc.ts:10-19,31-71`; SRC-10 `src/inject-codex.ts:11-41`; SRC-10 `hooks/session-start.ts:9-17`. Implementation conclusion status: wired.

>   // The OPEN model (agent-profile): an explicit selection is EXACT — it names precisely which
>   // injects fire, and naming a `dep`/`discover` inject is how a human opts that consumed one in.
>   // No selection is the role-scoped DEFAULT SET: only the editable authoring surfaces
>   // (`entry`/`edit`), so a bare launch never runs a dependency's standing context.
>   const select = options.select
>   const injects = select
>     ? discovered.filter((i) => select.includes(injectKey(i)))
>     : discovered.filter(inDefaultSet)
> --- [src/inject/materialize.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/inject/materialize.ts#L181)

>   const delivery = await recoverStartupContext(payload)
>   if (delivery.context) { outputAttempted = true; await emitHookOutput({ hookSpecificOutput: { hookEventName: 'SessionStart', additionalContext: delivery.context } }) }
>   markStartupContextEmitted(delivery)
> --- [hooks/session-start.ts](https://github.com/arsumbris/au-mcp-adapter-codex/blob/3b0e3a3cf67b3143819c61c590efc85d36c23bc5/hooks/session-start.ts#L15)

CC packs into 8,500-character slots; its default has no total slot cap, while an optional cap reports dropped whole blocks. Codex's optional byte budget counts envelopes and overflow notices and drops whole blocks. These are context-volume controls, not relevance learning. Exact profile keys and reference traversal are identifier selection; default member role and total budgeting are coarse selection. Live repository overview additionally pushes current editable README tldr content, discovery names and dependency counts at session open (SRC-8 `src/repo-overview.ts:3-18,68-111`). Graph pull interfaces and skill descriptions leave content choice with the requesting agent/harness; no inferred-embedding or inferred-judgment push selector was found in these paths.

#### RTE-10 — Session capture, recovery and consultation

The daemon appends stamped events, persists emitted governance facts, and reloads the appropriate session on open/resume. consultTrace is an afforded pull interface for named mediators and callable plugins; the release wiring supplies its closure but the cited external workflow mediator is outside scope. This establishes continuity storage and replay availability, not successful learned behavior or an instantiated external step-gate. Resume selection uses session identity, not inferred task similarity. The kernel age sweep forgets dormant stores after the configured window (default 30 days) and orphan stores after one day. SRC-6 `src/daemon/daemon.ts:181-189,344-364,624-675`; SRC-6 `src/daemon/crash-recovery.ts:237-263`. Implementation conclusion status: wired for retention/recovery; consumer consultation conclusion status: afforded.

>    * The `consultTrace` closure over one session's live log — the single source for the read a
>    * mediator gets (MediationContext), a callable gets (CallableContext), and the consult-trace
>    * wire case returns. Factored so the three paths cannot drift on the slice shape.
>    */
>   function makeConsultTrace(session: Session): ConsultTrace {
>     return async (query) => ({ events: queryLog(session, query), headSeq: sessions.headSeq(session.id) })
>   }
> --- [src/daemon/daemon.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/daemon.ts#L344)

>   for (const s of listSessions(workspace)) {
>     const window = s.dormant ? opts.dormantWindowMs : opts.orphanWindowMs
>     if (s.lastActiveMs > 0 && now - s.lastActiveMs > window) {
>       retire(s.id)
>       retired.push(s.id)
>     }
> --- [src/daemon/crash-recovery.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/crash-recovery.ts#L250)

>         // A clean close leaves the session DORMANT, not gone. Its governance slice + run record are
>         // KEPT (for resume rehydration) and only `retire` clears them; here we just flag dormancy and
>         // preserve the run index as the resume marker, so a later open bumps the run (resume) rather
>         // than reusing it. The orphan age-sweep bounds a session that never resumes.
>         markSessionDormant(opts.workspace, request.session)
> --- [src/daemon/daemon.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/daemon.ts#L738)


#### RTE-11 — Auxiliary current-run access gating and freshness (outside memory profile)

Reads/served content update OBJ-4. At a later mediated overwrite, the read-guard compares the session's read hash with current content and can deny stale/unread overwrites. This is enforcement authority carried by current-run access metadata, not proof the agent understood the file or a later invocation received retained memory. OBJ-4 and this route are excluded from all normalized memory axes. It depends on the separate mediation call; invoking a write tool alone does not prove the guard ran. Explicit expected_hash reaches the engine check, whose absence allows an unconditional write. A changes subscription invalidates held hashes and pushes affected paths on the next tool result. SRC-8 `src/read-guard.ts:77-96`; SRC-2 `crates/au-engine/src/mutate.rs:102-142`; SRC-6 `src/daemon/freshness.ts:45-97`. Implementation conclusion status: wired, limited to the mediated path and advisory freshness route.

>     const seen = ctx.readHash(path)
>     if (seen === undefined) {
>       return deny(ctx, action, `read ${path} through the gate before overwriting it (read-before-write)`)
>     }
>     const now = await currentContentHash(ctx.broker, path)
>     if (now !== null && now !== seen) {
>       return deny(ctx, action, `${path} changed on disk since you read it — re-read it before overwriting (read-before-write)`)
>     }
> --- [src/read-guard.ts](https://github.com/arsumbris/au-mcp-core/blob/25e0625e553c237671bba9a3a8c173a889dddf02/src/read-guard.ts#L88)

>         if (s.readView.has(path) && s.readView.get(path) !== current) {
>           s.readView.delete(path)
>           invalidated = true
>         }
>         if (s.servedView.has(path) && s.servedView.get(path) !== current) {
>           s.servedView.delete(path)
>           invalidated = true
> --- [src/daemon/freshness.ts](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/freshness.ts#L62)

#### RTE-12 — Import originals as readable source notes

The ingest tool runs a format converter over a retained original, previews its typed result and writes a Markdown source note through the engine. Existing different content is preserved unless refresh is requested; source and destination hashes guard refresh races. A later weave/research agent consumes the source through RTE-6 and RTE-7. Originals remain separate from derived readable notes. Conversion is automatic acquisition, not trace learning or semantic consolidation. SRC-21 `README.md:13-15,43-60`; SRC-21 `ingest.mjs:194-240,253-278`. Implementation conclusion status: wired; specific later knowledge-task execution is afforded.

>       const before = await snapshot(broker, plan.path);
>       const derived = await runConverter({
>         module: converter.module, converter: converter.qualified, date: input.date,
>         rawPath: plan.rawPath, destination: plan.path, rawRef: plan.rawRef,
>       }, Math.max(1, Math.min(LIMITS.conversionMs, deadline - performance.now())));
>       const content = derived.source;
>       if (before && before.text !== content && !input.refresh) {
>         Object.assign(item, { status: 'conflict', hash: before.hash, error: 'existing note preserved; use refresh: true to replace its full content' });
>         continue;
> --- [ingest.mjs](https://github.com/arsumbris/au-ingest/blob/5b3c22f930231ed12c964dce0144a35b5562ef9d/ingest.mjs#L208)

>   if (diagnostics.some((diagnostic) => diagnostic.severity === 'error')) {
>     throw Object.assign(new Error('converted note has structural errors; nothing written'), { diagnostics });
>   }
> --- [pinned source](https://github.com/arsumbris/au-ingest/blob/5b3c22f930231ed12c964dce0144a35b5562ef9d/ingest.mjs)

>       if (hashOf(readRaw(plan.rawPath)) !== derived.rawHash) throw new Error('raw changed during conversion; nothing written');
> --- [pinned source](https://github.com/arsumbris/au-ingest/blob/5b3c22f930231ed12c964dce0144a35b5562ef9d/ingest.mjs)

>         // An unreflected acknowledgement has stale metadata. A lost acknowledgement
>         // may have committed. A live read can confirm bytes, but not index validation.
> --- [pinned source](https://github.com/arsumbris/au-ingest/blob/5b3c22f930231ed12c964dce0144a35b5562ef9d/ingest.mjs)

#### RTE-13 — Recompute a research navigation index

Implementation conclusion status: wired for the inspected refresh plugin; procedure conclusion status: afforded for the research agent’s choice to invoke it.

A research agent saves an article and answer link; refresh_research_map derives navigation from question parent relations and writes the Index section. Other sections and frontmatter survive; terminal question branches are suppressed according to the contract. A later reader/agent follows this map to retained articles and unfinished work. This is symbolic compilation and routing; the research article itself is agent-authored synthesis. SRC-22 `type/map.computed-index.type.yaml:1-25`; SRC-22 `refresh-research-map.mjs:10-55`; SRC-22 `skills/research.md:84-121`. Procedure conclusion status: afforded. No claim of index correctness rests on executing it.

> #: A computed tree of articles and open questions rooted at one premise.
> #: refresh_research_map derives it from the engine and writes through engine mutations.
> #: Refresh replaces only Index contents, preserving frontmatter, the heading and other sections.
> #: Question parents determine nesting; researched and dropped question entries and tldrs are hidden.
> #: An open question and any answers share one row, with descendants beneath it.
> #: The map inherits map::au-base-types for navigation discovery.
> --- [type/map.computed-index.type.yaml](https://github.com/arsumbris/au-tree-research/blob/65faf72fc107bb8eef84675e01bda18513d8b49a/type/map.computed-index.type.yaml#L1)

#### RTE-14 — Research an answer and update the research agenda. Procedure conclusion status: afforded. SRC-22 `skills/research.md`, `skills/mediate.md`, `type/question.researched.type.yaml`; SRC-20 `skills/self-research.md`. A user/question premise triggers an instructed research agent to gather sources, develop OBJ-11, check consequential claims and plausible alternatives, save/review the article and mark the question researched only after the answer exists. The agent proposes and evaluates content; a later mediation task ranks follow-up questions. Human scope controls the task. Expected answers are not generally supplied: external sources provide evidence, while model judgment is the semantic evaluator. Typed completion is a declaration, not a history check. The process can preserve explanations and inferences; no specific operative theory or improved capacity is observed. Retained article/reference/answer links supply later source and inquiry consumers. Recovery is to keep incomplete work open or revise the article; reverting an inadequate conclusion remains an agent/human decision. Guarantee strength: policy.

> Cross-check consequential or disputed facts against independent evidence where available.
> Test interpretations and arguments against plausible alternatives.
>
> Distinguish sourced findings, your inferences and illustrative examples.
> Never invent specifics or imply certainty the evidence does not support.
> --- [pinned source](https://github.com/arsumbris/au-tree-research/blob/65faf72fc107bb8eef84675e01bda18513d8b49a/skills/research.md)

> #: The workflow checks that a reviewed answer exists before recording completion.
> #: This type alone does not establish that an answer exists.
> --- [pinned source](https://github.com/arsumbris/au-tree-research/blob/65faf72fc107bb8eef84675e01bda18513d8b49a/type/question.researched.type.yaml)

#### RTE-15 — Check and repair a semantic finding. Procedure conclusion status: afforded. SRC-19 `skills/check.md`, `skills/fix.md`, `type/finding.type.yaml`, `type/finding.accepted.type.yaml`. A review request triggers a fresh reader to propose OBJ-12 against actual subject/doctrine. The checking agent verifies each catch before admitting repair work. The fix agent changes the subject, repeats the original check and records the result. A human can approve a scoped exception or dismiss a finding; finding.accepted records an exception, not repair success. Guidance and answer reference: the named doctrine, supplied by the workspace/owning author; it governs conformity but is not an independent oracle for the doctrine's truth. Retained finding/evidence and revised subject are later repair/operation inputs. Rejection is unsupported catch or unresolved check; recovery leaves work open, preserves reasons or follows a human ruling. Content-directed criticism of a subject is afforded; criticism of the doctrine itself and improved later capacity are uninspected. Guarantee strength: policy, not enforced lifecycle transitions.

> Check each reader catch against the subject and doctrine before recording it.
> A reader can lack context.
> An unsupported finding can prompt a harmful repair.
> --- [pinned source](https://github.com/arsumbris/au-govern/blob/8bf899b90a80081f328caacb0102ed47145b242d/skills/check.md)

> #: The engine checks compatible claims, not transition history.
> --- [pinned source](https://github.com/arsumbris/au-govern/blob/8bf899b90a80081f328caacb0102ed47145b242d/type/finding.type.yaml)

> #: Acceptance records an exception, not a repair.
> --- [pinned source](https://github.com/arsumbris/au-govern/blob/8bf899b90a80081f328caacb0102ed47145b242d/type/finding.accepted.type.yaml)

> Repeat the check that exposed the defect.
> Use the audit named by caught_by, or the documented direct check when no audit produced the finding.
> Do not invent an audit to close the record.
>
> Keep the repair and observed result on the finding.
> If the defect remains or the check cannot be completed, leave it open with the remaining work.
> --- [pinned source](https://github.com/arsumbris/au-govern/blob/8bf899b90a80081f328caacb0102ed47145b242d/skills/fix.md)

#### RTE-16 — Derive, approve, implement and assess a capability change. Procedure conclusion status: afforded. SRC-20 `skills/derive.md`, `skills/propose.md`, `skills/improve.md`, `type/proposal.type.yaml`; SRC-18 `guides/eval-driven-authoring.md`, `guides/guarantee-vs-guidance.md`. Recurring corrections, verified findings or corroborated research motivate a proposed remedy (OBJ-13) to a stated requirement (OBJ-14). The agent diagnoses, compares candidate mechanisms and proposes; the human rules on implementation scope and may veto; an instructed author implements within that scope, checks the intended consumer, and keeps unmet obligations open. No automatic scheduler or measured improvement is asserted. Approval is operational permission; successful completion demands evidence of the promised behavior, not just a saved artifact.

Guidance can be a normative rule, procedure, theory about why a remedy works, or executable contract; the record's label does not decide which. Reasons and expected checks are separately inspectable in a proposal's Why/grounds/change fields, while retained corrections preserve feedback and later improve reads them (RTE-8). Theory formulation conclusion status: afforded for a proposed explanatory/predictive rationale; operative use conclusion status: afforded when that rationale guides candidate comparison and checks; content-directed criticism conclusion status: afforded where alternatives or failed predicted behavior challenge it; resulting revision or changed reliance conclusion status: afforded through corrective revision/keeping work open; improved capacity attributable to criticism conclusion status: uninspected. These are route capacities, not observed instances. No opaque model reasoning is inferred to contain or lack formulation/criticism. Addressability is afforded at named assumptions, scope, grounds, proposal sections and skill steps; whole-replacement revisions remain possible. Retention covers correction, proposal, disposition, remedy and check record; later instruction use requires RTE-9 or explicit skill selection.

Answer-oracle access: the operator/evaluation designer can specify expected task outcomes before a skill trial; the release supplies evaluation guidance, not task answers. A human preference licenses intended behavior, not a causal claim that the remedy will produce it. Trial comparison, when needed, uses comparable tasks/model/environment with and without a skill; no such execution is evidence in this run. Operating modes include open improvement requests and optional bounded skill trials, not an implemented automatic curriculum. Adoption can precede efficacy checking, so instruction activation is not post-acceptance integration. Recovery is continued repair under approved scope, an open proposal, or renewed human ruling for material scope change; no universal automated rollback or successor selector is established. Guarantee strength: policy.

> Use the human's recorded ruling and approval already given in the session.
> Silence grants no approval.
> Resolve ordinary implementation choices within that scope.
> Return a material scope change through propose for a ruling.
> --- [pinned source](https://github.com/arsumbris/au-competency/blob/6f23713425b2ba58b7361471badd58f63ca0642b/skills/improve.md)

> Match checks to the promised behavior.
> A prevention claim needs an exercised boundary.
> A semantic claim needs judgment against its doctrine.
> --- [pinned source](https://github.com/arsumbris/au-competency/blob/6f23713425b2ba58b7361471badd58f63ca0642b/skills/improve.md)

> Keep the proposal accepted while promised behavior remains unproven.
> Name the remaining obligation and next action.
> Continue independent approved work where possible.
> Never weaken a requirement to make completion appear true.
> --- [pinned source](https://github.com/arsumbris/au-competency/blob/6f23713425b2ba58b7361471badd58f63ca0642b/skills/improve.md)

> Choose tasks and expected outcomes before revising the skill.
> Keep the model and environment comparable across runs with and without it.
> --- [pinned source](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/eval-driven-authoring.md)

> A check that passes with and without the skill can still protect required behavior.
> It does not demonstrate the skill's added value.
> --- [pinned source](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/eval-driven-authoring.md)

> Enforcement also needs a path that runs the check and refuses the invalid action.
> --- [pinned source](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/guarantee-vs-guidance.md)

> A script invoked only at the agent's discretion can be skipped.
> --- [pinned source](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/guides/guarantee-vs-guidance.md)

> Choose checks for the change:
> 
> - For a new skill or a changed task boundary, try requests it should own and similar requests it should leave to another skill.
> - For a procedure change, check the affected task result. Use [[eval-driven-authoring]] for a new skill's baseline or when its added value is uncertain.
> - For a delivery change, inspect discovery and the intended launch artifact through [[author-a-skill]].
> 
> Reuse evidence while its task, model and environment remain applicable.
> --- [skills/write-a-skill.md](https://github.com/arsumbris/au-skills/blob/d32336d25b6ad2513976cba15ed69f30d6d1b38f/skills/write-a-skill.md#L28)

### Claims

CLM-1 — source describes a “malleable, agent-native IDE for typed knowledge” and shared primitives for extending tools, views and the app. Claim conclusion status: claimed; extension/typed-file substrate conclusion status: wired through RTE-1, RTE-2, RTE-3. SRC-1 `README.md:6-18`. No observed end-user productivity improvement is established.


> You and your agent can build tools, add views and modify the app with the same primitives and SDKs we used to build it.
> --- [pinned source](https://github.com/arsumbris/arsumbris/blob/a9f6cceedb191b8504443222d55d3106f9f36ba9/README.md)

CLM-2 — the Claude Code shim tells agents that state-touching actions are governed and traced. Claim conclusion status: claimed. SRC-9 `src/mcp-server.ts:40-45`. Supported only conditionally: RTE-1 and RTE-2 implement checks and observation on ordinary hooked calls; RTE-3 and RTE-4 prevent upgrading this to a universal invariant. There is no observed deployment supporting universal coverage.


> State-touching actions (writes, edits, deletes) route through the gate, so every one is governed and traced.
> --- [pinned source](https://github.com/arsumbris/au-mcp-adapter-cc/blob/333b2117f338cd4815eeeb9ab7b3932b29fa7d62/src/mcp-server.ts)

The following claimed procedures retain conclusion status: claimed for their purpose; executable imports/navigation are wired and instructed semantic procedures afforded as recorded in the cited routes. No observed-run or causal support is inferred from source instructions.

| Claim | Claimed operation and source | Doctrine/design support | Implemented routes | Operation/causal support | Supported conclusion and limit |
|---|---|---|---|---|---|
| CLM-3 | Source-grounded connected notes; SRC-14 README, doctrine | Mine/cut/weave/reweave/tend and passage contracts | Semantic procedure supplied as instructions; RTE-6 provides graph plumbing | None inspected / none; no intervention comparison | Declared detailed source-grounding workflow; deliberate downstream truth adjudication. Calling admission or retention truth acceptance would exceed design. |
| CLM-4 | Deeply researched reusable articles; SRC-22 README, doctrine | Evidence standards, alternatives, self-review, completion and mediation | RTE-13 only computes map, not research | None inspected / none | Plausible executable-by-agent research procedure, not demonstrated answer adequacy; researched leaf does not prove reviewed answer. |
| CLM-5 | Verified semantic defects and demonstrated repairs; SRC-19 check/fix, doctrine | Independent reader, verification of catches, repeat defect check, human exceptions | Semantic checking is procedural; engine state does not establish transition history | None inspected / none | Distinct criticism, acceptance-for-repair and resolution guidance. Existing-doctrine conformity is narrower than truth of the doctrine or improved performance. |
| CLM-6 | Supported workspace change completed through intended consumer; SRC-20 improve, doctrine | Evidence-grounded proposal, human scoped approval, actual behavior check, keep unmet obligations open | Improvement is instructed agent/human work; changed mechanism depends on authoring/runtime | None inspected / none; no future outcome or controlled contrast | Architecture specifies a correction/design/research/revision loop and explicit completion limits. It does not show that a tentative theory was accepted, integrated, or improved later action. |
| CLM-7 | Convert files, retain originals and capture link/date; SRC-21 README, doctrine | User checks note against original; explicit refresh | RTE-12, RTE-12, RTE-12, RTE-12 | Code inspection only / none | Wrapper code constructs source metadata and refuses specified invalid import states. Conversion fidelity/source truth and runtime success unobserved; original link is provenance, not corroboration. |
| CLM-8 | Assess skill contribution through comparable tasks with/without it; SRC-18 eval guide, doctrine | Separates selection, task result, repaired procedure and added value | No evaluated trial runner inspected in this package | None / no treatment or comparison data, no causal identification | Soundly scoped evaluation guidance exists. No contribution estimate or component effect is established by the guidance itself. |

### Evidenced absences

#### ABS-1 — No in-release compaction distiller in inspected adapter path

Conclusion status: absent. Bounded search record: `git --no-replace-objects -C <source-root> grep -n -i -E 'compact|Compaction|summary|summar|distill' <full-revision> -- hooks src`, run separately over SRC-9 root `/home/zby/llm/commonplace/related-systems/arsumbris--au-mcp-adapter-cc` at `333b2117f338cd4815eeeb9ab7b3932b29fa7d62` and SRC-10 root `/home/zby/llm/commonplace/related-systems/arsumbris--au-mcp-adapter-codex` at `3b0e3a3cf67b3143819c61c590efc85d36c23bc5`. CC matches were only hook registration and compaction-event forwarding. Codex matches were pre-compact tail/event forwarding, hook registration, an approval-preview truncation and copying exposed reasoning summaries. The bounded hook and lift bodies were read, as cited below. This establishes absence of a distiller on the inspected two-adapter compaction capture paths; lexical search alone does not exclude differently named mechanisms elsewhere.

Evidence: SRC-9 `hooks/pre-compact.ts:1-11`; SRC-10 `hooks/pre-compact.ts:1-13`; SRC-10 `src/lift.ts:42-46,55-83`. PreCompact signals compaction; Codex first lifts the visible tail. Lift can copy explicitly exposed reasoning summary text but does not generate it. External summarizers and encrypted reasoning are excluded; neither a summary field nor a compaction event establishes release-owned trace learning. This is a bounded negative over the two adapters' inspected capture routes, not a statement about the harnesses.

> const payload = await readPayload(process.stdin)
> await liftRollout(payload)
> await observeEvent(payload, EventKind.Compaction, {
>   trigger: payload.trigger ?? null,
>   custom_instructions: payload.custom_instructions ?? null,
> })
> --- [hooks/pre-compact.ts](https://github.com/arsumbris/au-mcp-adapter-codex/blob/3b0e3a3cf67b3143819c61c590efc85d36c23bc5/hooks/pre-compact.ts#L7)

> /** Capture only explicitly exposed text. Encrypted-only reasoning contributes no fabricated content. */
> function reasoningText(p: ResponseItemPayload): string {
>   const texts = (arr: Array<{ text?: unknown }> | undefined): string =>
>     Array.isArray(arr) ? arr.map((x) => (typeof x?.text === 'string' ? x.text : '')).filter(Boolean).join('\n') : ''
>   return [texts(p.summary), texts(p.content)].filter(Boolean).join('\n\n').trim()
> --- [src/lift.ts](https://github.com/arsumbris/au-mcp-adapter-codex/blob/3b0e3a3cf67b3143819c61c590efc85d36c23bc5/src/lift.ts#L42)

No other absence is asserted. Missing product runs and provider internals are limitations.

### Behavioral-authority paths

BAP-1 — kernel/engine consumers receive profile, hook and mutation decisions through function/RPC returns. Force: enforcing only at the named RTE-2, RTE-4, RTE-5 seams; horizon: current action/session. Epistemic force is limited to request shape and content consistency, not truth. Implementation conclusion status: wired. See quoted branch evidence on those routes.

BAP-2 — discovery consumes OBJ-2 runtime metadata as executable routing/configuration; imported plugin code then affects future calls during that daemon lifetime. Force: routing and execution authority; horizon: registry/session lifetime. Implementation conclusion status: wired. RTE-3 contains evidence. Editable metadata constitutes a causally connected representation of available operations, bounded to discovery and later dispatch.


BAP-3 — later agent/harness consumes selected retained rules/skills via launch artifacts or requested skill content. Force: instruction; horizon: launch/task until refreshed. Implementation conclusion status: wired for delivery (RTE-9), with procedure execution afforded (RTE-8, RTE-16); changed model behavior remains uninspected.

BAP-4 — later knowledge-work agent consumes stored sources, nodes, articles and correction reasons through graph/file reads. Force: advisory knowledge and navigation; horizon: task and later tasks using retained files. Implementation conclusion status: wired for retrieval (RTE-6); semantic selection and evaluation afforded in RTE-7, RTE-14, RTE-15, RTE-16.

BAP-5 — guarded import plugin consumes preview diagnostics and hashes before writing; force: enforcing structural/stability admission within RTE-12, horizon one import item. Implementation conclusion status: wired. No content-truth authority follows.

## Runtime account

The ordinary progression is RTE-1 → the integrated context routes → model-selected tool request → adapter mediation → RTE-2 → observation and further model work. The application and kernel supply typed state, context and operations. They do not replace the harness's model loop. The concrete deployed grant set, model identity and user objective are inputs, not properties inferred from the release catalogue.

Three static forcing cases bound the interpretation:

| Case | Evidence and disposition | What follows |
|---|---|---|
| Stale or invalid knowledge write | RTE-2 checks explicit hashes/path/request shape, while result diagnostics are advisory | A structurally invalid knowledge artifact can still be written; a stale supplied hash can reject. Neither is a truth test. |
| Daemon loss or bypass of the ordinary hook path | RTE-4 allows on CC mediation error; RTE-5 denies on Codex mediation error; direct invoke has its own smaller check set | “Governed” depends on adapter and path; the typed API is not a machine-wide enforcement boundary. |
| Incompatible or untrusted extension | RTE-3 rejects/skips by contract and criticality, but imports admitted code in-process | Contract compatibility is enforced in the loader; OS isolation and semantic safety do not follow. |

The native-tool branch, direct engine/API clients, host terminal and extension module are material alternatives. Their existence does not prove a deployed bypass occurred; it prevents attributing a universal guarantee to a narrower seam. Model-side scheduling, remote execution, provider-native tools and harness compaction are not implemented or observed here and are left to the external harness boundary. Recovery/resume is assessed in the memory routes. No throughput, latency or operational reliability measurements were made.

Execution-preflight disposition: **no dynamic check planned**. Considered running a full Electron/harness session, injecting a stale write, and forcing adapter connection loss. Static branches settle the bounded wiring findings; product execution would additionally require a runnable sibling layout, installed Rust/Node/Electron dependencies, an active workspace and harness configuration. Those were not established, and no product code, GUI, daemon or model request was executed. This prevents observed or causal outcome claims. Source extraction and Commonplace artifact validation are analysis operations, not product probes.

## Lens scoping

### Memory/context scope

Depth: full within the frozen release and explicitly scoped opaque exclusions. Trigger evidence: SRC-6 session/inject/skill routes, SRC-2 graph/file retention, SRC-9 and SRC-10 resume/adapter context. A fresh specialist independently inventories accumulated files, instruction evolution, session recovery, selection and later consumers; its canonical route/object mapping follows below. Static shipped material is an access mechanism rather than proof that use produced memory. External harness transcripts are inspected only through the adapters' consuming interface; model internals and external compaction implementation are excluded.

### Epistemic scope

Depth: full for the material knowledge route families: source ingestion, claim weaving, tree research, competency derivation/improvement and governance findings; brief for transport/type checks, where the runtime already bounds their license. Trigger evidence: SRC-14, SRC-19, SRC-20, SRC-21 and SRC-22. A separate source-only lens identifies content transformation, acceptance, retention and operational force without treating type names as warranted conclusions. External fetched-source truth, private runs, model internals and uninspected optional plugins prevent whole-system claims of verified knowledge or observed learning.

## Lens outputs

### Memory/context lens

The independent memory specialist inventoried OBJ-3, OBJ-4, OBJ-5, OBJ-6 and OBJ-7, with RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12 and RTE-13. Files/Git retain editable knowledge; a derived graph and access metadata make it reachable; launch selection can give revised knowledge instruction force. RTE-6 is requested pull. RTE-9 automatically supplies selected retained parts: explicit owner:name and graph-reference selection are identifier push; member-role defaults and budgets are coarse push. RTE-11 uses held-path identity to push freshness notices within the current run; OBJ-4 and RTE-11 are auxiliary context/control records outside all normalized memory axes. Neither successful delivery nor a served marker demonstrates activation or benefit.

RTE-8 affords automatic trace-fed production when a selected correction directive tells the model to retain reusable feedback, then a later improve task reads it and authoring/adoption makes new guidance available. This supports trace_learning=yes at afforded basis, not a demonstrated kernel learning loop. Live correction capture is online and later adoption staged; the alternate skill-maintenance branch reads selection traces/task results whose format and timing are unspecified. The aggregate trace-source and timing remain not-determinable. Both branches target reusable cross-task, per-project guidance; both can yield prose or symbolic procedures/contracts. Curation's complete union is uncertain. Faithfulness testing is not-determinable because no sufficiently comprehensive retained-experiment search was made.

RTE-10 retains/replays session facts, not derived prescriptive memory; ABS-1 bounds the two adapters' compaction capture paths, with external compaction excluded. Raw logs, current-call payloads and unchanged shipped rules are not counted as learned memory. The report's comparison profile is integrated without strengthening its evidence basis; all adopted source quotes are on canonical records above.

### Epistemic lens

#### 1. Source-and-claim boundary

The frozen sources and inclusion/exclusion rules are those of the Source register, especially SRC-14, SRC-18, SRC-19, SRC-20, SRC-21 and SRC-22. The question is which content checks license reliance or action. Assessed families are import, weave, research, semantic governance and capability improvement; unsupported provider behavior, actual workspace outcomes and external evidence remain excluded. CLM-3, CLM-4, CLM-5, CLM-6, CLM-7 and CLM-8 register the relevant source claims. No candidate-linked run or causal comparison was inspected.

#### 2. Epistemic-object inventory

See OBJ-8 (converted source), OBJ-9 (extraction), OBJ-10 (woven claim), OBJ-11 (article), OBJ-12 (defect finding), OBJ-6 (feedback correction), OBJ-13 (remedy prediction), OBJ-14 (normative scope/dispositions), OBJ-15 (changed policy/capability), and the navigation branch of OBJ-7. These are parts of the retained substrate, separated because provenance, checks and authority differ. Their generic identity/form/lineage is declared once in Shared records.

#### 3. Authority-route ledger

Rows below annotate the canonical route's individual functions; repeated route IDs are the same route, not extra generic records. Architectural status is independent of conclusion status. All listed results are designed possibilities, with observed candidate state: no instance observed. Doctrine-only procedures acquire instruction force through BAP-3 when selected, not automatic semantic enforcement. Implemented imports use BAP-5; graph use uses BAP-4. Unknown activation and absent run evidence prevent actual acceptance claims.

| Route / function / architectural status | Object and update relation; target | Evaluator/condition, timing and result | Epistemic license; operational and behavioral-authority path | Evidence / claim / gap |
|---|---|---|---|---|
| RTE-12 / content transformation / implemented | OBJ-8; truth-apt transformation: acquisition/import from raw bytes | Selected document/PDF converter at ingest; returns Markdown or error | Acquired content with original link and supplied date; converter result becomes import candidate; plugin channel, invoked conversion | SRC-21 converter wrappers; CLM-7; source warrant unknown and fidelity untested |
| RTE-12 / check/evidence production / implemented | OBJ-8; no content change; converted note's engine-visible structure and raw stability | `preview_mutation`, converter-family check, raw rehash and destination reread before write | Structural/identity/stability findings only; results feed RTE-12, not source-truth acceptance | SRC-21 `ingest.mjs` `preview` and ingest revalidation; CLM-7 |
| RTE-12 / operational admission/selection/consumption / implemented | OBJ-8; no content change; eligibility to write | Structural errors or type mismatch reject; changed raw/destination reject; differing existing note requires explicit refresh | Licenses this import attempt after bounded checks; runner's controlled path refuses before broker write; horizon one item | SRC-21 `ingest.mjs`; CLM-7; concurrent new-file creation lacks engine absence guard; post-write diagnostics can still show errors |
| RTE-12 / retention / implemented | OBJ-8; no content change; converted note | Broker `write_file`, expected hash for existing destination; created/updated/present/unknown/pending outcomes | Durable candidate availability, no truth endorsement; plugin requests engine mutation; reads can confirm bytes while validation remains unknown | SRC-21 `ingest.mjs` write/recovery; CLM-7; parent supplies full storage semantics |
| RTE-7 / content transformation / doctrine only | OBJ-9; truth-apt transformation: indeterminate, intended non-ampliative reshaping | Mining agent reads whole source, excludes outside knowledge, preserves qualifications; produces extraction | At most source-faithful interpretation if actually checked; source text treated as evidence even if instruction-shaped; later cut consumes saved candidates | SRC-14 `skills/mine.md`, `type/candidate.type.yaml`; CLM-3; wording/implicit relations require semantic judgment |
| RTE-7 / disposition/acceptance / doctrine only | OBJ-9, OBJ-14; no content change to candidate, policy update to verdict | Cut agent judges premise, existing nodes and salience; weave/enrich/parked/dropped with why, before node creation | **Admission for graph utility**, not acceptance of proposition truth; verdict selects work for weave/reweave, guidance channel, current graph growth | SRC-14 `skills/cut.md`; CLM-3; no candidate outcome observed |
| RTE-7 / check/evidence production / doctrine only | OBJ-9, OBJ-10; no content change; passage identity and support of interpretation | Weave/reweave agent follows blocks, checks extraction source, text, qualifications and diagnostics; missing/uncheckable anchors leave pending | Source-grounding license for candidate interpretation only; guides writer to withhold resolution/fold until check | SRC-14 `skills/weave.md`, `skills/reweave.md`; CLM-3; semantic check not enforced by presence of links |
| RTE-7 / content transformation / doctrine only | OBJ-10; truth-apt transformation: indeterminate between faithful synthesis, derivation and ampliation | Weave/reweave agent synthesizes across sources, preserves hedges, sharpens only as newer evidence earns | Intended source-bounded statement; source-grounded assertion is not independent truth adjudication; resulting text available to graph consumers | SRC-14 `type/claim.type.yaml`, `skills/reweave.md`; CLM-3; no candidate-linked premises/derivation inspected |
| RTE-7 / disposition/acceptance / no route found within boundary | OBJ-10; no content change; proposition standing or resolution of contradictory ideas | No supplied evaluator; shipped vocabulary explicitly leaves this to downstream consumers | No truth verdict licensed by admission, resolution, or tension edge; no operational prohibition on downstream use established here | SRC-14 `type/claim.type.yaml`, `guides/the-argument-edge.md`; CLM-3; deliberate scope boundary, not product failure |
| RTE-7 / check/evidence production / doctrine only | OBJ-10; no content change; source drift and graph meaning | Tend fresh reader and reweave separate agent compare nodes, sources, links; risky merge/prune decisions held for human review | Scoped semantic maintenance advice; safe repair or proposed risky change, not globally warranted graph | SRC-14 `skills/tend.md`, `skills/reweave.md`; CLM-3; no maintained graph observed |
| RTE-14 / content transformation / doctrine only | OBJ-11; truth-apt transformation: indeterminate, with explicitly possible ampliative inferences | Research agent uses provisional outline, source search/read and synthesis for assigned question | Produces candidate answer, not warranted by fluency or format; article intended as reusable source | SRC-22 `skills/research.md`; CLM-4; no actual inference classified |
| RTE-14 / check/evidence production / doctrine only | OBJ-11; no content change; consequential facts, interpretation, argument and saved article adequacy | Appropriate evidence by claim kind; independent corroboration where available; plausible alternatives; reread saved answer and repair support/depth gaps | Intended evidence-sensitive review within question scope; model judgment guides continue/revise/finish; no universal test or external oracle | SRC-22 `skills/research.md`; CLM-4; derived testable consequences not a mandated phase |
| RTE-14 / disposition/acceptance / doctrine only | OBJ-11, OBJ-14; no content change to answer, update question state | Research agent after substantive review and diagnostics changes direct open leaf to researched; incomplete investigation stays open | **Completion acceptance** for a reviewed scoped answer, not every statement certified; operationally clears answers state mismatch and makes completion visible | SRC-22 `skills/research.md`, `type/question.researched.type.yaml`; CLM-4; state alone does not establish article exists |
| RTE-14 / lifecycle integration / doctrine only | OBJ-11; no content change to accepted answer; changes research queue/use | Mediation reads completed articles and premise, compares coverage, develops/ranks follow-ups; consumers may weave articles or use for capability design | Post-review connection of answer to further inquiry if RTE-14 actually ran; advisory queue ranking during mediation | SRC-22 `skills/mediate.md`, README; SRC-20 `skills/self-research.md`; CLM-4; no integration observed; map inclusion can precede acceptance |
| RTE-13 / content transformation / implemented | OBJ-7; truth-apt transformation: non-ampliative reshaping | Refresh plugin reads typed relations under held graph version, emits linked Index and warnings | Warrants navigation from read relationships only; changes computed Index through engine, selected invocation; warns on incomplete structure | SRC-22 `refresh-research-map.mjs`; CLM-4; map is not epistemic acceptance or proof of coverage |
| RTE-15 / content transformation / doctrine only | OBJ-12; truth-apt transformation: ampliative conjecture | Fresh reader proposes semantic defect from actual subjects/sources and doctrine | Candidate defect to check; author explanation excluded from review context, not proof of reader correctness | SRC-19 `skills/check.md`; CLM-5; no reader instance |
| RTE-15 / check/evidence production / doctrine only | OBJ-12; no content change; catch's actual violation | Check agent verifies reader catch against subject and doctrine before recording | Scoped justification of defect against named requirement; result feeds recording/fix, not general truth test | SRC-19 `skills/check.md`; CLM-5 |
| RTE-15 / disposition/acceptance / doctrine only | OBJ-12; no content change; defect accepted as repair work | Check agent records only verified finding.open with subject, breaks, evidence; unsupported catch not admitted | Accepted defect **for correction against doctrine**, possibly normative rather than empirical; gives fix worklist target | SRC-19 `skills/check.md`, `type/finding.type.yaml`; CLM-5; label alone is insufficient |
| RTE-15 / check/evidence production / doctrine only | OBJ-12, OBJ-15; no content change; repair against violated doctrine | Fix repeats original audit/direct check, records observed result; unavailable/failing check leaves open | Establishes only same doctrine-specific defect resolved if evidence supports; does not prove broad transfer or mechanism | SRC-19 `skills/fix.md`; CLM-5 |
| RTE-15 / disposition/acceptance / doctrine only | OBJ-12, OBJ-14; no truth-apt content change; finding terminal state | Passing repair → resolved; human ruling → accepted deviation or dismissed false alarm | Operational disposition with differing warrants: accepted is **exception**, not repaired; dismissed is rejected defect; current finding lifecycle | SRC-19 `skills/fix.md`, finding leaf schemas; CLM-5; transition history not engine-checked |
| RTE-15 / lifecycle integration / doctrine only | OBJ-12, OBJ-15; non-truth-apt policy/content update: repair subject and retain repair evidence | After defect acceptance, fix changes subject, checks impact and preserves finding/history | Revises governed content; future users read revised subject, with record of reason/check; not demonstrated future performance gain | SRC-19 `skills/fix.md`; CLM-5; mutation semantics parent-owned |
| RTE-8 / content transformation / doctrine only | OBJ-6; truth-apt transformation: acquisition/import for feedback report; recurrence relation indeterminate | Agent captures reusable human redirect and links repeated friction to root | Preserves feedback for later recognition; human preference warrants desired behavior, not causal remedy effectiveness | SRC-19 correction rule; SRC-20 `skills/improve.md`; CLM-6 |
| RTE-16 / content transformation / doctrine only | OBJ-13; truth-apt transformation: ampliative conjecture for predicted remedy; OBJ-14 requirement is non-truth-apt update | Derive requires recurring friction or corroborated research plus missing method; propose compares alternatives/current routes and uncertain behavior | Candidate supported design and bounded promise; no approval inferred from source citations or research selection | SRC-20 `skills/derive.md`, `skills/propose.md`; CLM-6 |
| RTE-16 / disposition/acceptance / doctrine only | OBJ-13, OBJ-14; no content change; implementation scope | Human's recorded ruling, including session approval; silence is insufficient | **Operational approval**, not epistemic acceptance of remedy prediction; improve agent may implement accepted scope, must return material scope change | SRC-20 `skills/improve.md`, `type/proposal.type.yaml`; CLM-6 |
| RTE-16 / check/evidence production / doctrine only | OBJ-13, OBJ-15; no content change; promised behavior through intended consumer | Improve observes intended consumer; exercised boundary for prevention, doctrine judgment for semantics; skill trial compares tasks/configurations with/without skill where contribution uncertain | Scope-specific behavior evidence; with/without comparison may assess contribution only under actual design; no observed causal trial here | SRC-20 `skills/improve.md`; SRC-18 `guides/eval-driven-authoring.md`; CLM-6, CLM-8 |
| RTE-16 / disposition/acceptance / doctrine only | OBJ-13, OBJ-14, OBJ-15; no content change to promise; completion state update | Keep proposal accepted until promised behavior demonstrated; answered competencies, forged addressed corrections, then implemented proposal | **Completion acceptance** for delivered scope, explicitly excludes untested larger integration; guides closure of work, not global competence | SRC-20 `skills/improve.md`; CLM-6; no actual completion record |
| RTE-16 / behavior/policy adaptation / doctrine only | OBJ-15; non-truth-apt policy/content update: approved mechanism authored/activated | Owning authoring capability builds approved scope, follows discovery/selection/activation contract | Revised behavior may reach future consumers via skill/rule/tool selection; prose says profile link is not invocation; delivered enforcement depends on actual mechanism | SRC-20 `skills/improve.md`; SRC-18 `guides/guarantee-vs-guidance.md`; CLM-6; parent establishes actual runtime authority |


#### 4. Per-object lifecycle disposition


All candidate states below are **no instance observed**: neither an actual candidate artifact produced by these routes nor a candidate-linked run was inspected. This is separate from architectural status. Shipped type/skill files are design evidence, not candidate-linked history.

- **OBJ-8:** RTE-12, RTE-12, RTE-12, RTE-12; transformation **acquisition/import**; discovery lifecycle **not applicable**. Source link/capture metadata, raw stability checks and retained originals support recoverable provenance within the import route. They do not establish the source's truth or converter fidelity. External converter implementation and converted-source comparison are missing.
- **OBJ-9:** RTE-7, RTE-7, RTE-7; transformation **indeterminate**. Intended classification is non-ampliative reshaping; interpreting implicit relations or compressing qualifications could instead add or distort content. Lineage is source `of`, source surface wording, and later checked passage links. Checks/admission are doctrine only. Actual source/candidate comparisons are needed to decide preservation or ampliation; utility verdict supplies no truth warrant.
- **OBJ-10:** RTE-7, RTE-7, RTE-7, RTE-7; transformation **indeterminate**. Faithful synthesis, entailed derivation and ampliative conjecture remain possible. Extraction resolutions and passage links retain intended provenance; semantic passage and drift checks are doctrine only. No standing/adjudication route found in this package boundary. No claim is classified as a produced accepted ampliative conclusion. Actual premises, claim, support reading and downstream adjudication would be needed.
- **OBJ-11:** RTE-14, RTE-14, RTE-14, RTE-14; transformation **indeterminate** for unspecified article content: source acquisition, non-ampliative synthesis, entailed reasoning and ampliative interpretation/inference are all permitted. The declared instruction to distinguish findings, inferences and illustrations does not identify an actual inference. Article citations and source details are intended lineage; substantive review/completion and later inquiry integration are doctrine only. Any future identified ampliative article claim must receive its own lifecycle record. No instance observed in any phase here.
- **OBJ-12:** transformation **ampliative conjecture**, semantic defect claim. Observation/anomaly: RTE-15, doctrine only, no instance observed (SRC-19 check skill). Conjecture: RTE-15, doctrine only, no instance observed. Derived consequence: no route found within boundary as a distinct predeclared consequence phase; no instance observed. Test/evidence: RTE-15, doctrine only, no instance observed; subject/doctrine verification. Acceptance: RTE-15, checking agent, criterion verified violation, intended use repair worklist, scope named subject/doctrine; doctrine only, no instance observed, accepted scope unobserved. Lifecycle integration: RTE-15, repair subject and retain evidence for future consumers; doctrine only, no instance observed. RTE-15 and RTE-15 govern checking/disposal after attempted repair, likewise no instance observed. Missing candidate-linked evidence prevents claiming actual accepted defect or successful repair.
- **OBJ-6:** RTE-8; transformation **acquisition/import** for recorded feedback, lifecycle not applicable to that part. Human desired behavior is normative authority, not proof of factual account. Recurrence interpretation remains **indeterminate** without occurrences: preserved root linkage is intended, but count/backlink alone is explicitly insufficient. No instance observed; no actual recurrence warrant established.
- **OBJ-13:** transformation **ampliative conjecture** for predicted remedy effectiveness. Observation/anomaly: RTE-8 and RTE-16, doctrine only, no instance observed; recurring friction or corroborated signal. Conjecture: RTE-16, doctrine only, no instance observed. Derived consequence: RTE-16 and RTE-16 prescribe expected acceptance checks and a case distinguishing alternatives, doctrine only, no instance observed; not a formal entailment proof. Test/evidence: RTE-16, doctrine only, no instance observed; intended-consumer checks matched to promise. Acceptance: RTE-16, improve agent, demonstrated promised behavior for delivered scope, doctrine only, no instance observed, accepted scope unobserved. RTE-16 is earlier operational authorization, not acceptance of prediction. Lifecycle integration: no distinct post-completion efficacy-based integration route found within boundary; RTE-16 builds and activates the approved mechanism before verification/completion and must not be relabeled post-acceptance integration. Architectural status for actual post-acceptance reuse: not determinable as post-acceptance integration: RTE-9 supplies later instruction delivery but does not condition it on demonstrated efficacy; observed candidate state no instance observed. Missing actual before/after outcomes, independent effect comparison and future transfer evidence prevents demonstrated learning.
- **OBJ-14:** No lifecycle record for OBJ-14: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-7, RTE-14, RTE-15, RTE-16, RTE-16. State claims declare workflow positions; any assertions embedded in their surrounding evidence belong to the relevant truth-apt object above.
- **OBJ-15:** No lifecycle record for OBJ-15: no candidate truth-apt output for the policy/code artifact itself; relevant direct-adaptation or update routes: RTE-15, RTE-16. Claims that its promised behavior was delivered are OBJ-13, checked through RTE-16 and disposed through RTE-16. No candidate instance or demonstrated future effect observed.
- **OBJ-7:** RTE-13; transformation **non-ampliative reshaping**; discovery lifecycle **not applicable**. Implementation checks live references, type contributions and graph version while rebuilding navigation. Warrant is stored-relationship navigation under those checks, not semantic completeness or truth; runtime execution unobserved.


#### 5. System-claim versus route comparison

The canonical CLM-3, CLM-4, CLM-5, CLM-6, CLM-7 and CLM-8 rows retain the layer-by-layer comparison. Import/navigation have implementation support. Source interpretation, semantic criticism, scope approval and demonstrated completion are articulated as procedures; no performed candidate lifecycle or causal comparison is established. Utility admission, human exception, authorization to build and efficacy acceptance have different scopes and are not interchangeable.

#### 6. Bounded conclusion

The bundle acquires content with structural/stability checks; it supplies detailed source-grounding and criticism procedures without settling truth by graph membership. A finding checked against doctrine licenses repair against that doctrine, not a truth verdict about the doctrine. An approved proposal licenses implementation, while its completion requires intended-consumer evidence. Proposed remedies may be tested and revised, but no actual comparison here demonstrates improved future capacity. Reflection of typed capabilities (RTE-3) and delivery of mutable instructions (RTE-9) do not establish revision of an operative self-theory.

## Reconciliation

Runtime, memory and epistemic work share one source boundary. Memory owns the comparison profile. Generic write admission remains RTE-2; RTE-6 describes its distinct author/read consumer chain. RTE-12 merges import operations across lenses; RTE-13 merges computed navigation. RTE-8 is feedback-to-guidance, while RTE-16 describes the broader proposal/approval/check workflow. Their relation does not imply enforced scheduling. The epistemic overlay splits functions within these routes, not the generic identity. OBJ-8, OBJ-9, OBJ-10, OBJ-11 and OBJ-12 are distinct typed-content parts of broad OBJ-3; the Index is the navigation branch of OBJ-7.

| Specialist proposal | Canonical disposition |
|---|---|
| MEM-OBJ-1 | OBJ-3 |
| MEM-OBJ-2 | OBJ-4 |
| MEM-OBJ-3 | OBJ-5 |
| MEM-OBJ-4 | OBJ-6 |
| MEM-OBJ-5 | OBJ-7 |
| MEM-RTE-1 | RTE-6 |
| MEM-RTE-2 | RTE-7 |
| MEM-RTE-3 | RTE-8 |
| MEM-RTE-4 | RTE-9 |
| MEM-RTE-5 | RTE-10 |
| MEM-RTE-6 | RTE-11 |
| MEM-RTE-7 | RTE-12 |
| MEM-RTE-8 | RTE-13 |
| MEM-ABS-1 | ABS-1 |
| EP-OBJ-1 | OBJ-8 |
| EP-OBJ-2 | OBJ-9 |
| EP-OBJ-3 | OBJ-10 |
| EP-OBJ-4 | OBJ-11 |
| EP-OBJ-5 | OBJ-12 |
| EP-OBJ-6 | OBJ-6 |
| EP-OBJ-7 | OBJ-13 |
| EP-OBJ-8 | OBJ-14 |
| EP-OBJ-9 | OBJ-15 |
| EP-OBJ-10 | OBJ-7 |
| EP-RTE-1 | RTE-12 |
| EP-RTE-2 | RTE-12 |
| EP-RTE-3 | RTE-12 |
| EP-RTE-4 | RTE-12 |
| EP-RTE-5 | RTE-7 |
| EP-RTE-6 | RTE-7 |
| EP-RTE-7 | RTE-7 |
| EP-RTE-8 | RTE-7 |
| EP-RTE-9 | RTE-7 |
| EP-RTE-10 | RTE-7 |
| EP-RTE-11 | RTE-14 |
| EP-RTE-12 | RTE-14 |
| EP-RTE-13 | RTE-14 |
| EP-RTE-14 | RTE-14 |
| EP-RTE-15 | RTE-13 |
| EP-RTE-16 | RTE-15 |
| EP-RTE-17 | RTE-15 |
| EP-RTE-18 | RTE-15 |
| EP-RTE-19 | RTE-15 |
| EP-RTE-20 | RTE-15 |
| EP-RTE-21 | RTE-15 |
| EP-RTE-22 | RTE-8 |
| EP-RTE-23 | RTE-16 |
| EP-RTE-24 | RTE-16 |
| EP-RTE-25 | RTE-16 |
| EP-RTE-26 | RTE-16 |
| EP-RTE-27 | RTE-16 |
| EP-CLAIM-1 | CLM-3 |
| EP-CLAIM-2 | CLM-4 |
| EP-CLAIM-3 | CLM-5 |
| EP-CLAIM-4 | CLM-6 |
| EP-CLAIM-5 | CLM-7 |
| EP-CLAIM-6 | CLM-8 |
| MEM-ABS-2 | Withdrawn before canonical allocation; faithfulness remains not-determinable, not an absence. |

Corrections/amendments: the memory specialist replaced a documentation-only graph quote with executable assembly evidence on OBJ-3; added a bounded search/status to ABS-1; and withdrew the unsupported broad absence of recall-dependence evidence. A final semantic correction kept OBJ-4 and RTE-11 as auxiliary context/control records but excluded them from all memory-comparison axes: their read credit clears at close and does not establish later memory read-back. This narrows the profile scope without changing either record’s referent; enforcement was removed from the memory authority set, while launch-based coarse/identifier push remains supported by RTE-9. Source comments claiming deletion at close are superseded as interpretation by RTE-10's implemented dormancy retention. Comments suggesting automatic expected-hash injection are not used: RTE-2 and RTE-11 distinguish separate mediation from explicit caller CAS. RTE-13 keeps procedure conclusion status afforded and adds implementation conclusion status wired only for inspected index computation, as the epistemic source reading supports. These amendments preserve each record's referent. Integration also inserts blank lines between separate quote blocks in the specialist report; this is formatting only, and the report digest above binds those exact bytes.

Independent convergence: both specialists found the feedback/adoption procedure and the gap between procedural evaluation and demonstrated improvement. The coordinator supplied the mediation/invoke boundary to the memory specialist, so agreement on that detail is integration, not independent corroboration. There are no unresolved source conflicts. No actor is promoted to a verified evaluator merely from a type or hook name.

## Bounded synthesis

arsumbris makes knowledge, instructions, schemas and extension metadata editable within a shared typed-file substrate. The engine rebuilds a graph, the host exposes it to humans, and adapters connect model-driven work to a plugin kernel. This is a configurable agent operating layer around external model loops, not a release-owned replacement for those loops. Its discriminating feature is that the same retained file can be advisory knowledge in a pull request and behavioral instruction when a launch profile selects it.

For source-backed graph work, the machinery preserves originals, references, hashes, typed relations and later access. The weave procedures further ask agents to check source passages and constrain their interpretations. That supports provenance and a route for criticism; the vocabulary deliberately leaves proposition standing and contradiction resolution downstream. A successful write or clean schema diagnostics is consequently weaker than semantic acceptance. Ingest can refuse structural errors locally even though generic engine writes retain diagnostic errors.

For controlled operation, the relevant unit is a concrete adapter/plugin/engine path. Profile visibility, critical-plugin failures, malformed input and stale supplied hashes have executable checks. The CC and Codex mediation failure branches differ. Direct clients, ambient extension code and native tools outside a restrictive profile prevent a universal isolation or governance claim. This is consistent with the release's explicit lack of sandboxing.

For retained improvement, the strongest supported contribution is a specified feedback-to-remedy route: capture an interaction correction, preserve the reason, compare a proposed response, obtain scoped authorization, implement it and check its intended consumer. RTE-8 affords trace-fed memory and RTE-16 affords evidence-sensitive revision. Their availability is useful evidence of mechanism; the missing result is improved future capacity attributable to criticism. **Conjectural-learning conclusion status: uninspected** for demonstrated improvement; formulation/use/criticism/revision affordances are separately recorded on RTE-16. No actual before/after outcome was examined.

**Reflection conclusion status: wired**, restricted to typed capability/profile representation, discovery and subsequent dispatch (OBJ-2, RTE-3, BAP-2). **Reflective theory-builder conclusion status: uninspected**: mutable descriptions and a skill named self-research do not show an operative self-theory of theory-building organization being revised. **Self-improvement pathway conclusion status: afforded** through correction/proposal/implementation/delivery. **Occurrent self-improvement conclusion status: uninspected**: no later operation was observed to depend on an evidence-responsive change. These are independent properties, not a maturity ranking.

The assessment would change with a pinned workspace and active profile, an actual correction/proposal/remedy lineage plus later consumer output, or comparable trials varying recalled guidance. Adapter outage and direct-client probes would strengthen deployed control findings; source/candidate comparisons would decide preservation versus amplification in a concrete weave/article case. Provider/model pins and dependency inspection would close different limits, without themselves proving learning.

The mappings use [conjectural learning](../../../../notes/definitions/conjectural-learning.md), [reflection](../../../../notes/definitions/reflective-system.md), and [self-improvement](../../../../notes/definitions/self-improving-system.md) in their separate technical senses.

## Limitations

| Limitation | Affected records/sources | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No product execution or candidate-linked outcomes | RTE-1, RTE-8, RTE-14, RTE-15, RTE-16 | Static release code and doctrine | Observed reliability, acceptance, activation, benefit or causality | Pinned operational runs and designed comparisons |
| Model/harness internals and compaction excluded | CMP-4, ABS-1 | Adapter hook/launch interface only | Exact weights/fixity, opaque memory content, full scheduling or hidden criticism | Versioned provider/harness contracts and inspectable runs |
| Current grants and platform configuration unknown | RTE-1, RTE-3, RTE-4, RTE-5 | Shipped profile and adapter mechanisms | Actual deployed tool access or isolation | Frozen launch/profile and platform observations |
| External packages, converters and code beyond inspected paths | SRC-3, SRC-4, SRC-7, SRC-11, RTE-12 | Frozen release plus inspected wrappers | Converter fidelity and exhaustive guarantees across dependencies | Pinned dependency sources and focused checks |
| Semantic workflows are instructions | RTE-7, RTE-14, RTE-15, RTE-16 | Selected skill/type bodies | Performed checks, transition history, truth or improved capacity | Candidate-linked evidence and evaluator outcomes |
| Curation, trace source/timing and faithfulness aggregates uncertain | RTE-8, RTE-16, memory-comparison | Retained-file and feedback paths; external summaries excluded | Exhaustive curation/source/timing sets and recall-dependence evidence classification | Representative deployment paths and retained trials |
| Mutable code/configuration does not ensure hot reload | RTE-3, RTE-9 | Discovery and launch materialization | Immediate effect of every edit on an already running consumer | Lifecycle-specific reload evidence |
| Full projection behavior, optional provenance/workflow implementations and binaries excluded | CMP-3, SRC-23 | Text source subset and material routes | Whole-UI safety/performance and external recorder operation | Separate pinned implementations and execution evidence |

## Verification and blockers

### Semantic verification

Verified source identity and role separation: implementation, doctrine and hypothetical execution are not conflated. Every retained quote is attributed to its exact full-commit blob within SRC-23. Required routes have immediate/later consumer and recovery dispositions below; no generic write, type marker or stored rationale supplies a missing criticism/learning link. Claim scopes remain within inspected paths.

Comparison scope matches OBJ-3, OBJ-5, OBJ-6, OBJ-7 and RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-12, RTE-13. OBJ-4 and RTE-11 are auxiliary current-run controls excluded from every memory axis, alongside external opaque harness payloads and unchanged shipped instructions. RTE-8's correction and selection-trace branches both contribute to source/timing/form/scope assessments; the latter prevents complete source/timing values. RTE-10 and ABS-1 do not qualify as an in-release distillation route. RTE-9 names later agent, launch trigger, owner:name/reference inputs and selected bodies; RTE-11 names affected-path selector and next-result notice. Requested returns remain pull. Curation and faithfulness uncertainties are preserved rather than filled from labels.

Route audit: RTE-1, RTE-2, RTE-3, RTE-4 and RTE-5 carry explicit runtime fields. RTE-6 returns requested graph/file content and persists authored files; RTE-7 returns proposed/revised graph artifacts, later read through RTE-6; RTE-8 returns retained feedback/remedies, with later explicit improve reads and RTE-9 delivery; RTE-9 pushes selected bodies but cannot prove model activation; RTE-10 restores facts to the matching session and exposes consultation, not guaranteed model consumption; RTE-11 returns notices or denies at its specific seam; RTE-12 returns imported note/status with explicit refresh/recovery; RTE-13 updates only computed navigation for later readers; RTE-14 returns articles/questions, RTE-15 findings/repairs, RTE-16 proposals/remedies and check records. For procedural routes, an external model/human owns the next decision, while storage/execution uses RTE-2. Delegated visibility is shared-file availability or adapter session identity, not inferred model-context inheritance. Selection is explicit task/source/path or the stated launch selector. Expiry/invalidation is edit/supersession, freshness or retirement as recorded, with no unclaimed semantic TTL. Actual downstream activation for the instructed knowledge routes remains uninspected; policy guidance does not become an invariant.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/result.md` with `commonplace-validate --full`. Validation passed cleanly with no warnings or failures. All 64 retained quote blocks were additionally matched against their full-commit source blobs and the frozen bundle; source hashes and report/input identities match. Publication preparation rechecks these byte identities.

### Blockers

none
