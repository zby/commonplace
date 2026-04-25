# Workshop: Research Wiki Integration

## Question

Can ARIS Research Wiki be used directly in commonplace, or should we adapt its classification and lifecycle patterns into our own workshop/source system?

## Why this workshop exists

ARIS's Research Wiki is the strongest part of [ARIS](../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) for commonplace purposes: it gives an active project a typed field map of papers, ideas, experiments, claims, gaps, and relationships, plus a generated `query_pack.md` that later skills must read before ideating. That is close to a missing middle layer in commonplace.

The question is not whether it replaces `kb/sources/`. It probably should not: [kb/sources](../../sources/COLLECTION.md) separates immutable snapshots from ingest analysis, while ARIS paper pages are already interpreted research-memory artifacts. The real question is whether ARIS gives us a better lifecycle for active investigations than our current workshop conventions.

## Working Materials

- [classification-comparison.md](./classification-comparison.md) - maps ARIS papers, ideas, experiments, claims, gaps, and edges against commonplace sources, notes, structured claims, reviews, and workshops.
- [lifecycle-analysis.md](./lifecycle-analysis.md) - analyzes the lifecycle ARIS enforces and where it exposes weaknesses in commonplace.
- [borrowable-features.md](./borrowable-features.md) - ranks features we should borrow, adapt, or reject.
- [parallel-adoption-tracks.md](./parallel-adoption-tracks.md) - keeps the full-subsystem experiment and one-by-one generalization path separate.
- [aris-artifact-inventory.md](./aris-artifact-inventory.md) - records what ARIS writes and how feasible it is to redirect into `kb/work/<somedir>/`.
- [integration-sketch.md](./integration-sketch.md) - proposes a minimal commonplace-shaped implementation path, including the static `README.md` / dynamic working-README split.

## Current Position

Do not decide too early between adoption and extraction. Run two paths in parallel:

1. **Full ARIS-shaped subsystem trial.** Preserve the Research Wiki structure under a workshop and see whether the whole design has value as a coherent subsystem.
2. **Incremental generalization.** Borrow individual ARIS ideas into commonplace one by one: working READMEs, failed idea ledgers, claim/experiment loops, lifecycle lint, mutation logs, and reactivation triggers.

The boundary still matters:

- `kb/sources/` remains the provenance layer: immutable snapshots and ingest reports.
- `kb/notes/` remains the durable theory layer: promoted, transferable claims.
- `kb/work/<workshop>/` is the experimental surface where ARIS can either remain a subsystem or yield generalized commonplace conventions.

## What Would Close This Workshop

This workshop closes when it produces one of:

1. A note about active research lifecycle as the missing piece between sources and notes.
2. An update to [kb/work/COLLECTION.md](../COLLECTION.md) describing an optional investigation-map pattern.
3. A reference or instruction spec for a helper that generates workshop working READMEs and lifecycle lint.

## Grounding

- [ARIS review](../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) - derived-from: local review of the system and Research Wiki implementation.
- [Sources collection](../../sources/COLLECTION.md) - contrasts: source snapshots are provenance artifacts, not active research-memory pages.
- [A functioning KB needs a workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - grounds: workshops are temporal artifacts whose value is consumed and promoted.
- [Lifecycle management workshop](../lifecycle-management/README.md) - depends-on: the broader open problem this integration sharpens.
