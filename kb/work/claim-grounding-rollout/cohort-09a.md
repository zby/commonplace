# Cleanup cohort 09a — frozen 2026-08-24

**Status: ready.** Frozen at repository `a91ed377`. Split from cohort 09 on
2026-08-24 to bound one agent's context; the original manifest's scope was
15 targets over 20 ingests.

**Run sequentially with [cohort 09b](./cohort-09b.md), never concurrently.**
Cohort 09 is a single connected component — every target shares an ingest with
another — so no parallel split of it exists. This cut minimizes the bridge to
**2 shared ingests**, but two agents appending to the same `Claims`
section can still lose an entry, since V1 ships no locking. The pair is disjoint
from every other cohort on both mutation axes.

Bridge ingests, shared with cohort 09b: `co-harness-co-evolving-harness-and-model-weights`, `meta-harness-end-to-end-optimization-of-model-harnesses`.
Whichever half runs second will find incumbent entries there; reuse an adequate
one rather than appending a near-duplicate.

Scope: 7 targets, 11 ingests, 19 note-to-ingest pairs,
0.96 MB of snapshots. 3 ingests already carry Claims entries; the rest
are empty. An existing entry is a candidate for exact reuse, not a presumption
that a target use is supported.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `a-retrieval-miss-is-a-local-reflective-path-failure` | `6cd511d5` | `memento-skills-let-agents-design-agents` |
| `an-experiment-identifies-only-the-contrast-it-actually-runs` | `b516e373` | `harness-if-instruction-following-across-instruction-surfaces`<br>`llm-agents-are-not-always-faithful-self-evolvers`<br>`memento-skills-let-agents-design-agents`<br>`meta-harness-end-to-end-optimization-of-model-harnesses` |
| `claw-learning-loops-must-improve-action-capacity-not-just-retrieval` | `8687d14d` | `koylanai-personal-brain-os`<br>`llm-agents-are-not-always-faithful-self-evolvers`<br>`simon-willison-karpathy-claws` |
| `diagnostic-richness-constrains-outer-loop-learning-quality` | `d01fbbd4` | `meta-harness-end-to-end-optimization-of-model-harnesses` |
| `process-structure-and-output-structure-are-independent-levers` | `508d6695` | `cedar-grpo-process-aware-rl-abductive-reasoning`<br>`verbalizable-representations-global-workspace-llms` |
| `readable-artifact-loop-is-the-tractable-unit-for-continual-learning` | `83b4779d` | `co-harness-co-evolving-harness-and-model-weights`<br>`memento-skills-let-agents-design-agents`<br>`symbolic-learning-enables-self-evolving-agents` |
| `treat-continual-learning-as-representational-form-coevolution` | `2e356187` | `co-harness-co-evolving-harness-and-model-weights`<br>`memento-skills-let-agents-design-agents`<br>`symbolic-learning-enables-self-evolving-agents`<br>`verbalizable-representations-global-workspace-llms`<br>`wikipedia-bitter-lesson` |

## Source-blind claim inventory

Pending. Before opening any listed ingest or snapshot, replace this paragraph
with one table row per load-bearing source-dependent use:

`ID | target | claim as frozen | source-side need`

## Source-demand plan and grounding record

Pending. After the complete inventory is saved, group its rows by ingest. For
each source-side need, record the incumbent Claims entry reused or the new entry
appended, plus checksum and validation results. Do not begin target repair until
every source-side need for that target is grounded or has a named blocker.

## Completion record

Pending. Record one row per claim use:

`ID | disposition | target change | validation and source-review result`

## Identity and accumulation observation

Pending. Record reuse, similar-entry accumulation, ambiguous selection,
disputed entries, or pressure for claim IDs or reconciliation. Distinguish
scope pressure in a target from identity pressure in a Claims section.
