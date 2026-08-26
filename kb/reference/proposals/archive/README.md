# Proposal archive

Adopted and retired design proposals, kept out of the frontier.

Nothing here describes a live design question. Everything still current was extracted before the move; what remains is the irreproducible remainder — dated current-state anchors and the corpus measurements a design rested on.

## What this is for

Three jobs, all deliberate: **re-extraction** (something current was left behind and must be promoted into the frontier), **decision audit** (reconstructing how a choice was reached in more detail than its ADR compresses), and **re-opening** (a foreclosed design becomes live again — which means writing a new proposal in the frontier, not editing one here).

Archived files are frozen. Correct them only for link integrity when something they point at moves.

This README is the door: nothing else outside the archive links to files in it, so reaching one means coming through the Contents list below. If a job here turns up something still current, promote it into the frontier rather than linking to it.

What must hold of an archived proposal, and why: [`../README.md`](../README.md). How a proposal gets here: [retire an artifact](../../../instructions/retire-artifact.md). Decision record: [ADR 056](../../adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md).

## Contents

- [External articles collection](./external-articles-collection.md) — adopted by ADR 057, 2026-07-26. Editorial/expository profile, ProperDocs publication channel, excluded draft subtree, dated-body lifecycle, and searchable source lineage; the first-article test configuration is the texture behind the shipped procedure.
- [Harness-orchestrated review sweeps](./harness-orchestrated-review-sweeps.md) — adopted by ADR 035, 2026-07-01. Parent-owned, harness-neutral orchestration over deterministic job endpoints; the earlier Claude-only experiment and the instruction-versus-vendor-script choice are the texture behind the shipped procedure.
- [Ingest source units and supporting material](./ingest-source-units-and-supporting-material.md) — adopted by ADR 072, 2026-08-23. The pre-migration split between ingest and snapshot authority, three code-grounded ingests, and directory-source behavior that bounded the primary-plus-implementation decision.
- [Deterministic note-to-ingest claim checking](./deterministic-note-to-ingest-claim-checking.md) — retired by the ADR 073 revision, 2026-08-25. The 4-of-65 normalized-claim reuse result, 119-entry/374-quote corpus shape, and false-extract observations behind direct quote-or-snapshot checking.
- [Source genre is one open-vocabulary field on the snapshot](./source-genre-is-one-open-field-on-the-snapshot.md) — adopted by ADR 045, 2026-07-12. Genre unification across snapshots and ingest-reports; the open-vocabulary mechanism choice (a vocabulary file versus per-constraint severity) and the per-genre lens-home question are the texture behind that decision.
- [Assertion force separate from lifecycle status](./assertion-force-separate-from-lifecycle-status.md) — retired by ADR 044, 2026-07-11. The proposal to split the fused `status` field into a structural lifecycle enum plus contract-declared assertion force, including its later axis-decomposition self-critique; ADR 044 deleted the field instead.
- [Source-claim grounding skill and evidence-retention boundary](./source-claim-grounding-skill-and-evidence-retention.md) — adopted by ADR 076 and ADR 078, 2026-08-25. The ADR 073-era state in which `cp-skill-ingest` owned the quote-append path and writers stopped at a path-addressed instruction, the four evidence-persistence options weighed, and the 44-of-59 rollout figure behind keeping the ingest Quotes pool.
- [Operational destinations for literature-grounding findings](./operational-destinations-for-literature-grounding-findings.md) — adopted by ADR 081, 2026-08-26. The fourteen-candidate cohort, one-of-twenty propagation trace, and bounded Pirolli isolation option behind the claim-grained assessment and ordinary-writer prior-art boundary.
- [User-level uv tool installation for Commonplace commands](./user-level-uv-tool-installation-for-commonplace-commands.md) — adopted by ADR 064, 2026-08-08. The 0.1.4 project-venv, generated `.envrc`, and pip-based CI state plus the reported positive native Windows fresh-process experiment behind the new command authority.
