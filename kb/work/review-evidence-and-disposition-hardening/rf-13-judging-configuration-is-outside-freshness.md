# RF-13 — Judging configuration is outside freshness identity

**State:** open  
**Repair shape:** configuration identity and migration design  
**Severity:** high  
**Related:** [RF-14](./rf-14-model-partitions-lack-equivalence-evidence.md), [RF-21](./rf-21-reviewer-system-prompt-has-no-consumer.md)

## Finding

Prompt rendering, protocol wrappers, system and ambient instructions, sampling
policy, and registry behavior can change verdicts without changing the note or
criterion. They are deliberately outside the freshness key. Documentation asks
for deliberate corpus-wide rereview or acknowledgement after a judgment-shifting
change, but the store records no configuration identity against which that work
can be selected or verified.

## Evidence

- [Review architecture](../../reference/review-architecture.md) excludes prompt
  scaffolding and says judgment-shifting changes require an operational rereview.
- [`freshness.py`](../../../src/commonplace/review/freshness.py) documents the
  exact two-input boundary.
- [The calibration proposal](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)
  names rendered prompt, system instructions, sampling, and repetition protocol
  as parts of the judging configuration and calls invalidation a missing trigger.

## Why it matters

Old baselines remain structurally fresh after a system upgrade that changes
judgments. A manual migration cannot prove completeness because neither old nor
new configuration has a stored identity.

## Provisional repair direction

Define a versioned effective judging-configuration fingerprint. Include only
inputs whose change can alter the contracted judgment, not every ambient process
detail. Store it with jobs and baselines, provide reverse selection by obsolete
configuration, and define when acknowledgement is permitted instead of rereview.

## Done when

- Every retained evidence pair names the judgment configuration that produced it.
- A configuration upgrade can deterministically list every affected baseline.
- Migration completion is queryable rather than a convention.
- Tests distinguish a formatting-only renderer change from a judgment-shifting
  configuration change.
