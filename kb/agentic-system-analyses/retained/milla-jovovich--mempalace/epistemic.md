---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MemPalace epistemic routes: stored testimony, similarity-based admission, temporal fact replacement and bounded evaluation at the frozen revision."
run-id: AAS-2026-10-14-mempalace-ed71875aea5a-01
reviewed-boundary: "1392e1810c3ca67776bd7fe3e198788a96dbd6d1"
---

# MemPalace epistemic report

## Source-and-claim boundary

The question is what licenses reliance on retained conversation and project content, and what checks actually change its admission or later use. Scope and exclusions are those in [boundary](boundary.md#boundary-and-evidence); sources are declared in its [Source register](boundary.md#source-register). All added inspection uses SRC-1, implementation unless explicitly labelled doctrine/design. No target or evaluator was executed.

The supplied runtime is a provisional route account, not a coverage limit. Direct inspection of CLI and MCP fragment loading found additional material functions: checkpoint near-duplicate rejection, explicit drawer replacement/deletion, KG temporal withdrawal/replacement, and navigability audit with a failing exit threshold. These refine rather than supersede the runtime's valid containers. A claim that MemPalace merely appends or only returns text would miss these functions. A claim that it verifies stored propositions would confuse structural, similarity and temporal checks with evidence-consuming acceptance.

Public warrant claims include [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol) and [EPI-CLM-benchmark-recall](#epi-clm-benchmark-recall). The capability claim [RT-CLM-readonly-boundary](runtime.md#rt-clm-readonly-boundary) limits operational admission, not epistemic endorsement.

| Entry point or operation | Source path | Coverage and supporting records, or prevented conclusion |
|---|---|---|
| CLI dispatch | `mempalace/cli/__init__.py` | Direct read of fragment list; mining/setup/task routes supplied by runtime. Individual parser branches not fully inspected here. |
| Full/light MCP dispatch and registered handlers | `mempalace/mcp_server/__init__.py`, `mempalace/mcp_light_server.py` | Direct fragment list and result-enrichment read; supplied [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch). Registry includes KG and diary, not only drawer tools. Full schema catalog not independently read. |
| Turn, transcript and setup admission | `mempalace/integrations/hermes/__init__.py`, `mempalace/hooks_cli.py`, `mempalace/cli/cmd_init.py` | Supplied [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture), [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest), [RT-RTE-init-detection](runtime.md#rt-rte-init-detection); source excerpts supplied, not fresh full reads. |
| Drawer add/update/delete and structural checking | `mempalace/mcp_server/tools_write.py`, `mempalace/config.py` | Direct reads; [EPI-RTE-drawer-revision](#epi-rte-drawer-revision), with [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch). |
| Semantic duplicate check and checkpoint skip | `mempalace/mcp_server/tools_read.py`, `mempalace/mcp_server/tools_diary.py` | Direct reads; separate [EPI-RTE-duplicate-check](#epi-rte-duplicate-check) and [EPI-RTE-checkpoint-disposition](#epi-rte-checkpoint-disposition). Other diary implementation remains unassessed. |
| Query/prefetch/wake-up and recall instructions | `mempalace/searcher/query.py`, `mempalace/searcher/candidates.py`, `skills/mempalace-recall/SKILL.md` | Supplied [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall) and [RT-BAP-agent-context](runtime.md#rt-bap-agent-context); direct light-wrapper read adds [EPI-RTE-relevance-tags](#epi-rte-relevance-tags). No complete backend-specific recall assessment. |
| KG add/invalidate/supersede/query | `mempalace/mcp_server/tools_kg.py`, `mempalace/knowledge_graph.py` | Direct handler reads and add/invalidate implementation; supersede read through boundary validation, not its complete transaction or underlying query SQL. [EPI-RTE-kg-temporal](#epi-rte-kg-temporal). Atomic/as-of guarantee remains partly uninspected. |
| Audit and tunnel maintenance | `mempalace/cli/cmd_audit.py`, `mempalace/palace_audit.py`, `mempalace/cli/cmd_tunnels.py` | Direct audit consumer and score function reads; [EPI-RTE-palace-audit](#epi-rte-palace-audit). [EPI-RTE-tunnel-maintenance](#epi-rte-tunnel-maintenance) directly covers proposal review, `--yes` apply/prune and stale-wing exclusion; underlying proposal/prune algorithms not inspected, preventing validity or completeness conclusions for inferred associations. |
| Retrieval/model evaluation | `benchmarks/longmemeval_bench.py`, `benchmarks/model_eval/runner.py`, `README.md` | Direct selected metric/consumer reads; [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation), [EPI-CLM-benchmark-recall](#epi-clm-benchmark-recall). Model runner directly dispatches labelled calibration/classification/entity/memory scoring; its scorers and providers not inspected. No verified model-quality conclusion. |
| Coordination, patch delivery and backend capability admission | `mempalace/tasks.py`, `mempalace/logstream.py`, `mempalace/backends/registry.py` | Supplied [RT-RTE-task-launch](runtime.md#rt-rte-task-launch), [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery), [RT-RTE-backend-registration](runtime.md#rt-rte-backend-registration); no new truth-acceptance finding. |
| Other included material families | `mempalace/miner.py`, `mempalace/layers.py`, `crates/`, `mempalace/backends/`, `benchmarks/` | Project/document/source-adapter transformations, closet/AAAK generation, native/media/code routes, non-Chroma variants, replication, repair/backup, other evaluators and host shell variants remain partly or wholly unassessed here. Available evidence is not an access gap. Their omission prevents a system-complete negative about derivation, conjecture, acceptance or evaluator routes. |

Missing evidence is local to conclusions: no live corpus prevents assessment of the actual truth of retained claims; no host trace prevents demonstrated compliance or behavioral activation; no rerun/dataset inspection prevents reproduced recall or encoding-fidelity conclusions; no controlled intervention prevents attributing improvement to a component. Exact external model artifacts and provider internals are unavailable within this pin, preventing claims about their learning, knowledge or stable behavior. Distributed-parametric fixity is separately assessed in [RT-CMP-minilm](runtime.md#rt-cmp-minilm), [RT-CMP-embeddinggemma](runtime.md#rt-cmp-embeddinggemma), [RT-CMP-embeddinggemma2](runtime.md#rt-cmp-embeddinggemma2), [RT-CMP-openai-compat](runtime.md#rt-cmp-openai-compat) and [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider). Fixed inference weights do not imply absence of behavior change through retained text.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | User/assistant testimony or caller-authored propositions, where the text states propositions | Recallable drawer | SRC-1 `mempalace/mcp_server/tools_write.py` | Particular truth-apt claims not determinable without corpus; attribution is not verification. |
| [EPI-OBJ-kg-triple](#epi-obj-kg-triple) | Subject–predicate–object relationship over a caller-specified interval | Fact with optional provenance | SRC-1 `mempalace/knowledge_graph.py` | Default numerical confidence is not calibrated evidence; predicate interpretation and external truth unchecked. |
| [EPI-OBJ-search-tags](#epi-obj-search-tags) | Algorithm-relative relevance class and recency rank, not truth probability | Decorate recall result | SRC-1 `mempalace/mcp_light_server.py` | Distance and timestamps are the inputs; no endorsement or supersession follows. |
| [EPI-OBJ-audit-report](#epi-obj-audit-report) | Computed organization scores relative to fixed formulas | Navigability report | SRC-1 `mempalace/palace_audit.py` | Formula target differs from truth or actual answer quality. |
| [EPI-OBJ-retrieval-metrics](#epi-obj-retrieval-metrics) | Label-relative retrieval hit metrics | Benchmark evidence | SRC-1 `benchmarks/longmemeval_bench.py` | Label/source correctness, actual run and live-loop transfer not established. |
| [RT-OBJ-task-request](runtime.md#rt-obj-task-request) | Goal/done/delivery instructions; any embedded propositions depend on task body | Worker guidance | see [RT-OBJ-task-request](runtime.md#rt-obj-task-request) | Instruction force is not proposition acceptance. |
| [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact) | Diff is an executable proposal; accompanying rationale may be truth-apt | Delivered change proposal | see [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact) | Persistence does not establish correct code or installation. |

## Authority-route ledger

Rows separate checking, disposition and retention even when one handler connects them. Architectural status describes wiring, not observed activation. Repeated record-owned fields are supplied by the cited declaration; ledger-local judgments below state the epistemic license.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture), [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest) | content transformation | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | truth-apt transformation: acquisition/import | Host/source content enters palace | see cited records | see cited records | see cited records | Filing request | Source warrant unknown; host labels preserve attribution, not truth | May retain user and model text without per-item approval | see cited records | see cited records | [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol) | Lossless capture not guaranteed | No corpus/host trace |
| [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) | check/evidence production | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | no content change | Input structure, duplicate ID, post-write readability | Software validates size/type/null bytes, identity and storage IDs; not truth | see record; add handler before/after upsert | Error, existing ID, readable ID | Handler refuses malformed/unreadable writes | Only structural validity or detected storage visibility | Blocks add or reports success/error | Caller through MCP result, enforcing current request | SRC-1 `mempalace/config.py`, `mempalace/mcp_server/tools_write.py` | none | Storage success is not acceptance | Backend atomicity remains an external contract |
| [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) | retention | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | truth-apt transformation: non-ampliative reshaping | Validated drawer to bounded chunks | Deterministic slicing; see record for admission | see record | see record | Durable upsert | No added warrant; textual retention before acceptance | Later search/direct reads allowed | see [RT-BAP-agent-context](runtime.md#rt-bap-agent-context) | SRC-1 `mempalace/mcp_server/tools_write.py` | [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol) | none | Sanitization can alter invalid encoding; no universal fidelity claim |
| [EPI-RTE-duplicate-check](#epi-rte-duplicate-check) | check/evidence production | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | no content change | Similarity of candidate to up to five retrieved drawers | see record | see record | see record | Diagnostic on direct call | Similarity relative to model/metric; not equivalence or truth | Supplies checkpoint's skip predicate | see record | see record | none | Semantic sameness unestablished | Contradictory or materially changed wording can be close in embedding space |
| [EPI-RTE-checkpoint-disposition](#epi-rte-checkpoint-disposition) | disposition/acceptance | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | no content change | Whether item is filed | see record | see record | see record | Enforcing skip or add call | Admission/rejection only; no acceptance against truth evidence | Suppresses duplicate-marked candidates; dedup error does not veto filing | see record | see record | [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol) | Approximate match can suppress a correction | No preserved rejected-candidate text in returned duplicate entry |
| [EPI-RTE-drawer-revision](#epi-rte-drawer-revision) | lineage/freshness/recovery | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | truth-apt transformation: acquisition/import | Caller replacement or deletion of retained text | see record | see record | see record | Enforcing storage/cache changes | Caller-supplied revision, warrant unknown; deletion is not disproof | Replaces/removes content and purges source closets | see record | see record | none | none | No automatic evidence-based correction or guaranteed historical rollback established |
| [EPI-RTE-kg-temporal](#epi-rte-kg-temporal) | retention | implemented | [EPI-OBJ-kg-triple](#epi-obj-kg-triple) | truth-apt transformation: acquisition/import | Supplied relation into triples | see record | see record | see record | Persistent insertion | Structural/interval validity, not external fact truth | Admits optional-provenance assertions | see record | see record | none | `confidence=1.0` is not acceptance | Underlying predicate semantics remain caller-defined |
| [EPI-RTE-kg-temporal](#epi-rte-kg-temporal) | disposition/acceptance | implemented | [EPI-OBJ-kg-triple](#epi-obj-kg-triple) | truth-apt transformation: acquisition/import | Caller marks ended or supplies successor | see record | see record | see record | Enforcing metadata/state update | Withdrawal/replacement request, not checked criticism | Changes later temporal classification; preserves historical route | see record | see record | none | `active_facts` is not endorsement | Complete supersede transaction/query boundary not inspected |
| [EPI-RTE-relevance-tags](#epi-rte-relevance-tags) | content transformation | implemented | [EPI-OBJ-search-tags](#epi-obj-search-tags) | truth-apt transformation: entailed derivation | Distance/timestamp to algorithm-relative tags | see record | see record | see record | Advisory annotation | Formula-relative class/rank only; premises' accuracy unchecked | Hints returned without changing hit order | see record | see record | none | Relevance/freshness is not truth | No calibration evidence |
| [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall) | operational admission/selection/consumption | implemented | [EPI-OBJ-drawer-content](#epi-obj-drawer-content) | truth-apt transformation: non-ampliative reshaping | Retained text to selected context | see record | see record | see record | Ranking and context supply | Retained testimony; no added source warrant | May shape later answers if consumed | see [RT-BAP-agent-context](runtime.md#rt-bap-agent-context) | see record | [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol) | Full verbatim delivery not assured | Hydration/truncation prevents completeness inference |
| [EPI-RTE-palace-audit](#epi-rte-palace-audit) | check/evidence production | implemented | [EPI-OBJ-audit-report](#epi-obj-audit-report) | truth-apt transformation: entailed derivation | Organization under fixed score formula | see record | see record | see record | Report | Formula result, not proposition truth or measured navigability | Supplies optional threshold consumer | see record | see record | none | none | Analyzer correctness and real utility not measured |
| [EPI-RTE-palace-audit](#epi-rte-palace-audit) | operational admission/selection/consumption | implemented | [EPI-OBJ-audit-report](#epi-obj-audit-report) | no content change | Overall score versus requested threshold | see record | see record | see record | Exit status 2 below threshold | No claim accepted or rejected | Signals CLI failure; does not mutate palace | CLI exit, enforcing process result; external caller may gate work | see record | none | none | External CI/maintenance consumption unobserved |
| [EPI-RTE-tunnel-maintenance](#epi-rte-tunnel-maintenance) | disposition/acceptance | implemented | none — navigation proposal | non-truth-apt policy/content update: caller-approved graph navigation changes | Proposed tunnel plan or prune request to stored graph | Caller selects `--yes`; code rejects stale endpoints and delegates apply/prune | see record | see record | Enforcing graph maintenance | No truth acceptance; inferred associations remain unassessed | Adds/removes navigation links | CLI flag to graph writer, enforcing persistent navigation state | see record | none | Association strength is not warrant | Underlying algorithms and later graph use uninspected |
| [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation) | check/evidence production | implemented | [EPI-OBJ-retrieval-metrics](#epi-obj-retrieval-metrics) | truth-apt transformation: entailed derivation | Ranking versus labelled session IDs | see record | see record | see record | Reporting/persistence | Label-relative retrieval success only | Produces report, no demonstrated live-memory acceptance or policy update | see record | see record | [EPI-CLM-benchmark-recall](#epi-clm-benchmark-recall) | Retrieval is not QA accuracy | Dataset, execution and causal contrast missing |

The derivations above are domain-local: an audit formula or benchmark set-membership formula derives a computed property from supplied counts/labels. Neither derives a warranted proposition about the user's world. No assessed row establishes lifecycle integration after evidence-consuming acceptance. This is a bounded finding about these rows, not a searched system-wide absence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol) | see record | see record | see record | [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall), [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture), [EPI-RTE-checkpoint-disposition](#epi-rte-checkpoint-disposition) | None supplied | Capture drop, near-duplicate rejection and selected/truncated returns are counterexamples to guaranteed complete verbatim recall | Shipped request to search/quote, supported by retained-content delivery mechanisms | Host compliance and answer truth unknown; skill policy not enforceable truth gate |
| [EPI-CLM-benchmark-recall](#epi-clm-benchmark-recall) | see record | see record | see record | [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation) | No executed/reviewed result trace here | Fixed labels define relevance, not truth; reranked/full-set figure and held-out figure have different conditions | Implements bounded retrieval metric; source reports results and explicitly separates QA accuracy | Numbers unreproduced; component attribution and live-loop transfer unsupported |
| [RT-CLM-readonly-boundary](runtime.md#rt-clm-readonly-boundary) | see record | see record | see record | [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) | None supplied | Name-based request gate excludes direct writes and recovery exceptions | Protocol-level operational refusal, not endorsement or universal immutable storage | See record for stronger-claim counterexamples |

## Bounded conclusion

MemPalace can import caller and host testimony, retain it before any truth acceptance, and deliver selected passages to later agents. Source/session/time metadata preserves some attribution, while the evidence warrant of source propositions remains unknown. Caller-authored assistant text is retained alongside user text; storage does not upgrade either into established knowledge. See [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture), [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) and [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall).

The material admission criteria differ. Drawer writes have structural, ID and visibility checks. Checkpoints additionally reject near matches at a configurable similarity threshold, with a fail-open path for dedup errors. These criteria target encoding/storage or approximate redundancy, not factual accuracy. A rejected near match can contain a correction, so suppression is consequential without constituting checked semantic equivalence. Explicit replacement/deletion supplies a separate correction capability; cleanup of closets prevents continued selection from stale source summaries, but does not verify the replacement. See [EPI-RTE-duplicate-check](#epi-rte-duplicate-check), [EPI-RTE-checkpoint-disposition](#epi-rte-checkpoint-disposition) and [EPI-RTE-drawer-revision](#epi-rte-drawer-revision).

KG assertions differ from ordinary text: code validates interval structure, persists triples and allows caller-requested temporal withdrawal/successor installation. The query wrapper separates active, historical and future results. This gives temporal state operational authority at a later reader, not truth endorsement; optional provenance and default confidence do not establish acceptance. See [EPI-RTE-kg-temporal](#epi-rte-kg-temporal).

Navigation maintenance separately retains a reviewable proposal and uses an operator flag to apply or prune graph links; stale-wing checks constrain operational admission, not the truth of inferred associations. See [EPI-RTE-tunnel-maintenance](#epi-rte-tunnel-maintenance).

Algorithm-relative relevance tags, organization scores and label-relative retrieval metrics are inspectable derivations in narrow formal domains. Their premises are not independently warranted here. Audit has a consequential threshold-to-exit consumer; checkpoint has a check-to-skip consumer; retrieval evaluation produces reports rather than a demonstrated change to live memory or answer policy. These distinct consumers prevent treating all evaluators as one oracle. See [EPI-RTE-relevance-tags](#epi-rte-relevance-tags), [EPI-RTE-palace-audit](#epi-rte-palace-audit) and [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation).

Setup classifications can be model/heuristic candidates admitted automatically or edited by people, as in [RT-RTE-init-detection](runtime.md#rt-rte-init-detection). Whether particular outputs preserve inputs, derive facts or conjecture beyond them is not determinable from the supplied route account alone. No assessed route supplies an evidence-consuming decision that accepts an ampliative proposition for a named truth use and scope, then integrates it on that basis. Unassessed extraction, maintenance and evaluator families preclude promoting that local finding into a complete-system absence.

Retained text can change later behavioral context without changing embedding weights. Delivery and policy requests are implemented; exercised reliance, improved capacity, content-directed iterative criticism and exercised self-improvement are independently unestablished in this evidence. Task launch and patch delivery add operational capability and proposal persistence, not product installation or truth warrant. The report assigns no single system-wide epistemic score.

## Shared records

### Operative objects

#### EPI-OBJ-drawer-content
Label: Drawer content

Source-native identity: drawer `documents` text, including physical chunks linked by `parent_drawer_id`. Representational form: natural language interpreted by agents/humans. Storage substrate: backend collection documents. Distinct from [RT-OBJ-task-request](runtime.md#rt-obj-task-request) and [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact): these are conversation/project memory, not coordination events or diffs. Closest supplied route is [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch), whose effects include this object; the route itself is not an object counterpart. SRC-1 `mempalace/mcp_server/tools_write.py`. Load-bearing storage/chunk evidence follows in [EPI-RTE-drawer-revision](#epi-rte-drawer-revision) and the supplied dispatch record.

#### EPI-OBJ-kg-triple
Label: Knowledge graph triple

Source-native identity: `triples` relationship with interval, confidence and optional provenance fields. Representational form: symbolic fields with fixed temporal/database consumers; world-relation interpretation depends on caller-defined predicates and readers. Storage substrate: SQLite. Distinct from supplied drawer capture/search routes and coordination objects: temporal relationship rows have separate update and query consumers. SRC-1 `mempalace/knowledge_graph.py`.

> confidence: float = 1.0,
> source_closet: str = None,
> source_file: str = None,
> source_drawer_id: str = None,
> adapter_name: str = None,
> --- `mempalace/knowledge_graph.py:250-269`

#### EPI-OBJ-search-tags
Label: Search result annotations

Source-native identity: `relevance_confidence`, `recency_rank`, `is_latest_record`. Representational form: symbolic classifications rendered in a tool response for human/model interpretation. Storage substrate: current response dictionary, not durable acquired memory. Distinct from stored drawers; these are transient derived annotations on [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall) output. SRC-1 `mempalace/mcp_light_server.py`; passage in [EPI-RTE-relevance-tags](#epi-rte-relevance-tags).

#### EPI-OBJ-audit-report
Label: Palace audit report

Source-native identity: audit report's per-layer/overall scores and findings. Representational form: symbolic numeric results plus natural-language diagnostics. Storage substrate: transient dictionary rendered to terminal/JSON; external retention is not established. No supplied object counterpart after comparison with runtime task/patch objects; navigability evaluation is separate. SRC-1 `mempalace/palace_audit.py`; formula and consumer passages in [EPI-RTE-palace-audit](#epi-rte-palace-audit).

#### EPI-OBJ-retrieval-metrics
Label: Retrieval metrics

Source-native identity: session/turn `recall_any`, `recall_all` and NDCG results. Representational form: symbolic floats keyed by rank cutoff; storage substrate: in-memory result log and optional JSONL report. No supplied object counterpart; unlike [RT-OBJ-task-request](runtime.md#rt-obj-task-request), these are benchmark results, not instructions. SRC-1 `benchmarks/longmemeval_bench.py`; passages in [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation).

### Routes

#### EPI-RTE-duplicate-check
Label: Semantic duplicate check
Part of: [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch)

This is the check operation within MCP dispatch, not its content-retention or disposition part. Endpoints: candidate content → vector query for five hits → metric-specific distance conversion → threshold matches and boolean. Owner: read handler and backend embedder; context/state: current candidate and indexed drawers. Effects: produces a redundancy diagnostic, consumed separately by checkpoint. SRC-1 `mempalace/mcp_server/tools_read.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `is_duplicate` and matches, or vector-disabled/error diagnostic.
- Later read-back: inapplicable — the diagnostic is not persisted as knowledge by this handler; the check reads retained drawers.
- Delegated visibility: inapplicable — this operation launches no worker; external embedding-provider behavior is uninspected.
- Selection predicate: nearest five queried hits whose rounded metric-derived similarity meets caller threshold, default 0.9.
- Invalidation or expiry: current-call result; changes to corpus/model/threshold can change later checks.
- Activation or effect: diagnostic production wired; checkpoint skip consumer inspected separately, actual execution unobserved.
- Evidence limits: top-five and embedding closeness do not establish exhaustive duplicates or semantic equivalence; provider/backend versions differ.

Code proposes the match classification; caller supplies candidate/threshold; software decides it, with no human veto inside the check. Open request mode, no reference-answer oracle. Fixed similarity rules guide the result. On unusable vectors the handler exposes a limitation instead of asserting a trustworthy negative.

> similarity = round(_distance_to_similarity(dist, metric), 3)
> if similarity >= threshold:
> --- `mempalace/mcp_server/tools_read.py`

> return {
>     "is_duplicate": len(duplicates) > 0,
>     "matches": duplicates,
> }
> --- `mempalace/mcp_server/tools_read.py`

#### EPI-RTE-checkpoint-disposition
Label: Checkpoint duplicate disposition
Part of: [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch)

Endpoints: checkpoint item → duplicate diagnostic → skip or `tool_add_drawer` → aggregate result; optional diary follows. Owner: checkpoint software; context/state: submitted items and shared palace. This differs from [EPI-RTE-duplicate-check](#epi-rte-duplicate-check), which supplies evidence but does not itself reject filing. SRC-1 `mempalace/mcp_server/tools_diary.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: lists of added, duplicates, errors and optional diary result.
- Later read-back: successfully added items can reach drawer search; skipped item content is not filed by this route.
- Delegated visibility: inapplicable — batch saving launches no isolated agent.
- Selection predicate: valid item fields; positive `is_duplicate` skips; otherwise invokes drawer add, including on dedup error.
- Invalidation or expiry: checkpoint result is transient; resulting drawers persist until other maintenance.
- Activation or effect: enforcing skip/add branch wired, no supplied checkpoint execution.
- Evidence limits: skip establishes storage rejection only, not falsity or equivalence; each item can fail separately, not one all-or-none batch.

Client proposes content, software decides storage admission, human contribution is unresolved from client identity. No per-item confirmation or answer oracle. Open save mode; configurable threshold and verbatim-retention priority shape disposition. Rejected near matches are not a rollback mechanism; client can choose another write path. No truth acceptance or criticism-based successor selection is established.

> dup = tool_check_duplicate(content, threshold=dedup_threshold)
> if dup.get("is_duplicate"):
>     out["duplicates"].append({"room": room, "matches": dup.get("matches", [])})
>     continue
> --- `mempalace/mcp_server/tools_diary.py`

> # On a dedup error (genuine index failure — content is guaranteed a
> # string by the guard above) we still file rather than drop the
> # memory: verbatim recall is the priority and add_drawer's own
> # idempotency blocks exact duplicates.
> res = tool_add_drawer(wing=wing, room=room, content=content, added_by=resolved_added_by)
> --- `mempalace/mcp_server/tools_diary.py`

#### EPI-RTE-drawer-revision
Label: Drawer replacement and withdrawal
Part of: [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch)

Endpoints: explicit update/delete request → logical drawer resolution/validation → backend update/upsert/delete → cache invalidation and source-closet purge → result. Owner: write handler; state: old document/chunks/metadata and caller replacement. These are maintenance parts of supplied dispatch, not automatic truth criticism. SRC-1 `mempalace/mcp_server/tools_write.py`, `mempalace/config.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success with drawer/chunk/closet information, not-found/validation error, or backend failure.
- Later read-back: revised content/metadata can reach search/direct reads; removed rows no longer supply those reads if backend mutation succeeds.
- Delegated visibility: inapplicable — maintenance launches no worker.
- Selection predicate: caller-specified drawer ID; logical handle resolves group while a physical chunk delete selects one row; new content/names validated.
- Invalidation or expiry: update sets `last_modified`; stale chunks removed after replacement upsert; content changes/deletes purge source closets and invalidate overview caches.
- Activation or effect: storage and later-selection changes wired; no observed mutation or answer dependence.
- Evidence limits: backend failure/atomicity not independently checked; WAL intent/result is not a demonstrated undo history or evidence-consuming correctness decision.

Caller proposes replacement/removal, software can veto malformed input/not-found/backend errors. Human authorship/approval is not guaranteed by an MCP client. Open maintenance request, no answer oracle. Fixed validation/chunking/cleanup guidance governs it; explicit later writes can replace content, but automatic truth rollback is not established.

Concrete deterministic trace, deduced without execution: with configured `chunk_size=4`, input `Alice left.` passes the shown nonempty/length/null checks and contains no lone surrogate. Add slices it into `Alic`, `e le`, `ft.` with ordered chunk linkage. Concatenating in that order preserves the input proposition; none of the three chunks individually is guaranteed to state it. This supports non-ampliative reshaping, not a new fact. Invalid Unicode sanitization remains a separate fidelity limit.

> if not isinstance(value, str) or not value.strip():
>     raise ValueError("content must be a non-empty string")
> if len(value) > max_length:
>     raise ValueError(f"content exceeds maximum length of {max_length} characters")
> if "\x00" in value:
>     raise ValueError("content contains null bytes")
> return strip_lone_surrogates(value)
> --- `mempalace/config.py`

> for i in range(0, len(content), chunk_size):
>     chunk_idx = i // chunk_size
>     chunk_ids.append(f"{drawer_id}_chunk_{chunk_idx:06d}")
>     chunk_docs.append(content[i : i + chunk_size])
> --- `mempalace/mcp_server/tools_write.py`

> if content is not None and source_file:
>     closets_deleted = _purge_source_closets(source_file, commit=True)
> --- `mempalace/mcp_server/tools_write.py`

> col.delete(ids=record["ids"])
> _invalidate_overview_caches()
>
> source_file = record["metadata"].get("source_file")
> closets_deleted = _purge_source_closets(source_file, commit=True) if source_file else 0
> --- `mempalace/mcp_server/tools_write.py`

#### EPI-RTE-kg-temporal
Label: Knowledge graph temporal maintenance
Part of: [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch)

Endpoints: caller relation/interval → input and temporal validation → SQLite triple insert or interval end/successor request → later KG query wrapper's active/historical/future grouping. Owner: KG handler and graph code; state: entities, triples and optional provenance. Material part distinct from drawer replacement: stored intervals change temporal query eligibility without deleting historical relationships. SRC-1 `mempalace/mcp_server/tools_kg.py`, `mempalace/knowledge_graph.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: triple ID/fact, resolved ended value, superseded value or input/domain error.
- Later read-back: KG query returns stored relationships and temporal categories; timeline is an exposed alternate not traced here.
- Delegated visibility: inapplicable — graph maintenance launches no separate agent.
- Selection predicate: supplied subject/predicate/object; invalidate targets open matching rows; interval checks reject ends preceding starts; supersede supplies old/new object and boundary.
- Invalidation or expiry: invalidate stores end time; supersede requests shared boundary, default current UTC; add does not automatically resolve conflicting alternative objects.
- Activation or effect: add/invalidate database writes and wrapper temporal categorization inspected; supersede handler and boundary preparation wired, complete atomic transaction/as-of guarantee uninspected.
- Evidence limits: callers decide external truth; provenance optional; complete supersede transaction and query SQL not read; no live KG trace.

Caller proposes assertion, ending or successor; software checks structural/interval validity, not evidence for the relationship. No human review required by handlers, no answer oracle; open requests. Fixed temporal schema guides the change. Historical categories preserve some withdrawn state; this is not an established truth-directed criticism loop or automatic rollback. An inverted interval is rejected because it would hide the row from queries, not because its world proposition has been falsified.

> if (
>     valid_from is not None
>     and valid_to is not None
>     and _temporal_end_key(valid_to) < _temporal_start_key(valid_from)
> ):
>     raise ValueError(
>         f"valid_to={valid_to!r} is before valid_from={valid_from!r}; "
>         "an inverted interval would be invisible to every KG query"
>     )
> --- `mempalace/knowledge_graph.py`

> conn.execute(
>     "UPDATE triples SET valid_to=? "
>     "WHERE subject=? AND predicate=? AND object=? AND valid_to IS NULL",
>     (ended, sub_id, pred, obj_id),
> )
> --- `mempalace/knowledge_graph.py`

> "active_facts": active,
> "historical_facts": historical,
> "future_facts": future,
> "facts": results,
> --- `mempalace/mcp_server/tools_kg.py`

#### EPI-RTE-relevance-tags
Label: Light search relevance annotations
Part of: [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall)

Endpoints: search result → minimum available distance and timestamp order → relevance/recency annotations → light response. Owner: deterministic light wrapper; current response state changes, hit ordering retained. SRC-1 `mempalace/mcp_light_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: enriched response or no-matches status; original search ranking remains.
- Later read-back: inapplicable — wrapper does not persist annotations; response carries previously retained hit text.
- Delegated visibility: inapplicable — no agent is launched by enrichment.
- Selection predicate: existing results; minimum nonmissing distance; descending available filing/creation timestamp for recency.
- Invalidation or expiry: invocation-local; later query or timestamps can yield other annotations.
- Activation or effect: annotations wired into returned envelope; downstream use and improved decisions unobserved.
- Evidence limits: fixed thresholds not calibrated truth or retrieval-success probability; missing/incorrect timestamps defeat stronger freshness conclusions.

Concrete deduction: if the only available distance is 0.34, minimum distance is below 0.35 and the output class is `high`; 0.60 gives `low`. This derives a formula-relative tag, not an entailed world proposition. Software computes it; no candidate acceptance or answer oracle occurs. Annotation channel is advisory to response consumers for the current invocation.

> distances = [d for d in (_search_distance(item) for item in results_list) if d is not None]
> if distances:
>     min_dist = min(distances)
>     if min_dist > 0.52:
>         res["relevance_confidence"] = "low"
>     elif min_dist < 0.35:
>         res["relevance_confidence"] = "high"
>     else:
>         res["relevance_confidence"] = "moderate"
> --- `mempalace/mcp_light_server.py`

#### EPI-RTE-palace-audit
Label: Palace navigability audit

No counterpart in the supplied runtime after comparison: unlike dispatch gates and setup detection, this route evaluates stored organization and can change CLI exit status. Endpoints: palace counts/organization analysis → score formula/report → JSON/terminal output → optional `fail_under` comparator. Owner: audit code and CLI; context/state: current organization snapshot. SRC-1 `mempalace/palace_audit.py`, `mempalace/cli/cmd_audit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: report printed, or exit 2 when nonmissing overall score falls below supplied threshold.
- Later read-back: inapplicable — inspected CLI does not retain report; an external caller may store JSON but that path is uninspected.
- Delegated visibility: inapplicable — audit launches no agent.
- Selection predicate: selected palace; layer availability determines which scores enter mean; threshold only applies when supplied and overall is not None.
- Invalidation or expiry: current snapshot report, no palace mutation by this command.
- Activation or effect: threshold changes process outcome; automated maintenance or downstream gating is unobserved.
- Evidence limits: analyzer internals only selectively inspected; scores encode navigational heuristics, not observed usability or factual truth.

Software evaluates generic-room share, name drift and relationship artifacts/coverage; caller selects failure threshold and can veto subsequent work externally. No expected-answer oracle. Open audit mode; fixed formula is the governing guidance, not a learned revision theory. The CLI returns a signal, not a factual-content rejection or automatic repair.

> scores["rooms"] = _clamp(100 * (1 - rooms["generic_share"])) if rooms["total_drawers"] else None
> --- `mempalace/palace_audit.py`

> present = [s for s in scores.values() if s is not None]
> scores["overall"] = _clamp(sum(present) / len(present)) if present else None
> return scores
> --- `mempalace/palace_audit.py`

> threshold = getattr(args, "fail_under", None)
> overall = report["scores"]["overall"]
> if threshold is not None and overall is not None and overall < threshold:
>     sys.exit(2)
> --- `mempalace/cli/cmd_audit.py`

#### EPI-RTE-tunnel-maintenance
Label: Tunnel proposal admission and cleanup

No supplied counterpart after comparison: this is navigation-graph maintenance rather than task patch delivery or drawer capture. Endpoints: current wings/hallways → proposal or prune report → optional user-edited plan → `--yes` apply/prune branch → saved tunnels. Owner: CLI orchestration and imported tunnel functions; context/state: persistent proposal plan and navigation graph. Only the orchestration was directly inspected. SRC-1 `mempalace/cli/cmd_tunnels.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: dry-run/proposal report, created/removed count, or stale/invalid-plan error.
- Later read-back: proposal file is reloaded by a later apply invocation; saved tunnels belong to graph navigation, whose downstream internals remain uninspected here.
- Delegated visibility: inapplicable — this CLI route launches no agent.
- Selection predicate: action propose/prune; `--yes` selects graph modification; apply drops plan rows whose normalized wings no longer exist and refuses if none remain.
- Invalidation or expiry: proposal can be manually edited; stale endpoints filtered on application; prune can remove reported artifacts under the graph writer lock.
- Activation or effect: application and cleanup calls wired; graph-write algorithms, actual changes and later traversal effects unobserved.
- Evidence limits: underlying strength, artifact and application algorithms not inspected; no warrant about real-world associations or measured navigation improvement.

Code proposes a plan; operator can delete unwanted rows and chooses apply. This is human-editable operational admission, not evidence-consuming acceptance of the association's truth. `--yes` on prune executes the delegated cleanup without a separate dialogue. Open maintenance mode, no answer oracle. Fixed proposal/endpoint rules guide it. No demonstrated rollback or automatic policy-improvement loop follows. Semantic relation of underlying inferred associations is not determinable; the inspected boundary establishes only persistent navigation-state update.

> print(f"\n  Plan saved to {path}. Delete rows you do not want, then re-run with --yes.")
> --- `mempalace/cli/cmd_tunnels.py`

> if not fresh:
>     print(f"  Every proposed tunnel names a wing that no longer exists ({stale} rows).")
>     print("  Re-run `mempalace tunnels propose` against the current wings.")
>     sys.exit(1)
> created = apply_proposal({**plan, "tunnels": fresh}, config=config)
> --- `mempalace/cli/cmd_tunnels.py`

> with mine_lock(_get_tunnel_file(config)):
>     kept, report = prune_tunnels(_load_tunnels(config), wings)
>     if report["removed"]:
>         _save_tunnels(kept, config)
> --- `mempalace/cli/cmd_tunnels.py`

#### EPI-RTE-retrieval-evaluation
Label: Labelled retrieval evaluation

No counterpart in supplied runtime records: evaluator existence was mentioned, but no evaluator route was declared. Endpoints: benchmark ranking and labelled answer session IDs → session/turn membership metrics → aggregate/per-type reporting and optional JSONL result log. Owner: benchmark harness; context/state: benchmark corpus/rankings/reference IDs. SRC-1 `benchmarks/longmemeval_bench.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rank-cutoff metrics and printed summary; optional result file.
- Later read-back: optional persisted report is available to later file readers; no inspected automatic live-policy consumer or demonstrated later reliance.
- Delegated visibility: inapplicable — inspected metric calculation delegates no agent; other retrieval/reranking modes have uninspected provider behavior.
- Selection predicate: top-k ranking IDs versus reference IDs; session-level corpus IDs collapse to session identities; turn reference set includes all corpus IDs from answer sessions.
- Invalidation or expiry: results belong to dataset/mode/configuration; no automatic expiration or product rollback in the inspected save path.
- Activation or effect: report production/persistence wired; route not executed, no observed product change.
- Evidence limits: expected-session membership is not end-to-end answer correctness; turn labels inherit session attribution, not independently annotated minimal evidence; dataset and retained result files not inspected.

Harness supplies the ranking; dataset supplies the reference-outcome oracle (`answer_sids`); code computes metrics. This is bounded benchmark evaluation, not open live-answer acceptance. Human reference construction is uninspected. Report saving does not itself select a production successor, reject memories or establish an evidence-responsive improvement loop. Concrete deduction: rankings `[0]`, corpus IDs `[s1]`, correct IDs `{s1}`, k=1 gives both recalls 1; replacing correct IDs with `{s2}` gives both 0. The checked domain is labelled retrieval membership only.

> top_k_ids = set(corpus_ids[idx] for idx in rankings[:k])
> recall_any = float(any(cid in top_k_ids for cid in correct_ids))
> recall_all = float(all(cid in top_k_ids for cid in correct_ids))
> ndcg_score = ndcg(rankings, correct_ids, corpus_ids, k)
> return recall_any, recall_all, ndcg_score
> --- `benchmarks/longmemeval_bench.py`

> session_level_ids = [session_id_from_corpus_id(cid) for cid in corpus_ids]
> session_correct = answer_sids
> --- `benchmarks/longmemeval_bench.py`

> if out_file:
>     with open(out_file, "w") as f:
>         for entry in results_log:
>             f.write(json.dumps(entry) + "\n")
>     print(f"  Results saved to: {out_file}")
> --- `benchmarks/longmemeval_bench.py`

### Claims

#### EPI-CLM-benchmark-recall
Label: Reported benchmark recall

Claimed operation: README reports raw LongMemEval R@5 96.6%, hybrid held-out 98.4%, and rerank full-set ≥99%, while warning against equating retrieval recall with QA accuracy and against test-specific tuning. Source: SRC-1 `README.md`, doctrine/design and attributed reported results, not an inspected run trace. Distinct from [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol): numeric evaluator claims are not the agent's recall policy. The registered source layer and this inspection support attribution and evaluator implementation, not independent result authentication. [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation) supplies the bounded metric interpretation.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> | Raw (semantic search, no heuristics, no LLM) | **96.6%** | None |
> | Hybrid v4, held-out 450q (tuned on 50 dev, not seen during training) | **98.4%** | None |
> | Hybrid v4 + LLM rerank (full 500) | ≥99% | Any capable model |
> --- `README.md`

> metrics on different splits, and placing retrieval recall next to
> end-to-end QA accuracy is not an honest comparison. See each project's
> own research page for their published numbers.
> --- `README.md`
