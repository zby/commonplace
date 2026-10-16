---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Reflexion's task-local evidence, correctness labels and unchecked reflection guidance at the frozen revision."
run-id: AAS-2026-10-14-reflexion-19159b69b712-01
reviewed-boundary: "218cf0ef1df84b05ce379dd4a8e47f17766733a0"
---

# Reflexion epistemic report

## Source-and-claim boundary

The question is how the four shipped task workflows acquire candidate content, evaluate it, license reliance and influence later attempts. Scope and dependency exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and layers are see [Source register](boundary.md#source-register). Evidence is SRC-1 implementation and attributed doctrine/design. No target execution, saved result examination or causal experiment was performed. Neither benefit nor exercised learning follows from source wiring.

The public claims assessed are [RT-CLM-persisting-memory](runtime.md#rt-clm-persisting-memory) and [EPI-CLM-strategy-guidance](#epi-clm-strategy-guidance). They concern retention and later guidance rather than acceptance of universally correct explanations. The title's verbal reinforcement learning terminology is not treated as an independent result or a weight-training contract.

| Entry point or operation | Source path | Coverage and limits |
|---|---|---|
| Programming CLI and six strategies | SRC-1 `programming_runs/main.py` | Direct dispatch read; supplied [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt), [RT-RTE-program-variants](runtime.md#rt-rte-program-variants). Missing UCS import and test-accuracy mismatch limit launchability. |
| Program generation, test filtering, diagnosis | SRC-1 `programming_runs/generators/generator_utils.py` | Prior direct complete helper read; correction directly inspected Python/Rust `internal_tests`, their predicates and `func_impl` callers; [EPI-RTE-test-filter](#epi-rte-test-filter). SRC-1 `programming_runs/generators/py_generate.py`, `programming_runs/generators/rs_generate.py`. Other prompt details not independently exhaustive; Rust generation call omits required argument. |
| Local Python and Rust checks, cleanup | SRC-1 `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py` | Direct complete reads; supplied [RT-RTE-code-execution](runtime.md#rt-rte-code-execution). Host execution is not containment or general correctness. |
| Offline Python/Rust result validation | SRC-1 `programming_runs/validate_py_results.py`, `programming_runs/validate_rs_results.py` | Direct complete reads; [EPI-RTE-result-audit](#epi-rte-result-audit). Console result has no persisted withdrawal consumer. |
| Offline LeetCode evaluation | SRC-1 `programming_runs/evaluate_leet_results.py`, `programming_runs/evaluate_rs_leet_results.py` | Direct reads; [EPI-RTE-leet-audit](#epi-rte-leet-audit). Rust-named file empty; other script defective and dependency absent. Remote judgment unknown. |
| HotPotQA notebooks, alternate environment | SRC-1 `hotpotqa_runs/notebooks/`, `hotpotqa_runs/react.py`, `hotpotqa_runs/environment.py` | Supplied [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt); no notebook outputs used. |
| HotPotQA main agents, retrieval, EM and reflection prompts | SRC-1 `hotpotqa_runs/agents.py`, `hotpotqa_runs/prompts.py` | Direct complete reads; [EPI-RTE-answer-normalize](#epi-rte-answer-normalize). Wikipedia/provider internals excluded. |
| ALFWorld trial, reflection, persistence and resume | SRC-1 `alfworld_runs/main.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/env_history.py` | Supplied [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial), not new direct reads. Environment semantics unknown. |
| WebShop HTTP client, trial, reflection and resume | SRC-1 `webshop_runs/main.py`, `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`, `webshop_runs/env_history.py` | Supplied [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial), not new direct reads. Server grading unknown; plans omitted from action prompt. |
| Other included evidence | SRC-1 `programming_runs/human-eval/`, `programming_runs/generate_dataset.py`, `programming_runs/benchmarks/`, task datasets and stored results | Available but uninspected here. Prevents a complete audit of test provenance, dataset transformations, observed performance and every auxiliary evaluation path. |

This is not a system-complete negative about acceptance or knowledge production. Missing search/evaluation dependencies prevent full UCS/LeetCode routes; inaccessible provider weights prevent assessment of internal factual warrant and parameter adaptation. Uninspected logs prevent operation and outcome conclusions, not architectural conclusions. Supplied runtime findings are used as provisional, cited evidence containers, not a restriction on direct inspection. Newly inspected offline evaluators add coverage rather than superseding valid runtime containers.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl) | Code is operational; the proposition that it satisfies a specification is truth-apt | see cited record | SRC-1 `programming_runs/reflexion.py` | Execution and text-guidance consumers differ; persisted solution may fail reference tests. |
| [EPI-OBJ-internal-tests](#epi-obj-internal-tests) | Assertions predict outputs of specified calls | Provisional test expectations | SRC-1 `programming_runs/generators/generator_utils.py` | Python syntax validity does not validate expected answers; Rust's predicate accepts every parsed fragment without syntax validation. |
| [EPI-OBJ-test-feedback](#epi-obj-test-feedback) | Recorded pass/fail and output claims about candidate/test pairs | Evidence for revision and host branching | SRC-1 `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py` | Wrapper/parser/timeouts bound interpretation; external reference tests not authenticated. |
| [EPI-OBJ-qa-content](#epi-obj-qa-content) | Retrieved/dataset paragraphs, proposed answer and recorded match to key | Answer evidence, candidate and outcome respectively | SRC-1 `hotpotqa_runs/agents.py` | These are separate parts of the cited container; imported content has unknown source warrant, key match is not a fact proof. |
| [EPI-OBJ-program-reflection](#epi-obj-program-reflection) | Requested causal diagnosis, if produced; actual truth-apt instance not determinable | Hint for successor code | SRC-1 `programming_runs/generators/generator_utils.py` | Requested explanation is not observed explanation or validated cause. |
| [EPI-OBJ-qa-reflections](#epi-obj-qa-reflections) | Possible failure explanation mixed with non-truth-apt future plan; actual instance not determinable | Same-question guidance | SRC-1 `hotpotqa_runs/agents.py`, `hotpotqa_runs/prompts.py` | Last-attempt strategy retains trace rather than newly produced diagnosis. |
| [EPI-OBJ-alfworld-state](#epi-obj-alfworld-state) | Observations/outcome claims and requested mistake diagnoses; plans are directives | Trial evidence, success flag and future-task guidance | SRC-1 `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py` | `done` is consumed instead of `won`; stored plan quality unknown. |
| [EPI-OBJ-webshop-state](#epi-obj-webshop-state) | Page observations, server reward and requested diagnosis; plans are directives | Trial evidence, success flag and reflection context | SRC-1 `webshop_runs/webshop_trial.py` | HTML filtering and opaque server grading limit warrant; plans do not reach action caller. |
| [RT-CMP-gpt4](runtime.md#rt-cmp-gpt4), [RT-CMP-gpt35](runtime.md#rt-cmp-gpt35), [RT-CMP-text-davinci](runtime.md#rt-cmp-text-davinci), [RT-CMP-star-chat](runtime.md#rt-cmp-star-chat), [RT-CMP-code-llama](runtime.md#rt-cmp-code-llama) | not determinable from accessible weights/interfaces | see cited component records | SRC-1 `programming_runs/generators/model.py`, `hotpotqa_runs/llm.py`, `alfworld_runs/utils.py`, `webshop_runs/utils.py` | Distributed-parametric content inaccessible; client generation is not inspected training; aliases/loading revisions unpinned. |

## Authority-route ledger

Each compact row below separates checks from dispositions and retention from integration. A supplied route can implement several functions; the local split does not change its identity. Record-owned progression, return and read-back fields are see the cited declaration.

Route ID: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl), [EPI-OBJ-program-reflection](#epi-obj-program-reflection)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: task specification/feedback to candidate code and requested failure explanation.
Evaluator/condition and domain: model generation, not an evidence-consuming acceptance procedure. Actual explanation could merely restate an error or propose a non-entailed cause; outputs needed to distinguish.
Activation and timing: initial and failure-driven successor calls; see cited route.
Possible or observed result: candidate code and hint, operation unobserved.
Implemented force: code replacement and delivery of hint before another check.
Epistemic authority and scope: candidate only, no warrant for explanation or general specification satisfaction.
Operational authority: new candidate executed; hint can guide generator.
Behavioral-authority path: generator text channel advisory within task; executor channel executable for current evaluation, see [RT-BAP-executable-code](runtime.md#rt-bap-executable-code).
Evidence source ID and local anchor: SRC-1 `programming_runs/reflexion.py`, `programming_runs/generators/generator_utils.py`; see cited records and quotations below.
Claim IDs: none
Mismatch marker: none
Gap/limit: code is also a non-truth-apt operational update; no model compliance or improved program observed. This wiring describes ordinary Python generation, not complete Rust progression: SRC-1 `programming_runs/generators/rs_generate.py` omits required `code_block_instruction` when calling `generic_generate_func_impl` in `programming_runs/generators/generator_utils.py`; see the test-filter record's retained caller evidence.

Route ID: [EPI-RTE-test-filter](#epi-rte-test-filter)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-internal-tests](#epi-obj-internal-tests)
Content/update relation: no content change
Transition or check target: Python parsed assertions' syntax; Rust parsed fragments' membership only, not syntax or expected-output truth.
Evaluator/condition and domain: Python `py_is_syntax_valid` uses `ast.parse`; Rust supplies `lambda x: True` to the same helper.
Activation and timing: after generation/parsing, before sampling/execution.
Possible or observed result: Python syntax-eligible subset; every Rust fragment remains eligible for sampling.
Implemented force: Python parse failures removed; Rust predicate rejects nothing.
Epistemic authority and scope: Python parseability only; no Rust syntax license or semantic expected-value license in either branch.
Operational authority: selected assertions become test oracles for internal branching.
Behavioral-authority path: generator list to executor, enforcing membership for this pass; sampling then limits coverage.
Evidence source ID and local anchor: SRC-1 `programming_runs/generators/generator_utils.py`, `programming_runs/generators/py_generate.py`, `programming_runs/generators/rs_generate.py`; see declaration.
Claim IDs: none
Mismatch marker: Python syntax eligibility is not semantic test acceptance; Rust predicate supplies neither check.
Gap/limit: empty Python subset possible; Rust split can retain malformed fragments; no evidence expected values were independently checked.

Route ID: [RT-RTE-code-execution](runtime.md#rt-rte-code-execution)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-test-feedback](#epi-obj-test-feedback)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Python candidate against generated assertions or reference `check`; Rust candidate against generated/reference assertions.
Evaluator/condition and domain: Python exception/no exception within wrapper; Rust compiler JSON and stderr recognizer. Source warrant unknown for model-authored expectations; supplied benchmark authority conditional on valid tests. Runtime measurements are wrapper-bounded.
Activation and timing: generated candidate executed before correctness judgment; internal and reference calls separate.
Possible or observed result: Boolean, per-test states and textual output/errors; operation unobserved.
Implemented force: result returned to caller, not yet acceptance.
Epistemic authority and scope: observed wrapper outcome for specified code/test run if exercised; not all-input correctness, isolation, explanation or transfer.
Operational authority: caller receives branching/ranking evidence.
Behavioral-authority path: executor result to selected strategy, informational then enforcing through separate branch.
Evidence source ID and local anchor: SRC-1 `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py`; see cited route and feedback record.
Claim IDs: none
Mismatch marker: outcome label narrower than correctness
Gap/limit: empty Python tests yield initial pass; timeout does not kill thread; Rust lacks general return-code check; remote LeetCode semantics unavailable.

Route ID: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl)
Content/update relation: no content change
Transition or check target: correctness label of current candidate for benchmark task.
Evaluator/condition and domain: host consumes reference evaluator Boolean after internal pass or final permitted iteration.
Activation and timing: see cited route.
Possible or observed result: `is_solved` true/false; initial internal pass can exit even on reference failure.
Implemented force: sets label and success count, can terminate pass loop.
Epistemic authority and scope: criterion is passing supplied reference tests, intended use benchmark success classification, scope that task/evaluator. Not proof of complete specification.
Operational authority: reject success label, not execution or final persistence; reference rejection need not trigger another diagnosis.
Behavioral-authority path: strategy Boolean branch enforcing immediate scheduling and logged label.
Evidence source ID and local anchor: SRC-1 `programming_runs/reflexion.py`; see cited route.
Claim IDs: none
Mismatch marker: persisted output is not accepted correctness
Gap/limit: no successful execution observed; no accepted explanatory claim follows from program pass.

Route ID: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl), [EPI-OBJ-program-reflection](#epi-obj-program-reflection), [EPI-OBJ-test-feedback](#epi-obj-test-feedback)
Content/update relation: no content change
Transition or check target: task-local state and final JSONL, without correctness prerequisite.
Evaluator/condition and domain: host append at task completion; see cited route.
Activation and timing: rounds and final write.
Possible or observed result: code, hint and feedback retained.
Implemented force: next generation receives current values; resume counts rows rather than restoring hints.
Epistemic authority and scope: retention does not endorse hint or failed final code.
Operational authority: hints advisory for next generation; row count suppresses processed tasks.
Behavioral-authority path: model context within task; result file to resume selector on subsequent invocation.
Evidence source ID and local anchor: SRC-1 `programming_runs/reflexion.py`, `programming_runs/utils.py`; see cited route.
Claim IDs: none
Mismatch marker: none
Gap/limit: this is not lifecycle integration of an accepted diagnosis.

Route ID: [RT-RTE-program-variants](runtime.md#rt-rte-program-variants)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl), [EPI-OBJ-program-reflection](#epi-obj-program-reflection)
Content/update relation: non-truth-apt policy/content update: candidate replacement or ranking
Transition or check target: simple/direct evaluation; immediate-reflexion revisions with omitted test feedback; immediate-refinement using feedback without generated reflection; UCS callback costs and final selection.
Evaluator/condition and domain: see cited route for separate strategy predicates/oracles. UCS cost counts generated test failures, not factual diagnosis quality.
Activation and timing: selected CLI strategy; external UCS scheduler uninspected.
Possible or observed result: replacements, ranked candidates and benchmark labels.
Implemented force: callbacks and local branches; full UCS force not determinable.
Epistemic authority and scope: same task-local evaluator bounds; omitted feedback grants no execution evidence to immediate diagnosis.
Operational authority: permit successor generation or select code.
Behavioral-authority path: local driver model context advisory; costs to missing search implementation ranking with unknown horizon.
Evidence source ID and local anchor: SRC-1 `programming_runs/immediate_reflexion.py`, `programming_runs/immediate_refinement.py`, `programming_runs/reflexion_ucs.py`, `programming_runs/test_acc.py`; see cited route.
Claim IDs: none
Mismatch marker: no common evidence rule across variants
Gap/limit: UCS selected/evaluated code can differ from logged solution; intended test-accuracy dispatch mismatches arguments. The Rust generation caller also omits required `code_block_instruction`, so complete Rust variant-generation wiring is not established. Independently callable Rust executors/auditors remain supported. This grouped overview does not assert equivalent warrant or launchability among languages or variants.

Route ID: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-content](#epi-obj-qa-content)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: dataset supporting paragraphs or Wikipedia Search/Lookup response enters context.
Evaluator/condition and domain: annotation selection or external docstore lookup; no factual verification gate shown.
Activation and timing: notebook context assembly or model-requested lookup during attempt.
Possible or observed result: source text in scratchpad/context.
Implemented force: available as evidence to answer model.
Epistemic authority and scope: source warrant unknown; presence is not endorsement. Line-removing formatting can merge text boundaries.
Operational authority: answer generation may use imported text.
Behavioral-authority path: docstore/context to model, informational/advisory, current attempt.
Evidence source ID and local anchor: SRC-1 `hotpotqa_runs/agents.py`; see cited route.
Claim IDs: none
Mismatch marker: none
Gap/limit: source identity/content not authenticated here; no observed retrieval or factual correctness.

Route ID: [EPI-RTE-answer-normalize](#epi-rte-answer-normalize)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-content](#epi-obj-qa-content)
Content/update relation: non-truth-apt policy/content update: comparison-key normalization
Transition or check target: answer/key strings to comparison representations.
Evaluator/condition and domain: fixed lowercasing, punctuation/article removal and whitespace collapse.
Activation and timing: every EM call before equality.
Possible or observed result: distinct strings collide; deterministic deduction in declaration.
Implemented force: defines equality domain, does not replace displayed answer.
Epistemic authority and scope: no semantic-equivalence license; transformation may discard distinguishing information.
Operational authority: normalized values govern correctness branch.
Behavioral-authority path: comparison strings to EM Boolean, enforcing next check's criterion for this answer.
Evidence source ID and local anchor: SRC-1 `hotpotqa_runs/agents.py`; see declaration.
Claim IDs: none
Mismatch marker: normalized equality is not unrestricted answer truth
Gap/limit: no target execution required for code-derived trace.

Route ID: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-content](#epi-obj-qa-content)
Content/update relation: no content change
Transition or check target: proposed answer compared to supplied key after normalization.
Evaluator/condition and domain: deterministic EM, not model judgment of factual truth.
Activation and timing: Finish/is_correct and notebook retry checks.
Possible or observed result: equal/unequal.
Implemented force: Boolean returned; downstream disposition separate.
Epistemic authority and scope: normalized string match to that key only.
Operational authority: informs result text, stop/retry predicate.
Behavioral-authority path: EM to agent/notebook, enforcing through downstream branch, same-question rounds.
Evidence source ID and local anchor: SRC-1 `hotpotqa_runs/agents.py`, `hotpotqa_runs/environment.py`; see cited route and normalization record.
Claim IDs: none
Mismatch marker: none
Gap/limit: correct synonyms can fail; distinct punctuation-sensitive strings can match; dataset key authority assumed, not verified.

Route ID: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-content](#epi-obj-qa-content)
Content/update relation: no content change
Transition or check target: benchmark answer success and continuation.
Evaluator/condition and domain: host consumes EM result; intended use question success classification, scope sampled dataset/key.
Activation and timing: Finish records outcome; notebook excludes correct agents from future rounds.
Possible or observed result: accepted match label or failure/retry eligibility.
Implemented force: outcome scratchpad and skip predicate.
Epistemic authority and scope: criterion-bounded acceptance of answer label only, not reasoning/diagnosis.
Operational authority: success blocks further attempts; failure can permit reflection.
Behavioral-authority path: agent outcome and notebook predicate enforcing subsequent rounds for same question.
Evidence source ID and local anchor: SRC-1 `hotpotqa_runs/agents.py`; see cited route.
Claim IDs: none
Mismatch marker: none
Gap/limit: no accepted explanatory claim or general fact incorporation established.

Route ID: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-reflections](#epi-obj-qa-reflections)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: failed trace to requested possible diagnosis and high-level plan.
Evaluator/condition and domain: model; directive explicitly admits possible phrasing discrepancy. No distinct diagnosis evaluator.
Activation and timing: incorrect previous attempt; strategy selects new reflection versus old trace.
Possible or observed result: generated text; no actual instance inspected.
Implemented force: text available for retention without acceptance check.
Epistemic authority and scope: conjectural role requested; neither actual non-entailment nor factual adequacy of output established.
Operational authority: plan may influence next answer call.
Behavioral-authority path: see [RT-BAP-plan-guidance](runtime.md#rt-bap-plan-guidance), advisory same-question attempts.
Evidence source ID and local anchor: SRC-1 `hotpotqa_runs/prompts.py`, `hotpotqa_runs/agents.py`; see cited route and object declaration.
Claim IDs: [EPI-CLM-strategy-guidance](#epi-clm-strategy-guidance)
Mismatch marker: requested diagnosis is not checked explanation
Gap/limit: directive portions are non-truth-apt plans; old trace strategy is retention rather than new diagnosis.

Route ID: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-reflections](#epi-obj-qa-reflections)
Content/update relation: no content change
Transition or check target: append reflection, replace trace or replace combined reflection list by strategy.
Evaluator/condition and domain: software strategy rule, no per-content human/semantic approval.
Activation and timing: before reset; serialization after round per supplied route.
Possible or observed result: material preserved for subsequent calls.
Implemented force: stored reflection string inserted into next model prompt.
Epistemic authority and scope: operational guidance, no truth license.
Operational authority: influences model input, not guaranteed answer choices.
Behavioral-authority path: see [RT-BAP-plan-guidance](runtime.md#rt-bap-plan-guidance); serialized agents lack inspected reload invocation.
Evidence source ID and local anchor: SRC-1 `hotpotqa_runs/agents.py`, `hotpotqa_runs/util.py`; see cited route.
Claim IDs: [EPI-CLM-strategy-guidance](#epi-clm-strategy-guidance)
Mismatch marker: retention/use is not lifecycle integration
Gap/limit: trimming deletes selected observations; provenance context can be lost without a summary or new warrant.

Route ID: [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-alfworld-state](#epi-obj-alfworld-state)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: environment completion signal to task-success flag.
Evaluator/condition and domain: host consumes external `done`, although `won` is read separately.
Activation and timing: after action step.
Possible or observed result: success on done; false on exhaustion/budget.
Implemented force: success flag suppresses later attempts and reflection updates.
Epistemic authority and scope: only completion as reported by environment; equivalence to objective success requires unavailable environment contract.
Operational authority: stop current and later trials for configuration.
Behavioral-authority path: environment to trial return/config selector, enforcing current and future same-task trials.
Evidence source ID and local anchor: SRC-1 `alfworld_runs/alfworld_trial.py`; see cited route.
Claim IDs: none
Mismatch marker: done versus won
Gap/limit: cannot certify goal attainment; external outcome source warrant unknown.

Route ID: [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-alfworld-state](#epi-obj-alfworld-state)
Content/update relation: no content change
Transition or check target: failed-task generated plans to indexed memory/config snapshots.
Evaluator/condition and domain: failure/not-skip flags; generated diagnosis content uninspected, no independent adequacy gate.
Activation and timing: optional update after whole trial.
Possible or observed result: append plan, retain success flag and serialize; resume restores state.
Implemented force: last three plans delivered to action model next trial.
Epistemic authority and scope: no acceptance of causal claim; plan is task-local guidance.
Operational authority: next action input changed, not executable permission or assured compliance.
Behavioral-authority path: see [RT-BAP-plan-guidance](runtime.md#rt-bap-plan-guidance), advisory later same-index trials/resume.
Evidence source ID and local anchor: SRC-1 `alfworld_runs/generate_reflections.py`, `alfworld_runs/env_history.py`; see cited route.
Claim IDs: [RT-CLM-persisting-memory](runtime.md#rt-clm-persisting-memory)
Mismatch marker: none
Gap/limit: production of truth-apt explanation not determinable without outputs; requested plan-generation relation indeterminate, not proved ampliative. Index alignment external.

Route ID: [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-webshop-state](#epi-obj-webshop-state)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: terminal server reward to task-success flag.
Evaluator/condition and domain: host equality to 1.0 at terminal page; criterion full server reward, intended use task-success classification, scope fixed shopping session.
Activation and timing: after client action/HTTP response.
Possible or observed result: success or failure.
Implemented force: trial return and later skip flag.
Epistemic authority and scope: server-scored success only; source warrant unknown, grading semantics unavailable.
Operational authority: terminate attempt and suppress later successful-task trials.
Behavioral-authority path: client reward to host config selector, enforcing current and later fixed-session trials.
Evidence source ID and local anchor: SRC-1 `webshop_runs/webshop_trial.py`; see cited route.
Claim IDs: none
Mismatch marker: none
Gap/limit: no correctness of server or shopping explanation established.

Route ID: [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-webshop-state](#epi-obj-webshop-state)
Content/update relation: no content change
Transition or check target: failure-generated plans into config/history and future reflection query.
Evaluator/condition and domain: optional failure update; no semantic gate.
Activation and timing: after trial; resume restores plans.
Possible or observed result: appended memory and logged history.
Implemented force: later reflection producer sees plans; action call uses other prompt string without plans.
Epistemic authority and scope: neither retention nor another reflection call validates diagnosis.
Operational authority: reflection-input guidance only through this retained-plan path; no action-plan delivery.
Behavioral-authority path: history/config to reflection model, advisory next failed-trial update; action consumer absent from this channel.
Evidence source ID and local anchor: SRC-1 `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`; see cited route.
Claim IDs: none
Mismatch marker: history retention not action consumption
Gap/limit: actual diagnosis content and truth relation indeterminate; client action assertions check page-transition eligibility, not factual warrant or server success.

Route ID: [EPI-RTE-result-audit](#epi-rte-result-audit)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl), [EPI-OBJ-test-feedback](#epi-obj-test-feedback)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: logged solved Python/Rust candidate replayed against logged reference test.
Evaluator/condition and domain: Python exec with signal alarm; Rust wrapper evaluate. Only solved rows executed.
Activation and timing: standalone operator invocation after experiment.
Possible or observed result: pass or failed-but-should-have-passed, printed counts.
Implemented force: console report, no log rewrite or automatic withdrawal.
Epistemic authority and scope: bounded replay result under that test and wrapper, not provenance authenticity or all-row reevaluation.
Operational authority: expose inconsistency to operator; no inspected automated candidate/retry consumer.
Behavioral-authority path: script to console, informational, invocation only; future human reliance uninspected.
Evidence source ID and local anchor: SRC-1 `programming_runs/validate_py_results.py`, `programming_runs/validate_rs_results.py`; see declaration.
Claim IDs: none
Mismatch marker: rejection report lacks withdrawal consumer
Gap/limit: no observed replay; Python prepends prompt differently from ordinary evaluator; no general effect rollback.

Route ID: [EPI-RTE-leet-audit](#epi-rte-leet-audit)
Route function: check/evidence production
Architectural status: no route found within boundary
Object/candidate ID: [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: stored implementations submitted to remote grader.
Evaluator/condition and domain: parent script constructs submissions; unavailable formatter/env dependency determines semantics.
Activation and timing: intended standalone invocation; with assertions enabled, no argument length can pass the assertion and index access, even if dependencies become available.
Possible or observed result: intended in-memory status/reward/done/info list; no observed run.
Implemented force: no wired standalone submission consumer; unreachable parent scaffold describes list appends and reset, with no output write.
Epistemic authority and scope: remote verdict not determinable from accessible evidence.
Operational authority: intended submissions and reset only, not wired delivery from this entry point; no inspected correction of retained result.
Behavioral-authority path: intended stored-code submission to remote environment, but argument contradiction blocks delivery before that consumer with assertions enabled; scaffold results would remain in process only.
Evidence source ID and local anchor: SRC-1 `programming_runs/evaluate_leet_results.py`; see declaration.
Claim IDs: none
Mismatch marker: output path unused and argument count inconsistent
Gap/limit: architectural finding concerns the declared standalone stored-implementation audit: executable delivery is not established, rather than parent text being a wired inner route. Parent scaffold is afforded; remote semantics independently remain unknown. See [MEM-RTE-leet-evaluation](memory.md#mem-rte-leet-evaluation); no supersession is asserted to settle an evidence-strength conflict.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-persisting-memory](runtime.md#rt-clm-persisting-memory) | see record | SRC-1 `README.md`, doctrine/design | Explicit ALFWorld parameter description | [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial) | uninspected | No intervention examined | ALFWorld retains and delivers task plans conditionally | Storage does not establish correct explanations or benefit; WebShop not within this claim's explicit ALFWorld scope. |
| [EPI-CLM-strategy-guidance](#epi-clm-strategy-guidance) | see record | SRC-1 `README.md`, `hotpotqa_runs/prompts.py`, doctrine/design | Strategies promise prior material as context and request improvement | [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt) | uninspected | No independent variation or outcome comparison | Context-delivery capacity and improvement-directed instruction implemented | Improvement, semantic use and truth of diagnosis unestablished. |

## Bounded conclusion

The ordinary Python programming route produces and executes candidates, runs generated and reference tests, and records criterion-bounded benchmark labels. Python generated-test filtering establishes parseability only, not expected-output truth. Rust's always-true predicate accepts every parsed fragment for sampling without syntax validation. Its generation caller also omits a required helper argument; language-equivalent end-to-end progression is not established. Reference passing licenses the supplied benchmark classification, not general program correctness or validity of the generated explanation. Internal passing can stop retries even after reference failure; failed final code can persist. The selected Python/Rust console validators provide a countercheck capacity but their failure reports do not rewrite labels or restore prior code. The standalone LeetCode audit is only an afforded scaffold: its contradictory argument handling blocks delivery with assertions enabled, independently of missing dependencies. The unassessed vendored HumanEval subtree prevents a repository-complete conclusion about offline evaluation or result-file writeback.

HotPotQA imports paragraphs and Wikipedia responses with unknown source warrant. It generates answer candidates and compares normalized strings to a supplied key. Its acceptance criterion is that match for benchmark classification on the question. The enforcing path changes outcome labels and later-round selection. Normalization itself has no semantic-equivalence warrant. Retained reflections/last traces enter subsequent calls as advisory context; selective excerpt deletion can remove supporting evidence without validating what remains.

ALFWorld consumes completion, not directly the read `won` signal, to suppress later trials. WebShop consumes terminal full server reward. Both rely on external evaluators whose validity is outside the frozen source. ALFWorld retains plans and delivers a three-plan tail to later action input. WebShop stores plans and supplies them to later reflection production, but its inspected action prompt omits them. This is a local implemented delivery negative, not a general absence of adaptation in WebShop.

Generated diagnoses are candidates, with actual truth-apt content not determinable from the inspected wiring. A possible causal explanation is requested, but no inspected diagnosis-specific evidence-consuming acceptance or subsequent lifecycle integration is established in these ordinary loops. The relation remains indeterminate without output instances: it must not be upgraded to entailed derivation, or to ampliative conjecture merely because entailment was not demonstrated. Plans also contain non-truth-apt directives; their retention and model-input authority do not require calling them accepted knowledge. No warranted novel explanatory proposition or checked entailed factual derivation was demonstrated here.

Learning, reflection, autonomy and self-improvement retain the independent limits in the supplied runtime route theory accounts. Computational scheduling and advisory delivery are supported architecture; actual content-directed criticism, later semantic dependence, improved capacity and benefit remain unobserved. ALFWorld/HotPotQA have improvement-directed retained-input pathways; WebShop's action-side plan pathway is not supported by its caller. Client generation alone does not establish weight change or absence of learning through other retained material. No single system-wide epistemic status follows.

## Shared records

### Operative objects

#### EPI-OBJ-internal-tests
Label: Generated internal assertions

Part of: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

This object is the generated test-state part of that route, not the candidate code in [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl). Source-native identity: `valid_tests`, `tests`; form: symbolic executable assertions and textual expected-value claims; substrate: process list, later feedback/log fields. SRC-1 `programming_runs/generators/generator_utils.py`, `programming_runs/generators/py_generate.py`, `programming_runs/generators/rs_generate.py`. Python parses assertion-containing lines and applies `ast.parse` before sampling. Rust splits on semicolons, adds semicolons back and applies an always-true predicate: all fragments, including malformed ones, are eligible. The variable name `valid_tests` supplies no Rust syntax warrant; expected-output validity remains uninspected in both branches.

> valid_tests = [test for test in all_tests if is_syntax_valid(test)]
>
> return sample_n_random(valid_tests, max_num_tests)
> --- `programming_runs/generators/generator_utils.py`

#### EPI-OBJ-test-feedback
Label: Per-test outcomes and reference result

Part of: [RT-RTE-code-execution](runtime.md#rt-rte-code-execution)

The result part of the supplied execution route: source-native identities `ExecuteResult`, `feedback`, `state` and returned reference Boolean. Form: symbolic Boolean/tuple and natural-language error feedback; substrate: return values and caller state/log. This differs from executable code, which is input rather than result. SRC-1 `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py`; closest supplied record is the parent.

Python starts with `is_passing = True` and iterates over the test count, so an empty list leaves success true. Rust's evaluator checks recognized errors rather than exit status, limiting the license of its pass label.

> return ExecuteResult(is_passing, feedback, state)
> --- `programming_runs/executors/py_executor.py`

> print("Passed eval", flush=True)
> return len(errs) == 0
> --- `programming_runs/executors/rs_executor.py`

#### EPI-OBJ-qa-content
Label: Question evidence answer and match

Part of: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Container of individually assessed parts: source-native `context`/`scratchpad` paragraphs are natural-language imported evidence; `answer` is natural-language proposed answer; `key` is benchmark answer; EM Boolean is symbolic comparison result. Substrate: agent strings/fields and notebook dataset. The route parent contains each part; no counterpart object supplied. Their checks and consumers are split in the ledger, not assigned common factual warrant. SRC-1 `hotpotqa_runs/agents.py`; see parent's passages for comparison and prompt delivery.

> self.scratchpad += format_step(self.docstore.search(argument))
> --- `hotpotqa_runs/agents.py`

#### EPI-OBJ-program-reflection
Label: Program diagnosis hint

Part of: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Source-native `reflection`; natural-language model output held in process strings/list and JSONL. This is the diagnostic part of the parent, distinct from executable candidate and feedback. Requested explanation can make truth-apt causal claims; actual content uninspected. No separate acceptance check established. SRC-1 `programming_runs/generators/generator_utils.py`; parent supplies delivery passage and theory limits.

> reflection = model.generate(
>     f'{self_reflection_completion_instruction}\n{add_code_block(func)}\n\n{feedback}\n\nExplanation:')
> return reflection  # type: ignore
> --- `programming_runs/generators/generator_utils.py`

#### EPI-OBJ-qa-reflections
Label: Prior trace and diagnosis plans

Part of: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Source-native `reflections`, `reflections_str`; natural-language trace or model-generated diagnosis/plan, substrate agent list/string and serialized agent. Distinct part from current evidence/answer. Last-attempt retains trace; REFLEXION accumulates generated text; combined mode keeps one latest generated reflection with prior trace. SRC-1 `hotpotqa_runs/agents.py`, `hotpotqa_runs/prompts.py`; source request alone does not establish actual formulation, criticism or consumption. Theory properties are see parent route.

> self.reflections += [self.prompt_reflection()]
> self.reflections_str = format_reflections(self.reflections)
> --- `hotpotqa_runs/agents.py:305-306`

> lines[ind] = largest_observation.split(':')[0] + ': [truncated wikipedia excerpt]'
> --- `hotpotqa_runs/agents.py`

#### EPI-OBJ-alfworld-state
Label: ALFWorld outcome and task plans

Part of: [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial)

Source-native `env_history`, `env_configs`, `memory`, success flag. Natural-language observation/plan parts and symbolic success/index fields; substrate process history, logs and JSON snapshots. Distinct parts within the parent's trial: outcome has enforcing skip force; plans have advisory model-input force. SRC-1 `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/env_history.py`; see parent load-bearing passages for done/won, append and [RT-BAP-plan-guidance](runtime.md#rt-bap-plan-guidance) for actual consumer. No counterpart object supplied.

#### EPI-OBJ-webshop-state
Label: WebShop reward and stored plans

Part of: [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial)

Source-native `env_history`, `env_configs`, `memory`, server score. Natural-language HTML-derived observations/plans and symbolic reward/success fields; substrate client state, logs and JSON configs. Outcome, plan and action-input parts differ: stored plans reach reflection input, not inspected action input. SRC-1 `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`; see parent for minimum reward and action-call passages. This is a part object, not a duplicate of its containing route.

### Routes

#### EPI-RTE-test-filter
Label: Generated test predicate selection

Part of: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Generation output → language parser → caller predicate → sampled test list. Owner: `generic_generate_internal_tests`. This is the test eligibility subroute rather than the parent's program-success branch. Software decides membership, model proposes assertions; no per-test human veto established. Oracle is model-authored expected output, not validated by either predicate. Mode: bounded benchmark generation; guidance comes from caller instructions/examples. Python removes `ast.parse` failures; Rust removes nothing through its always-true predicate. Neither rejects false expectations; no rollback needed before execution. SRC-1 `programming_runs/generators/generator_utils.py`, `programming_runs/generators/py_generate.py`, `programming_runs/generators/rs_generate.py`; helper passage is see [EPI-OBJ-internal-tests](#epi-obj-internal-tests).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of up to max_num_tests Python parseable assertions or sampled Rust parsed fragments without syntax validation.
- Later read-back: inapplicable — ordinary current-pass tests, not a separately accumulated retained store in this helper.
- Delegated visibility: Provider gets specification/examples, executor later gets sampled assertions.
- Selection predicate: Python assertion-containing lines must pass py_is_syntax_valid (ast.parse); Rust semicolon-split fragments all pass lambda x: True; random subset if oversized.
- Invalidation or expiry: Caller replaces tests for a new pass; helper has no retention.
- Activation or effect: Subset determines later executor tests, not demonstrated semantic validity.
- Evidence limits: Caller predicates directly inspected in this correction; no generated test output inspected. Python parseability is not type checking or expected-value truth, and Rust's predicate checks neither syntax nor type correctness. Rust generation-to-execution remains separately blocked by its missing helper argument.

> is_syntax_valid=py_is_syntax_valid,
> --- `programming_runs/generators/py_generate.py`

> def py_is_syntax_valid(code: str) -> bool:
>     try:
>         ast.parse(code)
>         return True
>     except Exception:
>         return False
> --- `programming_runs/generators/py_generate.py`

> def parse_tests(tests: str) -> List[str]:
>     return [test + ";" for test in tests.split(";")]
> --- `programming_runs/generators/rs_generate.py`

> parse_tests=parse_tests,
> is_syntax_valid=(lambda x: True)  # TODO: for now. typecheck maybe?
> --- `programming_runs/generators/rs_generate.py`

The generation-call limitation is independent of these test predicates: the Rust caller omits the required helper argument below, whereas the Python caller supplies it. This prevents a complete Rust attempt or variant-generation wiring conclusion, not independent Rust executor/audit analysis.

> reflexion_few_shot=RS_REFLEXION_FEW_SHOT_ADD,
> parse_code_block=lambda x: parse_code_block(x, "rust"),
> add_code_block=lambda x: add_code_block(x, "rust"),
> )
> --- `programming_runs/generators/rs_generate.py`

> code_block_instruction: str,
> --- `programming_runs/generators/generator_utils.py`

> code_block_instruction=USE_PYTHON_CODEBLOCK_INSTRUCTION,
> --- `programming_runs/generators/py_generate.py`

#### EPI-RTE-answer-normalize
Label: Answer comparison normalization

Part of: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Source-native `normalize_answer` → `EM`; owner fixed Python helpers. This is a comparison-key subroute, not a different referent for the enclosing attempt. Natural-language answer/key are transformed to symbolic equality inputs. SRC-1 `hotpotqa_runs/agents.py` implementation. Concrete deduction without execution: `The A-B` lowercases to `the a-b`, loses punctuation to `the ab`, removes article `the` and collapses whitespace to `ab`. Key `AB` also becomes `ab`; EM returns true. This establishes equality under code, not semantic equivalence between the originals. Countercase also matters: a differently phrased true answer can fail key equality.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized string, then equality Boolean.
- Later read-back: inapplicable — pure comparison on current values, no accumulated store.
- Delegated visibility: inapplicable — no provider or separate agent call in normalization.
- Selection predicate: Every input character/string processed by fixed helper sequence.
- Invalidation or expiry: inapplicable — no retained normalized object or expiry protocol.
- Activation or effect: EM consumes result for correctness; semantic truth is not checked.
- Evidence limits: Deterministic code deduction, not observed target operation or key authentication.

> return white_space_fix(remove_articles(remove_punc(lower(s))))
> --- `hotpotqa_runs/agents.py`

> return normalize_answer(answer) == normalize_answer(key)
> --- `hotpotqa_runs/agents.py`

> return "".join(ch for ch in text if ch not in exclude)
> --- `hotpotqa_runs/agents.py`

> return re.sub(r"\b(a|an|the)\b", " ", text)
> --- `hotpotqa_runs/agents.py`

#### EPI-RTE-result-audit
Label: Solved result replay audit

Closest supplied [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) supplies local execution, but this distinct standalone route selects already logged solved rows and prints summary instead of revising attempts. Owner: `validate_py_results`/`validate_rs_results`; endpoints JSONL → tests → console. Two language branches are assessed separately in ledger evaluator field. Python code includes logged prompt+solution+tests+check; Rust invokes RsExecutor evaluate. Neither updates `is_solved` or writes corrected JSONL. Operator initiates audit, software decides outcome. Oracle: logged reference tests; mode bounded post-run audit. No proposals or product replacement occur, no automated veto/rollback; source diagnosis text is not assessed. SRC-1 `programming_runs/validate_py_results.py`, `programming_runs/validate_rs_results.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Console per-item verdict and summary; no corrected artifact.
- Later read-back: Logged solved code/test fields imported for reevaluation; no newly retained result read-back implemented.
- Delegated visibility: Python interpreter or Rust wrapper gets logged candidate/tests.
- Selection predicate: Only rows with is_solved true are executed; false rows print failed without reevaluation.
- Invalidation or expiry: No label invalidation/writeback; Rust wrapper cleanup does not roll back code effects.
- Activation or effect: Rerun results change printed counters/messages, not inspected future scheduling.
- Evidence limits: No audit run inspected; provenance of logs/tests and downstream human reliance uninspected.

> if item["is_solved"]:
>     func_impl = item["solution"]
>     code = f'{item["prompt"]}{func_impl}\n\n{item["test"]}\n\ncheck({item["entry_point"]})'
> --- `programming_runs/validate_py_results.py`

> red_text_out = red_text(f"failed but should have passed!")
> print(f"Test {i}: {red_text_out}")
> --- `programming_runs/validate_py_results.py`

> res = rs_executor.evaluate(item["entry_point"], func_impl, item["test"])
> --- `programming_runs/validate_rs_results.py`

#### EPI-RTE-leet-audit
Label: Stored LeetCode submission audit

Closest supplied [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) describes online wrapper evaluation; this distinct standalone script intends to consume every stored implementation and append an in-memory evaluations list. Its referent is the same scaffold as the supplied [MEM-RTE-leet-evaluation](memory.md#mem-rte-leet-evaluation); this correction aligns evidence strength rather than superseding that finding. Owner module body; endpoints input JSONL → formatter/submission → external environment → process list. SRC-1 `programming_runs/evaluate_leet_results.py`. It asserts len argv 3 but reads index 3: with assertions enabled length 3 reaches out-of-range access, while documented length 4 fails assertion. Unconditional dependency imports occur earlier and can fail first. Output path is read but unused; `evaluate_rs_leet_results.py` is empty. Do not infer successful offline grading/writeback.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Intended in-memory evaluations only; with assertions enabled no argument length can reach the loop because the length assertion and index access contradict each other, even if dependencies are supplied.
- Later read-back: Intended stored-implementation import is blocked at entry with assertions enabled; no persisted new evaluations or later consumer shown.
- Delegated visibility: External formatter/environment would receive code and question slug if reached.
- Selection predicate: Every implementations entry in each input row; no correctness prefilter.
- Invalidation or expiry: env.reset after each submission if reached; no prior result withdrawal.
- Activation or effect: Parent submission/list-append/reset text is an afforded scaffold, not wired delivery through this standalone entry point; argument contradiction blocks it with assertions enabled. Dependency availability alone would not repair that defect.
- Evidence limits: Remote semantics inaccessible, implementation representation compatibility unresolved, no observed run.

> assert len(sys.argv) == 3, "Provide a language [py, rs], input and output log file"
> lang = sys.argv[1]
> input_log_path = sys.argv[2]
> output_log_path = sys.argv[3]
> --- `programming_runs/evaluate_leet_results.py`

> status, reward, done, info = env.step(submission)
> --- `programming_runs/evaluate_leet_results.py`

### Claims

#### EPI-CLM-strategy-guidance
Label: Prior attempt strategy guidance

No counterpart after comparison with [RT-CLM-persisting-memory](runtime.md#rt-clm-persisting-memory), whose declared scope is ALFWorld storage. This claim concerns HotPotQA prior-material context and requested answer improvement. SRC-1 `README.md` and `hotpotqa_runs/prompts.py`, doctrine/design. Instructional claim is intended use, not demonstrated benefit or diagnosis truth.

> - `ReflexionStrategy.REFLEXION` - The agent is given its self-reflection on the last attempt as context.
> --- `README.md`

> REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'
> --- `hotpotqa_runs/prompts.py`
