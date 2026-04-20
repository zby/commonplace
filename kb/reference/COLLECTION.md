# Writing conventions for kb/reference/ (descriptive register)

## Register

This collection operates in the **descriptive register**. Documents here account for what exists in the shipped commonplace system — its architecture, type system, operator surface, and decision history. They aim for faithful representation of the system as built, not transferable theory about KB methodology.

The quality goal is **fidelity + economy**: say what the system actually does, in minimum tokens, without omitting load-bearing details. A description that misrepresents the system is worse than none; a description that takes 2000 tokens where 500 would do wastes bounded context.

## Title conventions

**Topical titles by default.** Name the document after what it describes: "Type loading", "Available types", "Storage architecture". The title should answer "what is this about?" not "what does this argue?"

Composability test: a link like `see [type loading](./type-loading.md) for how types are resolved` should read naturally. Topical titles work as noun-phrase references.

**Exceptions.** ADRs use a numbered-decision format: `012-types-for-structure-traits-for-review.md`. Definitions use the term itself as title.

## Description conventions

For reference docs, descriptions should name the specific system aspect covered — "how commonplace resolves a note's type contract at authoring and validation time" beats "type loading in commonplace".

## Economy as quality discipline

Reference docs face the hardest economy pressure. An agent loading system documentation into context is usually trying to do something — write a note, debug validation, understand a decision. Every token beyond what's needed for that task competes with the task itself.

Quick tests:
- Could this section be cut without losing information the reader needs to act?
- Is the same fact stated in two places? Deduplicate or link.
- Would a table or list say this more compactly than prose?

Economy is a goal, not a gate. Some topics genuinely need exposition. But prefer compact forms when they don't sacrifice clarity.

## Outbound linking conventions

When linking FROM this collection:

| To register | Appropriate relationships | Notes |
|---|---|---|
| Descriptive (same register) | cross-reference / see-also / supersedes | Internal navigation within the system account. ADRs reference each other through supersedes chains. |
| Theoretical (kb/notes/) | rationale — "shaped this way because [theory]" | Descriptions can cite theories as justification for design choices. The description depends on the theory — if the theory changes, the design rationale may need revision. |
| Prescriptive (kb/instructions/) | procedure — "for how to do this, see [instruction]" | Reference docs point to instructions for the operational how-to. |

**Fidelity constraint.** Descriptions must be faithful to the system as built, even when the implementation deviates from the theory that inspired it. If the system does X but the theory says Y, the description says X and notes the deviation.

## Types

- `note` -> `kb/types/note.md`
  Use for general shipped-system reference documents.
- `adr` -> `kb/reference/types/adr.md`
  Use for architecture decision records.
- `definition` -> `kb/types/definition.md`
  Use for shipped-system vocabulary terms.
- `index` -> `kb/types/index.md`
  Use for reference navigation hubs and generated directory indexes.

## What does NOT belong here

- Transferable claims about KB methodology → theoretical register (`kb/notes/`)
- Procedures and how-to guidance → prescriptive register (`kb/instructions/`)
- Descriptions of external systems → `kb/agent-memory-systems/reviews/`
- Work in progress → `kb/work/` (workshops)
- Generated operational artifacts → `kb/reports/`
