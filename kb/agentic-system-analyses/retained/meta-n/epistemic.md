---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Meta-n epistemic routes: candidate strategy generation, benchmark checks, operational selection and bounded warrant."
run-id: AAS-2026-10-14-meta-n-18c23b6f8bb4-01
reviewed-boundary: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
---

# Meta-n epistemic report

## Source-and-claim boundary

See [boundary and evidence](boundary.md#boundary-and-evidence) and the [Source register](boundary.md#source-register). The selected whole-system boundary is the shipped improvement plane, including its native and external solver consumers. This report asks what content it produces or acquires, what the checks license, and how results affect subsequent behavior. All direct inspection below is SRC-1 implementation or doctrine/design at the frozen revision; no target execution was performed. Supplied runtime findings are provisional source-grounded accounts, not observed runs.

Material objects are task statements, generated solutions and strategy explanations, evaluator outcomes, retained chains, model-produced summaries and post-run analytical propositions. Executable policy is assessed even when no particular truth-apt proposition can be individuated. Scope does not turn arbitrary code into an accepted theory. Provider weights, external datasets and upstream evaluator/SDK internals are not independently frozen. Their absence prevents weight-learning, source-label truth, upstream-oracle validity and end-to-end success conclusions. No supplied campaign trace establishes that any generated rationale was formulated, checked or accepted. No intervention comparison establishes causal depth or component benefit.

Public claims assessed: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement), [EPI-CLM-verified-channel](#epi-clm-verified-channel) and [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary). The first two are design/reported claims, not observed evidence. Budget authority is outside truth checking but remains a material continuation control; see [RT-CLM-budget-bound](runtime.md#rt-clm-budget-bound).

### Coverage

| Entry point or operation | SRC-1 source path | Coverage basis and records | Remaining limit / conclusion prevented |
|---|---|---|---|
| Installed CLI and dispatch | `pyproject.toml`, `meta_n/main.py` | Direct entry-point search; supplied [RT-RTE-native-solve](runtime.md#rt-rte-native-solve), [RT-RTE-external-spine](runtime.md#rt-rte-external-spine) | CLI feature activation is configuration-specific; no invocation observed. |
| Ω generation, rationales and feedback | `meta_n/core/omega.py`, `meta_n/core/prompts.py` | Direct prompt and context-stack reads; [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-OBJ-rationale](runtime.md#rt-obj-rationale) | No concrete generated claim supports entailment, non-entailment or content-directed criticism. |
| Native preprocessing/helpers, frozen source and debug | `meta_n/core/meta_layer.py` | Direct wrapper/debug reads; supplied [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection), [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing), [RT-RTE-native-solve](runtime.md#rt-rte-native-solve) | Checks on emitted context's truth are not established by execution screening. |
| Native agentic context replacement | `meta_n/core/agentic_solver.py` | Direct summarizer read; [EPI-RTE-summary-replacement](#epi-rte-summary-replacement), supplied [RT-RTE-agentic-loop](runtime.md#rt-rte-agentic-loop) | Summary fidelity and actual use remain unobserved. |
| Generation gate; helper check/filter; best index | `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/archive.py`, `meta_n/core/verified_code.py` | Direct gate, helper filter/verifier and archive-add reads; new check/disposition records below | No check is a universal correctness or generalization criterion. |
| Classification oracle and feedback | `meta_n/integrations/text_classification.py`, `meta_n/integrations/benchmark.py` | Direct scoring/normalization and adapter-to-trace reads; [EPI-RTE-classification-check](#epi-rte-classification-check) | Dataset-label truth and uninspected F1 implementation remain outside this assessment. |
| CO-Bench helper oracle and ordinary scoring | `meta_n/integrations/co_bench.py` | Direct crew harness/factory and split-evaluation reads; [EPI-RTE-helper-check](#epi-rte-helper-check) | Dataset/config implementation unavailable; signature/deploy equivalence not independently proved. |
| External SDK tools, cleanup and scorer | `scripts/oh_runner.py`, `scripts/t2_runner.py`, `meta_n/core/external_agents/solver.py` | Supplied [RT-RTE-external-spine](runtime.md#rt-rte-external-spine), [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary) | No fresh direct SDK audit; cleanup bounds workspace lifetime, not truth or rollback of effects. |
| Within-layer and downstream repair | `meta_n/core/evolutionary_orchestrator.py` | Supplied [RT-RTE-within-refine](runtime.md#rt-rte-within-refine), [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair); direct gate-failure branch contract read | Requests to diagnose failures do not establish correct blame or explanatory transfer. |
| Persistence, resume and final test consumers | `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`, `meta_n/core/evolutionary_orchestrator.py` | Supplied [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing) | Configuration drift and inherited traces prevent treating stored scores as fresh replay evidence. |
| Post-run best-of-K comparison | `meta_n/analysis/best_of_k.py` | Complete direct read; [EPI-RTE-arm-report](#epi-rte-arm-report) | Reporting criterion does not enforce compute parity or causal design. |
| Other benchmark oracles | `meta_n/integrations/arc_agi.py`, `meta_n/integrations/openevolve.py`, `meta_n/integrations/swe_bench.py`, `meta_n/integrations/terminal_bench/` | Scoped operation search and supplied runtime only | Detailed evaluator algorithms not assessed; prevents system-complete negative about evidence-consuming acceptance or all outcome domains. |
| Other post-run analysis and synthetic data | `meta_n/analysis/metrics.py`, `meta_n/analysis/emergent_roles.py`, `meta_n/analysis/depth_attribution.py`, `meta_n/analysis/injection_telemetry.py`, `meta_n/analysis/telemetry.py`, `scripts/generate_synthetic_sr.py` | Scoped function/score search, not semantic audit | Includes heuristic roles, embeddings, attribution/verdict and data-generation routes not fully inspected; prevents a system-wide knowledge-production negative. |

The source has one installed `meta-n` entry point. The supplied runtime additionally establishes preprocessing hooks, Python/bash helper staging, native code actions, SDK terminal/file editing and frozen-map dispatch. These are separate effect channels, not a registered universal truth-check tool. No source-supported premise permits equating a finished SDK conversation with benchmark success. Available uninspected operations above are inspection limits, not access gaps or evidenced absences.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-pre-process](runtime.md#rt-obj-pre-process) | No individuated claim in unsupplied preprocessing source | see [RT-OBJ-pre-process](runtime.md#rt-obj-pre-process) | SRC-1 `meta_n/core/meta_layer.py` | Executable policy, not automatically an assertion. |
| [EPI-OBJ-additional-context](#epi-obj-additional-context) | Potential strategy/context assertions emitted by preprocessing | see [EPI-OBJ-additional-context](#epi-obj-additional-context) | SRC-1 `meta_n/core/meta_layer.py` | String typing does not establish truth. |
| [EPI-OBJ-code-library-python](#epi-obj-code-library-python) | Helper behavior may instantiate a proposed strategy; no particular proposition individuated | see [EPI-OBJ-code-library-python](#epi-obj-code-library-python) | SRC-1 `meta_n/core/verified_code.py` | Entry-point checks do not cover all dependencies. |
| [EPI-OBJ-code-library-bash](#epi-obj-code-library-bash) | Executable policy; no particular truth-apt content individuated | see [EPI-OBJ-code-library-bash](#epi-obj-code-library-bash) | SRC-1 `meta_n/core/evolutionary_orchestrator.py` | Python value gate does not cover this part. |
| [RT-OBJ-rationale](runtime.md#rt-obj-rationale) | Proposed explanations of failure patterns and improvements | see [RT-OBJ-rationale](runtime.md#rt-obj-rationale) | SRC-1 `meta_n/core/omega.py` | No rationale instance or separate rationale acceptance decision. |
| [RT-OBJ-task-solution-map](runtime.md#rt-obj-task-solution-map) | Task-specific source and inherited outcome association | see [RT-OBJ-task-solution-map](runtime.md#rt-obj-task-solution-map) | SRC-1 `meta_n/core/meta_layer.py` | Assembly is not fresh execution or new-task evidence. |
| [EPI-OBJ-predictions](#epi-obj-predictions) | Class assertions over the supplied examples | see [EPI-OBJ-predictions](#epi-obj-predictions) | SRC-1 `meta_n/integrations/text_classification.py` | Imported reference labels are not independently validated truths. |
| [EPI-OBJ-eval-result](#epi-obj-eval-result) | Scoped success/score propositions | see [EPI-OBJ-eval-result](#epi-obj-eval-result) | SRC-1 `meta_n/integrations/benchmark.py` | Numeric outcomes do not warrant the proposed strategy mechanism. |
| [EPI-OBJ-eval-feedback](#epi-obj-eval-feedback) | Textual comparison and mismatch evidence | see [EPI-OBJ-eval-feedback](#epi-obj-eval-feedback) | SRC-1 `meta_n/integrations/text_classification.py` | Feedback interpretation is separate from symbolic score consumption. |
| [EPI-OBJ-prior-summary](#epi-obj-prior-summary) | Model account of previous actions and outcomes | see [EPI-OBJ-prior-summary](#epi-obj-prior-summary) | SRC-1 `meta_n/core/agentic_solver.py` | Semantic preservation indeterminate. |
| [EPI-OBJ-arm-report](#epi-obj-arm-report) | Comparative score/count/p-value claims | see [EPI-OBJ-arm-report](#epi-obj-arm-report) | SRC-1 `meta_n/analysis/best_of_k.py` | Arithmetic warrants conditional on accurate and comparable inputs. |

Distributed-parametric components are see [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-inner-llm](runtime.md#rt-cmp-inner-llm), [RT-CMP-external-backend](runtime.md#rt-cmp-external-backend). Each has unpinned provider state and no inspected Meta-n training call. This does not negate adaptation through retained code or summaries; provider-side parameter changes remain uninspected. Optional analytical embeddings are an unassessed alternative, not evidence of training.

## Authority-route ledger

Fields owned by canonical records say `see`; the overlay adds function, architectural status and content/update relation. Repeated citations with different functions deliberately separate checking, disposition and retention.

Route ID: [RT-RTE-native-solve](runtime.md#rt-rte-native-solve)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-RTE-native-solve](runtime.md#rt-rte-native-solve)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve).
Evaluator/condition and domain: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve).
Activation and timing: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve).
Possible or observed result: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve); no operation observed.
Implemented force: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve).
Epistemic authority and scope: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve); Task import preserves the supplied text but its source warrant is unknown. Model-produced solution assertions are separately indeterminate: no generated instance establishes entailment or non-entailment.
Operational authority: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve).
Behavioral-authority path: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve).
Evidence source ID and local anchor: see [RT-RTE-native-solve](runtime.md#rt-rte-native-solve) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Task import preserves the supplied text but its source warrant is unknown. Model-produced solution assertions are separately indeterminate: no generated instance establishes entailment or non-entailment.

Route ID: [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-rationale](runtime.md#rt-obj-rationale)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Evaluator/condition and domain: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Activation and timing: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Possible or observed result: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); no operation observed.
Implemented force: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Epistemic authority and scope: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); Ω may infer novel strategies, copy prior content or derive from it. Requested novelty is not evidence of non-entailment; actual output and premises are needed.
Operational authority: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Behavioral-authority path: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Evidence source ID and local anchor: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Ω may infer novel strategies, copy prior content or derive from it. Requested novelty is not evidence of non-entailment; actual output and premises are needed.

Route ID: [EPI-RTE-classification-check](#epi-rte-classification-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-eval-result](#epi-obj-eval-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see [EPI-RTE-classification-check](#epi-rte-classification-check).
Evaluator/condition and domain: see [EPI-RTE-classification-check](#epi-rte-classification-check).
Activation and timing: see [EPI-RTE-classification-check](#epi-rte-classification-check).
Possible or observed result: see [EPI-RTE-classification-check](#epi-rte-classification-check); no operation observed.
Implemented force: see [EPI-RTE-classification-check](#epi-rte-classification-check).
Epistemic authority and scope: see [EPI-RTE-classification-check](#epi-rte-classification-check); The checked arithmetic derives match fractions from supplied labels and predictions, not the truth of medical labels.
Operational authority: see [EPI-RTE-classification-check](#epi-rte-classification-check).
Behavioral-authority path: see [EPI-RTE-classification-check](#epi-rte-classification-check).
Evidence source ID and local anchor: see [EPI-RTE-classification-check](#epi-rte-classification-check) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: The checked arithmetic derives match fractions from supplied labels and predictions, not the truth of medical labels.

Route ID: [EPI-RTE-gate-check](#epi-rte-gate-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-eval-result](#epi-obj-eval-result)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-gate-check](#epi-rte-gate-check).
Evaluator/condition and domain: see [EPI-RTE-gate-check](#epi-rte-gate-check).
Activation and timing: see [EPI-RTE-gate-check](#epi-rte-gate-check).
Possible or observed result: see [EPI-RTE-gate-check](#epi-rte-gate-check); no operation observed.
Implemented force: see [EPI-RTE-gate-check](#epi-rte-gate-check).
Epistemic authority and scope: see [EPI-RTE-gate-check](#epi-rte-gate-check); Comparative gate result depends on sampled task scores and success.
Operational authority: see [EPI-RTE-gate-check](#epi-rte-gate-check).
Behavioral-authority path: see [EPI-RTE-gate-check](#epi-rte-gate-check).
Evidence source ID and local anchor: see [EPI-RTE-gate-check](#epi-rte-gate-check) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Comparative gate result depends on sampled task scores and success.

Route ID: [EPI-RTE-gate-disposition](#epi-rte-gate-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-eval-result](#epi-obj-eval-result)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).
Evaluator/condition and domain: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).
Activation and timing: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).
Possible or observed result: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition); no operation observed.
Implemented force: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).
Epistemic authority and scope: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition); Acceptance for candidate trial continuation, not acceptance of its explanation.
Operational authority: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).
Behavioral-authority path: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).
Evidence source ID and local anchor: see [EPI-RTE-gate-disposition](#epi-rte-gate-disposition) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Acceptance for candidate trial continuation, not acceptance of its explanation.

Route ID: [EPI-RTE-helper-check](#epi-rte-helper-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see [EPI-RTE-helper-check](#epi-rte-helper-check).
Evaluator/condition and domain: see [EPI-RTE-helper-check](#epi-rte-helper-check).
Activation and timing: see [EPI-RTE-helper-check](#epi-rte-helper-check).
Possible or observed result: see [EPI-RTE-helper-check](#epi-rte-helper-check); no operation observed.
Implemented force: see [EPI-RTE-helper-check](#epi-rte-helper-check).
Epistemic authority and scope: see [EPI-RTE-helper-check](#epi-rte-helper-check); Crew measurements and threshold result are conditional on upstream config and emitted JSON integrity; stub has no evidential result.
Operational authority: see [EPI-RTE-helper-check](#epi-rte-helper-check).
Behavioral-authority path: see [EPI-RTE-helper-check](#epi-rte-helper-check).
Evidence source ID and local anchor: see [EPI-RTE-helper-check](#epi-rte-helper-check) (SRC-1).
Claim IDs or none: [EPI-CLM-verified-channel](#epi-clm-verified-channel).
Mismatch marker or none: entry-point-only / dependency restoration / stub fallback.
Gap/limit: Crew measurements and threshold result are conditional on upstream config and emitted JSON integrity; stub has no evidential result.

Route ID: [EPI-RTE-helper-disposition](#epi-rte-helper-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition).
Evaluator/condition and domain: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition).
Activation and timing: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition).
Possible or observed result: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition); no operation observed.
Implemented force: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition).
Epistemic authority and scope: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition); Admission license applies to the tested entry point/configuration; dependency restoration has a distinct operational, not value-verified, license.
Operational authority: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition).
Behavioral-authority path: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition).
Evidence source ID and local anchor: see [EPI-RTE-helper-disposition](#epi-rte-helper-disposition) (SRC-1).
Claim IDs or none: [EPI-CLM-verified-channel](#epi-clm-verified-channel).
Mismatch marker or none: entry-point-only / dependency restoration / stub fallback.
Gap/limit: Admission license applies to the tested entry point/configuration; dependency restoration has a distinct operational, not value-verified, license.

Route ID: [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)
Content/update relation: no content change
Transition or check target: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Evaluator/condition and domain: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Activation and timing: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Possible or observed result: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); no operation observed.
Implemented force: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Epistemic authority and scope: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); Evaluated candidates remain available even when worse. Retention alone is not claim acceptance or lifecycle integration.
Operational authority: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Behavioral-authority path: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Evidence source ID and local anchor: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Evaluated candidates remain available even when worse. Retention alone is not claim acceptance or lifecycle integration.

Route ID: [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)
Content/update relation: no content change
Transition or check target: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Evaluator/condition and domain: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Activation and timing: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Possible or observed result: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); no operation observed.
Implemented force: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Epistemic authority and scope: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); Score/elite/UCB selection grants breeding opportunity, not explanatory warrant. Best-index bars do not withdraw the archived capability.
Operational authority: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Behavioral-authority path: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission).
Evidence source ID and local anchor: see [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Score/elite/UCB selection grants breeding opportunity, not explanatory warrant. Best-index bars do not withdraw the archived capability.

Route ID: [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-pre-process](runtime.md#rt-obj-pre-process)
Content/update relation: no content change
Transition or check target: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Evaluator/condition and domain: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Activation and timing: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Possible or observed result: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance); no operation observed.
Implemented force: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Epistemic authority and scope: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance); Guidance is model-interpreted and advisory; no truth check on emitted context is established.
Operational authority: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Behavioral-authority path: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Evidence source ID and local anchor: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Guidance is model-interpreted and advisory; no truth check on emitted context is established.

Route ID: [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)
Content/update relation: non-truth-apt policy/content update: executable helper or script organization
Transition or check target: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection).
Evaluator/condition and domain: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection).
Activation and timing: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection).
Possible or observed result: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection); no operation observed.
Implemented force: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection).
Epistemic authority and scope: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection); Execution authority differs from measured correctness and from model adoption.
Operational authority: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection).
Behavioral-authority path: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection).
Evidence source ID and local anchor: see [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Execution authority differs from measured correctness and from model adoption.

Route ID: [RT-RTE-within-refine](runtime.md#rt-rte-within-refine)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-rationale](runtime.md#rt-obj-rationale)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine).
Evaluator/condition and domain: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine).
Activation and timing: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine).
Possible or observed result: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine); no operation observed.
Implemented force: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine).
Epistemic authority and scope: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine); Failure feedback requests a repaired proposal; a actual claim/result/blame account is unsupplied.
Operational authority: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine).
Behavioral-authority path: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine).
Evidence source ID and local anchor: see [RT-RTE-within-refine](runtime.md#rt-rte-within-refine) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Failure feedback requests a repaired proposal; a actual claim/result/blame account is unsupplied.

Route ID: [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)
Content/update relation: non-truth-apt policy/content update: intermediate injection replacement
Transition or check target: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair).
Evaluator/condition and domain: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair).
Activation and timing: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair).
Possible or observed result: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair); no operation observed.
Implemented force: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair).
Epistemic authority and scope: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair); Mean-score classification does not establish causal blame; non-improving variants can still be archived.
Operational authority: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair).
Behavioral-authority path: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair).
Evidence source ID and local anchor: see [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Mean-score classification does not establish causal blame; non-improving variants can still be archived.

Route ID: [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-task-solution-map](runtime.md#rt-obj-task-solution-map)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing).
Evaluator/condition and domain: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing).
Activation and timing: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing).
Possible or observed result: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing); no operation observed.
Implemented force: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing).
Epistemic authority and scope: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing); Deterministic assembly preserves stored task winners. Its aggregate does not entail a freshly achieved combined score.
Operational authority: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing).
Behavioral-authority path: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing).
Evidence source ID and local anchor: see [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing) (SRC-1).
Claim IDs or none: [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement).
Mismatch marker or none: none.
Gap/limit: Deterministic assembly preserves stored task winners. Its aggregate does not entail a freshly achieved combined score.

Route ID: [EPI-RTE-summary-replacement](#epi-rte-summary-replacement)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-prior-summary](#epi-obj-prior-summary)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Evaluator/condition and domain: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Activation and timing: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Possible or observed result: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement); no operation observed.
Implemented force: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Epistemic authority and scope: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement); Possible non-ampliative compression, omission or new inference cannot be separated without input/output instances and a fidelity check.
Operational authority: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Behavioral-authority path: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Evidence source ID and local anchor: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Possible non-ampliative compression, omission or new inference cannot be separated without input/output instances and a fidelity check.

Route ID: [EPI-RTE-summary-replacement](#epi-rte-summary-replacement)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-prior-summary](#epi-obj-prior-summary)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Evaluator/condition and domain: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Activation and timing: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Possible or observed result: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement); no operation observed.
Implemented force: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Epistemic authority and scope: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement); Unvalidated summary enters the next foreground turn, so its consequence is material even without epistemic acceptance.
Operational authority: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Behavioral-authority path: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement).
Evidence source ID and local anchor: see [EPI-RTE-summary-replacement](#epi-rte-summary-replacement) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Unvalidated summary enters the next foreground turn, so its consequence is material even without epistemic acceptance.

Route ID: [EPI-RTE-arm-report](#epi-rte-arm-report)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-arm-report](#epi-obj-arm-report)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Evaluator/condition and domain: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Activation and timing: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Possible or observed result: see [EPI-RTE-arm-report](#epi-rte-arm-report); no operation observed.
Implemented force: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Epistemic authority and scope: see [EPI-RTE-arm-report](#epi-rte-arm-report); Scope is deterministic statistics from inputs, not causal superiority or generalization.
Operational authority: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Behavioral-authority path: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Evidence source ID and local anchor: see [EPI-RTE-arm-report](#epi-rte-arm-report) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Scope is deterministic statistics from inputs, not causal superiority or generalization.

Route ID: [EPI-RTE-arm-report](#epi-rte-arm-report)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-arm-report](#epi-obj-arm-report)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Evaluator/condition and domain: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Activation and timing: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Possible or observed result: see [EPI-RTE-arm-report](#epi-rte-arm-report); no operation observed.
Implemented force: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Epistemic authority and scope: see [EPI-RTE-arm-report](#epi-rte-arm-report); Printed/written comparison is advisory to an operator; no automated archive or deployment veto consumes it.
Operational authority: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Behavioral-authority path: see [EPI-RTE-arm-report](#epi-rte-arm-report).
Evidence source ID and local anchor: see [EPI-RTE-arm-report](#epi-rte-arm-report) (SRC-1).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Printed/written comparison is advisory to an operator; no automated archive or deployment veto consumes it.

No lifecycle integration of an accepted strategy explanation is established on these inspected routes. This is a route-local limit, not a system-complete absence: the unassessed analytical verdict routes prevent that broader negative. Retaining a tested capability and connecting its traces to later generation are implemented, but do not independently constitute acceptance of a truth-apt mechanism claim.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement) | see [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement) | SRC-1 `README.md`; doctrine/design and attributed reported operation | see claim | [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection) | No registered empirical campaign | No intervention isolates depth, helper value or model inference | Trace-responsive code-change capacity is wired; this changes behavior-determining organization, not weights | Improved capacity, emergent roles and generalization are unestablished independently. |
| [EPI-CLM-verified-channel](#epi-clm-verified-channel) | see [EPI-CLM-verified-channel](#epi-clm-verified-channel) | SRC-1 `meta_n/core/verified_code.py`; doctrine/design | see claim | [EPI-RTE-helper-check](#epi-rte-helper-check), [EPI-RTE-helper-disposition](#epi-rte-helper-disposition), [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection) | None | One narrow held-out harness, unknown upstream oracle and JSON trust; no observed benefit | Optional entry-point check and filtering, with explicit unverified fallback | All failing helpers dropped / host never executes helper is overbroad; dependencies restored and native host paths remain. |
| [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary) | see [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary) | SRC-1 `meta_n/core/prompts.py`; doctrine/design, bounded by implementation | see claim | [RT-RTE-native-solve](runtime.md#rt-rte-native-solve), [RT-RTE-external-spine](runtime.md#rt-rte-external-spine) | None | Screening is not a proof of safety or truth | Sandbox properties are path-specific | No universal host isolation or warrant follows. |

## Bounded conclusion

Meta-n imports task descriptions and reference labels whose source warrant remains unknown. On the inspected classification route it derives normalized label-match fractions and feedback, with an enforcing code evaluator over a specified answer domain. A positive score means some matches, not complete correctness. Benchmark outcome evidence is materially distinct from the generated explanation of why an intervention works.

Ω receives selected traces, prior code and rationale. It is asked to identify patterns and propose improvements. No supplied output individuates an entailed or demonstrably ampliative claim. Thus candidate semantic relation stays indeterminate while the executable policy update capacity is implemented. Fixed doctrine and score feedback do not establish formulated criticism naming a claim, result and blame. The runtime's localized strategy capacity, executable consumption, persistence and representation-mediated feedback conclusions remain independent of exercised criticism, improved future capacity, autonomous theory building and reflective revision of method texts.

The generation gate grants operational continuation against sampled success and relative-score/floor criteria. It can reject a proposal and permit a separate repair attempt; it does not certify all-task non-regression or accept a strategy explanation. The optional crew helper gate is a narrower evidence-consuming acceptance decision: held-out full-set score above its fixed comparator plus at least 50% feasibility, for entry-point admission under that oracle. Stub-kept and dependency-restored helpers carry no equivalent license. Admission into the stored injection differs from deployment when the adapter demotes the code library. The same test split is used during this optional selection, so subsequent reporting on it is not an untouched holdout for those helper-selected candidates. This counterexample qualifies, rather than erases, the runtime's held-out value-harness finding.

Archive retention is broader than improvement selection: worse evaluated children and non-improving repropagation variants can persist. Selection, best-index promotion and bars have different effects; bars do not remove the candidate or its mean. Prior code, rationales and outcomes influence later model proposals and resumed trials. Matching frozen task scripts receive enforcing execution authority but assembly does not establish fresh outcome success. Override and filtering can withdraw live helper names; retention of prior candidates is recovery, not reversal of already incurred effects.

Agentic compaction gives an unchecked model summary advisory influence over later actions. Its operation may compress, omit or infer; no fidelity acceptance criterion is implemented in the inspected summarizer. Post-run best-of-K produces entailed arithmetic and an advisory comparison criterion, not a causal experiment. Neither a significant sign test nor compute counts alone identify a component effect.

Improvement-directed self-change is wired over the bounded search/resume horizon with task score as its independently specified objective. Trace-fed proposal, retained organization change and live authority channels establish dispositional capacity. No observed subsequent operation closes causal link 4 or proves successful improvement. No single epistemic score or whole-system knowledge-production verdict follows, especially with other evaluator and analytical routes unassessed.

## Shared records

### Operative objects

#### EPI-OBJ-additional-context
Label: Emitted additional context

Part of: [RT-OBJ-pre-process](runtime.md#rt-obj-pre-process)

Source-native identity: `additional_context`, the emitted string in the supplied preprocessing container. Representational form: natural-language guidance interpreted by the native solver or SDK model. Storage substrate: task-local context/message state, reproducible from retained preprocessing source but not necessarily identical on replay. Distinct operative part from the executable producer because string typing/screening and advisory interpretation do not share a truth check. SRC-1 `meta_n/core/meta_layer.py`, implementation; evidence and downstream authority are supplied by [RT-OBJ-pre-process](runtime.md#rt-obj-pre-process) and [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance). No emitted instance establishes its truth.

#### EPI-OBJ-code-library-python
Label: Python helper library

Part of: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)

Source-native identity: `InjectedCode.code_library`. Representational form: symbolic Python source with fixed execution semantics; advertised descriptions are a separate model-interpreted consumption path. Storage substrate: injection JSON, merged dictionary and staged/prepended source. The Python-only verifier gives this part different checks from bash. SRC-1 `meta_n/core/evolutionary_orchestrator.py`, implementation; minimum passages supplied by [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification) and [EPI-RTE-helper-disposition](#epi-rte-helper-disposition). Actual entry-point invocation and observed benefit are uninspected.

#### EPI-OBJ-code-library-bash
Label: Bash helper library

Part of: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)

Source-native identity: `InjectedCode.code_library_bash`. Representational form: symbolic bash source; signature/docstring descriptions are model-interpreted advertisements. Storage substrate: injection JSON, merged dictionary, native prepended source or external staged file. The Python value gate does not check this part. SRC-1 `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/meta_layer.py`, implementation; minimum passage for the distinct pass-through contract:

> ``pre_process`` and bash
> helpers always pass through.
> --- `meta_n/core/evolutionary_orchestrator.py`

Consumption evidence is see [RT-OBJ-code-library](runtime.md#rt-obj-code-library) and [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection); staging alone establishes no helper call or correctness.

#### EPI-OBJ-predictions
Label: Classification predictions

Source-native identity: `predictions_json` / `predictions`. Representational form: symbolic case-key-to-label mapping, with class assertions relative to examples. Storage substrate: generated solution output, parsed mapping during scoring. No supplied object counterpart after comparison: [RT-RTE-native-solve](runtime.md#rt-rte-native-solve) covers its production/execution but not this result part. Distinct from the numeric comparison result and explanatory rationale. SRC-1 `meta_n/integrations/text_classification.py`, implementation; passages and concrete comparison in [EPI-RTE-classification-check](#epi-rte-classification-check). Produced labels may be correct or incorrect; no supplied instance proves exercised generation.

#### EPI-OBJ-eval-feedback
Label: Evaluation feedback text

Source-native identity: `EvalResult.feedback` / `Trace.eval_feedback`. Representational form: natural-language interpretation of arithmetic and mismatch evidence. Storage substrate: result/trace, saved traces and subsequent rendered Ω/debug prompts. No supplied operative-object counterpart after comparison: [RT-RTE-native-solve](runtime.md#rt-rte-native-solve) covers its transport but not this text object. SRC-1 `meta_n/integrations/text_classification.py`, `meta_n/integrations/benchmark.py`, implementation. Numeric consumers and model-interpreted feedback have different force; the latter can influence new proposals without independently checking their explanation.

> feedback = f"Accuracy: {correct}/{total} = {score:.4f}"
> --- `meta_n/integrations/text_classification.py`

#### EPI-OBJ-eval-result
Label: Numeric evaluation result

Source-native identity: `EvalResult.success`, `score`, `raw_score`. Representational form: symbolic numeric/Boolean comparison results. Storage substrate: runtime result and `Trace` fields, subsequently saved through the supplied runtime persistence route. No supplied operative-object counterpart after comparison: [RT-RTE-native-solve](runtime.md#rt-rte-native-solve) covers execution but is not this result object. Distinct from strategy source [RT-OBJ-code-library](runtime.md#rt-obj-code-library), prediction mapping and feedback text. SRC-1 `meta_n/integrations/benchmark.py`, `meta_n/integrations/text_classification.py` supply implementation evidence. The wrapper preserves numeric results and feedback but truncates separate error displays; this does not validate reference-answer truth.

> success=result.success,
> score=result.score,
> error_summary=self._error_summary(result),
> eval_feedback=result.feedback,
> --- `meta_n/integrations/benchmark.py`

#### EPI-OBJ-prior-summary
Label: Prior work summary

Source-native identity: `summary` from `AgenticSolver._summarize_context`; natural-language account consumed by model interpretation. Storage substrate: replacement message list within a task frame. Distinct from [RT-OBJ-rationale](runtime.md#rt-obj-rationale): it describes the conversation, not the Ω injection. The closest supplied route [RT-RTE-agentic-loop](runtime.md#rt-rte-agentic-loop) supplies replacement wiring, not a summary object or fidelity evidence. SRC-1 `meta_n/core/agentic_solver.py`, implementation. No actual summary available; semantic preservation is indeterminate.

> to_summarize = messages[1:-keep_n]
> conversation_text = "\n\n".join(
>     f"[{m['role']}]\n{m['content']}" for m in to_summarize
> )
> --- `meta_n/core/agentic_solver.py`

#### EPI-OBJ-arm-report
Label: Best-of-K comparison report

Source-native identity: `report` constructed by `meta_n.analysis.best_of_k.main`; symbolic statistics rendered as natural-language/Markdown interpretation. Storage substrate: stdout and optional operator-selected Markdown file. No supplied counterpart after comparison; [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing) assembles solver winners, whereas this object compares already saved runs. SRC-1 `meta_n/analysis/best_of_k.py`, implementation. Output is not consumed by the search loop.

> report = "\n".join(out)
> if args.output:
>     Path(args.output).write_text(report + "\n")
> print(report)
> --- `meta_n/analysis/best_of_k.py`

### Routes

#### EPI-RTE-classification-check
Label: Classification answer measurement

Part of: [RT-RTE-native-solve](runtime.md#rt-rte-native-solve)

This is a material functional part of the supplied route, separated because its target or force differs from the enclosing sequence.

Predictions and imported example labels → `_score_predictions` / `_score_accuracy` → `EvalResult` → `AdapterExecutor` trace. Program owns the check; the model proposes predictions and cannot redefine the comparison through its completion assertion. The check target is correctness relative to supplied labels on the provided example set; reference outcome is normalized gold text. Operating mode is bounded benchmark evaluation, not human per-answer approval. Invalid JSON/non-object is rejected with zero; accuracy is matches divided by total, with at most five mismatch examples in feedback. `success=score > 0` means partial success, not universal correctness. License: exact match fraction under this normalization, conditional on label correctness. No claim that symptom labels themselves are medically true is licensed.

Concrete source deduction, not execution: one example labeled `Disease A` and prediction JSON `{"case_0":"  DISEASE   A  "}` both normalize to `disease a`; `correct=1`, `total=1`, `score=1.0`, `success=True`. Changing the prediction to `Disease B` gives `0.0` and False. The result entails a property of the provided strings, not a causal diagnostic explanation.

> def _normalize(text: str) -> str:
>     """Case-insensitive, whitespace-normalized string for comparison."""
>     return " ".join(text.lower().split())
> --- `meta_n/integrations/text_classification.py`

> score = correct / total if total > 0 else 0.0
> --- `meta_n/integrations/text_classification.py`

> success=score > 0,
> --- `meta_n/integrations/text_classification.py:932-943`

- Immediate return: Numeric result plus feedback trace
- Later read-back: Saved trace feeds later Ω and selection through the parent route
- Delegated visibility: Scorer sees predictions and gold examples; Ω receives selected/truncated trace renderings, not necessarily all examples
- Selection predicate: Valid JSON mapping and benchmark metric choose scoring branch; this record assesses accuracy only
- Invalidation or expiry: Results scoped to supplied examples/evaluator; no source-truth endorsement or automatic expiry
- Activation or effect: Scoring enforces result fields; downstream gate/ranking and feedback change opportunities for execution, not guaranteed model compliance
- Evidence limits: F1 branch, dataset provenance and operation uninspected
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-gate-check
Label: Sampled candidate gate check

Part of: [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)

This is a material functional part of the supplied route, separated because its target or force differs from the enclosing sequence.

Candidate chain plus parent per-task scores → `_gate_check` sampled solves → clearing/floor result and gate traces. Code chooses samples and repeats; evaluator supplies scores and success. The target is operational viability/relative score on the sampled tasks, not rationale truth. Missing baseline or disabled margin yields liveness-only clearing. Repeats choose the middle ordered trace with non-finite values sorted as negative infinity. With no floor, one clearing task returns immediately; with a floor, sampled regressions can veto. Reference outcomes are task executor and stored parent baseline; operator configures criteria but does not decide each check. This bounded experiment cannot certify unsampled tasks or causal mechanism.

> cleared = trace.success and (
>     baseline is None or trace.score >= baseline - margin
> )
> --- `meta_n/core/evolutionary_orchestrator.py`

> if protect is None:
>     return True, gate_n, gate_traces
> --- `meta_n/core/evolutionary_orchestrator.py`

- Immediate return: Pass Boolean, sampled count and gate traces
- Later read-back: Gate traces reused in full evaluation and supplied to optional repair on failure
- Delegated visibility: Selected solver receives task/chain; criterion sees success, score and parent baseline
- Selection predicate: Configured gate sampling/depth/repeats and success/relative margin; optional floor veto
- Invalidation or expiry: Stored baseline lacks replay freshness; no automatic epistemic expiry
- Activation or effect: Result is consumed by the separate disposition part to permit full evaluation or reject/repair
- Evidence limits: Implementation only; evaluator semantics vary by family, floor protects sampled tasks only
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-gate-disposition
Label: Candidate continuation disposition

Part of: [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)

This is a material functional part of the supplied route, separated because its target or force differs from the enclosing sequence.

Gate result → orchestrator continuation or rejection/optional separate refinement. Code decides and vetoes; Ω proposes content, human configures bounded experiment. Criterion and intended use: clearing the sampled success/relative-score gate, with configured floor, licenses further evaluation of that child, not accepted explanation or production deployment. Ordinary full evaluation then archives a child even when its mean is worse. Gate failures can guide a new proposal under the fixed repair directive; rejected proposal is not overwritten into its repair. Recovery keeps prior candidates, not rollback of execution effects. See closest parent and [RT-RTE-within-refine](runtime.md#rt-rte-within-refine) for retained code/rationale and repair evidence. No formulated theory instance is supplied; theory conditions and independent properties remain as bounded in the parent, not inferred from this veto.

Evidence passage is supplied by [RT-RTE-within-refine](runtime.md#rt-rte-within-refine) and [EPI-RTE-gate-check](#epi-rte-gate-check); additional SRC-1 `meta_n/core/evolutionary_orchestrator.py` implementation contract:

> builds a NEW candidate from the corrected injection (monotonic — the
> rejected ``buggy_child`` is never mutated or archived), re-gates it, and
> KEEPS IT iff it now clears the gate.
> --- `meta_n/core/evolutionary_orchestrator.py`

- Immediate return: Child continues to full trial or is withheld; repair can yield a distinct child
- Later read-back: Passing child code/outcomes enter archive and later generation; rejected original is not archived on this branch
- Delegated visibility: Orchestrator sees pass/traces; repair Ω sees failed traces and newest injection
- Selection predicate: Configured non-focus generation gate; optional refinement and re-gate
- Invalidation or expiry: Old parent survives; no automatic withdrawal of previously archived code
- Activation or effect: Enforcing branch controls continuation before further evaluation; later archive selection is a separate authority path
- Evidence limits: No per-content human approval, no mechanism-claim acceptance, no universal route gate
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-helper-check
Label: Crew helper value check

Part of: [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification)

This is a material functional part of the supplied route, separated because its target or force differs from the enclosing sequence.

Helper source with prior/sibling sources → signature-guarded crew verifier → Docker runner/config oracle → JSON threshold and `VerifyResult`. Target: this helper as crew entry point under the mounted config, normalization, split and resources. Only a crew-only selection returns the real factory; all other selections use the unverified stub. Program config and threshold, not proposal model, evaluate it. Human contribution is the shipped harness/reference outcome, not per-helper review. Operating mode: optional bounded helper experiment before child creation. Runner computes per-file full means with failed/nonpositive cases zeroed and aggregate feasibility. It calls `cfg.eval_func` and optional `norm_score`; their upstream correctness and comparator provenance are not established from the shipped constant.

> runner_args=["test", repr(_CREW_BEST_OF_N)],
> --- `meta_n/integrations/co_bench.py`

> out["passed"] = (out["full_mean"] > GATE
>                      and out["feasibility_rate"] >= 0.5)
> --- `meta_n/integrations/co_bench.py`

This is selection on the `test` split, despite an ordinary adapter docstring saying final reporting only. The test data need not be displayed to Ω for selection to depend on them. Do not treat later measurements on that split as independent untouched holdout evidence for helper-selected chains.

The runner's measurements support conditional outcome-fit, not mechanism truth, transfer or sandbox safety of all channels. JSON is consumed from stdout with no inspected authentication boundary between generated candidate and runner. In particular `_docker_run_json` parses the last nonempty stdout line and does not first reject nonzero process return codes. This bounds provenance and the failure-closed doctrine: a valid emitted object is trusted by the predicate. No exploit was run or asserted.

> result = json.loads(last)
> --- `meta_n/core/verified_code.py`

> ran_in_sandbox = result.get("status") != "exec_error"
> passed = bool(self.success_predicate(result))
> --- `meta_n/core/verified_code.py`

The provenance bit means invocation attempted (timeouts/no-JSON can retain True), not a separately proven helper call. Passed plus bit grants a verified-name status downstream, conditional on trustworthy runner output. This qualifies the supplied runtime's shorthand "genuinely verified"; its stub/dependency distinction remains correct.

- Immediate return: Pass/evidence/sandbox bit, or failed/crashed verifier result; stub returns unverified pass
- Later read-back: Verified-name metadata retained with injections; raw evidence is logged, not a retained explanatory proof
- Delegated visibility: Runner sees test reference data and source; Ω does not receive mounted ground truth via this factory
- Selection predicate: verified_code plus Python library; crew-solo factory or stub; signature/domain requirements
- Invalidation or expiry: Prior-source/sibling composition and later overrides can change the tested context; no fresh proof for arbitrary replay
- Activation or effect: Conditional check result feeds keep/drop and name stamping; stub gives no value evidence
- Evidence limits: No target execution, upstream config unavailable, JSON provenance and generalization unestablished
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-helper-disposition
Label: Helper keep/drop and dependency disposition

Part of: [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification)

This is a material functional part of the supplied route, separated because its target or force differs from the enclosing sequence.

`VerifyResult` → kept dictionary and sandbox-verified names → dependency closure → possibly replaced injection → child. Code admits or vetoes Python entry points; model proposes source; operator enables features but is not a per-helper approver. Intended use and scope of real acceptance: candidate helper admission for the crew value domain if the measured full-set held-out score beats the fixed comparator and feasibility is at least 50%. Failed/crashed helpers are initially dropped. Stub pass keeps all without verification. Transitive sibling calls from kept source restore needed siblings even if individually failed; restored names are not newly stamped verified. This is a separate operational dependency criterion, not acceptance against a value oracle.

> if res.passed:
>     kept[name] = source
>     if res.ran_in_sandbox:
>         sandbox_verified.add(name)
> --- `meta_n/core/evolutionary_orchestrator.py`

> if dep not in kept:
>     kept[dep] = injected.code_library[dep]
>     frontier.append(dep)
> --- `meta_n/core/evolutionary_orchestrator.py`

Preprocessing and bash pass through. CO-Bench helpers can be demoted unless `force-code-library-live` is on; record admission does not imply live deployment. Native foster/deploy requests and wrapper authority remain see [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification). Override-aware verified-name aggregation controls non-adoption bars; archive still keeps barred candidates and mean scores. This explicitly withholds best-index promotion, not execution permission or truth endorsement. Old candidates persist as recovery; no effect rollback. Guidance is fixed Ω strategy instructions and the fixed helper criterion. Actual formulated theory content remains uninspected, so this record does not upgrade criticism/learning conclusions.

> The candidate is still added in full (monotonic; mean_score intact); only the
> per-task-best index skips those tasks.
> --- `meta_n/core/archive.py`

- Immediate return: Filtered injection and verified-name set; original may remain when no source is dropped
- Later read-back: Stamped names, full chain and best-index bars survive persisted/resumed selection via parent route
- Delegated visibility: Child consumes retained source; next Ω sees selected prior injections, not a universal proof
- Selection predicate: Verifier pass then transitive dependency restoration; per-task-best bar requires live verified helper advertisement without measured call evidence
- Invalidation or expiry: Same-name unverified override clears previous live verification; prior archived candidate unchanged
- Activation or effect: Enforcing source filter / ranking bar; executable source enters later solvers only when adapter/staging permits
- Evidence limits: Stub/dependency admission lacks value warrant; call scan is syntax evidence, not runtime invocation proof
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-summary-replacement
Label: Agentic summary replacement

Part of: [RT-RTE-agentic-loop](runtime.md#rt-rte-agentic-loop)

This is a material functional part of the supplied route, separated because its target or force differs from the enclosing sequence.

Removed conversation turns → provider summary → replacement user message → subsequent foreground model turn. Program owns slicing and context thresholds; provider produces summary. No inspected fidelity evaluator or evidence-consuming acceptance stage exists here: successful return is sufficient for replacement. Check target would be semantic faithfulness to removed turns; it is not assessed by a source comparison. The summary can carry outcome/strategy assertions, but without a supplied instance neither entailment nor non-entailment can be shown. First message and last four messages remain verbatim. Advisory model interpretation is the force, within later turns of this task frame. No reload route to removed raw turns is established by the summarizer. Distinct functional part, not a duplicate of the full agentic action/observation loop. SRC-1 `meta_n/core/agentic_solver.py`, implementation; parent supplies threshold/recovery evidence.

> return [
>     first,
>     {
>         "role": "user",
>         "content": f"## Prior work summary\n{summary}",
>     },
>     *keep,
> ], summ_tokens
> --- `meta_n/core/agentic_solver.py`

- Immediate return: Replacement message list and summary token count
- Later read-back: Summary reaches subsequent foreground calls within this task; successive compactions can summarize earlier summaries
- Delegated visibility: Summarizer sees removed slice; foreground receives first, summary and tail
- Selection predicate: Parent context estimate above 85%, with at least six messages; provider return enables replacement
- Invalidation or expiry: Raw slice removed from model window; invocation frame ends on task return; no content expiry/check
- Activation or effect: Model-interpreted summary can condition later actions without a faithfulness license
- Evidence limits: Summary instance and semantic fidelity uninspected; preservation cannot be assumed
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-arm-report
Label: Best-of-K statistical report

Saved summaries → finite-value load → run-level and per-task maxima → paired task deltas/sign test → stdout/optional Markdown. Code owns deterministic reduction; operator supplies arms and chooses comparison. Closest supplied [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing) also selects task winners but this route only reports cross-run comparisons and does not assemble executable chains: distinct identity, no route counterpart after comparison. Target: recorded per-task treatment/control score differences on the intersection of task IDs. Evaluator domain: arithmetic and a two-sided sign test under its binomial null, not generated rationale truth. No answer oracle beyond imported numeric results; operating mode is post-run analysis of a bounded experiment.

Concrete deduction from code, not execution: treatment `{a:1,b:0,c:0.9}`, control `{a:0,b:1}` gives shared tasks a,b, deltas +1,-1, wins=1, losses=1, ties=0, mean=0, n=2, k=1, cumulative binomial probability 3/4, two-sided p clipped to 1. Task c is omitted. The report cannot support a full-universe mean for these inputs. Likewise per-task maxima across runs may combine winners no one run achieved.

> tasks = sorted(set(treat) & set(control))
> deltas = {t: treat[t] - control[t] for t in tasks}
> --- `meta_n/analysis/best_of_k.py`

> cum = sum(math.comb(n, i) for i in range(0, k + 1)) / (2 ** n)
> return min(1.0, 2 * cum)
> --- `meta_n/analysis/best_of_k.py`

It prints an advisory criterion requiring positive mean, p<0.05 and matched compute; code does not enforce compute equality or automatically accept/reject a solver. Counts alone do not assure matched effective compute, independent trials or independent task sampling. Repeated selection and a particular intervention design bound causal attribution, which is absent without campaign data. No product/knowledge admission or source rollback occurs: it formats a report for human interpretation.

> "\n> Reject H0 (Ω beats best-of-N) only if mean_delta>0 AND sign-test p<0.05 "
> "AND compute is matched. Otherwise report as a TIE.",
> --- `meta_n/analysis/best_of_k.py`

- Immediate return: Report text; optional file and stdout
- Later read-back: inapplicable — no later automated consumer or search reload implemented in this utility
- Delegated visibility: Operator sees reduced scores/counts and p-value; this is not evaluator ground truth
- Selection predicate: Requested --arm and optional --pair; finite score values and shared task IDs
- Invalidation or expiry: Recompute report after changed input; no result freshness/endorsement check
- Activation or effect: Advisory comparison report, no enforcing deployment or archive consequence
- Evidence limits: No campaign evidence, parity enforcement, causal identification or source-data truth validation
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### EPI-CLM-recursive-improvement
Label: Recursive code-driven improvement

Claimed operation: fixed Ω reads lower execution traces and writes executable intervention code that changes solver behavior; roles emerge from context and the framework self-improves. Source: SRC-1 `README.md`, doctrine/design, with attributed reported prototype properties. Distinct from [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary) and [RT-CLM-budget-bound](runtime.md#rt-clm-budget-bound), which assess guarantees rather than improvement. Closest route [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) is the implementation comparison, not a duplicate claim. Paper/visual examples are not independent run or causal evidence.

> Most "self-improving" agent loops refine *answers*, not the process that produces them. Meta^n instead keeps a single universal meta-operation **Ω** fixed and recurses on its **input**: Ω reads execution traces from the layers below and writes *executable code* (a `pre_process` hook plus a `code_library` of utilities) that is injected into the layer beneath it, changing its behavior.
> --- `README.md`

> Empirical results are exploratory and should not be read as headline wins — see the paper for the full analysis.
> --- `README.md`

#### EPI-CLM-verified-channel
Label: Verify-then-inject channel guarantee

Claimed operation: drop helpers that fail a held-out check so wrong/dead helpers do not reach candidates, and untrusted Ω source never executes on host. SRC-1 `meta_n/core/verified_code.py`, doctrine/design. Closest [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary) addresses prompt sandbox language broadly; this claim targets the verifier module's stronger keep/drop and host invariant wording. Possible overlap on host scope is intentional, not a replacement of the supplied claim. The module itself qualifies ordinary benchmark fallback as unmeasured and stub-kept; dependency closure and native consumers further bound the guarantee.

> gate: after Ω produces a ``code_library`` helper, EXECUTE it in a ``--network none``
> sandbox against a held-out check and KEEP it in the injection ONLY if it passes —
> otherwise DROP it so dead/wrong helpers never reach a candidate.
> --- `meta_n/core/verified_code.py`

> Untrusted Ω code NEVER executes on the host.
> --- `meta_n/core/verified_code.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
