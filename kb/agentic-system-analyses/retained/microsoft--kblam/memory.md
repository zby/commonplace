---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "KBLaM memory: retained records, paired embeddings, trained checkpoints and evaluation artifacts, with numerical and textual context alternatives."
run-id: AAS-2026-10-15-kblam-5a0c2fe96cc1-01
source-identity: https://github.com/microsoft/KBLaM
reviewed-boundary: "69683ad096e022b58854fd88c0c58968c7d8c470"
---

# KBLaM memory report

## Boundary and evidence

KBLaM's memory boundary is its shipped research knowledge-production and consumption loop, not an agent's autobiographical memory. Included are retained entity/QA records; cached base embeddings; trained encoder/model parameters and configuration; inference context selection; prediction, attention and judgment artifacts; and authentication persistence. Current-generation KV state is described separately from cross-invocation read-back. External model/provider internals, unfrozen local assets and the unavailable synthetic LFS payload prevent operational reproduction and complete lineage verification. The whole-system scope and SRC-1 identity remain those of [boundary](boundary.md#boundary-and-evidence).

Evidence below is implementation at SRC-1's frozen commit unless explicitly attributed to a dataset card. Direct inspection extends the supplied runtime: all dataset scripts, data/train/evaluation utilities, encoder, processor, GPT client and scorer bodies; selected training/checkpoint/evaluation bodies; Llama pruning/cache/attention-saving bodies; Phi attention saving; configuration; package declaration; tracked entry-point inventory, Makefile command search and notebook cell sources. Notebook outputs were not used. Supplied runtime records remain provisional: one additional import defect and two cleanup surfaces are material additions. No target code, tests, providers or examples were executed.

| Entry point / operation | Source path in SRC-1 | Coverage and limit |
|---|---|---|
| Synthetic acquisition, reload, question perturbation and extension | `dataset_generation/gen_synthetic_data.py`; `src/kblam/utils/data_utils.py` | Direct reads; [MEM-OBJ-entity](#mem-obj-entity), [MEM-OBJ-data-point](#mem-obj-data-point); annotation on [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production). Typo blocks downstream CLI stages; no semantic verification inferred. |
| Offline key/value embedding writes and paired train/test slicing | `dataset_generation/generate_kb_embeddings.py`; `dataset_generation/create_train_test_split.py` | Direct reads; [MEM-OBJ-embd-key](#mem-obj-embd-key), [MEM-OBJ-embd-value](#mem-obj-embd-value). Row order is the join; historical correspondence remains unverified. |
| Training selection, augmentation, truncation, optimizer, checkpoint save/resume | `experiments/train.py`; `src/kblam/utils/train_utils.py` | Direct selected bodies plus supplied [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training); [MEM-OBJ-encoder](#mem-obj-encoder), [MEM-OBJ-kblam-config](#mem-obj-kblam-config). No exact resume or optimizer-state restoration established. |
| Evaluation dispatch: generation, accuracy, acc_results, refusal, standard | `experiments/eval.py` | Dispatch directly checked against supplied routes; selected bodies directly read. [MEM-OBJ-attention-weights](#mem-obj-attention-weights), [MEM-OBJ-eval-example](#mem-obj-eval-example), [MEM-RTE-result-cleanup](#mem-rte-result-cleanup). Missing `aug_row` import prevents treating the frozen CLI as executable unchanged. |
| Text/base-vector processor and direct tensor consumers | `src/kblam/models/kblam_processor.py`; `src/kblam/kb_encoder.py`; `src/kblam/utils/train_utils.py`; `src/kblam/utils/eval_utils.py` | Direct reads; annotations on [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference) and [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention). Public tensor/list layout compatibility is not established by the interface label. |
| Numerical context, dynamic sparsification, generation cache | `src/kblam/models/llama3_model.py`; `src/kblam/models/phi3_model.py`; `src/kblam/models/kblam_config.py` | Selected Llama and Phi bodies directly read; supplied runtime supplies insertion passages. Top-k is internal selection, not proof of relevance or a retained KB deletion. |
| Reference and open-ended judgment | `experiments/output_scorer.py`; `experiments/output_scorer_open_ended.py` | Both directly re-read for this correction; container [MEM-OBJ-eval-example](#mem-obj-eval-example), reference part [MEM-OBJ-reference-judgment](#mem-obj-reference-judgment) and open-ended part [MEM-OBJ-open-judgment](#mem-obj-open-judgment). Persistence timing, evaluator domains and rationale differ; normal open-ended completion returns None, preventing its CLI mean. No inspected inference consumer reads the reasons. |
| Batch caller, notebook and result conversion | `experiments/Makefile`; `eval_acc.ipynb`; `src/kblam/utils/convert.py` | Makefile commands searched, notebook code read as text, converter directly read. Notebook has stale imports/call arguments and destructive scratch cleanup; converter reads accuracy JSON and writes CSV, not KB state. |
| Shipped corpus and fixtures | `datasets/datasetcard_enron.md`; `datasets/datasetcard_synthetic.md`; `tests/test_dataset_construction.py`; `tests/test_kb_encoder.py` | Cards directly read; test loading/encoding paths searched; corpus/fixture coverage supplied by boundary. Enron upstream extraction is attributed provenance; synthetic payload unavailable. No corpus-wide correctness or test-pass claim. |
| Credentials and opaque provider state | `src/kblam/gpt_session.py` | Direct read; annotation on [RT-CMP-gpt-session](runtime.md#rt-cmp-gpt-session). Local access metadata is not semantic KB memory; provider retention is uninspected. |
| CLI / extension completeness check | `pyproject.toml`; tracked `src/`, `dataset_generation/`, `experiments/`, `tests/` inventory | Package declaration has no console-script table; actual script dispatch above is material. No additional hook/tool registration was identified in this inspected surface; no universal repository security or plugin-absence claim follows. |

## Core ideas

1. **Knowledge text and learned machinery are separate retained inputs.** Dataset rows supply key/description content; optional NumPy caches replace base encoding, not the trained projection. A later invocation combines selected row vectors with the currently loaded encoder and model. Editing text without rebuilding the cached pair need not change the numerical knowledge actually consumed. See [MEM-OBJ-data-point](#mem-obj-data-point), [MEM-OBJ-embd-key](#mem-obj-embd-key), [MEM-OBJ-embd-value](#mem-obj-embd-value) and [MEM-OBJ-encoder](#mem-obj-encoder).
2. **Selection has several different inputs and budgets.** Drivers select row indices and KB sizes; the textual alternative serializes selected content into tokens; Llama optionally further ranks numerical rows using current queries. Attention frequency and scale determine where/how much KB competes with text. Neither filename selection nor an attention weight certifies factual trust. These distinctions qualify the README's no-external-retrieval claim, already recorded in [RT-CLM-knowledge-augmentation](runtime.md#rt-clm-knowledge-augmentation).
3. **The write side admits plausible synthetic material, not established truth.** Model output parsing, template expansion, index slicing and optimizer steps are different admissions. Starting a script is not content approval. Cards identify synthetic GPT provenance and automated Enron extraction; neither establishes historical row-by-row lineage. Entity prompts ask for low name/content correlation. Extension declares an evidence-only system prompt, but the helper reads a different attribute, so that constraint is not established as delivered. Only returned text and fields persist. See [MEM-OBJ-entity](#mem-obj-entity), [MEM-OBJ-data-point](#mem-obj-data-point) and the dataset-production annotation.
4. **Evaluation retention is not automatically memory for answering.** Attention arrays feed metrics; prediction text feeds separate judgments; open-ended judgments can retain reasons. Accuracy sweep cleanup deletes raw evidence after deriving metrics. These consumers are distinct from model inference or checkpoint admission. See [MEM-OBJ-attention-weights](#mem-obj-attention-weights), [MEM-OBJ-eval-example](#mem-obj-eval-example) and [MEM-RTE-result-cleanup](#mem-rte-result-cleanup).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-entity
Label: Entity records

SRC-1, `src/kblam/utils/data_utils.py`, `dataset_generation/gen_synthetic_data.py`. Source-native `Entity` holds name, description, objectives and purpose. The values are natural-language content in symbolic JSON fields, retained as append-only linewise JSON by `save_entity`; this is the raw stage relative to derived QA, not a full provider-call trace. The producer parses GPT text into the dataclass; the script reloads existing raw files and skips generation. The later consumer is `post_process_data`, which expands three properties into data points. Its authority is input content for transformation, not a privileged instruction channel. It has no retained provider rationale, generating prompt, immutable model revision or per-record provenance field. Actual historical initialization of supplied corpora remains unresolved.

Closest supplied record is [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), a route rather than this retained object; no supplied operative-object counterpart exists. Dataclass construction accepts field presence, not semantic truth or runtime type enforcement. `save_entity` catches write exceptions, so an in-memory appended entity is not proof of successful persistence.

> entity = Entity(**json.loads(gpt_output))
> return entity
> --- `dataset_generation/gen_synthetic_data.py:185-187`

> with open(output_file, "a+") as f:
>     json.dump(pair.__dict__, f)
>     f.write("\n")
> --- `src/kblam/utils/data_utils.py`

#### MEM-OBJ-data-point
Label: DataPoint knowledge and supervision rows

SRC-1, `src/kblam/utils/data_utils.py`, `dataset_generation/gen_synthetic_data.py`, `experiments/train.py`, `src/kblam/utils/train_utils.py`. DataPoint content has distinct consumers: `key_string` and `description` are natural-language knowledge, while `Q`/`A` and optional `extended_Q`/`extended_A` are natural-language supervision/questions. Name and description type feed templates. Symbolic field names and row positions control extraction, sampling and joins; they are not separate semantic evidence. Substrate is JSONL for generator files, JSON arrays for shipped downstream readers, and Python dictionaries after reload. A compatible conversion is required between these formats.

Lineage: raw Entity properties become template questions, answers and keys; GPT can mutate questions and extend QA. Perturbation changes `Q` while leaving the knowledge key/description and answer unchanged; extension adds fields, not a separate authoritative KB replacement. Training can instead synthesize multi-entity/template QA in memory. These transformations differ from human editing; no per-item human review is implemented. Supplied synthetic rows' actual generating calls are unavailable, and the Enron card's extraction/entity-linking account is doctrine/design, not inspected upstream processing (SRC-1, `datasets/datasetcard_synthetic.md`, `datasets/datasetcard_enron.md`).

Later consumers: embedding creation reads keys/descriptions; uncached encoding projects those same fields; training interprets answers as token targets; evaluation uses questions and references, or serializes knowledge text into ICL. A row's text therefore has numerical influence after encoding, natural-language authority in ICL, and oracle authority at a training/metric consumer. None guarantees truth. Initial file choice/replacement is caller-controlled; author identity alone does not establish review. Existing raw/QA filenames suppress regeneration without comparing changed prompts or provider identities.

Closest supplied records are [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production), [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) and [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes); these are routes using this object, not duplicate object declarations.

> Q = "What is the {} of {}?".format(entity.description_type, entity.name)
> A = f"The {entity.description_type} of {entity.name} is {entity.description}."
> key_string = f"the {entity.description_type} of {entity.name}"
> --- `dataset_generation/gen_synthetic_data.py`

> data.Q = gpt_output
> --- `dataset_generation/gen_synthetic_data.py`

> if use_extended_qa:
>     Q, A = dataset[idx]["extended_Q"], dataset[idx]["extended_A"]
> --- `experiments/train.py`

#### MEM-OBJ-embd-key
Label: embd_key base-vector arrays

SRC-1, `dataset_generation/generate_kb_embeddings.py`, `dataset_generation/create_train_test_split.py`, `src/kblam/utils/train_utils.py`, `experiments/eval.py`. Dense distributed-parametric key representations persist in `.npy` files; NumPy/PyTorch arrays are the read substrate. The generator embeds `key_string` with a selected local sentence model or Azure embedding endpoint, then saves in dataset order. Model-family names in filenames are labels, not exact model revision or content checksums. Split copies the corresponding index slice; neither split nor later projection re-derives key provenance.

Later selector is driver-supplied row indices; the cached branch indexes key/value arrays and then applies the loaded encoder. These are base vectors, not already projected attention tensors. Actual consumer authority is numerical input to key projection/attention matching; not a textual instruction and not an independent truth assertion. No per-vector proposal/approval or quality filter intervenes; script execution authorizes the write as software admission. Caller-chosen paths and external assets leave historical initial curation unresolved. Persistence ends by external replacement/deletion; the inspected loaders do not automatically invalidate vectors after text changes. Evaluation checks dataset/key length, which does not establish content alignment or value-array equality.

Distinct part from [MEM-OBJ-embd-value](#mem-obj-embd-value): different source field, projector and attention role. Closest supplied route [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) groups creation of both, while [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder) is the transforming machinery, not these retained vectors.

> key_embeds.append(gpt.generate_embedding(entity.key_string))
> value_embeds.append(gpt.generate_embedding(entity.description))
> --- `dataset_generation/generate_kb_embeddings.py`

> precomputed_base_embd=np.stack([key_embds[indices], value_embds[indices]]),
> --- `src/kblam/utils/train_utils.py`

#### MEM-OBJ-embd-value
Label: embd_value base-vector arrays

SRC-1, `dataset_generation/generate_kb_embeddings.py`, `dataset_generation/create_train_test_split.py`, `src/kblam/utils/train_utils.py`, `src/kblam/kb_encoder.py`. Dense distributed-parametric description representations persist separately as `.npy`; read substrate is NumPy/PyTorch. Producer uses `description`, not `A`, `extended_A` or scorer reasons. The same software write admission, unresolved historical provider version and positional alignment limits as [MEM-OBJ-embd-key](#mem-obj-embd-key) apply, but a value vector supplies what is aggregated, rather than the key used to match queries. It is projected by `projector_v` without the key's layer normalization. Actual later consumer is model value aggregation after row selection; effect on answers is unobserved.

Closest supplied records: [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) and [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder); no supplied object counterpart. Numerical payload is not human-readable evidence; companion JSON can explain its intended content but the loader does not verify that explanation against the vector.

> return self.projector_v(base_embedding).bfloat16()
> --- `src/kblam/kb_encoder.py`

> np.save(
>     f"{args.output_path}/{args.dataset_name}_{save_name}_embd_value.npy",
>     np.array(value_embeds),
> )
> --- `dataset_generation/generate_kb_embeddings.py`

#### MEM-OBJ-encoder
Label: encoder.pt retained parameter state

SRC-1, `experiments/train.py`, `experiments/eval.py`, `src/kblam/models/kblam_processor.py`. A serialized PyTorch state dictionary is a retained distributed-parametric object, distinct from live [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder). Origin is current encoder state after supervised optimization; source does not establish the history or exact identity of externally supplied checkpoints. Periodic main-process save admits the current parameters without a validation-improvement threshold. File loading supplies later projection machinery, not advisory knowledge prose. Persisted weights do not carry formulated reasons, per-example criticisms or an invertible record of their training data.

Closest supplied records [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) and [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) establish production and authority. Saved encoder lives in a sibling `_encoder` directory; evaluation/processor accept explicit paths, while resume assumes `encoder.pt` under the model directory. Model checkpoint retention is covered by annotation on the model component rather than re-declared as an alias. Separate external query-head files have a loader, but their producer is not established by this inspected save path.

> encoder_ckpt_name = encoder_dir / "encoder.pt"
> torch.save(self.kbretriever.encoder.state_dict(), encoder_ckpt_name)
> --- `experiments/train.py`

#### MEM-OBJ-kblam-config
Label: KBLaMConfig and persisted KB configuration

SRC-1, `src/kblam/models/kblam_config.py`, `experiments/train.py`, `experiments/eval.py`. Symbolic Python/JSON configuration controls layer frequency, separate query head, numerical scale and optional sparsification budget. It is not knowledge content or a display summary of the model. Training constructs or reloads it and writes `kb_config_explicit.json`; resume asks for `kb_config.json`. Evaluation constructs its KB configuration from its own arguments, so saving a training configuration does not establish exact later reuse. Consumer authority is executable branch/shape/score control. Configuration authorship is launcher/code choice, not model-selected KB maintenance. Initial external file provenance is unresolved.

Closest supplied route [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) already records the save/resume mismatch; this object separates configuration from trained numerical weights and from [MEM-OBJ-encoder](#mem-obj-encoder).

> top_k_kb: int = 100,
> dynamic_sparsify: bool = False,
> sep_query_head: bool = False,
> --- `src/kblam/models/kblam_config.py`

> config_path = model_ckpt_name / "kb_config_explicit.json"
> with open(config_path, 'w') as f:
>     f.write(kb_config.to_json_string())
> --- `experiments/train.py`

#### MEM-OBJ-attention-weights
Label: attention weights and derived accuracy results

SRC-1, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py`, `experiments/eval.py`, `src/kblam/utils/convert.py`. Raw numerical attention snapshots are `.npy` arrays, not stored knowledge or token KV caches. Saving requires nongradient attention, enabled save flag and `q_len > 1`; they are not a complete per-token execution trace. Later accuracy code reloads snapshots, slices KB positions, sums scores and compares argmax/top-five against row-position labels. Derived accuracy arrays/JSON/CSV are symbolic quantitative reports. They lose individual answer evidence and are not warranted summaries of factual correctness. Selection/aggregation is code-owned; no human approval is required before result persistence.

Consumers are metric code and the fixed-path JSON-to-CSV converter, not later knowledge generation. Results may cross invocations for analysis even though snapshot reload inside `eval_accuracy` occurs within the same evaluator call. File basenames/layer indices control access but are not content-targeted retrieval. Sweep cleanup removes raw snapshots after deriving metrics; source wires no score-to-checkpoint admission. Closest supplied records [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation) and [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) are consumers/producers, not duplicate objects. See [MEM-RTE-result-cleanup](#mem-rte-result-cleanup) for lost evidence and aliasing limits.

> if not attn_weights.requires_grad:
>     # TODO: Make this function injectable
>     if save_attention_weights:
>         if q_len > 1:
> --- `src/kblam/models/llama3_model.py`

The metric passage is retained in [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation). The converter's later read is explicit:

> with open("/datadisk/kblam_attention_acc_results/accuracy_results.json", "r") as f:
>     results = json.load(f)
> --- `src/kblam/utils/convert.py`

#### MEM-OBJ-eval-example
Label: Exported answers and EvalExample judgments

SRC-1, `experiments/eval.py`, `experiments/output_scorer.py`, `experiments/output_scorer_open_ended.py`. This valid container covers exported natural-language answer traces in local text and their derived judgment records in memory/JSONL. It is not a uniform judgment schema. Its material judgment parts are separately declared as [MEM-OBJ-reference-judgment](#mem-obj-reference-judgment) and [MEM-OBJ-open-judgment](#mem-obj-open-judgment), with different domains, persistence timing and rationale. Original reference content is dataset-derived; open-ended evidence is supplied in the exported input, not independently acquired.

Later consumers: separate scorer invocations read exported text and transform it into the two judgment parts. The reference main block computes a mean after batch return and saving. The open-ended method returns None on normal completion, so its main block cannot normally compute the requested mean; a caught exception instead returns a partial list that may support a prefix mean. Per-record open-ended append occurs before that defect. No inspected route reloads saved judgments/reasons into KB attention, dataset revision or checkpoint selection. Neither score nor reason is an independent answer oracle. Both defaults use `GPT4`, outside the helper allowlist; no default execution or successful scoring is established.

Closest supplied record [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) covers the broad judgment route but explicitly leaves open-ended detail unassessed. This object is the retained result, not a new declaration of that route. Open-ended reasons are the important countercase to a claim that all judgment output discards rationale.

> class EvalExample:
>     evidence: str
>     question: str
>     response: str
>     score: float
>     reason: str
> --- `experiments/output_scorer_open_ended.py`

> except Exception as e:
>     print("Error evaluating example.")
>     print(e)
>     return eval_examples
> --- `experiments/output_scorer_open_ended.py`

#### MEM-OBJ-reference-judgment
Label: Reference-answer EvalExample judgment

Part of: [MEM-OBJ-eval-example](#mem-obj-eval-example)

SRC-1 implementation, `experiments/output_scorer.py`. The source-native `EvalExample` consists of natural-language `text` and `true_answer` plus a symbolic quantitative `score`. Substrate: an in-memory dataclass list, later appended as linewise JSON to the caller-selected output file by the main block after batch evaluation returns. It is a derived judgment of exported prediction/reference text, not the raw answer trace or an encoded KB vector. Exact historical provider identity and actual saved records are unavailable.

Its evaluator domain is agreement with the supplied reference, under user-prompt guidance requesting only a number between 0 and 1. GPT proposes the scalar; `float(score)` admits numeric output without a range or semantic-validity gate. A parsing/provider failure is caught per example and skipped, allowing later examples to continue. The launcher chooses files and service, not per-item approval; no human veto, quality-triggered replacement or automatic rollback is wired. The save helper catches I/O failures without removing the corresponding in-memory example. Repeated invocations append rather than invalidate prior results; no semantic expiry or provenance-based deduplication is implemented here.

The later main-block consumer saves the returned list and computes its mean for reporting. The saved JSONL has storage capability but no inspected subsequent reload into answering, dataset revision or checkpoint admission. Its authority is a reference-agreement assessment at the reporting consumer, not truth or deployment authority. No provider rationale is requested or stored; the retained reference and answer are comparison inputs, not reasons for the numeric judgment. No exercise, calibration or benefit is observed. The `GPT4` default is incompatible with the helper allowlist, as retained in [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes).

Distinct from [MEM-OBJ-open-judgment](#mem-obj-open-judgment): different fields, 0–1 reference-agreement guidance, post-batch persistence and no reason field. Closest supplied [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) is a route, not this retained part; the supplied peer [EPI-RTE-open-judgment](epistemic.md#epi-rte-open-judgment) concerns the other judgment operation, not this object.

> class EvalExample:
>     text: str
>     true_answer: str
>     score: float
> --- `experiments/output_scorer.py`

> score = self.generate_response(prompt)
> example = EvalExample(text, true_answer, float(score))
> return example
> --- `experiments/output_scorer.py`

> eval_examples = eval.evaluate_output_batch(examples)
> for example in eval_examples:
>     save_example(example, args.output_file)
> --- `experiments/output_scorer.py`

#### MEM-OBJ-open-judgment
Label: Open-ended EvalExample score and reason

Part of: [MEM-OBJ-eval-example](#mem-obj-eval-example)

SRC-1 implementation, `experiments/output_scorer_open_ended.py`. Source-native `EvalExample` retains natural-language evidence, question, response and reason, with a symbolic numeric score; the schema is quoted in the parent container. Substrate: in-memory dataclass list and linewise JSON appended during each successful loop iteration. Lineage is exported evidence/question/model-output text → provider rubric response → regex-extracted score/reason → dataclass/JSONL. The opaque provider response is not retained whole; the displayed reason is parsed model prose, not independently checked causal evidence or hidden model reasoning.

Its evaluator domain is evidence-relative accuracy/relevance and common-sense reasonableness of the open-ended answer, not exact reference agreement. The user prompt requests an integer 0–5 score and step-by-step explanation; regex plus float conversion, not an integer/range check, admits the score and matching reason. The subclass system message/seed is overwritten by parent initialization, while the substantive rubric remains in the user prompt, as established by supplied [EPI-RTE-open-judgment](epistemic.md#epi-rte-open-judgment). That supplied route also provides rubric and parse passages. A launcher supplies input/output paths and service configuration, not per-item approval. No human veto, factual-quality gate or rollback is wired. A caught evaluation exception stops the batch and returns accumulated examples; the save helper catches its own I/O failures, so list membership alone does not prove durable retention. Writes depend on the module-level `args.output_file`, limiting standalone library use without that state.

Each admitted record is appended before normal method completion, so its persistence does not depend on a successful aggregate mean. Normal completion returns None implicitly; the main block then attempts to iterate None for the mean. A caught failure can instead return a prefix list whose mean is attempted. The list's immediate reporting consumer is that main block; no inspected route subsequently reloads stored reasons into inference, knowledge revision or checkpoint selection. Reporting authority is an opaque provider's rubric judgment, not a truth oracle or successor-admission decision. Score and reason persist together for possible external inspection, without a shipped reason-consumption route. Repeated runs append, with no expiry, deduplication or withdrawal policy in this script. Actual judgments, range compliance, successful persistence, calibration and benefit remain unobserved; the default `GPT4` also fails the helper allowlist contract.

Distinct from [MEM-OBJ-reference-judgment](#mem-obj-reference-judgment): evidence/question/response inputs, 0–5 reasonableness guidance, per-record persistence and retained reason. Closest supplied [EPI-RTE-open-judgment](epistemic.md#epi-rte-open-judgment) is the producing operation, not a duplicate operative object. [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes) explicitly leaves its detailed rubric unassessed.

> eval_examples.append(eval_example)
>
> save_example(eval_example, args.output_file)
>
> except Exception as e:
>     print("Error evaluating example.")
>     print(e)
>     return eval_examples
> --- `experiments/output_scorer_open_ended.py`

Complete-file reinspection confirms that no normal-return statement follows this exception handler. Countercase: caught failure can return a prefix list, but does not establish completed batch reporting.

### Routes

#### MEM-RTE-result-cleanup
Label: Accuracy result derivation and scratch cleanup

Distinct lifecycle route overlapping [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation) and [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes): it governs retention/deletion after evaluation, not token generation or judgment. Endpoints are operator-launched `acc_results` → repeated `eval_accuracy` → in-memory accuracy summaries → raw attention-directory deletion/recreation → final JSON. Code owns the sweep and cleanup. Objective is bounded experiment reporting; row-position labels are the metric oracle. No model proposes deletion and no human per-directory veto is wired. `eval_acc.ipynb` also exposes a manually run shell cleanup cell; that independent notebook action is not proof that a sweep was run.

- Immediate return: per-size accuracy dictionaries accumulate in memory; final `accuracy_results.json` is written after the sweep; converter can turn such JSON into CSV.
- Later read-back: result JSON is read by the shipped converter; deleted snapshots cannot be reloaded without regeneration or external backup. The final JSON is not read into the KB by this route.
- Delegated visibility: inapplicable — local evaluation/filesystem operations and reporting, not delegated agents.
- Selection predicate: fixed KB-size list drives evaluation; every completed iteration removes the entire caller-selected attention directory, not just files produced by that iteration. Notebook cleanup separately targets a literal scratch glob.
- Invalidation or expiry: unconditional per-iteration directory removal/recreation replaces raw retention with reduced summaries; no age, semantic quality or dependency predicate controls it.
- Activation or effect: source calls destructive filesystem cleanup after metric derivation; actual deletion and subsequent reporting are unobserved.
- Evidence limits: frozen evaluator has an import defect; notebook has stale interfaces; no supplied run proves success. If output/log locations alias the attention directory, cleanup can also remove outputs or prior summaries. No path-separation validation or automatic rollback appears in the inspected sweep; final summary write occurs only after all iterations.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/recovery: launcher chooses the path, but code authorizes each deletion without content approval. The deleted material is not rejected knowledge or a withdrawn theory; it is raw experiment evidence. A failed later iteration can leave only in-memory earlier aggregates unless separately persisted. Regeneration or external copies, not an implemented trash/restore mechanism in this sweep, would be required for recovery (SRC-1, `experiments/eval.py`, `eval_acc.ipynb`, `src/kblam/utils/convert.py`).

> shutil.rmtree(args.attn_save_dir)
> os.mkdir(args.attn_save_dir)
> accuracy_results.append({"kb_size": x, "accuracy_results": accs})
> --- `experiments/eval.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production)

Write agency and admission differ by stage. Azure proposes Entity prose; JSON/dataclass construction rejects structural failures, not unsupported assertions. Code writes raw JSONL and can later reload it to skip generation. Template expansion derives QA from three properties; perturbation replaces only `Q`; extension adds `extended_Q`/`extended_A`. A shared in-memory dataset is mutated, so successful perturbation would also affect subsequent extension input; this is not a second independently curated corpus. CLI spelling `perturbe_names` prevents that downstream sequence unchanged. Guidance and parseability do not establish reviewed content. The extension method assigns its evidence-only guidance to `self.system_prompt`, but calls inherited `generate_response`, whose system message comes from `self.system_msg`. Those are different attributes; the default helper message is not changed by that assignment. The actual user prompt supplies the original QA and asks for an extended QA, but the stronger evidence-only constraint is not wired through that system-message path. Initial entity generation instead explicitly builds messages from `self.system_prompt`. This countercase prevents treating all declared generation guidance as delivered. The retained reasons for individual generated claims are uninspected; schema stores content, not prompts or critiques (SRC-1, `dataset_generation/gen_synthetic_data.py`, `src/kblam/utils/data_utils.py`).

> if os.path.exists(raw_output_file):
>     # skip entities creation if it's already generated
> --- `dataset_generation/gen_synthetic_data.py`

> Please ensure that the generated contents has **LOW** correlation with the name.
> --- `dataset_generation/gen_synthetic_data.py`

> self.system_prompt = """You are given a question and answer pair, please extend the question to be open-ended and generate a short answer.
> --- `dataset_generation/gen_synthetic_data.py`

> messages = [
>     {
>         "role": "system",
>         "content": self.system_msg,
>     },
> --- `src/kblam/gpt_session.py`

Embedding/split writes are software admissions chosen by launcher arguments: transform all loaded rows, persist key/value arrays separately, then slice records and both arrays at one index. No semantic rejection gate, multi-file transaction or provenance manifest is established by the inspected bodies. Content replacement is possible by editing/replacing inputs, but existing-file skip and cached-array branches mean that editing alone is not a universal read-back mechanism. Exception handling can skip generation/augmentation items; it does not roll back already appended records or prove cross-file completeness. See [MEM-OBJ-data-point](#mem-obj-data-point), [MEM-OBJ-embd-key](#mem-obj-embd-key) and [MEM-OBJ-embd-value](#mem-obj-embd-value).

#### On [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training)

The retained behavior-shaping result is parameter state and configuration, not the printed/logged prediction trace. Dataset answers, optional extended answers and code-composed targets feed loss; logits/labels feed gradients; `optim.step` changes current parameters; checkpoint save retains them for explicit later loading. This is a supervised error-to-parameter transformation, not an inspected cross-session conversational trace-learning loop. Logs and sampled decoded predictions are separate outputs, not inputs to the inspected optimizer. No checkpoint-quality gate, human per-update approval or rollback-on-bad-score is wired in the inspected save path. External selection of an older checkpoint is an afforded recovery action, subject to the already recorded layout mismatch (SRC-1, `experiments/train.py`).

Working-context control is code-owned: first N dataset rows limit training material; selected QA plus randomly sampled distractor rows become KB tensors. The KB-size schedule controls distractor count, not text-token count. Optional `max_seq_len` keeps the leading slice of input IDs, masks and labels, discarding the tail rather than making a reloadable summary. Dataset files remain reachable for later sampling; there is no automatic reattachment of a truncated tail in this training path. This is filtering and prefix retention, not a sub-agent frame. It can remove answer supervision as well as question text (SRC-1, `experiments/train.py`, `src/kblam/utils/train_utils.py`).

> input_ids = input_ids[:, : self.max_seq_len]
> attention_masks = attention_masks[:, : self.max_seq_len]
> labels = labels[:, : self.max_seq_len]
> --- `experiments/train.py`

The source comment about outliers overstates exclusion: the code independently resamples indices, rather than checking disjointness from question indices. This preserves an implemented refusal-training proposal but prevents a guaranteed missing-answer label interpretation. It is not an additional retained-store route.

> # Generate a new set of indices, such that the KB does not contain the entity where the question comes from
> batch_indices = np.random.choice(len(dataset), B, replace=False)
> --- `experiments/train.py`

#### On [RT-CMP-llama3-model](runtime.md#rt-cmp-llama3-model)

Training persists the unwrapped model with `save_pretrained`; this is parameter machinery spanning later processes, not a text memory file. Selected query-head updates can therefore survive separately from [MEM-OBJ-encoder](#mem-obj-encoder). Explicit `load_query_head` accepts an alternative external state dictionary keyed by layer and sets separate-head mode. Its inspected loader does not establish how that external file was produced or whether it matches the encoder/dataset. Exact external checkpoint history remains uninspected (SRC-1, `experiments/train.py`, `src/kblam/models/llama3_model.py`).

> learned_query_heads = torch.load(ckpt_dir)
> assert len(learned_query_heads) == self.model.config.num_hidden_layers
> --- `src/kblam/models/llama3_model.py`

#### On [RT-CMP-phi3-model](runtime.md#rt-cmp-phi3-model)

The shared training driver persists the selected Phi model through the same unwrapped-model save path, while encoder and KB configuration are separately retained. Saved parameter lineage and caller-selected reload have the same unresolved external provenance limit; Phi's attention-save branch also emits raw snapshots, not derived knowledge. These objects must not be collapsed into its text-generation cache (SRC-1, `experiments/train.py`, `src/kblam/models/phi3_model.py`; [MEM-OBJ-attention-weights](#mem-obj-attention-weights)).

#### On [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention)

Read-back context arrives through caller-selected tensors; the model does not autonomously fetch a named document. Driver row selection precedes projection; Llama's optional sparsification then uses current queries and per-row dot-product scores summed over heads/query positions, keeping top-k keys/values. This reduces currently visible numerical KB rows, not durable corpus membership. Removed rows remain in supplied original tensors/files for another call; no pointer token or summary represents them in the text window. Default sparsification is false and configured top-k is 100; actual budgets are caller-configurable. The supplied score-slicing defect prevents asserting correct score/value alignment under pruning. Phi is a distinct consumer without this pruning branch in the supplied inspected path (SRC-1, `src/kblam/models/kblam_config.py`, `src/kblam/models/llama3_model.py`, `src/kblam/models/phi3_model.py`).

Layer frequency controls insertion; optional `kb_scale_factor` adjusts KB scores by log KB length/scale before joint attention normalization. Thus a large numerical KB is not cost-free context or a token-budget exemption for the textual alternative. Authority is weighted numerical influence, as [RT-BAP-knowledge-attention](runtime.md#rt-bap-knowledge-attention) records; actual answer activation remains unobserved.

#### On [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation)

Retained inputs are dataset/arrays/checkpoints; row-index selection delivers only the chosen numerical rows. Output attention snapshots feed position-label metrics, while decoded answer files are a separate trace. The generation cache is invocation working state, not automatically persisted knowledge. Llama preparation discards already processed input IDs because prior text is represented in cache, conditionally crops the attention mask at cache capacity, and carries the same KB inputs forward. This is not a summary and establishes no cross-invocation reload of generated text (SRC-1, `experiments/eval.py`, `src/kblam/models/llama3_model.py`).

> "past_key_values": past_key_values,
> "use_cache": use_cache,
> "attention_mask": attention_mask,
> "kb_kvs": kb_kvs,
> "kb_config": kb_config,
> --- `src/kblam/models/llama3_model.py`

There is an additional source-level entry failure beyond the supplied wrapper defects: `experiments/eval.py` imports `aug_row`, but the fully inspected data utility defines `augment_row` and no `aug_row`. This prevents claiming unchanged CLI reachability even for accuracy. Branch-level persistence/read-back wiring remains inspectable, but operation is uninspected, not working by implication.

> from kblam.utils.data_utils import aug_row, generate_multi_entity_qa
> --- `experiments/eval.py`

> def augment_row(row: dict[str, str]) -> list[dict[str, str]]:
> --- `src/kblam/utils/data_utils.py`

#### On [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes)

The textual alternative serializes `key_string is description;` pairs and instructions into token context; zeroshot omits knowledge content. Numerical KB projection is computed earlier in `perform_eval` even for text/zeroshot branches, but only `kb` passes those tensors to answering. Optional `remove_sorry` discards matching outputs before appending both metric predictions and exported pairs, so these files need not preserve every attempted answer. Refusal scoring similarly classifies the substring, not a source-verified knowledge withdrawal. These controls change experiment visibility, not retained KB membership (SRC-1, `experiments/eval.py`, `src/kblam/utils/eval_utils.py`).

> if remove_sorry:
>     if "sorry" in model_output:
>         continue
> full_outputs.append((model_output, answer))
> --- `experiments/eval.py`

Open-ended scoring explicitly requests reasons and persists their parsed display text alongside score/evidence/question/response; this differs from a bare scalar reference judgment. Its rubric is natural-language guidance to an opaque provider, not symbolic proof or guaranteed compliance. Neither scorer result is wired to select a successor model in the inspected routines. See [MEM-OBJ-open-judgment](#mem-obj-open-judgment) for the reason-bearing part, its per-record append timing and normal-return defect, and [MEM-OBJ-reference-judgment](#mem-obj-reference-judgment) for the scalar-only post-batch persistence path.

#### On [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference)

Caller-selected text pairs or base embeddings bypass disk knowledge acquisition; model calls may bypass the processor entirely. Encoder checkpoint reload is explicit, whereas projecting supplied material is not itself a persistent write. The processor tests a list's first pair to select text versus tensor encoding. Its tensor-list surface does not establish compatible input layout: `encode_base_embeddings` iterates `zip(kb[0], kb[1])`, while `encode_key`/`encode_val` use `torch.from_numpy` for the base input. This adds a type/layout limit to the supplied defective convenience-loader connection; no successful processor tensor run is established (SRC-1, `src/kblam/models/kblam_processor.py`, `src/kblam/kb_encoder.py`).

> for key, value in zip(kb[0], kb[1]):
> --- `src/kblam/kb_encoder.py`

#### On [RT-CMP-gpt-session](runtime.md#rt-cmp-gpt-session)

Local retained authentication data is symbolic access metadata: `auth_record.json` and an Azure credential cache under a home/LOCALAPPDATA-rooted location. Credential code creates the directory/record after authentication or reloads an existing record, then supplies bearer authentication to later chat/embedding calls. Software writes/reloads it; the user's authentication action is not approval of generated knowledge. Its authority is service access, not answer content. The cache explicitly permits unencrypted storage. Exact tokens, granted permissions, expiry, host protection and provider-side retention/deletion policies remain uninspected. Message lists are constructed for calls; their presence in the client does not establish provider conversational memory (SRC-1, `src/kblam/gpt_session.py`).

> cache_options = TokenCachePersistenceOptions(
>     name=f"{lib_name}.cache", allow_unencrypted_storage=True
> )
> --- `src/kblam/gpt_session.py`

## Write side

The concrete write mechanisms are separated by admission control, not grouped under the word "learning":

| Mechanism | Proposer / physical writer | Admission and rejection / replacement | Retained result and later consumer |
|---|---|---|---|
| Entity creation / related people | GPT proposes; generator and save helper write | JSON/dataclass parsing; caught generation exceptions skip items; save failures print rather than guarantee commit. Launcher supplies configuration, not per-content approval. | Raw [MEM-OBJ-entity](#mem-obj-entity) → reload / QA derivation. |
| QA templates, perturbation and extension | Code templates or GPT; generator writes | Existing-file skips or regex extraction / assignment, not truth review; failed augmentation continues. Caller may replace files; typo blocks unchanged CLI progression. | [MEM-OBJ-data-point](#mem-obj-data-point) → encoding, supervision, questions/references. |
| Base embedding / train-test split | Local or Azure encoder computes; scripts save | Whole loaded inputs transformed or index-sliced; no per-row quality veto or verified multi-file atomicity. Initial corpus curation remains unresolved. | Separate key/value arrays → selected projection; partitioned JSON → training/evaluation. |
| Supervised parameter update / checkpoint | Gradient computation proposes; optimizer/save admits | Every configured step updates; save period, not validation success, controls retention. Exceptions re-raise; manual older-path selection is not automatic rollback. | Parameters/config → later model and encoder loads, subject to layout compatibility. |
| Experiment outputs / judgments | Model, metric code or GPT proposes; drivers append/overwrite | Parsing, regex and numeric conversion gate scores; substring omission changes exported population. No judgment-to-KB admission established. | Raw and derived [MEM-OBJ-attention-weights](#mem-obj-attention-weights), [MEM-OBJ-eval-example](#mem-obj-eval-example) → metrics/scorers/converter. |
| Scratch cleanup | Sweep code, or operator-running notebook cell | Whole selected directory/glob; not item quality rejection; no implemented restore in inspected cleanup. | Reduced metrics survive only if separately retained; raw arrays can disappear. |
| Authentication persistence | User authenticates; client serializes access record | Credential existence/load/authentication controls service access, not content validity. | Access metadata → later Azure client requests. |

Sources and minimum passages reside in the corresponding objects, route and annotations. The distinction between known transformations and unknown historical initialization is important: inability to authenticate a supplied checkpoint/corpus history does not erase the inspected generator, projection or save mechanisms.

The trace-to-derived chains have different horizons. Provider response → Entity/QA is synthetic content construction, not learning from KBLaM's own past answers. Supervised token prediction/error → gradient → retained parameters → later loaded inference machinery is implemented, but no actual later answer dependence or improvement was observed. Evaluation answers → scores/reasons or attention → metrics are retained analysis chains; the inspected consumers do not turn those results into revised knowledge or selected checkpoints. The open-ended reason field is a rationale-bearing result, but no later inference reader for that reason is established. Ordinary text KV caches and truncation do not create alternative durable checkpoint summaries. Checkpoint files preserve numerical state/configuration rather than formulated criticism. See [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training), [MEM-OBJ-encoder](#mem-obj-encoder) and [MEM-OBJ-eval-example](#mem-obj-eval-example).

## Read-back

Read-back is primarily request-driven by experiment configuration. There is no need to posit an unsolicited memory injector: scripts load paths, select row indices and explicitly pass context. These are source-wired delivery mechanisms, not observed activations.

| Retained input → later consumer | Trigger, selector and delivery | Budget, authority and limits |
|---|---|---|
| Raw/QA files → resumed generator stages | Existing named paths cause JSONL reload rather than regeneration | Whole file, no semantic change detection; raw data controls derived QA, QA controls extension input. |
| JSON plus optional paired arrays → training/evaluation encoder | Caller-selected paths; driver-selected row indices; `get_kb_embd` indexes arrays or extracts text | Full/subset/random and schedule-dependent rows, not semantic search. Both arrays present selects cached route. Identity/length checks do not verify text-vector lineage. |
| Selected projected rows → Llama/Phi attention | `kb_kvs`, configured insertion layers; optional Llama current-query top-k | Numerical influence, not privileged truth; layer frequency, scale and sparsification are separate controls. Pruning changes current context but leaves the corpus reachable. |
| Selected knowledge prose → ICL | Mode flag constructs literal key/value sentences plus instruction and question | Occupies text context; no inspected explicit pre-budget truncation in `perform_eval`. Actual tokenizer/model limits are external contracts. Zeroshot excludes knowledge by mode. |
| Parameter/config files → later inference or resume | Explicit checkpoint paths and load calls | Machinery authority, not knowledge assertions; external version/history, path mismatch and separately constructed eval configuration limit equivalence. |
| Attention snapshots → metric code; summary JSON → converter | File/layer naming and fixed-path JSON read | Numerical ranking/reporting, not truth checking. Same-call snapshot reload is not by itself later invocation memory; separate converter is a later consumer. |
| Prediction/reference text → GPT scorer | Operator selects prediction file; code parses fields and sends prose | Opaque model judgment; open-ended reasons can persist. No inspected score/reason-to-answering read-back. |
| Authentication record/cache → GPT client | Subsequent client initialization reuses local record and SDK cache | Access authority only; provider retained state and actual expiry are unresolved. |

The source-native working-context mechanisms are row selection, optional numerical pruning, textual inclusion/exclusion, training prefix truncation and generation-cache input/mask handling. None is an inspected sub-agent isolation/return mechanism. The stack-frame analogy therefore adds little: there is no child context whose returned finding alone escapes. Nor are omitted KB rows token-window references: the original tensors/files remain host-managed inputs that code must select and supply again. Numerical KB context is consumed outside the ordinary text-token sequence; this does not make knowledge immune to budgets, competing attention or stale retained inputs. Source evidence and routes are in the annotations on [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention), [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation), [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) and [RT-RTE-evaluation-modes](runtime.md#rt-rte-evaluation-modes).

## Integration issues

1. **Frozen CLI blocker now carried by supplied runtime.** The supplied runtime treats accuracy as the ordinary source-level invocation and now explicitly records its failing `aug_row` import; this resolves the previous report's requested runtime correction. SRC-1, `experiments/eval.py` imports that name; the fully inspected `src/kblam/utils/data_utils.py` provides `augment_row` only. Correct reachability qualifications for [RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation) and all evaluation dispatch paths. Internal branch wiring remains valid evidence; unchanged end-to-end executability does not. The supporting passages are in that route's annotation.
2. **Cleanup adds a destructive retained-result path.** [MEM-RTE-result-cleanup](#mem-rte-result-cleanup) is distinct from the supplied generation/evaluation routes but spans their outputs; it is not a duplicate route. SRC-1, `experiments/eval.py` removes the attention directory after deriving accuracy. `eval_acc.ipynb` also contains a manually runnable destructive scratch cell. Reconciliation must not describe raw attention as indefinitely retained, and must retain output/log-directory aliasing and final-write failure limits for [MEM-OBJ-attention-weights](#mem-obj-attention-weights).
3. **Outlier membership is not guaranteed by independent resampling.** The training source comment says correct KB entities are excluded, but its code does not enforce disjointness. This limits any refusal-target interpretation of [RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training); it does not negate the wired gradient/checkpoint route. SRC-1, `experiments/train.py`, passage in annotation.
4. **Processor base-vector input remains an unresolved compatibility surface.** The processor accepts a list selected by tensor type, while encoder code consumes a key/value-array layout and converts base entries through NumPy. [RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference) should preserve this limit in addition to its constructor defect. No target execution was authorized; compatible external conversions are not supplied. This prevents a universal working public-processor claim, not direct compatible tensor attention.
5. **Lineage/invalidation questions remain local.** [MEM-OBJ-embd-key](#mem-obj-embd-key), [MEM-OBJ-embd-value](#mem-obj-embd-value) and [MEM-OBJ-data-point](#mem-obj-data-point) lack verified historical alignment/model revision; source joins by position. The JSONL/array boundary and generator typo already in [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) prevent turnkey-pipeline claims. [MEM-OBJ-encoder](#mem-obj-encoder) and [MEM-OBJ-kblam-config](#mem-obj-kblam-config) expose separately retained parts of the existing checkpoint route, not aliases for [RT-CMP-kb-encoder](runtime.md#rt-cmp-kb-encoder). External query-head producer/history is unresolved. Provider retained state/expiry is uninspected in [RT-CMP-gpt-session](runtime.md#rt-cmp-gpt-session). These unknowns prevent exact reconstruction and freshness guarantees, not the supported transformations.
6. **Declared extension guidance is not all delivered.** The supplied [RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production) describes evidence-only QA guidance, but `augmenta_data_with_synthetic_QA` stores it in `system_prompt` while inherited `generate_response` reads `system_msg` (SRC-1, `dataset_generation/gen_synthetic_data.py`, `src/kblam/gpt_session.py`). Preserve it as declared intent, not a wired constraint on extended answers. Supporting passages are in the dataset-production annotation; the consequence concerns [MEM-OBJ-data-point](#mem-obj-data-point)'s derivation trust, not whether software can store returned fields.
7. **No new declaration is a possible duplicate after comparison with supplied runtime.** Runtime declares no operative objects; this member separates retained artifacts from its components/routes. [MEM-RTE-result-cleanup](#mem-rte-result-cleanup) has distinct deletion/reporting progression. A peer analyst could independently declare the same dataset, checkpoint or judgment referent; no peer records were supplied to establish identity now. The newly supplied peer [EPI-RTE-open-judgment](epistemic.md#epi-rte-open-judgment) is a producing route, not a duplicate object. The valid [MEM-OBJ-eval-example](#mem-obj-eval-example) container is preserved; [MEM-OBJ-reference-judgment](#mem-obj-reference-judgment) and [MEM-OBJ-open-judgment](#mem-obj-open-judgment) now supply the previously missing operative comparison units. They separate evaluator domains, admission, persistence timing, authority and rationale. Open-ended per-record retention remains wired despite its normal-return defect; completed aggregate reporting must not be inferred.

## Limitations and checks

The source HEAD was rechecked as `69683ad096e022b58854fd88c0c58968c7d8c470`; the Commonplace method checkout HEAD was `26c5bf9df8ca39166fd6bdc39476689dad437cb5`. Runtime identity was read from PI environment variables and recorded separately. Source analysis used only SRC-1 and supplied members. No agents were launched and no target execution, downloads, model calls or dependency installation occurred.

The boundary's missing synthetic payload, external weights/embeddings/checkpoints and upstream Enron extraction constrain historical lineage and operation. Available but uninspected internals are not access gaps or evidenced absences. Provider/model opacity cannot prove absent learning or retention. No improved grounding, exercised capacity improvement, automatic score-driven successor adoption or causal self-improvement is established by the source-only retained chains. Numerical parameter updates, rationale-bearing open-ended judgments and actual source-wired read-back mechanisms remain positive findings with their own limits.

For this correction, both complete scorer files were directly re-read at the rechecked source HEAD, with the supplied refusal and previous report as the baseline. The correction preserves prior IDs and separates the judgment parts rather than treating a prose schema caveat as part-level coverage.

Validation: the invocation-specific `commonplace-run validate-output` check passed (exit 0: "Member content check passes; invocation residue not checked"). This establishes checked form and quotation occurrence, not semantic correctness or job acceptance.
