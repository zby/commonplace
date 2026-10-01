---
description: Agentic analysis instructions, report types and retention areas belong to their research collection, with a bounded migration of paths and byte pins.
type: reference/types/adr.md
tags: []
status: accepted
---

# 099-Agentic analysis method and reports belong to the collection

**Status:** accepted
**Date:** 2026-10-01
**Amends:** [ADR 084](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) for collection-specific operation placement, and [ADR 087](./087-source-and-report-types-are-global-library-types.md) for agentic analysis report types.

## Context

Agentic-system analysis is focused research machinery. Its instructions and
report types serve one collection, while generic Commonplace operations serve
consuming KBs. Shipping the research method as global library content gives it
a broader apparent scope than its actual consumers. Local types are eligible
only in their owning collection, so moving types alone would leave reports
outside their allowed scope.

## Decision

The agentic-systems collection owns its analysis instructions, shared analysis
contracts, landscape synthesis, taxonomy maintenance, report types and report
lifecycle areas. Generic instruction and type-spec contracts and base schemas
remain global. Keep one collection contract: it carries placement, lifecycle
and instruction composition rules. There are no nested collection contracts.

A collection-specific operation may live in its owning collection's
`instructions/`; general operations remain in `kb/instructions/`. The
Commonplace transfer scan remains general because its result serves a current
Commonplace design question. Analysis-specific Python commands remain packaged;
a separate extension is deferred.

The relocated types use `agentic-systems/types/<name>.md`. Working runs live in
`reports/state/` and tracked frozen sets in `reports/retained/` within that
collection. Exact historical analyses live in `reports/retained-archive/` under
their producing contracts. Current validation excludes local state and archives
from sweeps but explicitly validates selected current runs and sets.

Authorize one bounded layout migration of frozen sets and their pins. It may
rewrite declared paths, type identities and relocation-required relative links,
then recompute their dependent checksums. It preserves analytical content,
source boundaries, evidence assessments, record and run IDs, and historical
method commits. Retain a machine-readable old/new hash map and acceptance
report. Commit-bound syntheses retain their original input commit and hashes;
they do not become current analyses by migration.

## Considered alternatives

**Move only the types.** Rejected because reports outside the owning collection
would fail existing type eligibility. Moving method and reports together
preserves that rule without adding resolver exceptions.

**Keep the research method global.** Rejected because its actual consumers are
collection-specific and it need not appear in every installed KB's library.
The generic library remains usable without the analysis corpus.

**Extract a separate package now.** Deferred because document ownership solves
the present placement problem. Moving executable commands and dependency
management adds another deployment boundary without a current consumer need.

**Retype historical archives under the current schema.** Rejected because a
mechanical move supplies no new analytical evidence or method clearance. Preserve
their producing contracts and exact bytes instead.

## Consequences

Collection-local types, working state, frozen evidence and their method share
one ownership boundary. Research skills remain discoverable in this checkout;
ordinary package initialization installs only the promoted generic skills.

The operativity path runs through collection and type contracts loaded by
writers, local schema resolution and validator registrations, workflow input
and output emitters, publication method checks and byte pins, comparison
readers, runtime skill projections, and package build/init consumers. Their
shared path identities enforce the boundary without resolver aliases.

This decision covers the agentic analysis machinery and its direct research
companions. It does not relocate general Commonplace procedures, change generic
type eligibility, authorize analytical revisions, or let an old run resume by
rewriting its method commit. The immutable-byte exception applies only to this
recorded layout migration.
