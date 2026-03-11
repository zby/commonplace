---
description: Real LLMs produce outputs that no valid interpretation of the spec allows — violating explicit constraints, hallucinating, failing at fully specified bookkeeping — a property of the interpreter itself, absent from the idealised two-phenomena model
type: note
areas: [llm-interpretation-errors]
status: seedling
---

# Interpretation errors are failures of the interpreter

Real LLMs produce outputs outside the space of valid interpretations. The spec rules them out, but the LLM fails to comply. This is not [underspecification](./agentic-systems-interpret-underspecified-instructions.md) (where multiple outputs are valid) and not [indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md) (sampling noise across runs). It's a property of the interpreter itself: the gap between what a perfect interpreter would do and what a real LLM does.

Examples:
- **Constraint violation**: "Output JSON only" → LLM produces markdown with a JSON block
- **Hallucination**: "Summarise this document" → LLM includes facts not in the document
- **Bookkeeping failure**: tracking compositional depth (fully specified, one correct answer) → [F1 collapses from 1.0 to 0.2](../sources/convexbench-can-llms-recognize-convex-functions.md) at depth 100 despite short context
- **Content bias**: reasoning accuracy varies with semantic content rather than logical structure, producing errors on valid syllogisms with unfamiliar premises
- **Emotional prompt sensitivity**: [Ma et al.](https://arxiv.org/pdf/2509.13680) show that semantically equivalent prompts with different emotional framing produce systematic performance degradation — bias, not noise, since the functional spec is unchanged

In each case, a perfect interpreter given the same spec would not make the error. The spec is sufficient; the interpreter is not.

## Why this matters as a distinct claim

The [idealised two-phenomena model](./agentic-systems-interpret-underspecified-instructions.md) implicitly assumes a perfect interpreter — one that always lands within the valid interpretation space. This is a useful simplification for reasoning about system design, but it leaves out the failure mode that dominates practical experience: the LLM just getting it wrong.

The remedy is fundamentally different from the other two phenomena. Narrowing the spec (underspecification remedy) can make things worse by overloading context. Sampling control (indeterminism remedy) is irrelevant — a deterministic LLM still makes interpretation errors. The correct remedies are **error detection and correction**: validation, [oracles](./oracle-strength-spectrum.md), [voting](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md), guardrails, and [architectural separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) that moves error-prone operations to reliable substrates.

This is also the phenomenon that makes [discrimination](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — knowing per-instance whether the output is wrong — the binding constraint on automation. If LLMs were perfect interpreters, the only question would be which valid interpretation they chose. Because they're not, you also need to detect when they've left the valid space entirely.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the idealised two-phenomena model this note extends; covers underspecification and indeterminism in depth
- [execution indeterminism is a property of the sampling process](./execution-indeterminism-is-a-property-of-the-sampling-process.md) — sibling: the second phenomenon, a property of the execution engine
- [LLM interpretation errors](./llm-interpretation-errors.md) — parent area: the three-phenomena taxonomy this note is part of
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — remedy: the general theory of error correction applicable to interpretation errors
- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — architectural remedy: moving error-prone bookkeeping to a reliable substrate
- [Ma et al. (Sep 2025) — Prompt Stability in Code LLMs](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — evidence: emotional prompt variation produces systematic performance degradation (bias) on functionally identical tasks

Topics:

- [llm-interpretation-errors](./llm-interpretation-errors.md)
