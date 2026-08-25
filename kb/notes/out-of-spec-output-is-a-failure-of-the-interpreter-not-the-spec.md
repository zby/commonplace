---
description: Interpreter failure is output that a spec's public meaning rules out; the fault attaches to the interpreter's role, so repair uses detection and correction rather than narrowing an already sufficient spec
type: kb/types/note.md
traits: [title-as-claim]
tags: [llm-reliability]
---

# Out-of-spec output is a failure of the interpreter, not the spec

Real LLMs produce outputs outside the space of valid interpretations. The spec rules them out, but the LLM fails to comply. This is not [underspecification](./agentic-systems-interpret-underspecified-instructions.md) (where multiple outputs are valid) and not [indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md) (sampling noise across runs). It is **interpreter failure**: the gap between what a conforming interpreter of the spec's public meaning would do and what a real LLM does.

Calling it a *failure* is a claim about a role, not about the computation. The forward pass computes its own function flawlessly, the way a buggy compiler binary executes its own instructions flawlessly; the fault is non-conformance to what the spec's words publicly mean — the same norm a compiler is held to by a language standard. Classical stacks can bracket that norm because compilers honor it reliably; [LLM systems cannot](./traditional-software-can-bracket-executor-conformance-llm-systems.md). And the norm is the spec's public meaning under a competent reading, never the author's private intent: an unwanted output the words admit is underspecification, the author's problem — not this phenomenon.

Examples:
- **Constraint violation**: "Output JSON only" → LLM produces markdown with a JSON block
- **Hallucination**: "Summarise this document" → LLM includes facts not in the document
- **Bookkeeping failure**: on ConvexBench's mechanically verifiable convexity-classification task, [reported performance falls from F1=1.0 at depth 2 to approximately 0.2 at depth 100](../sources/convexbench-can-llms-recognize-convex-functions.ingest.md)
- **Content bias**: reasoning accuracy varies with semantic content rather than logical structure, producing errors on valid syllogisms with unfamiliar premises
- **Emotional prompt sensitivity**: [Ma et al.](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) hold functional specifications fixed across semantically equivalent variants under a uniform 16-sample decoding policy. Under valence×arousal conditions, they report that emotional prompting mildly reshapes correctness and calibration for some models, with effects varying by model and family.

In each case, a conforming interpreter given the same spec would not make the error. The spec is sufficient; the interpreter is not.

Not every measured sensitivity establishes interpreter failure. In the pinned [Mazur position-bias benchmark](../sources/position-bias.ingest.md), the median of 27 judge models changed its canonical winner in 44.8% of decisive swapped-order sibling-edit pairs. The retained source material establishes order sensitivity, but not a judging contract or public-meaning norm that makes one canonical winner the only valid interpretation. Without that premise, the result could reflect underspecification, sampling variation, or non-conformance; it cannot by itself distinguish them.

## Why this matters as a distinct claim

The [idealised two-phenomena model](./agentic-systems-interpret-underspecified-instructions.md) implicitly assumes a conforming interpreter — one that always lands within the valid interpretation space. This is a useful simplification for reasoning about system design, but it leaves out a prominent practical failure mode: the LLM just getting it wrong. The examples above establish existence and variety, not a comparative prevalence rate.

The remedy is fundamentally different from the other two phenomena. Narrowing the spec (underspecification remedy) can make things worse by overloading context. Sampling control (indeterminism remedy) is irrelevant — a deterministic LLM still fails as an interpreter. The correct remedies are **error detection and correction**: validation, [oracles](./oracle-strength-spectrum.md), [voting](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md), guardrails, and [architectural separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) that moves error-prone operations to reliable substrates.

This is also one phenomenon that makes [discrimination](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — knowing per-instance whether the output is wrong — the binding constraint on automation. If LLMs were conforming interpreters, the only question would be which valid interpretation they chose. Because they're not, you also need to detect when they've left the valid space entirely.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the idealised two-phenomena model this note extends; covers underspecification and indeterminism in depth
- [execution indeterminism is a property of the sampling process](./execution-indeterminism-is-a-property-of-the-sampling-process.md) — sibling: the second phenomenon, a property of the execution engine
- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — synthesis: the three-question diagnosis this note is part of, and why error detection and correction is the primary repair surface for out-of-spec output
- [LLM reliability](./llm-reliability-README.md) — parent area: deviation sources plus the verification and correction machinery
- [traditional software can bracket executor conformance; LLM systems cannot](./traditional-software-can-bracket-executor-conformance-llm-systems.md) — grounds: why the failure attribution is legitimate — the interpreter is held to a role norm, like a compiler to a language standard, and for LLMs that norm cannot be bracketed
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — remedy: the general theory of error correction applicable to interpreter failures
- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — architectural remedy: moving error-prone bookkeeping to a reliable substrate
- [Ma et al. (Sep 2025) — Prompt Stability in Code LLMs](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — evidenced-by: under fixed requirements and uniform repeated sampling, emotional prompting mildly reshapes correctness and calibration for some models, with effects varying by model and family
- [Mazur position-bias benchmark](../sources/position-bias.ingest.md) — contrasts: establishes bounded order sensitivity, but lacks the judging-contract premise needed to classify every flip as interpreter failure rather than underspecification or sampling variation
