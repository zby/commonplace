---
description: "Job of an analyse-agentic-system run: reconcile the runtime member and both lenses, and write the overview's reconciliation, synthesis and limitations"
type: types/instruction.md
---

# Reconcile the lenses and write the synthesis

Write the output your prompt names, with exactly these sections, which go into the overview unchanged; the [overview type](../../../types/agentic-system-analysis-overview.md) fixes what each holds:

```markdown
## Reconciliation

## Bounded synthesis

## Limitations
```

## Reconcile

Resolve proposed records into canonical IDs. Map exact identifier tokens rather than substrings, and check that every mapped target is declared and unique. The specialist proposal mapping is the table the overview type fixes, `specialist proposal | canonical record | disposition`, with one row for every proposal ID in the memory report; `rejected` removes a proposal. Epistemic `EPI-` proposals are mapped in the same way in a second table, `epistemic proposal | canonical record | disposition`.

State each correction to a canonical record as an `Amendment:` entry naming the record, preserve anchored conflicts, and report independent convergence only when the lenses reached it independently. Recheck shared-route ownership. Attach the admission fields of memory routes from the specialist's findings rather than tracing those mechanisms twice. The specialist's `memory-comparison` profile stays in the memory member with its scope, per-value evidence bases and records, coverage assessments, uncertainties, and rationale preserved; check it against the records of the whole set. Each specialist quote stays in the memory member beside the record it supports; a runtime record cites that record rather than repeating the passage. Do not draft a second memory analysis, and do not silently strengthen the specialist's findings.

Every record you register from an `EPI-` proposal, every amendment to a record the runtime draft declares, and every passage the epistemic draft asks to retain for such a record is written into the runtime member by a later job, from what you state here; give each new record its canonical ID, kind and identity in the epistemic table's row or under it. A passage for a record the memory report declares is a return to the specialist.

Code finalizes the memory member from your table and appends to your Reconciliation the local report's path, its SHA-256, and the mechanical edits finalization made. Do not write those yourself. If the table leaves a proposal unmapped, or rejects one that other findings still reference, your output is refused with the reason.

## Return findings to the specialist

When a substantive conflict needs the specialist, add a fourth section, `## Returned to the specialist`, listing each returned finding with its IDs and evidence anchor. Code then runs a correction round of the memory specialist and gives you its report in the next reconciliation. Your prompt says whether this round may return findings. In the last round it may not: retain each unresolved conflict as explicit uncertainty in the Reconciliation and the Limitations. A malformed citation in the specialist report is also a return, not something you fix.

## Synthesize

Write the Bounded synthesis from the reconciled records, organized around the system's operational progression rather than by lens, citing member records rather than restating them. Write the Limitations as the overview type's rows; use `none` only after checking the whole set.
