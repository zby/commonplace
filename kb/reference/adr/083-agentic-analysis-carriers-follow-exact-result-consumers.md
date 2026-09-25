---
description: "Decision that agentic-system analysis keeps one minimal completion record and reruns failed work from a frozen source"
type: ../types/adr.md
tags: []
status: accepted
---

# 083-Agentic analysis uses minimal rerunnable state

**Status:** accepted
**Date:** 2026-09-04

## Context

An agentic-system analysis needs a reproducible source boundary, an exact
result, and public reviews that never expose a failed replacement. It does not
need to resume midway when the operator is willing to rerun failed work.

Encoding every intermediate phase, worker packet, correction, retry, and
validation receipt made the workflow harder to execute and validate than the
failure cost justified.

## Decision

Every run writes one exact result under
`kb/reports/state/agentic-system-analysis/<run-id>/result.md` and one minimal
run state with `running`, `complete`, or `failed` status.

The state records only the run identity, frozen Git commit or captured-source
identity, completed output paths and SHA-256 values, or one failure reason. A
failed run is not resumed. A later run gets a new ID and repeats the work.

Public reviews use validate-before-replace publication. A failed candidate
leaves the incumbent unchanged. Successful tracked versions rely on Git for
history; the analysis workflow does not stage or commit them.

## Considered alternatives

**Keep resumable phase and packet state.** Rejected because it optimizes an
accepted rerun cost while adding failure modes to every successful run.

**Keep no run state.** Rejected because later consumers still need to verify
the source pin and exact bytes that produced each published review.

**Write directly to the public path.** Rejected because validation failure
would damage or remove the last valid review.

**Archive the incumbent first and restore it if the run fails.** Rejected
because every failure after the archive step would need an exercised inverse,
and only an exact byte restore could honestly return a human `user-verified`
attestation that an agent had stripped. Validating a candidate before
replacement never moves the incumbent, so a failed run has nothing to restore.
This decision retires the proposal "Recoverable replacement of an incumbent
review", which weighed this option.

## Consequences

The skill, schema, validator, and handoff use one small state model. Source
pinning and output identity remain machine-checked, while intermediate work is
disposable. A failed long analysis may consume more time because it starts
again, but failure handling cannot corrupt the published collection.

The operativity path has two consumers: `analyse-agentic-system` writes the
state, and `commonplace-validate` plus
`commonplace-agentic-analysis-handoff` refuse outputs whose source or byte
identity no longer matches. This decision applies only to agentic-system
analysis; it does not prescribe retry policy for other workflows.

---

- [Agentic system analysis run state](../../types/agentic-system-analysis-run-state.md) — implemented-by: the minimal completion record
- [Analyse an agentic system](../../instructions/analyse-agentic-system/SKILL.md) — implemented-by: the rerun and candidate-publication workflow
