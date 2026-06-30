---
description: "Code resolves a name to its value everywhere; LLM-read prose has no such dereference, so a fact stated once may not govern where it applies — restate it at the point of use, kept honest by a check"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis, computational-model]
status: seedling
---

# Prose has no reliable dereference, so a declared fact must be reinforced where it applies

In a formal system, a reference can mechanically resolve to a declaration: write `status = SEEDLING` once and every context that reads the name receives that value. Distance, surrounding content, and non-obvious applications do not change the result. Single-source declarations are safe where references perform that propagation operation.

Prose read by an LLM has no such operation. A fact stated in frontmatter — `status: seedling` — governs a passage three sections down only if the model infers that the label matters there. Restating the literal value is easier to check than restating its interpreted consequences, but even the consequence still has to be applied: hedge this claim, distrust this inference, do not cite this as settled. That application is not dereference but interpretation — [underspecified, and unpredictable even when the model is deterministic](./agentic-systems-interpret-underspecified-instructions.md) — sensitive to content, position, and how obvious the use is. A single declaration's reach therefore decays with indirection: the further and less obvious the application, the lower the chance the fact is in force where it matters.

The consequence is that single-source declarations, reliable where references mechanically resolve, are unsafe as the only control for prose. To make a fact reliably govern a prose context, reinforce it at the nearest reliable control point, often the point of use. The reinforcement may repeat the fact itself or a specific consequence it implies. The redundancy a formal system would call a smell is, in prose, what buys reliable propagation.

Denormalization has a cost — the copies can drift from the canonical fact — but it is payable when the *check* stays normalized. Keep one external verifier, such as a validator or test, that confirms every restatement still matches the source. Denormalize the human- and agent-facing copy for reach; normalize the check that guards it.

## Costs

Reinforcement is not free, and the cost rises with how conditional the fact is.

- **Bulk.** Every restatement adds text. An artifact that reinforces several facts, or one fact across many points of use, grows; length is itself a context cost for the next call that loads it.
- **Conditional applicability pushes branching somewhere.** A restatement is keyed to one value of the fact: a `seedling` warning fits a seedling note but not a `current` one. Reusing one template across statuses requires branching the template, while constraining the workflow so the template is only used in one case moves the branching into process. Denormalization stays cheap only when the fact holds unconditionally wherever it is restated.
- **The guard is real work.** The external check that keeps copies honest has to be built and run. It is what makes denormalization safe, but it is not free.

## Scope

The reliability of single-source scales with **representational form**. At the codified end — a schema field, a type, a function signature — a declaration dereferences and one statement suffices. At the prose end it does not, and reinforcement is needed. Between them the requirement is graded: the more formal the artifact, and the more local and obvious the application, the fewer restatements; the more prose-like, distant, and non-obvious, the more.

## Testing it

The falsifiable form: an agent's adherence to a declared fact should rise when the fact is restated at the point of use instead of declared only in frontmatter. For a `seedling` note, downstream behavior should more often hedge the claim, distrust the inference, or avoid citing it as settled; the gap should widen with distance and non-obviousness. Ablation: present the same note with the fact (a) only in frontmatter and (b) also restated at the point of use, then measure the downstream behavior. If a single declaration already propagates reliably — if behavior is the same — the claim is wrong, and single-source declarations carry into prose after all.

---

Relevant Notes:

- [representational-form](./definitions/representational-form.md) — grounds: whether a declared name dereferences reliably is a property of representational form; this note draws the normalization consequence for the prose end
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: that applying a declared fact is an interpretive, unpredictable act — even a deterministic model picks an interpretation you can't read off the spec — is the premise behind "no reliable dereference"
- [codification](./definitions/codification.md) — contrasts: at the codified (symbolic) end a declaration dereferences and single-source-of-truth holds; this is the prose end where it fails
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: both move information to the point of use, but frontloading precomputes an instruction's input to spare context, while this restates a fact because runtime propagation is unreliable
- [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — exemplifies: this is that rule in the prose regime — the banner is a derived copy of `status`, and because "absent" costs reach, it must take the *checked* branch (denormalize the copy, normalize the check)
- [links encode conditional possibilities, not obligations](./links-encode-conditional-possibilities-not-obligations.md) — extends: the same no-dereference logic applied to links — a link is a reference a reader may not follow, so content required for all readers is inlined, not linked
