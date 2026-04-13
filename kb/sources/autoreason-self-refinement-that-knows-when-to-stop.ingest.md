---
description: Autoreason paper showing self-refinement improves only when candidate synthesis is paired with blind comparative judging and incumbent survival, with gains concentrated in the generation-evaluation gap
source_snapshot: autoreason-self-refinement-that-knows-when-to-stop.md
ingested: "2026-04-13"
type: ingest-report
source_type: scientific-paper
domains: [evaluation, self-refinement, oracle-theory, agent-orchestration]
---

# Ingest: Autoreason: Self-Refinement That Knows When to Stop

Source: autoreason-self-refinement-that-knows-when-to-stop.md
Captured: 2026-04-13
From: https://github.com/NousResearch/autoreason/blob/main/paper/autoreason.pdf

## Classification

Type: scientific-paper -- GitHub-hosted preprint-style paper with a method, benchmark results, ablations, failure taxonomy, and citations; not confirmed peer-reviewed.
Domains: evaluation, self-refinement, oracle-theory, agent-orchestration
Author: SHL0MS / Hermes Agent; the author signal is less important than the source's concrete ablations and mixed subjective/objective evaluation, but provenance should be treated as preprint-level rather than peer-reviewed.

## Summary

Autoreason proposes an iterative self-refinement architecture where each pass compares the unchanged incumbent (A), an adversarial revision (B), and a synthesis (AB), then uses blind fresh-agent judges with Borda aggregation and incumbent-favoring ties to decide whether to change the output. The central thesis is that self-refinement fails because critique prompts create prompt bias, repeated revision causes drift or bloat, and models rarely decline to edit; making "do nothing" a first-class option prevents degradation. Across writing tasks, CodeContests problems, model-tier comparisons, and ablations, the method helps most when a model can generate useful alternatives but cannot reliably choose among them. The paper frames this as a generation-evaluation gap: too-weak models lack candidate diversity, stronger models can self-evaluate well enough that external structure adds little, and mid-tier/cost-conscious models gain most.

## Connections Found

The connect report found the source belongs in the KB's soft-oracle and error-correction cluster. It **grounds** [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) with a concrete Borda/paired-comparison loop; **exemplifies** [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) through fresh isolated judges, randomized labels, judge-count ablations, and broken-panel failure; and **extends** [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md) by showing synthesis can be useful as candidate generation when selection remains separate. It also connects to [Topology, isolation, and verification form a causal chain for reliable agent scaling](../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md), [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [Evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md), [Automated synthesis is missing good oracles](../notes/automated-synthesis-is-missing-good-oracles.md), and [Quality signals for KB evaluation](../notes/quality-signals-for-kb-evaluation.md). The source-to-source bridge is [Improving AI Skills with autoresearch & evals-skills](./improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.ingest.md): that report emphasizes manual judge construction before optimization, while autoreason contributes an architectural pattern for comparative judging and restraint.

## Extractable Value

1. **Candidate synthesis is useful only when paired with a separate comparative oracle** -- Autoreason's AB candidate adds value because a judge panel compares it against A and B; without that selection layer, synthesis would be another drift mechanism. This is high-reach because it bridges KB synthesis, multi-agent aggregation, and self-refinement under one design rule. [quick-win]
2. **Make "do nothing" a first-class candidate in critique loops** -- The incumbent-survival mechanism directly counters prompt bias from "find problems" critique prompts and mandatory revision. This is immediately transferable to note revision, source ingestion review, and skill optimization loops where models otherwise always edit. [quick-win]
3. **Soft-oracle hardening needs both comparative format and judge hygiene** -- Blind labels, fresh contexts, multiple judges, Borda aggregation, conservative ties, and parser integrity all matter. The broken mixed-panel result is a practical warning: a broken judge does not just add noise; it can prevent convergence. [experiment]
4. **The generation-evaluation gap is a non-monotonic architecture-placement signal** -- Autoreason helps most when models are strong enough to generate alternatives but weak enough to need selection help. The Haiku 4.5 transition result suggests refinement architecture should be re-evaluated as model generations shift, not treated as a permanent best practice. [deep-dive]
5. **Scope constraints turn defensive refinement into useful improvement** -- On unconstrained tasks, autoreason mainly prevents baselines from drifting or bloating; on constrained writing tasks and competitive programming, structured recovery produces stronger gains. This reinforces existing KB claims that oracle strength and scoped task boundaries determine whether automation can improve rather than merely churn. [just-a-reference]
6. **Recovery after first failure is the measurable mechanism in code** -- The CodeContests results suggest autoreason does not improve first attempts; it improves what happens after failure by forcing analysis before revision. This is useful for agent workflows: spend structure on post-failure diagnosis, not on indiscriminate extra passes. [experiment]

## Limitations (our opinion)

The paper should not be treated as settled evidence that autoreason is generally superior self-refinement. Most writing evaluation relies on LLM judges rather than human raters, and all reported model families are Anthropic plus a small set of comparison tiers; cross-provider generality is limited. The code results provide objective private-test evaluation, but several reported advantages are modest or not statistically significant, with the strongest significance attached to a paired recovery subset rather than the full aggregate. The proposed four success conditions -- external verification, constrained scope, structured reasoning, and sufficient decision space -- are plausible but not cleanly ablated, so the simpler account may be that scope plus a decent selection oracle explains most of the gains. The central claim is partly hard to vary because the incumbent-vs-revision-vs-synthesis tournament has a specific mechanism, but the paper still risks over-attributing to the full architecture where cheaper variants such as conservative prompting, better judge prompts, or best-of-N with stronger external tests might suffice in some domains. Treat the method as a promising design pattern and empirical probe, not a universal refinement recipe.

## Recommended Next Action

Write a note titled "Candidate synthesis needs a separate comparative oracle" connecting to [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md), [Automated synthesis is missing good oracles](../notes/automated-synthesis-is-missing-good-oracles.md), and [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md). It would argue that synthesis should be used as a proposal generator, not as a verifier: generate AB-style candidates freely, but promote only through an explicit comparative oracle with incumbent survival and judge-hygiene checks.
