---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Agent-R epistemic routes: environment outcome checks, model critique, synthetic revision examples and the limits of iterative-training warrant."
run-id: AAS-2026-10-12-agent-r-216224d4270a-01
reviewed-boundary: "82fcc1ca7873b460949ed49022146dd988c32e31"
---

# Agent-R epistemic report

## Source-and-claim boundary

The question is what licenses Agent-R's action judgments and revision examples, and how those judgments reach later behavior. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. The selected target is the shipped builder/improvement plane, with a complete artifact but partial training loop. External environment semantics, model checkpoints and Xtuner are not inspected implementations here.

The consequential claim is see [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training): first-error identification, same-parent successful continuation, reflection and iterative self-training. The bounded comparison below concerns that claim, not the external paper or diagram-specific assertions. No target was executed. A saved example was not supplied, so no route is classified as exercised merely because its constructor exists.

| Entry point or operation | SRC-1 source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Collection task dispatch, actor calls, persistence | `mcts_collection.py`; `mcts_utils/webshop/mcts_ws.py`; `mcts_utils/mcts_raw.py` | Direct full reads; see [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), [EPI-RTE-reward-check](#epi-rte-reward-check) | Environment correctness and reset/replay equivalence are external contracts, not checked here. |
| TextCraft and SciWorld collection variants | `mcts_utils/textcraft/mcts_tc.py`; `mcts_utils/sciworld/mcts_sci.py` | Supplied runtime full inspection; own scoped searches for score, reset, step and substitution calls; see [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), [RT-RTE-sciworld-action](runtime.md#rt-rte-sciworld-action) | Variant conclusions rely on supplied records, not a new full direct read. |
| Current SciWorld action substitution | `mcts_utils/sciworld/eval_utils_sw.py` | Direct read through entire `findValidActionNew`; see [RT-RTE-sciworld-action](runtime.md#rt-rte-sciworld-action) | Lexical substitution is not a task-success or all-actions-valid certificate. |
| Revision CLI, threshold filters, critique, splice and append | `path_collection.py`; `mcts_utils/llm_server.py` | Direct full reads; see [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), [EPI-RTE-critique-check](#epi-rte-critique-check), [EPI-RTE-prefix-disposition](#epi-rte-prefix-disposition), [EPI-RTE-conversation-splice](#epi-rte-conversation-splice) | Float/string comparisons block nonempty export paths when reached; successful export is unobserved. |
| Sequential evaluation and supplied-prefix helper | `eval.py`; `mcts_utils/llm_server.py` | Direct full reads; see [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation) | Missing `test_id/` prevents unchanged-CLI runnability; no checkpoint comparison or intervention evidence. |
| API alternative and local weights | `mcts_utils/llm_server.py` | Direct full read; see [RT-RTE-provider-alternate](runtime.md#rt-rte-provider-alternate), [RT-CMP-func-call-offline](runtime.md#rt-cmp-func-call-offline), [RT-CMP-func-call](runtime.md#rt-cmp-func-call) | Provider/model internals and exact weight identities are uninspected. |
| Exposed dataset rewriter | `mcts_utils/llm_server.py` | Direct `rewrite`, `expand_dataset` and I/O reads; new [EPI-RTE-dataset-rewrite](#epi-rte-dataset-rewrite) | Callable helper, not CLI-wired; optimizer handling of its format remains unknown. |
| Other SciWorld helpers and standalone utilities | `mcts_utils/sciworld/eval_utils_sw.py`; `mcts_utils/sciworld/data_utils_sw.py` | Scoped definition/call searches only beyond the supplied/current validity route: prompt construction, history cleaning, model generation, action conversion and `__main__` helpers remain unassessed | Available but uninspected, not absent. Prevents a system-complete negative about all auxiliary knowledge/criticism routes. |
| Task JSON contents and method graphics | `mcts_utils/webshop/webshop_test.json`; `mcts_utils/textcraft/textcraft_test.json`; `mcts_utils/sciworld/sciworld_test.json`; `assets/method.png`; `assets/method.pdf` | No content assessment; shipped selectors assessed via runtime and driver reads | No claim about dataset representativeness, reference-answer contents or diagram-specific method warrant. |
| Training and checkpoint admission | `README.md` | Direct full read and tracked-tree enumeration; see [RT-ABS-training-machinery](runtime.md#rt-abs-training-machinery) | Advertised configuration absent; actual ingestion, optimization, acceptance and later deployment cannot be traced. |

Before settling the comparison, countercases were checked: `good` mode and `--revise 0` bypass critique; `uncertain` continues rather than rejects; a string containing `good` can continue despite negative language; terminal leaves can be budget stops rather than successes; all distinct paths can be paired rather than same-parent siblings; and `rewrite` removes loss flags. These are implementation findings, not observed failures. Relevant records below retain the passages. No supplied fact needs supersession: new declarations split material functions or add the omitted rewriter without replacing the runtime containers.

## Epistemic-object inventory

The mixed tree and exported row are not each given one epistemic status. Their model text, environment report, numerical aggregate and synthetic conversation parts have different lineage and consumers.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-env-score](#epi-obj-env-score) | External reports of current state, reward and completion; stored value/visits quantify sampled outcomes | Outcome evidence for branch and path ranking | SRC-1, `mcts_utils/webshop/mcts_ws.py`; see record | Reward is not a correctness proof for every thought or action; negative rewards are clamped. |
| [EPI-OBJ-revision-feedback](#epi-obj-revision-feedback) | Requested claim that this action helps, harms, or is uncertain for this task, plus reasons | First-error localization | SRC-1, `path_collection.py`; `mcts_utils/llm_server.py`; see record | Actual text unavailable; model compliance, truth and calibration unknown. |
| [EPI-OBJ-revise-log](#epi-obj-revise-log) | Copied observations/thoughts plus inserted error admission and synthetic wait acknowledgement | Corrective training conversation | SRC-1, `path_collection.py`; see record | Splice is not verified as one executable trajectory. |
| [EPI-OBJ-conversation](#epi-obj-conversation) | Reindexed message contents in training-shaped fields | Dataset conversion output | SRC-1, `mcts_utils/llm_server.py`; see record | Drops metadata distinguishing loss eligibility, feedback and path provenance. |
| [RT-CMP-func-call-offline](runtime.md#rt-cmp-func-call-offline) | Specific internal truth-apt propositions not determinable from accessible weights or source | Local actor/verifier | SRC-1, `mcts_utils/llm_server.py`; see component | Fixed inference parameters do not demonstrate learned knowledge or reliable judgment. |
| [RT-CMP-func-call](runtime.md#rt-cmp-func-call) | Specific internal truth-apt propositions not determinable | Injectable hosted alternative | SRC-1, `mcts_utils/llm_server.py`; see component | Mutable endpoint identity and provider state uninspected; not selected by shipped CLI. |

Actor responses may include truth-apt thoughts, but action commands themselves are behavioral proposals. Without response instances their semantic relation to input evidence remains indeterminate. The model-action consumer is see [RT-BAP-model-action](runtime.md#rt-bap-model-action), not an epistemic acceptance gate.

## Authority-route ledger

Compact records below are the sparse overlay. Fields owned by canonical records are cited rather than duplicated. Architectural status describes inspected wiring, not successful invocation. Each check is separated from its disposition.

Route ID: [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-env-score](#epi-obj-env-score); actor text in the cited tree container.
Content/update relation: truth-apt transformation: acquisition/import for environment state/outcome reports; source warrant unknown. Actor propositional generation is truth-apt transformation: indeterminate; commands are non-truth-apt policy/content update: action proposals.
Transition or check target: see route; environment reports enter branch histories and sampled outcomes.
Evaluator/condition and domain: no additional source-truth evaluator at import; the external task server's semantics are uninspected.
Activation and timing: see route.
Possible or observed result: see route; no observed instance.
Implemented force: stores reports; model proposals can execute before any retrospective critique.
Epistemic authority and scope: attributed task-environment reports only, not independent authentication.
Operational authority: behavior permitted, blocked, or changed: see route and [RT-BAP-model-action](runtime.md#rt-bap-model-action).
Behavioral-authority path: consumer, channel, force, horizon: see cited route and behavioral-authority record.
Evidence source ID and local anchor: SRC-1, `mcts_collection.py`; `mcts_utils/webshop/mcts_ws.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: none.
Gap/limit: reset/replay is not a test that copied history and reconstructed state agree; model-call trimming omits history while stored nodes retain full context.

Route ID: [EPI-RTE-reward-check](#epi-rte-reward-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-env-score](#epi-obj-env-score).
Content/update relation: truth-apt transformation: acquisition/import; external score warrant unknown.
Transition or check target: task outcome after a particular action sequence, not the agent's explanatory mechanism.
Evaluator/condition and domain: see record; external environment reward/done within the selected benchmark task.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: returns evidence to score processing, not an acceptance decision about every proposition.
Epistemic authority and scope: conditional outcome evidence, bounded by unknown reward semantics and replay correctness.
Operational authority: behavior permitted, blocked, or changed: subsequent selector and stop rules consume it.
Behavioral-authority path: consumer, channel, force, horizon: adapter terminal handling and MCTS backpropagation, numerical fields, ranking/enforcing, current search.
Evidence source ID and local anchor: SRC-1, `mcts_utils/webshop/mcts_ws.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: outcome-to-process limit.
Gap/limit: no successful run, reference solution or component contrast supplied.

Route ID: [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-env-score](#epi-obj-env-score).
Content/update relation: no content change.
Transition or check target: next search branch and termination; exact-response duplicate retention.
Evaluator/condition and domain: see route; symbolic visit/value/exploration rules, random ties and terminal flags.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: branch selection and terminal exclusion; response deduplication after candidate actions have executed.
Epistemic authority and scope: prioritization under sampled outcomes, not a claim-truth acceptance criterion.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route; selector reads counters within the current search.
Evidence source ID and local anchor: SRC-1, `mcts_utils/mcts_raw.py`; `mcts_utils/webshop/mcts_ws.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: none.
Gap/limit: average value ranks sampled terminal rewards; it does not establish all future branches' success or action-local causality.

Route ID: [RT-RTE-sciworld-action](runtime.md#rt-rte-sciworld-action)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: actor command and current environment action set; see route.
Content/update relation: non-truth-apt policy/content update: lexical action substitution.
Transition or check target: proposed SciWorld command, not factual truth or task usefulness.
Evaluator/condition and domain: see route; exact/token overlap against a modified environment candidate set.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: replaces command before the new step, but does not universally reject invalid actions.
Epistemic authority and scope: none for correctness of a rationale; bounded compatibility heuristic only.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route; environment step consumes replacement immediately.
Evidence source ID and local anchor: SRC-1, `mcts_utils/sciworld/eval_utils_sw.py`.
Claim IDs or none: none.
Mismatch marker or none: no universal-validity license.
Gap/limit: hard-coded doors, zero-overlap fallback, and bypass by replay/other adapters defeat an all-actions-valid interpretation.

Route ID: [EPI-RTE-critique-check](#epi-rte-critique-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-revision-feedback](#epi-obj-revision-feedback).
Content/update relation: truth-apt transformation: indeterminate; requested action-usefulness assessment, actual semantic content unobserved.
Transition or check target: current action's usefulness for a supplied task, given preceding action/observation text and current observation.
Evaluator/condition and domain: see record; local model prompted with helpful/harmful/uncertain categories.
Activation and timing: see record; reachable as a callable helper, CLI upstream comparisons defective.
Possible or observed result: see record.
Implemented force: generates reasons and judgment text for a separate consumer; no certified categorical parse.
Epistemic authority and scope: model opinion under partial context, not a correctness oracle.
Operational authority: behavior permitted, blocked, or changed: supplied to [EPI-RTE-prefix-disposition](#epi-rte-prefix-disposition).
Behavioral-authority path: consumer, channel, force, horizon: see disposition record and [RT-BAP-verifier-prefix](runtime.md#rt-bap-verifier-prefix).
Evidence source ID and local anchor: SRC-1, `path_collection.py`; `mcts_utils/llm_server.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: requested first-error diagnosis is not verified diagnosis.
Gap/limit: science-task wording is used across task modes; task description is extracted positionally; no successful path/reference answer or judge reliability comparison is supplied.

Route ID: [EPI-RTE-prefix-disposition](#epi-rte-prefix-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-revision-feedback](#epi-obj-revision-feedback).
Content/update relation: no content change.
Transition or check target: continue or truncate the low-path prefix.
Evaluator/condition and domain: see record; substring predicates rather than an evidence-consuming truth acceptance decision.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: continues or breaks; keeps the triggering node in either case.
Epistemic authority and scope: no accepted factual claim established. Operational disposition only.
Operational authority: behavior permitted, blocked, or changed: determines prefix length of one candidate example.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-verifier-prefix](runtime.md#rt-bap-verifier-prefix).
Evidence source ID and local anchor: SRC-1, `path_collection.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: `uncertain` and malformed negative phrases can continue.
Gap/limit: no rollback of already executed actions, per-row approval, or correctness certification.

Route ID: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-env-score](#epi-obj-env-score); path candidates in the cited route.
Content/update relation: no content change.
Transition or check target: terminal-leaf paths and distinct high/low pairs intended for dataset inclusion.
Evaluator/condition and domain: see route; positive root and intended ALPHA/BETA reward thresholds; not a proposition checker.
Activation and timing: see route.
Possible or observed result: early return, empty candidates, or type error at numeric/string comparison; hypothetical passing predicates are not shipped successful execution.
Implemented force: filters/ranks batch candidates where predicates can operate; reached thresholds fail instead of certifying quality.
Epistemic authority and scope: at most sampled outcome-based intended eligibility; no verification of first-error mechanism, transfer, or same-parent continuity.
Operational authority: behavior permitted, blocked, or changed: see route; export stops on uncaught comparison error.
Behavioral-authority path: consumer, channel, force, horizon: see route; path construction reads ranked candidates within one export invocation.
Evidence source ID and local anchor: SRC-1, `path_collection.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: threshold defect; same-parent condition unenforced.
Gap/limit: no actual admission criterion successfully exercised; `good` bypasses critique, paired no-revise mode bypasses diagnosis.

Route ID: [EPI-RTE-conversation-splice](#epi-rte-conversation-splice)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-revise-log](#epi-obj-revise-log).
Content/update relation: truth-apt transformation: non-ampliative reshaping for copied message contents; truth-apt transformation: ampliative conjecture for inserted actor error admissions not entailed by input logs. Constructed wait/acknowledgement is non-truth-apt policy/content update: synthetic dialogue event, not observed transition evidence.
Transition or check target: selected path logs into one corrective conversation.
Evaluator/condition and domain: see record; no post-splice environment replay or semantic evaluator.
Activation and timing: see record.
Possible or observed result: see record; output instance unobserved.
Implemented force: marks synthetic correction and good continuation loss-eligible; bad prefix ineligible.
Epistemic authority and scope: copied reports remain attributed to original branches; assembled sequence has no newly checked execution warrant.
Operational authority: behavior permitted, blocked, or changed: training eligibility flags are written, but optimizer interpretation is not captured.
Behavioral-authority path: consumer, channel, force, horizon: constructor to JSONL writer, message fields/loss booleans, dataset construction within export; later training only declared.
Evidence source ID and local anchor: SRC-1, `path_collection.py`; `mcts_utils/llm_server.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: synthetic self-report is not observed self-recognition; splice coherence untested.
Gap/limit: model feedback remains side metadata and is not used to author the fixed revision thought.

Route ID: [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-env-score](#epi-obj-env-score), [EPI-OBJ-revision-feedback](#epi-obj-revision-feedback), [EPI-OBJ-revise-log](#epi-obj-revise-log).
Content/update relation: no content change.
Transition or check target: recursive tree save and append-only example rows.
Evaluator/condition and domain: see routes; completed search and export control flow, not evidence-consuming factual acceptance.
Activation and timing: see routes; export upstream defect remains.
Possible or observed result: see routes; no saved instance supplied.
Implemented force: retains candidate material and metadata; existing tree filename suppresses recollection.
Epistemic authority and scope: retention does not convert judgments or synthetic transcripts into accepted knowledge.
Operational authority: behavior permitted, blocked, or changed: later tree reload changes candidate selection; later optimizer consumption is uninspected.
Behavioral-authority path: consumer, channel, force, horizon: see routes; separate collection/export invocations via JSON trees; intended training via JSONL.
Evidence source ID and local anchor: SRC-1, `mcts_collection.py`; `path_collection.py`; `mcts_utils/llm_server.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: none.
Gap/limit: no accepted-claim lifecycle integration shown; append has no deduplication, invalidation, or transactional rollback.

Route ID: [EPI-RTE-dataset-rewrite](#epi-rte-dataset-rewrite)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-conversation](#epi-obj-conversation).
Content/update relation: truth-apt transformation: non-ampliative reshaping of retained strings, with lineage/eligibility metadata omitted.
Transition or check target: `revise_log` message array into position-indexed `conversation` fields.
Evaluator/condition and domain: see record; deterministic positional mapping, not validation of roles or truth.
Activation and timing: see record; helper caller required, no CLI invocation found.
Possible or observed result: see record.
Implemented force: writes reshaped data; actual trainer consumption unknown.
Epistemic authority and scope: preserves selected text, not original metadata or masking semantics.
Operational authority: behavior permitted, blocked, or changed: may supply training-shaped input; not a captured parameter update.
Behavioral-authority path: consumer, channel, force, horizon: see record; save_json writes conversion output for a later unspecified caller.
Evidence source ID and local anchor: SRC-1, `mcts_utils/llm_server.py`.
Claim IDs or none: none.
Mismatch marker or none: dropped loss/lineage metadata.
Gap/limit: no external trainer format contract; metadata omission does not prove that a particular optimizer trains on bad-prefix text.

Route ID: [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: configured actor's task outcome report, not a proposed theory.
Content/update relation: truth-apt transformation: acquisition/import of final reward; source warrant unknown.
Transition or check target: one actor rollout on a selected test task.
Evaluator/condition and domain: see route; external environment reward/done plus continuation budget.
Activation and timing: see route; missing input directory limits CLI activation.
Possible or observed result: see route.
Implemented force: negative reward/done stops rollout; final score is written, with no shipped later checkpoint-admission consumer.
Epistemic authority and scope: outcome measurement under environment scoring only; no causal attribution to revision training.
Operational authority: behavior permitted, blocked, or changed: see route; supplied prefix is executable without critique.
Behavioral-authority path: consumer, channel, force, horizon: see route; current rollout stops and result file is retained.
Evidence source ID and local anchor: SRC-1, `eval.py`; `mcts_utils/llm_server.py`.
Claim IDs or none: [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training).
Mismatch marker or none: outcome versus process/transfer limit.
Gap/limit: no paired checkpoint experiment; no later result consumer establishing promotion or withdrawal.

Route ID: [RT-RTE-provider-alternate](runtime.md#rt-rte-provider-alternate)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-CMP-func-call](runtime.md#rt-cmp-func-call).
Content/update relation: truth-apt transformation: indeterminate for any generated propositional text; non-truth-apt action proposals may also be returned.
Transition or check target: see route; injected inference calls, no independent truth check.
Evaluator/condition and domain: see route; remote model generation is not an answer oracle.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: caller may consume returned text; repeated transport retry does not improve epistemic warrant.
Epistemic authority and scope: none independently established for returned claims.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route; only a caller-supplied alternative, not CLI selection.
Evidence source ID and local anchor: SRC-1, `mcts_utils/llm_server.py`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: provider internals, usable completion and activation unobserved.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training) | Actor locates first error; adjacent correct path shares a parent; training supports timely reflection and iterative improvement | SRC-1, `README.md`, doctrine/design; see claim | Explicit framework intent; external training instructions | [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), [EPI-RTE-critique-check](#epi-rte-critique-check), [EPI-RTE-prefix-disposition](#epi-rte-prefix-disposition), [EPI-RTE-conversation-splice](#epi-rte-conversation-splice), [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation) | None supplied | No intervention/comparison; score ranking does not identify the cause of success; feedback substring matching does not certify the first error; splice not replayed | Implemented outcome-driven search and callable critique/construction machinery; declared later training | Thresholds defective; same-parent predicate absent; actor/verifier weight equality unenforced; training/promotion absent from shipped tree |

The verifier prompt's helpful/harmful criterion is operational guidance, not an additional public reliability claim: see [EPI-RTE-critique-check](#epi-rte-critique-check). Its "good verifier" wording grants no independently established competence.

## Bounded conclusion

Agent-R imports environment observations and scores, executes model action proposals, and lets numerical outcomes select branches and candidate paths. Source warrant is unknown because environment semantics and replay fidelity are not captured. Software can validly compute aggregates from the supplied numbers; that arithmetic does not warrant the observations, action rationale, or transfer to another task. Outcome scoring and lexical validity substitution retain separate targets and limits. See [EPI-RTE-reward-check](#epi-rte-reward-check), [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), [RT-RTE-sciworld-action](runtime.md#rt-rte-sciworld-action).

The critique route requests a truth-apt action-usefulness judgment and reasons. The implemented consumer grants the resulting string operational authority over one exported prefix, not acceptance of the diagnosis as true. Continuing on `uncertain` is deliberate source behavior; it withholds neither the prefix nor the example merely because uncertainty is reported. A concrete `Judgement: not good` response would also continue because the substring `good` is present. This is a deduction from the inspected parser, not a target execution. No evidence-consuming decision licenses a new factual claim for reliance beyond this bounded dataset-construction purpose. See [EPI-RTE-critique-check](#epi-rte-critique-check), [EPI-RTE-prefix-disposition](#epi-rte-prefix-disposition).

Corrective examples copy branch text, insert an unverified self-error admission and fabricate a wait/acknowledgement event. The model's critique reasons remain side metadata. An intended high score does not establish that the assembled transcript is executable, or that the inserted admission describes actual model self-recognition. Threshold errors prevent claiming a successful shipped export. Tree persistence and intended JSONL retention precede any established epistemic acceptance; no accepted-claim lifecycle integration is demonstrated by those writes. The exposed `rewrite` helper further discards masking and provenance metadata while preserving selected strings. See [EPI-RTE-conversation-splice](#epi-rte-conversation-splice), [EPI-RTE-dataset-rewrite](#epi-rte-dataset-rewrite), [RT-RTE-revision-export](runtime.md#rt-rte-revision-export).

There is direct non-truth-apt behavior adaptation in branch selection, action substitution and prefix-length decisions. Inference wrappers do not update parameters; exact checkpoints are caller-selected and unpinned. Iterative training, checkpoint admission and later behavioral dependence remain unestablished within this partial loop. Missing run and causal evidence prevent demonstrated learning or benefit. The requested self-critique capacity is distinct from reliable reflective operation; fixed stock admissions alone do not establish it. The self-improvement links and their horizon are see [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training). Independent action-generation and software-control capacities remain inspectable despite those limits. No single epistemic score or system-wide negative follows, especially with auxiliary SciWorld operations still unassessed.

## Shared records

### Operative objects

#### EPI-OBJ-env-score
Label: Environment reports and sampled score state

Natural-language observations and symbolic reward/done fields enter task-specific nodes; value/visits are symbolic aggregates in memory and saved JSON. These are material contents of [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), not a duplicate of that whole route. No supplied operative-object counterpart exists. Reports describe the external task state/outcome; negative reward is clamped before storage. SRC-1, `mcts_utils/webshop/mcts_ws.py`, implementation:

> current_obs = current_env_state
> done = current_env_done
> new_env_score = current_env_reward
> --- `mcts_utils/webshop/mcts_ws.py`

> if new_env_score < 0:
>     is_terminal = True
>     new_env_score = 0
>     disaster = True
> --- `mcts_utils/webshop/mcts_ws.py`

Score aggregation is numerical bookkeeping, not new empirical warrant. SRC-1, `mcts_utils/mcts_raw.py`, implementation:

> self.visits += 1
> self.value += reward
> --- `mcts_utils/mcts_raw.py`

#### EPI-OBJ-revision-feedback
Label: revise_feedback model judgments

Source-native `revise_feedback` contains natural-language reasons and judgment text alongside action and observation strings, in an in-memory list and intended JSONL side field. Distinct from [RT-BAP-verifier-prefix](runtime.md#rt-bap-verifier-prefix), which is its consumer path, and from the encompassing [RT-RTE-revision-export](runtime.md#rt-rte-revision-export). No supplied object counterpart. SRC-1, `path_collection.py`, implementation:

> judgement = response.split('Judgement:')[-1].strip()
> revise_feedback.append({
>     "revision_feedback": response,
>     "action": node.action,
>     "obs": node.obs,
>     "judgement": judgement
> })
> --- `path_collection.py`

#### EPI-OBJ-revise-log
Label: revise_log corrective conversation

Source-native `revise_log` is a message list with natural-language contents and symbolic roles/loss flags. It is constructed in memory for JSONL retention. Distinct material output of [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), not a duplicate of the route; no supplied object counterpart. Bad-path assistant contents receive `loss: False`, stock correction and good continuation `loss: True`. Source histories originate in separate branches; new synthetic dialogue has different lineage. SRC-1, `path_collection.py`, implementation:

> bad_log.append({"role": "assistant", "content": node.llm_response, "loss": False})
> bad_log.append({"role": "user", "content": node.obs})
> --- `path_collection.py`

> revision_thought = revision_thoughts[random.randint(0, 9)]
> bad_log.append({"role": "assistant", "content": f"Thought: {revision_thought}\nAction: wait", "loss": True})
> bad_log.append({"role": "user", "content": "ok."})
> --- `path_collection.py`

#### EPI-OBJ-conversation
Label: rewrite conversation output

The `rewrite` output is a list of symbolic `conversation`/`system`/`input`/`output` fields containing copied natural-language contents, accumulated in memory and saved as JSON. Distinct from [EPI-OBJ-revise-log](#epi-obj-revise-log): it replaces the message representation and omits role/loss and enclosing example metadata. Closest supplied route is [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), but this separate conversion helper is neither that exporter nor a part of its CLI flow. SRC-1, `mcts_utils/llm_server.py`, implementation:

> final_dataset.append({"conversation": conversation})
>
> save_json(final_dataset, output_path)
> --- `mcts_utils/llm_server.py`

### Routes

#### EPI-RTE-reward-check
Label: Environment outcome evidence
Part of: [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)

This isolates the check/evidence-producing step from the collection container's branch selection and retention. Owner: task adapter calls the external task environment. Endpoint/progression: parsed proposed action → environment `step` → state/reward/done report → score processing. The actor proposes, environment returns outcomes, software decides continuation; caller configures the batch without per-action approval. Answer oracle is an external outcome signal, not a reference trajectory delivered to the actor. Mode: bounded curriculum/search; improvement trigger is sampled task reward.

- Immediate return: External state, reward and done fields for the new environment step.
- Later read-back: Reports and aggregates enter saved trees later reloaded by the revision driver.
- Delegated visibility: Server receives action after reset/replay; actor receives conversation text, not the score-selection formula.
- Selection predicate: New action is executed before terminal reward processing; done, negative reward or depth boundary can make the child terminal.
- Invalidation or expiry: No independent remeasurement or report-expiry check; see parent route's persistence policy.
- Activation or effect: Terminal child reward updates counters and feeds later ranking; no observed execution supplied.
- Evidence limits: External scoring/state correctness and deterministic replay uninspected; outcome is not an action-local causal diagnosis.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `mcts_utils/webshop/mcts_ws.py`, implementation:

> step_output = current_env.step(new_action)
> current_env_state, current_env_reward, current_env_done = (
>         step_output.state,
>         step_output.reward,
>         step_output.done,
>     )
> --- `mcts_utils/webshop/mcts_ws.py`

#### EPI-RTE-critique-check
Label: Model action usefulness check
Part of: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

This is only the verifier request/result, not the subsequent prefix decision. Owner: `revise_worst_path`. Endpoint/progression: task description and action/observation prefix → word-count truncation → local model call → reasons/judgment feedback. The model proposes the judgment; software later decides how to consume it. No reference action or successful path is sent to the verifier; model judgment alone is not an answer oracle. Mode: offline paired-example construction; trigger is `revise` enabled after path selection. Task description is `low_path[-1].state[3]["content"]`, not a separately validated instruction extraction.

- Immediate return: Model response and extracted suffix after `Judgement:` collected as feedback.
- Later read-back: Feedback is stored in intended output rows; no shipped later semantic consumer of the reasons is established.
- Delegated visibility: Verifier receives preceding text, current action/observation and positional task description; successful path and tree statistics are omitted.
- Selection predicate: Iterates through low-path nodes until the separate prefix disposition breaks; `good` mode and no-revise mode bypass it.
- Invalidation or expiry: No recalibration, second judge, challenge or withdrawal mechanism in this helper.
- Activation or effect: Produces requested judgments for the prefix consumer, but upstream CLI type errors prevent claiming successful activation.
- Evidence limits: Actual response content, diagnosis truth, calibration and reliability unobserved; reasons may be generated but do not themselves certify evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guidance is action usefulness, not a formulated theory about a general mechanism. SRC-1, `mcts_utils/llm_server.py`, doctrine/design embedded in implementation:

> You need to verify whether the current action is good, bad, or uncertain in the log.
> - A **good** action is greatly helpful to solve the task.
> - A **bad** action is greatly harmful to solve the task.
> - An **uncertain** action is one that is neither good nor bad, or you cannot judge based on the current information.
> --- `mcts_utils/llm_server.py`

SRC-1, `path_collection.py`, implementation:

> message = [{"role": "user", "content": prompt}]
> response = calling.llm_func(message, os.environ["MODEL_NAME"])
> --- `path_collection.py`

#### EPI-RTE-prefix-disposition
Label: Judgment substring prefix disposition
Part of: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

This is the software consumer, distinct from the check and coextensive with the decision described by [RT-BAP-verifier-prefix](runtime.md#rt-bap-verifier-prefix), which is a behavioral-authority path rather than a second route. Owner: `revise_worst_path`. Endpoint/progression: extracted judgment → lowercase substring tests → append/continue or append/break. Model proposes; software decides; no per-example human veto is wired. Operating mode and upstream trigger are the parent's offline revision construction; no new answer oracle.

- Immediate return: Delimited bad path, good path without root, and feedback list.
- Later read-back: Delimited path becomes retained conversation content if export reaches its writer.
- Delegated visibility: Splice receives nodes and feedback is kept separately; stock revision text is not generated from the reasons.
- Selection predicate: `good` or `uncertain` anywhere in lowercased judgment continues; anything else includes current node then breaks.
- Invalidation or expiry: No revision of an earlier judgment or automatic withdrawal of exported rows.
- Activation or effect: Controls one erroneous-prefix boundary; does not roll back environment actions or admit a true diagnosis.
- Evidence limits: Malformed text can determine continuation; upstream threshold defects and absent traces limit activation claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission target is prefix membership, not factual knowledge. Recovery is caller-side dataset rebuilding/removal, not a shipped rollback. SRC-1, `path_collection.py`, implementation:

> if "good" in judgement.lower() or "uncertain" in judgement.lower():
>     revise_path.append(node)
> else:
>     if node.disaster:  # Stop revision if the node represents a disaster
>         flag = 0
>     revise_path.append(node)
>     break
> --- `path_collection.py`

#### EPI-RTE-conversation-splice
Label: Synthetic corrective conversation splice
Part of: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

Owner: `conversation_generation`. Endpoint/progression: selected bad/good node lists → copied messages with loss flags → random stock admission and wait acknowledgement → good continuation, skipping an initially equal response prefix. Software authors the correction cue; model critic does not supply it. Proposed change is a training conversation, not live policy/weights. Trigger: paired construction with or without critique. Intended eligibility comes from parent path predicates; no post-splice acceptance, replay or per-row human approval. Recovery: external removal/rebuild only.

- Immediate return: Concatenated initial state, bad log, synthetic correction event and good log.
- Later read-back: Intended JSONL output for external training; optimizer ingestion and later checkpoint authority not inspected.
- Delegated visibility: Writer receives assembled transcript and parent side fields; no environment is asked to execute the assembled path.
- Selection predicate: Random integer 0 through 9 chooses from stock thoughts; exact initial response equality suppresses duplicated good-prefix messages.
- Invalidation or expiry: No coherence check, expiry or invalidation after assembly.
- Activation or effect: Changes transcript lineage and symbolic loss eligibility; actual training impact unobserved.
- Evidence limits: Parent comparison defects; no runtime example or successful splice replay; correct outcome does not entail an actor's self-error admission.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The input need not contain a self-report of misunderstanding. Yet the helper can insert one from static text. That new proposition is not entailed by copied observations or scores. The wait acknowledgement is constructed even though no `step` occurs in this function. Construction evidence is in [EPI-OBJ-revise-log](#epi-obj-revise-log). SRC-1, `mcts_utils/llm_server.py`, implementation constant:

> "I see an error in my actions. I need to fix it.",
> "I misunderstood the situation. Time to reassess.",
> "My decision was wrong. I should reevaluate.",
> --- `mcts_utils/llm_server.py`

SRC-1, `path_collection.py`, implementation:

> good_log.append({"role": "assistant", "content": node.llm_response, "loss": True})
> good_log.append({"role": "user", "content": node.obs})
> --- `path_collection.py`

#### EPI-RTE-dataset-rewrite
Label: Positional training dataset rewrite

No supplied counterpart after comparison: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export) produces rows, while `rewrite` is a separate callable helper mapping supplied rows and saving a new dataset. Owner: `rewrite`; endpoints/progression: `dataset[*].revise_log` → content-only positional fields → JSON file. It does not call critique, enforce source roles, preserve loss flags, or test proposition truth. Caller supplies input and destination; software makes all conversion decisions. Mode: batch transformation. No answer oracle; no per-content approval or later rollback is implemented.

- Immediate return: No explicit return; saves `final_dataset` to output_path.
- Later read-back: uninspected — no caller or training consumer for this helper is wired in the three shipped drivers.
- Delegated visibility: Output receives content strings and new field names, not feedback, task number, high/low logs, roles or loss flags.
- Selection predicate: First three content positions become system/input/output; subsequent pairs beginning at index 3 become input/output; unmatched trailing content is omitted.
- Invalidation or expiry: save_json overwrites destination; no provenance, freshness, expiry or rollback mechanism.
- Activation or effect: Affords content-only conversion, including loss-ineligible bad-prefix strings when present; no execution or optimizer effect observed.
- Evidence limits: Positional mapping assumes message order and length; external training schema/semantics unavailable; no shipped invocation found.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Concrete source deduction, not execution: a five-message `revise_log` with content strings `S`, `U`, `A`, `O`, `B` becomes `conversation` entries `{system: S, input: U, output: A}` and `{input: O, output: B}`. Giving the last message `loss: False` does not change that mapping: the implementation reads only `content`. A sixth trailing string would be omitted because index 5 has no paired successor. Thus text preservation for included positions coexists with metadata and unmatched-content loss. SRC-1, `mcts_utils/llm_server.py`, implementation:

> temp = {
>     "system": revise_log[0]["content"],
>     "input": revise_log[1]["content"],
>     "output": revise_log[2]["content"],
> }
> conversation.append(temp)
> i = 3
> while i+1 < len(revise_log):
>     temp = {
>         "input": revise_log[i]["content"],
>         "output": revise_log[i+1]["content"],
>     }
>     i += 2
>     conversation.append(temp)
> --- `mcts_utils/llm_server.py`
