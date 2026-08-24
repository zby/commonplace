# Cleanup cohort 10b — frozen 2026-08-24

**Status: ready.** Frozen at repository `a91ed377`. Split from cohort 10 on
2026-08-24 to bound one agent's context; the original manifest's scope was
18 targets over 36 ingests.

**Run sequentially with [cohort 10a](./cohort-10a.md), never concurrently.**
Cohort 10 is a single connected component — every target shares an ingest with
another — so no parallel split of it exists. This cut minimizes the bridge to
**2 shared ingests**, but two agents appending to the same `Claims`
section can still lose an entry, since V1 ships no locking. The pair is disjoint
from every other cohort on both mutation axes.

Bridge ingests, shared with cohort 10a: `goedel-machines-schmidhuber`, `language-models-like-humans-show-content-effects-on-reasoning`.
Whichever half runs second will find incumbent entries there; reuse an adequate
one rather than appending a near-duplicate.

Scope: 9 targets, 18 ingests, 27 note-to-ingest pairs,
1.41 MB of snapshots. 0 ingests already carry Claims entries; the rest
are empty. An existing entry is a candidate for exact reuse, not a presumption
that a target use is supported.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `a-proposal-selection-loop-requires-search-evaluation-and-retention` | `5c6cfc0e` | `goedel-machines-schmidhuber` |
| `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | `f32b01bd` | `autogenesis-a-self-evolving-agent-protocol`<br>`continual-harness-online-adaptation-foundation-agents`<br>`darwin-godel-machine-open-ended-evolution-self-improving-agents`<br>`huxley-godel-machine-human-level-coding-agent-development`<br>`hyperagents`<br>`self-harness-harnesses-that-improve-themselves`<br>`self-improving-ai-coding-agents-through-accumulated-rules` |
| `brainstorming-maintainability-oracles-for-agentic-development` | `9c3a8378` | `agentic-code-reasoning`<br>`huxley-godel-machine-human-level-coding-agent-development`<br>`towards-automating-eval-engineering-2079976006644072796`<br>`why-software-factories-fail-slopcodebench-2081797628552270027` |
| `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | `68fdead9` | `agent-optimizers-compound-terminal-bench`<br>`harness-updating-is-not-harness-benefit`<br>`hyperagents`<br>`poetiq-perspective-on-recursive-self-improvement` |
| `computationally-directed-self-improvement-is-a-reallocation` | `933f5793` | `poetiq-perspective-on-recursive-self-improvement` |
| `epiplexity-by-example-what-entropy-and-complexity-miss` | `ae35ffc9` | `from-entropy-to-epiplexity-rethinking-information-computational` |
| `goedel-machines-are-a-proof-governed-case-of-self-modification` | `1b97b5ed` | `darwin-godel-machine-open-ended-evolution-self-improving-agents`<br>`goedel-machines-schmidhuber`<br>`huxley-godel-machine-human-level-coding-agent-development` |
| `structured-prompt-gains-do-not-establish-distribution-selection` | `1605d875` | `agentic-code-reasoning`<br>`from-entropy-to-epiplexity-rethinking-information-computational`<br>`language-models-like-humans-show-content-effects-on-reasoning` |
| `verifiable-subroles-before-reviewer-identity` | `2a43d52a` | `agentic-code-reasoning`<br>`beyond-not-novel-enough-llm-assisted-scholarly-critique`<br>`towards-automating-scientific-review-google-paper-assistant` |

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
