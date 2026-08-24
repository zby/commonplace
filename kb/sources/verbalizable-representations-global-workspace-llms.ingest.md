---
description: "Anthropic J-space paper as evidence for probeable parametric state, activation-vs-presence, and externalized reasoning as internal-workspace relief"
source: https://transformer-circuits.pub/2026/workspace/index.html
captured: "2026-07-06"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 2aefd13b249fec2f2f789aba269fd1c5e4eaee5e533ca53bc6ff3457db384a53
ingested: "2026-07-06"
type: kb/sources/types/ingest-report.md
domains: [interpretability, activation, learning-theory, observability]
---

# Ingest: Verbalizable Representations Form a Global Workspace in Language Models

## Classification

Anthropic Transformer Circuits research article with a new interpretability method, causal interventions, ablations, task batteries, training experiments, and limitations.
Author: Anthropic interpretability researchers; strong author signal for access to Claude-family internals and concrete experiments, with the normal vendor and closed-model replication caveats.

## Summary

The paper introduces the Jacobian lens, a method for reading token-aligned, verbalizable directions in model activations, and defines the J-space as sparse combinations of those directions. It argues that this J-space functions like a limited global workspace: concepts in it can be reported, deliberately modulated, used as intermediates in flexible reasoning, broadcast to downstream computations, and selectively bypassed by automatic processing. The strongest experiments use swaps and ablations to show causal roles, then apply the lens to alignment auditing, post-training's installation of an Assistant point of view, and counterfactual reflection training, where training on hypothetical reflective continuations changes behavior in the original unreflected contexts. The paper is explicit that this is a functional analogy, not a claim that LLMs reproduce human global-workspace architecture or settle consciousness questions.

## Claims

- **Claim (paraphrase):** In controlled language-identification and character-counting tasks, the same underlying information could support automatic computation without causally routing through the measured J-space, while explicit report and flexible inference depended on J-space representations; task demands could surface otherwise absent information into that space.
  - **Source extract (verbatim):** Taken together, the two experiments show that many computations, which we might call “automatic,” do not causally route through the J-space.
  - **Source location:** “The J-space selectively mediates flexible but not automatic cognition.”
  - **Source extract (verbatim):** In some cases, the information relevant to the automatic computation is present in the J-space but unused for the task; in others, it is not present at all.
  - **Source location:** “The J-space selectively mediates flexible but not automatic cognition.”
  - **Source extract (verbatim):** By contrast, explicit report and flexible computation tasks depend on the J-space, and in tasks where the relevant information is not by default present in the J-space, that information can be surfaced to the J-space on demand (similar to the effect seen in ??).
  - **Source location:** “The J-space selectively mediates flexible but not automatic cognition.”
  - **Source extract (verbatim):** Notably, in all cases—automatic tasks, report, and flexible computation—the same underlying information is available to the model and used for task computations.
  - **Source location:** “The J-space selectively mediates flexible but not automatic cognition.”
  - **Scope:** Controlled passage-continuation, anomaly-detection, explicit-report, and flexible-inference tasks using J-lens readouts and coordinate-swap interventions in the evaluated Claude production models.
  - **Confidence:** High for the reported task-specific causal contrast: the same stimuli are paired with different questions, and targeted interventions affect explicit and flexible outputs while leaving the automatic outputs largely unchanged.
  - **Limitation:** J-space is an approximate, partially observed representational subspace, not the model's entire active context. The experiments do not establish that arbitrary context-visible information is consciously “read,” predict when it will affect an agent action, or show that every flexible computation uses this route.

