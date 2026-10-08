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
      cites: [boundary, runtime, memory, epistemic]
    record-verification:
      path: record-verification.md
      type: agentic-system-analyses/types/agentic-system-verification.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic, reconciliation]
    profile-verification:
      path: profile-verification.md
      type: agentic-system-analyses/types/agentic-system-verification.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [runtime, memory, epistemic, memory-profile]
    synthesis-verification:
      path: synthesis-verification.md
      type: agentic-system-analyses/types/agentic-system-verification.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic, synthesis]
  required:
    always: [boundary, overview]
    by:
      role: boundary
      field: result-disposition
      values:
        complete: [runtime, memory, epistemic, reconciliation, memory-profile, synthesis, record-verification, profile-verification, synthesis-verification]
---

# Agentic system analysis set

A directory artifact in the agentic-system-analyses collection's `retained/`
area or a local working run. The opt-in engine uses `state/<run-id>/set/` as
its sole working set; the live legacy skill and CLI still use
`state/<run-id>/output/`. These are distinct run formats, not mirrored paths.
`ARTIFACT.yaml` selects this type. In a finished set it records a SHA-256 for every member and
names the worker that produced the run under `worker`: the exact `model`
identifier and, when the harness reports one, its reasoning `effort`. One
model writes a whole run, so the manifest carries it once; sets published
before 2026-10-06 have no `worker`.

The layout above declares the members. Every set has the boundary and the
overview; a `complete` boundary disposition adds the four reports, the
memory profile, the synthesis and three verifications. Any other disposition
admits no other member. Membership
is closed. Each member keeps its own type and passes ordinary file
validation independently.

The boundary is the run's first member and the source of its identity and
source declarations. Every other member repeats its run and boundary
identity; the overview repeats all of its boundary fields and its
disposition. The overview is an entry page, not a copy of member accounts.
It declares no sources or records. Each member's record references
resolve against the members its layout role cites. The profile cites only
the three analyst reports: it declares or annotates no records, contributes
no new evidence, cites no source directly, and its source identity matches
the memory member.

The set rule also checks that the manifest pins every member once it pins
any, duplicate declarations, the overview's amendment index against the
reconciliation, and the profile's comparison references. The three
verification roles respectively require `verifies: records`, `profile` and
`synthesis`. Their citation partners include the reconciliation, memory profile
and synthesis respectively, alongside the reports declared in the layout.
Their Blockers and Limits are `none` or Markdown lists; record
blockers name the report owner. Every verification limit that cites IDs has
at least one of those IDs in the synthesis's Limitations. This checks
traceability, not whether the consequence is faithfully stated; review checks
that meaning. Every member's quotations resolve against the boundary's frozen
source; unavailable pinned bytes are reported as unverified. The set requires
no run-state file. The memory analyst's provenance remains a workflow check.

A working set starts with a manifest naming only the type, so it is
recognized from its first member. Until code pins it, whole-set validation
reports the unpinned manifest and any absent required members, and checks
relations among the members present.

The opt-in engine keeps a type-only working manifest in `set/`; assembly
returns an exact-byte pinned manifest that publication consumes as an engine
output, not a second mutable projection. Legacy run state pins its output
manifest bytes. Published sets are frozen; corrections require a new run.
Earlier member versions, answers, attempts, judgments, effect journals and
prompts live outside `set/` and are never published. Legacy correction packets,
change diffs, round set-check files and run state likewise stay outside
`output/`. The opt-in engine does not manufacture legacy run-state or an
`output/` twin.
