---
type: types/type-spec.md
name: collection-contract
description: "A collection's COLLECTION.md: the binding local contract that sets the collection's goals, quality standards and linking rules for every artifact under it"
schema: ./collection-contract.schema.yaml
---

# Collection contract

A collection contract is the `COLLECTION.md` at the root of a
[collection](../reference/definitions/collection.md). It is the one binding
local contract for every artifact in that collection
([ADR 071](../reference/adr/071-text-contract-is-part-of-the-collection-definition.md)).
Every `COLLECTION.md` declares this type, and only a `COLLECTION.md` may;
validation fails otherwise.

A contract states rules for its collection; it is not one of the collection's
artifacts. Validating a collection checks that its `COLLECTION.md` declares
this type but does not validate it as one of the artifacts, and tags never
count it as a member.

## What a contract does

A contract plays three roles. Authors read it before writing in the
collection; collection-conformance reviews judge each artifact against it
([ADR 041](../reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)).

1. **Goals.** It says what the collection is for: what kind of contribution
   belongs here, what its scope is, and where nearby content goes instead. A
   reader should be able to decide from this alone whether an artifact
   belongs in the collection.
2. **Quality standards.** It names the quality goal artifacts aim at and the
   tests for it, such as explanatory reach for theory or fidelity and economy
   for reference. It also sets the title and description conventions and any
   attribution or evidence requirements.
3. **Linking.** It defines how artifacts in the collection link out: which
   link labels they may use, to which collections, and for what reader need.
   This is usually a table under an "Outbound links" heading.

A contract may also state maintenance rules, such as how artifacts are
revised, retired or moved. Rules about the shape of one kind of artifact
belong in that kind's type spec, not here
([ADR 084](../reference/adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)).

## Authoring outbound-link rules

Organise outbound-link rules **per destination** — naming local collections by directory path (e.g. `kb/theory/` or `theory`, preserving subdirectory restrictions like `theory/definitions`) and using the reserved token `external` for targets outside the KB. For each destination, declare:

1. **Search guidance** — concrete triggers for when `cp-skill-connect` or an author should search that destination (specific enough to bound context, open enough to avoid missing adjacent finds).
2. **Authorised links.** For formal links, list the labels allowed for this source and destination and the reader need each serves (palette in [link vocabulary](../reference/link-vocabulary.md)). For `external`, a collection may also authorise inline citations by stating their permitted purpose and where they may appear. These citations need no formal label.

Unlisted destinations are unauthorized. The wildcard `any` authorizes every destination including `external`; a named `external` entry scopes external links narrowly without making the open web a connect-search surface ([ADR 059](../reference/adr/059-external-is-a-reserved-outbound-destination.md)). State the collection's inline-vs-footer convention: authorised labels govern what a footer link may be called, while footer inclusion remains a separate, selective author judgment unless the contract explicitly declares a checked completeness rule.

## Frontmatter

- `type`: `types/collection-contract.md`.
- `description` (optional): what the collection holds, for agents choosing
  where to read or write.
- `participating` (optional, tag collection only): the collections whose
  `tags:` lines count as tag membership, named relative to the KB root. The
  tag collection's contract explains it.
- `unquoted-source-limit` (optional): the most distinct tracked sources an
  artifact in the collection may cite without a verified verbatim quotation
  paired to each. Set it where the collection holds its artifacts to a
  one-pass grounding review; `commonplace-validate` then fails every artifact
  over it, whatever its type
  ([ADR 122](../reference/adr/122-collections-set-the-unquoted-source-limit.md)).
  The contract's prose states the authoring conventions that go with it; the
  [validation contract](../reference/validation-contract.md#the-unquoted-source-limit)
  describes what counts and how a source is discharged.

The type does not yet require the three roles' sections by name, because
existing contracts title them differently.
