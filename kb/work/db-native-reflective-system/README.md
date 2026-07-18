# Workshop: a DB-native reflective self-improving system

## Question

If you were building a [reflective](../../notes/definitions/reflective-system.md), [self-improving](../../notes/definitions/self-improving-system.md) LLM-based system — structurally like Commonplace, but committed from day one to a database as the primary store for its *content*, not just its churning operational edge-state — what would the complete data model need to cover?

The [freshness store](../../reference/freshness-architecture.md) is the closest thing Commonplace has to this already: it retains exact artifact text in `artifact_snapshots`, tracks accepted baselines and their inputs, and selects targets affected by change. It is the starting skeleton, not the answer — it was built to cache *just enough* file content to detect staleness for review pairs, not to be the canonical home for all KB content, structure, and behavior-determining organization. This workshop asks what has to be added to turn that skeleton into a complete substrate.

## Why this isn't re-litigating files-vs-database for Commonplace

Commonplace has already decided this for itself: [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md), with the scoped exception named precisely in [churning state on a many-to-many edge is where files yield to a database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — which is exactly what the review/freshness tables are. That note itself says a database "may earn its place" once access patterns stabilize, "either as a replacement or, more likely, as a derived layer alongside files" — but nothing currently justifies that move for Commonplace, and this workshop does not manufacture such a justification. Two active neighbor workshops already own the Commonplace-specific version of this question at narrower scope — see below.

This workshop instead removes the file constraint as a starting axiom and asks the counterfactual design question on its own terms: for a *hypothetical* system built DB-native from the start (no git, no filesystem-as-source-of-truth), what does completeness require? That is additive, not redundant, as long as it doesn't quietly re-derive `files-not-database.md`'s conclusion by another route — the answer here is expected to be a schema and a gap list, not a recommendation to migrate Commonplace.

## Scope

In scope:

- what "content" itself looks like as DB rows with real version history (notes, instructions, ADRs, types, tags, links), replacing git+markdown as the mechanism that currently gives versioning, diffing, and browsing for free;
- lifting the freshness schema from "cache of file-text used for staleness comparison" to "the canonical representation" — identity (path vs. stable ID vs. content-address), write-time versioning vs. accept-time snapshotting, structure/collection membership, and a type/schema registry;
- links and tags as first-class relational edges rather than authored prose — the general case the [many-to-many edge-state note](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) leaves open ("every authored link is a latent dependency edge... ranking link and edge types by disruption probability... is the larger analysis this boundary opens");
- what the [reflective-system](../../notes/definitions/reflective-system.md) obligations demand of the schema itself — self-representation availability, causal connection, a declared aspect boundary — including whether the schema-of-the-schema (the type registry) needs the same versioning machinery as ordinary content;
- what the [self-improving-system](../../notes/definitions/self-improving-system.md) obligations demand beyond plain versioning — if a proposal-selection improvement loop is a target property, candidate/evaluation/retention needs bookkeeping distinct from an accepted-version history, echoing the still-unimplemented [workshop-layer types](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) (decision threads, experiments) that the file-based system has never formally modeled either;
- a substitute for the capabilities files supply for free, named explicitly in `files-not-database.md`: browsing without a bespoke viewer, and agent access without an API layer.

Out of scope:

- migrating Commonplace itself off files — settled, see above;
- the Commonplace-specific review-store source-of-truth question (SQLite-as-store vs. append-only log vs. pure-file) — owned by [src-architecture-alternatives](../src-architecture-alternatives/README.md); this workshop may use its findings as evidence but does not re-decide them;
- the general derived-artifact lineage vocabulary and storage-weight rules for Commonplace's actual subsystems — owned by [lineage-mechanisms](../lineage-mechanisms/README.md);
- the [collection-as-artifact-freshness proposal](../../reference/proposals/collection-as-artifact-freshness.md) specifics — reference its `collection-text` encoding as one input to the DB-native collection model, don't redesign it.

## Relationship to prior work

| artifact | relationship |
|---|---|
| [files-not-database.md](../../notes/files-not-database.md) | the settled default this workshop deliberately steps outside of, for a hypothetical system only |
| [many-to-many-edge-state...](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) | supplies the structural predicate; this workshop asks what happens once *every* edge is treated this way, not just the churning ones |
| [freshness-architecture.md](../../reference/freshness-architecture.md) / [storage-architecture.md](../../reference/storage-architecture.md) | the schema and physical-store facts this workshop starts from |
| [artifact-freshness-and-referential-checks](../artifact-freshness-and-referential-checks/README.md) | shipped the v1 schema this workshop treats as a skeleton; that workshop's own closure does not depend on this one |
| [lineage-mechanisms](../lineage-mechanisms/README.md) | owns Commonplace's actual storage-weight decisions; this workshop may borrow its in-artifact/event-surface/operational-store weight vocabulary for the hypothetical design |
| [src-architecture-alternatives](../src-architecture-alternatives/README.md) | owns the review-store source-of-truth debate for Commonplace; its three candidate shapes (SQLite-as-store, pure-file, append-only-log+index) are evidence, not a decision to redo |
| [reflective-system.md](../../notes/definitions/reflective-system.md), [self-improving-system.md](../../notes/definitions/self-improving-system.md) | supply the two completeness checklists (five reflective obligations; evidence-responsive operative change, optionally a proposal-selection loop) the schema is graded against |
| [commonplace-as-a-reflective-system.md](../../reference/commonplace-as-a-reflective-system.md) | worked example of what "reflective coverage" looks like when graded pathway-by-pathway; useful as a rubric for evaluating the hypothetical schema's coverage claims |

## Document map

- [README.md](./README.md) — this framing
- [freshness-schema-as-starting-skeleton.md](./freshness-schema-as-starting-skeleton.md) — first pass: what the shipped freshness/review tables already give for free, and the gap list against the two completeness checklists
- [generalized-schema-draft.md](./generalized-schema-draft.md) — second pass: one candidate schema (artifact / versioned content / current head / opt-in-tracked edge) drafted against the gap list, with what doesn't fit named explicitly (browsing/agent access, diff storage, rename tracking, the type-registry bootstrap seam)

## What closes the workshop

1. a candidate DB schema (or a small set of alternatives) covering content, structure/collections, types, links/tags, review/freshness, and workshop/task lifecycle state, evaluated against both checklists above;
2. an explicit disposition for each gap in the survey — solved by the schema, deferred with a reason, or found to require a non-DB component after all (e.g., a rendering/browsing layer that turns out to be irreducible infrastructure);
3. either a promoted reference artifact (a note or reference doc describing the hypothetical architecture) or an explicit finding that the exercise doesn't converge on a stable design, with the reason;
4. no change to Commonplace's own storage decisions — if the exercise surfaces something Commonplace should actually adopt, that becomes a proposal handed to `lineage-mechanisms` or `src-architecture-alternatives`, not applied here.

Then delete this workshop and remove its entry from [kb/work/README.md](../README.md).
