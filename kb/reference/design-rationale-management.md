---
description: "Where to recover the reasons for a Commonplace design choice, what an ADR records, and why the implementation alone cannot tell a maintainer which alternatives were rejected."
type: types/note.md
---

# Design rationale management in Commonplace

When reconsidering a Commonplace design, start with the contract or code to establish **what would change**. To recover **why that design was chosen**, look for the decision record. For example, the collection templates show what a new project can copy. [ADR 069](./adr/069-collection-contract-bundles-become-one-time-prototypes.md#considered-alternatives) explains why Commonplace does not synchronize those copies: later framework updates would compete with the destination project’s authority over its own contract.

## Where to look

| State of the design | Where to look | What the record can tell you |
|---|---|---|
| Still being explored | A named workshop under `kb/work/` | Which problem prompted the work, what has been tried, and what remains uncertain. A workshop is temporary. |
| Proposed but not adopted | A [design proposal](./types/design-proposal.md) | The alternatives, their trade-offs, and what adoption would commit the project to. A recommendation is not a decision. |
| Implemented | An [architecture decision record (ADR)](./types/adr.md) | The choice and its consequences. For decisions dated 2026-07-25 or later, the contract requires a **Considered alternatives** section; it may explicitly say none were developed. |
| In use now | The applicable collection contract, type spec, instruction, validator, or package code | What a reader or program acts on today. Check amendments and later decisions before treating an older ADR as a description of current behavior. |
| Rejected or replaced | The decision’s alternatives, a superseding ADR, or the implementing commit | An explicit reason if someone recorded it. A diff alone shows what changed, not why another option lost. |

These are places to look, not required stages. A local convention may stay local; a validator fix need not begin with a proposal. Even a complete ADR helps only if the maintainer can find it from the behavior under review. Commonplace does not require every implementation to link back to its decision, or every decision to link back to its originating evidence. When a link is missing, search for the behavior or the change in Git; distinguish a recovered reason from one that merely fits the result. For the reverse task—deciding where to put new material—use [content routing](./content-routing.md).

## What the Epistack casework added

The `epistack-casebooks` work raised a question about reuse: was a feature necessary because a consumer depended on it, required only in that project, or simply chosen from several workable options? A later maintainer could mistake a local choice for a requirement elsewhere. The casework raised that risk; it did not demonstrate that recording the distinction changed a subsequent decision.

## Open questions

- In a worked reuse comparison, does preserving inherited constraints, local requirements, and free choices change what a later project adopts? The intended source of a comparison is the Epistack casework; none is documented here yet.
- For one ordinary Commonplace decision, can a later reader recover the original constraints and alternatives from the implementation, including why a local choice was later promoted, if it was? Trace what the reader actually finds, including any stage skipped or link missing.
