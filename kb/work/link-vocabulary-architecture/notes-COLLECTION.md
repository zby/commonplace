# PROPOSED: Writing conventions for kb/notes/ (theoretical register)

> Workshop draft. Delta from current `kb/notes/COLLECTION.md`:
> - Outbound linking section reorganised **per destination collection** rather than by register. Each destination block declares when the connect skill should search it and which labels writers may use.
> - Intra-collection labels align with the seven canonical labels (ADR 009 + ADR 018 draft), replacing the current informal mix of `since / because / contradicts / extends / qualifies`.
> - Cross-collection labels selected from the shared catalogue in [`link-vocabulary.md`](./link-vocabulary.md). This `COLLECTION.md` is authoritative for writers; `link-vocabulary.md` is a resource for `COLLECTION.md` authors.
> - All other sections unchanged.

## Register

This collection operates in the **theoretical [register](../../notes/definitions/register.md)** (one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules). Documents here make transferable claims about what is true — mechanisms, principles, and general arguments that should hold across systems, not just in this one.

The quality goal is **reach**: the most general formulation the argument supports, with boundaries mapped explicitly. A note with reach compresses many situations into one explanation, making bounded context work harder.

## Title conventions

**Claim titles by default.** Name the note like a claim, not a topic: "structure enables navigation without reading everything" rather than "thoughts on structure." The title should be something that could be true or false.

Composability test: the title should work as prose when linked — `since [title](./title.md)` or `because [title](./title.md)` should read naturally.

Claim strength test: the claim should be contestable. "Continuous learning is substrate-independent" fails — nobody would push back. "Continuous learning can happen outside of weights" names the thing people actually doubt.

**Exceptions.** Don't force a claim title when it feels strained. Common exceptions:
- Multi-claim specs and frameworks (no single claim subsumes the content)
- Definitional notes (the title is the term being defined)
- Indexes (navigation hubs)
- Seedlings not ready to assert a clear claim

If using a claim title, add the `title-as-claim` trait so review gates can check the promise.

## Note composability

A note should be linkable from other notes without dragging irrelevant context. The title-level prose test checks whether the link text can work in an argument; the note-level composability test asks whether the body is focused enough that another note can use it as a premise without inheriting unrelated claims, examples, or local context.

If a note has one strong claim plus a second cluster that future links would not want to import, split the cluster into another note or move it to `kb/work/` until its role is clear.

## Reach as quality discipline

Aim for notes that explain *why*, not just record *what works*. Quick tests:
- If you changed one premise, could you predict what changes in the conclusion?
- Would the insight still apply in a different domain?
- Could someone say exactly how the explanation is wrong, not just that it's incomplete?

Notes that only record "X works" are adaptive — useful but brittle. Notes that explain why X works have reach. Reach is a goal to move toward, not a gate every note must clear.

**Formulation constraint.** The theory's claim — title and opening argument — must be statable in general terms, even when derived from a specific system. If you can't state it without referencing a particular system, it's not yet a theory.

## Outbound linking conventions

Outbound rules are organised by destination collection. Each block declares when to search the destination for link targets (for the connect skill) and what labels writers may use.

Inline position for strongest commitment: `since [title](./path.md)`, `because [title](./path.md)`, `but [title](./path.md)`. Footer position with explicit label and context phrase: `- [title](./path.md) — label: context phrase`. Asymmetric labels are forward-authored; don't write a reverse edge — backlinks are computed.

### → `kb/notes/` (within this collection)

**Search:** the densest path. Most notes connect to other notes — to sharpen, ground, challenge, or generalise a claim. Search when the current note's argument touches any ongoing thread in the collection, or when a premise is asserted without being developed here.

**Labels:**

| label | kind | reader-need |
|---|---|---|
| `extends` | asymmetric | wants to see the argument developed further |
| `grounds` | asymmetric | wants to verify the premise / check the basis |
| `enables` | asymmetric | wants to check the operational prerequisite |
| `exemplifies` | asymmetric (instance → general) | wants the general claim this instance falls under |
| `mechanism` | asymmetric | wants to understand how the claim operates |
| `contradicts` | symmetric | wants to resolve a disagreement |
| `contrasts` | symmetric | wants to see the neighbouring-shape distinction |
| `defined-in` | asymmetric | reader may not know a term; target is under `kb/notes/definitions/` |

### → `kb/reference/`

**Search:** when the claim describes behaviour the commonplace system exhibits, was abstracted from a shipped-system fact, or touches a system component in an adjacent way. Reference docs are where theoretical claims touch ground in the system as built. Scan liberally — the agent filters candidates that don't connect.

**Labels:**

| label | reader-need |
|---|---|
| `evidence` | this shipped-system observation corroborates the claim |
| `derived-from` | this shipped-system fact is where the claim was abstracted from |
| `see-also` | might benefit but no specific need; use sparingly |

### → `kb/agent-memory-systems/`

**Search:** when the claim is about how external agent memory / knowledge / context-engineering systems work or should work, or when a reviewed system is a plausible counterexample, parallel, or source of abstraction. Reviews here are primary sources for deriving theoretical claims; scan broadly when the theme overlaps, the agent filters.

**Labels:**

| label | reader-need |
|---|---|
| `evidence` | this external system corroborates the claim |
| `derived-from` | this review is where the claim was abstracted from |
| `see-also` | might benefit but no specific need; use sparingly |

### → `kb/instructions/`

**Search:** uncommon. Theoretical notes typically don't cite procedures, but a scan is worth it when the claim has operational implications — a procedure may enforce it, or an adjacent instruction may exist. The primary edge is usually the inverse (`instruction → this note` via `rationale`); backlinks surface it.

**Labels:**

| label | reader-need |
|---|---|
| `see-also` | the instruction is a directly relevant companion |

**Theory-independence constraint.** The claim must stand without any single descriptive example — if the claim collapses when any one cited description is removed, it's still a description, not yet a theory.

## Types

- `note` -> `kb/types/note.md`
  Use for transferable theoretical notes.
- `structured-claim` -> `kb/notes/types/structured-claim.md`
  Use for developed arguments where explicit evidence and reasoning sections clarify the case.
- `definition` -> `kb/types/definition.md`
  Use for KB vocabulary definitions under `kb/notes/definitions/`.
- `index` -> `kb/types/index.md`
  Use for curated or generated navigation hubs.

## What does NOT belong here

- Descriptions of how a specific system works → descriptive register (`kb/reference/` or `kb/agent-memory-systems/`)
- Procedures, conventions, how-to guidance → prescriptive register (`kb/instructions/`)
- Raw captures without frontmatter → `text` type, any collection
- Work in progress → `kb/work/` (workshops)
