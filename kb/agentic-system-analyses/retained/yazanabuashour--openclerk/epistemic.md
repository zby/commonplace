---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenClerk epistemic routes: source acquisition, synthesis, source-sensitive repair, retrieval authority and bounded evaluation."
run-id: AAS-2026-10-16-openclerk-ec0e00c2bb0a-01
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
---

# OpenClerk epistemic report

## Source-and-claim boundary

The question is how OpenClerk's knowledge interface acquires claims, checks them and authorizes later reliance. Scope and exclusions are those of the [boundary and Source register](boundary.md#source-register), SRC-1. This is implementation and doctrine/design inspection, not target execution. External host reasoning, provider weights, private vault quality and actual human approval remain unobserved. Source identity is not a truth guarantee.

The supplied runtime is provisional rather than an inspection ceiling. Direct inspection adds compilation, source-sensitive audit/repair, web extraction, OCR candidate intake and retrieval regression evaluation. Compilation and repair are important counterexamples to treating OpenClerk as storage alone. They do not establish general semantic validation. The claims assessed are [EPI-CLM-markdown-authority](#epi-clm-markdown-authority), [EPI-CLM-source-repair](#epi-clm-source-repair), and [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary). No independent claim to infallible or general autonomous knowledge production was found in the inspected README and agent contract; that is not a repository-wide absence finding.

| Entry point or operation | Source path | Coverage and records, or limitation |
|---|---|---|
| CLI dispatch | SRC-1, `cmd/openclerk/main.go` | Direct switch inspection: document, retrieval, clerk, module, config, inspect, init, demo and informational commands. No hook dispatcher appears in this inspected switch; not a global hook absence. |
| Context pack and session planning | SRC-1, `internal/chronicler/chronicler.go` | Supplied [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), [RT-RTE-session-plan](runtime.md#rt-rte-session-plan); no new claim of full-document delivery. |
| Lifecycle writes, promotion, rollback | SRC-1, `internal/runner/document.go` | Supplied [RT-RTE-document-write](runtime.md#rt-rte-document-write); direct compile/validation dispatch read. Detailed move, git lifecycle and cleanup internals uninspected here: prevents universal withdrawal/rollback conclusions. |
| compile_synthesis and disposable validation_synthesis | SRC-1, `internal/runner/compile_synthesis.go` | Direct full read; [EPI-RTE-synthesis-build](#epi-rte-synthesis-build), [EPI-RTE-synthesis-write](#epi-rte-synthesis-write). Disposable marker checks are not truth tests. |
| Synthesis invalidation | SRC-1, `internal/infra/sqlite/synthesis.go` | Direct full read; [EPI-RTE-synthesis-freshness](#epi-rte-synthesis-freshness). |
| audit_contradictions / source_audit_report | SRC-1, `internal/runner/audit_contradictions.go`, `internal/runner/source_audit_report.go` | Direct full reads; [EPI-RTE-audit-conflicts](#epi-rte-audit-conflicts), [EPI-RTE-audit-repair](#epi-rte-audit-repair). Runtime omitted these material retrieval-family mutations. |
| Web source ingestion | SRC-1, `internal/infra/sqlite/ingest_source.go` | Direct createWebSourceURL and extraction/note-builder reads; [EPI-RTE-web-import](#epi-rte-web-import). Network/download, PDF, video and update/restore bodies not fully inspected: prevents source-complete fidelity or recovery claims. |
| Artifact/OCR planning | SRC-1, `internal/runner/artifact_candidate_plan.go` | Direct planning and image OCR bodies; [EPI-RTE-artifact-ocr](#epi-rte-artifact-ocr). PDF OCR pipeline and duplicate/confidence helper internals not fully inspected: no OCR accuracy or complete planner characterization. |
| search / semantic_search / module administration | SRC-1, `internal/runner/retrieval.go`, `internal/runner/semantic_search.go`, `internal/runclient/modules.go` | Direct retrieval dispatch and write-mode check; supplied [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search), [RT-RTE-module-install](runtime.md#rt-rte-module-install). Provider internals excluded. |
| retrieval_eval_capture / replay | SRC-1, `internal/runner/retrieval_eval.go` | Direct capture, replay, comparison and metric bodies; [EPI-RTE-eval-capture](#epi-rte-eval-capture), [EPI-RTE-eval-replay](#epi-rte-eval-replay). File-integrity helpers not fully assessed. |
| Other exposed retrieval reports | SRC-1, `internal/runner/retrieval.go` | Dispatch searched: records/services/decisions, graph, provenance, projections, memory_router_recall, source_discovery, evidence_bundle, duplicate_candidate, workflow_guide, structured_store, hybrid_retrieval, graph_context/relationship/maintenance, diagnostics and maintenance_report. Their transformation and downstream handoff bodies remain uninspected here; prevents a system-complete negative about derivation, checks or adaptation. |
| Shipped Codex evaluation caller | SRC-1, `scripts/agent-eval/ockp/codex_runner.go`, `scripts/agent-eval/ockp/verify_helpers.go` | Supplied [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn); no independent execution evidence. Bundled results and further scenario verifiers unassessed; no score or causal benefit adopted. |
| Demo, initialization, release and maintainer paths | SRC-1, `cmd/openclerk/main.go`, `scripts/`, `docs/` | Boundary-included but detailed paths not assessed here. Prevents exhaustive state-producer, release-integrity and improvement-loop conclusions. |

Available uninspected files are not access gaps. Missing linked deployment traces prevent conclusions about exercised acceptance, host compliance or retained-output effects; missing intervention/comparison evidence prevents attributing retrieval or task improvement to a component. These limits do not negate implemented routes below.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-note](#epi-obj-source-note) | Imported page assertions; local source status and references | Source note | see record | Authenticity and source truth unknown; HTML extraction can lose relationships. |
| [EPI-OBJ-artifact-plan](#epi-obj-artifact-plan) | Extracted artifact text, proposed body; metadata guesses | Reviewable candidate | see record | OCR text fidelity unknown; planning confidence is not evidence-consuming truth acceptance. |
| [EPI-OBJ-synthesis](#epi-obj-synthesis) | Caller body/facts; copied current-source summary; provenance and freshness assertions | Derived synthesis | see record | Body support is not checked by compilation; freshness is a separate symbolic assessment. |
| [EPI-OBJ-audit-report](#epi-obj-audit-report) | Classified source paths, conflict snippets, repair result | Source-sensitive audit | see record | Numeric-day heuristic and metadata are not a general contradiction oracle. |
| [EPI-OBJ-retrieval-eval](#epi-obj-retrieval-eval) | Result identities, timings, overlap and top-result equality | Regression evidence | see record | No reference relevance labels or task-truth judgment. |
| [RT-OBJ-agent-contract](runtime.md#rt-obj-agent-contract) | Primarily policy, not a candidate factual answer | Agent behavior contract | see record | Delivery does not establish compliance. |
| [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) | Not determinable as individuated propositions in weights/vectors | Similarity ranking | see record | Weights/version and parameter changes uninspected. |
| [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model) | Not determinable as individuated propositions in weights | Evaluation agent inference | see record | Inference label is not immutable parameter identity. |

## Authority-route ledger

Each compact row below owns its architectural assessment. Other fields say `see` where the cited declaration owns them. Implementation is not observed operation. Candidate objects and behavioral paths are resolved in the cited records.

Route ID: [EPI-RTE-web-import](#epi-rte-web-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-note](#epi-obj-source-note).
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown, and HTML relational fidelity potentially degraded.
Transition or check target: see record; public bytes to source note.
Evaluator/condition and domain: see record; parsability/access markers, not source truth.
Activation and timing: see record.
Possible or observed result: see record; possible note or error, not an observed import.
Implemented force: see record; errors prevent reaching this create call, successful extraction supplies its body.
Epistemic authority and scope: attribution to a source, not endorsement of its assertions.
Operational authority: see record; permits note creation and subsequent indexed retrieval.
Behavioral-authority path: see record; canonical storage to later retrieval/agent, permissive then advisory.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-markdown-authority](#epi-clm-markdown-authority).
Mismatch marker or none: none; canonical authority is not a truth certificate.
Gap/limit: metadata and citation checks do not establish content truth.

Route ID: [EPI-RTE-artifact-ocr](#epi-rte-artifact-ocr)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-artifact-plan](#epi-obj-artifact-plan).
Content/update relation: truth-apt transformation: acquisition/import; transcription warrant unknown.
Transition or check target: see record; artifact text to body preview.
Evaluator/condition and domain: see record; module/file/process/nonempty-output checks license extraction availability only.
Activation and timing: see record.
Possible or observed result: see record; review_required candidate or error.
Implemented force: see record; blocks invalid extraction, returns candidate on success.
Epistemic authority and scope: no automatic source-truth or transcription-fidelity acceptance.
Operational authority: see record; suggests a separate create/ingest request, not a durable write.
Behavioral-authority path: see record; planner JSON to host, advisory for current task.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-markdown-authority](#epi-clm-markdown-authority).
Mismatch marker or none: none; module verification and text review are separate.
Gap/limit: cannot establish semantic preservation from external OCR code.

Route ID: [EPI-RTE-synthesis-build](#epi-rte-synthesis-build)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: truth-apt transformation: non-ampliative reshaping for supplied body/facts and extracted summary text; source-role labels are metadata-relative derivations, not independently warranted real-world claims.
Transition or check target: see record.
Evaluator/condition and domain: see record; string/heading/metadata rules, not a semantic judge.
Activation and timing: see record; before write.
Possible or observed result: see record; assembled body with active/fresh headers.
Implemented force: supplies the content consumed by compilation write.
Epistemic authority and scope: preservation/attribution within string operations only; no claim that caller facts follow from source_refs.
Operational authority: see record; output can enter durable synthesis.
Behavioral-authority path: see record; body to store then retrieval and host, permissive storage/advisory use across tasks.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-markdown-authority](#epi-clm-markdown-authority).
Mismatch marker or none: `freshness: fresh` in generated Markdown is not the projection check's verdict.
Gap/limit: factual correctness and accepted ampliative production not established.

Route ID: [EPI-RTE-synthesis-write](#epi-rte-synthesis-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: no content change.
Transition or check target: see record; duplicate target and create/update selection.
Evaluator/condition and domain: deterministic target count and runner input/mode checks; see record.
Activation and timing: see record; before store mutation.
Possible or observed result: see record; skipped duplicate, created, updated or error.
Implemented force: enforcing operational admission, not evidence-consuming truth acceptance.
Epistemic authority and scope: no substantive proposition is licensed as true by duplicate avoidance.
Operational authority: see record; blocks multiple matches; otherwise selects create or replace.
Behavioral-authority path: see record; runner/client storage call, enforcing for this invocation.
Evidence source ID and local anchor: see record.
Claim IDs or none: [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary).
Mismatch marker or none: symbolic approval mode is not authenticated human approval.
Gap/limit: production admission and epistemic acceptance must not be conflated.

Route ID: [EPI-RTE-synthesis-write](#epi-rte-synthesis-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: no content change.
Transition or check target: see record; assembled body to canonical Markdown/derived state.
Evaluator/condition and domain: see record; successful store calls.
Activation and timing: see record.
Possible or observed result: see record; durable synthesis and citation-bearing handoff.
Implemented force: persistence and availability for retrieval, not acceptance or post-acceptance lifecycle integration.
Epistemic authority and scope: remains derived evidence according to returned authority limits.
Operational authority: see record; later calls may retrieve the document.
Behavioral-authority path: see record; store/retrieval/host, permissive then advisory, later tasks.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-markdown-authority](#epi-clm-markdown-authority).
Mismatch marker or none: none.
Gap/limit: no observed later reliance or accepted-claim integration.

Route ID: [EPI-RTE-synthesis-freshness](#epi-rte-synthesis-freshness)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: truth-apt transformation: entailed derivation, conditional on the stored paths, metadata and timestamps being accurate.
Transition or check target: see record; local source-reference currency, not body truth.
Evaluator/condition and domain: see record; missing paths, timestamps, supersession declarations.
Activation and timing: see record; projection rebuild.
Possible or observed result: see record; fresh/stale and reason details, provenance event.
Implemented force: persists status consumed by audit and compilation reports; not automatic rejection/removal of synthesis content.
Epistemic authority and scope: metadata-relative reference currency only.
Operational authority: see record; status informs audit current/superseded selection and host warning.
Behavioral-authority path: see record; projection details to audit code (selection) and report JSON to host (advisory), across rebuilds/tasks.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-source-repair](#epi-clm-source-repair).
Mismatch marker or none: none; freshness does not establish endorsement.
Gap/limit: truthful metadata and source truth are unchecked premises.

Route ID: [EPI-RTE-audit-conflicts](#epi-rte-audit-conflicts)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-audit-report](#epi-obj-audit-report).
Content/update relation: truth-apt transformation: entailed derivation only for the proposition that inspected snippets contain multiple recognized day values; semantic contradiction is indeterminate.
Transition or check target: see record; query-selected current source paths and snippets.
Evaluator/condition and domain: see record; finite number/day token recognizer, at least two nonsuperseded paths.
Activation and timing: see record; explicit conflict_query after target handling.
Possible or observed result: see record; unresolved group or none.
Implemented force: report/handoff evidence; no implemented winner or veto of repair from this later check.
Epistemic authority and scope: local heuristic discrepancy, not general contradiction detection.
Operational authority: see record; host may inspect unresolved evidence.
Behavioral-authority path: see record; report JSON, advisory, current request.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-source-repair](#epi-clm-source-repair).
Mismatch marker or none: source-native `current sources disagree` exceeds the recognizer's semantic license if read literally without its domain limit.
Gap/limit: differing quantities can be compatible; missed quantities do not show agreement.

Route ID: [EPI-RTE-audit-repair](#epi-rte-audit-repair)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthesis](#epi-obj-synthesis), [EPI-OBJ-audit-report](#epi-obj-audit-report).
Content/update relation: truth-apt transformation: non-ampliative reshaping of the first classified current source's Summary; role labels derive from projection metadata.
Transition or check target: see record; existing target Summary, not competing claims' truth.
Evaluator/condition and domain: see record; exactly one target, nonempty current and superseded classes, nonempty current summary.
Activation and timing: see record; explicit repair mode.
Possible or observed result: see record; planned/skipped/applied; unresolved conflicts remain reported.
Implemented force: replaces target Summary, persists it; no automatic epistemic acceptance.
Epistemic authority and scope: declared supersession guides copying; cannot resolve unresolved factual claims.
Operational authority: see record; changes material available to later retrieval.
Behavioral-authority path: see record; projection selection to ReplaceSection (enforcing local effect), later retrieval/host (advisory).
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-source-repair](#epi-clm-source-repair), [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary).
Mismatch marker or none: durable writes also occur through retrieval repair actions, not only the doctrine's document-family workflow.
Gap/limit: source classification and lexicographic first path are not semantic preference judgments.

Route ID: [RT-RTE-document-write](runtime.md#rt-rte-document-write)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: source/synthesis caller bodies; see record.
Content/update relation: no content change at the mode gate.
Transition or check target: see record.
Evaluator/condition and domain: see record; modes, paths and syntax.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: enforcing for covered runner branches, not universal human consent.
Epistemic authority and scope: no factual warrant follows from writing or promotion alone.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary).
Mismatch marker or none: default permissive mode and lower-level callers limit the policy claim.
Gap/limit: no deployment approval trace.

Route ID: [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: retrieved snippets/citations and decision summaries; see records.
Content/update relation: truth-apt transformation: non-ampliative reshaping for delivered text; similarity vectors rank, not warrant assertions.
Transition or check target: see records.
Evaluator/condition and domain: see records; lexical selection versus explicit embedding similarity are separate selectors.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: ranking and bounded context supply, not answer verification.
Epistemic authority and scope: traceable retrieval, source warrant unknown; no automatic endorsement.
Operational authority: see records.
Behavioral-authority path: see records; external host JSON, advisory, current task with later cache reuse on semantic path.
Evidence source ID and local anchor: see records.
Claim IDs or none: [EPI-CLM-markdown-authority](#epi-clm-markdown-authority).
Mismatch marker or none: none; embedding similarity is not a truth evaluator.
Gap/limit: no observation that a host changed its answer.

Route ID: [EPI-RTE-eval-capture](#epi-rte-eval-capture)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-retrieval-eval](#epi-obj-retrieval-eval).
Content/update relation: truth-apt transformation: non-ampliative reshaping of retrieval identities and measurements.
Transition or check target: see record; explicit local capture.
Evaluator/condition and domain: see record; action/path/write-mode checks, not relevance labels.
Activation and timing: see record.
Possible or observed result: see record; JSONL appended or error.
Implemented force: baseline availability, not default-rank modification.
Epistemic authority and scope: regression baseline only.
Operational authority: see record; later replay may consume it.
Behavioral-authority path: see record; local capture to replay, permissive across requests.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: captured top result is not a reference correct answer.

Route ID: [EPI-RTE-eval-replay](#epi-rte-eval-replay)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-retrieval-eval](#epi-obj-retrieval-eval).
Content/update relation: truth-apt transformation: entailed derivation for identifier overlap/top1 equality, conditional on captured/current result identities; timing is measured data.
Transition or check target: see record; ranking stability and latency under replay conditions.
Evaluator/condition and domain: see record; Jaccard/top1/averaging.
Activation and timing: see record.
Possible or observed result: see record; metrics and inspection advice.
Implemented force: advisory report; no automatic successor admission or policy update.
Epistemic authority and scope: bounded regression comparison, not relevance, truth or causal component benefit.
Operational authority: see record; caller decides follow-up.
Behavioral-authority path: see record; handoff to host, advisory, current report.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: corpus/provider changes can confound comparison.

Route ID: [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: scenario output documents/results; see record.
Content/update relation: truth-apt transformation: entailed derivation for required/forbidden substring predicates only.
Transition or check target: see record; bounded scenario outcomes.
Evaluator/condition and domain: see record; scenario-authored answer oracle, not universal truth.
Activation and timing: see record.
Possible or observed result: see record; pass/fail and artifacts, no run supplied here.
Implemented force: evaluation result; no demonstrated release or self-modification admission.
Epistemic authority and scope: checked outcome assertions, not producing mechanism, transfer or replay safety.
Operational authority: see record.
Behavioral-authority path: see record; driver reports, not an implemented autonomous product-successor selector.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no observed or causal experiment established.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-markdown-authority](#epi-clm-markdown-authority) | see record | see record | see record | [EPI-RTE-synthesis-write](#epi-rte-synthesis-write), [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search) | None assessed | None; authority hierarchy is policy and storage organization, not factual certification | Derived outputs preserve citations/authority-limit text; canonical content remains retrievable | A host can rely incorrectly; compliance unobserved |
| [EPI-CLM-source-repair](#epi-clm-source-repair) | see record | see record | see record | [EPI-RTE-synthesis-freshness](#epi-rte-synthesis-freshness), [EPI-RTE-audit-repair](#epi-rte-audit-repair), [EPI-RTE-audit-conflicts](#epi-rte-audit-conflicts) | None assessed | No causal comparison; metadata-relative repair only | Shipped code detects reference staleness, copies classified current summaries and reports some unresolved discrepancies | Not a broad contradiction engine; exact demo execution unassessed |
| [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary) | see record | see record | see record | [RT-RTE-document-write](runtime.md#rt-rte-document-write), [EPI-RTE-audit-repair](#epi-rte-audit-repair) | None assessed | No universal host gate or per-content human authenticator shown | Policy plus narrower mode veto | Retrieval-family repair is another durable path; an omitted mode can be permissive |

## Bounded conclusion

OpenClerk has implemented acquisition, reshaping, retention, retrieval and source-sensitive correction routes, not merely a passive index. Web and OCR intake acquire external assertions with source truth unknown. HTML extraction can degrade relations; OCR checks establish configured extraction availability, not accurate transcription. Candidate planning requests later review and a separate write.

Compilation reshapes caller statements and selected source summaries, adds role labels from metadata, and retains derived synthesis. Its duplicate/path/mode checks admit an artifact for storage; they do not accept substantive claims against an evidence-consuming truth criterion. The code sets an active/fresh header even though independently computed projection freshness can be stale. Neither retained prose nor an operational write establishes accepted ampliative production or post-acceptance lifecycle integration. The inspected deterministic compiler does not demonstrate new explanatory conjectures; uninspected report families and external model reasoning prevent extending that result to every shipped route.

Freshness and supersession provide a real, narrower authority path: local metadata/timestamps produce projection details, audit code selects classified sources, and repair can replace an existing Summary. The target is local reference currency and declared source roles. It is not real-world truth. The conflict recognizer tests a finite day-value pattern in search snippets; it can flag compatible statements and miss genuine contradictions. Its result is advisory and occurs after possible repair, not as a semantic veto before mutation. The source-audit handoff preserves unresolved evidence rather than implementing a winner selection.

Retained documents can reach later agents through cited lexical/semantic retrieval and bounded context packs. Similarity, citation, freshness and successful continuation do not supply source endorsement. Operational authority is specific: mode/path/duplicate gates enforce admission on covered calls; code can mutate the selected Summary; handoff and skill text advise an external host. No inspected trace establishes that a later answer depended on a retained update.

Retrieval replay evaluates result-identity stability and latency; shipped Codex verifiers evaluate bounded scenario predicates. These checks do not establish a generally reliable knowledge producer, a causal benefit of embeddings, or automatic improvement of OpenClerk's own machinery. Distributed-parametric model changes and immutable weight versions remain uninspected. Learning benefit, reflective criticism, autonomous theory-building and exercised self-improvement are independently unestablished by these routes; none is refuted merely by the missing run evidence. A system-complete negative about acceptance or adaptation is withheld because the named shipped reports and maintenance/development paths remain unassessed.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-note
Label: Source note

Source-native identity: web source Markdown produced by createWebSourceURL; source documents also carry status, supersedes and superseded_by metadata. Representational form: natural-language extracted text and symbolic URL/hash/path/time/status fields, assessed separately by their consumers. Storage substrate: canonical Markdown and indexed local storage. Distinct from [RT-OBJ-agent-contract](runtime.md#rt-obj-agent-contract), which is shipped policy, not imported source content; no supplied object counterpart. SRC-1, `internal/infra/sqlite/ingest_source.go`, `internal/infra/sqlite/synthesis.go`. Text consumers see fenced extracted text; projection code reads metadata rather than endorsing assertions.

> body.WriteString("\n## Extracted Text\n")
> --- `internal/infra/sqlite/ingest_source.go`

#### EPI-OBJ-artifact-plan
Label: Artifact candidate plan

Source-native identity: ArtifactCandidatePlan with BodyPreview and optional OCRExtraction. Natural-language candidate text is separate from symbolic paths, status, confidence and next-request JSON. Storage substrate: returned Go value/JSON; durable storage needs a subsequent action. No supplied object counterpart; it is the material candidate output of [RT-RTE-session-plan](runtime.md#rt-rte-session-plan), rather than the whole session orchestration. SRC-1, `internal/runner/artifact_candidate_plan.go`.

> WriteStatus:             "planned_no_write",
> --- `internal/runner/artifact_candidate_plan.go`

#### EPI-OBJ-synthesis
Label: Synthesis

Source-native identity: compiled synthesis Markdown with Summary, Sources, Freshness and generated frontmatter. Natural-language body assertions are separate from symbolic source_refs/status/freshness and derived ProjectionState details. Storage substrate: canonical vault Markdown; SQLite stores document/projection/provenance derivatives. No supplied object counterpart; [RT-RTE-document-write](runtime.md#rt-rte-document-write) is a route container, not this artifact. SRC-1, `internal/runner/compile_synthesis.go`, `internal/infra/sqlite/synthesis.go`.

> "type: synthesis",
> "status: active",
> "freshness: fresh",
> --- `internal/runner/compile_synthesis.go`

#### EPI-OBJ-audit-report
Label: Source audit report

Source-native identity: SourceAuditReport / AuditContradictionsResult. Natural-language snippets and reason strings coexist with symbolic source paths, classifications, repair statuses and projection details. Substrate: request-local Go values/returned JSON; this report is not itself persisted by the inspected wrapper. No counterpart among supplied objects; context-pack output is a different consumer contract. SRC-1, `internal/runner/source_audit_report.go`, `internal/runner/audit_contradictions.go`.

> UnresolvedConflictGroups:  audit.UnresolvedConflictGroups,
> FailureClassification:     audit.FailureClassification,
> --- `internal/runner/source_audit_report.go`

#### EPI-OBJ-retrieval-eval
Label: Retrieval eval case

Source-native identity: RetrievalEvalCase and replay comparison fields. Symbolic query/filter/result identifiers plus numerical latency/overlap values; query text is retrieval input, not a gold answer. Storage substrate: local JSONL capture; replay report in returned JSON. Distinct from scenario evaluation in [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn); no supplied object counterpart. SRC-1, `internal/runner/retrieval_eval.go`.

> retrievalEvalAuthorityLimits      = "retrieval eval rows are regression evidence for ranking and latency changes only; canonical markdown, citations, provenance, projection freshness, and approved runner writes remain authority"
> --- `internal/runner/retrieval_eval.go`

### Routes

#### EPI-RTE-web-import
Label: Web source import

Endpoints/progression: downloaded bytes → extractWebSource → extractMarkdownSource or extractWebPage → attributed/hash-bearing source note → CreateDocument → indexed citation check. Owner: deterministic Go store; caller supplies URL/title, external source supplies assertions. Context/state/effect: selected download bytes, vault path and store; imports source text. Distinct from the generic write envelope [RT-RTE-document-write](runtime.md#rt-rte-document-write): this record assesses web extraction and its content lineage, not runner admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: source ingestion result with citations/hash/time, or error.
- Later read-back: created source note becomes available to later document/search/projection calls.
- Delegated visibility: source text enters local store; caller receives source metadata/citations, not proof of the assertions.
- Selection predicate: explicit URL and source-type/MIME dispatch; HTML removes hidden-element blocks/comments/tags and normalizes text; Markdown preserves body text apart from whitespace normalization.
- Invalidation or expiry: uninspected — source update/recovery bodies were not fully traced; import itself has no semantic expiry.
- Activation or effect: successful extraction supplies the body for a canonical source write; indexed citations are checked after creation.
- Evidence limits: implementation only; no network run, source authenticity, source truth or HTML semantic fidelity established.

The access/parse check target is supported source text, not assertion truth. Its errors can prevent this CreateDocument call; the post-create citation error is not a pre-write semantic veto. Open-request intake: caller proposes, code selects/rejects structure, host/user content approval is external. Recovery beyond generic [RT-RTE-document-write](runtime.md#rt-rte-document-write) remains uninspected. Operationally the source can influence later retrieval; epistemic source warrant is unknown.

Concrete implementation deduction: a Markdown body `# Policy\nKeep logs for seven days.` enters extractMarkdownSource unchanged except trimming/CRLF normalization, and is fenced in a source note with URL/hash. The propositions were imported, not invented or accepted as true. Conversely `<p>A</p><p>B</p>` loses its paragraph tags under HTML replacement; there is no universal claim of semantic preservation.

SRC-1, `internal/infra/sqlite/ingest_source.go`:

> text := strings.TrimSpace(strings.ReplaceAll(string(body), "\r\n", "\n"))
> --- `internal/infra/sqlite/ingest_source.go`

> withoutHidden := htmlScriptStylePattern.ReplaceAllString(raw, " ")
> withoutHidden = htmlCommentPattern.ReplaceAllString(withoutHidden, " ")
> --- `internal/infra/sqlite/ingest_source.go`

> text := htmlTagPattern.ReplaceAllString(withoutHidden, " ")
> text = cleanExtractedHTMLText(text)
> --- `internal/infra/sqlite/ingest_source.go`

> body := buildWebSourceNoteBody(sourceURL, sourcePath, title, shaHex, int64(len(download.Body)), download.MIMEType, capturedAt, extracted)
> --- `internal/infra/sqlite/ingest_source.go:311-311`

#### EPI-RTE-artifact-ocr
Label: Artifact OCR planning

Endpoints/progression: explicit artifact/local path and optional OCR review → installed/enabled/verified module and file checks → tesseract image process or PDF helper → nonempty text → candidate planner → body preview, extraction provenance and next request. Owner: Go admission/planning rules; external OCR executable produces transcription. State/effects: file bytes/hash and local module configuration; returned candidate, no durable candidate write. Distinct material extraction branch below [RT-RTE-session-plan](runtime.md#rt-rte-session-plan), which owns session orchestration rather than this document-level planner; direct document artifact_plan also reaches it.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ArtifactCandidatePlan with OCR review_required metadata/body preview, or extraction/configuration error.
- Later read-back: inapplicable — this planner does not persist the candidate; later use requires a separate write.
- Delegated visibility: selected file reaches a local OCR process; extracted text reaches planner and caller, not a provider model in this inspected image branch.
- Selection predicate: explicit OCR request/local path, tesseract provider, verified enabled module, supported file extension and size, nonempty extracted text.
- Invalidation or expiry: inapplicable — request-local candidate; changed input/module requires another planning call.
- Activation or effect: returns a reviewable candidate and metadata; image process runs with a timeout; no truth judgment or durable write is performed here.
- Evidence limits: no OCR execution/accuracy evidence; PDF helper and confidence/duplicate internals only partially inspected.

Open intake: caller requests the candidate; code can reject module/file/process/output conditions; human/agent decides the later create request. There is no reference transcription oracle. Module verification checks installed binding, not fidelity. Review_required is a warning and proposed workflow, not an authenticated review decision. The code-derived preview permits current-task host advice only, until a separately admitted write. No rollback is needed for candidate storage because none occurs; process-side effects are not audited here.

SRC-1, `internal/runner/artifact_candidate_plan.go`:

> if extracted == "" {
>     return nil, "", nil, domain.ValidationError("OCR review produced no extracted text", nil)
> }
> --- `internal/runner/artifact_candidate_plan.go`

> TextStatus:          "review_required",
> --- `internal/runner/artifact_candidate_plan.go`

> Warnings:            []string{"OCR text requires review before create_document or ingest_source_url approval"},
> --- `internal/runner/artifact_candidate_plan.go`

#### EPI-RTE-synthesis-build
Label: Synthesis body construction
Part of: [RT-RTE-document-write](runtime.md#rt-rte-document-write)

This is the compile branch's content-producing part of the supplied write container; it does not replace the container's gate findings. Endpoints: caller body/body_facts plus source_refs → source evidence lookup/role facts → strip/wrap/assemble content → generated synthesis body. Owner: deterministic Go code. Context: source documents and metadata, caller text/title/freshness note. Effect: body consumed by [EPI-RTE-synthesis-write](#epi-rte-synthesis-write).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: internal body string and source citations/role facts.
- Later read-back: body is later readable only if the write part persists it; this part does not independently store it.
- Delegated visibility: code reads referenced source metadata and a narrow summary prefix; caller body reaches the store unchanged in substance apart from assembly/added role facts.
- Selection predicate: nonempty Body takes priority over BodyFacts; presence of Sources/Freshness headings selects preservation versus wrapping; supersession metadata supplies role labels.
- Invalidation or expiry: no body-level support recheck; later projection freshness is a separate route.
- Activation or effect: produces the text passed into create/replace; no runtime model call or independent source-truth test in this inspected function chain.
- Evidence limits: string/metadata derivations are conditional on caller premises; unknown source truth and no execution evidence.

Concrete deduction: title `Policy`, body_facts `["Keep logs for seven days."]`, source_refs `["sources/policy.md"]`, and no role facts produce a Summary bullet containing precisely that caller sentence, a Sources bullet for the path and the default Freshness note. The function never compares the seven-day assertion with source prose. If the path is missing, compileSynthesisSourceEvidence appends a path-only citation and continues. Thus source_refs do not entail body support. Conversely, when supersession metadata exists, the function really does add source-role facts; it is not simply byte copying. A narrowly prefixed current-source Summary is rewritten as a revisit-decision label. These are conditional metadata/text derivations, not accepted new explanatory claims.

SRC-1, `internal/runner/compile_synthesis.go`:

> if !ok {
>     citations = append(citations, Citation{Path: ref})
>     continue
> }
> --- `internal/runner/compile_synthesis.go`

> return "Current compile_synthesis revisit decision: " + strings.TrimSpace(summary[len(revisitPrefix):])
> --- `internal/runner/compile_synthesis.go`

> freshnessNote = "Checked current source evidence through compile_synthesis."
> --- `internal/runner/compile_synthesis.go`

#### EPI-RTE-synthesis-write
Label: Synthesis target write
Part of: [RT-RTE-document-write](runtime.md#rt-rte-document-write)

Specific compile_synthesis create/update branch, not a new identity for all document writes. Endpoints: assembled body and inspected synthesis targets → count-based admission → CreateDocument or ReplaceDocument → projection/provenance inspection → handoff. Owner: Go runner/client/store; caller proposes title/path/content. Context: existing target matches and source_refs. Effects: canonical body and synchronized derived state.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: skipped duplicate target, created/updated result and handoff, or error.
- Later read-back: persisted synthesis may feed later document/retrieval/context requests.
- Delegated visibility: body crosses into store; caller gets selected path, citations, provenance/freshness and authority limits, not a verified proof of the Summary.
- Selection predicate: more than one matching target blocks; zero creates; one replaces that existing document.
- Invalidation or expiry: projection freshness can later invalidate derived currency; not a content TTL or deletion.
- Activation or effect: creates/replaces canonical synthesis; host effect unobserved.
- Evidence limits: target-selection guard is not epistemic acceptance; write precedes later report inspections, so a report error need not mean no write.

Open request mode, no factual answer oracle. Code decides target uniqueness/admission; caller controls content, and supplied [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary) supplies the external approval policy and weaker technical gate. Guidance limits synthesis to derived evidence. The block can be resolved by correcting duplicate targets and retrying. Automatic compensating rollback is not implemented in this compile function. Disposable validation uses the same compiler after checking vault basename/source marker; that is environment admission, not additional truth acceptance.

SRC-1, `internal/runner/compile_synthesis.go`:

> CandidateStatus:      "blocked_duplicate_target",
> DuplicateStatus:      "duplicate_target_path_detected",
> WriteStatus:          "skipped",
> --- `internal/runner/compile_synthesis.go`

> if len(matches) == 0 {
>     document, err = client.CreateDocument(ctx, domain.CreateDocumentInput{
> --- `internal/runner/compile_synthesis.go`

> return "canonical source documents and promoted records remain authority; synthesis is derived evidence with source refs, provenance, and projection freshness"
> --- `internal/runner/compile_synthesis.go`

#### EPI-RTE-synthesis-freshness
Label: Synthesis projection freshness

Endpoints: documents/source_refs/metadata/timestamps → buildSynthesisProjectionState → transactional projection replacement and provenance events → compile/audit reports. Owner: deterministic store code. Context: all loaded documents and prior projection versions. Effects: derived status and event, not source/body revision. No supplied route counterpart: [RT-RTE-document-write](runtime.md#rt-rte-document-write) mentions synchronization but does not individuate this check or its audit consumer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rebuild success/error; persisted ProjectionState has freshness and reason/current/superseded/missing/stale reference details.
- Later read-back: compile and audit calls read persisted projection state; audit uses current/superseded classes for repair.
- Delegated visibility: metadata and timestamps reach local code; callers receive derived fields, not independently checked source propositions.
- Selection predicate: synthesis path plus type; declared source_refs resolved against document paths.
- Invalidation or expiry: missing reference, newer source, superseded source lacking replacement, or replacement absent from source_refs yields stale; changed version creates refreshed/invalidated event.
- Activation or effect: writes derived check results used by later report/repair selection; no automatic source truth revision or synthesis deletion.
- Evidence limits: metadata-relative, no observed run; fresh does not mean supported or endorsed body.

Target/domain: reference currency in local stored metadata. No factual answer oracle. The result is entailed only under accurate path/time/metadata premises. Missing source_refs also yields stale; this is a concrete counterexample to relying on the compiler's generated fresh header. Derived checks do not supply an evidence-consuming acceptance criterion for a substantive Summary.

SRC-1, `internal/infra/sqlite/synthesis.go`:

> if source.UpdatedAt.After(input.Document.UpdatedAt) {
>     staleRefs = appendUnique(staleRefs, ref)
>     reasons = appendUnique(reasons, "source newer than synthesis")
> }
> --- `internal/infra/sqlite/synthesis.go`

> freshness := "fresh"
> if len(reasons) > 0 || len(missingRefs) > 0 || len(staleRefs) > 0 {
>     freshness = "stale"
> }
> --- `internal/infra/sqlite/synthesis.go`

#### EPI-RTE-audit-conflicts
Label: Audit unresolved conflicts

Endpoints: conflict_query → search snippets/citations → current source classification → auditClaimsDisagree → unresolved group → SourceAuditReport handoff. Owner: deterministic Go recognizer. State: search results and loaded source metadata; effect: reported discrepancy, no source winner. Distinct from [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), which supplies task context rather than this check; no supplied audit route counterpart.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: unresolved groups and provenance inspections, or none/error.
- Later read-back: inapplicable — groups are returned, not persisted by these functions.
- Delegated visibility: query-selected snippets, current paths and provenance summaries reach the report/handoff; source bodies inform status classification, not general semantic comparison.
- Selection predicate: at least two nonsuperseded source paths, plus multiple recognized number/day values among search snippets; supported numbers are one through ten and thirty, as words or digits.
- Invalidation or expiry: inapplicable — request-local search snapshot; a new query is needed after state changes.
- Activation or effect: source_audit_report includes conflict paths/claims and status; no enforcing winner/veto in the conflict check.
- Evidence limits: finite lexical heuristic, incomplete snippet coverage and no attribution of each numerical claim to a distinct same-subject proposition.

Target/domain: recognized retention-day quantities in query-selected snippet text. This is not a broad contradiction evaluator. Concrete deduction: snippets `Keep auth logs for seven days.` and `Keep billing logs for thirty days.` produce values 7 and 30; with two current source paths the code can report an unresolved disagreement despite compatible subjects. Conversely `Keep logs for 14 days.` and `Keep logs for 90 days.` produce no recognized values. Search-selected claims are collected before current-path filtering, further limiting their semantic relationship to the reported paths. There is no correct-answer oracle or human judgment in this check. The source_audit handoff includes conflict_claims, so the heuristic output reaches the host rather than stopping at an unused field. It runs after the possible repair, not as its precondition.

SRC-1, `internal/runner/audit_contradictions.go`:

> if len(currentPaths) < 2 {
>     return nil, inspections, nil
> }
> if !auditClaimsDisagree(claims) {
>     return nil, inspections, nil
> }
> --- `internal/runner/audit_contradictions.go`

> return len(retentionDays) > 1
> --- `internal/runner/audit_contradictions.go`

> case "30", "thirty":
>     return 30, true
> default:
>     return 0, false
> --- `internal/runner/audit_contradictions.go`

SRC-1, `internal/runner/source_audit_report.go`:

> "conflict_claims=" + strings.Join(conflictClaims, " | "),
> --- `internal/runner/source_audit_report.go`

#### EPI-RTE-audit-repair
Label: Source-sensitive summary repair

Endpoints: audit/source_audit request → existing synthesis target inspection → projection classes and source summaries → plan or ReplaceSection(Summary) → projection report/handoff. Owner: deterministic Go rules. Context: target, sorted current/superseded paths and source bodies. Effect: optional durable Summary change. No supplied counterpart; this retrieval-family mutation is additional to the generic document-family witness [RT-RTE-document-write](runtime.md#rt-rte-document-write), not a defect in its explicitly bounded coverage.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: planned, skipped missing/duplicate target, skipped insufficient classification, or applied, with report/handoff.
- Later read-back: changed canonical Summary can enter later retrieval and context packs.
- Delegated visibility: code reads source summaries; host receives report status, source paths, freshness and conflicts; later agents may retrieve replacement text.
- Selection predicate: exactly one target; repair mode rather than plan_only; at least one current and superseded path; nonempty Summary from the first current source in sorted projection-derived paths.
- Invalidation or expiry: later projection rebuilds can flag changed sources; no automatic semantic withdrawal of the copied Summary.
- Activation or effect: replaces an existing target Summary; later behavioral reliance unobserved.
- Evidence limits: metadata classification is not semantic adjudication; code may repair before conflict reporting; no general rollback receipt shown in this branch.

Admission: caller chooses target/query/mode; code can veto missing/duplicate target or insufficient classification. The runner's mutating retrieval path uses a write lock and approval-mode veto; this is not a separate authenticated human decision. Guidance is to preserve canonical source/supersession authority and not choose unresolved claims. No factual answer oracle. What persists is copied source Summary and role references, not criticism explaining why one substantive theory failed. Recovery requires explicit correction/replacement/replanning; the function provides no automatic undo. This is content-changing maintenance but not evidence-consuming epistemic acceptance or a demonstrated theory revision loop.

SRC-1, `internal/runner/audit_contradictions.go`:

> repaired, err := client.ReplaceSection(ctx, target.DocID, domain.ReplaceSectionInput{
>     Heading: "Summary",
>     Content: repairContent,
> })
> --- `internal/runner/audit_contradictions.go`

> "Current source summary: " + currentSummary,
> "Current source: " + currentSourcePaths[0],
> "Superseded source: " + supersededSourcePaths[0],
> "Audit repair did not choose unresolved claims beyond source classification.",
> --- `internal/runner/audit_contradictions.go`

SRC-1, `internal/runner/retrieval.go`:

> return (normalized.Action == RetrievalTaskActionAuditContradictions && normalized.Audit.Mode == "repair_existing") ||
>     (normalized.Action == RetrievalTaskActionSourceAuditReport && normalized.SourceAudit.Mode == "repair_existing")
> --- `internal/runner/retrieval.go`

> return "autonomy.approval_mode propose_only does not allow mutating retrieval actions"
> --- `internal/runner/retrieval.go`

#### EPI-RTE-eval-capture
Label: Retrieval eval capture

Endpoints: explicit search/semantic options → sanitized query and retrieval → result identity/timing/provider row → local JSONL → capture handoff. Owner: deterministic Go runner; caller opts in. Context/state/effects: query/filter, installed provider/corpus state and capture file; appends regression evidence only. Distinct from [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn), which invokes Codex and scenario verifiers rather than capturing retrieval identities.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: case, capture path, local_eval_artifact_appended status and replay advice, or error.
- Later read-back: explicit replay reads captured cases and reruns their query/action/filter settings.
- Delegated visibility: capture stores identifiers/paths and measurements, not document bodies/snippets; host gets case/report metadata.
- Selection predicate: explicit supported search action and capture path; runner write-mode checks apply to opt-in capture.
- Invalidation or expiry: uninspected — file helper integrity/retention policy not fully assessed; no automatic time expiry shown in inspected capture/replay bodies.
- Activation or effect: appends local regression baseline; no change to default ranking or canonical claims in this function.
- Evidence limits: no observed capture; sanitized query is the actual searched query; baseline correctness and causal relevance unestablished.

Admission: caller requests a baseline; code validates action/path and can reject; user approval is external policy. No gold relevance oracle. Open opt-in requests, not an automatic curriculum. Guidance explicitly restricts rows to ranking/latency regression evidence. What persists is JSONL. Recovery/deletion helpers unassessed; a failed capture cannot be assumed to undo provider/cache effects of preceding retrieval. No automatic successor-policy selector.

SRC-1, `internal/runner/retrieval_eval.go`:

> if err := appendRetrievalEvalCase(filepath.Dir(client.Paths().DatabasePath), capturePath, row); err != nil {
>     return RetrievalEvalCaptureReport{}, err
> }
> --- `internal/runner/retrieval_eval.go`

> FollowUpPrimitiveInspection: `run retrieval_eval_replay against the same capture_path after retrieval changes; use search or semantic_search directly for source-sensitive answers`,
> --- `internal/runner/retrieval_eval.go`

#### EPI-RTE-eval-replay
Label: Retrieval eval replay

Endpoints: captured cases → rerun selected search/semantic request → reference-set overlap/top1/latency comparison → aggregate report/handoff. Owner: Go evaluator, with embedding inference external when selected. Context: captured baseline plus current corpus/config/provider; no product mutation in inspected replay/report bodies. Distinct from [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn); linked consumer of [EPI-RTE-eval-capture](#epi-rte-eval-capture).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-case result identities, Jaccard/top1/status/latency, averages and handoff.
- Later read-back: inapplicable — replay report is returned, not persisted by this inspected function.
- Delegated visibility: current retrieval receives captured query/filters/provider/model label; host gets overlap metrics and advice, not relevance judgments or source bodies.
- Selection predicate: explicit capture path and bounded case limit; case action chooses lexical versus semantic replay.
- Invalidation or expiry: inapplicable — report is a current comparison; endpoint/corpus changes can alter its meaning and require contextual interpretation.
- Activation or effect: reports ranking stability/latency; advises inspecting low overlap/top1 mismatch before changing defaults, but does not change them itself.
- Evidence limits: implementation only; no independent intervention, immutable provider identity or reference relevance labels; latency and corpus drift confound broad attribution.

Check target/domain: equality/overlap of doc_id, chunk_id and path, plus observed-in-a-future-run timings. Baseline results are a reference outcome, not an answer oracle for factual truth or relevance. Open explicit regression mode. Code computes the metrics; caller decides any subsequent update. Both empty result sets receive Jaccard 1 and top1 match, a concrete reason not to read a perfect score as good retrieval. No implemented rejection, acceptance or policy adaptation follows the metric in this chain.

SRC-1, `internal/runner/retrieval_eval.go`:

> if len(union) == 0 {
>     return 1
> }
> --- `internal/runner/retrieval_eval.go`

> return ref.DocID + "\x00" + ref.ChunkID + "\x00" + ref.Path
> --- `internal/runner/retrieval_eval.go`

> FollowUpPrimitiveInspection: "inspect cases with low jaccard or top1 mismatch using search, semantic_search, provenance_events, and projection_states before changing defaults",
> --- `internal/runner/retrieval_eval.go`

### Claims

#### EPI-CLM-markdown-authority
Label: Canonical Markdown authority

Claimed operation: canonical Markdown remains authority; derived/optional recall layers and modules do not become truth. SRC-1, `README.md`, `docs/agent-contract.md`, doctrine/design. Distinct from [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary), which concerns permission rather than evidence hierarchy. Implementation provides source refs, canonical writes and explicit authority-limit handoffs; these do not enforce external model endorsement policy. No observed compliance claim.

> Canonical Markdown is authority.
> --- `docs/agent-contract.md`

> Optional modules can accelerate recall or extraction, but they do not become
> truth.
> --- `README.md`

#### EPI-CLM-source-repair
Label: Source-sensitive synthesis repair

Claimed operation: demo changes a source and reports stale synthesis with citations/repair request; source-audit design preserves supersession/freshness evidence and does not force unresolved conflicts to a winner. SRC-1, `README.md`, `internal/runner/source_audit_report.go`, doctrine/design text embedded in implementation. No supplied claim counterpart; [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary) concerns write consent, not source currency. Code supports metadata-relative checks and repair, not a general contradiction oracle or independently confirmed demo outcome.

> The demo creates an isolated sample vault, changes a source note, and reports
> stale synthesis with citations and a repair request.
> --- `README.md`

> return "canonical source documents and runner-visible supersession/freshness evidence remain authority; unresolved current-source conflicts are explained with source paths and are not forced to a winner"
> --- `internal/runner/source_audit_report.go`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; route declarations specify their consumers/channels/force/horizons, while [RT-BAP-skill-routing](runtime.md#rt-bap-skill-routing) owns the supplied instruction path.
