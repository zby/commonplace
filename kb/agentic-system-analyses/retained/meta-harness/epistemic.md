---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Meta-Harness epistemic routes: task-answer checking, harness selection and the limits of mechanism inference from benchmark feedback."
run-id: AAS-2026-10-14-meta-harness-5e480e270fee-01
reviewed-boundary: "8123ccabe2b19fa1123090b2e5f1bacc20963ce8"
---

# Meta-Harness epistemic report

## Source-and-claim boundary

The question is what Meta-Harness acquires, checks and licenses for later reliance, and whether checking task outcomes also accepts explanations of harness improvement. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and layers are see [Source register](boundary.md#source-register). The whole-system repository boundary includes both reference experiments, onboarding and the pilot, but not the external providers, Harbor internals, paper or optimized artifact. All new findings below are SRC-1 implementation or doctrine/design evidence. No target execution was performed.

The supplied runtime is provisional. Direct reads added dataset evaluator semantics, baseline demonstration handling, numerical aggregation, pilot local verifiers, and observation filtering. The runtime already covers candidate import, finalization, source staging, tool grants and model mutability. The additional records are parts of those routes, not competing whole-loop accounts. No supplied fact requires supersession; two important qualifications are that trial-count warnings do not enforce complete terminal sampling, and the pilot's `accepted` means source admission to scoring, not evidence-consuming acceptance of a useful harness.

| Entry point or operation | Source path, SRC-1 | Coverage basis and records | Unassessed portion and prevented conclusion |
|---|---|---|---|
| Classification proposer and pending handoff | `reference_examples/text_classification/meta_harness.py`; `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md` | Direct skill read and dispatch search; supplied [RT-RTE-classification-search](runtime.md#rt-rte-classification-search), [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval), [RT-BAP-proposer-instructions](runtime.md#rt-bap-proposer-instructions) | No actual model hypothesis/report; prevents judging semantic inference or compliance in a round. |
| Benchmark/inner-loop direct commands, training and test mode | `reference_examples/text_classification/benchmark.py`; `reference_examples/text_classification/inner_loop.py` | Direct evaluation, aggregation/frontier reads and CLI search; [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-frontier-selection](#epi-rte-frontier-selection); supplied [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize) | Loader bodies and all dataset records not inspected here; source-label truth and full data provenance not established. |
| Classification retained demonstrations and answer extraction | `reference_examples/text_classification/agents/fewshot_memory.py`; `reference_examples/text_classification/memory_system.py`; `reference_examples/text_classification/data/evaluators.py` | Direct reads; [EPI-RTE-example-context](#epi-rte-example-context), [EPI-RTE-answer-check](#epi-rte-answer-check) | Generated replacement systems unavailable; their learned summaries or other semantic transformations cannot be assessed from the baseline. |
| Classification provider cache and prompt truncation | `reference_examples/text_classification/llm.py` | Direct selected ranges; [EPI-RTE-observation-filter](#epi-rte-observation-filter); supplied [RT-CMP-classification-llm](runtime.md#rt-cmp-classification-llm) | Provider weights and backend cache validity inaccessible; replay identity does not establish current model identity. |
| Terminal proposal, admission, smoke bypass and final pass | `reference_examples/terminal_bench_2/meta_harness.py`; `reference_examples/terminal_bench_2/scripts/run_eval.sh`; `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md` | Direct skill, parser/frontier reads and dispatch search; supplied [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), new [EPI-RTE-terminal-scoring](#epi-rte-terminal-scoring) | Shell adapter semantics supplied by runtime rather than reread; external official verifier/task payloads not frozen. Prevents full task-oracle correctness assessment. |
| KIRA shell/image/completion tools, output cleanup and recovery | `reference_examples/terminal_bench_2/agents/baseline_kira.py` | Direct marker-filter read and tool search; supplied [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution), new [EPI-RTE-observation-filter](#epi-rte-observation-filter) | Inherited summarization, image inference and model-produced completion claims not observed; their semantic fidelity remains unresolved. |
| Pilot registered tools and controller CLI | `experimental/harbor_meta_harness/agents/meta_harness.py`; `experimental/harbor_meta_harness/controller.py` | Complete direct reads; [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-suite-scoring](#epi-rte-suite-scoring); supplied [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) | Direct controller has no outer-tool budget. Child Harbor import/runtime remains external. |
| Pilot local suite and outer reward verifier | `experimental/harbor_meta_harness/suite.toml`; `experimental/harbor_meta_harness/tasks/budget-rollups/tests/test_outputs.py`; `experimental/harbor_meta_harness/tasks/dedupe-events/tests/test_outputs.py`; `experimental/harbor_meta_harness/tasks/reconcile-ledger/tests/test_outputs.py`; `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py` | Complete direct reads; [EPI-RTE-suite-scoring](#epi-rte-suite-scoring), [EPI-RTE-history-selection](#epi-rte-history-selection) | Input fixtures/instructions not independently reconciled with hardcoded expected outputs; prevents certifying those expectations as correct derivations. |
| Pilot terminal scaffold and collection preparation | `experimental/harbor_meta_harness/agents/terminal_harness.py`; `experimental/harbor_meta_harness/scripts/prepare_collections.py` | Scaffold tool search; supplied [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) and boundary trace | Collection preparation and remaining suite variants not directly inspected here; downloaded task semantics unavailable. No system-complete absence claim about all possible evaluators. |
| Domain-spec onboarding | `ONBOARDING.md` | Supplied [RT-RTE-domain-onboarding](runtime.md#rt-rte-domain-onboarding) | No completed spec or downstream adoption trace; prevents assessment of actually accepted domain decisions. |

Dispatch/tool search covered the reference drivers, benchmark, inner loop and wrappers, KIRA, the pilot controller, outer agent and terminal scaffold for CLI argument declarations, main dispatch, hooks, tool grants and tool-call branching. It confirmed direct benchmark/controller alternatives and the exposed shell/evaluation routes, not an additional universal epistemic gate. External host hooks were not inspected. This coverage is sufficient for the positive witnesses below, not an exhaustive system-wide negative.

Knowledge/warrant claims assessed are see [RT-CLM-fixed-model](runtime.md#rt-clm-fixed-model) and [EPI-CLM-mechanism-tests](#epi-clm-mechanism-tests). The root release caveat bounds the architectural claim; it is not evidence of measured performance:

> This is a cleaned-up version of the code we used for the paper. It has not been tested beyond verifying that it runs. Please let us know if anything goes wrong.
> --- `README.md`

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval) | Hypotheses predicting mechanism effects; candidate IDs themselves are not truth claims | see record | see record | No produced hypothesis instance supplied; source instructions establish requested forecasts, not their actual content. |
| [EPI-OBJ-examples](#epi-obj-examples) | Imported input/target associations | see record | see record | Dataset warrant unknown; raw-question substitution and caps affect what reaches inference. |
| [EPI-OBJ-predictions](#epi-obj-predictions) | Predicted labels, reactants, diagnoses or charges relative to an input | see record | see record | No prediction instance supplied; truth beyond dataset convention not established. |
| [EPI-OBJ-val-results](#epi-obj-val-results) | Correctness, accuracy, context cost and ranked candidate identities | see record | see record | Metrics warrant only their defined transformation of supplied records, not causal explanations. |
| [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | Admission flag, source digest, per-task/aggregate reward and historical reward | see record | see record | Distinct components have distinct criteria and consumers; flag is not performance acceptance. |
| [EPI-OBJ-terminal-output](#epi-obj-terminal-output) | Environment observations and model summaries may contain factual assertions | see record | see record | Shell tails/filters can discard evidence; inherited summary semantics unresolved. |
| [RT-CMP-claude-proposer](runtime.md#rt-cmp-claude-proposer), [RT-CMP-classification-llm](runtime.md#rt-cmp-classification-llm), [RT-CMP-kira-llm](runtime.md#rt-cmp-kira-llm), [RT-CMP-pilot-outer](runtime.md#rt-cmp-pilot-outer), [RT-CMP-pilot-child](runtime.md#rt-cmp-pilot-child) | not determinable for individuated weight-encoded propositions | see records | see records | No weight access, training provenance or operation trace; component mutability findings do not individuate accepted knowledge. |
| [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution) | Executable harness policies; propositional assumptions depend on actual code | see record | see record | Execution authority is separate from evidential warrant; arbitrary generated replacements not supplied. |

## Authority-route ledger

Fields owned by cited records say `see`. Each row assesses a distinct consequential function; sharing a route citation does not merge its checking, selection or retention functions.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-classification-search](runtime.md#rt-rte-classification-search), [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search) | content transformation | implemented | [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval) | truth-apt transformation: indeterminate | Proposed hypothesis/code | see records | see records | Candidate source/manifest possible; no observed instance | see records | Candidate generation only; semantic preservation, entailment and novelty require actual outputs | see records | see records | see records | [EPI-CLM-mechanism-tests](#epi-clm-mechanism-tests) | none | Forecasts are requested but no content edge can be classified from an unavailable round. |
| [RT-RTE-classification-search](runtime.md#rt-rte-classification-search), [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), [EPI-RTE-source-check](#epi-rte-source-check) | operational admission/selection/consumption | implemented | [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution) | non-truth-apt policy/content update: install candidate execution rules | Candidate compatibility/admission | see records | see records | Import/interface pass or rejection; smoke bypass possible | see records | No truth or useful-performance license from compatibility alone | see records | see records | see records | [RT-CLM-fixed-model](runtime.md#rt-clm-fixed-model) | none | Code gains force before frontier selection. |
| [EPI-RTE-example-context](#epi-rte-example-context) | content transformation | implemented | [EPI-OBJ-examples](#epi-obj-examples) | truth-apt transformation: acquisition/import | Training labels into demonstrations | see record | see record | Input/target pairs copied | see record | Source warrant unknown, not improved by copying | see record | see record | see record | none | none | Acquisition, not production of training-label truth. |
| [EPI-RTE-example-context](#epi-rte-example-context) | retention | implemented | [EPI-OBJ-examples](#epi-obj-examples) | no content change | State serialization/load | see record | see record | JSON examples retained and restored | see record | No evidence-consuming acceptance criterion | see record | see record | see record | none | none | Retention precedes demonstrated correctness of examples. |
| [EPI-RTE-example-context](#epi-rte-example-context) | operational admission/selection/consumption | implemented | [EPI-OBJ-examples](#epi-obj-examples) | truth-apt transformation: non-ampliative reshaping | Select and format Q/A context | see record | see record | Sample/tail selection and bounded formatting | see record | Selected associations only; omitted input scope may matter | see record | see record | see record | none | none | Not a warranted general lesson or new explanation. |
| [EPI-RTE-answer-check](#epi-rte-answer-check) | check/evidence production | implemented | [EPI-OBJ-predictions](#epi-obj-predictions) | truth-apt transformation: entailed derivation | Answer/target comparison | see record | see record | Boolean/metrics and accuracy | see record | Entailed comparator results conditional on target and encoding; not source truth | see record | see record | see record | none | none | Comparator interpretations differ by task. |
| [EPI-RTE-frontier-selection](#epi-rte-frontier-selection) | disposition/acceptance | implemented | [EPI-OBJ-val-results](#epi-obj-val-results) | no content change | Validation winner/Pareto eligibility | see record | see record | Selected candidate identities | see record | Evidence-consuming operational acceptance for further use under metric criterion, not mechanism explanation | see record | see record | see record | [EPI-CLM-mechanism-tests](#epi-clm-mechanism-tests) | outcome/mechanism distinction | Dataset coverage and freshness bound comparison. |
| [EPI-RTE-frontier-selection](#epi-rte-frontier-selection) | retention | implemented | [EPI-OBJ-val-results](#epi-obj-val-results) | truth-apt transformation: non-ampliative reshaping | Write frontier and summaries | see record | see record | Rounded scores and selected IDs persisted | see record | No extra warrant from retention | see record | see record | see record | none | none | Summary hypotheses remain model-authored, not software-certified. |
| [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize) | check/evidence production | implemented | [EPI-OBJ-val-results](#epi-obj-val-results) | truth-apt transformation: entailed derivation | Selected systems on test targets | see record and [EPI-RTE-answer-check](#epi-rte-answer-check) | see record | Test metrics and completion/missing-result state | see record | Test-target agreement only; operational holdout not secrecy | see record | see record | see record | none | none | No observed test outcome or authenticated candidate-byte freeze. |
| [EPI-RTE-terminal-scoring](#epi-rte-terminal-scoring) | check/evidence production | implemented | [EPI-OBJ-val-results](#epi-obj-val-results) | truth-apt transformation: entailed derivation | Rewards from discovered trial directories | see record | see record | Positive-reward pass fractions | see record | Defined trial-file statistic, not necessarily a complete official-dataset estimate | see record | see record | see record | none | completeness warning | Entire missing directories are not denominator entries. |
| [EPI-RTE-terminal-scoring](#epi-rte-terminal-scoring) | disposition/acceptance | implemented | [EPI-OBJ-val-results](#epi-obj-val-results) | no content change | Better per-task/overall score | see record | see record | Frontier replacement | see record | Operational acceptance for subsequent search/final reevaluation on same dataset | see record | see record | see record | [EPI-CLM-mechanism-tests](#epi-clm-mechanism-tests) | outcome/mechanism distinction | No component intervention or transfer test. |
| [EPI-RTE-source-check](#epi-rte-source-check) | check/evidence production | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | truth-apt transformation: entailed derivation | Literal-reference/syntax/minimal AST interface | see record | see record | Rejection reason or no reason | see record | Only predicates over source spelling and syntax | see record | see record | see record | none | none | Semantic safety and hidden-suite nonaccess not proved. |
| [EPI-RTE-source-check](#epi-rte-source-check) | disposition/acceptance | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | no content change | Admit candidate to child scoring | see record | see record | `accepted=False` rejection or `accepted=True` scored | see record | Admission criterion for evaluation, not a success threshold | see record | see record | see record | none | acceptance-label limit | Zero-reward source can still be accepted. |
| [EPI-RTE-suite-scoring](#epi-rte-suite-scoring) | check/evidence production | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | truth-apt transformation: entailed derivation | Local output equality/child reward aggregation | see record | see record | Task rewards and suite aggregate | see record | Agreement with encoded expected objects; aggregate conditional on child records | see record | see record | see record | none | none | Task expectations not independently certified; runtime failure maps to zero. |
| [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) | retention | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | truth-apt transformation: non-ampliative reshaping | Record and upload evaluation history | see record | see record | Full result history retained; subset sent to outer model | see record | Digest tracks evaluated source, not final code identity | see record | see record | see record | none | none | Tool response omits accepted flag/digest, retaining reward/tasks/reason/budget. |
| [EPI-RTE-history-selection](#epi-rte-history-selection) | disposition/acceptance | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | truth-apt transformation: entailed derivation | Budget arithmetic and historical accepted reward | see record | see record | Maximum historical reward or zero | see record | Report-conditional outer score only | see record | see record | see record | none | history/final-artifact distinction | No final-source revalidation, cryptographic lineage check or restore-best. |
| [EPI-RTE-observation-filter](#epi-rte-observation-filter) | content transformation | implemented | [EPI-OBJ-terminal-output](#epi-obj-terminal-output) | truth-apt transformation: indeterminate | Cleanup/truncation of observations and prompts | see record | see record | Tail/head kept, middle or marker-bearing lines removed | see record | Neither a factual evaluator nor a warranted complete summary | see record | see record | see record | none | semantic-loss countercase | Can remove load-bearing information; preserved fragments versus altered interpretation require actual content. |
| [RT-RTE-classification-search](runtime.md#rt-rte-classification-search), [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) | behavior/policy adaptation | implemented | [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution) | non-truth-apt policy/content update: model-selected executable edits | Score/history to later edit opportunity | see records | see records | Feedback can shape later code; no observed dependency | see records | Performance feedback does not itself warrant theory acceptance | see records | see records | see records | [RT-CLM-fixed-model](runtime.md#rt-clm-fixed-model) | none | Actual evidence-responsive change and benefit remain unobserved. |

The countercases used to bound these rows are source-supported: a correctly imported harness may fail tasks; a pilot source may score zero yet receive `accepted=True`; warnings permit incomplete terminal trial counts; demonstration retention occurs without testing target truth; and marker cleanup removes whole matching lines rather than just protocol tokens. These are implementation deductions, not adversarial runs. See the respective shared records for their passages.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-fixed-model](runtime.md#rt-clm-fixed-model) | see record | see record | see record | [RT-RTE-classification-search](runtime.md#rt-rte-classification-search), [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) | none supplied | No controlled model-version trace or comparison; component fixity is see runtime components | Search changes code/context/state rather than implementing weight training | Exact served model identity and improved performance unestablished. |
| [EPI-CLM-mechanism-tests](#epi-clm-mechanism-tests) | see record | see record | One mechanism, falsifiable hypothesis, trace-led design requested | [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-frontier-selection](#epi-rte-frontier-selection), [EPI-RTE-terminal-scoring](#epi-rte-terminal-scoring) | none supplied | Benchmark outcome comparison can test predicted consequence, but does not isolate mechanism; code/auxiliaries and sampling may also change | Software supplies outcome evidence and operational selection; model instructions request explanatory criticism | No implemented automatic acceptance of explanatory truth, blame placement or transfer warrant is established by these paths. |

## Bounded conclusion

Meta-Harness has several check-and-use routes, not one epistemic oracle. Classification imports target-labelled examples, retains them and selects demonstrations for prediction. In the inspected baseline, acquisition preserves copied target strings but source warrant is unknown; formatting, raw-question substitution, sampling and caps bound delivered context. It produces model answers whose semantic relation to inputs is not determinable without actual outputs. Its programs derive comparator results and accuracies within dataset-specific text/set domains. Those derivations inherit, rather than validate, their targets. See [EPI-RTE-example-context](#epi-rte-example-context) and [EPI-RTE-answer-check](#epi-rte-answer-check).

Classification frontier selection consumes accuracy/context evidence for a named intended use: retain candidate identities for subsequent search and final test selection. Per-dataset maximization and aggregate Pareto eligibility are operational acceptance criteria, not evidence that a proposed explanation is true. Complete seed groups are required by the result loader, but complete dataset coverage per candidate and source/model freshness are not established by those checks. Terminal selection instead uses positive-reward fractions from discovered trial directories, replacing winners on strict improvement. Its trial-count warnings and same-dataset final pass do not supply a separately held-out transfer check. See [EPI-RTE-frontier-selection](#epi-rte-frontier-selection), [EPI-RTE-terminal-scoring](#epi-rte-terminal-scoring) and [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize).

The pilot has independent source admission, output evaluation, retention and outer scoring. The AST/string gate licenses evaluation, even if child tasks all fail. The local task verifiers license equality with hardcoded JSON expectations; their reward feeds the suite aggregate and model-visible feedback. History scoring licenses an outer reward from maximum accepted historical score, conditional on report arithmetic, not a claim that final code embodies the winning evaluated source. These channels enforce execution admission and reward computation; they provide the outer model an advisory opportunity for further edits. No human per-content acceptance is wired. See [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-suite-scoring](#epi-rte-suite-scoring), [EPI-RTE-history-selection](#epi-rte-history-selection) and [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search).

Retained scores, hypotheses, code and training state do have later consumers. That does not establish lifecycle integration of accepted explanatory claims. The selected paths show no evidence-consuming decision that licenses an ampliative explanation under a named intended scope and then integrates it as accepted knowledge. This is a route-local finding: uninspected generated candidates and opaque model processes prevent a system-complete negative. The instructions request conjectures and content-directed criticism, while the implemented checks chiefly assess answer/output agreement and performance selection. Scores can challenge a forecast without deciding whether blame belongs to code, data, measurement or the theory. See [EPI-CLM-mechanism-tests](#epi-clm-mechanism-tests).

Direct policy adaptation is architecturally available through executable edits and admission even without accepted truth-apt theory. Learning benefit, exercised reflection, autonomous theory-building and successful self-improvement remain independent and unobserved here; the runtime records preserve their separate dispositional and theory-condition findings. Model parameters are external and not updated by the inspected routes, but exact identities are not pinned. Neither this fixity nor the feedback architecture proves model knowledge or gain. Observation filtering can further limit what evidence reaches model judgment, as shown by [EPI-RTE-observation-filter](#epi-rte-observation-filter). No single system-wide epistemic status follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-examples
Label: FewShotMemory examples

Natural-language input/target pairs within a symbolic Python list and serialized JSON on disk; demonstrations are consumed by model interpretation. No supplied object counterpart after comparison with [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval): the manifest identifies candidates, while this list supplies labelled task context. SRC-1, `reference_examples/text_classification/agents/fewshot_memory.py`, implementation.

> ex = {"input": r["input"], "target": r["ground_truth"]}
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

#### EPI-OBJ-predictions
Label: Classification predictions

Natural-language model answer strings, consumed as symbolic comparator inputs and retained in prediction-result JSON. Distinct from the hypotheses/candidate IDs in [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval). SRC-1, `reference_examples/text_classification/inner_loop.py`, implementation.

> pred, _ = memory.predict(ex["input"])
> --- `reference_examples/text_classification/inner_loop.py:439-443`

#### EPI-OBJ-val-results
Label: Validation results

Symbolic metrics, frontier identities and result JSON/JSONL on disk. Model-authored hypotheses carried in summaries retain natural-language consumption separately; this object denotes numerical evaluation and selection fields, not those hypotheses. No supplied object counterpart after comparison with [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval), which is an input handoff rather than measured output. Covers reference classification and terminal result families with heterogeneous checks identified in routes. SRC-1, `reference_examples/text_classification/benchmark.py`, `reference_examples/terminal_bench_2/meta_harness.py`, implementation.

> frontier_path.write_text(json.dumps(frontier, indent=2))
> --- `reference_examples/text_classification/benchmark.py`

#### EPI-OBJ-evaluation-results
Label: EvaluationResult and history

Pilot symbolic source digest, admission flag, reward and task results in JSON; accumulated results also occupy an immutable tuple in outer state and uploaded history JSON. Distinct from [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval): this is a pilot controller response/history, not either reference manifest. SRC-1, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`, implementation.

> class EvaluationResult:
>     source_sha256: str
>     accepted: bool
>     reason: str
>     reward: float | None
>     tasks: tuple[TaskResult, ...]
> --- `experimental/harbor_meta_harness/controller.py`

#### EPI-OBJ-terminal-output
Label: Terminal output

Environment-produced textual observations in transient message/terminal state, interpreted by models; observations may encode data, program results or claims. KIRA and pilot retain/filter different portions. Distinct from [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval), and not another identity for any model component. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`, implementation.

> output = await session.get_incremental_output()
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

### Routes

#### EPI-RTE-example-context
Label: Example acquisition and context
Part of: [RT-RTE-classification-search](runtime.md#rt-rte-classification-search)

Training batch results → FewShotMemory list → serialized state → restored state → selected Q/A prompt → model answer. Python owns copying, state I/O and selection; the model owns answer generation. SRC-1, `reference_examples/text_classification/agents/fewshot_memory.py`, `reference_examples/text_classification/memory_system.py`, implementation. The reused restored state also enters [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize); the declared referent is the baseline acquisition/context mechanism within search.

- Immediate return: `predict` returns extracted `final_answer` plus response metadata; learning appends examples, state returns JSON.
- Later read-back: Accumulated examples reach subsequent prediction calls and serialized training memory reaches test prediction via `set_state`.
- Delegated visibility: Solver receives formatted examples and current input, not the full training trace or outer proposer history.
- Selection predicate: Input-hash seed; random sample above max_examples, otherwise tail selection/shuffle; loop stops at MAX_CHARS. Raw question substitutes for full input when supplied.
- Invalidation or expiry: Restoring state replaces examples; no per-example warrant withdrawal or stale-label check is implemented in this baseline.
- Activation or effect: Selected strings enter the model prompt; actual reliance or accuracy effect is unobserved.
- Evidence limits: No actual state or prediction supplied; copying source targets does not validate them. Generalized generated-memory behavior cannot be inferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software copying, not human per-example approval; the answer oracle is supplied ground truth for later evaluation, not model interpretation of examples. Mode is configured training/evaluation. No separate acceptance threshold gates example addition, and no formulated lesson is produced by this baseline. Concrete deduction: a batch with input `q` and ground_truth `safe` adds that pair; absent raw_question, formatting emits `Q: q` followed by `A: safe`. This is acquisition and reshaping, not a new general claim.

> part = f"Q: {question}\nA: {ex['target']}"
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

> return json.dumps({"examples": self.examples}, indent=2)
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

#### EPI-RTE-answer-check
Label: Classification answer checking
Part of: [RT-RTE-classification-search](runtime.md#rt-rte-classification-search)

Prediction and dataset target → task-specific extraction/normalization/comparison → Boolean/metrics → accuracy result. Python evaluator owns checking; the target is answer agreement under the named dataset encoding, not open-world diagnosis/legal/chemical truth. SRC-1, `reference_examples/text_classification/data/evaluators.py`, `reference_examples/text_classification/inner_loop.py`, implementation.

- Immediate return: Correctness and optional metrics, then prediction records and aggregate accuracy.
- Later read-back: Validation/test result files reach benchmark aggregation, frontier selection and later instructed proposer reads.
- Delegated visibility: Evaluator receives prediction, target and optional example kwargs, not a proof or complete proposer rationale.
- Selection predicate: FiNER lowercased trimmed equality; USPTO dotted-string sets and Jaccard; diagnosis normalized text; LawBench charge sets/F1; AEGIS safe/unsafe substring extraction; transfer classification normalization.
- Invalidation or expiry: Recalculation on another evaluation call; result reuse has no source/model digest enforcement established here.
- Activation or effect: Comparator outcomes determine score fields consumed by selection; model compliance is not checked by this path.
- Evidence limits: Oracle targets are imported conventions; label truth, chemical equivalence and clinical/legal validity beyond comparison are unchecked here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No per-answer human verdict is wired. The model proposes an answer; software can mark it wrong, but scoring does not prevent prior code execution. Operational mode is configured train/validation/test evaluation. Concrete countercase: `eval_aegis` with prediction `not unsafe` and target `unsafe` returns true because the substring `unsafe` is selected. This implementation deduction defeats interpreting its Boolean as a checked reading of the whole sentence. For USPTO, duplicated/order-swapped dotted strings collapse to a set, licensing that text-set equivalence only.

> if "unsafe" in pred:
>     pred = "unsafe"
> elif "safe" in pred:
>     pred = "safe"
> --- `reference_examples/text_classification/data/evaluators.py`

> raw = check_answer(pred, ex["target"], **_get_eval_kwargs(ex))
> ok, metrics = _unpack_eval_result(raw)
> --- `reference_examples/text_classification/inner_loop.py:439-450`

#### EPI-RTE-frontier-selection
Label: Classification frontier selection
Part of: [RT-RTE-classification-search](runtime.md#rt-rte-classification-search)

Result files → complete configured seed groups → aggregate metrics → per-dataset winner/aggregate Pareto list → frontier JSON → search/finalization consumers. Python benchmark owns the decision. SRC-1, `reference_examples/text_classification/benchmark.py`, implementation. This is the numerical selection part, not another declaration of the full search loop.

- Immediate return: Printed statistics and frontier JSON.
- Later read-back: Driver/proposer instructions use frontier; finalization selects its entries for test evaluation.
- Delegated visibility: Consumers receive selected identities and aggregate accuracy/context fields, not necessarily all seed-level evidence.
- Selection predicate: Required seed groups; correct/total pooled when present, otherwise mean accuracy; dataset max accuracy with shorter-context tie break; non-dominated aggregate accuracy/context points.
- Invalidation or expiry: Frontier recomputed/written; usable numeric accuracy files can be reused without code-digest invalidation.
- Activation or effect: Frontier determines final-test candidate selection and supplies advisory next-proposal evidence; actual proposer reliance unobserved.
- Evidence limits: Aggregation does not verify targets, candidate byte identity or complete dataset coverage per candidate; no observed improvement or causal component contrast.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operator chooses configuration and initiates finalization; model proposes code, software selects winners and excludes incomplete seed groups. There is no per-content human approval or statistical-significance gate. Oracle is target agreement upstream. Operational criterion is maximization/non-domination for retained search candidates and final-test eligibility; it grants no explanatory warrant. Frontier replacement/recomputation is recovery, not transactional rollback of arbitrary candidate edits. Hypotheses travel with scores but are not certified. Theory conditions and independent learning/reflection findings remain see the parent record.

> if any(seed not in by_seed for seed in required_seeds):
>     continue
> --- `reference_examples/text_classification/benchmark.py`

> best = max(
>     by_dataset[dataset], key=lambda x: (x["accuracy"], -x["ctx_len"])
> )
> --- `reference_examples/text_classification/benchmark.py`

#### EPI-RTE-terminal-scoring
Label: Terminal reward scoring and selection
Part of: [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search)

Discovered trial-directory rewards → zero substitution for missing/malformed trial results → positive-reward fractions → strict-improvement frontier replacement. Python owns computation and selection; external Harbor verifiers supply reference outcomes. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`, implementation.

- Immediate return: Per-task/flat pass rates and updated frontier JSON.
- Later read-back: Frontier/summary reach later proposal instructions; overall winner enters optional same-dataset final reevaluation.
- Delegated visibility: Proposer/analysis child is instructed to read scores and trajectories; actual reads/compliance unobserved.
- Selection predicate: Any reward greater than zero is a pass; frontier replaces on strict improvement. Trial counts only produce warnings.
- Invalidation or expiry: Existing per-task/overall winners remain unless exceeded; no statistical uncertainty adjustment or source-hash invalidation established here.
- Activation or effect: Ranking changes retained candidate identity and optional final-evaluation choice; useful deployed gain unobserved.
- Evidence limits: Missing entire task/trial directories do not enter the denominator; reward extraction does not validate external verifier semantics. No held-out transfer or component causality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model supplies variants; software decides ranking; operator chooses trial count/mode and can skip smoke, but does not approve each content change. Oracle is imported task verifier reward. Recovery keeps previous winners and maps many trial-result failures to zero. Mechanism criticism and resulting reliance remain requested rather than observed; see the parent theory account. Concrete deduction: one discovered trial with reward 1 for a task and expected_trials 2 yields a warning and a 1.0 pass rate, not a forced 0.5; the undiscovered second trial is not added.

> if len(rewards) != expected_trials:
>     print(
>         f"  {_yellow('warning')}: {task} has {len(rewards)}/{expected_trials} trials"
>     )
> --- `reference_examples/terminal_bench_2/meta_harness.py`

> per_task[task] = sum(r > 0 for r in rewards) / len(rewards) if rewards else 0.0
> --- `reference_examples/terminal_bench_2/meta_harness.py`

> if avg > current_best_avg:
>     frontier["_best"] = {
>         "agent": agent_name,
>         "avg_pass_rate": avg,
>     }
> --- `reference_examples/terminal_bench_2/meta_harness.py`

#### EPI-RTE-source-check
Label: Pilot source admission check
Part of: [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search)

Downloaded source → digest → literal forbidden scan and minimal AST interface → rejection or temporary staging → child execution/scoring. The controller owns check and disposition, independently of outer model judgments. SRC-1, `experimental/harbor_meta_harness/controller.py`, implementation.

- Immediate return: Source digest, accepted flag and rejection reason or scored result.
- Later read-back: Full result is retained in history; outer model receives reward/tasks/reason/budget, not digest or flag in the normal response.
- Delegated visibility: Child receives staged candidate source and suite child configuration, not outer conversation.
- Selection predicate: No forbidden literal; parseable source; top-level AgentHarness with async run and syntactically named BaseAgent base.
- Invalidation or expiry: Temporary candidate directory deleted after scoring; persistent snapshots/history retain earlier source/reward identity.
- Activation or effect: Rejection blocks child launch on this controller route; passing grants child import/execution before task success is known.
- Evidence limits: Does not resolve base identity semantically, type-check behavior, enforce all forbidden equivalent actions or validate final artifact identity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model proposes source edits and chooses tool timing; controller software vetoes incompatible/literal-forbidden source, human only configures the initial task/suite. Mode is bounded evaluation-tool experimentation or standalone controller. There is no answer oracle for the source-admission predicate; task output oracles operate downstream. Passing source stays accepted even when every child fails and returns zero. No automatic restoration follows rejection. Guidance against benchmark references is supplemented by this lexical protocol, not a universal isolation invariant.

> if reason:
>     return EvaluationResult(source_sha256, False, reason, None, ())
> --- `experimental/harbor_meta_harness/controller.py`

> return EvaluationResult(
>     source_sha256,
>     True,
>     "scored",
>     suite.aggregator(rewards),
>     tuple(task_results),
> )
> --- `experimental/harbor_meta_harness/controller.py`

#### EPI-RTE-suite-scoring
Label: Pilot child outcome checking
Part of: [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search)

Task output files → local equality verifiers → child Harbor result files → controller rewards → suite aggregate → outer model feedback/history. Local verifier programs own output checks; controller owns extraction/aggregation; Harbor scheduling/result production is external. SRC-1, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/suite.toml`, the three local verifier paths below, implementation.

- Immediate return: Local scalar reward; controller TaskResult tuple and aggregate reward.
- Later read-back: Result history reaches outer reward verifier; scores/tasks/reasons reach another outer-model invocation within the run.
- Delegated visibility: Outer model receives task summaries and job paths; evaluated source digest and accepted flag remain in history, not its normal tool response.
- Selection predicate: Local parsed JSON exact equality; controller expects exactly one `*/result.json` per task job, extracts numeric reward; suite selects mean/min/fraction_solved aggregation.
- Invalidation or expiry: New evaluations produce new snapshots/jobs; no automatic accepted-claim withdrawal or restore-best code action.
- Activation or effect: Rewards become advisory edit feedback and authoritative inputs to historical outer scoring; actual edits caused by feedback unobserved.
- Evidence limits: Imported hardcoded expected outputs not independently derived here. Nonzero exit, timeout and missing/malformed/ambiguous result all map to zero, conflating infrastructure and answer failure.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Check targets are `/app/rollups.json`, `/app/unique.json` and `/app/report.json` under the three local tasks, respectively. The oracle is each verifier's fixed expected object, not model critique. Evaluation judges only file equality, including list order for dedupe; it does not establish the producing process. The model supplies task actions; software supplies outcome and aggregate, with no human verdict. Default mode is three tasks, one attempt, mean aggregate. Counterpath: configurable multiple attempts yield zero at `child_result` if more than one result file matches; n_attempts configurability is not evidence that multi-attempt aggregation is implemented there.

> Path("/logs/verifier/reward.txt").write_text("1\n" if actual == expected else "0\n")
> --- `experimental/harbor_meta_harness/tasks/budget-rollups/tests/test_outputs.py`

> Path("/logs/verifier/reward.txt").write_text("1\n" if actual == expected else "0\n")
> --- `experimental/harbor_meta_harness/tasks/dedupe-events/tests/test_outputs.py`

> Path("/logs/verifier/reward.txt").write_text("1\n" if actual == expected else "0\n")
> --- `experimental/harbor_meta_harness/tasks/reconcile-ledger/tests/test_outputs.py`

> result_files = list(job_dir.glob("*/result.json"))
> if len(result_files) != 1:
>     return ChildResult(0.0, "missing Harbor result", str(job_dir))
> --- `experimental/harbor_meta_harness/controller.py`

#### EPI-RTE-history-selection
Label: Pilot history reward selection
Part of: [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search)

Uploaded history JSON → accepted/non-null rewards and budget arithmetic → max reward or zero → outer Harbor reward file. Outer task verifier owns this disposition; it does not reopen candidate source or child jobs. SRC-1, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`, implementation.

- Immediate return: `/logs/verifier/reward.txt` scalar.
- Later read-back: inapplicable — this verifier does not implement subsequent candidate-history reload; external Harbor consumes its reward.
- Delegated visibility: Verifier sees report fields, not final source or independent run provenance.
- Selection predicate: Entries whose accepted field is truthy and reward non-null; remaining_budget equals budget minus history length; budget at least one; maximum reward.
- Invalidation or expiry: Missing/malformed input or invalid arithmetic gives zero; no source-digest or final-file invalidation check.
- Activation or effect: Sets enclosing task score, not selection/restoration of final harness code.
- Evidence limits: Arithmetic does not require nonnegative remaining budget or authenticate report entries. No observed forged report or deployed exploit is claimed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This checks report eligibility rather than harness truth; no independent answer oracle exists at this layer. The initial human chooses suite/budget, outer software normally writes report, final software decides scalar. Example deduction: budget 1, remaining_budget -1 and two history entries satisfies the stated arithmetic; this verifier is not itself an enforcing nonnegative-budget gate. Normal outer-tool budget enforcement is a separate route. Historical score acceptance grants no final-code authority or causal explanation; recovery is zero on specified parse/key/type failures, not code rollback.

> valid = (
>     report["remaining_budget"] == report["budget"] - len(history)
>     and report["budget"] >= 1
> )
> --- `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`

> reward = max(rewards, default=0.0) if valid else 0.0
> --- `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`

#### EPI-RTE-observation-filter
Label: Observation cleanup and truncation

Distinct numerical/text filtering mechanisms overlap [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) and the classification context account: this referent is their lossy model-visible evidence transformation, not another whole-loop route. It spans several supplied routes, so it has no single Part of relation. KIRA removes every output line containing any generated marker, pilot keeps stdout/stderr tails, classification keeps prompt head/tail. Code owns preferential removal; models receive the remainder. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`, `reference_examples/text_classification/llm.py`, implementation.

- Immediate return: Filtered/truncated text to the selected model call.
- Later read-back: inapplicable — these inspected filters do not themselves persist and later reload removed evidence; inherited summarization is a separate uninspected transformation.
- Delegated visibility: Pilot shell response contains last 12,000 characters per stream; classification prompt loses its middle above limit; KIRA loses complete marker-bearing lines before inherited output limiting.
- Selection predicate: Explicit substring deletion or character limits; no truth/evidence importance evaluator.
- Invalidation or expiry: Each observation/prompt transformation applies anew; no semantic correction, expiry or reload mechanism is implemented by these filters.
- Activation or effect: Delivered context differs from raw evidence; whether removed facts change actual model action is unobserved.
- Evidence limits: Exact summary fidelity and inherited output-limiter behavior unresolved; supplied source supports loss capacity, not a measured rate of errors.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete KIRA deduction: with marker set containing `m`, output `value=7 m\nnext=8` leaves `next=8` before inherited limiting, because the whole first line matches. A claim that cleanup preserves all substantive output is false even though protocol-token deletion is the intent. Prompt middle removal can erase a scope condition while retaining its surrounding claims; semantic preservation is indeterminate for arbitrary inputs, not guaranteed non-ampliative compression. Pilot tail truncation can similarly omit initial errors. The filters grant no epistemic endorsement. Cache replay uses normalized model/API/prompt/kwargs identity without backend weight identity, per [RT-CMP-classification-llm](runtime.md#rt-cmp-classification-llm); preserved cached text does not establish current endpoint truth or freshness.

> lines = [line for line in lines if not any(m in line for m in markers)]
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

> "stdout": (execution.stdout or "")[-12000:],
> "stderr": (execution.stderr or "")[-12000:],
> --- `experimental/harbor_meta_harness/agents/meta_harness.py`

> prompt = prompt[:half] + "\n\n... [TRUNCATED] ...\n\n" + prompt[-half:]
> --- `reference_examples/text_classification/llm.py`

### Claims

#### EPI-CLM-mechanism-tests
Label: Mechanism-first hypothesis tests

Doctrine requests one mechanism per terminal candidate and falsifiable classification hypotheses, using traces to target failure modes. This is a design claim about what the comparison intends to test, not a reported causal result. Distinct from [RT-CLM-fixed-model](runtime.md#rt-clm-fixed-model), which concerns the mutable boundary. SRC-1, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, doctrine/design.

> One mechanism per candidate. Each candidate tests exactly one hypothesis. If you're tempted to add "and also..." -- that's a second candidate.
> --- `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`

> Formulate 3 hypotheses — each must be falsifiable and target a different mechanism.
> --- `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`

The comparison can assess an expected outcome under its selected benchmark conditions, but one candidate identity and a score are not independent component variation or a checked explanation. Actual hypothesis formulation, source-change isolation, criticism and transfer remain unobserved. The parent runtime theory accounts separately retain the requested criticism, executable consumption and unavailable iteration evidence.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
