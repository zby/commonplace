---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Hyperagents' prediction, benchmark-checking and executable-reliance routes: what evaluation licenses and what recursive improvement remains unestablished."
run-id: AAS-2026-10-14-hyperagents-dd9d501b160c-01
reviewed-boundary: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
---

# Hyperagents epistemic report

## Source-and-claim boundary

The question is whether producing, evaluating and reusing code-modified agents also produces warranted knowledge about their answers, performance or improvement mechanisms. The target is the whole shipped builder or improvement plane, including its task callers, evaluators, archive, replay, selection and optional ensemble. Frozen evidence and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); sources resolve through its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. No target code was executed.

The consequential design claim is [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement). It requests evidence-responsive improvement of generating machinery; it does not itself claim a formal proof or universal answer verifier. [RT-CLM-bash-description](runtime.md#rt-clm-bash-description) is relevant to the warrant of advertised execution restrictions, not task-answer truth. No broader conclusion is imported from the unfrozen paper, blog or external logs.

Missing execution traces prevent attributing actual model evidence use, successful edits, accepted answers, effective recovery or improved capacity. Missing comparisons prevent causal attribution to editor changes, archive delivery, selection, or any component. Uninspected provider weights and external proof-grader/environment/test implementations prevent checking their accuracy, parameter provenance and hidden state. Reference labels enter as references with unknown source warrant; the implementation does not independently authenticate them. These limits do not negate the wired outcome checks and executable authority paths.

### Coverage

“Direct” means this analyst inspected SRC-1 source text; “supplied” means reliance on a cited runtime record and its retained passage. Added reads are at the registered commit, not new sources. Uninspected relevant detail prevents a system-complete negative about acceptance or criticism.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Generation CLI and mode dispatch | `generate_loop.py` | Direct CLI read; supplied [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle), [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission) | No execution; CLI exposure does not show exercised mode. |
| Initial editor, runner, domain reset and patch replay | `meta_agent.py`, `run_meta_agent.py`, `utils/git_utils.py`, `utils/gl_utils.py` | Supplied [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission), [RT-BAP-code-replay](runtime.md#rt-bap-code-replay) | Generated descendants can replace policies; initial checks are not adversarial integrity guarantees. |
| Registered tools and model dispatch | `agent/tools/__init__.py`, `agent/tools/bash.py`, `agent/tools/edit.py`, `agent/llm_withtools.py`, `agent/llm.py` | Direct loader read and directory listing: Bash and edit are the shipped tool modules; supplied [RT-RTE-model-tools](runtime.md#rt-rte-model-tools) | No separately registered acceptance hook established here; arbitrary Python/shell effects prevent inferring a universal fixed route set. |
| Task response extraction and tabular harness CLI, resume | `task_agent.py`, `domains/harness.py` | Direct full reads; supplied [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation); [EPI-OBJ-predictions](#epi-obj-predictions) | Fresh calls and cached predictions differ; no code-version invalidation is checked by the inspected cache rule. |
| Human-preference and grading reports | `domains/report.py`, `domains/search_arena/utils.py`, `domains/imo/grading_utils.py` | Direct reads; [EPI-RTE-label-normalization](#epi-rte-label-normalization), [EPI-RTE-label-scoring](#epi-rte-label-scoring) | Dataset correctness/curation not assessed; agreement is not independently established truth. |
| Proof generation and proof grading | `domains/report.py`, `domains/harness.py`, `domains/imo/proof_grading_utils.py`, `domains/imo/proof_eval.py` | Direct dispatch, formatter and report reads; [EPI-RTE-proof-grading](#epi-rte-proof-grading) | External `proofgrader.task_agent` implementation unavailable in SRC-1; formal soundness and actual grading accuracy unestablished. |
| BALROG action and report | `domains/balrog/evaluator.py`, `domains/balrog/eval.py`, `domains/balrog/utils.py` | Supplied [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects); direct report entry and complete aggregation-function reads; [EPI-RTE-outcome-summary](#epi-rte-outcome-summary) | Full environment internals uninspected; progress does not license an explanation of the action policy. |
| Genesis reward code, training and report | `domains/genesis/evaluator.py`, `domains/genesis/eval.py`, `domains/genesis/genesis_utils.py`, `domains/genesis/genesis_train/rl_trainer.py`, `domains/genesis/genesis_eval/rl_eval.py` | Supplied [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects), [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner); direct aggregation-function and report entry reads | Training dependency and metric implementations uninspected; no checkpoint/run evidence. |
| Polyglot task patch/tests | `domains/polyglot/harness.py`, `run_task_agent.py` | Supplied [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects) | Incompatible logging keyword on nonempty-patch path limits successful test-flow claims; tests cannot warrant general correctness. |
| Independent replay evaluation | `domains/run_eval.py` | Supplied runtime account, [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle) for contrasted generation flow | Independent replay lacks generation eligibility checks; no complete independent-entry audit here. |
| Score loading and host selection | `utils/gl_utils.py`, `utils/domain_utils.py` | Direct score reader/key dispatch; supplied [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection) | Missing/NaN score withdrawal is not removal of archived code. |
| Editable selector and saved-answer ensemble | `select_next_parent.py`, `ensemble.py`, `utils/run_select_next_parent.py`, `utils/run_ensemble.py` | Supplied [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers) | Split-specific score selection does not establish unseen-split generalization. |
| Bootstrap, DGM and no-selfimprove/no-archive alternatives | `setup_initial.sh`, `baselines/dgm/coding_agent.py`, `generate_loop.py` | Supplied runtime account and [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission); direct CLI exposure | Detailed DGM diagnosis semantics not inspected here; prevents universal negative about formulated criticism. |
| Post-generation analysis and transfer helpers | `analysis/plot_progress.py`, `analysis/visualize_archive.py`, `analysis/transfer_utils.py` | Included boundary paths, supplied runtime account only | Statistical/transfer consumers not directly assessed; no complete negative about downstream knowledge production. |

## Epistemic-object inventory

Each row identifies a material operative part. Executable code and natural-language guidance remain separate from answer and measurement propositions. Provider and RL numerical state have no individuated truth-apt propositions established by the accessible sources.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-predictions](#epi-obj-predictions) | Paper outcome/preference/grade or mathematical proof answer; whether correct is domain-dependent | see record | SRC-1, `task_agent.py`, `domains/harness.py` | JSON extraction is not semantic verification; cached output may precede current code. |
| [EPI-OBJ-report](#epi-obj-report) | Dataset agreement rate and failed/passed question IDs | see record | SRC-1, `domains/report.py` | Truth of input labels is not established. |
| [EPI-OBJ-proof-grades](#epi-obj-proof-grades) | Grader judgment and arithmetic points proportion | see record | SRC-1, `domains/imo/proof_eval.py` | Judgment is not a proof certificate; unknown label becomes zero. |
| [EPI-OBJ-outcome-reports](#epi-obj-outcome-reports) | Aggregated episode progression or robot fitness over configured trials | see record | SRC-1, `domains/balrog/utils.py`, `domains/genesis/genesis_utils.py` | Failed/missing-trial conventions are part of the statistic, not observed physical performance. |
| [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch) | Executable change; any truth-apt comments/rationale not determinable without candidate evidence | see record | SRC-1, `run_meta_agent.py` | Code behavior is not automatically a formulated explanation of improvement. |
| [RT-OBJ-metadata](runtime.md#rt-obj-metadata) | Recorded execution/admission flags and lineage identifiers | see record | SRC-1, `generate_loop.py` | `valid_parent` has operational meaning, not certification of improvement. |
| [RT-OBJ-readme](runtime.md#rt-obj-readme) | Design instructions and objective; successful improvement is not established | see record | SRC-1, `utils/gl_utils.py` | Possible read through tools is not observed evidence consumption. |
| [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models) | Not determinable: opaque parameters | see record | SRC-1, `agent/llm.py` | No inspected parameter update or verified exact weight version. |
| [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner) | Not determinable: numerical policy, not localized proposition | see record | SRC-1, `domains/genesis/genesis_train/rl_trainer.py` | Parameters intended to change; no run-produced checkpoint registered. |
| [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects) | BALROG action: policy output, not necessarily truth-apt; Genesis reward code: production machinery; Polyglot patch: executable candidate | see record | SRC-1, `domains/balrog/evaluator.py`, `domains/genesis/evaluator.py`, `domains/polyglot/harness.py` | Container record covers distinct effects, not one epistemic object or oracle. |

## Authority-route ledger

Every row is an independently assessed consequential function. Shared implementation citations recur where checks, disposition, retention and consumption differ. Fields owned by the cited records are marked `see`. All implemented rows lack observed activation in this boundary.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation) | content transformation | implemented | [EPI-OBJ-predictions](#epi-obj-predictions) | truth-apt transformation: acquisition/import | Reference and task-input loading | CSV and formatter; label/preference domains | see route | External content loaded | Supplies task inputs and report references | Source warrant unknown | Permits inference and comparison | Harness/formatter to model; input supply; current task | SRC-1, `domains/harness.py` | none | none | No reference provenance validation. |
| [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation) | content transformation | implemented | [EPI-OBJ-predictions](#epi-obj-predictions) | truth-apt transformation: indeterminate | Task input to answer/proof | Provider plus response extraction; task domain | see route | Candidate answer or `None` | Candidate generation | No acceptance from fluency or JSON | Supplies candidate to report | Task model to CSV/report; candidate supply; trial and later reuse | SRC-1, `task_agent.py` | none | none | Could conjecture, derive or reshape; no concrete response establishes which. |
| [EPI-RTE-label-normalization](#epi-rte-label-normalization) | content transformation | implemented | [EPI-OBJ-predictions](#epi-obj-predictions) | truth-apt transformation: non-ampliative reshaping | Label spelling | see route | Before match | Lowercase trimmed string | Enforces comparison convention | Only equivalence under this spelling convention | Changes score input | Report string processor; enforcing; this report | SRC-1, `domains/report.py` | none | none | Arbitrary proof prose not covered by label equivalence. |
| [EPI-RTE-label-scoring](#epi-rte-label-scoring) | check/evidence production | implemented | [EPI-OBJ-report](#epi-obj-report) | truth-apt transformation: entailed derivation | Candidate-label agreement | see route | After prediction CSV exists | Match flags, rates, error statistic | Measurement | Conditional arithmetic over supplied rows | Enables staged evaluation and score selection | see [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection); ranking/permissive; later generations | SRC-1, `domains/report.py` | none | none | Does not independently validate label truth or mechanism. |
| [EPI-RTE-proof-grading](#epi-rte-proof-grading) | check/evidence production | implemented | [EPI-OBJ-proof-grades](#epi-obj-proof-grades) | truth-apt transformation: indeterminate | Candidate mathematical proof | External grader with problem, solution and guidelines; see route | After proof generation | Grade judgment | Model-mediated grading input to score | Unknown grader accuracy; no formal validity license | Produces host-consumed score | Grader to report to selector; ranking; later rounds | SRC-1, `domains/report.py` | none | none | Model judgment is not independently verified acceptance. |
| [EPI-RTE-proof-grading](#epi-rte-proof-grading) | content transformation | implemented | [EPI-OBJ-proof-grades](#epi-obj-proof-grades) | truth-apt transformation: entailed derivation | Grade labels to points proportion | Fixed map 0/1/6/7, unknown zero; see route | After grading | Points percentage | Fixed symbolic aggregation | Arithmetic on grader labels only | Makes score available | Report to host score loader; measurement; later rounds | SRC-1, `domains/imo/proof_eval.py` | none | none | No inference from high grade to formal soundness. |
| [EPI-RTE-outcome-summary](#epi-rte-outcome-summary) | check/evidence production | implemented | [EPI-OBJ-outcome-reports](#epi-obj-outcome-reports) | truth-apt transformation: entailed derivation | Episode progress or fitness logs | Two domain-specific aggregation rules; see route | After trials | Progress/fitness report | Measurement | Conditional descriptive statistic | Permits domain score consumption | Report to host; ranking/permissive; later rounds | SRC-1, `domains/balrog/utils.py`, `domains/genesis/genesis_utils.py` | none | none | Different missing-trial conventions; metric fidelity uninspected. |
| [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects) | check/evidence production | implemented | see route | no content change | BALROG action validity, Polyglot patched solution tests | Environment rules or test exit; see route | Before step or after test restore | Rejection/feedback or test result | Local gating/measurement | Action legality or tested behavior only | Allows step or supplies resolution result | see route; enforcing within trial | SRC-1, `domains/balrog/evaluator.py`, `domains/polyglot/harness.py` | none | none | Polyglot logging defect; no general correctness or actual outcome. |
| [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission) | disposition/acceptance | implemented | [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch) | no content change | Edited code eligibility for evaluation/reuse | Nonempty diff/import checks and metadata; see route | After edit; before evaluation/reuse | Admit or suppress evaluation | Permissive/veto | Importability and eligibility, not improvement acceptance | Allows edited task execution and possible lineage reuse | see [RT-BAP-code-replay](runtime.md#rt-bap-code-replay); permissive then executable; later rounds | SRC-1, `generate_loop.py` | [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement) | operational-not-epistemic | Neither exceeding parent score nor independent successful score is universally required. |
| [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation) | retention | implemented | [EPI-OBJ-predictions](#epi-obj-predictions), [EPI-OBJ-report](#epi-obj-report) | no content change | CSV/report persistence | File checkpoint/write; see route | During/after evaluation | Saved candidates and scores | Durable storage | Retention is not acceptance | Cached non-NA prediction suppresses new inference | CSV to harness/report/ensemble; enforcing skip or answer reuse; later invocation | SRC-1, `domains/harness.py`, `domains/report.py` | none | none | Reuse not bound here to candidate code version. |
| [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle) | retention | implemented | [RT-OBJ-metadata](runtime.md#rt-obj-metadata), [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch) | no content change | Archive and lineage persistence | Append/save; see route | Every generated node | Retained failed or successful node | Durable storage | No successful-agent certification | Makes later replay/resume possible | see [RT-BAP-code-replay](runtime.md#rt-bap-code-replay) and [RT-BAP-selector-flags](runtime.md#rt-bap-selector-flags) | SRC-1, `utils/gl_utils.py` | [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement) | none | Archive append is not lifecycle integration after epistemic acceptance. |
| [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-report](#epi-obj-report), [RT-OBJ-metadata](runtime.md#rt-obj-metadata) | no content change | Score-based successor and staged continuation | see route; missing/NaN score returns None | Staged gate and later selection | Full-evaluation gate or selected ID | Ranking/permissive, with fallback | Scores describe evaluated domain/split; not expected future gain | Changes exploration lineage; may continue without scored candidates | Host score reader/selector to replay; ranking then executable; next round/resume | SRC-1, `utils/gl_utils.py` | [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement) | score-not-warrant | Withdrawing a score does not erase patch or archive; initial/fallback exceptions remain. |
| [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers) | operational admission/selection/consumption | implemented | [EPI-OBJ-predictions](#epi-obj-predictions), [EPI-OBJ-report](#epi-obj-report) | truth-apt transformation: acquisition/import | Ensemble saved answer | Highest archived split score; see route | Requested ensemble trial | Existing prediction returned | Answer selection | Inherits candidate's unknown warrant, not fresh validation | Uses selected saved answer as ensemble prediction | Ensemble to report/selection; answer supply/ranking; requested split and later rounds | SRC-1, `ensemble.py` | none | split-selection-limit | Validation/test-score selection can condition answers on those same splits. |
| [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers) | disposition/acceptance | implemented | [RT-OBJ-metadata](runtime.md#rt-obj-metadata) | no content change | Editable selector reuse | Exception disables selector node, retry earlier eligible source; see route | On optional selector failure | Flag veto/retry | Operational veto | No claim-truth adjudication | Stops reuse of failing selector code source | Wrapper flags to code-source chooser; enforcing; later optional invocations | SRC-1, `generate_loop.py` | none | none | Node can remain archived; retry is operational recovery. |
| [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission) | behavior/policy adaptation | implemented | [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch) | non-truth-apt policy/content update: executable code editing | Task/editor/tools/optional policies | Model proposes; host admits; see route | Editing and later replay | Changed executable machinery | Executable | No mechanism explanation licensed by outcome score | Can change future generation and task behavior | see [RT-BAP-code-replay](runtime.md#rt-bap-code-replay) | SRC-1, `meta_agent.py`, `utils/gl_utils.py` | [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement) | none | Evidence responsiveness requested, actual update determination and benefit unobserved. |
| [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects) | behavior/policy adaptation | implemented | [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner) | non-truth-apt policy/content update: trained numerical policy | Genesis generated reward/training | Training process and training-success gate; see route | Before checkpoint evaluation | Policy checkpoint and fitness trial | Training/executable policy | Not a localized accepted claim | Allows learned policy to control simulated robot | Reward code to trainer/checkpoint to inference policy; executable; trial/checkpoint reuse | SRC-1, `domains/genesis/genesis_train/rl_trainer.py` | none | none | Algorithm and run-produced weights uninspected; capacity improvement not established. |
| [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission) | lineage/freshness/recovery | implemented | [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch) | no content change | Domain reset and patch application | Post-edit reset/filter and checked replay; see route | After editing and before inherited execution | Restoration, replay or failure | Best-effort path policy/protocol | Does not guarantee evaluator independence | Limits inherited domain changes on covered path; cleanup attempts reset | Runner/replay host to worktree; enforcing attempt; round | SRC-1, `run_meta_agent.py`, `utils/gl_utils.py` | none | dependency-integrity-limit | Mutable dependencies outside domains and direct entries defeat a universal evaluator-protection claim. |

No lifecycle-integration route after an evidence-consuming acceptance of an explanatory improvement claim is established by these inspected paths. This is a bounded finding about the ledger, not a system-complete absence: DGM diagnosis, generated descendants, analysis consumers and opaque inference remain independently unresolved. Outcome checks, operational admissions and numerical adaptation remain positive findings.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement) | Improve agents and their generating mechanisms using earlier results | SRC-1, `utils/gl_utils.py`; doctrine/design | see claim | [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission), [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection), [RT-BAP-code-replay](runtime.md#rt-bap-code-replay) | None registered | No comparison or update-dependence trace; fallback/admission exceptions and editable dependencies limit score-based warrant | Improvement-directed self-change is wired; score feedback can select live code, but neither successful improvement nor an accepted explanation follows | Actual evidence-responsive proposal determination and later causal dependence unknown; answer success cannot certify editor mechanism. |
| [RT-CLM-bash-description](runtime.md#rt-clm-bash-description) | No internet and persistent shell state | SRC-1, `agent/tools/bash.py`; doctrine/design | see claim | [RT-RTE-model-tools](runtime.md#rt-rte-model-tools) | None registered | Host networking and newly constructed sessions contradict stronger implementation guarantees | Tool description has advisory force, not established network denial or cross-call shell-state persistence | Files can persist; session variables/cwd are a separate unsupported claim. |

## Bounded conclusion

Hyperagents implements candidate production, benchmark checking and consequential reuse, not merely a passive result archive. Tabular references are acquired with unknown source warrant. Candidate answers are normalized and compared to labels; the resulting agreement propositions are arithmetic deductions conditional on those inputs, not independent confirmation of source truth. IMO proof judgments come from an external grader and become points through a fixed map, not through inspected formal verification. BALROG progress, Genesis fitness and Polyglot tests retain distinct targets and limits; none warrants the explanation or transfer of the producing mechanism.

The material criteria grant operational authority. Nonempty patches and imports enable evaluation; staged positive scores can enable fuller evaluation; metadata and scores usually determine candidate reuse. Their intended scope is benchmark search, not acceptance of an explanatory claim. Starting nodes, fallback, the non-None meta-patch condition and independent replay prevent reading that admission as a universal successful-evaluation requirement. Scores can be withdrawn as missing while code remains archived. Selector failure can veto future use of that selector source without deleting it. Post-edit domain restoration and cleanup are best effort and do not establish evaluator integrity against editable dependencies.

Retained patches enter later executable behavior through replay and imports. Retained answers can suppress new task calls or become ensemble answers; retained scores influence lineage selection. Those are different behavioral-authority paths. Copying evaluations for possible editor inspection does not establish model evidence consumption. There is no supplied accepted explanatory conjecture connecting an outcome to a specific edit mechanism, no checked transfer argument, and no observed causal improvement. Provider numerical content cannot be individuated as truth-apt propositions here. Genesis explicitly wires numerical policy training and checkpoint evaluation, independently of natural-language knowledge acceptance.

The recursive-improvement objective therefore has a live dispositional code-change path and benchmark feedback, while exercised evidence-responsive self-improvement and improved future capacity remain unestablished. Localized explanation, content-directed criticism, iteration of criticism and reflective theory-building are not inferred from score selection; uninspected diagnosis and opaque processing prevent turning that limit into a system-wide negative. No single epistemic score or universal oracle follows.

## Shared records

### Operative objects

#### EPI-OBJ-predictions
Label: Task predictions

Part of: [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

This object is the candidate-output part of the supplied evaluation route, not a replacement for the route's control flow. Source-native identity: `prediction` cells in `predictions.csv`, produced from TaskAgent's response. Representational form: natural-language answer/proof content; label strings also undergo fixed symbolic comparison. Storage substrate: CSV files and current task return. SRC-1, `task_agent.py`, `domains/harness.py`. The formatter imports task data; model response generation and extraction establish candidate production, not a semantic-preservation or entailment relation. Existing non-NA cells can be reused without current inference.

> prediction = extracted_jsons[-1]['response']
> --- `task_agent.py`

> existing_df[~existing_df["prediction"].isna()][question_id_col]
> --- `domains/harness.py`

#### EPI-OBJ-report
Label: Label agreement report

Part of: [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

This is the measurement-output part of the supplied route. Source-native identity: `report.json`, `overall_accuracy`, failed/passed question IDs and IMO-grading `normalized_mean_absolute_error`. Representational form: symbolic JSON numerics and lists. Storage substrate: evaluation output directory. SRC-1, `domains/report.py`. Scope is conditional agreement with the given row labels, not general truth or causal evidence of improvement. Distinct from control metadata [RT-OBJ-metadata](runtime.md#rt-obj-metadata): these values measure candidates rather than flagging permission.

> "overall_accuracy": float(accuracy),
> --- `domains/report.py`

#### EPI-OBJ-proof-grades
Label: Proof grading outputs

No counterpart after comparison with supplied operative objects: proof-grader judgments and points summaries differ from executable patches, control metadata and README guidance. They share CSV transport with [EPI-OBJ-predictions](#epi-obj-predictions), but have a separate producer/check target and missing oracle implementation. Source-native identity: grading `predictions.csv` and `report.json` with `points_percentage` and `correct_percentage`. Representational form: natural-language categorical judgments plus symbolic point map/report. Storage substrate: grading subdirectory and report moved to proof-output directory. SRC-1, `domains/report.py`, `domains/imo/proof_eval.py`. No ground-truth grade comparison is supplied by this formatter.

> GROUND_TRUTH_KEY = None  # Ground truth does not exist
> --- `domains/imo/proof_grading_utils.py`

#### EPI-OBJ-outcome-reports
Label: Environment outcome reports

Part of: [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)

These are the measured-result parts of the supplied domain route, not its action/code/checkpoint parts. Source-native identity: BALROG `average_progress` and Genesis `average_fitness` in their separate `report.json` files. Representational form: symbolic JSON numbers with domain-specific meanings. Storage substrate: evaluation output folders. SRC-1, `domains/balrog/utils.py`, `domains/genesis/genesis_utils.py`. Both support conditional descriptive outcomes, not a shared evaluator domain. Separate ledger targets preserve their different rules. Reports are distinct from [EPI-OBJ-report](#epi-obj-report), which compares answers to reference labels.

> "average_progress": 100 * overall_avg_progression,
> --- `domains/balrog/utils.py`

> "average_fitness": np.mean(all_fitness_scores),
> --- `domains/genesis/genesis_utils.py`

### Routes

#### EPI-RTE-label-normalization
Label: Label normalization

Part of: [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

Endpoints/progression: CSV prediction/reference strings → trim/lowercase → equality operands. Owner: `domains/report.py`. SRC-1 implementation. This part changes spelling without proposing a new task proposition under the report's case/whitespace equivalence convention. Concrete deduction without execution: prediction ` Correct ` and reference `correct` both become `correct`, giving equality true; prediction `partial` remains different. This inference is about deterministic implementation, not an observed task result. No acceptance hook occurs in this transformation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized dataframe columns for the next comparison.
- Later read-back: inapplicable — these temporary columns are not separately persisted; the report result has later consumers.
- Delegated visibility: Equality/metric code receives normalized strings, not raw spelling distinctions.
- Selection predicate: Rows with prediction not equal to empty string; this comparison alone is not a pandas missing-value check.
- Invalidation or expiry: Temporary state ends with the report process; source CSV remains.
- Activation or effect: Normalization determines which labels compare equal.
- Evidence limits: No proof that arbitrary answer semantics are preserved; equivalence is bounded to label spelling.

> df["prediction"] = df["prediction"].str.strip().str.lower()
> df[ground_truth_key] = df[ground_truth_key].str.strip().str.lower()
> --- `domains/report.py`

#### EPI-RTE-label-scoring
Label: Label scoring

Part of: [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

Endpoints/progression: normalized prediction/reference columns → row matches and statistics → JSON report → host score reader. Owner: report program; dataset supplies reference outcome, and task model proposes the answer. No per-answer human approval is implemented by this scoring step. Target: agreement on paper review, search preference or IMO-grading rows, not source-label truth. Operating mode: bounded benchmark, staged/full according to outer host. The deterministic report derives arithmetic propositions conditional on its CSV. Agreement licenses reporting that statistic; it does not accept an explanatory improvement hypothesis. For IMO grading the category-to-point map adds normalized absolute error; the driver selects `overall_accuracy` rather than that error statistic.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Report dictionary/path with match rates and row IDs.
- Later read-back: Host loads the JSON score for staged/full decisions and parent/ensemble selection; evaluations can be copied to future editors.
- Delegated visibility: Report receives answer and reference columns; selector receives domain score, not a checked explanation.
- Selection predicate: Domain-specific reference key; fixed normalized equality, with grading error map 0/1/6/7.
- Invalidation or expiry: Missing or NaN host score is withheld; report/CSV is not automatically erased.
- Activation or effect: Score can gate full evaluation and rank/filter future lineages, as [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection) establishes.
- Evidence limits: Reference correctness and exercised effects uninspected; no parent-improvement acceptance criterion.

SRC-1, `domains/report.py`, `utils/domain_utils.py`, `utils/gl_utils.py`.

> df["match"] = df[ground_truth_key] == df["prediction"]
> --- `domains/report.py`

> accuracy = df["match"].mean()
> --- `domains/report.py`

> if domain in ["search_arena", "paper_review", "imo_grading"]:
>         return "overall_accuracy"
> --- `utils/domain_utils.py`

#### EPI-RTE-proof-grading
Label: Proof grading

No counterpart after comparison: this is an additional domain evaluator selected by the supplied tabular machinery, not equivalent to [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)'s reference-label match or [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)'s environment/test checks. Endpoints/progression: produced proof CSV → harness copies prediction into `Response` → external `proofgrader.task_agent` receives problem, solution, grading guidelines and student answer → grade CSV → fixed point-map report → move report into proof-output directory → host score reader. Owners: shipped harness/report control routing, external grader judges, arithmetic report computes points. Target/domain: mathematical proof adequacy under supplied grading guidelines. Reference solution/guidelines are provided; model judgment is not an independently inspected answer oracle. No formal checker is established by this route. Operating mode: bounded proof benchmark, not open-ended acceptance of explanations. No per-proof human veto shown by these callers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Grading folder followed by points/correctness proportion report for nonempty input.
- Later read-back: Host reads `points_percentage` to score/rank proof agents; copied outputs may later guide editors.
- Delegated visibility: Grader receives candidate response and problem/solution/guidelines, not a locally checked proof certificate.
- Selection predicate: Grader TaskAgent loading followed by literal label map incorrect=0, partial=1, almost=6, correct=7; unknown labels become zero.
- Invalidation or expiry: Empty input returns before writing report; missing report can yield withheld host score. No correctness-based deletion of candidate proof is implemented here.
- Activation or effect: Grade aggregation supplies a score consumed in generation selection; successful invocation and accurate grading are not observed.
- Evidence limits: Grader implementation and reference provenance absent from registered source; formal validity, encoding fidelity and actual proof correctness remain unknown.

SRC-1, `domains/report.py`, `domains/harness.py`, `domains/imo/proof_grading_utils.py`, `domains/imo/proof_eval.py`, `utils/domain_utils.py`.

> domain="imo_proof_grading",
>         agent_path="proofgrader.task_agent",
> --- `domains/report.py`

> dataset["Response"] = dataset["prediction"].copy()
> --- `domains/harness.py`

> .map({"incorrect": 0, "partial": 1, "almost": 6, "correct": 7})
>         .fillna(0)
>         .astype(float)
> --- `domains/imo/proof_eval.py`

> points_percentage = preds.sum() / (MAX_POINTS * total)
> --- `domains/imo/proof_eval.py`

#### EPI-RTE-outcome-summary
Label: Outcome summary

Part of: [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)

Endpoints/progression: domain episode/fitness JSON and expected task counts → domain-specific aggregation → report JSON → host score loader/selection. Owners: BALROG and Genesis summary programs. These are two measurement subpaths with the same downstream role, not one oracle. Target/domain: configured environment progression trials versus robot-policy fitness trials. BALROG uses expected counts in progression denominators and adds discovered missing tasks as zero; whole environments without summaries are not thereby witnessed. Genesis averages each run's fitness values and pads missing configured run counts with zeros before the final mean. Values are conditional on the logs and failure convention. In Genesis the field named `standard_error` is computed with `np.std`, so the source-native label alone cannot establish a standard error of the mean. Task model proposes actions/reward code, environment/training produces outcomes, program computes report, host decides next lineage. Human contribution is setup/domain choice, not per-result acceptance. Benchmark scores are reference outcomes, not expected correct answers to code improvement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Saved report; BALROG collector returns summary, Genesis collector prints it without an explicit return.
- Later read-back: `get_score` loads domain report key for later parent selection and copied evaluation evidence.
- Delegated visibility: Aggregator receives persisted logs/configuration; host gets numeric outcome, not causal explanation.
- Selection predicate: Domain directory/JSON selection and expected-trial rules; host withholds missing/NaN or empty-environment BALROG results.
- Invalidation or expiry: Failed/missing Genesis trials can contribute zero; missing host report is withheld. No archive deletion follows automatically.
- Activation or effect: Report numbers can rank or filter code lineages via [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection).
- Evidence limits: Environment/fitness metric fidelity and experiment operation uninspected; descriptive fitness does not identify a component effect.

SRC-1, `domains/balrog/utils.py`, `domains/genesis/genesis_utils.py`, `utils/gl_utils.py`.

> sum(env_episode_progress) / env_total_episodes
> --- `domains/balrog/utils.py`

> task_to_runs[task_name] += [0] * (expected_count - len(task_to_runs[task_name]))
> --- `domains/genesis/genesis_utils.py`

> "standard_error": np.std(all_fitness_scores),
> --- `domains/genesis/genesis_utils.py`

> return score
>     except Exception:
>         return None  # If score is missing or file not found
> --- `utils/gl_utils.py`
