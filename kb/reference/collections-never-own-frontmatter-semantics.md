---
description: "Why the collection/type split is asymmetric: a type spec fully owns frontmatter semantics, COLLECTION.md owns only text-level features, plus the sanctioned moves when a field would vary by collection"
type: kb/types/note.md
traits: []
tags: []
---

# The collection–type split is asymmetric: collections never own frontmatter semantics

Collections and types look like symmetric complements — two contract surfaces that together specify an artifact — and design work has repeatedly asked which properties belong on which side. The split is not symmetric, and the asymmetry is deliberate. A type-spec doc fully and self-containedly determines what an artifact's frontmatter *means*: which fields exist, what values they admit, and the truth conditions of each — validator-checkable, interpretable without reading anything else. A [`COLLECTION.md`](./collections-and-types.md) owns only text-level contract features: the [text contract](../notes/definitions/text-contract.md) or register, the quality goal, title and description conventions, and the outbound-link policy. Collections never define, redefine, or select frontmatter-field semantics.

## Why the boundary holds this way

The argument is self-containment. If a collection could reinterpret what a schema field means — same committed value, different truth conditions per directory — or select which fields or axes apply at all, the type would stop being self-contained. Three costs follow directly:

- Reading any artifact's frontmatter would require joining two documents — the type spec *and* the local `COLLECTION.md` — instead of one.
- Moving a file between collections would silently change what its frontmatter asserts, even with every byte of the file unchanged.
- Validators would check syntax whose meaning they no longer know: the schema keyword would be intact while its semantics floated free in prose the validator does not read.

Keeping frontmatter semantics wholly inside the type spec is what makes a committed value mean one thing everywhere, checkable by code that reads only the schema.

## The pressure case that proved it

The epistack casework produced two ideas that would each have breached this boundary. The retired proposal [assertion force separate from lifecycle status](./proposals/assertion-force-separate-from-lifecycle-status.md) had each collection's `COLLECTION.md` redefine what `status: current` asserts — endorsement here, attribution accuracy there — the same committed value with per-directory truth conditions. A sharper idea from the extensible-controlled-vocabularies workshop went further: let the contract declare which status *axes* apply at all, so a collection could drop the endorsement axis rather than re-value it. Both put frontmatter meaning under collection control.

[ADR 044](./adr/044-user-verification-replaces-global-note-status.md) resolved the fork by deleting the global `status` field outright rather than making its semantics collection-relative — replacing it with an optional `user-verified` field whose meaning is fixed and type-owned. The boundary held by removing the field, not by relativizing it.

## The sanctioned alternatives

When a field's meaning would otherwise have to vary by collection, the moves that preserve the boundary are:

1. **Delete the global field.** ADR 044 for `status`: if no single meaning survives across collections, the field carries no coherent global semantics and is removed.
2. **Carry the distinction in placement and prose, with no field at all.** [ADR 017](./adr/017-collection-md-is-the-register-convention-boundary.md) for register: which register applies is encoded by which collection a file lives in and stated in that `COLLECTION.md`, never as a frontmatter field whose meaning a collection sets.
3. **Push it into a collection-local type whose spec owns the field with fixed meaning.** A distinction that only exists under one contract becomes a field on a collection-local type (for example, a casebook-local claim type), where the type spec still fully determines what the field means.

Extending a field's *value set* while keeping each value's meaning fixed does **not** breach the boundary. The extensible-controlled-vocabularies direction for `source_type` — adding new enum values that each mean one thing everywhere — is fine; adding values is a different operation from relativizing meaning. The boundary forbids only the second.

## Why this is worth stating

The two epistack ideas are instances of a recurring shape: a field whose meaning feels like it should follow the collection. Expect more of them. This note is the guard — when a design proposal wants a collection to reinterpret or select frontmatter semantics, the answer is one of the three sanctioned moves above, not a collection-relative type.

---

Relevant Notes:

- [Collections and types](./collections-and-types.md) — part-of: the composition model this sharpens; states the two-surface split that this note shows is asymmetric
- [ADR 044: user verification replaces global note status](./adr/044-user-verification-replaces-global-note-status.md) — implemented-by: the decision that held the boundary by deleting the field rather than relativizing its meaning
- [ADR 017: COLLECTION.md is the register convention boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — implemented-by: the precedent for carrying a per-collection distinction in placement and prose with no frontmatter field
- [Assertion force separate from lifecycle status](./proposals/assertion-force-separate-from-lifecycle-status.md) — see-also: the retired proposal whose per-collection meaning-redefinition of `status` this boundary rules out
- [ADR 042: register becomes a default profile under open-ended text contracts](./adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — see-also: the sibling open-but-guarded value-set extension that stays on the text-contract side of this boundary
