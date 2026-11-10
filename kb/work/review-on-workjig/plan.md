# Implementation plan

Written 2026-11-09 by the planning session (Claude, claude-fable-5-2) on
the operator's direction to update the workshop, plan its implementation
and start building. The [README](./README.md) holds the goal, the design
direction and what closes the workshop; this file holds the build order,
the choices the design left open, and the state of each step.

The plan details phase 1 and keeps phases 2 to 4 coarse. Each coarse phase
names what returns it to a decision.

## Choices this plan makes

The design items were silent on these. Each is the planner's choice, open
to the operator's veto, and cheap to change before the first real sweep
writes results.

| Choice | Decision | Reason |
|---|---|---|
| Code location | `src/commonplace/lib/review_workflows/` (`results.py`, `gates.py`), CLI `src/commonplace/cli/review_workflows.py`, command `commonplace-review` | follows `lib/tasks.py` with `cli/task.py`; the old `commonplace.review` package stays untouched until phase 4 |
| Tests | `tests/commonplace/review_workflows/`, with a row in `tests/README.md` | a subsystem directory per responsibility |
| State root | `kb/reports/state/review/` with `results/` and `runs/<stamp>/` | already ignored by `kb/reports/.gitignore`; separate subdirectories keep a note path from colliding with `runs` |
| Criterion id | the catalog gate id (`prose/source-residue`) for a file under the gates directory; otherwise the criterion's repository path without `.md` | short paths for the 43 gates; any markdown file still has an id without a registry |
| Frontmatter keys | `note`, `note-sha256`, `criterion`, `criterion-sha256`, `outcome` (`pass`, `warn`, `fail` or `report`), `profile`, `model`, `run`, `launch`, `completed-at` | kebab-case YAML keys (ADR 116); `profile` and `model` name the executor |
| Note hash | SHA-256 over the parts the criterion `watches:`; over the whole file when it declares none | replaces acknowledgement of unwatched changes; README item 1 |
| Model partition | dropped; profile and model are provenance, and `status` can filter on them | README item 1 |
| Both inputs changed | the state lists both, in the order note, criterion | no information is lost; the caller chooses what to show |
| Deleted note | its results are reported as `orphaned`, and removing them is deleting files | replaces `freshness-retire` |
| Old package | the surviving pure helpers moved into `lib/review_workflows/` when the old package was deleted | no code path reaches a store |
| Review profiles | `kb/instructions/review-profiles.yaml`, same entry shape as `kb/tasks/profiles.yaml`, without edit or commit grants on the checkout | a task profile may commit; a review worker may not |

Installed projects: a criterion is named by its artifact identity, a
repository path or `commonplace:<path>` for a library file. A catalog
gate's id is `<lens>/<name>` in both layouts, and another library
criterion's id is `commonplace/<path>`.

## Phase 1, the gate sweep

### Step 1.1, result files and status (easy)

Pure functions, no runtime and no worker launch.

- `results.py`: the result record; reading and atomic writing of a result
  file; the criterion id; the watched-parts note hash; `freshness()` for
  one pair, answering `fresh`, `missing`, or stale with the changed
  inputs; `status()` over a list of pairs; `orphaned()` for results whose
  note or criterion file is gone.
- Tests for the consumer-visible contracts: a written result reads back
  equal; an edit outside the watched parts leaves a pair fresh and an edit
  inside stales it; a criterion edit stales exactly its pairs; a path
  that would escape the results root is refused.

Done when the tests pass with `uv run pytest tests/commonplace/general
tests/commonplace/review_workflows` and `uv run ruff check .` is clean.

### Step 1.2, the gates workflow and the command (hard)

Built in a separate worktree on top of step 1.1.

- `gates.py`: expand note and criterion requests into applicable pairs
  with the existing resolution; skip fresh pairs; for each remaining pair
  one `checked()` call with inputs `note` and `criterion`, one output
  `review`, and the outcome parser as the check; write the result file
  when the answer is accepted; report worker problems without writing a
  result. `gather` runs the calls, and `Run(max_workers=n)` bounds them.
