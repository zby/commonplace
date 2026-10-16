---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "WikiSkill epistemic routes: trace-derived wiki claims, validation-limited skill acceptance and downstream instruction authority."
run-id: AAS-2026-10-15-2608-27454-65116a9d0de7-01
reviewed-boundary: arxiv-2608.27454v1-text-2026-10-15
---

# WikiSkill epistemic report

## Source-and-claim boundary

This report assesses how WikiSkill turns execution experience into reusable claims and instructions, what is checked, and what later consumers may rely on. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); sources: see [Source register](boundary.md#source-register). SRC-1 is a complete paper text capture, not executable code or an execution bundle. All architectural positives below are **doctrine only**; reported cases do not establish inspected implementation or observed operation. No target execution was performed.

The knowledge/warrant claims are [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth), [EPI-CLM-objective-audit](#epi-clm-objective-audit) and [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit). Coverage is a route-family overlay, not a system-complete implementation negative.

| Entry point or operation | Source path / anchor in SRC-1 | Coverage and inspection basis | Missing evidence and prevented conclusion |
|---|---|---|---|
| Outer loop, initialization and early termination | Registered capture, Appendix A.1 | Direct read; [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate) | No executable dispatch/harness: enforcement and variable recovery unknown |
| Task inference, tools and final outcomes | Registered capture, §2–3.2.1; Appendix B | Direct reads plus supplied [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) and [EPI-RTE-task-import](#epi-rte-task-import) | Providers, shell wrapper, tool implementation and exact scorers absent: source truth, action confinement and answer correctness not independently verified |
| Maintainer comparison, creation, patching, full index replacement, log append | Registered capture, §3.2.2; Appendix C/E.2 | Direct reads; [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis), [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation), [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) | No actual before/after wiki or edit parser: semantic preservation, specific conjectures, duplicate cleanup and edit fidelity unresolved |
| Proposer reads and finish(create/patch/no_action) | Registered capture, §3.2.3; Appendix E.3 | Direct reads; [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal) | No tool registry/dispatch: minimum-read enforcement, no_action processing and replacement behavior unknown |
| Validation, rejection, restoration, active-skill integration, impact append | Registered capture, §3.2.4; Appendix A | Direct reads; [EPI-RTE-validation-scoring](#epi-rte-validation-scoring), [EPI-RTE-skill-disposition](#epi-rte-skill-disposition), [EPI-RTE-impact-retention](#epi-rte-impact-retention), [EPI-RTE-skill-integration](#epi-rte-skill-integration) | No scorer/restore implementation or raw scores: transactional enforcement and exercised improvement unknown |
| Default full-skill injection and wiki-enabled ablation | Registered capture, §3.2.1; §5.1; §7 | Supplied [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection); [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | Wiki-enabled alternative prevents generalizing default indirect wiki authority to every mode |
| Case study and evaluation reporting | Registered capture, §5.3; Appendix B/C | Direct reads; [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | Simplified case and aggregate author reports, not full traces or independent causal experiment |
| Cleanup, withdrawal and longer-horizon adaptation | Registered capture, E.2–E.3; §7 | Direct reads: patch/refine and do-not-repeat rules; [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) | Explicit lack of automated pruning; no claim-level retraction propagation specified; unavailable implementation prevents exhaustive absence claim |
| CLI, registered hooks and alternate exposed operations | No executable source in frozen capture | Boundary exclusion/access limit, not a searched-code absence | Cannot check frozen dispatch or enumerate implementation bypasses |

Model weight state and fixity: see [RT-CMP-model-backends](runtime.md#rt-cmp-model-backends). No accessible evidence supports attributing parameter updates or claims of parametric knowledge production to this loop.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw-traces](#epi-obj-raw-traces) | see [EPI-OBJ-raw-traces](#epi-obj-raw-traces) | Raw traces; see [EPI-OBJ-raw-traces](#epi-obj-raw-traces) | SRC-1 §3.1 | see [EPI-OBJ-raw-traces](#epi-obj-raw-traces) |
| [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | see [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | Wiki patterns; see [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | SRC-1 Appendix E.2 | see [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) |
| [EPI-OBJ-wiki-index](#epi-obj-wiki-index) | see [EPI-OBJ-wiki-index](#epi-obj-wiki-index) | Wiki index; see [EPI-OBJ-wiki-index](#epi-obj-wiki-index) | SRC-1 Appendix E.2 | see [EPI-OBJ-wiki-index](#epi-obj-wiki-index) |
| [EPI-OBJ-evolution-log](#epi-obj-evolution-log) | see [EPI-OBJ-evolution-log](#epi-obj-evolution-log) | Evolution log; see [EPI-OBJ-evolution-log](#epi-obj-evolution-log) | SRC-1 Appendix E.2 | see [EPI-OBJ-evolution-log](#epi-obj-evolution-log) |
| [EPI-OBJ-skill-impact](#epi-obj-skill-impact) | see [EPI-OBJ-skill-impact](#epi-obj-skill-impact) | Skill impact; see [EPI-OBJ-skill-impact](#epi-obj-skill-impact) | SRC-1 §3.2.4 | see [EPI-OBJ-skill-impact](#epi-obj-skill-impact) |
| [EPI-OBJ-skill-content](#epi-obj-skill-content) | see [EPI-OBJ-skill-content](#epi-obj-skill-content) | Skill content; see [EPI-OBJ-skill-content](#epi-obj-skill-content) | SRC-1 Appendix E.3 | see [EPI-OBJ-skill-content](#epi-obj-skill-content) |
| [EPI-OBJ-skill-purpose](#epi-obj-skill-purpose) | see [EPI-OBJ-skill-purpose](#epi-obj-skill-purpose) | Skill purpose; see [EPI-OBJ-skill-purpose](#epi-obj-skill-purpose) | SRC-1 Appendix E.3 | see [EPI-OBJ-skill-purpose](#epi-obj-skill-purpose) |
| [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence) | see [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence) | Imported evidence; see [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence) | SRC-1 §2; Appendix B | see [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence) |
| [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions) | see [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions) | Produced predictions; see [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions) | SRC-1 §2; Appendix B | see [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions) |

## Authority-route ledger

Fields owned by declaring records are linked rather than redefined. Each new route is a material phase of its cited runtime container, not a second name for that whole route.

Route ID: [EPI-RTE-task-import](#epi-rte-task-import)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-task-import](#epi-rte-task-import)
Evaluator/condition and domain: see [EPI-RTE-task-import](#epi-rte-task-import)
Activation and timing: see [EPI-RTE-task-import](#epi-rte-task-import)
Possible or observed result: see [EPI-RTE-task-import](#epi-rte-task-import)
Implemented force: see [EPI-RTE-task-import](#epi-rte-task-import)
Epistemic authority and scope: see [EPI-RTE-task-import](#epi-rte-task-import)
Operational authority: see [EPI-RTE-task-import](#epi-rte-task-import)
Behavioral-authority path: see [EPI-RTE-task-import](#epi-rte-task-import)
Evidence source ID and local anchor: SRC-1 Appendix B; §2
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-task-import](#epi-rte-task-import)
Gap/limit: see [EPI-RTE-task-import](#epi-rte-task-import)

Route ID: [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Evaluator/condition and domain: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Activation and timing: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Possible or observed result: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Implemented force: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Epistemic authority and scope: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Operational authority: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Behavioral-authority path: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Evidence source ID and local anchor: SRC-1 Appendix E.2; Appendix C
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)
Gap/limit: see [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis)

Route ID: [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Evaluator/condition and domain: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Activation and timing: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Possible or observed result: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Implemented force: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Epistemic authority and scope: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Operational authority: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Behavioral-authority path: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Evidence source ID and local anchor: SRC-1 §3.2.2; Appendix E.2
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)
Gap/limit: see [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation)

Route ID: [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Evaluator/condition and domain: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Activation and timing: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Possible or observed result: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Implemented force: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Epistemic authority and scope: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Operational authority: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Behavioral-authority path: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Evidence source ID and local anchor: SRC-1 §3.2.2–3.2.4; Appendix E.2
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)
Gap/limit: see [EPI-RTE-wiki-retention](#epi-rte-wiki-retention)

Route ID: [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Evaluator/condition and domain: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Activation and timing: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Possible or observed result: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Implemented force: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Epistemic authority and scope: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Operational authority: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Behavioral-authority path: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Evidence source ID and local anchor: SRC-1 §2; §3.2.4; Appendix A/B
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)
Gap/limit: see [EPI-RTE-validation-scoring](#epi-rte-validation-scoring)

Route ID: [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Evaluator/condition and domain: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Activation and timing: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Possible or observed result: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Implemented force: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Epistemic authority and scope: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Operational authority: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Behavioral-authority path: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Evidence source ID and local anchor: SRC-1 §3.2.4; Appendix A
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)
Gap/limit: see [EPI-RTE-skill-disposition](#epi-rte-skill-disposition)

Route ID: [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-impact](#epi-obj-skill-impact)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Evaluator/condition and domain: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Activation and timing: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Possible or observed result: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Implemented force: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Epistemic authority and scope: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Operational authority: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Behavioral-authority path: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Evidence source ID and local anchor: SRC-1 §3.2.4; §5.3
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-impact-retention](#epi-rte-impact-retention)
Gap/limit: see [EPI-RTE-impact-retention](#epi-rte-impact-retention)

Route ID: [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Evaluator/condition and domain: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Activation and timing: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Possible or observed result: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Implemented force: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Epistemic authority and scope: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Operational authority: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Behavioral-authority path: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Evidence source ID and local anchor: SRC-1 §3.2.4; §3.2.1
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no verified implementation or observed route; see [EPI-RTE-skill-integration](#epi-rte-skill-integration)
Gap/limit: see [EPI-RTE-skill-integration](#epi-rte-skill-integration)

Route ID: [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Evaluator/condition and domain: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Activation and timing: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Possible or observed result: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Implemented force: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Epistemic authority and scope: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Operational authority: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Behavioral-authority path: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Evidence source ID and local anchor: SRC-1 §3.2; Appendix E
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no demonstrated entailment, compliance or truth acceptance
Gap/limit: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)

Route ID: [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Content/update relation: no content change
Transition or check target: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Evaluator/condition and domain: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Activation and timing: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Possible or observed result: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Implemented force: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Epistemic authority and scope: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Operational authority: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Behavioral-authority path: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)
Evidence source ID and local anchor: SRC-1 §3.2; Appendix E
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no demonstrated entailment, compliance or truth acceptance
Gap/limit: see [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)

Route ID: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Evaluator/condition and domain: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Activation and timing: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Possible or observed result: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Implemented force: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Epistemic authority and scope: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Operational authority: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Behavioral-authority path: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Evidence source ID and local anchor: SRC-1 §3.2; Appendix E
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no demonstrated entailment, compliance or truth acceptance
Gap/limit: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Route ID: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Content/update relation: non-truth-apt policy/content update: skill-conditioned task action selection
Transition or check target: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Evaluator/condition and domain: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Activation and timing: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Possible or observed result: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Implemented force: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Epistemic authority and scope: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Operational authority: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Behavioral-authority path: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Evidence source ID and local anchor: SRC-1 §3.2; Appendix E
Claim IDs: [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth)
Mismatch marker: no demonstrated entailment, compliance or truth acceptance
Gap/limit: see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source / evidence layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | None inspectable in capture | None supplied; see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) | see [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) |
| [EPI-CLM-objective-audit](#epi-clm-objective-audit) | see [EPI-CLM-objective-audit](#epi-clm-objective-audit) | see [EPI-CLM-objective-audit](#epi-clm-objective-audit) | see [EPI-CLM-objective-audit](#epi-clm-objective-audit) | None inspectable in capture | None supplied; see [EPI-CLM-objective-audit](#epi-clm-objective-audit) | see [EPI-CLM-objective-audit](#epi-clm-objective-audit) | see [EPI-CLM-objective-audit](#epi-clm-objective-audit) | see [EPI-CLM-objective-audit](#epi-clm-objective-audit) |
| [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | None inspectable in capture | None supplied; see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) | see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) |

## Bounded conclusion

WikiSkill declares a trace-fed explanation and procedure loop, not merely raw-log retrieval. [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis) and [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation) distinguish checking requested from the model from candidate generation. The prompts request generalized causes and fixes, but no complete input/output pair establishes a particular ampliative proposition or entailed derivation. Indeterminate semantics is not evidence that all changes merely summarize, nor that all novel text is conjecture.

Imported evidence has unknown source warrant ([EPI-RTE-task-import](#epi-rte-task-import), [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence)). Generated answers/artifacts are instead model-produced candidates with an indeterminate semantic relation to their inputs, not imports ([EPI-OBJ-produced-predictions](#epi-obj-produced-predictions)). Their correctness is the task scorer's target; neither external source warrant nor delivery alone establishes it. Raw traces preserve declared interaction lineage, not truth of reasoning inside them. Wiki patterns, index summaries and log narratives are retained before any described claim-level acceptance ([EPI-RTE-wiki-retention](#epi-rte-wiki-retention)). Their advisory authority can shape later proposals even when a related skill is rejected. Rejection is therefore not withdrawal of all behavior-shaping content.

The acceptance criterion is stricter and narrower for skills: benchmark-referenced validation mean must exceed the incumbent best. Checking, deciding, retaining feedback and integrating accepted instructions are separate phases ([EPI-RTE-validation-scoring](#epi-rte-validation-scoring), [EPI-RTE-skill-disposition](#epi-rte-skill-disposition), [EPI-RTE-impact-retention](#epi-rte-impact-retention), [EPI-RTE-skill-integration](#epi-rte-skill-integration)). This accepts a configuration for procedural use on that measured basis, not each causal explanation or its transfer. Candidate validation inference itself consumes unaccepted instructions. The later active-skill channel is [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection); force is model-interpreted guidance, not verified obedience. Instructions can directly change action policy without producing a truth-apt claim.

The supplied runtime’s independent learning, reflection, autonomy, theory-builder and self-improvement qualifications remain bounded ([RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal), [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)). Model-owned updates and persistent instructions support a declared improvement pathway; neither scores alone nor the simplified case closes content-directed criticism and exercised causal dependence. The reported wiki contrast concerns a bundled maintenance/access treatment, not individually verified knowledge warrant or an isolated component effect ([RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit)). No system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-raw-traces
Label: Raw traces

Identity and candidate content: Accounts of actions, observations and answers; recorded occurrence is truth-apt, while embedded reasoning can be wrong.
Representational form and storage substrate: Natural-language logs plus symbolic call/result fields in raw/ filesystem storage.
Evidence: SRC-1 §3.1. Closest supplied record: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: Declared immutability preserves history, not truth of every embedded claim.

> These traces capture the agent’s complete step-by-step interactions, including reasoning, tool calls, tool-call outputs, and final answers.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-wiki-patterns
Label: Wiki patterns

Identity and candidate content: Descriptions of failures/successes, causal explanations and conditional workarounds; commands also carry procedural force.
Representational form and storage substrate: Natural-language Markdown in wiki/patterns/.
Evidence: SRC-1 Appendix E.2. Closest supplied record: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: Requested generalization is a candidate, not automatically accepted knowledge.

> - Root cause analysis (WHY it happens, not just WHAT happens)
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-wiki-index
Label: Wiki index

Identity and candidate content: Condensed problem/cause/fix claims governing relevance selection.
Representational form and storage substrate: Natural-language Markdown catalog in wiki/index.md.
Evidence: SRC-1 Appendix E.2. Closest supplied record: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: Full replacement can change claims or omit pages; semantic preservation unverified.

> - [pattern-name](wiki/patterns/pattern-name.md): PROBLEM + ROOT CAUSE + FIX in one or two sentence.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-evolution-log
Label: Evolution log

Identity and candidate content: Maintainer narrative of findings and actions.
Representational form and storage substrate: Natural-language Markdown log in wiki; §3.1 logs.md versus E.2 log.md naming unresolved.
Evidence: SRC-1 Appendix E.2. Closest supplied record: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: Not equivalent to the harness-written score audit.

> - "append_log": "brief summary of this iteration’s findings and actions"
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-skill-impact
Label: Skill impact

Identity and candidate content: Proposal, validation score and acceptance facts; diff text remains a rejected or accepted candidate, not uniformly endorsed.
Representational form and storage substrate: Symbolic score/outcome fields and natural-language diff/metadata in wiki/skill-impact.md.
Evidence: SRC-1 §3.2.4. Closest supplied record: [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: Audit scope is intervention/outcome correspondence, not causal diagnosis.

#### EPI-OBJ-skill-content
Label: Skill content

Identity and candidate content: Conditional action rules, not necessarily assertions; efficacy and applicability claims are truth-apt.
Representational form and storage substrate: Natural-language SKILL.md in skills/ filesystem directories.
Evidence: SRC-1 Appendix E.3. Closest supplied record: [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: Candidate validation use precedes acceptance; active use follows it.

> - "skill_md": full SKILL.md content with YAML frontmatter + When to Apply + When NOT to Apply + Instructions
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-skill-purpose
Label: Skill purpose

Identity and candidate content: Origin and motivating-pattern lineage assertions.
Representational form and storage substrate: Natural-language PURPOSE.md in each skill directory.
Evidence: SRC-1 Appendix E.3. Closest supplied record: [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: No distinct provenance-correctness evaluator described.

> - "purpose_md": full PURPOSE.md content with Origin + Patterns Addressed + Evolution History
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-task-evidence
Label: Task evidence and predictions

Identity and candidate content: Container for the distinct imported-evidence and produced-prediction parts declared below. Retained ID; acquisition lineage belongs only to the imported part, while generation and prediction checking belong to the produced part.
Representational form and storage substrate: Natural-language evidence and answers with symbolic task/artifact fields in current contexts and retained trajectories; part-specific distinctions are below.
Evidence: SRC-1 §2; Appendix B. Closest supplied record: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); this object is a distinct material payload of that route, not the route itself. No operative-object counterpart is declared in the supplied runtime.
Gap/limit: This container supplies no uniform content relation, producer or warrant; operative inventory and ledger assignments use its parts. No supersession is needed for the valid container.

> The final action aTa_{T} emits a predicted answer y^i\hat{y}_{i}.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-imported-evidence
Label: Imported task evidence

Part of: [EPI-OBJ-task-evidence](#epi-obj-task-evidence)

Identity and candidate content: Externally supplied task documents, retrieved search/file content, simulator observations and benchmark references. Assertions about the task or environment are truth-apt over their source domain. These are not model-produced predictions.
Representational form and storage substrate: Natural-language task/tool evidence and symbolic observation/reference fields in task contexts, benchmark data and, where captured, raw training trajectories.
Producer and consumers: Dataset/setup and external tools/environment supply content. Task agents receive task evidence; benchmark scoring consumes expected outcomes. Training ground truth also reaches the proposer in outcome summaries. OfficeQA's initial reference pages are document evidence, not proof that expected answers reach every task agent.
Content relation and authority: Acquisition/import, with external source warrant unknown in this capture. Evidence supply permits task reasoning, not truth certification; reference outcomes define the stated scorer comparison, not an independently verified oracle.
Evidence: SRC-1 §2 and Appendix B; [EPI-RTE-task-import](#epi-rte-task-import) retains the OfficeQA passage. Closest supplied record is [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), whose incoming payload this part identifies; unlike [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions), it has an external producer.
Gap/limit: Source correctness, retrieval fidelity and exact delivered contents are uninspected. Scoring-reference access is not generalized to inference.

> When executing a task xix_{i}, the agent receives the task context xix_{i} and access to the available skills SS.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-OBJ-produced-predictions
Label: Produced task predictions

Part of: [EPI-OBJ-task-evidence](#epi-obj-task-evidence)

Identity and candidate content: Task-model emitted answers and task artifacts; answer propositions and artifact correctness are truth-apt over the benchmark task. Simulator action commands themselves can instead be non-truth-apt policy outputs.
Representational form and storage substrate: Natural-language predicted answers and symbolic answer/artifact fields; spreadsheet artifacts at task output paths; training outputs retained in raw trajectories and outcome summaries as described, not inspected files.
Producer and consumers: Inference Agent produces predictions, using task evidence and active skill guidance; task tools execute artifact-producing actions. Benchmark scorer compares outputs against external references. Maintainer/proposer later receive outputs through selected traces or summaries, not as endorsed knowledge.
Content relation and authority: Truth-apt transformation is indeterminate: no complete input/output pair establishes preservation, entailment or non-entailment. Generated outputs are not acquisition/import merely because they rely on imported evidence. Emission supplies a candidate for evaluation; finite task scoring does not license every explanation or future transfer.
Evidence: SRC-1 §2; Appendix B; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) is the closest supplied route, with distinct generation and action outputs. The container's final-answer passage establishes emission; [EPI-RTE-validation-scoring](#epi-rte-validation-scoring) retains the correctness-check passage. This part differs from imported evidence in producer, content relation and checking role.
Gap/limit: Exact generation semantics and actual answer correctness remain uninspected. Training, validation and final testing have different downstream uses; validation-generated scores can affect admission, not arbitrary task outputs directly.

### Routes

#### EPI-RTE-task-import
Label: Task evidence acquisition

Part of: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Distinct identity: the content transformation phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: The task-visible portion of [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence) enters task context through setup and task tools/environment; no source-truth certification described. Scorer-only benchmark references are not asserted to enter this route.
Context/state/action effects and timing: Task setup and tool responses before prediction. Result: Imported evidence delivered; source warrant unknown. Model-produced predictions are a separate output, [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions), not this route's acquired object.
Operational authority: Allows model reasoning and tool/action choice. Force: Evidence supply, not endorsement.
Epistemic authority and scope: Imported content acquired, not newly produced knowledge.
Behavioral-authority path: Task model; task prompt/tool messages; advisory; current rollout.
Evidence: SRC-1 Appendix B; §2, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Evidence/tool observations
- Later read-back: Training evidence can reach later analysts through raw traces
- Delegated visibility: Task-specific evidence, not all backend state
- Selection predicate: Task setup and model-chosen queries/actions
- Invalidation or expiry: uninspected — tool context lifetime and source invalidation unavailable
- Activation or effect: Declared evidence-conditioned prediction
- Evidence limits: No retrieval implementation, source authentication or run bundle
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected



> Following the setup in Yang et al. (2026), the agent is provided with pre-parsed oracle reference pages as initial document evidence in the prompt, while retaining access to local text-processing tools (glob, grep, read) to search, cross-reference, and inspect full Treasury bulletin files on disk.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-RTE-wiki-diagnosis
Label: Wiki diagnostic checking

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Distinct identity: the check/evidence production phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Trace actions, outcome contrasts and adherence to existing skill guidance. Maintainer model comparing sampled successes/failures; bounded training experience.
Context/state/action effects and timing: After training, before wiki editing. Result: Requested diagnosis and assessment of guidance usefulness.
Operational authority: Guides which explanations and workarounds to write. Force: Advisory to the same model’s edits.
Epistemic authority and scope: Model interpretation of sampled records, not independently warranted root cause.
Behavioral-authority path: Maintainer; sampled logs/current wiki; advisory; current edit and later rounds.
Evidence: SRC-1 Appendix E.2; Appendix C, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Diagnostic judgment carried into maintainer JSON
- Later read-back: Diagnosis can be encoded in later pattern/log content
- Delegated visibility: At most eight traces, up to five failures/three successes; 15,000-character cap per trace
- Selection predicate: Harness stratifies; model interprets differences
- Invalidation or expiry: uninspected — no diagnostic-result invalidation policy supplied
- Activation or effect: Requested content-directed assessment, actual assessment unobserved
- Evidence limits: Outcome contrast does not isolate cause; truncated evidence can omit relevant actions
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Model proposes diagnoses and edits; no separate human or software content veto is described. Training outcomes come from benchmark ground truth/scoring, not a model-invented oracle. This is bounded evolution, not open-request fact checking. For formulated-theory assessment, see the parent’s separately bounded theory-builder conditions 1–4: a requested check of guidance is not a supplied claim/result/blame/revision transcript.

> 4. Check whether the agent followed any active skills, and whether the skill guidance was helpful or not
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-RTE-wiki-formulation
Label: Wiki claim formulation

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Distinct identity: the content transformation phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Trace observations and existing wiki → descriptions, explanations, fixes, index and log. Maintainer model; meaningful/generalizable observation rule.
Context/state/action effects and timing: Each maintenance call after diagnosis. Result: New/refined candidate claims and action advice.
Operational authority: Requests new pattern pages or patches and a replacement index. Force: Proposed edit content.
Epistemic authority and scope: Could reshape observations, derive claims, or conjecture causes; exact semantic edge unresolved.
Behavioral-authority path: Maintainer → filesystem edit executor; JSON; requested write; future rounds.
Evidence: SRC-1 §3.2.2; Appendix E.2, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Pattern edits, full index and log append
- Later read-back: If applied, future maintainer/proposer contexts receive content
- Delegated visibility: Sampled/capped logs plus full current wiki
- Selection predicate: Model chooses new/refined patterns; duplicate avoidance instructed
- Invalidation or expiry: Can be revised by subsequent span patches
- Activation or effect: Declared formulation and revision, not demonstrated generalization
- Evidence limits: No actual input/output pair establishes entailment or non-entailment; novelty language alone is insufficient
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Descriptions, causal explanations, index summaries and log prose have different roles (separate objects), but share one authoring mechanism. Source-native deep-analysis and exact-command guidance shapes edits; model decides and surrounding software applies. No per-content human approval is specified. The parent supplies the independent condition-by-condition theory account, addressability, persistence, learning, reflection and autonomy limits.

> 2. Use "append" to add new evidence. Use "replace" to fix or refine existing text.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-RTE-wiki-retention
Label: Wiki write and retention

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Distinct identity: the retention phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Authored patterns/index/log admitted to persistent wiki. Maintainer edit selection, system application; no separate content acceptance criterion described.
Context/state/action effects and timing: Before skill proposal, independent of subsequent score acceptance. Result: Wiki retained even after skill rejection.
Operational authority: Keeps candidates available for future proposals. Force: Operational persistence, not epistemic acceptance.
Epistemic authority and scope: No evidenced evidence-consuming acceptance of each causal/general claim.
Behavioral-authority path: Later maintainer/proposer; wiki context/read_file; advisory; evolution rounds.
Evidence: SRC-1 §3.2.2–3.2.4; Appendix E.2, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Updated wiki workspace
- Later read-back: Persistent patterns/index/log for later invocations
- Delegated visibility: Maintainer gets wiki context; proposer starts with index/history, reads pages selectively
- Selection predicate: Model-specified edits; index regeneration
- Invalidation or expiry: No skill-rejection rollback; later edits possible; automated pruning lacking (§7)
- Activation or effect: Declared durable candidate availability
- Evidence limits: Parser correctness, partial writes and actual persistence uninspected
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Admitting text is distinct from accepting its truth. Computational authorship/application are described; human contribution is dataset/setup, not per-page approval. Rejection ability for malformed edits and content-review veto are uninspected. Pattern, index and log remain separate objects because their downstream selection and lineage differ.

#### EPI-RTE-validation-scoring
Label: Validation evidence production

Part of: [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)

Distinct identity: the check/evidence production phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Candidate-conditioned [EPI-OBJ-produced-predictions](#epi-obj-produced-predictions) versus benchmark references from [EPI-OBJ-imported-evidence](#epi-obj-imported-evidence). Domain scoring function then arithmetic mean; validation tasks, not explanation truth.
Context/state/action effects and timing: After provisional application and validation rollout, before comparison. Result: Per-task scores and candidate validation mean.
Operational authority: Supplies comparison input; not itself admission. Force: Evidence for software admission.
Epistemic authority and scope: Performance on specified examples under the stated scoring contract only.
Behavioral-authority path: Harness comparator; numeric score; decision input; current candidate.
Evidence: SRC-1 §2; §3.2.4; Appendix A/B, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Validation score
- Later read-back: Score later written to impact history
- Delegated visibility: Gate sees aggregate; proposer later receives audit
- Selection predicate: Fixed validation split; candidate skill configuration
- Invalidation or expiry: Superseded by next evaluation, no estimator correction described
- Activation or effect: Specified metric evaluation, no inspected scorer execution
- Evidence limits: Exact scorer, reference correctness and model stochasticity uninspected; small validation sets introduce noise
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Benchmark datasets supply expected outcomes; model generates predictions, not its own answer oracle. Human dataset/setup contribution is external. A finite score does not test every rule, explanation or future domain.

> The correctness of the prediction is evaluated by a domain-specific scoring function f⁡(y^i,yi)∈[0,1]f(\hat{y}_{i},y_{i})\in[0,1].
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-RTE-skill-disposition
Label: Skill acceptance or rollback

Part of: [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)

Distinct identity: the disposition/acceptance phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Candidate skill set versus best validation threshold. Harness strict greater-than numeric comparison; benchmark optimization domain.
Context/state/action effects and timing: After scoring; baseline initialized from empty skills. Result: Accept improvement, reject equality/decrease and restore incumbent.
Operational authority: Permits future active skill use or blocks rejected candidate from active set. Force: Enforcing in declared algorithm only.
Epistemic authority and scope: Acceptance for use as validation-improving procedural configuration, not truth endorsement.
Behavioral-authority path: Harness; score comparison and restore; enforcing protocol; subsequent iterations.
Evidence: SRC-1 §3.2.4; Appendix A, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Decision, active configuration and updated threshold if accepted
- Later read-back: Active text and decision history later consumed
- Delegated visibility: Single-skill proposal applied within incumbent full set
- Selection predicate: Score strictly exceeds incumbent best
- Invalidation or expiry: Rejection restores skills only; no wiki rollback
- Activation or effect: Specified operational acceptance; implementation and exercised benefit unavailable
- Evidence limits: No unseen-task guarantee or attribution to each individual rule
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Proposer model authors; harness decides/vetoes; no per-candidate human approval described. Proposal guidance is wiki, traces and impact history (parent proposal route). Acceptance criterion is explicit, evidence-consuming and scope-limited. Neutral changes are rejected even if potentially useful later. Rejected content can still influence future proposals through wiki/history.

#### EPI-RTE-impact-retention
Label: Impact audit retention

Part of: [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)

Distinct identity: the retention phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Proposal diff, score and decision → audit entry. Outer harness programmatically records outcome.
Context/state/action effects and timing: After either acceptance or rejection. Result: Appended intervention/outcome history.
Operational authority: Enables later avoidance or reconsideration of failed approaches. Force: Durable feedback supply.
Epistemic authority and scope: Records what was tried and scored if logging is faithful; no mechanism/transfer warrant.
Behavioral-authority path: Later proposer; skill-impact.md; advisory; later rounds. Maintainer tracker delivery remains uncertain: §3.1/§3.2.2's broad history/full-wiki descriptions exceed E.2's explicit input enumeration.
Evidence: SRC-1 §3.2.4; §5.3, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: History entry
- Later read-back: Initially supplied to later proposer; necessarily complete maintainer tracker supply is unresolved because E.2 enumerates index, log and pattern pages, unlike §3.1/§3.2.2's broad history/full-wiki wording
- Delegated visibility: Diff, metadata, score and decision, not all hidden evaluation state
- Selection predicate: Every validation result, not just successes
- Invalidation or expiry: Persists across skill rollback; no automated wiki pruning
- Activation or effect: Declared feedback retention; case study reports later use
- Evidence limits: No audit artifacts to verify completeness or fidelity; §3.2.4's unified diff and E.3's full rejected-content wording do not establish whole-file reconstructability. E.2's input list does not establish complete maintainer tracker delivery
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected



#### EPI-RTE-skill-integration
Label: Accepted skill integration

Part of: [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)

Distinct identity: the lifecycle integration phase of that container; parent findings remain valid, no supersession needed.
Endpoints, progression and owner: Accepted configuration becomes active instruction organization. Harness preserves accepted skill set after strict score decision.
Context/state/action effects and timing: After acceptance, before later task invocation. Result: Accepted content available for full prompt injection.
Operational authority: Changes instruction source for future inference. Force: Configuration-changing, then model-interpreted guidance.
Epistemic authority and scope: Integrates operationally accepted procedures; does not validate motivating explanations.
Behavioral-authority path: Task agent; full active skill system prompt; advisory guidance; later tasks/evolution/final evaluation.
Evidence: SRC-1 §3.2.4; §3.2.1, doctrine/design; parent supplies supporting passages where none is repeated here.

- Immediate return: Active accepted skill set
- Later read-back: Full active skills injected in later tasks
- Delegated visibility: No relevance retrieval; full active skill text
- Selection predicate: Accepted configuration only
- Invalidation or expiry: Later accepted edits supersede; rejection restores incumbent
- Activation or effect: Declared integration; actual behavioral dependence unobserved
- Evidence limits: PURPOSE.md links origin by design; evidence-link accuracy not separately checked
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

This is a material phase of the parent gate, distinct from retention and the score decision. Downstream delivery/force is separately declared by [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection). No automatic claim-level acceptance/integration of wiki explanations follows.

### Claims

#### EPI-CLM-knowledge-growth
Label: Increasingly supported knowledge

Claimed operation: SRC-1 introduction and §6 describe increasingly well-supported and integrated knowledge from accumulated experience. Distinct from [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit), which owns a numerical bundled-treatment contrast; this record assesses the broader warrant language.

> This layer allows skill development to build on increasingly well-supported and integrated knowledge across iterations, rather than on knowledge scattered across skill-evolution artifacts.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

Design support: [EPI-RTE-wiki-diagnosis](#epi-rte-wiki-diagnosis), [EPI-RTE-wiki-formulation](#epi-rte-wiki-formulation), [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) and [EPI-RTE-skill-disposition](#epi-rte-skill-disposition). Reported-operation evidence is the simplified §5.3 case, not an observed-run artifact:

> At Iteration 0, the Wiki Maintainer identifies a basic looping behavior (take-examine-move-loop.md), while the Skill Proposer proposes goal-directed-action, which fails to improve performance on the validation set and is rejected. Crucially, skill-impact.md preserves the proposal diff and rejection outcome, allowing subsequent skill updates to account for this failed attempt.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

Supported conclusion: the source declares evidence-linked candidate refinement and validation-selected procedures. It does not independently establish accepted ampliative explanatory knowledge. The prospective universal force of Never Return an Item to Its Origin Location is not entailed by a finite sample; however the capture does not supply the full upstream claim/input pair needed to classify that particular generation edge. The task-performance check does not itself adjudicate the proposed loop explanation.

Implementation and observed-run support: unavailable in capture. Causal support: reported ablations and examples, not independent raw-run evidence; see [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit). Disconfirming scope: wiki retention bypasses skill rejection, and the paper acknowledges noisy gating and absent pruning. These qualify, rather than erase, the positive declared feedback pathway.

> Following established setups in prior work (Yang et al., 2026; Alzubi et al., 2026), benchmark validation splits are relatively small, which can introduce evaluation noise into gating decision.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> Third, the Wiki Layer continuously accumulates pattern pages, evolution logs, and proposal diffs across iterations, but WikiSkill currently lacks an automated mechanism to prune the wiki.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

#### EPI-CLM-objective-audit
Label: Ground-truth intervention audit

Claimed warrant: SRC-1 §3.2.4 calls the harness-written history an objective, ground-truth audit trail. This is distinct from [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) and is supported as design by the audit phase [EPI-RTE-impact-retention](#epi-rte-impact-retention), not as a truth oracle for the whole wiki.

> providing an objective, ground-truth audit trail of past interventions that the Skill Proposer can consult in subsequent iterations to avoid repeating failed modifications.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

Supported conclusion: faithful harness logging would ground what proposal was evaluated, its measured score and its disposition. It does not certify a pattern’s causal explanation, independent effect of a changed clause, or general uselessness of a rejected approach. The proposer instruction not to repeat rejected approaches is behavior-shaping advice extending from a context-bound result. Implementation, authentic log artifacts and observed enforcement are uninspected; the reported case in [EPI-CLM-knowledge-growth](#epi-clm-knowledge-growth) supports attributed historical use only. No independent causal attribution follows.
