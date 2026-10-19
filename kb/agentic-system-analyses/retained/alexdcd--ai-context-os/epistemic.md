---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AI-Context-OS epistemic routes: imported and generated candidates, governance checks, operational admission and later reliance."
run-id: AAS-2026-10-18-ai-context-os-82777c0c3926-01
reviewed-boundary: "9ed263080cadf98702bebb42d5260b45bd526f6c"
---

# AI-Context-OS epistemic report

## Source-and-claim boundary

The question is how this public MEMM snapshot acquires or produces truth-apt content, checks it, grants reliance and makes it consequential. The functional boundary and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); evidence identity is [its Source register](boundary.md#source-register), SRC-1. The workspace's designation as canonical is a storage/operating convention, not proof of its propositions. See [EPI-CLM-canonical-files](#epi-clm-canonical-files).

All added findings below are implementation deductions from SRC-1 at the frozen revision, except explicitly attributed design claims. No target, test, example or provider was executed. No observed-run or causal evidence was supplied. The provider component remains opaque; see [RT-CMP-inference-provider](runtime.md#rt-cmp-inference-provider). Neither its internal checking nor its training can be inferred from the Markdown or HTTP interfaces.

The ledger is a sparse overlay: fields owned by supplied records say `see` rather than re-declaring those records. Existing route containers remain valid; their checks, dispositions and retention functions are assessed separately below. No supplied record needs supersession. In particular, the supplied warning that ingestion review is not universal survives direct inspection of MCP save and proposal application. A contrary witness to a broad “no checks” conclusion is the implemented duplicate predicate, conflict heuristic and deterministic test assertions; their licenses are narrower than factual validation.

### Coverage

“Direct” means source text read for this member. “Supplied” means the pinned runtime account, not independent confirmation. Available but uninspected operations are not access gaps or evidenced absences.

| Entry point or operation | SRC-1 source path | Coverage and records / prevented conclusion |
|---|---|---|
| Desktop command registry | `src-tauri/src/lib.rs` | Direct registry read; used to check runtime omissions, especially governance and health. |
| CLI init/search/score/regenerate/list/show/MCP dispatch | `src-tauri/src/cli.rs` | Direct match-body read. Search/score select rather than certify; show bypasses query allocation. See [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff), [RT-RTE-context-query](runtime.md#rt-rte-context-query). |
| All four MCP tools | `src-tauri/src/core/mcp.rs` | Direct bodies: get_context, save_memory, get_skill, log_session. See [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write), [RT-RTE-skill-load](runtime.md#rt-rte-skill-load), [EPI-RTE-governance-checks](#epi-rte-governance-checks). Session logs are caller assertions, not verified events. |
| HTTP/embedded stdio transport | `src-tauri/src/core/mcp_http.rs`, `src-tauri/src/lib.rs` | Supplied runtime findings; no independent dependency/security audit. No inference about host authentication or grants. |
| Capture, import, editing, normalization | `src-tauri/src/commands/inbox.rs` | Direct helpers and command bodies; [EPI-RTE-inbox-capture](#epi-rte-inbox-capture). |
| Proposal generation, parsing, duplicate policy, reject/apply and destination builders | `src-tauri/src/commands/inbox.rs` | Direct; [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), [EPI-OBJ-proposal-content](#epi-obj-proposal-content), [EPI-OBJ-proposal-control](#epi-obj-proposal-control). |
| Desktop chat and provider consumers | `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/inbox.rs` | Supplied [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat), [RT-BAP-context-provider](runtime.md#rt-bap-context-provider); no independent full provider-body reread. Truth of any particular answer is not determinable. |
| Scan admission, usage and score computation; context assemblers/tests | `src-tauri/src/core/index.rs`, `src-tauri/src/core/usage.rs`, `src-tauri/src/core/scoring.rs`, `src-tauri/src/core/engine.rs` | Direct relevant bodies; allocator progression supplied by [RT-RTE-context-query](runtime.md#rt-rte-context-query). Added [EPI-RTE-usage-feedback](#epi-rte-usage-feedback), [EPI-RTE-source-tests](#epi-rte-source-tests). |
| Static adapters, connector handoff | `src-tauri/src/core/router.rs`, `src/views/ConnectorsView.tsx` | Supplied [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff), [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions); CLI regeneration directly inspected. No observed host compliance. |
| External-edit refresh hook | `src/hooks/useFileWatcher.ts` | Direct complete hook; regeneration/reload is wired, not semantic re-acceptance. See [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write). Backend watcher conditions remain supplied evidence. |
| Memory read/save/protection/delete | `src-tauri/src/commands/memory.rs` | Direct relevant bodies; [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write), [EPI-RTE-governance-removal](#epi-rte-governance-removal). Raw filesystem guard analysis remains supplied runtime evidence. |
| Governance detectors, UI and graph importance intervention | `src-tauri/src/core/governance.rs`, `src-tauri/src/commands/governance.rs`, `src/views/GovernanceView.tsx`, `src-tauri/src/core/graph.rs` | Direct; [EPI-RTE-governance-checks](#epi-rte-governance-checks), [EPI-RTE-governance-removal](#epi-rte-governance-removal), [EPI-RTE-importance-boost](#epi-rte-importance-boost). |
| Optimization and health | `src-tauri/src/core/optimizer.rs`, `src-tauri/src/core/health.rs`, `src-tauri/src/commands/observability.rs` | Detector/health implementations direct; status-command bodies supplied by [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status). UI API-name search only; [EPI-RTE-health-score](#epi-rte-health-score). |
| Evaluator sources | `src-tauri/tests/diagnose_vault_query.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/governance.rs` | Direct selected tests and diagnostic; [EPI-RTE-source-tests](#epi-rte-source-tests). No results, quality benchmark or intervention comparison supplied. |
| Product/design claims | `README.md`, `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md` | Direct README and selected proposal sections; [EPI-CLM-canonical-files](#epi-clm-canonical-files), [EPI-CLM-governed-promotion](#epi-clm-governed-promotion). Other documentation not exhaustively assessed. |
| Journal/task/daily CRUD, onboarding templates, backup/restore, vault switching and configuration | `src-tauri/src/lib.rs` | Registered operations identified; detailed bodies uninspected here except supplied provider/config routes. These can retain text, replace workspace state or introduce instructions. No system-complete negative about semantic production, acceptance, rollback or initial lineage is warranted. |

Missing real vaults prevent individuating actual retained claims and assessing their source warrant. Missing inference traces prevent classifying particular generated propositions or establishing that a generated claim was checked or accepted. Missing execution and comparison evidence prevents quality, causal benefit and exercised self-improvement conclusions. Private continuation and later releases remain excluded, as in the boundary. These limits do not make the inspected architecture indeterminable.

## Epistemic-object inventory

Each row separates an operative part or consumer path. Identity/form/storage are owned by the cited records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | Vault propositions in L0/L1/L2, if present | see record | SRC-1; see record | No actual user claim or warranted premise supplied. |
| [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata) | Some provenance assertions; many fields are policy rather than claims | see record | SRC-1; see record | A confidence number is not an evidence-consuming decision. |
| [EPI-OBJ-memory-instructions](#epi-obj-memory-instructions) | Rules/skills are primarily prescriptions; embedded factual premises may be truth-apt | see record | SRC-1; see record | Host interpretation/compliance unobserved. |
| [EPI-OBJ-inbox-item](#epi-obj-inbox-item) | Imported text, previews and provenance assertions | see record | SRC-1; see record | Preview fidelity and original truth are separate. |
| [EPI-OBJ-proposal-content](#epi-obj-proposal-content) | Proposed summaries, detail and rationale | see record | SRC-1; see record | Particular inferred meaning/entailment not determinable. |
| [EPI-OBJ-proposal-control](#epi-obj-proposal-control) | Action/state are policy; confidence purports to assess a candidate without calibration evidence | see record | SRC-1; see record | Applied/Rejected describe dispatch, not factual verdicts. |
| [RT-OBJ-context-result](runtime.md#rt-obj-context-result) | Selected vault assertions plus IDs/ranks | see record | SRC-1; see record | Score is delivery priority, not truth probability. |
| [EPI-OBJ-usage-store](#epi-obj-usage-store) | Recorded accesses, not demonstrated successful use | see record | SRC-1; see record | Delivery/read counts are not correctness feedback. |
| [RT-CMP-inference-provider](runtime.md#rt-cmp-inference-provider) | Internal truth-apt units not determinable from interfaces | see record | SRC-1; see record | Parameters, exact model identity and internal checks remain opaque. |

Diagnostic vectors, health snapshots and optimization records are assessed with their producing routes below; they have different targets and are not folded into a single knowledge object.

## Authority-route ledger

All rows are architectural assessments, not observations. Where a source-native candidate can contain either factual or policy text, the relation is scoped accordingly. The following tables separate checking from disposition and retention from integration.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-inbox-capture](#epi-rte-inbox-capture) | content transformation | implemented | [EPI-OBJ-inbox-item](#epi-obj-inbox-item) | truth-apt transformation: acquisition/import | External text/link/file enters inbox | see route | see route | see route | Retains candidate | Source warrant unknown; URL/attachment supplies provenance, not endorsement | No canonical admission from capture alone | see route | SRC-1; see route | none | none | URL fetch can fail while a link record is still created. |
| [EPI-RTE-inbox-capture](#epi-rte-inbox-capture) | content transformation | implemented | [EPI-OBJ-inbox-item](#epi-obj-inbox-item) | truth-apt transformation: non-ampliative reshaping | Preview and normalization | see route | see route | see route | Replaces summary/status | Text compaction/truncation only; no truth check | Marks normalized; preview available to proposer | see route | SRC-1; see route | none | none | Truncation can remove qualifications; original text/attachment may remain separately reachable. |
| [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) | content transformation | implemented | [EPI-OBJ-proposal-content](#epi-obj-proposal-content) | truth-apt transformation: non-ampliative reshaping | Heuristic content fields | see route | see route | see route | Copies title/summary/detail to pending candidate | No added factual warrant | Candidate made available to caller | see route | SRC-1; `src-tauri/src/commands/inbox.rs` | none | none | This classification covers copied content, not heuristic action recommendations. |
| [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) | content transformation | implemented | [EPI-OBJ-proposal-content](#epi-obj-proposal-content) | truth-apt transformation: indeterminate | Model content/rationale | see route | see route | see route | Requests and retains generated fields | Generation only; may reshape, derive or conjecture | Can replace non-discard heuristic proposal | see route | SRC-1; `src-tauri/src/commands/inbox.rs` | [EPI-CLM-governed-promotion](#epi-clm-governed-promotion) | intended-versus-implemented | Need actual input/output propositions to separate preservation, entailment and non-entailment; provider accuracy uninspected. |
| [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) | check/evidence production | implemented | [EPI-OBJ-proposal-control](#epi-obj-proposal-control) | no content change | Duplicate identity; response JSON/enum shape | see route | see route | see route | Duplicate discard survives inference replacement; parse failure leaves heuristic fallback | Hash/URL equality and response parseability only | Chooses pending candidate/action, not acceptance | see route | SRC-1; `src-tauri/src/commands/inbox.rs` | none | none | Same URL does not entail identical current content or truth. Confidence is clamped, not calibrated. |
| [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) | disposition/acceptance | implemented | [EPI-OBJ-proposal-control](#epi-obj-proposal-control) | non-truth-apt policy/content update: proposal and item state | Caller reject/apply | see route | see route | see route | Persists Rejected/Applied and action effects | Operational disposition only; no recorded evidence-consuming truth criterion/intended-use decision | Chosen action allowed; rejection is not enforced as an irreversible veto | see route | SRC-1; `src-tauri/src/commands/inbox.rs` | [EPI-CLM-governed-promotion](#epi-clm-governed-promotion) | intended-versus-implemented | Apply has no Pending-state check. `needs_review`/`update_memory` do not merge a canonical body. |
| [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) | retention | implemented | [EPI-OBJ-proposal-content](#epi-obj-proposal-content) | no content change | Proposal JSON; promoted/source Markdown | see route | see route | see route | Durable candidates and admitted files | Retention does not upgrade warrant | Later index/router/query can use admitted content | see route | SRC-1; `src-tauri/src/commands/inbox.rs` | [EPI-CLM-canonical-files](#epi-clm-canonical-files) | none | Derived-from item ID and source URL aid lineage; no accepted-claim integration established. |
| [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-content](#epi-obj-memory-content), [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata) | truth-apt transformation: acquisition/import | Caller-authored canonical write, parsing/indexing | see route | see route | see route | Protection/shape/path checks on specified APIs; scan skips excluded/invalid material but warns on folder violations | Source warrant unknown; validity/protection does not test factual premises | Direct canonical writes bypass proposal review | see route | SRC-1; `src-tauri/src/core/index.rs`; see route | [RT-CLM-protected-edit](runtime.md#rt-clm-protected-edit) | scope-limited | No universal semantic acceptance gate. External edits refresh derived state, not truth judgment. |
| [RT-RTE-context-query](runtime.md#rt-rte-context-query) | operational admission/selection/consumption | implemented | [RT-OBJ-context-result](runtime.md#rt-obj-context-result) | truth-apt transformation: non-ampliative reshaping | Query priority and detail allocation | see route | see route | see route | Ranking and selection | No endorsement or verified relevance license | Selects what caller/provider can see now | see [RT-BAP-context-provider](runtime.md#rt-bap-context-provider) and [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions) | SRC-1; `src-tauri/src/core/scoring.rs`; see route | [RT-CLM-context-start](runtime.md#rt-clm-context-start) | none | Confidence is not a term in inspected compute_score; token accounting is not semantic verification. |
| [RT-RTE-skill-load](runtime.md#rt-rte-skill-load), [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-instructions](#epi-obj-memory-instructions) | non-truth-apt policy/content update: deliver selected instructions and summaries | Skill/dependency or adapter/connector read | see routes | see routes | see routes | Instructional text/pointers, not execution control | Embedded factual premises receive no new warrant | Advises later agent reading/actions | see [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions) | SRC-1; see routes | [RT-CLM-context-start](runtime.md#rt-clm-context-start) | scope-limited | Immediate dependency L1 only; adapter compliance and full-body reading remain host-owned. |
| [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat) | content transformation | implemented | [EPI-OBJ-memory-content](#epi-obj-memory-content) as input; provider text as output | truth-apt transformation: indeterminate | User answer | see route | see route | see route | Provider response forwarded into assistant turn | No answer correctness license from transport success or memory IDs | Displays answer; later history may reuse it | see [RT-BAP-context-provider](runtime.md#rt-bap-context-provider) | SRC-1; see route | none | none | Truth-apt content of a particular answer not determinable; no inspected answer oracle. |
| [EPI-RTE-usage-feedback](#epi-rte-usage-feedback) | behavior/policy adaptation | implemented | [EPI-OBJ-usage-store](#epi-obj-usage-store) | non-truth-apt policy/content update: later score inputs | Successful read/delivery accounting | see route | see route | see route | Durable count/date overlay feeds future priority | Records access, not evidence for the accessed claim | Can alter later selection and decay judgments | see route | SRC-1; see route | none | none | Trace-fed operational adaptation is implemented; improvement is not established. |
| [EPI-RTE-governance-checks](#epi-rte-governance-checks) | check/evidence production | implemented | Related memory L1 texts | truth-apt transformation: entailed derivation | Token-pair occurrence in linked memories | see route | see route | see route | Conflict description for coded pair | Licenses token occurrence, not logical contradiction | UI warning, not admission veto or forced revision | see route | SRC-1; see route | [EPI-CLM-governed-promotion](#epi-clm-governed-promotion) | heuristic-versus-semantic | Concrete counterexample below; shared tags are not tested despite doc comment. |
| [EPI-RTE-governance-checks](#epi-rte-governance-checks) | check/evidence production | implemented | Memory metadata and scratch file ages | no content change | Decay/TTL candidates | see route | see route | see route | Candidate lists | Age/usage threshold, not obsolescence or falsity | Offers removal candidates to UI | see route | SRC-1; see route | none | none | Not automatic withdrawal and no revocation of delivered copies. |
| [EPI-RTE-governance-checks](#epi-rte-governance-checks) | content transformation | implemented | Daily entries | truth-apt transformation: non-ampliative reshaping | Consolidation grouping/count | see route | see route | see route | Suggestions include cloned entries and count summary | Group/count only; no synthesized knowledge or acceptance | Display suggestion | see route | SRC-1; see route | none | none | Entity/Synthesis labels do not establish semantic synthesis. |
| [EPI-RTE-governance-removal](#epi-rte-governance-removal) | disposition/acceptance | implemented | Memory/scratch candidates | non-truth-apt policy/content update: deletion from future local availability | Confirmed UI removal | see route | see route | see route | Delete or error | Operational withdrawal, not refutation | Removes indexed unprotected file, refreshes router | see route | SRC-1; see route | none | none | Scratch path-to-ID conversion can fail to address an indexed memory; UI clears lists after attempts. |
| [EPI-RTE-importance-boost](#epi-rte-importance-boost) | behavior/policy adaptation | implemented | [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata) | non-truth-apt policy/content update: importance | Graph hub suggestion plus user action | see route | see route | see route | Persisted importance increase | Graph degree does not establish truth/utility | Later scoring can prefer boosted memory | see route | SRC-1; see route | none | none | Human-triggered, not autonomous quality learning. |
| [EPI-RTE-health-score](#epi-rte-health-score) | check/evidence production | implemented | Workspace statistics | truth-apt transformation: entailed derivation | Coded health formula | see route | see route | see route | Score/breakdown/snapshot | Formula result over input statistics only | UI diagnostic, no demonstrated content veto | see route | SRC-1; see route | [EPI-CLM-canonical-files](#epi-clm-canonical-files) | proxy-versus-quality | Score is not a truth/accuracy measure; dismissal may reduce pending-suggestion penalty without content repair. |
| [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status) | disposition/acceptance | implemented | Optimization suggestions | non-truth-apt policy/content update: suggestion status | Apply/dismiss suggestion | see route | see route | see route | DB status only | No acceptance of canonical propositions | Changes suggestion visibility/status, not suggested canonical text | see route | SRC-1; see route | [EPI-CLM-governed-promotion](#epi-clm-governed-promotion) | intended-versus-implemented | Independent detectors propose compression, importance, archive, merge and thresholds; no automatic execution follows this apply body. |
| [EPI-RTE-source-tests](#epi-rte-source-tests) | check/evidence production | implemented | Allocator, renderer and detector examples | no content change | Program behavior in specified fixtures | see route | see route | see route | Assertions/diagnostic output if run | Fixture properties only, not truth of fixture text or real answers | Test process can fail; no live epistemic admission consumer traced | see route | SRC-1; see route | none | none | Not executed; tests do not establish observed operation or causal improvement. |
| [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) | lifecycle integration | doctrine only | Accepted proposed knowledge | no content change | Governed promotion as designed | see claim | Proposal describes governance before promotion | Desired canonical update | Intended governed integration | No implemented evidence-consuming acceptance step established in inspected promotion body | File writing/refresh exists separately; not enough for lifecycle integration after acceptance | Intended later vault consumers; no established acceptance-to-integration chain | SRC-1; see claim | [EPI-CLM-governed-promotion](#epi-clm-governed-promotion) | intended-versus-implemented | Does not deny that a trusted caller could perform external review; that decision/criterion/evidence was not supplied. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-canonical-files](#epi-clm-canonical-files) | see claim | SRC-1; see claim; doctrine/design | see claim | [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write), [RT-RTE-context-query](runtime.md#rt-rte-context-query), [EPI-RTE-health-score](#epi-rte-health-score) | None supplied | No intervention comparison | Files own canonical content; telemetry makes usage and proxies observable | Canonical storage does not warrant factual truth; quality proxies unvalidated here. |
| [EPI-CLM-governed-promotion](#epi-clm-governed-promotion) | see claim | SRC-1; see claim; doctrine/design, explicit feature proposal | see claim | [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), [EPI-RTE-governance-checks](#epi-rte-governance-checks), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status) | None supplied | No evidence of prevented misinformation or improved retrieval | Candidate/proposal persistence, duplicate policy and explicit apply/reject exist | Semantic validation-before-promotion is not implemented as the universal gate the proposal desires; this is a proposal, not a failed observed guarantee. |
| [RT-CLM-context-start](runtime.md#rt-clm-context-start) | see claim | SRC-1; see claim; doctrine/design | see claim | [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-skill-load](runtime.md#rt-rte-skill-load) | None supplied | No client-compliance comparison | Tool supports requests for selected context | Instruction does not schedule client calls or validate delivered claims. |
| [RT-CLM-protected-edit](runtime.md#rt-clm-protected-edit) | see claim | SRC-1; see claim; doctrine/design | see claim | [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write), [EPI-RTE-governance-removal](#epi-rte-governance-removal) | None supplied | No deployment isolation audit | API guards protect specified existing memories | Source immutability convention is not truth verification or OS-wide enforcement. |

## Bounded conclusion

**The inspected routes give retained content operational reach without supplying a general truth-acceptance procedure.** Acquisition preserves pointers or attachments on some paths, while previews and optional generated replacements change what downstream consumers actually see. Source warrant is unknown, not inherited merely from `protected`, `confidence`, `source`, `derived_from` or “canonical.” See [EPI-RTE-inbox-capture](#epi-rte-inbox-capture), [EPI-OBJ-proposal-content](#epi-obj-proposal-content), [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write).

**There are real checks, with narrow domains.** Duplicate predicates, shape parsing, protection checks, coded conflict terms, age/usage thresholds, health arithmetic and fixture assertions are independently implemented. They support equality/shape/occurrence/threshold conclusions over their inputs, not factual warrant for an admitted memory. Deterministic conflict descriptions and health totals are entailed only within their encoded domains; no warranted real-world premises are supplied. Model generation is wired, but no particular non-entailed proposition is evidenced, so an ampliative-conjecture classification would exceed the evidence. See [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), [EPI-RTE-governance-checks](#epi-rte-governance-checks), [EPI-RTE-health-score](#epi-rte-health-score), [EPI-RTE-source-tests](#epi-rte-source-tests).

**Disposition is not acceptance.** Apply/reject records operational state, confidence does not gate apply, and rejection is not checked by subsequent apply. No inspected promotion decision records evidence consumed against a truth criterion, intended use and scope. Thus promoted storage and router refresh establish retention/use eligibility, not lifecycle integration after epistemic acceptance. Actual external caller review remains possible but unobserved. Deletion removes future local availability where successful; it neither refutes the text nor revokes copied context. See [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), [EPI-RTE-governance-removal](#epi-rte-governance-removal).

**Later behavior has distinct authority paths.** Code ranks and admits context; providers and hosts interpret text advisory channels. Usage counts feed future ranking without correctness feedback. Governance UI can increase importance or invoke guarded deletion. These are implemented operational adaptations, not demonstrated epistemic improvement. Optimization “apply” is narrower still: a DB disposition, not a canonical rewrite. See [RT-BAP-context-provider](runtime.md#rt-bap-context-provider), [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions), [EPI-RTE-usage-feedback](#epi-rte-usage-feedback), [EPI-RTE-importance-boost](#epi-rte-importance-boost), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status).

No exercised learning benefit or causal quality improvement is established. The usage path is an evidence-responsive priority mechanism, whereas health and optimization provide representations/advice; neither proves content-directed criticism, an autonomous theory-building loop or exercised self-improvement. Provider internals remain independently unassessed, not declared absent. Registered but uninspected journal/task/template/restore paths and missing runtime evidence prevent a system-complete negative. The result is a set of route-specific conclusions, not a single system-wide epistemic score.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memory-content
Label: Memory content

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Identity: L0 summary and L1/L2 factual/descriptive text within the supplied Markdown container. Form: natural language; substrate: canonical Markdown files. Different levels can carry different qualifications; their consistency is not checked by the inspected selector. Producer is the caller or proposal builder, consumer is retrieval/host/provider. SRC-1: `src-tauri/src/core/mcp.rs`, `src-tauri/src/core/engine.rs`. The supplied container provides schema evidence; the rendering assertion below supplies the minimum passage for level-specific consumption.

> assert!(rendered.contains("Alex DC es indie hacker en Madrid."));
> assert!(!rendered.contains("MCP WORKSPACE RULES"));
> --- `src-tauri/src/core/engine.rs`

This is test code, not evidence that the biographical assertion is true or that a real provider consumed it.

#### EPI-OBJ-memory-metadata
Label: Memory metadata

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Identity: symbolic fields selecting ontology, importance, dependencies, provenance, protection and indexing. Substrate: YAML plus runtime usage overlay. These differ from descriptive bodies because fixed code interprets them. Confidence/provenance assertions are not backed by a required factual evaluator in these constructors. SRC-1: `src-tauri/src/core/mcp.rs`, `src-tauri/src/core/scoring.rs`.

> confidence: 0.9,
> tags: params.tags,
> related: vec![],
> --- `src-tauri/src/core/mcp.rs`

> + weights.access_frequency * access_frequency
> + weights.graph * graph_proximity;
> --- `src-tauri/src/core/scoring.rs`

#### EPI-OBJ-memory-instructions
Label: Memory instructions

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Identity: natural-language rule/skill prescriptions in memory summaries/bodies, with symbolic role and dependency selectors. Substrate: canonical Markdown; delivery substrates include generated adapters and tool strings. This is the instruction-consumption part, not a claim that all memories are instructions. Same file can contain factual premises; this record separates their behavioral use. Source evidence and consumer distinction: [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions), [RT-RTE-skill-load](runtime.md#rt-rte-skill-load), SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/core/mcp.rs`.

#### EPI-OBJ-inbox-item
Label: Inbox item

Identity: `InboxItem` persisted as inbox Markdown, manifest metadata and optional copied attachments. Form: natural-language imported/edited content and previews, symbolic capture/status/hash/source fields; attachment encoding can be opaque. Closest supplied [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal) is a separate derived proposal; [RT-OBJ-memory](runtime.md#rt-obj-memory) is the separate canonical destination. SRC-1: `src-tauri/src/commands/inbox.rs`.

> content_hash: hash_str(url.as_str()),
> --- `src-tauri/src/commands/inbox.rs`

> let needs_extraction = !is_text_like(&source);
> --- `src-tauri/src/commands/inbox.rs`

URL equality is used as an identity proxy, not a content-truth check. Non-text artifacts are retained without implemented OCR in the inspected import body.

#### EPI-OBJ-proposal-content
Label: Proposal content

Part of: [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal)

Identity: natural-language `l0`, L1/L2 and rationale inside persisted proposal JSON. Heuristics copy title/summary/detail; provider inference may replace these fields. Application may write that replacement into a protected source memory; protection is not a fidelity check. SRC-1: `src-tauri/src/commands/inbox.rs`.

> l1_content: parsed.l1_content.or_else(|| Some(item.summary.clone())),
> l2_content: parsed.l2_content.or_else(|| Some(item.l2_content.clone())),
> --- `src-tauri/src/commands/inbox.rs`

> let mut l2 = proposal
>     .l2_content
>     .clone()
>     .unwrap_or_else(|| item.l2_content.clone());
> --- `src-tauri/src/commands/inbox.rs`

Thus source routing can retain provenance and attachments while its served Markdown contains model-selected content. Imported truth warrant and transformation fidelity remain separate unknowns.

#### EPI-OBJ-proposal-control
Label: Proposal control

Part of: [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal)

Identity: symbolic action/state/confidence/origin/derivation fields in proposal JSON; fixed Rust branches consume action, caller commands select disposition. Confidence is stored/clamped, not an evidence record or apply threshold. Source evidence: [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), SRC-1: `src-tauri/src/commands/inbox.rs`.

> proposal.state = ProposalState::Rejected;
> proposal.modified = Utc::now();
> write_proposal(&root, &proposal)?;
> --- `src-tauri/src/commands/inbox.rs`

> let mut proposal = load_proposals(&root)?
>     .into_iter()
>     .find(|proposal| proposal.id == input.proposal_id)
>     .ok_or_else(|| format!("Proposal not found: {}", input.proposal_id))?;
> --- `src-tauri/src/commands/inbox.rs`

The inspected apply lookup proceeds to load the item and dispatch action without checking proposal state. Rejection persists a disposition but does not enforce future non-application.

#### EPI-OBJ-usage-store
Label: Memory usage store

Identity: `MemoryUsageStore.memories` keyed by memory ID, containing last_access and access_count. Form: symbolic dates/counts; substrate: `.cache/memory-usage.json`, located by SystemPaths. Distinct from [RT-OBJ-memory](runtime.md#rt-obj-memory): sidecar runtime data overlays its metadata without rewriting the canonical frontmatter. Closest supplied [RT-RTE-context-query](runtime.md#rt-rte-context-query) already notes access accounting but does not declare this separate retained object. SRC-1: `src-tauri/src/core/usage.rs`, `src-tauri/src/core/paths.rs`.

> self.root.join(".cache/memory-usage.json")
> --- `src-tauri/src/core/paths.rs`

The update and later consumers are evidenced in [EPI-RTE-usage-feedback](#epi-rte-usage-feedback).

### Routes

#### EPI-RTE-inbox-capture
Label: Inbox capture

Distinct from [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal): creates/edits its upstream items, rather than deriving or applying proposals. Endpoints: caller text, URL or file → capture/preview and metadata → inbox file/manifest; normalize edits capture state/summary. Owner: command code, with caller supplying content and trigger. Context: active root and source bytes. Mode: open capture, no expected-answer oracle. URL parser/public-host check and HTTP success assess fetch eligibility, not truth; failed fetch falls back to empty preview. Rejection/recovery: invalid URL/I/O may error; caller can edit/retry. Original attachment retained on file import. Guidance is capture schema, not an editorial acceptance criterion. SRC-1: `src-tauri/src/commands/inbox.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: InboxItem(s), normalized item(s), or error; manifest/log/event effects accompany writes.
- Later read-back: persisted items reload for proposal generation; attachment and original-file references may remain after previewing.
- Delegated visibility: proposal provider receives selected item fields; captured attachment bytes are not automatically OCR text.
- Selection predicate: caller input/path set or item IDs; text-like classification determines preview/extraction flags.
- Invalidation or expiry: editing replaces fields/hash; normalization changes status and fills blank summary; no truth-based expiry found in these bodies.
- Activation or effect: durable candidate capture is wired; canonical admission and model benefit are not observed.
- Evidence limits: imported source warrant unknown; lossy UTF-8, HTML stripping and 280-character preview can omit context. Normalized is a capture-state label.

> fn preview_text(value: &str) -> String {
>     let compact = value.split_whitespace().collect::<Vec<_>>().join(" ");
>     compact.chars().take(280).collect()
> }
> --- `src-tauri/src/commands/inbox.rs`

Concrete deduction, not target execution: input `React\n\tand Vue` becomes `React and Vue`; 281 ASCII `x` characters become 280. This changes layout/length, not a new inferred proposition. Truncating a long qualification can nevertheless degrade what a later reader can recover from the preview alone.

#### EPI-RTE-usage-feedback
Label: Usage feedback

Distinct continuation across [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-skill-load](runtime.md#rt-rte-skill-load) and desktop memory reads: it is the durable trace-to-future-priority loop, not their immediate returns. Endpoints: selected/read ID → count/date store → scan overlay → scoring/decay consumers. Owner: usage/index/scoring code; state: root-specific JSON and memory metadata. No model or human judges correctness. Open operation; no answer oracle. The recorded behavior is access/delivery, not subsequent successful application. SRC-1: `src-tauri/src/core/usage.rs`, `src-tauri/src/core/index.rs`, `src-tauri/src/core/scoring.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/memory.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: access-recording success/error; MCP ignores its failure, desktop get_memory propagates it.
- Later read-back: scans overlay persisted last_access/access_count; score uses recency and normalized access frequency; decay also consumes usage metadata.
- Delegated visibility: later caller receives changed priorities/content, not a separately validated fact.
- Selection predicate: MCP loaded IDs, skill plus required IDs, or explicit desktop memory ID; optional skill dependencies are not recorded by the inspected loop.
- Invalidation or expiry: later access overwrites date and increments count; unreadable/malformed usage store loads empty and scan falls back to modified date/zero count.
- Activation or effect: automatic durable update and future scoring dependence are wired, not observed; no improvement objective or correctness feedback is evaluated.
- Evidence limits: reads can change priority without semantic approval; usage is an exposure trace. Provider quality and later successful use remain unknown.

> meta.last_access = usage.last_access;
> meta.access_count = usage.access_count;
> --- `src-tauri/src/core/usage.rs`

> entry.last_access = timestamp;
> entry.access_count = entry.access_count.saturating_add(1);
> --- `src-tauri/src/core/usage.rs`

#### EPI-RTE-governance-checks
Label: Governance checks

No counterpart in supplied routes: complements, rather than duplicates, [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status). Endpoints: indexed memories / scanned metadata / daily entries / scratch directory → governance functions → UI diagnostics. The separate targets are related-memory token-pair occurrence, coded decay threshold, scratch age in days and daily-entry type/count. Owners: Rust detectors; UI/human may interpret or initiate separate actions. No expected factual answer oracle. Mode: open workspace diagnostics. Related L1s are tokenized and checked against seven fixed technology pairs; tags are not tested by this body. Consolidation groups decision/idea entries at count at least three and labels ontology; it does not synthesize explanations. MCP log_session writes to session logs, while consolidation reads daily logs: no inspected automatic bridge equates those streams. SRC-1: `src-tauri/src/core/governance.rs`, `src-tauri/src/commands/governance.rs`, `src/views/GovernanceView.tsx`, `src-tauri/src/core/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: conflict, decay, scratch or consolidation vectors displayed in the UI, or command errors.
- Later read-back: inapplicable — these command results are transient; retained source memories/logs are reread on refresh, not a persisted evaluator verdict.
- Delegated visibility: human UI receives conflict descriptions and candidate/suggestion lists; no semantic gate is inserted into MCP save or proposal apply.
- Selection predicate: related IDs with opposing coded terms; configured decay threshold; scratch modification age greater than TTL; at least three entries of supported daily type.
- Invalidation or expiry: refresh recomputes; missing/unreadable files may be omitted; no delivered-context revocation.
- Activation or effect: advisory diagnostic production/display is wired; removal and importance interventions use separate routes below.
- Evidence limits: occurrence/age/grouping is not factual contradiction, obsolescence or accepted synthesis. No observed accuracy or exercised review supplied.

> if (a_has_first && b_has_second) || (a_has_second && b_has_first) {
> --- `src-tauri/src/core/governance.rs`

> "{} mentions '{}' but {} mentions '{}'",
> a.meta.id, term_a, b.meta.id, term_b
> --- `src-tauri/src/core/governance.rs`

Concrete counterexample by implementation deduction: with `a.related = [b]`, a L1 `React` and b L1 `Vue` trigger the pair. Both can be true descriptions of different projects; neither text states exclusive technology choice. Conversely unlinked contradictory memories are not compared. The check supports occurrence of the pair, not inconsistency or placement of blame. This is a defeater of an overly broad semantic-conflict claim, not an executed test.

> entries: ideas.iter().map(|e| (*e).clone()).collect(),
> suggested_ontology: MemoryOntology::Synthesis,
> --- `src-tauri/src/core/governance.rs`

#### EPI-RTE-governance-removal
Label: Governance removal

Distinct UI disposition route using [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write)'s guarded deletion API. Endpoints: decay/scratch candidates → confirmation dialog → ID-directed delete_memory → filesystem removal/index/router effects. Proposed by detectors, decided/vetoed by human confirmation; protected-memory guard can reject. Mode: maintenance, no answer oracle. Criterion is the candidate threshold plus user choice, not an evidence-consuming factual refutation. Archive labels invoke deletion, not an inspected move to an archive. SRC-1: `src/views/GovernanceView.tsx`, `src-tauri/src/commands/memory.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deletion success/error, UI list removal and refreshed router on successful command completion.
- Later read-back: successful file removal excludes it from future scans; existing copied strings/history remain outside revocation.
- Delegated visibility: UI receives outcome; future context consumers see remaining files; no correction notice is sent to prior recipients.
- Selection predicate: user confirms candidate(s); scratch derives ID from filename before calling indexed-memory deletion.
- Invalidation or expiry: direct file removal, no transaction/automatic undo shown; removal of index entry precedes filesystem operation and can leave inconsistent transient state on error.
- Activation or effect: guarded removal and regeneration are wired; scratch IDs can be absent from index and bulk UI code skips errors then clears candidate lists.
- Evidence limits: no actual deletion/restore trace supplied; no semantic rejection or guarantee every scratch candidate is removed. Backup/restore bodies were not inspected, so broader recovery remains unknown.

> for (const m of decayCandidates) {
>   try { await deleteMemory(m.id); } catch { /* skip */ }
> }
> setDecayCandidates([]);
> --- `src/views/GovernanceView.tsx`

> ensure_not_protected(meta, "deleting it")?;
> --- `src-tauri/src/commands/memory.rs`

> fs::remove_file(&path).map_err(|e| format!("Failed to delete {}: {}", path, e))?;
> --- `src-tauri/src/commands/memory.rs`

#### EPI-RTE-importance-boost
Label: Importance boost

Distinct from [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status): this UI path actually persists a priority change through memory save. Endpoints: explicit graph degree/importance mismatch → god-node list → user boost → incremented importance → future score. Owners: graph detector, human trigger and guarded save command. Context: indexed memories and explicit graph links. Selection uses normalized degree minus importance >0.2 or degree >=2, orders by mismatch/degree, truncates to 20. No answer oracle or claim correctness target. Guidance is a hub-priority heuristic, not criticism of the memory's claims. User can refrain; save guard can reject; recovery is another authorized metadata edit. SRC-1: `src-tauri/src/core/graph.rs`, `src/views/GovernanceView.tsx`, `src-tauri/src/commands/memory.rs`, `src-tauri/src/core/scoring.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved memory or displayed error and refreshed local importance value.
- Later read-back: saved importance enters canonical metadata and later score computation.
- Delegated visibility: later context consumer can receive different ranked content; no truth judgment accompanies it.
- Selection predicate: coded graph criterion followed by explicit user boost; increment is capped at 1.0.
- Invalidation or expiry: another edit can replace importance; no automatic decay of the boost or quality rollback demonstrated.
- Activation or effect: durable policy change is wired; changed retrieval and benefit are not observed.
- Evidence limits: graph position is not truth or causal utility evidence; not an autonomous semantic evaluator.

> const newImportance = Math.min(1.0, memory.meta.importance + 0.2);
> --- `src/views/GovernanceView.tsx`

> let mismatch_score = normalized_degree - memory.meta.importance;
> --- `src-tauri/src/core/graph.rs`

#### EPI-RTE-health-score
Label: Health score

Distinct from supplied [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status): assesses a workspace-wide proxy vector and stores a snapshot, not suggestion disposition. Endpoint: scanned entries plus observability stats/pending suggestions → fixed arithmetic → score/breakdown/summary and attempted SQLite snapshot. Owner/evaluator: Rust health code. Target domain: access coverage, estimated-budget efficiency, last-access freshness, ontology diversity/concentration and pending-suggestion penalties. No truth/answer oracle. Mode: requested workspace diagnostic; human may act on advice, but this body neither revises content nor admits a claim. SRC-1: `src-tauri/src/core/health.rs`, `src-tauri/src/commands/observability.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HealthScore or error; empty workspace returns zero without the normal snapshot step.
- Later read-back: attempted daily score/breakdown snapshot is exposed by health-history command; current computation rereads source statistics.
- Delegated visibility: API/UI receives score and Spanish summary; no provider correctness certificate or forced canonical update.
- Selection predicate: fixed 14-day/access/token/type/suggestion components; weights 25%, 25%, 20%, 15%, 15%; summary thresholds >70 and >40.
- Invalidation or expiry: subsequent daily insert replaces that date's snapshot; fresh calls recompute; stats errors may default and snapshot failures are ignored.
- Activation or effect: computation and snapshot attempt wired; observed governance benefit absent from supplied evidence.
- Evidence limits: exact arithmetic result is entailed by inputs/formula, but inputs are telemetry rather than validated knowledge; no calibration to factual accuracy or task outcomes supplied.

> let weighted = coverage * 0.25
>     + efficiency * 0.25
>     + freshness * 0.20
>     + balance * 0.15
>     + cleanliness * 0.15;
> --- `src-tauri/src/core/health.rs`

#### EPI-RTE-source-tests
Label: Source tests

Distinct from runtime delivery routes: development evaluators, not live answer acceptance. SRC-1: `src-tauri/src/core/engine.rs` allocator/assembler tests, `src-tauri/src/core/governance.rs` conflict fixtures and `src-tauri/tests/diagnose_vault_query.rs` ignored diagnostic. Owners: test author specifies expected fixture properties; test runner would decide assertions, diagnostic prints for human inspection. Named targets: L2 cap/relative allocation, loaded-content inclusion/prelude exclusion and related-term detection. Expected outputs come from explicit fixture assertions, not a factual answer corpus. Mode: bounded program fixtures, plus open real-vault diagnostic; none executed in this analysis.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: assertion pass/fail or printed diagnostic if run; no supplied test output.
- Later read-back: inapplicable — inspected tests do not retain accepted knowledge for later agent use.
- Delegated visibility: developer/test runner receives assertions or console output; no live chat gate traced from these tests.
- Selection predicate: source-selected fixtures; ignored diagnostic uses environment/default vault/query/budget.
- Invalidation or expiry: fixture/source changes require rerun; no test result supplied to invalidate or promote.
- Activation or effect: executable evaluator source exists; no exercised acceptance, deployment gate or benefit established.
- Evidence limits: fixture validity is narrow; passing would not establish real-world relevance, answer truth, process explanation, component causal benefit or transfer. The diagnostic has no expected factual answer.

> let capped = select_load_level(0.88, 0.9, 3, false, 1_000, 10, 20, 30);
>
> assert!(matches!(capped, Some((LoadLevel::L1, _))));
> --- `src-tauri/src/core/engine.rs`

> #[test]
> #[ignore]
> fn diagnose_chat_context_for_query() {
> --- `src-tauri/tests/diagnose_vault_query.rs`

### Claims

#### EPI-CLM-canonical-files
Label: Canonical files

Distinct from supplied [RT-CLM-context-start](runtime.md#rt-clm-context-start) and [RT-CLM-protected-edit](runtime.md#rt-clm-protected-edit): public product thesis about canonical storage and governable context, not a tool-use instruction or mutation guard. SRC-1: `README.md`, doctrine/design.

> - The canonical source of truth is the workspace file tree.
> --- `README.md`

> - Context quality must be observable and governable.
> --- `README.md`

The first claim is supported as canonical storage ownership, not epistemic truth of all stored text. The second is an objective: telemetry/governance routes provide observability/proxy controls without supplied evidence that factual quality is measured.

#### EPI-CLM-governed-promotion
Label: Governed promotion

No supplied claim counterpart: source-native feature proposal for governance before promotion, including consistency and provenance checks. SRC-1: `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`, doctrine/design. It is explicitly aspirational, not an observed guarantee.

> Estado: propuesta de feature
> --- `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`

> La gobernanza evalúa la propuesta antes de promoverla.
> --- `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`

> - no entra en conflicto con memorias relacionadas
> - cumple el contrato `L0/L1/L2`
> - tiene trazabilidad respecto al origen
> --- `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`

> - evita que la IA escriba conocimiento dudoso como verdad permanente
> --- `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`

Compared with [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), implemented JSON proposals and stateful dispatch supply part of the design. Apply does not invoke semantic conflict checks or record an evidence-consuming truth acceptance. Compared with [EPI-RTE-governance-checks](#epi-rte-governance-checks), keyword warnings are neither full semantic consistency checks nor a promotion veto. The proposal's own stated limits on reliable unsupervised semantic judgment are consistent with this narrower account.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
