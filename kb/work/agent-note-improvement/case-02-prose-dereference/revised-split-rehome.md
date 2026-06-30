---
description: "Code resolves a name to its value everywhere; LLM-read prose has no such dereference, so a fact stated once may not govern where it applies — restate it at the point of use, kept honest by a check"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis, computational-model]
status: seedling
---

# Prose has no reliable dereference, so a declared fact must be reinforced where it applies

In a formal system, a name dereferences. Write `status = SEEDLING` once and any later reference can resolve to that value exactly. Distance, surrounding prose, and non-obvious consequences do not change the lookup. Single-source-of-truth is safe where this mechanical resolution exists: declare the fact once, refer to it elsewhere, and the system carries the value.

LLM-read prose has no equivalent operation. A fact stated in frontmatter — `status: seedling` — governs a passage three sections down only if the model *interprets* it that way: the label applies here; this claim should be hedged; this inference should be distrusted; this note should not be cited as settled. That is not dereference. It is an [underspecified interpretation](./agentic-systems-interpret-underspecified-instructions.md), sensitive to position, surrounding content, and how obvious the consequence is.

So a declaration's reach decays with indirection. The further away the use is, and the less obvious the consequence, the less reliable it is that the fact remains in force where it matters.

The operational consequence is uncomfortable but useful: single-source-of-truth, safe in codified forms, is unsafe for prose-facing control. To make a fact reliably govern a context, often you have to **restate it there**. Denormalize the reader-facing copy: repeat the fact, or the consequence it implies, at the point of use. The redundancy a formal system would call a smell is, in prose, what buys propagation.

That does not license unchecked duplication. Repeated prose copies can drift from the canonical fact. The safe pattern is asymmetric: **denormalize the copy for reach; normalize the check for honesty**. Keep one verifier — a validator, test, or generation step — that confirms each restatement still matches the source.

## Costs

Reinforcement is not free.

- **Bulk.** Every restatement adds text. Reinforcing many facts, or one fact in many places, raises the context cost for the next agent that reads the artifact.
- **Conditional facts push branching somewhere.** A `seedling` warning fits a seedling note but not a `current` one. If one template spans both cases, the template needs prose branching. If the template stays branch-free, the workflow must constrain when it is used. Either way, conditionality has to live in the template, the process, or the validator.
- **The guard is real work.** The external check is what makes denormalization safe, and it has to be built and run.

Denormalization is cheapest for facts that apply unconditionally wherever repeated. It gets expensive when the fact is value-dependent, context-dependent, or easy to restate with a slightly wrong consequence.

## Scope

The need for reinforcement scales with **representational form**. At the codified end — schema fields, types, function signatures — declarations dereference and one statement can suffice. At the prose end, they do not. Between them the requirement is graded: the more formal, local, and obvious the application, the fewer restatements; the more prose-like, distant, and non-obvious, the more reinforcement is needed.

## Testing it

The weak point is empirical. An agent's adherence to a declared fact should improve when the fact is restated at the point of use rather than declared only once, and the improvement should grow with distance and non-obviousness.

Ablation: present the same note with a fact only in frontmatter, then with the fact or its consequence repeated at the relevant passage. Measure downstream behavior: does the agent hedge a `seedling` claim, distrust the inference, and avoid citing it as settled? If behavior is the same, the claim is wrong and single-source-of-truth carries farther into prose than this note predicts.

---

Relevant Notes:

- [representational-form](./definitions/representational-form.md) — grounds: whether a declared name dereferences reliably is a property of representational form; this note draws the normalization consequence for the prose end
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: that applying a declared fact is an interpretive, unpredictable act — even a deterministic model picks an interpretation you can't read off the spec — is the premise behind "no reliable dereference"
- [codification](./definitions/codification.md) — contrasts: at the codified (symbolic) end a declaration dereferences and single-source-of-truth holds; this is the prose end where it fails
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: both move information to the point of use, but frontloading precomputes an instruction's input to spare context, while this restates a fact because runtime propagation is unreliable
- [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — exemplifies: this is that rule in the prose regime — the banner is a derived copy of `status`, and because "absent" costs reach, it must take the *checked* branch (denormalize the copy, normalize the check)
- [links encode conditional possibilities, not obligations](./links-encode-conditional-possibilities-not-obligations.md) — extends: the same no-dereference logic applied to links — a link is a reference a reader may not follow, so content required for all readers is inlined, not linked
