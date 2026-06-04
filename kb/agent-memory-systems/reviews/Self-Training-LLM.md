---
description: "Review of Self-Training-LLM: offline Wikipedia QA self-training that promotes generated answer traces into SFT/DPO checkpoints"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# Self-Training-LLM

Self-Training-LLM, from `wj210/Self-Training-LLM`, is a research codebase for factual-QA post-training rather than a runtime agent memory service. It builds Wikipedia-derived question/answer corpora, scores sampled model answers for uncertainty or hallucination, converts selected traces into SFT or DPO datasets, and trains new model checkpoints that carry the learned behavior in weights.

**Repository:** https://github.com/wj210/Self-Training-LLM

**Reviewed commit:** [97839b29d0fd8bb474f5549fa3e9d6ca504732e0](https://github.com/wj210/Self-Training-LLM/commit/97839b29d0fd8bb474f5549fa3e9d6ca504732e0)

**Last checked:** 2026-06-02

## Core Ideas

**The memory target is the checkpoint, not a retrieved store.** The pipeline writes SFT and DPO checkpoints under model-specific paths such as `model_checkpoints/SFT/tinyllama_{answer_generator}` and `model_checkpoints/DPO/tinyllama_{answer_generator}`; evaluation then loads the selected checkpoint by `mode` and generates answers directly ([tinyllama config](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/model/tinyllama.yaml), [training entrypoint](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py), [response generation](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/generate_response.py)). That makes it a distributed-parametric memory system: later behavior changes because the model itself has changed.

**Wikipedia documents are converted into self-training traces.** `wiki_generation.py` loads or creates accepted Wikipedia documents, selects predefined topic categories, asks GPT models to create held-out and training questions, generates context-grounded and no-context answers, samples multiple raw answers, scores them, and saves question JSONL plus answer pickles ([wiki generation](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [topic generator](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/topic_generator.py), [wiki config](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/data/wiki.yaml)). The repository is explicit that `script/wiki_ques_gen.sh` generates SFT and DPO data and performs knowledge filtering ([README](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/README.md), [generation script](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/wiki_ques_gen.sh)).

**Uncertainty scoring is the selection policy.** `NLIScorer` implements SelfCheckGPT-style contradiction scoring, BSDetector-style entailment plus optional self-reflection, and semantic-consistency clustering. `return_question_type` classifies scored rows as known or unknown by scoring method and threshold, and DPO training filters to unknown samples before creating preference pairs ([scorer](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py), [utils](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/utils.py), [training entrypoint](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py)).

**DPO preferences are synthesized from answer traces.** For each scored question, `get_dpo_sample` chooses preferred and rejected answers from generated samples using contradiction, confidence, or semantic-cluster evidence; with `ref_as_chosen`, the context answer is forced as chosen, while high-hallucination raw samples become rejected candidates ([scorer](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py)). `self_learning_training.py` then converts those records into TRL `DPOTrainer` or `SFTTrainer` datasets and saves the trained model ([self-learning training](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/self_learning_training.py)).

**Context efficiency is mostly a training-time concern.** At inference, the learned material costs no prompt tokens because it is in the checkpoint. During data generation and testing, the system bounds context with fixed Wikipedia chunks, maximum prompt/response token settings, DPO max lengths, and optional RAG mode that inserts the document directly into the answer prompt ([data utils](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/data_utils.py), [training config](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/training/dpo_trainer.yaml), [response generation](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/generate_response.py)). It does not maintain a searchable external memory with progressive disclosure, source citations at read time, or per-query memory activation.

**Evaluation compares checkpoints, not memories.** The test script first generates responses for a selected mode, then `pairwise_eval.py` compares the post-training response against a baseline response with a GPT-4o judge and appends aggregate win/tie/lose metrics ([testing script](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/testing.sh), [pairwise eval](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)).

## Artifact analysis

- **Storage substrate:** `model-weights` — Local `data/wiki/` JSONL and pickle files, plus intermediate `data/embeddings/accepted_topic_doc.pkl` and topic split pickles
- **Representational form:** `prose` `symbolic` `parametric` — readable/generated corpora, symbolic JSON/pickle/policy records, and trained model weights
- **Lineage:** `authored` `imported` `trace-extracted` — authored scorer/prompt/training code imports Wikimedia data and extracts generated QA traces into training rows and checkpoints
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `validation` `ranking` `learning` — source/traces act as evidence; prompts instruct generation; filters and thresholds gate, validate, and rank examples; trainers promote selected traces into learned weights

**Wikipedia source documents and generated questions.** Storage substrate: local `data/wiki/` JSONL and pickle files, plus intermediate `data/embeddings/accepted_topic_doc.pkl` and topic split pickles. Representational form: prose documents and questions wrapped in symbolic JSON/Python objects. Lineage: imported from the Hugging Face Wikimedia dataset, filtered by length and predefined topic categories, then chunked and transformed into questions. Behavioral authority: knowledge artifacts for corpus evidence during generation; system-definition artifacts only when the scripts use them to decide training/test splits and prompts.

**Generated answer and score pickles.** Storage substrate: `data/wiki/answer/*_sft_*.pkl`, `*_dpo_*.pkl`, `questions.jsonl`, `context_answer.jsonl`, and `data/wiki/test.jsonl` paths configured per model ([model configs](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/model/tinyllama.yaml)). Representational form: mixed symbolic records containing prompt fields, documents, generated answers, sampled answers, NLI/self-check scores, and category/topic metadata. Lineage: derived from Wikipedia documents, GPT question generation, model/TGI generations, and NLI or self-reflection scorers. Behavioral authority: knowledge artifacts while stored as traces; system-definition artifacts when `train.py` filters them into SFT or DPO training examples.

**Uncertainty scorer and filtering thresholds.** Storage substrate: Python scorer code and command-line thresholds such as `question_filtering_threshold`, `unknown_threshold`, `beta`, and `num_samples` in scripts and CLI args ([train script](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/train.sh), [training entrypoint](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py)). Representational form: symbolic Python policy plus numeric parameters. Lineage: authored repository state. Behavioral authority: system-definition artifact authority because it ranks questions, selects unknown examples, constructs chosen/rejected pairs, and controls what can affect model weights.

**Prompt templates and formatting functions.** Storage substrate: authored Python strings/functions in `templates.py` and formatting utilities in `utils.py`. Representational form: prose prompts plus symbolic chat-template formatting. Lineage: authored code. Behavioral authority: system-definition artifact authority over question generation, answer generation, self-reflection, SFT formatting, DPO prompt formatting, and optional document-grounded response prompts ([templates](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/templates.py), [utils](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/utils.py)).

**SFT/DPO checkpoints.** Storage substrate: Hugging Face/TRL output directories under `model_checkpoints/`, optionally full-parameter or PEFT-merged. Representational form: distributed-parametric model weights plus tokenizer/config side effects. Lineage: base model -> generated/scored training data -> SFT or DPO trainer -> saved model. Behavioral authority: system-definition artifact with direct behavioral force because the loaded checkpoint determines future answers; it is not inspectable as individual memories and must be probed or evaluated.

**Response and judge outputs.** Storage substrate: `responses/{mode}/...jsonl`, `test_results/{mode}/...txt`, and `llm_judge_cache/{engine}.pkl` created by evaluation code. Representational form: generated prose responses, symbolic JSONL rows, aggregate text metrics, and cached judge choices. Lineage: generated from baseline and post-training checkpoints plus GPT-4o pairwise judging. Behavioral authority: evaluation artifacts, not runtime memory. They can justify a training variant but do not feed back automatically unless a user reruns training with changed settings.

**Promotion path.** Self-Training-LLM promotes corpus-grounded generation traces into model weights: Wikipedia document -> generated question -> context/no-context answers and answer samples -> uncertainty scores -> SFT examples or DPO preference pairs -> trained checkpoint -> future answers. The path crosses from readable prose/symbolic traces into distributed-parametric state. It has measurable evaluation but weak item-level provenance after promotion: a checkpoint answer cannot be traced back to the specific question/score pair that caused it.

## Comparison with Our System

| Dimension | Self-Training-LLM | Commonplace |
|---|---|---|
| Primary purpose | Improve factual-QA model behavior through SFT/DPO self-training | Maintain an agent-operated methodology KB with typed, reviewable artifacts |
| Retained behavior surface | Model checkpoints | Markdown notes, instructions, reviews, sources, schemas, indexes, and review state |
| Learning input | Wikipedia documents, generated questions, sampled answers, uncertainty scores | Source snapshots, notes, review findings, validation output, agent/human edits |
| Promotion target | Distributed-parametric weights | Readable prose and symbolic artifacts, with validation and review gates |
| Read-back | Loaded checkpoint or explicit document-in-prompt mode | Mostly pull through search/indexes/links, with push only where instructions or generated context are deliberately loaded |
| Governance | Threshold filters, NLI scorers, trainer eval loss, GPT-4o pairwise evaluation | Frontmatter schemas, link checks, collection contracts, semantic review, git history |

Self-Training-LLM is useful to Commonplace mainly as the opposite design pole. It spends expensive training work to make future inference cheap: no prompt-time retrieval, no per-note context budget, and no agent-visible memory management. Commonplace keeps the learned surface readable and cheap to edit, but pays runtime search and context-assembly costs.

The strongest alignment is the trace-derived split. Both systems distinguish raw evidence from promoted behavior-shaping artifacts. In Self-Training-LLM, the raw layer is generated questions, sampled answers, scores, and result rows; the promoted layer is SFT/DPO weights. In Commonplace, the raw layer is source/work/review evidence, while the promoted layer is a typed note, instruction, schema, or index. The tradeoff is auditability: Commonplace can inspect a promoted artifact directly, while a checkpoint must be evaluated behaviorally.

**Read-back:** `push` — By checkpoint selection/always-load rather than retrieval. Targeting is `coarse`, signal n/a: once the caller loads an SFT or DPO checkpoint, the learned behavior is always active in generation. The `rag` mode inserts the current test document into the prompt, but that is evaluation-time document context rather than retained memory read-back. This commit does not implement relevance-gated memory/context injection, so `push-activation` is not warranted.

**Read-back signal:** `coarse` — loaded checkpoint behavior is always active once selected, without per-instance memory retrieval.

**Faithfulness tested:** `yes` — pairwise evaluation compares post-training checkpoint responses against baseline responses, though it does not preserve item-level attribution from a response back to the training trace.

### Borrowable Ideas

**Separate evidence generation from promotion policy.** Commonplace could mirror the pipeline shape for review experiments: generate candidate examples, score or classify them, then promote only the selected material. Ready now as a workshop pattern, not as automatic library mutation.

**Make uncertainty thresholds explicit knobs.** `unknown_threshold`, `question_filtering_threshold`, `beta`, and scoring method choices are crude but reviewable. Commonplace review automation should expose similar thresholds when deciding which findings deserve agent attention. Ready now where review bundles already produce structured findings.

**Keep the "unknown sample" concept.** The DPO path focuses on model-uncertain or high-hallucination questions. Commonplace could prioritize notes or procedures where agents disagree, validation is unstable, or review gates repeatedly fail. Needs a concrete signal source.

**Do not borrow opaque promotion for KB methodology.** Weight promotion is appropriate for model behavior experiments with benchmark oracles. For KB methodology, it would hide the exact rule or claim that changed agent behavior. Commonplace should prefer readable or symbolic promotion unless a benchmarked model-update use case exists.

**Use pairwise evaluation for artifact variants.** The baseline-vs-post-training comparison shape could transfer to generated instructions or review rewrites: compare old/new outputs on fixed tasks before adoption. Needs a benchmark set and a calibrated judge, otherwise it becomes another ungrounded LLM vote.

## Write-side placement

**Write agency:** `automatic` — generation, scoring, filtering, DPO/SFT conversion, and training scripts turn selected answer traces into saved checkpoints without manual authoring of each retained behavior.

**Curation operations:** `promote` — uncertainty scores, filters, preference construction, and trainer selection promote generated traces into SFT/DPO datasets and then into distributed-parametric checkpoint state.

### Trace-derived learning

**Trace source:** `trajectories` — generated QA examples, sampled answers, scored training rows, response JSONL, and pairwise judge outputs are the retained generation/evaluation trajectories.

**Learning scope:** `cross-task` — the trained checkpoint carries behavior across later factual-QA generations rather than one deployed session or project.

**Learning timing:** `offline` `staged` — the loop generates data, scores/filters, trains SFT or DPO, and then evaluates; it is not an online deployed-agent memory loop.

**Distilled form:** `parametric` — selected traces are ultimately promoted into SFT/DPO model weights.

**Trace source.** Self-Training-LLM qualifies as trace-derived learning. The qualifying traces are generated Wikipedia QA examples, context-grounded answers, raw sampled no-context answers, TGI/HF generation details and logprobs, NLI/self-check scores, SFT/DPO training rows, response JSONL, and pairwise judge outputs ([wiki generation](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [scorer](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py), [pairwise eval](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)).

**Extraction.** Extraction is partly LLM-mediated and partly deterministic. GPT models generate questions and context answers; the local model generates greedy and sampled responses; NLI/self-check/semantic-consistency code scores answer sets; filtering code selects known or unknown questions; DPO conversion code chooses preferred and rejected answers; TRL trainers convert those rows into a checkpoint.

**Four fields.** Raw traces persist as JSONL and pickle files in `data/wiki/`, response JSONL, result text, and judge caches. Their representational form is mixed prose plus symbolic fields and numeric scores. The distilled artifact is distributed-parametric model state under `model_checkpoints/`. Lineage is script-stage lineage rather than item-level provenance inside the final weights. Behavioral authority moves from knowledge-artifact traces to system-definition artifact weights with direct generation authority.

**Scope and timing.** Scope is offline, benchmark-like Wikipedia factual QA over model-specific configs. Timing is staged: generate data, score/filter, train SFT or DPO, then evaluate. There is no online loop where a deployed agent writes a memory item for immediate future retrieval.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Self-Training-LLM belongs in the trace-to-weights family. It strengthens the survey distinction between readable artifact promotion and distributed-parametric promotion: the pipeline's intermediate traces are inspectable, but the final behavior-shaping artifact is not.

## Curiosity Pass

**The system calls itself self-learning, but the loop is staged and offline.** The code does not run a deployed agent that notices failures and writes memories during work. It is closer to dataset curation plus post-training.

**The strongest "memory" is invisible after training.** Answer traces and scores are readable before promotion. Once promoted into weights, the retained behavior is cheap to use and hard to audit.

**RAG appears only as an evaluation mode.** `generate_response.py` can format the test question with its document in `rag` mode, but the central self-training mechanism does not implement a retrieval index or context memory service.

**The oracle stack is layered but brittle.** The pipeline uses documents, GPT-generated questions/answers, NLI scorers, self-reflection, thresholds, and GPT-4o pairwise judging. Each layer improves automation but can introduce bias or preserve dataset artifacts.

**The context-efficiency tradeoff is shifted into training cost.** Post-training removes prompt-time memory overhead, but it also removes per-query control over what memory is active.

## What to Watch

- Whether future commits preserve item-level provenance from checkpoint behavior back to the generated question, answer samples, scores, and training row. That is the main missing bridge from post-training memory to auditability.
- Whether evaluation adds ablations by trace type or threshold, not just checkpoint win/tie/lose. That would show which retained signals actually changed behavior.
- Whether the data-generation loop expands beyond predefined Wikipedia factual QA. Generalizing to less stable domains would stress the current oracle and filtering assumptions.
- Whether the project adds a retrieval or prompt-memory path alongside weights. That would change the read-back classification from checkpoint always-load to a hybrid memory architecture.
- Whether checkpoint selection gains governance metadata such as source dataset hash, scorer version, threshold settings, and judge model. Without it, comparing trained artifacts depends on external run discipline.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Self-Training-LLM promotes corpus-grounded generation traces into model checkpoints.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: generated traces, scorer policies, prompts, evaluation outputs, and model weights differ by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Self-Training-LLM avoids prompt-time activation by baking behavior into a selected checkpoint.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: sampled answer traces and uncertainty scores become training data for later behavior.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - contrasts: intermediate traces are preserved for training/evaluation, but later inference uses weights rather than reloading those traces.
- [Representational form](../../notes/definitions/representational-form.md) - distinguishes: the final memory form is distributed-parametric rather than prose or symbolic.
