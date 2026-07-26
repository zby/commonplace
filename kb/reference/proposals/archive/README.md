# Proposal archive

Adopted and retired design proposals, kept out of the frontier.

Nothing here describes a live design question. Everything still current was extracted before the proposal was archived: shipped behavior into reference docs, the decision-relevant reasoning into the superseding ADR's `## Considered alternatives`, transferable requirements into `kb/notes/`. What remains is design texture — dated current-state anchors, corpus statistics, the dialectic a proposal accumulated while it waited.

## What this is for

Three jobs, all deliberate: **re-extraction** (something current was left behind and must be promoted into the frontier), **decision audit** (reconstructing how a choice was reached in more detail than its ADR compresses), and **re-opening** (a foreclosed design becomes live again — which means writing a new proposal in the frontier, not editing one here).

Archived files are frozen. Correct them only for link integrity when something they point at moves.

## Rules

- **No library artifact links to files in it.** Two exceptions: this README, the door everyone comes through; and the workshop layer (`kb/work/`), where archive work is actually done and whose files are themselves temporary. ADRs and reference docs name archived proposals by title in prose, never by path.
- **Archived files may link out.** Each carries a banner pointing to the ADR that adopted or retired it; sinks may cite sources.
- **Repair by re-extraction, never by linking in.** Promote what was missed into the frontier. A live inbound link would make an archived document load-bearing again and defeat the separation.

Contract: [`../README.md`](../README.md). Decision record: [ADR 056](../../adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md).

## Contents

- [External articles collection](./external-articles-collection.md) — adopted by ADR 057, 2026-07-26. Editorial/expository profile, ProperDocs publication channel, excluded draft subtree, dated-body lifecycle, and searchable source lineage; the first-article test configuration is the texture behind the shipped procedure.
- [Harness-orchestrated review sweeps](./harness-orchestrated-review-sweeps.md) — adopted by ADR 035, 2026-07-01. Parent-owned, harness-neutral orchestration over deterministic job endpoints; the earlier Claude-only experiment and the instruction-versus-vendor-script choice are the texture behind the shipped procedure.
- [Source genre is one open-vocabulary field on the snapshot](./source-genre-is-one-open-field-on-the-snapshot.md) — adopted by ADR 045, 2026-07-12. Genre unification across snapshots and ingest-reports; the open-vocabulary mechanism choice (a vocabulary file versus per-constraint severity) and the per-genre lens-home question are the texture behind that decision.
- [Assertion force separate from lifecycle status](./assertion-force-separate-from-lifecycle-status.md) — retired by ADR 044, 2026-07-11. The proposal to split the fused `status` field into a structural lifecycle enum plus contract-declared assertion force, including its later axis-decomposition self-critique; ADR 044 deleted the field instead.
