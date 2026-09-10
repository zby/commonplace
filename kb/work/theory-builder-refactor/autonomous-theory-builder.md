# Autonomous theory builder

> **Status:** Workshop definition, 2026-09-10; renamed and revised 2026-09-10
> so that autonomy is defined over any theory builder rather than only over
> reflective ones, and so that it inherits the KB's closure and warrant terms.

An **autonomous theory builder** is a [theory builder](./theory-builder.md)
whose theory-building pathway is
[computationally closed](../../notes/methodological-and-computational-closure-track-different-changes.md):
within the declared boundary and over the assessed horizon, computation
supplies every internal theory-building role. Those roles are the ones the
boundary rule names: interpreting what a theory implies, choosing which part
to blame or revise, evaluating a candidate revision, selecting the retained
successor, and repairing the machinery.

Users remain outside the builder when they supply questions, cases, evidence,
requirements, observations, or acceptance judgments. Whether a person's
judgment is an external acceptance judgment or an internal evaluation is
decided by the role rule, not by who makes it: the judgment is internal when
the system depends on it to complete an episode of theory building. Report
each consequential role as human, computational, or joint, and declare the
seed and its construction separately from interventions during the assessed
run.

Autonomy is independent of [reflection](./reflective-theory-builder.md) and of
open-endedness. Bare autonomy is free: any role can be handed to a model. The
research target is **warranted** autonomy in the sense of
[warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md):
the builder's evaluators cover the revisions it accepts with the required
confidence. Reduction of human presence alone is not the target.

## Boundary cases

- **FORTE** is autonomous over its single run: every role it performs is
  computational. It is neither persistent, reflective, nor open-ended.
- **Commonplace today** is not autonomous: the operator performs diagnosis,
  admission, and successor selection for library changes, and these are
  internal roles under the role rule.
- **The research target** is an autonomous, reflective, open-ended theory
  builder, with the autonomy warranted.
