---
description: "Batch-invariant kernels remove reported temperature-zero output variation, qualifying sampling-only accounts of LLM indeterminism without establishing semantic correctness."
source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
captured: "2026-11-02"
capture: html-article-extraction
capture_scope: full-source
doi: "10.64434/tml.20250910"
genre: practitioner-report
snapshot_sha256: 95e29665ab558db1bc0159a0781cc0bddae396416d7e5b8d43755ff93a52cfa2
ingested: "2026-11-02"
occasion: "Is indeterminism incidental to LLM operation, and what should that change in how we discuss LLM-based systems?"
type: types/ingest-report.md
domains: [batch-invariant-inference, floating-point-reductions, numerical-reproducibility, on-policy-RL]
learning_claims: true
---

# Ingest: Defeating Nondeterminism in LLM Inference

## Classification

A practitioner research report explaining a numerical failure mechanism, an implementation intervention, and completion, performance, and reinforcement-learning experiments. Author: Horace He and Thinking Machines Lab, reporting their own kernel and serving work with implementation links and concrete comparisons. The report is first-party engineering evidence, not an independent reproduction.

## Summary

The article explains how deterministic GPU kernels can produce user-visible LLM nondeterminism: varying server load changes batch sizes, which changes floating-point reduction order and hence numerical outputs. Determinism for identical complete kernel inputs is weaker than invariance of one request across batches. The proposed repair fixes reduction order in RMSNorm, matrix multiplication, and attention, including attention's sequence partitioning and cache boundaries. In a vLLM-based intervention holding the model, prompt, and greedy decoding fixed, the authors report that 1,000 Qwen3-235B-A22B-Instruct-2507 completions yielded 80 distinct outputs before enabling batch-invariant kernels and one afterward. A separate single-GPU Qwen-3-8B workload took 26 seconds with default vLLM, 55 with the unoptimized deterministic implementation, and 42 with improved attention. These are implementation-specific comparisons, not a general cost of determinism. A further RL experiment reports stable training when sampler and trainer numerics match, or when importance weighting corrects their mismatch. Together, the explanation and intervention show a removable source of variation in the tested stack, not invariance across arbitrary hardware, software, or agent environments.

## Quotes

> However, when a non-batch-invariant kernel is used as part of a larger inference system, the system can become nondeterministic. When you make a query to an inference endpoint, the amount of load the server is under is effectively “nondeterministic” from the user’s perspective. The load determines the batch size that the kernels are run under, and thus changes the eventual result of each individual request!
> --- `kb/sources/.snapshots/defeating-nondeterminism-in-llm-inference.md` @ `sha256:95e29665ab558db1bc0159a0781cc0bddae396416d7e5b8d43755ff93a52cfa2` — Batch invariance and determinism

> The requirement for batch invariance is that the <b>reduction order for each element must be fixed regardless of the batch-size of the kernel.</b>
> --- `kb/sources/.snapshots/defeating-nondeterminism-in-llm-inference.md` @ `sha256:95e29665ab558db1bc0159a0781cc0bddae396416d7e5b8d43755ff93a52cfa2` — Batch-invariant RMSNorm

> We use <code>Qwen/Qwen3-235B-A22B-Instruct-2507</code> and sample 1000 completions at temperature 0 with the prompt “Tell me about Richard Feynman” (non-thinking mode), generating 1000 tokens each. Surprisingly, we generate <em>80</em> unique completions, with the most common of these occuring 78 times.
> --- `kb/sources/.snapshots/defeating-nondeterminism-in-llm-inference.md` @ `sha256:95e29665ab558db1bc0159a0781cc0bddae396416d7e5b8d43755ff93a52cfa2` — Completion experiment, baseline

> On the other hand, when we enable our batch-invariant kernels, all of our 1000 completions are identical. This is what we would mathematically expect from our sampler, but we aren’t able to achieve deterministic results without our batch-invariant kernels.
> --- `kb/sources/.snapshots/defeating-nondeterminism-in-llm-inference.md` @ `sha256:95e29665ab558db1bc0159a0781cc0bddae396416d7e5b8d43755ff93a52cfa2` — Completion experiment, intervention

## Connections Found

