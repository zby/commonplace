---
description: "Ground source-dependent claims through immutable Claims entries on tracked ingests, preserve them across re-ingest, and review artifact uses through link-derived source pairs"
type: ../types/adr.md
tags: []
status: accepted
---

# 073-Untracked source snapshots require ingest grounding

**Status:** accepted
**Date:** 2026-08-24

## Context

Primary-source snapshots are ignored local reading copies. A fresh checkout
therefore retains an ingest's source identity and snapshot checksum, but not the
passages used to support a later artifact. Existing ingest analysis emphasizes
classification, novelty, connections, and limitations; it may omit an ordinary
premise that a later artifact needs.

This left two unsafe shortcuts. A writer could treat model familiarity or an
ingest's thematic analysis as source support, while a reviewer could follow a
link to an ingest without knowing which bounded source proposition the artifact
used. Re-reading an available snapshot during every write would hide expensive
and mutation-bearing source work inside the common write path, and would still
fail in a fresh checkout.

[ADR 072](./072-ingests-own-source-authority-and-snapshots-are-local.md)
made the ingest authoritative for durable identity and the checksum
authoritative for exact captured bytes. Its checksum-first cache lookup was
appropriate for recovering an observation, but insufficient to authorize a
mutation of a named ingest: integrity equality does not establish the intended
ingest-to-local-path binding.

## Decision

Every ingest report has exactly one `## Claims` section immediately before
`## Connections Found`. An empty section contains `No claims have been grounded
yet.` Each populated entry records one bounded `Claim (paraphrase)`, one or more
adjacent `Source extract (verbatim)` / `Source location` pairs, then `Scope`,
`Confidence`, and `Limitation`. Target-specific transfer reasoning stays in the
artifact that uses the claim.

Grounding is an explicit preparation step. The
[grounding instruction](../../instructions/ground-source-dependent-claims.md)
reads the complete Claims section and reuses an adequate entry unchanged. When
none exists, it reads the primary snapshot and hands one complete entry to the
ingest skill's deterministic append path. The ingest skill rechecks path
identity, canonical source equality, checksum, shape, and every verbatim
extract; replaces the canonical empty sentence on the first append; preserves
all incumbent entries and every byte outside Claims; validates; and reports the
exact normalized claim. It does not dispatch an analysis worker for this
append. Similar, narrower, broader, or disputed entries may coexist; V1 has no
claim IDs, merge, deduplication, or reconciliation protocol.

Grounding and ingest mutation require the exact name-paired paths
`kb/sources/<slug>.ingest.md` and
`kb/sources/.snapshots/<slug>.md`. The ingest's `snapshot_sha256` verifies that
named file; it does not discover a substitute. This partially supersedes ADR
072's checksum-first resolution rule for grounding, claim append, and
re-ingest/report replacement. Generic cache recovery may still locate exact
bytes by checksum, but that result alone cannot authorize these mutation paths.
Missing or mismatched named bytes route to re-ingest.

The two promoted artifact writers only check source dependencies. When a
candidate adds or materially changes a dependency on a named external source,
the writer resolves the ingest and reads all Claims. An adequate entry supplies
the preferred exact normalized wording and the target links the ingest. Without
one, the writer stops before the first durable target write and reports the
grounding route with `Target` and `Claim needed` filled in. The multistage writer
applies the same guard to `candidate.md`; a blocker remains in the workshop and
nothing is promoted. Neither writer invokes grounding, reads snapshots, or
edits an ingest. Unchanged source-dependent wording does not retrigger the
guard.

A virtual `source` verdict lens reviews artifact-to-ingest use independently.
Within the artifact scope already selected by `--note` or `--user-verified`, it
derives one pair for every resolved direct link to
`kb/sources/<slug>.ingest.md`; fragments do not affect identity and repeated
links deduplicate. `source/<slug>` filters one ingest, and `--all-gates`
includes source pairs. The exact ingest path is the persisted criterion. The
complete raw ingest is the criterion snapshot and freshness input, so either an
artifact edit or ingest edit can stale the pair. Job creation rechecks current
link applicability, and source criteria never qualify for trivial auto-ack
because ingests declare no `watches:`.

The source wrapper is mechanical prompt scaffolding outside the freshness hash.
It compares every articulated use with the complete Claims section and returns
the worst result: `pass` for supported uses within bounds or purely adjacent
links, `warn` when a claim, qualifier, or transfer is too unclear to verify, and
`fail` when support is absent, exceeds Scope or Limitation, or asserts an
unsupported transfer. A semantic wrapper change is a review-system upgrade and
requires deliberate corpus-wide re-review or acknowledgement; it is not
ordinary file-triggered staleness.

