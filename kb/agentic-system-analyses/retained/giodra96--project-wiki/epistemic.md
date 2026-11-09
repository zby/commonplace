---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Project Wiki epistemic routes: source provenance, semantic admission, structural checks and later project reliance."
run-id: AAS-2026-11-08-project-wiki-b055e5c71dc7-01
reviewed-boundary: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
---

# Project Wiki epistemic report

## Source-and-claim boundary

The question is how Project Wiki turns source documents, explicit project intent, code observations and agent answers into material later coding agents rely on, and what its checks actually license. Scope and exclusions are those in [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). All source anchors below use SRC-1 at the frozen commit. The target is an instruction-based skill plus deterministic helpers, not its unspecified host model/runtime.

Direct inspection here covers the skill dispatcher, semantic workflow bodies, requirement templates, extraction/chunking, review command dispatch and transformations, optional skip diagnostics, structural validator progression and integrated evidence checks, inbox classification, contract-check dispatch and CI. These add depth to the supplied runtime, not a new source. Source files were read only; no target code, tests, fixtures or examples were executed.

| Entry point or operation | Source path (SRC-1) | Coverage and record citations |
| --- | --- | --- |
| Explicit task routing and automatic triggers | `SKILL.md` | Direct full read; [RT-OBJ-skill](runtime.md#rt-obj-skill), [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle). No central runtime dispatcher or registered model tools are supplied by this skill. |
| init / scan, generated instruction installation | `references/initialization-workflows.md` | Direct full procedure read; helper internals from supplied [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki); host model interpretation not inspected. |
| Notes / answers | `references/update-workflows.md`, `references/common-policies.md` | Direct full reads; [RT-RTE-note-update](runtime.md#rt-rte-note-update). Includes answer filing, OQ reconciliation, CR/ADR creation and audit logging. |
| Inbox process/skip/review and quarantine | `scripts/check_inbox.py`, `references/source-inbox.md` | Direct classifier and reason-to-action read; remaining control flow supplied by [RT-RTE-source-intake](runtime.md#rt-rte-source-intake). Byte/hash decisions are not source-authority judgments. |
| Extraction, chunk generation and source hash checks | `scripts/ingest_document.py` | Direct format dispatch, normalization/chunking, wrappers and main admission ranges; [EPI-RTE-extract-source](#epi-rte-extract-source). Dependency internals uninspected: prevents format-wide semantic-fidelity guarantee. |
| status / inspect / view / apply / audit | `scripts/review_progress.py` | Direct CLI branch, view selection/output, apply, state validation and audit construction; [EPI-RTE-ledger-check](#epi-rte-ledger-check). Structural progress is not proof of review. |
| Optional audit-skips | `scripts/review_progress.py` | Direct signal/run-output construction and dispatch; [EPI-RTE-skip-audit](#epi-rte-skip-audit); possible diagnostic rereading, no mandatory veto. |
| Document comparison, direct versus blocking review, finalization and rejection | `references/document-ingestion.md` | Direct full substantive procedure; [EPI-RTE-content-compare](#epi-rte-content-compare), [EPI-RTE-content-admit](#epi-rte-content-admit), [EPI-RTE-canonical-retain](#epi-rte-canonical-retain), [EPI-RTE-canonical-link](#epi-rte-canonical-link). |
| maintain / structural validation / semantic lint / migration / alerts | `references/maintenance-workflows.md`, `scripts/validate_wiki.py` | Direct full procedure, validator dispatch/run pipeline, integrated ledger/evidence checks; [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-semantic-lint](#epi-rte-semantic-lint), [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw). Other validator routines supplied at overview depth, not individually re-audited here. |
| sync and automatic source reconciliation | `references/synchronization-workflow.md`, `references/automatic-workflows.md` | Direct full reads; [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile), [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle). Source-scope helper mechanics from runtime, not a new sandbox claim. |
| config / help / protocol refresh | `scripts/wiki_config.py`, `scripts/wiki_help.py`, `assets/core-templates.md` | Supplied runtime only: [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle), [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol). Preference admission and static guide do not validate project facts. |
| Contract drift and CI | `scripts/check_contracts.py`, `.github/workflows/tests.yml` | Direct dispatcher/check-family and full CI read; [EPI-CLM-provenance-rule](#epi-clm-provenance-rule) records bounded evaluator contrast. Detailed contract checks and test assertions not all independently inspected here; no success trace or semantic benchmark supplied. |

Claims assessed are [RT-CLM-project-memory](runtime.md#rt-clm-project-memory), [EPI-CLM-provenance-rule](#epi-clm-provenance-rule) and [EPI-CLM-active-governance](#epi-clm-active-governance). No system-complete negative about possible model reasoning follows from this coverage. Available but uninspected helper/test details remain uninspected, not absent evidence. Missing populated project artifacts prevent individuating actual generated claims and recorded acceptances. Missing host traces prevent establishing instruction loading, semantic judgment, later reliance or automatic activation. Missing independent task outcomes/comparisons prevent benefit and causal attribution. Host/provider internals and exact deployed model identities are not supplied; mutability and distributed-parametric learning remain as bounded in [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent).

## Epistemic-object inventory

These are operative parts, not claims that a populated instance was observed. Form and substrate are owned by the cited records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-chunks](#epi-obj-chunks) | Extracted assertions about project intent, facts and constraints | see [EPI-OBJ-chunks](#epi-obj-chunks) | SRC-1, `scripts/ingest_document.py` | Import does not endorse source; nontext/encoding fidelity bounded. |
| [EPI-OBJ-review-progress](#epi-obj-review-progress) | Coverage/classification assertions; statuses/IDs are workflow state, not source truth | see [EPI-OBJ-review-progress](#epi-obj-review-progress) | SRC-1, `scripts/review_progress.py` | Syntactic validity and final dispositions do not prove accurate reading. |
| [EPI-OBJ-requirements](#epi-obj-requirements) | Claims about explicit intended behavior, not necessarily actual behavior | see [EPI-OBJ-requirements](#epi-obj-requirements) | SRC-1, `assets/requirements-change-templates.md` | Confirmed intent cannot be inferred from code alone. |
| [EPI-OBJ-technical](#epi-obj-technical) | Claims about implementation and architecture | see [EPI-OBJ-technical](#epi-obj-technical) | SRC-1, `references/initialization-workflows.md` | Inferred/unknown findings must remain qualified. |
| [EPI-OBJ-analysis](#epi-obj-analysis) | Significant tradeoff/impact/risk synthesis; potentially conjectural | see [EPI-OBJ-analysis](#epi-obj-analysis) | SRC-1, `references/update-workflows.md` | No concrete candidate establishes entailment or non-entailment. |
| [EPI-OBJ-questions-alerts](#epi-obj-questions-alerts) | Unresolved propositions, conflicts and risk assumptions; status encodes reliance | see [EPI-OBJ-questions-alerts](#epi-obj-questions-alerts) | SRC-1, `references/common-policies.md` | A resolved status needs evidence; does not guarantee correctness. |
| [EPI-OBJ-requirement-evidence](#epi-obj-requirement-evidence) | Explicit attribution edges, not claim meaning | see [EPI-OBJ-requirement-evidence](#epi-obj-requirement-evidence) | SRC-1, `assets/requirements-change-templates.md` | Reciprocal graph consistency does not show semantic support. |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Normative operating instructions; not newly acquired project facts | see [RT-OBJ-skill](runtime.md#rt-obj-skill) | SRC-1, `SKILL.md` | Static guidance not trace-learned methodology. |
| [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) | Symbolic schema/policy contract | see [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) | SRC-1, `schema/project-wiki.yml` | Structural contract, not a truth oracle. |
| [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent) | Potential model-mediated claims; internal contents not determinable | see [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent) | SRC-1, `README.md` | No frozen model/provider internals or execution trace. |

## Authority-route ledger

Each route's shared record owns endpoints, evaluator domain, timing, effects and limits. Architectural status here distinguishes executable helpers from host-interpreted instructions: a declared host procedure is not an inspected host implementation. No route below has observed-run support.

Route ID: [EPI-RTE-extract-source](#epi-rte-extract-source)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-chunks](#epi-obj-chunks)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Evaluator/condition and domain: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Activation and timing: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Possible or observed result: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Implemented force: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Epistemic authority and scope: Unknown source warrant; preserving bytes or words does not endorse source claims.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Behavioral-authority path: see [EPI-RTE-extract-source](#epi-rte-extract-source).
Evidence source ID and local anchor: SRC-1, `scripts/ingest_document.py`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-extract-source](#epi-rte-extract-source).

Route ID: [EPI-RTE-ledger-check](#epi-rte-ledger-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-review-progress](#epi-obj-review-progress)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Evaluator/condition and domain: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Activation and timing: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Possible or observed result: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Implemented force: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Epistemic authority and scope: Licenses statements about ledger completeness and bytes, not reading, source interpretation or canonical truth.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Behavioral-authority path: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).
Evidence source ID and local anchor: SRC-1, `scripts/review_progress.py`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-ledger-check](#epi-rte-ledger-check).

Route ID: [EPI-RTE-skip-audit](#epi-rte-skip-audit)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-review-progress](#epi-obj-review-progress)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Evaluator/condition and domain: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Activation and timing: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Possible or observed result: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Implemented force: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Epistemic authority and scope: Supports identifying textual signals among skipped units, not that skipping is wrong.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Behavioral-authority path: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).
Evidence source ID and local anchor: SRC-1, `scripts/review_progress.py`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-skip-audit](#epi-rte-skip-audit).

Route ID: [EPI-RTE-content-compare](#epi-rte-content-compare)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-chunks](#epi-obj-chunks)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Evaluator/condition and domain: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Activation and timing: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Possible or observed result: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Implemented force: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Epistemic authority and scope: Candidate support is source- and project-relative; classification alone licenses no independent truth claim.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Behavioral-authority path: see [EPI-RTE-content-compare](#epi-rte-content-compare).
Evidence source ID and local anchor: SRC-1, `references/document-ingestion.md`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-content-compare](#epi-rte-content-compare).

Route ID: [EPI-RTE-content-admit](#epi-rte-content-admit)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-requirements](#epi-obj-requirements)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Evaluator/condition and domain: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Activation and timing: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Possible or observed result: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Implemented force: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Epistemic authority and scope: Intended criterion is clear source-backed content within authorized scope, for canonical project use. A procedural acceptance route exists; no recorded evidence-consuming acceptance instance is supplied.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Behavioral-authority path: see [EPI-RTE-content-admit](#epi-rte-content-admit).
Evidence source ID and local anchor: SRC-1, `references/document-ingestion.md`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-content-admit](#epi-rte-content-admit).

Route ID: [EPI-RTE-canonical-retain](#epi-rte-canonical-retain)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-requirements](#epi-obj-requirements)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Evaluator/condition and domain: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Activation and timing: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Possible or observed result: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Implemented force: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Epistemic authority and scope: Retains the bounded source/intent authority assigned by admission; disk persistence adds no warrant.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Behavioral-authority path: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).
Evidence source ID and local anchor: SRC-1, `references/document-ingestion.md`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-canonical-retain](#epi-rte-canonical-retain).

Route ID: [EPI-RTE-canonical-link](#epi-rte-canonical-link)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-requirement-evidence](#epi-obj-requirement-evidence)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Evaluator/condition and domain: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Activation and timing: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Possible or observed result: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Implemented force: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Epistemic authority and scope: Preserves explicit evidence attribution after admission; valid reciprocal edges do not entail source support.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Behavioral-authority path: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).
Evidence source ID and local anchor: SRC-1, `assets/requirements-change-templates.md`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-canonical-link](#epi-rte-canonical-link).

Route ID: [EPI-RTE-structure-check](#epi-rte-structure-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-requirement-evidence](#epi-obj-requirement-evidence)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Evaluator/condition and domain: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Activation and timing: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Possible or observed result: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Implemented force: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Epistemic authority and scope: Bounded structural facts only; no entailment, source authority or exhaustive semantic traceability license.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Behavioral-authority path: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Evidence source ID and local anchor: SRC-1, `scripts/validate_wiki.py`.
Claim IDs or none: [EPI-CLM-provenance-rule](#epi-clm-provenance-rule)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-structure-check](#epi-rte-structure-check).

Route ID: [EPI-RTE-semantic-lint](#epi-rte-semantic-lint)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-technical](#epi-obj-technical)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Evaluator/condition and domain: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Activation and timing: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Possible or observed result: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Implemented force: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Epistemic authority and scope: Candidate criticism only until evidence-consuming decisions; no observed truth or accuracy license.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Behavioral-authority path: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).
Evidence source ID and local anchor: SRC-1, `references/maintenance-workflows.md`.
Claim IDs or none: [EPI-CLM-active-governance](#epi-clm-active-governance)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-semantic-lint](#epi-rte-semantic-lint).

Route ID: [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-technical](#epi-obj-technical)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Evaluator/condition and domain: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Activation and timing: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Possible or observed result: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Implemented force: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Epistemic authority and scope: Scoped changed reliance based on current evidence/confirmation, not proof that all remaining claims are true.
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Behavioral-authority path: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).
Evidence source ID and local anchor: SRC-1, `references/maintenance-workflows.md`.
Claim IDs or none: [EPI-CLM-active-governance](#epi-clm-active-governance)
Mismatch marker or none: none — scope limits are explicit in the record.
Gap/limit: see [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw).

Route ID: [RT-RTE-note-update](runtime.md#rt-rte-note-update)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-analysis](#epi-obj-analysis), [EPI-OBJ-requirements](#epi-obj-requirements), [EPI-OBJ-technical](#epi-obj-technical)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-note-update](runtime.md#rt-rte-note-update).
Evaluator/condition and domain: see [RT-RTE-note-update](runtime.md#rt-rte-note-update).
Activation and timing: see [RT-RTE-note-update](runtime.md#rt-rte-note-update).
Possible or observed result: see [RT-RTE-note-update](runtime.md#rt-rte-note-update).
Implemented force: see [RT-RTE-note-update](runtime.md#rt-rte-note-update).
Epistemic authority and scope: pasted explicit intent is acquired; model-authored synthesis requires its own evidence. No concrete output establishes whether synthesis only reshapes, derives or conjectures.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-note-update](runtime.md#rt-rte-note-update).
Behavioral-authority path: see [RT-RTE-note-update](runtime.md#rt-rte-note-update), [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol).
Evidence source ID and local anchor: SRC-1, `references/update-workflows.md`.
Claim IDs or none: [RT-CLM-project-memory](runtime.md#rt-clm-project-memory)
Mismatch marker or none: none.
Gap/limit: no candidate or acceptance trace; document-ledger controls do not apply to pasted notes.

Route ID: [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-technical](#epi-obj-technical), [EPI-OBJ-requirements](#epi-obj-requirements)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: project-specific scan/initial identity capture only; scaffold mechanics see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki).
Evaluator/condition and domain: see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki).
Activation and timing: see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki).
Possible or observed result: see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki).
Implemented force: see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki).
Epistemic authority and scope: observed implementation belongs in technical records; confirmed product requirements need explicit intent; uncertain architectural inference remains inferred/unknown.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki).
Behavioral-authority path: see [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki), [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol).
Evidence source ID and local anchor: SRC-1, `references/initialization-workflows.md`.
Claim IDs or none: [RT-CLM-project-memory](runtime.md#rt-clm-project-memory)
Mismatch marker or none: none — scaffold success explicitly disclaims semantic completion.
Gap/limit: host semantic production not observed; no concrete claim tests entailment or ampliation.

Route ID: [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-requirements](#epi-obj-requirements), [EPI-OBJ-technical](#epi-obj-technical), [EPI-OBJ-analysis](#epi-obj-analysis)
Content/update relation: no content change
Transition or check target: see [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle).
Evaluator/condition and domain: see [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle).
Activation and timing: see [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle).
Possible or observed result: see [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle).
Implemented force: see [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol).
Epistemic authority and scope: selected canonical pages guide task work; selection/delivery does not renew source warrant or prove correctness. Disabled/invalid auto-sync requires checking relevant claims against current sources.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle).
Behavioral-authority path: see [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol).
Evidence source ID and local anchor: SRC-1, `references/automatic-workflows.md`.
Claim IDs or none: [RT-CLM-project-memory](runtime.md#rt-clm-project-memory)
Mismatch marker or none: unknown — conditional instruction loading and adherence.
Gap/limit: no actual coding trace shows what survived selection or changed action.

The intake lineage/freshness and operational selection subfunctions are also supplied in [RT-RTE-source-intake](runtime.md#rt-rte-source-intake): process/skip/review decisions precede extraction, quarantine can remove duplicate inbox copies, expected hashes bind inbox decisions, and source/ledger changes require rechecking. These grant processing permission over named bytes, not epistemic endorsement. Direct document intake can omit the expected hash; pasted-note intake has no chunk coverage gate. They therefore cannot be treated as a universal source acceptance interlock. Configuration and protocol replacement change behavior by policy, not by producing new truth-apt claims; their consumer and force are see [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | see record | SRC-1, `README.md`; doctrine/design | Index-first retrieval, canonical capture and generated protocol: see record | [EPI-RTE-extract-source](#epi-rte-extract-source), [EPI-RTE-structure-check](#epi-rte-structure-check); host parts remain doctrine | None supplied | No recall/benefit comparison; helper code is not a deployed host | Durable file-based memory and selective read-back are designed; benefit unobserved | Instant recall/usefulness is not demonstrated |
| [EPI-CLM-provenance-rule](#epi-clm-provenance-rule) | see record | SRC-1, `README.md`; doctrine/design | Distinct comparison, disposition, retention and integration policies | [EPI-RTE-extract-source](#epi-rte-extract-source), [EPI-RTE-ledger-check](#epi-rte-ledger-check), [EPI-RTE-skip-audit](#epi-rte-skip-audit), [EPI-RTE-structure-check](#epi-rte-structure-check) | None supplied | No acceptance instance; byte fidelity and graph consistency do not prove source meaning | Clear source-backed canonical admission is prescribed; structural/provenance support is implemented | Treating integrated status alone as warranted truth would exceed checks |
| [EPI-CLM-active-governance](#epi-clm-active-governance) | see record | SRC-1, `README.md`; doctrine/design | [EPI-RTE-semantic-lint](#epi-rte-semantic-lint), [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw) | [EPI-RTE-structure-check](#epi-rte-structure-check) before semantic lint | None supplied | Explicit maintain plus task triggers, not an independently scheduled semantic monitor | Evidence-directed correction and preserved risk state are specified | “Continuous” is conditional host behavior, not observed autonomous evaluation |

## Bounded conclusion

Project Wiki separates provenance from canonical project use. Extraction acquires truth-apt source text without establishing its truth. Source hashes and chunk IDs preserve attribution to bytes, while format extraction can omit content; original source warrant remains unknown. For a concrete plain-text witness, inspected code normalizes `# Policy\r\n\r\nUsers  must log in.\r\n` to `# Policy\n\nUsers must log in.`. It creates a heading block and a following body block and, with max_words 80, one chunk joining them with a blank line. This deduction uses only implementation evidence, not execution. It establishes lexical non-ampliative reshaping for that input, not a new claim about actual user authentication or source correctness ([EPI-RTE-extract-source](#epi-rte-extract-source)).

Ledger completion, digest checks and reciprocal evidence edges produce bounded structural evidence. A complete ledger can be submitted without a preceding content view; even correct identifiers can link a false or misinterpreted assertion. Conversely, semantic review is not absent: the host is explicitly told to compare source with project evidence and to identify contradictions/stale meaning. These are distinct evaluator domains and must not be collapsed ([EPI-RTE-ledger-check](#epi-rte-ledger-check), [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-content-compare](#epi-rte-content-compare), [EPI-RTE-semantic-lint](#epi-rte-semantic-lint)).

The material acceptance criterion is conservative, clear source-backed representation within authorized project scope for canonical project use. Explicit intent governs requirements; current code governs observed technical behavior; inference/unknown state, questions and alerts preserve unresolved content. Direct integration is authorized without per-claim human review, while source authority, scope, incompatible baselines, binding choices and re-baselining confirmed intent can require a human decision. Low-risk maintenance repairs are direct; high-impact canonical meaning changes require confirmation. These are operative policy permissions and vetoes through the host, not machine proof of truth ([EPI-RTE-content-admit](#epi-rte-content-admit), [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw)).

Retention and post-admission integration remain distinct. Canonical files persist accepted content alongside marked uncertainty; sidecar edges and navigation connect accepted document-derived records to evidence and later use. Terminal intake is normally excluded from coding context and available for provenance/conflict investigation. Later hosts are instructed to use selected canonical knowledge when coding, giving retained text an intended advisory behavioral path across tasks/sessions. No trace establishes any particular acceptance, integration or later action ([EPI-RTE-canonical-retain](#epi-rte-canonical-retain), [EPI-RTE-canonical-link](#epi-rte-canonical-link), [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle)).

No supplied candidate permits a content-specific entailed-derivation or ampliative-conjecture finding for agent synthesis. Plausible architecture or tradeoff prose is not enough to infer either relation. There is no demonstrated new accepted ampliative claim; this is an evidence limit, not a claim that the host cannot conjecture or accept one. Likewise model parameter state, exercised learning and benefit are unestablished, independently of the designed persistent-text path. The examined procedures support project-memory maintenance and criticism of project claims, not an evidenced iterative theory-building episode or improvement of this skill's own method. No system-wide epistemic score, learning verdict or self-improvement inference follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-chunks
Label: Intake source chunks

Natural-language extracted text, stored in chunks/CH-*.md with symbolic provenance metadata. The substantive text is imported candidate content; wrappers and hash/ID metadata are not truth validation. Manifest JSON indexes the chunks; source-info.yml identifies source bytes and optional copied source. Source: SRC-1, `scripts/ingest_document.py`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> "## Text",
> "",
> chunk.text,
> "",
> --- `scripts/ingest_document.py`

#### EPI-OBJ-review-progress
Label: Review progress ledger

Symbolic per-chunk statuses, classifications, target IDs and counts in review-progress.yml; free-text notes provide natural-language skip/review rationale. Code consumes the symbolic fields for workflow completeness; the host interprets notes. These parts share the ledger substrate but have different force: nonempty notes are checked, their reasonableness is not. Source: SRC-1, `scripts/review_progress.py`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> entries_by_id[chunk_id].update(
>     status=status,
>     classifications=classifications,
>     target_ids=target_ids,
>     notes=notes,
> )
> --- `scripts/review_progress.py`

#### EPI-OBJ-requirements
Label: Canonical intent records

Natural-language REQ/NFR/CON statements, rationale and acceptance notes, in Markdown topic files/constraints; symbolic IDs, statuses and confidence fields support routing and checks. The source of confirmed authority is explicit product intent, not code observed to behave that way. Source: SRC-1, `references/initialization-workflows.md`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> Fill requirements only when they are explicitly stated in product-intent sources such as README files, product docs, issue or ticket descriptions, imported requirements documents, meeting notes, or user-provided notes.
> --- `references/initialization-workflows.md`

#### EPI-OBJ-technical
Label: Technical project records

Natural-language descriptions of code behavior and architecture in technical/ Markdown; source paths and confidence/status metadata are symbolic pointers/qualifiers. These claim actual implementation, independently of requirements' intent claims. Source: SRC-1, `references/initialization-workflows.md`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> Populate `technical/architecture.md` with a concise architecture overview. Mark unverified architectural claims as `confidence: inferred`.
> --- `references/initialization-workflows.md`

#### EPI-OBJ-analysis
Label: Durable project analysis

Natural-language non-canonical/exploratory synthesis in analysis/AN-*.md, or useful answers incorporated into canonical files; registry/index/evidence links provide symbolic selection. No instance is supplied to determine what proposition was produced or whether it exceeds premises. Source: SRC-1, `references/update-workflows.md`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-note-update](runtime.md#rt-rte-note-update); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> If the answer is useful but non-canonical or exploratory, create or update `analysis/AN-YYYYMMDD-NNN-short-title.md`.
> --- `references/update-workflows.md`

#### EPI-OBJ-questions-alerts
Label: Questions and alerts

Natural-language unresolved questions, conflicts, dangerous assumptions and resolution evidence in requirements/open-questions.md and alerts/*.md. Symbolic dispositions and confidence guide reliance and routing; resolution text/evidence is interpreted by the host, not automatically checked for semantic sufficiency. This combined inventory groups uncertainty tracking, not the differently scoped acceptance checks. Source: SRC-1, `references/common-policies.md`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> Update `requirements/open-questions.md` with status, updated date, resolution or narrowed question, evidence links, and related IDs.
> --- `references/common-policies.md`

#### EPI-OBJ-requirement-evidence
Label: Requirement evidence edges

Symbolic YAML mapping from atomic REQ/NFR/CON IDs to full chunk IDs in traceability/requirement-evidence.yml; fixed consumer rules check existence and reciprocal integrated ledger edges. It encodes provenance assertions separately from natural-language requirement bodies. Source: SRC-1, `assets/requirements-change-templates.md`. Distinct identity: these are consuming-project retained/generated parts, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) or instruction object [RT-OBJ-skill](runtime.md#rt-obj-skill). The closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake); it describes production/use rather than declaring this object. No supplied object counterpart was declared.

> `traceability/requirement-evidence.yml` is the machine-facing source of truth for atomic requirement provenance:
> --- `assets/requirements-change-templates.md`

### Routes

#### EPI-RTE-extract-source
Label: Extract source

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

This is the extraction subroute, not the whole source-intake workflow. Import preserves lineage through the source hash and chunk IDs; PDF layout, DOCX nontext content and malformed UTF-8 can be lost. For a plain-text witness the lexical reshaping is non-ampliative; that does not prove semantic preservation for every supported format.

Endpoints/progression, owner and context/state effects: Local source snapshot to normalized blocks and chunk files. Format dispatcher and deterministic normalizer/chunker; PDF/DOCX extraction relies on uninspected dependencies. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Extracted text and provenance, or extraction/hash/publication error.

- Immediate return: Intake report/location and extraction files; errors stop local publication.
- Later read-back: Chunk files can be reloaded through inspect/view during resumed review; terminal intake is provenance-only by policy.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Supported source extension, source-scope checks and optional expected hash; chunk selection occurs downstream.
- Invalidation or expiry: Known-bad pre-integration extraction is rejected/superseded and regenerated; post-integration errors require canonical correction.
- Activation or effect: Artifact creation is wired; no supplied operation or later activation.
- Evidence limits: inspected helper implementation only; no supplied execution or causal comparison. Unknown source warrant; preserving bytes or words does not endorse source claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Force: Helper errors enforce local refusal; successful artifacts remain provenance, not canonical authority.
Operational consequence: Makes extracted text available to review, not ordinary coding-task reliance.
Behavioral-authority path: Host reviewer receives chunk text through view; informational/advisory; one intake and resumed review.

Evidence: SRC-1, `scripts/ingest_document.py`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> text = normalize_text(source.read_text(encoding="utf-8", errors="replace"))
> --- `scripts/ingest_document.py`

#### EPI-RTE-ledger-check
Label: Audit review ledger

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

The audit is a subroute of intake and never a semantic acceptance evaluator. Direct apply does not prove previous view. A ledger may be structurally complete while its classifications are wrong. The helper does not atomically set terminal intake status.

Endpoints/progression, owner and context/state effects: Ledger identity, allowed states, count consistency, complete dispositions and optionally byte digest. review_progress audit; exact manifest identity, summary/state consistency and digest equality domain. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: review-complete/review-incomplete with SHA-256, or error including changed digest.

- Immediate return: Audit status, summary and exact ledger SHA-256, or error.
- Later read-back: inapplicable — audit is read-only; a host copies evidence into the persistent wiki log.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Explicit audit with intake ID and optional expected digest.
- Invalidation or expiry: Changed ledger bytes invalidate the copied digest; rerun audit after correction.
- Activation or effect: Checks and output are wired; no observed completion or compliance.
- Evidence limits: inspected helper implementation only; no supplied execution or causal comparison. Licenses statements about ledger completeness and bytes, not reading, source interpretation or canonical truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Force: Digest mismatch errors locally; review-incomplete can return exit 0. Host must consume audit_status.
Operational consequence: Policy requires review-complete before reviewed/integrated status; no atomic status write or lock.
Behavioral-authority path: Host finalizer, audit output, enforcing local error plus procedural admission condition, finalization checkpoint.

Evidence: SRC-1, `scripts/review_progress.py`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> if args.command == "audit":
>     validate_ledger_state(ledger, contract)
>     print_audit(build_ledger_audit(args.intake_id, ledger, ledger_sha256), args.format)
>     return 0
> --- `scripts/review_progress.py`

#### EPI-RTE-skip-audit
Label: Audit skipped chunks

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

A distinct optional diagnostic subroute omitted from runtime's detailed forcing cases, not a second semantic review implementation. It reads skipped source text but does not change ledger or canonical state.

Endpoints/progression, owner and context/state effects: Already-skipped chunks, skip notes, normative terms and contiguous runs. Optional audit-skips lexical patterns, not entailment, relevance or correctness. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Skip list, signals and contiguous runs for investigation.

- Immediate return: Skipped chunks, lexical signals, notes and run grouping.
- Later read-back: inapplicable — diagnostic output is read-only and not automatically retained.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Explicit audit-skips; only entries with status skipped.
- Invalidation or expiry: inapplicable — rerunning computes from current validated snapshot; no stored decision is made.
- Activation or effect: Output construction is implemented; diagnostic use remains unobserved.
- Evidence limits: inspected helper implementation only; no supplied execution or causal comparison. Supports identifying textual signals among skipped units, not that skipping is wrong.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Force: Diagnostic only; not a mandatory gate and no automatic disposition change.
Operational consequence: Host can select units for rereading; output alone neither rejects nor reinstates a chunk.
Behavioral-authority path: Investigating host, diagnostic output then view --chunks, advisory, current investigation.

Evidence: SRC-1, `scripts/review_progress.py`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> if normative_terms:
>     signals.append("normative-language")
> if AUDIT_DEFERRED_NOTE_PATTERN.search(notes):
>     signals.append("deferred-or-unmodeled-note")
> --- `scripts/review_progress.py`

#### EPI-RTE-content-compare
Label: Compare document candidates

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

Comparison is not acceptance. No concrete generated candidate or comparison trace is supplied, so acquisition/reshaping/entailed derivation/ampliative conjecture cannot be individuated for model-authored findings. The workflow requests conservative representation and preserving uncertainty, not model omniscience.

Endpoints/progression, owner and context/state effects: Document candidates against canonical project records, explicit intent and as-is technical state. Host agent interpreting source and project context; no inspected semantic evaluator implementation or expected-answer oracle. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Classifications, target IDs, uncertainty, questions, alerts and identification of blocking decisions.

- Immediate return: Proposed classifications, questions, evidence links and blocking choices.
- Later read-back: Ledger checkpoints support resumed review; associated questions/alerts retain unresolved judgments.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Every source chunk must receive a final disposition; compare against relevant canonical state.
- Invalidation or expiry: New evidence, extraction defects or resolved authority choices require revisiting affected findings.
- Activation or effect: Semantic comparison is prescribed to the host; not observed.
- Evidence limits: inspected host-directed procedure only; no supplied execution or causal comparison. Candidate support is source- and project-relative; classification alone licenses no independent truth claim.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Force: Requested judgment informs downstream admission; apply validates labels, not semantic adequacy.
Operational consequence: Feeds direct integration or narrowly scoped human review; unresolved information may be represented conservatively.
Behavioral-authority path: Host integrator, interpreted source/wiki comparison, advisory to permissive via subsequent decision, one intake.

Admission/decision roles: the host proposes and performs representation; the user can veto the blocking choices or high-impact maintenance changes described here. Computational checks reject malformed structure, not semantic alternatives. Operating mode is an open project update/audit, not a bounded experiment/curriculum. No expected-answer oracle is supplied; comparison against source/code is evidence, not a reference answer. Trigger and proposed change: Every source chunk must receive a final disposition; compare against relevant canonical state. Guidance: preserve source-backed intent, uncertainty and history. What persists: canonical/project review state and associated evidence, not model parameters. Rejection/recovery: retain unresolved findings or reject/supersede bad intake, and correct affected canonical records; no multi-file semantic rollback is implemented here.

Evidence: SRC-1, `references/document-ingestion.md`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> Compare candidate document items against `.project-wiki/INDEX.md`, `REGISTRY.yml`, relevant requirements, changes, technical docs, implementation docs, and traceability maps.
> --- `references/document-ingestion.md`

#### EPI-RTE-content-admit
Label: Direct or blocking integration

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

This is disposition, separate from content comparison, retention and linking. Explicit update is not per-assertion human approval. Requirements express authorized product intent; that is not proof of actual implementation or external legal correctness.

Endpoints/progression, owner and context/state effects: Source-backed information for canonical project representation, including authority, scope and confirmed-intent conflicts. Host admits conservative source-backed content under explicit update authority; human decides enumerated blocking choices or review-only requests. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Direct admission, represented uncertainty, pending review, integration after decision, rejection or postponement.

- Immediate return: Integration decision or exact blocking question; rejection/postponement remain reportable outcomes.
- Later read-back: Final status, canonical records or pending review retain disposition for later tasks/integration.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Clear conservative source-backed representation versus listed authority/scope/binding/baseline blockers.
- Invalidation or expiry: Decision changes or material extraction defects require correction, rejection or supersession; no whole-write-set rollback.
- Activation or effect: Host decision protocol is declared, not implemented by a semantic engine here or observed.
- Evidence limits: inspected host-directed procedure only; no supplied execution or causal comparison. Intended criterion is clear source-backed content within authorized scope, for canonical project use. A procedural acceptance route exists; no recorded evidence-consuming acceptance instance is supplied.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Force: Procedural human veto over blocking choices; no host-independent semantic interlock.
Operational consequence: Permits canonical writing directly unless a blocking decision or requested review-only mode intervenes.
Behavioral-authority path: Host integrator and conditional human approver, canonical write/review.md decision, permissive/veto policy, intake integration.

Admission/decision roles: the host proposes and performs representation; the user can veto the blocking choices or high-impact maintenance changes described here. Computational checks reject malformed structure, not semantic alternatives. Operating mode is an open project update/audit, not a bounded experiment/curriculum. No expected-answer oracle is supplied; comparison against source/code is evidence, not a reference answer. Trigger and proposed change: Clear conservative source-backed representation versus listed authority/scope/binding/baseline blockers. Guidance: preserve source-backed intent, uncertainty and history. What persists: canonical/project review state and associated evidence, not model parameters. Rejection/recovery: retain unresolved findings or reject/supersede bad intake, and correct affected canonical records; no multi-file semantic rollback is implemented here.

Evidence: SRC-1, `references/document-ingestion.md`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> Integrate clear information directly. Preserve non-blocking ambiguity through accurate status and confidence, open questions, alerts, blocked records, or explicit alternatives instead of stopping the workflow.
> --- `references/document-ingestion.md`

#### EPI-RTE-canonical-retain
Label: Retain integrated records

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

This is document-derived retention, not static schema storage or all routes that write the wiki. It remains distinct from accepted-claim linking. Physical persistence is afforded by host files; no populated wiki or cross-session trace was supplied.

Endpoints/progression, owner and context/state effects: Admitted document-derived canonical records and retained unresolved records. Host writes Markdown/YAML, with deterministic structural checks downstream. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: REQ/NFR/CON, technical or other canonical records, statuses and audit entries.

- Immediate return: Canonical files and audit references after host edits.
- Later read-back: Future preflight selects canonical records; terminal intake normally stays out of coding context.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Accepted clear content and conservatively represented uncertainty under admission policy.
- Invalidation or expiry: Preserve history; correct affected canonical records and append audit entry on post-integration extraction defects.
- Activation or effect: Retained-state write procedure is declared; actual persistence/use unobserved.
- Evidence limits: inspected host-directed procedure only; no supplied execution or causal comparison. Retains the bounded source/intent authority assigned by admission; disk persistence adds no warrant.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Force: Retention makes records available; unresolved status is not converted into accepted truth.
Operational consequence: Enables future index-selected task context; intake status alone must not replace canonical integration.
Behavioral-authority path: Future host through canonical pages and indexes, advisory natural-language knowledge, later tasks/sessions.

Admission/decision roles: the host proposes and performs representation; the user can veto the blocking choices or high-impact maintenance changes described here. Computational checks reject malformed structure, not semantic alternatives. Operating mode is an open project update/audit, not a bounded experiment/curriculum. No expected-answer oracle is supplied; comparison against source/code is evidence, not a reference answer. Trigger and proposed change: Accepted clear content and conservatively represented uncertainty under admission policy. Guidance: preserve source-backed intent, uncertainty and history. What persists: canonical/project review state and associated evidence, not model parameters. Rejection/recovery: retain unresolved findings or reject/supersede bad intake, and correct affected canonical records; no multi-file semantic rollback is implemented here.

Evidence: SRC-1, `references/document-ingestion.md`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> On the direct path, write planned REQ/NFR records in their topic files and CON records in `requirements/constraints.md`, record every record-to-chunk edge in `traceability/requirement-evidence.yml`, and preserve non-blocking uncertainty through OQ, alerts, status, confidence, blocked records, or explicit alternatives.
> --- `references/document-ingestion.md`

#### EPI-RTE-canonical-link
Label: Link accepted requirements

Part of: [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

This is post-admission lifecycle integration, not raw artifact retention. It does not establish that all persisted edges are warranted, or that a model followed them later.

Endpoints/progression, owner and context/state effects: Admitted document-derived atomic requirements connected to source chunks and project routing. Host records exact edges; structural validator checks registered targets and reciprocal consistency, not evidential adequacy. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Requirement-evidence sidecar, reciprocal ledger targets, registry/index/traceability updates.

- Immediate return: Written exact record-to-chunk edges and routing references.
- Later read-back: Sidecar and canonical traceability support future audit/conflict investigation and record selection.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Document-derived atomic REQ/NFR/CON produced or updated by integrated chunks.
- Invalidation or expiry: Record relocation/relationship changes require updating affected edges and routing; contradictory evidence needs semantic reconciliation.
- Activation or effect: Post-admission linking is prescribed; deterministic reciprocal checks are separately implemented.
- Evidence limits: inspected host-directed procedure only; no supplied execution or causal comparison. Preserves explicit evidence attribution after admission; valid reciprocal edges do not entail source support.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Force: Structural errors block procedural completion; linkage enables later provenance investigation.
Operational consequence: Allows records to enter canonical navigation and be traced back to source; conditional on prior content acceptance.
Behavioral-authority path: Host and validator consume YAML edges; enforcing fixed structural checks and advisory evidence pointers; future task/audit horizon.

Admission/decision roles: the host proposes and performs representation; the user can veto the blocking choices or high-impact maintenance changes described here. Computational checks reject malformed structure, not semantic alternatives. Operating mode is an open project update/audit, not a bounded experiment/curriculum. No expected-answer oracle is supplied; comparison against source/code is evidence, not a reference answer. Trigger and proposed change: Document-derived atomic REQ/NFR/CON produced or updated by integrated chunks. Guidance: preserve source-backed intent, uncertainty and history. What persists: canonical/project review state and associated evidence, not model parameters. Rejection/recovery: retain unresolved findings or reject/supersede bad intake, and correct affected canonical records; no multi-file semantic rollback is implemented here.

Evidence: SRC-1, `assets/requirements-change-templates.md`; closest supplied record [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) owns the containing workflow.

> Use full chunk IDs, one explicit entry per edge, with no ranges or duplicates. Keep chunk IDs and paths out of readable REQ/NFR/CON bodies; non-intake source paths remain valid elsewhere. The human requirement map is derived from this sidecar, and integrated ledger targets must match it bidirectionally.
> --- `assets/requirements-change-templates.md`

#### EPI-RTE-structure-check
Label: Validate wiki structure

No single supplied route contains this shared evaluator: it overlaps initialize-wiki, source-intake and explicit-reconcile but is distinct from each whole workflow. One internally consistent false claim would not be rejected solely because it is false; the inspected checks compare identifiers/edges, not proposition meaning.

Endpoints/progression, owner and context/state effects: Stored wiki structure, syntax, IDs, links, review coverage, registered targets and reciprocal requirement evidence edges. WikiValidator under shipped schema; deterministic local file/graph consistency, not source meaning. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Sorted findings and valid flag; CLI 0/1, execution/dependency failure 2.

- Immediate return: ValidationReport with structural findings and valid flag; CLI status.
- Later read-back: inapplicable — validator is read-only; host may retain its result in lint/status/log artifacts.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Explicit validation, scaffold staging validation or procedural intake/maintenance checks.
- Invalidation or expiry: File/schema changes require rerunning; past validity does not establish current semantic freshness.
- Activation or effect: Validator control flow is wired; no supplied run, publication or repair trace.
- Evidence limits: inspected helper implementation only; no supplied execution or causal comparison. Bounded structural facts only; no entailment, source authority or exhaustive semantic traceability license.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Force: Enforcing within scaffold publication; host protocol blocks intake completion on deterministic errors and requires repair during maintenance.
Operational consequence: Blocks helper scaffold publication or procedural completion, prompts structural repair before semantic lint.
Behavioral-authority path: Scaffold caller or host intake/maintenance finalizer, report/exit status, enforcing helper or host policy, current publication/audit.

Evidence: SRC-1, `scripts/validate_wiki.py`; closest supplied records [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki), [RT-RTE-source-intake](runtime.md#rt-rte-source-intake) and [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile) invoke or prescribe this same evaluator; none declares it independently.

> return 0 if report.valid else 1
> --- `scripts/validate_wiki.py`

#### EPI-RTE-semantic-lint
Label: Lint current meaning

Part of: [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile)

This is the semantic checking subroute, not explicit sync's source reconciliation. It can detect mistakes that the structural checker cannot, so missing machine entailment checks do not establish absence of semantic review architecture.

Endpoints/progression, owner and context/state effects: Claims, contradictions, stale meaning, missing evidence, traceability adequacy and significant risks against current project evidence. Host analysis after deterministic validation; no supplied semantic implementation or model-task evaluation. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Evidence-linked lint findings and proposed corrections/questions/alerts.

- Immediate return: Lint report with evidence, reviewed scope, contradictions and proposed follow-up.
- Later read-back: Lint, questions, alerts and status persist; corrected canonical records can reach later coding tasks.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Explicit maintain after deterministic result is known; scope/coverage limits must be stated.
- Invalidation or expiry: New evidence or decisions can supersede findings; incomplete review does not prove freshness.
- Activation or effect: Evidence-directed semantic lint is prescribed; correctness and activation unobserved.
- Evidence limits: inspected host-directed procedure only; no supplied execution or causal comparison. Candidate criticism only until evidence-consuming decisions; no observed truth or accuracy license.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Force: Advisory proposals; high-impact canonical changes go to human confirmation before disposition.
Operational consequence: Direct low-risk repairs, or human-confirmation queue for consequential canonical changes.
Behavioral-authority path: Host maintainer and human approver, lint report/evidence links, advisory then conditional permission, maintenance round and later review.

Admission/decision roles: the host proposes and performs representation; the user can veto the blocking choices or high-impact maintenance changes described here. Computational checks reject malformed structure, not semantic alternatives. Operating mode is an open project update/audit, not a bounded experiment/curriculum. No expected-answer oracle is supplied; comparison against source/code is evidence, not a reference answer. Trigger and proposed change: Explicit maintain after deterministic result is known; scope/coverage limits must be stated. Guidance: preserve source-backed intent, uncertainty and history. What persists: canonical/project review state and associated evidence, not model parameters. Rejection/recovery: retain unresolved findings or reject/supersede bad intake, and correct affected canonical records; no multi-file semantic rollback is implemented here.

Evidence: SRC-1, `references/maintenance-workflows.md`; closest supplied record [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile) owns the containing workflow.

> The validator deliberately does not decide contradictions, implicit requirements, stale meaning, meaningful backlink adequacy, traceability quality, orphan concepts, risky assumptions, or missing source material.
> --- `references/maintenance-workflows.md`

#### EPI-RTE-claim-withdraw
Label: Correct or withdraw claims

Part of: [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile)

Disposition is separate from lint evidence production. Trigger is a maintenance finding; proposal guidance preserves history and current evidence. No automatic semantic rollback or actual correction episode is supplied.

Endpoints/progression, owner and context/state effects: Lint-supported stale or contradictory canonical claims and alert/question dispositions. Host applies low-risk fixes; human confirms high-impact contradictions, stale claims, alert resolutions or canonical meaning changes. Context is the foreground host's project task/intake or maintenance state; no separate model worker is invoked by these helpers. Timing and output: Correction, superseded/deprecated/placeholder state, resolved/dismissed/accepted-risk alerts or blocked finding.

- Immediate return: Applied fixes or request for confirmation with retained finding.
- Later read-back: Changed canonical state and retained lint/alert history inform subsequent readers.
- Delegated visibility: inapplicable — no distinct delegated semantic worker is specified; helpers return to the foreground host.
- Selection predicate: Low-risk repair versus enumerated high-impact meaning changes requiring confirmation.
- Invalidation or expiry: Further evidence/decisions may revise reliance again; keep audit history instead of deleting it.
- Activation or effect: Changed-reliance procedure is declared; no observed withdrawal or downstream behavioral change.
- Evidence limits: inspected host-directed procedure only; no supplied execution or causal comparison. Scoped changed reliance based on current evidence/confirmation, not proof that all remaining claims are true.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Force: Policy veto for consequential changes; history is preserved, not silently erased.
Operational consequence: Changes future canonical task context and disposition; unresolved changes remain documented rather than guessed.
Behavioral-authority path: Host edits canonical records and status after conditional human decision, instructional/advisory to future readers, later tasks.

Admission/decision roles: the host proposes and performs representation; the user can veto the blocking choices or high-impact maintenance changes described here. Computational checks reject malformed structure, not semantic alternatives. Operating mode is an open project update/audit, not a bounded experiment/curriculum. No expected-answer oracle is supplied; comparison against source/code is evidence, not a reference answer. Trigger and proposed change: Low-risk repair versus enumerated high-impact meaning changes requiring confirmation. Guidance: preserve source-backed intent, uncertainty and history. What persists: canonical/project review state and associated evidence, not model parameters. Rejection/recovery: retain unresolved findings or reject/supersede bad intake, and correct affected canonical records; no multi-file semantic rollback is implemented here.

Evidence: SRC-1, `references/maintenance-workflows.md`; closest supplied record [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile) owns the containing workflow.

> Mark stale documents as `superseded`, `deprecated`, or `placeholder` rather than deleting history.
> --- `references/maintenance-workflows.md`

The concrete reshaping deduction in the bounded conclusion also uses SRC-1, `scripts/ingest_document.py`:

> def normalize_text(text: str) -> str:
>     text = text.replace("\r\n", "\n").replace("\r", "\n")
>     text = re.sub(r"[ \t]+", " ", text)
>     text = re.sub(r"\n{3,}", "\n\n", text)
>     return text.strip()
> --- `scripts/ingest_document.py`

> text = "\n\n".join(current_parts).strip()
> sequence = len(chunks) + 1
> --- `scripts/ingest_document.py`

> segment = block.text[
>     word_spans[position].start() : word_spans[end_position - 1].end()
> ]
> --- `scripts/ingest_document.py`

An implemented optional skip diagnostic is not an undiscovered semantic veto. Its procedural consumer is explicitly bounded (SRC-1, `references/document-ingestion.md`):

> `audit-skips` is an optional diagnostic that lists skipped chunks, contiguous runs, notes, and lexical signals. Use it only when investigating exclusions; its output is not a semantic verdict or a finalization requirement. Use `view --chunks` for any source units selected for rereading.
> --- `references/document-ingestion.md`

The structural evaluator's integrated evidence domain is supported by its actual reciprocal-edge comparison, not by the label “evidence” (SRC-1, `scripts/validate_wiki.py`):

> evidence_atomic_edges = {
>     (chunk_id, document_id)
>     for document_id, evidence in self.requirement_evidence_by_id.items()
>     for chunk_id in evidence
>     if chunk_id.startswith(f"{intake_id}-")
> }
> for chunk_id, document_id in sorted(evidence_atomic_edges - ledger_atomic_edges):
> --- `scripts/validate_wiki.py`

The consumer of maintenance criticism is conditional human/agent action, not merely a retained report (SRC-1, `references/maintenance-workflows.md`):

> Apply low-risk fixes directly. For high-impact contradictions, stale claims, alert resolutions, or canonical meaning changes, write the lint finding and ask for user confirmation before changing canonical docs.
> --- `references/maintenance-workflows.md`

### Claims

#### EPI-CLM-provenance-rule
Label: Knowledge provenance principle

Claimed operation: raw external documents are provenance, not unreviewed canonical truth; classification/integration confer canonical project use, and confirmed business requirements require explicit product intent. Source: SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-project-memory](runtime.md#rt-clm-project-memory): this is an admission/authority claim, not persistence/usefulness. Closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake), which supplies the whole integration procedure.

> Raw external documents (PDF, DOCX) ingested via `intake/` are treated as **provenance** (evidence), never as unreviewed canonical truth. Information becomes canonical only when classified and integrated into official wiki records. Likewise, code scanned via `sync` documents observed technical reality, while confirmed business requirements require explicit product intent.
> --- `README.md`

Countercase search and limits: complete classifications and matching evidence IDs can coexist with mistaken interpretation; inspect/apply/audit and validator do not perform semantic entailment checks ([EPI-RTE-ledger-check](#epi-rte-ledger-check), [EPI-RTE-structure-check](#epi-rte-structure-check)). But direct integration does not require silently accepting arbitrary content: source comparison and a narrow human authority gate are prescribed ([EPI-RTE-content-compare](#epi-rte-content-compare), [EPI-RTE-content-admit](#epi-rte-content-admit)). Thus no supersession of runtime's bounded structural account is needed.

The shipped development checks are not an additional canonical-content oracle. Directly inspected check_contracts dispatch compares schema versions, public tree, path references, forbidden roots, intake names and templates; CI invokes unittest, contract checks, compilation and CLI smoke checks. Targets are packaged helper/contract behavior, not the truth of a consuming project's claims. The CI consumer can fail a development job, not accept a project assertion. Detailed test assertions and successful runs remain uninspected/not supplied; no causal or model-quality inference follows (SRC-1, `scripts/check_contracts.py`, `.github/workflows/tests.yml`).

> check_version_references(repo_root, contract, findings)
> check_public_tree(repo_root, contract, findings)
> check_required_path_references(repo_root, contract, findings)
> check_forbidden_root_paths(repo_root, contract, findings)
> check_intake_artifact_references(repo_root, contract, findings)
> check_template_contracts(repo_root, contract, findings)
> --- `scripts/check_contracts.py`

> - name: Run unit tests
>   run: python -m unittest discover -s tests -v
>
> - name: Check schema contract drift
>   run: python scripts/check_contracts.py
> --- `.github/workflows/tests.yml`

#### EPI-CLM-active-governance
Label: Active governance

Claimed operation: continuous semantic linting tracks gaps, risks and alerts. Source: SRC-1, `README.md`, doctrine/design; no observed run or causal result. Distinct from [RT-CLM-project-memory](runtime.md#rt-clm-project-memory): correction/evaluation rather than storage and read-back. Closest supplied route [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile) makes the scope qualification explicit.

> **Active governance**: Continuous semantic linting tracks gaps, risks, and alerts explicitly
> --- `README.md`

Countercase search and limits: maintain explicitly includes semantic checks and source reconciliation even for gaps missed by automatic updates. This defeats a claim that only syntax is checked. However explicit maintain and host-mediated task triggers do not establish a scheduled always-running monitor, nor correctness of any lint finding. Disabled/invalid automatic writes do not eliminate explicit sync/maintain or preflight. See [EPI-RTE-semantic-lint](#epi-rte-semantic-lint), [EPI-RTE-claim-withdraw](#epi-rte-claim-withdraw), [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle).

> The automatic write filter does not reduce this audit: check for missing durable knowledge, stale claims, and evidence gaps against current included sources, including changes not logged by automatic updates.
> --- `references/maintenance-workflows.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; route-local paths above are scoped consumers of the supplied [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol), not additional globally enforced instruction channels.
