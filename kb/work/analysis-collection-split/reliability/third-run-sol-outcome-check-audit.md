# Sol rerun outcome audit: accepted analysis, blocked publication

Commissioned by the operator on 2026-10-04 for a check two hours after the
rerun began. This audits the workflow and its visible traces, compared with
the [first](./first-run-outcome-check-audit.md) and
[second](./second-run-outcome-check-audit.md) Dynamic Cheatsheet runs. It does
not revise the worker outputs, the method, or the retained set.

The Sol run produced a complete candidate set. Its twelve jobs passed local
acceptance, the independent record, profile and synthesis reviews passed, and
full set validation passed. Publication then raised `ValueError: replacement
requires a new run ID`: the isolated worktree allocated
`AAS-2026-10-04-dynamic-cheatsheet-01`, which is already the published
incumbent's ID. The coordinator reported this block at 22:09:17 UTC. The
publication effect remains `started`; no retained-set replacement or archive
was written. The incumbent overview's SHA-256 still equals its opening
expected digest. The workflow remains blocked with repair permitted, and
`run-state.md` still says `running` because the run has not been marked
abandoned. The coordinator ended its session; the public set is unchanged.

## Evidence and limits

- Worktree: `.commonplace/worktrees/dynamic-cheatsheet-4d912688cb3b`, method
  commit `49725e9aab162a67ef352c880d03631c5ddad6ae`. The frozen source is
  the same clean Git checkout and commit as the earlier runs:
  `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`.
- All thirteen session contexts (coordinator and twelve workers) report
  `gpt-6.1-sol` at low effort. The [evidence file](./third-run-sol-outcome-check-evidence.json)
  records their trace paths, hashes, token use, calls, output truncations,
  local-check logs, accepted output hashes and decisive run-file hashes.
- The two method commits after the second run changed only this workshop's
  audit and navigation files. No workflow code or instruction changed between
  the Luna and Sol runs. The source revision also stayed fixed. Stochastic
  execution, worker decisions and effort setting still prevent attributing
  any difference to the model alone.
- Trace reasoning and inter-agent messages are not inspectable. This audit
  uses visible calls, results, delivered text, accepted files and run state.
  The ignored worktrees retain the underlying traces and state only while
  those directories exist. No target system execution was performed by this
  audit.

## Comparison

| Measure | First Luna run | Second Luna run | Sol run |
|---|---:|---:|---:|
| Workflow result | Published | Stopped at synthesis review | Blocked at publication |
| Accepted job outputs | 10 | 16 | 12 |
| Worker sessions | 10 | 16 | 12 |
| Substantive correction rounds | 0 | 3 | 1: memory checkpoint decomposition |
| Acceptance refusals | 0 | 0 | 0 |
| Analyst check calls | 16 | 27 | 18 |
| Check calls with refusals | 4 | 9 | 4 |
| Opening to coordinator result | about 21 min | about 47 min | about 39 min |
| Coordinator and worker tokens, mostly cached input | 7.6m | 18.3m | 14.8m |
| Quotations in accepted source members | 26 | 43 in unpublished candidate | 58 in unpublished candidate |

Every Sol job was accepted on its first handout. Four local-check calls
refused draft text: boundary had one source identity defect, runtime and the
first memory report each had one ambiguous quotation, and epistemic had two
ambiguous and one missing quotation. Later checks passed. No accepted output
hash differs from its recorded acceptance hash, and the worker traces show
no further tool call after their final check. This supports check use before
submission, not the truth of every accepted claim.

The first reconciliation returned one substantive finding. The original
memory report grouped checkpoint fields with different consumers: last-record
reference restoration, all-record solution restoration, historical step
inspection and offline answer extraction, evaluation operands, and separate
run parameters. The memory analyst declared those operative parts and their
containment in a second report; reconciliation then passed. Record verification
read the frozen implementation, prompts, notebook code and relevant result
sample independently, and checked all 58 quote blocks against source text.
This source-reading trace repairs the unsupported team-wide inspection claim
in the first run and the independent-verifier reading gap in the second.

## Candidate content against earlier defects

The unpublished overview uses the source-native `Dynamic Cheatsheet` name and
a canonical repository URL and revision in its Source register. It contains
no worktree path. Runtime and record-verification traces include complete
reads of the auxiliary `sonnet_eval.py` source, which the first published set
claimed to inspect without a supporting trace. These are candidate
improvements only; the published first-run set remains unchanged.

The second run's fatal synthesis sentence said no retrieval route checks
prior outputs for correctness before inclusion. The Sol synthesis separates
the curator's prompt-requested correctness assessment from an independently
enforced truth check and says the raw history is retained regardless of
correctness. Its synthesis verifier explicitly checked that distinction.
The profile also restores `learning` under `behavioral_authority` alongside
`trace_learning: "yes"`, resolving the second audit's cross-axis concern on
the candidate's own account. It gives checkpoint compatibility a separate
validation/enforcement role, excludes static templates and provider weights
from scoped memory, and marks axes partial where native retained state is
opaque. These are more discriminating classifications, not evidence of
causal benefit from the analysed system.

The local worktree's `commonplace-validate <run>/output --full` passes with
zero failures and warnings, including the six member schemas, manifest and
cross-member links. Validation and the three semantic reviews establish a
reviewable candidate; they do not establish that every model-dependent
classification is correct. There is no published Sol result to compare in
the public collection, and replacement/archive/link-following behavior was
not exercised.

## Hidden and residual failures

1. **The same-day run ID collision is confirmed, not merely latent.** The
   second audit predicted the exact publication rejection. The third run
   reached `_check_set` and failed there. Fresh worktree-local state permits
   reuse of an ID already present in its inherited retained set. The
   publication gate correctly refuses replacement under that ID, but the
   workflow spends the full analysis before detecting it. A new attempt
   needs allocation or preflight that checks retained and archived IDs; the
   current blocked run cannot be published under its present ID.
2. **Run state is not a live workflow status.** The coordinator's report and
   block file establish a publication failure. `run-state.md` says `running`
   because that status means neither completed nor abandoned. Workflow
   `stopped` is null because this block permits repair, and the `publish`
   effect is recorded as `started`. Read the workflow block and report for
   the current operating state. Marking the run `failed` would be an
   abandonment decision, not an automatic consequence of `report stop`.
3. **Two epistemic tool outputs were truncated.** One combined prompt/source
   read and one broad search exceeded the visible output limit. The worker
   continued with narrower reads, and the independent record verifier read
   the decisive source paths without truncation. The complete match set of
   the broad search is not demonstrated by the original output alone; no
   conclusion here relies on that negative search result.

The coordinator read the publication instruction before the final step, but
did not detect the ID collision until code attempted publication. The candidate
manifest is complete and its member hashes match the prepared files. The
source checkout is clean at the pinned revision. The public incumbent's
overview hash is unchanged at
`c1a930c035b6a236d1279aedf7cfc3aacecaef8e5aa04ef270a25ec8c3dc9202`.

## Assessment

Sol produced a more detailed, internally reviewed candidate than the first
published set and repaired the specific synthesis and profile problems that
stopped or weakened the second attempt. It used fewer sessions, checks and
tokens than the second Luna run, but more than the first; one same-source
comparison is insufficient to assign the differences to the model. The run
did not deliver a new retained set because the known ID-allocation defect
blocked publication. Address that preflight before spending another run on
the same day. Keep this worktree and its candidate until the ID and
publication path are resolved or the candidate is explicitly abandoned.
