# Installed-product decision: one disjoint-root, evidence-local projection

**Status:** concrete workshop recommendation for the successor installation
ADR and the I1/I2/I3/V1 implementation program. This file is not system
authority.

**Decision date:** 2026-08-27

**Measured tree:** tracked files at
`bade480fed0694ef9a688d85d5542ebd847a6e59`. Untracked files and the operator's
uncommitted work were excluded from size and graph measurements. Contradiction
counts remain those reproduced at `6660bd2a` in the
[witness baseline](./baseline-2026-08-27.md).

## Goal

Define the product installed into a host project so its topology, paths,
ownership, validation, and upgrade behavior can be implemented as one
contract. The result must preserve a host project's independent KB, install a
locally useful Commonplace library, and avoid treating one KB as a special
subtree of another.

## Vocabulary

This design needs three system-wide compounds. Their hyphenated forms identify
the technical meanings; the corresponding ordinary words keep their ordinary
English meanings.

- **`kb-root`** — the concrete directory that bounds one independently
  operated KB in one materialized tree. Type resolution, collection
  participation, tag membership, and root-relative paths stop at this
  boundary. Declared `kb-root`s in one product are pairwise disjoint: no root
  is an ancestor of another.
- **`install-projection`** — the deterministic source-to-installed transform
  that chooses files, rewrites projection-sensitive paths, and records the
  result.
- **`installed-product`** — the complete materialized result placed in a host
  project: the host scaffold, the projected Commonplace library, runtime
  projections, and installer state.

`namespace` remains ordinary local terminology when useful. It is not a new
system-wide kind. This decision does not use it to explain the product
topology. `knowledge root`, `logical root`, and `shared-types root` are also not
introduced as technical terms.

## Recommendation

Ship one default **hybrid evidence-local edition**. Do not add an edition flag
yet.

The edition contains:

1. every tracked artifact in the Commonplace methodology core:
   `kb/notes/`, `kb/reference/`, and `kb/instructions/`;
2. the Commonplace root's global and collection-local type contracts;
3. a read-only framework evidence collection containing the least set of
   tracked source analyses needed to close source-to-source links reachable
   from the methodology core; and
4. user collection heads, operating directories, the control-plane template,
   selected host-root type replicas, and promoted skill projections required
   to operate a host KB.

Materialize the installed Commonplace library at
`commonplace-library/kb/`. Keep the host KB at `kb/`. These are sibling,
pairwise-disjoint `kb-root`s. The source checkout still has one Commonplace
`kb-root`, at `kb/`; the install projection changes its physical location.

The existing reader install at `commonplace/kb/` remains the full-corpus
vendoring option. That path is deliberately not reused for the curated
installed library. A project may therefore carry the installed product and an
explicit reader checkout without a path collision.

Raw captures under `kb/sources/.snapshots/` never enter the package. Do not
ship the whole `kb/agent-memory-systems/` or `kb/agentic-systems/` review
corpora, articles, this repository's reports, tasks, log, or workshops. Links
that need those first-party artifacts become immutable
source-revision-pinned publication links. A link that needs an original
external source becomes that source's canonical URL. The projection must
distinguish those meanings; it must not replace Commonplace analysis with the
evidence that analysis interpreted.

## Concrete topology

The same Commonplace KB has one identity and different physical paths in two
projections:

| Projection | `kb-root` identity | Physical directory | Role |
|---|---|---|---|
| Commonplace source checkout | `commonplace-kb` | `kb/` | Canonical framework KB and authoring source |
| Initialized host project | `host-kb` | `kb/` | Independently operated, user-owned host KB |
| Initialized host project | `commonplace-kb` | `commonplace-library/kb/` | Read-only projection of the Commonplace library |
| Optional reader checkout | explicitly selected reader target | `commonplace/kb/` | Full Commonplace repository vendored for reading; not automatically joined to host operations |

`commonplace-library/` is the installed product container. It is not a
`kb-root`; its `kb/` child is. Runtime skill directories are projection
surfaces, not KB roots.

The invariant is structural:

> Declared `kb-root`s are pairwise disjoint. No `kb-root` is an ancestor of
> another.

