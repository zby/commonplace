---
source: https://arxiv.org/html/2601.03220v1
captured: 2026-03-05
capture: web-fetch
type: academic-paper
---

# From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence

Author: Marc Finzi, Shikai Qiu, Yiding Jiang, Pavel Izmailov, J. Zico Kolter, Andrew Gordon Wilson
Source: https://arxiv.org/html/2601.03220v1
Date: 2026-01

Institutions: Carnegie Mellon University, New York University

## Overview

This paper introduces **epiplexity** (epistemic complexity), a new information measure designed to quantify structural information extractable by computationally constrained observers. The work addresses fundamental gaps between classical information theory and modern machine learning practice.

## Core Problem

Existing frameworks (Shannon entropy, Kolmogorov complexity) fail to explain:
- How synthetic data improves model capabilities despite deterministic generation
- Why data ordering affects learning outcomes
- How models learn more structure than present in data-generating processes
- How AlphaZero extracts strategy from simple game rules alone

## Key Contributions

### 1. Three Apparent Paradoxes

The authors identify tensions between theory and practice:

- **Paradox 1:** Deterministic transformations cannot increase information (yet AlphaZero, synthetic data, and emergent phenomena contradict this)
- **Paradox 2:** Information is factorization-independent (yet left-to-right text ordering outperforms reverse)
- **Paradox 3:** Likelihood modeling merely matches distributions (yet observers extract structures beyond generating processes)

### 2. Epiplexity Definition

Epiplexity separates random from structural information by finding the program minimizing time-bounded MDL (Minimum Description Length):

> "Epiplexity captures the structural information present to a computationally bounded observer"

Key distinctions:
- **Time-bounded entropy (H_T):** Unpredictable random content (like CSPRNG outputs)
- **Epiplexity (S_T):** Learnable structural patterns visible within computational limits

### 3. Measurement Approaches

**Prequential Coding:** Estimates model description length as area under loss curves above final loss — simple but heuristic.

**Requential Coding:** Uses cumulative KL divergence between teacher and student models — rigorous but computationally expensive (2-10x slower).

Both approaches rank datasets consistently, though absolute values differ.

## Theoretical Results

**Theorem 9:** CSPRNGs exhibit maximum time-bounded entropy but negligible epiplexity — matching intuition that pseudorandom sequences are structurally empty despite appearing random.

**Theorem 10:** Under one-way function assumptions, high-epiplexity random variables exist (scaling logarithmically with dimension).

## Applications

The framework explains:
- Why pre-training on text transfers better than images
- How data ordering and interventions affect generalization
- Why certain datasets support broader out-of-distribution performance
- How emergent phenomena arise in cellular automata and dynamical systems

## Key Insights

1. **Observer-dependent randomness:** The same object may appear structured or random depending on computational budget
2. **Information creation through computation:** Deterministic processes can extract exploitable structure when observers have bounded resources
3. **Separation of concerns:** Epiplexity provides a task-independent measure of learnable content, distinct from downstream performance guarantees

## Practical Implications

The work provides a theoretical foundation for **data selection** (complementing traditional model selection), suggesting principles for:
- Choosing or generating training data
- Curriculum design for language models
- Synthetic data creation strategies
- Dataset interventions improving generalization

## Mathematical Framework

The formalization rests on:
- **Prefix-free Turing machines** for unambiguous program encoding
- **Time-constructible bounds** on computation
- **Two-part MDL codes** balancing model complexity against prediction accuracy
- **Cryptographic primitives** (one-way functions, CSPRNGs) motivating resource-bounded distinctions

## Significance

This work bridges algorithmic information theory with practical machine learning, offering novel perspectives on why modern systems succeed where classical theory predicts failure. It establishes computational boundedness as fundamental to understanding information in realistic learning scenarios.
