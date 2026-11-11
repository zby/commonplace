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

## Current status — 2026-11-09

Repository-state refresh, not a new transcript review. The retained review and
B diagnosis remain unchanged; prior test and trial results below were not rerun.

- **A and B closed:** scanner precision and Claude Code advisory auditing shipped.
- **D resolved:** the current instruction supports each harness through its own
  scanner, but requires a separate review in each executing harness. The obsolete
  mapping draft has been removed.
- **G integration resolved:** the parcha analysis is on main. The stopped ingest's
  two leftover files still exist; their keep-or-delete decision remains open.
- **C open:** reproduce the historical prerequisite search without its cap before
  deciding whether the prioritisation conclusion was defective.
- **E watch only:** retain the recurrence trigger; this refresh did not search
  new sessions for another incident.
- **F closed:** both process episodes are retained under Historical observations
  in `kb/log.md`, with original trace locators and repair evidence.

Next work is C's bounded historical check, not another audit implementation.
C needs the exact search expression from the cited Claude Code call: the retained report abbreviates it as `grep ...`. Obtain that through
an authorized Claude Code review rather than inventing an equivalent query.
The workshop stays open for C and G's cleanup decision.

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

Status 2026-11-07: done. The three signals are gated on `is_error`, a
regression test covers false, absent and true flags, and the README notes
the xargs masking. Ruff and the general plus tooling suites passed after the
last edit; the whole-corpus scan lost exactly the two `is_error: false` leads.

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
outside the original review's authorized directory; authorization was pending
at framing. The diagnosis and implementation records below supersede that
initial blocker.

Closes with: a diagnosis record here and either an ADR-backed change to the
audit or a recorded decision to keep Pi-only auditing with the gap stated in
the analysis instruction.

Status 2026-11-07: diagnosis done, see [b-audit-diagnosis.md](./b-audit-diagnosis.md),
reviewed and corrected once. Finding: unfinished scope, not design pressure.
The 18 parcha streams correlate every one of 602 results to its call by ID
and hold 21 explicit errors, 20 of them harness permission refusals. The
right scan target is the manifest-owned `stdout.log` stream, on ownership
and retention grounds. Recommended repair, option (a): a `claude-stream-json`
scan path keyed on protocol, with tests and a SKILL.md wording change, under
existing authority since ADR 121 already requires every attempt be scanned;
also report `failure_count` as null or qualified when nothing was scanned.
Open operator decisions before option (b): which model runs the Pi auditor
when the run profile is not Pi, and authority for one trial launch on the
parcha audit snapshot.

Status 2026-11-07, option (a) implemented. The Claude Code scanner moved into
`src/commonplace/lib/agentic_analysis/claude_code_tool_failures.py`, reads
both session files and `claude-stream-json` streams, correlates results to
calls by tool-use ID and records permission denials and the stream's final
result. The audit selects a scanner by the attempt's output protocol and
reports a null finding count when nothing was scanned. The code landed in
`5184dd297` together with the shared v2 result contract from a concurrent
session; this commit carries the SKILL.md and commands reference wording and
this record. Verified on the committed tree: the six review-window session
files reproduce the pre-change baseline tool counts, failures, compactions
and provider errors; the parcha streams scan with exit 0, both Bash failures
located to their calls, and both permission denials recorded; general,
tooling and agentic-analysis suites pass, including slow. Not verified:
subagent streams with `parent_tool_use_id`, and no parcha audit was rerun,
since the scope string change gives a new audit fingerprint. Option (b) and
its two operator decisions stay open; ADR 121 line 58 still states the
meta-analyser runs only for Pi analyses, which remains true.

Status 2026-11-07, option (b) implemented, item closed. Operator decisions:
the whole workflow runs in one harness, and the auditor reuses the run
profile's model and effort. The meta-analyser now launches through the run
profile's harness; Pi and Claude Code have auditor configurations, Codex
records a skipped audit. ADR 121 amended. Trial launch on the parcha run
snapshot (`audit/a441e124…` in the run directory): state complete, 18 tool
calls, 0 permission denials, model `claude-opus-5-5`, 101 seconds, report
with no material finding. Analysis of the parcha workers' 20 permission
refusals: all 18 workers ran print mode with `acceptEdits`, which covers
only Edit and Write tool changes; Bash commands that defeat static checking
(`cd` before `git`, 10 of 10 refused; shell variable prefixes, 9 of 9;
shell writes, 1) are refused because no operator answers prompts. Every
refusal was recovered on the next call. The worker rules paragraph that
told workers to change into the source checkout caused the first pattern;
it is replaced by four command rules, also added to the meta-analyser
instruction, and the `UNATTENDED` docstring now states what each flag
grants. Not verified: an auditor whose allowed roots lie outside the
worktree, where `--add-dir` is added but untested. Candidate catalogue
entry for `kb/work/unattended-processing-failure-modes/`: a harness safety
check converts an operator prompt into a silent refusal, paid repeatedly
by independent workers because nothing carries the rule between them.

