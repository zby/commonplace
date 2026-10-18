# Batch 21 correction mechanism: eight conditional routes, one blocker

## Decision and authority

**STOP the proposed uniform nine-case route.** Resetting at the earliest
verifier preserves the intended author witness for eight cases, but not for
AREX-Skill: resetting `report-verification` removes `synthesis` and its
installing acceptances. There is then no synthesis member to refuse, and no
latest synthesis output to drive its correction input. Also, **neither current
origin nor any of these nine frozen CLIs supports `--findings-file`**. All
support `--findings TEXT`. A parent wrapper may read a pinned file and pass its
text as one argument; it must not claim that option is native.

This is the operator's read-only preparation commission, not launch authority.
Only this new report is owned. No workers were launched; no sources, installs,
state transitions, native reset/judge/advance/handout commands, target execution,
integration or commits were performed. No worker prompts or logs were read.
Existing audit findings are inputs, not freshly confirmed semantic judgments.
The report provides conditional mechanism details, not clearance to execute the
eight-case subset or invent a ninth route.

The intended end state of any later released correction is a renewed,
independently audited exact-byte publication, retaining predecessor run and
publication evidence. A native acceptance alone does not establish that state.
The parent should not implement a launchable nine-case batch from this report.
Return AREX's scope/feedback-placement decision to the operator; do not repair
state, patch frozen methods, substitute an aspect author, or use an old version
as a way around the missing member.

## Evidence and read-only checks

Primary bindings are [the batch record](./batch-21.json),
[the case contracts](./batch-21.md), and
[the explicit AI Memex pilot](./reentry-pilots.md). The pilot's second reset at
`synthesis-verification`, followed by operator refusal `000038-operator-0`,
kept synthesis installed and delivered the public-qualification requirement.
It establishes one feedback-assisted route, not arbitrary reset-point safety.
The initial no-feedback trial did not repair the claim.

Origin HEAD during this review was
`f12f9a7467f4b01a5777bf8f65f109560b05e848`. Relevant implementation:

- `src/commonplace/artifactrun/reset.py:41–101,142–251`:
  `affected_jobs`, archive preparation, operator withdrawal, budget floor,
  effect snapshots and interrupted-reset roll-forward.
- `src/commonplace/artifactrun/engine.py:177–227,346–361,389–449,477–581`:
  `judge`, current outputs, refusal answers, materialization and scheduling.
- `src/commonplace/artifactrun/run.py:104–113,117–195,238–247,278–327,439–480`:
  attempt counts, installed members, refusal selection, readiness and coverage.
- `src/commonplace/artifactrun/store.py:73–96,157–168`:
  lock acquisition and judgment-first/completed-attempt-last commit protocol.
- `src/commonplace/cli/run.py:63–86,152–187`:
  reset arguments, judgment arguments, code-binding guard and dispatch.
- `src/commonplace/lib/agentic_analysis/publication.py:303–384`:
  `reset_publish_analysis`, protected publication checks and replacements.
- `src/commonplace/artifactrun/inspection.py:18–72`:
  terminal-job completion and the distinction between coverage and publication.
- `src/commonplace/artifactrun/worktree.py:169–202,316–331`:
  checkout binding and preparation identity.

No native inspection command was needed. Read-only Python loaded `Run` and
`RunStore` without taking their lock, called `affected_jobs`/`coverage`, and
computed surviving installing judgments by excluding affected attempts. It
never called reset preparation, handlers, materialization, sequence allocation,
or store writes. `PYTHONDONTWRITEBYTECODE=1` suppressed import cache writes.
The successful evaluation used the existing origin Python with `PYTHONPATH=src`;
initial stdlib-Python import probes lacked the package/dependencies and stopped
before evaluation. No dependency installation followed.

For **each of the nine**, recomputation found:

- run-definition, preparation and case-evidence hashes equal the batch bindings;
- the five runtime files listed in the next section equal their own recorded
  method commit, checked with `git show`, not assumed from a common version;
