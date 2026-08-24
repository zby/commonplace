# Cleanup cohort 10a — frozen 2026-08-24

**Status: ready.** Frozen at repository `a91ed377`. Split from cohort 10 on
2026-08-24 to bound one agent's context; the original manifest's scope was
18 targets over 36 ingests.

**Run sequentially with [cohort 10b](./cohort-10b.md), never concurrently.**
Cohort 10 is a single connected component — every target shares an ingest with
another — so no parallel split of it exists. This cut minimizes the bridge to
**2 shared ingests**, but two agents appending to the same `Claims`
section can still lose an entry, since V1 ships no locking. The pair is disjoint
from every other cohort on both mutation axes.

Bridge ingests, shared with cohort 10b: `goedel-machines-schmidhuber`, `language-models-like-humans-show-content-effects-on-reasoning`.
Whichever half runs second will find incumbent entries there; reuse an adequate
one rather than appending a near-duplicate.

Scope: 9 targets, 20 ingests, 29 note-to-ingest pairs,
0.80 MB of snapshots. 2 ingests already carry Claims entries; the rest
are empty. An existing entry is a candidate for exact reuse, not a presumption
that a target use is supported.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `active-work-state-is-not-retrospective-memory-or-chat-history` | `6d49281b` | `claude-workstream-kit-fable-agent-scaffolding` |
| `checked-outcome-licenses-episode-retention-not-abstraction` | `e80970f4` | `an-enigma-of-artificial-reason-production-evaluation-gap-lrms`<br>`language-models-dont-always-say-what-they-think` |
| `context-contamination-operates-below-an-agents-compliance-reasoning` | `37726219` | `language-models-like-humans-show-content-effects-on-reasoning`<br>`semantic-leakage-lms-gonen` |
| `formal-systems-assess-explanatory-reach-through-causal-and-proof` | `0e5f3442` | `causal-inference-using-invariant-prediction`<br>`causal-learn-causal-discovery-in-python`<br>`dowhy-expressing-and-validating-causal-assumptions`<br>`goedel-machines-schmidhuber`<br>`the-risks-of-invariant-risk-minimization`<br>`towards-causal-representation-learning` |
| `parametric-reproduction-cannot-replace-an-authoritative-record` | `0e56dd1e` | `claude-workstream-kit-fable-agent-scaffolding`<br>`rome-locating-and-editing-factual-associations-in-gpt`<br>`we-should-take-text-optimization-more-seriously` |
| `reasoning-production-is-not-reasoning-evaluation` | `ba832e07` | `an-enigma-of-artificial-reason-production-evaluation-gap-lrms` |
| `scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier` | `fed3fc64` | `claude-workstream-kit-fable-agent-scaffolding`<br>`effective-harnesses-for-long-running-agents` |
| `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one` | `85e1f499` | `concept-bottleneck-models`<br>`language-models-dont-always-say-what-they-think`<br>`towards-faithfully-interpretable-nlp-systems` |
| `theory-mediated-learning-may-improve-sample-efficiency-under-shifts` | `b237ff15` | `causal-inference-using-invariant-prediction`<br>`concept-bottleneck-models`<br>`discoverphysics-benchmarking-llms-out-of-the-box-scientific`<br>`dreamcoder-wake-sleep-bayesian-program-learning`<br>`falsifybench-inductive-reasoning-rule-discovery-games`<br>`in-search-of-lost-domain-generalization`<br>`rome-locating-and-editing-factual-associations-in-gpt`<br>`the-risks-of-invariant-risk-minimization`<br>`towards-causal-representation-learning` |

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
