# PROPOSED: Writing conventions for kb/reference/ (descriptive register)

> Workshop draft. Delta from current `kb/reference/COLLECTION.md`:
> - Outbound linking section reorganised **per destination collection** rather than by register. Each destination block declares when the connect skill should search it and which labels writers may use.
> - Intra-descriptive labels proposed explicitly (was previously a loose list: `cross-reference / see-also / supersedes`). Added `part-of` and `implements` to cover component/abstract-to-concrete relations.
> - `cross-reference` and `describes` dropped per [`label-audit.md`](./label-audit.md) — neither names a specific reader-need; both absorb into `part-of` or `see-also`.
> - Cross-collection labels selected from the shared catalogue in [`link-vocabulary.md`](./link-vocabulary.md). This `COLLECTION.md` is authoritative for writers; `link-vocabulary.md` is a resource for `COLLECTION.md` authors.
> - All other sections unchanged.

## Register

This collection operates in the **descriptive [register](../../notes/definitions/register.md)** (one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules). Documents here account for what exists in the shipped commonplace system — its architecture, type system, operator surface, and decision history. They aim for faithful representation of the system as built, not transferable theory about KB methodology.

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

Outbound rules are organised by destination collection. Each block declares when to search the destination for link targets and which labels writers may use.

### → `kb/reference/` (within this collection)

**Search:** when the current doc describes a piece of a larger described system, a realization of a specified contract, or a decision that updates or follows from an earlier ADR.

**Labels:**

| label | reader-need |
|---|---|
| `part-of` / `contains` | wants to situate this in the larger system |
| `implements` / `implemented-by` | wants the concrete realization (or the abstract contract) |
| `supersedes` / `superseded-by` | wants the current or prior version (primarily ADR chains) |
| `see-also` | might benefit but author can't name a specific need; use sparingly |

### → `kb/agent-memory-systems/`

**Search:** uncommon but worth a scan — commonplace and external systems occasionally share design patterns, and thematic adjacency can be instructive. Search when a design decision has known analogues, contrasts, or antecedents in reviewed systems, whether or not the connection was explicit. Let the agent filter.

**Labels:**

| label | reader-need |
|---|---|
| `see-also` | the external system is an instructive adjacent reference |

### → `kb/notes/`

**Search:** when a design choice here rests on a theoretical claim. Descriptions justify their shape by pointing at theory; this is the primary theory-ward edge.

**Labels:**

| label | reader-need |
|---|---|
| `rationale` | this design rests on this claim |
| `defined-in` | reader may not know a term; target is under `kb/notes/definitions/` |
| `see-also` | might benefit but no specific need; use sparingly |

### → `kb/instructions/`

**Search:** when the described system component has an operational how-to documented as an instruction. Reference docs point outward to the instructions that act on them.

**Labels:**

| label | reader-need |
|---|---|
| `procedure` | for how to do this, see this instruction |
| `see-also` | might benefit but no specific need; use sparingly |

**Fidelity constraint.** Descriptions must be faithful to the system as built, even when the implementation deviates from the theory that inspired it. If the system does X but the theory says Y, the description says X and notes the deviation — the `rationale` link may carry the qualifier.

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