- active attempt filename/hash map equals the batch binding;
- own publication file map equals both the bound map and journal `new` map;
- no open attempt, no pending-reset marker, and logical coverage present;
- no active operator judgment in the current judgment records.

These observations are metadata checks, not writer-idleness clearance,
publication reset-hook execution, source verification or semantic audits.
No claim is made that every hook guard was exercised or every external effect
was freshly recognized.

## Frozen interfaces: all nine checked separately

`W`, `R` and the command directory mean each row's literal `worktree`, `run`
and `command-prefix` in the batch record, not paths reconstructed from a slug.
All rows use the same engine and store bytes as current origin. Their native
judge implementation is therefore the current one described above.

| Case | Frozen method commit | Runtime family | Proposed barrier | Author roles that survive that reset |
| --- | --- | --- | --- | --- |
| Supermemory | `a568c6dc489ad546374536b642c3889ce23149a8` | old | report | `runtime` |
| ContextPilot | `4266dabc470929df0ff753e57fee0c55d7b87fc6` | old | report | `boundary`, `runtime` |
| OpenRSI | `f7732e9c6bc5622031571d2d429bc017253eb64f` | old | report | `runtime` |
| ModularRSI | `8414ddbd35da24645c020789bd824cb9749fa677` | old | report | `runtime` |
| JAZ | `a568c6dc489ad546374536b642c3889ce23149a8` | old | profile | `memory-profile` |
| Autogenesis | `a320038ed1a423b051eedbcec593172f8c2032f4` | old | report | `boundary`, `runtime` |
| MehmetGoekce LLM Wiki | `fb6ad58fd2fdc0e595e1e6671079b98e2e29730f` | new | profile | `memory-profile` |
| ClawVault | `fb6ad58fd2fdc0e595e1e6671079b98e2e29730f` | new | report | `boundary`, `runtime` |
| AREX-Skill | `a320038ed1a423b051eedbcec593172f8c2032f4` | old | report | **not `synthesis`** |

“Report” means `report-verification`; “profile” means
`profile-verification`. These are job names, not author reset selections.

Byte-family evidence (SHA-256 prefixes below identify the full files; executable
glue must retain full digests, not use prefixes as verification):

| File under `W/src/commonplace/` | Old family | New family / current origin |
| --- | --- | --- |
| `cli/run.py` | `87595959caae676e` | `c932f1e85f485f1c` |
| `artifactrun/run.py` | `45ec62ef68e55991` | `74777a8d1a658f8b` |
| `artifactrun/engine.py` | `eec3d74427e9c6e4` | same |
| `artifactrun/store.py` | `440e90fa26a7fcbe` | same |
| `lib/agentic_analysis/publication.py` | `f0d1e068b2fabbea` | `3ddc551eb1c4b86c` |

Old-family CLIs have no reset subcommand; their `Run` has neither pending-reset
fencing nor budget-floor consumption, and their publication module has no reset
hook. New-family files above equal current origin. Both families support judge
with `--role`, `--outcome`, `--findings`, optional `--version`, `--scope`,
`--override` and `--basis`; neither supports a findings-file argument.

For old methods the pilot-compatible operation is an **explicit external origin
API reset**, not the origin CLI aimed at a foreign worktree. The CLI's
`require_run_code` rejects that mixed-checkout call. Importing current origin
`reset_run` externally also ensures that dynamic publication-hook imports come
from current origin, where the withdrawal hook exists. Pin the origin package
and handler resolution as well as the frozen run declaration. Do not import a
mixture of current reset and frozen publication modules. Subsequent native
judge and coordinator operations remain in the case's unchanged frozen command
environment. Never advance the old engine during a pending reset: it lacks the
new fence. The parent must enforce that interlock externally.

## Exact dependency result and witness preservation

For all seven report-barrier cases, current `affected_jobs` returned exactly:

```text
report-verification
apply-report-verification
memory-profile
check-memory-profile
profile-verification
apply-profile-verification
synthesis
check-synthesis
synthesis-verification
apply-synthesis-verification
assemble
publish
```

For JAZ and Mehmet it returned exactly:

```text
profile-verification
apply-profile-verification
synthesis
check-synthesis
synthesis-verification
apply-synthesis-verification
assemble
publish
```

This is a forward-dependency closure, not every chronologically later attempt.
Refusal edges and optional candidate-check partners are deliberately not reset
edges. Report reset keeps opening, acquisition, boundary, aspect authors,
reconciliation and their upstream checks. Profile reset additionally keeps
memory-profile and its candidate check plus report verification/application.
Both closures retire assembly and publication. The eight named author members
survive and equal their authors' latest primary outputs; their exact versions
are already in the batch publication maps. A reset at an author itself would
remove that output and installing checks, defeating the proposed feedback path.

AREX's intended synthesis member
`a6f7c590677b7024740c4c877209ed12b6cc09f8077d518918119462510b2080`
does **not** survive report reset. Calling judge with no explicit version fails
with “role synthesis has no member to judge”. `--version` can record historical
evidence because immutable versions survive; it cannot make the deleted
synthesis attempt the latest output or recreate an installing acceptance.
`refusal_in_force` requires the refused version to equal the producer's latest
output. An evidence-only judgment is not a supported correction handoff here.

Resetting AREX only at synthesis verification would preserve that witness, as
in the AI Memex pilot, but would leave the earlier report-verification concern
unreopened. It is **not** the requested earliest-verifier route. Refusing first
and then resetting report verification also fails: the operator judgment about
synthesis is withdrawn along with that reset subject. No replacement sequence
for all nine is established by this review. The
[AREX audit](./audits/post-migration/AAS-2026-10-15-arex-skill-1871063034b5-01.md)
requires disposition of the witness, not a predetermined positive label or
permission to select another author.

## Conditional sequence for the eight surviving-author cases

This sequence is a specification for later authorized glue, **not an executable
commission**. Stop before step 1 for the nine-case batch because AREX is blocked.
Do not silently drop it and launch eight.

1. Obtain explicit case release and writer/owner reconciliation. Recheck all
   pins below and reject open attempts, pending reset, uncertain latest effects,
   changed publications or an integrated result. Prepare one immutable findings
   payload per affected role from that case's current bound audit. Include the
   exact finding, evidence locators, limits and desired disposition, not a
   prescribed verdict. Pin the payload bytes and role/version destination.
2. With no coordinator running, execute current-origin
   `commonplace.artifactrun.reset.reset_run(Path(R), BARRIER)` externally once,
   using the pinned origin runtime and current publication hook. Record its
   returned archive, jobs, attempts, effects and completed state. New-family
   native reset is available, but choosing the same external API for these
   cases makes the mechanism explicit. Do not call origin CLI on the foreign
   run. Do not reset the author or add another reset after recording feedback.
3. Before any advance, verify the returned closure against the expected set,
   the complete predecessor snapshot and publication-effect snapshots against
   preflight maps, unchanged upstream versions/run identity, cleared pending
   marker, and each target's still-installed latest primary output. If anything
   disagrees, stop without state repair or coordinator launch.
4. In each case's own `W` and command environment, invoke native judge once per
   listed role, with this argument vector shape:

   ```text
   commonplace-run judge R --role ROLE --outcome refused --findings TEXT
   ```

   `TEXT` is the exact UTF-8 content read from the pinned findings file by the
   parent wrapper, passed as one argument without shell evaluation. There is
   no native `--findings-file`. Do not use `--version`, `--override`, `--basis`
   or invented relation scopes for this plain author correction. Verify the
   subject version immediately before and after the call. Record returned
   operator judgment IDs and persisted findings equality.
