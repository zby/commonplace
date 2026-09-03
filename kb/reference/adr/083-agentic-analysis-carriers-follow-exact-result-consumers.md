---
description: "Decision that each agentic-system analysis declares its exact-result consumers and carrier before execution, uses checked local run state, and keeps compact system analyses as projections"
type: ../types/adr.md
tags: []
status: accepted
---

# 083-Agentic analysis carriers follow exact-result consumers

**Status:** accepted
**Date:** 2026-09-03

## Context

An agentic-system analysis can produce three artifacts with different jobs: a
complete typed run result, temporary coordination state, and a compact external
system analysis. The first post-promotion run emitted its complete result only
in a response, later recovered it into ignored cache, and published only the
compact projection. That preserved the main findings but left no
lifecycle-valid local carrier for the exact result. Cache cannot fill that role
because deleting a cache entry must lose no unique evidence or unresolved
state.

The complete result may be consumed only during a local operation, or it may be
needed later from a clean checkout for audit, reproduction, or citation. Those
uses require different retention. The workflow also spans enough phases that
source, register, packet, validation, and handoff identities cannot safely
remain only in the executor's conversation context.

## Decision

Every `analyse-agentic-system` run declares the consumers of the exact result,
its canonical carrier and physical form, permitted projections, retention and
cleanup rule, and write authority before source inspection.

- An explicit response is canonical only when no local operation needs the
  exact bytes.
- `kb/reports/state/agentic-system-analysis/` is canonical while named local
  consumers need the bytes. The analysis workflow owns cleanup and may remove a
  completed run only after every declared consumer has completed or been
  disposed and no unresolved transfer or projection state remains.
- `kb/reports/retained/` is canonical when a named future operation must read
  the exact bytes from a clean checkout. Retention lasts while that consumer or
  a durable citation remains.
- `kb/reports/cache/` is never a canonical carrier.
- A compact `kb/agentic-systems/` artifact is a derived library projection. It
  does not replace the complete typed result.

Every run also opens one checked operational record of type
`agentic-system-analysis-run-state`. The record advances monotonically from
declared authority through source freezing, runtime-baseline sealing, lens
packet issue and acceptance, reconciliation, assembly, validation, and
handoff readiness. Immutable packet and return files carry byte identities.
A correction names both register versions and the packet it invalidates; an
invalidated packet cannot be accepted.

Final validation uses `commonplace-validate --json` on the exact assembled
entry. The recorded receipt must identify one analyzed artifact of type
`agentic-system-analysis-result`, with no warnings or failures. Before handoff,
the run-state validator rechecks the entry's bytes, type, run ID, and declared
carrier. This checked record is specific to this workflow; it is not a generic
durable-execution framework.

## Considered alternatives

**Keep response-only as the default.** Rejected because a response can satisfy
the immediate reader while losing the exact input needed by a local transfer,
publication, or audit operation. A response remains available when its lack of
a local consumer is explicit.

**Retain every complete result in Git.** Rejected because many results have
only short-lived local consumers. Permanent retention without a named consumer
would broaden `kb/reports/retained/` into a run archive.

**Use cache as the local carrier.** Rejected because an LLM-produced exact
result is not reproducible byte-for-byte and may hold unique evidence. Calling
it cache would contradict the reports contract.

**Rely only on stronger prose in the skill.** Rejected because the original
skill already stated most ordering and lifecycle rules. The failure was losing
their state across a long execution, so the repair needs an inspectable record
and referential validation.

**Build a general run engine.** Rejected because only this workflow has supplied
a worked failure and acceptance case. A reusable execution framework would
commit other workflows to an untested abstraction.

## Consequences

Interrupted analyses leave an honest, locally recoverable phase and the exact
inputs already supplied to workers. State costs additional writes and hash
checks, and retained results require an explicit future consumer. A compact
publication can stay economical while its source run remains identifiable.

The operativity path has two consumers. `analyse-agentic-system` creates and
advances the record as binding workflow state. `commonplace-validate` consumes
the run-state type and referenced byte identities with fail force before lens
dispatch, final validation, and handoff. The result type records the selected
carrier and projection lineage for readers.

This decision stops at the `analyse-agentic-system` workflow. It does not make
all agent work durable, establish a shared run-state service, or require every
LLM report to be retained.

---

- [Agentic system analysis run state](../../reports/types/agentic-system-analysis-run-state.md) — implemented-by: the checked phase, packet, validation, and handoff record
- [Analyse an agentic system](../../instructions/analyse-agentic-system/SKILL.md) — implemented-by: selects the carrier and advances the run state
- [The validation contract](../validation-contract.md) — see-also: supplies the referential type-rule and machine-readable validation surfaces
