---
source: https://arxiv.org/html/2604.02280v1
description: Adaptive budgeted forgetting framework for long-horizon conversational agents — relevance scoring (recency, frequency, semantic alignment) plus constrained optimization to prune memory while reducing false memory propagation.
captured: 2026-04-04
capture: web-fetch
type: snapshot
tags: [academic-paper]
---

# Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency

Author: Payal Fofadiya, Sunil Tiwari
Source: https://arxiv.org/html/2604.02280v1
Date: 2026

## Abstract

Long-horizon conversational agents require persistent memory for coherent reasoning, yet uncontrolled accumulation causes temporal decay and false memory propagation. This work introduces an adaptive budgeted forgetting framework that regulates memory through relevance-guided scoring and bounded optimization. The approach integrates recency, frequency, and semantic alignment to maintain stability under constrained context, demonstrating improved long-horizon performance while reducing false memory behavior.

## Key Contributions

The paper addresses how to introduce controlled forgetting into autonomous agents while preserving reasoning accuracy under constrained memory budgets. Three research questions guide the investigation:

1. How can controlled forgetting under fixed memory budgets maintain long-horizon reasoning on benchmarks like LOCOMO and LOCCO?
2. What impact does relevance-driven memory pruning have on false memory rates in multi-domain settings?
3. How does adaptive decay-based memory selection influence memory-performance tradeoffs across extended interactions?

## Proposed Methodology

The framework organizes interaction history into multi-layer memory components with a relevance-guided control module. Key components include:

**Relevance Scoring:** Each memory element receives an importance score integrating recency, usage frequency, and semantic alignment with current queries.

**Constrained Forgetting:** Memory selection is formulated as a maximization problem: "retain high-importance elements while discarding low-impact ones under budget limits."

**Adaptive Decay:** Temporal decay prevents abrupt forgetting, using exponential decay where older memories gradually reduce in priority.

## Experimental Evaluation

The study evaluates three benchmarks:

- **LOCOMO:** Dialogues exceeding 600 turns measuring multi-hop and temporal reasoning
- **LOCCO:** 3,080 dialogues examining long-term memory persistence across temporal stages
- **MultiWOZ 2.4:** Task-oriented dialogue accuracy with false memory rate metrics

Results demonstrate improved long-horizon F1 scores beyond baseline levels, higher retention consistency, and reduced false memory behavior without increasing context usage.

## Key Findings

The framework achieves "performance stability under bounded memory growth" while prior approaches either preserved performance with unrestricted accumulation or reduced memory at the cost of degradation. Controlled regulation balances retention quality and efficiency, confirming that "selective retention mitigates false memory while preserving reasoning consistency."
