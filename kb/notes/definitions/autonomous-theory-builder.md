---
description: "Definition — an autonomous theory builder performs every internal theory-building role computationally within a declared boundary; users still supply tasks and acceptance, and autonomy settles neither reliability nor objective governance"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Autonomous theory builder

An **autonomous theory builder** is a [theory builder](./theory-builder.md)
whose theory-building pathway is
[computationally closed](../methodological-and-computational-closure-track-different-changes.md):
within the declared boundary and over the assessed horizon, computation
supplies every internal theory-building role. Those roles are the ones the
boundary rule names: constructing a first theory, interpreting what a
theory implies, choosing which part to blame or revise, producing a
candidate revision, evaluating a candidate theory, selecting the theory to
retain, and extending and repairing the machinery. The KB needs the term
because autonomy has to be measurable without pretending that an
autonomous learner lives in an environment without people.

Users remain outside the builder when they supply questions, cases,
evidence, requirements, observations, or acceptance judgments. Whether a
person's judgment is an external acceptance judgment or an internal
evaluation is decided by the role rule, not by who makes it: evaluating a
candidate theory or selecting its successor is internal, and judging the
resulting product against the external task contract is not. An assessment
reports each consequential role as human, computational, or joint, and
declares the seed and its construction separately from interventions during
the assessed run.

## Scope

- **Independent of reflection and of extension.** See
  [reflective theory builder](./reflective-theory-builder.md) and
  [extension](./theory-builder.md#extension).
- **Not reliability.** Computational performance of a role does not
  establish its reliability. Warranted autonomy, in the sense of
  [warranted autonomy is bounded by oracle domain](../warranted-autonomy-is-bounded-by-oracle-domain.md),
  is the condition that the builder's evaluators cover the revisions it
  accepts with the required confidence; it is a separate assessment.
- **Not objective governance.** Autonomy does not determine who may change
  the objective or what would warrant that change. The declared evidence
  interface can include externally supplied acceptance judgments while the
  builder remains autonomous; what licenses an objective change is the
  second obligation in
  [a claim without external assessment carries three obligations](../a-claim-without-external-assessment-carries-three-obligations.md).

## Exclusions

- A builder that depends on a person for diagnosis, admission, or successor
  selection of its theories, however small the person's share.
- A computational procedure that is not a theory builder, such as a
  refinement algorithm run once over supplied cases; autonomy qualifies a
  builder, it does not create one.
- Reduction of human presence as such. The target the term serves is
  warranted autonomy, not fewer people.

## Misuse Cases

- Calling a builder autonomous because users supply only tasks, when a
  person still evaluates or selects its theories.
- Calling a builder non-autonomous because people judge its products; that
  is the external acceptance role.
- Inferring from autonomy that the objective cannot change, or that its
  change cannot be licensed.
- Reading a proof obligation on rewrites as reliability beyond what the
  proof covers.

## Boundary cases

- **FORTE** performs its refinement computationally but is not persistent,
  so it is not an autonomous theory builder.
- **Commonplace today** is not autonomous: the operator performs diagnosis,
  admission, and successor selection for library changes, and these are
  internal roles under the role rule.
- **The Gödel machine** performs every role it has computationally, with
  warrant within its proof surface; whether it is a theory builder is
  assessed separately and stays open.

---

Relevant Notes:

- [Theory builder](./theory-builder.md) — defined-in: the system this condition qualifies and the roles the boundary rule names
- [Methodological and computational closure track different changes](../methodological-and-computational-closure-track-different-changes.md) — grounds: computational closure of the pathway
- [Warranted autonomy is bounded by oracle domain](../warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the reliability condition autonomy does not supply
- [Reflective theory builder](./reflective-theory-builder.md) — contrasts: the independent condition on whether changes pass through a self-theory
- [A claim without external assessment carries three obligations](../a-claim-without-external-assessment-carries-three-obligations.md) — extends: objective governance as an obligation separate from autonomy
