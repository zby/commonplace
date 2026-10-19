# Rerun the previously analysed agentic systems

**Current publication checkpoint: 182 canonical sets / 2,366 members.**
The [batches 21–22 commission](./batch21-22-commission.md) is audited and reconciled: **13 exact publications, nine content-positive audit recommendations and four audit holds**. Parent review sealed **eight transfer approvals** and added one source-selection/scope stop for the conceptual Ontology account. **Zero integrations:** the ordinary native command refused the three unrelated untracked source ingests in origin; they remain untouched. [Results and exact blockers](./batch21-22-results.md), [guarded integration evidence](./batch21-22-integration.json) and the [complete 25-target remainder](./batch21-22-remainder.md) retain all outcomes. All twelve fresh audits are complete and parent-read; the unchanged Supermemory hold was reused by exact hash. The fixed inventory remains **181 complete, 21 pending and four older target holds**; Talorys is outside its 206 targets. Previous batch-20 and older holds remain preserved.

[Batch 21](./batch-21.md)'s nine fresh selections produced **two exact publications, one failed run, one interrupted run and five preparation refusals**. Supermemory remains semantically held; ModularRSI is approved but not integrated. ContextPilot stopped on a workflow input defect; OpenRSI still has reconciliation open without publication. [Exact outcomes](./batch21-22-outcomes.md) preserve all logs and worktrees. The [preparation manifest](./batch-21-fresh.json) is historical; the operator-edited [script](./bash-21.sh) is now a launcher that skips existing evidence, not the old read-only checker. Do not run it as recovery or replay it under this audit commission.

The [original 25-case narrative](./batch-21-original.md), [machine record](./batch-21.json), [original checker](./bash-21-original.sh), [nine correction packets](./batch-21-corrections/README.md), [decision brief](./batch-21-decisions.md) and [compatibility review](./batch-21-compatibility-review.md) remain historical preparation. The reset-helper guard stays unchanged; reset bridge tests, old budget renewal and same-run writer clearance are no longer admission requirements for the fresh route. Do not launch the superseded correction helper or take over old workspaces. Exclusive ownership is required only for new disjoint destinations; old runs, holds and unknown collateral effects remain preserved.

[Batch 22](./batch-22.md)'s thirteen targets produced **eleven exact publications and two completed local source stops** (Awesome Agent Memory out-of-scope; Letta blocked), not thirteen publications. Its eight earlier attempts are separately retained: six preparation refusals and two interruptions before settled tool execution. Fresh ACE, Fragility Grid and Sift-KG publications are operationally held; the [Ontology scope decision](./batch21-22-ontology-scope-stop.md) is also unresolved. The [operator-edited script](./bash-22.sh) now selects fresh retry suffixes and is not the historical read-only checker. Do not replay it under this commission. The [earlier execution route](./batch-22-execution.md) retains its source-selection contract, not fresh execution authority. DualGraph and Fintool remain deferred; Agentic Harness Engineering remains separately gated. Historical [profile alignment](./profile-coverage-alignment.md) and all old incident evidence remain unchanged.

The historical fixed 169-publication sweep and [reviewed results](./publication-audit-current-results.md) remain unchanged as evidence. Dated batch sections retain their historical scope and then-current status; they are not fresh launch authority.

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

## Completed fixed publication sweep

The [current commission](./publication-audit-current-commission.md) expands intake
to all own completed worktree publications, including completed batch-18 results.
The [fixed inventory](./publication-audit-current-intake.md) contains 169 live
publications with exact effect/manifest binding; active and unpublished runs
remain excluded. The [assignment ledger](./publication-audit-current-ledger.json)
tracks 43 new/unbound cases plus a supplemental Agemem audit commissioned for
an intake lookup/binding gap; an existing batch-03 audit was later rediscovered.
The [reviewed results](./publication-audit-current-results.md) and
[integration ledger](./publication-audit-current-integration.json) account for
all 169: **138 integrated, six positive incumbent alternatives and 25 holds**.
All 44 fresh substantive audits are complete and parent-read. After committing
the [sealed decisions](./publication-audit-current-decisions.json), all **40 new
transfers** completed through the ordinary guarded route. **175 canonical sets**
now retain all 135 previous sets and root `.gitignore` byte-identically. The 520
new member files retain accepted own-publication bytes; 31 legacy destinations
moved separately to owner-qualified names. The fixed checklist has **174 complete,
28 pending and four older target holds**; Talorys is integrated outside its 206
targets. The [checklist reconciliation](./publication-audit-current-checklist.json)
binds 39 supported target completions without inventing a Talorys/PAL match.
All workers of this sweep have finished. Deep holds go to batch 19; local faults
and separate operational stops go to the [reset-and-rework list](./reset-and-rework.md).
No reset or recovery launch is implied. Historical checkpoints retain their
then-current counts and scope; use the reviewed results before resuming work.

## Batch 19: depth-aware recovery preparation

