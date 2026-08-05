---
description: "The spec's valid set, the interpreter's output distribution, and the sampling process are three different objects, so prompt narrowing, error correction, and sampling control each repair one failure and leave the others untouched"
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [llm-reliability, computational-model]
---

# LLM output deviation has three sources with non-substitutable remedies

When an LLM's output is not what the user wanted, the deviation has one of three causes, and each is a property of a different part of the system. Take three objects: the intended set `I` of outputs the user would accept, the valid set `V` of outputs the specification admits, and the output distribution `D` the interpreter produces from that specification.

- **[Underspecification](./agentic-systems-interpret-underspecified-instructions.md)** — `V` is larger than `I`. The spec admits outputs the user did not want. A property of the specification language; a perfect, deterministic interpreter still faces it.
- **[Interpretation error](./interpretation-errors-are-failures-of-the-interpreter.md)** — `D` puts mass outside `V`. The spec rules the output out and the interpreter produces it anyway. A property of the interpreter.
- **[Indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md)** — `D` is not concentrated on a point, so repeated draws differ. A property of the sampling process.

The three claims are about three different objects, which is why the taxonomy is not a list of observed symptoms but a decomposition of the pipeline. Any system that runs `specification → interpreter → sampled execution` has these three loci, whether the interpreter is an LLM, a contractor working from a brief, or a compiler for a language with implementation-defined behavior. The symptom — "the output is wrong" — is identical across all three; the locus is not.

## Why the remedies do not substitute

Each standard remedy acts on exactly one of the three objects, so it cannot repair a failure located in another.

**Narrowing the spec** — more explicit instructions, schemas, few-shot examples, [constraining](./definitions/constraining.md) part of the task to code — shrinks `V` toward `I`. It does not move mass from outside `V` to inside it, and it does not concentrate `D`. Worse, the text added to shrink `V` enlarges the context the interpreter must honour, which can *increase* out-of-`V` mass: the classic case of fixing an interpreter failure by writing a longer prompt and getting more constraint violations, not fewer.

**Error detection and correction** — validation, [oracles](./oracle-strength-spectrum.md), voting, guardrails, architectural separation — moves the realized output back inside `V`. It says nothing about whether `V` is close to `I`. An oracle can only reject a valid-but-unwanted output if the oracle itself encodes the missing intent, and at that point the spec narrowing has happened in the checker rather than the prompt; the work was not avoided, only relocated.

**Sampling control** — temperature, deterministic decoding, best-of-N — concentrates `D`. It neither shrinks `V` nor moves mass inside it. At temperature 0 the interpreter still picks one point from a plural `V`, and a deterministic interpreter still makes interpretation errors; you get the same wrong output every time instead of a different one each run.

So misdiagnosis is expensive in a specific way: the wrong remedy does not merely fail, it consumes the budget (context, latency, review attention) that the right remedy needs. Rewriting a prompt against an interpreter failure spends context to no effect; lowering temperature against underspecification removes the variation that was the only visible evidence that `V` was too wide.

## Distinguishing them

The three have different empirical signatures, and each signature holds one of the three objects fixed while varying another.

- Hold the prompt fixed and resample: variation across runs is indeterminism. Consistent failure is not.
- Hold the task fixed and vary framing that does not change meaning — emotional register, persona, ordering of candidates: systematic performance change is interpreter bias, since `V` did not move.
- Read the spec against the bad output: if a competent reader given only that spec would accept the output, `V` admits it and the failure is underspecification, not interpreter failure.

[Ma et al.'s prompt stability study](https://arxiv.org/pdf/2509.13680) runs all three separations in one design: temperature and sampling measure indeterminism within a prompt variant, cross-variant comparison measures underspecification, and systematic degradation under emotionally framed but functionally identical prompts reveals bias. Their finding that performance and stability are decoupled (Spearman rho = -0.433) is the direct evidence that these are not one phenomenon measured three ways — a model can be accurate and unstable, or stable and wrong.

## Scope

The three loci are distinct objects, but they are not independent knobs. Indeterminism is the mechanism that makes a plural `V` visible, since a deterministic interpreter would silently pick one interpretation forever. Lowering temperature concentrates `D` and can therefore change *which* interpretation is realized, not just how often it varies. The taxonomy classifies causes; it does not promise that a given control touches only one of them.

Attribution between underspecification and interpreter failure depends on how the spec is read, and for genuinely borderline cases the assignment is contestable. The competent-reader test above operationalizes it well enough for triage but is not a decision procedure.

The decomposition assumes `I` exists and is known to the user. When the intent is itself unformed — the user cannot say what would count as acceptable — the failure sits upstream of all three, and no remedy in this taxonomy applies.

## Open Questions

- Can the three contributions be measured per-deployment rather than merely separated in a controlled study? Ma et al. show the separation is possible in principle; a per-system decomposition would let a team see which remedy has the best return before spending on it.
- Interpreter failure rates are model properties that improve with model generation, while underspecification is a property of the specification language and does not. Whether the practical mix shifts toward underspecification as models improve is testable but untested here.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: the source framing for underspecification, and for the projection model that makes `V` an object rather than a metaphor
- [interpretation errors are failures of the interpreter](./interpretation-errors-are-failures-of-the-interpreter.md) — grounds: the third source, with the worked catalogue of out-of-`V` failures
- [execution indeterminism is a property of the sampling process](./execution-indeterminism-is-a-property-of-the-sampling-process.md) — grounds: the sampling-process source and why it obscures the other two
- [llm-debugging-starts-with-retry-versus-rewrite-triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) — extends: turns the diagnostic signatures into a first debugging move, for the two-source case
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: when the error-correction remedy actually works, and what it costs
- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: the architectural form of the error-correction remedy, moving out-of-`V`-prone work to a substrate with hard oracles
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — contrasts: hidden recovery after an ambiguous spec, which looks like interpreter failure but is located in `V`
- [Ma et al. (Sep 2025) — Prompt Stability in Code LLMs](https://arxiv.org/pdf/2509.13680) — evidenced-by: separates all three sources methodologically; the performance-stability decoupling is the evidence they are not one phenomenon
