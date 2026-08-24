---
description: "A small paired-prompt PoC reports fewer fabricated or looping responses when impossible tasks permit explicit non-success outputs."
source: https://github.com/OttoRenner/Gentle-Coding/blob/main/Proof-of-Concept.md
captured: "2026-07-17"
capture: web-fetch
genre: practitioner-report
snapshot_sha256: 1a8e61f03823ef1341a1a1f7dfeaa8b763813b5900ae47e046a1fc0d341d189f
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [prompt-design, evaluation, response-policy]
---

# Ingest: Gentle-Coding Proof of Concept

## Classification

This is a practitioner report of a small, informal paired-prompt experiment rather than a controlled scientific study. Author: Otto Renner is the repository author and reports the tests directly; the snapshot supplies no institutional affiliation, peer review, model logs, or independent replication signal.

## Summary

The report gives six cloud-model interfaces three impossible or contradictory tasks under paired “authoritarian” and “gentle” prompts, then reports that the authoritarian conditions more often produced fabricated answers, slow or looping reasoning, and one manual termination while the gentle conditions more often produced the allowed fallback or acknowledged uncertainty. Its useful observation is narrower than its psychological explanation: the paired prompts change stakes, task assertions, output constraints, permission to fail, and explicit fallback availability together, so the results support only a bundle-level contrast and do not identify empathy, pressure, or training penalties as the cause.

## Claims

No claims have been grounded yet.

## Connections Found

The source is bounded practitioner evidence for [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): each pair changes several causally relevant prompt components, so the observed behavior cannot be assigned to tone alone. It is also a worked negative case for [Structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md), because the report attributes the result to penalty-shaped training without discriminating that account from task semantics or response policy. The reported loops, fabricated exits, and manual termination provide limited evidence for [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md), though not a measured cost estimate. Most usefully, comparison with [Simplification](./simplification-2090443748077416467.ingest.md) and [Assessing LLM Reasoning in Evidence-Based Claim Verification](./assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) suggests that an explicit no-op, unknown, or insufficient-evidence branch changes which correct outcomes are representable rather than merely making a prompt gentler.

## Extractable Value

1. **Permitted non-success is a task-design variable** -- The “Random,” “No word present,” and uncertainty responses expose a reusable response-policy hypothesis already echoed by the no-op and abstention cases in connected sources. [quick-win]
2. **The paired conditions are a multi-factor bundle** -- The report is a compact teaching case for why task assertions, social stakes, output shape, permission to fail, and fallback availability need separate ablations before component-level causal claims. [quick-win]
3. **Impossible-task behavior can fail soft rather than fail stop** -- Fabricated answers, repeated reasoning, and a manually stopped run offer context-bound examples of an interpreter continuing to pursue an infeasible goal instead of surfacing blockage. [just-a-reference]
4. **A matched factorial follow-up could isolate the active lever** -- Hold the task and output vocabulary fixed while independently varying tone, threat language, and fallback availability across repeated runs with pinned model versions and recorded timings. [experiment]
5. **Anthropomorphic labels obscure testable mechanisms** -- Recasting “performance anxiety” as a choice among response-policy, task-semantics, salience, and inference-allocation explanations would make the proposal easier to falsify and transfer. [deep-dive]

## Limitations (our opinion)

The report is a self-described small PoC using free cloud interfaces, with no pinned model versions, raw transcripts, repeated-run counts, controlled sampling settings, token logs, or measured latency. It changes several factors at once and classifies some outputs informally, so neither the reported unanimity on the random-sequence task nor the latency descriptions support population estimates. Survivorship and observer bias are plausible because the author supplies the hypothesis, prompts, judgments, and causal story.

The experiment also fixes the decomposition whose adequacy it appears to test. Models condition on one prompt in an isolated session; their available response operations are generated text, but the prompts make different terminal responses acceptable; and their effective hypothesis classes and hidden interface policies are unknown. Task construction, truth labels, response vocabulary, prompt bundle, model selection, and measurement choices remain outside any effective update space. Under [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within the gentle condition shows only that the compound configuration sufficed here. It does not validate that decomposition or establish empathy, anxiety, trauma response, RLHF penalty avoidance, or hard training penalties as the mechanism.

## Recommended Next Action

Write one synthesis note, “An explicit non-success branch makes warranted abstention representable,” using this PoC, Simplification, and the claim-verification benchmark analysis to distinguish response-space design from prompt tone.
