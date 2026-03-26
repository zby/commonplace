---
source: https://arxiv.org/html/2503.16743v5
description: Introduces SuperARC, an AIT-grounded benchmark showing frontier LLMs score near zero on recursive compression tasks and newer versions often regress, while neuro-symbolic CTM/BDM methods achieve perfect scores — evidence that statistical pattern matching differs fundamentally from algorithmic abstraction.
captured: 2026-03-26
capture: web-fetch
type: academic-paper
---

# Can Complexity and Uncomputability Explain Intelligence? SuperARC: A Test for Artificial Super Intelligence Based on Recursive Compression

Author: Alberto Hernández-Espinosa, Luan Ozelim, Felipe S. Abrahão, Hector Zenil
Source: https://arxiv.org/html/2503.16743v5
Date: 2025

## Abstract

This research introduces SuperARC, an increasing-complexity, open-ended benchmark grounded in Algorithmic Information Theory (AIT) to evaluate AI models' capacity for abstraction and prediction. Unlike human-centric tests, SuperARC measures fundamental mathematical properties of randomness and optimal inference. The authors tested frontier LLMs and found that while leading models outperform others on multiple tasks, newer versions often regress, falling far from theoretical intelligence targets. A hybrid neuro-symbolic approach (CTM/BDM) outperforms specialized prediction models, demonstrating that "predictive power through arbitrary formal theories is directly proportional to compression over the algorithmic space, not the statistical space."

## 1 Introduction

Traditional intelligence metrics suffer from anthropocentric bias. The paper argues for grounding AI evaluation in fundamental mathematics—specifically Algorithmic Information Theory—rather than human-centric frameworks like IQ tests or language benchmarks.

The authors note that some industry leaders now explicitly connect data compression, algorithmic complexity, and AI development. This connection motivates SuperARC: a test that evaluates compression-based model abstraction and recursive prediction capabilities. The framework builds on prior work applying CTM/BDM methods to human and animal cognition.

**Key distinction**: SuperARC avoids benchmark contamination through open-endedness and theoretical uncomputability, making the test equally complex as the phenomenon it measures—intelligence itself.

## 2 Results

### 2.1 Next-Digit Prediction with Binary and Non-Binary Sequences

Researchers tasked LLMs specialized in time-series prediction with forecasting final digits in sequences categorized by algorithmic complexity. Results for binary "climber" sequences (those with recursive properties) showed Lag-Llama achieving 70% precision, while TimeGPT-1 and Chronos barely reached 50%. For truly random sequences, all models performed near chance (50%), indicating limited predictive capability beyond training distribution pattern matching.

Analysis of non-binary sequences using Levenshtein distance metrics revealed that "predictive accuracy of LLM models, even when fine-tuned for numerical series, diminishes as the complexity of the sequences increases." BDM captured complexity more consistently than Shannon entropy or traditional compression algorithms.

### 2.2 Free-Form Generation Tasks

When asked to generate formulas reproducing increasingly complex sequences, LLM-generated models became progressively longer and less compressible. As complexity increased, models fundamentally failed to compress sequences into concise formulas, instead relying on convoluted representations—evidence of comprehension failure.

#### 2.2.1 Emergent Abilities

Testing claims about LLM creativity and innovation, the researchers challenged models to generate diverse solution approaches for sequence reproduction. Results showed Gemini, Claude-3.5-Sonnet, and ChatGPT-4o performed relatively better than Meta and Mistral, yet all shared fundamental limitations: inability to generate novel solutions beyond memorized patterns.

### 2.3 Code Generation Tasks

The majority of "correct" generated programs simply printed target sequences directly—"correct programs are more common at the lowest levels of complexity," indicating solutions without compression or genuine understanding. Higher complexity led to increased reliance on trivial strategies.

Across programming languages, print-statement solutions dominated correct outputs. Temperature parameter variations produced nearly identical no-compression percentages, suggesting the effect wasn't temperature-dependent but reflected fundamental model limitations.

