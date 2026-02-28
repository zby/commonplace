---
description: Descriptions don't appear spontaneously — they exist because the note base type requires them; without enforcement, metadata degrades and navigation collapses to opening every document
type: note
areas: [document-system]
status: seedling
---

# Type system enforces metadata that navigation depends on

The [navigation argument](./types-give-agents-structural-hints-before-opening-documents.md) assumes documents *have* descriptions. But descriptions don't appear spontaneously — the type system is what makes them exist.

The [note base type](../../types/note.md) defines `description` as the only required field. Any document that crosses from [text](../../types/text.md) to `note` must acquire a description, and validation can check that it's present, non-empty, and discriminating. This is the enforcement mechanism: the type creates the obligation, and `/validate` checks compliance.

Without this enforcement, a knowledge base degrades quickly. Agents writing notes under time pressure skip metadata. Human authors forget. The result is a collection of documents that can only be navigated by opening each one — which defeats the point of having a structured KB.

The type system's role here is not routing (that's the [navigation claim](./types-give-agents-structural-hints-before-opening-documents.md)) but **ensuring the routing data exists at all**. It's the difference between a library with a catalogue and a library where some books have catalogue cards and some don't. The catalogue is only useful if it's comprehensive; the type system is the mechanism that makes it comprehensive.

---

Relevant Notes:
- [types-give-agents-structural-hints-before-opening-documents](./types-give-agents-structural-hints-before-opening-documents.md) — depends on: the navigation argument that assumes descriptions exist; this note explains why they do
- [note base type](../../types/note.md) — defines description as the only required field — the enforcement mechanism this note describes
- [text root type](../../types/text.md) — the boundary: crossing from text to note triggers the description requirement
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview of all type system roles; this note develops the enforcement role

Topics:
- [document-system](./document-system.md)
