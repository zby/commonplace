# Reflective theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-14 in a later
> session to make the self-theory a fallible theory read by the interpreter,
> separate reflection from extension, and add the Gödel machine as a
> boundary case.

A **reflective theory builder** is a [theory builder](./theory-builder.md) that
performs [reflective theory refinement](../../notes/definitions/theory-refinement.md#departures)
on a theory of its own
[behavior-determining organization](../../notes/definitions/behavior-determining-organization.md),
where the organization in question is the machinery that determines how its
theories are built, tested, and revised. The self-theory must be a causally
connected self-representation in the sense of
[reflective system](../../notes/definitions/reflective-system.md): changes in
the machinery update the theory, and revisions of the theory can change the
machinery. A builder that holds a description of its machinery and consults it
without that two-way connection is not reflective in this sense.

The self-theory is a [fallible theory](./fallible-theory.md). The
[interpreter](./resource-bounded-ideal-interpreter.md) reads its claims about
the machinery faithfully, including claims about the interpreter itself, and
those claims are decided by evidence, not by being read. A self-theory's own
acceptance of a machinery change does not make the change warranted.

Work on external theories is both useful work and a test of the current
machinery. When that work exposes a machinery limitation, the builder may
revise its self-theory, change the implicated machinery, and test the change
by returning to external theory-building work. Reflection therefore serves
external theory-building competence; it is not a requirement to build
theories only about the builder itself.

The condition is independent of [autonomy](./autonomous-theory-builder.md):
a reflective builder may depend on a person for diagnosis or machinery
changes. It is also independent of
[extension](./theory-builder.md#extension). Reflection concerns whether
machinery changes pass through a causally connected self-theory; extension
concerns whether capability-adding changes happen and are retained. A builder
that refines a self-theory but only retunes values within its existing
capabilities is reflective and extends nothing. A builder whose machinery is
extended with no retained account of why is extended and not reflective.

## Boundary cases

- **FORTE** is not reflective: its theory is external and its machinery is
  not represented in any theory it refines.
- **The Gödel machine** is a reflective system, since its axioms describe its
  own software and its rewrites are causally connected to them, but it is not
  a reflective theory builder. Its self-representation is a premise of every
  rewrite and a candidate of none: it is never revised against evidence, so
  there is no reflective theory refinement.
- **Commonplace today**, with the operator inside the boundary, is reflective:
  the KB's methodology notes, type specs, and ADRs are a theory of its own
  theory-building machinery, and revisions of them change the validators,
  skills, and contracts that build later theories. The evidence for the
  two-way connection is in
  [Commonplace as a reflective system](../../notes/evidence/commonplace-as-a-reflective-system.md).
- **The research target** is reflective by stipulation.
