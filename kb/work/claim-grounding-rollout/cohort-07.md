# Cleanup cohort 07 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.53 MB across 9 ingests.

Executed 2026-08-24 at repository `9f6176a9`. All four working-tree target
blobs still matched their frozen blob IDs before source reading.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `choosing-what-to-learn-requires-both-validity-and-learning-value-gates` | `97a26495` | `into-the-unknown-self-learning-large-language-models`<br>`self-training-large-language-models-through-knowledge-detection` |
| `history-has-one-chance-to-become-checkable` | `380508b6` | `in-toto-farm-to-table-guarantees`<br>`prov-overview` |
| `llm-output-deviation-requires-three-way-diagnosis` | `d4bc92bc` | `many-ai-analysts-one-dataset-agentic-data-science-multiverse`<br>`prompt-stability-code-llms-emotion-personality-variations` |
| `reflective-coverage-is-graded-across-representational-forms` | `f75a1fd4` | `gybels-et-al-2006-inter-language-reflection`<br>`maes-computational-reflection-1988`<br>`wuyts-ducasse-2001-symbiotic-reflection` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Frozen claim inventory

Recorded from the four frozen note blobs before opening any of the nine named
ingests or snapshots.

| ID | Target | Claim as frozen | Source-side need |
|---|---|---|---|
| LG-1 | `choosing-what-to-learn-requires-both-validity-and-learning-value-gates` | Learning loops need separate validity and learning-value checks before promotion. | A self-learning or self-training system in which one filter controls trustworthiness and another selects material the current model would benefit from learning. |
| LG-2 | `choosing-what-to-learn-requires-both-validity-and-learning-value-gates` | *Into the Unknown* “frames the upstream problem as deciding what previously unknown knowledge to absorb.” | The paper's own formulation of the knowledge-selection problem and what “unknown” means there. |
| LG-3 | `choosing-what-to-learn-requires-both-validity-and-learning-value-gates` | Self-Training-LLM constructs factual QA examples from Wikipedia-grounded traces, then filters them before SFT or DPO training. | The paper's pipeline order, grounding input, filtering stage, and downstream training uses. |
| LG-4 | `choosing-what-to-learn-requires-both-validity-and-learning-value-gates` | The paper calls its two filters consistency filtering and knowledge filtering: one rejects low-confidence reference answers; the other keeps cases where unconditioned model answers contradict the source-grounded answer. | The paper's definitions and mechanics for both named filters, including what each rejects or retains. |
| HH-1 | `history-has-one-chance-to-become-checkable` | W3C PROV is a systems exemplar for the records/attestation route: capturing production facts as provenance records while those facts remain available. | What PROV represents, when provenance is acquired or recorded, and whether it supports the note's production-time characterization rather than merely representing provenance later supplied to it. |
| HH-2 | `history-has-one-chance-to-become-checkable` | in-toto attestations are a systems exemplar for the records/attestation route, providing “cryptographic whole-chain attestation.” | What in-toto records and authenticates across a software supply chain, when those records are produced, and what guarantee the chain supplies. |
| OD-1 | `llm-output-deviation-requires-three-way-diagnosis` | Ma et al.'s prompt-stability study separates repeated-sample variation from systematic sensitivity to semantically equivalent framing. | The experimental factors and metrics that distinguish repeated sampling from meaning-preserving prompt variation. |
| OD-2 | `llm-output-deviation-requires-three-way-diagnosis` | The prompt-stability study does not measure underspecification because public meaning is fixed. | Whether the paper treats its prompt variants as semantically equivalent and what, exactly, its stability measures capture; the `V` inference remains target-side transfer. |
| OD-3 | `llm-output-deviation-requires-three-way-diagnosis` | The study's performance–stability result is Spearman rho = -0.433 and shows that accuracy and framing sensitivity are different properties. | The reported statistic, the variables correlated, and the authors' supported interpretation of that relationship. |
| OD-4 | `llm-output-deviation-requires-three-way-diagnosis` | In the agentic data-science multiverse, repeated runs within a fixed cell expose sampling variation. | What is held fixed within an experimental cell, what is rerun, and whether observed within-cell differences are attributed to stochastic execution. |
| OD-5 | `llm-output-deviation-requires-three-way-diagnosis` | Materially different auditor-accepted analyses support a plural valid set, conditional on that auditor. | Evidence that multiple substantively different analyses passed the same compliance evaluation, including the evaluator's role and limits. |
| OD-6 | `llm-output-deviation-requires-three-way-diagnosis` | Rejected noncompliant runs illustrate output outside the valid set, including pilot runs that hallucinated results or recalled published findings. | The paper's compliance failures and pilot exclusions, with the concrete hallucination or result-recall behavior and its status in the workflow. |
| OD-7 | `llm-output-deviation-requires-three-way-diagnosis` | Persona comparisons are not clean bias estimates when personas change the commission or stated prior. | The actual persona manipulations, especially whether they alter task instructions, role, or prior beliefs rather than style alone. |
| OD-8 | `llm-output-deviation-requires-three-way-diagnosis` | Fixed datasets, models, tools, and auditor criteria bound what the workflow can expose. | Which inputs and execution/evaluation components the experiment fixes across its multiverse and which it varies. |
| RC-1 | `reflective-coverage-is-graded-across-representational-forms` | Maes distinguishes procedural reflection, where implementation and self-representation share one operative representation, from declarative reflection, where explicit constraints must be kept consistent with procedural behavior. | Maes's definitions of procedural and declarative reflection, including the representation and consistency distinction. |
| RC-2 | `reflective-coverage-is-graded-across-representational-forms` | The representation best suited to implementation may differ from the one best suited to reasoning. | Whether Maes explicitly supports this tradeoff or whether it is a target-side inference from the procedural/declarative distinction. |
| RC-3 | `reflective-coverage-is-graded-across-representational-forms` | Wuyts and Ducasse make entity transfer explicit so each language can reason about and act on the other. | The symbiotic-reflection mechanism: what crosses the language boundary and which reflective operations become available on each side. |
| RC-4 | `reflective-coverage-is-graded-across-representational-forms` | Gybels et al. separate data mappings, which move values across a boundary, from protocol mappings, which make receiving-side operations applicable to representations of those values. | The paper's definitions and roles for data mappings and protocol mappings in inter-language reflection. |