### C. Exhaustive claim on capped evidence (I2)

Finding: a prioritisation reply said every open workshop README had been
checked for prerequisites. The grep behind it ended in `head -40` and returned
exactly 40 lines; the reply did not qualify the claim. Disposition unknown.

Next observation, before any rule: at commit `cbf2389b5`, count the same
prerequisite-pattern matches over `kb/work/*/README.md` with no cap. If the
count is at most 40, close as no defect. If it exceeds 40, check whether any
extra line records a semantics-to-machine dependency and record the outcome
here.

Status 2026-11-09: still open. Repository history is available at `cbf2389b5`,
but the retained review omits the original grep expression and does not name
the five machine-side READMEs. A keyword search of the historical tree does not
recover either fact reliably; it cannot establish the original uncapped count.
No fresh transcript inspection or finding of no defect is claimed.

Bounded handoff for an operator-invoked Claude Code agent: inspect only session
`25868e95-d6c5-4168-af25-ff2b1fac1682.jsonl` under
`~/.claude/projects/-home-zby-llm-commonplace/`, calls L206–L207, result L215 and
conclusion L229, plus L161 if needed to interpret the prioritisation question.
Return the exact search command, its path selection and ordering, and the five
README paths. Do not blindly replay transcript commands or widen the session
review. Reconstruct only the read-only search over the historical blobs.
Then reproduce the search against repository blobs at `cbf2389b5` without
`head` or character truncation, record the full count, and inspect omitted
matches and the five complete READMEs for the stated dependency. If the command
or historical working-tree state cannot be recovered, report that limit rather
than substituting a query and claiming reproduction. Keep any coverage failure
separate from a demonstrated wrong prioritisation conclusion.

Candidate durable output: an entry in the
[unattended-processing failure modes](../unattended-processing-failure-modes/README.md)
catalogue, "coverage claim over capped output", with a countermeasure such as
reporting the cap or the count alongside any exhaustiveness claim. That
workshop owns catalogue entries; this one supplies the instance.

### D. Review instruction coverage — resolved

Original finding: the review needed an ad hoc Claude Code mapping because the
instruction used Pi session directories, parser and branch model.

Status 2026-11-09: resolved by the shipped
[review instruction](../../instructions/review-recent-logs-for-hidden-failures.md).
Commit `c86e04b05` added harness-independent scanner selection and evidence
handling; `4c183c724` restricted each invocation to the executing harness's logs.
The operator invokes separate agents for cross-harness coverage. The procedure
now distinguishes native sessions from streams and directs readers to
`scripts/scan_tools/README.md` for supported formats rather than duplicating
parser details.

The obsolete mapping draft was deleted in this refresh. Its claims that no
stream variant or `--format` flag exists were superseded by B's scanner work.
The current instruction was validated during this refresh.

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
goes into the README.

Status 2026-11-09: closed. Both episodes are retained under Historical
observations in `kb/log.md`, citing I6/I7, their original session locators and
repair commit `91810b276`. No new rule was added and no fresh test run is claimed.

### G. Operator decisions, not fixes (I3, I4)

- The stopped parcha ingest left `kb/sources/.snapshots/parcha-skills-recall.md`
  and `kb/reports/cache/connect/sources/parcha-skills-recall.connect.md`.
  Both still exist on 2026-11-09. Keep or delete remains the operator's call;
  this refresh did not remove either file.
- Integration is resolved: merge `330ea995a` integrated publication `b71e3abed`.
  The [retained parcha analysis](../../agentic-system-analyses/retained/parcha-ai--parcha-skills/overview.md)
  is present on main. The worktree now points to `b71e3abed` on its analysis
  branch, not detached `cbf2389b5`. No integration or worktree cleanup is needed
  as a repair of I4.

## Boundary and bookkeeping

- Evidence is the retained review plus the session files it cites. Do not
  copy trace contents here; cite locators.
- Items A, B and D are resolved. Do not reopen their implementation or trial
  launches merely to refresh this workshop. C is observation-first; E waits
  for recurrence. F is retained in the log. G's remaining file cleanup needs
  the operator's decision.
- One commit per item. Cite this workshop in the trailer
  `Workshop: kb/work/hidden-failures-review-fixes`.

## What closes the workshop

Every item is implemented, handed to diagnosis with a record here, recorded
in the log, or dropped with a reason. Durable outputs go to their collections:
the scanner change to `scripts/`, the instruction change to `kb/instructions/`,
catalogue instances to the failure-modes workshop, episodes to `kb/log.md`.
Then delete this directory and its Active Workshops entry.
