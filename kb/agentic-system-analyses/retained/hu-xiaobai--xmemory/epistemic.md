---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "xMemory epistemic routes: conversation-derived candidates, comparison extraction, admission, hierarchy selection and offline answer scoring."
run-id: AAS-2026-10-15-xmemory-b9a2b9f58eda-01
reviewed-boundary: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
---

# xMemory epistemic report

## Source-and-claim boundary

This report asks which conversation-derived propositions xMemory produces or acquires, what checks license reliance, and how results reach later behavior. The functional scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, with README performance statements only reported operation. There is no registered observed run or causal experiment. No target execution was performed.

The relevant public claims are [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose) and [EPI-CLM-faithful-hierarchy](#epi-clm-faithful-hierarchy). Provider internals, immutable weights, external paper results and release memories are excluded or unavailable as specified by boundary. This prevents conclusions about provider truthfulness, exact parameter provenance, paper-wide results and prebuilt-memory quality. Missing runs prevent activation and benefit conclusions, not source-wiring conclusions.

| Entry point or operation | Source path under SRC-1 | Coverage and evidence basis | Limit / prevented conclusion |
|---|---|---|---|
| Public add, flush, wait, search, async search and maintenance | `src/api/facade.py` | Direct signature/dispatch inspection and supplied [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission), [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search), [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) | Facade does not automatically execute the construction driver's entire maintenance loop. |
| Dataset admission and forced flush | `evaluation/locomo/add.py` | Supplied [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) | Input speech is not independently authenticated world truth. |
| Episode formatting, validation and fallback | `src/generation/episode_generator.py` | Direct essential-field/cleanup inspection; supplied [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission); new [EPI-RTE-episode-normalization](#epi-rte-episode-normalization) | Model semantic fidelity unobserved. |
| Prediction, comparison extraction and cold start | `src/generation/prediction_correction_engine.py`, `src/generation/prompts.py` | Direct inspected prediction, comparison, cold-start and conversion; [EPI-RTE-comparison-extraction](#epi-rte-comparison-extraction) | No instances establish produced entailment or successful criticism. |
| Alternate per-episode extraction | `src/generation/semantic_generator.py` | Supplied [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission); direct fallback prompt read | Alternate output semantics unobserved. |
| Semantic deduplication, saving and index failure | `src/core/memory_system.py` | Direct [EPI-RTE-duplicate-check](#epi-rte-duplicate-check), [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition), [EPI-RTE-semantic-retention](#epi-rte-semantic-retention) | Similarity rejection is not truth adjudication. |
| Theme summaries, structural maintenance and graph | `src/core/memory_hierarchy.py`, `src/core/memory_system.py` | Direct orchestration, local clustering, summary recomputation and summary-prompt inspection; supplied [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) | All split/merge objective internals not exhaustively inspected; prevents full numerical/fidelity audit. |
| Baseline, lightweight and alternate ranking | `src/core/lightweight_search_system.py`, `src/core/memory_system.py` | Supplied [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search) | Individual ranking backend internals not exhaustively inspected; no complete ranking-quality verdict. |
| CLI strategy, adaptive scoring, hydration and final answer | `evaluation/locomo/xMemory_search_framework.py` | Direct CLI dispatch search; supplied [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) | Full KV/cache internals not directly inspected; prevents numerical-equivalence conclusion. |
| Owner deletion and cache cleanup | `src/core/memory_system.py` | Direct [EPI-RTE-owner-deletion](#epi-rte-owner-deletion) | No universal withdrawal across reader caches or in-flight tasks established. |
| Offline evaluation and aggregation | `evaluation/locomo/evals.py`, `evaluation/locomo/metrics/utils.py`, `evaluation/locomo/generate_scores.py` | Direct evaluator and aggregation reads; [EPI-RTE-lexical-evaluation](#epi-rte-lexical-evaluation) | Scores do not consume causal comparisons or trigger memory revision. |
| Host injection and model/provider loading | `src/utils/llm_client_openllm.py`, `src/services/providers.py` | Supplied [RT-RTE-provider-admission](runtime.md#rt-rte-provider-admission), [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client) | Injected Python and external model internals are not covered by default-route conclusions. |

The CLI search confirms `baseline` is default and `adaptive_hier` is optional. The supplied runtime's dispatch search and loader witness [RT-ABS-action-dispatch](runtime.md#rt-abs-action-dispatch) distinguish text/JSON/logprob operations from a general action dispatcher. No additional registered tool or hook route was established here. That bounded finding is not a whole-repository absence proof. Uninspected ranking, backend and maintenance branches preclude a system-complete negative about all checks or all possible withdrawal mechanisms.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-original-messages](#epi-obj-original-messages) | see record | see record | SRC-1, `src/generation/prediction_correction_engine.py` | see record |
| [EPI-OBJ-episode-content](#epi-obj-episode-content) | see record | see record | SRC-1, `src/generation/episode_generator.py` | see record |
| [EPI-OBJ-predicted-episode](#epi-obj-predicted-episode) | see record | see record | SRC-1, `src/generation/prediction_correction_engine.py` | see record |
| [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | see record | see record | SRC-1, `src/generation/prediction_correction_engine.py` | see record |
| [EPI-OBJ-theme-summary](#epi-obj-theme-summary) | see record | see record | SRC-1, `src/core/memory_hierarchy.py` | see record |
| [EPI-OBJ-selection-state](#epi-obj-selection-state) | see record | see record | SRC-1, `src/core/memory_hierarchy.py` | see record |
| [EPI-OBJ-embedding-vectors](#epi-obj-embedding-vectors) | see record | see record | SRC-1, `src/core/memory_system.py` | see record |
| [EPI-OBJ-entropy-score](#epi-obj-entropy-score) | see record | see record | SRC-1, `evaluation/locomo/xMemory_search_framework.py` | see record |
| [EPI-OBJ-qa-result](#epi-obj-qa-result) | see record | see record | SRC-1, `evaluation/locomo/evals.py` | see record |
| [EPI-OBJ-reference-answer](#epi-obj-reference-answer) | see record | see record | SRC-1, `evaluation/locomo/evals.py` | see record |

## Authority-route ledger

Each row below separates a consequential function. The cited declaring record owns its mechanisms, timing, force and limits. Several rows cite one valid runtime container; this does not merge checking with disposition or retention with acceptance-based integration.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) | content transformation | implemented | [EPI-OBJ-original-messages](#epi-obj-original-messages) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Source warrant unknown; speech imported, not independently verified | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `src/core/memory_system.py` | none | none | see record |
| [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) | content transformation | implemented | [EPI-OBJ-episode-content](#epi-obj-episode-content) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Requested condensation, not established entailment | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `src/generation/episode_generator.py` | none | none | see record |
| [EPI-RTE-episode-normalization](#epi-rte-episode-normalization) | content transformation | implemented | [EPI-OBJ-episode-content](#epi-obj-episode-content) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/generation/episode_generator.py` | none | none | see record |
| [EPI-RTE-comparison-extraction](#epi-rte-comparison-extraction) | content transformation | implemented | [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/generation/prediction_correction_engine.py` | none | none | see record |
| [EPI-RTE-duplicate-check](#epi-rte-duplicate-check) | check/evidence production | implemented | [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/core/memory_system.py` | none | none | see record |
| [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition) | disposition/acceptance | implemented | [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/core/memory_system.py` | none | Operational admission, not epistemic acceptance | see record |
| [EPI-RTE-semantic-retention](#epi-rte-semantic-retention) | retention | implemented | [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/core/memory_system.py` | none | none | see record |
| [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) | content transformation | implemented | [EPI-OBJ-theme-summary](#epi-obj-theme-summary) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Topic abstraction is not validated source truth | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `src/core/memory_hierarchy.py` | [EPI-CLM-faithful-hierarchy](#epi-clm-faithful-hierarchy) | Fidelity unverified | see record |
| [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) | operational admission/selection/consumption | implemented | [EPI-OBJ-selection-state](#epi-obj-selection-state) | non-truth-apt policy/content update: memberships and numerical retrieval organization | see record | see record | see record | see record | see record | Structural criteria do not establish factual correctness | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `src/core/memory_hierarchy.py` | [EPI-CLM-faithful-hierarchy](#epi-clm-faithful-hierarchy) | Organization is not acceptance-based integration | see record |
| [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search) | operational admission/selection/consumption | implemented | [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | no content change | see record | see record | see record | see record | see record | Relevance ranking, not truth endorsement | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `src/core/memory_system.py` | none | none | see record |
| [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) | check/evidence production | implemented | [EPI-OBJ-entropy-score](#epi-obj-entropy-score) | no content change | see record | see record | see record | see record | see record | Generated-token NLL surrogate only | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `evaluation/locomo/xMemory_search_framework.py` | [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose) | Not a correctness oracle | see record |
| [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) | operational admission/selection/consumption | implemented | [EPI-OBJ-original-messages](#epi-obj-original-messages) | no content change | see record | see record | see record | see record | see record | No truth license from threshold or fallback | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `evaluation/locomo/xMemory_search_framework.py` | [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose) | Raw-message utility not directly checked | see record |
| [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) | content transformation | implemented | [EPI-OBJ-qa-result](#epi-obj-qa-result) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Model answer candidate, not accepted knowledge | see record | see [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) | SRC-1, `evaluation/locomo/xMemory_search_framework.py` | none | none | see record |
| [EPI-RTE-lexical-evaluation](#epi-rte-lexical-evaluation) | check/evidence production | implemented | [EPI-OBJ-qa-result](#epi-obj-qa-result) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `evaluation/locomo/metrics/utils.py` | [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose) | Offline metric, not admission gate | see record |
| [EPI-RTE-owner-deletion](#epi-rte-owner-deletion) | lineage/freshness/recovery | implemented | [EPI-OBJ-semantic-memory](#epi-obj-semantic-memory) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/core/memory_system.py` | none | Not claim-specific refutation | see record |

No acceptance-based lifecycle-integration route is established by these records. This is a conclusion about the assessed routes, not a system-complete absence assertion over uninspected branches. Retention and theme organization occur without an evidenced evidence-consuming acceptance decision against a truth criterion.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose) | see record | SRC-1, `README.md`; doctrine/design and reported operation | see record | see [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader), [EPI-RTE-lexical-evaluation](#epi-rte-lexical-evaluation) | None supplied | No experiment; fixed-baseline NLL, fallback, prompt mismatch and hydration confound utility interpretation | Optional score-guided selection and offline lexical scoring implemented | “Only when” is stronger than negative thresholds/fallback; answer quality and token efficiency unverified |
| [EPI-CLM-faithful-hierarchy](#epi-clm-faithful-hierarchy) | see record | SRC-1, `README.md`; doctrine/design | see record | see [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), [EPI-RTE-semantic-retention](#epi-rte-semantic-retention) | None supplied | No fidelity measurement or independent intervention; split/merge objective not fully audited | Originals and lineage IDs coexist with generated abstractions and numerical organization | Retained originals permit later checking but do not prove summary faithfulness |

## Bounded conclusion

xMemory acquires conversation text of unknown external warrant, retains originals, generates episode and semantic candidates and makes them available to later prediction and question answering. These are distinct functions: retaining the evidence source is useful lineage, but does not itself certify generated claims. Episode cleanup has a narrow deterministic preservation case; model summaries, semantic extraction, themes and final answers remain semantically indeterminate without output instances and checked relations. No warranted-premise entailed-derivation route, or produced accepted ampliative claim, is established here. Non-entailment is not inferred merely because generation uses a model.

Prediction/comparison is a substantive evidence-directed generation mechanism: originals and a prediction reach the same extraction call. It is not merely blind storage. However, the call returns statements, not a retained criticism identifying a challenged proposition and allocating blame. Constant `confidence=0.9` is not measured warrant. Similarity checks can enforce nonduplication policy; admission and persistence do not enforce source faithfulness. Prompt persistence/utility tests are requested model criteria, not independently measured six-month truth or future utility. See [EPI-RTE-comparison-extraction](#epi-rte-comparison-extraction), [EPI-RTE-duplicate-check](#epi-rte-duplicate-check), [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition).

Structural updates change later candidate selection, while retained natural-language material has advisory/model-interpreted force through [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader). Code inclusion and exclusion are enforcing at context assembly, not proof of model compliance. Adaptive NLL governs the current query; offline reference scoring produces a report, not an automatic instruction, policy or memory update. Owner deletion is a separate administrative removal route, not an evidential withdrawal decision; all-consumer revocation is unestablished.

The inference and embedding components have separately bounded parameter/version findings in [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) and [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client). No inspected parameter-training step is established; this does not negate retained-state adaptation. No observed improvement or learning benefit follows from wiring. Autonomous software admission is not evidence of autonomous theory building; inaccessible model internals establish neither criticism nor its absence. This report makes no reflective-system or self-improvement attribution and assigns no system-wide epistemic score.

## Shared records

### Operative objects

#### EPI-OBJ-original-messages
Label: Original messages

Source-native identity: `Episode.original_messages`. Natural-language speech with symbolic role/timestamp fields, stored in episode JSONL and host lists. Candidate truth-apt content includes claims uttered in a conversation; their authorship and external truth are not authenticated. They serve as comparison evidence and conditional answer context. SRC-1, `src/generation/prediction_correction_engine.py`; originals retention and consumption evidence is supplied by [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) and [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader). Distinct object, no runtime object counterpart; it spans those routes rather than replacing them. Source warrant is unknown, not upgraded by import.

#### EPI-OBJ-episode-content
Label: Episode content

Source-native identity: `Episode.content`; natural-language representation in host memory and episode JSONL. It claims what happened in a segment and serves as a retained evidence proxy. It differs from originals because generated prose can omit or introduce meaning. SRC-1, `src/generation/episode_generator.py`. Distinct object inventory entry, overlapping [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission) and [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), not duplicate routes. The model request and retention mechanism are evidenced in the former. Semantic fidelity is unobserved.

#### EPI-OBJ-predicted-episode
Label: Predicted episode

Source-native identity: local `predicted_episode`; natural-language prediction in transient host memory, not the saved episode. Its candidate propositions describe plausible conversation content given episode title and relevant prior statements. Consumer: comparison extraction, which also sees originals. No instance establishes actual non-entailment or faithful prediction. SRC-1, `src/generation/prediction_correction_engine.py`; [EPI-RTE-comparison-extraction](#epi-rte-comparison-extraction). Distinct object with no supplied operative-object counterpart; it is input to the supplied [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), not another admission route.

> predicted_episode = self._predict_episode(
>     new_episode.title, relevant_statements
> )
> --- `src/generation/prediction_correction_engine.py`

#### EPI-OBJ-semantic-memory
Label: SemanticMemory

Source-native identity: `SemanticMemory.content`; natural-language assertions in semantic repository/JSONL, with symbolic source episode IDs and numerical confidence metadata. The propositions concern identity, relationships, preferences, habits and other conversation-derived facts. Consumers are later prediction, theme generation and retrieval/answer calls. SRC-1, `src/generation/prediction_correction_engine.py`, `src/core/memory_system.py`; [EPI-RTE-comparison-extraction](#epi-rte-comparison-extraction), [EPI-RTE-semantic-retention](#epi-rte-semantic-retention). Confidence metadata is constant, not a calibrated evaluation. No supplied runtime operative-object counterpart; the object spans semantic admission and later reader routes.

#### EPI-OBJ-theme-summary
Label: ThemeNode summary

Source-native identity: `ThemeNode.summary`. Natural-language abstract topic/recurring-fact description in theme JSONL and host dictionary. A pure topic label need not be truth-apt; any assertion that constituent facts recur is truth-apt over its members. No instance permits finer individuation here. Consumers are adaptive retrieval/scoring, not the final answer's direct theme list. SRC-1, `src/core/memory_hierarchy.py`, `src/core/memory_system.py`; [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader). Distinct object, no runtime object counterpart. Minimum implementation witness:

> theme.summary = summary
> theme.embedding = emb.astype(float).tolist()
> theme.updated_at = now_iso()
> --- `src/core/memory_hierarchy.py:445-447`

#### EPI-OBJ-selection-state
Label: Selection state

Source-native identity: `ThemeNode.semantic_ids`, symbolic membership in hierarchy JSONL and host dictionaries. It is not itself a truth-bearing conversational proposition. Consumers use membership to organize and select candidates, rather than endorse their contents. SRC-1, `src/core/memory_hierarchy.py`; supplied [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) establish structural production and later selection. No supplied operative-object counterpart; this object spans those routes. Full structural/numerical correctness is uninspected.

#### EPI-OBJ-embedding-vectors
Label: Embedding vectors

Source-native identity: statement/theme/episode embeddings. Distributed-parametric dense representations stored in host caches, vector indexes and hierarchy vector artifacts, used by deterministic similarity and graph algorithms. They encode text for proximity selection, not individually inspectable truth claims. Their lifetime is retained/recomputed across reader loading, distinct from transient answer scores. SRC-1, `src/core/memory_system.py`, `src/core/memory_hierarchy.py`; [EPI-RTE-duplicate-check](#epi-rte-duplicate-check), [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader). No supplied object counterpart; these are outputs of [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client), not a duplicate provider component. That component record owns parameter mutation/version/endpoint findings; no vector-to-weight update is established. Proximity quality and exact model provenance remain unverified.

#### EPI-OBJ-entropy-score
Label: Reader entropy score

Source-native identity: local `entropy`, a scalar mean negative log probability stored in current-query host state. Symbolic numerical result consumed by fixed threshold/difference rules, not distributed model parameters. It is not itself a conversational fact. SRC-1, `evaluation/locomo/xMemory_search_framework.py`; [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) supplies the formula, fallback and consumer evidence. No runtime object counterpart. It differs from retained vectors and membership in producer, horizon and force: transient scoring can enforce current-context choice, but supplies no factual correctness or demonstrated final-answer utility license.

#### EPI-OBJ-qa-result
Label: QA response and reference

Source-native identity: result `response`, accompanied by question/category metadata. Natural-language answer candidate in saved JSON; propositions answer the supplied question. Consumers: operator and offline evaluator, not an established automatic semantic-memory updater. SRC-1, `evaluation/locomo/evals.py`; [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader), [EPI-RTE-lexical-evaluation](#epi-rte-lexical-evaluation). No runtime object counterpart. Candidate truth, rationale and entailment from retrieved sources remain unverified.

#### EPI-OBJ-reference-answer
Label: Reference answer

Source-native identity: saved `answer`. Imported natural-language dataset reference in QA result JSON, consumed only by offline evaluation on the inspected path; it is not input to the final answer call. It supplies an expected-answer oracle within the dataset domain, not independent world-truth verification. SRC-1, `evaluation/locomo/evals.py`; [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader), [EPI-RTE-lexical-evaluation](#epi-rte-lexical-evaluation). No runtime object counterpart. Distinct from the generated response by provenance and authority; reference correctness itself was not audited.

> gt_answer = str(item["answer"])
> pred_answer = str(item["response"])
> --- `evaluation/locomo/evals.py`

### Routes

#### EPI-RTE-episode-normalization
Label: Episode text normalization
Part of: [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission)

The part is post-generation field normalization, not the parent's broader import/generation/retention path. Owner: `EpisodeGenerator`. Model response dictionary → field validation → stripped strings and parsed optional timestamp → episode construction. SRC-1, `src/generation/episode_generator.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normalized title/content and optional timestamp dictionary; exceptions propagate to enclosing fallback logic.
- Later read-back: normalized episode fields persist and later reach generation and reader calls through the parent route.
- Delegated visibility: inapplicable — this local transformation makes no additional delegated model call.
- Selection predicate: dictionary with essential title/content; empty fields receive placeholders; invalid timestamp is omitted.
- Invalidation or expiry: inapplicable — normalization itself has no expiry; retained episode lifetime is parent-owned.
- Activation or effect: normalized fields are wired to episode creation, not observed in operation.
- Evidence limits: format checking is not checking conversational truth; placeholder substitution is not semantic preservation.

Concrete implementation deduction, without execution: response content `"  Alice likes tea.  "` becomes `"Alice likes tea."` through `str(...).strip()`. This whitespace-only case is non-ampliative reshaping. A blank content instead becomes `"Episode content not generated"`; that branch reports missing generation, not an entailed conversation fact. The license is string normalization only. Code enforces the emitted field value for later calls; no human verdict or truth oracle participates. Guidance is the static generator contract; the normalized fields, not a new method, persist. Fallback and essential-field rejection qualify any claim that successful generation proves content quality.

> content = str(response["content"]).strip()
> if not content:
>     content = "Episode content not generated"
> --- `src/generation/episode_generator.py`

#### EPI-RTE-comparison-extraction
Label: Comparison extraction
Part of: [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission)

Owner: `PredictionCorrectionEngine`. Selected prior statements plus episode title → model prediction → originals/prediction comparison prompt → new statement list → `SemanticMemory` objects. Cold start uses episode summary, not direct originals in that call. SRC-1, `src/generation/prediction_correction_engine.py`, implementation; `src/generation/prompts.py`, doctrine/design. This is the model-dependent candidate-generation part, not duplicate checking or saving.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated semantic objects or empty list on error.
- Later read-back: admitted statements later guide prediction, theme organization and answers through the parent route.
- Delegated visibility: prediction gets title/relevant statements; comparison gets formatted originals and prediction; cold start gets episode title/content/time.
- Selection predicate: existing statements select comparison mode; none selects cold start; model output and empty-string filtering select candidate statements.
- Invalidation or expiry: prediction is transient; no old-statement replacement or claim-specific expiry is implemented in this extraction method.
- Activation or effect: output candidates feed semantic admission; no observed factual correction established.
- Evidence limits: no candidate instances establish entailment/non-entailment; output has no retained per-claim criticism, blame or calibrated warrant.

The evaluator requested by the prompt is the same model performing generation. Target/domain: missing or misrepresented valuable conversational information relative to prediction, with persistence/specificity/utility/independence criteria. It consumes evidence but returns candidate assertions, not a distinct evidence-consuming acceptance decision. Relation: indeterminate between reshaping, entailed derivation and ampliative conjecture; paired inputs/output with semantic checking would decide it. New prediction content is also semantically indeterminate without a concrete instance. Code filtering/admission does not prove these relations.

Model proposes; code decides parse/empty filtering and creates objects; no human per-statement veto or held-out oracle. Operating mode is incremental conversation extraction, triggered by a new episode. Static guidance shapes proposals; what persists is statement content, source ID and generic metadata, not criticism or method revision. Exceptions return empty candidates; no revision or rollback of previous statements occurs here. `confidence=0.9` is assigned regardless of whether any source claim was independently checked. Authority is candidate evidence for later model interpretation, not warranted external truth.

> Extract ONLY the valuable knowledge that exists in the original but is missing or misrepresented in the prediction.
> --- `src/generation/prompts.py`

> memory = SemanticMemory(
>     user_id=user_id,
>     content=statement,
>     knowledge_type="knowledge",  # Use generic type
>     source_episodes=[source_episode.episode_id],
>     confidence=0.9,  # High confidence, learned from actual differences
>     created_at=source_episode.timestamp  # Use actual occurrence time of source episode
> )
> --- `src/generation/prediction_correction_engine.py`

#### EPI-RTE-duplicate-check
Label: Semantic duplicate check
Part of: [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission)

Owner: `MemorySystem`. Candidate content embedding plus existing same-type embeddings → cosine comparisons → Boolean duplicate result. This is the check part; disposition has its own record. SRC-1, `src/core/memory_system.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: true above configured threshold, false otherwise, including on caught failure.
- Later read-back: inapplicable — Boolean check is transient; retained prior statements are inputs, not an accumulated check report.
- Delegated visibility: embedding provider receives candidate/existing text when vectors are missing; deterministic comparison receives vectors and type labels.
- Selection predicate: compare only equal knowledge types; similarity strictly greater than `semantic_similarity_threshold`.
- Invalidation or expiry: inapplicable — recomputed check result has current-call lifetime.
- Activation or effect: result reaches the skip predicate in semantic disposition.
- Evidence limits: semantic proximity is neither identity nor contradiction resolution; failure is fail-open for this check.

Target/domain: vector proximity among same-type stored/candidate statement texts. Program evaluator licenses only the configured redundancy decision. It grants no truth authority. No human, expected-answer oracle or delayed outcome check participates; code may veto insertion using the Boolean. Operational path is check result → semantic save loop → enforcing skip for this insertion only. Existing statements are not withdrawn. No content change occurs.

> if similarity > self.config.semantic_similarity_threshold:
>     return True
> --- `src/core/memory_system.py`

> except Exception as e:
>     logger.error(f"Error checking semantic memory duplication: {e}")
>     return False
> --- `src/core/memory_system.py`

#### EPI-RTE-semantic-disposition
Label: Semantic insertion disposition
Part of: [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission)

Owner: `MemorySystem`. Candidate list and duplicate result → skip or repository-save continuation. SRC-1, `src/core/memory_system.py`, implementation. Distinct from the checking part and the persistence part.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: loop continues on duplicate or proceeds to save the candidate.
- Later read-back: admitted content later reaches readers through [EPI-RTE-semantic-retention](#epi-rte-semantic-retention).
- Delegated visibility: inapplicable — local branch consumes check result rather than delegating judgment.
- Selection predicate: `if self._is_duplicate_semantic_memory(...): continue`.
- Invalidation or expiry: inapplicable — skip decision ends this insertion attempt; no per-claim revision record is retained.
- Activation or effect: enforcing insertion gate, not observed operation.
- Evidence limits: no separate truth acceptance criterion, intended-use test result or source-faithfulness check is consumed here.

Model proposes content, software decides insertion, and no per-content human approval or expected-answer oracle is wired. The trigger is generated semantic candidates, not failed QA scores. Rejection is duplicate skipping; failure can admit a candidate because the check returns false. Static extraction guidance requests usefulness/persistence; repository content persists without an acceptance rationale. No automatic rollback of already admitted candidates is established. Operational authority is permission to persist and become later context; epistemic acceptance is not established by this gate.

> if self._is_duplicate_semantic_memory(
>     owner_id,
>     memory,
>     existing_memories=existing_semantic_memories,
>     embedding_cache=existing_embeddings,
>     new_embedding=new_embedding
> ):
>     continue
> --- `src/core/memory_system.py`

#### EPI-RTE-semantic-retention
Label: Semantic retention
Part of: [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission)

Owner: `MemorySystem` with repository/index providers. Passed candidate → repository save → index attempt → cache/incremental result → later maintenance and reader reload. SRC-1, `src/core/memory_system.py`, implementation. This is retention, not acceptance-based lifecycle integration.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved-memory dictionaries include content, ID, embedding and source episode ID.
- Later read-back: statement repository supplies later predictions and retrieval; incremental batches feed themes/graph.
- Delegated visibility: repository and search index receive statement object; later models receive selected text rather than every retained field.
- Selection predicate: save continuation after duplicate gate; index failure does not undo repository save.
- Invalidation or expiry: no TTL or evidence-triggered claim withdrawal in this save loop; deletion is a separate administrative route.
- Activation or effect: persistence/read-back wiring only; actual durability and behavioral effect unobserved.
- Evidence limits: cache/index/file agreement and atomic multi-layer commits are not established; source ID preserves navigation, not warrant.

The save stores a candidate with provenance, not an accepted theory. Behavioral authority is later advisory/model-interpreted text through [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader), plus numerical ranking influence from vectors. Code owns persistence; no new human/content review, answer oracle or truth test occurs at this stage. Errors do not imply rollback; the source explicitly continues after indexing failure. Guidance remains static extraction prompts, not automatically revised instructions.

> memory_id = self._semantic_repository.save(memory)
> --- `src/core/memory_system.py`

> logger.warning(f"Failed to add semantic memory to search index (continuing): {e}")
> --- `src/core/memory_system.py`

#### EPI-RTE-lexical-evaluation
Label: Offline lexical evaluation
Part of: [RT-RTE-offline-evaluation](runtime.md#rt-rte-offline-evaluation)

Owner: evaluation software/operator. Saved response/reference → normalization/token sets and BLEU → per-item metrics → metrics JSON → category/overall mean printing. This narrows the parent evaluator to the inspected lexical target/domain and its consumer. SRC-1, `evaluation/locomo/evals.py`, `evaluation/locomo/metrics/utils.py`, `evaluation/locomo/generate_scores.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: F1 and BLEU scores per non-category-5 item; later aggregate tables printed.
- Later read-back: metrics JSON is read by `generate_scores.py`; no score-to-memory or prompt revision consumer is established.
- Delegated visibility: workers receive saved question/reference/response/category; no model judge is called in the inspected scoring loop.
- Selection predicate: category 5 skipped; lexical metrics computed against dataset answer.
- Invalidation or expiry: inapplicable — operator selects artifact paths/reruns; no live acceptance state.
- Activation or effect: scoring and report production wired, no enforcing effect on subsequent answer or memory admission.
- Evidence limits: lexical overlap licenses lexical agreement only, not truth, reasoning correctness, fidelity, transfer or component attribution; no completed result supplied.

Target/domain: saved answer token overlap with the reference for included LoCoMo items. Program evaluator uses expected dataset answer after generation. Model proposes response, software scores, operator may interpret results; no automated deployment/admission veto exists in this route. F1 uses sets, not token multiplicities. Concrete source deduction: `prediction="tea tea"`, `reference="tea"` both yield the singleton token set and hence F1=1; this says nothing about repeated-answer quality. This evaluator is operative for the report consumer but not for future generation. The truth-apt answer content is unchanged; numerical scores are metrological output, not accepted conversation claims.

> pred_tokens = set(simple_tokenize(prediction))
> ref_tokens = set(simple_tokenize(reference))
> common_tokens = pred_tokens & ref_tokens
> --- `evaluation/locomo/metrics/utils.py`

> #llm_score = evaluate_llm_judge(question, gt_answer, pred_answer)
> llm_score = None
> --- `evaluation/locomo/evals.py`

> result = df.groupby("category").agg({"bleu_score": "mean", "f1_score": "mean", "llm_score": "mean"}).round(4)
> --- `evaluation/locomo/generate_scores.py`

#### EPI-RTE-owner-deletion
Label: Owner data deletion

No counterpart after comparison with supplied runtime routes: the nearest are [RT-RTE-baseline-search](runtime.md#rt-rte-baseline-search) and [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission), but neither refers to administrative removal. Owner: `MemorySystem`; explicit call → owner lock → buffer and stores deletion → index clearing → status dictionary. SRC-1, `src/core/memory_system.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-component deletion status flags, potentially partial after exception.
- Later read-back: later repository/index reads can lose removed data; already loaded reader hierarchy state is not invalidated by this method.
- Delegated visibility: stores and search engine receive owner ID, not a criticized proposition or evidence rationale.
- Selection predicate: caller-supplied owner; semantic deletion conditional on enablement.
- Invalidation or expiry: deletes owner storage/index state; a found load-cache key has only `pass` in this method; no cancellation of semantic tasks or theme/reader-cache invalidation is shown here.
- Activation or effect: administrative removal calls wired, not observed successful all-layer revocation.
- Evidence limits: backend deletion guarantees and concurrent-reader/task interactions not exhaustively inspected; prevents universal withdrawal claim.

No evaluator of truth participates: caller initiates, code executes and catches errors, backend flags report completion. Human identity for arbitrary caller is unresolved; no oracle or evidence-driven improvement trigger. Operational force is removal from affected stores/indexes for later reads, not retroactive erasure from model contexts or a refutation decision. No statement text changes and no epistemic authority is conferred. No rollback protocol is implemented in the inspected method.

> results["episodic_storage"] = self.storage["episode"].delete_user_data(owner_id)
> --- `src/core/memory_system.py`

> results["search_index"] = self.search_engine.clear_user_index(owner_id)
> --- `src/core/memory_system.py`

> if self.performance_optimizer.cache.contains(cache_key):
>     # Simple cache cleanup (sharding system will automatically expire)
>     pass
> --- `src/core/memory_system.py`

### Claims

#### EPI-CLM-faithful-hierarchy
Label: Faithful high-level hierarchy

Claimed operation: hierarchy of intact units with faithful high-level node organization guided by split/merge objective. SRC-1, `README.md`, doctrine/design. Distinct from the inference/benefit claim [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose), though the same paragraph makes both claims. Implementation organization is established by [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), not a fidelity acceptance test. Directly inspected summary prompt and recomputation do not independently validate generated summaries; full objective internals were not audited here. No observed or causal evidence establishes faithful content preservation.

> We propose xMemory, which builds a hierarchy of intact units and maintains a searchable yet faithful high-level node organisation via a sparsity–semantics objective that guides memory split and merge.
> --- `README.md`
