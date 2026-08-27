# Installed-product decision: one hybrid evidence-local edition

**Status:** concrete recommendation for the successor installation ADR and the
I1/I2/I3/V1 implementation program. This workshop file is not system
authority.

**Decision date:** 2026-08-27

**Measured tree:** tracked files at
`bade480fed0694ef9a688d85d5542ebd847a6e59`. Untracked files and the operator's
uncommitted workshop work were excluded from size and graph measurements. The
contradiction counts remain those reproduced at `6660bd2a` in the
[witness baseline](./baseline-2026-08-27.md).

## Recommendation

Ship one default **hybrid evidence-local edition**. Do not add an edition flag
yet.

The edition contains:

1. every tracked artifact in the Commonplace methodology core:
   `kb/notes/`, `kb/reference/`, and `kb/instructions/`;
2. the shared global types and the framework-supplied operational type specs;
3. a read-only framework evidence collection containing the least set of
   tracked source analyses needed to close source-to-source links reachable
   from the methodology core; and
4. user collection heads, operating directories, the control-plane template,
   and promoted skill projections required to operate a host KB.

Install the framework collections under `kb/commonplace/`, including the new
evidence collection at `kb/commonplace/sources/`. Keep the user's writable
source collection at `kb/sources/`. Raw captures under
`kb/sources/.snapshots/` never enter the package.

Do not ship the whole `kb/agent-memory-systems/` or `kb/agentic-systems/`
review corpora, articles, this repository's reports, tasks, log, or workshops.
Links that need those first-party artifacts become immutable
source-revision-pinned publication links. A link that needs an original
external source becomes that source's canonical URL. The projection must
distinguish those two meanings; it must not replace Commonplace analysis with
the evidence that analysis interpreted.

