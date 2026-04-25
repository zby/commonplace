# Parallel Adoption Tracks

## Summary

Do not force an early choice between "use ARIS directly" and "borrow a few ideas." Run both paths in parallel.

The full ARIS-shaped path tests whether Research Wiki's value depends on the whole subsystem. The incremental path tests which mechanisms are general enough to become commonplace conventions.

## Track A: Full ARIS-Shaped Subsystem

Goal: try Research Wiki as a coherent subsystem, scoped under `kb/work/`, without redesigning it first.

Candidate location:

```text
kb/work/<workshop>/research-wiki/
  index.md
  log.md
  gap_map.md
  query_pack.md
  papers/
  ideas/
  experiments/
  claims/
  graph/edges.jsonl
```

What this preserves:

- ARIS's entity split: papers, ideas, experiments, claims.
- ARIS's relationship source of truth: `graph/edges.jsonl`.
- ARIS's volatile orientation artifact: `query_pack.md`.
- ARIS's mutation log and gap map.
- The possibility that the whole structure is useful as a subsystem, even if some parts are not broadly general.

Questions to answer:

- Does `query_pack.md` materially improve agent orientation in large workshops?
- Do `ideas/`, `experiments/`, and `claims/` stay useful, or do they become ceremony?
- Does `papers/` duplicate `kb/sources/`, or does it provide useful source cards for active work?
- Do structured edges pay for themselves compared with markdown links?
- Does the subsystem remain disposable at workshop closure?
- Is there a class of work where this should remain a named commonplace subsystem?

## Track B: Incremental Generalization

Goal: pull ARIS mechanisms into commonplace one at a time when they prove useful outside the full Research Wiki shape.

Candidate imports:

- `working-readme.md` as a volatile README variant for large workshops.
- Failed idea ledgers as durable negative memory during active work.
- Claim/experiment status loops before promotion into `kb/notes/`.
- Lifecycle lint for stale claims, dead ideas, orphan source cards, and open gaps.
- Mutation logs for helper-driven workshop changes.
- Reactivation triggers when new sources, contradictions, or unresolved gaps accumulate.

Generalization test:

- Can the idea apply to non-research workshops?
- Does it preserve the `kb/sources/` boundary?
- Does it reduce future agent context load?
- Does it create a promotion path into notes, instructions, references, or ADRs?
- Does it remain disposable when the workshop closes?

## How The Tracks Interact

Track A is the evidence generator. Use it to experience the whole lifecycle and discover which parts are load-bearing.

Track B is the promotion path. When a pattern from Track A proves useful beyond the subsystem, rewrite it in commonplace vocabulary and promote it into `kb/work/COLLECTION.md`, `kb/reference/`, or `kb/instructions/`.

Avoid two failure modes:

- **Premature trimming.** If we remove ARIS pieces before using the system, we may destroy the interaction that made it useful.
- **Permanent shadow library.** If the full subsystem accumulates durable knowledge that should live in `kb/sources/` or `kb/notes/`, it has escaped the workshop layer.

## Decision Points

After one or two real trials, decide:

- Keep Research Wiki as a named workshop subsystem.
- Replace it with the generalized investigation-map pattern.
- Keep only selected features such as `working-readme.md` and failed idea ledgers.
- Retire the experiment if the maintenance cost exceeds the orientation value.
