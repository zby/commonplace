# Cleanup cohort 05 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.31 MB across 5 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `bounded-context-orchestration-model` | `b06b3041` | `context-providers-the-missing-layer-between-agents-and-tools` |
| `final-task-success-does-not-establish-intended-path-health` | `18fd0bf0` | `the-self-healing-agent-harness-2048912026018484317` |
| `maintenance-capacity-must-match-harmful-artifact-inflow` | `254e5e7f` | `hacker-news-ai-dr-ai-didnt-read` |
| `oracle-accumulation-improves-the-selection-environment` | `e40efdea` | `harness-engineering-leveraging-codex-agent-first-world` |
| `world-models-assess-explanatory-reach-through-action-conditioned` | `48a31ff4` | `why-ai-systems-dont-learn-and-what-to-do-about-it` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Frozen claim inventory

Recorded from the five frozen note blobs before any named ingest or source
snapshot was read.

| ID | Target | Claim as frozen | Source-side need |
|---|---|---|---|
| BC-1 | `bounded-context-orchestration-model` | “The ContextProvider pattern is a source-scoped singleton-batch instance.” | Whether the source describes source-scoped provider agents that a parent invokes through a bounded request. The singleton-batch mapping is the note's transfer. |
| BC-2 | `bounded-context-orchestration-model` | “A parent offers a small action set such as `query_slack`, and `select(K)` chooses the source boundary and frames the request.” | Whether the parent-facing ContextProvider interface is a small action set that includes `query_slack`; selection and framing in `select(K)` are the note's transfer. |
| BC-3 | `bounded-context-orchestration-model` | “A provider sub-agent owns the raw tools, source quirks, permissions, and optional skills used by its `call(C)`.” | Whether a provider agent encapsulates the underlying source tools, source-specific behavior, permissions, and optional skills. The `call(C)` mapping is the note's transfer. |
| BC-4 | `bounded-context-orchestration-model` | “The source supplies no reproducible token or latency evidence, so it illustrates the decomposition without establishing its efficacy.” | Whether the named source reports reproducible token-usage or latency evidence for the ContextProvider pattern. |
| FH-1 | `final-task-success-does-not-establish-intended-path-health` | The ingest “independently separates final outcome grading from trajectory monitoring for infrastructure health.” | Whether the source treats final-outcome validation and execution-trajectory monitoring as separate checks, with the latter used to detect infrastructure problems. |
| MC-1 | `maintenance-capacity-must-match-harmful-artifact-inflow` | “Generated comments and documentation can enter later agents' context, where those agents may trust, imitate, or elaborate on them.” | Whether practitioners report later coding agents consuming retained AI-generated comments or documentation as context and relying on or reproducing it. |
| MC-2 | `maintenance-capacity-must-match-harmful-artifact-inflow` | “A misleading explanation can therefore increase exposure and seed further defects before removal.” | Whether practitioner reports support propagation from a misleading retained explanation into later agent output or defects. |
| MC-3 | `maintenance-capacity-must-match-harmful-artifact-inflow` | “The AI;DR discussion supplies practitioner reports of this path, but its self-selected anecdotes establish a possible mechanism, not prevalence or effect size.” | Whether the source consists of self-selected practitioner anecdotes rather than systematic evidence measuring prevalence or effect size. |
| OA-1 | `oracle-accumulation-improves-the-selection-environment` | “Repeated human cleanup was progressively encoded as repository principles, structural tests, and linter rules.” | Whether the source reports recurring human cleanup being converted into repository guidance and enforced structural tests or lint rules. |
| WM-1 | `world-models-assess-explanatory-reach-through-action-conditioned` | The ingest supplies a “broader LeCun/Dupoux/Malik architecture where observational world modeling and action learning interact.” | Whether the source presents an architecture in which learning a world model from observation and learning through action are related parts of the system. |

## Grounded entries written

Each named snapshot was present, name-paired, source-identical, and an exact
match for its ingest's `snapshot_sha256`. Each ingest had an empty `Claims`
section before this run. One entry was appended to each:

- `context-providers-the-missing-layer-between-agents-and-tools` — “In Bedi's reported ContextProvider pattern, each provider wraps one source behind two natural-language query/update tools; a source-scoped sub-agent owns the underlying tools and source-specific operating details and may load a source skill.”
- `the-self-healing-agent-harness-2048912026018484317` — “In the reported CREAO harness, graders evaluate final responses rather than trajectories; low outcome scores then trigger separate engineering investigation that can work backward to integration, infrastructure, tool-contract, context, or deployment failures.”
- `hacker-news-ai-dr-ai-didnt-read` — “Several commenters in one Hacker News discussion report that retained AI-generated code comments become later model input, can mislead or anchor the model on its own prior ideas, and may compound context poisoning.”
- `harness-engineering-leveraging-codex-agent-first-world` — “In the Codex team's reported codebase, recurring manual AI-slop cleanup was replaced by repository-encoded standards and automated cleanup, alongside structural tests and custom linters that enforce architecture and other rules.”
- `why-ai-systems-dont-learn-and-what-to-do-about-it` — “Dupoux, LeCun, and Malik propose observation learning and action learning as interacting subsystems: observational world models can support action learning, action can improve observational data, and meta-control decides when and how the interactions occur.”

## Completion record

Deterministic validation passed cleanly for all five ingests and all five
notes. The `source` lens was run explicitly under the `codex` partition. Four
pairs passed on the first review. OA-1 initially warned because “at scale” was
not retained in the normalized Claims entry; the target was narrowed to “one
practitioner instance,” and the replacement pair passed. The final selector
returned no stale source pairs.

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| BC-1 | retained local delta | Recast the provider description in the normalized source wording and made the singleton-batch interpretation explicitly the note's `select`/`call` transfer. | ingest + note PASS; source PASS (job 7981) |
| BC-2 | narrowed | “A small action set such as `query_slack`” became the source's exact two query/update tools per provider; source selection and framing remain note-side transfer. | ingest + note PASS; source PASS (job 7981) |
| BC-3 | narrowed | Raw-tool, operating-detail, and optional-skill ownership remain; generic permission ownership became permission isolation in the reported database and GitHub examples only. | ingest + note PASS; source PASS (job 7981) |
| BC-4 | grounded | Kept the no-reproducible-evidence boundary and named what is present and absent: rough Scout trends, but no table, workload definition, raw data, or pinned revision. | ingest + note PASS; source PASS (job 7981) |
| FH-1 | false positive | Replaced `evidenced-by` with a bounded `see-also`: the source grades outcomes and investigates low scores, but does not test successful fallbacks or intended-path health. | ingest + note PASS; source PASS (job 7982) |
| MC-1 | narrowed | Replaced “trust, imitate, or elaborate” with the reports actually retained: comments become later model input and may mislead or anchor it. | ingest + note PASS; source PASS (job 7983) |
| MC-2 | narrowed | Replaced “seed further defects” with a possible exposure-and-constraint path and stated that the thread does not establish later outputs became defects. | ingest + note PASS; source PASS (job 7983) |
| MC-3 | grounded | Kept and made explicit the bound to self-selected, unverified anecdotes from one discussion with no prevalence or effect-size result. | ingest + note PASS; source PASS (job 7983) |
| OA-1 | narrowed | Replaced a progressive pattern “at scale” with one practitioner instance: manual cleanup was replaced by encoded standards and automation alongside tests and linters; no per-check lineage or later discrimination is shown. | ingest + note PASS; source PASS (job 7991; job 7984 WARN repaired) |
| WM-1 | grounded | Aligned the footer with the normalized A-B-M interaction claim and stated that this ingest does not ground the note's reach-assessment claim. | ingest + note PASS; source PASS (job 7985) |

**Distribution:** three grounded, five narrowed, one false positive, and one
retained local delta. No source was unavailable, no re-ingest or literature
handoff was needed, and no claim was contradicted.

## Identity and accumulation observation

No ingest had an incumbent entry, so no similar entries accumulated and no
selection ambiguity or reconciliation pressure appeared. Whole-section
selection was trivial with one entry in each of five sections. The OA-1 warning
was scope pressure, not identity pressure: the target used a scale
characterization absent from the selected entry, and narrowing the target
resolved it without adding or reconciling another entry. This cohort therefore
adds no evidence that denser Claims sections need claim IDs or intermediate
nodes.