This boundary keeps the methodology and its immediate source receipts locally
searchable. It externalizes large comparative corpora that are useful for
research but are not needed to operate a host KB. The existing
[reader install](../../../INSTALL.md#reader-install-the-kb-as-a-vendored-reference)
remains the full-corpus option.

## Evidence

### The current installed cut is neither closed nor declared once

The live [scaffold manifest](../../../src/commonplace/scaffold_manifest.py)
projects three library trees: notes, reference, and instructions. It also
projects shared and operational types. The wheel and sdist repeat their own
source-tree lists in [pyproject.toml](../../../pyproject.toml), so the manifest
does not yet own package membership. The
[init implementation](../../../src/commonplace/cli/init_project.py) copies
source bytes directly and preserves every differing existing target. It has no
logical-root metadata, link projection, prior-version baseline, or terminal
upgrade transition.

The current [install guide](../../../INSTALL.md) and root
[README](../../../README.md) accurately describe the implemented thin cut:
they promise methodology but omit external-system reviews and the source
corpus. That description is evidence of the present product, not proof that
its local graph is valid.

At the workshop baseline, a pristine install had 532 missing-link warnings
across 181 files and one projection-specific type failure. The missing edges
included 335 edges into `kb/sources/`, 101 into
`kb/agent-memory-systems/`, and 31 into `kb/agentic-systems/`. The normal
validation procedure skipped all three nested library collections. These are
the I2 and V1 witnesses, not merely stale documentation.

### Current size and graph measurements

A fresh wheel built from the measured tree into `/tmp` was 2,248,337 bytes. It
contained 761 entries and 5,348,641 uncompressed bytes. Its shipped KB core and
support inputs account for 656 tracked files and 4,682,389 raw bytes.

The table below uses `git ls-files` membership. "Deflated" is the sum of each
file compressed with raw DEFLATE at level 6, so it is a comparative package
payload estimate rather than an exact future wheel size.

| Candidate proxy | Tracked files | Raw bytes | Deflated bytes | Meaning |
|---|---:|---:|---:|---|
| Curated operational hard floor | 130 | 612,421 | 246,382 | All current instructions plus global, report, and source types; it omits the theory and reference dependencies that would make this a usable edition |
| Thin current core | 656 | 4,682,389 | 1,867,513 | Current three library collections plus shared and operational type support |
| Recommended hybrid | 835 | 6,606,412 | 2,632,303 | Thin core plus the measured source-analysis closure and source collection heads |
| Self-contained durable-corpus proxy | 1,174 | 12,004,929 | 4,520,848 | Core plus all tracked sources, agent-memory reviews, agentic-system analyses, and articles; still excludes operational residue and raw snapshots |

The hybrid proxy would put a wheel near 3.0 MB if code and metadata stayed at
their current size. The self-contained proxy would put it near 4.9 MB. Size is
therefore not, by itself, a reason to reject self-containment.

Graph shape is the stronger evidence. From the current core, direct local
links reached:

| Target class | Unique tracked target files | Target bytes | Shape |
|---|---:|---:|---|
| `kb/sources/` | 129 | 1,442,330 | 125 ingests, three source analyses/reviews, and the collection contract |
| `kb/agent-memory-systems/` | 37 | 860,140 | 30 individual reviews plus analyses and navigation |
| `kb/agentic-systems/` | 5 | 75,175 | Five analyses |

Following every tracked local target transitively from the core added 368
files and 6,034,215 bytes. It also pulled in `kb/work/`, `kb/log.md`,
`kb/tasks/`, `kb/reports/`, `src/`, and `scripts/`. Literal graph closure is
therefore not a product boundary. It confuses a durable dependency with a
historical or implementation witness.

The narrower source-only fixed point is coherent. Start with tracked source
analysis files directly linked from the core, then follow only local links to
other tracked source analysis files until stable. At the measured commit this
set contained 177 files and 1,916,068 raw bytes (761,215 deflated bytes). The
counts are observations, not constants to hardcode. The compiler recomputes
the set and the product test compares its declared inputs with its output.

## Option disposition

### Self-contained methodology library

This is technically affordable and gives the best offline research surface.
It is not selected because collection inclusion still does not close links to
implementation and operational witnesses. It would require the same
projection compiler as every other option while adding the whole 3.92 MB
agent-memory corpus and 3.14 MB source collection, even though the current core
directly selects only a fraction of each. It also makes every external-system
review part of the installed upgrade and freshness surface.

Keep full-corpus vendoring as the deliberate reader product instead of making
every operating KB carry the research repository.

### Thin publication

This matches the current advertised bundle and is the smallest edition that
retains all methodology. It is not selected because it would externalize the
335 source-evidence edges in the baseline. That makes ordinary evidence
inspection depend on network access and removes the source analyses from local
search, despite their modest payload. Thin publication remains a useful
fallback if redistribution or package-size constraints later become concrete;
neither is currently evidenced strongly enough to choose it.

### Curated operational edition

This could become much smaller, but there is no declared workload set that
identifies which notes and reference pages the promoted procedures need. The
612 KB hard floor is not a real product: it retains procedure bodies while
discarding their explanatory and architectural dependencies. Selecting a
curated core now would invent a second content-classification program before
I2 has made the current projection sound.

Reject this as the default. Reconsider it only as a separately evaluated
edition with workload fixtures and a navigation contract.

### Hybrid evidence-local edition

This is selected. It retains the complete methodology instead of guessing
which explanations an installed agent will need. It keeps the bounded source
analysis closure local and externalizes the larger descriptive review
collections. Its selection rule is mechanical, but each omitted edge still
needs an authored semantic disposition. This is a better trade than either
including every reachable collection or putting all evidence behind the
network.

## Exact bundle rule

Let `C` be every tracked file under `kb/notes/`, `kb/reference/`, and
`kb/instructions/`, plus the shared framework types and operational support
types declared by the scaffold manifest.

Let `E0` be every tracked source-analysis artifact under `kb/sources/` that is
the target of a local Markdown link originating in a Markdown artifact in
`C`. A source-analysis artifact is an ingest report, source review, or another
explicitly declared tracked analysis type. A snapshot is never eligible.

Let `E` be the least fixed point containing `E0` and every eligible tracked
source-analysis artifact targeted by a local Markdown link from an artifact
already in `E`.

The shipped knowledge bundle is:

- all framework collection files in `C`;
- all evidence files in `E`;
- a read-only, projection-specific `kb/commonplace/sources/COLLECTION.md`;
- a generated `kb/commonplace/sources/README.md` that lists only the projected
  evidence surface;
- collection-local evidence type specs under
  `kb/commonplace/sources/types/`; and
- the shared and user-scaffold surfaces declared below.

The source-side `kb/sources/COLLECTION.md` is not copied verbatim into the
framework evidence collection. It governs a writable source collection with
local snapshots. The installed framework evidence collection is read-only and
needs a contract that says so. The canonical source type specs may project to
both `kb/commonplace/sources/types/` for framework evidence and
`kb/sources/types/` for the user's writable collection; those outputs have
different ownership classes.

The fixed-point rule is a build input, not permission to silently expand into
another collection. An edge from `E` to an agent-memory review, agentic-system
analysis, article, or another omitted first-party artifact is externalized to
an immutable Commonplace publication. An edge back into `C` remains local.

## Logical roots and topology

Use three logical-root identities:

| Logical root | Physical boundary | Meaning |
|---|---|---|
| `commonplace-library` | `kb/commonplace/` | Read-only framework knowledge. The directory is a namespace, not a collection; its contract-bearing children are collections. |
| `host-kb` | Contract-bearing collections under `kb/` that are outside `kb/commonplace/` and are not the shared type collection | User-owned knowledge and operating collections, including `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/sources/`, and `kb/work/`. |
| `shared-types` | `kb/types/` | The global type collection. It is a real collection for discovery and conformance, but it is support shared by both knowledge roots and does not participate in either root's tag membership. |

`kb/commonplace/notes/`, `reference/`, `instructions/`, and `sources/` all
belong to `commonplace-library`. Top-level user collections belong to
`host-kb`. A user-created collection inherits `host-kb` when it is outside a
more specific declared logical root. Runtime skill directories are projection
surfaces, not KB roots.

Collection discovery remains contract-based and recursive. Logical-root
metadata controls membership and projection semantics; it must not cause
`kb/types/COLLECTION.md` to disappear from collection discovery. A consumer
that wants knowledge artifacts may exclude `shared-types` explicitly without
redefining "collection."

## Ownership classes

Ownership is per target file, not per directory. This is required because
`kb/types/`, `kb/sources/types/`, and runtime skill directories mix framework
files with user additions.

| Class | Examples | Write and upgrade rule |
|---|---|---|
| `framework-managed` | Files under `kb/commonplace/`; known global type specs in `kb/types/`; framework command-facing source/report type specs | Read-only by convention. Upgrade unchanged files automatically. Preserve and report local edits as forks. |
| `framework-replica` | `.agents/skills/cp-skill-*/` and `.claude/skills/cp-skill-*/` | Derived from canonical instructions. Use the same hash-based transition as framework-managed files, but never treat a projection as authority. |
| `seeded-user` | User `COLLECTION.md` and `README.md` heads; `AGENTS.md.template`; user source ignore file; a generic work contract and landing | Create on a fresh install, then transfer authority to the user. Never overwrite or recreate automatically after the seed is recorded as accepted or deliberately removed. Report a newer template as available. |
| `user-owned` | User artifacts, logs, reports, workshops, tasks, added types, and added collections | Never overwrite, delete, or claim provenance. The manifest may declare a directory role without owning its later contents. |
| `installer-state` | `kb/commonplace/.installed-product.json` | Machine-owned provenance. Replace atomically only after a successful reconciliation; a missing or invalid record makes automatic upgrade fail closed. |

The heads of the shared `kb/types/` collection are `seeded-user`, because a
project may extend that collection and curate its landing. The known framework
type-spec files beneath it are `framework-managed`. Presence in the same
directory does not blur those file-level rules.

## Projection policy

### One executable inventory

Extend `ScaffoldManifest` rather than create a parallel topology file. Each
declared entry needs at least:

- stable artifact/source identity;
- source and target path or generated-template identity;
- kind (`namespace`, `collection`, `support`, `template`, or `projection`);
- logical root;
- ownership class and writability;
- projection transform and dependency policy; and
- upgrade policy.

The edition declaration owns the seed roots and evidence-closure rule. A build
step emits the exact per-file product manifest. Hatch configuration, init,
tests, and documentation consume or parity-check that output; they do not
repeat the edition as hand-maintained tree lists.

### One deterministic compiler

Compile the installed product as a non-identity projection:

1. resolve each Markdown link and `type:` pointer at its canonical source
   location;
2. classify the target as included-local, omitted-first-party,
   original-external-source, or prohibited/unresolved;
3. map included targets to installed paths and recompute the URL from the
   installed source path;
4. apply an explicit immutable URL override for omitted first-party targets;
5. retain an original source URL only when the edge actually cites that source;
   and
6. fail if an edge lacks a legal disposition under the source collection's
   link grammar.

Use the existing fenced-code-safe relocation tokenizer and relative-link
formatter. Do not add a second Markdown regex rewriter. Global type pointers
remain repository-relative `kb/types/...`; collection-local pointers are
rewritten or authored file-relative under the projected collection.

A published product records a source revision and uses commit-pinned Commonplace
URLs for omitted first-party material. The rendered site's moving URL may be a
reader convenience, but it is not the evidence identity. Editable-source and
wheel builds run the same compiler and must produce byte-identical product
trees for the same inputs and revision.

The compiler output, not the source checkout, is the release target. Its audit
fails on an unresolved local edge, an invalid type pointer, a local link into
an omitted artifact, an illegal externalized relation, or a snapshot entering
the bundle. V1 then validates every declared collection, and the product test
raises missing-link warnings to release failures.

## Terminal upgrade policy

A version marker is insufficient. Persist
`kb/commonplace/.installed-product.json` with the edition, package version,
source revision, projection-format version, and one record per owned target.
For a managed or replica file, record its source identity, target path,
ownership class, last accepted base hash, and desired hash for the selected
package.

Build and validate the desired tree before touching the project. Then apply
these transitions:

| Current state | Ordinary upgrade action |
|---|---|
| New managed target is absent | Create it and record the new base hash. |
| A new desired target already exists without an ownership record | Preserve it and report an ownership conflict; do not adopt or overwrite it implicitly. |
| Current bytes equal the recorded base and a new desired version exists | Replace atomically; the new desired hash becomes the base. |
| Current bytes already equal the new desired bytes | Accept them as the new base without rewriting. |
| Current bytes differ from both base and desired | Preserve them, report a local fork, retain the old base, and record the new desired hash. |
| A recorded managed target is absent | Preserve the local deletion and report it as a missing fork; restore it only through an explicit repair action. |
| Upstream removed a managed target whose current bytes equal its base | Report it as obsolete and keep it during ordinary upgrade. An explicit prune may delete it. |
| Upstream removed a managed target whose current bytes differ from its base | Preserve it as an obsolete fork. Prune refuses it unless the operator explicitly exports or force-removes that exact path. |
| Seeded-user or user-owned target exists, differs, or was deliberately removed | Do not overwrite or recreate it. Report only the relevant template or topology consequence. |

Projected skills use the same transition table as other framework replicas.
Ordinary upgrade never deletes a file. Pruning is a separate deliberate mode
that prints exact targets before mutation.

If installer state is missing, corrupt, or inconsistent, do not guess from
presence. Abort automatic replacements and deletions before mutation. A fresh
install may bootstrap state only when its target set is demonstrably new. A
legacy adoption path may baseline files byte-identical to a known projection;
all other existing files remain unresolved forks until the operator classifies
them.

Write the new state only after all planned writes succeed. A preserved fork
keeps its earlier accepted base and the current package's desired hash, so a
later manual reconciliation to the desired bytes can be recognized without
guessing.

This is the terminal policy. Preserve-only reruns may be documented as an
interim limitation, but they do not close I1.

## Consequences for the open plans

- [I3](./plans/i3-installed-topology.md) can now implement the three logical
  roots, file ownership, work templates, and contract-based discovery.
- [V1](./plans/v1-validate-all.md) can enumerate all visible collection
  contracts while treating `shared-types` as an explicit support root.
- [I2](./plans/i2-install-projection-integrity.md) can compile the fixed hybrid
  edition and disposition every edge against one product manifest.
- [I1](./plans/i1-shipping-upgrade.md) can replace ADR 021's marker promise
  with the base/desired hash transitions above.

The successor ADR should adopt this packet's edition, roots, ownership
classes, projection boundary, and terminal transitions together. Splitting
those decisions across four patches would recreate the inconsistency this
workshop is meant to remove.