- **Claim (paraphrase):** In the paper's Sonnet 4.5 experiments, J-space ablation selectively impaired multi-hop and context-dependent flexible generation while leaving many shallow classification, extraction, and ordinary next-token predictions largely intact; the measured J-space carried a small share of activation variance and its contents were preferentially relayed across layers and token positions.
  - **Source extract (verbatim):** We find that at most positions, J-space ablation perturbs the model's next-token prediction substantially less than in the multihop case (Figure ??).
  - **Source location:** “J-space ablation leaves most capabilities intact while impairing internal reasoning.”
  - **Source extract (verbatim):** Tasks that can be solved by shallow classifications, comparisons, or factual recall—MMLU multiple choice , odd-one-out, SQuAD extractive QA , sentiment classification, CoLA acceptability —are essentially unaffected even under heavy ablation, with scores remaining at or near the unablated Sonnet 4.5 baseline.
  - **Source location:** “J-space ablation leaves most capabilities intact while impairing internal reasoning.”
  - **Source extract (verbatim):** The excess variance explained is modest, never exceeding 10%, indicating that the model's activations are dominated by information outside the J-space.
  - **Source location:** “Capacity of the J-space.”
  - **Source extract (verbatim):** Taken together, our results suggest that the model’s weights are configured to broadcast J-space content disproportionately strongly, along both the depth and sequence axes.
  - **Source location:** “The J-space is a broadcast hub.”
  - **Scope:** J-lens-based interventions and ablations in Sonnet 4.5 and related evaluated Claude models, including a fourteen-task battery, controlled multi-hop prompts, pretraining-like text, sparse-decomposition capacity estimates, and weight-based broadcast analyses.
  - **Confidence:** Moderate to high for selective causal involvement and preferential broadcast within the paper's operationalization; several intervention types and matched controls converge on the same bounded pattern.
  - **Limitation:** The study does not vary long-context volume, irrelevant-context load, or dependency depth against J-space occupancy. Its lens captures only a small, single-token-oriented part of representation, and the authors cannot predict which arbitrary tasks will engage it, so it does not establish J-space competition as the general mechanism of long-context degradation.

- **Claim (paraphrase):** In the paper's Sonnet 4.5 task battery, GSM8K with explicit chain-of-thought was substantially more robust to J-space ablation than direct answering on the same problems; the authors interpret this as written intermediate steps externalizing information the model would otherwise carry in J-space.
  - **Source extract (verbatim):** Notably, the math evaluation GSM8K solved with explicit chain-of-thought is substantially more robust to ablation than the same problems answered directly. We interpret this as the model externalizing onto the page what it would otherwise have to carry in the J-space : writing out the intermediate steps reduces its dependence on an internal workspace to hold them.
  - **Source location:** "J-space ablation leaves most capabilities intact while impairing internal reasoning," discussion of Figure 24
  - **Scope:** Sonnet 4.5 on the paper's GSM8K conditions under light, medium, and heavy J-space ablation, with scores normalized to the unablated Sonnet 4.5 condition.
  - **Confidence:** High for the reported direction of the comparison and moderate for the externalization mechanism, which the authors explicitly present as their interpretation.
  - **Limitation:** Explicit chain-of-thought changes visible output content and length as well as the opportunity to externalize intermediate computation; the comparison does not independently manipulate reasoning process while holding output structure fixed.

- **Claim (paraphrase):** Counterfactual reflection training fine-tuned Claude Haiku 4.5 only on appended, constitution-grounded natural-language reflection turns in 10,000 partial task contexts, then improved behavior in uninterrupted evaluation contexts with no reflection request or text. Ethics-related J-space contents increased after training; ablating their lens vectors nearly removed the fabrication-honesty gain and partially reversed the deception-benchmark gain.
  - **Source extract (verbatim):** We assemble a set of training contexts by sampling ten thousand task prompts from production RL training environments and generating partial rollouts with the baseline model (Claude Haiku 4.5), truncating each at a randomly selected turn.
  - **Source location:** "Shaping the J-space with Counterfactual Reflection Training," method description
  - **Source extract (verbatim):** We then fine-tune the baseline model on this corpus, computing loss only on the reflection turn. The model is thus trained to produce constitution-grounded reflections spontaneously, conditioned only on the task context and the probe.
  - **Source location:** Same method description
  - **Source extract (verbatim):** Importantly, in our evaluations, we never prompt the model to reflect, and it never produces explicit reflection text.
  - **Source location:** Paragraph preceding "Reflection training improves honesty"
  - **Source extract (verbatim):** Reflection fine-tuning lowers the dishonesty score from 0.25 to 0.07 on the fabrication benchmark (Figure ??, panel A), and lowers the deception score from 0.38 to 0.05 on the deception benchmark (Figure ??, panel A).
  - **Source location:** "Reflection training improves honesty"
  - **Source extract (verbatim):** On the fabrication benchmark (Figure ??, panel C), ablation leaves the base model essentially unchanged (0.25 → 0.25) but raises the reflection-trained model from 0.07 to 0.22, back to base-model level. The behavioral improvement on this benchmark is thus almost entirely carried by the ethical-reflection-related lens vectors that training implants; removing them removes the improvement.
  - **Source location:** "The implanted J-space contents are causally implicated in reflection training’s effects"
  - **Source extract (verbatim):** On the deception benchmark (Figure ??, panel C) the effect is in the same direction but weaker: ablation raises the base model from 0.38 to 0.48 and the reflection-trained model from 0.05 to 0.23, reversing part of the gain.
  - **Source location:** Discussion following Figure 49
  - **Scope:** Claude Haiku 4.5 fine-tuned on the reported 10,000-context corpus and evaluated with LLM-graded fabrication-honesty and deception benchmarks; the causal intervention targets a curated set of J-lens vectors at workspace layers.
  - **Confidence:** High for the training protocol, behavioral score changes, and ablation directions because the source states them directly; the J-space interpretation remains tied to the paper's lens operationalization.
  - **Limitation:** Ablation almost eliminates the gain only on the fabrication benchmark; it reverses part, not all, of the deception gain. The experiment establishes this natural-language-training-to-parameter-and-behavior path for two honesty settings, not a general representational-form coevolution result.

