# Structured recovery proposal

Agent draft, 2026-10-04, at the operator's request; current state rechecked
after named record IDs landed. Awaiting adoption. Authorizes nothing.

## Partly absorbed into a plan

The [analyst acceptance check plan](./analyst-acceptance-check-plan.md),
adopted on 2026-10-04, takes over item 1 below, reporting every independent
failure in one refusal, and gives the analyst the acceptance check as a tool
before submission. That reduces how often a refusal happens at all. What
remains proposed here: the three-part message form for all checks, code
fixing mechanical values, not repeating an identical refusal, and recording
refusals per rule. Reassess their value after the first run with the tool.

## Problem

Catching a failure is half of a repair. The KB's note
[enforcement without structured recovery is incomplete](../../../notes/enforcement-without-structured-recovery-is-incomplete.md)
observes that after a check fires, what happens next is usually left to the
agent's improvisation. In an analysis run, a refused output costs a full
worker attempt, and a job that runs out of attempts blocks the run.

## Current state (as of 2026-10-04)

Read from `src/commonplace/workflow/engine.py` and
`src/commonplace/lib/agentic_workflow.py`.

- A refused job is handed out again with a section "Why the previous attempt
  was refused" listing the refusal messages, and the preserved previous output
  as the baseline to amend.
- `retry_limit` is 1 and `repair_limit` is 1 by default. After the retry is
  refused, the job blocks.
- **Checks run in stages and stop at the first failing stage.** For an
  analyst's member, `pass_refusals` returns schema failures or reference
  failures first; only when those pass does it check member identity, then
  record prefixes, then quotations. A worker whose output has errors in two
  stages sees only the first, repairs it, and is refused again for the second.
  With one retry, that job blocks although each error was simple.
- Messages vary in how much they help. The unresolved-reference refusal now
  names the nearest declared ID, which is the three-part form proposed
  below. Others state only the mismatch, such as the member identity check.
- Refusals are not recorded in a form that allows counting by rule across
  runs.

Some staging is necessary: quotations cannot be checked in a member that does
not parse. Much of it is not: identity fields, prefixes and record syntax are
independent of each other.

## Proposal

1. **Report every independent failure in one refusal.** Run all checks whose
   preconditions hold and return their messages together. Keep staging only
   where a later check cannot run without an earlier one passing.
2. **Give each refusal message three parts:** the rule, the location (record
   ID, field, or line), and the repair action. Follow
   [error messages that teach](../../../notes/error-messages-that-teach-are-a-constraining-technique.md).
3. **Classify each check's recovery, and route by class:**
   - *Mechanical*: code can produce the correct value. Code fixes it and does
     not bounce the output. Example: an identity field that must equal a run
     parameter. The [remaining code checks](./remaining-code-checks-proposal.md)
     list the same field as a candidate for code to write outright.
   - *Local edit*: the worker amends the named location in the previous
     output. The current repair path, with better messages.
   - *Re-derive*: the failure shows the finding may be wrong, such as a
     quotation that does not occur in the source. The message tells the
     worker to reread the source and recheck the dependent claim, as the
     worker rules already require for quote repairs.
4. **Do not repeat an identical refusal.** If the retry fails the same check
   at the same location, the next message adds what the first lacked: the
   offending excerpt and a correct example. If it fails again, block with a
   report that names the rule, so the operator sees a method defect and not a
   worker defect.
5. **Record refusals per job** with rule, location, recovery class and
   attempt number, in run state. This is the measurement the failure
   register needs: which rules fail, where, and whether a repair worked.

## Constraints

- Code never edits analytical content. A mechanical fix applies only to
  values that are functions of run parameters.
- The repair scope rule stays: an orchestrating agent does not write a job's
  output. This proposal changes what code and the worker do, not that.
- Raising the retry limit is not part of this proposal. More attempts without
  better messages buy cost, not reliability.

## Check before adoption

Two checks need no model run:

1. Replay the refusals recorded in the audited runs against the proposed
   staging. Count how many attempts would have carried more than one failure
   class, and how many retries reporting them together would have saved. If
   almost every refusal had a single class, item 1 buys little.
2. Review every existing refusal message for the three parts and list those
   that lack a repair action. The list is the work.

Then compare attempts per accepted job on the next commissioned run against
the recorded baseline.

## Costs and risks

- Longer refusal messages cost input on a retry, when the worker is already
  loaded. Keep them to the failing locations.
- Reporting many failures at once can overwhelm a repair. If a refusal lists
  more than a handful, a fresh attempt may beat an amendment; the audited
  runs do not say where that point is.
- Mechanical fixes by code can hide a worker that systematically ignores a
  rule. Record them as refusals of class mechanical so the count stays visible.
