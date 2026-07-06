# Lineage mechanisms workshop

## Purpose

Design the general lineage mechanism for Commonplace's growing set of derived materials: source ingests, connect reports, critique reports, review outputs, generated indexes, compiled views, skills, cue surfaces, source-to-source comparisons, agent-memory-system reviews over external repositories, ad-hoc distillations, merge-back edits, and future automatic derivations.

The critical requirement is automation. Commonplace should become more bitter-lesson-compatible by letting agents generate, check, refresh, route, and merge more derived material automatically. The lineage mechanism is the substrate that makes that safe: it records what a retained artifact depends on, what role it plays, when it is stale, whether it can be regenerated, whether it belongs in git, and why source material remains necessary even when a derivative is more useful for a specific consumer.

## Scope After Cleanup

This workshop now owns the **general derived-artifact lineage model**, not the current review-system migration.

In scope:

- a shared vocabulary for derivation events, inputs, producer/model provenance, freshness, merge-back, retirement, and promotion;
- storage-weight rules for lineage state: frontmatter/prose, shared append-only ledger, edge files, generated indexes, or database;
- git-retention rules for sources, report contracts, cheap generated reports, durable analyses, deterministic views, high-churn state, and merge-back provenance;
- model-provenance policy for one-shot derivatives, generated reports, reviews, durable source analyses, and canonical notes revised through many events;
- ad-hoc distillation and source-preservation rules;
- source/linking policy follow-up for contrast, parallel-mechanism, inverse-lineage, and source-to-source comparison cases.

Out of scope:

- current review Git decoupling, DB snapshots, selector-vs-runner boundary, and `model_partition` decision — accepted in [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) and described in [REVIEW-SYSTEM](../../reference/REVIEW-SYSTEM.md);
- review store source-of-truth alternatives, append-only review logs, and pure file review stores — owned by [src-architecture-alternatives](../src-architecture-alternatives/README.md);
- local connect-report cleanup queues — owned by [connect-maintenance-observations](../connect-maintenance-observations/README.md);
- generic code architecture cleanup outside lineage.

## Current Position

The review system supplied the first concrete witness, but the review details should no longer dominate this workshop. The reusable lesson is narrower:

> Static dependency edges can stay as links or frontmatter. Dynamic, churning edge-state with no natural owner file needs relational structure; a real database is earned when keyed lookup, churn, and consistency outgrow a filesystem-backed relation.

The extracted note [many-to-many-edge-state-is-where-files-yield-to-a-database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) is the storage predicate for future investigations. Review remains the current example of the heavy tier, but the general mechanism should not copy review tables or review execution concepts into every derivative class.

The likely architecture is **one lineage vocabulary, multiple storage weights**:

| weight | carrier | use when |
|---|---|---|
| In-artifact | frontmatter pointers and prose | lineage is low-churn and read on demand |
| Shared event surface | commit message convention, JSONL, or small ledger | events must be auditable independently of one artifact file but do not need a swept selector |
| Operational edge store | edge-file tree, generated index, or SQLite | automation repeatedly queries mutable current state over many-to-many edges |

Files remain the primary API for authored and readable artifacts. The lineage layer should be a freshness and provenance substrate, not a batch processor: it records accepted dependency baselines, resolves current versions, and emits refresh targets. Review sweeps, connect jobs, source processors, and agents decide how to perform refreshes.

## Open Work

Close this workshop by extracting durable artifacts for these decisions:

- the verification-locus theory notes and the type-spec/skill contract-migration proposal drafted in [verification-locus-and-provenance-theory.md](./verification-locus-and-provenance-theory.md) — the theoretical basis for assigning every derivation edge an invalidation rung (watched / recorded / untracked);
- a general lineage model for derived artifacts that distinguishes source material, generated reports, durable analysis, compiled views, canonical artifacts, merge-back events, and promoted library artifacts;
- an explicit storage-weight rule based on the many-to-many/churning-edge predicate;
- a retention policy for which automatic derivations are committed, gitignored, stored in a state store, summarized into durable artifacts, or discarded after merge-back;
- a model-provenance rule for derivative artifacts and derivation events, without turning canonical notes into "last edited by model" records;
- a merge-back lineage model for note edits driven by connect reports, reviews, critique reports, source ingests, or ad-hoc distillations;
- a source-preservation rule for snapshots, external git-backed sources, reviewed revisions, citations, and cases where the derivative cannot replace the source;
- an ad-hoc distillation rule for one-off prompts, source packets, and workshop artifacts that may later be reused, promoted, or extracted into skills;
- updates or proposals for `kb/sources/COLLECTION.md`, `kb/reference/link-vocabulary.md`, or report-type contracts if the transferred cases require new link labels or promotion expectations.

## Transferred Case Backlog

These cases came from `kb/work/connect-maintenance-observations/`. They are test cases for the mechanism, not the goal of the workshop.

| case | mechanism question |
|---|---|
| Claude dynamic-workflows docs vs practitioner article | Durable source-to-source `compares-with` vs synthesis-owned comparison. |
| How to build your own agent harness | Whether source-to-note contrast or parallel-mechanism labels belong in source collection policy. |
| The log is the agent | Near-duplicate ingest cross-reference and sovereignty/lock-in synthesis trigger. |
| Text optimization | How to record external-cognition lineage and future Meta-Harness cross-references. |
| Where it lives | How to represent an external paper downstream of internal vocabulary without lying about provenance. |

## Working Files

- [verification-locus-and-provenance-theory.md](./verification-locus-and-provenance-theory.md) - theoretical spine: state vs history verification, the two reification bridges, dual invalidation semantics, the graduated invalidation ladder, and the external literature anchors (build systems, PROV, in-toto, credence goods).
- [current-practices-and-theory.md](./current-practices-and-theory.md) - descriptive inventory of current lineage mechanisms, theory, and unresolved tensions.
- [automatic-derivation-rules.md](./automatic-derivation-rules.md) - draft policy for git retention, merge-back lineage, derivative refresh, and automation boundaries.
- [storage-weight-across-cases.md](./storage-weight-across-cases.md) - comparison of derivation cases against the many-to-many/churning-edge storage predicate.
- [model-provenance.md](./model-provenance.md) - model metadata rule for derivation events, one-shot derivatives, reviews, canonical note merge-back, and deterministic generated views.
- [general-lineage-refresh-state-design.md](./general-lineage-refresh-state-design.md) - SQLite-backed lineage freshness design that stays isolated from batch refresh execution.

Moved out of this workshop:

- [review-lineage-storage-case.md](../src-architecture-alternatives/review-lineage-storage-case.md) and [pure-file-review-store-design.md](../src-architecture-alternatives/pure-file-review-store-design.md) - now belong to the review-store architecture alternatives workshop.
