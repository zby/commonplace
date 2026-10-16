---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "KBLaM epistemic routes: synthetic references, numerical knowledge consumption, answer checks and the limits of reliance."
run-id: AAS-2026-10-15-kblam-5a0c2fe96cc1-01
reviewed-boundary: "69683ad096e022b58854fd88c0c58968c7d8c470"
---

# KBLaM epistemic report

## Source-and-claim boundary

The question is how KBLaM's shipped research workflow acquires or produces answerable content, checks it, and gives it consequential use. The whole-system functional boundary and exclusions are those in [boundary](boundary.md#boundary-and-evidence); evidence identities and unavailable assets are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. This report does not treat an upstream dataset card, a model's judgment, or a checkpoint filename as independent evidence of truth.

The consequential public claims are [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation) and [RT-CLM-base-preservation](runtime.md#rt-clm-base-preservation). Research scope and explicit warnings about incorrect answers bound their interpretation. The target is not claiming autonomous scientific discovery. Synthetic facts can be truth-apt relative to a stipulated fictional KB without being historical claims about the real world.

### Coverage

Direct reads below are SRC-1 at the frozen commit. Supplied findings are distinguished rather than represented as fresh inspection. No target execution was performed.

| Entry point or operation | Source path | Evidence and coverage | Limit and conclusion prevented |
|---|---|---|---|
| Package entry surface | `pyproject.toml` | Direct full read: package dependencies/build, no console-script registration | Does not establish runtime installation or external hooks |
| Evaluation dispatch | `experiments/eval.py` | Direct `main`, generation/refusal bodies; dispatch names generation, accuracy, acc_results, refusal, standard; supplied [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation), [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) cover driver paths | Other evaluator bodies rely on supplied findings; metric reproduction unobserved |
| Accuracy and saved-attention reanalysis | `experiments/eval.py` | Supplied [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation) | Row-index attention oracle, not answer-truth oracle |
| Standard paired KB/no-KB evaluation and notebook | `experiments/eval.py`, `eval_acc.ipynb` | Supplied runtime evaluation account and boundary notebook coverage | No observed intervention; neither causal benefit nor successful notebook execution follows |
| Synthetic/related entity production, reload, perturbation, augmentation | `dataset_generation/gen_synthetic_data.py` | Direct proposal/parser/postprocessing/augmentation/CLI bodies; [EPI-RTE-template-qa](#epi-rte-template-qa), [EPI-RTE-augment-qa](#epi-rte-augment-qa); supplied [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) | Provider output and full synthetic LFS payload unavailable; normal CLI has a misspelled method call |
| JSONL append, refusal reference, multi-entity assembly | `src/kblam/utils/data_utils.py` | Direct full read; [EPI-RTE-template-qa](#epi-rte-template-qa) | Serialization is not factual acceptance |
| Embeddings, splits, cached or online encoder | `dataset_generation/generate_kb_embeddings.py`, `dataset_generation/create_train_test_split.py`, `src/kblam/kb_encoder.py` | Supplied [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder) | No independent semantic-fidelity check or pinned provider weights established |
| Processor, direct model tensors, Llama/Phi attention, optional pruning | `src/kblam/models/kblam_processor.py`, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py` | Supplied [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference), [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention) | Direct callers bypass processor; no semantic approval gate implied by tensor compatibility |
| Answer formatting and cleanup | `src/kblam/utils/eval_utils.py` | Direct full read; [EPI-RTE-answer-cleanup](#epi-rte-answer-cleanup) | Text extraction can lose content before scoring |
| ROUGE/BERTScore and refusal scoring | `experiments/eval.py` | Direct generation/refusal bodies; [EPI-RTE-metric-inputs](#epi-rte-metric-inputs) | Lexical/semantic similarity and a substring are bounded proxies; metric package internals uninspected |
| Reference-answer scorer | `experiments/output_scorer.py` | Direct full read; supplied [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) | Configurable model judge, not independent oracle; default GPT4 rejected by client allowlist |
| Open-ended scorer | `experiments/output_scorer_open_ended.py` | Direct full read; [EPI-RTE-open-judgment](#epi-rte-open-judgment) | Normal batch completion lacks a return; persisted partial scores need not yield a mean |
| Azure chat/embedding CLI and client | `src/kblam/gpt_session.py` | Direct full read; [RT-CMP-gpt-session](runtime.md#rt-cmp-gpt-session), [EPI-RTE-augment-qa](#epi-rte-augment-qa) | Opaque mutable deployment; client retries concern response presence, not truth |
| Training, optimizer, save/resume, reload | `experiments/train.py`, `src/kblam/utils/train_utils.py`, `experiments/eval.py` | Supplied [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training), [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) | No observed later exercise or validation-selected successor; save/resume mismatch retained |
| Test, dataset-card and command-wiring surfaces | `tests/test_kb_encoder.py`, `tests/test_dataset_construction.py`, `datasets/datasetcard_enron.md`, `datasets/datasetcard_synthetic.md`, `experiments/Makefile` | Supplied boundary coverage, not fresh content-quality inspection | Shape/loading tests do not authenticate factual references; upstream Enron extraction remains attributed |

External pretrained/checkpoint assets, complete synthetic data, historical embedding provenance, provider internals, and end-to-end traces are missing. These respectively prevent exact parametric-content individuation, full-corpus assessment, embedding lineage authentication, provider-process assessment, and exercised-route/benefit conclusions. Available but uninspected internals are not access gaps. This coverage supports the positive routes below and bounded negatives within inspected consumers, not an exhaustive system-wide denial of every possible acceptance or criticism mechanism.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-entity](#epi-obj-entity) | Name-property assertions, stipulated or externally supplied | Entity | See record | Source warrant unknown; synthetic assignment is not real-world verification |
| [EPI-OBJ-data-point](#epi-obj-data-point) | Same property as an explicit QA reference | DataPoint | See record | Template copying preserves inputs, not their truth |
| [EPI-OBJ-extended-qa](#epi-obj-extended-qa) | Model-written extended answer and perturbed question | extended_Q / extended_A | See record | Preservation versus novel assertion is output-dependent; not determinable without outputs |
| [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder) | No individually recoverable proposition established in projections/base vectors | KBEncoder | See record | Numerical transformation affects use; semantic preservation unchecked |
| [RT-CMP-llama3-model](runtime.md#rt-cmp-llama3-model), [RT-CMP-phi3-model](runtime.md#rt-cmp-phi3-model) | Individual parameter-encoded claims not determinable | Model weights | See records | Exact assets unavailable; fixed-weight evaluation does not prove lack of knowledge influence |
| [EPI-OBJ-model-output](#epi-obj-model-output) | Decoded candidate answers or refusals | Model output | See record | A fluent answer is not an accepted proposition |
| [EPI-OBJ-eval-example](#epi-obj-eval-example) | Container for two script-local judgment record types; parts assessed below | EvalExample | See record | Container does not give the distinct judgments a common evaluator or license |
| [EPI-OBJ-reference-judgment](#epi-obj-reference-judgment) | Scalar assessment of candidate text relative to a supplied answer | EvalExample | See record | Reference-relative judgment, not independent factual confirmation; no calibration evidence |
| [EPI-OBJ-open-judgment](#epi-obj-open-judgment) | Evidence-relative and common-sense assessment with numeric score and stated reason | EvalExample | See record | Rationale-bearing plausibility judgment does not verify open-ended claims; no calibration evidence |

## Authority-route ledger

Own assessments below separate checking from disposition and storage from integration. A `see` cell delegates the canonical field to its linked declaration. Multiple rows may cite one container because its functions have different force. Implementation is not evidence of activation. Source and passage ownership follows the cited records.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) | content transformation | implemented | [EPI-OBJ-entity](#epi-obj-entity) | truth-apt transformation: acquisition/import | Caller records or provider-generated entity assertions enter local data | No independent factual evaluator; scope is supplied/synthetic KB | See route | See route | See route | Source warrant unknown; entity-generation request proposes fictional assignments, not validated historical facts | See route | See route | See route | none | none | External model is producer, not inspected evidence-consuming acceptance authority |
| [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) | disposition/acceptance | implemented | [EPI-OBJ-entity](#epi-obj-entity) | no content change | Provider response to Entity and saved row | JSON decoding/dataclass construction; structural domain | See route | Parse failures skipped; constructible rows may be saved | Enforcing structural admission | Syntactic compatibility only; not epistemic acceptance for factual use | See route | See route | See route | none | none | Dataclass construction is not semantic type or truth validation |
| [EPI-RTE-template-qa](#epi-rte-template-qa) | content transformation | implemented | [EPI-OBJ-data-point](#epi-obj-data-point) | truth-apt transformation: non-ampliative reshaping | Property to question, answer and key; multi-entity answer concatenation | Code templates; aligned names/properties/answers domain | See route | See route | See route | Conditional preservation of source strings, not independent truth | See route | See route | See route | none | none | No new warranted premise produced |
| [EPI-RTE-augment-qa](#epi-rte-augment-qa) | content transformation | implemented | [EPI-OBJ-extended-qa](#epi-obj-extended-qa) | truth-apt transformation: indeterminate | Model rewrites question or extends QA | Model proposal; regex checks extractability only | See route | See route | See route | No checked entailment or source fidelity; ampliative claims possible, not established by request alone | See route | See route | See route | none | Runtime guidance qualification | Intended QA-only system guidance is not delivered by generate_response; CLI typo also blocks ordinary continuation |
| [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) | retention | implemented | [EPI-OBJ-data-point](#epi-obj-data-point) | no content change | Appended rows, cached arrays and paired partitions | File/path and split rules, not a factual evaluator | See route | See route | See route | Retention licenses no additional truth claim | See route | See route | See route | none | none | No lifecycle integration inferred from storage/reload; no semantic expiry |
| [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention) | operational admission/selection/consumption | implemented | [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder) | no content change | Numerical knowledge contribution at configured layers | Shape/config branches, attention and optional Llama top-k | See route | See route | See route | Attention relevance/rank is not factual acceptance | See route | See [RT-BAP-knowledge-attention](runtime.md#rt-bap-knowledge-attention) | See route | [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation) | none | Phi has no inspected pruning counterpart; Llama score slicing qualification retained |
| [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference) | content transformation | implemented | [EPI-OBJ-model-output](#epi-obj-model-output) | truth-apt transformation: indeterminate | Inputs and parameters to decoded answer | Learned token computation; no per-answer evidence-consuming acceptor | See route | See route | See route | Could restate KB, draw an inference, or invent content; exact relation needs actual input/output and checks | See route | See route | See route | [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation) | none | Defective convenience loader does not remove direct-tensor route |
| [EPI-RTE-answer-cleanup](#epi-rte-answer-cleanup) | content transformation | implemented | [EPI-OBJ-model-output](#epi-obj-model-output) | truth-apt transformation: indeterminate | Decoded text to extracted answer body | Global marker replacement and question splitting, not semantic evaluator | See route | See route | See route | Formatting intent does not prove preservation on arbitrary text | See route | See route | See route | none | none | A concrete repeated-question countercase loses subsequent content |
| [EPI-RTE-metric-inputs](#epi-rte-metric-inputs) | disposition/acceptance | implemented | [EPI-OBJ-model-output](#epi-obj-model-output) | no content change | Eligibility for generation-metric population | Optional case-sensitive sorry substring test | See route | See route | Enforcing omission from metric inputs/export | No license to regard retained outputs as true or unbiased population | See route | See route | See route | none | none | Declared refusal can be dropped rather than counted; not answer correction |
| [EPI-RTE-metric-inputs](#epi-rte-metric-inputs) | check/evidence production | implemented | [EPI-OBJ-model-output](#epi-obj-model-output) | no content change | Extracted answer similarity; refusal classification | ROUGE/BERTScore versus descriptions; sorry test versus index labels | See route | See route | Measurement/reporting, not answer veto | Reference-relative score and refusal-string detection only | See route | See route | See route | [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation) | none | Metrics cannot authenticate synthetic references or justify explanations |
| [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation) | check/evidence production | implemented | [RT-CMP-llama3-model](runtime.md#rt-cmp-llama3-model) | no content change | Selected KB row attention rank | Code row-position oracle; tensor ranking domain | See route | See route | See route | Attention-index correctness, not answer truth or causal grounding | See route | See route | See route | [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation) | none | No component effect inferred from a high attention score |
| [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) | check/evidence production | implemented | [EPI-OBJ-reference-judgment](#epi-obj-reference-judgment) | truth-apt transformation: indeterminate | Answer versus exported True answer | GPT reference-comparison prompt, 0–1 numeric parse | See route | See route | See route | Model judgment relative to supplied reference, not an independent oracle | See route | See route | See route | none | none | Prompt's own high-score example tolerates property mismatch; no calibrated truth license |
| [EPI-RTE-open-judgment](#epi-rte-open-judgment) | check/evidence production | implemented | [EPI-OBJ-open-judgment](#epi-obj-open-judgment) | truth-apt transformation: indeterminate | Evidence/question/response groundedness and reasonableness | GPT rubric, 0–5 score/reason extraction | See route | See route | See route | Common-sense plausibility and evidence-relative assessment, not confirmation of open-ended claims | See route | See route | See route | none | Omitted detailed scorer now covered | Normal batch return missing; model default rejected |
| [EPI-RTE-open-judgment](#epi-rte-open-judgment) | retention | implemented | [EPI-OBJ-open-judgment](#epi-obj-open-judgment) | no content change | Parsed score/reason to appended JSONL | Float/regex success and file I/O | See route | See route | File retention | Not evidence-consuming acceptance of the judged answer | See route | See route | See route | none | none | No downstream deployment or KB-update consumer found in this script |
| [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) | behavior/policy adaptation | implemented | [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder) | non-truth-apt policy/content update: numerical parameter optimization | Token predictions versus dataset expected tokens | Weighted cross-entropy, AdamW; supervised training domain | See route | See route | See route | Loss expresses fit to supervision, not source truth or validated capacity improvement | See route | See [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) | See route | none | none | No formulated theory or criticism inferred from gradients |
| [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) | retention | implemented | [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder) | no content change | Periodic parameter/config saves | Configured step period, not validation acceptance | See route | See route | See route | Checkpoint persistence does not confer epistemic warrant | See route | See [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) | See route | none | none | Save/resume naming mismatch; later causal exercise unobserved |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation) | See record | See record | See record | [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention), [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes), [EPI-RTE-metric-inputs](#epi-rte-metric-inputs), [EPI-RTE-open-judgment](#epi-rte-open-judgment) | None supplied | Paired source-level comparisons are not executed interventions; no component isolation | Numerical KB influence is wired without an external search service; bounded evaluation procedures exist | Grounded truth and scaling benefits unmeasured; internal top-k selection qualifies a broad no-retrieval reading; dataset similarity is not factual verification |
| [RT-CLM-base-preservation](runtime.md#rt-clm-base-preservation) | See record | See record | See record | [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention), [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) | None supplied | No exact-output equivalence comparison; loaders, formatting and decoding remain auxiliary conditions | Conditional numerical KB bypass | Universal exact-output equality not established |

The reference judge's prompt includes a high-score example with different property labels. This is a limit of the declared rubric, not an observed scoring error:

> Model output: "The purpose of Alexandria is to extract knowledge."
> True answer: "The color of Alexandria is to discover and organize knowledge into a structured form."
> Score: 0.9
> --- `experiments/output_scorer.py`

The README itself supplies an important countercase to any interpretation of grounding as guaranteed correctness:

> When used with knowledge bases that are very different from the knowledge base it was trained on, KBLaM will give incomplete answers, and the answers can be reworded from the original value in the knowledge base or at times entirely incorrect.
> --- `README.md`

## Bounded conclusion

**KBLaM wires operational reliance on supplied knowledge, not a general truth-acceptance pipeline.** The generator/import route supplies entity assertions whose source warrant is unknown. Template QA construction preserves property strings under aligned inputs. It does not derive new real-world facts from independently warranted premises. Embedding projection and learned generation carry those inputs into numerical attention and decoded answers, but inspected evidence does not individuate the propositions in dense state or establish entailment of the output. Accordingly their truth-apt transformation relation remains indeterminate rather than being labeled conjecture merely because entailment is unproved. See [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), [EPI-RTE-template-qa](#epi-rte-template-qa), [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention), and [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference).

**The checks have different targets and licenses.** JSON/regex admission tests structural usability. Attention accuracy tests row ranking. Generation metrics test extracted-text similarity to a dataset value. Refusal scoring tests a lowercase substring against code-defined inclusion labels. Reference GPT scoring tests reference-relative answer quality. Open-ended GPT scoring requests groundedness plus reasonableness; its exemplar explicitly rewards a sensible extension, not independent verification of that extension. These do not share a single truth oracle. The scalar reference assessment [EPI-OBJ-reference-judgment](#epi-obj-reference-judgment) and rationale-bearing open-ended assessment [EPI-OBJ-open-judgment](#epi-obj-open-judgment) are separate operative objects: the former feeds list-return, save and mean reporting, while the latter is appended per record and has only an exception-prefix list return. Neither consumer path licenses factual acceptance. Optional refusal omission changes the evaluated population, and question-splitting/regex extraction changes what the metric consumer sees. None of these inspected evaluator consumers enforces a per-answer release gate or a validation-selected model successor. That is a bounded finding about these consumers, not an inferred absence throughout opaque model internals. See [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation), [EPI-RTE-answer-cleanup](#epi-rte-answer-cleanup), [EPI-RTE-metric-inputs](#epi-rte-metric-inputs), and [EPI-RTE-open-judgment](#epi-rte-open-judgment).

**Retention and use must not be promoted to acceptance or lifecycle integration.** Rows, embeddings, scores and checkpoints can persist, and selected records/parameters reach later model calls. The implemented authority is file admission, ranking/selection, numerical inference influence, or gradient update, with horizons recorded in the cited routes. There is no evidenced acceptance decision here naming factual criterion, intended use and scope for a newly produced ampliative claim. No post-acceptance lifecycle-integration route is established by these records. Existing-file skips, append/save operations and manual file selection do not demonstrate semantic invalidation, withdrawal or a quality-based rollback. See [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training), [RT-BAP-knowledge-attention](runtime.md#rt-bap-knowledge-attention), and [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption).

**Training supports a separate, bounded adaptation conclusion.** Dataset loss causally shapes parameter updates in inspected code; checkpoints can later determine projection and generation machinery. This is not itself localized formulated criticism, reflection, or a theory-builder loop. Improved future capacity and exercised self-improvement remain unestablished without outcomes and later operation causally depending on the saved change. The source supports an improvement-directed dispositional update path with the supervised-answer objective, not a successful-improvement verdict. Autonomy of bounded numerical steps does not establish autonomous conduct of the whole research workflow. These limits are independent of the positive knowledge-consumption route. See [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training).

**Two implementation qualifications matter to claims about operation.** Intended QA-only augmentation guidance is assigned to a different attribute from the one the chat wrapper consumes. The normal generator CLI also stops at a misspelled method unless externally repaired. The open-ended scorer persists parsed records in its loop but returns a list only on an exception; its normal completion yields no list for the mean-score caller. These are source deductions, not observed failures. They prevent claiming a turnkey semantic-curation/evaluation pipeline while leaving the separately implemented library and direct-model routes intact. See [EPI-RTE-augment-qa](#epi-rte-augment-qa) and [EPI-RTE-open-judgment](#epi-rte-open-judgment).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-entity
Label: Entity

SRC-1, `src/kblam/utils/data_utils.py`, `dataset_generation/gen_synthetic_data.py`: named description/objectives/purpose values in an Entity dataclass. Values are natural-language assertions; field names and JSON structure are symbolic. Storage is Python objects and appended JSONL. Closest supplied record is [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), a process container rather than an object counterpart. The record includes caller-loaded entities as well as generated ones. A generated synthetic description may define a fictional entity rather than report a real-world fact. No independent factual provenance is recorded by this dataclass.

> class Entity:
>     name: str
>     description: str
>     objectives: str
>     purpose: str
> --- `src/kblam/utils/data_utils.py`

#### EPI-OBJ-data-point
Label: DataPoint

SRC-1, `src/kblam/utils/data_utils.py`, `dataset_generation/gen_synthetic_data.py`: the ordinary name, description_type, description, Q, A and key_string fields. Symbolic field structure carries natural-language property and answer content in memory/JSONL; numerical encoding is a downstream distinct part. Closest supplied record is [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), not an object counterpart. Optional extension fields are split into [EPI-OBJ-extended-qa](#epi-obj-extended-qa) because a model, not the property template, produces them. Later consumers include embedding, training and evaluation drivers; source-provenance metadata is not supplied by these fields.

> class DataPoint:
>     name: str
>     description_type: str
>     description: str
>     Q: str = None
>     A: str = None
>     key_string: str = None
> --- `src/kblam/utils/data_utils.py`

#### EPI-OBJ-extended-qa
Label: extended_Q and extended_A

SRC-1, `dataset_generation/gen_synthetic_data.py`, `src/kblam/utils/data_utils.py`: optional natural-language QA extensions plus model-written perturbed Q. Stored in DataPoint objects and exported JSONL by the driver. They differ from ordinary QA in producer and unchecked semantics; they are not a separately encoded model component. Closest supplied [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) contains their production, not an object declaration. [EPI-RTE-augment-qa](#epi-rte-augment-qa) supplies passages and the guidance-delivery qualification. No actual generated extension is supplied here.

#### EPI-OBJ-model-output
Label: Model output

SRC-1, `src/kblam/utils/eval_utils.py`, `experiments/eval.py`: natural-language decoded answers and refusal text, held in Python strings and optionally exported prediction text. Token IDs are a symbolic intermediate; generation weights and KV tensors are separate distributed-parametric machinery. Closest supplied [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference) and [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) are production/consumption routes, not duplicate objects. Later consumers see cleaned/extracted text, not necessarily the whole decoded sequence. Passages are in [EPI-RTE-answer-cleanup](#epi-rte-answer-cleanup) and [EPI-RTE-metric-inputs](#epi-rte-metric-inputs).

#### EPI-OBJ-eval-example
Label: EvalExample

SRC-1, `experiments/output_scorer.py`, `experiments/output_scorer_open_ended.py`: two distinct script-local EvalExample dataclasses, retained here as a container for [EPI-OBJ-reference-judgment](#epi-obj-reference-judgment) and [EPI-OBJ-open-judgment](#epi-obj-open-judgment), whose payloads, checks and consumers are assessed separately. Reference scorer stores text/true_answer/score; open-ended scorer stores evidence/question/response/score/reason. Numeric fields and JSON names are symbolic; reason and candidate/reference strings are natural language. Storage is lists and appended JSONL. The ledger splits the open-ended evaluator from the supplied reference-judge route [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes). Neither is a supplied object counterpart. Scores are assessments, not evidence that the underlying candidate was factually accepted.

> class EvalExample:
>     evidence: str
>     question: str
>     response: str
>     score: float
>     reason: str
> --- `experiments/output_scorer_open_ended.py`

#### EPI-OBJ-reference-judgment
Label: Reference scorer EvalExample
Part of: [EPI-OBJ-eval-example](#epi-obj-eval-example)

SRC-1 implementation, `experiments/output_scorer.py`: the reference scorer's script-local dataclass has text, true_answer and score, with no rationale field. Its natural-language candidate/reference strings and symbolic float/field structure live in Python lists and appended JSONL. This is the scalar-reference part of the retained container, distinct from [EPI-OBJ-open-judgment](#epi-obj-open-judgment) in payload, evaluator target and consumer path. Closest supplied [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) describes its evaluator, not an object counterpart. The provider's numeric response is admitted by float conversion without a 0–1 range gate. Batch errors skip individual examples; successful records return as a list, then the main block saves each record and computes a mean of their scores. These consumers give reporting and retention force, not answer-release or model-selection authority. The intended license is only comparison with supplied true_answer; neither that label nor a score establishes source truth or calibrated correctness.

> class EvalExample:
>     text: str
>     true_answer: str
>     score: float
> --- `experiments/output_scorer.py`

> score = self.generate_response(prompt)
> example = EvalExample(text, true_answer, float(score))
> return example
> --- `experiments/output_scorer.py`

> for example in eval_examples:
>     save_example(example, args.output_file)
>
> mean_score = np.mean([example.score for example in eval_examples])
> --- `experiments/output_scorer.py`

#### EPI-OBJ-open-judgment
Label: Open-ended scorer EvalExample
Part of: [EPI-OBJ-eval-example](#epi-obj-eval-example)

SRC-1 implementation, `experiments/output_scorer_open_ended.py`: the evidence/question/response/score/reason dataclass quoted in the container is this script-local part. Natural-language evidence, question, response and reason coexist with symbolic field names and float score in Python lists and appended JSONL. Unlike [EPI-OBJ-reference-judgment](#epi-obj-reference-judgment), this part carries an explanatory judgment about groundedness and common-sense reasonableness, not a scalar comparison against a designated true_answer. Closest supplied [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) explicitly leaves the detailed open-ended scorer unassessed; it supplies no object counterpart. [EPI-RTE-open-judgment](#epi-rte-open-judgment) owns the rubric, extraction and retention passages: regex/float success admits score/reason without a 0–5 range gate, and each parsed record is appended before batch completion. Its reason is model-produced assessment content, not independent evidence for the candidate. No observed result establishes whether a particular reason follows from evidence. Normal completion returns None; a caught exception returns an accumulated prefix that the caller may average. Therefore per-record retention is wired, but completed aggregate reporting and downstream answer acceptance are not established.

### Routes

#### EPI-RTE-template-qa
Label: Template QA construction
Part of: [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production)

SRC-1 implementation, `dataset_generation/gen_synthetic_data.py`, `src/kblam/utils/data_utils.py`. Owner: deterministic helper code; Entity property values become DataPoint QA/key strings. The separate multi-entity helper joins aligned answers with name/property labels. This is non-ampliative reshaping on aligned, faithfully interpreted property strings, not factual checking or a novel conclusion. Code proposes and admits the formatted strings without human per-row approval or semantic veto. Operating mode is bounded dataset preparation. No independent answer oracle is consulted; source property values are the references. File replacement is caller-controlled; no factual rollback is implemented in these helpers.

- Immediate return: Q/A/key_string tuple or multi-entity question/answer tuple, then DataPoint rows.
- Later read-back: driver can append these rows for later embedding/training/evaluation; helpers themselves do not reload.
- Delegated visibility: inapplicable — deterministic local helpers, no delegated principal.
- Selection predicate: three entity property keywords in post_process_data; supplied aligned lists in multi-entity helper.
- Invalidation or expiry: inapplicable — no validity metadata or retained helper state; caller controls persisted files.
- Activation or effect: formatting wiring preserves descriptions as answer strings; no output run is observed.
- Evidence limits: copying an unsupported source assertion creates no warrant; mismatched names/answers invalidate the aligned-input interpretation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Q = "What is the {} of {}?".format(entity.description_type, entity.name)
> A = f"The {entity.description_type} of {entity.name} is {entity.description}."
> key_string = f"the {entity.description_type} of {entity.name}"
> return Q, A, key_string
> --- `dataset_generation/gen_synthetic_data.py`

> for answer, name, property in zip(answers, names, properties):
>     answer_str += f"The {property} of {name} is {answer}; "
> return templates[template_idx].format(question_body), answer_str.strip()
> --- `src/kblam/utils/data_utils.py`

Concrete source deduction, not execution: a DataPoint named `Atlas`, description_type `purpose`, description `store records` becomes Q `What is the purpose of Atlas?`, A `The purpose of Atlas is store records.`, key `the purpose of Atlas`. No predicate not already in the property assignment is warranted by that formatting.

#### EPI-RTE-augment-qa
Label: Model QA augmentation and name perturbation
Part of: [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production)

SRC-1 implementation, `dataset_generation/gen_synthetic_data.py`, `src/kblam/gpt_session.py`. Owner: generator helper; provider proposes text; code extracts Q/A or overwrites Q and driver can save the modified rows. Separate identity from the parent is the model rewrite/extension portion, not a replacement of its other generation/embedding/split functions. No factual oracle, evidence-consuming acceptance, human per-item veto or semantic rollback is wired. Exceptions skip an item; caller may externally replace files. Mode: bounded augmentation. Proposed guidance asks for QA-only support but delivery is defective: the helper assigns `system_prompt`, whereas `generate_response` uses `system_msg`, set by the base constructor. The user prompt contains the QA pair, not that QA-only system constraint. Perturbation instructions, in contrast, are passed in the user prompt. Exact semantic relation is output-dependent and indeterminate.

This qualifies the guidance sentence in [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production): the constraint is present in source as intended guidance, not established as delivered guidance for extension calls. The parent remains a valid multi-function container; no supersession is needed.

- Immediate return: modified DataPoint list; extractable extension strings or replacement Q are assigned in place.
- Later read-back: CLI has append calls for modified rows, conditional on reaching them; no subsequent inference using those exact rows is observed.
- Delegated visibility: provider receives QA in a user prompt or a name-perturbation instruction; no inspectable child-agent process.
- Selection predicate: each supplied row; regex first Q/A match for extension; any returned string for perturbation.
- Invalidation or expiry: no semantic invalidation; existing rows remain on caught errors; no quality-based withdrawal.
- Activation or effect: mutation/save paths are implemented, but ordinary CLI calls nonexistent perturbe_names before extension; successful operation is not claimed.
- Evidence limits: actual model outputs absent; system_prompt is not consumed by generate_response; exceptions do not identify factual failures.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.system_prompt = """You are given a question and answer pair, please extend the question to be open-ended and generate a short answer.
>                                 For example, you could generate "What is the objective of xxx and what do you think of it?"
>                                 Make sure the answer is **only** based on information provided from the QA pair. In addition, please generate in the format of:
>                                 Q: ...
>                                 A: ...
>                             """
> --- `dataset_generation/gen_synthetic_data.py`

> gpt_output = self.generate_response(prompt)
> extended_q = re.findall(r"Q: (.*)", gpt_output)[0]
> extended_a = re.findall(r"A: (.*)", gpt_output)[0]
> data.extended_Q = extended_q
> data.extended_A = extended_a
> --- `dataset_generation/gen_synthetic_data.py`

> messages = [
>     {
>         "role": "system",
>         "content": self.system_msg,
>     },
>     {
>         "role": "user",
>         "content": prompt,
>     },
> ]
> --- `src/kblam/gpt_session.py`

> self.max_retries = max_retries
> self.system_msg = system_msg
> self.model_name = model_name
> --- `src/kblam/gpt_session.py`

> perturbed_dataset = data_generator.perturbe_names(dataset)
> --- `dataset_generation/gen_synthetic_data.py`

#### EPI-RTE-answer-cleanup
Label: Answer cleanup and question split
Part of: [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes)

SRC-1 implementation, `src/kblam/utils/eval_utils.py`, `experiments/eval.py`. Owner: local helper/evaluator. This is the cleanup portion from decoded sequence through header pruning and `.split(Q)[1]`; later metric extraction is [EPI-RTE-metric-inputs](#epi-rte-metric-inputs). The helper returns decoded full sequence with marker substitutions, not a token-indexed answer-only slice. Case-sensitive global replacements remove markers wherever they appear. A deterministic trace shows that formatting intent does not guarantee arbitrary semantic preservation.

- Immediate return: pruned decoded string from helper; evaluator selects the substring after the first occurrence of Q and before the next occurrence if any.
- Later read-back: inapplicable — this transformation retains no state; enclosing evaluator may export its result.
- Delegated visibility: inapplicable — local string operations, no delegated principal.
- Selection predicate: model family chooses marker replacements; caller's literal Q chooses split boundary.
- Invalidation or expiry: inapplicable — no persistent helper state.
- Activation or effect: transformed string, not complete decoded text, feeds subsequent metrics/export in the source.
- Evidence limits: expected generation contains echoed input, but absent/multiple Q occurrences can error or discard answer text; no observed output supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> S = S.replace("<|eot_id|>", "")
> S = S.replace("<|start_header_id|>assistant<|end_header_id|>", "\n\n")
> S = S.replace("<|start_header_id|>user<|end_header_id|>", "")
> S = S.replace("<|end_of_text|>", "")
> return S
> --- `src/kblam/utils/eval_utils.py`

> tokenizer, model, ins_prompt + Q, kb=None, kb_config=kb_config
> ).split(Q)[1]
> --- `experiments/eval.py`

Concrete source deduction: with Q `What is Atlas?` and helper text `What is Atlas? Atlas stores records. What is Atlas? It also indexes them.`, splitting and selecting index 1 gives only ` Atlas stores records. `. The later clause disappears before scoring/export. With a single Q and no literal markers in content, the same operation can preserve the intended answer; this countercase limits rather than universally invalidates cleanup.

#### EPI-RTE-metric-inputs
Label: Metric population and answer extraction
Part of: [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes)

SRC-1 implementation, `experiments/eval.py`. Owner: evaluator. Code optionally omits outputs containing `sorry`, then exports the surviving full answer/reference pairs while a regex-extracted variant reaches ROUGE/BERTScore. Ordinary single-entity references use row description; multi-entity references are template assemblies. Refusal evaluation uses a separate substring classification against included/excluded-index labels. Human supplies configuration/dataset, not per-result acceptance; code decides omission/measurement; model proposes answers. Domain: bounded answer similarity and refusal detection experiments. These are not epistemic acceptance decisions for real-world use, and no score threshold changes checkpoints in these bodies.

- Immediate return: exported full-output text plus metric dictionaries; refusal returns exported text and prediction/label arrays.
- Later read-back: exports can be read by separate scorer; supplied route covers output persistence; no score-to-KB or score-to-checkpoint admission established.
- Delegated visibility: metric packages receive extracted prediction/reference arrays; reference scorer may later send exported full answers to a provider.
- Selection predicate: sampled rows/mode, optional case-sensitive sorry omission, regex extraction; refusal labels are set by row inclusion/exclusion.
- Invalidation or expiry: no metric expiry or semantic withdrawal policy in these bodies.
- Activation or effect: omission and extraction change metric inputs; actual scores and benefits unobserved.
- Evidence limits: kb calls pass unsupported topk_size keyword to answer_question; package scorers are external; lexical refusal and similarity do not validate propositions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if remove_sorry:
>     if "sorry" in model_output:
>         continue
> full_outputs.append((model_output, answer))
> --- `experiments/eval.py`

> pattern = r'The\s+\w+\s+of\s+[^"]+\s+is\s+(.+)'
> match = re.search(pattern, model_output)
> answers.append(row["description"])
> if match:
>     model_output = match.group(1)
> --- `experiments/eval.py`

> rouge_scores = rouge.compute(predictions=model_outputs, references=answers)
> --- `experiments/eval.py`

> prediction = [int("sorry" in model_output) for model_output in model_outputs]
> --- `experiments/eval.py`

Deterministic deduction: with removal enabled, `The purpose is to say sorry to customers.` is excluded even if correct. A refusal `I cannot answer.` lacks `sorry` and is not classified as a refusal by this detector. Conversely, a conventional sorry refusal is detected. These countercases bound the evaluator's target; they do not purport to measure actual error rates.

#### EPI-RTE-open-judgment
Label: Open-ended response scoring

SRC-1 implementation, `experiments/output_scorer_open_ended.py`, `src/kblam/gpt_session.py`. No counterpart after comparison: [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) explicitly leaves this scorer's detailed rubric unassessed; its reference-answer scorer is a different operation. Owner: separately launched scorer. Input text split on delimiters is sliced by Evidence/Question/Model output labels, inserted into a model prompt, parsed to float score and reason, appended to list and saved JSONL. Target is evidence-relative accuracy/relevance plus common-sense reasonableness of an open-ended answer. Provider judges; regex/float code admits its result; no independent answer oracle or human per-item veto. Mode: bounded experiment, no automatic improvement trigger. The rubric's prompt examples are guidance, not demonstrated valid judgments. The parent's constructor overwrites the subclass system_msg/seed, but the substantive rubric remains in the user prompt.

- Immediate return: on caught exception returns the accumulated example list; on normal loop completion returns None implicitly.
- Later read-back: records are appended to args.output_file; normal CLI attempts a mean over the returned value; no downstream acceptance/deployment read found in this script.
- Delegated visibility: provider receives evidence, question and response in the rubric prompt; provider internals uninspected.
- Selection predicate: delimiter-split examples in order; regex extracts first matching Score/Reason, float accepts numeric score without a 0–5 range gate; exception returns early.
- Invalidation or expiry: append-only output in this script, no factual rollback or expiry; I/O errors print without withdrawing prior entries.
- Activation or effect: parsed scores/reasons reach files before the normal-return defect; source does not wire them into KB truth or model deployment authority.
- Evidence limits: default GPT4 is outside valid_models; compatible model and provider/assets required; no observed judged example, calibrated validity or successful aggregate run supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Evaluate the response based on how grounded it is given the evidence and how reasonable it is.
> Return an integer score and step by step explanation of how you arrived at the score.
> Score of 5 means the response is accurate, relevant and reasonable (in that it meets common sense).
> --- `experiments/output_scorer_open_ended.py`

> Model output: "GreatTool is an app that helps users to be more productive. It may affect the community by helping users to organize their tasks and manage their time better improving their productivity."
> Score: 5
> Reason: The model's response is accurate and relevant to the question and evidence and the open ended part is sensible and reasonable.
> --- `experiments/output_scorer_open_ended.py`

> score = float(re.search(score_pattern, eval_example).group(1).strip())
> reason = re.search(reason_pattern, eval_example).group(1).strip()
> --- `experiments/output_scorer_open_ended.py`

> eval_examples.append(eval_example)
>
> save_example(eval_example, args.output_file)
>
> except Exception as e:
>     print("Error evaluating example.")
>     print(e)
>     return eval_examples
> --- `experiments/output_scorer_open_ended.py`

> eval_examples = eval.evaluate_output_batch(examples)
> mean_score = np.mean([example.score for example in eval_examples])
> --- `experiments/output_scorer_open_ended.py`

The exception-only return is at the end of the method; direct full-file inspection establishes no normal return. Countercase: a late exception returns a partial list which may support a mean of only its prefix. Neither that conditional result nor normal per-record retention establishes completed evaluation of the requested batch.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
