# Consumer surface: what a workflow's own code should need

## Question

[Requirements](./requirements.md) and [scenarios](./scenarios.md) fix the
engine's semantics. They do not say how much code a consumer must write to
live inside those semantics. The analysis workflow is the first consumer, and
its package `src/commonplace/lib/agentic_analysis/` is about 3,400 lines plus a
1,121-line `plan.yaml`. The expectation was mostly declarations, with code
for checks whose logic is genuinely complex.

That count mixes layers. Roughly 1,550 lines are handlers (`handlers`,
`profile`, `verification`, `publication`, `checks`, `boundary`,
`acquisition`); about 950 are run setup and Git integration (`worktree`,
`checkout`, `report`, `ledger`); the rest is record parsing and shared
support (`records`, `sets`, `guards`, `validation`, `plan`). The
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
  record, pins and sequence numbers included (`run.py` `resolve`). Handlers
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
- **Output-digest checks.** `profile.py:95` compares the recorded output with
  the candidate's digest; the engine resolved the candidate from that record.
  The similar check in `publication._provenance` stays: there the subject is
  the current member, which can be older than the producer's latest completed
  output, so the digest is what ties the worker identity to the published
  member.
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
  `plan.yaml`. Rename the inputs; roles stay internal.
- **Splitting `run_dir`.** Its uses are the artifact path, which a Decision fixes;
  the run id, which is the directory name; effect journals, which
  `api-design.md` leaves consumer-owned; and the opening guard. Each is
  legitimate and none needs its own accessor.
- **A default judgment scope.** Scopes are explicit by design. A default
  could claim coverage of a relation the check never examined.

## Resolutions at requirement level

Discussed 2026-10-08; each amends the requirements or a scenario as stated.

### The artifact type is fixed for the run

`start_run` fixes layout and relations in `run.json`, and the engine
schedules, scopes and computes coverage from that copy. Handlers read the
artifact type as a pinned file input (13 `set-type` inputs), so a mid-run edit
makes them validate against a layout the engine does not use.
`publication.py:42` imports the private `_parse_type` for this.

One side was already decided. Jobs are declared against the type's roles,
relation names are checked against the type at start, and the Decisions
count a mid-run edit of the declaration as a method change that makes the
run unpublishable. The layout cannot follow a live edit whatever the
handlers read. Scenario 8 does not require otherwise: the contracts it
edits are member types and schemas among a check job's inputs, and those
stay live file inputs. The artifact type says what the artifact is, and the run was
started against one answer to that.

