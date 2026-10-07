# Scenarios the requirements must cover

Each scenario names a situation, walks it under
[requirements](./requirements.md), and states the expected outcome. The
numbers in brackets are requirement numbers. Jobs are from
[the analysis mapping](./analysis-workflow-as-job-set.md); `R` is a model
job producing a member, `check-R` its code check, `V` a verifier whose
blockers an apply job turns into refusals.

**1. First attempt, accepted.** `R`'s required inputs are present; its
refusal input is absent. Attempt 1 records both and writes candidate A.
`check-R` reads A and accepts it with a scope of the relations its role
declares. A is the
member. Nothing is ready. [4, 5, 6]

**2. Refuse, correct, accept.** `V` refuses A with a blocker. `R`'s refusal
input appeared, so `R` is ready. Attempt 2 reads the refusal, which supplies
A and the findings, and writes B and `answers.md`, recording the refusal's
version. B is now `R`'s latest completed output and has no refusal, so the
refusal input has lapsed; an input that has lapsed has not changed, so
`R` is not ready. `check-R` accepts B. Installing B changes the member,
but `R` has no input on its own role, so `R` stays quiet. Downstream
inputs on the member changed, so `reconcile` and `V` rerun. `V` has no blocker; the apply
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

**4. Second refusal of the correction.** `V` refuses B. `R`'s refusal input
has a new version, which is a change. Attempt 3 reads it. If the job set
bounds `R` at three attempts in the run, attempt 3 is the last; a further
refusal would call for a fourth, and the command stops naming `R` instead.
The structural acceptances of A and B along the way do not reset the
count. [4, 7]

**5. Waiting for a settled stage.** `profile` declares as required inputs
the acceptances of the three reports against the record verification,
each addressed by role, relation and outcome. While `V` still raises
blockers, those acceptances do not exist, so `profile` is unready however
many verifications have been written. When the apply job accepts the
reports against a blocker-free verification, the inputs appear and
`profile` is ready. If a report is later corrected, its acceptance stops
holding; the required input has lapsed, and `profile` waits for the
new acceptance instead of running once per verification. [1, 4, 6]

**6. Upstream member replaced, downstream only re-judged.** `memory` was
handed the runtime report as untracked context, not as an input. Runtime
is corrected. `memory` is not ready, because none of its inputs changed.
`check-memory` has the runtime member as an input, so it reruns, and
either re-accepts the memory report with `memory:cites:runtime` in scope or refuses it with a
finding, which then makes `memory` ready. Model cost is paid only when a
check fails. The same holds for AGENTS.md, skills and anything else the
worker read beyond its declaration. [2, 4, 5, 6]

**7. Identical rerun.** A method file is edited; `reconcile` reruns and
produces byte-identical output. Identity is by content, so no downstream
input changed and `V` does not rerun. [4]

**8. Criteria change.** A type contract among `check-R`'s inputs is edited.
`check-R` reruns and refuses the member under the new rule. `R` is ready
with those findings. The member stays in its role until a new version is
accepted, and publication is blocked until then. [4, 5, 6, 9]

**9. Operator intervention.** The workflow is autonomous; an operator who
judges from the command line steps outside it and must know how it works.
Three things to know. A refusal with a reason and no relation is an
ordinary refusal: `R` is ready with the reason as findings. An acceptance
of a version only supersedes a refusal within its scope (scenario 17), so an
override of a check's refusal must name that refusal. And two effects the
autonomous flow never produces: a refusal of a member whose acceptances
all hold does not by itself block publication, since no acceptance's basis
changed, so the operator should also hold publication or wait for the
correction; and a judgment of a historical version is evidence only
under requirement 6. Putting an old version back is not supported: the
operator refuses the current version with a reason, and the rerun decides
what to carry forward. [5, 6, 7, 9]

**10. Publication blocked by an acceptance that stopped holding.**
Synthesis B replaced A. The synthesis verification was accepted against A,
so that acceptance no longer holds. `verify-synthesis` reruns, because its
input changed; until its new verification is accepted against B and B
against it, the set lacks a holding acceptance covering the relation. In
the mapping that acceptance is a required input of `publish`, so `publish`
is not ready rather than refusing. [1, 4, 5, 9]

**11. Worker reports a problem.** `R`'s worker writes the problem file
instead of a candidate. The command stops naming `R` and the problem. The
failed attempt records no inputs, so `R` is still ready: after the operator
has acted, the next invocation hands it out again, and if the problem
recurs the command stops again. No version is produced, but the attempt
counts toward the bound, so repeated failure ends in a stop at the bound
rather than an operator noticing the repetition. A code job that raises
behaves the same way. [4, 7, 8]

**12. Interrupted invocation.** The command is killed after running two
code jobs and halfway through a third. The next invocation finds the two
attempts' records and continues; the third left output without a record,
which is disregarded and removed, and the job is still ready. If the kill
fell between copying B into its role's file and recording the acceptance,
the file's bytes have no record behind them: the member is whatever the latest
acceptance names, holding or not, since requirement 6 keeps a member when
its acceptance stops holding, and the file is re-materialized from it. No
job runs twice unless an input changed. A publication left half-written is an
external effect: the engine compares the retained manifest with the pinned
one and finds it complete, absent or partial; only partial stops the
command for the operator. A worker killed mid-write leaves an open
attempt and a candidate under it, which cleanup spares; the coordinator
that ran the worker reports an attempt result with no output, which closes
the attempt as failed, counts it, and leaves the job ready, and the candidate,
now under no open attempt and no record, is removed. A coordinator that
died with attempts open is closed the same way by the next session or the
operator. [3, 4, 6, 8]

