---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "REM's content generation, reliance, evaluation and withdrawal routes at its frozen source boundary."
run-id: AAS-2026-10-14-rem-a81fdc774400-01
reviewed-boundary: "935e8be0a1fca5b23dbabfe16c48b562c1cd24cc"
---

# REM epistemic report

## Source-and-claim boundary

The question is how REM obtains truth-apt content, checks it and licenses later reliance. Scope and dependency exclusions are see [boundary](boundary.md#boundary-and-evidence); the evidence identity is SRC-1 in its [Source register](boundary.md#source-register). All new findings use implementation or doctrine/design from that source. No target execution, provider response, benchmark result or causal comparison was supplied or produced. Thus accuracy, semantic preservation in actual model outputs, actual host compliance and improved capacity remain unestablished. Provider weights are opaque; the model versions and parameter mutability findings are see [RT-CMP-parse-service](runtime.md#rt-cmp-parse-service), [RT-CMP-consolidation-engine](runtime.md#rt-cmp-consolidation-engine) and [RT-CMP-embed-service](runtime.md#rt-cmp-embed-service).

The supplied runtime is provisional, not an inspection limit. This report directly checked exposed Python operations, Go routing, engine and helper implementations, storage read filters, graph traversal, benchmark dispatch, evaluators and cleanup. No supplied runtime finding requires supersession: the direct correctly shaped consolidation input is a countercase to a claim that the engine cannot generate candidates at all, not to the runtime's narrower write-back finding.

| Entry point or operation | SRC-1 source path | Coverage and supporting records | Limit or conclusion prevented |
|---|---|---|---|
| Episode write, get/list; caller admission | `go-api/internal/api/router.go`; `go-api/internal/services/write_service.go`; `go-api/internal/domain/episode.go` | Direct reads; handler/storage progression also supplied by [RT-RTE-episode-write](runtime.md#rt-rte-episode-write) | Static admission is not truth acceptance; successful deployed storage unobserved |
| Python `/parse` | `python-worker/api/router.py`; `python-worker/api/handlers/parse.py`; `python-worker/services/parse_service.py` | Direct complete reads; [EPI-OBJ-parse-fields](#epi-obj-parse-fields) | Model interpretations unavailable |
| Python `/embed`, cache and batch helper | `python-worker/api/handlers/embed.py`; `python-worker/services/embed_service.py` | Direct complete reads; [RT-CMP-embed-service](runtime.md#rt-cmp-embed-service) | Vectors are selection machinery, not individuated propositions; provider behavior uninspected |
| Python `/consolidate` and Celery tasks | `python-worker/main.py`; `python-worker/api/handlers/consolidate.py`; `python-worker/workers/tasks.py`; `python-worker/services/consolidation/engine.py` | Direct complete reads; [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction), [EPI-RTE-candidate-filter](#epi-rte-candidate-filter); scheduler/publication also supplied by [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation) | No observed generation or durable write-back |
| Alternative compressor, clusterer and LLM wrapper | `python-worker/services/consolidation/compressor.py`; `python-worker/services/consolidation/clusterer.py`; `python-worker/services/llm_service.py` | Direct complete reads and caller search; [EPI-RTE-compressor-helper](#epi-rte-compressor-helper) | Callable helpers are not established exposed routes; no model response |
| Retrieval and semantic listing | `go-api/internal/services/retrieve_service.go`; `go-api/internal/db/qdrant/client.go`; `go-api/internal/db/postgres/semantic.go`; `go-api/internal/api/handlers/semantic.go` | Direct complete reads; [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve), [EPI-RTE-retrieval-feedback](#epi-rte-retrieval-feedback), [EPI-ABS-semantic-withdrawal](#epi-abs-semantic-withdrawal) | Actual retained semantic content and its initial provenance uninspected |
| Graph service and traversal | `go-api/internal/services/graph_service.go`; `go-api/internal/db/neo4j/client.go` | Direct complete reads; [EPI-CLM-causal-graph](#epi-clm-causal-graph) | Temporal adjacency is not causal evidence |
| SDK, LangChain and AutoGen before/after hooks | `sdk/python/rem_memory/client.py`; `sdk/python/rem_memory/integrations/langchain.py`; `sdk/python/rem_memory/integrations/autogen.py` | Supplied findings: [RT-RTE-host-integration](runtime.md#rt-rte-host-integration), [RT-BAP-context-injection](runtime.md#rt-bap-context-injection) | Host activation and framework behavior unobserved |
| Seed and process startup | `scripts/seed_demo.py`; `Makefile` | Supplied findings: [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation), [RT-ABS-worker-bridge](runtime.md#rt-abs-worker-bridge) | Shipped invocation does not establish successful consolidation |
| Benchmark CLI, all three evaluators and adapter/reset | `benchmarks/run_all.py`; `benchmarks/longmemeval.py`; `benchmarks/locomo.py`; `benchmarks/convomem.py`; `benchmarks/adapters/rem_adapter.py` | Direct complete reads; [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation), [EPI-RTE-benchmark-cleanup](#epi-rte-benchmark-cleanup) | No results; synthetic references do not establish official-dataset performance |
| Public knowledge claims | `README.md`; `dashboard/src/lib/config.tsx` | README complete and FAQ bounded direct read; [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop), [EPI-CLM-recursive-memory](#epi-clm-recursive-memory), [EPI-CLM-causal-graph](#epi-clm-causal-graph), [EPI-CLM-recall-performance](#epi-clm-recall-performance) | Marketing wording is doctrine/design, not measurement |
| Authentication and remaining presentation/setup surfaces | `go-api/internal/api/middleware/auth.go`; `docs/api-reference.md`; `docs/quickstart.md`; `dashboard/src/app/page.tsx` | Authentication supplied by [RT-RTE-key-admission](runtime.md#rt-rte-key-admission); remaining surfaces only boundary inspection/search | Not a comprehensive UI, deployment or security audit; no system-complete negative beyond the named executable route searches |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw-content](#epi-obj-raw-content) | see record | see record | SRC-1 `go-api/internal/domain/episode.go` | see record |
| [EPI-OBJ-parse-fields](#epi-obj-parse-fields) | see record | see record | SRC-1 `python-worker/services/parse_service.py` | see record |
| [EPI-OBJ-semantic-candidate](#epi-obj-semantic-candidate) | see record | see record | SRC-1 `python-worker/services/consolidation/engine.py` | see record |
| [EPI-OBJ-semantic-result](#epi-obj-semantic-result) | see record | see record | SRC-1 `go-api/internal/services/retrieve_service.go` | see record |
| [RT-CMP-parse-service](runtime.md#rt-cmp-parse-service) | Parametric truth-apt content not determinable | see record | SRC-1 `python-worker/services/parse_service.py` | Provider internals and individual propositions inaccessible |
| [RT-CMP-consolidation-engine](runtime.md#rt-cmp-consolidation-engine) | Parametric truth-apt content not determinable | see record | SRC-1 `python-worker/services/consolidation/engine.py` | Provider internals and individual propositions inaccessible |
| [EPI-CMP-benchmark-judge](#epi-cmp-benchmark-judge) | Parametric truth-apt content not determinable | see record | SRC-1 `benchmarks/longmemeval.py` | Provider internals inaccessible; output judgments unobserved |
| [RT-CMP-embed-service](runtime.md#rt-cmp-embed-service) | No individuated proposition established in opaque weights or dense vectors | see record | SRC-1 `python-worker/services/embed_service.py` | Parametric truth-apt content not determinable; selection use is implemented |
| [EPI-OBJ-benchmark-results](#epi-obj-benchmark-results) | see record | see record | SRC-1 `benchmarks/longmemeval.py` | see record |

## Authority-route ledger

The ledger separates functions even where one runtime container carries several. Foreign-owned fields say see; this report owns the architectural status and epistemic classification.

Route ID: [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw-content](#epi-obj-raw-content)
Content/update relation: truth-apt transformation: acquisition/import; raw caller description preserved, source warrant unknown.
Transition or check target: see route record.
Evaluator/condition and domain: see route record; no source-truth oracle.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: retention eligibility, not endorsement.
Epistemic authority and scope: Records what the caller submitted; does not license the truth of the described event.
Operational authority: behavior permitted, blocked, or changed: see route record.
Behavioral-authority path: see [RT-BAP-context-injection](runtime.md#rt-bap-context-injection).
Evidence source ID and local anchor: SRC-1 `go-api/internal/domain/episode.go`
Claim IDs: [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop)
Mismatch marker: none.
Gap/limit: Caller authorship and event truth uninspected.

Route ID: [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-parse-fields](#epi-obj-parse-fields)
Content/update relation: truth-apt transformation: indeterminate; extraction may preserve explicit content or introduce an interpretation not entailed by it. Actual paired inputs/outputs are needed to decide.
Transition or check target: see object record.
Evaluator/condition and domain: see object record and [RT-CMP-parse-service](runtime.md#rt-cmp-parse-service).
Activation and timing: see route record.
Possible or observed result: see object record.
Implemented force: Proposed metadata can become stored classification and later clustering input.
Epistemic authority and scope: No checked semantic fidelity; generated intent is an interpretation, not evidence of the agent's actual objective.
Operational authority: behavior permitted, blocked, or changed: see route record.
Behavioral-authority path: Stored metadata to engine domain/intent selector on later consolidation; symbolic selection force, conditional on compatible serialization.
Evidence source ID and local anchor: SRC-1 `python-worker/services/parse_service.py`
Claim IDs: [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop)
Mismatch marker: Parser accuracy is requested, not verified.
Gap/limit: No returned provider output; defaults can occupy the same fields as extracted metadata.

Route ID: [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw-content](#epi-obj-raw-content), [EPI-OBJ-parse-fields](#epi-obj-parse-fields)
Content/update relation: no content change
Transition or check target: see route record and parse object.
Evaluator/condition and domain: Software structural admission, not proposition accuracy; see route record.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: Enforces request/dependency admission; nonempty parse fields and range-valid importance may overwrite defaults.
Epistemic authority and scope: Operational admission only; no evidence-consuming acceptance criterion for a knowledge claim.
Operational authority: behavior permitted, blocked, or changed: see route record.
Behavioral-authority path: Go handler/service checks to storage progression; permissive/enforcing force, current request.
Evidence source ID and local anchor: SRC-1 `go-api/internal/services/write_service.go`
Claim IDs: none.
Mismatch marker: Stored status is not epistemic acceptance.
Gap/limit: Per-content human approval unresolved for generic caller.

Route ID: [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-episode](runtime.md#rt-obj-episode)
Content/update relation: no content change
Transition or check target: see route record.
Evaluator/condition and domain: see route record.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: Sequential persistence, not accepted-claim lifecycle integration.
Epistemic authority and scope: Retention preserves availability but adds no warrant.
Operational authority: behavior permitted, blocked, or changed: see route record.
Behavioral-authority path: see [RT-BAP-context-injection](runtime.md#rt-bap-context-injection).
Evidence source ID and local anchor: SRC-1 `go-api/internal/services/write_service.go`
Claim IDs: [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop)
Mismatch marker: none.
Gap/limit: Partial-store effects and later use are see route record.

Route ID: [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: truth-apt transformation: indeterminate; requested durable facts may be extraction, reshaping or ampliative generalization. No actual output establishes non-entailment or semantic preservation.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: Candidate production, not warrant for durable rules; attached cluster IDs do not certify per-fact support.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `python-worker/services/consolidation/engine.py`
Claim IDs: [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop), [EPI-CLM-recursive-memory](#epi-clm-recursive-memory)
Mismatch marker: Full-cluster evidence count exceeds model-visible input for large clusters.
Gap/limit: see record.

Route ID: [EPI-RTE-candidate-filter](#epi-rte-candidate-filter)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: no content change
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: Nonempty fact plus numeric conversion licenses candidate return, not truth or suitability for reliance.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `python-worker/services/consolidation/engine.py`
Claim IDs: [EPI-CLM-recursive-memory](#epi-clm-recursive-memory)
Mismatch marker: No confidence threshold or evidence entailment test.
Gap/limit: see record.

Route ID: [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-semantic-candidate](#epi-obj-semantic-candidate)
Content/update relation: no content change
Transition or check target: see route record.
Evaluator/condition and domain: see route record.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: HTTP attempt exists; completed semantic admission is not wired, see [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes).
Epistemic authority and scope: Neither durable candidate admission nor accepted knowledge integration follows from returned candidate dictionaries.
Operational authority: behavior permitted, blocked, or changed: see route record.
Behavioral-authority path: Proposed semantic writes to future retrieval, not a completed shipped handoff.
Evidence source ID and local anchor: SRC-1 `python-worker/workers/tasks.py`
Claim IDs: [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop)
Mismatch marker: Unregistered POST/PATCH consumers.
Gap/limit: Direct database loading remains possible; it is not this route.

Route ID: [EPI-RTE-compressor-helper](#epi-rte-compressor-helper)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: truth-apt transformation: indeterminate; generated text unavailable, extraction versus generalization unresolved.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: Candidate helper only, no warranted fact admission.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `python-worker/services/consolidation/compressor.py`
Claim IDs: none.
Mismatch marker: This is not the active engine implementation.
Gap/limit: see record.

Route ID: [EPI-RTE-compressor-helper](#epi-rte-compressor-helper)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: truth-apt transformation: indeterminate; structural sanitization includes arbitrary clipping at 300 characters, which does not establish semantic preservation. Depending on the proposed text, the edge may preserve a proposition or remove a qualification and change it; paired full and clipped content with a checked interpretation is needed to classify that edge.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: Bounds/types only; no check of what the candidate says.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `python-worker/services/consolidation/compressor.py`
Claim IDs: none.
Mismatch marker: Structural validation is not truth acceptance.
Gap/limit: see record.

Route ID: [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw-content](#epi-obj-raw-content), [EPI-OBJ-semantic-result](#epi-obj-semantic-result).
Content/update relation: truth-apt transformation: non-ampliative reshaping; selection and formatting, not a new factual inference.
Transition or check target: see route record.
Evaluator/condition and domain: see route record; similarity/recency/popularity target relevance, not truth.
Activation and timing: see route record.
Possible or observed result: see route record.
Implemented force: see [RT-BAP-context-injection](runtime.md#rt-bap-context-injection).
Epistemic authority and scope: Advisory contextual reliance; learned-fact label and confidence convey no independently checked license.
Operational authority: behavior permitted, blocked, or changed: see route record.
Behavioral-authority path: see [RT-BAP-context-injection](runtime.md#rt-bap-context-injection).
Evidence source ID and local anchor: SRC-1 `go-api/internal/services/retrieve_service.go`
Claim IDs: [EPI-CLM-causal-graph](#epi-clm-causal-graph)
Mismatch marker: Source episode IDs absent from displayed fact line; withdrawal flags not selection criteria, see [EPI-ABS-semantic-withdrawal](#epi-abs-semantic-withdrawal).
Gap/limit: A selected fact's originating route and warrant are unknown; semantic writer gaps do not erase this conditional read capability.

Route ID: [EPI-RTE-retrieval-feedback](#epi-rte-retrieval-feedback)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: non-truth-apt policy/content update: retrieval-count changes future episode ranking.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: None for accuracy; retrieval frequency is not an outcome evaluation.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `go-api/internal/services/retrieve_service.go`
Claim IDs: [EPI-CLM-recursive-memory](#epi-clm-recursive-memory)
Mismatch marker: none.
Gap/limit: No demonstrated improved capacity or exercised self-improvement.

Route ID: [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: truth-apt transformation: entailed derivation; arithmetic/string predicates over supplied response text and source-native references, not real-world source truth.
Transition or check target: Deterministic response predicates and timing; see record.
Evaluator/condition and domain: Software substring/token-set/snippet predicates and timing over synthetic references; see record.
Activation and timing: see record.
Possible or observed result: Deterministic scores; see record.
Implemented force: see record.
Epistemic authority and scope: License only the recorded predicate/arithmetic metric over those inputs, not semantic correctness or source truth.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `benchmarks/longmemeval.py`
Claim IDs: [EPI-CLM-recall-performance](#epi-clm-recall-performance)
Mismatch marker: Retrieves context, not a host answer; no acceptance/adaptation consumer.
Gap/limit: No actual scores or causal support supplied.

Route ID: [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: truth-apt transformation: indeterminate; model judgment unavailable, so agreement with the reference cannot be established.
Transition or check target: Optional LongMemEval question/reference/injection-text judgment; see record.
Evaluator/condition and domain: see [EPI-CMP-benchmark-judge](#epi-cmp-benchmark-judge) and route record.
Activation and timing: Optional USE_LLM_JUDGE branch; see record.
Possible or observed result: Boolean judgment or false on exception; see record.
Implemented force: Saved/displayed metric only; see record.
Epistemic authority and scope: Uncalibrated model assessment of the supplied triple; no verified answer or production acceptance.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: Benchmark aggregate/file/display, advisory force over the probe run; no production consumer.
Evidence source ID and local anchor: SRC-1 `benchmarks/longmemeval.py`
Claim IDs: [EPI-CLM-recall-performance](#epi-clm-recall-performance)
Mismatch marker: A model reply starting Y and an exception false are both scoring inputs, not independent truth evidence.
Gap/limit: No judgment output or accuracy calibration supplied.

Route ID: [EPI-RTE-benchmark-cleanup](#epi-rte-benchmark-cleanup)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: no content change
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: Attempted reset does not achieve wired removal.
Epistemic authority and scope: No license to treat subsequent probes as fresh isolated conversations under one agent.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `benchmarks/adapters/rem_adapter.py`
Claim IDs: [EPI-CLM-recall-performance](#epi-clm-recall-performance)
Mismatch marker: Consumer IDs and endpoint registration do not support deletion.
Gap/limit: No reset run observed.

Route ID: [EPI-ABS-semantic-withdrawal](#epi-abs-semantic-withdrawal)
Route function: lifecycle integration
Architectural status: no route found within boundary
Object/candidate ID: Semantic claims.
Content/update relation: no content change
Transition or check target: Accepted proposition and evidence-consuming admission for an intended use.
Evaluator/condition and domain: No such evaluator found in the named search boundary; see absence record.
Activation and timing: No activation established.
Possible or observed result: No accepted-claim integration established.
Implemented force: No evidenced acceptance-to-integration handoff.
Epistemic authority and scope: Retention, IDs, retrieval and flags alone do not establish acceptance.
Operational authority: behavior permitted, blocked, or changed: None established for this function.
Behavioral-authority path: None established for acceptance/integration; contextual delivery separately implemented.
Evidence source ID and local anchor: SRC-1 `python-worker/services/consolidation/engine.py`
Claim IDs: [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop)
Mismatch marker: Operational candidate use is not accepted knowledge integration.
Gap/limit: Bounded inspected route absence, not a verdict on opaque provider internals or an operator-added process.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-episode-write](runtime.md#rt-rte-episode-write), [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction), [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) | None supplied | No intervention; [RT-ABS-worker-bridge](runtime.md#rt-abs-worker-bridge), [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes) | Components exist, not completed durable semantic loop | Stored/generated is not accepted true |
| [EPI-CLM-recursive-memory](#epi-clm-recursive-memory) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction), [EPI-RTE-retrieval-feedback](#epi-rte-retrieval-feedback) | None supplied | No semantic successor evaluation or efficacy comparison | Candidate extraction and popularity feedback are distinct capacities | Recursive semantic revision and first-class forgetting unestablished |
| [EPI-CLM-causal-graph](#epi-clm-causal-graph) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) | None supplied | Temporal edges do not identify causes | Context expansion is implemented | No causal warrant for selected explanation or rule |
| [EPI-CLM-recall-performance](#epi-clm-recall-performance) | see record | SRC-1 `dashboard/src/lib/config.tsx`, doctrine/design | see record | [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | None supplied | Synthetic samples; no intervention or official-dataset results | Evaluator code can measure limited response predicates | 81.6% and sub-50ms unsupported by admitted evidence |

## Bounded conclusion

REM imports descriptions and can retain raw text and model-interpreted metadata for later selection. Source warrant is unknown, although raw text is preserved by the write construction. Parser outputs are not independently checked for factual fidelity. Structural admission can proceed with default metadata; this is useful availability behavior, not endorsement. See [EPI-OBJ-raw-content](#epi-obj-raw-content), [EPI-OBJ-parse-fields](#epi-obj-parse-fields) and [RT-RTE-episode-write](runtime.md#rt-rte-episode-write).

The active engine requests durable factual candidates from selected and truncated episodes. Exact content-edge classification remains indeterminate without provider outputs: explicit preference extraction and novel recurring-rule conjecture are different possible results. There is no basis for counting all generated statements as either entailed derivations or produced accepted ampliative claims. Returned confidence is model-supplied; evidence counts and source IDs are software attachments to the whole cluster, not checked support for each proposition. Candidate rejection is empty output/nonempty-fact filtering and dependency handling, not semantic falsification. Direct lowercase-key requests can reach this computation even where fetched Go episodes cannot form intended clusters. See [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction), [EPI-RTE-candidate-filter](#epi-rte-candidate-filter) and [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation).

The task attempts retention but lacks accepting write-back routes. No evidence-consuming acceptance decision naming a truth criterion, intended use and scope was found in the inspected material loop; no accepted-claim lifecycle integration or operative contradiction withdrawal follows from flags or lineage IDs. This conclusion is local to the search in [EPI-ABS-semantic-withdrawal](#epi-abs-semantic-withdrawal). It does not deny the implemented ability to retrieve externally present semantic payload. Delivery to a host is advisory: raw episodes and learned-fact/confidence lines can affect a later prompt, but actual obedience or benefit is unknown. Temporal graph expansion and vector/ranking selection add relevance machinery, not factual or causal warrant. See [RT-BAP-context-injection](runtime.md#rt-bap-context-injection), [EPI-CLM-causal-graph](#epi-clm-causal-graph).

Retrieval-count feedback directly changes ranking without a truth-apt update or outcome check. This is implemented behavior adaptation, independent of whether knowledge production succeeds. Learning as improved capacity, reflection as a two-directional self-representation path, and exercised self-improvement are not demonstrated by these counts or static extraction requests. No content-directed criticism/retained method revision is established in the inspected engine and helpers; opaque model processing is not treated as an evidenced absence. See [EPI-RTE-retrieval-feedback](#epi-rte-retrieval-feedback), [EPI-RTE-compressor-helper](#epi-rte-compressor-helper). The alternative compressor's numeric/enum sanitization remains implemented, but its arbitrary fact clipping is not a semantic-preservation check. Its content edge remains indeterminate; the short sanitation example does not license a general reshaping finding.

Benchmarks supply actual reference strings and implement bounded checkers, unlike production routes. They evaluate answer-string presence/token overlap in retrieved context, not truthful downstream task completion. Their result consumer saves and displays scores; it does not accept, revise, withdraw or rank production memories. Cleanup cannot establish fresh per-conversation state through the shipped endpoints. No benchmark output or causal intervention licenses performance or component-effect claims. The supplied runtime also withholds fresh-install readiness: the unapplied migration repeats an episode trigger, its transactional runner returns the error, and main treats migration failure as fatal. Default benchmarks generate agent IDs without creating rows required by the episode foreign key. Externally prepared migrations and caller-supplied registered agents are different conditions, not demonstrated default setup. See [RT-RTE-episode-write](runtime.md#rt-rte-episode-write) and [Runtime account](runtime.md#runtime-account). See [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation), [EPI-RTE-benchmark-cleanup](#epi-rte-benchmark-cleanup), [EPI-CLM-recall-performance](#epi-clm-recall-performance).

## Shared records

### Components

#### EPI-CMP-benchmark-judge
Label: Optional benchmark judge

Distinct role from [RT-CMP-parse-service](runtime.md#rt-cmp-parse-service), despite the same provider alias: benchmark-local OpenAI `gpt-4o-mini` judges question/reference/retrieved-text triples. Distributed-parametric representation in opaque provider weights; no local parameter update. Exact version unpinned; alias may resolve to another version. No output or calibration supplied. SRC-1 `benchmarks/longmemeval.py`, implementation.

> model="gpt-4o-mini",
> --- `benchmarks/longmemeval.py`

### Operative objects

#### EPI-OBJ-raw-content
Label: Episode raw content
Part of: [RT-OBJ-episode](runtime.md#rt-obj-episode)

Source-native `Episode.RawContent`: natural-language task/interaction description, PostgreSQL row text. The truth-apt candidate is the described event, preference or utterance over the caller's task scope. A record of asserted content is not proof of that content. The caller is the producer; retrieval/injection and consolidation are later consumers. This part differs from model-produced parse fields in lineage and warrant. SRC-1 `go-api/internal/domain/episode.go`, implementation.

> RawContent:      req.Content,
> --- `go-api/internal/domain/episode.go`

#### EPI-OBJ-parse-fields
Label: Episode parsed fields
Part of: [RT-OBJ-episode](runtime.md#rt-obj-episode)

Source-native intent/entities/domain/emotion/importance fields. Natural-language intent and entity names plus symbolic categorization/numeric importance; retained in PostgreSQL and selected vector payload. Candidate content includes what the task aimed to do and what sentiment/domain it had. Importance is an operational recommendation rather than an independently checked fact. Producer: parser model or defaults; consumer: Go write and later engine clustering. Parser requests concise accurate extraction but checks JSON/conversion, not correspondence with evidence. Pydantic checks response types; Go accepts nonempty text and range-valid importance. Prompt enum/length guidance is not the implemented truth gate. No paired response evidence permits deciding faithful reshaping versus added interpretation. SRC-1 `python-worker/services/parse_service.py`, `python-worker/api/handlers/parse.py`, `go-api/internal/services/write_service.go`, implementation.

> "You are an AI memory parser. Extract structured information from "
> "agent episode descriptions. Be concise and accurate. "
> "Always return valid JSON only, no markdown, no explanation."
> --- `python-worker/services/parse_service.py`

> if parsed.ImportanceScore >= 0 && parsed.ImportanceScore <= 1 {
> episode.ImportanceScore = parsed.ImportanceScore
> }
> --- `go-api/internal/services/write_service.go`

#### EPI-OBJ-semantic-candidate
Label: Semantic memory candidate

Source-native engine dictionary `fact`, `confidence`, `fact_type`, `domain`, `evidence_count`, `source_episode_ids`; natural-language proposed fact plus symbolic annotations, request-local Python objects/JSON. Distinct from [RT-OBJ-episode](runtime.md#rt-obj-episode): it can summarize or generalize several episodes, not merely name that envelope. Runtime's [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation) declares a computation, not this output object; no supplied object counterpart after comparison. Truth-apt candidates concern user preferences, patterns, errors, skills and recurring rules. Model produces text/confidence; code adds full-cluster lineage. Go semantic storage/read structures are potential later representations, not evidence that these candidate instances were retained. SRC-1 `python-worker/services/consolidation/engine.py`, implementation.

> "evidence_count": len(source_ids),
> "source_episode_ids": source_ids,
> --- `python-worker/services/consolidation/engine.py`

#### EPI-OBJ-semantic-result
Label: Retrieved semantic result

Source-native Qdrant semantic payload mapped to Go `SemanticResult` and injection text; natural-language `Fact` plus symbolic confidence/type/domain/evidence count/score, stored payload then request-local response/string. Truth-apt part is the retrieved fact over its purported domain. Producer provenance and initial warrant are unknown: no actual stored instance or trace supplied. Distinct from [EPI-OBJ-semantic-candidate](#epi-obj-semantic-candidate), whose retention is not wired, and [RT-OBJ-episode](runtime.md#rt-obj-episode), which is an episodic envelope. Closest runtime finding [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) declares the consumer route, not this object. Returned semantic structure has evidence count but no source episode IDs; displayed learned-fact line has only fact/confidence. Candidate identity with retrieved payload cannot be assumed from matching names. SRC-1 `go-api/internal/services/retrieve_service.go`, `go-api/internal/domain/episode.go`, implementation.

> fact, _ := payload["fact"].(string)
> conf, _ := payload["confidence"].(float64)
> --- `go-api/internal/services/retrieve_service.go`

> fmt.Sprintf("[Learned Fact]: %s (confidence: %.0f%%)\n",
> sm.Fact, sm.Confidence*100),
> --- `go-api/internal/services/retrieve_service.go`

#### EPI-OBJ-benchmark-results
Label: Benchmark result records

Source-native result/summary dictionaries and JSON files; symbolic metric values with natural-language questions, reference answers and response excerpts, stored under benchmark `results`. Truth-apt content is a predicate or measured value about the actual tested response and timing, not a real user's life. References are synthetic source strings: 10 LongMemEval samples, five LoCoMo session groups and eight ConvoMem conversations by default. Source truth outside these fixtures is not established. No supplied runtime object counterpart; [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) supplies the response being judged, not the metric record. SRC-1 `benchmarks/longmemeval.py`, `benchmarks/locomo.py`, `benchmarks/convomem.py`, implementation.

> "exact_match": exact,
> "f1":          round(f1, 4),
> "llm_judge":   judge,
> --- `benchmarks/longmemeval.py`

### Routes

#### EPI-RTE-pattern-extraction
Label: Engine pattern extraction

Distinct subroutine route spanning [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation) and [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation): shared `ConsolidationEngine.consolidate`/`_compress_cluster`, not either endpoint container. Owner: Python engine code and provider for generated content. Agent ID and lowercase dictionaries enter domain grouping, greedy seed-intent overlap, selected/truncated model input, then output parsing and lineage attachment. Object: [EPI-OBJ-semantic-candidate](#epi-obj-semantic-candidate). Fixed extraction guidance requests durable preferences, patterns, errors, skills and repeated rules. It is not a test of that guidance. SRC-1 `python-worker/services/consolidation/engine.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate dictionaries or empty list on insufficient groups or model/JSON failure.
- Later read-back: inapplicable — engine retains no candidates itself; task's proposed write-back is a separate route.
- Delegated visibility: At most 15 episodes, each with first 500 raw-content characters, domain/outcome and intent; no independent ground truth.
- Selection predicate: At least three inputs per domain/cluster, at least two intent tokens shared with the seed.
- Invalidation or expiry: inapplicable — request-local output has no assigned retained lifetime.
- Activation or effect: Requests model inference and creates candidate objects; no observed output or durable acceptance.
- Evidence limits: Provider outputs absent; full-cluster IDs/counts can include material not supplied to model. No proposition-wise support check.

Caller/task triggers an open request, code selects inputs, model proposes text, software can withhold candidates. There is no per-content human veto or expected-answer oracle. Confidence is generated/defaulted, not independently measured. Recovery is empty result for caught model/JSON failure; later conversion errors may escape. Successful proposal returns candidate text and annotations, not criticism or revised extraction method. Conditions for formulated theory consumption/criticism/iteration are not established for actual output; no output supplied. Parameter findings are see [RT-CMP-consolidation-engine](runtime.md#rt-cmp-consolidation-engine).

> limited_eps = episodes[: self.max_cluster_size]
> --- `python-worker/services/consolidation/engine.py`

> f"Content: {str(ep.get('raw_content','?'))[:500]}"
> --- `python-worker/services/consolidation/engine.py`

> Focus on: user preferences explicitly stated, recurring patterns,
> errors to avoid, skills demonstrated, rules that apply repeatedly.
> Skip: one-time events, transient states, obvious facts.
> --- `python-worker/services/consolidation/engine.py`

> source_ids = [str(ep.get("episode_id") or "") for ep in episodes]
> --- `python-worker/services/consolidation/engine.py`

Concrete implementation deduction: three lowercase episodes all with domain `coding` and intent `fix parser` form one eligible cluster; three otherwise identical PascalCase Go episodes yield default domain and empty intents, so no overlap and no eligible cluster. Sixteen eligible episodes supply only the first 15 text previews but get 16 attached source IDs. These are code deductions, not executed cases or evidence of model compliance.

#### EPI-RTE-candidate-filter
Label: Engine candidate filtering
Part of: [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction)

Owner: engine output loop. Model output JSON enters list/object-key extraction, then nonempty fact test, float conversion and dictionary return. Different function from generation: operational candidate disposition. Target/domain: output shape/presence/numeric convertibility, not truth or causal adequacy. Object: [EPI-OBJ-semantic-candidate](#epi-obj-semantic-candidate). SRC-1 `python-worker/services/consolidation/engine.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate dictionaries surviving the fact test; float conversion can raise.
- Later read-back: inapplicable — filter writes no retained state.
- Delegated visibility: Python consumes generated fact and confidence, not a separate evidence dossier.
- Selection predicate: Truthy `fact`; confidence default 0.7 and conversion to float, with no range or threshold comparison.
- Invalidation or expiry: inapplicable — local candidate list only.
- Activation or effect: Enables direct return or task embed/write attempt for survivors; rejects empty facts.
- Evidence limits: This neither measures confidence nor certifies evidence IDs; observed candidate disposition unavailable.

Model proposes; software decides presence/conversion; human approval absent on this subroute, caller identity unresolved. Open inference, not a comparison experiment. No expected answer. Fixed extraction prompt guides proposals; returned annotations persist only if another route retains them. Recovery/rollback: rejected facts omitted, caught generation error produces no list; malformed item/conversion errors can abort the enclosing invocation.

> fact = item.get("fact")
> if not fact:
> continue
> confidence = float(item.get("confidence", 0.7))
> --- `python-worker/services/consolidation/engine.py`

#### EPI-RTE-compressor-helper
Label: Alternative compressor helper

Distinct from [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation) and [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation): `Compressor.compress`/`_parse_response` is a separate implementation, not imported by the inspected entry point/tasks/engine. Search for `Compressor`, `Clusterer`, `LLMService` across shipped roots plus complete helper reads found definitions but no caller wiring. `Clusterer` defaults to two-member groups and one keyword shared from intent/content, unlike the active engine. `LLMService` offers JSON/summarise calls but is not the active engine client. These available alternatives prevent equating all helper semantics with the active path. SRC-1 `python-worker/services/consolidation/compressor.py`, `python-worker/services/consolidation/clusterer.py`, `python-worker/services/llm_service.py`, implementation.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Sanitized fact dictionaries on explicit helper invocation; errors raise or return empty after failed JSON parsing.
- Later read-back: inapplicable — helper retains no output.
- Delegated visibility: Slim episode fields with content previews of 300 characters.
- Selection predicate: Nonempty cluster; dict/list response handling; dict items with nonempty stripped `content`; safe enum defaults and bounded numeric scores.
- Invalidation or expiry: inapplicable — helper output is request-local.
- Activation or effect: Model request then structural sanitization; no exposed consumer or durable admission established.
- Evidence limits: No helper caller or provider output supplied; truth or entailment not checked. Arbitrary output clipping does not establish non-ampliative reshaping; semantic preservation remains indeterminate for actual candidates.

Owner: helper code/provider. Producer model, deciding/vetoing party software; no human veto/answer oracle. Trigger explicit method call, fixed distillation guidance, open request. Proposed changes are output candidates, not production machinery; exceptions/empty output are recovery, no durable rollback. Model is distributed-parametric `gpt-4o` default (caller-overridable), opaque provider weights, no parameter updates in helper, exact version unpinned and alias mutable. Actual formulated theory and conditions 1–4 are unestablished without output; fixed guidance alone establishes no content-directed criticism or method iteration.

Concrete deterministic transformation: `_parse_response` applied to `[{"content":"  Prefer Rust  ","fact_type":"bogus","importance_score":2,"outcome":"bogus","confidence_score":-1}]` yields content `Prefer Rust`, fact_type `context`, importance 1.0, outcome `unknown`, confidence 0.0. A blank content item is dropped. The implementation supports this deduction without target execution. Numeric/enum sanitation does not test whether the user prefers Rust. The short input illustrates a preserved fact string, not preservation for all inputs. For a concrete countercase, a proposed content string consisting of `Use Rust`, 292 spaces and `only for prototypes` has its qualification removed by `content[:300]`, leaving `Use Rust` and the spaces. The full string is restricted to prototypes; the clipped string no longer states that restriction. This implementation deduction shows why the arbitrary clipping edge cannot receive a definite non-ampliative classification. No target code was executed.

> "content": content[:300],
> --- `python-worker/services/consolidation/compressor.py`

> content = str(item.get("content", "")).strip()
> if not content:
> continue
> --- `python-worker/services/consolidation/compressor.py`

> return max(0.0, min(1.0, float(value)))
> --- `python-worker/services/consolidation/compressor.py`

#### EPI-RTE-retrieval-feedback
Label: Retrieval popularity feedback
Part of: [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve)

Owner Go retrieval service; selected episodes enter asynchronous PostgreSQL count increments; later retrieval reads the count into ranking. Object: symbolic `RetrievalCount` on [RT-OBJ-episode](runtime.md#rt-obj-episode). This is a behavioral adaptation part, not the entire retrieval chain. SRC-1 `go-api/internal/services/retrieve_service.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Retrieval response does not await count update.
- Later read-back: Later query's rehydrated episode count increases the ranking bonus, capped at 0.3 before its 0.15 weight.
- Delegated visibility: Code sees selections/counts; no user/model evaluation of retrieval utility is consumed.
- Selection predicate: Final ranked selected episodes receive attempted increments.
- Invalidation or expiry: No count expiry/reset in this route; errors ignored.
- Activation or effect: Popularity can change future ordering; actual changed ranking unobserved.
- Evidence limits: No objective/outcome evidence shapes the update; successful count writes unknown.

Consumer/channel/force/horizon: later Go reranker through PostgreSQL counter, ranking force across subsequent requests. No epistemic license for truth or usefulness. Selector is software; generic caller chooses queries. This is not an oracle-driven improvement experiment. Improved capacity is unestablished; self-improvement's objective-evidence and subsequent-exercise links are unestablished, independently of implemented counter adaptation.

> retrievalBonus := float64(ep.RetrievalCount) * 0.05
> if retrievalBonus > 0.3 {
> retrievalBonus = 0.3
> }
> --- `go-api/internal/services/retrieve_service.go`

#### EPI-RTE-benchmark-evaluation
Label: Synthetic benchmark evaluation

Distinct from production [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve); repository drivers consume that output and produce [EPI-OBJ-benchmark-results](#epi-obj-benchmark-results). `run_all.py` dispatches three known benchmark names and saves combined summaries. Owner: benchmark software, optionally [EPI-CMP-benchmark-judge](#epi-cmp-benchmark-judge). Target: reference-answer presence and token overlap in injection context, ConvoMem stringified snippet presence, and elapsed retrieval timing. Domain: synthetic source samples or caller-supplied sample list, configured API. SRC-1 `benchmarks/run_all.py`, `benchmarks/longmemeval.py`, `benchmarks/locomo.py`, `benchmarks/convomem.py`, `benchmarks/adapters/rem_adapter.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary metrics and console display if API writes/retrieval succeed.
- Later read-back: JSON results saved locally; suite reloads in-memory summaries for display/combined file. No production admission/update consumer found in these drivers.
- Delegated visibility: Optional judge receives question, expected answer and retrieved injection text; software sees references and full response/stringified snippets.
- Selection predicate: Requested suite targets; all default samples or supplied list; judge enabled only by USE_LLM_JUDGE.
- Invalidation or expiry: Result files overwritten per benchmark; reset attempt separately assessed.
- Activation or effect: Saves/displays scores; does not revise or accept memory content or block production use.
- Evidence limits: No observed result or comparison; synthetic references, fixture padding and reset failures bound inference; no downstream answer generation here. Default benchmark executability is not established: generated agent IDs have no corresponding created agent rows under the episode foreign key; fresh Go setup also meets the duplicate-trigger migration failure described in [Runtime account](runtime.md#runtime-account). Prepared migration state and registered caller-supplied agents are separate conditions.

Operating mode bounded synthetic probes, not production acceptance. Source authors/supplied samples provide expected-answer oracle strings. Software decides substring/F1/snippet predicates; optional model provides judgment without proven calibration. Human per-result veto absent. The benchmarks compare responses with references, not independent variation of a memory component or against a no-memory treatment. They do not identify consolidation benefit or mechanism transfer.

The optional judge's evaluator output has a separate conversion path: a reply starting `Y` becomes true, and a caught provider error becomes false, conflating a negative answer with unavailable judgment. Neither result changes production-memory admission.

> return resp.choices[0].message.content.strip().upper().startswith("Y")
> --- `benchmarks/longmemeval.py`

> print(f"  [LLM judge error] {e}")
> return False
> --- `benchmarks/longmemeval.py`

Concrete deduction: `contains_answer("The dog is not Biscuit", "Biscuit")` is true; token-set F1 on prediction `Biscuit Biscuit` and gold `Biscuit` is 1.0. Thus the label exact-match means normalized substring presence, not semantic agreement or exact answer equality. ConvoMem precision is fraction of stringified returned snippets containing the answer, not a general relevance judgment; it reads `memories`, while Go returns `episodes`, yielding an empty default on that response shape. LoCoMo stores session metadata but scores no session-identity predicate. LongMemEval stores only the first 300 characters of prediction after scoring the full text; saved excerpts alone need not reproduce the score. These are implementation deductions, not measured results.

> return normalize(gold) in normalize(prediction)
> --- `benchmarks/longmemeval.py`

> pred_tokens = set(normalize(prediction).split())
> gold_tokens = set(normalize(gold).split())
> --- `benchmarks/longmemeval.py`

> memories  = result.get("memories", [])
> --- `benchmarks/convomem.py`

> hits = sum(1 for m in memories if normalize(answer) in normalize(str(m)))
> return hits / len(memories)
> --- `benchmarks/convomem.py`

> "prediction": prediction[:300],
> --- `benchmarks/longmemeval.py`

#### EPI-RTE-benchmark-cleanup
Label: Benchmark memory reset

Distinct lifecycle consumer inside benchmarks, absent from supplied runtime route inventory; overlaps the endpoint absence in [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes), not a duplicate of the write-back task. Owner benchmark adapter; list → lowercase ID extraction → attempted DELETE with no response success check. Source Go episodes have PascalCase IDs, and router has no DELETE. Fresh agent UUIDs can isolate separate default benchmark runs, a countercase to a general claim of inevitable cross-run contamination; ConvoMem reuses one ID across its eight conversations and relies on reset. SRC-1 `benchmarks/adapters/rem_adapter.py`, `benchmarks/convomem.py`, `go-api/internal/domain/episode.go`, `go-api/internal/api/router.go`, implementation.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: None; exceptions suppressed.
- Later read-back: Later probes use the same agent ID within ConvoMem; removal is not wired, so prior retained input remains eligible.
- Delegated visibility: Adapter sees episode list, not proof of completed deletion.
- Selection predicate: First up to 200 listed episodes with `id` or `episode_id` present; neither matches Go `EpisodeID`.
- Invalidation or expiry: Proposed DELETE not registered; no achieved expiry/removal established.
- Activation or effect: Best-effort cleanup attempt, not enforced fresh state.
- Evidence limits: No reset run; actual deployed state unknown.

Consumer/channel/force/horizon: subsequent benchmark retrieval through reused agent identity, intended cleanup/isolating force that is not completed at this revision. No truth evaluator or acceptance criterion. Cleanup failure limits session isolation, not every individual answer-presence result.

> eid = ep.get("id") or ep.get("episode_id", "")
> if eid:
> c.delete(f"/episodes/{eid}")
> --- `benchmarks/adapters/rem_adapter.py`

### Claims

#### EPI-CLM-recursive-memory
Label: Recursive evolving memory

Distinct claims adjacent to [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop), which covers the write/consolidate/retrieve connection: README presents recursive consolidation, self-evolving memories and first-class forgetting. SRC-1 `README.md`, doctrine/design. Active engine reads raw episodes and produces candidates, not semantic predecessors; retrieval-count feedback exists but is not recursive semantic criticism. Roadmap qualifies forgetting ambitions. Actual exercised revision or benefit unobserved.

> | Forgetting policy        | **First‑class** |
> | Self‑evolving memories   | **✅**  |
> --- `README.md`

> - [ ] Fine‑grained forgetting and redaction policies
> --- `README.md`

#### EPI-CLM-causal-graph
Label: Causal graph reasoning

Distinct from [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop): claim is causal reasoning/graph, not merely context return. SRC-1 `README.md`, doctrine/design. Direct implementation reads of graph/write/retrieval show `FOLLOWED_BY` edges from preceding stored episode and undirected temporal neighbors; helper `COMPRESSED_INTO` records source compression, not causes. Graph display method returns empty arrays even after its query. These support temporal context expansion and schema/helper capability, not a causal inference evaluator or causal explanation warrant. SRC-1 `go-api/internal/db/neo4j/client.go`, `go-api/internal/services/write_service.go`, implementation.

> - **Graph reasoning** — a causal graph of episodes and facts your agent can traverse.
> --- `README.md`

> MERGE (a)-[:FOLLOWED_BY]->(b)
> --- `go-api/internal/db/neo4j/client.go`

> MATCH (e)-[:FOLLOWED_BY*1..%d]-(n:Episode)
> --- `go-api/internal/db/neo4j/client.go`

#### EPI-CLM-recall-performance
Label: Recall accuracy claim

No supplied runtime counterpart: public FAQ attributes 81.6% LongMemEval accuracy and sub-50ms latency to hybrid retrieval. SRC-1 `dashboard/src/lib/config.tsx`, doctrine/design. [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) establishes evaluators only; no result artifact, deployment condition, official dataset capture or intervention was supplied. The source's default ten synthetic samples and substring metric cannot establish the claimed number or a component cause. Static code timing support is not latency measurement.

> "REM uses hybrid retrieval combining dense vector search (via Qdrant) for semantic similarity, graph traversal (via Neo4j) for causal and relational reasoning, and recency weighting. This achieves 81.6% accuracy on the LongMemEval benchmark at sub-50ms latency."
> --- `dashboard/src/lib/config.tsx`

### Evidenced absences

#### EPI-ABS-semantic-withdrawal
Label: Semantic acceptance and withdrawal

- implementation conclusion status: absent

Bounded absence at SRC-1 revision 935e8be0a1fca5b23dbabfe16c48b562c1cd24cc: searches across `python-worker`, `go-api`, `sdk`, `scripts`, `docs`, `dashboard/src`, `README.md`, `Makefile` for `contradict`, `supersed`, `forget`, `confidence`, `InsertSemanticMemory`, `UpsertSemantic`, `Delete`, plus complete engine/tasks/router, PostgreSQL semantic, Qdrant, graph and helper reads, found fields/defaults and operational candidate filters but no evidence-consuming semantic acceptance decision, contradiction evaluator, operative supersession/withdrawal consumer or accepted-claim lifecycle integration route in that loop. Closest supplied finding is [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes), a narrower HTTP registration absence; this record concerns warrant and withdrawal semantics, not endpoint identity.

SQL listing does not filter active/superseded/contradicted flags; Qdrant semantic search filters agent only. `active` affects SQL statistics, not a truth check or retrieval withdrawal. Therefore schema fields cannot establish a veto. This conclusion does not exclude opaque provider internal assessment, external host review or administrator-loaded data; those are not inspected REM acceptance routes. It prevents attributing accepted knowledge production, automatic correction or effective forgetting to these fields. SRC-1 `go-api/internal/db/postgres/semantic.go`, `go-api/internal/db/qdrant/client.go`, `python-worker/services/consolidation/engine.py`, implementation.

> WHERE agent_id = $1
> ORDER BY created_at DESC
> LIMIT $2
> --- `go-api/internal/db/postgres/semantic.go`

> return c.search(ctx, "semantic_memories", queryVector, filter, topK, 0)
> --- `go-api/internal/db/qdrant/client.go`

### Behavioral-authority paths

none declared in this member; contextual host path is see [RT-BAP-context-injection](runtime.md#rt-bap-context-injection), and the new route records identify their narrower consumers/channels/forces/horizons.
