---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Self-Training-LLM workflow: operator-mediated Wikipedia preference-data generation, DPO checkpoint delivery and pairwise evaluation at the frozen revision."
run-id: AAS-2026-10-15-self-training-llm-5b5ee621bde2-01
reviewed-boundary: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
---

# Self-Training-LLM workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is a Wikipedia DPO experiment: produce scored preference candidates using an SFT model, train a DPO checkpoint, generate held-out answers, and compare them with SFT answers. It is selected because the shipped launchers and path configuration connect these stages, exposing both change admission and a later consumer. It is a staged builder workflow, not a task assigned to a supervising conversational agent. The operator supplies the launch decisions, model service, credentials and compatible files; Python owns stage-local sequencing. Models supply content or judgments, not instructions for which stage to launch next (SRC-1, `script/wiki_ques_gen.sh`, `script/train.sh`, `script/testing.sh`, `script/tgi.sh`, `configs/model/tinyllama.yaml`; [RT-RTE-data-generation](runtime.md#rt-rte-data-generation), [RT-RTE-model-training](runtime.md#rt-rte-model-training)).

This is an implementation trace at the frozen commit, not a reconstructed successful run. No generated dataset, weights, service transcript or evaluation output was supplied. The default generation wrapper has the scorer-name and fresh-test obstacles documented in [RT-RTE-data-generation](runtime.md#rt-rte-data-generation). Consequently, the stages below describe the wired route conditional on usable prerequisites and invocation settings, not a claim that the wrappers work unchanged from a fresh checkout (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/scorer.py`).

### 1. Operator request becomes scored candidates

The operator requests a bounded generation job through configuration and flags. DPO generation requires an existing SFT question artifact. The generation route selects Wikipedia documents/topics, obtains document-answerable questions and reference answers, samples answers without documents, and applies NLI scoring. Context is supplied separately to each call; models do not inherit an entire preceding worker conversation. The question/reference/sampling distinctions and model identities are established in [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) and [RT-CMP-question-model](runtime.md#rt-cmp-question-model) (SRC-1, `uncertainty/wiki_generation.py`).

The handoff to training is a file, not a delegated agent return. For self-generated data with reference-as-chosen and multiple samples, the producer stores reference-sample consistency under `question_hallucination`; it then scores raw answer samples and persists the resulting records. Local threaded calls return candidate content to the producer, which filters failed results. Existing answer files are loaded instead of regenerating their contents, then scored again. This makes file reuse a partial recovery path, not a check that the file matches the current model or settings (SRC-1, `uncertainty/wiki_generation.py`; [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)).

> all_scored_instances = get_scored_ds(ans_dict,'raw_answer_sample')
> with open(answer_path,'wb') as f:
>     pickle.dump(all_scored_instances,f)
> --- `uncertainty/wiki_generation.py`

The generated reference is an optimization target, not an independently certified answer. NLI scores decide consistency-based eligibility; they do not verify the source document or establish factual correctness. This distinction remains material at every later handoff (SRC-1, `uncertainty/scorer.py`; [RT-RTE-model-training](runtime.md#rt-rte-model-training)).

### 2. Training admits examples, then saves a checkpoint

The operator launches training separately. In the selected DPO branch, `train.py` chooses the configured SFT model as its starting model and reloads the scored pickle. With question filtering and reference-as-chosen enabled, it first selects low `question_hallucination` records; with a positive unknown threshold it then selects high answer-hallucination records. The shipped training wrapper sets an unknown threshold of 0.8 and reference-as-chosen. Thresholds and model paths are operator choices; per-record eligibility is a software decision without per-record human approval (SRC-1, `script/train.sh`, `uncertainty/train.py`; [RT-RTE-model-training](runtime.md#rt-rte-model-training)).

`NLIScorer.get_dpo_sample` rejects records whose sample/score lengths disagree or whose raw samples are all empty. In the single-preference SelfCheckGPT branch, it selects the most contradictory raw sample as rejected; reference-as-chosen overrides the chosen answer with `gold_answer`. Training removes `None` results. Thus rejection can discard a candidate before optimization, but an admitted pair is not a proof that the preferred answer is true (SRC-1, `uncertainty/scorer.py`, `uncertainty/train.py`; [RT-RTE-model-training](runtime.md#rt-rte-model-training)).

The trainer receives less than the selector. Although the single-preference output retains document metadata, `list_to_hf_ds` constructs only formatted instruction prompts and chosen/rejected answer columns. Topic, category, document and score fields do not become additional DPO input columns. The returned schema is explicit:

> return HFDataset.from_dict({
>     'prompt': prompt,
>     'chosen': chosen,
>     'rejected': rejected,
> })
> --- `uncertainty/self_learning_training.py`

The prompt formatter is called on the instruction alone. The chosen answer receives EOS; the rejected answer receives EOS with a random 50% choice. These transformations, not the full source candidate record, define the external trainer's supplied input. The trainer handles optimization and internal training/validation machinery; this repository calls `trainer.train()` and saves the resulting model. Saving is not conditional on winning the later pairwise comparison (SRC-1, `uncertainty/self_learning_training.py`; [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model), [RT-RTE-model-training](runtime.md#rt-rte-model-training)).

The delivered training product is therefore a checkpoint at a derived path, not an approved deployment. Intermediate save configuration offers retention, but this route does not automatically restore the SFT model after an unfavorable external judgment. The operator owns whether to consume a saved checkpoint (SRC-1, `uncertainty/train.py`, `uncertainty/self_learning_training.py`; [RT-RTE-model-training](runtime.md#rt-rte-model-training)).

### 3. A separate inference invocation consumes a selected model

The next handoff requires another operator decision. Direct inference loads the configured, flag-derived DPO checkpoint path. TGI inference instead calls a localhost endpoint whose weights are selected by the separately launched server. The tokenizer still follows the configured model path. The shipped TGI launcher defaults to base TinyLlama, so a DPO-labeled response file alone does not prove DPO checkpoint consumption. The operator must align server weights, tokenizer and output settings; the client does not enforce this identity contract (SRC-1, `uncertainty/generate_response.py`, `script/tgi.sh`; [RT-RTE-response-generation](runtime.md#rt-rte-response-generation), [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption)).

For ordinary held-out DPO evaluation, the driver reads `data/wiki/test.jsonl`, supplies formatted questions without source documents, batches greedy generation, and writes instruction/response JSONL. The sampled-response branch is disabled. The document is supplied later to the judge, not to the ordinary DPO answer generator. Completing this file write delivers answers for evaluation, not a verified accuracy result (SRC-1, `uncertainty/generate_response.py`; [RT-RTE-response-generation](runtime.md#rt-rte-response-generation)).

### 4. Evaluation delivers a comparison, not a successor decision

`pairwise_eval.py` requires baseline responses, the evaluated response file, test documents and credentials. It joins by instruction and passes question, document, baseline answer and new answer to GPT-4o through `LLMJudge`. The source document is the requested truthfulness reference, but no independent expected A/B choice is supplied. The judge sees neither checkpoint bytes nor training history. It returns a ranking proposal, and parser/order logic determines whether to count it (SRC-1, `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py`; [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)).

Each uncached comparison is requested in both answer orders. Valid choices favoring the evaluated response in both orders yield win; choices favoring baseline yield lose; order disagreement yields tie. The cache can bypass new provider calls. The evaluator prints and appends aggregate win/tie/lose proportions, cost, no-count and length information to the configured result file. This appended report is the terminal product of the selected experiment. There is no result-to-trainer launch or automatic checkpoint promotion on this traced route (SRC-1, `uncertainty/scorer.py`, `uncertainty/pairwise_eval.py`; [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)).

### Failure and recovery boundaries

The judge has a concrete failure path. It tries each response order at most three times, sleeps after provider exceptions, and retries unparseable replies. Without two valid choices it returns `None`. Evaluation then omits these failed comparisons, caches successful labels and returns a no-count total (SRC-1, `uncertainty/scorer.py`; [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)).

> len_no_counts = [1 if r is None else 0 for r in remaining_results]
> non_empty_idx = [i for i,r in enumerate(remaining_results) if r is not None]
> remaining_results = [remaining_results[i] for i in non_empty_idx]
> --- `uncertainty/scorer.py`

Consequently, the proportions use only counted results, not all requested comparisons. With zero counted results, the divisions have no guard and the aggregate write is not reached normally. There is no whole-workflow retry: code owns these bounded request retries; the operator must rerun or repair the stage when necessary. Successful cached judgments can be reused, but that does not recover a missing checkpoint or repair mismatched response paths (SRC-1, `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py`).

> total_counted = len(results)
>
> tie_score = tie_count/total_counted
> win_score = win_count/total_counted
> lose_score = lose_count/total_counted
> --- `uncertainty/pairwise_eval.py`

The testing wrapper additionally expands `answer_generator` and `beta` without locally assigning them. It is not self-contained evidence of consistent experiment settings. Together with the fresh-generation obstacles and independent server selection, this prevents an unconditional end-to-end delivery guarantee. No supplied run establishes that a checkpoint was produced, used, or improved answers; source-wired handoffs and bounded rejection mechanisms are the supported result (SRC-1, `script/testing.sh`; [RT-RTE-data-generation](runtime.md#rt-rte-data-generation), [RT-RTE-response-generation](runtime.md#rt-rte-response-generation)).

### Inspection coverage

This member independently inspected all of `uncertainty/train.py`, `uncertainty/self_learning_training.py`, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`, all four shell launchers and `configs/model/tinyllama.yaml`; it also inspected `NLIScorer.get_dpo_sample`, `LLMJudge` and the answer-generation/persistence segment of `uncertainty/wiki_generation.py`. These extend the boundary's initial inspected scope under SRC-1 and supply implementation evidence only. Earlier question/document construction is supported through the supplied runtime records rather than a claim of independent full helper inspection. Provider behavior, trainer internals and successful execution remain outside what this trace establishes.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-model-training](runtime.md#rt-rte-model-training)

Workflow handoff: candidate selection returns richer records than optimization receives. The account's checked schema passage shows the conversion to prompt/chosen/rejected columns, including instruction-only prompt construction. The checkpoint completes the training stage; it does not certify evaluation success. Rejection precedes optimization, whereas later checkpoint consumption remains operator-mediated (SRC-1, `uncertainty/scorer.py`, `uncertainty/self_learning_training.py`).

#### On [RT-RTE-response-generation](runtime.md#rt-rte-response-generation)

Workflow delivery condition: response-file completion is separable from checkpoint identity. A matching TGI endpoint is an external operator-maintained precondition even when output filenames name DPO. The next consumer receives question/response records, not evidence of which server weights answered (SRC-1, `uncertainty/generate_response.py`, `script/tgi.sh`).

#### On [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)

Workflow recovery and terminal condition: retry exhaustion omits a comparison rather than rejecting the checkpoint. Successful comparisons survive through the judge cache; aggregate reporting requires nonzero counted results. The appended comparison report ends this selected workflow without making the evaluator a trainer supervisor or deployment authority (SRC-1, `uncertainty/scorer.py`, `uncertainty/pairwise_eval.py`).
