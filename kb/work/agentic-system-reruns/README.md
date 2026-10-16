# Rerun the previously analysed agentic systems

## Commission and current approach

The operator commissioned this workshop on 2026-10-12 to rerun previously
analysed systems through the current
[`analyse-agentic-system` skill](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md).
Produce fresh source-grounded analyses, not conversions of historical reviews.
The inventory contains 206 targets from 223 historical analysis records;
[systems](./systems.md) retains the inclusion references and outcomes.

On 2026-10-13, the operator replaced the outer model-driven rolling coordinator
with **ordinary Bash batches**. First test a single CLI analysis, then run four
scripts with ten systems each. Each script starts a fresh Pi session per system
and runs its ten analyses sequentially. Running all four scripts concurrently
allows four analyses at once, each with its standard internal analytical workers.
The single-system CLI test has not yet been confirmed successful.

No workshop takeover, queue-ownership claim, per-system reservation, rolling
handle map or additional scheduling coordinator is required. The scripts call
`/analyse-agentic-system <repository>`; the skill handles isolated preparation,
source acquisition, analytical rounds, checks and publication. Its source
isolation and stop conditions still apply. This changes outer scheduling, not
the analysis method or permission to modify frozen runs.

The motivation is to remove the accumulating outer coordinator conversation and
its context-capacity drain. Per-system coordinators still exist. Prompt-cache
expiration and provider pressure remain hypotheses, not established causes of
the failures. Bash launching does not guarantee lower request concurrency or
solve per-system context exhaustion.

## First Bash batch

The four scripts contain **40 distinct pending systems without a new retained
analysis in the origin or preserved analysis worktrees at selection time**:

- [bash-01.sh](./bash-01.sh): Agno AgentOS, Awesome Agent Memory, Claude Workstream
  Kit, ClawVault, Closure-SDK, Clude, LLM Wiki (cobusgreyling), CocoIndex, Cognee,
  Company Brain.
- [bash-02.sh](./bash-02.sh): Compound Engineering Plugin, Context Constitution,
  ContextPilot, Continuity, CORAL, Cortex, cq, CrewAI Memory, Decapod, deja-vu.
- [bash-03.sh](./bash-03.sh): dense-mem, DocMason, EAL-bench, Ecdysis, Echel,
  EchoesVault, EchoWiki, Eidetic, Eigenius, Engraph.
- [bash-04.sh](./bash-04.sh): Enoch, EQUIPA, EvoOntology, Exo, Exocomp, ExpeL,
  Funes, G-Memory, getsentry/skills, Gnosis.

Historical records were used only to resolve source identities. The scripts
forward repository URLs, not old findings. Held systems, older refresh-workshop
reservations, Academic Research Skills' unresolved source-exposure case and the
separate beads_rust CLI trial are excluded from this batch. This selection does
not mark targets as taken over or change checklist completion counts.

After the single-system CLI test, run from the repository root:

```bash
bash kb/work/agentic-system-reruns/bash-01.sh &
bash kb/work/agentic-system-reruns/bash-02.sh &
bash kb/work/agentic-system-reruns/bash-03.sh &
bash kb/work/agentic-system-reruns/bash-04.sh &
wait
```

Each script also works when invoked by path from another directory. It writes
combined JSON event output and stderr to
`kb/work/agentic-system-reruns/outputs/<system>.output`, one file per system.
These are raw process logs, not accepted analysis reports. A script skips an
existing output file rather than overwriting evidence. Do not run the same
batch twice concurrently; make new scripts after reviewing the previous batch.
A nonzero process exit does not stop subsequent independent systems.

The approval-gate removal must be committed before the CLI test: isolated
preparation uses a committed method and refuses changed startup files. Start a
fresh Pi process to load the new extension. Do not patch the preserved trial
worktrees or resume them implicitly.

## Second Bash batch

Prepared on 2026-10-14: another **40 distinct pending systems**, disjoint from
scripts 01–04 and without matching retained publications in the origin or
preserved worktrees at selection time. No held targets, older reservations or
failed-run recovery are included. Memori and OpenClerk already had separate
runs and output files at verification time; Letta also had a preserved run.
They were excluded to avoid duplicating existing work. The scripts use the same command, output
naming and sequential execution as the first batch.

- [bash-05.sh](./bash-05.sh): HALO, Hermes Agent, Hindsight, hyalo, HyperAgents,
  interview-doc-agent, KBLaM, kgai, Kompl, LACP.
- [bash-06.sh](./bash-06.sh): Playground, Link, llm-context-base, llm-project-wiki,
  llm-wiki-coordination, LLM-WIKI-MCP, LLM-Wiki-v3, llmwiki-marimo, Mem0, Memex.
