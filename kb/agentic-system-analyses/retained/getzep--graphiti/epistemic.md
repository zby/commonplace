---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Graphiti's truth-apt content, temporal comparison, reliance and downstream authority at the frozen revision."
run-id: AAS-2026-10-12-graphiti-1d535ca565a4-01
reviewed-boundary: "964bb11d1e7020e3cc67fab244268b0736b6c219"
---

# Graphiti epistemic report

## Source-and-claim boundary

The question is how Graphiti imports or produces truth-apt graph content, checks it, changes reliance and makes it consequential. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not an observed invocation or causal experiment. The whole-system source boundary includes services, maintenance, shipped consumers and evaluators. This member's inspection is selective within it, not a system-complete semantic audit.

The public temporal-truth and full-provenance claims are see [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance). The distinction between representation checks, semantic comparisons, persistence and warranted acceptance matters: none of those phases substitutes for another. Structured schemas and reference timestamps are not source-truth oracles. Provider weights, external host enforcement, database engines, proprietary Zep, live deployments and historical notebook outputs remain outside the inspected evidence as specified by the boundary. No target execution was performed.

Coverage below distinguishes direct source reads in this job from supplied runtime findings. Paths are commit-relative anchors in SRC-1. Direct inspection of a selected range does not imply complete file coverage.

