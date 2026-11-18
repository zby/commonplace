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
4. [The draft instruction](../../instructions/continue-a-revise-pass.md) is in
   `kb/instructions/`, reached from the run report, and its siblings
   [decide items](../../instructions/decide-items.md) and
   [approve a text](../../instructions/approve-a-text.md) agree with it.
5. At least two live continuations are retained in `episodes.md` here, and
   what they showed is extracted or discarded.

State on 2026-11-18: conditions 1 to 4 are met by the merge `5d97ab35f`
and [ADR 138](../../reference/adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md).
Condition 5 is open: no live run has used the new flow. The result is
compared with the earlier prediction in
[implementation comparison](./implementation-comparison.md).

Left for later work by the operator: making old unanswered stops listable
(one live plan stop is affected), and naming a review profile in the
stale-reviews item. Not yet decided: declining a held candidate leaves no
recorded reason.

## Decided

- **A stop ends the pass.** A pass ends in one of three ways: it completed,
  it needs continuation, or it failed. A publication is the pass's last
  write, not a checkpoint. As implemented, a run publishes before it asks a
  per-item pass for proposals; when that pass proposes nothing the run goes
  on and publishes again at its end. Nothing waits between the two, and
  nothing is written after the run ends.
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
- **The pass ends at its first per-item entry.** It does not run later
  entries first. They wait in the continuation record, so they run on text
  that already has the approved items.
- **A failed entry does not hold back the completed ones.** The pass
  publishes what the entries before the failure applied, under the usual
  publication checks, and ends. The failed entry and those after it go into
  the continuation record.
- **Existing decisions are converted once.** The runs on disk hold 28
  operator records, 18 of them answered. A one-time script rewrites the
  answered ones into the new recorded form, in place. The new code gets no
  reader for the old format. The old run directories keep their hash names.
- **A held candidate ends the pass before any proposals.** When the edits
  so far add a validation warning, the candidate is not published and the
  pass ends there. It does not ask for the proposals of the next per-item
  entry, which would concern a text that may never be published. So every
  item in a continuation record concerns the text `made-for` names.
- **Each leftover item names who can resolve it.** The
  [unresolved frontier](../../reference/definitions/unresolved-frontier.md)
  definition now asks a feasibility claim to name the actor: the operator, a
  configured LLM agent, or later a decision model. The record applies that to
  each item. It names the actor expected to be able to do the work. It is not
  a statement of permission.

## State before the change (`209d4dc3d`)

This section and [Design](#design) are the record of what was planned. The
shipped behaviour is in ADR 138 and
[the review system](../../reference/README-REVIEW-SYSTEM.md).

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
- `decisions.py` accepts a revise or rewrite run directory only when its
  name matches a 12-digit hash with an optional number (`_RUN`). A
  timestamp name does not match, so the listing and the carry-over would
  skip the new runs.
- A plan entry that ends with a problem prevents the final publication: the
  run publishes only when no entry has the state `problem`.
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
| `made-for` | Hash and path of the note's text when the pass ended: its last publication, or its start text. Every item was computed on it. Never updated. |
| `what` | The item: see the kinds below |
| `actor` | Who is expected to be able to resolve it |
| `after` | Items that must be settled first |
| `how` | The command, or the section of the instruction |
| `evidence` | Paths of the proposals, reports or candidate the item rests on |

The record is not a lock on the note. Each command guards its own input:
the answers-taking command refuses when the note is not the text the
proposals were made for, and a focused run of a direct operation works on
whatever the note holds. After the first publication of a session the note
no longer matches `made-for`. That is expected, and the instruction has the
agent account for the difference from the note's run records.

A later session takes up unfinished items from the episode record of the
earlier session, which lists the items done, dropped and remaining. No
handoff is carried by the operator, and the run is not reopened.

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

[Continue a revise pass](../../instructions/continue-a-revise-pass.md) is
live in `kb/instructions/`. It carries three judgments that code does not
make:

- whether a leftover plan entry still fits the text that was published;
- whether a finding's reason still holds in the current context, not just
  whether its quoted passage survives;
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
- Publish the completed entries before a failed one.
- End the pass at a held candidate without asking for the next per-item
  entry's proposals.
- Accept both directory names in `decisions.py`: the hash names of existing
  runs and the timestamp names of new ones.
- Write and run the one-time conversion of answered operator records. Keep
  it under `scripts/` only if it is reusable; otherwise remove it after the
  run and state the counts in the commit.
- Keep `triage-inputs.json`, `earlier-decisions.json` and the captured stop
  decisions as the record of what a run read. Remove the branches that read
  them back on a repeat.
- Remove or rewrite the tests of replay across invocations, including
  `test_revise_keys.py`.
- Update the report's `waiting-for` text, `README-REVIEW-SYSTEM.md`,
  `decide-items.md` step 4 and `approve-a-text.md`, which tell the agent to
  repeat the command.

One writer per note at publication was first placed outside this workshop
as independent of the design. That was wrong: repeated runs had shared one
run directory and its lock, and the change removed that. `apply()` now
holds a per-note publication lock across the check and the write. The note
is still written before the publication record.

## Open choices

None on 2026-11-18. Two were settled by the agent as defaults, for the
operator to overrule: captured input files stay as a record of what the run
read; and `episodes.md` stays in this workshop until it closes, when its
content is extracted or discarded.

## What the episodes should show

Seek two contrasting live episodes: one where an approved edit makes a later
entry unnecessary, and one where the operator leaves items for another
session after a publication. In the second, check whether the next session
can identify what changed and what remains from the episode record and the
note's run records, without repeating the run. If it cannot, that is the
evidence for a stricter handoff. Report if either case was not
observed. These outcomes test the procedure; source line counts test only
the prediction about implementation size.

- How often the operator accepted unchanged what a worker proposed, by
  operation. This is the evidence ADR 137 names for moving a per-item
  operation to applying directly.
- How often a leftover entry no longer fitted the published text.
- How often a new pass asked the operator a question already decided, in
  different words. Decisions carry over only for an identical `quote` and
  `change`.
- Which steps the session agent spent time on that the workflow could have
  prepared.