### 2.4 SuperARC-seq Framework

The authors developed a quantitative metric φ combining three dimensions:

**Output classification:**
- Type 1: Correct solutions avoiding simple reproduction
- Type 2: Correct solutions using ordinal mappings
- Type 3: Correct solutions as direct prints
- Type 4: Incorrect outputs

The metric incorporates normalized Block Decomposition Method (nBDM) values to weight compression quality:

**φ = δ₁ρ₁ + (δ₂ρ₂)/10 + (δ₃ρ₃)/100**

Where δ represents harmonic means of compression ratios per type, and ρ represents output type percentages. This weighting deliberately privileges non-trivial solutions.

#### 2.4.1 SuperARC-seq Results

Testing on 100 binary sequences revealed stark performance differences:

**Top performers (binary sequences):**
- AIXI/BDM/CTM: φ = 1.000 (perfect score)
- ChatGPT-4.5: φ = 0.042 (only ordinal mappings)
- Claude-3.5: φ = 0.033
- Most other LLMs: φ ≈ 0.007–0.008

**Critical finding**: Most frontier LLMs produced print-only responses (ρ₃ ≈ 1.0), indicating zero compression and no pattern abstraction. Notably, "newer models—with the exception of Grok—demonstrated a degradation in performance" compared to earlier versions.

When integer sequences were tested, LLM performance improved dramatically—attributed to memorization of common mathematical sequences in training data. This finding established that binary sequences are essential for unbiased evaluation.

Bootstrap analysis demonstrated test robustness: confidence intervals narrowed as sample size increased from 25 to 100 sequences, validating the metric's reliability.

## 3 Discussion

The authors contextualize findings within Algorithmic Information Dynamics (AID), which combines statistical causal inference with Algorithmic Information Theory. Their fundamental claim: "recursive compression and optimal prediction go hand in hand," yet LLMs fail at both.

**Key theoretical contributions:**
- Mathematical proof (Section 7.1.4) demonstrates equivalence between compression and prediction via Martingale theory
- Establishes that abstraction capability reflects pattern identification through compression
- Shows planning/prediction skills depend on modeling capacities beyond training data

**Observed LLM deficiencies:**
- High dependency on predefined patterns
- Inability to synthesize novel solutions as complexity increases
- Reversion to trivial strategies (direct copying, simple brute-force approaches)
- Performance regression in newer versions despite improvements on human benchmarks
- Fundamental failure at model abstraction requiring "mathematical ingenuity"

**Critical observation**: LLMs demonstrate simultaneous regression in algorithmic reasoning while improving on human-centric benchmarks, suggesting these traditional metrics miss essential cognitive capabilities.

The authors argue that LLM developers increasingly adopt symbolic computation techniques (RAGs, KAGs, agentic workflows) without formal integration into core loss functions or solution-space exploration—addressing symptoms rather than causes.

**Fundamental conclusion**: Current LLMs "can mimic comprehension through retrieval, pattern matching, and Chain-of-Thought techniques," but "their capabilities remain bounded when tested against algorithmically complex sequences." True AGI/ASI requires autonomous strategy generation and flexible problem-solving beyond training distribution.

## Key Methodological Elements

**Testing framework foundations:**
- Grounded in CTM/BDM methods (previously validated on human cognition)
- Uses Algorithmic Information Theory as mathematical foundation
- Incorporates increasing complexity to prevent benchmark gaming
- Employs uncomputability to ensure open-endedness

**Comparison baseline**: AIXI/BDM/CTM represents theoretical optimal performance, instantiating "Universal AI" based on algorithmic probability principles.

## Implications

The research demonstrates that compression-based metrics fundamentally differ from statistical approaches. Shannon entropy and standard compression algorithms (GZIP, LZW) cannot capture algorithmic complexity required for genuine abstraction and prediction.

The authors contend that progress toward AGI/ASI demands "deeper integration" of symbolic approaches into core LLM functions, not peripheral augmentation through retrieval or agentic systems.
