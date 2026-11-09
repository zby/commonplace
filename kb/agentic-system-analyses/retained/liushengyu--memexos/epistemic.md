---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MemexOS epistemic routes: source faithfulness, publication authority, catalog metadata, feedback and bounded evaluation."
run-id: AAS-2026-11-07-memexos-5cd34a715eb7-01
reviewed-boundary: bb9e9b2ac0adbca87d13a9f7600867128b5f71b9
---

# MemexOS epistemic report

## Source-and-claim boundary

This report asks which contents MemexOS acquires, transforms, checks, admits and makes available for later reliance, and what those checks license. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Source identity and layers: see the [Source register](boundary.md#source-register). All added reads use SRC-1 at the frozen revision. Implementation establishes wiring, not exercised model compliance. No target was executed. No production trace, independently warranted input/output pair or causal intervention is supplied.

The main distinction is between checking faithfulness to retained sources and checking whether those sources are true. The rubric explicitly excludes the latter: see [EPI-RTE-review-claims](#epi-rte-review-claims). Publication is conditional and can admit honestly marked speculation: see [EPI-RTE-review-decision](#epi-rte-review-decision). Source classification also changes later evidence-strength guidance without establishing the correctness of that guidance: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission) and [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).

Consequential claims: see [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication), [RT-CLM-schema-change](runtime.md#rt-clm-schema-change), [EPI-CLM-reviewed-memory](#epi-clm-reviewed-memory) and [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). No supplied record requires supersession. Newly inspected catalog synchronization adds a forcing publication path, rather than replacing the supplied compile route's identity.

### Coverage

“Direct” means source text inspected for this report; “supplied” means the runtime/boundary finding, not an independent reread. Available but uninspected operations remain inside the functional boundary. Their presence prevents a system-complete negative about knowledge production, checking or adaptation.

| Entry point or operation | SRC-1 path | Coverage or limit |
|---|---|---|
| CLI dispatch and evaluation trace/stub hook | `src/memexos/cli.py` | Direct complete command map and dispatch; [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring). |
| ingest writer, rework, gate and publish continuation | `src/memexos/pipeline/compile.py` | Direct review_loop, classifications and ingest_batch; supplied broader maintenance paths: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish). |
| Gate 1 | `src/memexos/pipeline/gate1.py` | Direct complete implementation; [EPI-RTE-gate1-check](#epi-rte-gate1-check). |
| self-check and support question | `src/memexos/pipeline/selfcheck.py`, `src/memexos/judge.py` | Direct self-check and support instruction; [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check). Hosted judge calibration uninspected. |
| semantic review and feedback rendering | `src/memexos/pipeline/gate2.py`, `src/memexos/pipeline/report.py`, `src/memexos/prompts/en/gate2_rubric.md` | Direct complete files; [EPI-RTE-review-claims](#epi-rte-review-claims), [EPI-RTE-review-decision](#epi-rte-review-decision). |
| catalog classify, category screen, effective metadata, sync | `src/memexos/catalog/classify.py`, `src/memexos/catalog/taxonomy.py` | Direct run_batch/settle/classify, screen, primary_raw/writer_set/effective/set_frontmatter/sync/catalog_sync; [EPI-RTE-catalog-screen](#epi-rte-catalog-screen), [EPI-RTE-catalog-admission](#epi-rte-catalog-admission), [EPI-RTE-catalog-sync](#epi-rte-catalog-sync). Full taxonomy registry, domain decisions and reassignment internals not audited; category correctness and complete category lifecycle remain unresolved. |
| usage judgment, feedback verification and fix-job conversion | `src/memexos/usage.py`, `src/memexos/prompts/en/usage_verify.md` | Direct judgment/verify/to_fix_job and ordinary verify prompt; [EPI-RTE-usage-judgment](#epi-rte-usage-judgment), [EPI-RTE-feedback-check](#epi-rte-feedback-check). Event extraction and alternate source-error prompt not inspected in depth; no complete trace-provenance or alternate-verification equivalence conclusion. |
| lint/fix/correct/inbox decisions and application | `src/memexos/pipeline/compile.py`, `src/memexos/inbox.py` | Supplied [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance). Direct report-to-writer filtering adds coverage of what feedback survives. Detailed inbox research/triage prompts uninspected; no complete research acceptance finding. |
| search/get/reindex/models | `src/memexos/search/cli.py`, `src/memexos/search/engine.py`, `src/memexos/search/rerank.py` | Supplied [RT-RTE-search-get](runtime.md#rt-rte-search-get) and [RT-CMP-qmd](runtime.md#rt-cmp-qmd); no claim that relevance ranking verifies truth. |
| evaluation dispatch, retrieval bank verification and L1/L2 | `src/memexos/evals/__init__.py`, `src/memexos/evals/retrieval.py` | Direct suite dispatch and verify/L1 score/grade functions; [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank), [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring), [EPI-RTE-answer-grading](#epi-rte-answer-grading). Generation/mining and qrel pool not fully inspected; reference independence is not established. |
| review calibration and tool-use evaluator | `src/memexos/evals/gate2.py`, `src/memexos/evals/tooluse.py` | Direct run_case/caught and score; [EPI-RTE-review-calibration](#epi-rte-review-calibration), [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring). Shipped sample results not adopted; no score or observed benefit conclusion. |
| fetch/add-url/add-video/add-visual, sessions/intake | `src/memexos/capture/`, `src/memexos/intake/` | Supplied [RT-RTE-source-admission](runtime.md#rt-rte-source-admission). Detailed extraction, ASR and vision transformations remain uninspected, including opaque providers. Source warrant on these acquisition paths is unknown, not presumed preserved by storage. |
| backend tools and plugins | `src/memexos/backends/`, `src/memexos/plugins/__init__.py` | Supplied [RT-RTE-backend-execution](runtime.md#rt-rte-backend-execution), [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading), including alternate fetch dispatch and policy limits. External tools/provider internals excluded. No uniform enforcement or absence-of-external-evidence claim. |
| nightly/schedule/console, pause/resume | `src/memexos/schedule.py`, `src/memexos/console/actions.py`, `src/memexos/cli.py` | Supplied runtime coordination; direct CLI dispatch. These launch or stop existing work; completion events are not semantic acceptance. |
| init/setup/config/doctor/help/status, secret/cookies/login | `src/memexos/cli.py` | Direct dispatch, supplied scaffold account; detailed setup/help/credential bodies uninspected. No source-truth evaluator inferred from operational diagnostics. |
| vault doctrine, public claims, localized assets | `src/memexos/templates/vault/en/AGENTS.md`, `README.md` | Direct English rules and README claim passages. Chinese prompts, sample vault, test assertions, developer tooling and illustrative images not assessed as semantic outcomes; no translation-equivalence, test-pass or longitudinal result. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-wiki](#epi-obj-wiki) | see record | see record | SRC-1, `src/memexos/templates/vault/en/AGENTS.md` | see record |
| [EPI-OBJ-catalog](#epi-obj-catalog) | see record | see record | SRC-1, `src/memexos/catalog/classify.py` | see record |
| [EPI-OBJ-review](#epi-obj-review) | see record | see record | SRC-1, `src/memexos/pipeline/gate2.py` | see record |
| [EPI-OBJ-evaluation](#epi-obj-evaluation) | see record | see record | SRC-1, `src/memexos/evals/retrieval.py` | see record |
| [EPI-OBJ-questions](#epi-obj-questions) | see record | see record | see [EPI-OBJ-questions](#epi-obj-questions) | see record |
| [EPI-OBJ-rank-results](#epi-obj-rank-results) | see record | see record | see [EPI-OBJ-rank-results](#epi-obj-rank-results) | see record |
| [EPI-OBJ-answer-judgments](#epi-obj-answer-judgments) | see record | see record | see [EPI-OBJ-answer-judgments](#epi-obj-answer-judgments) | see record |
| [EPI-OBJ-calibration-cases](#epi-obj-calibration-cases) | see record | see record | see [EPI-OBJ-calibration-cases](#epi-obj-calibration-cases) | see record |
| [EPI-OBJ-calibration-results](#epi-obj-calibration-results) | see record | see record | see [EPI-OBJ-calibration-results](#epi-obj-calibration-results) | see record |
| [EPI-OBJ-cli-traces](#epi-obj-cli-traces) | see record | see record | see [EPI-OBJ-cli-traces](#epi-obj-cli-traces) | see record |
| [EPI-OBJ-tool-metrics](#epi-obj-tool-metrics) | see record | see record | see [EPI-OBJ-tool-metrics](#epi-obj-tool-metrics) | see record |
| [RT-OBJ-policy](runtime.md#rt-obj-policy) | none: capability policy | see record | SRC-1, `src/memexos/backends/base.py` | see record |

The raw-source and candidate intake objects are covered by [RT-RTE-source-admission](runtime.md#rt-rte-source-admission), but their complete extracted propositions are not individuated here. Model parameter state is separate from text and symbolic records: see [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code), [RT-CMP-codex](runtime.md#rt-cmp-codex), [RT-CMP-anthropic-api](runtime.md#rt-cmp-anthropic-api), [RT-CMP-openai-compatible](runtime.md#rt-cmp-openai-compatible), [RT-CMP-jev](runtime.md#rt-cmp-jev) and [RT-CMP-qmd](runtime.md#rt-cmp-qmd). No inspected weight-training route follows from wiki updates; provider state remains opaque.

## Authority-route ledger

Route ID: [EPI-RTE-writer-transform](#epi-rte-writer-transform)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Content/update relation: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Transition or check target: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Evaluator/condition and domain: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Activation and timing: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Possible or observed result: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Implemented force: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Epistemic authority and scope: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Evidence source ID and local anchor: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Claim IDs or none: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Mismatch marker or none: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).
Gap/limit: see [EPI-RTE-writer-transform](#epi-rte-writer-transform).

Route ID: [EPI-RTE-gate1-check](#epi-rte-gate1-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Content/update relation: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Transition or check target: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Evaluator/condition and domain: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Activation and timing: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Possible or observed result: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Implemented force: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Epistemic authority and scope: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Evidence source ID and local anchor: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Claim IDs or none: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Mismatch marker or none: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).
Gap/limit: see [EPI-RTE-gate1-check](#epi-rte-gate1-check).

Route ID: [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Content/update relation: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Transition or check target: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Evaluator/condition and domain: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Activation and timing: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Possible or observed result: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Implemented force: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Epistemic authority and scope: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Evidence source ID and local anchor: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Claim IDs or none: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Mismatch marker or none: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).
Gap/limit: see [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).

Route ID: [EPI-RTE-review-claims](#epi-rte-review-claims)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Content/update relation: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Transition or check target: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Evaluator/condition and domain: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Activation and timing: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Possible or observed result: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Implemented force: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Epistemic authority and scope: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Evidence source ID and local anchor: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Claim IDs or none: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Mismatch marker or none: see [EPI-RTE-review-claims](#epi-rte-review-claims).
Gap/limit: see [EPI-RTE-review-claims](#epi-rte-review-claims).

Route ID: [EPI-RTE-review-decision](#epi-rte-review-decision)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Content/update relation: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Transition or check target: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Evaluator/condition and domain: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Activation and timing: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Possible or observed result: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Implemented force: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Epistemic authority and scope: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Evidence source ID and local anchor: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Claim IDs or none: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Mismatch marker or none: see [EPI-RTE-review-decision](#epi-rte-review-decision).
Gap/limit: see [EPI-RTE-review-decision](#epi-rte-review-decision).

Route ID: [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Content/update relation: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Transition or check target: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Evaluator/condition and domain: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Activation and timing: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Possible or observed result: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Implemented force: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Epistemic authority and scope: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Evidence source ID and local anchor: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Claim IDs or none: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Mismatch marker or none: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).
Gap/limit: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention).

Route ID: [EPI-RTE-catalog-screen](#epi-rte-catalog-screen)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Content/update relation: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Transition or check target: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Evaluator/condition and domain: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Activation and timing: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Possible or observed result: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Implemented force: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Epistemic authority and scope: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Evidence source ID and local anchor: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Claim IDs or none: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Mismatch marker or none: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).
Gap/limit: see [EPI-RTE-catalog-screen](#epi-rte-catalog-screen).

Route ID: [EPI-RTE-catalog-admission](#epi-rte-catalog-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Content/update relation: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Transition or check target: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Evaluator/condition and domain: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Activation and timing: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Possible or observed result: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Implemented force: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Epistemic authority and scope: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Evidence source ID and local anchor: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Claim IDs or none: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Mismatch marker or none: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).
Gap/limit: see [EPI-RTE-catalog-admission](#epi-rte-catalog-admission).

Route ID: [EPI-RTE-catalog-sync](#epi-rte-catalog-sync)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Content/update relation: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Transition or check target: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Evaluator/condition and domain: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Activation and timing: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Possible or observed result: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Implemented force: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Epistemic authority and scope: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Evidence source ID and local anchor: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Claim IDs or none: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Mismatch marker or none: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).
Gap/limit: see [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).

Route ID: [EPI-RTE-usage-judgment](#epi-rte-usage-judgment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Content/update relation: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Transition or check target: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Evaluator/condition and domain: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Activation and timing: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Possible or observed result: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Implemented force: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Epistemic authority and scope: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Evidence source ID and local anchor: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Claim IDs or none: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Mismatch marker or none: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).
Gap/limit: see [EPI-RTE-usage-judgment](#epi-rte-usage-judgment).

Route ID: [EPI-RTE-feedback-check](#epi-rte-feedback-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Content/update relation: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Transition or check target: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Evaluator/condition and domain: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Activation and timing: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Possible or observed result: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Implemented force: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Epistemic authority and scope: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Evidence source ID and local anchor: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Claim IDs or none: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Mismatch marker or none: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).
Gap/limit: see [EPI-RTE-feedback-check](#epi-rte-feedback-check).

Route ID: [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Content/update relation: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Transition or check target: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Evaluator/condition and domain: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Activation and timing: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Possible or observed result: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Implemented force: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Epistemic authority and scope: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Evidence source ID and local anchor: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Claim IDs or none: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Mismatch marker or none: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).
Gap/limit: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank).

Route ID: [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Content/update relation: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Transition or check target: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Evaluator/condition and domain: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Activation and timing: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Possible or observed result: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Implemented force: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Epistemic authority and scope: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Evidence source ID and local anchor: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Claim IDs or none: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Mismatch marker or none: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).
Gap/limit: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).

Route ID: [EPI-RTE-answer-grading](#epi-rte-answer-grading)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Content/update relation: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Transition or check target: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Evaluator/condition and domain: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Activation and timing: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Possible or observed result: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Implemented force: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Epistemic authority and scope: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Evidence source ID and local anchor: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Claim IDs or none: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Mismatch marker or none: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).
Gap/limit: see [EPI-RTE-answer-grading](#epi-rte-answer-grading).

Route ID: [EPI-RTE-review-calibration](#epi-rte-review-calibration)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Content/update relation: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Transition or check target: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Evaluator/condition and domain: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Activation and timing: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Possible or observed result: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Implemented force: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Epistemic authority and scope: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Evidence source ID and local anchor: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Claim IDs or none: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Mismatch marker or none: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).
Gap/limit: see [EPI-RTE-review-calibration](#epi-rte-review-calibration).

Route ID: [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Content/update relation: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Transition or check target: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Evaluator/condition and domain: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Activation and timing: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Possible or observed result: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Implemented force: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Epistemic authority and scope: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Evidence source ID and local anchor: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Claim IDs or none: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Mismatch marker or none: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).
Gap/limit: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication) | see record | see record | see record | [EPI-RTE-review-decision](#epi-rte-review-decision), [EPI-RTE-catalog-sync](#epi-rte-catalog-sync) | none supplied | no experiment | see route records | see route records |
| [EPI-CLM-reviewed-memory](#epi-clm-reviewed-memory) | see record | see record | see record | [EPI-RTE-writer-transform](#epi-rte-writer-transform), [EPI-RTE-review-claims](#epi-rte-review-claims), [RT-RTE-search-get](runtime.md#rt-rte-search-get) | none adopted | no experiment | see record | see record |
| [EPI-CLM-evolves-itself](#epi-clm-evolves-itself) | see record | see record | see record | [EPI-RTE-usage-judgment](#epi-rte-usage-judgment), [EPI-RTE-feedback-check](#epi-rte-feedback-check), [EPI-RTE-catalog-admission](#epi-rte-catalog-admission) | none supplied | no longitudinal intervention | see record | see record |
| [RT-CLM-schema-change](runtime.md#rt-clm-schema-change) | see record | see record | see record | [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance) | none supplied | no experiment | see record | see record |

## Bounded conclusion

MemexOS implements source acquisition/admission, model compilation, source-relative checking, conditional batch acceptance and persistent retrieval. See [RT-RTE-source-admission](runtime.md#rt-rte-source-admission), [EPI-RTE-writer-transform](#epi-rte-writer-transform), [EPI-RTE-review-claims](#epi-rte-review-claims), [EPI-RTE-review-decision](#epi-rte-review-decision), [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) and [RT-RTE-search-get](runtime.md#rt-rte-search-get). Imported source warrant is unknown on uninspected extraction paths. Source citations and classification preserve or expose intended lineage but do not independently authenticate original claims.

The material acceptance criterion is changed-batch source faithfulness and coverage under the model-produced review inventory, for publication into this vault. Its consumer is the compiler's continuation branch, its channel is a structured review and program-derived status, and its force is enforcing only on enabled covered paths. See [EPI-RTE-review-decision](#epi-rte-review-decision) and [RT-BAP-review-verdicts](runtime.md#rt-bap-review-verdicts). This accepts some text as honestly marked uncertainty, not as established truth. Gate 1 establishes structural properties, and self-check requests additional verification; neither supplies a truth oracle. See [EPI-RTE-gate1-check](#epi-rte-gate1-check) and [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check).

Retention and subsequent use must not be collapsed into acceptance or lifecycle integration. Publication makes draft text and its prepared links live. A separate post-acceptance semantic integration judgment is not established by the inspected compile path. Retrieval supplies informational text to a later caller; compliance and changed answers are unobserved. See [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) and [RT-BAP-retrieved-pages](runtime.md#rt-bap-retrieved-pages).

Catalog metadata receives organizing and evidence-guidance authority through classification and synchronization, including a Gate-1-only publication route. This is a material exception to any universal review reading. See [EPI-RTE-catalog-screen](#epi-rte-catalog-screen), [EPI-RTE-catalog-admission](#epi-rte-catalog-admission) and [EPI-RTE-catalog-sync](#epi-rte-catalog-sync). It does not negate the separate conditional compiler gate.

Feedback provides an implemented criticism-to-repair path, not demonstrated improvement. See [EPI-RTE-usage-judgment](#epi-rte-usage-judgment), [EPI-RTE-feedback-check](#epi-rte-feedback-check) and [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance). Evaluation references, rank scores, answer grading, reviewer calibration and tool-use matching license different local conclusions; no one score establishes knowledge quality. See [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank), [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring), [EPI-RTE-answer-grading](#epi-rte-answer-grading), [EPI-RTE-review-calibration](#epi-rte-review-calibration) and [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring).

No concrete writer-produced accepted ampliative proposition or warranted-premise derivation is individuated from the supplied evidence. Deterministic rank/seed computations do support bounded mathematical derivations from their inputs, not source truth. This is a finding about available evidence, not absence of conjecturing, learning or reasoning. The public evolution claim receives a separate bounded assessment in [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Uninspected relevant capture, research and taxonomy branches prevent a system-complete negative.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-wiki
Label: Wiki content

Source-native identity: wiki Markdown pages, index entries and their citations, in staging and after publication. Form: natural-language claims/summaries/inferences plus symbolic paths, frontmatter and wikilinks. Substrate: filesystem and Git. Truth-apt content includes source summaries, entity/concept/topic claims and evidence-strength descriptions; marked speculation remains truth-apt but not accepted as true merely by marking. Producers: writer/maintenance agents and metadata sync. Consumers: reviewer, later writers, search/get and external readers. Distinct from [RT-OBJ-stage](runtime.md#rt-obj-stage): that record is the isolated organizational workspace, whereas this identity follows content across draft and published revisions. A stage contains a draft instance, not this entire cross-revision object. No actual user-vault proposition is supplied. Evidence: SRC-1, `src/memexos/templates/vault/en/AGENTS.md`.

> Each page: a one-sentence definition → the body → a **Sources** section listing the `raw/` files or external links that support it
> --- `src/memexos/templates/vault/en/AGENTS.md`

#### EPI-OBJ-catalog
Label: Source catalog

Source-native identity: `.memex/catalog.jsonl` rows and effective source-page classification. Form: symbolic category/evidence/type/usage/durability labels plus natural-language scope_note/summary. Substrate: append-only JSONL and Markdown frontmatter. Claims concern a source's domain, evidential character and suitable use; registry identifiers are organizational rather than truth claims on their own. Producers: screen, classification worker, registry/settle code and writer overrides. Consumers: compile prompt, sync and downstream page/search metadata. Distinct from [RT-RTE-source-admission](runtime.md#rt-rte-source-admission): it characterizes admitted raw content, not keep/drop of offered intake items. Label correctness is unobserved. Evidence: SRC-1, `src/memexos/catalog/classify.py`; load-bearing implementation passages in [EPI-RTE-catalog-admission](#epi-rte-catalog-admission) and [EPI-RTE-catalog-sync](#epi-rte-catalog-sync).

#### EPI-OBJ-review
Label: Review and feedback judgments

Source-native identity: review.json/report.json and usage judgment/feedback-status records. Form: symbolic verdicts, criticality, covered/admission flags and status, with natural-language challenged claims, evidence, locations and reasons. Substrate: JSON/JSONL and rendered Markdown. Split consumers: program threshold admission, model rework, later fix, and operational summaries. These paths are separately assessed below because the same text can be advisory to a writer but enforcing through a gate. Distinct from [RT-OBJ-stage](runtime.md#rt-obj-stage) and its files: review evidence can persist outside the stage and outlive discarded drafts. No observed correct judgment instance is assumed. Evidence: SRC-1, `src/memexos/pipeline/gate2.py`, `src/memexos/usage.py`; supporting passages below.

#### EPI-OBJ-evaluation
Label: Evaluation references and results

Source-native identity: retrieval question bank/gold_pages/key_facts/qrels, L1/L2 results, calibration cases and tool-use trace metrics. Form: natural-language questions/reference facts/answers and symbolic paths, judgments, seeds, CLI argument lists and numerical metrics. Substrate: JSON/JSONL and reports. The parts have distinct evaluators and consumers: bank admission; rank computation; model answer grading; fixture comparator; procedure matcher. Material parts: [EPI-OBJ-questions](#epi-obj-questions), [EPI-OBJ-rank-results](#epi-obj-rank-results), [EPI-OBJ-answer-judgments](#epi-obj-answer-judgments), [EPI-OBJ-calibration-cases](#epi-obj-calibration-cases), [EPI-OBJ-calibration-results](#epi-obj-calibration-results), [EPI-OBJ-cli-traces](#epi-obj-cli-traces), [EPI-OBJ-tool-metrics](#epi-obj-tool-metrics). Each owns separate form, storage, lineage, checks and authority. Route records split those authorities. This is not a duplicate of [RT-RTE-search-get](runtime.md#rt-rte-search-get): it measures selected outputs or calls against references. Generation provenance and actual performance remain unestablished where uninspected. Evidence: SRC-1, `src/memexos/evals/retrieval.py`, `src/memexos/evals/gate2.py`, `src/memexos/evals/tooluse.py`; passages below.

#### EPI-OBJ-questions
Label: Retrieval reference bank
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: retrieval reference bank within the evaluation container. Form: Natural-language questions/key_facts/use_rule and symbolic IDs, gold_pages, qrels and admission flags. Storage substrate: vault questions.jsonl and qrels.jsonl. Lineage: Candidate questions plus model-returned keep, gold_pages, key_facts and reason; qrel-pool provenance remains uninspected. Checks: Model keep and returned-page existence admit references; stale paths affect selection, not semantic correctness. Actual consumer authority: L1 scoring, L2 grading and procedural gold matching consume benchmark-reference authority across evaluations, not production truth endorsement. Evidence: SRC-1, `src/memexos/evals/retrieval.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

#### EPI-OBJ-rank-results
Label: L1 rank results
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: l1 rank results within the evaluation container. Form: Symbolic path lists and numerical ranks/recall/aggregates. Storage substrate: run l1.json, summary.json and reports. Lineage: Search results feed deterministic score and summarize using bank/qrels. Checks: Fixed arithmetic and error predicates; no source-truth judgment. Actual consumer authority: Reports/status and optional CLI thresholds consume diagnostic metrics; no automatic production optimizer established. Evidence: SRC-1, `src/memexos/evals/retrieval.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

#### EPI-OBJ-answer-judgments
Label: L2 answer judgments
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: l2 answer judgments within the evaluation container. Form: Natural-language judgments with symbolic keyed verdict fields. Storage substrate: verdicts in l2.json and rendered reports. Lineage: A separate model call receives nonempty recorded answers and bank references. Checks: Model grading plus offered-key filtering; empty answers excluded, reference correctness not independently established. Actual consumer authority: l2_report and operator reports consume advisory answer-quality judgments; no live publication veto or policy revision established. Evidence: SRC-1, `src/memexos/evals/retrieval.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-answer-grading](#epi-rte-answer-grading). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

#### EPI-OBJ-calibration-cases
Label: Reviewer calibration cases
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: reviewer calibration cases within the evaluation container. Form: Natural-language authored raw/wiki text and seeded errors plus symbolic expect_pass/detect rules. Storage substrate: shipped case assets and constructed case vault. Lineage: Target-authored fixtures loaded by cases and build; not production episodes. Checks: Authored expected outcomes and textual seed rules are comparator references; independent correctness/representativeness unestablished. Actual consumer authority: Gate 2 consumes constructed inputs; run_case/caught consume local test-reference authority, not live knowledge admission. Evidence: SRC-1, `src/memexos/evals/gate2.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-review-calibration](#epi-rte-review-calibration). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

#### EPI-OBJ-calibration-results
Label: Reviewer calibration results
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: reviewer calibration results within the evaluation container. Form: Symbolic passed/completed/as_expected and seed flags, metrics and natural-language errors. Storage substrate: case review/review.json and summary.json, rendered output. Lineage: Model review and program gate results feed deterministic expectation/seed comparison. Checks: Equality and textual seed predicates; as_expected alone need not imply all seeds caught. Actual consumer authority: render and evaluation CLI status consume diagnostic calibration results; no automatic rubric rewrite established. Evidence: SRC-1, `src/memexos/evals/gate2.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-review-calibration](#epi-rte-review-calibration). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

#### EPI-OBJ-cli-traces
Label: Evaluation CLI traces
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: evaluation cli traces within the evaluation container. Form: Symbolic argv/command/exit and search/opened metadata. Storage substrate: per-run calls.jsonl and loaded call dictionaries. Lineage: CLI hook records calls and load_calls combines associated metadata. Checks: Trace selection supplies procedure evidence, not validation of real side effects; non-CLI behavior not complete. Actual consumer authority: score/rescore consume recorded procedure evidence; stub success carries no real command-effect authority. Evidence: SRC-1, `src/memexos/evals/tooluse.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

#### EPI-OBJ-tool-metrics
Label: Tool-use procedure metrics
Part of: [EPI-OBJ-evaluation](#epi-obj-evaluation)

Source-native identity: tool-use procedure metrics within the evaluation container. Form: Symbolic procedure flags, numerical counts/efficiency and formatted trace summaries. Storage substrate: tool fields in l2.json and tool-use summaries/reports. Lineage: score derives results from calls, scenario references and gold/qrels. Checks: Deterministic step/order/forbidden/search-count predicates; failed_calls separate from procedure_ok. Actual consumer authority: Reports/rescore consume diagnostic procedure metrics, not acceptance of answer truth or successful side effects. Evidence: SRC-1, `src/memexos/evals/tooluse.py`; minimum load-bearing passages and bounded route findings: see [EPI-RTE-tooluse-scoring](#epi-rte-tooluse-scoring). No observed result is adopted. Distinct material part of the valid container, not a replacement. Closest supplied runtime record [RT-RTE-search-get](runtime.md#rt-rte-search-get) concerns operational retrieval rather than evaluation references, evidence or results.

### Routes

#### EPI-RTE-writer-transform
Label: Writer compilation
Part of: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Endpoints/progression/owner: raw batch and existing pages → model writer → staged wiki/index/log/inbox edits. Code schedules, writer proposes, later checks veto. Object: [EPI-OBJ-wiki](#epi-obj-wiki). Content/update relation: truth-apt transformation: indeterminate. The requested summary, revision and inference operations do not establish semantic preservation or non-entailment of a concrete output. Remaining classifications include acquisition of quoted content, non-ampliative paraphrase, entailed conclusions and ampliative conjecture; deciding requires paired actual inputs/outputs. Guidance: compile prompt and requested full AGENTS read. Mode: unattended open-source batches, not a curriculum. No independent answer oracle; raw interpretation is model-mediated. Retained change: draft and potentially published text, not an inspected parameter update. Source warrant is unknown beyond retained attribution. Epistemic authority: candidate production only. Operational authority/path: writer receives natural-language instructions through backend prompts for this call, while checks decide later publication. No actual formulated theory instance is supplied.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: writer Result and staged edits.
- Later read-back: draft files reach reviewer/rework; published pages reach maintenance and search/get.
- Delegated visibility: separate model calls receive staging paths and task guidance; prior hidden state is not shown to cross calls.
- Selection predicate: pending raw batch plus writer-selected related pages.
- Invalidation or expiry: discard/hold/merge; later Git reversal is separate.
- Activation or effect: proposed text can reach gate inputs; semantic compliance unobserved.
- Evidence limits: implementation of a request does not establish its execution, correctness or accepted novel knowledge.

Evidence: SRC-1, `src/memexos/prompts/en/compile.md`; publication/recovery evidence also in the parent record. Claim association: [EPI-CLM-reviewed-memory](#epi-clm-reviewed-memory). Mismatch: requested synthesis is not demonstrated truth production.

> You maintain this knowledge base. First read AGENTS.md in full, then compile the raw files below following its §2.1 "Automatic mode"
> --- `src/memexos/prompts/en/compile.md`

#### EPI-RTE-gate1-check
Label: Gate 1 structural check
Part of: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Endpoints/owner: staged diff/base → deterministic gate1.check → errors/warnings/stats. Object/target/domain: changed paths, new-page structure/index inclusion, cited-file existence, duplicate/near-miss links and append-only log entry. Content/update relation: no content change. Epistemic license: checked structural properties of this diff, not source truth or entailment. Operational path: code errors reach writer rework and caller continuation as enforcing publication conditions; warnings only record concerns. Human contribution: no per-content approval. No semantic answer oracle. Admission/recovery belongs to the parent route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: passed/errors/warnings/stats.
- Later read-back: report errors reach a later rework invocation; live text only after caller publication.
- Delegated visibility: writer receives rendered structural problems.
- Selection predicate: changed paths and selected added lines/whole-file structural conditions.
- Invalidation or expiry: recheck after writer rework against the same base.
- Activation or effect: errors veto normal caller continuation; warnings do not.
- Evidence limits: structural checks do not establish semantic truth or undo prior out-of-worktree effects.

Evidence: SRC-1, `src/memexos/pipeline/gate1.py`. Claim association: [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication). Mismatch: structural pass is not semantic acceptance.

> if not SOURCES_HEADING.search(text):
>             errors.append(i18n.t("gate1.no_sources", path=p))
>         elif "raw/" not in text:
>             warnings.append(i18n.t("gate1.sources_no_raw", path=p))
> --- `src/memexos/pipeline/gate1.py`

#### EPI-RTE-selfcheck-check
Label: Sentence self-check
Part of: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Endpoints/owner: new unmarked diff sentences → selected evidence chunks → configured judge → low-support list → writer verification. Object: sentence/evidence pairs. Target/domain: every specific detail being stated or directly implied by the excerpts, not source reliability. Content/update relation: no content change. Code excludes metadata/headings/raw-list lines, repeated removed sentences and marked uncertainty/inference; BM25 selects three chunks from batch raws, up to eight cited raws and linked wiki pages. Default flag threshold is 0.6; fewer than half answered or unavailable judge yields skipped check. At most 60 flags are rendered, with sentence/excerpt truncation. Epistemic authority: provisional support diagnostics. Operational authority/path: advisory flags become another writer prompt, not an independent final publication veto. On skipped self-check code proceeds to Gate 2; rework need not receive another self-check. No reference-answer oracle or calibrated confidence established. Mode: open batch checking.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: 0/1/2 plus flags and summary.
- Later read-back: another writer invocation receives flag text against retained draft files.
- Delegated visibility: judge receives selected excerpts; writer receives a bounded rendered list, not the complete evidence set.
- Selection predicate: new unmarked diff units; low non-None support scores after BM25 selection.
- Invalidation or expiry: current draft/base only; no durable correctness certificate.
- Activation or effect: possible rework; unavailable judgment does not reject publication by itself.
- Evidence limits: omitted evidence and circular support from linked wiki remain possible; no observed accuracy.

Evidence: SRC-1, `src/memexos/pipeline/selfcheck.py`, `src/memexos/judge.py`, `src/memexos/pipeline/compile.py`. Claim association: [EPI-CLM-reviewed-memory](#epi-clm-reviewed-memory). Mismatch: “each sentence” is bounded by exclusions, evidence selection and availability.

> if s in old or MARKED.search(s):
>                     continue
> --- `src/memexos/pipeline/selfcheck.py`

> flagged = [(p, u, best[0] if best else "") for p, u, best in zip(scores, units, evid) if p is not None and p < threshold]
> --- `src/memexos/pipeline/selfcheck.py`

#### EPI-RTE-review-claims
Label: Gate 2 reviewer
Part of: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Endpoints/owner: raw/base access and changed wiki/index diff → structured reviewer → review.json. Object: [EPI-OBJ-review](#epi-obj-review). Content/update relation: truth-apt transformation: indeterminate; support judgments are themselves truth-apt but no inspected run individuates a correct entailment or conjecture. Target/domain: source faithfulness, key-point coverage, overwrite support/disclosure, citation support, injection compliance. Reviewer is asked to read raw before wiki. Other raw/existing wiki can support a claim missing from batch raws. Unchanged older content and source trustworthiness are out of scope. Honest marking is accepted as marking, not truth. Independence is a requested role distinction; model-family diagnostic is not a veto. No independent answer key or required human judgment. Epistemic authority: provisional source-relative judgments. Operational authority/path: structured fields feed a separate deterministic admission decision; integration notes and PARTIAL results can become advisory repairs. Mode: repeated review of open batch drafts, not an intervention study.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: persisted review.json and computed report.
- Later read-back: decide consumes fields; report.problems feeds rework/fix.
- Delegated visibility: bounded diff plus read-only file access; rework sees problems, not the whole reviewer session.
- Selection predicate: changed wiki/index and model-generated inventory/criticality/key-point labels.
- Invalidation or expiry: revised drafts get new reviews; old evidence remains recorded.
- Activation or effect: evidence production for a separate disposition, not an autonomous truth guarantee.
- Evidence limits: no observed complete claim inventory, raw-first compliance or reliable independent error distribution.

Evidence: SRC-1, `src/memexos/pipeline/gate2.py`, `src/memexos/prompts/en/gate2_rubric.md`. Claim association: [EPI-CLM-reviewed-memory](#epi-clm-reviewed-memory). Mismatch: source faithfulness is not truth of source.

> - **Out of scope**: unchanged older content (the weekly lint covers it); formatting (gate 1 checks it); writing style; whether the raw
>   source itself is trustworthy.
> --- `src/memexos/prompts/en/gate2_rubric.md`

> | `MARKED` | Explicitly marked `⚠️ unverified` or `(compiler's inference)`, stated as speculation, or stated as "not in the source; this knowledge base's own convention". **Honest marking is correct and not a problem** |
> --- `src/memexos/prompts/en/gate2_rubric.md`

#### EPI-RTE-review-decision
Label: Gate 2 disposition
Part of: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Endpoints/owner: review dictionary → gate2.decide → errors/warnings/metrics → caller review_loop → rework/hold/discard/publish eligibility. Object: reviewed draft and verdict fields. Content/update relation: no content change. Target: eligibility of this changed batch for source-faithful wiki publication. Evaluator/domain: deterministic rules over model inventory. Criterion: critical UNSUPPORTED/CONTRADICTED claims, unsupported/undisclosed substantive overwrites, complied injections and missed critical points veto; noncritical bad fraction >5% or must coverage <80% veto. MARKED is excluded from judged claims and the noncritical denominator. PARTIAL and integration notes warn, not block. No must points defaults to coverage 1.0. This is evidence-consuming acceptance for publication under that rubric, not truth acceptance of marked speculation or source claims. Code owns veto and continuation; writer proposes revisions, reviewer supplies labels; no routine human approval. The off/no-change branches are separate bypasses. Failed review returns bounded problems for model rework, then hold; unavailable review discards/cooldowns. Git permits operator recovery, not automatic semantic withdrawal. report.problems drops SUPPORTED/MARKED, retains PARTIAL/bad claims, bad overwrites/injections, missed must/critical points and integration notes; nice omissions do not enter that list. for_writer carries claim/source/location/reason to another writer. Force/path/horizon: enforcing symbolic batch admission in enabled paths, natural-language corrective guidance across rework and later fix.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: errors/warnings/metrics, pass/fail and orchestration outcome.
- Later read-back: review directories feed rework/fix; passing text feeds later readers.
- Delegated visibility: model judgments reach code; filtered problem list reaches writer.
- Selection predicate: reported verdict/criticality/importance and configured gate mode.
- Invalidation or expiry: revised drafts reviewed again; no automatic factual expiry of a passed sentence.
- Activation or effect: conditional publication permission, failure repair or holding/discard.
- Evidence limits: correctness of rules over fields does not establish completeness or truth of fields; pass can include MARKED, PARTIAL and some unsupported claims.

Evidence: SRC-1, `src/memexos/pipeline/gate2.py`, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/report.py`. Claim association: [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication). Mismatch: unqualified “nothing unreviewed” and “verified” exceed this conditional license.

> noncrit = [c for c in claims if not c["critical"] and c["verdict"] != "MARKED"]
> --- `src/memexos/pipeline/gate2.py`

> must_cov = sum(k["covered"] for k in must) / len(must) if must else 1.0
> --- `src/memexos/pipeline/gate2.py`

> if v in ("SUPPORTED", "MARKED"):
>             continue
> --- `src/memexos/pipeline/report.py`

#### EPI-RTE-wiki-retention
Label: Wiki publication
Part of: [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Endpoints/owner: caller-admitted staging → Stage.publish → live Git-backed vault/index refresh. Object: [EPI-OBJ-wiki](#epi-obj-wiki). Content/update relation: no content change at merge. Target/condition: caller continuation after checks or accepted off branch; Stage.publish has no independent certificate requirement. Epistemic license: none added by persistence. Operational path: live Markdown and indexes supply informational content to search/get and future maintenance across sessions. Prepared source links become live, but no separate post-acceptance semantic integration judgment is established by these inspected branches. This row isolates retention from checking/disposition; recovery/index details belong to the parent. No new human approval, answer oracle or improved-capacity evidence arises at merge.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: merge/publication status.
- Later read-back: search/get, future compile, lint/fix/correct read live pages.
- Delegated visibility: published files/indexes, not model hidden state.
- Selection predicate: caller outcome, including gate-off continuation.
- Invalidation or expiry: subsequent revision or operator Git reversal; no automatic source-truth expiry.
- Activation or effect: retained availability; downstream changed answers unobserved.
- Evidence limits: publication does not prove fresh indexes, reader snapshot consistency, factual truth or acceptance of a novel proposition.

Evidence: SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`; load-bearing passages and recovery in parent record. Claim association: [EPI-CLM-reviewed-memory](#epi-clm-reviewed-memory). Mismatch: retention is not infallible memory or independently checked lifecycle integration.

#### EPI-RTE-catalog-screen
Label: Category screen

Distinct identity: after source admission, this evaluates category fit; [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) evaluates keeping offered material. Endpoints/owner: source digest and taxonomy candidates → judge choice/scope calls → code adopt flag. Object: [EPI-OBJ-catalog](#epi-obj-catalog). Content/update relation: no content change. Target/domain: category and stated-scope fit, not truth or credibility of source claims. Default adopt requires membership, top probability ≥0.9, none-fits ≤0.1 and scope ≥0.8. Epistemic license: provisional category fit. Operational path: screen fields give precedence to primary domain at settle; they do not approve all evidence/usage labels. No independently correct reference label or human per-source decision. Mode: open classification; thresholds and candidate scope guide judgment.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: top/probabilities/scope/alternatives/adopt map.
- Later read-back: settle consumes screen; worker receives hints/precedents.
- Delegated visibility: judge sees digests and candidates, not proven complete source content.
- Selection predicate: taxonomy candidate set and probability/scope thresholds.
- Invalidation or expiry: later classification/reassignment may replace catalog choice.
- Activation or effect: can determine primary category at catalog admission.
- Evidence limits: confidence calibration and label correctness unobserved; not evidence-strength validation.

Evidence: SRC-1, `src/memexos/catalog/taxonomy.py`, `src/memexos/catalog/classify.py`. Claim association: [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Mismatch: confidence is not independent warrant.

> adopt = bool(choice in cand and p >= self.th("judge_min_top", 0.9) and p_none <= self.th("judge_max_none", 0.1)
>                          and scope is not None and scope >= self.th("judge_min_scope", 0.8))
> --- `src/memexos/catalog/taxonomy.py`

#### EPI-RTE-catalog-admission
Label: Catalog classification

Distinct identity: [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) keeps/drops sources; this characterizes already retained raws. Endpoints/owner: taxonomy/digests/hints/precedents → structured worker rows and proposed categories → settle/registry proposal checks → append catalog rows. Object: [EPI-OBJ-catalog](#epi-obj-catalog). Content/update relation: truth-apt transformation: indeterminate. Worker summaries and evidence labels have no inspected actual input/output establishing entailment or non-entailment. Target/criterion: accept normalized returned classifications under settle/category registry rules, for organizing this vault and guiding use. Confident screen can override primary domain; fallback/canonicalization handles unknown/proposed categories. Model proposes evidence/type/usage/durability/scope labels; code admits records without a separate per-source factual check in the inspected path. No routine human approval or independent correct-answer oracle. Mode: open categorization. Proposed new categories and catalog rows persist; later reassignment can replace them. Epistemic license: characterization for use, not certification of source truth. Operational path: catalog labels reach compile guidance, source pages and retrieval metadata across calls. Full registry decision/recovery internals remain uninspected.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: classification count, rows and events.
- Later read-back: compile classifications, effective metadata and synchronization consume catalog.
- Delegated visibility: worker receives bounded digests and taxonomy guidance; later consumers get normalized labels/notes.
- Selection predicate: requested/missing raw paths, screen precedence, registry/canonicalization/fallback rules.
- Invalidation or expiry: appended newer rows/reassignment and category decisions; writer overrides may persist.
- Activation or effect: source-use guidance and organization change, without demonstrated source-truth improvement.
- Evidence limits: no observed row correctness, independently validated evidence labels or full taxonomy lifecycle audit.

Evidence: SRC-1, `src/memexos/catalog/classify.py`. Claim association: [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Mismatch: organization is not knowledge acceptance.

> if s and s["adopt"]:
>             dom, by = s["top"], "judge"
> --- `src/memexos/catalog/classify.py`

> append_jsonl(catalog_path(cfg), rows)
>         done += len(rows)
> --- `src/memexos/catalog/classify.py`

#### EPI-RTE-catalog-sync
Label: Catalog synchronization

Distinct identity: metadata synchronization is not model compilation in [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish). This is an additional shipped publication route. Endpoints/owner: catalog/history plus source-page frontmatter → effective fields/set_frontmatter/regroup_index → Stage → Gate 1 → publish, without Gate 2. Object: [EPI-OBJ-catalog](#epi-obj-catalog) to [EPI-OBJ-wiki](#epi-obj-wiki). Content/update relation: truth-apt transformation: non-ampliative reshaping, mechanically assigning already selected metadata; not discovery of a new fact. For concrete code deduction, text `---\nevidence: old\n---\nBody` with fields `{'evidence':'new'}` loses the old evidence line, gains a JSON-string-valued `evidence: "new"` line and retains Body. No target execution is needed for that deduction. sync associates a page through primary_raw; writer_set/effective preserve detected writer overrides; scope_note can be cut to 300 characters. Full semantic preservation of a truncated note is not established. Target/condition: structural admissibility of metadata changes, not truth of new label. Owner/proposer/decider: program applies catalog values and runs Gate 1; no human approval or model answer oracle. Recovery: Gate 1 failure holds staging; otherwise publish. Epistemic license: none added by copying labels. Operational path: source-page metadata and index reach later compiler/retrieval users, potentially changing evidence-strength guidance. This is a forcing case against universal semantic review, not a supersession of the runtime's valid compile container.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed/page counts and status.
- Later read-back: source pages and index expose revised metadata to writers/readers.
- Delegated visibility: selected symbolic fields become visible source-use guidance; no model call during sync.
- Selection predicate: source pages with identified catalogued primary raw; fields not detected as writer overrides.
- Invalidation or expiry: later sync/catalog change; preserved writer overrides can outlive catalog changes.
- Activation or effect: metadata publication after Gate 1, with no semantic reviewer requirement in catalog_sync.
- Evidence limits: example is implementation deduction, not observation; file existence and valid frontmatter do not prove an evidence label true.

Evidence: SRC-1, `src/memexos/catalog/classify.py`. Claim association: [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication). Mismatch: additional Gate-1-only publication of material source-use metadata.

> """Run sync in a staging worktree, check it with gate 1 and publish (no model involved)."""
> --- `src/memexos/catalog/classify.py`

> return "---\n" + "\n".join(new) + "\n---\n" + (text[m.end():] if m else text)
> --- `src/memexos/catalog/classify.py`

#### EPI-RTE-usage-judgment
Label: Usage judgment

Distinct identity: produces feedback reports that [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance) can later verify; not that route's verification itself. Endpoints/owner: extracted real events with answers → model judgment of question/search/opened/answer excerpts → verdict/reason/bad_pages → judgment and pending-feedback/source-error ledgers. Object: usage part of [EPI-OBJ-review](#epi-obj-review). Content/update relation: truth-apt transformation: indeterminate. Target/domain: apparent usefulness or problems from use context, not independent truth checking or causal usefulness identification. Code selects events; worker proposes diagnostics. Question is cut to 1500 characters and answer to 2500. No expected-answer oracle or routine human approval; deployment-feedback mode, not randomized experiment. Bad-page prefix routes reports; later verifier can reject them. Epistemic license: provisional diagnostic evidence only. Operational path: reports reach summary/verification/fix through stored ledgers across calls, advisory until downstream disposition.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: judgment count and appended records.
- Later read-back: summaries and pending feedback reach verification/fix.
- Delegated visibility: batched excerpts to worker; generated reasons/targets to verifier.
- Selection predicate: real, unjudged events with answer and no follow_up; model bad_pages selects target.
- Invalidation or expiry: judged keys suppress repeat; downstream rejection/unsure can withhold repair.
- Activation or effect: diagnostics queue possible repairs, not immediate page revision.
- Evidence limits: no observed episode, accurate diagnosis or causal outcome attribution supplied; extraction provenance not independently inspected.

Evidence: SRC-1, `src/memexos/usage.py`. Claim association: [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Mismatch: inferred usefulness is not measured component benefit.

> append_jsonl(d / "judgments.jsonl", rows)
>         append_jsonl(d / "feedback.jsonl", fb)
>         append_jsonl(d / "source-errors.jsonl", srcerr)
> --- `src/memexos/usage.py`

#### EPI-RTE-feedback-check
Label: Feedback verification
Part of: [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance)

Endpoints/owner: pending feedback/page/raw → worker → confirmed/rejected/unsure and evidence → separate repair disposition in parent route. Object: feedback part of [EPI-OBJ-review](#epi-obj-review). Content/update relation: truth-apt transformation: indeterminate; no concrete correct diagnosis supplied. Target/domain: page disagreement with source, newer raw statement or missed source point. Prompt makes raw the only ground truth; external reporter evidence may be read for reference but cannot alone ground the page. Outdated without newer raw should be unsure; stale or mistaken report can be rejected. No independent answer oracle or routine human approval. Mode: open feedback checking. Host creates fix jobs only for confirmed plus nonempty problems, admitting repair work rather than directly replacing page text. to_fix_job converts MISSED to missing must points, other problems to claim verdicts, and retains source/location/reason. Subsequent fix/correct and review retain their own veto/recovery paths. Epistemic license: source-relative diagnosis. Operational path: structured judgment/status then stored review-format problem list shapes a later writer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: worker verdict/evidence, feedback-status and possible fix directory.
- Later read-back: fix consumes stored problems, revised pages later reach search/get.
- Delegated visibility: read-only verifier sees report and vault; writer sees converted problem list.
- Selection predicate: pending feedback limit; source_error uses a separate prompt.
- Invalidation or expiry: status removes work from pending; later source/page change can need new feedback.
- Activation or effect: conditional admission of repair tasks, not direct acceptance of corrected truth.
- Evidence limits: alternate source-error prompt not assessed; external measurement truth may need capture as raw before this route licenses correction.

Evidence: SRC-1, `src/memexos/usage.py`, `src/memexos/prompts/en/usage_verify.md`; host conditional quoted in parent record. Claim association: [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Mismatch: confirmation concerns raw-relative defects, not universal factual validation.

> - unsure: not enough evidence. When the report says "outdated" but raw/ has nothing newer, answer unsure and say in summary that a new source is needed first
> --- `src/memexos/prompts/en/usage_verify.md`

#### EPI-RTE-evaluation-bank
Label: Retrieval bank verification

Distinct identity: no supplied route declares reference-bank admission; [RT-RTE-search-get](runtime.md#rt-rte-search-get) returns operational content, not test references. Endpoints/owner: candidate questions → model verifier → keep/gold_pages/key_facts/reason → code bank/dropped append. Object: [EPI-OBJ-questions](#epi-obj-questions). Content/update relation: truth-apt transformation: indeterminate. Target/criterion/use/scope: eligibility as reference for this vault's retrieval evaluation, based on model keep and existing returned gold pages for answerable questions. Reference oracle for later scores is this bank plus qrels, not an independently authored answer key established by this run. Model proposes/revises reference material, host admits; no per-question human approval. Failure drops or retries failed model batch; IDs support resumption, stale page references affect later selection. Guidance is eval_verify prompt, whose full semantics and generation/mining/pool provenance remain uninspected. Epistemic license: local benchmark-reference authority only. Operational path: bank fields control L1 relevant-page metrics and L2 model grading across evaluation runs, not automatic wiki admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: kept count, bank and dropped records, bank commit attempt.
- Later read-back: L1/L2 and reports consume bank; renamed/merged gold paths become stale.
- Delegated visibility: verifier returns revised gold_pages/key_facts; scorers consume admitted reference.
- Selection predicate: not already banked/dropped; returned keep and file-existence condition.
- Invalidation or expiry: stale path logic; semantic staleness detection beyond that unestablished.
- Activation or effect: evaluation-reference authority, not production truth endorsement.
- Evidence limits: empty gold_pages can satisfy all(...); file existence and model keep do not prove correct answer or oracle independence.

Evidence: SRC-1, `src/memexos/evals/retrieval.py`. Claim association: [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Mismatch: model-maintained reference is not independent ground truth.

> if r and r["keep"] and all((cfg.vault / p).exists() for p in r["gold_pages"] if it.get("answerable")):
> --- `src/memexos/evals/retrieval.py`

#### EPI-RTE-retrieval-scoring
Label: L1 rank scoring

Distinct identity: evaluates outputs of [RT-RTE-search-get](runtime.md#rt-rte-search-get), not retrieval itself. Endpoints/owner: result path lists plus bank/qrels → deterministic score/summarize → report. Object: [EPI-OBJ-rank-results](#epi-obj-rank-results); reference input: [EPI-OBJ-questions](#epi-obj-questions). Content/update relation: truth-apt transformation: entailed derivation. Target/domain: first relevant-page rank and gold recall@10 for answerable nonstale selected questions/modes. Reference oracle: bank/qrels. Example implementation deduction: top [a,b], relevant {b}, gold_pages [b] gives first=2 and recall10=1. Warrant is conditional on input lists/definitions, not warranted subject facts. Epistemic license: arithmetic benchmark metric. Operational path: persisted report and optional CLI thresholds inform operators; no automatic production optimizer is established in inspected scoring. Mode: bounded benchmark, not a controlled causal comparison merely by including several modes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranks/recall/aggregates and report.
- Later read-back: operator reports and summaries; no inspected automatic parameter/policy update consumer.
- Delegated visibility: metrics summarize references and results; do not expose all reference correctness evidence.
- Selection predicate: answerable nonstale bank entries, selected modes and limit.
- Invalidation or expiry: rescore can use current bank/qrels; historical path lists persist.
- Activation or effect: diagnostic metrics and optional evaluation exit status, not factual certification.
- Evidence limits: deduction was not executed; sampling, oracle quality and component-effect attribution remain unestablished.

Evidence: SRC-1, `src/memexos/evals/retrieval.py`. Claim association: [EPI-CLM-evolves-itself](#epi-clm-evolves-itself). Mismatch: relevance score does not warrant source truth or causal improvement.

> r["first"] = ranks[0] if ranks else None
>         r["recall10"] = len(set(r["top"][:10]) & set(it["gold_pages"])) / max(len(it["gold_pages"]), 1)
> --- `src/memexos/evals/retrieval.py`

#### EPI-RTE-answer-grading
Label: L2 answer grading

Distinct identity: unlike [RT-RTE-search-get](runtime.md#rt-rte-search-get), judges final answer text against bank references. Endpoints/owner: nonempty recorded answers and question/key_facts/use_rule/gold_pages → model grader → filtered verdict keys → l2.json/report. Object: [EPI-OBJ-answer-judgments](#epi-obj-answer-judgments); reference input: [EPI-OBJ-questions](#epi-obj-questions). Content/update relation: truth-apt transformation: indeterminate. Target/domain: answer quality against this bank. No-answer is excluded from wrong-answer judgment. Oracle provider: bank reference, itself model-maintained. Model judges, code persists; no routine human answer judgment. Epistemic license: local answer-quality judgment under the reference, not producing-process explanation or source truth. Operational path: advisory reports across evaluation calls; no production veto or automatic policy revision in inspected grade. Mode: bounded evaluation, not independent component intervention.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: grading status, persisted verdicts and report.
- Later read-back: report consumers; no automatic live-rule change established.
- Delegated visibility: grader receives up to 6000 answer characters plus reference fields.
- Selection predicate: ungraded nonempty answers with question still in bank; result keys filtered to offered items.
- Invalidation or expiry: resumable keyed grading, mutable model endpoint outside source.
- Activation or effect: advisory benchmark verdicts.
- Evidence limits: separate grader call does not establish independent truth, calibration or causal benefit; no results adopted.

Evidence: SRC-1, `src/memexos/evals/retrieval.py`. Claim association: none. Mismatch: benchmark success cannot establish mechanism, transfer or replay safety.

> data["verdicts"] += [v for v in res["results"] if v["key"] in keys]
> --- `src/memexos/evals/retrieval.py`

#### EPI-RTE-review-calibration
Label: Gate 2 calibration

Distinct identity: measures [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)'s reviewer on constructed cases, not live source admission. Endpoints/owner: authored case/expect_pass/detect seeds → constructed vault and review → caught()/equality comparison → summary/CLI status. Objects: [EPI-OBJ-calibration-cases](#epi-obj-calibration-cases) supplies references; [EPI-OBJ-calibration-results](#epi-obj-calibration-results) receives judgments/comparisons. Content/update relation: truth-apt transformation: entailed derivation for computed comparisons, conditional on the model-produced review. Target/domain: expected batch outcome and seeded error detection on selected authored cases. Answer oracle: case expect_pass and seed-detection rules, not model confidence. Concrete deduction: completed passed=False, expect_pass=False gives as_expected=True even if a seed was missed; seed flags are separately checked for CLI success. No target execution occurred here. Epistemic license: matching authored expectations, not production recall or independence. Operational path: summary and evaluation exit status, diagnostic to operators; no inspected automatic rubric rewrite. Mode: bounded authored fixtures, not independently varied component effect.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: summary including as_expected and seed-caught flags.
- Later read-back: reports and CLI evaluation outcome.
- Delegated visibility: reviewer gets constructed vault; comparator gets structured judgments and seed rules.
- Selection predicate: selected shipped cases and textual detection rules.
- Invalidation or expiry: each case/run defines scope; no automatic deployment revision.
- Activation or effect: bounded diagnostic/status.
- Evidence limits: seed phrase matching can miss paraphrases; no observed calibration or production-quality result adopted.

Evidence: SRC-1, `src/memexos/evals/gate2.py`. Claim association: none. Mismatch: fixture outcome is not global reviewer reliability.

> "as_expected": code != 2 and rep.get("passed") == case["expect_pass"], "seeds": seeds,
> --- `src/memexos/evals/gate2.py`

#### EPI-RTE-tooluse-scoring
Label: Tool-use scoring

Distinct identity: scores CLI procedure, not the content returned by [RT-RTE-search-get](runtime.md#rt-rte-search-get). Endpoints/owner: CLI trace plus scenario reference steps/forbid/max_search/gold → deterministic matcher → metrics/report. Objects: [EPI-OBJ-cli-traces](#epi-obj-cli-traces) supplies evidence; [EPI-OBJ-tool-metrics](#epi-obj-tool-metrics) receives results; [EPI-OBJ-questions](#epi-obj-questions) can supply gold references. Content/update relation: truth-apt transformation: entailed derivation for metrics under the reference. Target/domain: procedural match/call efficiency, not answer truth or successful side effects. Oracle: task reference and gold/qrels. CLI hook records argv/exit; MEMEX_EVAL_STUB can return success without carrying out configured side-effect commands. procedure_ok depends on matched steps/forbidden/excess searches; failed_calls is computed separately. Therefore procedural success cannot warrant real command-effect success. No human per-call judgment; mode is bounded scenario evaluation. Epistemic license: measured procedure under those predicates only. Operational path: diagnostic tool-use reports and summaries, not automatic production adaptation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: procedure_ok/efficiency/failed/repeated/forbidden/trace metrics.
- Later read-back: report/summary and rescore consumers.
- Delegated visibility: scorer gets recorded CLI calls and reference; evaluated agent can see simulated success text.
- Selection predicate: reference order/steps, matching calls/gold, forbidden and max-search rules.
- Invalidation or expiry: rescore can recompute from stored traces/current references.
- Activation or effect: bounded procedure score, not acceptance of answer truth or actual side effects.
- Evidence limits: shipped result artifacts remain uninspected; non-CLI actions, reference quality and stubbed effects bound conclusions.

Evidence: SRC-1, `src/memexos/evals/tooluse.py`, `src/memexos/cli.py`. Claim association: none. Mismatch: procedural success and actual execution success differ.

> procedure_ok = len(matched) == len(ref["steps"]) and not forbidden and not too_many
> --- `src/memexos/evals/tooluse.py`

> print(f"(evaluation) `memex {' '.join(argv)}` was recorded and not carried out; treat it as done.")
> --- `src/memexos/cli.py`

### Claims

#### EPI-CLM-reviewed-memory
Label: Reviewed persistent memory

Claim/source/layer: SRC-1, `README.md`, doctrine/design, advertises reviewed searchable knowledge across conversations and unreviewed-publication exclusion. Closest supplied claim is [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication): that record concerns the compiler contract, while this records the broader public memory/verification claim and its sentence-level reading. Support: implemented candidate compilation, review, persistence and retrieval, not observed reliable performance. [EPI-RTE-selfcheck-check](#epi-rte-selfcheck-check) excludes marked content and selected diff categories; [EPI-RTE-review-claims](#epi-rte-review-claims) excludes source trust; [EPI-RTE-review-decision](#epi-rte-review-decision) permits PARTIAL/MARKED and bounded noncritical errors. Configured off/no-change continuation and [EPI-RTE-catalog-sync](#epi-rte-catalog-sync)'s Gate-1-only metadata publication defeat an unqualified universal-review interpretation. No observed complete source retention or later caller reliance; no causal benefit evidence. The supported claim is an implemented, conditional source-relative review and memory service, not “nothing lost” or “every sentence verified true.”

> - **Publishes nothing unreviewed.** Each compile happens in a staging copy and passes program checks, a self-check and an
>   independent review by a second model that compares every sentence with its source. Failures go back for rework;
> --- `README.md`

#### EPI-CLM-evolves-itself
Label: Evolving knowledge service

Claim/source/layer: SRC-1, `README.md`, doctrine/design, describes learning on its own and evolving itself through usage, correction, taxonomy and evaluations. Distinct from [RT-CLM-schema-change](runtime.md#rt-clm-schema-change), which addresses the schema proposal/approval contract, not this broad adaptation claim. Implementation support: usage diagnostics → verification → stored repair problems → staged correction → later retrieval; classification/category affordances and local evaluation references. See [EPI-RTE-usage-judgment](#epi-rte-usage-judgment), [EPI-RTE-feedback-check](#epi-rte-feedback-check), [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance), [EPI-RTE-catalog-admission](#epi-rte-catalog-admission) and [EPI-RTE-evaluation-bank](#epi-rte-evaluation-bank). No observed run or causal comparison adopted.

Self-improvement attribution boundary: MemexOS's retained knowledge/organization and its later compilation/retrieval service across sessions, not the external model's weights or an external agent's whole capacity. Objective independent of a particular edit: reduce wrong/missing source-relative knowledge and retrieval failures. Link 1 (evidence shapes proposed update) is wired through report/verification/problem prompts, but accurate evidence use is unobserved. Link 2 (update changes own organization) is wired through staged wiki publication and metadata/category maintenance. Link 3 (live behavioral-authority path) is wired through later writer guidance and retrieval delivery; delivery does not guarantee changed external answers. Link 4 (subsequent operation exercises and depends on the change) is unestablished without longitudinal trace/intervention. Thus an improvement-directed self-change pathway is implemented/dispositional; exercised self-improvement and successful improvement are not established. Evaluation reports alone have no inspected automatic optimizer consumer. This conclusion does not require a universal rejection gate or deny the existing pathways.

Independent properties: learning as improved future capacity is unestablished, not disproved by fixed model weights; retained revisions can change available knowledge without demonstrated improvement. Reflection has a partial source-native wiring witness: usage events can update judgments about use, and those judgments can drive repairs; fidelity of this representation and exercised two-way effect are unobserved. Autonomy is wired for several internal admission/review/repair operations, not established for every system operation or all inbox decisions. A concrete formulated theory instance is not individuated in this report: theory-builder conditions 1–4, addressability and reflective theory building remain unestablished here, rather than inferred from correction loops or model opacity. Raw/page claim criticisms can be retained and shape a next writer, but their existence alone does not establish a theory-builder cycle. The schema proposal route supplies a different, bounded doctrine-only collaboration claim, not automatic criticism and deployment of changed method texts.

> - **Evolves itself.** It watches how agents use the knowledge (what they searched for, opened, cited, and whether it
>   helped), turns wrong or missing answers into corrections, lints itself weekly, proposes new categories as your
>   interests shift, and measures its own retrieval quality with a question bank it maintains.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member. Supplied [RT-BAP-writer-guidance](runtime.md#rt-bap-writer-guidance), [RT-BAP-review-verdicts](runtime.md#rt-bap-review-verdicts) and [RT-BAP-retrieved-pages](runtime.md#rt-bap-retrieved-pages) retain their identities; newly traced catalog, feedback and evaluation consumers/forces/horizons are specified in their route records above.
