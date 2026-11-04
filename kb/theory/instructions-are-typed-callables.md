---
description: Skills and tasks are typed callables — they accept document types as input and produce types as output, and should declare their signatures like functions declare parameter types.
type: types/note.md
traits: [title-as-claim]
tags: []
---

# Instructions are typed callables with document type signatures

[Document types mark affordances](./document-types-should-be-verifiable.md): a structured claim can be reviewed for evidential support, while an index can be used for navigation. Instructions that operate on these documents can declare their input and output types. This makes their interfaces checkable before an agent follows the procedure.

Skills, tasks and workflows are callable in this limited sense: a caller supplies inputs and asks an executor to perform an operation. Their bodies may remain natural-language procedures. Declaring a signature does not turn those procedures into conventional functions or establish their correctness.

## Skills have type signatures

A path alone does not state which document type an operation accepts. An enforced signature can reject an index passed to a workflow that requires a structured claim. It establishes interface compatibility, not that the document's evidence is good or that the workflow will review it correctly.

Illustrative signatures, rather than a catalog of current commands:

| Operation | Signature |
|---|---|
| Source analysis | `source → source-analysis` |
| Connection discovery | `note → connection-report` |
| Structural validation | `note → validation-report` |
| Note conversion | `text → note` |

A signature must describe the operation's actual outputs and mutations. A connection report and an edited note are different results; a caller needs to know which one a procedure promises.

## The signature leaves semantic questions open

Consider two checks on a structured claim: whether it contains an Evidence section, and whether that evidence supports its conclusion. The first can use a heading predicate. The second needs a standard for support and evidence sufficient to apply it. Both can return a review report, so their shared signature does not capture this difference.

The [governing reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) determines what counts as the operation's semantics. Adopting a model package as that reference can fix the support-checking operation's semantics, even when predicting its judgments is costly. Under an English requirement, the caller, reviewer or stated conventions must settle what support means. Neither choosing a model reference nor implementing a predicate establishes adequacy to that requirement.

The implementation can change while the interface stays fixed. Rewriting a check as code is [codification](./definitions/codification.md); treating it as a checked [program refinement](./definitions/program-refinement.md) additionally requires evidence that it preserves the applicable guarantees. Stable behavior alone supplies neither that evidence nor a reason to prefer code.

## Open questions

- Should skill signatures be declared in the skill file itself (machine-readable) or just documented?
- What happens when a skill accepts a union type — does it behave differently per type, or is the union the real input type?
- How do compound documents work — a note that contains both claims and questions?

---

Relevant Notes:

- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — foundation: types mark affordances; this note extends the idea from data types to function types
- [collections and types](../reference/collections-and-types.md) — the artifact type model whose contracts would appear in skill signatures
- [codification](./definitions/codification.md) — the operations afforded by types can themselves codify from LLM to code
- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: separates the governing semantic reference from adequacy to an English requirement
