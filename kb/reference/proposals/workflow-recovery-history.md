---
type: reference/types/design-proposal.md
description: "Proposal: preserve enough workflow recovery evidence to distinguish clean completion from completion after repairs"
---

# Workflow recovery history

A completed workflow can have encountered refusals, blocked steps and worker
errors. Operators evaluating a method need to distinguish completion without
these events from completion after recovery. Current job state answers whether
work remains; it does not reliably answer what happened before acceptance.

## Current state (as of 2026-10-03)

In `src/commonplace/workflow/engine.py`, `accept` resets the job's failure
counter and history. The block path also clears those values while retaining
block counts. A successful final state therefore cannot establish that no
earlier refusal occurred. This behavior serves scheduling and retry accounting;
changing it merely to support audits could change recovery behavior.

The Dynamic Cheatsheet `AAS-2026-10-02-dynamic-cheatsheet-01` audit needed
worker session traces to recover verification refusals and repairs made inside
worker sessions. The accepted analysis is retained separately from those local
traces. A worker's recovered shell error may never reach the workflow engine.
Engine history alone would therefore leave part of the audit unanswered.

## Options and consumers

**Keep manual trace audits.** Operators read session traces alongside accepted
outputs, and describe which traces they inspected. This supplies evidence to
human or agent reviewers without changing scheduling or acceptance. It has no
binding force on a run. It requires accessible traces and repeated audit work;
missing traces must remain a stated evidence limit.

**Derive an audit summary from existing evidence.** An audit consumer would
combine saved workflow records and session traces after a run. It would expose
refusals, blocked steps and recoveries with their evidence locations, separating
engine events from events inferred from worker traces. No consumer currently
provides this combined summary; one would need to be built. Its output would
inform operators and method reviewers, without changing retries or certifying
the accepted analysis. Trace formats and retention would limit coverage.

**Retain a separate engine event history.** The engine would retain observed
failures, refusals and recoveries independently of mutable scheduling state.
An operator or audit consumer would read it through the run's reporting path.
This would make engine events available after acceptance, without assigning
them new acceptance force. A reporting consumer and retention policy would
need to be built. It would still require traces for worker-internal recovery;
worker reports could supplement it but cannot warrant complete coverage.

These options do not introduce an automated quality verdict. If a later design
makes recovery evidence affect acceptance, it needs a separate justification
for why the observed events warrant that decision. Recovery alone does not
establish that the final output is defective.

## Forces and choices left open

The audit needs evidence of recovered problems while the scheduler needs
current retry state. Their meanings must stay distinct. Retention should make
an audit reproducible without requiring every routine run to retain unlimited
raw traces. Readers also need to know whether evidence is complete, missing,
or inferred; an empty report cannot mean an error-free run unless its coverage
supports that conclusion.

The choice between a derived summary and retained engine events depends on
whether local traces remain available and whether repeated audits justify
changing the run store. The required retention duration, access to sensitive
trace content, and the boundary between engine-observed and worker-reported
events remain open. This proposal selects no storage change.

## Adoption criteria

Compare the options against the known Dynamic Cheatsheet recovery cases:
engine refusals, blocked environment repair and errors recovered inside a
worker session. A candidate must show which cases it recovers, identify missing
evidence explicitly and preserve existing scheduling and retry behavior.
Before adopting engine retention, decide who consumes that evidence and for
how long it must survive. Before adopting a derived summary, demonstrate that
its evidence remains available and that another auditor can verify its claims.
If manual audits remain sufficient, the additional machinery stays unadopted.
