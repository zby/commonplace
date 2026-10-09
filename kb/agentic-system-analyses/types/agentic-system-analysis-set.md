---
description: A frozen analysis directory whose layout declares its products and judgments, their relations, and completeness by disposition.
type: types/type-spec.md
name: agentic-system-analysis-set
schema: ./agentic-system-analysis-set.schema.yaml
layout:
  membership: closed
  roles:
    boundary:
      path: boundary.md
      type: agentic-system-analyses/types/agentic-system-boundary.md
      cites: [boundary]
    overview:
      path: overview.md
      type: agentic-system-analyses/types/agentic-system-analysis-overview.md
      identity:
        - from: boundary
          fields: [run-id, result-disposition, target-class, boundary-kind, reviewed-boundary, analysis-cutoff, evidence-tier]
      cites: [boundary, runtime, memory, epistemic]
    runtime:
      path: runtime.md
      type: agentic-system-analyses/types/agentic-system-runtime-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    memory:
      path: memory.md
      type: agentic-system-analyses/types/agent-memory-analysis-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    epistemic:
      path: epistemic.md
      type: agentic-system-analyses/types/agentic-system-epistemic-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    reconciliation:
      path: reconciliation.md
      type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    memory-profile:
      path: memory-profile.md
      type: agentic-system-analyses/types/agent-memory-profile.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
        - {from: memory, fields: [source-identity]}
      cites: [runtime, memory, epistemic]
    synthesis:
      path: synthesis.md
      type: agentic-system-analyses/types/agentic-system-synthesis.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic, report-verification, profile-verification]
    report-verification:
      path: report-verification.md
      type: agentic-system-analyses/types/agentic-system-verification.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic, reconciliation]
      verifies: [runtime, memory, epistemic, reconciliation]
    profile-verification:
      path: profile-verification.md
      type: agentic-system-analyses/types/agentic-system-verification.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [runtime, memory, epistemic, memory-profile]
      verifies: [memory-profile]
    synthesis-verification:
      path: synthesis-verification.md
      type: agentic-system-analyses/types/agentic-system-verification.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic, synthesis]
      verifies: [synthesis]
  required:
    always: [boundary, overview]
    when:
      role: boundary
      field: result-disposition
      values:
        complete: [runtime, memory, epistemic, reconciliation, memory-profile, synthesis, report-verification, profile-verification, synthesis-verification]
---

# Agentic system analysis set

A directory artifact: a retained analysis in the collection's `retained/`
area, or the working set of a run. The layout above declares the members;
each member's type says what it contains.

A finished set's manifest pins a SHA-256 for every member and records the
worker that produced the run under `worker`: the `profile` the run started
with, its `harness`, `launch-model` and `effort`, and the exact `model`
every worker reported, or `not stated`. The launch model is the name the
harness selects a model by; the reported model is what ran.

Beyond the layout, validation of the set checks that the manifest pins
every member once it pins any, that no record is declared twice, the
overview's amendment index against the reconciliation, the profile's
comparison references, the verifications' Blockers and Limits lists and
each limit's trace into the synthesis, and that every member's quotations
resolve against the boundary's frozen source. A verification's role names
its stage; the role's layout `verifies` names the roles its verdict settles
(ADR 114).

A published set is frozen: a correction is a new run, and the run's earlier
versions, answers, attempts, judgments and prompts are never published.
