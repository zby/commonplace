---
description: "Tev1 uses supervised fine-tuning and ordinary token generation for finite-option decisions; development results bound its comparison with non-generating decision interfaces."
source: https://huggingface.co/togethercomputer/Tev1-4B-experimental
captured: "2026-10-24"
capture: trafilatura
capture_scope: partial-source
genre: tool-announcement
snapshot_sha256: 8a66921ea1c907c09dca81e38f01141f5a9764dcd080f7c8a6d07d0b3b1a5332
ingested: "2026-10-24"
type: types/ingest-report.md
domains: [typed-decisions, model-evaluation, supervised-fine-tuning]
learning_claims: true
---

# Ingest: Tev1-4B-experimental model card

## Classification

A producer's experimental model release card describing an intended decision interface, development measurements and deployment caveats. It is not an independent benchmark or a scientific paper.

Author: Together AI, the model producer. The card is direct evidence of the announced interface and acknowledged limitations, but an interested source for performance claims.

## Summary

Tev1-4B-experimental is Together AI's supervised fine-tune of Qwen3.5-4B for choosing among 2–24 labeled options from a supplied state and question. It retains the standard next-token language-model head: this is a Jev-inspired experiment, not a non-autoregressive Jev runtime. The intended response is one option letter, which application code maps to a semantic key; recommended inference disables thinking, uses temperature zero and allows eight output tokens. Within this supplied-state, finite-option, generative setup, the producer reports 880/1,000 correct main decisions, 300/300 correct policy-transfer decisions and 1,300/1,300 valid single-letter outputs. The evaluation mixture informed development, includes synthetic policy structures and has no untuned-Qwen baseline, so these are development observations, not evidence of a fine-tuning gain or superiority over other decision architectures. Injection resistance, calibration and broad distributional robustness remain insufficiently evaluated; local loading and the fine-tuned weights' release license also remain unsettled in the captured card.

## Quotes

> Tev1-4B-experimental is an experimental 4B decision model from Together AI. It is a supervised fine-tune of Qwen3.5-4B trained to choose one option from a structured state, question, and list of choices.
> 
> This is a Jev-inspired experiment, not a non-autoregressive Jev runtime. It retains Qwen’s standard next-token language-model head.
> --- `kb/sources/.snapshots/together-tev1-4b-20261024.md` @ `sha256:8a66921ea1c907c09dca81e38f01141f5a9764dcd080f7c8a6d07d0b3b1a5332`

> Provide a system instruction followed by a structured decision containing `state`, `question`, and 2–24 labeled `options`. The model should return exactly one option letter; application code maps that letter back to the semantic key.
> --- `kb/sources/.snapshots/together-tev1-4b-20261024.md` @ `sha256:8a66921ea1c907c09dca81e38f01141f5a9764dcd080f7c8a6d07d0b3b1a5332`

> These are development results, not an independent benchmark. The evaluation mixture informed model development, there is no untuned-Qwen baseline yet, and the policy-transfer set contains synthetic policy structures.
> --- `kb/sources/.snapshots/together-tev1-4b-20261024.md` @ `sha256:8a66921ea1c907c09dca81e38f01141f5a9764dcd080f7c8a6d07d0b3b1a5332`

## Connections Found

This source is an implementation counterpoint to [Basal 2.0 max](basal-2-0-max-20261024.ingest.md): both accept caller-described finite choices, but Tev1 generates an option letter through a standard language-model head, whereas Basal's documented engine reads option-code logits without generating text. A shared task interface does not establish a shared runtime, calibrated confidence or interchangeable behavior. Neither this card nor the comparison provides a matched experiment establishing which implementation is better for KB decisions.

It also illustrates the distinction in [Generation confidence does not by itself certify soundness](../theory/generation-confidence-does-not-by-itself-certify-soundness.md). Perfect output-format compliance in the development evaluation coexists with incorrect main-set decisions. The card reports no validated confidence output; neither the single-letter interface nor the retained next-token head supplies a correctness certificate.

## Learning Claims (our opinion)

The source describes supervised weight adaptation to structured decision examples. At inference, caller-supplied state, question and option descriptions specify the current problem; no request-driven weight update or retained correction loop is described. Learned behavior persists in the released checkpoint across requests, but the card does not demonstrate improvement over the untuned base model. Development accuracy and successful policy-transfer cases are observations of the resulting model, not isolation of the causal contribution of fine-tuning.

Against the four conditions of a [theory builder](../theory/definitions/theory-builder.md), localized content is present in textual policy states and option descriptions, but the card identifies no stated units carrying the learned weights' content. Consumption of the supplied content is the intended interface; the reported policy-transfer result gives limited outcome evidence for it, without controlled tests of operative content changes. Content-directed criticism of identified theories is not demonstrated by supervised fitting or aggregate error counts. Iteration is indicated by the admission that evaluation informed development, but the card does not show retained, stated criticism shaping successive theories. Thus the captured component is not established as a theory builder; the larger producer development process remains insufficiently described to classify. This does not rule out learning through weight adaptation.

The fixed-boundary distinction in [Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) bounds reuse. The model chooses among supplied options using supplied information; the card does not compare alternative state representations, option sets or readout mechanisms. Its results do not establish that a KB operator's categories preserve the distinctions a task needs. The source adds a concrete case separating persistent weight adaptation from request-local policy consumption, not evidence that consuming a new policy revises a retained theory.

## Extractable Value

1. **Separate a decision interface from its inference mechanism.** Tev1 shows that a finite-option interface can be implemented with ordinary token generation. Its Jev-inspired label does not establish a non-autoregressive runtime, and the Basal comparison concerns documented mechanisms, not measured relative efficiency or accuracy. [quick-win]
2. **Score format validity separately from semantic correctness.** The producer reports all 1,300 outputs as valid letters but only 880/1,000 main decisions as correct within its development setup. A KB routing trial should retain separate measures rather than treat parser success as successful judgment; these observations neither establish a training gain nor validate the supplied categories. [experiment]
3. **Retain an explicit application boundary.** The model returns a letter; application code resolves the semantic key. This makes option-to-action mapping an independently checkable interface, but does not make the chosen option correct or authorize automatic KB mutation. [just-a-reference]

## Limitations (our opinion)

The capture is marked partial-source. It contains extracted page text, not an inspected training recipe, checkpoint, linked repository or reproduction. No model, implementation or benchmark was executed. The linked training-cost tutorial does not establish this checkpoint's measured training cost, and generic platform-generated chat and image examples are not validation of its intended decision interface.

The central empirical limitation is the absence of an untuned-Qwen comparison and an independent evaluation. Because the development mixture informed model development, the scores cannot establish out-of-sample performance; the synthetic policy-transfer set does not establish transfer to real KB policy ambiguity. There is no controlled variation of the state/question/options decomposition or generative readout, and no reported ablation isolates a training choice. The measurements therefore do not warrant either a fine-tuning improvement claim or a preference over Basal or Jev.

The instruction to treat state as data is not evidence of injection resistance. The card explicitly leaves prompt injection, multilingual behavior, calibration and broad out-of-distribution robustness incompletely evaluated. Valid output in the tested requests is not a guarantee outside them; generic chat may produce prose. Local Transformers loading and exact environment requirements require validation. At this observation, the fine-tuned weights' release license is being finalized and dataset terms remain source-specific; the base model's Apache-2.0 license alone does not settle reuse permissions.

## Recommended Next Action

File this ingest as a source-only reference for finite-option decision-interface comparisons, without promoting its development scores into a KB model-selection or deployment recommendation.
