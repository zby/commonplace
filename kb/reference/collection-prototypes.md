---
description: "Catalogue of optional Commonplace collection prototypes: creation-time contract text that may be copied and then becomes an independently owned COLLECTION.md"
type: ../types/note.md
tags: []
---

# Collection prototypes

A **collection prototype** is optional creation-time text for a new
`COLLECTION.md`. It supplies a worked starting contract that a project may copy
and adapt instead of drafting every clause from scratch.

Copying ends the relationship. The destination project's `COLLECTION.md` is the
only binding contract for its collection, and that project owns and maintains
it. Commonplace does not synchronize the copy, apply later prototype changes to
it, or treat the collection as conforming to the prototype. A prototype update
therefore affects only future copies.

This differs from a [text contract](../notes/definitions/text-contract.md),
which is the current, binding declaration in a collection's own
`COLLECTION.md`. Writing, connection, conformance review, and validation consume
the local contract; they do not resolve a prototype or inherit rules from this
catalogue.

## Shipped prototypes

`commonplace-init` uses three prototypes when it creates a project's standard
collections. Their source files are package data under
`src/commonplace/_data/templates/`:

| Prototype | Source file | Starting purpose |
|---|---|---|
| Notes | `user-notes-COLLECTION.md` | Claims, mechanisms, definitions, and synthesis used to reason about the project's domain |
| Reference | `user-reference-COLLECTION.md` | Faithful, economical accounts of the system the project ships |
| Instructions | `user-instructions-COLLECTION.md` | Executable procedures, skills, and operational rules |

Each installed contract tells the maintainer to replace its placeholders and
state the collection's own purpose, scope, quality goal, conventions, link
rules, and type eligibility. Existing destination files are preserved rather
than refreshed from the prototype.

## Experimental prototypes

### Dialectical / evidential

`user-dialectical-evidential-COLLECTION.md` is an opt-in prototype for a
collection that maps a live, sourced disagreement without adjudicating it. It
requires every substantive proposition to name an asserter and carry a
source-span citation with a prose locator and grounding marker. Its quality
goal is faithful representation of the state of contestation.

The file carries an **experimental collection prototype** banner. One worked
case established that the contract is usable, but independently maintained
collections have not tested it. `commonplace-init` does not install it
automatically. A maintainer who deliberately copies it must replace its paths,
link rules, and type-eligibility placeholder, then owns the resulting contract
without any continuing prototype relationship.

## What is not a prototype

`kb/articles/COLLECTION.md` is a complete local editorial contract, not a
shared prototype. It has one realization and no present creation-time
consumer. Keeping its conventions local avoids advertising reuse that the
framework neither supplies nor maintains. A future reusable article starting
contract should be added only when a concrete collection-creation need exists.

Ordinary collection contracts also need not begin from a prototype. A
maintainer may write a complete local contract directly whenever none of the
available starting points fits.

---

Relevant Notes:

- [Text contract](../notes/definitions/text-contract.md) — defined-in: distinguishes the binding local declaration from optional creation-time material
- [ADR 069: Collection contract bundles become one-time prototypes](./adr/069-collection-contract-bundles-become-one-time-prototypes.md) — evidenced-by: records the clone-only semantics and retirement of text-contract profiles
