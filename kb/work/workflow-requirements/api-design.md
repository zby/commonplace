# Workflow API design sketch

The [Python sketch](./api_sketch.py) expresses the updated
[requirements](./requirements.md) through a small public boundary. Behavior
is `...`; it is not a working engine or a complete analysis job declaration.
The requirements govern its scheduling and judgment semantics. Names follow
the [glossary](./glossary.md). Operator entry points are omitted from this
sketch by request; that omission does not remove the command-line capability
from the requirements.

## Public boundary

- `JobSet`, `ModelJob`, `CodeJob` and `Input` describe the declaration-file schema.
- `start_run(run_dir, job_set, parameters=...)` starts a run: it writes the
  run metadata naming the job set and parameters, which fixes the
  declaration for the run.
- `advance(run_dir, results=...)` runs one invocation and returns a
  `RunStatus`. It loads the job-set file named by the run metadata.
- `CodeAttempt.read()` reads a pinned input by name.
- `CodeAttempt.judge()` stages acceptance or refusal of one subject version,
  with findings, a scope of covered relations and optional explicit refusal
  overrides.
- `AttemptResult` closes an open model attempt as completed or failed, with
  worker identity.
- `Handout`, `Stop` and `RunStatus` report work and state to the coordinator.
  `RunStatus.handouts` lists the attempts that invocation opened;
  `open_attempts` lists every attempt still open, whenever it was opened.
- `start_run()` on a run directory that already holds a run raises
  `FileExistsError`.

There is no public engine object, storage API, pin constructor, verdict parser
or specialized structural-check method. Handlers return named output bytes;
judgments and outputs commit together only after a handler succeeds.
Operator request records and command-line judgment entry points are not part
of this sketch. Code jobs retain explicit scoped overrides through `judge()`.

## Declaration and type separation

The job set is a declaration file, not executable code, under the workflow's
instructions. It names the type, and the run metadata names the job set.
Code jobs name package handlers by dotted path; a handler receives a
`CodeAttempt` and returns named output bytes. The Python dataclasses show the
loaded schema, not a Python configuration format. The serialization format
is not selected here. File inputs name absolute paths; a base for relative
paths is not specified.

Instruction trees install as shared data, while handlers live in the
package. The type supplies roles, relations and disposition requirements but
knows nothing of producers. A relation runs from an origin role to a partner
role and is named by both ends and its kind, such as
`verification:cites:runtime`. Loading and validating the declaration are
internal to `advance()`. The first job, such as `open`, is an ordinary code
job whose input is the run metadata that `start_run()` wrote.

Each role-filling job names its role; its first output is the primary
output, with any remaining outputs auxiliary. A check job can judge a
candidate among its inputs, while assembly can judge its own returned
primary output. Both use the same `judge()` operation. The implementation
must reject ambiguous output ownership and a job with its own role as input.

Each input has an address: a file, a member, a job's latest completed output, a
latest completed attempt record, a version that record says was handed, a
judgment addressed by role, relation and outcome, or a producer's current
refusal. Required and optional inputs record presence or absence. A required
judgment input is present only while the judgment holds. Workers can read
untracked context, but it is not authoritative, tracked or a currency
signal.

A handed input names an attempt input and the producer's input name. For
example, an apply job can declare:

```python
inputs={
    "verdict": Input("output", "verify-records:verdict"),
    "verification-attempt": Input("attempt", "verify-records"),
    "runtime-seen": Input("handed", "verification-attempt:runtime"),
}
```

`attempt.read("runtime-seen")` returns the bytes the verifier saw, and
`attempt.judge("runtime-seen", ...)` takes that exact member version as its
subject. The engine keeps the version's role internally. This adds no
public pin-construction or historical-storage method. The route is static;
only the attempt record selecting the version changes.

## Attempts and currency

Hand-outs pin every input and always supply the previous output by identity;
it is not an input. The attempt record retains those delivered previous-output
versions in `previous_outputs`. A code consumer declaring the producer's
attempt can compare a candidate with its delivered baseline without reading a
mutable member or adding a self-input. There is no opt-in previous-output flag. A completed
attempt records the versions pinned at opening, not those current when its
result is reported. An open model attempt is closed only by an attempt
result. A result with no output closes it as failed; a killed worker is not
silently cleaned up or reissued while its attempt remains open.

