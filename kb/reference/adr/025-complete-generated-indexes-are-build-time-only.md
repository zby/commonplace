---
description: Complete generated listings (the per-collection dir-index and the per-tag generated tail) retire from git and the agent read path and are regenerated at mkdocs build time for human readers, while agents discover via committed curated heads plus scoped rg; supersedes ADR 003's index-first connect discovery, and adds no new query command because scoped rg recovers what the retired index gave.
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
2. Regenerate them at mkdocs build time for human readers, where browser scroll and find restore sublinear access. One source of truth (note frontmatter), two materializations.
3. Keep curated heads committed at every scope: directory `README.md` / `COLLECTION.md`, and the editorial body of each tag index. The tag index is the tag's README; its generated tail is the detachable part.
4. Agents discover via curated heads plus scoped `rg`; add no new query command, because scoped rg recovers the operative part of the retired index. Documented recipes: by tag, `rg -l '^tags:.*\bTAG\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` (the `xargs -r` guard prevents an empty match from falling back to a whole-repo search); by keyword, `rg '^description:' <scoped path>`. Codifying these into a `commonplace-*` command is deferred until a recurring failure justifies it.
5. Colocation is conditional on weight: a small tag keeps its short generated list colocated under the curated head; a popular tag detaches it, because a curated index is an agent read surface and must stay context-feasible.

This supersedes ADR 003's primary-discovery decision (read `dir-index.md` first). 003's surviving element — curated focused indexes as a discovery surface — is retained as the curated-heads path; complete-index reads are removed from standard connect discovery.

## Consequences

Easier:
- Per-fork load scales with the task, not the collection: write, connect, and ingest stop paying tens of KB of denormalized index on every fork.
- Adding a note no longer requires keeping a heavy committed index current for agents (003's maintenance burden); the human site regenerates from source.

Harder / migration:
- `git rm` plus gitignore the ~50 committed `dir-index.md` files; strip the committed generated tail from tag indexes.
- `cp-skill-connect` standard discovery is rewritten to drop complete-index reads (curated heads plus scoped rg; broad scans reserved for deep mode).
- Reference sweep: `navigation.md`, `CLAUDE.md` Key Indexes, and any README or curated index that links to a `dir-index.md`.
- The mkdocs build becomes responsible for human-facing inventories.

Risks / watch:
- Scoped rg has a footgun: a tag that matches zero files makes `xargs` run rg with no path argument, which searches the whole repo. Mitigated by `xargs -r`; recurring trips would be the signal to codify a command.
- rg yields `path + description`, not the human H1 title; the path stands in for the title in triage. If title-in-output proves necessary, that is the case a command would justify.
- Description quality stays load-bearing (inherited from 003).

Deferred (mechanism, not direction):
- mkdocs generation mechanism: a `commonplace-refresh-indexes --for-build` mode the hook calls, or a dedicated plugin (must emit both the directory inventory and the per-tag listing).
- Curated-index weight reporting plus soft/hard thresholds (bytes vs entry count; scope).
- Whether curated indexes must declare focused-routing vs archival, or whether "curated = focused" suffices.

## Links

- [003-connect-skill-discovery-strategy](./003-connect-skill-discovery-strategy.md) — supersedes: this replaces 003's index-first primary discovery while retaining its curated-focused-index surface
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — rationale: the per-fork cost of a whole-index read is what makes retiring it worthwhile
- [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md) — rationale: per-fork load is the boundary this decision optimizes
- [feasibility-is-the-heaviest-forks-net-load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) — rationale: feasibility is set by the heaviest fork's net load, which the complete-index read inflates
- [index-curation-adds-orientation-that-generation-cannot-produce](../../notes/index-curation-adds-orientation-that-generation-cannot-produce.md) — rationale: why curated heads stay committed while generated listings move to build time
- [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) — procedure: the discovery skill whose standard read path this decision rewrites
