# Agent prompt — cleanup cohort 09a

Self-contained. Point one agent at this file; it needs nothing from the
conversation that created it.

**Scope:** 15 targets, 20 ingests, 37 note-to-ingest pairs, 1.13 MiB of
snapshots. Four ingests already carry five Claims entries. This is the smaller
of the two residual high-connectivity components and should run before cohort 10
if the cohorts are executed serially.

---

Work cleanup cohort 09a in the Commonplace repository at
`/home/zby/llm/commonplace`.

Read `kb/work/claim-grounding-rollout/cohort-09a.md`, then
`kb/work/claim-grounding-rollout/procedure.md`. Follow the procedure's six steps
and literal grounding route, subject to the stricter phase barriers below. The
manifest is the only authority for which notes and ingests you may mutate.

## Ownership and concurrency

You own every note and ingest listed in cohort 09a and no others. Cohorts 08, 09,
and 10 are disjoint on both notes and ingests and may run concurrently. Do not
edit the rollout README, another cohort file, or an artifact outside your
manifest. Do not delegate or spawn writers inside this cohort; its connectivity
is exactly why it has one mutation owner.

Concurrent work may make the repository dirty. Ignore unrelated changes, never
stage them, and stop only if another change overlaps one of your owned paths.

## Phase 1 — freeze and inventory every target before source reading

1. Verify each target's current blob against the manifest with
   `git rev-parse --short HEAD:<path>`. A mismatch is a named blocker; do not
   silently refreeze or inventory a moved target.
2. Read all fifteen target notes, but open no listed ingest or snapshot yet.
3. Replace the manifest's pending inventory with one row per load-bearing
   source-dependent use: `ID | target | claim as frozen | source-side need`.
   Footer wording that repeats a body use travels with the same row.
4. Save the complete inventory before beginning Phase 2. The unit is one claim
   use, not one note; one note may produce several rows and dispositions.

Do not weaken this to “inventory a note, then read its source.” A source shared
by later notes would contaminate their inventories. The phase barrier preserves
the source-blind baseline across the whole connected component.

## Phase 2 — build the source-demand plan and ground it

Group the completed inventory by ingest in the manifest. Work one ingest at a
time; do not try to retain several source bodies in working context.

For each ingest:

1. Require its exact name-paired snapshot. Check canonical source equality and
   the snapshot's exact SHA-256 against the ingest before using it.
2. Read the complete Claims section and map every target need for this ingest to
   an adequate incumbent entry or to a required append.
3. For each unmet need, read and execute
   `kb/instructions/ground-source-dependent-claims.md` with the exact ingest path
   and source-side need. Preserve incumbent entries exactly. Similar, narrower,
   broader, or disputed entries may coexist; do not merge them.
4. Only the checksum-verified snapshot establishes a source claim. Never infer a
   Claims entry from Summary, Connections Found, Extractable Value, model
   familiarity, or a secondary resource.
5. Quote snapshot bytes exactly. Whitespace normalization permits wrapped spans;
   it does not permit silently repairing capture artifacts.
6. Validate the ingest and record reuse or append, target rows served, checksum,
   and result before moving to the next source.

Do not compress several distinct demands into one broad entry to reduce work.
The purpose of the cohort is to test whether natural accumulation remains
selectable without claim IDs. If a target needs a source outside the manifest,
record a `literature handoff`; do not capture it here.

Phase 2 closes only when every inventory row has an adequate selected Claims
entry or a named source blocker. Do not repair a target before all its listed
source needs reach that state.

## Phase 3 — disposition and repair targets

Work one target at a time from its frozen inventory. Compare each use with the
selected Claim, Scope, Limitation, and target-side transfer. Use exactly one
terminal disposition: `false positive`, `unavailable`, `grounded`, `narrowed`,
`contradicted/repaired`, `retained local delta`, or `literature handoff`.

Thematic overlap is not support. If the source establishes less than the target
asserts, use `narrowed`; if it establishes the opposite, repair the target. Keep
human-to-agent or system-specific transfer reasoning in the target and label it
as local analysis.

If target repair exposes a genuinely missing source-side need, do not infer the
answer or append opportunistically while editing the target. Record the new need,
return to Phase 2 for that ingest, validate it, and only then resume the target.

After each target is repaired, run `commonplace-validate` on every changed note
and ingest and run source-as-gate review for every listed note-to-ingest pair.
Repair WARN or FAIL findings within the manifest. Finish only when every
inventory row has a terminal disposition or named blocker and the final source
selector is empty for the requested model partition.

Fill the manifest's grounding record, completion record, disposition
distribution, and identity/accumulation observation. Explicitly distinguish
scope pressure from ambiguous entry selection, duplication, dispute, or genuine
reconciliation pressure.

Review `git diff` before committing. Stage only this cohort's manifest and the
listed notes and ingests you changed; use atomic stage-and-commit commands and
never `git add -A`. A source-phase checkpoint commit is allowed after the entire
source-demand plan is grounded. Report all commits, dispositions, validation and
review results, handoffs, blockers, and identity evidence.
