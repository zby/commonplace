---
description: "Workflow state has one ignored payload tree and its own collection; retained reports stay in the main history and can be searched separately."
type: reference/types/adr.md
tags: []
status: accepted
---

# 128-One ignored operational tree for workflow state

**Status:** accepted
**Date:** 2026-11-11
**Amends:** [ADR 007](./007-reports-directory-for-generated-snapshots.md): the collection and its `retained/` area stay; the `cache/` area and the regenerability criterion that separated it from `state/` go.
**Amended:** 2026-11-12 — [ADR 129](./129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md) moves multistage, AutoReason, article-staging and memory-landscape run bundles under `state/` and keeps them; the analysis process record stays outside until integration copies it

**Amended:** 2026-11-23 — the workflow state collection aligns the search boundary with the existing Git boundary.

## Context

ADR 007 split ignored report output into `cache/`, "safe to delete and
regenerate from authoritative inputs", and `state/`, whose owning workflow
controls cleanup. The split assumed that regenerability is a property a
reader can tell from the directory. An inventory on 2026-11-11 found that of
the cache producers only the promotion ranking is deterministic. Connect,
critique, friction and premise-decomposition reports are paid model
judgments: a rerun costs money and returns a different text. A review result,
which lived in `state/`, is the same kind of record with one difference, the
input hashes that let code tell whether it still applies. Both areas also
drifted: finished investigations left evidence bundles in `cache/`, and
`state/` held directories no workflow read. The location told a reader
nothing reliable about what deleting a file would cost, and no cleanup
decision was ever made from it.

A second force is the plan to keep operational state in a separate repository
so that collaborators can run reports and the work survives a change of
machine. That needs one publication boundary, not two trees with different
promises.

## Decision

The [workflow state collection](../../workflow-state/COLLECTION.md) has one ignored payload directory, `kb/workflow-state/data/`. New runs use `current/<workflow>/` inside it. Retained reports stay in `kb/reports/retained/`. Run records are not endorsements: they include unreviewed output, failed candidates and stops.

Cleanup is decided per workflow, not per class. The state README carries one
row per workflow output stating what deletion loses and the cleanup rule.
"Rebuild", "rerun" and "preserve" are ordinary words for those rows, not a
required classification, and no per-file metadata or numeric score is added.
An output whose use changes, such as a connect report that justified a
decision, gets an exception in its row or moves to `retained/`.

The operativity path: producers write to the paths named in their commands
and skills; KB discovery skips the payload subtree while direct validation can still check an individual result; the documentation site excludes it by configuration; installed
projects receive the layout from the scaffold manifest with no compatibility
shim. New projects start with this layout. Init preserves existing project
files; existing projects need a separate migration of old payloads and policy
files, not merely a rerun of init.

## Considered alternatives

Keep the split and add a numeric measure of how cache-like an output is.
Rejected: no consumer makes a decision from such a score, and the inventory
showed the split itself misclassified most outputs.

Keep the split but move the model-judgment reports to `state/`. Rejected:
`cache/` would then hold one deterministic file and the scratch directory for
captures, which does not justify a policy area.

Rename the unified tree during the original cache migration. Deferred at the time: `state/` already holds every path the
review code depends on, so keeping the name made the migration a move of the
cache producers only. A rename by `commonplace-relocate` remains possible.

Add a third area for finished investigations' evidence. Rejected: evidence a
tracked record cites belongs in `retained/`; evidence nothing cites belongs
in an archive outside the checkout, where the 2026-11-11 cleanup put it.

## Consequences

One ignore rule covers the payload; the contract and landing remain visible. A new workflow output has
one place to go and one row to write. The publication boundary for a state
repository is the one tree.

Nothing says "safe to delete" by location any more. A reader must consult the
workflow's row before removing anything, and a row that is wrong or missing
is now the failure mode. The tree grows until workflows remove their own
outputs through ordinary deletion.

Connect reports still carry no freshness accounting, so an input change
leaves one silently outdated; adding hashes like the review results' is
deferred, and this decision does not depend on it.

In the Commonplace checkout, workflow state has its own Git history. Frequent
changes that help explain individual runs would make substantive KB changes
harder to find in the main history. Keeping a run record does not require
promoting it to a retained report. The separate repository is not a requirement
for installed projects.

Readers looking for a citable report can search the reports collection without excluding run records. Maintainers investigating a stop can search workflow state directly. Historical records remain unchanged for comparison, not for resumption by current instructions. No alias at the former location is required. Public release and history pruning are separate decisions.
