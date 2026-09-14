# Autonomous theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-14 to cover
> first-theory construction and align the boundary cases with persistence.

An **autonomous theory builder** is a [theory builder](./theory-builder.md)
whose theory-building pathway is
[computationally closed](../../notes/methodological-and-computational-closure-track-different-changes.md):
within the declared boundary and over the assessed horizon, computation
supplies every internal theory-building role. Those roles are the ones the
boundary rule names: constructing a first theory, interpreting what a theory
implies, choosing which part to blame or revise, producing a candidate
revision, evaluating a candidate theory, selecting the theory to retain, and
extending and repairing the machinery.

Users remain outside the builder when they supply questions, cases, evidence,
requirements, observations, or acceptance judgments. Whether a person's
judgment is an external acceptance judgment or an internal evaluation is
decided by the role rule, not by who makes it: the judgment is internal when
the system depends on it to complete an episode of theory building. Report
each consequential role as human, computational, or joint, and declare the
seed and its construction separately from interventions during the assessed
run.

Autonomy is independent of [reflection](./reflective-theory-builder.md) and of
[open-endedness](./theory-builder.md#open-ended-theory-builder). Computational
performance of a role does not establish its reliability. The research target
is **warranted** autonomy in the sense of
[warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md):
the builder's evaluators cover the revisions it accepts with the required
confidence. Reduction of human presence alone is not the target.

## Boundary cases

- **FORTE** performs its refinement procedure computationally. It is not an
  autonomous theory builder because it does not meet the base definition's
  persistence condition.
- **Commonplace today** is not autonomous: the operator performs diagnosis,
  admission, and successor selection for library changes, and these are
  internal roles under the role rule.
- **The research target** is an autonomous, reflective, open-ended theory
  builder, with the autonomy warranted.
