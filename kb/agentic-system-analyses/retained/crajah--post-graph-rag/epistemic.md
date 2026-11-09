---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "post-graph-rag epistemic routes: source assertions, structural admission, contradiction withdrawal, community reports and bounded benchmark judging."
run-id: AAS-2026-11-08-post-graph-rag-448d75e4222d-01
reviewed-boundary: "bce4146a7dc4684e9b66806915c29b0eed57ba23"
---

# post-graph-rag epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on imported assertions, extracted graph content, summaries and answers, and which checks actually change use. The scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is its [Source register](boundary.md#source-register), SRC-1. Python library entry points, not a package CLI, own the principal routes. Direct inspection of SRC-1 `pyproject.toml` and `post_graph_rag/__init__.py` found exported Python operations and no package CLI entry-point declaration there. The supplied runtime establishes model messages rather than registered native tools, host-process callback replacement, maintenance and release paths. Those findings are inputs, not an exhaustive independent tool audit.

Direct reads added extraction gates and prompts, contradiction candidate construction and consumers, relation upsert and provenance withdrawal, report rendering/flattening, query rendering/return metadata, community reranking, and three offline scorer implementations. All new findings below use implementation or embedded doctrine in SRC-1, not executed target behavior. No model request, database operation or test was run. Tracked result JSON, evaluation ablations and article tables were not assessed as run or causal evidence. Their availability is not an access gap. Provider internals, database contents and external benchmark reference provenance remain outside the frozen evidence; these prevent source-truth certification, deployed guarantees and independently authenticated performance.

