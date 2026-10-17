# Batch 19: restart held analyses at the faulty stage

## Commission and status

The operator requested batch 19 after the Supermemory re-entry trial, then asked
to check how deep the errors in the other held publications go. After the
publication audit and integrations, the operator requested a runnable batch:
**the operator will launch it**, while work on the other cases stays separate.
The [launcher](./bash-19.sh) is prepared but has not been executed beyond its
read-only check. No run was reset or launched while creating it. It selects only
the six recoveries below, without waiving holds or authorizing integration.
Supermemory is first, restarting from `runtime`; its source acquisition and
frozen boundary remain unchanged.

The [batch ledger](./batch-19.json) owns selection and assignment status.
The [completed depth investigation](./batch-19-depth-results.md) covers 23 held
runs and initially supported seven selected recoveries. Under the subsequent
[all-publication audit commission](./publication-audit-current-commission.md),
AREX moves to the [local reset-and-rework list](./reset-and-rework.md), leaving
six selected deep recoveries. Eleven other deep cases are recorded here as
**blocked**, not selected for incumbent replacement or reserved work. The four
baseline depth reports are complete and parent-reviewed. New sweep findings
extend these lists only after complete review.

A different source boundary, unavailable source, incumbent replacement,
reserved-owner coordination or authority violation remains an explicit decision,
not automatic scheduling permission. Completed batch-18 results were handled by
the separate publication sweep; excluded active/unpublished runs remain untouched.
Unreviewed results are not presumed erroneous or selected for recovery.

## First selected target: Supermemory

- Run: `AAS-2026-10-15-supermemory-ae21530d128d-01`.
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/supermemory-ae21530d128d`.
- Run directory: that worktree's `kb/agentic-system-analyses/state/AAS-2026-10-15-supermemory-ae21530d128d-01`.
- Command directory: that worktree's `.venv/bin`.
- Method: `a568c6dc489ad546374536b642c3889ce23149a8`.
- Source: `https://github.com/supermemoryai/supermemory`, revision
  `5323f427d076c7a158a9154867d293b53acc3841`.
- Selected reset job: **`runtime`**. This means the whole analytical chain,
  not a fresh acquisition or a new run identity.
- Existing hold: [renewed-publication audit](./audits/next-publications/AAS-2026-10-15-supermemory-ae21530d128d-01-reentry.md).

Parent read-only tracing found the overbroad capture account already in runtime
attempt `000005`; memory `000007` repeats it, and report verification `000022`
accepts it. The original source-read trace at
`/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/supermemory.output`,
JSONL lines 929 and 2400, has successful paired middleware reads for both the
runtime author and report verifier. Both returned the generic string-content
branch and the later option-gated structured branches. This establishes source
availability, not either worker's reasoning or compliance with every obligation.
Valid typed-SDK reachability remains unestablished; no disclosure is claimed.

Read-only dependency calculation gives 29 current attempts in the `runtime`
reset closure. It includes all lens reports, reconciliation, verification,
profile, synthesis and publication, while retaining opening, acquisition and
boundary. By comparison, `report-verification` would retire 12 current attempts
and test independent detection against the original reports. Counts are a
checkpoint, not permission to skip a new preflight.

## Selected restart depths

| Order | Target | Existing run token | Reset from |
| --- | --- | --- | --- |
| 1 | Supermemory | `ae21530d128d` | `runtime` |
| 2 | ContextPilot | `30d0d09e6cdc` | `boundary` |
| 3 | OpenRSI | `c72dec9967a3` | `runtime` |
| 4 | ModularRSI | `96b89989168e` | `runtime` |
| 5 | JAZ | `a94bea79c61a` | `runtime` |
| 6 | Autogenesis | `9bcfa57fd7c1` | `boundary` |

The immutable intake named by the ledger resolves each exact run, worktree,
command directory and frozen source/method identity. The initial seven
publications matched their own completed effects, had no open attempts, and had
no canonical incumbent in the then-current 135-set boundary-identity scan. These
point-in-time checks do not authorize skipping launch preflight.

ContextPilot and Autogenesis have misleading boundary **narratives**, not a need
to fetch different source evidence. Regenerate those documents and their
analytical dependents while keeping opening/acquisition and source identity,
revision, method and run identity. Independent rechecking must inspect the new
functional scope as well as the repaired narrative. All other selected runs
retain boundary. AREX retains its useful records and reopens the verifier's own
assessment through the separate local-rework list; do not force a positive
conclusion through a special handoff.

