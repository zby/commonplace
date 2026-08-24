# Cleanup cohort 08 — frozen 2026-08-24

**Status: ready.** Frozen at repository `a91ed377`.

This cohort combines the two smallest residual connected components. Its four
notes and two ingests are disjoint from cohorts 09 and 10 on both mutation
axes. The two pairs inside this cohort are also disjoint, but one agent owns the
whole cohort so no internal coordination is required.

Scope: 4 targets, 2 ingests, 4 note-to-ingest pairs, 0.04 MiB of snapshots. Both
ingests already contain one Claims entry from cohort 02. Reuse an incumbent
entry only if it fully answers the frozen source-side need; prior population is
not evidence of adequacy.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `files-defer-centralized-schema-commitment-until-invariants-stabilize` | `402dbe16` | `lessons-from-building-ai-agents-for-financial-services` |
| `first-principles-reasoning-selects-for-explanatory-reach-over` | `f7004778` | `superarc-ait-benchmark-llm-compression-abstraction` |
| `linked-note-durable-payload-is-what-consumption-path-cannot-supply` | `9346afe1` | `lessons-from-building-ai-agents-for-financial-services` |
| `reverse-compression-is-when-llm-output-expands-without-adding` | `293cd102` | `superarc-ait-benchmark-llm-compression-abstraction` |

## Source-blind claim inventory

Pending. Before opening either ingest or snapshot, replace this paragraph with
one table row per load-bearing source-dependent use:

`ID | target | claim as frozen | source-side need`

## Grounding record

Pending. Record which incumbent Claims entry was reused or which new entry was
appended for every source-side need, plus checksum and validation results.

## Completion record

Pending. Record one row per claim use:

`ID | disposition | target change | validation and source-review result`

## Identity and accumulation observation

Pending. Record reuse, similar-entry accumulation, ambiguous selection,
disputed entries, or pressure for claim IDs or reconciliation. “None observed”
is a finding when bounded to this cohort.
