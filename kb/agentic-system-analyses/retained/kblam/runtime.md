---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "KBLaM runtime baseline: knowledge-conditioned generation, alternate context routes, dataset admission and adapter training at the frozen research implementation."
run-id: AAS-2026-10-15-kblam-5a0c2fe96cc1-01
reviewed-boundary: "69683ad096e022b58854fd88c0c58968c7d8c470"
---

# KBLaM runtime report

## Runtime account

### Work and evidence basis

KBLaM supplies external knowledge to a modified causal language model. It does not assign next actions to an autonomous agent: the shipped Python drivers choose examples, model calls, optimization steps and file writes. The consequential work is answering questions with knowledge represented as extra attention keys and values, plus producing the datasets, embeddings and trained adapters consumed by that operation. The README calls this a research project and warns that answers can be incomplete or entirely incorrect. Its linear-overhead and grounded-answer claims are declarations, not measured results here ([RT-CLM-knowledge-augmentation](#rt-clm-knowledge-augmentation)).

All source citations below refer to SRC-1 at the boundary's frozen commit. Evidence is inspected implementation or explicitly attributed doctrine/design. No target code, tests, model calls or benchmarks were executed. Operation, activation and benefit are unobserved. Additional inspected coverage includes the full encoder, processor, GPT helper, embedding and split scripts; material bodies of both attention implementations, generation input preparation, evaluation modes, query-head selection, optimizer and checkpoint logic; and the reference-answer scorer. These extend the boundary's initial inspection, not its source register. External weights, provider internals, local checkpoints and complete synthetic payload remain outside available execution evidence. Notebook outputs are not used as run evidence.

### Ordinary shipped invocation: accuracy evaluation

The ordinary source-level invocation selected here is `experiments/eval.py`'s `accuracy` subcommand. The frozen CLI cannot reach its configured dispatch: its top-level import requests `aug_row`, but the fully inspected `src/kblam/utils/data_utils.py` defines `augment_row` and no `aug_row` alias. Compatible external assets alone do not suffice; source repair is also necessary, even when fancy questions are disabled. The internal fancy-question branch also calls `aug_row`, so repairing only the import without binding that name would not repair that branch. The account below traces the implemented dispatch to `eval_accuracy_cli` and `eval_accuracy` conditionally on repairing this mismatch; it does not establish unchanged CLI reachability (SRC-1, `experiments/eval.py`, `src/kblam/utils/data_utils.py`; minimum passages in [RT-RTE-accuracy-generation](#rt-rte-accuracy-generation)). The principal is the experiment launcher; CLI arguments identify the dataset, embedding paths, encoder checkpoint, model and tokenizer locations, model family, KB size and output locations. These are configuration identities, not verified immutable model identities. `_prepare_models` loads the requested Llama or Phi implementation, tokenizer and encoder state; it sets the model to evaluation mode and constructs a separate KB configuration with a separate query head enabled. `KBRetriever` loads both cached arrays when supplied, otherwise encodes selected records. Selection is by dataset indices, not a semantic-search service (SRC-1, `experiments/eval.py`, `src/kblam/utils/train_utils.py`).

[RT-RTE-accuracy-generation](#rt-rte-accuracy-generation) traces the internal path behind that import failure. Code selects all records or a random subset without replacement, chooses questions from its first test-batch records, formats model-family-specific user/assistant headers, tokenizes them and supplies `kb_kvs` to `model.generate`. The encoder turns each selected key and description, or each cached base vector, into layer-specific projected tensors. The model's next-token computation owns token production; Transformers' external generation machinery owns stopping and decoding policy subject to the explicit 60-token bound. The driver owns the next experiment step. Its intended terminal result after source repair and compatible setup is decoded output text, saved attention arrays and attention-index accuracy measurements; the unchanged CLI instead stops at the import failure before these branches. There is no tool-result or child-agent return in this loop.

At configured layers, the attention implementation reshapes projected knowledge into heads, concatenates it before text keys/values, extends the attention mask, optionally substitutes a separate query projection's KB scores, normalizes scores jointly and multiplies by values. Thus external knowledge bypasses text tokenization but not numerical attention competition. Natural-language knowledge is transformed into distributed-parametric vectors; configuration and record indexing are symbolic. Model and encoder mutability are separate in [RT-CMP-llama3-model](#rt-cmp-llama3-model), [RT-CMP-phi3-model](#rt-cmp-phi3-model), and [RT-CMP-kb-encoder](#rt-cmp-kb-encoder).

The process retains text KV-cache state during generation. Llama generation preparation keeps only unprocessed token IDs, crops masks if a cache limit applies, and carries `kb_kvs` and `kb_config` forward. This is current-invocation working state, not a write-back of generated answers into the KB. The external knowledge stays separately supplied each step. The source wires these controls; it does not establish successful cache-limit operation on actual model assets (SRC-1, `src/kblam/models/llama3_model.py`).

### Forcing cases and material alternates

Four challenges bound the runtime account rather than assuming one wrapper covers every path.

1. **No KB and textual KB.** The generation evaluator also selects `icl` or `zeroshot`. ICL concatenates `key is value;` text and instructions into the token sequence and passes no numerical KB; zeroshot supplies instructions and the question without that knowledge. These bypass the numerical admission path. The `standard` evaluator makes paired no-KB/true-KB calls, but that source comparison is not a supplied causal experiment. The no-KB equality claim remains qualified in [RT-CLM-base-preservation](#rt-clm-base-preservation). See [RT-RTE-evaluation-modes](#rt-rte-evaluation-modes).
2. **Direct tensors and another model family.** `KBLaMProcessor` can encode text pairs or base embeddings and returns a `BatchFeature` containing `kb_kvs`; callers may also pass tensors directly to the model without this processor. Both Llama and Phi attention accept unbatched or batched KB tensors. Consequently processor formatting and checkpoint loading are not universal enforcement points. The public helper itself passes extra positional arguments to a constructor accepting only tokenizer and args positionally; successful helper invocation is not established. See [RT-RTE-direct-inference](#rt-rte-direct-inference).
3. **Dynamic selection.** Llama optionally prunes knowledge to top-k rows using query/key scores summed across heads and query positions. The helper asserts a nongradient query, so this is an inference-time selection path, not a training mechanism. Phi's inspected attention body has no corresponding pruning branch. Llama's pruned return slices score positions rather than gathering the selected score indices, limiting confidence in the separate-query-head/pruning combination. This prevents treating pruning as a proven equivalent optimization. See [RT-RTE-kb-attention](#rt-rte-kb-attention).
4. **Change and recovery paths.** Training changes adapters and optionally selected query heads, persists artifacts and later loads them; dataset generation admits model-written records before training. These are different consumers and admissions from inference. Checkpoint save/resume paths and generator spelling/format defects prevent claiming a working uninterrupted production pipeline. See [RT-RTE-adapter-training](#rt-rte-adapter-training) and [RT-RTE-dataset-production](#rt-rte-dataset-production).

### Guarantees, effects and authority

The load-bearing structural guarantee is conditional knowledge insertion, owned by the model attention implementation and enforced at its `kb_kvs is not None` and layer-frequency branch. Its strength is an **invariant** of that branch for compatible tensors/configuration, not a guarantee of truth, relevance or refusal. It covers direct model calls and wrapper calls that reach the inspected attention path, including batched and unbatched shapes; it does not cover the ICL/zeroshot alternative or upstream data quality. It requires external tensor, tokenizer, model-shape and Transformers contracts. Implementation conclusion status: wired. Operation conclusion status: uninspected. The minimum enforcement passage is in [RT-RTE-kb-attention](#rt-rte-kb-attention).

Training's freezing policy is owned by the training driver, not by the inference model. It sets all model parameters nongradient, then conditionally enables selected query heads and includes them in the optimizer. Encoder projections remain trainable. Guarantee strength: protocol, limited to that driver and its optimizer setup. It is not a restriction on arbitrary library callers modifying weights. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-adapter-training](#rt-rte-adapter-training).

Capability surface and actual grants differ. Drivers can read/write caller-selected local artifacts, load model code with `trust_remote_code=True`, and the GPT helper authenticates to a caller-selected Azure endpoint with persisted device-code credentials. These are host-side capabilities, not privileges selected by generated answers. The helper allows unencrypted credential-cache storage. Actual filesystem permissions, Azure grants and a deployed isolation envelope are uninspected; neither these APIs nor a model allowlist proves sandboxing. No inference answer dispatches a shell or tool in the inspected generation path. This is a bounded description of that path, not a repository-wide security absence claim (SRC-1, `src/kblam/gpt_session.py`, `src/kblam/utils/model_utils.py`, `experiments/eval.py`).

Dataset and training admission are detailed below. New model-family support is a source-code change rather than a model-selected runtime extension: the README says to update model processing scripts. Local model/tokenizer loads explicitly trust remote code; that external loader's isolation is not supplied. Neither mechanism establishes autonomous self-modification. Behavioral authority through numerical knowledge and retained parameters is separately recorded in [RT-BAP-knowledge-attention](#rt-bap-knowledge-attention) and [RT-BAP-checkpoint-consumption](#rt-bap-checkpoint-consumption).

## Shared records

### Components

#### RT-CMP-llama3-model
Label: KblamLlamaForCausalLM

Source-native component in SRC-1, `src/kblam/models/llama3_model.py`; loaded by `experiments/eval.py` and `experiments/train.py`. Form: distributed-parametric transformer weights and runtime tensors; substrate: PyTorch CPU/GPU state, pretrained directories and saved model artifacts. Parameters are not updated by the inspected no-gradient evaluation calls. Training optionally updates selected separate query projections after freezing the rest. Exact external pretrained/checkpoint version is not pinned by the reviewed repository commit; callers provide locations. A remote model location can resolve differently absent an external revision contract. Provider/Hub internals are uninspected.

> query_states_2 = self.q_proj_new(hidden_states)
> --- `src/kblam/models/llama3_model.py`

#### RT-CMP-phi3-model
Label: KBLaMPhi3ForCausalLM

Distinct Phi implementation in SRC-1, `src/kblam/models/phi3_model.py`, selected by evaluation/training family arguments. Form and substrate: distributed-parametric transformer weights in PyTorch and checkpoint files. Inference is no-gradient in the inspected callers; training can enable selected `q_proj_new.weight` parameters. Exact pretrained revision is caller-supplied, not pinned here; a remote asset may change. External weight/loader behavior remains uninspected. Phi's KB attention consumer is distinct from Llama's pruning path.

> attn_weights_2 = torch.matmul(
>     query_states_2, kb_keys.transpose(2, 3)
> ) / math.sqrt(self.head_dim)
> --- `src/kblam/models/phi3_model.py`

#### RT-CMP-kb-encoder
Label: KBEncoder

SRC-1, `src/kblam/kb_encoder.py`: distributed-parametric key/value projectors, optional sentence-transformer backbone and special-token embedding in PyTorch; encoder state persists in `encoder.pt`. Key projection includes nonaffine normalization; value projection does not. Backbone can be frozen or trainable by constructor option; the inspected drivers request frozen backbones. Projections change during adapter training but not through the inspected evaluation calls. SentenceTransformer's model name has no explicit revision pin. OAI/BigOAI can use supplied cached vectors or an online endpoint; cached data does not pin the historical provider weights. The projection checkpoint's provenance is unresolved when supplied only as a path.

> return self.key_layernorm(self.projector_k(base_embedding)).bfloat16()
> --- `src/kblam/kb_encoder.py`

> return self.projector_v(base_embedding).bfloat16()
> --- `src/kblam/kb_encoder.py`

#### RT-CMP-gpt-session
Label: GPT provider client

SRC-1, `src/kblam/gpt_session.py`: symbolic Azure client configuration and natural-language messages cross into opaque distributed-parametric chat/embedding services. Client state lives in process memory; authentication records/cache persist on the host. Allowed model names are not exact weight versions. The configured endpoint can resolve to a changed deployment; provider parameter changes and retained provider state are uninspected. The client implements no parameter-update operation. Generation and scoring use this service through separate prompts; embedding generation uses the embeddings endpoint.

> valid_models = ["gpt-4o", "ada-embeddings", "text-embedding-3-large"]
> --- `src/kblam/gpt_session.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-accuracy-generation
Label: Accuracy driver to generated output and attention-index scores

Endpoints and owner: intended internal progression is operator-configured `accuracy` CLI → `_prepare_models`/`KBRetriever` → `eval_accuracy` → model generation → local result files. The frozen module's top-level `aug_row` import fails against its shipped data utility, which defines only `augment_row`; this blocks CLI dispatch before loading or generation regardless of the fancy-question flag. Source repair must also preserve the name used by the internal fancy-question call. The following effects describe internal branch wiring conditional on that repair and compatible assets, not a reachable unchanged CLI. Code chooses data and scoring; the model chooses tokens. Context is the formatted questions plus projected selected KB, not a conversation history. State is the loaded dataset/arrays, model/encoder and generation cache. The answer oracle for attention-index accuracy is the first test-batch rows' positions in the selected KB, supplied by code as `np.arange(test_batch_size)`. It measures selected-row attention ranking, not answer truth. Operating mode is a bounded experiment; human contribution is configuration/assets, not per-output approval (SRC-1, `experiments/eval.py`).

- Immediate return: `eval_accuracy` returns layer-index accuracy/top-five dictionaries; decoded answers and arrays are also written to caller-selected paths.
- Later read-back: saved attention arrays are reloaded in the same evaluator for metrics; no generated-answer admission into later KB inference is wired here.
- Delegated visibility: inapplicable — no child agent; tensors go to the local model and results to the caller/files.
- Selection predicate: full dataset at equal size, error above dataset size, otherwise random subset without replacement; questions come from its first test-batch rows.
- Invalidation or expiry: in-memory state ends with its owner; result paths can be overwritten; no semantic freshness policy in this route.
- Activation or effect: knowledge tensors enter generation and attention files feed scoring in source; actual answer changes remain unobserved.
- Evidence limits: the known top-level import mismatch blocks unchanged CLI execution before model loading; source repair as well as compatible external model/encoder assets is necessary. No supplied run establishes repaired execution or metrics; internal assumptions include a sufficiently large selected subset and family-compatible shapes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The wired implementation status describes the inspected internal progression, not successful CLI entry or completion. Full inspection of SRC-1, `src/kblam/utils/data_utils.py` establishes the missing alias, rather than a search miss alone.

> from kblam.utils.data_utils import aug_row, generate_multi_entity_qa
> --- `experiments/eval.py`

> def augment_row(row: dict[str, str]) -> list[dict[str, str]]:
> --- `src/kblam/utils/data_utils.py`

> input_strs_gen = (aug_row(dataset_subset[i]) for i in range(test_batch_size))
> --- `experiments/eval.py`

> label = np.arange(test_batch_size)
> --- `experiments/eval.py`

> weight = weight.reshape(test_batch_size, -1, kb_size)
> acc = (weight.sum(1).argmax(1) == label).mean()
> --- `experiments/eval.py`

#### RT-RTE-kb-attention
Label: Projected KB admission into attention

Endpoints: caller's `kb_kvs` and `kb_config` → layer-specific reshape → optional Llama pruning → concatenated keys/values and masks → softmax/value aggregation. Owner is model code. Decision policy combines symbolic layer selection with learned numerical attention. The contextual state consists of current hidden states, text cache and externally supplied KB tensors. There is no answer oracle or candidate-approval step in this read/compute route (SRC-1, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py`).

- Immediate return: attention output tensor, then model logits/generation to the enclosing caller.
- Later read-back: inapplicable — this route does not persist a KB update; generation cache is current-invocation state.
- Delegated visibility: inapplicable — numerical model layers, not delegated principals, consume the tensors.
- Selection predicate: non-null KB and layer index divisible by frequency; optional Llama dynamic sparsification ranks rows by summed query/key scores, top-k across heads/query positions.
- Invalidation or expiry: tensors are supplied per invocation; selection may be recomputed as generation progresses; no retained expiry metadata.
- Activation or effect: source connects KB values to weighted attention output; successful activation or improved grounding is not observed.
- Evidence limits: shape/config compatibility and external generation semantics are assumed; dynamic pruning's score-slicing issue limits equivalence claims; Phi's inspected branch has no dynamic-pruning counterpart.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if kb_kvs is not None:
>     if self.layer_idx % kb_layer_frequency == 0:
> --- `src/kblam/models/llama3_model.py:256-257`

> key_states = torch.concat([kb_keys, key_states], dim=2)
> value_states = torch.concat([kb_values, value_states], dim=2)
> --- `src/kblam/models/llama3_model.py:292-295`

> return kb_keys, kb_values, attn_weights[..., :topk_size]
> --- `src/kblam/models/llama3_model.py`

The pruning score return is not a gather by `top_idx`, although keys and values are gathered by that index. Hence identical outputs to unsparsified attention cannot be assumed, especially with separate-query-head score reuse. Its nongradient assertion is an invariant at that helper, not a restriction on every caller's model mutability.

#### RT-RTE-direct-inference
Label: Processor and direct-model entry paths

SRC-1, `src/kblam/models/kblam_processor.py`, `src/kblam/utils/model_utils.py`, `src/kblam/utils/eval_utils.py`. Endpoints: caller's text pairs/base embeddings → processor → `BatchFeature`, or caller's tensors directly → model/`answer_question`. Caller owns data and controls; processor constructs Llama-style text headers and encodes recognized list types. `answer_question` formats by model family and bounds generation to 150 new tokens. Constructor/load behavior is not an admission gate for callers using direct tensors.

- Immediate return: processor returns tokenizer fields and `kb_kvs`; generation helper returns decoded, header-pruned text.
- Later read-back: encoder checkpoint is loaded for inference; this read route makes no persistent knowledge write.
- Delegated visibility: inapplicable — local caller/model interface, no worker handoff.
- Selection predicate: recognized list input's first element determines string encoding versus base-embedding encoding; direct callers choose all supplied tensors.
- Invalidation or expiry: inapplicable — caller controls input and lifetime; checkpoint changes require subsequent loading.
- Activation or effect: processor delivers KB tensors without proving use; direct calls reach the attention consumer when compatible.
- Evidence limits: `load_model_and_processor` passes extra positional arguments to `KBLaMProcessor`, whose constructor accepts two positional arguments besides self; processor defaults to CUDA in its encoder; no successful public-helper run is supplied.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> return BatchFeature(data={**text_inputs, "kb_kvs": knowledge_base})
> --- `src/kblam/models/kblam_processor.py`

> processor = KBLaMProcessor(tokenizer, args, get_oai_embd_online, token)
> --- `src/kblam/utils/model_utils.py`

> def __init__(self, tokenizer: AutoTokenizer, args: EncoderArgs, **kwargs):
> --- `src/kblam/models/kblam_processor.py`

The afforded status reflects implemented interfaces with a visibly defective convenience-loader connection; it does not withdraw the separately wired direct model route.

#### RT-RTE-evaluation-modes
Label: KB, textual-context, zeroshot and judgment modes

SRC-1, `experiments/eval.py`, `src/kblam/utils/eval_utils.py`, `experiments/output_scorer.py`. Endpoints: sampled dataset and selected mode → question generation → postprocessing → reference comparison/result files. Code decides modes and sample membership. In `kb` mode it supplies tensors; `icl` supplies serialized key/value text with instructions; `zeroshot` supplies the question and response-format instruction. The refusal task mixes questions from included and excluded row indices, then classifies refusal by the substring `sorry`. These are experimental comparisons, not live routing by the model.

Answer oracles: dataset `A`/description fields for generation metrics; code's inclusion/exclusion labels for refusal; exported `True answer:` text for the GPT scorer. The GPT judge supplies a judgment, not an independent oracle. Human contribution is launching/configuring tasks and selecting inputs, with no per-score veto in the scorer. No source-wired score threshold admits a new checkpoint. Improvement triggers are external experiment choices, not an automatic score-to-successor loop.

- Immediate return: evaluation routines return generation text/metric dictionaries; CLI and scorer persist metrics or example scores.
- Later read-back: exported predictions/reference text can be read by the separate scorer; no score-driven deployment or KB update is established.
- Delegated visibility: scorer sends candidate text and expected answer to Azure chat; provider internals are opaque, not an inspected child-agent runtime.
- Selection predicate: seeded random KB indices; refusal samples outside those indices; mode flag selects tensor versus text versus no knowledge; optional `remove_sorry` omits selected outputs from metric inputs.
- Invalidation or expiry: output files may be replaced/appended; no score expiry or dependency invalidation is wired in these routines.
- Activation or effect: modes change model-visible context; postprocessing changes what reaches metrics; judged quality or comparative benefit is unobserved.
- Evidence limits: the same top-level `aug_row` import failure blocks all unchanged `experiments/eval.py` CLI modes before dispatch, as established in [RT-RTE-accuracy-generation](#rt-rte-accuracy-generation); the internal modes described here are conditional on source repair. Separately, `perform_eval`/`perform_eval_refusal` pass `topk_size` to `answer_question`, whose signature lacks it, preventing an unqualified working generation/refusal CLI claim; scorer defaults to `GPT4`, outside the GPT helper allowlist; metrics remain implementation only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> prediction = [int("sorry" in model_output) for model_output in model_outputs]
> --- `experiments/eval.py`

> Return a score of 1 if the text is exactly the same as the ground truth answer,
> Return a score of 0 if the text is completely wrong,
> Return a score between 0 and 1 if the text is partially correct. A more correct text should have a higher score.
> --- `experiments/output_scorer.py`

Separate open-ended judgment is shipped in `experiments/output_scorer_open_ended.py`; this report does not assess its detailed rubric or actual judgments. The wired status concerns explicit mode/metric policy, not a claim that the defective wrapper paths complete.

#### RT-RTE-dataset-production
Label: Synthetic records, embeddings and paired split admission

SRC-1, `dataset_generation/gen_synthetic_data.py`, `dataset_generation/generate_kb_embeddings.py`, `dataset_generation/create_train_test_split.py`. Operator starts scripts and selects model, paths and split index. Code proposes seed instructions; GPT proposes entity JSON, related people, perturbed questions and extended QA. JSON construction/regex extraction admit syntactically acceptable responses, not verified truths. The knowledge guidance requests descriptions/objectives/purpose and QA based only on supplied information. No per-record human approval is wired. Operator can choose/edit/replace input files before later runs; that capacity is distinct from demonstrated human curation. Operating mode is bounded synthetic-data construction, not an open agent task. There is no independent factual answer oracle.

- Immediate return: generator constructs entity/QA records; embedding command saves key/value arrays; split command writes corresponding train/test records and arrays.
- Later read-back: generator reloads existing raw/QA files to skip prior stages; embedding/split/training/evaluation drivers load selected retained files in later invocations.
- Delegated visibility: Azure receives generation prompts or individual key/description strings for online embeddings; local sentence encoding is another branch; no agent delegation is implemented here.
- Selection predicate: prompt combinations generate entities; three property types create QA rows; embedding branch selects named encoder; split slices records and both arrays at the supplied index.
- Invalidation or expiry: existing raw/QA path presence skips regeneration; there is no source-wired semantic invalidation on prompt/model change; later file replacement is caller-controlled.
- Activation or effect: persisted records/arrays are inputs to subsequent training or generation paths; no completed pipeline or beneficial knowledge change is observed.
- Evidence limits: generator CLI calls nonexistent `perturbe_names` rather than declared `perturb_names`; saved linewise records and downstream JSON-array readers require compatible preparation; these defects prevent claiming the script as a turnkey end-to-end pipeline.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection/recovery: model output is parsed into `Entity`, transformed to data points, then appended by save helpers. Exceptions in generation/augmentation print errors and skip individual items; this rejects parse failures, not semantic errors. No quality-based rollback is wired. Embedding arrays overwrite named outputs; split regenerates separate output files without content approval. A user can rerun or replace files, but automatic transactional recovery across record/array outputs is not established. Detailed retained-object revision findings are left to the memory member.

> entity = Entity(**json.loads(gpt_output))
> return entity
> --- `dataset_generation/gen_synthetic_data.py:185-187`

> test_key_embds = np.load(embedding_keys_path).astype("float32")[split_index:]
> test_value_embds = np.load(embeddings_values_path).astype("float32")[split_index:]
> --- `dataset_generation/create_train_test_split.py`

#### RT-RTE-adapter-training
Label: Supervised optimization, checkpoint admission and reload

SRC-1, `experiments/train.py`, `src/kblam/utils/train_utils.py`, `experiments/eval.py`. Trigger is an operator-launched bounded training run with selected dataset, KB-size schedule, optimization flags and steps. Code samples QA, adds randomly sampled knowledge distractors, optionally truncates tokenized input to `max_seq_len`, computes weighted token cross-entropy and takes optimizer steps. Dataset answers supply the expected-token oracle. Gradient descent proposes numerical changes and the optimizer admits them on every step; human contribution is run configuration, not approval of each update. Optional separate query heads are included in the optimizer alongside encoder parameters. Distributed coordination uses Accelerate rank assignment, gradient machinery, metric gathering and a barrier before main-process saves, not delegated epistemic authority.

- Immediate return: updated in-process encoder/query-head parameters, training losses/logs and periodic checkpoint files; the trainer has no explicit product-return value.
- Later read-back: evaluation contains model/encoder reload wiring, but its unchanged CLI is blocked by the import failure in [RT-RTE-accuracy-generation](#rt-rte-accuracy-generation); resume code also attempts to reload model, encoder and KB config.
- Delegated visibility: accelerator processes participate in gradient computation and synchronization; no child-language-agent finding is returned to a parent.
- Selection predicate: first N dataset rows form training data; batch sampling, KB-size schedule and optional augmentation/outlier/multi-entity settings choose supervision and distractors; checkpoint period controls saves.
- Invalidation or expiry: selected output paths persist until externally replaced/deleted; checkpoint identity encodes step, not a semantic validity deadline.
- Activation or effect: optimizer updates parameters and saves artifacts for later consumers; successful later exercise and capacity improvement are unobserved.
- Evidence limits: save puts encoder in a sibling `_encoder` directory and config in `kb_config_explicit.json`, whereas resume looks for `encoder.pt` and `kb_config.json` under the model directory; external preparation is needed for that resume contract; no exact optimizer/scheduler-state restoration is established by this path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for _, param in model.named_parameters():  # type: ignore
>     param.requires_grad = False
> --- `experiments/train.py`

> self.accelerator.backward(loss)
> losses.append(loss.item())
> 
> self.optim.step()
> --- `experiments/train.py`

> encoder_ckpt_name = encoder_dir / "encoder.pt"
> torch.save(self.kbretriever.encoder.state_dict(), encoder_ckpt_name)
> --- `experiments/train.py`

Admission/rejection/recovery: configured AdamW steps admit gradient changes without a quality gate; the inspected save logic does not require validation improvement. Save exceptions are logged and re-raised. Earlier checkpoints can be selected manually if compatible, but the current save/resume naming mismatch blocks an automatic recovery guarantee. What persists is parameters/configuration, not formulated criticisms. This route does not expose a theory-revision procedure merely by using supervised errors. Learning objective is improved knowledge-conditioned answers; realized improved capacity, reflection and exercised self-improvement are not established by optimization wiring alone. In particular later use causally depending on a saved update is unobserved.

### Claims

#### RT-CLM-knowledge-augmentation
Label: Knowledge augmentation and linear overhead

Claimed operation (doctrine/design): external knowledge can ground answers without an external retrieval module, with overhead linear rather than quadratic in KB size. SRC-1, `README.md` supplies the claim. Attention wiring in [RT-RTE-kb-attention](#rt-rte-kb-attention) supports an implementation account, not measured complexity across deployments, accuracy or reliable factual grounding.

> Unlike Retrieval-Augmented Generation, KBLaM eliminates external
> retrieval modules, and unlike in-context learning, its computational overhead scales linearly with KB size rather than quadratically.
> --- `README.md`

The Llama dynamic top-k branch is a countercase to interpreting “no retrieval modules” as “no selection”: internal numerical row selection exists. It does not establish a separate external retrieval service. No benchmark or causal benefit is supplied.

#### RT-CLM-base-preservation
Label: No-knowledge base-model preservation

Claimed operation (doctrine/design), SRC-1, `README.md`: no knowledge should preserve base-model outputs.

> If given no knowledge base, the model outputs the exact same thing as the base model for any given input.
> --- `README.md`

Implementation supports the narrower claim that the KB concatenation/substitution branches are conditional on non-null tensors. Training normally freezes original model parameters and can train separate query heads. That does not prove bitwise output equality across differing loaders, tokenization, kernels, stochastic decoding or arbitrary direct callers. The structural bypass covers both inspected attention families; the processor's always-Llama formatting is an alternate-path qualification. No exact-output equivalence execution is supplied (SRC-1, `experiments/train.py`, `src/kblam/models/kblam_processor.py`, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py`).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-knowledge-attention
Label: External knowledge as numerical answer influence

Consumer: modified Llama/Phi attention. Channel: encoded keys/values, with optional separate query scores, concatenated with textual attention states. Force: numerical influence on logits, not an instruction-priority or factual-correctness guarantee. Horizon: current generation plus subsequent invocations that reload the same retained knowledge and encoder. SRC-1, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py`; minimum passages and limits are in [RT-RTE-kb-attention](#rt-rte-kb-attention). Delivery and computational wiring are established; actual answer dependence on specific knowledge is unobserved.

#### RT-BAP-checkpoint-consumption
Label: Trained parameters as later inference machinery

Consumer: `KBEncoder` and modified causal model loaded by evaluation. Channel: state-dictionary/pretrained file loading. Force: loaded numerical parameters determine projection and token computation; this is machinery, not advisory prose. Horizon: later processes selecting those artifacts, subject to shape/version compatibility and caller path choices. SRC-1, `experiments/train.py`, `experiments/eval.py`. Save and load wiring exist, but evaluation's unchanged CLI cannot reach loading until the import mismatch in [RT-RTE-accuracy-generation](#rt-rte-accuracy-generation) is repaired. The exact saved-to-resumed organization is also not guaranteed; [RT-RTE-adapter-training](#rt-rte-adapter-training) records the mismatch. This permits a dispositional parameter-change account, not an exercised self-improvement claim.

> encoder.load_state_dict(torch.load(encoder_path))
> return tokenizer, encoder, model, kb_config
> --- `experiments/eval.py`

## Annotations

none
