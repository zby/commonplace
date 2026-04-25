# Classification Comparison

## Summary

ARIS Research Wiki classifies active research objects. Commonplace classifies knowledge artifacts by provenance, register, and durability. That difference matters.

ARIS's `Paper`, `Idea`, `Experiment`, and `Claim` are not replacements for commonplace `snapshot`, `ingest-report`, `note`, or `structured-claim`. They are workflow-state objects: things an active investigation needs to remember so the next agent does not rediscover the same literature, revive a failed idea, or forget which experiment changed which claim.

## Mapping

| ARIS object | ARIS role | Closest commonplace object | Fit | Integration decision |
|---|---|---|---|---|
| `Paper` | Interpreted research-paper page with metadata, thesis, gap, method, results, limitations, claims, and relevance | `snapshot` + `ingest-report` + maybe `source-review` | Partial | Do not replace sources. Keep snapshots immutable; optionally create workshop paper cards that point at source artifacts. |
| `Idea` | Candidate research direction, including failed ideas and outcomes | Workshop note, task, or seed for a future note | Missing | Borrow directly as a workshop entity. Notes are too durable and too committed for live ideas. |
| `Experiment` | Concrete test or run that updates ideas and claims | Review run, test result, probe, or workshop log | Missing | Borrow as a workshop entity for methodology experiments, review probes, and validation trials. |
| `Claim` | Testable scientific claim with evidence status and experiment links | `structured-claim`, title-as-claim note, or extracted source claim | Partial | Split into two layers: workshop claim ledger while under test; promote to `structured-claim` only when durable. |
| `Gap` | Open problem that seeds ideas and re-ideation | Index gap, open question, TODO, workshop question | Missing as entity | Borrow lightly as a workshop entity or section, especially for query packs. |
| `edges.jsonl` | Source of truth for typed relationships | Markdown links plus link labels | Partial | Borrow for workshop-local operational edges; do not replace durable markdown links in library artifacts. |
| `query_pack.md` | Generated bounded context for ideation | Indexes, descriptions, review bundles | Strong new fit | Borrow as a workshop context artifact. |

## Classification Difference

Commonplace's durable classifications answer: what kind of artifact is this, what register governs it, and how should a reader cite or maintain it?

ARIS's Research Wiki classifications answer: what phase object is this in the research loop, what can act on it next, and what must later agents not forget?

That is why `Idea` and `Experiment` are the important imports. They are lifecycle-bearing entities, not library classifications. Commonplace currently has strong places for source evidence and stable claims, but weak places for "we considered this", "we tried this", "this failed", "this claim is under test", and "this gap should trigger new ideation after enough evidence changes".

## Paper Versus Source

ARIS paper pages combine capture, interpretation, and operational relevance. That is useful inside one project, but it blurs a boundary commonplace deliberately keeps clean.

In commonplace:

- A source snapshot preserves what was captured.
- An ingest report records what the source contributes.
- A note carries transferable theory extracted from one or more sources.
- A workshop artifact can hold temporary interpretation while the investigation is active.

So the equivalent of an ARIS `Paper` should not be one file. It should be a workshop paper card that references `kb/sources/<snapshot>` and `kb/sources/<snapshot>.ingest.md`, then records only the investigation-specific fields that should not be promoted yet.

## Claim Versus Note

ARIS claims are experimentally live. Commonplace notes are durable commitments, and `structured-claim` files are developed arguments with evidence and reasoning.

That means ARIS `Claim` should map to a staging ledger before it maps to `kb/notes/`. A workshop claim can be `reported`, `under-test`, `supported`, `invalidated`, `qualified`, or `promoted`. Only after promotion should it become a library note or structured claim. This keeps the library from accumulating half-tested assertions while still letting the workshop reason explicitly over claims.

## Edge Semantics

ARIS edge labels are operational:

- `inspired_by`
- `tested_by`
- `supports`
- `invalidates`
- `addresses_gap`
- `supersedes`
- `extends`
- `contradicts`

Commonplace link labels are reader-facing semantic contracts. They explain why a durable reader should follow a link. ARIS edges explain what the workflow should do next.

Use ARIS-style edges inside a workshop. Promote only the relationships that survive into library artifacts as normal markdown links with commonplace labels.
