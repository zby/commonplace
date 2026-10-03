---
type: reference/types/design-proposal.md
description: "Proposal: separate Commonplace workflow requirements from execution machinery so an agent-plus-script orchestrator and a harness-native orchestrator can implement the same workflow."
---

# Replaceable workflow orchestrators

## Problem

Commonplace needs workflows that run across agent harnesses. Its current
orchestration combines an orchestrator agent with a replayable Python script.
That arrangement supports a harness whose agent invokes separate commands and
launches workers through native tools. It need not be the required execution
model for every harness.

Propose making the **whole orchestrator** replaceable: the component that
schedules workers, judges results, tracks progress, handles interruption, and
publishes accepted artifacts. The replaceable unit includes both the
orchestrator agent and the Python machinery, not just the worker launcher.
A candidate Pi implementation would perform orchestration directly in
TypeScript, without a model acting as the workflow scheduler.

The workflow's requirements would remain portable. Its command protocol and
internal recovery representation would not automatically become universal
requirements. This is an unadopted design, not authority to replace the current
engine or relax any workflow safeguard.

## Current state (as of 2026-10-03)

`src/commonplace/workflow/engine.py` runs a workflow definition from the top
on each `step`. Durable records determine which work has been accepted and
which effects may execute. The engine provides output judgment, attempt and
repair limits, a run lock, atomic state updates, interrupted-file-move recovery,
and recognition of uncertain effects.

`step` is replayable but not generally idempotent. Calling it again can consume
a worker round and count absent output as a failed attempt. Safe operation
requires the orchestrator to know that every worker of the previous round has
finished or failed to start. Recovery also requires establishing that workers
from an earlier session have stopped.

For `analyse-agentic-system`, the driving instruction makes the agent execute
this protocol, launch workers with prescribed handoffs, and stop when code
requires it. The Python definition in
`src/commonplace/lib/agentic_workflow.py` contains workflow-specific decisions
as well as calls into execution machinery. There is not yet a separate contract
against which alternative orchestrators demonstrate equivalence.

## Shared workflow requirements

The common contract would state what constitutes a correct execution, rather
than prescribe how an implementation retains its execution position:

- Worker roles, dependencies, and permitted input boundaries.
- Mutation authority and separation of worker outputs from live targets.
- Output formats and acceptance conditions.
- Retry, repair, and stop rules.
- Conditions for publishing exact accepted bytes.
- Required provenance and retained artifacts.
- Interruption guarantees required for that workflow.

Fresh contexts, staged disclosure, and independent review remain requirements
where the workflow uses them. An implementation cannot substitute forwarding
the full conversation or previous outputs merely because its harness makes
that convenient.

The user-facing agent may still commission the work and explain its outcome.
It need not make scheduling decisions during execution.

## Options and their consumers

### Retain one engine and add harness drivers

A Pi extension could execute the current command protocol, dispatch workers,
wait for each round, and report launch failures. The Python engine would remain
the sole scheduler and authority for acceptance and publication.

**Consumption path:** a workflow invocation would enter a harness driver;
the driver would consume the engine's outcomes as binding execution commands.
No automatic Pi driver exists yet; one would need to be built.

This option reduces model-mediated protocol errors and avoids duplicating
workflow decisions. It preserves the replayed-definition model and command
boundary in harnesses that could otherwise execute a direct asynchronous
workflow. It replaces only the driver, not the whole orchestrator.

### Replace the whole orchestrator against a common contract

The current agent-plus-Python implementation would remain available. A
candidate Pi implementation would use TypeScript control flow to launch
independent agent sessions, await results, invoke validators, and publish under
the same workflow requirements. It would not have to emulate `step`.

**Consumption path:** a workflow invocation would select an orchestrator
implementation. Each implementation would consume the shared workflow contract
as binding requirements. TypeScript code, rather than the coordinator model,
would determine execution transitions in Pi. The contract and native
orchestrator do not exist yet; both would need to be built.

