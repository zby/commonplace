---
description: "Job of an analyse-agentic-system run: reconcile the runtime member and both lenses, and write the overview's reconciliation, synthesis and limitations"
type: types/instruction.md
---

# Reconcile the lenses and write the synthesis

Write the output your prompt names, with exactly these sections. The last three go into the overview unchanged; the [overview type](../../../types/agentic-system-analysis-overview.md) fixes what each holds:

```markdown
## Description

## Reconciliation

## Bounded synthesis

## Limitations
```

## Reconcile

Every pass has declared its own records: unprefixed IDs in `output/runtime.md`, `MEM-` IDs in the memory report your prompt names, `EPI-` IDs in `output/epistemic.md`. No member is rewritten after the pass that wrote it, and nothing is renamed. Your Reconciliation is where the set's judgments about those records live.

Look for records two passes established for the same thing, and supersede one with the evidence for the identity: `Amendment: MEM-RTE-3 is superseded by RTE-7`, citing the anchors that show both trace the same thing. Both records stay declared. State each correction to any pass's record as an `Amendment:` paragraph naming the record by full ID, with the superseded value, replacement value, evidence anchor and affected findings. Preserve anchored conflicts, and report independent convergence only when the lenses reached it independently. Recheck shared-route ownership. Attach the admission fields of memory routes from the specialist's findings rather than tracing those mechanisms twice. The specialist's `memory-comparison` profile stays in the memory member with its scope, per-value evidence bases and records, coverage assessments, uncertainties, and rationale preserved; check it against the records of the whole set. Do not draft a second memory analysis, and do not silently strengthen the specialist's findings.

Every ID you cite, in amendments too, must resolve in the set your output makes: the Source register, the runtime member, the memory report and the epistemic member. Your output is refused with the unresolved IDs otherwise.

## Return findings to the specialist

When a substantive conflict needs the specialist, add a fourth section, `## Returned to the specialist`, listing each returned finding with its IDs and evidence anchor. Code then runs a correction round of the memory specialist and gives you its report in the next reconciliation. Your prompt says whether this round may return findings. In the last round it may not: retain each unresolved conflict as explicit uncertainty in the Reconciliation and the Limitations. A malformed citation in the specialist report is also a return, not something you fix.

## Resolve a verification's blockers

When your prompt says the previous round's verification named blockers, its inputs include that verification and the set check. Resolve each blocker in what you write: correct the reconciliation, the synthesis or the limitations; amend or supersede a record through an `Amendment:` paragraph; or return it to the specialist when the memory report is at fault. The runtime and epistemic members are not rewritten; a blocker in one of them that no amendment resolves stays a limitation. The previous reconciliation is an input too: carry over what still holds.

## Synthesize

Write the Bounded synthesis from the reconciled records, organized around the system's operational progression rather than by lens, citing member records rather than restating them. Code also publishes it, with the Limitations, as the body of the public review, so it must read on its own: a reader has the cited IDs and links, not the members' context. Write the Limitations as the overview type's rows; use `none` only after checking the whole set.

Under Description write one sentence of 50 to 250 characters that describes the system's mechanism and its limits for retrieval. Code uses it as the `description` of the overview and of the public review.
