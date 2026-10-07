# Scenarios the requirements must cover

Each scenario names a situation, walks it under
[requirements](./requirements.md), and states the expected outcome. The
numbers in brackets are requirement numbers. Jobs are from
[the analysis mapping](./analysis-workflow-as-job-set.md); `R` is a model
job producing a member, `check-R` its code check, `V` a verifier whose
blockers an apply job turns into refusals.

**1. First attempt, accepted.** `R`'s required reads are present; its
refusal read is absent. Attempt 1 records both and writes candidate A.
`check-R` reads A, accepts it against the members it relates to. A is the
member. Nothing is ready. [4, 5, 6]

**2. Refuse, correct, accept.** `V` refuses A with a blocker. `R`'s refusal
read appeared, so `R` is ready. Attempt 2 reads the refusal, which supplies
A and the findings, and writes B and `answers.md`, recording the refusal's
version. While B awaits judgment the refusal read is unchanged, so `R` is
not ready. `check-R` accepts B. Installing B changes the slot, but the
refusal still names A by identity and `R` reads no slot of its own, so its
recorded reads are unchanged and `R` stays quiet. Downstream reads of the
member changed, so `reconcile` and `V` rerun. `V` has no blocker; the apply
job accepts the members against the new verification. [1, 4, 5, 6, 7]

**3. Refusal not repeated before the rerun.** `V` refuses A. Before `R` is
handed out, another member's correction reruns `V`, and the new
verification does not repeat the blocker. Two cases. If the new
verification has no blockers at all, the apply job accepts A against it;
that later acceptance of the same version supersedes the refusal, and `R`
is no longer ready: the verifier has withdrawn the finding by accepting A.
If blockers remain on other members, nothing accepts A, the refusal stands
unread, and `R` reruns. One attempt is spent on a finding not repeated;
accepted, since no judgment has withdrawn it. [4, 7]

**4. Second refusal of the correction.** `V` refuses B. `R`'s refusal read
has a new version, which is a change. Attempt 3 reads it. If the job set
bounds `R` at three attempts in the run, attempt 3 is the last; a further
refusal would call for a fourth, and the command stops naming `R` instead.
The structural acceptances of A and B along the way do not reset the
count. [4, 7]

**5. Waiting for a settled stage.** `profile` declares as required reads
the acceptances of the three reports against the record verification,
each addressed by member, relation and outcome. While `V` still raises
blockers, those acceptances do not exist, so `profile` is unready however
many verifications have been written. When the apply job accepts the
reports against a blocker-free verification, the reads appear and
`profile` is ready. If a report is later corrected, its acceptance stops
holding; the required read is absent again, and `profile` waits for the
new acceptance instead of running once per round. [1, 4, 6]

**6. Upstream member replaced, downstream only re-judged.** `memory` was
handed the runtime report as context, not as a declared read. Runtime is
corrected. `memory` is not ready, because none of its reads changed.
`check-memory` reads the runtime member, so it reruns, and either
re-accepts the memory report against the new runtime or refuses it with a
finding, which then makes `memory` ready. Model cost is paid only when a
check fails. The same holds for AGENTS.md, skills and anything else the
worker read beyond its declaration. [2, 4, 5, 6]

**7. Identical rerun.** A method file is edited; `reconcile` reruns and
produces byte-identical output. Identity is by content, so no downstream
read changed and `V` does not rerun. [4]

**8. Criteria change.** A type contract that `check-R` reads is edited.
`check-R` reruns and refuses the member under the new rule. `R` is ready
with those findings. The member stays in the slot until a new version is
accepted, and publication is blocked until then. [4, 5, 6, 9]

**9. Operator intervention.** The workflow is autonomous; an operator who
judges from the command line steps outside it and must know how it works.
Three things to know. A refusal with a reason and no relation is an
ordinary refusal: `R` is ready with the reason as findings. An acceptance
of a version only supersedes a refusal within its scope (scenario 17), so an
override of a check's refusal must name that refusal. And two effects the
autonomous flow never produces: a refusal of a member whose acceptances
all hold does not by itself block publication, since no acceptance's reads
changed, so the operator should also hold publication or wait for the
correction; and a judgment of a historical version is evidence only
under requirement 6, so putting an old version back is an explicit
restoration, recorded as a new acceptance of that version as the job's
output, not a side effect of judging it. [5, 6, 7, 9]

**10. Publication blocked by an acceptance that stopped holding.**
Synthesis B replaced A. The synthesis verification was accepted against A,
so that acceptance no longer holds. `verify-synthesis` reruns, because its
read changed; until its new verification is accepted against B and B
against it, the set lacks a holding acceptance covering the relation. In
the mapping that acceptance is a required read of `publish`, so `publish`
is not ready rather than refusing. [1, 4, 5, 9]

**11. Worker reports a problem.** `R`'s worker writes the problem file
instead of a candidate. The command stops naming `R` and the problem. The
failed attempt records no reads, so `R` is still ready: after the operator
has acted, the next invocation hands it out again, and if the problem
recurs the command stops again. No version is produced, but the attempt
counts toward the bound, so repeated failure ends in a stop at the bound
rather than an operator noticing the repetition. A code job that raises
behaves the same way. [4, 7, 8]