This is the candidate direction. It permits a harness-appropriate execution
model while preserving cross-harness workflow behavior. Its main cost is the
risk that implementations interpret or duplicate workflow policy differently.
Existing Python validators and publication components could remain reusable;
a TypeScript orchestrator does not require every supporting component to be
rewritten.

## Portability and recovery

Two requirements must be distinguished:

- **Execution portability:** different harnesses can execute the same workflow
  correctly and produce artifacts under a common public contract.
- **Recovery portability:** an unfinished run can move between orchestrator
  implementations without losing accepted work or violating execution rules.

Execution portability is required by this proposal. Recovery portability is
an additional, unresolved choice.

With execution portability alone, implementations may use different internal
checkpoints. Each must still meet the workflow's interruption guarantees and
identify the implementation needed to resume its unfinished runs. A
TypeScript implementation cannot rely on live async variables for recovery
after its host stops. Publication interrupted between an effect and its
completion record still needs recognition or an explicit uncertain outcome.

Recovery portability would additionally require compatible durable run state,
worker ownership, and interrupted-effect semantics. It would constrain both
implementations beyond their common published outputs. The candidate starting
scope is execution portability without cross-implementation resume, subject
to an operator decision about the value of transferring unfinished runs.

## Forces and free choices

**Policy drift is the primary risk.** Implementations could disagree about
repair allowances, reviewer inputs, or publication eligibility while producing
structurally valid artifacts. The common contract needs an authoritative home
independent of either implementation. Its representation is not selected:
a shared specification with conformance tests and an executable common
representation are both possible. The latter may reduce duplication but also
constrain native control flow.

**Recovery guarantees must be chosen explicitly.** Removing repeated command
invocations does not itself justify weaker interruption handling. Whether an
implementation resumes, safely restarts, or stops for operator reconciliation
must satisfy the named workflow's requirements.

**Reuse is independent of language.** Validation and publication can remain
shared components even when scheduling differs. Rewriting them would need a
separate benefit and evidence of preserved behavior.

No TypeScript orchestration library, checkpoint format, selection interface,
or migration procedure is selected here. The current engine remains operative
until an alternative has been adopted for a named workflow.

## Acceptance and evaluation warrant

Common conformance cases would test both orchestrators against the workflow
contract: launch failure, missing or rejected output, exhausted repair allowance,
review digest mismatch, restricted worker inputs, concurrent workers during
recovery, and interruption around publication. Dispatch inspection is needed
for information boundaries; artifact validation alone cannot establish them.

**Consumption path:** an implementation's test suite and adoption review would
consume these cases as evidence of contract conformance. They are not an oracle
for the substantive truth of worker analyses. Their warrant comes from explicit
workflow requirements and expected outcomes, not agreement between two
implementations. Matching results can preserve a shared defect.

This proposal does not add an automated semantic evaluator or authorize
replacing an independent reviewer with deterministic validation.

## Adoption criteria

Adoption for a named workflow would require:

- An authoritative contract separating workflow requirements from the current
  agent-and-command protocol.
- An explicit choice about cross-implementation recovery and the interruption
  guarantees each implementation must preserve.
- A native orchestrator that preserves authorized handoffs, acceptance rules,
  stop conditions, provenance, and publication safeguards.
- Common conformance evidence for the current and candidate implementations,
  including failures and interruption rather than only successful runs.
- A defined consumer that selects the implementation and identifies how an
  unfinished run can be recovered.

`analyse-agentic-system` is a candidate first workflow because its current
implementation already separates worker jobs from deterministic scheduling
and judgment. Success for that workflow would not establish suitability for
all Commonplace procedures, especially those requiring staged interaction
with the same worker.

---

- [Drive a code-scheduled run](../../agentic-systems/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md) — see-also: the current agent-facing execution protocol, which an alternative orchestrator need not reproduce internally.
