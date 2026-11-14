# Draft: the first variant, fix findings

## Status

Drafted on 2026-11-14 as the first variant of the
[one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md).
It recomposes [fix review warnings](../../instructions/fix-warnings/fix-review-warnings.md),
the one improvement procedure that leaves no run record today, over the
drafted [run type](./improvement-run-type.md),
[answers schema](./improvement-run-answers-schema.md) and
[edit-operation type](./edit-operation-type.md). It has not been run.
Writing it exposed three gaps in those drafts, listed
[at the end](#what-writing-the-variant-exposed).

The section "The variant" is the instruction as an agent would follow it.
The rest is commentary for the workshop.

## What changes against the fix procedure

| | Fix review warnings today | This variant |
|---|---|---|
| Record | One free-form report per note, overwritten by the next fix | One run directory per run, kept |
| Higher-order check | None | Runs first, once it exists as an atom |
| A finding the agent does not fix: judged spurious, unsure, or needing a human decision | `rejected` or `deferred` row in the report | One kind of record: an open item in the answers, with the agent's view, left for later |
| The decision on an open item | Not recorded | The item's state, its reason and who decided |
| Texts before and after | The checkout and Git | Stored in the run |
| What is unchanged | The entry queue, the strategies, minimal edits, the re-review | |

The fix procedure let the agent reject a finding by its own judgment. The
operator decided on 2026-11-14 that the line between a finding the agent
thinks is wrong and one it is unsure about is a matter of degree, so the
variant has one set. The agent either fixes a finding or leaves it open,
and says in the open item what it thinks.

## The variant

**Goal.** The note no longer has the problems its fresh review warnings
name, where a change of framing or accuracy can remove them, and the run
leaves a record from which the gates, the fix strategies and the operator's
decisions can each be assessed later.

**Use when** a note has fresh `warn` or `fail` review results and the
operator wants them worked. The operator need not be present: the run
decides nothing it is unsure of.

**The rule of the variant,** set by the operator on 2026-11-14: be
conservative, and note everything. The agent edits only where it is sure
the finding applies and the fix is safe. Every other finding is left
unchanged and recorded as an open item, with the agent's view of it. Open
items are part of the
[unresolved frontier](../../reference/definitions/unresolved-frontier.md):
they wait there, findable per note, until the operator or a later
workflow decides them. The
agent closes no finding by its own judgment, and no finding is dropped
without a record.

### Before starting

1. Run `commonplace-review status <note> --fresh --outcome warn fail --json`.
   With no rows, report that there is nothing to fix and stop; no run is
   created.
2. Check that the note has no uncommitted change. If it has, stop and ask.
3. Run `commonplace-review decisions --note <note>` and read the open items
   of earlier runs on this note. Handle each as the answers schema's
   closing rules say: re-propose it in this run or expire it, with a reason.
4. Create the run directory, write the start text to `texts/`, and write
   the report with `ending: open`.

### Higher-order check

5. Run the higher-order check on the note through `commonplace-review`
   and cite its result in the findings.
   - **Strong proposal:** record it as a pending item, set `ending: stopped`,
     present it to the operator and end the run. Make no edit.
   - **Weak proposal:** record it as a pending item and continue.
   - **No proposal:** continue.

   Until the check is extracted from its
   [evaluation workshop](../higher-order-check-evaluation/README.md) as an
   atom, skip this step and say in the report that it was skipped.

### Findings

6. Read each row's result file and list its findings. For each finding,
   read the flagged passage and enough context to follow the argument, then
   give it one of two dispositions:
   - **fix:** the agent is sure the finding applies, and a change of
     framing or accuracy resolves it without changing the argument;
   - **leave open:** everything else. The finding looks mistaken, the fix
     would change the argument, the choice is not the agent's, or the agent
     is not sure.
7. Write every finding to the findings member with its citation and
   disposition.

### Edits

8. Apply the findings marked fix in one run of the fix operation,
   [fix a finding by a named strategy](../../instructions/fix-warnings/fix-strategy-taxonomy.md).
   Each fix is the smallest edit that resolves its finding and touches only
   the flagged passage. Record on each finding the strategy used, or
   `new-pattern` with a line describing it.
9. Store the resulting text under `texts/` and add one entry to the edit
   chain. If the note carries `user-verified` and any fix was applied,
   remove the field.

### Open items

10. For each finding left open, write an item in the answers: the passage,
    the finding, and the change that would act on it. In the item's agent
    note, say what the agent thinks and how sure it is: that the finding
    is mistaken and on what evidence, that the change is right but not the
    agent's to make, or that it cannot tell. Name alternatives where there
    are several. The item is `pending`. Write it so that a reader who has
    only the item and the note can decide.
11. Do not wait for the operator. If the operator is in the session and
    wants to answer now, present the items one at a time and record each
    answer with its reason; an approved response is applied as a further
    edit that cites the item. Otherwise the items stay pending and the run
    goes on to closing.

### Closing

12. If any edit was applied, re-review the note with
    `commonplace-review run gates <note> --all-gates` and cite the new
    results in the findings. Do not fix what the re-review finds; a new
    warning is input to the next run. Report separately any pair that
    passed before and warns now.
13. Run `commonplace-validate` on the note and on the run directory.
14. Complete the report: set `final-sha256` and the ending, `applied` when
    no item is open and `partly-applied` otherwise. In the body, state what
    was fixed, what was left open and why, and what the re-review returned.
15. Show the operator the diff. The operator's commit is the publication;
    do not commit unless asked.

### Bounds

- Do not change the title, the H1, the type or the note's claims. A finding
  that can only be resolved that way is left open.
- Do not improve text that no finding flagged.
- Do not remove examples; frame them.
- Do not edit result files.
- One edit round per run. The variant does not loop on its own re-review.

## What the variant composes

| Step | Atom | Kind | Exists today |
|---|---|---|---|
| 1, 12 | The gate catalog, through the gate sweep | Review | Yes |
| 5 | The higher-order check | Review | No; in calibration |
| 8 | Fix a finding by a named strategy | Edit, `decision: none` | As a taxonomy, not yet typed |
| 10 | Record an open item | Stop | No; the answers schema is its form |
| 11 | Present, ask and record, when the operator is present | Stop | Only for strike lists, as [resolve a strike list](../../instructions/simplification-passes/resolve-a-strike-list.md) |

Step 6, the disposition of each finding, is the variant's own judgment and
not an atom. It is where this variant differs most from the full pass,
which takes its dispositions from a packet.

## What writing the variant exposed

1. **The findings member needs a disposition per finding.** The run type
   draft listed one entry per review result. The fix case decides per
   finding, and a result can hold several. Each entry therefore needs the
   finding's text, a disposition of `fixed`, `open` or `none`, the strategy
   when fixed and the item when left open. This member then replaces the
   fix report's mapping table. The run type draft is updated to say so.
2. **An item offers one proposal; a deferred finding offers alternatives.**
   The answers schema models accepting or rejecting one proposal. A finding
   left open often has two or three acceptable responses. The variant
   states the recommended response as the proposal and the alternatives in
   its text; an operator who prefers an alternative rejects the item with
   that as the reason, and the agent writes a new item. A `chosen` field
   would be shorter and is left out until a run shows the detour is common.
3. **An item needs a place for the agent's view.** With one set of
   unfixed findings, the item's proposal is the change that would act on
   the finding, and the agent's opinion of the finding is separate from
   it. The answers schema gains an optional `agent-note`. A decider who
   agrees that a finding is mistaken rejects the item, and the reason
   becomes evidence about the gate. The agent makes no decision that is
   recorded only on a finding, so the answers hold every decision and the
   decisions command reads one member.

## Before a first run

- The run types must exist under `kb/reports/types/`, or step 13 cannot
  validate the run directory. Registering them experimentally is therefore
  a precondition of the first run, not its consequence.
- The fix operation needs its typed file, or the run cites the taxonomy as
  it stands.
- Step 3 reads earlier runs through `commonplace-review decisions`, which
  does not read improvement runs yet. For the first run there are no
  earlier runs, so the gap does not block it; it blocks the second.
- A note with fresh warnings. The operator need not be present.

## Open choices

1. **How many open items a conservative run produces.** Every false
   warning is now an open item. The agent's note makes most of
   them quick to decide, but the count is unknown until the first run. If
   it is high, the remedy is to fix the gates that produce the false
   warnings, which the rejections with their reasons point at.
2. **One edit entry for all fixes, or one per fix.** One keeps the text
   chain short. One per fix would let each strategy's effect on the review
   results be read alone, at the cost of a stored text per fix.
3. **Whether the re-review belongs to the variant.** It doubles the review
   cost of a run. The fix procedure lets the operator skip it; the draft
   requires it, because without it the run cannot say whether the fixes
   worked.
