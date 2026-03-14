---
source: https://arxiv.org/html/2603.10062v1
description: Position paper reframing multi-agent memory management through a computer architecture lens — proposes shared vs. distributed memory paradigms, a three-layer hierarchy (I/O, cache, memory), and identifies memory consistency as the most urgent unresolved challenge for scalable multi-agent systems.
captured: 2026-03-13
capture: web-fetch
type: academic-paper
---

# Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead

Author: Zhongming Yu, Naicheng Yu, Hejia Zhang, Wentao Ni, Mingrui Yin, Jiaying Yang, Yujie Zhao, Jishen Zhao (University of California, San Diego; Georgia Institute of Technology)
Source: https://arxiv.org/html/2603.10062v1
Date: March 9, 2026

---

## Abstract

This position paper reframes multi-agent memory management through a computer architecture lens. It proposes distinguishing shared versus distributed memory paradigms, introduces a three-layer hierarchy (I/O, cache, memory), and identifies critical protocol gaps. The authors argue that multi-agent memory consistency represents the most urgent unresolved challenge for building scalable, dependable multi-agent systems.

## Why Memory Matters

Modern LLM agents face evolving complexity:
- Longer context windows requiring multi-hop reasoning
- Multimodal inputs (images, videos, diagrams)
- Structured executable traces
- State tracking in customized environments

Context is no longer static; it functions as a dynamic system with bandwidth, caching, and coherence demands.

## Memory Architectures

The paper identifies two fundamental approaches:
- **Shared memory:** All agents access a common pool but require coherence support
- **Distributed memory:** Each agent maintains local memory with selective synchronization

Most practical systems exist between these extremes.

## Three-Layer Hierarchy

- **I/O layer:** Information ingestion/emission interfaces
- **Cache layer:** Fast, limited-capacity reasoning memory
- **Memory layer:** Large-capacity, persistent storage systems

## Protocol Gaps

Two critical missing elements:

1. **Cache sharing protocol:** Systems lack principled approaches for agents to share and reuse cached artifacts across systems
2. **Memory access protocol:** Frameworks don't standardize permissions, scope, and granularity for shared memory access

## Multi-Agent Consistency Challenge

The authors highlight that agent systems require consistency models analogous to hardware architecture. Key requirements include:
- "Read-time conflict handling under iterative revisions"
- Update visibility and ordering determining when writes become observable

This challenge is harder than classical settings because artifacts are heterogeneous and conflicts carry semantic weight.

## Conclusion

Current agent memory systems resemble informal human memory. Advancing toward reliable multi-agent systems requires better hierarchies, explicit protocols, and principled consistency models maintaining coherent shared context.
