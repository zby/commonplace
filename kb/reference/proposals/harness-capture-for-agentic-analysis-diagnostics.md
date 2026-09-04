---
description: "Proposal: capture harness-visible failures and truncation for agentic-system analysis without claiming completeness from repository state alone"
type: ../types/design-proposal.md
tags: [context-engineering, kb-maintenance]
---

# Harness capture for agentic-analysis diagnostics

Agentic-system analysis now keeps a structured, byte-identified diagnostic
ledger. That ledger can prove the integrity and disposition of events recorded
in it. It cannot prove that it contains every relevant event, because
Commonplace does not receive the harness's tool-call and output-delivery stream.
This proposal holds the remaining design question: whether and how a harness
should supply that stream without making the analysis workflow vendor-specific.

## Current state (as of 2026-09-04)

- `analyse-agentic-system` requires the orchestrator to record each material
  workflow failure, truncation, or non-execution immediately.
- The run-state validator checks every recorded diagnostic's identity, shape,
  output evidence, recovery, and unresolved-result disposition.
- A command that Commonplace launches can expose its exit status and captured
  bytes. A malformed harness API call may be rejected before any Commonplace
  process starts. A harness may also truncate delivered output after the child
  process completed successfully.
- The Apache Maka analysis postmortem found both classes only by inspecting the
  surrounding session. They were absent from the run state even though the
  final analysis itself validated.

## Problem and forces

The framework needs to distinguish three claims: recorded diagnostics are
intact, all Commonplace-mediated commands were recorded, and the whole harness
session was captured. Only the first is currently justified.

The design must preserve harness portability, exact event provenance, secret
redaction, bounded retained state, and the difference between process output
and output delivered to the agent. Capture must not silently expand analysis
authority or retain unrelated conversation. It must also fail visibly when a
harness changes its event format.

## Options and operativity

### Keep orchestrator-authored ledgers

The analysis skill remains the consumer. Its natural-language instruction is
the channel and has prescriptive force over the orchestrator, which writes the
ledger. This is portable and already shipped, but completeness rests on the
same agent whose mistakes the ledger is meant to expose.

### Add a harness event adapter

A harness integration consumes tool requests, rejection events, process
results, and delivery metadata and projects analysis-scoped events into the
ledger. The harness event stream is the channel and adapter validation has
enforcing force. This is the only option that can support a session-completeness
claim, but no portable event interface is currently available.

### Route source inspection through a Commonplace wrapper

The analysis orchestrator invokes a command wrapper for repository queries.
The CLI call is the channel and the wrapper enforces command/output recording.
This can cover Commonplace-mediated source reads without harness support. It
cannot see rejected delegation calls or delivery truncation, and it risks
creating a second shell interface for operations agents already perform.

### Import a transcript after the run

A postmortem operation consumes an exported harness transcript, compares its
events with the run ledger, and reports omissions. The export file is the
channel and the importer has diagnostic rather than execution force. This
keeps runtime coupling low but depends on export availability and cannot repair
missing evidence before the analysis uses it.

**Candidate selection: none.** The event adapter is the only complete option,
but adopting it without an inspectable harness event contract would invent an
integration surface. The wrapper and importer remain partial alternatives, not
silent substitutes for session capture.

## Free choices

- Whether the useful target is whole-session completeness or only complete
  capture of source inspections that can support findings.
- Whether normalized events or exact vendor events are canonical. Normalized
  events improve portability; exact events preserve failure evidence.
- Where redaction occurs and how the consumer can verify that redaction did not
  remove an analysis-relevant diagnostic.
- Whether a transcript mismatch blocks handoff or produces a named limitation.
- Which party owns retention and cleanup for event bytes that extend beyond the
  analysis run's current state directory.

## Adoption criteria

Choose an integration only when at least one harness used for Commonplace work
exposes an inspectable event stream containing pre-execution call rejection and
post-process delivery metadata. A candidate must be testable with fixtures for
malformed calls, nonzero exits, successful-but-truncated delivery, retries, and
secret-bearing output. Its result must distinguish recorded-event integrity
from claimed capture coverage and degrade explicitly on an unknown event
version.

## Risks

- A partial adapter may create more confidence than the manual ledger while
  still missing the most important host-side events.
- Exact transcripts may retain secrets or unrelated user material beyond the
  authority of the analysis run.
- Vendor-specific schemas can leak into the run-state contract and make a
  portable methodology depend on one execution host.
- Blocking every transcript mismatch can make analysis availability depend on
  telemetry rather than evidence needed for the substantive result.

---

Relevant Notes:

- [Trajectory-aware evaluation of transforming agent workflows](./trajectory-aware-evaluation-of-transforming-agent-workflows.md) — see-also: the broader proposal for using intermediate execution evidence to diagnose agent workflows
- [Analyse an agentic system](../../instructions/analyse-agentic-system/SKILL.md) — procedure: the shipped workflow that records diagnostics but cannot observe the harness event stream
