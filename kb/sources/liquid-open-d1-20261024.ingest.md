---
description: "Liquid AI reports one-pass multimodal decision models and device-specific latency, offering a bounded comparison for offloading KB judgments rather than evidence of a general speed advantage."
source: https://www.liquid.ai/blog/open-d1
captured: "2026-10-24"
capture: trafilatura
capture_scope: partial-source
genre: tool-announcement
snapshot_sha256: b3d6180f06d1c5ddb0a1e46b2359dbf094fc175eacfc7e7c651e3fce254c7854
ingested: "2026-10-24"
type: types/ingest-report.md
domains: [decision-models, model-training, edge-inference]
learning_claims: true
---

# Ingest: Open d1: Edge decision models for text, vision, and audio

## Classification

A producer release announcement combining architecture and training descriptions with benchmark and hardware measurements. It advertises downloadable weights and demos rather than presenting a controlled research study.
Author: Liquid AI, the models' developer; direct knowledge of the release, with a commercial interest in its framing.

## Summary

Liquid AI introduces d1-3B and the experimental d1-omni-600M as models that answer decision questions in one forward pass without generating tokens. The former derives from a decoder-only vision-language model; the latter combines a bidirectional text encoder with vision and audio encoders. Liquid reports a public Decision Index v0.2.1 score of 48.57 for d1-3B and 15.95 for d1-omni-600M, plus seven text benchmarks where their means are 82.9 and 78.4 against Decider 4B's 81.1 and Decider 2B's 77.1. These are comparisons of complete models within the supplied decision tasks, not controlled tests of decoder versus encoder architecture or decision versus generation interfaces. Reported d1-3B single-question latency ranges from 8 ms on an RTX 4090 to 50 ms on an Orin Nano; longer states are substantially slower. The announcement makes specialized judgment offloading worth investigating, but does not demonstrate its reliability or net benefit for KB operations.

## Quotes

> Unlike our generative Liquid Foundation Models (LFMs), our d1 decision models don’t produce tokens. Instead, they produce an answer in a single forward pass.
> 
> d1-3B and d1-omni-600M are trained from two very different backbones:
> 
> - **d1-3B** is trained from[LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) , our latest VLM, which is decoder-only. It accepts text and images as inputs.
> - **d1-omni-600M** is trained from[LFM2.5-Encoder-350M](https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M) , a bidirectional encoder. It adds vision and audio encoders to handle all three modalities. It accepts either text and image, or text and audio as inputs.
> --- `kb/sources/.snapshots/liquid-open-d1-20261024.md` @ `sha256:b3d6180f06d1c5ddb0a1e46b2359dbf094fc175eacfc7e7c651e3fce254c7854`

> **d1-3B.** We averaged the weights of LFM2.5-2.6B and the text backbone of LFM2.5-VL-3B to create a better base model. We then fine-tuned checkpoints with different random seeds and data mixtures before merging them again. Training on long inputs, shuffling answer options, and fixing shortcuts in the data made a bigger difference than more advanced techniques.
> --- `kb/sources/.snapshots/liquid-open-d1-20261024.md` @ `sha256:b3d6180f06d1c5ddb0a1e46b2359dbf094fc175eacfc7e7c651e3fce254c7854`

> Since decision models don’t generate output tokens, we measure end-to-end latency, from input to output. We report inference numbers for d1-3B. d1-omni-600M is an early research release and is under active development.
> 
> **Edge inference.** We measure latency on an Apple M5 Pro and, in collaboration with NVIDIA, on an NVIDIA Jetson AGX Thor, a Jetson AGX Orin 64 GB, and a Jetson Orin Nano. We measure one request at a time, across a single question, three questions over one state, a 3.4K-token state, and a 384px image.
> --- `kb/sources/.snapshots/liquid-open-d1-20261024.md` @ `sha256:b3d6180f06d1c5ddb0a1e46b2359dbf094fc175eacfc7e7c651e3fce254c7854`

## Connections Found

