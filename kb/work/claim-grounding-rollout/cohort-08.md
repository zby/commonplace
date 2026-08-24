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

Recorded from the four blob-verified target notes before opening either listed
ingest or snapshot. Each row is one source-dependent use. Footer wording that
restates a body use remains in the same row.

| ID | target | claim as frozen | source-side need |
|---|---|---|---|
| FDS-1 | `files-defer-centralized-schema-commitment-until-invariants-stabilize` | One self-reported production system writes canonical objects to S3 while using PostgreSQL as a derived index for important list queries. The case is specific to that system's AWS setting and access patterns, and serves as an existence witness that serving dependence can coexist with canonical state elsewhere. | `lessons-from-building-ai-agents-for-financial-services`: whether the report identifies S3 objects as the canonical or source-of-truth state and PostgreSQL as a derived index, which queries depend on that index, and the system and workload limits on the example. Keep the target's lineage inference separate from the report's own claims. |
| FPR-1 | `first-principles-reasoning-selects-for-explanatory-reach-over` | SuperARC's integer-versus-binary sequence performance is suggestive evidence for cue sensitivity and algorithmic-compression explanatory-reach, but is not load-bearing for the note. | `superarc-ait-benchmark-llm-compression-abstraction`: whether the benchmark reports a performance difference between integer and binary sequence representations, the evaluated conditions and magnitude or direction of that difference, and what—if anything—the source attributes to cue sensitivity or algorithmic compression. Keep the explanatory-reach transfer as target-side analysis. |
| LDP-1 | `linked-note-durable-payload-is-what-consumption-path-cannot-supply` | A bounded practitioner case reports that model-absorbed procedural scaffolding shrank while exact fiscal-calendar normalization remained explicit. | `lessons-from-building-ai-agents-for-financial-services`: whether the practitioner report removed or reduced procedural prompt material because the model already supplied it while retaining an exact fiscal-calendar normalization rule, including what changed, why, and the case boundary. Keep the durable-payload generalization as target-side analysis. |
| RC-1 | `reverse-compression-is-when-llm-output-expands-without-adding` | In SuperARC's recursive-compression benchmark, many LLM-generated programs that pass the output check directly print the target sequence instead of encoding a generative rule. Print-statement solutions dominate across programming languages and temperature changes, so the target treats the result as a formal instance of reverse-compression rather than a sampling accident. The footer repeats this use. | `superarc-ait-benchmark-llm-compression-abstraction`: the benchmark task and correctness oracle, how direct-print programs are treated by its compression measure, the reported prevalence across languages and temperatures, and the limits on inferring absence of algorithmic structure or robustness beyond the evaluated runs. Keep the reverse-compression label and transfer to KB writing as target-side analysis. |

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
