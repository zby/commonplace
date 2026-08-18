---
description: "For a fixed assembled input, whether V exceeds I, whether D escapes V, and how D's spread affects realization are three diagnostic questions with different primary repair surfaces"
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [llm-reliability, computational-model]
---

# LLM output deviation requires three-way diagnosis because remedies target different relations

When an LLM's output is not what the user wanted, diagnosis must answer three distinct questions. Represent the problem with the intended set `I` of outputs the user would accept, the valid set `V` of outputs the specification admits, and the output distribution `D` the interpreter produces from that specification.

- **[Underspecification](./agentic-systems-interpret-underspecified-instructions.md)** — Does `V` extend beyond `I`? The specification admits outputs the user did not want. A perfect, deterministic interpreter still faces this mismatch.
- **[Interpreter failure](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md)** — Does `D` put mass outside `V`? The specification rules an output out, but the interpreter can produce it anyway.
- **[Indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md)** — How dispersed is `D`? Repeated draws can differ, and that spread contributes to user-visible failure when it crosses the boundaries of `I` or `V`.

Several questions can matter in the same run. A plural `V` can admit unwanted outputs, an imperfect interpreter can place mass outside `V`, and sampling determines which point is realized. The decomposition is for diagnosis, not for exclusive blame assignment. Any system that runs `specification → interpreter → sampled execution` raises the same questions, whether the interpreter is an LLM, a contractor working from a brief, or a compiler for a language with implementation-defined behavior.

The practical consequence is that each repair class has a different primary target. Prompt narrowing, error correction, and sampling control therefore cannot substitute for one another as complete repairs, even when one intervention affects more than one relation.

## Why the remedies do not substitute

Each standard remedy directly changes a different relation in the diagnosis. Cross-effects are common, but they do not guarantee that the intervention repairs the primary defect.

**Narrowing the spec** — more explicit instructions, schemas, few-shot examples, or [constraining](./definitions/constraining.md) part of the task to code (thereby narrowing the space of valid interpretations) — shrinks `V` toward `I`. This directly repairs underspecification, but it does not guarantee that `D` stays inside `V` or becomes concentrated. Prompt changes can also steer the interpreter and reduce out-of-`V` mass. That is a useful cross-effect, but added context can also increase constraint violations by giving the interpreter more text to honour.

**Error detection and correction** — validation, [oracles](./oracle-strength-spectrum.md) (checks that distinguish better from worse outputs), voting, guardrails, or architectural separation — detect or correct outputs relative to `V`. They do not determine whether `V` is close to `I`. A checker can reject a valid-but-unwanted output only if it encodes the missing intent. In that case the operational narrowing has moved into the checker, which may be cheaper or more auditable than putting it in the prompt; the work was relocated, not avoided.

**Sampling control** — temperature adjustment or deterministic decoding — concentrates `D`. It neither defines a narrower `V` nor guarantees that `D` lies inside `V`. Lower temperature can suppress a bad tail, but it can also concentrate on a valid-but-unwanted or out-of-`V` point. `best-of-N` is a mixed strategy rather than pure sampling control when a scorer or chooser provides an oracle or preference.

A remedy aimed at the wrong relation can leave the primary defect intact while still consuming context, latency, or review attention. Rewriting a prompt may fail against interpreter non-conformance, while lowering temperature can hide the run-to-run variation that made a wide `V` visible without narrowing it.

## Distinguishing them

The three questions have different empirical signatures, although none is a complete decision procedure.

- Hold the assembled input fixed and resample: variation that crosses `I` or `V` shows that sampling affects whether failure is realized. Stable failure does not by itself distinguish underspecification from interpreter failure.
- Hold public meaning fixed and vary only surface style or the ordering of equivalent candidates: systematic performance change reflects interpreter sensitivity because `V` did not move.
- Read the spec against the bad output: if a competent reader, given only that spec, would accept the output, `V` admits it and the failure is underspecification, not interpreter failure.