- The prompt keeps what the reviewer scaffolding in
  `review/protocol/prompt.py` says for a single pair: the note's
  repository path so its links resolve, the conformance wrappers for type
  and collection pairs, the one derived local path a criterion may name,
  and the strict `## Result:` line.
- The run records the working tree before and after and fails the run
  when a worker changed the checkout, as `lib/tasks.py` reports
  `leftover`.
- `commonplace-review status`, `run gates`, `retry` and `acknowledge`,
  with a new run directory per invocation and `--resume <run>` to
  continue one.
- Tests on a fake harness, as `tests/commonplace/headless/test_tasks.py`
  has: a sweep writes one result per pair; a second sweep launches
  nothing; a note edit re-asks only that note's pairs; a malformed review
  costs one corrected attempt; a worker problem leaves no result; a
  worker that writes the checkout fails the run.

Done when those tests pass with the `headless/` suite and ruff, and one
live pair has run through `commonplace-review run gates` with a real
profile. The planning session runs the live pair after review, not the
worker.

### Step 1.3, the first sweep (operator, still open)

One collection with one profile. It costs real launches, so the operator
chooses the collection and profile and starts it. It decides:

- call granularity (README item 3), from the usage evidence of the
  launches against one bundle call on the same notes;
- whether the watched-parts hash is kept;
- whether the result file carries the cost and boundary field asked for
  in the mailbox message
  `kb/messages/20261030T085047Z-economics-workshop-unattended-workflows-cost-per-yield-records.md`.
  The reply is written then.

## Phases 2 to 4, as built

On 2026-11-09 the operator directed the planner to finish the work
without stopping: no backwards compatibility, no data migration, one
commit per larger step. Phases 2 to 4 were therefore built before step
1.3 ran. Opus workers implemented each step and the planning session
reviewed, corrected and committed.

**Retirement of the old code** came first, so the later phases built on
one package. It moved the surviving pure helpers into
`lib/review_workflows/` (`criteria.py`, `outcomes.py`), made criteria
work as library identities in installed projects, and deleted the SQLite
store, the review and freshness packages, 12 commands and their tests:
78 files and about 14,400 lines. `commonplace-status --review` reads
result files. Relocation never rekeyed the store in code, so only its
tests changed.

**Phase 2, the full pass.** `gates.py` gained bundle grouping, the
headless runtime gained `decide()`, and `full_pass.py` runs the pass as
`commonplace-review run full-pass`. The packet lives at
`kb/reports/state/review/packets/<note-path>`; `commonplace-review
packet` checks its hashes. The guard command, `lib/full_pass.py` and the
validation rule for the old report are deleted, and the type is cut to
the packet. The directory-type question of README item 8 is answered no
for now: the run's `artifact/` and the packet schema carry what code
needs.

**Phase 3, the revision.** `Run.ask`, `checked` and `decide` take a
profile per call. `revise.py` runs `commonplace-review run revise` with
the assessment stop, the operator-edited `plan.yaml`, a strike stop for
`plain-wording` and `abstractions`, and profiles chosen by each pass's
`effort`. `narrow-overclaims` runs only with a non-empty defend list and
`split-out-a-treatment` never runs headless. The six ordered pass files
gained a `depth` field so code can check plan order.

**Phase 4, documents.** [ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md)
supersedes ADR 010, 029, 032, 035, 036, 043, 052, 065 and 067 and amends
038, 039, 041, 051 and 080. The review README and review architecture
are rewritten; the freshness architecture page, review triage and the
semantics-preserving gate migration are retired; the fix, batch and
retire instructions operate the new command. Sixteen proposals and seven
theory notes were corrected where they stated the store as present
fact, and two proposals were archived.

## Phase 5, runs as functions of their inputs

On 2026-11-10 an outside review (Astra) found two defects in resumed
runs: a resumed run could report success for text the operator had
edited since, and a plan named with `--plan` was lost on the next
resume. Both were fixed in place, and both came from one cause. The
workflows wrote the note during a run, while the runtime treats a run as
a replayable function of its inputs. The operator then directed a
simplification on that line. Four changes were built the same way as the
earlier phases:

1. **One write, at the end.** The full pass and the revision carry each
   edited text in memory and in the run's `artifact/texts/`. The last
   step writes the note once, and only over the start text. A hand-back
   writes nothing, so there is nothing to restore. A revision applies
   its text only when every pass of the plan ended well. The write log,
   its replay, the interrupted-write recovery and the restore are
   deleted.
2. **The run directory is derived from the inputs**:
   `runs/<workflow>/<note path>/<start-text hash prefix>`. Repeating a
   command continues its run by replay, and an edited note opens a new
   run. `--resume` is gone from `full-pass` and `revise`; the options a
   run recorded are reused when a repeat omits them.
3. **Gate verdicts in the full pass come from answers.** `gates.ask()`
   returns results without writing them; `gates.sweep()` writes them as
   they arrive. The full pass writes result files once, at its end, for
   the text the note then holds. The per-cycle report cache is deleted,
   and gate applicability is computed from the text under review.
4. **One mechanism for operator input**, `headless.operator.answer()`:
   the workflow proposes a file in the run and stops; on the repeat the
   file, edited or not, is the answer. The plan stop and the strike stop
   use it, and `--direction` is a recorded option.

The change is in kind, not in size: `src/` is about 30 lines larger
than before phase 5, because the documentation in docstrings grew by
more than the deleted machinery. A fifth candidate, dropping the closing
cycle's rerun of every method, was left out. It changes the method, and
the evidence is one live run.

None of phase 5 has run with a live worker.

## Phase 6, shared operations under two orchestrators

Recorded 2026-11-10 from a design conversation between the operator and
Claude (claude-fable-5-2). This phase is an architecture and a list of
candidates. Nothing in it is built. Statements marked "operator's
direction" were decided in that conversation; the rest is proposed.

The architecture has four parts:

1. **Operations.** Every step is a report, an edit or a write.
2. **A shared layer.** Instruction files, checks, the write and the file
   formats, reachable as commands over files.
3. **Two orchestrators.** Workjig sequences operations in Python. An
   agent sequences them in a conversation with ordinary sub-agents.
4. **One operator interface.** A worker proposes a file, and the
   operator's edited or unedited file is the answer.

Staging, by the operator's direction:

- **Remote goal: unification.** The two kinds of workflow share one
  layer, so a task can move between them by rewriting only its
  sequence. Nothing is built toward this yet, and the sections below
  describe it as the direction, not as the next work.
- **First step: similar, not necessarily identical.** Agent-run
  workflows take the same shape as the Workjig ones. They need not
  share code or exact file formats.
- **First step: try editing a report as the operator interface.** It
  is new and has not been tried beyond one simple case.

"Similar" is proposed to mean four things: the steps are named as
reports, edits and writes; a worker drafts into a working directory and
never into the library; code makes the one write, after code checks;
and an operator decision is a proposed file the operator may edit.

### Operations

The operator's observation: review has two kinds of operation,
generating reports and applying them to the note, and the full pass
combines them. Before phase 5 each intermediate text was saved in the
note. Since phase 5 they are saved in the run directory, and the note
changes once, after the pass ends. That separated a third, mechanical
operation from applying.

| Operation | Inputs | Output | Who | Changes the note |
|---|---|---|---|---|
| report | a text, an instruction, possibly other reports | a report file | worker | no |
| edit | a text, reports, an instruction | the next text, in a working directory | worker | no |
| write | the final text, the start text | the note | code | once, only over the start text |

On terms: "edit" here is the worker's step of applying reports to a
text. The code's `edits.apply()` is the write.

**Report.** A gate review, a critique, a method report, a connect report,
a packet, a closing status and a revision plan are all reports. They
differ in the contract code checks on the output: a strict result line,
a closed schema, or a report type's schema. A packet is a report whose
inputs include other reports. Reports never change a text, so they can
run in parallel and be repeated.

**Edit.** Each edit consumes the previous text, so edits run in order.
An edit also makes every report about the earlier text out of date.
That is why the full pass has a closing cycle. Code checks each edited
text against bounds that depend on the task.

**Write.** Code writes the final text once, only when the note still
holds the start text.

