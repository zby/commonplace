# Fresh reruns for failed Bash-batch analyses

## Commission and decision

On 2026-10-14 the operator requested new batches for analyses that failed in previous batches, while four batches were still processing. This prepares scripts only. It does not launch analyses, resume old runs, repair engine state, release existing audit holds, integrate publications or change completion counts.

**Prepare 22 fresh analyses:** [bash-15.sh](./bash-15.sh) contains 16 stopped runs; [bash-16.sh](./bash-16.sh) contains six disk-full interruptions. Retain all old worktrees, partial outputs, failed attempts and logs. Five other failed targets require a source, isolation, boundary or namespace decision before scheduling. Three completed local outcomes are not process failures and are also excluded.

This selection covers Bash scripts 01–10, not a blanket release of earlier rolling-workshop holds or separate CLI trials. The operator's request permits fresh isolated attempts for the selected targets, not recovery of their old attempts. Dense-mem's earlier unauthorized metadata write remains unresolved and preserved; the new analysis must start in a different prepared worktree and may not repair that file.

## Inventory boundary and evidence

Selection snapshot: **2026-10-14T19:08:51Z**, origin HEAD `a568c6dc4`. Sources were taken from the existing batch scripts, not inferred from historical analysis findings. Enumerated sibling preparation records and own-token run directories; read each run's parameters, attempt records and publication-effect presence. Copied/inherited runs did not establish own publication. Completed retained publications were excluded even when absent from origin main.

For the 120 targets in scripts 01–10, the source-matched inventory found:

| Outcome at selection | Count | Scheduling disposition |
|---|---:|---|
| Own retained publication | 54 | Exclude; publication is not audited/integrated completion. |
| Unpublished, already in scripts 11–14 | 33 | Exclude every source in those scripts, including not-yet-started entries. |
| Nonempty unpublished outcome | 30 | Inspect failed/open attempts and completed local dispositions below. |
| Zero-byte original output, not rescheduled | 3 | Known different-owner `llm-wiki` collisions; remain deferred. |

The 30 nonempty outcomes comprise **27 failures/interruption cases and three completed local results**. Of the 27, 22 are selected and five deferred. All 30 had discoverable own runs; no missing-run outcome was silently classified as failure or success.

Original logs are at `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/<output-key>.output`. The selected old run root is `W/kb/agentic-system-analyses/state/<run-id>`. Here `W` is `/home/zby/llm/commonplace/.commonplace/worktrees/<source-slug>-<token>`, with the slug and token from the run ID. The sibling `<worktree>.preparation.json` binds its environment. Exception for the deferred Fintool run: `W` is `fintool-e109159e0559`, not its numeric source slug. Failed reasons below come from `state/attempts/<attempt>.json`; bounded log tails corroborated stopped/local outcomes or visibly truncated stream endings. No state-writing inspect command or huge-log copy was used.

Process checks found the four active pipelines to be scripts 11–14. No selected old worktree path/token matched a live same-user process command or readable cwd. Four unreadable cwd entries belonged to systemd, sd-pam, ssh-agent and a Bun web server, not identified analysis workers. This is a point-in-time ownership check, not a permanent lock or exhaustive worker-compliance claim. Open attempts in six old runs are retained logical state, not evidence that those workers still run. Recheck ownership before executing if another operator resumes or reschedules them.

## Batch 15: stopped analyses

Fourteen targets have the exact failed-attempt reason `OpenAI Responses stream ended before a terminal response event`. EchoesVault reports the API 503 shown below. Dense-mem reports a write-scope violation rather than a provider error. Later completed sibling jobs do not erase an earlier failed job.

