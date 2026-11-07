# Item B diagnosis: advisory audit skipped for Claude Code workers

Instruction: [Review design pressure behind recurring errors](../../instructions/review-design-pressure-behind-recurring-errors.md).
Authority used: read-only inspection of code, contract, ADR 121, the parcha run
directory and one persisted session file. No code, contract or harness was run.

## Outcome

The gap is unfinished scope, not design pressure. Nothing in the Claude Code
stream makes scanning hard: every tool result in the parcha run correlates to
its call by ID. The Pi-only meta-analysis gate is a separate, real limit, but
it rests on one coupling (auditor model = run model) and on pilot evidence,
not on anything a worker or the runner finds convenient to skip.

Recommendation: do (a) now; decide (b) with one operator choice, the auditor
profile. Defer (c). Reject (d) as a standing state, because (a) is cheap.

## What must remain true

From ADR 121 (Decision, lines 19 to 30) and SKILL.md "Advisory trace audit"
(lines 185 to 214):

- Every manifest-recorded attempt of a run, including failed and superseded
  ones, gets an explicit-failure scan saved as local run evidence.
- Coverage limits stay visible: an attempt that could not be scanned is
  counted and named, not silently dropped.
- After a completed analysis, a fresh, read-only, bounded auditor uses the
  failures as leads for at most three questions and 30 calls.
- Nothing about the audit changes publication, the receipt or the exit status.
- Only manifest-owned files inside the run's launch tree are evidence; personal
  sessions and undeclared nested workers are out of scope (audit.py lines 47 to
  51; meta-analyser.md lines 41 to 44).

The worker harness, the trace format and the auditor harness are
implementation choices. None of them is part of the outcome.

## Where the Pi assumption lives

1. Scan gate: audit.py line 68 marks an attempt supported only for worker
   `pi` with protocol `pi-json`; line 78 calls `scan(stdout, "pi-json")`.
2. Scanner formats: tool_failures.py accepts only `pi-json` and `pi-session`
   (line 178). It treats a missing boolean `isError` as a scan issue (lines 58
   to 60). That rule would misfire on Claude records, where `is_error` is
   optional.
3. Scope string: audit.py line 84 says "explicit Pi tool failures only".
4. Meta-analysis gate: audit.py line 221 skips unless the run profile's
   harness is `pi`.
5. Auditor launch: audit.py line 95 builds `Profile("pi", profile.launch_model,
   profile.effort, FLAGS)`. It reuses the run's model and effort. The FLAGS at
   lines 24 to 30 are Pi's isolation flags. Line 242 takes `harnesses["pi"]`.
6. Result parser: audit.py lines 117 to 145 read Pi events
   (`tool_execution_start`, `message_end`, `agent_settled`) for completion and
   the call budget.
7. Allowed roots: audit.py line 229 grants the auditor only the launch dirs of
   scanned attempts. Unscanned attempts' prompts are invisible to it.
8. Contract and decision text: SKILL.md lines 47 to 48, 188, 192 and "Other
   harnesses do not launch it"; ADR 121 lines 21 and 58; worker-profiles.yaml
   comment line 3; meta-analyser.md description line 2.

These are three decisions, not one:

- Which trace formats the scan reads (items 1 to 3, 7). This is independent
  of the auditor.
- Which harness the auditor runs on (items 5 and 6). Items 5 and 6 are one
  decision: the result parser follows the auditor harness, not the worker.
- Which model the auditor uses (item 5, worker-profiles.yaml line 3). Today
  it is tied to the run profile.

Item 4 conflates the second decision with the worker harness. The auditor
harness and the audited harness need not match.

## Is there design pressure?

Observation: the auditing commit c2e0d61c3 (2026-10-21) landed when
worker-profiles.yaml already had Claude Code and Codex profiles. The default
profile is `pi-sol` (SKILL.md line 49). The pilot used only Pi with
`gpt-6.1-sol` (ADR 121 lines 47 to 49). Pi-only therefore matched the default
path and the evidence, and other harnesses were deferred.

What the shortcut saves: one trace parser per worker protocol, one
isolation-flag set per auditor harness, and one result parser per auditor
harness. It also avoids choosing an auditor model outside the run profile.

Would a different design leave the same reason to skip? For the scan, no.
The parcha streams are easy to parse (measured below). For a Claude Code
auditor, partly yes: Claude Code loads ambient `CLAUDE.md`, skills and hooks
from the worktree, so a clean-context auditor needs different isolation
flags, and those are untested here. For a Pi auditor on Claude traces, the
only remaining reason is model choice.

No worker deviated. The skip was the code doing what the contract says, and
the status reported it (`unscanned_attempt_count: 18`). One presentation
defect: status shows `failure_count: 0` next to 18 unscanned attempts. A
reader who skips the coverage field sees zero failures.

## Evidence from the parcha stream

Parsed all 18 `stdout.log` files under `calls/launches/` (read-only, Python):

- 602 `tool_use` blocks and 602 `tool_result` blocks; every result's
  `tool_use_id` matches an earlier call. No `parentUuid` chain is needed.
