---
description: Skills and tasks are typed callables — they accept document types as input and produce types as output, and should declare their signatures like functions declare parameter types.
type: note
areas: [claw-design]
status: speculative
---

# Instructions are typed callables with document type signatures

[Document types mark affordances](../claw-design/document-types-should-be-verifiable.md) — a `structured-claim` affords verification, a `spec` affords implementation, an `index` affords navigation. Each type step [trades generality for compound gains in reliability, speed, and cost](./learning-is-capacity-change.md): the structure guarantees the parts are there, making operations reliable without reading the whole document first.

But some documents aren't data — they're *procedures*. Skills, tasks, workflows: their primary affordance is *being followed*. A task has prerequisites, a goal, a checklist of steps, a verification plan. An agent picks it up and executes it. Skills are the same — `/ingest` is a procedure that transforms a source into a `source-review`. These are the document equivalent of callables: the content is a procedure, and the valid operation is execution.

## Skills have type signatures

If types mark valid operations on documents, then instructions that operate on documents should declare which types they accept — the same way functions declare parameter types.

Currently KB operations take a path and hope for the best. `/connect` implicitly expects a `note` or `index`. `/ingest` expects a source file. A verification workflow would expect a `structured-claim`. None of them check.

With type annotations on instructions, you get early validation: "this document is an `index`, but this workflow operates on `structured-claim` — wrong type." The instruction is a function, the document is an argument, and the document's type determines whether the operation is valid.

This gives skills type signatures:

| Skill | Signature |
|-------|-----------|
| `/ingest` | `source → source-review` |
| `/connect` | `note \| index → note \| index` (mutates links) |
| `/validate` | `note → validation-report` |
| `/convert` | `text → note` |

The operations afforded by a type can range from precise semantics (does this `structured-claim` have an `## Evidence` section?) to fuzzy semantics (does the evidence actually support the claim?). The type is the interface; the implementation can [crystallise](./agentic-systems-learn-through-three-distinct-mechanisms.md) from LLM to code as patterns [stabilise](./agentic-systems-interpret-fuzzy-specifications.md) — committing to one interpretation from the space the spec admits.

## Open questions

- Should skill signatures be declared in the skill file itself (machine-readable) or just documented?
- What happens when a skill accepts a union type — does it behave differently per type, or is the union the real input type?
- How do compound documents work — a note that contains both claims and questions?

---

Relevant Notes:
- [document-types-should-be-verifiable](../claw-design/document-types-should-be-verifiable.md) — foundation: types mark affordances; this note extends the idea from data types to function types
- [document-classification](./document-classification.md) — the spec defining the types that would appear in skill signatures
- [learning-is-capacity-change](./learning-is-capacity-change.md) — the capacity framework: each type step trades generality for reliability+speed+cost, making operations reliable without reading the full document
- [stabilisation-is-learning](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the operations afforded by types can themselves crystallise from LLM to code
- [agentic systems interpret fuzzy specifications](./agentic-systems-interpret-fuzzy-specifications.md) — parent framing: operations on types range from fuzzy to precise semantics; stabilisation commits to one interpretation

Topics:
- [claw-design](./claw-design.md)