**13. Parallel hand-outs.** Two analysts are refused by the same verification.
Both are printed as ready. If the coordinator runs one and calls again, `reconcile` is
ready after the first acceptance and runs; it runs again after the second.
Running both before calling again avoids the extra attempt. The spec
permits either; the hand-out can say which the workflow prefers. In both
cases the second analyst has an open attempt, so it is neither printed as
ready again nor touched by cleanup. [3, 4]

**14. Non-complete disposition.** The type discriminates on the boundary's
disposition, which exists before any analysis job runs. Before the
boundary is accepted every role is permitted and nothing but the boundary
is ready. The boundary is accepted with a disposition other than complete;
now the type permits only the boundary and the overview, so each analysis
job produces a member for a role the type does not permit and none is
ready. `assemble` is: its required acceptances cover only the boundary and
the overview. Had the type discriminated on the overview, which `assemble`
writes last, the gate could never close. [1, 4, 9]

**15. Identical bytes after a refusal.** `V` refuses A. Attempt 2 reads
the refusal and the worker hands back bytes identical to A. By content
identity this is no new version, so no check reruns and no new judgment
appears; were the attempt treated as answered, `R` would be unready and
the run would stall with a refused member and nothing to do. Requirement 8
instead treats it as a failed attempt: the command stops naming `R`, no
inputs are recorded, so `R` stays ready, and the attempt counts. A worker
that keeps returning A ends in a stop at the bound with the right
diagnosis: `R` answered its refusal without change. [4, 7, 8]

**16. Structural acceptance does not replenish the budget.** A passes
`check-R`, `V` refuses A, B passes `check-R`, `V` refuses B, and so on.
Each structural pass is an acceptance, but the bound counts attempts in
the run and never resets, so after the third attempt the command stops
naming `R`. The verifier's findings for A and B are on record for the
operator. [7]

**17. A re-check does not supersede a refusal outside its scope.** `V`
refuses A; the apply job records the refusal of the runtime report with
`record-verification:cites:runtime` as its scope. `check-R` has that refusal as an input, so it
reruns, finds unchanged A structurally sound, and accepts it on identity
and citations. That scope does not include the refusal's, and the
acceptance names no refusal it overrides, so the refusal stands and `R` is
ready. The duplicate acceptance is harmless: safe to repeat, and it moves
no count. [5, 7]

**18. Input versions are fixed at hand-out.** `reconcile` is handed out
while the reports are at version set 1; the hand-out pins those versions
and points the worker at them. A report is corrected before `reconcile`
completes. The completed attempt records set 1, so the attempt stands as work against
what the worker read, and `reconcile` is ready again at once because an
input changed. Nothing is recorded against inputs the worker never saw.
[3, 4]

**19. Cleanup spares an open attempt.** Two analysts are handed out. The
first completes and the coordinator advances while the second is still
writing.
The second has an open attempt, so its half-written candidate is not a
cleanup target and the job is not handed out again. Cleanup removes only
files with no open attempt and no record, such as a candidate from a
killed worker once its attempt has been reported closed. [3, 4]

**20. Rerun with its own previous version.** A report is corrected, so
`reconcile`'s input changed and it is handed out again. The hand-out
supplies its previous output by identity, not as an input, so the worker
can carry forward what still holds without its role becoming a
dependency the next acceptance would move. `verify-records` gets its
previous verification the same way, which its instruction relies on.
[3, 4]

**21. A late verdict about a replaced version.** Two analysts are
refused. The first is corrected and the coordinator advances: `reconcile` reruns
and `V` is handed out pinned to the reports as they stand, including the
second analyst's A. The second analyst's correction, running in parallel,
completes with B; the coordinator advances and `check-R` installs B. `V`
then completes with a verdict about A. The apply job's inputs are `V`'s attempt record
and the members it was handed, so its judgments are about A. An
acceptance of A is evidence only, because A is not `R`'s latest completed output; B stays the
member. A refusal of A is likewise not the refusal `R`'s input counts, so B
is not thrown away. The verification's acceptance against A still holds,
since its handed input has not moved, but it covers nothing: the partner
version in its basis is not the partner's current member. B has no acceptance
against the verification, so the gates and publication wait; `V`'s inputs
changed, so `V` reruns and judges B. [3, 4, 6, 7, 9]

**22. Identical verdict text about different inputs.** `V` reruns on B
and writes the same "no blockers" bytes it wrote about A. By content
identity the verification is the same version, so a job with only the
verification as an input would see no change and B would never be accepted against
it. The apply job also has `V`'s attempt record as an input, which is a
new one with B among its handed versions, so the apply job reruns, judges B, and
accepts it against the verification. `reconcile` producing identical
bytes in scenario 7 still changes nothing downstream, because `V`'s input
is the reconciliation, not `reconcile`'s attempt record: a transform's
identical output is early cutoff, a judgment about different inputs is
not. [1, 3, 4, 6]

## Not yet covered

Nothing from the analysis mapping.
