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
   handed. Instructions a model job follows and contracts a
   check job applies are among its inputs. A job never has the role it
   writes as an input. The declaration is fixed; nothing adds a dependency
   at run time. Roles and their relations come from the set's type; a
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
   content, so an identical rerun changes nothing downstream. Each run of a
   job is an attempt, and it records the version of every input, absence
   included. A job is ready when its required inputs are present and
   either it has no completed attempt or some input has changed since its
   last completed one; 7 excepts one case. A job with an open attempt is
   not ready, nor is a job producing a member for a role that the type
   does not permit given the members present.
   An input changes when it appears or its current version differs from
   the recorded one; an input that has lapsed has not changed. Outputs
   and judgments are never removed, but an input can lapse: a refusal
   input when its job completes a newer output, and a required judgment
   input, which is present only while the judgment holds. A change
   outside a job's inputs is not a signal.
5. **Judgments.** The one engine primitive: a job records a judgment of a
   subject version, accepted or refused, with findings. The judgment
   records its basis, the job's pinned inputs, and its scope, the declared
   relations it covers, possibly none. The subject's role is at one end of
   each relation in the scope, and the version at the other end is in the
   basis. It may name a refusal it overrides. It holds while its basis is at its
   recorded versions. Any job may judge, as may the operator from the
   command line.
6. **Acceptance.** An acceptance of the producing job's latest completed
   output makes it the current member of its declared role, one per role,
   safe to repeat. A judgment of any earlier version is recorded as
   evidence and moves nothing. The member stays when the acceptance stops
   holding. A worker's output is a candidate until accepted.
7. **Refusal.** A job's refusals are one versioned, optional input of that
   job, whose current version is the latest refusal of its latest
   completed output, supplying the refused version by identity and the
   findings. An attempt that read a refusal has answered it; only a newer
   refusal makes the job ready again, and not one that a later acceptance
   of the same version supersedes. An acceptance supersedes a refusal only
   when its scope includes the refusal's scope or it names that refusal as
   overridden. The job set may bound how many attempts a job makes in the
   run, identical and failed attempts included, before the command stops;
   a bound never resets.
8. **Failure stays visible.** A job that cannot complete, whether the worker
   reported a problem, a code job failed, or an external effect's outcome
   cannot be established, leaves a record; the invocation stops and names
   it, and the job is ready on the next invocation. An attempt that
   answers a refusal with the refused version unchanged has failed. A
   failed attempt records no inputs, so the job stays ready; it counts
   toward the bound.
9. **Publication.** A set is publishable when every relation the type
   declares between its members is covered. A relation is covered by a
   holding acceptance of the current member at either end that has the
   relation in its scope and the current member at the other end in its
   basis. A code job checks this and copies the current versions out,
   pinned.

## Open

- **Acceptances that stopped holding.** Reported every invocation, or at
  publication.
- **Hand-out form.** How a prompt presents present and absent optional
  inputs.

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
  bounds, with each code job naming its handler by dotted path into the
  package. A run is started by an operation of its own, which writes the
  run's metadata naming the job set and the run parameters and fixes the
  declaration for the run; every later invocation loads the job set from
  that metadata. A job set's first code job, such as `open`, is then an
  ordinary job with the metadata as an input. The type knows nothing
  about producers. The instruction trees install as shared data, not as
  Python, which is why handlers live in the package and the file only
  names them. Why: a type says what a set is and a job set says how
  one is made; they change for different reasons, type specs are shared
  library artifacts, and one type may have several job sets, such as a
  production and a test configuration.
- **Only code jobs judge.** A model job that wants a judgment writes a
  document, and a code job reads it and records the judgment. Why: a
  judgment's basis and scope must be exact, and a worker's reading is
  not; the apply jobs in the analysis mapping show the pattern.
- **Bounds are for model jobs and never reset.** Every failure of a code
  job already stops the invocation with the operator in the loop; a count
  would only turn an environment problem into a dead run. A model job that
  exhausts its bound gets no further attempt in this run: the operator's
  recourse is an override acceptance of its latest output, or a new run.
  Raising the bound is a method change; the declaration is fixed for the
  run and the run would be unpublishable against a changed method. This is
  deliberate.
- **Completion is reported, never inferred.** The coordinator reports a
  model attempt completed; the command closes the attempt then and
  advances, which runs the check job. The validator never registers
  anything, so a worker may run it as often as it likes and keep editing
  after a pass. Why: a passing check is an answer to "would this pass?",
  not a statement that the work is done; only the worker's side knows that.
- **Completing is final for the attempt.** A change of mind after
  completing, for example to fix warnings the check printed, is a refusal
  of the submitted version by the coordinator, with a reason, and a new
  attempt that counts toward the bound. Why: any submission can be
  regretted, so no moment of registration avoids this; making regret an
  ordinary refusal keeps one path and one record for every rerun.
- **Attempt results ride on the advancing call.** Attempt results are
  arguments to the next invocation, which closes their attempts before
  computing readiness: one invocation per batch of results, not one per
  job. A result also carries the worker identity the retained manifest
  records. Why: the coordinator is about to call the command anyway, and
  the engine learns the worker's model and effort at no other moment.

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
