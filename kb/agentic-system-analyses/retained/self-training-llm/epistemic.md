---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Self-Training-LLM epistemic routes: source-conditioned candidates, consistency proxies, training authority and document-relative model judging."
run-id: AAS-2026-10-15-self-training-llm-5b5ee621bde2-01
reviewed-boundary: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
---

# Self-Training-LLM epistemic report

## Source-and-claim boundary

Scope and source identity: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register), SRC-1. The question is whether this operator-launched model-building workflow produces warranted answers or instead gives generated candidates and consistency proxies authority to train later models. Provider internals, external dataset truth, weights and execution artifacts are outside the available evidence. No target execution was performed. Source-supported paths below are implemented capacities, not observations of successful execution.

The consequential public claim is [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering); the clustering method's narrower design claim is [EPI-CLM-semantic-clustering](#epi-clm-semantic-clustering). Its source-native distinction between consistency and knowledge scoring is assessed separately from factual correctness. No universal knowledge-production verdict follows from these routes.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Four shipped launchers | `script/wiki_ques_gen.sh`, `script/train.sh`, `script/testing.sh`, `script/tgi.sh` | Direct full reads; see [RT-RTE-data-generation](runtime.md#rt-rte-data-generation), [RT-RTE-model-training](runtime.md#rt-rte-model-training), [RT-RTE-response-generation](runtime.md#rt-rte-response-generation), [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) | Launchers do not enforce matching server/checkpoint identities; default generation blockers remain. |
| Topic/document acquisition and cleanup | `uncertainty/topic_generator.py`, `uncertainty/data_utils.py` | Direct reads of predefined-topic selection, document cleanup, chunking, training loaders and length normalization; [EPI-RTE-document-transform](#epi-rte-document-transform) | External corpus contents and source accuracy uninspected; no fact certification. |
| Question, gold, context and raw answer routes | `uncertainty/wiki_generation.py`, `uncertainty/templates.py` | Direct reads of generation functions and training-artifact handoff; prompt formatters, self-rating prompt and initial few-shot examples; [EPI-OBJ-gold-answer](#epi-obj-gold-answer), [EPI-RTE-answer-cleaning](#epi-rte-answer-cleaning); remaining setup/test behavior supplied by [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) | Not all example bodies independently read; no claim of exhaustive prompt-content audit or measured compliance. |
| Scorers, clustering, self-rating, judge/cache | `uncertainty/scorer.py`, `uncertainty/utils.py` | Complete scorer read in bounded ranges; direct question/answer cleaning and duplicate helpers; [EPI-RTE-score-evidence](#epi-rte-score-evidence), [EPI-RTE-preference-selection](#epi-rte-preference-selection); see [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) | No calibration data, valid provider replies or reference truth supplied. |
| Training and parameter consumer | `uncertainty/train.py`, `uncertainty/self_learning_training.py`, `uncertainty/generate_response.py` | Direct full training-driver read and DPO formatter read; trainer save/model loading and response alternatives supplied by [RT-RTE-model-training](runtime.md#rt-rte-model-training), [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) | No weights or traced subsequent behavior; parameter-level propositions not determinable. |
| Pairwise result consumer, oracle/RAG/known/DoLA alternatives | `uncertainty/pairwise_eval.py`, `uncertainty/generate_response.py` | Supplied [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) and [RT-RTE-response-generation](runtime.md#rt-rte-response-generation); judge implementation directly read | No evaluation artifacts, human decision trail or causal experiment; cannot establish superiority, transfer or component effects. |
| Other exposed/helper alternatives | `uncertainty/data_utils.py`, `uncertainty/topic_generator.py` | Symbol/entry-point search across Python files; direct external-training loader read | Embedding/topic-ranking alternatives and unrelated benchmark dataset classes not comprehensively traced. No system-complete negative about all epistemic mechanisms. Frozen scripts expose Python stages, not a registered model-tool or hook dispatch surface. |

All direct inspection is SRC-1 implementation except README and requested prompt behavior, which are doctrine/design. The four shell dispatches agree with the runtime stage inventory. No additional launched evaluator was found in those scripts. Available helper branches are not access gaps. Missing traces prevent activation claims; missing independent references and calibration prevent treating agreement as factual warrant; missing interventions prevent causal benefit attribution. Opaque provider processing cannot establish either hidden criticism or its absence.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-document](#epi-obj-document) | Imported article assertions | Source context/reference | see record | External warrant unknown; reference sections removed. |
| [EPI-OBJ-instruction](#epi-obj-instruction) | A question is normally a request, not an asserted answer; presuppositions can be truth-apt | Curriculum prompt | see record | Lexical admission does not check answerability or presuppositions. |
| [EPI-OBJ-gold-answer](#epi-obj-gold-answer) | Generated factual answer candidates | Gold/reference/SFT labels | see record | Document-conditioned, context-free SFT, context-answer and external-answer producers differ; none is certified by its field name. |
| [EPI-OBJ-raw-answer](#epi-obj-raw-answer) | Generated context-free answer candidates | Knowledge samples/rejected candidates | see record | No actual generated instance supplied. |
| [EPI-OBJ-score-result](#epi-obj-score-result) | Numerical estimates, cluster assignments and A/B-derived rankings about candidate relations | Consistency/knowledge/confidence and evaluation signals | see record | Different target domains; not interchangeable factuality measurements. |
| [EPI-OBJ-preference](#epi-obj-preference) | Symbolic chosen/rejected designation over answer strings | Optimization input | see record | Policy designation is not acceptance of an answer as true. |
| [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model) | Not determinable as individuated propositions from accessible weight evidence | Trained behavior | see record | Distributed-parametric changes do not expose an accepted claim or its warrant. |

## Authority-route ledger

Each compact row cites its declaring record; `see` delegates that record's owned facts rather than reproducing its return/read-back fields. Linked uses of a container separate consequential functions. Architectural status is this report's assessment. No lifecycle integration of accepted factual claims is established by the inspected training/evaluation chain; retention and numerical training remain separate functions.

Route ID: [EPI-RTE-document-transform](#epi-rte-document-transform)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document](#epi-obj-document)
Content/update relation: truth-apt transformation: acquisition/import; external source warrant unknown. Subsequent heading-based deletion and chunk selection are non-ampliative reshaping at the retained-text level, not proof of preserved qualification or full article coverage.
Transition or check target: see route.
Evaluator/condition and domain: see route; no truth evaluator is supplied by cleanup.
Activation and timing: see route.
Possible or observed result: see route; no observed result.
Implemented force: see route.
Epistemic authority and scope: imported text is a local reference, not certified world truth.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering).
Mismatch marker or none: loss of source reference tail is not epistemic validation.
Gap/limit: see route.

Route ID: [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-instruction](#epi-obj-instruction), [EPI-OBJ-gold-answer](#epi-obj-gold-answer), [EPI-OBJ-raw-answer](#epi-obj-raw-answer).
Content/update relation: truth-apt transformation: indeterminate for generated answer content. Model calls may repeat, derive or add claims; no output/premise pair establishes which. Questions primarily constitute non-truth-apt policy/content update: curriculum requests.
Transition or check target: see record.
Evaluator/condition and domain: see record; document-answering request is not a checked entailment.
Activation and timing: see record.
Possible or observed result: see record; candidates and artifacts are possible, not observed.
Implemented force: see record.
Epistemic authority and scope: candidate generation only; gold naming grants no additional factual license.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record; candidate text can later become a label.
Evidence source ID and local anchor: see record.
Claim IDs or none: [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering).
Mismatch marker or none: requested grounding versus demonstrated grounding.
Gap/limit: see record; an unavailable concrete answer prevents classifying generated novelty as an ampliative conjecture rather than indeterminate.

Route ID: [EPI-RTE-answer-cleaning](#epi-rte-answer-cleaning)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-gold-answer](#epi-obj-gold-answer).
Content/update relation: truth-apt transformation: non-ampliative reshaping for clause/sentence deletion and formatting. Retained wording does not guarantee retained meaning in context.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: no license for stronger positive assertions after removal of a caveat.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: none.
Mismatch marker or none: deleting document-related caveats can change reliance without checking truth.
Gap/limit: source deduction only; no executed input.

Route ID: [EPI-RTE-answer-cleaning](#epi-rte-answer-cleaning)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-instruction](#epi-obj-instruction), [EPI-OBJ-gold-answer](#epi-obj-gold-answer).
Content/update relation: no content change.
Transition or check target: see route; lexical admissibility, empty/duplicate/length conditions, not factual accuracy.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route; omitted candidate or continuation.
Implemented force: see route.
Epistemic authority and scope: operational admission only, not factual acceptance.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: alternative branches use different cleaners; no universal cleaning invariant.

Route ID: [EPI-RTE-score-evidence](#epi-rte-score-evidence)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-result](#epi-obj-score-result).
Content/update relation: truth-apt transformation: indeterminate for model-assessed semantic relations; averaging the returned numbers is an entailed arithmetic consequence conditional on those numbers, not a factual derivation about the world.
Transition or check target: SelfCheckGPT reference/sample contradiction or sample/sample contradiction; see route.
Evaluator/condition and domain: see route; NLI relations over truncated answer texts, not source/document truth.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route; score production is separate from selection below.
Epistemic authority and scope: classifier estimates of textual relations only; no calibrated knowledge probability established.
Operational authority: behavior permitted, blocked, or changed: downstream selector can admit examples.
Behavioral-authority path: consumer, channel, force, horizon: see route and [EPI-RTE-preference-selection](#epi-rte-preference-selection).
Evidence source ID and local anchor: see route.
Claim IDs or none: [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering).
Mismatch marker or none: contradiction proxy versus knowledge claim.
Gap/limit: agreement among false answers is a source-compatible countercase; reference truth is not independently checked here.

Route ID: [EPI-RTE-score-evidence](#epi-rte-score-evidence)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-result](#epi-obj-score-result).
Content/update relation: truth-apt transformation: indeterminate for BSDetector confidence estimates; score arithmetic is a conditional numerical derivation.
Transition or check target: BSDetector answer confidence; see route.
Evaluator/condition and domain: see route; NLI entailment estimates plus optional model self-rating, not an independent answer oracle.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: estimated consistency and declared confidence; not certified entailment or truth.
Operational authority: behavior permitted, blocked, or changed: see route; branch compatibility limits apply before selection.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering).
Mismatch marker or none: self-declared certainty is not independently measured correctness.
Gap/limit: no successful alternative-mode trace or calibration supplied.

Route ID: [EPI-RTE-score-evidence](#epi-rte-score-evidence)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-result](#epi-obj-score-result).
Content/update relation: truth-apt transformation: indeterminate for semantic-equivalence judgments; cluster bookkeeping and entropy arithmetic are conditional numerical derivations.
Transition or check target: semantic_consistency cluster membership and likelihood-based entropy; see route.
Evaluator/condition and domain: see route; two-direction NLI noncontradiction against cluster representatives, then token-likelihood aggregation.
Activation and timing: see route.
Possible or observed result: see route; grouping and numerical uncertainty estimates.
Implemented force: see route; output supplies later ranking where compatible.
Epistemic authority and scope: predicted relation among question/answer strings; no guarantee of semantic equivalence, source truth or calibrated uncertainty.
Operational authority: behavior permitted, blocked, or changed: see route; branch compatibility limits apply before selection.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: [EPI-CLM-semantic-clustering](#epi-clm-semantic-clustering).
Mismatch marker or none: neutral-as-similar implementation is weaker than bidirectional-entailment wording.
Gap/limit: no successful alternative-mode trace, cluster artifact or calibration supplied.

Route ID: [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-gold-answer](#epi-obj-gold-answer), [EPI-OBJ-raw-answer](#epi-obj-raw-answer), [EPI-OBJ-score-result](#epi-obj-score-result).
Content/update relation: no content change.
Transition or check target: see record.
Evaluator/condition and domain: see record; existence/reload is not endorsement.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: retained candidates and scores, not accepted factual claims.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record; serialized data reach later training invocations.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: see record; no route-linked candidate instance supplied.

Route ID: [EPI-RTE-preference-selection](#epi-rte-preference-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-preference](#epi-obj-preference).
Content/update relation: non-truth-apt policy/content update: designation of optimization examples and chosen/rejected roles.
Transition or check target: see route.
Evaluator/condition and domain: see route; numerical rules enforce configured criteria, not truth.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: acceptance for optimization under score/flag criteria only; not an evidence-consuming decision accepting an ampliative factual claim.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering).
Mismatch marker or none: nonpositive unknown threshold bypasses question-filtered subset; reference identity is enforced only for the single-preference pair and first multiple-preference pair when reference-as-chosen is enabled, not later pairs.
Gap/limit: see route.

Route ID: [RT-RTE-model-training](runtime.md#rt-rte-model-training)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model).
Content/update relation: non-truth-apt policy/content update: distributed parameter optimization from labels/preferences; individuated propositional content is not determinable.
Transition or check target: see record.
Evaluator/condition and domain: see record; validation loss selection, where enabled, evaluates fit rather than independent factual truth.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: no inference of accepted claims from numerical integration.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption).
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: saving a checkpoint is not a judge-approved deployment.
Gap/limit: see record; learned capacity and exercised dependence unobserved.

Route ID: [RT-RTE-response-generation](runtime.md#rt-rte-response-generation)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model), [EPI-OBJ-document](#epi-obj-document).
Content/update relation: truth-apt transformation: indeterminate for newly generated responses; selection/loading alone makes no content change.
Transition or check target: see record.
Evaluator/condition and domain: see record; local configured path or independently served endpoint.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: downstream answers remain unchecked candidates; RAG supplies context, not truth certification.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption).
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: result filename versus actual TGI weights.
Gap/limit: see record; DoLA, known-subset and ordinary test branches do not supply independent correctness references.

Route ID: [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-result](#epi-obj-score-result).
Content/update relation: truth-apt transformation: indeterminate for model-relative rankings about truthfulness/relevance; parsed category follows the two returned choices under fixed rules.
Transition or check target: see record; paired responses relative to document and question.
Evaluator/condition and domain: see record; GPT-4o then two-order parser, not expected correct labels.
Activation and timing: see record.
Possible or observed result: see record; win/lose/tie or omitted failed sample.
Implemented force: see record.
Epistemic authority and scope: model preference under the supplied document, not absolute factual accuracy, mechanism attribution or replay safety.
Operational authority: behavior permitted, blocked, or changed: see record; aggregate report, no automatic checkpoint veto.
Behavioral-authority path: consumer, channel, force, horizon: see record; operator-facing advisory report, no evidenced later operator uptake.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: disabled hallucination branch yields placeholder zeros, not evidence.
Gap/limit: see record; omission changes denominator, and oracle mode uses generated responses rather than certified answers.

Route ID: [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-score-result](#epi-obj-score-result).
Content/update relation: no content change.
Transition or check target: see record; judge cache reuse.
Evaluator/condition and domain: see record; formatted first user-message key and engine-named cache.
Activation and timing: see record.
Possible or observed result: see record; old category consumed without a new provider call.
Implemented force: see record.
Epistemic authority and scope: cached judgment retains its original bounded license; freshness or endorsement after provider/system-prompt change is not established.
Operational authority: behavior permitted, blocked, or changed: see record; skips new evaluation and contributes to aggregates.
Behavioral-authority path: consumer, channel, force, horizon: see record; persisted category to later evaluator invocation, enforcing cache hit.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: cache key omits actual weight revision and system message.
Gap/limit: see record; no explicit withdrawal/rejudging policy tied to those changes.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering) | see record | see record; SRC-1, `README.md`, doctrine/design | see record | [EPI-RTE-score-evidence](#epi-rte-score-evidence), [EPI-RTE-preference-selection](#epi-rte-preference-selection), [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) | see runtime routes; none supplied | No comparison or intervention; sampling agreement cannot independently establish factual knowledge | Context inclusion/omission and numerical filtering are wired, subject to branch prerequisites | “Knowledge score” is an operational proxy; no calibrated knowledge/factuality interpretation demonstrated. SFT generation exits before DPO consistency scoring. |
| [EPI-CLM-semantic-clustering](#epi-clm-semantic-clustering) | see record | see record; doctrine/design | see record | [EPI-RTE-score-evidence](#epi-rte-score-evidence) | none supplied | No cluster-validation comparison or component intervention | Two-direction comparison and clustering exist | Noncontradiction, including neutrality, passes rather than requiring two entailment labels. |

## Bounded conclusion

The workflow acquires external article text and gives selected chunks reference authority in questions, context answers and model judging. Source warrant is unknown; source references can be removed before model calls. Generated `gold_answer` values are not imported authoritative answers merely because they are conditioned on those chunks. Context-free SFT labels, context-conditioned auxiliary labels, DPO references and raw samples have different premises. No supplied answer instance supports an assertion that a generated proposition is entailed, non-entailed, or accepted as true. See [EPI-RTE-document-transform](#epi-rte-document-transform), [EPI-OBJ-gold-answer](#epi-obj-gold-answer), [RT-RTE-data-generation](runtime.md#rt-rte-data-generation).

The checks have distinct licenses. Lexical/length/repetition checks decide candidate admissibility, not truth. NLI estimates answer-to-answer textual relations; self-rating adds the generator's declared confidence; semantic clustering admits pairs without predicted contradiction, including neutral pairs, rather than requiring bidirectional entailment. These estimates can control optimization examples. Arithmetic over their outputs does not create warranted factual premises. See [EPI-RTE-answer-cleaning](#epi-rte-answer-cleaning), [EPI-RTE-score-evidence](#epi-rte-score-evidence).

Training selection grants operational authority under thresholds, extrema and reference override: intended use is SFT labels or DPO optimization, scope is the configured dataset/invocation. With reference-as-chosen enabled, the single-preference pair and first multiple-preference pair use extracted `gold_answer`; later multiple-preference pairs instead use selected `gold_answer_sample` entries. The training driver admits those later pairs through `extend`, so reference identity is not uniform across admitted examples. The selector can omit candidates, but it does not record an independent acceptance criterion for relying on their factual assertions. Parameter updating and checkpoint saving therefore establish a direct behavior-adaptation path, not lifecycle integration following factual acceptance. Local inference can consume those parameters in later invocations; TGI requires matching operator configuration. No observed dependence or successful improvement follows. See [EPI-RTE-preference-selection](#epi-rte-preference-selection), [RT-RTE-model-training](runtime.md#rt-rte-model-training), [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption).

The downstream judge requests document-relative truthfulness and relevance rankings, filters invalid judgments, derives two-order categories, caches them and produces operator-facing aggregate reports. It neither retrospectively warrants the training explanation nor gates checkpoint admission. Cached labels may survive a provider/system-prompt change, and omitted judgments bound the reported denominator. Withdrawal from optimization after a later adverse ranking is not wired in the supplied training/evaluation chain. This is a bounded chain finding, not a system-complete absence across untraced alternatives. See [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation).

Parameter adaptation is inspectable separately from learning benefit. Self-improvement retains the runtime's dispositional, operator-mediated pathway assessment; exercised behavior and causality remain unobserved. Numerical criticism/selection does not establish formulated content-directed theory criticism, reflection or autonomous ownership of every stage. Nor does opaque model processing establish their absence. These properties remain independent of the positive scoring, selection and parameter-update mechanisms.

## Shared records

### Operative objects

#### EPI-OBJ-document
Label: Selected Wikipedia document

Source-native identity: `document`, `document_dict`, `topic2doc`. Representational form: natural-language article assertions. Storage substrate: external dataset, local document cache, question/answer records and prompts. Evidence: SRC-1, `uncertainty/topic_generator.py`, `uncertainty/data_utils.py`; see [EPI-RTE-document-transform](#epi-rte-document-transform). Distinct from [RT-RTE-data-generation](runtime.md#rt-rte-data-generation): this is its input content, not a second route. No operative-object counterpart is declared in the supplied runtime.

#### EPI-OBJ-instruction
Label: Generated question instruction

Source-native identity: `instruction`, `unique_qns`. Representational form: natural-language question, with possible factual presuppositions. Storage substrate: JSONL records and per-call prompts. Evidence: SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/templates.py`; see [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) and [EPI-RTE-answer-cleaning](#epi-rte-answer-cleaning). Distinct input/output part of the generation route; no supplied operative-object counterpart.

#### EPI-OBJ-gold-answer
Label: Gold answer candidates

Source-native identity: `gold_answer`, `gold_answer_sample`, `context_ans`. Representational form: natural-language answer strings, sometimes wrapped in provider generation objects. Storage substrate: JSONL/pickle, current-call objects and training text. Evidence: SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/templates.py`; closest supplied record is [RT-RTE-data-generation](runtime.md#rt-rte-data-generation), a route rather than this object. The producer roles differ: SFT self-generation sets `add_document = False`; DPO sets it true for gold but not raw answers; SFT auxiliary context answers use OpenAI with documents; `get_openai_answer` supplies only the question for optional external gold labels. These are candidate families with different premises, not uniformly grounded references.

> if generate_sft:
>     base = True
>     add_few_shot = True
>     add_document = False
> --- `uncertainty/wiki_generation.py`

> qns = qns_dict['instruction']
> ans_prompt = [{'role':'user','content':qns}]
> --- `uncertainty/wiki_generation.py`

The complementary document-omission rule and reference-generation premises are retained in [RT-RTE-data-generation](runtime.md#rt-rte-data-generation); context labels are added by [RT-RTE-model-training](runtime.md#rt-rte-model-training). The actual semantic relation of generated claims to those inputs is indeterminate without an output and checked interpretation. No supplied object counterpart exists.

#### EPI-OBJ-raw-answer
Label: Raw sampled answer candidates

Source-native identity: `raw_answer_sample`, `raw_answer`. Representational form: natural-language answers with associated generation/logprob structures. Storage substrate: current-call objects and scored answer pickle. Evidence: SRC-1, `uncertainty/wiki_generation.py`; see the document-omission passage in [RT-RTE-data-generation](runtime.md#rt-rte-data-generation). Distinct from gold because conditioning and downstream preference roles differ. No supplied object counterpart exists.

#### EPI-OBJ-score-result
Label: Scoring and judging results

Source-native identity: `hallucination`, `confidence`, `entropy`, `semantic_clusters`, `question_hallucination`, judge `result`. Representational form: symbolic numbers, memberships and categories consumed by fixed rules. Storage substrate: scored answer pickle, judge cache and aggregate result text. Material parts are assessed separately in [EPI-RTE-score-evidence](#epi-rte-score-evidence) and [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation). Evidence: SRC-1, `uncertainty/scorer.py`, `uncertainty/wiki_generation.py`. This object spans generation and judging routes rather than duplicating either. No supplied operative-object counterpart exists; their different evaluator domains do not license one combined quality score.

#### EPI-OBJ-preference
Label: Chosen and rejected training examples

Source-native identity: `chosen_ans`, `rejected_ans`, then `prompt`, `chosen`, `rejected`. Representational form: symbolic role designation over natural-language strings. Storage substrate: in-memory dataset and trainer tensors; saved parameters are a separate object, [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model). Evidence: SRC-1, `uncertainty/scorer.py`, `uncertainty/self_learning_training.py`; see [EPI-RTE-preference-selection](#epi-rte-preference-selection). No supplied object counterpart; closest route container is [RT-RTE-model-training](runtime.md#rt-rte-model-training).

### Routes

#### EPI-RTE-document-transform
Label: Document cleanup and selection

Part of: [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected cleaned topic/document mapping and bounded document chunks.
- Later read-back: Generation records preserve selected document text for later training context or judging; see parent route for file reload.
- Delegated visibility: Models receive selected chunks, not removed reference/see-also tails or the full corpus.
- Selection predicate: Predefined topics; remove tail beginning at a line exactly matching references or see also, case-insensitively; chunk by token/sentence limits with repeated first-sentence header.
- Invalidation or expiry: No truth-based invalidation in these text functions; parent file-existence reuse can retain older inputs.
- Activation or effect: Cleaned/chunked text becomes the reference used by generators and judge; successful delivery unobserved.
- Evidence limits: No corpus capture or model transcript; selected wording and source qualifications need not remain complete.

Endpoints/progression: dataset article → `get_predefined_topics` → `clean_document` → `chunk_document` → generation context. Owner is Python, not a human per-article acceptance decision. The fixed source-selection policy proposes no certified factual correction. The behavioral path is text supplied to generation/judge models, model-interpreted influence over each call and retained document context over later file consumers. SRC-1, `uncertainty/topic_generator.py`, `uncertainty/data_utils.py`.

> for i,doc in enumerate(split_document):
>     if doc.strip().lower() == 'references' or doc.strip().lower() == 'see also':
>         end_pos = i
>         break
> return '\n'.join(split_document[:end_pos])
> --- `uncertainty/topic_generator.py`

> if length > max_length:
>     continue
> --- `uncertainty/data_utils.py`

Concrete source deduction, not execution: `Claim.\nReferences\nCitation` becomes `Claim.` because the heading sets the slice endpoint. This preserves the retained assertion's words while discarding its citation tail. It cannot certify the claim or preserve its external warrant. Chunking additionally changes coverage; reference text is not a proof premise authenticated by this code.

#### EPI-RTE-answer-cleaning
Label: Question and answer cleanup

Part of: [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lexically admissible question, modified answer, or `None`/omitted candidate.
- Later read-back: Surviving gold answers are serialized and later used as labels/references; rejected candidates are not automatically restored.
- Delegated visibility: Subsequent scorer/trainer receives surviving text, not necessarily the original full generated answer.
- Selection predicate: Question empty/banned-word/uniqueness checks; branch-specific base delimiter cleanup, length/repetition checks, incomplete-sentence trimming, and nonhelpful-answer filtering.
- Invalidation or expiry: Current candidate processing; no semantic revalidation or version-based withdrawal of previously retained answers.
- Activation or effect: Controls retry/omission and label text; no factual correction is established.
- Evidence limits: TGI and local branches differ; `filter_nonhelpful_ans` applies through non-base `check_answer`, not uniformly to every answer path.

Endpoints: generated question → `check_question` → retry/admit; generated gold answer → TGI `check_single_answer` or local `check_answer` → save/score. Owner: code rules. Models propose, software can veto, human launches the stage but approves no individual answer. Operating mode: bounded Wikipedia curriculum. Guidance is fixed prompt/heuristic text; retained material is surviving answer text, not a criticism explaining why it is true. Recovery is bounded retry or rerun, not restoration of deleted qualifications. Evidence: SRC-1, `uncertainty/utils.py`, `uncertainty/wiki_generation.py`.

> if question.strip() == "" or 'document' in question or 'text' in question or 'passage' in question or 'information' in question:
>     return False
> --- `uncertainty/utils.py`

> if any(['document' in s for s in sents]):
>     # 2)
>     sents = [s for s in sents if 'document' not in s]
>     if len(sents) == 0:
>         return None
> --- `uncertainty/utils.py`

Source deduction with sentence segmentation held fixed: `The document is incomplete. The date is 1900.` loses the first sentence and retains `The date is 1900.` through this branch and `clean_incomplete_response`. This is deletion, not evidence of accuracy or proof that meaning is preserved. A stronger countercase to indiscriminate continuation is implemented rejection: a sentence containing `not` and one of `mentioned`, `specified`, `provided` can reject the whole answer. Such rejection still assesses lexical form, not whether the date is true. The base branch uses delimiter removal rather than this filter. Thus neither universal semantic damage nor universal harmlessness follows.

#### EPI-RTE-score-evidence
Label: NLI and uncertainty evidence

Part of: [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Score dictionary or `None`: contradiction averages, BSDetector confidence components, or semantic clusters and entropy.
- Later read-back: Scores are persisted with answers and reloaded for training selection; see parent route.
- Delegated visibility: NLI sees answer-pair text truncated at 512 tokens; semantic clustering prepends the instruction. Self-rating sees a question and proposed answer, not independent truth evidence.
- Selection predicate: Configured scoring method; empty references/samples omitted; SelfCheckGPT uses reference/sample pairs or pairwise sample comparisons depending on flags; BSDetector optionally adds generator confidence when beta is below one; semantic clustering compares against cluster representatives.
- Invalidation or expiry: Scores can be recomputed on reload; no calibration/provenance-based expiry for a changed external classifier is established.
- Activation or effect: Supplies numeric/categorical evidence to the separate training selector. This declaration does not merge evaluation with acceptance.
- Evidence limits: Model accuracy, exact parameter revisions and activation unobserved; alternative scorer paths have source-level compatibility constraints.

Endpoints/progression: answer candidates → configured NLI/self-rating/cluster computations → score dictionary → parent persistence → training selector. Owner: Python formulas over external classifier/generator judgments. Components: see [RT-CMP-nli-model](runtime.md#rt-cmp-nli-model), [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model). Their mutability/version limits remain local to those components. No human approves individual scores. The answer oracle is not independent: reference answers are generated, and self-rating is a model's choice among correctness/confidence labels. Scope is bounded curriculum scoring. The behavioral path is serialized score → deterministic training selector → optimization examples, enforcing eligibility/ranking for later training invocations. Evidence: SRC-1, `uncertainty/scorer.py`, `uncertainty/templates.py`.

> nli_batch = [(ref_text,a) for a in sample_text]
> all_hallu_scores =  self.get_nli_score(nli_batch).tolist()
> hallu_score = np.mean(all_hallu_scores).item() # main ref hallu score
> --- `uncertainty/scorer.py`

> overall_confidence =  (self.beta * o) + ((1 - self.beta) * s) # confidence for response to question x
> --- `uncertainty/scorer.py`

These computations warrant the arithmetic result given the returned numbers; neither authenticates the reference answer. A countercase to equating low contradiction with knowledge is mutually consistent false answers: the inspected selector has no independent factual comparison that would distinguish them from consistent true answers.

> semantically_different = np.any(pred_label == 0,axis=1) # if any is contradiction, then it is semantically different
> semantically_similar = ~semantically_different
> --- `uncertainty/scorer.py`

This is weaker than [EPI-CLM-semantic-clustering](#epi-clm-semantic-clustering): predicted neutrality in both directions passes the similarity mask. The computed class probabilities select among passing representatives; they do not require both directions to be entailment. This is an implementation deduction, not a measured clustering error.

Alternative-route reachability is qualified, not assumed: `get_dpo_sample` accesses `all_hallu_scores` before scorer-specific branching, while BSDetector returns `all_nli_scores` and semantic_consistency returns clusters/entropy instead. A caller would need compatible fields to reach their preference branches. The supplied runtime's broad scorer-selection wording is therefore read as available code branches, not demonstrated successful DPO invocation in all methods. This limit does not invalidate its SelfCheckGPT baseline.

> if len(raw_answer_sample) != len(content_dict['all_hallu_scores']):
>     if multiple_pref:
>         return [None]
>     else:
>         return None
> --- `uncertainty/scorer.py`

#### EPI-RTE-preference-selection
Label: Training example selection

Part of: [RT-RTE-model-training](runtime.md#rt-rte-model-training)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SFT training text or DPO chosen/rejected triples; invalid samples omitted.
- Later read-back: inapplicable — selection itself returns current training inputs; saved-parameter read-back belongs to the parent route and checkpoint consumer.
- Delegated visibility: Trainer receives formatted labels or prompt/chosen/rejected text, not an independent certificate of truth or the complete document/score provenance.
- Selection predicate: Optional known-question threshold; positive unknown threshold versus full-dataset fallback; answer-score extrema or cluster ranks; reference-as-chosen override for the single-preference pair and first multiple-preference pair only; later multiple-preference pairs use selected gold samples; optional length-difference exclusion.
- Invalidation or expiry: Current training invocation rebuilds selected examples; no judge-driven retroactive withdrawal of old examples or automatic rollback of saved model is wired in the parent chain.
- Activation or effect: Examples admitted to SFT/DPO optimization; when reference-as-chosen is enabled, extracted gold_answer is enforced as chosen only in the single-preference pair and first multiple-preference pair. Later pairs use selected gold_answer_sample entries, not necessarily the reference. Neither path enforces factual correctness.
- Evidence limits: No training data/trace supplied; alternate scoring compatibility limits in EPI-RTE-score-evidence apply; no benefit or factual acceptance established.

Endpoints: reloaded candidates/scores → `return_question_type` → `get_dpo_sample` → optional `normalize_ds_seq_length` → formatter → trainer. Owner: Python policy. Operator supplies configuration and starts optimization; models propose answer text and scores; code decides inclusion, and operator can decline to launch/use a checkpoint. Intended use/scope is configured optimization, not public reliance on each answer's truth. Guidance is fixed thresholds, extrema, flags and loss settings. Parent [RT-RTE-model-training](runtime.md#rt-rte-model-training) supplies trigger, save, selection bypass and recovery evidence. The later behavioral-authority path is [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption), not an independently tested correctness gate. Evidence: SRC-1, `uncertainty/scorer.py`, `uncertainty/train.py`, `uncertainty/data_utils.py`, `uncertainty/self_learning_training.py`.

> chosen_ans = all_answers[min_hallu_id]
> rejected_ans = all_answers[max_hallu_id]
> rejected_hallu_score = np.max(all_hallu_scores)
> --- `uncertainty/scorer.py`

Reference override evidence is in [RT-RTE-model-training](runtime.md#rt-rte-model-training). The override sets `chosen_ans = gold_answer`, which the single-preference constructor and first multiple-preference constructor consume. The later multiple-preference loop instead writes `chosen_ans` from `g[0]`, a selected `gold_answer_sample` entry; it need not equal the extracted reference. The training driver uses `extend` to admit those later pairs too. Thus reference identity is enforced only for the single pair or initial pair when the flag is enabled, not uniformly across the multiple-preference result. This preserves the supported override without granting additional epistemic warrant (SRC-1, `uncertainty/scorer.py`, `uncertainty/train.py`).

Multiple-preference filtering compares gold-sample scores against `question_filtering` when it is below one and raw-sample scores against positive `unknown_filtering`; otherwise candidate positions remain available for sampling. It adds no independently expected answer. The later-pair constructor and training admission passages are retained in [RT-RTE-model-training](runtime.md#rt-rte-model-training). Length normalization excludes records whose chosen/rejected length gap exceeds the current mean, rather than changing answer truth.

> diff = [abs(c-r) for c,r in zip(chosen_len,rejected_len)]
> mean_diff = np.mean(diff)
> rejected_mask = [1 if d > mean_diff else 0 for d in diff]
> out_ds = [d for d,m in zip(ds,rejected_mask) if m == 0]
> --- `uncertainty/data_utils.py`

> return HFDataset.from_dict({
>     'prompt': prompt,
>     'chosen': chosen,
>     'rejected': rejected,
> })
> --- `uncertainty/self_learning_training.py`

The DPO consumer receives these three fields; no source document or evidence certificate travels through this formatter. This is operational use of selected candidates, not lifecycle integration after acceptance of their factual assertions.

### Claims

#### EPI-CLM-semantic-clustering
Label: Bidirectional entailment clustering

Claimed operation: `cluster_semantic_sets` describes grouping according to bidirectional entailment. Evidence: SRC-1, `uncertainty/scorer.py`, doctrine/design in its method docstring. Distinct from [RT-CLM-knowledge-filtering](runtime.md#rt-clm-knowledge-filtering): this claims the clustering criterion, not the context-conditioned knowledge-score workflow. Implementation comparison belongs to [EPI-RTE-score-evidence](#epi-rte-score-evidence); no observed clustering result or benefit is supplied.

> Developed for semantic_consistency scoring method
> Cluster responses according to bidirectional entailment
> return cluster of responses
> --- `uncertainty/scorer.py`
