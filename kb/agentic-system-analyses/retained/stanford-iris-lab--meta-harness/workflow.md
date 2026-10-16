---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Meta-Harness workflow account: Terminal-Bench scaffold proposal, delegated implementation, admission, evaluation and winner delivery."
run-id: AAS-2026-10-14-meta-harness-5e480e270fee-01
reviewed-boundary: "8123ccabe2b19fa1123090b2e5f1bacc20963ce8"
---

# Meta-Harness workflow report

## Workflow account

This account selects the Terminal-Bench reference search because its shipped proposer instructions specify consequential analysis and implementation handoffs, and its driver connects their candidate output to independent task evaluation and retained winner selection. It traces [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), not a composite of the classification and experimental pilot workflows. Evidence is SRC-1 at the revision in [boundary](boundary.md): inspected implementation and shipped doctrine/design, with no observed delegation, completed search or measured improvement.

### Request and division of responsibility

The operator invokes `meta_harness.py` with iteration, trial, concurrency and run-name controls. The Python driver creates run-specific job/log directories, optionally evaluates baselines, seeds the frontier from available baseline results, and resumes iteration numbering from the highest summary entry. It removes the previous pending manifest before starting a fresh Claude proposer session. The session receives the current iteration, model, parent baseline, evaluation size and explicit paths to history, frontier, reports and pending output. The driver owns benchmarking; the coding model owns candidate design and implementation. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`.

The wrapper supplies the proposer skill as described in [RT-BAP-proposer-instructions](runtime.md#rt-bap-proposer-instructions). The skill states the division explicitly:

> **You do NOT run benchmarks.** You analyze results + failed trajectories, propose agent variants, and implement them. The outer loop (`meta_harness.py`) handles benchmarking.
> --- `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`

This is requested model behavior, not a filesystem prohibition. The operator starts and configures the search but does not approve each candidate. The model receives instructions to create one general-purpose variant testing one mechanism, without task-specific hints or edits to existing agents, driver or wrapper. Actual compliance is unobserved; candidate execution authority follows the software checks, not a human content decision. See [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution).

### Analysis → implementation → manifest

The main proposer is instructed to launch one analysis subagent. That child reads frontier and evolution-summary files, failed and successful trajectories under the run's jobs/logs, and candidate implementations. Its requested return is a five-line state summary plus a falsifiable hypothesis, candidate name, specific changes and predicted pass-rate and token/turn effects. The main proposer then launches one implementation subagent with the selected change and working directory:

> Launch **1 Agent subagent** (subagent_type: "general-purpose"). The prompt must include the candidate name, class name, specific changes from Step 1, and the working directory.
> --- `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`

The implementation child copies a starting agent into a new candidate file, makes targeted edits, performs an import check and returns its file path and validation status. Its instruction calls this a smoke test, but the specified command only imports Python; it is distinct from the driver's subsequent one-task runtime smoke trial. These handoffs are doctrine/design evidence. They do not show that children actually ran, received only those inputs, or returned correct conclusions. Shared filesystem edits remain effects outside a child's returned text; Claude Code owns actual context isolation. SRC-1, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`.

The main proposer writes the pending manifest with iteration, candidate name/import path, hypothesis, changes and expected efficiency. Its terminal `CANDIDATES` text is not the driver's candidate-list authority. The driver reads [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval) and normalizes the class portion of each import path to `AgentHarness`. Successful proposer exit and file existence advance this handoff; they do not establish manifest correctness. In the inspected driver, manifest JSON parsing is not wrapped in a recovery handler, so malformed JSON is not covered by the graceful no-candidate continuation. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`.

### Admission and task verification

