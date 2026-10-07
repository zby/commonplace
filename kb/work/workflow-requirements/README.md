# Workshop: redesign the analysis machinery

- **Posed:** 2026-10-07, by the operator's direction, after the fixed-snapshot
  proposal showed that the current engine's model had grown past its problem.
- **Closes when:** the operator has accepted or amended each requirement in
  [requirements](./requirements.md) and a design proposal has been derived
  from the accepted set. Implementing that design for the analysis
  workflow also needs the set type to declare the relations its prose now
  states; see the type needs in [the mapping](./analysis-workflow-as-job-set.md).

## Goal

Redesign the machinery behind the analysis workflow so that it is easier to
work with and robust: correct for the current needs of
[`analyse-agentic-system`](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md),
and expandable along useful lines without growing a special case per need.

## First approach

Redefine the machinery around one compact abstraction that other workflows
could reuse later: a directory declares its jobs and their file
dependencies, one command advances the directory, and a single relative
judgment record, acceptance or refusal of a version against named inputs,
carries acceptance, correction and publication. The abstraction is stated
as requirements in [requirements](./requirements.md); the analysis workflow
is its first consumer and the test of whether it is enough. That test is
[the analysis workflow as a job set](./analysis-workflow-as-job-set.md),
which maps the current workflow onto the spec and reports what the spec
lacks, without changing it. [Scenarios](./scenarios.md) walks the
situations the spec must cover and names those it does not yet.

## API proposal

[API design](./api-design.md) and the [Python sketch](./api_sketch.py) propose
only the version-1 public boundary. They retain pinning and verdict provenance
internally and explicitly defer general operator judgments and multiple semantic
judges. These are proposed changes to the requirements, not adopted rules.

## Related

- [Code-scheduled workflows](../../reference/proposals/code-scheduled-workflows.md)
  and its [workshop](../code-scheduled-workflows/README.md): the current
  engine's design and build.
- [Record acceptance reads and judged versions](../../reference/proposals/record-acceptance-reads-and-judged-versions.md):
  the replay defect that prompted this workshop, and the repair proposed
  within the current engine.