All output identity and downstream currency are content-based. There is no
special verdict currency rule. Max attempts are optional and never reset;
identical and failed attempts count. Code jobs have no max attempts. Failures
retain diagnostics, record no inputs, stop the invocation, and leave the job
ready for a later invocation. Exhausted max attempts prevent a further attempt
in this run; neither an acceptance nor an invocation resets them. Raising
max attempts edits the fixed declaration, which is a method change and makes the
run unpublishable. Further model work requires a new run; operator override
acceptance remains a spec capability outside this sketch.

An attempt answering a refusal may keep its primary output unchanged if it
produces a changed auxiliary output, compared with its previous completed
attempt. A newly present auxiliary version counts; an omitted output does
not. With neither a changed primary nor a produced changed auxiliary version,
the attempt fails. This permits an analyst to decline blockers with new
answers while preserving the report. Consumer checks validate those answers;
completion does not accept the report or supersede a refusal. A verifier
must declare the answers as an input to reassess them despite an unchanged
report. Checks that need to rerun for the new attempt declare its attempt
record, as the analysis checks already do.

An input that appears or differs from its recorded version is a readiness
signal; one that lapses is not. A job waits while a producer of any of its
inputs is ready or has an open attempt: the job filling the input's role
and every job that judges it, the job writing an output or attempt record,
and the job recording a judgment. Code jobs run to a fixed point first, so
only pending model jobs hold others back. Missing required inputs still block
readiness. A producer's refusal input lapses after a newer output without
scheduling another correction.

The engine supplies each producer's latest refusal of its latest completed
output, including the refused version, the findings and the refusal's
identity. Historical refusals stay as evidence but do not enter that
producer's refusal input. Reading it answers it; only a newer, unsuperseded
refusal triggers another correction. Supersession requires a sufficient
scope or an explicit override. There is no designated-verifier ownership
map or aggregation of outstanding findings beyond the requirement's
latest-refusal address.

## Judgments and publication

Only code jobs judge autonomously. A model-written verification is a document;
consumer code parses it and calls `judge()` for each applicable member.
The engine does not distinguish structural acceptance from semantic
acceptance. Every judgment records the judging attempt's pinned inputs as
its basis. The subject's role is at one end of every relation in its scope,
and the version at the other end must be in the basis.

An acceptance installs its subject only when that version is the producing
job's latest completed output. A judgment of any earlier version is evidence
only: it moves no member and cannot supply a refusal of the latest output.
The member stays when its acceptance stops holding.

Publication remains a code job. It checks that every relation the type
declares between the members is covered. A relation is covered by a
holding acceptance of the current member at either end that has the
relation in its scope and the current member at the other end in its
basis; a holding acceptance whose basis has a handed, historical version
at the other end is not sufficient. The job copies the current members,
pinned. The type's disposition determines required roles and gates the jobs
that fill them. State, attempts, versions, judgments and prompts remain
siblings of `set/`, never members.

External-effect recognition remains consumer-owned. Acquisition and
publication must establish whether an interrupted effect completed before
retrying; uncertainty leaves a failure record and stops. The public sketch
omits a reusable effect-adapter protocol, not this recovery obligation.

## Remaining design checks

The apply jobs must declare the verifier's attempt record and the member
versions it was handed, as the updated mapping requires. Scenario 21 then
judges A without restoring it over B or delivering A's refusal as B's
refusal input. In scenario 22, identical verdict bytes about B still rerun
the apply job because its attempt-record input changed. Ordinary transforms
retain content-only early cutoff.

The complete declaration should exercise these scenarios, interrupted code
recovery, repeated attempt results, scoped refusal supersession, disposition
changes and unioned publication coverage. These are future test
obligations, not passing test results.

## Delayed public features

Storage adapters, configurable declaration discovery, generic external-effect
protocols, automatic check-pair generation, decorator DSLs, public pin records,
arbitrary historical-version lookup and diff generation remain outside this
sketch. Handed inputs are included because the spec and first consumer
require them. Operator entry points remain outside this sketch by request,
although the spec still requires them. Scoped overrides remain available to
code jobs.
