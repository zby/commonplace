---
description: "Tests length and domain transfer in language-model harnesses and shows how synthetic training can improve the choice of decomposition within a fixed runtime."
source: https://www.alphaxiv.org/abs/2611.harness-cg
captured: "2026-11-20"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 6497ccfb147bdd01f3a4335a555d52732c45dbb7472f75d1a95a38fe251a25ec
ingested: "2026-11-20"
type: types/ingest-report.md
domains: [compositional generalization, recursive language models, surrogate harness training]
learning_claims: true
---

# Ingest: Language Model Harnesses Can Be Compositional Generalizers

## Classification

A preprint with comparative post-training experiments, held-out benchmarks, and diagnostics of model behavior. Alex L. Zhang, Souradip Chakraborty, and Omar Khattab list MIT CSAIL as their affiliation.

## Summary

The [preprint](https://www.alphaxiv.org/abs/2611.harness-cg) asks whether a runtime can turn unfamiliar tasks into familiar computations for individual model calls. In the tested Recursive Language Model (RLM) configuration, a root model writes code over inputs stored outside its prompt and can dispatch fresh model calls. After reinforcement learning on short tasks, this configuration transferred better than the direct Transformer baseline to tested variants 2–64 times longer and to three domain shifts selected for shared solution structure (§3). Within the same RLM runtime, supervised fine-tuning of Qwen3.8-27B on synthetic traces designed around target strategies raised the eight-benchmark average from 46.1 to 58.5 while using roughly half as many inference tokens (§4.2, Tables 4–5). A separate gated-chain experiment tests recursive reuse of the trained solver as part of a package that changes training and runtime conditions (§4.3).

## Contribution assessment (our opinion)

The paper makes progress on an important problem: how to reuse capabilities on longer or unfamiliar tasks without training on full target rollouts. Its strongest contribution is not decomposition itself, which the paper situates among earlier prompting and recursive methods, but evidence that training on simpler tasks can teach a reusable orchestration strategy. The authors test a consequence of that explanation at two levels: whether the root repeats a strategy and whether local execution still works. The Pi counterexample helps rule out root-trace similarity as a sufficient explanation. Target-aware surrogate design narrows the claim to transfer where a usable strategy can already be specified; it does not erase the demonstrated transfer to new instances.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper gives [bounded-context scheduling heuristics](../theory/decomposition-heuristics-for-bounded-context-scheduling.md) a concrete test case. In the tested RLM, one OOLONG trace pair shows code splitting records into batches, fresh calls labeling each batch, and code counting the results. The longer example repeats the same strategy with more calls. In the tested Pi configuration, a similar root trace instead returns wrong counts on the longer task. Together these cases support checking local results independently of whether the orchestrator repeats its plan; they do not establish that open-ended synthesis admits the same split.

The paper also adds an acquisition example to the [orchestration design space](../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md): synthetic traces change which scheduling programs the model generates in a fixed runtime, while code still executes those programs. This measures reuse of a strategy through model weights, not reuse of a saved executable.

## Learning Claims (our opinion)

The paper uses *locally in-distribution* to mean that a call receives a familiar, solvable input, not that its prompt was observed during training. Reinforcement learning uses task reward; surrogate fine-tuning instead imitates selected traces, mostly at the root, generated with teacher-designed strategy hints and sometimes simulated sub-call responses. The root can learn which slices to expose, what to delegate, and how to combine outputs. In §3 the RLM's loss targets the root trajectory, but root and sub-calls share the served policy: excluding sub-call tokens from the loss does not freeze a separate child model. These are changes within a [fixed learning boundary](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): the runtime supplies offloaded input, persistent execution state and callable operations; surrogate designers supply candidate strategies.

The runtime and weight-update loop do not establish a [theory builder](../theory/definitions/theory-builder.md). **Localized content:** generated code states inspectable steps, whereas no corresponding commitments are separately identified in the updated weights. **Consumption:** executing the generated program determines what sub-calls see and how their answers are used. **Criticism:** a task score can reject an outcome, but the training loop does not show stated criticism aimed at a particular program assumption. **Iteration:** rewards shape later policies, and some within-run retries respond to failed answers; the paper does not show a stated criticism retained and used to revise a stated strategy. Programs and intermediate state guide work within a run; weight changes persist across runs. Separately, the held-out gains demonstrate improved capacity for future action on the tested tasks, not revision of a retained, inspectable theory.

## Extractable Value

1. **Test orchestration and local execution separately.** In the offloaded-context experiments, a matching root plan can coexist with incorrect local results. For a KB workflow expected to transfer, check both whether the split still fits the new task and whether the returned evidence preserves what the merge needs. [experiment]
2. **Separate strategy acquisition from execution.** Mostly root-level synthetic traces taught Qwen3.8-27B more effective scheduling behavior in the same RLM runtime. The result adds a measured alternative to supplying a strategy in a prompt or saving executable code, without comparing their costs directly. [quick-win]

## Limitations (our opinion)

The harness comparisons vary bundles. The CodeAct variant drops both programmatic sub-calls and output truncation; Pi uses different call interfaces, training targets, and budget settings. They compare tested configurations, not the isolated effect of offloading or delegation. §4.2 holds the RLM runtime fixed but compares training packages: the supervised traces include teacher hints and filtering, whereas synthetic reinforcement learning does not. Some surrogates reuse benchmark question wording with different content (Appendix B.9). Rollout speed varies (Appendix B.10), so lower inference token use is not evidence of lower total training cost.

The chain experiment draws from tasks the trained model already solves much better than the base model. Full-chain success for RLM-27B rises from 55.2% to 77.5% with additional fine-tuning, a handoff operation, a progress cue, and a different turn allocation; the recursion-hint condition scores 47.2%. This is evidence for the tested package on selected gated chains, not for recursion alone or for tasks whose stages need shared evidence.

## Recommended Next Action

Add surrogate training as a measured strategy-acquisition example in the [orchestration design-space note](../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md#decomposition-policy-artifact), distinguishing changes to the learned policy from changes to the runtime.
