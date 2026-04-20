# Writing conventions for kb/notes/ (theoretical register)

## Register

This collection operates in the **theoretical register**. Documents here make transferable claims about what is true — mechanisms, principles, and general arguments that should hold across systems, not just in this one.

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

When linking FROM this collection:

| To register | Appropriate relationships | Notes |
|---|---|---|
| Theoretical (same register) | since / because / contradicts / extends / qualifies | The claim-traversal graph. These are the argumentative links that make traversal-as-reasoning work. |
| Descriptive (reference, agent-memory-systems) | evidence / derived-from / exemplifies | Theories cite descriptions as observations and evidence. The theory must stand without any single description — if it can't, it's still a description, not yet a theory. |
| Prescriptive (instructions) | evidence (rare) | Theories rarely need to cite procedures. When they do, it's usually to note that a practice exists, not to depend on it. |

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
