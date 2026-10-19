---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "JAZ's content checks, execution authority, retained-response reuse and limits on knowledge and optimization claims."
run-id: AAS-2026-10-15-jaz-a94bea79c61a-01
reviewed-boundary: 0803d4971be785e95b80054b02259664d70fa3da
---

# JAZ epistemic report

## Source-and-claim boundary

The question is what licenses reliance on JAZ's generated answers, code, observations and reused execution material. The frozen package and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). All additional reads below are SRC-1 implementation unless explicitly labelled doctrine/design or reported operation. No target execution was performed. No observed run or causal experiment is supplied.

The runtime account is a useful baseline, not a complete inventory of evaluators. In particular, pre-execution code validation, the console's live model probe, rollout export predicates and explicit SGLang weight-update operations need separate treatment. These additions qualify the coverage of [RT-RTE-hook-control](runtime.md#rt-rte-hook-control) and [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend); they do not supersede the narrower ordinary-query findings.

Public claims considered are [RT-CLM-repl-work](runtime.md#rt-clm-repl-work), [EPI-CLM-agent-optimization](#epi-clm-agent-optimization), [EPI-CLM-model-validation](#epi-clm-model-validation), [EPI-CLM-rollout-fidelity](#epi-clm-rollout-fidelity) and [EPI-CLM-code-framing](#epi-clm-code-framing). They concern computation, optimization, availability and recording fidelity, not an unconditional assertion that every answer is true.

| Entry point or operation | Source path | Coverage and basis | Limit and conclusion prevented |
|---|---|---|---|
| invoke/ainvoke, recursion, parser, REPL | `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/protocol/code_only.py`, `src/jaz/repl/python_repl.py` | Supplied [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop), [RT-RTE-recursive-work](runtime.md#rt-rte-recursive-work); direct observation/history rendering read | Arbitrary tasks have no supplied candidate instance or reference answer; truth and entailment of a particular answer are not determinable. |
| Installed console and module dispatch: -c, files, stdin, interactive | `src/jaz/console.py`, `src/jaz/__main__.py`, `pyproject.toml` | Direct `main` read; supplied [RT-RTE-settings-change](runtime.md#rt-rte-settings-change); direct helper, history, ping and switch reads | Plain console Python is host code, not a universal semantic-validation boundary. |
| Exposed hook implementations | `src/jaz/hooks/builtin/__init__.py`, `src/jaz/hooks/builtin/repl_code_hooks.py`, `src/jaz/hooks/builtin/return_hooks.py` | Direct export inventory and validator implementations; supplied [RT-RTE-hook-control](runtime.md#rt-rte-hook-control) | Caller predicates are unspecified. No common task-correctness criterion follows from the interface. |
| Budget forcing/context warning | `src/jaz/hooks/builtin/budget_forcing.py`, `src/jaz/hooks/builtin/context_window.py` | Direct full reads, [EPI-RTE-budget-forcing](#epi-rte-budget-forcing); runtime supplies cost/iteration/recursion governance | More iterations and prompt warnings do not themselves check truth. |
| Registered SWE tools | `src/jaz/_library/swe.py` | Direct full read; [RT-RTE-host-tools](runtime.md#rt-rte-host-tools) | Shell status and replacement cardinality are not semantic correctness tests. Other caller-supplied tools are opaque. |
| Recording, replay, workflow emission | `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py` | Supplied [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) and boundary recorder passages | Detailed complete trace fidelity audit not performed; no supplied trace proves success, replay equivalence or task acceptance. |
| Token rollouts and export | `src/jaz/hooks/builtin/rollout.py` | Direct `_extends`, projections and recorder lifecycle reads; [EPI-RTE-rollout-export](#epi-rte-rollout-export) | SGLang stamp production/tokenizer fidelity not fully traced. The structural predicate does not independently authenticate sent tokens. |
| Model weight operations | `src/jaz/llm/sglang.py` | Direct `_post` and update/memory/generation controls; [EPI-RTE-weight-update](#epi-rte-weight-update) | Server internals, trainer, update criterion and resulting parameter versions unavailable; update success and improved capacity unobserved. |
| Diff extraction | `src/jaz/utils/extract_git_diff.py` | Direct full read | Copies the `git_diff` string from JSON to a file after existence/truthiness checks; does not verify patch applicability or improvement. No added semantic evaluator. |
| Trace/log directory and Markdown conversion | `src/jaz/utils/trace_to_directory.py`, `src/jaz/utils/log_to_markdown.py` | Scoped symbol search and supplied boundary coverage only | Detailed transformation lineage uninspected. Prevents a system-complete negative about every provenance-preserving or provenance-losing transformation. |
| Other model adapters, external tracing exporters and arbitrary hooks/components | `src/jaz/llm/`, `src/jaz/hooks/builtin/otel_tracing.py`, `src/jaz/hooks/dispatcher.py` | Supplied runtime adapter/dispatcher findings; built-in exports inspected | Not a complete adapter/exporter audit. No universal exclusion of remote evaluation, learning or provider tools. |

The source has no supplied execution evidence, model weights, training driver or unshipped evaluation harness. Those gaps prevent observed acceptance, causal optimization and learned-capacity findings. Available but uninspected package details above are inspection limits, not access gaps or evidenced absences. The report therefore makes route-specific negatives, not a system-complete assertion that no other evaluator exists.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer) | Inputs, descriptions and observations can assert facts; no particular proposition supplied | see cited record | SRC-1, `src/jaz/_agent.py` | Acquisition preserves supplied assertions, not source warrant; origin/credibility vary by caller. |
| [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | Native data and values can encode propositions; code is also executable policy | see cited record | SRC-1, `src/jaz/repl/python_repl.py` | Computing a value does not establish its interpretation or premises. |
| [EPI-OBJ-observation-text](#epi-obj-observation-text) | Printed measurements/error claims over the current execution; can also contain arbitrary prose | REPL observation | SRC-1, `src/jaz/protocol/code_only.py` | Abbreviation can remove the error or qualifying context. |
| [EPI-OBJ-helper-response](#epi-obj-helper-response) | An answer can assert facts about current config or JAZ; a code response is primarily a proposed action | Tagged helper response | SRC-1, `src/jaz/console.py` | Type acceptance does not substantiate either answer or snippet. |
| [EPI-OBJ-rollout](#epi-obj-rollout) | Token/context/outcome assertions about a trajectory; not a theory of task success | Rollout | SRC-1, `src/jaz/hooks/builtin/rollout.py` | Token-less responses withdraw the entire invoke's rollout; driver judgment remains separate. |
| [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) | Distributed-parametric content cannot be individuated as a particular truth-apt claim from these sources | see cited record | SRC-1, `src/jaz/llm/sglang.py` | Explicit update API supplements the ordinary completion route; actual weights and changes remain uninspected. |

## Authority-route ledger

The ledger separates checking from disposition, and retention from acceptance or lifecycle integration. A linked implementation can perform more than one function. `see` cells defer to the cited declaring record rather than restating its route fields. All implemented rows are static wiring, not observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | content transformation | implemented | see [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer) | truth-apt transformation: indeterminate | Task/observations to answer-bearing native value or code | Model chooses response; no ordinary answer oracle | see cited route | see cited route | Candidate production; execution | No blanket semantic license | see cited route | see [RT-BAP-response-execution](runtime.md#rt-bap-response-execution) | SRC-1, `src/jaz/_agent.py` | [RT-CLM-repl-work](runtime.md#rt-clm-repl-work) | none | Without a concrete input/output proposition neither entailment nor non-entailment is established. |
| [RT-RTE-host-tools](runtime.md#rt-rte-host-tools) | content transformation | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | truth-apt transformation: acquisition/import | External file/process data enters REPL | see cited route | see cited route | see cited route | Data delivery, possible effects | Source warrant unknown; read success is not endorsement | see cited route | see cited route | SRC-1, `src/jaz/_library/swe.py` | none | none | Exact-match edit guard concerns targeting, not truth. |
| [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | check/evidence production | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | Python source execution under current namespace | Python compiler/interpreter and configured guards, not task oracle | see cited route | Value, stdout or exception | Current-turn evidence | Evidence of behavior under these bindings; not explanation, transfer or premise truth | see cited route | see [RT-BAP-response-execution](runtime.md#rt-bap-response-execution) | SRC-1, `src/jaz/repl/python_repl.py` | [RT-CLM-repl-work](runtime.md#rt-clm-repl-work) | none | Supplied execution results can bypass local work. |
| [EPI-RTE-code-validation](#epi-rte-code-validation) | check/evidence production | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | Committed code string before execution | Host predicate on source text; criterion caller-defined | see cited route | Exception or ordinary return | Predicate evidence only | At most satisfaction of supplied predicate | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/repl_code_hooks.py` | none | none | No claim that predicate is sound for task truth. |
| [EPI-RTE-code-validation](#epi-rte-code-validation) | disposition/acceptance | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | Admit or veto committed code | Failure count and predicate result | see cited route | Continue/Abort or no veto | Enforcing pre-execution veto | Policy admission, not general epistemic acceptance | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/repl_code_hooks.py` | none | none | No rollback of prior turns; counter cleanup is not knowledge withdrawal. |
| [RT-RTE-hook-control](runtime.md#rt-rte-hook-control) | check/evidence production | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | ReturnType: native terminal value against configured type hint | Type checker, type domain only | see cited route | Type pass/mismatch | Type evidence | Type conformity, not answer truth | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | none | none | No type hint implies no such optional check. |
| [RT-RTE-hook-control](runtime.md#rt-rte-hook-control) | disposition/acceptance | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | ReturnType result admission | Type result and configured failure tolerance | see cited route | Recoverable feedback or terminal error | Enforcing result reshape/backstop | Type-scoped admission only | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | none | none | Hook bug handling limits universal fail-closed guarantees. |
| [EPI-RTE-return-validation](#epi-rte-return-validation) | check/evidence production | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | Native Return value | Host callback; arbitrary caller-defined value criterion | see cited route | Callback returns or raises | Predicate evidence | Acceptance warrant depends on actual evidence-consuming callback, criterion and use | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | none | none | Supplied source does not instantiate a task correctness oracle. |
| [EPI-RTE-return-validation](#epi-rte-return-validation) | disposition/acceptance | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | no content change | Recover, reject terminal value or permit completion | Callback result, count and final Return identity | see cited route | Continue, Raise or unchanged Return | Enforcing output decision | Operational acceptance; substantive epistemic license not determinable without callback | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | none | none | Rejection occurs after effects; no transactional rollback. |
| [EPI-RTE-observation-cut](#epi-rte-observation-cut) | content transformation | implemented | see [EPI-OBJ-observation-text](#epi-obj-observation-text) | truth-apt transformation: indeterminate | Full output to shortened observation | Deterministic character slicing, not semantic evaluator | see cited route | Prefix/marker/suffix | Evidence delivery with omission | Warrant can be degraded by lost qualifiers/errors; no endorsement | see cited route | see cited route | SRC-1, `src/jaz/string_utils.py` | none | none | Intact substrings do not guarantee intact propositions. |
| [EPI-RTE-helper-unwrapping](#epi-rte-helper-unwrapping) | content transformation | implemented | see [EPI-OBJ-helper-response](#epi-obj-helper-response) | non-truth-apt policy/content update: unwrap proposed code | Helper code string to executable snippet | Regex whole-string fence match | see cited route | Unwrapped or whitespace-stripped string | Action preparation | No truth license; no code validator here | see cited route | see [RT-BAP-helper-proposal](runtime.md#rt-bap-helper-proposal) | SRC-1, `src/jaz/console.py` | none | none | Code classification is an action path, not proof of semantic preservation for every possible string. |
| [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) | disposition/acceptance | implemented | see [EPI-OBJ-helper-response](#epi-obj-helper-response) | no content change | Helper answer versus proposed code | see cited route | see cited route | see cited route | Answer advisory; code human-gated | Human consent licenses action, not verified correctness | see cited route | see [RT-BAP-helper-proposal](runtime.md#rt-bap-helper-proposal) | SRC-1, `src/jaz/console.py` | none | none | Answers print without confirmation; rejected code remains remembered as unapplied. |
| [EPI-RTE-model-ping](#epi-rte-model-ping) | check/evidence production | implemented | see [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) | no content change | Configured backend/model/key minimal completion | Provider round-trip: no ordinary Exception | see cited route | None or exception | Evidence for one request | Availability of that request, not task competence or future uptime | see cited route | see cited route | SRC-1, `src/jaz/console.py` | [EPI-CLM-model-validation](#epi-clm-model-validation) | future-availability overreach | No response-content criterion. |
| [EPI-RTE-model-ping](#epi-rte-model-ping) | disposition/acceptance | implemented | see [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) | non-truth-apt policy/content update: replace model component | Candidate model switch | Human/caller choice plus successful ping | see cited route | Retain old component on error, configure new on success | Permissive configuration gate | Accepted for request availability only | see cited route | see cited route | SRC-1, `src/jaz/console.py` | [EPI-CLM-model-validation](#epi-clm-model-validation) | future-availability overreach | Direct configure/startup flags do not use this gate. |
| [EPI-RTE-budget-forcing](#epi-rte-budget-forcing) | behavior/policy adaptation | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | non-truth-apt policy/content update: refuse early finish | Return/Raise before refusal count exhausted | Counter, not semantic evaluator | see cited route | Continue with caller refusal text | Enforcing continuation; advisory instruction content | None about answer quality | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/budget_forcing.py` | [EPI-CLM-agent-optimization](#epi-clm-agent-optimization) | none | No outcome-responsive quality comparison. |
| [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) | operational admission/selection/consumption | implemented | see [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer) | no content change | Saved response selection for live code path | see cited route | see cited route | see cited route | Execution-permissive reuse | Replay compatibility is not truth or current applicability | see cited route | see [RT-BAP-response-execution](runtime.md#rt-bap-response-execution) | SRC-1, `src/jaz/hooks/builtin/replay.py` | none | none | Divergence fallback changes supplier, not epistemic status of a claim. |
| [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) | retention | implemented | see [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | non-truth-apt policy/content update: emit executable workflow | Event-associated code to files | see cited route | see cited route | see cited route | Program retention, not automatic next-policy installation | No correctness certification | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/workflow_replay.py` | [EPI-CLM-agent-optimization](#epi-clm-agent-optimization) | none | Partial failed/aborted workflows are possible. |
| [EPI-RTE-rollout-export](#epi-rte-rollout-export) | retention | implemented | see [EPI-OBJ-rollout](#epi-obj-rollout) | truth-apt transformation: acquisition/import | Backend TurnRecords to per-invoke Rollout | Token-record presence and InvokeExit | see cited route | Rollout or withdrawal/no rollout | Collector state retention | Backend record warrant not independently authenticated | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/rollout.py` | [EPI-CLM-rollout-fidelity](#epi-clm-rollout-fidelity) | none | No built-in reward or task-success admission. |
| [EPI-RTE-rollout-export](#epi-rte-rollout-export) | check/evidence production | implemented | see [EPI-OBJ-rollout](#epi-obj-rollout) | no content change | Adjacent context-prefix stamp lineage for one flat export | `_extends`: message IDs and prefix lengths | see cited route | Compatible or NonMonotoneRolloutError | Export representation gate | Flatness relative to supplied stamps, not semantic correctness or authentic execution | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/rollout.py` | [EPI-CLM-rollout-fidelity](#epi-clm-rollout-fidelity) | authentication unverified | Token/value equivalence is not the comparison predicate. |
| [EPI-RTE-rollout-export](#epi-rte-rollout-export) | disposition/acceptance | implemented | see [EPI-OBJ-rollout](#epi-obj-rollout) | no content change | Admit flat export or select alternate projection | Compatibility check; caller chooses projection | see cited route | Flat, pieces or per-turn samples | Enforcing flat rejection, permissive alternatives | Representation suitability only | see cited route | see cited route | SRC-1, `src/jaz/hooks/builtin/rollout.py` | [EPI-CLM-rollout-fidelity](#epi-clm-rollout-fidelity) | none | Nonmonotone data remains available, not rejected as false or useless. |
| [EPI-RTE-weight-update](#epi-rte-weight-update) | behavior/policy adaptation | implemented | see [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) | non-truth-apt policy/content update: request server weight replacement | SGLang model-serving state | HTTP status, no local quality evaluator | see cited route | Server JSON/None or mapped exception | Update transport capability | No learned proposition or improvement license established | see cited route | see cited route | SRC-1, `src/jaz/llm/sglang.py` | [EPI-CLM-agent-optimization](#epi-clm-agent-optimization) | none | Server application, algorithm and later behavioral effect unobserved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-repl-work](runtime.md#rt-clm-repl-work) | see cited record | SRC-1, `src/jaz/__init__.py`; doctrine/design | see cited record | [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | none supplied | Suppliers can bypass model or REPL | Model-directed iterative computation is wired | Not a warrant that returned answers are true. |
| [EPI-CLM-agent-optimization](#epi-clm-agent-optimization) | see cited record | SRC-1, `README.md`; doctrine/design | Framework positioning, not a specified accuracy guarantee | [EPI-RTE-budget-forcing](#epi-rte-budget-forcing), [EPI-RTE-rollout-export](#epi-rte-rollout-export), [EPI-RTE-weight-update](#epi-rte-weight-update), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) | none supplied | Training/evaluation driver absent; no intervention comparison | Provides iteration, recording/export and update affordances for optimization | Improved capacity, autonomous optimization and causal benefit not established. |
| [EPI-CLM-model-validation](#epi-clm-model-validation) | see cited record | SRC-1, `src/jaz/console.py`; doctrine/design plus implementation | Candidate tested before `switch_model` installs it | [EPI-RTE-model-ping](#epi-rte-model-ping) | none supplied | One minimal request cannot identify future availability | Ping gates this model switch; ordinary exceptions preserve previous component | Source itself admits a validated pair can fail seconds later; literal future guarantee unsupported. |
| [EPI-CLM-rollout-fidelity](#epi-clm-rollout-fidelity) | see cited record | SRC-1, `src/jaz/hooks/builtin/rollout.py`; doctrine/design | Structural lineage and loss-mask rationale | [EPI-RTE-rollout-export](#epi-rte-rollout-export) | none supplied | No independently inspected complete stamp-to-wire trace; no trainer | Exact projections conditional on trusted records; no fabricated rollout on token-less completion | Cannot elevate “ground truth” into independently authenticated execution or accepted task knowledge. |
| [EPI-CLM-code-framing](#epi-clm-code-framing) | see cited record | SRC-1, `src/jaz/protocol/code_only.py`; attributed reported operation | Source explicitly narrows robustness claim and rejects general performance inference | [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | Reported measurements only; no supplied raw runs | Clustered task comparison, heavy-tail sensitivity and non-replicating controlled reproduction stated in source | Maintainers report a context-dependent robustness basis for code-only framing | Not an independently verified causal effect or general success improvement. |

## Bounded conclusion

**JAZ grants execution authority more broadly than it grants epistemic warrant.** Model or replay response text can reach Python execution; native return can terminate the task. Neither constitutes evidence-consuming acceptance of a proposition for a specified use. Execution feedback is useful evidence about a particular computation, bounded by its premises, bindings, supplied-result seams and observation losses. No concrete supplied answer lets this analysis establish warranted entailed derivation or ampliative conjecture; failure to prove entailment is not evidence of non-entailment. [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop), [RT-BAP-response-execution](runtime.md#rt-bap-response-execution), [EPI-RTE-observation-cut](#epi-rte-observation-cut).

**Checks have different licenses.** ReturnType licenses type conformity. ValidateREPLCode licenses caller-policy source admission before execution, whereas ValidateReturn can reject an already-produced result and feed criticism back into the same invocation. A substantive evidence-consuming callback could implement task acceptance, but this package does not supply its criterion, reference answer, intended use or domain. It would be misleading either to call every completion accepted knowledge or to assert that the runtime cannot host knowledge acceptance. Counter cleanup does not withdraw retained claims, and output rejection does not undo effects. [RT-RTE-hook-control](runtime.md#rt-rte-hook-control), [EPI-RTE-code-validation](#epi-rte-code-validation), [EPI-RTE-return-validation](#epi-rte-return-validation).

**The helper has separate factual and action paths.** It is instructed to consult configuration, reference and source before answering; that is implemented guidance, not demonstrated grounding. Text answers print without semantic acceptance; snippets undergo syntactic fence cleanup and then human action consent, not proof of correctness. The model ping is a real environment check, but licenses only success of the minimal request. Its switch consumer changes session configuration and attempts durable persistence; it is not an evaluator of answer quality or a guarantee of the next request. [EPI-RTE-helper-unwrapping](#epi-rte-helper-unwrapping), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), [EPI-RTE-model-ping](#epi-rte-model-ping).

**Retention and reuse do not establish lifecycle integration after epistemic acceptance.** Console turns retain both successes and errors; replay admits saved responses to code execution; workflow emission can preserve failed runs; rollouts preserve partial trajectories but withdraw records if a completed query lacks token stamps. The rollout export gate evaluates representation compatibility, not task success, and permits other projections when flat export fails. No acceptance-linked evidence integration route was established in these inspected mechanisms. This is a bounded finding, not a negative about arbitrary host hooks or trainers. [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission), [EPI-RTE-rollout-export](#epi-rte-rollout-export), SRC-1 `src/jaz/console.py`.

**Continuation and parameter replacement are independent of learning evidence.** BudgetForcing changes continuation without truth evaluation. SGLang exposes explicit weight-update transport; therefore the ordinary completion route cannot justify a package-wide claim that parameter updates are impossible. Provider/server parameter application, training criteria and improved future capacity remain uninspected. Learning benefit is unestablished, not contradicted by that opacity. The helper can represent current configuration and change it through an approved snippet, but reliable use, formulated content-directed criticism, repeated theory revision and autonomous optimization are not demonstrated. The reported framing experiment is historical attributed evidence, not an implemented runtime critic. These conclusions do not collapse reflection, autonomy, theory building and self-improvement into one status. [EPI-RTE-budget-forcing](#epi-rte-budget-forcing), [EPI-RTE-weight-update](#epi-rte-weight-update), [EPI-CLM-code-framing](#epi-clm-code-framing), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-observation-text
Label: Rendered REPL observation

Part of: [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer)

The observation is a natural-language string in a user-role message dictionary, interpreted by the model. Its producer reads an execution result's output and abbreviates it. It is distinct from the full output/exception parts of [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state). SRC-1, `src/jaz/protocol/code_only.py`, implementation:

> return [{"role": "user", "content": abbreviated_output}]
> --- `src/jaz/protocol/code_only.py`

#### EPI-OBJ-helper-response
Label: Helper response tuple

Part of: [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)

This object is the tagged return within that route, not another invocation route. The Python tuple supplies symbolic dispatch through its kind and a string whose answer branch is human-readable natural language, while its code branch becomes symbolic Python after cleanup and approval. Storage is a native return value, then HelperHistory entries within the console session. SRC-1, `src/jaz/console.py`, implementation and task guidance:

> kind, content = raw
>     # Fences only make sense to strip on code; an answer is printed verbatim.
>     return kind, (_strip_code_fences(content) if kind == "code" else content)
> --- `src/jaz/console.py`

> "- Return ('answer', text) for any QUESTION: read the answer off `config` for "
> --- `src/jaz/console.py`

The task guidance is an instruction to the model, not observed compliance. The branch and response-shape mechanism are also covered by [RT-RTE-settings-change](runtime.md#rt-rte-settings-change).

#### EPI-OBJ-rollout
Label: Rollout and export samples

A frozen Python dataclass holds tuples of symbolic token IDs, context lineage, numerical logprob values and terminal facts. Numeric token/logprob arrays here are localized recorded values consumed by fixed export rules, not the model's distributed-parametric weights. FlatSample/TurnSample project that record for an external consumer. This is distinct from [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) and the text/exec artifacts in [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay): none is a token-stamp rollout. SRC-1, `src/jaz/hooks/builtin/rollout.py`, implementation:

> invoke_id: str
>     depth: int
>     turns: tuple[TurnRecord, ...]
>     finished: str
>     model: str
> --- `src/jaz/hooks/builtin/rollout.py`

### Routes

#### EPI-RTE-code-validation
Label: ValidateREPLCode check and veto

Part of: [RT-RTE-hook-control](runtime.md#rt-rte-hook-control)

This material part is the source-predicate seam, separate from return-value validation and generic effect composition. SRC-1, `src/jaz/hooks/builtin/repl_code_hooks.py`, implementation. The caller installs a validator and tolerance; model code proposes the candidate; Python callback decides, and the hook can veto. It is open-request validation, with no intrinsic answer oracle or improvement trigger. Success emits no veto. No human decision per candidate is required. Guidance is the caller predicate, whose content is unspecified.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: No effect on predicate pass; SupplyExecResult(Continue) on tolerated exception, Abort beyond the cap.
- Later read-back: inapplicable — the failure counter is working invocation state, not later-invocation retained knowledge.
- Delegated visibility: Context-managed hook applies in nested invokes; positional hook applies locally, with per-invoke counters.
- Selection predicate: REPLExecSend committed source; any ordinary predicate exception rejects, count greater than max_failures aborts.
- Invalidation or expiry: InvokeExit removes the counter; valid turns do not reset accumulated failures. Prior effects are not rolled back.
- Activation or effect: Dispatcher consumes the supplier to skip code and feed error text into the next model turn, or consumes Abort to end the run. Channel is committed-source validation; force is enforcing; horizon is this turn/invocation.
- Evidence limits: Callback truth criterion and quality are external. This checks source strings, not runtime return values or all host effects.

> try:
>             self.validator(event.code)
>         except Exception as exc:  # noqa: BLE001 — any validator exception is a rejection
> --- `src/jaz/hooks/builtin/repl_code_hooks.py`

> return [Abort(error=exc)]
> --- `src/jaz/hooks/builtin/repl_code_hooks.py`

> SupplyExecResult(
>                     result=Continue(
> --- `src/jaz/hooks/builtin/repl_code_hooks.py`

#### EPI-RTE-return-validation
Label: ValidateReturn check and disposition

Part of: [RT-RTE-hook-control](runtime.md#rt-rte-hook-control)

This is the return-predicate material part rather than the source veto or type checker. SRC-1, `src/jaz/hooks/builtin/return_hooks.py`, implementation. A host-supplied callback consumes a native Return value after execution; its nonraising return permits continuation toward completion. The model proposes the value, callback decides, effect composition applies its result, and final validation can veto terminal Return. No per-value human intervention or answer oracle is established. Operating mode is caller-defined open-request validation. The predicate supplies guidance/criterion only to the extent its actual implementation does so; the package defines no improvement objective.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: No override on pass; ModifyExecResult(Continue) for tolerated rejection; Raise past cap; final callback exception becomes ModifyInvokeResult(Raise).
- Later read-back: inapplicable — cached checked Return identity and failure counts are current-invoke state, not durable accepted claims.
- Delegated visibility: Context-managed validator applies in nested invokes with separate counts; positional installation is local.
- Selection predicate: Return instances only. InvokeComplete skips callback reexecution for the exact already-passed Return object, and checks a different final Return.
- Invalidation or expiry: InvokeExit clears failures and passed-object cache; this cleanup neither retracts external claims nor reverses side effects. A failed final value becomes a terminal exception.
- Activation or effect: Complete-stage effects alter the Agent loop's result. Rejection error text reaches the model for another attempt, or Raise reaches the public caller; force is enforcing result disposition over the current invocation.
- Evidence limits: Post-execution rejection is not pre-effect admission. Same-object identity reuse does not independently prove immutability of a mutable return payload; hook bug handling follows the runtime qualification.

> if isinstance(result, Return) and result is not already_ok:
>             try:
>                 self.validator(result.return_value)
>             except Exception as exc:  # noqa: BLE001 — any validator exception is a rejection
>                 effects = [ModifyInvokeResult(result=Raise(exception=exc))]
> --- `src/jaz/hooks/builtin/return_hooks.py`

> return [ModifyExecResult(result=Raise(exception=exc))]
> --- `src/jaz/hooks/builtin/return_hooks.py`

> self._validated_ok[event.invoke_id] = result
> --- `src/jaz/hooks/builtin/return_hooks.py`

#### EPI-RTE-observation-cut
Label: Output abbreviation

Part of: [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop)

The selected material transformation changes what execution evidence reaches the model; it is not a separate task evaluator. SRC-1, `src/jaz/protocol/code_only.py` and `src/jaz/string_utils.py`, implementation. A concrete source deduction: for `string='ABERRCD'`, `max_length=4`, `prefix_ratio=0.5`, the code calculates prefix=2, suffix=2, omitted=3 and returns `AB[...3 characters omitted...]CD`. An error indicator in the omitted span disappears. This is a deterministic code trace, not target execution. It disproves lossless-observation delivery, but not lossless availability of the unabridged Continue output in history.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A user-role message containing abbreviated output; full output retained separately in the protocol history entry for Continue.
- Later read-back: inapplicable — this is ordinary current-run observation/history, not automatic later-invocation memory.
- Delegated visibility: Child contexts do not automatically inherit the parent observation; explicit passed data follows the runtime recursion route.
- Selection predicate: Output length exceeds configured maximum; configured prefix ratio chooses retained ends, with no semantic ranking.
- Invalidation or expiry: Message lifetime follows the invocation buffer and installed message-edit hooks; whole Continue output remains reachable through current REPL history.
- Activation or effect: The next model query receives only the selected observation text unless it explicitly consults history. Force is advisory/evidentiary through model interpretation; horizon is later turns in that invocation.
- Evidence limits: Under a custom REPL, even history may already contain truncated data. No particular omitted real-world claim or behavioral effect is supplied.

> abbreviated_output, _ = abbreviate_string(
>             output,
>             max_length=self.max_repl_output_length,
>             prefix_ratio=self.truncation_prefix_ratio,
>         )
> --- `src/jaz/protocol/code_only.py`

> prefix_length = int(prefix_ratio * max_length)
>     suffix_length = max_length - prefix_length
>     omitted = len(string) - prefix_length - suffix_length
> --- `src/jaz/string_utils.py`

> f"{string[:prefix_length]}[...{omitted} characters omitted...]{suffix}",
> --- `src/jaz/string_utils.py`

#### EPI-RTE-helper-unwrapping
Label: Helper code-fence cleanup

Part of: [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)

This part changes a proposed code string before the human gate; it is not CodeOnlyProtocol.parse. SRC-1, `src/jaz/console.py`, implementation. For a helper code response whose content is the whole fenced string ` ```python\nx=1\n``` `, the regex capture is `x=1`, and `.strip()` produces `x=1` for display and possible host compilation. This source deduction does not execute code. The ordinary Agent parser, by contrast, does not remove markdown fences. Cleanup can make previously non-Python wrapper text executable; it is not semantic validation of the body.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Code response with single whole-string wrapper removed, or stripped original string; answer response unchanged.
- Later read-back: HelperHistory remembers the resulting proposal, including applied status, for later helper requests; detailed consumers are in the parent route.
- Delegated visibility: Helper receives textual history and configuration, not automatic live mutable configuration access.
- Selection predicate: Code-tag branch and regex whole-string fence match; no body-correctness criterion.
- Invalidation or expiry: Human rejection prevents current execution, not retention of the unapplied proposal. Session history lifetime follows console state.
- Activation or effect: Display and confirmation consume the cleaned string; approved content enters host compile/exec. This transformation prepares execution authority, while the separate gate supplies permission.
- Evidence limits: No evidence of a successfully applied snippet. Task text asks for source-grounded answers but that request does not establish model compliance.

> return m.group(1).strip() if m else text.strip()
> --- `src/jaz/console.py`

The parent response object's passage establishes that only code enters this function; the parent route supplies the human-confirmation/exec passages.

#### EPI-RTE-model-ping
Label: Live model probe and switch

This adds a specific environment evaluator and consumer not individuated by [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), which concerns `%` helper proposals. It changes the configured component in [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend). SRC-1, `src/jaz/console.py`, implementation. The caller chooses a model/backend; `_ping_llm` asks the backend for a minimal `ping` completion, treating ordinary Exception as failure and ignoring response content. `switch_model` calls configure only after success, then attempts settings persistence. A failure to persist can leave the live switch effective. The source also says direct configure and startup flags bypass this probe; this is not a universal model admission policy. The provider is an availability evaluator for this request, not an expected-answer oracle. Human/caller selection is not computational optimization.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Probe returns None or an exception; switch raises on failure or configures the new component and reports persistence scope.
- Later read-back: Successful persistence stores model/backend defaults for console startup; it is not retained evaluation evidence or a pinned model-weight version.
- Delegated visibility: Later invocations resolve active configuration; the ping does not pass a task reference answer into recursive calls.
- Selection predicate: Known backend, nonempty model, no ordinary probe exception; Copilot omits sampling cap while other backends receive max_tokens=16.
- Invalidation or expiry: Failed ping leaves current component unchanged; no expiry of a successful availability judgment is implemented. Future request failure still possible. Recovery is another switch/configuration or setup.
- Activation or effect: Probe result gates `jaz.configure(llm=llm)`; configuration reaches later model requests. Channel is component replacement, force permissive/enforcing admission, horizon session and persisted startup defaults.
- Evidence limits: Minimal successful round-trip does not prove any output proposition, capability on larger tasks or future availability. Server/provider behavior is external; no ping was executed here.

> backend.complete(model, [{"role": "user", "content": "ping"}], **kwargs)
> --- `src/jaz/console.py`

> error = _ping_llm(llm, model)
>     if error is not None:
>         raise ValueError(_describe_ping_failure(model, error, backend)) from error
>     jaz.configure(llm=llm)
> --- `src/jaz/console.py`

#### EPI-RTE-budget-forcing
Label: BudgetForcing continuation

This is a distinct optional continuation policy within the effect surface of [RT-RTE-hook-control](runtime.md#rt-rte-hook-control), not the monetary/call limit. SRC-1, `src/jaz/hooks/builtin/budget_forcing.py`, implementation. Caller refusal count/text governs the policy; model finishing attempts trigger it. No evidence or answer oracle assesses the candidate's quality. Software decides continuation, without per-finish human judgment. It is an open-request work-extension mechanism, not a bounded learning experiment. The candidate behavior change is another turn; nothing installs a new lasting policy.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ModifyExecResult with recoverable Continue and BudgetForcingError, or no effect after refusals exhausted.
- Later read-back: inapplicable — only per-invocation counter state and ordinary current-turn feedback are maintained.
- Delegated visibility: Context-managed use propagates with separate per-invoke counts; positional use is local.
- Selection predicate: Return or Raise result while configured refusal count remains positive.
- Invalidation or expiry: Counter decremented on refusal and removed at InvokeExit; prior side effects are not undone. Budget/last-iteration coordination gaps are explicitly documented in the source.
- Activation or effect: Agent consumes the transformed Continue and sends refusal text as feedback, requiring another turn until another limit ends the run or the policy permits finishing. Force enforcing continuation, horizon current invocation.
- Evidence limits: More work is not evidence of better reasoning or improved answer; no evaluated benefit supplied.

> if isinstance(result, (Return, Raise)):
>             self._refusals_remaining[event.invoke_id] = remaining - 1
>             return [_refuse(self.refusal_text)]
> --- `src/jaz/hooks/builtin/budget_forcing.py`

#### EPI-RTE-rollout-export
Label: Rollout retention and export admission

Distinct from ATIF replay and workflow materialization in [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) and [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission), this route accumulates token-native backend TurnRecords, freezes a Rollout at exit and exports projections. SRC-1, `src/jaz/hooks/builtin/rollout.py`, implementation. Backend records propose the accumulated content; recorder software decides token-presence admission. Export software decides flatness; caller chooses flat, pieces or turn projections. No task answer oracle or reward is built in. A trainer can judge results externally, but that consumer/criterion is not supplied. This is an open recording/export mode, not itself a parameter-training loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Observer emits no execution override; completed records accumulate in `rollouts`. Export yields FlatSample/list projections or NonMonotoneRolloutError.
- Later read-back: Caller can inspect/export records for external training; no automatic later Agent invocation or trainer is wired by this recorder. Serialization and training use remain external choices.
- Delegated visibility: Context-managed recorder sees nested invokes, demultiplexed by invoke_id rather than sharing one flat parent trajectory.
- Selection predicate: Completed query with tokens; a token-less completed response stands the invoke down and drops partial log. Flat export checks adjacent context prefix stamp IDs and lengths; pieces/turn samples provide alternatives.
- Invalidation or expiry: Token-less completion withdraws the invoke's pending rollout; setup resets collector state on reactivation. Aborted/failed outcomes retain partial records if token records exist. Nonmonotonicity refuses a flat projection, not the underlying data.
- Activation or effect: Export gate constrains what caller receives as a single training sequence; loss masks target owned sampled spans rather than all assistant text. Channel is returned sample objects, force enforcing representation compatibility, horizon external consumer chosen by caller. Actual training is unobserved.
- Evidence limits: Trusted stamps are premises, not independently checked wire evidence. No correctness acceptance, optimizer, parameter update consumer or demonstrated learning benefit is supplied for these exports.

> self._stood_down.add(event.invoke_id)
>                 self._log.pop(event.invoke_id, None)
>                 return []
> --- `src/jaz/hooks/builtin/rollout.py`

> return len(cur.sent) >= len(expected) and all(
>         a.message_id == b.message_id for a, b in zip(expected, cur.sent, strict=False)
>     )
> --- `src/jaz/hooks/builtin/rollout.py`

> for prev, cur in zip(self.turns, self.turns[1:], strict=False):
>             if not _extends(prev, cur):
>                 raise NonMonotoneRolloutError(
> --- `src/jaz/hooks/builtin/rollout.py`

> if stamp.sampled_span is not None and stamp.message_id in own_samples:
> --- `src/jaz/hooks/builtin/rollout.py`

#### EPI-RTE-weight-update
Label: SGLang weight-update transport

This is a separate exposed operation on the backend component, not the ordinary completion route in [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend). SRC-1, `src/jaz/llm/sglang.py`, implementation. Explicit methods post disk paths, distributed-group configuration or tensor payloads to serving-engine endpoints. A caller/trainer determines the candidate update and invokes the method; `_post` checks HTTP status, not improvement. No local reference outcome, theory criticism or training algorithm decides acceptance. Server-side veto/application/recovery are uninspected. Pause/continue and release/resume methods are adjacent operational controls, not quality checks. Guidance, selection objectives and rollback weights are external.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP JSON response or None for non-JSON success; mapped or original exception on request/status failure.
- Later read-back: uninspected — updated server weights could shape later completions, but no supplied server state or subsequent run establishes loading or consumption.
- Delegated visibility: Backend object can be used by host/trainer; automatic exposure of update methods to agent code is not established.
- Selection predicate: Explicit API method and payload; response.raise_for_status is a transport gate, not a model-quality criterion.
- Invalidation or expiry: Parameter lifetime, rollback and exact version pinning remain server/caller responsibilities. Source can request further replacement; no local quality-triggered rollback is shown.
- Activation or effect: Wired outbound update request; server application and later behavior remain uninspected. Intended consumer is serving engine, channel HTTP endpoint, force update-capable under its external contract, horizon subsequent serving operation.
- Evidence limits: Distributed-parametric weights, exact revision and change during any run are unknown. Mutable server can resolve to changed weights; an API request alone is neither learning nor exercised self-improvement.

> return self._post(
>             "update_weights_from_disk", {"model_path": model_path, **options}
>         )
> --- `src/jaz/llm/sglang.py`

> response = self._http.post(
>                 f"{self.base_url}/{endpoint}",
>                 json=payload or {},
>                 timeout=_DEFAULT_TIMEOUT_SECONDS,
>             )
>             response.raise_for_status()
> --- `src/jaz/llm/sglang.py`

### Claims

#### EPI-CLM-agent-optimization
Label: Building and optimizing agents

A broad framework-purpose claim distinct from the concrete REPL computation claim [RT-CLM-repl-work](runtime.md#rt-clm-repl-work). SRC-1, `README.md`, doctrine/design:

> A Python framework for building and optimizing LLM-agents through intelligent, iterative execution.
> --- `README.md`

#### EPI-CLM-model-validation
Label: Validated model switch

The console asserts a future-availability guarantee for a successful switch, a different warrant claim from the human snippet gate [RT-RTE-settings-change](runtime.md#rt-rte-settings-change). SRC-1, `src/jaz/console.py`, doctrine/design:

> # round-trip buys the one guarantee that matters: the user is never switched onto a
>     # model that then fails their next real turn.
> --- `src/jaz/console.py`

Counterevidence in the same implementation bounds that claim to the probe rather than the next turn:

> # validated pair broke in the last seconds (or the provider is flapping) —
>             # re-prompting forever would be a worse loop than reporting it. A successful
> --- `src/jaz/console.py`

The actual gate is documented by [EPI-RTE-model-ping](#epi-rte-model-ping); a provider can change state after the probe, so no future-request invariant follows.

#### EPI-CLM-rollout-fidelity
Label: Structural token fidelity

Distinct warrant claim for token records, not the execution narrative in [RT-CLM-repl-work](runtime.md#rt-clm-repl-work). SRC-1, `src/jaz/hooks/builtin/rollout.py`, doctrine/design:

> # * The recorder is an ACCUMULATOR, NOT A VERIFIER — and export does not verify either.
> #   The record is the GROUND TRUTH of what the model saw and produced: token truth lives
> #   in the frozen stamps the messages own, the TurnRecord references only frozen data, and
> #   nothing is ever re-derived — so nothing can drift. Fidelity is STRUCTURAL: the backend
> --- `src/jaz/hooks/builtin/rollout.py`

The same source expressly leaves judgments outside the record:

> # * Rollout deliberately has NO `reward` field (executive call, user, 2026-08-13). The
> #   record holds facts about the trajectory; a reward is a judgment about it, and its
> --- `src/jaz/hooks/builtin/rollout.py`

#### EPI-CLM-code-framing
Label: Reported code-only robustness comparison

No counterpart in the supplied runtime claim: this is an attributed historical design/evaluation argument, not the implemented runtime evaluator. SRC-1, `src/jaz/protocol/code_only.py`, reported operation and doctrine/design within the one registered source:

> # **Task scores did not favor it, and are not significant either way.** SWE-bench resolved 20.0%
> # [9.5%, 37.3%] for BOTH arms (Fisher p=1.0). StuLife 93.5% vs 92.3% and Recall 100% vs 100% are
> # single episodes: n=1, no interval, not estimates. This default rests on robustness, NOT on
> # performance.
> --- `src/jaz/protocol/code_only.py`

> # So the advantage is specific to SWE-bench-shaped work, or needs more power to see elsewhere. It
> # is not a demonstrated general property of the framing.
> --- `src/jaz/protocol/code_only.py`

The source describes instance-level sampling, a heavy-tail-sensitive contrast and a controlled reproduction that did not separate arms. Raw runs are not supplied; these comments cannot establish independently observed operation or causal benefit in this analysis.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
