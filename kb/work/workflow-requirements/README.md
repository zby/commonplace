# Workshop: redesign the analysis machinery

- **Posed:** 2026-10-07, by the operator's direction, after the fixed-snapshot
  proposal showed that the current engine's model had grown past its problem.
- **Closes when:** the operator has accepted or amended each requirement in
  [requirements](./requirements.md) and a design proposal has been derived
  from the accepted set. Implementing that design for the analysis
  workflow also needs the artifact type to declare the relations its prose now
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
[the analysis workflow as a plan](./analysis-workflow-as-job-set.md),
which maps the current workflow onto the spec and reports what the spec
lacks, without changing it. [Scenarios](./scenarios.md) walks the
situations the spec must cover and names those it does not yet.

## Future direction: a movable boundary

Not a requirement yet, recorded so the design does not close it off. The
coordinator, the agent that calls the command and runs the workers (see
the [glossary](./glossary.md)), should be able to take over more of the
run later, in the
sense of [relaxing](../../notes/agentic-systems-interpret-underspecified-instructions.md):
a code job's interpretation moved to the agent when the code's one
projection becomes the bottleneck, and moved back when a pattern settles
([codification and relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)).
The spec already permits this without new machinery because its primitives
are the same whoever invokes them: a judgment or an attempt result leaves
one record whether a code job or the coordinator at the command line made
it, so an apply job that parses a verification can be replaced by the
coordinator reading it and judging, and the engine, the records and
publication do not notice.

The line to hold when that happens: bookkeeping stays in code, because
readiness, currency, cleanup, attempt limits and coverage are enforcement
properties that only a deterministic interpreter can guarantee;
interpretation is what moves. In the active analysis path, code owns scheduling
and hands out each ready round; the coordinator launches all handed-out workers
and settles the round before advancing. A job waits while a producer of its
inputs is pending, except a code consumer applying completed work to immutable
handed subjects as specified in scenario 21.
When the direction is taken up, requirement
5 and the decision "only code jobs judge" are the two places that name the
operator where they should name the coordinator too.

## API proposal

[API design](./api-design.md) and the [Python sketch](./api_sketch.py) propose
the minimal public boundary under the updated requirements: one advancing
call and one generic judgment primitive for code jobs. Operator entry points
are omitted from the sketch by request. The declaration is data, with package
handlers named by dotted path. Pinning and storage remain internal; the sketch
does not add alternative currency or refusal-ownership rules.
[Glossary](./glossary.md) sets one word per concept for the spec and the
API together; it is applied to every file here.

## Translation review

[Translation coherence review](./translation-coherence-review.md) records the
integrated handlers, fixed invariant defects and remaining limits.
[Publication consumer boundary](./publication-consumer-handoff.md) describes
pinned validation, provenance, effects, coordination and format separation.
The operator requested coherence review instead of the planned end-to-end proof.
The operator subsequently authorized retirement of the old engine and a new-only
CLI/skill route. `commonplace-workflow` now prepares, starts, reports and integrates
analyses; `commonplace-run` advances the active plan. Old run directories are
rejected without deleting retained data. This adoption decision does not supply
the missing end-to-end proof or establish production fitness. YAML compaction
remains deferred.

## Consumer surface

[Consumer surface](./consumer-surface.md) reviews the boundary between the
engine and the analysis package: which handler needs are legitimate, which
checks re-prove engine invariants, and two requirement-level resolutions,
settled 2026-10-08: the artifact type is fixed for the run, and coverage is an
engine-derived input rather than a handler recomputation.

## Related

- [Code-scheduled workflows](../../reference/proposals/archive/code-scheduled-workflows.md),
  archived under ADR 113: the retired engine's design; its build workshop
  was deleted at closure on 2026-10-09.
- [Record acceptance reads and judged versions](../../reference/proposals/archive/record-acceptance-reads-and-judged-versions.md):
  the replay defect that prompted this workshop, and the repair proposed
  within the engine then in use.
