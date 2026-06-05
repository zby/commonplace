---
description: "KBLaM review: model-integrated key/value knowledge injection with trained encoders, modified attention, and KB-conditioned generation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# KBLaM

KBLaM, from Microsoft, is a research implementation of Knowledge Base Augmented Language Models. It does not build an autonomous memory agent or an external retrieval service. Instead, it trains a KB encoder that maps key/value records into tensors shaped for supported Llama and Phi-3 attention layers, then lets the modified model attend over those tensors during generation.

**Repository:** https://github.com/microsoft/KBLaM

**Reviewed commit:** [4db377fa4dad2134a38fbc06f80938e66b9b5897](https://github.com/microsoft/KBLaM/commit/4db377fa4dad2134a38fbc06f80938e66b9b5897)

**Source directory:** `related-systems/microsoft--KBLaM`

## Core Ideas

**The knowledge base is key/value memory transformed into model attention state.** `KBEncoder` embeds keys and values with either SentenceTransformers or Azure OpenAI embeddings, projects them through separate key/value projectors, and returns stacked key/value tensors. The modified Llama and Phi-3 attention modules accept those tensors as `kb_kvs`, reshape them by KB layer frequency, and concatenate KB keys and values into the model's attention key/value states ([src/kblam/kb_encoder.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/kb_encoder.py), [src/kblam/models/llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py), [src/kblam/models/phi3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/phi3_model.py)).

**The base LLM is mostly a host for trained adapters.** Training freezes the loaded language model, trains the KB encoder parameters, and optionally trains a separate query head for KB attention. Checkpoints save the wrapped model, encoder state dict, and KB configuration, so the durable learned behavior is in model/encoder weights rather than in a mutable note-like memory store ([experiments/train.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/train.py), [src/kblam/models/kblam_config.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_config.py)).

**Context efficiency is architectural injection rather than prompt compression.** KBLaM avoids putting every KB record into the text prompt. KB entries become attention key/value tensors, are inserted only at layers whose index matches `kb_layer_frequency`, and in the Llama path can be pruned at test time with `dynamic_sparsify` and `top_k_kb`. Complexity is still tied to KB tensor count and model attention behavior, but it is not quadratic prompt-token growth from in-context examples ([README.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/README.md), [src/kblam/models/kblam_config.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_config.py), [src/kblam/models/llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py)).

**Data construction is synthetic and document-like, not trace learning.** The included generator asks an Azure OpenAI-backed model to create entities, descriptions, objectives, purposes, and QA pairs, then writes JSON lines. The training and evaluation scripts consume JSON datasets and optional cached `.npy` embeddings. I did not find code that derives durable behavior-shaping artifacts from agent sessions, tool traces, event streams, or trajectories ([dataset_generation/gen_synthetic_data.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/dataset_generation/gen_synthetic_data.py), [dataset_generation/generate_kb_embeddings.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/dataset_generation/generate_kb_embeddings.py), [src/kblam/utils/data_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/data_utils.py)).

**The public integration surface is library and experiment code.** `load_model_and_processor` builds a model plus processor, `answer_question` passes `kb` into `model.generate`, and evaluation scripts compare KB-conditioned, in-context, and zero-shot modes. There is no MCP server, provider hook, scheduler, session recorder, or deployed agent loop in the inspected code ([src/kblam/utils/model_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/model_utils.py), [src/kblam/utils/eval_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/eval_utils.py), [experiments/eval.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/eval.py)).

## Artifact analysis

- **Storage substrate:** `files` — KBLaM's durable artifacts are filesystem-backed: JSON datasets, cached `.npy` base embeddings, Hugging Face/PyTorch model checkpoints, encoder `encoder.pt` files, explicit KB config JSON, and optional attention-weight `.npy` outputs.
- **Representational form:** `prose` `symbolic` `parametric` — KB values and generated QA text are prose; dataset schemas, key strings, config values, layer-frequency rules, command arguments, and checkpoint paths are symbolic; sentence embeddings, projected KB tensors, trained encoder/query-head weights, and attention scores are parametric.
- **Lineage:** `authored` `imported` — The model wrappers, configs, prompts, and experiment code are authored; KB records can be imported caller data or synthetic generated records. The learned encoder and optional query heads derive from those imported/generated datasets, not from agent traces.
- **Behavioral authority:** `knowledge` `routing` `ranking` `learning` — KB values provide knowledge to the model; `kb_layer_frequency`, `kb_scale_factor`, `sep_query_head`, and generation arguments route how KB tensors enter computation; attention and optional dynamic sparsification rank which KB tensors affect decoding; training updates encoder/query-head weights as learning artifacts.

**KB records and cached embeddings.** The dataset path stores records with names, description types, descriptions, questions, answers, and key strings. Cached embedding generation writes separate key/value arrays, and the train/eval retrievers either load those arrays or compute embeddings from the dataset on demand ([src/kblam/utils/data_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/data_utils.py), [dataset_generation/generate_kb_embeddings.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/dataset_generation/generate_kb_embeddings.py), [experiments/train.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/train.py), [experiments/eval.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/eval.py)).

**KB encoder and special tokens.** `KBEncoder` is the central promotion mechanism from prose/symbolic KB records into parametric tensors. It owns the key/value projectors, an optional frozen base sentence model, Azure OpenAI embedding support, layer normalization for keys, and special KB token embeddings ([src/kblam/kb_encoder.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/kb_encoder.py), [tests/test_kb_encoder.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/tests/test_kb_encoder.py)).

**Modified model attention.** The Llama and Phi-3 wrappers are system-definition artifacts: they decide where KB tensors enter attention, how masks expand to include KB length, whether a separate KB query head is used, and whether test-time sparsification selects top KB vectors before concatenation. That is stronger than retrieved context text because the KB state directly changes model computation ([src/kblam/models/llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py), [src/kblam/models/phi3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/phi3_model.py)).

**Evaluation and attention outputs.** Evaluation artifacts are evidence surfaces rather than runtime memory. The code can write generated outputs, metric JSON, refusal arrays, and attention tensors, which help inspect whether KB conditioning changes behavior, but those artifacts are not fed back into a later agent policy in the inspected repository ([experiments/eval.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/eval.py), [src/kblam/utils/eval_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/eval_utils.py)).

**Promotion path.** KBLaM promotes records from JSON prose and key strings into base embeddings, projected KB key/value tensors, trained encoder weights, and optionally separate query-head weights. The path increases computational authority but decreases direct inspectability: after training, the decisive adaptation is parametric and must be tested rather than read.

## Comparison with Our System

| Dimension | KBLaM | Commonplace |
|---|---|---|
| Primary purpose | Research method for injecting KB key/value tensors into LLM attention | Agent-operated methodology KB with typed durable Markdown artifacts |
| Canonical memory | Imported/generated records plus encoder/model checkpoints | Git-tracked notes, reviews, instructions, ADRs, sources, indexes, and validation reports |
| Write path | Dataset generation/import, embedding generation, encoder/query-head training, checkpoint save | Human/agent-authored Markdown under collection contracts, validation, review, and git history |
| Read-back | Host passes `kb_kvs` into generation; model attends over KB tensors | Agents pull notes, indexes, links, sources, reports, and instructions into bounded context |
| Governance | Benchmark metrics, refusal tests, attention inspection, and unit tests | Schema validation, collection routing, source discipline, semantic review, and replacement lifecycle |

KBLaM is almost the opposite of Commonplace's text-governed design. Commonplace keeps the authoritative artifact readable and reviewable, then relies on context routing to expose it to an agent. KBLaM makes the behavior-shaping memory parametric, then uses evaluation to ask whether the model learned to use it. That gives KBLaM a strong path for compact model-side recall, but it does not provide Commonplace-style auditability, explicit invalidation, link semantics, or per-claim review.

The useful comparison is not "RAG versus KB." It is "retrieval-readable memory versus model-integrated memory." KBLaM shows a way to avoid prompt-token expansion by turning records into attention state, but the price is that the memory's effective authority is only observable through generated behavior, metrics, and attention probes.

### Borrowable Ideas

**Treat model-integrated memory as a separate authority tier.** Ready now as a taxonomy rule. Commonplace should classify fine-tuned/adapted memory as parametric learning authority, not as equivalent to reviewed prose, even when both originate from the same source documents.

**Use attention probes as diagnostic evidence, not acceptance gates.** Ready with a concrete evaluation use case. KBLaM's attention-weight saving suggests a useful diagnostic for "did the model look at the retained artifact," but Commonplace should not equate attention with faithful use.

**Keep readable source artifacts beside any parametric projection.** Ready now. If Commonplace experiments with embeddings, adapters, or retrieval models, the reviewed Markdown/source artifact should remain the source of truth and the parametric layer should be regenerable.

**Borrow the separation between base model and memory adapter cautiously.** Needs a concrete use case. Training only the encoder/query head while freezing the base model is attractive for controlled adaptation, but Commonplace's current artifacts are better served by explicit review and validation than by model-weight updates.

**Do not borrow KB injection as an agent loop.** Ready now as a boundary. KBLaM affords host-side push into generation, but it does not decide when an agent should retrieve, remember, invalidate, or act on memory.

## Write side

**Write agency:** `manual` `automatic` — Humans or upstream processes supply/import KB records and choose datasets, while scripts automatically generate synthetic records, compute cached embeddings, train encoder/query-head parameters, and save model/config/encoder checkpoints.

**Curation operations:** `none` — I found automatic acquisition, embedding, training, checkpointing, and evaluation, but not implemented consolidation, deduplication, evolution, synthesis, invalidation, decay, or promotion over memory already in the store. KB tensors can be selected or pruned at read time, but that is ranking/access behavior rather than store-changing curation.

## Read-back

**Read-back:** `push` — KBLaM is a library/model capability rather than a deployed agent loop, but once a host passes `kb_kvs` into `model.generate` or `forward`, the retained KB tensors are inserted into attention without the model issuing a separate retrieval call.

**Read-back signal:** `coarse` `inferred / embedding` — The basic path pushes the supplied KB tensor set into every eligible KB attention layer. The Llama path also supports `dynamic_sparsify`, which uses query-to-KB attention scores over vector states to keep top KB entries before concatenation.

**Faithfulness tested:** `yes` — The experiment code includes KB, in-context, and zero-shot evaluation modes plus refusal tests and attention-weight capture. That is an experiment-level with/without and inspection surface for KB conditioning, not evidence of a deployed autonomous agent faithfully obeying pushed memory in real tasks.

The push classification is intentionally scoped to the model invocation. I did not find a scheduler, event hook, MCP/tool wrapper, or session-start injector that decides when to feed memory to an agent. A host application could pass a curated KB for every user turn, pass a selected KB subset, or pass no KB at all; those deployment choices are outside the repository's inspected loop.

Context selection is partly host-controlled and partly model-internal. The host chooses the KB records or indices, `KBRetriever` turns them into key/value tensors, and the model attends over the supplied tensors. With `dynamic_sparsify`, the Llama attention module prunes by top attention score at inference time, but the code does not turn that score into a durable retrieval explanation or source-level citation.

## Curiosity Pass

**KBLaM removes the retriever by moving retrieval pressure into attention.** That is a real architectural shift, but it does not remove selection; it relocates selection from an external retriever into host KB choice, attention weights, and optional dynamic sparsification.

**The memory is harder to audit exactly where it gains authority.** JSON records are readable, but the trained encoder and query heads determine how those records influence generation. Review has to move from source reading to behavioral tests and probes.

**The code contains experiment infrastructure, not product governance.** Accuracy, Rouge, BERTScore, refusal checks, and attention dumps are useful research measures, but I did not find source-span preservation, claim status, reviewer acceptance, or invalidation history for individual KB entries.

**The synthetic-data generator is an import/generation path, not trace-derived memory.** It uses model calls to create records and QA pairs, but the source is prompted synthetic content rather than traces of an agent's own sessions, tools, actions, or trajectories.

**Push capability is not the same as an agent memory policy.** KBLaM can make a model attend to KB tensors when the host passes them. It does not itself decide which remembered artifacts a future agent task deserves.

## What to Watch

- Whether future releases add a host-side retrieval or routing layer before `kb_kvs`; that would change the read-back signal from mostly coarse/model-internal to an explicit targeted push policy.
- Whether dynamic sparsification is implemented for Phi-3 as well as Llama; the current sparsify path I found is in the Llama attention implementation.
- Whether checkpoints or model cards define a stable source-to-weight lineage format; that would matter for invalidating or regenerating parametric memory when KB records change.
- Whether evaluation grows per-record faithfulness tests or source-citation checks; that would make KBLaM more usable for governed knowledge rather than only benchmark QA.
- Whether a deployment wrapper appears that continuously feeds user/session memory into KBLaM; that would raise trace-derived and agent-loop questions not present in the inspected code.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: KBLaM stores and trains memory artifacts, but activation depends on host-supplied `kb_kvs` at model invocation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: KBLaM's records, configs, checkpoints, embeddings, and attention tensors have different forms and authorities.
- [Representational form](../../notes/definitions/representational-form.md) - classifies: KBLaM moves readable records into parametric tensors and trained weights.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - classifies: KBLaM's KB tensors advise generation through attention, while encoder/query-head weights carry learning authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: model wrappers, KB config, training scripts, and checkpointed adapters define how future generation uses memory.
