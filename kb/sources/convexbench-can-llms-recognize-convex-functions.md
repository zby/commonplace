---
source: https://arxiv.org/html/2602.01075v2
captured: 2026-03-04
capture: web-fetch
type: academic-paper
---

# ConvexBench: Can LLMs Recognize Convex Functions?

Author: Yepeng Liu, Yu Huang, Yu-Xiang Wang, Yingbin Liang, Yuheng Bu
Source: https://arxiv.org/html/2602.01075v2
Date: February 1, 2026 (v1); February 4, 2026 (v2)
arXiv: 2602.01075 (cs.AI)
DOI: https://doi.org/10.48550/arXiv.2602.01075

## Abstract

This paper introduces ConvexBench, a mechanically verifiable benchmark for evaluating whether large language models can identify convexity in deeply composed symbolic functions. Experiments reveal a sharp compositional reasoning gap: performance drops from F1=1.0 at depth 2 to approximately 0.2 at depth 100. Two failure modes are identified: parsing failures and lazy reasoning. The authors propose agentic divide-and-conquer frameworks that employ external parsing tools and recursive reasoning with focused context, achieving F1=1.0 at depth 100.

## Introduction

As LLMs are positioned for research automation, their ability to understand symbolic expressions becomes critical. Many practical optimization problems involve deeply compositional objectives—functions built through repeated transformations. Analyzing convexity in such expressions requires verifying conditions at every composition level.

The paper asks: "Can LLMs recognize convex functions as composition depth increases?" To answer this, they introduce ConvexBench, generating functions using disciplined convex programming (DCP) atoms with certified composition rules. This enables mechanical label verification and controllable complexity.

## Key Findings

**Performance degradation**: One-shot reasoning achieves perfect F1-scores on shallow expressions but "performance degrades rapidly as compositional depth increases, beginning as early as depth 5" and dropping to 0.2 at depth 100.

**Failure modes identified**:

1. **Parsing failures**: Models lose track of parentheses and operator scope, misidentifying sub-expressions
2. **Lazy reasoning**: Models rely on shallow heuristics rather than step-by-step verification, with token usage plateauing beyond depth thresholds

## Proposed Solutions

The authors develop three progressively refined approaches:

1. **One-shot Reasoning with Decomposition**: Offloads expression parsing to external tools, providing explicit abstract syntax trees (ASTs)
2. **Agentic Reasoning**: Enforces recursive step-by-step verification of each intermediate sub-expression
3. **Agentic Reasoning with Focused Context**: Prunes irrelevant historical context, keeping only direct dependencies for each sub-task

## Experimental Results

Testing on frontier models (GPT-5, Gemini-2.5-Pro, Qwen3-8B/30B):

- One-shot reasoning collapses at depth 100 (F1≈0.2)
- Agentic framework with focused context achieves F1=1.0 across all depths
- Improvements: +0.79 (GPT-5), +0.54 (Gemini), +0.82 (Qwen3-30B) over baseline

**Error analysis**: As depth increases, models increasingly misclassify convex/concave functions as "neither"—the safest prediction requiring only one constraint violation.

## Context and Long-Horizon Reasoning

A critical finding: even with token counts (5,331 at depth 100) far below LLM context limits (128k+), models degrade substantially. This reveals a distinction between "long-context capability" (handling token length) and "long-horizon reasoning capability" (maintaining correctness over dependent steps).

## Ablation Studies

- Finer decomposition (10-character sub-functions) consistently outperforms coarser decomposition
- Agentic reasoning scales near-linearly with depth, while one-shot shows plateau
- Recursive steps increase from 22 to 146 at depth 100, with performance gains at each level

## Practical Implications

1. Complex symbolic reasoning benefits from delegating parsing to deterministic external tools
2. Recursive scaffolding provides substantial gains for smaller models, enabling previously unsolved tasks
3. Framework design should be capability-aware: stronger models gain from decomposition alone; weaker models need full agentic recursion

## Conclusion

The research demonstrates that current LLMs exhibit systematic brittleness in compositional reasoning despite operating well within context windows. "Models condition on an expanding history of intermediate sub-functions," creating a reasoning-horizon bottleneck beyond token-level effects. Agentic frameworks with focused context effectively address this by enforcing verification while managing attention distribution.