5. For `boundary` plus `runtime` cases, record **both role refusals before any
   advance**, boundary first then runtime. This is two judgments, not two resets
   or a multi-role CLI option. A refusal of boundary does not remove its member;
   both current subjects remain addressable. Use a consolidated payload for
   each role: several refusals of the same latest output are not merged; only
   the latest is selected. Do not give one role only the other's finding.
6. Verify without mutation that each author has the expected refusal in force
   and resolves its declared optional `refusal` input to a document containing
   the exact payload and refused version. Confirm required inputs, permission,
   readiness, pending producers and frozen-method attempt headroom. Stop if any
   payload is missing, superseded, misaddressed or cannot be scheduled.
7. Only under separate launch authority resume the ordinary frozen-method
   coordinator. No special worker prompt injection is required: the ordinary
   refusal input carries feedback. Let native checks, dependent author jobs and
   independent verifiers run; do not manually restrict execution to the listed
   correction authors or skip dependency-driven reruns. Preserve new stops.
   Fresh exact-byte audit and integration remain separately commissioned.

Allowed initial role targets for these conditional routes are **only** those
in the table. Their payload topics are fixed by the batch contracts: generic
string capture qualification (Supermemory); selector/fallback qualification
(ContextPilot); possible shared-mount answer access, not observed leakage
(OpenRSI); post-review repair versus final bytes (ModularRSI); merged invocation
input-origin uncertainty (JAZ); missing import prerequisite, static only
(Autogenesis); human-approved access-log pruning/update authority (Mehmet);
narrow new-OpenClaw-deployment deprecation (ClawVault). Use each bound audit,
not historical original findings that the latest audit says were repaired.

## Multi-role, stale decisions and correction budgets

The proposed reset preserves unaffected upstream work **initially**, not a
promise that all of it remains current after an author changes bytes. Boundary
is a required, non-order-only input to runtime, memory, epistemic and workflow.
Changing boundary can make all four ready. Runtime is order-only for the three
specialists, but not for reconciliation. Reconciliation also tracks the aspect
members. Their checks and subsequent verification must refresh as dictated by
the actual pins. `check-boundary` has no required runtime dependency; both
boundary/runtime refusals need not be staged in separate coordinator phases.
A bounded correction is not a guarantee of a two-worker cost ceiling.

An operator refusal does not delete the member or erase earlier acceptances.
Coverage alone can therefore remain true in a published run after a refusal;
that is one reason to retire downstream publication first. The author becomes
ready from a changed refusal input. A later acceptance of the same role/version
can supersede the refusal (empty refusal scope is covered by any later accepted
scope); a new primary output makes the old refusal no longer match. An unchanged
refused primary requires a new auxiliary answer version, otherwise engine
closure fails. Repeated refusal must not be treated as an accumulating inbox.

Reset removes operator attempts whose subject role is in the reset roles,
whose role-addressed basis names such a role, or whose overrides intersect
judgments withdrawn with affected attempts. It retains unrelated operator
records; it is not a global operator-decision purge. A stale basis alone is
not a safety gate for author feedback: `refusal_in_force` does not call `holds`.
Do not attach cross-role bases hoping that changing boundary will automatically
retire runtime feedback. None of the nine currently has an active operator
record, but future glue must calculate withdrawals and retained decisions,
not assume this remains true.

Current reset writes a floor for **all** model jobs at the maximum old attempt
sequence, while preserving upstream records and the sequence counter. The new
family consumes this floor. The old family ignores it and counts every retained
attempt of that job. For old-family initial targets, raw retained counts/limits
are: Supermemory runtime 1/3; ContextPilot boundary 1/2 and runtime 2/3;
OpenRSI runtime 1/3; ModularRSI runtime 2/3; JAZ memory-profile 2/3;
Autogenesis boundary 1/2 and runtime 1/3. Thus each has at least one initial
correction attempt, but ContextPilot runtime, ModularRSI runtime and JAZ profile
have only one. ContextPilot epistemic and reconciliation, and ModularRSI memory,
epistemic and reconciliation, already retain 2/3 as well. Dependency reruns or
failed candidates can exhaust those budgets. Deleted downstream jobs start
without retained attempts; that does not renew untouched old-method authors.
New-family Mehmet and ClawVault consume the new floor normally. Do not promise
three fresh attempts to every author or reset again to evade an exhaustion stop.

