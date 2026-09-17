# Autonomous theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-14 in a later
> session to drop the reference to open-endedness, add the objective
> consequence, and add the Gödel machine as a boundary case.

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

Autonomy is independent of [reflection](./reflective-theory-builder.md) and
of [extension](./theory-builder.md#extension). Computational performance of
a role does not establish its reliability. The research target is
**warranted** autonomy in the sense of
[warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md):
the builder's evaluators cover the revisions it accepts with the required
confidence. Reduction of human presence alone is not the target.

## The objective

With no person inside the boundary, no change to the terminal objective is
licensed, since
[revising an improvement objective is licensed from outside it or is not improvement](../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md).
The objective may still change unlicensed, including through a conceptual
revision of its terms, which the
[objective clause](./theory-retention-policy.md#the-objective-clause) of the
policy draft treats as an objective change. Warranted extension is then bounded by
what evaluators judged against the seed objective can warrant. Whether that
bound is a closure over the seed objective and admitted evidence is
unsettled; the policy draft records the question. This paragraph's inference
from autonomy to an absence of licensed objective change also remains under
[review](./README.md#next-review-reconcile-the-definitions); it is not part of
the meaning of tentative theory. Commonplace
today escapes the question only because the operator licenses objective
changes from outside the boundary.

## Boundary cases

- **FORTE** performs its refinement procedure computationally. It is not an
  autonomous theory builder because it does not meet the base definition's
  persistence condition.
- **The Gödel machine** is autonomous: every role it performs is
  computational, and its autonomy is warranted within its proof surface. Its
  classification as a theory builder remains under review in the base
  definition; the vocabulary change does not decide it.
- **Commonplace today** is not autonomous: the operator performs diagnosis,
  admission, and successor selection for library changes, and these are
  internal roles under the role rule.
- **The research target** is an autonomous, reflective theory builder with
  the autonomy warranted, under the [fixed-model constraint](./README.md#goal).
