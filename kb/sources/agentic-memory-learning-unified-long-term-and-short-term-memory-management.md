---
source: https://arxiv.org/html/2601.01885v1
captured: 2026-03-08
capture: web-fetch
type: academic-paper
---

# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

Author: Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, Libing Wu (Alibaba Group, Wuhan University)
Source: https://arxiv.org/html/2601.01885v1
Date: 2025

## Abstract

This paper introduces AgeMem, a unified framework that integrates long-term memory (LTM) and short-term memory (STM) management directly into LLM agent policies. Rather than treating memory as external components, the system exposes memory operations as tool-based actions, enabling agents to autonomously decide when and how to store, retrieve, update, summarize, or discard information.

## Key Contributions

1. **Unified Memory Framework:** A single system managing both LTM and STM through learnable, tool-based actions instead of heuristic pipelines

2. **Three-Stage Progressive RL Strategy:** Agents first acquire LTM storage capabilities, then learn STM context management, finally coordinating both under full task settings

3. **Step-wise GRPO Mechanism:** Addresses sparse and discontinuous rewards from memory operations through group-normalized advantage broadcasting across all trajectory timesteps

## Core Technical Approach

### Memory Management Tools

The system provides six primary tools:
- **LTM operations:** Add, Update, Delete
- **STM operations:** Retrieve, Summary, Filter

### Problem Formulation

The agent observes state s_t = (C_t, ℳ_t, 𝒯) comprising conversation context, long-term memory store, and task specification. Actions span both language generation and memory operations, optimized through policy π_θ.

### Three-Stage Trajectory Structure

Each trajectory τ = (τ^(1), τ^(2), τ^(3)) includes:
- **Stage 1:** Casual interaction where agents identify salient information for LTM storage
- **Stage 2:** Context reset with distractors testing STM management through filtering/compression
- **Stage 3:** Formal task requiring coordinated retrieval and reasoning

### Reward Function Design

The composite reward combines:
- **Task completion reward** (R_task): LLM-based judgment of answer correctness
- **Context management reward** (R_context): Compression efficiency, preventive actions, information preservation
- **Memory management reward** (R_memory): Storage quality, maintenance operations, semantic relevance
- **Penalty terms:** Discourage context overflow and excessive interaction rounds

## Experimental Results

Evaluation across five benchmarks (ALFWorld, SciWorld, PDDL, BabyAI, HotpotQA):

- **Performance gains:** 23.52-49.59% improvement over no-memory baselines
- **Memory quality:** Higher semantic relevance of stored memories versus baselines
- **Context efficiency:** 3.1-5.1% token reduction while maintaining task performance
- **RL contribution:** 8.53-8.72 percentage point improvements from training strategy

## Notable Findings

The paper demonstrates that:
- Unified management outperforms independent LTM/STM optimization
- Tool usage increases meaningfully post-training (Add operations 0.92→1.64 on Qwen2.5-7B)
- Multi-component rewards accelerate convergence better than task-only signals
- The system generalizes across diverse task types and model backbones

## Limitations

The authors acknowledge that the fixed tool set, while effective, could support finer-grained control. Broader evaluation across additional task domains could strengthen empirical understanding.
