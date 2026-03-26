---
source: https://arxiv.org/html/2512.04307v1
description: Benchmark showing LLM-based web agents fail badly under long context with injected irrelevant task sequences — success rates drop from 40-50% to under 10% at 150k tokens, with loop and lost-objective failures dominating; implicit RAG provides only modest relief.
captured: 2026-03-26
capture: web-fetch
type: academic-paper
---

# Evaluating Long-Context Reasoning in LLM-Based WebAgents

Author: Andy Chung, Yichi Zhang, Kaixiang Lin, Aditya Rawal, Qiaozi Gao, Joyce Chai
Source: https://arxiv.org/html/2512.04307v1
Date: December 3, 2025

## Abstract

This research introduces a benchmark for assessing how well LLM-based web agents reason across extended interaction histories. The team developed an evaluation framework simulating multi-session user interactions by injecting irrelevant task sequences between dependent subtasks, creating contexts from 25,000 to 150,000 tokens.

Testing four models — Claude-3.7, GPT-4.1, Llama 4, and o4-mini — revealed significant performance decline with increased context. Success rates drop from 40-50% in baseline conditions to less than 10% in long context scenarios.

The analysis identified primary failure modes: agents became trapped in loops and lost sight of original objectives. The researchers tested an implicit RAG approach generating task-relevant summaries, which provided modest improvements but did not resolve fundamental limitations.

## Key Findings

- Dramatic performance degradation as context length increases from 25k to 150k tokens
- Agents struggle with maintaining coherent task execution across extended interactions
- Current architectures lack robust mechanisms for long-term user session management

## Failure Modes (at 150k tokens)

- **Claude-3.7**: 16.4% false ends, 35% inefficient progress, 16.7% loops
- **GPT-4.1**: 6.9% false ends, 32.7% inefficient progress, 44.3% loops
- **o4-mini**: Outperforms other models despite similar challenges

## Proposed Solution

Implicit RAG (iRAG) breaks complex instructions into sub-instructions, generating task-relevant summaries to improve retrieval. Results show modest improvements though fundamental limitations in long context reasoning persist.

## Implications

Current state-of-the-art models struggle maintaining coherence across realistic long-term interactions, highlighting critical challenges for deploying WebAgents in realistic scenarios. The research underscores the need for enhanced memory architectures and planning capabilities.

## Publication Details

- **Status**: Accepted at NeurIPS 25 LAW Workshop
- **Subject Areas**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **DOI**: https://doi.org/10.48550/arXiv.2512.04307
