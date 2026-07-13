---
description: "Semantic leakage — undue prompt-to-generation association from unrelated context — measured by control/test Leak-Rate across 13 models; instruction-tuned models leak more"
source_snapshot: semantic-leakage-lms-gonen.md
ingested: "2026-07-13"
type: kb/sources/types/ingest-report.md
domains: [context-degradation, reasoning-robustness, llm-bias, evaluation-benchmarks]
---

# Ingest: Does Liking Yellow Imply Driving a School Bus? Semantic Leakage in Language Models

Source: semantic-leakage-lms-gonen.md
Captured: 2026-07-13
From: https://arxiv.org/html/2408.06518v3

## Classification

Genre: **scientific-paper** — preprint with a novel phenomenon definition, curated 109-prompt test suite, automatic and human evaluation across 13 GPT and Llama models, and multilingual/open-ended extensions.

Domains: context-degradation, reasoning-robustness, llm-bias, evaluation-benchmarks

Author: Gonen, Blevins, Liu, Zettlemoyer, Smith (University of Washington / Allen Institute for AI). Credible NLP faculty line; contribution is naming and operationalizing a broad association-bias family with a reproducible control/test metric rather than a single-task benchmark win.

## Summary

Gonen et al. define **semantic leakage**: generations that reflect undue semantic influence from prompt words that should not govern the completion ("He likes yellow. He works as a" → "school bus driver"). They operationalize it with paired **control** and **test** prompts that differ only by an injected unrelated concept, then score **Leak-Rate** — the fraction of instances where the test generation is more semantically similar to the concept than the control generation (chance = 50%). Across 109 hand-crafted prompts (colors, animals, food, occupations, idioms), 13 models, four temperatures, and three embedding metrics, Leak-Rate stays well above 50% with human validation. Key findings: leakage is universal across tested models; **instruction-tuned variants leak more** than base models (Llama chat/instruct; GPT-4o > GPT-4 > GPT-3.5); lower Llama temperature increases leakage; leakage persists in Chinese, Hebrew, crosslingual, storytelling, and recipe generation. The authors frame semantic leakage as an umbrella over stereotype bias and relate it to psychological semantic priming and to distraction via overshadowing (Zhang et al., 2024).

## Connections Found

This source is the **association-mechanism anchor** for the KB's irrelevant-context evidence — not a separate failure family, but the named channel behind several existing claims that currently describe interference architecturally without a measured mechanism.

**Sibling sources (compares-with):** [GSM-DC ingest](./gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md), [Lampinen ingest](./language-models-like-humans-show-content-effects-on-reasoning.ingest.md), and ConvexBench (via GSM-DC ingest) are **not independent interference axes** — they stress the same mechanism under different experimental regimes. The shared mechanism: **prompt semantics integrate non-selectively into generation** because context is flat and unscoped ([llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md)). What differs is measurement surface, not underlying cause: GSM-DC varies distractor *count* (math reasoning errors); Gonen varies injected *concepts* (completion Leak-Rate); Lampinen varies belief-congruence (logic-task accuracy); ConvexBench varies compositional *depth* (symbolic collapse). Random template distractors (GSM-DC) are the easy control condition; semantically linked but task-irrelevant material (Gonen, Lampinen, real agent contaminants) is the realistic case of the same integration failure. A four-axis taxonomy would mistake benchmark labels for mechanisms.

**Context-engineering cluster (evidence / rationale):** Grounds the relevance/interference claim in [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) with a named mechanism (non-selective semantic integration) rather than treating volume, noise, and association as separate degradation families. Grounds [context-contamination-operates-below-an-agents-compliance-reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md): stance drift is a higher-dose, task-embedded case of the same non-isolation, with "semantic leakage" supplying vocabulary the note's "diffuse steering" lacks (Gonen does not test refusal). Names a measured channel for the contamination failure mode in [agent-orchestration-needs-coordination-guarantees-not-just](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md). Reinforces [llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md) and [session-history-should-not-be-the-default-next-context](../notes/session-history-should-not-be-the-default-next-context.md): Leak-Rate above chance in flat prompts shows task-irrelevant tokens steer generation; exclusion, not instruction, removes the channel.

**Interpretation-error cluster (evidence / extends):** Extends [interpretation-errors-are-failures-of-the-interpreter](../notes/interpretation-errors-are-failures-of-the-interpreter.md) — association bias and Lampinen's content effects are the same interpreter failure (output distribution steered by prompt semantics the task contract does not license) measured on different task grains (generation vs deductive reasoning). Extends [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md): association leakage is another shared-across-models correlated error source; metamorphic checks that add/remove unrelated prompt fragments could probe it the way content reframing probes belief bias. Supports [topology-isolation-and-verification-form-a-causal-chain-for-reliable](../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md): shared context should bias a judge toward the generator's association errors, and Gonen shows that channel is systematic in instruction-tuned models.

**Human-LLM overlap and instruction tuning (evidence / extends):** Second empirical pillar for [human-writing-structures-transfer-to-llms-because-failure-modes](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) beside Lampinen — semantic priming at generation grain, not reasoning-accuracy grain. **Instruction-tuning paradox (productive tension, not contradiction):** Lampinen finds instruction tuning does not reduce content effects on reasoning; Gonen finds instruction-tuned models leak *more* on generation associations. [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md) should treat these as different phenomena — alignment may reward content-rich completions that widen associative steering even while reasoning bias persists.

