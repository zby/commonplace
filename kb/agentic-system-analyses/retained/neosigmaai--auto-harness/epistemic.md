---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "auto-harness epistemic routes: benchmark evidence, candidate selection, retained diagnoses and the limits of improvement claims."
run-id: AAS-2026-10-15-auto-harness-92303e444cb2-01
reviewed-boundary: "52360dbbeb8cea8886d90778e634a145c51da735"
---

# auto-harness epistemic report

## Source-and-claim boundary

The question is how benchmark interactions become evidence, candidate changes and later authority. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identities: see its [Source register](boundary.md#source-register). This is the shipped improvement plane, including local candidate templates and BIRD wrappers, not the external coding-agent scheduler or external verifiers. All source anchors below refer to SRC-1. Python supplies implementation evidence; programs and README supply doctrine/design or attributed reported operation. No observed run or causal experiment was supplied.

Missing task data and gold answers prevent oracle-validity conclusions. Missing generated traces, learnings, candidate revisions and histories prevent individuation of actual diagnoses, accepted explanations, retained criticisms and achieved improvement. Missing external callbacks, benchmark implementations and provider internals prevent claims about their enforcement, semantic checks or parameter changes. Available local source was not treated as an access gap.

| Entry point or operation | Source path | Coverage and evidence basis |
|---|---|---|
| Preparation, baseline, splits and provisioning | `prepare.py`; `agent/helpers/bird_interact/setup.py` | Supplied [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline); no target execution |
| Benchmark CLI, alternate split and explicit IDs | `benchmark.py` | Direct read of dispatch, scoring and final persistence; supplied task-route records below |
| Terminal registered bash, output filtering, completion and trace | `agent/templates/terminal_bench.py` | Direct complete read; [EPI-RTE-output-filter](#epi-rte-output-filter), [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task) |
| Tau model/tool messages and reward import | `agent/templates/tau_bench.py`; `benchmark.py` | Supplied [RT-RTE-tau-task](runtime.md#rt-rte-tau-task); symbol/dispatch search corroborates tool delegation |
| BIRD HTTP init/run/health and direct service launch | `agent/helpers/bird_interact/bird_service.py` | Direct complete read; [RT-RTE-bird-session](runtime.md#rt-rte-bird-session); health checks availability, not answer correctness |
| BIRD modes, tools and hooks | `agent/templates/bird_interact.py`; `agent/helpers/bird_interact/bird_adk_runtime.py` | Direct builder read and runtime symbol search; supplied [RT-RTE-bird-session](runtime.md#rt-rte-bird-session); callback internals external |
| Gate comparison, intermediate saves and promotion | `gating.py` | Direct read of loaders and entire `run_gate`; [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) |
| Recorder CLI and last-commit guard | `record.py` | Direct complete read; [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record) |
| Failure analysis, rollback, learnings and stopping | `program_templates/base.md` | Direct complete read; supplements supplied through [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision) |
| Warrant and benefit claims | `README.md`; `program_templates/base.md` | Direct targeted README reads/search; [EPI-CLM-gate-everything](#epi-clm-gate-everything), [EPI-CLM-eval-curation](#epi-clm-eval-curation), [EPI-CLM-structural-cheating](#epi-clm-structural-cheating), [EPI-CLM-score-improvement](#epi-clm-score-improvement), [RT-CLM-timeout-failure](runtime.md#rt-clm-timeout-failure) |

The tracked-file inventory and entry-point search found no additional local CLI, HTTP operation or registered tool family requiring a new runtime route. This is not an enumeration of external framework operations. Cleanup, rejection, reset and withdrawal are covered through the supplied task, preparation, gate and revision routes; only candidate rollback is requested, not executed by the gate. No supersession of the supplied runtime findings is needed. The correction retains the valid task-content container and declares its imported-input, tool-observation, generated-assertion and operational-action parts. Coverage descriptions above are carried from the supplied previous report; this correction directly reread the complete Terminal template to verify those distinctions. Non-default Harbor dataset comparability remains unestablished: preparation omits the configured dataset in baseline constructors whereas the gate forwards it (SRC-1 `prepare.py`, `gating.py`; supplied refusal's checked passages). The stock workflow and conditional arithmetic do not establish a same-population baseline or split for custom datasets, nor the broader “all work as-is” implication.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-task-content](#epi-obj-task-content) | Container only; independently assessed parts below | see record | SRC-1 `agent/templates/terminal_bench.py` | No uniform warrant or authority assigned to the container |
| [EPI-OBJ-task-input](#epi-obj-task-input) | Imported task/user assertions, where present | see record | SRC-1 `agent/templates/terminal_bench.py` | Requirements and requests are not automatically truth-apt; source warrant unknown |
| [EPI-OBJ-tool-output](#epi-obj-tool-output) | Imported reported observations and diagnostic assertions | see record | SRC-1 `agent/templates/terminal_bench.py` | Unknown external warrant; filtering may omit qualifications |
| [EPI-OBJ-assistant-content](#epi-obj-assistant-content) | Generated answer and completion assertions, where present | see record | SRC-1 `agent/templates/terminal_bench.py` | Entailment indeterminate without concrete answers; no local truth acceptance |
| [EPI-OBJ-task-actions](#epi-obj-task-actions) | None required: operational commands, tool arguments and SQL submissions | see record | SRC-1 `agent/templates/terminal_bench.py` | Execution authority is not assertion warrant; SQL correctness is separately externally evaluated |
| [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | Reported task rewards, means and pass outcomes | see record | SRC-1 `benchmark.py`, `gating.py`, `record.py` | External evaluator correctness and provenance unresolved |
| [EPI-OBJ-learnings](#epi-obj-learnings) | Requested failure explanations and claims about what worked | see record | SRC-1 `program_templates/base.md` | No concrete learned instance supplied |
| [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) | None required: executable behavior; embedded statements assessed separately | see record | SRC-1 `prepare.py` | Program effectiveness is a testable claim, not established by executable form |
| [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) | Mostly non-truth-apt prescriptions | see record | SRC-1 `agent/templates/terminal_bench.py` | Requesting verification does not verify a result |
| [RT-OBJ-program](runtime.md#rt-obj-program) | Method guidance plus warrant claims | see record | SRC-1 `program_templates/base.md` | Delivered procedure is not demonstrated compliance |
| [RT-CMP-candidate-model](runtime.md#rt-cmp-candidate-model), [RT-CMP-user-model](runtime.md#rt-cmp-user-model), [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model) | Particular encoded propositions not determinable | see individual records | SRC-1 `benchmark.py`; `program_templates/base.md` | Distributed-parametric state is opaque; separate pinning and mutability limits remain as recorded |

## Authority-route ledger

Fields owned by a declaring record are referenced with `see`; distinctions below are this report's epistemic assessment. A shared route may perform several functions, so repeated citations do not create new identities.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline) | operational admission/selection/consumption | implemented | [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) | non-truth-apt policy/content update: template installation and split selection | see route | see route | see route | see route | see route | No generalization warrant from a baseline-selected split | see route | see route | SRC-1 `prepare.py` | none | none | Timeout exclusion selects the measured population; baseline reuse is not revalidation |
| [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session) | content transformation | implemented | [EPI-OBJ-task-input](#epi-obj-task-input), [EPI-OBJ-tool-output](#epi-obj-tool-output) | truth-apt transformation: acquisition/import | Imported task/user assertions and reported tool observations entering candidate context; distinct parts, common unknown source warrant | Local adapters; external source warrant unknown | see routes | see routes | see routes | Delivery of reported observations, not independent endorsement | see routes | see routes | SRC-1 `benchmark.py`; `agent/templates/terminal_bench.py` | none | none | A simulator statement is not automatically ground truth; BIRD SQL and tau answers have opaque external semantics |
| [EPI-RTE-output-filter](#epi-rte-output-filter) | content transformation | implemented | [EPI-OBJ-tool-output](#epi-obj-tool-output) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | Preserves selected characters, not completeness of source evidence | see route | see route | SRC-1 `agent/templates/terminal_bench.py` | none | none | Source warrant can degrade through omitted qualifications |
| [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session) | content transformation | implemented | [EPI-OBJ-assistant-content](#epi-obj-assistant-content) | truth-apt transformation: indeterminate | Candidate answer and completion assertions, excluding executable tool arguments and SQL submissions | Models; actual content unavailable | see routes | see routes | see routes | Generation only; entailment versus conjecture cannot be settled for absent answers | see routes | see routes | SRC-1 `agent/templates/terminal_bench.py`; `agent/templates/bird_interact.py` | none | none | Text-only Terminal completion is self-declared, not evaluator acceptance |
| [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session) | check/evidence production | implemented | [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | truth-apt transformation: acquisition/import | Task behavior against external benchmark criteria | see routes; external verifier domain uninspected | see routes | see routes | see routes | Imported reward with unknown source warrant beyond local extraction | see routes | see routes | SRC-1 `benchmark.py` | [RT-CLM-timeout-failure](runtime.md#rt-clm-timeout-failure) | Returned mapping is not necessarily full requested population | No independent answer oracle verification |
| [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | check/evidence production | implemented | [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | truth-apt transformation: entailed derivation | Returned numeric outcomes versus configured thresholds and prior best | Deterministic arithmetic over loaded values, not semantic task correctness | see route | see route | see route | Conditional numerical conclusions only; premises are reported scores | see route | see route | SRC-1 `gating.py`; `benchmark.py` | [EPI-CLM-gate-everything](#epi-clm-gate-everything) | none | No warranted-source premise or statistical improvement proof |
| [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | disposition/acceptance | implemented | [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) | no content change | Candidate's eligibility for prescribed commit | see route | see route | see route | see route | Acceptance for configured benchmark protocol only, not acceptance of a causal explanation | see route | see route | SRC-1 `gating.py` | [EPI-CLM-gate-everything](#epi-clm-gate-everything) | Script success does not mediate every commit | Empty/partial mappings and editable history limit license |
| [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | retention | implemented | [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | truth-apt transformation: non-ampliative reshaping | Suite last-results save | see route | see route | see route | see route | Retention of measurements, including before final gate acceptance | see route | see route | SRC-1 `gating.py` | none | none | Saving observations is not lifecycle integration of an accepted explanation |
| [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | behavior/policy adaptation | implemented | [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | non-truth-apt policy/content update: suite membership | Passing rerun IDs become future regression tasks after gate success | see route | see route | see route | see route | A task passed a rerun under the imported reward; no explanation accepted | see route | see route | SRC-1 `gating.py` | [EPI-CLM-eval-curation](#epi-clm-eval-curation) | Deterministic promotion, not coding-model membership judgment | Loader ignores split metadata; no demotion transaction |
| [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record) | retention | implemented | [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | truth-apt transformation: acquisition/import | Caller numerical claims enter TSV | see route | see route | see route | see route | Caller report, not authenticated accepted measurement | see route | see route | SRC-1 `record.py` | [EPI-CLM-gate-everything](#epi-clm-gate-everything) | No gate certificate consumed | Commit label does not authenticate evaluated bytes |
| [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | operational admission/selection/consumption | implemented | [EPI-OBJ-evaluation-state](#epi-obj-evaluation-state) | no content change | History maximum and prior failures consumed for comparison/reruns | see route | see route | see route | see route | Numerical reliance granted without provenance authentication | see route | see [RT-BAP-history-gate](runtime.md#rt-bap-history-gate) | SRC-1 `gating.py` | none | none | Strong operational force can coexist with weak epistemic license |
| [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision) | content transformation | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | truth-apt transformation: indeterminate | Failure explanation and what-worked claims | External coding agent; see route | see route | see route | see route | Requested diagnosis only; actual propositions unavailable | see route | see [RT-BAP-program-coder](runtime.md#rt-bap-program-coder) | SRC-1 `program_templates/base.md` | none | none | A proposed explanation would normally go beyond scores, but no concrete non-entailment witness supplied |
| [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision) | retention | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | no content change | Requested append after success or failure | see route | see route | see route | see route | No evidence-consuming acceptance criterion for explanatory truth | see route | see route | SRC-1 `program_templates/base.md` | none | none | Log can contain hypotheses, requests and failures, not only accepted claims |
| [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision) | behavior/policy adaptation | doctrine only | [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) | non-truth-apt policy/content update: model-directed Python/prompt revision and requested revert | see route | see route | see route | see route | see route | Benchmark eligibility, not truth of proposed mechanism | see route | see [RT-BAP-candidate-runtime](runtime.md#rt-bap-candidate-runtime) | SRC-1 `program_templates/base.md` | [EPI-CLM-score-improvement](#epi-clm-score-improvement) | Revision requested, not observed | Import path implemented; evidence-responsive optimizer conduct not locally implemented |
| [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session), [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision) | lineage/freshness/recovery | implemented | [EPI-OBJ-task-content](#epi-obj-task-content) | no content change | Trace filtering/copying, stale cleanup and reset; requested revert is doctrine only | see routes | see routes | see routes | see routes | No independent endorsement from freshness or selective visibility | see routes | see routes | SRC-1 `benchmark.py`; `agent/templates/terminal_bench.py` | [EPI-CLM-structural-cheating](#epi-clm-structural-cheating) | Selective copying is not access confinement | Reset/cleanup do not retract previously recorded history or learnings |
| [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session) | operational admission/selection/consumption | implemented | [EPI-OBJ-task-actions](#epi-obj-task-actions) | non-truth-apt policy/content update: generated commands and tool/SQL arguments | Dispatch of actions rather than acceptance of assertions | Terminal name and JSON checks; external tau/BIRD tool and callback conditions remain uninspected | see routes | Tool execution or local dispatch error; see routes | Terminal directly calls environment executor; external frameworks dispatch other tools | No truth warrant follows from executable syntax or submission | Task tools can change environment or submit SQL; no local per-call human approval | Terminal Python to environment via command string, enforcing dispatch for this task; tau/BIRD via external tools, force limited to inspected registration | SRC-1 `agent/templates/terminal_bench.py`; see task records | none | Execution is not epistemic acceptance | Tool effects and external submission checks unobserved |

No lifecycle-integration route for accepted ampliative explanatory claims was established in the inspected local program, gate and recorder. Suite growth is implemented evaluation-policy adaptation, not evidence that a causal theory was accepted and integrated. This distinction does not deny the operational value of a regression suite.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-gate-everything](#epi-clm-gate-everything) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission), [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record) | None supplied | No commit interceptor or authenticated gate-to-record transaction | Prescribed sequencing plus conditional checks | Universal commitment guarantee unsupported |
| [EPI-CLM-eval-curation](#epi-clm-eval-curation) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | None supplied | Membership selection is fixed by returned rewards and stored failures | Automatic suite growth exists | Coding agent influences performance, but is not the direct implemented membership decider |
| [EPI-CLM-structural-cheating](#epi-clm-structural-cheating) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session) | None supplied | No access-control experiment; candidate can be edited; external logs opaque | Stock trace controls reduce designated diagnosis exposure | Cannot infer only train evidence is accessible |
| [EPI-CLM-score-improvement](#epi-clm-score-improvement) | see record | SRC-1 `README.md`, reported operation | see record | [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | No inspectable supporting run | No matched comparison, repeated-trial uncertainty or component intervention supplied | Attributed score report, architecturally plausible loop | Neither reproduced gain nor causal explanation established |
| [RT-CLM-timeout-failure](runtime.md#rt-clm-timeout-failure) | see record | SRC-1 `program_templates/base.md`, doctrine/design | see record | [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline), [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) | None supplied | See claim and runtime forcing cases | `None` entries count zero in returned mapping | Does not restore all absent tasks or baseline-excluded timeouts |

## Bounded conclusion

The implemented plane imports externally evaluated rewards, derives conditional arithmetic results, and grants those results operational authority over gate return and future suite membership. The intended use and acceptance criterion are explicit: configured suite pass rate and nondecreasing test mean permit the prescribed commit. This acceptance is bounded to benchmark protocol eligibility. It is neither a correctness proof nor acceptance of a failure explanation. The history-to-gate channel is enforcing within an invoked gate, while gate-to-coding-agent commit/revert is procedural; see [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission), [RT-BAP-history-gate](runtime.md#rt-bap-history-gate) and [RT-BAP-program-coder](runtime.md#rt-bap-program-coder).

Imported task/user assertions and tool observations are acquired with source warrant unknown; Terminal filtering can degrade the tool-observation part by omitting decisive middle text. Generated assistant assertions have indeterminate entailment, whereas generated commands, tool arguments and submitted SQL have operational authority through dispatch, not truth warrant. These are separately declared parts of the task interaction container; see [EPI-OBJ-task-input](#epi-obj-task-input), [EPI-OBJ-tool-output](#epi-obj-tool-output), [EPI-OBJ-assistant-content](#epi-obj-assistant-content) and [EPI-OBJ-task-actions](#epi-obj-task-actions). Numeric derivations are entailed by supplied numeric premises and inspected arithmetic, not by independently warranted benchmark facts. For example, `val_score` maps `{a: 1.0, b: None}` to `0.5`, whereas `{a: 1.0}` yields `1.0`: missing entries and explicit failures differ. This is an implementation deduction, not a target run (SRC-1 `benchmark.py`; [RT-CLM-timeout-failure](runtime.md#rt-clm-timeout-failure)).

Candidate generation, failure diagnosis and append-only learnings are requested. Actual answer semantics, conjectures and explanations cannot be individuated from templates alone. No observed evidence-consuming acceptance or lifecycle integration of an ampliative explanatory claim was supplied. Retention of caller scores and requested hypotheses must not be promoted to such acceptance; see [EPI-OBJ-learnings](#epi-obj-learnings) and [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record).

Direct adaptation does not require a truth-apt learning product: suite membership changes future checks, and editable executable code can change later candidate behavior. Reflection is afforded through trace-to-revision feedback; learning remains uninspected without future-capacity evidence; autonomous theory criticism remains claimed rather than observed. Theory-builder conditions, addressability, persistence and self-improvement limits remain independently as assessed in [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision). In particular, the standing candidate-to-import path does not establish exercised link 4 or successful improvement. Opaque distributed-parametric models support no additional weight-learning or theory-content conclusion beyond [RT-CMP-candidate-model](runtime.md#rt-cmp-candidate-model), [RT-CMP-user-model](runtime.md#rt-cmp-user-model) and [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model). There is no single system-wide epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-task-content
Label: Task interaction content

Source-native identity: task instruction, tool messages and assistant content in Terminal `messages`; tau `HarnessState` messages; BIRD session messages/SQL. Form: natural-language descriptions/results, with symbolic command, SQL and tool-call parts. Substrate: current process/session context and optional trace files. These are distinct from the code and instructions in [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) and [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions); no supplied object denotes their task-generated content. Parts differ: imported task/tool assertions have unknown source warrant; generated final assertions have indeterminate entailment; command/tool syntax has operational rather than intrinsically truth-apt authority. Supplied task routes retain these separate consumers and external-evaluator limits. Evidence: SRC-1 `agent/templates/terminal_bench.py`; [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session).

> messages.append({
>                     "role": "tool",
>                     "tool_call_id": tc.id,
>                     "content": output,
>                 })
> --- `agent/templates/terminal_bench.py`

#### EPI-OBJ-task-input
Label: Imported task and user content
Part of: [EPI-OBJ-task-content](#epi-obj-task-content)

Source-native identity: Terminal user task instruction, tau incoming user/history content, and BIRD turn user content. Form: natural-language task descriptions, requests and any assertions; substrate: current task/session messages and optional traces. Role: supply the problem and reported user facts to the candidate model. Assertions enter with source warrant unknown; prescriptions have no truth value merely by being instructions. No concrete task instance or independent validation is supplied. Distinct from static [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions): this is invocation input, not candidate policy. SRC-1 `agent/templates/terminal_bench.py`; [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session).

> {"role": "user", "content": f"Task:\n{instruction}"},
> --- `agent/templates/terminal_bench.py`

#### EPI-OBJ-tool-output
Label: Imported tool observations
Part of: [EPI-OBJ-task-content](#epi-obj-task-content)

Source-native identity: Terminal environment stdout/stderr/return-code reports and local dispatch diagnostics inserted as tool messages; corresponding tau tool results and BIRD function responses remain bounded by their supplied route accounts. Form: natural-language or symbolic reported observations; substrate: task/session messages and optional traces. Producer: environment/tool or adapter diagnostics, not assistant answer generation. Consumer: next candidate-model call, with Terminal filtered content also reaching optional diagnosis traces. Assertions are acquired with external source warrant unknown; Terminal selection can degrade completeness. No claim that arbitrary output strings are all truth-apt. SRC-1 `agent/templates/terminal_bench.py`; the container's retained insertion passage and [EPI-RTE-output-filter](#epi-rte-output-filter); [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session). Unlike the imported task part, this part is produced in response to tool execution and is subject to the inspected output filter.

#### EPI-OBJ-assistant-content
Label: Generated assistant assertions
Part of: [EPI-OBJ-task-content](#epi-obj-task-content)

Source-native identity: Terminal `message.content`, tau returned assistant text and BIRD final/fallback text. Form: natural-language answer, explanation or completion assertions where present; substrate: current message/session state and optional trace. Candidate models produce this content; later model turns or the task caller consume it. No concrete answer is supplied: entailment versus ampliative conjecture is indeterminate, not established by model generation alone. Terminal text without tool calls terminates the loop without semantic acceptance. This excludes the separately declared executable action part. Distinct from [EPI-OBJ-learnings](#epi-obj-learnings): the task candidate produces this content, not the outer diagnosing coding agent. SRC-1 `agent/templates/terminal_bench.py`; [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session).

> assistant_msg = {"role": "assistant", "content": message.content}
> --- `agent/templates/terminal_bench.py`

#### EPI-OBJ-task-actions
Label: Generated task actions
Part of: [EPI-OBJ-task-content](#epi-obj-task-content)

Source-native identity: Terminal `message.tool_calls` and bash `command`, tau assistant tool calls, and BIRD SQL/tool arguments. Form: symbolic executable commands, structured tool calls and SQL; substrate: message objects/session events and optional traces. Producer: candidate model; consumers: Terminal Python/environment executor, external tau tool machinery and BIRD ADK tools/callbacks. This content is operational rather than intrinsically truth-apt: execution or SQL submission is not acceptance of an answer proposition. SQL correctness is assessed through externally produced rewards, not by the local string's existence. Distinct from [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code): these are per-task generated actions, not the Python implementation producing/dispatching them. SRC-1 `agent/templates/terminal_bench.py`; [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session).

> command = args.get("command", "")
> --- `agent/templates/terminal_bench.py`

> result = await environment.exec(command, timeout_sec=120)
> --- `agent/templates/terminal_bench.py`

#### EPI-OBJ-evaluation-state
Label: Evaluation state

Source-native identity: runner result mappings, `workspace/train_results.json`, suite `last_results` and task IDs, TSV score rows. Form: symbolic JSON/TSV numeric measurements and policy membership; substrate: memory and local workspace files. This object spans the evaluation data consumed/changed by [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) and [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record), rather than duplicating either route or any supplied operative object. The ledger separates imported measurements, derived comparisons, caller-authored rows and non-truth-apt membership because they have different warrant and consumers. SRC-1 `benchmark.py`, `gating.py`, `record.py`; supplied routes carry minimum passages for promotion and append.

> return sum(0.0 if v is None else v for v in results.values()) / len(results)
> --- `benchmark.py`

> return data.get("results", {})
> --- `gating.py`

#### EPI-OBJ-learnings
Label: Learnings log

Source-native identity: `workspace/learnings.md`. Form: requested natural-language hypotheses, outcome descriptions, patterns and human requests; substrate: local Markdown initialized during preparation and prescribed append log. Distinct from [RT-OBJ-program](runtime.md#rt-obj-program), which requests its creation, and from [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), which encompasses the requested update. No concrete log instance was supplied. The supposed memory role licenses requested later use, not demonstrated reading, accepted truth or causal improvement. SRC-1 `program_templates/base.md`.

> After every iteration — gate passed or failed — append to `workspace/learnings.md`:
> --- `program_templates/base.md`

> - **Patterns confirmed** — failure modes that appear repeatedly
> - **What worked** — prompt changes that improved the score
> --- `program_templates/base.md`

### Routes

#### EPI-RTE-output-filter
Label: Terminal output filter
Part of: [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task)

Endpoints/progression: environment stdout/stderr/exit status → joined string → `_truncate` → tool message → next model call and optional saved trace. Owner: deterministic candidate Python. It reshapes source text without generating a new substantive proposition; first/last selection can remove evidence or qualifications. Target domain: strings, not correctness of their assertions. Concrete source-only deduction: with default limit, input consisting of 4000 `A` characters, then `X`, then 4000 `B` characters returns the two 4000-character ends separated by the marker saying one character was truncated. `X` is absent from both later message and saved conversation. This does not execute the target. No acceptance or rejection of a truth claim occurs. The filter has fixed force over model input; it is not model-directed summarization.

- Immediate return: at most the selected ends plus truncation marker, or unchanged short string.
- Later read-back: optional saved `trace.json` contains the already filtered tool messages for outer diagnosis; no automatic full-output pointer is emitted.
- Delegated visibility: next candidate-model call receives the filtered content, not the omitted middle.
- Selection predicate: nonempty text longer than `MAX_OUTPUT_CHARS=8000`; first and last `limit // 2` characters retained.
- Invalidation or expiry: current context ends with task; trace retention follows the containing task route; rereading environment files is possible via bash, not automatic recovery.
- Activation or effect: wired string transformation and context insertion; effect on model decisions unobserved.
- Evidence limits: no actual long output or task run supplied; selection preserves literal endpoints, not semantic completeness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1 `agent/templates/terminal_bench.py`.

> if not text or len(text) <= limit:
>         return text or ""
>     half = limit // 2
>     return (
>         text[:half]
>         + f"\n\n... [{len(text) - limit} chars truncated] ...\n\n"
>         + text[-half:]
>     )
> --- `agent/templates/terminal_bench.py`

> output = _truncate(output)
> --- `agent/templates/terminal_bench.py`

### Claims

#### EPI-CLM-gate-everything
Label: Gate everything

Claimed operation: no change committed without passing both gates. Source: SRC-1 `README.md`, doctrine/design. Distinct from the narrower [RT-CLM-timeout-failure](runtime.md#rt-clm-timeout-failure). The program requests this sequence, but inspected gate/recorder do not intercept commits or authenticate score provenance; see [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record).

> - **Gate everything.** No change is committed without passing both the eval suite and the full test score gate.
> --- `README.md`

#### EPI-CLM-eval-curation
Label: Self-maintained evals

Claimed operation: coding agent decides suite membership without manual curation. Source: SRC-1 `README.md`, doctrine/design. No counterpart among supplied claims. [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) instead implements deterministic reward-driven promotion; the coding agent can affect membership indirectly by modifying candidate behavior.

> - **Self-maintained evals.** The coding agent decides which tasks belong in the regression suite — no manual curation needed.
> --- `README.md`

#### EPI-CLM-structural-cheating
Label: Structural anti-cheating

Claimed operation: no test traces saved and only train traces readable. Source: SRC-1 `README.md`, doctrine/design. Distinct from timeout claim; no supplied claim counterpart. [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task) and [RT-RTE-bird-session](runtime.md#rt-rte-bird-session) support designated local trace suppression/copy controls, not filesystem confinement or control of all external logs.

> - **Structural anti-cheating.** Test traces are not saved to disk. The coding agent can only read train traces.
> --- `README.md`

#### EPI-CLM-score-improvement
Label: Tau3 score improvement

Claimed operation: score improves from 0.56 to 0.78 while mining failures and maintaining evals. Source: SRC-1 `README.md`, reported operation, not supplied observed-run evidence. No counterpart among supplied claims. The source supplies a narrative endpoint comparison, not the run, evaluated candidate identities, uncertainty or an independently varied component. Accessible implementation establishes a possible improvement loop, not attribution to mining, prompts, tools or suite maintenance.

> This repo is a simplified version of our auto-harness agent setup. We demonstrate our system on Tau3 benchmark tasks where the agent's score improves from 0.56 to 0.78 (~40% jump) while mining failures and auto maintaining live evals. If you are curious to learn more, read the full blog here - https://www.neosigma.ai/blog/self-improving-agentic-systems.
> --- `README.md`
