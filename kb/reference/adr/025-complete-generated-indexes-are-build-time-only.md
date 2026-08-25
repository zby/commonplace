---
description: "Complete generated listings move to ProperDocs build time; agents discover through curated heads plus scoped path-and-description searches with a 50–250-character soft description warning"
type: ../types/adr.md
tags: []
status: accepted
---

# 025-Complete generated indexes are build-time only; agents read curated heads plus scoped rg

**Status:** accepted
**Date:** 2026-06-09

## Context

- Generated navigation is committed and read whole by agents: the per-collection `dir-index.md` and the per-tag `## Other tagged notes` tail. `cp-skill-connect` (per [003-connect-skill-discovery-strategy](./003-connect-skill-discovery-strategy.md)) reads `kb/notes/dir-index.md` first. A full index read costs tens of KB before any candidate body is selected; under sub-agent decomposition, per-fork load then grows with total collection size rather than with the task.
- These complete listings are pure denormalization: every title and description already lives in the note's own frontmatter.
- The root cause is an access-mode asymmetry: an agent reads an index whole (linear cost into bounded context, every byte counted), while a human skims, scrolls, and Ctrl-Fs (sublinear). The same complete listing is context debt for the agent and a convenience for the human — which is why we design for the first-time human except where [access cost dominates](../../notes/design-for-the-first-time-human-except-on-access-cost.md).
- ADR 003 bet that index-first discovery would stay viable by keeping the collection curated and loading the index in portions. Collection growth has made the complete-index read the dominant per-fork cost, so that bet no longer holds.

## Decision

Complete generated listings are build-time-only; the agent read path is curated heads plus scoped rg.

1. Retire complete generated listings from git and the agent read path — both the per-collection `dir-index.md` and the per-tag `## Other tagged notes` tail.
2. Regenerate them at ProperDocs build time for human readers, where browser scroll and find restore sublinear access. One source of truth (note frontmatter), two materializations.
3. Keep curated heads committed at every scope: directory `README.md` / `COLLECTION.md`, and the editorial body of each tag index. The tag index is the tag's README; its generated tail is the detachable part.
4. Agents discover via curated heads plus scoped `rg` (by tag, listing the matching files' descriptions; by keyword, over a scoped path); add no new query command, because scoped rg recovers the operative part of the retired index. Codifying the recipes into a `commonplace-*` command is deferred until a recurring failure justifies it.
5. Colocation is conditional on weight: a small tag keeps its short generated list colocated under the curated head; a popular tag detaches it, because a curated index is an agent read surface and must stay context-feasible. *(Refined by [ADR 026](./026-tag-readme-type-with-completeness-and-coverage-marks.md): nothing generated is committed at any size.)*

This supersedes ADR 003's primary-discovery decision (read `dir-index.md` first). 003's surviving element — curated focused indexes as a discovery surface — is retained as the curated-heads path; complete-index reads are removed from standard connect discovery.

### Amendment: description upper warning (2026-07-28)

The shared description warning band is 50–250 characters, raising the former upper warning from 200. The ceiling is an allowance, not a target: authors should still use the shortest description that changes a read/skip decision, and descriptions above 250 warn rather than fail.

The inherited 200-character ceiling had been justified partly by the cost of complete description listings, but this ADR removed those listings from the agent path. A controlled retrieval assay compared independently written variants under allowances from 120 to 300 characters (44 trials per allowance): 250 was the shortest allowance with no false skips or irrelevant opens; 300 added no retrieval benefit and exceeded the assay's token budget at an 80-result slice. The only observed benefit over shorter variants came from distinguishing a same-title source snapshot from its ingest analysis, so the evidence warrants a soft global warning—not a hard maximum or a recommendation that ordinary descriptions approach 250.

The operativity path has two parts. The shared note schema is consumed by `commonplace-validate`, which warns outside the band; writing instructions teach the same allowance before drafting. Agents then consume the resulting descriptions through the scoped path-plus-description searches established by this ADR. Whether explicit artifact-role display can resolve same-title and same-lineage collisions more cheaply than description headroom remains open.

## Consequences

Easier:
- Per-fork load scales with the task, not the collection: write, connect, and ingest stop paying tens of KB of denormalized index on every fork.
- Adding a note no longer requires keeping a heavy committed index current for agents (003's maintenance burden); the human site regenerates from source.

Harder:
- `cp-skill-connect` standard discovery drops complete-index reads (curated heads plus scoped rg; broad scans reserved for deep mode).
- The ProperDocs build becomes responsible for human-facing inventories.

Risks / watch:
- Scoped rg has a footgun: a tag that matches zero files can make the piped search fall back to the whole repo. The documented recipe guards against it; recurring trips would be the signal to codify a command.
- rg yields `path + description`, not the human H1 title; the path stands in for the title in triage. If title-in-output proves necessary, that is the case a command would justify.
- Description quality stays load-bearing (inherited from 003).
- Raising the soft ceiling permits up to 50 more characters per pointer. The assay bounded that cost at its observed p95 and 80-result conditions, but the largest current tag slice still needs candidate-set control rather than longer per-item compression.

Deferred (mechanism, not direction):
- ProperDocs generation mechanism: a `commonplace-refresh-indexes --for-build` mode the hook calls, or a dedicated plugin (must emit both the directory inventory and the per-tag listing).
- Curated-index weight reporting plus soft/hard thresholds (bytes vs entry count; scope).
- Whether curated indexes must declare focused-routing vs archival, or whether "curated = focused" suffices.

## Links

- [003-connect-skill-discovery-strategy](./003-connect-skill-discovery-strategy.md) — supersedes: this replaces 003's index-first primary discovery while retaining its curated-focused-index surface
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — rests-on: the per-fork cost of a whole-index read is what makes retiring it worthwhile
- [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md) — rests-on: per-fork load is the boundary this decision optimizes
- [feasibility-is-the-heaviest-forks-net-load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) — rests-on: feasibility is set by the heaviest fork's net load, which the complete-index read inflates
- [index completeness does not determine editorial orientation](../../notes/index-completeness-does-not-determine-editorial-orientation.md) — rests-on: why curated heads stay committed while generated listings move to build time
- [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) — procedure: the discovery skill whose standard read path this decision rewrites
