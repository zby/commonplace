---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "GMemory epistemic routes: task-outcome checks, lossy experience extraction and automatic admission of reusable guidance."
run-id: AAS-2026-10-15-gmemory-a2192cc823f7-01
reviewed-boundary: "7b581c51d993bd600df14691d101d7e601040cc6"
---

# GMemory epistemic report

## Source-and-claim boundary

The question is which content GMemory checks, what those checks license, and how retained results affect later tasks. Scope and external exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not authenticated GMemory operation or causal comparison. Runtime findings are provisional source-grounded inputs, not execution evidence.

The consequential public claim is [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory). The report assesses the implemented routes underlying it, including model calls outside solving agents. External provider weights, benchmark correctness and live Wikipedia truth remain unassessed. No target execution was performed. Missing authenticated traces prevent identifying actual generated propositions, observed semantic preservation, qualifying acceptance of particular generalized claims, activated behavioral dependence and benefit. Missing intervention/comparison prevents attributing improvement to memory or any component. These gaps do not erase implemented selection and revision.

| Entry point or operation | Source path in SRC-1 | Coverage and conclusion boundary |
|---|---|---|
| Launcher, CLI and module dispatch | `run_mas.sh`, `tasks/run.py`, `mas/module_map.py` | Runtime launcher findings; direct CLI and fixed-map reads confirm GMemory selection, shared model and task loop. [RT-RTE-task-retention](runtime.md#rt-rte-task-retention). Comparator modes excluded as in boundary. |
| Chat and embedding backends | `mas/llm.py`, `mas/utils.py` | Direct chat read; embedding findings supplied by [RT-CMP-embedding-func](runtime.md#rt-cmp-embedding-func). No provider-native tools in inspected chat request. Remote learned state remains opaque; no claim about its epistemic process. |
| Retrieval, ranking, role projection | `mas/memory/mas_memory/GMemory.py`, `tasks/mas_workflow/format.py` | Direct reads; [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery). Both projection variants inspected, including optional trajectory input. Ranking is relevance, not truth adjudication. |
| Task extraction, diagnosis and persistence | `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/memory_base.py`, `mas/memory/common.py` | Direct GMemory extraction and StateChain slice/pop reads plus supplied base-lifecycle findings; [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup), [RT-RTE-task-retention](runtime.md#rt-rte-task-retention). |
| Rule proposal, parser, mutation, pruning, merging and backward | `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py` | Direct implementation and maintenance-prompt reads; [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [EPI-RTE-rule-disposition](#epi-rte-rule-disposition). Separate merge path is not covered by operation-parser checks. |
| AutoGen, DyLAN and MacNet consumers/critics | `tasks/mas_workflow/autogen/autogen.py`, `tasks/mas_workflow/dylan/dylan.py`, `tasks/mas_workflow/macnet/graph_mas.py` | Supplied [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions), [RT-RTE-dylan-actions](runtime.md#rt-rte-dylan-actions), [RT-RTE-macnet-actions](runtime.md#rt-rte-macnet-actions), not new full workflow reads. Repetition, consensus and model ranking are action-selection signals, not independent answer oracles. |
| FEVER Search, Lookup, Finish and final feedback | `tasks/envs/fever_env.py`, `tasks/envs/utils.py` | Direct reads; [EPI-RTE-wiki-acquisition](#epi-rte-wiki-acquisition), [EPI-RTE-fever-check](#epi-rte-fever-check). |
| ScienceWorld outcome | `tasks/envs/sciworld_env.py` | Direct step/feedback/subgoal reads; [EPI-RTE-subgoal-check](#epi-rte-subgoal-check). |
| ALFWorld and PDDL outcome | `tasks/envs/alfworld_env.py`, `tasks/envs/pddl_env/pddl_env.py` | Direct step/feedback reads plus supplied [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions). Third-party/vendored simulator semantics not audited; no simulator-correctness conclusion. |
| Improvement-analysis prompt | `mas/memory/mas_memory/prompt.py` | Direct read of `analyze_mas_pattern` prompts; source search across `mas/` and `tasks/` found definitions/attribute exposure only. [EPI-CLM-output-improvement](#epi-clm-output-improvement). It does not establish an operative evaluator. |
| Dataset/static prompts, graph index, logs | `data/`, `tasks/prompts/`, `mas/memory/mas_memory/GMemory.py`, `logs/` | Supplied boundary/runtime findings only for datasets, static prompts and logs; graph role supplied, merge consumer directly read. No exhaustive dataset, prompt-quality, graph-quality or observed-run assessment. |

Coverage supports route-local conclusions, not a system-complete negative about every possible content check. Available uninspected benchmark internals and prompt bodies are not access gaps or evidence of absence. Frozen CLI/module selection and the inspected chat request reveal a fixed benchmark action channel, not an additional registered provider-tool/hook evaluator. The extra exposed improvement prompt remains doctrine-only within the recorded search.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-task-trajectory](#epi-obj-task-trajectory) | Actions and observed task states; sequence claims over one task | see record | see record | Attempted reward-based deletion leaves backing states unchanged; digit erasure loses numeric distinctions in model input. Final label is not proof of every step. |
| [EPI-OBJ-key-steps](#epi-obj-key-steps) | Model statements about necessary/salient steps | see record | see record | Not determined to be entailed by trace; no particular output supplied. |
| [EPI-OBJ-fail-reason](#epi-obj-fail-reason) | Model explanation of task failure | see record | see record | Outcome mismatch does not identify causal blame; prompt is household-object oriented even for other tasks. |
| [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | Generalized causal assertions when present; imperatives can instead be non-truth-apt policies | see record | see record | Actual content not determinable without generated rules. Causal wording is requested, not validated. |
| [EPI-OBJ-insights-score](#epi-obj-insights-score) | Numerical scores and task associations; not themselves evidence that a rule is true | see record | see record | Retention and selection controls, not calibrated probabilities or isolated component effects. |
| [EPI-OBJ-projected-insights](#epi-obj-projected-insights) | Role-adapted claims or policies, if produced | see record | see record | Preservation versus changed meaning is indeterminate; unnumbered output can disappear. |
| [EPI-OBJ-wiki-document](#epi-obj-wiki-document) | External encyclopedic claims | see record | see record | URL remains in adapter metadata but is not necessarily present in returned observation; source truth unverified. |

## Authority-route ledger

Architectural status is local to this assessment. Other fields owned by a declaring record are cited with `see`. Each row separates a consequential function even when one supplied container record supports several rows. All implemented rows lack authenticated operation evidence.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-wiki-acquisition](#epi-rte-wiki-acquisition) | content transformation | implemented | [EPI-OBJ-wiki-document](#epi-obj-wiki-document) | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | External content acquired; warrant unknown and displayed lineage degraded | see route | see route | see route | none | none | Not knowledge produced by GMemory |
| [EPI-RTE-fever-check](#epi-rte-fever-check) | check/evidence production | implemented | Proposed Finish label | no content change | see route | see route | see route | see route | see route | Normalized equality to dataset answer only | see route | see route | see route | none | none | Not verification of supporting Wikipedia passages or reasoning |
| [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions) | disposition/acceptance | implemented | Final task outcome | no content change | Final feedback label | see route | see route | see route | see route | ALFWorld done; PDDL wrapper done/reward; task-domain outcomes only | see route | see route | see route | none | none | Code recording a success criterion can license task success, not generalized guidance |
| [EPI-RTE-subgoal-check](#epi-rte-subgoal-check) | check/evidence production | implemented | ScienceWorld subgoal completion | no content change | see route | see route | see route | see route | see route | Configured regex occurrence only | see route | see route | see route | none | none | State-goal fidelity rests on configuration and simulator |
| [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup) | content transformation | implemented | [EPI-OBJ-task-trajectory](#epi-obj-task-trajectory) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Does not preserve all task-state distinctions | see route | see route | see route | none | Lossy input to later interpretation | Cannot assume a faithful abstraction in numeric tasks |
| [RT-RTE-task-retention](runtime.md#rt-rte-task-retention) | content transformation | implemented | [EPI-OBJ-key-steps](#epi-obj-key-steps), [EPI-OBJ-fail-reason](#epi-obj-fail-reason) | truth-apt transformation: indeterminate | Key-step extraction and failure diagnosis, distinct outputs | see route | see route | see route | see route | Candidate interpretations, not checked deductions | see route | see route | see route | none | none | Extractor outputs and explanations lack semantic gate |
| [RT-RTE-task-retention](runtime.md#rt-rte-task-retention) | retention | implemented | [EPI-OBJ-task-trajectory](#epi-obj-task-trajectory), [EPI-OBJ-key-steps](#epi-obj-key-steps), [EPI-OBJ-fail-reason](#epi-obj-fail-reason) | no content change | see route | see route | see route | see route | see route | Task label qualifies outcome, not generated condensation/explanation | see route | see route | see route | [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | none | Retention before semantic acceptance, not lifecycle integration |
| [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | content transformation | implemented | [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | truth-apt transformation: indeterminate | Success-only or success/failure-based generalized guidance | see route | see route | see route | see route | Prompt requests generalized causal hypotheses; no inspected concrete entailment or non-entailment witness for an output | see route | see route | see route | [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | Generality requested, not earned by syntax | Some outputs may be policies rather than propositions |
| [EPI-RTE-rule-disposition](#epi-rte-rule-disposition) | check/evidence production | implemented | [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | no content change | see route | see route | see route | see route | see route | Syntactic/substring/index predicates only | see route | see route | see route | none | none | No truth license follows |
| [EPI-RTE-rule-disposition](#epi-rte-rule-disposition) | disposition/acceptance | implemented | [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | no content change | see route | see route | see route | see route | see route | Software admission, not evidence-consuming semantic acceptance | see route | see route | see route | [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | Operational admission differs from epistemic acceptance | See AGREE text/index counterexample in record |
| [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | retention | implemented | [EPI-OBJ-insights-rule](#epi-obj-insights-rule), [EPI-OBJ-insights-score](#epi-obj-insights-score) | no content change | see route | see route | see route | see route | see route | Positive score licenses survival, not truth | see route | see route | see route | [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | none | JSON persistence is not post-acceptance lifecycle integration |
| [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | content transformation | implemented | [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | truth-apt transformation: indeterminate | Cluster-based merge | see route | see route | see route | see route | Prompt asks strict input-based consolidation; implementation does not verify preservation | see route | see route | see route | none | Requested non-ampliative reshaping remains unverified | Numbered-list parser bypasses operation checks |
| [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | disposition/acceptance | implemented | Merged [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | no content change | Replacement rule list | see route | see route | see route | see route | No new truth warrant; fresh score/associations are bookkeeping | see route | see route | see route | none | none | Old list cleared; no semantic veto/rollback in inspected routine |
| [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | behavior/policy adaptation | implemented | [EPI-OBJ-insights-score](#epi-obj-insights-score) | non-truth-apt policy/content update: survival score | Retrieved raw rule credit after final outcome | see route | see route | see route | see route | Outcome-correlated survival only; no isolated rule-effect estimate | see route | see route | see route | [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | Raw-rule credit without verified use | DyLAN has no post-task backward; merge before backward may change text matching |
| [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) | operational admission/selection/consumption | implemented | Task examples and [EPI-OBJ-insights-rule](#epi-obj-insights-rule) | no content change | see route | see route | see route | see route | see route | Similarity/relevance/association licenses selection only | see route | see route; [RT-BAP-retained-guidance](runtime.md#rt-bap-retained-guidance) | see route | [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | none | Failed tasks returned but discarded by schedules; not discarded by maintenance |
| [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) | content transformation | implemented | [EPI-OBJ-projected-insights](#epi-obj-projected-insights) | truth-apt transformation: indeterminate | Role and optional trajectory adaptation | see route | see route | see route | see route | No renewed semantic acceptance after projection | see route | see route | see route | none | none | Successful parse need not preserve raw rule content |
| [RT-RTE-dylan-actions](runtime.md#rt-rte-dylan-actions), [RT-RTE-macnet-actions](runtime.md#rt-rte-macnet-actions), [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions) | operational admission/selection/consumption | implemented | Action candidates, model critiques and consensus | non-truth-apt policy/content update: next action selection | see routes | see routes | see routes | see routes | see routes | Repetition, agreement and model preference are not external correctness evidence | see routes | see routes | see routes | none | none | Model explanations may also contain truth-apt content, not individually recoverable here |
| [EPI-CLM-output-improvement](#epi-clm-output-improvement) | check/evidence production | doctrine only | Initial versus final MAS output | no content change | see claim | see claim | No invocation found in recorded source search | Requested True/False judgment only | No demonstrated consumer | None established | None established | None found in searched code | see claim | [EPI-CLM-output-improvement](#epi-clm-output-improvement) | Unused evaluator prompt | No implemented improvement gate established by this prompt |

No separate post-acceptance lifecycle-integration route is established for generalized guidance in these inspected maintenance and delivery routines. Associations, retrieval and use happen without such acceptance; they remain real operational functions. This is not an assertion that acceptance is required for a useful operational memory.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory) | see claim | see claim | Hierarchical experience and revisable rules | [RT-RTE-task-retention](runtime.md#rt-rte-task-retention), [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | None authenticated for these routes | No independent memory/rule intervention; benchmark labels do not isolate mechanism | Implemented cross-task adaptation capacity, not demonstrated improvement | General causal rules lack semantic acceptance; delivery is not compliance |
| [EPI-CLM-general-principles](#epi-clm-general-principles) | see claim | see claim | Causal/generalized criticism requested | [EPI-RTE-rule-disposition](#epi-rte-rule-disposition), [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) | No specific generated rule inspected as an authenticated output | Success/failure comparison does not itself identify causal mechanisms or transfer | Candidate guidance can be revised and reused | Format acceptance does not establish causal/general applicability |
| [EPI-CLM-output-improvement](#epi-clm-output-improvement) | see claim | see claim | Prompt asks model to compare initial and final outputs | No invoked route found in searched `mas/` and `tasks/` | None | Even an invoked model judgment alone would not isolate memory benefit | Design text only within search | No consequential improvement-check consumer established |

## Bounded conclusion

GMemory acquires environment observations and, in FEVER, external Wikipedia text. The latter is imported, not produced knowledge; the adapter retains a page URL internally while delivering paragraphs without an enforced citation field. External source warrant is unknown and displayed lineage is degraded ([EPI-RTE-wiki-acquisition](#epi-rte-wiki-acquisition)). Outcome checks have narrow and different licenses: normalized FEVER label equality, ScienceWorld observation-pattern completion, ALFWorld done, and PDDL wrapper outcome. They supply operative success labels for retention and rule feedback, not validation of trajectory explanations, causal guidance or replay safety ([EPI-RTE-fever-check](#epi-rte-fever-check), [EPI-RTE-subgoal-check](#epi-rte-subgoal-check), [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)). FEVER step termination on a wrong Finish is not final success.

Experience is retained after trajectory reconstruction and model interpretation. Attempted negative-reward-state deletion does not mutate the backing chain; those states remain in the reconstructed trajectory. Independently, digit erasure in `clean_traj` loses numeric distinctions before extraction/diagnosis. A concrete numeric counterexample prevents treating that transformation as universally meaning-preserving. Key steps and failure reasons are candidates; no checked derivation from warranted premises is established. Rules and role-adapted/merged variants can contain truth-apt claims, but their exact semantic relations remain indeterminate without outputs. Prompts asking for broad causal claims are not evidence that any produced claim was non-entailed, true, or accepted ([EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup), [EPI-OBJ-key-steps](#epi-obj-key-steps), [EPI-OBJ-fail-reason](#epi-obj-fail-reason), [EPI-OBJ-insights-rule](#epi-obj-insights-rule), [EPI-OBJ-projected-insights](#epi-obj-projected-insights)).

The material admission criteria are task labels, model-proposed operations, format/index/substring filters, positive survival scores and numbered-list merge parsing. AGREE's numeric check does not guarantee the intended target: a no-match text lookup returns -1 and can credit the last rule. Their intended use is reusable benchmark guidance. None of those inspected gates records an evidence-consuming semantic acceptance decision with a criterion for the general truth and scope of a particular rule. Retention and task associations therefore do not establish post-acceptance lifecycle integration. They do establish automatic, revisable operational guidance: update models consume old rules and experiences; solving models receive selected/projected text through advisory user prompts over later tasks and reloads ([EPI-RTE-rule-disposition](#epi-rte-rule-disposition), [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [RT-BAP-retained-guidance](runtime.md#rt-bap-retained-guidance)).

Score feedback is a direct policy adaptation even when a rule is only an imperative. Task success/failure changes survival without demonstrating rule compliance or identifying causal contribution. DyLAN differs from AutoGen/MacNet in post-task credit; merging can replace the text before cached-rule credit. These are operational distinctions, not a reason to deny adaptation capacity ([EPI-OBJ-insights-score](#epi-obj-insights-score)).

The independent theory, learning and reflection limits remain those in [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance): localized revisable guidance is afforded; actual content-dependent criticism and iteration of qualifying criticism are not established by syntax or scores. Computation performs internal sampling/proposal/admission; that automation does not entail all theory-builder conditions. Remote model parameters and version identity remain bounded as in [RT-CMP-gpt-chat](runtime.md#rt-cmp-gpt-chat) and [RT-CMP-embedding-func](runtime.md#rt-cmp-embedding-func). No local model training follows from rule revision. For the shipped cross-task benchmark horizon and independently specifiable objective of later task success, source wiring supports improvement-directed self-change through guidance, but authenticated later operation causally depending on the change is missing; exercised self-improvement and successful improvement are not established. No single epistemic verdict follows across these heterogeneous routes.

## Shared records

### Operative objects

#### EPI-OBJ-task-trajectory
Label: Extracted task trajectory

Part of: [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

This object is retained material within that route, not a duplicate of the route. Source-native identity: `MASMessage.task_trajectory`, `chain_of_states`, and extra `clean_traj`. Form: natural-language actions/observations with symbolic sequence and reward metadata; storage: copied MASMessage, then Chroma metadata. SRC-1, `mas/memory/mas_memory/GMemory.py`. Successful stored trajectory and cleaned model-input trajectory are distinct views; see [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup) for the load-bearing passage and differences.

#### EPI-OBJ-key-steps
Label: Extracted key steps

Part of: [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

Object within the route, not its replacement. Source-native identity: `key_steps` extra field. Form: natural language interpreted by models; storage: MASMessage extra metadata in task storage. Producer consumes task description and `clean_traj`; later consumers include example formatting and success-only rule generation. No expected condensation or entailment check is wired around the response. SRC-1, `mas/memory/mas_memory/GMemory.py`.

> response: str = self.llm_model(messages, temperature=0.1)
> mas_message_copy.add_extra_field('key_steps', response)
> --- `mas/memory/mas_memory/GMemory.py`

> history: list[str] = [f'task{i}:\n' + task.task_description + task.get_extra_field('key_steps') for i, task in enumerate(success_trajectories)]
> --- `mas/memory/mas_memory/GMemory.py`

#### EPI-OBJ-fail-reason
Label: Model failure reason

Part of: [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

Distinct output object inside task retention. Source-native identity: `fail_reason`. Form: natural language; storage: task extra metadata. `_detect_mistakes` consumes the cleaned failed trajectory, not an independent causal experiment. Comparative rule prompts later consume this explanation. SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py`. Household-object mismatch guidance is not a universal benchmark-specific diagnosis contract.

> if mas_message_copy.label == False:
>     reason: str = self._detect_mistakes(mas_message_copy)
>     mas_message_copy.add_extra_field('fail_reason', reason)
> --- `mas/memory/mas_memory/GMemory.py`

> Based on the above rules, summarize the most likely reason for the error in a concise manner.
> --- `mas/memory/mas_memory/prompt.py`

#### EPI-OBJ-insights-rule
Label: Insight rule text

Part of: [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)

This is the text part of the maintenance container, not a second declaration of the container. Source-native identity: `insights_memory` entries' `rule`. Form: natural language; storage: in-process dictionaries and namespace JSON. Generated generalized claims/policies are supplied to maintenance, merge, projector and solving consumers. Text is individually replaceable, but no explicit assumptions/scope/rationale structure is enforced. SRC-1, `mas/memory/mas_memory/GMemory.py`; requested semantics in [EPI-CLM-general-principles](#epi-clm-general-principles), admission in [EPI-RTE-rule-disposition](#epi-rte-rule-disposition).

> rule_data['rule'] = operation_rule_text
> rule_data['score'] += 1
> rule_data['positive_correlation_tasks'] = list(set(rule_data['positive_correlation_tasks'] + relative_tasks))
> --- `mas/memory/mas_memory/GMemory.py`

Merge is a distinct generation/admission path over the same text object. The prompt requests non-ampliative consolidation, but no semantic equivalence check is implemented. The implementation asks for `actual_num//3` after setting `actual_num = len(batch)//3`; advertised limits and actual compliance must not be inferred from naming. The old list is cleared and rebuilt with score 2 and all cluster task associations, so the rebuilt correlations do not demonstrate per-task successful use.

> merged_rules.extend(parse_numbered_list(raw_merged_rules))
> --- `mas/memory/mas_memory/GMemory.py`

> self.insights_memory.clear()
>
> for label, related_rules in merged_label_rules.items():
> --- `mas/memory/mas_memory/GMemory.py`

> - All merged insights **must be based strictly on the given inputs**. You are **not allowed to make up** or infer any new information.
> --- `mas/memory/mas_memory/prompt.py`

#### EPI-OBJ-insights-score
Label: Rule score and task associations

Part of: [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)

Distinct symbolic metadata part, not text or model weights. Source-native identities: `score`, `positive_correlation_tasks`, `negative_correlation_tasks`; storage: rule dictionaries/JSON. Score controls survival; positive associations control candidate selection and ranking. Negative associations are recorded but `_find_related_insights` reads positive membership only. Retrieval counts association matches rather than sorting by survival score. See supplied maintenance route for count triggers and read-back. SRC-1, `mas/memory/mas_memory/GMemory.py`.

> for inner_insight in self.insights_memory:
>     if insight in inner_insight['rule']:
>         inner_insight['score'] += reward
> --- `mas/memory/mas_memory/GMemory.py`

> self.insights_memory = [self.insights_memory[i] for i in range(len(self.insights_memory))
>                         if self.insights_memory[i]['score'] > 0]
> --- `mas/memory/mas_memory/GMemory.py`

> score: int = sum(task in rule.get('positive_correlation_tasks', []) for task in task_mains)
> --- `mas/memory/mas_memory/GMemory.py`

Backward rewards all matching cached raw rule substrings by +1 on success or -2 on failure, without checking which projected statement was used. Nominal REMOVE decreases score; it need not delete immediately. This is survival feedback, not semantic falsification or a calibrated rule-effect estimate. Because save-time merge precedes workflow backward, replaced text can fail to match cached text; that bounds even operational credit assignment.

#### EPI-OBJ-projected-insights
Label: Role-specific insights

Part of: [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)

Distinct transient text output within delivery. Source-native identity: `project_insights` return. Form: natural-language list; storage: transient returned list/role rules, not a separately persisted verified rule version. Consumers are role-specific solver prompts. Both raw-only and raw-plus-trajectory paths request adaptation; no semantic equivalence test separates faithful rewriting from added claims. SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py`.

> role_insights = self.llm_model(messages)
>
> try:
>     role_insights = parse_numbered_list(role_insights)
>     return role_insights
> except:
>     return raw_insights
> --- `mas/memory/mas_memory/GMemory.py`

A nonnumbered response has no regex matches and returns an empty list without an exception. Thus the exception fallback is not a guarantee that raw guidance survives.

#### EPI-OBJ-wiki-document
Label: Wikipedia document and displayed passages

Source-native identity: `LangChainWiki.document`, `Document.page_content` and `metadata['page']`. Form: natural-language encyclopedic content plus symbolic URL metadata; storage: adapter process memory; passages subsequently enter task observations and retained traces. No supplied operative-object counterpart; the closest supplied [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions) is a broad action route, not the external content object. SRC-1, `tasks/envs/utils.py`; passage and lineage details in [EPI-RTE-wiki-acquisition](#epi-rte-wiki-acquisition).

### Routes

#### EPI-RTE-trajectory-cleanup
Label: Attempted reward filtering and numeric erasure

Part of: [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

Distinct transformation phase inside the retention container. Owner: GMemory `_extract_mas_message`. Endpoints: deep-copied MASMessage → attempted negative-reward-state deletion via `pop_state` → reconstruction from unchanged backing states → digit-free `clean_traj` → model extraction/diagnosis. `chain_of_states` returns a fresh slice; popping it does not remove a backing-list state. Successful `task_trajectory` is replaced by the reconstructed trajectory before numeric erasure; failed `task_trajectory` is not replaced there. SRC-1, `mas/memory/mas_memory/GMemory.py` and `mas/memory/common.py`, implementation; the slice/pop finding agrees with [MEM-RTE-state-roundtrip](memory.md#mem-rte-state-roundtrip) and the corrected parent retention record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: copied MASMessage with backing state chain unchanged by the deletion attempt, digit-erased `clean_traj` and generated extra fields.
- Later read-back: saved trajectory and key steps enter future examples; clean trajectory feeds key steps and failure diagnosis before save.
- Delegated visibility: extraction/diagnosis model receives cleaned text, not original numeric distinctions in that trajectory.
- Selection predicate: state graph reward below zero triggers a pop on a temporary slice, not effective state removal; every digit run is then erased from reconstructed text.
- Invalidation or expiry: copied views replace or supplement fields; original current-task object is not mutated by the deep copy.
- Activation or effect: implemented altered inputs to model interpretation and later storage; behavioral dependence unobserved.
- Evidence limits: slice/pop behavior and digit erasure are static implementation deductions, not observed operation. No actual trajectory supplied with authenticated route provenance; reward negativity would not itself prove that a step contains no useful evidence.

> if state_chain.get_state(state_id).graph.get('reward', 0) < 0:
>     state_chain.pop_state(state_id)
> --- `mas/memory/mas_memory/GMemory.py`

> def pop_state(self, idx: int) -> nx.Graph:
>     if idx >= len(self.chain_of_states) or idx < -len(self.chain_of_states):
>         raise ValueError('Index out of range.')
>     return self.chain_of_states.pop(idx)
> --- `mas/memory/common.py`

> @property
> def chain_of_states(self) -> list[nx.Graph]:
>     return self._chain_of_states[:-1]
> --- `mas/memory/common.py`

> if mas_message_copy.label == True:
>     mas_message_copy.task_trajectory = trajectory
>
>
> trajectory = re.sub(r'\d+', '', trajectory)
> mas_message_copy.add_extra_field('clean_traj', trajectory)
> --- `mas/memory/mas_memory/GMemory.py`

Implementation deduction, not target execution: reconstructed observation `The temperature is 20 C.` becomes `The temperature is  C.`; `The temperature is 80 C.` produces the same result. This erases a truth-relevant measurement distinction, not just an object identifier. In household tasks the prompt deliberately tolerates renumbered identical objects, a countercase where number removal may be harmless; that does not make it semantically safe across benchmark domains. The attempted deletion criterion is reward, not direct correctness of every state proposition; the called slice/pop implementation leaves those states available for reconstruction. This failed deletion attempt is separate from the effective digit erasure.

#### EPI-RTE-wiki-acquisition
Label: FEVER Wikipedia acquisition

Part of: [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)

The part denotes the FEVER environment subroute within that action container; the adapter is also used by other selected workflows. Owner: `FeverEnv` and `LangChainWiki`. Endpoints: Search argument → Wikipedia library page content/URL → stored Document → first paragraph or Lookup-selected paragraph → environment observation → current task context. SRC-1, `tasks/envs/utils.py`, `tasks/envs/fever_env.py`, implementation. Import does not validate external source truth. URL metadata is not added to the returned paragraph by these routines, degrading explicit lineage at the task-observation boundary.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search first paragraph or suggestions/error; Lookup numbered matching paragraph or no-result status.
- Later read-back: observations can enter task retention and examples through [RT-RTE-task-retention](runtime.md#rt-rte-task-retention); exact saved external statements are uninspected.
- Delegated visibility: solving model gets observation text; no enforced page-URL field in that text.
- Selection predicate: model proposes Search/Lookup terms; adapter selects page or case-insensitive paragraph matches and advances lookup index.
- Invalidation or expiry: a new successful search replaces document; failed search clears it. External page version is not pinned.
- Activation or effect: advisory observation text can shape next action; actual influence unobserved.
- Evidence limits: no network call performed; Wikipedia/library behavior, truth and current availability unverified.

> page_content = wikipedia.page(search).content
> url = wikipedia.page(search).url
> result: Union[str, Document] = Document(
>     page_content=page_content, metadata={"page": url}
> )
> --- `tasks/envs/utils.py`

> if isinstance(result, Document):
>     self.document = result
>     return self._sumary
> --- `tasks/envs/utils.py`

> def _sumary(self) -> str:
>     return self._paragraphs[0]
> --- `tasks/envs/utils.py`

No human per-passage approval, expected true passage or source-evaluation gate appears in these inspected adapter methods. This is evidence acquisition, not an acceptance decision on the encyclopedia's claims.

#### EPI-RTE-fever-check
Label: FEVER reference-label check

Part of: [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)

Distinct environment check within the action container, shared with other workflows. Owner/evaluator: `FeverEnv.success_fn` plus `match_exactly`; target: Finish argument against configured dataset answer, domain: normalized textual label equality. Model proposes; deterministic code decides; no per-answer human veto. Oracle is dataset `answer`, not model confidence or Wikipedia. Mode: bounded benchmark task. SRC-1, `tasks/envs/fever_env.py`, `tasks/envs/utils.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Finish gives CORRECT/reward 1/done True or INCORRECT/reward 0/done True.
- Later read-back: final feedback computes success from reward equal to one; label conditions later retention, comparison and rule credit.
- Delegated visibility: solving model can receive correctness observation; memory receives final label and feedback text.
- Selection predicate: lowercasing, punctuation/article removal and whitespace normalization followed by equality to reference.
- Invalidation or expiry: environment reset zeros reward; no revision to dataset oracle here.
- Activation or effect: enforces episode termination and changes success labeling; not a proof of evidence quality or causal reasoning.
- Evidence limits: reference correctness/split provenance not audited; label match supports only the configured task criterion.

> def success_fn(self, agent_ans: str) -> bool:
>     return match_exactly(agent_ans, self.config.get('answer'))
> --- `tasks/envs/fever_env.py`

> n_answer = normalize_answer(answer)
> n_key = normalize_answer(key)
> return n_answer == n_key
> --- `tasks/envs/utils.py`

> done = self.reward == 1
>
> return self.reward, done, feedback
> --- `tasks/envs/fever_env.py`

The source-supported countercase is an incorrect Finish: step `done` still terminates, but final feedback is failure. Continuation/termination is not acceptance, and the retained failure is not silently converted to success.

#### EPI-RTE-subgoal-check
Label: ScienceWorld observation-pattern completion

Part of: [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions)

Distinct environment evaluator inside the action container, also available to other workflows. Owner: Sciworld wrapper. Target: configured `selected_obs` patterns occurring in observations during the task. Evaluator: regex matches latched in `finished_sub_goal`, then all-completed count. Domain: textual observation-pattern completion, not arbitrary scientific claims. Environment supplies observations; config supplies patterns; model proposes actions; code decides with no per-action human approval. Mode: bounded benchmark task. SRC-1, `tasks/envs/sciworld_env.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: progress-based reward/done and final success or completed/uncompleted subgoal feedback.
- Later read-back: final label and feedback enter retained task context and maintenance sampling.
- Delegated visibility: model receives observations and final feedback through workflow; memory receives outcome.
- Selection predicate: each regex match sets corresponding completion flag; sum reaching pattern count is done.
- Invalidation or expiry: within-task flags latch; task reset establishes a new task's progress, not a truth revision process.
- Activation or effect: completion changes task continuation and success labeling, and can feed later rule survival.
- Evidence limits: pattern-to-goal fidelity and simulator truth are external/configuration assumptions; matches do not validate generalized causal principles.

> for i, pattern in enumerate(self.selected_obs):
>     match = re.search(pattern, obs)
>     if match:
>         self.finished_sub_goal[i] = 1.
> --- `tasks/envs/sciworld_env.py`

> def _check_is_done(self) -> bool:
>     return sum(self.finished_sub_goal) >= len(self.selected_obs)
> --- `tasks/envs/sciworld_env.py`

#### EPI-RTE-rule-disposition
Label: Rule syntax checks and mutation

Part of: [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)

Distinct parser/update phases within that container; ledger separates checking from disposition. Owner: InsightsManager. Endpoints: model operation text → regex/period/banned-word filter → local/global index mapping → duplicate/index rejection → ordered REMOVE/AGREE/EDIT/ADD mutation → pruning and JSON. SRC-1, `mas/memory/mas_memory/GMemory.py`, implementation. Target/domain: operation shape and addressable rule references, not rule truth. Model proposes and semantically judges; code admits/rejects within these predicates; no internal human approval. No answer oracle for correct generalized rules. Mode/trigger: sampled completed-task maintenance as specified in the parent.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parser operation list and mutated rule dictionaries; maintenance persists survivors.
- Later read-back: changed strings and associations enter later maintenance and solver prompts through parent route.
- Delegated visibility: proposer sees sampled histories and existing numbered rules; later solvers see selected text without the full proposal argument.
- Selection predicate: recognized operation shape, period-ending nonempty text, banned-word exclusion, index checks and substring duplicate checks; then positive score survival.
- Invalidation or expiry: EDIT replaces text; REMOVE subtracts score; pruning removes nonpositive scores. No versioned semantic rollback in these routines.
- Activation or effect: enforcing data mutation/admission, advisory effect through later natural-language prompts; activation unobserved.
- Evidence limits: operation checks do not test transfer, causal explanation, future task success or semantic faithfulness. Merge follows a different numbered-list path.

> if text != '' and not any([w in text for w in banned_words]) and text.endswith('.'):
> --- `mas/memory/mas_memory/GMemory.py`

> elif operation_type == 'AGREE':
>     rule_index: int = self._retrieve_rule_index(operation_rule_text)
>     rule_data: dict = self.insights_memory[rule_index]
>     rule_data['score'] += 1
> --- `mas/memory/mas_memory/GMemory.py`

> def _retrieve_rule_index(self, operation_rule_text: str) -> int:
>
>     for idx, insight in enumerate(self.insights_memory):
>         if insight['rule'] in operation_rule_text:
>             return idx
>     return -1
> --- `mas/memory/mas_memory/GMemory.py`

Countercase to an apparently complete index guarantee: AGREE passes numeric range checks but mutation resolves the target again from operation text by substring, not the supplied number. If no stored rule is contained in that text, `_retrieve_rule_index` explicitly returns -1. With a nonempty rule list admitted by the numeric check, Python negative indexing selects the last rule, increasing its score and adding positive task associations rather than failing with a None index. If another stored rule matches, that rule can be credited instead of the numbered target. Thus these are limited software checks, not a guarantee of intended-target resolution. A well-formed false rule ending in a period would face no truth test in these predicates; that is a conditional implementation assessment, not an observed false rule.

New rule/instruction admission is automatic. Guidance requests generalized causal criticism; what persists is rule text, score and associations, with prompts/responses logged separately. Rejection is syntactic/index/duplicate-based; recovery is not a transactional restoration of previous rule sets. The parent record supplies the independent theory-builder conditions 1–4, addressability, persistence, learning, reflection and autonomy assessment; this subroute's checks add no semantic acceptance or oracle to those findings.

### Claims

#### EPI-CLM-general-principles
Label: General causal principles from trials

Part of: [RT-CLM-evolving-memory](runtime.md#rt-clm-evolving-memory)

This is the maintenance-guidance claim within the broader adaptation claim, not its replacement. Claimed operation: extract causal, broadly applicable principles from success/failure examples. SRC-1, `mas/memory/mas_memory/prompt.py`, doctrine/design. Comparison to task outcomes supports candidate generation; it does not by itself establish that any generated explanation is causally identified or transfers.

> - Avoid vague statements; ensure each insight has a clear causal relationship.
> - Focus only on strategies that apply to a broad range of scenarios rather than case-specific advice.
> --- `mas/memory/mas_memory/prompt.py`

#### EPI-CLM-output-improvement
Label: Model judgment of MAS output improvement

No counterpart after comparison with supplied runtime claims: this names a distinct prompt-level evaluator claim, not hierarchical memory benefit. Claimed operation: classify whether final MAS output improves on initial agent outputs; target is relative output quality, domain/criterion unspecified beyond that wording. SRC-1, `mas/memory/mas_memory/prompt.py`, doctrine/design. Direct search for `analyze_mas_pattern` across `mas/` and `tasks/` at the frozen revision found only prompt definitions and GMemoryPrompt attribute exposure; no caller or consequential consumer was found there. No implementation-level negative beyond this search boundary is asserted.

> Given the initial outputs from several agents and the final output produced by the MAS, your task is to determine whether the MAS output shows any **improvement** over the initial agent outputs.
> --- `mas/memory/mas_memory/prompt.py`

> If there is an improvement, respond with: True
> If there is no improvement, respond with: False
> --- `mas/memory/mas_memory/prompt.py`
