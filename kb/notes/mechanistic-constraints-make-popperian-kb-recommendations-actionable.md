---
description: Bounded context and underspecification don't just permit conjecture-and-refutation — they require it; derives three concrete practices (falsifier blocks, contradiction-first connection, rejected-interpretation capture) from KB mechanics.
type: note
traits: []
areas: [kb-design]
status: seedling
---

# Mechanistic constraints make Popperian KB recommendations actionable

This note tries to apply Popperian epistemology — conjecture and refutation — to KB design. It asks whether the KB's computational constraints (bounded context, underspecification, statelessness) give Popperian practices concrete value here, and derives three specific practices from the analysis.

## Why conjecture is forced, not chosen

[Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md), so every agent run selects among multiple valid interpretations. That selection is an implicit hypothesis about what the instruction means in this context. The agent conjectures whether it wants to or not.

This is distinct from claim-level conjecture. A claim-titled note is an object-level proposition ("context efficiency is the central design concern"). A runtime interpretation is an execution-level guess about intent ("the user probably wants me to add a link here, not rewrite the section"). Both are criticizable, but they live at different levels and need different criticism mechanisms:

- **Claims** need explicit falsifiers — conditions stated in the note itself that would invalidate the claim.
- **Interpretations** need capture-on-rejection — when a user corrects "that's not what I meant," the correction should become a durable test case, not a forgotten conversation turn.

## Why criticism must be structural, not ambient

You might think the LLM can just "notice" when claims conflict or interpretations fail. Two constraints prevent this:

[LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — unstructured accumulation causes interference. Contradictions between notes loaded into the same context aren't flagged; they're silently averaged. [Context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — we cannot load everything and let the model sort it out. So criticism that depends on loading two contradictory notes simultaneously is unreliable.

This means criticism must be externalized into the notes themselves. Claim titles and [link semantics](./links.md) already do part of this — [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md), and typed links make foundation/extension/contradiction explicit. But the current system lacks two things: a way to state what would *defeat* a claim, and a systematic pass that looks for contradiction before looking for agreement.

## Whether criticism can converge depends on oracle quality

Not all criticism is useful. [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — criticism converges only when the checking process is better than random and independent of the original error. An LLM re-reading its own note under the same prompt is a correlated check and will not reliably find flaws. A human reviewer, a different prompt strategy, or a structural test (does the falsifier condition hold?) provides decorrelated checking.

This is why falsifier blocks work: they convert criticism from "re-read and see if it still seems right" (correlated, weak) into "check whether this specific condition has been observed" (decorrelated, testable).

## Three practices that follow

### 1. Falsifier blocks on claim notes

Add a short "What would defeat this claim?" block to `note` and `structured-claim` types. The attempt to write one is diagnostic — if you cannot state what would refute a claim, that reveals something about the claim's nature (definitional? tautological? too vague to test?).

Not every claim has a clean falsifier, and that's fine. The value is in the attempt, not universal coverage.

### 2. Contradiction-first connection passes

When `/connect` discovers relationships, it should look for tension and contradiction *before* looking for agreement and extension. The current default is to find notes that "extend" or "ground" the new note. Reversing the priority means criticism is not optional — every note gets at least one check for conflict with existing claims.

### 3. Rejected interpretations become instruction tests

When a user corrects an agent's interpretation ("that's not what I meant"), that rejection is evidence about the instruction's ambiguity. Encoding the rejected case as a test or example in the instruction makes the same failure harder to repeat. This is [stabilisation](./stabilisation.md) driven by error, and across sessions it compounds as [deploy-time learning](./deploy-time-learning-the-missing-middle.md).

## What would defeat this claim?

If bounded-context systems could reliably detect contradictions without externalized structure — e.g. through improved retrieval that always surfaces conflicting notes together — then the "criticism must be structural" argument weakens. The practices might still be useful, but the argument that KB mechanics *force* them would no longer hold.

---

Relevant Notes:
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: why execution already entails conjecture selection
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — grounds: why criticism must be externalized into explicit structure
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — constrains: bounded context makes ambient contradiction detection unreliable
- [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: why falsifier blocks produce better criticism than re-reading
- [stabilisation](./stabilisation.md) — mechanism: user corrections narrow interpretation space by changing instructions
- [deploy-time learning: the missing middle](./deploy-time-learning-the-missing-middle.md) — mechanism: instruction refinements persist across sessions
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — example: existing convention that already externalizes conjectures
- [links](./links.md) — example: existing relation semantics that already structure criticism

Topics:
- [kb-design](./kb-design.md)
