---
description: "Conjectures that an unrecoverable governing intent yields more local rationale per token than rationale snippets, while contingent design facts need their own record"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [document-system, context-engineering]
---

# A specific intent may out-yield local rationales, but contingent facts stay separate

A retained design theory should hold what an interpreter — the reader or agent reconstructing design understanding — cannot recover from the artifact and the interpreter's general knowledge, since [design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md). That criterion sets the retention boundary. This note makes a narrower, unmeasured conjecture about priority inside that boundary: when a specific governing purpose is not otherwise recoverable, retaining that **intent** should reconstruct more local rationale per token than retaining an equal-size bundle of local rationale snippets.

**Contingent facts** are outside that comparison. Choices, encounters, conventions, and limits that do not follow from the purpose still need separate retention when no artifact, standard, history, or available context carries them.

## Why intent may out-yield local rationales

Given a specific intent and the implementation, an interpreter can reconstruct several local judgments. It can ask why each part serves the purpose, which facts matter to that purpose, and whether a new demand belongs under the same purpose or a different one. In *Programming as Theory Building*, Peter Naur describes the theory-holder as someone who “can explain why each part of the program is what it is” and can support the program text with justification ([Programming as Theory Building](../sources/programming-as-theory-building.ingest.md)). Naur supports the role of design theory in justification. The per-token ranking is this note's conjecture.

Yield here means useful local judgments reconstructed per token retained. A specific intent is plausibly high-yield because one purpose can constrain many parts, while one local rationale usually explains fewer. But upstream position does not guarantee the highest yield overall. A rationale that encodes a shared invariant, or a compact hard constraint such as a regulatory prohibition, can govern more choices than a broad purpose. The conjecture therefore compares intent with a same-size set of local rationales, not with every other kind of retained knowledge.

This is why an instruction can often retain its goal while omitting reasons that follow from the goal and the steps, as [an author should fix what the executor can't determine](./fix-what-the-executor-cant-determine-not-what-it-will.md). It should still retain a step rationale when that rationale records a contingent constraint or decision. Losing the goal removes the seed for local reconstruction, which helps explain why [a goal-holding interpreter fails soft](./a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md).

## The limit: contingent fact

Yield is a property of the intent-interpreter pair. A stronger interpreter may derive more from artifact plus intent, especially when it can also inspect tests, history, logs, or current standards. Only facts unavailable from those inputs remain unregenerable. Purpose alone does not supply several common kinds:

- **Selected alternative and decision status.** The artifact may expose what was implemented, but intent alone does not reveal the rejected alternatives, why the selection remains binding, or whether it was incidental. [Naur's account](../sources/programming-as-theory-building.ingest.md) treats qualities such as simplicity and good structure as comparisons against possible program texts not present in the artifact. This note's narrower inference is to record the decision basis when later work must not reverse the choice by accident.
- **Unavailable world-side forces.** A purpose does not supply project-specific facts about payment rails, regulators, upstream systems, or physical constraints. When a test, type boundary, or other artifact already exposes the force, that representation may make a separate account unnecessary.
- **Encountered observations and results.** A measured performance limit, failure trace, or user-reported surprise is learned from the world rather than inferred from purpose. It must remain available when it changes what later work should believe or do.
- **Applicability limits not included in the intent.** A scoped purpose can name its own domain, but an unrecorded boundary does not follow from an unscoped one. Extending a design safely requires whichever limits the governing intent and artifact do not already state.
- **Arbitrary conventions.** When several values serve the purpose equally and no external standard selects one, the chosen value cannot be reconstructed from purpose or general knowledge.

Intent can therefore be a high-yield inference seed without replacing contingent facts. The two answer different reconstruction failures: retaining more intent does not recover a fact that was never entailed by the purpose, and retaining more facts does not necessarily help reconstruct rationale elsewhere.

## Testable prediction

Compare three agents under the same token budget on artifacts whose specific intent and selected contingent facts are not otherwise recoverable. Give the first agent the intent, the second local rationales for non-held-out parts of the artifact, and the third a compact selection of decision bases, encountered forces or results, and scope limits.

On held-out parts, the intent-fed agent should reconstruct local justifications better than the local-rationale-fed agent. On tasks that depend on selected contingent facts, the fact-fed agent should do better: avoid reversing a binding decision, recover an encountered force or result, and respect a withheld limit.

The yield conjecture fails if equal-budget local rationales match or beat a specific intent at reconstructing held-out local justifications across representative artifacts. The contingent-fact boundary fails if intent alone reliably recovers facts genuinely absent from the artifact and background context.

## Scope

- **The comparison is an unmeasured conjecture.** “Out-yield” means more held-out local rationale reconstructed per retained token; the experiment above, not the title, must establish the ranking.
- **Intent means first-order governing purpose.** A purpose may already include audience, domain, or done-conditions. Such content is not a separate contingent fact merely because it also constrains the design.
- **Specificity and recoverability are preconditions.** A vague intent, or one already obvious from the artifact, may add less than a compact constraint, decision record, or observation. This note makes no claim that intent has the highest overall retention value across those rivals.

---

Relevant Notes:

- [Theory-mediated self-improvement needs both interpretation and retention](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — grounds: gives the interpreter/retained-text split that makes a seed's yield the retention question
- [Bottom-up structure inference needs capture at the decision surface, not the state](./structure-inference-needs-capture-at-the-decision-surface.md) — mechanism: explains why contingent decision knowledge must be captured while its context is still live
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — extends: develops the selected-alternative category into the commitment/derivation boundary
- [A bare writing prompt does not determine its intended contribution](./a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) — evidenced-by: gives a compact case where topic and output form do not recover intent
- [Memory-backed personalization can look like model improvement](./memory-backed-personalization-can-look-like-model-improvement.md) — enables: gives the source, subject, scope, and status record shape a person-supplied intent needs to be retained usably
- [Content routing](../reference/content-routing.md) — see-also: applies the regeneration-source and intent/contingent-fact distinction to artifact placement
