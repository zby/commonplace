---
description: "Proposal archive: 2026-09-26 pilot observation of mixed-strength memory profiles before ADR 093 adopted evidence per value"
type: reference/types/design-proposal.md
---

# Evidence granularity for memory-comparison counts

Adopted by ADR 093. This archive retains the dated observation; the decision and
considered alternatives live in the ADR.

## Current state (as of 2026-09-26)

The [result contract](../../../types/agentic-system-analysis-result.md#memory-comparison-fields)
requires the union of scoped values and the weakest evidence basis supporting
that union. The numerical analyzer admits known values at wired, observed, or
causally supported basis. It correctly excludes a complete set whose basis is
only afforded; it cannot recover a stronger member from the canonical prose.

The retained [Mem0 result](../../../reports/retained/agentic-system-analysis/AAS-2026-09-26-mem0-01/result.md)
records automatic extraction as wired and caller-authored direct writes as
afforded. Their shared write-agency profile is therefore afforded. Its wired
internal push and afforded application pull similarly share an afforded
read-back profile. The [Dynamic Cheatsheet result](../../../reports/retained/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-01/result.md)
combines automatic curator writes with afforded manual initialization. A
membership query for wired automatic writing excludes both rows, despite the
more specific evidence retained in their records. This is a consequence of
the current aggregation contract, not a parser malfunction.