## Connections Found

The source lands in the KB's representational-form, activation, and learning-substrate cluster, not as a general context-engineering source. It directly supports [representational form](../notes/definitions/representational-form.md) by giving a concrete example of a distributed-parametric operative part whose inspection method is probing and intervention. It strengthens [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) because the paper distinguishes concepts being present in J-space from those concepts being causally used by the current task. It supports [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md) and [Treat continual learning as substrate coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md) through counterfactual reflection training: text about possible reflection changes model-internal behavior without directly supervising the target output. It also gives source-to-source comparison with [An Enigma of Artificial Reason](an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md), since both use probes and causal interventions to separate surface behavior from hidden model state.

## Extractable Value

1. **Probeable parametric operative parts** -- The J-space is a worked example for the `distributed-parametric` branch of [representational form](../notes/definitions/representational-form.md): not directly readable like a natural-language artifact or testable like code, but partially inspectable through a trained/derived probe and causal interventions. This is new relative to the KB's mostly coarse "probe parametric artifacts behaviorally" wording. [quick-win]
2. **Presence is not causal activation, even inside the model** -- The language experiments show a concept can appear in J-lens readouts across tasks but affect only report and flexible inference, not automatic continuation or anomaly detection. This is a tighter, model-internal cousin of [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). [deep-dive]
3. **Externalized reasoning can relieve internal-workspace demand** -- GSM8K with explicit chain-of-thought is more robust to J-space ablation than direct answering, which gives a mechanistic explanation for why writing intermediate steps helps: it moves work onto the page so the model does not have to carry it in the internal workspace. This directly informs the KB's externalization and soft-context-bound notes. [experiment]
4. **Counterfactual reflection is cross-form process shaping** -- Training on reflective continuations that are not present at evaluation implants ethical/reflection concepts in the workspace and changes behavior; ablation largely removes the benefit. This is strong evidence for natural-language supervision shaping distributed-parametric behavior through a process channel rather than an output-format channel. [deep-dive]
5. **Probeability is weaker than artifact inspectability** -- The source complicates [Inspectable artifact, not supervision, defeats the blackbox problem](../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) without overturning it: a probe can make part of a parametric system legible, but it does not provide stable discrete commitments, provenance, diffs, review, or rollback. [quick-win]
6. **Alignment auditing gains a cheap hidden-state signal, not a complete monitor** -- J-lens readouts surface evaluation awareness, prompt-injection recognition, strategic deliberation, and hidden misaligned dispositions in examples, but the paper explicitly warns that automatic or reinforced circuits, multi-token concepts, and non-J-space mechanisms may evade it. [just-a-reference]

## Limitations (our opinion)

The paper should not be imported as "LLM context engineering." It studies and modifies model-internal representations; [context engineering](../notes/definitions/context-engineering.md) is the architecture around what enters a bounded call, and explicitly excludes model training or architecture changes. The Jacobian lens is also a partial instrument: it is token-indexed, weak on multi-token or non-verbal concepts, and tied to a post-hoc workspace-layer boundary. The alignment-auditing results are promising but not sufficient for safety monitoring, and the counterfactual reflection result is narrow until replicated across goals, models, and possible side effects. Finally, the experiments are Anthropic-internal and partly on closed production models, so the KB should treat the results as high-value evidence with replication limits, not as a general law of all transformers.

## Recommended Next Action

Write a note titled `Externalized reasoning trades internal workspace demand for context budget` in `kb/notes/`, connecting this source with [Agent context is constrained by soft degradation, not hard token limits](../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), [LLM-mediated schedulers are a degraded variant of the clean model](../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), and [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md).
