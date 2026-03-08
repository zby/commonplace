---
source_snapshot: agentic-memory-learning-unified-long-term-and-short-term-memory-management.md
ingested: 2026-03-08
type: scientific-paper
domains: [agent-memory, reinforcement-learning, context-management, llm-agents]
---

# Ingest: Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for LLM Agents

Source: agentic-memory-learning-unified-long-term-and-short-term-memory-management.md
Captured: 2026-03-08
From: https://arxiv.org/html/2601.01885v1

## Classification

Type: scientific-paper -- preprint (arXiv, January 2025) with formalized problem statement, multi-stage RL training methodology, ablation studies, and evaluation across five benchmarks (ALFWorld, SciWorld, PDDL, BabyAI, HotpotQA) on multiple model backbones.

Domains: agent-memory, reinforcement-learning, context-management, llm-agents

Author: Yi Yu, Liuyi Yao, Yuexiang Xie et al. (Alibaba Group, Wuhan University). Active in LLM agent infrastructure. The Alibaba affiliation signals production-scale orientation; the multi-backbone evaluation (Qwen, Llama) suggests practical deployment concerns rather than benchmark-only research.

## Summary

AgeMem proposes unifying long-term memory (LTM) and short-term memory (STM) management as learnable tool-based actions within an LLM agent's policy, trained through reinforcement learning. Instead of treating memory as an external service or relying on in-context instructions, the system exposes six memory operations (Add, Update, Delete for LTM; Retrieve, Summary, Filter for STM) and trains the agent to use them through a three-stage progressive RL strategy: first learning LTM storage, then STM context management, then coordinating both. A step-wise GRPO mechanism addresses sparse rewards from memory operations. Results show 23-49% improvement over no-memory baselines, 3-5% token reduction in context, and meaningful RL contribution (8-9 percentage points) beyond the base model's capability.

## Connections Found

The `/connect` discovery identified six substantive connections and one synthesis opportunity:

**Memory architecture contrast.** AgeMem's LTM/STM distinction maps onto but diverges from the KB's [three-space memory model](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md). The three-space model separates by content type (semantic/episodic/procedural); AgeMem separates by access pattern (persistent store vs active context). AgeMem's unified RL-trained management is evidence against the three-space separation claim -- the RL agent learns to coordinate across spaces rather than keeping them structurally isolated. However, AgeMem's benchmarks test task completion, not the organizational failure modes the three-space model predicts.

**Context engineering evidence.** AgeMem's STM operations (Retrieve, Summary, Filter) are literally context management -- the agent learns to compress and filter its working context. The 3.1-5.1% token reduction while maintaining performance directly exemplifies [context efficiency as a central design concern](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), providing empirical data that learned context management can outperform heuristic approaches.

**Different bet on automation.** The KB's framework for [automating KB learning](../notes/automating-kb-learning-is-an-open-problem.md) envisions a boiling cauldron of proposed mutations with human review gates. AgeMem takes a fundamentally different approach: train the agent's policy through RL to manage its own knowledge store, removing the human from the loop entirely. This contrasts with the deploy-time learning framework's emphasis on [inspectable, versioned artifacts](../notes/stabilisation-during-deployment-is-continuous-learning.md) -- AgeMem's learned memory policy is opaque.

**Memory agency mechanism spectrum.** Against the [comparative review of agentic memory systems](./agentic-memory-systems-comparative-review.md), AgeMem fills a new cell: "RL-trained self-managed." This extends beyond Letta (in-context tool descriptions) and A-MEM (heuristic pipelines) to a learned policy. Combined with [Letta](./letta-memgpt-stateful-agents.ingest.md) and [A-MEM](./a-mem-agentic-memory-for-llm-agents.ingest.md), this creates a three-point spectrum of memory agency mechanisms, each with different trade-offs in inspectability, adaptability, and training cost.

## Extractable Value

1. **Three-stage curriculum for memory training** (LTM first, STM second, coordination third): a progressive RL strategy that decomposes a complex multi-objective problem into learnable stages. No parallel exists in the KB for curriculum design in agent training. The principle -- train simpler capabilities first, compose later -- may apply to skill acquisition beyond memory. [deep-dive]

2. **Unified management outperforms independent optimization**: the paper shows that jointly training LTM and STM management outperforms optimizing each independently. This is a concrete data point against architectural separation of memory spaces, relevant to the three-space model debate. [quick-win]

3. **Composite reward design for memory operations**: the four-component reward (task completion + context management + memory management + penalties) addresses the sparse reward problem in memory operations. The step-wise GRPO mechanism that broadcasts advantages across all trajectory timesteps is a specific technique for credit assignment when the beneficial action (storing a memory) is temporally distant from the reward (using it successfully). [just-a-reference]

4. **STM as learnable context management**: the Retrieve/Summary/Filter tool set for STM is effectively a learned context engineering toolkit. The finding that trained agents increase tool usage post-training (Add operations 0.92 to 1.64) suggests that base models underuse memory operations and RL training can close this gap. [experiment]

5. **RL contribution quantified**: 8.53-8.72 percentage point improvement from the training strategy specifically, separable from base model capability. This quantifies the value of learned memory management over instruction-following, directly comparable to A-MEM's heuristic approach and Letta's in-context approach. [just-a-reference]

6. **Weight-based vs artifact-based learning tension**: AgeMem represents the opposite pole from deploy-time learning. Where stabilisation accumulates inspectable artifacts, AgeMem trains opaque policy weights. The trade-off is adaptability (RL-trained policies generalize across tasks) vs inspectability (artifacts can be reviewed, rolled back, debugged). This tension is not yet named in the KB. [deep-dive]

## Notes Written

- [Memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — deep-dive on extractable values 1, 4, 6: analyzes AgeMem through the bitter-lesson boundary and learning-theory frameworks, showing that the RL success depends on task-completion oracles the KB lacks

## Recommended Next Action

Update the [agentic memory systems comparative review](./agentic-memory-systems-comparative-review.md) to add AgeMem as the RL-trained self-managed entry, specifically in the agency model dimension (Section 2) and the curation operations dimension (Section 5). AgeMem fills a gap the current review identifies but doesn't populate: the "who decides what to remember" question now has a fourth answer beyond developer-managed, agent-instructed, and human-collaborative -- "RL-trained agent policy." The update should note that AgeMem's approach trades the inspectability that deploy-time learning provides for the adaptability that weight-based training enables, sharpening the strategic question the review already raises about automation without sacrificing navigability.
