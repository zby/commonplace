---
description: "Perplexity's decision checkpoint shows task-dependent joint-question effects, specialized serving needs and limits on calibration transfer."
source: https://huggingface.co/perplexity-ai/pplx-decider-v1.2
captured: "2026-10-24"
capture: trafilatura
capture_scope: partial-source
genre: tool-announcement
snapshot_sha256: 6c782c27e5971fee23451a5d4da0f8b2124a0fef24509a4c5d57f62123d5d112
ingested: "2026-10-24"
type: types/ingest-report.md
domains: [decision-models, evaluation, calibration]
learning_claims: true
---

# Ingest: Perplexity pplx-decider-v1.2

## Classification

A producer model card announcing a decision checkpoint, documenting its request protocol and reporting benchmarks, calibration and serving measurements. It is not an independent evaluation or a scientific paper.
Author: Perplexity AI, the checkpoint's developer and the source of the reported measurements.

## Summary

Perplexity presents a Qwen3.8-27B-based model that answers bounded choice, binary-probability and ordinal-score questions without generating answer text. A request contains shared state and questions, each with a marker-position readout through a separate 255-row decision head. Full-attention layers are noncausal within the request, so questions influence one another. On this checkpoint, grouping questions improves some related-facet tasks but worsens several independent-candidate tasks; the overall Decision Index score is 68.09 jointly versus 67.75 with separate questions. The larger gain over v1.1's 62.30 also includes changed training data and does not isolate the joint format. Temperature calibration improves reported development-set calibration but leaves held-out decision tasks somewhat overconfident. The card describes request-isolated fast-path packing and roughly twofold throughput gains on a GB200, while warning that ordinary causal serving cannot reproduce the checkpoint and that lengths beyond roughly 32k training tokens are only spot-checked.

## Quotes

> | Type | `criteria` | Answer | 
> |---|---|---|
> | `choice` | `{option_name: description or None}` , 1 to 255 options | `choice` ,`probabilities` (per option),`confidence` | 
> | `noul` | optional `{"true": description, "false": description}` | `noul` = P(true) | 
> | `score` | list of 2 to 255 level descriptions, lowest first | `score` (expected level index),`probabilities` ,`legend` ,`confidence` |
> --- `kb/sources/.snapshots/perplexity-decider-v1-2-20261024.md` @ `sha256:6c782c27e5971fee23451a5d4da0f8b2124a0fef24509a4c5d57f62123d5d112`

> All questions in a request share one sequence. Full attention is noncausal, so every question attends to the state
> and to every other question. This changes the answers. Grouping helps when the questions are **facets of one
> decision**, and hurts when they are **independent candidates** competing for the same judgement:
> --- `kb/sources/.snapshots/perplexity-decider-v1-2-20261024.md` @ `sha256:6c782c27e5971fee23451a5d4da0f8b2124a0fef24509a4c5d57f62123d5d112`

> This is the native decision-checkpoint layout: a `Qwen3_5Model` backbone plus `readout.safetensors`, a BF16
> `[255, 5120]` decision head. The Transformers class name does not change the base model identity, Qwen3.8-27B.
> `joint_config.json` declares the request protocol (`version: 3`, `joint-question-inline-readout-v1`, marker
> `<|fim_suffix|>`).
> 
> - Full-attention layers are **noncausal** over the whole request. The linear-attention layers keep their native
> causal behavior. Default causal inference does not reproduce this checkpoint.
> - The readout is applied at each `<|fim_suffix|>` marker, one per question, not at the last token. Literal special
> tokens in user content are neutralized before tokenization, so user text cannot create markers.
> - This artifact has a separate readout, **not a full-vocabulary `lm_head`** . A serving system needs both the
> noncausal attention and the per-marker readout. Readout row`i` corresponds to vocabulary row`decision_config.json["token_ids"][i]` .
> --- `kb/sources/.snapshots/perplexity-decider-v1-2-20261024.md` @ `sha256:6c782c27e5971fee23451a5d4da0f8b2124a0fef24509a4c5d57f62123d5d112`

> `decision_config.json` stores the temperature fitted on held-out calibration data (1.382 for this
> checkpoint). `decide` applies it exactly once, then normalizes a softmax over each question's valid options only.
> `decide(..., temperature=t)` overrides it. When you use `logits` directly, divide by the saved temperature before the
> softmax, and do not include the unused codes. It was fitted in the joint format, on data separate from
> the development set. On the development set (1,497 questions) it gives accuracy
> 91.3%, ECE 0.014 and Brier 0.134 (without temperature: ECE 0.033, Brier 0.137). On decision datasets held out from
> all training, probabilities remain somewhat over-confident (ECE about 0.05), as for every model we measured,
> though less so than v1.1.
> --- `kb/sources/.snapshots/perplexity-decider-v1-2-20261024.md` @ `sha256:6c782c27e5971fee23451a5d4da0f8b2124a0fef24509a4c5d57f62123d5d112`

