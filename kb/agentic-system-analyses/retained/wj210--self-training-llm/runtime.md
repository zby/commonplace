---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Self-Training-LLM runtime baseline: operator-launched generation, SFT/DPO admission, checkpoint consumption and model judging at the frozen source revision."
run-id: AAS-2026-10-15-self-training-llm-5b5ee621bde2-01
reviewed-boundary: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
---

# Self-Training-LLM runtime report

## Runtime account

### Work and principals

Self-Training-LLM ships a staged model-building workflow, not a conversation agent that owns an ongoing task loop. A human operator launches data generation, training, model serving and evaluation separately. Python code owns each stage's next steps; language models propose questions and answers, an NLI classifier supplies scores, and another language model judges paired responses. Those model outputs do not select shell commands or rewrite the workflow's code. The consequential change-admission path is generated answers and scores → filtered training examples → trained parameters → a separately selected inference model. This is source wiring, not supplied evidence of an exercised improvement cycle (SRC-1, `README.md`, `script/wiki_ques_gen.sh`, `script/train.sh`, `script/tgi.sh`, `script/testing.sh`).

> - `train.sh` - SFT and DPO
> --- `README.md`

The ordinary source-native sequence is [RT-RTE-data-generation](#rt-rte-data-generation), [RT-RTE-model-training](#rt-rte-model-training), [RT-RTE-response-generation](#rt-rte-response-generation), then [RT-RTE-pairwise-evaluation](#rt-rte-pairwise-evaluation). These records locate decision roles, reference outcomes, admission and recovery. Model mutability is separated into [RT-CMP-causal-model](#rt-cmp-causal-model), [RT-CMP-nli-model](#rt-cmp-nli-model), [RT-CMP-question-model](#rt-cmp-question-model), [RT-CMP-test-question-model](#rt-cmp-test-question-model) and [RT-CMP-judge-model](#rt-cmp-judge-model).

### One ordinary invocation, including where it can stop

The shipped generation wrapper launches `uncertainty/wiki_generation.py` with TinyLlama configuration, ten samples, TGI on port 8082, and reference-as-chosen enabled. The operator must first provision credentials, models, GPU infrastructure and a matching TGI server. The program seeds random generators, reads YAML, exports the OpenAI key, selects SFT-versus-DPO artifact names, and creates an inference client and tokenizer. It loads or constructs a Wikipedia title/document cache and selects predefined train/test topics. It then constructs the NLI scorer and enters the question/answer producer (SRC-1, `script/wiki_ques_gen.sh`, `uncertainty/wiki_generation.py`, `uncertainty/topic_generator.py`).

This is not an assertion that the wrapper runs successfully. Its omitted scoring argument leaves the misspelled default `SelCheckGPT`, whereas the scorer dictionary supports `SelfCheckGPT`. Assuming earlier external setup succeeds, the dictionary lookup raises before the generation function. Correcting that invocation argument alone does not establish success: the wrapper also omits `--generate_sft`, so the DPO branch requires an existing SFT question file, and an absent/empty test file reaches an unchecked `test_ds[0]`. These source counterexamples are retained below rather than treating the README's stage sequence as an execution trace.

When its prerequisites and branch conditions hold, the producer chunks documents, asks OpenAI for document-answerable questions, requests reference and sampled answers, scores contradictions, and writes JSONL/pickle artifacts. Training is a new invocation that reloads those files; it does not receive a live return from generation. SFT trains from answer labels, while DPO selects questions and chosen/rejected answers by score rules. The trainer saves parameters. Evaluation again requires operator selection: the direct loader consumes a checkpoint path, but TGI consumes whatever model the separately launched endpoint actually serves. Response JSONL is joined to baseline responses and source documents for judging, whose cache and aggregate result text are terminal evaluation artifacts. The code does not feed the judge's win rate directly back into a trainer launch (SRC-1, `uncertainty/train.py`, `uncertainty/self_learning_training.py`, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py`).

### Forcing cases and guarantees

Four forcing cases bound the account:

1. **Fresh generation versus reused artifacts.** The scorer-key mismatch, required preexisting questions in DPO mode, and empty-test indexing invalidate an unconditional fresh-start claim. Existing files instead cause reload or skip behavior; existence is not validation of their provenance or current configuration ([RT-RTE-data-generation](#rt-rte-data-generation)).
2. **Threshold controls versus bypass.** In DPO training, a positive unknown threshold selects from the question-filtered dataset. At a nonpositive threshold, `unknown_ds = dataset` bypasses even that prior question-filtered subset. Thus enabling question filtering is not an invariant that every possible DPO invocation consumes only its output ([RT-RTE-model-training](#rt-rte-model-training)).
3. **Direct model versus TGI.** The direct route loads `model_path`; the TGI route supplies only a localhost URL. The launcher defaults to a base TinyLlama model even though evaluation may label its outputs DPO. Checkpoint identity is therefore an operator-maintained cross-process contract, not an enforced result-label guarantee ([RT-RTE-response-generation](#rt-rte-response-generation)).
4. **Successful judge replies versus partial failure/cache.** Judging requests both response orders, retries invalid/missing replies and omits samples without two valid choices. Cached results skip the provider. Reported proportions describe counted results, not necessarily all baseline questions, and do not gate checkpoint admission ([RT-RTE-pairwise-evaluation](#rt-rte-pairwise-evaluation)).

The selection guarantee's owner is training code, enforcement points are `return_question_type` and `get_dpo_sample`, and strength is **policy**: they enforce numerical selection where called, not factual correctness. Covered paths are the configured SFT/DPO branches; bypasses include unfiltered SFT, nonpositive unknown thresholds and alternative training datasets. The required external contract is the meaning/calibration of NLI outputs and the accuracy of reference answers. Implementation conclusion status: wired. Operation conclusion status: uninspected. Benefit conclusion status: uninspected (SRC-1, `uncertainty/train.py`, `uncertainty/utils.py`, `uncertainty/scorer.py`).

The reference-as-chosen guarantee's owner is `NLIScorer.get_dpo_sample`, its enforcement point is the explicit override plus the returned-pair constructors, and strength is **invariant** only for the single-preference pair and the first pair of a multiple-preference result when `ref_as_chosen` is enabled. Those chosen fields receive the extracted `gold_answer`. The later multiple-preference loop instead appends chosen answers from `gold_answer_sample`; these need not equal `gold_answer`. The training CLI exposes that alternate path through `--multiple_pref` and extends its dataset with the returned pairs. Thus the flag does not enforce a uniform reference target across all admitted pairs. The guarantee also does not cover invocation paths without the flag, SFT label acquisition, or factual validity of any reference. It requires correctly formed input records and successful completion of the selector. Implementation conclusion status: wired. Operation conclusion status: uninspected. Benefit conclusion status: uninspected (SRC-1, `uncertainty/scorer.py`, `uncertainty/train.py`; [RT-RTE-model-training](#rt-rte-model-training)).

> if self.ref_as_chosen: # force chosen ans as reference answer
>     chosen_ans = gold_answer
> --- `uncertainty/scorer.py`

### Context, effects and operational envelope

Working context is assembled per model call, not maintained as a long conversation. Question calls receive a document chunk and three sampled shipped examples; base-answer calls use up to ten examples. DPO answer calls omit examples, include the document for reference answers, and remove it for raw answers. Base evaluation adds five examples; RAG evaluation includes the test document; ordinary SFT/DPO evaluation passes the instruction without that document. NLI tokenization truncates pairs at 512 tokens. Document chunking discards overlong sentences and limits chunks; these rules change what evidence reaches each model and do not establish complete document coverage (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/data_utils.py`, `uncertainty/generate_response.py`, `uncertainty/scorer.py`, `uncertainty/templates.py`).

> if ('gold' not in type_ or not add_document) and not use_chatgpt:
>     document = ''
> --- `uncertainty/wiki_generation.py`

Independent thread-pool tasks receive selected inputs and return generated/scored values, with no model-directed delegation protocol. This resembles independent call frames whose return values are collected; there is no inspected mechanism that summarizes a growing transcript and later reloads removed turns. Dataset files, rather than context-frame pointers, cross stage boundaries. Memory revisions and detailed retention inventories are left to the memory member (SRC-1, `uncertainty/scorer.py`, `uncertainty/utils.py`, `uncertainty/wiki_generation.py`).

Capability, grants and isolation must not be conflated. The workflow's capability surface includes filesystem reads/writes, pickle deserialization, GPU execution, provider requests, and remote model-code loading. Its current credentials and filesystem grants are not supplied. Its deployed container/process isolation is unobserved. The inspected model-call adapters send prompts, not provider tool schemas or shell capabilities; Python and shell execute with host authority, independently of what the generated prose says. Models loaded with remote-code trust can introduce executable dependency behavior; that is a host loading decision, not an LLM approval gate (SRC-1, `uncertainty/utils.py`, `uncertainty/self_learning_training.py`, `script/tgi.sh`).

> trust_remote_code=True,
> use_cache = False if training_args.gradient_checkpointing else True,
> --- `uncertainty/self_learning_training.py`

Local batching, thread concurrency, token limits, optional quantization/PEFT, and Accelerate/FSDP handling affect resource use and execution paths. No benchmark or isolation guarantee follows. Training reports to TensorBoard and prints examples; generation prints failures/costs; evaluation appends aggregate scores. Retries and file reuse are partial recovery mechanisms, not transactional stage completion. External framework/provider internals and actual compatibility remain uninspected (SRC-1, `uncertainty/utils.py`, `uncertainty/scorer.py`, `uncertainty/self_learning_training.py`, `configs/training/sft_trainer.yaml`, `configs/training/dpo_trainer.yaml`, `requirements.txt`).

### Evidence coverage

All findings use SRC-1 at the frozen revision. Beyond boundary inspection, this member inspected complete generation, training, response-generation and evaluation drivers; complete scorer implementations; model-call, model-loading, validation and threshold helpers; document chunking and relevant training-data loaders; topic selection; prompt formatters; TinyLlama configuration; training/data configurations; and all four launchers. These supply **implementation** evidence. README supplies **doctrine/design**. Example-list bodies, unrelated dataset helpers, other model configurations and embedding/topic-ranking alternatives were not comprehensively analysed here; their presence does not establish activation in the predefined-topic route. No target execution, observed run, provider transcript, causal experiment or measured benefit was supplied. All operational and improvement conclusions remain bounded accordingly.

## Shared records

### Components

#### RT-CMP-causal-model
Label: Configured causal language model

Source-native identity: `base_model_name`, SFT/DPO model paths and TGI's `model` argument. Representational form: distributed-parametric. Storage substrate: external pretrained weights, local checkpoint directories, GPU memory, or external TGI process. This is the model role whose parameters the training route changes, including optional LoRA parameters later merged into the saved model. Inference calls run without a training update; serving internals are outside the boundary. Exact weight versions are not pinned: training requests `revision='main'`, direct inference omits an immutable revision, and local checkpoint paths are mutable. A TGI URL can resolve to another model without changing the client configuration (SRC-1, `configs/model/tinyllama.yaml`, `uncertainty/self_learning_training.py`, `uncertainty/utils.py`, `script/tgi.sh`).

> trainer.train()
> if saved_model_path is None:
>     saved_model_path = "trained_" + str(time.time()).replace('.', '_')
> if trainer.is_fsdp_enabled:
>     trainer.accelerator.state.fsdp_plugin.set_state_dict_type("FULL_STATE_DICT")
> trainer.save_model(saved_model_path)
> --- `uncertainty/self_learning_training.py`

#### RT-CMP-nli-model
Label: NLIScorer classification model

Source-native identity: `NLIScorer.nli_model`, selected by `NLI_MODEL`. Representational form: distributed-parametric classifier parameters. Storage substrate: externally downloaded model weights and local GPU memory. `SelfCheckGPT` and `BSDetector` select `potsawee/deberta-v3-large-mnli`; semantic consistency selects `microsoft/deberta-large-mnli`. The inspected scorer loads the classifier in evaluation mode and uses no-grad inference; it does not update these parameters. Exact versions are not pinned because no immutable model revision is passed; a later download may resolve different weights. No mutable HTTP endpoint is used for this component; upstream model resolution remains external (SRC-1, `uncertainty/scorer.py`).

> self.nli_model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL[scoring_method]).cuda()
> self.nli_tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL[scoring_method])
> --- `uncertainty/scorer.py`

#### RT-CMP-question-model
Label: OpenAI training-question and label model

Source-native identity: `question_model = 'gpt-3.5-turbo-0125'` and the optional GPT answer-generation branch. Representational form: distributed-parametric. Storage substrate: opaque OpenAI service. Used for training questions, context answers, optional labels and test greedy answers. The repository issues inference requests, not parameter updates. Exact service weight identity and provider-side parameter changes are uninspected; a dated API identifier is not a supplied weight digest or proof of immutability. Endpoint resolution can change outside repository control. The optional answer-generator label does not alone guarantee the provider model: its helper is passed `question_model` (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/utils.py`).

> question_model = 'gpt-3.5-turbo-0125'
> --- `uncertainty/wiki_generation.py`

#### RT-CMP-test-question-model
Label: OpenAI held-out question model

Source-native identity: `gpt-4-turbo-2024-04-09`. Representational form: distributed-parametric. Storage substrate: opaque OpenAI service. Repository inference only; no local parameter updates. Exact version beyond the API name and service-internal mutability are uninspected; mutable provider resolution is possible outside this source boundary. This component proposes test questions, not expected correct answers (SRC-1, `uncertainty/wiki_generation.py`).

> test_qn,cost = openai_call("gpt-4-turbo-2024-04-09",
>                             tp['instruction'],
>                             max_tokens=gen_kwargs['questions']['max_new_tokens'],
>                             temperature=0)
> --- `uncertainty/wiki_generation.py`

#### RT-CMP-judge-model
Label: LLMJudge GPT-4o model

Source-native identity: `LLMJudge(engine = "gpt-4o")`. Representational form: distributed-parametric. Storage substrate: opaque OpenAI service. The repository requests judgments without updating this model. Exact parameters are not pinned, and the unversioned API name may resolve another model over time; provider-internal learning is uninspected. Cache results can also outlive service changes (SRC-1, `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py`).

> llm_judge = LLMJudge(engine = "gpt-4o")
> --- `uncertainty/pairwise_eval.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-data-generation
Label: Wikipedia question and answer generation

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stage-local generated lists and scores; SFT generation terminates via `exit` after saving labels, while DPO generation writes scored answer pickle and returns from main.
- Later read-back: Questions, test JSONL, context answers, document cache and answer pickle are reloaded by later producer invocations; training reloads answer artifacts.
- Delegated visibility: OpenAI receives selected question/document/example messages; TGI or the local model receives formatted answer prompts; NLI receives selected reference/sample text, not the complete source corpus.
- Selection predicate: Predefined titles split by category; documents initially retained above 512 words, chunked to a 512-token target; question text checks and retries; reference-answer cleaning; empty/failed outputs omitted; scoring method chooses NLI/consistency processing.
- Invalidation or expiry: File existence controls reuse; no config/version-based expiry is implemented in this producer. Final scoring overwrites the answer pickle.
- Activation or effect: Code writes training candidates and numeric scores for a later training invocation; changed model behavior from these artifacts is unobserved.
- Evidence limits: Default scorer spelling and fresh-test indexing obstruct fresh starts; provider accuracy, successful completion and compatibility of local-versus-TGI answer representations are not demonstrated.

Endpoints/progression: operator wrapper → Python setup → document/topic selection → OpenAI question proposals → reference/sample answer proposals → NLI scores → disk. Owner and next-step policy: Python branches, fixed retry counts and file-existence rules. The operator chooses mode/config and supplies credentials, but is not asked to approve each proposed question or answer. OpenAI and the generator propose content; lexical checks and scoring code admit or omit it. Rejection ability includes `None` filtering and question retries. Recovery reuses existing artifacts, with no inspected atomic-write or rollback protocol (SRC-1, `script/wiki_ques_gen.sh`, `uncertainty/wiki_generation.py`, `uncertainty/utils.py`, `uncertainty/data_utils.py`, `uncertainty/topic_generator.py`).

Mode: bounded Wikipedia curriculum. Improvement trigger: explicit operator invocation, SFT/DPO flags and requested sampling, not a continuously scheduled loop. Reference outcome: source-document text supplies context, while generated `gold_answer` text is a model-produced target, not an independently certified correct answer. Training questions request answerability from the document; sampled consistency supplies a proxy rather than an answer oracle. Guidance consists of shipped few-shot examples and document-answering prompts. It persists in source; generated questions/answers/scores persist in artifacts. No workflow text or prompt rewrite is admitted by this route.

> all_scored_instances = get_scored_ds(ans_dict,'raw_answer_sample')
> with open(answer_path,'wb') as f:
>     pickle.dump(all_scored_instances,f)
> --- `uncertainty/wiki_generation.py`

Counterexample to turnkey invocation (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/scorer.py`):

> parser.add_argument("--scoring_method", type=str, default="SelCheckGPT",required=False)
> --- `uncertainty/wiki_generation.py`

That string is not a key in `NLI_MODEL` shown by the component's constructor. The DPO branch separately requires a question artifact:

> assert os.path.exists(question_path),'Reuse questions from sft phrase'
> --- `uncertainty/wiki_generation.py`

A fresh test file is another forcing case; the first operand indexes an empty list before testing the second operand:

> generated_test_questions = True if len(test_ds) == len(test_qn_prompts) else False
> generated_test_answers = True if ('greedy_response' in test_ds[0] and generated_test_questions) else False
> --- `uncertainty/wiki_generation.py`

The `--iter` option changes the answer filename but the inspected model selection still starts from configured SFT; that flag alone does not wire successive DPO checkpoints into an autonomous iterative trainer (SRC-1, `uncertainty/wiki_generation.py`).

#### RT-RTE-model-training
Label: SFT and DPO checkpoint admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Trainer completion saves a checkpoint; optional PEFT handling merges adapters and saves the merged model. The CLI has no agent-facing structured return.
- Later read-back: Response generation directly loads configured checkpoint paths; operators can serve them through TGI. Generation's DPO-data phase loads an SFT model, not automatically the preceding DPO output.
- Delegated visibility: Trainer workers receive formatted SFT text or prompt/chosen/rejected triples; DPO triples omit document metadata. Accelerate coordinates process execution; provider services are not asked to approve checkpoints.
- Selection predicate: SFT optionally keeps low-question-hallucination records; DPO optionally filters questions, then selects unknown records and NLI-ranked preference pairs. With reference-as-chosen enabled, the single-preference pair and first multiple-preference pair use extracted `gold_answer`; additional multiple-preference pairs use selected `gold_answer_sample` entries instead. Optional length normalization further selects examples.
- Invalidation or expiry: Paths encode some flags and hyperparameters but are not immutable versions; configured overwrite and save limits govern local retention. No automatic semantic invalidation of old generated data is shown.
- Activation or effect: The trainer is called to modify model/adaptor parameters and save them. Later inference consumption is wired but exercised behavioral effects and improvement are unobserved.
- Evidence limits: No saved weights, training trace or evaluation comparison is supplied. External trainer internals and dependency compatibility are uninspected; a call to `trainer.train()` does not demonstrate its successful execution.

Endpoints: operator → `train.py` → persisted dataset reload → sample construction → `do_train` → SFTTrainer/DPOTrainer → checkpoint directory. The operator selects SFT/DPO, thresholds, epochs/steps, PEFT and configuration. Python decides example eligibility and constructs training/validation splits; the external trainer performs optimization. The program asserts one positive duration choice, with the other negative. No per-example human approval or post-judge admission gate appears along this traced path (SRC-1, `uncertainty/train.py`, `uncertainty/self_learning_training.py`).

> assert (args.max_epochs > 0 and args.max_steps < 0) or (args.max_epochs < 0 and args.max_steps > 0), 'Either max_epochs or max_steps should be set.'
> --- `uncertainty/train.py`

Operating mode: bounded training experiment/curriculum under operator control. Trigger/proposed change: explicit training launch proposes replacing/adding model parameters based on retained labels/preferences. Admission: scorer/rule-selected samples reach optimization and the resulting model is saved without an evaluation-win requirement. Rejection: code drops invalid pairs and thresholds exclude records; the operator can decline to launch or consume a checkpoint. Recovery: checkpoint retention is configurable; no automatic revert-to-baseline on unfavorable judge result is wired. The optional TinyLlama best-model branch uses validation loss when not saving last only, not external correctness. PEFT merge deletes adapter files, so it is not a universal reversible adapter deployment mechanism (SRC-1, `uncertainty/train.py`, `uncertainty/self_learning_training.py`, `configs/training/sft_trainer.yaml`, `configs/training/dpo_trainer.yaml`).

Guidance: fixed selection code, thresholds, supervised labels or chosen/rejected preferences, and configured optimization settings. What persists: parameters and optional intermediate checkpoints; not a formulated criticism of the training method. Answer oracle: generated targets/preferences are optimization references; no independent expected correct answer is required by the selector. NLI judgment is not a truth oracle.

> if args.unknown_threshold > 0.:
>     unknown_ds = return_question_type(filtered_ds,args.scoring_method,'unknown',args.unknown_threshold) # filter to unknown samples.
> else:
>     unknown_ds = dataset
> --- `uncertainty/train.py`

This bypass is material to selection coverage. For SelfCheckGPT, `unknown` means a stored hallucination score greater than the threshold, not measured lack of factual knowledge:

> unknown_qns = [x for x in data if x[scoring_key] > score_threshold ]
> known_qns = [x for x in data if x[scoring_key] <= score_threshold]
> --- `uncertainty/utils.py`

The multiple-preference path selects context-conditioned answer samples by `gold_answer_scores` when `question_filtering < 1.0`, otherwise retaining all candidate positions before sampling. It selects raw answers by `unknown_filtering` when positive, then sorts or samples the candidate lists, capped using `shortest_len`. Its first pair uses `chosen_ans = gold_answer`; subsequent pairs use `g[0]` from the selected context-conditioned samples. These numerical rules do not enforce textual identity with the reference or factual correctness. The training driver admits those additional returned pairs through `extend`, not just the initial reference pair (SRC-1, `uncertainty/scorer.py`, `uncertainty/train.py`).

> for g,r in zip(gold_answer_sample,filtered_raw_answer_sample[1:]):
>     out_dict.append({
>     'instruction':instruction,
>     'topic':topic,
>     'category': category,
>     'chosen_ans':g[0],
>     'rejected_ans':r[0],
>     'question_score':question_score
>     })
> --- `uncertainty/scorer.py`

> if args.multiple_pref:
>     train_ds.extend(scorer.get_dpo_sample(d,multiple_pref=True,unknown_filtering=args.unknown_threshold,question_filtering=args.question_filtering_threshold))
> else:
>     train_ds.append(scorer.get_dpo_sample(d,multiple_pref=False,unknown_filtering=args.unknown_threshold,question_filtering=args.question_filtering_threshold))
> --- `uncertainty/train.py`

Learning: future capacity improvement is uninspected, separately from implemented parameter updating. Self-improvement assessment boundary: the model-building workflow including its later model consumer; horizon: operator-mediated generation/training/evaluation invocations; objective: more truthful, question-relevant Wikipedia responses, specified independently of a particular checkpoint. The source affords improvement-directed self-change when a generated-data-trained checkpoint becomes its later generator. Link 1 (evidence shaping update) and link 2 (parameter change) are wired by selection and training; link 3 (later behavioral-authority path) is wired by checkpoint loading. Link 4 (subsequent behavior causally depending on that update) is not observed. This supports a dispositional pathway, not exercised or successful self-improvement. Reflection, autonomy and formulated-theory criticism are not inferred from numerical training or the repository name.

#### RT-RTE-response-generation
Label: Checkpoint and endpoint response generation

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Batched generation yields greedy answers; the driver writes instruction/response JSONL.
- Later read-back: Pairwise evaluation reloads that JSONL as evaluation or baseline responses.
- Delegated visibility: Direct or TGI model receives formatted questions, base-model examples when applicable, and source documents only in RAG mode. Worker threads return values to the calling process.
- Selection predicate: CLI mode and flag-derived paths select base/SFT/DPO models locally; TGI selection is solely the endpoint. `--known` selects or persists a 200-question known subset instead of the normal test file.
- Invalidation or expiry: Response output is overwritten per derived path; existing known-subset files are reused. No endpoint-weight identity check or automatic expiry is shown.
- Activation or effect: Model calls are wired to produce response artifacts. Actual dependence on a changed checkpoint is not observed, especially for independently served TGI.
- Evidence limits: No response artifact or service trace is supplied. RAG and DoLA branches exist but successful operation is not established; DoLA explicitly disallows TGI.

Owner: the operator selects mode and starts the server; code batches examples and calls `HF_generate`. The ordinary test output is greedy only: sampled-response code is disabled by `if False`. Terminal effect is a file, not a tool action. The instruction/document text has model-interpretive authority over answer content, not direct authority to execute host commands. Mode `oracle` is an evaluation-side alternate, not a response-generation checkpoint mode (SRC-1, `uncertainty/generate_response.py`, `uncertainty/utils.py`, `uncertainty/pairwise_eval.py`).

> if args.use_tgi:
>     client = InferenceClient(model = f"http://127.0.0.1:{args.port}")
> else:
>     client = load_hf_model(model_path,use_flash=use_flash).eval()
> --- `uncertainty/generate_response.py`

This creates a control-path distinction: the tokenizer is loaded by `model_path` in both modes, but the server weights are not selected by that argument. The shipped server launcher defaults to base TinyLlama; the operator must change it for checkpoint consumption (SRC-1, `script/tgi.sh`).

> model=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T # change the model name here.
> --- `script/tgi.sh`

No automatic deployment, rollback or model-judge veto is part of this read route. Recovery is operator rerun/reselection rather than a coded successor-admission loop. The testing wrapper also leaves `answer_generator` and `beta` undefined locally while expanding them into arguments; it is not a self-contained guarantee of matching generation and evaluation configurations (SRC-1, `script/testing.sh`).

#### RT-RTE-pairwise-evaluation
Label: Document-conditioned pairwise judging

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Judge returns win/lose/tie labels, cost and no-count count; evaluator prints and appends aggregate text results.
- Later read-back: Judge cache pickle is loaded on later judge construction; cached identical prompt content skips new requests. No automatic training consumer of aggregate results is wired in these drivers.
- Delegated visibility: GPT-4o receives question, source document and both response texts twice in reversed orders. It does not receive the training trajectory or checkpoint bytes.
- Selection predicate: Evaluation joins responses by instruction against the baseline; two parsed choices agreeing on a response yield win/lose, inconsistent order choices yield tie, and missing valid choices produce no-count omissions.
- Invalidation or expiry: Cache is keyed by first formatted user-message content and partitioned by engine name; no model-revision, system-prompt or time-based expiry is included. Result text is appended.
- Activation or effect: Judgment requests and aggregate scoring are wired, but their quality and any influence on subsequent operator choices are unobserved.
- Evidence limits: Cached scores, provider reliability and end-to-end results are not supplied. Denominator is counted results; zero counted results has no explicit division guard. Hardcoded hallucination placeholders are not measured hallucination outcomes.

Endpoints: operator's baseline/evaluation response paths → `pairwise_eval.py` joins test documents → `LLMJudge.evaluate` → cache/provider → result file. Owner: Python selects comparisons; GPT-4o proposes rankings; parser/order logic decides result category. Operator supplies baseline and may interpret scores later; the evaluator cannot veto checkpoint saving because training is a separate prior invocation. Answer oracle/reference outcome: document text is the reference for the requested truthfulness/relevance ranking. There is no expected A/B label from independent ground truth. Evaluation mode `oracle` substitutes test dataset `greedy_response` values, which generation obtained from GPT-3.5 without documents; the mode name does not certify correctness (SRC-1, `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py`, `uncertainty/wiki_generation.py`).

> if len(pair_result) == 2:
>     if pair_result == correct_order:
>         result = 'win'
>     elif pair_result == wrong_order:
>         result = 'lose'
>     else:
>         result = 'tie'
> --- `uncertainty/scorer.py`

Guarantee owner: LLMJudge request/parser code. Enforcement point: two-order completion and parsing. Strength: **best effort** for bias reduction and valid judgments, not an accuracy invariant. Covered path: uncached two-order requests; alternate: cache reuse. External contract: provider follows the requested ranking and reference document is adequate. Implementation conclusion status: wired. Operation conclusion status: uninspected. Benefit conclusion status: uninspected. Requests use at most three tries per order, with exceptions printed and a five-second sleep; failures can remove a question from the denominator (SRC-1, `uncertainty/scorer.py`).

> self.cache[message['message'][0][-1]['content']] = rel
> --- `uncertainty/scorer.py`

This cache key includes response and document text through formatting, but not the system message or actual provider weight identity. The evaluator's hallucination branch is disabled and replaces scores with `[0]`, so its printed zeros cannot support factuality improvement (SRC-1, `uncertainty/pairwise_eval.py`).

> base_hallu = [0]
> eval_hallu = [0]
> --- `uncertainty/pairwise_eval.py`

### Claims

#### RT-CLM-knowledge-filtering
Label: Claimed knowledge-score workflow

Claimed operation: README describes context-conditioned sampling for consistency filtering and context-free sampling for knowledge scoring. This is doctrine/design; the implementation supplies document omission, NLI scoring and training selection described above, not a demonstrated correspondence between contradiction and factual knowledge (SRC-1, `README.md`).

> 3) Generate the K sampled responses given the document ($Y_c$) as context for consistency filtering and compute the consistency score, $S_L$.
> 4) Generate K sampled responses without the context for $Y_r$ and compute knowledge score $S_K$.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-checkpoint-consumption
Label: Saved parameters to later answers

Consumer: local causal model loader or separately configured TGI server. Channel: checkpoint files/model identifier resolved into distributed-parametric weights. Force: numerical generation behavior, not advisory prose. Horizon: subsequent process invocations that select the saved artifact. Training changes parameters and saves them; direct response generation consumes a derived SFT/DPO path, while TGI consumption depends on the operator's matching server selection. This is a live-capable wired path, not observed activation or demonstrated improvement. Source evidence is the save passage in [RT-CMP-causal-model](#rt-cmp-causal-model) and the direct-versus-endpoint passage in [RT-RTE-response-generation](#rt-rte-response-generation) (SRC-1, `uncertainty/self_learning_training.py`, `uncertainty/generate_response.py`, `script/tgi.sh`).

## Annotations

none
