# Tentative theory

> **Status:** Workshop vocabulary, 2026-09-17. The operator selected Popper's
> established term. The theory's structure remains in the library's
> theory-refinement definition; retention and use are separate policy
> questions. This entry is not yet promoted into the library.

A **tentative theory** is a theory in the
[theory-refinement sense](../../notes/definitions/theory-refinement.md#what-the-loop-requires-of-a-theory),
put forward as a solution to a problem and held open to criticism and revision
through attempted error elimination.

The term is Popper's: `TT` names the tentative theory in his
`P1 → TT → EE → P2` schema, between an initial problem and attempted error
elimination that produces further problems
([1966 essay, retained schema passage](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
In *Conjectures and Refutations*, he describes proposing a theory as a
solution, accepting it provisionally if at all, and criticizing and testing
it. He also says that theories remain tentative even when we no longer feel
able to doubt them
([Chapters 1 and 15, retained passages](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
Tentativeness is therefore not a temporary stage that ends when a theory
becomes established as true.

## What the workshop adds

The structural requirements come from theory refinement: consequences a
case can contradict, parts available as candidate repair locations, and
parts editable separately. Applying Popper's term to that particular
refinement object is the workshop's use of his vocabulary. It does not make
our machinery or acceptance rules part of Popper's definition.

A failed prediction may implicate a combination of premises without uniquely
identifying the faulty one; this does not mean that fault localization is
always impossible. Popper states both qualifications in
[Chapter 10, section XVI](../../sources/popper-conjectures-and-refutations.ingest.md#quotes).
They agree with the existing theory-refinement definition's distinction
between candidate repair locations and an identified fault.

In an [externally tested theory builder](./externally-tested-theory-builder.md),
a request may supply the initial problem, testing and criticism may perform
error elimination, and a failure may expose the next problem. This is a local
application of the schema. Error elimination includes diagnosis and revision;
it is not supplied by the external failure signal alone.

## Retention and use

The term does not specify how much support permits retention, experimental
use, routine reliance, or codification. A corroborated theory can remain
tentative; changing its representational form does not establish its truth.
The builder must state its policy for those uses. The
[theory-retention policy draft](./theory-retention-policy.md) preserves the
workshop's proposed obligations and unresolved questions separately from
this vocabulary entry.
