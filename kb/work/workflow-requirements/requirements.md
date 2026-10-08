# Workflow engine requirements

## Purpose

One command that, given a run directory, works out what remains to be done
there, does the deterministic part itself, and lists the model-executed part
for a coordinator to run. The analysis workflow is the first consumer;
nothing here is specific to it. Words follow the [glossary](./glossary.md).

## Requirements

1. **Declaration.** A run directory declares its job set: each job's kind,
   its inputs, required or optional, and the outputs it writes.
   Dependencies are those inputs. Judgments (5) are files addressed by
   role, relation and outcome, with the latest one current, and may be
   declared as inputs; so may a job's attempt record (3), with the latest
   completed one current, which carries the versions that attempt was
   handed; and so may the set's coverage (9). Instructions a model job follows and contracts a
   check job applies are among its inputs; a file input may name its path
   relative to the library, resolved against the library the run was
   started with, so a job set is a file that names no machine's paths. An
   input may be order-only, in the sense of Make's order-only
   prerequisites: it orders the job after it and its version is recorded,
   but it is never a rerun trigger. A job never has the role it
   writes as an input. The declaration is fixed; nothing adds a dependency
   at run time. Roles and their relations come from the set's type, which
   the declaration names and which is fixed with it for the run; a
   relation runs from an origin role to a partner role and is named by
   both ends and its kind, such as `verification:cites:runtime`. The job
   set adds only who produces what from what.
2. **Two kinds of job.** A code job runs under the command and reads only
   its inputs. A model job is handed out as a prompt and an expected output
   path; the command never calls a model. Its inputs are authoritative and
   are its rerun triggers. Whatever else its worker reads is untracked
   context, and its output answers to judgments, not to that context.
3. **One call advances.** An invocation reads the run directory, runs every
   ready code job and prints the ready model jobs. The next invocation
   continues from the files it finds; none depends on an earlier process.
   A hand-out opens an attempt and pins the version of every input; the
   worker is pointed at those versions, which exist because every version
   is kept. A hand-out of a job with a previous attempt also supplies that
   attempt's output by identity as previous output, not as an input. A
   completed attempt records the pinned versions, not those current when
   it is reported. An attempt's outputs and judgments count only once its
   record is written, last and whole. For a model job the coordinator that
   ran the worker reports the attempt's result through the command, which
   writes the record then; an open attempt is closed only by such a
   result, whatever its outcome, and a result for a job with no output
   closes it as failed (8). Files with neither an open attempt nor a
   record are disregarded and removed on the next invocation; files under
   an open attempt are left alone. Members are derived from acceptance
   records, so a role's file is re-materialized from them.
4. **Versions, attempts and currency.** Every output keeps all its versions;
   one is current, and other jobs read only that one. Identity is by
   content, so an identical output changes nothing for consumers of that
   output. Other outputs and the attempt record can change independently.
   Each run of a job is an attempt, and it records the version of every input, absence
   included. A job is ready when its required inputs are present and
   either its latest attempt failed, it has no completed attempt, or some input
   has changed since its last completed one; 7 excepts one input-change case. A job with an open attempt is
   not ready, nor is a job producing a member for a role that the type
   does not permit given the members present.
   An input changes when it appears or its current version differs from
   the recorded one; an input that has lapsed has not changed. Outputs
   and judgments are never removed, but an input can lapse: a refusal
   input when its job completes a newer output, and a required judgment
   input, which is present only while the judgment holds and its subject
   is its role's current member. A change
   outside a job's inputs is not a signal, nor is a change of a
   order-only input. Whether a ready job is run or
   handed out at once is a scheduling decision, recorded under Decisions.
5. **Judgments.** The one engine primitive: a job records a judgment of a
   subject version, accepted or refused, with findings. The judgment
   records its basis, the job's pinned inputs, and its scope, the declared
   relations it covers, possibly none. The subject's role is at one end of
   each relation in the scope, and the version at the other end is in the
   basis. It may name a refusal it overrides. It holds, or is up to date,
   while its basis is at its recorded versions; otherwise it is stale. Any job may judge, as may the operator from the
   command line.
