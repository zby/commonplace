---
description: "Accepted decision that a collection contract's unquoted-source-limit field, not a list of type paths in the validator, decides which artifacts the ADR 082 grounding bound applies to; Notes and Articles set it at five"
type: reference/types/adr.md
tags: []
status: accepted
---

# 122-Collections set the unquoted-source limit

**Status:** accepted
**Date:** 2026-10-23
**Amends:** [082-Grounding is bounded on the artifact by unquoted sources](./082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md), decision 2

## Context

[ADR 082](./082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md)
bounds an artifact at five tracked sources cited without a verified verbatim
quotation, so that its grounding review fits one pass. It enforced the bound as
a validator type rule registered for three type paths: `types/note.md`,
`notes/types/structured-claim.md` and `articles/types/article.md`.

What the bound protects is a collection's review standard, not a property of a
kind of artifact. A type list follows that standard only by accident:

- An artifact in `kb/notes/` escaped the bound by using another type. All 26
  definitions and both theory proposals were unchecked.
- An artifact held to no grounding review was bound because it used the note
  type: 29 reference pages, 14 agentic-systems pages and 13 workshop notes.
- A type relocation silently drops the rule unless someone remembers its
  registration. Renaming `kb/notes/` to `kb/theory/` would have done so for
  `structured-claim`.

Applying the bound to every artifact is also wrong. It would newly fail three
source ingests, which link other ingests as related reading, and four
plain-text reports and workshop files. Nobody grounding-reviews either kind.

## Decision

1. **The collection contract declares the bound.** The
   [collection-contract type](../../types/collection-contract.md) gains an
   optional integer field, `unquoted-source-limit`. Where a contract sets it,
   `commonplace-validate` applies the ADR 082 count to every artifact in the
   collection, whatever its type, plain text included, and fails an artifact
   over the limit. The nearest contract governs. A collection whose contract
   omits the field is not bound.
2. **Notes and Articles set it at five.** Five remains ADR 082's convention,
   not a measured capacity. Each contract states its authoring conventions for
   the bound in its own prose, as before.
3. **The type registrations are removed.** No type path selects the rule.
   ADR 082's counting rules are unchanged: which sources count, the
   `(snapshot required)` marker and the `## Quotes` confinement.

The operativity path: `commonplace-validate` reads the field from the governing
contract's frontmatter on every validation run and fails over-limit artifacts.
The pinned-artifact adapter reads the same field from the contract snapshot it
already requires. Authors read the field and its prose convention in the
contract before writing.

## Considered alternatives

**Keep the exact type-path registrations** and update them when types move.
The hardwired-collections workshop's Gate E had adopted this. It lost because
the registrations select the wrong population today, as Context shows, not only
because they are fragile.

**The type spec declares the bound**, for example `grounding-bound: true` read
from the resolved spec. This follows [ADR 084](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)
and survives type moves. But every type a collection uses must opt in
separately: note, definition, structured-claim, theory proposal, article. A
note-typed scratch file in `kb/work/` would stay bound. The bound concerns how
a collection is reviewed, which ADR 084 leaves to the collection contract.

**Inherit through schema composition**: bind any type whose schema extends the
note schema. It needs no field, but it ties a review-economy rule to structural
inheritance, which is implicit and surprising to an author.

**Apply it to every artifact, or wherever the grounding gate applies.** The gate
has no type requirement, so the two are the same. Both lost to the seven new
failures in ingests and text reports named in Context.

**A boolean field with the number in code.** Rejected. An integer lets a
consuming KB choose its own bound per collection without a code change.

Free choices resolved: the operator chose Notes and Articles. Reference,
Agentic Systems and the workshop layer stay unbound. The frozen Agent Memory
Systems reviews stay unbound too.

## Consequences

In `kb/notes/`, definitions and theory proposals are now checked; none is over
the limit. The rename to `kb/theory/` carries the bound with the contract and
needs no validator change. A consuming KB enables the bound per collection by
editing its contract, not code.

The note-typed pages outside Notes and Articles lose the check. None was over
the limit when the check was removed, and their collections never promised a
one-pass grounding review. A collection that adopts such a review should set
the field when it adopts it.

Where the decision stops applying: it moves the bound's applicability, not its
counting rules or its value. A nested collection inside a bound collection is
governed by its own contract and is unbound unless that contract sets the field.
The limit covers tracked ingests under `kb/sources/` only, as ADR 082 does.

---

Relevant Notes:

- [082-Grounding is bounded on the artifact by unquoted sources](./082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md) — amends: replaces decision 2's type-rule enforcement with a contract field
- [Collection contract type](../../types/collection-contract.md) — implemented-by: declares the `unquoted-source-limit` field and its quality-standards role
- [084-Kind rules live in type specs and operations in instructions](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) — see-also: why a collection-level review standard belongs in the contract rather than a type spec
- [048-Imperative type rules dispatch by canonical path](./048-imperative-type-rules-dispatch-by-canonical-path.md) — see-also: the dispatch this rule leaves; other type rules keep it
