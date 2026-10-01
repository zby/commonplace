---
description: A frozen analysis directory with outcome-dependent membership and a manifest pinning every report.
type: types/type-spec.md
name: agentic-system-analysis-set
schema: ./agentic-system-analysis-set.schema.yaml
---

# Agentic system analysis set

A directory artifact in the reports collection. `ARTIFACT.yaml` selects this
type and records a SHA-256 for every member. All direct Markdown children
are members; this type uses closed membership.

A complete outcome requires `overview.md`, `runtime.md`, `memory.md`,
`epistemic.md` and `reconciliation.md`. A blocked or out-of-scope outcome
requires only `overview.md`.
The overview's `result-disposition` selects the schema branch. The memory
member must have `report-status: complete`. Each report keeps its own type
and passes ordinary file validation independently.

The set rule checks run and boundary agreement, duplicate declarations,
cross-member record references and comparison-profile references against
the union of declarations. It requires no run-state file or frozen checkout.
Source anchors and the memory analyst's provenance remain workflow checks.

Run-state and generated reviews pin the manifest bytes. Published sets are
frozen; corrections require a new run. Working inputs and run state live
outside the output directory.
