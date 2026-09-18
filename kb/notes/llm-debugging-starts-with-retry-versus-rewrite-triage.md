---
description: "Choose a debugging move by checking intent against the specification, output against the specification, and variation across repeated runs; failure frequency alone cannot identify the defect"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, llm-reliability]
---

# LLM debugging separates specification gaps, instruction violations, and run-to-run variation

Failure frequency alone cannot tell a debugger whether to rewrite a prompt or correct the model's behavior. [LLM output deviation requires three-way diagnosis because remedies target different relations](./llm-output-deviation-requires-three-way-diagnosis.md) distinguishes underspecification, interpreter failure, and indeterminism. In debugging, these become three checks that supply different evidence for choosing a repair.

## Three checks guide the next move

1. **Compare the specification with the intended result.** Does the specification permit the unwanted answer? If it does, the gap is underspecification: following the instructions is insufficient to produce what the user wants. Adding the missing requirement addresses that gap. For example, “give me a short list” permits three items even if the user wanted exactly two.
2. **Compare the actual output with the specification.** Does the answer violate a requirement already present? If it does, the observed defect is interpreter failure. “Return exactly two items” followed by three items is such a violation, whether it happens once or on every run. The next move needs to improve or enforce conformance: for this example, a count check can detect the defect and trigger correction. A prompt edit can also improve conformance, but its success would not show that the original instruction was ambiguous.
3. **Compare repeated runs under fixed conditions.** With the assembled input, model, sampling settings, and relevant tool state held fixed, do outcomes vary, and does that variation cross the acceptance boundary? This estimates run-to-run variation and whether retrying can recover an acceptable answer. It does not establish whether the bad answers were permitted by the specification.

These checks need not produce one exclusive diagnosis. A specification can admit an unwanted answer while some outputs also violate it; variation can determine which failure appears on a given run. The checks prevent a remedy from being chosen solely from the failure's frequency.

## What a retry establishes

A successful retry demonstrates recovery on that attempt. It does not establish that the specification captures the intent or that later outputs will obey it. Using retries operationally also requires a way to recognize an acceptable result; generating another answer supplies no such check by itself.

Both misleading frequency patterns have simple counterexamples. A model can consistently return three items despite an explicit two-item requirement. Conversely, an ambiguous request for a short list can sometimes produce the intended two items and sometimes an unwanted three. Consistency therefore does not establish underspecification, and intermittence does not establish that the specification is adequate.

Lowering temperature is likewise an intervention to evaluate, not a diagnosis. It may suppress a bad outcome or concentrate on it. Assess the resulting outputs against both the specification and the intent, rather than treating reduced variation as correctness.

## Where to inspect

The nearest [LLM↔code boundary](./llm-code-boundaries-are-natural-checkpoints.md) exposes arguments and results for inspection. Check the argument against the request and the code's handling against its contract. An upstream mistake and a code defect can coexist. Capturing a concrete argument helps localize the failure; it does not decide which of the three checks explains the upstream mistake.

## Scope

The checks assume the intended result can be stated and the effective input is available. Wrong retrieval, stale memory, or changing tool results require inspection of input assembly before attributing variation to model sampling. A finite set of identical outputs does not establish determinism. When competent readers disagree about whether the specification permits an answer, the underspecification-versus-violation judgment remains unresolved.

---

Relevant Notes:

- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — grounds: distinguishes the three relations and explains repair versus masking
- [LLM↔code boundaries are natural checkpoints](./llm-code-boundaries-are-natural-checkpoints.md) — enables: concrete arguments and results supply evidence for localizing failures