## Completion record

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| LG-1 | retained local delta | Kept the general two-gate argument, but made the paper's two filters bounded proxies rather than evidence that the broader gates are universally required. | target PASS; both source pairs PASS |
| LG-2 | narrowed | Limited *Into the Unknown* to its own “what to learn” framing and hallucination-defined unknown factual knowledge; it does not supply general learning value. | target PASS; source PASS |
| LG-3 | **contradicted / repaired** | Replaced “filters before SFT or DPO” with the paper's actual sequence: instruction generation → SFT → preference labeling → filtering before DPO. | target PASS; source PASS |
| LG-4 | narrowed | Stated the exact filter roles: consistency removes low-confidence document-conditioned reference responses; knowledge filtering removes samples on which the SFT model appears knowledgeable. | target PASS; source PASS |
| HH-1 | narrowed | Recast PROV as a representation-and-interchange exemplar for carried provenance. The production-time necessity remains the note's argument, not a PROV claim. | target PASS; source PASS |
| HH-2 | narrowed | Replaced “cryptographic whole-chain attestation” with the signed-layout, per-step link-metadata, artifact-rule, and key-trust bounds that in-toto actually checks. | target PASS; source PASS |
| OD-1 | **contradicted / repaired** | Now says PromptSE uses repeated samples to estimate stability across variants but does not separately estimate sampling dispersion, so it does not isolate the two causes. | target PASS; source PASS after repair rerun |
| OD-2 | narrowed | Made the no-underspecification inference conditional on generated variants actually preserving public meaning; the source states and constrains that intention but does not independently audit it. | target PASS; source PASS after repair rerun |
| OD-3 | **contradicted / repaired** | Added `p = 0.122` and the confidence interval spanning zero, and deleted the inference that `ρ = −0.433` establishes decoupled properties. | target PASS; source PASS after repair rerun |
| OD-4 | narrowed | Recast fixed-cell results as run-to-run dispersion consistent with execution indeterminism; the paper does not isolate decoder sampling from runtime effects or agents' analytical choices. | target PASS; source PASS |
| OD-5 | grounded | Retained the plural-`V` inference for divergent auditor-accepted analyses, explicitly conditional on that auditor. | target PASS; source PASS |
| OD-6 | narrowed | Separated the final 33% compliance exclusions from the pilot hallucination/recall examples that motivated the auditor; the pilots are not identified as final rejected runs. | target PASS; source PASS |
| OD-7 | grounded | Retained the caution: persona prompts alter prior plausibility or the commission itself, so their comparison is not a meaning-preserving framing test. | target PASS; source PASS |
| OD-8 | narrowed | Distinguished settings fixed within a dataset × model × persona cell from the three datasets, four models, and five personas varied across the study. | target PASS; source PASS |
| RC-1 | grounded | Replaced the compact gloss with Maes's normalized distinction: one representation serves implementation and reasoning in procedural reflection; declarative reflection separates an explicit constraint representation from the procedural implementation. | target PASS; source PASS |
| RC-2 | grounded | Made Maes's explicit implementation-efficiency versus reasoning-suitability tradeoff its own sentence. | target PASS; source PASS |
| RC-3 | narrowed | Scoped bidirectional reasoning and action to the SOUL/Smalltalk construction and identified upping/downing as one mechanism, not a sufficient cause by itself. | target PASS; source PASS |
| RC-4 | narrowed | Replaced “moves values” with the source's distinction: data mapping makes foreign data appear native; protocol mapping makes receiving-side meta-operations applicable to their representations. | target PASS; source PASS |

