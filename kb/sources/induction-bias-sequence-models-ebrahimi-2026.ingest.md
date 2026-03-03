---
source_snapshot: induction-bias-sequence-models-ebrahimi-2026.md
ingested: 2026-03-03
type: scientific-paper
domains: [ml-architecture, state-tracking, data-efficiency, inductive-bias]
---

# Ingest: On the "Induction Bias" in Sequence Models

Source: induction-bias-sequence-models-ebrahimi-2026.md
Captured: 2026-03-03
From: https://arxiv.org/pdf/2602.18333

## Classification

Type: scientific-paper -- Large-scale empirical study (190,000+ training runs) with systematic methodology, quantitative metrics (sharing factor kappa), and controlled comparisons across architectures and supervision regimes. Published as a preprint by Qualcomm AI Research.

Domains: ml-architecture, state-tracking, data-efficiency, inductive-bias

Author: M. Reza Ebrahimi, Defferrard, Panchal, Memisevic at Qualcomm AI Research. Ebrahimi has prior published work on transformer limitations in state tracking (COLM 2024) and bilinear RNN architectures (NeurIPS 2025). The team has systematic expertise in the transformer-vs-recurrent comparison space.

## Summary

The paper conducts a large-scale empirical study comparing transformers and recurrent neural networks (LSTMs, Dense-SSMs) on state-tracking tasks (modular addition, permutation composition), focusing on in-distribution data efficiency rather than the usual OOD length-generalization framing. The central finding is that transformers require dramatically more training data than RNNs for state tracking -- sometimes by orders of magnitude -- because they lack what the authors call "induction bias": the structural constraint that forces step-by-step state updates. The paper introduces a sharing factor (kappa) that quantifies whether a model reuses learned mechanisms across different sequence lengths. Transformers show kappa near or below 1 (learning length-specific solutions in isolation, with destructive interference under CoT), while RNNs show kappa >> 1 (amortized learning via shared transition operators). The paper further shows that in-distribution data efficiency and cross-length weight sharing are highly correlated with OOD length-generalization ability, connecting the in-distribution and OOD failures as manifestations of the same underlying architectural limitation.

## Connections Found

The `/connect` discovery found 4 strong and 3 moderate connections, all cross-domain (this is the first ML-research paper in the KB, so connections are analogical rather than within-domain):

**Strong connections:**
- [bitter-lesson-boundary](./bitter-lesson-boundary.md) -- **grounds**: The paper provides direct empirical evidence for when the bitter lesson fails. Transformers (the "general method leveraging computation") are dramatically outperformed by RNNs with structural priors on state tracking, a calculator-class problem where architectural constraint is permanent leverage, not a temporary advantage scale will dissolve. The kappa < 1 finding (destructive interference) is especially telling -- more data actively hurts, the opposite of the bitter lesson's prediction.
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) -- **exemplifies**: The three supervision formats (outcome, CoT, ACoT) map to different oracle granularities. The finding that architecture interacts with oracle granularity (RNNs benefit from per-step ACoT supervision while transformers do not) demonstrates that oracle strength is necessary but not sufficient -- the learner's architecture must match the oracle's structure.
- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) -- **extends by analogy**: Both describe the same mechanism at different levels -- structural constraints that do not add information but constrain the search space so learning converges faster. The KB note operates at the prompt level; the paper operates at the architecture/weight level.
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **extends**: Transformers' length-isolated learning (kappa near 1) is analogous to correlated errors -- knowledge at one length does not transfer. RNNs' high kappa achieves the decorrelated, amortized learning that error correction requires.

**Moderate connections:**
- [meyerson-maker-million-step-llm-zero-errors](./meyerson-maker-million-step-llm-zero-errors.md) -- Brackets the same problem from the opposite direction. Ebrahimi explains WHY transformers fail at long-range state tracking; MAKER shows HOW to build reliable systems despite that failure via decomposition + error correction.
- [stabilisation](./stabilisation.md) -- Analogous mechanism: induction bias constrains the hypothesis space as stabilisation constrains the interpretation space, both trading generality for efficiency.
- [deploy-time-learning-the-missing-middle](./deploy-time-learning-the-missing-middle.md) -- The supervision regimes map loosely to the verifiability gradient: making intermediate computation explicit and verifiable makes learning cheaper.

**Synthesis opportunity:** "Architectural constraints as a form of stabilisation" -- constraint-as-learning-accelerator operates at every level (weights, artifacts, prompts), with the bitter lesson boundary determining which constraints are permanent vs. temporary.

## Extractable Value

1. **The sharing factor kappa as a diagnostic metric** -- kappa quantifies whether a system reuses learned mechanisms across problem variations or learns isolated solutions. This concept could transfer beyond ML architectures to evaluate whether knowledge-system structures (templates, indexes, conventions) enable amortized learning or force per-instance solutions. [experiment]

2. **Destructive interference is possible (kappa < 1)** -- More data and more diversity can actively hurt when the architecture lacks the right inductive bias. Transformers with CoT on mixed lengths showed kappa = 0.28. This is a concrete counter-example to "more data is always better" and directly grounds the bitter-lesson-boundary note with quantitative evidence. [quick-win]

3. **Architecture-supervision interaction** -- Transformers prefer CoT (non-aligned), RNNs prefer ACoT (aligned). The optimal supervision format depends on the learner's architecture, not just the task. This has implications for how we think about oracle design: the oracle must match the learner, not just the problem. [just-a-reference]

4. **In-distribution failure as the real story** -- The paper reframes transformer state-tracking limitations from "OOD failure" to "in-distribution data inefficiency." This is a more practically relevant framing: even with unlimited training distribution coverage, the data cost may be prohibitive. Connects to how we think about scaling costs in the bitter lesson boundary. [quick-win]

5. **Permutation composition generalizes beyond commutative tasks** -- The findings hold for non-commutative state tracking (S_5), which is the canonical non-commutative structure by Cayley's theorem. This means the limitation is not specific to simple arithmetic but applies to any finite discrete state-tracking task. [just-a-reference]

6. **Step-by-step decomposition as permanent architectural advantage** -- For tasks with exact specifications (calculator-class problems), forcing step-by-step computation is not a temporary crutch but a permanent efficiency gain. This strengthens the argument that some problems should never be approached with general methods, regardless of scale. [deep-dive]

## Recommended Next Action

Update [bitter-lesson-boundary](../notes/bitter-lesson-boundary.md): add a "Grounding evidence" section citing this paper as the strongest empirical case for the calculator side of the boundary. The paper's kappa metric (sharing factor) and the destructive interference finding (kappa = 0.28 for transformers with CoT) provide quantitative evidence that on calculator-class problems, architectural structure is not just temporarily better but that the general method actively degrades with more diverse data. This directly strengthens the note's central claim with hard numbers rather than intuition.
