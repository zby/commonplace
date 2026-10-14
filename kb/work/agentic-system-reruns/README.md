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
previous runs. [bash-09.sh](./bash-09.sh) contains **76 eligible targets** in one
sequential script: 69 repositories and 7 explicitly identified document sources.
[Selection and exclusions](./residue-09.md) retain the snapshot checks. It excludes
all targets in scripts 01–08, separately attempted systems, holds, completions
and existing reservations. It contains no retry of ContextPilot or other previous
runs. Preparing the script did not launch it or change acceptance counts.

Run with `bash kb/work/agentic-system-reruns/bash-09.sh` when desired. Running it
alongside existing scripts adds another analysis pipeline; it does not reduce the
recent overload pressure. Recheck the selection if other work starts before it.

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

Audited/integrated progress is **38 complete, 148 pending, 20 held** after
[current-batch audits and integration](./audit-current-batch.md). Eighteen
publications cleared; ContextPilot adds one hold for an omitted training-route
selector qualification. [Claude Context Guard integration](./claude-context-guard-integration.md)
and [rolling execution 09](./rolling-09.md) retain earlier checkpoints. These
are acceptance counts, not a live Bash-batch status. The checklist retains
remaining holds and unblock conditions.
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
