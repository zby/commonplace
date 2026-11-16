---
description: "Consequences of using a claim in a live system show its fit and causal usefulness in the working theory; they add to its independent test record only where the use could have gone against the claim"
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, evaluation, self-improving-systems, theory-builder]
---

# System use provides evidence of theory fit and causal usefulness, not an independent test

Putting a claim to work in a live system creates evidence that static inspection cannot supply. If the claim changes proposal, diagnosis, branch allocation, modification, recovery, transfer, or later operation, and those changes survive consequential use, the result bears on whether the claim fits the working theory and is causally useful there. It does not by itself add to the claim's independent test record, and it does not show that the claim is true.

The distinction follows because [a claim's test record does not determine its fit in a working theory](./a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md). System use primarily exposes fit. A claim that sounds coherent but never changes behavior provides weak evidence of operative fit. A claim that changes search, helps distinguish rival repairs, reduces later repair, or transfers to a new case provides stronger evidence that it participates usefully in the theory's operation.

But a live system can confirm claims it already assumes, including mistaken ones. Earlier implementation choices may already assume the claim; neighboring retained claims may make it appear indispensable; an evaluator may share the same error; or the current task distribution may never expose the claim's bad scope. Successful use can therefore be self-confirming.

Independent factual, formal, source, and scope evidence must remain able to overturn the claim. Depending on the claim, that may include empirical observation, derivation, source review, contradiction tests, preregistered predictions, held-out demands, or transfer outside the cases that shaped the current theory. These checks test the claim at the strength their own evidence licenses. Their strength depends only on their own evidence, not on the system's success.

The useful division is not "system evidence versus real evidence." System-building consequences are real evidence for fit and causal usefulness. They become a test of the claim's truth, validity or scope only through an additional argument showing that the observed consequence could have gone against the claim.

## The evidence can run in both directions

System use gives evidence in both directions. A claim may fit poorly when it repeatedly fails to affect decisions, increases search or repair cost, breaks under later demands, or performs worse than a rival formulation under a controlled comparison. Those outcomes can motivate rescoping or removal even when the claim's independent test record is good.

Conversely, system failure can show that some claim needs a new independent test without identifying which. A failed modification may reveal that the guiding claim was false, that its scope was wrong, that another premise was missing, that the interpreter misapplied it, or that the evaluator accepted the wrong candidate. An interpretation of the outcome must assign the failure at the granularity the evidence supports, not treat every bad outcome as a refutation of the theory.

## Scope

- The claim concerns evidence produced by operating or modifying a system with a working theory. It does not require that the system itself perform the independent tests.
- Causal usefulness is relative to an objective, task distribution, horizon, and comparison. A useful claim under one regime need not fit another.
- An independent test can itself use operational evidence when the claim predicts system behavior. The requirement is that the outcome could have gone against the claim, not separation by data source.
- The note does not define a complete oracle for theory fit. It only separates what system-use evidence shows directly from what requires an independent test.

---

Relevant Notes:

- [A claim's test record does not determine its fit in a working theory](./a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md) — grounds: supplies the distinction between a claim's independent test record and its fit
- [System use is an initial selection environment when theory fit lacks a fixed oracle](./system-use-selects-theory-fit-without-a-fixed-oracle.md) — extends: develops why distributed and delayed live-system consequences can serve as an initial selection environment