The source is qualifying evidence for [Execution indeterminism is a property of the sampling process](../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md). That note acknowledges batching effects but also says temperature zero eliminates variation and that all deployed systems exhibit indeterminism. The article supplies a concrete mechanism and a reported intervention against those unconditional formulations: with prompt, model, and greedy decoding fixed, changing the numerical implementation removed variation in the tested completion trial. It supports treating this variation as an engineering property rather than a necessary feature of LLM computation, while showing why sampling control alone is insufficient. It does not test the note's account of underspecification or establish that a repeatable answer is the intended answer.

## Learning Claims (our opinion)

The learning experiment concerns reinforcement learning with verifiable rewards on Bigmath, initialized from Qwen 2.5-VL instruct 8B with a maximum rollout length of 4096. The source reports collapse without importance weighting under mismatched sampler–trainer numerics, smooth training with that correction, and smooth training with zero reported sampler–trainer KL divergence after numerical alignment. The intervention changes numerical agreement and correction, not the task, reward scheme, or model family. It supports a learning-infrastructure claim: discrepancies hidden by the nominal identity of the policy can affect training stability. It does not establish that numerical alignment generally outperforms corrected off-policy learning.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), applied to the RL learner rather than the researchers, the four conditions have different support. **Localized content:** no retained, stated theory revised by the learner is shown; adaptation is in policy weights. **Consumption:** the policy guides rollouts, but consumption of retained theories through what they say is not demonstrated. **Criticism:** reward and numerical divergence supply evaluation signals, not demonstrated stated criticism of an identified theory's content. **Iteration:** updates do affect later rounds within the training run, but this is parameter-update iteration rather than established retention of such criticism. The report does not demonstrate reuse across runs or problems. Stable training is evidence of avoiding one failure, not by itself a held-out demonstration of improved capacity for future action. As in [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within the supplied policy and reward setup does not compare alternative task representations or feedback schemes.

## Extractable Value

1. **Separate probabilistic modeling from necessary output variation.** The reported greedy-decoding intervention removes variation in one tested stack without replacing the LLM. This challenges claims that LLM-based systems must be nondeterministic by nature. Distinguish chosen stochastic sampling, removable numerical sensitivity, and uncontrolled system inputs; do not turn the demonstration into a universal guarantee. [quick-win]
2. **State the boundary of a repeatability claim.** A fixed prompt and sampler do not fix the numerical computation when batch sizes or sequence partitions vary. Descriptions of reproducible agent experiments should identify which serving conditions are controlled or invariant, rather than equating temperature zero with repeatability. This is a transfer from the source's serving mechanism, not a tested agent-workflow result. [quick-win]
3. **Treat numerical alignment as a substantive training condition.** The Bigmath comparison makes sampler–trainer mismatch worth measuring rather than dismissing as harmless noise. Its value here is a bounded counterexample to that dismissal, not a prescription to add RL infrastructure to Commonplace. [just-a-reference]

## Limitations (our opinion)

The completion evidence uses one prompt and one model configuration. One thousand identical outputs after intervention support the proposed mechanism in that setup; they do not prove universal endpoint determinism. The article itself distinguishes run-to-run determinism from hardware/software-version invariance and excludes parallelism-related reductions from its detailed treatment. Attention's fixed-size splitting also required internal FlexAttention changes absent from the described release. No implementation was inspected or executed for this ingest.

The performance comparison bundles kernel choices with a less-optimized FlexAttention integration. It cannot isolate an unavoidable overhead of batch invariance. The RL comparison reports a particular training failure and two remedies but supplies no broad model/task coverage or repeated-run uncertainty estimates. The retained article includes chart captions and external data references, not the underlying plotted data, limiting numerical reassessment of those curves.

Most importantly for KB methodology, bitwise repeatability does not establish instruction compliance, truth, or adequate specification. Nor does stabilizing inference stabilize tools, retrieval, mutable context, scheduling, or other inputs of an entire agent system. The source warrants replacing essentialist language about LLM randomness with scoped causal claims, not dropping verification because an execution can be repeated.

## Recommended Next Action

Revise [Execution indeterminism is a property of the sampling process](../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) to distinguish stochastic sampling from batch-dependent numerical variation and make temperature-zero repeatability conditional on the serving implementation, while preserving the distinction between repeatability and adequate specification.
