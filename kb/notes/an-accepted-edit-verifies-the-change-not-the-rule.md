---
description: "Human acceptance of an edit is a strong oracle for 'this change was wanted here' but a weak oracle for 'this generalizes' — mining rules from accepted edits inherits instance-level verification while the generalization step stays oracle-poor"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, agent-memory]
---

# An accepted edit verifies the change, not the rule

A human-accepted edit is among the strongest oracles a text system can get: someone looked at this change, in this artifact, and kept it. But the acceptance event judged the *instance* — this wording, in this context. It never judged the *rule* a learner might extract from it ("define opaque internal terms inline", "remove stock rhetoric"). Generalization asks which features of the case carry to other cases, and that is a different judgment the acceptance never performed. The oracle is strong at the instance and silent about the rule.

In maturation terms, acceptance sits at the verify rung and rule extraction at the abstraction rung, and the rungs have different oracles — [trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). The asymmetry is why a learning loop can be seeded with excellent evidence and still stall: instance verification is abundant (every accepted edit supplies it), while the generalization step faces the same oracle gap that makes [automating KB learning an open problem](./automating-kb-learning-is-an-open-problem.md).

## Consequences for mining rules from accepted edits

- **Attribution is ambiguous in coupled edits.** A structural rewrite also fixes local clarity issues; which candidate rule did the acceptance actually support?
- **Rules overfit the instance's accidents** — one author's style, one artifact family — because nothing in the acceptance marks which features were load-bearing.
- **A rule can be satisfied while the artifact worsens elsewhere**; the acceptance never promised the rule captures everything the human weighed.

So a loop that mines rules from accepted edits needs **promotion and rollback, not accumulation**: candidates enter as instance-verified, and earn rule status only through repeated independent confirmation — re-verification at the rule level, not inheritance from the instance.

## Boundary

The asymmetry does not make accepted edits weak evidence — they are the best available seed, which is exactly why [spec mining](./spec-mining-as-codification.md) starts from observed accepted behavior. The claim is only that acceptance cannot be *transferred* from the instance to the rule: the rule must be verified as a rule.

---

Relevant Notes:

- [abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — exemplifies: the accepted edit is a success/confirmation that verifies the instance but imports an unearned boundary if abstracted into a rule
- [trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — exemplifies: acceptance is a verify-rung oracle and rule extraction an abstraction-rung operation; this asymmetry is the per-operation claim at the verify/abstraction boundary
- [spec-mining-as-codification](./spec-mining-as-codification.md) — grounds: accepted behavior is the seed material rules are mined from
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — grounds: the instance/rule asymmetry is a position change on the oracle-strength spectrum within one learning loop
- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — extends: locates the open problem precisely at the generalization step, even when instance oracles are strong
- [Gate learning from accepted edits](../reference/proposals/gate-learning-from-accepted-edits.md) — see-also: the Commonplace design that takes this asymmetry as its central constraint
