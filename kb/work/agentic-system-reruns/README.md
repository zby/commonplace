# Rerun the previously analysed agentic systems

## Commission

The operator commissioned this workshop on 2026-10-12 to rerun all systems
analysed under the previous analysis system. The goal is fresh, source-grounded
coverage through the current
[`analyse-agentic-system` workflow](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md),
not conversion of old reviews into the new format.

This workshop is the scheduling home for that whole-corpus rerun. Creating it
does not launch any analyses. Method changes, comparison regeneration and public
landscape synthesis are separate work unless explicitly commissioned.

## Population

[Systems](./systems.md) is the rerun checklist. Its initial inventory contains
**206 targets**, grouped from **223 analysis records**:

- 155 legacy implementation-grounded reviews in `kb/agent-memory-systems/reviews/`.
- Seven legacy lightweight reviews in `kb/agent-memory-systems/lightweight/`.
- 12 authored accounts in `kb/agentic-systems/reviews/`.
- 43 generated historical reviews in `kb/agentic-systems/reviews-archive/`.
- Six current sets in `kb/agentic-system-analyses/retained/`, included so already
  regenerated systems are not silently exempted from the requested rerun.

Repeated reviews of the same named system share a row. The dated Instinctual
Memory reviews are grouped, and `gbrain-garrytan` is grouped with GBrain. Four
`.replaced.` predecessor files are excluded as additional targets. Paper-only
WikiSkill and the independent Stahl-G implementation stay separate. Likewise,
different projects with similar names, such as the two SAGE systems and the
LLM Wiki variants, stay separate.

This is a scheduling inventory, not a verified count of distinct upstream
repositories. Verify identity and scope before dispatch; record any justified
split or merge in the checklist rather than silently dropping coverage. The
linked historical records establish inclusion, not findings for a fresh run.
Unreviewed TODOs, source ingests alone, and workshop trials are not extra targets.

## Relationship to existing work

The earlier [agentic-memory-refresh workshop](../agentic-memory-refresh/README.md)
inventoried the 162 legacy memory reviews and retains its pilots and execution
history. This new commission includes that population and the broader agentic
system accounts. Use this checklist for new scheduling; coordinate with any
unfinished run in the earlier workshop before assigning the same system.
Do not delete its evidence or treat an old completion as completion here.

## Execution boundary and bookkeeping

The coordinator owns target assignment, checklist updates, integration and
recovery. Read the current analysis skill and perform its worker-launch preflight
before opening a run. No worker count, concurrency setting or model choice is
fixed by this framing. Determine these from current runtime support and the
skill, not from previous launches.

Each run gets a fresh coordinator and the source identity, commissioned scope,
owned output destination, and current method instructions. Do not pass old
review findings, comparison values or previous analysis results as evidence.
Legacy links are for the scheduling coordinator to resolve source identity;
follow the skill's isolation rules when constructing worker handoffs.
Freeze a source revision or immutable document capture for the new run. If
identity, access, source selection or output ownership is unresolved, mark the
row blocked and return that decision to the coordinator before launch.

Only one active run may own a system's public destination. Parallel work needs
disjoint run/output ownership and coordination of shared publication state.
Use the skill's current run setup, validation and publication route; accepted
sets belong in `kb/agentic-system-analyses/retained/`, not this workshop. Leave
legacy reviews and archived results as historical evidence.

The checklist starts with every row `pending`. Change a row to `running` only
when it has an assigned run. Record its run identifier and frozen source boundary.
Use `complete` only after the current workflow accepts and publishes the set;
add its overview link. Use `blocked` with a concrete reason and unblock condition.
Keep the checkbox unchecked for pending, running and blocked rows. Check it only
for completed reruns. Any exclusion requires an explicit operator disposition
recorded beside the row; lack of evidence is a blocker, not completion.

Scheduling order is open. Before expanding a batch, reconcile the previous
batch's publication and blockers. A discovered shared-method defect pauses
affected targets and returns to method maintenance; do not compensate by editing
accepted results outside the workflow.

## Fast report-only statistics

Use the [stats script](../../../scripts/agentic_system_rerun_stats.py) for a
read-only summary of generated reports:

```bash
python3 scripts/agentic_system_rerun_stats.py
python3 scripts/agentic_system_rerun_stats.py --since 2026-10-12 --json
```

The default scans current retained sets. To include an in-flight run, supply its
report artifact directory with `--root`; supplied roots replace the default,
so also pass `--root kb/agentic-system-analyses/retained` when both are wanted.
Use repeated `--run-id` filters for exact workshop assignments. A date filter
includes other runs from that date too; it does not prove workshop ownership.

The script counts report sets and recorded blockers, limits/warnings, blocked
dispositions and incomplete sets. It reads only named generated Markdown
reports, including an exported `report-check.md` if supplied. It does not inspect
sources, traces, logs, manifests or runtime stores, and it does not run validators.
It uses structured report sections, not mentions of failure in descriptive prose.

This is a fast report-health snapshot, not the checklist completion count.
Reportless failures are invisible; zero recorded failures is not proof that all
206 targets succeeded. Keep scheduling progress in the checklist and use report
statistics to identify outputs needing attention. See the
[script documentation](../../../scripts/README.md#agentic-analysis-rerun-statistics)
for filters, status meanings and exit codes.

## Closure

The workshop closes when every listed target has a validated, published rerun
or an explicit operator-approved exclusion, and no running assignment remains.
Partial progress is useful: report completed, pending and blocked counts with
links to accepted outputs and concrete blockers. Never describe a partial batch
as a completed corpus refresh.

At closure, retain any durable operational lessons in the appropriate library
collection, then remove this temporary workshop and its Active Workshops entry.
The accepted analysis sets remain the durable outputs.
