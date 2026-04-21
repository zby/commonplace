---
description: "Research implementation that converts key-value KB records into trainable attention key/value tensors, replacing external retrieval with model-internal KB attention"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-15"
---

# KBLaM

KBLaM is Microsoft Research's ICLR 2025 research implementation of Knowledge Base Augmented Language Models: a method for giving a transformer access to an external key-value knowledge base without a separate retrieval module. The repository at https://github.com/microsoft/KBLaM is closer to a model-architecture experiment than an agent memory service: it trains small adapters that turn KB records into attention key/value tensors, then modifies LLaMA/Phi-3 attention so generated text can attend to those tensors.

**Repository:** https://github.com/microsoft/KBLaM

**Reviewed commit:** https://github.com/microsoft/KBLaM/commit/4db377fa4dad2134a38fbc06f80938e66b9b5897

## Core Ideas

**Key-value records become model attention tensors.** The KB atom is a pair: a key string such as "the objective of X" and a value string containing the answer. `KBEncoder` wraps either Azure/OpenAI embeddings or a SentenceTransformer backbone, then applies separate trainable projectors for keys and values into the target model's hidden dimension. The output is not a retrievable document or database row; it is a stack of tensors shaped for injection into transformer layers. [kb_encoder.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/kb_encoder.py) implements the encoder, and [kblam_processor.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/kblam_processor.py) accepts either raw `(str, str)` pairs or precomputed embedding tensors.

**Retrieval is relocated into attention.** The LLaMA and Phi-3 forks append KB keys and values to the ordinary attention key/value states every `kb_layer_frequency` layers, then extend the attention mask with a KB block. LLaMA also has `dynamic_sparsify`, which computes attention over all KB keys and keeps the top-K at test time. The design eliminates an external retriever, but the model still performs a query-to-KB selection operation; it happens inside dense attention rather than in a vector database or RAG pipeline. The central mechanism is visible in the modified [LLaMA attention](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/llama3_model.py) and [Phi-3 attention](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/src/kblam/models/phi3_model.py) implementations.

**The base language model is mostly frozen.** The training script freezes the loaded LLM and trains the KB encoder parameters, optionally with a separate query head copied from the base model's query projection. That makes the learnable surface small compared with full fine-tuning, but it still requires model-specific source forks, GPU training, and checkpoint management. The optimizer setup in [train.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/train.py) trains `self.kbretriever.encoder.parameters()` plus optional query-head parameters.

