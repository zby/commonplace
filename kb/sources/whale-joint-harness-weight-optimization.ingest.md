---
description: "Controlled WHALE experiments show alternating model updates and executable-harness search can beat either alone, within fixed tasks, verifiers, and search spaces."
source: https://arxiv.org/abs/2609.00196
captured: "2026-09-04"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 224cd409ca0e6c05103dd9f58b038c818bed7ed0185fde154e248b213bced85d
ingested: "2026-09-04"
type: kb/sources/types/ingest-report.md
domains: [agent-learning, harness-optimization, model-weight-training]
---

# Ingest: WHALE: Joint Harness-Weight Optimization

## Classification

This is a scientific paper presenting a method, controlled baseline comparisons, schedule ablations, and behavior analyses across three tool-using benchmark domains. Author: the research team is affiliated with KRAFTON, KAIST, and Stanford, includes researchers active in agent and learning research, and reports its own method with a linked implementation.

## Summary

WHALE alternates online rejection-sampling fine-tuning of model weights under a fixed harness with Meta-Harness search over executable harness code under fixed weights. On Qwen3.5-2B/4B agents for search question answering, mathematical reasoning, and chess puzzles, its main fixed schedule reports higher best mean@8 test accuracy than weight-only, harness-only, and prompt-and-weight baselines: it beats the stronger single-component baseline by 7.67--10.05 percentage points and the prompt-restricted control by 4.15--13.00 points. SearchQA appears harness-dominant, while Math appears model-dominant and shows harness gains only after a weight update. In SearchQA and Math, short alternating phases also beat one weight-then-harness stagewise pass, and a training-signal patience rule performs better than the main fixed schedule in both domains, though not better than the strongest hand-tuned schedule in Math. The paper is useful as bounded evidence that the effective optimization unit is a model-harness pair and that its update cadence matters.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper's strongest role is a controlled, domain-bounded empirical anchor for [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). Shared initial model-harness pairs and matched within-domain budgets produce different single-component rankings across tasks but consistent gains from updating both. Repeated cycles also instantiate [representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md): distributed-parametric weights change alongside a harness whose natural-language and symbolic parts remain separately searchable.

Its prompt-restricted control is technical evidence for [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md). Holding the updater and schedule fixed while widening the context-side search space identifies the value of the non-prompt harness bundle, not any individual parser, tool interface, feedback rule, context transformation, or termination policy. Compared with [Co-Harness](./co-harness-co-evolving-harness-and-model-weights.ingest.md), WHALE adds single-axis, prompt-only, stagewise, and cadence controls across three domains, so its distinctive role is evidence about attribution and scheduling rather than another general example of co-adaptation.

## Extractable Value

1. **Treat a component bottleneck as conditional, not intrinsic.** SearchQA and Math reverse the relative strength of harness-only and weight-only adaptation, while a small weight update makes harness search more effective in Math. This supports a new synthesis explaining that the current task, counterpart, and intervention jointly determine which component limits performance. [deep-dive]
2. **Use short alternation as a scheduling hypothesis for cross-form learning.** In SearchQA and Math, a single full-budget weight-then-harness pass is worse in both best accuracy and rollout count than the tested short alternating schedule. The result gives concrete design evidence for limiting optimization against a counterpart that will soon change, while leaving the proposed over-optimization mechanism to further tests. [deep-dive]
3. **Preserve the full-harness versus prompt-only contrast as a bundle-level result.** The matched FST control supports widening the editable surface beyond prompts, but it cannot identify which added harness operation causes the gain. This is a useful positive case for the KB's treatment-grain discipline. [quick-win]
4. **Test cheap component interventions as moving-bottleneck diagnostics.** Harness-only search reaches SearchQA's weight-only peak with far fewer target-agent rollouts, suggesting a short harness probe before expensive weight training; the experiment must include proposer compute and domains beyond SearchQA before this becomes an operating rule. [experiment]
5. **Evaluate training-signal patience as a phase scheduler.** Adaptive WHALE removes fixed per-cycle budgets and beats the main schedule in SearchQA and Math, but falls below the best hand-tuned Math schedule. This supplies a concrete scheduling mechanism to compare with fixed cadence and validation-gated switching. [experiment]

## Limitations (our opinion)

The result is narrow in models, methods, and tasks: one RSFT/Meta-Harness instantiation is tested on Qwen3.5-2B/4B across three benchmark domains with sparse binary verifiers. The available task prompts and harness-produced observation histories can condition model behavior; the model can compose text and tool calls; and Meta-Harness can compose executable edits within the allowed prompt, tool-I/O, parser, feedback, context, and termination surfaces. Together these choices express model-harness mappings from tasks and histories to trajectories. However, the model families, data partitions, verifier objectives, reference answers, environment transitions, proposer, update algorithms, phase order, sampling settings, and domain-specific harness boundaries remain outside the effective update space. Improvement inside this decomposition therefore does not validate those fixed choices.

The prompt-only ablation identifies the broader non-prompt harness bundle, not any one added operation. The stagewise comparison covers only SearchQA and Math, and the accompanying behavior metrics are observational; neither isolates conditional over-optimization as the cause of the schedule result. Headline results use best-so-far mean@8 test accuracy, and the stated algorithm returns the pair with the best test accuracy, so applicability to checkpoint selection without test-set access is unclear. Whole-run uncertainty across independent seeds is not reported in the captured paper. Rollout-efficiency comparisons exclude proposer compute and therefore do not establish total-compute efficiency. The linked implementation was not inspected or executed, so implementation fidelity and empirical reproduction remain unverified.

## Recommended Next Action

Write a note titled **A component bottleneck is conditional on its current counterpart**, using WHALE's matched interventions as bounded evidence that an update can move the limiting component rather than reveal an intrinsic model-versus-harness ranking.
