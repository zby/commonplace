# Agent prompt — cleanup cohort 08

Self-contained. Point one agent at this file; it needs nothing from the
conversation that created it.

**Scope:** 4 targets, 2 ingests, 4 note-to-ingest pairs, 0.04 MiB of snapshots.
This combines two disconnected two-note components. Both ingests already carry
one Claims entry, making this the cheapest residual cohort and the best first
check that incumbent entries can be reused across later target uses.

---

Work cleanup cohort 08 in the Commonplace repository at
`/home/zby/llm/commonplace`.

Read `kb/work/claim-grounding-rollout/cohort-08.md`, then
`kb/work/claim-grounding-rollout/procedure.md`. Follow the procedure's six steps
and literal grounding route, subject to the stricter phase ordering below. The
manifest is the only authority for which notes and ingests you may mutate.

## Ownership and concurrency

You own every note and ingest listed in cohort 08 and no others. Cohorts 08, 09,
and 10 are disjoint on both notes and ingests and may run concurrently. Do not
edit the rollout README, another cohort file, or an artifact outside your
manifest. Do not delegate or spawn writers inside this cohort.

Concurrent work may make the repository dirty. Ignore unrelated changes, never
stage them, and stop only if another change overlaps one of your owned paths.

## Phase 1 — freeze and inventory before source reading

1. Verify each target's current blob against the manifest with
   `git rev-parse --short HEAD:<path>`. A mismatch is a named blocker; do not
   silently refreeze or inventory a moved target.
2. Read all four target notes, but open no listed ingest or snapshot yet.
3. Replace the manifest's pending inventory with one row per load-bearing
   source-dependent use: `ID | target | claim as frozen | source-side need`.
   Footer wording that repeats a body use travels with the same row.
4. Save the complete inventory before beginning Phase 2. The unit is one claim
   use, not one note; one note may produce several rows and dispositions.

This ordering is load-bearing. Reading a source first lets its vocabulary decide
what counts as the target's claim and has already produced charitable
over-attribution in this rollout.

## Phase 2 — ground source-side needs

Work one ingest at a time after the complete inventory is saved.

1. Require its exact name-paired snapshot. Check canonical source equality and
   the snapshot's exact SHA-256 against the ingest before using it.
2. For each source-side need, read and execute
   `kb/instructions/ground-source-dependent-claims.md` with the exact ingest path
   and need. Read the complete incumbent Claims section first. Reuse an entry
   unchanged only when its proposition, scope, and limitation fully answer the
   need; otherwise append a new bounded entry through the instructed route.
3. Only the checksum-verified snapshot establishes a source claim. Never infer a
   Claims entry from Summary, Connections Found, Extractable Value, model
   familiarity, or a secondary resource.
4. Quote snapshot bytes exactly. Whitespace normalization permits wrapped spans;
   it does not permit silently repairing capture artifacts.
5. Record reuse or append, checksum result, and ingest validation in the
   manifest. Do not merge or broaden distinct source demands for convenience.

If a target needs a source outside the manifest, record a `literature handoff`.
Do not capture or ingest it in this cohort.

## Phase 3 — disposition and repair targets

For each inventory row, compare the frozen use with the selected Claim, Scope,
Limitation, and target-side transfer. Use exactly one terminal disposition:
`false positive`, `unavailable`, `grounded`, `narrowed`,
`contradicted/repaired`, `retained local delta`, or `literature handoff`.

Thematic overlap is not support. If the source establishes less than the target
asserts, use `narrowed`; if it establishes the opposite, repair the target. Keep
human-to-agent or system-specific transfer reasoning in the target and label it
as local analysis.

After each target is repaired, run `commonplace-validate` on every changed note
and ingest and run source-as-gate review for every listed note-to-ingest pair.
Repair WARN or FAIL findings within the manifest. Finish only when every
inventory row has a terminal disposition or named blocker and the final source
selector is empty for the requested model partition.

Fill the manifest's grounding record, completion record, disposition
distribution, and identity/accumulation observation. Explicitly distinguish
scope pressure from ambiguity about which Claims entry applies.

Review `git diff` before committing. Stage only this cohort's manifest and the
listed notes and ingests you changed; use one atomic stage-and-commit command and
never `git add -A`. Report the commit, dispositions, validation and review
results, handoffs, blockers, and any pressure for claim IDs or reconciliation.
