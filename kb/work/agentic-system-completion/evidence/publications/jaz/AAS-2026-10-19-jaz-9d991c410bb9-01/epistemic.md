---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "JAZ epistemic routes: candidate generation, validator authority, observation loss and replay reliance at the frozen release."
run-id: AAS-2026-10-19-jaz-9d991c410bb9-01
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
---

# JAZ epistemic report

## Source-and-claim boundary

The question is which JAZ routes produce or acquire truth-apt content, what checks license reliance, and which consumers act on the results. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, but no supplied execution or causal experiment. This report assesses the enclosing runtime, including console, optional hooks and shipped tools, not an imagined knowledge-base application.

JAZ can execute code that computes answers, obtains evidence or criticizes a previous answer. That open capacity is not evidence that an identified proposition was derived from warranted premises or accepted against an evidence-consuming criterion. Candidate content depends on the task, tool results and provider output. The concrete proposition and source warrant are not determinable without such inputs. The configured model's parameters, endpoint mutability and missing exact weight pin are see [RT-CMP-llm](runtime.md#rt-cmp-llm). No provider-internal learning finding follows from this source.

The scoped public/design claims assessed here are [EPI-CLM-hook-contracts](#epi-clm-hook-contracts), [EPI-CLM-protocol-framing](#epi-clm-protocol-framing) and [EPI-CLM-token-rollouts](#epi-clm-token-rollouts). The policy claim is see [RT-CLM-repl-policy](runtime.md#rt-clm-repl-policy). These are validation, representation and execution claims, not a blanket public claim to produce accepted knowledge.

### Coverage

“Direct” means this analyst read the source; “supplied” means the runtime record supplies the inspected mechanism and passage. Available but uninspected paths are not access gaps or evidence of absence.

| Entry point or operation | Source path, SRC-1 | Coverage and limits |
|---|---|---|
| Installed/module console and command/file/pipe/interactive dispatch | `src/jaz/console.py`; `pyproject.toml`; `src/jaz/__main__.py` | Direct main dispatch; supplied [RT-RTE-console-turn](runtime.md#rt-rte-console-turn). These share a namespace and dispatch to host Python or invocation. |
| Public sync/async invoke, model/code/observation, recursion | `src/jaz/invoke.py`; `src/jaz/_agent.py`; `src/jaz/_invoke_tool.py` | Supplied [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop), [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke). Custom components and actual task semantics remain unknown. |
| Prompt, response parser, observation/history projection | `src/jaz/protocol/code_only.py`; `src/jaz/string_utils.py` | Direct complete reads; [EPI-RTE-observation-projection](#epi-rte-observation-projection). Default codec only; arbitrary custom codec semantics unassessed. |
| Registered built-in hooks, code/type/value validators and cleanup | `src/jaz/hooks/builtin/__init__.py`; `src/jaz/hooks/builtin/repl_code_hooks.py`; `src/jaz/hooks/builtin/return_hooks.py` | Direct exports and implementations; supplied dispatcher/result consumers [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission). Compiler policy is supplied runtime evidence, not an answer oracle. |
| Early-finish refusal | `src/jaz/hooks/builtin/budget_forcing.py` | Direct complete read; new material route [EPI-RTE-budget-forcing](#epi-rte-budget-forcing). |
| Replay serving, comparison, fallback | `src/jaz/hooks/builtin/replay.py` | Direct serving, response and observation comparison, normalization; [EPI-RTE-replay-comparison](#epi-rte-replay-comparison). Tree conversion and concurrent stack ownership not audited end to end. |
| Trace recording, workflow emission, later consumers | `src/jaz/hooks/builtin/atif_trace.py`; `src/jaz/hooks/builtin/workflow_replay.py` | Supplied [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission). Emitter does not certify success or equivalence. |
| Token-native rollout accumulation/export | `src/jaz/hooks/builtin/rollout.py` | Direct complete read; [EPI-RTE-rollout-export](#epi-rte-rollout-export). Backend stamp creation and remote training uninspected; prevents verification of the whole token-fidelity claim, not inspection of the export predicate. |
| Settings helper, cleanup, confirmation, ping, settings reload | `src/jaz/console.py`; `src/jaz/user_settings.py` | Direct fence stripping and dispatch; supplied [RT-RTE-settings-admission](runtime.md#rt-rte-settings-admission), [RT-BAP-settings-load](runtime.md#rt-bap-settings-load). Human confirmation licenses execution, not truth. |
| Registered SWE tools | `src/jaz/_library/swe.py` | Direct complete read; [EPI-RTE-swe-tools](#epi-rte-swe-tools). Only available if granted; arbitrary shell programs are not inspected evaluators. |
| Ancillary extraction/converters/loggers | `src/jaz/utils/extract_git_diff.py`; `src/jaz/utils/log_to_markdown.py`; `src/jaz/utils/trace_to_directory.py`; `src/jaz/hooks/builtin/trajectory_directory.py`; tracing/logging hooks | Direct diff extractor: copies a supplied field, no patch applicability check. Other converters and telemetry paths uninspected here; no system-complete negative about all lineage transformations is made. |
| Resource/depth governance, credentials and alternative adapters | `src/jaz/hooks/builtin/budget_pool.py`; `src/jaz/hooks/builtin/iteration_limit.py`; `src/jaz/hooks/builtin/recursion_limit.py`; `src/jaz/credentials.py`; `src/jaz/llm/` | Supplied runtime governance/adapter coverage only. Full adapter metadata fidelity and governance composition remain unassessed, preventing universal route or containment claims. |

No execution trace ties a particular available answer, code artifact or rollout to a successful check. No experiments compare validator/replay effects on task quality. Those missing evidence items respectively prevent observed acceptance and causal benefit conclusions. The unshipped evaluation environment prevents checking the protocol's numerical reports; it does not make the inspected parser opaque.

## Epistemic-object inventory

Owned fields are see the cited declaration; these rows add only the candidate-content assessment.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | Operational instructions; embedded tool/domain descriptions can make claims | see record | SRC-1, `src/jaz/templates/system_prompt.jinja2` | Textual request is not enforced compliance or domain evidence. |
| [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | Host inputs/tool objects may contain claims; concrete propositions not determinable | see record | SRC-1, `src/jaz/repl/python_repl.py` | Container and shared references do not authenticate supplied content. |
| [EPI-OBJ-llm-response](#epi-obj-llm-response) | Code/comments can assert propositions; code can also be purely imperative | see record | SRC-1, `src/jaz/protocol/code_only.py` | Novel truth-apt content versus reshaping/derivation needs actual input/output. |
| [EPI-OBJ-repl-observation](#epi-obj-repl-observation) | Claims about execution/output and recoverable failures | see record | SRC-1, `src/jaz/protocol/code_only.py` | Abbreviation can remove the only error text; terminal history loses output. |
| [EPI-OBJ-return-value](#epi-obj-return-value) | Returned object may encode a task answer or none | see record | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | Type membership is not answer truth; user predicate's evidence and criterion unknown. |
| [EPI-OBJ-rollout](#epi-obj-rollout) | Token/conditioning/finish facts, not reward or task-correctness judgment | see record | SRC-1, `src/jaz/hooks/builtin/rollout.py` | Export checks structure, not provenance back to an actual provider execution. |

## Authority-route ledger

Each row assesses a distinct consequential function. Repeated record citations refer to different functions of the same mechanism, not new declarations. All implementation routes below are conditional on invocation/configuration and are unobserved in this run. “See” delegates owned facts, not this ledger's architectural assessment.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | content transformation | implemented | [EPI-OBJ-llm-response](#epi-obj-llm-response) | truth-apt transformation: indeterminate | Inputs to model output | Provider model; open tasks | see record | Candidate code/comments | Generation only | No inherent warrant; source warrant unknown | Candidate reaches admission | see [RT-BAP-prompt-code](runtime.md#rt-bap-prompt-code) | SRC-1, `src/jaz/_agent.py` | none | none | Without concrete content, cannot distinguish reshaping, derivation or conjecture; not every response is truth-apt. |
| [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | check/evidence production | implemented | [EPI-OBJ-repl-observation](#epi-obj-repl-observation) | no content change | Code execution in granted environment | Compiler/interpreter/tool; execution domain only | see record | Output, exception or return | Execution and feedback | At most evidence of that code's bounded outcome, not task correctness | Continue or terminal branch | Executor → result kind → Agent; enforcing; invocation | SRC-1, `src/jaz/repl/python_repl.py` | [RT-CLM-repl-policy](runtime.md#rt-clm-repl-policy) | none | Actual grants and outcomes absent; tool success is not explanation or transfer evidence. |
| [EPI-RTE-swe-tools](#epi-rte-swe-tools) | content transformation | implemented | [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | truth-apt transformation: acquisition/import | File bytes or subprocess result to agent | OS/tool function; no source-truth test | If granted and called | Text or CompletedProcess | Data delivery | Source warrant unknown; no endorsement | Evidence becomes accessible to generated code | see record | SRC-1, `src/jaz/_library/swe.py` | none | none | Shell commands can implement arbitrary tests; their domains cannot be inferred from this wrapper. |
| [EPI-RTE-swe-tools](#epi-rte-swe-tools) | operational admission/selection/consumption | implemented | [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) | non-truth-apt policy/content update: literal file replacement | Proposed text replacement | Count predicate, file text domain | Before write | Reject missing/ambiguous match or write | Enforcing occurrence gate | No truth/correctness license for replacement | File changes immediately | Generated call → count check → write; enforcing; file lifetime | SRC-1, `src/jaz/_library/swe.py` | none | none | Claim-bearing replacements would need content-specific assessment; no semantic gate or rollback. |
| [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission) | check/evidence production | implemented | [EPI-OBJ-llm-response](#epi-obj-llm-response) | no content change | Committed code | Host validator; unspecified predicate domain | REPLExecSend | Exception or no exception | Check result feeds disposition | Only supplied predicate's criterion | No direct acceptance at check step | Validator → effect producer; invocation | SRC-1, `src/jaz/hooks/builtin/repl_code_hooks.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | Validator need not inspect evidence or answer truth. |
| [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission) | disposition/acceptance | implemented | [EPI-OBJ-llm-response](#epi-obj-llm-response) | no content change | Execute code or refuse | Validator exception and cumulative cap | After code check, before execution | Continue or Abort; otherwise normal execution | Veto; enforcing | Operational admission only | Rejected code skipped; model may retry | see [RT-BAP-hook-effects](runtime.md#rt-bap-hook-effects) | SRC-1, `src/jaz/hooks/builtin/repl_code_hooks.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | Does not undo earlier host/hook effects; no success benefit observed. |
| [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission) | check/evidence production | implemented | [EPI-OBJ-return-value](#epi-obj-return-value) | no content change | Return value's type membership | beartype is_bearable against host hint | Return at exec Complete; new final Return at InvokeComplete | Type error or pass | Feeds return disposition | Type-hint contract only | Determines return eligibility | ReturnType → result effects; invocation | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | External type checker implementation not audited; mutable payload can differ without changing Return identity. |
| [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission) | check/evidence production | implemented | [EPI-OBJ-return-value](#epi-obj-return-value) | no content change | Return value against caller predicate | ValidateReturn callable; domain supplied by host | Same event boundaries; same approved Return skips repeat | Raised exception or pass | Feeds return disposition | Unknown beyond predicate; no built-in reference answer | Determines return eligibility | Callable → ValidateReturn effects; invocation | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | Could be evidence-consuming in a host; no such concrete validator supplied. |
| [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission) | disposition/acceptance | implemented | [EPI-OBJ-return-value](#epi-obj-return-value) | no content change | Release, retry or terminal rejection | Installed ReturnType/ValidateReturn, per-invoke tolerance | After relevant check | Continue, Raise, or unmodified Return | Enforcing release gate | Satisfies installed checks, not generic truth acceptance | Rejected value withheld; prior effects survive | see [RT-BAP-hook-effects](runtime.md#rt-bap-hook-effects) | SRC-1, `src/jaz/hooks/builtin/return_hooks.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | Exit clears counters/approved identities, not external effects or previously retained claims. |
| [EPI-RTE-budget-forcing](#epi-rte-budget-forcing) | disposition/acceptance | implemented | [EPI-OBJ-return-value](#epi-obj-return-value) | no content change | Attempted Return or Raise | Remaining refusal count, not correctness | Exec Complete when enabled | Continue with caller's refusal text | Enforcing continuation | None: refusal is not evidence of an incorrect answer | Blocks early termination | see record | SRC-1, `src/jaz/hooks/builtin/budget_forcing.py` | none | none | More work need not improve answer; no evidence consumption. |
| [EPI-RTE-observation-projection](#epi-rte-observation-projection) | content transformation | implemented | [EPI-OBJ-repl-observation](#epi-obj-repl-observation) | truth-apt transformation: non-ampliative reshaping | Output to next model observation | Deterministic head/tail budget | Continue rendering | Shortened output and omission marker | Advisory text supply | Partial source text, not complete outcome evidence | Changes evidence available for next action | see record | SRC-1, `src/jaz/protocol/code_only.py` | none | none | Warrant degraded where qualifying/error text is removed; unchanged retained fragments do not recover missing context. |
| [EPI-RTE-observation-projection](#epi-rte-observation-projection) | retention | implemented | [EPI-OBJ-repl-observation](#epi-obj-repl-observation) | truth-apt transformation: non-ampliative reshaping | Result to history entry | Continue versus terminal result kind | Each finalized iteration | Full continuing output; terminal empty string | In-process retention | History records outcome projection, not endorsement | Reachable history can inform current work or escaped parent value | see record | SRC-1, `src/jaz/protocol/code_only.py` | none | none | Terminal output/exception omission prevents complete reconstruction from this record alone. |
| [EPI-RTE-replay-comparison](#epi-rte-replay-comparison) | check/evidence production | implemented | [EPI-OBJ-repl-observation](#epi-obj-repl-observation) | no content change | Message-edit signatures, response content, normalized rendered observations | Program equality in three distinct representation domains | Optional Send/Exit comparisons | Equality, mismatch, or skipped comparison | Mismatch latches divergence | Representation agreement only; no task-correctness license | Supplies selection state, not rollback | see record | SRC-1, `src/jaz/hooks/builtin/replay.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | Equality omits seed, in-place message mutations, wire projection, omitted output and token/cost-only changes. |
| [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) | operational admission/selection/consumption | implemented | [EPI-OBJ-llm-response](#epi-obj-llm-response) | truth-apt transformation: acquisition/import | Saved response to live code path | Queue availability, optional divergence latch | Query Send | Saved response or live provider fallback | Permissive reuse; live execution remains | Imported candidate; trace does not warrant task answer | Bypasses model calls, not code/tool effects | see record | SRC-1, `src/jaz/hooks/builtin/replay.py` | [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | none | Source warrant unknown; response/output mismatch cannot undo current turn or earlier side effects. |
| [RT-RTE-console-turn](runtime.md#rt-rte-console-turn) | retention | implemented | [EPI-OBJ-return-value](#epi-obj-return-value) | no content change | Prompt/input/result or failure into conversation history | Completed/failed turn, not truth check | After console turn | Live objects retained | Retention for later delivery | No implicit acceptance | Subsequent turns can inspect old objects | see record | SRC-1, `src/jaz/console.py` | none | none | Live references can change; no cross-session object restoration shown. |
| [RT-RTE-console-turn](runtime.md#rt-rte-console-turn) | operational admission/selection/consumption | implemented | [EPI-OBJ-return-value](#epi-obj-return-value) | truth-apt transformation: acquisition/import | Previous turns into later invocation | Nonempty history | Next prompt turn | conversation_history input | Model-mediated advisory context | Previous result, not automatically trusted evidence | May affect next code selection | see record | SRC-1, `src/jaz/console.py` | none | none | Delivery is wired; reliance and behavioral effect unobserved. |
| [RT-RTE-settings-admission](runtime.md#rt-rte-settings-admission) | disposition/acceptance | implemented | [EPI-OBJ-llm-response](#epi-obj-llm-response) | non-truth-apt policy/content update: confirmed host snippet | Helper proposal to host execution | Tuple/tag, TTY and human y/yes; model ping only connectivity | Before host exec / model switch | Discard or execute; ping failure rejects switch | Enforcing human gate for helper code | Execution consent, not truth or improved model quality | Host configuration/capabilities may change | see [RT-BAP-settings-load](runtime.md#rt-bap-settings-load) | SRC-1, `src/jaz/console.py` | none | none | Fence cleanup is formatting, not validation. Direct user Python bypasses helper gate legitimately. |
| [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) | retention | implemented | [EPI-OBJ-llm-response](#epi-obj-llm-response) | non-truth-apt policy/content update: event-derived executable artifact | Iterations to program files | Event selection and emitter, not semantic evaluator | Including abnormal exit | Durable Python artifacts | Write; later execution separate | No equivalence or success certificate | Makes later code execution available, not installed | see record | SRC-1, `src/jaz/hooks/builtin/workflow_replay.py` | none | none | Pre-edit stashed code can differ from committed source; no accepted claim integration follows. |
| [EPI-RTE-rollout-export](#epi-rte-rollout-export) | retention | implemented | [EPI-OBJ-rollout](#epi-obj-rollout) | truth-apt transformation: non-ampliative reshaping | Token-bearing responses to frozen rollout | Record presence and completed-query predicate | Exit; partial invokes also retained | Rollout or stand-down/drop partial log | Structural retention gate | Conditional trajectory facts only | Export available to caller | see record | SRC-1, `src/jaz/hooks/builtin/rollout.py` | [EPI-CLM-token-rollouts](#epi-clm-token-rollouts) | none | No rewards/trainer consumer supplied; missing token record withdraws this invoke's log. |
| [EPI-RTE-rollout-export](#epi-rte-rollout-export) | check/evidence production | implemented | [EPI-OBJ-rollout](#epi-obj-rollout) | no content change | Can turns share one flat sequence? | _extends checks length and message_id prefix agreement | to_flat; to_pieces instead splits | FlatSample or NonMonotoneRolloutError | Enforces flat-export eligibility | Monotone representation only, conditional on stamps | Blocks unsuitable flat projection, not turn export | see record | SRC-1, `src/jaz/hooks/builtin/rollout.py` | [EPI-CLM-token-rollouts](#epi-clm-token-rollouts) | none | Neither task reward nor truth check; backend token fidelity remains uninspected. |

No lifecycle-integration route for accepted ampliative claims is established by these records. This is a bounded result over the assessed mechanisms, not a claim that arbitrary host validators/tools cannot implement one. The early-finish refusal and token-export routes supplement runtime coverage rather than supersede its valid containers. Runtime's replay comparison caveat is refined locally: the output check calls the depth-resolved codec's render seam, rather than assuming default-codec abbreviation attributes.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-hook-contracts](#epi-clm-hook-contracts) | see record | SRC-1, `README.md`; doctrine/design | Hook table | [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission), [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), [EPI-RTE-replay-comparison](#epi-rte-replay-comparison) | None supplied | No quality comparison; generic predicates and equality have narrow domains | Type/value/code gates and replay→live fallback are implemented | “Validated” does not mean factually correct; replay agreement is not safe re-execution. |
| [EPI-CLM-protocol-framing](#epi-clm-protocol-framing) | see record | SRC-1, `src/jaz/protocol/code_only.py`; doctrine/design and reported operation | Source explains collision removal and reports narrower robustness comparisons | [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop) | Numerical reports only, no inspectable traces | Report names clustered instances and no task-score advantage; cannot independently check design/data | Parser does not search delimiters; embedded delimiters survive | Does not remove code over-escaping; no independently supported performance improvement. |
| [EPI-CLM-token-rollouts](#epi-clm-token-rollouts) | see record | SRC-1, `src/jaz/hooks/builtin/rollout.py`; doctrine/design | Token facts separated from driver reward | [EPI-RTE-rollout-export](#epi-rte-rollout-export) | None supplied | No trainer, reward or intervention; backend stamp origin not audited | Accumulation, no-token stand-down and structural export checks implemented | “Training-grade” not a knowledge-acceptance or learning-success certificate. |
| [RT-CLM-repl-policy](runtime.md#rt-clm-repl-policy) | see record | SRC-1, `src/jaz/repl/python_repl.py`; implementation/doctrine | see record | [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop), [EPI-RTE-swe-tools](#epi-rte-swe-tools) | None supplied | see record | Configured execution policy, not universal isolation | Correct execution or containment is separate from source truth. |

## Bounded conclusion

JAZ's model loop can produce candidate code and claim-bearing answers, and its Python/tool channel can acquire external evidence or compute results. No actual content pair here supports classifying a model answer as entailed derivation or ampliative conjecture. A concrete deterministic case does support non-ampliative observation reshaping: an interior error can be removed before the next model query while surviving in current-run history, see [EPI-RTE-observation-projection](#epi-rte-observation-projection). Import through file/tool/replay channels carries unknown source warrant; observation omission can degrade the evidence delivered to a consumer.

The consequential checking domains remain independent. Code validators judge committed source under host predicates; ReturnType judges type membership; ValidateReturn judges a supplied value predicate; replay checks selected representation agreement; rollout export checks monotone stamp lineage. Their consumers can block execution, withhold return, continue the model loop, switch replay to live calls, or refuse a flat export. None is an inherent factual-answer oracle. A host could supply evidence-consuming acceptance, but no named evidence criterion, intended use and accepted ampliative proposition are supplied here. Hence retention of console results, traces, workflows and rollouts is not evidence of lifecycle integration after such acceptance.

Withdrawal is local. Validator rejection withholds code or return, not already performed tool side effects. Exit cleanup clears bookkeeping, not false beliefs or external files. Replay divergence withdraws future saved-response service, not the turn just consumed. Missing token records drop a partial rollout; nonmonotone context blocks flat export but leaves alternative exports. BudgetForcing can reject an early finish without evaluating its content. These differences matter to what later behavior is actually controlled; see the separate ledger rows.

The settings helper provides a human-admitted behavior/configuration-change channel, while persisted settings select later providers. Neither a confirmation nor a connectivity ping establishes quality improvement. Workflow emission makes event-derived code available without installing or certifying it. Model parameter updates, observed learning, reflection, theory-directed criticism and exercised self-improvement are not established merely by these routes. Their uncertainty is separate from the positively established execution, retention, checking and configuration capacities. Backend internals, uninspected converters/custom components and absent traces/experiments prevent a system-complete negative and any system-wide epistemic score.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-llm-response
Label: LLM response content

Part of: [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop)

Material output object of that route, not a duplicate route. Source-native identity: LLMResponse.content, projected by CodeOnlyProtocol.parse. Form: symbolic Python source with natural-language comments/string content where present. Substrate: provider response and in-process message strings. Consumer: parser then REPL; comments may express reasons but need not be true or checked. SRC-1, `src/jaz/protocol/code_only.py`, implementation.

> return ParsedCode((llm_response.content or "").strip("\n\r"), None)
> --- `src/jaz/protocol/code_only.py`

For concrete source-text input `html = "<repl_code>hi</repl_code>"`, this expression removes only leading/trailing CR/LF. The inner closing tag is unchanged; no delimiter search truncates the literal. This is deduction from implementation, not executed target evidence. It supports the narrow framing claim, not the truth of any string or generated program.

#### EPI-OBJ-repl-observation
Label: REPL output and history projection

Part of: [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Material information product within the context-control route. Source-native identity: Continue.output, rendered observation and REPLHistoryEntry projection. Form: natural-language/tool-output text plus symbolic exception field; substrate: current invocation messages and history list. Checks/consumers differ: model receives abbreviated output; code reading history receives whole continuing output but terminal output is empty. SRC-1, `src/jaz/protocol/code_only.py`, implementation. These are distinct projections, not an authenticated execution transcript.

> repl_output=exec_result.output if isinstance(exec_result, Continue) else "",
> --- `src/jaz/protocol/code_only.py`

#### EPI-OBJ-return-value
Label: Return value

Part of: [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission)

The value tested by the return-validation part of that container, not the admission route itself. Source-native identity: Return.return_value. Form: arbitrary Python object; symbolic structure or natural-language proposition depends on payload. Substrate: live process object. Consumer: optional type/predicate hooks, then caller/parent or console history. No fixed claim content can be individuated without inputs and execution evidence. SRC-1, `src/jaz/hooks/builtin/return_hooks.py`, implementation.

> if not isinstance(result, Return):
>     return []
> try:
>     self.validator(result.return_value)
> --- `src/jaz/hooks/builtin/return_hooks.py`

This passage identifies the per-exec check. Passing a callable that returns False without raising is still success under this API; boolean return is not consulted.

#### EPI-OBJ-rollout
Label: Rollout

Distinct from [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state): a frozen tuple of token turn records and terminal facts, not a live REPL namespace. Source-native identity: Rollout/FlatSample/TurnSample. Form: symbolic numerical IDs, masks, log probabilities and metadata, not provider parameter weights. Substrate: hook-owned process objects and caller-exportable dictionaries. Consumer: caller's export API; a trainer is only an illustrated external consumer. SRC-1, `src/jaz/hooks/builtin/rollout.py`, implementation/doctrine.

> turns=tuple(turns),
> finished=finished,
> model=turns[-1].model,
> --- `src/jaz/hooks/builtin/rollout.py`

### Routes

#### EPI-RTE-observation-projection
Label: Observation abbreviation and history projection

Part of: [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Owner: CodeOnlyProtocol. Endpoints: finalized execution result → observation abbreviation and history projection → next model query/history reader. This is the deterministic, warrant-relevant part of context control; it is not a new generic context route. SRC-1, `src/jaz/protocol/code_only.py`; `src/jaz/string_utils.py`, implementation.

- Immediate return: A single user observation string for Continue, and a separately constructed history entry.
- Later read-back: inapplicable — ordinary history is current-run state; an escaped history object or console bridge requires the supplied runtime consumer routes.
- Delegated visibility: Child messages are not merged; returned/shared history can escape by reference, as bounded in the default protocol's history comments.
- Selection predicate: Output length versus max_repl_output_length; prefix_ratio chooses retained head/tail. History uses result kind rather than the abbreviation predicate.
- Invalidation or expiry: Ordinary invocation state ends with the frame unless retained/shared externally; omitted observation content remains in continuing history, but terminal output is discarded by this projection.
- Activation or effect: Next query receives only abbreviated text; a model's actual use or reload through history is unobserved.
- Evidence limits: No task trace; deterministic projection does not show which omitted fragment would change an answer. Custom codecs can differ.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> abbreviated_output, _ = abbreviate_string(
>     output,
>     max_length=self.max_repl_output_length,
>     prefix_ratio=self.truncation_prefix_ratio,
> )
> --- `src/jaz/protocol/code_only.py`

> prefix_length = int(prefix_ratio * max_length)
> suffix_length = max_length - prefix_length
> omitted = len(string) - prefix_length - suffix_length
> --- `src/jaz/string_utils.py`

> f"{string[:prefix_length]}[...{omitted} characters omitted...]{suffix}",
> --- `src/jaz/string_utils.py`

Concrete deduction, with no target execution: input `AAAAAAAAAAERRORBBBBBBBBBB`, content budget 10, ratio 0.5 has length 25. Prefix and suffix each retain 5 characters, omitted count 15. Rendered observation is `AAAAA[...15 characters omitted...]BBBBB`; `ERROR` vanishes. Continue history retains all 25 characters. This falsifies any unconditional inference that a recoverable error's text reaches the next model query. Error metadata is not separately rendered in this codec.

#### EPI-RTE-replay-comparison
Label: Replay divergence comparison

Part of: [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay)

Owner: TrajectoryReplay; this record isolates its checking subroute from saved-response serving. Endpoints: recorded edit/content/observation expectations plus live events → comparisons → per-node diverged latch → later serving branch. SRC-1, `src/jaz/hooks/builtin/replay.py`, implementation. The check target is representation agreement, not answer truth. Host enables detect_divergence; software decides mismatches; no human or expected task answer is involved. Open replay/live mode, not a controlled improvement experiment.

- Immediate return: Empty effects plus changed node.diverged state on a mismatch; comparison helpers return booleans.
- Later read-back: Recorded expectations from a saved trace are compared during a later invocation; the latch subsequently gates that node's saved responses.
- Delegated visibility: Each recorded child has a node; active-stack ownership is used, with concurrency correctness uninspected here.
- Selection predicate: Enabled detection; available expectations and completed event outcomes. Edit signatures compare at Send; post-transform response content at query Exit; rendered normalized observations at exec Exit.
- Invalidation or expiry: Divergence disables remaining saved responses for that invoke. Missing expectations skip their check; queue exhaustion independently causes live fallback.
- Activation or effect: Latch is consumed by on_llm_query_send; prompt-edit mismatch prevents serving that query, later mismatches affect subsequent queries. No rollback of committed content or prior effects.
- Evidence limits: Does not establish seed/wire/in-place-message equivalence, task success, or safe re-execution; trace loader and concurrency not fully inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return event.outcome.result.content != node.responses[index].content
> --- `src/jaz/hooks/builtin/replay.py`

> expected_norm = [_normalize_output(s) for s in expected]
> if actual != expected_norm:
>     node.diverged = True
> --- `src/jaz/hooks/builtin/replay.py`

> # diverging response itself is not re-served.
> if node.diverged:
>     return []
> --- `src/jaz/hooks/builtin/replay.py`

> s = _REPL_SESSION_ID_RE.sub("<repl_X>", s)
> s = _TRACEBACK_LINE_RE.sub(r"\1 N", s)
> return s.rstrip()
> --- `src/jaz/hooks/builtin/replay.py`

Agreement is after protocol rendering and these normalizations. With default abbreviation, different omitted interiors of equal length and identical retained edges can compare equal. This is a concrete countercase to full execution equivalence, not a defect in the stated narrower comparison criterion.

#### EPI-RTE-budget-forcing
Label: Budget forcing refusal

Distinct from [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission): this specific refusal policy does not evaluate source/type/value validity. Owner: BudgetForcing. Endpoints: attempted terminal execution result → per-invoke refusal count → ModifyExecResult Continue → observation and next model turn. SRC-1, `src/jaz/hooks/builtin/budget_forcing.py`, implementation. Host selects refusal count/text; software decides; model chooses any subsequent revision. No answer oracle. Operating mode: open task with forced continuation, not evidence-based candidate selection.

- Immediate return: Continue carrying BudgetForcingError and caller's refusal text, or no effect after count exhaustion.
- Later read-back: inapplicable — counter and feedback govern the current invoke; trace persistence belongs to a separate route.
- Delegated visibility: Propagating activation applies independently per child invoke; local hook applies locally.
- Selection predicate: Remaining count positive and result is Return or Raise; not an assessment of its content.
- Invalidation or expiry: Count decremented on refusal and cleared at InvokeExit, including abnormal exit.
- Activation or effect: Refusal changes termination to continuation and is logged as finalized refusal, not clean success.
- Evidence limits: No observed quality improvement; extra computation is not warrant. No established rollback of code/tool effects.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if isinstance(result, (Return, Raise)):
>     self._refusals_remaining[event.invoke_id] = remaining - 1
>     return [_refuse(self.refusal_text)]
> --- `src/jaz/hooks/builtin/budget_forcing.py`

#### EPI-RTE-rollout-export
Label: Rollout accumulation and export

No counterpart after comparison with [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay): this route consumes token records and exports samples, not saved text for live execution. Owner: RolloutRecorder/Rollout. Endpoints: token-bearing LLMQueryExit results → per-invoke log → frozen Rollout at exit → caller-selected flat, piecewise or per-turn export. SRC-1, `src/jaz/hooks/builtin/rollout.py`, implementation. Host selects hook/export; software checks record presence and monotonicity. Domain is token representation. No reward oracle or task judgment; the docstring places reward with the external driver.

- Immediate return: Hook produces no effects; caller accesses rollouts and export values, or receives NonMonotoneRolloutError from to_flat.
- Later read-back: uninspected — caller can serialize/use exported dictionaries, but no shipped trainer execution or later training consumer was traced.
- Delegated visibility: With activation, logs demultiplex by invoke_id, including nested invokes; no merge into one inferred successful trajectory.
- Selection predicate: Only completed query outcomes with tokens contribute. A completed tokenless query stands down the invoke and drops partial log. _extends compares message_id prefix and length for flat eligibility.
- Invalidation or expiry: Activation resets prior scope; invoke exit removes mutable bookkeeping. Nonmonotonicity rejects only flat export; piecewise/per-turn alternatives remain.
- Activation or effect: Retention and structural export wired; finished metadata can mark abnormal partial work. No weight update or learned capacity follows from producing samples.
- Evidence limits: Stamp generation/backend truth not independently audited; exact weight_version may be absent. No target execution, reward evaluation, training or causal benefit supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._stood_down.add(event.invoke_id)
> self._log.pop(event.invoke_id, None)
> return []
> --- `src/jaz/hooks/builtin/rollout.py`

> for prev, cur in zip(self.turns, self.turns[1:], strict=False):
>     if not _extends(prev, cur):
>         raise NonMonotoneRolloutError(
> --- `src/jaz/hooks/builtin/rollout.py`

> return len(cur.sent) >= len(expected) and all(
>     a.message_id == b.message_id for a, b in zip(expected, cur.sent, strict=False)
> )
> --- `src/jaz/hooks/builtin/rollout.py`

#### EPI-RTE-swe-tools
Label: SWE file and shell tools

No counterpart after comparison with [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop): these registered, optionally granted tool implementations are external-effect endpoints that the general loop can call, not its executor. Owner: host grants SWE_LIBRARY; model/user code selects call; functions act on host filesystem/subprocess. Source-native read returns file text, bash returns CompletedProcess, replace edits literal text. SRC-1, `src/jaz/_library/swe.py`, implementation.

- Immediate return: read returns file contents; bash returns stdout/stderr/return code in CompletedProcess; replace returns None or raises.
- Later read-back: Changed file persists and can be read in later invocations if accessible/granted; no automatic reload or actual later use is shown.
- Delegated visibility: Only when tool objects are passed/inherited; not an automatic grant to all children.
- Selection predicate: Caller-selected path/command; replace counts literal matches and refuses zero or multiple unless replace_all is true.
- Invalidation or expiry: File writes replace prior text immediately; no transactional rollback, source-truth expiry or semantic invalidation is implemented here.
- Activation or effect: File acquisition and host side effects are wired; arbitrary shell test effects depend on the supplied command.
- Evidence limits: OS/dependency behavior uninspected; occurrence count does not establish replacement correctness, factual truth or software success.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller/model proposes replacement, software can veto ambiguity; no per-write human approval inside the function. Guidance describes literal replacement; what persists is replacement bytes, not a justified claim or criticism record. Recovery requires another file edit or external tooling.

> with open(file_path) as f:
>     return f.read()
> --- `src/jaz/_library/swe.py`

> if count > 1 and not replace_all:
>     raise ValueError(
> --- `src/jaz/_library/swe.py`

> new_content = content.replace(to_replace, replace_with)
>
> with open(file_path, "w") as f:
>     f.write(new_content)
> --- `src/jaz/_library/swe.py`

### Claims

#### EPI-CLM-hook-contracts
Label: Validation and replay contracts

Distinct from [RT-CLM-repl-policy](runtime.md#rt-clm-repl-policy): these are hook-specific type/value/code/replay contracts, not REPL isolation. Claimed operation: enforce return type, validate return values/veto source before execution, and resume saved responses before live calls take over. SRC-1, `README.md`, doctrine/design. Actual check domains and consumers are split in the ledger; no source-truth guarantee is stated in these rows.

> | `ReturnType` | Declare + enforce the invoke's return type |
> | `ValidateReturn` / `ValidateREPLCode` | Validate the return value / veto REPL code before it runs |
> --- `README.md`

> | `TrajectoryReplay` | Resume a run from an ATIF trace: saved responses replay, then live calls take over |
> --- `README.md`

#### EPI-CLM-protocol-framing
Label: Raw code framing robustness

No counterpart after comparison with [RT-CLM-repl-policy](runtime.md#rt-clm-repl-policy): this concerns codec integrity and attributed experimental reports, not execution policy. Claimed operation: removing delimiters prevents content/delimiter ambiguity specifically; source reports fewer non-runnable turns on a clustered SWE-bench comparison but not improved task scores or elimination of over-escaping. SRC-1, `src/jaz/protocol/code_only.py`, doctrine/design and reported operation. Underlying logs are not supplied, so these numbers are attributed, not independently inspected experiments.

> **This fixes delimiter collision specifically, NOT over-escaping in general.**
> --- `src/jaz/protocol/code_only.py`

> # **Task scores did not favor it, and are not significant either way.** SWE-bench resolved 20.0%
> # [9.5%, 37.3%] for BOTH arms (Fisher p=1.0). StuLife 93.5% vs 92.3% and Recall 100% vs 100% are
> # single episodes: n=1, no interval, not estimates. This default rests on robustness, NOT on
> # performance.
> --- `src/jaz/protocol/code_only.py`

#### EPI-CLM-token-rollouts
Label: Training grade rollout facts

No counterpart after comparison with [RT-CLM-repl-policy](runtime.md#rt-clm-repl-policy): token provenance/export claim. Claimed operation: accumulate exact token IDs, loss mask and log probabilities as training-grade rollouts; design assigns reward to driver and calls the recorder an accumulator rather than verifier. SRC-1, `src/jaz/hooks/builtin/rollout.py`, doctrine/design. Inspected export checks bound representation, while complete backend stamp fidelity remains uninspected.

> """Record agent runs as training-grade rollouts: exact token ids, loss mask, logprobs.
> --- `src/jaz/hooks/builtin/rollout.py`

> # * The recorder is an ACCUMULATOR, NOT A VERIFIER — and export does not verify either.
> --- `src/jaz/hooks/builtin/rollout.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