Consumers must not recover this invariant by scanning for nested roots and
subtracting them from an outer root. An explicit cross-root navigation action
may union separately resolved results. It does not transfer collection
participation, tag marks, type scope, or ownership between roots.

## Root discovery

Root discovery is explicit rather than recursive:

- a Commonplace source checkout uses its declared source root, `kb/`;
- an initialized project always has the host root `kb/` and reads the
  installed Commonplace root from installer state;
- a caller may explicitly select a reader checkout or another declared target;
  its mere presence below the project does not join it to host operations;
- startup and validation reject overlapping declared roots before traversing
  collections.

Within each selected root, collection discovery remains recursive and
contract-based: a directory containing `COLLECTION.md` is a collection. This
keeps user-created collections visible without adding them to package
configuration. A product-wide operation first selects declared roots, then
discovers collections independently inside each root.

## Type identity and resolution

Each KB owns its type contracts:

- the source Commonplace root owns `kb/types/`;
- the installed Commonplace root owns `commonplace-library/kb/types/`;
- the host root owns `kb/types/`;
- framework type contracts required by host-root operations are explicit
  `commonplace-replica` files in the host root, while user additions remain
  `user-owned`.

A `kb/...` type pointer is relative to the artifact's owning `kb-root`, not to
the project or repository root. Its canonical identity therefore includes the
root identity and the root-relative path. The text `kb/types/note.md` in two
different roots does not silently name one shared file.

Collection-local pointers remain file-relative. Schema references and other
root-relative paths obey the same boundary. A type resolver may not fall
through from one root to another. If a host operation needs a framework type,
the manifest must project that file into the host root and record its
ownership; shared physical placement is not an implicit dependency mechanism.

Type collections remain real collections. They are non-participating or
tag-prohibited because of their artifact role, not because they sit outside a
KB root.

## Cross-root links

The installed Commonplace library must be closed without depending on the host
root. A host artifact may author an explicit physical link into
`commonplace-library/kb/`, and a product-level navigation command may show
results from both roots. Those are cross-root references or unions, not shared
membership.

Projection-sensitive library links are rewritten relative to the installed
Commonplace root. Omitted first-party targets are externalized according to the
bundle policy below. No consumer may interpret a relative link, type pointer,
or tag mark by silently searching another root.

## Evidence

### The current installed cut is neither closed nor declared once

The live [scaffold manifest](../../../src/commonplace/scaffold_manifest.py)
projects three library trees: notes, reference, and instructions. It also
projects shared and operational types. The wheel and sdist repeat their own
source-tree lists in [pyproject.toml](../../../pyproject.toml), so the manifest
does not yet own package membership. The
[init implementation](../../../src/commonplace/cli/init_project.py) copies
source bytes directly and preserves every differing existing target. It has no
root metadata, link projection, prior-version baseline, or terminal upgrade
transition.

At the workshop baseline, a pristine install had 532 missing-link warnings
across 181 files and one projection-specific type failure. The missing edges
included 335 edges into `kb/sources/`, 101 into
`kb/agent-memory-systems/`, and 31 into `kb/agentic-systems/`. The normal
validation procedure skipped all three nested library collections. These are
I2 and V1 witnesses, not merely stale documentation.

### Current size and graph measurements

A fresh wheel built from the measured tree into `/tmp` was 2,248,337 bytes. It
contained 761 entries and 5,348,641 uncompressed bytes. Its shipped KB core and
support inputs account for 656 tracked files and 4,682,389 raw bytes.

The table below uses `git ls-files` membership. "Deflated" is a comparative
payload estimate, not an exact future wheel size.

| Candidate proxy | Tracked files | Raw bytes | Deflated bytes | Meaning |
|---|---:|---:|---:|---|
| Curated operational hard floor | 130 | 612,421 | 246,382 | Current instructions plus type support, without the theory and reference dependencies needed for a useful edition |
| Thin current core | 656 | 4,682,389 | 1,867,513 | Current three library collections plus type support |
| Recommended hybrid | 835 | 6,606,412 | 2,632,303 | Thin core plus the measured source-analysis closure and source collection heads |
| Self-contained durable-corpus proxy | 1,174 | 12,004,929 | 4,520,848 | Core plus all tracked sources, agent-memory reviews, agentic-system analyses, and articles; operational residue and raw snapshots excluded |

