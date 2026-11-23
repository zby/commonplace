---
description: "Retires the tag participation list. Each selective head gets an exact generated list grouped by collection, without traversing workflow state or source snapshots."
type: reference/types/adr.md
tags: []
status: accepted
---

# 141-List tag members by collection

**Status:** accepted
**Date:** 2026-11-23
**Amends:** [ADR 089](./089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md). The shared namespace and head requirement remain.

## Context

A source ingest and a theory note can both address the same topic. The former participation list omitted the ingest to keep source lookup separate from theory lookup. A reader who wanted both had to know to search sources separately. One group per collection preserves the distinction without requiring two searches.

## Decision

Discover top-level collections by their `COLLECTION.md`. On each shared tag head, append all eligible artifacts carrying that tag, grouped by collection. Include artifacts already recommended by the [selective head](./140-tag-heads-are-selective.md); the generated list alone answers the exact membership question. An eligible tag assignment needs a head, including an assignment on a source analysis. A collection's contract still decides what may be tagged. Do not infer endorsement or permission to add tags from membership.

Never traverse `kb/workflow-state/` or `kb/sources/.snapshots/` to collect tags. Run data and captured originals are not authored tag assignments. This applies even when both directories are populated in a local checkout. The [tag collection contract](../../tags/COLLECTION.md#membership-by-collection) defines the other exclusions.

## Considered alternatives

Keeping `participating:` while grouping its members would still omit tagged sources unless someone maintained the list. Making separate heads per collection would duplicate the topic definition. Keep a single definition and separate the member lists instead.

## Consequences

New collections need no registration. Remove `participating:` from existing project-owned tag contracts; the collection-contract schema rejects it. One collector supplies exact lookup and the published groups. Checking one artifact's tags requires collection roots and head filenames, not a walk over other members. Source discovery beyond existing assignments and the editorial audit remain separate work.
