---
description: "Repeated-run and shuffled-order evidence that textual-memory agents amplify variance and can turn a hidden curriculum into apparent self-improvement"
source: https://arxiv.org/abs/2608.18066
captured: "2026-08-22"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: a432fc696ee1fce4d986b2fc7de9a337e8a5e463bf22e8e1a621bf7eb43b6339
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, agent-evaluation, deploy-time-learning, reliability]
---

# Ingest: On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification

## Classification

An arXiv v1 preprint with repeated benchmark runs, task-order interventions, memory inspection, and ablations over the information supplied during memory construction.
Author: Qinyuan Ye, Yu Li, Yada Pruksachatkun, Jiaxin Zhang, and Chien-Sheng Wu. The paper and its linked repositories identify Salesforce AI Research provenance. Its strongest author signal is methodological: it stress-tests two existing methods rather than introducing another memory method.

## Summary

The paper re-evaluates Agent Workflow Memory (AWM) and ReasoningBank on WebArena, VisualWebArena, and SCUBA with GPT-5-mini and newer agent harnesses. It runs each main setting three times and tests the default task order plus two shuffled orders. Memory increases run-to-run variance in 17 of 24 domain-method comparisons; the largest three-run best-worst gap is 10.42 percentage points on WebArena's 48-task Multisite subset. On WebArena, ReasoningBank moves from a 1.5-point average gain under the default order to an average 4.5-point loss under the shuffled orders. The authors trace some failures to memory construction that lacks task intent and environment constraints: accepted memories recommend unsupported APIs or human confirmation, generalize from evaluator mistakes, or preserve a rewarded Haversine shortcut. Supplying evaluator rubrics, action-error feedback, and explicit environment constraints recovers part of the shuffled-order loss, but the enhanced system still trails the no-memory baseline.

## Connections Found

