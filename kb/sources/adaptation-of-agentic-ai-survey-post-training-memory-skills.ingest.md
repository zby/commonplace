---
description: "Survey mapping agentic adaptation across A1/A2 agent training, T1/T2 tool adaptation, memory, skills, and dynamics-aware evaluation"
source_snapshot: "adaptation-of-agentic-ai-survey-post-training-memory-skills.md"
ingested: "2026-06-09"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [agentic-adaptation, learning-theory, agent-memory, evaluation-methodology]
---

# Ingest: Adaptation of Agentic AI

Source: adaptation-of-agentic-ai-survey-post-training-memory-skills.md
Captured: 2026-04-27
From: https://arxiv.org/html/2512.16301v3

## Classification

Type: scientific-paper -- arXiv v3 survey/preprint with a formal taxonomy, extensive literature review, citations, comparative tables, and evaluation recommendations, but no new original experiment.
Domains: agentic-adaptation, learning-theory, agent-memory, evaluation-methodology
Author: Pengcheng Jiang, Jiacheng Lin, Zhiyi Shi, Zifeng Wang, Luxi He, Yichen Wu, Ming Zhong, Peiyang Song, Qizheng Zhang, Heng Wang, Xueqiang Xu, Hanwen Xu, Pengrui Han, Dylan Zhang, Jiashuo Sun, Chaoqi Yang, Kun Qian, Tian Wang, Changran Hu, Manling Li, Quanzheng Li, Hao Peng, Sheng Wang, Jingbo Shang, Chao Zhang, Jiaxuan You, Liyuan Liu, Pan Lu, Yu Zhang, Heng Ji, Yejin Choi, Dawn Song, Jimeng Sun, and Jiawei Han; the multi-institution author list includes established AI, ML, NLP, security, and data-mining researchers, so the paper is worth treating as a field-map signal rather than a single-system report.

## Summary

The paper surveys adaptation in agentic AI under a four-paradigm taxonomy: A1 adapts the agent from tool-execution feedback, A2 adapts the agent from final-output or holistic rewards, T1 trains agent-agnostic tools, and T2 adapts tools under supervision from a fixed agent. Its most relevant contribution for this KB is not any one method but the organizing frame: post-training, memory, skill libraries, retrievers, planners, subagents, and tool ecosystems are all adaptation surfaces. The survey also argues that evaluation must be paradigm-aware, component-counterfactual, and dynamics-aware, because endpoint success rates hide data efficiency, forgetting, co-adaptation instability, safety regression, and tool-vs-agent attribution.

## Connections Found

The regenerated connect report (2026-06-09) confirms the source's primary landing zone has since been realized as a note. The prior report's recommended synthesis — that agentic adaptation taxonomies need an artifact-substrate axis — was written as [The adaptation survey corroborates memory requirements but misses artifact governance](../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md), which already authors an `evidence` link back to this ingest report. No new synthesis note is required for that thread.

