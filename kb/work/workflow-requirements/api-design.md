# Workflow API design sketch

The [Python sketch](./api_sketch.py) expresses the updated
[requirements](./requirements.md) through a small public boundary. Behavior
is `...`; it is not a working engine or a complete analysis job declaration.
The requirements govern it. This revision removes the previous sketch's
alternative currency, refusal-ownership and acceptance policies.

## Public boundary

- `JobSet`, `ModelJob`, `CodeJob` and `Read` declare jobs and file dependencies.
- `advance(directory, completions=..., judgments=...)` is the coordinator call.
  It loads the job-set file named by the run's opening metadata.
- `CodeContext.read()` reads a pinned declared input.
- `CodeContext.judge()` stages acceptance or refusal of an exact version,
  with findings, covered relations and optional explicit refusal overrides.
- `Completion` reports finished or failed model attempts with worker identity.
- `OperatorJudgment` carries the same judgment primitive from the command line.
- `Handout`, `Stop` and `Advance` report work and state to the coordinator.

There is no public engine object, storage API, pin constructor, verdict parser
or specialized structural-check method. Code handlers return named output
bytes; judgments and outputs commit together only after a handler succeeds.
An operator supplies a retained subject identity and explicit basis reads,
not an instruction to silently approve whatever is current.

## Declaration and type separation

The job set is its own file under the workflow's instructions. It names the
type, and the run metadata names the job set. The type supplies slots,
relations and disposition requirements but knows nothing of producers.
Loading and validating the declaration are internal to `advance()`.

Each member-producing job identifies its member; its first output is the
primary member output, with any remaining outputs auxiliary. A code check
can judge a member-producing candidate it reads, while assembly can judge
its own returned primary output. Both use the same `judge()` operation.
The implementation must reject ambiguous output ownership and self-reads.

Reads include ordinary files, members, job outputs, judgments addressed by
member/relation/outcome, and a producer's latest refusal. Required and
optional reads record presence or absence. A required judgment read is
available only while the judgment holds. Workers can read additional context,
but it is not authoritative, tracked or a currency signal.

## Attempts and currency

Hand-outs pin declared reads and always supply any previous attempt outputs
by identity as context. There is no opt-in previous-output flag. Completion
records opening pins, not the inputs current when completion is reported.
An open model attempt is closed only by an explicit report. Reporting no
output closes it as failed; a killed worker is not silently cleaned up or
reissued while its attempt remains open.

All ordinary output identity and downstream currency are content-based.
There is no special verdict currency rule. Model bounds are optional and
never reset; identical and failed attempts count. Code jobs have no bounds.
Failures retain diagnostics, record no reads, stop the invocation, and leave
the job ready for a later invocation.

The engine supplies each producer's latest refusal, including the refused
version and findings. Reading it answers it; only a newer nonsuperseded
refusal triggers another correction. Supersession requires sufficient scope
or an explicit override. There is no designated-verifier ownership map or
aggregation of arbitrary outstanding findings beyond the requirement's
latest-refusal view.

## Judgments and publication

Only code jobs judge autonomously. A model-written verification is a document;
consumer code parses it and calls `judge()` for each applicable member.
The engine does not distinguish structural acceptance from semantic
acceptance. Every judgment records the judging job's pinned declared reads.
Covered relation partners must be among them.

An acceptance installs its subject version at the member slot, including a
historical version. The member stays when its acceptance stops holding.
This sketch does not add a no-restoration policy. Operator interventions
have the same effects and must be deliberate.

Publication remains a code job. It checks that holding acceptance scopes
cover every relation declared for each required current member and copies
pinned current versions. The type's disposition determines required members
and gates their producers. State, attempts, versions, judgments and prompts
remain siblings of the typed output directory, never members.

External-effect recognition remains consumer-owned. Acquisition and
publication must establish whether an interrupted effect completed before
retrying; uncertainty leaves a failure record and stops. The public sketch
omits a reusable effect-adapter protocol, not this recovery obligation.

## Remaining design checks

The sketch follows the spec rather than silently repairing it. In particular,
pinning a verifier's attempt inputs does not by itself make an apply job's
current member reads equal to the versions that verifier saw. The consumer
mapping still needs an explicit rule preventing a late verdict about A from
being applied as a judgment of B. A special evidence currency rule or
historical non-installing acceptance would change the spec and is not added
here.

The complete job declaration should also exercise interrupted code recovery,
completion replay, scoped refusal supersession, disposition changes and
unioned publication coverage. These are future test obligations, not passing
test results.

## Delayed public features

Storage adapters, configurable declaration discovery, generic external-effect
protocols, automatic check-pair generation, decorator DSLs, public pin records,
historical-read APIs and diff generation remain outside this sketch. Operator
judgments and scoped overrides are not deferred: the updated spec requires
them.
