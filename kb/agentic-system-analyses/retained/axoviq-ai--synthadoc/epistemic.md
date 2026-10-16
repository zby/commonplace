---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Synthadoc epistemic routes: compilation, citation checks, lifecycle authority, withdrawal and later consumption at the frozen source boundary."
run-id: AAS-2026-10-15-synthadoc-a3cae9152fff-01
reviewed-boundary: b80d9388a3013e8051baf2854c7250942c46e91a
---

# Synthadoc epistemic report

## Source-and-claim boundary

The question is how source documents become claims that Synthadoc later permits models and users to rely on, and what its checks actually license. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design only. No target execution was performed.

The runtime is a provisional route map, not an inspection limit. Direct inspection adds citation annotation, structural citation checking, adversarial checks and their disposition consumer, automatic lifecycle admission, link cleanup, semantic citation faithfulness and its cache/CLI/editor consumers, sensitive-data withdrawal, cross-wiki synthesis and the AquaFlow evaluator. These extend SRC-1 inspection, not its identity. Public warrant claims are [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization), [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) and [EPI-CLM-active-review](#epi-clm-active-review).

| Entry point or operation | Source path, SRC-1 | Coverage record or limit | Reading basis |
|---|---|---|---|
| CLI dispatch | `synthadoc/cli/main.py` | registrations checked against routes below; cross-wiki and retract are additional material entries | direct |
| Ingest and annotation | `synthadoc/agents/ingest_agent.py` | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | runtime plus direct prompt/annotation reads |
| Query, packs, export and bundle consumer | `synthadoc/agents/query_agent.py`; `synthadoc/agents/context_agent.py`; `synthadoc/core/export.py`; `tests/integration/okf_consumer_agent.py` | [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); [RT-RTE-context-export](runtime.md#rt-rte-context-export) | supplied runtime, not independent reread |
| Lint, lifecycle, cleanup, automatic resolution | `synthadoc/agents/lint_agent.py` | [EPI-RTE-structural-citations](#epi-rte-structural-citations); [EPI-RTE-adversarial-review](#epi-rte-adversarial-review); [EPI-RTE-warning-gate](#epi-rte-warning-gate); [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission); [EPI-RTE-link-cleanup](#epi-rte-link-cleanup); [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | direct, including callers/results |
| Faithfulness job, cache, CLI and editor | `synthadoc/agents/citation_faithfulness_agent.py`; `synthadoc/agents/faithfulness_cache.py`; `synthadoc/core/orchestrator.py`; `synthadoc/cli/audit.py`; `obsidian-plugin/src/main.ts` | [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | direct |
| MCP writes, reads and lifecycle tools | `synthadoc/integration/mcp_server.py` | [RT-RTE-client-write](runtime.md#rt-rte-client-write); [RT-RTE-context-export](runtime.md#rt-rte-context-export); registered-tool search | runtime plus direct registry search; full MCP lifecycle branch not independently traced |
| Candidate promotion/discard, explicit HTTP lifecycle | `synthadoc/integration/http_server.py` | [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission); explicit transition handler remains unassessed here | supplied runtime plus endpoint search; prevents complete lifecycle acceptance/recovery verdict |
| Maintenance tool loop and confirmation | `synthadoc/agents/workflows/_loop.py`; `synthadoc/agents/workflows/_base.py` | [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop); [RT-CLM-confirm-scope](runtime.md#rt-clm-confirm-scope) | supplied runtime; individual contradiction/citation/content-health successor criteria not exhaustively assessed |
| Sensitive-data masking | `synthadoc/core/retract.py`; `synthadoc/integration/http_server.py`; `synthadoc/cli/retract.py` | [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | direct scanner/post-ingest read; CLI dispatch/write search; periodic-loop details not fully traced |
| Cross-wiki querying | `synthadoc/agents/cross_wiki_query_agent.py` | [EPI-RTE-cross-wiki](#epi-rte-cross-wiki) | direct complete agent read; peer deployments unobserved |
| Providers, extensions, hooks, schedule | `synthadoc/providers/coding_tool.py`; `synthadoc/agents/skill_agent.py`; `synthadoc/core/hooks.py`; `synthadoc/core/scheduler.py` | [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation); [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading); [RT-RTE-scheduled-operation](runtime.md#rt-rte-scheduled-operation) | supplied runtime plus direct complete hook executor read; configured external code and provider state uninspected |
| HTTP exposed-operation inventory and rollback | `synthadoc/integration/http_server.py` | [EPI-RTE-snapshot-rollback](#epi-rte-snapshot-rollback); decorators checked against runtime routes | direct endpoint inventory and rollback read; `/analyse`, routing validation/cleanup, sessions and history purge not fully traced; prevents complete claims about all transformations, lineage or recovery |
| AquaFlow evaluation | `docs/example/aquaflow/evaluation/scripts/eval_queries.py` | [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | direct question-bank, scorer and runner reads; retained benchmark result files not adopted |
| Generated instructions, scaffold, backup/restore, templates, remaining live tests | `synthadoc/cli/_init.py`; `synthadoc/cli/scaffold.py`; `synthadoc/core/backup.py`; `tests/live/` | included system surfaces, not fully assessed epistemically here | boundary/runtime only where supplied; prevents system-complete negative about trace-fed guidance revision, all recovery or all evaluators |

Missing production corpus and provenance-linked traces prevent attributing a candidate to an exercised production/check/acceptance route. No supplied comparison establishes factual benefit, component effects or transfer. Accessible but uninspected paths above are not access failures or evidenced absences. External provider weights and host policies are not inspectable here. These limits do not erase implemented checks or their actual code-level force.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | see record | see record | SRC-1, `synthadoc/agents/ingest_agent.py` | No production instance or demonstrated support |
| [EPI-OBJ-extracted-text](#epi-obj-extracted-text) | see record | see record | SRC-1, `synthadoc/agents/citation_faithfulness_agent.py` | Text extraction fidelity and underlying source truth unknown |
| [EPI-OBJ-lifecycle-state](#epi-obj-lifecycle-state) | none as a permission field; see record | see record | SRC-1, `synthadoc/agents/lint_agent.py` | Operational state is not factual acceptance |
| [EPI-OBJ-query-result](#epi-obj-query-result), answer | see record | see record | SRC-1, `synthadoc/agents/cross_wiki_query_agent.py` | Natural-language answer, no actual supported output supplied |
| [EPI-OBJ-query-result](#epi-obj-query-result), citation identifiers | reference assertions, see record | see record | SRC-1, `synthadoc/agents/cross_wiki_query_agent.py` | Code-selected symbolic IDs, not verified semantic support |
| [EPI-OBJ-query-facts](#epi-obj-query-facts), curated bank | see record | see record | SRC-1, `docs/example/aquaflow/evaluation/scripts/eval_queries.py` | Curated strings are not a complete semantic oracle |
| [EPI-OBJ-query-facts](#epi-obj-query-facts), score report | see record | see record | SRC-1, `docs/example/aquaflow/evaluation/scripts/eval_queries.py` | Symbolic coverage report, no adopted observed result |
| [EPI-OBJ-citation-markers](#epi-obj-citation-markers) | see record | see record | SRC-1, `synthadoc/agents/citation_faithfulness_agent.py` | Marker presence differs from warrant |
| [EPI-OBJ-lint-warnings](#epi-obj-lint-warnings), criticism text | see record | see record | SRC-1, `synthadoc/agents/lint_agent.py` | Natural-language challenged claim/concern, not verified refutation |
| [EPI-OBJ-lint-warnings](#epi-obj-lint-warnings), list/count | none as gate input; see record | see record | SRC-1, `synthadoc/agents/lint_agent.py` | Symbolic gate input can include a skipped-check sentinel |
| [EPI-OBJ-faithfulness-cache](#epi-obj-faithfulness-cache) | see record | see record | SRC-1, `synthadoc/agents/faithfulness_cache.py` | Freshness key does not bind exact body/source content |
| [RT-OBJ-workflow-guidance](runtime.md#rt-obj-workflow-guidance) | policy, see record | see record | SRC-1, `synthadoc/agents/workflows/content_health_resolver.py` | Guidance is not an implemented factual criterion |
| [RT-OBJ-workflow-protocol](runtime.md#rt-obj-workflow-protocol) | none, see record | see record | SRC-1, `synthadoc/agents/workflows/_loop.py` | Approval protocol is not evidence of human review quality |
| [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model) | distributed-parametric content not individually determinable | see record | SRC-1, `synthadoc/providers/anthropic.py` | Provider internals and exact numerical version uninspected |
| [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding) | no individuated proposition established | see record | SRC-1, `synthadoc/storage/search.py` | Dense ranking representation does not establish source truth |

## Authority-route ledger

Each row separates a consequential function; shared records retain endpoints, context and evidence. `see` delegates those owned fields, not this report's architectural or content-relation assessment. Implemented means executable wiring, never observed operation. No new epistemic acceptance is inferred from a live page, a clean warning list, a move, an approval boolean or a citation label.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-extracted-text](#epi-obj-extracted-text) | truth-apt transformation: acquisition/import | Extracted external source | Source selection and extraction; source warrant unknown | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | Delivery | Acquired content, not independently endorsed | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | Ingest model; clipped source; advisory; current compilation | SRC-1, `synthadoc/agents/ingest_agent.py` | none | none | Extraction may already use a model; complete source not guaranteed |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Compiled page/update | Model decision from source and snippets | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | Proposal then write dispatch | No checked entailment or established non-entailment for an actual output | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | Storage dispatch; JSON action; permissive; later page life | SRC-1, `synthadoc/agents/ingest_agent.py` | [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization) | none | Could reshape, derive or conjecture; output and evidence comparison needed |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | retention | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Proposed page | Action/staging/force branches | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | Persistent write | Retention, not acceptance | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | Wiki readers; Markdown; permissive; later invocations | SRC-1, `synthadoc/agents/ingest_agent.py` | none | none | Draft/staged/live and force paths differ; see record |
| [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | content transformation | implemented | [EPI-OBJ-citation-markers](#epi-obj-citation-markers) | truth-apt transformation: indeterminate | Text and source-line assertions | Model plus structural response safeguards | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | Accepted returned annotation or original text | Traceability candidate, not semantic support | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | Ingest writer/readers; annotated body; permissive; later reads | SRC-1, `synthadoc/agents/ingest_agent.py` | [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) | Coverage not guaranteed | No equality check proves body-preserving annotation |
| [EPI-RTE-structural-citations](#epi-rte-structural-citations) | check/evidence production | implemented | [EPI-OBJ-citation-markers](#epi-obj-citation-markers) | truth-apt transformation: entailed derivation | Marker shape/source membership/available line count | Regex, metadata membership, file line count | see [EPI-RTE-structural-citations](#epi-rte-structural-citations) | see [EPI-RTE-structural-citations](#epi-rte-structural-citations) | Report/audit issue | Conditional reference-integrity deduction only | see [EPI-RTE-structural-citations](#epi-rte-structural-citations) | Lint/report reader; issue list; advisory; this and later review | SRC-1, `synthadoc/agents/lint_agent.py` | [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) | none | Missing sidecar is not semantic endorsement; no source truth test |
| [EPI-RTE-adversarial-review](#epi-rte-adversarial-review) | check/evidence production | implemented | [EPI-OBJ-lint-warnings](#epi-obj-lint-warnings) | truth-apt transformation: indeterminate | Overstatement or conflict with well-established facts | Model on first 3000 body characters | see [EPI-RTE-adversarial-review](#epi-rte-adversarial-review) | see [EPI-RTE-adversarial-review](#epi-rte-adversarial-review) | Warning list or empty/skipped/error-derived list | Fallible model criticism, not independently verified refutation | see [EPI-RTE-adversarial-review](#epi-rte-adversarial-review) | Gate and editor; warning fields; advisory before gate; later lint | SRC-1, `synthadoc/agents/lint_agent.py` | [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization) | none | No raw-source comparison; malformed response may become no warnings |
| [EPI-RTE-warning-gate](#epi-rte-warning-gate) | disposition/acceptance | implemented | [EPI-OBJ-lint-warnings](#epi-obj-lint-warnings) | non-truth-apt policy/content update: lifecycle restriction | Warning count and current state | Configured numeric threshold | see [EPI-RTE-warning-gate](#epi-rte-warning-gate) | see [EPI-RTE-warning-gate](#epi-rte-warning-gate) | Demotion and auto-resolve block | Withheld ordinary-search eligibility, not proof of falsity | see [EPI-RTE-warning-gate](#epi-rte-warning-gate) | Search/auto-resolver; lifecycle/count; enforcing; until changed | SRC-1, `synthadoc/agents/lint_agent.py` | [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization) | none | Gate optional; cached unchanged pages skip reapplication; direct reads/export differ |
| [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | check/evidence production | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: entailed derivation | Source existence/hash/age | Filesystem/hash/clock or opt-in availability check | see [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | see [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | Source availability/change findings | Freshness/availability evidence only | see [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | Lifecycle logic; local facts; enforcing transition condition; current check | SRC-1, `synthadoc/agents/lint_agent.py` | none | none | Hash inequality proves bytes changed, not which proposition changed |
| [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | disposition/acceptance | implemented | [EPI-OBJ-lifecycle-state](#epi-obj-lifecycle-state) | non-truth-apt policy/content update: lifecycle eligibility | Draft/current lifecycle state | Code lifecycle branch | see [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | see [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | Draft becomes active; unavailable sources may archive | Operational admission without factual acceptance criterion | see [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) | BM25; status; permissive/enforcing; later rebuild/query | SRC-1, `synthadoc/agents/lint_agent.py` | [EPI-CLM-active-review](#epi-clm-active-review) | Active is not human-reviewed by invariant | Draft promotion branch does not consume citation/adversarial pass results |
| [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | check/evidence production | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Editorial resolvability | Model on contradiction note and 2000-character body | see [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | see [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | Resolvable boolean and rewrite | Candidate editorial assessment, no complete-source warrant | see [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | Auto-resolution code; JSON; permissive after gate; current lint | SRC-1, `synthadoc/agents/lint_agent.py` | [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization) | none | No expected-answer oracle; source truths not independently tested |
| [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | disposition/acceptance | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Resolvable response | Code consumes model boolean after applicable gate | see [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | see [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | Rewrite/active or unresolved note | Operational acceptance of model answer, not established ampliative knowledge acceptance | see [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) | Store/search; body and lifecycle; enforcing; later invocations | SRC-1, `synthadoc/agents/lint_agent.py` | [EPI-CLM-active-review](#epi-clm-active-review) | Automatic activation bypasses human review | Observed faithful reconciliation unestablished |
| [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: non-ampliative reshaping | Dangling inline and list links | Regex and supplied existing-slug set | see [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) | see [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) | Unlinked text or removed pure-link list item | No new factual warrant | see [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) | Page writer; stripped Markdown; enforcing; later reads | SRC-1, `synthadoc/agents/lint_agent.py` | none | none | Loss of standalone list references; not truth adjudication |
| [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | check/evidence production | implemented | [EPI-OBJ-citation-markers](#epi-obj-citation-markers) | truth-apt transformation: indeterminate | Claim fragment versus cited sidecar lines | Model semantic comparison | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | Supported/drift/hallucination/skipped | Evidence-consuming support judgment over extracted fragment only | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | Cache/CLI/editor; verdict; advisory; later review | SRC-1, `synthadoc/agents/citation_faithfulness_agent.py` | [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) | none | Not a universal truth oracle or implemented page-admission gate |
| [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | retention | implemented | [EPI-OBJ-faithfulness-cache](#epi-obj-faithfulness-cache) | no content change | Audit verdicts | JSON cache merge with source-ingestion key | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | Persistent verdict entries | Retains assessment, not accepted wiki truth | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | Later audit/CLI/editor; cached verdict; advisory/selection; later invocation | SRC-1, `synthadoc/agents/faithfulness_cache.py` | none | none | Key is not exact body or cited-source hash; empty results can be fresh |
| [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | operational admission/selection/consumption | implemented | [EPI-OBJ-faithfulness-cache](#epi-obj-faithfulness-cache) | no content change | Audit result presentation | CLI issue predicate and editor counts | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | Exit 1 for drift/hallucination; editorial guidance | Review signal only | see [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) | Caller/reader; exit status/badges; advisory to human, enforcing process result; current command | SRC-1, `synthadoc/cli/audit.py` | none | none | No inspected automatic rewrite/demotion consumer; downstream shell policy unknown |
| [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | check/evidence production | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: entailed derivation | Regex matches in text | Built-in/custom patterns | see [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | see [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | Line/category matches | Pattern membership only, not factual error or actual confidentiality | see [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | Masker; line numbers; enforcing selection; current scan | SRC-1, `synthadoc/core/retract.py` | none | none | False positives/negatives possible against real secrets |
| [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: non-ampliative reshaping | Selected substrings | Deterministic replacement | see [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | see [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | Redacted page | Withholds content; establishes no corrective claim | see [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal) | Later readers; persisted masked Markdown; enforcing; after scan | SRC-1, `synthadoc/integration/http_server.py` | none | none | Post-write scan; does not prove copies, exports, caches or histories purged |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Eligible ranked pages | Search states/rank/budget | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Budgeted context | Relevance/eligibility, not endorsement | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Synthesis model; context; advisory; current answer | SRC-1, `synthadoc/agents/query_agent.py` | none | none | Retrieved citations can exceed pages delivered in context |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | content transformation | implemented | [EPI-OBJ-query-result](#epi-obj-query-result) | truth-apt transformation: indeterminate | Answer from supplied context | Model synthesis | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Answer and metadata | Neither entailment nor conjecture established without output/input comparison | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | User/session consumer; prose; advisory; response and possible later history | SRC-1, `synthadoc/agents/query_agent.py` | [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) | none | Citation list alone does not establish claim support |
| [RT-RTE-context-export](runtime.md#rt-rte-context-export) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: non-ampliative reshaping | Pack/export selection and truncation | Rank/budget or export-state/file-order filters | see [RT-RTE-context-export](runtime.md#rt-rte-context-export) | see [RT-RTE-context-export](runtime.md#rt-rte-context-export) | Excerpts or bundle context | Delivery with provenance, not preserved source warrant by itself | see [RT-RTE-context-export](runtime.md#rt-rte-context-export) | MCP/OKF consumer provider; excerpts; advisory; later caller invocation | SRC-1, `synthadoc/core/export.py` | none | none | Contradicted pages eligible for default OKF; excerpt can omit qualifications |
| [EPI-RTE-cross-wiki](#epi-rte-cross-wiki) | content transformation | implemented | [EPI-OBJ-query-result](#epi-obj-query-result) | truth-apt transformation: indeterminate | Cross-wiki answer | Model over ranked budgeted peer pages | see [EPI-RTE-cross-wiki](#epi-rte-cross-wiki) | see [EPI-RTE-cross-wiki](#epi-rte-cross-wiki) | Answer plus first-ten-page citation IDs | No independent support or conflict test | see [EPI-RTE-cross-wiki](#epi-rte-cross-wiki) | Answer consumer; prose/citations; advisory; current and later history | SRC-1, `synthadoc/agents/cross_wiki_query_agent.py` | [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) | none | Peer page availability not source warrant; no actual result supplied |
| [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop) | disposition/acceptance | implemented | [RT-OBJ-workflow-protocol](runtime.md#rt-obj-workflow-protocol) | non-truth-apt policy/content update: approval for write | Applicable guarded proposal | Session client boolean; wrappers enforce | see [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop) | see [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop) | Allow/cancel/timeout | Write permission, not evidence of factual acceptance | see [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop) | Registered tool; boolean gate; enforcing where wrapped; workflow/batch or call | SRC-1, `synthadoc/agents/workflows/_base.py` | none | none | Full successor criteria unassessed; approval identity/review not established |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | disposition/acceptance | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Candidate file | Caller-selected promotion/discard | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | Move or delete | Review affordance, not evidence-consuming factual acceptance | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | Live wiki file; move; permissive; later eligible reads | SRC-1, `synthadoc/integration/http_server.py` | none | none | Can remain draft; no proof caller read it |
| [RT-RTE-client-write](runtime.md#rt-rte-client-write) | retention | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: acquisition/import | Caller-supplied edit | Existing/nonempty checks | see [RT-RTE-client-write](runtime.md#rt-rte-client-write) | see [RT-RTE-client-write](runtime.md#rt-rte-client-write) | Persisted replacement | Imported content with unknown warrant | see [RT-RTE-client-write](runtime.md#rt-rte-client-write) | Later reader; Markdown; permissive; subsequent reads | SRC-1, `synthadoc/integration/mcp_server.py` | [EPI-CLM-active-review](#epi-clm-active-review) | Direct edit can preserve active status | Host authorship/checks unknown; clears contradiction note |
| [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | check/evidence production | implemented | [EPI-OBJ-query-facts](#epi-obj-query-facts) | truth-apt transformation: entailed derivation | Answer contains curated fact strings | Case/dash normalized substring check | see [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | see [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | Counts and PASS/WARN | Text-match result only | see [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | Benchmark reader; JSON/printed grade; advisory; retained report | SRC-1, `docs/example/aquaflow/evaluation/scripts/eval_queries.py` | [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization) | Score cannot diagnose root cause | No reproduced run, controlled intervention or automatic production update |
| [EPI-RTE-snapshot-rollback](#epi-rte-snapshot-rollback) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: non-ampliative reshaping | Historical body restoration | Caller index and code existence checks | see [EPI-RTE-snapshot-rollback](#epi-rte-snapshot-rollback) | see [EPI-RTE-snapshot-rollback](#epi-rte-snapshot-rollback) | Body replacement plus undo checkpoint | Recovery, not renewed source warrant | see [EPI-RTE-snapshot-rollback](#epi-rte-snapshot-rollback) | Store/search; restored body; enforcing; later reads | SRC-1, `synthadoc/integration/http_server.py` | none | Lifecycle status preserved despite body replacement | No observed restoration; source/provenance consistency not certified |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-accuracy-optimization](#epi-clm-accuracy-optimization) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair), [EPI-RTE-adversarial-review](#epi-rte-adversarial-review), [EPI-RTE-warning-gate](#epi-rte-warning-gate), [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | none adopted | No objective-linked intervention/comparison; substring scoring cannot separate code/model causes | Compilation, criticism, rewriting and restricted admission are implemented | Maintained accuracy and autonomous successful improvement not demonstrated |
| [EPI-CLM-citation-coverage](#epi-clm-citation-coverage) | see record | SRC-1, `README.md`, doctrine/design | see record | [EPI-RTE-citation-annotation](#epi-rte-citation-annotation), [EPI-RTE-structural-citations](#epi-rte-structural-citations), [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [EPI-RTE-cross-wiki](#epi-rte-cross-wiki) | none adopted | No completeness or semantic correctness measurement adopted | Annotation and optional semantic audit exist; answer citation identifiers are emitted | Annotation can fall back without markers; answer list is not verified support; semantic audit is advisory |
| [EPI-CLM-active-review](#epi-clm-active-review) | see record | SRC-1, `synthadoc/agents/ingest_agent.py`; `README.md`, doctrine/design | see record | [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission), [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair), [RT-RTE-client-write](runtime.md#rt-rte-client-write) | none adopted | No human-review trace; policy wording does not bind all alternate writes | Active-page protection is requested in the ingest decision prompt | Automatic draft promotion and auto-resolution are counterexamples to active implying human-reviewed |

## Bounded conclusion

Synthadoc acquires external source material and retains model-compiled Markdown with provenance and optional line citations. Ingest selection, clipping and separate annotation mean source warrant is unknown, not automatically preserved; synthesis without an actual input/output pair is semantically indeterminate rather than automatically a new conjecture or a checked derivation. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [EPI-RTE-citation-annotation](#epi-rte-citation-annotation).

The checks differ in domain and force. [EPI-RTE-structural-citations](#epi-rte-structural-citations) derives reference-integrity issues, not factual support. [EPI-RTE-adversarial-review](#epi-rte-adversarial-review) generates fallible criticism from truncated page text; [EPI-RTE-warning-gate](#epi-rte-warning-gate) can enforce exclusion from ordinary search and block auto-resolution. [EPI-RTE-faithfulness-audit](#epi-rte-faithfulness-audit) does consume cited sidecar evidence against a named semantic criterion, but licenses at most a fallible support assessment of the extracted fragment, not truth of the source, page-wide acceptance or a production gate. Its retained results affect review display, audit selection and CLI status; these are real consumers even without an automatic page rewrite.

Operational reliance is broader than epistemic acceptance. [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission) activates surviving drafts without consuming a factual test result; [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) can activate a model rewrite from a resolvable boolean. [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop) supplies scoped permission/veto, and [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) supplies move/discard, not established evidence-consuming acceptance with criterion, intended use and scope. No inspected route establishes acceptance of a produced ampliative claim followed by lifecycle integration in that technical sense. This is bounded to inspected routes, not a system-complete negative; individual workflow successor criteria and other included operations remain partly unassessed.

Withdrawal is also heterogeneous. Source unavailability and byte changes alter lifecycle eligibility; warning thresholds can demote; missing links are reshaped; sensitive patterns can be masked after a write. None proves a factual refutation or full revocation across copies and earlier contexts. [EPI-RTE-snapshot-rollback](#epi-rte-snapshot-rollback) can restore a caller-selected historical body with an undo checkpoint and invalidate search, but preserves lifecycle state rather than revalidating its warrant. See [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission), [EPI-RTE-warning-gate](#epi-rte-warning-gate), [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) and [EPI-RTE-sensitive-withdrawal](#epi-rte-sensitive-withdrawal). Default OKF consumption can include contradicted content, while ordinary BM25 admits active/stale; reliance boundaries cannot be unified into an active-only guarantee ([RT-RTE-context-export](runtime.md#rt-rte-context-export)).

Later query, context, export and cross-wiki calls consume retained text under selectors and budgets, not verified source-truth warrants. Their delivered text can shape model behavior; actual dependence and benefit remain unobserved. Parameters, exact numerical version and mutable model resolution are see [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model) and [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding); no weight-learning conclusion follows from changing wiki text.

There is implemented automatic product revision and warning-directed change in operational authority, independently of any proof of learning. Improved future capacity is unestablished. Reflection, autonomous theory-building and reflective theory-building are not established by the supplied workflow method strings or by the scorer; formulated-theory contents, content-dependent decisions, criticism with blame and retained iterative consequences would each need their own evidence. Model opacity supplies neither a positive nor a negative finding for these properties. For the public self-optimization claim, the assessed boundary is the shipped wiki-maintenance system across later invocations and the independent objective is accurate retained content. Warning evidence can determine lifecycle changes and those changes can reach search; no observed subsequent dependence or objective outcome closes the exercised self-improvement chain. Other guidance-revision paths are not exhaustively inspected. [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) licenses substring coverage only, not that objective or component attribution. No single system-wide epistemic score follows.

## Shared records

### Operative objects

#### EPI-OBJ-extracted-text
Label: Extracted source text and sidecar lines

Source text is natural language acquired from external documents through extraction skills; sidecars persist extracted text on disk under `.synthadoc/extracted`. Compilation consumes a clipped/sanitized version, whereas the semantic citation checker reloads named line slices from sidecars. These are different delivery paths, not a guarantee that either faithfully represents the entire original. Source truth and extraction fidelity remain unknown. Closest supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) are routes, not operative-object declarations; no supplied object counterpart. SRC-1, `synthadoc/agents/citation_faithfulness_agent.py`; minimum reloading passage is retained in [EPI-OBJ-citation-markers](#epi-obj-citation-markers).

#### EPI-OBJ-lifecycle-state
Label: WikiPage lifecycle status

This symbolic field lives in persisted page frontmatter and audit state. Fixed consumers use draft/active/stale/contradicted/archived to select transitions or retrieval eligibility. Its permission role differs from factual body content in [EPI-OBJ-wiki-page](#epi-obj-wiki-page); status is not a proof of factual correctness or human authorship. The prompt's interpretation of active as reviewed is separately [EPI-CLM-active-review](#epi-clm-active-review). No supplied object counterpart after comparison with [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair). SRC-1, `synthadoc/agents/lint_agent.py`; transition passage is retained in [EPI-RTE-lifecycle-admission](#epi-rte-lifecycle-admission).

#### EPI-OBJ-query-result
Label: QueryResult answer and citation identifiers

Answer text is natural-language content returned in a Python QueryResult and then caller responses; its factual claims can be truth-apt over the question domain. Citation identifiers are symbolic references emitted beside the answer, not automatically a checked support relation. The synthesis model produces answer text, while code assembles citation identifiers from retrieved pages. Ordinary query storage/history is see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); cross-wiki assembly is see [EPI-RTE-cross-wiki](#epi-rte-cross-wiki). No supplied operative-object counterpart after comparison with that runtime route. SRC-1, `synthadoc/agents/cross_wiki_query_agent.py`; minimum citation assembly passage is in the cross-wiki route. No persisted production answer was supplied.

#### EPI-OBJ-query-facts
Label: AquaFlow curated fact bank and scores

The Python QUERIES bank stores questions and expected fact strings in source. These strings cue domain facts but their scoring consumer uses symbolic substring membership, not proposition interpretation. The resulting matched/total/missing/status JSON is a separate symbolic report part retained by the script, interpreted by benchmark readers. It asserts string coverage, not semantic truth. Neither part has a supplied operative-object counterpart after comparison with [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). SRC-1, `docs/example/aquaflow/evaluation/scripts/eval_queries.py`; scoring/report passages are in [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation).

#### EPI-OBJ-wiki-page
Label: WikiPage compiled claims

Source-native WikiPage body is natural-language Markdown on disk; its factual claims are truth-apt over their subject domains. Lifecycle status/confidence are symbolic metadata, not additional truth warrant. The compiler can create draft/medium pages. Closest supplied records are [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), which trace production/consumption, not this object's identity. No supplied operative-object counterpart declares WikiPage. SRC-1, `synthadoc/agents/ingest_agent.py`; body replacement evidence is also in [RT-RTE-client-write](runtime.md#rt-rte-client-write).

> status=LifecycleState.DRAFT, confidence="medium",
> --- `synthadoc/agents/ingest_agent.py`

#### EPI-OBJ-citation-markers
Label: Inline citation markers and claim fragments

Symbolic source filename/line-range markers are embedded in natural-language page bodies; interpreted as support assertions, their truth-apt content is that specified lines support the associated claim. The checker extracts up to 400 characters before a marker, bounded by the previous marker and last sentence boundary; this fragment is not necessarily the intended whole claim. Markdown and extracted text sidecars are distinct substrates. Closest supplied record [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) mentions annotations but does not declare this object; no supplied object counterpart. SRC-1, `synthadoc/agents/citation_faithfulness_agent.py`.

> window_start = max(prev_end, marker_start - _CLAIM_MAX_CHARS)
> window = body[window_start:marker_start]
> --- `synthadoc/agents/citation_faithfulness_agent.py`

> source_lines = "\n".join(lines[line_start - 1: line_end])
> --- `synthadoc/agents/citation_faithfulness_agent.py`

#### EPI-OBJ-lint-warnings
Label: Lint warning claims and count

A natural-language claim/concern pair is a criticism candidate, stored in page frontmatter by WikiStorage. Its cardinality is symbolic input to a lifecycle gate. A rate-limit sentinel is not a challenged factual claim, although it occupies the same list. Closest supplied route [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) is a container for maintenance, not this mixed object's declaration. No supplied operative-object counterpart. SRC-1, `synthadoc/agents/lint_agent.py`.

> page.lint_warnings = warnings
> self._store.write_page(slug, page)
> --- `synthadoc/agents/lint_agent.py`

#### EPI-OBJ-faithfulness-cache
Label: Faithfulness result cache

JSON at `.synthadoc/faithfulness-cache.json` retains symbolic verdicts, marker IDs, timestamps and a freshness key, plus natural-language reasons. Verdicts assert support/drift/hallucination relative to cited extracted lines, or record skipped evaluation. The key is max source ingestion timestamp, not content identity. No supplied counterpart after comparison with [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair), which explicitly leaves faithfulness untraced. SRC-1, `synthadoc/agents/faithfulness_cache.py`.

> raw = [s.ingested for s in page.sources if s.ingested]
> if not raw:
>     return None
> --- `synthadoc/agents/faithfulness_cache.py`

### Routes

#### EPI-RTE-citation-annotation
Label: Citation annotation and fallback
Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This is the annotation part, not a second declaration of compilation. Ingest supplies a page section plus numbered, line-limited source text to its provider. Guidance requests identical section text except markers. Python rejects too-short, JSON-looking or missing-keyword output, normalizes markers and clamps ranges; otherwise the model's whole returned body can survive. The accepted body and collected citation list return to the ingest writer. These structural safeguards neither compare all words nor validate semantic support. Failure preserves the original section and no citations, rather than rejecting the page. Code admits the proposal; no per-annotation human veto or independent answer oracle appears. Mode is open compilation; trigger is a new/update section. Recovery is original-section fallback, not a factual rollback. Source warrant is unknown after synthesis/annotation. SRC-1, `synthadoc/agents/ingest_agent.py`.

- Immediate return: Annotated or original section and citation list.
- Later read-back: Persisted annotations/body can reach future queries, audits and viewers.
- Delegated visibility: Section and source prefix by configured line limit, not necessarily full source.
- Selection predicate: Nonempty section/source; cache keyed by section body hash and filename; structural safeguards choose response/fallback.
- Invalidation or expiry: bust_cache bypass; source text is not an input of the shown annotation cache key.
- Activation or effect: Accepted annotation text flows to the normal writer; actual semantic preservation unobserved.
- Evidence limits: Same-length or longer rewrites can satisfy safeguards; semantic relation needs actual pair comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "Return ONLY the annotated section — identical to the input except for added ^[...] markers.\n\n"
> --- `synthadoc/agents/ingest_agent.py`

> Returns (annotated_section, citation_list). On any failure returns
> (original_section, []) so ingest always succeeds.
> --- `synthadoc/agents/ingest_agent.py`

> {"body_hash": body_hash, "filename": filename},
> --- `synthadoc/agents/ingest_agent.py`

#### EPI-RTE-structural-citations
Label: Structural citation validation
Part of: [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair)

This part checks reference integrity, not semantic support. Code consumes page source filenames, marker syntax and available sidecar line counts; it derives malformed/broken_ref/out_of_range issues and adds report/audit records. Missing/unreadable sidecars do not generate a semantic assessment. Full-scope lint calls this checker, but its issue list is not a factual acceptance criterion consumed by the later draft-promotion branch. Code proposes/decides issue classification; users may repair later. No factual answer oracle; open maintenance mode, triggered by lint. The route itself admits no content change and supplies no rollback obligation. SRC-1, `synthadoc/agents/lint_agent.py`.

- Immediate return: Issue list, then report and audit events.
- Later read-back: Audit issues may inform later review; no implemented semantic reliance follows merely from no issue.
- Delegated visibility: Report readers receive issue/slug/marker, not source truth verification.
- Selection predicate: Non-system pages in full-scope lint; syntactic and membership predicates.
- Invalidation or expiry: Recomputed on later lint from current files; audit history is not proof of current validity.
- Activation or effect: Reports and audit events wired; no shown citation-issue block on draft promotion.
- Evidence limits: Valid range and listed filename can still cite irrelevant or false source lines.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if filename not in source_basenames:
>     issues.append({"slug": slug, "citation": citation, "reason": "broken_ref"})
>     continue
> --- `synthadoc/agents/lint_agent.py`

> if line_end > line_count:
>     issues.append({"slug": slug, "citation": citation, "reason": "out_of_range"})
> --- `synthadoc/agents/lint_agent.py`

#### EPI-RTE-adversarial-review
Label: Adversarial warning generation
Part of: [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair)

This part generates criticism, separately from its disposition consumer below. Full-scope or scoped-page lint supplies up to 3000 body characters to a configured provider and requests at most N high-confidence overstated or fact-conflicting claims. The model's parametric background is the comparison basis; complete raw-source evidence is not supplied in this prompt. Python parses/filters/caps the response, stores warnings and returns them. Rate limits produce a skipped-warning sentinel; unexpected exceptions return empty warnings; unparseable nonempty responses can be logged as no warnings. This defeats an inference that zero warnings means a successful factual check. Code initiates/filters, model proposes criticisms; no human veto or expected-answer oracle. Open maintenance mode; body change triggers fresh checking. SRC-1, `synthadoc/agents/lint_agent.py`.

- Immediate return: Warnings and token count, aggregated into report.
- Later read-back: Persisted lint_warnings feed later review and auto-resolve gate.
- Delegated visibility: Model sees truncated body, not full sources; report/gate receives parsed warning list.
- Selection predicate: Non-skip slugs; persistent content hash partitions fresh and cached pages.
- Invalidation or expiry: Matching content hash skips model and retains existing warnings; model/prompt changes alone are not keys in the shown comparison.
- Activation or effect: Warning writes and gate call wired; no observed accuracy benefit.
- Evidence limits: Empty and error-derived lists differ epistemically despite same count; source entailment untested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "contradict well-established facts. Only flag issues you are highly confident\n"
> --- `synthadoc/agents/lint_agent.py`

> f"--- PAGE CONTENT ---\n{content[:3000]}"
> --- `synthadoc/agents/lint_agent.py`

> if adv_cache.get(slug) == _content_hash(page.content or ""):
>     cached_pairs.append((slug, page))
> --- `synthadoc/agents/lint_agent.py`

#### EPI-RTE-warning-gate
Label: Warning threshold disposition
Part of: [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair)

This is the gate consumer, distinct from warning production. Configured positive threshold plus enough warnings demotes active/stale pages to contradicted. A separate auto-resolve prerequisite blocks when persisted warning count still meets threshold. Code decides state restrictions from the count, with no human decision required. This is operational rejection/withholding of ordinary-search authority, not evidence that every flagged statement is false. No reference-answer oracle; open maintenance under caller/configuration control. The proposal is lifecycle restriction; rejected conditions return without change. Later edits/lifecycle tools can change status; generic atomic rollback is unestablished. Guidance for warning proposals belongs to [EPI-RTE-adversarial-review](#epi-rte-adversarial-review). SRC-1, `synthadoc/agents/lint_agent.py`; ordinary search consequence is see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).

- Immediate return: Demoted boolean or skip-resolve boolean and report/audit update.
- Later read-back: Persisted status changes later BM25 corpus inclusion; warnings can block later auto-resolution.
- Delegated visibility: Gate sees count/status/configuration, not independent evidence supporting criticisms.
- Selection predicate: Positive configured threshold, count at least threshold, active/stale for demotion.
- Invalidation or expiry: Cached unchanged adversarial pages skip gate reapplication; later edits/configuration and state transitions can change effect.
- Activation or effect: State transition and auto-resolution block implemented; actual provider criticism and subsequent retrieval unobserved.
- Evidence limits: Direct reads/export need not honor ordinary search exclusion; changing threshold alone does not force cached pages through demotion again.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> threshold = self._cfg.lint.adversarial_gate_threshold
> if threshold is None or threshold <= 0:
>     return False
> if len(warnings) < threshold:
>     return False
> --- `synthadoc/agents/lint_agent.py`

> report.adversarial_gate_skipped_resolve.append(slug)
> --- `synthadoc/agents/lint_agent.py`

#### EPI-RTE-lifecycle-admission
Label: Automatic lifecycle admission and withdrawal
Part of: [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair)

This material part separates source availability/freshness checks from admission in the ledger. Filesystem absence, source hash changes, opt-in URL availability and URL age can archive or mark stale. The later draft branch changes draft to active when promotion is enabled, with reason lint passed, without consulting citation issue lists, content-health issues or warning count in that branch. The adversarial demotion gate only handles active/stale, so a draft with warnings is not necessarily rejected before this promotion. Code proposes/decides; no mandatory human review or factual oracle. Open maintenance; full-scope lint enables promotion, while stale-only does not. New state persists; lifecycle history supports inspection but no universal rollback claim is made. Source availability is not source truth, and stale still belongs to the ordinary-query state set. SRC-1, `synthadoc/agents/lint_agent.py`; closest runtime consequence is [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).

- Immediate return: Lifecycle report counters and transition records.
- Later read-back: Status/frontmatter and audit states affect future store/search and maintenance.
- Delegated visibility: Code reads source references/files/audit hashes or dates; later model sees selected content, not a factual proof from lint.
- Selection predicate: Current state, source availability/change/age and promote_drafts option.
- Invalidation or expiry: Later lint, re-ingest, manual edits or lifecycle commands may change state.
- Activation or effect: Draft promotion, stale/archive writes and archive cascades wired.
- Evidence limits: No evidence-consuming factual acceptance criterion for draft promotion; lifecycle synchronization does not certify authorship.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if promote_drafts and current == LifecycleState.DRAFT:
>     await self._transition(slug, page, LifecycleState.DRAFT,
>                            LifecycleState.ACTIVE, "lint passed")
>     report.lifecycle_promoted += 1
>     current = LifecycleState.ACTIVE
> --- `synthadoc/agents/lint_agent.py`

#### EPI-RTE-link-cleanup
Label: Dangling link cleanup
Part of: [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair)

The deterministic helper removes a whole pure-link list item when target is missing, or preserves display text without its link for an inline occurrence. Lint calls cleanup; archive cascades also invoke link removal. This is non-ampliative reshaping with information loss, not checking truth of linked propositions. Concrete code deduction, not execution: with existing_slugs empty, `See [[missing|Evidence]].` becomes `See Evidence.`; a line `- [[missing]]` is dropped by the pure-list branch. Code owns this cleanup, no per-item human veto or expected-answer oracle. Open maintenance is triggered by lint/archive, guided by existing-slug membership; later storage/history can be inspected but automatic restoration of removed links is not shown. SRC-1, `synthadoc/agents/lint_agent.py`.

- Immediate return: Rewritten string; callers write pages and report counts.
- Later read-back: Cleaned retained body reaches subsequent readers.
- Delegated visibility: Later reader receives display text or absence, not necessarily the removed slug.
- Selection predicate: Regex link/list match and existing-slug membership.
- Invalidation or expiry: Recreating target does not itself reconstruct removed link in this helper.
- Activation or effect: Text rewrite and caller persistence wired; concrete example deduced from implementation only.
- Evidence limits: Deletion can remove a retrieval/navigation lead; not an entailment or rejection of target content.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> display = parts[1].strip() if len(parts) > 1 else parts[0].strip()
> return display if slug_key not in existing_slugs else match.group(0)
> --- `synthadoc/agents/lint_agent.py`

> if slug_part not in existing_slugs:
>     continue  # drop the whole list-item line
> --- `synthadoc/agents/lint_agent.py`

#### EPI-RTE-faithfulness-audit
Label: Semantic citation audit and result consumers

No supplied counterpart after comparison: [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) explicitly leaves this responsibility untraced. This separate on-demand job loops active pages, extracts claim fragments and cited sidecar lines, and asks the configured adversarial provider whether lines clearly support, overstate or contradict the claim. Code constrains verdict vocabulary; missing sidecars/provider failures/omitted indices yield skipped, and missing citations yield no checks. The returned model judgment consumes source evidence against a named criterion; it is not formal entailment, source-truth verification or a page-wide acceptance decision. Comparison domain is the extracted fragment and sidecar slice, not all surrounding context or original binary document.

The orchestrator merges results into a JSON cache. Freshness uses source ingestion timestamps, so a body or sidecar edit without those timestamps changing need not be marked stale. Checked pages with no results can receive fresh empty entries. CLI reads the cache and exits nonzero for drift/hallucination; Obsidian displays counts and recommends editorial review or no action. This is a consequential consumer chain, but inspected code here does not automatically demote, rewrite or accept the page based on faithfulness. Caller/configuration selects audit; model proposes verdict, code parses/records; human editorial disposition is recommended but not observed. No expected-answer oracle; open audit mode. Cache replacement and later force/stale reruns refresh assessment, not content rollback. SRC-1, `synthadoc/agents/citation_faithfulness_agent.py`, `synthadoc/agents/faithfulness_cache.py`, `synthadoc/core/orchestrator.py`, `synthadoc/cli/audit.py`, `obsidian-plugin/src/main.ts`.

- Immediate return: Verdicts or skipped records; job completion counts; CLI display/exit or editor display.
- Later read-back: Cache verdicts are reloaded by later CLI/editor/audit-selection invocations.
- Delegated visibility: Judge receives fragment and cited lines; user gets verdict/reason/marker, not a guaranteed complete proposition alignment.
- Selection predicate: Active pages, optional slug/stale selection; regex citations; available sidecars; vocabulary/parser checks.
- Invalidation or expiry: Cache key comparison uses max source-ingestion timestamp, not body/source content digest; force can request rerun.
- Activation or effect: Persisted audit results alter CLI status and editor guidance; no observed editorial repair or automatic production gate established.
- Evidence limits: Supported is a fallible scoped judgment, not source truth or accepted ampliative knowledge; skipped/no-citation is not a pass.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "supported"     — source lines clearly support the claim
> "drift"         — claim overstates, extrapolates from, or partially misrepresents the source
> "hallucination" — source lines do not support or directly contradict the claim
> --- `synthadoc/agents/citation_faithfulness_agent.py`

> merge_results_into_cache(wiki_root, all_results, store, checked_slugs=slugs)
> --- `synthadoc/core/orchestrator.py`

> if entry is None or entry.get("page_key") != key:
>     stale.append(slug)
> --- `synthadoc/agents/faithfulness_cache.py`

> has_issues = any(r.verdict in ("drift", "hallucination") for r in all_results)
> raise SystemExit(1 if has_issues else 0)
> --- `synthadoc/cli/audit.py`

> ? "Hallucinations and drifts indicate claims that need editorial review. "
> --- `obsidian-plugin/src/main.ts`

#### EPI-RTE-sensitive-withdrawal
Label: Sensitive pattern scanning and masking

No supplied counterpart after comparison with [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair), which leaves sensitive retraction untraced. Pattern scanner emits line/category matches without the matched value; masker substitutes REDACTED on matched lines. Post-ingest HTTP worker scans completed-job created/updated live files when configured and writes masked text plus audit event. CLI also exposes scan/apply with confirmation or yes bypass; periodic scanning is registered but not exhaustively assessed here. This withdraws text, not false claims, and is not evidence of complete deletion from source files, histories, exports, cache or already supplied contexts. Code evaluates pattern membership; actual sensitivity is not determined. Caller configuration/CLI approval decides permission; there is no factual oracle. Mode is open privacy maintenance. Guidance consists of built-in/custom patterns, not a theory of factual correctness; rollback of redaction is not shown in this route. SRC-1, `synthadoc/core/retract.py`, `synthadoc/integration/http_server.py`, `synthadoc/cli/retract.py`.

Concrete implementation deduction: line `Contact alice@example.com` matches the email regex, producing the line/category record; masking that match substitutes `[REDACTED]`, leaving `Contact [REDACTED]`. This follows inspected regex/substitution code without running the target. It is non-ampliative removal; it does not establish that the email was real or confidential.

- Immediate return: ScanMatch list; masked string and changed-line count; post-ingest audit event.
- Later read-back: Persisted masked live page reaches later readers; retained prior copies are not shown purged.
- Delegated visibility: Match consumers receive line/category, not values; subsequent page consumer sees masked body.
- Selection predicate: Enabled scan, completed ingest, created/updated slugs and matching built-in/custom regex; CLI has additional scope/apply options.
- Invalidation or expiry: Repeated scanning handles current text; post-ingest branch itself does not show universal search/cache invalidation.
- Activation or effect: Actual write of masked text implemented after a successful ingest, not before initial content persistence.
- Evidence limits: Pattern completeness, all-copy purge, deployed enablement and observed redaction unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> new_line = pattern.sub(repl, new_line)
> --- `synthadoc/core/retract.py`

> masked, lines_changed = scanner.mask_page(slug, content, matches)
> if lines_changed > 0:
>     page_path.write_text(masked, encoding="utf-8")
> --- `synthadoc/integration/http_server.py:792-794`

#### EPI-RTE-cross-wiki
Label: Cross-wiki answer synthesis

Distinct from [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query): this agent selects peer servers, fetches /retrieve results and synthesizes across them. Static routing rules or a model choose registered wikis, always including own wiki where registered. Code merges/sorts pages by reported scores, caps context at 80000 characters and trims history; model receives page-labeled text and instructions to use only those pages. Answer citations are generated separately from first ten merged pages; these need not exactly equal pages actually delivered under the context budget. Returned text is not checked for factual support or source conflict by this path. Code directs context, model proposes answer; no per-answer human veto or expected-answer oracle. Mode is open query, not an experiment. No content-admission guarantee is provided; caller can ask again but no factual rollback is meaningful for an already delivered answer. SRC-1, `synthadoc/agents/cross_wiki_query_agent.py`.

- Immediate return: QueryResult with answer, namespaced citation identifiers, offline/routing metadata, or no-result/action result.
- Later read-back: Reads retained peer wiki pages and supplied history; this agent does not itself persist answer into a wiki.
- Delegated visibility: Provider sees budgeted cross-wiki context; peers receive question/subquestions/top_k, not accumulated parent conversation.
- Selection predicate: Routing keywords or model wiki choice, valid registry filter, own-wiki inclusion, peer ranks and character budget.
- Invalidation or expiry: Later call re-fetches peers; peer cache/coherence and opaque provider state uninspected.
- Activation or effect: Model delivery and response return implemented; actual support and dependence on specific claims unobserved.
- Evidence limits: Cross-peer score comparability, factual truth and citation support not independently validated.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> cited_slugs = [
>     f"{p['wiki_name']}::{p['slug']}"
>     for p in pages[:10]
> ]
> --- `synthadoc/agents/cross_wiki_query_agent.py`

#### EPI-RTE-snapshot-rollback
Label: Caller-selected snapshot rollback

This distinct recovery path adds detail to, rather than replaces, [RT-RTE-client-write](runtime.md#rt-rte-client-write) and [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop), which mention possible history recovery but do not declare this HTTP handler. Caller selects page, snapshot index and reason. Code checks page/snapshot existence, records current content as a forced undo checkpoint, strips possible snapshot frontmatter, restores the body, writes and invalidates epoch/search. Current lifecycle state is preserved; the body can change while operational state remains active. This is recovery permission, not factual revalidation or renewed acceptance. Caller decides, software performs I/O; human identity and evidence review remain unresolved. There is no expected-answer oracle; mode is open recovery. The proposal is historical body replacement, guidance is caller selection, rejection is missing page/snapshot or caller abstention, and the stored pre-rollback checkpoint affords another rollback. SRC-1, `synthadoc/integration/http_server.py`.

- Immediate return: Snapshot metadata, restored character count and undo event index, or 404.
- Later read-back: Restored body reaches subsequent page/query consumers; checkpoint supports later rollback.
- Delegated visibility: Handler receives index/reason; later model receives restored body under ordinary selectors, not automatic evidence that it is more accurate.
- Selection predicate: Explicit slug/index plus available content_snapshot.
- Invalidation or expiry: Epoch bump and search invalidation implemented; snapshot/history purges are separate operations, not fully assessed here.
- Activation or effect: Forced checkpoint and body replacement wired; no observed replay or improved factual result.
- Evidence limits: Historical availability does not establish truth or restoration of source/provenance consistency across all stores.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> page.content = strip_frontmatter(snap["content_snapshot"])
> orch._store.write_page(slug, page)
> orch._bump_epoch()
> orch._search.invalidate_index()
> --- `synthadoc/integration/http_server.py`

#### EPI-RTE-answer-evaluation
Label: AquaFlow answer fact-string evaluation

No supplied counterpart after comparison with [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), which has no reference-answer oracle in ordinary production. This offline evaluation script supplies a 15-question curated fact-string bank, requests query answers from a configured server, normalizes case and dashes, counts substring matches and writes per-model-label JSON and printed grades. The model label is caller text, not verified actual model identity. The explicit oracle is curated expected strings used for scoring, not a complete expected answer. These scores are consumed by report writing/comparison, not automatic production policy update. Human-curated questions/facts define criteria; software scores; the script's low-score root-cause wording is not a causal diagnosis.

Domain: occurrence of selected fact strings in English/Chinese demo answers. Concrete deduction from code, not execution: answer `There is no PFAS.` with facts `["pfas"]` yields matched=1,total=1 and PASS despite negation. This evaluator measures string presence, not correctness, source support or logical relation. Executable grade emits PASS at 85% and WARN below, whereas the file's introductory docstring advertises PASS/WARN/FAIL tiers; automatic FAIL is not implemented in grade. No intervention holds inputs fixed while independently varying compilation or another component. No benchmark result file is adopted as observed success here. SRC-1, `docs/example/aquaflow/evaluation/scripts/eval_queries.py`.

- Immediate return: Counts/missing list, printed PASS/WARN/error and JSON report.
- Later read-back: Saved result files can be loaded by comparison mode; no automatic production update consumer shown.
- Delegated visibility: Server receives question; scorer gets answer text and curated strings, not source evidence or answer semantics.
- Selection predicate: Fixed query bank, caller server port/model label; normalized substring matching.
- Invalidation or expiry: Subsequent invocation overwrites model-label report; no verified numerical provider pin or causal design.
- Activation or effect: Report/grade production wired, execution unobserved; no established self-improvement consequence.
- Evidence limits: Outcome fit cannot locate blame in code/model/data; matching strings can appear in false or negated answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if _norm(fact) in answer_norm:
>     matched.append(fact)
> else:
>     missing.append(fact)
> --- `docs/example/aquaflow/evaluation/scripts/eval_queries.py`

> return "PASS" if matched / total >= 0.85 else "WARN"
> --- `docs/example/aquaflow/evaluation/scripts/eval_queries.py`

### Claims

#### EPI-CLM-accuracy-optimization
Label: Accuracy through autonomous self-optimization

Public doctrine links maintained accuracy to autonomous self-optimization. Closest supplied [RT-CLM-confirm-scope](runtime.md#rt-clm-confirm-scope) and [RT-CLM-effect-boundary](runtime.md#rt-clm-effect-boundary) are control/effect claims, not this accuracy/improvement claim; no counterpart. SRC-1, `README.md`, doctrine/design. Mechanisms alone do not establish this claimed benefit or causal pathway.

> **Engineered for solo users and enterprises alike, providing a domain-specific knowledge base that scales seamlessly while maintaining accuracy through autonomous self-optimization.**
> --- `README.md`

#### EPI-CLM-citation-coverage
Label: Every claim and answer source-linked

Public doctrine promises claim-level source-line citations and answer source citation. No supplied claim counterpart after comparison with [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), which report implementations rather than declare this public claim. SRC-1, `README.md`, doctrine/design. Traceability, annotation completeness and semantic support are separate assessments; optional semantic audit does not make annotation or answer support invariant.

> **Citation quality:** Generated pages include inline citations linking every claim to its source lines. Pages without citations trigger a model-compatibility warning — use Gemini 2.5 Flash or higher for reliable citation annotation.
> --- `README.md`

> Cross-references are built automatically, contradictions are detected and surfaced, orphan pages are flagged, and every answer cites its sources.
> --- `README.md`

#### EPI-CLM-active-review
Label: Active implies human-reviewed authority

The ingest decision prompt instructs the model to treat active pages as human-reviewed and authoritative, and prefer flag over update for factual disputes. README repeats human-review language. This claim/policy differs from scoped write-confirmation in [RT-CLM-confirm-scope](runtime.md#rt-clm-confirm-scope); no supplied claim counterpart. SRC-1, `synthadoc/agents/ingest_agent.py`, `README.md`, doctrine/design. Counterexamples are automatic draft promotion, auto-resolution and state-preserving direct writes; this qualifies claimed authority without denying that a particular active page could have been human reviewed.

> "RULE 1b — ACTIVE PAGE PROTECTION: A page with status='active' has been human-reviewed and is\n"
> "authoritative. Treat its existing facts as correct. If the source gives a DIFFERENT value,\n"
> --- `synthadoc/agents/ingest_agent.py`
