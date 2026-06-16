---
description: "Code resolves a name to its value everywhere; LLM-read prose has no such dereference, so a fact stated once may not govern where it applies — restate it at the point of use, kept honest by a check"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis]
status: speculative
---

# Prose has no reliable dereference, so a declared fact must be reinforced where it applies

*Speculative. The claim rests on modeling LLM interpretation as stochastic, and needs the ablation test below to move past intuition.*

In a formal system a name dereferences: write `status = SEEDLING` once and the value is carried, exactly, into every context that reads it. The reference resolves the same way regardless of distance, surrounding content, or how non-obvious the application is. This is what makes **single-source-of-truth** safe — declare a fact once, reference it everywhere, and the reference does the propagation.

Prose read by an LLM has no such operation. A fact stated in the frontmatter — `status: seedling` — governs a passage three sections down only if the model *infers* that it does: that the label applies here, and that its consequences (hedge the claim, distrust the inference, don't cite it as settled) hold in this case. That inference is not a dereference; it is a probabilistic act, sensitive to content, position, and how obvious the application is. So a single declaration's reach decays with indirection: the further and less obvious the application, the lower the chance the fact is actually in force where it matters.

This holds even if the model is deterministic. We cannot predict, for a given passage, whether it will make the connection, so for design we can only model the application of a declared fact as a stochastic event — a probability of being honored, not a guarantee.

The consequence is that single-source-of-truth, correct for code, is unsafe for prose. To make a fact reliably govern a context you often have to **restate it there** — denormalize: repeat the fact, or the specific consequence it implies, at the point of use. The redundancy a formal system would call a smell is, in prose, what buys reliable propagation.

Denormalization has a cost — the copies can drift from the canonical fact — but it is payable, because the *check* can stay normalized. Keep one external verifier (a validator, a test) that confirms every restatement still matches the source. Denormalize the human- and agent-facing copy for reach; normalize the check that guards it.

## Scope

The reliability of single-source scales with **representational form**. At the codified end — a schema field, a type, a function signature — a declaration dereferences and one statement suffices. At the prose end it does not, and reinforcement is needed. Between them the requirement is graded: the more formal the artifact, and the more local and obvious the application, the fewer restatements; the more prose-like, distant, and non-obvious, the more.

## Testing it (the weak point)

The claim is currently intuition. Its falsifiable form: an agent's adherence to a declared fact — does it actually hedge a `seedling` claim, distrust it, refrain from citing it as settled — should rise when the fact is restated at the point of use versus declared only in frontmatter, and the gap should widen with distance and non-obviousness. Ablation: present the same note with the fact (a) only in frontmatter and (b) also restated at the point of use, and measure the downstream behavior. If a single declaration already propagates reliably — if behavior is the same — the claim is wrong, and single-source-of-truth carries into prose after all.

---

Relevant Notes:

- [representational-form](./definitions/representational-form.md) — grounds: whether a declared name dereferences reliably is a property of representational form; this note draws the normalization consequence for the prose end
- [codification](./definitions/codification.md) — contrasts: at the codified (symbolic) end a declaration dereferences and single-source-of-truth holds; this is the prose end where it fails
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: both move information to the point of use, but frontloading precomputes an instruction's input to spare context, while this restates a fact because runtime propagation is unreliable
