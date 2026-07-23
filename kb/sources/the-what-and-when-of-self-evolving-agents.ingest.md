---
description: "3×3 framework mapping self-evolving-agent updates across external files, harnesses, and model weights over task, session, and population horizons"
source_snapshot: "kb/sources/the-what-and-when-of-self-evolving-agents.md"
ingested: "2026-07-23"
type: kb/sources/types/ingest-report.md
domains: [self-evolving-agents, continual-learning, deploy-time-learning, agent-harness]
---

# Ingest: The What & When of Self-Evolving Agents

Source: kb/sources/the-what-and-when-of-self-evolving-agents.md
Captured: 2026-07-23
From: https://xinmingtu.cn/blog/2026/self-evolving-agents/

## Classification

Genre: conceptual-essay -- a framework essay that organizes named systems and mechanisms but does not present a controlled experiment or formal evaluation.
Domains: self-evolving-agents, continual-learning, deploy-time-learning, agent-harness
Author: Xinming Tu; the page is a dated technical blog essay with a broad appendix and explicit acknowledgement of readers, but the source's claims remain authorial synthesis rather than independently validated results.

## Summary

The essay proposes a 3×3 map of self-evolving agents: three update substrates (external files, the agent harness, and model weights) crossed with three persistence horizons (single session, across sessions, and across users). It then reframes those horizons around the agent as intra-task, inter-task, and inter-agent evolution, and describes a possible consolidation path from task-local artifacts to reusable harness logic to future model weights. The useful contribution is vocabulary and boundary-setting: files can become harness logic when runtime discovery and routing make them operative; deployment becomes part of the training loop; and recursive self-improvement is the same experience → state → behaviour loop aimed at AI development. The appendix adds mechanisms and caveats for memory, dynamic orchestration, test-time adaptation, skills, workflow optimization, shared commons, platform flywheels, and checkpoint bootstrapping.

## Connections Found

This is a conceptual anchor for the KB's deploy-time-learning and self-improvement-profile threads. It gives [Continual learning's open problem is behaviour, not knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) a compact substrate-and-horizon taxonomy, and it complements [Deploy-time learning is the missing middle](../notes/deploy-time-learning-is-the-missing-middle.md) by placing durable files and harnesses between ephemeral context and weight updates. Its orthogonal matrix supports [A self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md), while [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) and [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) supply the evaluation condition the taxonomy lacks: retained state must be causally used and diagnostically useful. [Meta-Harness: End-to-End Optimization of Model Harnesses](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) is a concrete, empirically stronger instance of one matrix cell.

## Extractable Value

1. **Substrate × horizon is a retrieval-ready vocabulary for self-evolution.** It separates where a change lands from how long it persists, avoiding a single “more autonomous” ladder and giving the KB a compact way to classify files, workflows, skills, harness updates, and weight updates. [quick-win]

2. **The agent-centered reframe adds task, task-family, and peer triggers.** Translating product surfaces into intra-task, inter-task, and inter-agent horizons makes environmental feedback, domain recurrence, and peer discovery explicit as different learning triggers. [quick-win]

3. **Capability consolidation is a hypothesis about promotion, not an automatic pipeline.** The proposed path from task-local artifact to harness logic to model weights suggests a focused deep dive on promotion gates, portability, generalization, provenance, and rollback. [deep-dive]

4. **The file-to-harness boundary is operationally important.** An artifact changes category when runtime discovery, loading, and routing make it part of future control flow; this gives the readable-artifact and skill-library work a concrete boundary to test. [experiment]

5. **The essay itself states the governance gap.** Shared skill commons, platform defaults, and checkpoint bootstrapping require provenance, sandboxing, evaluation, rollout control, and human approval; this aligns with the KB's claim that automation is bounded by verification rather than by naming a loop. [quick-win]

## Limitations (our opinion)

This is a conceptual essay, so the matrix is not an empirically established taxonomy. The article does not provide operational tests for when a file becomes harness logic, how much persistence qualifies as “across sessions,” or when a discovery has generalized enough to promote inward toward weights. Its examples are curated anchors and appendix references with mixed evidential status; naming a system in a cell does not demonstrate that the system satisfies the mechanism described there.

The consolidation path is especially easy to over-read. Portability, repeated success, and training-data availability do not by themselves establish generalization, causal faithfulness, or safe promotion. The essay acknowledges that humans still design rewards, curate data, evaluate regressions, and approve checkpoints, but it does not quantify those costs or specify governance interfaces. Finally, the broad use of “self-evolving” risks treating storage, runtime adaptation, engineering updates, and model learning as equivalent unless the later action change and its evaluation are made explicit; [Continual learning's open problem is behaviour, not knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) is the stronger guardrail here.

## Recommended Next Action

Update [A self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md) with a compact substrate × persistence table from this essay, while adding faithfulness/diagnostic evidence and promotion gates as separate profile fields so the taxonomy is not mistaken for proof of learning or autonomy.
