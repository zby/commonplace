# Claims-shape evidence

Two source-first reconstructions and blind whole-section checks fixed the V1
shape.

## Pirolli

Source ingest:
[Pirolli proximal information scent](../../sources/pirolli-proximal-information-scent-distal-content.ingest.md).
Verified snapshot SHA-256:
`dcbc565308e0a9eab683087f729137d462f8b6f0d5a8808f989b10b3095e1da2`.

Two entries were enough to separate the proximal-scent/link-choice mechanism
from the broader value-versus-cost hypothesis. A blind verifier rejected the
claim that follow/skip is the source's fundamental navigation unit, required
narrowing of the proposed pointer-cost and surrounding-context formulations,
and found no support for a context-quantity/navigation-cost claim.

## Agent Workflow Memory

Source ingest:
[Agent Workflow Memory](../../sources/agent-workflow-memory.ingest.md).
Verified snapshot SHA-256:
`470b8ee461cb933d48a4eab1f53643baeb247e8b909c50c9d26a9cc6e4cbe0bd`.

Five entries covered one method claim and four benchmark claims. The blind
check supported two bounded quantitative comparisons, narrowed two broader
claims, and caught a contradiction between source prose and table values.

## Decisions supported

- Whole-section reading worked without IDs or anchors.
- The normalized claim must be paired with exact source language.
- Each extract needs its adjacent human-resolvable location; the pair may
  repeat within an entry.
- Scope and limitation prevent thematic overlap from being mistaken for
  support.
- Source-to-ingest reconstruction and note-to-ingest judgment should remain
  separate contexts.

## Retained semantic acceptance cases

Run these against fixture copies, not the live ingests. Construct their Claims
sections from the checksum-matching local snapshots through the grounding
instruction. Then give the source-review worker only the candidate artifact and
the resulting ingest criterion. Exact prose may vary; the dispositions may not.

### Pirolli: thematic overlap must not become support

The reconstructed Claims section must let the reviewer distinguish these uses:

- `pass`: proximal information-scent cues provide concise information about
  unavailable distal content and inform source-selection judgments;
- `fail`: follow/skip is the fundamental unit of navigation;
- `fail`: more surrounding pointer context makes the navigation decision
  cheaper; and
- `fail`: the source establishes that surrounding context avoids loading the
  target as the mechanism that makes navigation tractable.

The last three require narrowing or a separate local transfer argument. A
reviewer that passes them from topical similarity fails the case.

### Agent Workflow Memory: tables bound quantitative claims

The reconstructed Claims section must retain enough table context to produce:

- `pass`: on Mind2Web cross-domain, `AWMonline` reports 35.5 step success and
  `AWMoffline` 32.6;
- `pass`: on Mind2Web cross-task, text workflows report 45.4 step success versus
  45.1 for code workflows, while full task success is 3.6 versus 4.8; and
- `fail`: AWM and AWM-as-action have the same 3.2 full task success.

The final statement follows the source prose but contradicts Table 9, which
reports 4.8 for AWM and 3.6 for AWM-as-action. Grounding must expose that
conflict rather than silently choosing the flattering sentence.
