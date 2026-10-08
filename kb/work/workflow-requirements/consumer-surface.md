# Consumer surface: what a workflow's own code should need

## Question

[Requirements](./requirements.md) and [scenarios](./scenarios.md) fix the
engine's semantics. They do not say how much code a consumer must write to
live inside those semantics. The analysis workflow is the first consumer, and
its package `src/commonplace/lib/agentic_analysis/` is about 3,400 lines plus a
1,121-line `job-set.yaml`. The expectation was mostly declarations, with code
for checks whose logic is genuinely complex.

This document reviews the boundary between the engine and that package after
the legacy engine was retired (`d3bd9a0ba`, `d279aba8f`). Each need a handler
shows is tested before anything is exposed:

1. Does the handler need it to produce its output or judgment?
2. Does it re-prove an invariant the engine already guarantees? Then the
   check is deleted, not served.
3. Does a declaration or design choice cause it? Then the choice changes.

Exposing less is the default; `api-design.md` deliberately has no storage API,
pin constructor or public engine object.

## Legitimate needs

### Published formats for attempt-record and refusal inputs

Requirement 1 makes attempt records declarable inputs, and requirement 7 makes
a job's refusals one. Their bytes are engine internals today:

- An `attempt` input resolves to the canonical JSON of the whole internal
  record, pins and sequence numbers included (`state.py` `resolve`). Handlers
  `json.loads` it (`handlers.py`, `profile.py`, `verification.py`,
  `publication.py`).
- A `refusal` input is an engine-rendered text header followed by the
  findings. `checks.py:19` removes the header by splitting at the first blank
  line, so a change of the rendering would silently break correction checks.

The fields consumers legitimately use are few: `previous_outputs`, to refuse
"corrected" over unchanged bytes; worker identity, which the retained
manifest records; the attempt id, named in correction feedback; and the
refusal's findings. **Proposal:** document a public subset of each format and
make the engine produce exactly it. No accessor is added; `read()` stays the
only way in.

### Engine-owned run inspection

Two modules reach past `CodeAttempt` into engine internals:

- `report.py` uses `inspect`, `Run` and `RunStore`, and calls `ready`,
  `permitted`, `holds`, `attempt_count`, `latest_completed` and `members` to
  compute stale acceptances, exhausted jobs, canonical-peer drift and
  "completed".
- `worktree._integration_publication` (`:402`) resolves the publish job's
  pins itself, compares them with its completed record, checks every job for
  open, failed or ready attempts, and constructs a `CodeAttempt` by hand to
  call the private `publication._prepare_publication` (`:443`).

None of this is analysis-specific. Stale acceptances are the
requirements' one Open item. **Proposal:** the engine's `inspect` reports
stale acceptances, exhausted jobs and whether the run is settled, and answers
whether a named job's latest completed attempt is still current with its
outputs. Both reach-ins then disappear. This moves code into the engine; it
adds no handler capability.

## Deletions: checks that re-prove engine invariants

- **Completed-state checks.** `profile.py:93` and `verification.py:202`
  require `state == "completed"`; the `attempt` address resolves only
  completed attempts.
- **Output-digest checks.** `profile.py:95` and `publication.py:141-143`
  compare the recorded output with the candidate's digest; the engine resolved
  the candidate from that record.
- **Environment guards in intermediate jobs.** `_opened_environment` and
  `_require_opened_method` appear 29 times (handlers 9, verification 8,
  profile 7, publication 5). The Deferred item *Validator code identity*
  keeps this an environment check at open and publish.

These change no design and can go first.

## Not needs

- **A version accessor.** Identity is the content hash (requirement 4), so a
  consumer computing `sha256` uses a public rule.
- **Role-keyed snapshots.** The input-name tables (`-seen`, the `profile`
  alias in `profile.py:35`) come from inconsistent input naming in
  `job-set.yaml`. Rename the inputs; roles stay internal.
- **Splitting `run_dir`.** Its uses are the set path, which a Decision fixes;
  the run id, which is the directory name; effect journals, which
  `api-design.md` leaves consumer-owned; and the opening guard. Each is
  legitimate and none needs its own accessor.
- **A default judgment scope.** Scopes are explicit by design. A default
  could claim coverage of a relation the check never examined.

## Design questions at requirement level

- **Two sources of truth for the type.** `start_run` fixes layout and
  relations in `run.json`, and the engine schedules, scopes and computes
  coverage from that copy. Handlers read the set type as a pinned file input
  (13 `set-type` inputs), which follows criteria edits as scenario 8 expects.
  An edit mid-run makes handlers validate against a layout the engine does
  not use. `publication.py:42` imports the private `_parse_type` for this.
  Exposing `attempt.layout` would hide the split, not settle it. The question
  is whether the type is fixed for the run or a live criterion.
- **Publication coverage.** Requirement 9 says a code job checks coverage,
  and a handler reads only its inputs. Together they produce 186 `coverage-*`
  and 21 `*-accepted` judgment inputs and the recomputation in
  `publication._snapshot` (`:92`), which duplicates `Run.publishable()`. A
  declared publishable gate, pinned by the engine, would remove both.
  It amends requirement 9 and scenario 10.

## Outside the handler surface

- **Criteria declarations.** `job-set.yaml` has 329 file inputs, mostly the
  same type and schema files repeated per check job, and
  `agentic_analysis/validation.py` mirrors their names in a `CRITERIA` table.
  This is a declaration-grouping question for a later section.
- **Duplicated utilities** (atomic write, locks, Git wrappers, path
  containment) are ordinary refactoring, not engine design.