This paper is a direct empirical anchor for [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [A checked outcome licenses retaining an episode, not abstracting its explanation](../notes/checked-outcome-licenses-episode-retention-not-abstraction.md), and [Trace-extracted memory earns authority per operation, not at capture](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). Its evaluator-bug, irrelevant-medical-advice, unsupported-API, and Haversine cases show how an outcome-gated trace can become prompt-level guidance without evidence for the explanation or its transfer boundary. The partial gains from rubrics and action errors also show that a richer diagnostic surface can improve the next memory proposal without making reward itself a stronger abstraction oracle.

At the system level, the source adds repeated-run and shuffled-order reliability evidence to the existing reviews of [Agent Workflow Memory](../agent-memory-systems/reviews/agent-workflow-memory.md) and [ReasoningBank](../agent-memory-systems/reviews/reasoning-bank.md). It qualifies the positive evidence in the [original AWM ingest](./agent-workflow-memory.ingest.md). It also extends the stateless perturbations in [Towards a Science of AI Agent Reliability](./towards-a-science-of-ai-agent-reliability.ingest.md) with path-dependent retained state. Its relation to [Large Language Model Agents Are Not Always Faithful Self-Evolvers](./llm-agents-are-not-always-faithful-self-evolvers.ingest.md) is complementary: that study asks whether stored memory changes behavior, while this paper asks whether behavior shaped by the stored memory remains reliable.

The fixed-decomposition lens narrows the result. The memory constructor can condition on the task, trajectory, and ground-truth reward; the interventions add rubrics, action errors, and explicit prompt constraints. The acting agent can compose only the web actions exposed by the harness, while AWM injects accumulated workflows and ReasoningBank retrieves one prior task's textual memories. The base model, harness, action basis, natural-language memory forms, write cadence, retrieval policies, and prompt-level memory authority remain fixed. Because adding signals recovers some performance, the paper does not show that the needed correction was unreachable inside the effective update space. It shows that the original evidence surface was inadequate within this fixed design; it does not validate the surrounding decomposition.

## Extractable Value

1. **A stateful learner needs sequence perturbation in addition to repeated runs.** Repeating one order estimates dispersion conditional on that order. Shuffling the learning sequence tests path dependence because an early memory changes the context and behavior available to every later task. This distinction is not yet a settled note in the KB. [quick-win]

2. **Retained state can amplify ordinary execution noise.** The no-memory agent is already stochastic, but memory turns early random outcomes and abstractions into persistent causes of later behavior. Evaluation should therefore report whole-stream run distributions, not only averages over independently treated tasks. [experiment]

3. **Ground-truth task success is too weak a memory-write oracle.** The study deliberately replaces a noisy LLM judge with ground-truth reward, yet still obtains misleading reusable lessons. Outcome correctness can select an episode while task ambiguity, evaluator bugs, and unintended shortcuts leave its explanation unwarranted. [quick-win]

4. **Memory quality and behavioral faithfulness are independent evaluation axes.** A memory may be useful but ignored, or wrong and faithfully applied. This paper supplies the second failure mode; the self-evolver study supplies the first. A complete memory evaluation needs interventions for causal uptake and checks on content authority. [deep-dive]

5. **The mitigation ablation tests evidence-surface expansion, not the memory architecture.** Rubrics, environment errors, and prompt constraints improve ReasoningBank under the tested orders, but the experiment does not vary its textual representation, top-1 retrieval, per-task write policy, absence of validation, or prompt-level authority. Rival decompositions remain an open experiment. [experiment]

6. **A stronger current baseline can erase an apparent self-improvement gain.** The GPT-5-mini no-memory baseline matches or exceeds earlier memory-enhanced results, and ReasoningBank's 1.5-point default-order gain has an unpaired-test p-value of 0.23 over three runs. Memory methods need comparison with a current harness, not only their historical baseline. [just-a-reference]

## Limitations (our opinion)

The evidence is narrow. This is a v1 preprint about two textual-memory methods in web-browsing environments. Three runs are too few to characterize tail behavior or support a precise variance estimate, and the reported significance test has only three observations per condition. Two fixed shuffles probe order sensitivity but do not establish performance over the distribution of realistic task streams. The 10.42-point maximum also comes from the smallest WebArena subset, with 48 tasks. The paper's 17-of-24 and 31% figures should not be generalized to all self-improving agents.

The underspecification explanation is plausible but only partly isolated. The authors qualitatively inspect a subset of ReasoningBank memories. Their interventions alter both available evidence and instructions, and exact benchmark rubrics expose intended answers that a deployment may not possess. The combined treatment recovers only part of the loss. It therefore supports diagnostic insufficiency as one cause, not as a complete explanation of variance or order dependence.

The unresolved question is causal: does the fragility originate when the system constructs an incorrect memory, retrieves an irrelevant one, grants injected memory too much behavioral authority, or lets a bad memory persist without verification and invalidation? The paper does not separate these mechanisms. Fixed-memory replay could hold memory content constant while varying retrieval and authority; a complementary intervention could hold retrieval constant while varying the evidence available during construction. These contrasts would locate the failure boundary more directly.

As [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) warns, the ablations do not test adjacent fixed choices. They leave the memory representation, retrieval and injection policies, model, harness, task partition, web action space, and lack of a separate verify/invalidate operation unchanged. The paper recommends memory validation and human intervention interfaces but does not evaluate either one.

The paper uses ground-truth rewards during induction, unlike original paths that may use a noisy LLM judge, so it does not measure the full practical error cascade. Conversely, its newer backbone and harness limit direct comparison with the original implementations. Released code is linked from the paper, but this ingest did not inspect or execute it; all outcome claims remain paper-reported rather than reproduced.

## Recommended Next Action

Write to the authors with a focused root-cause question: ask whether they have run or plan fixed-memory replay or crossed interventions that separate memory construction, retrieval, behavioral authority, and verification or invalidation. Until that causal boundary is established, treat the concrete failure modes rather than a general theory of memory fragility as the paper's durable contribution.
