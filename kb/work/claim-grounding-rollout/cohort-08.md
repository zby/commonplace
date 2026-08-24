# Cleanup cohort 08 — frozen 2026-08-24

**Status: complete.** Frozen at repository `a91ed377`; executed 2026-08-24.

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

No incumbent entry fully answered a complete frozen source-side need. Four
entries were appended through the Claims-owned mutation route:

- **FDS-1 — added:** “In a first-person account of Fintool's S3-first
  architecture, the author says user data including watchlists, portfolios,
  preferences, memories, and skills is stored as YAML files in S3 as the source
  of truth; Lambda functions synchronize changes to PostgreSQL, list queries
  use the database, and writes and single-item reads use S3.”
- **FPR-1 — added:** “In the captured SuperARC report, LLM performance improved
  dramatically when integer sequences rather than binary sequences were
  tested; the authors attribute the improvement to memorization of common
  mathematical sequences in training data and use it to argue that binary
  sequences are needed for an unbiased evaluation.”
- **LDP-1 — added:** “In a first-person account of Fintool, the author says some
  simple tasks that previously needed detailed step-by-step skills can now
  often be requested with a short instruction as models improve; separately,
  the system maintains fiscal calendars for more than 10,000 companies,
  normalizes period references to absolute date ranges, and has more than 200
  period-extraction tests.”
- **RC-1 — added:** “In SuperARC's reported code-generation results, most
  programs classified as correct printed the target sequences directly;
  print-statement solutions dominated correct outputs across programming
  languages, and temperature variations produced nearly identical
  no-compression percentages. The SuperARC-seq framework classifies direct
  prints separately as Type 3 and weights non-trivial solutions more heavily.”

The exact name-paired financial-services snapshot matched canonical source
`https://x.com/nicbstme/status/2015174818497437834` and SHA-256
`5d31480668eb9fedea35957fd66e72133d066c3e9300c80df68d1c3ee57cdebf`.
Its ingest passed cleanly after each append; the final validation resolved all
seven verbatim extracts.

The exact name-paired SuperARC snapshot matched canonical source
`https://arxiv.org/html/2503.16743v5` and SHA-256
`8ad7f503f89df5ffa942fa83dda845f3d6d772049043f22619d65e2e512026fe`.
Its ingest passed cleanly after each append; the final validation resolved all
eight verbatim extracts.

## Completion record

All four notes and both changed ingests pass `commonplace-validate` cleanly.
Source conformance ran in the `codex` model partition through the local-review
fallback required by this cohort's no-delegation rule. Every requested pair
returned PASS, and its follow-up selector returned `targets: []`. There were no
literature handoffs, unavailable sources, or blockers.

| ID | disposition | target change | validation and source-review result |
|---|---|---|---|
| FDS-1 | grounded | None. The frozen text already presents the architecture as one self-reported, AWS- and access-pattern-specific existence witness, not a universal storage prescription. | Note and ingest PASS clean; source pair PASS in review job 8020; follow-up selector empty. |
| FPR-1 | retained local delta | Reworded the footer to the reported integer-over-binary direction and source attribution. Cue sensitivity and explanatory-reach are now explicitly target-side analysis and remain non-load-bearing. | Note and ingest PASS clean; source pair PASS in review job 8017; follow-up selector empty. |
| LDP-1 | narrowed | Replaced “model-absorbed” scaffolding and normalization that “remained explicit” with the reported simple-task instruction reduction and separately retained fiscal normalization and tests. The footer states that the source does not locate normalization in the model's consumption path and labels the durable-payload transfer as local analysis. | Note and ingest PASS clean; source pair PASS in review job 8018; follow-up selector empty. |
| RC-1 | narrowed | Replaced the hard-oracle and “more than a sampling accident” claims with the source's correct-output classification, Type 3 treatment, and qualitative language/temperature results. The note now preserves the missing settings, counts, uncertainty, and beyond-run sampling limit and labels reverse-compression as local analysis. The footer was aligned to the same use. | Note and ingest PASS clean; source pair PASS in review job 8019; follow-up selector empty. |

## Disposition distribution

One grounded, two narrowed, one retained local delta, and zero false positives,
unavailable, contradicted/repaired, or literature handoff dispositions.

## Identity and accumulation observation

Both incumbent entries exerted **scope pressure**, but neither created ambiguity
about which entry applied. The financial-services incumbent covered fiscal
normalization but not its contrast with reduced skill detail. The SuperARC
incumbent covered binary-task scores and print-only prevalence but not the
integer comparison or the cross-language and temperature result. Under the
one-need/one-entry and append-only rules, neither could be reused unchanged for
the complete frozen need.

Each ingest therefore accumulated two new entries alongside one incumbent.
LDP-1 repeats the fiscal-normalization premise already retained by the
financial-services incumbent, and RC-1 overlaps the SuperARC incumbent's
print-only premise while adding the missing robustness dimensions. The exact
new entries remain uniquely selectable for the frozen uses, and no entry was
disputed. This is modest pressure for later reconciliation of shared premises,
not observed pressure for claim IDs or an intermediate claim node: exact
paraphrase plus Scope and Limitation still disambiguated every selection in this
four-use cohort.
