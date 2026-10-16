---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Pond's archival warrant, structural admission, recall authority and operational evaluators at the frozen revision."
run-id: AAS-2026-10-14-pond-7a589a889ca1-01
reviewed-boundary: "0c440e130faf44052d0d896a585e572090079f1f"
---

# Pond epistemic report

## Source-and-claim boundary

The question is what Pond licenses a later agent to infer from archived sessions, and which checks actually change admission, use or recovery. The whole-system functional boundary and external exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation, doctrine/design and attributed measurements, not a newly observed Pond or host execution. This report inspected source text only.

Pond explicitly distinguishes its archive from a distilled-fact memory layer. Its consequential claims concern lossless preservation, cross-client recall/restoration and small ranked context, not autonomous discovery of verified knowledge: see [EPI-CLM-archive-recall](#epi-clm-archive-recall). The narrower operational evaluation routes matter nonetheless: admission checks, deletion detection, model-identity diagnosis, copy verification and retrieval benchmarks produce judgments with different targets and forces. None is interchangeable with judging whether a historical explanation is true.

### Coverage

“Direct” below denotes this analyst's source reads, including scoped dispatch/registration searches; “supplied” denotes the runtime's findings. All paths are SRC-1 commit-relative anchors. A supplied finding is not represented as a fresh source audit.

| Entry point or operation | Source path | Coverage and records; prevented conclusion |
|---|---|---|
| CLI dispatch: sync, optimize, adapters, serve/MCP, search, get, resume, config, schedule, skill, storage, creds, copy, SQL; init/status/support commands | `packages/pond/src/main.rs` | Direct dispatch search and sync/optimize, resume/SQL/copy, diagnosis/recovery ranges. Supplied capture/configuration, recall and restore: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-adapter-config](runtime.md#rt-rte-adapter-config), [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall), [RT-RTE-session-restore](runtime.md#rt-rte-session-restore). Setup/credential/scheduling internals not fully inspected here; no complete operational-security or scheduler-reliability conclusion. |
| HTTP ingest/search/gets/SQL, four MCP tools and schema instructions | `packages/pond/src/transport.rs`, `packages/pond/src/handlers.rs` | Direct router/tool-registration searches and schema instructions; supplied handler traces: [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql), [RT-CLM-transport-gates](runtime.md#rt-clm-transport-gates). No extra model-evaluation tool identified in those registrations. Not an exhaustive handler audit. |
| Canonical ingestion, source-field extraction, index-text construction | `packages/pond/src/sessions.rs`, `packages/pond/src/adapter/extract.rs` | Direct: [EPI-RTE-ingest-check](#epi-rte-ingest-check), [EPI-RTE-ingest-disposition](#epi-rte-ingest-disposition), [EPI-RTE-field-extraction](#epi-rte-field-extraction), [EPI-RTE-search-projection](#epi-rte-search-projection). Individual codecs remain uninspected; universal codec fidelity and upstream source truth are not established. |
| Rendered recall and Pi output bounding/instructions | `packages/pond/src/render.rs`, `packages/pi-pond/src/tools.ts`, `packages/pond/SKILL.md` | Direct: [EPI-RTE-recall-rendering](#epi-rte-recall-rendering); supplied [RT-BAP-recall-guidance](runtime.md#rt-bap-recall-guidance). Session/message renderer bodies not fully inspected here; supplied pagination/expansion account bounds conclusions. |
| Pi lifecycle hooks, interactive recall/restore; OpenClaw/Hermes projections | `packages/pi-pond/index.ts`, `packages/openclaw-pond/index.ts`, `packages/hermes-pond/__init__.py` | Direct Pi registration/lifecycle reads and registration searches for all three; supplied [RT-RTE-openclaw-tools](runtime.md#rt-rte-openclaw-tools), [RT-BAP-session-switch](runtime.md#rt-bap-session-switch), [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall). Other interactive picker bodies and host interpretation uninspected; no demonstrated host acceptance or continuation. |
| Optional embedding and replacement of stale-model vectors | `packages/pond/src/embed.rs`, `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs` | Direct loader/inference, one-row model-ID probe and maintenance consumer: [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder), [EPI-RTE-maintenance-check](#epi-rte-maintenance-check), [EPI-RTE-maintenance-recovery](#epi-rte-maintenance-recovery). Remote weights unpinned/uninspected; no independent cross-lingual quality or training conclusion. |
| OpenClaw deletion reconciliation | `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs` | Direct detector contract, dispatch-to-summary and multi-root preservation policy: [EPI-RTE-deletion-detection](#epi-rte-deletion-detection). DB helper internals uninspected; no authenticated deletion decision or whole-codebase erasure audit. |
| Store copy/archive transfer and verification | `packages/pond/src/main.rs` | Direct store-copy admission and composite-key checker: [EPI-RTE-copy-verification](#epi-rte-copy-verification). Archive codecs/copy substrate internals remain uninspected; verification does not establish byte equality or truthful transcript content. |
| Retrieval evaluator, context-cost report | `ops/search-benchmarks/bench.py`, `docs/benchmarks/recall-context-cost.md` | Direct ground-truth matching, verify/score routines and full cost report: [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark), [EPI-CLM-ranked-context](#epi-clm-ranked-context). Captured-arm/fusion routines, full query corpus and benchmark artifacts not inspected; no observed current-pin ranking experiment. |
| Adapter development, test/e2e suites, fleet drivers | `skills/pond-add-adapter/SKILL.md`, `packages/pond/tests/integration/search.rs`, `ops/e2e/README.md`, `ops/examples/pi-fleet/worker.sh` | Supplied development/fleet account: [RT-RTE-adapter-development](runtime.md#rt-rte-adapter-development). Scoped searches identify search assertions and e2e's non-CI operation; suites and results not fully read or run. No passing-test, complete conformance, release-admission or independent agent-benefit conclusion. |

There is no supplied host transcript linking an archive row to a checked answer, no independently inspected reference evidence establishing the truth of imported decisions, and no intervention isolating downstream benefit. These prevent observed acceptance, source-truth warrant and causal improvement conclusions respectively. Available but uninspected codecs, tests, research/design files and deployment internals prevent a system-complete negative about every conceivable checking route. The bounded negatives below concern the inspected archival/recall routes, not all repository contents.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-archive-fields](#epi-obj-archive-fields) | Imported statements, decisions, tool observations and their recorded role/time/lineage; particular proposition truth is not determinable without an instance | Historical session evidence, not accepted distilled facts | SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/adapter/extract.rs` | Source origin is not source truth; cap and codec qualifications apply |
| [EPI-OBJ-search-text](#epi-obj-search-text) | Selected conversational text/file descriptors from those records | Retrieval projection | SRC-1 `packages/pond/src/sessions.rs` | Excludes tool results, reasoning and injected scaffolding; cannot establish absence from the full archive |
| [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder) | No individuated proposition in inspected numerical weights/vectors | Semantic retrieval; form, substrate and fixity see record | SRC-1 `packages/pond/src/embed.rs` | Similarity is not truth; exact downloaded revision and internal learned content uninspected |
| [RT-OBJ-prompt-guidelines](runtime.md#rt-obj-prompt-guidelines) | Policy instructions plus warnings about retrieval scope and temporal supersession | Requested interpretation/selection policy; identity see record | SRC-1 `packages/pi-pond/src/tools.ts`, `packages/pond/SKILL.md` | Latest text is not automatically most warranted; model compliance unobserved |
| [EPI-OBJ-row-outcome](#epi-obj-row-outcome) | Structural ingest errors or operational row eligibility | Canonical admission result | SRC-1 `packages/pond/src/sessions.rs` | Structural validity is not truth of a body |
| [EPI-OBJ-maintenance-finding](#epi-obj-maintenance-finding) | Model-ID mismatch/layout/index condition | Maintenance trigger | SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs` | Sampled ID/metadata does not prove complete artifact fixity |
| [EPI-OBJ-reconciliation-report](#epi-obj-reconciliation-report) | Deleted-archive/live-entry classification | Operator report | SRC-1 `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs` | Detection is not implemented withdrawal |
| [EPI-OBJ-storage-verify](#epi-obj-storage-verify) | Key coverage, duplicates and index presence | Copy completion result | SRC-1 `packages/pond/src/main.rs` | Membership is not payload equality |
| [EPI-OBJ-benchmark-ranks](#epi-obj-benchmark-ranks) | Rank of a nominated ID-prefix/text anchor and derived retrieval metrics | Developer comparison evidence | SRC-1 `ops/search-benchmarks/bench.py` | Anchor detection is not factual answer correctness; intended label validity unverified |

## Authority-route ledger

Each record owns its endpoints, status fields and read-back details. Ledger cells say `see` where those fields are already declared. “Implemented” is architectural wiring, never an assertion that the route operated in this run.

Route ID: [EPI-RTE-field-extraction](#epi-rte-field-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields)
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown, with over-cap content fidelity degraded.
Transition or check target: External source fields to extracted/capped canonical values.
Evaluator/condition and domain: Deterministic extraction and per-leaf byte cap, not a truth evaluator.
Activation and timing: During source decoding before storage; see record.
Possible or observed result: Extracted value or head-preserving marked truncation; no operation observed.
Implemented force: Enforcing value bounding.
Epistemic authority and scope: Evidence of what survives extraction, not certification of the source claim.
Operational authority: Behavior permitted, blocked, or changed: Subsequent archive/replay uses bounded values; discarded tails cannot be recovered from this projection alone.
Behavioral-authority path: Adapter to store and later recall/restore, enforcing at extraction and advisory as historical evidence at host interpretation; cross-session horizon.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/adapter/extract.rs`; see record.
Claim IDs or none: [EPI-CLM-archive-recall](#epi-clm-archive-recall)
Mismatch marker or none: Unqualified losslessness has a concrete cap exception.
Gap/limit: Not every codec inspected; source warrant and truth remain unknown.

Route ID: [EPI-RTE-ingest-check](#epi-rte-ingest-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-row-outcome](#epi-obj-row-outcome)
Content/update relation: truth-apt transformation: entailed derivation; error conditions follow from fields under the inspected validator rules, not from warranted historical claims.
Transition or check target: Empty trimmed source-agent and parent-message-without-parent-session structure.
Evaluator/condition and domain: Software predicates over canonical schema; see record.
Activation and timing: Session-event admission before substream buffering.
Possible or observed result: RowOutcome error or eligible session; see record.
Implemented force: Produces structural results consumed by the linked disposition.
Epistemic authority and scope: License only to report these field violations.
Operational authority: Behavior permitted, blocked, or changed: See [EPI-RTE-ingest-disposition](#epi-rte-ingest-disposition).
Behavioral-authority path: Validator result to buffering/writer, enforcing during ingestion; immediate batch horizon.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/sessions.rs`; see record.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No check of task-answer truth, tool-result authenticity or explanation validity in these predicates.

Route ID: [EPI-RTE-ingest-disposition](#epi-rte-ingest-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields)
Content/update relation: no content change
Transition or check target: Retention eligibility after the linked structural checks.
Evaluator/condition and domain: Software, canonical schema/order/storage keys; see record and [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).
Activation and timing: Before buffered substream reaches store.
Possible or observed result: Reject malformed session; otherwise proceed toward additive insertion.
Implemented force: Enforcing rejection or operational admission, not epistemic acceptance.
Epistemic authority and scope: No recorded evidence-consuming decision that an archived historical claim is true for answering a future question.
Operational authority: Behavior permitted, blocked, or changed: Malformed substream cannot anchor later message/part admission; admissible rows may enter archive.
Behavioral-authority path: Validator to store writer; enforcing per-batch, with later archive reachability.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/sessions.rs`; see record.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Starting sync or naming a harness is not per-claim human approval.

Route ID: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields)
Content/update relation: no content change
Transition or check target: Eligible canonical events to durable messages/parts/sessions.
Evaluator/condition and domain: See record; additive keys and immutable-label handling are storage rules.
Activation and timing: See record.
Possible or observed result: See record; separate table commits and convergent retry, not observed success.
Implemented force: Durable historical availability.
Epistemic authority and scope: Retention before semantic acceptance; no upgrade from testimony to certified knowledge.
Operational authority: Behavior permitted, blocked, or changed: Rows become candidates for future search/get/SQL/restore.
Behavioral-authority path: See record; archive tables to requested consumers, cross-session horizon.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/sessions.rs`; see record and [RT-CLM-ingest-recovery](runtime.md#rt-clm-ingest-recovery).
Claim IDs or none: [EPI-CLM-archive-recall](#epi-clm-archive-recall)
Mismatch marker or none: none
Gap/limit: Retention is not lifecycle integration after accepted knowledge.

Route ID: [EPI-RTE-search-projection](#epi-rte-search-projection)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-text](#epi-obj-search-text)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Canonical parts to indexed text.
Evaluator/condition and domain: Fixed role/provenance/part selection; see record.
Activation and timing: At ingestion before durable index-text storage.
Possible or observed result: Restricted conversational projection or null search text.
Implemented force: Enforcing content selection.
Epistemic authority and scope: Selected source excerpts, not a complete record or distilled decision.
Operational authority: Behavior permitted, blocked, or changed: Search excludes tool/reasoning/injected parts; other surfaces can still read canonical parts.
Behavioral-authority path: Buffering to stored search_text to retrieval index; enforcing projection with cross-session retrieval consequences.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/sessions.rs`; see record.
Claim IDs or none: [EPI-CLM-archive-recall](#epi-clm-archive-recall)
Mismatch marker or none: Corpus storage is broader than ordinary search coverage.
Gap/limit: Codec provenance correctness unverified; search miss is not archive absence.

Route ID: [EPI-RTE-recall-rendering](#epi-rte-recall-rendering)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-text](#epi-obj-search-text)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Selected hits to bounded readable context.
Evaluator/condition and domain: Deterministic rendering/byte limits; see record.
Activation and timing: At requested recall, then plugin relay.
Possible or observed result: Bounded session-grouped hit text with follow-up instructions.
Implemented force: Enforcing omission/formatting, advisory warnings to host model.
Epistemic authority and scope: Delivered historical excerpts; neither complete record nor authoritative latest decision.
Operational authority: Behavior permitted, blocked, or changed: Host receives only rendered/bounded text; omitted content requires another explicit read.
Behavioral-authority path: MCP/CLI renderer to Pi bounded relay, then host model; enforcing byte/selection limits, advisory interpretation, current recall turn.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/render.rs`, `packages/pi-pond/src/tools.ts`; see record.
Claim IDs or none: [EPI-CLM-ranked-context](#epi-clm-ranked-context)
Mismatch marker or none: “Complete ranked answer” exceeds the guaranteed delivered evidence.
Gap/limit: A clipped quotation can lack its later correction; warnings do not prove follow-up.

Route ID: [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields), [EPI-OBJ-search-text](#epi-obj-search-text)
Content/update relation: no content change
Transition or check target: Candidate selection for requested historical search/get reads.
Evaluator/condition and domain: See record: caller query/filter/ID; deterministic planner and optional embedding-based ranking.
Activation and timing: See record.
Possible or observed result: Ranked snippets, chronological pages or expanded parts.
Implemented force: Ranking and bounded delivery; not claim acceptance.
Epistemic authority and scope: Evidence about the archived record under selected scope, not factual endorsement.
Operational authority: Behavior permitted, blocked, or changed: Selected material reaches requesting host; vector-disabled requests refused and unembedded corpus fallback handled as in record.
Behavioral-authority path: See record; tool result to host interpretation, advisory as task evidence, current turn.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/handlers.rs`; see record.
Claim IDs or none: [EPI-CLM-archive-recall](#epi-clm-archive-recall), [EPI-CLM-ranked-context](#epi-clm-ranked-context)
Mismatch marker or none: none
Gap/limit: Vector proximity and recency do not establish factual warrant or host acceptance.

Route ID: [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields), [EPI-OBJ-search-text](#epi-obj-search-text)
Content/update relation: no content change
Transition or check target: SQL query admission and archive-table read/analytics.
Evaluator/condition and domain: See record: caller SQL; shared read-only grammar/planning gate.
Activation and timing: See record.
Possible or observed result: Rows/text, aggregate query result or export file; rejected query on invalid grammar.
Implemented force: Enforcing query admission and read/export effects, not claim acceptance.
Epistemic authority and scope: SQL aggregates can derive corpus-relative results, conditional on query interpretation and stored premises; no particular checked proposition supplied.
Operational authority: Behavior permitted, blocked, or changed: Gate blocks corpus mutation but not export writes; reads can cover tool bodies outside ordinary search.
Behavioral-authority path: See record; parser/planner to rows/export to caller, enforcing query gate and advisory evidence, query/export horizon.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/sql.rs`; see record.
Claim IDs or none: [EPI-CLM-archive-recall](#epi-clm-archive-recall)
Mismatch marker or none: none
Gap/limit: Read-only is not authorization, payload truth certification or side-effect freedom.

Route ID: [RT-RTE-openclaw-tools](runtime.md#rt-rte-openclaw-tools)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields), [EPI-OBJ-search-text](#epi-obj-search-text)
Content/update relation: no content change
Transition or check target: Plugin tool availability and projected request scope.
Evaluator/condition and domain: See record: caller context/scope/visibility policy; software factory and execution checks.
Activation and timing: See record; factory registration and request execution.
Possible or observed result: Withheld tool, scoped search or allowed get/SQL relay.
Implemented force: Enforcing local projection policy, not epistemic warrant or universal corpus ACL.
Epistemic authority and scope: No change to truth warrant of returned history.
Operational authority: Behavior permitted, blocked, or changed: Sub-agent factory tools withheld; SQL requires all visibility; get IDs are not independently project-confined.
Behavioral-authority path: See record; plugin policy to host grant/request to MCP relay, enforcing within this projection, per-registration/request horizon.
Evidence source ID and local anchor: SRC-1 `packages/openclaw-pond/src/tools.ts`; see record.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Host identity/context correctness and bypass prevention are external contracts.

Route ID: [RT-RTE-session-restore](runtime.md#rt-rte-session-restore), [RT-BAP-session-switch](runtime.md#rt-bap-session-switch)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-archive-fields](#epi-obj-archive-fields)
Content/update relation: truth-apt transformation: indeterminate; individual native/foreign codec semantic preservation is not audited here.
Transition or check target: Requested archive lineage to native client files and Pi session-loader handoff.
Evaluator/condition and domain: See restore record: supported lineage, actual adapter fidelity, collision and write conditions; no semantic truth evaluator.
Activation and timing: Explicit restore; local Pi handoff on success.
Possible or observed result: Written files and switch request, or rejection/failed write with best-effort cleanup.
Implemented force: Enforcing filesystem admission; executable host-switch request.
Epistemic authority and scope: Restored history for continuation, not verified truths or verified transfer of task success.
Operational authority: Behavior permitted, blocked, or changed: See records; no-overwrite gate and unsupported-depth refusal are distinct from epistemic acceptance.
Behavioral-authority path: See [RT-BAP-session-switch](runtime.md#rt-bap-session-switch); serialized history to replacement host session, possible later turns.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/adapter/mod.rs`, `packages/pi-pond/index.ts`; see records.
Claim IDs or none: [EPI-CLM-archive-recall](#epi-clm-archive-recall)
Mismatch marker or none: Universal continuation remains unobserved.
Gap/limit: Codec audit needed to distinguish non-ampliative faithful reconstruction from changed meaning; host parse/continuation evidence missing.

Route ID: [EPI-RTE-maintenance-check](#epi-rte-maintenance-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-maintenance-finding](#epi-obj-maintenance-finding)
Content/update relation: truth-apt transformation: entailed derivation; findings follow inspected metadata/probe rules within their domain.
Transition or check target: Model-ID agreement, index intent/manifest conditions and legacy fragment layouts.
Evaluator/condition and domain: Software metadata comparison/probes, not semantic quality comparison; see record.
Activation and timing: On-demand diagnosis and enabled embedding-stage guard.
Possible or observed result: ModelSwap/manifest/layout findings or no such finding.
Implemented force: Results feed recovery and reporting.
Epistemic authority and scope: Local storage/model-ID condition only; same ID does not prove same fetched weights.
Operational authority: Behavior permitted, blocked, or changed: See [EPI-RTE-maintenance-recovery](#epi-rte-maintenance-recovery).
Behavioral-authority path: Probe to optimize/embed-stage controller; enforcing guard/recovery trigger or advisory status output.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`; see record.
Claim IDs or none: none
Mismatch marker or none: One-row/ID comparison is not a complete artifact-freshness or corpus homogeneity proof.
Gap/limit: External storage semantics and assumed single-active-model consistency unverified.

Route ID: [EPI-RTE-maintenance-recovery](#epi-rte-maintenance-recovery)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder), [EPI-OBJ-maintenance-finding](#epi-obj-maintenance-finding)
Content/update relation: non-truth-apt policy/content update: rebuild numerical retrieval representations and storage/index layout
Transition or check target: Diagnosed conditions to refusal or selected repair.
Evaluator/condition and domain: Fixed dispatch over findings and explicit force/full flags; see record.
Activation and timing: Ordinary embed stage refuses unforced model mismatch; optimize --full consumes findings.
Possible or observed result: Refusal; drop stale vector index and re-embed; orphan-index removal, fragment rewrite or index rebuild.
Implemented force: Enforcing maintenance effects and nonzero failure reporting.
Epistemic authority and scope: Restored retrieval machinery, not endorsement of historical claims or demonstrated improved relevance.
Operational authority: Behavior permitted, blocked, or changed: Changes future retrieval representations/indexes; does not revise loaded embedding parameters by training.
Behavioral-authority path: Maintenance controller to store vectors/indexes, then later search; enforcing update, ranking effect at subsequent reads.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/main.rs`; see record.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Repair success, replay safety and retrieval improvement not observed.

Route ID: [EPI-RTE-deletion-detection](#epi-rte-deletion-detection)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-reconciliation-report](#epi-obj-reconciliation-report)
Content/update relation: truth-apt transformation: entailed derivation; operational classification under archive/DB rules, not proof of human intent.
Transition or check target: Deleted-reason archive versus live-entry presence within an OpenClaw root.
Evaluator/condition and domain: Software detector; ambiguity and multi-root uncertainty favor preservation; see record.
Activation and timing: Configured reconciliation in sync.
Possible or observed result: Erase targets or preserve notes reported; no observed run.
Implemented force: Advisory summary, not implemented content withdrawal in this traced path.
Epistemic authority and scope: Only detector classification; no inferred universal user-intent or warrant revocation.
Operational authority: Behavior permitted, blocked, or changed: Sync reports; already archived bytes remain eligible for reads.
Behavioral-authority path: Detector to sync summary/log/JSON, advisory to operator at sync horizon; no implemented purge consumer here.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs`; see record.
Claim IDs or none: none
Mismatch marker or none: Returning an erase set does not erase.
Gap/limit: Not a global erasure audit; DB helper internals uninspected.

Route ID: [EPI-RTE-copy-verification](#epi-rte-copy-verification)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-storage-verify](#epi-obj-storage-verify)
Content/update relation: truth-apt transformation: entailed derivation; key-membership/duplicate/index facts under the scanned store state.
Transition or check target: Source composite-key coverage in destination, destination duplicates and index coverage.
Evaluator/condition and domain: Deterministic scans and metadata checks; see record.
Activation and timing: Closing store-copy check or --verify-only.
Possible or observed result: SYNCED/FAILED summary; failed verify-only result drives exit 6.
Implemented force: Advisory verification detail and enforcing command failure, not payload rejection/rollback.
Epistemic authority and scope: Coverage of keys and indexes, not field-value equality or truth of archived claims.
Operational authority: Behavior permitted, blocked, or changed: Caller sees success/failure and retry guidance; no automatic deletion of partially copied rows.
Behavioral-authority path: Store scan to CLI renderer/exit, advisory and enforcing at command completion.
Evidence source ID and local anchor: SRC-1 `packages/pond/src/main.rs`; see record.
Claim IDs or none: none
Mismatch marker or none: Equal/matching keys cannot certify equal content.
Gap/limit: Individual payload equality, copy internals and deployment concurrency not assessed.

Route ID: [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-benchmark-ranks](#epi-obj-benchmark-ranks)
Content/update relation: truth-apt transformation: entailed derivation; metrics follow nominated reference labels and result files, conditional on their validity.
Transition or check target: Reachability/rank of a nominated session/message ID-prefix or text anchor in query results.
Evaluator/condition and domain: Python matching and metric arithmetic; human-curated reference labels, not an answer oracle for claim truth.
Activation and timing: Explicit developer benchmark verify/score invocation.
Possible or observed result: Verify pass/fail exit; ranks CSV and printed success/precision/reciprocal-rank metrics.
Implemented force: Benchmark command status and persisted comparison output; no inspected automatic product-admission consumer.
Epistemic authority and scope: Reference-relative retrieval rank only, not correctness of an answer or its explanation.
Operational authority: Behavior permitted, blocked, or changed: Developer can use output; no proven deployed policy update.
Behavioral-authority path: Query/results to benchmark checker to developer via exit/CSV/stdout; advisory comparison, enforcing benchmark failure only; experiment horizon.
Evidence source ID and local anchor: SRC-1 `ops/search-benchmarks/bench.py`; see record.
Claim IDs or none: [EPI-CLM-ranked-context](#epi-clm-ranked-context)
Mismatch marker or none: No current-pin observed metric or causal answer-quality support.
Gap/limit: Corpus labels and full experimental design uninspected; scoring does not establish content-directed theory criticism.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-archive-recall](#epi-clm-archive-recall) | Automatic lossless archive, whole-corpus recall and cross-client restoration/continuation | SRC-1 `README.md`, doctrine/design | Explicit archive-versus-memory distinction; see claim | [EPI-RTE-field-extraction](#epi-rte-field-extraction), [EPI-RTE-search-projection](#epi-rte-search-projection), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall), [RT-RTE-session-restore](runtime.md#rt-rte-session-restore) | None supplied connecting these routes to host continuation | No causal experiment; external source/host behavior and codec coverage limit attribution | Archival acquisition, requested recall and restoration handoff are wired | 10 MiB leaf cap qualifies losslessness; search is a projection, not every stored part; any-client continuation not demonstrated |
| [EPI-CLM-ranked-context](#epi-clm-ranked-context) | Small “complete ranked answer” versus expensive grep read | SRC-1 `README.md`, doctrine/design; `docs/benchmarks/recall-context-cost.md`, reported operation | Report explicitly limits its response to a starting point and acknowledges follow-up cost | [EPI-RTE-recall-rendering](#epi-rte-recall-rendering), [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall); separate rank evaluator [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | Cost report has attributed table, not a host answer trace or inspected current-pin raw runs | Five author-chosen queries; unequal corpus coverage; bytes/4; median matching-file comparison; no answer-correctness outcome | Bounded first-read context cost is reported and bounded rendering implemented | Complete/final answer, general quality improvement and component causal benefit unsupported |
| [RT-CLM-ingest-recovery](runtime.md#rt-clm-ingest-recovery) | Durable partial writes converge on retry | SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/transport.rs`, implementation/design; see record | See record | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | Uninspected | Atomic table commits/external storage and available future source required; no whole-session atomicity | Recovery plumbing can preserve/add missing archive rows | This is not semantic revision, claim acceptance or warrant repair |
| [RT-CLM-transport-gates](runtime.md#rt-clm-transport-gates) | Route-specific Host protection | SRC-1 `packages/pond/src/transport.rs`, implementation/design; see record | See record | [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql) and HTTP router | Uninspected | Network/deployment/SDK contract; no universal ACL | Selected entry points have a protocol gate | Does not authenticate source content or establish authorized reliance on its propositions |

## Bounded conclusion

Pond acquires and retains mixed human/model/tool session history, with source warrant unknown. The archive is operationally admitted through structural rules, not accepted as truthful knowledge. The extraction cap supplies a concrete counterexample to unqualified value completeness. Index construction and rendering reshape a subset without creating an explanation; search does not cover all archived tool bodies or reasoning. See [EPI-RTE-field-extraction](#epi-rte-field-extraction), [EPI-RTE-ingest-disposition](#epi-rte-ingest-disposition), [EPI-RTE-search-projection](#epi-rte-search-projection), [EPI-RTE-recall-rendering](#epi-rte-recall-rendering).

The implemented consequential consumers are requested host recall, corpus SQL, and a separate restored-session switch request. Ranking, chronology, explicit IDs and plugin scope policy select what can reach those consumers. They do not decide that the selected historical claim is true. Advisory instructions warn that early conclusions may be overturned and that weak search does not prove absence; no trace establishes compliance. Restoration has stronger operational force than a tool-result quotation, but still supplies history rather than epistemic acceptance. See [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall), [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql), [RT-RTE-openclaw-tools](runtime.md#rt-rte-openclaw-tools), [RT-BAP-recall-guidance](runtime.md#rt-bap-recall-guidance), [RT-BAP-session-switch](runtime.md#rt-bap-session-switch).

The narrow deductions supported by inspected evaluators concern schema errors, metadata mismatch, deletion classifications, key coverage and reference-relative retrieval rank. Their premises are the supplied fields/scanned state/reference labels, not independently warranted claims about the user's task. Each check's criterion and intended operational use are in its route. Maintenance checks have executable repair/guard consumers. Copy verification can fail a command without certifying payload equality. Deletion detection reports a classification without withdrawing retained bytes. The benchmark has local command and developer-output force, not an inspected automatic acceptance or deployed update path. See [EPI-RTE-ingest-check](#epi-rte-ingest-check), [EPI-RTE-maintenance-check](#epi-rte-maintenance-check), [EPI-RTE-maintenance-recovery](#epi-rte-maintenance-recovery), [EPI-RTE-copy-verification](#epi-rte-copy-verification), [EPI-RTE-deletion-detection](#epi-rte-deletion-detection), [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark).

Within the inspected capture/recall/maintenance chain, no route found within boundary establishes evidence-consuming acceptance of a new ampliative historical claim against a named truth criterion, or lifecycle integration after such acceptance. This is not a complete repository-wide absence claim: individual codecs, development review, test results and research material remain incompletely inspected. Imported statements may themselves be explanations or conjectures; Pond did not produce them merely by archiving them. There is no individuated candidate and derivation evidence here that warrants attributing ampliative conjecture generation to Pond. Codec semantic fidelity remains local uncertainty, not evidence that restoration invents claims.

Loaded embedding weights have inspected inference but no parameter-training update in that path, and the model ID is not an immutable artifact pin. Numerical representations are rebuilt for retrieval after diagnosed ID changes; this direct machinery adaptation does not establish improved capacity, semantic acceptance, autonomous criticism or exercised self-improvement. Raw history may contain criticism and iterative work by external agents, but delivery alone does not establish Pond's consumption of a formulated theory, content-directed criticism or iteration. Archive persistence is supported independently of those unestablished properties. The cost report's first-read savings do not close downstream activation or benefit attribution. See [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder), [EPI-RTE-maintenance-recovery](#epi-rte-maintenance-recovery), [RT-RTE-adapter-development](runtime.md#rt-rte-adapter-development), [EPI-CLM-ranked-context](#epi-clm-ranked-context).

## Shared records

### Operative objects

#### EPI-OBJ-archive-fields
Label: Archived source fields
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Material payload of the capture route, not another capture mechanism. The route parent contains the admitted canonical session/message/part fields. Their natural-language bodies receive meaning through later host interpretation; symbolic role/time/ID/provenance fields receive fixed storage and selector consequences. Storage substrate is buffered Rust events then Lance tables. Split from the supplied route's operational admission, not a duplicate of [RT-OBJ-adapter-config](runtime.md#rt-obj-adapter-config), which governs which sources are captured. SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/adapter/extract.rs`; load-bearing persistence/provenance passage see [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), bounding passage see [EPI-RTE-field-extraction](#epi-rte-field-extraction). Particular imported claims and upstream truth remain uninspected.

#### EPI-OBJ-search-text
Label: search_text
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Material derived field produced during buffering, distinct from the full canonical part payload. Natural-language text is concatenated under symbolic role/provenance rules; substrate is a stored message text column plus retrieval indexes. It belongs to the capture route even though recall later consumes it. SRC-1 `packages/pond/src/sessions.rs`; passage and concrete deduction see [EPI-RTE-search-projection](#epi-rte-search-projection). Numerical vectors are a separate representation, not this field.

#### EPI-OBJ-operational-findings
Label: Operational check results

Aggregate inventory of symbolic result variants with separate operative parts: ingestion RowOutcome/RowError, MaintenanceFinding, OpenClaw ReconciliationReport and StorageVerify. Substrate is Rust memory and returned/logged/printed JSON/text, not a unified accepted-knowledge store. Distinct from the static [RT-OBJ-prompt-guidelines](runtime.md#rt-obj-prompt-guidelines) and adapter configuration: these are computed judgments about an operation's state. No counterpart result object is declared in the supplied runtime. SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`, `packages/pond/src/adapter/openclaw.rs`. The separately declared check and consumer routes below own their domains, forces and evidence; aggregation confers no common epistemic authority.

#### EPI-OBJ-row-outcome
Label: RowOutcome
Part of: [EPI-OBJ-operational-findings](#epi-obj-operational-findings)

Symbolic per-event status/error fields in Rust memory and wire/summary output. Their consumer is the current ingest admission/response path, not a semantic-knowledge evaluator. This separates the ingestion-result part of the local result container; the supplied [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) describes its enclosing mechanism. SRC-1 `packages/pond/src/sessions.rs`; load-bearing predicates and disposition passage see [EPI-RTE-ingest-check](#epi-rte-ingest-check) and [EPI-RTE-ingest-disposition](#epi-rte-ingest-disposition).

#### EPI-OBJ-maintenance-finding
Label: MaintenanceFinding
Part of: [EPI-OBJ-operational-findings](#epi-obj-operational-findings)

Symbolic enum values and associated metadata in Rust memory, rendered status output and maintenance dispatch. Distinct from RowOutcome by target and consumer: storage/retrieval diagnosis drives repair. No corresponding supplied result object; closest supplied context is [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder), which is a model component, not a diagnosis. SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`; passages see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check) and [EPI-RTE-maintenance-recovery](#epi-rte-maintenance-recovery).

#### EPI-OBJ-reconciliation-report
Label: ReconciliationReport
Part of: [EPI-OBJ-operational-findings](#epi-obj-operational-findings)

Symbolic erase-target/preserve arrays with reasons in Rust memory, sync JSON/text/log output. Distinct from repair-trigger findings: this consumer reports rather than purges. Closest supplied context is [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)'s deletion-detection account; no supplied result object. SRC-1 `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs`; passage see [EPI-RTE-deletion-detection](#epi-rte-deletion-detection).

#### EPI-OBJ-storage-verify
Label: StorageVerify
Part of: [EPI-OBJ-operational-findings](#epi-obj-operational-findings)

Symbolic table-coverage/duplicate/index fields in Rust memory and CLI verdict output. Its consumer changes copy/verify completion reporting and status, not archived payload truth. No corresponding supplied result object; distinct from [RT-RTE-session-restore](runtime.md#rt-rte-session-restore)'s host-native file outcome. SRC-1 `packages/pond/src/main.rs`; passage see [EPI-RTE-copy-verification](#epi-rte-copy-verification).

#### EPI-OBJ-benchmark-ranks
Label: Retrieval ranks

Symbolic per-query rank/stratum/language/mode/note rows persisted as CSV; derived metrics printed as Markdown. Natural-language text anchors and symbolic ID-prefix references come from caller-supplied TSV labels. This is developer-evaluation output, distinct from [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall)'s host recall result; no counterpart benchmark-output object is supplied. SRC-1 `ops/search-benchmarks/bench.py`; passage see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark).

### Routes

#### EPI-RTE-field-extraction
Label: Source field extraction
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Source rows enter module-private Extracted wrappers through extraction helpers. The inspected shared seam bounds raw JSON string leaves as well as extracted strings. This is the capture route's extraction part, not its structural admission part. Source author/provider supplies values; extraction does not certify their propositions. SRC-1 `packages/pond/src/adapter/extract.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Extracted source values or bounded JSON copies with marked oversized leaves.
- Later read-back: Stored surviving prefixes can reach later archive reads/restoration; a discarded tail is not present in the bounded raw record.
- Delegated visibility: inapplicable — extraction does not dispatch workers.
- Selection predicate: Requested source field/type and per-string byte length; nested strings traversed recursively.
- Invalidation or expiry: Over-cap tail replaced at extraction; source logs may retain originals outside this projection.
- Activation or effect: Enforcing value cap; subsequent host interpretation unobserved.
- Evidence limits: Individual adapters and unbounded external originals not audited; wrapper construction has crate-internal storage and serde paths, so sealing is not independent source authentication.

A concrete implementation deduction needs no execution: a UTF-8 ASCII source string consisting of 10,485,761 `a` bytes enters `bound_str`. It exceeds LEAF_CAP = 10,485,760; `truncate_to_marker` returns a prefix plus `<pond:truncated 10485761 bytes>`, within the cap, and increments the counter. `extract_raw_record` applies this recursively even to the retained raw JSON copy. A claim in the discarded tail is no longer available from that copy. This bounds the losslessness claim without asserting that ordinary sub-cap extraction changes meaning.

> pub(crate) const LEAF_CAP: usize = 10 * 1024 * 1024;
> --- `packages/pond/src/adapter/extract.rs`

> pub(crate) fn bound_str(s: &mut String) -> bool {
>     if s.len() <= LEAF_CAP {
>         return false;
>     }
>     *s = truncate_to_marker(s.as_bytes(), s.len());
>     true
> }
> --- `packages/pond/src/adapter/extract.rs`

> pub fn extract_raw_record(row: &Value) -> Value {
>     let mut bounded = row.clone();
>     bound_value(&mut bounded);
>     bounded
> }
> --- `packages/pond/src/adapter/extract.rs`

#### EPI-RTE-ingest-check
Label: Structural ingest checks
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Canonical Session event to RowOutcome error or eligibility, owned by IngestValidator. These are a material checking part of the supplied capture container; admission/disposition is separately declared below. SRC-1 `packages/pond/src/sessions.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Error outcome for empty trimmed source_agent or parent_message_id without parent_session_id; otherwise continue processing.
- Later read-back: inapplicable — these checks produce current-batch outcomes, not a retained semantic decision.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: Session event with named schema relationships; validator software decides, producer proposes, software can veto.
- Invalidation or expiry: Current-batch check result; later ingest retries must meet rules again.
- Activation or effect: Structural outcomes feed immediate buffering/admission control.
- Evidence limits: These predicates do not inspect the truth of bodies; complete validator/order/storage semantics only partly inspected directly and otherwise supplied by runtime.

Open ingest mode; no reference task answer or model oracle. Domain is schema validity, intended use is safe canonical admission, scope is the current event/substream. Software computes the result; no per-event human check is inserted by these conditions.

> let trimmed = session.source_agent.trim();
>         if trimmed.is_empty() {
> --- `packages/pond/src/sessions.rs`

> if session.parent_message_id.is_some() && session.parent_session_id.is_none() {
> --- `packages/pond/src/sessions.rs`

#### EPI-RTE-ingest-disposition
Label: Structural ingest disposition
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Checked event to rejected substream or buffered records then store flush. Same container as [EPI-RTE-ingest-check](#epi-rte-ingest-check), distinct function: consuming the structural outcome. Validator/writer own effects, producers propose records, code can veto; no per-claim human review or expected-answer oracle. Open capture mode. Trigger is an ingest event; guidance is canonical event order/schema and core provenance ownership, not a semantic knowledge-production method. Retry/fixed source can recover; persistent rows and partial commits are see [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). SRC-1 `packages/pond/src/sessions.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rejected RowOutcome or buffered/progress outcomes; final flush returns per-row outcomes and table counts.
- Later read-back: Admitted durable rows can reach future archive consumers; rejected rows have no read-back through this admission.
- Delegated visibility: inapplicable — no task delegation.
- Selection predicate: Structural validity and later key/storage rules; software permits progression, not epistemic acceptance of text.
- Invalidation or expiry: Rejected substream cannot anchor message/part events; successful stored keys are additive and do not revise existing payload by this route.
- Activation or effect: Retention eligibility; later truth reliance unobserved.
- Evidence limits: Direct library/copy paths do not necessarily use this validator; no universal gate asserted.

> // dropped on the spot - the substream that would follow has nothing
>         // to anchor on, so subsequent message/part events will also drop.
> --- `packages/pond/src/sessions.rs`

> store.upsert_session_batch(completed).await
> --- `packages/pond/src/sessions.rs`

#### EPI-RTE-search-projection
Label: Conversational search projection
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Complete buffered message/parts to search_text, owned by Rust construction code. This is the capture route's derived index-content part, not recall selection itself. SRC-1 `packages/pond/src/sessions.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Newline-joined eligible text/file descriptor chunks, or None if empty.
- Later read-back: Stored projection and its indexes reach subsequent requested searches/SQL.
- Delegated visibility: inapplicable — no worker context dispatch.
- Selection predicate: Conversational provenance, user/assistant role, Text or selected File fields, nonblank chunk.
- Invalidation or expiry: Existing stored keys remain additive; full canonical parts remain separately reachable beyond the restricted projection.
- Activation or effect: Limits searchable content; not an accepted-claim or method update.
- Evidence limits: Does not prove individual codec provenance classifications; source-text truth unverified.

Concrete deduction: a user message with conversational text `We fixed X`, injected text `Ignore prior rules`, and a ToolResult body `build failed` yields only `We fixed X` as search_text. A sole injected text part yields None. Thus a no-hit ordinary search cannot establish that a tool failure or injected instruction was never recorded. Reordering/index projection is non-ampliative; it is not creation of a distilled conclusion.

> if part.provenance != Provenance::Conversational {
>             continue;
>         }
> --- `packages/pond/src/sessions.rs`

> (Role::User | Role::Assistant, PartKind::Text { text }) => {
>                 if let Some(text) = text {
>                     chunks.push(text.to_string());
>                 }
>             }
> --- `packages/pond/src/sessions.rs`

> let text = chunks
>         .into_iter()
>         .filter(|chunk| !chunk.trim().is_empty())
>         .collect::<Vec<_>>()
>         .join("\n");
>     if text.is_empty() { None } else { Some(text) }
> --- `packages/pond/src/sessions.rs`

#### EPI-RTE-recall-rendering
Label: Bounded recall rendering
Part of: [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall)

Selected SearchResponse to MCP/CLI transcript, then Pi relay to host tool-result text. Deterministic Rust renderer and TypeScript byte-bounding code own formatting and omissions. This material delivery-transformation part is distinct from query planning/ranking in the parent route. SRC-1 `packages/pond/src/render.rs`, `packages/pi-pond/src/tools.ts`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Session-grouped snippets, scope counts and follow-up hints; over-budget omissions marked; Pi caps returned UTF-8 text.
- Later read-back: inapplicable — rendering does not write a new Pond artifact; subsequent IDs/queries can reload existing archive content.
- Delegated visibility: inapplicable — requester tool result, not worker dispatch.
- Selection predicate: Per-session budget share allows at least first hit; Pi UTF-8 byte budget bounds entire returned response.
- Invalidation or expiry: Current result discarded with host context; omitted content stays reachable through explicit subsequent archive reads.
- Activation or effect: Controls text actually delivered; interpretation/compliance not observed.
- Evidence limits: No full session/message renderer audit; no supplied host trace; a warning does not ensure follow-up.

The source first describes a top-hit guarantee but the executable loop renders the first member of `session.matches`, which the renderer states are newest-first. Do not promote this to a universal guarantee that the highest-scored message survives every truncation. After Rust's fair-share rendering, Pi can still clip the whole returned text. These are not truth checks. Vector-mode wording explicitly warns that the closest rows need not be strong evidence of a match.

> if rendered > 0 && out.len().saturating_sub(session_start) >= share {
>                 break;
>             }
> --- `packages/pond/src/render.rs`

> " Vector mode returns the closest rows by meaning even when none are strong; for exact-word matching set mode=\"fts\"."
> --- `packages/pond/src/render.rs`

> return response.ok ? okResult(boundedText(response.text)) : errorResult(response.error);
> --- `packages/pi-pond/src/tools.ts`

#### EPI-RTE-maintenance-check
Label: Maintenance diagnosis

Store metadata/probe state to MaintenanceFinding or embedding mismatch guard, owned by Store/Rust controller. The supplied runtime mentions maintenance but declares no equivalent diagnosis record; distinct from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)'s admission and [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder)'s inference. SRC-1 `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ModelSwap, manifest/layout findings, or no finding/error.
- Later read-back: inapplicable — current probe output; repaired persistent state is the linked recovery route's result.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: Enabled embeddings; LIMIT-1 model ID versus configured ID; metadata/legacy-layout checks. Software judges, operator requests diagnosis/maintenance and can choose force/full repair.
- Invalidation or expiry: Recomputed from sampled/manifest state; one row relies on single-active-model assumption.
- Activation or effect: Findings drive refusal, reporting and selected repair.
- Evidence limits: Model ID is not artifact hash; equal ID need not imply equal resolved weights; storage/model consistency assumptions unverified.

Target/domain is storage/retrieval machinery health, not relevance accuracy. Reference is configured model/index/layout intent, not an expected answer. Open maintenance mode, triggered by diagnosis/embed work.

> pub async fn embedding_model_swapped(&self) -> Result<bool> {
>         Ok(self
>             .sample_embedded_model()
>             .await?
>             .is_some_and(|model| model != crate::embed::model_id()))
>     }
> --- `packages/pond/src/sessions.rs`

> let (model_swap, manifest, sessions, messages) = tokio::try_join!(
>             model_swap,
>             self.manifest_findings(),
>             self.handle.legacy_layout(Table::Sessions),
>             self.handle.legacy_layout(Table::Messages),
>         )?;
> --- `packages/pond/src/sessions.rs`

#### EPI-RTE-maintenance-recovery
Label: Findings-directed maintenance

Diagnosis/flags to repair calls and future retrieval state, owned by CLI maintenance controller. Distinct consequential consumer of [EPI-RTE-maintenance-check](#epi-rte-maintenance-check), not a duplicate embedder component. Operator initiates open maintenance, software maps findings to repairs and can refuse unforced stale-model work. Reference/guidance is configured model/index/layout intent. Proposed update changes vectors/indexes/layout, not claim text or a theory. Rollback/atomic recovery is not established; errors and subsequent rerun/rebuild are operational recovery paths. SRC-1 `packages/pond/src/main.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Guard refusal or repair progress/outcome; failed index phase can exit nonzero.
- Later read-back: Changed vectors/index/layout feed subsequent search and storage reads.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: OrphanIndex, LegacyLayout, ModelSwap and DeltaPileup variants plus force/full flags and enabled embedding state.
- Invalidation or expiry: Stale vector index can be dropped before re-embedding; orphan indexes removed; old fragment layout rewritten.
- Activation or effect: Enforcing mutation of retrieval/storage machinery; downstream ranking benefit unobserved.
- Evidence limits: No exercised repair or outcome-quality comparison, crash-safety proof or training change; external storage internals uninspected.

> if !force {
>             bail!(
>                 "messages embedded under a different model id; pass `{force_hint}` \
>                  to re-embed (the vector index will be rebuilt under the configured \
>                  model {:?})",
>                 pond::embed::model_id(),
>             );
>         }
> --- `packages/pond/src/main.rs`

> store.drop_vector_index().await?;
> --- `packages/pond/src/main.rs`

> let model_swapped = findings
>         .iter()
>         .any(|finding| matches!(finding, MaintenanceFinding::ModelSwap { .. }));
>     let started = std::time::Instant::now();
>     run_embed_stage(store, model_swapped).await?;
> --- `packages/pond/src/main.rs`

#### EPI-RTE-deletion-detection
Label: OpenClaw deletion detection
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Sync's reconciliation part maps deleted archives/live DB entries to ReconciliationReport then summary/log output. This refines the parent record's already stated detection-not-purge finding; not another retention route. OpenClawAdapter proposes classification; software decides, ambiguity vetoes erasure classification; no per-item human approval. Target is archive/live-entry relation, reference is source archive reason and DB liveness, operating mode is open periodic/explicit sync. SRC-1 `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs`, implementation/design.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Erase target/preserve classification array and sync human/log/JSON summary.
- Later read-back: inapplicable — detection does not persist a purge/denylist or semantic withdrawal through the inspected consumer.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: Configured reconciliation, deleted archive, known stored session and source live-entry state; multi-root ambiguity downgrades erase to preserve.
- Invalidation or expiry: Detection result applies to current source observations; archive bytes not expired by this route.
- Activation or effect: Advisory operator reporting, no executable purge consumer in traced sync.
- Evidence limits: DB helper decisions not exhaustively audited; no universal erasure absence claimed outside this route.

> This is a pure detection pass: it
>     /// names every action for the sync summary and returns the erase set; the
>     /// actual byte-purge + denylist is the caller's `pond erase` step
> --- `packages/pond/src/adapter/openclaw.rs`

> "openclaw: {} explicitly deleted session(s) detected (erase pending; pond erase is not yet implemented): {}",
> --- `packages/pond/src/main.rs`

The first passage declares a future caller responsibility, not an available command. Dispatch search plus the actual summary prevents reading it as implemented withdrawal. This is qualification of doctrine beside its real consumer, not a change to the supplied runtime record.

#### EPI-RTE-copy-verification
Label: Store copy verification

Source/destination stores to key/duplicate/index checks and CLI completion verdict. Rust verify_stores owns checking; CLI renderer/verify-only branch consume results. Runtime mentions store copy but supplies no equivalent checker record; distinct from [RT-RTE-session-restore](runtime.md#rt-rte-session-restore), which creates host-native files. SRC-1 `packages/pond/src/main.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: StorageVerify and rendered SYNCED/FAILED detail; verify-only failure exits 6.
- Later read-back: inapplicable — checker reads retained stores but does not itself accumulate new content; copied rows are a separate transfer effect.
- Delegated visibility: inapplicable — no worker dispatch.
- Selection predicate: Source composite keys versus destination key set; destination duplicate count; index-presence/activation metadata.
- Invalidation or expiry: Results describe scanned state, not a permanent certificate; subsequent store changes may invalidate the comparison.
- Activation or effect: Completion/failure report and command status; failed verification does not automatically retract copied content.
- Evidence limits: Keys rather than payload values are compared; external concurrent-storage semantics not independently verified.

Caller selects stores; software refuses identical/empty mistaken sources and computes verification; no expected-answer oracle. Open copy/verify mode. Criterion is operational archive coverage, intended use is detecting incomplete transfer, scope is the scanned tables/index intent. It is not semantic acceptance of the archived claims. Source/destination membership checks do not prove byte equality.

> let (dest_keys, dest_rows) = to.composite_pk_index(table).await?;
>         let dest_duplicates = dest_rows - dest_keys.len();
>         let (source_rows, missing) = from.composite_pk_diff_against(table, &dest_keys).await?;
> --- `packages/pond/src/main.rs`

> if !render_storage_verify(&verify, &from_resolved.display(), &to_resolved.display())?.synced
>         {
>             std::process::exit(6);
>         }
> --- `packages/pond/src/main.rs`

#### EPI-RTE-retrieval-benchmark
Label: Reference-relative retrieval evaluation

TSV query/reference labels plus live/captured retrieval output to anchor reachability or rank CSV/metrics. Python evaluator owns matching; caller supplies references and experiment choices. No equivalent evaluator record is supplied: [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall) is the subject, not the evaluator. SRC-1 `ops/search-benchmarks/bench.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verify success/failure exit and missing-reference detail; score writes ranks CSV and prints stratum metrics.
- Later read-back: CSV/results are available to subsequent developer analysis; actual later consumer/admission uninspected.
- Delegated visibility: inapplicable — benchmark invokes retrieval, not agent workers.
- Selection predicate: Caller query set, mode/limit/results directory; first matching session/message eight-character ID-prefix or normalized text-anchor occurrence.
- Invalidation or expiry: Labels/results are specific to corpus, query set and retrieval configuration; file lifetime not specified by scorer.
- Activation or effect: Benchmark exit/outputs wired; no inspected automatic product change from scores.
- Evidence limits: Source code not executed; full label validity, artifacts and fusion experiment design uninspected; textual anchor is not an oracle for answer correctness.

Reference outcome is the caller-nominated ID-prefix/anchor. Criterion for verify is reachability in either FTS or vector top-limit; rank scorer measures first occurrence. Human/caller reference selection and computational matching are distinct. Mode is a bounded retrieval benchmark, not open user answering. A failed verify reports and exits 1; no automatic revised method, merge gate or deployed ranking-policy consumer is established by these routines.

> sid = (hit.get("session_id") or "")[:8]
>             mid = (hit.get("message_id") or "")[:8]
>             if sid in tokens or mid in tokens:
>                 return idx
> --- `ops/search-benchmarks/bench.py`

> text = nfc((hit.get("text") or "").lower())
>             if any(tok in text for tok in tokens):
>                 return idx
> --- `ops/search-benchmarks/bench.py`

> with out_csv.open("w", newline="") as f:
>         w = csv.DictWriter(f, fieldnames=["id", "stratum", "lang", "mode", "rank", "note"])
>         w.writeheader()
>         for r in rows:
>             w.writerow({**r, "mode": args.label})
> --- `ops/search-benchmarks/bench.py`

### Claims

#### EPI-CLM-archive-recall
Label: Archive preservation and recall

README claims automatic lossless capture, corpus search/SQL and restoration into supported clients. It explicitly declines the distilled-fact memory role. Closest supplied counterpart is [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), which describes implementation rather than this public capability claim; no supplied CLM record owns the README claim. SRC-1 `README.md`, doctrine/design. Preservation does not itself warrant the truth of preserved claims.

> Pond ingests them all automatically and losslessly into storage you own (a local dir or your own S3 bucket), makes the whole corpus searchable and SQL-queryable, and hands that recall back to your agents over MCP
> --- `README.md`

> Pond keeps the sessions: every message, tool call, and result, value-complete, cross-client, in storage you own, never pruned - searchable over MCP and restorable into any client.
> --- `README.md`

#### EPI-CLM-ranked-context
Label: Ranked recall context

README image alt text presents a complete ranked answer in 1.5–3k tokens against much larger grep workflow context. The associated context-cost report bounds its method and qualifies completeness. Distinct from [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall)'s wiring and [RT-CLM-ingest-recovery](runtime.md#rt-clm-ingest-recovery)'s durability claim. SRC-1 `README.md`, doctrine/design; `docs/benchmarks/recall-context-cost.md`, reported operation. The script/raw execution was not inspected here, so this record retains attributed measurements, not an observed current-pin benchmark.

> pond_search returns a complete ranked answer in 1.5-3k tokens; grep plus reading one matching transcript costs 90-255k tokens
> --- `README.md`

> Tokens estimated as bytes/4.
> --- `docs/benchmarks/recall-context-cost.md`

> One corpus, one machine, five queries, chosen by the author. This measures
>   the shape of the problem, not a universal constant.
> --- `docs/benchmarks/recall-context-cost.md`

> The pond response is a starting point, not always the full answer: the agent
>   may follow up with `pond_get_session` on a hit, which adds tokens.
> --- `docs/benchmarks/recall-context-cost.md`