**Metric design (see-also):** [process-structure-and-output-structure-are-independent-levers](../notes/process-structure-and-output-structure-are-independent-levers.md) already cites GSM-DC's PAcc/SAcc split; Gonen's control/test Leak-Rate is the parallel A/B metric for association interference at generation grain.

**Not the same failure family:** Flat-memory cross-contamination ([flat-memory-predicts-specific-cross-contamination-failures-that-are](../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md)) and harness skill-discovery leakage ([skill-discovery-re-fires-in-every-sub-agent-context](../notes/skill-discovery-re-fires-in-every-sub-agent-context.md)) share "contamination"/"leak" vocabulary but address memory-role collapse and discovery surfaces, not prompt-token association steering.

## Extractable Value

1. **Semantic leakage names the mechanism the sibling benchmarks circle.** Leak-Rate with control/test prompt pairs gives vocabulary for non-selective prompt integration — the same failure GSM-DC measures as distractor-induced reasoning error and Lampinen as content-congruent logic bias. High reach: control/test design transfers to any contaminant A/B test. [quick-win]

2. **Instruction-tuned models leak more — direct tension with "just instruct it to ignore."** The strongest models in agent stacks (GPT-4o, Llama-Instruct) show higher Leak-Rate than base counterparts. This is evidence that compliance-oriented fine-tuning does not close the association channel and may widen it. High reach for context-engineering and contamination notes. [quick-win]

3. **Reframes the GSM-DC ingest's multi-axis synthesis as premature.** Converging benchmarks (GSM-DC, Lampinen, Gonen, ConvexBench) are evidence for one mechanism surfacing under different doses and task shapes — not independent axes requiring axis-specific mitigations. The durable synthesis is mechanism + architectural remedy (exclusion/scoping), not a taxonomy of distraction types. Gonen makes explicit what GSM-DC's "semantically richer distractors" limitation already implied. [experiment]

4. **Association bias as a decorrelation problem.** Shared across model families like Lampinen's content effects, association leakage is another correlated-error source for [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md). Metamorphic add/remove of unrelated prompt fragments could probe it. [experiment]

5. **Instruction-tuning paradox cluster.** Reasoning content bias unchanged (Lampinen) vs generation association amplified (Gonen) — do not collapse into one "instruction tuning fails" claim; different tasks and metrics. Qualifies [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md). [quick-win]

6. **Semantic priming as the cognitive parallel.** Paper links leakage to semantic priming (Meyer and Schvaneveldt, 1971) — second empirical pillar for [human-writing-structures-transfer-to-llms-because-failure-modes](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) beside Lampinen, at generation grain. [just-a-reference]

7. **Open-ended and crosslingual persistence.** Leakage in storytelling and multilingual settings is not confined to short completions — relevant to long, mixed-language agent context files. Moderate reach: open-ended evaluation is partly qualitative. [just-a-reference]

## Limitations (our opinion)

**What was not tested:**

- **No refusal or counter-instruction baselines.** The paper never asks models to ignore the injected concept or to maintain neutrality. It cannot speak to whether explicit compliance reasoning neutralizes leakage — the central question in [context-contamination-operates-below-an-agents-compliance-reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md). GSM-DC similarly omits "ignore irrelevant information" baselines; both leave the instruction-vs-exclusion distinction empirically open.

- **Association strength confounded with plausibility.** Many test cases ("likes koalas" → eucalyptus leaves) are associations humans also make. The metric detects *overrepresentation* relative to control, not whether the completion is wrong for the task. Stance-drift contamination in agent casework often involves subtler, task-appropriate language that still leans directionally — a harder signature than Gonen's forced children's-story completions.

- **Models are one to two generations old.** GPT-3.5/4/4o and Llama 2/3; no extended-reasoning or process-reward architectures. Whether newer models reduce or relocate leakage is unknown. Your Substack observation that the canonical yellow/school-bus example no longer reproduces on current models is a live validity concern for specific instances, though the paper's aggregate Leak-Rate across 109 prompts is the durable claim.

- **Embedding-dependent automatic metric.** Leak-Rate depends on BERT-score, SentenceBERT, or OpenAI embeddings. Human validation is solid (high interannotator agreement), but cross-metric disagreement on GPT models (OpenAI embeddings diverge) limits precision for comparing families.

- **No scoping or context-exclusion baselines.** Like GSM-DC, the paper tests in flat prompt settings only. It cannot assess whether architectural exclusion (sub-agent frames, contaminant removal) outperforms accepting the association channel.

- **Short-generation bias.** Most prompts prime single-phrase completions; open-ended sections are exploratory. Agent contamination signatures (structural asymmetry, provenance promotion) operate at document grain and may compound many low-dose association leaks.

- **Do not over-merge instruction-tuning findings.** Lampinen (reasoning content effects unchanged by instruction tuning) and Gonen (generation leakage increased) measure different phenomena. Treating them as one "alignment fails" claim would misstate both.

## Recommended Next Action

Update [context-contamination-operates-below-an-agents-compliance-reasoning.md](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md): add this ingest as `evidence` naming **semantic leakage** as the measured form of non-selective prompt integration behind diffuse stance steering; cite GSM-DC and Lampinen as the same mechanism under different benchmark regimes (not separate axes); state that Gonen establishes systematic association leakage (especially in instruction-tuned models) but does not test refusal — so the below-compliance-reasoning claim remains on the epistack experiment.