# Consumer surface: what a workflow's own code should need

## Question

[Requirements](./requirements.md) and [scenarios](./scenarios.md) fix the
engine's semantics. They do not say how much code a consumer must write to
live inside those semantics. The analysis workflow is the first consumer, and
its package `src/commonplace/lib/agentic_analysis/` is about 3,400 lines plus a
1,121-line `job-set.yaml`. The expectation was mostly declarations, with code
for checks whose logic is genuinely complex.

That count mixes layers. Roughly 1,550 lines are handlers (`handlers`,
`profile`, `verification`, `publication`, `checks`, `boundary`,
`acquisition`); about 950 are run setup and Git integration (`worktree`,
`checkout`, `report`, `ledger`); the rest is record parsing and shared
support (`records`, `sets`, `guards`, `validation`, `declaration`). The
expectation applies to the handler layer. Integration code is the
coordinator's side of the boundary and is measured separately.

This document reviews the boundary between the engine and that package after
the legacy engine was retired (`d3bd9a0ba`, `d279aba8f`). Each need a handler
shows is tested before anything is exposed:

1. Does the handler need it to produce its output or judgment?
2. Does it re-prove an invariant the engine already guarantees? Then the
   check is deleted, not served.
3. Does a declaration or design choice cause it? Then the choice changes.

Exposing less is the default; `api-design.md` deliberately has no storage API,
pin constructor or public engine object. One rule decides the shape of what
is exposed: values fixed by the declaration at start get accessors, as
`parameters` already does; everything versioned goes through `read()`.

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
only way in. The refusal format goes first: the header split is the most
fragile dependency on the list and its public subset is the smallest.

Weigh an address against a format for the attempt record before committing
to it. The field handlers mostly want is the delivered previous output, and
the `handed` address already routes a version named by a producer's record
through the input mechanism. A handed address for the previous output would
leave worker identity as the only field that needs a published format, and
only publication reads it.

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
requirements' one Open item. **Resolution:** the engine's `inspect` reports
stale acceptances, exhausted jobs and whether the run is settled, and answers
whether a named job's latest completed attempt is still current with its
outputs. Both reach-ins then disappear. This moves code into the engine; it
adds no handler capability. The Open item closes as "every invocation":
`inspect` reports stale acceptances whenever asked, and publication neither
reports nor refuses them. With the coverage gate below it is not ready until
coverage holds, and the report says why it waits.

"Settled" needs a glossary entry before it is implemented, as does the
narrow "completed" that the [publication handoff](./publication-consumer-handoff.md)
uses. Proposed: a run is settled when no job is ready and no attempt is
open, and the run is publishable, published or stopped by a failure or an
exhausted job. The leftover state, nothing ready, nothing open, not
publishable and not stopped, is a stuck run; `inspect` names it as such
rather than the specification arguing it cannot occur. Whether it can is an
engine test.

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
  keeps this an environment check at open and publish. The guard is not
  only a check: it returns the metadata and the repository path that every
  caller uses afterwards (`handlers.py:168-179`). The change is a split
  into a cheap locate step and the removal of the checks, not a deletion.

These change no design and can go first. The provenance checks that survive
are the producer's name and kind and the worker identity.

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

## Resolutions at requirement level

Discussed 2026-10-08; each amends the requirements or a scenario as stated.

### The set type is fixed for the run

`start_run` fixes layout and relations in `run.json`, and the engine
schedules, scopes and computes coverage from that copy. Handlers read the
set type as a pinned file input (13 `set-type` inputs), so a mid-run edit
makes them validate against a layout the engine does not use.
`publication.py:42` imports the private `_parse_type` for this.

One side was already decided. Jobs are declared against the type's roles,
relation names are checked against the type at start, and the Decisions
count a mid-run edit of the declaration as a method change that makes the
run unpublishable. The layout cannot follow a live edit whatever the
handlers read. Scenario 8 does not require otherwise: the contracts it
edits are member types and schemas among a check job's inputs, and those
stay live file inputs. The set type says what the set is, and the run was
started against one answer to that.

**Resolution:** the set type is part of the fixed declaration. Delete the
13 `set-type` inputs, then expose the parsed layout and relations on
`CodeAttempt`. The accessor hides the split only while the file inputs
remain; once they are gone the engine's copy is the one source. Exposing
the parsed value rather than the type bytes keeps the parser private.
Analysis runs already pin a commit in a worktree, so fixing the type
changes nothing they do today. Amends requirement 1 (the set type is named
by the declaration and fixed with it) and the Decision on the fixed
declaration.

### Coverage is an engine-derived input

Requirement 9 says a code job checks coverage, and a handler reads only its
inputs. Together they produce 186 `coverage-*` and 21 `*-accepted` judgment
inputs on `assemble` and `publish` and the recomputation in
`publication._snapshot` (`:92`), which duplicates `Run.publishable()`. The
two can diverge: the engine scans every judgment for one that holds and
covers, while the handler reads the latest judgment at each address and
tests only that one, so a later non-holding acceptance hides an earlier
holding one.

