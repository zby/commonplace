---
description: "Decision that kb/reports keeps one ignored operational tree, state/, with one directory per producing workflow and a per-workflow statement of what deletion loses, replacing the cache/state split by regenerability"
type: reference/types/adr.md
tags: []
status: accepted
---

# 128-One ignored operational tree under kb/reports/state

**Status:** accepted
**Date:** 2026-11-11
**Amends:** [ADR 007](./007-reports-directory-for-generated-snapshots.md): the collection and its `retained/` area stay; the `cache/` area and the regenerability criterion that separated it from `state/` go.

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

`kb/reports/` has one ignored operational tree, `state/`, and one tracked
record tree, `retained/`. Every ignored workflow output lives under `state/`
in its workflow's directory. The `cache/` area is removed from the contract,
the ignore rules, the scaffold for installed projects and every producer's
path. Presence in `state/` is not endorsement: the tree holds unreviewed model
output, failed candidates and stopped runs.

Cleanup is decided per workflow, not per class. The state README carries one
row per workflow output stating what deletion loses and the cleanup rule.
"Rebuild", "rerun" and "preserve" are ordinary words for those rows, not a
required classification, and no per-file metadata or numeric score is added.
An output whose use changes, such as a connect report that justified a
decision, gets an exception in its row or moves to `retained/`.

The operativity path: producers write to the paths named in their commands
and skills; the validator excludes the tree through the tracked marker at
`state/`; the documentation site excludes it by configuration; installed
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

Name the unified tree afresh. Deferred: `state/` already holds every path the
review code depends on, so keeping the name made the migration a move of the
cache producers only. A rename by `commonplace-relocate` remains possible.

Add a third area for finished investigations' evidence. Rejected: evidence a
tracked record cites belongs in `retained/`; evidence nothing cites belongs
in an archive outside the checkout, where the 2026-11-11 cleanup put it.

## Consequences

One ignore rule, one landing page and one marker. A new workflow output has
one place to go and one row to write. The publication boundary for a state
repository is the one tree.

Nothing says "safe to delete" by location any more. A reader must consult the
workflow's row before removing anything, and a row that is wrong or missing
is now the failure mode. The tree grows until workflows remove their own
outputs through ordinary deletion.

Connect reports still carry no freshness accounting, so an input change
leaves one silently outdated; adding hashes like the review results' is
deferred, and this decision does not depend on it.

This decision stops at the tree's layout and cleanup rule. It does not decide
whether the tree becomes a separate repository, what that repository may
publish, or how its history is pruned; those stay with the
[public state repository workshop](../../work/public-state-repository/README.md)
until decided.