The current workflows as sequences:

- **Gate sweep:** reports over many notes.
- **Full pass:** reports on the start text; the packet; two edits (the
  editor, then the copyeditor); reports on the result; the closing
  status; at most one repair edit with its reports; write.
- **Revision:** one report (the plan), one edit per listed pass, write.

Two consequences:

- **A report belongs to a text, not to a file.** A result records the
  hash of the text the worker read. That text may be the note on disk or
  a text in a working directory. The full pass relies on this when it
  publishes its closing verdicts as fresh for the note it then writes.
- **The run's `artifact/texts/` is a private version chain.** Each text
  has the reports made about it. Only the final text reaches Git, so
  the per-step diffs are local to one machine.

### The shared layer

This section describes the remote goal. Operator's direction: the two
kinds of workflow become compatible in most details, so a task can move
between them. A task moves to Workjig when its bookkeeping grows, and
to an agent orchestrator when it needs flexibility.

A task can move only if everything except its sequence is the same on
both sides:

| Shared | Form | Today |
|---|---|---|
| the judgment | an instruction file that names its inputs and outputs and not who runs it | exists: the gates, `draft-ingest-report.md`, the connect skill used as an instruction in the full pass |
| the checks | code that takes an output and returns problems | Python only: the result-line parser, `decide()` schemas, `bounds()` |
| the write | one compare and write over the start text | Python only: `edits.apply()` |
| the files | result files, reports, candidate texts, the working-directory layout | review only |

An agent orchestrator can only call commands. So each check and the
write need a command in front of the function. A Python workflow calls
the function and an agent calls the command. Moving a task then means
rewriting its sequence, from prose to Python or back.

The first step does not need this. A similar agent-run workflow may
have its own commands and its own file layout. What it learns decides
which parts are worth sharing.

### The two orchestrators

What stays different:

- **Launching.** Workjig gives captured inputs, a restricted profile,
  launch records and replay. A sub-agent reads live files with the
  session's tools.
- **Pinning.** A Workjig worker reads a captured copy, so the recorded
  hash is exact. For a sub-agent, code hashes the inputs before dispatch
  and verifies them after, as ingest does with the snapshot checksum.
- **Provenance.** A result file records profile, launch and the model
  the harness recorded. A result from a sub-agent needs a truthful
  executor value.
- **Enforcement.** Python cannot skip a check. An agent can. The write
  command can refuse an unchecked candidate, but an agent can still
  write the file directly.

Three proposed conditions. The first applies from the first step; the
other two apply once tasks can move:

1. **The agent side gets only stateless commands**: functions over
   files, such as "check this output" and "write this text". ADR 127
   removed an agent orchestrator with a command per transition over a
   store. Commands that track jobs, attempts or locks would rebuild it.
2. **Run state is the signal to move.** A task that needs replay after
   a usage limit, attempt counting or many parallel calls moves to
   Workjig. A task that needs questions to the user, a choice of the
   next step, or tools the profiles deny moves to the agent.
3. **One orchestrator per task at a time.** A task is moved, not kept
   in a prose version and a Python version.

Where the tasks sit:

| Task | Orchestrator | Basis |
|---|---|---|
| gate sweep, full pass | Workjig | many calls; code decides the branches |
| ingest | agent | operator's direction: it does not move to Workjig, and it takes the similar shape |
| connect | agent as a skill; one plain call inside the full pass | one operation, so either side can ask it |
| revision | Workjig, unchanged for now | operator's direction; `readability-and-flow` may move out later |

On the revision: its passes differ in what they need.
`readability-and-flow` needs only the text and the purpose.
`narrow-overclaims` needs evidence that normally comes from the
conversation. `plain-wording` and `abstractions` need the operator to
strike a list. `split-out-a-treatment` never runs headless.
`audit-a-prior-pass` and one step of `place-external-systems` need
Bash, which the profiles deny. The workflow's bounds keep the title and
the H1, so it can apply only the TL;DR half of `opening-and-title`. A
split along this line was discussed and deferred.

### The operator interface

