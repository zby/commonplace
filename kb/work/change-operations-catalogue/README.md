# Which operations change Commonplace, and what must each read first?

## Governing question

[ADR 074](../../reference/adr/074-git-is-the-change-history-layer.md) fixed the
placement rule for `kb/reference/`: a passage earns its place by naming the
operation of changing the system that must read it before acting. That rule can
only be applied per passage until the operations themselves are listed. This
workshop builds that list and uses it in both directions:

- **operation → premises → home.** For each way the system gets changed, what
  must the actor know before acting, and where does that currently live
  (reference, instruction, type spec, code site, ADR, git, nowhere)?
- **reference artifact → operation.** Which operation reads each
  `kb/reference/` artifact? An artifact that traces to none is a candidate for
  git, ADR context, or retirement — or evidence that the list is missing an
  operation.

## Maturity, stated so it is not misread

The catalogue is a **working list grown by observation**. An operation enters
it only when an observed instance — an ADR, a commit, or a recorded episode —
shows the system being changed that way. It carries no completeness mark and
will not until a checkable one exists ([a derived copy of recomputable truth
must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)).
Consequences for a reader:

- An operation missing from the list is not evidence that it does not exist.
- An empty or thin premises cell is not a licence to act without searching; it
  records that nobody has yet written down what that operation needs.
- The reference→operation audit is a first pass by one session. Its "traces to
  no operation" flags are questions, not dispositions.

Nothing in the library links here. If a later session wants agents to consult
the list at change time, that is a routing decision for
[adr-routing](../adr-routing/README.md) and the wiring question in
[self-improvement-cluster-operationalization](../self-improvement-cluster-operationalization/README.md),
which both consume this list rather than own it.

## Files

- [catalogue.md](./catalogue.md) — the operations, each with observed
  instances, premises, current homes, and gaps; followed by the first-pass
  reference audit.

## What closes this workshop

Both audits have been run against the current `kb/reference/` listing and acted
on: each reference artifact either traces to a named operation or has been
moved, folded, or retired under `retire-artifact.md`; each operation's premises
resolve to a named home or the gap is recorded as a proposal. The catalogue
then either promotes to `kb/reference/` under a stated maintenance rule (how an
operation is admitted, how the list is kept honest without a completeness
mark) or is judged not worth keeping as a standing artifact, with the reason
written down. Either outcome is recorded as an ADR.
