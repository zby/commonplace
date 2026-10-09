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
    by:
      role: boundary
      field: result-disposition
      values:
        complete: [runtime, memory, epistemic, reconciliation, memory-profile, synthesis, record-verification, profile-verification, synthesis-verification]
---

# Agentic system analysis set

A directory artifact, as the reference definitions define it: a retained
analysis in the collection's `retained/` area, or the working set of a run. In a finished set the manifest pins a SHA-256 for every member and
records the worker that produced the run under `worker`:

- `profile`: the worker profile the run started with;
- `harness`, `launch-model` and `effort`: that profile's harness, the name
  the harness selects a model by, and its reasoning effort;
- `model`: the exact model ID every worker reported, or `not stated`.

A launch model is an alias such as `sonnet` that may later select a newer
model; the reported model is what ran. One profile writes a whole run, and
publication requires every worker to have reported the same model.

## Members

The layout above declares the members. Every set has the boundary and the
overview. A boundary whose `result-disposition` is `complete` adds the four
reports, the memory profile, the synthesis and the three verifications; any
other disposition admits no other member. Membership is closed. Each member
has its own type and passes ordinary file validation on its own.

The boundary is written first. It declares the analysed source and the run
and boundary identity that every other member repeats; the overview repeats
all of its boundary fields and its disposition. The overview is an entry
page: it declares no sources or records. A member's record references
resolve against the members its role cites. The profile cites only the
three analyst reports: it declares or annotates no records, contributes no
new evidence, cites no source directly, and its source identity matches the
memory report's.

## Whole-set checks

Beyond the layout, validation of the set checks that the manifest pins every
member once it pins any, that no record is declared twice, the overview's
amendment index against the reconciliation, the profile's comparison
references, and that every member's quotations resolve against the
boundary's frozen source, with unavailable pinned bytes reported as
unverified rather than failed.

The word `verifies` has two uses. A verification document's `verifies`
field names its stage, `records`, `profile` or `synthesis`, and must match
its role. A verification role's layout entry `verifies` names the roles
whose acceptance its verdict settles; validation only checks that the names
are roles, and the engine covers each such relation by a judgment of the
verified version (ADR 114).

A verification's Blockers and Limits are `none` or Markdown lists, and a
record blocker starts with the report it addresses. Every limit that cites
record IDs has at least one of those IDs in the synthesis's Limitations.
This checks traceability, not whether the synthesis states the consequence
faithfully; review judges that. The memory report's provenance is a
workflow check, not a set check.

## Working and published sets

Until publication pins the manifest, whole-set validation reports it as
unpinned. A published set is frozen: its manifest pins every member, and a
correction is a new run. Earlier versions, answers, attempts, judgments and
prompts stay in the run's state and are never published.