| Output key | Original batch | Exact previous run | Failed attempt / cause |
|---|---:|---|---|
| claude-workstream-kit | 01 | `AAS-2026-10-13-claude-workstream-kit-12b5b9198bf7-01` | `000008-epistemic`; terminal stream missing |
| cludebot | 01 | `AAS-2026-10-14-cludebot-ac0108386612-01` | `000019-reconciliation`; terminal stream missing |
| cocoindex | 01 | `AAS-2026-10-14-cocoindex-2ecd2052d8c0-01` | `000022-report-verification`; terminal stream missing |
| context-constitution | 02 | `AAS-2026-10-13-context-constitution-8157ef4d6366-01` | `000008-epistemic`; terminal stream missing |
| coral | 02 | `AAS-2026-10-14-coral-99830583a327-01` | `000032-report-verification`; terminal stream missing |
| crewai-memory | 02 | `AAS-2026-10-14-crewai-80a0dcde153b-01` | `000022-report-verification`; terminal stream missing |
| dense-mem | 03 | `AAS-2026-10-13-dense-mem-720113385baf-01` | `000007-memory`; unauthorized run-root `worker-identity.json` write; prior contents unknown; no memory report |
| eal-bench | 03 | `AAS-2026-10-13-eal-bench-73e273c04742-01` | `000019-reconciliation`; terminal stream missing |
| echel | 03 | `AAS-2026-10-14-echel-2b34ae0df7c8-01` | `000044-synthesis-verification`; terminal stream missing |
| echoes-vault-opencode | 03 | `AAS-2026-10-14-echoes-vault-opencode-eedd273a23d2-01` | `000024-runtime`; API 503 |
| eigenius | 03 | `AAS-2026-10-14-eigenius-0f032bc7781a-01` | `000034-memory-profile`; terminal stream missing |
| equipa | 04 | `AAS-2026-10-13-equipa-1a6691b447ef-01` | `000005-runtime`; terminal stream missing |
| exo | 04 | `AAS-2026-10-14-exo-d97f08ac25c6-01` | `000007-memory`; terminal stream missing |
| funes | 04 | `AAS-2026-10-14-funes-3dbc3618accb-01` | `000032-report-verification`; terminal stream missing |
| g-memory | 04 | `AAS-2026-10-14-gmemory-f68cd70c7b02-01` | `000005-runtime`; terminal stream missing |
| gnosis | 04 | `AAS-2026-10-14-gnosis-0c7b2f042457-01` | `000007-memory`; terminal stream missing |

EchoesVault's retained reason is:

```text
OpenAI API error (503): 503 upstream connect error or disconnect/reset before headers. retried and the latest reset reason: remote connection failure, transport failure reason: delayed connect error: Connection refused
```

The new script does not retry an old worker or assert these failures are fixed. It asks for a new source-first analysis under the committed method selected by normal preparation at execution time. Source acquisition may select a newer upstream revision; this is not a same-revision experimental replication. No prior findings, accepted reports or failure-derived substantive guidance are sent to analytical jobs.

## Batch 16: disk-full interruptions

These six retain open attempts and truncated logs from the [disk-full incident](./disk-recovery-batches.md). Preserve their state exactly; fresh preparation is not an `advance`, attempt closure, orphan recovery or permission to remove their evidence.

| Output key | Original batch | Exact previous run | Retained open attempts |
|---|---:|---|---|
| kblam | 05 | `AAS-2026-10-14-kblam-d3f74e1e83d1-01` | `000005-runtime` |
| llm-wiki-mcp | 06 | `AAS-2026-10-14-llm-wiki-mcp-5c8291a71578-01` | `000035-report-verification` |
| miroshark | 07 | `AAS-2026-10-14-miroshark-47b6fb7583ad-01` | `000028-memory-profile` |
| origin | 08 | `AAS-2026-10-14-origin-bc322d6fcabe-01` | `000007-memory`, `000008-epistemic`, `000009-workflow` |
| isaacclupus-mnemosyn-spec | 09 | `AAS-2026-10-14-isaacclupus-mnemosyn-spec-88936d915df6-01` | `000022-report-verification` |
| quicky-wiki | 10 | `AAS-2026-10-14-quicky-wiki-53f96249d08f-01` | `000030-synthesis-verification` |

None of these sources is in scripts 11–14 and none has an own retained publication at selection. Six interrupted coordinators do not establish six clean worker terminations; absence of currently matching processes is the additional scheduling evidence. Source-grounded work must be performed anew, not copied from their installed members.

## Deferred and excluded outcomes

These are not entries in either new script. No existing hold or ownership reservation is released.

