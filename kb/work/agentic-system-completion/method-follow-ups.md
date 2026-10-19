# Disposition of the rerun campaign's method follow-ups

Use this triage when commissioning further work on the sixteen unresolved
targets. It replaces the old campaign's eight-item discussion list, not the
canonical analysis method. The operator commissioned triage on 2026-10-19;
no implementation, new verification stage, containment mechanism or additional
retry layer is selected here.

## Dispositions

| Original item | Current disposition | Owner / next decision |
| --- | --- | --- |
| 1. Provider failures | **Retain the measure-before-more-retries decision.** The old Pi retry increase was reported, not evaluated causally. The current headless launcher has its own bounded relaunch policy; the retired coordinator's retry account is not its execution contract. | The next run's commissioning operator and harness maintainer assess the selected profile's effective retry/wait budget before adding layers. Reopen only with post-mitigation evidence of a specific failure mode; no new retry work is queued here. |
| 2. Disk capacity | **Defer under the existing operator decision.** The one-time incident and move to external worktrees do not establish future capacity. No automatic evidence cleanup is authorized. | Revisit free space, inodes and measured storage growth when planning another substantial batch, including if the sixteen-target work is commissioned as one. The batch commissioner owns that decision before launch. |
| 3. Manual path transcription | **Coordinator case superseded; worker case remains an existing proposal.** Headless code now composes the prompt and launches workers, so no coordinator copies the printed prompt path into a wrapper. Workers can still reconstruct supplied paths incorrectly. | Use the existing [worktree-relative paths proposal](../../reference/proposals/worktree-relative-worker-paths.md) for any future worker-facing change. Do not implement the obsolete wrapper-printing suggestion or create a duplicate path project. Adoption remains uncommissioned. |
| 4. Local-negative profile example | **Addressed; old rule superseded.** The current profile type contains a worked example: a known local `"no"` plus an unresolved unit gives partial axis coverage, with no system-wide negative conclusion. The old list's claim that `partial` requires a positive finding is no longer the current contract. | Use the [profile type](../../agentic-system-analyses/types/agentic-system-memory-profile.md). No separate example or diagnostic work remains justified by this historical item. Existing failed-run holds are not cleared by the contract change. |
| 5. Conditions, fallback paths and policy strength | **General instruction improvement implemented.** Current runtime, report verification, synthesis and synthesis verification instructions require tracing alternate paths and retaining claim conditions and unresolved reachability. This is instruction delivery, not measured elimination of misses. | Analysis-method maintainers own future changes through the current [maintenance procedure](../../agentic-system-analyses/instructions/maintain-analysis-method.md). No extra semantic-audit stage is adopted. Historical defects remain outside fresh analyst packets; unresolved target holds remain separate. |
| 6. Enforced worker write scope | **Open boundary, no containment design selected.** Output collection and validation do not stop a worker writing elsewhere, and neither before/after checks nor shorter paths establish containment. | The commissioning operator and harness/execution-environment maintainer own any containment requirement. Before a future launch that relies on enforced write boundaries, specify and establish that guarantee or return the unmet requirement to the operator. Do not silently make the standalone workflow extraction own it. This workshop retains incident dispositions, not a containment implementation project. |
| 7. Attempt-indexed traces | **Partly addressed; complete trace retention remains undecided.** Headless attempts retain prompts and `launch.json` with stdout/stderr, timing, argv and session identity; answer/failure records retain attempt references. This is not guaranteed complete chronological tool-call capture or durable retention of harness-owned session files. | Use the existing [workflow recovery-history proposal](../../reference/proposals/workflow-recovery-history.md) for the residual evidence/retention decision. Its old-engine description is historical and must be re-evaluated against the current engine before adoption. Do not duplicate the proposal or add a trace-audit acceptance gate. |
| 8. Publication namespace | **Implemented.** GitHub publications use lowercase `owner--project`; run IDs remain immutable. The publication procedure also distinguishes frozen pre-migration worktrees from current naming. | Follow [publication and legacy-worktree handling](../../agentic-system-analyses/instructions/publish-analysis.md). No namespace migration project remains from this list. A particular old publication still needs its own supported transfer decision; do not patch its frozen method or receipt. |

## Inspection basis and limits

Inspected the committed checkout following evidence/closeout commit
`fa1bde38d`. This was source/document inspection, not a new run or test execution.
The original list is retrievable without keeping its old workshop live:

```bash
git show defc4efaeeae631cff2a6f3f2370603df504b3ff:kb/work/agentic-system-reruns/failure-prevention-follow-ups.md
```

Useful implementation anchors:

- `src/commonplace/headless/jobs.py`: `Run.ask` composes the prompt, assigns
  per-attempt paths, writes `prompt.md`, and retains answer/failure metadata.
- `src/commonplace/headless/harness.py`: `launch` saves `launch.json`;
  `BACKOFF` and the relaunch code own current bounded launch retries. Session
  identifiers can point to harness-managed storage outside the run.
- `tests/commonplace/comparison/test_systems_matrix.py`: current local-negative
  and unresolved-axis assertions; their older names/results in the original
  follow-up are not a fresh test result.
- Commit `0355617f1` clarified profile coverage; `83cb60e46` strengthened the
  general source/verification/synthesis questions; `300954cbc` separated
  publication names from run IDs. Current instructions, not historical job
  paths, are the consumption surface.

The active standalone headless extraction's [boundary](../headless-workflow-extraction/README.md)
explicitly leaves filesystem permissions and process isolation to the caller's
harness/environment. It is context for item 6, not a commissioned task for that
separately owned workshop. No files in that workshop were changed.

Items 1–2 and 6 retain operator decisions or decision triggers, not newly
approved engineering scope. Items 3 and 7 point to their existing proposal
owners rather than copying their design backlogs. Items 4, 5 and 8 need no
further method extraction from the old workshop. A positive future comparison
or verifier result does not erase earlier incidents or establish improvement
rates.
