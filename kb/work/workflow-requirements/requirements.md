# Workflow engine requirements

## Purpose

One command that, given a directory, works out what remains to be done there,
does the deterministic part itself, and lists the model-executed part for an
agent to run. The analysis workflow is the first consumer; nothing here is
specific to it.

## Requirements

1. **Declaration.** A directory declares its job set: each job's kind, the
   files it reads, required or optional, and the files it writes.
   Dependencies are those files. Judgments (5) are files addressed by
   member, relation and outcome, with the latest one current, and may be
   declared as reads. Instructions a model job follows and contracts a
   check job applies are among its reads. A job never reads the slot it
   writes. The declaration is fixed; nothing adds a dependency at run time.
   Members and their relations come from the directory's type; the job set
   adds only who produces what from what.
2. **Two kinds of job.** A code job runs under the command and reads only
   its declared files. A model job is handed out as a prompt and an
   expected output path; the command never calls a model. Its declared
   reads are its authoritative inputs and its rerun triggers. Whatever else
   its worker reads is untracked, and its output answers to judgments, not
   to that context.
3. **One call advances.** An invocation reads the directory, runs every
   ready code job and prints the ready model jobs. The next invocation
   continues from the files it finds; none depends on an earlier process.
   A hand-out opens an attempt and pins the version of every read; the
   worker is pointed at those versions, which exist because every version
   is kept. A hand-out of a job with a previous attempt also supplies that
   attempt's output by identity, as context, not as a read. Completion
   records the pinned versions, not those current when it is reported. An
   attempt's outputs and judgments count only once its record is written,
   last and whole. For a model job the agent that ran the worker reports
   completion through the command, which writes the record then; an open
   attempt is closed only by such a report, whatever its outcome, and a
   report for a job with no output closes it as failed (8). Files with
   neither an open attempt nor a record are disregarded and removed on the
   next invocation; files under an open attempt are left alone. Members are derived from acceptance records, so
   a slot is re-materialized from them.
4. **Versions, attempts and currency.** Every output keeps all its versions;
   one is current, and other jobs read only that one. Identity is by
   content, so an identical rerun changes nothing downstream. Each run of a
   job is an attempt, and it records the version of every declared read,
   absence included. A job is ready when its required reads are present
   and either it has no completed attempt or some read has changed since
   its last completed one; 7 excepts one case. A job with an open attempt
   is not ready, nor is a job producing a member that the type does not
   require given the members present.
   A read changes when it appears or its current version differs from the
   recorded one. Outputs and judgments are never removed, so a read once
   present stays present, with one exception: a required read of a
   judgment is present only while the judgment holds. A change outside a
   job's declared reads is not a signal.
5. **Judgments.** The one engine primitive: a job records a judgment of a
   version, accepted or refused, with findings. The judgment records the
   reads the job used and names the declared relations it covers, possibly
   none, which are among those reads. It may name a refusal it overrides.
   It holds while its reads are at their recorded versions. Any job may
   judge, as may the operator from the command line.
6. **Acceptance.** An acceptance of the producing job's latest completed
   output makes it the current member at its declared slot, one per slot,
   safe to repeat. A judgment of any earlier version is recorded as
   evidence and moves nothing. The member stays when the acceptance stops
   holding. A worker's output is a candidate until accepted.
7. **Refusal.** A job's refusals are one versioned, optional read of that
   job, whose current version is the latest refusal of its latest
   completed output, supplying the refused version by identity and the
   findings. An attempt that read a refusal
   has answered it; only a newer refusal makes the job ready again, and
   not one that a later acceptance of the same version supersedes. An
   acceptance supersedes a refusal only when its scope includes the
   refusal's scope or it names that refusal as overridden. The job set may
   bound how many attempts a job makes in the run, identical and failed
   attempts included, before the command stops; a bound never resets.
8. **Failure stays visible.** A job that cannot complete, whether the worker
   reported a problem, a code job failed, or an external effect's outcome
   cannot be established, leaves a record; the invocation stops and names
   it, and the job is ready on the next invocation. An attempt that
   answers a refusal with the refused version unchanged has failed. A
   failed attempt records no reads, so the job stays ready; it counts
   toward the bound.
9. **Publication.** A set is publishable when every member has holding
   acceptances whose scopes together cover every relation the type
   declares for it. A code job checks this and copies the current versions
   out, pinned.

## Open

- **Acceptances that stopped holding.** Reported every invocation, or at
  publication.
- **Hand-out form.** How a prompt presents present and absent optional
  reads.

## Decisions

Settled choices beneath the requirements, of the kind an ADR would record.
They bind an implementation of this spec; they are not requirements.

- **State lives beside the typed directory.** The command is given a run
  directory; the typed set is one subdirectory of it, and attempts,
  versions, judgments, hand-out prompts and failure records are its
  siblings, never members. Why: the set type has closed membership, so
  anything else inside it is a violation; kept outside, the set validates
  as it stands at every moment, publication is a plain copy, and no
  consumer needs an exclusion rule.
- **The job set is its own file, named by the run, naming the type.** It
  lives under the workflow's instructions beside the worker instructions
  it refers to; the run's metadata, written at opening, names the job set
  it runs, which fixes the declaration for the run. The type knows nothing
  about producers. Why: a type says what a set is and a job set says how
  one is made; they change for different reasons, type specs are shared
  library artifacts, and one type may have several job sets, such as a
  production and a test configuration.
- **Only code jobs judge.** A model job that wants a judgment writes a
  document, and a code job reads it and records the judgment. Why: a
  judgment's reads and scope must be exact, and a worker's reads are not;
  the apply jobs in the analysis mapping show the pattern.
- **Code jobs carry no bound.** Every failure of a code job already stops
  the invocation with the operator in the loop; a count would only turn an
  environment problem into a dead run. Bounds are for model jobs.
- **Completion is reported, never inferred.** The orchestrating agent
  reports a model job finished; the command closes the attempt then and
  advances, which runs the check job. The validator never registers
  anything, so a worker may run it as often as it likes and keep editing
  after a pass. Why: a passing check is an answer to "would this pass?",
  not a statement that the work is done; only the worker's side knows that.
- **Finishing is final for the attempt.** A change of mind after finishing,
  for example to fix warnings the check printed, is a refusal of the
  submitted version by the agent, with a reason, and a new attempt that
  counts toward the bound. Why: any submission can be regretted, so no
  moment of registration avoids this; making regret an ordinary refusal
  keeps one path and one record for every rerun.
- **Finish rides on the advancing call.** Finished jobs are arguments to
  the next invocation, which closes their attempts before computing
  readiness: one call per round, not one per job. The call also carries
  the worker identity the retained manifest records. Why: the agent is
  about to call the command anyway, and the engine learns the worker's
  model and effort at no other moment.

## Deferred

- **Validator code identity.** A package change can alter a check's verdict
  with no read changing. It stays an environment check at open and
  publish, as today, not a currency rule.
- **Freshness after publication.** A published set is frozen; whether it is
  stale against later methods is the library's freshness question, not the
  engine's.

## Non-goals

Engine-level validation or repair policy; parallel writers; a resident
scheduler process; harness-specific launching; a general workflow language.
