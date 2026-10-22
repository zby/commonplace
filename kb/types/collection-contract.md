---
type: types/type-spec.md
name: collection-contract
description: "A collection's COLLECTION.md when it carries frontmatter: the binding local text contract, with optional control fields such as the tag collection's participating list"
schema: ./collection-contract.schema.yaml
---

# Collection contract

A collection contract is a `COLLECTION.md`: the one binding local contract of
its [collection](../reference/definitions/collection.md), supplying the text
contract for every artifact under it ([ADR 071](../reference/adr/071-text-contract-is-part-of-the-collection-definition.md)).
Every authored contract declares this type, and the scaffold templates do too.
A contract without frontmatter, such as an older installed KB's or an exact
copy inside a captured bundle, still validates as [text](./text.md).

The contract is not collection content: collection-scoped validation and tag
membership leave it out, and conformance reviews read it as the gate rather
than judging it as an artifact. Choose this type for a `COLLECTION.md` and for
nothing else.

## Frontmatter

- `type`: `types/collection-contract.md`.
- `description` (optional): a retrieval description of what the collection
  holds.
- `participating` (optional, tag collection only): the collections whose
  `tags:` lines are membership claims, by name under the KB root. The tag
  collection's contract explains its semantics.

## Body

The body is the text contract: purpose and scope, quality goal, title and
description conventions, lifecycle, and outbound-link rules, as the
[collection definition](../reference/definitions/collection.md#text-contract)
lists them. This type does not yet require those sections by name, because
existing contracts title them differently.
