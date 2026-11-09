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
| Reuse of the old package | the new code imports pure helpers from `commonplace.review` (criterion resolution, applicability, conformance pairs, the outcome parser, note-part extraction) and nothing that opens the store | the helpers survive; phase 4 moves them when it deletes the rest |
| Review profiles | `kb/instructions/review-profiles.yaml`, same entry shape as `kb/tasks/profiles.yaml`, without edit or commit grants on the checkout | a task profile may commit; a review worker may not |

Not decided here: installed projects, where gates resolve through the
installed library root. Phase 1 runs in this checkout only. The
identities must not foreclose the library form, and phase 4 settles it
before the old commands are deleted.

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

### Step 1.3, the first sweep (operator)

One collection with one profile. It costs real launches, so the operator
chooses the collection and profile and starts it. It decides:

- call granularity (README item 3), from the usage evidence of the
  launches against one bundle call on the same notes;
- whether the watched-parts hash is kept;
- whether the result file carries the cost and boundary field asked for
  in the mailbox message
  `kb/messages/20261030T085047Z-economics-workshop-unattended-workflows-cost-per-yield-records.md`.
  The reply is written then.

## Later phases

**Phase 2, the full pass** (README item 6). It starts when step 1.3 has
kept or changed the result file. Its first step is the `decide()` helper
with the packet schema. It returns to planning before any code if the
gate sweep shows that a launch's fixed cost makes six parallel method
asks per note too expensive.

**Phase 3, one revision** (README item 7). It needs `ask` to accept a
profile, which changes `headless/jobs.py` and therefore requires the
`headless/` and `agentic_analysis/` suites. That change waits for this
phase, because no earlier workflow needs it. The operator's judgment of
the stop-and-rerun shape decides whether the workflow replaces the
interactive skill.

**Phase 4, retirement.** It starts when the operator has kept or reverted
one result from each workflow. The latest safe point to settle the
installed-project identities and the fate of `commonplace-status`'s
review section is before the first deletion.

## Execution record

| Step | State | Commit |
|---|---|---|
| README update, phase 0 | done 2026-11-09 | with this plan |
| 1.1 results and status | done 2026-11-09, Opus worker, accepted unchanged | `7d2af63dd` |
| 1.2 gates workflow and command | done 2026-11-09, Opus worker in a worktree; the planner made criteria explicit for a sweep | `5ce47edc3`, `0bc400508`, `4e03cbcff` |
| 1.2 live pair | done 2026-11-09, see below | |
| 1.3 first sweep | waits for the operator | |

## Live pair, 2026-11-09

`commonplace-review run gates kb/theory/definitions/storage-substrate.md
--criteria prose/source-residue` with the default `sonnet` profile wrote a
`pass` result on the first attempt. The rerun launched nothing and
`status` showed the pair fresh.

| Measure | Value |
|---|---|
| wall time | 13 s |
| harness-reported cost | $0.095 |
| turns | 5 (three reads, one write) |
| context read from cache | 95,525 tokens over the turns |
| context written to cache | 18,399 tokens |
| output | 1,201 tokens |
| permission denials | 0 |

The cost is almost all fixed context: the note and criterion are about
2,000 tokens together, and each turn rereads roughly 30,000 tokens of
harness and project context. At this rate all 43 gates on one note cost
about $4 as 43 calls. This is one observation, and it points the
granularity decision of README item 3 toward one call per note and
bundle; step 1.3 measures a bundle call on the same note before deciding.

What the live pair did not show:

- that the profile denies a write outside the run directory. The worker
  did not try one. The guard is the only verified control.
- the `opus` and `codex` profiles. The codex profile can write the
  checkout at the sandbox level, which its comment states.

## Open after step 1.2

- **The guard fails a sweep when another session edits the checkout.**
  It reports every path that changed while the run was open and cannot
  tell whose change it was. In this checkout other sessions commit
  several times an hour, so a long sweep will usually exit nonzero with
  paths to inspect. Step 1.3 shows whether that is useful or noise.
- **A sweep with nothing stale still creates a run directory.**
- **`retry` of an answer needs `--force` on the rerun**, because the
  written result makes the pair fresh.
- **The prompt is part of each call's identity.** Editing
  `gates.PROMPT` relaunches calls on `--resume`; it does not stale
  results, which hash only the note and the criterion.
- **Directory expansion is reimplemented** in `gates.note_paths`,
  because the old selector module imports the store.
