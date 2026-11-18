# Continuing a revise pass interactively

Posed 2026-11-18 by the operator, as direction. The decisions under
[Decided](#decided) are the operator's, from a design conversation on that
date. The rest is an agent's design, awaiting the operator's reading.

## Goal

A `commonplace-review run revise` pass publishes what it can and then ends.
It never waits to be resumed. What it could not finish is left as a
**continuation record**, and an agent in a session with the operator
continues from that record by an instruction, not by the workflow.

The outcome sought is a smooth interactive procedure. Moving parts of it
back into the workflow is later work, decided from the episodes this
workshop retains.

## What closes this workshop

1. The operator has accepted or changed the design below.
2. An ADR amends [ADR 137](../../reference/adr/137-revise-publishes-without-a-publication-stop.md),
   whose clause "a run continues after it publishes" this design replaces.
3. The runner writes the continuation record and no longer resumes after a
   publication.
4. [The draft instruction](./continue-a-revise-pass.md) is in
   `kb/instructions/`, reached from the run report, and its siblings
   [decide items](../../instructions/decide-items.md) and
   [approve a text](../../instructions/approve-a-text.md) agree with it.
5. At least two live continuations are retained in `episodes.md` here, and
   what they showed is extracted or discarded.

## Decided

- **A stop ends the pass.** A pass ends in one of three ways: it completed,
  it needs continuation, or it failed. A publication is the pass's last
  write, not a checkpoint.
- **Partial publication stays.** Edits that need no decision are published
  before the pass ends, as ADR 137 has it.
- **Continuation is interactive first.** An instruction for a session agent
  carries it. The workflow may later prepare material that makes the session
  faster, such as proposals, alternatives or cached results.
- **No run is repeated.** Every invocation of `run revise` or `run rewrite`
  starts a new run. A later command that acts on a run's output names the
  run or the file.
- **Run directories are named by start time.** Revise and rewrite runs get
  `<note path>/<UTC timestamp>/`, as gate sweeps already do, in place of the
  hash of the note's text. A note's runs are still found by listing the
  note's directory, and the last entry is the latest run.
- **Naming the answers file is the approval.** A command that consumes an
  answers file reads it, checks it with the validator and keeps a copy in
  its own run. The agent runs it on the operator's word for that file. There
  is no separate approval before it, no operator record and no proposal key.
- **Unconsumed decisions get a small recording command.** A rejection, a
  deferral, a plan-stop answer and the decisions on an overtaken run have no
  command that consumes them. One command fixes such a file's text and time
  as the record, with no key and no tie to a waiting run.
- **Each leftover item names who can resolve it.** The
  [unresolved frontier](../../reference/definitions/unresolved-frontier.md)
  definition now asks a feasibility claim to name the actor: the operator, a
  configured LLM agent, or later a decision model. The record applies that to
  each item. It names the actor expected to be able to do the work. It is not
  a statement of permission.

## Current state (2026-11-18)

Read from `src/commonplace/lib/review_workflows/revise.py` and `edits.py`.

- A pass stops at the first `per-item` entry of its plan. It first publishes
  what the earlier entries applied. Repeating the command after approval
  applies the approved items and runs the rest of the plan.
- A revise or rewrite run's directory is
  `runs/v2/<workflow>/<note path>/<first 12 hex of the text's SHA-256>/`
  (`edits.run_dir_for()`). Repeating a command on the same text finds the
  same directory, and Workjig replays the answered calls.
- A run that published has changed the note's text, so the hash no longer
  leads to it. To resume it, `edits.run_dir()` first looks through the
  note's runs for one marked open whose last publication is the note's
  current text. `mark_open()` keeps that mark, `known_text()` has a second
  case for a run that published, and a note reverted to a text an earlier
  run published over gets a directory with the suffix `-2`.
- Gate sweeps are named `runs/v2/<UTC timestamp>/`, with `-2`, `-3` on a
  collision (`_run_dir()` in `cli/review_workflows.py`).
- Two readers depend on the hash name. `revise.py` finds the role report
  for a text by computing that text's run directory. `decisions.overtaken()`
  decides whether a pending stop is overtaken by comparing the run's
  directory with the directory of the note's current text.
- Several inputs are captured once so that a repeat reads the same ones:
  `triage-inputs.json`, `earlier-decisions.json` and the captured stop
  decisions. A run also records its mode and options for the repeat.
- The per-item operations are `abstractions` (depth 3) and `plain-wording`
  (depth 5). `readability-and-flow` (4) and `opening-and-title` (6) follow
  them in depth order, so a plan with `abstractions` usually has entries
  after its first stop.
- Of the 10 recorded revise plans without a plan `stop`, 3 hold a per-item
  entry and 1 has entries after it. Two runs have published automatically.
  ADR 137 says the behaviour is not yet run live.
- `run revise NOTE --pass NAME` runs a one-entry plan and publishes. For a
  per-item operation it asks a worker for new proposals. No publishing
  command takes an existing approved answers file.
- `run edit OPERATION NOTE --input answers=FILE` applies approved answers,
  when the answers' question is a result of the same operation on the same
  text. It writes nothing to the checkout.
- `--finding RESULT` accepts a review result of the note without checking
  that the result is fresh (`read_finding()`).
- After any publication the note's text has changed, so every stored review
  result of the note is stale.

## Design

### The pass ends at its first stop

The pass runs as it does now up to the first point that needs something no
worker in the pass can supply. It publishes the text reached so far, when
the publication checks pass. It writes the continuation record and ends.
Every later command on the note opens a new run.

Each run directory is `<note path>/<UTC timestamp>/`, with the sweep's
collision suffix. The run records the hash of its start text beside
`artifact/start.md`. Within one invocation Workjig's call records still
serve retries.

A pass that fails partway is not continued. A new pass pays again for the
assessment, the edit passes and, in the full procedure, the synthesis and
the role report. Review results are reused from the shared store by their
own freshness checks.

### The continuation record

One file in the run directory, also given in the run report. It states the
text it describes, and one item per piece of unfinished work, in the order
the work depends on. The field names below are illustrative.

| Field | Content |
|---|---|
| `made-for` | Hash and path of the text the items were computed on: the pass's last publication, or its start text |
| `what` | The item: see the kinds below |
| `actor` | Who is expected to be able to resolve it |
| `after` | Items that must be settled first |
| `how` | The command, or the section of the instruction |
| `evidence` | Paths of the proposals, reports or candidate the item rests on |

Values of `actor`: `operator`; `session-agent`, an agent working with the
operator; `worker` with the `effort` that selects its profile. A decision
model would be one more value. The value is an estimate. The instruction
says what to do when the named actor cannot settle the item.

Kinds of item a revise pass can leave:

| Item | Expected actor | Source in the run |
|---|---|---|
| Proposals of a per-item operation awaiting decision | operator | the pending answers file |
| Plan entries not run | worker at the entry's effort; for a per-item entry, then the operator | the plan and the pass states |
| An operation skipped as interactive (`narrow-overclaims` without evidence, `split-out-a-treatment`) | session-agent | the pass states |
| Claim questions the assessor listed for the operator | operator | `artifact/assessment.md` |
| A candidate held back because it adds a validation warning | operator | `artifact/final.md`, its diff, `new-warnings` |
| A plan `stop` on a proposal | operator | `artifact/stop-answers.md` |
| A worker or review failure | whoever can repair the environment | the run report |
| Review results made stale by the publication | worker; one launch per review operation | the publication record |

The last kind is the "automatic but expensive" case. It is listed so that
the session can name its cost. Nothing in the record schedules it.

### Applying approved answers

The one piece the interactive procedure cannot do with today's commands is
apply the operator's approved items and publish the result. Three ways:

1. **A focused run that takes answers.** `run revise NOTE --pass NAME` with
   an approved answers file as input. It checks that the note holds the text
   the proposals were made for, applies the approved items through the edit
   route and publishes. It is a new run that names the file it acts on.
   Recommended.
2. **`run edit` with answers, then a separate publishing command.** Two
   steps for the session agent on every per-item pass.

Letting the old run finish its stopped entry is ruled out by "no run is
repeated".

The same rule gives every other stop a command that names its input:

| Stop | Later command takes |
|---|---|
| Per-item proposals | the approved answers file |
| A candidate held for a validation warning, and a rewrite's candidate | the run, to publish that exact candidate; `--revised` likewise |
| Triage | the approved finding-answers files, to plan and run the fixes |

### The instruction

Drafted in [continue a revise pass](./continue-a-revise-pass.md). It is not
live: nothing loads it, and it names the command of option 1, which does not
exist. It carries three judgments that code does not make:

- whether a leftover plan entry still fits the text that was published;
- whether a finding made on the earlier text still describes a passage of
  the current text;
- when to stop continuing and recommend a new pass.

### Code changes implied

- End the pass at its first stop and write the continuation record.
- Add the answers-taking focused run (option 1).
- Name revise and rewrite run directories by timestamp, sharing the
  sweep's naming. Record the start text's hash in the run.
- Remove what only a repeat needs: the lookup of an open run in
  `run_dir()`, `mark_open()`, the second case of `known_text()`, the `-2`
  suffix, and the reuse of a run's recorded mode and options.
- Change the two readers of the hash name to read the recorded start hash:
  the role-report lookup and `decisions.overtaken()`.
- Add the commands that take a stop's output: publish a held candidate,
  supply a revised one, and plan fixes from triage answers.
- Remove the approval step: operator records, the `approve` command,
  proposal keys, edit detection and invalidation. Add the recording command
  for unconsumed decisions.
- Change `commonplace-review decisions` and the carry-over of earlier
  decisions to read answers files: the copies in consuming runs and the
  recorded unconsumed ones. How much of `decisions.py` this touches has not
  been read.
- Remove or rewrite the tests of replay across invocations, including
  `test_revise_keys.py`.
- Update the report's `waiting-for` text, `README-REVIEW-SYSTEM.md`,
  `decide-items.md` step 4 and `approve-a-text.md`, which tell the agent to
  repeat the command.

Not in this workshop: one writer per note at publication. `apply()` checks
the note and then replaces it, and the note is written before the
publication record. A lock keyed by the note closes both. It is independent
of this design.

## Open choices

1. **Captured inputs.** `triage-inputs.json` and `earlier-decisions.json`
   no longer need to be frozen for a repeat. They can stay as the record of
   what the run read.
2. **Publishing before a failure.** A pass with a failed entry applies
   nothing today. It could publish the entries that completed, as it does
   before a per-item stop, so that a new pass repeats less.
3. **Existing run directories.** The hash-named runs on disk stay where
   they are. Whether `decisions` must keep reading them, and how it tells
   their start text, is not settled. The same holds for the operator
   records in those runs, which hold the decisions made so far.
4. **How far "publish what it can" goes.** As drafted, the pass ends at the
   first per-item entry. It could instead run later entries that need no
   decision first. A later pass may change a passage an earlier proposal
   quotes, which makes that proposal stale. Not proposed.
5. **Where episodes go after the trial.** `episodes.md` here holds them
   until the workshop closes.

## What the episodes should show

- How often the operator accepted unchanged what a worker proposed, by
  operation. This is the evidence ADR 137 names for moving a per-item
  operation to applying directly.
- How often a leftover entry no longer fitted the published text.
- How often a new pass asked the operator a question already decided, in
  different words. Decisions carry over only for an identical `quote` and
  `change`.
- Which steps the session agent spent time on that the workflow could have
  prepared.