**Resolution:** the artifact type is part of the fixed declaration. Delete the
13 `set-type` inputs, then expose the parsed layout and relations on
`CodeAttempt`. The accessor hides the split only while the file inputs
remain; once they are gone the engine's copy is the one source. Exposing
the parsed value rather than the type bytes keeps the parser private.
Analysis runs already pin a commit in a worktree, so fixing the type
changes nothing they do today. Amends requirement 1 (the artifact type is named
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
(`run.py:217`) so that an apply job re-recording an unchanged verdict is
no change, and coverage must not rerun `publish`, an external effect, for
the same non-event. Member, judgment and refusal inputs are already
engine-derived views; this adds no new category. Declared required, it makes
`publish` not ready until coverage holds, which is what scenario 10 already
expects. Its producers for the pending-producer wait are those of a judgment
input. Amends requirement 9: the engine determines coverage; a code job
copies the current versions out, pinned.

The input's scope is derived, not declared. `assemble` fills the `overview`
role and judges the overview itself, while the `overview:*` relations sit on
`publish` (`plan.yaml:919-930`). A whole-artifact coverage input on `assemble`
would depend on its own judgment, which requirement 1 forbids and which
would rerun it without end. So a coverage input covers the relations not
touching the declaring job's role; `publish` has no role and gets the whole
artifact. No new field is needed.

The gate forces one semantic gap into the open. `Run.publishable()` checks
relation coverage only. The handler additionally requires a holding
acceptance of every member. These differ for a member with no relation to
another present member, such as a blocked disposition holding only a
boundary: its acceptance can go stale while the member stays (requirement
6), and the engine calls the artifact publishable where the handler refuses.
**Resolution:** the stricter reading. An artifact is publishable when every role
the disposition requires is present, some holding acceptance exists for
each current member, and every relation between members is covered.
Requirement 9 states all three conditions. The first is not implied by the
other two: with only an accepted complete-disposition boundary, coverage
among present members holds trivially, and only the pending-producer wait,
a scheduling accident, would keep `assemble` off a partial artifact.

A coverage input applies all three conditions to the derived scope: the
declaring job's own role is excluded from the required roles and from the
member acceptances as well as from the relations, so `assemble` does not
wait for the overview it writes.

## Criteria declarations

After the steps above, `plan.yaml` (775 lines) declares 316 file inputs
over 55 distinct files. The same contracts, type specs and schemas recur on
up to 23 jobs: `agentic-analysis-sources.md` 23 times, each analyst type and
schema 12 times. Every check job lists its candidate's type closure by hand,
and two declaration tests verify that each list is closed under schema
`$ref`s. `agentic_analysis/validation.py` repeats the alias-to-path mapping
as a `CRITERIA` table so that a handler can hand the validator its pinned
bytes keyed by library path. The validator fails closed on a missing file,
so an incomplete list is a refused member, not a silent pass.

Scenario 8 fixes what any change must keep: each criterion stays a live
file input of the job that applies it, pinned at hand-out, a rerun trigger,
and part of the judgment's basis.

Two shapes keep that:

- **Named groups in the declaration.** The plan declares groups of
  library paths once, and a job lists the groups it applies. The loader
  expands each group into ordinary file inputs, so pinning, currency and
  bases are unchanged and the engine learns nothing about types or
  schemas. A code attempt returns its pinned file inputs keyed by library
  path, which replaces the `CRITERIA` table. The closure tests then check
  the groups, not every job.
- **Engine-derived closure.** A job names the roles whose types it applies,
  and the engine pins each type spec, its schema and their `$ref` closure.
  This removes the lists and the closure tests, but the engine would parse
  schema references, which is validator knowledge, and a criterion a job
  depends on would no longer be visible in the declaration.

**Recommendation:** named groups. They remove the repetition without moving
validator knowledge into the engine, keep every dependency readable in the
declaration, and change no requirement: requirement 1 already makes
contracts inputs, and a group is declaration syntax for several of them.
The Decision on the plan file gains the group syntax; the API design
gains the path-keyed read of pinned file inputs. Estimated effect: about
300 lines of input declarations become about 60 lines of groups and a few
references per job.

## Check skeleton

After the steps above, nine code jobs judge a model candidate: the boundary,
three analyst, reconciliation, profile and synthesis checks, and the first
half of the three verdict applications, which judge the verdict document
before parsing it. Each runs the same skeleton, written four times
(`handlers.check_boundary`, `handlers._check_analyst`,
`verification._candidate_reasons` with `check_reconcile`, and
`profile._check` with `_apply`):

1. locate the run's metadata and checkout;
2. read the candidate;
3. snapshot the partner members at their artifact paths, from current member
   inputs or, in verdict applications, from handed `-seen` inputs (three
   implementations);
4. validate the candidate as a draft at its role against that snapshot and
   the pinned criteria, keeping failures as `[set]` reasons;
5. check the boundary's frozen source as `[invocation]` reasons;
6. compare candidate identity fields with the opening metadata;
7. check correction answers against the refusal the producer answered;
8. judge the candidate, refused with a findings packet that carries the
   answered blockers forward, or accepted with a hand-written scope.

Reading the four copies side by side shows more than repetition:

- **Step 6 mostly re-proves the type.** The artifact type makes every member
  copy `run-id` and `reviewed-boundary` from the boundary, and the profile
  copy `source-identity` from the memory report. Draft validation in step 4
  checks those identity relations against the snapshot, and the boundary
  check already binds the boundary to the opening. What remains genuinely
  per job is small: the profile's comparison version, and the memory
  report's source identity, which the boundary check does not cover.
- **The copies disagree.** The boundary check keeps validation warnings as
  refusal reasons; the others drop warnings. Verdict applications refuse
  with plain reasons; the others build a findings packet. Neither
  difference is stated as intended.
- **Step 8's scope is derivable.** Each hand-written scope is the type's
  relations from the candidate's role to the partners in the snapshot, which
  are exactly the relations step 4 validated. Deriving the scope from the
  snapshot claims no relation the check did not examine, which is the
  objection that ruled out an engine-level default scope above.

Three shapes:

- **A consumer helper.** One function in the analysis package takes the
  attempt, the candidate's role, the partner roles and where their versions
  come from, and returns the reasons of steps 3 to 5 and 7. One more judges
  the candidate with a derived scope and the findings packet. Each handler
  keeps only its domain checks: boundary source refusals, the memory
  source identity, the profile comparison version, limit carrying and
  verdict parsing. The engine is unchanged, which respects the non-goal of
  engine-level validation policy.
- **A declared generic check.** One handler serves every check job, with
  role, partners and extra checks named in the declaration. Code jobs have
  no parameters today, so this needs an engine change, and it hides the
  per-job domain checks behind names in YAML.
- **Engine-generated check pairs.** The mapping's remark that "a
  declaration default could generate these pairs". The engine would know
  what a content check is, which the non-goals exclude.

**Recommendation:** the consumer helper, together with deleting the step-6
checks the type already enforces and settling the two disagreements as
deliberate choices or defects. This changes no requirement or decision.
Estimated effect: the four copies, about 250 lines, become a helper of
about 80 lines plus per-job domain checks. Implementation must first
confirm that draft validation enforces the identity relations for a
candidate whose partners are in the snapshot, since the deletion rests on
it.

**Implemented (2026-10-08)** as `agentic_analysis/candidate.py`. Draft
validation reports identity mismatches as failures of the candidate's role,
so the step-6 checks were deleted. Two remain: the memory report's source
identity, and the profile's comparison version, which the schema leaves
optional. Both disagreements were treated as defects: every check now
refuses on failures only, with the findings packet, and the packet also
carries the answered refusal's limits. Every check scopes a refusal as it
would scope an acceptance; a verdict leaves out its subjects either way.
`apply-verify` gained the answered refusal the other applications declare,
the handed profile input is named by its role, and the nine jobs that no
longer read the opening metadata no longer declare it. The four copies,
about 340 lines, became a 129-line helper plus per-job checks; the package
shrank by 76 lines, less than estimated, because the helper keeps
docstrings and also serves the record-check job.

## Refusal and correction protocol

A verdict's `## Blockers` become refusals of its subjects. The producer
answers each blocker in its `answers` output with `- corrected: ` or
`- declined: ` and a reason, and its check tests the count, the grammar, and
that a corrected answer comes with changed bytes. A structural refusal
carries the answered refusal's blockers, cited records and limits forward,
because only the latest refusal is in force (requirement 7) and the verifier
reads the answers to its own blockers. The code is about 150 lines:
`checks.py`, the routing in `verification.py` (`_blockers`, `_entries`,
`_addressee`, `_feedback`) and the subject judgment in `profile._apply`.

- **Nothing moves to the engine.** Answer checks count entries in the
  refusal's body, which is a consumer format. Accumulating obligations in
  the engine would replace the ten-line carry-forward with a multi-valued
  refusal input and a changed requirement 7.
- **The routing re-proves the type.** The verification type's validation
  (`validation._verification_findings`) already refuses a Blockers section
  that is not `none` or a list, and a record blocker without a report
  addressee. `review` runs it, so `_blockers`' grammar and addressee checks
  repeat it. Parsing the entries is all that remains.
- **Three blocker parsers.** `correction_blockers` counts `- ` lines,
  `verification._entries` joins continuation lines, and `profile._apply`
  takes the section whole. One entry parser serves all three.
- **The grammar is stated six times.** The shared worker rules, which every
  model job receives, state it. The records contract states it for
  analysts, and four job instructions restate it. The job instructions need
  only what is specific to the job.

**Recommendation:** delete the re-proving grammar checks, share one entry
parser, and trim the instruction restatements to their job-specific parts.
No requirement or engine change. The effect is small, about 30 lines of
code: the protocol is mostly legitimate domain logic.

## Layers

The generic checks are neither scheduling nor analysis, so they are the
engine's reuse modules (2026-10-09):

- `commonplace.artifactrun`, the engine. Its scheduling knows nothing of
  validation, Git or files outside its store. Its reuse modules serve any
  consumer of a typed artifact: the compact-plan loader (`compact`), the
  standard check, verdict application and artifact check (`handlers`), candidate
  checks and the correction protocol (`checks`), frozen external sources and
  their acquisition (`sources`), the journaled directory install
  (`effects`), commit-bound worktrees and branch-and-merge transfer
  (`worktree`), and the run report (`report`).
  They depend on `commonplace.lib`, never on a consumer; a test enforces
  that.
- `commonplace.lib.agentic_analysis`, the domain: the handlers of its own
  code jobs, the declared checks and feedback its compact plan names, record
  and ledger rules, boundary semantics, assembly,
  the publication proof, and the paths, run naming and role names it passes
  to the engine's reuse modules as arguments.

The artifact type reaches the checks from the run (`CodeAttempt.type_spec`), not
a constant. A structural refusal now carries every section of the answered
refusal except Findings and Blockers, so `artifactrun/checks.py` names no
analysis section. The analysis data modules (`analyses`, `records`, `ledger`) must import
without the engine, so the helpers they share with the reuse modules moved to
`commonplace.lib` (`note_parser.section`, `source_identity`).

The analysis type rules now live in `agentic_analysis.rules` and register
through the validator's `type_rule` and `directory_type_rule` tables. The
validator imports that module once, by name, at the end of
`lib/validation.py`; that line is the only reference left from generic
validation to the analysis. The pinned-set adapter takes the set type as an
argument (`validate_pinned_set_snapshot`), and the frozen Git reader moved
to `quote_grounding`.

`systems_matrix` stays in `commonplace.lib`. It reads retained analyses for
the landscape synthesis in `kb/agentic-systems`, a second consumer of the
analysis data modules, not part of the analysis workflow.

## Outside the handler surface

- **Duplicated utilities** (atomic write, locks, Git wrappers, path
  containment) are ordinary refactoring, not engine design.
- **The publication journal is the effect's recovery record.** Integration
  no longer reads it (2026-10-08). The publish receipt, the retained tree
  and the archive compared with the method commit's incumbent prove
  everything the journal's intent, `old`, `archive` and `state` fields did.
  Acquisition and publication journals differ in shape and recognition, so
  only the atomic write is shared.

## Order and acceptance

Order: the guard split and the deletions; the refusal format; the
attempt-record decision (published subset or handed address) and its
implementation; the fixed artifact type and its accessor; the coverage gate with
the stricter publishable rule; engine-owned inspection and locking;
criteria groups; then the check skeleton. Each step leaves the tests passing.

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

- the analysis package and the CLI import nothing from the engine's core
  modules except the public names in `api-design.md`, locking and version
  reads included;
- no handler reads the artifact type as a file input or parses it;
- `plan.yaml` has no `coverage-*` or `*-accepted` inputs, and `assemble`
  is not ready, rather than failing, while a relation is uncovered;
- scenarios 8 and 10, the blocked-disposition gap, the unchanged re-recorded
  verdict, the stuck-run state, and a complete-disposition run with only the
  boundary accepted, where `assemble` is not ready, are tests;
- the handler layer's line count is reported against the expectation,
  separately from integration and support.
