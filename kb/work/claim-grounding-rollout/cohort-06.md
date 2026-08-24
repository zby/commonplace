# Cleanup cohort 06 — frozen 2026-08-24

**Status: executed 2026-08-24; ten rows reached a terminal disposition. A
post-completion exact-pair repair removed the snapshot-identity blocker; DS-1
and DS-2 now await grounding and disposition.**

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.12 MB across 5 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision` | `2b29fb47` | `how-to-recursively-improve-your-agents-2084301728363462919` |
| `automated-synthesis-is-missing-good-oracles` | `8b89f83a` | `geometry-of-knowledge-extending-diversity-boundaries-llms` |
| `llm-generation-relaxes-goals-where-human-writing-stalls` | `29f897dd` | `borretti-human-routers-of-machine-words` |
| `structure-inference-needs-capture-at-the-decision-surface` | `2e01de4d` | `palantir-ontology-vs-decision-traces` **(blocked: no snapshot)** |
| `trace-extracted-memory-earns-authority-per-operation-not-at-capture` | `a4d17feb` | `trace-trajectory-attribution-for-automated-context-engineering` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Source-blind claim inventory

Recorded from the five frozen note blobs before opening any ingest or source
snapshot.

| ID | Target | Claim as frozen | Source-side need |
|---|---|---|---|
| RP-1 | `a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision` | Agno's workflow edits a target agent's instructions, tools, parameters, and code, then restarts and retests it. | Does the source describe a recursive-improvement workflow with those editable surfaces and a restart-and-retest step? |
| RP-2 | `a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision` | In that workflow, the target specification, probe derivation, judge, platform architecture, and stopping rule remain supplied. | Which parts of the workflow are fixed or externally supplied rather than revised, specifically including the named five parts? |
| AO-1 | `automated-synthesis-is-missing-good-oracles` | Bystroński et al.'s method shifts generation diversity from the prompt surface to the embedding surface via anchor plus interpolation and improves NoveltyBench and AUT scores. | Does the paper describe anchor/interpolation in latent or embedding space, and what improvement does it report on NoveltyBench and AUT? |
| AO-2 | `automated-synthesis-is-missing-good-oracles` | The authors explicitly flag the absence of a low-quality or out-of-distribution detector, so the diversity results establish reachable novelty rather than useful novelty. | Does the paper state that its method lacks low-quality and out-of-distribution detection, and what does that limitation bound? |
| LG-1 | `llm-generation-relaxes-goals-where-human-writing-stalls` | Borretti uses "a language as fast as C and as dynamic as Lisp" as an example of a vague goal that can hold contradictory demands until concretization. | Does Borretti use the C-speed/Lisp-dynamism example and connect unconstrained imagination with internally conflicting or impossible requirements? |
| LG-2 | `llm-generation-relaxes-goals-where-human-writing-stalls` | Human writing can stall at the point where understanding or inference fails, while LLM generation returns fluent prose and leaves a human to check and route the result. | Does Borretti contrast the epistemic friction of human writing with fluent machine generation and the resulting human review/routing burden? |
| LG-3 | `llm-generation-relaxes-goals-where-human-writing-stalls` | Weizenbaum writes that a pen may stop at "because" or "therefore" when the writer discovers a missing explanation or defective inference; the quotation is attributed to *Computer Power and Human Reason*, page 108. | Does the primary source establish the quotation and page attribution? If the Borretti snapshot only reproduces it, this needs a primary-source handoff rather than grounding against Borretti. |
| DS-1 | `structure-inference-needs-capture-at-the-decision-surface` | The source supplies an architectural distinction between a world model prescribed upfront and one extracted bottom-up from decision traces. | Does the source make this architectural distinction, and how does it characterize each side? |
| DS-2 | `structure-inference-needs-capture-at-the-decision-surface` | State records the endpoint of a decision but not its legible "why"; capturing at the decision surface preserves rationale-bearing material that later state cannot reliably recover. | Does the source distinguish decision rationale from resulting state and argue that the rationale must be captured where the decision occurs? |
| TA-1 | `trace-extracted-memory-earns-authority-per-operation-not-at-capture` | In TRACE, a user correction defines the discrepancy, a root-cause agent traces backward to nominate a fault source, and a recommender treats that attribution as a hypothesis. | Does the paper describe this correction-to-attribution pipeline, including the status of the nominated source? |
| TA-2 | `trace-extracted-memory-earns-authority-per-operation-not-at-capture` | The recommender reads the implicated context artifact, checks authoritative sources, may confirm, refine, or override the diagnosis, and proposes a file operation for human review. | Does the paper separate attribution from source-grounded recommendation in this way, including human review of the proposed operation? |
| TA-3 | `trace-extracted-memory-earns-authority-per-operation-not-at-capture` | TRACE's reported "fix effectiveness" measures agreement between a recommended operation/path and synthetic labels; it does not apply the change or rerun the task. | What exactly is the fix-effectiveness metric, and does the evaluation apply proposed changes or test repaired task behavior? |

## Original blocker

- `palantir-ontology-vs-decision-traces` — the required name-paired snapshot
  `kb/sources/.snapshots/palantir-ontology-vs-decision-traces.md` is absent.
  Snapshotting the ingest's canonical URL returned the existing
  `kb/sources/.snapshots/palantir-competed-with-snowflake-before-llms.md` with
  the incumbent checksum `b98dc7e5…b6e`; the re-ingest contract forbids using a
  differently named checksum match, so grounding and source review did not run.

## Post-completion exact-pair repair — 2026-08-24

The incumbent bytes were already present at
`kb/sources/.snapshots/palantir-competed-with-snowflake-before-llms.md`. Their
SHA-256 matched the ingest's recorded
`b98dc7e5e9919a865f861d85586c1af18bc49286c90aaa02acd7db77eced6b6e`, and the
snapshot and ingest carried the same canonical source. The Markdown snapshot
was moved without byte changes to the required
`kb/sources/.snapshots/palantir-ontology-vs-decision-traces.md` path; its X
capture companion was moved to the same stem. The paired ingest then passed
`commonplace-validate` cleanly.

This repairs path identity only. DS-1 and DS-2 retain their original completion
record below until the now-available snapshot is grounded, the target is
dispositioned, and source review runs.

## Completion record

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| RP-1 | grounded | Replaced the compressed workflow description with the selected source wording: probes come from the specification and sessions, run against the live agent, and failures lead to target edits, restart, and rerun. | Target and ingest clean PASS; source gate PASS (`codex`, job 7986). |
| RP-2 | narrowed | Replaced "remain supplied" with the observable bound: the post reports no revision to the surrounding method or platform, which does not prove those parts incapable of revision. | Target and ingest clean PASS; source gate PASS (`codex`, job 7986). |
| AO-1 | narrowed | Replaced the prompt-surface shorthand and generic "improving scores" with the anchored interpolation mechanism and the specific reported NoveltyBench diversity and AUT originality comparisons. | Target and ingest clean PASS; source gate PASS (`codex`, job 7987). |
| AO-2 | contradicted / repaired | Deleted the inference that the results measure reachable rather than useful novelty; retained the missing explicit detector as an output-screening gap without erasing the paper's utility/originality measurements. | Target and ingest clean PASS; source gate PASS (`codex`, job 7987). |
| LG-1 | grounded | Attributed Borretti's concretization claim and C-speed/Lisp-dynamism example directly, then marked the conjunction and witness model as the note's extension. | Target clean PASS; ingest PASS with its pre-existing missing-`distillation.md` link warning; final source gate PASS (`codex`, job 7990). |
| LG-2 | narrowed | Recast the human/LLM contrast as a conceptual, idealized failure mode with no prevalence claim; the argmax and silent-relaxation mechanism remains explicitly conjectural. | Target clean PASS; ingest PASS with its pre-existing link warning; final source gate PASS (`codex`, job 7990). |
| LG-3 | literature handoff | Changed direct primary-source presentation to "Borretti reproduces and attributes" and recorded that the book wording, context, and page remain unverified until a primary snapshot is captured. A bounded secondary-attribution Claim was added after the first source gate exposed the missing support. | Initial source gate FAIL (job 7988); repaired ingest validates with its pre-existing link warning; rerun PASS (`codex`, job 7990). |
| DS-1 | named blocker | None; the frozen claim was not compared with source content because the exact name-paired snapshot could not be produced through the required route. | Unchanged target clean PASS; grounding and source gate not run. |
| DS-2 | named blocker | None; same snapshot-identity blocker as DS-1. | Unchanged target clean PASS; grounding and source gate not run. |
| TA-1 | narrowed | Restated the delta-to-reverse-attribution pipeline from the selected Claim and added its synthetic-trace and chain-of-thought scope. | Target and ingest clean PASS; source gate PASS (`codex`, job 7989). |
| TA-2 | grounded | Restated the Recommender's hypothesis verification, authoritative cross-check, possible refinement/override, and CRUD recommendation for human review. | Target and ingest clean PASS; source gate PASS (`codex`, job 7989). |
| TA-3 | contradicted / repaired | Replaced "the system does not apply the change" with the supported distinction: the proposed architecture applies approved fixes, but reported fix effectiveness measures only operation-and-path agreement and contains no application, rerun, or behavioral outcome. | Target and ingest clean PASS; source gate PASS (`codex`, job 7989). |

Final freshness check for the four reviewed source pairs returned
`{"targets": []}` under the `codex` partition.
