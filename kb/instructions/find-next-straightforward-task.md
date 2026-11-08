---
description: "Use when asked what useful KB work to do next: scan unresolved work, verify one straightforward task is still needed, and recommend it with a bounded change and check."
type: types/instruction.md
---

# Find the next straightforward useful task

Find one useful task on the [unresolved frontier](../reference/definitions/unresolved-frontier.md)—the discoverable field of
possible further work—whose need, scope, approach and verification are clear
enough for an agent to carry out without inventing a solution to a hard problem.

## Invocation and authority

An operator or parent agent loads this instruction when choosing the next KB
task. Use any supplied objective, search scope, exclusions and search budget.
If none are supplied, look for concrete improvements to this KB within a bounded
inspection of local files. Choose where to look from current evidence; do not
attempt an exhaustive survey or claim to have found the globally best task.

This instruction authorizes read-only discovery and a recommendation. It does
not authorize edits, external acquisition, agent launches, running a workflow,
executing the selected task or committing changes. Separate permission to execute
must specify its scope; selection does not expand that permission. Follow the
repository's instructions for any subsequently authorized execution.

## Find and check a candidate

1. Inspect working-tree status and any supplied coordination constraints. Avoid
   work already owned by another actor or whose relevant files are changing
   unless coordination is explicit.
2. Search promising work surfaces: open log observations, Open Questions in
   notes, pending ledger entries, live proposals, unfinished workshop work, and
   reviews or other recurring work that may need attention. These are examples,
   not separate eligibility classes. A due item is a candidate, not an automatic
   priority. Start with the caller's focus when provided; otherwise choose
   likely entry points. Use titles, descriptions and headings before full files.
   For theory questions, this is a discovery aid, not a complete inventory:

   ```bash
   rg -ni '^#{1,6}[[:space:]]+.*open questions' kb/theory --glob '*.md'
   ```

3. Read a candidate's source and enough current evidence to check that it is
   still needed. Look for an existing answer, superseding decision or completed
   implementation. Historical observations and archived proposals are not live
   tasks merely because they contain unresolved language. Respect explicit
   deferral triggers; do not turn an unmet trigger into permission to proceed.
4. Select a candidate only when you can name:
   - a concrete benefit, not just another document or a closed-entry count;
   - the exact defect or small unresolved task, with current evidence;
   - a bounded change using a known approach;
   - a check that can establish the intended result, including semantic support
     where a structural validator would not suffice.
5. Skip candidates that require an unsettled design choice, speculative research,
   new policy, unavailable evidence, or an unbounded audit to determine the
   remedy. For an established workflow, check that its current procedure is
   usable for the bounded task; do not start it just because work is overdue.
   Do not redesign a system merely to make a candidate executable.
   A clear local repair may remain useful even when the surrounding problem is
   hard. Stop searching once a sufficiently useful candidate meets the checks.

If the inspection budget is exhausted or plausible candidates remain unclear,
return that no straightforward task was established in the inspected scope.
Name the limiting uncertainty; do not infer that the KB contains no useful work.
Do not fill a quota by proposing cosmetic churn or continuing a failing approach.

## Return

Recommend one task, briefly stating:

- **Task and source:** the action and its originating path or section.
- **Benefit:** what improves for a reader, operator or executing agent.
- **Current evidence:** what establishes that it remains needed.
- **Bounded change:** intended files and why the approach is straightforward.
- **Verification:** what would show the repair worked.
- **Authority and stop condition:** permission needed and what would make the
  task cease to be straightforward during execution.
- **Search coverage:** surfaces inspected and important omissions, without
  claiming exhaustive prioritization.

Do not execute the recommendation under this instruction alone. If separately
authorized execution uncovers a consequential choice or missing support, stop
that task, preserve the finding and return for direction or select another task
within the caller's remaining authority. Do not repeatedly elaborate a speculative
solution merely because this task was selected first.
