---
description: "Gentle Coding's repository README proposes low-stakes collaboration, explicit completion criteria, and permitted failure outputs as prompt-contract elements."
source: https://github.com/OttoRenner/Gentle-Coding
captured: "2026-07-17"
capture: web-fetch
genre: code-repository
snapshot_sha256: 5c99601b818bcc5461e7c7c2fe4d8776773cca417aee8775d197d0739b65bb56
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [ai-coding, prompt-framing, context-engineering, llm-evaluation]
---

# Ingest: Gentle Coding Framework README

## Classification

This repository-root README is a code-repository artifact that functions as a practitioner design proposal and project overview. It defines three prompt-framing concepts, supplies example prompts, summarizes community benchmark results, and states a research roadmap without preserving the underlying experimental records.
Author: Otto Renner is the repository maintainer and identifies the framework as an open community project. The README says its sections were structured by him and its AI-generated or AI-summarized text was vetted and edited during generation; it also acknowledges that the prose is being rewritten.

## Summary

The README proposes three elements for human-LLM task framing: a low-stress collaborative "Gentle Mindset," a "Defined Winning Condition" that makes completion and exclusions explicit, and a "Safety-Token" that makes an uncertain or non-success response valid. It argues that this combination can reduce self-policing, loops, forced answers, token use, and latency, then gives exploratory and fixed-output prompt examples. A community-results table reports improvements for some model/settings but neutral N=100 results for Sonnet 4.6, Opus 4.6, and GPT-5.5. For this KB, the README is useful as a prompt-contract proposal and a map to evidence that must be assessed in its own primary sources, not as a controlled demonstration of the proposed mechanisms.

## Quotes

No source quotes have been retained yet.

## Connections Found

The README's durable role is a practitioner proposal for defining both successful and acceptable non-successful task outcomes. Its Defined Winning Condition rests on [fixing what the executor cannot determine](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), while its Safety-Token rests on the need for [structured recovery alongside enforcement](../notes/enforcement-without-structured-recovery-is-incomplete.md). Its anxiety, trauma, and engagement explanations also make it a useful case for [testing psychology-to-agent transfers per principle and failure mode](../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md), without establishing those explanations.

[Prompt Stability in Code LLMs](./prompt-stability-code-llms-emotion-personality-variations.ingest.md) is the controlled empirical counterpart for emotional and personality framing, while [Agent Behavioral Contracts](./agent-behavioral-contracts-formal-specification-runtime.ingest.md) is the formal runtime counterpart for fallback and escalation policy. The [Gentle-Coding Proof of Concept](./gentle-coding-proof-of-concept.ingest.md) separately owns the origin experiment, and the [Gentle-Coding Comparative Research Catalog](./gentle-coding-research.ingest.md) separately owns the annotated bibliography; they are companions, not evidence contained in this README.

## Extractable Value

1. **Success and non-success can be specified together** -- Defined Winning Condition fixes what counts as done, while Safety-Token adds an acceptable observable response when the primary result cannot be produced. This sharpens the task's response space beyond tone alone. [quick-win]

2. **The framework decomposes into independently testable prompt-contract variables** -- collaborative tone, stakes, completion criteria, role framing, and permitted fallback outputs can be varied separately even though the README recommends them as a bundle. [experiment]

3. **The reported null results bound the README's own generalization** -- neutral N=100 entries for three named frontier-model families argue against treating the proposed bundle as uniformly beneficial across models and settings. [just-a-reference]

4. **The benchmark table is a source lead rather than durable outcome evidence** -- its linked community study may contain the prompts, task cells, run records, model identifiers, and uncertainty needed to evaluate the reported token and latency deltas. [deep-dive]

5. **The psychological story can be separated from the engineering proposal** -- explicit goals and fallback responses can be evaluated through observable task behavior without assuming that an LLM experiences anxiety, trauma, or a human-like power dynamic. [quick-win]

## Limitations (our opinion)

This is editorial opinion. As a repository README and design proposal, the source reflects one maintainer's evolving, point-in-time account. Its concepts are stated more precisely than its causal explanations: claims about self-policing, panic, trauma-like behavior, RLHF pressure, and shareholder incentives are not established by evidence preserved in the README. The community table omits the compared prompts, task cells, run records, exact model identifiers, sampling settings, variance, and analysis, so its numerical summaries cannot be independently checked from this source.

The reported evaluations also leave their effective update space underspecified. The visible conditioning signals are task instructions plus compound social, stakes, success, and fallback framing; the permitted responses range from free-form explanations to a fixed success-or-help output. The black-box models can map those prompts to outputs, but their hypothesis classes, histories, provider prompts, harnesses, and decoding choices are not documented here. Because the proposed bundle changes several fixed design choices together, any improvement within that setup supports only the compound configuration in its tested context; it does not identify Gentle Mindset, Defined Winning Condition, or Safety-Token as the cause. The README's own neutral N=100 results further limit transfer across models.

## Recommended Next Action

Capture and ingest the README's linked `oh-my-pi` research PR as a separate primary source so its protocol and records, if present, can be checked before the benchmark table informs a KB claim.
