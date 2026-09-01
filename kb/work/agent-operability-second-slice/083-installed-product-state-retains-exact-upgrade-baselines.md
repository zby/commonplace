---
description: "Proposed decision that installed-product state retains portable content-addressed base bytes so project drift and offline three-way upgrades share one authority"
type: kb/reference/types/adr.md
tags: []
---

# 083-Installed product state retains exact upgrade baselines

**Status:** workshop draft; not accepted  
**Date:** 2026-09-01  
**Promotion condition:** accept only with the implementation that makes the
producer, status consumer, upgrade-plan consumer, integrity checks, and
recovery behavior operative.

## Context

`commonplace-init` copies framework library files, user-space seeds, and skill
projections into a project. It preserves every differing existing file. The
active command reports its package version, but the project retains neither an
exact identity for the bytes established by initialization nor the prior bytes
needed to compare a local edit with a later upstream edit. A rerun can compare
the project only with the active package and therefore cannot tell which side
changed.

The [Stage 1 baseline](./baseline.md) reproduced this failure. A fixture whose
project and command versions both said `0.1.5` remained healthy after an
installed framework file was edited. A clean install contained 760
destinations but 734 unique content blobs; the two runtime skill projections
accounted for the duplicate destinations. Hashing the entire installed tree
took about 45 milliseconds on the measured machine. Hash identity is therefore
cheap enough for status, but a hash cannot reconstruct prior content. When the
local and upstream versions changed the same 7,478-byte file differently, the
prior file was required to locate the conflict and preserve its unaffected
content.

The active [installed-product ADR draft](../system-contract-consistency/successor-installation-adr-draft.md)
already owns installed topology, per-file ownership, projection, and the
installer-state manifest. It selects
`commonplace-library/.installed-product.json` in its proposed disjoint-root
layout. Creating a second root `.commonplace/` record, as the initial
[Stage 1 design choice](./design-choice.md) suggested before that owner was
found, would divide authority over the same files. This decision instead
extends the installed-product state with the exact baseline content required
by classification and upgrade planning.

## Decision

### One installed-product state owns identity and prior content

Use the installed-product manifest selected by the installed-topology decision
as the sole project-side authority for framework projection identity,
ownership, and accepted baselines. Do not create a parallel root-level project
provenance manifest.

In the topology currently proposed by that decision, the versioned manifest is
`commonplace-library/.installed-product.json`. Store baseline blobs adjacent to
it under an installer-owned content-addressed directory. If the topology draft
changes before implementation, promotion of this ADR must use the final
installer-state location while preserving the single-owner rule. The ADR does
not reserve a second path independently of the installed-product decision.

The manifest maps each owned destination to:

- its installed-product ownership role;
- canonical source identity and path or template identity;
- the hash of the accepted rendered baseline bytes;
- a reference to the corresponding content-addressed baseline blob; and
- the source/package identity and record-schema version needed to interpret
  the entry.

The record retains template render inputs when a later upstream template needs
them to produce a comparable desired destination. A projected skill has its
own destination entry and current hash, but its entry references the same
baseline blob and canonical skill source as equivalent projections. One set of
prior bytes can therefore govern several independently checked destinations.

Retain baseline content for `commonplace-managed`, `commonplace-replica`, and
`user-seed` destinations. A `user-seed` remains protected from automatic
replacement, but its base is necessary to distinguish retained user work from
an upstream change and to prepare a merge. Do not record arbitrary
`user-owned` content as part of the installed product.

The content address is over exact installed bytes. Compression and archive
encoding may change without changing blob identity, provided integrity checks
recover the exact bytes before comparison. A manifest entry whose blob is
missing or fails its content hash is corrupt state, not evidence that the
project is current.

### State transitions are explicit and atomic at the authority boundary

Initialization publishes the complete manifest and its referenced blobs only
after it has materialized the intended project outputs successfully. A partial
initialization with no complete published record is an unknown installation;
it must not masquerade as a current baseline.

Read-only inspection, status, and upgrade planning never create, adopt,
repair, or advance installer state. A legacy project without a trusted record
is `unknown`. Adoption requires a separate inspectable operation that names
the evidence and authority used; equality with the active package is not
implicit adoption.

Only a successful explicit upgrade may advance the accepted baseline. It
publishes the new complete record after its declared changes and verification
succeed. A failed or interrupted apply leaves the prior complete baseline
authoritative and reports recovery work. Baseline blobs remain until no
published or recovery record references them; the installer-state producer
owns their cleanup.

### Classification and planning consume the same three identities

For each destination, compare:

1. the accepted baseline from installer state;
2. the current project bytes; and
3. the desired upstream bytes resolved by the active package and install
   projection.

