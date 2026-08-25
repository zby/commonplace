---
description: "DFA-MoE separates forgetting acquired classes from eroding a model's pre-trained zero-shot baseline, but the captured repository exposes design and workflow rather than paper outcomes"
source: https://github.com/RL-MIND/DFA-MoE
captured: "2026-08-21"
capture: web-fetch
genre: code-repository
snapshot_sha256: 39f1f8196272e57cb04978d0cc89b185b7b8a4e99b24013afc36fbb0350abc71
ingested: "2026-08-21"
type: kb/sources/types/ingest-report.md
domains: [continual-learning, vision-language-models, model-editing, evaluation]
---

# Ingest: DFA-MoE: Tackling Dual Forgetting in Vision-Language Continual Learning

## Classification

The captured README documents an official PyTorch implementation, its declared method, supported datasets, configuration, and evaluation workflow rather than presenting the unavailable paper itself.
Author: RL-MIND publishes the repository for the ICML 2026 paper by Borui Kang, Jinrui Gu, Tao Feng, Qi Fan, Yinghuan Shi, Lei Wang, Wenbin Li, and Yang Gao. The authors have direct implementation access, but this ingest inspected only the captured README and did not verify the implementation or reported research outcomes.

## Summary

The repository frames vision-language continual learning as two retention problems: Incremental Knowledge Forgetting harms classes learned during the task sequence, while Pre-trained Knowledge Forgetting erodes the original model's zero-shot capability. Its README declares three corresponding contributions: the DFA-CIL evaluation protocol, a Similarity-Calibrated Retention metric intended to separate foundational retention from positive transfer, and DFA-MoE, which places task-agnostic alignment preservation and task-specific adaptation in separate expert pathways joined by hierarchical routers. It also provides Hydra configuration examples and a three-step evaluation workflow that records the original CLIP zero-shot baseline, generates a frozen-CLIP task-to-upstream similarity matrix, and computes SCR. The README contains no quantitative result table, and the accompanying paper was not available for this ingest.

## Quotes

No source quotes have been retained yet.

## Connections Found

The closest source comparison is [HCL](harness-continual-learning-adaptation-beyond-model-parameters.ingest.md): HCL protects sampled behavior acquired earlier in a harness-update history, while DFA-MoE separately names forgetting of incremental history and forgetting of capabilities inherited from pre-training. That distinction sharpens [continual learning as governance of behaviour-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md), whose current regression requirement does not separate those baselines. [Harness-IF](harness-if-instruction-following-across-instruction-surfaces.ingest.md) supplies a measurement analogue rather than the same mechanism: its withheld-rule control and DFA-MoE's claimed similarity calibration both try to keep pre-existing capability or transfer from inflating the quantity attributed to an intervention. Interpretation rests on [the fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), because the repository exposes learning inside a supplied two-pathway architecture and evaluation protocol, not evidence that those fixed choices are necessary or preferable.

## Extractable Value

1. **Retention may need two temporal baselines** -- prior-task checks ask whether an update preserves capabilities acquired during the adaptation history; a pre-adaptation baseline asks whether the same history damages capabilities inherited before it began. HCL already supplies the first case for readable harness state, while this repository makes the second explicit for parametric VLM adaptation. Treating the split as substrate-general remains a hypothesis. [quick-win]
2. **Raw zero-shot performance can confound retention with positive transfer** -- the README's motivation for SCR is that similarity between downstream and upstream tasks can make a post-update zero-shot score look preserved even when the original capability changed. This gives evaluation design a sharper target than merely replaying an upstream benchmark, although the absent formula and results prevent assessment of whether SCR succeeds. [experiment]
3. **A foundational-retention metric requires a before-update observation** -- the supplied workflow refuses to compute SCR without a `task: -1` row containing the original zero-shot result, per-task post-update zero-shot results, and a similarity matrix produced by a frozen CLIP model. The operational lesson is that inherited capability must be measured before the learning history begins; it cannot be reconstructed reliably from later scores alone. [quick-win]
4. **Stability and plasticity are assigned different mechanisms** -- DFA-MoE declares a task-agnostic contrastive alignment expert for pre-trained-knowledge retention, task-specific experts for incremental learning, an inner task-expert router, and an outer alignment-versus-plasticity router. This is a concrete architecture for making the tradeoff addressable, but the README supplies no ablation or outcome evidence that functional separation causes better retention. [experiment]
5. **The effective update space is narrower than the dual-forgetting framing** -- behavior can condition on class-incremental data, task identity, the model's pre-task and per-task zero-shot measurements, and a frozen-model similarity matrix; it can compose updates to alignment and task-specific PEFT experts and their hierarchical routers. The CLIP backbone, two-pathway partition, task boundaries, dataset pool, prompt template, expert counts, routing topology, similarity construction, and SCR protocol remain fixed. Improvement inside that space would test the compound configuration, not validate the decomposition as a whole. [deep-dive]

## Limitations (our opinion)

This is a point-in-time repository README, not the paper or a code-grounded reproduction. It states the method and provides entry points, but it reports no quantitative outcomes, uncertainty, baselines, or ablations. The implementation was not statically inspected, no command was executed, and the advertised datasets were still described as forthcoming. The capture also follows the mutable `main` branch rather than an immutable commit, so later repository changes may overturn details preserved here.

The central measurement claim cannot be evaluated from the snapshot. The README says SCR uses similarity weights to disentangle foundational retention from positive transfer, but it omits the full definition, assumptions, and empirical comparison. A simpler account for any eventual gain could be added expert capacity, a protected alignment path, or task routing rather than the dual-forgetting analysis specifically. Only matched ablations and results from the paper or an independently executed implementation could distinguish those accounts.

The fixed decomposition also limits transfer. The learner operates over two supplied functional pathways and hierarchical routing around a named CLIP configuration; it cannot revise that partition, the available evidence, or the evaluation protocol. More importantly for this KB, “pre-trained foundation” has no automatic harness analogue. A deployed agent inherits model priors, seed prompts, tools, safety policies, and platform behavior from different authorities. Extending DFA-MoE's two baselines to readable artifacts requires declaring which inherited behavior is normative and which is merely incumbent, then testing whether separate checks discriminate regressions across those forms.

## Recommended Next Action

Write a hypothesis note titled **“Continual adaptation needs separate inherited-capability and acquired-history retention checks”**, grounded in this repository and [HCL](harness-continual-learning-adaptation-beyond-model-parameters.ingest.md), with an explicit cross-form transfer test and the caveat that the DFA-MoE paper outcomes remain unavailable.
