---
description: "Conjecture about why immediate coding success can underselect project-specific structure: authors who can proceed without it miss a pressure that benefits later contributors."
type: types/note.md
traits: [title-as-claim]
---

# Reasoning limits may select for design commitments

A programmer may restrict how code is organized because they need those restrictions to write the next part. Useful structure could therefore arise from the author's need to understand the code, rather than an explicit goal of making it maintainable. An LLM that can complete the same change without those restrictions may face less pressure to introduce them, even when they would help later contributors.

This is a conjecture about how useful structure arises. The proposed human–LLM difference and its training explanation remain untested. Greater capacity to work without these restrictions could remove one reason to introduce them; it need not produce worse code.

Here, a **design commitment** is a restriction on acceptable future implementations: only one component owns a state transition, validation happens at a particular boundary, or two subsystems remain independent even when sharing code would remove duplication. A commitment is unwritten when its holder relies on it without recording it as a shared requirement. It need not be a formal invariant or an explicitly articulated rule.

## Structure can be selected through the author's own difficulty

The proposed mechanism is:

1. The author cannot reliably track the interactions needed for the next change.
2. The author introduces boundaries, conventions, or abstractions that restrict those interactions.
3. Those restrictions make further work tractable for that author.
4. Where the restrictions also help later contributors, maintainability is a by-product of solving the author's immediate reasoning problem.

The benefit need not have been selected directly as a maintainability objective. Conversely, restrictions that merely suit the original author can obstruct others. More structure is not automatically better structure; its value depends on subsequent work.

General practices such as SOLID supply some restrictions but leave project-specific choices unresolved. Avoiding duplication can conflict with keeping components independent. A local design commitment settles which consideration takes priority here and why. Applying familiar practices case by case does not necessarily preserve that settlement across changes.

## The proposed human–LLM difference is a selection difference

The hypothesis is not that LLMs use no structure. It is that they can sometimes complete changes without introducing restrictions a human would need to continue reasoning. If training rewards successful bounded changes more strongly than their consequences for subsequent contributors, it can underselect those additional commitments.

Two candidate explanations need separate tests. A model may handle a larger change without comparable reasoning aids. Its training may also provide insufficient feedback from later modification. Neither follows from the length of its context window. Effective code-tracking capacity, human working memory, and training objectives cannot be equated merely by analogy.

This is not proposed as a permanent model limitation. Training on continued modification and contributor handoffs could reward commitments that improve later work. Rewarding architectural-looking output alone could instead produce unnecessary layers and rules.

## Unwritten commitments do not reliably survive contributor changes

A human team already faces this problem: one author's useful restrictions may be unknown to another, and independently invented restrictions may conflict. Fresh agent invocations face the same transfer problem whenever prior project-specific understanding is absent from their supplied context. General programming competence survives; the local commitments must be recovered or supplied again.

Writing commitments and their reasons down is a candidate continuity mechanism. Code may show that all state changes currently pass through one function without establishing whether this is deliberate or incidental. A retained record can distinguish those cases and explain what a future change must preserve. The [rationale-retention argument](./design-rationale-must-preserve-unregenerable-decision-premises.md) identifies why some such premises cannot be faithfully reconstructed from implementation and general knowledge. Recording them helps only if later contributors retrieve, interpret, and use them.

## Discriminating tests

The prediction concerns sequences of changes, not the appearance of a finished patch. A useful comparison would track when humans and models introduce commitments and whether those commitments precede or follow reasoning failures. It would also test whether an independent contributor can make the next change more reliably at comparable total cost.

For the proposed mechanism, consider a range where the author can still solve the task. Within that range, reducing the author's effective ability to track interactions should increase the introduction of useful commitments before failure. Merely reducing change size or adding stylistic structure would not satisfy that prediction. If commitments instead follow only explicit instructions or learned conventions, the reasoning-difficulty explanation loses support.

For the training explanation, compare immediate-success selection with selection that includes later changes and fresh contributors. An improvement only under the latter would support the proposed selection gap. If bounded-change selection preserves equally useful commitments, that explanation loses support.

For the retention intervention, compare the same code with and without accurate commitment records. Control available information and total effort. No improvement in later coherent modification would count against the proposed benefit of making the commitments visible.

## Scope

- This note supplies a mechanism to test, not prevalence evidence that humans introduce more useful structure than current LLMs.
- The mechanism concerns commitments introduced to support reasoning. Product requirements, explicit architecture instructions, and enforced contracts can supply structure independently.
- Reasoning difficulty can also produce bad abstractions, abandonment, or mistakes. The useful operating range and the benefit to later contributors must be established experimentally.
- Preserving a commitment is not always correct. New requirements may require revising it; successful continuity includes deliberate revision with reasons.
- The contribution to KB design is the continuity problem: fresh agents modifying a shared artifact system need access to the local commitments its organization depends on, not just generic writing or engineering practices.

---

Relevant Notes:

- [Project-theory possession requires comparing new demands with existing organization](./project-theory-relates-new-demands-to-existing-organization.md) — contrasts: tests whether commitments guide modification; this note asks what pressure produces those commitments in the first place.
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — enables: identifies what a retained commitment record must supply when a fresh contributor cannot reconstruct it.
