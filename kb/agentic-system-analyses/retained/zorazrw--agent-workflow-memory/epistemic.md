---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Agent Workflow Memory's trajectory checks, workflow warrant and later behavioral authority at the frozen revision."
run-id: AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01
reviewed-boundary: "8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1"
---

# Agent Workflow Memory epistemic report

## Source-and-claim boundary

The question is whether AWM checks and accepts reusable web-task knowledge, rather than merely retaining and supplying workflow candidates. Scope and external exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). All findings below use SRC-1 at the frozen commit. Direct inspection adds evaluator prompt dispatch, result conversion, post-selection trajectory cleanup, workflow filtering and retrieval ablation to the provisional runtime account. No target execution or provider calls were made.

Two consequential source claims are [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) and [EPI-CLM-benchmark-benefit](#epi-clm-benchmark-benefit). Operational integration in the first claim must not be mistaken for integration after an evidence-consuming acceptance of the generated workflow's truth or transfer safety.

| Entry point or operation | Source path (SRC-1) | Coverage basis and records | Limit and conclusion prevented |
|---|---|---|---|
| Both pipeline drivers and WebArena run CLI | `mind2web/pipeline.py`, `webarena/pipeline.py`, `webarena/run.py` | Supplied [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), [RT-RTE-browser-action](runtime.md#rt-rte-browser-action) | Child failure handling and default handoff defects limit end-to-end confidence; no observed operation. |
| Mind2Web offline and online induction | `mind2web/offline_induction.py`, `mind2web/online_induction.py`, `mind2web/utils/data.py` | Direct source reads; [EPI-RTE-workflow-filter](#epi-rte-workflow-filter); supplied [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission) | Online task/trace identity join and success gate are not established by this wiring. |
| Mind2Web prediction, annotation scoring, results | `mind2web/memory.py`, `mind2web/run_mind2web.py`, `mind2web/results/calc_score.py` | Direct complete memory read; supplied driver/aggregation account; [EPI-RTE-annotation-score](#epi-rte-annotation-score) | External dataset and ranking scores unavailable; cannot reproduce metrics or infer live navigation success. Aggregator details not independently audited. |
| Optional workflow retrieval and concrete-example ablation CLI | `mind2web/workflow/retrieve.py` | Direct complete read; [EPI-RTE-retrieval-selection](#epi-rte-retrieval-selection), supplied [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) | Semantic workflow path returns metadata instead of queryable index. Ablation builds the index directly; the defect is not universal to embedding use. No retrieval accuracy test. |
| WebArena evaluator text/vision dispatch and status parsing | `webarena/autoeval/evaluator.py`, `webarena/autoeval/prompts.py`, `webarena/autoeval/evaluate_trajectory.py` | Direct complete reads; [EPI-RTE-trajectory-check](#epi-rte-trajectory-check), [EPI-RTE-success-selection](#epi-rte-success-selection) | Text receives the last logged thought, not an independently verified final DOM; vision receives the last screenshot and retained actions, which can include the answer in `send_msg_to_user(...)`. Vision omits a dedicated response field, not necessarily answer content. |
| WebArena neural induction and fixed reminders | `webarena/induce_prompt.py`, `webarena/prompt/instruction.txt` | Direct complete reads; [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup); supplied [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) | Outcome selection precedes lossy cleanup and generation; does not license a new workflow's general validity. |
| WebArena rule/manual alternative | `webarena/induce_rule.py` | Direct complete read; supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | Exact human `y` gives item-level admission, but no named correctness/transfer criterion or retained rationale. Auto bypasses it. |
| Legacy action parse/retry and workflow read hook | `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/dynamic_prompting.py` | Supplied [RT-RTE-browser-action](runtime.md#rt-rte-browser-action), [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | Not independently reread; conversion constrains syntax, not factual warrant or task success. Host execution is external. |
| Basic agent auxiliary entry | `webarena/agents/basic/agent.py` | Supplied [RT-RTE-basic-action](runtime.md#rt-rte-basic-action) | Raw response route has no workflow integration and no local truth check in the supplied account. |
| Retained examples, induction demonstrations, helper/provider internals | `webarena/workflow/shopping.txt`, `mind2web/data/memory/exemplars.json`, `mind2web/prompt/instruction_action.txt`, `webarena/prompt/one_shot.txt`, `webarena/autoeval/clients.py` | Direct complete shopping-file read; other materials supplied boundary/runtime coverage; [EPI-OBJ-workflow-text](#epi-obj-workflow-text), [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client) | Other static files and helpers not independently exhaustively inspected; no whole-corpus quality or system-complete negative. Provider internals inaccessible. |

No separate registered tool or hook registry is described by the supplied runtime; the shipped CLI alternatives and workflow read hook above are the assessed exposed operations. Available but unaudited helpers and static contents remain inspection limits, not absences. Missing observed trajectories, evaluator decisions and human review records prevent deciding whether particular persisted examples passed these routes. Missing causal comparisons prevent verifying benchmark benefit or workflow-specific contribution. External BrowserGym reward semantics prevent treating a truthy reward as a fully specified oracle for all web tasks.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | see record | see record | SRC-1, `webarena/workflow/shopping.txt` | see record |
| [EPI-OBJ-trajectory-input](#epi-obj-trajectory-input) | see record | see record | SRC-1, `webarena/induce_prompt.py` | see record |
| [EPI-OBJ-evaluation-result](#epi-obj-evaluation-result) | see record | see record | SRC-1, `webarena/autoeval/evaluate_trajectory.py` | see record |
| [EPI-OBJ-annotation-metrics](#epi-obj-annotation-metrics) | see record | see record | SRC-1, `mind2web/memory.py` | see record |
| [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) | not determinable in opaque weights; text candidates belong to the objects above | see records | SRC-1, `webarena/agents/legacy/utils/chat_api.py` | Exact revisions and provider-internal updates uninspected; inference calls do not establish parameter learning. |
| [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) | Dense similarity representations, not individually assessable assertions | see record | SRC-1, `mind2web/workflow/retrieve.py` | Similarity does not check workflow truth; source lineage of vectors is names/docstrings or exemplar specifiers. |

## Authority-route ledger

Each row describes one function. Fields owned by a shared record are `see` that record. Architectural status describes inspected implementation (including provisional supplied source findings), not activation. Relations below distinguish acquisition, filtering and generation; a single parent route can therefore occur in several rows.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-trajectory-check](#epi-rte-trajectory-check) | check/evidence production | implemented | [EPI-OBJ-evaluation-result](#epi-obj-evaluation-result) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `webarena/autoeval/evaluator.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | Final-state evidence differs between modes | see record |
| [EPI-RTE-success-selection](#epi-rte-success-selection) | disposition/acceptance | implemented | [EPI-OBJ-trajectory-input](#epi-obj-trajectory-input) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `webarena/induce_prompt.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | Trace selection is not workflow acceptance | see record |
| [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup) | content transformation | implemented | [EPI-OBJ-trajectory-input](#epi-obj-trajectory-input) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `webarena/induce_prompt.py` | none | Selection warrant does not certify transformed trace completeness | see record |
| [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) | content transformation | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | truth-apt transformation: indeterminate | Selected trajectories to reusable recipes | see record | see record | see record | see record | No generated-workflow truth license; generalization is requested, output semantics unobserved | see record | see [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | SRC-1, `webarena/prompt/instruction.txt` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | Finite traces do not entail cross-task invariant IDs | No generated output trace supplied |
| [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) | retention | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | no content change | see record | see record | see record | see record | see record | Retention before workflow acceptance | see record | see [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | SRC-1, `webarena/induce_prompt.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | none | see record |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | content transformation | implemented | [EPI-OBJ-trajectory-input](#epi-obj-trajectory-input) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Deduplication does not establish equivalence of task answers | see record | see [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | SRC-1, `webarena/induce_rule.py` | none | Abstract key drops fill values | see record |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | disposition/acceptance | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | no content change | see record | see record | see record | see record | see record | Manual operational admission; epistemic criterion unspecified. Auto admission is not human review | see record | see [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | SRC-1, `webarena/induce_rule.py` | none | No evidence-consuming claim acceptance established | see record |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | retention | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | no content change | see record | see record | see record | see record | see record | Trace provenance not retained as evaluator linkage in text | see record | see [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | SRC-1, `webarena/induce_rule.py` | none | none | see record |
| [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission) | content transformation | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Offline annotations are acquired premises, not independent warrant for novel workflows; online predictions are unfiltered candidates | see record | see [RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar) | SRC-1, `mind2web/online_induction.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | Online pairing weakens lineage | see record |
| [EPI-RTE-workflow-filter](#epi-rte-workflow-filter) | content transformation | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `mind2web/utils/data.py` | none | Literal substring exclusion is not semantic criticism | see record |
| [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission) | retention | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | no content change | see record | see record | see record | see record | see record | No workflow acceptance established by write | see record | see [RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar) | SRC-1, `mind2web/offline_induction.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | none | see record |
| [EPI-RTE-annotation-score](#epi-rte-annotation-score) | check/evidence production | implemented | [EPI-OBJ-annotation-metrics](#epi-obj-annotation-metrics) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `mind2web/memory.py` | [EPI-CLM-benchmark-benefit](#epi-clm-benchmark-benefit) | Offline replay not interactive navigation | see record |
| [EPI-RTE-retrieval-selection](#epi-rte-retrieval-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `mind2web/workflow/retrieve.py` | none | Semantic workflow branch defective, ablation distinct | see record |
| [RT-RTE-browser-action](runtime.md#rt-rte-browser-action) | operational admission/selection/consumption | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | no content change | see record | see record | see record | see record | see record | Action conversion licenses syntax only, no task/factual truth | see record | see [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system) | SRC-1, `webarena/agents/legacy/agent.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | none | see record |
| [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action) | operational admission/selection/consumption | implemented | [EPI-OBJ-workflow-text](#epi-obj-workflow-text) | no content change | see record | see record | see record | see record | see record | Delivery confers guidance, not factual endorsement | see record | see [RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar) | SRC-1, `mind2web/memory.py` | [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | Context fitting may omit workflows | see record |

No lifecycle integration after acceptance of generated workflow claims was found in the inspected induction writers and consumer hooks. They install candidates for operational use, without a generated-content check against a named intended-use criterion. This is a bounded source finding, not an absence claim about human activity outside the scripts or opaque provider reasoning. Whole-file replacement removes prior content from the next file read, but is not a recorded epistemic withdrawal or rollback decision; see the three supplied admission records. The manual rule alternative is a counterexample to fully automatic admission across AWM, not evidence of a universal epistemic acceptance protocol.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-workflow-induction](#epi-clm-workflow-induction) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-browser-action](runtime.md#rt-rte-browser-action), [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action) | None registered | No experiment isolating abstraction or memory; default handoff defects persist | Prompt-directed induction, retention and subsequent supply are implemented | Integration means operational context supply here; correct generalized knowledge and actual use remain unestablished |
| [EPI-CLM-benchmark-benefit](#epi-clm-benchmark-benefit) | see record | SRC-1, `README.md`; reported operation | see record | [EPI-RTE-annotation-score](#epi-rte-annotation-score), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) | None registered | Missing data/runs/comparison design prevent independent reproduction, transfer or component attribution | README reports outcomes; source defines some evaluation mechanisms | 35.6% and cross-domain generalization are attributed reports, not this run's findings |
| [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) | see record | SRC-1, `webarena/agents/legacy/dynamic_prompting.py`; implementation | see record | [RT-RTE-browser-action](runtime.md#rt-rte-browser-action), [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action) | None registered | Not a truth evaluator | see record | Limits delivery rather than warrant |

## Bounded conclusion

AWM has distinct checks with distinct targets. Mind2Web computes annotation agreement over supplied candidate actions and reference steps; this warrants a conditional statement about exact replay agreement, not successful live navigation. Its online writer does not consume those scores as a success gate. WebArena's model evaluator assesses apparent task completion from a selected evidence view, then software uses a Boolean result to select source trajectories. The external reward alternative supplies a reference outcome whose semantics are not frozen here. Neither assesses the subsequently generated recipe. Manual rule induction adds human per-item operational admission, unlike automatic neural and Mind2Web writes; its epistemic criterion remains unspecified. These conclusions follow [EPI-RTE-annotation-score](#epi-rte-annotation-score), [EPI-RTE-trajectory-check](#epi-rte-trajectory-check), [EPI-RTE-success-selection](#epi-rte-success-selection) and [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission).

Source warrant is bounded and can degrade along the route. Annotations are imported, online predictions are candidates with an order-based task association, and WebArena retained histories omit observations and evaluator linkage. Neural cleanup even removes scroll/noop evidence after successful-trace selection. The deterministic filters and deduplication are non-ampliative selection/reshaping, not tests of task success or recipe equivalence. The induced response's relation is indeterminate without a source-linked generated artifact: the instruction requests generalization, but instruction delivery does not establish semantic compliance. If it produces a claim that an element ID stays invariant across unseen tasks, that is ampliative relative to finite input traces. No checked inference from warranted premises to that general claim is established. See [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup), [EPI-RTE-workflow-filter](#epi-rte-workflow-filter), and [EPI-OBJ-workflow-text](#epi-obj-workflow-text).

Operational authority is nevertheless real at the implementation level. Whole-file writes can change the next agent's model context: WebArena appends workflows to a system message; Mind2Web supplies them as user-message exemplars subject to budget. These are guidance paths, not enforced subroutine execution or demonstrated dependence on content. Trace-conditioned replacement is an implemented behavior-shaping update pathway, but no supplied run establishes activation, improved future capacity or exercised self-improvement. The inspected writers do not persist content-directed criticisms of previous workflows or feed such criticisms into a next round; this does not settle opaque model cognition. Parameter updates are not implemented by the inspected inference clients; provider internals remain uninspected. Learning, reflection, autonomy and successful self-improvement cannot be bundled into one verdict from this fact. See the supplied admission records, [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system), [RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar) and model component records.

The retained shopping examples demonstrate that truth-apt local assertions exist alongside procedural instructions, but not their production or acceptance history. There is no system-wide epistemic score: source-trajectory selection, annotation scoring, literal cleanup, model abstraction and operational installation have different licenses and evidence limits. Benchmark benefit and generalization remain source-reported claims without registered observed or causal evidence.

## Shared records

### Operative objects

#### EPI-OBJ-workflow-text
Label: Workflow text

Source-native identity: workflow text files written by the three supplied admission routes and consumed by the two agent paths. Natural-language thoughts, task claims and recipes are interpreted by models; embedded action spellings here are demonstrations, not directly dispatched programs. Storage is local text files, including `webarena/workflow/shopping.txt`. Distinct from the supplied route containers; no operative-object counterpart is declared in runtime. Overlap is the retained output of [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), and [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission).

The candidate truth-apt content includes site-specific statements about where account/order links are and assertions about an order number, reviewers and dates. Imperatives are not true/false merely as commands; their implied applicability can be assessed over a named website/task scope. Localized natural-language assertions are available in the shipped shopping file, but no linked induction trace, evaluator decision or manual-review record is supplied. Thus this artifact is not evidence that any named route produced or accepted it. Newly generated generalizations remain unobserved. SRC-1, `webarena/workflow/shopping.txt`, `webarena/prompt/instruction.txt`.

> To get the order number of the most recent cancelled order, I need to look for the order with the status "Canceled" and note its order number. From the current page, I can see that the most recent cancelled order is order number 000000170.
> --- `webarena/workflow/shopping.txt`

> Keep the values of invariant elements, e.g., id of "Search" or "Customers", as they will share and stay invariant across tasks.
> --- `webarena/prompt/instruction.txt`

#### EPI-OBJ-trajectory-input
Label: Trajectory input

Source-native identity: query/think/action dictionaries formatted into induction prompts or concrete examples; natural-language thoughts plus text action spellings on local files and in request messages. Distinct object with multiple producers: selected WebArena logs, Mind2Web annotations and saved input/output conversations. Closest supplied records are [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission); no object counterpart is declared. Claims about observations in thoughts are truth-apt but not independent observations. WebArena induction omits screenshots/DOM, and online Mind2Web uses only the final input message and output, not all preceding context. The latter's unsorted directory zip does not establish task identity. SRC-1, `webarena/induce_prompt.py`, `mind2web/online_induction.py`.

> "env": "# " + item["input"][-1]["content"],
>             "action": item["output"],
> --- `mind2web/online_induction.py`

> for r, s in zip(result_list, samples):
>         examples.append({
>             "confirmed_task": s["confirmed_task"],
>             "action_reprs": [step["env"] + '\n' + step["action"] for step in r],
>         })
> --- `mind2web/online_induction.py`

#### EPI-OBJ-evaluation-result
Label: Evaluation result

Source-native identity: evaluator thoughts/status and stored `rm`, `gt`, `uid` JSON. Mixed natural-language rationale and symbolic Boolean/result identifiers on disk. Candidate proposition: this trajectory completed this task. Operational role: selection evidence, not workflow correctness certificate. Distinct from [EPI-OBJ-trajectory-input](#epi-obj-trajectory-input); closest supplied route is [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), with no runtime object counterpart. `gt` records an external reward, while `rm` comes from model output; saving them together does not compare them or validate the model. SRC-1, `webarena/autoeval/evaluate_trajectory.py`.

> "gt": traj_info["eval"],
>                 "rm": eval_result,
>                 "thoughts": out["thoughts"],
>                 "uid": traj_info["traj_name"],
> --- `webarena/autoeval/evaluate_trajectory.py`

#### EPI-OBJ-annotation-metrics
Label: Annotation metrics

Source-native identity: element accuracy, action F1, step success and task success appended to a saved conversation JSON. Symbolic numbers/Booleans on local disk, separate from natural-language predictions and exemplars. Candidate truth-apt content is agreement with imported annotations under code-defined criteria. Closest supplied record is [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action); no operative-object counterpart is declared. External reference truth and annotation fidelity are not independently verified. Online induction selects input/output dictionaries, not these metric entries. SRC-1, `mind2web/memory.py`, `mind2web/online_induction.py`; evidence for scoring is retained in [EPI-RTE-annotation-score](#epi-rte-annotation-score).

### Routes

#### EPI-RTE-trajectory-check
Label: Trajectory completion check
Part of: [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)

This is the evaluator subroute, not the parent's later generation or file admission. Endpoints: task intent plus filtered actions and last thought or screenshot → model evaluation → extracted thoughts/status → Boolean/result JSON. Owner: evaluator scripts. Text and vision are alternative evidence domains for apparent completion of information-seeking, navigation and modification tasks. The prompt criteria differ: information seeking requires an adequate response; navigation/modification consider actions and final state. Text passes the last logged thought as `cap` and inserts a dedicated response field. Vision chooses the final screenshot but its builder does not insert the response argument separately. However, evaluator cleanup preserves `send_msg_to_user(...)` actions, and vision formats every retained action into its prompt. An answer recorded in such an action can therefore reach the vision evaluator through action history, allowing the requested response-adequacy assessment from that input. The unused dedicated argument does not establish an absent response-check route or an inability to receive the final answer. Whether a particular history contains that answer, or the model checks it correctly, remains unobserved. No independent expected answer is supplied to the model, and no model judgment is treated as an oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Extracted thoughts/status and stored task-level Boolean result, not a workflow assessment.
- Later read-back: Matching model-named JSON is consumed by induction selection; rationale is not delivered in the generated workflow's file format.
- Delegated visibility: Both modes receive intent and all retained actions, including any preserved `send_msg_to_user(...)` answer content. Text additionally receives the last thought and dedicated response field; vision additionally receives the last screenshot but no separate response field. Neither receives the full environment history; actual answer presence and evaluation are unobserved.
- Selection predicate: CLI `text` or `vision`, with `gpt-4o` forced to vision; exact extracted status equal to success after lowercasing yields true.
- Invalidation or expiry: Evaluation JSON overwritten for the selected model/task; no freshness, calibration or expiry rule inspected.
- Activation or effect: Status-to-result production wired; subsequent selection wired but no observed decisions supplied.
- Evidence limits: Model accuracy, external environment truth and actual input histories unobserved; error returns a dictionary rather than success's one-element list, so downstream list indexing is not a reliable rejection protocol.

Possible outcomes are success/failure, empty or malformed status converted to false, or exception with `rm: None`. Software enforces status conversion, not factual correctness. License is bounded apparent task completion under the presented evidence. The operational consumer is the induction success selector, through JSON with enforcing eligibility force for later induction invocations. The model proposes the judgment; software decides its Boolean encoding; there is no per-result human veto in this script. Content/update relation is indeterminate: no supplied model output establishes whether a judgment restates evidence or makes a non-entailed inference. SRC-1, `webarena/autoeval/evaluator.py`, `webarena/autoeval/prompts.py`, `webarena/autoeval/evaluate_trajectory.py`.

> prompt, sys_msg = build_text_eval_prompt(
>             info["captions"][-1], info["intent"], response, action_history
>         )
> --- `webarena/autoeval/evaluator.py`

> else:
>             valid_actions.append(a)
>     return valid_actions
> --- `webarena/autoeval/evaluate_trajectory.py`

> actions = [act for acts in action_list for act in acts]
>     if "send_msg_to_user" in action_list[-1][0]:
>         response = extract_response(action_list[-1][0])
>     else:
>         response = ""
> --- `webarena/autoeval/evaluate_trajectory.py`

> def eval_vision(self, info, client):
>         assert client == "gpt-4v" or client == "gpt-4o"
>         action_history = ""
>         for idx, act in enumerate(info["actions"]):
>             action_history += f"{idx+1}: {act}\n"
>         prompt, sys_msg = build_vision_eval_prompt(
>             info["intent"], info["response"], action_history
>         )
>         img = info["images"][-1]
> --- `webarena/autoeval/evaluator.py`

> prompt = f"""User Intent: {intent}
>
> Action History:
> {last_actions}
>
> The last snapshot of the web page is shown in the image."""
> --- `webarena/autoeval/prompts.py`

> if out["status"].lower() == "success": eval_result = True
>         else: eval_result = False
> --- `webarena/autoeval/evaluate_trajectory.py`

#### EPI-RTE-success-selection
Label: Success trajectory selection
Part of: [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)

The neural parent's source-trajectory disposition is separate from checking and generation. Rule induction has equivalent predicates, see [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), but owns a different subsequent human/automatic admission. Owner: induction driver. Trigger: direct CLI or pipeline after task evaluation. Endpoints: result directories → truthy reward or matching evaluation JSON → eligible trajectory directories → template grouping and random sampling → induction prompt. Operating mode is bounded benchmark source curation. Software decides eligibility; autoeval model proposes the signal, `gt` imports BrowserGym cumulative reward as a reference outcome. Human per-trace veto is absent in this neural selector. Target/use/criterion: choose ostensibly successful executions as induction examples; predicate is truthiness, not a replay test or generated-workflow acceptance criterion. No content update occurs at this disposition.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Eligible directory list and sampled examples.
- Later read-back: Selected trace content can be transformed into workflow files and reach later action calls through the parent's write/read path.
- Delegated visibility: Induction model receives formatted selected query/thought/action examples, not evaluation rationale, reward or full observations.
- Selection predicate: `criteria == gt` with truthy `cum_reward`, or matching model filename with truthy `record[0]["rm"]`; template-group random sample after parsing.
- Invalidation or expiry: Missing autoeval file skipped; parse failures skipped later; no result freshness check or rollback transaction.
- Activation or effect: Enforcing eligibility gate for induction inputs, not permission for browser actions; actual choices unobserved.
- Evidence limits: Default evaluator/model filenames differ; external reward semantics unavailable; malformed result objects can raise before the later parse-skip branch.

Epistemic authority is at most outcome-based source selection in the original task domain. It does not warrant explanation, generalization, replay safety or component attribution. Behavioral path: induction model consumes selected examples in a user prompt, with software-enforced source eligibility and model-interpreted example guidance; horizon is this induction and later consumers of its result. New workflow replacement and its recovery are owned by the parent record. SRC-1, `webarena/induce_prompt.py`; the parent's retained quote supplies the autoeval predicate.

> if json.load(
>                 open(os.path.join(res_dir, f, "summary_info.json"))
>             )["cum_reward"]
> --- `webarena/induce_prompt.py`

#### EPI-RTE-trajectory-cleanup
Label: Neural trajectory cleanup
Part of: [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)

Owner: neural induction's parser. Endpoints: selected experiment log → action filtering and aligned thoughts → formatted induction example. This function deletes invalid/missing steps and scroll/noop, not task claims through criticism. Deterministic concrete deduction without execution: an action list containing `scroll(0, 300)`, `click('abc')` and `fill('123', 'x')` loses the first by explicit branch, loses the second because inner `eval('abc')` raises in the protected click branch, and retains the third because its first argument evaluates to a string. If a block loses all actions, the paired thought is skipped. Thus a selected successful trajectory can reach induction without navigation steps. The evaluator's cleanup, by contrast, keeps scroll/noop and requires only string-valued click arguments; rule cleanup also keeps scroll/noop. Non-ampliative reshaping does not imply a complete or replay-equivalent history.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Filtered actions with corresponding thoughts formatted as text.
- Later read-back: Filtered examples feed model generation whose written output may be read by later legacy calls; raw removed steps do not reach this prompt.
- Delegated visibility: Induction model receives query, aligned thoughts and surviving actions, not screenshots or evaluator record.
- Selection predicate: Click ID must be a string whose inner evaluation is an integer; fill ID string; scroll/noop removed; other action text retained.
- Invalidation or expiry: Failed click parsing drops action; failed trajectory extraction skips the example; no restoration of removed steps.
- Activation or effect: Enforcing source-content omission before induction, wired without observed activation.
- Evidence limits: These are code deductions only. `eval` is executable log consumption, not a semantic validator; a fill parse exception may discard the whole trace through the caller's broad catch.

Evaluator is a symbolic parser over textual action arguments, with a type/shape domain, not task truth. Epistemic authority is only provenance as a filtered excerpt, degraded for completeness. Operational authority is controlling what the induction model receives; channel is formatted user-prompt examples, force enforcing omission then advisory interpretation, horizon current induction and later retained output. SRC-1, `webarena/induce_prompt.py`, `webarena/induce_rule.py`, `webarena/autoeval/evaluate_trajectory.py`.

> elif "scroll(" in a or "noop(" in a:
>             continue
> --- `webarena/induce_prompt.py`

> if len(actions) == 0: continue
>         action_list.append(actions)
> --- `webarena/induce_prompt.py`

#### EPI-RTE-workflow-filter
Label: Mind2Web workflow filter
Part of: [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission)

Owner: shared data helper, called by both offline and online writers. Endpoints: generated text → blank-line block splitting → requested website-header trimming → delta-header truncation → literal substring deletion → joined text. Concrete deduction: with website `shop`, input `# shop\n\nUseful workflow\n\nSearch delta airlines\n\n# delta\n\nOther text` yields only `Useful workflow`. The first header removes the prefix; the delta header removes itself and following blocks; the remaining block mentioning delta is removed even though it is not a header. This does not add propositions, but can delete legitimate task content. No truth evaluator is present in this function: the target is block labels/substrings, not correctness of instructions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Joined retained workflow blocks.
- Later read-back: Parent writer saves the result; later Mind2Web exemplar loading receives that filtered file subject to budget.
- Delegated visibility: Downstream model gets only surviving blocks without deletion rationale.
- Selection predicate: Single-line heading ending with website, first delta heading, then any remaining block containing lowercase delta.
- Invalidation or expiry: Removed content unavailable in the written file; whole-file replacement and recovery are see parent record.
- Activation or effect: Enforcing textual omission before writing; no observed target output or behavioral dependence.
- Evidence limits: Does not validate step count, non-overlap, grounding or task transfer; this deterministic example is implementation-layer deduction only.

Epistemic license is retained-text identity, not a workflow correctness decision. Operational consequence: changes subsequent exemplar content. Behavioral path: helper → file writer → prediction user-message exemplar, enforcing omission then advisory guidance, horizon later sample invocations. SRC-1, `mind2web/utils/data.py`.

> blocks = [b for b in blocks if "delta" not in b.lower()]
>     return '\n\n'.join(blocks)
> --- `mind2web/utils/data.py`

#### EPI-RTE-annotation-score
Label: Mind2Web annotation scoring
Part of: [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action)

Owner: Mind2Web consumer. Endpoints: predicted action and imported annotation → first-positive-ID membership, action-string F1, exact step equality → all-step task indicator → saved conversation metrics. Target/domain: agreement with annotated actions and elements in bounded benchmark replay, not actual environment completion. The expected answer oracle is the dataset, supplied externally; it supplies scoring reference and previous-step context. Program decides scores, model proposes prediction, no human per-score veto. Deterministic derivation: equal parsed prediction and target strings append a one; all episode steps equal produces task success one. These propositions follow from the inputs under the code's criteria, without establishing annotation truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Metrics and prediction/target pair appended to task conversation JSON.
- Later read-back: Result aggregation can consume metrics; online induction consumes only input/output dictionaries, not a success gate based on them.
- Delegated visibility: Acting provider receives observations and prior annotated actions; online induction receives last input/output, not metric-based admission.
- Selection predicate: First positive candidate for element membership, F1 over constructed operation/value strings, exact action equality and all-step success; missing target/context overflow produces failed steps.
- Invalidation or expiry: Per-task metric arrays reinitialized and task JSON rewritten; no versioned score history in this function.
- Activation or effect: Diagnostic/scoring force, not enforcing exclusion from online induction; no observed scores or benefit supplied.
- Evidence limits: External annotations/ranking scores absent; supplied observed pages are not reached by executing predictions. F1 helper is not independently audited here.

Epistemic scope is conditional agreement, not process correctness or workflow quality. Operational consequence is stored evaluation data and aggregation, with no checked generated-workflow acceptance. Consumer/channel/force/horizon: saved JSON to results analysis, diagnostic over benchmark tasks; online induction bypasses metric decisions. SRC-1, `mind2web/memory.py`, `mind2web/online_induction.py`.

> if pred_act == target_act:
>             step_success.append(1)
>         else:
>             step_success.append(0)
> --- `mind2web/memory.py`

> if np.sum(step_success[-episode_length:]) == episode_length:
>         success.append(1)
>     else:
>         success.append(0)
> --- `mind2web/memory.py`

#### EPI-RTE-retrieval-selection
Label: Optional retrieval selection

Distinct source-native CLI route, not called by the default pipelines or identical to their consumers. Closest supplied record [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) owns the component; [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action) owns later prediction, not this file-producing selector. Owner: retrieval script. Endpoints: parsed workflow blocks or concrete exemplars → random choice or dense similarity ranking → selected text file. Workflow parsing rejects blocks shorter than four lines and normalizes names. The ordinary semantic workflow branch passes a metadata list into `similarity_search_with_score`; the ablation branch creates FAISS directly and therefore is not covered by that defect. Both semantic branches request name/docstring or exemplar-specifier similarity, not correctness assessment. Selection is computational; operator selects mode, not each item. No expected-answer oracle or human content veto. Trigger: direct CLI. Proposed change is consumer-ready selected text, admission through ranking/random sampling, recovery absent in these writes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Randomly selected workflow text, or ablation-selected exemplar text written to output; ordinary semantic workflow branch has incompatible object wiring.
- Later read-back: Output is suitable for workflow-file consumers if the operator passes its path; automatic default-pipeline linkage not found in supplied runtime.
- Delegated visibility: Embedding service sees names/docstrings or exemplar specifiers; output consumer sees full selected content, not similarity scores.
- Selection predicate: Random sample or query similarity per task, followed by pooled score sort descending; parser length/name conditions and suffix selection also limit admission.
- Invalidation or expiry: Whole output overwrite; optional saved FAISS index; no expiry or correctness invalidation.
- Activation or effect: Selection/write implementation inspected, with ordinary semantic defects; no observed retrieval quality or downstream dependence.
- Evidence limits: Non-null workflow suffix references undefined `args.suffix`; external score semantics uninspected, so descending order is described without claiming relevance-optimal ranking.

Content relation is non-ampliative reshaping/selection with warrant neither improved nor checked; original context may be omitted. Behavioral path: selector → local output → optional consumer prompt, ranking/permissive file admission then advisory model guidance, horizon later tasks using supplied path. No lifecycle integration after claim acceptance. SRC-1, `mind2web/workflow/retrieve.py`.

> return metadatas
> --- `mind2web/workflow/retrieve.py`

> memory = FAISS.from_texts(texts=texts, embedding=embedding, metadatas=metadatas)
> --- `mind2web/workflow/retrieve.py`

### Claims

#### EPI-CLM-workflow-induction
Label: Workflow induction and integration

Claimed operation: induce, integrate and utilize workflows with example-specific contexts abstracted away, offline from annotated examples or online from experience. SRC-1, `README.md`, doctrine/design. Distinct from supplied [RT-CLM-context-budget](runtime.md#rt-clm-context-budget), which claims context fitting rather than induction or knowledge production. Shipped neural and Mind2Web instructions request reusable abstraction; operational context supply is implemented. No claim of formal proof or infallibility is found in this README passage.

> Agent Workflow Memory (AWM) proposes to induce, integrate, and utilize workflows via an agent memory.
> A workflow is usually a common sub-routine in solving tasks, with example-specific contexts being abstracted out.
> --- `README.md`

#### EPI-CLM-benchmark-benefit
Label: Reported benchmark benefit

Claimed operation/warrant: 35.6% WebArena success and strong Mind2Web cross-task/site/domain generalization. SRC-1, `README.md`, reported operation. Distinct from [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) and [EPI-CLM-workflow-induction](#epi-clm-workflow-induction): this concerns measured benefit, not route existence. No inspectable execution/comparison data registered for reproducing these statements; outcome success alone would not establish a component effect or explanatory mechanism.

> We achieve the state-of-the-art result -- 35.6% success rate.
> --- `README.md`

> We also get the best scores among text-based agents. Particularly, AWM offline effectively generalizes across a wide range of tasks, websites, and domains.
> --- `README.md`
