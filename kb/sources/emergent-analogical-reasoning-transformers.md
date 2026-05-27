---
source: https://arxiv.org/html/2602.01992v4
description: "Transformer analogy paper that treats analogical reasoning as relational-structure alignment plus functor-like vector transformation"
captured: 2026-05-26
capture: web-fetch
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Emergent Analogical Reasoning in Transformers

Author: Gouki Minegishi, Jingyuan Feng, Hiroki Furuta, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo
Source: https://arxiv.org/html/2602.01992v4
Date: 23 May 2026

arXiv:2602.01992v4 [cs.AI]

Snapshot note: The arXiv HTML rendering omits or mangles some mathematical symbols and table values. This snapshot preserves the paper's section structure and recoverable prose, but formulas should be checked against the PDF before precise technical use.

## Abstract

The paper studies how Transformers acquire and implement analogical reasoning. It frames analogy as inferring correspondences between entities across categories, inspired by functors in category theory. The authors introduce a synthetic task for controlled evaluation and report that analogical reasoning depends strongly on data characteristics, optimization choices, and scale. Their mechanistic account decomposes analogical reasoning into structural alignment in embedding space and functor application inside the Transformer. They also report analogous signatures in pretrained LLMs.

## 1 Introduction

The paper contrasts compositional reasoning, where conclusions follow from chaining local relations, with analogical reasoning, where a model identifies shared relational structure across domains. The authors use a category-theoretic framing: entities and relations form categories, and analogy is represented as a mapping between relational structures.

The central empirical claim is that Transformers learn analogical reasoning through a staged process. In their synthetic task, models first fit in-distribution facts, then acquire compositional reasoning, and only later acquire analogical reasoning. The paper argues that this later stage depends on structured internal representations rather than mere memorization or parameter count.

## 2 Synthetic Task for Analogical Reasoning

The task defines entities, relations, and three fact types:

- Atomic facts: single relation-labeled edges between entities.
- Compositional facts: two-hop relational compositions derived from atomic facts.
- Analogical facts: cross-category entity correspondences induced by a bijective mapping between two categories.

The model is trained on token sequences representing these facts and evaluated on held-out compositional and analogical facts. Compositional reasoning tests whether a model can combine known relational edges. Analogical reasoning tests whether a model can infer a counterpart entity in another category despite not seeing the direct correspondence during training.

The default setup uses causal Transformers trained with final-token cross entropy. Experiments vary the number of entities, number of relations, out-of-distribution ratios, optimization settings, width, and depth.

## 3 Emergent Analogical Reasoning

The paper reports a three-stage learning progression:

1. Memorization of in-distribution facts.
2. Acquisition of compositional reasoning.
3. Later acquisition of analogical reasoning.

Analogical reasoning behaves differently from compositional reasoning. More entities make analogical reasoning slower to acquire. Too few relation types can prevent it from emerging because entities cannot be distinguished by relational role. Very large relation sets can lead to transient analogical reasoning that later disappears. Increasing the analogical out-of-distribution ratio makes analogical generalization harder.

Optimization matters. Moderate weight decay accelerates analogical reasoning, but excessive weight decay can prevent it while compositional reasoning remains intact. Larger batch sizes generally accelerate acquisition. The authors argue that analogy is not explained solely by weight-norm regularization and requires more structured internal representations.

Scaling is non-monotonic. Compositional reasoning improves more predictably with model size, while analogical reasoning can degrade when models become wider or deeper under fixed optimization settings. Learning-rate sweeps can recover performance in deeper models, so the depth result may be partly an optimization artifact.

## 4 The Mechanism of Analogy in Transformer

The proposed mechanism has two components:

1. Structural alignment in embedding space. Entities across categories become geometrically aligned according to relational role.
2. Functor application in Transformer layers. The model applies a mapping-like transformation from a source entity to its counterpart.

The authors use Dirichlet energy over a graph of analogical correspondences to quantify structural alignment. Lower energy indicates that related entities are closer in representation space. In the synthetic task, analogical performance rises after Dirichlet energy decreases.

They also analyze attention and representation geometry. Attention from the functor token to the source entity increases before reliable analogical outputs appear, suggesting internal circuit formation before behavioral success. A parallelism measure between source entity, functor representation, and target unembedding increases with analogical performance, supporting an additive vector-transformation account.

## 5 The Mechanism of Analogy in LLMs

The paper probes pretrained LLMs with in-context analogy prompts using Gemma 2 models. The prompt presents two categories with shared relational structure and asks for a missing cross-category counterpart. The authors use logit-lens analysis across layers and compare answer probability with Dirichlet energy.

They report that answer probability rises as Dirichlet energy decreases across layers, echoing the synthetic training dynamics. In the synthetic task, alignment emerges over training steps; in pretrained LLMs, a similar pattern appears over network depth during in-context computation.

## 6 Related Works and Discussion

The paper positions its contribution against work on analogy in language models, synthetic tasks for understanding Transformers, grokking, compositional generalization, and linear representations. It argues that analogy is not merely compositional chaining, because it requires relational-role alignment across domains.

The authors describe analogy as a potential route to sample efficiency and creativity, since a model can transfer relational structure from one domain to another without learning every target-domain fact directly.

## 7 Limitations

The authors identify several limitations:

- The synthetic task is intentionally controlled and abstract, so it does not capture the full complexity of real-world analogy.
- The mechanistic story depends on a task with explicit categories and a functor token; natural analogies may be less explicit.
- Prompt design matters in LLM experiments. Some prompt variants introduce arithmetic shortcuts or tokenization artifacts.
- Dirichlet energy can be affected by representation norm growth, so it is not a pure alignment metric in every setting.
- The observed scaling behavior depends on optimization settings and data regime.

## 8 Conclusion

The paper argues that analogical reasoning in Transformers emerges through geometric alignment of relational structures and a functor-like transformation mechanism. It proposes that this provides a concrete mechanistic account of analogy in neural networks and a basis for studying reasoning beyond sequential composition.

## Appendix Signals

- Learning-rate sweeps show that overly large learning rates can block generalization.
- PCA visualizations show entity embeddings becoming organized by relational role over training.
- A derivation extends Dirichlet energy to multidimensional node embeddings.
- Deeper models may fit training data without developing the aligned geometry needed for analogy.
- Alternative prompts reveal that LLM analogy probes can be confounded by arithmetic shortcuts, tokenization, and entity-marker choices.
- Entity-count experiments in LLMs suggest that more complex analogical problems require later-layer computation.
- LLaMA experiments show qualitatively similar Dirichlet-energy trends.
- E-KAR benchmark experiments extend the energy/probability analysis to natural-language analogies.
- Noisy or imperfect isomorphism degrades analogical reasoning.
- Multiple functor/category variants can still produce analogical reasoning.
- An implicit-functor variant can work, but is harder and lower-performing than the explicit-functor setup.
- Linear probes detect analogical information earlier than logit lens in some layers.
- Bilinear probe analysis provides complementary evidence for a functor-direction interpretation.
