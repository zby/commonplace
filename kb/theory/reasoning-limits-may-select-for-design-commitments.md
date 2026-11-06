---
description: "Conjecture about why immediate coding success can underselect project-specific structure: authors who can proceed without it miss a pressure that benefits later contributors."
type: types/note.md
traits: [title-as-claim]
---

# Reasoning limits may select for design commitments

A programmer may restrict how code is organized because they need those restrictions to write the next part. Useful structure could therefore arise from the author's need to understand the code, even when making it maintainable is not an explicit goal. An LLM that can complete the same change without those restrictions may face less pressure to introduce them, even when they would help later contributors.

This is a conjecture about how useful structure arises. The proposed human–LLM difference and its training explanation remain untested.

Here, a **design commitment** is a restriction on acceptable future implementations: only one component owns a state transition, validation happens at a particular boundary, or two subsystems remain independent even when sharing code would remove duplication. A commitment is unwritten when its holder relies on it without recording it as a shared requirement. It need not be a formal invariant or an explicitly stated rule.

## Structure can be selected through the author's own difficulty

The proposed mechanism is:

1. The author cannot reliably track the interactions needed for the next change.
2. The author introduces boundaries, conventions, or abstractions that restrict those interactions.
3. Those restrictions make further work manageable for that author.
4. Where the restrictions also help later contributors, maintainability is a by-product of solving the author's immediate reasoning problem.

The benefit need not have been selected directly as a maintainability objective. Restrictions that suit the original author can also hinder others. Reasoning difficulty can also produce bad abstractions, abandonment, or mistakes. Experiments must establish both the range in which the mechanism produces useful commitments and the benefit to later contributors.

General practices such as SOLID supply some restrictions but leave project-specific choices unresolved. Avoiding duplication can conflict with keeping components independent. A local design commitment settles which consideration takes priority in this project and why. Applying familiar practices case by case does not necessarily preserve that decision across changes.

## Useful commitments can make code easier to describe

A useful commitment can replace many separate facts with a rule and its exceptions. If all state changes pass through one function, a contributor can use that rule to locate behavior instead of remembering each path independently. The compression hypothesis is that the rule and its exceptions are easier for that contributor to represent and use than the separate facts. Additional structure helps only when it achieves this reduction; elaborate rules with many exceptions can cost more than they save.

This connects to Jürgen Schmidhuber's [Formal Theory of Creativity, Fun, and Intrinsic Motivation](../sources/schmidhuber-formal-theory-creativity.ingest.md), which proposes encouraging actions expected to improve a world model's performance and describes compression cost as including both the predictor and deviations from its predictions. Applying this framework to code organization is our conjecture: organizing code can make it easier for its author to model. Its objective is progress in modeling, rather than compressibility alone; a compact organization that is already understood offers no further progress merely by remaining compact.

## The proposed human–LLM difference is a selection difference

LLMs may sometimes complete changes without introducing restrictions a human would need to continue reasoning. If training rewards successful changes of limited scope more strongly than their consequences for later contributors, it can underselect those additional commitments.

Two candidate explanations need separate tests:

- A model may handle a larger change without comparable reasoning aids.
- Its training may provide insufficient feedback from later modification.

Neither explanation follows from the length of the model's context window.

Training on continued modification and contributor handoffs could reward commitments that improve later work. Rewarding architectural-looking output alone could instead produce unnecessary layers and rules.

## Unwritten commitments do not reliably survive contributor changes

Contributor changes already pose a problem for human teams: one author's useful restrictions may be unknown to another, and independently invented restrictions may conflict. Fresh agent invocations face the same transfer problem whenever prior project-specific understanding is absent from their supplied context. Fresh invocations retain general programming competence; the local commitments must be recovered or supplied again.

Recording commitments and their reasons is one candidate way to preserve continuity. Code may show that all state changes currently pass through one function without establishing whether this is deliberate or incidental. A retained record can distinguish those cases and explain what a future change must preserve. The [rationale-retention argument](./design-rationale-must-preserve-unregenerable-decision-premises.md) identifies why some such premises cannot be faithfully reconstructed from implementation and general knowledge. Recording them helps only if later contributors retrieve, interpret, and use them.

For KB design, the continuity problem is the central implication: fresh agents modifying a shared artifact system need access to the local commitments its organization depends on, not just generic writing or engineering practices.

## Predictions and tests

Test the prediction across a sequence of changes. A useful comparison would track when humans and models introduce commitments and whether those commitments precede or follow reasoning failures. It would also test whether an independent contributor can make the next change more reliably at comparable total cost.

### Reasoning-difficulty mechanism

Consider a range where the author can still solve the task. Within that range, reducing the author's effective ability to track interactions should lead the author to introduce more useful commitments before failure. Merely reducing change size or adding stylistic structure would not satisfy that prediction. If commitments instead follow only explicit instructions or learned conventions, the reasoning-difficulty explanation loses support.

### Training explanation

Compare selection for immediate success with selection that includes later changes and fresh contributors. An improvement only under the latter would be consistent with the proposed selection gap. Attributing that improvement to design commitments would also require checking whether the reward for later work improved other aspects of the solutions. If selection for bounded changes preserves equally useful commitments, the training explanation loses support.

### Retention intervention

Compare the same code with and without accurate commitment records. Control available information and total effort. No improvement in later coherent modification would count against the proposed benefit of making the commitments visible.

## Scope

- The mechanism concerns commitments introduced to support reasoning. Product requirements, explicit architecture instructions, and enforced contracts can supply structure independently.
- New requirements may call for deliberately revising a commitment and explaining why.

---

Relevant Notes:

- [Project-theory possession requires comparing new demands with existing organization](./project-theory-relates-new-demands-to-existing-organization.md) — contrasts: tests whether commitments guide modification; this note asks what pressure produces those commitments in the first place.
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — enables: identifies what a retained commitment record must supply when a fresh contributor cannot reconstruct it.