- [bash-07.sh](./bash-07.sh): Pond, MemPalace, memwiki, MentisDB, Meta-Harness,
  MiroShark, nao, Nuggets, o-o, OKF Harness.
- [bash-08.sh](./bash-08.sh): Prime Agent, OpenSage, OpenViking, OpenWiki,
  Operational Ontology Framework, Origin, PageIndex, Pal, Phantom, pi-self-learning.

Run these scripts by the same `bash <path>` route. Starting all four while older
batches remain active increases the total number of simultaneous analyses.
Fresh Pi sessions use the committed subagent error-handling fix; existing
sessions and frozen worktrees retain their versions. No retry settings changed.

[Worktree publication audit inventory](./unaudited-publications.md) retains the
first batch's 19-publication snapshot separately from older experimental runs.
A subsequent operator commission [audited all 19](./audit-current-batch.md) and
integrated 18 with recorded limits; ContextPilot is held. This is not a live
inventory of later publications or a takeover list. No real analysis was launched
while preparing scripts 05–08.

## Clean residue batch

On 2026-10-14 the operator requested the untouched remainder, with nothing from
previous runs. The **76 eligible targets** are split across four sequential
scripts: [bash-09.sh](./bash-09.sh), [bash-10.sh](./bash-10.sh) and
[bash-11.sh](./bash-11.sh) have 20 runs each; [bash-12.sh](./bash-12.sh) has 16.
Together they cover 69 repositories and 7 explicitly identified document sources.
[Selection and exclusions](./residue-09.md) retain the snapshot checks. It excludes
all targets in scripts 01–08, separately attempted systems, holds, completions
and existing reservations. It contains no retry of ContextPilot or other previous
runs. Preparing the script did not launch it or change acceptance counts.

Scripts 09–10 subsequently stopped during the disk-full incident. Do not use
them as restart entry points. [Disk recovery batches](./disk-recovery-batches.md)
retarget unstarted scripts 11–12 to the external disk and add scripts 13–14 for
38 eligible zero-output targets. Three same-name wiki repositories are deferred
for the known publication-path collision. The six interrupted runs and earlier
nonempty failures remain outside these fresh batches.

## External logs and audit prompt

Scripts 11–14 write under
`/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/`, with separate
`batch-13/` and `batch-14/` subdirectories for new outputs. Complete the
operator-owned move and ensure directory write permission before execution.
The scripts refuse an unmounted disk; worktrees and other runtime storage still
use the primary filesystem. See [disk recovery batches](./disk-recovery-batches.md)
for selection and remaining disk risks.

[Audit-unintegrated prompt](./audit-unintegrated-prompt.md) supplies the requested
fresh-coordinator audit commission for all exact own-worktree publications not
integrated into main, including older alternatives. Creating it does not launch
auditors, authorize integration or clear existing holds.

## Fresh reruns for previous batch failures

The operator requested new batches on 2026-10-14 while scripts 11–14 were still
processing. [Failed-batch inventory and decisions](./failed-batch-reruns.md)
reconcile the 30 nonempty unpublished outcomes in scripts 01–10: 27 failures or
interruptions and three completed local results. Prepare **22 fresh analyses**:
[bash-15.sh](./bash-15.sh) has 16 stopped targets; [bash-16.sh](./bash-16.sh) has
six disk-full interruptions. Both use new external log subdirectories and leave
old worktrees, open attempts, partial outputs and logs unchanged.

Five failed targets remain deferred for source/access, source-isolation,
boundary or publication-namespace decisions. The three completed local outcomes,
all sources already assigned to scripts 11–14, retained publications and existing
holds/reservations are excluded. No analysis was launched during preparation.
Wait for the active four pipelines to finish and recheck ownership/publication
and disk capacity before running the new scripts. This authorizes fresh attempts,
not old-run recovery or a change to acceptance counts.

## Audited integration and expanded failure batch, 2026-10-15

The operator requested integration of the cleared analyses, a new batch for all
rerunnable failures, then continued audits of the 61 new publications.
[Integration evidence](./audit-integration-2026-10-15.md) records **32 unchanged
new-source integrations**, bringing the retained corpus to **70 sets**. Six
positive older alternatives were not substituted for incumbents; all 13
exact-run semantic holds remain held.

