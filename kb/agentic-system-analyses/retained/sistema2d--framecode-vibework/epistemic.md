---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "FrameCode-VibeWork epistemic routes: sourced wiki promotion, source review, declared QA evidence and bounded deterministic checks."
run-id: AAS-2026-11-08-framecode-vibework-d38fb53e8013-01
reviewed-boundary: "847cdcedc02d08531961c8367f4e2ddb2dc392f1"
---

# FrameCode-VibeWork epistemic report

## Source-and-claim boundary

Can FrameCode-VibeWork (FCVW) turn project evidence into warranted reusable understanding, distinguish intended behavior from observations, and revise later reliance? The assessed target is the shipped governance/memory layer, not its external host's inference or a receiving application's truth. Scope, exclusions, cutoff and evidence identity are those of the [boundary](boundary.md#boundary-and-evidence); SRC-1 is registered in its [Source register](boundary.md#source-register). No target execution was performed.

The public knowledge claims assessed here are [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) and [EPI-CLM-product-evidence](#epi-clm-product-evidence); the routing/authority claim is [RT-CLM-context-controls](runtime.md#rt-clm-context-controls). The negative control is the system's own separation of Markdown contracts from proof of execution, retained in the boundary. Neither a metadata label nor operational continuation establishes acceptance of an ampliative claim.

### Coverage

Direct reads below add SRC-1 implementation or doctrine/design coverage at the frozen commit. Supplied findings are identified separately; they are not represented as direct inspection.

| Entry point or operation | SRC-1 source path | Coverage and consequential record |
|---|---|---|
| Wiki promotion, review, handoff and archive | `FCVW/wiki/README.md`, `FCVW/skills/wiki-curator/SKILL.md` | Direct full doctrine reads; [EPI-RTE-wiki-review](#epi-rte-wiki-review), [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate); session retention is also covered by supplied [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission). |
| QA discovery, live observation and user decisions | `FCVW/skills/QA/SKILL.md`, `FCVW/skills/QA/PRODUCT_WIKI.md` | Direct full doctrine reads; material added coverage beyond runtime's summary: [EPI-RTE-live-qa](#epi-rte-live-qa), [EPI-RTE-divergence-decision](#epi-rte-divergence-decision). |
| Selected QA CLI check | `tools/qa_wiki_fcvw.py` | Direct complete implementation read, including main; [EPI-RTE-qa-check](#epi-rte-qa-check). This is a separate operation, not one of the five registered MCP tools. |
| Optional evidence-method and authority checks | `tools/validate_fcvw.py` | Direct `check_evidence`, frontmatter checks, and main dispatch; [EPI-RTE-evidence-check](#epi-rte-evidence-check). Other validator checks are supplied or unassessed, not a semantic audit of every rule. |
| Digest, review dates, typed graph | `tools/knowledge_sources_fcvw.py`, `tools/knowledge_graph_fcvw.py` | First file read completely; graph construction body inspected; [EPI-RTE-source-review](#epi-rte-source-review). Graph CLI/output and target-resolution helpers not independently audited. |
| Index builder CLI | `tools/build_context_index.py` | Direct complete implementation read; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). Concrete transformation traced below. |
| Retrieval scoring, filtering and output | `tools/retrieve_context.py` | Direct `bm25` body; CLI dispatch, routing and budget consumers supplied by [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-CLM-context-controls](runtime.md#rt-clm-context-controls). |
| MCP routes, sections, validation, queue, digest | `tools/mcp_server_fcvw.py` | Direct validator/queue/digest handlers and handler registry; remainder supplied by [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks). |
| Hook start, edit denial and stop repair | `tools/hook_fcvw.py` | Supplied [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle), including fail-open and shell bypass cases; not a new direct read. |
| Retrieval evaluation CLI | `tools/benchmark_retrieval_fcvw.py` | Direct complete implementation read; [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark). |
| Local tests, release/layout verification | `tools/check_fcvw.py` | Supplied [RT-RTE-local-checks](runtime.md#rt-rte-local-checks); individual test assertions and release verification bodies not audited here. No universal correctness conclusion. |
| Plans, skill improvement, factory, upgrade | `AGENTS.md`, `FCVW/skills/self-improvement/SKILL.md`, `FCVW/skills/agent-factory/SKILL.md`, `tools/upgrade_fcvw.py` | Supplied [RT-RTE-governed-change](runtime.md#rt-rte-governed-change), [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), [RT-RTE-framework-upgrade](runtime.md#rt-rte-framework-upgrade); no new claim of automatic semantic acceptance. |
| Historical pages, feedback instances, remaining tools and QA target adapters | `FCVW/`, `tools/` | Available but unassessed beyond rows above. Prevent exhaustive enumeration of actual claim instances, criticisms and every evaluator domain; do not support a system-complete negative. |

No host/model trace, consuming-project requirements corpus, live QA evidence or controlled intervention was supplied. This prevents actual acceptance, adherence, execution, semantic preservation of generated prose, real task benefit and causal improvement conclusions. The external distributed-parametric component retains the limits in [RT-CMP-host-model](runtime.md#rt-cmp-host-model); neither parameter adaptation nor absence of learning is inferred.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | Reusable project claims, synthesis, failures, questions and imported material | see [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | SRC-1, `FCVW/wiki/README.md` | No project claim instance authenticated. |
| [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | Declared evidence/status/provenance claims; typed edges | see [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | SRC-1, `tools/validate_fcvw.py` | Symbolic labels are not the underlying evidence. |
| [EPI-OBJ-product-contract](#epi-obj-product-contract) | Approved, provisional or unknown expected behavior, scoped by case | see [EPI-OBJ-product-contract](#epi-obj-product-contract) | SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md` | Approval provenance remains a host responsibility. |
| [EPI-OBJ-qa-run](#epi-obj-qa-run) | Assertions of execution, observations, evidence references and user decisions | see [EPI-OBJ-qa-run](#epi-obj-qa-run) | SRC-1, `tools/qa_wiki_fcvw.py` | Declared run rows, not observed execution in this analysis. |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Method guidance; individual truth-apt assumptions depend on the loaded skill | see [RT-OBJ-skill](runtime.md#rt-obj-skill) | SRC-1, `FCVW/AI.md` | Policy content is not automatically knowledge about outcomes. |
| [RT-OBJ-skill-frontmatter](runtime.md#rt-obj-skill-frontmatter) | None intrinsically: routing declarations and version fields | see [RT-OBJ-skill-frontmatter](runtime.md#rt-obj-skill-frontmatter) | SRC-1, `tools/validate_fcvw.py` | Discovery metadata does not warrant method efficacy. |

Indexed excerpts and evaluation reports are material outputs of the cited routes, not new canonical knowledge objects. Their source content, symbolic selection and derived metrics are kept separate in the route assessments.

## Authority-route ledger

All rows describe architecture, not observed operation. Fields owned by a declaring record are referenced rather than reproduced. Multiple rows for one record distinguish functions, not duplicate route identities.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-wiki-review](#epi-rte-wiki-review) | disposition/acceptance | doctrine only | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | no content change | Promotion/review decision | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | Evidence-consuming source review is requested; no performed acceptance decision supplied. |
| [EPI-RTE-wiki-review](#epi-rte-wiki-review) | content transformation | doctrine only | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | truth-apt transformation: indeterminate | Source-bounded synthesis or revision | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | see [EPI-RTE-wiki-review](#epi-rte-wiki-review) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | May import, reshape, derive or conjecture; no input/output trace resolves semantic relation. |
| [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | retention | doctrine only | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | no content change | Keep selected pages and history | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | Retention alone does not establish acceptance. |
| [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | lifecycle integration | doctrine only | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | non-truth-apt policy/content update: index, canonical and supersession links | Connect reviewed knowledge for later use | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | see [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | Conditional on prior review; a link alone does not prove its prerequisite. |
| [EPI-RTE-evidence-check](#epi-rte-evidence-check) | check/evidence production | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | truth-apt transformation: entailed derivation | Optional evidence labels and authority compatibility | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | see [EPI-RTE-evidence-check](#epi-rte-evidence-check) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | Formal consistency/referent existence, not truth, source entailment or execution. |
| [EPI-RTE-source-review](#epi-rte-source-review) | check/evidence production | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | truth-apt transformation: entailed derivation | Digest mismatch, direct dependent review, overdue dates | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | see [EPI-RTE-source-review](#epi-rte-source-review) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | Changed bytes or selected section imply review condition, not changed truth. |
| [EPI-RTE-live-qa](#epi-rte-live-qa) | content transformation | doctrine only | [EPI-OBJ-qa-run](#epi-obj-qa-run) | truth-apt transformation: acquisition/import | Observe bounded application cases | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | [EPI-CLM-product-evidence](#epi-clm-product-evidence) | none | External observation enters recorded assertions; warrant unknown without trace. |
| [EPI-RTE-live-qa](#epi-rte-live-qa) | check/evidence production | doctrine only | [EPI-OBJ-product-contract](#epi-obj-product-contract) | no content change | Actual behavior against approved scoped expectations | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | see [EPI-RTE-live-qa](#epi-rte-live-qa) | [EPI-CLM-product-evidence](#epi-clm-product-evidence) | none | Requested live comparison; outcome fit does not explain its producing mechanism. |
| [EPI-RTE-qa-check](#epi-rte-qa-check) | check/evidence production | implemented | [EPI-OBJ-qa-run](#epi-obj-qa-run) | truth-apt transformation: entailed derivation | Selected contracts and declared case/decision coverage | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | [EPI-CLM-product-evidence](#epi-clm-product-evidence) | none | Hashes bind the selected contract representation; references do not authenticate evidence. |
| [EPI-RTE-qa-check](#epi-rte-qa-check) | operational admission/selection/consumption | implemented | [EPI-OBJ-qa-run](#epi-obj-qa-run) | no content change | CLI exit from derived execution/decision status | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | see [EPI-RTE-qa-check](#epi-rte-qa-check) | [EPI-CLM-product-evidence](#epi-clm-product-evidence) | none | Blocks CLI success, not arbitrary host changes. |
| [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | disposition/acceptance | doctrine only | [EPI-OBJ-product-contract](#epi-obj-product-contract) | no content change | User chooses direction for each divergence | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | see [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | [EPI-CLM-product-evidence](#epi-clm-product-evidence) | none | Intent approval differs from factual acceptance and cannot retroactively pass a failed case. |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | content transformation | implemented | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | truth-apt transformation: non-ampliative reshaping | Markdown to chunks, excerpts and references | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | SRC-1, `tools/retrieve_context.py` | [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | none | Lexical delivery preserves available text only; truncation can remove conditions. |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | no content change | Rank/filter optional context | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | SRC-1, `tools/retrieve_context.py` | [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | none | Freshness/status influence ranking, not endorsement or exclusion of every disputed claim. |
| [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | check/evidence production | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | truth-apt transformation: entailed derivation | Labeled retrieval/routing performance | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | see [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark) | [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | none | Labeled corpus only; no model-executed task correction or causal component benefit. |
| [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | operational admission/selection/consumption | implemented | [RT-OBJ-skill](runtime.md#rt-obj-skill) | no content change | Plan presence and changed-file validator findings | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | see [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) | SRC-1, `tools/hook_fcvw.py` | [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | none | Conditional protocol; a plan and permission to continue grant no epistemic license. |
| [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | behavior/policy adaptation | doctrine only | [RT-OBJ-skill](runtime.md#rt-obj-skill) | non-truth-apt policy/content update: revise operational guidance | Evidence-triggered skill/profile revision | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | see [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission) | SRC-1, `FCVW/skills/self-improvement/SKILL.md` | [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | none | An afforded host-mediated improvement path; exercised learning and causal benefit unestablished. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | see [EPI-CLM-sourced-knowledge](#epi-clm-sourced-knowledge) | SRC-1, `FCVW/wiki/README.md`; doctrine/design | [EPI-RTE-wiki-review](#epi-rte-wiki-review), [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate) | [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-source-review](#epi-rte-source-review) | None supplied | Optional labels and existence checks are narrower than semantic justification | A sourced-review protocol plus deterministic review support | No authenticated accepted ampliative instance; no equation of validated label with truth. |
| [EPI-CLM-product-evidence](#epi-clm-product-evidence) | see [EPI-CLM-product-evidence](#epi-clm-product-evidence) | SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`; doctrine/design | [EPI-RTE-live-qa](#epi-rte-live-qa), [EPI-RTE-divergence-decision](#epi-rte-divergence-decision) | [EPI-RTE-qa-check](#epi-rte-qa-check) | None supplied | Declared-only provenance explicitly prevents execution/consent attestation | Concrete scoped test/evidence contract, not only generic wiki curation | Actual live comparison, approval and completeness remain unknown. |
| [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | see [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | SRC-1, `FCVW/AI.md`; doctrine/design, supplied record | see [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [EPI-RTE-evidence-check](#epi-rte-evidence-check) | None supplied | Metadata can affect builder/ranker before validation; validator does flag incompatible authority | Optional scoring differs from instruction authority; checks exist at a separate consumer | Added countercase qualifies any inference that authority spoofing is never checked; it does not make retrieval fail-closed. |

## Bounded conclusion

FCVW's source-native knowledge loop is promotion, selective source review, lifecycle linking and later on-demand use. It explicitly separates raw imports, uncertain claims, validated pages, historical handoffs and authoritative project state. Those are meaningful design distinctions, not evidence that a particular claim was accepted. The curator requests evidence-consuming decisions under reuse, source and nonduplication criteria; retained prose may be acquisition, reshaping, derivation or conjecture. Without paired source/output and decision records, its semantic relation is indeterminate, not automatically ampliative. [EPI-RTE-wiki-review](#epi-rte-wiki-review), [EPI-RTE-wiki-integrate](#epi-rte-wiki-integrate).


The deterministic checks consume retained wiki provenance/status metadata on later validator and graph invocations; their lack of writes does not make that read-back inapplicable. This wiring does not itself deliver claim bodies, retain output reports or accept their semantic content. [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-source-review](#epi-rte-source-review).

The deterministic layer warrants narrower propositions: metadata/reference consistency, changed tracked bytes/sections, declared contract identity, case coverage and scores against explicit retrieval labels. None establishes the truth of a referenced source or the fidelity of an asserted observation. A digest mismatch requests review and does not revoke a claim automatically. Contradictory or superseded records receive a ranking penalty rather than universal withdrawal from retrieval. Authority metadata is checked by the validator but is accepted first by the independent index builder; there is no inspected mandatory validation-before-index chain. [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-source-review](#epi-rte-source-review), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

QA is a distinct, consequential route omitted from the runtime's detailed account, not a contradiction requiring replacement of its valid container records. It requests direct application observations, independently sourced expectations, per-case comparisons and explicit user direction on divergence. Its checker binds declared results to selected contract hashes and keeps functional failure separate from decision clearance. The CLI enforces its result through exit status; the host must still obey the resulting stop/review decision. No shipped application execution evidence establishes that the live route actually operated. [EPI-RTE-live-qa](#epi-rte-live-qa), [EPI-RTE-qa-check](#epi-rte-qa-check), [EPI-RTE-divergence-decision](#epi-rte-divergence-decision).

Later behavioral force is differentiated: ranked excerpts advise an invoking host; canonical policy/skill bodies instruct a host under its higher-level authority; hooks can conditionally deny recognized edits or request repair; a user decision permits a dependent QA direction, not a factual pass. These horizons extend only through the consumers actually named in the records. The external model's parameters and actual compliance remain uninspected. [RT-BAP-policy-consumption](runtime.md#rt-bap-policy-consumption), [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle), [RT-CMP-host-model](runtime.md#rt-cmp-host-model).

Evidence-triggered method revision is independently afforded by [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission). Its localized guidance, requested content-directed diagnosis and retained patches do not establish exercised theory criticism/iteration, improved future capacity, autonomous execution of all internal operations or successful self-improvement. The runtime's separately scoped theory-builder, reflection and self-improvement findings remain bounded; this report adds no single epistemic score or system-wide verdict. Retrieval evaluation is a separate bounded check, not a causal demonstration of these properties: [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-wiki-content
Label: Wiki claim prose

Natural-language note bodies in versioned Markdown: concepts, patterns, failures, synthesis, questions, raw material and session claims. Producer and semantic interpreter are the host/human; source records constrain the intended warrant. Distinct from procedural guidance in [RT-OBJ-skill](runtime.md#rt-obj-skill); no supplied object denotes this claim-bearing content. Product contracts and QA runs below are distinct specialized operative parts rather than generic prose assessments. SRC-1, `FCVW/wiki/README.md`.

> - Knowledge pages state reusable understanding, decisions, patterns, questions, or syntheses.
> --- `FCVW/wiki/README.md`

> - `type: raw` pages preserve imported material when preservation is necessary; they are not validated knowledge.
> --- `FCVW/wiki/README.md`

#### EPI-OBJ-wiki-metadata
Label: Wiki evidence and lifecycle metadata

Symbolic YAML fields stored with Markdown; evidence_method, verified_by, status, source_digest, derived_from and relationship fields are consumed by Python checks, graph construction and indexing. Their strings assert provenance or state; they are not an independent evaluator of prose meaning. Distinct from skill routing metadata in [RT-OBJ-skill-frontmatter](runtime.md#rt-obj-skill-frontmatter). Same physical pages as [EPI-OBJ-wiki-content](#epi-obj-wiki-content), different consumer/force. SRC-1, `FCVW/wiki/README.md`, `tools/validate_fcvw.py`.

> Frontmatter relations remain machine metadata.
> --- `FCVW/wiki/README.md`

#### EPI-OBJ-product-contract
Label: Product surface behavior contract

Versioned Markdown surface pages carry natural-language expectations and sources interpreted by the host. Stable IDs, element/case tables, expectation classifications and selected contract hashes have symbolic consumers in the selected-page checker. The checker hashes the parsed contract, not all surrounding prose. Scope is selected surfaces/cases, not arbitrary hidden application behavior. Distinct from [EPI-OBJ-wiki-content](#epi-obj-wiki-content) by case-specific tests and user-approval path; no supplied counterpart after comparison with [RT-OBJ-skill](runtime.md#rt-obj-skill). SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`, `tools/qa_wiki_fcvw.py`.

> Classify expectations as approved, provisional or unknown. Approved means supported by an existing approved requirement, acceptance criterion, design decision or owner confirmation.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

#### EPI-OBJ-qa-run
Label: QA observation and decision record

Application-owned Markdown audit. Observation/evidence text is a natural-language assertion read by the host; result enums, case identities, contract hashes and divergence decision fields have symbolic coverage/status consumers. File storage can preserve earlier runs across sessions; a supplied row is not authenticated interaction evidence. Unlike [EPI-OBJ-product-contract](#epi-obj-product-contract), this records asserted actual behavior and decisions, not expected intent. No supplied operative object covers this output. SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`, `tools/qa_wiki_fcvw.py`.

> No application execution records are shipped in the clean framework.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

### Routes

#### EPI-RTE-wiki-review
Label: Source-bounded wiki promotion and revision

Part of: [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission)

This is the knowledge-specific admission part, not a replacement for the runtime's combined asset gate. Trigger sources enter host/human inspection; the host proposes promotion or revision against reusable, sourced and not-already-canonical criteria. The reviewer may confirm, update, supersede, invalidate or defer. Claimed evaluator domain: the selected sources and affected pages, not the entire wiki. Intended use: reusable current project understanding. Acceptance is requested, not observed; neither a page's existence nor its label proves it occurred. The human has scope/veto authority but per-note human approval is not universally required. Answer oracle: linked project evidence where available, not model confidence. Operating mode: open maintenance requests and changed-source triggers. Rejection is permitted; source history/versioning supports recovery but no automatic rollback occurs. SRC-1, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/wiki/README.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: reviewed page proposal/edit or deferral and residual review work, if followed.
- Later read-back: selected revised prose can be read in later sessions through the wiki index or search.
- Delegated visibility: inapplicable — no independent worker is created by this procedure.
- Selection predicate: explicit trigger sources and affected pages; reuse, sourcing and existing canonical-page comparison.
- Invalidation or expiry: changed source, conflict, due review or supersession reopens reliance.
- Activation or effect: host-mediated claim retention/revision; no actual decision or changed reliance is evidenced here.
- Evidence limits: doctrine requests content-based review but supplies no inspected input/output pair or performed acceptance decision.

Epistemic authority is limited to the evidence and use scope actually reviewed. Behavioral-authority path: host/human consumer, selected page and decision record channel, advisory knowledge force subordinate to canonical project documents, horizon later tasks that retrieve it. Possible transformations include importing observations, condensing sources or proposing a generalization; failure to prove entailment does not prove non-entailment. No individual accepted ampliative proposition is established.

> 2. **Decide promotion**: promote only knowledge that meets `wiki/README.md` promotion criteria.
> 3. **Merge before create**: update an existing related page when the topic already exists; create a new page only for a distinct reusable concept.
> --- `FCVW/skills/wiki-curator/SKILL.md`

> 7. **Review changed sources**: when a tracked `source_digest` changes, inspect only pages linked through `derived_from`; confirm, update, supersede, or invalidate them before refreshing the digest.
> --- `FCVW/skills/wiki-curator/SKILL.md`

#### EPI-RTE-wiki-integrate
Label: Retain and connect reviewed wiki knowledge

Part of: [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission)

Distinct consequential phase from [EPI-RTE-wiki-review](#epi-rte-wiki-review): retention is keeping pages/history; lifecycle integration is connecting reviewed results to canonical/topic/index/supersession links. The host owns file edits and metadata updates. Neither keeping material nor indexing it establishes the prerequisite acceptance. Intended domain is selected reusable project knowledge and its evidence lineage. Sources remain authoritative for their own roles. SRC-1, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/wiki/README.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: retained pages, current index links, metrics/plan record and explicit unresolved gaps.
- Later read-back: future host reads linked canonical pages or searches archived sessions; actual later use unobserved.
- Delegated visibility: inapplicable — the procedure creates no delegated model context.
- Selection predicate: reviewed reusable content; existing canonical page preferred; bounded archive range for old sessions.
- Invalidation or expiry: review dates, obsolete/superseded/contradictory status, replacement links; historical records remain historical.
- Activation or effect: links and active/archive organization are requested to change later selection, not automatically to prove truth.
- Evidence limits: no performed promotion or integration event with authenticated source trace was supplied.

Behavioral-authority path: later host/human via wiki index, typed relationships and on-demand pages, advisory knowledge force, later session horizon. Retention before acceptance, including raw or session content, has a separate ledger function. Rotation preserves evidence rather than claiming its rejection. No universal withdrawal is implemented by these instructions alone.

> 4. **Cluster topics**: link related pages with Obsidian-style links and record canonical pages for superseded or overlapping notes.
> --- `FCVW/skills/wiki-curator/SKILL.md`

> 5. Move old sessions to `wiki/archive/YYYY/`; do not delete audit evidence.
> --- `FCVW/wiki/README.md`

#### EPI-RTE-evidence-check
Label: Deterministic evidence and authority metadata checks

No identical supplied route: this is a distinct check/evidence-production function reached through the validator used by [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks), [RT-RTE-local-checks](runtime.md#rt-rte-local-checks) and [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle). It is not a part of exactly one of those dispatch routes. Python consumes metadata and filesystem existence, emits findings, then main applies optional exact legacy baseline, changed-file filtering and fail-on policy. MCP deliberately uses fail-on never and returns JSON; hook and local driver have their own consequential consumers, not a shared universal rejection gate. SRC-1, `tools/validate_fcvw.py`, `tools/mcp_server_fcvw.py`.

Target/domain: declared evidence-method enum/list shape, references, role/authority compatibility and template/generated retrieval scope. Optional provenance is an important countercase: the validated-method check is guarded by a nonempty method; URLs are accepted without fetching; local `::test` suffixes are removed before existence checking. Therefore it derives reference/metadata consistency, not execution of a test, truth of a URL or entailment of the page. Authority checking does reject an explicit role-incompatible value as a finding; it does not force index building to consume that finding.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: findings, counts and CLI status under selected fail-on policy, or MCP JSON report.
- Later read-back: later validator invocations load persisted wiki frontmatter and pass evidence_method, status and verified_by metadata into check_evidence. This consumes retained provenance/status assertions, not claim-body delivery or semantic acceptance. The checker need not author those fields; caller retention of its output reports is separate, and actual later reliance is unobserved.
- Delegated visibility: inapplicable — no model worker or delegated evidence review is launched.
- Selection predicate: validator main dispatch, wiki schema checks and metadata presence; baseline and since can alter emitted blockers.
- Invalidation or expiry: findings describe inspected filesystem state and chosen profile; edits require a new check.
- Activation or effect: deterministic findings can block default CLI success; host/MCP/hook interpretation determines later action.
- Evidence limits: no semantic evidence reading, mandatory provenance method for every page, observed invocation or acceptance decision is established.

Behavioral-authority path: CLI caller through status/findings (enforcing only command success), MCP host through JSON (advisory), and configured hook through selected attributed errors (conditional repair request); horizon current check/closeout. No epistemic license beyond checked metadata/reference predicates. Supplied runtime authority concern is qualified, not superseded: it already identifies validator/review as a separate consumer.

> if method and scalar(metadata, "status") == "validated":
>     if method == "ai_inference":
>         findings.append(Finding("wiki-schema", relative, "ai_inference alone cannot validate a claim"))
>     elif not verified:
>         findings.append(Finding("wiki-schema", relative, "validated claim requires verified_by evidence"))
> --- `tools/validate_fcvw.py`

> for reference in verified:
>     if re.match(r"^https?://", reference, re.I):
>         continue
> --- `tools/validate_fcvw.py`

> target = reference.split("::", 1)[0].split("#", 1)[0]
> --- `tools/validate_fcvw.py`

> if authority and expected_authority and authority != expected_authority:
>     findings.append(
>         Finding(
>             "frontmatter-retrieval",
>             relative,
>             f"{role} artifacts cannot elevate or change authority from {expected_authority}",
>         )
>     )
> --- `tools/validate_fcvw.py`

>         metadata = frontmatter_of(path)
>         page_id = scalar(metadata, "id")
> --- `tools/validate_fcvw.py`

>             check_evidence(root, path, metadata, findings)
> --- `tools/validate_fcvw.py`

> if args.fail_on == "never":
>     return 0
> --- `tools/validate_fcvw.py`

#### EPI-RTE-source-review
Label: Source digest and direct-dependent review findings

Distinct from supplied context delivery and MCP wrapper routes: this computes an evidence condition, not semantic acceptance or a file read API alone. Python resolves a tracked file or selected Markdown section, hashes its bytes, compares a well-formed stored digest, then graph construction marks direct explicit derived_from dependents for review. Review-date checks use the current date. Main validator consumes graph findings; MCP digest returns only path/digest. Owner is Python for calculation and host for the subsequent review in [EPI-RTE-wiki-review](#epi-rte-wiki-review). SRC-1, `tools/knowledge_sources_fcvw.py`, `tools/knowledge_graph_fcvw.py`, `tools/validate_fcvw.py`, `tools/mcp_server_fcvw.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: digest, stale-source warning, direct-dependent review warning or overdue-review warning, depending on entry point.
- Later read-back: later graph/check invocations load persisted wiki source_path/source_digest, derived_from relations and next_review metadata. Python compares the retained digest with current source bytes, resolves dependent relations and checks due dates to emit review findings. This is retained metadata consumption, not claim-body delivery, report adoption or semantic acceptance; the checker need not write the inputs, and actual later reliance is unobserved.
- Delegated visibility: inapplicable — no delegated model consumer.
- Selection predicate: source_path and optional anchor, valid recorded digest; explicit non-derived derived_from edge to a stale source; optional next_review.
- Invalidation or expiry: recomputation follows bytes/date, not semantic change; missing/invalid provenance yields a different finding or no stale comparison.
- Activation or effect: review candidates can influence a host; default error-only CLI does not fail solely on these warning-severity findings.
- Evidence limits: no transitive semantic invalidation, endorsement, automatic status rewrite or performed source review follows from mismatch.

Epistemic authority: bytes or normalized selected-section equality/difference and declared graph dependency, not factual truth. Behavioral-authority path: host/reviewer via report, advisory review force until a reviewer acts, current review horizon. Concrete implementation deduction, not target execution: for a valid tracked source with actual digest differing from stored digest, `validate_source_page` returns True plus a warning; a non-derived edge whose target is in stale_sources produces a warning on its source_path. This licenses a review request only.

>         metadata = cache_frontmatter(path)
>         if metadata:
>             records.append((path, metadata))
> --- `tools/knowledge_graph_fcvw.py`

>         source_stale, source_findings = validate_source_page(root, path, metadata)
> --- `tools/knowledge_graph_fcvw.py`

> if actual == source_digest:
>     return False, findings
> --- `tools/knowledge_sources_fcvw.py`

> "knowledge-source-stale",
> relative,
> f"tracked source digest changed: expected {source_digest}, actual {actual}",
> "warning",
> --- `tools/knowledge_sources_fcvw.py`

> if edge["derived"] or edge["relation"] != "derived_from":
>     continue
> --- `tools/knowledge_sources_fcvw.py`

> "knowledge-review-candidate",
> str(edge["source_path"]),
> f"derived knowledge requires review because source changed: {target_path}",
> "warning",
> --- `tools/knowledge_sources_fcvw.py`

#### EPI-RTE-live-qa
Label: Live QA observation against sourced expectations

No supplied route describes live product testing; [RT-RTE-local-checks](runtime.md#rt-rte-local-checks) concerns framework verification, not this host-run application route. The host reads selected requirements/contracts, discovers the authorized target, proposes cases and records live observations. Expected behavior requires an approved requirement, acceptance criterion, design decision or owner confirmation; unknown/provisional intent blocks passing assertions. Execution environment, tool/hardware, revision and roles bound the comparison. Model inference may help propose descriptions; it is not an answer oracle. Oracle: approved scoped expectation, with application observations as test evidence. The user controls permitted scope/actions and divergence direction. Operating mode: scoped initial mapping followed by affected-case regression, not a universal curriculum. SRC-1, `FCVW/skills/QA/SKILL.md`, `FCVW/skills/QA/PRODUCT_WIKI.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: bounded discovery checkpoint or selected case observations and dated QA run, if followed.
- Later read-back: later sessions read recent exact runs and affected surface pages; previous failures must remain.
- Delegated visibility: inapplicable — QA describes a host invocation, not an independent worker allocator.
- Selection predicate: authorized QA/product-wiki request, available target tools/roles, selected cases and relevant data/state classes.
- Invalidation or expiry: changed behavior contract or requirements require review and affected-case rerun; old runs remain historical.
- Activation or effect: requested comparison produces evidence and updates observation/confidence fields; divergence hands control to user decision.
- Evidence limits: source inspection here neither visits an application nor establishes any actual test pass or approval.

Acquisition/import is the route by which external observations enter the record; source warrant is unknown without the actual target trace. Testing licenses only an observed result for the named case/environment if it happened; not intended behavior inferred from implementation, causal explanation or transfer. Behavioral-authority path: host/human reads product page and exact QA run, advisory factual evidence plus requested test-completion criteria, current QA and later affected runs. Recovery/checkpoint preserves unresolved intent, failures and frontier rather than silently retrying to pass.

> Unknown/provisional expectations cannot produce a passing assertion.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

> A discrepancy is a defect or an unresolved requirement; never rewrite expected behavior merely to make a failing test pass.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

#### EPI-RTE-qa-check
Label: Selected product QA contract and run checker

Distinct from [EPI-RTE-live-qa](#epi-rte-live-qa) (which requests actual interaction) and [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks) (which does not register this tool). Python parses selected Markdown tables, hashes a contract dict, checks inventory/contract/run consistency, then computes result counts, missing cases and consultation metrics. Owner is Python; evaluator domain is the declared tables, not the application or conversation. A failed case missing a divergence row still becomes pending. Approved expectation is a string classification with meaningful source text, not authenticated approval. Check and CLI disposition are separate ledger functions of the same implementation. SRC-1, `tools/qa_wiki_fcvw.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: report or structural error; with run, CLI returns nonzero unless execution_status is pass and decision gate is not blocked.
- Later read-back: optional output retains a report for a caller; no automatic future policy/knowledge write follows.
- Delegated visibility: inapplicable — no delegated execution or host conversation API is used.
- Selection predicate: explicit surfaces or mapped inventory entries, optional run; exact expected case keys and contract hashes.
- Invalidation or expiry: differing current selected contract hash rejects run reuse; this does not measure unencoded behavior changes.
- Activation or effect: structural errors abort; declared failures/blocked/missing/not-run and pending decisions prevent successful run-check exit.
- Evidence limits: a fabricated pass/evidence reference can satisfy declared fields; checker explicitly disclaims proof of live execution, truth, consent and hidden completeness.

Epistemic authority is derived consistency of the selected representation. Behavioral-authority path: invoking host/local automation through JSON and exit status, command-success enforcement plus advisory findings, current selected run only. The doctrine's human veto is not implemented as a trusted conversation event check. A decision can clear the decision gate while execution_status remains fail.

Concrete static trace: suppose one selected approved case has a matching contract hash, a declared fail observation/evidence, and no Divergences row. The failed-case union includes it, default decision is pending, pending_decisions becomes one, user_decision_gate becomes blocked, execution_status is fail and main returns 1. Adding a well-formed defer decision can clear pending but does not change the failed result or exit 1. This is an implementation deduction, not an executed test.

> keys = {key for key, row in results.items() if row['result'] == 'fail'} | decisions.keys()
> --- `tools/qa_wiki_fcvw.py`

> 'consultation_provenance': 'declared_only' if run else 'not_evaluated',
> --- `tools/qa_wiki_fcvw.py`

> return int(bool(args.run) and (report['execution_status'] != 'pass' or report['user_decision_gate'] == 'blocked'))
> --- `tools/qa_wiki_fcvw.py`

#### EPI-RTE-divergence-decision
Label: User direction after expected-actual divergence


Distinct from general wiki review and [RT-RTE-governed-change](runtime.md#rt-rte-governed-change): this is a mandatory per-divergence user choice rather than generic session authorization. Host proposes fix, expectation revision, investigation or deferral and must ask the user; the human decides/vetoes, no answer oracle is invented. Scope is the affected case and dependent next action. An approved expectation change must enter the authoritative source and new contract/test; it does not erase historical failure. Operating mode: evidence-triggered QA continuation. SRC-1, `FCVW/skills/QA/SKILL.md`, `FCVW/skills/QA/PRODUCT_WIKI.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: question and explicit direction or pending/blocked checkpoint.
- Later read-back: dated question/response references and preserved original run support later handoff; actual conversation authenticity is not checked here.
- Delegated visibility: inapplicable — no independent worker context.
- Selection predicate: every expected/observed divergence including provisional-intent mismatches; missing access alone is not a divergence.
- Invalidation or expiry: an exact existing answer may be reused; a new or materially changed divergence requires a new question.
- Activation or effect: pending answer blocks dependent action/completion by instruction; independent tests may continue.
- Evidence limits: checker sees declared references only; no trusted host event corroboration or performed approval supplied.

Epistemic scope: human approval can specify product intent; it is not evidence that observed execution succeeded. Behavioral-authority path: host executor, user response/decision row channel, permissive direction and blocking pending-answer policy, current affected action and later handoff. Proposed code repairs are external products, not automatic self-improvement of FCVW.

> Silence and suggested answers remain pending.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

> A clear decision gate does not make a failed test pass.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

#### EPI-RTE-retrieval-benchmark
Label: Labeled routing and retrieval evaluation

Part of: [RT-RTE-local-checks](runtime.md#rt-rte-local-checks)

This is the labeled retrieval check invoked by the local driver; its separate CLI also permits synthetic or paired external case/index inputs. Python computes mandatory recall, optional precision/useful recall, forbidden hits, estimated serialized-result cost and bounded retrieval/selection timing. Targets are label agreement and optional-selection regressions on these corpora. Expected-answer provider is the authored synthetic labels or external caller, not retrieval's own returned result. It does not execute an agent model. Missing task outcomes are null; caller outcome labels are aggregated separately. Check policy admits CLI success or nonzero, not knowledge acceptance. SRC-1, `tools/benchmark_retrieval_fcvw.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: benchmark JSON/report; with check, nonzero for required misses/missing paths, forbidden hits or lower selected than baseline useful recall.
- Later read-back: report can be retained for review; no automated policy/parameter update consumes it in this implementation.
- Delegated visibility: inapplicable — repeats run deterministic retrieval/selection, not delegated agents.
- Selection predicate: synthetic cases by default or supplied paired index/cases; useful labels must resolve and not overlap forbidden labels.
- Invalidation or expiry: report input_digest binds serialized records/cases; corpus, date, budget and repeats bound comparison.
- Activation or effect: local driver consumes status; caller may use evidence for maintenance but benchmark does not patch or publish anything.
- Evidence limits: baseline versus selection is one local comparison, not independent interventions on each ranking component or measured downstream model benefit.

Behavioral-authority path: local checker/caller via report and optional CLI failure, enforcing local step success when check requested, present verification horizon. Its entailments are arithmetic over supplied labels, not claims that arbitrary returned prose is true. No proposal/rollback loop is implemented here; failures report rather than revise.

> baseline, selected = candidates[:8], selection["results"]
> --- `tools/benchmark_retrieval_fcvw.py`

> failed = any(r["mandatory_recall"] < 1 or r["mandatory_missing"] or r["selected"]["forbidden_hits"]
>              or r["baseline"]["forbidden_hits"]
>              or r["selected"]["useful_recall"] < r["baseline"]["useful_recall"] for r in result["cases"])
> return int(args.check and failed)
> --- `tools/benchmark_retrieval_fcvw.py`

### Claims

#### EPI-CLM-sourced-knowledge
Label: Sourced reusable wiki knowledge

FCVW claims reusable sourced knowledge, independent evidence for validation, and selective reconsideration on source change. This is a doctrine/design claim, not a supplied observed acceptance event. Closest supplied claim [RT-CLM-context-controls](runtime.md#rt-clm-context-controls) concerns routing/authority, not semantic wiki admission. SRC-1, `FCVW/wiki/README.md`.

> Keep inferred and verified knowledge apart: a `validated` page that declares a method must cite resolvable `verified_by` evidence, and `ai_inference` alone never validates. Retrieval labels `ai_inference` results as unverified.
> --- `FCVW/wiki/README.md`

> Review confirms, updates, supersedes, or invalidates the knowledge and only then refreshes the stored digest and review dates.
> --- `FCVW/wiki/README.md`

#### EPI-CLM-product-evidence
Label: Scoped product expectation and observation evidence

FCVW claims a sourced expectation/actual-behavior separation with mandatory divergence consultation and contract-bound selected-case checking. It expressly disclaims checker attestation of live execution. Distinct from [RT-CLM-context-controls](runtime.md#rt-clm-context-controls); no supplied QA-specific claim. SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`.

> The first command validates structure and returns contract hashes without claiming execution.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

> The checker neither opens the application nor proves evidence truth or completeness of unobserved behavior.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

### Additional implementation passages for supplied routes

These passages add epistemic interpretation without duplicating runtime records. SRC-1, `tools/build_context_index.py`: for the concrete input `## Claim\n\nThe cache is disposable.\n`, sections produces heading Claim and content containing that heading and sentence; bounded_chunks recombines those short blocks without adding a proposition. build_index stores that content with its path and digest. The non-ampliative classification is for this deterministic packaging, not an assurance that every later excerpt retains every condition. No target execution is needed for this deduction.

> return [(title, "\n".join(body).strip()) for title, body in chunks]
> --- `tools/build_context_index.py`

> "chunk_hash": f"sha256:{digest}",
> "content_hash": f"sha256:{digest}",
> "content": content,
> --- `tools/build_context_index.py`

For [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), withdrawal differs from ranking: disputed/obsolete content is downweighted, not rejected by status. The lexical ai_inference branch adds a warning reason; graph additions use their own reason list, so this does not establish that every graph-returned inferred chunk carries the same explicit warning. Neither path evaluates factual truth. Source warrant after excerpt omission is unknown where a condition lies outside the returned slice. SRC-1, `tools/retrieve_context.py`.

> if status in {"obsolete", "superseded", "contradictory", "archived"}:
>     score *= 0.35
> --- `tools/retrieve_context.py`

> if record.get("evidence_method") == "ai_inference":
>     reasons.append("unverified: ai_inference")
> --- `tools/retrieve_context.py`

> graph_reasons = [
>     f"graph:{relation}",
>     f"from={source_path}",
>     "bounded-one-hop",
>     f"priority={target.get('retrieval_priority', 'normal')}",
> ]
> --- `tools/retrieve_context.py`