6. **Acceptance.** An acceptance of the producing job's latest completed
   output makes it the current member of its declared role, one per role,
   safe to repeat. A judgment of any earlier version is recorded as
   evidence and moves nothing. The member stays when the acceptance stops
   holding. A role the type does not permit given the members present has
   no member; its versions and judgments stay recorded. A worker's output is a candidate until accepted.
7. **Refusal.** A job's refusals are one versioned, optional input of that
   job, whether or not the job set declares it, whose current version is the latest refusal of its latest
   completed output, supplying the refused version by identity and the
   findings. An attempt that read a refusal has answered it; only a newer
   refusal makes the job ready again, and not one that a later acceptance
   of the same version supersedes. An acceptance supersedes a refusal only
   when its scope includes the refusal's scope or it names that refusal as
   overridden. The job set may set a job's max attempts: how many attempts it
   makes in the run, identical and failed attempts included, before the
   command stops; the count never resets.
8. **Failure stays visible.** A job that cannot complete, whether the worker
   reported a problem, a code job failed, or an external effect's outcome
   cannot be established, leaves a record; the invocation stops and names
   it, and the job is ready on the next invocation. An attempt that answers
   a refusal with the refused primary version unchanged and produces no
   changed auxiliary output has failed. Compare each produced auxiliary
   version with that job's previous completed attempt; a newly present
   output counts as changed, but omitting an output does not. A changed
   auxiliary output permits completion, not acceptance: consumer code checks
   whether the answer resolves the refusal, and a downstream verifier must
   declare that output as an input to reassess it. A failed attempt records
   no inputs, so the job stays ready; every attempt counts toward max attempts.
9. **Publication.** A set is publishable when every role its disposition
   requires is present, every member has a holding acceptance, and every
   relation the type declares between its members is covered. A relation
   is covered by a holding acceptance of the current member at either end
   that has the relation in its scope and the current member at the other
   end in its basis. The engine determines this and supplies it as a
   coverage input: a job may declare one, and it is present only while the
   three conditions hold for the set minus the declaring job's own role.
   Its version names the members and the covering claims, never judgment
   records. A code job declaring it copies the current versions out,
   pinned.

## Decisions

Settled choices beneath the requirements, of the kind an ADR would record.
They bind an implementation of this spec; they are not requirements.

- **State lives beside the set.** The command is given a run directory;
  the typed set is its `set/` subdirectory, and attempts, versions,
  judgments, hand-out prompts and failure records are its siblings, never
  members. Why: the set type has closed membership, so anything else
  inside it is a violation; kept outside, the set validates as it stands
  at every moment, publication is a plain copy, and no consumer needs an
  exclusion rule.
- **The job set is its own file, named by the run, naming the type.** It
  is a declaration file, not code, under the workflow's instructions
  beside the worker instructions it refers to: jobs, inputs, outputs and
  max attempts, with each code job naming its handler by dotted path into the
  package. A run is started by an operation of its own, which writes the
  run's metadata naming the job set and the run parameters and fixes the
  declaration and the set type it names for the run; every later invocation loads the job set from
  that metadata. A job set's first code job, such as `open`, is then an
  ordinary job with the metadata as an input. The type knows nothing
  about producers. The instruction trees install as shared data, not as
  Python, which is why handlers live in the package and the file only
  names them. Why: a type says what a set is and a job set says how
  one is made; they change for different reasons, type specs are shared
  library artifacts, and one type may have several job sets, such as a
  production and a test configuration.