The driver independently imports the exact class and requires Terminus2 inheritance. With smoke enabled, it then runs one task/one trial through the evaluation adapter. Smoke accepts a zero subprocess exit, existing job result and no reported errors; it does not require a positive verifier reward. Thus the check screens compatibility/runtime failure, not candidate improvement. `--skip-smoke` bypasses that runtime gate, but not the import check. Importing itself executes Python; neither stage proves safe source or deployed isolation. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`.

The admission branch is explicit:

> if args.skip_smoke:
>     print(f"{prefix} {_green('import OK')} (smoke skipped)")
>     valid.append(c)
> elif smoke_test(name, import_path):
>     print(f"{prefix} {_green('import OK + smoke OK')}")
>     valid.append(c)
> --- `reference_examples/terminal_bench_2/meta_harness.py`

For admitted candidates, the driver supplies import path, trial count, concurrency, job name and job directory to `scripts/run_eval.sh`. The adapter validates the class again and dispatches Harbor with the dataset, selected external model and Runloop/Modal environment. Harbor imports the candidate and owns the external task execution/verifier machinery. The target's parser reads individual trial results, not the possibly stale top-level aggregate. Missing/corrupt trial files and missing rewards contribute zero; positive verifier rewards count as passes. Expected trial counts produce warnings rather than an enforced complete-dataset gate. Therefore a displayed rate is over parsed trials, not proof that every expected task/trial completed. SRC-1, `reference_examples/terminal_bench_2/scripts/run_eval.sh`, `reference_examples/terminal_bench_2/meta_harness.py`. Task verifier rewards are the answer oracle; proposer critique is not.

### Rejection, recovery and return to another round

Proposer failure or missing manifest skips the iteration. Invalid imports and failed smoke checks are not admitted to full evaluation. If none are valid, the driver records the proposed candidates with failed outcomes and continues. A nonzero or timed-out main benchmark produces an empty per-task result and zero aggregate for that candidate; the main evaluation loop does not parse that failed job's partial results. Earlier frontier winners are retained unless a strictly better parsed score replaces them. Recovery is continuation and retained selection, not automatic restoration of filesystem edits. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`; see [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search).

After evaluation, software updates per-task and overall frontier entries and appends candidate identity, hypothesis, changes, scores, outcome, timing and rollout metrics to the evolution summary. The next fresh proposer receives history paths and is instructed to read them. This wires a feedback opportunity across rounds, not evidence that the model diagnosed failure, revised its hypothesis or improved future capacity. The theory and operation limits in the runtime route remain applicable.

### What is delivered

Ordinary completion leaves candidate Python/prompt files, job artifacts, summary and frontier files, with printed evaluation status. These are search outputs; no deployment or automatic installation of the winner into an unrelated application is shown by this driver. The frontier names the best scored agent rather than freezing its bytes. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`.

With `--full-eval`, if uninterrupted, the driver looks up the overall frontier winner's import path in the summary and runs five trials on the same full dataset, provided the winner is not the baseline and a path is found. This is repeat evaluation, not an untouched holdout. The final branch differs from the main benchmark's failure treatment: it ignores the success flag and parses results whenever the job directory exists. Consequently partial results can be displayed even after a failed/timed-out final job, and the completion message is not a universal successful-evaluation certificate. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`.

> job_dir, _ = harbor_run(
>     import_path,
>     job_name,
>     n_trials=5,
>     n_concurrent=args.concurrent,
> )
> if job_dir.exists():
> --- `reference_examples/terminal_bench_2/meta_harness.py`

Added inspection for this lens covers the full terminal proposer skill and evaluation adapter, plus driver sections for class validation, result parsing, history writes, proposal/smoke handling, search sequencing and optional final evaluation. These supply implementation and doctrine/design evidence only. External Claude Code delegation, Harbor execution/verifiers, providers and remote sandboxes remain external contracts; no target code, tests or model calls were executed.

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

#### On [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search)

Workflow handoff distinction: the requested implementation child's import check returns file/status to the parent proposer; the driver's independent import/subclass check and optional one-task smoke trial decide admission to benchmarking. The former is an instructed self-check, not delegation of the driver's veto. The analysis child's requested mechanism/efficiency prediction supplies the implementation brief; it does not supply a verifier score.

Delivery limit: the ordinary search delivers retained files and selected identities, not deployment. The optional final pass may display partial results because its caller discards the evaluation success flag before checking job-directory existence. This qualifies the main-loop failure policy without changing the route's identity or claiming an observed failure.
