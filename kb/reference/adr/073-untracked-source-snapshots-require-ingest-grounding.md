---
description: "Retain only verbatim source quotes in ingests, mark source links that require a snapshot, and use the standard grounding gate for both routes"
type: ../types/adr.md
tags: []
status: accepted
---

# 073-Untracked source snapshots require ingest grounding

**Status:** accepted
**Date:** 2026-08-24
**Revised:** 2026-08-25

## Context

Primary-source snapshots are ignored local reading copies. A fresh checkout
therefore retains an ingest's source identity and snapshot checksum, but not the
complete captured source. Ingest analysis is tracked, but its summaries,
classifications, connection judgments, and limitations are interpretations.
They are not source text.

The first version of this decision added a `## Claims` ledger. Each entry held
a normalized `Claim (paraphrase)`, exact extracts, and authored Scope,
Confidence, and Limitation fields. A virtual source-conformance review then
checked a note's wording against that normalized claim. This created two
semantic hops: the note was checked against an ingest paraphrase that had
itself been checked against the source. Rewording at either hop could change the
proposition. The ledger therefore made the final judgment easier to run but did
not make it sound.

A direct check has two possible inputs. A bounded verbatim passage may contain
enough source material to judge the note's use. Some claims instead depend on
broad, distributed, or contextual material that cannot be represented soundly
by a small set of retained quotes. The full snapshot is then required, but it
cannot be assumed to exist on every machine.

[ADR 072](./072-ingests-own-source-authority-and-snapshots-are-local.md)
makes the ingest authoritative for durable source identity and the checksum
authoritative for exact captured bytes. This decision keeps that split and
makes the unavailable-snapshot case an explicit property of the source link.

## Decision

Every ingest report has exactly one `## Quotes` section immediately before
`## Connections Found`. The empty section contains `No source quotes have been
retained yet.` A populated section contains only adjacent pairs of
`Source extract (verbatim)` and `Source location`. It contains no normalized
claim, scope judgment, confidence assessment, limitation, or target-specific
transfer argument.

Quote append is mechanical. The grounding procedure reads the exact
name-paired snapshot, verifies its canonical source and `snapshot_sha256`, and
appends the minimum one or more exact passages needed for a sound later check.
The ingest skill verifies that every retained passage occurs in those exact
snapshot bytes, preserves incumbent quote items and all other bytes, and runs
deterministic validation. Similar, overlapping, and disputed passages may
coexist; V1 has no quote IDs, semantic deduplication, or reconciliation.

Every new or materially changed source-dependent claim is checked directly
against source material during authoring. The writer applies the existing
`semantic/grounding-alignment` test to one of two routes:

- **Quotes route.** An ordinary link to
  `kb/sources/<slug>.ingest.md` declares that the tracked Quotes section is
  sufficient. The writer and reviewer read only its verbatim extracts as
  source support. They ignore every analytical ingest section. If the quotes
  are insufficient, the check fails; it never silently falls back to a local
  snapshot.
- **Snapshot route.** The ingest link text contains the exact marker
  `(snapshot required)`. The checker derives only
  `kb/sources/.snapshots/<slug>.md`, verifies exact-byte SHA-256 and canonical
  source equality against the ingest, and reads the snapshot. Missing,
  mismatched, or unreadable bytes are a failure, not a warning or an invitation
  to find another copy.

A purely adjacent source link makes no support claim and passes either way.
The marker applies to the linked source use, not to every claim in the artifact.
Writers keep target-specific transfer reasoning in the target and apply the
same gate to that inference rather than asking the source to contain the
target's conclusion.

The standard `semantic/grounding-alignment` gate is the only persisted semantic
checker for these routes. Review prompts already carry each target's resolved
Markdown-link table and allow semantic gates to read linked material. Prompt
scaffolding adds only a generic allowance for an active criterion to derive one
exact local path from a target link. The judgment-bearing route, failure rules,
and marker syntax live in the gate file, so changing them stales ordinary gate
baselines as `criterion-changed`.

The virtual `source` lens, link-derived `(artifact, ingest)` pairs, raw-ingest
criterion handling, source-specific prompt wrapper, applicability resolver, and
source-specific freshness behavior are removed. `--all-gates` continues to
include `semantic/grounding-alignment` as part of the semantic catalog; it no
longer creates an additional pair per ingest link.