The comparison distinguishes current, locally customized, upstream-changed,
convergent, and both-sides-changed cases without Git. Both-sides-changed is a
conflict candidate: the upgrade planner uses the retained baseline bytes for a
real three-way comparison rather than declaring conflict from hashes alone.
An absent trusted record is `unknown`; a syntactically valid record with an
unsupported schema or compatibility range is `incompatible`; a malformed
record or mismatched blob is an integrity failure. These states must not be
collapsed into current, customization, or ordinary upstream drift.

`commonplace-status` reads only the aggregate classification and stable action
routes needed for its compact default. Per-file evidence belongs to structured
output or an explicit installer-state drill-down. Status remains read-only and
continues to exclude review-system state unless `--review` is supplied.

### Operativity path

The decision becomes operative through one coordinated path:

- the package-owned scaffold/install projection enumerates owned destinations,
  canonical inputs, template renders, and projection relations;
- initialization produces and atomically publishes the manifest and exact
  baseline blobs;
- installer-state integrity checks verify schema support, referential closure,
  and blob hashes;
- project status consumes aggregate classifications and offers stable
  drill-down or upgrade-plan actions;
- the non-mutating upgrade planner consumes the same manifest, current bytes,
  proposed upstream bytes, and baseline blobs; and
- source-checkout, wheel, template, skill-projection, legacy, corruption,
  interruption, and offline-conflict fixtures exercise the complete path.

The manifest and blobs carry binding force only after those consumers activate
together or behind an explicit staged boundary. Writing state without its
integrity and consumption paths does not implement the decision.

## Considered alternatives

### Create a root `.commonplace/` provenance store

Rejected after the duplicate guard found the installed-product design already
owns the same identities and transitions. A second manifest could disagree
with installer ownership, desired projection, or accepted hashes. The exact
path is less important than keeping one owner; this proposal follows the
installed-product state instead of establishing a competing project-control
root.

### Record package or project version only

Rejected by the worked fixture. Equal version strings survived a local edit
without any diagnostic. A version identifies a release label, not the rendered
bytes in one project.

### Record destination hashes and retrieve the old package on demand

Rejected as the complete baseline. Hashes cheaply identify which side changed,
but an old package may be absent locally, unavailable from the network, or may
not represent an editable-source installation. Without prior bytes, a
both-sides-changed case cannot produce an offline three-way plan.

### Retain one prior copy per destination

Rejected because projections repeat canonical content. The measured install
had 760 destinations and 734 unique blobs. Destination entries remain separate
for drift detection, while content addressing retains shared bytes once.

### Retain the originating wheel

Rejected because editable-source initialization has no originating wheel and a
wheel contains command code, metadata, and dependencies outside the installed
projection baseline. The measured wheel was also larger than the compressed
complete-input probe. A wheel hash remains useful source identity when a wheel
was the producer.

### Use Git history as the baseline

Rejected as a requirement. Valid initialized projects need not be Git
repositories, Commonplace commands do not assign Git semantic authority in
downstream projects, and archives or shallow copies may lack the needed
history. Git may still assist inspection when available.

### Put the baseline in `kb/reports/state/` or the Commonplace store

Rejected because report-state payloads are ignored and machine-local, while
the operational SQLite store is not created by default status and currently
owns freshness and review state. Project provenance must travel with a plain
directory or clean clone and must not make review-store creation a prerequisite
for installation inspection.

## Consequences

Project status and upgrade planning gain one shared, inspectable account of
what the installer established. Local edits and upstream changes become
different facts. Projected skills remain independently checked without
duplicating their prior content. A customized project can prepare an offline
three-way upgrade after the active command version has changed.

The installed product becomes larger. The measured clean baseline contained
about 5.28 MB of unique raw content; a format-neutral gzip-tar probe occupied
about 1.76 MB. The exact retained cost will depend on encoding and corpus
growth. Content addressing prevents projection multiplicity from multiplying
that cost, but it does not make baseline retention free. The producer must own
garbage collection, interrupted publication, corruption diagnosis, and
recovery.

Portable generated control state enters the installed project and may enter
its version history. It is not authored KB content, a report, or a substitute
for the package-owned scaffold manifest. Documentation and tooling must keep
those roles distinct. Operators may inspect the state, but ordinary semantic
editing of it is unsupported; a changed or incomplete record is diagnosed
rather than trusted.

The decision stops at identity, baseline retention, deterministic
classification, and non-mutating upgrade planning. It does not authorize
automatic replacement, conflict resolution, pruning, baseline adoption,
receipt design, generic operation packets, review-state defaults, or a general
content-addressed project store. Apply and receipt behavior require the later
authority decision named by the workshop plan. The measurements come from one
Linux fixture at one corpus size; performance and storage tests must remain in
the implementation suite rather than becoming universal constants.

