---
description: "Vocabulary, judging norms and register ownership shared by the jobs of an analyse-agentic-system run that judge evidence"
type: types/instruction.md
---

# Judge evidence in an analysis run

Load the [overview type](../../../types/agentic-system-analysis-overview.md) before recording findings: its set-wide sections own the namespace, the declaration and annotation grammar, the conclusion-status values, the source anchors and the quotation contract for every member. The [runtime report type](../../../types/agentic-system-runtime-report.md) owns the runtime account, probe evidence and record fields, and the theory-builder terms; the [memory report type](../../../types/agent-memory-analysis-report.md) owns the `memory-comparison` contract; the [epistemic report type](../../../types/agentic-system-epistemic-report.md) owns the six epistemic blocks.

## Judging norms

- Never upgrade context presence to activation, a claim to an affordance, an affordance to wiring, wiring to observation, observation to causality, or curation to warrant.
- Give each theory-builder condition, and learning, reflection and autonomy, its own conclusion status from its own evidence, under the [Shared records](../../../types/agentic-system-runtime-report.md#shared-records) rules for theory routes.
- When describing revision selection, write that it prefers reach among revisions that fit the evidence, not "reach rather than fit". This applies whether or not the route is reflective.
- Describe every external mechanism in source-native terms before mapping it to Commonplace ontology. Explain the fit and mark partial or unresolved mappings. Do not turn omission of an open-ended mechanism into evidence of absence. An `uninspected` gap or a casual search miss is a limitation, not an `ABS-*` record. Create an `ABS-*` record only for a load-bearing absence claim; it always states its searched boundary.

## Register ownership

Each pass declares the records it establishes, in its own member, under its own prefix: the runtime job unprefixed IDs, the memory lens `MEM-` IDs, the epistemic lens `EPI-` IDs. A lens annotates or cites another pass's records and never re-declares them. The prefix stays part of the ID, and no job renames or rewrites another's records. Allocate IDs monotonically within your prefix and never reuse one; gaps are harmless. Only the reconciliation amends a record, in the overview: it changes evidence or status without changing the referent, supersedes a duplicate, and splits a combined record only by giving the parts new IDs and marking the original superseded.