An ingest's `snapshot_sha256` is immutable. Same-checksum re-ingest may redraft
the analytical sections while preserving the complete Quotes block
byte-for-byte. Changed source bytes are a new observation and require a
distinct snapshot basename and ingest path. This rule is necessary even when
Quotes is empty because a `(snapshot required)` link may depend on the recorded
bytes.

The operativity path is direct. The source collection contract, ingest type and
schema, drafting and re-ingest instructions, grounding instruction, ingest
skill, and deterministic quote validator bind source-side writes. The promoted
writers apply the gate before landing new source-dependent claims. The standard
review selector, job pipeline, and grounding gate provide independent
retrospective review without a source-specific pair type. Scaffolding packages
the complete instruction tree into new installations; existing user-owned
copies are not silently upgraded.

This revision retires the proposal *Deterministic note-to-ingest claim
checking*. Its corpus measurements remain relevant: only 4 of 65 sampled
note-to-ingest pairs reused the normalized claim string, while the first
grounded corpus contained 119 paraphrased entries and 374 retained exact
extracts. The migration keeps those extracts and removes the interpreted
fields.

## Considered alternatives

**Keep the paraphrased Claims ledger.** This keeps compact scope and limitation
statements, but makes the review depend on a paraphrase of a paraphrase. The
semantic relation that matters remains indirect.

**Store a verbatim copy of every note claim in the ingest.** Exact string
matching would become possible, but the ingest would duplicate consumer prose
rather than retain source material. Each rewording would add another copy, and
string equality would still not establish source support.

**Always require the snapshot.** This gives the reviewer the strongest input
but makes every source-grounded note non-portable. The selected split preserves
the common bounded case in tracked state and exposes the exceptional
availability requirement.

**Track every primary snapshot.** This would eliminate local absence, but
reverses ADR 072's repository-weight and durable-path decision. Quotes retain
only the minimum passages that ordinary checks need.

**Let the checker fall back to any available snapshot automatically.** This
would make the same note pass or fail according to ambient cache state without
declaring that dependency. The marker makes non-portability visible in the
artifact and fail-closed in review.

**Keep the virtual source-conformance lens alongside the standard gate.** This
would duplicate an already operational semantic-review path. The standard gate
already owns grounding alignment, participates in the existing catalog and
review pipeline, and can express both source-input routes in its hashed
criterion text. A lens would read the same note-to-source relation while
maintaining separate selection, prompt, freshness, and result paths.

**Use checksum-first lookup for the snapshot route.** Equal bytes do not bind a
local path to the ingest being cited. Exact name pairing makes the declared
dependency inspectable; the checksum then verifies the bytes at that path.

## Consequences

The semantic check is direct: note claim to source quote, or note claim to the
full pinned source. Ingest analysis remains useful for discovery and
orientation but cannot acquire source authority by being tracked. A fresh
checkout can review ordinary quote-backed uses and must fail declared
snapshot-dependent uses until the exact observation is restored.

Ingests may accumulate overlapping quotes, and source locations remain authored
locators rather than mechanically verified anchors. Some claims will carry a
visible availability dependency in their link text. Authors may pay a
grounding-and-retry round trip to retain a bounded quote or may need to restore
a snapshot before a claim can land.

The standard grounding gate has one freshness pair per note rather than one
pair per linked ingest. Quote append does not stale an accepted grounding
review. This is safe under the selected mutation rules: Quotes is append-only,
analytical sections are ignored as support, and `snapshot_sha256` never
changes. A note edit or grounding-gate edit still stales the pair. Removing or
rewriting an incumbent quote is outside the supported mutation contract.

Existing source-conformance baselines are obsolete and should be retired. The
grounding-gate edit makes existing standard grounding baselines stale, so the
next semantic review applies the new direct-source rules without a special
migration result protocol.

---

Relevant Notes:

- [ADR 072: Ingest reports own source authority and snapshots are local materializations](./072-ingests-own-source-authority-and-snapshots-are-local.md) — supersedes: replaces checksum-first resolution for grounding and makes each recorded observation immutable while retaining its authority and cache split
- [Grounding alignment gate](../../instructions/review-gates/semantic/grounding-alignment.md) — implemented-by: the sole semantic check for quote-backed and snapshot-required source uses
- [Ground a source-dependent claim](../../instructions/ground-source-dependent-claims.md) — procedure: retain bounded exact quotes or declare the snapshot-required route
- [Ingest-report type](../../sources/types/ingest-report.md) — see-also: tracked Quotes shape and source-record boundary consumed by the decision
