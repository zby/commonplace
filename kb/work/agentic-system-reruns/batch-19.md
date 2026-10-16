# Batch 19: restart held analyses at the faulty stage

## Commission and status

The operator requested batch 19 after the Supermemory re-entry trial, then asked
to check how deep the errors in the other held publications go. This prepares a
recovery batch and investigates restart depth; **it does not launch analyses,
reset runs, correct accepted outputs, waive holds or integrate publications**.
The first selected target is Supermemory, restarting its analytical chain from
`runtime`. Source acquisition and the frozen boundary remain unchanged.

The [batch ledger](./batch-19.json) owns selection and assignment status.
The [completed depth investigation](./batch-19-depth-results.md) covers 23 held
runs and supports seven selected recoveries. Four isolated reports covering the
other 22 runs are complete and parent-reviewed; no worker remains active.
Only a parent-reviewed depth finding can support another selection. If a case
needs a different source boundary, an unavailable source, incumbent replacement,
reserved-owner coordination or disposition of an authority violation, retain
that decision rather than automatically scheduling it.
Batch 18's seventeen identities and worktrees are outside this commission.
The 33 unaudited later publications are a separate queue, not known errors.

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
| 6 | AREX-Skill | `1871063034b5` | `report-verification` |
| 7 | Autogenesis | `9bcfa57fd7c1` | `boundary` |

The immutable intake named by the ledger resolves each exact run, worktree,
command directory and frozen source/method identity. All seven current
publications match their own completed effects, have no open attempts, and have
no canonical incumbent in the current 135-set boundary-identity scan. These
point-in-time checks do not authorize skipping launch preflight.

ContextPilot and Autogenesis have misleading boundary **narratives**, not a need
to fetch different source evidence. Regenerate those documents and their
analytical dependents while keeping opening/acquisition and source identity,
revision, method and run identity. Independent rechecking must inspect the new
functional scope as well as the repaired narrative. All other selected runs
retain boundary. AREX retains its useful records and reopens the verifier's own
assessment; do not force a positive conclusion through a special handoff.

The other sixteen cases are explicitly excluded: eleven incumbent alternatives,
four operational-only holds and reserved Agent Skills. Their depth findings and
separate decisions remain in the completed investigation; no hold is waived.

## Execution boundary for the future launch

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

No `bash-19.sh` is provided: this batch is a selected-job reset queue for existing
runs, not the fresh-run launch pattern of batches 15–18. A shell launcher must
not invoke an agent CLI in place of harness worker delegation.
