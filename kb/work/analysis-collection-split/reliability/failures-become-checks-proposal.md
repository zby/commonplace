# Failures become checks proposal

Agent draft, 2026-10-04, at the operator's request. Awaiting adoption.
Authorizes nothing.

## Revise after named record IDs

The operator decided on 2026-10-04 to implement
[short named record IDs](./short-named-record-ids-plan.md) first. Revise this
proposal against the implemented state before adopting it:

- The record-range failure is then removed at its cause, not checked. The
  range check remains only for `SRC-*` IDs. Update the current-state section
  and use this as the worked example of the "remove" disposition.
- New failure classes enter the register: misspelled or unresolved names,
  an ID that extends another ID, and a vague group phrase replacing explicit
  membership. The first two are checkable; the third is not.
- The cited-identifier check must not treat a named record ID as a source
  identifier.

## Problem

After each run the method has been repaired mostly by adding instruction
text. `worker-rules.md` grew about 45% in three days. Added text has two
weaknesses. Every worker pays for it in every job, whether or not the mistake
would have occurred. And it helps only if the worker applies it: the audited
runs show rules that were read and then not applied when writing.

[Oracle accumulation](../../../notes/oracle-accumulation-improves-the-selection-environment.md)
states the alternative. A failure can be retained as a lesson, which helps
only when it is delivered and applied, or as a check, which runs against
every output in its scope. A check costs worker input only when the mistake
happens.

## Current state (as of 2026-10-04)

Code checks exist for: member schema and frontmatter; record syntax, ID
ranges, part relations, prefixes and duplicates; cross-member reference
resolution; route fields and conclusion statuses; epistemic ledger syntax and
controlled values; quotation and source anchors; member identity; the memory
profile's structure and cited records.

The range check shows both the value and the limit of a check. It was added
after the first run. Ranges still appeared in later jobs, but each was
refused and corrected instead of reaching the accepted set. A check makes the
accepted output reliable. It does not by itself stop the attempt from failing.

Observed failures with no check today:

| Failure | Checkable by code? |
|---|---|
| Ledger cells holding the wrong category of reference | Yes: column category conformance. Already item 6 of the Sol run follow-up plan. |
| A cited code identifier that does not exist in the source | Yes: every identifier a record names in code formatting occurs in the frozen source. |
| A required assessment missing from synthesis | Yes, as presence of the section or labelled statement. Not its adequacy. |
| A classification with an added condition (`decay`) | No. Semantic. |
| Parts with different update semantics combined | No. Semantic. |
| Source register overstating inspection | Partly: listed paths exist. Not whether they were inspected. |

## Proposal

1. **Keep a failure register for the method.** One row per distinct observed
   failure: what happened, in which job, how often, how it was caught, and its
   disposition. It replaces ad hoc repair lists across audits.
2. **Give each failure one disposition, in this order of preference:**
   - *Remove the obligation* (see [code-owned bookkeeping](./code-owned-bookkeeping-proposal.md)).
   - *Check*: a deterministic check with a refusal that says what to do.
   - *Template*: an output form that makes the mistake hard to write.
   - *Instruction*: text at the step where the worker writes the affected
     output. Only when none of the above is possible.
   - *Accept*: record the limit and its cost; revisit on recurrence.
3. **When a check covers a rule, shorten the instruction** to what the worker
   needs to avoid the refusal. Do not keep the long form "to be safe".
4. **State each check's warrant.** A check establishes form or conformance,
   not truth or relevance. Its refusal message must not claim more.

## Constraints

- A check must have a typed target: a named field, column, section or record
  kind. Do not add pattern checks over free prose; the earlier range check
  produced a false positive on ordinary `to` phrasing before it was narrowed.
- No semantic judgment is moved into code. Semantic failures stay with
  independent verification.
- A check that refuses valid output is a defect of the same weight as a
  missed error. Test each check against the retained sets before adoption.

## Check before adoption

Build the register from the three audited runs. If most rows are semantic,
this proposal changes little and the effort belongs elsewhere. For the
checkable rows, run each candidate check over the retained sets: it must flag
the recorded failure and pass the accepted outputs. The identifier check is
the first candidate, because it is cheap and its failure reached
reconciliation.

## Costs and risks

- Checks accumulate too. Each needs a test, an owner and a removal condition
  when the method changes under it.
- A passing check can be read as assurance about content. The member's
  "Limitations and checks" section must keep the distinction.
- More refusals per attempt until workers adapt. This proposal therefore
  depends on [structured recovery](./structured-recovery-proposal.md) to keep
  a refusal cheap.
