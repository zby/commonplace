---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agent runtime, orchestration system, agent operating layer, agent memory/knowledge/context-engineering system, or narrower model-dependent operational mechanism from inspectable sources."
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Bash
argument-hint: "<repository locator or explicit local/document source>, optional source revision and worker profile"
---

# Analyse an Agentic System

Analyse the caller's explicit system at a frozen evidence boundary, integrate
its accepted publication into `main`, and report the result and advisory audit.
The command owns preparation, execution, guarded integration and reporting;
this skill is an invocation adapter, not another scheduler.

A new `analyse` or `batch` invocation authorizes isolated worktrees, local run
evidence, source acquisition, accepted publication and guarded integration.
Integration stages and commits only that publication and its required incumbent
archive. Invocation does not authorize source edits, unrelated staging or
commits, cleanup, transfer scans, comparison rebuilds or landscape synthesis. Do not read prior retained analyses or reviews
to select a target or supply analyst inputs.

## Confirm the target

Use only the caller's supplied source. If it is missing or ambiguous, ask:
“Which system should I evaluate? Please provide its repository URL or local
checkout.” Stop for the answer. Do not infer a target from the ambient checkout,
prior reports or triage conclusions. Resolve ambiguous source scope, requested
revision and nondefault worker profile before invocation.

For a supplied repository root locator:

```bash
commonplace-analysis analyse https://github.com/owner/repository
```

The command validates locator shape without network probes. New runs default to
`pi-sol` (`gpt-6.1-sol`, medium effort). Pass `--worker-profile <name>` for an
explicit override; every role, including verifiers, uses that one profile.
An initiating agent supplies `--model <its-model-id>` for integration commit
attribution; do not infer that identity from the analyst profile.
`--source-revision <full-40-hex-commit>` pins a caller-selected GitHub revision.
Do not select another method revision after preparation refuses the default;
`--revision <commit>` requires the operator's choice.

Preserve explicit non-repository inputs:

```bash
commonplace-analysis analyse /absolute/source/path --source-kind local
commonplace-analysis analyse "supplied document bundle" --source-kind documents \
  --system "System name" --source-identity "stable source identity"
```

Local paths are made absolute before preparation. Non-Git capture remains the
boundary worker's responsibility. GitHub identities use code-owned acquisition;
do not clone or fetch ahead of the command. If the caller requests preserving a
local GitHub checkout's revision, read its full commit and pass
`--source-revision`. Do not silently reinterpret malformed repository input as
documents.

For an explicitly authorized list, use one bounded queue:

```bash
commonplace-analysis batch /absolute/targets.txt --concurrency 4
```

The list is newline repository locators or a JSON list of target objects. See
`commonplace-analysis batch --help` and the [command reference](../../../reference/commands.md#commonplace-analysis).
Duplicate normalized identities are refused. Keep triage rationale outside the
source inputs. Four simultaneous analyses with the default three role workers
permit twelve role workers, not four. Audits occupy their analysis's slot.
Before a substantial real batch, obtain provider-capacity, storage/inode and
worktree-placement decisions. Fixtures do not establish live capacity.

## Isolated run setup

`analyse` and `batch` prepare dedicated, commit-bound worktrees and invoke their
own commands with explicit working directories and environments. Keep the
prepared method, code, lockfile and environment unchanged. The origin's unrelated
dirty files are excluded; startup changes or a stale default method stop setup.
The command retains failed preparations and never chooses another destination
or revision automatically. After analysis children drain, new controllers
integrate complete publications serially through their pinned commands. The
recorded origin must be clean and on `main` at integration. Dirty origin,
competing publication or merge refusal preserves the accepted publication and
requires operator repair; do not stash, copy results or choose a conflict side.
Low-level `prepare` and `run` remain the publication-only route. If sandbox permissions block acquisition or setup,
request approval for the requested command, not a manual replacement lifecycle.

Keep the printed controller directory. Wait for the command to exit. SIGINT and
SIGTERM stop new claims and drain owned children; they are not immediate
cancellation. After abrupt interruption, reconcile with the same controller:

```bash
commonplace-analysis resume /absolute/controller
commonplace-analysis report /absolute/controller
```

Resume reconciles old effects before claiming pending targets. It does not
retry stopped analyses. After the operator resolves a recorded stop, explicitly
select its recorded normalized identity with `resume ... --target <identity>`.
The existing allocation, method and profile remain fixed. Resume reconciles
integration evidence without rerunning accepted analysis work. Existing
publication-only controllers keep that policy; resuming one does not grant
automatic integration authority. Unsettled workers, uncertain effects and
interrupted audits require operator attention; missing
PIDs do not prove descendants stopped. Never acknowledge, retry, reset or launch
a replacement on the command's convenience or an audit's authority. The
[command reference](../../../reference/commands.md#commonplace-analysis) describes
separately authorized low-level recovery.

## Advisory trace audit

The command reports the saved advisory audit separately from analysis acceptance.
Read a completed report at its recorded evidence path and report material
findings and coverage limits. A failed or skipped audit does not invalidate a
completed receipt; no findings is not a correctness certificate. An interrupted
audit requires process/descendant settlement review, not an automatic relaunch.
Audit evidence is local state, not included by integration.

## Report and separately commissioned work

Return the controller JSON unchanged with its exit status and a short summary:
publication and integration versus local completion, stopped or
operator-attention targets, method/profile/source bindings, run/worktree and
evidence paths, advisory audit outcome and limits. For new automatic controllers,
exit 0 means every target integrated or completed locally without a publication.
Legacy publication-only controllers retain their recorded success policy.
Exit 2 means ordinary recorded stops; 1 means command/preparation failure;
3 means pending work, unintegrated publication, interruption or operator attention. Never call a stopped target
successful. `report` reads saved orchestration state; `resume` reconciles it
against pinned-child records. Use the command's recorded checks rather than
adding immediate independent checksum sweeps. Investigate a specific failure,
changed input or recovery uncertainty when it gives a reason to distrust them.

After integration, say that comparisons are stale unless rebuilt under separate
authority and a prior landscape synthesis is historical unless refreshed. Do
not perform either as part of this run.

Cleanup remains separately authorized. For manual integration of an existing
publication, obtain authorization and read [publication](../publish-analysis.md);
call the prepared worktree's `commonplace-analysis integrate <run>` from that
worktree, with `--model <model-id>` for an agent commit. Never copy outputs into
`main`. Do not retrofit new integration code or authority into an old run.
Worktree removal requires every publication integrated, no unresolved integration
branch, and useful audit evidence extracted or the operator's explicit decision
that none needs retention. Failed worktrees and local non-complete results need
separate disposition decisions. Nothing removes them automatically.

Before editing this method, read [method maintenance](../maintain-analysis-method.md).
