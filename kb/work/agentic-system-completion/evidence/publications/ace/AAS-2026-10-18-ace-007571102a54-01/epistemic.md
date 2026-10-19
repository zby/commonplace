---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ACE epistemic routes: answer matching, model-generated lessons, playbook admission and later reliance at the frozen main-repository revision."
run-id: AAS-2026-10-18-ace-007571102a54-01
reviewed-boundary: "82709de050e1db6e6ef2f07bcb0393560b94992a"
---

# ACE epistemic report

## Source-and-claim boundary

The question is how ACE turns task experience into content used on later tasks, and what its checks license. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). The main repository supplies implementation and doctrine/design, plus attributed performance reports, not inspected runs or causal experiments. AppWorld is unavailable. No source, test, example or model call was executed.

The assessment distinguishes matching a dataset answer, diagnosing why it matched, proposing a reusable lesson, admitting text, and using that text. These are not one acceptance event. Public claims include [RT-CLM-context-improvement](runtime.md#rt-clm-context-improvement) and [EPI-CLM-context-quality](#epi-clm-context-quality).

### Coverage

Direct reads below supplement, rather than silently reproduce, the supplied runtime account. SRC-1 supplies all paths. Searches checked tracked Python entry points, function definitions and packaging against the runtime; they found no packaged CLI script registration in `pyproject.toml`. The shipped invocation surface is the three run scripts and public Python methods described by the runtime, not a provider tool registry. No system-complete negative is asserted.

| Entry point or operation | Source path | Coverage and records / conclusion prevented |
|---|---|---|
| Sequential training, run modes, regeneration and online windows | `ace/ace.py` | Supplied findings: [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-online-windows](runtime.md#rt-rte-online-windows). Scheduling and target-derived feedback taken from these records, not independently reread here. |
| Batch training, grouped proposals, reducer, rollback | `ace/ace_batch.py` | Supplied findings: [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation). Direct reducer prompt and curator parser reads; [EPI-RTE-curator-admission](#epi-rte-curator-admission). |
| Finance and both Mind2Web CLI callers, eval_only/test, reload | `eval/finance/run.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`, `utils.py` | Entry-point search plus supplied [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select), [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload). No independent caller execution. |
| Generator/reflector context and bullet selection | `ace/core/generator.py`, `ace/core/reflector.py`, `ace/prompts/reflector.py`, `playbook_utils.py` | Generator supplied via [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation); reflector and bullet extraction directly read. [EPI-OBJ-reflection](#epi-obj-reflection), [EPI-RTE-counter-update](#epi-rte-counter-update). |
| Curator generation, schema, ADD consumer; proposal/reducer policy | `ace/core/curator.py`, `ace/prompts/curator.py`, `playbook_utils.py` | Direct sequential curate, parser/filter, prompt and deterministic application reads; proposal/reducer wiring additionally supplied by runtime. [EPI-RTE-curator-admission](#epi-rte-curator-admission). |
| Optional similarity grouping, merge, removal and failure fallback | `ace/core/bulletpoint_analyzer.py` | Direct merge/analyze read; embedding/grouping mechanics supplied by [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). |
| Finance and both Mind2Web answer evaluators | `eval/finance/data_processor.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py` | Direct scoring reads: [EPI-RTE-answer-match](#epi-rte-answer-match). Host-interpreter force also [RT-RTE-finer-scoring](runtime.md#rt-rte-finer-scoring). |
| Transport, logs, provider weights | `llm.py`, `logger.py`, `utils.py` | Supplied runtime findings. Logs do not feed later curation here. Remote model processing and actual weight identities uninspected; no internal learning conclusion. |
| Dataset preparation/provenance and extension documentation | `eval/mind2web/prepare_data.py`, `eval/mind2web2/prepare_data.py`, `EXTENDING_ACE.md`, `tutorials/ExtendingDatasets.md` | Available but not directly assessed. Prevents benchmark-construction validity and completeness of extension-contract conclusions; scoring conclusions are conditional on supplied standardized targets. |
| AppWorld integration | `ace-appworld` | Unavailable submodule, as boundary records; prevents full AppWorld feedback, admission and environment-effect conclusions. |
| Public claims and packaging | `README.md`, `pyproject.toml` | Direct relevant passages/package read; [EPI-CLM-context-quality](#epi-clm-context-quality). README reports do not supply inspectable comparison evidence. |

No supplied execution trace ties an actual candidate to generation, checking or acceptance. Thus implementation supports route capacity, not the semantic classification or acceptance history of a particular generated lesson. No supplied intervention separates reflector, curator, selection and other treatment effects. Missing provider internals prevent weight-update assessment, not assessment of the text-update path. Uninspected preparation remains a local limit, not evidence that targets are defective.

## Epistemic-object inventory

Fields owned by a declaring record are `see` that record. No operative objects were supplied in runtime; the following split content from metadata and current answer from proposed explanation.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-answer](#epi-obj-answer) | Dataset-relative answer propositions; action descriptions may instead be proposals | see record | SRC-1, `eval/finance/data_processor.py` | A matching answer does not establish correct reasoning or source truth. |
| [EPI-OBJ-reflection](#epi-obj-reflection) | Candidate error diagnoses, root causes, recommended principles | see record | SRC-1, `ace/prompts/reflector.py` | Requested fields, not an observed diagnosis or established cause. |
| [EPI-OBJ-playbook](#epi-obj-playbook) | Potential formulas, task regularities and strategies; also non-truth-apt instructions | see record | SRC-1, `ace/prompts/curator.py` | Actual generated content and source warrant not determinable. |
| [EPI-OBJ-bullet-tags](#epi-obj-bullet-tags) | Model utility judgments plus symbolic counts and identifiers | see record | SRC-1, `playbook_utils.py` | Counter truth is about processed tags, not independently measured usefulness. |

## Authority-route ledger

The same container record can support separate functions below; checking, disposition, retention and integration remain separate rows. All rows describe implemented possibilities, not observed events. `see` defers generic fields to their records. No route below licenses general truth or cross-task transfer merely from successful consumption.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload) | content transformation | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | truth-apt transformation: acquisition/import | Caller-supplied text enters playbook | Existing path and truthy content, not truth check | Explicit run initialization | Full text imported | Enforcing delivery | Source warrant unknown; no authentication or endorsement | Initializes context without curator gate | see record and [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance) | SRC-1, `eval/finance/run.py` | none | none | Imported content is acquired, not produced by ACE. |
| [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) | content transformation | implemented | [EPI-OBJ-answer](#epi-obj-answer) | truth-apt transformation: indeterminate | Task/context/playbook to answer | Generator model; requested task reasoning | Each generation; see record | Candidate answer/trace and reported IDs | Candidate supply | No warrant before task check | Makes answer available for scoring | Processor consumes extracted answer; enforcing branch input; current sample | SRC-1, `ace/core/generator.py` | [RT-CLM-context-improvement](runtime.md#rt-clm-context-improvement) | none | Could copy, derive or conjecture; actual output needed to distinguish. |
| [EPI-RTE-answer-match](#epi-rte-answer-match) | check/evidence production | implemented | [EPI-OBJ-answer](#epi-obj-answer) | no content change | Extracted answer versus dataset target | Task processor, restricted matching domain; see record | Training/evaluation scoring | Boolean or aggregate metric | Produces operative comparison | Dataset-relative match only, conditional on target and parser | Feeds next row, not a direct playbook truth veto | Python branch/metric consumer, returned value, enforcing, current round/snapshot | SRC-1, `eval/finance/data_processor.py` | none | none | FINER truncation, Mind2Web missing target value, skipped evaluation errors limit license. |
| [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) | disposition/acceptance | implemented | [EPI-OBJ-answer](#epi-obj-answer) | no content change | Accept answer for stopping or retry | Processor Boolean; round limit bounds continuation | After scoring | Stop regeneration or request another round | Enforcing | Acceptance for matching this sample target, not reasoning validation | Correct/incorrect feedback and retry selection | Orchestrator, correctness flag, enforcing, sample | SRC-1, `ace/ace.py` | [RT-CLM-context-improvement](runtime.md#rt-clm-context-improvement) | Label-free reading contradicted | no_ground_truth still uses oracle; stopping by round limit is not acceptance. |
| [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) | content transformation | implemented | [EPI-OBJ-reflection](#epi-obj-reflection) | truth-apt transformation: indeterminate | Trace/feedback/selected bullets to diagnosis | Reflector model, task-local diagnosis | Correct result once, incorrect result per permitted round | Reflection and tags | Advisory interpretation plus counter input | Candidate explanation only | Reflection reaches regenerator/curator | Prompt slots, model interpretation, advisory, current and update rounds | SRC-1, `ace/core/reflector.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | none | Root-cause claim is not entailed by answer mismatch; no actual diagnosis supplied to establish non-entailment of a particular output. |
| [EPI-RTE-counter-update](#epi-rte-counter-update) | behavior/policy adaptation | implemented | [EPI-OBJ-bullet-tags](#epi-obj-bullet-tags) | non-truth-apt policy/content update: model tags change displayed utility counters | Tagged bullet utility | Reflector judgment; code maps recognized tags to increments | After reflection, before later prompts | helpful/harmful increment or unchanged count | Enforcing metadata write; later advisory use | Counts document accepted tag events, not causal bullet benefit | Changes metadata supplied to future model judgments | Generator/curator prompt text, advisory, later samples and reload | SRC-1, `playbook_utils.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | none | Harmful count is not withdrawal; duplicate IDs/tags are not independent causal trials. |
| [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation) | content transformation | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | truth-apt transformation: indeterminate | Reflections/context to proposed lesson; proposals to reducer output | Curator model; reducer novelty/usefulness policy | Scheduled sequential curation or batch group/reduction | ADD proposals or empty operations | Model selection then parser | Proposed guidance, not accepted explanation | Supplies prospective instructions | Curator/reducer prompt, advisory policy then operation output, update stage | SRC-1, `ace/prompts/curator.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | none | Reducer can drop proposals but does not receive complete original traces; no observed semantic preservation/novelty. |
| [EPI-RTE-curator-admission](#epi-rte-curator-admission) | check/evidence production | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | no content change | JSON outer structure and ADD keys | Python parser; syntax/key-presence domain | After curator response | Structure accepted or exception | Enforcing parser gate | Structural compatibility only; not truth, relevance or transfer | Allows application attempt or failure fallback | Curate/proposer/reducer caller, parsed dict/exception, enforcing, current update | SRC-1, `ace/core/curator.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | none | content/section types not fully checked; unsupported names can pass sequential validation. |
| [EPI-RTE-curator-admission](#epi-rte-curator-admission) | disposition/acceptance | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | no content change | Admit supported ADD; reject malformed response or empty result | Python application plus upstream model choice | After schema gate | Applied ADD or prior playbook | Enforcing text admission | Operational admission, not evidence-consuming acceptance of lesson truth | New text can govern next generation without a per-lesson accuracy veto | Operation interpreter, ADD list, enforcing write, subsequent calls | SRC-1, `playbook_utils.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | No semantic acceptance established | No human per-addition approval; failure fallback subject to logging success. |
| [EPI-RTE-curator-admission](#epi-rte-curator-admission) | content transformation | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | truth-apt transformation: non-ampliative reshaping | Fixed single-line content placed under section with fresh ID | Deterministic application for well-formed ADD | Application stage | Content retained verbatim with zero counters and section placement | Enforcing formatting | No extra warrant from reshaping | Addressable bullet enters playbook | String construction to generator/curator, advisory downstream, later tasks | SRC-1, `playbook_utils.py` | none | none | Bounded deduction in record; arbitrary multiline/non-string content excluded from this preservation conclusion. |
| [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload) | retention | implemented | [EPI-OBJ-playbook](#epi-obj-playbook), [EPI-OBJ-bullet-tags](#epi-obj-bullet-tags) | no content change | Runtime playbook to files and later explicit reload | Save schedule/path choice | In-run snapshots/end; later invocation | Retained text | Enforcing write/read | Retention is not endorsement | Makes prior guidance available across runs | see record | SRC-1, `ace/ace.py` | none | none | No complete provenance ledger or restored ID history. |
| [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select) | disposition/acceptance | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | no content change | Whole snapshot for final offline testing | Strict validation-accuracy improvement; successful scored subset | Periodic offline validation | best_playbook replaced or kept | Enforcing selection | Empirical selection for this validation criterion, not per-claim acceptance or causal explanation | Chooses final-test context; current training state not rolled back | Python snapshot selector, metric, ranking then permissive, offline run | SRC-1, `ace/ace.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | none | Exceptions skipped; no observed comparison or transfer test here. |
| [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge) | check/evidence production | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | no content change | Candidate redundancy groups | Embedding dot-product threshold, not logical equivalence | Optional analyzer after curation | Similarity groups | Ranking/grouping | Numerical similarity only | Selects groups for rewrite/removal | Analyzer group indices, threshold, permissive, current maintenance | SRC-1, `ace/core/bulletpoint_analyzer.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | none | High similarity does not establish same truth conditions. |
| [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge) | content transformation | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | truth-apt transformation: indeterminate | Similar group to replacement or first-member-only result | Merge model plus regex; merge=False keeps first | After grouping | Group replaced, other members removed | Enforcing reconstruction | No checked meaning-preservation license | Can withdraw guidance, including on merge failure | Analyzer to orchestrator playbook, enforcing write then advisory use, later calls | SRC-1, `ace/core/bulletpoint_analyzer.py` | [EPI-CLM-context-quality](#epi-clm-context-quality) | Preservation claim limited | Loss may be real distinct content, not proven duplicate removal. No analyzer-specific undo. |
| [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance) | operational admission/selection/consumption | implemented | [EPI-OBJ-playbook](#epi-obj-playbook) | no content change | Retained text delivered for task solving and further additions | Model interpretation; no enforced per-bullet obedience | Regeneration, later samples/windows and explicit reload | Full playbook delivered | Advisory content, enforcing delivery | Operational reliance allowed without lesson truth acceptance | Can influence answers and new guidance | see record | SRC-1, `ace/prompts/generator.py` | [RT-CLM-context-improvement](runtime.md#rt-clm-context-improvement) | none | Delivery is not observed dependence or benefit. |
| [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) | lifecycle integration | no route found within boundary | [EPI-OBJ-playbook](#epi-obj-playbook) | no content change | Accepted individual truth claim connected to evidence/use | No such phase established by inspected curate/apply or supplied loop | No established activation | Operational retention exists instead | No established epistemic integration force | No individual accepted ampliative claim established | Do not confuse use before acceptance with integration | No such consumer established within these inspected routes | SRC-1, `ace/core/curator.py` | none | none | Bounded to main-repository routes above; AppWorld and actual candidate histories unresolved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-context-improvement](runtime.md#rt-clm-context-improvement) | see record | SRC-1, `README.md`; doctrine/design and reported operation | Three model roles, retained context, no-GT prompts | [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation), [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance) | None supplied | No intervention; AppWorld absent | Improvement-directed context-change capacity is wired | Label-free interpretation does not hold for inspected target-scored drivers. Exercised self-improvement and learning benefit unestablished. |
| [EPI-CLM-context-quality](#epi-clm-context-quality) | see record | SRC-1, `README.md`; doctrine/design and reported operation | Reflection asks for diagnoses; curator asks for new useful content; reducer asks to discard low-value proposals | [EPI-RTE-answer-match](#epi-rte-answer-match), [EPI-RTE-curator-admission](#epi-rte-curator-admission), [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge), [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select) | None supplied; README gains are attributed reports | No inspectable comparison design or independent component variation; similarity is not equivalence | Incremental ADD formatting and optional redundancy-management machinery exist; snapshot ranking uses scored outcomes | Preservation is consumer-local; merging is model-mediated and can delete on fallback. Quality, latency and accuracy gains not verified here. |

## Bounded conclusion

ACE can import text of unknown warrant, generate answers against it, compare extracted answers with dataset targets, ask a model to diagnose errors, and let another model propose retained guidance. It stores natural-language playbook content with symbolic identifiers/counters, not updated provider weights. The separate remote and embedding components' mutability limits are in [RT-CMP-generator](runtime.md#rt-cmp-generator), [RT-CMP-reflector](runtime.md#rt-cmp-reflector), [RT-CMP-curator](runtime.md#rt-cmp-curator) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model).

Answer matching has consequential but narrow authority: it controls retry/stop decisions and validation-snapshot ranking. FINER field matching, formula numeric/string matching and Mind2Web action-description matching do not validate the producing reasoning, causal diagnosis or transferable strategy. The FINER interpreter path adds operational host effects before comparison, not extra warrant. Successful outcomes therefore cannot establish reflector explanations or individual bullet utility ([EPI-RTE-answer-match](#epi-rte-answer-match), [RT-RTE-finer-scoring](runtime.md#rt-rte-finer-scoring)).

The deterministic ADD wrapper is non-ampliative for the inspected well-formed single-line case. No warranted-premise derivation of new task knowledge is established. Model-generated answers, diagnoses, proposals and merges remain semantically indeterminate without concrete outputs; some might copy, derive, conjecture or merely instruct. The architecture requests generalization, but that is not evidence of a produced accepted ampliative claim. Schema admission licenses application attempts, not truth. Counter increments represent model judgments; harmful tags do not automatically revoke guidance ([EPI-RTE-curator-admission](#epi-rte-curator-admission), [EPI-RTE-counter-update](#epi-rte-counter-update)).

The main loop implements operational retention/use before any established per-lesson evidence-consuming acceptance. Validation chooses a whole playbook for final testing under a named accuracy criterion; it neither accepts each lesson nor rolls back current training state. Similarity maintenance can remove content, including when merging fails, without truth-directed withdrawal or a preservation check. Explicit reload permits cross-run reuse without provenance authentication ([RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select), [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge), [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload)).

The behavioral-authority path is full playbook text in generator and curator prompts: delivery is enforced by code, interpretation is advisory, and the horizon spans immediate regeneration, later samples/windows and explicit cross-run reload. This wires an improvement-directed self-change pathway relative to the independent answer-accuracy objective; subsequent behavior causally depending on a retained change is not evidenced. Thus exercised self-improvement and successful improvement remain separately unestablished. Reflection has an implemented feedback channel, but both causal directions of actual reflective behavior remain unobserved. Computation performs the bounded driver's internal proposal/decision/application roles; no actual localized theory, content-dependent theory consumption or claim/result/blame-directed criticism was supplied. The theory-builder conditions and learning limits remain separate as assessed in [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), not a combined negative verdict.

## Shared records

### Operative objects

#### EPI-OBJ-answer
Label: Extracted answer

Source-native identity: generator answer extracted for `DataProcessor.answer_is_correct`; natural-language or numeric answer strings in Python memory, with task-specific symbolic parsing. Dataset targets are external answer references, not ACE-produced facts. Closest supplied [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) and [RT-RTE-finer-scoring](runtime.md#rt-rte-finer-scoring) are routes, not an object counterpart; this object spans their input/output interfaces. SRC-1, `eval/finance/data_processor.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py`.

> if self.task_name == "finer":
>             return self._finer_answer_is_correct(predicted, ground_truth)
> --- `eval/finance/data_processor.py`

#### EPI-OBJ-reflection
Label: Reflection response

Source-native identity: `reflection_content` returned as reflector response text; natural-language diagnosis and proposed principles mixed with JSON tags, held in Python strings and model-call logs. Closest supplied [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) is the encompassing process, not this object; batch also produces reflections. Requested fields do not establish an actual truth-apt theory or a correct diagnosis. SRC-1, `ace/core/reflector.py`, `ace/prompts/reflector.py`.

> - error_identification: what specifically went wrong in the reasoning?
>   - root_cause_analysis: why did this error occur? What concept was misunderstood?
>   - correct_approach: what should the model have done instead?
>   - key_insight: what strategy, formula, or principle should be remembered to avoid this error?
> --- `ace/prompts/reflector.py:20-23`

#### EPI-OBJ-playbook
Label: Playbook content

Source-native identity: `current_playbook` / `self.playbook`, specifically bullet content and section organization, excluding the separately assessed tags/counters. Natural language in Python strings and saved text files is interpreted by generator and curator models. It may express truth-apt formulas/regularities or prescriptions; no concrete produced instance is supplied. Closest supplied [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload) and [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance) describe transport and consumers rather than declare this object. SRC-1, `ace/prompts/curator.py`, `playbook_utils.py`.

> - The playbook you created will be used to help answering similar questions.
> --- `ace/prompts/curator.py:9-9`

#### EPI-OBJ-bullet-tags
Label: Bullet tags and counters

Source-native identity: reflector `bullet_tags`, stored line `helpful`/`harmful` counters and bullet IDs. JSON/list values and integer fields have symbolic update rules; model utility judgments are semantically interpreted before their encoding. Substrates are Python values, playbook strings and saved text. Distinct from [EPI-OBJ-playbook](#epi-obj-playbook): counters can change while content remains fixed. Closest supplied [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) spans their production/consumption, not an object counterpart. SRC-1, `playbook_utils.py`.

> return f"[{bullet_id}] helpful={helpful} harmful={harmful} :: {content}"
> --- `playbook_utils.py`

### Routes

#### EPI-RTE-answer-match
Label: Dataset answer matching

Endpoints/progression/owner: task processor receives extracted prediction and dataset target, parses according to task and returns correctness or aggregate accuracy. Computational comparison owns the decision; human/data authors supply reference labels, not per-prediction approval. It overlaps the check portions of [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select) and [RT-RTE-finer-scoring](runtime.md#rt-rte-finer-scoring); it is a cross-route scoring part, not a replacement for their orchestration or host-effect findings. Mode is bounded labelled training/evaluation. SRC-1 implementation: `eval/finance/data_processor.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py`.

- Immediate return: Boolean correctness or task-level aggregate accuracy; FINER can return matched/total field counts.
- Later read-back: inapplicable — this scorer does not retain updated content for later invocations; snapshot selection and retained playbooks are separate routes.
- Delegated visibility: Full extracted answer and target strings reach the host processor; it does not see or validate the full generating reasoning.
- Selection predicate: FINER task selects lowercased comma-fragment matching; formula selects float equality with string fallback; Mind2Web selects parsed element/operation/value matching.
- Invalidation or expiry: inapplicable — each comparison evaluates current inputs, not a retained cache.
- Activation or effect: Returned correctness controls retries and contributes to validation ranking through supplied runtime consumers; actual effects unobserved.
- Evidence limits: Targets are assumed references, not independently validated facts. FINER can execute prediction expressions after successful target eval; aggregate evaluation can skip errors per supplied runtime. No target execution performed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deterministic trace, by code inspection: FINER target `1`, prediction `1,999` produces labels `["1"]` and predictions `["1","999"]`; length normalization truncates the latter to `["1"]`. Both retained fragments evaluate to integer 1, count is 1 and score is 1, so the checker returns true. This is a deduction about the implementation, not a run or an invented observed candidate. It refutes an exact-whole-answer interpretation while preserving the narrower field-match license. Formula float equality also checks values, not derivations. In both Mind2Web processors a matching CLICK needs only element and operation, and a TYPE/SELECT with no parsed target value can pass without value verification. Neither checks live browser success.

> if len(pred) != len(label):
>             if len(pred) > len(label):
>                 pred = pred[:len(label)]
> --- `eval/finance/data_processor.py`

> score = count / len(pred) if pred else 0
>         if return_counts:
>             return count, len(pred)
>         return score == 1
> --- `eval/finance/data_processor.py`

> if truth["value"] is None:
>             return True  # No value to check
> --- `eval/mind2web/data_processor.py`

> if truth["value"] is None:
>             return True  # No value to check
> --- `eval/mind2web2/data_processor.py`

#### EPI-RTE-counter-update
Label: Counter update

Endpoints/progression/owner: reflector response supplies tags; `update_bullet_counts` creates an ID lookup and increments matching parsed lines. Python owns the write; reflector supplies utility judgments. This spans counter-update portions of [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) and [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation), not a new adaptation container. The target is bullet usefulness for the current task according to model interpretation, not independently isolated causal contribution. SRC-1 implementation, `ace/core/reflector.py`, `playbook_utils.py`; prompt policy, `ace/prompts/reflector.py`.

- Immediate return: Playbook text with matching helpful/harmful counters incremented, or original text if no valid tag map.
- Later read-back: Updated counters travel in full playbook prompts to generator/curator and may persist through files and explicit reload.
- Delegated visibility: Reflector receives the response trace and only parsable bullets selected by generator-reported IDs; this does not prove actual bullet use. Future consumers see counters without independently validated utility evidence.
- Selection predicate: Dict tag entries with id or bullet key; matching parsed IDs; only helpful and harmful values increment. Last tag for an ID wins within the lookup.
- Invalidation or expiry: Neutral leaves counts unchanged; harmful increments do not remove content or automatically expire it.
- Activation or effect: Metadata is rewritten and delivered for possible model interpretation; causal behavioral dependence unobserved.
- Evidence limits: Code counts tags, not successful interventions on bullet presence. Malformed/unmatched tags may not change counters. No independent causal utility oracle or per-content human approval is wired here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is symbolic tag recognition, with no content-specific human veto. The guidance asks helpful/harmful/neutral judgments. There is no truth-directed rollback in this utility; later caller replacement/analyzer rewriting are distinct mechanisms. Content persists unchanged by this utility.

> if tag == 'helpful':
>                 parsed['helpful'] += 1
>             elif tag == 'harmful':
>                 parsed['harmful'] += 1
> --- `playbook_utils.py`

#### EPI-RTE-curator-admission
Label: Curator structural admission

Endpoints/progression/owner: curator response goes through `_extract_and_validate_operations`, then deterministic `apply_curator_operations`; batch additionally filters proposer/reducer operations to ADD. This cross-cutting parser/application part overlaps [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) and [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation), but does not replace either. Models propose/select content; Python checks outer structure and writes supported additions. No per-content human approval or dataset answer oracle evaluates each proposed lesson. Context is scheduled training curation, not a universal knowledge-acceptance gate. SRC-1 implementation, `ace/core/curator.py`, `playbook_utils.py`; proposal guidance, `ace/prompts/curator.py`.

- Immediate return: Parsed operations, then updated playbook/next ID; handled parse/application errors or empty-response sentinel return previous text and empty operations where failure logging succeeds.
- Later read-back: Admitted text enters post-curator generation, later samples/windows, future curator inputs and persisted snapshots/reload.
- Delegated visibility: Sequential curator gets current playbook, recent reflection, question context and stats; batch reducer gets base playbook and operation groups rather than complete raw traces.
- Selection predicate: Reasoning must be a string, operations a list, each operation a dict with type, and ADD must contain type/section/content. Batch drops non-ADD names; deterministic application implements ADD only.
- Invalidation or expiry: This application consumer preserves existing lines; no implemented DELETE/UPDATE here. Failure fallback and the separate analyzer/reload routes qualify whole-system preservation.
- Activation or effect: Supported additions are written without per-addition accuracy veto and delivered downstream; actual interpretation and gain unobserved.
- Evidence limits: Structural checks do not validate truth, semantic novelty or full content types. No actual proposed/accepted lesson supplied. Batch exception-recovery limitations remain as supplied by runtime.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guidance asks new, nonredundant, concise strategies; batch reducer may drop already-covered/vague/low-value proposals. That is model-mediated disposition, not checked semantic equivalence or evidence-consuming acceptance against a proposition-specific truth criterion. Empty operations can reject all proposals; no score threshold vetoes every admitted lesson. Curator reasoning is logged, but only admitted bullet text/counters form the reconstructed playbook.

Concrete deterministic reshaping deduction: with initial text `## OTHERS`, next ID 1, and one well-formed ADD to `others` whose single-line content is `Revenue equals price times quantity.`, application normalizes the section, obtains a section slug, allocates a fresh suffixed ID, initializes both counters to zero, and places exactly that content after the header. The wrapper adds no proposition about revenue. It preserves the given proposition without checking it. This case does not prove that a model-produced proposal was an entailed derivation, nor that arbitrary multiline content is safely represented.

> required_fields = {"type", "section", "content"}
>                 missing_fields = required_fields - set(op.keys())
>                 if missing_fields:
>                     raise ValueError(f"ADD operation {i} missing fields: {list(missing_fields)}")
> --- `ace/core/curator.py`

> content = op.get('content', '')
>             
>             new_line = format_playbook_line(new_id, 0, 0, content)
>             bullets_to_add.append((section, new_line))
> --- `playbook_utils.py`

> - Drop proposals that are already covered by the current playbook.
> - Drop vague, redundant, or low-value proposals.
> --- `ace/prompts/curator.py`

### Claims

#### EPI-CLM-context-quality
Label: Context quality and preservation claims

Source-native claims: README says incremental updates preserve prior knowledge, reflection improves context quality/downstream performance, curator uses deterministic merging/de-duplication/pruning, and reports performance gains. Closest supplied [RT-CLM-context-improvement](runtime.md#rt-clm-context-improvement) concerns evolving contexts and label-free self-supervision; this record separately addresses preservation, quality mechanism and quantitative outcome claims, not that record's identity. SRC-1, `README.md`, doctrine/design and reported operation, not observed or causal evidence in this run.

> - 📈 **Incremental Delta Updates**: Localized edits that preserve prior knowledge while accumulating new insights
> --- `README.md`

> 2. **Reflector** separates evaluation and insight extraction from curation, improving context quality
> 3. **Curator** converts lessons into structured delta updates with helpful/harmful counters, using deterministic merging with de-duplication and pruning
> --- `README.md`

> ACE consistently outperforms strong baselines, achieving average gains of **+10.6%** on agent tasks and **+8.6%** on domain-specific benchmarks, across both offline and online adaptation settings.
> --- `README.md`

The ADD consumer preserves old lines; the optional analyzer can remove them and its replacement is model-generated. Thus the deterministic description does not establish deterministic semantic preservation across all paths. Benchmark and efficiency reports remain attributed, without supplied experimental design/trace sufficient for independent causal attribution.