After [qualified AI Memex integration and the Supermemory re-entry check](./reentry-pilots.md),
the operator requested [batch 19](./batch-19.md) and a check of where the other
held accounts first went wrong. The [completed investigation](./batch-19-depth-results.md)
covers the original 23 held runs, with all four independent reports parent-reviewed.
The later deep/local split leaves six selected deep recoveries and eleven blocked
deep cases. AREX moves to local rework; mixed cases retain independent profile
repairs. The operator subsequently authorized execution after batch 20 preparation;
the six-run launcher finished internally with six completed publications.
All six renewed publications remain held after the new independent audits. The [depth commission](./batch-19-depth-commission.md)
and [ledger](./batch-19.json) preserve their original scope and assignments;
the separate publication sweep now includes completed batch-18 results and the
previous unaudited queue. The 135-set pre-transfer baseline is preserved within
the then-current **175-set** canonical corpus, now preserved within 182 sets. Content depth, incumbent-transfer stops and operational
violations remain separate decisions.
The operator-run [batch-19 launcher](./bash-19.sh) has finished. Its default
`--check` was read-only. The authorized launch used this command; **do not replay
it against the now-existing batch logs**:

```bash
bash kb/work/agentic-system-reruns/bash-19.sh --confirm-idle
```

It resets the six existing runs sequentially, starting with Supermemory, then
uses their ordinary frozen drivers without audit feedback. It stops on failures
and refuses existing batch logs. Nothing was reset or launched while preparing
it. The operator then explicitly requested its launch. External
`outputs/batch-19-launch.log` and `outputs/batch-19/` retain progress and evidence;
the [ledger](./batch-19.json) records launch ownership. Renewed results remain
held for independent audit, and integration stays separate.

## Batch 20: ordinary fresh reruns

The operator ran [script 20](./bash-20.sh), following its [plan](./batch-20.md),
for nine fresh starts: Academic Research Skills, three remaining LLM Wiki owners,
ClawVault, Cortex, PAL, Semantic Engine and Memori. The invocation was:

```bash
bash kb/work/agentic-system-reruns/bash-20.sh
```

The [batch-18 reconciliation](./batch-20-reconciliation.json) found seven stopped
opening attempts with inherited naming mismatches, plus ClawVault's pre-creation
storage check stop. None of those predecessor attempts had a publication to
audit instead of scheduling a fresh run. The completed batch-20 publications
are covered by the new audit below. The script validates the committed inherited corpus and pins all preparations to
that launch-time commit. It uses new external worktrees and preserves old runs.
Four targets keep their authorized historical local source pins. No reset,
old-run recovery or integration occurs. Do not restart batch 18 concurrently.
The separate batch-19 six-run recovery selection is unchanged.

## Independent audit of batches 19 and 20

The operator ran batch 20 separately; all nine fresh runs published internally.
The [new audit commission](./batches-19-20-audit-commission.md) covers those nine
and the six renewed batch-19 publications. The [fixed intake](./batches-19-20-audit-intake.md)
found all 15 outside the then-current 175-set canonical corpus. The
[assignment ledger](./batches-19-20-audit-ledger.json) records isolated single-case
Sol/medium audits and complete parent review. The
[completed results](./batches-19-20-audit-results.md) are **seven qualified positive
recommendations and eight holds**: all six batch-19 renewals remain held; batch 20
had seven positives and two holds. The audit itself preserved all 175 canonical sets unchanged and authorized no integration, reset, source mutation or checklist acceptance change. The operator subsequently authorized only the seven positive transfers; see below.

## Seven transfers and batch 21

The [integration commission](./batches-19-20-integration-commission.md), approvals and complete audit evidence were committed before transfer. Seven ordinary prepared integration commands added 91 exact files, with clean-origin and source/method/incumbent guards before each effect. [The ledger](./batches-19-20-integration.json) binds successful transfers, preservation proofs and the helper-only preflight failure, which was preserved and reconciled before a separate successful attempt. Fourteen per-publication checks and one full-corpus check passed, with zero failures/warnings and the same 208 unavailable-source notices across 37 old sets, none new.

The [batch-21 record](./batch-21.json) binds every incomplete inventory target, native run/preparation and attempt snapshots, and sixteen held own publication maps. [The plan](./batch-21.md) separates actual current repair loci from old reset selections and preserves source, refusal, ownership and operational decisions. Check it read-only:

```bash
bash kb/work/agentic-system-reruns/bash-21.sh --check
```

There is no launch mode and no batch-21 analysis has started. A later explicit decision must release the applicable repair/source/ownership route and revalidate current evidence; a successful check does not prove writer idleness or transfer ownership.

The [independent preparation review](./audits/batch-21-preparation-review.md) established no consequential defect. The [parent verification record](./batch-21-preparation-checks.json) binds twenty read-only checker scenarios, 96 selected general/tooling tests and final Markdown/native-map checks. The parent's post-review change only clarifies historical scheduling wording and updates that navigation input's binding; no target, repair scope or gate changed.

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
