---
description: MIA mixed-substrate deep-research agent memory paper — search trajectories become both workflow memory and Planner weight updates during test-time learning
source_snapshot: memory-intelligence-agent.md
ingested: 2026-04-11
type: scientific-paper
domains: [agent-memory, trace-derived-learning, test-time-learning, reinforcement-learning]
---

# Ingest: Memory Intelligence Agent

Source: memory-intelligence-agent.md
Captured: 2026-04-11
From: https://arxiv.org/html/2604.04503v2

## Classification

Type: scientific-paper — arXiv preprint with methodology, architecture, algorithm sketches, ablations, benchmark comparisons, and academic references.

Domains: agent-memory, trace-derived-learning, test-time-learning, reinforcement-learning

Author: Jingyang Qiao, Weicheng Meng, Yu Cheng, Zhihang Lin, Zhizhong Zhang, Xin Tan, Jingyu Gong, Kun Shao, and Yuan Xie — multi-institution team from East China Normal University, Shanghai Innovation Institute, Harbin Institute of Technology, Xiamen University, Shanghai AI Laboratory, and an independent researcher; worth attending to because the paper directly targets deep-research-agent memory and reports linked code/model/dataset artifacts.

## Summary

MIA proposes a Manager-Planner-Executor architecture for deep research agents. The Memory Manager stores compressed historical search trajectories as explicit workflow memory; the Planner uses retrieved workflows to generate search plans and is updated through RL; the frozen Executor carries out tool-using research under the plan. The distinctive mechanism is a bidirectional loop between non-parametric and parametric memory during test-time learning: multiple plan rollouts produce tool/reasoning trajectories, an LLM Judger or unsupervised reviewer/area-chair process labels them, successful and failed trajectories are compressed into workflow memory, and the Planner parameters are updated from the same reward signal. The paper argues this avoids long-context memory bloat and improves planning, with ablations suggesting that memory-as-planning-prior and test-time learning matter more than simply feeding memory to the Executor.

## Connections Found

The strongest connection is [trace-derived-learning-techniques-in-related-systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md): MIA extends that survey space as a mixed-substrate trajectory-derived learning system, because the same test-time trajectories promote into explicit workflow memory and Planner weights. It also extends [the fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md) by adding a design point where memory agency is distributed across Manager, Planner, Executor, Router, and Judger rather than held by one agent or one memory service. It exemplifies [agent memory is a crosscutting concern](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md): storage, retrieval/activation, learning, and action capacity are separate architectural roles. It extends [memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), since MIA learns a Planner policy from plan/trajectory rewards while trying to replace ground-truth labels with a weak unsupervised judge. Sibling sources include [Trajectory-Informed Memory Generation](./trajectory-informed-memory-generation-self-improving-agents.ingest.md), [AgeMem](./agentic-memory-learning-unified-long-term-and-short-term-memory-management.ingest.md), and [A-MEM](./a-mem-agentic-memory-for-llm-agents.ingest.md).

## Extractable Value

1. **Mixed-substrate trace learning** — MIA is a clean example where the same search trajectories become both inspectable-ish workflow memories and opaque Planner weight updates. This sharpens the substrate/timing matrix for continuous learning: trace-derived learning can run at test time and promote to artifacts, weights, or both. [deep-dive]

2. **Memory as a planning prior, not Executor context** — the ablation reports that "Only Memory" can underperform, while "Memory for Planner" improves results. The transferable insight is that stored trajectories may be more useful for shaping a plan than for bloating the actor's direct context. [quick-win]

3. **Contrastive workflow memory** — MIA selects the shortest successful trajectory and samples a failed trajectory, then stores them as positive/negative paradigms for future planning. This is a compact pattern worth comparing with ReasoningBank's success/failure extraction and trajectory-informed tips. [experiment]

4. **Weak-oracle design for open-world self-evolution** — the unsupervised reviewer/area-chair judge decomposes evaluation into logic, format, and factuality reviewers plus a meta-decision. This is directly relevant to oracle theory: it is an attempt to turn one unreliable scalar judge into a structured bundle of weaker checks. [deep-dive]

5. **Frequency reward as retrieval diversity pressure** — MIA retrieves memory by combining semantic similarity, value reward, and frequency reward. The frequency term explicitly rewards low-frequency memory units, a simple way to avoid always reusing the same high-similarity examples. [experiment]

6. **Planner/Executor stability split** — the Executor is frozen during test-time learning while the Planner updates. This is a useful architectural pattern: keep the operational tool-using service stable while learning the strategy generator around it. [just-a-reference]

## Limitations (our opinion)

**Paper-only ingest; code not inspected.** The snapshot links a GitHub repository, model, and dataset, but this ingest is based on the arXiv HTML text, not code review. Claims about what is implemented should stay at paper-confidence until the repository is reviewed separately.

**Benchmark-bound oracle evidence.** Most of the learning loop depends on correctness labels, LLM Judger outputs, or the proposed reviewer/area-chair surrogate. The paper reports benchmark improvements, but does not show that the unsupervised judge would remain reliable for open-ended research where there is no known answer and no clean factuality target.

**Opaque policy updates inherit the usual inspectability costs.** The Planner's learned improvements live in weights. That may be useful for speed and generalization, but the paper does not discuss rollback, debugging, provenance, or how to inspect a bad learned planning habit.

**The simpler-account question remains open.** MIA compares against several memory baselines and includes ablations, but the headline advantage could still partly come from extra rollout compute, any relevant plan examples, or a strong planner/router scaffold rather than the full bidirectional parametric/non-parametric memory loop.

**No mature memory lifecycle.** The Memory Manager stores compressed workflows and updates counts, but the paper does not offer a strong story for retiring stale workflows, detecting contradictory memories, or maintaining long-running memory quality beyond selective clearing after Planner training.

**Deep-research specificity limits reach.** The architecture is tuned around search trajectories, tool calls, and benchmarked question answering. Its strongest lessons transfer to agent learning loops, but the exact Manager-Planner-Executor setup may not transfer to KB curation, open-ended methodology work, or systems where the best output is not a final answer.

## Recommended Next Action

Update [trace-derived-learning-techniques-in-related-systems.md](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md): add MIA as a source-only mixed-substrate trajectory-run system. The note should say that MIA mines deep-research search trajectories into both structured workflow memory and Planner weight updates during test-time learning, and that its reviewer/area-chair unsupervised judge is a concrete weak-oracle attempt worth comparing against the survey's oracle bottleneck claim.
