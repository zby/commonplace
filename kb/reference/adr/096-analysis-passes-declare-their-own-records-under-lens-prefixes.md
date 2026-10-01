---
description: Each pass of an agentic-system analysis declares its own records under a canonical lens prefix, so no step renames IDs and reconciliation keeps only judgment
type: reference/types/adr.md
status: accepted
---

# 096 — Analysis passes declare their own records under lens prefixes

**Status:** accepted
**Date:** 2026-09-29

**Amended 2026-10-01:** [ADR 098](./098-separate-analysis-reconciliation-from-synthesis.md) moves amendments to a separate reconciliation member and separates public synthesis from record reconciliation. Lens-prefixed identities and immutable analyst members remain in force; the location and combined-writing descriptions below record the prior decision.

## Context

An agentic-system analysis set has one record namespace, and three passes
add to it: the runtime pass and the memory and epistemic lenses, which run
in parallel. Before this decision only the runtime pass minted canonical
IDs. The lenses proposed records under local `MEM-` and `EPI-` IDs, the
reconciliation mapped each proposal to a canonical ID in a table, and code
or a job rewrote lens output with the mapped IDs. Memory finalization
renamed tokens, converted merged declarations to annotations, removed
rejected proposals and pinned the local report as `finalized-from`. Each
reconciliation round then ran a `runtime-final` job, which declared
registered `EPI-` records in the runtime member, and an `epistemic-final`
job, which remapped the epistemic member's IDs.

The first code-scheduled run (`AAS-2026-09-29-instinctual-memory-01`)
failed in that renaming: ten records the epistemic lens proposed were
registered but declared in no member, so the set did not validate. The
failure is structural: a record can go undeclared whenever a pass other
than the one that established it must declare it.

## Decision

The prefix of the pass that established a record is part of its canonical
ID for the life of the set: none for the runtime pass (`OBJ-1`), `MEM-`
for the memory lens (`MEM-OBJ-1`), `EPI-` for the epistemic lens
(`EPI-OBJ-1`). Each pass declares its records in its own member, with the
passages that support them. The epistemic member gains a
`## Shared records` section. Nothing is renamed.

No member is rewritten after the pass that wrote it. The runtime member
is written once, before the lenses. The memory member is the specialist's
accepted report, copied byte for byte; it keeps only the
`canonical-register-sha256` pin to its frozen input.

Amendments to any pass's records live in the overview's
`## Reconciliation`, as `Amendment:` paragraphs naming the record by full
ID. When two passes established the same thing, both records stay
declared, and the reconciliation supersedes one:
`Amendment: MEM-RTE-3 is superseded by RTE-7`, with the evidence for the
identity. References to either ID keep resolving.

The reconciliation keeps only judgment: supersessions, amendments,
anchored conflicts, independent convergence, ownership checks, the
memory-comparison check against the whole set, and the synthesis and
limitations. Its validator checks that every ID it cites resolves in the
set it will make. Each pass's validator checks that its member's citations
resolve against the set so far.

This removes the mapping table, memory finalization and its
`commonplace-agentic-analysis-finalize memory` command, the `finalized-from`
field, member `## Amendments` sections, the unintegrated-proposal check,
and the `runtime-final` and `epistemic-final` jobs.

## Considered alternatives

**Keep proposals and mapping.** No contract change, but the renaming step
stays a place where a registered record can go undeclared or a reference
can dangle, and the definition keeps the jobs and validators that exist
only to guard it.

**Canonical ID blocks per lens.** Code would give each lens a numeric block
per kind before the lenses start (memory `OBJ-100…`, epistemic
`OBJ-200…`), and lenses would declare canonical IDs directly. IDs stay in
one grammar, but a block is an arbitrary number a reader cannot tell apart
from a runtime ID, and a block can overflow.

**Amendments in the declaring member.** Keeping amendments beside the
record they correct needs a job that writes into every member after
reconciliation, which reintroduces a rewriting step per round. The
overview's Reconciliation is already where set-wide judgment lives and
can cite every member.

**A finalized memory copy with amendments appended.** It would keep the
memory member self-describing, at the cost of a second version of the
specialist's report and a pin between the two. With amendments in the
overview, the copy would differ from the report only by bookkeeping.

## Consequences

IDs get longer, and a reader sees three ID families in one namespace; in
exchange each ID says which pass established it. A lens can declare a
record that duplicates a runtime record without anyone deciding, so the
reconciliation instruction requires a search for duplicates, where the
mapping used to force a decision per proposal. A blocker in the runtime or
epistemic member that no amendment resolves stays a limitation, because
those members are not rewritten.

The one retained set written under the old grammar
(`AAS-2026-09-28-pageindex-01`) and its generated review were deleted
rather than migrated; a rerun under this contract replaces them. The
change takes effect for runs opened after the commit that lands it, since
a run pins its method commit. The decision is untested by a completed run:
its adoption test is one run through the code-scheduled definition that
publishes with no renaming step and no job that exists only to declare or
remap another pass's records.

This ADR adopts the design proposal *Lens-prefixed canonical record IDs*.
