# Borrowable Features

## Decision

Do both experiments in parallel: try the full ARIS-shaped Research Wiki inside a workshop, and separately borrow individual lifecycle patterns into commonplace.

The full subsystem trial protects against premature decomposition: some value may come from the whole loop, not any one artifact. The incremental path protects against overfitting commonplace to an ML-research schema when a smaller convention would solve the general problem.

## Borrow Now

1. **Dynamic working README.** Generate or refresh a bounded orientation document for active workshops. ARIS calls this `query_pack.md`; in commonplace the better concept may be a separate working README that includes the question, current gaps, active claims, failed ideas, selected sources, experiments/probes, and open decisions. This is the most directly useful feature because it changes what future agents load.

2. **Failed ideas as first-class memory.** Failed ideas should not disappear into logs. For design work, knowing what not to retry is often more valuable than another source summary.

3. **Claim/experiment loop.** Active claims need states and links to probes. This fills the gap between ingest reports and durable structured claims.

4. **Lifecycle lint.** Add checks for stale claims, dead ideas, orphan source cards, open gaps without active ideas, and promoted artifacts that still appear as active.

5. **Mutation log.** Every helper-driven change should leave a receipt. This is cheap and improves recovery after compaction or handoff.

## Adapt Carefully

1. **Edges as source of truth.** A JSONL edge file is useful for workshop-local operational relationships, especially for generating query packs. It should not replace markdown links in durable library artifacts.

2. **Paper cards.** ARIS paper pages are useful, but in commonplace they should be workshop cards pointing to `kb/sources/` snapshots and ingest reports, not replacements for them.

3. **Gap map.** Useful for active investigations, but gaps should not become a permanent parallel taxonomy unless they promote into indexes or notes.

4. **Re-ideation triggers.** The triggers are promising: enough new sources, enough failed ideas, a contradiction, or an unaddressed gap. They should start as lint warnings or review prompts, not autonomous task creation.

5. **Stats command.** Counts for active claims, failed ideas, experiments, sources, edges, and stale items would help workshop reviews. Avoid making metrics into quality proxies.

## Do Not Borrow Directly

1. **Do not replace `kb/sources/`.** ARIS paper pages mix capture and interpretation. Commonplace intentionally separates immutable source capture from ingest analysis.

2. **Do not create a top-level `research-wiki/` peer to the KB.** The workflow belongs inside `kb/work/<workshop>/` unless it proves general enough to become a reference subsystem.

3. **Do not copy ARIS entity names as permanent collection types.** `Idea`, `Experiment`, and `Claim` are good workshop states, but durable commonplace artifacts already have their own type system.

4. **Do not rely on prose-only lifecycle rules.** ARIS's strongest implemented parts have helpers and generated receipts. If we borrow the lifecycle, it needs at least a small helper or deterministic lint.

5. **Do not promote every workshop claim.** The workshop needs a graveyard as much as a promotion path. Retired and invalidated claims are local memory, not necessarily library content.

## Feature Priority

| Priority | Feature | Why |
|---|---|---|
| 1 | Dynamic working README | Directly improves context loading for active work without making the canonical README volatile. |
| 2 | Failed idea ledger | Prevents repeated waste and captures negative learning. |
| 3 | Claim/experiment statuses | Gives lifecycle shape to claims before promotion. |
| 4 | Lifecycle lint | Makes stale or orphaned work visible. |
| 5 | Mutation log | Improves handoff and recovery with low cost. |
| 6 | Workshop edges file | Useful if working-README generation needs structured relationships. |
| 7 | Re-ideation triggers | Useful after the first manual lifecycle has evidence. |

## Strongest Design Constraint

The workshop map must be disposable. Its purpose is to help an active investigation complete and promote durable outputs. If it becomes a permanent shadow library, it has failed the commonplace workshop model.
