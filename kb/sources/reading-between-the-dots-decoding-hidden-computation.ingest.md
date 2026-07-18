---
description: "Filler-token study as evidence that monitorability depends on the observation surface and that hidden process traces can diagnose failures"
source_snapshot: "reading-between-the-dots-decoding-hidden-computation.md"
ingested: "2026-07-18"
type: kb/sources/types/ingest-report.md
domains: [mechanistic-interpretability, monitorability, reasoning, evaluation]
---

# Ingest: Reading Between the Dots: Decoding Hidden Computation across Filler Tokens

Source: [reading-between-the-dots-decoding-hidden-computation.md](reading-between-the-dots-decoding-hidden-computation.md)
Captured: 2026-07-18
From: https://arxiv.org/abs/2607.03502

## Classification

Genre: scientific-paper -- an ICML 2026 Mechanistic Interpretability Workshop paper with behavioral experiments, logit-lens analysis, causal KV-cache transplants, decoding evaluations, ablations, and explicit limitations.
Domains: mechanistic-interpretability, monitorability, reasoning, evaluation
Author: Academic mechanistic-interpretability researchers releasing code and data; the workshop venue, two principal models, quantized mechanistic runs, and dependence on open-weight access limit the strength and breadth of the evidence.

## Summary

Brauer, Mayrink Verdun, and Marks show that DeepSeek V3 and Kimi K2 can use content-free filler tokens as additional computation positions: filler improves accuracy across retrieval, composition, letter-position, and synthetic equation tasks; attention forms a question-to-filler-to-answer relay; intermediate values appear at ordered filler positions in residual-stream readouts; and transplanting filler-only KV caches causally moves answers toward a donor computation. They then aggregate residual logit-lens scores and use an LLM judge to recover discrete hidden intermediates without training labels, generally reaching 80-95% accuracy on correct examples. The important result is bounded: surface-token opacity does not imply total unauditability when white-box hidden states expose vocabulary-aligned, nameable intermediates.

## Connections Found

The paper gives [Oracle strength spectrum](../notes/oracle-strength-spectrum.md) a concrete oracle-manufacturing case: changing the observation surface from meaningless output tokens to residual states produces a useful soft process oracle. It provides direct evidence for [An outcome check licenses replay; a rule needs the process verified](../notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md), since decoded traces distinguish retrieval failure from composition failure where final correctness cannot. That failure localization also supports [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Its closest source companion is the [J-space/global-workspace ingest](verbalizable-representations-global-workspace-llms.ingest.md): both recover causally relevant verbalizable hidden content, but this paper contributes temporal localization across filler positions and a label-free aggregation pipeline, while remaining narrower in task and concept scope.

## Extractable Value

1. **Monitorability is relative to the observation surface** -- A content-free explanation channel can hide a computation that remains partially legible through internal states. This refines "opaque" from a property of the whole system into a property of a chosen observation channel. [deep-dive]
2. **Oracle hardening can mean instrumenting a different substrate** -- The paper does not improve the behavioral judge; it manufactures a stronger soft oracle by exposing residual-state evidence and then aggregating it. This adds an observation-surface move to the manufacture stage in [Oracle strength spectrum](../notes/oracle-strength-spectrum.md). [quick-win]
3. **Process traces diagnose error type beyond outcome checks** -- Wrong 2-fact answers often retain both operands but lack their sum, while letter-position failures more often lack the retrieved intermediate. The distinction operationalizes the KB's claim that process evidence licenses conclusions an outcome check cannot. [quick-win]
4. **Causal localization strengthens decoding claims** -- Filler-only KV-cache transplants shift donor-answer rank, and transplanting only positions where a particular addend decodes recovers most of the full-region effect. This is stronger than treating probe accuracy alone as proof that the model uses the decoded representation. [just-a-reference]
5. **Unsupervised does not mean assumption-free** -- The decoder uses no labels or training, but assumes relevant content projects through the vocabulary, repeats across selected late-layer positions, survives aggregation, and is interpretable by an LLM judge. Residual subtraction can help or harm depending on filler and target, so audit pipelines need condition-specific ablation. [experiment]
6. **Filler computation is not simply hidden written chain-of-thought** -- On the equation task, the latent sequence resembles ordinary depth-ordered single-pass computation spread over positions more than explicit step-by-step text. Monitoring methods should not assume that a hidden process shares the syntax of a verbal rationale. [deep-dive]

## Limitations (our opinion)

The evidence establishes partial auditability only for four decomposable tasks with discrete, nameable intermediates, chiefly on two frontier-scale mixture-of-experts models. It does not test long-horizon agent work, free-form planning, semantic argument validity, deceptive intent, or models trained adversarially to evade the decoder. The logit lens cannot see computation that is orthogonal to the unembedding vocabulary or represented primarily in attention patterns; all mechanistic runs use 4-bit checkpoints, and the chain-of-thought comparison is qualitative. Reported 80-95% recovery is also not a general monitor reliability figure: scoring focuses on correct examples with known targets, stronger LLM judges add substantial task-dependent inference, and the paper does not report the per-instance discrimination needed to justify automated escalation. Closed-weight frontier systems cannot currently be checked by this method. The result therefore complements, rather than overturns, the KB's preference for inspectable external artifacts and independent process verification.

## Recommended Next Action

Write a note titled `Monitorability depends on the observation surface, not the explanation channel` in `kb/notes/`, using this paper and the [J-space/global-workspace ingest](verbalizable-representations-global-workspace-llms.ingest.md) to extend [Oracle strength spectrum](../notes/oracle-strength-spectrum.md) while preserving the white-box, partial-decoding, and non-adversarial boundaries.
