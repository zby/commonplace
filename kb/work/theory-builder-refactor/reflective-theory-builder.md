# Reflective theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-10 to compose
> existing terms instead of restating them.

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

Work on external theories is both useful work and a test of the current
machinery. When that work exposes a machinery limitation, the builder may
revise its self-theory, change the implicated machinery, and test the change
by returning to external theory-building work. Reflection therefore serves
external theory-building competence; it is not a requirement to build
theories only about the builder itself.

The condition is independent of [autonomy](./autonomous-theory-builder.md)
and of open-endedness. A reflective builder may depend on a person for the
diagnosis or the machinery change, and may hold family-fixed machinery.

## Boundary cases

- **FORTE** is not reflective: its theory is external and its machinery is
  not represented in any theory it refines.
- **Commonplace today**, with the operator inside the boundary, is reflective:
  the KB's methodology notes, type specs, and ADRs are a theory of its own
  theory-building machinery, and revisions of them change the validators,
  skills, and contracts that build later theories. The evidence for the
  two-way connection is in
  [Commonplace as a reflective system](../../notes/evidence/commonplace-as-a-reflective-system.md).
- **The research target** is reflective by stipulation.
