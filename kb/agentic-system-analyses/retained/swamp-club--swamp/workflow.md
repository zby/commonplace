---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Swamp workflow account: commit verification through selected parallel agent reviews, verdict rejection and cleanup."
run-id: AAS-2026-10-15-swamp-440d19cc0bcc-01
reviewed-boundary: "380e3c307164501c7d705f7707a864f4612b2785"
---

# Swamp workflow report

## Workflow account

### Selection and evidence

The representative workflow is `verify-reviews`, the shipped pre-PR review of a proposed commit. It connects a concrete request, isolated review checkout, change selection, parallel external-agent calls, computational verdict checks and terminal cleanup. Unlike an invented combination of CLI capabilities, these handoffs are joined in one authored workflow. Its existing identity is [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict); scheduling and returning method execution are [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run) and [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run). This member adds workflow-specific findings without redeclaring those referents.

All source evidence is SRC-1 at the revision fixed in [boundary](boundary.md#boundary-and-evidence). Added inspection covers the complete `verification/workflow-verify-reviews.yaml`, `scripts/check_review_verdict.ts` and `verification/review-prompts/code-review.md`, plus the guard evaluation branch in `src/domain/workflows/execution_service.ts`. YAML, shell and parser code supply implementation evidence; the review prompt supplies doctrine/design. No execution trace establishes that reviews ran, files were actually read, cleanup succeeded or the reviewed change was correct. Specialized review prompt bodies and downstream attestation/merge consumers were not inspected here; their effectiveness and admission authority remain outside this account's conclusions.

### 1. Request to a review checkout

The caller supplies required string inputs `commit` and `branch`; the checkout command uses `commit` as its revision. The inspected workflow does not use `branch` to choose the review target or independently establish an authenticated proposer. The workflow, not a foreground agent, owns the next-step schedule. SRC-1: `verification/workflow-verify-reviews.yaml`.

The setup shell retries a failed fetch of `origin/main` once, creates a detached run-keyed worktree, initializes Swamp there and restores tracked files changed by initialization. This separates review file reads from the invoking checkout and removes initialization edits from the diff. It does not pin the external main ref to this analysis revision, isolate host capabilities or authenticate the submitted code. The source being analyzed is frozen; the workflow's future review inputs are not a supplied observed run.

> git worktree add --detach "$CHECKOUT_DIR" "${{ inputs.commit }}"
> swamp repo init "$CHECKOUT_DIR"
> --- `verification/workflow-verify-reviews.yaml`

> git -C "$CHECKOUT_DIR" checkout -- .
> --- `verification/workflow-verify-reviews.yaml`

### 2. Checkout to change selection

Only a successful setup permits `detect-changes`. Its two ordered `@swamp/git` calls request a merge-base-relative diff and then changed filenames, explicitly pointing at the run's worktree. The per-run behavior name keeps persisted input definitions from deliberately sharing one worktree path across runs. The comments explain that motivation; this is not measured race freedom. SRC-1: `verification/workflow-verify-reviews.yaml`.

> repoPath: "/tmp/swamp-verify-reviews-${{ run.id }}"
> base: "origin/main"
> nameOnly: true
> threeWay: true
> --- `verification/workflow-verify-reviews.yaml`

After successful detection, code review is unconditional. Adversarial, UX and CI-security reviews have path guards over the retained `diff` data's file list: adversarial covers selected implementation directories, UX covers CLI/presentation/errors/libswamp paths, and CI security covers `.github/workflows/`. A zero matching count produces a truthy guard, which skips the step rather than running it. The scheduler's implementation confirms this non-obvious polarity. The specialized reviewer receives the full generated diff, not a path-filtered subset; paths select which reviewer runs. SRC-1: `verification/workflow-verify-reviews.yaml`, `src/domain/workflows/execution_service.ts`.

> if (guardResult) {
>   guardLogger
>     .debug`Step ${stepName} guard skipped: ${guardCel} → ${guardResult}`;
>   stepRun.skip({ kind: "guarded", expression: guardCel });
> --- `src/domain/workflows/execution_service.ts`

### 3. Selected work to external reviewers

The workflow sets concurrency to four and leaves review steps without mutual dependencies. Each selected shell step computes its merge base, writes a diff to a temporary file and builds a prompt from a review-specific Markdown file plus a diff pointer and verdict-format instruction. Despite the YAML description saying the diff is inlined, the implementation passes its pathname and asks the reviewer to read it. The handoff therefore supplies reachability, not proof of consumption. SRC-1: `verification/workflow-verify-reviews.yaml`; invocation evidence is retained in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict).

Each step launches a separate `claude -p` process requesting `claude-opus-5-5` and Read, Glob and Grep. Swamp owns the task split, filesystem context and shell return channel; the external model owns review judgment. Exact weights, actual tool enforcement and internal context management remain uninspected as recorded in [RT-CMP-agent-models](runtime.md#rt-cmp-agent-models).

The code-review prompt scopes findings to changed code, permits contextual reads, asks for repository conventions and the DDD skill, and distinguishes blocking defects from suggestions. It supplies review criteria, not an expected correct answer. There is no established answer oracle for code quality. SRC-1 doctrine/design: `verification/review-prompts/code-review.md`.

> You may read other files in the repository for context, but
> every finding must be about a change in the diff.
> --- `verification/review-prompts/code-review.md`

Separate reviewer processes keep their full review conversations out of any caller's conversation. Raw reviewer prose crosses back through `tee`, shell output and persisted workflow outputs; temporary prompt/diff/result files are deleted on the ordinary inspected shell paths. This is task isolation and selective return, not an inspectable Swamp token-window policy or demonstrated compliance with the prompts. SRC-1: `verification/workflow-verify-reviews.yaml`; persistence mechanism: [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run).

### 4. Reviewer return to computational acceptance or rejection

The shell enables `pipefail`, captures the pipeline exit, removes prompt/diff files and fails explicitly if that pipeline failed. Otherwise it passes the captured reviewer output to the verdict script, removes that result file and returns the script's exit code. Both an agent-process failure and an unfavorable parsed verdict can therefore reject this review step. SRC-1: `verification/workflow-verify-reviews.yaml`.

> VERDICT_EXIT=$?
> rm -f "$RESULT_FILE"
> exit $VERDICT_EXIT
> --- `verification/workflow-verify-reviews.yaml:146-148`

The parser first detects recognized provider-error text outside stripped Markdown code. Otherwise it uses the first line-initial pass/fail marker, with flexible emphasis and case. It does not require the first response line to contain that marker. Its byte threshold classifies missing-marker output; it does not impose a minimum-length requirement on a marked pass. These checks govern output syntax and recognized failures, not defect-detection accuracy. SRC-1: `scripts/check_review_verdict.ts`; provider and marker passages are retained in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict).

> const marker = output.match(VERDICT_MARKER_PATTERN);
> if (marker) {
>   return marker[1].toLowerCase() === "pass" ? { kind: "pass" } : {
>     kind: "fail",
>   };
> }
> --- `scripts/check_review_verdict.ts`

The script prints a separate `GATE_VERDICT` line and returns zero only for pass. Explicit fail, missing output/marker, recognized provider error or unreadable result file fails the script. The model proposes the quality judgment; the script decides protocol acceptance and has a computational veto. No per-review human decision is required by this YAML, and this veto is not proof of a universal merge gate. SRC-1: `scripts/check_review_verdict.ts`.

> const verdict = determineVerdict(output);
> console.log(formatGateVerdict(verdict));
>
> if (verdict.kind === "pass") {
>   return 0;
> }
> reportFailure(label, verdict, output);
> return 1;
> --- `scripts/check_review_verdict.ts`

### 5. Failure handling and delivered result

The authored cleanup job depends on reviews with an `always` condition. It attempts forced worktree removal, prunes worktree metadata and deletes run-keyed auto-definitions. The shell tolerates removal/deletion errors and its task sets `ignoreExitCode: true`; cleanup is best effort, not evidence that all temporary state disappears. This inspected dependency does not establish cleanup after every possible setup failure, process kill or host crash. SRC-1: `verification/workflow-verify-reviews.yaml`.

> git worktree remove --force "$CHECKOUT_DIR" 2>/dev/null || true
> git worktree prune
> --- `verification/workflow-verify-reviews.yaml`

> ignoreExitCode: true
> --- `verification/workflow-verify-reviews.yaml`

The workflow delivers review prose, parser diagnostics/gate decisions and workflow step/run outcomes through the execution machinery, not a merged change. Persisted run state supports inspection and continuation as described in [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run). The selected review YAML contains one reviewer invocation per selected step, not an automatic repair-and-re-review loop. Its only explicit retry is the setup fetch. The caller must decide whether to repair code, fix provider access or rerun after rejection; general failed-run reset is a separate scheduler facility in [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run). Neither retry nor cleanup rolls back the submitted code, and no successful improvement, release or downstream use follows from this source inspection.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict)

Workflow role: the selected end-to-end review request, from commit input through setup, change detection, parallel review, gate parsing and cleanup. The account above supplies added SRC-1 evidence and local limits rather than a second route identity.

Delegation: symbolic job/step dependencies delegate selected review tasks to separate external Claude processes. Prompt files carry criteria; diff pointers and the fresh worktree supply reachable evidence. Only reviewer output and shell/gate results cross back, not a demonstrated complete model conversation.

Verification authority: the external reviewer judges changed code; shell and parser can veto a review step. The parser checks a protocol, not a reference answer. This is open commit verification, not a bounded curriculum. Human merge/admission decisions beyond this workflow are uninspected.

Recovery and delivery: one setup fetch retry is explicit. Review rejection returns diagnostics and a failing step; the selected YAML does not repair code automatically. Cleanup is best effort. Delivered review/run outputs are not demonstrated repository admission, successful criticism or improved code.

- implementation conclusion status: wired
- operation conclusion status: uninspected
