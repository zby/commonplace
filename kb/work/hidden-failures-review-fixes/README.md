# Workshop: fixes from the 2026-11-07 hidden-failures review

## Origin and goal

On 2026-11-07 the operator had the [hidden-failures review](../../instructions/review-recent-logs-for-hidden-failures.md)
run by an Opus worker over this checkout's Claude Code sessions from
2026-11-05 onward, using the new Claude Code scanner. The worker's report is
retained unchanged as [review-2026-11-07.md](./review-2026-11-07.md); its
locators point at session files under `~/.claude/projects/` on the operator's
machine, not at repository files. The operator then directed: make a workshop
for fixing these. That direction is the commission. It does not by itself
authorize any individual repair below; each item names what authorizes it.

No delivered result was shown defective. The findings are masking mechanisms,
an unmet audit requirement, a scanner precision defect and a gap in the
instruction itself.

## Items

Each item states the finding, the fix candidate, what closes it and the
evidence locator in the retained review. Item letters are this workshop's
bookkeeping; incident numbers (I1 to I7) are the review's.

### A. Scanner over-flags harness signals on successful results

Finding: `scan_claude_code_tool_failures.py` applies its substring signals
(`user_rejected`, `permission_denied`, `tool_use_error`) without checking
`is_error`, so a successful result whose output quotes trace text is reported
as a failure. Three false leads in one session (review, Groups, "Scanner false
positives"). Any session that reads logs reproduces this.

Fix candidate: gate those signals on `is_error`, or emit them in a separate
list that does not count toward `failure_count`. Add a regression test with a
successful result quoting the strings. Also note in `scripts/scan_tools/README.md`
that `xargs` masks the scanner's exit code (I7).

Closes with: a commit, and the tooling suite run after the last edit (I6).
Authority: ordinary code change to a script committed this morning.

### B. Advisory audit skipped for analysis runs with Claude Code workers (I5)

Finding: the parcha-recall analysis ran with Opus workers. The audit in
`src/commonplace/lib/agentic_analysis/audit.py` scans a worker attempt only when
the worker is Pi with the `pi-json` protocol, and launches the meta-analysis
only when the run profile's harness is Pi. Eighteen attempts went unscanned and
the status said so (review, I5). The gap applies to every analysis run that
uses Claude Code workers.

Fix candidate: not chosen. The review recommends a design-pressure diagnosis
under [Review design pressure behind recurring errors](../../instructions/review-design-pressure-behind-recurring-errors.md)
with the question: should the audit accept Claude Code worker traces, and if
so, which trace? The attempt's `stdout.log` is a `claude` stream, while the
scanner reads persisted session JSONL. The first observation is to read
`calls/run.json` in the parcha run directory for the worker's recorded output
protocol and check whether a session file or stream copy sits in the launch
tree. That evidence is in worktree `.commonplace/worktrees/parcha-recall-d5ad184aa4af`,
outside the review's authorized directory; reading it needs the operator's
authorization, which this workshop records as pending.

Closes with: a diagnosis record here and either an ADR-backed change to the
audit or a recorded decision to keep Pi-only auditing with the gap stated in
the analysis instruction.

### C. Exhaustive claim on capped evidence (I2)

Finding: a prioritisation reply said every open workshop README had been
checked for prerequisites. The grep behind it ended in `head -40` and returned
exactly 40 lines; the reply did not qualify the claim. Disposition unknown.

Next observation, before any rule: at commit `cbf2389b5`, count the same
prerequisite-pattern matches over `kb/work/*/README.md` with no cap. If the
count is at most 40, close as no defect. If it exceeds 40, check whether any
extra line records a semantics-to-machine dependency and record the outcome
here.

Candidate durable output: an entry in the
[unattended-processing failure modes](../unattended-processing-failure-modes/README.md)
catalogue, "coverage claim over capped output", with a countermeasure such as
reporting the cap or the count alongside any exhaustiveness claim. That
workshop owns catalogue entries; this one supplies the instance.

### D. The review instruction is Pi-only

Finding: the instruction names Pi session directories, the Pi parser and the
Pi branch model. Running it on Claude Code required an ad hoc mapping in the
worker brief, which is retained as [claude-code-mapping.md](./claude-code-mapping.md).
The scan tools README already covers three harnesses.

Fix candidate: generalize the instruction to execution logs with a
harness-specific section per supported scanner, or keep it Pi-named and add a
sibling for Claude Code. Preference not fixed; the retained mapping is the
draft either way. Read the instruction type before editing.

Closes with: the instruction change validated and committed, and the mapping
file deleted from here.

### E. Silent no-op scripted edit under a concurrent writer (I1)

Finding: an unguarded `str.replace` on a README matched nothing because
another session had rewritten the anchor, and exited cleanly. Caught by
chance, redone with an assertion. Recovered; disclosed only in part.

Fix candidate: none now. Watch for recurrence while two agents share one
checkout. On recurrence, consider a Development line in `AGENTS.md` that
scripted edits assert their anchor, or route the mechanism to item C's
catalogue as "silent no-op edit". Trigger: the next observed stale or lost
edit in a shared checkout.

### F. Process lapses recorded, no design change (I6, I7)

I6: the commit of the scanners followed a claim that the general and tooling
suites passed, but that run preceded the last scanner edit; only the scanner's
own tests ran afterwards. I7: the scanner exit code reported to the operator
was inferred through `xargs`, not observed. Both are compliance lapses against
rules already in `AGENTS.md`. Action: item A reruns the suites; the xargs note
goes into the README. Record both in `kb/log.md` at closure as episodes, not
as new rules.

### G. Operator decisions, not fixes (I3, I4)

- The stopped parcha ingest left `kb/sources/.snapshots/parcha-skills-recall.md`
  and `kb/reports/cache/connect/sources/parcha-skills-recall.connect.md`.
  Keep or delete is the operator's call; the ingest file itself was never written.
- The parcha-recall analysis is still not integrated; its worktree sits at
  detached `cbf2389b5`. Integration is a separate commission.

## Boundary and bookkeeping

- Evidence is the retained review plus the session files it cites. Do not
  copy trace contents here; cite locators.
- Items A and D are implementable within existing authority. Item B needs
  authorization to read the parcha worktree traces. Items C and E are
  observation-first. Items F and G need no implementation.
- One commit per item. Cite this workshop in the trailer
  `Workshop: kb/work/hidden-failures-review-fixes`.

## What closes the workshop

Every item is implemented, handed to diagnosis with a record here, recorded
in the log, or dropped with a reason. Durable outputs go to their collections:
the scanner change to `scripts/`, the instruction change to `kb/instructions/`,
catalogue instances to the failure-modes workshop, episodes to `kb/log.md`.
Then delete this directory and its Active Workshops entry.
