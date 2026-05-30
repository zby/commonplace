---
description: "KBLaM review: Microsoft Research model fork that projects key-value KB rows into learned attention key/value tensors rather than a retrievable agent KB"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# KBLaM

KBLaM, from Microsoft Research, is a research implementation of Knowledge Base Augmented Language Models for Llama 3 and Phi-3. It does not maintain an agent memory store. Instead, it turns flat key/value KB rows into projected key and value tensors, modifies transformer attention so selected layers can attend to those tensors, and trains the projection adapter plus optional query heads on synthetic or Enron-derived grounded QA tasks.

**Repository:** https://github.com/microsoft/KBLaM

**Reviewed commit:** [4db377fa4dad2134a38fbc06f80938e66b9b5897](https://github.com/microsoft/KBLaM/commit/4db377fa4dad2134a38fbc06f80938e66b9b5897)

**Last checked:** 2026-05-16

## Core Ideas

**The source KB is a flat key/value table.** The code expects rows with `name`, `description_type`, `description`, `Q`, `A`, and `key_string`; dataset cards describe the synthetic KB as GPT-4-generated triples and the Enron KB as triples extracted from Enron email with downstream entity linking ([datasets/datasetcard_synthetic.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/datasets/datasetcard_synthetic.md), [datasets/datasetcard_enron.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/datasets/datasetcard_enron.md), [src/kblam/utils/data_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/data_utils.py)). These rows are prose-plus-symbolic knowledge artifacts: they provide evidence and answer content, but they are not themselves the runtime mechanism that ranks or activates knowledge.

**The KB encoder maps rows into attention-shaped tensors.** `KBEncoder` wraps either OpenAI embeddings or a SentenceTransformer, freezes the base embedding model by default, then trains separate key and value projectors plus a small special-token embedding table. `encode()` and `encode_base_embeddings()` output stacked key/value tensors whose dimensionality is sized for the target model hidden size and selected KB-attention layers ([src/kblam/kb_encoder.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/kb_encoder.py), [src/kblam/models/kblam_processor.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_processor.py)). The learned adapter state is distributed-parametric retained state; its storage substrate is model checkpoints such as `encoder.pt`, not readable notes or database records.

**The model forks put KB tensors directly into self-attention.** KBLaM copies Hugging Face Llama and Phi-3 model code, adds `kb_kvs` and `KBLaMConfig`, reshapes the provided KB tensors per layer, prepends them to the attention keys and values at layers matching `kb_layer_frequency`, and extends the attention mask so text tokens can attend over KB entries ([src/kblam/models/llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py), [src/kblam/models/phi3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/phi3_model.py), [src/kblam/models/kblam_config.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_config.py)). The symbolic system-definition artifact is the model fork; the behavior-changing runtime artifact is the transient KB key/value tensor block inside attention.

**Attention is the activation and authority surface.** For Llama, `dynamic_sparsify` can prune runtime KB keys/values to top-k entries by a separate query projection; `sep_query_head` can replace the KB-attention scores with scores from `q_proj_new`; `kb_scale_factor` can rescale KB attention logits before softmax ([src/kblam/models/llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py), [src/kblam/models/kblam_config.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_config.py)). The behavioral authority is not advice or instruction; it is ranking and activation force inside the model's attention computation.

**Training learns projection and optional query-head state, not a maintained KB.** The training script freezes the base LLM, builds a `KBEncoder`, samples true rows plus random context rows, feeds their encoded tensors through the model, and optimizes cross-entropy on generated answers. It saves the model checkpoint, `encoder.pt`, and a JSON KB config; if `sep_query_head` is enabled, selected query-head parameters are also trainable ([experiments/train.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/train.py), [src/kblam/utils/train_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/train_utils.py)). The lineage runs from dataset rows and precomputed `.npy` base embeddings into adapter/checkpoint state, but the resulting weights do not preserve row-level provenance in a reviewable form.

**Evaluation treats KBLaM as an alternative to retrieval and in-context baselines.** Evaluation loads a checkpointed model, encoder state, and KB config, encodes a sampled KB subset, then measures generation, refusal, attention accuracy, ROUGE, BERTScore, and memory cost against `kb`, `icl`, and `zeroshot` modes ([experiments/eval.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/eval.py), [src/kblam/utils/eval_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/eval_utils.py)). Optional attention-weight dumps are diagnostic artifacts, not a memory lifecycle.

## Comparison with Our System

| Dimension | KBLaM | Commonplace |
|---|---|---|
| Primary purpose | Research architecture for grounding LLM answers in flat KB rows without an external retriever | Agent-operated methodology KB with durable notes, sources, instructions, reviews, ADRs, and validation |
| Storage substrate | JSON datasets, `.npy` base embeddings, PyTorch/Hugging Face checkpoints, `encoder.pt`, config JSON, runtime tensors | Git-tracked Markdown, schemas, scripts, source snapshots, generated indexes, review outputs |
| Representational form | Mixed symbolic rows/config/code plus distributed-parametric embeddings, adapter weights, query heads, and attention activations | Mostly prose and structured frontmatter, with symbolic links, schemas, commands, and validation code |
| Lineage | Dataset-to-embedding-to-checkpoint lineage exists operationally, but adapter weights and attention effects are not row-auditable artifacts | Source-pinned notes, authored citations, replacement archives, status fields, validation, and review gates |
| Activation | Model-internal attention over projected KB keys/values, optional top-k sparsification and attention dumps | `rg`, indexes, descriptions, authored links, skills, instructions, validation and review workflows |
| Behavioral authority | Ranking and activation authority inside transformer attention | Advice, instruction, routing, validation, review, and governance authority in inspectable artifacts |

KBLaM and commonplace agree that knowledge storage alone is insufficient. A row matters only when it can change a later answer. KBLaM achieves that by moving KB rows into the model's attention substrate; commonplace achieves it by making human- and agent-readable artifacts discoverable before a worker acts.

The main divergence is inspectability. In KBLaM, the decisive system-definition artifacts are source code forks, adapter weights, query-head weights, config settings, and transient attention tensors. The original KB rows remain knowledge artifacts, but the behavior-changing route from row to answer passes through distributed-parametric state and softmax attention. In commonplace, stronger behavioral authority is intentionally assigned to inspectable notes, type specs, instructions, schemas, and commands.

KBLaM is much closer to model augmentation than to agent memory. It has no authored link graph, review status, contradiction handling, retirement lifecycle, source snapshot discipline, or promotion path from evidence to notes or instructions. It also does not qualify as trace-derived learning under this review vocabulary: the implemented learning loop trains over datasets of KB rows and QA pairs, not over agent sessions, tool traces, conversations, rollouts, or repeated task trajectories.

The model-fork boundary is important. KBLaM does not package a generic memory service that any agent can query; it modifies specific Llama and Phi-3 implementations. That gives the KB tensors high activation authority when the forked model is used, but weak adoption affordances for ordinary coding-agent workflows where memory should remain inspectable, editable, and portable across model providers.

**Read-back:** push — supplied KB tensors enter model attention directly, with optional top-k sparsification inside the forward pass.

## Borrowable Ideas

**Separate source rows, learned adapters, runtime tensors, and attention effects.** Ready to borrow as analysis vocabulary. KBLaM is a clean reminder that one "memory" feature may contain knowledge artifacts, system-definition artifacts, distributed-parametric checkpoints, and transient activation state with different governance needs.

**Treat attention-facing memory as an activation layer, not a library.** Useful conceptually. Commonplace should not make its durable knowledge opaque, but it could still study compiled activation aids that help a model focus on relevant notes after source-grounded retrieval has already selected candidates.

**Use refusal/outlier training as a benchmark axis.** Worth borrowing for eval design, not architecture. KBLaM's training and evaluation include questions whose answer is absent from the KB, which directly tests whether the system overclaims from available retained state.

**Do not borrow model-specific forks as the primary memory interface.** The implementation shows why: changing each supported model architecture is expensive, provider-specific, hard to audit, and distant from agent-native file and terminal workflows.

## Takeaways

**KBLaM is an attention-integration experiment, not a maintainable agent KB.** Its contribution is showing how flat KB rows can become attention keys and values. It does not solve authoring, review, source trust, lifecycle, or cross-agent use.

**The artifact stack is unusually explicit.** Source KB rows, precomputed base embeddings, learned projector weights, optional query-head weights, model forks, config values, runtime KB tensors, and attention dumps each need separate substrate, form, lineage, and authority labels.

**Behavioral authority sits inside softmax.** The projected KB tensors influence generation because the model attends to them. That authority is strong but hard to inspect after training, especially when adapter weights and query heads mediate the original row content.

**Lineage weakens as soon as rows become weights.** Dataset cards and embedding generation scripts describe the upstream sources; checkpoint directories preserve training outputs. But individual facts do not carry durable review status or row-level provenance through the learned adapter.

**No trace-derived tag.** Ordinary supervised training over generated or extracted KB datasets is not trace-derived learning in the current survey sense. There is no implemented path from agent behavior traces into durable lessons, instructions, rankers, or model state.

## Curiosity Pass

The surprising part is how direct the mechanism is. KBLaM does not retrieve passages, construct a graph, or write prompts containing the KB. It reshapes encoded KB rows into the same key/value space that attention already consumes, then lets the model's attention select among them.

The system's limitation follows from the same choice. Once the KB becomes tensors and learned projections, ordinary KB governance disappears. A maintainer can inspect rows, scripts, and checkpoints, but cannot read the behavior-shaping adapter state as claims.

The code is research-shaped. It supports specific model forks, experiment scripts, cached embeddings, and diagnostics; it is not a production substrate for evolving knowledge. The README also states the project is intended for research and warns that out-of-distribution KBs can produce incomplete or incorrect answers ([README.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/README.md)).

## Open Questions

- How stable is the row-to-attention mapping when the KB distribution differs from synthetic and Enron-style training data?
- Can attention dumps be turned into useful provenance explanations for which KB row affected a generated answer?
- Would a stronger checkpoint format preserve row-set identity, embedding model version, dataset card, and train/eval split metadata alongside `encoder.pt`?
- How much of the gain comes from learned key/value projection versus the optional separate query head?
- Can a model-internal KB layer coexist with a source-auditable KB lifecycle, or does the opacity of weights make it a separate product category?
- What happens when KB rows conflict, supersede each other, or require retirement after checkpoint training?

## What to Watch

- Whether KBLaM adds first-class provenance metadata for checkpoints and encoded KB tensors.
- Whether future versions support model families without source-level model forks.
- Whether attention explanations become user-facing enough to audit row influence.
- Whether updates to KB rows require full adapter retraining, partial regeneration, or only runtime tensor recomputation.
- Whether future work trains from interaction traces or correction feedback; that would change the trace-derived classification.

## Bottom Line

KBLaM is best read as a model-architecture experiment that moves knowledge activation from external retrieval into transformer attention. Its source KB rows are knowledge artifacts, but the behavior-changing machinery is a stack of learned adapters, optional query heads, model forks, runtime key/value tensors, and attention scores. The borrowable lesson for commonplace is the artifact split, not the architecture: keep durable knowledge inspectable, and be explicit when compiled or learned activation layers gain authority over what the model sees.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: KBLaM requires separating source rows, embeddings, adapter checkpoints, model forks, runtime tensors, and attention weights by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: KB rows and dataset cards serve as evidence and answer content before projection.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: model forks, adapter weights, query heads, and config values carry ranking and activation authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - illustrates: KBLaM's stored rows matter only after they are transformed into attention-facing tensors.
