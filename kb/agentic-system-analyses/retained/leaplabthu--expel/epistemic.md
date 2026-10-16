---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ExpeL epistemic routes: benchmark checks, trace-fed insight revision and later reliance without a separate insight acceptance gate."
run-id: AAS-2026-10-14-expel-efd908f05069-01
reviewed-boundary: e41ec9a24823e7b560c561ab191441b56d9bcefc
---

# ExpeL epistemic report

## Source-and-claim boundary

The question is whether experience-derived text becomes checked knowledge, or instead becomes operational guidance whose truth and transfer remain unestablished. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). The shipped benchmark loop, extraction drivers, prompts, maintenance and later consumers are included. Provider weights, external simulators, live Wikipedia and the WebShop server are outside the frozen source. Their responses and correctness cannot be established here. No execution corpus, generated rule payload, intervention or comparison is supplied: wiring does not establish operation or improvement.

Public knowledge-extraction and performance claims are [EPI-CLM-experience-knowledge](#epi-clm-experience-knowledge) and [EPI-CLM-learning-efficacy](#epi-clm-learning-efficacy). The prompt's requested generality is [EPI-CLM-general-insights](#epi-clm-general-insights). Pure advice can be non-truth-apt; a statement that an action strategy prevents a class of failures is truth-apt over that task class. Without generated content, the actual mixture is not determinable.

### Coverage

Direct reads below are implementation evidence except README and prompt instructions, which are doctrine/design. Supplied runtime evidence is explicitly distinguished. All paths are SRC-1.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Training dispatch and saving | `train.py` | Direct task-loop/save/summary read; construction and resume supplied by [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) and [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore) | No run or retained trajectory instance; exercised feedback unestablished |
| Extraction, resume and fold exclusion | `insight_extraction.py` | Complete direct read; [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [EPI-RTE-insight-proposal](#epi-rte-insight-proposal) | Driver exclusion is not proof of effective holdout in every extraction branch |
| Evaluation, cached rules, no_rules | `eval.py` | Complete direct read; [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context), [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore) | No supplied outcome comparison; no per-rule attribution |
| Acting, observation delivery, retry reflection | `agent/react.py`, `agent/reflect.py`, `agent/base.py` | Direct acting/formatting bodies and complete reflection/base reads; [RT-RTE-training-loop](runtime.md#rt-rte-training-loop), [EPI-RTE-source-acquisition](#epi-rte-source-acquisition) | Model-internal inference and actual response semantics uninspected |
| Trajectory classification, critic, parsing, updating, retrieval | `agent/expel.py` | Direct next_task, critique helpers, prompt dispatch, create_rules, insertion, complete retrieval and parser/updater bodies; new EPI routes below | Alternate critique helpers have dispatch gaps; do not infer a working universal critique interface |
| HotpotQA Search/Lookup/Finish | `envs/hotpotqa/hotpotqa.py`, `utils.py` | Complete adapter and normalize_answer/EM reads; [EPI-RTE-answer-check](#epi-rte-answer-check) | Key quality and external Docstore behavior uninspected |
| FEVER search, lookup, finish and label reward | `envs/fever/wikienv.py`, `envs/fever/wrappers.py` | Direct search/step/page-excerpt bodies and complete wrapper read; [EPI-RTE-source-acquisition](#epi-rte-source-acquisition), [EPI-RTE-answer-check](#epi-rte-answer-check) | Dataset labels and live page truth unvalidated; label match is not evidence verification |
| ALFWorld/WebShop outcome signals | `envs/alfworld/alfworld.py`, `envs/webshop/webshop.py` | Direct action/reward consumers; wider dispatch supplied by runtime; [EPI-RTE-answer-check](#epi-rte-answer-check) | External win/reward calculation excluded; no local certification of those objectives |
| Generic critique cleanup and history withdrawal | `agent/expel.py` | Direct task_critique, success_critique, failure_critique, prepare_new_eval; [EPI-RTE-critique-cleanup](#epi-rte-critique-cleanup) | No shipped consumer of cleaned critique dictionaries established; all_fail/all_reflection templates missing from generic mapping |
| Logs and plotted results | `tools/visualize_logs.py`, `utils.py` | Complete visualization driver, direct recompute_stats/plot_trial_stats bodies; [EPI-RTE-log-summary](#epi-rte-log-summary) | Other token/mean-score helper bodies not fully assessed; exact quantitative reporting not certified |
| Prompts and dispatch | `prompts/templates/human.py`, `README.md` | Complete direct reads; [EPI-CLM-general-insights](#epi-clm-general-insights) | Benchmark-specific examples/parsers supplied by runtime, not independently read in full; no system-complete negative about all shipped prompt content |
| Parametric models, embeddings, persistence | `models/llm.py`, `memory/__init__.py`, `agent/react.py`, `utils.py` | Supplied [RT-CMP-gpt-wrapper](runtime.md#rt-cmp-gpt-wrapper), [RT-CMP-embedder](runtime.md#rt-cmp-embedder), [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore) | Exact weights, external provenance and replay uninspected; no independent weight-warrant assessment |
| Task/reference data and static demonstrations | `data/`, `prompts/` | In boundary, but individual records/examples not inspected | Prevents exact source-quality and instance-level truth judgments; not evidence of absence |

The route search includes the CLI dispatch, exposed class operations and hooks. `ReactAgent.step` calls `BaseAgent.after_step(self)`, whose body is `pass`; the inspected ExpeL after_step also does nothing. Thus no additional operative feedback evaluator is established at that hook. Evaluation results are logged after acting and do not veto previously supplied rule content. This is a bounded account of those consumers, not a universal negative about dependency internals (SRC-1: `agent/react.py`, `agent/base.py`, `agent/expel.py`, `eval.py`).

> def after_step(self, *args, **kwargs) -> None:
>     pass
> --- `agent/base.py`

> BaseAgent.after_step(self)
> --- `agent/react.py`

## Epistemic-object inventory

Owned fields, including form and checks, are see the cited declaring records. Objects split natural-language rule content from symbolic counters because their consumers and authority differ.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-observation](#epi-obj-observation) | see record | see record | SRC-1 `agent/react.py` | see record |
| [EPI-OBJ-answer](#epi-obj-answer) | see record | see record | SRC-1 `envs/hotpotqa/hotpotqa.py` | see record |
| [EPI-OBJ-rule-items](#epi-obj-rule-items) | see record | see record | SRC-1 `agent/expel.py` | see record |
| [EPI-OBJ-rule-count](#epi-obj-rule-count) | see record | see record | SRC-1 `agent/expel.py` | see record |
| [EPI-OBJ-critiques](#epi-obj-critiques) | see record | see record | SRC-1 `agent/expel.py` | see record |
| [RT-CMP-gpt-wrapper](runtime.md#rt-cmp-gpt-wrapper) | not determinable from accessible weights | see record | SRC-1 `models/llm.py` | see record |
| [RT-CMP-embedder](runtime.md#rt-cmp-embedder) | no individuated propositions established in vectors | see record | SRC-1 `memory/__init__.py` | see record |
| [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) | Trial observations, thoughts and reflections; truth aptitude depends on actual text | see record | SRC-1 `agent/reflect.py` | No payload; outcome warrant does not propagate to every sentence |

## Authority-route ledger

The ledger is a sparse overlay: owned fields say see rather than reproduce canonical records. Multiple rows for a container separate checks from disposition and retention from integration. A linked EPI part owns its narrower fields. Architectural status is assessed here from inspected code and supplied implementation passages.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-source-acquisition](#epi-rte-source-acquisition) | content transformation | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `envs/fever/wikienv.py` | none | none | see record |
| [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Candidate answers/diagnoses only; outcome does not license explanation | see record | see record | SRC-1 `agent/reflect.py` | [EPI-CLM-experience-knowledge](#epi-clm-experience-knowledge) | Actual reflection semantics unknown | see record |
| [EPI-RTE-answer-check](#epi-rte-answer-check): HotpotQA | check/evidence production | implemented | see record | see HotpotQA relation in record | see HotpotQA target in record | see HotpotQA evaluator in record | see record | see record | see record | see HotpotQA license in record | see record | see record | SRC-1 `envs/hotpotqa/hotpotqa.py` | none | none | see record |
| [EPI-RTE-answer-check](#epi-rte-answer-check): FEVER | check/evidence production | implemented | see record | see FEVER relation in record | see FEVER target in record | see FEVER evaluator in record | see record | see record | see record | see FEVER license in record | see record | see record | SRC-1 `envs/fever/wrappers.py` | none | none | see record |
| [EPI-RTE-answer-check](#epi-rte-answer-check): ALFWorld | check/evidence production | implemented | see record | see ALFWorld relation in record | see ALFWorld target in record | see ALFWorld evaluator in record | see record | see record | see record | see ALFWorld license in record | see record | see record | SRC-1 `envs/alfworld/alfworld.py` | none | none | see record |
| [EPI-RTE-answer-check](#epi-rte-answer-check): WebShop | check/evidence production | implemented | see record | see WebShop relation in record | see WebShop target in record | see WebShop evaluator in record | see record | see record | see record | see WebShop license in record | see record | see record | SRC-1 `envs/webshop/webshop.py` | none | none | see record |
| [EPI-RTE-outcome-disposition](#epi-rte-outcome-disposition) | disposition/acceptance | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/expel.py` | none | none | see record |
| [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | Retained trial is evidence of a classified outcome, not accepted rationale | see record | see record | SRC-1 `train.py` | none | none | see record |
| [EPI-RTE-insight-proposal](#epi-rte-insight-proposal) | content transformation | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/expel.py` | [EPI-CLM-general-insights](#epi-clm-general-insights) | see record | see record |
| [EPI-RTE-syntax-check](#epi-rte-syntax-check) | check/evidence production | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/expel.py` | none | none | see record |
| [EPI-RTE-counter-disposition](#epi-rte-counter-disposition) | disposition/acceptance | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/expel.py` | [EPI-CLM-general-insights](#epi-clm-general-insights) | see record | see record |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | retention | implemented | [EPI-OBJ-rule-items](#epi-obj-rule-items) | no content change | see record | see record | see record | see record | see record | No per-rule accepted truth established | see record | see record | SRC-1 `insight_extraction.py` | none | Retention is not lifecycle integration | see record |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | lifecycle integration | no route found within boundary | [EPI-OBJ-rule-items](#epi-obj-rule-items) | no content change | Accepted insight-to-evidence connection | No per-rule evidence-consuming acceptance found in create_rules/parser/updater/cache load | Extraction and reuse | No separate accepted-claim integration found | No such gate | No accepted ampliative product established | Operational use can occur without it | Next critic/actor can read retained text; see [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting) | SRC-1 `agent/expel.py` | [EPI-CLM-experience-knowledge](#epi-clm-experience-knowledge) | Knowledge wording exceeds established warrant | Narrow search boundary, not absence of model-internal checking |
| [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context) | operational admission/selection/consumption | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Similarity/length grant no truth license | see record | see [RT-BAP-fewshots-acting](runtime.md#rt-bap-fewshots-acting) | SRC-1 `agent/expel.py` | [EPI-CLM-experience-knowledge](#epi-clm-experience-knowledge) | Shipped examples and acquired traces mixed | see record |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | behavior/policy adaptation | implemented | [EPI-OBJ-rule-items](#epi-obj-rule-items) | non-truth-apt policy/content update: imperative tips can change guidance without asserting truth | see record | see record | see record | see record | see record | No new proposition required for this edge | see record | see [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting) | SRC-1 `prompts/templates/human.py` | [EPI-CLM-learning-efficacy](#epi-clm-learning-efficacy) | Benefit unobserved | Actual advice/claim mixture unknown |
| [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore) | lineage/freshness/recovery | implemented | see record | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Source warrant unknown; loader does not revalidate truth | see record | see record | SRC-1 `utils.py` | none | Bypasses critique/parser admission | see record |
| [EPI-RTE-critique-cleanup](#epi-rte-critique-cleanup) | content transformation | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/expel.py` | none | see record | see record |
| [EPI-RTE-log-summary](#epi-rte-log-summary) | check/evidence production | implemented | see record | see record | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `utils.py` | [EPI-CLM-learning-efficacy](#epi-clm-learning-efficacy) | see record | see record |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-experience-knowledge](#epi-clm-experience-knowledge) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-training-loop](runtime.md#rt-rte-training-loop), [EPI-RTE-insight-proposal](#epi-rte-insight-proposal), [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context), [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting) | None supplied | Delivery is not dependence; generalized rules not independently accepted | Experience gathering, extraction requests and later context supply are wired | Knowledge understood as warranted general claims is not established |
| [EPI-CLM-learning-efficacy](#epi-clm-learning-efficacy) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [EPI-RTE-log-summary](#epi-rte-log-summary) | None supplied; README is attributed assertion only | No intervention/comparison; component effects cannot be inferred; log parser differs from reward predicate | Improvement-directed retained policy change is afforded; successful learning unestablished | No empirical efficacy conclusion from source code |
| [EPI-CLM-general-insights](#epi-clm-general-insights) | see record | SRC-1 `prompts/templates/human.py`, doctrine/design | see record | [EPI-RTE-insight-proposal](#epi-rte-insight-proposal), [EPI-RTE-syntax-check](#epi-rte-syntax-check), [EPI-RTE-counter-disposition](#epi-rte-counter-disposition) | None supplied | Finite trace contrast does not entail future transfer; updater has no semantic veto | Generality and failure avoidance are requested, not enforced | Counters are retention preferences, not calibrated evidence of truth |

## Bounded conclusion

ExpeL imports task observations, proposes answers and diagnoses, and checks benchmark outcomes. HotpotQA licenses normalized answer-key equality; FEVER licenses normalized label equality; ALFWorld and WebShop import external win/full-reward judgments. These results control continuation and trajectory classification. They do not validate the acting rationale, reflection, evidence-verification process, generalized insight, replay safety or transfer ([EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-outcome-disposition](#epi-rte-outcome-disposition)). Wikipedia acquisition supplies excerpts, not independently endorsed facts; source warrant remains unknown and FEVER excerpts lose surrounding text ([EPI-RTE-source-acquisition](#epi-rte-source-acquisition)).

Stored success/failure traces prompt rule revision. Generalizing from finite trials to future tasks is requested ampliation, not entailment; actual generated propositions and whether the model makes that extension are uninspected. Parser checks and counter updates admit, rank, edit and withdraw rule text. They grant operational reliance through subsequent critic inputs and acting prompts, not a recorded per-rule acceptance against a truth or transfer criterion. Retention/cache formatting and example retrieval do not close that gap. No accepted ampliative claim or post-acceptance lifecycle integration is established in these inspected paths ([EPI-RTE-insight-proposal](#epi-rte-insight-proposal), [EPI-RTE-syntax-check](#epi-rte-syntax-check), [EPI-RTE-counter-disposition](#epi-rte-counter-disposition), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)).

Checks are consequential but heterogeneous. Rule suggestions reach the actor as interpretive references, or FEVER's stronger prompt wording, not a programmatic action veto. Counters enforce membership and ordering; embedding/length filters select demonstrations, not truths. Cached or restored content can bypass extraction entirely. `no_rules` disables rule guidance without necessarily disabling examples. These are separate authority paths and horizons ([RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting), [RT-BAP-fewshots-acting](runtime.md#rt-bap-fewshots-acting), [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore)).

A direct policy-adaptation route exists even if a retained rule is merely an imperative. Trial representations feed later reflection and critique requests, localized rule units are revisable, and revised text feeds further critique and later tasks. These support implemented feedback and iteration, not observed content-directed criticism, decision dependence or improved capacity. The supplied runtime's independent theory-builder, reflection and self-improvement limits remain see [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) and [RT-RTE-training-loop](runtime.md#rt-rte-training-loop). Dispositional improvement-directed self-change does not establish exercised or successful self-improvement. Neither model has an inspected parameter-update route; opaque weights do not justify a verdict about all learning ([RT-CMP-gpt-wrapper](runtime.md#rt-cmp-gpt-wrapper), [RT-CMP-embedder](runtime.md#rt-cmp-embedder)).

Two additional limits matter. Generic critique cleanup can remove meaning-bearing parentheses, and some exposed critique modes lack a matching shipped template. Log summaries can count WebShop score-marker text as success without checking the numerical full-reward criterion. Neither cleaned critique retention nor a plotted summary supplies an independent knowledge acceptance decision ([EPI-RTE-critique-cleanup](#epi-rte-critique-cleanup), [EPI-RTE-log-summary](#epi-rte-log-summary)). Effective fold holdout also requires insertion-order task indices to match task IDs in the success-group branch; driver exclusion alone is insufficient ([EPI-RTE-insight-proposal](#epi-rte-insight-proposal)). No single system-wide epistemic verdict follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-observation
Label: Environment observation text

Source-native identity: `observation`, then `observation_history` in `ReactAgent.step`. Form: natural language; substrate: environment state, prompt messages, later trajectory/checkpoint text. Candidate truth-apt content: Wikipedia excerpts, environment descriptions and outcome statements; error/status messages and task instructions have different roles. Claimed role: acting evidence and later experience. Source warrant is unknown; status reports license their named adapter domain only. Different from model parameters and contained trial records: closest supplied [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) is a route, not this text object. Evidence: SRC-1 `agent/react.py`, `envs/fever/wikienv.py`; see [EPI-RTE-source-acquisition](#epi-rte-source-acquisition) for passages.

#### EPI-OBJ-answer
Label: Benchmark answer text

Source-native identity: `self.answer` in QAEnv and WikiEnv. Form: natural-language answer or FEVER label string; substrate: adapter state and logged Finish action. Candidate truth-apt content: answer to a question or label about the supplied claim. Exact propositions depend on missing task/output instances. Claimed role: terminal benchmark answer. Closest [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) spans the producing/consuming process rather than this part. Source: SRC-1 `envs/hotpotqa/hotpotqa.py`, `envs/fever/wikienv.py`; check passages are in [EPI-RTE-answer-check](#epi-rte-answer-check).

#### EPI-OBJ-rule-items
Label: Natural-language rule items

Source-native identity: `rule_items`, `rules`, text projection of `rule_items_with_count`, `cache_rules`. Form: natural language with symbolic numbering; substrate: lists, formatted strings and pickle checkpoints. Claimed role: reusable general insights and acting references. Candidate truth-apt content: any causal/predictive assertions about future task performance; imperative tips need not be truth-apt. Actual text mixture is not determinable without generated artifacts. Distinct from counter part [EPI-OBJ-rule-count](#epi-obj-rule-count); closest supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) is the containing process, not a duplicate object. Source: SRC-1 `agent/expel.py`, `prompts/templates/human.py`; passages in [EPI-RTE-insight-proposal](#epi-rte-insight-proposal), [EPI-RTE-counter-disposition](#epi-rte-counter-disposition).

#### EPI-OBJ-rule-count
Label: Rule retention counters

Source-native identity: second tuple element of `rule_items_with_count`. Form: symbolic integers and ordered tuples; substrate: Python lists and saved dictionaries. No truth-apt knowledge claim is established by a counter itself: it is an updater-controlled retention preference, not calibrated probability. Claimed role: importance/order and removal control. Distinct from the interpreted rule text; closest supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) is the process using both parts. Source: SRC-1 `agent/expel.py`; updater passage in [EPI-RTE-counter-disposition](#epi-rte-counter-disposition).

#### EPI-OBJ-critiques
Label: Cleaned critique dictionaries

Source-native identity: `critiques`, `all_success_critiques`, `all_fail_critiques`. Form: natural-language lists keyed by task/group; substrate: agent dictionaries potentially saved by type-filtered checkpoints. Candidate truth-apt content: proposed diagnoses/tips, not determinable without outputs. Claimed role: critiques of trials; these dictionaries are distinct from the create_rules operation stream and retained rule pool. Closest [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) overlaps critic invocation but not these cleaned outputs. Source: SRC-1 `agent/expel.py`; evidence in [EPI-RTE-critique-cleanup](#epi-rte-critique-cleanup).

### Routes

#### EPI-RTE-source-acquisition
Label: Environment evidence acquisition
Part of: [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)

Endpoints: benchmark search/lookup or action → adapter observation → `ReactAgent.step` formatting → model history. Owner: actor selects action, adapter/program extracts text. Context/state: current page/session, task and accumulated observations. Effects: candidate evidence enters acting and later logged trajectories. Content/update relation: truth-apt transformation: acquisition/import. Source warrant unknown; FEVER truncation degrades context without independently checking truth. HotpotQA delegates search/lookup to DocstoreExplorer; ALFWorld/WebShop import external state reports. Material coverage also overlaps [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context), which is the evaluation consumer rather than the acquisition part.

- Immediate return: Adapter returns observation and status tuple; step formats the text into messages.
- Later read-back: Training logs/trajectories can later supply observation text to critique/retrieval; see supplied training and evaluation records.
- Delegated visibility: inapplicable — no worker handoff; external service supplies observations.
- Selection predicate: Actor action grammar and adapter search/lookup/page logic; FEVER returns the first five normalized sentences on search.
- Invalidation or expiry: Environment/task reset replaces current page/session and prompt frame; retained trials can survive.
- Activation or effect: Text delivery is implemented; altered action due to acquired facts is uninspected.
- Evidence limits: Live responses, source quality, exact extraction fidelity and actual factual inference are not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Check target/evaluator: no independent truth check on imported page text in these bodies. Epistemic license: acquired excerpt with unknown source warrant, not endorsement. Operational authority/path: model history, advisory evidence, later acting call; trajectory consumer can reuse it across tasks. SRC-1 `envs/fever/wikienv.py`, `agent/react.py`, `envs/hotpotqa/hotpotqa.py`.

> return ' '.join(sentences[:5])
> --- `envs/fever/wikienv.py`

> observation_history, operation = self.observation_formatter(observation, step=self.curr_step)
> if operation == 'append':
>     self.prompt_history.append(observation_history)
> --- `agent/react.py`

#### EPI-RTE-answer-check
Label: Benchmark outcome checks
Part of: [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)

Endpoints: proposed answer or external action outcome → benchmark predicate → Boolean reward/success. Owner: adapter and imported evaluator. This part produces results; [EPI-RTE-outcome-disposition](#epi-rte-outcome-disposition) separately consumes them. It also runs under [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context). Content/update relation for HotpotQA, FEVER and WebShop: truth-apt transformation: entailed derivation, narrowly the Boolean result of the specified equality given its inputs, not truth of those inputs. ALFWorld relation: truth-apt transformation: acquisition/import of external win judgment, source warrant unknown.

Targets/domains: QA answer string against supplied key via normalized EM; FEVER answer label against dataset label via normalized equality; ALFWorld task completion via external `info['won'][0]`; WebShop session outcome via externally supplied reward equal to 1. QA/FEVER are local comparison programs using reference outcomes; other criteria are external with local Boolean consumption. Context/state: answer/key, wrapper info, environment/session reward. Possible result: success or nonsuccess, not a proof of reasoning or rule generality. Timing: adapter steps and is_success consumers. License: exact checked benchmark criterion, no process/transfer warrant. Path/force: reward and success predicate → agent continuation/classification, enforcing selection for the current attempt; downstream trajectory consequences are separately declared.

- Immediate return: Reward/success Boolean, with terminal observations reflecting some outcomes.
- Later read-back: Recorded classification and terminal text can enter retained trials and summaries; the check itself does not save a separate proof.
- Delegated visibility: inapplicable — evaluator services are not delegated workers.
- Selection predicate: Finish answer equality for QA/FEVER or adapter-provided win/full reward for interactive tasks.
- Invalidation or expiry: New task/reset supplies new answer or reward state; prior recorded outcomes remain in histories.
- Activation or effect: Predicate is wired into acting/retry/classification; no executed outcome supplied.
- Evidence limits: Reference quality and external win/reward computation uninspected; no candidate answer instance checked here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Computational evaluation follows model proposal; humans configure tasks, not ordinarily approve each answer. Testing can supply text via input. Operating mode is bounded benchmark curriculum/evaluation. Source: SRC-1 `envs/hotpotqa/hotpotqa.py`, `envs/fever/wrappers.py`, `envs/alfworld/alfworld.py`, `envs/webshop/webshop.py`, `utils.py`.

> return normalize_answer(answer) == normalize_answer(key)
> --- `utils.py`

> label = normalize_answer(self.data[self.data_idx][1])
> pred = normalize_answer(info['answer'])
> if label == pred:
>   return 1
> --- `envs/fever/wrappers.py`

> observation, reward, done = process_observation(observation[0]), info['won'][0], done[0]
> --- `envs/alfworld/alfworld.py`

> self.reward = (reward==1)
> --- `envs/webshop/webshop.py`

#### EPI-RTE-outcome-disposition
Label: Outcome-based trajectory disposition
Part of: [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)

Endpoints: success predicate and trial completion state → next_task history branches → successful/failed experience pools. Owner: Python; model does not veto classification. Context/state: current task, increment_task, mode and Trajectory. Content/update relation: no content change; classification/admission of a trial is not acceptance of all its claims. Criterion/intended use/scope: successful benchmark attempt selected as successful experience for training extraction and later demonstration; retry failure is recorded as failure. Epistemic license: benchmark outcome classification only. Operational authority/path: success/failure dictionaries → critic comparison or retrieval, enforcing selection across extraction rounds and later evaluation. Trigger: training next_task after an attempt; mode and retry state gate admission. Evaluation bypasses this training route. Recovery remains checkpoint-based, not semantic rollback. Source: SRC-1 `agent/expel.py`; closest supplied route is the containing loop.

- Immediate return: Dictionary append/update then ReflectAgent.next_task control progression.
- Later read-back: Extraction reads successes/failures; evaluation retrieves success histories and shipped examples.
- Delegated visibility: inapplicable — no delegated worker.
- Selection predicate: Training mode; increment_task plus is_success selects success, otherwise failed history.
- Invalidation or expiry: No per-claim invalidation; prepare_new_eval can clear both history dictionaries, while separate snapshots can preserve old content.
- Activation or effect: Classifications alter input pools and later selection, without truth approval of trial prose.
- Evidence limits: No supplied trajectory corpus; classification accuracy outside named criteria unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.increment_task:
>     if self.is_success():
>         self.succeeded_trial_history[self.task].append(trajectory)
>     else:
>         self.failed_trial_history[self.task].append(trajectory)
> --- `agent/expel.py`

#### EPI-RTE-insight-proposal
Label: Trial-conditioned insight proposals
Part of: [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)

Endpoints: selected traces plus existing rules → critique prompt → GPTWrapper or testing input → operation text. Owner: driver/code selects inputs, model proposes edits; no per-rule human veto in ordinary execution. Context: success/failure pair, task, existing numbered rules, or grouped successful first trials. Content/update relation: truth-apt transformation: indeterminate for actual outputs. Requested generalization is ampliative: finite observed attempts cannot entail that a strategy avoids similar failures on different questions. Remaining actual classifications are imperative policy tips, reshaping, entailed claims within the trial, or ampliative assertions; generated outputs and their input linkage are needed to decide. No failure to prove entailment is treated as proof of conjecture.

Evaluator: critic's prompted interpretation over supplied trials/rules; no separate rule oracle. Timing: extraction and optional evaluation fold extraction; next proposal sees current revised rules. Possible result: ADD/EDIT/REMOVE/AGREE requests. Force: candidate-generation authority, downstream parser/updater decides admitted operations. Epistemic license: none beyond candidate provenance. Path: operation text → parser/updater; model-interpreted trace evidence and guidance are advisory at proposal, then symbolic admission grants retention. Guidance asks high-level general insights and future failure avoidance; actual criticism/blame and truth-apt products unobserved. Theory properties remain separately bounded by [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission).

Needed qualification beside supplied runtime finding: the driver excludes eval IDs, but the create_rules success-group branch uses `enumerate(self.succeeded_trial_history)` positions, not `task2idx`. Holdout is effective there only if insertion order matches task IDs. Restored/custom dictionaries can violate that assumption; no observed leakage is claimed. The compare branch does use idx2task. This qualifies the runtime's unconditional held-out-ID wording without changing its route identity. Source: SRC-1 `agent/expel.py`, `insight_extraction.py`, `eval.py`, `prompts/templates/human.py`.

- Immediate return: Critic response text and extraction log entries.
- Later read-back: Accepted symbolic operations alter rules which enter next critic prompt and later actor prompts; raw output also enters extraction logs.
- Delegated visibility: inapplicable — synchronous critic invocation, not worker delegation.
- Selection predicate: Included training task success/failure comparisons, then success groups; insertion-order caveat above.
- Invalidation or expiry: Fresh extraction clears working rules; resume restores fields; no automatic semantic regression rollback.
- Activation or effect: Proposals reach parser/updater; actual content and behavior change uninspected.
- Evidence limits: No response payload, acceptance evidence or controlled transfer comparison supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for idx, task in enumerate(self.succeeded_trial_history):
>     if idx in training_ids and len(self.succeeded_trial_history[task]) > 0:
>         all_success.append((task, self.succeeded_trial_history[task][0].trajectory))
> --- `agent/expel.py`

> existing_rules=rule_items,
> reflections=reflections,
> task=task,
> --- `agent/expel.py`

#### EPI-RTE-syntax-check
Label: Rule protocol checks
Part of: [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)

Endpoints: critic response → parse_rules recognized operations → update_rules preliminary duplicate/index filtering. Owner/evaluator: deterministic Python regex and string/index rules. Target/domain: operation protocol, nonempty terminal-period text, banned uppercase strings and selected existing-text/index relations. Not the truth, generality or future efficacy of a rule. Content/update relation: truth-apt transformation: non-ampliative reshaping for admitted text selection; no truth inference. Timing: before application. Possible results: omit malformed operations, convert a matching EDIT to AGREE, pass remaining operations. License: bounded protocol eligibility, not complete safety or semantic validity. Path/force: filtered operation list → updater, enforcing which changes are attempted. Humans can supply test response strings but do not independently assess truth in this check. Source: SRC-1 `agent/expel.py`; evidence and broader limitations also see parent.

- Immediate return: Recognized and filtered operation tuples.
- Later read-back: inapplicable — this check retains no independent artifact; applied output can persist through the separate disposition route.
- Delegated visibility: inapplicable — local Python computation.
- Selection predicate: Regex operation recognition, period/nonempty/banned-word test, substring duplicate and some index conditions.
- Invalidation or expiry: inapplicable — eligibility computed per proposal, no expiring approval.
- Activation or effect: Can block operations or convert EDIT to AGREE; not an independent truth veto.
- Evidence limits: Zero/negative/index edge cases not certified; prompt operation-count limits are not enforced here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if text != '' and not any([w in text for w in banned_words]) and text.endswith('.'):
> --- `agent/expel.py`

> parsed_operations = parse_rules(llm_output)
> --- `agent/expel.py`

#### EPI-RTE-counter-disposition
Label: Counter-mediated rule disposition
Part of: [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)

Endpoints: filtered operations and text/counters → ordered updated rule pool → numbered rules/cache. Owner: Python enacts model proposals. Target: pool membership, replacement and retention priority, not a truth criterion. Content/update relation: non-truth-apt policy/content update: symbolic retention counters and rule membership change; the semantic content edge of inserted/replaced text is separately indeterminate in [EPI-RTE-insight-proposal](#epi-rte-insight-proposal). Timing: each critique round. Possible result: ADD starts at 2; AGREE increments; EDIT replaces text and increments; REMOVE decrements by 1 or 3 when list_full; nonpositive counters disappear; remaining rules sort descending. Force: enforcing membership/order. Epistemic license: no independently accepted rule claim; counter agreement is not independent evidence. Operational authority/path: next critic receives pool, later actor receives formatted rule text via [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting), interpretive guidance across rounds/tasks/processes. Removing a rule withdraws future pool delivery, not retroactive correction of previous actions or saved snapshots. Trigger/proposal/guidance are see parent and proposal part; code can reject protocol failures, not independently falsify meaning. Checkpoints permit caller recovery; no automatic performance-regression rollback established. Source: SRC-1 `agent/expel.py`.

- Immediate return: Sorted positive-counter rule tuples, then text projection and cache updates.
- Later read-back: Next critique receives rules; saved/cached rules can reach later acting calls.
- Delegated visibility: inapplicable — synchronous local updater.
- Selection predicate: Fixed REMOVE, AGREE, EDIT, ADD order and counter greater than zero retention.
- Invalidation or expiry: Counter depletion withdraws pool membership; fresh extraction resets; no time-based truth expiry.
- Activation or effect: Text and priority can change delivered guidance; actual compliance/benefit uninspected.
- Evidence limits: No actual rule history supplied; no held-out per-rule criterion before use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> rules = [rules[i] for i in range(len(rules)) if rules[i][1] > 0] # remove rules when counter reach 0
> rules.sort(key=lambda x: x[1], reverse=True)
> --- `agent/expel.py`

> rules.append((operation_rule_text, 2))
> --- `agent/expel.py`

#### EPI-RTE-critique-cleanup
Label: Generic critique text cleanup

Distinct from [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission): task_critique/success_critique/failure_critique populate critique dictionaries rather than applying rule operations. Shared model/prompt infrastructure is possible overlap, not identity. Endpoints: generic critic output → split/parenthesis removal/empty filtering → critique dictionaries. Owner: model proposes, code transforms and retains. Context: stored successes/failures; failure_critique can omit one trajectory under a token-pressure strategy. Content/update relation: truth-apt transformation: indeterminate because qualifier deletion need not preserve semantics. Deterministic witness, not execution: an output `Use Search (only for named entities).` becomes `Use Search .` through the regex substitution and strip calls. If parentheses encode a scope condition, removing them broadens the instruction; if they are formatting, it merely reshapes. This is a concrete deduction from inspected implementation, not an observed generated claim.

Prompt-dispatch limit: these helpers request compare/all_success/all_fail without existing_rules. The supplied generic HUMAN_CRITIQUES mapping contains only compare_existing_rules and all_success_existing_rules. Ordinary driver injection therefore does not establish runnable generic helper calls; `_build_critique_prompt` directly indexes the missing key. all_reflection is also selected when reflections are passed and lacks a generic mapping entry. A custom caller can supply templates, so this is not absent architectural capacity. Source: SRC-1 `agent/expel.py`, `prompts/templates/human.py`. No later consequential reader of the cleaned dictionaries is established in the inspected shipped drivers; saving text alone grants no operative warrant. prepare_new_eval clears histories, not an independent semantic rejection decision.

- Immediate return: task_critique optionally returns a log; helpers update critique dictionaries if prompt dispatch succeeds.
- Later read-back: Potential checkpoint retention; no shipped decision consumer of these cleaned dictionary contents established in inspected train/extract/eval bodies.
- Delegated visibility: inapplicable — model call, not worker delegation.
- Selection predicate: Trial availability; success subsets or more than one failure; empty cleaned entries removed.
- Invalidation or expiry: success/failure critique dictionaries can be reset; cleanup discards parenthetical material with no restoration pointer.
- Activation or effect: Transformed text is retained, but consequential use is unestablished; shipped template dispatch can block production.
- Evidence limits: No outputs; helper operation and truth-apt semantics unobserved; implementation body does not establish successful entry via default mapping.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> pattern = r"\s*\([^()]*\)"
> self.critiques[task] = [re.sub(pattern, '', critique).strip().strip('- ') for critique in self.critiques[task]]
> --- `agent/expel.py`

> HUMAN_CRITIQUES = dict(
>     compare_existing_rules=human_existing_rules_critique,
>     all_success_existing_rules=human_all_success_existing_rules_critique,
> )
> --- `prompts/templates/human.py`

#### EPI-RTE-log-summary
Label: Log-derived outcome summaries

Distinct from [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) and [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context): this is the later reporting path, not the environment evaluator or state-admission branch. Endpoints: parsed log last-step text → recompute_stats → plot_trial_stats → printed/saved result summaries. Owner/evaluator: Python substring rules over benchmark logs. Target/domain: textual success/fail/halted categorization per trial. Content/update relation: truth-apt transformation: entailed derivation of counts under the parser's predicates, not necessarily true benchmark success counts. Timing: end-of-driver run or visualization invocation. Force/path: report/plot and log writer, informational to operator over recorded trials; no inspected automatic rule veto or rollback consumer. License: bounded text classification only.

Concrete deduction: for WebShop a last step containing `Your score: 0.5` satisfies the `Your score` test and increments success, whereas the adapter admits success only when numerical reward equals 1. Thus the summary is not a second independent task validator. Actual occurrences, aggregate accuracy and reported improvement are unobserved. Source: SRC-1 `utils.py`, `tools/visualize_logs.py`, `train.py`, `eval.py`, `envs/webshop/webshop.py`.

- Immediate return: Count dictionary then per-trial result lists/plots.
- Later read-back: Drivers append result strings to logs; visualization reads saved logs; no downstream admission based on summary established.
- Delegated visibility: inapplicable — local report computation.
- Selection predicate: Selected last trajectory/last line and benchmark-specific substrings; fixed dataset-length assertions in plotting.
- Invalidation or expiry: Recompute on supplied log; no content-level correction or expiry of prior summaries implemented here.
- Activation or effect: Results are displayed and appended to logs; no automatic behavioral-policy force established.
- Evidence limits: No log corpus; other reporting helpers not fully audited; no intervention/comparison evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if ': 1.0' in last_step or 'Your score' in last_step:
>     stats["success"] += 1
> --- `utils.py`

> stats = recompute_stats(parsed_result, benchmark, i)
> --- `utils.py`

### Claims

#### EPI-CLM-experience-knowledge
Label: Experience-derived knowledge and recall

Claimed operation: autonomous experience gathering, natural-language knowledge extraction and recall for informed decisions. Source: SRC-1 `README.md`, doctrine/design. No counterpart among supplied runtime Claims (none declared); distinct from runtime wiring findings. Claimed knowledge warrant is not specified as a per-claim acceptance contract.

> Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions.
> --- `README.md`

#### EPI-CLM-learning-efficacy
Label: Robust learning efficacy

Claimed operation: consistent performance enhancement with accumulated experience, attributed to empirical results. Source: SRC-1 `README.md`, doctrine/design assertion about results, not supplied observed/causal experiment. Distinct from preceding operation claim and no supplied runtime claim counterpart.

> Our empirical results highlight the robust learning efficacy of the ExpeL agent, indicating a consistent enhancement in its performance as it accumulates experiences.
> --- `README.md`

#### EPI-CLM-general-insights
Label: Generally applicable future insights

Claimed operation: revise rules into general high-level critiques useful for different future questions. Source: SRC-1 `prompts/templates/human.py`, doctrine/design requested behavior. This is a normative model instruction, not observed generality. Distinct from public efficacy and recall claims; no supplied runtime claim counterpart.

> By examining and contrasting to the successful trial, and the list of existing rules, you can perform the following operations: add, edit, remove, or agree so that the new list of rules is GENERAL and HIGH LEVEL critiques of the failed trial or proposed way of Thought so they can be used to avoid similar failures when encountered with different questions in the future. Have an emphasis on critiquing how to perform better Thought and Action. Follow the below format:
> --- `prompts/templates/human.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
