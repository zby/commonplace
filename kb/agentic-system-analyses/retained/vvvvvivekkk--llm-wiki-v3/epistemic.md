---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LLM-Wiki-v3 epistemic routes: source-conditioned proposals, lexical checks, curated retention and evaluation authority."
run-id: AAS-2026-10-18-llm-wiki-v3-0c553a3118eb-01
reviewed-boundary: "267541db838cbca757a112bd0cfa47fa61eb5fb2"
---

# LLM-Wiki-v3 epistemic report

## Source-and-claim boundary

The question is what licenses reliance on retained claims, and how checking, admission and retrieval affect that license. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identities/layers: see [Source register](boundary.md#source-register), SRC-1. No additional source or revision is introduced. All new findings below are implementation or doctrine/design; no target execution was performed. The tracked Ada page establishes a candidate artifact, not an observed execution of a producing or accepting route.

Coverage distinguishes direct inspection in this job from supplied findings. Each cited record owns its detailed evidence and limitations.

| Entry point / operation | SRC-1 source path | Coverage / records | Limit and prevented conclusion |
| --- | --- | --- | --- |
| CLI dispatch, validate, validate-all, hook | `src/wiki/cli/__init__.py`, `scripts/pre-commit`, `src/wiki/validate.py`, `Makefile` | Direct complete reads; [EPI-RTE-schema-check](#epi-rte-schema-check) | Installed hook and actual successful commits unobserved |
| ingest and propose_pages | `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/hashing.py`, `AGENTS.md` | Direct complete reads; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), new material parts below | No model response/proposal history; semantic preservation unresolved |
| quote/check/escalation/dedupe | `src/wiki/ingest/spancheck.py`, `src/wiki/ingest/diff.py`, `src/wiki/ingest/pipeline.py` | Direct complete reads; [EPI-RTE-span-check](#epi-rte-span-check), [EPI-RTE-proposal-selection](#epi-rte-proposal-selection) | No semantic truth adjudicator in these inspected checks |
| review/edit/reject/direct acceptance | `src/wiki/review.py`, `src/wiki/cli/__init__.py` | Direct complete reads; [RT-RTE-page-review](runtime.md#rt-rte-page-review), new disposition/retention parts | Human evidence use and correctness unobserved |
| direct curated seed | `scripts/seed_corpus.py` | Direct main read; supplied [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed) | Individual source/page specs not audited; no seed-wide fidelity conclusion |
| rebuild, query, adapters, optional ranking | `src/wiki/retrieve/store.py`, `src/wiki/retrieve/query.py`, `src/wiki/retrieve/fusion.py` | Direct complete reads; internals/builders supplied by [RT-RTE-index-query](runtime.md#rt-rte-index-query) | Optional model internals uninspected; no downstream agent answer path supplied |
| retrieval/components metrics and saved outputs | `src/wiki/eval/harness.py`, `src/wiki/eval/metrics.py`, `src/wiki/cli/__init__.py` | Direct complete reads; [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement) | Saved baselines remain attributed reports; no causal or reproduced outcome |
| ingest metric | `src/wiki/eval/ingest_eval.py`, `src/wiki/cli/__init__.py` | Direct complete reads; [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement) | Missing raw bytes prevent corpus replay; subset selection limits mean |
| query bootstrap | `src/wiki/cli/__init__.py` | Direct complete read; [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap), [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap) | No actual label review/merge evidence |
| namespace YAML, chunking, audit, component internals | `schema/`, `src/wiki/ingest/chunk.py`, `src/wiki/audit.py`, `src/wiki/retrieve/` | Supplied boundary/runtime findings, not re-audited here | No independent exhaustive contract/encoder audit or system-complete semantic negative |
| MCP, context compiler, autonomous eval admission, lint/supersede | `README.md`, `Makefile`, `src/wiki/cli/__init__.py` | Direct dispatch/stub comparison; supplied boundary exclusions | Intended future paths are not an observed deployed loop |

Knowledge/warrant claims: [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy), [RT-CLM-history-policy](runtime.md#rt-clm-history-policy), [EPI-CLM-faithfulness-support](#epi-clm-faithfulness-support), [EPI-CLM-eval-gates](#epi-clm-eval-gates), [EPI-CLM-provenance-trust](#epi-clm-provenance-trust). No defect requiring supplied-member supersession was found: runtime's partial-enforcement and forcing-route qualifications survive direct inspection. This report adds evaluator scope, separate lifecycle functions and the no-marker metric countercase. Uninspected page specifications prevent a corpus-complete truth assessment, not completion of this bounded architectural account.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-raw-source](#epi-obj-raw-source) | see [EPI-OBJ-raw-source](#epi-obj-raw-source) | see [EPI-OBJ-raw-source](#epi-obj-raw-source) | SRC-1, `src/wiki/ingest/hashing.py` | see [EPI-OBJ-raw-source](#epi-obj-raw-source) |
| [EPI-OBJ-page-body](#epi-obj-page-body) | see [EPI-OBJ-page-body](#epi-obj-page-body) | see [EPI-OBJ-page-body](#epi-obj-page-body) | SRC-1, `knowledge/entities/ada-lovelace.md` | see [EPI-OBJ-page-body](#epi-obj-page-body) |
| [EPI-OBJ-page-metadata](#epi-obj-page-metadata) | see [EPI-OBJ-page-metadata](#epi-obj-page-metadata) | see [EPI-OBJ-page-metadata](#epi-obj-page-metadata) | SRC-1, `src/wiki/ingest/pipeline.py` | see [EPI-OBJ-page-metadata](#epi-obj-page-metadata) |
| [EPI-OBJ-query-labels](#epi-obj-query-labels) | see [EPI-OBJ-query-labels](#epi-obj-query-labels) | see [EPI-OBJ-query-labels](#epi-obj-query-labels) | SRC-1, `src/wiki/cli/__init__.py` | see [EPI-OBJ-query-labels](#epi-obj-query-labels) |
| [EPI-OBJ-eval-results](#epi-obj-eval-results) | see [EPI-OBJ-eval-results](#epi-obj-eval-results) | see [EPI-OBJ-eval-results](#epi-obj-eval-results) | SRC-1, `src/wiki/eval/harness.py` | see [EPI-OBJ-eval-results](#epi-obj-eval-results) |

Opaque parametric components and instruction authority are separately inventoried by [RT-CMP-haiku-extractor](runtime.md#rt-cmp-haiku-extractor), [RT-CMP-sonnet-extractor](runtime.md#rt-cmp-sonnet-extractor), [RT-CMP-dense-embedding](runtime.md#rt-cmp-dense-embedding), [RT-CMP-cross-encoder](runtime.md#rt-cmp-cross-encoder) and [RT-BAP-ingest-instructions](runtime.md#rt-bap-ingest-instructions). These supply parameters/version/endpoint and guidance limits; this job adds no claim about inaccessible weights. Derived index representations belong to [RT-RTE-index-query](runtime.md#rt-rte-index-query), not a new accepted theory.

## Authority-route ledger

The linked declarations own the fields indicated by “see”; architectural status is this overlay's assessment. No route below is classified as observed. Check production, disposition and retention are distinct rows; no accepted-claim lifecycle-integration route is established by storing links or rebuilding an index.

Route ID: [EPI-RTE-raw-import](#epi-rte-raw-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Content/update relation: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Transition or check target: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Evaluator/condition and domain: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Activation and timing: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Possible or observed result: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Implemented force: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Epistemic authority and scope: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Evidence source ID and local anchor: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Claim IDs or none: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Mismatch marker or none: see [EPI-RTE-raw-import](#epi-rte-raw-import)
Gap/limit: see [EPI-RTE-raw-import](#epi-rte-raw-import)

Route ID: [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Content/update relation: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Transition or check target: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Evaluator/condition and domain: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Activation and timing: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Possible or observed result: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Implemented force: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Epistemic authority and scope: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Evidence source ID and local anchor: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Claim IDs or none: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Mismatch marker or none: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)
Gap/limit: see [EPI-RTE-page-extraction](#epi-rte-page-extraction)

Route ID: [EPI-RTE-quote-location](#epi-rte-quote-location)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Content/update relation: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Transition or check target: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Evaluator/condition and domain: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Activation and timing: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Possible or observed result: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Implemented force: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Epistemic authority and scope: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Evidence source ID and local anchor: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Claim IDs or none: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Mismatch marker or none: see [EPI-RTE-quote-location](#epi-rte-quote-location)
Gap/limit: see [EPI-RTE-quote-location](#epi-rte-quote-location)

Route ID: [EPI-RTE-schema-check](#epi-rte-schema-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Content/update relation: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Transition or check target: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Evaluator/condition and domain: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Activation and timing: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Possible or observed result: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Implemented force: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Epistemic authority and scope: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Evidence source ID and local anchor: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Claim IDs or none: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Mismatch marker or none: see [EPI-RTE-schema-check](#epi-rte-schema-check)
Gap/limit: see [EPI-RTE-schema-check](#epi-rte-schema-check)

Route ID: [EPI-RTE-span-check](#epi-rte-span-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-span-check](#epi-rte-span-check)
Content/update relation: see [EPI-RTE-span-check](#epi-rte-span-check)
Transition or check target: see [EPI-RTE-span-check](#epi-rte-span-check)
Evaluator/condition and domain: see [EPI-RTE-span-check](#epi-rte-span-check)
Activation and timing: see [EPI-RTE-span-check](#epi-rte-span-check)
Possible or observed result: see [EPI-RTE-span-check](#epi-rte-span-check)
Implemented force: see [EPI-RTE-span-check](#epi-rte-span-check)
Epistemic authority and scope: see [EPI-RTE-span-check](#epi-rte-span-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-span-check](#epi-rte-span-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-span-check](#epi-rte-span-check)
Evidence source ID and local anchor: see [EPI-RTE-span-check](#epi-rte-span-check)
Claim IDs or none: see [EPI-RTE-span-check](#epi-rte-span-check)
Mismatch marker or none: see [EPI-RTE-span-check](#epi-rte-span-check)
Gap/limit: see [EPI-RTE-span-check](#epi-rte-span-check)

Route ID: [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Content/update relation: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Transition or check target: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Evaluator/condition and domain: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Activation and timing: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Possible or observed result: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Implemented force: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Epistemic authority and scope: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Evidence source ID and local anchor: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Claim IDs or none: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Mismatch marker or none: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)
Gap/limit: see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)

Route ID: [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Content/update relation: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Transition or check target: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Evaluator/condition and domain: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Activation and timing: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Possible or observed result: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Implemented force: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Epistemic authority and scope: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Evidence source ID and local anchor: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Claim IDs or none: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Mismatch marker or none: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)
Gap/limit: see [EPI-RTE-pending-retention](#epi-rte-pending-retention)

Route ID: [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Content/update relation: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Transition or check target: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Evaluator/condition and domain: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Activation and timing: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Possible or observed result: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Implemented force: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Epistemic authority and scope: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Evidence source ID and local anchor: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Claim IDs or none: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Mismatch marker or none: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Gap/limit: see [EPI-RTE-review-disposition](#epi-rte-review-disposition)

Route ID: [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Content/update relation: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Transition or check target: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Evaluator/condition and domain: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Activation and timing: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Possible or observed result: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Implemented force: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Epistemic authority and scope: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Evidence source ID and local anchor: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Claim IDs or none: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Mismatch marker or none: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)
Gap/limit: see [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention)

Route ID: [EPI-RTE-query-selection](#epi-rte-query-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Content/update relation: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Transition or check target: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Evaluator/condition and domain: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Activation and timing: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Possible or observed result: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Implemented force: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Epistemic authority and scope: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Evidence source ID and local anchor: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Claim IDs or none: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Mismatch marker or none: see [EPI-RTE-query-selection](#epi-rte-query-selection)
Gap/limit: see [EPI-RTE-query-selection](#epi-rte-query-selection)

Route ID: [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Content/update relation: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Transition or check target: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Evaluator/condition and domain: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Activation and timing: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Possible or observed result: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Implemented force: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Epistemic authority and scope: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Evidence source ID and local anchor: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Claim IDs or none: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Mismatch marker or none: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)
Gap/limit: see [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement)

Route ID: [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Content/update relation: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Transition or check target: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Evaluator/condition and domain: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Activation and timing: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Possible or observed result: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Implemented force: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Epistemic authority and scope: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Evidence source ID and local anchor: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Claim IDs or none: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Mismatch marker or none: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)
Gap/limit: see [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement)

Route ID: [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Content/update relation: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Transition or check target: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Evaluator/condition and domain: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Activation and timing: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Possible or observed result: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Implemented force: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Epistemic authority and scope: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Evidence source ID and local anchor: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Claim IDs or none: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Mismatch marker or none: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)
Gap/limit: see [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap)

Route ID: [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-page-body](#epi-obj-page-body) and [EPI-OBJ-page-metadata](#epi-obj-page-metadata)
Content/update relation: no content change
Transition or check target: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Evaluator/condition and domain: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed) and shared lexical/structural check records
Activation and timing: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Possible or observed result: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Implemented force: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Epistemic authority and scope: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Evidence source ID and local anchor: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy) | see claim | see claim | see claim | [EPI-RTE-page-extraction](#epi-rte-page-extraction), [EPI-RTE-quote-location](#epi-rte-quote-location), [EPI-RTE-span-check](#epi-rte-span-check), [EPI-RTE-schema-check](#epi-rte-schema-check) | see records | see records | see records | see records |
| [RT-CLM-history-policy](runtime.md#rt-clm-history-policy) | see claim | see claim | see claim | [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention), [EPI-RTE-query-selection](#epi-rte-query-selection) | see records | see records | see records | see records |
| [EPI-CLM-faithfulness-support](#epi-clm-faithfulness-support) | see claim | see claim | see claim | [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement), [EPI-RTE-span-check](#epi-rte-span-check) | see records | see records | see records | see claim |
| [EPI-CLM-eval-gates](#epi-clm-eval-gates) | see claim | see claim | see claim | [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement), [EPI-RTE-review-disposition](#epi-rte-review-disposition) | see records | see records | see records | see claim |
| [EPI-CLM-provenance-trust](#epi-clm-provenance-trust) | see claim | see claim | see claim | [EPI-RTE-raw-import](#epi-rte-raw-import), [EPI-RTE-quote-location](#epi-rte-quote-location), [EPI-RTE-query-selection](#epi-rte-query-selection) | see records | see records | see records | see claim |

## Bounded conclusion

The inspected architecture acquires source text with unknown external warrant, requests source-faithful candidate pages, checks localized structural/lexical conditions and retains eligible candidates for review. Those functions do not establish the truth or semantic entailment of every assertion. Extraction's semantic relation remains indeterminate; requested non-ampliative extraction is not evidence that it occurred, and no generated non-entailment witness establishes produced conjecture. See [EPI-RTE-raw-import](#epi-rte-raw-import), [EPI-RTE-page-extraction](#epi-rte-page-extraction), [EPI-RTE-quote-location](#epi-rte-quote-location), [EPI-RTE-span-check](#epi-rte-span-check) and [EPI-RTE-schema-check](#epi-rte-schema-check).

Staging disposition, human review, seed writing and retained-store availability have different authority. Checks enforce eligibility for specific writes; the human CLI can veto or edit a file, but evidence-consuming truth acceptance with named criterion, intended use and scope is not established. Consequently neither typed links nor index rebuilds are classified here as lifecycle integration of accepted knowledge. Rejection removes a pending file, not raw evidence; same-ID replacement and stale retrieval constrain withdrawal/history claims. See [EPI-RTE-proposal-selection](#epi-rte-proposal-selection), [EPI-RTE-pending-retention](#epi-rte-pending-retention), [EPI-RTE-review-disposition](#epi-rte-review-disposition), [EPI-RTE-knowledge-retention](#epi-rte-knowledge-retention), [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed) and [EPI-RTE-query-selection](#epi-rte-query-selection).

The supported deterministic derivations are numerical measurements from declared input conventions, not new domain explanations. Search reshapes/indexes existing content and ranks identifiers; its source-ID output is less lineage detail than the Markdown store. Measurements license lexical-pass and dataset-label agreement claims only. Candidate-query generation can change later evaluation labels without independent semantic acceptance, including a caller-selected active-dataset path. No inspected automatic result consumer promotes a product change, revises extraction guidance, trains weights or turns metrics into truth endorsement. These are scoped consumer findings, not claims about provider learning or all manual development. See [EPI-RTE-query-selection](#epi-rte-query-selection), [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement), [EPI-RTE-retrieval-measurement](#epi-rte-retrieval-measurement) and [EPI-RTE-query-bootstrap](#epi-rte-query-bootstrap).

Validation-triggered escalation changes the current extraction choice without a retained policy update; scored variants alone establish no content-directed theory criticism. Improved future capacity, reflective self-representation, autonomous truth acceptance and exercised self-improvement are independently unestablished on these routes, rather than one inferred system-wide negative. Parameter opacity neither establishes nor refutes internal theory processing. No observed-run or causal evidence closes the later-use and benefit links. See [EPI-RTE-proposal-selection](#epi-rte-proposal-selection), [RT-RTE-eval-report](runtime.md#rt-rte-eval-report) and the separately scoped component records cited in the inventory.

## Shared records

### Operative objects

#### EPI-OBJ-raw-source
Label: Raw source documents

Candidate truth-apt content: External propositions over the input document's domain. Claimed role: Source evidence bytes. Source-native raw/<sha256>/source plus meta.json; natural-language document bytes on filesystem, symbolic hash/origin metadata. Distinct from model parameters and page propositions; no supplied operative-object counterpart. Closest container is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Hash names content, not warrant. Quote support and source credibility remain separate.

Evidence: SRC-1, `src/wiki/ingest/hashing.py`; implementation / candidate-artifact evidence as applicable. Gap/limit: External truth and actual stored raw bytes unavailable.

> (raw_dir / stored_name).write_bytes(data)
> --- `src/wiki/ingest/hashing.py`

#### EPI-OBJ-page-body
Label: Proposed and retained page body

Candidate truth-apt content: Historical/domain assertions. Claimed role: Source-attributed candidate claims. Source-native RawExtractedPage.body / PageRecord.body; natural-language Markdown on pending/knowledge files. Distinct operative part from typed metadata. Candidate instance states Ada Lovelace was a nineteenth-century English mathematician, among other claims; citations alone do not establish their truth. Closest containers are [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-page-review](runtime.md#rt-rte-page-review); this object spans proposal and retained phases rather than duplicating either route.

Evidence: SRC-1, `knowledge/entities/ada-lovelace.md`; implementation / candidate-artifact evidence as applicable. Gap/limit: Artifact provenance does not prove execution/acceptance.

> Ada Lovelace was a nineteenth-century English mathematician. [^src:1]
> --- `knowledge/entities/ada-lovelace.md`

#### EPI-OBJ-page-metadata
Label: Page fields, sources and relations

Candidate truth-apt content: Definitions/relations plus lineage assertions. Claimed role: Typing, lineage and selection. Source-native fields/frontmatter/sources: symbolic IDs, source offsets, timestamps, supersession links and typed edges in YAML on files, plus natural-language definition/aliases used as search text. Split from body because checks and consumers differ; schema validates shapes while graph/loaders consume metadata operationally. No supplied object counterpart; overlaps the same multi-route containers as page-body. Content of generated definitions/relations is unobserved.

Evidence: SRC-1, `src/wiki/ingest/pipeline.py`; implementation / candidate-artifact evidence as applicable. Gap/limit: Lexical body checks do not check every prose field.

> "superseded_by": None,
> "supersedes": fields.pop("supersedes", []),
> "related": fields.pop("related", []),
> --- `src/wiki/ingest/pipeline.py`

#### EPI-OBJ-query-labels
Label: Queries and expected page IDs

Candidate truth-apt content: Candidate relevance assertions. Claimed role: Evaluation reference answers. Source-native query / expected_page_ids / query_type in JSONL. Query text is natural-language request (not necessarily truth-apt); expected-ID association is symbolic relevance assertion consumed as binary oracle. Filesystem active or bootstrap dataset. No supplied object counterpart; spans [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap) and [RT-RTE-eval-report](runtime.md#rt-rte-eval-report), so not a part of exactly one container.

Evidence: SRC-1, `src/wiki/cli/__init__.py`; implementation / candidate-artifact evidence as applicable. Gap/limit: Model-generated labels not independently verified.

> if line:
>     fh.write(_json.dumps({"query": line, "expected_page_ids": [path.stem],
>                           "query_type": "lookup"}) + "\n")
>     n += 1
> --- `src/wiki/cli/__init__.py`

#### EPI-OBJ-eval-results
Label: Evaluation metrics and reports

Part of: [RT-RTE-eval-report](runtime.md#rt-rte-eval-report)

The object is the material measurement output of that route, hence its parent is a route rather than an object.

Candidate truth-apt content: Bounded numerical measurement claims. Claimed role: Operator assessment. Source-native result / overall / by_type / per_query; symbolic numerical summaries and natural-language Markdown rendering on baseline JSON/Markdown; ingest measurement only stdout. No supplied operative-object counterpart; material measurement output of [RT-RTE-eval-report](runtime.md#rt-rte-eval-report), not a second route.

Evidence: SRC-1, `src/wiki/eval/harness.py`; implementation / candidate-artifact evidence as applicable. Gap/limit: No automatic admission or causal license.

> "n": len(dataset),
> "overall": aggregate(per_query),
> --- `src/wiki/eval/harness.py`

### Routes

#### EPI-RTE-raw-import
Label: Raw source import

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This is the material content transformation function within the supplied container, not a replacement for that container. 

Object/candidate ID: [EPI-OBJ-raw-source](#epi-obj-raw-source)

Content/update relation: truth-apt transformation: acquisition/import

Transition or check target: External document bytes enter the raw store

Evaluator/condition and domain: SHA-256 addresses bytes; no source-truth evaluator

Activation and timing: Operator ingest, before extraction

Possible or observed result: Source bytes plus origin/hash sidecar

Implemented force: Enforcing storage identity, not endorsement

Epistemic authority and scope: Source warrant unknown; byte retention preserves an evidence reference, not its truth

Operational authority: behavior permitted, blocked, or changed: Makes raw text available for extraction and lexical checking

Behavioral-authority path: consumer, channel, force, horizon: Pipeline and checker; file read; permissive; later ingests/evaluations

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: UTF-8 decoding can fail; loader does not rehash retained bytes.

Evidence source ID and local anchor: SRC-1, `src/wiki/ingest/hashing.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Source ID and raw directory
- Later read-back: Stored bytes are reloaded by pipeline and ingest evaluation
- Delegated visibility: Selected text later reaches extractor; raw writer makes no delegation
- Selection predicate: Operator-selected file; existing meta.json suppresses a rewrite
- Invalidation or expiry: No expiry; existing hash directory reused
- Activation or effect: Raw persistence wired; use unobserved
- Evidence limits: UTF-8 decoding can fail; loader does not rehash retained bytes.

> data = source_path.read_bytes()
> sha = sha256_hex(data)
> --- `src/wiki/ingest/hashing.py`

#### EPI-RTE-page-extraction
Label: Source-conditioned page proposal

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This is the material content transformation function within the supplied container, not a replacement for that container. The model proposes; Python advances and can reject. Open document extraction has no expected-answer oracle. Prompt forbids outside knowledge and requests citations. Static instructions are guidance, not a formulated content-directed criticism loop. Provider internals are opaque; parameter/fixity limits remain in [RT-CMP-haiku-extractor](runtime.md#rt-cmp-haiku-extractor) and [RT-CMP-sonnet-extractor](runtime.md#rt-cmp-sonnet-extractor).

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: truth-apt transformation: indeterminate

Transition or check target: Source chunk to proposed claims, definitions, edges and quotes

Evaluator/condition and domain: Anthropic generation under root instructions; no independent semantic judge

Activation and timing: Each chunk and, after failed checks, alternate extractor

Possible or observed result: RawExtractedPage values

Implemented force: Advisory proposal, not retained-store admission

Epistemic authority and scope: Requested faithful extraction; whether each generated statement preserves source meaning is not determinable without outputs and semantic comparison

Operational authority: behavior permitted, blocked, or changed: Supplies candidates to construction and checks

Behavioral-authority path: consumer, channel, force, horizon: Pipeline via propose_pages tool payload; permissive; current chunk

Claim IDs or none: [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy)

Mismatch marker or none: Requested fidelity does not establish reliable semantic preservation

Gap/limit: Import of document is acquisition; generation may reshape or introduce unsupported propositions. No non-entailment witness for a generated candidate is supplied, so ampliative conjecture is not established.

Evidence source ID and local anchor: SRC-1, `src/wiki/extract.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured proposal list with usage
- Later read-back: Valid descendants may persist in pending and knowledge; no extraction transcript retained here
- Delegated visibility: Source chunk, source ID/offset, root instructions and tool schema; not existing corpus
- Selection predicate: First matching propose_pages tool block
- Invalidation or expiry: Next attempt can replace current attempt; pending same-ID writes can overwrite
- Activation or effect: Proposal delivery wired; compliance and activation unobserved
- Evidence limits: Import of document is acquisition; generation may reshape or introduce unsupported propositions. No non-entailment witness for a generated candidate is supplied, so ampliative conjecture is not established.



#### EPI-RTE-quote-location
Label: Quote location and lineage construction

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This is the material check/evidence production function within the supplied container, not a replacement for that container. 

Object/candidate ID: [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: no content change

Transition or check target: Each proposed quote against complete decoded source text

Evaluator/condition and domain: Exact substring, else rapidfuzz partial alignment at minimum 85

Activation and timing: Before schema and marked-claim checks

Possible or observed result: Offsets and score, or issue and zero span

Implemented force: Enforcing input to page validity

Epistemic authority and scope: Locates matching text only; fuzzy match is not exact quotation and neither establishes source truth or claim support

Operational authority: behavior permitted, blocked, or changed: Unlocated quote makes candidate invalid; offsets become retained source references

Behavioral-authority path: consumer, channel, force, horizon: build_page to issue list and sources array; enforcing; current proposal and later source lookup

Claim IDs or none: [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy)

Mismatch marker or none: Lineage metadata is not truth endorsement

Gap/limit: Duplicate source quotes select first exact occurrence; no adjudication of surrounding context

Evidence source ID and local anchor: SRC-1, `src/wiki/ingest/pipeline.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Located offsets or None
- Later read-back: Derived offsets persist with staged/retained page
- Delegated visibility: inapplicable — deterministic host computation
- Selection predicate: Every supplied quote, not every substantive assertion
- Invalidation or expiry: Recomputed on new build; no automatic recheck on edited acceptance
- Activation or effect: Validity input wired; no run supplied
- Evidence limits: Duplicate source quotes select first exact occurrence; no adjudication of surrounding context

> idx = source_text.find(quote)
> if idx >= 0:
>     return idx, idx + len(quote), 100.0
> --- `src/wiki/ingest/pipeline.py`

#### EPI-RTE-schema-check
Label: Structural page validation

This structural evaluator spans [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed), the optional commit step of [RT-RTE-page-review](runtime.md#rt-rte-page-review), and standalone validation. It is not contained in exactly one supplied route. It identifies the shared check and its distinct invocation consumers, not another end-to-end admission route. Additional entry points compared with runtime: validate and validate-all report structural results; scripts/pre-commit selects staged namespace filenames but validates working-tree files. It invokes the same CLI, not check_page_spans. A failing hook blocks commit only if installed and invoked. The CLI exposes no automatic repair or withdrawal on a failed standalone check (SRC-1, `src/wiki/cli/__init__.py`, `scripts/pre-commit`).

Object/candidate ID: [EPI-OBJ-page-metadata](#epi-obj-page-metadata); [EPI-OBJ-page-body](#epi-obj-page-body)

Content/update relation: no content change

Transition or check target: Frontmatter against namespace schema and existing citation indexes

Evaluator/condition and domain: JSON Schema/format checks plus footnote-index loop; structural domain

Activation and timing: Ingest and seed prewrite; standalone validate/validate-all; optional installed pre-commit hook

Possible or observed result: Issue list; CLI success/failure exit

Implemented force: Enforcing within ingest/seed and installed commit hook; reporting in standalone CLI

Epistemic authority and scope: Schema conformity and reference bounds, not truth or complete citation coverage

Operational authority: behavior permitted, blocked, or changed: Issues block staging/seed writes; hook failure blocks commit after review move, not that move

Behavioral-authority path: consumer, channel, force, horizon: Pipeline/seed via issue list; Git via hook exit; enforcing; one build or commit

Claim IDs or none: [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy)

Mismatch marker or none: Unknown fields and invalid markers can fail while unmarked false text is outside body check

Gap/limit: Effective individual schema constraints supplied by runtime/boundary; this inspection does not re-audit all YAML contracts

Evidence source ID and local anchor: SRC-1, `src/wiki/validate.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Issues or CLI exit
- Later read-back: Standalone validation retains no changed claim; hook and ingest outputs may be recorded elsewhere
- Delegated visibility: inapplicable — no model call
- Selection predicate: Parsed namespace; only existing citation markers enumerated
- Invalidation or expiry: No cached approval; later edits can bypass earlier result
- Activation or effect: Structural check and hook dispatch wired, installation unobserved
- Evidence limits: Effective individual schema constraints supplied by runtime/boundary; this inspection does not re-audit all YAML contracts

> for m in _FOOTNOTE_RE.finditer(body):
>     n = int(m.group(1))
> --- `src/wiki/validate.py`

#### EPI-RTE-span-check
Label: Marked-claim lexical support check

This lexical evaluator spans [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed) and [RT-RTE-eval-report](runtime.md#rt-rte-eval-report). It is not contained in exactly one supplied route. It identifies the shared check and distinguishes its admission and measurement consumers rather than duplicating their end-to-end routes. 

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: no content change

Transition or check target: Fragment before each citation against the addressed raw slice

Evaluator/condition and domain: Index/text/bounds/nonempty checks then token_set_ratio threshold; lexical domain

Activation and timing: Ingest/seed construction; reused by faithfulness metric

Possible or observed result: Issue strings or empty list

Implemented force: Enforcing input to staging/seed; measurement input in evaluation

Epistemic authority and scope: Lexical overlap within checked fragments only; does not license entailment, negation handling or source truth

Operational authority: behavior permitted, blocked, or changed: Low overlap prevents staging/seed admission; failures can trigger alternate extraction

Behavioral-authority path: consumer, channel, force, horizon: Page validity and faithfulness; issue list; enforcing or reporting by consumer; current candidate

Claim IDs or none: [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy); [EPI-CLM-faithfulness-support](#epi-clm-faithfulness-support)

Mismatch marker or none: Semantic support claim exceeds lexical evaluator

Gap/limit: Unmarked sentences and namespace-specific prose metadata are not enumerated by the body loop

Evidence source ID and local anchor: SRC-1, `src/wiki/ingest/spancheck.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of issues
- Later read-back: Issues influence manifest rejection; not fed as critique into retry prompt
- Delegated visibility: inapplicable — local lexical procedure
- Selection predicate: Only extract_claims matches
- Invalidation or expiry: Recomputed on ingestion/evaluation; edited review not rechecked
- Activation or effect: Check wiring established, true-positive/false-positive rates unobserved
- Evidence limits: Unmarked sentences and namespace-specific prose metadata are not enumerated by the body loop

> span_text = full_text[start:end]
> score = token_set_ratio(claim, span_text)
> --- `src/wiki/ingest/spancheck.py`

#### EPI-RTE-proposal-selection
Label: Retry, deduplication and staging eligibility

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This is the material disposition/acceptance function within the supplied container, not a replacement for that container. Model proposes, software decides and vetoes, no human per-candidate decision here. Mode is open ingestion, not fixed-answer experimentation; lexical source spans are a reference rather than truth oracle. Failure triggers fresh alternate-model generation, not instruction/parameter revision. No transactional rollback of prior raw writes.

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: no content change

Transition or check target: Candidate sets for current chunk and per-ID staging eligibility

Evaluator/condition and domain: Python nonempty/all-valid predicate, last attempt fallback, first-ID dedupe and page.is_valid

Activation and timing: After each extractor result and after all chunks

Possible or observed result: Retry, valid candidate selected, invalid candidate rejected, duplicate suppressed

Implemented force: Enforcing staging disposition, not epistemic acceptance

Epistemic authority and scope: Eligibility under structural/lexical criteria for pending review only; no named truth acceptance decision

Operational authority: behavior permitted, blocked, or changed: Validation failure can switch to stronger model; only issue-free deduped pages can be staged

Behavioral-authority path: consumer, channel, force, horizon: Pipeline via conditions; enforcing; current ingest

Claim IDs or none: none

Mismatch marker or none: Manifest accepted means pending, not knowledge acceptance

Gap/limit: First duplicate can suppress a later better candidate; no content-level comparison of duplicates

Evidence source ID and local anchor: SRC-1, `src/wiki/ingest/pipeline.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected candidates and manifest disposition
- Later read-back: Manifest records reasons; no consumer automatically learns a policy from them
- Delegated visibility: Same selected input/instructions to retry, not explicit first-attempt critique
- Selection predicate: First all-valid set, otherwise last set; first ID across chunks
- Invalidation or expiry: Later ingest replaces same manifest/pending name
- Activation or effect: Deterministic selection wired; route operation unobserved
- Evidence limits: First duplicate can suppress a later better candidate; no content-level comparison of duplicates



#### EPI-RTE-pending-retention
Label: Pending page and manifest retention

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This is the material retention function within the supplied container, not a replacement for that container. 

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: no content change

Transition or check target: Selected candidate values to pending files

Evaluator/condition and domain: Software serialization; eligibility see [EPI-RTE-proposal-selection](#epi-rte-proposal-selection)

Activation and timing: After selection

Possible or observed result: Pending Markdown and manifest

Implemented force: Permissive retention before epistemic acceptance

Epistemic authority and scope: No additional epistemic license from writing

Operational authority: behavior permitted, blocked, or changed: Makes candidates available to review

Behavioral-authority path: consumer, channel, force, horizon: Review via sorted pending Markdown; permissive; across invocations

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: No claim that persisted proposals were checked in an actual run

Evidence source ID and local anchor: SRC-1, `src/wiki/ingest/pipeline.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Manifest
- Later read-back: Pending Markdown to review; source manifest not a review gate
- Delegated visibility: Human preview/editor later receives file
- Selection predicate: Only valid first-ID proposals
- Invalidation or expiry: Accept moves; reject deletes; same-ID ingest overwrites; no expiry
- Activation or effect: Retention wired; no pending instance supplied
- Evidence limits: No claim that persisted proposals were checked in an actual run



#### EPI-RTE-review-disposition
Label: Human decision and page deletion

Part of: [RT-RTE-page-review](runtime.md#rt-rte-page-review)

This is the material disposition/acceptance function within the supplied container, not a replacement for that container. Human can propose edits and veto in interactive mode; Python routes the chosen action. No software answer oracle or epistemic criterion; guidance is extraction doctrine, not automatically reapplied. Open review, not a bounded experiment. Changed files persist or are deleted; Git recovery depends on successful commits. A body-difference flag from diff_page is advisory rather than semantic contradiction adjudication (SRC-1, `src/wiki/ingest/diff.py`).

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: no content change

Transition or check target: Pending file for retain/replace, reject, skip or quit

Evaluator/condition and domain: Human prompt decision; callable accept/reject has no proof of human decision

Activation and timing: After 800-character preview and optional editor

Possible or observed result: Accept invokes move; reject unlinks; skip retains candidate

Implemented force: Enforcing human protocol on CLI; permissive public callable

Epistemic authority and scope: Operational approval recorded, but criterion/intended-use/evidence-consuming truth judgment not enforced or supplied

Operational authority: behavior permitted, blocked, or changed: Allows file retention/replacement or deletes candidate; rejection leaves raw source and manifests

Behavioral-authority path: consumer, channel, force, horizon: CLI human response to accept_page/reject_page; enforcing on interactive path; one file

Claim IDs or none: [RT-CLM-history-policy](runtime.md#rt-clm-history-policy)

Mismatch marker or none: Admission does not revalidate edits or automatically preserve superseded content

Gap/limit: Human may inspect evidence externally, but that judgment is unobserved

Evidence source ID and local anchor: SRC-1, `src/wiki/review.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Destination or rejection status
- Later read-back: Accepted files reach loader; rejected file has no later read-back; raw evidence remains
- Delegated visibility: Human gets preview or editor file, not automatically full raw sources
- Selection predicate: Sorted pending files and human response; callable path bypasses prompt
- Invalidation or expiry: Move/delete; no automatic rollback after failed commit
- Activation or effect: Disposition wiring established; no exercised acceptance established
- Evidence limits: Human may inspect evidence externally, but that judgment is unobserved



#### EPI-RTE-knowledge-retention
Label: Retained page move

Part of: [RT-RTE-page-review](runtime.md#rt-rte-page-review)

This is the material retention function within the supplied container, not a replacement for that container. 

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: no content change

Transition or check target: Pending page to namespace file

Evaluator/condition and domain: Parsed type membership, then Path.replace; not schema/span checks

Activation and timing: After CLI accept or direct accept_page invocation

Possible or observed result: Knowledge file can replace same-name destination

Implemented force: Permissive retained-store use

Epistemic authority and scope: Retained availability, not evidence-consuming acceptance or lifecycle integration

Operational authority: behavior permitted, blocked, or changed: Future loads see moved content; Git optional and after move

Behavioral-authority path: consumer, channel, force, horizon: load_pages/rebuild/query/bootstrap/evaluation via namespace files; permissive; cross-invocation

Claim IDs or none: [RT-CLM-history-policy](runtime.md#rt-clm-history-policy)

Mismatch marker or none: Same-name replacement contradicts an unconditional old-pages-stay invariant

Gap/limit: Seed alternate is separately covered by [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed); seed checks before direct write but no per-page human gate

Evidence source ID and local anchor: SRC-1, `src/wiki/review.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Destination path
- Later read-back: Namespace Markdown feeds all later consumers
- Delegated visibility: inapplicable — move itself delegates no interpretation
- Selection predicate: Namespace membership and supplied filename
- Invalidation or expiry: Replacement possible; no TTL or automatic reciprocal supersession update
- Activation or effect: Persistence wired; Git history and actual reuse unobserved
- Evidence limits: Seed alternate is separately covered by [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed); seed checks before direct write but no per-page human gate



#### EPI-RTE-query-selection
Label: Current-page loading and ranked identifier delivery

Part of: [RT-RTE-index-query](runtime.md#rt-rte-index-query)

This is the material operational admission/selection/consumption function within the supplied container, not a replacement for that container. Concrete deterministic reshaping: a PageRecord with id ada-lovelace, body B, aliases [Augusta Ada King], and no tags/parents/definition yields search_text equal to "ada lovelace B Augusta Ada King". The code replaces hyphens in the id, appends body and selected metadata and joins with spaces. This is indexing text, not a derived historical proposition. Separately, rrf({bm25: [ada-lovelace]}) produces that ID with score 1/61 and source list [bm25], directly from the inspected enumerate/add formula. These are deductions from implementation, not target executions (SRC-1, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/fusion.py`). Query strips lineage to source IDs; full source spans remain in Markdown, not in returned dictionaries. Optional-model fixity and opaque state remain as scoped in [RT-CMP-dense-embedding](runtime.md#rt-cmp-dense-embedding) and [RT-CMP-cross-encoder](runtime.md#rt-cmp-cross-encoder).

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-page-metadata](#epi-obj-page-metadata)

Content/update relation: truth-apt transformation: non-ampliative reshaping

Transition or check target: Retained page representations to search text, indexes and selected IDs

Evaluator/condition and domain: BM25, graph, optional embedding ranks; RRF; optional cross-encoder; relevance not truth domain

Activation and timing: Explicit rebuild then later query; not automatic on admission

Possible or observed result: IDs, scores, contributing paths and source-ID lists; no generated answer

Implemented force: Ranking and permissive delivery; no semantic endorsement

Epistemic authority and scope: Relevance ordering only; no new domain claim or acceptance license

Operational authority: behavior permitted, blocked, or changed: Changes what operator/evaluator sees first; superseded pages excluded on load but stale fused IDs can escape

Behavioral-authority path: consumer, channel, force, horizon: CLI/evaluator via result dictionaries and IDs; ranking; current query and persistent indexes

Claim IDs or none: [RT-CLM-history-policy](runtime.md#rt-clm-history-policy)

Mismatch marker or none: Current-page filter is not universal output withdrawal; provenance omits spans/extractor/time

Gap/limit: A downstream agent consumer is not implemented; freshness does not establish endorsement

Evidence source ID and local anchor: SRC-1, `src/wiki/retrieve/query.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked dictionaries
- Later read-back: Index state reused by later queries; query writes no retained answer
- Delegated visibility: Optional models see search text/query; downstream agent not supplied
- Selection predicate: Enabled components and top-k; active rerank filters IDs against current pages
- Invalidation or expiry: Explicit rebuild; query lacks hash/freshness check
- Activation or effect: Selection wired; answer effects unobserved
- Evidence limits: A downstream agent consumer is not implemented; freshness does not establish endorsement

> return " ".join(parts)
> --- `src/wiki/retrieve/store.py`

#### EPI-RTE-ingest-measurement
Label: Faithfulness measurement

Part of: [RT-RTE-eval-report](runtime.md#rt-rte-eval-report)

This is the material check/evidence production function within the supplied container, not a replacement for that container. Concrete countercase, deduced without execution: body "The Moon is made of cheese." contains no citation marker. extract_claims returns []; faithfulness therefore returns 1.0 for any sources/texts. The function does not inspect the truth of that sentence. This falsifies interpreting its maximum as semantic faithfulness for every body assertion; it does not falsify the narrower marked-claim statistic. For footnoted claims the statistic is max(0, round(1 - issue_count/claim_count, 4)); source truth remains an unchecked premise (SRC-1, `src/wiki/ingest/spancheck.py`, `src/wiki/eval/ingest_eval.py`).

Object/candidate ID: [EPI-OBJ-page-body](#epi-obj-page-body); [EPI-OBJ-eval-results](#epi-obj-eval-results)

Content/update relation: truth-apt transformation: entailed derivation

Transition or check target: Marked claims on retained pages with available raw text

Evaluator/condition and domain: Ratio derived from extract_claims count and span-check issues; lexical-domain statistic

Activation and timing: Explicit wiki eval ingest

Possible or observed result: Per-page number and mean over included pages

Implemented force: Advisory reporting only

Epistemic authority and scope: Entails the implemented lexical-pass statistic conditional on parsed inputs; not fraction of true or semantically supported claims

Operational authority: behavior permitted, blocked, or changed: Prints metric; no implemented automatic promotion, repair or withdrawal

Behavioral-authority path: consumer, channel, force, horizon: Operator via CLI stdout; advisory; one evaluation

Claim IDs or none: [EPI-CLM-faithfulness-support](#epi-clm-faithfulness-support)

Mismatch marker or none: Name/docstring implies support beyond implemented check

Gap/limit: Missing raw files skip pages; no claims returns 1.0; mean is subset-dependent

Evidence source ID and local anchor: SRC-1, `src/wiki/eval/ingest_eval.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Page score and aggregate stdout
- Later read-back: inapplicable — CLI does not persist this measurement or automatically consume it later
- Delegated visibility: inapplicable — no model judge
- Selection predicate: Namespace files with sources and loadable raw documents; not current-page filter
- Invalidation or expiry: Fresh computation only; no retained approval
- Activation or effect: Measurement wired; observed scores and semantic accuracy unestablished
- Evidence limits: Missing raw files skip pages; no claims returns 1.0; mean is subset-dependent

> claims = extract_claims(body)
> if not claims:
>     return 1.0
> --- `src/wiki/eval/ingest_eval.py`

#### EPI-RTE-retrieval-measurement
Label: Retrieval agreement and component reporting

Part of: [RT-RTE-eval-report](runtime.md#rt-rte-eval-report)

This is the material check/evidence production function within the supplied container, not a replacement for that container. Expected IDs are supplied reference answers, not independent factual adjudication. Metrics derive propositions about ranks and those labels through inspected arithmetic (SRC-1, `src/wiki/eval/metrics.py`). Components command varies complete adapters under one dataset, but aliases/fallback availability and source-only evidence do not establish independent component effects. No empirical improvement or transfer follows.

Object/candidate ID: [EPI-OBJ-query-labels](#epi-obj-query-labels); [EPI-OBJ-eval-results](#epi-obj-eval-results)

Content/update relation: truth-apt transformation: entailed derivation

Transition or check target: Ranked IDs compared to expected_page_ids on current dataset

Evaluator/condition and domain: Deterministic binary relevance NDCG/MRR/recall and means; dataset-label domain

Activation and timing: Explicit retrieval/components commands

Possible or observed result: Per-query/aggregate report and component delta; optional saved snapshots

Implemented force: Advisory; no product-change gate

Epistemic authority and scope: Label agreement for specified corpus/query/adapters, not answer truth, generalization or isolated causal component benefit

Operational authority: behavior permitted, blocked, or changed: Saves reports for operator; does not automatically change retrieval or content

Behavioral-authority path: consumer, channel, force, horizon: Operator via stdout and baseline files; advisory; across invocations when manually read

Claim IDs or none: [EPI-CLM-eval-gates](#epi-clm-eval-gates)

Mismatch marker or none: README gate claim versus explicit reporting-only implementation

Gap/limit: Dataset labels and current component availability constrain comparisons; implementation is not reproduced experiment

Evidence source ID and local anchor: SRC-1, `src/wiki/eval/harness.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Metrics and optional saved JSON/Markdown
- Later read-back: Reports retained; no inspected automatic adoption consumer
- Delegated visibility: Adapters receive query; optional model inputs as in query selection
- Selection predicate: Nonempty JSONL rows; expected IDs supplied as oracle
- Invalidation or expiry: Latest named report overwritten, timestamped snapshots retained
- Activation or effect: Report route wired; causal advantage unobserved
- Evidence limits: Dataset labels and current component availability constrain comparisons; implementation is not reproduced experiment

> rel = set(q["expected_page_ids"])
> --- `src/wiki/eval/harness.py`

#### EPI-RTE-query-bootstrap
Label: Generated evaluation queries and automatic labels

Part of: [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap)

This is the material content transformation function within the supplied container, not a replacement for that container. Model proposes queries; software assigns labels and writes; human review is requested, not enforced. Open per-page query generation has no answer oracle for label correctness. Starting command is not per-row human approval. No ingest instructions or cost guard; no automatic rollback or learning from earlier metric results.

Object/candidate ID: [EPI-OBJ-query-labels](#epi-obj-query-labels)

Content/update relation: truth-apt transformation: indeterminate

Transition or check target: Retained body to candidate query plus assertion that current page is expected answer

Evaluator/condition and domain: Model generation then filename-derived expected_page_ids; no semantic label check

Activation and timing: Explicit bootstrap command, every namespace page including superseded

Possible or observed result: Candidate JSONL rows at caller-selected output

Implemented force: Permissive dataset write, intended human-review protocol

Epistemic authority and scope: Candidate relevance assertion only; semantic correctness and entailment not established

Operational authority: behavior permitted, blocked, or changed: Default output awaits merge; selected active-dataset output can directly reach evaluator

Behavioral-authority path: consumer, channel, force, horizon: Harness via JSONL expected IDs; permissive; later evaluation

Claim IDs or none: none

Mismatch marker or none: Review reminder does not enforce separate active-data admission

Gap/limit: Query itself need not be truth-apt, but associated relevance label is; no generated example establishes ampliation

Evidence source ID and local anchor: SRC-1, `src/wiki/cli/__init__.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate count and output file
- Later read-back: Later harness can consume rows if merged or written to active dataset
- Delegated visibility: Model receives body and query-generation instruction, not full source evidence
- Selection predicate: All nonempty response lines; labels always current filename; no superseded filter
- Invalidation or expiry: Output truncated on invocation; partial writes may survive failure
- Activation or effect: Writing wired; label validity, human merge and later use unobserved
- Evidence limits: Query itself need not be truth-apt, but associated relevance label is; no generated example establishes ampliation



### Claims

#### EPI-CLM-faithfulness-support
Label: Faithfulness as source support

Claimed operation: ingest metric describes the fraction of footnoted claims whose spans actually support them. SRC-1, `src/wiki/eval/ingest_eval.py`; doctrine/design docstring, not run evidence. Distinct from [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy): this concerns a reported numerical evaluator, not extraction instructions. The implemented lexical statistic and no-marker countercase are owned by [EPI-RTE-ingest-measurement](#epi-rte-ingest-measurement); [EPI-RTE-span-check](#epi-rte-span-check) bounds support to token overlap. No observed or causal validation of semantic-support accuracy is supplied.

> faithfulness — fraction of footnoted claims whose cited span actually supports
> the claim (reuses the span-check; no LLM needed).
> --- `src/wiki/eval/ingest_eval.py`

#### EPI-CLM-eval-gates
Label: Evaluation-gated changes

Claimed operation: retrieval and ingest changes require metric deltas and an autonomous write route proceeds through an eval gate. SRC-1, `README.md`; doctrine/design. No counterpart after comparison with supplied runtime Claims; closest route is [RT-RTE-eval-report](runtime.md#rt-rte-eval-report). Implemented reporting does not itself enforce such a development/promotion gate. CLI review is a human choice, seed writes are directly checked, and no inspected CLI operation automatically accepts knowledge based on reported deltas. This is not a claim that an external maintainer cannot voluntarily require them. Run and causal support for the stronger gate are missing.

> - **Evals gate changes.** No retrieval change ships without an NDCG/MRR delta;
>   no ingest change without a faithfulness delta (Phase 2).
> --- `README.md`

> typer.echo("(gate relaxed for toy corpus — reporting only)")
> --- `src/wiki/cli/__init__.py`

#### EPI-CLM-provenance-trust
Label: Reconstruct trust from provenance

Claimed operation: trust is reconstructed on demand from source identity, span, extraction time and extractor, without numeric confidence. SRC-1, `README.md`; doctrine/design. Closest supplied claim [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy) concerns generation coverage and invention; this distinct claim concerns later reliance on a lineage chain. Metadata retention and source-byte access afford inspection, but [EPI-RTE-query-selection](#epi-rte-query-selection) returns source IDs only. No inspected query consumer reconstructs endorsement or source truth; full manual reconstruction also needs unavailable retained raw bodies. Retrieval relevance scores are not stored numeric confidence about claim truth. No observed-run or causal trust benefit follows.

> - **No numeric confidence scores.** Trust is reconstructed on demand from a
>   **provenance chain** — `source_id`, `span`, `extracted_at`, `extractor` —
>   never stored as a float.
> --- `README.md`