[Ma et al.'s prompt stability study](https://arxiv.org/pdf/2509.13680) separates repeated-sample variation from systematic sensitivity to semantically equivalent framing. It does **not** measure underspecification, because if public meaning is fixed, `V` is fixed too. Its performance–stability decoupling (Spearman rho = -0.433) still shows that accuracy and framing sensitivity are different properties.

[Bertran, Fogliato, and Wu's agentic data-science multiverse experiment](../sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md) illustrates all three questions in one workflow. Repeated runs within a fixed cell expose sampling variation. Materially different auditor-accepted analyses support a plural `V`, conditional on that auditor. Rejected noncompliant runs illustrate mass outside `V`, including pilot runs that hallucinated results or recalled published findings. Persona comparisons are not clean bias estimates when they change the commission or stated prior. Fixed datasets, models, tools, and auditor criteria bound what the workflow can expose; they do not add a fourth relation inside the fixed pipeline.

## Scope

The three diagnostic relations are distinct, but they are not independent knobs. One bad run can have joint attribution: if `D` contains both conforming and non-conforming outputs, interpreter failure explains the out-of-`V` tail while sampling explains why that tail was realized on this run. The taxonomy routes diagnosis; it does not assign each output to exactly one cause or promise that a control touches only one relation.

Repeated sampling is one way to make a plural `V` visible, because a deterministic interpreter can silently choose the same admissible interpretation every time. Reading the specification can reveal the same mismatch without resampling.

Attribution between underspecification and interpreter failure depends on how the spec is read. In genuinely borderline cases, the assignment is contestable. The competent-reader test above operationalizes the distinction well enough for triage, but it is not a decision procedure.

The decomposition begins after the assembled input is fixed. Wrong retrieval, stale memory, or bad tool output change that input upstream rather than adding another relation inside it. It also assumes `I` exists and is known to the user. When intent is itself unformed — the user cannot say what would count as acceptable — no remedy in this taxonomy applies.

## Open Questions

- Can the three contributions be measured per deployment rather than only separated at cohort level? Bertran et al. show that repeated runs, compliance judgments, and decision extraction can expose all three questions in one workflow. They do not assign a cause to each individual deviation, and their AI auditor is not independent ground truth. Per-output diagnosis could help a team estimate which remedy is most worth pursuing before spending on it.
- With the assembled input held fixed, interpreter failure rates are model properties that can improve with model generation, while underspecification belongs to the input and does not. Memory or context assembly can narrow the effective specification by adding information; that changes the input rather than improving its interpreter. Whether the practical mix shifts toward underspecification as models improve is testable but untested here.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: the source framing for underspecification, and for the projection model that makes `V` an object rather than a metaphor
- [out-of-spec output is a failure of the interpreter, not the spec](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — grounds: the third source, with the worked catalogue of out-of-`V` failures
- [traditional software can bracket executor conformance; LLM systems cannot](./traditional-software-can-bracket-executor-conformance-llm-systems.md) — extends: why the analysis needs exactly these three questions — classical practice collapses to one only because executor conformance and singleton meaning can be assumed there
- [execution indeterminism is a property of the sampling process](./execution-indeterminism-is-a-property-of-the-sampling-process.md) — grounds: the sampling-process source and why it obscures the other two
- [llm-debugging-starts-with-retry-versus-rewrite-triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) — extends: turns the diagnostic signatures into a first debugging move, for the two-source case
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: when the error-correction remedy actually works, and what it costs
- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: the architectural form of the error-correction remedy, moving out-of-`V`-prone work to a substrate with hard oracles
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — contrasts: hidden recovery after an ambiguous spec, which looks like interpreter failure but is located in `V`
- [Ma et al. — Prompt Stability in Code LLMs](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — evidenced-by: separates sampling variation from meaning-preserving framing bias; performance-stability decoupling shows those are not one phenomenon
- [context contamination operates below an agent's compliance reasoning](./context-contamination-operates-below-an-agents-compliance-reasoning.md) — evidenced-by: a worked case of non-substitutability — instruction-level narrowing applied to an interpreter-level failure demonstrably fails
