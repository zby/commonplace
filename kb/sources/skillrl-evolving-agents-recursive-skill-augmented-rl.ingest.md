---
description: "SkillRL paper showing trajectory-distilled skill banks co-evolving with GRPO-trained agent policy, bridging readable skill artifacts and weight-based learning"
source_snapshot: "skillrl-evolving-agents-recursive-skill-augmented-rl.md"
ingested: "2026-06-30"
type: kb/sources/types/ingest-report.md
domains: [skill-learning, trace-derived-learning, reinforcement-learning, deploy-time-learning]
---

# Ingest: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

Source: [skillrl-evolving-agents-recursive-skill-augmented-rl.md](skillrl-evolving-agents-recursive-skill-augmented-rl.md)
Captured: 2026-06-30
From: https://arxiv.org/abs/2602.08234

## Classification

Type: scientific-paper -- arXiv preprint with a proposed framework, algorithm, benchmark results, ablations, implementation details, and appendices containing prompts and example skills.
Domains: skill-learning, trace-derived-learning, reinforcement-learning, deploy-time-learning
Author: multi-institution research team from UNC-Chapel Hill, University of Chicago, UCSD, NEC Labs America, UC Berkeley, and UC Santa Cruz; the evidence is useful but not yet independently reproduced in this KB.

## Summary

SkillRL proposes a recursive skill-augmented RL loop for LLM agents. It collects successful and failed trajectories, uses a teacher model to distill them into a hierarchical skill bank of general and task-specific natural-language skills, cold-start fine-tunes a base model to retrieve and apply those skills, and then runs GRPO while periodically adding or refining skills from validation failures. On ALFWorld, WebShop, and search-augmented QA benchmarks, the paper reports better success rates than prompt-based memory, vanilla RL, and memory-augmented RL baselines, plus lower prompt length than raw trajectory memory. The central contribution for this KB is the hybrid learning shape: trace-derived readable skills and policy weights co-evolve instead of treating memory as either passive retrieval context or opaque learned policy alone.

## Connections Found

SkillRL lands in the KB's trace-derived learning and deploy-time learning cluster. It supports [Distillation is transformation, not selection](../notes/distillation-is-transformation-not-selection.md) and [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md) because raw trajectories are transformed into named skills with principles and applicability conditions. It extends [Treat continual learning as substrate coevolution](../notes/treat-continual-learning-as-substrate-coevolution.md) by giving a concrete prose-plus-distributed-parametric loop: the skill bank remains readable prompt context while GRPO trains the policy to use it. It also compares directly with [SkillOpt](skillopt-executive-strategy-self-evolving-agent-skills.ingest.md), [Agent Workflow Memory](agent-workflow-memory.ingest.md), [Trajectory-Informed Memory Generation](trajectory-informed-memory-generation-self-improving-agents.ingest.md), [Agentic Memory](agentic-memory-learning-unified-long-term-and-short-term.ingest.md), [SkillWeaver](../agent-memory-systems/reviews/SkillWeaver.md), and [Amazon Science SAGE](../agent-memory-systems/reviews/amazon-science--SAGE.md). Relative to the self-evolver faithfulness paper, SkillRL is an important boundary case: condensed experience may be inert when merely injected, but it can become behavior-shaping when the policy is explicitly trained to retrieve and apply it.

## Extractable Value

1. **Skill banks can couple readable artifacts and policy learning** -- SkillRL's strongest theoretical value is the coevolution pattern: prose skills stay inspectable and retrievable, while model weights learn to consume them through cold-start SFT and GRPO. This is new relative to notes that mostly contrast readable artifacts against weight updates. [deep-dive]
2. **Failed trajectories become counterfactual skills, not discarded noise** -- the paper's differential processing turns failures into concise lessons naming failure point, flawed reasoning, corrective action, and prevention principle. That is a reusable trace-derived extraction shape for operational memory. [quick-win]
3. **Cold-start SFT is an activation bridge** -- simply providing skills is not enough; the model first needs demonstrations of retrieval, interpretation, and application before RL can optimize skill-augmented behavior. This sharpens the activation gap between stored memory and action. [experiment]
4. **Task-completion oracles make recursive skill evolution possible** -- ALFWorld, WebShop, and QA rewards supply the selection signal for both policy updates and validation-failure skill growth. This corroborates [Memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) while changing the retained substrate from opaque memory policy to a readable skill bank plus weights. [just-a-reference]
5. **Compression has to preserve actionability, not just reduce tokens** -- the reported context savings and ablations support skill distillation only because the skill format encodes action conditions and the policy is trained around it. This qualifies the "condensed experience can be inert" warning rather than contradicting it broadly. [deep-dive]
6. **Skill library lifecycle is still under-governed** -- SkillRL evolves skills, but the paper does not describe durable provenance, conflict handling, retirement, review status, or source spans for individual skills. That is exactly where KB-style governance remains relevant. [just-a-reference]

## Limitations (our opinion)

This is a new preprint, so the benchmark numbers should be treated as provisional until code and reproduction are inspected. The snapshot was captured from PDF text extraction, and tables, formulas, and figure layout contain artifacts; use the original PDF for precise numeric claims. The method is strongest where task success and validation failure are crisp enough to drive GRPO and skill evolution; it does not solve open-ended KB curation, research synthesis, or subjective advisory work where the oracle is weak. The results also bundle several interventions -- teacher distillation, hierarchical retrieval, cold-start SFT, GRPO, and dynamic skill evolution -- so the headline improvements should not be attributed to "skill memory" alone. Finally, the skill bank is readable in principle but not governed like a durable KB artifact: lineage, review, conflict, and retirement metadata are missing from the paper's design.

## Recommended Next Action

Write a note titled **Skill banks couple readable artifacts and policy learning**. It should use SkillRL as the main evidence, compare against SkillOpt, AgeMem, Agent Workflow Memory, SkillWeaver, and Amazon SAGE, and connect to [Treat continual learning as substrate coevolution](../notes/treat-continual-learning-as-substrate-coevolution.md), [Continual learning's open problem is behaviour, not knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md), and [Use Trace-Derived Extraction As Meta-Learning](../notes/agent-memory-requirements/use-trace-derived-extraction.md).