- 498 results have no `is_error` key, 83 have `false`, 21 have `true`.
- Of the 21 errors, 20 are Bash permission refusals ("changes directory
  before running a version-control command": 10; "variable set in this
  command can't be checked": 8; two others). One is an Edit "String to replace
  not found". Twenty matching `system/permission_denied` events exist.
- No record has a non-null `parent_tool_use_id`, so no subagent output appears
  in these streams. All 18 results report `is_error: false`.
- Each stream names one `session_id`; each has a persisted session file.

So a scan would have produced 21 leads in 18 attempts. Most are harness
policy refusals: a command the worker wanted did not run. Those are exactly
the leads the meta-analyser is for ("what the analyst was trying to
understand").

## Which trace to scan

Scan the stream (`stdout.log`) in the launch tree.

- Ownership: it is the manifest-owned trace (audit.py lines 64 to 67). The
  persisted session lives under `~/.claude/projects/`, outside the run.
  Reading it breaks the evidence boundary that collect() and the
  meta-analyser commission both state.
- Retention: the stream travels with the run directory; the personal store
  may be pruned or may hold unrelated sessions in the same cwd slug.
- Content: for attempt 6722cd579c4d the session file's `user` records hold
  the same 27 tool results as the stream, with the same 2 errors. It adds
  record types a parser must ignore: `api-request-blob` copies of outgoing
  requests, `attachment` and session metadata. Content does not favour the
  session file; ownership and retention decide.
- What the stream lacks: persisted `parentUuid` branches, spilled
  `tool-results/` files and subagent transcripts. Rewinds do not occur in a
  headless print run. Subagent coverage is an open question (see below).

## Repair options

(a) Claude stream scan path, meta-analysis still Pi-only.
Needs: a `claude-stream-json` format in tool_failures.py or a sibling
module (ID correlation, absent `is_error` = false, record
`permission_denied` and `result.permission_denials` as signals); the gate at
line 68 keyed on protocol, not worker name; the scope string; unit tests with
a stream fixture covering absent, false and true flags; SKILL.md line 188
wording. No ADR change: ADR 121 already requires every attempt be scanned.
Leaves uncovered: the meta-analysis for Claude runs. Codex attempts stay
unscanned. Cost: small; mostly a parser and tests.

(b) Pi auditor for any worker harness.
Needs (a) first; line 221 keyed on scan coverage instead of run harness;
an auditor model independent of the run profile when the run is not Pi;
updated SKILL.md lines 47 to 48 and 192, worker-profiles.yaml line 3 and
meta-analyser.md line 2; an ADR 121 revision, because its Decision says
"After a completed Pi analysis". Tests for a Claude-worker run launching the
Pi auditor. Leaves uncovered: whether the auditor reads Claude stream records
well; the pilot only audited Pi traces. Risk: the auditor model differs from
the analysts', which is arguably better for independence but is a change.

(c) Claude Code auditor.
Needs a Claude result parser (completion, call count from `tool_use`), a
clean-context flag set for Claude Code (ambient CLAUDE.md, skills, hooks and
MCP suppression), tests, and the same ADR revision. Adds a second auditor
path with no pilot evidence. Gains nothing over (b) unless Pi becomes
unavailable.

(d) Keep Pi-only, state the gap.
Needs a SKILL.md sentence that non-Pi runs get no scan and no meta-analysis.
Matches ADR 121's stated limit (line 58). Leaves the scan requirement
("every recorded attempt") unmet for every non-Pi run, though the cost of
meeting it is now known to be small.

## Recommendation

Implement (a) under existing authority as a code change that brings the code
closer to ADR 121; it needs the agentic-analysis and tooling suites.

For (b), one question blocks the choice: which model runs the auditor when
the run profile is not Pi? Two candidates exist. A fixed `pi-sol` auditor
reproduces the piloted configuration exactly; it would arguably fit Pi runs
on Luna or Ultramarine better than today's reuse of the run model, which is
already outside pilot evidence. Reusing the run's model fails for Claude
aliases: Pi would receive `--model opus`, whose resolution under Pi I did not
check. The smallest resolving step is the operator naming the auditor profile
in an ADR 121 revision. After that, one Pi auditor launch on the parcha run's
audit snapshot would show whether it handles Claude stream records within 30
calls. That launch needs separate authority.

Also fix the status presentation: report `failure_count` as null or qualified
when every attempt is unscanned.

## Uncertainties and not inspected

- Subagents: no parcha worker used one. Whether `claude --print
  --output-format stream-json --verbose` streams subagent tool records with a
  `parent_tool_use_id` is untested here. If not, (a) under-reports for runs
  that use subagents; the contract already excludes undeclared nested workers.
- I first counted the session's `api-request-blob` copies as results; a review identified them as request copies, and the count above is corrected.
- Codex attempts have the same gap; not examined.
- Pi model alias handling, Claude Code isolation flags and the meta-analyser's
  ability to read Claude streams were not tested.
- I read one persisted session file only, to compare counts.
