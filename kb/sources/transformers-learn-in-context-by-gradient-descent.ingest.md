---
description: Mechanistic ICML paper showing in-context regression can be implemented as gradient descent inside Transformer forward passes, sharpening the internal half of the KB's in-context-learning theory
source_snapshot: transformers-learn-in-context-by-gradient-descent.md
ingested: "2026-04-20"
type: kb/sources/types/ingest-report.md
domains: [in-context-learning, meta-learning, transformer-mechanisms, learning-theory]
---

# Ingest: Transformers Learn In-Context by Gradient Descent

Source: transformers-learn-in-context-by-gradient-descent.md
Captured: 2026-04-20
From: https://arxiv.org/pdf/2212.07677

## Classification

Type: scientific-paper -- ICML 2023 paper with explicit constructions, regression-task experiments, ablations, and citations; the PDF is an arXiv preprint/proceedings version.
Domains: in-context-learning, meta-learning, transformer-mechanisms, learning-theory
Author: Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, Joao Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov from ETH Zurich and Google Research; credible ML researchers working directly on mechanistic accounts of Transformer learning.

## Summary

The paper argues that Transformer in-context learning can, at least in controlled regression settings, be understood as gradient-based learning executed inside the model's forward pass. The authors give an explicit construction where a single linear self-attention layer induces the same data transformation as one gradient descent step on a squared-error regression loss, then show that trained self-attention-only Transformers often recover or closely match that construction. Deeper models can outperform plain gradient descent by learning a curvature-correction variant (GD++), MLPs let the mechanism operate over learned representations for nonlinear regression, and a copying/induction-head-like first layer can assemble the input-target token structure needed for the gradient-descent layer. The contribution is strongest as a mechanistic proof-of-possibility and empirical toy-domain result, not as a general explanation of all language-model in-context learning.

## Connections Found

The connection pass found a learning-theory cluster rather than a broad context-management cluster. The strongest direct connection is to [in-context-learning-presupposes-context-engineering](../notes/in-context-learning-presupposes-context-engineering.md): that note argues that in-context learning depends on external machinery to put the right knowledge in the window, while this source explains a possible internal mechanism once examples are present. It also extends [llm-learning-phases-fall-between-human-learning-modes](../notes/llm-learning-phases-fall-between-human-learning-modes.md) by making the "between long-term and short-term" phase more concrete: trained weights enable ephemeral inner-loop adaptation during one context. It grounds [treat-continual-learning-as-substrate-coevolution](../notes/treat-continual-learning-as-substrate-coevolution.md) as an opaque-substrate case where outer-loop training discovers an inner-loop algorithm, and it exemplifies [information-value-is-observer-relative](../notes/information-value-is-observer-relative.md) because the same examples become usable depending on architecture and trained weights. Source-to-source, it qualifies [Mesa Optimizers and Language Recursion](./mesa-optimizers-and-language-recursion.ingest.md) with narrow empirical evidence for learned optimizer-like behavior, and it contrasts with [On the "Induction Bias" in Sequence Models](./induction-bias-sequence-models-ebrahimi-2026.ingest.md) by showing that Transformers can learn some algorithms cheaply when the architecture, task, and token presentation fit.

## Extractable Value

1. **In-context learning has internal and external layers** -- high reach. The KB already has the external layer: context engineering selects and organizes what reaches the window. This source adds the internal layer: model weights determine what adaptation can be computed from those examples once loaded. [deep-dive]

2. **A trained model can encode a learning algorithm without updating weights at inference time** -- the paper cleanly separates durable outer-loop learning (weights trained across tasks) from ephemeral inner-loop adaptation (forward-pass gradient-like updates over context). This sharpens substrate and timescale vocabulary in [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md). [quick-win]

3. **Mechanistic evidence beats analogy for mesa-optimizer claims** -- unlike the speculative mesa-recursion source, this paper shows a concrete optimizer-like forward-pass mechanism and weight construction. The value is bounded but real: learned internal optimization exists in at least one simple, inspectable regime. [quick-win]

4. **Architecture and data presentation decide which algorithms are cheap to learn** -- the construction depends on token structure, linear self-attention, and a copying layer that merges inputs and targets. This pairs well with the induction-bias paper: Transformers are not uniformly bad or good at algorithm learning; their inductive biases make some computations easy and others expensive. [experiment]

5. **MLPs plus attention recover kernelized regression as an in-context mechanism** -- the paper's Proposition 2 connects Transformer blocks to gradient descent on learned representations and one-step kernel smoothing. This is a useful reference when reasoning about how examples in context become usable structure for a bounded observer. [just-a-reference]

6. **Standard architecture choices complicate the story** -- softmax attention and LayerNorm perform worse in these constructed regression settings, while softmax helps the copying layer. This matters because "Transformers learn by gradient descent" is not a single mechanism claim; it depends on which part of the architecture is doing which job. [just-a-reference]

## Limitations (our opinion)

The paper's strongest claims are narrow. The core experiments use simple noiseless regression tasks, small architectures, and carefully constructed tokens. That makes the single-layer construction hard to vary and valuable, but it does not establish that large language models generally perform gradient descent during ordinary prompting. The paper itself acknowledges that linear self-attention-only Transformers explain only a limited part of a complex process.

The usual Transformer architecture is only partially covered. Linear self-attention gives the cleanest construction; softmax attention and LayerNorm weaken alignment with gradient descent in the tested setup. The authors provide arguments and ablations for why softmax can still support copying, but the path from these toy settings to full autoregressive language modeling remains indirect.

The broader slogan is easy to overstate. "In-context learning is gradient descent" can absorb too many phenomena unless the target task, token construction, loss, and architecture are specified. A simpler account explains much of the result: for squared-error regression with examples laid out as input-target pairs, attention has a strong inductive path to kernel smoothing or gradient-like updates. That simpler account is still valuable, but it is not a universal theory of in-context learning.

The paper does not test noisy regression, regularization, open-ended reasoning, long-context retrieval, or real agent tasks. It also does not resolve the tension with architecture-limit evidence such as the induction-bias paper; instead, it helps phrase the better question: which algorithms does a given architecture make learnable under available training signals?

## Recommended Next Action

Update [in-context-learning-presupposes-context-engineering](../notes/in-context-learning-presupposes-context-engineering.md): add a section titled "Internal and external layers" connecting to [llm-learning-phases-fall-between-human-learning-modes](../notes/llm-learning-phases-fall-between-human-learning-modes.md) and [treat-continual-learning-as-substrate-coevolution](../notes/treat-continual-learning-as-substrate-coevolution.md). It should argue that context engineering supplies the right examples, while model-internal mechanisms determine what adaptation can be extracted from those examples.
