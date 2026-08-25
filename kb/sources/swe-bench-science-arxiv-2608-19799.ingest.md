---
description: Author-controlled benchmark paper separates visible test success from scientific correctness and bounds the mixed effects of supplied scientific guidance.
source: https://arxiv.org/pdf/2608.19799
captured: "2026-08-25"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: 7d7458bddf1d2789b61d8a128fcc1a107b9bd457c4321c2b3d898fef633b0d16
ingested: "2026-08-25"
type: kb/sources/types/ingest-report.md
domains: [coding-agents, evaluation, scientific-software, context-engineering]
---

# Ingest: SWE-bench Science full paper on scientific-software repairs

## Classification

This is a scientific paper: it defines a repository-level benchmark, reports comparative agent evaluations, manually audits failed repairs, and runs a paired scientific-guidance ablation. Author: Zhipeng Xu, Jiahao Lu, Yining Zheng, Yuxin Wang, and Xipeng Qiu; the paper identifies affiliations with the Shanghai Innovation Institute and Fudan University and is an arXiv v1 preprint dated 2026-08-20, with no peer-review signal stated.

## Summary

SWE-bench Science evaluates eight model-harness configurations on 119 tasks from 98 repositories across 20 scientific domains, using public checks for interactive repair and private cases for exact scientific correctness. The best overall Pass@1 is 47.90% despite public scores of at least 93.28%, and a manual audit assigns unsuccessful repairs to scientific-abstraction, exploration, system-integration, or generalization failures. On a 91-task subset, a paired comparison adds or removes auxiliary scientific information while preserving required context and executable repository evidence: the information lowers GPT-5.6-sol Pass@1 from 36.26% to 31.87% but raises DeepSeek-V4-flash from 16.48% to 23.08%, with different token-cost effects. For Commonplace, the paper is most useful as bounded evidence that visible conformance does not establish objective achievement, aggregate scores erase mechanism distinctions, and supplied context is not equivalent to beneficial use; the authors appropriately describe the ablation differences as model-specific and non-causal.

## Quotes

No source quotes have been retained yet.

## Connections Found

This full paper is the author-controlled empirical anchor for the provisional [AlphaXiv-derived SWE-bench Science analysis](swe-bench-science-coding-agents-scientific-software.ingest.md). Its public/private evaluation split supplies a bounded scientific-software instance for [Exact implementation does not validate a requirement against its objective](../notes/exact-implementation-does-not-validate-a-requirement.md), while its four-way failure audit supports the diagnostic-insufficiency premise of [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). The paired guidance comparison is a clean worked example for [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) and bears narrowly on the presence-to-benefit rung of [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md): it observes outcomes after supplying information but does not measure consultation or semantic uptake.

Read through [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), each attempt can condition repair on the repository snapshot, problem statement, required scientific context, code and runtime observations, public-test feedback, interaction history, and, in one condition, auxiliary scientific guidance. The agent can compose workspace inspection, hypothesis formation, source edits, public-test execution, revision, and patch submission; its fixed model-harness configuration maps the available evidence and history to those operations and patches. Task selection and taxonomy, frozen repositories and environments, problem and context representations, model weights and harness, guidance design, public/private oracle partition, hidden validators, scores, and manual failure labels remain outside the within-task update space. Performance therefore assesses repair inside that fixed decomposition. The paired ablation identifies only descriptive differences from adding that particular auxiliary-information block in two configurations; it does not validate the guidance design, establish an activation or anchoring mechanism, or test the fixed benchmark and agent interfaces.

## Extractable Value

1. **Use visible and objective-level checks as distinct evaluation layers.** The large gap between public scores and exact private success gives the exact-implementation note a repository-level case where exposed checks guide search but do not warrant the larger scientific objective. [quick-win]
2. **Keep mechanism labels beside aggregate success metrics.** The four-category audit distinguishes wrong scientific abstractions, surface repair, incomplete integration, and failed generalization, providing a reusable diagnostic vocabulary while stopping short of showing that the labels improve a later learning loop. [just-a-reference]
3. **Separate information presence from uptake, direction, and benefit.** The paired conditions manipulate availability and measure task outcomes, but they do not observe whether an agent consulted the information or how it affected a particular decision. [quick-win]
4. **Attribute the ablation only to its actual treatment.** Required scientific context, repository evidence, task objective, and evaluators stay fixed while heterogeneous auxiliary guidance is removed, so the result bears on that supplied block rather than scientific knowledge in general. [quick-win]
5. **Audit the effective update space before crediting agent improvement.** Repository exploration and patch revision remain learnable or composable inside each run, whereas task decomposition, oracle design, guidance construction, and model-harness choice cannot be repaired by the evaluated agent. [deep-dive]

## Limitations (our opinion)

In our opinion, the benchmark supports bounded claims about these curated tasks, not scientific software generally. The five largest domains supply 63.9% of tasks and six domains supply one task each; task redesign, hidden-oracle validity, and scientific-contract judgments also depend on the authors' manual construction process. The paper does not report repeated-run uncertainty, statistical significance, or a causal estimate for the 91-task comparison, and only two model-harness configurations enter that ablation. Its auxiliary-information treatment combines rationales, upstream repairs, audit findings, paper excerpts, and expert guidance, so a score change cannot identify which kind of information helped or harmed. Consultation and semantic uptake are unobserved, and anchoring is a hypothesis from case inspection rather than an isolated mechanism. The manual failure taxonomy is useful descriptively, but the paper reports no independent coding reliability, and mutually exclusive labels can hide interacting causes. Model and harness also vary together in the main comparison. We inspected neither the released benchmark code, dataset, nor evaluator and executed no experiments, so this ingest does not reproduce the paper's construction or outcomes. As the paper is an arXiv v1 preprint, later review or revisions may change the evidence.

## Recommended Next Action

Update [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) with the 91-task comparison as bounded evidence that supplied information and downstream benefit are separate, explicitly noting that consultation and semantic uptake were not measured and that the reported differences are descriptive results from two model-harness configurations.
