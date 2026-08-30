---
description: "When no complete fixed oracle decides whether a claim belongs in a working theory, distributed consequences of live system use can provide an initial selection environment"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, evaluation]
---

# System use is an initial selection environment when theory fit lacks a fixed oracle

A working theory may contain claims that are individually warranted yet still fit poorly together or fail to help the system reason, modify, or recover. [A claim's warrant does not determine its fit in a working theory](./a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md). When no complete fixed oracle decides that fit, using the theory in the live system supplies an initial selection environment: claims and formulations can earn provisional standing by changing consequential work and surviving the distributed consequences of that use.

For a narrow transformation, a test suite may give a compact acceptance criterion. Open-ended project theory is different. No current automatic evaluator fully decides whether a candidate claim belongs in the larger causal picture, which neighboring claims it should displace, whether its abstraction is useful, or whether it will still guide coherent modification when later demands expose consequences that were not locally visible.

This does not make theory fit untestable. It changes the shape of the test. Fit is exposed through a portfolio of consequences spread across operation and time, including whether a claim:

- changes proposal, diagnosis, branch allocation, or recovery rather than merely being cited;
- yields expectations that survive later evidence;
- helps modifications preserve relevant organization across subsequent demands;
- helps distinguish a bad candidate from a bad underlying theory;
- reduces search, repair, or intervention relative to rival formulations; and
- transfers when the task changes while the structure named by the theory remains relevant.

No one item is a complete oracle. Together they can discriminate among rival theory states more strongly than static coherence alone.

## Why live use can select

The system under construction is where many consequences of theory fit become observable. A claim about architecture may change where an agent searches for a defect. A decomposition may change which artifact is revised. A theory of failure may change whether a process retries, backtracks, or revises its own assumptions. Later work can then expose whether those choices made recovery cheaper, preserved structure, or failed in a predictable way.

The important property is counterfactual effect. A claim that is repeatedly retrieved but never changes work has little evidence of operative fit. A claim whose withholding, replacement, or perturbation changes search or recovery has stronger mediation evidence. A claim whose use survives later demands and beats a rival formulation has stronger selection evidence still.

The live system is therefore an **initial** selection environment, not a final authority. It supplies consequences against which theory can compete before a complete global evaluator exists.

## Initial selection is vulnerable to self-confirmation

A system can reward its own misconceptions. Earlier design choices may already assume a claim, neighboring artifacts may encode the same error, or the current workload may never reach the claim's bad scope. Successful use can then make a mistaken claim appear indispensable.

For that reason, [system use provides evidence of theory fit and causal usefulness, not independent warrant](./system-use-provides-evidence-of-theory-fit-not-independent-warrant.md). Rival formulations, withholding or perturbation, held-out demands, transfer, delayed outcomes, and independent factual or formal checks are ways to make the selection environment less self-sealing.

The same limitation applies to blame assignment. A failed modification may reflect a false theory, a misapplied theory, a missing premise, a bad implementation, or a weak evaluator. System use exposes the failure but does not identify its cause automatically. The theory-mediated path must retain enough structure for later read-back to assign credit or blame at the granularity the evidence supports.

## Why "initial" matters

This claim does not reserve global fit for permanent human judgment. The present selection environment may be partly human-inclusive because people supply high-level criticism, comparison, and authorization where reusable evaluators are weak. Recurring judgments can later become retained methods, search controls, critics, validators, tests, or other machinery when their scope and discrimination become strong enough.

Nor does the claim say that explicit theory-guided selection is the only route. A learned evaluator, end-to-end search process, or future weight-updating system may eventually provide a better selection environment. The live-system route is useful while global evaluation is incomplete because it converts ongoing construction and operation into evidence that can improve the theory and, potentially, the machinery that evaluates it.

## Scope

- The claim concerns **theory fit**, not independent warrant. The distinction is developed in the linked notes above.
- "Initial" means a starting environment under incomplete evaluation, not a permanent architecture or a promise that human holistic judgment remains necessary.
- No single scalar is assumed to capture theory fit. A portfolio of causal, predictive, operational, and transfer evidence may support selection.
- The current absence of a complete fixed oracle is a statement about this research setting, not a proof that no general evaluator can exist.
- Objectives, commitments, and grants of authority may remain externally supplied even when empirical and procedural theory selection becomes increasingly computational.

## Open Questions

- Which aspects of theory fit can be operationalized without encoding the incumbent theory as the evaluator?
- Which delayed consequences discriminate among rival theories strongly enough to guide selection rather than merely report viability?
- How should fit evidence from the system be combined when different signals disagree?
- When does a learned or formal evaluator outperform live-system selection at comparable total cost?

---

Relevant Notes:

- [A claim's warrant does not determine its fit in a working theory](./a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md) — grounds: separates independent warrant from relational fit
- [System use provides evidence of theory fit and causal usefulness, not independent warrant](./system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) — extends: bounds the evidential meaning of successful system use
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — grounds: identifies the longitudinal consequences through which program-theory fit can become visible
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — grounds: bounds what one successful configuration can establish beyond its originating context
- [Weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — mechanism: explains why qualities with weak operative signals can disappear under selection despite sounding important
