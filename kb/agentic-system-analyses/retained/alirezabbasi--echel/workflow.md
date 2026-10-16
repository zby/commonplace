---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Echel workflow account: caller-created legacy work packet through Hermes delegation, separately invoked verification and bounded result delivery."
run-id: AAS-2026-10-15-echel-08d27848b99a-01
reviewed-boundary: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
---

# Echel workflow report

## Workflow account

### Selected workflow and starting condition

The representative workflow is a caller-created legacy work packet, compiled into a Hermes task, followed by caller-invoked verification. It was selected because the shipped CLI wires each of these steps to concrete state producers and consumers, rather than merely listing agent capabilities. This is a supported sequence of explicit invocations, not an autonomous orchestration loop or an observed successful run. The frozen source and external-runtime exclusions are in [boundary](boundary.md#boundary-and-evidence). All source evidence below is SRC-1 implementation or doctrine/design; no target commands, tests or examples were executed.

The starting condition is existing legacy `FileStore` project state and any related knowledge. The runtime baseline establishes the important break: current CLI initialization writes canonical records, not the legacy project/work/knowledge layout needed here. Consequently this account does not claim a working fresh `init` → implementation journey. See [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) and [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow), grounded in SRC-1, `src/echel/cli/main.py`, `src/echel/storage/files.py` and `src/echel/workflow.py`. The in-repository `FileStore.initialize` API supplies the legacy starting state; the CLI's current `init` branch does not call it.

### Work definition and context handoff

The caller owns decomposition into work items. Through `work`, the caller supplies title, objective, explicit knowledge relationships, acceptance criteria and verification commands. `WorkflowService.add_work` checks that referenced records exist, assigns an ID and the project's current stage, and persists a planned work item. It does not generate a plan with a model or require that related knowledge be accepted. This is the existing [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow), not a new workflow identity (SRC-1, `src/echel/workflow.py`, `src/echel/model/records.py`).

The next invocation is the caller's choice: inspect `context`, preview `run`, or launch `run --execute`. Compilation reloads the work record and rejects a non-work record. It includes knowledge whose IDs occur in `relates_to`, and open findings whose affected IDs intersect those relationships. The text contains objective, acceptance, verification commands, knowledge statements with status/confidence, and finding statements. It omits full provenance and most metadata. There is no accepted-only predicate. [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) and [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) retain the selection evidence (SRC-1, `src/echel/context/compiler.py`).

This working-context boundary is deterministic code selection before delegation, not an isolated subagent frame. Unrelated records stay out of the supplied text but remain on disk. A later invocation recompiles from current files. The source's explicit repair guidance is to change justified relationships rather than load everything (SRC-1, `examples/first-product.md`, doctrine/design):

> Once a work item exists, `echel context` includes only explicitly related knowledge. This is intentional: context omissions should be fixed by adding a justified relationship, not by injecting the whole repository.
> --- `examples/first-product.md`

### Delegation, return and delivery

Echel delegates one task to the external Hermes process, not a source-visible tree of workers. The handoff is rendered natural-language context, workspace directory, optional model label and requested toolsets. Hermes receives the text through `-q`; it owns subsequent model/tool decisions. Echel's adapter waits synchronously. Runtime-internal delegation, summarization and actual tool behavior remain uninspected, not evidenced absent. See [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) and [RT-CMP-runtime-model](runtime.md#rt-cmp-runtime-model), supported by SRC-1, `src/echel/runtimes/hermes.py`. The implementation skill requests inspection, verification and separately returned knowledge proposals, but its automatic loading is not established; [RT-BAP-implementation-skill](runtime.md#rt-bap-implementation-skill) is instruction evidence, not enforced output structure.

Without `--execute`, the delivered result is only a persisted preview run with a constructed command. With execution, the CLI converts process exit into run status and retains a bounded stdout summary (SRC-1, `src/echel/cli/main.py`, implementation):

> if args.execute:
>     result = runtime.execute(request)
>     run.status = "completed" if result.exit_code == 0 else "failed"
>     run.exit_code = result.exit_code
>     run.summary = result.stdout[-4000:]
> store.put("runs", run.to_dict())
> _emit(run, args.json)
> --- `src/echel/cli/main.py`

Delivery at this boundary therefore means run JSON persisted and emitted to the caller, with command, context digest and available process result. `completed` is not semantic acceptance of the implementation. The CLI does not update the work item's planned status, set the run's completion timestamp, preserve stderr in that run, promote discoveries into knowledge, or automatically run verification. These limits follow the inspected run branch and record defaults (SRC-1, `src/echel/cli/main.py`, `src/echel/model/records.py`). Code edits, if Hermes makes them, occur in the supplied workspace; Echel supplies no separate commit, release or deployment handoff here.

### Verification, failure and recovery

The caller separately invokes `verify` for the work ID. The runner loads stored verification strings, splits each into argv, and runs the executable at the workspace directory. These checks are not mediated by Hermes toolsets. Every returned command result becomes an Evidence record linked to the work ID, with exit code and a checksum of stdout plus stderr, rather than retained output bytes. The existing [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) supplies the route and quotation (SRC-1, `src/echel/verification/runner.py`).

The computational acceptance predicate is executable exit zero. Whether a command encodes the work's semantic acceptance criteria depends on the caller-authored executable; no general product-correctness oracle is supplied. A failed check records failure but does not reject knowledge, undo code changes, or cause another Hermes run. The loop continues after a nonzero return because `check=False` is followed by evidence persistence and the next iteration. Launch or argument-parsing exceptions can interrupt the sequence after earlier effects and evidence. A list of checks is thus not an atomic verification transaction (SRC-1, `src/echel/verification/runner.py`).

A concrete earlier failure path is missing Hermes. The adapter rejects execution before returning a runtime result (SRC-1, `src/echel/runtimes/hermes.py`):

> if not self.available():
>     raise RuntimeError("Hermes executable is not installed or not on PATH")
> --- `src/echel/runtimes/hermes.py`

The CLI catches this RuntimeError and returns error code 2. Because persistence follows execution, that failure does not save the allocated Run. In contrast, a subprocess that returns nonzero produces a persisted failed Run, while the CLI still reaches its ordinary return code 0. A caller must inspect run status/exit code, not treat CLI success as task success (SRC-1, `src/echel/cli/main.py`; [RT-RTE-compile-run](runtime.md#rt-rte-compile-run)).

Recovery belongs to the caller: remedy the runtime problem, revise work/context or project changes, and explicitly rerun execution or verification. The inspected adapter/CLI/runner provide no retry, compensating rollback or verification-driven scheduler. Formal knowledge approval is a different canonical service, [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide), not a wired final stage that converts this workflow's run summary or evidence into accepted knowledge. No successful implementation, repair cycle, human acceptance or production delivery is established by these source paths.

### Inspected scope

This member directly inspected SRC-1, `src/echel/cli/main.py`, `src/echel/workflow.py`, `src/echel/context/compiler.py`, `src/echel/runtimes/hermes.py`, `src/echel/verification/runner.py`, `src/echel/model/records.py`, `src/echel/storage/files.py`, `examples/first-product.md` and `docs/hermes.md`. The latter explicitly describes streamed events, cancellation, resumption, tool approvals, isolated worktrees and bounded subagent summaries as future work. This adds workflow-focused inspection and a source passage for context-omission repair, not another source or observed execution layer.

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

#### On [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow)

Workflow role: caller-owned decomposition and packet definition precede agent delegation. Lifecycle advance is not a prerequisite enforced by work creation. The caller supplies both acceptance language and executable checks; reference existence is not knowledge approval or semantic work validation.

#### On [RT-RTE-compile-run](runtime.md#rt-rte-compile-run)

Workflow role: one blocking external-runtime handoff and result return. Preview delivery and executed-run delivery are different outcomes. Returned process status does not close the work item or schedule the verifier; caller control resumes after the emitted run. Missing-runtime failure occurs before run persistence, unlike a nonzero returned process result.

#### On [RT-RTE-verify-work](runtime.md#rt-rte-verify-work)

Workflow role: independently invoked check/evidence phase, not an automatic acceptance gate after Hermes. Checks can fail without rollback and without requesting repair. Evidence delivery ends this inspected sequence; further revision, acceptance and release remain caller decisions, not attained outcomes.
