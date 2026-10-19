# Extract a base workflow system for headless harnesses

Posed 2026-10-19 by the operator: extract a reusable base workflow system
from Commonplace's headless work so other workflows can use it without
depending on the KB's types, analysis method, or environment preparation.

The operator identifies the sibling project Treadle at
`/home/zby/llm/treadle` as the first attempt at this extraction. This attempt
uses headless harnesses directly, instead of an orchestrator agent executing
step-program instructions. Ordinary workflow code owns branches, loops,
concurrency and correction order; workers perform the model tasks.

The operator authorized implementation on 2026-10-19 using Sol workers with
parent review. Implementation is staged as the standalone `treadle-headless`
package under `package/`, with its own build and test configuration and no
Commonplace imports. Treadle's existing implementation and the ongoing
Commonplace port remain separate work. Final repository placement and public
package naming remain open; this local staging choice replaces neither.

The operator further directed that implementation be independent of the
headless branch. The [implementation plan](./implementation-plan.md) defines
standalone delivery and acceptance; Commonplace integration is a later
consumer project, not a prerequisite for building or releasing the base.

## Implementation status

The [standalone package](./package/README.md) is implemented and reviewed.
[Implementation results](./implementation-results.md) record the fixes,
55 passing tests in both source and clean installed-wheel environments, and
successful real Codex/Pi Sol probes. Claude remains unprobed with a real model.
The package is staged locally; final repository placement and Commonplace
integration remain separate decisions.

## Agreed boundary

The base executes jobs in a caller-supplied working directory. It does not
promise a pinned code version or an isolated execution environment.

The [responsibility matrix](./responsibility-matrix.md) assigns ownership,
inputs and guarantees across this boundary. It expands these agreed scope
decisions into a proposed extraction contract; it does not fix a package API.

Output separation means that collecting one launch's result cannot silently
collect files from a different launch. It does not prevent a worker from
writing elsewhere. Filesystem permissions, process isolation, credentials and
network restrictions belong to the caller's harness or execution environment.

No generic environment-provider framework, container management, worktree
manager, or deployment system is required for this extraction. No general
scheduler or orchestrator-agent handoff protocol is required either.

## Resumption and reuse

Scope retained results to an explicit run. The caller is responsible for
maintaining the environment in which those results remain reusable. A key
over the prompt, supplied inputs and worker configuration cannot establish
that ambient files, tools or user configuration stayed unchanged.

Commonplace can continue preparing and checking its pinned worktrees outside
the base. Another caller may use an ordinary directory. Cross-run caching is
deferred until a consumer needs it.

Before implementation, state the interruption contract precisely: what is
recorded, when a rerun repeats work, how failures spend budgets, and how live
workers are handled when their controller stops. Do not imply exactly-once
execution from durable results. Any stronger recovery requirement needs a
concrete consumer and a separate scope decision.

## Inputs and coordination

- [Headless analysis](../headless-analysis/README.md) contains the initial
  harness and result-cache experiment.
- [Headless engine port](../headless-engine-port/README.md) owns adapting the
  Commonplace analysis workflow and deciding its adoption. This workshop
  owns the reusable extraction boundary, not that port's rollout.
- The active implementation is being developed by another agent in
  `/home/zby/llm/commonplace-headless`, particularly
  `src/commonplace/headless/` and
  `src/commonplace/lib/agentic_analysis/workflow.py`. Inspect its current
  state only when a later integration or comparison needs it. It is not an
  implementation baseline or dependency for the standalone package.
- Inspect `/home/zby/llm/treadle/README.md` and its current design before
  deciding what to reuse. The operator's identification of Treadle as the
  predecessor does not require retaining its APIs or execution machinery.
- [Replaceable workflow orchestrators](../../reference/proposals/replaceable-workflow-orchestrators.md)
  supplies prior Commonplace framing for separating workflow requirements
  from execution machinery; it is a proposal, not additional adopted scope.

The standalone implementation has separate ownership from the port. Any later
integration must coordinate ownership and record the compared revisions.
Do not edit the other agent's work or replace live command installations as an
incidental part of this workshop.

## Evaluation boundary

The result must demonstrate reuse without importing Commonplace's KB
validation, type interpretation, analysis roles or publication policy into
the base. Preserve those capabilities in the consuming layers rather than
weakening them to make extraction easier.

Use a small workflow producing ordinary files with a caller-supplied check
to establish independent package acceptance. A later Commonplace integration
must establish that its types, verification and publication guarantees survive;
that evaluation does not block the standalone package. Reconsider the boundary
if either use requires hidden Commonplace dependencies or generic machinery
without a demonstrated use.

Acceptance evidence must cover successful execution and the failure cases
that determine whether results can be trusted:

- A failed launch leaves partial outputs or a problem file; a retry cannot
  silently inherit them or misattribute their provenance.
- Missing outputs, rejected candidates and exhausted budgets have explicit
  outcomes, including after a restart.
- Independent jobs respect the concurrency bound, and accepted results can
  be reused within a run without launching workers again.
- Checks that depend on sibling outputs receive a defined snapshot. Exercise
  opposite completion orders where order could change acceptance or spend
  retries; assign snapshot construction explicitly to the base or caller.
- Fake-harness tests exercise the actual file and result protocol. Bounded
  real-harness checks establish that supported adapters can execute it.

These cases retain concerns raised during the operator's design discussion;
they are acceptance requirements, not assertions that the active port still
has the reviewed defects. Recheck their disposition at the chosen revision.
Passing them does not establish the substantive truth of model outputs or
reproducibility of an uncontrolled environment.

Keep observations, decisions and unresolved questions here as work proceeds.
Record the inspected revision and exact test scope beside implementation
evidence. If implementation is blocked, retain the concrete boundary or
consumer conflict rather than widening the package speculatively.

## Closes when

The standalone base and its independent example meet the agreed acceptance
boundary, ownership, API and operational guarantees have durable documentation,
and any Commonplace integration follow-up has an explicit owner; or the operator
abandons the work with a recorded reason. Promote Commonplace decisions to the
library, retain package documentation with its implementation, then remove
this workshop and its active-list entry. Completion does not require the
headless branch to land or adopt the package.
