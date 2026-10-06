---
description: "Use when planning or implementing the analysis method's type/instruction separation, with freedom to choose the design within the stated outcome and boundaries."
type: types/instruction.md
---

# Separate analysis types from instructions

Make every accepted analysis output checkable against its content contract
without reading the procedure that generated it.

## Intent

The operator wants `analyse-agentic-system` to follow the same division as
Commonplace as a whole: types specify what a conforming artifact is;
instructions explain how to produce or check it. An independent checker should
not need to reconstruct the author's task to discover the acceptance criteria.

This applies to the full method, including shared definitions, intermediate
results, retained reports, verification results and completion state. It is not
just a relocation of files into `types/`.

A verifier still needs its own instructions for inspection, evidence access,
authority and reporting. Those instructions must not be the sole owner of a
criterion for the artifact being judged. Classify a rule by its function, not
its grammatical form.

## Authority and boundaries

This operator-requested plan awaits a separate implementation commission.
It authorizes neither method changes nor worker launches, live analysis runs,
publication, staging or commits. An implementer commissioned through the
[workshop](./README.md) follows
[method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md)
and the repository's standing rules.

Other agents are working on the method. Coordinate ownership before touching
shared files and judge what remains from the current checkout, not from this
plan's observations alone.

Preserve analytical standards, worker authority, correction ownership, round
budgets and publication policy. Do not rewrite retained analyses or alter an
open run's pinned method. If completing the split requires a policy change or
resolving contradictory requirements, bring that decision back to the operator.

## Freedom of execution

Choose the architecture, work order, contract granularity and verification
approach that meet the intent at reasonable cost. No ownership spreadsheet,
particular file layout, new type per fragment, fixed editing sequence or live
model trial is required by this plan. Reuse existing mechanisms where they fit;
introduce structure only when an actual consumer needs it.

Shared criteria may remain shared. The requirement is an authoritative,
available type-side contract, not a copy in every report type. Instructions may
remind workers of a criterion without becoming a competing definition.

Keep these distinctions intact while choosing the design:

- Artifact conformance concerns the document or set's content and structure.
- Job acceptance also checks invocation-specific expectations and obligations.
- Run completion also checks source pins, method identity and publication state.

A run's expected identity need not become a universal report rule. A standalone
set check must not claim to prove source support or execution history that
requires additional evidence. Relationships between artifacts, such as stable
record IDs or equality of accepted and published bytes, can be contract
properties even though checking them requires more than one file.

## Starting evidence, not a prescribed worklist

The read-only assessment found the following concentrations of mixed
responsibility. They are leads for the implementer, not a frozen inventory:

- The shared boundary, sources and records documents under
  `kb/agentic-system-analyses/instructions/` contain both content criteria and
  worker procedures.
- The boundary job, synthesis job and shared worker rules define intermediate
  output formats that are not fully specified independently of those procedures.
- Record verification judges boundary classification while its declared inputs
  exclude the shared boundary contract; its instruction repeats some criteria.
- Run-state and overview types include directions about validation timing,
  restarting or stopping, alongside checkable artifact properties.
- Coverage and uncertainty requirements recur across contracts, generation jobs
  and verification jobs, leaving several texts to maintain for one standard.

The [Sol follow-up plan](./sol-run-follow-up-plan.md#7-small-repairs-found-by-the-complexity-measurement)
already identifies related delivery gaps. Reconcile overlapping work rather
than assuming every older repair recommendation remains appropriate.

The [type-spec contract](../../types/type-spec.md) and
[validation contract](../../reference/validation-contract.md) supply the system
model. The workflow's dependency construction and its tests show what workers
actually receive; links alone do not establish delivery.

## Evidence of completion

Demonstrate that:

- Every accepted output has an identifiable content contract independent of its
  generation procedure, including meaningful intermediate results.
- Producers and checkers receive the applicable criteria through their actual
  consumption paths. No acceptance criterion exists only in a generation job
  or is silently added by a verifier instruction.
- Types describe checkable properties; instructions retain production,
  inspection, coordination and recovery procedure.
- Schemas, imperative checks and semantic criteria agree. Necessary criteria
  survive the refactor without accidental changes to analytical or workflow
  policy.
- The changed method remains executable and its dependencies remain available
  and pinned where required. Applicable repository validation and tests pass.

Choose evidence proportionate to the changes. Existing dependency tests,
interface fixtures and a review with generation instructions withheld are
possible means, not mandatory rituals. Distinguish demonstrated interface
behavior from claims about model adherence or analytical quality.

### Shared-contract review boundary

Account for ordinary type-conformance review as well as the analysis jobs.
The current [review architecture](../../reference/review-architecture.md) pins
the note and criterion for freshness; linked context does not automatically
become a freshness input. Show how required shared criteria reach that reviewer
and what changing them means for an existing review baseline.

If this cannot be satisfied within existing review mechanisms, return the
smallest unresolved decision and its consequences to the operator before
expanding into generic review or freshness changes. Do not conceal the gap
through duplicated criteria or claim full completion from analysis-job delivery
alone.

## Partial progress and return conditions

Prioritize authoritative content criteria and reliable delivery to checkers
over cosmetic relocation. If work stops, leave a coherent result and report
which outputs are independently checkable, which are not, and what decision or
dependency prevents completion. Partial progress is useful; a renamed directory
or passing structural checks alone is not proof of the intended separation.

Return policy conflicts, scope expansion and unresolved cross-agent ownership
before making the affected change. Otherwise exercise implementation judgment
within the stated boundaries. Close with a concise account of the achieved
separation, supporting checks and any remaining limits; no additional planning
artifact is required merely to document compliance with this plan.
