---
description: A frozen analysis directory whose layout declares its boundary, overview and reports, their relations, and completeness by disposition.
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
  required:
    always: [boundary, overview]
    by:
      role: overview
      field: result-disposition
      values:
        complete: [runtime, memory, epistemic, reconciliation, memory-profile]
---

# Agentic system analysis set

A directory artifact in the agentic-system-analyses collection's `retained/`
area, or its local working `state/<run-id>/output/` directory. `ARTIFACT.yaml`
selects this type. In a finished set it records a SHA-256 for every member and
names the worker that produced the run under `worker`: the exact `model`
identifier and, when the harness reports one, its reasoning `effort`. One
model writes a whole run, so the manifest carries it once; sets published
before 2026-10-06 have no `worker`.

The layout above declares the members. Every set has the boundary and the
overview; a `complete` overview disposition adds the four reports and the
memory profile, and any other disposition admits no other member. Membership
is closed. Each member keeps its own type and passes ordinary file
validation independently.

The boundary is the run's first member and the source of its identity and
source declarations. Every other member repeats its run and boundary
identity; the overview repeats all of its boundary fields and its
disposition. The overview's `Boundary and evidence` and `Source register`
sections are a copy of the boundary's, which the set rule checks; the
overview's register declares nothing. Each member's record references
resolve against the members its layout role cites. The profile cites only
the three analyst reports: it declares or annotates no records, contributes
no new evidence, cites no source directly, and its source identity matches
the memory member.

The set rule also checks that the manifest pins every member once it pins
any, duplicate declarations, the overview's amendment index against the
reconciliation, and the profile's comparison references. It requires no
run-state file or frozen checkout. Source anchors and the memory analyst's
provenance remain workflow checks.

A working set starts with a manifest naming only the type, so it is
recognized from its first member. Until code pins it, whole-set validation
reports the unpinned manifest and any absent required members, and checks
relations among the members present.

Run state pins the manifest bytes. Published sets are frozen; corrections
require a new run. Working inputs and run state live outside the output
directory.
