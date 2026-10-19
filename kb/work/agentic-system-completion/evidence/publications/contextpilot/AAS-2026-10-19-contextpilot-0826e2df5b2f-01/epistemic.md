---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ContextPilot epistemic routes: document evidence, unverified context replacement, answer evaluation and reward-driven policy updates."
run-id: AAS-2026-10-19-contextpilot-0826e2df5b2f-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot epistemic report

## Source-and-claim boundary

The question is whether ContextPilot's document-QA, memory and training routes establish warrant for content, rather than merely making it available for use. Scope, exclusions, immutable identity and evidence layers are those of [boundary](boundary.md#boundary-and-evidence); sources resolve through its [Source register](boundary.md#source-register). All direct inspection below is SRC-1 implementation unless explicitly identified as doctrine/design or reported operation. No target execution occurred. The supplied runtime is provisional implementation evidence, not an execution trace.

The knowledge-related design and outcome claims are [EPI-CLM-context-management](#epi-clm-context-management), [EPI-CLM-performance-results](#epi-clm-performance-results), and [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls). The design promises evidence-oriented context management, not a formal truth oracle. Structured memory and review must nevertheless be distinguished from evidence-consuming acceptance.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| FSM and base inference dispatch; retry; finish extraction | `infer/src/contextpilot_fsm.py`, `infer/src/hf_test_runner.py` | Supplied [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-RTE-base-inference](runtime.md#rt-rte-base-inference), [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls) | Not directly reread here; no observed compliance or universal oracle isolation. |
| Configured tool surface and maintenance instructions | `infer/tools/context-shaper_tools.json`, `infer/configs/fsm_plan_bm25_mc_prompt.txt` | Direct full reads; [EPI-CLM-context-management](#epi-clm-context-management) | Requests do not prove model reasoning or execution. |
| Read/search; note/memory mutation and related selection; merge; context dispatch and compressor | `infer/src/contextpilot.py` | Direct selected function reads; [EPI-RTE-memory-merge](#epi-rte-memory-merge), [EPI-OBJ-memory-content](#epi-obj-memory-content), supplied [RT-RTE-context-edit](runtime.md#rt-rte-context-edit) | Optional semantic/hybrid search and detailed chunk construction not directly assessed; no system-complete negative about all checks. |
| All exposed scoring CLI operations and task scorer dispatch | `infer/src/hf_score_fns.py`, `infer/scripts/eval_task.sh` | Direct reads of choice, LongMemEval, BrowseComp+ and Fire dispatch; [EPI-RTE-choice-evaluation](#epi-rte-choice-evaluation), [EPI-RTE-longmemeval-evaluation](#epi-rte-longmemeval-evaluation), [EPI-RTE-browsecomp-evaluation](#epi-rte-browsecomp-evaluation) | Transport helpers/provider internals uninspected; no judge reliability conclusion. |
| Training memory handlers and terminal scorer | `train/verl/tools/statelm_tools.py`, `train/verl/utils/reward_score/statelm_qa.py` | Direct selected memory handlers and full scorer; [EPI-RTE-terminal-evaluation](#epi-rte-terminal-evaluation) | Structured training store internals supplied by runtime, not independently audited here. |
| Training branches, snapshot rewards, actor update, checkpoints | `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py` | Supplied [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), [RT-RTE-actor-update](runtime.md#rt-rte-actor-update) | Optimizer, synchronization and production export unresolved; no end-to-end trained-successor deployment conclusion. |
| Public design/results | `README.md` | Direct full read; both EPI claim records | Attributed results only, no inspected comparison or causal experiment. |

Missing benchmark payloads prevent audits of reference truth and reproduction. Missing model versions/weights prevent identifying parametric propositions and their provenance. Missing run artifacts prevent activation and achieved-quality conclusions. Missing controlled comparisons prevent assigning an outcome effect to memory, planning, compression or branch credit. These are separate from available but uninspected optional implementations; see boundary for external service and dataset limits. No supplied fact needs supersession: scorer and merge findings below extend runtime's selected routes rather than contradicting them.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-document-evidence](#epi-obj-document-evidence) | see record | see record | see record | Source warrant unknown; delivery is not endorsement. |
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | see record | see record | see record | Model-authored content may omit qualifiers or be wrong. |
| [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks) | see record | see record | see record | Symbolic masks are not truth claims; replacement text may be. |
| [RT-OBJ-full-history](runtime.md#rt-obj-full-history) | see record | see record | see record | Contains plans and answer candidates; no instantiated run supplied. |
| [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation) | see record | see record | see record | Reference-relative correctness is not evidence for every intermediate assertion. |
| [RT-CMP-actor-model](runtime.md#rt-cmp-actor-model) | not determinable | see record | see record | Accessible code cannot individuate propositions in weights. |
| [RT-CMP-judge-model](runtime.md#rt-cmp-judge-model) | not determinable | see record | see record | Judge behavior/version unobserved. |
| [RT-CMP-compression-model](runtime.md#rt-cmp-compression-model) | not determinable | see record | see record | Output semantic fidelity unverified. |
| [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) | not determinable | see record | see record | Ranking features are not a truth oracle. |

## Authority-route ledger

Each compact row gives this report's assessment; record-owned implementation and evidence fields are reached with `see`. Repeated citations split a route's consequential functions, not its identity. No route below is asserted observed.

Route ID: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document-evidence](#epi-obj-document-evidence)
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown.
Transition or check target: supplied document to selected evidence in model context.
Evaluator/condition and domain: selection, not truth evaluation; see route and object.
Activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: imported text has only its source's unresolved warrant; retrieval rank does not certify it.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see route and object.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: selected chunks/highlights do not establish exhaustive search, especially for counts or chronology.

Route ID: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: no content change at admission; preceding model generation is truth-apt transformation: indeterminate.
Transition or check target: admission of proposed facts, summaries and structured fields to a keyed store.
Evaluator/condition and domain: see route and object; structural validity/key/mode checks, not documentary truth.
Activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: operational write acceptance only; no evidenced semantic acceptance criterion for these entries.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see object and route.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none; retention is not epistemic acceptance.
Gap/limit: generated entries could be faithful extraction, inference or error. No instances establish entailment or non-entailment.

Route ID: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: no content change for storage/read; append/overwrite can change content as described in the object.
Transition or check target: saved entries to later inventories and explicit reads.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route and object.
Epistemic authority and scope: retained candidate, not an accepted claim.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see object and route.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: deletion changes future availability, not a recorded evidence-based withdrawal; no cross-sample knowledge reload established.

Route ID: [EPI-RTE-memory-merge](#epi-rte-memory-merge)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping for concatenated bodies; supplied replacement summary is truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: no additional warrant; structured provenance is degraded.
Operational authority and behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: configured optional handler, not in the shipped default tool JSON; no exercised merge inferred.

Route ID: [RT-RTE-context-edit](runtime.md#rt-rte-context-edit)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks)
Content/update relation: truth-apt transformation: indeterminate for model-authored manual summaries.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route and [EPI-OBJ-memory-content](#epi-obj-memory-content) for the concrete transformation witness.
Epistemic authority and scope: no semantic fidelity license; a substring or sampled word sequence can lose a negation or condition.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see route and object witness.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: failure to establish entailment is not evidence that every output is an ampliative conjecture.

Route ID: [RT-RTE-context-edit](runtime.md#rt-rte-context-edit)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks)
Content/update relation: truth-apt transformation: indeterminate for compression output where truth-apt; empty output carries no proposition.
Transition or check target: selected message to remote compressor output, or sampled words on exception.
Evaluator/condition and domain: compressor request is not fidelity evaluation. Exception triggers fallback; rate/count rules constrain word retention, not truth.
Activation and timing; possible or observed result; implemented force: see route and [RT-CMP-compression-model](runtime.md#rt-cmp-compression-model).
Epistemic authority and scope: neither remote output nor fallback is checked for preservation of meaning.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see route and [EPI-OBJ-memory-content](#epi-obj-memory-content) for the zero-rate witness.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: fallback success is operational replacement, not a certificate that evidence survived.

Route ID: [RT-RTE-context-edit](runtime.md#rt-rte-context-edit)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks)
Content/update relation: truth-apt transformation: non-ampliative reshaping for deterministic span extraction.
Transition or check target: selected message to a contiguous substring with truncation wrapper.
Evaluator/condition and domain: boundary-string occurrence, not semantic equivalence; see [EPI-OBJ-memory-content](#epi-obj-memory-content) for the concrete witness.
Activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: retained substring only; removed context can change interpretation.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see route and witness.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: preservation of bytes in a span does not preserve every qualified proposition.

Route ID: [RT-RTE-context-edit](runtime.md#rt-rte-context-edit)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks)
Content/update relation: no content change to backing history; restored visibility changes reliance opportunities.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: restoration recovers original evidence, not its truth; masks do not mark evidence-based rejection.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls).
Mismatch marker: none.
Gap/limit: automatic pruning and explicit restoration differ; not all hidden history has an admitted restore path.

Route ID: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-RTE-base-inference](runtime.md#rt-rte-base-inference)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-full-history](runtime.md#rt-obj-full-history)
Content/update relation: no content change by tool-state admission; model plans/answers remain truth-apt transformation: indeterminate where truth-apt.
Transition or check target: next tool, review and finish; not the truth of a proposed answer.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see routes and [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls).
Epistemic authority and scope: protocol continuation, not evidence-consuming answer acceptance. The review instruction asks relevant checking; a successful read alone proves none.
Operational authority and behavioral-authority path: see routes and [RT-BAP-context-policy](runtime.md#rt-bap-context-policy).
Evidence source ID and local anchor: see routes.
Claim IDs: [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls).
Mismatch marker: conditional enforcement; base dispatch, fallback schemas, synthetic review and incomplete-run extraction defeat an unconditional review claim.
Gap/limit: opaque model processing could compare evidence; neither presence nor absence of such reasoning is established.

Route ID: [EPI-RTE-choice-evaluation](#epi-rte-choice-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation)
Content/update relation: truth-apt transformation: entailed derivation for rule-defined labels/aggregates.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: heuristic reference-label agreement only, not document truth or valid explanation.
Operational authority and behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-performance-results](#epi-clm-performance-results).
Mismatch marker: none.
Gap/limit: ambiguous-answer false-positive witness limits correctness interpretation.

Route ID: [EPI-RTE-longmemeval-evaluation](#epi-rte-longmemeval-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation)
Content/update relation: truth-apt transformation: indeterminate for judge verdict; aggregate arithmetic is entailed derivation within parsed-label domain.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: task-specific reference/rubric agreement, including temporal tolerance, not independent source truth.
Operational authority and behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-performance-results](#epi-clm-performance-results).
Mismatch marker: none.
Gap/limit: judge/reference reliability unknown; parse failures enter denominator as false.

Route ID: [EPI-RTE-browsecomp-evaluation](#epi-rte-browsecomp-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation)
Content/update relation: truth-apt transformation: indeterminate for judge verdict; aggregate arithmetic is entailed derivation within valid-label domain.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: reference equivalence under the judge prompt, not independent solution verification.
Operational authority and behavioral-authority path; evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-performance-results](#epi-clm-performance-results).
Mismatch marker: none.
Gap/limit: judge/reference reliability unknown; unparsed verdicts excluded rather than rejected as incorrect.

Route ID: [EPI-RTE-terminal-evaluation](#epi-rte-terminal-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation)
Content/update relation: truth-apt transformation: entailed derivation for deterministic scoring arithmetic; open-ended judgment is truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: terminal reference-relative correctness and format, not truth of every snapshot, memory relation or action explanation.
Operational authority and behavioral-authority path: see [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor).
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: model failure can substitute exact-string comparison, changing the effective evaluator rather than providing semantic rejection evidence.

Route ID: [RT-RTE-actor-update](runtime.md#rt-rte-actor-update)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation)
Content/update relation: no content change at training-row selection; descendant averaging is numerical credit computation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: training-row admission, not acceptance of an intermediate truth-apt claim. A correct descendant answer need not vindicate each ancestor's fact or mechanism.
Operational authority and behavioral-authority path: see [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor).
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-context-management](#epi-clm-context-management).
Mismatch marker: none.
Gap/limit: no descendant terminals causes a drop; no per-content human approval or validation-score veto established.

Route ID: [RT-RTE-actor-update](runtime.md#rt-rte-actor-update)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-CMP-actor-model](runtime.md#rt-cmp-actor-model)
Content/update relation: non-truth-apt policy/content update: numerical policy optimization; particular propositions in weights not determinable.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: no claim-level acceptance or warranted premises licensed by actor optimization.
Operational authority and behavioral-authority path: see [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor).
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-performance-results](#epi-clm-performance-results).
Mismatch marker: none.
Gap/limit: update wiring and checkpoint reload are supported; exercised dependence and improved capacity are not.

Route ID: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)
Route function: lifecycle integration
Architectural status: no route found within boundary
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: no content change established for post-acceptance integration.
Transition or check target: accepted memory claim to evidence-connected organization/use.
Evaluator/condition and domain: no semantic acceptance phase found in the inspected inference write/read/update/merge functions.
Activation and timing; possible or observed result; implemented force: inapplicable here; storage, indexing and later delivery are separately implemented above.
Epistemic authority and scope: no post-acceptance status can be assigned to these writes.
Operational authority and behavioral-authority path: see [RT-BAP-context-policy](runtime.md#rt-bap-context-policy) for pre-acceptance use, not lifecycle integration.
Evidence source ID and local anchor: see [EPI-OBJ-memory-content](#epi-obj-memory-content) and [EPI-RTE-memory-merge](#epi-rte-memory-merge).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: bounded to those inspected handlers; optional uninspected routes and opaque model reasoning prevent a system-wide absence claim.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-context-management](#epi-clm-context-management) | see record | see record | see record | see [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-RTE-context-edit](runtime.md#rt-rte-context-edit), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), [RT-RTE-actor-update](runtime.md#rt-rte-actor-update) | none supplied | Terminal outcomes do not isolate an intermediate edit's causal effect. | Context management and reward assignment are wired. | Planning is model-authored; structured memory is not verified knowledge; long-term wording does not establish cross-task reuse. |
| [EPI-CLM-performance-results](#epi-clm-performance-results) | see record | see record | see record | see evaluator records and [RT-RTE-actor-update](runtime.md#rt-rte-actor-update) | attributed report only | No inspected comparison design/results; component effects unestablished. | A public performance claim and evaluation machinery exist. | Actual superiority and context/accuracy tradeoff unverified. |
| [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls) | see record | see record | see record | see record | none supplied | Protocol completion is not semantic fidelity. | Conditional operational control. | See record's alternate routes and recovery qualifications. |

## Bounded conclusion

ContextPilot acquires selected document content and gives model-written summaries, facts and answers consequential use. Retrieval preserves some local chunk identity, but imported source truth is unknown. Keyed storage and optional related-memory ranking supply retention and selection rather than semantic endorsement. Merge can discard structured provenance even while preserving concatenated text. Context restoration recovers visible evidence without certifying it. See [EPI-OBJ-document-evidence](#epi-obj-document-evidence), [EPI-OBJ-memory-content](#epi-obj-memory-content), [EPI-RTE-memory-merge](#epi-rte-memory-merge), and [RT-RTE-context-edit](runtime.md#rt-rte-context-edit).

The inspected content handlers provide no evidence-consuming acceptance decision naming a criterion, intended use and scope for retained facts. Their operational admission licenses later prompt delivery within the sample, not truth. Model-authored summaries and answers remain candidates with indeterminate transformation relations; absence of instantiated outputs prevents deciding extraction versus derivation versus conjecture. There is no established derivation of domain knowledge from independently warranted premises. Rule-defined scorer outputs can be deduced from code and inputs, but their correctness labels have only the matcher/rubric's domain. See [RT-RTE-document-qa](runtime.md#rt-rte-document-qa) and [EPI-OBJ-answer-evaluation](#epi-obj-answer-evaluation).

The offline evaluators consume references for benchmark reporting. Their score artifacts do not implement answer rollback, memory acceptance or automatic revision of the QA episode. Training evaluations differ: terminal reference comparison and penalties feed descendant credit, row selection and actor updates. That is an operative computational authority path across training steps/checkpoint resume, not a claim-level acceptance or theory-criticism path. See the EPI evaluator records and [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor).

Parametric state is accessible only through configuration and update calls. Propositions inside it are not determinable; actor, judge, compressor and embedding-provider fixity remain independently bounded by the runtime component records. Learning benefit, exercised self-improvement and component attribution are unobserved. Reward-responsive policy-update capacity remains supported independently of those missing outcomes. Planning requests self-assessment, but a plan success result is not evidence of content-directed criticism, repeated theory revision or exercised reflection. Neither opacity nor an answer score establishes those properties. See [RT-RTE-actor-update](runtime.md#rt-rte-actor-update), [RT-CMP-actor-model](runtime.md#rt-cmp-actor-model), and [EPI-CLM-context-management](#epi-clm-context-management). These route-specific conclusions yield no single epistemic score or unqualified system-wide verdict.

## Shared records

### Operative objects

#### EPI-OBJ-document-evidence
Label: Selected document chunks and highlights

Part of: [RT-OBJ-full-history](runtime.md#rt-obj-full-history)

This is the imported evidence-text part of history, not the entire message store. Natural-language document passages are carried in symbolic chunk/result envelopes, stored in the local index and tool-history entries. `readChunk` uses a model-supplied ID or sequential scan; multi-read caps honored IDs. `searchEngine` filters by active document ID and returns ranked highlights and chunk IDs, not all matching document text. Owner is ToolLibrary. External source warrant is unknown; relevance score concerns query match, not truth. Direct SRC-1 implementation: `infer/src/contextpilot.py`. Closest supplied route is [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), whose broad invocation contains this evidence delivery.

> return {"retrieved_chunk": [self.index[chunk_id]], "chunk_id": chunk_id}
> --- `infer/src/contextpilot.py`

> items.sort(key=lambda x: x["relevance_score"], reverse=True)
> --- `infer/src/contextpilot.py`

#### EPI-OBJ-memory-content
Label: Memory and note content

Natural-language `summary`, `full_content`, entities and episodes coexist with symbolic keys, relation dictionaries and model-supplied source IDs in StateManager dictionaries. Simple notes lack structured provenance. This retained backing-store object is distinct from [RT-OBJ-full-history](runtime.md#rt-obj-full-history) and [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks), though their payloads can contain copies. It is consumed through inventories and read results by [RT-BAP-context-policy](runtime.md#rt-bap-context-policy). The closest route [RT-RTE-document-qa](runtime.md#rt-rte-document-qa) describes the containing invocation, not this store's identity.

Direct SRC-1 implementation in `infer/src/contextpilot.py`: add replaces the keyed entry and reindexes it; read returns a deep copy plus related-memory summaries; update checks existence/mode/content, permits append/overwrite/delete and rebuilds or removes graph edges. These checks never compare proposed content to the cited chunks. Source fields record model assertions of provenance, not verified entailment. The relation scorer uses shared entities, times, facets, explicit connections and optional vector similarity. It ranks candidate neighbors rather than judging their truth. Training memory handlers likewise delegate proposed structured content or directly write simple notes (SRC-1, `train/verl/tools/statelm_tools.py`); deeper training-store semantics are not independently assessed here.

> self.notes[k] = self._build_memory(key, content, summary, entities, episodes, relations, source)
> --- `infer/src/contextpilot.py`

> self.simple_notes[str(key)] = {"summary": str(summary), "full_content": str(content)}
> --- `infer/src/contextpilot.py`

> related.sort(key=lambda item: item["score"], reverse=True)
> --- `infer/src/contextpilot.py`

Context replacements are a separate part owned by [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks), not this store. A concrete deterministic witness bounds their warrant: for an assistant text `not true`, truncate boundaries `true` and an absent later stop return an error; for `not true end`, boundaries `true`/`end` keep `true end` and drop `not`. This follows first-substring selection without executing the target. At compression rate zero, `not true` becomes an empty body; the success wrapper still replaces the visible message. Positive-rate random fallback can also omit qualifiers. Thus mechanical extraction/compression does not check semantic preservation. SRC-1 implementation, `infer/src/contextpilot.py`:

> truncated = text[start_idx:stop_idx + len(stop_sentence)]
> --- `infer/src/contextpilot.py`

> if not words or compression_rate <= 0:
>     return ""
> --- `infer/src/contextpilot.py`

#### EPI-OBJ-answer-evaluation
Label: Answer candidates and evaluation artifacts

Natural-language answer strings and reference answers are compared by symbolic matchers or external model interpretation. Boolean labels, parse flags and scalar rewards are symbolic objects in Python dictionaries/numbers and serialized output files. This object spans final-answer portions of [RT-OBJ-full-history](runtime.md#rt-obj-full-history) and downstream scoring outputs; it is not part of exactly one supplied object. It differs from the actor/judge parameters in [RT-CMP-actor-model](runtime.md#rt-cmp-actor-model) and [RT-CMP-judge-model](runtime.md#rt-cmp-judge-model). References are supplied benchmark/training inputs, not discovered truths. Evidence is SRC-1 `infer/src/hf_score_fns.py` and `train/verl/utils/reward_score/statelm_qa.py`; the route records below supply passages and distinguish report versus update consumers.

### Routes

#### EPI-RTE-memory-merge
Label: Optional memory merge

Part of: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)

An additional configurable ToolLibrary operation omitted from the runtime's selected detail: `mergeNotes` delegates to StateManager `merge_notes`. It merges structured-memory `notes`, not `simple_notes`, despite the tool name. Python decides which requested keys exist; missing keys are skipped. Existing selected entries and graph links are removed before one new entry is written. The model/caller supplies keys and optional replacement summary; there is no human per-content approval, truth check or merge-specific rollback. The new entry keeps only summary/full_content, losing structured sources/entities/episodes/relations. This is not lifecycle integration after acceptance. SRC-1 implementation: `infer/src/contextpilot.py`; default schema absence checked in full `infer/tools/context-shaper_tools.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success/new key/merged-from keys, or no-notes error.
- Later read-back: Inventories and keyed reads can deliver merged content to subsequent QA turns.
- Delegated visibility: Policy model receives resulting inventory/read text; no independent merger evaluator.
- Selection predicate: Requested existing keys; optional new_key/new_summary, otherwise joined keys/summaries.
- Invalidation or expiry: Selected old entries and graph links deleted; per-agent lifetime bounds new entry. No transactional recovery established.
- Activation or effect: Direct local store replacement changes subsequent available text; exercised behavioral dependence unobserved.
- Evidence limits: Reachable through configurable dispatch, absent from shipped default schema; no observed invocation.

A concrete deduction: entries with bodies `rain` and `wind` and source IDs become a body `rain\nwind`; with no new summary the summaries are joined, but source IDs are not copied into the new dictionary. Body concatenation is non-ampliative reshaping; metadata lineage degrades. A supplied new summary has no semantic check and is indeterminate. A pre-existing new_key can be overwritten by the final assignment. Behavioral-authority path: policy model, inventory/read text, advisory evidence, later turns of this sample.

> merged_content = "\n".join([note[2] for note in notes_to_merge])
>
> self.notes[merged_key] = {"summary": str(existing_summary), "full_content": str(merged_content)}
> --- `infer/src/contextpilot.py`

#### EPI-RTE-choice-evaluation
Label: Choice-file evaluation

Distinct from the inference invocation [RT-RTE-document-qa](runtime.md#rt-rte-document-qa): a post-generation CLI/file consumer. SRC-1 implementation `infer/src/hf_score_fns.py` exposes both `score_choice_file` and `evaluate_choice_file`; `infer/scripts/eval_task.sh` selects the latter for InfBench/NovelQA. The deterministic evaluator consumes prediction and label, handling lists, last isolated option, first character, substring and prefix heuristics. The named target/domain is answer-label matching, not document entailment. The benchmark supplies the answer oracle; the operator selects files and matcher keys, not individual verdicts. No human veto or QA continuation consumer is wired here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed correctness/aggregate counts and optional score file; evaluate also rewrites rows with correct_list.
- Later read-back: uninspected — artifacts persist but no later policy reload/revision consumer was established.
- Delegated visibility: inapplicable — local Python matching, no provider call.
- Selection predicate: All loaded rows, selected prediction/label fields; missing values default empty.
- Invalidation or expiry: Evaluate overwrites input JSONL; score output is overwritten. No semantic withdrawal lifecycle.
- Activation or effect: Artifact annotations and aggregate score, not acceptance of retained memory or blocking answer publication.
- Evidence limits: Heuristic agreement with a supplied label; no proof of reference truth or model process.

Counterexample to treating this as strict option correctness: for prediction `B or A` and label `A`, the final isolated-option regex selects `A` and returns true despite the ambiguous response. This is code deduction, not target execution. Rule-defined result is entailed within the matcher domain; the stronger claim that ambiguity was resolved correctly is not. Its authority path is matcher result to JSONL/report writers, computational labeling, this evaluation batch only.

> match = re.search(r"\b[A-D]\b(?!.*\b[A-D]\b)", prediction)
> if match and match.group(0) in label:
>     return True
> --- `infer/src/hf_score_fns.py`

> row[output_key] = [bool(score)]
> --- `infer/src/hf_score_fns.py`

#### EPI-RTE-longmemeval-evaluation
Label: LongMemEval evaluation

No same referent in supplied runtime; this is a separate post-generation evaluator. SRC-1 implementation `infer/src/hf_score_fns.py` and task dispatch `infer/scripts/eval_task.sh`. Target is reference-relative answer correctness, with task-specific criteria: coverage/equivalence, off-by-one temporal tolerance, updated-answer allowance, preference rubric, or unanswerability recognition. Reference records supply oracle inputs; the model proposes the verdict and local parsing decides the stored label. The operator supplies endpoint/data and may defer judging; no per-answer human approval is implemented. External judge exact version/mutability follows endpoint configuration, not a pinned weight identity; scorer calls do not update its parameters and provider internals are uninspected. This is a separately configured consumer from the training judge component.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Annotated JSONL with label, reasoning, matched_span and parse_error plus aggregate/per-task reports.
- Later read-back: uninspected — persisted reports have no inspected QA revision or training-update consumer.
- Delegated visibility: External endpoint receives question, reference/rubric and model response.
- Selection predicate: Predictions with matching question_id; max_samples may limit input. Abstention determined by _abs in ID.
- Invalidation or expiry: Output/report overwrites; missing reference IDs are skipped, not scored false.
- Activation or effect: Parsed labels are counted into benchmark aggregates; parse failure defaults false and remains in denominator.
- Evidence limits: Requested semantic evaluation, not verified judge reliability; permissive parsing may accept final yes/no token or an invalid typed label as false without a parse-error flag.

The result's license is this rubric and selected dataset subset, not universal factual accuracy. No answer rejection/revision follows from a negative label in this route. Behavioral-authority path: judge response to local parser to report writer, computational scoring, one evaluation batch. Contrast with BrowseComp+ denominator handling below.

> result["parse_error"] = True
> return result
> --- `infer/src/hf_score_fns.py:418-419`

> counts[reference["question_type"]].append(int(label))
> --- `infer/src/hf_score_fns.py`

#### EPI-RTE-browsecomp-evaluation
Label: BrowseComp+ evaluation

Distinct from the supplied runtime routes and from LongMemEval's rubric/parser. SRC-1 implementation `infer/src/hf_score_fns.py`, dispatch `infer/scripts/eval_task.sh`. Target is semantic equivalence of extracted final answer to supplied reference, allowing greater precision and a small numerical margin. The external model receives instructions not to solve the question or challenge the reference. Local parser extracts verdict and confidence; confidence is not used as an admission threshold. External endpoint weights are unpinned, potentially mutable, not updated by this caller; provider internals remain uninspected.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Annotated JSONL with prompt/response/verdict/extracted answer/reasoning/confidence/parse flag and aggregate score report.
- Later read-back: uninspected — no subsequent answer or memory revision consumer established.
- Delegated visibility: Model service receives question, answer candidate and reference.
- Selection predicate: Matching query IDs only; only parsed verdicts enter aggregate denominator.
- Invalidation or expiry: Output/report overwrites; unparsed responses stay annotated but are excluded from aggregate, not treated as incorrect.
- Activation or effect: Parsed correctness controls aggregate counts; confidence is retained without weighting the score.
- Evidence limits: Model semantic judgment against unverified reference; exact judge version and actual reliability unobserved.

Humans supply benchmark/configuration; model judges and Python determines parsing/selection, without per-verdict human veto. This bounded benchmark mode does not change the QA episode. Behavioral-authority path: parsed verdict to aggregate writer, computational reporting, evaluation batch.

> valid = [row["autoeval_judge"] for row in scored_rows if not row["autoeval_judge"]["parse_error"]]
> correct = sum(bool(row["correct"]) for row in valid)
> score = correct / len(valid) if valid else 0.0
> --- `infer/src/hf_score_fns.py`

#### EPI-RTE-terminal-evaluation
Label: Training terminal QA evaluation

Part of: [RT-RTE-actor-update](runtime.md#rt-rte-actor-update)

This is its terminal check subroute, not snapshot-row admission or policy optimization. Owner is `compute_score`, SRC-1 implementation `train/verl/utils/reward_score/statelm_qa.py`. Target/domain: finish-answer reference agreement and format in bounded training/validation samples. It extracts the first tool call after the last literal `assistant`, requires finish plus answer, and recognizes MCQ by reference being one character A–D. MCQ permits exact stripped prediction or a reference-letter-dot prefix. Open answers use the model comparison prompt; exceptions can substitute normalized exact equality. A reference is an oracle input, not supplied by model judgment alone. Format penalty can lower even a correct response's score; trajectory execution/budget penalty is separate in the containing runtime route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numerical outcome plus format score; not a validated set of intermediate propositions.
- Later read-back: Descendant credit, advantages and actor updates consume this score through the containing route.
- Delegated visibility: Open-answer judge sees question/reference/prediction; MCQ path is local and bypasses judge.
- Selection predicate: Parsed valid finish required for positive correctness; ground-truth shape chooses evaluator. Format metadata controls penalty.
- Invalidation or expiry: Recomputed per response; model errors can fall back to exact-string comparison rather than veto training. No semantic rollback criterion.
- Activation or effect: Numerical score reaches training-credit/update machinery; exercised parameter/behavior changes unobserved.
- Evidence limits: Cannot attribute descendant success to each context edit or establish truth of retained facts. Reference accuracy and judge reliability unverified.

Model proposes answers; Python and optional external judge decide score. Humans select data/configuration, not each answer's admission. Guidance is the reference comparison prompt and fixed scoring rules; persisted products are training signals and, via the parent route, parameters/checkpoints. There is no separate evidence-consuming acceptance of an explanatory claim. Behavioral-authority path is [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor); component fixity is [RT-CMP-judge-model](runtime.md#rt-cmp-judge-model).

> (predicted.strip() == ground_truth) or (predicted.strip().startswith(f"{ground_truth}."))
> --- `train/verl/utils/reward_score/statelm_qa.py`

> pred_normalized = prediction.lower().strip()
> gt_normalized = ground_truth.lower().strip()
> return pred_normalized == gt_normalized
> --- `train/verl/utils/reward_score/statelm_qa.py:152-154`

> r_out = 1.0 if is_correct else 0.0
> r_fmt = -0.5 if had_format_violation else 0.0
> score = r_out + r_fmt
> --- `train/verl/utils/reward_score/statelm_qa.py`

### Claims

#### EPI-CLM-context-management
Label: Planning memory and partial-rollout design

SRC-1 doctrine/design `README.md` claims planning, structured memory, soft offloading and branch-outcome credit for intermediate snapshots. Distinct from [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls), which concerns legal-tool ordering. The maintenance prompt requests evidence gathering, preservation of directional/temporal qualifiers, count deduplication and review; those are epistemic instructions rather than an independent evaluator. Direct reads in `infer/configs/fsm_plan_bm25_mc_prompt.txt` and `infer/tools/context-shaper_tools.json` establish guidance, not compliance. Plan execution only validates model-authored text; [RT-RTE-document-qa](runtime.md#rt-rte-document-qa) supplies the broader mechanism.

> ContextPilot extends context management with planning, structured memory, and
> soft context offloading. Its context-aware partial rollout focuses exploration
> on sensitive context-editing decisions, while fine-grained credit assignment
> trains intermediate snapshots using the outcomes of their downstream
> branches.
> --- `README.md`

> 8. Continue searching, reading, memorizing, cleaning, and reviewing until the evidence is sufficient; then call `finish` with a concise answer grounded in the document.
> --- `infer/configs/fsm_plan_bm25_mc_prompt.txt`

> The tool itself does
> NOT produce any planning text — it just validates the argument and
> returns a short success message so the pipeline can advance.
> --- `infer/src/contextpilot.py`

#### EPI-CLM-performance-results
Label: Stronger performance with compact context

SRC-1 `README.md`, reported operation, not an inspected experimental source. This distinct outcome claim has no supplied runtime claim counterpart; [RT-RTE-actor-update](runtime.md#rt-rte-actor-update) supports wiring but explicitly leaves benefit uninspected. No frozen comparison table, execution traces or intervention design was supplied. Evaluation implementations alone do not verify superiority or component effects.

> Experiments on long-context QA and deep search tasks show that ContextPilot
> achieves stronger performance with a more compact working context,
> outperforming existing baselines across various base models and benchmarks.
> --- `README.md`
