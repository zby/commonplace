# RF-04 — Linked evidence is outside review freshness

**State:** open  
**Repair shape:** architecture decision and schema/runtime change  
**Severity:** high  
**Related:** [RF-05](./rf-05-quote-append-does-not-preserve-grounding-warrant.md), [RF-06](./rf-06-grounding-snapshot-invariants-are-not-enforced.md)

## Finding

Semantic criteria may require a worker to judge linked content. Job preparation
retains the link path, availability, and size, while the worker later reads the
live file. The exact linked bytes are neither captured nor registered as
freshness inputs. A judgment can therefore remain fresh after evidence that
determined it changes.

## Evidence

- [Review architecture](../../reference/review-architecture.md) deliberately
  limits a baseline to note and criterion and calls links reading context.
- [`resolve_note_markdown_links()`](../../../src/commonplace/review/job_prompt.py)
  records path and size, not content identity.
- [The generated prompt](../../../src/commonplace/review/protocol/prompt.py)
  tells grounding and consistency reviewers to follow those live paths.
- The linked-content intervention in
  [the evidence boundary](./evidence-boundary.md) changed the source's meaning
  without reselecting the pair.

## Why it matters

The actual judgment dependency set can be larger than the registered freshness
dependency set. Calling the complete assay snapshot-anchored then overstates
what can be reconstructed or invalidated.

## Provisional repair direction

Decide between capturing all criterion-authorized linked inputs before dispatch
and retaining a verified consumed-dependency set at finalization. Either design
must bind exact bytes to the evidence pair and define how changes reselect work.
Do not use unverified worker self-report as the sole identity source.

## Done when

- The exact linked versions that may determine a verdict are reconstructable.
- A material linked-content change stales or otherwise reopens the affected
  evidence pair.
- Prompt creation and worker reading cannot silently observe different versions.
- Generic links, ingests, and snapshot-required links have explicit behavior.