Same-checksum re-ingest preserves the Claims block byte-for-byte. A changed
observation requires explicit approval and proceeds only for the same source
and path while Claims are empty. Before an existing report is handed to a
drafting worker, the ingest parent creates and verifies an exact-byte temporary
backup. It retains that backup through the primary and one repair attempt,
restores it after handled final failure, and deletes it only after validated
success or verified restoration.

The operativity path is direct. The source collection contract, ingest type and
schema, drafting and re-ingest instructions, grounding instruction, and ingest
skill bind source-side writes. The two promoted writer skills enforce the
prospective stop. Review path normalization, selector derivation, job creation,
raw-input capture, and prompt rendering enforce the retrospective source lens.
Scaffolding packages the complete instruction tree into new installations;
existing user-owned copies are not silently upgraded.

## Considered alternatives

**Keep citations at external URLs and re-read the source on demand.** This keeps
the ingest small, but a fresh checkout may lack the historical bytes and each
writer would repeat source reconstruction. It also leaves no tracked statement
of the bounded proposition that was actually checked.

**Track every primary snapshot.** This would preserve direct evidence in Git,
but reverses ADR 072's repository-weight and durable-path decision. Claims keep
only the passages and bounds later consumers need while the checksum continues
to identify the full local observation.

**Use checksum-first lookup for grounding and report mutation.** Exact bytes are
necessary but do not bind a local filename to the ingest being changed. The
name-paired rule makes the mutation target and its evidence path inspectably
deterministic; the checksum then verifies the bytes at that path.

**Let writers invoke grounding automatically.** This removes a visible retry,
but mixes source reading and ingest mutation into a common artifact write,
expands its context, and makes a blocked write harder to reason about. The
selected prepare-then-retry boundary leaves both writers read-only toward
sources.

**Infer support from existing ingest prose or redraft the whole report.** The
analysis sections were not written as exhaustive source evidence. Rewriting
them to add one premise risks unrelated drift and conflicts with immutable
incumbent Claims. A deterministic Claims-only splice has the smaller mutation
surface.

**Add claim IDs, semantic deduplication, or conflict resolution now.** The
worked cases needed only whole-section reading and bounded entries. Similar or
disputed entries can coexist without ambiguity that justifies identity or merge
machinery.

**Widen review freshness with a snapshot or synthetic third input.** The
reviewer needs the artifact's use and the tracked ingest's bounded Claims, not
the ignored source body. A factored `(artifact, ingest)` pair reuses the
two-input freshness store and makes each source dependency stale
independently.

The deciding forces were operability in a fresh checkout, bounded tracked
support, explicit mutation authority, preservation of writer context, and reuse
of the existing two-file freshness architecture. V1 deliberately leaves
crash-safe staging, locking, compare-and-swap, concurrent-writer coordination,
secondary-resource grounding, universal write interception, and wider review
scan roots open until observed failures warrant them.

## Consequences

Source support becomes inspectable from tracked state without treating the
ingest as a copy of the primary source. Claim capture grows only when an
artifact needs it, and a later reviewer can distinguish source-side support
from the target's local transfer argument. Each linked ingest invalidates its
own review pair independently.

Authors may pay a grounding-and-retry round trip. Claims sections can accumulate
overlapping or disputed entries, and changing an already populated source
observation is intentionally blocked. The writer guard covers the two promoted
writers, not manual edits or every specialized Markdown workflow, and it cannot
detect unattributed prior art. The review lens can detect only dependencies
represented by resolved ingest links.

The append and re-ingest paths gain exact-preservation and handled-failure
restore obligations. They remain last-writer-wins under concurrent mutation and
are not crash-safe between overwrite and restore. Prompt-wrapper semantics also
gain an operational migration obligation: changing their judgment mapping
requires an explicit corpus-wide review decision because wrapper text is not a
freshness input.

---

Relevant Notes:

- [ADR 072: Ingest reports own source authority and snapshots are local materializations](./072-ingests-own-source-authority-and-snapshots-are-local.md) — supersedes: replaces checksum-first resolution only for grounding and mutation-bearing ingest paths while retaining its authority, cache, and checksum decisions
- [Factored dependency pairs for review freshness](../proposals/factored-dependency-pairs-for-review-freshness.md) — implements: adopts the proposal's source-as-gate case without widening the two-input freshness model
- [Review system architecture](../review-architecture.md) — part-of: uses its persisted criterion identity, two-file freshness, and mechanical-wrapper boundary
- [Ground a source-dependent claim](../../instructions/ground-source-dependent-claims.md) — procedure: explicit prepare-then-retry path for adding one bounded Claims entry
- [Ingest-report type](../../sources/types/ingest-report.md) — see-also: tracked Claims shape and source-record boundary consumed by the decision