The shape also makes assembly fail where it should wait. `assemble` requires
only the boundary acceptance; every other member, attempt and coverage input
is optional. When a relation is uncovered, `_snapshot` raises `ValueError`,
which requirement 8 treats as a code-job failure that stops the invocation.
An ordinary intermediate state, a verification not yet accepted, is thus
reported as a failure. This is a defect in its own right and the strongest
evidence for the gate; it also rules out exceptions as a handler's way of
saying "not yet" anywhere else.

The case for the inputs is auditability: the attempt record pins exactly
which acceptances backed the publication. A gate loses that unless its
version carries it.

**Resolution:** the engine determines coverage and supplies it as a derived
input address that a job declares like any other. Its version is a
canonical digest over the covering claims, sorted, together with the member
versions, so the publication record still names its evidence. Claims, not
judgment-record ids: the judgment address already uses claim identity
(`state.py:217`) so that an apply job re-recording an unchanged verdict is
no change, and coverage must not rerun `publish`, an external effect, for
the same non-event. Member, judgment and refusal inputs are already
engine-derived views; this adds no new category. Declared required, it makes
`publish` not ready until coverage holds, which is what scenario 10 already
expects. Its producers for the pending-producer wait are those of a judgment
input. Amends requirement 9: the engine determines coverage; a code job
copies the current versions out, pinned.

The input's scope is derived, not declared. `assemble` fills the `overview`
role and judges the overview itself, while the `overview:*` relations sit on
`publish` (`job-set.yaml:919-930`). A whole-set coverage input on `assemble`
would depend on its own judgment, which requirement 1 forbids and which
would rerun it without end. So a coverage input covers the relations not
touching the declaring job's role; `publish` has no role and gets the whole
set. No new field is needed.

The gate forces one semantic gap into the open. `Run.publishable()` checks
relation coverage only. The handler additionally requires a holding
acceptance of every member. These differ for a member with no relation to
another present member, such as a blocked disposition holding only a
boundary: its acceptance can go stale while the member stays (requirement
6), and the engine calls the set publishable where the handler refuses.
**Resolution:** the stricter reading. A set is publishable when every role
the disposition requires is present, some holding acceptance exists for
each current member, and every relation between members is covered.
Requirement 9 states all three conditions. The first is not implied by the
other two: with only an accepted complete-disposition boundary, coverage
among present members holds trivially, and only the pending-producer wait,
a scheduling accident, would keep `assemble` off a partial set.

A coverage input applies all three conditions to the derived scope: the
declaring job's own role is excluded from the required roles and from the
member acceptances as well as from the relations, so `assemble` does not
wait for the overview it writes.

## Outside the handler surface

- **Criteria declarations.** `job-set.yaml` has 329 file inputs, mostly the
  same type and schema files repeated per check job, and
  `agentic_analysis/validation.py` mirrors their names in a `CRITERIA` table.
  A per-job criteria group in the declaration would shrink the file more than
  any change above, and it is the one item that touches scenario 8's
  live-criteria behaviour. It needs a section of its own, not a deferral.
- **Duplicated utilities** (atomic write, locks, Git wrappers, path
  containment) are ordinary refactoring, not engine design.

## Order and acceptance

Order: the guard split and the deletions; the refusal format; the
attempt-record decision (published subset or handed address) and its
implementation; the fixed set type and its accessor; the coverage gate with
the stricter publishable rule; engine-owned inspection and locking; then the
criteria-declaration section. Each step leaves the tests passing.

Every design step begins by amending the specification texts, not by code.
The resolutions above touch requirements 1 and 9, the fixed-declaration
Decision, the Open item and scenario 10; they add glossary entries for
settled, the narrow completed and the coverage address; and they add
`inspect`, the layout and relations accessors and the coverage address to
`api-design.md`. The first done criterion depends on those additions, since
`inspect` is not a public name there today.

Review before steps 3 to 5 (2026-10-08) found two further reach-ins the
inspection step must absorb. `worktree.py:418,524` takes the store's lock
directly, and `cli/workflow.py:54-59` both locks and reads a version's bytes
from the store, which is the storage API the design says does not exist.

Done when:

- the analysis package and the CLI import nothing from `commonplace.workflow`
  except the public names in `api-design.md`, locking and version reads
  included;
- no handler reads the set type as a file input or parses it;
- `job-set.yaml` has no `coverage-*` or `*-accepted` inputs, and `assemble`
  is not ready, rather than failing, while a relation is uncovered;
- scenarios 8 and 10, the blocked-disposition gap, the unchanged re-recorded
  verdict, the stuck-run state, and a complete-disposition run with only the
  boundary accepted, where `assemble` is not ready, are tests;
- the handler layer's line count is reported against the expectation,
  separately from integration and support.