- **The hand-out keeps the analysis workers' shape.** A prompt names the
  instruction, then lists `name = value` lines for the job, its declared
  parameters, every input (or `absent`), the outputs, the problem file,
  the workspace and any previous output, then reading batches over the
  inputs. File inputs are handed at their own path so relative links in
  instructions resolve; engine-held versions are copied into the
  hand-out. Parameters are plain strings with `{run}`, `{run-id}`, `{set}`,
  `{workspace}` and `{param:<name>}` substituted; no template language.
  Why: the analysis instructions already follow this shape, so they port
  unchanged.
- **Code jobs see the fixed type, not a file of it.** A code attempt
  exposes the run's layout and relations and the fixed type text, so a
  handler never declares the set type as a file input. Member types,
  schemas and contracts stay live file inputs, which scenario 8 edits.
  Why: a file input of the set type would follow a mid-run edit while the
  engine schedules, scopes and covers against the copy fixed at start.
- **File inputs are checked, not snapshotted.** A file input is handed at
  its own path and its digest is pinned at hand-out; completing the
  attempt fails if the file then differs. A change reverted before
  completion is not detected. Runs that need the stronger guarantee run in
  a worktree pinned to a commit, as analysis runs already do. Why: a
  snapshot would have to mirror every file an instruction links to, and
  the method tree is already frozen where it matters.
- **Relation names are checked at start.** Every relation a judgment
  input names must be declared by the type, with the input's role at one
  end, or the run does not start. Why: an undeclared relation leaves the
  input permanently absent, and the job gated on it would wait with no
  stop to say why.
- **Only code jobs judge.** A model job that wants a judgment writes a
  document, and a code job reads it and records the judgment. Why: a
  judgment's basis and scope must be exact, and a worker's reading is
  not; the apply jobs in the analysis mapping show the pattern.
- **A ready job waits for pending producers of its inputs.** A job is not
  run or handed out while a producer of one of its inputs is ready or has
  an open attempt, so it waits for the run to settle upstream instead of
  running once against inputs about to change. A member's producers are
  the job filling its role and every job that judges it; an output's or
  an attempt record's producer is its job; a judgment input's are the
  model jobs filling its subject's role and the roles at its relation's
  ends, the work behind the code job that records it. One narrow code-only
  exception applies a completed model attempt to immutable handed subjects
  before that producer's rerun, as scenario 21 requires. It needs a triggering
  completed-attempt input and a present handed member from another role; every
  dependency on the exempt producer must be that completed attempt, its outputs
  or its handed inputs. Live member/judgment dependencies and a check reading
  only its own answered refusal retain the wait. This changes scheduling, not
  readiness, subjects, installation or refusal supersession. A second narrow
  exception checks a newly completed upstream primary candidate before handing
  out a downstream model that requires that role as an order-only input. Only
  optional member dependencies on that downstream model may bypass the wait;
  an open downstream attempt, required member or live judgment gate still blocks
  it. The check must not have consumed that candidate in its last completion.
  It pins the existing peer bytes, and rechecks when those bytes change. This
  avoids handing out the old upstream member merely because its check waited
  for the downstream consumer. When every ready job waits for another ready
  job, the invocation stops naming the cycle. Code jobs run
  to a fixed point, in declaration order, before model readiness is
  computed, so a code producer is never pending when model jobs are handed
  out and a correction loop through an apply job cannot deadlock; the wait
  is therefore applied to model producers only. Between code jobs it is
  not applied: a code job declared before its code producer may run once
  against stale input and again after it, which wastes a run but records
  nothing wrong, so a job set should declare code jobs in dependency order. Why: without the wait a
  correction makes a transform and its verifier ready together, and the
  verifier runs once against stale state; the current engine avoids that
  through its round structure. This is a scheduling policy over ready
  jobs, not a change to what readiness means, which is why it is a
  decision and not part of requirement 4.
