---
description: "Proposal: make the memory and epistemic lenses' prefixed record IDs canonical, so no step renames proposals, each lens declares its own records, and reconciliation keeps only merges, conflicts, amendments and synthesis"
type: reference/types/design-proposal.md
---

# Lens-prefixed canonical record IDs

An analysis set has one record namespace, but three passes add to it: the runtime pass and the two lenses, which run in parallel. Today only the runtime pass mints canonical IDs. The lenses propose records under local `MEM-` and `EPI-` IDs, and a reconciliation maps each proposal to a canonical ID; code or a job then rewrites the lens output with the mapped IDs. The first code-scheduled run (`AAS-2026-09-29-instinctual-memory-01`) failed in that rewriting: ten records the epistemic lens proposed were registered but declared in no member, so the set did not validate. Most of the jobs and checks around reconciliation exist to carry out the renaming.

## Current state (as of 2026-09-29)

- The [overview type](../../types/agentic-system-analysis-overview.md) defines one namespace (`SRC`, `CMP`, `OBJ`, `RTE`, `CLM`, `ABS`, `BAP`), declares each record once "in the member that established it", and states that the epistemic lens "proposes new records under `EPI-` IDs and declares none"; the coordinator registers them in the runtime report.
- The [memory report type](../../types/agent-memory-analysis-report.md) has the specialist declare `MEM-` proposals in its local report; finalization maps them by exact token to canonical IDs from the overview's Reconciliation table (`specialist proposal | canonical record | disposition`), turns re-declared seeds into `On <ID>` annotations, removes rejected proposals, and pins the local report as `finalized-from`.
- The [epistemic report type](../../types/agentic-system-epistemic-report.md) member declares no records and holds no evidence passages.
- `src/commonplace/lib/agentic_records.py` accepts `MEM-` only in declarations of the local report and reports any `MEM-` or `EPI-` ID outside a Reconciliation section as an unintegrated proposal.
- The code-scheduled definition (`src/commonplace/lib/agentic_workflow.py`) spends, per reconciliation round, a `runtime-final` job (declare registered `EPI-` records, retain their passages, apply amendments) and an `epistemic-final` job (remap `EPI-` IDs), and validates the reconciliation by a trial finalization of the memory report.

## Options

**A. Keep proposals and mapping.** No contract change. The renaming stays a step that can leave a registered record undeclared or a reference dangling; the definition keeps its validators for that.

**B. Canonical ID blocks per lens.** Before the lenses start, code gives each one a numeric block per kind (memory `OBJ-100…`, epistemic `OBJ-200…`), and the lenses declare canonical IDs directly. No renaming; IDs stay in one grammar. Blocks are arbitrary numbers a reader cannot tell apart from runtime IDs, and a block can overflow.

**C. Lens prefixes are canonical (operator preference, 2026-09-29).** Each pass declares its records under its own prefix: the runtime pass bare `OBJ-1`, the memory lens `MEM-OBJ-1`, the epistemic lens `EPI-OBJ-1`. The prefix is part of the canonical ID and stays for the life of the set. Each lens declares its records in its own member, with the passages that support them. Parallel lenses cannot collide, and nothing is renamed. The ID says which pass established the record.

## What option C changes

- **Set grammar.** A canonical ID is `[MEM-|EPI-]KIND-N`. Declarations stay one per record, in the member of the pass that established it: bare IDs in the runtime member, `MEM-` in the memory member, `EPI-` in the epistemic member. The unintegrated-proposal check goes away.
- **Duplicates.** When two passes established the same thing, both records stay, and the reconciliation supersedes one with an amendment in its declaring member: `Amendment: MEM-RTE-3 is superseded by RTE-7`, with the evidence for the identity. References to the superseded ID remain resolvable. Split records work as today.
- **Memory member.** With nothing to map, finalization reduces to appending the reconciliation's amendments to the specialist's records and to any re-declared seed; whether the member can be the local report byte for byte, with the amendments kept elsewhere, is a free choice below.
- **Epistemic member.** It declares its own records and retains their passages, so the epistemic type loses "declares no records and holds no evidence passages". Targeted-read requests to the coordinator go away.
- **Reconciliation.** The mapping table goes away. What remains is judgment: supersession of duplicates, anchored conflicts, amendments to any pass's records, independent convergence, the memory-comparison check against the whole set, and the synthesis and limitations.
- **Definition.** `epistemic-final` goes away. `runtime-final` keeps only applying amendments to runtime records, or goes away too (see free choices). The trial finalization in the reconciliation's validator becomes a reference check.

## Forces

- The failure it removes is structural: a record one pass established cannot fail to be declared, because the pass that established it declares it.
- IDs get longer, and a reader sees three families in one namespace; in exchange each ID says where it was established.
- It touches three shipped type specs, their schemas and the record validator, and publication's `finalized-from` check. Retained sets written under the current grammar hold no lens-prefixed canonical IDs, so accepting the new grammar does not invalidate them; whether they must still validate under the old rules is a separate choice.
- A lens can now declare a record that duplicates a runtime record without anyone deciding; the reconciliation must look for duplicates, where today the mapping forces a decision per proposal.

## Free choices

- Where amendments to another pass's records live: in the declaring member (as today, which needs a job that writes into that member after reconciliation), or in the overview's Reconciliation, which the whole set can cite (no member rewriting after the lenses).
- Whether the memory member is the specialist's report unchanged, pinned by hash, or a finalized copy with amendments appended.
- Whether the runtime member is written once, before the lenses, and never rewritten.

## Operativity

The change is consumed by the record validator and publication checks (code), the three type specs, and the job instructions of `kb/instructions/analyse-agentic-system/jobs/`, which the workers load with binding force. It takes effect for the next run opened after the commit that lands it, since a run pins its method commit.

## Adoption criteria

The operator selects C and the free choices; one run through the code-scheduled definition then publishes with no ID renaming step and no job that exists only to declare or remap another pass's records.