The public warrant claims are [EPI-CLM-close-fact](#epi-clm-close-fact), [EPI-CLM-report-grounding](#epi-clm-report-grounding), [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates), [EPI-CLM-validity-effect](#epi-clm-validity-effect), and the supplied [RT-CLM-passage-priority](runtime.md#rt-clm-passage-priority). No single knowledge-production verdict follows from them.

| Entry point or operation | SRC-1 path | Coverage and records, or limit |
| --- | --- | --- |
| Package exports/configuration and caller injection | `post_graph_rag/__init__.py`, `pyproject.toml`; supplied `post_graph_rag/config.py` | Direct exports/metadata; [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension) covers callbacks and replacement; arbitrary callback semantics uninspected. |
| index_text/index_documents/index_document | `post_graph_rag/engine.py`, `post_graph_rag/extractor.py` | Supplied [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), plus direct [EPI-RTE-validation-check](#epi-rte-validation-check) and [EPI-RTE-contradiction-check](#epi-rte-contradiction-check). |
| Direct store upsert, supersession and source deletion | `post_graph_rag/graph_store.py` | Direct [EPI-RTE-relation-upsert](#epi-rte-relation-upsert), [EPI-RTE-supersession-write](#epi-rte-supersession-write), [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal). |
| build_communities and parent reports | `post_graph_rag/reporting.py`, `post_graph_rag/engine.py` | Direct renderer and supplied [RT-RTE-community-build](runtime.md#rt-rte-community-build); [EPI-RTE-community-render](#epi-rte-community-render). |
| query_data, query, bypass, streaming | `post_graph_rag/engine.py`, supplied `post_graph_rag/llm.py` | Direct render/return and rerank; supplied [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-direct-answer](runtime.md#rt-rte-direct-answer). |
| apply_retention/restore, telemetry, coverage, deltas | `post_graph_rag/retention.py`, `post_graph_rag/deltas.py`, `post_graph_rag/engine.py` | Supplied [RT-RTE-retention-control](runtime.md#rt-rte-retention-control). Delta/exploration arithmetic not independently assessed: prevents a complete account of every diagnostic proposition. |
| document_stats/document_graph/sweep_orphaned_relations | `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py` | Direct wrapper and deletion/dormancy reads; [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal). Detailed stat/graph SQL not audited; no complete diagnostic accuracy claim. |
| Shipped index/reload callers and examples | `demo_rag.py`, `examples/`, `evaluation/index_corpus.py`, `evaluation/analyse_graph.py`, `evaluation/ectqa/replay.py` | Supplied boundary/runtime coverage only; no independently observed caller episode. |
| Offline ECT-QA and LongMemEval scoring | `evaluation/ectqa/native_score.py`, `evaluation/ectqa/score.py`, `evaluation/longmemeval/regrade_official.py` | Direct [EPI-RTE-benchmark-check](#epi-rte-benchmark-check); this is not the complete evaluator family. |
| Other benchmark runners, blind judges, calibration, comparison and ablation | `evaluation/`, `tables/`, `docs/index.md` | Available but detailed mechanisms/results uninspected. Prevents evaluator-complete negatives, independent headline-rate verification and component attribution. |
| Tests, CI and publication | `tests/`, `.github/workflows/` | Supplied [RT-RTE-package-release](runtime.md#rt-rte-package-release); tests unexecuted/unassessed as correctness evidence. |

## Epistemic-object inventory

Each object owns its fields in the cited declaration; the inventory is a sparse index, not a second store of those fields.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-document](#epi-obj-document) | Source assertions | see record | SRC-1 `post_graph_rag/engine.py` | Source truth unknown |
| [EPI-OBJ-entity](#epi-obj-entity) | Names, identity and descriptions | see record | SRC-1 `post_graph_rag/extractor.py` | Alias equivalence unverified |
| [EPI-OBJ-triple](#epi-obj-triple) | Relation plus polarity and temporal scope | see record | SRC-1 `post_graph_rag/graph_store.py` | Upsert combines evidence fields |
| [EPI-OBJ-contradiction-result](#epi-obj-contradiction-result) | Offered-ID contradiction judgment | see record | SRC-1 `post_graph_rag/extractor.py` | Candidate projection may omit decisive detail |
| [EPI-OBJ-community-report](#epi-obj-community-report) | Summary/findings | see record | SRC-1 `post_graph_rag/reporting.py` | Faithfulness not established |
| [EPI-OBJ-community-rating](#epi-obj-community-rating) | Importance judgment, not a source-fact certificate | see record | SRC-1 `post_graph_rag/engine.py` | Ranking force distinct from summary |
| [EPI-OBJ-answer](#epi-obj-answer) | Answer propositions | see record | SRC-1 `post_graph_rag/engine.py` | No inspected query-time truth gate |
| [EPI-OBJ-grade](#epi-obj-grade) | Correctness/refusal estimates relative to gold | see record | SRC-1 `evaluation/ectqa/native_score.py` | Domain-specific proxy |
| [RT-OBJ-query-param](runtime.md#rt-obj-query-param) | see record | see record | SRC-1 `post_graph_rag/models.py` | History truth and authorship unresolved |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-local-embedding](runtime.md#rt-cmp-local-embedding) | No individually readable proposition established in dense vectors | see records | SRC-1 `post_graph_rag/llm.py` | Provider provenance and vector-space compatibility unresolved |

## Authority-route ledger

Architectural status refers to implemented pathways, not observed activation. “See” fields are owned by the cited records. A model transformation is indeterminate when the available implementation permits reshaping, entailed inference or unsupported additions without establishing which occurred. Requested groundedness alone establishes none of these semantic outcomes.

Route ID: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document](#epi-obj-document)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller text into passage store
Evaluator/condition and domain: Caller input, not truth evaluator
Activation and timing: Caller indexes a chunk
Possible or observed result: Passage and vector; source warrant unknown
Implemented force: Permissive import
Epistemic authority and scope: No source-truth license
Operational authority: behavior permitted, blocked, or changed: Stored source assertions available to later queries
Behavioral-authority path: consumer, channel, force, horizon: Store → retrieval → synthesis, evidential/advisory, later invocations
Evidence source ID and local anchor: SRC-1 `post_graph_rag/engine.py`
Claim IDs or none: [RT-CLM-passage-priority](runtime.md#rt-clm-passage-priority)
Mismatch marker or none: none
Gap/limit: See record; failures can occur before passage write.

Route ID: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity](#epi-obj-entity), [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Text/context to model extraction/gleaning
Evaluator/condition and domain: Prompt requests stated facts; model interpretation
Activation and timing: Default extraction; optional gleaning
Possible or observed result: Candidate structure
Implemented force: Proposal only, then gates
Epistemic authority and scope: Requested grounding; preservation/entailment unproved
Operational authority: behavior permitted, blocked, or changed: Candidates may enter graph without source-truth test
Behavioral-authority path: consumer, channel, force, horizon: Extraction → validation/writer, permissive after gates, later queries
Evidence source ID and local anchor: SRC-1 `post_graph_rag/extractor.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Alternatives: reshaping, derivation or conjecture; deciding requires input/output content and evidence.

Route ID: [EPI-RTE-validation-check](#epi-rte-validation-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: no content change
Transition or check target: Names/predicates/confidence/polarity gates
Evaluator/condition and domain: Deterministic configured rules over candidate fields
Activation and timing: On default validated branch
Possible or observed result: Filtered structure or ExtractionError
Implemented force: Enforcing only on invoking branches
Epistemic authority and scope: Conformity to rules, not truth
Operational authority: behavior permitted, blocked, or changed: Rejects nonconforming records from returned extraction
Behavioral-authority path: consumer, channel, force, horizon: _validate → extraction return → writer, enforcing, current admission
Evidence source ID and local anchor: SRC-1 `post_graph_rag/extractor.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Coercion, parsing and semantic truth are separate.

Route ID: [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity](#epi-obj-entity), [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: no content change
Transition or check target: External result admission
Evaluator/condition and domain: Caller configuration plus coercion/optional gates
Activation and timing: External replace or merge
Possible or observed result: Usable structured candidate accepted operationally
Implemented force: Permissive configurable admission
Epistemic authority and scope: No evidence-consuming truth acceptance established
Operational authority: behavior permitted, blocked, or changed: Can bypass default semantic gates
Behavioral-authority path: consumer, channel, force, horizon: Callback → extract_from_text → writer, permissive, persisted graph
Evidence source ID and local anchor: SRC-1 `post_graph_rag/extractor.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: See record; arbitrary injected extractor is opaque.

Route ID: [EPI-RTE-relation-upsert](#epi-rte-relation-upsert)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Repeated same-key assertions to one edge
Evaluator/condition and domain: Symbolic merge; source IDs/fields, no truth oracle
Activation and timing: Relation insertion/reobservation
Possible or observed result: Combined description/polarity/confidence/period/provenance
Implemented force: Enforcing payload replacement
Epistemic authority and scope: Provenance indicates assertions, not independent corroboration
Operational authority: behavior permitted, blocked, or changed: Retained edge used by retrieval/build
Behavioral-authority path: consumer, channel, force, horizon: Store edge → retrieval/build, permissive evidence, later invocations
Evidence source ID and local anchor: SRC-1 `post_graph_rag/graph_store.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Merge can change semantic scope; see counterexample in record. Not lifecycle integration after epistemic acceptance.

Route ID: [EPI-RTE-contradiction-check](#epi-rte-contradiction-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction-result](#epi-obj-contradiction-result)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Compatibility of new assertion and offered earlier assertions
Evaluator/condition and domain: Extraction model; same-subject limited candidates, projected descriptions/periods
Activation and timing: Enabled and declarative pass found no conflict
Possible or observed result: Offered IDs judged contradicted or empty list
Implemented force: Advisory judgment until write route
Epistemic authority and scope: Conditional incompatibility judgment; no independent source-truth test
Operational authority: behavior permitted, blocked, or changed: Supplies withdrawal IDs
Behavioral-authority path: consumer, channel, force, horizon: Model → offered-ID filter → mark_superseded, permissive decision input, current update
Evidence source ID and local anchor: SRC-1 `post_graph_rag/extractor.py`
Claim IDs or none: [EPI-CLM-close-fact](#epi-clm-close-fact)
Mismatch marker or none: none
Gap/limit: Prompt examples assume uniqueness; underlying assertions may be false.

Route ID: [EPI-RTE-supersession-write](#epi-rte-supersession-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: no content change
Transition or check target: Change reliance on earlier edge
Evaluator/condition and domain: Exclusive predicate groups/document order OR filtered model IDs
Activation and timing: After new relation write
Possible or observed result: superseded_by and t_expired set
Implemented force: Enforcing for default relation filter
Epistemic authority and scope: Operational retraction, not verification of successor
Operational authority: behavior permitted, blocked, or changed: Earlier relations withheld unless include_superseded; other channels unaffected
Behavioral-authority path: consumer, channel, force, horizon: Store flags → engine relation filter, enforcing, later queries
Evidence source ID and local anchor: SRC-1 `post_graph_rag/graph_store.py`
Claim IDs or none: [EPI-CLM-close-fact](#epi-clm-close-fact)
Mismatch marker or none: overbroad if read as every answer channel
Gap/limit: Failure retains new edge; no universal replay/historical-answer guarantee.

Route ID: [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: no content change
Transition or check target: Deleted chunk contributions and dormant relations
Evaluator/condition and domain: Source membership and endpoint liveness, not truth
Activation and timing: Deletion/replacement; repair sweep for endpoint orphans
Possible or observed result: Sources/weight updated, unsupported edges dormant
Implemented force: Enforcing in default relation consumers
Epistemic authority and scope: Loss of retained provenance, not falsification
Operational authority: behavior permitted, blocked, or changed: Withholds dormant relations by default; revival needs specific conditions
Behavioral-authority path: consumer, channel, force, horizon: Deletion → SQL payload → store read gates, enforcing, later invocations
Evidence source ID and local anchor: SRC-1 `post_graph_rag/graph_store.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No automatic community report rewrite; old source-less relations need bounded repair.

Route ID: [EPI-RTE-community-render](#epi-rte-community-render)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-triple](#epi-obj-triple)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Graph fields to report-model input
Evaluator/condition and domain: Deterministic projection/clipping
Activation and timing: Each report, including pseudo-graph of child reports
Possible or observed result: Names/types/descriptions, polarity/weight; dates not separately rendered
Implemented force: Enforcing input selection
Epistemic authority and scope: Degraded explicit temporal lineage; descriptions may retain dates
Operational authority: behavior permitted, blocked, or changed: Limits evidence available for report generation
Behavioral-authority path: consumer, channel, force, horizon: Renderer → community model user input, evidential, current report
Evidence source ID and local anchor: SRC-1 `post_graph_rag/reporting.py`
Claim IDs or none: [EPI-CLM-report-grounding](#epi-clm-report-grounding)
Mismatch marker or none: none
Gap/limit: Concrete date/polarity projection below; no execution needed.

Route ID: [RT-RTE-community-build](runtime.md#rt-rte-community-build)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-community-report](#epi-obj-community-report), [EPI-OBJ-community-rating](#epi-obj-community-rating)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Graph/child reports to summary/findings/rating
Evaluator/condition and domain: Community model instructed to ground every statement
Activation and timing: Caller build, optional hierarchy
Possible or observed result: Candidate report and importance rating
Implemented force: Proposal before parsing
Epistemic authority and scope: Grounding requested; not demonstrated
Operational authority: behavior permitted, blocked, or changed: Produces text eligible for storage and future ranking
Behavioral-authority path: consumer, channel, force, horizon: Community model → reporter, permissive, current build
Evidence source ID and local anchor: SRC-1 `post_graph_rag/reporting.py`
Claim IDs or none: [EPI-CLM-report-grounding](#epi-clm-report-grounding)
Mismatch marker or none: none
Gap/limit: No outputs inspected to distinguish faithful compression from additions.

Route ID: [RT-RTE-community-build](runtime.md#rt-rte-community-build)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-community-report](#epi-obj-community-report)
Content/update relation: no content change
Transition or check target: Report usability, not proposition truth
Evaluator/condition and domain: Parsing/type/nonempty summary
Activation and timing: After model return
Possible or observed result: Usable report or exception
Implemented force: Enforcing syntactic/usability gate
Epistemic authority and scope: Schema/nonempty only
Operational authority: behavior permitted, blocked, or changed: Bad parse/empty summary cannot proceed
Behavioral-authority path: consumer, channel, force, horizon: Reporter → engine, enforcing, current cluster
Evidence source ID and local anchor: SRC-1 `post_graph_rag/reporting.py`
Claim IDs or none: [EPI-CLM-report-grounding](#epi-clm-report-grounding)
Mismatch marker or none: none
Gap/limit: No ground-truth or entailment evaluator in this function.

Route ID: [RT-RTE-community-build](runtime.md#rt-rte-community-build)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-community-report](#epi-obj-community-report)
Content/update relation: no content change
Transition or check target: Admit usable report for answering
Evaluator/condition and domain: Engine persists returned report after embedding; cluster failures skipped per policy
Activation and timing: Caller-triggered rebuild
Possible or observed result: Stored report/membership, possibly partial build
Implemented force: Permissive operational admission
Epistemic authority and scope: No named evidence-consuming semantic acceptance decision
Operational authority: behavior permitted, blocked, or changed: Later queries and parent reports may rely on it
Behavioral-authority path: consumer, channel, force, horizon: Engine → store → parent/query, permissive, until rebuild
Evidence source ID and local anchor: SRC-1 `post_graph_rag/engine.py`
Claim IDs or none: [EPI-CLM-report-grounding](#epi-clm-report-grounding)
Mismatch marker or none: none
Gap/limit: Retention follows operational admission; lifecycle integration after epistemic acceptance unestablished.

Route ID: [RT-RTE-community-build](runtime.md#rt-rte-community-build)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-community-report](#epi-obj-community-report)
Content/update relation: no content change
Transition or check target: Report text, rating and membership stored
Evaluator/condition and domain: Store writes, not truth check
Activation and timing: Successful report embedding/write
Possible or observed result: Retained derived artifact
Implemented force: Enforcing storage policy
Epistemic authority and scope: Retention adds no warrant
Operational authority: behavior permitted, blocked, or changed: Feeds later global/hybrid queries
Behavioral-authority path: consumer, channel, force, horizon: Store → retrieval/model, evidential, subsequent queries/build levels
Evidence source ID and local anchor: SRC-1 `post_graph_rag/graph_store.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Old communities cleared before rebuild; staleness warns instead of rejecting.

Route ID: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document](#epi-obj-document), [EPI-OBJ-triple](#epi-obj-triple), [EPI-OBJ-community-report](#epi-obj-community-report)
Content/update relation: no content change
Transition or check target: Context selection/ranking/filtering
Evaluator/condition and domain: Fixed retrieval/fusion rules and auxiliary proposals
Activation and timing: Query mode and options
Possible or observed result: Selected context, not accepted truths
Implemented force: Ranking and relation-filter enforcement
Epistemic authority and scope: Relevance/temporal eligibility, not endorsement
Operational authority: behavior permitted, blocked, or changed: Selected text reaches synthesis/raw-context caller
Behavioral-authority path: consumer, channel, force, horizon: Store → engine → user message/caller, ranking/evidential, current query
Evidence source ID and local anchor: SRC-1 `post_graph_rag/engine.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Community importance is model-generated and affects score; temporal protections are channel-specific.

Route ID: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Retrieved fields to answer
Evaluator/condition and domain: Synthesis model instructed to use context/abstain
Activation and timing: Normal query; history may intervene
Possible or observed result: Answer or streamed deltas
Implemented force: Advisory output, no correctness veto
Epistemic authority and scope: No answer certification
Operational authority: behavior permitted, blocked, or changed: Caller receives answer; no automatic answer-store write
Behavioral-authority path: consumer, channel, force, horizon: Synthesis → return/stream, advisory, current answer
Evidence source ID and local anchor: SRC-1 `post_graph_rag/engine.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Returned retrieved_graph_triples omit polarity/period despite richer synthesis prompt.

Route ID: [RT-RTE-direct-answer](runtime.md#rt-rte-direct-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: History/question without corpus to answer
Evaluator/condition and domain: External model; no reference check
Activation and timing: Bypass
Possible or observed result: Direct answer/stream
Implemented force: Advisory
Epistemic authority and scope: No corpus-derived warrant
Operational authority: behavior permitted, blocked, or changed: Caller receives answer without retrieval
Behavioral-authority path: consumer, channel, force, horizon: Provider → caller, advisory, current answer
Evidence source ID and local anchor: SRC-1 `post_graph_rag/engine.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: See record; not evidence that every answer is grounded in this corpus.

Route ID: [RT-RTE-retention-control](runtime.md#rt-rte-retention-control)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity](#epi-obj-entity)
Content/update relation: non-truth-apt policy/content update: archive eligibility flags
Transition or check target: Exposure/age/degree to archive selection
Evaluator/condition and domain: Fixed scoring, caller threshold
Activation and timing: Telemetry enabled then caller retention non-dry-run
Possible or observed result: Changed entity seed/snapshot eligibility
Implemented force: Enforcing on named consumers
Epistemic authority and scope: Not correctness evaluation
Operational authority: behavior permitted, blocked, or changed: Archive/restore changes later selection
Behavioral-authority path: consumer, channel, force, horizon: Event stats → retention → entity search/snapshot, enforcing, subsequent queries
Evidence source ID and local anchor: SRC-1 `post_graph_rag/retention.py`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Trace-fed selection is not demonstrated learning or improved answers.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grade](#epi-obj-grade)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: ECT-QA stored answer elements against stored gold/temporal scope
Evaluator/condition and domain: Configured LLM with native element rubric; factual figures about 1% tolerance
Activation and timing: Native scorer, gold not unanswerable, parseable nonempty element list
Possible or observed result: correct/refusal/incorrect fractions, with failed cases excluded and reportable flag
Implemented force: Advisory benchmark reporting
Epistemic authority and scope: Model-relative reference agreement; no guarantee of full gold decomposition or exhaustive label validity
Operational authority: behavior permitted, blocked, or changed: Report rows/statistics, no inspected query veto or automatic product patch
Behavioral-authority path: consumer, channel, force, horizon: Scorer → JSON/console → operator, advisory, offline comparison
Evidence source ID and local anchor: SRC-1 `evaluation/ectqa/native_score.py`
Claim IDs or none: [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates)
Mismatch marker or none: protocol and comparison limits
Gap/limit: Native protocol differs from paper rubric/model; grade label vocabulary not enforced. No observed execution or causal component support assessed.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grade](#epi-obj-grade)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: ECT-QA gold=unanswerable prediction refusal
Evaluator/condition and domain: Deterministic lexical markers in entire lowercased answer
Activation and timing: Native scorer special branch, before model call
Possible or observed result: One correct or incorrect element, refusal fraction zero
Implemented force: Advisory benchmark reporting
Epistemic authority and scope: Lexical refusal recognition only, not proof of justified abstention
Operational authority: behavior permitted, blocked, or changed: Report rows/statistics, no inspected query veto or automatic product patch
Behavioral-authority path: consumer, channel, force, horizon: Scorer → JSON/console → operator, advisory, offline comparison
Evidence source ID and local anchor: SRC-1 `evaluation/ectqa/native_score.py`
Claim IDs or none: [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates)
Mismatch marker or none: protocol and comparison limits
Gap/limit: A marker can appear without genuine refusal; no semantic evaluator in this branch. No observed execution or causal component support assessed.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grade](#epi-obj-grade)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: ECT-QA answer figures or periods relative to gold
Evaluator/condition and domain: numeric_f1 else period_f1, threshold default 0.60
Activation and timing: Strict scorer, gold answerable and an F1 proxy available
Possible or observed result: Boolean correct plus refusal label; numeric score retained
Implemented force: Advisory benchmark reporting
Epistemic authority and scope: Proxy figure/period overlap; referent and broader factual support not established
Operational authority: behavior permitted, blocked, or changed: Report rows/statistics, no inspected query veto or automatic product patch
Behavioral-authority path: consumer, channel, force, horizon: Scorer → JSON/console → operator, advisory, offline comparison
Evidence source ID and local anchor: SRC-1 `evaluation/ectqa/score.py`
Claim IDs or none: [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates)
Mismatch marker or none: protocol and comparison limits
Gap/limit: Underlying imported numeric/period metric helpers not fully inspected; prevents a complete metric-validity conclusion. No observed execution or causal component support assessed.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grade](#epi-obj-grade)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: ECT-QA narrative answer relative to gold
Evaluator/condition and domain: Embedding cosine, threshold default 0.62
Activation and timing: Strict scorer only when numeric and period F1 unavailable
Possible or observed result: Similarity score and boolean correct
Implemented force: Advisory benchmark reporting
Epistemic authority and scope: Embedding similarity, not entailment; provider geometry uninspected
Operational authority: behavior permitted, blocked, or changed: Report rows/statistics, no inspected query veto or automatic product patch
Behavioral-authority path: consumer, channel, force, horizon: Scorer → JSON/console → operator, advisory, offline comparison
Evidence source ID and local anchor: SRC-1 `evaluation/ectqa/score.py`
Claim IDs or none: [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates)
Mismatch marker or none: protocol and comparison limits
Gap/limit: Versioned provider vectors and threshold calibration not assessed. No observed execution or causal component support assessed.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grade](#epi-obj-grade)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: ECT-QA refusal identification
Evaluator/condition and domain: Deterministic startswith unanswerable within normalized first 60 characters
Activation and timing: Strict scorer; also determines correctness for gold=unanswerable
Possible or observed result: Boolean refusal, and correct for unanswerable cases
Implemented force: Advisory benchmark reporting
Epistemic authority and scope: Literal prefix conformance only
Operational authority: behavior permitted, blocked, or changed: Report rows/statistics, no inspected query veto or automatic product patch
Behavioral-authority path: consumer, channel, force, horizon: Scorer → JSON/console → operator, advisory, offline comparison
Evidence source ID and local anchor: SRC-1 `evaluation/ectqa/score.py`
Claim IDs or none: [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates)
Mismatch marker or none: protocol and comparison limits
Gap/limit: Different from native scorer's multi-marker rule. No observed execution or causal component support assessed.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grade](#epi-obj-grade)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: LongMemEval stored answer relative to supplied gold/type rubric
Evaluator/condition and domain: Configured judge, default gpt-4o; substring yes parser
Activation and timing: Regrade caller-selected arms, first repeat by default; type and _abs select prompt
Possible or observed result: Boolean labels and first-repeat per-type/overall aggregates; grader failure is non-yes
Implemented force: Advisory benchmark reporting
Epistemic authority and scope: Agreement under requested type rubric and substring parsing, not source truth
Operational authority: behavior permitted, blocked, or changed: Report rows/statistics, no inspected query veto or automatic product patch
Behavioral-authority path: consumer, channel, force, horizon: Scorer → JSON/console → operator, advisory, offline comparison
Evidence source ID and local anchor: SRC-1 `evaluation/longmemeval/regrade_official.py`
Claim IDs or none: [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates)
Mismatch marker or none: protocol and comparison limits
Gap/limit: Can accept a reply containing yes beyond an exact yes token; observed error rate unknown. No observed execution or causal component support assessed.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-close-fact](#epi-clm-close-fact) | see record | SRC-1 `README.md`, doctrine/design | Explicit later-fact closure | [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-supersession-write](#epi-rte-supersession-write) | Unassessed | No intervention evidence assessed; model error and candidate coverage remain | Later assertions can suppress earlier relation edges | “Stops reporting” is not universal: passages, entity descriptions and stale reports can still carry old assertions. |
| [EPI-CLM-report-grounding](#epi-clm-report-grounding) | see record | SRC-1 `post_graph_rag/reporting.py`, embedded doctrine | Explicit no-outside-knowledge rule | [EPI-RTE-community-render](#epi-rte-community-render), [RT-RTE-community-build](runtime.md#rt-rte-community-build) | Unassessed | No faithfulness experiment assessed; temporal fields dropped from structured rendering | Requested grounded summary admitted after usability checks | Grounding instruction is not semantic verification. |
| [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates) | see record | SRC-1 `README.md`, reported operation | Named benchmark protocols and caveats | [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) covers selected scorers, not headline reproduction | Tracked results unassessed | Different generations/judges/corpus slices; no independent component variation established | Repository reports strong task scores and ships checks | Neither those rates nor cross-system superiority independently verified here. |
| [EPI-CLM-validity-effect](#epi-clm-validity-effect) | see record | SRC-1 `README.md`, reported operation | Explicit effect attribution | [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) plus direct renderer read | Ablation artifacts unassessed | Implementation shows added dates, not +38-point causal effect; comparison design unassessed | Rendering can expose dates to synthesis | Component effect remains unestablished, not refuted. |
| [RT-CLM-passage-priority](runtime.md#rt-clm-passage-priority) | see record | SRC-1 `post_graph_rag/engine.py`, doctrine/design | see record | [RT-RTE-document-admission](runtime.md#rt-rte-document-admission) | Unassessed | No crash/recovery experiment; pre-insertion failures and replacement deletion limit guarantee | Best-effort preservation after passage insertion | Not atomic admission or unconditional recoverability. |

## Bounded conclusion

The inspected system acquires assertions by importing caller documents, then requests model extraction into localized graph records. Passage retention preserves an opportunity to inspect source text, but does not establish the truth of that text. Model extraction, alias resolution, predicate snapping, report generation and answer synthesis do not come with a checked interpretation proving semantic preservation or entailment. Their relation is indeterminate, not automatically ampliative conjecture merely because the model generated text. No warranted-premise derivation is established by the inspected pathways. See [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), [EPI-OBJ-entity](#epi-obj-entity), [EPI-OBJ-triple](#epi-obj-triple).

The default extraction gate checks candidate fields against configurable rules. It licenses rule conformity, not source truth; the external replacement path can bypass those rules. Operational graph admission and report usability admission are consequential even without evidence-consuming semantic acceptance. Retention, graph membership and later retrieval therefore do not establish lifecycle integration of accepted ampliative knowledge. This is a bounded conclusion about the inspected routes, not an evaluator-complete negative: uninspected evaluation families and custom callbacks remain explicit in coverage. See [EPI-RTE-validation-check](#epi-rte-validation-check), [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension), [RT-RTE-community-build](runtime.md#rt-rte-community-build).

Contradiction judging is a genuine content-sensitive check with a consequential withdrawal consumer. It is not merely unused criticism. Its target is the compatibility of a newly supplied assertion with a bounded same-subject candidate list, not whether the new assertion is true. Deterministic exclusive groups instead encode an incompatibility premise and let document order decide. Both can change later relation reliance, without certifying the successor. Default filtering gives stored withdrawal flags operational force. Document deletion also withdraws provenance and can retire relations without judging them false; revival and source-less repair have separate rules. These paths qualify the broad public “stops reporting” claim because unfiltered source passages/descriptions/reports can still carry a withdrawn assertion. See [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-supersession-write](#epi-rte-supersession-write), [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal).

Community reports are retained generated content, admitted by parsing/nonempty-summary checks, then consumed by parent reporting and global/hybrid answering. Their generated importance rating has separate symbolic ranking force. Rendering can discard explicit time bounds before reporting, and report staleness warns rather than forbids use. Neither groundedness nor freshness is independently proven. The answer prompt preserves relation polarity and optionally periods, while the terminal answer dictionary's abbreviated triple strings omit them; a downstream caller must not treat those strings as the complete scoped claims. The context-only API is a countercase: it returns structured retrieval instead of those abbreviated strings. See [EPI-RTE-community-render](#epi-rte-community-render), [EPI-OBJ-community-rating](#epi-obj-community-rating), [EPI-OBJ-answer](#epi-obj-answer), [RT-BAP-answer-context](runtime.md#rt-bap-answer-context).

Offline scorers do consume reference answers and produce operational benchmark labels; they are not the query's truth gate. Each licenses only protocol-relative agreement over its benchmark domain. Element decomposition, tolerance rules, lexical refusal detection, grader errors and denominator exclusions matter. Source reports and stored artifacts do not by themselves identify a component effect or establish external comparison validity. See [EPI-RTE-benchmark-check](#epi-rte-benchmark-check), [EPI-CLM-benchmark-rates](#epi-clm-benchmark-rates), [EPI-CLM-validity-effect](#epi-clm-validity-effect).

Retention scoring provides direct exposure-fed behavioral adaptation through archive flags, not a proposition-truth check. Improved future capacity, reliable reflection, a theory-builder loop and exercised self-improvement do not follow from it. The model components are externally parameterized and unpinned as recorded in runtime; the inspected repository calls do not train them, and opaque provider state does not establish absence of other learning. Content-sensitive contradiction withdrawal is independently supported regardless of these unresolved properties. No single system-wide epistemic or autonomy score is assigned. See [RT-RTE-retention-control](runtime.md#rt-rte-retention-control), [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-community-model](runtime.md#rt-cmp-community-model), [RT-CMP-synthesis-model](runtime.md#rt-cmp-synthesis-model).

## Shared records

### Operative objects

#### EPI-OBJ-document
Label: Document passage

Caller text is natural-language truth-apt assertions stored as document content plus symbolic metadata in PostgreSQL through the store. Embedding is a separate numerical retrieval representation. No counterpart object is declared in the supplied runtime; this is the passage consumed along its document-admission route, not the query configuration object. SRC-1 `post_graph_rag/engine.py`.

> doc_vertex = await self.store.add_document(
>             prepared["text"], prepared["doc_emb"], stamped, space=target_space
>         )
> --- `post_graph_rag/engine.py`

#### EPI-OBJ-entity
Label: Entity

Natural-language canonical name, aliases and description, with symbolic type/identity fields, stored in an entity vertex. Extraction requests canonicalization and source-local descriptions, not externally checked identity resolution. Alias/name matching can conflate or split actual referents. No counterpart object in supplied runtime; distinct from RT-OBJ-query-param and model components; related route is [RT-RTE-document-admission](runtime.md#rt-rte-document-admission). SRC-1 `post_graph_rag/extractor.py`.

> - Description: Brief summary of the entity's role in THIS text.
> --- `post_graph_rag/extractor.py`

#### EPI-OBJ-triple
Label: Relation edge

Natural-language descriptions/name semantics and symbolic relation label, endpoint IDs, polarity, confidence, dates, source IDs and timestamps in a database edge payload. Truth scope depends on these fields together. No counterpart object in supplied runtime; the document-admission route writes it. Weight counts source chunks when provenance is supplied, otherwise observations; neither is independent-source validation. See [EPI-RTE-relation-upsert](#epi-rte-relation-upsert). SRC-1 `post_graph_rag/graph_store.py`.

> "negated": bool(negated),
>             "confidence": float(confidence),
> --- `post_graph_rag/graph_store.py`

#### EPI-OBJ-contradiction-result
Label: ContradictionResultSchema

Symbolic list of IDs in process memory expresses the model's truth-apt judgment that the offered earlier assertions cannot coexist with the new assertion. It is transient but changes durable withdrawal flags. No counterpart object in supplied runtime; related document admission container includes this distinct judgment before the store disposition. SRC-1 `post_graph_rag/extractor.py`.

> return [str(i) for i in ids if str(i) in offered]
> --- `post_graph_rag/extractor.py`

#### EPI-OBJ-community-report
Label: CommunityReport text

Natural-language title, summary and findings, stored with community membership in database vertices; process-local Pydantic object before storage. Distinct from the separately consumed rating part. No counterpart object in supplied runtime; related [RT-RTE-community-build](runtime.md#rt-rte-community-build) is a route, not this artifact. Its content is requested to be source-grounded but not checked for source entailment. SRC-1 `post_graph_rag/reporting.py`.

> class Finding(BaseModel):
>     summary: str = Field(..., description="Short headline for this finding")
>     explanation: str = Field(..., description="Supporting explanation grounded in the listed entities and relations")
> --- `post_graph_rag/reporting.py`

#### EPI-OBJ-community-rating
Label: CommunityReport rating

Symbolic numeric importance judgment in process and community database payload, consumed by fixed ranking rules; not a distributed-parametric representation. It is a material part of the community-build output distinct from the report's natural-language findings. No supplied object counterpart. Its claimed importance is subjective to corpus understanding, not a source-fact reliability score. SRC-1 `post_graph_rag/engine.py`.

> importance = min(max(c["rating"], 0.0), 10.0) / 10.0
> --- `post_graph_rag/engine.py`

#### EPI-OBJ-answer
Label: Answer and retrieval metadata

Natural-language model answer returned in a Python dictionary or stream, not automatically retained as an answer store. Returned retrieval metadata is symbolic/textual process data. No counterpart object in runtime: related question-answer/direct-answer routes produce it; caller history is separately [RT-OBJ-query-param](runtime.md#rt-obj-query-param). A concrete implemented projection: a retrieved relationship with negated=true and valid_from=2020 reaches the synthesis prompt with NOT and (when enabled) a from-date. The terminal dictionary instead emits only endpoints/relation_type, so opposite-polarity or differently scoped inputs can have the same abbreviated triple string. This does not prove the generated answer is wrong; it limits consumers of that field. SRC-1 `post_graph_rag/engine.py`.

> "retrieved_graph_triples": [
>                 f"({r['src_id']}) --[{r['relation_type']}]--> ({r['tgt_id']})"
>                 for r in data["relationships"]
>             ],
> --- `post_graph_rag/engine.py`

#### EPI-OBJ-grade
Label: Benchmark grade

Symbolic booleans/rates and model-produced element labels in JSON/console outputs; explanatory gold/prediction text is natural language. Grades claim protocol-relative answer correctness, not universal truth. No counterpart object in supplied runtime; separate offline consumer from the production query route. Parameter versions of grading providers are not pinned by a name string; no parameter update is made by the inspected scoring calls, and provider internals remain uninspected. SRC-1 `evaluation/ectqa/native_score.py`.

> c = collections.Counter(e.verdict.strip().lower() for e in els)
>             n = len(els)
> --- `evaluation/ectqa/native_score.py`

### Routes

#### EPI-RTE-validation-check
Label: Extraction validation check

Part of: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

GraphExtractor._validate takes structured model candidates and returns filtered/canonicalized entities/triples or raises. Python owns the check; the model supplied the confidence, not measured correctness. Default model extraction invokes it; external validation is optional. The target/domain is candidate name/predicate shape, self-reference, configured confidence/polarity and date cleanliness, not correspondence with external reality. Literal transformation witness from inspected code: normalise_predicate('was_appointed_knight_of') lowercases/joins, then removes the was_ prefix, producing appointed_knight_of. This is intended label normalization, not a checked theorem about tense/meaning. Configured alias and morphological snapping can change predicate interpretation, so a universal semantic-preservation classification is unwarranted. Rule evaluation and downstream writer admission are separate functions. Caller chooses configuration; software vetoes candidate records; no expected-answer oracle or bounded experimental curriculum. Changes to gates affect future ingestion; recovery of earlier results requires re-indexing, not a gate rollback. SRC-1 `post_graph_rag/extractor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Filtered ExtractionResult or ExtractionError.
- Later read-back: Returned candidates can be retained by document admission and consumed later.
- Delegated visibility: inapplicable — local check, not agent delegation.
- Selection predicate: All invoking branches; candidate-specific gates.
- Invalidation or expiry: inapplicable — check result has no separate cache; retained graph lifecycle is downstream.
- Activation or effect: Deterministic drop/canonicalization of candidate fields; no observed factual benefit.
- Evidence limits: External bypass and injected extractors prevent universal gate claims.

> if t.confidence < self.min_confidence:
>                 continue
>             if t.negated and self.drop_negated:
>                 continue
> --- `post_graph_rag/extractor.py`

#### EPI-RTE-relation-upsert
Label: Relation payload merge

Part of: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

Store.add_relation receives an edge proposal and either inserts it or merges it into the edge found by subject/predicate/object identity. Python/store owns progression and writes. The source document or extractor proposes assertions; software admits them, with no truth oracle or per-edge human veto. This subroute differs from the whole document-admission container by its same-key payload merge semantics; direct store callers also reach this function. Ingestion order and provenance are policy inputs, not adjudication of claim truth. A concrete inspected-code deduction: prior negated=True plus incoming negated=False produces False via boolean AND; confidence takes max, description takes the new nonempty string, each date takes the incoming nonempty value or prior value. Consequently a repeated edge can mix provenance/period/description from distinct assertions without a conflict trial. Same endpoint/predicate matching does not distinguish opposite polarities or two periods. Source count is distinct chunk count when IDs are available, not evidence of independent testimony. A provenance-bearing assertion revives dormant edges; existing supersession pointers are preserved. No semantic rollback history of merged descriptions is implemented in this function. SRC-1 `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Inserted/upserted Edge.
- Later read-back: Persisted payload reaches query_data, graph_snapshot and reports.
- Delegated visibility: inapplicable — store writes, no agent delegation.
- Selection predicate: Same subject/predicate/object key; direct callers may omit provenance.
- Invalidation or expiry: Sources withdrawn on document deletion; source-backed reassertion can clear dormancy, but preserves supersession fields.
- Activation or effect: Combines fields and replaces payload; weight/confidence/polarity can alter reliance cues.
- Evidence limits: No observed merge episode or guarantee about dependency concurrency.

> "negated": bool(prev.get("negated", False)) and negated,
>                 "confidence": max(float(prev.get("confidence", 0.0)), float(confidence)),
> --- `post_graph_rag/graph_store.py`

#### EPI-RTE-contradiction-check
Label: Model contradiction judgment

Part of: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

After new-edge insertion, engine requests same-subject current candidates and calls detect_contradictions when configured and the declarative pass returned none. Candidates are newest-first and limited; their model projection includes ID, description or predicate and available validity periods. The new assertion contains endpoint names/predicate/description but does not explicitly append its separate validity fields. Candidate object endpoints and polarity are not separately rendered either. A rich description can supply those facts, so omission is a risk, not proof of every judgment being defective. The extraction model proposes incompatibilities under the supplied same-time rule; Python filters IDs to those offered. This is a check, distinct from the store's retraction decision. Model uncertainty/failure returns no IDs. No independent oracle checks either assertion's truth. Caller config enables the route; no per-judgment human approval. The fixed prompt requests conservative decisions, but does not establish actual conservatism. Judgments can result in changed reliance without changing the original assertion text; this is a real content-sensitive criticism affordance/wiring, not evidence of an iterative theory-builder practice. SRC-1 `post_graph_rag/extractor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of offered candidate IDs, or empty on failure/no candidates.
- Later read-back: inapplicable — judgment object itself is not persisted; resulting edge flags have a later consumer in the disposition route.
- Delegated visibility: Selected new/candidate facts go to extraction provider, not an independent agent loop.
- Selection predicate: Enabled config, no declarative conflict, same-subject current candidate cap.
- Invalidation or expiry: inapplicable — no judgment cache/expiry; stored flags have separate lifecycle.
- Activation or effect: Returned IDs feed mark_superseded; no operation trace assessed.
- Evidence limits: Projection, candidate cap, missing new validity rendering and provider accuracy bound the check.

> except Exception as e:
>             logger.warning("Contradiction detection failed (%s); retracting nothing.", e)
>             return []
> --- `post_graph_rag/extractor.py`

#### EPI-RTE-supersession-write
Label: Supersession disposition

Part of: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

Two implemented inputs reach withdrawal writes: configured exclusive predicate groups over the same subject/object pair, or IDs from the model contradiction check. Declarative software selects conflicting predicates and gives the newer indexed assertion precedence; it does not compare source quality or dates. The model branch has already filtered IDs. The store records superseded_by and t_expired; engine._filter_temporal then excludes those relations unless include_superseded is enabled. Owner is Python/store; no additional human veto or expected-answer oracle, and no evidence-consuming decision that verifies the successor. This is operational retraction, not lifecycle integration of an accepted new explanation. The target/domain differs by branch: declared predicate incompatibility for the fixed pair versus model-selected offered assertions. Recovery includes opt-in retrieval of superseded edges; pointer/history preservation is not an automatic rollback decision. New relation insertion precedes this enrichment and survives errors. SRC-1 `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: IDs marked superseded, returned to engine count.
- Later read-back: Default relation filtering reads stored flags on later queries.
- Delegated visibility: inapplicable — store disposition has no agent delegation.
- Selection predicate: Exclusive groups then optional model IDs; new relation already exists.
- Invalidation or expiry: Flags persist; include_superseded controls retrieval, not deletion of history.
- Activation or effect: Earlier relation reliance changes in named filtered channels; source passages/reports need not change.
- Evidence limits: No guarantee of true successor, all-channel retraction or historical snapshot reproducibility.

> if payload.get("superseded_by"):
>                 continue
>             payload["superseded_by"] = str(new_edge_id)
>             payload["t_expired"] = _utc_now()
> --- `post_graph_rag/graph_store.py`

#### EPI-RTE-source-withdrawal
Label: Source withdrawal and dormancy

Part of: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

Deletion/replacement calls delete_document_chunks, removes mentions/documents, withdraws chunk IDs from relation sources and recomputes weight. It then refreshes entity dormancy and endpoint-orphaned relations. This is the replacement/deletion subroute of document admission, distinct from epistemic contradiction. Owner is store code, triggered by caller replacement/deletion or explicit repair. A relation with no remaining contributing chunks becomes dormant; this says its retained documentary support was removed, not that the assertion was false. Remaining source IDs can clear dormancy in the withdrawal SQL. Endpoint-only orphan revival is separate: explicit source-withdrawal dormancy does not revive solely because an endpoint returns. add_relation with a new source assertion can revive it. Legacy source-less relations require endpoint-orphan repair; sweep_orphaned_relations cannot prove which document asserted them. Dormant relation gates are defaulted in store reads, but reports already built are not rewritten here. No answer oracle or content-truth acceptance, and no per-edge human decision. Re-index/repair is recovery, not an atomic rollback of old content. SRC-1 `post_graph_rag/graph_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deletion counts and dormant/withdrawn counts.
- Later read-back: Source lists/weights/dormancy flags reach later relation reads and graph snapshots.
- Delegated visibility: inapplicable — local/database lifecycle code.
- Selection predicate: Contributing chunk IDs; endpoint liveness for orphan sweep.
- Invalidation or expiry: Document reassertion can revive source-withdrawn edges; endpoint-only revival has narrower reason handling.
- Activation or effect: Default reads withhold dormant relations; no guarantee of changed answers across every channel.
- Evidence limits: Direct source reading supports wiring, not observed deletion correctness or dependency atomicity.

> A relation left with no contributing chunk is marked dormant rather than
>         deleted, matching how orphaned entities are handled: the assertion was
>         genuinely made once, and the audit trail is meant to keep it.
> --- `post_graph_rag/graph_store.py`

#### EPI-RTE-community-render
Label: Community evidence projection

Part of: [RT-RTE-community-build](runtime.md#rt-rte-community-build)

render_community projects graph members into one prompt string. It keeps at most 60 entity and 80 relation lines by default and clips each line to 400 characters. This is a material subroute of community build, not a duplicate of the whole build. Concrete deterministic witness, deduced without target execution: a relation {src:A, tgt:B, predicate:works_at, negated:true, valid_from:2020, valid_to:2021, weight:1, description:''} renders the line '- (A) --[NOT works_at]--> (B) (weight=1): '. Changing only its valid_from/valid_to yields the same line because the function never reads them. Thus polarity survives but separate period fields do not, unless descriptions repeat them. This prevents a general scope-preserving reshaping conclusion; relation content/update classification remains indeterminate rather than proved ampliative. For parents, summarise_reports creates pseudo-entities and includes-relations from child report summaries/findings/ratings; these again pass through the same renderer, not original source documents. Python controls projection; model receives only rendered fields. This is evidence selection, not an evaluator of truth. SRC-1 `post_graph_rag/reporting.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Prompt-body string.
- Later read-back: inapplicable — renderer output is current model input, not a separately retained cache; generated reports are retained downstream.
- Delegated visibility: Body delivered to community model endpoint.
- Selection predicate: Fixed prefix slices and line clipping; parent inputs are child-report projections.
- Invalidation or expiry: inapplicable — transient prompt string, no expiry mechanism.
- Activation or effect: Determines what evidence reporting model can see; semantic fidelity remains unobserved.
- Evidence limits: Short descriptions may retain dates, but separate dates/source lineage are not rendered.

> neg = "NOT " if r.get("negated") else ""
>         weight = r.get("weight", 1)
>         desc = (r.get("description") or "")
> --- `post_graph_rag/reporting.py`

#### EPI-RTE-benchmark-check
Label: Offline benchmark checks

Distinct from supplied runtime question-answer routes: selected offline scorers read already stored predictions and gold, compute judgments, persist labels/aggregates and print summaries. No supplied route counterpart; package-release is a different consumer/admission mechanism. Target/domain one: ECT-QA earnings-call answer elements relative to stored gold and requested temporal scope, judged by a configurable model rubric. It admits successfully parsed nonempty element sets to the scored denominator; exceptions or no elements go to failed. Verdict is a free string, so unrecognized labels still increase n without contributing to the three named counters; sums-to-one is requested, not enforced for all strings. A special unanswerable branch uses lexical refusal markers instead of the model. reportable is not failed, an advisory flag in saved JSON, not a prevention of file creation. Target/domain two: the strict ECT-QA scorer's numeric/period F1 (default 0.60) or embedding cosine (0.62) plus refusal rule. These are proxy matches against gold; numeric agreement alone does not prove correct referent or period attribution. Target/domain three: LongMemEval regrading uses question-type/abstention rubrics and supplied gold, default gpt-4o, tests substring yes, and writes per-arm rates; a final grader exception becomes non-yes rather than a separate excluded case. All are reference-consuming checks, but references and model compliance are not independently validated here. Native rubric admits element-wise agreement (about 1% figures); its same-family default judge and nonverbatim rubric explicitly limit comparison. The reference oracle is stored gold supplied by input files, not the production graph. Caller chooses scorer/model/files; software/model decide labels, no human per-case veto. Operating mode is offline bounded benchmark scoring, not open query admission. No automatic parameter/configuration/product update consumer was found in these three inspected scorer files; broader evaluator/maintainer adoption remains uninspected. SRC-1 `evaluation/ectqa/native_score.py`, `evaluation/ectqa/score.py`, `evaluation/longmemeval/regrade_official.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON/console labels, counts and rates.
- Later read-back: Saved score files can be read externally; no inspected automatic query/product admission read-back in these scorer files.
- Delegated visibility: Gold/question/prediction text sent to configured judge or embedding endpoint.
- Selection predicate: Caller result file and arms/repeats; native failures excluded with reportable flag, regrade defaults first repeat.
- Invalidation or expiry: inapplicable — no score invalidation policy in these files; rerun creates new output from supplied inputs.
- Activation or effect: Score/report generation is wired; actual scoring, adoption and benefit unobserved.
- Evidence limits: Other harnesses, tracked output artifacts and comparison designs unassessed; no headline-rate reproduction or causal attribution.

> "failed": failed, "reportable": not failed,
> --- `evaluation/ectqa/native_score.py`

Additional load-bearing passages for the distinctions above follow. These are implementation evidence, not observed runs (SRC-1).

> Resolution is by document order, not by dates: the newer assertion wins.
> --- `post_graph_rag/graph_store.py`

> f"- ID {c['id']}: {c.get('description') or c.get('relation_type')}"
> --- `post_graph_rag/extractor.py`

> f"- ({r.get('src')}) --[{neg}{r.get('predicate')}]--> ({r.get('tgt')})"
>             f" (weight={weight}): {desc}"[:400]
> --- `post_graph_rag/reporting.py`

> "description": description or prev.get("description", ""),
>                 "sources": sources,
>                 "weight": weight,
> --- `post_graph_rag/graph_store.py`

> "valid_from": valid_from or prev.get("valid_from"),
>                 "valid_to": valid_to or prev.get("valid_to"),
> --- `post_graph_rag/graph_store.py`

> label = "yes" in text.lower()
> --- `evaluation/longmemeval/regrade_official.py`

> if f1 is not None:
>             ok, metric, value = f1 >= args.f1_threshold, "numeric_f1", f1
>         elif pf1 is not None:
>             ok, metric, value = pf1 >= args.f1_threshold, "period_f1", pf1
> --- `evaluation/ectqa/score.py`


> if gold == "unanswerable":
>                 # The dataset's own unanswerable questions: declining IS the
>                 # correct answer, so a refusal scores correct rather than
>                 # landing in its own bucket and deflating every rate.
>                 low = ans.lower()
>                 declined = ("unanswerable" in low or "not support" in low
>                             or "do not contain" in low or "no context" in low)
> --- `evaluation/ectqa/native_score.py`

> return (answer or "").strip().lower()[:60].startswith("unanswerable")
> --- `evaluation/ectqa/score.py`

### Claims

#### EPI-CLM-close-fact
Label: Later fact closure

Claimed operation: later documents can close earlier facts so answering no longer repeats an obsolete relation. This extends beyond the supplied passage-priority claim: it concerns changed reliance, not passage preservation. SRC-1 `README.md`, doctrine/design.

> What makes it different: **a later document can close an earlier fact**, so your model stops reporting that someone is both an ally and a rival.
> --- `README.md`

#### EPI-CLM-report-grounding
Label: Grounded community reporting

Claimed contract: statements grounded in provided entities/relations without outside knowledge or speculation. Distinct from supplied runtime claims; this is the content contract within the community-build route. SRC-1 `post_graph_rag/reporting.py`, doctrine/design.

> - Ground every statement in the supplied entities and relations. Do not introduce
>   outside knowledge, and do not speculate beyond what the relations state.
> --- `post_graph_rag/reporting.py`

#### EPI-CLM-benchmark-rates
Label: Benchmark reliability rates

Claimed reported operation: README reports 94.0% overall LongMemEval and 0.807 ECT-QA correct rate, with different generation/judging protocols and corpus-slice caveats. These are not a source-independent answer oracle. No counterpart claim in supplied runtime; offline scoring is a distinct use. SRC-1 `README.md`, reported operation.

> | **post-graph-rag** · `gemini-3.6-flash` | **94.0%** | **90.2%** | **96.2%** | **94.9%** |
> --- `README.md`

> | **post-graph-rag** · `gemini-3.6-flash` | **0.807** |
> --- `README.md`

> Their figures are on their corpus slice; ours is 78 questions over 6 companies. Read a few points of margin as approximate rather than decisive.
> --- `README.md`

#### EPI-CLM-validity-effect
Label: Validity rendering effect

Claimed component effect: validity in the synthesis prompt accounts for a temporal reasoning gain. Distinct from supplied runtime passage claim and from headline task rates: this is a causal attribution requiring an intervention comparison; the named implementation alone does not establish its magnitude. SRC-1 `README.md`, reported operation.

> Three things in that diagram are the whole argument: **supersession** at write time, **three retrieval channels fused rather than one**, and **validity rendered into the prompt** — the last being worth +38 points on temporal reasoning on its own.
> --- `README.md`
