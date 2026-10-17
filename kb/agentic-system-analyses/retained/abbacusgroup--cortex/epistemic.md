---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Cortex epistemic routes: imported assertions, model metadata, formal inference, heuristic warnings and the limits of reliance."
run-id: AAS-2026-10-17-cortex-3da14ce55a2b-01
reviewed-boundary: a51c2209eb6d26812c19c97aaade3cb64ccfc23c
---

# Cortex epistemic report

## Source-and-claim boundary

The question is what Cortex acquires, produces, checks and licenses for later reliance, rather than whether its database deserves the name knowledge. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers: see [Source register](boundary.md#source-register). All new evidence below is SRC-1 at that pin, implementation unless marked doctrine/design. No target execution was performed. No observed run, production corpus, provider response or causal comparison is supplied. Consequently operation, summary fidelity, actual acceptance by a host and improved task performance remain unestablished. Provider weights and host reasoning are excluded, preventing claims about their internal epistemic processes. Repository evaluators are available source, not measured outcomes.

The following coverage distinguishes direct reads/searches in this job from supplied findings. It is a material-route account, not a complete file audit. No supplied runtime fact needs supersession; the doctor route and the stronger alert wording add coverage to that provisional baseline.

| Entry point or operation | SRC-1 source path | Coverage and records / remaining limit |
|---|---|---|
| CLI capture, direct capture, imports; pipeline bypass | `src/cortex/cli/main.py`, `src/cortex/pipeline/importer.py`, `src/cortex/pipeline/orchestrator.py` | Supplied: [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline), [RT-RTE-direct-import](runtime.md#rt-rte-direct-import). CLI dispatch signatures searched directly; importer bodies not independently reread. |
| Public MCP capture, classify, link, feedback, pipeline | `src/cortex/transport/mcp/server.py` | Tool registrations searched; classify/pipeline bodies directly read; other entry behavior supplied by [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline), [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge), [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). |
| Classification, entity filtering, relationship proposal and rejection | `src/cortex/services/llm.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/link.py` | Direct complete reads: [EPI-RTE-metadata-generation](#epi-rte-metadata-generation), [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-metadata-admission](#epi-rte-metadata-admission). |
| Enrichment tier/staleness metadata and template application | `src/cortex/pipeline/enrich.py`, `src/cortex/pipeline/orchestrator.py` | Supplied [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) and [RT-CLM-stage-resilience](runtime.md#rt-clm-stage-resilience); not independently read. Supplied evidence supports metadata updates, not truth checking. Detailed enrichment criteria remain unassessed, preventing exhaustive authority coverage. |
| Fixed-rule inference and fixpoint diagnosis | `src/cortex/pipeline/reason.py` | Direct complete read: [EPI-RTE-rule-derivation](#epi-rte-rule-derivation), [EPI-RTE-rule-retention](#epi-rte-rule-retention), [EPI-RTE-health-check](#epi-rte-health-check). |
| Contradiction, pattern, gap, staleness and chain operations | `src/cortex/pipeline/advanced_reason.py` | Direct complete read: [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics). Chain assembly follows existing causal edges; it does not independently identify causes. |
| Search/context/read, dossier and graph selection | `src/cortex/retrieval/engine.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/transport/mcp/server.py` | Supplied: [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). Direct presenter synthesis/alert reads add [EPI-RTE-period-synthesis](#epi-rte-period-synthesis) and [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics). Dossier and engine bodies not independently reread. |
| Feedback and access promotion; weight helper APIs | `src/cortex/retrieval/learner.py` | Complete direct read and caller search in `src/`, `.github/`, `pyproject.toml`: [EPI-RTE-access-adaptation](#epi-rte-access-adaptation). Search finds no shipped calls to detect_miss, adjust_tiers or get_weights outside their definitions; update_weights is called by reset_weights only. No automatic ranking tuning established by these helpers. |
| Admin edit/delete/unlink/status/reason and safety | `src/cortex/transport/mcp/server.py`, `src/cortex/db/store.py` | Direct handlers through unlink read; remainder supplied: [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge), [RT-RTE-transport-control](runtime.md#rt-rte-transport-control), [RT-OBJ-store](runtime.md#rt-obj-store). Store method/call searches supplement supplied storage findings. |
| Doctor check/repair | `src/cortex/cli/main.py` | Direct complete function reads: [EPI-RTE-health-check](#epi-rte-health-check), [EPI-RTE-health-repair](#epi-rte-health-repair). FTS backing implementation searched, not independently read: actual FTS correctness not assessed. |
| REST/dashboard, backup/restore, install/release, embedding adapters | `src/cortex/transport/api/server.py`, `src/cortex/dashboard/server.py`, `src/cortex/cli/backup.py`, `src/cortex/cli/install.py`, `src/cortex/services/embeddings.py` | Supplied findings: [RT-RTE-transport-control](runtime.md#rt-rte-transport-control), [RT-RTE-install-release](runtime.md#rt-rte-install-release), [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge), component records below. Not independently reread; no deployment or weight-learning verdict. |
| Source evaluators and agent instructions | `benchmarks/b3_contradiction/test_bench.py`, `benchmarks/b4_graph_intelligence/test_bench.py`, `benchmarks/b5_pattern_detection/test_bench.py`, `README.md`, `llms.txt` | Scoped direct searches: [EPI-CLM-formal-intelligence](#epi-clm-formal-intelligence), [EPI-CLM-retrieval-learning](#epi-clm-retrieval-learning). Test outcome assertions are not supplied results. Other tests, corpus and benchmark metrics not independently assessed; prevents a system-complete evaluation-quality conclusion. |

Claims considered: [EPI-CLM-formal-intelligence](#epi-clm-formal-intelligence), [EPI-CLM-semantic-checks](#epi-clm-semantic-checks), [EPI-CLM-retrieval-learning](#epi-clm-retrieval-learning), plus the supplied resilience and consistency claims below. No universal claim that every stored assertion has been truth-validated is attributed to Cortex.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-document-text](#epi-obj-document-text) | Caller/imported assertions about decisions, fixes, lessons and other domains; particular truth-apt units depend on input | see record | SRC-1 `src/cortex/db/store.py` | Imported, not produced; author/source warrant unknown |
| [EPI-OBJ-summary](#epi-obj-summary) | Claims compressing source text | see record | SRC-1 `src/cortex/pipeline/normalize.py` | Internal summary, external summary and fallback differ; fidelity not guaranteed |
| [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | Typed propositions, e.g. A causedBy B or A supersedes C | see record | SRC-1 `src/cortex/pipeline/link.py`, `src/cortex/pipeline/reason.py` | Native asserted and inferred edges not separately warranted |
| [EPI-OBJ-classification](#epi-obj-classification) | Type/project/entity associations; confidence/tier are control metadata, not proofs | see record | SRC-1 `src/cortex/services/llm.py`, `src/cortex/retrieval/learner.py` | Class membership can be truth-apt under an ontology; intended-use truth criteria unestablished |
| [EPI-OBJ-diagnostic-result](#epi-obj-diagnostic-result) | Counts, dependency patterns; proposed systemic issue or documentation gap | see record | SRC-1 `src/cortex/pipeline/advanced_reason.py`, `src/cortex/retrieval/presenters.py` | Structural observation versus explanatory extrapolation split in ledger |
| [EPI-OBJ-period-narrative](#epi-obj-period-narrative) | Period counts or model-composed cross-document claims | see record | SRC-1 `src/cortex/retrieval/presenters.py` | No actual model output supplied |
| [RT-OBJ-inference-rules](runtime.md#rt-obj-inference-rules) | Explicit formal assumptions about predicates | see record | SRC-1 `src/cortex/pipeline/reason.py` | World truth of input edges not checked by closure |
| [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer), [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider) | Particular truth-apt content in weights/vectors not determinable | see records | SRC-1 `src/cortex/services/llm.py`, `src/cortex/services/embeddings.py` | Distributed-parametric components; supplied records establish inference-only adapters, no exact version pin and model-resolution uncertainty, not absence of provider learning |

## Authority-route ledger

The rows split checking, disposition, retention and use. Architectural status is assessed here; fields owned by supplied records are cited rather than redeclared. All implemented rows are static evidence, not observed operation. “No acceptance established” below concerns the named candidate and criterion, not an assertion that no external human could accept it.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source and local anchor | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | content transformation | implemented | [EPI-OBJ-document-text](#epi-obj-document-text) | truth-apt transformation: acquisition/import | Caller assertions enter retained service | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | Source warrant unknown; origin channel is not authentication | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery) | SRC-1 `src/cortex/pipeline/orchestrator.py` | none | none | Direct/import alternatives: see [RT-RTE-direct-import](runtime.md#rt-rte-direct-import) |
| [EPI-RTE-metadata-generation](#epi-rte-metadata-generation) | content transformation | implemented | [EPI-OBJ-summary](#epi-obj-summary); [EPI-OBJ-classification](#epi-obj-classification); [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | truth-apt transformation: indeterminate | Model interpretations of bounded input | Configured model; no supplied semantic comparison | When summary absent and model available | Summary/type/entity proposals or fallback | Candidate generation | Preservation versus new proposition cannot be settled without source/output pairs | Proposals proceed to structure checks | Normalizer → metadata; candidate then stored and served | SRC-1 `src/cortex/services/llm.py` | none | none | Fallback title copy is non-ampliative reshaping; model branch may reshape, derive or conjecture |
| [EPI-RTE-structure-check](#epi-rte-structure-check) | check/evidence production | implemented | [EPI-OBJ-classification](#epi-obj-classification); [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | no content change | JSON/type/entity schema; relation endpoints, predicate, self-link, confidence | Parser and fixed predicates; structural domain only | After completion, before relationship writes | Pass/skip/fallback; see record | Enforcing for named structural gates | Well-formedness/existence only; confidence is not calibrated truth evidence | Allows conforming proposals to reach writes | LLMClient/LinkStage → filtered proposals → writer, immediate | SRC-1 `src/cortex/services/llm.py`, `src/cortex/pipeline/link.py` | none | none | No reference-answer oracle or semantic verification established |
| [EPI-RTE-metadata-admission](#epi-rte-metadata-admission) | disposition/acceptance | implemented | [EPI-OBJ-summary](#epi-obj-summary); [EPI-OBJ-classification](#epi-obj-classification); [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | no content change | Which proposals are written | Fixed software; caller classify bypasses internal model; see record | After structure checks, or explicit caller reclassification | Stored metadata/edges; invalid proposals skipped | Enforcing operational disposition | No evidence-consuming truth acceptance for intended knowledge use | Classifications/edges become available to retrieval and reasoning | Normalizer/LinkStage/classify → SQLite/Oxigraph → later service calls | SRC-1 `src/cortex/pipeline/normalize.py`, `src/cortex/transport/mcp/server.py` | none | none | Admission is not epistemic acceptance; confidence 0.9 on classify is assigned |
| [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | retention | implemented | [EPI-OBJ-document-text](#epi-obj-document-text); [EPI-OBJ-summary](#epi-obj-summary); [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | no content change | Retain before and after stages | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | Persistence does not endorse assertions | see [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | see [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery) | SRC-1 `src/cortex/pipeline/orchestrator.py` | none | none | No observed operation |
| [EPI-RTE-rule-derivation](#epi-rte-rule-derivation) | content transformation | implemented | [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | truth-apt transformation: entailed derivation | Symmetry, inverse and transitive closure within four rules | SPARQL patterns; formal graph domain under rule assumptions | Pipeline reason or explicit repair; see record | Missing triples constructed | Fixed query semantics | Conditional entailment only, not truth of premises or encoding | Constructed triples become candidates for graph addition | see [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution) | SRC-1 `src/cortex/pipeline/reason.py` | [EPI-CLM-formal-intelligence](#epi-clm-formal-intelligence) | none | No rule-specific source-truth check; concrete deduction in record |
| [EPI-RTE-rule-retention](#epi-rte-rule-retention) | retention | implemented | [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | no content change | Absent inferred triples become persistent edges | Existence check; not an independent evidence check | During each rule application | Graph additions and counts | Enforcing writes | No extra warrant beyond conditional derivation | Later graph queries and derivations can use inferred edges | see [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution) | SRC-1 `src/cortex/pipeline/reason.py` | [EPI-CLM-formal-intelligence](#epi-clm-formal-intelligence) | none | No dependency-based retraction established by additive reasoner |
| [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics) | check/evidence production | implemented | [EPI-OBJ-diagnostic-result](#epi-obj-diagnostic-result) | truth-apt transformation: entailed derivation | Counts/patterns in bounded current graph | Fixed structural predicates; listed objects/mentions only | reason/status request; dossier supplied in runtime | Superseded dependent, frequency/window, missing type, stale edge | Advisory | License limited to matching structural conditions | Warnings returned; do not themselves revise reliance or content | AdvancedReasoner/AlertPresenter → result/status → caller, advisory current request | SRC-1 `src/cortex/pipeline/advanced_reason.py`, `src/cortex/retrieval/presenters.py` | [EPI-CLM-semantic-checks](#epi-clm-semantic-checks) | Semantic docstring overstates body | No semantic LLM contradiction comparison in inspected body; list caps prevent completeness |
| [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics) | content transformation | implemented | [EPI-OBJ-diagnostic-result](#epi-obj-diagnostic-result) | truth-apt transformation: ampliative conjecture | Repeated fixes → systemic issue; missing type → architecture/learning gap | Fixed heuristic, not independent explanatory test | After structural match | Possible systemic issue, or stronger alert label | Advisory | Non-entailment: repeated fixes can be unrelated; decisions may be documented elsewhere | Suggests review only; no automatic truth rejection | Diagnostics/status → caller prose, immediate; no enforced host uptake | SRC-1 `src/cortex/pipeline/advanced_reason.py`, `src/cortex/retrieval/presenters.py` | [EPI-CLM-formal-intelligence](#epi-clm-formal-intelligence) | Alert wording stronger than advanced result | No causal experiment validates explanatory inference |
| [EPI-RTE-period-synthesis](#epi-rte-period-synthesis) | content transformation | implemented | [EPI-OBJ-period-narrative](#epi-obj-period-narrative) | truth-apt transformation: indeterminate | Model narrative from first 20 recent summaries | Configured model; no post-completion evidence check | Explicit synthesis request with nonempty recent set | Narrative response and bounded source list | Advisory | No semantic fidelity or acceptance license | Returned as service output, not automatically persisted as accepted synthesis | Presenter → MCP/CLI caller, advisory immediate response | SRC-1 `src/cortex/retrieval/presenters.py` | none | none | Could reshape, derive or conjecture; source/output evidence needed to classify |
| [EPI-RTE-period-synthesis](#epi-rte-period-synthesis) | content transformation | implemented | [EPI-OBJ-period-narrative](#epi-obj-period-narrative) | truth-apt transformation: entailed derivation | Fallback period count and type histogram | Deterministic counts over selected list | No available model or completion failure | Count narrative | Advisory | Correct only about selected bounded records and metadata | Returned as synthesis, no automatic capture | Presenter → requesting caller, current response | SRC-1 `src/cortex/retrieval/presenters.py` | none | none | Not a complete claim about events outside bounded database listing |
| [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context) | operational admission/selection/consumption | implemented | [EPI-OBJ-document-text](#epi-obj-document-text); [EPI-OBJ-summary](#epi-obj-summary) | no content change | Select and deliver retained assertions | see [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context) | see [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context) | see [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context) | Ranking and informational delivery | Relevance/recency is not endorsement | see [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context) | see [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery) | SRC-1 `src/cortex/retrieval/presenters.py` | none | none | Context reshapes projection non-ampliatively; host action unobserved |
| [EPI-RTE-access-adaptation](#epi-rte-access-adaptation) | behavior/policy adaptation | implemented | [EPI-OBJ-classification](#epi-obj-classification) | non-truth-apt policy/content update: access counters and tier | Frequency of reads or positive relevance signals | Counter threshold ≥10, not truth evaluator | After read/positive feedback | Counter increment, possible reflex tier | Enforcing metadata update | No truth license; relevance is not correctness | Changes tier surfaced by future briefings; no automatic weight tuning established | read/feedback → learner → stored tier → later briefing metadata | SRC-1 `src/cortex/retrieval/learner.py` | [EPI-CLM-retrieval-learning](#epi-clm-retrieval-learning) | none | Improved capacity and host response to tier not demonstrated |
| [EPI-RTE-health-check](#epi-rte-health-check) | check/evidence production | implemented | [RT-OBJ-store](runtime.md#rt-obj-store) | no content change | FTS consistency and pending rule closure | Backing FTS check and four CONSTRUCT queries | Explicit doctor check | Status/warning, repair suggestion | Advisory | Index consistency/closure only, not content truth | Guides operator; does not automatically invoke repair | Doctor → terminal → operator, immediate advisory | SRC-1 `src/cortex/cli/main.py`, `src/cortex/pipeline/reason.py` | none | none | Rule query errors counted as zero; fixpoint OK cannot certify error-free reasoning |
| [EPI-RTE-health-repair](#epi-rte-health-repair) | lineage/freshness/recovery | implemented | [RT-OBJ-store](runtime.md#rt-obj-store) | no content change | Index rebuild/checkpoint and invocation of additive reasoning | Operator request and stopped-server guard | Explicit doctor repair | Rebuilt index, inferred edges, WAL checkpoint | Enforcing on direct local path | Recovery consistency, no endorsement; new edge relation assessed separately | May make existing content retrievable and add formal consequences | Doctor → content index/graph → later search/graph consumers | SRC-1 `src/cortex/cli/main.py` | none | none | No observed successful repair; default ten reasoning iterations is bounded |
| [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) | lineage/freshness/recovery | implemented | [EPI-OBJ-document-text](#epi-obj-document-text); [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | no content change | Edits, unlink/delete, temporal snapshot and restore | see [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) | see [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) | see [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) | Caller-selected mutation | No semantic rejection criterion established | Explicitly changes retained content/edges; no automatic cascaded warrant withdrawal shown | Handler → stores → later retrieval; see [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) | SRC-1 `src/cortex/transport/mcp/server.py` | none | none | Deleting an edge is not proof that all conclusions derived from it are withdrawn |

No route found within the inspected pipeline, presenters and maintenance handlers establishes lifecycle integration *after evidence-consuming truth acceptance*. Their graph linking is pre-acceptance organization, and formal derivation has only its conditional license. External human acceptance is not excluded. Uninspected relevant source prevents a system-complete negative.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-formal-intelligence](#epi-clm-formal-intelligence) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-rule-derivation](#epi-rte-rule-derivation), [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics), [EPI-RTE-period-synthesis](#epi-rte-period-synthesis); retrieval see runtime | None supplied | Source benchmark assertions are not observations or interventions | Typed retention, structural inference and presentation implemented | “Knowledge”/“intelligence” do not independently warrant outputs |
| [EPI-CLM-semantic-checks](#epi-clm-semantic-checks) | see record | SRC-1 `src/cortex/pipeline/advanced_reason.py`, doctrine/design | see record | [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics) | None supplied | Structural fixture F1 does not measure semantic conflict detection | Structural dependency warning supported | Semantic LLM comparison declared but not implemented by inspected detect_contradictions body |
| [EPI-CLM-retrieval-learning](#epi-clm-retrieval-learning) | see record | SRC-1 `src/cortex/retrieval/learner.py`, `llms.txt`, doctrine/design | see record | [EPI-RTE-access-adaptation](#epi-rte-access-adaptation) | None supplied | Usage frequency has no independent correctness reference; no compared outcome | Persistent counters and promotion wired | Automatic weight tuning and retrieval improvement not established |
| [RT-CLM-stage-resilience](runtime.md#rt-clm-stage-resilience) | see record | SRC-1 `src/cortex/pipeline/orchestrator.py`, doctrine/design | see record | [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) | None supplied | see record | Continuation not rejection/acceptance | Partial or complete labels cannot certify semantic quality |
| [RT-CLM-store-consistency](runtime.md#rt-clm-store-consistency) | see record | SRC-1 `src/cortex/db/store.py`, doctrine/design | see record | [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) | None supplied | see record | Path-specific snapshots and compensation | Direct updates qualify universal lineage/consistency interpretation |

## Bounded conclusion

Cortex admits externally supplied assertions before optional processing. Source warrant is unknown, not automatically preserved by a capture ID or channel. It retains and retrieves content and model/caller summaries through the routes in [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline), [RT-RTE-direct-import](runtime.md#rt-rte-direct-import) and [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). Delivery is informational, not evidence of host reliance: see [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery).

Model classification and synthesis request truth-apt interpretations, but no input/output evidence distinguishes faithful compression from new claims. Their structural gates do not test source truth. Metadata and relationships nevertheless become operationally available to search and inference: see [EPI-RTE-metadata-generation](#epi-rte-metadata-generation), [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-metadata-admission](#epi-rte-metadata-admission), [EPI-RTE-period-synthesis](#epi-rte-period-synthesis). Neither accepted ampliative knowledge nor post-acceptance lifecycle integration is established for these routes.

Four fixed rules derive graph propositions under explicit assumptions. Their license is conditional entailment over encoded premises, not independent warrant for those premises, causal explanations or semantic consistency. Derived edges are retained without a separate truth decision; additive closure does not establish automatic withdrawal after premise edits. See [EPI-RTE-rule-derivation](#epi-rte-rule-derivation), [EPI-RTE-rule-retention](#epi-rte-rule-retention). Structural diagnostics can warrant bounded pattern reports; “systemic issue” and “missing architecture” add conjectural interpretations that are not entailed by those patterns. Their force is advisory, and alerts are not automatic correction: see [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics).

Access feedback directly changes counters and tier metadata without a truth-apt theory update. It establishes a durable usage-to-metadata path, not calibrated correctness, automatic ranking optimization or improved future capacity. Doctor operations assess and repair indexes/closure, not propositions. Explicit edit, unlink, deletion and restore can change later reliance material but do not constitute a semantic acceptance protocol. See [EPI-RTE-access-adaptation](#epi-rte-access-adaptation), [EPI-RTE-health-check](#epi-rte-health-check), [EPI-RTE-health-repair](#epi-rte-health-repair), [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge).

The formal rules are localized and consumed, independently of whether they are criticized. The supplied [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) assesses those theory-builder conditions separately. No additional rule-criticism/revision loop is established here. Neither learning benefit, reflection, autonomous theory building nor exercised self-improvement follows from formal iteration or the access path. Distributed-parametric internals remain bounded by the separate [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer) and [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider) evidence. No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-document-text
Label: Document text

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

Natural-language title/content in SQLite with graph identity. Caller/importer supplies assertions, which can be true or false over caller domains; actual candidate units are not determinable without a corpus. Producer/retention/read-back and unknown authorship are supplied by [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) and [RT-RTE-direct-import](runtime.md#rt-rte-direct-import). This is the content part of the container, distinct from summaries and graph assertions. SRC-1 `src/cortex/db/store.py`; minimum storage passage supplied by [RT-OBJ-store](runtime.md#rt-obj-store).

#### EPI-OBJ-summary
Label: Summary

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

Natural-language summary in SQLite and graph properties. Caller summary, model summary and fallback title share a field but not a common derivation guarantee. NormalizeStage and BriefingPresenter consume it; fallback uses title, not verification of a proposition. Distinct material part from full content: it can reach context without its supporting body. SRC-1 `src/cortex/pipeline/normalize.py`; see [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context).

#### EPI-OBJ-graph-assertions
Label: Graph assertions

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

Symbolic predicate/endpoint triples in Oxigraph, interpreted by graph queries and fixed inference. Imported/caller and model-proposed edges coexist with rule-derived edges. The predicate causedBy is an asserted causal relation, not an experiment. Distinct from the shipped rule objects [RT-OBJ-inference-rules](runtime.md#rt-obj-inference-rules): these are their data and products. SRC-1 `src/cortex/pipeline/link.py`, `src/cortex/pipeline/reason.py`.

#### EPI-OBJ-classification
Label: Classification metadata

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

Symbolic type/project/entity associations, numerical confidence and tier/access configuration in SQLite and graph metadata. Consumption uses fixed comparisons and filters, not distributed model parameters. Parts share the retained metadata container but differ from document propositions; checks/admission versus access adaptation are split in route records. SRC-1 `src/cortex/services/llm.py`, `src/cortex/retrieval/learner.py`.

#### EPI-OBJ-diagnostic-result
Label: Diagnostic result

Natural-language messages plus symbolic type/severity/IDs/counts in returned Python dictionaries. Produced transiently by AdvancedReasoner or AlertPresenter, delivered through reason/status tools. No automatic persistence of these result dictionaries in inspected bodies. Distinct output part of [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) rather than that combined route itself; also overlaps retrieval presentation, so it is not a part of exactly one supplied record. SRC-1 `src/cortex/pipeline/advanced_reason.py`, `src/cortex/retrieval/presenters.py`.

#### EPI-OBJ-period-narrative
Label: Period narrative

Natural-language model prose or deterministic count summary, transient response string accompanied by symbolic themes and source descriptors. It is not automatically a stored object of type synthesis. Distinct output of synthesis within [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context); no supplied standalone object counterpart. SRC-1 `src/cortex/retrieval/presenters.py`.

Minimum passages for these material parts (SRC-1, implementation):

> existing_summary = doc.get("summary", "")
> --- `src/cortex/pipeline/normalize.py`

> graph_updates = {"summary": classification["summary"]}
> --- `src/cortex/pipeline/normalize.py`

> "confidence": float(data.get("confidence", 0.5)),
> --- `src/cortex/services/llm.py`

> "narrative": narrative,
> --- `src/cortex/retrieval/presenters.py`

### Routes

#### EPI-RTE-metadata-generation
Label: Metadata generation

Part of: [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Classification dictionary, or minimal fallback.
- Later read-back: Proposed summary and metadata can be written by normalization and reach later context calls.
- Delegated visibility: Classification model sees title and first 8000 content characters; relationship call sees new object title/type and first 4000 content characters plus up to 20 candidate titles/types/IDs; no worker delegation.
- Selection predicate: No existing summary; internal model requires availability.
- Invalidation or expiry: Rerun reuses existing summary rather than necessarily regenerating it.
- Activation or effect: Produces proposed interpretation, not an observed reliable semantic transformation.
- Evidence limits: No supplied classification response or expected-answer comparison.

The internal model proposes; Python requests type, summary, entities, properties and confidence. Stored caller summary skips this classification step, not necessarily relationship discovery. LLMClient.discover_relationships separately requests relations using new title/type, at most 4000 content characters and at most 20 existing object titles/types/IDs selected from recent candidates. Those titles do not supply full evidence for causal or contradiction assertions. Without a returned proposal and its source evidence, relationship meaning is indeterminate among reshaping, entailed derivation and conjecture; missing entailment evidence alone does not establish conjecture. Model processing is opaque; preservation, entailment and non-entailment of actual returned propositions are indeterminate. Fallback title copy is non-ampliative reshaping. This is generation within the supplied pipeline route, not another whole capture route. SRC-1 `src/cortex/services/llm.py`, `src/cortex/pipeline/normalize.py`.

> prompt = CLASSIFY_PROMPT.format(title=title, content=content[:8000])
> --- `src/cortex/services/llm.py`

> "summary": title,
> --- `src/cortex/services/llm.py`

> # Pre-classified at capture time — skip LLM, use stored data
> --- `src/cortex/pipeline/normalize.py`

#### EPI-RTE-structure-check
Label: Structure check

Part of: [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized dictionary or filtered relationships; errors trigger fallback/empty list.
- Later read-back: Only indirectly: admitted proposals can later be read.
- Delegated visibility: Same bounded model context as generation; validation itself is local code.
- Selection predicate: Parseable output; known types, entity categories/stopwords; relationship confidence >0.5, known predicate, different existing endpoints.
- Invalidation or expiry: Each completion/proposal is checked anew; no approval certificate.
- Activation or effect: Can reject malformed/low-confidence relationship proposals before graph writes.
- Evidence limits: Structural admissibility does not establish truth, semantic fidelity or confidence calibration.

Check targets are JSON syntax, known classification values and graph endpoint/predicate admissibility. Evaluators are json.loads, fixed Python conditions and SQLite existence queries. Domain is representation/graph structure, not whether an alleged root cause or contradiction is true. Python decides and vetoes, not a human per item. No answer oracle; mode is open capture. Classification invalid type becomes idea with capped confidence, while unsupported entity entries are filtered. Relationship parse failure returns no proposals; LinkStage can skip specific candidates. SRC-1 `src/cortex/services/llm.py`, `src/cortex/pipeline/link.py`.

> if result["type"] not in valid_types:
>     result["type"] = "idea"
>     result["confidence"] = min(result["confidence"], 0.3)
> --- `src/cortex/services/llm.py`

> and r.get("confidence", 0) > 0.5
> --- `src/cortex/services/llm.py`

> if from_id == to_id:
>     continue
> --- `src/cortex/pipeline/link.py`

> if not self.store.content.get(from_id) or not self.store.content.get(to_id):
> --- `src/cortex/pipeline/link.py`

#### EPI-RTE-metadata-admission
Label: Metadata admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized/linked/classified status and updates.
- Later read-back: SQLite summaries/types and graph metadata/edges feed later service calls and inference.
- Delegated visibility: No separate worker; model receives proposal context, caller reclassification is tool input.
- Selection predicate: Confidence >0 changes normalized type; summaries written regardless; structurally admitted edges; explicit classify accepts supplied nonempty fields.
- Invalidation or expiry: Edits/unlink/delete or later classification; automatic snapshots differ by path.
- Activation or effect: Writes metadata and relations without a semantic acceptance decision.
- Evidence limits: Status labels do not certify truth; graph write failures may be suppressed.

Distinct write/disposition function spanning [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) and [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge); not a second declaration of either complete route. Caller or optional internal model proposes. Fixed software decides; per-content human veto is not wired here, though callers may be human. Open request mode, no reference-answer oracle. Guidance is classification prompt and tool instruction to read before reclassifying; read-first is not checked by the handler. Caller classify assigns confidence 0.9 rather than consuming accuracy evidence. Recovery is explicit edits/deletion and path-specific snapshots, not rollback on semantic rejection. Retained edges are organization before acceptance, not evidence of lifecycle integration. SRC-1 `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/link.py`, `src/cortex/transport/mcp/server.py`.

> if classification["confidence"] > 0.0:
>     updates["type"] = classification["type"]
> --- `src/cortex/pipeline/normalize.py`

> self.store.content.update(obj_id, **updates)
> --- `src/cortex/pipeline/normalize.py`

> updates: dict[str, Any] = {"confidence": 0.9}
> --- `src/cortex/transport/mcp/server.py`

> created.append(rel)
> --- `src/cortex/pipeline/link.py`

#### EPI-RTE-rule-derivation
Label: Rule derivation

Part of: [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CONSTRUCT query result; rule counts reported by run.
- Later read-back: Derived triples can become premises and be read after retention; see rule-retention.
- Delegated visibility: inapplicable — local deterministic graph processing, no delegated model.
- Selection predicate: Four shipped query patterns with missing-edge filters.
- Invalidation or expiry: Rules static in code; edits to source/data can change results; no dependency lineage retraction in this method.
- Activation or effect: Derives conditional graph consequences, not checks of input truth.
- Evidence limits: Implementation deduction only; no observed graph or independently warranted premises.

This is the derivation part of ordinary/maintenance reasoning, distinct from retention below. A concrete symbolic input with edges A supersedes B and B supersedes C, A != C and no A supersedes C matches transitive_supersedes_1hop and constructs A supersedes C. This follows from the inspected query, conditional on the rule and exact encoded premises; no target execution is needed. Likewise causedBy inversion is not an independent causal discovery. Query failure returns zero, so zero inferred triples is not proof of successful closure. Owner is ReasonStage with fixed Python order, at most ten iterations by default. Rules propose formal consequences and software selects query matches; no answer oracle or per-triple human acceptance. Rule bodies are guidance, not revised products. For theory-builder conditions 1–4, addressability, persistence, learning, reflection and autonomy, see [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge): this part adds no criticism/revision mechanism. SRC-1 `src/cortex/pipeline/reason.py`.

> CONSTRUCT {{ ?a cortex:supersedes ?c }}
> WHERE {{
>     ?a cortex:supersedes ?b .
>     ?b cortex:supersedes ?c .
>     FILTER(?a != ?c)
>     FILTER NOT EXISTS {{ ?a cortex:supersedes ?c }}
> }}
> --- `src/cortex/pipeline/reason.py`

> for iteration in range(max_iterations):
> --- `src/cortex/pipeline/reason.py`

#### EPI-RTE-rule-retention
Label: Rule retention

Part of: [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Count of newly added graph triples.
- Later read-back: Retained Oxigraph edges feed graph queries and subsequent derivations across invocations.
- Delegated visibility: inapplicable — local backing-store mutation.
- Selection predicate: Constructed triple not already present.
- Invalidation or expiry: Explicit unlink/delete can remove edges; this additive method does not track premise-dependent withdrawal.
- Activation or effect: Direct graph additions, not truth acceptance or criticism.
- Evidence limits: No execution evidence or provenance chain distinguishing asserted from inferred edges in this method.

Owner ReasonStage._apply_rule admits formal query products after an existence check; software can veto duplicates, not semantically false premises. No human approval, answer oracle or independent evidence acceptance. Open graph maintenance guided by fixed rules; additions persist in graph, and explicit maintenance/recovery is separate. This retention part differs from both derivation and lifecycle integration after acceptance. SRC-1 `src/cortex/pipeline/reason.py`; behavioral force see [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution).

> if not existing:
>     self.graph._store.add(quad)
>     count += 1
> --- `src/cortex/pipeline/reason.py`

#### EPI-RTE-state-diagnostics
Label: State diagnostics

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lists of contradiction/pattern/gap/staleness findings or status alerts.
- Later read-back: inapplicable — these returned finding lists are not persisted by the inspected producer methods.
- Delegated visibility: Caller receives findings; no LLM invoked by detect_contradictions body.
- Selection predicate: Superseded node with dependents; ≥3 recent fixes per entity; type-presence gaps; stale dependency patterns.
- Invalidation or expiry: Computed anew on request over capped listings (advanced 1000; alerts 500).
- Activation or effect: Advisory reporting; no automatic withdrawal, correction or acceptance of challenged content.
- Evidence limits: Warnings may be incomplete and heuristic explanations exceed formal pattern evidence.

Distinct check/output functions spanning [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) and [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). AdvancedReasoner.run_all returns results; cortex_reason exposes it, cortex_status returns AlertPresenter output. Code selects matches and names hypotheses; caller can ignore them. There is no answer oracle or obligatory human decision after findings. Domain is current graph bookkeeping, not semantic truth of whole documents. Structural contradiction means superseded yet depended upon, not P and not-P detection. propagate_staleness returns warnings; it does not mutate dependent objects.

The heuristic claim “possible systemic issue” is ampliative: three fixes about Redis can correct three independent mistakes rather than one systemic cause. Missing decision objects does not entail missing architecture documentation elsewhere. AlertPresenter strengthens the label to “Systemic issue” without adding evaluation. This counterexample qualifies the inference rather than erasing the factual count. Chain assembly follows causedBy/ledTo edges with visited/depth limits; it cannot validate causation. SRC-1 `src/cortex/pipeline/advanced_reason.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/transport/mcp/server.py`.

> findings.extend(self._structural_contradictions())
> return findings
> --- `src/cortex/pipeline/advanced_reason.py`

> f"{window_days} days — possible systemic issue"
> --- `src/cortex/pipeline/advanced_reason.py`

> f"Systemic issue: {len(fix_ids)} fixes in 14 days "
> --- `src/cortex/retrieval/presenters.py`

> stats["alerts"] = alerts
> --- `src/cortex/transport/mcp/server.py`

#### EPI-RTE-period-synthesis
Label: Period synthesis

Part of: [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Themes, source descriptors and narrative string, or nothing_to_synthesize.
- Later read-back: inapplicable — this presenter returns a dictionary, not a persisted synthesis object.
- Delegated visibility: Internal completion sees title/type/summary of first 20 recent objects; response sources list first 30.
- Selection predicate: At most 500 listed project objects filtered by created_at cutoff; LLM available selects model branch.
- Invalidation or expiry: Recomputed per request; caller could capture separately but no automatic capture here.
- Activation or effect: Returns model prose or deterministic selected-set counts without post-generation acceptance.
- Evidence limits: No model output, fidelity comparison or host reliance trace; source list need not identify every counted object.

Explicit caller request triggers synthesis. Model proposes a narrative; successful completion is returned directly, exceptions choose fallback. No semantic veto or answer oracle. Mode is open query, not experiment. Prompt asks for a brief narrative, not corroboration against independent evidence. Retention/recovery inapplicable to transient result. Deterministic deduction: with selected recent objects of types fix, fix, lesson and no model, themes becomes fix:2, lesson:1; fallback says three objects captured plus those counts. This is entailed by selected metadata, not a novel lesson. The model alternative remains indeterminate without concrete source/output pairs. SRC-1 `src/cortex/retrieval/presenters.py`.

> themes[t] = themes.get(t, 0) + 1
> --- `src/cortex/retrieval/presenters.py`

> f"brief narrative (3-5 sentences):\n\n{summaries}"
> --- `src/cortex/retrieval/presenters.py`

> lines = [f"Over the past period, {len(objects)} objects were captured."]
> --- `src/cortex/retrieval/presenters.py`

#### EPI-RTE-access-adaptation
Label: Access adaptation

Part of: [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Read/feedback result and count, while access metadata persists.
- Later read-back: Counters/last-access config keys and changed tier survive; briefing returns tier (see runtime retrieval record).
- Delegated visibility: Caller relevance boolean is input, not a separate critic worker.
- Selection predicate: Read or positive feedback increments; threshold of ten accesses permits promotion.
- Invalidation or expiry: Counts accumulate; tier can later change by edits or explicit maintenance.
- Activation or effect: Trace-fed tier change is wired; later host behavior or better retrieval not observed.
- Evidence limits: No identified truth-apt improvement claim produced; no automatic trained parameters or ranking tuner established.

Caller supplies relevance, or read generates an implicit access event. Code decides threshold/promotion; no human per-item approval inside the write. The independent target would be retrieval usefulness, but access frequency alone does not test it. No expected-answer oracle or bounded experiment. Guidance is fixed promotion threshold; durable product is counters/time/tier, not a criticized theory. Record scope is automatic access path, not all helper APIs. Search in src/, .github/ and pyproject.toml finds only helper definitions for detect_miss, adjust_tiers and get_weights; update_weights has the reset helper call. Retrieval construction supplied by runtime uses defaults rather than loading these persisted weights. Thus get/set APIs do not establish an exercised or automatic ranking adaptation loop. SRC-1 `src/cortex/retrieval/learner.py`; closest container [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context).

> if current + 1 >= 10:
>     self._maybe_promote(obj_id)
> --- `src/cortex/retrieval/learner.py`

> self.store.content.update(obj_id, tier="reflex")
> --- `src/cortex/retrieval/learner.py:134-134`

> return subsequent_read_id not in context_result_ids
> --- `src/cortex/retrieval/learner.py`

#### EPI-RTE-health-check
Label: Health check

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Terminal health messages and suggestions; missing stores abort.
- Later read-back: inapplicable — diagnostic results are printed, not retained by doctor_check.
- Delegated visibility: inapplicable — direct local checks, no model/delegation.
- Selection predicate: Explicit doctor check; missing stores, FTS report and pending rule counts; locked graph may skip.
- Invalidation or expiry: Checks rerun on request against current stores.
- Activation or effect: Reports warnings and suggests repair; no automatic repair invocation.
- Evidence limits: FTS helper body not independently assessed; zero pending can hide rule query errors.

New direct-CLI diagnostic omitted from the supplied runtime detail; related but distinct from [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge). Owner doctor_check calls content.fts_integrity_check and ReasonStage.check_fixpoint. The target/domain is index consistency and missing rule consequences. Neither check licenses truth of document content. Query failure in check_fixpoint assigns zero and continues, while ok is total_pending == 0; therefore all failing rules can still produce an OK closure result. Source-level countercase, not observed failure. Operator decides whether to repair; no answer oracle for knowledge admission. SRC-1 `src/cortex/cli/main.py`, `src/cortex/pipeline/reason.py`.

> typer.echo("              Run `cortex doctor repair` to rebuild.")
> --- `src/cortex/cli/main.py`

> rule_counts[rule["name"]] = 0
> continue
> --- `src/cortex/pipeline/reason.py`

> "ok": total_pending == 0,
> --- `src/cortex/pipeline/reason.py`

#### EPI-RTE-health-repair
Label: Health repair

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed rebuild/inference/checkpoint results, or refusal if server detected running.
- Later read-back: Rebuilt index and new graph edges affect later retrieval/graph consumers.
- Delegated visibility: inapplicable — direct local code, no delegated worker.
- Selection predicate: Explicit doctor repair; process check, SQLite existence, optional graph existence.
- Invalidation or expiry: No semantic candidate expiry; backup/restore is a separate recovery mechanism.
- Activation or effect: Calls FTS rebuild, bounded ReasonStage.run and WAL checkpoint.
- Evidence limits: No exercise or rollback evidence; printed fixpoint label is stronger than a bounded loop guarantees.

New direct maintenance route related to, but not a duplicate of, [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge). Operator proposes repair, software may reject detected running server or missing SQLite; mode is open maintenance without per-triple approval or truth oracle. Guidance is fixed repair sequence. Index rebuild retains the same input assertions; reasoning adds conditional consequences as separately assessed above. No semantic truth acceptance or automatic criticism retention. Reasoner run defaults to ten iterations, while CLI prints “fixpoint” from returned iteration count without separately confirming closure. Recovery is not a semantic rejection gate. SRC-1 `src/cortex/cli/main.py`, `src/cortex/pipeline/reason.py`.

> result = content.fts_rebuild()
> --- `src/cortex/cli/main.py`

> f"(fixpoint in {result['iterations']} iteration(s))"
> --- `src/cortex/cli/main.py`

### Claims

#### EPI-CLM-formal-intelligence
Label: Formal intelligence

No supplied claim counterpart: the supplied resilience/consistency claims concern different operations. Cortex's README describes capture, classification, relationship discovery, graph reasoning and serving intelligence. This warrants checking routes, not attributing infallibility or an acceptance protocol. SRC-1 `README.md`, doctrine/design.

> Cortex captures knowledge objects (decisions, lessons, fixes, sessions, research, ideas), classifies them with an OWL-RL ontology, discovers relationships, reasons over the graph, and serves intelligence through hybrid retrieval.
> --- `README.md`

The source benchmark tests are implementation evidence of evaluator design only. Scoped searches in SRC-1 `benchmarks/b4_graph_intelligence/test_bench.py` show fixture-node membership/order assertions for causal chains; these evaluate traversal against inserted edges, not whether real causes were correctly inferred. SRC-1 `benchmarks/b5_pattern_detection/test_bench.py` evaluates matching fixture-defined frequency/window/gap criteria. No results or independent component intervention supplied.

> assert a_id in ids, "Root cause A must be in chain"
> --- `benchmarks/b4_graph_intelligence/test_bench.py`

#### EPI-CLM-semantic-checks
Label: Semantic contradiction checks

No supplied standalone claim counterpart; related discrepancy already noted in [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge). The AdvancedReasoner module and method docstrings declare semantic LLM-compared conflict detection. Its inspected detect_contradictions body calls only structural checks. This is doctrine beyond implemented route coverage, not an access gap. SRC-1 `src/cortex/pipeline/advanced_reason.py`, doctrine/design versus implementation.

> - Semantic contradictions (LLM-compared content)
> --- `src/cortex/pipeline/advanced_reason.py`

The structural implementation passage is retained in [EPI-RTE-state-diagnostics](#epi-rte-state-diagnostics). A source benchmark asserts F1 for its selected contradiction fixtures; that assertion is neither a run nor evidence for unimplemented semantic comparison. SRC-1 `benchmarks/b3_contradiction/test_bench.py`, implementation evaluator design.

> assert scores["f1"] == 1.0, (
> --- `benchmarks/b3_contradiction/test_bench.py`

#### EPI-CLM-retrieval-learning
Label: Retrieval learning

No supplied standalone claim counterpart; closest supplied mechanism is [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). Learner module claims usage-based retrieval improvement and ranking-weight tuning; agent instructions label relevance feedback retrieval learning. Source implements counters/promotion and weight persistence helpers; callers searched in [EPI-RTE-access-adaptation](#epi-rte-access-adaptation) do not establish automatic tuning. Source alone establishes neither improved capacity nor actual task benefit. SRC-1 `src/cortex/retrieval/learner.py`, `llms.txt`, doctrine/design.

> Learns from usage patterns to improve retrieval over time:
> --- `src/cortex/retrieval/learner.py`

> - Tunes ranking weights based on feedback
> --- `src/cortex/retrieval/learner.py`

> Provide explicit relevance feedback for retrieval learning.
> --- `llms.txt`

### Components

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
