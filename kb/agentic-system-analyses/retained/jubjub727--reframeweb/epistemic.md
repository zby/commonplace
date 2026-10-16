---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ReframeWeb's routes from remembered assertions and tool evidence through completion, guidance admission and saved Store testing, with bounded warrant and consumer scope."
run-id: AAS-2026-10-14-reframeweb-cff918d7eb1e-01
reviewed-boundary: 318987dcde9a016f8e3db819ed9a73abf6b3ad81
---

# ReframeWeb epistemic report

## Source-and-claim boundary

The question is which acquired or generated content can receive reliance, through which checks, and with what consequences. The whole-system functional boundary, frozen source and exclusions are [see boundary](boundary.md#boundary-and-evidence); evidence identity is the boundary's [Source register](boundary.md#source-register). All additional inspection below uses SRC-1 at that revision. Source code establishes implementation; model instructions establish requested behavior. No target execution was performed.

ReframeWeb combines remembered assertions, live tool observations, model-composed task inputs, action summaries, completion tokens, reusable guidance and checkpoint-backed executable configuration. These have different authority paths. A completion token governs continuation after effects; a guidance review governs persistent prompt supply; a candidate test returns startup evidence without enforcing production publication. The source-supported counterexamples to stronger readings are recorded beside those routes.

Consequential warrant declarations are [EPI-CLM-completion-evidence](#epi-clm-completion-evidence), [EPI-CLM-supported-guidance](#epi-clm-supported-guidance), and the supplied [RT-CLM-agent-output](runtime.md#rt-clm-agent-output). They are not claims that all retained material is true.

### Coverage

“Supplied” means a runtime finding rather than an independent source read in this member. “Direct” means source text inspected here; available but uninspected paths are not access gaps.

| Entry point or operation | SRC-1 source path | Coverage and records, or limit |
| --- | --- | --- |
| CLI dispatch, including voice, standalone choice, setup/seeding, workspace, benchmarks and analysis commands | `agent-host/src/reframe_agent_host/cli.py` | Direct dispatch read. Voice loop supplied: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle). Standalone choice, memory-browser edits, seeding, workspace subcommands and benchmark-analysis handlers were not traced here; prevents a system-complete negative concerning other checks or writes. Audio/device checks are not treated as truth acceptance. |
| Task completion and downstream success gate | `agent-host/baml_src/ns_task/completion/flow.baml`; `agent-host/baml_src/ns_voice_turn/agent_routing.baml`; `agent-host/baml_src/ns_voice_turn/task_flow.baml` | Direct prompt and gate reads; selected dispatch/completion/retry section directly read. [EPI-RTE-completion-check](#epi-rte-completion-check), [EPI-RTE-completion-gate](#epi-rte-completion-gate). Request completion and failure resolution supplied by [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle), not independently audited. |
| Graph acquisition, relevance filtering and prompt consumption | `agent-host/baml_src/ns_task/prompting/memory_context.baml`; `agent-host/baml_src/ns_task/prompting/flow.baml`; `agent-host/baml_src/ns_task/prompting/assembly.baml`; `agent-host/baml_src/ns_task/ns_internal/prompt_text.baml` | Direct context builder, composer instructions and assembly; retrieval/SelectedGraph supplied by [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle). [EPI-RTE-prompt-assembly](#epi-rte-prompt-assembly). No database contents or composed prompt trace; semantic preservation and source warrant remain local unknowns. |
| Optional guidance proposals, review, write and later reload | `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`; `agent-host/baml_src/ns_memory/candidate_review_prompt_host.baml`; `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`; `agent-host/baml_src/ns_voice_turn/memory_review_flow.baml` | Direct review inputs, requested criteria, parallel calls and ID filtering. Proposal/persistence/reload supplied by [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review) and [boundary](boundary.md#boundary-and-evidence). [EPI-RTE-guidance-check](#epi-rte-guidance-check), [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition). No candidate instance establishing actual conjecture or acceptance. |
| Normal and Codex execution; action summaries | `agent-host/baml_src/ns_task/action_history/flow.baml`; `agent-host/baml_src/ns_task/action_history/purpose.baml` | Direct normal-summary request; executable routing directly read. Executor details supplied by [RT-RTE-model-task](runtime.md#rt-rte-model-task), [RT-RTE-codex-task](runtime.md#rt-rte-codex-task). Opaque provider/Codex state prevents claims about internal inference, training or reliability. |
| Registered tool catalog and evidence tools | `agent-host/src/reframe_agent_host/task_tools/catalog.py`; `agent-host/src/reframe_agent_host/host_services.py`; `agent-host/src/reframe_agent_host/task_tools/panel_evidence.py`; `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py`; `agent-host/baml_src/ns_task/execution/tool_media.baml` | Direct catalog, service registration section, CDP/PNG processing and model attachment. [EPI-RTE-panel-evidence](#epi-rte-panel-evidence). Project, object, route, Store-call and other panel handlers were identified at registration but not exhaustively inspected; prevents exhaustive evaluator/withdrawal coverage. |
| Explicit Store test, publication, startup and live activation | `agent-host/src/reframe_agent_host/task_tools/store_publication.py`; `agent-host/src/reframe_agent_host/candidate_testing.py`; `agent-host/src/reframe_agent_host/candidate_config.py`; `agent-host/src/reframe_agent_host/startup_stores.py` | Direct tool definitions, candidate test/config and startup gate. [EPI-RTE-candidate-startup](#epi-rte-candidate-startup). Retention/CAS/live recovery supplied by [RT-RTE-saved-store](runtime.md#rt-rte-saved-store); native guest execution and backend enforcement not independently audited. |
| Session-management initial publication | `applications/session-management/publish.py`; `applications/session-management/session_task_publication.py` | Supplied [RT-RTE-application-publish](runtime.md#rt-rte-application-publish). Matching receipts are a stronger gate than generic publication; acceptance program/assertion coverage and receipt authenticity were not inspected here, so actual correctness remains unestablished. |
| Memory-relevance and task-prompt benchmark checks | `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`; `agent-host/src/reframe_agent_host/benchmarks/task_prompt_execution.py`; `agent-host/baml_src/ns_benchmarks/evaluation.baml` | Direct relevance runner, task-prompt evaluator section and deterministic evaluator definitions. [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks). Stored benchmark results, other suites, native acceptance programs and source-native audits not inspected; no performance or causal-benefit finding. |
| Store callbacks, native panel imports, workspace and native subsystems | `agent-host/src/reframe_agent_host/store_host_boundary.py`; `semantic-store/crates/store-runtime/src/panel/host.rs`; `workspace-fs/`; `panel-manager/`; `semantic-store/` | Supplied [RT-BAP-store-callback](runtime.md#rt-bap-store-callback), [RT-BAP-panel-import](runtime.md#rt-bap-panel-import) and boundary coverage. Local authority checks are not truth evaluators. Remaining native implementation and authoring/evaluation paths are available but uninspected here; excludes a system-wide absence of further admission/check routes. |

Missing concrete model outputs prevent identifying which guidance units contain truth-apt generalizations rather than policy recommendations, whether summaries preserve meaning, and whether any produced ampliative claim was accepted. Missing live receipts and later-consumer traces prevent observed activation findings. Missing interventions/comparisons prevent attribution of improved task capacity to memory or review. External weights and version-resolution contracts are excluded, not presumed fixed: see [RT-CMP-model-transport](runtime.md#rt-cmp-model-transport), [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model), and [RT-CMP-whisper-transcriber](runtime.md#rt-cmp-whisper-transcriber).

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-task-input](#epi-obj-task-input) | See record: remembered factual assertions mixed with request/policy content | See record | SRC-1, `agent-host/baml_src/ns_task/prompting/flow.baml` | No concrete composition to classify semantic change |
| [EPI-OBJ-output-summary](#epi-obj-output-summary) | See record: assertions of delivered outcomes and changes | See record | SRC-1, `agent-host/baml_src/ns_task/action_history/purpose.baml` | Summary and executor feedback are not independent corroboration |
| [EPI-OBJ-candidate-entry](#epi-obj-candidate-entry) | See record: possible observations/generalizations; policy advice may be non-truth-apt | See record | SRC-1, `agent-host/baml_src/ns_memory/candidate_review_prompt.baml` | Actual content and its original evidence not supplied |
| [EPI-OBJ-test-result](#epi-obj-test-result) | See record: startup-state and cleanup predicates over one candidate fixture | See record | SRC-1, `agent-host/src/reframe_agent_host/candidate_testing.py` | Result source is inspected; no emitted instance inspected |
| [EPI-OBJ-rendered-evidence](#epi-obj-rendered-evidence) | See record: rendering observation, artifact metadata and CDP result assertions | See record | SRC-1, `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py` | Preview is lossy; source frame, website truth and interactions not thereby verified |

The symbolic PASS/FAIL and kept-ID decisions belong to the separate route records below. Tool-assignment and uncertainty state is [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt), not an assertion corpus. Saved code and task/tool grants can change behavior without a truth-apt content update; see [RT-RTE-saved-store](runtime.md#rt-rte-saved-store) and [RT-RTE-application-publish](runtime.md#rt-rte-application-publish).

## Authority-route ledger

Route ID: [EPI-RTE-prompt-assembly](#epi-rte-prompt-assembly)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-task-input](#epi-obj-task-input)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: See route; deterministic envelope only, not model composition.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_task/ns_internal/prompt_text.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: Composer meaning preservation remains indeterminate; this narrow positive does not classify the whole route.

Route ID: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-task-input](#epi-obj-task-input)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: See route: graph retrieval, ID selection and model composition.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Imported remembered claims have unknown source warrant; relevance establishes intended usefulness, not endorsement. Composer is instructed to preserve provenance, without a demonstrated semantic check.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_task/prompting/flow.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: Imported facts are acquired, not produced knowledge; no sample separates preserved meaning from derivation or non-entailed conjecture.

Route ID: [RT-RTE-model-task](runtime.md#rt-rte-model-task)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-output-summary](#epi-obj-output-summary)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: See object and route: action-history summary generation.
Evaluator/condition and domain: See object: model requested to base assertions on recorded action inputs/outputs.
Activation and timing: See route: after execution and output recording.
Possible or observed result: See object: compact natural-language summary; no instance supplied.
Implemented force: See [EPI-RTE-completion-check](#epi-rte-completion-check).
Epistemic authority and scope: No demonstrated fidelity or entailment; this is a generated candidate description of attempt outcomes.
Operational authority: See [EPI-RTE-completion-gate](#epi-rte-completion-gate).
Behavioral-authority path: See completion records: summary → validator → success/retry branch during current request.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_task/action_history/flow.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: Reinterpretation/non-entailment cannot be inferred merely from model generation. Agent executor feedback instead comes directly from [RT-RTE-codex-task](runtime.md#rt-rte-codex-task), without a second summary model.

Route ID: [EPI-RTE-completion-check](#epi-rte-completion-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-output-summary](#epi-obj-output-summary)
Content/update relation: no content change
Transition or check target: See route.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route.
Operational authority: See [EPI-RTE-completion-gate](#epi-rte-completion-gate).
Behavioral-authority path: See [EPI-RTE-completion-gate](#epi-rte-completion-gate).
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_task/completion/flow.baml`
Claim IDs: [EPI-CLM-completion-evidence](#epi-clm-completion-evidence)
Mismatch marker: none
Gap/limit: Requested local validation, not an independent fact oracle or an observed successful check.

Route ID: [EPI-RTE-completion-gate](#epi-rte-completion-gate)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-output-summary](#epi-obj-output-summary)
Content/update relation: no content change
Transition or check target: See route.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route: operational task success, not acceptance of every reported proposition.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_voice_turn/task_flow.baml`
Claim IDs: [EPI-CLM-completion-evidence](#epi-clm-completion-evidence)
Mismatch marker: none
Gap/limit: Effects and output dispatch precede this decision; failure is not rollback.

Route ID: [EPI-RTE-guidance-check](#epi-rte-guidance-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-entry](#epi-obj-candidate-entry)
Content/update relation: no content change
Transition or check target: See route.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition).
Epistemic authority and scope: See route.
Operational authority: See [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition).
Behavioral-authority path: See [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition).
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_voice_turn/memory_review_flow.baml`
Claim IDs: [EPI-CLM-supported-guidance](#epi-clm-supported-guidance)
Mismatch marker: evidence-input gap
Gap/limit: Reviewer receives candidates and stored guidance, not an independent interaction/tool trace.

Route ID: [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-entry](#epi-obj-candidate-entry)
Content/update relation: no content change
Transition or check target: See route.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route: admission for future guidance, without observed claim-level acceptance.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`
Claim IDs: [EPI-CLM-supported-guidance](#epi-clm-supported-guidance)
Mismatch marker: evidence-input gap
Gap/limit: Model selection and ID intersection cannot independently authenticate an observation.

Route ID: [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-entry](#epi-obj-candidate-entry)
Content/update relation: no content change
Transition or check target: See route: selected title/description writes to five layer-specific collections.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Retention after guidance admission is not independently warranted factual acceptance or lifecycle integration.
Operational authority: See route.
Behavioral-authority path: See route: later decision prompts, advisory natural-language force, across turns while retained.
Evidence source ID and local anchor: SRC-1, `agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py`
Claim IDs: [EPI-CLM-supported-guidance](#epi-clm-supported-guidance)
Mismatch marker: none
Gap/limit: No later behavior trace; expiry/revision maintenance outside this adapter remains unassessed.

Route ID: [EPI-RTE-candidate-startup](#epi-rte-candidate-startup)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-test-result](#epi-obj-test-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: See route: conditional program predicate over measured fixture startup state.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route; warranted conditional on faithful native observations, not source truth or full UI behavior.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/src/reframe_agent_host/candidate_testing.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: Generic publication does not consume this result as a mandatory gate.

Route ID: [EPI-RTE-panel-evidence](#epi-rte-panel-evidence)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-rendered-evidence](#epi-obj-rendered-evidence)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: See route.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route: source warrant unknown; source frame preserved as PNG, preview degraded by resizing/lossy encoding.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_task/execution/tool_media.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: Visibility is not verification of interactions, website assertions or component causality.

Route ID: [EPI-RTE-panel-evidence](#epi-rte-panel-evidence)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-rendered-evidence](#epi-obj-rendered-evidence)
Content/update relation: no content change
Transition or check target: See object and route: full returned PNG retained on workspace filesystem.
Evaluator/condition and domain: See route: size, base64 and PNG-header prerequisites, not interaction validation.
Activation and timing: See route: screenshot tool call before result return.
Possible or observed result: See object: durable artifact path and metadata.
Implemented force: See route: writes artifact; not factual acceptance.
Epistemic authority and scope: Preservation of returned bytes only, with source warrant unknown.
Operational authority: See route: evidence becomes reachable by path/journal.
Behavioral-authority path: See route: workspace artifact and tool receipt, retained for subsequent interpretation.
Evidence source ID and local anchor: SRC-1, `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed artifact or accepted claim; retention is not lifecycle integration.

Route ID: [EPI-RTE-panel-evidence](#epi-rte-panel-evidence)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-rendered-evidence](#epi-obj-rendered-evidence)
Content/update relation: no content change
Transition or check target: See route: image selection for next model invocation.
Evaluator/condition and domain: See route: completed observations, image MIME and newest-eight rule.
Activation and timing: See route: before native BAML model turn.
Possible or observed result: See route: original image or existing resized preview attached.
Implemented force: See route: code-enforced attachment window, advisory evidence at model consumer.
Epistemic authority and scope: Seeing rendering does not warrant successful interaction or website truth.
Operational authority: See route: changes model-visible visual context; compliance unobserved.
Behavioral-authority path: See route: ToolMediaClient → selected provider, next inference; older journal remains reachable.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_task/execution/tool_media.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: Preview generation is lossy reshaping, described in the object; actual model interpretation unknown.

Route ID: [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: See route: kept-memory-ID decision.
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: See route.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: See route: memory-selection reference agreement, including multiplicity.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_benchmarks/evaluation.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: This row covers memory-ID reference agreement; report metrics are not production admission.

Route ID: [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: See route: task ID.
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: See route: task choice, exact identifier domain.
Evaluator/condition and domain: See route: equality to expected_task_id.
Activation and timing: See route: benchmark evaluation.
Possible or observed result: See route: task_correct boolean.
Implemented force: See route: reporting only.
Epistemic authority and scope: Exact reference agreement, not task adequacy beyond authored case.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/baml_src/ns_benchmarks/evaluation.baml`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed benchmark result or oracle authenticity established.

Route ID: [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-task-input](#epi-obj-task-input)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: See route: complete prompt string, envelope-shape domain.
Evaluator/condition and domain: See route: nonempty Task/Input segments under exact parser.
Activation and timing: See route: after benchmark prompt assembly.
Possible or observed result: See route: structural_pass boolean.
Implemented force: See route: reporting only.
Epistemic authority and scope: Syntactic shape only, not preservation of meaning or factual truth.
Operational authority: See route.
Behavioral-authority path: See route.
Evidence source ID and local anchor: SRC-1, `agent-host/src/reframe_agent_host/benchmarks/task_prompt_execution.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: “correct” is structural; snapshot/request content is not consumed by this evaluator.

Route ID: [RT-RTE-saved-store](runtime.md#rt-rte-saved-store)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: See record: saved executable metadata.
Content/update relation: non-truth-apt policy/content update: saved machinery
Transition or check target: See record: reference/CAS admission, separate membership and live revision checks.
Evaluator/condition and domain: See record.
Activation and timing: See record.
Possible or observed result: See record.
Implemented force: See record.
Epistemic authority and scope: Saving code and accepting caller verification text do not establish factual acceptance.
Operational authority: See record.
Behavioral-authority path: See record: startup and explicit live activation, enforcing executable force at next launch or live revision.
Evidence source ID and local anchor: SRC-1, `agent-host/src/reframe_agent_host/task_tools/store_publication.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: Distinct membership/live-apply predicates and recovery remain owned by supplied record; activation and benefit unobserved.

Route ID: [RT-RTE-application-publish](runtime.md#rt-rte-application-publish)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: See record: application metadata, task prompts/grants and instruction links.
Content/update relation: non-truth-apt policy/content update: application machinery, tool grants and instructions
Transition or check target: See record: matching build/acceptance receipt and publication predicates.
Evaluator/condition and domain: See record.
Activation and timing: See record.
Possible or observed result: See record.
Implemented force: See record.
Epistemic authority and scope: Receipt matching bounds admission but does not independently authenticate tests or factual instruction content.
Operational authority: See record.
Behavioral-authority path: See record: next-launch startup plus later task-selection/execution prompt and tool consumers.
Evidence source ID and local anchor: SRC-1, `applications/session-management/publish.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: Acceptance assertions, receipt authenticity and later consumption uninspected; multi-write partial failure differs from generic live recovery.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-completion-evidence](#epi-clm-completion-evidence) | See claim | SRC-1, `agent-host/baml_src/ns_task/completion/flow.baml`, doctrine/design | See claim | [EPI-RTE-completion-check](#epi-rte-completion-check), [EPI-RTE-completion-gate](#epi-rte-completion-gate) | None supplied | No comparison; summary/input fidelity and model compliance unknown | Local failure-seeking validator is requested and its token changes continuation | PASS deliberately tolerates uncertainty and missing external facts; not comprehensive truth endorsement |
| [EPI-CLM-supported-guidance](#epi-clm-supported-guidance) | See claim | SRC-1, `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`, doctrine/design | See claim | [EPI-RTE-guidance-check](#epi-rte-guidance-check), [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition), [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review) | None supplied | No benefit experiment or original evidence supplied to reviewer | Implemented selection for future decision guidance; factual support remains bounded by candidate/stored text | Reviewer has no separate observed-interaction argument; self-described observations can be considered without independent corroboration |
| [RT-CLM-agent-output](runtime.md#rt-clm-agent-output) | See claim | SRC-1, `agent-host/baml_src/ns_task/execution/agent_prompts.baml`, doctrine/design; executable consumer supplied | See claim | [RT-RTE-codex-task](runtime.md#rt-rte-codex-task), [EPI-RTE-completion-gate](#epi-rte-completion-gate) | None supplied | No model-compliance or output-truth evidence | Effects precede completion; returned feedback is data for review | Labels and summaries do not authenticate executed effects or truthful reporting |

## Bounded conclusion

The implemented loop acquires remembered assertions and tool evidence and uses selected content to compose downstream prompts. Relevance is a selection criterion, not a truth check. Deterministic prompt packaging preserves the supplied strings; model composition and action summarization request faithful provenance and payload handling, but no concrete outputs establish semantic preservation or novel inference. Their truth-apt update relation therefore remains indeterminate. Imported content is not a produced claim. No inspected instance establishes a produced accepted ampliative claim; this is an evidence limit, not a whole-system absence.

Completion is an operational adequacy check over the newest summarized outcome, request, requirement and scoped conversation. Its prompt explicitly favors PASS when compact failure evidence is missing. The code's success conjunction additionally rejects known execution/summary failures. A successful gate ends the task attempt and records it for request completion; it does not undo prior effects or validate every proposition in the summary. This criterion is appropriate to bounded operational continuation, but cannot license stronger claims about factual correctness, replay safety, explanation or transfer. See [EPI-RTE-completion-check](#epi-rte-completion-check) and [EPI-RTE-completion-gate](#epi-rte-completion-gate).

Guidance selection requests durable, distinct, interaction-supported lessons for five decision purposes. It can veto all candidates, and code admits only actual selected candidate IDs. The review receives candidate and stored-guidance text, however, not a separately supplied interaction trace. The resulting titles/descriptions persist and are available as advisory context on later turns. This is a prompt-shaping admission and retention path, not evidence of reliable factual acceptance, lifecycle integration or increased capacity. Natural-language policy advice need not be truth-apt. No concrete candidate supports independent theory formulation, content-directed criticism or iteration findings here; opaque model processing is not evidenced absent. See [EPI-RTE-guidance-check](#epi-rte-guidance-check), [EPI-RTE-guidance-disposition](#epi-rte-guidance-disposition) and [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review).

Separate evidence routes have narrower but clearer domains. Program predicates derive fixture startup success and exact reference/shape agreement from their inputs. Candidate cleanup can revoke a passing test result. Screenshots preserve a native-returned full-resolution PNG, while the model may receive a lossy preview among its eight newest images; a rendering observation cannot prove interactions work. These do not collapse into a common oracle. See [EPI-RTE-candidate-startup](#epi-rte-candidate-startup), [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks) and [EPI-RTE-panel-evidence](#epi-rte-panel-evidence).

Production machinery can change through publication, startup membership, explicit live activation and application edits of prompts/tool grants. Generic Store publication records verification text without enforcing the separate candidate-test result; initial application publication has a matching-receipt gate. Such policy/machinery change need not pass through a truth-apt claim. No run or causal comparison closes the links from retained change to later exercised behavior or improved capacity. Learning, reflection, autonomous operation and self-improvement cannot be inferred together from these mechanisms. Available uninspected operations and external providers preserve additional local uncertainty rather than an unqualified system-wide verdict.

## Shared records

### Operative objects

#### EPI-OBJ-task-input
Label: Standalone task input
Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

This object is the prompt-composition part of the broader runtime route (cross-kind containment), not a replacement for its invocation record. Source-native identity: `TaskPromptComposition.task_input` and `TaskPromptDecision.full_task_prompt`. Representational form: natural-language assertions, requests and instructions within a symbolic typed string field. Storage substrate: BAML values delivered to the chosen executor; persistence beyond the turn is not established by these builders. Factual remembered context can be truth-apt; requests and instructions are not themselves factual claims. Producer is a composition model, followed by deterministic envelope construction; consumers are normal task execution and Codex task prompting. Model instruction asks for accurate attribution and provenance, but evidence of compliance is missing. SRC-1, `agent-host/baml_src/ns_task/prompting/flow.baml`; `agent-host/baml_src/ns_task/ns_internal/prompt_text.baml`.

> Reinterpret the supplied context into a coherent, self-contained account
> of the task the downstream runner should handle. The downstream runner has
> no access to the upstream context objects.
> --- `agent-host/baml_src/ns_task/prompting/flow.baml`

> - Make source provenance clear wherever it affects meaning or confidence.
> --- `agent-host/baml_src/ns_task/prompting/flow.baml`

#### EPI-OBJ-output-summary
Label: Newest outcome summary
Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

This is the reviewed output-summary part of the runtime route, not the full execution. Source-native identity: `output_summary`, assembled from `summary.text`, `summary.failure` and `execution.failure`. Representational form: natural-language outcome assertions and error descriptions in a symbolic string. Storage substrate: current BAML values and completion-review entries returned in the result. Normal producer is action-history summarization; agent producer is executor feedback, per [RT-RTE-codex-task](runtime.md#rt-rte-codex-task). Consumer is completion checking. Statements about posted payloads, artifacts and changed state are truth-apt within the attempt, but no sample establishes fidelity. The normal summary request constrains its scope to recorded actions, not the original user request. SRC-1, `agent-host/baml_src/ns_task/action_history/purpose.baml`; `agent-host/baml_src/ns_voice_turn/task_flow.baml`.

> - The listed actions are the complete scope of this summary.
> - Base each statement on their inputs and outputs.
> --- `agent-host/baml_src/ns_task/action_history/purpose.baml`

> let output_summary = summary.text + "\n" + (summary.failure ?? "") + "\n" + (execution.failure ?? "");
> --- `agent-host/baml_src/ns_voice_turn/task_flow.baml`

#### EPI-OBJ-candidate-entry
Label: Proposed decision guidance
Part of: [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)

Cross-kind containment: this is the candidate text carried by the supplied proposal/admission route. Source-native identity: `CandidateMemoryEntry` groups and later selected title/description content. Representational form: natural-language guidance under symbolic IDs/layer membership. Storage substrate: transient staged groups; admitted text later occupies graph guidance collections, as the supplied record establishes. Possible truth-apt parts are claims about observations, decision behavior or reusable lessons; policy recommendations need not be truth-apt. No candidate text was supplied, so acquisition versus entailed derivation versus ampliative conjecture is not determinable for any actual unit. Reviewer and later decision models are different consumers. SRC-1, `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`; persistence passage is supplied by [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review).

> Keep a candidate only when the observation itself describes a reusable
> lesson about the decision behavior named by the stated purpose.
> --- `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`

#### EPI-OBJ-test-result
Label: Candidate startup test result

Distinct from [RT-RTE-saved-store](runtime.md#rt-rte-saved-store): this is the returned/persisted test evidence, not saved Store configuration or its production admission. Source-native identity: result dictionary in `test_candidate`, including `passed`, `startup`, `selection_valid`, artifact identity and optional error/cleanup_error. Representational form: symbolic status and measured fields plus natural-language error text. Storage substrate: return value and fixture-root `result.json`. Its truth-apt assertions concern the one private candidate startup/cleanup, not all Store behavior or production acceptance. Result implementation inspected, no emitted instance or later production consumption observed. SRC-1, `agent-host/src/reframe_agent_host/candidate_testing.py`.

> result.update(passed=True, startup=state['startup'],
>     panel_count=len(candidate.startup.panels.panels), hidden=True,
>     artifact=memory.artifact.model_dump(), selection_valid=True)
> --- `agent-host/src/reframe_agent_host/candidate_testing.py`

#### EPI-OBJ-rendered-evidence
Label: Panel rendering evidence

No counterpart after comparison with the supplied runtime objects: [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt) is authority/replay state, not the tool-returned image/CDP data. Source-native identity: CDP result, PNG artifact and optional JPEG preview. Representational form: image observation and symbolic path/MIME/dimension/byte metadata; error messages are natural language. Storage substrate: native stream results and workspace `verification-evidence` files. Content supports candidate observations of the rendered scene; any stronger proposition needs interpretation and a named test. Full PNG bytes are preserved; oversized images get resized, white-composited JPEG previews for model consumption. Source warrant and deployed browser fidelity unknown. SRC-1, `agent-host/src/reframe_agent_host/task_tools/panel_evidence.py`; `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py`; `agent-host/baml_src/ns_task/execution/tool_media.baml`.

> path.write_bytes(data)
> artifact = {"path": str(path), "mime_type": "image/png", "bytes": len(data),
>             "width": width, "height": height}
> --- `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py`

> preview.save(output, format="JPEG", quality=85)
> --- `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py`

### Routes

#### EPI-RTE-prompt-assembly
Label: Deterministic task envelope
Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

Endpoints/progression: existing selected task prompt and composed task input → `PromptDecision` → `PromptText` → full execution prompt. Owner: BAML deterministic functions; they neither invent assertions nor check source truth. This part is separated from model composition because its semantic transformation is inspectable. Concrete deduction from code: prompt `Read X` and input `X is red.` yield `Task:\nRead X\n\nInput:\nX is red.`. The factual string is unchanged, not a newly established proposition. No target execution is needed for this implementation-layer deduction. SRC-1, `agent-host/baml_src/ns_task/prompting/assembly.baml`; `agent-host/baml_src/ns_task/ns_internal/prompt_text.baml`.

- Immediate return: typed decision with the packaged string.
- Later read-back: inapplicable — this builder alone changes no retained state.
- Delegated visibility: full packaged prompt reaches selected executor; upstream objects do not automatically cross that boundary.
- Selection predicate: caller supplies selected task prompt and composition.task_input.
- Invalidation or expiry: current prompt value replaced on retry/refinement; no independent persistent version here.
- Activation or effect: execution prompt supply; no observed downstream compliance.
- Evidence limits: preservation established only for deterministic envelope; model-generated input meaning remains uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Epistemic authority: none beyond preservation of input strings. Operational path: executor prompt, advisory natural-language force during one attempt. Retry assembly also appends role-labelled previous replies and refusal strings without itself validating their assertions.

> function PromptText(selected_task_prompt: string, task_input: string) -> string {
>     `Task:\n${selected_task_prompt}\n\nInput:\n${task_input}`
> }
> --- `agent-host/baml_src/ns_task/ns_internal/prompt_text.baml`

#### EPI-RTE-completion-check
Label: Candidate-local completion judgment
Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

Endpoints/progression: newest summary plus failure text, task output requirement, active request and scoped conversation → `CallCheckTaskCompletion` → model PASS/FAIL. Owner/evaluator: completion model; check target/domain is material responsiveness of the newest delivered outcome under supplied constraints, not universal factual truth. Human supplies the request; task catalog supplies requirement; model supplies judgment. No independent expected-answer oracle: history's answers are explicitly not an answer key. Open-request operating mode; failure can trigger prompt refinement, not a demonstrated capacity increase. Consumer/force is separated into [EPI-RTE-completion-gate](#epi-rte-completion-gate). SRC-1, `agent-host/baml_src/ns_task/completion/flow.baml`; `agent-host/baml_src/ns_voice_turn/task_flow.baml`.

- Immediate return: PASS or FAIL classification token, recorded with attempt/summary/requirement and timing.
- Later read-back: uninspected — result metadata returns to caller; supplied runtime traces retry context, but durable reuse of this judgment is not established here.
- Delegated visibility: summary and scoped conversation, not a fresh independent execution of all reported effects.
- Selection predicate: every executed attempt reaching this stage invokes the check on its newest output_summary.
- Invalidation or expiry: judgment concerns one attempt; another attempt receives a new check.
- Activation or effect: token is consumed by the separately declared success conjunction; requested scrutiny may fail in model operation.
- Evidence limits: no model output supplied; no independent truth test, complete action verification or measured error rate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Requested epistemic license: compact local failure evidence can support rejection in this supplied-information domain. PASS licenses operational adequacy under an intentionally asymmetric threshold, not correctness of unknown facts. A counterexample to broad truth endorsement is that missing external facts are explicitly not reasons to fail.

> Uncertainty, missing
> external facts, harmless differences in wording, style, method, or
> formatting, and merely possible problems are not reasons to fail.
> --- `agent-host/baml_src/ns_task/completion/flow.baml`

> A false FAIL is worse than letting an uncertain problem pass. If compact
> failure evidence is unavailable, return PASS.
> --- `agent-host/baml_src/ns_task/completion/flow.baml`

#### EPI-RTE-completion-gate
Label: Attempt success disposition
Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

Endpoints/progression: model classification and execution/summary failure fields → `TaskAttemptSucceeded` → successful-task record and break, or failure resolver/retry/reselection. Owner: deterministic BAML control flow. Proposer is executor of the outcome; model judges, code can veto PASS for known failures. Human contribution is original problem/criteria, not per-attempt approval. No answer oracle; open-request mode. Trigger is completion of an attempt; proposed disposition is accept as operationally complete or continue trying. Recovery is continuation, not rollback of executed actions; failure guidance can refine the prompt. See supplied [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle) for full bounded exhaustion and request-completion control. SRC-1, `agent-host/baml_src/ns_voice_turn/agent_routing.baml`; `agent-host/baml_src/ns_voice_turn/task_flow.baml`.

- Immediate return: boolean and selected cycle-result branch; successful task output_summary is added to successful_tasks.
- Later read-back: inapplicable — current invocation's successful_tasks is not a later retained consumer here; durable interaction-state read-back remains supplied runtime scope.
- Delegated visibility: consumes only classification and explicit failure fields, not original effect state.
- Selection predicate: PASS and both failure fields null.
- Invalidation or expiry: one attempt's verdict; bounded retries/cycles have their own terminal behavior.
- Activation or effect: PASS conjunction breaks the attempt loop; false invokes failure resolution. Output dispatch already occurred, so rejection does not retract delivered effects.
- Evidence limits: no executed gate/result; a failure-free summary is not comprehensive evidence that every external action succeeded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Behavioral-authority path: BAML attempt loop and successful-task list, symbolic enforcing branch, remainder of this request. Epistemic license is operational task acceptance against the requested compact-evidence criterion, not acceptance/integration of every contained factual claim.

> completion == root.task.CompletionResult.PASS
>     && execution_failure == null
>     && summary_failure == null
> --- `agent-host/baml_src/ns_voice_turn/agent_routing.baml`

> successful_tasks.push(successful_task);
> --- `agent-host/baml_src/ns_voice_turn/task_flow.baml`

#### EPI-RTE-guidance-check
Label: Guidance-worthiness judgment
Part of: [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)

Endpoints/progression: nonempty layer candidates and stored memories → purpose-specific review input → parallel `CallSelectCandidateMemories` → kept IDs. Owner/evaluator: review model. Target/domain: durable, distinct reusable decision guidance for task choice, search planning, search breadth, relevance or task-input composition. Decision models propose; reviewer can veto all candidates. Human contribution is not per-content approval; no expected-answer oracle or independently supplied evidence of correct guidance. Mode is open requests; objective is future decision usefulness, not a benchmark curriculum. SRC-1, `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`; `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`; `agent-host/baml_src/ns_voice_turn/memory_review_flow.baml`.

- Immediate return: CandidateMemoryReviewDecision with kept_candidate_ids.
- Later read-back: inapplicable — this check returns a selection; persistence and later prompt use are the supplied container's separate functions.
- Delegated visibility: purpose, candidates, stored_memories; no separate conversation/tool-history argument in the actual review call.
- Selection predicate: only nonempty groups create review inputs; purpose is fixed by layer.
- Invalidation or expiry: decision applies to this candidate batch; no source-established factual correction/expiry in this check.
- Activation or effect: selected IDs reach filtering and write-batch construction, not direct writes by the reviewer.
- Evidence limits: observations may be narrated in candidate text, but their independent lineage/support is not verified by this interface. No candidate/model result supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Epistemic license: requested judgment of fit and distinctness; no demonstrated acceptance of a new factual generalization. The strongest falsifier of “no check exists” is this implemented review. The falsifier of “review independently validates observed support” is its bounded input interface.

> let decision = root.memory.CallSelectCandidateMemories(
>     input.purpose,
>     input.candidates,
>     input.stored_memories, client = client);
> --- `agent-host/baml_src/ns_voice_turn/memory_review_flow.baml`

#### EPI-RTE-guidance-disposition
Label: Kept-ID guidance admission
Part of: [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)

Endpoints/progression: staged candidates plus model kept IDs → `KeptCandidateMemories` intersection → layer-specific `CandidateMemoryWriteBatch` → host persistence. Owner: deterministic BAML filter and Python write callback. Proposer/decider/veto: proposer model, review model, code intersection/empty-content validation per supplied container; no intervening human approval. No answer oracle; open-request mode. Trigger is end-of-request candidate review, proposed change is adding reusable layer-specific guidance. Rejection can drop all candidates; no rollback/withdrawal of already stored guidance is established by this adapter. Proposal guidance excludes user facts, preferences, task instructions and results; kept title/description persists. SRC-1, `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`; [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review) supplies persistence and validation evidence.

- Immediate return: layer-specific write batch, then callback acknowledgment when nonempty.
- Later read-back: selected titles/descriptions reach later layer-specific prompt loaders, as the supplied container and boundary establish; actual content influence unobserved.
- Delegated visibility: writer receives kept candidates, not a full independent evidence trace or an explanation of each review verdict.
- Selection predicate: candidate.id must occur in decision.kept_candidate_ids; unknown model IDs cannot introduce new entries.
- Invalidation or expiry: staged candidates end with request; admitted graph records persist, with maintenance/expiry not established by this path.
- Activation or effect: admission permits persistence and subsequent advisory decision-context supply; no reliable compliance or observed improvement follows.
- Evidence limits: intersection checks identity, not truth; no concrete evidence-consuming claim-level acceptance decision supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Behavioral-authority path: write-batch consumer enforces selection now; later decision models receive natural-language guidance through loaders, advisory force across turns while retained. This is separate from lifecycle integration after factual acceptance: neither an evidence connection nor a claim-specific intended-use acceptance record is established here.

> candidates.filter((candidate) -> {
>     decision.kept_candidate_ids.includes(candidate.id)
> })
> --- `agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`

#### EPI-RTE-candidate-startup
Label: Private Store startup test
Part of: [RT-RTE-saved-store](runtime.md#rt-rte-saved-store)

The supplied container identifies an available isolated testing mechanism without characterizing it; this record owns that check, not generic production admission. Endpoints/progression: caller-proposed StoreMemory → private managers/config/graph and projected checkpoints → saved fixture startup membership → startup invocation → observation predicate → cleanup → result.json and tool return. Owner/evaluator: host program plus native environment observations. Target/domain: one checkpoint-backed candidate's startup and valid fixture selection, with configured native grants. Proposer is generic tool caller; code decides pass/failure and cleanup can veto success; human identity not fixed. No external answer oracle: known predicate is readiness plus accepting selection. Mode is explicit isolated candidate testing; objective is startup viability. Test strips instruction_ids in fixture metadata, so it does not assess instruction behavior. SRC-1, `agent-host/src/reframe_agent_host/candidate_testing.py`; `agent-host/src/reframe_agent_host/candidate_config.py`; `agent-host/src/reframe_agent_host/startup_stores.py`; `agent-host/src/reframe_agent_host/task_tools/store_publication.py`.

- Immediate return: result containing passed/error, startup and evidence_directory; optional cleanup_error can force passed=False.
- Later read-back: result.json is retained under private evidence directory; a mandatory later production read of it is not established by generic publish.
- Delegated visibility: caller receives reported startup/selection/artifact fields; private graph receives projected checkpoint memories and candidate configuration, without instruction links.
- Selection predicate: within timeout, startup must return, observations.accepting must be true and every startup state must equal ready; startup itself requires valid session/conversation selection.
- Invalidation or expiry: test is one fixture/configuration; timeout/exceptions or cleanup exception mark failure. No continuing validity across candidate/config changes is enforced here.
- Activation or effect: private managers/startup execute; result is evidence for caller choice, not an enforcing production publication gate.
- Evidence limits: no actual run inspected; panel_count/hidden/selection_valid labels do not prove arbitrary React interaction, website acceptance or production parity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Epistemic scope: conditional predicate follows from inspected state checks, assuming faithful external observations. Operational path: tool return and durable JSON, advisory force for caller's next choice. Production publish separately resolves references and saves metadata, returning caller verification unchanged. Test failure has no automatic production rollback. This counters both “no test exists” and “every publication must pass this test.”

> if not candidate.observations.accepting or any(s['state'] != 'ready' for s in state['startup']):
>     raise ValueError('candidate startup failed: ' + json.dumps(state['startup']))
> --- `agent-host/src/reframe_agent_host/candidate_testing.py`

> try: await candidate.close()
> except Exception as error: result.update(passed=False, cleanup_error=str(error))
> --- `agent-host/src/reframe_agent_host/candidate_testing.py`

> return {'memory_id':node.id, 'saved_for_next_launch':True, 'applied_live':False,
>         'artifact':node.content.artifact.model_dump(), 'reported_verification':args.verification}
> --- `agent-host/src/reframe_agent_host/task_tools/store_publication.py`

#### EPI-RTE-panel-evidence
Label: Native panel evidence acquisition

Distinct from [RT-RTE-model-task](runtime.md#rt-rte-model-task) and [RT-RTE-codex-task](runtime.md#rt-rte-codex-task): this registered evidence acquisition/attachment mechanism can supply those executors, rather than being exactly one supplied route's contained part. Endpoints/progression: authorized CDP session/method → streamed result/artifact → bounded JSON/error processing or PNG persistence/preview → tool receipt/model image attachment. Owner: Python panel adapter, native panel service and BAML ToolMediaClient. Check target/domain: CDP result envelope/size/error and PNG signature/header; this is not a test of all visible page assertions. No truth acceptance decision is attached. SRC-1, `agent-host/src/reframe_agent_host/task_tools/panel_evidence.py`; `agent-host/src/reframe_agent_host/task_tools/screenshot_artifact.py`; `agent-host/baml_src/ns_task/execution/tool_media.baml`; registered in `agent-host/src/reframe_agent_host/host_services.py`.

- Immediate return: CDP result or error; screenshot path/dimensions/bytes plus artifact descriptors.
- Later read-back: full PNG and optional preview are durable workspace artifacts; later tool/model turns can attach referenced images, with older receipt/journal content still reachable.
- Delegated visibility: native BAML model gets at most eight newest tool images, preview preferred when present; original artifact references remain in receipt. Codex transport is supplied runtime scope, not independently inspected here.
- Selection predicate: assigned evidence tool; screenshot requires durable workspace, valid base64/size/PNG header; attachment parses completed tool observations and accepts image MIME types.
- Invalidation or expiry: image depicts capture time, not current page forever; attachment drops oldest images above eight without deleting original receipt/artifact.
- Activation or effect: CDP operation may execute browser effects; screenshot evidence is advisory input for subsequent model choices, not an automated success criterion.
- Evidence limits: native returned frame and command result provenance depends on external backend; header checks are not full PNG semantic validation; no observed capture or interaction result supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Source warrant is unknown; full returned bytes are retained, while model preview is degraded. Behavioral-authority path: completed tool journal → ToolMediaClient → next inference, advisory visual evidence for task duration. Context selection keeps eight newest images; original paths and older journal entries remain, so eviction is from direct visual input rather than proven erasure. CDP stream closes in finally, but that cleanup does not withdraw browser effects.

> finally:
>     await stream.aclose()
> --- `agent-host/src/reframe_agent_host/task_tools/panel_evidence.py`

> let path = artifact.preview_path ?? artifact.path;
> let mime_type = artifact.preview_mime_type ?? artifact.mime_type;
> let image = baml.media.Image.from_file(path, mime_type);
> images.push(image);
> if (images.length() > 8) {
>     images.shift();
> }
> --- `agent-host/baml_src/ns_task/execution/tool_media.baml`

#### EPI-RTE-benchmark-checks
Label: Reference and prompt-shape checks

Distinct from [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle): these CLI benchmark evaluators produce reports outside production request completion. Endpoints/progression: benchmark model decision/prompt → deterministic equality or string-shape predicate → correctness fields in benchmark result. Owner/evaluator: BAML functions, Python result packaging. Separate targets/domains: task ID equality; sorted kept-ID equality including multiplicity; task-prompt envelope shape with nonempty Task/Input. Task/memory cases supply expected IDs through source-authored benchmark builders, not a model answer oracle. Prompt-shape check has no semantic expected answer: its Python evaluator discards snapshot. Mode is bounded benchmark cases, not the open production task mode. No automated successor selection or policy adaptation from these metrics was established in the inspected consumer. SRC-1, `agent-host/baml_src/ns_benchmarks/evaluation.baml`; `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`; `agent-host/src/reframe_agent_host/benchmarks/task_prompt_execution.py`.

- Immediate return: boolean reference agreement or TaskPromptEvaluation fields; Python labels evaluation.correct as structural_pass.
- Later read-back: uninspected — result dictionaries feed benchmark reporting; durable report review/selection policies and stored results not inspected here.
- Delegated visibility: predicate sees decision/expected IDs or prompt string; prompt check does not inspect request/memories for meaning.
- Selection predicate: exact task ID, sorted list equality or exactly two Task/Input string segments with nonempty bodies.
- Invalidation or expiry: result applies to this decision and reference/format specification; changing cases or prompt content requires recheck.
- Activation or effect: records report metrics; no automatic production admission, rejection or model revision found in these inspected evaluators/packagers.
- Evidence limits: no observed benchmark score, case-reference justification or comparison isolating memory/component effect inspected; report success cannot imply factual correctness or causal benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Epistemic license: entailed agreement/shape facts under exact parser rules, not source truth. Concrete deduction: `Task:\nSay the moon is cheese.\n\nInput:\nDo it.` satisfies both nonempty segments and has structural correct=true despite no factual validation. This is an implementation-layer counterexample, not executed target output. Behavioral-authority path: benchmark packaging/report channel, descriptive/advisory metrics for an eventual reader; no implemented admission force at these checked consumers.

> let shape_ok = task_present && input_present && (labels == ["Task", "Input"]);
> --- `agent-host/baml_src/ns_benchmarks/evaluation.baml`

> del snapshot
> evaluation = baml_benchmarks.EvaluateTaskPrompt(decision.full_task_prompt)
> result = evaluation.model_dump(mode="json")
> result["structural_pass"] = evaluation.correct
> --- `agent-host/src/reframe_agent_host/benchmarks/task_prompt_execution.py`

> "correct": baml_benchmarks.MemorySelectionCorrect(decision, expected_ids),
> --- `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`

> decision.selected_task_id == expected_task_id
> --- `agent-host/baml_src/ns_benchmarks/evaluation.baml`

> actual == expected_ids
> --- `agent-host/baml_src/ns_benchmarks/evaluation.baml`

### Claims

#### EPI-CLM-completion-evidence
Label: Compact failure evidence criterion
Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

This is the embedded evaluator doctrine in the supplied request route, not a claim duplicate of [RT-CLM-agent-output](runtime.md#rt-clm-agent-output). Claimed operation: requested completion judgment rejects only a specific material violation checkable from supplied information or a simpler candidate-centered check, never by constructing a full replacement answer. Intended use is binary operational completion for newest task outcome; source is SRC-1, `agent-host/baml_src/ns_task/completion/flow.baml`, doctrine/design. Implementation wires a model call with this prompt; it does not prove compliance or factual reliability.

> Return FAIL only when
> you find compact failure evidence: a specific, material violation in the
> delivered outcome that is checkable directly from supplied information or
> with a candidate-centered check plainly simpler than doing the original
> task.
> --- `agent-host/baml_src/ns_task/completion/flow.baml`

#### EPI-CLM-supported-guidance
Label: Interaction-supported reusable guidance
Part of: [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)

This is the review criterion inside the supplied guidance route, not a new claim that learning succeeds. Claimed operation: favor durable, observed-interaction-supported, distinct guidance useful beyond immediate request; reject memories of user facts/preferences, requests, instructions or results. Source: SRC-1, `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`, doctrine/design. Implemented review sees candidate/stored text and purpose, not an independently provided interaction trace. Unknown compliance and factual support remain distinct from the implemented criterion.

> Favor guidance that is durable, supported by the observed interaction, distinct from stored guidance, and useful beyond the immediate request.
> --- `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`

> Reject candidates that store, paraphrase, consolidate, infer, or promote
> user facts, user preferences, formatting preferences, request content,
> task instructions, task results, or the contents of this layer's inputs.
> --- `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`
