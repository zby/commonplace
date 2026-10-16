---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Cognee epistemic routes: session-lesson acceptance, conflict handling, ranking and reference-answer evaluation at the frozen revision."
run-id: AAS-2026-10-14-cognee-d8839fe03c5b-01
reviewed-boundary: f154b32a9e544dac73e7ddf2010327cf9988edcd
---

# Cognee epistemic report

## Source-and-claim boundary

Question: how does Cognee turn acquired material into claims for later reliance, and which checks actually control that reliance? Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity/layers are see [Source register](boundary.md#source-register). All added reads below are SRC-1 implementation or explicitly labelled doctrine/design at the frozen commit. No target code was executed. No supplied execution or causal comparison establishes operation, quality or benefit.

The boundary remains a complete artifact, partial loop. External provider internals/weights, database internals, independent consuming applications and Cloud are excluded implementations. Those exclusions prevent provider accuracy, deployed durability and arbitrary-host compliance conclusions. Available but uninspected frontend, connector, worker, custom pipeline and alternate retrieval paths prevent a system-complete negative about knowledge acceptance, learning or factual verification.

Public reusable-knowledge claim: see [EPI-CLM-durable-lessons](#epi-clm-durable-lessons). It is not treated as a promise of infallible truth. Maintenance control claims remain see [RT-CLM-auto-admission](runtime.md#rt-clm-auto-admission) and [RT-CLM-improve-coordination](runtime.md#rt-clm-improve-coordination); neither is a per-content epistemic acceptance criterion. The truth-subspace recovery claim has an explicit internal countercase: see [EPI-CLM-epoch-recovery](#epi-clm-epoch-recovery).

| Operation/entry | SRC-1 path / inspection basis | Records covering material behavior | Limit / conclusion prevented |
| --- | --- | --- | --- |
| remember/add/cognify | `cognee/api/v1/remember/remember.py`, `cognee/api/v1/cognify/cognify.py`; supplied runtime findings | [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory) | Imported content source truth and all extractor fidelity unresolved. Storage is not acceptance. |
| recall/search and decorated host | `cognee/api/v1/recall/recall.py`, `cognee/infrastructure/llm/LLMGateway.py`; supplied runtime | [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), [RT-RTE-decorated-agent](runtime.md#rt-rte-decorated-agent), [RT-BAP-memory-injection](runtime.md#rt-bap-memory-injection) | Every lane and unrelated provider calls not traced; no host obedience conclusion. |
| improve stage orchestration | `cognee/modules/improve/registry.py`, `cognee/api/v1/improve/improve.py`; supplied runtime | [RT-RTE-session-improve](runtime.md#rt-rte-session-improve) | Feedback weights, QA, context, preferences, enrichment and global index stage bodies remain unassessed. No all-maintenance warrant conclusion. |
| Session distillation | `cognee/modules/session_distillation/distill.py`; direct read; curator/writer prompts directly read | [EPI-RTE-lesson-curation](#epi-rte-lesson-curation), [EPI-RTE-lesson-check](#epi-rte-lesson-check), [EPI-RTE-lesson-admission](#epi-rte-lesson-admission), [EPI-RTE-lesson-retention](#epi-rte-lesson-retention), [EPI-RTE-lesson-integration](#epi-rte-lesson-integration), [EPI-RTE-distillation-recovery](#epi-rte-distillation-recovery) | Candidate/source authentication and model compliance unobserved. |
| Contradiction / temporal cleanup | `cognee/tasks/graph/detect_contradictions.py` judgment/write body directly read; `cognee/tasks/graph/resolve_temporal_contradictions.py`, `cognee/modules/graph/utils/temporal_conflict_resolver.py` directly read | [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-contradiction-annotation](#epi-rte-contradiction-annotation), [EPI-RTE-temporal-supersession](#epi-rte-temporal-supersession) | Conflict renderer not fully inspected; all downstream conflict/supersession consumers uninspected. No universal abstention/withdrawal claim. |
| Truth build and hybrid consumer | `cognee/modules/truth_subspace/build.py`, `cognee/modules/truth_subspace/align.py`, `cognee/modules/retrieval/hybrid/truth.py`, `cognee/modules/retrieval/hybrid/ranking.py`; direct reads | [EPI-RTE-truth-reranking](#epi-rte-truth-reranking) | Centroid construction internals and benefit uninspected; similarity is not empirical truth. |
| Agentic tools and skill replacement | `cognee/modules/tools/registry.py`, `cognee/modules/tools/builtin/load_skill.py`, `cognee/modules/tools/builtin/memory_search.py` direct reads; loop/skill apply supplied runtime | [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools), [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), [RT-OBJ-agent-step](runtime.md#rt-obj-agent-step) | Dynamic graph tool producers/handlers uninspected. load_skill caps body at 12,000 chars before runtime's 8,000-char tool-output cap; delivered procedure need not be complete. Search tool forwards rendered triplets, not certified facts. |
| CLI dispatch | `cognee/cli/_cognee.py` command discovery directly read; command files inventoried | [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory), [RT-RTE-session-improve](runtime.md#rt-rte-session-improve), [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | Includes feedback, forget, delete, memify, eval and migrations beyond remember/recall; their complete handlers not traced. No exhaustive CLI parity or deletion/retraction conclusion. |
| MCP exposed operations | `cognee-mcp/src/server.py` registration/function-name search; client branches supplied runtime | [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), [RT-RTE-session-improve](runtime.md#rt-rte-session-improve) | remember, recall, code_search, forget, improve, cognify_status located; registration/mode policy and hook parity not fully inspected. |
| Benchmark evaluators | `cognee/eval_framework/evaluation/metrics/exact_match.py`, `cognee/eval_framework/evaluation/deep_eval_adapter.py`, `cognee/eval_framework/evaluation/evaluation_executor.py`, `cognee/eval_framework/evaluation/run_evaluation_module.py`; direct reads | [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | Other metrics, adapters, evals/tests and run artifacts uninspected; no benchmark accuracy or causal attribution conclusion. |

Missing actual proposal/decision pairs prevents classification of generated statements as entailed or ampliative, and any observed accepted ampliative claim. Missing execution traces prevents exercised acceptance/integration/behavior-change conclusions. Missing controlled comparisons prevents learning, improved reliability and component-effect conclusions. Opaque providers remain see [RT-CMP-llm-gateway](runtime.md#rt-cmp-llm-gateway) and [RT-CMP-embedding-config](runtime.md#rt-cmp-embedding-config): endpoint/model strings do not pin weights, and no local parameter-update operation is established. Retained lesson/procedure changes are not weight updates.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID/local anchor | gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-proposed-lesson](#epi-obj-proposed-lesson) | see record | see record | see record | see record |
| [EPI-OBJ-written-lesson](#epi-obj-written-lesson) | see record | see record | see record | see record |
| [EPI-OBJ-learning-document](#epi-obj-learning-document) | see record | see record | see record | see record |
| [EPI-OBJ-contradiction-list](#epi-obj-contradiction-list) | see record | see record | see record | see record |
| [EPI-OBJ-temporal-edge](#epi-obj-temporal-edge) | see record | see record | see record | see record |
| [EPI-OBJ-truth-coordinates](#epi-obj-truth-coordinates) | see record | see record | see record | see record |
| [EPI-OBJ-eval-metrics](#epi-obj-eval-metrics) | see record | see record | see record | see record |
| [RT-OBJ-agent-step](runtime.md#rt-obj-agent-step) | see record; final answer may express claims | see record | see record | No actual answer for semantic classification. |
| [RT-OBJ-skill-proposal](runtime.md#rt-obj-skill-proposal) | see record; procedure is operational guidance, rationale may express claims | see record | see record | No actual proposal or evaluation evidence. |

Imported raw/session content and graph/vector storage within permanent recall routes remain container findings see [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory) and [RT-RTE-session-improve](runtime.md#rt-rte-session-improve); no new duplicate object declaration substitutes for the memory analyst's independent inventory. Source warrant is unknown, not upgraded by indexing or session retention.

## Authority-route ledger

Route ID: [EPI-RTE-lesson-curation](#epi-rte-lesson-curation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-proposed-lesson](#epi-obj-proposed-lesson)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Session timeline to proposed statements
Evaluator/condition and domain: Model over bounded chronological batches; grounding/durability instructions
Activation and timing: New gated entries and available curator prompt; operation unobserved.
Possible or observed result: ProposedLesson list, empty list, or failed call
Implemented force: candidate generation only
Epistemic authority and scope: No accepted claim; candidate scope is the supplied session slice
Operational authority: Pass candidate to writer
Behavioral-authority path: Curator output → writer input; permissive; this distillation run
Evidence source ID and local anchor: see [EPI-RTE-lesson-curation](#epi-rte-lesson-curation).
Claim IDs: [EPI-CLM-durable-lessons](#epi-clm-durable-lessons)
Mismatch marker: see [EPI-RTE-lesson-curation](#epi-rte-lesson-curation).
Gap/limit: see [EPI-RTE-lesson-curation](#epi-rte-lesson-curation).

Route ID: [EPI-RTE-lesson-check](#epi-rte-lesson-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-written-lesson](#epi-obj-written-lesson)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Proposed lesson support, novelty and durability
Evaluator/condition and domain: Model judging member entries, similar lessons and entity glossary
Activation and timing: Per curator proposal after scoped vector searches; operation unobserved.
Possible or observed result: WrittenLesson accept/reason/statement or None on failure
Implemented force: advisory decision payload before code admission
Epistemic authority and scope: Conditional model judgment against supplied entries, not external factual verification
Operational authority: Produce decision for admission code
Behavioral-authority path: Writer output → accept_proposed_lessons; advisory; current lesson
Evidence source ID and local anchor: see [EPI-RTE-lesson-check](#epi-rte-lesson-check).
Claim IDs: [EPI-CLM-durable-lessons](#epi-clm-durable-lessons)
Mismatch marker: see [EPI-RTE-lesson-check](#epi-rte-lesson-check).
Gap/limit: see [EPI-RTE-lesson-check](#epi-rte-lesson-check).

Route ID: [EPI-RTE-lesson-admission](#epi-rte-lesson-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-written-lesson](#epi-obj-written-lesson)
Content/update relation: no content change
Transition or check target: Decision plus nonempty statement to admitted list
Evaluator/condition and domain: Code tests non-None, accept and stripped statement
Activation and timing: After writer calls complete; operation unobserved.
Possible or observed result: Accepted list and failed-call count
Implemented force: enforcing publication eligibility
Epistemic authority and scope: Accept decision names support, durability and novelty for graph reuse; no guarantee those judgments are true
Operational authority: Block rejects, failures and blank accepted statements from publication
Behavioral-authority path: accept_proposed_lessons → publisher; enforcing; this run
Evidence source ID and local anchor: see [EPI-RTE-lesson-admission](#epi-rte-lesson-admission).
Claim IDs: [EPI-CLM-durable-lessons](#epi-clm-durable-lessons)
Mismatch marker: see [EPI-RTE-lesson-admission](#epi-rte-lesson-admission).
Gap/limit: see [EPI-RTE-lesson-admission](#epi-rte-lesson-admission).

Route ID: [EPI-RTE-lesson-retention](#epi-rte-lesson-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learning-document](#epi-obj-learning-document)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Written lesson to Markdown document and add
Evaluator/condition and domain: Template code and dataset write permission
Activation and timing: If accepted list is nonempty; operation unobserved.
Possible or observed result: Rendered documents submitted to add
Implemented force: retention, separate from checking
Epistemic authority and scope: Preserves written statement plus why_learned text; neither storage nor title adds warrant
Operational authority: Write candidate accepted under writer criterion into dataset
Behavioral-authority path: publisher → add; permissive write; cross-invocation intent
Evidence source ID and local anchor: see [EPI-RTE-lesson-retention](#epi-rte-lesson-retention).
Claim IDs: [EPI-CLM-durable-lessons](#epi-clm-durable-lessons)
Mismatch marker: see [EPI-RTE-lesson-retention](#epi-rte-lesson-retention).
Gap/limit: see [EPI-RTE-lesson-retention](#epi-rte-lesson-retention).

Route ID: [EPI-RTE-lesson-integration](#epi-rte-lesson-integration)
Route function: lifecycle integration
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learning-document](#epi-obj-learning-document)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Accepted documents to cognify graph organization
Evaluator/condition and domain: Configured extraction pipeline after add
Activation and timing: Publication after writer admission; operation unobserved.
Possible or observed result: Graph/vector processing and returned documents
Implemented force: organizational integration after acceptance
Epistemic authority and scope: Upstream acceptance applies to written lesson; extraction fidelity remains unresolved
Operational authority: Connect/index accepted content for subsequent recall
Behavioral-authority path: publisher → cognify → retrieval stores; permissive; later invocations
Evidence source ID and local anchor: see [EPI-RTE-lesson-integration](#epi-rte-lesson-integration).
Claim IDs: [EPI-CLM-durable-lessons](#epi-clm-durable-lessons)
Mismatch marker: see [EPI-RTE-lesson-integration](#epi-rte-lesson-integration).
Gap/limit: see [EPI-RTE-lesson-integration](#epi-rte-lesson-integration).

Route ID: [EPI-RTE-distillation-recovery](#epi-rte-distillation-recovery)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-written-lesson](#epi-obj-written-lesson)
Content/update relation: no content change
Transition or check target: Processed input IDs to watermark or retry
Evaluator/condition and domain: Code distinguishes empty decision results from failed calls
Activation and timing: After publishing surviving lessons; operation unobserved.
Possible or observed result: Watermark advances or DistillationCallsFailedError
Implemented force: enforcing retry eligibility, not factual approval
Epistemic authority and scope: No extra truth license from successful processing
Operational authority: Do not seal failed-call inputs; allow future retry, keep surviving publication
Behavioral-authority path: distill_session → watermark store → later distill invocation; enforcing; across runs
Evidence source ID and local anchor: see [EPI-RTE-distillation-recovery](#epi-rte-distillation-recovery).
Claim IDs: [EPI-CLM-durable-lessons](#epi-clm-durable-lessons)
Mismatch marker: see [EPI-RTE-distillation-recovery](#epi-rte-distillation-recovery).
Gap/limit: see [EPI-RTE-distillation-recovery](#epi-rte-distillation-recovery).

Route ID: [EPI-RTE-contradiction-check](#epi-rte-contradiction-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction-list](#epi-obj-contradiction-list)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Numbered neighboring graph facts for direct contradiction
Evaluator/condition and domain: LLM with structured ContradictionList over capped touched neighborhood
Activation and timing: Opt-in ingestion check, at least two rendered facts; operation unobserved.
Possible or observed result: Pairs, reasons and confidences or caught failure
Implemented force: advisory judgment before annotation filter
Epistemic authority and scope: A model conflict hypothesis about these facts; no resolution of which source is true
Operational authority: Supply candidate conflict annotations
Behavioral-authority path: LLM result → task loop; advisory; current pass
Evidence source ID and local anchor: see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check).
Claim IDs: none
Mismatch marker: see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check).
Gap/limit: see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check).

Route ID: [EPI-RTE-contradiction-annotation](#epi-rte-contradiction-annotation)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction-list](#epi-obj-contradiction-list)
Content/update relation: no content change
Transition or check target: Judgments to stored contradicts edges
Evaluator/condition and domain: Code confidence threshold, provided fact IDs, valid endpoints
Activation and timing: Following conflict model output; operation unobserved.
Possible or observed result: Warning plus graph edges or no additions
Implemented force: advisory retained conflict; no ingestion veto
Epistemic authority and scope: Anchored model judgment only; threshold is not truth verification
Operational authority: Annotate existing graph rather than choose a winner or delete either fact
Behavioral-authority path: task → graph.add_edges; advisory; persistent graph, downstream conflict consumer uninspected
Evidence source ID and local anchor: see [EPI-RTE-contradiction-annotation](#epi-rte-contradiction-annotation).
Claim IDs: none
Mismatch marker: see [EPI-RTE-contradiction-annotation](#epi-rte-contradiction-annotation).
Gap/limit: see [EPI-RTE-contradiction-annotation](#epi-rte-contradiction-annotation).

Route ID: [EPI-RTE-temporal-supersession](#epi-rte-temporal-supersession)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-temporal-edge](#epi-obj-temporal-edge)
Content/update relation: non-truth-apt policy/content update: current-edge metadata
Transition or check target: Multiple distinct targets of caller-declared functional relation
Evaluator/condition and domain: Deterministic updated_at string order and position tie-break
Activation and timing: Opt-in post-write pass over touched subjects; operation unobserved.
Possible or observed result: Older edges tagged superseded, superseded_by, supersession_reason
Implemented force: enforcing metadata write, downstream interpretation uninspected
Epistemic authority and scope: Licenses current-by-recency policy, not empirical truth of latest assertion
Operational authority: Retain historical edge; record a preferred current assertion
Behavioral-authority path: resolver → graph.add_edges; enforcing metadata; persistent graph
Evidence source ID and local anchor: see [EPI-RTE-temporal-supersession](#epi-rte-temporal-supersession).
Claim IDs: none
Mismatch marker: see [EPI-RTE-temporal-supersession](#epi-rte-temporal-supersession).
Gap/limit: see [EPI-RTE-temporal-supersession](#epi-rte-temporal-supersession).

Route ID: [EPI-RTE-truth-reranking](#epi-rte-truth-reranking)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-truth-coordinates](#epi-obj-truth-coordinates)
Content/update relation: no content change
Transition or check target: Chunk candidate ordering
Evaluator/condition and domain: Numerical alignment with learning-derived centroid directions and matching epoch
Activation and timing: Optional truth weight and loaded centroids during hybrid retrieval; operation unobserved.
Possible or observed result: Multiplicative factor in [0.75,1.25], sorted limited chunks
Implemented force: ranking
Epistemic authority and scope: No empirical truth test; similarity to accepted lesson directions
Operational authority: Change selection/rank of chunk context, not accept a proposition
Behavioral-authority path: truth context → rank_chunk_summary_pairs → selected chunks; ranking; current query plus retained coordinates
Evidence source ID and local anchor: see [EPI-RTE-truth-reranking](#epi-rte-truth-reranking).
Claim IDs: [EPI-CLM-epoch-recovery](#epi-clm-epoch-recovery)
Mismatch marker: see [EPI-RTE-truth-reranking](#epi-rte-truth-reranking).
Gap/limit: see [EPI-RTE-truth-reranking](#epi-rte-truth-reranking).

Route ID: [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-eval-metrics](#epi-obj-eval-metrics)
Content/update relation: no content change
Transition or check target: Answer versus benchmark golden_answer
Evaluator/condition and domain: EM normalized string equality; configured GEval judge uses expected answer
Activation and timing: Offline supplied answer rows and selected metric names; operation unobserved.
Possible or observed result: Scores/reasons, None after exhausted retries
Implemented force: advisory lab/report evidence, no inspected production gate
Epistemic authority and scope: EM licenses only normalized equality to reference; GEval is model comparison under configured rubric
Operational authority: Return/save metrics for analysis; no traced answer withdrawal or skill install
Behavioral-authority path: adapter → executor → JSON/relational Metrics → statistics; advisory; evaluation run and reports
Evidence source ID and local anchor: see [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation).
Claim IDs: none
Mismatch marker: see [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation).
Gap/limit: see [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation).

Permanent acquisition and generated recall remain see [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory) and [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), respectively. Their source warrant and content semantics are unresolved at individual extractor/answer edges. They must not be treated as accepted propositions merely because recall returned them.

## System-claim versus route comparison

| claim ID | claimed operation/warrant | source/anchor and layer | doctrine/design support | implemented routes | observed-run support | causal support/design limits | supported conclusion | mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-durable-lessons](#epi-clm-durable-lessons) | see record | see record | see record | see record | see record | see record | see record | see record |
| [EPI-CLM-epoch-recovery](#epi-clm-epoch-recovery) | see record | see record | see record | see record | see record | see record | see record | see record |
| [RT-CLM-auto-admission](runtime.md#rt-clm-auto-admission) | see record | see record | see record | see record | see record | see record | see record | Start admission is not content acceptance. |
| [RT-CLM-improve-coordination](runtime.md#rt-clm-improve-coordination) | see record | see record | see record | see record | see record | see record | see record | Coordination is not epistemic endorsement. |

## Bounded conclusion

Cognee has an inspected model-mediated acceptance route for session lessons, not just a retain-and-retrieve pipeline. Its criterion is support by member entries, novelty relative to retrieved prior lessons, and usefulness beyond the session; intended use is persistent graph reuse. Writer decisions acquire enforcing publication force through a Boolean/nonempty-statement filter. Retention and graph integration then follow as separate functions. No actual accepted output or evidence-consuming decision instance is supplied, so this does not establish an observed produced accepted ampliative claim or the factual reliability of that acceptance. The writer's evidence view can omit QA and unresolved member IDs; fail-open novelty lookup weakens deduplication, not a proof of novelty. See [EPI-RTE-lesson-check](#epi-rte-lesson-check), [EPI-RTE-lesson-admission](#epi-rte-lesson-admission), [EPI-RTE-lesson-retention](#epi-rte-lesson-retention) and [EPI-RTE-lesson-integration](#epi-rte-lesson-integration).

Permanent ingestion acquires content with unknown source warrant. Rendering accepted lesson documents is non-ampliative formatting under the demonstrated template; extraction, summary and generated-answer semantics remain indeterminate without content pairs. No derivation from independently warranted premises is established by the inspected routes. Prompts requesting grounding establish requests, not reliable compliance. No evidence of non-entailment licenses classifying every generated lesson/answer as an ampliative conjecture. See [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory), [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch) and [EPI-RTE-lesson-curation](#epi-rte-lesson-curation).

Conflict handling has several distinct authorities. Model conflict judgment can create retained warning edges without rejecting ingestion; deterministic functional-relation recency can label an older assertion superseded without testing whether the newer one is true. Downstream interpretation of both edge types remains uninspected. Truth-subspace alignment ranks chunk context using lesson-derived numerical directions; its name is not a truth license. Epoch gating limits stale-state use but does not close the documented abandoned-basis/reused-epoch failure. See [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-contradiction-annotation](#epi-rte-contradiction-annotation), [EPI-RTE-temporal-supersession](#epi-rte-temporal-supersession) and [EPI-RTE-truth-reranking](#epi-rte-truth-reranking).

Reference-answer evaluation is a separate lab route. EM checks normalized equality, not source truth or semantic equivalence; GEval compares to expected answers under model judgment. Inspected consumers return/store scores and calculate reports, not enforce production acceptance, correct an answer or install a skill. No comparative or component-causal result is supplied. See [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation).

Skill replacement has caller-selected apply and target identity checks, not a demonstrated performance acceptance test. Procedures can shape later model/tool decisions, but the actual delivered body is capped and host/model compliance is unobserved. The runtime's independent skill-route conclusions remain see [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision): self-improvement and reflection afforded; learning, reflective theory-builder, autonomous theory-builder and content-directed criticism uninspected. No blanket negative about these properties follows from partial maintenance/evaluator coverage. Neither learned-text retention nor adaptive ranking proves weight training or successful capacity improvement.

## Shared records

### Operative objects

#### EPI-OBJ-proposed-lesson
Label: ProposedLesson working statement

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

This object is an operative payload of the containing route, not a duplicate route declaration. Source-native identity: ProposedLesson working_statement and member_entry_ids. Representational form: Natural-language candidate assertion plus symbolic source-entry IDs. Storage substrate: Transient Python model objects during distillation. Content/claimed role: Subject facts or durable working practices grounded by curator instruction in a session slice. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation). Gap/limit: A material generated payload within the session-maintenance route, not the session store or skill proposal. No actual instance supplied.

#### EPI-OBJ-written-lesson
Label: WrittenLesson statement and decision

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

This object is an operative payload of the containing route, not a duplicate route declaration. Source-native identity: WrittenLesson statement/why_learned/entities, accept/reason. Representational form: Natural-language statement/context with symbolic admission flag and entity names. Storage substrate: Transient structured result/list; accepted text enters graph documents. Content/claimed role: Statement is candidate truth-apt; accept is publication decision, not independent proof. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation). Gap/limit: Split from curator proposal because evaluator input, disposition and later consumers differ. Rejection-reason persistence not established.

#### EPI-OBJ-learning-document
Label: Session learning document

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

This object is an operative payload of the containing route, not a duplicate route declaration. Source-native identity: render_lesson_document output. Representational form: Natural-language Markdown statement and learning context; source-session identifier. Storage substrate: Document strings handed to add then graph/vector processing. Content/claimed role: Standalone accepted lesson for cross-session retrieval. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation). Gap/limit: Accepted written text is retained, then extracted; source-session ID alone is not an evidence trace.

#### EPI-OBJ-contradiction-list
Label: ContradictionList result

Part of: [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory)

This object is an operative payload of the containing route, not a duplicate route declaration. Source-native identity: ContradictionList contradictions with first_fact_id/second_fact_id, reason, confidence. Representational form: Natural-language reason plus symbolic fact references and scalar model confidence. Storage substrate: Transient structured output; qualifying annotations persist in graph. Content/claimed role: Truth-apt hypothesis that two rendered facts directly conflict. Evidence: SRC-1, `cognee/tasks/graph/detect_contradictions.py` (implementation). Gap/limit: Material optional pipeline payload, distinct from graph facts and original document content.

#### EPI-OBJ-temporal-edge
Label: Superseded graph edge

Part of: [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory)

This object is an operative payload of the containing route, not a duplicate route declaration. Source-native identity: Graph Edge tuple and superseded/superseded_by/supersession_reason properties. Representational form: Symbolic tuple/flags and natural-language reason. Storage substrate: Graph edge property dictionaries. Content/claimed role: Underlying fact may be truth-apt; superseded flag records recency policy, not truth evaluation. Evidence: SRC-1, `cognee/modules/graph/utils/temporal_conflict_resolver.py` (implementation). Gap/limit: Material post-ingestion edge part; later current-versus-history retrieval not traced.

#### EPI-OBJ-truth-coordinates
Label: Truth alignment coordinates

Source-native identity: DocumentChunk truth_alignment/truth_epoch and centroid vectors. Representational form: Numerical dense embedding-derived coordinates plus symbolic epoch IDs. Storage substrate: Graph node truth state and vector centroids. Content/claimed role: No proposition individuated by coordinates; intended ranking signal relative to learning directions. Evidence: SRC-1, `cognee/modules/truth_subspace/build.py` (implementation). Gap/limit: No counterpart after comparison: runtime embedding configuration names the inference component, not these derived persisted coordinates. No provider-parameter mutation established.

#### EPI-OBJ-eval-metrics
Label: Evaluation metrics payload

Source-native identity: LLMTestCase actual/expected outputs and per-answer metrics. Representational form: Natural-language answer/reason, symbolic metric keys and scalar score. Storage substrate: Transient results then JSON and relational Metrics payload. Content/claimed role: Answer/reference may be truth-apt; EM score is normalized equality, GEval score is attributed model judgment. Evidence: SRC-1, `cognee/eval_framework/evaluation/deep_eval_adapter.py` (implementation). Gap/limit: No counterpart after comparison: runtime evaluator coverage was uninspected. Golden answer provenance and actual result artifacts unavailable as supplied evidence.

### Routes

#### EPI-RTE-lesson-curation
Label: Curator candidate generation

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: Session timeline to proposed statements → ProposedLesson list, empty list, or failed call. Owner: Model over bounded chronological batches; grounding/durability instructions. Context/state/action effects: Pass candidate to writer; Curator output → writer input; permissive; this distillation run. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation).

Curator request combines QA and gated entries. Candidate meaning may be preserved or generalized; no actual input/output pair decides reshaping, entailment or non-entailment. Curator doctrine forbids unsupported specifics, but does not establish compliance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Proposals and a failed-batch count.
- Later read-back: Candidate statements can later enter published lesson documents only through writer admission.
- Delegated visibility: Curator sees chronological QA, user feedback and candidate text, whitespace-normalized and character-bounded.
- Selection predicate: Net helpfulness >= 0 and entry confidence >= MIN_GATE_CONFIDENCE; watermark requires new entries before work.
- Invalidation or expiry: Failed calls leave watermark unchanged; successful no-proposal runs can advance it.
- Activation or effect: Model-facing candidate generation is wired, not observed.
- Evidence limits: No session trace, actual proposal or authenticated source truth supplied.

> Propose durable lessons grounded in this slice. For each lesson return:
> --- `cognee/infrastructure/llm/prompts/session_distillation_curator_system.txt`

> return clamped_net_helpfulness(entry) >= 0 and entry.confidence >= MIN_GATE_CONFIDENCE
> --- `cognee/modules/session_distillation/distill.py`

#### EPI-RTE-lesson-check
Label: Writer evidence-consuming judgment

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: Proposed lesson support, novelty and durability → WrittenLesson accept/reason/statement or None on failure. Owner: Model judging member entries, similar lessons and entity glossary. Context/state/action effects: Produce decision for admission code; Writer output → accept_proposed_lessons; advisory; current lesson. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation).

The writer both evaluates and rewrites. Semantic preservation of statement rewriting is indeterminate without a pair. Prior-lesson and glossary searches fail open to []; missing member IDs are omitted. Conversation-only proposals can have no member entries even though the curator permits them; the writer is not passed the original QA transcript.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: WrittenLesson or None; rejection is a decision with accept=False, not a failed call.
- Later read-back: Accepted written statements may be published; durable storage of rejected decisions/reasons is not established here.
- Delegated visibility: Working statement, resolved member contents, retrieved prior lessons and glossary; not full curator timeline.
- Selection predicate: Per proposed lesson; member_entry_ids resolving in entries_by_id; bounded similarity search.
- Invalidation or expiry: Writer failure leaves the run watermark unchanged; rejected lessons do not enter publication.
- Activation or effect: Evidence-consuming judgment is wired; accuracy and actual decisions unobserved.
- Evidence limits: No independent oracle or model-internal proof; glossary fidelity is instructed, not program-checked.

> - accept=false, reason="unsupported": the MEMBER ENTRIES do not actually support the statement.
> - Otherwise accept=true and write the lesson.
> --- `cognee/infrastructure/llm/prompts/session_distillation_writer_system.txt`

> sections = [f"PROPOSED LESSON:\n{lesson.working_statement}"]
> --- `cognee/modules/session_distillation/distill.py`

#### EPI-RTE-lesson-admission
Label: Written lesson admission

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: Decision plus nonempty statement to admitted list → Accepted list and failed-call count. Owner: Code tests non-None, accept and stripped statement. Context/state/action effects: Block rejects, failures and blank accepted statements from publication; accept_proposed_lessons → publisher; enforcing; this run. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation).

This is an implemented acceptance architecture, not evidence that any particular produced ampliative proposition was accepted. The model proposes/decides support; code admits; caller starts an open maintenance request, not per-lesson human approval. No expected-answer oracle is used. Model accept=False vetoes publication; runtime errors distinguish failure from rejection.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted list with failures counted separately.
- Later read-back: Admitted list feeds retained documents, not a persisted approval log shown here.
- Delegated visibility: Publisher sees accepted WrittenLesson objects only.
- Selection predicate: lesson is not None and lesson.accept and lesson.statement.strip().
- Invalidation or expiry: Rejected work is omitted; failed calls remain retryable via watermark policy.
- Activation or effect: Code gives writer judgment publication force.
- Evidence limits: Actual accepted content and decision reliability unobserved.

> accepted = [
>         lesson
>         for lesson in decisions
>         if lesson is not None and lesson.accept and lesson.statement.strip()
>     ]
> --- `cognee/modules/session_distillation/distill.py`

#### EPI-RTE-lesson-retention
Label: Accepted lesson document retention

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: Written lesson to Markdown document and add → Rendered documents submitted to add. Owner: Template code and dataset write permission. Context/state/action effects: Write candidate accepted under writer criterion into dataset; publisher → add; permissive write; cross-invocation intent. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation).

Template preserves statement and attaches source-session ID and why_learned. The latter is generated context, not independent corroboration. Concrete deduction: statement="Use retries.", why_learned="A timeout occurred.", session_id="s" yields "# Session learning (session s)\n\nUse retries. (A timeout occurred.)\n". This follows inspected string operations without target execution.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Document strings returned after publication completes.
- Later read-back: Dataset graph/vector chunks intended for later recall and novelty search.
- Delegated visibility: add receives documents, authorized dataset/user and learning node sets.
- Selection predicate: Only admitted lessons; one document per lesson.
- Invalidation or expiry: Date-free rendering supports content dedup intent; actual add dedup/storage and lesson retraction not inspected.
- Activation or effect: Retained-document submission wired; durable adapter success unobserved.
- Evidence limits: No independently checked proposition or durable decision provenance established by rendering.

> statement = lesson.statement.strip()
>     why = lesson.why_learned.strip().rstrip(".")
>     body = f"{statement} ({why}.)" if why else statement
>     return f"# Session learning (session {session_id})\n\n{body}\n"
> --- `cognee/modules/session_distillation/distill.py`

#### EPI-RTE-lesson-integration
Label: Accepted document graph integration

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: Accepted documents to cognify graph organization → Graph/vector processing and returned documents. Owner: Configured extraction pipeline after add. Context/state/action effects: Connect/index accepted content for subsequent recall; publisher → cognify → retrieval stores; permissive; later invocations. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation).

Unlike raw session retention, this route follows a named acceptance decision. add tags learning node sets; cognify processes the dataset. It does not prove every extracted edge preserves the accepted statement. Caller authorized scope and model admission govern the write; no per-entity human review or cross-store rollback shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Documents after add and cognify return.
- Later read-back: Learning node-set DocumentChunks feed future novelty lookup and truth-subspace build; central recall can consume dataset memory.
- Delegated visibility: cognify receives dataset and user; extraction prompts depend on pipeline configuration.
- Selection predicate: Accepted lesson documents in authorized dataset.
- Invalidation or expiry: Publication can partially survive a later model failure; no graph rollback in distill_session.
- Activation or effect: Graph organization calls wired, successful integration unobserved.
- Evidence limits: Extractor semantics, backend durability and deployed retrieval activation remain unresolved.

> node_set = [*DISTILLATE_NODE_SET, truth_session_node_set(scope.session_id)]
>     await add(documents, dataset_id=scope.dataset.id, user=scope.user, node_set=node_set)
>     await cognify(datasets=[scope.dataset.id], user=scope.user)
> --- `cognee/modules/session_distillation/distill.py`

#### EPI-RTE-distillation-recovery
Label: Distillation watermark recovery

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: Processed input IDs to watermark or retry → Watermark advances or DistillationCallsFailedError. Owner: Code distinguishes empty decision results from failed calls. Context/state/action effects: Do not seal failed-call inputs; allow future retry, keep surviving publication; distill_session → watermark store → later distill invocation; enforcing; across runs. Evidence: SRC-1, `cognee/modules/session_distillation/distill.py` (implementation).

No proposed or accepted lessons after successful calls still advances all gated entry IDs. Failed curator/writer calls raise after publishing survivors and do not advance. Thus failure is not atomic rejection of all new graph content. Watermark records processing, not endorsement of every input.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Completion/no-lessons status or raised failure.
- Later read-back: Watermark input IDs filter later invocation work.
- Delegated visibility: Session manager receives user/session/dataset and gated entry IDs.
- Selection predicate: New gated entries trigger work; proposals use all gated entries.
- Invalidation or expiry: No watermark on call failure; no retraction of already-published survivors.
- Activation or effect: Processing/retry policy wired; eventual retry not guaranteed.
- Evidence limits: Watermark backend atomicity and real recovery traces uninspected.

> if curator_failures or writer_failures:
>         # An LLM outage is not "nothing durable to keep". Leave the watermark
>         # untouched — sealing the entries here would mark them distilled
>         # forever on the strength of calls that never ran.
>         raise DistillationCallsFailedError(
> --- `cognee/modules/session_distillation/distill.py`

#### EPI-RTE-contradiction-check
Label: Contradiction candidate judgment

Part of: [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory)

Endpoints/progression: Numbered neighboring graph facts for direct contradiction → Pairs, reasons and confidences or caught failure. Owner: LLM with structured ContradictionList over capped touched neighborhood. Context/state/action effects: Supply candidate conflict annotations; LLM result → task loop; advisory; current pass. Evidence: SRC-1, `cognee/tasks/graph/detect_contradictions.py` (implementation).

Runtime mentioned conditional contradiction checks but did not establish their result consumer. The added part traces this missing judgment separately. Candidate judgments are truth-apt about compatibility; non-entailment is not evidenced by an actual pair. Structured schema and confidence do not warrant the source facts.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ContradictionList internally, original DataPoint list eventually returned.
- Later read-back: Qualifying conflict hypotheses are retained as edges by the linked annotation route.
- Delegated visibility: Model receives rendered facts from one-hop touched neighborhood, capped by config.
- Selection predicate: At least two facts and configured optional pipeline activation.
- Invalidation or expiry: Task catches errors and returns original data; no admission rollback.
- Activation or effect: Conflict judgment request wired, no observed judgments.
- Evidence limits: Fact renderer first half and model accuracy uninspected; no comprehensive conflict detection claim.

> result = await LLMGateway.acreate_structured_output(
>             text_input=user_prompt,
>             system_prompt=system_prompt,
>             response_model=ContradictionList,
>         )
> --- `cognee/tasks/graph/detect_contradictions.py`

#### EPI-RTE-contradiction-annotation
Label: Contradiction edge annotation

Part of: [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory)

Endpoints/progression: Judgments to stored contradicts edges → Warning plus graph edges or no additions. Owner: Code confidence threshold, provided fact IDs, valid endpoints. Context/state/action effects: Annotate existing graph rather than choose a winner or delete either fact; task → graph.add_edges; advisory; persistent graph, downstream conflict consumer uninspected. Evidence: SRC-1, `cognee/tasks/graph/detect_contradictions.py` (implementation).

Annotation retains own rendered first_fact/second_fact, reason and confidence, avoiding model-invented fact text. It does not enforce answer abstention, withdrawal or rejection in this inspected task. Actual downstream contradicts-edge consumers remain uninspected, so no system-wide claim of advisory-only force follows.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Original DataPoint list unchanged.
- Later read-back: Conflict edge remains graph material; concrete later answer handling uninspected.
- Delegated visibility: Graph engine receives endpoint IDs, rendered facts and model reason/confidence.
- Selection predicate: Confidence threshold and both fact IDs must map to supplied edges; endpoints must exist.
- Invalidation or expiry: Errors caught; no automatic deletion or truth winner; conflict expiration uninspected.
- Activation or effect: Graph annotation write wired; no run or later conflict-aware answer supplied.
- Evidence limits: No truth acceptance; no uniform all-retriever conflict behavior established.

> if contradiction_edges:
>             await graph_engine.add_edges(contradiction_edges)
>             logger.info("Flagged %s contradiction(s) in the graph.", len(contradiction_edges))
> --- `cognee/tasks/graph/detect_contradictions.py`

> # The model referenced an id we did not provide; nothing to anchor.
> --- `cognee/tasks/graph/detect_contradictions.py`

#### EPI-RTE-temporal-supersession
Label: Functional relation supersession

Part of: [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory)

Endpoints/progression: Multiple distinct targets of caller-declared functional relation → Older edges tagged superseded, superseded_by, supersession_reason. Owner: Deterministic updated_at string order and position tie-break. Context/state/action effects: Retain historical edge; record a preferred current assertion; resolver → graph.add_edges; enforcing metadata; persistent graph. Evidence: SRC-1, `cognee/tasks/graph/resolve_temporal_contradictions.py` (implementation).

Caller defines single-valued relations; code decides recency, no answer oracle or human per-edge approval. Countercase: a newer false assertion outranks an older true assertion under the same policy. Deterministic trace: two edges (A,B,ceo) updated_at="2026-01-01" and (A,C,ceo) updated_at="2026-02-01" choose C; only B receives copied supersession properties. This is implementation deduction, not target execution. No delete or automatic rollback shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Original DataPoint list; helper returns tagged copies of losing edges.
- Later read-back: Persisted supersession metadata is available to future graph readers; filtering semantics uninspected.
- Delegated visibility: Graph receives copied property dictionaries for losing assertions only.
- Selection predicate: Caller functional_relationships plus touched subject and more than one distinct target.
- Invalidation or expiry: No delete; original facts remain; revert mechanism not traced.
- Activation or effect: Recency-based metadata changes wired, actual current-fact answer handling unobserved.
- Evidence limits: Recency is not endorsement; no system-wide latest-only retrieval claim.

> for key, members in groups.items():
>         if len({edges[i][1] for i in members}) > 1:
>             winners[key] = max(members, key=lambda i: _recency_key(i, edges[i][3]))
> --- `cognee/modules/graph/utils/temporal_conflict_resolver.py`

#### EPI-RTE-truth-reranking
Label: Truth-subspace chunk ranking

Distinct identity: material optional selector inside [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), not that entire route.

Endpoints/progression: Chunk candidate ordering → Multiplicative factor in [0.75,1.25], sorted limited chunks. Owner: Numerical alignment with learning-derived centroid directions and matching epoch. Context/state/action effects: Change selection/rank of chunk context, not accept a proposition; truth context → rank_chunk_summary_pairs → selected chunks; ranking; current query plus retained coordinates. Evidence: SRC-1, `cognee/modules/retrieval/hybrid/ranking.py` (implementation).

Compared with runtime recall dispatch, this is a distinct material ranking part, not the entire dispatcher. Build reads learning node-set text, embeds it and corpus chunks, persists chunk coordinates before centroid epoch commit. Epoch mismatch suppresses weighting and lookup exceptions return baseline. The build explicitly names an abandoned-basis/reused-epoch two-failure countercase; integer epoch matching alone cannot prove coordinate-basis fidelity. A label truth_score does not establish a truth evaluator.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ordered limited chunk-summary pairs.
- Later read-back: Build persists coordinates and centroids; later queries reload both.
- Delegated visibility: Ranking code receives candidate ranks, query coords, retained truth state and live epoch.
- Selection predicate: use_truth_weight, nonempty q_coords, live epoch, and exact chunk epoch equality.
- Invalidation or expiry: Epoch mismatch ignores coordinates; load errors use baseline; reused epoch can admit abandoned-basis coords.
- Activation or effect: Optional alignment changes ranking by inspected multiplication; actual quality/activation unobserved.
- Evidence limits: Centroid algorithm internals not fully inspected; no warranted-premise derivation or external factual measurement.

> if truth_state.get("truth_epoch") == current_truth_epoch:
>                 final_score *= truth_factor(truth_state.get("truth_alignment", []), q_coords)
> --- `cognee/modules/retrieval/hybrid/ranking.py`

> return 0.75 + 0.5 * truth_score(node_coords, q_coords)
> --- `cognee/modules/truth_subspace/align.py`

#### EPI-RTE-benchmark-evaluation
Label: Reference-answer benchmark evaluation

Endpoints/progression: Answer versus benchmark golden_answer → Scores/reasons, None after exhausted retries. Owner: EM normalized string equality; configured GEval judge uses expected answer. Context/state/action effects: Return/save metrics for analysis; no traced answer withdrawal or skill install; adapter → executor → JSON/relational Metrics → statistics; advisory; evaluation run and reports. Evidence: SRC-1, `cognee/eval_framework/evaluation/deep_eval_adapter.py` (implementation).

No counterpart after comparison: runtime explicitly left evaluator bodies uninspected. This is a bounded benchmark mode with golden_answer as reference oracle; reference provenance/accuracy is uninspected. EM trace: actual=" Paris ", expected="PARIS" normalizes to equal and yields 1.0; actual="Paris, France" yields 0.0 against "PARIS" despite possible compatible meaning. No target execution needed. GEval correctness is a separate model judgment, not an equality guarantee. Other metrics and benchmark adapters uninspected.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-answer metrics returned with input payload.
- Later read-back: execute_evaluation saves JSON and a relational Metrics payload; statistics can later read metrics_path.
- Delegated visibility: LLMTestCase receives question, answer and golden_answer plus optional contexts.
- Selection predicate: Requested evaluator_metrics selects metrics; unsupported names raise.
- Invalidation or expiry: Metric retries ultimately return None score/reason; no answer repair here.
- Activation or effect: Metric production and reporting wired, not observed or causally validated.
- Evidence limits: No independently authenticated benchmark run; reporting does not prove deployed memory acceptance or component benefit.

> actual = test_case.actual_output.strip().lower() if test_case.actual_output else ""
>         expected = test_case.expected_output.strip().lower() if test_case.expected_output else ""
>         self.score = 1.0 if actual == expected else 0.0
> --- `cognee/eval_framework/evaluation/metrics/exact_match.py`

> expected_output=answer["golden_answer"],
> --- `cognee/eval_framework/evaluation/deep_eval_adapter.py`

> with open(params["metrics_path"], "w", encoding="utf-8") as f:
>         json.dump(metrics, f, ensure_ascii=False, indent=4)
> 
>     await create_and_insert_metrics_table(metrics)
> --- `cognee/eval_framework/evaluation/run_evaluation_module.py`

### Claims

#### EPI-CLM-durable-lessons
Label: Durable session lessons

Claimed operation: session lessons become durable knowledge another session can retrieve. Source: SRC-1, `README.md` (doctrine/design). No counterpart after comparison: runtime claims describe orchestration admission and locks, not this public knowledge-production claim. Support: curator requests grounded durable lessons; writer names support/novelty/durability and can reject; acceptance code gates publication; documents enter add/cognify, see [EPI-RTE-lesson-admission](#epi-rte-lesson-admission) and [EPI-RTE-lesson-integration](#epi-rte-lesson-integration). Implementation conclusion status: wired. Operation conclusion status: uninspected. No observed-run or causal support. Supported conclusion: an acceptance-and-persistence architecture for reusable lessons; no demonstrated true lessons, fidelity, future benefit or complete evidence preservation. Mismatch/unknown: factual support depends on selected entries and model judgment, not an external truth oracle.

> - **Give agents memory across runs.** Retain project context, past decisions, fixes, and learned rules. Distill useful session lessons into durable knowledge that another session can retrieve. [Connect your agent](#connect-your-agent).
> --- `README.md`

#### EPI-CLM-epoch-recovery
Label: Truth epoch recovery

Claimed operation: chunk-coordinate write-before-centroid commit and epoch checks yield degraded rather than wrong reranking after failure. Source: SRC-1, `cognee/modules/truth_subspace/build.py` (doctrine/design and implementation). Distinct identity from [RT-CLM-improve-coordination](runtime.md#rt-clm-improve-coordination): coordinate/basis consistency, not process-local locks. Support: write order and epoch consumer wired, see [EPI-RTE-truth-reranking](#epi-rte-truth-reranking). No observed-run or causal experiment support. Supported conclusion: mismatch epochs suppress weights; unqualified recovery guarantee is too broad. Mismatch: the same file documents abandoned-basis coordinates passing a reused integer epoch under two failures and changed lessons. This countercase limits the local docstring, not a supersession of runtime lock facts. It is not a supplied observed incident.

> leaves epoch N live. Chunks rewritten at N+1 before such a failure no longer
> match the live epoch, so the reranker ignores them until a later build
> succeeds — degraded reranking, never wrong reranking. Chunks whose
> --- `cognee/modules/truth_subspace/build.py`

> # Known limit: chunk validity at read time is the integer epoch alone
>         # (ranking.py compares truth_epoch), not the learning basis. A run
>         # that stamped chunks at N+1 and crashed before the commit, followed
>         # by a run over DIFFERENT learnings that also computes N+1 but skips
>         # some chunks (failed embedding batches are skipped, not cleared),
>         # leaves those chunks passing the epoch guard with abandoned-basis
>         # coordinates. Two independent failures, damage bounded by the
>         # [0.75, 1.25] factor; stamping ``signature`` per chunk would close
>         # it if it ever matters.
> --- `cognee/modules/truth_subspace/build.py`

### Behavioral-authority paths

none declared in this member; route records own the new paths. Existing memory-input and skill-input paths are see [RT-BAP-memory-injection](runtime.md#rt-bap-memory-injection) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). Added load_skill inspection qualifies delivered completeness, without superseding their valid container identities:

> body = skill.procedure or "(this skill has no procedure body)"
>     if len(body) > MAX_SKILL_BODY_CHARS:
>         body = body[:MAX_SKILL_BODY_CHARS] + "\n... [truncated]"
>     return f"# Skill: {skill.name}\n{body}"
> --- `cognee/modules/tools/builtin/load_skill.py`