The wider cluster the report found is intact. The source **compares with** [Continual learning's open problem is behaviour, not knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md), [Deploy-time learning is the missing middle](../notes/deploy-time-learning-is-the-missing-middle.md), and [Treat continual learning as substrate coevolution](../notes/treat-continual-learning-as-substrate-coevolution.md): the paper gives a mainstream ML taxonomy for agent/tool optimization, while the KB gives an artifact-substrate and role taxonomy that better captures readable repo artifacts. It **evidences** [Memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) and [Agent memory is a crosscutting concern, not a separable niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) by classifying memory according to update mechanism rather than treating it as one pluggable subsystem. It **compares with** [Skills derive from methodology through distillation](../notes/skills-derive-from-methodology-through-distillation.md) and [Skills are instructions plus routing and execution policy](../notes/skills-are-instructions-plus-routing-and-execution-policy.md): the paper covers acquisition and reuse of skill libraries, while the KB covers methodology distillation and harness binding. It also **evidences** [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) and **extends** [Reliability dimensions map to oracle-hardening stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) with adaptation-specific evaluation requirements. The report also surfaces two `agent-memory-systems` cross-references — [What the matrix shows across 129 agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) and [Trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — whose mechanism-based classifications parallel the survey's T1/T2 split.

The report's main non-actionable maintenance signal: [research/adaptation-agentic-ai-analysis.md](../notes/research/adaptation-agentic-ai-analysis.md) is an extended analysis of this exact paper but cites only a bare external arXiv URL with no link to the local snapshot or ingest report, breaking local lineage tracking. It also carries thin frontmatter (only `type:`). Mentioned here as context; the citation/frontmatter fix belongs to a maintenance pass, not this ingest.

## Extractable Value

1. **Optimization locus and supervision signal are not enough; artifact substrate is the missing axis.** High reach. A1/A2/T1/T2 cleanly separates agent-vs-tool and execution-vs-output signals, but it hides whether the durable learned result lives in weights, external tools, memory stores, prose policies, or symbolic artifacts. This is exactly where the KB's substrate-coevolution frame adds value. [quick-win]

2. **Memory and skills are adaptation mechanisms, not side modules.** High reach. The survey's surprising useful move is to place adaptive memory, skill libraries, retrievers, and subagents inside the same adaptation map as post-training. This supports the KB claim that memory crosses storage, context engineering, and learning, while adding a broader literature vocabulary for tool-side adaptation. [quick-win]

3. **T2 names a common pattern: keep the agent fixed and adapt its environment.** High reach. The T2 category captures retriever tuning, search subagents, memory-update modules, and skill libraries trained from frozen-agent feedback. That maps cleanly onto many practical agent systems where changing the model is expensive but changing the surrounding artifacts or tools is cheap. [experiment]

4. **Adaptation evaluation needs component counterfactuals.** High reach. The paper's strongest evaluation prescription is to hold the agent fixed while swapping tools, or ablate tool use while holding the agent fixed, so gains can be attributed to the adapted component rather than endpoint task success. This sharpens the KB's oracle/evaluation notes with a concrete reporting standard. [quick-win]

5. **Endpoint metrics erase adaptation dynamics.** Medium-high reach. Data efficiency, retention-set performance, safety-performance trajectories, and co-adaptation stability are different questions from final accuracy. This extends reliability evaluation from static "does it work?" checks to "how did it learn, what did it forget, and what failure window appeared while learning?" [experiment]

6. **Skill libraries have two separable questions: how skills are acquired and how skills are invoked.** Medium reach. The survey focuses on acquisition routes -- demonstration, reflection, exploration, RL, and programmatic skill induction -- while the KB focuses on discovery, invocation, execution policy, and methodology provenance. Keeping those questions separate prevents "skill" from becoming a vague label. [quick-win]

7. **The simpler account is oracle strength plus modular update cost.** The four paradigms sound like a full taxonomy, but many trade-offs reduce to two simpler forces: where the strongest feedback signal exists, and which component can be updated cheaply without breaking the rest of the system. The taxonomy is useful when it preserves those mechanisms; it becomes easier to vary when used as field-labeling alone. [just-a-reference]

## Limitations (our opinion)

This is a survey, not a primary empirical result. Its comparative claims depend on heterogeneous papers with different backbones, tasks, budgets, and evaluation protocols. Treat the taxonomy and literature map as valuable; treat quantitative cross-paradigm comparisons as prompts for follow-up, not settled evidence.

The A1/A2/T1/T2 taxonomy under-describes readable artifact learning. It sees memory and skills, but mostly through ML/tool-adaptation categories. Commonplace's central mechanisms -- maintained notes, instructions, schemas, tests, indexes, and skills as repo artifacts -- fit awkwardly unless an additional artifact-substrate axis is added.

The central claim is moderately easy to vary. One could redraw the same literature by feedback granularity, training time vs deploy time, component ownership, or artifact inspectability and still recover many of the same recommendations. The hard-to-vary part is narrower: adaptation decisions depend on what signal is available, what component is cheap to update, and whether evaluation can attribute gains to that component.

The evaluation section is stronger as an agenda than as a solved method. Counterfactual component swaps assume components are approximately separable, but adapted agents may change behavior when tools change. Living benchmarks need generated tasks that remain solvable, discriminative, and non-degenerate; the paper acknowledges this but does not solve the verifier problem.

Safety discussion is necessarily fast-moving. The paper names unsafe exploration, reward hacking, safety regression, and parasitic tool adaptation, but these risks depend on current protocol ecosystems and threat models. Use it for risk categories, not for durable prevalence estimates.

## Recommended Next Action

The artifact-substrate synthesis recommended in the original report has been written ([The adaptation survey corroborates memory requirements but misses artifact governance](../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md)), so that thread is closed. The one remaining unrealized synthesis worth one focused note is the evaluation thread: **"Adaptation evaluation must be component-counterfactual and dynamics-aware"**, connecting [Reliability dimensions map to oracle-hardening stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [Evaluate memory by effects](../notes/agent-memory-requirements/evaluate-memory-by-effects.md), and [Memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md). It would argue that endpoint success rates hide data efficiency, forgetting, co-adaptation instability, and tool-vs-agent attribution, so KB-relevant evaluation needs component-counterfactual swaps and dynamics-aware trajectories rather than static "does it work?" checks. This is the highest-value extractable item (#4 and #5) not yet captured as a standalone note.
