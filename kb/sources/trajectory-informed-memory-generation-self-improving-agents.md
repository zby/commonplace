---
source: https://arxiv.org/html/2603.10600v1
description: IBM Research framework that extracts three categories of actionable tips (strategy, recovery, optimization) from agent execution trajectories and injects them at runtime — evaluated on AppWorld showing up to 14.3 pp gains in scenario goal completion.
captured: 2026-03-13
capture: web-fetch
type: academic-paper
---

# Trajectory-Informed Memory Generation for Self-Improving Agent Systems

Author: Gaodan Fang, Vatche Isahagian, K. R. Jayaram, Ritesh Kumar, Vinod Muthusamy, Punleuk Oum, Gegi Thomas (IBM Research)
Source: https://arxiv.org/html/2603.10600v1
Date: March 11, 2026

## Abstract

This paper presents a framework for extracting actionable learnings from LLM-powered agent execution trajectories to improve future performance. The system analyzes agent reasoning patterns, identifies causal decision chains, and generates three types of guidance: strategy tips from successful patterns, recovery tips from failure handling, and optimization tips from inefficient but successful executions. Evaluation on AppWorld benchmark demonstrates consistent improvements, with up to 14.3 percentage point gains in scenario goal completion on held-out tasks.

## Key Contributions

1. **Trajectory Intelligence Extraction** – Semantic analysis of agent reasoning patterns including analytical thoughts, planning, validation behaviors, and self-correction sequences

2. **Decision Attribution Analysis** – Distinguishes immediate, proximate, and root causes of failures while identifying recovery patterns and inefficiencies

3. **Contextual Learning Generation** – Produces three categorized tip types: strategy, recovery, and optimization guidance with concrete implementation steps

4. **Adaptive Memory Retrieval** – Combines semantic similarity with metadata filtering for context-aware tip injection into agent prompts

## Framework Overview

The system operates as a three-phase pipeline:

### Phase 1: Trajectory Analysis and Tips Extraction

Analyzes completed agent trajectories to identify causal decision chains. Extracts tips at two granularities:
- **Task-level tips** capture holistic end-to-end patterns
- **Subtask-level tips** decompose into reusable logical phases for cross-task transfer

The Trajectory Intelligence Extractor identifies four reasoning categories: analytical thoughts, planning thoughts, validation thoughts, and reflection thoughts. It recognizes patterns like validation behaviors, error recognition, and API discovery through semantic understanding rather than keyword matching.

### Phase 2: Tip Storage and Management

Generalizes subtask descriptions, clusters semantically similar tips, and consolidates redundant guidance through LLM-based merging. Stored entries include vector embeddings for semantic search and structured metadata for filtering.

### Phase 3: Runtime Retrieval

Two retrieval strategies at agent invocation:
- **Cosine similarity retrieval** – Fast, embedding-based matching requiring no LLM calls
- **LLM-guided selection** – Richer task context reasoning with metadata filtering and category prioritization

Retrieved tips are injected into the agent prompt as actionable guidelines before reasoning begins.

## Evaluation Results

Tested on AppWorld benchmark with ReAct-style agent using GPT-4:

### Held-Out Test Results (Unseen Tasks)

**Subtask-level tips with LLM-guided selection (best configuration):**
- Task Goal Completion: 73.2% vs. 69.6% baseline (+3.6 pp)
- Scenario Goal Completion: 64.3% vs. 50.0% baseline (+14.3 pp)

**Difficulty-based improvements:**
- Difficulty 1: +1.7 pp TGC, +10.5 pp SGC
- Difficulty 2: +4.1 pp TGC, no SGC change
- Difficulty 3: +4.7 pp TGC, +28.5 pp SGC (149% relative increase)

### Configuration Insights

- **Tip granularity drives TGC** – Subtask-level tips outperform task-level regardless of retrieval strategy
- **Retrieval strategy drives SGC** – LLM-guided selection dramatically improves cross-variant consistency
- **Source partition benefits** – Larger gains when encountering similar tasks again (+4.4 pp TGC on train, +12.3 pp on dev)

## Problem Motivation

Current agent systems suffer from "amnesia" – lacking systematic mechanisms to learn from execution experiences. Existing approaches fall short:

- **Rule-based systems** require manual encoding and cannot adapt to unforeseen patterns
- **Prompt engineering** provides generic rather than experience-specific guidance
- **Generic memory systems** (Mem0, Letta) store conversational facts but lack understanding of execution patterns, causal analysis of failures, or structured learning extraction

The framework addresses these by extracting semantic learnings with provenance, performing causal attribution, and retrieving contextually relevant guidance.

## Related Work

The work relates to:
- **Memory taxonomies** – Recent surveys identify limitations of overly simplistic representations and fragmented evaluation
- **Semantic memory systems** – Mem0 and A-MEM store facts but not procedural/experiential knowledge
- **Trajectory learning** – AWM and Memp extract workflows/procedures; ReasoningBank distills strategies; ACE evolves context playbooks
- **Empirical foundations** – Studies show agents closely follow retrieved experiences, making mismatched retrieval problematic

## Conclusions

The framework enables agents to continuously improve from operational experience through structured trajectory analysis and adaptive retrieval. Results demonstrate particular effectiveness on complex, multi-step tasks requiring sophisticated planning and error recovery. Authors note extension to multi-agent systems and evaluation across additional model families as future work.

---

**License:** CC BY 4.0
