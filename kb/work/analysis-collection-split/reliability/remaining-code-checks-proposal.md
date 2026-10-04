# Remaining code checks proposal

Agent draft, revised 2026-10-04 at the operator's request. Awaiting adoption.
Authorizes nothing. It replaces two earlier drafts, "code-owned bookkeeping"
and "failures become checks", which git history keeps.

## Why this is now a short list

The two earlier drafts aimed at mechanical failures: work with exactly one
right answer that analysts still did by hand, and failures that no check
caught. Two redesigns have since removed the most frequent of them at their
cause:

- [Named record IDs](./short-named-record-ids-plan.md), implemented: record
  ranges cannot be written, and numbering is gone.
- The [analyst acceptance check](./analyst-acceptance-check-plan.md), adopted
  and planned: analysts write path-only quotations and run the acceptance
  check on their draft. No selection files, no JSON batch, no copied
  citation, and every check below becomes available to the analyst before
  submission.

What is left is smaller and less certain. This proposal lists it, orders it,
and names the test that decides whether more exists.

## The principle that stays

When a failure is observed, choose its repair in this order:

1. **Remove** the obligation or the pressure behind it, as the two redesigns
   did. Use [review design pressure behind recurring errors](../../../instructions/review-design-pressure-behind-recurring-errors.md).
2. **Code does it.** Where exactly one correct value exists given the job's
   inputs, code writes or supplies it.
3. **Code checks it.** A deterministic check with a refusal that says what to
   do.
4. **Instruction**, at the step where the worker writes the affected output.
5. **Accept** the limit and revisit on recurrence.

A check costs worker input only when the mistake happens; added instruction
text costs input in every job
([oracle accumulation](../../../notes/oracle-accumulation-improves-the-selection-environment.md)).
A check makes the accepted output reliable. It does not stop a draft from
failing it. What a failure costs is decided by the
[analyst acceptance check](./analyst-acceptance-check-plan.md): the analyst
runs every check on its draft and repairs what it reports.

## What remains

Ordered by expected value. Each needs its consumer confirmed in code before
it is built.

| # | Candidate | Kind | Evidence |
|---|---|---|---|
| 1 | Every code identifier a record cites occurs in the frozen source. | Check | A wrong identifier, `summary_valid_at`, reached reconciliation in the stopped Graphiti run. |
| 2 | An inventory of the files in the frozen checkout, supplied with the packet. | Code supplies | Wrong-path source reads in the Graphiti run. |
| 3 | An index of every declared record, with kind, member and part relation, supplied to reconciliation and verification. | Code supplies | No failure observed. Named IDs removed the order and count that numbers gave, so completeness now needs a list. |
| 4 | Identity fields in member frontmatter, `run-id` and `reviewed-boundary`. | Code writes | Checked today; no failure recorded in the audits. Under the acceptance check plan the message states the expected value, which may be enough. |
| 5 | Ledger cells hold only claim IDs or `none`. | Check | Five cells in the Graphiti run. Also item 6 of the Sol run follow-up plan. |
| 6 | A required assessment is present in synthesis. | Check, presence only | One synthesis blocker in the second Dynamic Cheatsheet run. |
| 7 | Frontmatter written as YAML by hand. | Accept for now | One broken indentation, caught by validation. |

Not checkable by code, and left to independent verification: a classification
with an added condition, parts with different update semantics combined, and
a source register that overstates what was inspected.

## The test that decides whether more exists

The candidates above are those found by reading code and audits. Whether the
roles hold more bookkeeping is unknown. The
[complexity measurements](../evidence/complexity-measurements.md) list every
output obligation per role, in `evidence/complexity-measurements.json` under
`obligations`. That inventory predates the collection split, the profile job
and named IDs, so refresh it for two roles first.

Classify each obligation of the memory and reconcile roles as semantic,
bookkeeping or mixed. Bookkeeping means code can compute the one correct
value from the job's inputs. If few are bookkeeping, close this line of work:
the remaining load is semantic, and reliability must come from elsewhere.

## The failure register

Keep one register for the method: a row per distinct observed failure, with
the job, the count, how it was caught, and its disposition under the order
above. It replaces repair lists scattered across audits, and it is what
shows whether a redesign worked. Its first rows are the failures the two
redesigns removed, the candidates above, and the new classes the redesigns
introduce: misspelled record names, an ID that extends another ID, vague
group phrases, and quotations not found or ambiguous.

Where it lives is decided at adoption. It is method-maintenance material and
must not enter a worker's input.

## Constraints

- A check has a typed target: a named field, column, section or record kind.
  No pattern checks over free prose; an earlier range check refused ordinary
  `to` phrasing before it was narrowed.
- No semantic judgment moves into code. A wrong computed value is worse than
  a refused one, because nothing rejects it.
- A check that refuses valid output is a defect of the same weight as a
  missed error. Test each against accepted outputs before adoption.
- A supplied input counts against the worker's read budget. It must replace
  discovery work, not add to it.
- The identifier check must not treat a named record ID as a source
  identifier.

## Check before adoption

1. Do the two-role classification. Stop if little is bookkeeping.
2. For candidate 1, run the check over accepted members: it must flag the
   recorded wrong identifier and pass every accepted citation. The retained
   sets use numeric record IDs and are valid input for this test, since it
   concerns source identifiers.
3. Build at most the first two candidates, then compare refusals and failed
   reads on the next commissioned run against the recorded baseline.

A fixture shows that a check behaves as specified. It does not show that
analyses improve.

## Costs and risks

- Checks accumulate as instructions did. Each needs a test and a removal
  condition when the method changes under it.
- A passing check can be read as assurance about content. It establishes
  form or conformance only.
- A supplied inventory or index can be wrong for an unusual source, and the
  worker may trust it. It must come from the frozen checkout the run
  registered.