The source is a concrete comparison for [Semantic work can be relocated but not eliminated](../theory/semantic-work-can-be-relocated-but-not-eliminated.md): semantic judgment remains in a trained model even when the output path avoids token generation. Training pays for reusable regularities, while each new input still incurs inference. The device and long-state measurements make that remaining cost visible. This illustrates placement of judgment rather than testing the note's general explanation. The reported model comparisons hold the benchmark decision tasks fixed; they do not show that replacing a generative KB worker with this decision interface preserves the worker's useful distinctions or quality.

## Learning Claims (our opinion)

The source describes offline weight adaptation, not learning during deployment. For d1-3B, Liquid averages backbone weights, fine-tunes with different seeds and data mixtures, and merges checkpoints. It says long-input training, answer-option shuffling, and removing data shortcuts mattered more than advanced techniques, but supplies no isolating ablations. For d1-omni-600M, staged training introduces audio and vision through encoders and adapters; some stages freeze the text backbone or vision encoder, and a later stage fine-tunes the full model. Freezing is therefore stage-specific, not a permanent limit on every parameter.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the deployed model does not demonstrate localized retained theories: no identified weight unit is shown to state a claim. Its answers demonstrate input-sensitive computation, but not consumption of such retained theories. Training losses and benchmark scores provide error signals, not demonstrated content-directed criticism of identified statements. Retained checkpoints carry weight updates into later training stages, but the account does not show a retained criticism shaping a next stated conjecture. The wider developer process may meet these conditions; this release description does not establish that. Checkpoints persist across deployment runs, without evidence of accumulating deployment experience.

This leaves ordinary learning possible without establishing theory building. The reported final-model scores show task competence relative to selected rivals, not how much a particular training operation improved future capacity. As [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) warns, training within the chosen input modalities, decision interface, and benchmark tasks does not validate that decomposition for a new objective. The two models also differ in size, backbone, and training, so their score difference cannot isolate any one architectural choice. Nothing here requires revising Commonplace's distinction between weight adaptation and criticism of stated theories.

## Extractable Value

1. **A concrete candidate for specialized judgment offloading.** One-pass, non-generative decisions provide a testable alternative execution path for a bounded KB classification task. The reported comparisons concern complete models on decision benchmarks, not a matched-quality replacement for a generative KB worker. [experiment]
2. **Workload-sensitive latency as an evaluation requirement.** On Orin Nano, the reported 50 ms single-question result becomes 1,640 ms for a 3.4K-token state. Any offloading experiment should measure representative context lengths and end-to-end cost rather than transfer the headline latency to document-scale judgments. [quick-win]
3. **Training recipes as hypotheses, not causal findings.** Option shuffling and shortcut removal are plausible interventions for decision training, but the announcement does not quantify their separate effects. Retain them as experiment candidates rather than established priorities over other techniques. [just-a-reference]

## Limitations (our opinion)

The partial-source capture retains extracted release text, not linked weights, code, embedded demos, or a reproduction package. It cannot establish implementation details beyond the announcement or independently verify the reported results. No code was inspected or executed for this ingest.

The benchmark tables compare whole model packages without controlling backbone, parameter count, data mixture, or training recipe. They establish neither the cause of the differences nor superiority of a one-pass decision interface over generation at matched quality. Public-split scores and seven text benchmarks do not establish calibration, abstention quality, or robustness on KB judgments. The producer itself omits the private vision split and identifies dedicated audio decision benchmarks as an open problem; demos are weaker evidence than quantified multimodal evaluation.

Hardware numbers are workload-specific producer measurements, not a controlled comparison with another execution path. The extracted account lacks enough measurement configuration to transfer them confidently to another deployment. Its prose also overstates strict latency boundaries: the table lists 50 ms on Orin Nano and 18 ms for an MI325X image, despite saying under 50 ms and under 18 ms respectively. Use the tabulated values rather than those strict inequalities.

## Recommended Next Action

Retain this ingest as a source-only reference for specialized judgment offloading until a concrete KB classification task supplies a meaningful quality-and-latency comparison.