`headless.operator.answer()` from phase 5: the workflow proposes a file
and stops; the file, edited or not, is the answer on the repeat. The
revision plan and the strike lists use it. The operator wants this
interface tried. One live revision has used it, in its simplest case: a
pass added to an empty plan.

Its place in the architecture:

- **It turns a decision into an input.** The edited file has a hash
  like any other input, so a run stays a function of its inputs and
  replay still works.
- **It is a report the operator may amend**, so it needs no fourth
  operation.
- **It works on both sides.** On the agent side the operator can state
  the change in conversation and the agent edits the same file.
- **It lets an agent drive a Workjig run**: start it, bring the
  proposal to the operator, write the answer, repeat the command. The
  file does not record who edited it or on whose word, so an
  instruction that allows this must state that the agent does not
  decide for the operator.

What a trial should show:

- whether a file in a git-ignored, hash-derived run directory is
  practical to find and edit;
- whether the assessment gives enough to judge the plan without
  reading the whole note;
- what "unedited is an answer" does to approvals made without reading;
- whether the error for an invalid edit is enough to fix the file;
- whether the operator mostly removes passes, adds them or changes
  scope.

Decisions that could later take this form: the full-pass hand-back
(now a pending packet, a resolve instruction and `--direction`), the
choice of connect candidates to author, and the choice of warnings to
fix. None is converted before the trial.

### Connect and ingest

**Connect is a report with one difference**: its input includes the
corpus at the time of the search, which no hash of the note and the
instruction covers. It can carry no freshness claim, and its reports
stay regenerable under `kb/reports/cache/connect/`. Code can check two
things the skill now asks of the worker: the report matches
`kb/types/connect-report.schema.yaml`, and every candidate path exists.
Whether a label is authorised cannot be checked in code, because the
authorised set is prose in `COLLECTION.md`. Reverse-edge candidates
change other notes, and a write is one compare of one file, so they
stay report-only.

**Ingest keeps its sub-agents and takes the similar shape.** Its parent
agent now performs the deterministic parts by hand. With commands of
its own:

| Step | Who | What |
|---|---|---|
| prepare | code | resolve the target, hash the snapshot, extract the retained Quotes block, create a working directory keyed by slug and snapshot hash |
| report | sub-agent | connect on the snapshot |
| edit | sub-agent | draft into the working directory, not into `kb/sources/` |
| check | code | the handoff checks (snapshot checksum, Quotes block byte-equal, capture metadata, forbidden fields and links) and `commonplace-validate`; the failures feed one repair attempt |
| write | code | write the ingest once, only if the output path holds what prepare saw |
| report | sub-agent | connect on the accepted ingest |

The worker never writes `kb/sources/`, so the backup and the restore go
away, as the restore did in phase 5.

**Ingest reads external texts.** The snapshot is read and never
changed; the ingest is written. In the model the snapshot is an input
to the edit, as a criterion is in review, and the ingest's
`snapshot_sha256` pins it as a result file's hashes do. Review
freshness never depended on Git, so a text Git does not track needs no
new machinery. Four differences from review:

- Fetching is not a function of its inputs, because a URL can return
  other bytes later. Capture stays outside the run, which starts from a
  snapshot path.
- A changed snapshot is a new observation with a new ingest. It is not
  a stale ingest to regenerate.
- The checkout guard ignores git-ignored files, so it cannot see a
  snapshot change. The checksum comparison before and after the draft
  covers this.
- External text is untrusted and may address the reader. The drafting
  sub-agent has Write, Bash, Skill and Task. A restricted profile would
  be a safer reader; this is a known cost of keeping ingest on the
  agent side.

An ingest is a report in content and an edit plus a write in handling:
it lands in the tracked library, must pass checks and may replace an
incumbent. The model classifies it by handling.

### Candidates

None is decided unless marked. Each needs the operator's direction.

**First step.**

| Candidate | Reason | What holds it |
|---|---|---|
| Try the edited report on a live revision | the interface is untried; the revision already has it for the plan and the strike lists | costs paid launches, so the operator starts it |
| Ingest takes the similar shape: prepare, check and write commands of its own | the worker drafts into a working directory, code checks and writes once; removes the hand-performed checks and the backup | nothing; it need not reuse review's code |
| An edited report in one agent-run workflow | tries the interface on the agent side, for example striking connect candidates | wait for the revision trial |

