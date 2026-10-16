---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "CORAL workflow: task-directed coding, circle-packing verification, asynchronous feedback and optional candidate export."
run-id: AAS-2026-10-15-coral-25e5fdab9dc4-01
reviewed-boundary: "0123dfb939b35228cf2c1fde224cd0561e727408"
---

# CORAL workflow report

## Workflow account

### Selection and evidence boundary

This account follows one coding experiment from a configured objective to a committed, graded candidate, then to optional export as an ordinary Git branch. Circle packing supplies the concrete objective and verifier. It was selected because the shipped task, candidate interface and grader make the evaluation handoff inspectable, rather than requiring an inferred research success. This is a source-supported workflow, not a reconstructed execution. SRC-1 supplies implementation and doctrine/design evidence only; no target code, tests, examples or services were executed.

The generic launch and supervision baseline comes from [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch). The concrete example's `examples/circle_packing/task.yaml` selects `docker-opencode`, not the baseline's default Claude runtime. Its comment describes preset inheritance, but this account does not independently inspect that preset or establish a successful OpenCode/Docker launch. The evaluation and export mechanisms below are inspected independently of that adapter choice. This prevents treating a generic capability trace as proof that the exact packaged example ran end to end.

Additional SRC-1 inspection covers the complete circle-packing task and grader; submission's queue, checkpoint and pending-record block in `coral/hooks/post_commit.py`; daemon `_grade_one` in `coral/grader/daemon.py`; and CLI evaluation, result formatting and export in `coral/cli/eval.py`. These add implementation coverage, except the task's objective and advice, which specify intent. They add no observed-run evidence.

### 1. Objective and launch handoff

The task author supplies a program contract: pack 26 circles in a unit square, maximize the sum of radii, and expose `initial_program.py:run()` returning centers, radii and a claimed sum. The task configuration chooses the packaged grader, maximization direction and a 600-second evaluation timeout. It also supplies optimization suggestions; these guide proposals rather than deciding which edits are accepted (SRC-1, `examples/circle_packing/task.yaml`).

> Pack N = 26 circles into a unit square (side length 1) to maximize the sum of radii.
> --- `examples/circle_packing/task.yaml`