- **Max attempts are for model jobs and never reset.** Every failure of a code
  job already stops the invocation with the operator in the loop; a count
  would only turn an environment problem into a dead run. A model job that
  exhausts its max attempts gets no further attempt in this run: the operator's
  recourse is an override acceptance of its latest output, or a new run.
  Raising max attempts is a method change; the declaration is fixed for the
  run and the run would be unpublishable against a changed method. This is
  deliberate.
- **Completion is reported, never inferred.** The coordinator reports a
  model attempt completed; the command closes the attempt then and
  advances, which runs the check job. The validator never registers
  anything, so a worker may run it as often as it likes and keep editing
  after a pass. Why: a passing check is an answer to "would this pass?",
  not a statement that the work is done; only the worker's side knows that.
- **Completing is final for the attempt.** The first closure wins, including
  conflicting or duplicate results in the same batch or later calls. A change of mind after
  completing, for example to fix warnings the check printed, is a refusal
  of the submitted version by the coordinator, with a reason, and a new
  attempt that counts toward max attempts. Why: any submission can be
  regretted, so no moment of registration avoids this; making regret an
  ordinary refusal keeps one path and one record for every rerun.
- **Attempt results ride on the advancing call.** Attempt results are
  arguments to the next invocation, which closes their attempts before
  computing readiness: one invocation per batch of results, not one per
  job. A result also carries the worker identity the retained manifest
  records. Why: the coordinator is about to call the command anyway, and
  the engine learns the worker's model and effort at no other moment.
- **A refusal input has a published format.** Its bytes are a Markdown
  document whose YAML frontmatter holds `refusal` (the refusal's identity),
  `version` (the refused version) and `scope` (the relation names, possibly
  none); the body is the findings, verbatim. Consumer code reads the
  findings as the body and the rest as fields; nothing else about the
  rendering is part of the contract. Why: a check that answers a refusal
  needs its findings exactly, and stripping an unspecified header made every
  consumer depend on the engine's display text. The identity and version
  stay in the bytes so that two refusals with the same findings remain
  different versions, as requirement 7 needs.
- **An attempt-record input has a published format.** Its bytes are
  canonical JSON with the fields present among `id`, `job`, `kind`
  (`model`, `code` or `operator`), `outputs` (output name to version),
  and, for a model attempt, `previous_outputs` (the versions delivered as
  previous output), `model` and `effort`. Pins, sequence numbers and other
  record internals are not part of it; the versions an attempt was handed
  reach a consumer through handed inputs. Why: consumers need the
  delivered baseline, the produced versions and worker identity, and a
  whole internal record made every field a dependency. The attempt id
  keeps each completed attempt a distinct version, as scenario 22 needs.
- **The engine reports a run's condition; consumers do not reconstruct it.**
  Inspection reads a run under its lock and reports members, open and
  failed attempts, refusals in force, stale acceptances, jobs that have
  exhausted max attempts, holding acceptances whose basis has a handed
  version that is no longer current, and the run condition, decided in
  this order: *running* while an attempt is open; *stopped* while a job's
  latest attempt failed or a job has exhausted max attempts, since jobs
  waiting on it will not run; *publishable*; *running* while a job is
  ready; otherwise *stuck*. A job's
  completion is *current* while its latest completed attempt's pins still
  resolve to the same versions, no attempt of it is open and it is not
  ready; only a current completion's outputs are read back. Stale
  acceptances are reported whenever inspection runs; publication neither
  reports nor refuses them, since the coverage input already waits.
  Consumers hold the run lock through a public context, never the store.
  Why: an operator report and a Git integration both need these answers,
  and computing them outside the engine made each consumer re-read
  internal records.

## Deferred

- **Validator code identity.** A package change can alter a check's verdict
  with no input changing. It stays an environment check at open and
  publish, as today, not a currency rule.
- **Freshness after publication.** A published set is frozen; whether it is
  stale against later methods is the library's freshness question, not the
  engine's.

## Non-goals

Engine-level validation or repair policy; parallel writers; a resident
scheduler process; harness-specific launching; a general workflow language.