**After the trial of the interface.**

| Candidate | Reason | What holds it |
|---|---|---|
| The full-pass hand-back as a proposed file | three mechanisms now serve one decision | the trial's result |

**Simplifications that do not depend on the staging.**

| Candidate | Reason | What holds it |
|---|---|---|
| Check the connect report in code | schema and path existence are deterministic | nothing |
| Drop `--resume`, `retry` and `acknowledge` from `run gates` | a rerun already skips fresh pairs, so replay only helps under `--force` | nothing; independent of live evidence |
| Keep one of `pair` and `bundle` | two groupings for one job | the verdict comparison of step 1.3 |
| Stop the guard from setting the exit code, or isolate workers in a worktree | no workflow writes mid-run now, and the guard cannot attribute a change | a worktree shows linked files at `HEAD` and hides ignored snapshots |

**Remote goal.**

| Candidate | Reason | What holds it |
|---|---|---|
| One set of commands in front of review's checks and write | both sides would call the same code | the first step shows which parts are worth sharing |
| An executor value in result files | a sub-agent's result must not claim a launch | no agent-side producer of results exists yet |
| Look up a report by text hash and criterion hash | a sweep and a full pass would share reports without reading each other's state | needs a rule for discarding reports about texts that exist nowhere |
| Merge the full pass and the revision | the full pass's editing step and a revision are both chains of edits | the revision stays as it is for now |

### Trials

For the first step:

- **One live revision with an operator-edited plan and at least one
  strike-list pass**, on the phase 5 code. It is the trial of the
  operator interface. It also gives the kept or reverted revision
  result the README asks for.
- **One live full pass on the phase 5 code**, which has not run with a
  live worker.

For the remote goal, when it is taken up:

- **Agent side to shared layer.** Have ingest call review's check and
  write. If they serve it unchanged, the layer is general.
- **Workjig side to agent.** Have an agent run one gate review and
  record it through a command. If `commonplace-review status` cannot
  tell that result from a sweep's, apart from the executor value, the
  file format is shared.

## Execution record

| Step | State | Commits |
|---|---|---|
| README update, phase 0 | done 2026-11-09 | `f85f19537` |
| 1.1 results and status | done, accepted unchanged | `7d2af63dd` |
| 1.2 gates workflow and command | done; the planner made criteria explicit for a sweep | `5ce47edc3`, `0bc400508`, `4e03cbcff` |
| retire the old code | done 2026-11-10 | `1e2027899`, `3562ca982` |
| 2 bundle grouping, `decide()`, full pass | done 2026-11-10 | `1b27a9b40`, `84fdda681`, `27d6ba9af`, `ef7b5a07c` |
| 3 profile per ask, revision | done 2026-11-10 | `07e2f984b`, `4422a531c` |
| 4 ADR and documents | done 2026-11-10 | `2fe4c0585` and the six commits after it |
| resume defects found in review | fixed 2026-11-10 | `7751d4f4c` |
| 5 one write, input-derived runs | done 2026-11-10 | `13ed322bf`, `563f4076b` |
| 5 gate results published once | done 2026-11-10 | `32c281ddd` |
| 5 one operator-input mechanism | done 2026-11-10 | `f9779b18f` |
| 6 two orchestrators: similar first, unified later | recorded 2026-11-10; nothing built | |
| 1.3 first sweep | waits for the operator | |

## Live runs

All on `kb/theory/definitions/storage-substrate.md` with the `sonnet`
profile, each a single observation.

| Run | Launches | Cost | Result |
|---|---|---|---|
| one gate, pair grouping (2026-11-09) | 1 | $0.095 | `pass`; 13 s; the rerun launched nothing |
| the `prose` bundle, bundle grouping | 1 | $0.172 | nine stale pairs reviewed, one fresh pair skipped; 31 s |
| full pass | 27 | $4.47 | `keep`, edited, closing `hand-back`, start text restored, packet pending |
| revision: assessment, then one operator-added pass | 2 | $0.235 | the assessor planned no pass; `readability-and-flow` returned no change |

