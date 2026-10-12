---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AgentFly's answer checking, case authority, model-mediated evidence acquisition and retriever selection at the frozen revision."
run-id: AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01
reviewed-boundary: "42fbbcac63dd58ed6856c0761357345a58e4f032"
---

# AgentFly epistemic report

## Source-and-claim boundary

The question is what AgentFly acquires or produces that can be true or false, what checks license reliance, and what later consumers those results reach. Scope and external exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, plus attributed README results, not observed execution or causal experiments. The source calls the project Memento; the analyzed target remains AgentFly.

Public claims are [EPI-CLM-experience-learning](#epi-clm-experience-learning), [EPI-CLM-weight-updates](#epi-clm-weight-updates) and [EPI-CLM-automated-retraining](#epi-clm-automated-retraining). None is treated as an execution trace. Accessible source permits assessing architectural capacity; it does not establish model compliance or benefit.

### Coverage

Direct inspection below supplements, rather than merely repeats, the supplied runtime. Registered tools were searched using `def`, `@mcp`, entry-point and judgment/write terms in SRC-1's client, memory and server files. CLI dispatch, recovery and permissions also use the supplied runtime findings; this is not an exhaustive independent read of all implementations.

| Entry point or operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| Ordinary CLI and local streaming CLI | `client/agent.py`, `client/agent_local_server.py` | Supplied [RT-RTE-query-execution](runtime.md#rt-rte-query-execution), [RT-RTE-local-execution](runtime.md#rt-rte-local-execution); no independent full reread. Prefix/parsing admission is not answer verification. |
| Both benchmark drivers: judges, writes, prompt formatting | `client/no_parametric_cbr.py`, `client/parametric_memory_cbr.py` | Direct judge, writer and formatter reads; parametric query loop/reload read directly. [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-outcome-label](#epi-rte-outcome-label), [EPI-RTE-case-format](#epi-rte-case-format). |
| Parametric scoring and standalone retrieval CLI | `memory/parametric_memory.py` | Complete direct read; [RT-CMP-case-retriever](runtime.md#rt-cmp-case-retriever), [EPI-RTE-case-format](#epi-rte-case-format). CLI sorts scores and prints top-k; it does not accept the case propositions. |
| Nonparametric retrieval | `memory/np_memory.py` | Supplied runtime's embedding/ranking findings; implementation details not independently reread. Prevents a complete semantic-preservation judgment for this alternative. |
| Trainer: parser, pair construction, evaluator, optimizer and checkpoint selection | `memory/train_memory_retriever.py` | Direct selected ranges; [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training), [EPI-RTE-case-format](#epi-rte-case-format). Pair-label prediction is the checked domain. |
| Query-aware crawl/extraction | `server/ai_crawl.py` | Direct grounding prompt and complete extraction-to-return path; [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction). Rate admission does not establish quote fidelity. |
| SearxNG and SerpAPI tools | `server/search_tool.py`, `server/serp_search.py` | Direct search dispatch/return and complete SerpAPI read; [EPI-RTE-search-import](#epi-rte-search-import). Provider truth is excluded. |
| Image and video question answering | `server/image_tool.py`, `server/video_tool.py` | Direct generation/return ranges; [EPI-RTE-media-answer](#epi-rte-media-answer). Preparation/keyframe/transcription detail remains uninspected; exact information loss is unresolved. |
| Arithmetic tools | `server/math_tool.py` | Complete direct read; [EPI-RTE-math-result](#epi-rte-math-result). This exposes a counterexample to a blanket reliable-arithmetic inference. |
| Document dispatcher | `server/documents_tool.py` | Direct format dispatch. Caption/transcription, spreadsheet, JSON/XML, text, DOCX and fallback routes differ. See coverage limit below; not all transformations assessed. |
| Other page tools and spreadsheet implementations | `server/craw_page.py`, `server/jina_fetch_tool.py`, `server/excel_tool.py` | Registration search only; material implementation unassessed here. Prevents system-complete conclusions about source fidelity and all evidence checking. |
| Workspace persistence, terminal execution and interpreter cleanup | `server/code_agent.py`, `server/interpreters/subprocess_interpreter.py` | Supplied [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution); registration search distinguishes exposed tools from lower-level execute_code. No independent full read or execution. |
| Claims, corpus and experiments | `README.md`, `data/deepresearcher.jsonl`, `memory/memory.jsonl`, `memory/training_data.jsonl`, `Figure/` | Direct relevant README claims; corpus sampling is supplied boundary evidence only. Full corpus and figures unassessed: no dataset-wide correctness, artifact genealogy or benchmark/causal conclusion. |

Document dispatch imports literal text/JSON/XML, calls model captions/transcription, and delegates other formats to conversion libraries/services (SRC-1, `server/documents_tool.py`). Uninspected converter, spreadsheet and fallback details prevent assigning a single content relation or fidelity guarantee to document processing. Provider parameters/checkpoints and live external responses are unavailable within scope. These gaps prevent parameter-content assessment, successful operation and provenance verification, not assessment of inspected wiring. No unassessed included operation is used to justify a system-complete negative about knowledge production or checking.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history) | Question premises and executor reports; task instructions themselves need not be truth-apt | see record | SRC-1, `client/agent.py` | Raw tool evidence reaches executor; planner receives task summaries, not a verified evidential chain. |
| [EPI-OBJ-model-output](#epi-obj-model-output) | Candidate final answer to a dataset question; error text/plan exhaustion need not answer it | see record | SRC-1, `client/parametric_memory_cbr.py` | Generation relation indeterminate; no inspectable inference proof or observed answer. |
| [EPI-OBJ-judge-result](#epi-obj-judge-result) | Correct/incorrect assertion and rationale about reference agreement | see record | SRC-1, `client/parametric_memory_cbr.py` | Semantic equivalence judgment is model-mediated; failure is encoded as incorrect. |
| [EPI-OBJ-case-entry](#epi-obj-case-entry) | Question, latest plan and outcome label; plan may contain factual premises as well as action instructions | see record | SRC-1, `client/parametric_memory_cbr.py`, `client/no_parametric_cbr.py` | Label checks answer outcome, not plan validity; full evidence is not retained in the case entry. |
| [EPI-OBJ-training-entry](#epi-obj-training-entry) | Pair label asserting current answer correctness; not independently established case usefulness | see record | SRC-1, `client/parametric_memory_cbr.py` | Same outcome applied to all retrieved cases; no marginal-effect comparison. |
| [RT-CMP-case-retriever](runtime.md#rt-cmp-case-retriever) | Not determinable as individuated propositions; numerical embeddings/weights and scores | see record | SRC-1, `memory/parametric_memory.py` | Ranking authority exists; trained content, exact version and improvement are unestablished. |
| [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction) | Page assertions and requested relevant answer/quotes | see record | SRC-1, `server/ai_crawl.py` | Returned model text is not a preserved full page or checked quotation. |
| [EPI-RTE-search-import](#epi-rte-search-import) | External titles, links and snippets | see record | SRC-1, `server/search_tool.py`, `server/serp_search.py` | Acquisition, not production; provider warrant unknown. |
| [EPI-RTE-media-answer](#epi-rte-media-answer) | Visual descriptions and answers about supplied media | see record | SRC-1, `server/image_tool.py`, `server/video_tool.py` | Semantic transformation indeterminate; sampled frames do not establish full-video coverage. |
| [EPI-RTE-math-result](#epi-rte-math-result) | Numeric results under Python arithmetic | see record | SRC-1, `server/math_tool.py` | Add/subtract and awaited round differ from multiply/divide's unawaited call. |
| [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution) | Files/stdout may contain claims; wrapper success label is a claim about execution, not result truth | see record | SRC-1, `server/code_agent.py` | String error reports can receive success wording. Workspace retention is not epistemic acceptance. |

## Authority-route ledger

Each row is a distinct function even when several cite one container. Fields owned by a declaring record say see rather than reproducing its account. All operation evidence remains uninspected; architectural status below refers to source wiring only.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-query-execution](runtime.md#rt-rte-query-execution) | content transformation | implemented | [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history) | truth-apt transformation: indeterminate | Task reports and answer candidates | see record | see record | see record | see record | No independent semantic warrant from fluent generation | see record | see [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) | SRC-1, `client/agent.py` | none | none | Entailment and non-entailment both unresolved without content/trace. |
| [RT-RTE-query-execution](runtime.md#rt-rte-query-execution), [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) | operational admission/selection/consumption | implemented | [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history) | no content change | Parsed plan, completion prefix, tool names | see records | see records | see records | see records | Syntax and routing only, not answer acceptance | see records | see [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) | SRC-1, `client/agent.py`, `client/agent_local_server.py` | none | none | Completion is admitted without semantic check on open CLI route. |
| [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Page-to-relevant-text fidelity | see record | see record | see record | see record | Source warrant unknown after model selection/rewriting | see record | Executor, tool-result text, advisory, current task | SRC-1, `server/ai_crawl.py` | none | none | Requested quotes are not independently checked. |
| [EPI-RTE-search-import](#epi-rte-search-import) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | External snippets | see record | see record | see record | see record | Unknown source warrant; links preserve some source identity | see record | Executor, MCP text, advisory, current task | SRC-1, `server/search_tool.py` | none | none | Search freshness filters do not establish endorsement or truth. |
| [EPI-RTE-media-answer](#epi-rte-media-answer) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Media description/QA | see record | see record | see record | see record | Candidate interpretation only | see record | Executor, tool text, advisory, current task | SRC-1, `server/image_tool.py`, `server/video_tool.py` | none | none | No independent fidelity evaluator in inspected return path. |
| [EPI-RTE-math-result](#epi-rte-math-result) | content transformation | implemented | see record | truth-apt transformation: entailed derivation | Add/sub and awaited round over supplied numbers | see record | see record | see record | see record | Python floating-point result given arguments; not source measurement truth | see record | Executor, numeric tool return, advisory, current task | SRC-1, `server/math_tool.py` | none | none | Multiply/divide do not share this numeric-result conclusion. |
| [EPI-RTE-answer-check](#epi-rte-answer-check) | check/evidence production | implemented | [EPI-OBJ-model-output](#epi-obj-model-output) | truth-apt transformation: indeterminate | Reference-answer semantic agreement | see record | see record | see record | see record | Fallible local agreement assessment, not independent world verification | see record | see record | SRC-1, `client/parametric_memory_cbr.py` | none | none | No trace checking or source provenance test. |
| [EPI-RTE-outcome-label](#epi-rte-outcome-label) | disposition/acceptance | implemented | [EPI-OBJ-judge-result](#epi-obj-judge-result) | no content change | Correctness judgment admitted as label basis | see record | see record | see record | see record | Answer accepted for benchmark scoring by semantic-match criterion only | see record | see record | SRC-1, `client/parametric_memory_cbr.py` | [EPI-CLM-experience-learning](#epi-clm-experience-learning) | answer/plan scope mismatch | Outcome label is not acceptance of plan claims or causal utility. |
| [RT-RTE-case-admission](runtime.md#rt-rte-case-admission) | retention | implemented | [EPI-OBJ-case-entry](#epi-obj-case-entry), [EPI-OBJ-training-entry](#epi-obj-training-entry) | no content change | Append after completed query/judgment | see record | see record | see record | see record | Retains candidates with labels, not warrant upgrade | see record | see [RT-BAP-case-guidance](runtime.md#rt-bap-case-guidance) | SRC-1, `client/parametric_memory_cbr.py` | [EPI-CLM-experience-learning](#epi-clm-experience-learning) | none | Positive and negative cases both retained; no selective rejection gate. |
| [EPI-RTE-case-format](#epi-rte-case-format) | content transformation | implemented | [EPI-OBJ-case-entry](#epi-obj-case-entry) | truth-apt transformation: non-ampliative reshaping | Selected descriptive text, ordered steps | see record | see record | see record | see record | No added warrant; omitted metadata cannot be relied on downstream | see record | see record | SRC-1, `memory/train_memory_retriever.py` | none | scope/provenance loss possible | This relation covers selected text, not preservation of every proposition in arbitrary JSON. |
| [RT-RTE-case-admission](runtime.md#rt-rte-case-admission) | operational admission/selection/consumption | implemented | [EPI-OBJ-case-entry](#epi-obj-case-entry) | no content change | Scores/top-k then positive/negative example partitions | see record; classifier scores are not semantic truth tests | see record | see record | see record | No independently established plan validity or transferable rule | see record | see [RT-BAP-case-guidance](runtime.md#rt-bap-case-guidance) | SRC-1, `client/parametric_memory_cbr.py`, `memory/parametric_memory.py` | [EPI-CLM-experience-learning](#epi-clm-experience-learning) | value proxy | Outcome-conditioned ranking is not identified marginal value. |
| [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) | check/evidence production | implemented | [RT-CMP-case-retriever](runtime.md#rt-cmp-case-retriever) | no content change | Pair-label prediction on validation data | see record | see record | see record | see record | Accuracy/F1/AUC assess agreement with labels, not underlying truth or agent improvement | see record | Trainer, metric variables, advisory to selector, current training run | SRC-1, `memory/train_memory_retriever.py` | [EPI-CLM-experience-learning](#epi-clm-experience-learning) | surrogate target | No isolated case effect. |
| [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) | disposition/acceptance | implemented | [RT-CMP-case-retriever](runtime.md#rt-cmp-case-retriever) | no content change | Optional best checkpoint | see record | see record | see record | see record | Operational successor selection by AUC/F1, not acceptance of a proposition | see record | Trainer, checkpoint file, enforcing overwrite, later initialization if installed | SRC-1, `memory/train_memory_retriever.py` | [EPI-CLM-automated-retraining](#epi-clm-automated-retraining) | scheduling unknown | Last checkpoint saves without this best-selection criterion. |
| [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) | behavior/policy adaptation | implemented | [RT-CMP-case-retriever](runtime.md#rt-cmp-case-retriever) | non-truth-apt policy/content update: gradient-trained numerical retrieval policy | Classifier parameters | see record | see record | see record | see record | No individuated accepted proposition established | see record | see [RT-BAP-case-guidance](runtime.md#rt-bap-case-guidance) | SRC-1, `memory/train_memory_retriever.py` | [EPI-CLM-weight-updates](#epi-clm-weight-updates), [EPI-CLM-experience-learning](#epi-clm-experience-learning) | LLM/retriever distinction | Case reload is not weight reload; live use unobserved. |
| [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution) | operational admission/selection/consumption | implemented | see record | no content change | Caller commands and file contents | see record | see record | see record | see record | Execution output is not independent proof of correctness | see record | see record | SRC-1, `server/code_agent.py` | none | success-label overreach | Completed effects are not rolled back by client cleanup. |

No lifecycle-integration row is established for accepted plan knowledge: inspected case writes do not decide plan validity or connect accepted plan claims to supporting evidence. This is a local limit of these writers, not an assertion about every tool or hidden model process.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-experience-learning](#epi-clm-experience-learning) | see record | SRC-1, `README.md`; doctrine/design and reported operation | Case bank, value retrieval and outcome reuse | [RT-RTE-case-admission](runtime.md#rt-rte-case-admission), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training), [EPI-RTE-outcome-label](#epi-rte-outcome-label) | None supplied | Whole-answer outcomes label every retrieved case; no independent variation of cases | Retained experience can guide later planning; numerical policy can be trained separately | Transfer, improved capacity and causal gains are unestablished; retained case is latest plan, not necessarily a whole trajectory. |
| [EPI-CLM-weight-updates](#epi-clm-weight-updates) | see record | SRC-1, `README.md`; doctrine/design | README specifies no LLM weight updates | [RT-RTE-query-execution](runtime.md#rt-rte-query-execution), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) | None supplied | Remote provider internals uninspected | Client inference does not issue planner/executor parameter updates; trainer does update retrieval classifier | A literal all-model-weights reading of the opening slogan is too broad. |
| [EPI-CLM-automated-retraining](#epi-clm-automated-retraining) | see record | SRC-1, `README.md`; doctrine/design | Checklist claims automated collection and retraining | [RT-RTE-case-admission](runtime.md#rt-rte-case-admission), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) | None supplied | Missing documented retrain script; separate executable trainer is not scheduled by query driver | Automatic pair collection plus operator-started training are implemented | Full automatic retraining/deployment cycle not established. |

## Bounded conclusion

AgentFly's inspected planner/executor routes consume imported tool information and produce candidate reports and answers. JSON parsing, completion prefixes, tool-name resolution and cleanup govern progression, not semantic acceptance. Tool extraction requests verbatim grounding but returns only model-selected text; preserved warrant cannot be inferred. Search snippets retain links but have unknown source truth. Media QA supplies additional candidate claims without an independent fidelity check in the inspected return paths. Symbolic arithmetic supports bounded derivation for add/subtract and awaited rounding, not a general oracle: multiply/divide's asynchronous-name collision prevents attributing their intended numeric result to this implementation.

The benchmark judge has a real evidence-consuming target: semantic agreement of the prediction with at least one dataset reference answer. Its criterion, intended benchmark use and question scope are explicit. A `correct` result is accepted for scoring and downstream labeling; it is not infallible world knowledge, a plan-quality check, a source-verification decision or a causal case-utility judgment. Parse/provider failure produces `incorrect` and can therefore poison negative labels instead of expressing uncertainty. Positive and negative plans are both retained and later delivered with adoption/avoidance instructions. Retention and guidance are not lifecycle integration of accepted plan knowledge. Result-file restart skipping can suppress later recovery of a failed memory write; no transactional withdrawal or automatic label correction is established by the inspected writers.

Case formatting preserves selected description strings but drops other fields; it cannot raise warrant. The supplied runtime's current-history delivery likewise exposes the planner to executor summaries, not all raw evidence. A case's label grants operational example authority across questions through user-role text, whereas the retriever's weights grant numerical ranking authority through checkpoint loading. Those are independent channels. None establishes compliance or improved capacity from delivery alone.

The standalone trainer adapts numerical retrieval policy from copied outcome labels and selects optional best weights by validation AUC/F1. These evaluators license label-prediction comparisons only. No exact trained checkpoint, observed exercise or causal contrast supports a stronger learning claim. The improvement-directed pathway is architecturally wired; later operation's causal dependence and successful improvement remain unestablished. Reflection, theory-building and autonomy do not follow from the existence of outcome-fed retention or gradient updates. The records retain operational feedback, not an inspected content-directed criticism/revision of a formulated explanatory theory. Uninspected models and included document/converter alternatives prevent broader negatives. No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-model-output
Label: QueryRecord model_output

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

This object is the answer input within the supplied route container (cross-kind containment), not a replacement for the route. Source-native `model_output` is natural-language candidate content in a Python QueryRecord and result JSONL; structural envelopes are symbolic. It may instead contain planner error/last-plan text. It differs from [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history): terminal output is the judge's input and can persist in result records after history clears. SRC-1 implementation, `client/parametric_memory_cbr.py`.

> model_output=final_answer,
> --- `client/parametric_memory_cbr.py`

#### EPI-OBJ-judge-result
Label: judgement and rationale

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

Cross-kind part: the route's check result. `judgement` is a symbolic branch token in a Python dictionary/result JSONL; `rationale` is natural-language candidate explanation. The token drives label assignment, while the rationale is logged without an implemented evidence-reassessment consumer in these writers. Distinct from answer text and retained plan. SRC-1 implementation, `client/parametric_memory_cbr.py`; evidence in [EPI-RTE-answer-check](#epi-rte-answer-check).

#### EPI-OBJ-case-entry
Label: memory_entry and mem_entry

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

Cross-kind part: retained case artifact, not the whole admission route. Parametric `memory_entry` stores case/plan/case_label; nonparametric `mem_entry` stores question/plan/reward. Questions/descriptions are natural language; plan JSON is symbolic for structure and natural language for descriptions; labels are symbolic. Substrate is append-only JSONL then Python pool/metadata. The retained latest plan is not identical to the result record's fuller traces. SRC-1 implementation, `client/parametric_memory_cbr.py`, `client/no_parametric_cbr.py`.

> memory_entry = {
>     "case": query,
>     "plan": plan,
>     "case_label": case_label
> }
> --- `client/parametric_memory_cbr.py`

> mem_entry = {
>     "question": q,
>     "plan": rec.plan_json or "",
>     "reward": reward
> }
> --- `client/no_parametric_cbr.py`

#### EPI-OBJ-training-entry
Label: training_entry truth_label

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

Cross-kind part: parametric pair artifact. Query/case/plan text plus symbolic case_label/truth_label are appended to training JSONL, then tokenized by the separate trainer into numerical inputs. This differs from the retained case: it pairs the current query with each retrieved prior case and copies current answer correctness, not the prior case's label. SRC-1 implementation, `client/parametric_memory_cbr.py`, `memory/train_memory_retriever.py`; evidence in [EPI-RTE-outcome-label](#epi-rte-outcome-label).

### Routes

#### EPI-RTE-answer-check
Label: llm_judge semantic agreement

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

Dataset ground_truth and prediction → formatted reference-comparison prompt → `gpt-4o-mini` inference → stripped/parsed JSON → normalized judgment. Python owns plumbing; remote model proposes rationale and decision; normalization vetoes unsupported tokens into incorrect. No human per-item veto is wired. The expected-answer oracle is the dataset reference, not the judge model. Mode is bounded benchmark evaluation. Target is answer/reference semantic agreement for this question, not explanation, tool evidence or source truth. The reference's own correctness is unverified. Model mutability is see [RT-CMP-tool-judge-models](runtime.md#rt-cmp-tool-judge-models).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dictionary with normalized judgement and rationale.
- Later read-back: Rationale/judgment can be retained in result JSONL; restart consumes question identity, not a fresh correctness assessment.
- Delegated visibility: Judge receives question, reference list and prediction; no planner or tool trace.
- Selection predicate: Model semantic agreement judgment, parsed into correct/incorrect; unsupported value or exception becomes incorrect.
- Invalidation or expiry: No automatic reconsideration/expiry in inspected drivers; files are externally editable.
- Activation or effect: Judgment is wired to reward/case_label/truth_label assignment and result recording; correctness or exercised dependence unobserved.
- Evidence limits: Prompt requests assessment but supplies no calibrated reliability or independent evidence check. SRC-1 implementation and prompt doctrine, `client/parametric_memory_cbr.py`, `client/no_parametric_cbr.py`.

> 1. The pred_answer doesn't need to be exactly the same as any of the ground truth answers, but should be semantically same for the question.
> 2. Each item in the ground truth answer list can be viewed as a ground truth answer for the question, and the pred_answer should be semantically same to at least one of them.
> --- `client/parametric_memory_cbr.py`

> if judgement not in ("correct", "incorrect"):
>     judgement = "incorrect"
> --- `client/parametric_memory_cbr.py`

> return {"judgement": "incorrect", "rationale": f"judge failed: {e}"}
> --- `client/parametric_memory_cbr.py`

#### EPI-RTE-outcome-label
Label: Outcome to case and pair labels

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

After evaluation, Python accepts correct as positive benchmark outcome and all other normalized outcomes as negative. This evidence-consuming decision names semantic-match criterion, benchmark scoring use and question scope through [EPI-RTE-answer-check](#epi-rte-answer-check). It does not accept plan propositions. Planner proposes the plan, judge determines outcome, software assigns labels; humans select dataset/configuration, not individual content. Trigger is completed query and judgment. Proposed durable change is a labeled latest-plan case and, when cases were retrieved, labeled query/case pairs. Both positive and negative writes are admitted; exception handling can abort later steps but supplies no transactional rollback or per-content rejection. Positive/negative prompt instructions shape later proposals; case text/labels persist, not a checked account of why the plan worked.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean is_correct, positive/negative case label, or nonparametric reward 1/0; written artifacts are separate retention effects.
- Later read-back: Labels partition later planning examples and pair labels feed operator-started training.
- Delegated visibility: Training receives every retrieved case with the same current outcome; case bank receives current question/latest plan/label without judge rationale or tool evidence.
- Selection predicate: Exact normalized correct token determines success; retrieval presence controls pair writes, not causal contribution.
- Invalidation or expiry: No automatic correction/withdrawal or rollback; append-only writes and externally edited files.
- Activation or effect: Label-dependent guidance and numerical training are wired, not observed as behavior changes.
- Evidence limits: A correct answer can arise despite a defective plan or unhelpful retrieved example. No intervention isolates the case effect. SRC-1 implementation, `client/parametric_memory_cbr.py`, `client/no_parametric_cbr.py`.

> is_correct = judge_res["judgement"] == "correct"
> --- `client/parametric_memory_cbr.py`

> for case in retrieved_cases:
>     training_entry = {
>         "query": query,
>         "case": case.get("case", ""),
>         "case_label": case.get("case_label", "unknown"),
>         "plan": case.get("plan", ""),
>         "truth_label": is_correct
>     }
> --- `client/parametric_memory_cbr.py`

#### EPI-RTE-case-format
Label: Case plan text formatting

This formatting crosses pool loading, training and planning delivery, so it overlaps [RT-RTE-case-admission](runtime.md#rt-rte-case-admission) and [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training), not exactly one container. Its distinct referent is deterministic selection/reshaping of plan fields, not outcome admission or numerical optimization. Python owns `_parse_plan`/`_pretty_plan`, `build_icl_text` and driver `build_prompt_from_cases`. Content selected for text is not newly inferred. Formatting can omit provenance, scope or other properties carried outside selected descriptions. Model interpretation of the formatted result is separate.

Concrete source deduction, without execution: for plan `{"plan":[{"id":1,"description":"Paris is in France","evidence":"source A"}]}`, `_parse_plan` returns the dictionary; `_pretty_plan` selects description and ID and produces `1. Paris is in France`. `build_icl_text("Q", plan)` produces `[CASE]\nQ\n[PLAN]\n1. Paris is in France`. The description is unchanged; the evidence field is omitted. Positive-example formatting likewise selects only IDs/descriptions. This is non-ampliative reshaping of selected descriptive text, not whole-object semantic preservation. The question argument `task_text` is not inserted into the formatter's returned prompt; the parametric query loop supplies the question separately.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted case/plan string or example prompt; malformed strings can fall back to literal text.
- Later read-back: Case JSONL is reformatted on later query retrieval; training reads pair JSONL separately. Current prompt strings need not themselves persist.
- Delegated visibility: Retriever/tokenizer sees selected case/plan text; planner sees capped positive/negative examples, with positive plans reduced to steps and negative plans shown raw.
- Selection predicate: Plan structure and description/desc/step priority; label partition and per-class caps in driver; configured use_plan in trainer.
- Invalidation or expiry: Recomputed from file data; no semantic-invalidity test in these formatters.
- Activation or effect: Text feeds numerical scoring or model guidance; behavioral dependence unobserved.
- Evidence limits: Arbitrary plan metadata can be consequential; no guarantee that all propositions or lineage survive. SRC-1 implementation, `memory/train_memory_retriever.py`, `memory/parametric_memory.py`, `client/parametric_memory_cbr.py`, `client/no_parametric_cbr.py`.

> desc = item.get("description") or item.get("desc") or item.get("step") or str(item)
> steps.append(f"{sid}. {desc}" if sid is not None else f"- {desc}")
> --- `memory/train_memory_retriever.py`

> parts = ["[CASE]", str(case)]
> if plan is not None:
>     pobj = _parse_plan(plan)
>     parts += ["[PLAN]", _pretty_plan(pobj) if pobj is not None else str(plan)]
> return "\n".join(parts).strip()
> --- `memory/parametric_memory.py`

#### EPI-RTE-search-import
Label: Search result acquisition

No counterpart after comparison with supplied runtime routes: crawl/extraction transforms a supplied page; these registered search tools acquire ranked search results. MCP caller → search provider → results/snippets → MCP caller. Operator/caller chooses query/provider; provider selects search results; Python limits/rekeys SearxNG results. Source warrant is unknown; URL identity is carried, not validated. SearxNG validates safety/time-range values and HTTP success, which check request/transport conditions, not snippet truth. SerpAPI code contains an empty API key; configured successful access is not established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Organic result dictionaries or SearxNG title/link/snippet dictionaries; SearxNG exceptions become a Search error entry.
- Later read-back: inapplicable — inspected functions do not retain a search corpus.
- Delegated visibility: Provider receives query/options; executor receives returned results, not independent verification.
- Selection predicate: Provider ranking; SearxNG takes first num_results.
- Invalidation or expiry: Current request data expire after consumption; no retained-claim revision here.
- Activation or effect: Returned text can guide executor within current task; no observed reliance.
- Evidence limits: Provider internals and live results excluded; neither freshness nor HTTP success licenses factual correctness. SRC-1 implementation, `server/search_tool.py`, `server/serp_search.py`.

> results = r.json().get("results", [])[: num_results]
> --- `server/search_tool.py`

> "title": it.get("title", ""),
> "link": it.get("url", ""),
> "snippet": it.get("content", ""),
> --- `server/search_tool.py`

#### EPI-RTE-media-answer
Label: Image and video interpretations

Distinct from [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction): input is visual/audio representation rather than page Markdown. Model components are see [RT-CMP-tool-judge-models](runtime.md#rt-cmp-tool-judge-models); this record owns returning generation wiring, not model identity. Image-to-text/image-QA → prepared image and text → remote vision call → answer text. Video-QA → keyframes and optional transcript → remote multimodal call → answer text. Generation relation is indeterminate: outputs may report visible facts or infer additional propositions; no concrete output establishes entailment or non-entailment. No independent semantic evaluator appears between these calls and their return.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stripped model text; missing video API key can return diagnostic text instead.
- Later read-back: inapplicable — inspected answer functions do not retain interpretations for later tasks.
- Delegated visibility: Image model receives prepared image/text; video model receives extracted frames and optional transcript, not full raw video. Caller receives answer text.
- Selection predicate: Caller question/media path and image system prompt; optional transcription flag; model interpretation.
- Invalidation or expiry: Current request messages are temporary; no correction/withdrawal mechanism inspected in return path.
- Activation or effect: Tool result becomes executor input when dispatched by client; actual use unobserved.
- Evidence limits: Keyframe selection, preprocessing and transcript fidelity unassessed; provider parameters unavailable. SRC-1 implementation, `server/image_tool.py`, `server/video_tool.py`.

> return response.choices[0].message.content.strip()
> --- `server/image_tool.py`

> frames = _extract_keyframes(video_path)
> images_b64 = _images_to_base64(frames)
> transcription = ""
> if use_audio_transcription:
>     transcription = await _transcribe_audio_async(_extract_audio(video_path))
> --- `server/video_tool.py`

#### EPI-RTE-math-result
Label: Python arithmetic tool results

No counterpart after comparison with supplied runtime routes: this registered returning computation differs from terminal command execution. MCP numeric arguments → Python arithmetic → return. Add/subtract and awaited `round` derive bounded Python numeric results given supplied operands, not truth of those operands as measurements. Important disconfirming source case: `multiply` and nonzero `divide` call global `round`, which is the later async definition, without await. Python name resolution therefore yields a coroutine object rather than the annotated numeric return before MCP serialization; dependency handling of that unexpected value is uninspected. `divide` explicitly rejects zero denominators. The implemented branch is not a reliable rounded arithmetic oracle across all tools.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numeric add/sub/awaited builtins.round result; multiply/divide return an unawaited coroutine on ordinary nonzero path; divide zero raises ValueError.
- Later read-back: inapplicable — tools retain no numerical history.
- Delegated visibility: Tool receives arguments; caller receives whatever MCP encodes from result or failure, not source-premise verification.
- Selection predicate: Called tool and operands; divide checks b == 0.
- Invalidation or expiry: Call-local arithmetic only; no retained claim to withdraw.
- Activation or effect: Numeric evidence can guide executor; actual invocation or serializer behavior unobserved.
- Evidence limits: Warrant is limited to Python numeric semantics; floating point is not exact real arithmetic and source operands remain unverified. SRC-1 implementation, `server/math_tool.py`.

> async def multiply(a: float, b: float, decimal_places: int = 2) -> float:
>     """Return a * b, rounded to *decimal_places* (default 2)."""
>     return round(a * b, decimal_places)
> --- `server/math_tool.py`

> async def round(a: float, decimal_places: int = 0) -> float:   # noqa: A001
>     """Round *a* to *decimal_places* (default 0)."""
>     return builtins.round(a, decimal_places)
> --- `server/math_tool.py`

### Claims

#### EPI-CLM-experience-learning
Label: Experience-driven transferable learning

No counterpart after comparison: runtime declares no CLM records. SRC-1, `README.md` supplies doctrine/design and reported benefit, not observed/causal evidence. It claims retained successful/failed trajectories and value retrieval enable transferable online continual learning. Assessment is in the comparison block; the implemented label proxy and latest-plan retention are narrower than causal value or full-trajectory reuse.

> **Learn from experiences, not gradients.** Memento logs successful & failed trajectories into a **Case Bank** and **retrieves by value** to steer planning and execution—enabling low-cost, transferable, and online continual learning.
> --- `README.md`

#### EPI-CLM-weight-updates
Label: No LLM weight updates

No counterpart after comparison with runtime Claims (none). SRC-1, `README.md` doctrine/design: an opening broad no-model-weight-update slogan is qualified by the explicit feature's no-LLM-weight-update wording. Source implementation permits separately trained retriever weights. Remote inference calls establish no client-issued LLM gradient update, not provider immutability.

> A memory-based, continual-learning framework that helps LLM agents improve from experience **without** updating model weights.
> --- `README.md`

> - **No LLM weight updates.** Memento reframes continual learning as **memory-based online reinforcement learning** over a **memory-augmented MDP**. A neural **case-selection policy** guides actions; experiences are stored and reused via efficient Read/Write operations.
> --- `README.md`

#### EPI-CLM-automated-retraining
Label: Automated collection and retraining

No counterpart after comparison with runtime Claims (none). SRC-1, `README.md` doctrine/design checklist claims automated training-data collection and model retraining. It is not inspectable evidence of a scheduled training/deployment loop; source of claimed automation is the checklist, and limits are supplied by [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) and boundary's missing-script finding.

> - [x] **Continual Learning Pipeline**: Automated training data collection and model retraining
> --- `README.md`
