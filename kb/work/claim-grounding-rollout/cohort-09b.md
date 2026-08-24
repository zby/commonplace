# Cleanup cohort 09b — frozen 2026-08-24

**Status: ready.** Frozen at repository `a91ed377`. Split from cohort 09 on
2026-08-24 to bound one agent's context; the original manifest's scope was
15 targets over 20 ingests.

**Run sequentially with [cohort 09a](./cohort-09a.md), never concurrently.**
Cohort 09 is a single connected component — every target shares an ingest with
another — so no parallel split of it exists. This cut minimizes the bridge to
**2 shared ingests**, but two agents appending to the same `Claims`
section can still lose an entry, since V1 ships no locking. The pair is disjoint
from every other cohort on both mutation axes.

Bridge ingests, shared with cohort 09a: `co-harness-co-evolving-harness-and-model-weights`, `meta-harness-end-to-end-optimization-of-model-harnesses`.
Whichever half runs second will find incumbent entries there; reuse an adequate
one rather than appending a near-duplicate.

Scope: 8 targets, 11 ingests, 18 note-to-ingest pairs,
0.30 MB of snapshots. 1 ingests already carry Claims entries; the rest
are empty. An existing entry is a candidate for exact reuse, not a presumption
that a target use is supported.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `evaluation-automation-is-phase-gated-by-comprehension` | `ae340da3` | `meta-harness-end-to-end-optimization-of-model-harnesses` |
| `frontloading-spares-execution-context` | `d116e1b4` | `machine-studying` |
| `instantiation-alone-cannot-model-agent-learning-across-sessions` | `4525afe5` | `erlang-compilation-and-code-loading`<br>`erlang-release-handling`<br>`fast-properties-in-v8`<br>`machine-studying`<br>`metaobject-protocols-why-we-want-them-and-what-else-they-can-do`<br>`monkey-patch` |
| `learning-inside-a-fixed-decomposition-inherits-its-mistakes` | `8a525199` | `acm-agentic-context-management-for-long-horizon-tasks`<br>`co-harness-co-evolving-harness-and-model-weights` |
| `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem` | `344a3ce7` | `position-ai-agents-in-scientific-teams-as-human-agent-systems` |
| `memory-design-adds-operational-axes-to-artifact-analysis` | `51cf0d71` | `machine-studying` |
| `retained-artifacts-enable-persistent-deployment-time-adaptation` | `c858696e` | `machine-studying`<br>`openclaw-rl-train-any-agent-simply-by-talking` |
| `the-deployed-system-not-the-model-is-the-unit-of-learning` | `d239761d` | `co-harness-co-evolving-harness-and-model-weights`<br>`machine-studying`<br>`meta-harness-end-to-end-optimization-of-model-harnesses`<br>`position-ai-agents-in-scientific-teams-as-human-agent-systems` |

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