The hybrid proxy would put a wheel near 3.0 MB if code and metadata stayed at
their current size. The self-contained proxy would put it near 4.9 MB. Size is
not, by itself, a reason to reject self-containment.

From the current core, direct local links reached 129 tracked source files
(1,442,330 bytes), 37 agent-memory-system files (860,140 bytes), and five
agentic-system files (75,175 bytes). Literal transitive closure also pulled in
workshops, logs, tasks, reports, source code, and scripts. It is therefore not
a product boundary.

The narrower source-only fixed point is coherent. At the measured commit it
contained 177 files and 1,916,068 raw bytes (761,215 deflated bytes). These
counts are observations, not constants. The compiler recomputes the set and
the product test compares declared inputs with output.

## Option disposition

### Self-contained methodology library

Technically affordable and strongest offline, but it makes every comparative
review part of the installed upgrade surface without closing links to all
implementation and historical witnesses. Keep full-corpus vendoring as the
reader product.

### Thin publication

Matches the current advertised bundle, but externalizes 335 source-evidence
edges and removes modest, useful evidence from local search. Keep it only as a
future response to demonstrated redistribution or package-size constraints.

### Curated operational edition

Potentially much smaller, but no declared workload set identifies which
methodology artifacts promoted procedures need. Reconsider it only as a
separately evaluated edition with workload fixtures and a navigation contract.

### Hybrid evidence-local edition

Selected. It retains the complete methodology and the bounded source-analysis
closure while externalizing larger descriptive review collections.

## Exact bundle rule

Let `C` be every tracked file under `kb/notes/`, `kb/reference/`, and
`kb/instructions/`, plus Commonplace type and operational support files
declared by the manifest.

Let `E0` be every eligible tracked source-analysis artifact under
`kb/sources/` targeted by a local Markdown link from a Markdown artifact in
`C`. A snapshot is never eligible. Let `E` be the least fixed point containing
`E0` and every eligible source-analysis artifact targeted from an artifact
already in `E`.

The projected Commonplace root contains:

- the framework collection files in `C`;
- the evidence files in `E`;
- a projection-specific `sources/COLLECTION.md` and generated
  `sources/README.md`;
- collection-local evidence types under `sources/types/`; and
- the root-local global type collection under `types/`.

The source-side sources contract is not copied verbatim: it governs a writable
collection with local snapshots, while the projected evidence collection is
read-only. Edges from `E` to omitted first-party material become immutable
Commonplace publication links. Edges back into `C` remain local.

## Ownership vocabulary

Ownership is per target file. The hyphenated values below have formal meaning
only in a declared `ownership` field:

| Value | Examples | Upgrade rule |
|---|---|---|
| `commonplace-managed` | Files in `commonplace-library/kb/` | Replace when unchanged from the recorded base; preserve and report local forks |
| `commonplace-replica` | `.agents/skills/cp-skill-*/`, `.claude/skills/cp-skill-*/`, and selected host-root type replicas | Same hash-aware transition, but never authority |
| `user-seed` | Initial user collection contracts and landings; `AGENTS.md.template`; generic work and sources heads | Create once, then transfer authority to the user; never recreate a deliberate deletion automatically |
| `user-owned` | User artifacts, added collections and types, logs, reports, workshops, and tasks | Never overwrite, delete, or claim provenance |
| `installer-state` | `commonplace-library/.installed-product.json` | Replace atomically only after successful reconciliation; invalid or missing state makes automatic replacement fail closed |

These values replace the broader `framework-managed`, `framework-replica`, and
`seeded-user` labels considered earlier. The scoped names reduce accidental
collision with ordinary uses of “framework” and “seed.”

## Manifest and projection policy

Extend `ScaffoldManifest` rather than create a parallel topology inventory.
Do not put topology, artifact role, ownership, and materialization into one
`kind` enum. They are independent axes. Manifest entries or derived product
records must express, as applicable:

- stable source identity and target path;
- owning `kb-root`, or an explicit statement that the target is outside a KB;
- collection discovery or contract-template responsibility;
- ownership value and writability;
- source, generated-template, or replica materialization;
- projection transform and dependency policy; and
- upgrade policy.

The exact Python fields remain an implementation choice. The manifest owns
the seed topology and edition inputs. A build step emits the exact per-file
installed-product manifest. Packaging, init, tests, and documentation consume
or parity-check that output instead of repeating tree lists.

Compile the product as one non-identity projection:

1. resolve Markdown links and `type:` pointers at canonical source locations;
2. classify each target as included-local, omitted-first-party,
   original-external-source, or prohibited/unresolved;
3. map included targets into the projected root and recompute relative URLs;
4. apply immutable URL dispositions to omitted first-party targets;
5. retain an original URL only when the edge actually cites that source; and
6. fail when no legal disposition exists.

Use the existing fenced-code-safe relocation tokenizer and relative-link
formatter. Editable-source and wheel builds run the same compiler and produce
byte-identical product trees for the same inputs and revision. The compiler
output, not a source-tree copy, is the release target. V1 validates each
declared root and collection; the packaged-product test raises missing-link
warnings to release failures.

## Terminal upgrade policy

Persist `commonplace-library/.installed-product.json` with the edition,
package version, source revision, projection-format version, declared roots,
and one record per owned target. Managed and replica records include source
identity, target path, ownership, last accepted base hash, and desired hash.

Build and validate the complete desired tree before touching the project. Then
apply these transitions:

| Current state | Ordinary upgrade action |
|---|---|
| New managed target is absent | Create it and record the new base hash |
| Desired target already exists without ownership state | Preserve and report an ownership conflict |
| Current bytes equal the recorded base | Replace atomically and advance the base |
| Current bytes equal the new desired bytes | Adopt the desired bytes as the new base without rewriting |
| Current bytes differ from base and desired | Preserve, report a local fork, retain the old base, and record the new desired hash |
| Recorded managed target is absent | Preserve the deletion and report a missing fork; restore only through explicit repair |
| Upstream removed a clean managed target | Report it as obsolete; remove only through explicit prune |
| Upstream removed a modified managed target | Preserve it as an obsolete fork; refuse ordinary prune |
| `user-seed` or `user-owned` target changed or disappeared | Do not overwrite or recreate it |

Ordinary upgrade never deletes a file. Pruning is a separate deliberate mode
that resolves and prints exact targets before mutation.

### Legacy nested-layout migration

Existing initialized projects may contain the old projected tree at
`kb/commonplace/`. I1 must treat that as a layout migration, not as evidence
that nested KB roots remain supported:

1. recognize only files that match a known legacy projection or a recorded
   prior base;
2. compile and validate the desired `commonplace-library/kb/` tree first;
3. install or reconcile the new tree through the ownership transition;
4. preserve unknown and locally edited legacy files as explicit forks;
5. report clean legacy paths as obsolete; and
6. remove them only through a deliberate prune after the new product is valid.

The migration must not recursively delete `kb/commonplace/` or infer ownership
from its path. Preserve-only reruns may remain an interim limitation, but they
do not close I1.

## Consequences for the open plans

- [I3](./plans/i3-installed-topology.md) supplies the `kb-root` declaration,
  pairwise-disjoint guard, root-local type semantics, and contract-based
  collection discovery.
- [V1](./plans/v1-validate-all.md) selects explicit roots, then recursively
  validates every collection and uncovered type surface in each one.
- [I2](./plans/i2-install-projection-integrity.md) compiles the hybrid edition
  into `commonplace-library/kb/` and dispositions every dependency.
- [I1](./plans/i1-shipping-upgrade.md) implements ownership-aware transition
  and the legacy `kb/commonplace/` migration.
- [T1](../tag-contract-convergence/README.md) consumes `kb-root` isolation;
  it no longer needs an outer-root exclusion for an embedded library.

The [consumer impact ledger](./disjoint-root-impact-ledger.md), [successor ADR
draft](./successor-installation-adr-draft.md), and [implementation
packets](./disjoint-root-implementation-packets.md) carry this recommendation
into reviewable future changes. None of these workshop documents activates the
new topology.