| Output key / original batch | Exact previous run | Observed outcome | Required decision before another batch |
|---|---|---|---|
| clawvault / 01 | `AAS-2026-10-13-clawvault-d44ad402971c-01` | `000002-acquire` failed: `RuntimeError: git clone https://github.com/Versatly/clawvault failed: fatal: could not read Username for 'https://github.com': No such device or address` | Supply a confirmed accessible source or authorization for credentials/access; failure does not establish whether the repository is private, removed or renamed. No external probe made. |
| cortex / 02 | `AAS-2026-10-14-cortex-77df30205b93-01` | `000002-acquire` failed with the same Username error for `https://github.com/abbacusgroup/cortex` | Confirm source/access; do not substitute a similarly named repository. |
| fintool / 09 | `AAS-2026-10-14-2015174818497437834-e109159e0559-01` | `000003-boundary` reports exposure to third-party target characterizations in captured replies; no boundary produced | Establish an article-only source view without those replies and a fresh unexposed worker; preserve canonical source identity. Generic recapture alone does not establish isolation. |
| fragility-grid / 09 | `AAS-2026-10-14-fragility-grid-f011bbbfc307-01` | `000022-report-verification` reports material same-system launchers outside the selected boundary | Authorize inclusion of the same-grid launchers or an explicitly narrower target; generic rerun scheduling does not dispose of this boundary choice. |
| pratiyush--llm-wiki / 10 | `AAS-2026-10-14-llm-wiki-2180ef6533c6-01` | `000001-opening` failed: `ValueError: publication destination belongs to another source` | Resolve namespace/owner collision without replacing cobusgreyling's publication. A different log key is not a different publication slug. |
| awesome-agent-memory / 01 | `AAS-2026-10-13-awesome-agent-memory-ad0b4035706a-01` | Completed local `out-of-scope` result; no retained publication | Not a failed analysis. Reopen only under a supported scope/disposition decision. |
| operational-ontology-framework / 08 | `AAS-2026-10-14-operational-ontology-framework-c5cd99471671-01` | Completed local `out-of-scope` result; no retained publication | Not a failed analysis; no automatic reanalysis. |
| dualgraph / 09 | `AAS-2026-10-14-dki-llm-da75a840ca8d-01` | Completed local `blocked` result; coherent single-system boundary unestablished | Select the intended system within the supplied collection; do not silently substitute a subproject. |

The three zero-output, unscheduled sources remain deferred for the known `llm-wiki` collision: kenhuangus/llm-wiki, nvk/llm-wiki and MehmetGoekce/llm-wiki. Their status is unstarted/deferred, not failed. Existing [audit holds](./unintegrated-audit-inventory.md#held-runs-and-concrete-unblock-conditions), [earlier partial-outcome decisions](./partial-outcomes-2026-10-13.md) and older refresh reservations remain outside this selection.

## Execution boundary

The four active pipelines already consume the intended four-analysis concurrency. **Do not add these two pipelines while all four remain active.** After scripts 11–14 finish, recheck that selected targets have not acquired new publications or owners, that no new same-source run is active, and that both disks have capacity. At preparation, the primary disk had about 45 GB free and the external disk about 769 GB. Worktrees, source checkouts, Pi sessions and temporary files still use the primary disk.

Then the operator can run either script alone or both concurrently:

```bash
bash kb/work/agentic-system-reruns/bash-15.sh &
bash kb/work/agentic-system-reruns/bash-16.sh &
wait
```

Each script runs its own entries sequentially using Sol/medium and the standard analysis skill. Following the operator's storage approval, fresh coordinators are instructed to prepare worktrees at external `outputs/commonplace-worktrees/batch-<number>-<output-key>` using the existing `--worktree` option, then use the returned local commands. Existing external worktrees/preparation records are skipped, not resumed; this was checked with mock launchers, not a real analysis. See [storage and restoration](./worktree-storage.md) for archive locations and future enumeration boundaries. New logs go to external `outputs/batch-15/` and `outputs/batch-16/`, not the original filenames. Mount/write checks and noclobber/existing-output guards preserve evidence. Scripts never fall back to primary-disk logs. Do not restart an old script or remove a new output to make it rerun; review the resulting exact run first. Process exit, output presence and prepared worktrees are not analysis verdicts. A later failure stops that analysis under the skill's rules; independent later entries may still run. No automatic worker retries, publication correction, integration, cleanup or comparison refresh is introduced.

## Verification

Selection checks establish 22 unique sources/output keys, exact agreement with original source locators, no overlap with scripts 11–14, no own publication for each selected source, and matching failed/open attempt evidence. All original evidence remains untouched. No real Pi analysis or auditor was launched to test these scripts; fake launchers exercised shell behavior only.

- `bash -n` passed for scripts 15–16.
- Selection assertions passed for 22 unique sources/output keys, 16/6 partition, exact original source locators, no overlap with scripts 11–14, no own publication and a failed/open attempt in every selected run.
- Temporary mock-only runs passed: exact Sol/medium CLI arguments; sequential continuation after a mocked exit 7; repeat skips with unchanged log hashes; initial and mid-pipeline unmount stops; invocation from outside the repository. No mock used the real external output directory or real Pi executable.
- `commonplace-validate` passed for this record and the changed README, each with zero failures or warnings.
- `uv run pytest tests/commonplace/general tests/commonplace/agentic_analysis`: **469 passed, 96 deselected** by the default marker filter, in 52.36 seconds. No production engine, method, dependency or relevant slow-test behavior changed; this is selected coverage, not the complete suite.

Preparing these scripts changes no target outcome, publication, source capture, existing process, log location, mount state or permissions. Broader workshop-link discovery, if wanted, is a separate `cp-skill-connect` task.