The operator launches the configured experiment. CORAL structurally validates the task, provisions project/worktree state, starts supporting services and delegates coding to external harness processes. Each handoff supplies worktree identity, role/instruction files, runtime settings and shared-state links; the external harness/model chooses implementation steps. CORAL owns process supervision, not every tool turn. Structural task admission is not proof that the seed passes the grader ([RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch), [RT-OBJ-task-config](runtime.md#rt-obj-task-config); SRC-1, `coral/cli/start.py`, `coral/agent/manager.py`).

Generated instructions prescribe plan → edit → eval → repeat. They also afford specialist delegation; the foreground agent chooses whether to spawn a seeded specialist, with host-owned execution and return transport. A requested librarian summary plus shared-file edits is not evidence that a separate context ran. The selected experiment does not require an invented specialist invocation to connect coding to evaluation ([RT-BAP-generated-instructions](runtime.md#rt-bap-generated-instructions), [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation); SRC-1, `coral/template/coral.md.template`, `coral/template/agents/librarian.md`).

### 2. Candidate submission and independent evaluation

The coding agent calls `coral eval -m ...` after editing. Submission checks the configured pending limit before committing; excess outstanding work can be rejected without a new candidate commit. On the admitted path it commits current code, checkpoints shared state and writes a pending attempt linking the commit, agent, parent and checkpoint. This captures lineage, not verified truth of notes or a passing solution. There is no score or human approval gate before this commit ([RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission), [RT-OBJ-attempt](runtime.md#rt-obj-attempt); SRC-1, `coral/hooks/post_commit.py`).

The daemon takes that commit hash, creates a detached checkout, invokes the configured grader worker, removes the checkout in `finally`, and writes a finalized attempt. The handoff gives evaluation an immutable candidate snapshot relative to concurrent live-worktree edits; it does not freeze external dependencies or establish hostile-code containment ([RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution); SRC-1, `coral/grader/daemon.py`).

In circle packing the grader calls the candidate's `run()`, converts the returned arrays, checks shapes, NaNs, negative radii, square boundaries and overlaps, then recomputes the radii sum. Boundary and overlap checks allow a numerical tolerance of `1e-6`. The score is recomputed sum divided by `2.635977`, not the candidate's claimed sum. That constant is a reference outcome, not an expected arrangement or proof of global optimality. The model proposes; task-author software decides the measured outcome. Inspection establishes these checks, not that they exhaust possible numerical or adversarial defects (SRC-1, `examples/circle_packing/grader/src/circle_packing_grader/grader.py`; [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution)).

### 3. Failure, information loss and recovery

An overlapping arrangement takes a concrete rejection branch: the evaluation script emits score zero and an overlap detail, then exits. This rejects the candidate as a positive-scoring packing, not its commit or its presence in attempt history. Importantly, the outer grader's ordinary explanation reads score, sum and elapsed time but does not incorporate `details`. The overlap diagnosis therefore does not automatically reach the agent in the normal score explanation. See the workflow annotation on [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution) below. A zero score must not be described as automatically giving the agent the exact violated constraint.

Infrastructure failure has a different owner and signal. A timeout or exception escaping to the daemon yields `timeout` or `crashed`, feedback and grader-error budget classification; the checkout is still removed. A grader that internally converts failure to a bundle instead follows the completed-bundle path. These distinctions limit any blanket statement that every candidate failure becomes a daemon crash (SRC-1, `coral/grader/daemon.py`, `examples/circle_packing/grader/src/circle_packing_grader/grader.py`).

The default CLI caller waits for finalization and prints score, commit, status and feedback. A caller wait timeout is not a failed grade: the CLI prints `STILL PENDING`, exits with code 2 and points to `coral wait <hash>`. Waiting again observes the same attempt rather than necessarily creating another evaluation. Asynchronous submission returns pending state earlier ([RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission); SRC-1, `coral/cli/eval.py`, `coral/hooks/post_commit.py`).

### 4. Feedback, continuation and delivery

The manager reads finalized attempts, applies stop rules and heartbeat selection, and can interrupt/resume the committing agent with selected score/title/feedback and action prompts. The resumed model chooses the next correction. Prompted reflection, consolidation and knowledge updates are not independently checked completion conditions. Batched arrival handling does not establish one feedback interrupt per attempt ([RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback); SRC-1, `coral/agent/manager.py`, `coral/agent/heartbeat.py`). This is a metric-directed experiment loop with software scheduling and model-authored candidates, not an evaluator that synthesizes the correction itself.

A failed iteration can be followed by another edited candidate. Explicit resume steering can instead select an earlier hash, reset matching descendant worktrees and archive discarded attempt segments. That is caller-directed recovery, not automatic rollback of code, knowledge, session narrative and services as one transaction ([RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering); SRC-1, `coral/agent/manager.py`, `coral/hub/steering.py`). Shared artifacts remain a coordination/read-back surface; a checkpoint alone does not prove a later agent used or corrected them.

An iteration is delivered locally when its committed candidate and terminal attempt remain inspectable and the CLI can report the outcome. That outcome may be failure. For handoff outside the experiment, a caller can select an attempt and export its commit as a normal branch ([WF-RTE-candidate-export](#wf-rte-candidate-export)). Export does not require a winning score or even inspect attempt status. It is a separate caller selection, not automatic best-candidate promotion. The printed checkout command hands subsequent ordinary Git work to the user. No deployment, task success, realized research improvement or instruction compliance is established by these source paths.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-candidate-export
Label: Candidate export handoff

Caller-selected attempt hash and branch → attempt-file resolution → run repository/object checks → branch conflict check → Git branch creation → printed checkout instructions. CORAL's CLI owns this symbolic Git operation; the caller chooses the candidate and destination branch. It changes a branch reference in the run's source clone, not the active agents or a deployed product. Evidence: SRC-1, `coral/cli/eval.py`, `cmd_export`.

Distinct identity: unlike [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission), this consumes an already recorded candidate rather than committing edits or queuing grading; unlike [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering), it does not reset/relaunch agent worktrees. No supplied runtime record declares this branch-export handoff.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success prints selected short hash, branch, repository path and a suggested Git checkout command; failures exit with a diagnostic.
- Later read-back: the new branch retains access to the selected candidate for later normal Git checkout; no automatic return into the agent loop is established.
- Delegated visibility: the caller receives repository and branch pointers, not a packaged session, shared-state restoration or deployment artifact.
- Selection predicate: caller hash resolves to an attempt file, run repository exists, object is accessible, and branch is absent unless force is requested; score/status is not checked.
- Invalidation or expiry: later Git operations can move/delete the branch; force permits overwriting an existing reference; no expiration is specified in this function.
- Activation or effect: creates or force-updates a Git branch; actual checkout, execution and downstream use are unobserved.
- Evidence limits: caller identity need not be human; successful export and external product acceptance were not observed; the function does not validate candidate correctness.

Admission trigger/change: explicit export request admits a selected candidate to an ordinary branch. Software can reject unresolved attempts, unavailable objects/repository, existing branch without force or Git failure. No model chooses the best candidate here and no expected-answer oracle is consulted. Operating mode is caller-controlled handoff after or during optimization. Guidance is the printed checkout instruction; the persistent result is a Git reference. Recovery from an undesired selection requires deliberate ordinary Git branch management, not an automatic rollback implemented here.

> if branch_exists and not args.force:
> --- `coral/cli/eval.py`

> print(f"Exported {target[:12]} → branch '{branch}' in {repo_dir}")
> print(f"  cd {repo_dir} && git checkout {branch}")
> --- `coral/cli/eval.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution)

Workflow verification boundary: circle-packing geometric rejection and agent-visible diagnosis differ. The script's overlap branch produces `score`, `details` and elapsed time. The enclosing `evaluate` extracts score and defaults missing sum to zero; its explanation uses those values and the benchmark but omits `details`. Thus a zero-scored invalid packing can produce a generic score explanation without the explicit rejection reason. This narrows what corrective information the candidate author receives; it does not change the supplied record's task-dependent oracle identity. SRC-1, `examples/circle_packing/grader/src/circle_packing_grader/grader.py` (implementation).

> score = result.get("score", 0.0)
> sum_radii = result.get("sum_radii", 0.0)
> eval_time = result.get("eval_time", 0.0)
> --- `examples/circle_packing/grader/src/circle_packing_grader/grader.py`

> explanation = (
>     f"Sum of radii: {sum_radii:.6f} | "
>     f"Score: {score:.6f} | "
>     f"Time: {eval_time:.1f}s | "
>     f"Benchmark: {BENCHMARK:.6f}"
> )
> --- `examples/circle_packing/grader/src/circle_packing_grader/grader.py`

The daemon adds an evaluation-log pointer, but that pointer alone does not establish that the missing geometric detail was logged or subsequently inspected. Candidate rejection leaves its commit and finalized attempt available for comparison or optional export. No supplied execution establishes successful diagnosis or recovery.

#### On [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission)

Workflow wait boundary: CLI observation timeout leaves grading unresolved rather than rejecting or rolling back the candidate. `cmd_eval` distinguishes a RuntimeError submission failure (exit 1) from a TimeoutError while waiting (exit 2), and instructs the caller to keep waiting. Evidence: SRC-1, `coral/cli/eval.py` (implementation).

> f"CORAL Eval: STILL PENDING\n"
> --- `coral/cli/eval.py`

> f"Use `coral wait <hash>` to keep waiting, or check `coral log`.\n"
> --- `coral/cli/eval.py`
