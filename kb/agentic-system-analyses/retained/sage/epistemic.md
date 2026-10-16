---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SAGE epistemic routes: executable skill admission, benchmark evidence, expert selection and reward-mediated policy change."
run-id: AAS-2026-10-15-sage-d0de15ae5730-01
reviewed-boundary: "3c9244e82244abb1adc5467ee601a03ba0f433a0"
---

# SAGE epistemic report

## Source-and-claim boundary

The question is what licenses reliance on generated functions, task outcomes and resulting policy changes. Scope and exclusions are as declared in [boundary](boundary.md#boundary-and-evidence); sources are registered once in its [Source register](boundary.md#source-register). This report uses SRC-1 implementation and doctrine/design only. No observed run or causal experiment is supplied. The linked paper is not an additional source.

The material boundary includes RL, evaluation, expert generation, dataset extraction, SFT, and the registered full-code-reflexion alternative. Functions can express truth-apt input/output assertions through descriptions and implementations, but no generated function instance is frozen here. Their actual propositions and correctness are not determinable. Code that changes a task world is not automatically a claim about that world. Benchmark results are truth-apt over the invoked tests, not over arbitrary function inputs or the training mechanism.

Consequential claims: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules) and [EPI-CLM-self-evolution](#epi-clm-self-evolution). These are design requests and framing, not evidence of achieved warrant.

| Entry point or operation | Source path under SRC-1 | Coverage and records, or limit |
|---|---|---|
| RL launch, paired progression, reward and update | `sage/run_sage_2nodes.sh`; `sage/llm_agent/appworld_generation.py`; `sage/verl/trainer/main_ppo.py`; `sage/verl/trainer/ppo/ray_trainer.py` | Supplied findings: [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update). No new backend audit. |
| Training extraction and reuse counting | `sage/llm_agent/app_world/app_world_env.py` | Direct reads of extraction/count predicates; [EPI-RTE-function-extraction](#epi-rte-function-extraction), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install). |
| CLI run dispatch and standalone evaluation | `patches/appworld/src/appworld/cli.py` | Direct read of dispatch to configured runner and `evaluate_dataset`; evaluation reports have no inspected skill-withdrawal consumer. Base task path: [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop). |
| Task evaluation and post-task extraction | `patches/appworld/experiments/code/skill_library_agent/agent.py` | Direct read of `solve_task`; supplied expert branch: [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission). |
| Predefined load, four retrieval branches, execution, extraction and JSONL/embedding save | `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py` | Direct reads of constructor, initialization and extraction/save; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions). Numerical model identity limits: [RT-CMP-retrieval-model](runtime.md#rt-cmp-retrieval-model). |
| Registered API prediction and full-code-reflexion agent | `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`; `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py` | Both directly read in full; [EPI-RTE-api-prediction](#epi-rte-api-prediction), [EPI-RTE-code-retrial](#epi-rte-code-retrial). Additional route coverage, not a correction of runtime's selected routes. |
| Expert-to-dataset normalization | `patches/appworld/extract_expert_dataset.py` | Direct read in full; [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission). |
| Supervised token admission, checkpoints, provider tools | `patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py`; `sage/verl/trainer/ppo/ray_trainer.py`; `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py` | Supplied findings: [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update). Provider accepts tools, but supplied task route does not dispatch provider-native tools. No new tool guarantee. |
| Hooks and agent registration | `patches/appworld/experiments/code`; `sage/llm_agent` | Scoped source search for `reflex`, `ApiPredictor`, `api_predict`, `tools=`, `register`, `hook` found the additional registered reflexion route. This search does not establish repository-wide absence of other hooks. |
| Alternate launchers, other workers and vendored infrastructure | `sage/` | Included but not exhaustively inspected; detailed backend, alternate-configuration and system-complete negative conclusions are prevented. |

Missing upstream evaluator implementation prevents judging test adequacy, source-data fidelity and sandbox restrictions. Missing weights, predefined libraries, generated data and trajectories prevent identifying actual learned claims, expert errors, executed retries and accepted skill instances. Uninspected alternate workers prevent exhaustive negative claims about training behavior. None of these limits erases the independently inspected admission and consumption routes.

## Epistemic-object inventory

Object identity, form and substrate remain in the declaring records; this inventory adds only candidate-content assessments.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-skill-libraries](runtime.md#rt-obj-skill-libraries) | Function bodies can implement input/output mappings; concrete asserted scope not determinable | see record | see record; SRC-1 `sage/llm_agent/app_world/app_world_env.py` | Definitions are not proven total, correct or reusable. |
| [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions) | Same potential assertions; task ID records collection origin, not verification provenance | see record | see record; SRC-1 `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py` | Predefined contents unavailable; output records lack per-function acceptance evidence. |
| [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout) | No individually identified proposition in weights | see record | see record | Parameter change is inspectable; truth-apt content and learned competence are not. |
| [RT-CMP-language-model](runtime.md#rt-cmp-language-model) | Responses can contain claims; actual content not determinable | see record | see record | Endpoint and response internals uninspected. |
| [RT-CMP-retrieval-model](runtime.md#rt-cmp-retrieval-model) | Similarity ranks, not correctness assertions | see record | see record | Encoding preserves no inspected correctness warrant. |
| [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model) | No individually identified proposition in weights | see record | see record | Configured supervision is not evidence of acquired true claims. |
| [EPI-OBJ-predicted-apis](#epi-obj-predicted-apis) | Candidate relevance of API names to a task | see record | see record | Membership in documented API namespace is checked; necessity/sufficiency is not. |

Task instructions, API descriptions, ground-truth required-API lists, demonstration solutions and execution observations are imported context, not SAGE-produced knowledge. Their paths and consumers are in [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [EPI-RTE-api-prediction](#epi-rte-api-prediction) and [EPI-RTE-code-retrial](#epi-rte-code-retrial). Source warrant is unknown: the frozen wrappers neither independently authenticate nor audit the external data. Benchmark pass fractions are derived from reported pass/test counts; their arithmetic does not establish that the tests encode the intended real-world objective.

## Authority-route ledger

Each compact entry separates a consequential function even when several cite the same containing runtime route. Fields owned by supplied records say `see`; the classifications and bounded licenses here are this report's assessments. All implemented routes below are unobserved in this run.

Route ID: [EPI-RTE-function-extraction](#epi-rte-function-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill-libraries](runtime.md#rt-obj-skill-libraries); evaluation counterpart [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: generated program to retained function source.
Evaluator/condition and domain: AST-based source slicing; not a semantic evaluator.
Activation and timing: see record.
Possible or observed result: function/import fragments with surrounding top-level bindings omitted.
Implemented force: source selection, not acceptance.
Epistemic authority and scope: no semantic-preservation license for arbitrary programs; simple self-contained definitions can be preserved, but the counterexample in the record defeats a universal reshaping claim.
Operational authority: behavior permitted, blocked, or changed: extracted code becomes eligible for later installation.
Behavioral-authority path: see [RT-BAP-function-execution](runtime.md#rt-bap-function-execution) and [RT-BAP-function-guidance](runtime.md#rt-bap-function-guidance).
Evidence source ID and local anchor: see record.
Claim IDs or none: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules).
Mismatch marker or none: self-containment is requested, not established.
Gap/limit: actual generated content unavailable; no general entailment or ampliative-conjecture classification follows.

Route ID: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill-libraries](runtime.md#rt-obj-skill-libraries).
Content/update relation: no content change.
Transition or check target: first-subtask execution output and candidate parseability, not function correctness over new inputs.
Evaluator/condition and domain: see record; failure-marker absence and AST parse domain only.
Activation and timing: see record.
Possible or observed result: parseable function candidates after non-failing output.
Implemented force: evidence supplied to admission predicate.
Epistemic authority and scope: at most absence of the inspected failure marker and syntactic extraction; no task-success or general correctness warrant.
Operational authority: behavior permitted, blocked, or changed: feeds the next disposition, separately below.
Behavioral-authority path: batch environment, local output string, permissive predicate, current extraction.
Evidence source ID and local anchor: see record.
Claim IDs or none: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules).
Mismatch marker or none: execution success is weaker than function validation.
Gap/limit: dependency output conventions not independently audited.

Route ID: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill-libraries](runtime.md#rt-obj-skill-libraries).
Content/update relation: no content change.
Transition or check target: eligibility for dictionary insertion/replacement.
Evaluator/condition and domain: see record; software gate, no per-function human veto.
Activation and timing: see record.
Possible or observed result: add/replace or skip on parse failure.
Implemented force: enforcing admission to paired library.
Epistemic authority and scope: operational admission only; no evidence-consuming acceptance against a function-correctness criterion and intended input domain.
Operational authority: behavior permitted, blocked, or changed: next subtask may install admitted source.
Behavioral-authority path: see [RT-BAP-function-execution](runtime.md#rt-bap-function-execution).
Evidence source ID and local anchor: see record.
Claim IDs or none: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules).
Mismatch marker or none: retention must not be called epistemic acceptance.
Gap/limit: same-name overwrite is not a correctness-based withdrawal.

Route ID: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see cited records.
Content/update relation: no content change.
Transition or check target: selected definitions execute in a new task world before model action; subsequent prompt visibility depends on installation output.
Evaluator/condition and domain: see records; training searches for success marker, evaluation requires exact success output.
Activation and timing: see records.
Possible or observed result: execution attempted; prompt text retained or cleared.
Implemented force: executable delivery, followed by enforcing prompt suppression on failed gate.
Epistemic authority and scope: installation does not test function calls or grant correctness warrant.
Operational authority: behavior permitted, blocked, or changed: interpreter receives code before the gate; prompt withdrawal is not undo of imports, defaults, decorators or other attempted effects.
Behavioral-authority path: see [RT-BAP-function-execution](runtime.md#rt-bap-function-execution), [RT-BAP-function-guidance](runtime.md#rt-bap-function-guidance).
Evidence source ID and local anchor: see cited records.
Claim IDs or none: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules).
Mismatch marker or none: prompt suppression is not world rollback.
Gap/limit: caller-specific success predicates differ; no transactional guarantee.

Route ID: [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: task outcome, not an individually tested skill.
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: current task's test report to pass fraction and `task_success`.
Evaluator/condition and domain: external `world.evaluate`; wrapper computes passes/num_tests and equality to 1.0.
Activation and timing: see record; direct reread of `solve_task` after task execution.
Possible or observed result: Boolean success returned to sequential caller.
Implemented force: outcome reporting; conditional downstream use is separate below.
Epistemic authority and scope: arithmetic from supplied test counts, assuming valid nonzero denominator; external benchmark criterion only. Warrant of test premises remains unknown.
Operational authority: behavior permitted, blocked, or changed: caller stores previous-task success.
Behavioral-authority path: sequential agent, returned Boolean, advisory/reporting or conditional gate, next task.
Evidence source ID and local anchor: SRC-1 `patches/appworld/experiments/code/skill_library_agent/agent.py`; see record.
Claim IDs or none: none.
Mismatch marker or none: task completion API and benchmark success are distinct.
Gap/limit: benchmark adequacy uninspected; no component-effect inference.

Route ID: [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions).
Content/update relation: no content change.
Transition or check target: post-task extraction eligibility.
Evaluator/condition and domain: see record; default unconditional with skills enabled, optional `last_task_success` predicate.
Activation and timing: see record.
Possible or observed result: extract current task history or skip it.
Implemented force: enforcing extraction gate.
Epistemic authority and scope: no current-task or per-function correctness acceptance in this gate; optional label is about the previous task.
Operational authority: behavior permitted, blocked, or changed: current functions can enter later executable library despite current task failure.
Behavioral-authority path: base agent, Boolean/config branch, permissive or enforcing, later tasks.
Evidence source ID and local anchor: see record; direct reread SRC-1 `patches/appworld/experiments/code/skill_library_agent/agent.py`.
Claim IDs or none: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules).
Mismatch marker or none: prior outcome must not be attributed to current candidate.
Gap/limit: normal config and label-enabled alternative have different predicates.

Route ID: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)
Route function: retention
Architectural status: implemented
Object/candidate ID: see cited records.
Content/update relation: no content change.
Transition or check target: admitted source to pair dictionary or evaluation list/output JSONL.
Evaluator/condition and domain: see records; storage follows admission, not an additional truth test.
Activation and timing: see records.
Possible or observed result: in-process reuse; evaluation also writes JSONL and optional embeddings.
Implemented force: availability for later selection.
Epistemic authority and scope: no added warrant; task-origin labels do not record validation lineage.
Operational authority: behavior permitted, blocked, or changed: later worlds and prompts can receive retained code.
Behavioral-authority path: see [RT-BAP-function-execution](runtime.md#rt-bap-function-execution), [RT-BAP-function-guidance](runtime.md#rt-bap-function-guidance).
Evidence source ID and local anchor: see records.
Claim IDs or none: none.
Mismatch marker or none: persistence is not lifecycle integration after acceptance.
Gap/limit: pair dictionaries expire per rollout; evaluation output is not automatically its restart input.

Route ID: [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions), [RT-CMP-retrieval-model](runtime.md#rt-cmp-retrieval-model).
Content/update relation: no content change.
Transition or check target: retained functions to selected source prompt.
Evaluator/condition and domain: scenario-ID matching, name deduplication, optional skill/query embedding or n-gram ranking; see record.
Activation and timing: see record.
Possible or observed result: selected functions or empty source; constructor can import predefined JSONL.
Implemented force: ranking/selection, then execution and interpreted model guidance.
Epistemic authority and scope: similarity and shared scenario names license retrieval preference only, not truth, applicability or safety. Imported source warrant unknown.
Operational authority: behavior permitted, blocked, or changed: selection controls what interpreter and model receive.
Behavioral-authority path: see [RT-BAP-function-execution](runtime.md#rt-bap-function-execution), [RT-BAP-function-guidance](runtime.md#rt-bap-function-guidance).
Evidence source ID and local anchor: see record; direct read SRC-1 `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.
Claim IDs or none: [RT-CLM-function-rules](runtime.md#rt-clm-function-rules).
Mismatch marker or none: none.
Gap/limit: predefined provenance and embedding quality unavailable; default route does not use encoders.

Route ID: [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: task trajectory and extracted definitions; see record.
Content/update relation: no content change.
Transition or check target: task success, first-task nonempty extraction, and fresh-world definition execution.
Evaluator/condition and domain: see record; external benchmark plus execution failure marker in verification world.
Activation and timing: see record.
Possible or observed result: success/failure and installation evidence.
Implemented force: feeds retry/admission below.
Epistemic authority and scope: stronger than default library admission for the tested trajectory, but defining functions is not testing their outputs on new inputs.
Operational authority: behavior permitted, blocked, or changed: provides eligibility evidence to expert scenario controller.
Behavioral-authority path: scenario controller, test tracker/output string, enforcing predicate input, current retry.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-self-evolution](#epi-clm-self-evolution).
Mismatch marker or none: neither trajectory success nor install success warrants general skill correctness.
Gap/limit: supplied runtime passages, not independently inspected test implementation.

Route ID: [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see record.
Content/update relation: no content change.
Transition or check target: trajectory eligible for scenario progression and later dataset extraction.
Evaluator/condition and domain: see record; software decides, model proposes, operator launches, no per-candidate human veto.
Activation and timing: see record.
Possible or observed result: retry, admit progression, or record failure at retry bound.
Implemented force: enforcing admission to expert workflow.
Epistemic authority and scope: evidence-consuming acceptance for the benchmark-successful trajectory's intended training-data use, conditional on subsequent file filtering; not acceptance of each function's generalized specification.
Operational authority: behavior permitted, blocked, or changed: later scenario tasks receive definitions; selected logs can become supervision.
Behavioral-authority path: see record; task controller then extractor, enforcing, remaining scenario/offline training.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-self-evolution](#epi-clm-self-evolution).
Mismatch marker or none: acceptance has a narrower scope than general knowledge production.
Gap/limit: actual accepted examples unavailable.

Route ID: [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: selected LM-call messages; see record.
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: logs to normalized message dataset.
Evaluator/condition and domain: see record; first complete code fence controls normalized final assistant content; trailing content can be omitted.
Activation and timing: see record; direct read of live extraction path.
Possible or observed result: dataset messages with code-fence/whitespace normalization, or exclusion by no-code marker.
Implemented force: determines available supervision content, not a correctness test.
Epistemic authority and scope: no universal semantic-preservation license for removed explanation or later code blocks; exact retained examples unavailable.
Operational authority: behavior permitted, blocked, or changed: only retained/masked token targets train downstream model.
Behavioral-authority path: see record and [RT-BAP-policy-weights](runtime.md#rt-bap-policy-weights).
Evidence source ID and local anchor: SRC-1 `patches/appworld/extract_expert_dataset.py`; see record.
Claim IDs or none: none.
Mismatch marker or none: benchmark acceptance upstream does not warrant every normalized token.
Gap/limit: unused `make_map_fn` does not define exported truncation; source does not show actual generated dataset.

Route ID: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: second-task source and retained function names.
Content/update relation: no content change.
Transition or check target: textual name occurrence without `def ` plus name in non-failing source.
Evaluator/condition and domain: literal substring predicate; see [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout).
Activation and timing: during second subtask, prior to reward shaping.
Possible or observed result: incremented `skill_counts`.
Implemented force: numerical input to shaped reward.
Epistemic authority and scope: evidence of a string match, not of function invocation or beneficial reuse. A source comment containing a retained name but no `def ` can satisfy the inspected predicate without calling it.
Operational authority: behavior permitted, blocked, or changed: counted reuse can affect reward when success masks permit it.
Behavioral-authority path: generation manager, scalar count, numerical weighting, current batch and later policy updates.
Evidence source ID and local anchor: SRC-1 `sage/llm_agent/app_world/app_world_env.py`; [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout).
Claim IDs or none: [EPI-CLM-self-evolution](#epi-clm-self-evolution).
Mismatch marker or none: reuse signal is not a call trace or causal component test.
Gap/limit: no supplied trace shows whether this proxy was exploited or useful.

Route ID: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout), [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model).
Content/update relation: non-truth-apt policy/content update: numerical optimization from rewards or supervised token targets.
Transition or check target: shaped scores/advantages or selected labels to parameter updates.
Evaluator/condition and domain: see records; optimization is not semantic acceptance of propositions stored in weights.
Activation and timing: see records; SFT and RL are separately launched and operator-linked.
Possible or observed result: changed weights/checkpoints if configured computation executes.
Implemented force: numerical behavior determination in later inference, not merely advice.
Epistemic authority and scope: no identified truth claim gains warrant just because its tokens were rewarded or trained.
Operational authority: behavior permitted, blocked, or changed: future action probabilities may change.
Behavioral-authority path: see [RT-BAP-policy-weights](runtime.md#rt-bap-policy-weights).
Evidence source ID and local anchor: see records.
Claim IDs or none: [EPI-CLM-self-evolution](#epi-clm-self-evolution).
Mismatch marker or none: update wiring is not observed learning or successful self-improvement.
Gap/limit: no exact weights, downstream causal dependence or controlled outcome comparison.

Route ID: [EPI-RTE-api-prediction](#epi-rte-api-prediction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-predicted-apis](#epi-obj-predicted-apis).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: task/API descriptions and demonstrations to proposed relevant API names.
Evaluator/condition and domain: model proposal; see record.
Activation and timing: first step of registered reflexion alternative.
Possible or observed result: predicted relevance list; actual output not supplied.
Implemented force: candidate generation followed by membership filter and document selection.
Epistemic authority and scope: descriptions do not by themselves prove predicted relevance; no particular output establishes non-entailment or correct inference here.
Operational authority: behavior permitted, blocked, or changed: can determine which API documentation is supplied to code generation.
Behavioral-authority path: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: API-name validity is not task-relevance validity.
Gap/limit: semantic relation remains indeterminate, rather than inferring ampliation from model use alone.

Route ID: [EPI-RTE-api-prediction](#epi-rte-api-prediction)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-predicted-apis](#epi-obj-predicted-apis).
Content/update relation: no content change.
Transition or check target: model lines to permitted documented API names.
Evaluator/condition and domain: case-normalized membership in `allowed_apis`, cap and deduplication; supervisor APIs supplied independently.
Activation and timing: see record.
Possible or observed result: documented-name list, even if no relevant model prediction survives.
Implemented force: enforcing list filter; relevance unchecked.
Epistemic authority and scope: namespace membership only.
Operational authority: behavior permitted, blocked, or changed: downstream documentation selection accepts surviving names.
Behavioral-authority path: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: no relevance oracle in the filter.
Gap/limit: external demonstration labels are imported, not independent evaluation of this prediction.

Route ID: [EPI-RTE-code-retrial](#epi-rte-code-retrial)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: generated full Python solution, execution output and retrial prompt; see record.
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: execution feedback to next candidate solution.
Evaluator/condition and domain: language model interprets stacktrace plus configured retrial prompt; external execution produces observations, not a checked general explanation.
Activation and timing: third and later steps; see record.
Possible or observed result: replacement executable code.
Implemented force: next attempted execution via base agent.
Epistemic authority and scope: establishes feedback-fed proposal route, not observed correction or formulated blame assignment.
Operational authority: behavior permitted, blocked, or changed: model output is sent for execution subject to base limits.
Behavioral-authority path: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: route name `reflexion` does not establish content-directed criticism or learning.
Gap/limit: prompt files are constructor-supplied; no selected execution or response establishes what criticism occurred.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-function-rules](runtime.md#rt-clm-function-rules) | see record | see record | Prompt requests reuse and self-contained functions | [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [EPI-RTE-function-extraction](#epi-rte-function-extraction) | none supplied | No independent intervention on reuse; extraction and string gates do not enforce specification | Reuse opportunity and operational code admission are wired | General correctness, self-containment and useful reuse remain unestablished |
| [EPI-CLM-self-evolution](#epi-clm-self-evolution) | see record | see record | Algorithm framing and claimed expert/SFT setup | [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission) | none supplied | No training comparison or component variation; reward proxy and selection are bundled | Improvement-directed policy change is implemented; selected benchmark-successful traces can feed supervision | Successful improvement, optimal performance and causal skill-library benefit unknown |

## Bounded conclusion

SAGE implements several distinct authority paths. Paired libraries and evaluation records retain executable candidates; retrieval controls their installation and prompt delivery. This gives code operational authority before any general input/output correctness acceptance. Installation checks, syntax extraction, namespace filtering and similarity ranks have narrower domains than skill correctness. Task/API context and demonstration solutions are acquired with unknown source warrant, not produced or independently authenticated by SAGE ([RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [EPI-RTE-api-prediction](#epi-rte-api-prediction)).

The inspected extractor is not a semantics-preserving transformation for arbitrary valid programs: omitted globals and multi-line source slicing can break retained definitions. Actual candidate semantics remain indeterminate without generated artifacts. Arithmetic on test counts derives a task-success predicate only within the external benchmark's domain. Neither that predicate nor the reuse substring count validates a general mechanism, safe replay or transfer ([EPI-RTE-function-extraction](#epi-rte-function-extraction), [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout)).

Expert admission is the significant countercase to a blanket claim that SAGE never consumes evidence for acceptance: benchmark success, first-task extraction and verification-execution criteria gate trajectory progression for training-data use. This is scoped acceptance of trajectories, not acceptance of all reusable function claims. Later dataset normalization and label masking delimit what reaches training. Retention and operational reuse elsewhere do not become lifecycle integration merely by occurring later; no inspected route establishes generalized function claims accepted against their specifications and then integrated as warranted knowledge ([RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)). This is a bounded finding about the inspected routes, not an exhaustive whole-repository negative.

RL directly changes behavior-determining numerical state from outcome and reuse signals. The independently stated objective is task success with reusable skills; later inference/checkpoint consumption is wired. Subsequent operation causally depending on a particular update is not supplied, so exercised self-improvement and successful learning remain unestablished. This does not negate the improvement-directed architectural pathway. SFT is a separate parameter-change path with an operator-supplied bridge to RL. No identifiable proposition in weights is shown true or accepted by either optimizer ([RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission), [RT-BAP-policy-weights](runtime.md#rt-bap-policy-weights)).

The additional registered reflexion branch implements observation-fed candidate revision and API-context selection. It prevents equating the target with only its default skill-library agent, but its name proves neither formulated criticism nor beneficial reflection. No actual model criticism, blamed assumption or retained revision rationale is available to assess theory-builder conditions across that branch. Computational proposal, gating and retry can be described independently of reliability, autonomy of every internal operation, or learning. No single epistemic score or system-wide verdict follows ([EPI-RTE-code-retrial](#epi-rte-code-retrial), [EPI-RTE-api-prediction](#epi-rte-api-prediction)).

## Shared records

### Operative objects

#### EPI-OBJ-predicted-apis
Label: Predicted APIs

Source-native identity: `predicted_apis`, normalized API-name strings. Representational form: symbolic namespace members; their proposed relevance is interpreted by the model and documentation selector. Substrate: process list and rendered prompt context. Distinct from executable function records in [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions): names select documentation, rather than define retained skills. No counterpart after comparison with the supplied runtime objects. SRC-1, implementation, `patches/appworld/experiments/code/skill_library_agent/api_predictor.py` and `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`.

> predicted_apis = unique(predicted_apis)
> return predicted_apis, output["cost"]
> --- `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`

### Routes

#### EPI-RTE-function-extraction
Label: Function source extraction
Part of: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)

This declares the extraction transformation inside the supplied combined extraction/install route, not a second identity for the whole route. Model-produced source enters `_extract_functions_from_code`; AST parsing and line selection return named imports/functions to the dictionary writer. Owner: batch environment. Context: first-subtask Python and execution output. Actions: parse, select top-level imports/functions, omit other top-level statements. The evaluation helper has the same inspected slicing algorithm, but its storage/disposition is separately owned by [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop). SRC-1 implementation, `sage/llm_agent/app_world/app_world_env.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

Deterministic source deduction, not target execution: for input `x = 2\ndef f():\n    return x`, only the FunctionDef slice is returned, without `x = 2`; a fresh world need not bind `x`. Even retaining a function verbatim therefore does not preserve the original program's input/output meaning. For input `def f():\n    return """a\nb"""`, AST node starting lines stop at line two, so the inspected maximum-`lineno` end slice omits the closing string line. These cases refute universal semantic preservation and universal self-containment. They do not establish that any supplied run generated these examples. A simple `def f():\n    return 2` is a preservation countercase against claiming extraction always damages semantics. The classification of unspecified real candidates remains indeterminate between non-ampliative reshaping, valid derivation and changed/unsupported content; candidate source and checked interpretation would be needed to decide.

- Immediate return: function source list and name list.
- Later read-back: extracted values can be installed in the paired second task through the parent route.
- Delegated visibility: matching pair's selected source only; omitted bindings are not delivered through this channel.
- Selection predicate: AST top-level Import/ImportFrom lines and FunctionDef nodes after the parent's output gate.
- Invalidation or expiry: parse failure skips extraction; parent handles same-name overwrite and per-rollout expiry.
- Activation or effect: extraction and subsequent dictionary insertion are wired; actual useful invocation unobserved.
- Evidence limits: no generated instance or semantic validation supplied; AST syntax is not a function-specification check.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The model proposes; software slicing decides inclusion with parse-error veto. No human content approval or reference oracle is present in this part. The parent retains prompt guidance and recovery responsibilities; this transformation does not independently admit validated capabilities.

> if isinstance(node, ast.FunctionDef):
>     function_names.append(node.name)
>     start_lineno = node.lineno - 1
>     end_lineno = max(
>         n.lineno for n in ast.walk(node) if hasattr(n, 'lineno')
>     )
>     func_code = "\n".join(import_lines + lines[start_lineno:end_lineno])
>     function_bodies.append(func_code)
> --- `sage/llm_agent/app_world/app_world_env.py`

#### EPI-RTE-api-prediction
Label: API prediction filtering

Distinct route from [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop): the registered full-code-reflexion alternative calls APIPredictor before full-code generation. It does not retain or install skill definitions. Endpoints: task descriptions plus ground-truth-labeled demonstrations → language-model response → normalized allowed-name filter/cap/deduplication → `predicted_apis` → selected API docs. Owners: APIPredictor and reflexion agent. Context: external task metadata, configured prompt and demo tasks. Actions: interpreted relevance proposal, symbolic membership filtering and context restriction. SRC-1 implementation, `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`, `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`.

The model proposes; software can veto unknown names, but no human or expected-relevance oracle judges this task's proposed subset. Demonstration labels are context, not a test result for the current prediction. Operating mode: bounded task-solving alternative. Consumer: full-code generator; channel: selected documentation and required-API list; force: enforcing documentation selection plus interpreted guidance; horizon: current task. Namespace admission permits context use, not epistemic acceptance of necessity/sufficiency. Recovery is later code-generation feedback under the companion route, not an inspected relevance-specific rollback.

Model component overlaps [RT-CMP-language-model](runtime.md#rt-cmp-language-model): same LiteLLMGenerator mechanism, separately constructor-configured predictor instance. Its actual model version and weights are unpinned here; no parameter update is implemented by prediction. A provider endpoint can resolve to other weights; internals and actual response are uninspected. This is not evidence of identical actual models across configurations.

- Immediate return: selected API-name list and call cost.
- Later read-back: inapplicable — prediction is current-task state, not accumulated experience retained through use.
- Delegated visibility: model receives task descriptions/demonstrations; full-code stage receives filtered names and selected docs, not an independently validated relevance explanation.
- Selection predicate: documented namespace membership, max predicted count, supervisor API inclusion, deduplication.
- Invalidation or expiry: prediction overwritten for another task; unsupported names omitted, no relevance-based withdrawal found in this inspected method.
- Activation or effect: returned names are wired to documentation selection; successful task effect unobserved.
- Evidence limits: constructor-supplied prompts and external demo/task artifacts are not frozen instances; no achieved prediction accuracy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if line.strip() and line.strip().lower() in allowed_apis
> --- `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`

> to_demo_apis = set(self.predicted_apis)
> for task_ in self.demo_tasks:
>     to_demo_apis = to_demo_apis | set(task_.ground_truth.required_apis)
> --- `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`

#### EPI-RTE-code-retrial
Label: Full code retrial

Distinct from [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)'s skill-agent proposal method: `SimplifiedFullCodeReflexionAgent` is registered as `simplified_full_code_reflexion`, uses API prediction and demonstration solutions, then supplies execution output plus configured retrial text to later model calls. The base solve/evaluate loop remains shared. Endpoints: API-selected context/demonstrations → generated full code → base execution → output/retrial prompt → next full code. Owners: subclass for messages/proposal, base Agent for world execution and limits. Context/state: current-task messages, selected API documentation, demo compiled solutions, last execution output. Model output is stripped of code-block formatting and sent as ExecutionIO. SRC-1 implementation, `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`.

Trigger: step three onward; max steps capped by configured retrials plus two. Model proposes the replacement; base controller enforces completion/cost/step stop, not a per-proposal correctness approval. Oracle: external task evaluation as in the base route, separate from the stacktrace supplied during retry. No human per-candidate veto is implemented. Guidance is the constructor-supplied code/retrial prompts and imported ground-truth demos; actual prompt contents and responses are not evidenced here. What remains is current-task messages and ordinary logs, not an inspected durable method revision. Recovery attempts another code generation; transaction rollback of prior world effects is not established. Model identity/mutability limits are the same configured adapter limits described in [RT-CMP-language-model](runtime.md#rt-cmp-language-model), not evidence of a particular provider invocation.

- Immediate return: next executable code and cost to base controller.
- Later read-back: inapplicable — this inspected retry loop accumulates ordinary current-task messages; no new persistent theory or skill store is established by the subclass.
- Delegated visibility: code model sees selected docs, demos, task and execution feedback; it does not receive a benchmark reference answer for each retry.
- Selection predicate: step number chooses API prediction, initial code or feedback-fed code; base max-step/cost/completion predicates stop execution.
- Invalidation or expiry: initialize resets base task context; generated code replaces the next attempted action, not an established world rollback.
- Activation or effect: feedback is wired into model requests and returned code into execution; observed revision quality unavailable.
- Evidence limits: no actual criticism, named blamed premise, successful repair, retained critique or causal benefit is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> stacktrace = last_execution_outputs[0].content
> content = stacktrace + "\n\n" + self.retrial_prompt
> self.messages.append({"role": "user", "content": content})
> --- `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`

> self.max_steps = min(self.max_steps, max_num_retrials + 2)
> --- `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`

### Claims

#### EPI-CLM-self-evolution
Label: Self evolution framing

Claimed operation: README frames SAGE as Skill Augmented GRPO for self-Evolution, combining sequential rollout and skill-integrated reward; it also describes expert generation and SFT as required for optimal AppWorld performance. This is doctrine/design and attributed setup, not frozen performance evidence. Distinct from [RT-CLM-function-rules](runtime.md#rt-clm-function-rules), which governs desired function content rather than training improvement. SRC-1 `README.md`.

> The figure below illustrates the Skill Library Agent and **Sequential Rollout with Skill-integrated Reward**, a core component of SAGE on which GRPO is applied.
> --- `README.md`

> To reach the optimal performance on AppWorld, Supervised Fine-tuning (SFT) with expert experience dataset generation is still required. Thus, here we also provide the data generation pipeline and SFT code for reference.
> --- `README.md`
