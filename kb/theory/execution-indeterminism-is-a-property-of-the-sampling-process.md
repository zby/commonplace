---
description: "Separates stochastic decoding, batch-dependent numerical variation, and changing system inputs; deterministic inference is possible without resolving intent or correctness."
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [llm-reliability, learning-theory]
---

# LLM output variation depends on decoding and execution conditions

Run-to-run output variation is not necessary to LLM computation. A model can assign probabilities to tokens while a deterministic decoder always selects the highest-scoring token. Whether a deployed request repeats also depends on the numerical computation and the inputs the system holds fixed. A probabilistic model does not by itself require probabilistic execution.

## Three sources of observed variation

**Stochastic decoding.** Sampling chooses among tokens rather than always selecting the highest-scoring one. It deliberately introduces variation. Greedy decoding removes this sampling choice, but it does not fix the scores supplied to the decoder.

**Numerical sensitivity to serving conditions.** Even deterministic kernels can give one request different results when the batch changes. [Thinking Machines' batch-invariant inference report](../sources/defeating-nondeterminism-in-llm-inference.ingest.md) explains how server load changes batch size and how fixing reduction order independently of batch size removes that dependency. The issue is not that a deterministic kernel randomly changes its answer to identical complete inputs; the surrounding system changes a condition that affects its computation.

The authors report 80 distinct completions in 1,000 temperature-zero requests to Qwen3-235B-A22B-Instruct-2507 with the prompt “Tell me about Richard Feynman.” After enabling batch-invariant kernels, all 1,000 completions were identical. This reported intervention supplies a concrete engineering route to repeatability in the tested setup. It does not establish repeatability for every model, prompt, hardware configuration, or serving implementation.

**Changing system inputs or dependencies.** Different retrieval results, tool state, assembled context, model versions, or scheduling-dependent inputs can change an agent's output even when inference itself is deterministic. From the caller's perspective, hidden changes can look like randomness. Making inference repeatable does not hold those other inputs fixed.

These mechanisms call for different controls. Sampling settings control token selection; numerical implementation controls address batch sensitivity; captured inputs and pinned dependencies address changes elsewhere in the system. A fixed prompt and temperature setting alone do not establish that the complete computation is fixed.

## Determinism does not settle meaning or correctness

Grant fully deterministic inference. Under an ordinary natural-language consumption path, the model can still select one of several reasonable interpretations, or consistently violate an explicit instruction. A stable answer is not evidence that the prompt uniquely requires it or that it is correct. [Semantic underspecification and interpreter failure remain separate questions](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md).

Nor must a language reference require only one output. Under the [representational-form definition](./definitions/representational-form.md), a governing reference can specify permitted variation. A system can adopt a frozen model package as that reference for an operation, with decoding included or its distribution specified. Whether the resulting operation satisfies the requirement remains separate from whether execution conforms to its reference.

Indeterminism distracts from these questions when it is treated as the defining difference between LLMs and other computation. Removing it simplifies replay and comparison; it does not establish intended meaning, instruction compliance, or task adequacy. Conversely, permitted variation does not by itself prevent defined semantics.

## Scope

The empirical case concerns one reported completion trial and a particular numerical intervention, not an independently reproduced universal guarantee. Finite identical outputs do not prove determinism. Claims about replay must name the inputs and execution conditions held fixed or made irrelevant by the implementation. Whole-agent repeatability requires accounting for more than inference.

---

Relevant Notes:

- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: repeatability does not settle which interpretation the specification permits or the user intends
- [Out-of-spec output is a failure of the interpreter, not the spec](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — contrasts: a repeated instruction violation remains a violation rather than becoming a specification gap
- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — extends: separates specification gaps, interpreter failure, and run-to-run variation to select repairs
- [LLM reliability](../tags/llm-reliability-README.md) — parent area: deviation sources plus the verification and correction machinery
