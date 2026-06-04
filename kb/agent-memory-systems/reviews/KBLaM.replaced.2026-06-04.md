---
description: "KBLaM review: research model architecture that encodes KB triples into learned key/value tensors attended by modified Llama/Phi layers"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# KBLaM

> Replaced 2026-06-04. See [KBLaM](./KBLaM.md) for the current review.

KBLaM, from Microsoft, is the official implementation of the ICLR 2025 "Knowledge Base Augmented Language Models" method. It is not an agent memory service or a file-backed KB operator. It is a research architecture that converts external knowledge-base entries into learned key/value tensors, inserts those tensors into modified transformer attention layers, and trains only the knowledge adapters and optional query heads while keeping the base LLM frozen.

**Repository:** https://github.com/microsoft/KBLaM

**Reviewed commit:** [4db377fa4dad2134a38fbc06f80938e66b9b5897](https://github.com/microsoft/KBLaM/commit/4db377fa4dad2134a38fbc06f80938e66b9b5897)

**Last checked:** 2026-06-02

## Core Ideas

**KB entries become model-side key/value tensors.** The retained knowledge unit used by the code is a pair such as `key_string` and `description`; `KBEncoder` embeds keys and values with OpenAI or SentenceTransformer embeddings, then projects them through separate key/value projectors into the hidden dimension expected by the modified LLM layers ([kb_encoder.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/kb_encoder.py), [train_utils.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/utils/train_utils.py)). The encoder can also consume precomputed base embeddings from `.npy` files rather than recomputing them during training or evaluation ([generate_kb_embeddings.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/dataset_generation/generate_kb_embeddings.py)).

**The base model is frozen; adapters carry the learned bridge.** The training script freezes the Hugging Face Llama or Phi model parameters, constructs a `KBEncoder`, and trains that encoder plus optional query-head parameters ([train.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/train.py)). Checkpoints save the wrapped model, an `encoder.pt` state dict, and an explicit KB config JSON, making the durable learned artifacts adapter weights and configuration rather than new text memories.

**Knowledge read-back is attention, not external retrieval.** The modified Llama and Phi attention modules accept `kb_kvs`, reshape the KB tensors per KB-enabled layer, concatenate KB keys and values in front of ordinary token key/value states, extend the attention mask, and let the model attend to those extra positions during generation ([llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py), [phi3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/phi3_model.py)). `KBLaMProcessor` exposes this as a Hugging Face processor that returns tokenized text plus `kb_kvs` ([kblam_processor.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_processor.py)).

**Context efficiency is shifted from prompt tokens to attention-side state.** The README frames KBLaM as avoiding an external retrieval module and avoiding in-context learning's quadratic overhead, with linear overhead in KB size ([README.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/README.md)). In code, the KB tensors are not serialized into natural-language prompt context. Llama support adds an optional `dynamic_sparsify` path: a separate query projection scores KB keys and keeps top-k KB tensors at test time before concatenation ([llama3_model.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py), [kblam_config.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_config.py)). Phi support at this commit concatenates the supplied KB tensors but does not implement the same dynamic sparsification branch.

**Evaluation is benchmark-oriented.** The repository includes synthetic and Enron-derived JSON datasets, scripts for synthetic data and base embedding generation, and evaluation loops for KBLaM, in-context learning, and zero-shot modes ([datasetcard_synthetic.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/datasets/datasetcard_synthetic.md), [datasetcard_enron.md](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/datasets/datasetcard_enron.md), [eval.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/eval.py)). The behavioral question is whether model outputs match KB answers or correctly refuse, not whether an agent maintained or promoted durable memories over time.

**The integration surface is a Python research package.** `pyproject.toml` packages `kblam` and depends on PyTorch, Transformers, SentenceTransformers, OpenAI, Azure ML, and evaluation libraries ([pyproject.toml](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/pyproject.toml)). There is no CLI, MCP server, editor extension, planner loop, file watcher, or agent hook in the inspected source.

## Artifact analysis

- **Storage substrate:** `model-weights` — JSON datasets in the repository or user-supplied dataset files, optionally split into train/test outputs
- **Representational form:** `parametric` — Symbolic JSON records with prose fields such as `name`, `description_type`, `description`, generated `Q`/`A`, and `key_string`
- **Lineage:** `authored` `imported` — synthetic rows are generated according to the dataset card, Enron rows are imported/extracted from an external dataset, embeddings are derived from row fields, and learned weights come from supervised training
- **Behavioral authority:** `knowledge` `routing` `ranking` `learning` — source rows and evaluation outputs act as knowledge/evidence, configs and attention code route KB tensors into layers, query heads and sparsification rank/select tensors, and encoder/query-head weights are learned conditioning artifacts

**Knowledge-base rows.** Storage substrate: JSON datasets in the repository or user-supplied dataset files, optionally split into train/test outputs. Representational form: symbolic JSON records with prose fields such as `name`, `description_type`, `description`, generated `Q`/`A`, and `key_string`. Lineage: synthetic rows are GPT-4-generated according to the dataset card; Enron rows are extracted from the Enron email dataset by a separate automated extraction/linking pipeline, then converted into triples. Behavioral authority: knowledge artifacts during training and evaluation, because they provide factual supervision and answer targets; they become stronger model-conditioning material only after encoding into KB tensors.

**Base embedding arrays.** Storage substrate: `.npy` files generated outside or alongside training, with separate key and value arrays. Representational form: distributed-parametric vectors from OpenAI embeddings or SentenceTransformer models. Lineage: derived from `key_string` and `description` fields by `generate_kb_embeddings.py`, invalidated when the source dataset, embedding model, or embedding endpoint changes. Behavioral authority: system-definition/ranking substrate only indirectly: these vectors determine the inputs to the learned key/value projectors and optional cached training path.

**`KBEncoder` projector weights and special-token embeddings.** Storage substrate: PyTorch module state dicts, saved as `encoder.pt` in training checkpoints. Representational form: distributed-parametric weights plus small symbolic choices such as projector type and special token names. Lineage: learned from supervised QA training over selected KB rows, optional outlier rows, augmented questions, dynamic KB sizes, and cached or online base embeddings. Behavioral authority: learning and conditioning authority. These weights decide how external KB rows are transformed into model-readable key/value tensors.

**Modified Llama/Phi attention code and `KBLaMConfig`.** Storage substrate: repository Python modules and saved Hugging Face config JSON. Representational form: symbolic code/config plus learned model/query-head weights where enabled. Lineage: authored modifications of upstream Transformers model implementations; runtime behavior changes when `kb_layer_frequency`, `kb_scale_factor`, `top_k_kb`, `dynamic_sparsify`, or `sep_query_head` changes. Behavioral authority: system-definition artifact with architectural force, because it decides which layers consume KB tensors, whether a separate query head scores KB keys, and how attention masks expose KB positions.

**Attention-weight dumps and evaluation outputs.** Storage substrate: `.npy` files and text/result dictionaries produced by evaluation options. Representational form: distributed-parametric attention matrices plus prose/model-output logs and scalar metrics. Lineage: derived from inference runs over chosen questions, KB subsets, model checkpoints, and configs. Behavioral authority: evaluation evidence for researchers; the inspected code does not feed these traces back into durable rules, new adapters, or future retrieval policies.

The main promotion path is model-training promotion: authored or generated KB rows become base embeddings, then learned key/value projections, then attention-accessible model state at inference. It is not a governance ladder from evidence to reviewed instruction. Nothing in the inspected implementation promotes a discovered lesson into a rule, validator, skill, or agent policy.

## Comparison with Our System

| Dimension | KBLaM | Commonplace |
|---|---|---|
| Primary purpose | Research architecture for conditioning frozen LLMs on external KB tensors | Git-native methodology KB for agent operation, review, validation, and navigation |
| Canonical retained artifact | KB rows, base embeddings, learned encoder/query-head weights, KB config | Typed Markdown notes, source snapshots, instructions, reviews, generated indexes, reports |
| Storage substrate | JSON datasets, `.npy` embeddings, PyTorch checkpoints, Python model code | Repository files, schemas, scripts, review reports, git history |
| Representational form | Mixed prose/symbolic rows plus distributed-parametric embeddings and weights | Mostly prose and symbolic metadata, with deterministic scripts and validation |
| Lineage | Dataset cards, generated embedding files, training checkpoints, configs | Source citations, archived replacements, collection contracts, review gates |
| Activation | Supplied KB tensors are concatenated into model attention layers during generation | Agents deliberately pull files/indexes/reports, with instructions and validators shaping behavior |
| Authority | Architectural attention pathway and learned adapter weights condition token generation | Collection/type contracts, skills, instructions, validation, semantic review, and human-readable evidence |

KBLaM is valuable evidence for a different class of memory system: one where retained knowledge is compiled into tensor state and consumed directly by a model's attention mechanism. Commonplace deliberately keeps most behavioral authority in inspectable prose, schemas, commands, and review artifacts. KBLaM gains runtime efficiency and avoids prompt-token bloat, but pays with lower inspectability, harder rollback at the individual fact level, and weaker source-level governance.

The context-efficiency contrast is sharp. Commonplace uses lexical search, indexes, type contracts, and skills so an agent can choose a small amount of text to load and explain why. KBLaM moves the KB outside the text prompt and into extra attention keys/values. That can be efficient for model inference, but the complexity of many KB tensors is hidden inside attention rather than exposed as a readable context bundle.

**Read-back:** `push` — Caller-supplied KB tensors are pushed into modified attention layers at generation time. Default KB supply is coarse; optional Llama `dynamic_sparsify` is instance-targeted inferred/embedding selection over current query states and KB keys. This is a library/model API surface, not a deployed agent loop.

The governance contrast is also sharp. KBLaM evaluates answer accuracy, refusal, precision, recall, ROUGE, and BERTScore; it does not keep a source snapshot, citation, reviewer decision, or replacement history for each durable fact. Commonplace would treat those missing surfaces as central if a fact can later shape agent behavior.

I did not find qualifying trace-derived learning. The repository uses synthetic and Enron-derived datasets, cached embeddings, supervised training, and evaluation outputs. Those are not agent/session/tool traces, and the evaluation traces are not distilled into durable behavior-shaping artifacts by the inspected code.

### Borrowable Ideas

**Separate memory representation from prompt representation.** Worth borrowing conceptually, not directly. Commonplace can keep prose as the authoritative artifact while generating compact derived views for runtime selection. KBLaM is a reminder that "what the model consumes" need not equal "what humans review."

**Make compiled memory explicitly invalidatable.** Ready as a design rule. If Commonplace grows embeddings, rankers, or compiled prompt packs, each compiled artifact should record the source notes, model/version/config, and regeneration command. KBLaM's cached embeddings and encoder checkpoints show the need, but not a full governance answer.

**Treat dynamic sparsification as a context budget primitive.** Needs a concrete search layer first. KBLaM's top-k KB pruning is attention-side selection; Commonplace's analogue would be a query-time cap over candidate notes or facts, paired with readable justifications.

**Keep the base model unchanged where possible.** Ready as an architectural bias for tools, not as model training. KBLaM preserves baseline behavior when no KB is supplied; Commonplace should likewise make generated indexes, reports, and optional search layers additive rather than changing the meaning of canonical notes.

**Do not borrow tensorized facts as authoritative KB entries.** A learned adapter can improve answers, but it is a poor canonical store for methodology knowledge. Commonplace should keep high-authority claims in reviewable artifacts and use distributed-parametric state only as a derived aid.

## Write-side placement

**Write agency:** `manual` `automatic` — researchers or hosts choose datasets, configs, cached embeddings, checkpoints, and supplied KB rows, while embedding generation and supervised training automatically derive base embeddings, encoder weights, query-head weights, and attention-accessible KB tensors from those inputs

**Curation operations:** `promote` — the review describes a model-training promotion path where authored or generated KB rows become base embeddings, learned key/value projections, and then attention-accessible model-conditioning state

## Read-back placement

**Direction.** KBLaM is push from the receiving model's perspective. `KBLaMProcessor` turns a supplied knowledge base into `kb_kvs`, and the modified Llama/Phi generation path consumes those tensors without the model or an agent calling a retrieval tool. Because this repository is a research package, the review treats that as an API capability: the host or evaluation script decides which KB tensors to provide.

**Read-back signal:** `coarse` `inferred / embedding` — the default path exposes caller-supplied KB tensors coarsely, while Llama `dynamic_sparsify` uses query-head vector scoring against KB keys for instance-targeted embedding selection.

**Faithfulness tested:** `no` — the review found benchmark and attention-dump support but no with/without activation ablation showing a fired KB tensor changed a decision.

**Targeting and signal.** There are two memory push shapes. The default path is `coarse`: a caller supplies a KB tensor batch or subset, and all supplied KB keys/values are exposed to KB-enabled layers. The Llama `dynamic_sparsify` path is `instance`-targeted when enabled: the current hidden states are projected through the separate query head, scored against KB keys by learned vector dot product, and pruned to `top_k_kb` before attention. The signal is therefore `inferred / embedding`. The Phi path at this commit concatenates supplied KB tensors and can use a separate query head for attention scoring, but it does not implement the same top-k pruning branch.

**Injection point.** Read-back occurs during generation, before token choices are made, so supplied or pruned KB tensors can affect the immediate answer.

**Selection, scope, and complexity.** Scope is mostly host-supplied: the caller chooses the KB rows or embeddings passed as `kb_kvs`. Inside Llama, `dynamic_sparsify`, `top_k_kb`, `kb_layer_frequency`, `sep_query_head`, and `kb_scale_factor` control which KB tensors are exposed at each KB-enabled layer and how their attention scores are scaled. Actual precision, recall, and context dilution are not verified from code.

**Authority at consumption.** The KB tensors have direct model-conditioning authority through attention-side keys and values. They are not human-readable prompt context at consumption time, and the receiving model cannot inspect their source rows unless the host separately preserves that mapping.

**Faithfulness.** The repository evaluates answer accuracy, refusal, precision, recall, ROUGE, BERTScore, and can dump attention weights, but I did not find a WITH/WITHOUT activation ablation proving that a particular fired KB tensor changed a decision. The `push-activation` tag rests on the implemented attention-side activation mechanism, not on measured downstream faithfulness.

**Other consumers.** Researchers consume datasets, checkpoints, metrics, and attention dumps. Those artifacts are evaluation evidence; the inspected code does not feed them back into a durable memory selector or governance loop.

## Curiosity Pass

**It is "memory" only after you accept model attention as the read path.** There is no agent store/retrieve loop, no persistent user memory API, and no context assembly service. The memory act is supplying KB tensors to `generate()`.

**Dynamic sparsification is implemented asymmetrically.** Llama attention has a `dynamic_sparsify` top-k pruning path; the Phi attention code reviewed here concatenates KB tensors but does not mirror that branch.

**The learned artifact is hard to inspect at fact granularity.** You can inspect source rows and embeddings, and you can dump attention weights, but a trained projector does not tell a maintainer which source fact was accepted, rejected, or distorted in a human-reviewable way.

**The README's "no retrieval module" claim is mostly true, but not "no selection."** KBLaM removes a separate retriever service. The Llama dynamic sparsification path still performs query-dependent top-k selection inside attention preparation.

**Dataset cards are better lineage than many model-memory repos provide.** They do not make generated/extracted facts reliable, but they clearly state synthetic generation, Enron extraction, and intended research/evaluation use.

## What to Watch

- Whether KBLaM adds source-span or row-level provenance through the encoding path, so an answer can be traced back to a specific KB row after tensor attention.
- Whether dynamic sparsification becomes a shared, evaluated path across supported model families rather than a Llama-specific branch.
- Whether checkpoints begin saving enough metadata to regenerate exact base embeddings, encoder weights, KB config, training data slice, and query-head state from source.
- Whether attention-weight dumps become a feedback loop that trains better pruning or fact selection. That would reopen the trace-derived decision if evaluation traces produce durable behavior-shaping artifacts.
- Whether downstream users wrap KBLaM in an agent harness that automatically selects, scopes, and supplies KB tensors before actions. That would be an integration review, not evidence present in this repository alone.

## Bottom Line

KBLaM is a serious model-architecture reference for tensorized external knowledge, not a governed agent memory system. It shows one way to keep KB content out of text prompts and inside attention-side key/value state, with optional query-dependent sparsification. For Commonplace, the main lesson is to keep compiled memory views clearly derived from inspectable sources, because the more behavior moves into tensors, the more explicit lineage and regeneration contracts matter.

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - contrasts: KBLaM reduces prompt-token pressure by moving KB entries into attention-side tensors.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: KBLaM requires separating source rows, base embeddings, learned projectors, configs, and evaluation outputs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: KB rows and dataset cards are evidence/reference material before model encoding.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: model code, configs, learned projectors, and query heads condition future token generation.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: KBLaM stores and compiles knowledge, but activation happens only when a caller supplies `kb_kvs` to the model.