**The knowledge base is flat and query-time supplied.** There is no persistent memory server, write API, graph, note lifecycle, or curation path. Evaluation samples a subset of JSON KB rows, encodes their keys and values, and passes the resulting `kb_kvs` tensors directly into `model.generate()`. The repo includes synthetic and Enron-derived JSON datasets, with dataset cards that explicitly frame them as grounded-LM training/evaluation material rather than complete real-world KBs. See the [synthetic dataset card](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/datasets/datasetcard_synthetic.md), [Enron dataset card](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/datasets/datasetcard_enron.md), and [eval.py](https://github.com/microsoft/KBLaM/blob/4db377fa4dad2134a38fbc06f80938e66b9b5897/experiments/eval.py).

**Evaluation is attention-centric.** The evaluation scripts compare KB mode with in-context and zero-shot modes, score generated answers with ROUGE/BERTScore/refusal metrics, and save attention weights to measure whether the correct KB row receives the most attention. This is a useful diagnostic: the system can ask not just "did the model answer correctly?" but "did the KB-attention head select the intended record?" That is stronger instrumentation than most external-memory systems expose.

**Model support is narrow by construction.** The README lists LLaMA 3, LLaMA 3.2 1B, and Phi-3 mini as supported models, and the source carries full copied/forked model files. Adding another architecture means writing another attention integration. This is the main practical cost of moving retrieval into the model: fewer moving parts at inference time, but tighter coupling to transformer internals and Hugging Face implementation details.

## Comparison with Our System

| Dimension | KBLaM | Commonplace |
|---|---|---|
| Primary substrate | Trained adapter weights plus query-time KB tensors | Markdown files in git |
| Knowledge unit | Flat key-value fact record | Typed note, claim, index, ADR, or instruction |
| Activation model | Transformer attention over encoded KB records | Agent chooses files/sections to load into bounded context |
| Retrieval boundary | Inside model attention; optional LLaMA top-K pruning | Outside model via grep, indexes, links, and reading decisions |
| Learning model | Supervised training on KB/QA datasets | Agent/human curation, distillation, link articulation, validation |
| Update path | Re-encode records; retrain adapters for new behavior | Edit files, validate, review, connect |
| Inspectability | Tensor attention and JSON rows; learned behavior opaque | Human-readable artifacts and git history |
| Integration surface | Python model classes and experiment scripts | Repository convention, CLI commands, skills, and notes |
| Governance | Dataset cards, tests, evaluation metrics | Structural validation, semantic gates, collection conventions |

**Where KBLaM is stronger.** It attacks activation at the model-mechanism level. A conventional RAG stack must choose chunks before the model reasons; KBLaM lets the model attend across KB records during generation, and can audit which records drew attention. It is also a clean counterexample to "external memory must be an external service": for bounded factual QA, a model-side adapter can make the KB feel like an extension of the transformer's attention state rather than a separate lookup system.

**Where commonplace is stronger.** Commonplace treats knowledge as a maintainable symbolic medium. Notes have source context, section structure, status, semantic links, and review gates; KBLaM's KB rows have no lifecycle beyond being encoded and attended to. Commonplace works with black-box frontier models and ordinary coding agents; KBLaM requires model forks, adapter training, and local GPU inference. Commonplace can represent methodology, design tradeoffs, contradictions, and procedures. KBLaM's implemented unit is a fact-shaped key/value pair.

**The deepest divergence is what "memory" is for.** KBLaM optimizes a grounded QA problem: given a set of factual records, answer questions by activating the right record without stuffing the records into prompt text. Commonplace optimizes agent competence over time: what should be remembered, how it should be structured, how agents discover it, and how it stays trustworthy. KBLaM is relevant to the activation layer of memory, not to curation, knowledge organization, or agent-operated maintenance.

## Borrowable Ideas

**Separate retrieval key from consumed value.** KBLaM's `key_string` and `description` split is simple and useful: one string exists to be matched, the other exists to be used. Commonplace already has a weak version in `description` frontmatter versus full note body. A stronger version would let notes carry generated retrieval handles tuned for semantic search without changing the prose artifact. *Needs a use case first - current grep/index navigation is good enough.*

**Attention-selection diagnostics as retrieval QA.** KBLaM's attention-weight evaluation asks whether the model looked at the expected KB row. A commonplace analogue would instrument context-building commands: for a known task, did the selector surface the notes a human expects? This would turn retrieval quality from anecdote into a testable signal. *Ready as a benchmark pattern, not an implementation priority.*

**Small learned adapters as activation experiments.** Training only KB projectors and optional query heads is a lower-risk way to study model-internal memory than full fine-tuning. For commonplace, this is not a near-term architecture, but it is a useful research reference if we ever evaluate whether a compiled representation of the KB can improve model activation. *Reference only - outside the file-first operating model.*

**Noise/outlier curricula for retrieval evaluation.** KBLaM trains and evaluates with distractor KB rows, increasing KB sizes, multi-entity questions, and outlier questions that should produce refusal. Those are good evaluation shapes for any memory system: not just "can it find a fact?" but "can it ignore many irrelevant facts, combine several records, and refuse unsupported queries?" *Ready to borrow for future KB retrieval benchmarks.*

## Curiosity Pass

**"No retrieval module" is not "no retrieval problem."** KBLaM removes an external retriever, but it still has to select relevant KB entries. The selection mechanism is attention over encoded KB keys, optionally followed by top-K pruning. That is a strong architectural move, not magic: the retrieval problem becomes differentiable and model-internal.

**The flat record shape is the real ceiling.** Even if the attention mechanism works perfectly, the implemented KB is a bag of key/value facts. There are no relationships among records, no contradiction handling, no provenance beyond dataset origin, no authority model, and no synthesis path. That is enough for the paper's grounded factual QA setting, but not enough for an agent-operated knowledge base.

**The implementation is research code, not a reusable memory product.** The experiment Makefile contains machine-specific `/datadisk/...` paths, the model support requires copied/forked transformer classes, and one evaluation branch imports `aug_row` even though `data_utils.py` defines `augment_row`. These are normal rough edges for a research repo, but they matter if someone reads "knowledge base augmented model" as deployable memory infrastructure.

**The interesting comparison is with in-context learning, not with file-backed KBs.** KBLaM's strongest claim is that it can scale KB access better than prompt-stuffing records as text. That is orthogonal to commonplace's main bet. Commonplace decides what artifacts should exist and how agents should navigate them; KBLaM decides how a model might condition on already-selected factual records without quadratic prompt overhead.

## What to Watch

- Whether the project publishes broadly usable checkpoints or Hugging Face integration that avoids local model forks and hard-coded experiment paths.
- Whether `dynamic_sparsify` becomes the practical default for large KBs, and how much quality it loses compared with full KB attention.
- Whether the adapter trained on synthetic/Enron-style records transfers to real enterprise KBs whose keys and values are messier, longer, and less single-fact-shaped.
- Whether future work moves beyond flat key/value facts into structured records, provenance, conflicting facts, or update semantics.
- Whether model-internal KB attention becomes a standard option in open models, making "compiled KB activation" a real alternative to external RAG for narrow factual workloads.

---

Relevant Notes:

- [charting-the-knowledge-access-problem-beyond-rag](../../notes/charting-the-knowledge-access-problem-beyond-rag.md) - complicates: KBLaM is a concrete example of leaving external RAG behind while still solving the same knowledge-access problem inside the model.
- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: KBLaM separates stored factual records from the activation mechanism that makes the model attend to them.
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - sharpens: KBLaM solves activation, not storage governance or learning lifecycle.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: KBLaM pays training and tensor-compute cost to avoid stuffing large KBs directly into prompt context.
- [distillation](../../notes/definitions/distillation.md) - contrasts: KBLaM compiles records into attention-facing tensors and learned adapters, while commonplace distillation produces inspectable symbolic artifacts for bounded-context consumers.
- [axes-of-artifact-analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: KBLaM combines flat key/value fact artifacts, JSON/NumPy/checkpoint backends, and an opaque learned adapter/query-head substrate.
