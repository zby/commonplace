---
description: "Self-Training-LLM review: offline Wikipedia QA self-training pipeline that turns model answer rollouts and uncertainty scores into SFT/DPO datasets and checkpoints"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Self-Training-LLM

Self-Training-LLM, from wj210, is not a deploy-time agent memory layer. It is an offline self-training pipeline for reducing factual hallucination on Wikipedia-style question answering: generate document-grounded questions, sample model answers with and without document context, score uncertainty or hallucination, build SFT and DPO datasets, and train new model checkpoints. Its retained behavior-shaping artifacts are generated corpora, scored rollout files, training datasets, and learned model weights rather than memories retrieved into an agent's prompt.

**Repository:** https://github.com/wj210/Self-Training-LLM

**Reviewed commit:** [97839b29d0fd8bb474f5549fa3e9d6ca504732e0](https://github.com/wj210/Self-Training-LLM/commit/97839b29d0fd8bb474f5549fa3e9d6ca504732e0)

**Last checked:** 2026-05-16

## Core Ideas

**The storage substrate is experiment files and model artifacts, not a memory service.** The README presents the project as scripts around `uncertainty/`, with `wiki_ques_gen.sh` generating SFT/DPO data and knowledge filtering, `train.sh` running SFT and DPO, `testing.sh` evaluating models, and `tgi.sh` serving a model through Hugging Face Text Generation Inference ([README.md](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/README.md), [script/wiki_ques_gen.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/wiki_ques_gen.sh), [script/train.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/train.sh), [script/testing.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/testing.sh), [script/tgi.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/tgi.sh)). The configured retained paths are under `data/wiki/`, `responses/`, `test_results/`, and `model_checkpoints/`, with TinyLlama as the example base model ([configs/model/tinyllama.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/model/tinyllama.yaml)). These files are the durable state; there is no database, vector store, runtime memory API, or agent-facing retrieval interface.

**Wikipedia documents become the source corpus for synthetic supervision.** The data config selects the `wikimedia/wikipedia` dataset, subset `20231101.en`, and file paths for generated test data ([configs/data/wiki.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/data/wiki.yaml)). `get_wiki` loads the Hugging Face dataset or selects predefined topics, while `get_predefined_topics` splits category/topic pairs into train and test sets and cleans documents by cutting references and "see also" sections ([uncertainty/data_utils.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/data_utils.py), [uncertainty/topic_generator.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/topic_generator.py)). The document chunks and generated questions are knowledge artifacts: they preserve evidence and task context used later by scoring, filtering, and training.

**Question and answer generation are staged to separate context-supported answers from model uncertainty.** `wiki_generation.py` chunks Wikipedia documents, asks OpenAI models to produce questions, writes reusable question JSONL, creates a held-out test set, and generates answers either with document context or without it depending on the training phase ([uncertainty/wiki_generation.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [uncertainty/templates.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/templates.py)). In the DPO path, the reference or chosen answer can come from document-grounded generation, while sampled raw answers are generated without document context so the system can identify where the model's internal knowledge is weak. This is a training-time analogue of memory: external source context creates labels, but the final behavior is meant to be absorbed into weights.

**The scoring layer turns answer rollouts into selection signal.** `NLIScorer` supports `SelfCheckGPT`, `BSDetector`, and `semantic_consistency` modes. It compares reference answers and sampled answers with NLI models, can add self-reflection prompts, clusters semantically similar responses, computes hallucination/confidence/entropy values, and stores per-sample scores such as `all_hallu_scores` or NLI scores ([uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py), [uncertainty/utils.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/utils.py)). The scored answer pickle is an intermediate knowledge artifact until `get_dpo_sample` converts it into prompt/chosen/rejected training rows. At that point, the same data gains system-definition-artifact authority because it directly controls optimization.

**DPO construction treats unknown or hallucinated regions as training targets.** `return_question_type` classifies examples as known or unknown according to the selected score key and threshold; `train.py` filters to unknown examples for DPO, optionally filters high-quality questions first, and calls `get_dpo_sample` to choose preferred and rejected answers ([uncertainty/utils.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/utils.py), [uncertainty/train.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py), [uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py)). When `ref_as_chosen` is set, document-grounded answers become chosen responses and high-hallucination sampled answers become rejected responses. The operative representational form is mixed: prose questions and answers, symbolic scores and thresholds, and eventually distributed-parametric model state.

**Training compiles the dataset into checkpoints or merged adapter weights.** `train.py` selects SFT or DPO mode, loads generated datasets, applies filtering flags, and delegates to `do_train`; `self_learning_training.py` converts list rows into Hugging Face datasets, runs `SFTTrainer` or `DPOTrainer`, saves model outputs, and merges PEFT adapters back into model weights when PEFT is used ([uncertainty/train.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py), [uncertainty/self_learning_training.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/self_learning_training.py), [configs/training/sft_trainer.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/training/sft_trainer.yaml), [configs/training/dpo_trainer.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/training/dpo_trainer.yaml), [configs/training/lora.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/training/lora.yaml)). The checkpoint is the strongest retained artifact in the system: a distributed-parametric system-definition artifact with learning authority over future generations.

**Evaluation is post-training comparison, not memory governance.** `generate_response.py` produces model responses for test or known examples, and `pairwise_eval.py` compares a base response with a post-training response using a GPT-4o pairwise judge and document-grounded prompt ([uncertainty/generate_response.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/generate_response.py), [uncertainty/pairwise_eval.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)). This creates evaluation records and scores, but it does not implement artifact review, source invalidation, retirement, rollback policy, or a governed promotion path from an individual fact to a runtime memory.

## Comparison with Our System

| Dimension | Self-Training-LLM | Commonplace |
|---|---|---|
| Primary purpose | Offline self-training for factual QA from Wikipedia-derived synthetic data | Agent-operated methodology KB with durable notes, instructions, reviews, ADRs, and validation |
| Storage substrate | JSONL, pickle files, response logs, test-result text files, configs, and `model_checkpoints/` outputs | Git-tracked typed Markdown, source snapshots, generated indexes, review artifacts, schemas, and scripts |
| Representational form | Mixed: prose documents/questions/answers, symbolic scores/configs/thresholds, distributed-parametric checkpoints | Typed prose and frontmatter, symbolic type specs/validators/commands, authored links, generated indexes |
| Lineage | Rows carry topic/category/document/instruction fields, but generated artifacts lack strong prompt/run/model/source-span provenance | Source-pinned citations, replacement archives, statuses, validation, semantic review, and explicit type contracts |
| Activation | Behavior changes after training because weights are updated; optional RAG/test modes pass documents at inference | Search, indexes, links, skills, instructions, validators, and review workflows activate retained artifacts before or during agent work |
| Behavioral authority | Training datasets and configs have learning/configuration authority; checkpoints have generation authority | Notes advise, instructions and skills instruct, schemas validate, commands enforce or regenerate, reviews document evidence |

The closest alignment is the idea that a retained artifact matters only when it changes later behavior. Self-Training-LLM makes that change through training: answer samples and scores are not retrieved at inference time, but they are compiled into checkpoint weights. Commonplace makes behavior change through inspectable symbolic artifacts: notes, instructions, skills, schemas, generated indexes, and review gates.

The sharpest divergence is authority and auditability. In Self-Training-LLM, the strongest behavior-shaping artifact is a model checkpoint. Once the DPO or SFT data has been compiled into weights, a later consumer cannot easily inspect which Wikipedia paragraph, generated question, sampled answer, threshold, or judge decision caused a specific future answer. Commonplace keeps the source artifact and the behavior-affecting artifact closer together: a note, instruction, schema, or review can be read, diffed, validated, replaced, or retired.

This also explains why Self-Training-LLM should not be treated as deploy-time agent memory. It has no consumer surface that retrieves relevant past traces into a prompt, no memory write API, no per-agent state, no runtime lineage display, and no activation policy. Its memory-like mechanism is offline distillation: generated and scored traces feed learning, and the learned numerical state changes later generations.

The useful comparison for commonplace is therefore not "should we add this as a memory backend?" but "what does this show about trace-derived promotion into stronger authority?" Self-Training-LLM demonstrates an extreme promotion path: source corpus and rollouts become training data, and training data becomes weights. That is powerful, but the lineage and invalidation costs are much higher than promoting an observation into a note, instruction, test, or validator.

**Read-back:** push — learned checkpoint state affects generation automatically; there is no agent-facing retrieval step.

## Borrowable Ideas

**Separate evidence generation from uncertainty filtering.** Ready to borrow as a design principle. The pipeline distinguishes document-grounded question/answer generation from no-context sampled answers, making it possible to identify where a model lacks reliable internal knowledge.

**Use scored counterexamples as promotion candidates.** Useful for future commonplace evaluation work. High-hallucination or high-uncertainty responses could become review prompts, tests, warnings, or note-revision candidates before they ever justify model training.

**Keep thresholds explicit.** Ready now. `unknown_threshold`, `question_filtering_threshold`, scoring method, beta, and mode flags make the curation policy visible in scripts and configs, even though the generated artifacts need stronger provenance.

**Do not borrow weight-level promotion for ordinary KB memory.** Training a checkpoint is too opaque and expensive for most knowledge-base updates. Commonplace should prefer symbolic promotion paths unless repeated, well-evaluated failures justify a learned component.

## Trace-derived learning placement

**Trace source.** Self-Training-LLM qualifies as trace-derived learning. The qualifying traces are not agent session logs; they are offline generation rollouts: document-grounded questions, context-grounded reference answers, sampled no-context model answers, optional sampled gold answers, generated test responses, and pairwise evaluation comparisons. The trigger boundary is a batch data-generation or evaluation run launched by the shell scripts and Python entrypoints.

**Extraction.** Extraction is a pipeline of generators and judges. OpenAI models generate questions and some answers from Wikipedia documents; the target/base model generates greedy and sampled answers; NLI classifiers, self-reflection prompts, semantic clustering, and GPT-4o pairwise judging convert answer traces into hallucination, confidence, entropy, win/tie/loss, and chosen/rejected signals ([uncertainty/wiki_generation.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py), [uncertainty/pairwise_eval.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)). The oracle is mixed: source documents, OpenAI generators, NLI models, threshold code, and DPO selection logic.

**Storage substrate.** Raw and intermediate retained state lives in local files: question/test JSONL, answer pickle files, context-answer JSONL, response JSONL, result text files, embedding/topic caches, YAML configs, and model checkpoints. There is no persistent service substrate. The strongest distilled state lives under configured checkpoint paths such as `model_checkpoints/SFT/...` and `model_checkpoints/DPO/...` ([configs/model/tinyllama.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/model/tinyllama.yaml)).

**Representational form.** Wikipedia documents, questions, answers, and evaluation prompts are prose. Dataset fields, JSONL/pickle rows, YAML configs, thresholds, score keys, and train/eval scripts are symbolic. NLI classifiers, generated model probabilities, PEFT adapters, and saved checkpoints are distributed-parametric. The operative path is mixed: prose traces become symbolic rows and scores, then become distributed-parametric model behavior after SFT or DPO.

**Lineage.** Lineage is present at row granularity but weak for governance. Generated rows carry topic, category, instruction, document, answer, score, and sometimes pre/post response fields; the configured file names distinguish SFT/DPO, model, answer generator, threshold, beta, and known/test modes. The code does not add prompt versions, source document revision IDs, OpenAI model/run IDs for every row, scorer model versions inside artifacts, extraction timestamps, review decisions, or invalidation rules. Once compiled into weights, the lineage from a future answer back to a particular source trace is not inspectable.

**Behavioral authority.** Wikipedia documents, generated questions, sampled answers, and score files are knowledge artifacts while they serve as evidence or training candidates. The DPO/SFT dataset rows, YAML configs, filtering thresholds, and training scripts are system-definition artifacts with configuration and learning authority. The saved checkpoint or merged adapter is a distributed-parametric system-definition artifact: it directly shapes future model outputs without a retrieval step.

**Scope.** The implemented scope is benchmark/domain self-training around Wikipedia-derived factual QA, with categories and predefined titles. The README notes that other unstructured knowledge sources could work if entries contain `document`, but the inspected code and configs are Wikipedia-centered ([README.md](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/README.md), [uncertainty/data_utils.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/data_utils.py)).

**Timing.** The loop is offline and staged: generate corpus artifacts, score answer samples, train SFT, train DPO, then evaluate. TGI is used as a fast inference server during generation or testing, but the final system is a trained checkpoint, not an online memory that updates during deployment.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Self-Training-LLM belongs on the rollout-to-dataset-to-weights axis. It strengthens the survey's distinction between raw traces and distilled behavior-shaping artifacts: the raw traces are generated QA samples, the intermediate distillation is scored SFT/DPO data, and the final retained behavior is distributed-parametric model state. It also marks a boundary case for agent-memory reviews: trace-derived learning can be real even when the system is not a deploy-time agent memory.

## Curiosity Pass

The interesting mechanism is not that the project generates synthetic QA data. It is the way it uses disagreement and hallucination estimates to choose where to train: the model's no-context sampled answers expose weak internal knowledge, while document-grounded answers provide candidate corrections.

The simplest version would stop at a filtered SFT corpus. The DPO path adds a stronger authority step by turning uncertainty estimates into preference pairs. That makes the training signal sharper, but it also increases dependence on the scoring oracle and threshold choices.

The implementation is experiment-oriented rather than platform-oriented. Generated files are named and reused, but they are not packaged as auditable datasets with stable lineage metadata. That is acceptable for a research codebase; it would be insufficient for a knowledge base that must explain why a retained claim or behavior is trusted.

## Takeaways

**Trace-derived does apply, but the trace is model rollout data.** The system learns from generated answers, sampled alternatives, uncertainty scores, and preference pairs, not from agent task histories or user memories.

**The retained-artifact stack is source corpus, generated QA, scored answers, training rows, and checkpoints.** Treating all of these as "memory" would hide the important authority changes along the path.

**The final memory-like artifact is distributed-parametric.** After training, behavior is stored in weights or merged adapters, so activation is automatic during generation and auditability is much weaker than file-backed KB artifacts.

**This is not deploy-time agent memory.** There is no retrieval API, per-agent memory store, prompt assembly layer, lifecycle policy, or runtime source display. The learning happens before deployment.

**The design is a useful warning about promotion cost.** Moving from evidence to notes or tests keeps lineage inspectable; moving from evidence to weights can improve behavior but makes invalidation, attribution, and review much harder.

## Open Questions

- Should generated JSONL and pickle artifacts record prompt versions, source dataset revision, generator model, scorer model, threshold settings, and run IDs per row?
- How sensitive are DPO gains to the selected uncertainty scorer, `unknown_threshold`, beta, and question-filtering threshold?
- Can the pipeline identify and remove source-document errors, ambiguous questions, or OpenAI-generated reference mistakes before they become training signal?
- Would claim-level provenance or counterexample tests preserve enough lineage after training to make the resulting behavior auditable?
- Does the DPO checkpoint generalize beyond the predefined Wikipedia categories, or mainly improve the generated benchmark distribution?
- Should high-uncertainty examples be retained as explicit eval/regression tests in addition to being compiled into weights?

## What to Watch

- Whether the repository adds dataset cards, artifact manifests, or per-row lineage metadata for generated corpora and scored samples.
- Whether scoring/evaluation moves beyond NLI and GPT-4o judging into reproducible regression suites.
- Whether future versions support non-Wikipedia document sources with the same curation and validation discipline.
- Whether generated counterexamples become explicit tests, not only training data.
- Whether trained checkpoints are published with enough data provenance to inspect what behavior was learned.

## Bottom Line

Self-Training-LLM is a trace-derived self-training system, not a runtime agent-memory system. It turns Wikipedia documents and model answer rollouts into scored SFT/DPO data, then compiles that signal into checkpoints or merged weights. Commonplace should borrow the evidence-to-counterexample-to-training-candidate lens, but keep ordinary KB memory in inspectable symbolic artifacts unless a learned component has enough provenance, evaluation, and rollback discipline to justify the loss of auditability.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Self-Training-LLM is rollout-to-dataset-to-weights trace-derived learning rather than deploy-time memory retrieval.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: generated QA rows, scored samples, training configs, and checkpoints require separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: Wikipedia documents, generated questions, sampled answers, and score files serve as evidence before training consumes them.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: training rows, thresholds, configs, scripts, and checkpoints configure or directly shape model behavior.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - clarifies: the behavior-changing retained state is not the file label "memory" but the generated corpus, preference data, and learned weights consumed by later loops.