The [fresh-failure batch](./fresh-failure-batch-2026-10-15.md) comprises **39 fresh
starts** across scripts 15–17: retain 15–16's 22 targets and add
[bash-17.sh](./bash-17.sh) for 16 older provider failures plus o-o's prompt-path
failure. The new commission releases those 16 operational target holds for fresh
starts only, not recovery of preserved attempts. The [independent selection](./retry-selection-2026-10-15.md)
retains exact sources, failed runs and deferrals. Preparation did not launch
analyses; all three scripts use external worktrees and logs. A later
[read-only execution follow-up](./fresh-failure-batch-2026-10-15.md#observed-execution-follow-up)
at 08:49 UTC found scripts 15–17 running outside this coordinator's launches.
Do not start duplicates or treat process/output presence as acceptance. Recheck
ownership/publications and capacity before any further launch.

The [next audit commission](./audit-next-61-commission.md) fixes its 61-run intake
at the previous 2026-10-15 06:29 UTC status snapshot. Its
[separate inventory](./next-publication-audit-inventory.md) records verified byte
maps and completed fresh Sol/medium audits. **All 61 reports are reviewed:
55 recommendations to integrate with recorded limits, three semantic holds and
three operational holds.** The coordinator rechecked all 793 publication files
and validated 71 explicit Markdown targets without failures, warnings or notices.
No candidate from this pass was integrated. Later Synto, Sift-KG and fresh-batch
publications do not move its finish line. All audit assignments have finished;
new positive recommendations require separate integration authorization.

## Worktree storage

The operator approved external storage and verified completed-worktree cleanup.
[Storage record and restore procedure](./worktree-storage.md) retain the result:
**37 integrated worktrees archived externally and removed locally**, with an
original-path restore pilot; Agemem remains pending audit retention. Running,
unintegrated, failed and held worktrees were not removed. Primary-disk free space
increased from about 44 GiB to 51 GiB during the operation.

Unstarted scripts 15–16 now instruct fresh coordinators to prepare worktrees
under external `outputs/commonplace-worktrees/`, alongside but separate from
logs. Future inventories must include those external preparation records and
archived integration evidence. Failed/held cold-storage decisions return at the
finished-run checkpoint; they are not routine completed-worktree cleanup.

## Publication namespace follow-up after all runs finish

After the operator reported all batches finished, they authorized the
[owner-qualified migration](./publication-namespace-migration.md) on 2026-10-15.
It moves 66 GitHub publications to lowercase `owner--project` paths and updates
links and validators. All 910 files across 70 publication sets remain byte-identical;
run IDs and frozen worktrees are unchanged. Four document-source names stay as-is.
The record also states the integration limits for old prepared worktrees.

After the namespace change is implemented and committed, prepare fresh reruns
for the four deferred repositories: Pratiyush/llm-wiki, kenhuangus/llm-wiki,
nvk/llm-wiki and MehmetGoekce/llm-wiki. Keep cobusgreyling's existing publication
as its own source; do not replace it with another owner's wiki. Different log
keys alone do not resolve the publication collision. This migration authorizes
no rerun launch or release of outstanding audit holds.

## Batch 18 preparation after the finished-batch reconciliation

The operator reported all batches finished and requested one more batch.
[Reconciliation](./finished-batch-residue-2026-10-15.md) verified all 39 targets
in scripts 15–17 published, with 507 files matching their recorded hashes.
[Batch 18](./batch-18.md) prepares seventeen sources in [bash-18.sh](./bash-18.sh):
the four deferred wiki repositories, four historical pinned local sources,
Memori, OpenClerk, beads_rust and six operator-released older refresh targets.
It has not launched. The batch record also lists the ten unpublished targets still
outside this selection. Its naming preflight refuses
the current project-only slug before creating logs or worktrees. Implement and
commit the namespace migration above before execution; preparing this script
does not implement that migration or release other blockers.

## Resumed audit and integration after namespace migration

The [resumed commission](./audit-integration-current.md) excludes independently
running batch 18 and fixes 127 unintegrated candidates. The parent integrated
[55 previously cleared results](./integration-next61-cleared-2026-10-16.md),
then reviewed the first 13 of 46 later-publication audits and integrated their
[nine positive results](./integration-later-nine-2026-10-16.md). Origin now has
**134 retained sets**; all transferred bytes and existing publication maps were
preserved. Four new exact-run holds remain. The other **33 audits are planned,
not completed**, in the [live ledger](./audit-integration-later-46.json).
Older holds, canonical-incumbent alternatives and batch-18 ownership remain
unchanged. This is a resumable checkpoint, not audit-workshop closure.

## Audit all current worktree publications

The [current commission](./publication-audit-current-commission.md) expands intake
to all own completed worktree publications, including completed batch-18 results.
The [fixed inventory](./publication-audit-current-intake.md) contains 169 live
publications with exact effect/manifest binding; active and unpublished runs
remain excluded. The [assignment ledger](./publication-audit-current-ledger.json)
tracks 43 new/unbound cases plus a supplemental Agemem audit commissioned for
an intake lookup/binding gap; an existing batch-03 audit was later rediscovered.
The [reviewed results](./publication-audit-current-results.md) account for all
169: 98 already integrated, 40 newly approved transfers, six positive incumbent
alternatives and 25 holds. All 44 fresh substantive audits are complete and
parent-read; their [sealed decisions](./publication-audit-current-decisions.json)
retain exact report bindings. No audit worker remains active. Integration is
pending the evidence commit and ordinary guarded route. Deep holds go to batch
19; local faults and separate operational stops go to the [reset-and-rework list](./reset-and-rework.md).
No reset or recovery launch is implied. Historical checkpoints retain their
then-current counts and scope; use the reviewed results before resuming work.

## Batch 19: depth-aware recovery preparation

After [qualified AI Memex integration and the Supermemory re-entry check](./reentry-pilots.md),
the operator requested [batch 19](./batch-19.md) and a check of where the other
held accounts first went wrong. The [completed investigation](./batch-19-depth-results.md)
covers the original 23 held runs, with all four independent reports parent-reviewed.
The later deep/local split leaves six selected deep recoveries and eleven blocked
deep cases. AREX moves to local rework; mixed cases retain independent profile
repairs. No reset or recovery run has launched. The [depth commission](./batch-19-depth-commission.md)
and [ledger](./batch-19.json) preserve their original scope and assignments;
the separate publication sweep now includes completed batch-18 results and the
previous unaudited queue. The canonical baseline remains 135 sets before the
approved transfers. Content depth, incumbent-transfer stops and operational
violations remain separate decisions.
Preparation does not authorize reset or integration.

## After the processes finish

Inspect the output files and retained run/publication state. Make lists of:

- systems with a new publication, including its worktree and run;
- systems stopped, interrupted or without an established outcome;
- eligible systems still without a new analysis.

Generate the next Bash files from those lists. Do not infer success from a
process exit code, an output file's existence or a prepared worktree. JSON mode
can record an assistant error while returning process exit status zero. An
interrupted process is not proof that all its workers have stopped; check before
scheduling the same system again. Preserve logs, worktrees and partial evidence.
No automatic retry or recovery of held runs is included in these scripts.

Publication is separate from audited, integrated corpus completion. The Bash
scripts do not launch audits or integration, update comparisons, synthesize a
landscape, clean up worktrees or push. Separately commissioned acceptance uses
the existing [audit procedure](./audit-a-rerun.md) and standard integration
command, not copied publication files. Update completed checklist rows after
those checks, not when Pi exits.

## Retained limits and history

The checklist checkpoint is **70 complete, 132 pending, 4 older target holds** after
[32 new-source integrations](./audit-integration-2026-10-15.md) and the
[fresh-start release of 16 operational holds](./fresh-failure-batch-2026-10-15.md).
Four older target-level holds remain: ACE, Agentic Harness Engineering, Agent
Skills and ContextPilot. All 13 exact-run semantic audit holds remain, including
alternatives for sources with integrated incumbents. [Current-batch audits](./audit-current-batch.md),
[Claude Context Guard integration](./claude-context-guard-integration.md) and
[rolling execution 09](./rolling-09.md) retain earlier checkpoints. These are
acceptance counts, not a live Bash-batch status. Exact-run audit holds and the
next-61 pass's new dispositions are tracked in their audit inventories rather
than silently changing this checkpoint. The checklist retains older holds,
historical stops and unblock conditions.
CLI trial failures are not included in these counts. Claude Context Guard's
coordinator failure and missing worker traces remain preserved as evidence;
operator-authorized integration does not certify unavailable worker compliance.

Older [agentic-memory-refresh](../agentic-memory-refresh/README.md) reservations
remain excluded: Agent-S, MemoryOS, Basic Memory, OS-Copilot, A-mem and HippoRAG.
This new scheduling approach does not release another operator's work or grant
recovery authority for held targets.

The [archived log](./archived-log.md), batch records and rolling records retain
previous execution history. Their outer scheduling, ownership and startup
procedures are superseded by this commission, not additional Bash startup gates.
The [validation-path maintenance](./validation-path-maintenance.md) is resolved;
reopen it only for contradictory new evidence, under separate maintenance
scope. Missing worker traces remain missing evidence, not certified compliance.

## Closure

The workshop closes when each included target has an audited, integrated analysis
or an explicit operator-approved exclusion, and no analysis remains running.
Extract durable operational lessons before removing this workshop. Partial
batch execution and failures remain useful evidence but are not completed corpus
coverage.
