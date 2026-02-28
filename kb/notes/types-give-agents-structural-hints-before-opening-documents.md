---
description: Types and descriptions let agents make routing decisions without loading full documents — the type says what operations a document affords, the description filters among instances of that type
type: note
areas: [document-system]
status: seedling
---

# Types give agents structural hints before opening documents

Agents are stateless — they start fresh every session with no memory of what they've read before. Context is finite and expensive. Without types, an agent must either load everything (wasteful) or guess what's relevant (error-prone).

Types solve this by giving agents structural hints *before* opening a document. A `spec` tells an agent it can implement from this. A `structured-claim` tells it there's a developed argument with evidence. An `index` tells it this is a navigation hub. These hints enable informed routing decisions: the agent reads a type and description, then decides whether to load the full document.

This is why [description is the most important field](../../types/note.md) — it's a retrieval filter, not a summary. The type tells the agent *what kind of thing* a document is; the description tells it *which instance* among documents of that kind is relevant to the current task. Together they let an agent narrow from hundreds of files to the few it needs without opening any of them.

The [verifiability criterion](./document-types-should-be-verifiable.md) is what makes this work: types must assert structural properties, not subject matter. "This is a design note" tells an agent nothing it can act on — every note in a design KB is about design. "This has Evidence and Reasoning sections" tells the agent it can extract a citable argument. The structural promise is what makes the routing decision informed rather than blind.

But these structural hints only work if the metadata exists reliably. That's the role of [type-system enforcement](./type-system-enforces-metadata-that-navigation-depends-on.md) — descriptions don't appear spontaneously; the type system is what makes them exist.

---

Relevant Notes:
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — foundation: the verifiability principle that makes type-based routing trustworthy
- [type-system-enforces-metadata-that-navigation-depends-on](./type-system-enforces-metadata-that-navigation-depends-on.md) — enables: descriptions exist because the type system requires them; without enforcement, routing data degrades
- [note base type](../../types/note.md) — defines description as the most important field — the retrieval filter this note's routing argument depends on
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview of all type system roles; this note develops the navigation role

Topics:
- [document-system](./document-system.md)
