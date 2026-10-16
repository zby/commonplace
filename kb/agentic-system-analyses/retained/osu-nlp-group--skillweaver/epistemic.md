---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SkillWeaver's routes from browser practice to claims, tested labels and executable skills, with the scope of their checks and later reliance."
run-id: AAS-2026-10-14-skillweaver-c921cc7a5ed0-01
reviewed-boundary: f2a63d65d0f6ff46ac30e817cede8797f8f25b97
---

# SkillWeaver epistemic report

## Source-and-claim boundary

The question is what browser practice licenses SkillWeaver to retain and use as reusable website knowledge, and what its evaluators actually establish. Scope, dependencies and frozen evidence identity are those of [boundary](boundary.md#boundary-and-evidence); source identities and evidence layers are in its [Source register](boundary.md#source-register). This is a source inspection, not a target execution. The whole-system functional boundary includes both the builder and its shipped consumers. Coverage below is deliberately less than an exhaustive epistemic audit of every shipped skill or scoring variant.

The consequential public claim is [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement). The update instructions' procedural generalization and semantic-knowledge language are separately recorded in [EPI-CLM-website-knowledge](#epi-clm-website-knowledge). Their request for useful general procedures is not evidence of correct generalization.

| Entry point or operation | Source path under SRC-1 | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| Exploration CLI, proposal, scheduling and practice | `skillweaver/explore.py` | Supplied [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice); direct reads of imports, test predicate and iteration update branch; [EPI-RTE-success-decision](#epi-rte-success-decision), [EPI-RTE-test-check](#epi-rte-test-check) | Proposal/argument-generation quality assessed only through supplied runtime; no observed exercise or curriculum benefit. |
| Native task CLI and action generation/execution | `skillweaver/attempt_task.py`, `skillweaver/agent.py` | Supplied [RT-RTE-native-task](runtime.md#rt-rte-native-task); direct reads of formatting/call detection and trajectory serializer; [EPI-RTE-trajectory-format](#epi-rte-trajectory-format) | No full verification of arbitrary generated code or its website effects. |
| Success judgment | `skillweaver/knowledge_base/check_success.py` | Direct full read; [EPI-RTE-success-check](#epi-rte-success-check) | Provider internals and judgment reliability unavailable; no independent outcome oracle for exploration. |
| Skill synthesis, checks, merge, save and reload | `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/knowledge_base/code_verification.py` | Direct reads of initialization through retrieval, controller and loader; full checker read; [EPI-RTE-code-check](#epi-rte-code-check), [EPI-RTE-skill-merge](#epi-rte-skill-merge), [EPI-RTE-tested-label](#epi-rte-tested-label); supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | External static-checker implementation uninspected; no proof of function semantics. |
| Retrieval, optional embedding selection, OpenAI tool-schema exports and controller callbacks | `skillweaver/knowledge_base/knowledge_base.py` | Direct reads of exposed methods; supplied [RT-CMP-embed](runtime.md#rt-cmp-embed), [RT-RTE-native-task](runtime.md#rt-rte-native-task), [RT-RTE-browser-use](runtime.md#rt-rte-browser-use) | Export/retrieval is not acceptance; external tool clients and Browser-Use internals uninspected. |
| Procedural single-episode prompt and base instructions | `skillweaver/templates/kb_procedural_update_single.md`, `skillweaver/templates/kb_procedural_update_base.md` | Direct full reads; [EPI-CLM-website-knowledge](#epi-clm-website-knowledge) | Multiple-episode and semantic templates are available but not fully assessed; search finds no active semantic-update call in the inspected builder. No repository-complete negative about every possible caller. |
| Locator-recovery hooks | `skillweaver/environment/patches.py` | Supplied [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery); direct serializer inspection tests onward recovery visibility | Immediate consistency checks do not establish user intent; no recovery success trace. |
| Benchmark orchestration and evaluator dispatch | `skillweaver/evaluation/evaluate_single_task.py`, `skillweaver/evaluation/evaluate_benchmark.py` | Direct single-task result-consumer branch; supplied [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation), [RT-ABS-cua-module](runtime.md#rt-abs-cua-module) | Missing import and CLI mismatch limit clean-pin activation; no supplied score or comparison. |
| WebArena string and URL checks | `skillweaver/evaluation/webarena_evaluators.py` | Direct `StringEvaluator` and `URLEvaluator` reads; [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) | HTML, visual, debug and helper/model judging bodies not fully inspected. Their exact warrant remains unassessed, preventing a system-complete evaluator verdict. |
| Shipped skill claims and code | `skillnet/map/map_kb_post_code.py` | Direct first four function bodies/docstrings; [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings); other four libraries sampled in boundary | No route-linked provenance for sample claims; remaining skill bodies available but uninspected. No correctness or generalization verdict over all shipped APIs. |
| Browser observation, model clients, containers and utility callers | `skillweaver/environment/browser.py`, `skillweaver/lm.py`, `skillweaver/containerization/serve.py`, `skillweaver/util/run_for_demo_video.py` | Supplied boundary/runtime coverage, including [RT-CMP-lm](runtime.md#rt-cmp-lm) | Browser/site/provider internals not frozen. No observation-fidelity, reproducibility or provider-learning finding. |

Additional searches in SRC-1's `skillweaver/` located `mark_all_as_tested`, `discard_references`, semantic-update references, multiple-episode template references and `check_success` callers. These extend coverage of exposed operations beyond the runtime narrative, not the source boundary. `mark_all_as_tested` is exposed by the class, with no caller found in that scoped search; imported semantic text is supported, but active semantic synthesis is not established by the inspected update. Missing run evidence prevents observed acceptance, exercised self-improvement and learning benefit; missing intervention/comparison evidence independently prevents causal attribution. Available uninspected evaluators and skill bodies are not access gaps.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-trajectory-string](#epi-obj-trajectory-string) | Observed URL/title/tree, action outputs/errors; model reasoning and terminal answer claims | Episode evidence for judgment/synthesis; see record | SRC-1, `skillweaver/agent.py` | Initial-only and recovery omission degrade lineage; observation fidelity unverified. |
| [EPI-OBJ-skill-code](#epi-obj-skill-code) | Code alone is a procedure, not automatically a proposition; implied claim that its operations achieve a task over a domain | Reusable executable skill; see record | SRC-1, `skillweaver/knowledge_base/knowledge_base.py` | Actual synthesized instance semantics not determinable without candidate and inputs. |
| [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings) | Behavior, precondition and usage-success claims | Model-visible guidance; see record | SRC-1, `skillnet/map/map_kb_post_code.py`; `skillweaver/knowledge_base/knowledge_base.py` | Sample claims available, not authenticated or linked to producer/check routes. |
| [EPI-OBJ-function-metadata](#epi-obj-function-metadata) | Counters/events and tested status; reference strings are lineage pointers, not proof | Scheduling and visibility; see record | SRC-1, `skillweaver/knowledge_base/knowledge_base.py` | Tested label can be set without a test; references can be discarded. |
| [EPI-OBJ-semantic-knowledge](#epi-obj-semantic-knowledge) | Not determinable: arbitrary loaded text, no instance supplied | Semantic website knowledge; see record | SRC-1, `skillweaver/knowledge_base/knowledge_base.py` | Loader/prompt supply exists; semantic claim production and acceptance not established. |
| [EPI-OBJ-success-result](#epi-obj-success-result) | Claim that this task attempt succeeded, plus reasoning | Builder branch selector; see record | SRC-1, `skillweaver/knowledge_base/check_success.py` | Model judgment, not independent ground truth. |
| [EPI-OBJ-benchmark-result](#epi-obj-benchmark-result) | Config-relative outcome match/score | Reporting, not library admission; see record | SRC-1, `skillweaver/evaluation/evaluate_single_task.py` | No score instance or observed execution; scoring scope varies by evaluator. |
| [RT-CMP-lm](runtime.md#rt-cmp-lm), [RT-CMP-embed](runtime.md#rt-cmp-embed) | Distributed-parametric content cannot be individuated from client code | Generation/judgment/relevance; see records | SRC-1, `skillweaver/lm.py`; `skillweaver/knowledge_base/knowledge_base.py` | No weight access or target-owned weight updates; endpoint version/fixity limits remain local to those components. |

## Authority-route ledger

Each entry separates the function assessed here from any larger runtime container. Shared records own endpoints, timing, results, force, scopes, consumers and evidence; `see` below delegates those fields rather than copying their account. Architectural status and content/update relation are the overlay's assessments. None of these implemented entries asserts observed operation.

Route ID: [EPI-RTE-trajectory-format](#epi-rte-trajectory-format)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-string](#epi-obj-trajectory-string).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-trajectory-format](#epi-rte-trajectory-format).
Claim IDs: [EPI-CLM-website-knowledge](#epi-clm-website-knowledge).
Mismatch marker: omitted later states/recovery can remove evidence of the producing process.
Gap/limit: selective representation is not a complete trajectory or evidence of successful effects.

Route ID: [EPI-RTE-success-check](#epi-rte-success-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-success-result](#epi-obj-success-result).
Content/update relation: truth-apt transformation: ampliative conjecture.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-success-check](#epi-rte-success-check).
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: no independent answer oracle.
Gap/limit: outcome inference is defeasible even with a final screenshot.

Route ID: [EPI-RTE-success-decision](#epi-rte-success-decision)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-success-result](#epi-obj-success-result).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-success-decision](#epi-rte-success-decision).
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement), [EPI-CLM-website-knowledge](#epi-clm-website-knowledge).
Mismatch marker: accepts an attempt as synthesis input, not an unseen generalized skill as correct.
Gap/limit: the successful-input criterion does not transfer its license to a new procedure's general domain.

Route ID: [EPI-RTE-test-check](#epi-rte-test-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-function-metadata](#epi-obj-function-metadata).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-test-check](#epi-rte-test-check).
Claim IDs: none.
Mismatch marker: syntactic call detection does not prove a function was executed.
Gap/limit: deduction is only about supplied code and result fields, whose completeness is assumed, not task achievement.

Route ID: [EPI-RTE-tested-label](#epi-rte-tested-label)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-function-metadata](#epi-obj-function-metadata).
Content/update relation: non-truth-apt policy/content update: counters and visibility status.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-tested-label](#epi-rte-tested-label), restricted here to automatic increment and later `is_tested` filtering after the test predicate passes.
Claim IDs: none.
Mismatch marker: automatic status inherits the shortcut's limited record-relative criterion.
Gap/limit: status controls filtered presentation and practice, not all native executable definitions.

Route ID: [EPI-RTE-tested-label](#epi-rte-tested-label)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-function-metadata](#epi-obj-function-metadata).
Content/update relation: non-truth-apt policy/content update: override tested status and metadata history.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-tested-label](#epi-rte-tested-label), restricted here to caller invocation of `mark_all_as_tested`. There is no evaluator: code sets all counts to one and replaces histories; later filtering treats entries as tested.
Claim IDs: none.
Mismatch marker: the override confers a tested label without test evidence.
Gap/limit: invocation and caller identity uninspected; no corresponding epistemic license follows from this operation.

Route ID: [EPI-RTE-code-check](#epi-rte-code-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-code](#epi-obj-skill-code), [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-code-check](#epi-rte-code-check).
Claim IDs: [EPI-CLM-website-knowledge](#epi-clm-website-knowledge).
Mismatch marker: checks are constraints on code text/AST/type diagnostics, not tests of docstring truth or website outcomes.
Gap/limit: external type-checker completeness uninspected; no final veto after retry exhaustion.

Route ID: [EPI-RTE-skill-merge](#epi-rte-skill-merge)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-code](#epi-obj-skill-code), [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-skill-merge](#epi-rte-skill-merge).
Claim IDs: [EPI-CLM-website-knowledge](#epi-clm-website-knowledge), [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: generalization is requested; the content relation of arbitrary generated procedures/docstrings is not established.
Gap/limit: may reshape prior content or introduce unsupported generalizations; candidate/trace comparison is needed to decide. Not lifecycle integration: no accepted generalized claim is established by merge.

Route ID: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-code](#epi-obj-skill-code), [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings), [EPI-OBJ-function-metadata](#epi-obj-function-metadata), [EPI-OBJ-semantic-knowledge](#epi-obj-semantic-knowledge).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), restricted here to checkpointing already merged code/metadata and existing semantic text.
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: retention does not establish acceptance.
Gap/limit: file reload permits later use, not proof that stored behavior is warranted or exercised.

Route ID: [RT-RTE-native-task](runtime.md#rt-rte-native-task)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-code](#epi-obj-skill-code), [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [RT-RTE-native-task](runtime.md#rt-rte-native-task) and [RT-BAP-library-execution](runtime.md#rt-bap-library-execution), restricted here to native consumption. Native descriptions rank/guide model choices while all code is assembled.
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: retrieval selects relevance, not truth or correctness.
Gap/limit: delivered guidance may not be followed; available code may not be invoked. Optional embedding selection and exported tool schemas also grant no outcome warrant (SRC-1, `skillweaver/knowledge_base/knowledge_base.py`).

Route ID: [RT-RTE-browser-use](runtime.md#rt-rte-browser-use)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-code](#epi-obj-skill-code), [EPI-OBJ-skill-docstrings](#epi-obj-skill-docstrings).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [RT-RTE-browser-use](runtime.md#rt-rte-browser-use) and [RT-BAP-library-execution](runtime.md#rt-bap-library-execution), restricted to the external controller. Selected callback descriptions guide the external planner; registered callbacks permit captured-function execution on its current page.
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: callback registration confers executable availability, not correctness or task success.
Gap/limit: the external planner and compatibility are uninspected; this consumer does not inherit the native action checker or exception-tracking protocol.

Route ID: [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trajectory-string](#epi-obj-trajectory-string) for the repair record; the immediate replacement locator is task-local.
Content/update relation: non-truth-apt policy/content update: replace an immediate locator selection.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery).
Claim IDs: none.
Mismatch marker: local identity/count consistency is not correct intended-target selection.
Gap/limit: original-operation retry is permitted, not library correction; default builder serialization omits repair evidence.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-benchmark-result](#epi-obj-benchmark-result).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-benchmark-check](#epi-rte-benchmark-check), restricted to deterministic terminal-answer normalization/equality/inclusion against configured references.
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: matching configured answer does not validate skill mechanisms, transfer or component effect.
Gap/limit: fuzzy judging is separate; dispatch has source-level activation defects.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-benchmark-result](#epi-obj-benchmark-result).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-benchmark-check](#epi-rte-benchmark-check), restricted to final-state URL base-path/query containment. Its software evaluator checks configured reference components and returns a report-bound score; it grants no skill authority.
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: allowed URL containment is narrower than full task completion.
Gap/limit: reference encoding/completeness and actual final-state observation remain unverified.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-benchmark-result](#epi-obj-benchmark-result).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-benchmark-check](#epi-rte-benchmark-check), restricted to the inspected fuzzy-match handoff. The model helper receives prediction, reference and intent; its returned judgment influences the score/report, not library admission.
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: model similarity judgment is not a deterministic reference proof.
Gap/limit: helper internals and actual content instances uninspected; distinction between reshaping, derivation and conjecture cannot be established for arbitrary helper outputs. Other HTML/visual/debug variants remain outside assessed evaluator bodies.

Route ID: [EPI-RTE-score-retention](#epi-rte-score-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-benchmark-result](#epi-obj-benchmark-result).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see [EPI-RTE-score-retention](#epi-rte-score-retention).
Claim IDs: [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement).
Mismatch marker: benchmark scores are reported, not used to approve/reject/rollback skills in the inspected drivers.
Gap/limit: no observed result, intervention or comparison; no causal benefit follows from scoring code.

For lifecycle integration of accepted generalized website claims, no route found within boundary in the inspected update/merge and benchmark consumers. This negative is local: imported content can carry external acceptance history not supplied here, and uninspected skill bodies/evaluator variants prevent a system-complete negative. For semantic-claim production the active update does not perform it; loaded semantic text remains an imported input with unknown warrant, while broader semantic maintenance intent is doctrine only (see [EPI-OBJ-semantic-knowledge](#epi-obj-semantic-knowledge)).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement) | See record | SRC-1, `README.md`; doctrine/design | Autonomous reusable skill synthesis | [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-BAP-library-execution](runtime.md#rt-bap-library-execution) | None supplied | No intervention/comparison; source checks do not measure benefit | Connected improvement-directed self-change is implemented; own later action machinery can change | Exercised dependence and increased capacity/robustness not established. |
| [EPI-CLM-website-knowledge](#epi-clm-website-knowledge) | See record | SRC-1, `skillweaver/templates/kb_procedural_update_base.md`; doctrine/design | General case, behavior documentation, usage logs, semantic knowledge | [EPI-RTE-success-check](#epi-rte-success-check), [EPI-RTE-success-decision](#epi-rte-success-decision), [EPI-RTE-skill-merge](#epi-rte-skill-merge) | Shipped docstrings supply attributed success claims only, not producer/check traces | Single successful episode does not identify transfer mechanism; unseen semantic synthesis not established | Procedural generation is instructed and merged; docstrings can affect future choices | No behavioral acceptance of generalized code/docstring claims; semantic text is loadable but unchanged by inspected update. |

## Bounded conclusion

SkillWeaver implements a route from browser observations and task-local results to a selective textual episode, a model success judgment, and conditional procedural synthesis. The success decision consumes evidence against the intended attempt's task and accepts it **for use as synthesis input**. That is an operative, evidence-consuming acceptance with a narrow scope; it is not acceptance of the generated procedure's generalized task-achievement claims. The judgment is ampliative: initial tree, action log and final screenshot do not entail that all requested persistent website effects occurred. Its epistemic license remains a model's task-scoped inference; its operational license is enforcing permission to synthesize.

The tested label has an even narrower basis. The automatic predicate derives a Boolean from a syntactic named-call occurrence, absence of a recorded exception and absence of recorded recovery. It does not prove dynamic execution or success. The exposed override sets tested metadata without any check. The counter controls future sampling, prompt inclusion and optional visibility, while the native executor still assembles the complete library. Counter changes therefore adapt later policy without requiring a new truth-apt website claim.

Skills and their docstrings are retained and subsequently selected, displayed or executed. Selection licenses relevance/availability, not reliability. Website observation enters through an external browser/site contract whose fidelity is unverified. Imported libraries and semantic text have unknown source warrant; loader references can be removed, and initial metadata may be reconstructed without tests. Serialization removes later observations and recovery detail, so evidence lineage is degraded for success/synthesis even though a final screenshot independently reaches the success checker. A sample docstring's reported success does not establish which inspected route generated or accepted it.

The static checker derives constraint violations from code/AST and delegated type diagnostics; those constraints neither test docstring truth nor prove website outcomes. Violations influence repair requests, not an invariant final gate. Merge gives a candidate executable authority after bounded retries; checkpoints/reload extend that authority to later iterations and sessions. Same-name replacement resets tested status but does not withdraw all executable availability. These are operational installation and retention, not lifecycle integration after accepted generalization. Actual content relations of generated code/docstrings remain indeterminate without candidate/input instances; requested generalization alone cannot be classified as achieved ampliative knowledge production.

Benchmark exact-string and URL checks have a distinct reference-based domain: they can establish normalized answer equality or configured URL containment for an attempted task. Model-based fuzzy judging and uninspected HTML/visual variants are separate uncertainties. Scores reach output files and aggregate reporting, not a score-fed skill acceptance/rollback consumer in the inspected drivers. A successful configured outcome would not establish replay safety, transfer, producing process or library-component benefit. No execution or comparison evidence closes those gaps.

The builder is computation-driven in the inspected roles; no per-skill human veto is wired. It has an improvement-directed dispositional self-change path through live code consumers, but later behavior causally depending on an update and successful learning are unobserved. Locator recovery adapts immediate action selection without establishing correct user intent. Provider parameters and version resolution remain opaque as recorded by the runtime; symbolic skill updates are independent of weight updates. Method reflection and a formulated content-criticism loop are not established merely by synthesis reasoning and retained docstrings. These properties remain independent of the positive procedural adaptation and retention findings.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-trajectory-string
Label: Formatted browser episode

Source-native identity: `trajectory_string` from `codegen_trajectory_to_string`. Representational form: natural-language observation text, model reasoning and terminal content, with symbolic Python source embedded. Storage substrate: string and `trajectory_pretty.txt`; underlying states/actions are separate task-local data. No supplied operative-object counterpart; this is the evidence-input part of [RT-RTE-native-task](runtime.md#rt-rte-native-task) and [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), not a duplicate of either route. SRC-1, `skillweaver/agent.py`, `skillweaver/explore.py`; serializer passages below support its contents and omissions.

#### EPI-OBJ-skill-code
Label: Retained Python function definitions

Source-native identity: `KnowledgeBase.code`, especially top-level function definitions merged by `_apply`. Representational form: symbolic executable Python. Storage substrate: in-process string/AST and `_code.py` checkpoint. Procedural operations are not automatically truth-apt; implied efficacy must be individuated against a named intended task and domain. No supplied object counterpart; producer/consumer routes are [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) and [RT-BAP-library-execution](runtime.md#rt-bap-library-execution). SRC-1, `skillweaver/knowledge_base/knowledge_base.py`; their retained passages and merge passage below support persistence/execution.

#### EPI-OBJ-skill-docstrings
Label: Skill behavior and usage documentation

Source-native identity: function docstrings extracted by `ast.get_docstring` and shown by pretty formatting or controller action descriptions. Representational form: natural language, unlike the executable function body. Storage substrate: literals inside `_code.py`, parsed strings in function dictionaries. No supplied object counterpart; its advice path overlaps [RT-BAP-library-execution](runtime.md#rt-bap-library-execution) but is not its code-execution referent. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillnet/map/map_kb_post_code.py`.

A concrete candidate makes a truth-apt usage claim:

> Usage Log:
> - Successfully used to toggle between Satellite and Map views on OpenStreetMap.
> --- `skillnet/map/map_kb_post_code.py`

The associated body navigates and clicks the Layers link; the sample is neither a trace of a view change nor proof that synthesis/check/acceptance routes produced it. Outcome and transfer warrant remain unknown; documentation shipping is the only established instance fact.

#### EPI-OBJ-function-metadata
Label: Function test and version metadata

Source-native identity: `metadata["functions"]` entries with `test_count`, `version`, references/events and `global_version`. Representational form: symbolic counters, names and events; reference strings identify episode labels, not retained proofs. Storage substrate: dict and `_metadata.json`. No supplied object counterpart; distinct decision input to [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice) and [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). SRC-1, `skillweaver/knowledge_base/knowledge_base.py`; tested-label evidence below.

#### EPI-OBJ-semantic-knowledge
Label: Loaded semantic website text

Source-native identity: `semantic_knowledge`. Representational form: natural-language input, with no supplied content instance to individuate propositions. Storage substrate: string and `_semantic_knowledge.txt`, loaded when present and otherwise empty. No supplied operative-object counterpart; contextual input to [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), not that route's synthesized Python result. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/templates/kb_procedural_update_single.md`.

> with open(prefix_path + "_semantic_knowledge.txt") as f:
>     semantic_knowledge = f.read()
> --- `skillweaver/knowledge_base/knowledge_base.py`

> semantic_update_diagnostics = None
> --- `skillweaver/knowledge_base/knowledge_base.py`

> instructions = kb_procedural_update_single_templ(
>     procedural_knowledge=filtered_code,
>     semantic_knowledge=self.semantic_knowledge,
>     action_history=trajectory_string,
>     intended_task=task_string,
>     feedback=feedback,
> )
> --- `skillweaver/knowledge_base/knowledge_base.py`

The update reads existing semantic text into instructions, returns `None` semantic diagnostics and does not assign new semantic content in the inspected update. Save/load establishes retention/import, not active semantic theory production or acceptance. Existing text's warrant is unknown.

#### EPI-OBJ-success-result
Label: Model success judgment

Source-native identity: `success_check` containing reasoning and `success`. Representational form: natural-language reasoning plus symbolic Boolean. Storage substrate: returned dict and `success_check.json`. No supplied operative-object counterpart; result part of [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice). Its content is the task-scoped outcome judgment rather than the synthesized skill. SRC-1, `skillweaver/knowledge_base/check_success.py`, `skillweaver/explore.py`; passages below.

#### EPI-OBJ-benchmark-result
Label: Evaluation score and checks

Source-native identity: evaluator `result` with `score` and `checks`. Representational form: symbolic numeric score/check structure with possible natural-language debug detail. Storage substrate: dict, `eval.json` and aggregate artifacts. No supplied object counterpart; output part of [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation), distinct from exploration's success Boolean. SRC-1, `skillweaver/evaluation/evaluate_single_task.py`; consumer passage below.

### Routes

#### EPI-RTE-trajectory-format
Label: Trajectory evidence shaping
Part of: [RT-RTE-native-task](runtime.md#rt-rte-native-task)

This is the serializer part of the native task route, also used by exploration. Endpoints: states/actions → `codegen_trajectory_to_string` → judgment/synthesis text. Owner: deterministic formatter. It includes initial observation, model reasoning/code, stdout, output repr, warnings and truncated exception text; default arguments omit later states and recovery annotations. SRC-1, `skillweaver/agent.py`, `skillweaver/explore.py`; implementation evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: textual episode, with initial state and serialized actions.
- Later read-back: stored pretty trajectory can be inspected; same text is consumed immediately by success/synthesis. Automatic later re-ingestion of this file is uninspected — no such caller traced.
- Delegated visibility: success model gets text and final screenshot separately; synthesis gets text but not the final screenshot in its update call.
- Selection predicate: default `only_initial=True`, `include_recoveries=False`; action fields determine included text.
- Invalidation or expiry: per-iteration serialization; source states/actions remain separate artifacts, with no automatic substitution here.
- Activation or effect: enforcing context shaping for downstream model calls, advisory evidence within those calls; horizon current attempt and potentially the retained skills it influences.
- Evidence limits: no observed consumer response; incomplete text can conceal recovery or later UI state.

> only_initial=True,
> include_recoveries=False,
> --- `skillweaver/agent.py`

> if not only_initial:
>     trajectory_string += f"<state {i+1}>\n{state_to_string(states[i + 1], include_axtree=not only_initial)}\n</state {i+1}>\n\n"
> --- `skillweaver/agent.py`

> trajectory_string = codegen_trajectory_to_string(states, actions)
> --- `skillweaver/explore.py`

Concrete implementation deduction, not execution: take two states whose trees are `S0` and `S1`, and one action whose `terminate_with_result` is `done`. Default formatting emits the initial state's URL/title/tree and `<terminate_with_result>\ndone\n</terminate_with_result>`, followed by its separator; it does not emit `S1`. The conclusion follows from the default and conditional above, with the terminal branch:

> if action["terminate_with_result"]:
>     return (
>         "<terminate_with_result>\n"
>         + action["terminate_with_result"]
>         + "\n</terminate_with_result>"
>     )
> --- `skillweaver/agent.py`

This is non-ampliative selection/formatting, with degraded evidential lineage, not a checked semantic summary. It does not create warrant for terminal claims.

#### EPI-RTE-success-check
Label: Attempt success judgment
Part of: [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice)

Endpoints: task + selected trajectory + final screenshot → `check_success_simple` → reasoning/Boolean. Owner/evaluator: configured success LM. Check target: whether the attempted task was achieved, in the domain described by the task. This is a distinct checking part, not disposition. SRC-1, `skillweaver/knowledge_base/check_success.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reasoning and `success` Boolean.
- Later read-back: judgment is saved in `success_check.json`; automatic later re-evaluation is uninspected — no caller traced.
- Delegated visibility: task, textual episode and final screenshot, not an independent expected answer or authoritative backend state.
- Selection predicate: exploration reaches this when the test shortcut fails or task is not a qualifying test.
- Invalidation or expiry: judgment is attempt-local; no expiry or withdrawal policy traced for saved judgment.
- Activation or effect: Boolean reaches the disposition branch; it does not directly install code.
- Evidence limits: model quality, observation fidelity and actual result unobserved; no independent answer oracle.

> "text": f"Please observe the following action log of someone using a computer. They were trying to do the following task: {task}. Given this log and the screenshot of their screen at the end of their attempt, please conclude whether they were successful.\n\nTrajectory:\n{trajectory_stringified}",
> --- `skillweaver/knowledge_base/check_success.py`

> json_schema=J.struct(step_by_step_reasoning=J.string(), success=J.boolean()),
> --- `skillweaver/knowledge_base/check_success.py`

The outcome judgment is an ampliative conjecture over task success: an identical visible screenshot/log can accompany a failed durable server update or an unobserved omitted requirement. Thus the inputs do not entail the outcome proposition, not merely fail to prove it. No per-result human approval is implemented. Operating mode: bounded exploration/practice. Proposer and computational judge coincide in the success LM; its output has no independent veto here.

#### EPI-RTE-success-decision
Label: Successful-attempt synthesis permission
Part of: [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice)

Endpoints: returned success Boolean → `_run_explore_iteration` branch → update or unchanged checkpoint. Owner/decider: software. Criterion: the success model judges the intended attempt successful; intended use: admit that attempt's evidence as input for procedural synthesis; scope: this attempt, not future task variants. No separate check is performed by this branch. SRC-1, `skillweaver/explore.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: update diagnostics if true; otherwise no synthesis result.
- Later read-back: checkpoint and diagnostics persist; generated skills can be read by later iterations/tasks through the runtime consumers.
- Delegated visibility: synthesis receives task and formatted trajectory, not success-check reasoning or final screenshot through this call.
- Selection predicate: `success_check["success"]` permits update; false withholds it. Successful test shortcut instead increments metadata.
- Invalidation or expiry: permission is per iteration; no automatic rollback of effects already taken by the attempt.
- Activation or effect: enforcing permission/withholding of synthesis, horizon current iteration with later effects via merged skills.
- Evidence limits: no observed acceptance instance; accepts input episode, not the truth of new skill documentation or generalized efficacy.

> if success_check["success"]:
>     await aprint("Successful attempt! Updating knowledge base...")
>     update_diagnostics = await knowledge_base.update(
>         api_synthesis_lm,
>         task,
>         trajectory_string,
>         f"iter_{iteration}",
>     )
> --- `skillweaver/explore.py`

Software can withhold update on false; a human configures models but supplies no per-content veto. A provider failure or exception can prevent progression. The bounded practice objective is reusable automation; branch permission is not acceptance against that broader objective. No rollback is selected from benchmark results.

#### EPI-RTE-test-check
Label: Named-call error-free predicate
Part of: [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice)

Endpoints: task + last action → AST call search and result-field predicate → Boolean. Owner/evaluator: deterministic code. Domain: recorded source/result structure for the last action of a test task. It entails only that a matching `ast.Name` call occurs somewhere and the recorded exception/recovery fields pass. SRC-1, `skillweaver/explore.py`, `skillweaver/attempt_task.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean predicate, not a website reference outcome.
- Later read-back: test-status consumer records a counter/event when true; predicate itself is not a retained memory object.
- Delegated visibility: task name, last-action source and exception/recovery fields; no backend state or intended-outcome check.
- Selection predicate: task type test, required fields present, named-call occurrence, no recorded exception/recovery.
- Invalidation or expiry: recomputed per iteration; metadata resets on replacement in the separate merge route.
- Activation or effect: enforcing branch selection between counter increment and model success judgment.
- Evidence limits: AST occurrence is not dynamic execution; recorded lack of exception is not outcome success.

> for node in ast.walk(tree):
>     if isinstance(node, ast.Call):
>         if isinstance(node.func, ast.Name) and node.func.id == function_name:
>             return True
> --- `skillweaver/attempt_task.py`

> return last_has_call_to_test_function and not (
>     last_has_exception or last_has_recovery_attempts
> )
> --- `skillweaver/explore.py`

Concrete countercase deduced from implementation: `async def act(page):\n    if False:\n        await target(page)` contains a matching call node but never executes `target`. With test task `target`, no exception and empty recovery results, this predicate returns true. No target execution is needed for the deduction. This qualifies the supplied runtime's “successful test”/“error-free execution” wording: the route is a **syntactic named-call plus result-field shortcut**, not execution coverage. The main runtime finding that it does not verify website outcomes remains supported; no supplied record is silently rewritten. No human judge or answer oracle intervenes. Operating mode: bounded function practice.

#### EPI-RTE-tested-label
Label: Tested metadata and filtered visibility

The automatic increment is part of [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), but this record also covers the independently exposed `mark_all_as_tested` override and shared `is_tested` consumer. It spans those operations, so is not wholly contained by exactly one supplied route. Endpoints: test predicate or caller override → metadata → tested visibility/filtering and future practice. Owner: `KnowledgeBase`; decider: code or caller of override. This is policy admission, not a semantic acceptance check. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/explore.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutated counters/events; override also replaces version/reference/event information.
- Later read-back: metadata saves/reloads; `is_tested`, verified-only synthesis/prompt filtering and practice selection consume it later.
- Delegated visibility: filter can show tested descriptions and specially included functions; `force_return_all`/native code assembly can bypass that presentation filter.
- Selection predicate: `test_count > 0`; automatic increment on shortcut, override sets all entries to one without checking execution.
- Invalidation or expiry: same-name merge resets test_count; caller override can reset histories; loader can discard references.
- Activation or effect: enforcing presentation/sampling policy; permissive inclusion in future synthesis, not an invariant execution barrier.
- Evidence limits: no observed test event; override invocation not found in scoped search; role of override caller cannot be inferred as human approval.

> def is_tested(self, function_name: str) -> bool:
>     return function_name in self.metadata["functions"] and (
>         self.metadata["functions"][function_name]["test_count"] > 0
>     )
> --- `skillweaver/knowledge_base/knowledge_base.py`

> fn["test_count"] = 1
> fn["version"] = 1
> fn["references"] = ["mark_all_as_tested"]
> --- `skillweaver/knowledge_base/knowledge_base.py`

> {"type": "exception_free_test", "reference": reference}
> --- `skillweaver/knowledge_base/knowledge_base.py`

> if discard_references:
>     for fn_name in kb.metadata["functions"].keys():
>         kb.metadata["functions"][fn_name]["references"] = []
> --- `skillweaver/knowledge_base/knowledge_base.py`

Override supplies no evaluator or reference outcome. Increment's authority is record-relative evidence, not proof of efficacy. Admission can be undone as a label by replacement, but all native executable definitions are not withdrawn by hiding. Human/computational contributions remain separate: automatic increment is code; override caller identity is uninspected. Shipped CLI reload with discarded references changes lineage without retesting (SRC-1, `skillweaver/explore.py`).

#### EPI-RTE-code-check
Label: Candidate coding-constraint checks
Part of: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Endpoints: candidate code + existing-code context → `check_code` → violation strings → bounded retry. Owner/evaluator: AST/text rules and delegated type diagnostics. Domain: syntax, permitted constructs, parameter/schema constraints, presence of documentation/navigation and selected selector/action forms. Proposer: synthesis LM; checker can request revision, not finally veto every candidate. SRC-1, `skillweaver/knowledge_base/code_verification.py`, `skillweaver/knowledge_base/knowledge_base.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: list of violations, including delegated type diagnostics.
- Later read-back: attempts/violations are logged in update diagnostics; retry context includes prior candidates and violations. Automatic use in later sessions is uninspected — no diagnostics loader traced.
- Delegated visibility: candidate text/AST and existing code reach checks; retry model gets exact candidate and reported violations.
- Selection predicate: violations trigger retry up to ten proposals; empty list breaks early.
- Invalidation or expiry: each new candidate is rechecked; final retry exhaustion proceeds to merge, with no retained accepted-warrant label.
- Activation or effect: enforcing retry decision before exhaustion, advisory criticism to model; no invariant final admission veto.
- Evidence limits: no behavioral test, docstring-truth check or reliable replay guarantee; type-checker internals uninspected.

> if "await page.goto(" not in source:
>     violations.append(
>         f"Please include an `await page.goto(url)` command as the first command in your function `{s.name}`. This ensures that the browser is in the correct state."
>     )
> --- `skillweaver/knowledge_base/code_verification.py`

This is a text occurrence check, despite its first-command wording. A `page.goto` after a click satisfies the occurrence test; the commented-out first-statement test does not enforce ordering. Documentation presence is separately checked:

> if not ast.get_docstring(s):
>     violations.append(
>         f"Please include a docstring for your function `{s.name}`."
>     )
> --- `skillweaver/knowledge_base/code_verification.py`

> violations = check_code(updated_code, "import asyncio\n" + self.code)
> --- `skillweaver/knowledge_base/knowledge_base.py`

Constraint results are entailed by inspected rules plus delegated diagnostics, not by warranted website premises. Static syntax errors may later stop parse/merge; parseable violations can survive exhaustion. No expected website answer oracle or per-candidate human veto is supplied. Operating mode: bounded syntactic repair within synthesis.

#### EPI-RTE-skill-merge
Label: Synthesis cleanup and function replacement
Part of: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Endpoints: successful-input task/trajectory + filtered library + semantic text → synthesis model → response cleanup/check loop → `_apply` name-indexed merge. Owner: `KnowledgeBase.update`/`_apply`; model proposes, software installs. This is the content-changing part of the larger runtime admission route, distinct from static checking and retention. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`; shaping instructions in `skillweaver/templates/kb_procedural_update_base.md` and `skillweaver/templates/kb_procedural_update_single.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutation of library and attempt diagnostics; same-name function definitions replace existing bodies/docstrings.
- Later read-back: merged definitions and metadata reach future task selection, retrieval and native/controller execution after save/reload.
- Delegated visibility: verified/specially included source, semantic text and selected trajectory reach synthesis; final screenshot/success reasoning do not pass through the shown update call.
- Selection predicate: true success branch invokes synthesis; new top-level functions are added/replaced by name regardless of final violation list after exhaustion.
- Invalidation or expiry: replacement increments version and resets test_count; nonreplaced functions remain. Parse errors can raise; no automatic rollback/best-prior-candidate selection shown.
- Activation or effect: permissive executable installation with later advisory docstring and symbolic code authority through RT-BAP-library-execution; activation remains unobserved.
- Evidence limits: cleanup/merge is not behavioral acceptance; arbitrary candidate semantics and actual generalization cannot be decided from prompt intent.

The runtime container supplies retry-exhaustion and unconditional `_apply` passages. Merge is explicitly name-local:

> updated_functions[node.name] = node
> --- `skillweaver/knowledge_base/knowledge_base.py`

> self.metadata["functions"][node.name]["test_count"] = 0
> --- `skillweaver/knowledge_base/knowledge_base.py`

Cleanup is not safely classifiable as formatting for every content edge:

> updated_code = (
>     updated_code.replace("```python3", "")
>     .replace("```python", "")
>     .replace("```", "")
>     .strip()
> )
> --- `skillweaver/knowledge_base/knowledge_base.py`

Concrete deduction: a candidate docstring containing the literal text `Use ```python examples` loses the literal ` ```python` sequence wherever it occurs, not just at a surrounding fence. The global replacement changes documentation strings as well as fence markup. For actual arbitrary responses, semantic preservation, entailment or novel generalization remains indeterminate; candidate/input evidence is needed. The merged AST retains function definitions but drops nonfunction top-level nodes, which can also remove candidate imports. No generalized outcome check occurs between synthesis and merge. No human veto is wired; parse/format errors can stop progression, static violations cause bounded retries, and earlier checkpoint recovery requires caller selection rather than automatic rollback. Persisted material is code/docstrings/metadata, not model weights or automatically accepted formulated criticism.

#### EPI-RTE-benchmark-check
Label: Reference-configured benchmark checking
Part of: [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)

Endpoints: config + terminal answer/final state → selected evaluator → score. Owner: evaluator dispatch and evaluator implementations. Inspected targets/domains: terminal answer normalized equality/inclusion against configured reference, and final URL base/query containment against configured URLs. This is a checking part distinct from result retention. SRC-1, `skillweaver/evaluation/webarena_evaluators.py`, `skillweaver/evaluation/evaluate_single_task.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: numeric match score, with optional debug check information through other dispatch variants.
- Later read-back: score-retention route makes reporting artifacts available; no automatic score-to-skill update traced.
- Delegated visibility: string check gets terminal response/config; URL check gets final state URL/config. Other evaluator visibility uninspected — their bodies were not fully read.
- Selection predicate: configured evaluator router and set/debug choice; reference approach chooses deterministic versus fuzzy judging.
- Invalidation or expiry: per-task evaluation; existing benchmark folders can be reused/skipped rather than automatically re-evaluated, as supplied runtime records.
- Activation or effect: computed score feeds report output; no admission, rollback or replay-safety guarantee.
- Evidence limits: deterministic matches validate configured representations, not source truth/encoding completeness; fuzzy judging remains model-dependent; no target run, clean-entry guarantee or causal comparison.

> return float(
>     StringEvaluator.clean_answer(pred) == StringEvaluator.clean_answer(ref)
> )
> --- `skillweaver/evaluation/webarena_evaluators.py`

> else:
>     # Was likely truncated.
>     return 0.0
> --- `skillweaver/evaluation/webarena_evaluators.py`

> ref_base_path in pred_base_paths
> --- `skillweaver/evaluation/webarena_evaluators.py`

> possible_ref_value in pred_query.get(k, [])
> --- `skillweaver/evaluation/webarena_evaluators.py`

The URL rule allows base-path containment, not necessarily strict equality; extra query values are not independently rejected by the shown test. The string checker lowercases and strips outer quotes, so normalized equality is its precise license, not textual identity. A model-based alternative exists:

> return llm_fuzzy_match(pred, ref, intent)
> --- `skillweaver/evaluation/webarena_evaluators.py`

Reference outcomes come from task configuration; their provenance and completeness are not validated here. Caller chooses benchmark tasks/options; evaluator software judges; model helper judges fuzzy cases. No per-score human veto is shown. Operating mode: fixed benchmark. The missing unconditional computer-use import limits enclosing-driver activation, not the existence of these inspected scoring methods.

#### EPI-RTE-score-retention
Label: Score artifacts and reporting consumer
Part of: [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)

Endpoints: evaluator result → `eval.json` → benchmark collection/reporting. Owner: evaluation drivers. This is result retention, not acceptance of skill content. SRC-1, `skillweaver/evaluation/evaluate_single_task.py`, `skillweaver/evaluation/evaluate_benchmark.py`; aggregate read-back is supplied by the runtime record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: persisted result file if evaluation reaches write; exceptions produce error diagnostics instead.
- Later read-back: benchmark driver reads result files and reports/aggregates scores; no score-fed library update is shown in inspected consumers.
- Delegated visibility: serialized result includes score/checks, not an automatically approved generalized procedure.
- Selection predicate: completed evaluation path writes result; benchmark reuse depends on existing task directories/results.
- Invalidation or expiry: caller controls output directories; metadata mismatch blocks reuse but existing tasks can be skipped. No automatic epistemic withdrawal of older scores established.
- Activation or effect: reporting evidence to later caller, advisory force, benchmark horizon; not live skill-authority revision.
- Evidence limits: no result instance, successful invocation or intervention supplied; report code cannot establish achieved performance.

> with open(out_dir + "/eval.json", "w") as f:
>     json.dump(result, f)
> --- `skillweaver/evaluation/evaluate_single_task.py`

Checking and retention are independently implemented even though source-level entry defects may prevent ordinary driver execution at this pin.

### Claims

#### EPI-CLM-website-knowledge
Label: Generalized website knowledge instructions

Claimed operation: maintain semantic website knowledge and procedural APIs representing general tasks, with behavior/usage documentation for later users. Source: SRC-1, `skillweaver/templates/kb_procedural_update_base.md`; doctrine/design. Distinct from [RT-CLM-self-improvement](runtime.md#rt-clm-self-improvement): this is the content contract requested of synthesis, rather than the README's performance/self-improvement framing.

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- benefit conclusion status: uninspected

Implementation status applies to supplying procedural instructions, not to semantic generation or reliable compliance with them.

> Try to make this logical procedure represent the general case of your task, rather than a specific case.
> --- `skillweaver/templates/kb_procedural_update_base.md`

> In your docstring, you must include a "usage log" which describes the different times you've used the function and what happened.
> --- `skillweaver/templates/kb_procedural_update_base.md`

> You are learning how to use a website. In addition to maintaining a semantic base of knowledge, you are also building a procedural knowledge base.
> --- `skillweaver/templates/kb_procedural_update_base.md`

A prompt assertion of learning/semantic maintenance is attributed intent. It does not establish increased future capacity, accepted generalized claims or active semantic-content mutation.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; the shared execution consumer is [RT-BAP-library-execution](runtime.md#rt-bap-library-execution). The local route records separately identify the judgment-to-permission, counter-to-visibility, checker-to-retry and score-to-report paths.
