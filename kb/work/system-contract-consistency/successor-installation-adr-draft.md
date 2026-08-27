# Draft ADR — Compile a disjoint, ownership-aware installed product

**Status:** workshop draft only. It is not an accepted ADR and has no binding
force.

**Promotion rule:** move this decision into `kb/reference/adr/` only in the
implementation packet that makes its operativity paths true, or with a precise
staged-activation boundary that prevents current guidance from claiming the
future product.

## Context

The current installer copies selected Commonplace collections below the host
KB at `kb/commonplace/`, keeps some type contracts at host `kb/types/`, and
projects skills into runtime directories. This produces two incompatible views
of the tree. Some consumers treat `kb/` as one KB; others treat
`kb/commonplace/` as a separate library and must exclude it from host scope.
The source checkout has no `kb/commonplace/`; that path exists only in the
installed projection.

At the 2026-08-27 audit baseline, a pristine install produced 532 missing-link
warnings across 181 files and one projection-specific type failure. The normal
`all` validation procedure skipped the three nested library collections.
Accepted ADR 021 also promised a marker-backed refresh that the installer never
implemented. The physical nesting, incomplete projection, inconsistent
discovery, and absent ownership baseline are one installed-product problem.

## Decision

### Vocabulary

Adopt these hyphenated technical terms:

- `kb-root`: the concrete boundary of one independently operated KB in one
  materialized tree;
- `install-projection`: the deterministic source-to-installed compilation;
- `installed-product`: the whole result placed in a host project.

Keep `namespace` as ordinary or local terminology. Do not introduce `logical
root`, `knowledge root`, or `shared-types root` as project vocabulary.

### Disjoint roots

Every declared pair of `kb-root`s in one product is disjoint. No root may be an
ancestor of another.

The Commonplace source checkout declares `commonplace-kb` at `kb/`. A fresh
initialized project declares:

- `host-kb` at `kb/`; and
- `commonplace-kb` at `commonplace-library/kb/`.

The existing reader checkout at `commonplace/kb/` remains a separate,
explicitly selected full-corpus target. Its presence never joins it to host or
installed-library operations automatically.

### Installed edition

Install one hybrid evidence-local edition. It contains the complete
methodology core, root-local Commonplace type contracts, and the least
source-analysis closure needed by the core. It omits large comparative review
collections and operational residue. Projection converts omitted first-party
dependencies to immutable revision-pinned Commonplace publication links and
original-source dependencies to canonical source URLs.

### Root-local paths and types

Collection discovery runs recursively within an already selected `kb-root`.
Root selection itself is explicit and rejects overlap.

A `kb/...` pointer resolves relative to the artifact's owning `kb-root`.
Canonical artifact and type identity includes the root identity and
root-relative path. Resolution never falls through into another root.

The Commonplace root contains its own `types/`. The host root contains its own
`types/`. Commonplace type files needed by host operations are explicit
replicas recorded by the product manifest; they are not a physically shared
third root.

### Manifest and projection

Extend `ScaffoldManifest` as the package-owned seed topology and edition
inventory. Keep root membership, collection role, ownership, and
materialization as separate fields or records rather than one `kind` enum.
Generate one exact per-file product manifest from it.

Wheel, sdist, editable-source operation, and initialization invoke the same
install projection. The compiler resolves source paths before mapping them,
rewrites included local targets, externalizes omitted targets only through
declared dispositions, rejects snapshots, and fails on unresolved
dependencies. The compiled tree is the release target.

### Ownership and upgrade

Record file ownership with the scoped values `commonplace-managed`,
`commonplace-replica`, `user-seed`, `user-owned`, and `installer-state`.
Formal meaning attaches to the value in the declared ownership field.

Write `commonplace-library/.installed-product.json` only after a complete
desired tree has been built, validated, and reconciled. For each owned file,
record source identity, target path, accepted base hash, and desired hash.

Ordinary upgrade replaces unchanged Commonplace-owned files, preserves and
reports local forks, never overwrites user-owned files, and reports upstream
removals without deleting them. Deletion is an explicit prune operation.
Missing or invalid installer state makes automatic replacement fail closed.

Legacy projects with `kb/commonplace/` migrate by installing and validating
the new disjoint root first. Known clean legacy paths become explicit prune
candidates. Modified, unknown, or deleted legacy paths remain preserved forks.
The migration never recursively deletes the legacy directory.

### Operativity path

This decision becomes operative through all of these surfaces:

- manifest-derived root and per-file product records;
- root-aware collection, path, type, validation, review, tag, and publishing
  consumers;
- the projection compiler used by every package/install channel;
- ownership-aware init and upgrade transitions;
- generated templates and promoted skills; and
- packaged-product, cross-root, and legacy-upgrade tests.

The ADR is not accepted as a promise before those consumers either activate
together or have an explicit, truthful staged boundary.

## Considered alternatives

### Keep `kb/commonplace/`

Rejected. It makes one KB an ancestor of another and forces outer-root
consumers to carry exclusion rules. The source and installed topology also
remain needlessly different in their scope semantics.

### Install the curated edition at `commonplace/kb/`

Rejected. That path already belongs to the documented full reader checkout.
Reusing it prevents the two products from coexisting and blurs a compiled
edition with a vendored repository.

### Install at `.commonplace/kb/`

Rejected. The Commonplace library is intended to be browsed, cited, and linked
directly; hiding it makes the product boundary less legible.

### Keep a shared top-level type collection

Rejected. Shared physical placement gives two KBs one mixed-ownership
dependency surface and makes `kb/...` mean different things by location. Small
explicit replicas are easier to identify, validate, and upgrade.

### Thin, curated, or full-corpus editions

The thin edition removes useful local evidence. A curated operational edition
lacks workload evidence. The full corpus is affordable but needlessly expands
the default freshness and upgrade surface. The hybrid edition is selected;
full reader vendoring remains available separately.

## Consequences

The product becomes easier to reason about because root membership is a
positive declaration, not a recursive scan plus exclusions. Type pointers,
tags, collections, and validation receive one common boundary. The reader and
installed editions can coexist. Upgrade gains a truthful ownership baseline.

The change is breaking. Existing installs must move framework content out of
the host root. Host operations may carry explicit replicas of selected type
contracts. Cross-root navigation must name both roots. Path and review
identities that previously assumed one `kb/` must include root identity.

This decision does not create an arbitrary multi-KB registry, allow arbitrary
custom install paths, or claim that cross-root search is exact tag membership.
Those features need separate evidence and decisions.

## Relationship to earlier decisions

The successor preserves ADR 021's intent that installed Commonplace material
is isolated and read-only, but supersedes its physical nesting, collection set,
marker, and refresh mechanism. It supersedes ADR 014's missing-only behavior
for recorded Commonplace-owned files while preserving user-owned safety. It
retains ADR 037's rule that runtime skill copies are projections, but gives
them the same ownership-aware transition as other replicas.

Historical ADRs remain as history and point forward. Current architecture,
installation, validation, navigation, type, and skill documentation change in
the activation packets rather than in this workshop draft.

## Promotion checklist

- The exact root and ownership structures exist in code.
- Pairwise root overlap is rejected.
- Root-local type resolution has no topology fallback.
- Wheel, sdist, editable, and fresh-init projections agree.
- V1 validates both installed roots and raises packaged-product link warnings
  to release failures.
- Legacy clean, modified, missing, unknown, and obsolete files have tested
  transitions.
- Generated templates and promoted skills name the new topology.
- Earlier accepted ADRs and current reference surfaces point to the successor.
