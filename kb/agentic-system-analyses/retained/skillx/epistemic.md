---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SkillX epistemic routes: experience import, model abstraction, admission checks and later instructional reliance."
run-id: AAS-2026-10-14-skillx-61e3fc8f9aa5-01
reviewed-boundary: b0047c848dbbcf019363d6d56eef8c558f69aefc
---

# SkillX epistemic report

## Source-and-claim boundary

The question is whether experience-derived skills acquire warrant for reuse, rather than merely becoming available for reuse. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register). SRC-1 is the sole source. Provider weights, live responses, benchmark evaluator internals and external environment implementations remain outside the frozen source. Their absence prevents verification of model compliance, evaluator validity and deployment behavior. No target execution was performed.

The account assesses import, compression, skill generation, quality/schema evaluation, candidate disposition, library retention, retrieval and formatting, rollout outcomes, and task synthesis. It also inspects an export-validation operation omitted from the supplied runtime. This is added coverage, not a correction of the runtime's valid container records. Distributed-parametric limits are see [RT-CMP-llm](runtime.md#rt-cmp-llm) and [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service): no inspected client weight-update route, no frozen weights, mutable endpoints, and opaque provider internals. This does not rule out learning through retained text or provider-side changes.

Public knowledge-production and warrant claims are see [EPI-CLM-skill-kb](#epi-clm-skill-kb), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement), [EPI-CLM-transfer-gains](#epi-clm-transfer-gains), and the narrower [RT-CLM-quality-control](runtime.md#rt-clm-quality-control). No system-complete negative about acceptance or theory production follows: available uninspected branches and artifacts remain explicitly bounded below.

| Entry point or operation | Source path, SRC-1 | Coverage records | Inspection basis and limit |
|---|---|---|---|
| CLI and construction stages | `pipeline.py`, `data/loaders.py` | [RT-RTE-library-build](runtime.md#rt-rte-library-build) | Supplied runtime; direct CLI dispatch and post-filter/conversion reads. CLI exposes filter bypass and expansion options, not a per-content approver. |
| Long feedback compression | `extraction/tool_summary.py` | [EPI-RTE-feedback-summary](#epi-rte-feedback-summary) | Direct full read; generated summaries and semantic fidelity unobserved. |
| Functional/atomic/plan extraction | `extraction/skill_extractor.py`, `extraction/plan_extractor.py`, `prompts/skill_prompts.py` | [RT-RTE-library-build](runtime.md#rt-rte-library-build) | Supplied runtime plus direct functional extractor body. Atomic helpers and all benchmark-specific adapters not independently read; prevents complete semantic-production classification. |
| General/schema checks and dispositions | `filtering/base.py`, `filtering/pipeline.py`, `prompts/filter_prompts.py` | [EPI-RTE-general-check](#epi-rte-general-check), [EPI-RTE-schema-check](#epi-rte-schema-check), [EPI-RTE-filter-disposition](#epi-rte-filter-disposition) | Direct complete operative bodies and prompts; no evaluator calibration or execution tests supplied. |
| Registered tool contracts and acquisition | `config/tool_schemas.py`, `scripts/extract_appworld_schemas.py`, `scripts/load_bfcl_schemas.py` | [EPI-OBJ-tool-schemas](#epi-obj-tool-schemas), [RT-CLM-quality-control](runtime.md#rt-clm-quality-control) | Direct registry read; acquisition scripts supplied boundary/runtime only. All individual schemas and external tool behavior unassessed; prevents certifying schema fidelity. Registry stores descriptions, not executable tool grants. |
| Clustering, merging, response parsing | `clustering/merger.py`, `clustering/dbscan.py`, `inference/skill_selector.py` | [RT-RTE-library-build](runtime.md#rt-rte-library-build), [RT-RTE-response-eval](runtime.md#rt-rte-response-eval) | Direct full merger; ranking and selector supplied runtime. Model merges not proven meaning-preserving. Local eval can have process effects before any type check. |
| Direct add/merge/save/load and export construction | `core/skill.py`, `data/exporters.py`, `data/schemas.py` | [RT-RTE-library-build](runtime.md#rt-rte-library-build), [EPI-RTE-export-validation](#epi-rte-export-validation) | Direct complete files. Structural validation is not semantic acceptance; exporter preflight has a constructor mismatch. |
| Retrieval, rewriting, selection, step query, benchmark preparation | `inference/skill_usage.py`, `inference/retriever.py`, `inference/plan_rewriter.py`, `inference/prompt_formatters.py`, `inference/benchmarks/` | [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | Supplied runtime; direct formatter read through BFCL and tau2 template. Rewrite/selector mismatch and execution stubs bound delivery; no task-agent compliance evidence. |
| Generic/AppWorld/client rollouts | `expansion/env_worker.py`, `expansion/env_explorer.py` | [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) | Direct generic/AppWorld execute and reward bodies; client route supplied runtime. Evaluator internals external. |
| Simulated/real strategies, post-filters, checkpoints, standalone task generator | `expansion/task_manager.py`, `expansion/task_generator.py`, `expansion/strategies/`, `expansion/explorer.py` | [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis), [EPI-OBJ-synthetic-task](#epi-obj-synthetic-task) | Supplied runtime plus direct duplicate/confidence filters and standalone full-task parser/conversion. Optional strategy parsers uninspected; model predictions are not environment observations. |
| Bundled candidate and reward artifacts | `skillx_db/appworld/vanilla-iter1/func_atomic_skills.json`, `exp_log/` | [EPI-OBJ-skill-content](#epi-obj-skill-content), [EPI-CLM-transfer-gains](#epi-clm-transfer-gains) | First candidate entries directly sampled; reward provenance limit supplied boundary. Other entries/results not aggregated. Candidate availability does not identify production or acceptance routes; prevents causal gain attribution. |
| Documentation, architectural image, auxiliary support | `README.md`, `assets/overview.png`, `utils/`, `llm/` | [EPI-CLM-skill-kb](#epi-clm-skill-kb), [RT-CMP-llm](runtime.md#rt-cmp-llm) | README directly complete; clients supplied runtime. Image and remaining support paths uninspected; no image-specific or complete hook-enumeration conclusion. |

Search of frozen Python entry points and evaluator/validation consumers covered `pipeline.py`, `expansion/`, `inference/`, `data/`, `scripts/`, `config/tool_schemas.py` and `core/skill.py` using `__main__`, `register`, `evaluate`, `filter_result`, `add_plan`, `merge(` and repository-wide `validate(`. It found exporter validation as an additional relevant exposed operation. These searches are source inspection, not proof that every optional hook was assessed.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback) | Tool observations and reward assertions about a task outcome; model summaries of those observations | Experience input and shorter extraction context | see record | Imported reward evaluator provenance unresolved; summary fidelity unchecked. |
| [EPI-OBJ-plan-content](#epi-obj-plan-content) | Prescriptions need not be truth-apt; implied feasibility/order sufficiency is truth-apt only over a specified task/tool domain | Task organization | see record | Actual generated propositions generally unavailable; no per-plan filter in supplied route. |
| [EPI-OBJ-skill-content](#epi-obj-skill-content) | Functionality, input/output and tool-constraint descriptions; code used as instructional reference, not automatically installed functions | Reusable subroutines and tool-use patterns | see record | Sampled candidate does not show criticism, acceptance provenance or transfer success. |
| [EPI-OBJ-tool-schemas](#epi-obj-tool-schemas) | Parameter/return/usage descriptions of tools | Reference for model tool-use judgment | see record | Source-to-tool fidelity and completeness unverified. |
| [EPI-OBJ-synthetic-task](#epi-obj-synthetic-task) | User request itself: none; confidence, predicted action sequence and simulated observations: potential claims about solvability/outcomes | Expansion objectives and proposed experience | see record | Model self-confidence is not calibrated probability; converted tasks have no observed execution reward. |
| [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service) | No independently individuated proposition in vectors | Similarity, grouping and ranking | see record | Similarity grants selection priority, not factual warrant. |
| [RT-CMP-llm](runtime.md#rt-cmp-llm) | Truth-apt content within opaque weights: not determinable | Generation and judgment | see record | Assess exposed outputs separately; no access to weight semantics or provider learning history. |

## Authority-route ledger

Compact records separate checks from disposition and retention from integration. Every repeated canonical field is supplied by the cited record; the ledger adds architectural status, transformation classification and scoped license.

Route ID: [RT-RTE-library-build](runtime.md#rt-rte-library-build)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Corpus trajectories selected by stored reward.
Evaluator/condition and domain: see route; numeric threshold over externally supplied task rewards, not independent reevaluation.
Activation and timing: see route; before abstraction.
Possible or observed result: see route; selected histories.
Implemented force: Enforcing selection predicate, not truth validation.
Epistemic authority and scope: Imported outcome signal with unknown source warrant; reward does not license procedure correctness, mechanism or transfer.
Operational authority: Selected histories may feed extraction.
Behavioral-authority path: Construction code, trajectory dictionaries, enforcing, current build.
Evidence source ID and local anchor: SRC-1, `data/loaders.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb)
Mismatch marker: unknown imported warrant.
Gap/limit: No original evaluator evidence or execution-to-claim entailment check.

Route ID: [EPI-RTE-feedback-summary](#epi-rte-feedback-summary)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Long feedback replaced with extracted summary.
Evaluator/condition and domain: see record; model asked to summarize, regex detects feedback block only.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: Replacement of extraction input; fallback preserves original on missing output/error.
Epistemic authority and scope: No increased warrant; could reshape, omit qualifications or add content. Actual pair and fidelity assessment needed to classify non-ampliative reshaping versus conjecture.
Operational authority: Later extractors receive substituted text.
Behavioral-authority path: Extractors, copied history content, enforcing context replacement, later invocation in build.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb)
Mismatch marker: none.
Gap/limit: Intended preservation is not checked preservation.

Route ID: [RT-RTE-library-build](runtime.md#rt-rte-library-build)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-plan-content](#epi-obj-plan-content), [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Experience to plan/skill proposals and clustered candidates to merged skills.
Evaluator/condition and domain: see route; generative models, parsers and similarity clustering. These are not semantic entailment evaluators.
Activation and timing: see route; pre-admission, with singleton merge passthrough and first-candidate fallback.
Possible or observed result: see route; candidate descriptions, examples and code.
Implemented force: Proposal creation and extraction-context changes, not acceptance of factual claims.
Epistemic authority and scope: Generic capability assertions may go beyond particular trajectories, but no traced input/output pair proves non-entailment. Available content could be imported, reshaped, derived or conjectured; actual provenance and proposition comparison needed.
Operational authority: Proposals can reach filters, conversion and later extraction calls.
Behavioral-authority path: Filter/update code and subsequent extractor models, candidate dictionaries/messages, permissive/advisory, current build and prospective saved reuse.
Evidence source ID and local anchor: SRC-1, `extraction/skill_extractor.py`, `clustering/merger.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement)
Mismatch marker: semantic generalization unverified.
Gap/limit: Novel output and merge labels alone do not establish ampliative conjecture or entailed derivation from warranted premises.

Route ID: [EPI-RTE-general-check](#epi-rte-general-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Candidate content against domain specificity, encapsulation, imports, parameters and code-style criteria.
Evaluator/condition and domain: see record.
Activation and timing: see record; functional candidates in enabled stage.
Possible or observed result: see record; Boolean model-text verdict.
Implemented force: Check result only; disposition is separate below.
Epistemic authority and scope: At most model judgment about supplied text under style/reusability criteria. No executed outcome or independent proof of generalized functionality.
Operational authority: Result is available to Stage 1 selection.
Behavioral-authority path: Filter code, filter_result Boolean, permissive/enforcing only at consumer, current batch.
Evidence source ID and local anchor: see record.
Claim IDs: [RT-CLM-quality-control](runtime.md#rt-clm-quality-control), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement)
Mismatch marker: substring verdict can invert negative wording.
Gap/limit: Concrete deduction: response `not good` yields True, despite negative semantics. No target execution is needed for this source-code deduction.

Route ID: [EPI-RTE-schema-check](#epi-rte-schema-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content), [EPI-OBJ-tool-schemas](#epi-obj-tool-schemas)
Content/update relation: no content change
Transition or check target: Candidate tool invocations against available reference schemas, dependencies and comment alignment.
Evaluator/condition and domain: see record; model, not formal schema execution.
Activation and timing: see record.
Possible or observed result: see record; Boolean verdict or no-documents True.
Implemented force: Check result only; disposition below.
Epistemic authority and scope: Conditional judgment of tool-use compatibility with supplied documentation. Cannot warrant documentation truth, omitted tool coverage, runtime permissions or successful replay.
Operational authority: Verdict can allow Stage 2 survival.
Behavioral-authority path: Stage 2 code, filter_result Boolean, permissive/enforcing at consumer, current batch.
Evidence source ID and local anchor: see record.
Claim IDs: [RT-CLM-quality-control](runtime.md#rt-clm-quality-control), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement)
Mismatch marker: weak verdict parsing and incomplete schema domain.
Gap/limit: Concrete deduction: `<answer>incorrect</answer>` splits to `incorrect</answer>`, contains `correct` and yields True. Absent documents return True without a model check.

Route ID: [EPI-RTE-filter-disposition](#epi-rte-filter-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Stage 1 survivors versus rejected functional candidates.
Evaluator/condition and domain: see record; software consumes general-quality Boolean outcomes. No human per-candidate decision.
Activation and timing: see record; enabled general stage in pre/post-merge filtering.
Possible or observed result: see record; returned candidate subset, including bypass branches.
Implemented force: Enforcing batch inclusion, not universal truth acceptance.
Epistemic authority and scope: An operative decision against requested quality/schema criteria for candidate-library use, bounded to material actually checked. No claim-specific evidence-consuming acceptance of generalized functionality or transfer was established.
Operational authority: Passed candidates may proceed to merge/conversion; rejected ones do not proceed through this call.
Behavioral-authority path: Pipeline, returned lists, enforcing, current build; later saved guidance only if conversion/update succeeds.
Evidence source ID and local anchor: see record.
Claim IDs: [RT-CLM-quality-control](runtime.md#rt-clm-quality-control), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement)
Mismatch marker: atomic bypass; whole-batch no-schema return; optional skips; unchecked post-filter transformation.
Gap/limit: These are operative evaluations and vetoes, not mere logging. Conversely, passing the Boolean gate does not establish accepted ampliative knowledge.

Route ID: [EPI-RTE-filter-disposition](#epi-rte-filter-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Stage 2 schema-bearing candidates surviving versus being rejected.
Evaluator/condition and domain: see record; code consumes schema-check Boolean results after structure/schema preparation.
Activation and timing: see record; enabled tool stage after general selection/atomic bypass.
Possible or observed result: see record; survivors or unchecked current_skills when no candidates qualify for schema checking.
Implemented force: Enforcing batch inclusion on covered candidates, permissive whole-batch fallback.
Epistemic authority and scope: At most operational acceptance against supplied tool specifications for reference-library admission; no universal factual or execution license.
Operational authority: Survivors proceed to conversion or merging; failing checked candidates are excluded.
Behavioral-authority path: Pipeline, returned candidate lists, enforcing/permissive, current build and prospective saved guidance.
Evidence source ID and local anchor: see record.
Claim IDs: [RT-CLM-quality-control](runtime.md#rt-clm-quality-control), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement)
Mismatch marker: Entirely absent schemas bypass this stage; partial schemas narrow its domain.
Gap/limit: Same implemented disposition container as preceding row, different check target and eligibility predicate; no claim-specific acceptance trace.

Route ID: [RT-RTE-library-build](runtime.md#rt-rte-library-build)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-plan-content](#epi-obj-plan-content), [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Object conversion, library insertion/replacement, checkpoint serialization.
Evaluator/condition and domain: see route; name/structure conversion and tool-name redundancy rules, not semantic equivalence.
Activation and timing: see route; plans before filtering, skills after configured stages, checkpoints per epoch.
Possible or observed result: see route; persisted instruction text and metadata.
Implemented force: Durable admission/replacement; redundancy can suppress incoming atomic skills without proving their content is redundant.
Epistemic authority and scope: Retains candidate status; name replacement, timestamps and persistence grant no additional warrant. Serialization preserves encoded fields, not completeness of provenance.
Operational authority: Admitted library may shape later extraction/expansion and be loaded by inference.
Behavioral-authority path: Library readers, objects and JSON files, permissive admission then advisory text, epochs and later sessions.
Evidence source ID and local anchor: SRC-1, `core/skill.py`, `pipeline.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb), [EPI-CLM-quality-refinement](#epi-clm-quality-refinement)
Mismatch marker: retention is not lifecycle integration after epistemic acceptance.
Gap/limit: Deterministic witness: `get_embedding_text` maps name `n`, document `d`, content `c` to `n\nd\nc` without adding a proposition; core JSON encodes the same strings. This limited reshaping conclusion does not extend to model merging or compression.

Route ID: [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-plan-content](#epi-obj-plan-content), [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Relevance selection and delivery of retained guidance; optional rewrite is a separate uncertain content transformation, not a check.
Evaluator/condition and domain: see records; cosine ranking, tool-set constraints and optional model relevance selection.
Activation and timing: see records; caller requests a task or step prompt.
Possible or observed result: see records; formatted prompt/metadata or integration failure.
Implemented force: Ranking/enforcing inclusion; advisory downstream guidance. No truth endorsement by retrieval score.
Epistemic authority and scope: Reference instructions only; AppWorld explicitly requests verification against API documentation before use.
Operational authority: Included skill descriptions/content can guide a task model; BFCL/tau2 omission of plan and wrapper stubs bound actual delivery.
Behavioral-authority path: see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1, `inference/prompt_formatters.py`; see records.
Claim IDs: [EPI-CLM-transfer-gains](#epi-clm-transfer-gains)
Mismatch marker: preparation is not exercised transfer.
Gap/limit: No live task-agent check, compliance, success or causal dependence supplied. Rewrite's required-argument mismatch prevents treating its intended generated plan as delivered on that shipped path.

Route ID: [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Outcome of an executed task in the configured environment, not the generalized skill or its mechanism.
Evaluator/condition and domain: see route; generic text heuristic over assistant content and observation text.
Activation and timing: see route; generic completion per step.
Possible or observed result: see route; histories, completion and reward.
Implemented force: Outcome signal returned; host observations re-enter model messages.
Epistemic authority and scope: Generic heuristic licenses only occurrence of its completion string, not task success, transfer or causal explanation.
Operational authority: Generic completion ends local continuation and returns the heuristic reward.
Behavioral-authority path: Worker/explorer, observation messages and done/reward fields, enforcing stop/advisory feedback, rollout and prospective caller reuse.
Evidence source ID and local anchor: SRC-1, `expansion/env_worker.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb), [RT-CLM-rollout-control](runtime.md#rt-clm-rollout-control)
Mismatch marker: outcome success cannot verify generating procedure.
Gap/limit: Countercase to 'verified reward': generic assistant text `do not call complete_task` still contains the trigger after a non-throwing host call. Imported warrant is unknown beyond the local heuristic.

Route ID: [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: AppWorld task outcome after local execution, not extracted reusable skill correctness.
Evaluator/condition and domain: see route; external world.evaluate tracker, local passes/(passes+failures) calculation when denominator is positive.
Activation and timing: see route; after rollout, reward defaults to zero if evaluator unavailable/fails.
Possible or observed result: see route; reward fraction and history; no observed run of this code supplied.
Implemented force: Returned outcome evidence; stopping separately uses world.task_completed.
Epistemic authority and scope: External evaluator's task-specific outcome license is unknown; the code warrants fraction arithmetic only, not evaluator correctness or skill transfer.
Operational authority: Reward becomes available to caller; no per-skill acceptance or revision forced here.
Behavioral-authority path: Caller/exploration consumers, trajectory reward/history, advisory evidence, current return and prospective later reuse.
Evidence source ID and local anchor: SRC-1, `expansion/env_worker.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb)
Mismatch marker: task outcome versus procedure warrant.
Gap/limit: Countercase to a blanket no-evaluation finding: world.evaluate is called. Its internals and actual producing outcome remain uninspected.

Route ID: [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Client-environment task outcome, not a generalized skill claim.
Evaluator/condition and domain: see route; environment step done/reward and optional env_client.evaluate under external contract.
Activation and timing: see route; during or after client rollout.
Possible or observed result: see route; reward/done and returned per-step history.
Implemented force: Done affects continuation; reward is returned evidence, not library acceptance.
Epistemic authority and scope: Unknown external task-evaluation license; cannot infer producing mechanism, replay safety or transfer.
Operational authority: Host result may stop rollout and make feedback available for summarization.
Behavioral-authority path: Explorer and caller, step observations/reward/done fields, enforcing continuation plus advisory outcome evidence, rollout and prospective reuse.
Evidence source ID and local anchor: SRC-1, `expansion/env_explorer.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb)
Mismatch marker: none.
Gap/limit: Supplied runtime inspection, not independently observed client operation; evaluator internals excluded.

Route ID: [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-feedback](#epi-obj-trajectory-feedback)
Content/update relation: no content change
Transition or check target: Continuation versus local stopping, not epistemic acceptance of a reusable claim.
Evaluator/condition and domain: see route; completion heuristics, host done/task_completed, errors and budgets.
Activation and timing: see route.
Possible or observed result: see route; terminal/partial history.
Implemented force: Enforcing local continuation decision.
Epistemic authority and scope: No additional license beyond outcome-check scope above.
Operational authority: Stop or continue local model/environment interactions.
Behavioral-authority path: Worker loop, done/completion signals, enforcing, current rollout.
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-rollout-control](runtime.md#rt-clm-rollout-control)
Mismatch marker: none.
Gap/limit: Stopping is not certification or rollback of environment effects.

Route ID: [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthetic-task](#epi-obj-synthetic-task)
Content/update relation: non-truth-apt policy/content update: proposed user objectives; predicted action/outcome claims remain indeterminate
Transition or check target: Exploration traces or model-simulated histories to task proposals.
Evaluator/condition and domain: see route; model summarization, no solvability oracle.
Activation and timing: see route.
Possible or observed result: see route; objectives, confidence and action-sequence text.
Implemented force: Candidate generation, not accepted capability.
Epistemic authority and scope: Simulated observations are predictions, not empirical observations; actual truth-apt output/provenance pairs needed to classify entailment versus conjecture.
Operational authority: Proposals can enter manager post-filters and checkpoints.
Behavioral-authority path: Manager/caller, task dictionaries, permissive/advisory, generation rounds.
Evidence source ID and local anchor: SRC-1, `expansion/task_generator.py`; see route and object.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb)
Mismatch marker: synthetic confidence/evaluator label is not external validation.
Gap/limit: Conversion resets history to empty and reward to None; the pipeline does not execute placeholders before the next success comparison.

Route ID: [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthetic-task](#epi-obj-synthetic-task)
Content/update relation: no content change
Transition or check target: Proposed tasks against normalized-query novelty and model-supplied confidence threshold.
Evaluator/condition and domain: see route; code plus optional caller post-filters.
Activation and timing: see route.
Possible or observed result: see route; surviving task list or disappearance on repeated cumulative filtering.
Implemented force: Enforcing candidate-list selection, not truth acceptance.
Epistemic authority and scope: Exact normalized uniqueness and threshold compliance only; no calibrated solvability license.
Operational authority: Survivors may persist as generation checkpoints or become placeholders.
Behavioral-authority path: Manager/caller, returned list/checkpoint, enforcing/permissive, generation and resume.
Evidence source ID and local anchor: SRC-1, `expansion/task_manager.py`; see route.
Claim IDs: [EPI-CLM-skill-kb](#epi-clm-skill-kb)
Mismatch marker: model confidence is not measured success.
Gap/limit: Countercase to deduplication-as-improvement: duplicate state can reject an earlier admitted query on re-filtering without new outcome evidence.

Route ID: [EPI-RTE-export-validation](#epi-rte-export-validation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content), [EPI-OBJ-plan-content](#epi-obj-plan-content)
Content/update relation: no content change
Transition or check target: Non-empty skill fields/tool lists; standalone plan marker validation.
Evaluator/condition and domain: see record; deterministic structure predicates, not truth or type verification.
Activation and timing: see record; direct schema calls are implemented, exporter wrapper fails earlier.
Possible or observed result: see record; Boolean/errors for direct call, constructor TypeError for shipped preflight.
Implemented force: Standalone return only; advertised export-gating consumer is unreachable in that method as written.
Epistemic authority and scope: Structural presence license only. Aggregate validation does not invoke PlanSchema.validate.
Operational authority: No verified checked export on the shipped validate_and_export path; direct export/save bypass this check.
Behavioral-authority path: Direct API caller, Boolean/error tuple, advisory unless caller enforces, current call; no supplied consequential consumer for direct validation.
Evidence source ID and local anchor: see record.
Claim IDs: none.
Mismatch marker: embeddings_config versus embeddings constructor mismatch.
Gap/limit: Source deduction, not an observed exception; no externally patched code assumed.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-skill-kb](#epi-clm-skill-kb) | Automated reusable KB from experience, including rollouts and expansion | see record | see record | [RT-RTE-library-build](runtime.md#rt-rte-library-build), [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout), [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis) | Candidate artifacts available, no linked construction trace | No causal experiment; expansion placeholders/interface wiring do not close execution-to-extraction cycle | Automated abstraction/admission/persistence capacity; separately exposed real-rollout capacity | 'End-to-end' is broader than the shipped convenience loop; reuse reliability unknown |
| [EPI-CLM-quality-refinement](#epi-clm-quality-refinement), [RT-CLM-quality-control](runtime.md#rt-clm-quality-control) | Filtering removes brittle/hallucinated/invalid skills; updates improve quality | see records | Requested quality/schema criteria and add/modify/keep | [EPI-RTE-general-check](#epi-rte-general-check), [EPI-RTE-schema-check](#epi-rte-schema-check), [EPI-RTE-filter-disposition](#epi-rte-filter-disposition), [RT-RTE-library-build](runtime.md#rt-rte-library-build) | No check calibration or revision outcome trace | No component intervention; substring acceptance, skips and unchecked merges limit guarantee | Operative model/software vetoes exist under bounded criteria | Semantic reliability and improvement not established; countercases defeat universal validation |
| [EPI-CLM-transfer-gains](#epi-clm-transfer-gains) | Plug-and-play transfer, around ten-point gains and fewer redundant steps | see record | Prompt injection and reference instructions | [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | README attributed reports; boundary's bundled reward summaries have unknown producing commit | No inspected independent component variation or controlled aggregate comparison | Retained guidance can be loaded and formatted for later tasks on compatible paths | Success, efficiency, transfer scope and representation-specific causal effects unresolved |

## Bounded conclusion

SkillX imports reported experience, generates plans and reusable-looking descriptions/examples, applies operative quality/schema filters on covered candidates, persists survivors, and prepares retained guidance for later model context. None of these stages alone establishes a true generalized skill claim. The imported rewards and tool contracts have unknown source warrant; model compression and merging do not supply fidelity or entailment checks. Deterministic serialization and embedding-text assembly reshape content without warrant amplification. The generated semantic edges remain indeterminate where actual input/output provenance is missing. See [RT-RTE-library-build](runtime.md#rt-rte-library-build), [EPI-RTE-feedback-summary](#epi-rte-feedback-summary) and [EPI-OBJ-tool-schemas](#epi-obj-tool-schemas).

The quality evaluators are consequential, not decorative. Their target is candidate style/reusability or tool-use compatibility with documentation, for admission to a reference library. Their Boolean results change candidate inclusion. Their license does not extend to successful execution, transfer, source truth or causal explanation, and simple negative-wording countercases defeat interpreting their parser as a reliable semantic verdict. Bypass, missing-schema and default pre-merge paths further narrow coverage. No inspected route establishes claim-specific acceptance of a produced ampliative proposition or subsequent lifecycle integration of such an accepted proposition. This is a bounded finding about the assessed routes, not a system-wide claim that no knowledge can be produced. See [EPI-RTE-general-check](#epi-rte-general-check), [EPI-RTE-schema-check](#epi-rte-schema-check) and [EPI-RTE-filter-disposition](#epi-rte-filter-disposition).

Real environment feedback is a separate warrant route. AppWorld/client evaluators may judge task outcomes under external contracts; generic completion strings provide much thinner evidence. Neither outcome check tests the extracted reusable procedure's explanation or transfer. Stopping on completion is operational disposition, not epistemic acceptance of the skill. Model-simulated observations, synthetic confidence and exact query deduplication supply no environment oracle. Placeholder conversion and interface breaks prevent attributing an exercised autonomous improvement cycle to the convenience pipeline. See [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) and [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis).

The behavior-shaping horizon can cross tasks and sessions through saved library files. Retrieval ranks reference text; formatting supplies advisory instructions, not callable installed skills. AppWorld requests subsequent API-documentation verification, but the wrappers do not implement task execution, and integration failures/formatter omissions prevent treating all metadata as delivered guidance. No inspected independent evidence closes downstream compliance or causal benefit. The local model-response eval path has a different, potentially immediate process force and is not epistemic checking despite its name. See [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance), [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) and [RT-RTE-response-eval](runtime.md#rt-rte-response-eval).

Retained experience can change later instruction inputs without changing weights. That supports a trace-fed instruction-update capacity, not demonstrated learning as improved future capacity. Reflection, content-directed theory criticism, theory iteration and exercised self-improvement are not inferred from add/modify/keep, scores or repeated epochs. This report establishes neither their universal absence nor their occurrence in inaccessible model processing. Historical candidate/result availability lacks provenance connecting the relevant checks, revisions and later behavior at this commit. README gains remain attributed reports; the standing prospective update-and-guidance path does not close the later exercised causal-dependence link needed for self-improvement attribution. See [EPI-CLM-transfer-gains](#epi-clm-transfer-gains) and [RT-RTE-library-build](runtime.md#rt-rte-library-build).

## Shared records

### Operative objects

#### EPI-OBJ-trajectory-feedback
Label: Trajectory observations and compressed feedback

Source-native identity: trajectory/task_history entries and reward fields; ToolSummary substitutes user/tool content in a deep copy. Representational form: natural-language observations and summaries interpreted by extraction models; symbolic role/reward fields select processing. Storage substrate: input JSON and in-memory dictionaries. SRC-1, `extraction/tool_summary.py`, `data/loaders.py`. Distinct from supplied runtime components; object inputs/outputs of [RT-RTE-library-build](runtime.md#rt-rte-library-build) and [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout), not duplicate route identities. Outcome evaluator provenance remains unknown. Summary ownership and later consumer are see [EPI-RTE-feedback-summary](#epi-rte-feedback-summary).

> trajectory = result.get("trajectory", result.get("task_history", []))
> --- `extraction/tool_summary.py`

#### EPI-OBJ-plan-content
Label: Planning skill text

Source-native identity: PlanSkill.task, plan and metadata. Representational form: natural-language plan text with symbolic step-marker parsing. Storage substrate: task-keyed in-memory map and library JSON. SRC-1, `core/skill.py`. No supplied operative-object counterpart; produced/retained by [RT-RTE-library-build](runtime.md#rt-rte-library-build), used by [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare). Recommendations are not intrinsically propositions; claims of sufficiency require a named task/tool scope. Retention does not establish their acceptance.

> class PlanSkill:
>     """
>     Planning skill for task-level planning.
>
>     Contains step-by-step plans for completing tasks.
>     """
> --- `core/skill.py`

#### EPI-OBJ-skill-content
Label: Skill descriptions and reference implementations

Source-native identity: Skill.name/document/content/tools/metadata, functional and atomic content kept distinct from embeddings and provider weights. Representational form: natural-language descriptions and examples, code-like text consumed as guidance; symbolic field/name/tool identities control indexing/admission. Storage substrate: library objects/JSON and shipped sample arrays. SRC-1, `core/skill.py`, `skillx_db/appworld/vanilla-iter1/func_atomic_skills.json`. No supplied object counterpart; input/output of [RT-RTE-library-build](runtime.md#rt-rte-library-build), later guidance through [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). First sampled entry describes finding the earliest release date; its availability and filter_result do not identify the producing evaluator or warrant for reuse. Actual source tasks/check traces unavailable for this candidate.

> - name: Skill name
> - document: Functionality description, parameters, outputs, notes
> - content: Implementation code (functional) or usage examples (atomic)
> - tools: List of tools used
> - metadata: Additional info (skill_type, source, cluster_id, etc.)
> --- `core/skill.py`

> "name": "spotify find oldest song by release date",
> --- `skillx_db/appworld/vanilla-iter1/func_atomic_skills.json`

> def get_embedding_text(self) -> str:
>     """Get text representation for embedding."""
>     return f"{self.name}\n{self.document}\n{self.content}"
> --- `core/skill.py`

#### EPI-OBJ-tool-schemas
Label: Registered tool specifications

Source-native identity: ToolSchemaRegistry._schemas indexed by domain/function name, plus custom schemas supplied to ToolSchemaFilter. Representational form: symbolic parameter/required/type structures and natural-language descriptions interpreted by the judging model. Storage substrate: shipped Python schema dictionaries, caller-loaded JSON and in-process registry maps. SRC-1, `config/tool_schemas.py`, `filtering/base.py`. No supplied operative-object counterpart; reference evidence for the quality-control route, not a component implementing those tools. Register accepts records having function keys; imports/custom overrides supply content, not verification of tool correspondence. Acquisition provenance and actual tool contracts remain outside assessed fidelity.

> if "function" in schema:
>     name = schema["function"]["name"]
>     cls._schemas[domain][name] = schema
> --- `config/tool_schemas.py`

#### EPI-OBJ-synthetic-task
Label: Synthetic task objective and action sequence

Source-native identity: task dictionaries with query/confidence/action_sequence and metadata evaluator synthetic. Representational form: natural-language user objective and predicted sequence; symbolic IDs/confidence and metadata guide filtering/conversion. Storage substrate: dictionaries and prospective task checkpoints/placeholder trajectories. SRC-1, `expansion/task_generator.py`, `expansion/task_manager.py`. No supplied operative-object counterpart; object in [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis). Objective request is not truth-apt; claimed confidence/solvability and simulated outcomes require separate assessment. Conversion stores sequence/confidence as metadata, not observed reward.

> "task_history": [],  # Empty - to be filled by agent execution
> "reward": None,  # Not yet executed
> --- `expansion/task_generator.py`

### Routes

#### EPI-RTE-feedback-summary
Label: Long-feedback replacement
Part of: [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Distinct material transformation inside the construction container. Owner: ToolSummary code triggers model invocation using preceding action and feedback; extracted output replaces feedback in a copied history. SRC-1, `extraction/tool_summary.py`, implementation. This part has different context and later consumer from skill generation, with no separate supplied counterpart.

- Immediate return: Summarized string or original feedback; copied trajectory from summarize_trajectory.
- Later read-back: The substituted feedback reaches subsequent extraction invocations within the build; no dereferenceable reload pointer supplied.
- Delegated visibility: Separate model call sees selected preceding action/feedback and summary prompt, not the enclosing conversation.
- Selection predicate: User/tool content longer than max_len, default 1500; non-empty extracted feedback preferred.
- Invalidation or expiry: Copy lives for construction; original caller data remains available; batch error keeps original item.
- Activation or effect: Code changes downstream model-visible history values; no observed semantic fidelity or behavioral effect.
- Evidence limits: Regex output extraction is not an evidence-consuming fidelity evaluation; semantic relation indeterminate without actual pair.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> feedback = self._extract_feedback(response)
> return feedback if feedback else environment_feedback
> --- `extraction/tool_summary.py`

> if "trajectory" in result:
>     result["trajectory"][idx]["content"] = summarized
> else:
>     result["task_history"][idx]["content"] = summarized
> --- `extraction/tool_summary.py`

#### EPI-RTE-general-check
Label: General content quality judgment
Part of: [RT-RTE-library-build](runtime.md#rt-rte-library-build)

A material check part, not duplicate of the runtime's overall admission route. Owner: GeneralFilter issues model call over candidate content and requested quality criteria. SRC-1, `filtering/base.py`, implementation; `prompts/filter_prompts.py`, doctrine/design. Model judges domain specificity, wrappers, imports, parameters and functional style; the program evaluates substring presence. Target is text suitability for reusable library guidance, not task success or truth of all document assertions.

- Immediate return: Boolean from presence of good in lowercased response.
- Later read-back: Verdict consumed by the disposition part in the same batch; no independent retained criticism account established.
- Delegated visibility: Model receives candidate content and quality prompt, not complete trajectory provenance or runtime tests.
- Selection predicate: Called on enabled functional general-stage candidates; exceptions become filter_result False in batch wrapper.
- Invalidation or expiry: Result pertains to the examined content; subsequent merged content can differ without default rechecking.
- Activation or effect: Produces operative Boolean check input; no observed model correctness.
- Evidence limits: Model judgment has no independent answer oracle; substring rule licenses no semantic guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model supplies verdict; code interprets it; caller configuration can skip the check; no per-candidate human evaluator is implemented. Bounded offline batch checking, triggered by proposed skills, not a controlled improvement experiment. Rejection consumer is see [EPI-RTE-filter-disposition](#epi-rte-filter-disposition).

> return "good" in response.lower()
> --- `filtering/base.py`

> 1. **Domain specificity**: Check whether the skill includes domain-specific library names apis, e.g., `apis.spotify.show_playlist_library`.
> 2. **Over-encapsulation**: Check whether the skill's implementation merely calls a single other skill (i.e., it is just a thin wrapper).
> --- `prompts/filter_prompts.py`

#### EPI-RTE-schema-check
Label: Tool-document compatibility judgment
Part of: [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Distinct check part. Owner: ToolSchemaFilter assembles available schema text and candidate content for model evaluation. SRC-1, `filtering/base.py`, implementation; `prompts/filter_prompts.py`, doctrine/design. It targets invocation parameters, ordering/dependencies and comment-function alignment against supplied specifications, not actual execution or transfer.

- Immediate return: Boolean correct-substring test, or True with no documents.
- Later read-back: Disposition code consumes verdict in batch; no later proof or evidence-linked claim acceptance established.
- Delegated visibility: Model sees candidate content and schemas found for listed tools, not missing schemas, actual environment or complete source history.
- Selection predicate: Available schemas selected by tool names; pipeline structure/schema eligibility narrows which candidates reach this call.
- Invalidation or expiry: Result tied to supplied content/docs; no external tool-version tracking; merging can change content afterward.
- Activation or effect: Returns check result consumed by Stage 2; no observed evaluator calibration.
- Evidence limits: Incomplete or false reference documentation and negative wording can defeat intended judgment; no answer oracle beyond model interpretation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model judges; code parses; callers supply/override schemas and can skip checking. No human approval is implemented. Intended use is candidate-library admission, with a veto only through its consumer. This does not certify provider/tool permissions or environment outcomes.

> if not tool_docs:
>     # No schemas available, skip validation
>     return True
> --- `filtering/base.py`

> answer_part = response.split("<answer>")[-1].lower() if "<answer>" in response else response.lower()
> return "correct" in answer_part
> --- `filtering/base.py`

> 2. **Call dependency**: For multiple tool calls, verify that their order does not violate logical dependencies. If there is no dependency between the calls, ignore this check.
> 3. **Comment–function alignment**: Ensure the logic described in any comments matches what the tool is designed to do.
> 4. **Output Format**: Provide your reasoning and conclude with either 'correct' or 'fail', wrapped in <answer></answer>.
> --- `prompts/filter_prompts.py`

#### EPI-RTE-filter-disposition
Label: Filter verdicts to candidate survival
Part of: [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Separate disposition part consuming the two checks, not another check evaluator. Owner: TwoStageFilterPipeline; progression functional Boolean selection plus atomic bypass, structure/schema preparation, then schema Boolean selection or bypass/whole-batch return. SRC-1, `filtering/pipeline.py`, `pipeline.py`, implementation. It changes the candidates entering later merge/conversion. Stages are separately licensed in the ledger because targets and bypasses differ.

- Immediate return: Candidate subset or unvalidated current_skills on the no-valid-schemas branch.
- Later read-back: Pipeline consumes survivors; accepted library objects can later be saved/reloaded, not the same thing as retaining check evidence.
- Delegated visibility: Consumers receive candidate dictionaries/filter_result; no claim-specific evidence package required by conversion.
- Selection predicate: Truthy filter_result for enabled checks; atomic bypass at Stage 1; Stage 2 preparation requires tools and at least one schema when some candidates qualify.
- Invalidation or expiry: Verdicts not automatically invalidated by post-check model merges under default pre_merge; optional post_merge/both can recheck.
- Activation or effect: Enforces candidate exclusion on covered stages; plans/direct add/filter-disabled paths remain separate admissions.
- Evidence limits: Positive check is operational admission, not accepted generalized knowledge; no observed performance consequences or universal validation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model proposes skills and judgments; software can veto through parse/check/conversion/merge; caller chooses mode, not implemented per-content approval. No independent task-answer oracle. Offline bounded admission driven by extracted proposals. Quality prompt shapes checks; passing candidate content/document/tools/metadata can persist. Filter failures reject current proposals rather than withdraw previously saved claims; same-name replacement can revise existing content through the library route. Saved checkpoints permit caller-managed recovery, not automatic rollback.

> passed_functional = [
>     s for s in stage1_results
>     if s.get("filter_result", False)
> ]
> --- `filtering/pipeline.py`

> final_skills = [
>     s for s in stage2_results
>     if s.get("filter_result", False)
> ]
> --- `filtering/pipeline.py`

Whole-batch and other bypass evidence is see [RT-CLM-quality-control](runtime.md#rt-clm-quality-control). Direct inspection confirms that claim; no supersession needed.

#### EPI-RTE-export-validation
Label: Structural validation and blocked export preflight

No supplied route counterpart: this exposed exporter operation was not covered by the runtime's library save path. It overlaps [RT-RTE-library-build](runtime.md#rt-rte-library-build) in accessing the same library but is a separate optional entry point. Owner: schema/exporter code. Endpoints: SkillLibrary to SkillLibrarySchema construction, intended validate call and conditional file export. SRC-1, `data/exporters.py`, `data/schemas.py`, implementation. Constructor supplies embeddings_config where the dataclass declares embeddings, so preflight raises before its intended evaluator and consumer. Standalone schema methods remain inspectable implemented checks; no source execution performed.

- Immediate return: Direct validation returns Boolean/errors; shipped validate_and_export fails at schema construction before its intended tuple/export.
- Later read-back: inapplicable — this preflight as written cannot create a validated export; standalone checks retain no content.
- Delegated visibility: inapplicable — deterministic code, no model or human delegation.
- Selection predicate: Direct schema checks require non-empty fields/tools; PlanSchema checks step marker, but library aggregate loops only functional and atomic lists.
- Invalidation or expiry: inapplicable — current-call structure checks, no retained result or freshness protocol.
- Activation or effect: Direct checks return results; advertised export gating is blocked by constructor mismatch. Other export/save functions write without this validation.
- Evidence limits: Non-empty strings/tool lists do not prove correctness; direct caller enforcement uninspected; TypeError deduction uses frozen implementation, not observed execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Code is evaluator/decider for structural suitability; no human or model approval or answer oracle. Open direct API invocation, not improvement selection. Intended gate would prevent export on errors, but no successful gate activation established. No content change or rollback implemented in this preflight.

> functional=[s.to_dict() for s in library.functional],
> atomic=[s.to_dict() for s in library.atomic],
> embeddings_config=library.embeddings_config,
> --- `data/exporters.py`

> atomic: List[Dict] = field(default_factory=list)
> embeddings: Dict[str, Any] = field(default_factory=dict)
> --- `data/schemas.py`

> if not self.content:
>     errors.append("content is required")
>
> if not self.tools or len(self.tools) == 0:
>     errors.append("at least one tool is required")
> --- `data/schemas.py`

### Claims

#### EPI-CLM-skill-kb
Label: Automated reusable skill knowledge base

Claimed operation: experience distilled to reusable hierarchical knowledge, with an end-to-end automated rollout/extraction/refinement/expansion pipeline. SRC-1, `README.md`, doctrine/design. Broader than [RT-CLM-quality-control](runtime.md#rt-clm-quality-control) and [RT-CLM-rollout-control](runtime.md#rt-clm-rollout-control); no duplicate supplied claim. It establishes declared scope, not reliable reuse or exercised end-to-end construction.

> **SkillX** is a fully automated framework that constructs a **reusable, plug-and-play skill knowledge base** for LLM agents from experience.
> --- `README.md`

> SkillX provides an end-to-end automated pipeline that:
> - rolls out agents on training tasks,
> - extracts reusable skills from successful trajectories,
> - consolidates and filters low-quality skills,
> - and builds a reusable **plug-and-play skill knowledge base**.
> --- `README.md`

#### EPI-CLM-quality-refinement
Label: Quality improvement through refinement

Claimed operation: merging/filtering/iterative updates continuously improve library quality and remove brittle or hallucinated skills. SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-quality-control](runtime.md#rt-clm-quality-control): that record owns filter coverage/strength; this record owns the public improvement and hallucination-removal claim. Operative checks exist, but no supplied calibration or observed improvement establishes this stronger warrant.

> SkillX continuously improves the skill library through:
> - **skill merging** for consolidating redundant behaviors,
> - **quality filtering** for removing brittle or hallucinated skills,
> - and **iterative updates** that add, modify, or keep skills based on execution feedback.
> --- `README.md`

#### EPI-CLM-transfer-gains
Label: Transfer and performance gains

Claimed operation: strong-to-weak transfer without retraining, success/efficiency/generalization gains and approximately ten-point improvements. SRC-1, `README.md`, doctrine/design and reported operation. No supplied counterpart; [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) is the implementation authority path, not the empirical gain claim. Boundary's bundled result provenance limits remain: unknown producing commit, no controlled comparison or component attribution inspected here.

> The resulting skill library can be directly injected into different base agents, enabling **strong-to-weak transfer** without retraining the underlying model.
> --- `README.md`

> - **~10% absolute improvement** for weaker base agents on multiple benchmarks
> - Consistent gains on **AppWorld**, **BFCL-v3**, and **τ2-Bench**
> --- `README.md`
