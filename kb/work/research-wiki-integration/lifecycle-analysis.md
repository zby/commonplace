# Lifecycle Analysis

## Summary

ARIS Research Wiki is valuable because it treats research memory as a lifecycle, not just a filing scheme. Commonplace has good artifact destinations but weak transitions. We know where snapshots, ingest reports, notes, reviews, and instructions belong, but the middle states are under-specified: candidate, tested, failed, stale, superseded, reactivated, and promoted.

That is the lifecycle weakness this workshop should address.

## Lifecycle ARIS Enforces

ARIS Research Wiki defines this practical loop:

1. `init` creates the wiki structure, index, gap map, query pack, graph, and mutation log.
2. `ingest` creates paper pages, deduplicates arXiv IDs/slugs, rebuilds generated views, and appends log receipts.
3. Agents add explicit edges in `graph/edges.jsonl`, making relationships queryable and auditable.
4. `query_pack.md` is loaded before ideation, so future work starts from compressed project memory.
5. New ideas are written as first-class artifacts, with failed ideas preserved as a high-value banlist.
6. Experiments update ideas and claims through `tested_by`, `supports`, and `invalidates` relationships.
7. `lint` checks orphan pages, stale claims, contradictions, missing connections, dead ideas, and sparse pages.
8. Re-ideation is triggered by events such as enough new papers, enough failed or partial ideas, a new contradiction, or a new gap with no idea.

The important mechanism is not the exact schema. It is the closed loop from source intake to ideation to experiment to claim update to reactivation.

## Implementation Reality

The ARIS helper code is strongest for paper ingest, deduplication, index rebuilds, dynamic orientation generation, stats, and mutation logging. The idea/experiment/claim lifecycle is specified mostly in skill prose. That matters for borrowing: we should not copy the repo expecting a complete lifecycle engine.

Use ARIS as a design pattern, not a dependency.

## Commonplace Lifecycle Gap

Commonplace has stable endpoints:

- `kb/sources/` preserves and analyzes external material.
- `kb/notes/` holds durable transferable claims and theory.
- `kb/reference/` documents the shipped system.
- `kb/instructions/` holds procedures.
- `kb/work/` holds temporal working artifacts.

The missing part is explicit state movement inside `kb/work/` and between `kb/work/` and the library. Current `status: seedling/current/outdated` is too coarse for active investigations. It says how mature a library artifact is, but not what should happen next to a candidate idea, failed hypothesis, stale claim, unresolved contradiction, or experiment result.

The [lifecycle-management](../lifecycle-management/README.md) workshop already names promotion, maturation, retirement, and partial extraction as open problems. ARIS adds a concrete pattern for the active middle: keep an investigation map that agents must consult and lint.

## Commonplace-Shaped Lifecycle

For an ARIS-inspired workshop subsystem, use these states:

| Entity | Candidate states | Promotion target |
|---|---|---|
| Source candidate | seen -> snapshotted -> ingested -> filed/promoted/ignored | `kb/sources/` snapshot and ingest report |
| Idea | proposed -> selected -> tested -> supported/invalidated/parked -> promoted/retired | note, instruction change, ADR, or retained failure record until workshop closes |
| Experiment/probe | planned -> running -> concluded -> interpreted | review result, validation change, note evidence, instruction update |
| Claim | reported -> under-test -> supported/invalidated/qualified -> promoted/retired | `kb/notes/` note or `structured-claim` |
| Gap | open -> addressed-by idea -> resolved/superseded | note gap section, index entry, or future workshop |
| Edge | proposed -> active -> promoted/dropped | markdown link in durable artifact if promoted |

## What Should Be Enforced

The enforcement should be light but real:

- Every mutation appends to a workshop `log.md`.
- Every active claim must have a status and either evidence, an experiment, or a stale marker.
- Failed ideas stay visible until the workshop closes or they are explicitly retired.
- Query packs have hard budgets, so active context does not grow without bound.
- Lint reports missing edges, dead ideas, stale claims, unconnected source cards, and open gaps with no idea.
- Promotion requires a target: note, structured claim, instruction, reference, ADR, source report, or explicit no-promote decision.

## Main Lesson

ARIS does not make our sources system obsolete. It shows that source intake is only one phase of a larger research lifecycle. Commonplace should keep its source/library boundary, then add an optional lifecycle map inside workshops for investigations that need to remember what has been tried, what failed, and what should be activated next.
