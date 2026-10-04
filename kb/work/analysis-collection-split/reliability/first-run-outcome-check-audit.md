# First run outcome check: audit

Commissioned by the operator on 2026-10-04 after the run completed, under the
[plan](./first-run-outcome-check-plan.md). This audits the analysis workflow,
not the analysed system. Published members are unchanged.

All ten jobs were accepted on their first handout. No output was refused at
acceptance, no job was blocked, and no correction cycle ran. Every analyst
ran the acceptance check before submitting, and the check caught the defects
that cost retries in the second audited run. Three defects survived
publication: an inspection claim no trace supports, a machine-local worktree
path in the public Source register, and the system named by its repository
slug. One run cannot attribute the difference to any of the four changes it
exercised.

## Evidence and limits

- Run: `AAS-2026-10-04-dynamic-cheatsheet-01`, in worktree
  `.commonplace/worktrees/dynamic-cheatsheet-3e10f8a5a72f`. Method commit
  `bb3126f84`. Source revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`,
  unchanged from both audited runs.
- Harness: Codex CLI 0.160.0, model `gpt-6-luna`, effort medium, for the
  coordinator and all workers. The second-run audit does not record its model.
  Of the 20 session files that name that run, 18 use `gpt-6-luna` at medium
  effort and two use `gpt-6.1-sol`; which two was not checked. The worker
  model therefore appears to match, without being established per session.
- The operator's invocation was the skill with the repository URL only. It
  named no system and no revision. The coordinator passed no
  `source-revision`; code took the default branch tip, which is the audited
  revision.
- [Evidence file](./first-run-outcome-check-evidence.json): the eleven trace
  files (coordinator and ten workers) with SHA-256, tool-call counts,
  durations and token totals; every acceptance-check log line of this run and
  of the stopped attempt; the retained manifest digest.
- The retained set passes `commonplace-validate` with zero failures and
  warnings. It was merged to `main` in `c59d2b8a4` before this audit.
- The scan covers tool calls, tool results and delivered assistant text.
  Worker handoff messages and reasoning are encrypted and not auditable.
  Negative findings mean no demonstrated case in these traces.
- Run state and scratch files remain only in the ignored worktree. Removing
  the worktree deletes them.

## Counts against the baseline

| Measure | Second run | This run |
|---|---|---|
| Accepted jobs | 14 | 10 |
| Worker sessions | 17 | 10 |
| Jobs needing a second handout | 3 | 0 |
| Substantive correction cycles | 2 | 0 |
| Environment blocks | 1 | 0 |
| Wall time, open to publication | about 54 minutes | about 21 minutes |
| Quotations in the final set | 14 | 26 |

The workflow gained two jobs, profile and profile verification. The job count
still fell because reconciliation, record verification and synthesis
verification each passed in round 0.

Per job:

| Job | Seconds | Check runs logged | Refusals found before submission |
|---|---:|---:|---|
| boundary | 132 | 1 | none |
| runtime | 194 | 4 | conclusion status, 8 fields in three runs; one ambiguous quotation |
| epistemic | 185 | 2 | none |
| memory | 284 | 3 | job contract: `Validation: pending` in a complete report |
| reconcile-0 | 89 | 1 | none |
| verify-0 | 104 | 1 | none |
| profile | 110 | 1 | none |
| verify-profile | 83 | 1 | none |
| synthesize | 95 | 1 | none |
| verify-synthesis | 68 | 1 | none |

Three further check calls left no log line: one refused by the checkout
guard, and two made before the output file existed.

The eleven sessions used 7.6 million tokens in total, mostly cached input.

## What the acceptance check changed

### Every analyst ran it, with the run's own command

All ten workers called `commonplace-analysis-check` from the supplied
`command-path` before reporting. No acceptance refusal exists that the check
would have reported. The revisit signal "analysts do not run it or do not act
on it" is not observed.

### Runtime: one repair error repeated twice, and the message lacks location

The first check reported eight `conclusion status` refusals and one ambiguous
quotation. The cause of the eight: the analyst wrote both statuses on one
line, ending with a period. Its repair split the line and kept the period, so
the value became `uninspected.`. The message named the invalid value and the
permitted values. The next repair was a `sed` whose pattern matched lines
without the period, so it changed nothing, and the third check returned the
same eight refusals. The analyst then searched the draft, saw the period and
removed it. The fourth check passed.

The message was sufficient to identify the defect. It was not acted on
precisely. Two properties of the message made that easier:

- The eight refusals are identical lines. None names the record or line, so
  the output does not show that one repeated typo causes all of them. The
  [acceptance check plan](./analyst-acceptance-check-plan.md) requires a
  location in every message.
- The repair line is generic: "correct the named field, section or citation".
  The determined repair here is "remove the trailing period".

The revisit signal "the same check failing repeatedly in one job" is observed
once. Its cause is a worker repair error, with the missing location as a
contributing design gap.

### Runtime: the ambiguous quotation was repaired by choosing another passage

The check reported one passage occurring more than once. The analyst replaced
it with a different, unique line from the same file. It did not paste a
proposed range and did not lengthen the passage. Whether the replacement
supports the finding as well as the original is not assessed here. No
quotation was reported as not found in this run.

### Memory: a recurrence from the second run, now caught locally

The first check refused `Validation: pending` in a report marked complete.
The second audited run recorded the same defect in the memory analyst. The
analyst replaced the marker, first with a narrative of the refusal and then
with "acceptance check passes after replacing the pending marker. It checks
form and occurrence, not claim support." No analyst presented a passing check
as evidence that findings are correct.

### Published quotations and IDs

All 26 attributions in the published set are path-only. None carries a range
or a revision written by hand. All record IDs are named. No numeric ID, range
phrase or group phrase appears. The second run's two range refusals have no
counterpart.

## The same-session handover

The skill prepared its worktree and continued in the same session, as
committed in `5fe0613be`. The coordinator called every `commonplace-workflow`
command by its absolute path in the worktree, with the worktree as working
directory. Workers started with the originating checkout as working directory
and read the run's files by absolute path.

One guard refusal occurred. After two passing checks, the memory analyst made
a final edit and ran the check from the originating checkout's `.venv/bin/`.
Code refused, naming the directory to use, and the analyst reran it from the
worktree. Without the guard, that call would have checked the draft with the
originating checkout's code.

No stale-context case is demonstrated: the session received its instructions
at 11:58, after the last method commit at 11:48.

## Earlier attempts on the same day

- **Codex-made worktree.** A session started in `~/.codex/worktrees/57ce/` at
  `62027f14c`, 33 commits behind `main`, with no local environment. It mixed
  old instructions with new engine code and is not evidence. It led to the
  refusal of an implicit `HEAD` behind `main`.
- **Preparation blocked by a local settings file.** Preparation refused every
  attempt in this checkout until `653ed1b2c` exempted an ignored
  `settings.local.json`.
- **Stopped run at `653ed1b2c`.** The boundary job was accepted with two
  Source register rows for `SRC-1`, which the source contract allowed. The
  runtime analyst's check then refused `duplicate set declaration: SRC-1`.
  The analyst repaired its own ten refusals, could not repair the boundary,
  and wrote a problem report. The coordinator stopped within its permitted
  scope. `bb3126f84` moved the refusal to boundary acceptance and aligned the
  instruction. The acceptance check surfaced a conflict between a contract
  and a validator in the first job that met it.
- Two launches at 11:15 and 11:16 were abandoned before a run opened. They
  are not examined.

## Failures that survived publication

### An inspection claim that no trace supports

The published record verification says the reports "additionally inspect"
`dynamic_cheatsheet/utils/sonnet_eval.py`. No worker read that file's
content. The boundary worker requested it in one combined read of twelve
files. The result was truncated in the middle and lost every file under
`dynamic_cheatsheet/`. The worker reread five of them in ranges, not this
one. The verifier read no source file; it listed the tree and read the
members.

The second audited run carried an unresolved conflict about this helper's
coverage. This run asserts inspection instead. The acceptance check cannot
catch it: the sentence has no quotation and no typed field.

### A worktree path in the public Source register

The published overview's Source register gives the access root as
`/home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-3e10f8a5a72f/related-systems/…`.
The path is machine-local and stops existing when the worktree is removed.
Earlier runs published a path in the originating checkout. Worktree isolation
makes the published path short-lived.

### The system is named by its slug

`system: dynamic-cheatsheet` and the overview title use the repository name.
Member descriptions say "Dynamic Cheatsheet". The skill asks for the
source-native system name. The operator gave only a URL, and the coordinator
used the repository name without deriving or asking.

## Other observations

- **A false init warning on every command.** Preparation creates
  `.commonplace/worktrees/` in the originating checkout. The library check
  treats any `.commonplace/` directory as an initialized project, so every
  decorated command run in or below the checkout prints "project files are
  out of date … rerun commonplace-init". Every check output carried about 230
  bytes of it. No worker acted on it. `AGENTS.md` forbids running
  `commonplace-init` in this checkout.
- **Truncated reads.** Four results were truncated: the boundary's combined
  read and a tree listing, one combined read by the epistemic analyst, and
  one search by the memory analyst. The boundary and epistemic workers reread
  most lost spans in ranges. The memory search's full match set was not
  restored. Member reads followed the supplied ranges and were not truncated.
- **Exit status discarded.** The coordinator delivered only `r.output` in all
  28 command calls, against the driver's complete-result pattern. Most
  workers did the same. This repeats a finding of both earlier audits.
- **Checks before writing.** The reconciliation worker's first write used a
  relative path from the wrong directory and failed; record verification ran
  the check before writing its output. Both recovered in the next call.
- **Publication instruction read late.** The coordinator read the publication
  instruction after `step` returned `done`. Code had already published.
- **The duplicate cheatsheet identity is gone.** The memory member annotates
  `RT-OBJ-cheatsheet` and does not redeclare it; reconciliation states so.
- **Register fidelity improved.** The boundary worker read the notebooks'
  code cells and the register says so. It claims roles, not contents, for
  `data/` and `embeddings/`.
- **The overview as review.** The overview reads without the members: a
  boundary table, a bounded synthesis with links to records, and limitations
  with resolving evidence. Its title and the register's access root are the
  reader-facing defects.

## Revisit conditions

| Marker | Observed in this run |
|---|---|
| ADR 105, acceptance check and path-only quotation | Used by every job. One job failed one rule in three consecutive checks. No avoidable acceptance refusal. No quotation not found; one ambiguous, repaired by substitution. No hand-written range or revision. No confusion of a pass with correctness. |
| ADR 104, named record IDs | No unresolved or misspelled name, no range or group phrase, no rename attempt, no collision. |
| ADR 103, profile job | Profile and its verification each passed in one handout with one check run. No correction cycle, so the correction path is untested. |
| ADR 102, stable path and archive | First publication at `retained/dynamic-cheatsheet/` with no incumbent. Archiving and link following are untested. |

One run closes no marker.

## Candidate repairs, for the operator to decide

Ordered by expected value. None is commissioned here.

1. Give each type-validation refusal its record or line, and collapse
   identical refusals. This closes the gap between the acceptance check plan
   and the runtime analyst's messages.
2. Stop the false init warning: require an init marker file, not the bare
   `.commonplace/` directory.
3. Keep the worktree's access root out of the published register, or record
   it relative to the checkout.
4. Decide how the system name is obtained when the invocation gives only a
   URL.
5. Treat "inspected" statements in verification as claims that need a traced
   read. This is a semantic check and belongs with independent verification,
   not code.

## What this run does not show

- Which of the acceptance check, named IDs and the smaller packets produced
  the improvement.
- That analyses are more correct. Semantic verification passed in round 0
  everywhere, and the one traced verification claim examined here is
  unsupported.
- Behaviour of the correction, archive and retry paths, which did not run.
