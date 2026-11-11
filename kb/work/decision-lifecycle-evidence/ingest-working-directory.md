# Ingest working directory: a provisional cache with an end condition

## The bounded question

After an ingest drafting run ends, what should remain beyond the tracked
ingest and the session trace?

This is the "ingest candidate" starting case of the
[admission map](./admission-to-the-main-record.md), decided on 2026-11-11 for
the arrangement that shipped that day. It covers retention only. Drafting a
candidate outside `kb/sources/` and publishing it against the incumbent's hash
is integration safety, and this case does not assess it.

## Chosen arrangement

The run's working directory, `kb/reports/state/ingest/<slug>/`, stays after the
run. It is local and ignored. Its record, `handoff.yaml`, lists every handoff
check with its failure lines and the run's outcome. A closed run keeps its
failed candidate. A published run's candidate is deleted, because it equals
the ingest. Only the last run of an ingest is kept.
`commonplace-ingest-handoff prune` deletes published runs.

In the map's terms this is a working cache of auxiliary information prepared
during work. Nothing is admitted to Git.

## Intended use

One decision: whether the ingest skill keeps its parent repair round, the
second drafting worker dispatched after a failed handoff check. The record
shows how often a candidate fails a check after the first worker returned, and
on which rules. The same counts show which drafting rules fail in practice.

The consumer is whoever revisits the ingest skill. No other use is claimed.

## Alternatives

- **Trace only.** Each check and its output is already in the session trace.
  Nothing extra is kept, and the earlier code deleted the directory on publish
  and close. The cost is one extraction when the question is asked: find the
  ingest sessions and parse their tool calls. Traces may have expired by then.
- **Kept record (chosen).** Saves that extraction on this machine. Costs a
  disposal command, a rule in the skill not to delete the directory, and the
  distinction between an open and a finished run in `prepare`.
- **Retain in Git.** Not considered further. A count of failed checks has no
  reader after the decision.

## Deciding reason and its limits

The extraction was awkward when it was done once for the analysis that led to
the refactoring: the first scan matched the wrong sessions. That is a judgment
about effort from one attempt, not a measurement.

Two arguments first given for the record do not hold and are not part of the
reason. The record does not cover other machines, because the state directory
is local too. And trace completeness is a fixed premise of this workshop, so
"the trace might miss it" does not count.

The record cannot tell a worker's own check from the parent's check. Both run
the same command. Order usually shows it: a failure after a clean check is the
parent's. That is an inference.

The first run under the new skill, on 2026-11-11, published on its first
check. It ran before the record existed and left no data.

## End condition

Revisit when about 20 ingest runs have records, or earlier if the skill is
revised for another reason. Then decide the repair round from the records.

After that decision the record has no consumer. Unless a new named use has
appeared, `publish` and `close` return to deleting the working directory, and
`prune` and the kept-run handling in `prepare` are removed.

If the records are lost or too few when the question is asked, fall back to
the trace. That loss is acceptable.
