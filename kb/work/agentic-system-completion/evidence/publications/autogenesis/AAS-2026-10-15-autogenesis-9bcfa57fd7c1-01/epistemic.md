---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Autogenesis epistemic routes: imported evidence, model reports, bounded checks and the authority of retained evaluations and capabilities."
run-id: AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis epistemic report

## Source-and-claim boundary

The question is which routes acquire or produce truth-apt content, evaluate it, license reliance and change later behavior. Scope and exclusions are those of [boundary.md](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). All new reads below are SRC-1 at the frozen commit. Executable code supplies implementation evidence; prompts, docstrings describing intended guarantees and README claims supply doctrine/design. No target execution, observed-run source or causal comparison was supplied or performed.

The material boundary includes user tasks and action results, child returns, web acquisition/synthesis, tiered execution-history memory, corpora and ranking, evaluator reports, benchmark scoring, workflow verification/evaluation records, extension admission and withdrawal, and administrative changes. Remote provider internals, other repositories and live services remain excluded. Their exclusion prevents identifying provider reasoning, source reliability and deployed behavior. Available but uninspected leaves are not absent routes. In particular, this is not a system-complete negative about knowledge production.

Claims assessed are [RT-CLM-self-evolution](runtime.md#rt-clm-self-evolution), [RT-CLM-user-approval](runtime.md#rt-clm-user-approval), [EPI-CLM-continuous-improvement](#epi-clm-continuous-improvement) and [EPI-CLM-smoke-safety](#epi-clm-smoke-safety). Their declared meanings are not copied here.

| Entry point or operation | Source path in SRC-1 | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| Console command, TUI, serve | `autogenesis/cli.py` | Direct read of entry/dispatch classes; supplied Gateway account: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) | No alternate console answer oracle found in this read; complete control-command internals not independently traced. |
| Model decisions, children, skills, native roster, playground | `autogenesis/agent/native_tools.py`, `autogenesis/agent/types.py`, `autogenesis/protocol/server.py`, `autogenesis/gateway/service.py` | Direct roster read; other mechanisms supplied: [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation), [RT-RTE-skill-instructions](runtime.md#rt-rte-skill-instructions), [RT-RTE-model-playground](runtime.md#rt-rte-model-playground) | No provider weights, exact deployed model or decisions; content classification of unseen completions remains indeterminate. |
| Web fetch, search, summary and merge | `autogenesis/tool/default/web_fetcher.py`, `autogenesis/tool/default/web_searcher.py` | Direct fetch handler and search output/summary/merge methods: [EPI-RTE-web-reports](#epi-rte-web-reports) | Search-engine adapters and URL extraction internals uninspected; cannot establish faithful original-page extraction or exhaustive retrieval. |
| History ingestion, compaction, context delivery | `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py` | Direct emit/get, todo summary, compaction, persistence, session creation/eviction and compact hook: [EPI-RTE-history-summary](#epi-rte-history-summary) | Full trace producer, renderer and all alternative memory implementations uninspected; cannot establish complete capture or universal restart recall. |
| Corpus ingestion and retrieval | `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py` | Both files read: [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [EPI-RTE-corpus-ranking](#epi-rte-corpus-ranking) | External ranker-library implementations uninspected; ranking relevance is not truth verification. |
| Tool and agent evaluators | `autogenesis/agent/evaluator/tool_evaluate_agent.py`, `autogenesis/agent/evaluator/agent_evaluate_agent.py`, `autogenesis/prompt/default/tool_evaluate_agent.html` | Direct classes and tool rubric: [EPI-RTE-evaluator-reports](#epi-rte-evaluator-reports) | Other evaluator prompts/classes except workflow evaluator remain uninspected; no universal evaluator-quality conclusion. |
| Workflow verification, benchmark, result delivery | `autogenesis/workflow/runtime.py`, `autogenesis/benchmark/server.py`, `autogenesis/benchmark/default/exact_match.py` | Direct VERIFY, benchmark dispatch and normalization, batch scoring, exact match: [EPI-RTE-workflow-checks](#epi-rte-workflow-checks) | Dataset-bound benchmarks, canvas compiler and downstream user programs uninspected; no general answer correctness or causal component attribution. |
| Process record transformations | `autogenesis/process/default/records.py` | Entire file read: [EPI-RTE-record-transforms](#epi-rte-record-transforms) | Text/table processors, dataset adapters and scientific computations uninspected; prevents a complete derivation inventory. |
| Workflow evaluation write, summary, inspection and reload | `autogenesis/tool/default/evolution.py`, `autogenesis/agent/evaluator/workflow_evaluate_agent.py`, `autogenesis/workflow/context.py`, `autogenesis/tool/default/inspect_workflow.py` | Direct tool/class, context initialization and evaluation methods, inspect consumer: [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | File save/load bodies located but not fully read; atomicity not assessed. No actual evaluation artifact or subsequent decision supplied. |
| Capability registration, smoke, rollback, unload | `autogenesis/extension/smoke_gate.py`, `autogenesis/tool/default/evolution.py`, `autogenesis/extension/server.py`, `autogenesis/hook/default/tool_registration.py` | Direct smoke and evolution tool; supplied registration/promotion: [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | General capability effects and rollback internals supplied, not re-audited. No evidence that rollback reverses arbitrary effects. |
| Runtime configuration and shell | `autogenesis/gateway/service.py`, `autogenesis/tool/default/bash.py` | Supplied [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration), [RT-RTE-shell-execution](runtime.md#rt-rte-shell-execution) | Administrative content can change decisions outside evolution checks; command success is not a content oracle. |
| Browser/reviewer, connectors, environments, science/kernel, canvas, other data/process/benchmark leaves | `autogenesis/`, `extension/`, `examples/`, `frontend/` | Included functional families; only supplied endpoint coverage in [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) and boundary | Detailed evaluators, action effects and report consumers unassessed. Prevents system-wide absence of acceptance, derivation or theory building. |

Missing execution evidence prevents saying any candidate was actually checked, accepted, integrated or beneficial. Missing concrete model input/output pairs prevent distinguishing semantic compression, entailment and ampliative conjecture for particular reports. Missing independent source/reference warrant prevents upgrading imported text or numeric comparisons into established external facts. These limits do not erase implemented checking and behavioral-authority paths.

## Epistemic-object inventory

Fields owned by existing records are reached through `see`, not redeclared.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-meta-agent](runtime.md#rt-obj-meta-agent), [RT-OBJ-self-evolving](runtime.md#rt-obj-self-evolving) | Diagnostic/method claims about when capability evolution is appropriate | see records | see records | Instructional imperatives are not themselves truth-apt; method applicability claims may be. Delivery is not compliance. |
| [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager) | Not individually recoverable from weights | see record | see record | Provider-parametric state inaccessible; local calls do not establish parameter training. |
| [EPI-OBJ-web-report](#epi-obj-web-report) | Page assertions, query summaries and cited synthesis | see record | see record | Original-source warrant unknown; citations do not check entailment. |
| [EPI-OBJ-tiered-history](#epi-obj-tiered-history) | Claims that actions ran, failed, returned paths/results; summaries of those claims | see record | see record | Success labels are operational. Summary fidelity unverified. |
| [EPI-OBJ-corpus-records](#epi-obj-corpus-records) | Caller-supplied text and metadata | see record | see record | Content lineage depends on caller; score may overwrite caller field. |
| [EPI-OBJ-evaluation-report](#epi-obj-evaluation-report) | Tool/agent quality and failure assertions, scores, suggestions | see record | see record | Rubric requests evidence but does not establish it was gathered. |
| [EPI-OBJ-workflow-evaluation](#epi-obj-workflow-evaluation) | Version-scoped run success, quality and aggregate health assertions | see record | see record | Run identity checks support lineage, not task correctness or independent quality judgment. |
| [EPI-OBJ-record-values](#epi-obj-record-values) | Source records, derived returns and reference-relative correctness scores | see record | see record | Formal/numeric relation has conditional warrant; input fact truth remains unestablished. |
| [RT-OBJ-extension-source](runtime.md#rt-obj-extension-source) | Executable policy: none necessarily; embedded descriptions may assert capability behavior | see record | see record | Code behavior change and accepted explanatory knowledge are different outcomes. |
| [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest), [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint) | Active/version/run-status assertions | see records | see records | Recovery identity licenses execution/reuse, not correctness of output. |

## Authority-route ledger

A repeated route citation identifies a different function of the same source-native route. Shared-record fields, evidence and activation conditions are owned by that record (`see`). All implemented rows describe inspected capacity, not observed operation. No row licenses an unqualified truth verdict.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) | content transformation | implemented | [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager) | truth-apt transformation: indeterminate | Task/context to model answer or action | see record | see record | Candidate answer or instructions | see record | No generic answer oracle | see record | see record and [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) | see record | none | lifecycle-success-not-truth | No concrete completion to classify; remote inference opaque. |
| [EPI-RTE-web-reports](#epi-rte-web-reports) | content transformation | implemented | [EPI-OBJ-web-report](#epi-obj-web-report) | truth-apt transformation: acquisition/import | Page/search material enters fetched results | Fetch success, not source verification | see record | Text with source URLs | Advisory delivery | Source warrant unknown | Calling model can use returned message | see record | see record | none | none | Transport/extraction fidelity unassessed. |
| [EPI-RTE-web-reports](#epi-rte-web-reports) | content transformation | implemented | [EPI-OBJ-web-report](#epi-obj-web-report) | truth-apt transformation: indeterminate | Truncated page to summary to merged research report | Model; no semantic-preservation checker | see record | Cited report or mechanical fallback | Advisory | Candidate synthesis, no established acceptance | Later foreground model receives report, not full original pages | see record | see record | none | citations-not-warrant | Could reshape, derive or conjecture; concrete pairs needed. |
| [EPI-RTE-history-summary](#epi-rte-history-summary) | content transformation | implemented | [EPI-OBJ-tiered-history](#epi-obj-tiered-history) | truth-apt transformation: indeterminate | Event records to short summary | CompactHook model; success/nonempty test only | Overflow, after removal of old chunk | Summary or restored chunk on empty result | Context replacement | No semantic truth check | Old verbatim records can leave prompt-visible recent history | see record | see record | none | none | Exact values are requested, not verified. |
| [EPI-RTE-history-summary](#epi-rte-history-summary) | retention | implemented | [EPI-OBJ-tiered-history](#epi-obj-tiered-history) | no content change | Summary enters working deque and later get | Bounded queue/window selectors | see record | Summary delivered in later context | Advisory context | Retained candidate, not accepted claim | Calling model can rely on summary | see record | see record | none | retention-before-acceptance | No direct report reload in inspected get/session creation. |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | retention | implemented | [EPI-OBJ-corpus-records](#epi-obj-corpus-records) | truth-apt transformation: acquisition/import | Supplied documents appended to corpus | Backend-name and I/O contract | see record | Persistent normalized documents | Storage admission | Source warrant unknown; no truth criterion | Later retrieval can select text | see record | see record | none | ingestion-not-acceptance | No named proposition accepted for a defined use. |
| [EPI-RTE-corpus-ranking](#epi-rte-corpus-ranking) | operational admission/selection/consumption | implemented | [EPI-OBJ-corpus-records](#epi-obj-corpus-records) | truth-apt transformation: non-ampliative reshaping | Query ranks retained documents | BM25 lexical score or fitted TF-IDF/cosine | On retrieval | Top-k records with scores | Ranking, not enforcing truth | Similarity ordering only | Workflow/data consumer gets selected subset | see record | see record | none | none | Model injection depends on subsequent caller. |
| [EPI-RTE-evaluator-reports](#epi-rte-evaluator-reports) | check/evidence production | implemented | [EPI-OBJ-evaluation-report](#epi-obj-evaluation-report) | truth-apt transformation: indeterminate | Named tool/agent behavior and source quality | Model agent, requested source/direct cases and rubric | Caller-requested evaluation | Scored report, partial report or failure | Advisory | Potential evidence about tested cases only | Parent can request revision/rollback | see record | see record | [RT-CLM-self-evolution](runtime.md#rt-clm-self-evolution) | rubric-not-independent-oracle | Expected answers chosen by evaluating model; no observed case/check. |
| [EPI-RTE-workflow-checks](#epi-rte-workflow-checks) | check/evidence production | implemented | [EPI-OBJ-record-values](#epi-obj-record-values) | truth-apt transformation: entailed derivation | Prediction versus caller ground truth | ExactMatchBenchmark numeric tolerance/string equality | Benchmark step/batch | Per-task score and mean | Data result, not adoption gate | Equality within encoded comparison domain | Scope outputs can drive user-authored next steps | see record | see record | none | reference-truth-unchecked | Does not prove reference, encoding or producing mechanism. |
| [EPI-RTE-workflow-checks](#epi-rte-workflow-checks) | check/evidence production | implemented | [EPI-OBJ-evaluation-report](#epi-obj-evaluation-report) | truth-apt transformation: indeterminate | VERIFY item | min_votes model-agent calls | VERIFY step | One verdict or verdict list | Returned evidence only | No consensus aggregation or truth license from call count | Workflow receives results for separately authored logic | see record | see record | none | verify-name-not-acceptance | Repeated calls need not be independent. |
| [EPI-RTE-record-transforms](#epi-rte-record-transforms) | content transformation | implemented | [EPI-OBJ-record-values](#epi-obj-record-values) | truth-apt transformation: non-ampliative reshaping | Record fields/order/subset/evaluation envelope | Fixed Python transformations | Process step | Projected, renamed, filtered or shaped records | Data output | Preservation limited to retained fields/records | Downstream pipeline consumes transformed records | see record | see record | none | lineage-can-be-dropped | Projection can discard provenance. |
| [EPI-RTE-record-transforms](#epi-rte-record-transforms) | content transformation | implemented | [EPI-OBJ-record-values](#epi-obj-record-values) | truth-apt transformation: entailed derivation | Numeric consecutive price values to return | Python arithmetic under field/order premises | derive_return call | New return column | Data output | Conditional arithmetic relation, not market explanation | Pipeline can use return values | see record | see record | none | none | Missing/non-numeric values and zero predecessor yield null; input truth not warranted. |
| [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | check/evidence production | implemented | [EPI-OBJ-workflow-evaluation](#epi-obj-workflow-evaluation) | no content change | Evaluation identity, terminal state, success consistency | Code against registered version/hash and retained run | Before recording | Reject or normalized evaluation | Enforcing evidence admissibility | Recorded-run linkage and metric provenance only | Invalid evidence write blocked | see record | see record | none | none | Quality remains caller judgment; static negative needs only case ID. |
| [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | disposition/acceptance | implemented | [EPI-OBJ-workflow-evaluation](#epi-obj-workflow-evaluation) | no content change | Evaluation record admission, not workflow quality acceptance | Same validation results | Before append | Evaluation retained or exception | Enforcing write gate | Acceptance as tracking evidence under lineage criterion | Admits records, not permission to execute workflow | see record | see record | none | evidence-admission-not-product-acceptance | No evidence-consuming adoption decision established. |
| [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | retention | implemented | [EPI-OBJ-workflow-evaluation](#epi-obj-workflow-evaluation) | no content change | Version-linked evaluation append/save/reload | Context manager | see record | Persisted evaluations; current-version readback | Tracking | Evidence ledger, not accepted theory | inspect_workflow can expose current evidence | see record | see record | none | none | Old-version records filtered from current view. |
| [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | check/evidence production | implemented | [EPI-OBJ-workflow-evaluation](#epi-obj-workflow-evaluation) | truth-apt transformation: entailed derivation | Current-version aggregates and healthy flag | At least 3 distinct cases, success rate ≥0.8, average quality ≥0.7 | Summary/inspect call | Boolean and aggregate values | Advisory summary | Threshold satisfaction over submitted evidence | Foreground agent may keep/optimize/rollback | see record | see record | [RT-CLM-self-evolution](runtime.md#rt-clm-self-evolution) | threshold-not-mandatory-adoption | No automatic keep/rollback consumer found in inspected path. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | check/evidence production | implemented | [RT-OBJ-extension-source](runtime.md#rt-obj-extension-source) | no content change | Generic agent loop health after registration | Response.success and no constraint stop; not candidate exercise | Optional default-on post-registration smoke | Probe success/failure | Feeds rejecting consumer | Synthetic loop completion only | Failed check triggers best-effort revert/unload | see record | see record | [EPI-CLM-smoke-safety](#epi-clm-smoke-safety) | candidate-not-required | Does not compare exact OK or prove benefit/safety. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | disposition/acceptance | implemented | [RT-OBJ-extension-source](runtime.md#rt-obj-extension-source) | non-truth-apt policy/content update: executable capability admission | Proposed file to live registry | Path/syntax/overwrite/registration, optional smoke | Automatic generator hook or Gateway promotion | Install or reject/recover | Permissive then rejecting | Operational admissibility, not epistemic endorsement | Code may execute before probe; future callers use active version | see record and [RT-BAP-extension-execution](runtime.md#rt-bap-extension-execution) | see record | [RT-CLM-user-approval](runtime.md#rt-clm-user-approval) | approval-not-invariant | Arbitrary import/external effects not undone by archive restore. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | retention | implemented | [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest) | no content change | Active files/manifests/archive | see record | see record | Reloadable installed version | Executable persistence | No accepted ampliative claim established | Startup and later dispatch load retained capability | see record | see record | [EPI-CLM-continuous-improvement](#epi-clm-continuous-improvement) | installation-not-benefit | Later use and improvement unobserved. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | behavior/policy adaptation | doctrine only | [RT-OBJ-meta-agent](runtime.md#rt-obj-meta-agent) | non-truth-apt policy/content update: keep, optimize or withdraw using evaluation | Evaluator evidence to choice of capability version | MetaAgent prose policy; human/model compliance unobserved | After evaluator/optional comparison | Requested keep/rollback/optimize | Advisory instruction to model | No independent transfer/mechanism license | Model can use evolution_tool rollback/unload | see record and [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | see record | [RT-CLM-self-evolution](runtime.md#rt-clm-self-evolution) | requested-not-exercised | Standing machinery exists; actual evaluation-shaped choice absent from evidence. |
| [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration) | operational admission/selection/consumption | implemented | [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager) | non-truth-apt policy/content update: endpoint and instruction configuration | Caller edit to active configuration | Field/type/provider validation | see record | Updated configuration | Enforcing schema, permissive update | No quality comparison | Later requests may use changed endpoint/skill | see record | see record | none | alternate-admission | Human authorship unresolved; restart persistence uninspected. |
| [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) | lineage/freshness/recovery | implemented | [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint) | no content change | Resume identity and completed invocation reuse | Version/hash/runtime checks | On resume | Reject, reuse completed record, or requeue incomplete work | Enforcing execution identity | Identity/cache eligibility only | Controls reexecution, not truth of cached output | see record | see record | none | recovery-not-revalidation | Partial external effects may repeat. |

No lifecycle-integration row is claimed: inspected retention/operational use does not by itself establish post-acceptance integration of a truth-apt ampliative claim. That is a limit of these routes, not an absence conclusion for all shipped operations.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-self-evolution](runtime.md#rt-clm-self-evolution) | see record | see record | see record | [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [EPI-RTE-evaluator-reports](#epi-rte-evaluator-reports), [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | None registered | No before/after or component intervention | Improvement-directed change, evaluators, evidence ledger and withdrawal affordances | Does not establish exercised evidence-responsive improvement. |
| [RT-CLM-user-approval](runtime.md#rt-clm-user-approval) | see record | see record | see record | [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | None registered | Automatic tool-hook route is counterexample to universal approval enforcement | Prompt policy, not invariant | Per-content user answer not consumed on that path. |
| [EPI-CLM-continuous-improvement](#epi-clm-continuous-improvement) | see record | see record | README claim; evolution/evaluation guidance | [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [EPI-RTE-workflow-evidence](#epi-rte-workflow-evidence) | None registered | Quality scores and installed changes do not identify benefit | Implemented capability ecosystem change path | Continuous beneficial operation unestablished. |
| [EPI-CLM-smoke-safety](#epi-clm-smoke-safety) | see record | see record | Smoke module's safety-net description | [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | None registered | General agent can finish without invoking candidate; probe runs after registration | Bounded generic-loop health check with rejecting consumer | Not candidate correctness, import sandbox or comprehensive first-use failure detection. |

## Bounded conclusion

Autogenesis has several independent routes, not one epistemic evaluator. Web pages and corpus documents are acquired with **unknown source warrant**. Search reports and history compaction request factual preservation but do not check semantic fidelity. Their later model-facing messages can affect decisions without a truth-apt acceptance step. Corpus ranking selects lexical/vector similarity; it neither endorses truth nor by itself demonstrates model reliance. These findings are bounded by [EPI-RTE-web-reports](#epi-rte-web-reports), [EPI-RTE-history-summary](#epi-rte-history-summary), [EPI-RTE-corpus-ranking](#epi-rte-corpus-ranking) and [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission).

The deterministic record and exact-match routes support conditional deductions. A numeric return follows from numeric predecessors under the inspected arithmetic and ordering convention; a benchmark score follows from a prediction/reference pair under the comparator. Neither warrants source prices, reference answers, explanatory mechanism or transfer. [EPI-RTE-record-transforms](#epi-rte-record-transforms) and [EPI-RTE-workflow-checks](#epi-rte-workflow-checks) retain concrete source-level examples. No target run is needed for these implementation deductions.

Model evaluators request tests and scored criticism, while VERIFY collects agent verdicts without deciding a consensus. Those are implemented evidence-production paths, not evidence of observed correct reports. The workflow evidence ledger is stronger on **lineage** than a free-form score: registered identity/hash, terminal state, recorded success and duplicate-run checks constrain successful submissions. Its healthy flag is a reproducible aggregate over submitted records, but quality and case identity still partly originate with the caller. Inspection returns the evidence to agents; keep/rollback remains requested decision policy. This newly inspected route supplements, rather than supersedes, the valid runtime container [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution).

Operational change admission is clear even where epistemic acceptance is not. Registration grants immediate executable authority and durable future dispatch; smoke may subsequently withdraw it. Smoke acceptance means generic-loop completion under its flags, not verified use, safety or effectiveness of the proposed capability. Rollback/unload are implemented intervention affordances; choosing them because a particular criticism was correct remains unobserved. There is no evidenced acceptance of an ampliative truth claim against a named criterion for an intended use, followed by lifecycle integration, on the assessed routes. Uninspected scientific, browser, reviewer and other evaluator leaves prevent extending that statement to the whole system.

For the capability ecosystem across later dispatches/restarts, the task-completion objective is independent of the update. [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) establishes a standing improvement-directed self-change path and live consumers. No supplied episode establishes that objective-bearing evidence selected this particular update or that subsequent operation causally depended on it; successful self-improvement and improved future capacity remain unestablished. Reflection, autonomous theory building and each theory-builder condition retain the runtime's separate evidence limits; a scored report or retained healthy flag does not fill missing content-directed criticism and iterative use. Provider weights and internal updates remain inaccessible; the local model configuration can resolve another model without demonstrating local parameter learning.

## Shared records

### Operative objects

#### EPI-OBJ-web-report
Label: Web source text and research report

Source-native identity: WebFetcherTool formatted page text, WebSearcherTool per-result summary and merged_summary. Natural-language assertions in transient dictionaries and Response.message; URLs/titles are symbolic lineage fields. Distinct from [RT-OBJ-meta-agent](runtime.md#rt-obj-meta-agent), which is governing instruction, not acquired evidence. No counterpart among supplied objects. SRC-1: `autogenesis/tool/default/web_fetcher.py`, `autogenesis/tool/default/web_searcher.py` (implementation).

> formatted = f"Title: {title}\nContent: {markdown}"
> --- `autogenesis/tool/default/web_fetcher.py`

> Content: {raw_content[:self.max_length]}
> --- `autogenesis/tool/default/web_searcher.py`

#### EPI-OBJ-tiered-history
Label: Tiered history records and working summaries

Source-native identity: TieredMemory state.recent, state.working and get result. Natural-language event assertions and model summaries in RAM deques; timestamps/status/session keys are symbolic selectors. Persistence serializes through subclass renderers to per-session files. Distinct from [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint), which controls workflow replay rather than model history. No supplied object counterpart. SRC-1: `autogenesis/memory/default/tiered.py` (implementation).

> lines.append("## Working Memory")
> lines += [f"- {s}" for s in working]
> --- `autogenesis/memory/default/tiered.py`

#### EPI-OBJ-corpus-records
Label: Knowledge corpus records

Source-native identity: corpus.jsonl documents and retrieval records; natural-language text plus symbolic metadata/score/backend fields, on disk and in RAM. This is the material retained by [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), which is a route, not a duplicate object. Source warrant is not established by coercion; dictionaries retain fields but retrieval overwrites any existing score. SRC-1: `autogenesis/knowledge/server.py` (implementation).

> results = [{**docs[index], "score": score} for index, score in hits if 0 <= index < len(docs)]
> --- `autogenesis/knowledge/server.py`

#### EPI-OBJ-evaluation-report
Label: Model evaluator reports

Source-native identity: AgentEvaluateAgent/ToolEvaluateAgent Response.message and workflow VERIFY verdicts. Natural-language judgments and localized score labels interpreted by a later model; carried in transient Responses and any retained action history. Distinct from governing [RT-OBJ-self-evolving](runtime.md#rt-obj-self-evolving); no supplied report object counterpart. SRC-1: `autogenesis/agent/evaluator/agent_evaluate_agent.py`, `autogenesis/agent/evaluator/tool_evaluate_agent.py`, `autogenesis/prompt/default/tool_evaluate_agent.html`, `autogenesis/workflow/runtime.py` (implementation; rubric doctrine/design).

> - Read the structured `results` and assign per-dimension scores using the rubrics in `<evaluation-rules>`.
> - Call `done_tool` with the complete report.
> --- `autogenesis/prompt/default/tool_evaluate_agent.html`

#### EPI-OBJ-workflow-evaluation
Label: Version-scoped workflow evaluations

Source-native identity: WorkflowEvaluation, _evaluations and evaluation_summary. Symbolic version/run/hash/success/quality/metric records and aggregates in RAM and evaluations.json; notes are natural-language explanations, with no inspected content-directed criticism instance. Distinct from [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint): it records evaluative evidence about runs, not execution resumption state. SRC-1: `autogenesis/workflow/context.py`, `autogenesis/tool/default/evolution.py` (implementation).

> self.evaluation_path = str(Path(evaluation_path or os.path.join(self.base_dir, "evaluations.json")))
> --- `autogenesis/workflow/context.py`

#### EPI-OBJ-record-values
Label: Pipeline records and comparator scores

Source-native identity: process record dictionaries, derive_return output column, ExactMatchBenchmark task.score and batch mean. Symbolic typed fields/numbers and fixed consumer rules, in transient Python lists/Task objects and workflow scope; not distributed model parameters. Different from [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint), though pipeline results can enter a checkpoint. No supplied record-value counterpart. SRC-1: `autogenesis/process/default/records.py`, `autogenesis/benchmark/default/exact_match.py`, `autogenesis/benchmark/server.py` (implementation).

> task.score = score
> self._tasks.append(task)
> --- `autogenesis/benchmark/default/exact_match.py`

### Routes

#### EPI-RTE-web-reports
Label: Web acquisition and report synthesis

Distinct from [RT-RTE-task-execution](runtime.md#rt-rte-task-execution): this is a callable tool's internal content pipeline, not agent scheduling. Owner: WebFetcherTool/WebSearcherTool. URL/query → fetch/search results → optional page summary → optional merged report → Response.message. Public flags govern fetch/summary/merge. Source text is truncated before model summarization; output includes a reference list but no entailment check. Models propose text; nonempty output admits the summary/report; exceptions use placeholders or mechanical fallback. No per-content human decision is consumed; caller identity unresolved. Open query mode, not a controlled experiment. SRC-1: `autogenesis/tool/default/web_fetcher.py`, `autogenesis/tool/default/web_searcher.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted fetched page or search/report text in message and query/count/merged-summary metadata in data.
- Later read-back: uninspected — this tool does not itself establish a durable store or later model call; action-memory retention can retain its message.
- Delegated visibility: Foreground caller gets synthesized report or fallback source listing; original raw_content is not returned as a complete records array in the inspected search Response.data.
- Selection predicate: Query/URL, search-engine results and enabled fetch/summary/merge flags; each page summary receives only max_length characters.
- Invalidation or expiry: Transient result dictionaries leave scope after return; no per-source withdrawal or durable revision handler here.
- Activation or effect: Message supplies candidate evidence to caller; compliance, reliance and benefit unobserved.
- Evidence limits: Extraction/search adapters and source reliability uninspected; requested factuality/citation is not checked preservation or acceptance.

> if response and response.message.strip():
>     result["summary"] = response.message.strip()
> --- `autogenesis/tool/default/web_searcher.py`

> if merged_summary:
>     output_message = merged_summary
> --- `autogenesis/tool/default/web_searcher.py`

#### EPI-RTE-history-summary
Label: Trace history compaction and later context

Distinct from [RT-RTE-task-execution](runtime.md#rt-rte-task-execution): internal retained-context transformation rather than task lifecycle. TieredMemory ingests action/agent events, stores event.message or error and status, removes old recent chunks on overflow, calls CompactHook, and appends returned summaries to bounded working memory. get selects recent tail and working summaries. Session creation constructs fresh state, not a file loader. Long todo descriptions also use model summarization with length truncation; todo content's downstream authority is not established by this get path. SRC-1: `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: emit mutates memory; CompactHook returns text; get returns selected Markdown or None.
- Later read-back: get returns last working_fetch summaries and recent tail by session ID; the agent consumer is supplied in RT-RTE-task-execution. Summaries are retained between model invocations; disk persistence is separate from restart recall.
- Delegated visibility: Context ID selects separate session history; no automatic parent/child history union in this path.
- Selection predicate: recent_max overflow triggers code-selected oldest compact_chunk records; latest working summary accompanies them; get applies working_fetch and short_term_n.
- Invalidation or expiry: Compaction removes chunk; empty summary restores it; bounded working deque and session eviction can remove prompt-reachable material. No semantic-validation rollback is present in inspected compaction.
- Activation or effect: Summary replaces verbatim history available to later context; model behavior change unobserved. Old retained file content is not automatically dereferenced by a path in a prompt.
- Evidence limits: Summary can reshape or add claims; absence of input/output examples prevents assigning semantic preservation or ampliative conjecture. This does not establish universal memory behavior.

> chunk = [state.recent.popleft() for _ in range(k)]
> --- `autogenesis/memory/default/tiered.py`

> if text:
>     state.working.append(text)
> else:
>     async with state._lock:  # lossless: restore and stop
>         state.recent.extendleft(reversed(chunk))
>     break
> --- `autogenesis/memory/default/tiered.py`

> text = response.message.strip() if response.success else ""
> --- `autogenesis/hook/default/compact.py`

#### EPI-RTE-corpus-ranking
Label: Corpus backend ranking

Part of: [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)

This part owns the backend ranking and returned-record transformation within the supplied ingest/retrieve route. BM25 lowercases/splits texts and query; TF-IDF fits current texts and cosine-ranks query. Numeric weights are freshly computed representations, not evidence of a trained persistent epistemic policy. Owning code calls external ranking libraries, whose internals are uninspected. SRC-1: `autogenesis/knowledge/default/rankers.py`, `autogenesis/knowledge/server.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked index/score pairs become top-k corpus records in Response.data.
- Later read-back: Corpus is reread on retrieval; freshly ranked retained documents reach caller, not automatically the model.
- Delegated visibility: Workflow normalization preserves data records; Agent paths returning only message would need a separate bridge to convey records.
- Selection predicate: Query lexical overlap or TF-IDF cosine, descending score, top_k at least one; no minimum truth/relevance threshold.
- Invalidation or expiry: Corpus/backend manifest changes affect next retrieval; no persistent index/update policy in these backend methods.
- Activation or effect: Ranking selects and orders what caller sees; does not establish changed model behavior or source endorsement.
- Evidence limits: Derived similarity is a retrieval signal; input provenance and external library correctness remain unestablished.

> matrix = vectorizer.fit_transform([str(text) for text in texts])
> query_vector = vectorizer.transform([str(query)])
> sims = cosine_similarity(query_vector, matrix)[0]
> --- `autogenesis/knowledge/default/rankers.py`

#### EPI-RTE-evaluator-reports
Label: Tool and agent quality reports

Different from [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission): produces advisory evidence rather than installs a capability. AgentEvaluateAgent and ToolEvaluateAgent delegate unchanged to base loop. Tool rubric requests known valid/invalid cases, interface inspection, source review and qualitative performance checks. Target is a named tool's behavior on the selected cases and source, not universal task success. Model chooses tests, expected answers and scores; code enforces ordinary routing/budgets, not rubric validity. Native roster respects allowlists, so prompt assertion that any registered target is callable is conditional on exposure. No mandatory human evaluator or independent oracle is supplied. Open task-directed evaluation; expected values are requested, not independently authenticated. SRC-1: `autogenesis/agent/evaluator/tool_evaluate_agent.py`, `autogenesis/agent/evaluator/agent_evaluate_agent.py`, `autogenesis/prompt/default/tool_evaluate_agent.html`, `autogenesis/agent/native_tools.py` (implementation and rubric doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ordinary evaluator Response, intended to carry scored report; no registrable artifact.
- Later read-back: uninspected — evaluator classes do not add a durable report ledger; caller/action memory may retain response text.
- Delegated visibility: Parent receives evaluator message under the supplied child-return route; not necessarily all structured Response.data or raw test evidence.
- Selection predicate: Caller names target and cases; registered evaluator, exposed tools, max steps and model decisions govern actual work.
- Invalidation or expiry: Model may revise report within task; no automatic score-triggered rejection/expiry of capability in these classes.
- Activation or effect: Parent can read report and request optimization/rollback; no observed evaluation-consumption episode.
- Evidence limits: Rubric is not a measured oracle. Self-selected expected answers, omitted cases and source-only performance assessment limit warrant.

> return await super().__call__(task=task, files=files, ctx=ctx, **kwargs)
> --- `autogenesis/agent/evaluator/tool_evaluate_agent.py`

> - Verify `success=True`, correct `message`, and correct `data` values (results live in `response.data`, a dict — NOT in `extra`).
> - Score guide: 20 = all cases pass; −4 per failing case.
> --- `autogenesis/prompt/default/tool_evaluate_agent.html`

#### EPI-RTE-workflow-checks
Label: Workflow verdicts and benchmark checks

Part of: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)

VERIFY invokes min_votes agent calls per item and returns verdicts; it does not compare or vote them into an acceptance decision. BENCHMARK invokes a named benchmark on normalized results; exact_match is the directly inspected comparator. Caller provides prediction/reference pairs; missing IDs and evaluation exceptions score zero in batch manager. A workflow benchmark Response succeeds even for score zero. _normalize blocks failed Responses but preserves data on successful ones, so data-dependent rejection needs separate authored control logic. No human per-item approval is read; caller origin unresolved. Bounded comparison mode, no verified improvement trigger. SRC-1: `autogenesis/workflow/runtime.py`, `autogenesis/benchmark/server.py`, `autogenesis/benchmark/default/exact_match.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verdict(s), or benchmark mean/count in successful Response.data; workflow normalization preserves message/data/files.
- Later read-back: uninspected — checkpoint persistence belongs to the supplied outer route; comparator retains Task list only in process for stats, not an inspected cross-restart result ledger.
- Delegated visibility: VERIFY agents receive resolved item arguments; workflow gets verdict values, not automatically a causal explanation or complete trace.
- Selection predicate: Workflow step type/target/items/min_votes; benchmark task ID, prediction and ground_truth; exact match strips strings and tries floats before string equality.
- Invalidation or expiry: Batch errors map to zero; exact-match reset clears task list; failed Response normalization raises, but zero score alone does not reject workflow.
- Activation or effect: Result is available to downstream scope references; no automatic truth acceptance or policy update in these branches.
- Evidence limits: Reference warrant, case selection and model-verdict independence unknown. Full dataset-specific evaluators uninspected.

Concrete source deduction, not target execution: prediction `" 2 "` and ground_truth `"2.0"` strip to `2` and `2.0`; float difference is zero, so exact_match assigns 1.0. This proves agreement under the comparator, not the factual truth of either string. Conversely two missing/empty values do not pass because pred must be nonempty.

> if pred:
>     try:
>         score = 1.0 if abs(float(pred) - float(gt)) < 1e-9 else 0.0
>     except (TypeError, ValueError):
>         score = 1.0 if pred == gt else 0.0
> --- `autogenesis/benchmark/default/exact_match.py`

> return verdicts[0] if step.min_votes == 1 else {"item": item, "verdicts": verdicts}
> --- `autogenesis/workflow/runtime.py`

> return {"message": value.message, "data": value.data, "files": value.files}
> --- `autogenesis/workflow/runtime.py`

#### EPI-RTE-record-transforms
Label: Record reshaping and arithmetic derivation

Part of: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)

Process manager calls can invoke registered record processors. The directly read file implements projection, head, rename, filtering, sort, evaluation-envelope mapping and return derivation. Fixed Python rules, not model judgment, select rows/fields and derive numbers. Caller specifies fields/mapping/order; no evidence/human acceptance decision is consumed. These functions are not truth checks or improvement selection. SRC-1: `autogenesis/process/default/records.py`; outer dispatch supplied by runtime (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Response.data records/count or argument failure.
- Later read-back: inapplicable — processors themselves retain no updated artifact; workflow output/checkpoint consumers are separate.
- Delegated visibility: Downstream workflow sees normalized data; projections may remove provenance while preserving selected values.
- Selection predicate: Configured fields, filters, sort key, count, evaluation mapping or arithmetic source field.
- Invalidation or expiry: Per-call output only; invalid required fields/operators reject; no rollback or endorsement history.
- Activation or effect: Produces transformed values available to downstream pipeline; no observed use or benefit.
- Evidence limits: Return interpretation assumes chronological numeric prices. In missing-value cases prev tracks previous numeric value, not necessarily the immediately preceding row.

Concrete source deductions: select_fields on `[{"text":"A","source":"S"}]` with fields `["text"]` yields `[{"text":"A"}]`, retaining text but dropping its source. derive_return on `[{"close":100},{"close":110}]` produces returns null and 0.1. The second is a new arithmetic proposition conditional on supplied values, not ampliative market knowledge. These are implementation deductions, not observed executions.

> out = [{k: row.get(k) for k in keep} for row in rows if isinstance(row, dict)]
> --- `autogenesis/process/default/records.py`

> if isinstance(current, (int, float)) and isinstance(prev, (int, float)) and prev != 0:
>     ret = (current - prev) / prev
> out.append({**row, output: ret})
> if isinstance(current, (int, float)):
>     prev = current
> --- `autogenesis/process/default/records.py`

#### EPI-RTE-workflow-evidence
Label: Workflow evaluation evidence ledger

Part of: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)

This is an evaluation-maintenance part of the workflow lifecycle, not a duplicate of runtime's executable invocation/recovery account. evolution_tool record_workflow_evaluation creates a WorkflowEvaluation from caller inputs. WorkflowContextManager checks active version, retained run identity/hash, terminal state and success agreement; it substitutes measured run token/time fields and rejects duplicate run IDs. A static failure needs case_id; successful evidence needs a real run. Caller supplies quality and notes. A read-only WorkflowEvaluateAgent explicitly allows this recording action and can expose the target workflow. No human veto or independent quality oracle is consumed. Evaluation mode is caller/model-selected cases; guideline thresholds target keep/optimize/rollback, not automatic promotion. Writes persist records, not a new capability. SRC-1: `autogenesis/tool/default/evolution.py`, `autogenesis/workflow/context.py`, `autogenesis/agent/evaluator/workflow_evaluate_agent.py`, `autogenesis/tool/default/inspect_workflow.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored evaluation and current summary from evolution_tool, or failed Response on exception.
- Later read-back: Context initialization loads evaluation records; current-version filtering feeds summary and inspect_workflow. inspect message includes aggregate summary and count; data additionally contains individual evaluations.
- Delegated visibility: Evaluating agent can record and inspect evidence; a parent receiving only inspect/evaluator message need not receive individual notes present only in data.
- Selection predicate: Active workflow/version, run/hash/state/success checks or static failure case_id, nonduplicate run; current-version records aggregated. Healthy requires 3 distinct cases, success rate at least 0.8 and average quality at least 0.7.
- Invalidation or expiry: Different active version filters old records out of evaluations(name); duplicate run rejected. Individual evidence rollback/deletion not established by inspected methods; capability rollback/unload is a separate evolution_tool action.
- Activation or effect: Successful record admission appends/saves and changes computed summary; inspect returns summary to model as advisory evidence. No mandatory automatic keep/rollback branch consumes healthy in the inspected runtime dispatch/evidence path.
- Evidence limits: Success agrees with recorded workflow lifecycle, not necessarily user-goal satisfaction. Quality and case labels are caller supplied; no supplied trace establishes an actual evidence-shaped change.

> if evaluation.success != run.successful:
>     raise ValueError("Evaluation success must match the recorded Workflow run")
> --- `autogenesis/workflow/context.py`

> if evaluation.run_id and any(item.run_id == evaluation.run_id for item in existing):
>     raise ValueError("This Workflow run has already been evaluated")
> existing.append(evaluation)
> self._save_evaluations()
> --- `autogenesis/workflow/context.py`

> "healthy": len(distinct_cases) >= 3 and success_rate >= 0.8 and quality >= 0.7,
> --- `autogenesis/workflow/context.py`

> f"- **Evaluation Summary**: {summary}\n\n"
> --- `autogenesis/tool/default/inspect_workflow.py`

### Claims

#### EPI-CLM-continuous-improvement
Label: Continuous capability improvement

Claimed operation: ongoing generator/optimizer/evaluator activity improves tool, skill and agent ecosystem. Broader outcome wording than [RT-CLM-self-evolution](runtime.md#rt-clm-self-evolution)'s task-serving change claim; the overlap is explicit, not an independent observed result. SRC-1: `README.md` (doctrine/design).

> A self-evolving multi-agent framework. A **MetaAgent** orchestrates sub-agents to complete user tasks, while optimizer / evaluator / generator agents continuously improve the tool, skill, and agent ecosystem.
> --- `README.md`

#### EPI-CLM-smoke-safety
Label: Smoke first-use safety net

Claimed operation: synthetic replay catches evolved components that import but break the loop before manifest commitment. Distinct from [RT-CLM-user-approval](runtime.md#rt-clm-user-approval); both concern admission but different warrants. SRC-1: `autogenesis/extension/smoke_gate.py` (module description doctrine/design; probe body implementation). Runtime's admission record supplies counterevidence about manifest timing. The code's general-agent choice and success predicate do not require candidate invocation or exact OK equality.

> A newly generated tool/agent/prompt that
> imports cleanly but blows up the loop (bad schema, exception on first use,
> runaway) is caught here before it is committed to the manifest.
> --- `autogenesis/extension/smoke_gate.py`

> probe_agent_name = "general_agent"
> --- `autogenesis/extension/smoke_gate.py`

> ok = bool(getattr(resp, "success", False)) and not data.get("stopped_by_constraint", False)
> --- `autogenesis/extension/smoke_gate.py`