The single-gate cost is almost all fixed context: the note and criterion
are about 2,000 tokens, and each of five turns reread roughly 30,000
tokens of harness and project context. Nine gates in one bundle call
cost about a fifth of nine pair calls. Whether one worker judges nine
gates as independently as nine workers is not measured, so the default
grouping stays `pair` until step 1.3 compares verdicts.

The full pass handed back because its closing premise check defeated a
sentence the pass had added, and the closing decision judged the repair
a claim-level choice for the author. The guard reported three files,
all edited by a worker building phase 3 in the same checkout at the
time.

No permission denial occurred in any run. No worker tried to write
outside its run directory, so the profiles' write restriction is still
unverified.

## Open

For the operator:

- **Step 1.3.** One collection, one profile, both groupings on the same
  notes. It decides the default grouping and whether the watched-parts
  hash is kept.
- **Keep or revert one result from each workflow**, which the README
  names as a closing condition. The full pass has run live only on its
  hand-back path; an accepted edit, a bounded repair and a non-keep
  packet are covered by fake-harness tests alone. The revision has not
  applied a change or stopped on a strike list live.
- **Delete the abandoned local data** in the main checkout:
  `kb/reports/state/commonplace-store.sqlite`, the
  `review-store.sqlite*` files, `review-store-backups/`, `review-jobs/`,
  `reviews/`, `bundle-reviews/` and `full-pass/`. Nothing reads them.
  The planning session did not delete untracked data.
- **Reinstall the user-level tool** so `commonplace-review` exists as a
  command and the 12 deleted launchers go away.
- **Read the paragraph added to**
  `kb/theory/many-to-many-edge-state-is-where-files-yield-to-a-database.md`.
  It records the return to files as evidence bearing on the note's
  claim.
- **Workshops whose subject was deleted**, proposed for closing:
  `review-evidence-and-disposition-hardening`,
  `artifact-freshness-and-referential-checks`,
  `freshness-module-review`, `review-bundle-packing`,
  `full-pass-instruction-coherence-audit`, and the review-storage thread
  of `src-architecture-alternatives`.
- **`collection-as-artifact-freshness`** is a proposal whose planned
  mechanism, the generic freshness store, no longer exists.
- **The mailbox message** on cost-per-yield records is unanswered. The
  result file carries no cost field; the launch records hold the
  harness's usage evidence.

Known limits of the code:

- The guard cannot tell a worker's change from another session's, so a
  long sweep in a busy checkout exits nonzero with paths to inspect.
- The codex profile can write the checkout at the sandbox level.
- A sweep with nothing stale still creates a run directory.
- `retry` of an answered pair needs `--force` on the rerun.
- A full pass no longer reuses fresh gate results from an earlier
  sweep; it asks every applicable gate, and replay covers a repeat.
- A finished run cannot be repeated for its report: the applied note has
  another hash, so the same command opens a new run.
- The review profiles deny Bash, so `audit-a-prior-pass` cannot read a
  diff and one step of `place-external-systems` cannot run.

Behaviour of the agent-run full pass that the workflow dropped or
changed:

- An undetermined update is not asked of the user mid-pass. The packet
  is pending, and the operator answers by repeating the command with
  `--direction`.
- The copyedit is accepted or rejected whole; code cannot apply only its
  in-bounds edits.
- The editor no longer rereads the friction and premise attention lines
  against the edited text. The closing cycle reruns both methods.
- A rejected packet no longer binds the next packet decision, and a
  changed pending packet is replaced by a new pass without a superseding
  step.
- A hand-back or undetermined packet is `pending` and blocks a new pass
  until it is resolved or the note changes.
- A worker problem or a spent call in any method stops the pass.
- The packet has no "Proposed revision shape" section and keeps the
  merge target's hash without a capture file.

Interactive revision behaviour the workflow does not cover is listed in
the "Run it as a workflow" section of
[revise an article or note](../../instructions/simplification-passes/revise-an-article-or-note.md).