## Grounded entries written

Ten Claims entries were appended through the checksum-guarded ingest mutation
path and each ingest passed `commonplace-validate`:

- `into-the-unknown-self-learning-large-language-models` — the paper's “what
  to learn” framing and PiU-based unknown-selection loop.
- `self-training-large-language-models-through-knowledge-detection` — the
  four-stage pipeline and the two filters' roles and placement before DPO.
- `prov-overview` — PROV's representation and interchange of production-related
  provenance, with no acquisition-time claim.
- `in-toto-farm-to-table-guarantees` — signed layouts, per-step link metadata,
  and client verification of the declared supply chain.
- `many-ai-analysts-one-dataset-agentic-data-science-multiverse` — one entry
  for the crossed design, auditor-retained cells, and divergent compliant
  results; one for the persona manipulations, pilot failures, and final pass
  rate.
- `prompt-stability-code-llms-emotion-personality-variations` — intended
  semantic/interface invariance, repeated-sample protocol, and the bounded
  performance–stability statistic.
- `maes-computational-reflection-1988` — procedural versus declarative
  reflection and the implementation/reasoning tradeoff.
- `wuyts-ducasse-2001-symbiotic-reflection` — the SOUL/Smalltalk construction
  and its upping/downing entity-transfer mechanism.
- `gybels-et-al-2006-inter-language-reflection` — data mapping versus protocol
  mapping in linguistic symbiosis.

All nine name-paired snapshots were present. Their canonical sources and exact
SHA-256 values matched the ingests, so no re-ingest or unavailable-source route
fired. A byte-level recheck confirmed that each ingest changed only inside its
`Claims` section.

## Validation and review

All four target notes and all nine changed ingests passed deterministic
validation without warnings. Source-conformance review ran under the `codex`
partition. Jobs `7993`, `7994`, and `7996` passed their seven pairs. Initial job
`7995` passed the multiverse pair but failed the PromptSE pair because the
repair introduced an ungrounded reference to the paper's four-quadrant result.
That attribution was deleted; replacement job `8001` passed both pairs. The
final source selector returned `targets: []` for all nine pairs.

## Cohort findings

Distribution: four grounded, ten narrowed, three contradicted-and-repaired,
and one retained local delta. No item was a false positive, unavailable, or a
literature handoff.

The multiverse ingest accumulated two entries, one about the experiment and
compliant dispersion and one about persona and auditor mechanics. They were
complementary rather than competing normalizations. The other eight ingests
received one entry each. No existing Claims entry was present, no entry was
reused, and no claim-identity ambiguity or need for a thinner intermediate node
appeared.
