---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OS-Copilot's routes from generated answers, execution feedback and acquired web content to completion, retention and later reliance."
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
reviewed-boundary: "f720af8807e49a92dda64572d2c6bc6c0ac7ee7e"
---

# OS-Copilot epistemic report

## Source-and-claim boundary

The question is which content OS-Copilot checks before letting it control task progression or later tasks. The functional inclusions, exclusions and frozen evidence identity are those of [boundary](boundary.md#boundary-and-evidence); the sole source is SRC-1 in its [Source register](boundary.md#source-register). This report adds direct implementation inspection of web acquisition, cleaning, summary and query-selection services, service routing, maintenance dispatch and benchmark consumption. It uses supplied runtime findings for the UI, provider adapters, interpreter internals and alternative example loops. These are not target executions.

The system's self-improvement claim is see [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement). Its more specific Excel improvement claim is see [EPI-CLM-excel-learning](#epi-clm-excel-learning). The judge's intended verification and generality assessment is see [EPI-CLM-code-judgment](#epi-clm-code-judgment).

| Entry point or operation | SRC-1 path | Coverage and record | Remaining limit and conclusion prevented |
| --- | --- | --- | --- |
| Task and UI launch | `quick_start.py`; `fronted/src/interface/api.js` | Supplied [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) | No live grants or UI run; no outcome claim |
| Exported FRIDAY, generation, judgment, repair | `oscopilot/agents/friday_agent.py`; `oscopilot/modules/executor/friday_executor.py`; `oscopilot/prompts/friday_pt.py` | Direct reads of consequential branches; [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair) | No candidate trace or validated model compliance |
| API and QA type bypass | `oscopilot/agents/friday_agent.py`; `oscopilot/modules/executor/friday_executor.py` | Direct; [RT-RTE-api-qa](runtime.md#rt-rte-api-qa) | Actual generated propositions and API responses unknown |
| Automatic storage, reload, retrieval, manual add/delete CLI | `oscopilot/tool_repository/manager/tool_manager.py`; `oscopilot/modules/executor/friday_executor.py` | Direct; [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), [RT-BAP-tool-context](runtime.md#rt-bap-tool-context) | No retained instance with route provenance; no demonstrated reuse benefit |
| Course design, demo extraction, saving | `course_learning.py`; `oscopilot/agents/self_learning.py`; `oscopilot/modules/learner/self_learner.py`; `oscopilot/tool_repository/basic_tools/text_extractor.py` | Supplied [RT-RTE-course-learning](runtime.md#rt-rte-course-learning); direct course-prompt search | Extraction fidelity and actual lesson success unobserved |
| Mounted search, page load, image search | `oscopilot/tool_repository/manager/api_server.py`; `oscopilot/tool_repository/api_tools/bing/bing_service.py`; `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`; `oscopilot/tool_repository/api_tools/bing/web_loader.py`; `oscopilot/tool_repository/api_tools/bing/image_search_api.py` | Direct; [EPI-RTE-page-content](#epi-rte-page-content) | Live search/source truth and dependency internals unassessed |
| Mounted transcription and caption | `oscopilot/tool_repository/api_tools/audio2text/audio2text_service.py`; `oscopilot/tool_repository/api_tools/image_caption/image_caption_service.py` | Direct wrappers; supplied [RT-CMP-audio2text](runtime.md#rt-cmp-audio2text), [RT-CMP-image-caption](runtime.md#rt-cmp-image-caption), [RT-RTE-api-qa](runtime.md#rt-rte-api-qa) | Recognition and answer accuracy unobserved; no independent check in read wrappers |
| Wolfram router | `oscopilot/tool_repository/api_tools/wolfram_alpha/wolfram_alpha.py`; `oscopilot/tool_repository/manager/api_server.py` | Direct: router defined/imported, excluded from server_list; [RT-RTE-api-qa](runtime.md#rt-rte-api-qa) | No ordinary mounted Wolfram computation; external mathematical warrant uninspected |
| Simplified/vision alternatives | `examples/light_friday/light_friday.py`; `examples/friday_vision/friday_vision.py` | Supplied [RT-RTE-example-loops](runtime.md#rt-rte-example-loops) | No observed screenshot interpretation or task success |
| GAIA benchmark and SheetCopilot driver | `examples/GAIA/run_GAIA.py`; `examples/SheetCopilot/run_sheet_task.py` | Direct; [EPI-RTE-gaia-comparison](#epi-rte-gaia-comparison) | No benchmark dataset/results inspected; SheetCopilot driver invokes tasks without workbook comparison |
| Other definitions, tests, schemas, adapter details | See boundary coverage | Not exhaustively inspected; tests not executed | Prevents a repository-complete negative about every possible check or derivation |

No supplied execution traces or causal experiments establish activation, improvement or transfer. Distributed-parametric provider internals and exact deployed weights are unavailable; that prevents claims about their internal acquisition or learning. Accessible but uninspected code is an inspection limit, not an access gap. There is no system-complete negative here about all possible truth production: arbitrary generated programs could calculate, measure or test claims, but no such concrete program/result was supplied.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph) | Task descriptions and result strings can carry claims; dependency/status symbols are coordination, not evidence of truth | see record | SRC-1, `oscopilot/agents/friday_agent.py` | A complete flag does not certify its result |
| [EPI-OBJ-candidate-code](#epi-obj-candidate-code) | Programs are action policies; docstrings may claim behavior | see record | SRC-1, `oscopilot/modules/executor/friday_executor.py` | No concrete candidate individuates explanatory content |
| [EPI-OBJ-judgment-result](#epi-obj-judgment-result) | Code accomplished task; code generalizes to other uses | see record | SRC-1, `oscopilot/prompts/friday_pt.py` | Criterion mixes execution completion and untested generality |
| [EPI-OBJ-tool-description](#epi-obj-tool-description) | First docstring sentence describing a retained tool's behavior | see record | SRC-1, `oscopilot/tool_repository/manager/tool_manager.py` | Description is candidate-authored, not independent verification |
| [EPI-OBJ-course-text](#epi-obj-course-text) | Lesson imperatives have no truth value; Prior Course framing implies completed lessons | see record | SRC-1, `oscopilot/prompts/friday_pt.py` | Saved course is not mastery evidence |
| [EPI-OBJ-qa-answer](#epi-obj-qa-answer) | Answers can assert facts or infer them from prior results | see record | SRC-1, `oscopilot/modules/executor/friday_executor.py` | Actual proposition and entailment not determinable |
| [EPI-OBJ-page-content](#epi-obj-page-content) | Web assertions, extracted text, selected excerpts and model summaries | see record | SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py` | Cleaning may alter truth conditions; response omits loader metadata |
| [RT-CMP-image-caption](runtime.md#rt-cmp-image-caption), [RT-CMP-audio2text](runtime.md#rt-cmp-audio2text), [RT-CMP-ocr-service](runtime.md#rt-cmp-ocr-service) | Caption assertions, transcribed speech and recognized coordinates/text | see records | SRC-1, service wrappers listed above; `examples/friday_vision/friday_vision.py` | Separate image, audio and OCR targets; no recognition-quality evidence |
| [RT-OBJ-friday-prompts](runtime.md#rt-obj-friday-prompts) | Mostly instructions; embedded descriptions/rubrics can make methodological claims | see record | SRC-1, `oscopilot/prompts/friday_pt.py` | Static method content is not evidence-responsive method revision |

## Authority-route ledger

All ledger statuses concern architecture, not observed operation. Fields owned by cited records are referenced rather than redeclared. A route ID can recur because checking, disposition and retention are distinct functions of one implementation.

Route ID: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-code](#epi-obj-candidate-code), [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph).
Content/update relation: non-truth-apt policy/content update: model proposes plan and executable actions; proposition content of arbitrary generated programs is not determinable.
Transition or check target: task and selected tools to plan/program.
Evaluator/condition and domain: no truth evaluator at generation; fixed parser and graph traversal select executable output.
Activation and timing: see route; before host execution.
Possible or observed result: candidate action program; only wiring established.
Implemented force: executable dispatch, not merely advice.
Epistemic authority and scope: generation alone licenses no claim of task correctness.
Operational authority: behavior permitted, blocked, or changed: program reaches host interpreter before semantic evaluation.
Behavioral-authority path: consumer, channel, force, horizon: see route and [RT-BAP-method-instructions](runtime.md#rt-bap-method-instructions); executor/Env, extracted code, permissive, current task and resulting host effects.
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`; see cited route passages.
Claim IDs or none: [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement).
Mismatch marker or none: none; execution is not acceptance.
Gap/limit: no concrete generated computation establishes entailed derivation.

Route ID: [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judgment-result](#epi-obj-judgment-result).
Content/update relation: truth-apt transformation: indeterminate; model judgment can repeat observations, infer completion or make unsupported claims; actual input/output needed to distinguish reshaping, derivation and conjecture.
Transition or check target: executed Python/Shell/AppleScript candidate, task completion and generality.
Evaluator/condition and domain: model compares source, task, error, directory listing, successor requirements and at most 999 characters of long output; requested domain includes current-task fit and code generality.
Activation and timing: see route; after effects, repeated after repairs without execution error.
Possible or observed result: reasoning/status/score; no observed verdict supplied.
Implemented force: check result itself is an input to separate disposition below.
Epistemic authority and scope: evidence-consuming but best-effort judgment of visible task evidence; no calibrated transfer license, process explanation or replay-safety conclusion.
Operational authority: behavior permitted, blocked, or changed: via the separate status consumer below.
Behavioral-authority path: consumer, channel, force, horizon: see route; judgment JSON to agent branches, current subtask and potential later retention.
Evidence source ID and local anchor: SRC-1, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/prompts/friday_pt.py`; [EPI-CLM-code-judgment](#epi-clm-code-judgment).
Claim IDs or none: [EPI-CLM-code-judgment](#epi-clm-code-judgment).
Mismatch marker or none: generality score exceeds the demonstrated domain of one execution.
Gap/limit: code can print completion; rubric permits that as sufficient evidence. Output truncation can omit counterevidence. Prompt compliance is unobserved.

Route ID: [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judgment-result](#epi-obj-judgment-result), [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph).
Content/update relation: no content change.
Transition or check target: whether to complete current node, repair it or insert prerequisites.
Evaluator/condition and domain: software branches on model status; initial non-Amend/non-Replan values permissively complete; repaired path explicitly requires Complete. See route for ownership, oracle and mode.
Activation and timing: after judgment, not before host action.
Possible or observed result: complete flag and result propagation, amendment, replan, or stop at repair exhaustion.
Implemented force: enforcing local branch; no transactional rollback.
Epistemic authority and scope: a Complete verdict is intended task acceptance against visible task requirements, not reliable certification; permissive fallback is operational acceptance without an explicit affirmative criterion.
Operational authority: behavior permitted, blocked, or changed: next graph nodes may consume result; repair executes revised code; replan changes pending work.
Behavioral-authority path: consumer, channel, force, horizon: see route; graph and model prompt assembly consume status/result/critique within run.
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/friday_agent.py`; see runtime passages and candidate-object evidence.
Claim IDs or none: [EPI-CLM-code-judgment](#epi-clm-code-judgment).
Mismatch marker or none: complete does not universally mean a checked positive verdict.
Gap/limit: not acceptance of every fact in output; no independently inspected world-state oracle.

Route ID: [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-code](#epi-obj-candidate-code).
Content/update relation: non-truth-apt policy/content update: amendment replaces executable code and replanning changes task policy.
Transition or check target: criticized action candidate and queued plan.
Evaluator/condition and domain: model proposes amendment/replan; software bounds repair and executes the candidate; computational versus human roles and trigger are see route.
Activation and timing: after criticism, within task.
Possible or observed result: changed code/graph, re-execution; operation unobserved.
Implemented force: direct control of future actions, without necessary formulation of a theory.
Epistemic authority and scope: no independent claim that the revision explains failure or improves future capacity.
Operational authority: behavior permitted, blocked, or changed: next repair program runs; new prerequisites can be inserted.
Behavioral-authority path: consumer, channel, force, horizon: see route; interpreter code and planner graph, permissive/enforcing, current task plus host effects.
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/friday_agent.py`; runtime repair passages.
Claim IDs or none: [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement).
Mismatch marker or none: none.
Gap/limit: program revision is not by itself formulated explanatory-theory revision.

Route ID: [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-code](#epi-obj-candidate-code).
Content/update relation: no content change.
Transition or check target: Python candidate eligibility for reuse.
Evaluator/condition and domain: see route; Python, completion, score threshold, then new-name gate. Model evaluates generality; software admits; no per-content human approval or answer oracle.
Activation and timing: after completion decision, before manager write.
Possible or observed result: eligible or skipped; wiring only.
Implemented force: enforcing this automatic call-site gate, not all repository writers.
Epistemic authority and scope: intended reuse criterion is generality score plus current-task completion; neither establishes cross-task reliability. Repaired score can authorize original code.
Operational authority: behavior permitted, blocked, or changed: permission to store candidate for later context selection.
Behavioral-authority path: consumer, channel, force, horizon: see route and [RT-BAP-tool-context](runtime.md#rt-bap-tool-context).
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/friday_agent.py`; runtime's admission passages.
Claim IDs or none: [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement).
Mismatch marker or none: tested/admitted candidate identity can diverge.
Gap/limit: execution success of repaired code does not license original code; no acceptance of an ampliative explanatory claim is established.

Route ID: [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-code](#epi-obj-candidate-code), [EPI-OBJ-tool-description](#epi-obj-tool-description).
Content/update relation: no content change.
Transition or check target: provided code and extracted description to files/JSON/vector index.
Evaluator/condition and domain: manager count assertion checks index/metadata cardinality, not code, provenance or truth. Admission predicates differ; see respective records.
Activation and timing: after automatic gate or direct caller write.
Possible or observed result: persistent tool entry; overwrite possible via manager; no exercised write supplied.
Implemented force: durable eligibility for later use, not evidence integration.
Epistemic authority and scope: stored description is a behavior claim supplied by candidate docstring, not verified documentation.
Operational authority: behavior permitted, blocked, or changed: selected retained material may shape later planning/generation.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-tool-context](runtime.md#rt-bap-tool-context).
Evidence source ID and local anchor: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`, `oscopilot/modules/executor/friday_executor.py`; description record and runtime passages.
Claim IDs or none: [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement).
Mismatch marker or none: retention is not lifecycle integration of accepted knowledge.
Gap/limit: no stored judgment/evidence connection in the manager's code/description entry; no automatic validation-driven withdrawal.

Route ID: [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidate-code](#epi-obj-candidate-code), [EPI-OBJ-tool-description](#epi-obj-tool-description).
Content/update relation: no content change.
Transition or check target: exact-name overwrite or deletion, not an epistemic reevaluation.
Evaluator/condition and domain: caller chooses; CLI tests add first then delete; manager removes selected persistent surfaces. See route for rejection/recovery.
Activation and timing: explicit maintenance command/API call.
Possible or observed result: replacement or removal; delete leaves current generated_tools dictionary unchanged.
Implemented force: persistent withdrawal from future index selection, not universal in-process revocation.
Epistemic authority and scope: no truth/quality decision is inherent in deletion or replacement.
Operational authority: behavior permitted, blocked, or changed: future selection changes; direct dictionary getters can still see stale entries in existing manager.
Behavioral-authority path: consumer, channel, force, horizon: see route; index and metadata reload determine later context eligibility.
Evidence source ID and local anchor: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`; runtime maintenance record.
Claim IDs or none: none.
Mismatch marker or none: disk deletion does not revoke all live copies or undo host effects.
Gap/limit: no versioned transactional rollback established.

Route ID: [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [RT-BAP-tool-context](runtime.md#rt-bap-tool-context)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-tool-description](#epi-obj-tool-description), [EPI-OBJ-candidate-code](#epi-obj-candidate-code).
Content/update relation: truth-apt transformation: non-ampliative reshaping; descriptions are indexed/ranked; retained code remains text for generation.
Transition or check target: task/subtask query to selected tool context.
Evaluator/condition and domain: embedding similarity ranks relevance, not truth or actual applicability; selected names retrieve descriptions/code. See records for top-k and delivery.
Activation and timing: planning and Python generation in later invocations.
Possible or observed result: selected context; behavioral dependence unobserved.
Implemented force: ranking then advisory model context, not direct stored-function execution.
Epistemic authority and scope: no new endorsement from retrieval score.
Operational authority: behavior permitted, blocked, or changed: examples/descriptions enter generation and can shape fresh executable code.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-tool-context](runtime.md#rt-bap-tool-context).
Evidence source ID and local anchor: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`; runtime context passages.
Claim IDs or none: [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement).
Mismatch marker or none: relevance is not warrant.
Gap/limit: no observed effect or retrieval-quality comparison.

Route ID: [RT-RTE-api-qa](runtime.md#rt-rte-api-qa)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-answer](#epi-obj-qa-answer); caption/transcription outputs see component records.
Content/update relation: truth-apt transformation: indeterminate; QA/caption may summarize, infer or conjecture; transcription attempts acquisition/import of spoken content with fidelity unknown. No concrete response establishes non-entailment or warranted derivation.
Transition or check target: question/prerequisites, image or audio to answer text.
Evaluator/condition and domain: model inference; service wrappers validate input availability or catch RuntimeError, not factual adequacy. QA guidance permits own knowledge and inference.
Activation and timing: selected QA/API node or independently called mounted service.
Possible or observed result: answer, caption, transcript, error; none observed.
Implemented force: text returned/printed and eligible prerequisite input.
Epistemic authority and scope: acquisition source warrant unknown; no independent fact acceptance demonstrated.
Operational authority: behavior permitted, blocked, or changed: QA/API nodes skip code judge and complete through the alternative branch; generated API Python can execute host effects.
Behavioral-authority path: consumer, channel, force, horizon: see route; graph result to downstream prompts, current run; direct service response to requesting client.
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`; service paths in coverage table.
Claim IDs or none: none.
Mismatch marker or none: node completion is not epistemic acceptance.
Gap/limit: external recognition and provider compatibility remain unobserved.

Route ID: [RT-RTE-course-learning](runtime.md#rt-rte-course-learning), [RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-course-text](#epi-obj-course-text).
Content/update relation: non-truth-apt policy/content update: parsed curriculum is retained as lesson descriptions, then treated as prior course.
Transition or check target: model-designed course to in-memory dictionary and merged JSON.
Evaluator/condition and domain: model proposes curriculum; parser/driver admit and save; lesson calls do not provide an independent pass/fail gate. See route for human role and mode.
Activation and timing: continuous mode updates course before lesson execution and saves after lesson calls.
Possible or observed result: durable lesson text; no observed mastery.
Implemented force: retention before evidence-consuming acceptance of learning success.
Epistemic authority and scope: no license for proposition that retained lessons were mastered.
Operational authority: behavior permitted, blocked, or changed: next design treats recent prior course as basis for progression.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks).
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/self_learning.py`, `oscopilot/prompts/friday_pt.py`; supplied course route passages.
Claim IDs or none: [EPI-CLM-excel-learning](#epi-clm-excel-learning).
Mismatch marker or none: completed-course framing is stronger than driver evidence.
Gap/limit: normal return after caught task failure can still lead to saving; no lifecycle integration of accepted mastery claim shown.

Route ID: [RT-RTE-course-learning](runtime.md#rt-rte-course-learning), [RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-course-text](#epi-obj-course-text).
Content/update relation: non-truth-apt policy/content update: prior lessons guide new lesson/task selection.
Transition or check target: prior course/demo context to next lesson set and task invocations.
Evaluator/condition and domain: course-design model requested to avoid duplicates and advance difficulty; ordinary agent executes each lesson. See route for selection and ownership.
Activation and timing: subsequent curriculum rounds; lesson execution synchronous.
Possible or observed result: new practice tasks; no observed capacity increase.
Implemented force: operative task input, with prior context advisory at course design.
Epistemic authority and scope: no truth-apt route is necessary for curriculum policy adaptation; course history is not correctness evidence.
Operational authority: behavior permitted, blocked, or changed: tasks select which host operations/tool-generation attempts occur next.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks).
Evidence source ID and local anchor: SRC-1, `oscopilot/agents/self_learning.py`; supplied runtime course route.
Claim IDs or none: [EPI-CLM-excel-learning](#epi-clm-excel-learning).
Mismatch marker or none: none.
Gap/limit: progression is not demonstrated learning or method revision.

Route ID: [EPI-RTE-page-content](#epi-rte-page-content)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-page-content](#epi-obj-page-content).
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown, with possible degradation by cleaning and omission.
Transition or check target: URL to response body, HTML/PDF extraction, cleaned string, possibly summary or selected chunks.
Evaluator/condition and domain: HTTP status checks transport success, token count chooses presentation; model summary and embedding similarity do not check source truth. See record for exact split.
Activation and timing: mounted page-load service, before response to client.
Possible or observed result: page_content only, including empty string on broad loader exception.
Implemented force: imported/reshaped assertions available for client reliance.
Epistemic authority and scope: no license from successful fetch to truth, faithful extraction or summary completeness. Concrete cleaning deduction below disproves universal semantic preservation.
Operational authority: behavior permitted, blocked, or changed: selected text replaces full page in returned response.
Behavioral-authority path: consumer, channel, force, horizon: requesting program/client, response page_content, advisory evidence, current call and any client-dependent continuation; ordinary API result may reach graph prompts.
Evidence source ID and local anchor: SRC-1, `oscopilot/tool_repository/api_tools/bing/web_loader.py`, `oscopilot/tool_repository/api_tools/bing/bing_service.py`, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`; see record passages.
Claim IDs or none: none.
Mismatch marker or none: cleaned does not entail meaning-preserving.
Gap/limit: summary relation internally indeterminate without actual text; selection is non-ampliative omission/grouping, not corroboration. No independent rejection of false content.

Route ID: [EPI-RTE-gaia-comparison](#epi-rte-gaia-comparison)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: model_answer and groundtruth, see route.
Content/update relation: truth-apt transformation: entailed derivation; for given strings the equality branch entails only that they match, not that the original answer is semantically correct.
Transition or check target: postprocessed model_answer versus dataset Final answer, exact-string domain.
Evaluator/condition and domain: software equality, external reference-answer oracle; see route for proposer, mode and limits.
Activation and timing: after task run/postprocessing in batch, or on previously written rows in get_numbers.
Possible or observed result: counter increments, result row, accuracy print; no supplied executed comparison.
Implemented force: benchmark accounting only, not agent repair or tool admission.
Epistemic authority and scope: exact agreement with the supplied reference after postprocessing; no causally warranted component, mechanism or transfer claim.
Operational authority: behavior permitted, blocked, or changed: reporting counters and last-index resume; no measured-error feedback to improve agent.
Behavioral-authority path: consumer, channel, force, horizon: benchmark counter/report and result-file loader; result fields/index, accounting and resume selection, current and subsequent benchmark launches.
Evidence source ID and local anchor: SRC-1, `examples/GAIA/run_GAIA.py`; see record passages.
Claim IDs or none: none.
Mismatch marker or none: exact-match oracle is mode-specific, not the FRIDAY judge's oracle.
Gap/limit: dataset truth, postprocessing fidelity and task performance not established.

Route ID: [RT-RTE-example-loops](runtime.md#rt-rte-example-loops)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: response code, feedback text and screenshots, see route.
Content/update relation: non-truth-apt policy/content update: model selects actions and terminal phrase from accumulated observations.
Transition or check target: response to immediate code execution and substring termination.
Evaluator/condition and domain: loop tests terminal substring after processing code; vision model is instructed to inspect screenshots. No independent correctness oracle; see route.
Activation and timing: each example iteration.
Possible or observed result: next program or stop; no observed success.
Implemented force: direct interpreter dispatch, history supply, termination.
Epistemic authority and scope: observations are evidence inputs, not automatically accepted explanations or verified outcomes.
Operational authority: behavior permitted, blocked, or changed: execution and continuation bypass ordinary FridayAgent gate.
Behavioral-authority path: consumer, channel, force, horizon: see route; model history to code and loop, current task plus host effects.
Evidence source ID and local anchor: SRC-1, `examples/light_friday/light_friday.py`, `examples/friday_vision/friday_vision.py`; supplied runtime passages.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: requested screenshot verification does not demonstrate its performance.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | see record | SRC-1, `setup.py`; doctrine/design | Reusable code and practice requested | [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [RT-RTE-course-learning](runtime.md#rt-rte-course-learning) | none supplied | No independently varied component or subsequent dependent-use trace | Improvement-directed dispositional pathway | Not exercised or successful improvement; repaired-code identity defect |
| [EPI-CLM-code-judgment](#epi-clm-code-judgment) | see record | SRC-1, `oscopilot/prompts/friday_pt.py`; doctrine/design | Completion and generality rubric | [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair) | none supplied | Output text is a limited proxy; no transfer experiment | Evidence-consuming model check with operative branch consumer | Not a reliable universal verifier; QA/API bypass |
| [EPI-CLM-excel-learning](#epi-clm-excel-learning) | see record | SRC-1, `docs/source/tutorials/self_learning.rst`; reported operation | Before/after task narrative | [RT-RTE-course-learning](runtime.md#rt-rte-course-learning), [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | none inspectable | No matched execution trace, retained-tool provenance, independent comparison or attribution | Tutorial reports improvement; implementation makes tool acquisition possible | Saved curriculum and possible tools do not establish mastery or causal benefit |

## Bounded conclusion

**There is a consequential local judgment route, but not a uniform warrant gate.** The model consumes execution evidence for code-task completion and produces a score/status; code uses the result to complete, repair or replan. This is more than merely logging a critique. Its evidence is nevertheless partial, its generality assessment extends beyond tested outcomes, and its initial fallback accepts unexpected statuses. QA/API and shipped simplified loops have different acceptance paths. See [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair), [RT-RTE-api-qa](runtime.md#rt-rte-api-qa), [RT-RTE-example-loops](runtime.md#rt-rte-example-loops).

**Retained tools are operational resources, not a demonstrated body of accepted claims.** Code/description entries are written automatically under a completion/score gate or directly by maintenance callers. They later supply ranked examples to planning/generation. The repaired-code identity defect weakens even the intended execution-to-admission connection. Manager storage does not preserve a judgment/evidence link or implement validation-driven rollback; deletion need not revoke live dictionary copies. No inspected route establishes lifecycle integration of an accepted ampliative claim. This is a bounded finding about these entries and writers, not a denial that arbitrary generated code might perform experiments. See [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), [RT-BAP-tool-context](runtime.md#rt-bap-tool-context).

**Web and perception routes acquire or propose content with unresolved warrant.** Page cleaning has a concrete meaning-changing case; summary output is unchecked; similarity-selected excerpts are relevant candidates, not corroboration. Audio, caption and OCR routes have distinct recognition targets and opaque provider quality. QA can use internal model knowledge or infer an answer without a subsequent fact check. No actual answer here individuates a produced ampliative proposition, and failure to establish entailment is not enough to classify it as conjecture. See [EPI-RTE-page-content](#epi-rte-page-content), [EPI-OBJ-qa-answer](#epi-obj-qa-answer) and the runtime component records.

**The deterministic comparison has a narrow formal license.** Given the same postprocessed string and reference string, GAIA equality establishes their equality. It does not establish source truth, postprocessor fidelity, task process correctness or component benefit. Its results affect accounting/resume, not agent acceptance. See [EPI-RTE-gaia-comparison](#epi-rte-gaia-comparison).

**Curriculum and repair can adapt action without producing accepted explanatory knowledge.** Course content shapes new tasks; candidate code and queued work can change after feedback. Static method prompts are not thereby revised. For the retained-tool pathway, the boundary is FRIDAY plus its tool state, objective is future reusable task capability, horizon is later tasks/sessions. Feedback-to-admission, durable update and a live context-delivery route are implemented, with the identity defect noted; causal link 4, subsequent operation depending on that update, is unestablished. This supports only a marked dispositional improvement-directed pathway. Successful improvement and learning each lack capacity/outcome and attribution evidence. Those limits do not negate computational action selection or feedback-responsive repair. A reflective theory builder and the four theory-builder conditions are not established by unidentified generated program content; the supplied runtime appropriately leaves concrete theory formulation/criticism uninspected rather than inferring it from iteration. See [RT-RTE-course-learning](runtime.md#rt-rte-course-learning), [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair), [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission).

## Shared records

### Components

#### EPI-CMP-web-models
Label: Web summary and embedding models

Source-native identity: BingAPIV2.web_summarizer and web_sniptter_embed. These are distinct distributed-parametric consumption paths: OpenAI completion inference for summaries and OpenAIEmbeddings inference for query ranking. Substrate is external provider state; vectors/documents are handed to Chroma for query selection. Neither exact weights nor dependency-selected model versions are pinned; mutable provider endpoints may resolve differently. No parameter update is requested in inspected implementation; provider-side changes remain uninspected. This is distinct from [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) and [RT-CMP-tool-embeddings](runtime.md#rt-cmp-tool-embeddings): separate constructors for web processing, not the BaseModule/tool repository adapters. Evidence: SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`, implementation.

> self.web_sniptter_embed = OpenAIEmbeddings()
> self.web_summarizer = OpenAI(
>     temperature=0,
>     )
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

### Operative objects

#### EPI-OBJ-candidate-code
Label: Generated and retained tool code

Source-native identity: generate_tool's code, repair_tool's new_code and manager entry code. Form: symbolic executable programs, separately natural-language docstrings interpreted by models; substrate is transient Python strings and, after admission, code files/JSON. The code is an action proposal, not intrinsically an explanatory theory. Specific factual or mathematical content remains not determinable without a candidate. This object spans [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair), [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance); those are routes, not duplicate code-object declarations. Its executable and model-context consumers differ. Evidence: SRC-1, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/agents/friday_agent.py`, implementation; supplied routes retain further passages.

> code = new_code
> --- `oscopilot/agents/friday_agent.py`

> return RepairingResult(status, code, critique, score, result)
> --- `oscopilot/agents/friday_agent.py`

#### EPI-OBJ-judgment-result
Label: Judge reasoning status and score
Part of: [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)

This object is the material verdict part of the parent route, not a duplicate route. Source-native identity: judge_json reasoning/status/score, then JudgementResult/RepairingResult. Natural-language reasoning and symbolic status/numeric score live in transient dictionaries/result objects. Reasoning concerns candidate fit and failure; score claims generality. The branch consumer grants operational force to status and retention score, not blanket warrant to all reasoning. Evidence: SRC-1, `oscopilot/modules/executor/friday_executor.py`, implementation; [EPI-CLM-code-judgment](#epi-clm-code-judgment) supplies the requested semantic target.

> reasoning = judge_json['reasoning']
> status = judge_json['status']
> score = judge_json['score']
> --- `oscopilot/modules/executor/friday_executor.py`

#### EPI-OBJ-tool-description
Label: Retained tool descriptions

Source-native identity: program_description and generated_tools[name][description]. Natural-language behavior claims are stored in JSON/text files and embedded for numerical relevance ranking. They come from the first matching docstring line/sentence, not independent documentation. This object overlaps the endpoints of [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), distinct from their write operations and from [RT-CMP-tool-embeddings](runtime.md#rt-cmp-tool-embeddings), which is the inference component. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`, implementation; automatic extraction also described in supplied admission record.

> pattern = r'"""\s*\n\s*(.*?)[\.\n]'
> match = re.search(pattern, code)
> if match:
>     description = match.group(1)
> --- `oscopilot/tool_repository/manager/tool_manager.py`

> self.generated_tools[program_name] = {
>     "code": program_code,
>     "description": program_description,
> }
> --- `oscopilot/tool_repository/manager/tool_manager.py`

#### EPI-OBJ-course-text
Label: Prior course lesson text
Part of: [RT-RTE-course-learning](runtime.md#rt-rte-course-learning)

This is the retained curriculum part of the parent route. Source-native identity: new_course, self.course and prior_course. Natural-language lessons keyed in symbolic JSON/dictionaries persist in course files and in process. The intended prior-course interpretation is completed lessons; no outcome record accompanies each retained lesson in the supplied driver account. Evidence: SRC-1, `oscopilot/prompts/friday_pt.py`, doctrine/design; parent route gives saving and later-read implementation passages.

> 9. Prior Course refers to the courses that have already been completed. If the Prior Course is not empty, you need to design new lessons based on the existing ones to learn more complex operations of the package, ensuring that these new lessons do not duplicate any lessons that are already in Prior Course.
> --- `oscopilot/prompts/friday_pt.py`

#### EPI-OBJ-qa-answer
Label: QA answer text
Part of: [RT-RTE-api-qa](runtime.md#rt-rte-api-qa)

This is the QA output part, not a second declaration of the parent route. Source-native identity: result of question_and_answer_tool. Natural-language text in transient return/result fields is printed and can become graph prerequisite context. It can assert facts from prior results, internal model knowledge or inference. No answer instance is supplied, so truth, entailment and novelty remain not determinable. Evidence: SRC-1, `oscopilot/modules/executor/friday_executor.py`, implementation; `oscopilot/prompts/friday_pt.py`, doctrine/design.

> 1. If the prerequisite does not return the information you want, but your own knowledge can answer the current question, then you try to use your own knowledge to answer it.
> --- `oscopilot/prompts/friday_pt.py`

> 3. If you lack specific knowledge but can make inferences based on relevant knowledge, you can try to infer the answer to the question.
> --- `oscopilot/prompts/friday_pt.py`

#### EPI-OBJ-page-content
Label: Loaded and selected webpage content

Source-native identity: WebPageLoader content, BingAPIV2 page_content_str, summarized_page_content and attended_content. Form: natural-language text, with possible embedded formal expressions; substrate: HTTP bodies, transient strings and chunk Documents/Chroma representations. Raw extraction, model summary and selected excerpts have separate warrant limits, preserved in the page route. Closest supplied [RT-RTE-api-qa](runtime.md#rt-rte-api-qa) describes clients/service discovery, not the distinct web-content object or transformations; no supplied counterpart declares this object. Evidence: SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`, implementation.

> page_content_str = page_data["data"][0]["content"]
> return page_content_str
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

### Routes

#### EPI-RTE-page-content
Label: Web page acquisition and reshaping

The requesting client supplies URL and optional query. The mounted load_pagev2 route calls the loader, counts tokens and returns raw extracted content up to 4096 tokens; above that it returns a map-reduce model summary if query is absent, otherwise three similarity-selected chunks joined with ellipses. Bing search and image search expose separate result lists; neither corroborates page claims. This record adds service-internal content transformations to [RT-RTE-api-qa](runtime.md#rt-rte-api-qa), which names the client/API path but does not declare this processing route. No existing referent is replaced.

Owner: BingAPIV2/WebPageLoader and FastAPI handler. Content acquisition uses external HTTP and extraction; truth preservation is not checked. Model chooses summaries, embedding similarity chooses chunks, software chooses threshold branch. Human participation is only caller-supplied input, not per-content approval. Mode: open query; no expected-answer oracle, improvement trigger, durable capability admission or automatic knowledge acceptance. HTTP success and token count are not semantic evaluators.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: response dictionary containing page_content; raw loader URL metadata/hash are not forwarded by BingAPIV2.load_page.
- Later read-back: inapplicable — inspected page route declares no deliberate later-session content reload; dependency-internal Chroma persistence/lifecycle is uninspected.
- Delegated visibility: external HTTP server receives requested URL/headers; summarizer receives chunks; embedding provider receives chunk/query material. Exact live payloads are unobserved.
- Selection predicate: HTML versus PDF Content-Type; HTML tag/id/class filters; <=4096 token raw response, otherwise no-query summary or query-selected k=3 chunks.
- Invalidation or expiry: no response revision, source endorsement or freshness acceptance recorded; dependency cache/index cleanup uninspected. Loader exceptions collapse to empty content.
- Activation or effect: response content is replaced by selected/summary text; downstream reliance is possible but actual behavior change unobserved.
- Evidence limits: implementation deduction only, no live pages, summary outputs or provider evaluation; external source truth unknown. No semantic rejection, evidence-linked acceptance or rollback of a claim is visible in these read functions.

Evidence: SRC-1, `oscopilot/tool_repository/api_tools/bing/web_loader.py`, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`, `oscopilot/tool_repository/api_tools/bing/bing_service.py`, implementation.

> cleaned_text = cleaned_text.replace("\\", "")
> --- `oscopilot/tool_repository/api_tools/bing/web_loader.py`

> cleaned_text = cleaned_text.replace("#", " ")
> --- `oscopilot/tool_repository/api_tools/bing/web_loader.py`

> cleaned_text = re.sub(r"([^\w\s])\1*", r"\1", cleaned_text)
> --- `oscopilot/tool_repository/api_tools/bing/web_loader.py`

Concrete static deduction: pass the text `1 == 1` to clean_string. Newline, whitespace, backslash and hash rules leave it unchanged; the final regex collapses the repeated equals signs to one, yielding `1 = 1`. In a Python-expression domain a boolean equality expression has become an assignment statement. Thus universal non-ampliative semantic preservation is false; actual prose/page truth effects remain content-dependent. This uses implementation evidence without target execution.

> summarize_chain = load_summarize_chain(self.web_summarizer, chain_type="map_reduce")
> main_web_content = summarize_chain.run(web_chunks)
> return main_web_content
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

> relatedChunks = chunSearch.similarity_search(query_str, k=3)
> attended_content = '...'.join([chunk.page_content for chunk in relatedChunks])
> return attended_content
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

> if(page_token_num <= 4096):
>     result = {"page_content": raw_page_content}
> --- `oscopilot/tool_repository/api_tools/bing/bing_service.py`

#### EPI-RTE-gaia-comparison
Label: GAIA exact answer comparison

Source-native endpoints: batch agent result → GAIA_postprocess → model_answer/reference equality → output row/counters; get_numbers reloads prior rows and returns last index for resume. Owner: GAIA script. This is a distinct benchmark evaluator route; [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) mentions the same code as a mode-specific oracle but does not declare its route. It does not alter the ordinary [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair) or [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission).

Model/agent proposes answer; dataset supplies Final answer oracle; fixed equality decides credit; no computational or human veto of agent actions follows the comparison. Mode: benchmark batch, not a controlled causal experiment; no improvement-triggered update or proposal admission. Single-task branch comments out agent.run and postprocesses a literal answer, so is not an execution witness. Postprocessing implementation remains uninspected here: comparison license is deliberately only over its output strings.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: updated correct counter, appended JSONL row and final printed aggregate.
- Later read-back: get_numbers reads prior model_answer/groundtruth and final index; prior rows affect counters/resume rather than the agent's task reasoning.
- Delegated visibility: inapplicable — ordinary synchronous agent/model calls, no delegated worker.
- Selection predicate: gaia_task_id selects literal single-item branch; otherwise validation task iteration, skipping indices <= last_run_index; string equality chooses credit.
- Invalidation or expiry: rows append; no revalidation of oracle correctness or changed postprocessor semantics is implemented in this script.
- Activation or effect: comparison changes accounting; resumed run selection is wired; no observed benchmark run supplied.
- Evidence limits: no dataset/result execution, no accuracy estimate, no independent intervention or successful improvement attribution; empty reasoning_trace prevents process reconstruction from the row alone.

Evidence: SRC-1, `examples/GAIA/run_GAIA.py`, implementation.

> if d["model_answer"] == d["groundtruth"]:
>     correct += 1
> --- `examples/GAIA/run_GAIA.py`

> if result == task["Final answer"]:
>     correct += 1
> --- `examples/GAIA/run_GAIA.py`

> if count <= last_run_index:
>     print("\t\t\t skip current run:", count)
>     count += 1
>     continue
> --- `examples/GAIA/run_GAIA.py`

Concrete static deduction: given result `17000` and Final answer `17000` as strings, equality increments correct; result `17000 ` with trailing space does not match at this comparison point. This deduction is over inspected equality, not a claim about what the uninspected postprocessor produces or what any task's correct answer is.

### Claims

#### EPI-CLM-code-judgment
Label: Code task verification and generality judgment

Claimed operation: verify code against user requirements from execution feedback and score generalizability. Distinct from [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement), which concerns improvement of the enclosing agent; this is the narrower evaluator contract. Evidence: SRC-1, `oscopilot/prompts/friday_pt.py`, doctrine/design. Implementation consumer is [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair).

> Your goal is to determine if the provided code accomplishes the user's specified task based on the feedback information, And score the code based on the degree of generalizability of the code.
> --- `oscopilot/prompts/friday_pt.py`

The countervailing clause is retained in the supplied route's quote: code output indicating completion can suffice. It limits the warrant of the requested verification; it does not erase that an evidence-consuming judgment route exists.

#### EPI-CLM-excel-learning
Label: Excel ability acquired through learning

Claimed operation: exploratory self-learning expands tools and enables a previously failed Excel task. Closest supplied [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) is a general design claim; this is a tutorial's specific attributed outcome, with no inspectable run or causal comparison supplied. Evidence: SRC-1, `docs/source/tutorials/self_learning.rst`, reported operation. It supports attribution of the report, not authentication of improvement.

> This time, FRIDAY will successfully complete the task, demonstrating the acquired ability to manipulate Excel files through the learned tools.
> --- `docs/source/tutorials/self_learning.rst`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