| Entry point / operation | Source path | Coverage and records / prevented conclusion |
|---|---|---|
| Single and bulk episodes, context and writes | `graphiti_core/graphiti.py` | Supplied [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion); direct temporal, saga and removal reads supplement these. Combined bulk prompt semantics not fully inspected: no single/bulk semantic-equivalence conclusion. |
| Entity extraction / identity / attributes | `graphiti_core/utils/maintenance/node_operations.py` | Supplied [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion); direct model identity resolution and summary branches. Attributes are covered by supplied processing account, not every cap/coercion/type variant; no universal identity or attribute fidelity. |
| Edge generation / comparison / invalidation | `graphiti_core/utils/maintenance/edge_operations.py` | Direct [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [EPI-RTE-fact-comparison](#epi-rte-fact-comparison), [EPI-RTE-fact-disposition](#epi-rte-fact-disposition); supplied [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) for surrounding persistence. |
| Built-in fact and comparison instructions | `graphiti_core/prompts/extract_edges.py`, `graphiti_core/prompts/dedupe_edges.py` | Direct [EPI-RTE-fact-extraction](#epi-rte-fact-extraction) and [EPI-RTE-fact-comparison](#epi-rte-fact-comparison); not all extraction prompt variants. No semantic-preservation proof for every provider/custom builder. |
| Exact normalization | `graphiti_core/utils/maintenance/dedup_helpers.py` | Direct [EPI-RTE-fact-comparison](#epi-rte-fact-comparison) concrete deduction. Fuzzy helper families not audited end to end. |
| Node summaries | `graphiti_core/utils/maintenance/node_operations.py` | Direct [EPI-RTE-entity-summary](#epi-rte-entity-summary): concatenation differs from model generation. |
| Community rebuild and update | `graphiti_core/utils/maintenance/community_operations.py`, `graphiti_core/graphiti.py` | Direct pairwise synthesis; supplied [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) for rebuild/write/clear. Clustering is organization, not a factual evaluator; all cluster choices not inspected. |
| Saga summarize and watermarks | `graphiti_core/graphiti.py` | Direct persistence and selected-watermark reads; supplied [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) for budget/context selection. No exhaustive summary fidelity or late-arrival proof. |
| Search recipes / numerical relevance | `graphiti_core/search/search.py`, `graphiti_core/cross_encoder/openai_reranker_client.py` | Supplied [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval) and model component records; no direct complete scoring audit or measured retrieval quality. |
| REST admission, retrieval and direct saves | `server/graph_service/routers/ingest.py`, `server/graph_service/routers/retrieve.py`, `server/graph_service/zep_graphiti.py` | Supplied [RT-RTE-service-admission](runtime.md#rt-rte-service-admission), [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes). Supplied findings, not fresh service source inspection; no deployment or authorization conclusion. |
| Registered MCP tools | `mcp_server/src/graphiti_mcp_server.py` | Direct tool-declaration search plus get-edge/get-episodes/delete implementations; supplied [RT-RTE-service-admission](runtime.md#rt-rte-service-admission), [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) cover add-memory, search, triplet, saga, communities and clear. Get-episode-entities is discovered but not closely inspected: prevents universal service-lineage delivery conclusions. Status/health are service liveness, not factual endorsement. |
| MCP direct reads and formatting | `mcp_server/src/graphiti_mcp_server.py`, `mcp_server/src/utils/formatting.py` | Direct [EPI-RTE-provenance-read](#epi-rte-provenance-read); fact responses retain temporal/episode fields unlike notebook fact strings. |
| Typed attributes | `graphiti_core/utils/maintenance/node_operations.py`, `graphiti_core/utils/maintenance/edge_operations.py` | Direct [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction); node overlay versus edge replacement, with cap/coercion internals uninspected. |
| MCP queue / shipped instructions | `mcp_server/src/services/queue_service.py`, `mcp_server/docs/cursor_rules.md` | Supplied [RT-RTE-service-admission](runtime.md#rt-rte-service-admission) and [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions); no evidence that a host follows instructions or grants tools. |
| Notebook consumer / automatic conversation recording | `examples/langgraph-agent/agent.ipynb` | Supplied [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop) and [RT-BAP-facts-context](runtime.md#rt-bap-facts-context); direct notebook chatbot/scheduler reads confirm post-tool input and intermediate-response admission. Other example consumers remain less inspected: no system-complete negative about consumer behavior. |
| CLI evaluator and graph judge | `tests/evals/eval_cli.py`, `tests/evals/eval_e2e_graph_building.py` | Direct CLI dispatch, construction/context/score; supplied [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison). No automatic score-to-production installation appears in these inspected functions. No executed evaluation. |
| Prompt routing / local or remote alternatives | `graphiti_core/llm_client/llm_runtime.py`, `graphiti_core/prompts/lib.py`, `graphiti_core/llm_client/gliner2_client.py` | Supplied [RT-RTE-prompt-routing](runtime.md#rt-rte-prompt-routing) and component records. Opaque inference remains opaque; custom clients/builders and other provider internals prevent global model correctness claims. |
| Object persistence / backend implementations | `graphiti_core/nodes.py`, `graphiti_core/edges.py`, `graphiti_core/driver/` | Direct selected object fields; supplied persistence accounts. Backend parity, namespace writes and every serialization path not audited; no universal atomicity/provenance preservation. |
| README claims | `README.md` | Direct [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance). Public performance claims are outside this truth/warrant assessment; no measurement is supplied. |

Missing evidence has local consequences: warranted source inputs and checked interpretation are needed to license derived facts as true; actual provider outputs are needed to classify particular semantic transformations; pinned runs are needed for activation; independent outcomes and comparisons are needed for benefit or component attribution. None is replaced by graph persistence. Available but uninspected paths are not access gaps or evidenced absences.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-episodic-node](#epi-obj-episodic-node) | see [EPI-OBJ-episodic-node](#epi-obj-episodic-node) | see [EPI-OBJ-episodic-node](#epi-obj-episodic-node) | SRC-1 `graphiti_core/nodes.py` | Source assertions may be false; notebook input can mix human, model and tool content. Its user-name prefix does not authenticate origin. |
| [EPI-OBJ-entity-node](#epi-obj-entity-node), identity part | see [EPI-OBJ-entity-node](#epi-obj-entity-node) | see [EPI-OBJ-entity-node](#epi-obj-entity-node) | SRC-1 `graphiti_core/nodes.py` | Name/type/UUID identity hypothesis; model resolution is not source authentication. |
| [EPI-OBJ-entity-attributes](#epi-obj-entity-attributes) | see [EPI-OBJ-entity-attributes](#epi-obj-entity-attributes) | see [EPI-OBJ-entity-attributes](#epi-obj-entity-attributes) | SRC-1 `graphiti_core/utils/maintenance/node_operations.py` | Schema-specific predicates; fidelity unmeasured. |
| [EPI-OBJ-entity-summary](#epi-obj-entity-summary) | see [EPI-OBJ-entity-summary](#epi-obj-entity-summary) | see [EPI-OBJ-entity-summary](#epi-obj-entity-summary) | SRC-1 `graphiti_core/utils/maintenance/node_operations.py` | Append and synthesis have different semantics. |
| [EPI-OBJ-entity-edge](#epi-obj-entity-edge), fact text part | see [EPI-OBJ-entity-edge](#epi-obj-entity-edge) | see [EPI-OBJ-entity-edge](#epi-obj-entity-edge) | SRC-1 `graphiti_core/edges.py` | Relational assertions over endpoints; factual warrant unknown. |
| [EPI-OBJ-edge-validity](#epi-obj-edge-validity) | see [EPI-OBJ-edge-validity](#epi-obj-edge-validity) | see [EPI-OBJ-edge-validity](#epi-obj-edge-validity) | SRC-1 `graphiti_core/edges.py` | Symbolic temporal scope, not independently verified history. |
| [EPI-OBJ-edge-episodes](#epi-obj-edge-episodes) | see [EPI-OBJ-edge-episodes](#epi-obj-edge-episodes) | see [EPI-OBJ-edge-episodes](#epi-obj-edge-episodes) | SRC-1 `graphiti_core/utils/maintenance/edge_operations.py` | Fallback can associate all input episodes; association is not exact evidential support. |
| [EPI-OBJ-edge-embedding](#epi-obj-edge-embedding) | none individuated | see [EPI-OBJ-edge-embedding](#epi-obj-edge-embedding) | SRC-1 `graphiti_core/edges.py` | Dense encoding controls similarity selection, not source truth. |
| [EPI-OBJ-entity-edge](#epi-obj-entity-edge), attributes part | Schema-dependent attribute assertions; see [EPI-OBJ-entity-edge](#epi-obj-entity-edge) | see [EPI-OBJ-entity-edge](#epi-obj-entity-edge) | SRC-1 `graphiti_core/utils/maintenance/edge_operations.py` | Edge replacement semantics differ from node overlay; cap/coercion implementation not audited. |
| [EPI-OBJ-edge-duplicate](#epi-obj-edge-duplicate) | see [EPI-OBJ-edge-duplicate](#epi-obj-edge-duplicate) | see [EPI-OBJ-edge-duplicate](#epi-obj-edge-duplicate) | SRC-1 `graphiti_core/prompts/dedupe_edges.py` | Indices are symbolic decisions about semantic comparisons, not certified truth. |
| [EPI-OBJ-community-node](#epi-obj-community-node), summary part | see [EPI-OBJ-community-node](#epi-obj-community-node) | see [EPI-OBJ-community-node](#epi-obj-community-node) | SRC-1 `graphiti_core/utils/maintenance/community_operations.py` | Pairwise compression; fidelity not checked. |
| [EPI-OBJ-community-node](#epi-obj-community-node), name part | Generated descriptive label; see [EPI-OBJ-community-node](#epi-obj-community-node) | see [EPI-OBJ-community-node](#epi-obj-community-node) | SRC-1 `graphiti_core/utils/maintenance/community_operations.py` | A new model call derives a name from summary, not a truth check. |
| [EPI-OBJ-community-node](#epi-obj-community-node), membership part | No independently evaluated world assertion established by clustering | see [EPI-OBJ-community-node](#epi-obj-community-node) | SRC-1 `graphiti_core/utils/maintenance/community_operations.py` | Symbolic grouping by neighbor edge counts is organization, not factual acceptance. |
| [EPI-OBJ-saga-node](#epi-obj-saga-node), summary part | see [EPI-OBJ-saga-node](#epi-obj-saga-node) | see [EPI-OBJ-saga-node](#epi-obj-saga-node) | SRC-1 `graphiti_core/graphiti.py` | Prior text becomes next summary context; semantic preservation unmeasured. |
| [EPI-OBJ-saga-watermarks](#epi-obj-saga-watermarks) | see [EPI-OBJ-saga-watermarks](#epi-obj-saga-watermarks) | see [EPI-OBJ-saga-watermarks](#epi-obj-saga-watermarks) | SRC-1 `graphiti_core/graphiti.py` | Selection coverage/currentness, not endorsement. |
| see [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder) and [RT-CMP-openai-reranker-client](runtime.md#rt-cmp-openai-reranker-client) | No individually recoverable proposition established in dense vectors / scores | see component records | SRC-1 `graphiti_core/embedder/openai.py`, `graphiti_core/cross_encoder/openai_reranker_client.py` | Relevance is a selection target, not truth. Internal distributed-parametric content is not determinable from adapters. |

## Authority-route ledger

The architectural status below concerns implementation, never observed success. Each function is split even when it cites one container record. No lifecycle integration after evidence-consuming factual acceptance is established in the inspected production routes; episode links and summary organization are retention/organization before such acceptance, not proof of it.

Route ID: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episodic-node](#epi-obj-episodic-node)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller episode content enters processing.
Evaluator/condition and domain: Caller selection, not an independent truth evaluator.
Activation and timing: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion); operation unobserved.
Possible or observed result: Possible imported assertions; see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
Implemented force: Permissive input supply.
Epistemic authority and scope: Source warrant unknown; source type is not certification.
Operational authority: behavior permitted, blocked, or changed: Later extraction can rely on selected previous episodes.
Behavioral-authority path: consumer, channel, force, horizon: Extraction client; episode content in prompts; advisory semantic context; current and later ingestion.
Evidence source ID and local anchor: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: none
Gap/limit: Human per-content approval unresolved; raw content can be dropped.

Route ID: [EPI-RTE-fact-extraction](#epi-rte-fact-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Text to relational assertions, endpoints and temporal candidates.
Evaluator/condition and domain: Configured model under extraction instructions; domain is textual factual relations.
Activation and timing: see [EPI-RTE-fact-extraction](#epi-rte-fact-extraction); operation unobserved.
Possible or observed result: Candidate facts; see [EPI-RTE-fact-extraction](#epi-rte-fact-extraction).
Implemented force: Candidate generation.
Epistemic authority and scope: Intended paraphrase/implicit relations; no checked entailment or source-truth license.
Operational authority: behavior permitted, blocked, or changed: Candidates proceed to graph resolution.
Behavioral-authority path: consumer, channel, force, horizon: Resolver; structured model response; permissive candidate supply; ingestion.
Evidence source ID and local anchor: see [EPI-RTE-fact-extraction](#epi-rte-fact-extraction).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: none
Gap/limit: Remaining possibilities are non-ampliative reshaping, entailed interpretation or unsupported conjecture; actual outputs and source comparison needed. Non-entailment not established merely by using a model.

Route ID: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: no content change
Transition or check target: Extracted entity identity against graph candidates.
Evaluator/condition and domain: Name/identity/fuzzy matching and model comparisons; entity equivalence domain, not general source truth.
Activation and timing: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion); operation unobserved.
Possible or observed result: Reuse/new identity hypothesis; see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
Implemented force: Comparative signal.
Epistemic authority and scope: Identity plausibility, bounded by candidate search and malformed-response defenses.
Operational authority: behavior permitted, blocked, or changed: Feeds UUID map and endpoint resolution.
Behavioral-authority path: consumer, channel, force, horizon: Resolution software; IDs from model/context; enforcing identity choice; persistent graph after save.
Evidence source ID and local anchor: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Direct source read: SRC-1 `graphiti_core/utils/maintenance/node_operations.py`; invalid candidate ID defaults to new node, not rejection of source content.

Route ID: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Identity remapping and duplicate consolidation.
Evaluator/condition and domain: Software consumes match/ID results; see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
Activation and timing: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion); operation unobserved.
Possible or observed result: Existing UUID reused or new node retained.
Implemented force: Enforcing identity consolidation.
Epistemic authority and scope: Operational disposition, not evidenced factual acceptance.
Operational authority: behavior permitted, blocked, or changed: Later facts connect to selected node identity.
Behavioral-authority path: consumer, channel, force, horizon: Graph writer and later search; UUID maps; enforcing; persisted state until mutation.
Evidence source ID and local anchor: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Wrong equivalence can merge assertions; model identity output accuracy unmeasured.

Route ID: [EPI-RTE-fact-comparison](#epi-rte-fact-comparison)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-edge-duplicate](#epi-obj-edge-duplicate)
Content/update relation: no content change
Transition or check target: Duplicate/contradictory relation between new and selected old fact strings.
Evaluator/condition and domain: Exact normalized fact+endpoints, or configured model semantic judgment; see [EPI-RTE-fact-comparison](#epi-rte-fact-comparison).
Activation and timing: see [EPI-RTE-fact-comparison](#epi-rte-fact-comparison); operation unobserved.
Possible or observed result: Duplicate/contradiction indices, or immediate reuse; see [EPI-RTE-fact-comparison](#epi-rte-fact-comparison).
Implemented force: Signals for reconciliation.
Epistemic authority and scope: String equivalence in exact domain; model requests mutual inconsistency, not independent verification.
Operational authority: behavior permitted, blocked, or changed: Signals feed disposition.
Behavioral-authority path: consumer, channel, force, horizon: Resolver; numeric indices or exact match; enforcing downstream after interpretation; this ingestion.
Evidence source ID and local anchor: see [EPI-RTE-fact-comparison](#epi-rte-fact-comparison).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: none
Gap/limit: Candidate retrieval is not exhaustive. Exact reuse is an exception to mandatory model checking.

Route ID: [EPI-RTE-fact-disposition](#epi-rte-fact-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Duplicate selection, valid-index filtering and temporal withdrawal.
Evaluator/condition and domain: Software index bounds and time comparisons, conditioned on model contradiction selection.
Activation and timing: see [EPI-RTE-fact-disposition](#epi-rte-fact-disposition); operation unobserved.
Possible or observed result: Reuse first valid duplicate; ignore bad indices; update invalid_at/expired_at if temporal conditions hold.
Implemented force: Enforcing operational disposition.
Epistemic authority and scope: No general assertion that new fact is true. Time-order deductions are conditional on selected contradictions and supplied dates.
Operational authority: behavior permitted, blocked, or changed: Changes graph identity and temporal reliance fields; retains history rather than deleting these contradicted edges.
Behavioral-authority path: consumer, channel, force, horizon: Persistence and temporal readers; IDs and timestamps; enforcing updates, filtering conditional on caller recipe; future reads.
Evidence source ID and local anchor: see [EPI-RTE-fact-disposition](#epi-rte-fact-disposition).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: none
Gap/limit: No independent truth oracle; invalid index rejection is representational. Equal dates/nonoverlap can avoid invalidation.

Route ID: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episodic-node](#epi-obj-episodic-node) and [EPI-OBJ-entity-edge](#epi-obj-entity-edge) and [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: no content change
Transition or check target: Graph content and source associations retained.
Evaluator/condition and domain: Software write orchestration; see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion).
Activation and timing: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion); operation unobserved.
Possible or observed result: Possible saved graph; bulk may prewrite episodes.
Implemented force: Permissive persistence.
Epistemic authority and scope: Retention adds no warrant; source linkage can help later checking.
Operational authority: behavior permitted, blocked, or changed: Makes content available to future ingestion/retrieval.
Behavioral-authority path: consumer, channel, force, horizon: Graph driver; serialized objects; enforcing storage requests; subsequent calls conditional on backend success.
Evidence source ID and local anchor: see [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: Full-lineage claim is conditional.
Gap/limit: No whole-invocation transaction guarantee. Raw-content suppression degrades source access; direct writes need not have episode origin.

Route ID: [EPI-RTE-entity-summary](#epi-rte-entity-summary)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Short existing summary plus edge.fact strings.
Evaluator/condition and domain: Deterministic concatenation under length condition.
Activation and timing: see [EPI-RTE-entity-summary](#epi-rte-entity-summary); operation unobserved.
Possible or observed result: Appended fact text assigned directly; see [EPI-RTE-entity-summary](#epi-rte-entity-summary).
Implemented force: Enforcing text assignment.
Epistemic authority and scope: Carries only warrant of input strings; makes no new world claim by concatenation.
Operational authority: behavior permitted, blocked, or changed: Changed summary can reach later identity/search/summary consumers.
Behavioral-authority path: consumer, channel, force, horizon: Node summary field; concatenated text; persisted descriptive influence; later invocations.
Evidence source ID and local anchor: see [EPI-RTE-entity-summary](#epi-rte-entity-summary).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Does not establish consistency, acceptance or currentness of all appended statements.

Route ID: [EPI-RTE-entity-summary](#epi-rte-entity-summary)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Long or forced episode-based entity summary.
Evaluator/condition and domain: Configured model plus output-name match and length truncation.
Activation and timing: see [EPI-RTE-entity-summary](#epi-rte-entity-summary); operation unobserved.
Possible or observed result: Generated summary assigned to matching node names.
Implemented force: Permissive semantic synthesis, enforcing assignment.
Epistemic authority and scope: Intended compression; no checked semantic preservation.
Operational authority: behavior permitted, blocked, or changed: Replaces summary used by later operations.
Behavioral-authority path: consumer, channel, force, horizon: Node summary consumers; generated text; advisory semantic influence after persistence; later calls.
Evidence source ID and local anchor: see [EPI-RTE-entity-summary](#epi-rte-entity-summary).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Remaining reshaping/entailed/ampliative alternatives require actual outputs; case-insensitive name match is not truth validation.

Route ID: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-community-node](#epi-obj-community-node)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Community text built from paired entity summaries; descriptive name generated from result.
Evaluator/condition and domain: Model pair summarizer/name generator; software clustering and truncation.
Activation and timing: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); operation unobserved.
Possible or observed result: Candidate summary/name; see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Implemented force: Permissive descriptive synthesis.
Epistemic authority and scope: No independent license beyond unverified inputs and requested summary semantics.
Operational authority: behavior permitted, blocked, or changed: Advanced retrieval/community updates can consume retained organization/text.
Behavioral-authority path: consumer, channel, force, horizon: Community builder/search; text plus membership edges; advisory semantics and enforcing membership; later calls.
Evidence source ID and local anchor: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Direct SRC-1 `graphiti_core/utils/maintenance/community_operations.py`; actual output relation unresolved.

Route ID: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-community-node](#epi-obj-community-node)
Content/update relation: no content change
Transition or check target: Community rebuild/update persistence.
Evaluator/condition and domain: Explicit caller maintenance; see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Activation and timing: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); operation unobserved.
Possible or observed result: Scoped old communities removed and replacements saved.
Implemented force: Enforcing state replacement.
Epistemic authority and scope: Organization before warranted acceptance; no lifecycle-integration finding.
Operational authority: behavior permitted, blocked, or changed: Changes future community availability.
Behavioral-authority path: consumer, channel, force, horizon: Driver and future readers; save/remove calls; enforcing; after write until next rebuild.
Evidence source ID and local anchor: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Destructive rebuild is not rollback and may fail between stages.

Route ID: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-saga-node](#epi-obj-saga-node)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Prior summary plus selected new episode content.
Evaluator/condition and domain: Configured saga summarizer under prompt budgets.
Activation and timing: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); operation unobserved.
Possible or observed result: Candidate incremental summary; see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Implemented force: Permissive synthesis.
Epistemic authority and scope: No source-fidelity check established.
Operational authority: behavior permitted, blocked, or changed: Summary enters next summarization as prior context.
Behavioral-authority path: consumer, channel, force, horizon: Saga model and API caller; retained text; advisory semantic input; across summarization calls.
Evidence source ID and local anchor: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Direct SRC-1 `graphiti_core/graphiti.py`; remaining transformation classes need output evidence.

Route ID: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-saga-node](#epi-obj-saga-node)
Content/update relation: no content change
Transition or check target: Summary ingestion/event-time watermarks.
Evaluator/condition and domain: Software max timestamps for actually selected episodes.
Activation and timing: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); operation unobserved.
Possible or observed result: Watermarks saved alongside summary.
Implemented force: Enforcing next-input selection.
Epistemic authority and scope: Freshness/coverage markers, not endorsement or proof all input facts survived.
Operational authority: behavior permitted, blocked, or changed: Controls later incremental selection.
Behavioral-authority path: consumer, channel, force, horizon: Next summarize_saga; stored watermarks; enforcing filter; later calls.
Evidence source ID and local anchor: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: none
Gap/limit: Watermark semantics are distinct from proposition correctness.

Route ID: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-node](#epi-obj-entity-node) and [EPI-OBJ-entity-edge](#epi-obj-entity-edge)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller-supplied triplet/name/summary or direct graph write.
Evaluator/condition and domain: Caller supply; triplet resolution checks differ from REST direct entity save.
Activation and timing: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); operation unobserved.
Possible or observed result: Supplied graph claims can be stored without episode extraction.
Implemented force: Permissive alternate admission.
Epistemic authority and scope: Source warrant unknown; imported rather than produced knowledge.
Operational authority: behavior permitted, blocked, or changed: Later graph consumers can use these claims.
Behavioral-authority path: consumer, channel, force, horizon: Core/service writers and search; graph properties; enforcing storage and advisory retrieval; future requests.
Evidence source ID and local anchor: see [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: Direct writes limit universal episode lineage.
Gap/limit: Not a universal extraction/episode-provenance gate.

Route ID: [RT-RTE-service-admission](runtime.md#rt-rte-service-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episodic-node](#epi-obj-episodic-node)
Content/update relation: no content change
Transition or check target: Timestamp/input validation and queue acceptance.
Evaluator/condition and domain: Service software; request-shape domain.
Activation and timing: see [RT-RTE-service-admission](runtime.md#rt-rte-service-admission); operation unobserved.
Possible or observed result: Queued response, not persisted fact acceptance.
Implemented force: Permissive processing admission.
Epistemic authority and scope: No factual license.
Operational authority: behavior permitted, blocked, or changed: Schedules ingestion; malformed input may block scheduling.
Behavioral-authority path: consumer, channel, force, horizon: Worker; process-local queue; permissive then core effects; until processing/process loss.
Evidence source ID and local anchor: see [RT-RTE-service-admission](runtime.md#rt-rte-service-admission).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No durable completion or approval follows queue success.

Route ID: [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge) and [EPI-OBJ-entity-node](#epi-obj-entity-node) and [EPI-OBJ-community-node](#epi-obj-community-node)
Content/update relation: no content change
Transition or check target: Ranking/filtering selected graph context for query.
Evaluator/condition and domain: Symbolic/numerical similarity and optional model relevance; query-relevance domain.
Activation and timing: see [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval); operation unobserved.
Possible or observed result: Ranked results; see [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval).
Implemented force: Ranking and selection.
Epistemic authority and scope: Retrieval rank does not warrant truth.
Operational authority: behavior permitted, blocked, or changed: Determines what caller receives and may use.
Behavioral-authority path: consumer, channel, force, horizon: Caller/core extraction context/service response; selected graph parts; advisory/ranking; invocation and later caller behavior.
Evidence source ID and local anchor: see [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No measured relevance or correctness; filters and date fields need caller use.

Route ID: [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge)
Content/update relation: no content change
Transition or check target: Selected facts delivered to conversational model.
Evaluator/condition and domain: Notebook formatting/scheduler, then opaque model interpretation.
Activation and timing: see [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop); operation unobserved.
Possible or observed result: Fact strings in system message/tool return.
Implemented force: Requested natural-language influence, not enforced factual compliance.
Epistemic authority and scope: Metadata and dates omitted; reliance channel degrades accessible lineage.
Operational authority: behavior permitted, blocked, or changed: May change answer/tool selection; actual activation unobserved.
Behavioral-authority path: consumer, channel, force, horizon: See [RT-BAP-facts-context](runtime.md#rt-bap-facts-context).
Evidence source ID and local anchor: see [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: Full lineage not delivered by this facts-only channel.
Gap/limit: Delivery is wired, not compliance, correctness or benefit.

Route ID: [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episodic-node](#epi-obj-episodic-node)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Latest state message object and newly generated response.content recorded together; post-tool input and intermediate tool-call responses are included.
Evaluator/condition and domain: Notebook schedules async ingestion after every successful model response, without checking message origin or waiting for a completed user turn.
Activation and timing: see [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop); operation unobserved.
Possible or observed result: Mixed-origin candidate episode.
Implemented force: Permissive automatic memory admission.
Epistemic authority and scope: Human-, model- and tool-derived statements have unknown source warrant; retaining them does not validate them. The unconditional user-name prefix on the latest state message does not license human origin.
Operational authority: behavior permitted, blocked, or changed: Can feed future extraction/search after completion.
Behavioral-authority path: consumer, channel, force, horizon: Episode ingester then later model; mixed conversation text; advisory future input; availability timing unresolved.
Evidence source ID and local anchor: see [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: May recirculate model errors or tool-returned graph facts. Async scheduling establishes neither completed persistence nor one write per completed user turn; no claim of exercised or improved learning.

Route ID: [EPI-RTE-episode-removal](#epi-rte-episode-removal)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episodic-node](#epi-obj-episodic-node) and [EPI-OBJ-entity-edge](#epi-obj-entity-edge) and [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: no content change
Transition or check target: Episode removal and dependent graph withdrawal.
Evaluator/condition and domain: Software first-origin edge criterion and node mention counts.
Activation and timing: see [EPI-RTE-episode-removal](#epi-rte-episode-removal); operation unobserved.
Possible or observed result: Delete selected edges/nodes and episode; see [EPI-RTE-episode-removal](#epi-rte-episode-removal).
Implemented force: Enforcing deletion requests.
Epistemic authority and scope: Withdrawal is not truth adjudication or complete restoration.
Operational authority: behavior permitted, blocked, or changed: Reduces future graph availability, including potentially multiply referenced facts.
Behavioral-authority path: consumer, channel, force, horizon: Core delete APIs via MCP; UUID deletion calls; enforcing; future reads after success.
Evidence source ID and local anchor: see [EPI-RTE-episode-removal](#epi-rte-episode-removal).
Claim IDs or none: [EPI-CLM-cleanup-contract](#epi-clm-cleanup-contract)
Mismatch marker or none: MCP sole-support description disagrees with first-origin edge criterion.
Gap/limit: No shown retraction of prior notebook answers or regeneration of summaries.

Route ID: [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge) and [EPI-OBJ-entity-node](#epi-obj-entity-node)
Content/update relation: no content change
Transition or check target: Candidate AddEpisodeResults compared with model-built baseline.
Evaluator/condition and domain: Model judge; relative graph-building quality on selected message dataset.
Activation and timing: see [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison); operation unobserved.
Possible or observed result: candidate_is_worse and aggregate not-worse fraction.
Implemented force: Scoring only.
Epistemic authority and scope: Reference is not independently certified world truth; missing key defaults to not worse.
Operational authority: behavior permitted, blocked, or changed: Changes reported score, not production admission.
Behavioral-authority path: consumer, channel, force, horizon: Evaluation script/operator; printed/returned score and exported JSON; advisory measurement; experiment.
Evidence source ID and local anchor: see [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Character-sliced context and non-strict zip weaken intended comparison; no execution or component intervention.

Route ID: [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-attributes](#epi-obj-entity-attributes)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Node attribute candidates from episode context, existing attributes and configured entity type.
Evaluator/condition and domain: Configured model; schema-specific descriptive predicates.
Activation and timing: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Possible or observed result: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Implemented force: Candidate generation.
Epistemic authority and scope: Request for extraction, not checked source entailment.
Operational authority: behavior permitted, blocked, or changed: Candidate values enter overlay/shape validation.
Behavioral-authority path: consumer, channel, force, horizon: Attribute merger; typed model response; permissive proposal; ingestion.
Evidence source ID and local anchor: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Actual values needed to distinguish reshaping, entailed interpretation and unsupported conjecture.

Route ID: [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-attributes](#epi-obj-entity-attributes)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Admitting node fields while retaining omitted/cap-dropped prior values.
Evaluator/condition and domain: Software overlay and Pydantic shape validation, not factual evaluation.
Activation and timing: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Possible or observed result: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Implemented force: Enforcing field retention/assignment.
Epistemic authority and scope: Operational schema admission, not warranted factual acceptance.
Operational authority: behavior permitted, blocked, or changed: Invalid merged shape can fail processing; allowed fields affect later context.
Behavioral-authority path: consumer, channel, force, horizon: Node writer/identity context; attribute properties; enforcing representation and advisory semantics; future calls.
Evidence source ID and local anchor: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Capping/coercion internals not audited, so this relation covers overlay preservation, not every value transformation.

Route ID: [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge), attributes part
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Edge attribute candidates from fact text and applicable relation schema.
Evaluator/condition and domain: Configured model with fact/reference-time/existing-attributes context; relation-specific predicates.
Activation and timing: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Possible or observed result: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Implemented force: Candidate generation.
Epistemic authority and scope: Source warrant cannot exceed the fact input; no independent fidelity check.
Operational authority: behavior permitted, blocked, or changed: Applicable model output enters edge attribute merge.
Behavioral-authority path: consumer, channel, force, horizon: Edge attribute merger; structured response; permissive; ingestion/triplet resolution.
Evidence source ID and local anchor: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Actual output/source comparison needed to classify semantic change.

Route ID: [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge), attributes part
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Edge attribute field replacement from the applicable response.
Evaluator/condition and domain: Software capped-attribute merger invoked with replace rather than node overlay semantics.
Activation and timing: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Possible or observed result: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Implemented force: Enforcing attribute assignment.
Epistemic authority and scope: Representation admission, not factual acceptance.
Operational authority: behavior permitted, blocked, or changed: Changes saved edge attributes and later consumers' available fields.
Behavioral-authority path: consumer, channel, force, horizon: Edge writer/readers; attribute properties; enforcing storage and advisory semantics; future calls.
Evidence source ID and local anchor: see [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction).
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Relation applies to field replacement only; capping/coercion fidelity remains uninspected.

Route ID: [EPI-RTE-provenance-read](#epi-rte-provenance-read)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entity-edge](#epi-obj-entity-edge) and [EPI-OBJ-edge-episodes](#epi-obj-edge-episodes) and [EPI-OBJ-edge-validity](#epi-obj-edge-validity)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: UUID edge retrieval to serialized MCP response.
Evaluator/condition and domain: UUID lookup and formatter, not truth or relevance evaluation.
Activation and timing: see [EPI-RTE-provenance-read](#epi-rte-provenance-read).
Possible or observed result: see [EPI-RTE-provenance-read](#epi-rte-provenance-read).
Implemented force: Requested delivery.
Epistemic authority and scope: Existing metadata made inspectable without certification.
Operational authority: behavior permitted, blocked, or changed: Host can inspect fact plus retained temporal/provenance fields; no automatic source check.
Behavioral-authority path: consumer, channel, force, horizon: MCP caller; structured JSON without embeddings; advisory; tool invocation.
Evidence source ID and local anchor: see [EPI-RTE-provenance-read](#epi-rte-provenance-read).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: Countercase to universal claims of metadata loss in retrieval.
Gap/limit: Fields may be empty and raw sources need a further read; host use unobserved.

Route ID: [EPI-RTE-provenance-read](#epi-rte-provenance-read)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episodic-node](#epi-obj-episodic-node)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Group-scoped recent episode retrieval to MCP content/source response.
Evaluator/condition and domain: Group selectors, created-time sorting and limit, not factual acceptance.
Activation and timing: see [EPI-RTE-provenance-read](#epi-rte-provenance-read).
Possible or observed result: see [EPI-RTE-provenance-read](#epi-rte-provenance-read).
Implemented force: Requested delivery.
Epistemic authority and scope: Preserves available source text/descriptors through this formatter; original warrant remains unknown.
Operational authority: behavior permitted, blocked, or changed: Caller can inspect available raw content; this operation is not targeted retrieval by fact's episode IDs.
Behavioral-authority path: consumer, channel, force, horizon: MCP caller; episode response content/source fields; advisory; tool invocation.
Evidence source ID and local anchor: see [EPI-RTE-provenance-read](#epi-rte-provenance-read).
Claim IDs or none: [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance)
Mismatch marker or none: none
Gap/limit: Empty/no effective groups return no episodes; previously stripped content cannot be recovered here.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance) | see [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance) | SRC-1 `README.md`; doctrine/design | see [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance) | [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [EPI-RTE-fact-comparison](#epi-rte-fact-comparison), [EPI-RTE-fact-disposition](#epi-rte-fact-disposition), [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes), [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval), [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop) | None supplied | No measured truth, full lineage delivery or quality; direct admission and raw-content removal are countercases | Temporal representation and history handling are implemented; metadata supports tracing in covered paths | “What's true” exceeds warranted truth; “every”/“full” source lineage is conditional, and notebook facts omit it. |
| [EPI-CLM-cleanup-contract](#epi-clm-cleanup-contract) | see [EPI-CLM-cleanup-contract](#epi-clm-cleanup-contract) | SRC-1 `mcp_server/src/graphiti_mcp_server.py`; doctrine/design | see [EPI-CLM-cleanup-contract](#epi-clm-cleanup-contract) | [EPI-RTE-episode-removal](#epi-rte-episode-removal) | None supplied | No executed deletion; core edge criterion differs from prose | MCP calls core removal, but sole-support preservation is not its actual edge test | Needed qualification of deletion guarantee, not a change to boundary or supplied runtime facts. |
| [RT-CLM-schema-boundary](runtime.md#rt-clm-schema-boundary) | see [RT-CLM-schema-boundary](runtime.md#rt-clm-schema-boundary) | see record | see record | [RT-RTE-prompt-routing](runtime.md#rt-rte-prompt-routing) | Uninspected | Supplied guarantee is correctly scoped to registry/dispatch | Response-schema restrictions are not source-truth acceptance | Client/SDK bypasses retained; no supersession needed. |

## Bounded conclusion

Graphiti imports episodes and supplied graph claims with **unknown source warrant**. It requests textual extraction, entity identity resolution, temporal interpretation, attributes and summaries. Built-in fact instructions demand stated or unambiguously implied relationships, but requesting this behavior is not checked entailment. Particular model outputs could preserve meaning, derive an implicit relation or introduce unsupported content; absent output comparisons those transformations remain indeterminate, not automatically classified as ampliative conjecture. See [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).

Two narrower implemented transformations have firmer classifications. Exact fact normalization lowercases and collapses whitespace before an endpoint-constrained match; it establishes string equality in that domain, not world truth. Short entity summaries concatenate already available facts without model generation. Their warrant cannot exceed their inputs. No newly produced accepted ampliative world claim is established by either transformation. See [EPI-RTE-fact-comparison](#epi-rte-fact-comparison) and [EPI-RTE-entity-summary](#epi-rte-entity-summary).

Semantic comparisons have consequential consumers. Model duplicate/contradiction judgments and software index/date checks change identities and temporal fields before future retention/use. The comparison criterion is semantic sameness or mutual inconsistency within selected graph candidates; the disposition criterion is valid indices and temporal overlap/order. Intended use is graph reconciliation, with enforcing authority over stored identities and date fields, not certified correctness. Bounds checks reject malformed decisions, not false facts. Novel candidates with no comparisons can still proceed; exact-match reuse can bypass model contradiction checking. See [EPI-RTE-fact-comparison](#epi-rte-fact-comparison) and [EPI-RTE-fact-disposition](#epi-rte-fact-disposition).

Production retention, summary replacement, community organization and saga watermarks do not record a separate evidence-consuming acceptance decision that licenses a claim as true for a named use. They are useful operational machinery without thereby becoming epistemic acceptance or lifecycle integration after acceptance. This is a bounded finding over the inspected routes, not a system-complete negative about every uninspected prompt, caller or deployment. See [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion), [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) and [EPI-RTE-entity-summary](#epi-rte-entity-summary).

Retrieval grants ranking/delivery authority, not truth authority. The notebook places fact strings in a model system message and asynchronously schedules recording of the latest state message object plus newly generated response content after every successful model call. The latest message can be human input, a post-tool result or a model message in supplied state; even intermediate tool-call responses trigger scheduling. The user-name adapter prefix does not establish human origin. Tool results can contain retrieved graph facts, so retained material can recirculate through tool and model channels with unknown source warrant. This is a wired behavioral-authority path and trace-fed update, not observed compliance, improved capacity, reflective criticism or exercised self-improvement. MCP instructions request stronger procedural reliance, but host loading/compliance remain unknown. Direct writes, raw-content omission and facts-only formatting limit public full-lineage claims. Metadata loss is channel-specific: MCP direct edge/fact formatting excludes embeddings but retains other model fields, while recent-episode retrieval delivers available raw content/source descriptors. See [EPI-RTE-provenance-read](#epi-rte-provenance-read) for this countercase. Typed attribute admission also differs by part: node overlay preserves omitted values, while edge extraction invokes replacement; neither shape check certifies its values. See [EPI-RTE-attribute-extraction](#epi-rte-attribute-extraction). See [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval), [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop), [RT-BAP-facts-context](runtime.md#rt-bap-facts-context), [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions) and [EPI-CLM-temporal-provenance](#epi-clm-temporal-provenance).

Removal is a separate enforcing withdrawal route, not a correctness evaluator. The core deletes an edge when the removed episode is its first episode reference even if later references exist; that challenges the MCP description of preserving multiply supported facts. Summary/answer rollback is not established by the inspected deletion function. See [EPI-RTE-episode-removal](#epi-rte-episode-removal) and [EPI-CLM-cleanup-contract](#epi-clm-cleanup-contract).

The evaluator compares candidate graphs with a model-produced baseline and returns a score; it neither supplies independent factual truth nor installs a winner in the inspected CLI/function. Character-sliced context, non-strict pairing and default not-worse interpretation bound even its intended relative judgment. No run or causal outcome evidence supports accuracy, benefit or component attribution. See [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison).

Distributed-parametric model state remains locally bounded: the supplied component records separately establish inference adapters, unpinned model identities/mutable endpoints and uninspected provider-side changes. No weight-training request is shown by those adapters; that does not rule out learning through retained graph material, nor establish learning benefit. See [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client), [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder), [RT-CMP-openai-reranker-client](runtime.md#rt-cmp-openai-reranker-client), [RT-CMP-gliner2-client](runtime.md#rt-cmp-gliner2-client) and [RT-CMP-chat-openai](runtime.md#rt-cmp-chat-openai). These independent properties yield no single epistemic score or unqualified system verdict.

## Shared records

### Operative objects

#### EPI-OBJ-episodic-node
Label: EpisodicNode input assertions

Source-native identity: `EpisodicNode.content`, with source/source_description. Natural-language or serialized source content on graph storage; fields and UUID/time references have symbolic consumers. Candidate truth-apt content is the assertions in an episode, not its source-type enum. Closest supplied record: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) is a route containing its processing, not an object counterpart. This declaration distinguishes source text from extracted graph statements; runtime declares no operative-object counterpart. In the shipped notebook, the episode combines the latest state message object with the new model response content, including post-tool input and intermediate responses. Human, model and tool origins can therefore mix; the unconditional user-name prefix does not establish human origin. Scheduling is automatic after each successful model call, not limited to completed user turns, and does not prove persistence. See [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop) for the producer and its scheduling/scheduler passages. SRC-1 implementation: `graphiti_core/nodes.py`, `examples/langgraph-agent/agent.ipynb`.

> content: str = Field(description='raw episode data')
> --- `graphiti_core/nodes.py`

#### EPI-OBJ-entity-node
Label: EntityNode identity and description

Source-native identity: `EntityNode.name`, labels, attributes and summary. Graph properties carry natural-language descriptions plus symbolic identity/type/attribute keys; name embeddings are separate dense numerical retrieval material. Candidate truth-apt content includes who/what a node identifies and descriptive assertions. Identity candidates reach deduplication; summary text reaches later identity context and summarization; attributes have schema-dependent consumers. Closest supplied [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) describes the enclosing processing route, not an object counterpart. The following routes separate checks and consumers of these parts. SRC-1 implementation: `graphiti_core/nodes.py`, `graphiti_core/utils/maintenance/node_operations.py`.

> 'summary': candidate.summary[:120] if candidate.summary else '',
> --- `graphiti_core/utils/maintenance/node_operations.py`

#### EPI-OBJ-entity-edge
Label: EntityEdge fact and temporal lineage

Source-native identity: `EntityEdge.fact` is natural-language relational assertion in graph properties. Endpoint UUIDs, episode references, valid_at/invalid_at/expired_at and attributes are symbolic graph metadata; fact_embedding is a dense numerical selection representation, not a recovered proposition. Facts assert relationships over entity/time scope; timestamps encode proposed validity and software withdrawal. These parts are assessed separately in extraction, comparison, disposition, retention and retrieval rows. Closest supplied [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval) are producer/consumer routes, not object duplicates. SRC-1 implementation: `graphiti_core/edges.py`.

> description='datetime of when the fact stopped being true; soft deadlines are not invalid_at',
> --- `graphiti_core/edges.py`

#### EPI-OBJ-edge-duplicate
Label: EdgeDuplicate semantic judgment indices

Source-native identity: `EdgeDuplicate.duplicate_facts` and `contradicted_facts`. Transient symbolic integer lists in a structured model response; their interpreted content is equivalence or mutual inconsistency of selected fact assertions. They are judgments about text, not newly verified world observations. Distinct from the fact strings on which they operate and from the enclosing [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion); no runtime object counterpart is declared. SRC-1 implementation/doctrine: `graphiti_core/prompts/dedupe_edges.py`; implementation consumer: `graphiti_core/utils/maintenance/edge_operations.py`.

> - duplicate_facts: ONLY idx values from EXISTING FACTS (NEVER include FACT INVALIDATION CANDIDATES)
> - contradicted_facts: idx values from EITHER list (EXISTING FACTS or FACT INVALIDATION CANDIDATES)
> --- `graphiti_core/prompts/dedupe_edges.py`

#### EPI-OBJ-community-node
Label: CommunityNode synthesized descriptions

Source-native identity: `CommunityNode.name` and summary carry natural-language generated description on graph storage; community membership edges are symbolic organization; embeddings select rather than warrant text. Candidate content is descriptive assertions inherited or synthesized from entity summaries. The generator pairs summaries recursively and generates a name from the final text. Closest supplied [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) contains rebuild/update operations, not an object counterpart. SRC-1 implementation: `graphiti_core/utils/maintenance/community_operations.py`.

> summary = truncate_at_sentence(summaries[0], MAX_SUMMARY_CHARS)
> name = await generate_summary_description(llm_client, summary, clients=clients)
> --- `graphiti_core/utils/maintenance/community_operations.py`

#### EPI-OBJ-saga-node
Label: SagaNode incremental summary and coverage

Source-native identity: saga summary is natural-language description on graph storage; ingestion/event-time watermarks are symbolic selection state. Summary assertions may span multiple episodes; the timestamp maximum does not certify each assertion's temporal scope or completeness. Closest supplied [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) owns the enclosing route, not an object counterpart. SRC-1 implementation: `graphiti_core/graphiti.py`.

> saga.summary = summary
> # Ingestion-time watermark for the next-run filter. Advance only
> # through the episodes that were actually sent to the summary prompt so
> # byte-budgeted later episodes remain reachable on subsequent runs.
> saga.last_summarized_at = max(summarized_created_ats) if summarized_created_ats else None
> --- `graphiti_core/graphiti.py`

#### EPI-OBJ-entity-attributes
Label: EntityNode schema attributes
Part of: [EPI-OBJ-entity-node](#epi-obj-entity-node)

Source-native identity: `EntityNode.attributes`, graph-stored symbolic keys/typed values with schema-dependent truth-apt predicates and potentially natural-language values. Producers are model extraction or caller writes; later identity/context consumers use the properties. Unlike summary text, typed extraction applies a schema and overlay merge. Prior values survive when no type applies or a field is omitted/cap-dropped. SRC-1 implementation: `graphiti_core/utils/maintenance/node_operations.py`. This is an operative part of the local object container, not a duplicate of runtime ingestion.

> # Overlay merge: cap-dropped or LLM-omitted fields keep prior values.
> # See attribute_utils for the merge_mode contract; the edge path uses 'replace'.
> --- `graphiti_core/utils/maintenance/node_operations.py`

> entity_type(**merged)
> --- `graphiti_core/utils/maintenance/node_operations.py`

#### EPI-OBJ-entity-summary
Label: EntityNode descriptive summary
Part of: [EPI-OBJ-entity-node](#epi-obj-entity-node)

Source-native identity: `EntityNode.summary`, natural-language descriptive assertions in graph properties. Produced by literal fact appending, model summarization or caller supply; consumed in later dedupe context and summarization/search. Different from identity keys and typed attributes. Its production evidence is retained by [EPI-RTE-entity-summary](#epi-rte-entity-summary). SRC-1 implementation: `graphiti_core/nodes.py`.

> summary: str = Field(description='regional summary of surrounding edges', default_factory=str)
> --- `graphiti_core/nodes.py`

#### EPI-OBJ-edge-validity
Label: EntityEdge temporal scope fields
Part of: [EPI-OBJ-entity-edge](#epi-obj-entity-edge)

Source-native identity: `valid_at`, `invalid_at`, `expired_at`, `reference_time`. Symbolic datetime graph properties interpret proposed fact scope, processing withdrawal time and source reference time. Model extraction and software temporal policy produce/update them; date-aware selectors and reconciliation consume them. Their semantics are not identical: expiration records invalidation rather than independently proving when a world event occurred. See [EPI-RTE-fact-disposition](#epi-rte-fact-disposition) for update evidence. SRC-1 implementation: `graphiti_core/edges.py`.

> reference_time: datetime | None = Field(
>     default=None, description='reference timestamp from the episode that produced this edge'
> )
> --- `graphiti_core/edges.py`

#### EPI-OBJ-edge-episodes
Label: EntityEdge episode references
Part of: [EPI-OBJ-entity-edge](#epi-obj-entity-edge)

Source-native identity: `EntityEdge.episodes`, symbolic UUID list on graph storage. It asserts source/reference associations used in tracing, duplicate provenance appending and episode withdrawal. Model episode indices are range-filtered; an empty resulting attribution list falls back to all episodes, so this is not a checked proof of per-fact entailment by each associated source. Direct supplied writes may have no episode lineage. SRC-1 implementation: `graphiti_core/utils/maintenance/edge_operations.py`.

> if not edge_episode_uuids:
>     edge_episode_uuids = [ep.uuid for ep in episodes]
> --- `graphiti_core/utils/maintenance/edge_operations.py`

#### EPI-OBJ-edge-embedding
Label: EntityEdge fact embedding
Part of: [EPI-OBJ-entity-edge](#epi-obj-entity-edge)

Source-native identity: `fact_embedding`, distributed-parametric dense numerical representation stored as graph properties. The embedding provider encodes fact text with newlines replaced by spaces; similarity selectors consume it. No independently individuated truth-apt proposition is established inside this encoding, and its stored presence does not authenticate the assertion. This is separate from provider weights in [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder). SRC-1 implementation: `graphiti_core/edges.py`.

> text = self.fact.replace('\n', ' ')
> self.fact_embedding = await embedder.create(input_data=[text])
> --- `graphiti_core/edges.py`

#### EPI-OBJ-saga-watermarks
Label: SagaNode input coverage watermarks
Part of: [EPI-OBJ-saga-node](#epi-obj-saga-node)

Source-native identity: `last_summarized_at` and `last_summarized_episode_valid_at`, symbolic graph timestamps. The first controls later ingestion-time input selection; the second records latest summarized episode reference time for public temporal consumers. They describe selected-input coverage, not summary truth. Persistence/update evidence is in [EPI-OBJ-saga-node](#epi-obj-saga-node) and the supplied [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes). SRC-1 implementation: `graphiti_core/graphiti.py`.

### Routes

#### EPI-RTE-fact-extraction
Label: Fact extraction candidates
Part of: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)

This route is the edge-candidate production part of the supplied episode ingestion route, not a replacement for that container. Owner: `extract_edges`; endpoints are episode/prior context/entities/reference time → configured prompt/model → typed relational edge candidates. Model proposes assertions; code validates/materializes endpoints and temporal/schema data before later resolution. Open caller-triggered production, not a bounded experiment; no certified expected answer, source-truth oracle or per-fact human veto is established. Instructions demand relationships stated or unambiguously implied by the current message and restrict prior messages to reference/continuity support. Such guidance intends faithful extraction but does not implement an entailment proof. Failures or invalid candidates can prevent downstream processing; recovery belongs to caller repair/retry, not an evidenced all-or-nothing rollback. Candidate content and applicable metadata persist through the parent route. Two inspection countercases limit the prompt's apparent guarantees: missing endpoint names are materialized rather than always rejected as the prompt warns; invalid/empty episode attribution falls back to all episodes. These are representational repair/admission choices, not truth validation. SRC-1 implementation: `graphiti_core/utils/maintenance/edge_operations.py`; doctrine/design: `graphiti_core/prompts/extract_edges.py`.

- Immediate return: extracted edge candidates plus any materialized endpoints to the ingestion caller.
- Later read-back: candidates that persist can enter future retrieval, resolution and summary context via the parent route.
- Delegated visibility: configured model receives current message, selected previous context, entities, reference time and custom instructions.
- Selection predicate: caller episode and selected entities/types/context; strict type instructions can restrict output relation types.
- Invalidation or expiry: subsequent resolution and caller deletion, not generation alone.
- Activation or effect: candidate generation and downstream submission are wired; faithful model extraction is unobserved.
- Evidence limits: actual outputs and checked interpretation missing; not every prompt/provider variant inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> - are clearly stated or unambiguously implied in the CURRENT MESSAGE,
>     and can be represented as edges in a knowledge graph.
> --- `graphiti_core/prompts/extract_edges.py`

> You may use information from the PREVIOUS MESSAGES only to disambiguate references or support continuity.
> --- `graphiti_core/prompts/extract_edges.py`

> source_node = name_to_node.get(_normalize_string_exact(source_name))
> if source_node is None:
>     source_node = materialize_dangling_endpoint_node(
> --- `graphiti_core/utils/maintenance/edge_operations.py`

#### EPI-RTE-fact-comparison
Label: Fact duplicate and contradiction comparison
Part of: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)

This is the fact-comparison part of ingestion, distinct from generation and from disposition. Owner: `_dedupe_extracted_edge`; inputs new edge plus related/invalidation candidates → exact-match shortcut or model EdgeDuplicate → resolution inputs. Target/domain: normalized fact text and endpoints for exact equivalence, otherwise semantic equivalence/mutual inconsistency among selected natural-language statements. Model proposes judgments; software supplies candidates and validates indices. No independent oracle verifies either assertion's truth. Open ingestion invocation, with configured prompt guidance and no demonstrated human per-comparison approval. The no-candidate branch skips duplicate/contradiction comparison while still allowing applicable attributes/timestamp processing.

Concrete implementation deduction, without target execution: `_normalize_string_exact('  Alice\tOWNS  Shoes ')` lowercases, collapses whitespace and strips to `alice owns shoes`; a related edge with `Alice owns shoes` and the same ordered endpoint UUIDs satisfies the fast-path predicate. The existing edge is returned and the episode UUID added if new. This is exact normalized-string reuse, not case-sensitive equality, semantic proof, or a new-world-fact derivation. The shortcut returns `None` for invalidation candidates, so a claim that every reuse undergoes model contradiction checking would be false. Endpoint mismatch fails this shortcut. SRC-1 implementation: `graphiti_core/utils/maintenance/dedup_helpers.py`, `graphiti_core/utils/maintenance/edge_operations.py`; doctrine: `graphiti_core/prompts/dedupe_edges.py`.

- Immediate return: resolved edge/duplicate information and selected invalidation candidates, or early-return marker.
- Later read-back: comparison-controlled identity and provenance changes reach future graph consumers through persistence.
- Delegated visibility: model receives candidate fact strings and indices, not independently authenticated source observations.
- Selection predicate: retrieved related and invalidation candidates; exact normalized fact plus ordered endpoint equality for shortcut.
- Invalidation or expiry: this comparison supplies candidates; the separate temporal disposition route applies withdrawal.
- Activation or effect: semantic judgments have wired consumers; their accuracy and execution remain unobserved.
- Evidence limits: candidate recall and model judgment reliability unmeasured; exact match licenses only its string/endpoint domain.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> normalized = re.sub(r'[\s]+', ' ', name.lower())
> return normalized.strip()
> --- `graphiti_core/utils/maintenance/dedup_helpers.py`

> resolved = edge
> if episode is not None and episode.uuid not in resolved.episodes:
>     resolved.episodes.append(episode.uuid)
> return resolved, [], None
> --- `graphiti_core/utils/maintenance/edge_operations.py`

> Only mark a fact as contradicted when the NEW FACT and the existing fact cannot both be true.
> --- `graphiti_core/prompts/dedupe_edges.py`

#### EPI-RTE-fact-disposition
Label: Fact identity and temporal disposition
Part of: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)

This is the interpreted-result/disposition part, not another declaration of comparison. Owners: `_dedupe_extracted_edge`, `_apply_temporal_invalidation`, `resolve_edge_contradictions`. Model judges candidate relations; software chooses the first valid duplicate and filters invalid indices. Timestamp comparison then controls which existing/resolved edge receives invalid_at/expired_at. Newer contradictory candidates can expire the incoming edge instead; nonoverlapping intervals are skipped, and an old candidate must start earlier to be invalidated by a newer edge. This is operational graph reconciliation against indices and dates, not an evidence-consuming acceptance decision that a fact is true. Trigger is open caller ingestion; guidance is comparison/temporal policy, and dates/identities persist through the parent route. No certified desired graph, human veto or invocation rollback established. SRC-1 implementation: `graphiti_core/utils/maintenance/edge_operations.py`.

- Immediate return: selected resolved edge and invalidated-edge list for later persistence.
- Later read-back: saved identities/date fields affect later graph resolution and date-aware selection.
- Delegated visibility: persistence receives modified graph objects; model judgment is already supplied by comparison.
- Selection predicate: valid duplicate/contradiction indices and time overlap/order; first valid duplicate chosen.
- Invalidation or expiry: updates invalid_at and expired_at rather than deleting contradicted history in this route.
- Activation or effect: field updates are wired; downstream filtering depends on recipe/caller and operation unobserved.
- Evidence limits: no source-truth oracle, full comparison coverage, or guaranteed temporal accuracy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> duplicate_fact_ids: list[int] = [i for i in duplicate_facts if 0 <= i < len(related_edges)]
> --- `graphiti_core/utils/maintenance/edge_operations.py`

> for duplicate_fact_id in duplicate_fact_ids:
>     resolved_edge = related_edges[duplicate_fact_id]
>     break
> --- `graphiti_core/utils/maintenance/edge_operations.py`

> edge.invalid_at = resolved_edge.valid_at
> edge.expired_at = edge.expired_at if edge.expired_at is not None else utc_now()
> invalidated_edges.append(edge)
> --- `graphiti_core/utils/maintenance/edge_operations.py`

#### EPI-RTE-entity-summary
Label: Entity summary append or synthesis
Part of: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)

Owner: `_extract_entity_summaries_batch` and `_process_summary_flight`. Distinct part of ingestion, not its whole producer route. Inputs node summaries, edges and applicable episode context → conditional literal append or configured model → summary assignment → parent persistence. Optional callback can exclude nodes; `skip_fact_appending` forces the episode-based model branch when content exists. Short combined summary uses literal edge.fact concatenation, while long/empty-with-episode cases can invoke model summarization. Returned model summaries are matched by case-insensitive name and truncated; unknown names warn rather than changing a node. Model proposes text; software name/length checks admit it for descriptive use. Caller human control is unresolved; there is no independent expected summary or entailment oracle. Open ingestion, not an autonomous improvement experiment. The summary supplies later identity/model/search context; retention is not acceptance of generated claims. Exceptions interrupt processing; no general rollback shown. SRC-1 implementation: `graphiti_core/utils/maintenance/node_operations.py`.

Concrete deterministic deduction: existing `node.summary = 'Alice lives in Paris.'` and one nonempty edge.fact `Alice owns shoes.` yield the two strings separated by a newline under the short-summary branch. The assignment introduces no new proposition beyond the input strings, although it does not check their consistency or currentness. For the model branch, semantic-preservation/entailed/ampliative alternatives remain indeterminate absent particular outputs.

- Immediate return: in-place modified node summaries after applicable branch.
- Later read-back: persisted summary reaches future dedupe candidate context and later summary inputs/search results.
- Delegated visibility: model branch receives node descriptions/attributes and applicable episode context; append branch needs no model.
- Selection predicate: callback, skip_fact_appending flag, available edges/context and combined text length.
- Invalidation or expiry: later summary assignment replaces text; no separate factual expiry/retraction policy shown here.
- Activation or effect: summary assignment and consumer context supply wired; correctness and behavioral benefit unobserved.
- Evidence limits: text match/truncation is not entailment; all persistence-side caps and consumer variants not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> edge_facts = '\n'.join(edge.fact for edge in node_edges if edge.fact)
> summary_with_edges = f'{summary_with_edges}\n{edge_facts}'.strip()
> --- `graphiti_core/utils/maintenance/node_operations.py`

> if summary_with_edges and len(summary_with_edges) <= MAX_SUMMARY_CHARS * 2:
>     node.summary = summary_with_edges
>     continue
> --- `graphiti_core/utils/maintenance/node_operations.py`

> for node in matching_nodes:
>     node.summary = truncated_summary
> --- `graphiti_core/utils/maintenance/node_operations.py`

#### EPI-RTE-episode-removal
Label: Episode removal dependent withdrawal
Part of: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)

Owner: `Graphiti.remove_episode`, exposed by MCP `delete_episode`. This is the deletion part of the supplied maintenance container, not a duplicate of its summary/direct-write mechanisms. Endpoints caller UUID → episode and referenced edges → first-origin edge selection and mention-count node selection → deletion → episode deletion. Caller proposes/removes, software decides cascade membership; no truth oracle or per-edge human approval. Open explicit maintenance, not evidence-driven acceptance. Guidance is creation/mention policy, whose persisted consequence is deletion. Node criterion counts mentions; edge criterion checks the first episode reference, not sole support. Hence a fact with references `[removed_episode, later_episode]` is selected for deletion by inspected code even though the MCP docstring says multiply supported facts are preserved. This deterministic code countercase needs no execution to challenge the contract. Recovery is explicit repair/reingestion, not restoration of prior state. SRC-1 implementation: `graphiti_core/graphiti.py`, `mcp_server/src/graphiti_mcp_server.py`.

- Immediate return: core completion without an explicit value; MCP success/error wrapper after await.
- Later read-back: deleted content becomes unavailable to later graph consumers conditional on successful database effects.
- Delegated visibility: driver receives UUID deletions and node mention-count query; no model evaluator invoked here.
- Selection predicate: edge.episodes exists and first UUID equals removed episode; nodes have one mention; exact episode UUID.
- Invalidation or expiry: physical withdrawal rather than temporal marking; no shown summary/previous-answer regeneration.
- Activation or effect: deletion requests wired; actual complete cascade and deployed backend outcome unobserved.
- Evidence limits: multi-backend parity and whole-deletion atomicity not established; failed writes can limit withdrawal.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if edge.episodes and edge.episodes[0] == episode.uuid:
>     edges_to_delete.append(edge)
> --- `graphiti_core/graphiti.py`

> await Edge.delete_by_uuids(self.driver, [edge.uuid for edge in edges_to_delete])
> await Node.delete_by_uuids(self.driver, [node.uuid for node in nodes_to_delete])
> --- `graphiti_core/graphiti.py`

#### EPI-RTE-attribute-extraction
Label: Typed node and edge attribute admission
Part of: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)

Distinct attribute-production/admission part of the ingestion container, not a replacement for its other functions. Owners: `_extract_entity_attributes` and applicable edge-resolution branches. Node input is episode context plus prior attributes, with summary excluded; applicable entity schema shapes model output. If no entity schema/fields apply, prior attributes are returned unchanged. Node overlay merge preserves omitted/cap-dropped prior fields and Pydantic validates merged shape. Edge input is fact/reference time/prior attributes; applicable edge model output passes a merger invoked with `replace` and is assigned to edge attributes. Models propose values; software admits representation. Caller supplies schemas/invocations, but human per-field veto is unresolved; no certified expected values or factual oracle. Open production requests, shaped by named attribute prompts/schema policy; changes persist via graph writers. Exceptions can fail processing; no whole-call rollback established. These branches do not prove semantic preservation; transformation classification remains separate from representation acceptance. SRC-1 implementation: `graphiti_core/utils/maintenance/node_operations.py`, `graphiti_core/utils/maintenance/edge_operations.py`.

- Immediate return: merged node attributes or in-place edge attribute assignment.
- Later read-back: saved values reach later identity/extraction context and graph readers.
- Delegated visibility: configured model receives applicable node episode context or edge fact/reference-time/attribute context and response schema.
- Selection predicate: applicable entity/relation model with fields; absent entity model preserves prior values.
- Invalidation or expiry: subsequent field updates or graph deletion; no factual expiry proof in attribute admission.
- Activation or effect: field admission/assignment wired; true values and benefit unobserved.
- Evidence limits: cap/coercion helper internals and all schemas not audited; no independent per-value entailment check.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if entity_type is None or len(entity_type.model_fields) == 0:
> --- `graphiti_core/utils/maintenance/node_operations.py:1040-1040`

> merge_mode='overlay',
> prompt_name='extract_nodes.extract_attributes',
> --- `graphiti_core/utils/maintenance/node_operations.py`

> merge_mode='replace',
> prompt_name='extract_edges.extract_attributes',
> --- `graphiti_core/utils/maintenance/edge_operations.py:929-930`

#### EPI-RTE-provenance-read
Label: MCP direct fact and episode delivery

Closest supplied [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval) covers hybrid query/ranking; this route has distinct UUID/direct recent-group selectors rather than that hybrid search progression. It is not a new identity for the same query-search route. Owners: MCP `get_entity_edge`, `get_episodes`, `format_fact_result`. UUID lookup returns edge model serialization excluding fact_embedding, including other retained fields such as episodes and dates. Group-scoped episode reads merge/sort by creation time/limit and return content, source, source_description and identifiers. No effective group IDs return an empty list. Delivery changes available evidence to the caller without certifying truth; no model judgment or acceptance occurs. This is a countercase to generalizing notebook metadata loss to all shipped readers. The same fact formatter is also called by MCP fact search, as established by the direct call-site search. SRC-1 implementation: `mcp_server/src/graphiti_mcp_server.py`, `mcp_server/src/utils/formatting.py`.

- Immediate return: serialized edge, episode response, empty episode list or error wrapper.
- Later read-back: caller-requested delivery of retained graph/source material from previous writes.
- Delegated visibility: MCP host receives available text and metadata; embeddings omitted from fact response.
- Selection predicate: edge UUID/effective driver group, or episode group IDs plus created-time sort/limit.
- Invalidation or expiry: inapplicable — read route; saved content may already be deleted or blanked by other routes.
- Activation or effect: evidence delivery wired; host inspection/compliance and epistemic use unobserved.
- Evidence limits: no certification of provenance links, recovery of removed raw text or proof of host source checking.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = edge.model_dump(
>     mode='json',
>     exclude={
>         'fact_embedding',
>     },
> )
> --- `mcp_server/src/utils/formatting.py`

> 'content': episode.content,
> 'created_at': episode.created_at.isoformat() if episode.created_at else None,
> --- `mcp_server/src/graphiti_mcp_server.py`

### Claims

#### EPI-CLM-temporal-provenance
Label: Temporal truth and full source lineage

Claimed operation: validity windows and non-deleting historical invalidation permit querying what is true now or before; every entity/relationship has full lineage to raw episodes. SRC-1 doctrine/design: `README.md`. Closest supplied [RT-CLM-write-envelope](runtime.md#rt-clm-write-envelope) concerns transaction boundaries and [RT-CLM-schema-boundary](runtime.md#rt-clm-schema-boundary) concerns schemas, not these public truth/lineage claims; distinct claim referent. The routes support temporal metadata and episode associations in covered processing paths. They do not establish certified truth, guaranteed raw-source availability, source fidelity, or lineage delivered by every consumer. Direct writes and raw-content suppression are consequential countercases; facts-only notebook formatting is another. Temporal truth depends on input truth and model interpretation not independently checked here.

> - **Temporal Fact Management:** Facts have validity windows. When information changes, old facts are
>   invalidated — not deleted. Query what's true now, or what was true at any point in time.
> - **Episodes & Provenance:** Every entity and relationship traces back to the episodes (raw data) that produced it.
>   Full lineage from derived fact to source.
> --- `README.md`

#### EPI-CLM-cleanup-contract
Label: MCP deletion sole-support preservation

Claimed operation: MCP `delete_episode` says core cascading deletion removes solely supported facts and preserves facts supported by other episodes. SRC-1 doctrine/design: `mcp_server/src/graphiti_mcp_server.py`. Closest supplied [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes) says deletion changes graph state without prior-version restoration; it does not state this exact support-preservation guarantee, so this is a distinct claim. The inspected core edge selection is first-origin, not sole-support. This mismatch can be stated faithfully without superseding the valid runtime maintenance container.

> Uses Graphiti.remove_episode, which cascades the deletion: entities and facts
> that were created solely by this episode are removed along with it, while
> entities and facts also supported by other episodes are preserved.
> --- `mcp_server/src/graphiti_mcp_server.py`

### Evidenced absences

none declared in this member. Limits on warranted acceptance, provider internals and uninspected variants are scoped findings, not repository-complete absence records.

### Behavioral-authority paths

none declared in this member. Supplied [RT-BAP-facts-context](runtime.md#rt-bap-facts-context) and [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions) cover the two named assistant-context paths; other consequential consumers are assessed in the ledger and route records without duplicating those referents.