The ledger retains eleven blocked deep cases: ten incumbent alternatives and
reserved Agent Skills. Their per-fault depths remain in the completed
investigation. GBrain's incumbent alternative and AREX are local rework instead.
The four original operational-only holds and two added by the current sweep
require the separate operational dispositions in the local-list companion, not
automatic content restarts. No hold is waived by appearing in either list.

## Operator launch

From the origin checkout:

```bash
# Default action: read-only identity, source, effect and dependency checks.
bash kb/work/agentic-system-reruns/bash-19.sh --check

# Run only after confirming no prior coordinator/worker can write these six runs.
bash kb/work/agentic-system-reruns/bash-19.sh --confirm-idle
```

The second command resets and runs **one case at a time**, in table order. It
checks all six before the first reset and repeats each case's checks immediately
before its reset. It calls the existing current `reset_run(run, job)` API from
the origin without changing the historical worktree's environment. The only
reset inputs are the existing run and selected job. A fresh ordinary Pi
coordinator then starts in that worktree, with only its run, prepared command
directory and frozen driver in the prompt. Audit findings and this plan are not
passed into that workflow. Workers must still launch through the harness tool.
The coordinator performs its required worker-launch diagnostic before advancing;
`--check` does not test runtime delegation or certify that future launch succeeds.

The launcher keeps reset code/dependency files fixed to their `ce0715a08` bytes.
Do not change those files or environments while it runs. Unrelated workshop
bookkeeping may continue. Stop if any selected run gains another writer or a
canonical incumbent; never run two launchers against these runs.

Logs go to the new external directory:

```text
/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-19/
```

It retains the initial preflight, per-run reset reports/errors, coordinator JSONL
and exit codes, and final prepared-command inspection output/errors. The reset
report names the complete `.reset-history` archive, including the withdrawn old
publication. An existing batch directory is a hard stop, not permission to
skip cases, overwrite logs or reset again. Preserve it after interruption and
reconcile the actual state before any separately authorized continuation.

A nonzero command/coordinator exit or an incomplete/unbound final publication
stops the batch before the next case. There is no automatic coordinator restart,
transient-failure retry authorization, operator advance loop, source acquisition,
new run allocation or integration. Internally completed results stay **held**
for independent archived-versus-new comparison; process success is not correction.

## Execution boundary

Before an authorized launch, recheck ownership, method/source identities, source
cleanliness, publication/effect bytes, open attempts, uncertain effects and
canonical incumbents. Stop on an unexplained mismatch or live same-run writer.
Never modify the frozen method, source or environment to enable recovery.

Use the existing external active-state reset mechanism. Historical worktrees
that predate the reset CLI can use the same current `reset_run()` Python API
used by the pilots; no new cross-checkout entry point or manual state edit is
introduced. Preserve the complete reset archive and exact old publication for
debugging and subsequent comparison. Reset inputs are only the run and selected
job, not this investigation's findings.

After reset, hand an ordinary fresh coordinator only its run, prepared command
directory and existing driver. Do not send this plan, old reviews, audit findings
or special re-entry instructions to the analytical workers. Follow the standard
step program, not a new resume command or operator advance loop. Renew the
worker-launch diagnostic before a launch after reload. Stop on unhandled
execution failure or uncertain effects; preparation is not authority for retries.

Keep the renewed result held until a separate independent exact-byte comparison
checks the archived and new publications, consequential historical differences
against the frozen source, and manifest/effect binding. Completion is not proof
of correction, worker compliance, target execution or operational benefit.
Integration and owner-qualified publication migration remain separate.

Unlike batches 15–18, `bash-19.sh` never invokes the fresh-analysis skill to
prepare or open a replacement run. Its operator-run Pi processes are whole
coordinators; their analytical workers still require harness-tool delegation,
not Bash agent-CLI substitutes.

## Preparation checks

- Bash syntax and embedded Python compilation passed; invalid options are refused.
- All six real `--check` preflights passed without resets or launches.
- All six exact prepared `inspect` commands and the launcher's completion/map
  gate passed against their **old publications**. This checks interface binding,
  not future execution or correction; no renewed publication was produced.
- `uv run pytest tests/commonplace/general tests/commonplace/artifactrun tests/commonplace/agentic_analysis -m ''`:
  **926 passed**, including slow tests in these directories. No complete-repository
  test-suite or target-system execution claim follows.

The actual reset/launch path has deliberately not been exercised on these live
runs. Runtime delegation, new worker behavior and content repair remain untested
until the operator launches and an independent audit checks the results.
