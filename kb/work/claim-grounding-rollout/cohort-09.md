# Cleanup cohort 09 — frozen 2026-08-24

**Status: ready.** Frozen at repository `a91ed377`.

This is the smaller of the two residual high-connectivity components. Its notes
and ingests are disjoint from cohorts 08 and 10 on both mutation axes. One agent
owns the complete component and works it in the inventory, grounding, and
target-repair phases defined by the dispatch prompt.

Scope: 15 targets, 20 ingests, 37 note-to-ingest pairs, 1.13 MiB of snapshots.
Four ingests already contain five Claims entries between them; sixteen have an
empty Claims section. Existing entries are candidates for exact reuse, not a
presumption that a target use is supported.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `a-retrieval-miss-is-a-local-reflective-path-failure` | `6cd511d5` | `memento-skills-let-agents-design-agents` |
| `an-experiment-identifies-only-the-contrast-it-actually-runs` | `b516e373` | `harness-if-instruction-following-across-instruction-surfaces`<br>`llm-agents-are-not-always-faithful-self-evolvers`<br>`memento-skills-let-agents-design-agents`<br>`meta-harness-end-to-end-optimization-of-model-harnesses` |
| `claw-learning-loops-must-improve-action-capacity-not-just-retrieval` | `8687d14d` | `koylanai-personal-brain-os`<br>`llm-agents-are-not-always-faithful-self-evolvers`<br>`simon-willison-karpathy-claws` |
| `diagnostic-richness-constrains-outer-loop-learning-quality` | `d01fbbd4` | `meta-harness-end-to-end-optimization-of-model-harnesses` |
| `evaluation-automation-is-phase-gated-by-comprehension` | `ae340da3` | `meta-harness-end-to-end-optimization-of-model-harnesses` |
| `frontloading-spares-execution-context` | `d116e1b4` | `machine-studying` |
| `instantiation-alone-cannot-model-agent-learning-across-sessions` | `4525afe5` | `erlang-compilation-and-code-loading`<br>`erlang-release-handling`<br>`fast-properties-in-v8`<br>`machine-studying`<br>`metaobject-protocols-why-we-want-them-and-what-else-they-can-do`<br>`monkey-patch` |
| `learning-inside-a-fixed-decomposition-inherits-its-mistakes` | `8a525199` | `acm-agentic-context-management-for-long-horizon-tasks`<br>`co-harness-co-evolving-harness-and-model-weights` |
| `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem` | `344a3ce7` | `position-ai-agents-in-scientific-teams-as-human-agent-systems` |
| `memory-design-adds-operational-axes-to-artifact-analysis` | `51cf0d71` | `machine-studying` |
| `process-structure-and-output-structure-are-independent-levers` | `508d6695` | `cedar-grpo-process-aware-rl-abductive-reasoning`<br>`verbalizable-representations-global-workspace-llms` |
| `readable-artifact-loop-is-the-tractable-unit-for-continual-learning` | `83b4779d` | `co-harness-co-evolving-harness-and-model-weights`<br>`memento-skills-let-agents-design-agents`<br>`symbolic-learning-enables-self-evolving-agents` |
| `retained-artifacts-enable-persistent-deployment-time-adaptation` | `c858696e` | `machine-studying`<br>`openclaw-rl-train-any-agent-simply-by-talking` |
| `the-deployed-system-not-the-model-is-the-unit-of-learning` | `d239761d` | `co-harness-co-evolving-harness-and-model-weights`<br>`machine-studying`<br>`meta-harness-end-to-end-optimization-of-model-harnesses`<br>`position-ai-agents-in-scientific-teams-as-human-agent-systems` |
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
