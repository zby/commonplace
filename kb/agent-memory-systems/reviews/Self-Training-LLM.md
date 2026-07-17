---
description: "Self-Training-LLM review: offline synthetic Wikipedia QA generation, uncertainty-filtered SFT/DPO datasets, and model-weight learning rather than contextual memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# Self-Training-LLM

Self-Training-LLM, by wj210, is an offline self-training pipeline for improving factual QA behavior on Wikipedia-derived questions. At the reviewed commit it generates synthetic questions from Wikipedia articles, produces reference and sampled model answers, scores uncertainty or hallucination with NLI/self-check methods, trains SFT and DPO models, and evaluates the resulting model against a baseline; it is not an agent runtime with an external retrieval memory store.

**Repository:** https://github.com/wj210/Self-Training-LLM

**Reviewed commit:** [97839b29d0fd8bb474f5549fa3e9d6ca504732e0](https://github.com/wj210/Self-Training-LLM/commit/97839b29d0fd8bb474f5549fa3e9d6ca504732e0)

**Source directory:** `related-systems/wj210--Self-Training-LLM`

## Core Ideas

**The durable memory is parametric, not a retrievable note store.** The workflow writes generated QA data under `data/wiki/`, trains SFT and DPO checkpoints under configured `model_checkpoints/` paths, and saves trained models with TRL trainers ([README.md](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/README.md), [configs/model/tinyllama.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/model/tinyllama.yaml), [uncertainty/self_learning_training.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/self_learning_training.py)). Later behavior changes because the model weights change, not because an agent retrieves stored episodes.

**The write path is synthetic data generation plus filtering.** `wiki_generation.py` selects and chunks Wikipedia documents, asks GPT models to generate questions, generates gold/context answers, samples raw model answers, and stores scored answer dictionaries for later training ([uncertainty/wiki_generation.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [uncertainty/topic_generator.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/topic_generator.py), [uncertainty/templates.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/templates.py)).

**Uncertainty scores decide what becomes training signal.** `NLIScorer` supports SelfCheckGPT, BSDetector, and semantic-consistency-style scoring; `return_question_type` splits known and unknown samples by score thresholds; `get_dpo_sample` chooses preferred and rejected answers from sampled responses, optionally forcing the reference answer as chosen ([uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py), [uncertainty/utils.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/utils.py), [uncertainty/train.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py)).

**Context efficiency is learned away rather than served at inference.** During data generation and RAG-mode evaluation, the system formats a document into the prompt; outside those modes, inference uses the fine-tuned model without a retrieval layer, top-k memory selection, progressive disclosure, or a context budget manager ([uncertainty/templates.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/templates.py), [uncertainty/generate_response.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/generate_response.py)). This avoids future context volume at the cost of turning source-grounded corrections into opaque weights.

**Evaluation is pairwise model comparison, not memory faithfulness.** The test script first generates responses, then `pairwise_eval.py` compares post-training responses against baseline responses with a GPT-4o judge and writes aggregate win/tie/lose and length metrics ([script/testing.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/testing.sh), [uncertainty/pairwise_eval.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)). This can test model improvement on the benchmark path, but it does not expose which training examples are causally used by a later answer.

## Artifact analysis

- **Storage substrate:** `files` `model-weights` — Generated questions, answers, scores, known/unknown splits, responses, cached judge outputs, configs, and metrics are local files; the final behavior-shaping artifact is a saved SFT or DPO model checkpoint.
- **Representational form:** `prose` `symbolic` `parametric` — Wikipedia documents, prompts, questions, and answers are prose; JSONL/pickle/YAML records, score fields, thresholds, trainer configs, and shell scripts are symbolic; learned model parameters and LoRA/full checkpoints are parametric.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompts, configs, scripts, and example templates are authored; Wikipedia documents and optional external datasets are imported; sampled answer rollouts, NLI/self-check scores, question-quality scores, preference pairs, judge caches, and trained weights are extracted or learned from generated traces.
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — Source documents and generated QA records provide knowledge; prompt templates and training configs instruct generation/training; scoring thresholds and pairwise evaluation validate or filter candidates; hallucination/confidence scores rank known versus unknown samples and preferred versus rejected answers; SFT/DPO training gives the distilled traces learning authority over future model behavior.

**Synthetic QA records.** `data/wiki/questions.jsonl`, answer pickles, `context_answer.jsonl`, and generated test sets are intermediate retained artifacts. Their prose fields carry the knowledge source and task framing, while their symbolic fields (`topic`, `category`, `document`, `gold_answer`, `raw_answer_sample`, score fields) drive filtering and trainer construction.

**Uncertainty and preference records.** The operative split is the raw answer rollout plus its scoring metadata. SelfCheckGPT/BSDetector/semantic-consistency scores decide whether a question is known or unknown and which sampled answer becomes chosen or rejected for DPO; the record is therefore more than evidence, because it becomes a training selector ([uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py), [uncertainty/utils.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/utils.py)).

**Training checkpoints.** SFT and DPO checkpoints are the strongest retained artifacts. `do_train` builds TRL datasets, trains `SFTTrainer` or `DPOTrainer`, saves the model, and merges PEFT adapters when used ([uncertainty/self_learning_training.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/self_learning_training.py)). The promotion path is trace record to selected dataset row to parametric checkpoint; after promotion, the source evidence is no longer inspectable at inference time.

**Evaluation records.** Response JSONL files and pairwise test results validate benchmark improvement, but they do not govern a live memory store. Their authority is experimental evidence about the trained model, not runtime retrieval or enforcement.

## Comparison with Our System

Self-Training-LLM sits almost opposite Commonplace on the memory design spectrum. Commonplace keeps behavior-shaping knowledge in inspectable Markdown, schemas, indexes, and review gates; Self-Training-LLM compiles selected source-grounded QA traces into model weights. That makes its future context cheap because no note or retrieved passage needs to be loaded, but it also removes the main Commonplace affordances: source review, diffable claims, replacement history, and targeted invalidation.

The closest alignment is the promotion question. Commonplace asks when a source observation should become a durable note, instruction, validator, or index entry. Self-Training-LLM asks when a generated answer trace should become a supervised example or a DPO preference pair. Both systems need a gate between raw material and behavior-shaping artifact; the difference is that Commonplace keeps the promoted artifact symbolic/prose, while this repo promotes into parametric state.

The biggest tradeoff is auditability. The code keeps intermediate files and evaluation outputs, so the training run can be inspected after the fact if artifacts are retained. At runtime, however, the trained model has no read-back path to a cited source document or preference pair. Commonplace should treat this as evidence for offline learning workflows, not as a substitute for governed knowledge artifacts.

### Borrowable Ideas

**Uncertainty-first candidate selection.** Commonplace could use disagreement, self-check, or contradiction scores to prioritize source claims for review before promotion. Ready as a review-prioritization experiment; not ready as automatic note acceptance.

**Known/unknown split as a maintenance queue.** The `return_question_type` pattern maps cleanly to KB upkeep: high-confidence items can pass through lighter checks, while uncertain or contradictory items become review work. Ready where deterministic or review-bundle scores already exist.

**Preference-pair construction from alternatives.** For writing workflows, generated revisions could be compared as chosen/rejected examples for future style or review training. Needs a concrete use case and strong provenance controls before it should affect system behavior.

**Keep parametric learning downstream of symbolic evidence.** If Commonplace ever trains a ranker or assistant adapter, the source artifacts and selection records should remain canonical and reviewable. Ready as a design constraint.

## Write side

**Write agency:** `automatic` — The operator launches scripts manually, but the store-changing mechanism is automatic: topic/document selection, question generation, answer rollout generation, scoring, filtering, dataset construction, model training, response generation, judge caching, and metric writing.

**Curation operations:** `promote` — The system promotes selected generated traces into stronger behavior-shaping artifacts: questions and answers become SFT rows, unknown/hallucinated sampled answers become DPO preference pairs, and those datasets become model checkpoints. I did not find implemented consolidation, deduplication, stale invalidation, decay, or synthesis across already stored memory; acquisition and training dominate the write side.

### Trace-learning

**Trace source:** `trajectories` — The qualifying traces are generated answer rollouts: greedy answers, sampled answers with generation details, sampled gold answers for question filtering, and baseline/post-training response pairs.

**Extraction.** The extraction oracle is a mix of GPT-generated reference/context answers, NLI/self-check scores, score thresholds, and optional GPT-4o pairwise judging. The curation policy selects known questions for SFT or question filtering, selects unknown/high-hallucination samples for DPO, and converts answer alternatives into chosen/rejected pairs ([uncertainty/wiki_generation.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [uncertainty/train.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py), [uncertainty/pairwise_eval.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)).

**Learning scope:** `cross-task` — The learned checkpoint is meant to improve model behavior across future questions in the same broad factual-QA domain, not only within one task instance.

**Learning timing:** `offline` — The scripts generate data, train, then evaluate in batches. I did not find an online loop that updates a deployed model during interaction.

**Distilled form:** `parametric` — The final distilled artifact is model weights, optionally reached through LoRA/PEFT and merged back into the saved checkpoint.

This strengthens the trace-learning survey's parametric-learning corner: the source trace is not an agent tool log, but sampled model behavior plus scoring traces. It also shows the auditability cost when trace-derived lessons are compiled into weights rather than retained as reviewable rules or notes.

## Read-back

**Read-back:** `pull` — The retained learning affects future answers only when a caller explicitly loads or serves the trained model and calls generation/evaluation scripts. There is no implemented external memory store, provider hook, session-start memory injection, MCP server, or retrieval API that pushes retained artifacts into an agent context.

The system can run a RAG-style evaluation mode that includes the source document in the prompt, but that is a test/generation mode over dataset rows, not a persistent read-back path from a memory system. The normal post-training path relies on parametric recall from the checkpoint. Effective use of particular training traces is not directly testable from the runtime call; pairwise evaluation measures aggregate answer quality against a baseline rather than faithfulness to a retrieved memory.

## Curiosity Pass

**"Self-training memory" is implicit memory.** The system remembers by changing weights, so it is relevant to agent-memory surveys even though it lacks a classic memory store. That makes it a useful boundary case for the retained-artifact vocabulary.

**The most reviewable part is before the final artifact.** Questions, documents, sampled answers, scores, and preference pairs are inspectable while they remain files. Once training completes, the behavior-shaping artifact is much harder to audit or selectively repair.

**The README's "knowledge filtering" is not knowledge-base governance.** It filters training candidates by uncertainty/hallucination scores; it does not create source-linked claims, contradiction records, invalidation state, or reviewed knowledge entries.

**Context efficiency comes with source-loss risk.** Avoiding retrieval-time context can reduce token pressure, but factual answers no longer carry the document context unless the caller uses RAG mode or preserves an external citation path.

## What to Watch

- Whether future versions keep stronger provenance from trained checkpoints back to exact generated examples; that would determine whether parametric learning can be audited after a model change.
- Whether the pipeline becomes iterative beyond the `--iter` answer-path suffix; a true multi-cycle loop would make curation and invalidation behavior more important.
- Whether evaluation adds trace-level ablations showing which selected examples drive gains; that would make the learning authority less opaque for Commonplace-style governance.
- Whether the approach expands beyond Wikipedia documents as the README suggests; that would test whether the topic/document acquisition path is domain-general or Wikipedia-specific.

Relevant Notes:

- [Retained artifact](../../notes/definitions/retained-artifact.md) - classifies trained checkpoints and generated datasets as retained state with future behavioral consequence.
- [Representational form](../../notes/definitions/representational-form.md) - supports separating prose/source records, symbolic scores/configs, and parametric model weights.
- [Lineage](../../notes/definitions/lineage.md) - frames the imported Wikipedia source, generated rollouts, selected preference records, and trained checkpoint lineage.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - positions sampled answer rollouts and scoring traces as trace-learning inputs.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - explains why this system remains pull-only despite durable checkpoints and datasets.