**12. Interrupted invocation.** The command is killed after running two
code jobs and halfway through a third. The next invocation finds the two
attempts' records and continues; the third left output without a record,
which is disregarded and removed, and the job is still ready. If the kill
fell between copying B into its slot and recording the acceptance, the
slot's bytes have no record behind them: the member is whatever the latest
acceptance names, holding or not, since requirement 6 keeps a member when
its acceptance stops holding, and the slot is re-materialized from it. No job
runs twice unless a read changed. A publication left half-written is an
external effect: the engine compares the retained manifest with the pinned
one and finds it complete, absent or partial; only partial stops the
command for the operator. A worker killed mid-write leaves an open
attempt and a candidate under it, which cleanup spares; the agent that ran
the worker reports the job finished with no output, which closes the
attempt as failed, counts it, and leaves the job ready, and the candidate,
now under no open attempt and no record, is removed. An orchestrator that
died with attempts open is closed the same way by the next session or the
operator. [3, 4, 6, 8]

**13. Parallel hand-outs.** Two analysts are refused in the same round. Both
are printed as ready. If the agent runs one and calls again, `reconcile` is
ready after the first acceptance and runs; it runs again after the second.
Running both before calling again avoids the extra attempt. The spec
permits either; the hand-out can say which the workflow prefers. In both
cases the second analyst has an open attempt, so it is neither printed as
ready again nor touched by cleanup. [3, 4]

**14. Non-complete disposition.** The boundary is accepted with a
disposition other than complete. The analysis jobs read the boundary, but
each produces a member the type does not require given the members
present, so none is ready. `assemble` is: its required acceptances cover
only the boundary and the overview. [1, 4, 9]

**15. Identical bytes after a refusal.** `V` refuses A. Attempt 2 reads
the refusal and the worker hands back bytes identical to A. By content
identity this is no new version, so no check reruns and no new judgment
appears; were the attempt treated as answered, `R` would be unready and
the run would stall with a refused member and nothing to do. Requirement 8
instead treats it as a failed attempt: the command stops naming `R`, no
reads are recorded, so `R` stays ready, and the attempt counts. A worker
that keeps returning A ends in a stop at the bound with the right
diagnosis: `R` answered its refusal without change. [4, 7, 8]

**16. Structural acceptance does not replenish the budget.** A passes
`check-R`, `V` refuses A, B passes `check-R`, `V` refuses B, and so on.
Each structural pass is an acceptance, but the bound counts attempts in
the run and never resets, so after the third attempt the command stops
naming `R`. The verifier's findings for A and B are on record for the
operator. [7]

**17. A re-check does not supersede a refusal outside its scope.** `V`
refuses A; the apply job records the refusal with the relation runtime to
record-verification as its scope. `check-R` reads that refusal, so it
reruns, finds unchanged A structurally sound, and accepts it on identity
and citations. That scope does not include the refusal's, and the
acceptance names no refusal it overrides, so the refusal stands and `R` is
ready. The duplicate acceptance is harmless: safe to repeat, and it moves
no count. [5, 7]

**18. Read versions are fixed at hand-out.** `reconcile` is handed out
while the reports are at version set 1; the hand-out pins those versions
and points the worker at them. A report is corrected before `reconcile`
finishes. Completion records set 1, so the attempt stands as work against
what the worker read, and `reconcile` is ready again at once because a
read changed. Nothing is recorded against inputs the worker never saw.
[3, 4]

**19. Cleanup spares an open attempt.** Two analysts are handed out. The
first finishes and the agent advances while the second is still writing.
The second has an open attempt, so its half-written candidate is not a
cleanup target and the job is not handed out again. Cleanup removes only
files with no open attempt and no record, such as a candidate from a
killed worker once its attempt has been reported closed. [3, 4]

**20. Rerun with its own previous version.** A report is corrected, so
`reconcile`'s read changed and it is handed out again. The hand-out
supplies its previous output by identity as context, not as a read, so the
worker can carry forward what still holds without the slot becoming a
dependency the next acceptance would move. `verify-records` gets its
previous verification the same way, which its instruction relies on.
[3, 4]

**21. A late verdict about a replaced version.** Two analysts are
refused. The first is corrected and the agent advances: `reconcile` reruns
and `V` is handed out pinned to the reports as they stand, including the
second analyst's A. The second analyst's correction, running in parallel,
finishes with B; the agent advances and `check-R` installs B. `V` then
finishes with a verdict about A. The apply job reads `V`'s attempt record
and the members at the versions it pinned, so its judgments are about A. An acceptance of A is
evidence only, because A is not `R`'s latest completed output; B stays the
member. A refusal of A is likewise not the refusal `R`'s read counts, so B
is not thrown away. B has no acceptance against the verification, so the
gates and publication wait; `V`'s reads changed, so `V` reruns and judges
B. [3, 4, 6, 7]

**22. Identical verdict text about different inputs.** `V` reruns on B
and writes the same "no blockers" bytes it wrote about A. By content
identity the verification is the same version, so a job reading only the
verification would see no change and B would never be accepted against
it. The apply job also reads `V`'s attempt record, which is a new one
with B among its pinned versions, so the apply job reruns, judges B, and
accepts it against the verification. `reconcile` producing identical
bytes in scenario 7 still changes nothing downstream, because `V` reads
the reconciliation, not `reconcile`'s attempt record: a transform's
identical output is early cutoff, a judgment about different inputs is
not. [1, 3, 4, 6]

## Not yet covered

Nothing from the analysis mapping.
