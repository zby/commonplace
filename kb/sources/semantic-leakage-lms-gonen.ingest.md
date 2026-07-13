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

This source is best read as the **association-mechanism anchor** for the KB's existing irrelevant-context evidence, not as a separate failure family.

**Closest mechanistic sibling:** [GSM-DC ingest](./gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) measures how **irrelevant context** degrades math reasoning via power-law distractor scaling. Gonen measures how **semantically unrelated but associatively linked** prompt fragments steer completions via learned concept links. Both treat flat prompt tokens as active interference sources the model cannot fully gate out. GSM-DC's limitation already flags that real distractors are "semantically richer" and "often partially relevant" — semantic leakage is exactly that harder regime: the distractor is not random noise but a **trained association channel**. The shared mechanism hypothesis: non-selective integration of prompt semantics into generation, below any explicit compliance or task contract.

**Soft-degradation axis:** Extends the relevance/interference dimension in [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). GSM-DC quantifies volume/noise; Gonen names the **semantic-similarity** variant where interference travels through embedding-space associations rather than distractor count alone.

**Contamination note:** Grounds the fine-grained leak signature in [context-contamination-operates-below-an-agents-compliance-reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md). That note's stance drift (evaluative lexicon, structural asymmetry) is a higher-dose, task-embedded case of the same non-isolation: prompt semantics shape output despite expressed refusal. Gonen does not test refusal, but establishes that association leakage is systematic — especially in instruction-tuned models, the same class used in agent workflows.

**Content-effects complement:** [Language Models, Like Humans, Show Content Effects on Reasoning](./language-models-like-humans-show-content-effects-on-reasoning.ingest.md) shows belief-congruent content shifts **reasoning accuracy** on logic tasks. Gonen shows unrelated concepts shift **generation content** on completion tasks. Together they cover content entanglement at both evaluation and production grains.

**Instruction-tuning paradox:** The finding that instruction-tuned models leak **more** extends [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md) with a cautionary counterpoint: alignment that rewards informative, content-rich completions may amplify associative steering from prompt surface features.

**Architectural response:** Reinforces [llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md) and [session-history-should-not-be-the-default-next-context](../notes/session-history-should-not-be-the-default-next-context.md) — if associations leak through tokens present in context, exclusion remains the reliable guarantee; "ignore this" does not remove the association channel.

## Extractable Value

1. **Semantic leakage as a named, measurable interference channel.** Leak-Rate with control/test prompt pairs gives the KB a vocabulary and metric for association-driven context interference distinct from distractor-count scaling (GSM-DC) and belief-congruent reasoning bias (Lampinen). High reach: the control/test design transfers to any setting where a contaminant can be A/B tested against a stripped control. [quick-win]

2. **Instruction-tuned models leak more — direct tension with "just instruct it to ignore."** The strongest models in agent stacks (GPT-4o, Llama-Instruct) show higher Leak-Rate than base counterparts. This is evidence that compliance-oriented fine-tuning does not close the association channel and may widen it. High reach for context-engineering and contamination notes. [quick-win]

3. **Mechanistic bridge to GSM-DC's "semantically richer distractors" gap.** GSM-DC's limitations section already predicts that semantic similarity between distractors and the task changes the degradation mechanism. Gonen provides the positive account: interference via learned associations, not just attention dilution from extra tokens. High reach for the planned multi-axis distraction synthesis. [experiment]

4. **Semantic priming as the cognitive parallel.** The paper explicitly links leakage to semantic priming (Meyer and Schvaneveldt, 1971), supporting [human-writing-structures-transfer-to-llms-because-failure-modes](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) and the KB's broader human-LLM failure-mode overlap thesis — but at the **association** grain rather than the reasoning-accuracy grain. [just-a-reference]

5. **Umbrella framing for stereotype and bias work.** Gendered nurse/doctor completions are presented as instances of semantic leakage, suggesting a single mechanism under many documented bias types. Moderate reach: framing is argued, not experimentally unified across bias benchmarks. [deep-dive]

6. **Open-ended and crosslingual persistence.** Leakage in storytelling and multilingual settings shows the phenomenon is not confined to short sentence-completion probes — relevant to agent casework where stance-bearing material sits in long, mixed-language context files. Moderate reach: open-ended evaluation is partly qualitative. [just-a-reference]

## Limitations (our opinion)

**What was not tested:**

- **No refusal or counter-instruction baselines.** The paper never asks models to ignore the injected concept or to maintain neutrality. It cannot speak to whether explicit compliance reasoning neutralizes leakage — the central question in [context-contamination-operates-below-an-agents-compliance-reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md). GSM-DC similarly omits "ignore irrelevant information" baselines; both leave the instruction-vs-exclusion distinction empirically open.

- **Association strength confounded with plausibility.** Many test cases ("likes koalas" → eucalyptus leaves) are associations humans also make. The metric detects *overrepresentation* relative to control, not whether the completion is wrong for the task. Stance-drift contamination in agent casework often involves subtler, task-appropriate language that still leans directionally — a harder signature than Gonen's forced children's-story completions.

- **Models are one to two generations old.** GPT-3.5/4/4o and Llama 2/3; no extended-reasoning or process-reward architectures. Whether newer models reduce or relocate leakage is unknown. Your Substack observation that the canonical yellow/school-bus example no longer reproduces on current models is a live validity concern for specific instances, though the paper's aggregate Leak-Rate across 109 prompts is the durable claim.

- **Embedding-dependent automatic metric.** Leak-Rate depends on BERT-score, SentenceBERT, or OpenAI embeddings. Human validation is solid (high interannotator agreement), but cross-metric disagreement on GPT models (OpenAI embeddings diverge) limits precision for comparing families.

- **No scoping or context-exclusion baselines.** Like GSM-DC, the paper tests in flat prompt settings only. It cannot assess whether architectural exclusion (sub-agent frames, contaminant removal) outperforms accepting the association channel.

- **Short-generation bias.** Most prompts prime single-phrase completions; open-ended sections are exploratory. Agent contamination signatures (structural asymmetry, provenance promotion) operate at document grain and may compound many low-dose association leaks.

## Recommended Next Action

Update [context-contamination-operates-below-an-agents-compliance-reasoning.md](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md): add this source as `evidence` for the mechanistic claim that fine-grained stance drift is an instance of non-selective semantic integration (semantic leakage), with GSM-DC and Lampinen cited as the adjacent noise and content-bias axes — and note explicitly that Gonen establishes systematic association leakage but does not test refusal, so the below-compliance-reasoning claim remains supported by the epistack experiment, not by this paper alone.