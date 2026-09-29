---
description: "Proposal: make the memory and epistemic lenses' prefixed record IDs canonical, so no step renames proposals, each lens declares its own records, and reconciliation keeps only merges, conflicts, amendments and synthesis"
type: reference/types/design-proposal.md
---

# Lens-prefixed canonical record IDs

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 096](../../adr/096-analysis-passes-declare-their-own-records-under-lens-prefixes.md): the overview, memory, epistemic and runtime report types and the analysis job instructions carry the live design. The pre-adoption state of the record namespace and the failed run that prompted the change remain here — design texture only.

An analysis set has one record namespace, but three passes add to it: the runtime pass and the two lenses, which run in parallel. Before adoption only the runtime pass minted canonical IDs. The lenses proposed records under local `MEM-` and `EPI-` IDs, and a reconciliation mapped each proposal to a canonical ID; code or a job then rewrote the lens output with the mapped IDs. The first code-scheduled run (`AAS-2026-09-29-instinctual-memory-01`) failed in that rewriting: ten records the epistemic lens proposed were registered but declared in no member, so the set did not validate.

## Current state (as of 2026-09-29)

- The overview type defined one namespace (`SRC`, `CMP`, `OBJ`, `RTE`, `CLM`, `ABS`, `BAP`), declared each record once "in the member that established it", and stated that the epistemic lens "proposes new records under `EPI-` IDs and declares none"; the coordinator registered them in the runtime report.
- The memory report type had the specialist declare `MEM-` proposals in its local report; finalization mapped them by exact token to canonical IDs from the overview's Reconciliation table (`specialist proposal | canonical record | disposition`), turned re-declared seeds into `On <ID>` annotations, removed rejected proposals, and pinned the local report as `finalized-from`.
- The epistemic report type's member declared no records and held no evidence passages.
- `src/commonplace/lib/agentic_records.py` accepted `MEM-` only in declarations of the local report and reported any `MEM-` or `EPI-` ID outside a Reconciliation section as an unintegrated proposal.
- The code-scheduled definition (`src/commonplace/lib/agentic_workflow.py`) spent, per reconciliation round, a `runtime-final` job (declare registered `EPI-` records, retain their passages, apply amendments) and an `epistemic-final` job (remap `EPI-` IDs), and validated the reconciliation by a trial finalization of the memory report.
- One retained set on main used the old grammar: `AAS-2026-09-28-pageindex-01`, deleted at adoption with its generated review.