## Publication protection, pins and required tests

Current external reset dynamically acquires handler effect locks before
preparing replacements. The publication hook accepts only the exact own,
unreleased worktree effect: opening metadata/preparation must agree, the journal
must establish run/source/destination and incumbent identity, current destination
must equal `new`, and the archived incumbent must equal `old`. It refuses an
already integrated result found in origin retained sets or its run archive.
It restores the opening incumbent (or removes a newly created destination),
withdraws the journal and archives both before/next effect trees. The full run
is snapshotted under `R.parent/.reset-history/R.name/<id>/before`, with prepared
next state and `reset.json`; effect snapshots are under `effects/<index>/`.
Existing publications survive there as evidence, not necessarily in their active
retained destination. Do not manually delete/recreate the journal or move a
publication to make a guard pass. Pending-reset recovery is native same-job
roll-forward only and requires later authorization, not improvisation here.

Before implementation, pin and retain:

- all nine exact case IDs, paths, method/source identities and revisions,
  preparation bytes, run JSON/declaration/type and plan identities;
- full digests of origin reset/run/engine/store/CLI/publication modules and
  their import locations, plus each frozen counterpart and command binding;
- complete attempts/judgments/version maps, budget files and sequence counter,
  member/latest-output maps, expected closures and operator withdrawal sets;
- opening metadata, current publication and manifest maps, effect journal,
  incumbent/archive maps, destination identity and protected origin baseline;
- latest audit files and immutable role-specific findings files, their full
  SHA-256 values, intended subject versions and resulting judgment IDs;
- explicit ownership/idleness evidence and authority for each later operation.

Required tests belong to a **later separately authorized disposable fixture
commission**, not the held runs and not this write-only-report scope. At minimum:
external origin reset with old frozen judge/advance; origin import/hook identity;
file-to-`--findings` transport preserving multiline text/quotes; reset removes an
author versus preserves it at its verifier; both multi-role payloads survive
boundary-first scheduling; latest-only refusal and stale operator basis/override
withdrawals; old/new budget behavior and dependency exhaustion; publish remains
retired until fresh terminal completion; exact predecessor archival, altered
publication refusal, integrated-result refusal and interrupted-reset fencing.
The AREX missing-witness test must fail closed, not be made to pass by editing
its contract. No such mutation tests were run here.

Existing relevant tests were read, not executed:
`tests/commonplace/artifactrun/test_reset.py` covers upstream preservation,
interruption and renewed budgets;
`tests/commonplace/agentic_analysis/test_reset_publication.py` covers withdrawal,
changed-byte refusal, integrated-result refusal and interrupted effects. They do
not by themselves establish the nine frozen-method feedback routes.

Read-only coverage verification can instantiate `Run(RunStore(R))`, check
`requirements`, `members`, `holds`, `coverage`, readiness, refusal inputs and
frozen-method attempt counts, and independently hash publication/effect maps.
Avoid `inspect`/`current_outputs` wrappers when strictly no filesystem changes
are allowed: their locks may create `state/lock`. Terminal success additionally
requires no open/failed/exhausted work and a **current `publish` completion**
with unchanged input pins, plus recognized exact publication bytes. Mere
`publishable: true`, an old publish receipt or an output directory is inadequate.
Metadata consistency cannot establish semantic repair; a new independent audit
must bind the resulting exact publication map. Integration is not part of any
route authorized here.

## Validation

The report is frontmatter-free workshop text under `kb/work/COLLECTION.md`.
Only this path may be validated or changed by this commission. The outcome of
its narrow deterministic validation is recorded in the completion response;
no execution test or semantic clearance is implied. Graph connection work,
if wanted, belongs to a separately scoped `cp-skill-connect` request.
