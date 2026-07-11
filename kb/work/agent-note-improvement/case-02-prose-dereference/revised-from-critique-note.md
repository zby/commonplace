---
description: "Code resolves a name to its value everywhere; LLM-read prose has no such dereference, so a fact stated once may not govern where it applies — restate it at the point of use, kept honest by a check"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis, computational-model]
---

# Prose has no reliable dereference, so a declared fact must be reinforced where it applies

In a formal system, a name dereferences. Write `status = SEEDLING` once and every use of that name resolves to the same value. Distance, surrounding content, and the non-obviousness of the application do not change the result. This is what makes **single-source-of-truth** safe in symbolic artifacts: declare the fact once, reference it elsewhere, and the reference does the propagation.

Prose read by an LLM has no equivalent operation. A fact stated in frontmatter, a heading, or a preamble governs a later passage only if the model interprets that fact as relevant there. For `status: seedling`, that means at least two steps: the model must carry forward the literal value, then map it to the right policy for the current use. That second step may mean "treat as provisional," "hedge when citing," or "do not treat as settled," depending on the local task. The application is [underspecified, and unpredictable even when the model is deterministic](./agentic-systems-interpret-underspecified-instructions.md), because the model is interpreting a frame rather than resolving a reference.

The consequence is not that single declarations are always useless in prose. A prominent governing frame can condition the whole read when the fact is salient, the artifact is short, and the operational meaning is clear. The unsafe case is narrower and more important: a single declaration becomes unreliable when the fact's application is distant, non-obvious, or consequence-heavy. The more a reader must infer from "this fact exists" to "this is what I should do here," the less a single source can be trusted to govern the point where the decision is made.

The repair is to put the fact at the nearest reliable control point. Sometimes that is the point of use: a local sentence, warning, or template slot that repeats the value or its required consequence. Sometimes it is a stronger artifact-level control point: frontmatter paired with a generated banner, a heading, a short preamble, or a type contract that agents are explicitly instructed to treat as governing. The point is not repetition for its own sake. The point is to make the relevant fact or policy present at the place the model is likely to consult while acting.

Two forms of reinforcement behave differently:

- **Literal restatement.** Repeat the declared fact itself: this note is `seedling`; this section inherits `status: seedling`; this generated banner reflects the status field. Literal copies are comparatively easy to check, because the validator can compare values.
- **Consequence restatement.** Repeat a policy derived from the fact: hedge this claim; do not cite this as settled; treat this as a lead, not a conclusion. Consequence copies are often more useful to agents, but they are harder to verify because they depend on the policy that maps the fact to action.

Denormalization therefore needs a normalized guard, but the guard must match the kind of copy. A validator or test can cheaply confirm that every literal restatement agrees with the canonical field. A semantic consequence may need a review gate, an explicit type or collection contract, or behavioral tests, because equality on text does not prove the consequence is the right one. Denormalize the human- and agent-facing copy only where propagation risk justifies the added text; normalize the check that keeps the copy aligned with its source.

## Costs

Reinforcement is not free, and the cost rises with how conditional the fact is.

- **Bulk.** Every restatement adds text. An artifact that reinforces several facts, or one fact across many control points, grows. Length is itself a context cost for the next call that loads it.
- **Local overfitting.** A nearby warning can make the reader treat a global fact as if it applied only to the adjacent passage. Reinforcement should preserve the fact's intended scope instead of shrinking it accidentally.
- **Consequence drift.** A broad status can be translated into an overly narrow command. `status: seedling` does not always mean "distrust this"; it may mean "use provisionally and avoid presenting as settled." Derived copy should point back to the policy that licenses it.
- **Conditional applicability pushes branching somewhere.** A `seedling` warning fits a seedling note but not a current one. Reusing one template across statuses means branching on the status, which puts conditional logic in prose; constraining the workflow so the template is only used for one status moves the branching into process. The branching does not vanish.
- **The guard is real work.** The external check that keeps copies honest has to be built, run, and maintained. It is what makes denormalization safe, but it is not free.

## Scope

The reliability of single-source declarations scales with **representational form**. At the codified end, a schema field, type, or function signature can be referenced by machinery that preserves the value exactly. At the prose end, the reader must infer whether a declaration applies and what follows from it. Between them the requirement is graded: the more formal the artifact, and the more local and obvious the application, the fewer reinforcements it needs; the more prose-like, distant, and consequence-heavy the application, the more it needs a reliable control point.

This is a claim about mechanical dereference, not about code and prose as social categories. A code comment can behave like prose. A generated banner or typed template slot can make prose behave more like a symbolic artifact. What matters is whether the consumer has a reliable operation that carries a declared value to the place it is used.

## Testing it (the weak point)

The claim is currently intuition. Its falsifiable form: an agent's adherence to a declared fact should rise when the fact or its policy is placed at a reliable control point near the action, compared with declaring it only in a distant governing field. For `status: seedling`, the measured behavior might be whether the agent treats claims as provisional, avoids citing them as settled, or applies the collection's seedling policy.

Ablation: present the same note with the fact (a) only in frontmatter, (b) also in a prominent artifact-level banner, and (c) also at the local point of use. Vary distance, salience, and whether the expected behavior requires literal value propagation or a derived consequence. If behavior is the same across these forms, then a single declaration already propagates reliably enough, and the denormalization advice is too strong. If literal restatements help but consequence restatements drift, the claim needs to split further between value propagation and policy specification.

---

Relevant Notes:

- [representational-form](./definitions/representational-form.md) — grounds: whether a declared name dereferences reliably is a property of representational form; this note draws the normalization consequence for the prose end
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: applying a declared fact is an interpretive act when the artifact does not mechanically carry the value and policy to the place of use
- [codification](./definitions/codification.md) — contrasts: at the codified, symbolic end a declaration dereferences and single-source-of-truth holds; this is the prose end where it weakens
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: both move information to a more useful place, but frontloading precomputes an instruction's input to spare context, while this reinforces a fact because runtime propagation is unreliable
- [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — exemplifies: this is that rule in the prose regime; the banner is a derived copy of `status`, and because absence costs reach, it must take the checked branch
- [links encode conditional possibilities, not obligations](./links-encode-conditional-possibilities-not-obligations.md) — extends: the same no-dereference logic applied to links; a link is a reference a reader may not follow, so content required for all readers is inlined or otherwise reinforced
