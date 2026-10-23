---
description: "Two audited Commonplace authority paths kept the same consumer, channel and force while the cohort or trigger they act on changed, so a behavioral-authority record of those three components cannot by itself say which use it describes"
type: types/note.md
traits: [title-as-claim]
tags: [artifact-analysis]
---

# Consumer, channel and force can stay fixed while the governed use changes

A [behavioral-authority](../definitions/behavioral-authority.md) record names
who consumes an artifact, through which channel, and with what force. That
triple can stay the same while the use it governs changes. Two paths in a
2026-08-04 audit of Commonplace show it:

- **A review gate scoped by trait.** The explanatory-reach gate is read by a
  reviewer, through the review channel, as an audit trigger. Its
  `requires_trait: title-as-claim` line decides whether it acts on every note
  or only on the cohort with that trait. Changing the line changes which
  artifacts the gate judges. It does not change the consumer, the channel or
  the force.
- **A validator rule scoped by type and trigger.** The tag-README completeness
  rule is read by the validator, through validation, with fail force. When it
  acts depends on three more things: the artifact's resolved type, which
  marked tag heads a change affects, and whether someone invoked validation.

In both cases, a record holding only consumer, channel and force fits several
different paths. To pick out one, it also needs the path's **applicability**:
the cohort, aspect or operation that receives the force, and the condition
under which the force acts. This holds for any system whose rules carry their
own scope, such as gates with trait filters or validators keyed to type. It
does not depend on how Commonplace chose to scope its rules.

The same audit kept three neighbouring questions outside the record:

- **Admission:** whether the actor or decision was entitled to give this
  content force.
- **Realization:** whether a request reached the consumer it named.
- **Dependency closure:** which derived artifacts must change with a revised
  one.

A path can have force without legitimate admission, or a legitimate request
that is never realized. It can also revise one artifact while dependent
surfaces go stale. Folding these into behavioral authority would let an
addressability finding pass as one about warrant or installation.

## Scope

- Two witnessed cases show that the triple can under-identify a path. They do
  not show how often it does, or that applicability is the only missing
  dimension.
- Whether applicability becomes a fourth component or a required qualifier is
  left to the
  [behavioral-authority decomposition proposal](../proposals/revise-behavioral-authority-decomposition.md).

---

Relevant Notes:

- [Behavioral authority](../definitions/behavioral-authority.md) — defined-in: the consumer, channel and force record whose identification limit this shows
- [Six Commonplace paths establish broad addressability, not completeness](../../reports/retained/six-commonplace-paths-establish-broad-addressability-not-completeness.md) — abstracted-from: the audit whose explanatory-reach and tag-README cases supply both witnesses
- [Axes of artifact analysis](../axes-of-artifact-analysis.md) — extends: scope is already recorded there as consumption-path metadata outside the triple
- [A consumption channel delivers force without the history that earned it](../a-consumption-channel-delivers-force-without-the-history-that.md) — contrasts: the admission question kept outside the record