## Connections Found

The card provides a concrete comparison for [error correction with decorrelated checks](../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md): multiple question readouts in one request explicitly share information and must not be counted as independent verification merely because they produce separate answers. Its joint-versus-separate evaluation varies question grouping within this checkpoint, not reviewer independence or error decorrelation. Separate requests remove this direct cross-question attention path but do not establish independent errors. The source therefore supplies a mechanism-level warning for KB evaluation design, not evidence that voting or verification has become reliable.

## Learning Claims (our opinion)

The reported adaptation is offline: revised decision-training data, inclusion of official benchmark training splits with claimed test decontamination, and averaging weights from several training runs. Evaluation tracking and compromise across tasks guide model selection. The card reports improvements on tasks held out from all training as well as public benchmarks, but supplies no isolated data ablation that attributes the gains to a particular addition. Joint-question interaction at inference changes predictions; it is not itself persistent learning.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the deployed checkpoint exposes localized request instructions and options, but does not show retained, stated theories encoding its learned decision rules. Consumption of instructions is documented by the interface; consumption of retained theories through their stated content is not established. Content-directed criticism of identified theory units is not shown. Iteration is reported for the producer's training and evaluation process, but the card does not establish that retained, stated criticisms shape successive theories. Learned changes persist across requests through the released weights; the inference interface documents no update from one request to the next. These boundaries do not rule out learning: producer-reported held-out gains support improved future decision capacity within the evaluated tasks, independently of whether the system meets the theory-builder conditions.

The [fixed-decomposition distinction](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters here. Training adjusts behavior within a bounded-option interface and a supplied state/question representation; the retained account does not expose the full training hypothesis space. The grouping comparison tests one consequential partition inside that design. It does not compare bounded decisions with alternative output representations or establish that this head and protocol are preferable to a generative system for KB review.

## Extractable Value

1. **Treat question grouping as a semantic intervention, not just batching.** With this checkpoint's noncausal cross-question attention and marker readouts fixed, grouping yields +11.3 points on SATA-Bench but −4.8 on ToolRet; BEIR's 13-dataset macro comparison is −0.5 nDCG@10 points. A KB experiment should distinguish related review facets from competing retrieval candidates rather than transfer the aggregate score. [experiment]
2. **Separate probability calibration from decision correctness.** The card reports development ECE falling from 0.033 to 0.014 after temperature scaling, while held-out decision-task ECE remains about 0.05. These producer measurements justify checking calibration on the intended KB task before using probabilities as acceptance thresholds; they do not supply such thresholds. [experiment]
3. **Preserve serving semantics when comparing implementations.** The documented protocol requires noncausal full-attention layers and per-marker readout, not ordinary causal next-token scoring. Fast-path requests remain isolated even though questions within a request interact. This distinction is reusable when specifying what counts as an equivalent decision-model deployment. [just-a-reference]

## Limitations (our opinion)

The partial-source capture retains model-card text, not the linked implementation, weights, complete datasets or a reproduction. No code was inspected or executed. Serving behavior and all numerical outcomes remain producer reports; this ingest cannot establish implementation fidelity or independent benchmark validity.

The version comparison changes training data and request format together, so its improvement cannot be attributed to joint questions alone. The within-v1.2 grouping comparison is narrower and more informative about request partitioning, but it holds the specialized checkpoint, head and option representation fixed. Neither comparison demonstrates superiority over alternative decision architectures for KB operations. Inclusion of official benchmark training splits also changes the interpretation of public-suite gains; claimed decontamination does not make those tasks fully out of domain.

Calibration was fitted in the joint format, and the retained evidence does not establish transfer to separate-request KB judgments or new class distributions. Grouping effects are task-dependent; removing direct question interaction does not measure decorrelation, as the connected reliability note requires. GB200 throughput and BF16 agreement measurements do not establish affordable deployment on other hardware or interchangeable probabilities near thresholds. Long-context fact retrieval beyond the training range is a narrow spot-check, not validation of complex long-context decisions.

## Recommended Next Action

Review `kb/theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` for a scoped example distinguishing multiple jointly attended decision readouts from decorrelated verification checks, using this model card as a producer-reported mechanism rather than a reliability result.
