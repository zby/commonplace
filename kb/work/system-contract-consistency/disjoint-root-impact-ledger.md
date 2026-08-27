# Disjoint `kb-root` impact ledger

**Status:** workshop design inventory. No listed production surface has changed
yet.

**Decision source:** [installed-product decision](./installed-product-edition-decision.md)

## Purpose

Make the disjoint-root decision reviewable before implementation by naming
every known consumer class, its current assumption, the replacement rule, the
owning implementation packet, and the acceptance evidence. This ledger is the
first worked application of the proposed contract-change implementation gate.

## Selected topology

| Projection | Root identity | Path |
|---|---|---|
| Source checkout | `commonplace-kb` | `kb/` |
| Initialized project | `host-kb` | `kb/` |
| Initialized project | `commonplace-kb` | `commonplace-library/kb/` |
| Optional reader checkout | explicitly selected reader target | `commonplace/kb/` |

The two initialized-product roots are siblings. Declared `kb-root`s are
pairwise disjoint. The reader checkout is not discovered or joined merely
because it exists.

## Vocabulary disposition

| Candidate | Disposition | Reason |
|---|---|---|
| `kb-root` | Adopt in the successor ADR | Names the boundary used by collection discovery, type resolution, tags, and validation |
| `install-projection` | Adopt in the successor ADR | Distinguishes compilation from copying |
| `installed-product` | Adopt in the successor ADR | Names the complete user-visible result |
| `namespace` | Keep as ordinary or local prose only | The new topology does not need a special nested container kind |
| `logical root`, `knowledge root` | Do not adopt | Both obscure the concrete path boundary |
| `shared-types root` | Reject | Types belong to their owning KB; required host copies are explicit replicas |
| `commonplace-managed`, `commonplace-replica`, `user-seed`, `user-owned`, `installer-state` | Adopt as values in an `ownership` field | Hyphenated, scoped identifiers avoid collisions with ordinary prose |

The earlier single `kind` enum is withdrawn. Collection status, ownership,
root membership, and materialization are orthogonal facts.

## Resolved design choices

### Installed path

The curated installed library uses `commonplace-library/kb/`. Reusing
`commonplace/kb/` would collide with the documented full reader checkout.
Using `.commonplace/kb/` would hide a library meant for direct reading and
linking. Keeping `kb/commonplace/` would preserve the nesting that caused the
outer-root exclusion problem.

### Types

Type contracts are root-local. A `kb/...` pointer resolves against the
artifact's owning `kb-root`. The installed Commonplace root contains its own
`types/`; the host root contains its own `types/`. Framework types needed by
host operations are explicit `commonplace-replica` files in the host root.
Canonical type identity includes root identity and root-relative path.

### Root discovery

Source operation declares `kb/`. Installed operation reads the host root and
the Commonplace library root from installer state. Collection discovery is
recursive only after a root has been selected. It never discovers nested roots
and then subtracts them from an ancestor.

### Installer state

The selected state path is
`commonplace-library/.installed-product.json`. It sits with the installed
product but outside the projected Commonplace KB. State records declared
roots, projection version, edition, source revision, and file ownership/hashes.

## Consumer matrix

| Consumer class | Current assumption or witness | Replacement rule | Owner packet | Acceptance evidence |
|---|---|---|---|---|
| Scaffold and package inventory | `ScaffoldManifest` and `pyproject.toml` independently enumerate source trees and target `kb/commonplace/` | One manifest-owned edition emits a per-file product manifest targeting `commonplace-library/kb/` | I3 foundation, then I2 compiler | Manifest/package parity; wheel and editable outputs match |
| Init materialization | `init_project.py` copies bytes into one top-level `kb/` tree and discovers promoted skills below `kb/commonplace/instructions/` | Materialize a compiled product, write installer state after success, and derive skill sources from the declared Commonplace root | I2 fresh install; I1 reconciliation | Fresh-install fixture has two disjoint roots and valid skill projections |
| Project and root paths | `project_paths.py` exposes one `workspace_root/kb` and recursively treats descendants as one space | Introduce explicit root identity/path objects; reject overlap; never infer a foreign root by depth | I3 foundation | Source, installed, and reader fixtures select only declared roots |
| Collection discovery | `collection_dirs()` recursively scans one tree and excludes every path containing `types` | Discover every `COLLECTION.md` independently within each selected root; prune only validation-ignore boundaries | I3 foundation | Root-local collection sets include type collections and exclude ignored fixtures |
| Collection conformance | Review code excludes contracts under `types` | Review each discovered collection according to its role; being a type collection is not grounds for disappearance | I3, V1 | Type collections are covered exactly once |
| Type and schema resolution | `kb/...` resolves from workspace root; a special fallback rewrites `kb/commonplace/types` to `kb/types` | Resolve `kb/...` from owning `kb-root`; prohibit fall-through; remove topology-specific fallback | I3 foundation, I2 projection | Identical pointer strings resolve independently in host and Commonplace fixtures |
| Validation suite | One-depth skill glob misses nested library collections; library and host are mixed under one path | Select declared roots, recursively discover their collections, continue across failures, and aggregate structured results | V1 | Every declared root, collection, and uncovered type spec is examined once |
| Note lookup and path identity | Helpers assume one `kb/` and often return workspace-relative identities | Carry root identity with root-relative artifact paths; require explicit union for cross-root navigation | I3 foundation | Same relative path in two roots remains unambiguous |
| Tags and exact membership | T1 readiness expected nested/foreign-root pruning | Resolve membership within one selected disjoint root; no embedded-root exclusion exists | Tag phases 1–3 | Host and Commonplace membership fixtures are independent |
| Connect and navigation skills | Instructions search explicit source/installed path lists and shell-union results | Use root-aware package operations; label any cross-root union as navigation, not exact membership | E1, tag phase 2 | Source and projected skills call the same root-aware operation |
| Review targets and store identities | Review paths and target keys assume one workspace-root-relative `kb/...` identity | Include root identity in any artifact identity that can span roots; preserve stable source identity through projection | I3 review packet, V1 | Host and Commonplace artifacts with equal relative paths cannot collide |
| Generated control plane | `AGENTS.md.template` routes library paths through `kb/commonplace/` and calls it a namespace with shared top-level types | Explain two explicit roots, root-local types, and root selection; derive paths from the manifest | I3 routing, I2 activation | Generated template matches fresh-install fixture and contains no retired topology claims |
| User collection templates | Seed contracts link examples into `kb/commonplace/` and assume shared types | Link to `commonplace-library/kb/` only when a cross-root reference is intended; use host-root type replicas for host artifacts | I3 routing | Every scaffolded contract validates in the installed tree |
| ProperDocs and publishing | Path construction assumes the source root and current head locations | Build one selected root at a time; externalize omitted library dependencies; make cross-root publication explicit | I2, tag phase 3 | Site and redirect tests cover source and installed paths |
| Package construction | Hatch force-includes canonical source directories; editable fallback can copy a different shape | Run the same install projection for wheel, sdist, and editable source | I2 compiler | Byte-identical product trees for one revision and inputs |
| Existing initialized projects | Preserve-only rerun leaves stale framework copies and has no ownership baseline | Recognize known legacy files, build new root first, preserve forks, and prune old clean paths only deliberately | I1 migration | Legacy clean, modified, deleted, and unknown-path fixtures follow the transition table |
| Optional reader install | `commonplace/kb/` may contain the full repository beside a host project | Reserve that path for reader mode and require explicit selection; do not merge it with the curated library | I2/I3 coexistence | Fixture contains host, installed library, and reader checkout without collision |
| Windows execution | POSIX pipelines encode path enumeration and one-depth traversal | Put deterministic root and collection enumeration behind Python package commands | E1 | Native-Windows CI and runtime probe exercise the same declared roots |

## Known file groups for the implementation refresh

The matrix is role-based; this list prevents obvious current consumers from
being missed when implementation begins:

- `src/commonplace/scaffold_manifest.py`, `src/commonplace/cli/init_project.py`,
  and `pyproject.toml`;
- `src/commonplace/lib/project_paths.py` and
  `src/commonplace/lib/type_resolver.py`;
- validation, collection-conformance, review-path, review-selector, and
  ProperDocs modules;
- `AGENTS.md.template`, install/reference/navigation documents, and user
  collection templates;
- every promoted skill containing a source-versus-installed path branch;
- init, type-resolver, collection-conformance, review, validation, package,
  scenario, and generated-control-plane tests.

The execution packet must refresh lexical and structural searches. This list
is not a frozen file inventory.

## Contract-change gate application

| Gate field | This change |
|---|---|
| Authoritative declaration | Future successor installation ADR plus current architecture/reference updates at activation; workshop draft is non-operative |
| Declared scope | Source checkout, fresh initialized product, upgraded initialized product, and explicitly selected reader checkout |
| Current operative consumer classes | Consumer matrix above |
| Generated or projected forms | Wheel, sdist, editable projection, fresh scaffold, promoted skills, generated control plane, site paths |
| Fresh-install consequence | `kb/` and `commonplace-library/kb/` are disjoint and fully validated |
| Existing-install migration | Ownership-aware migration from legacy `kb/commonplace/`, with explicit prune only |
| Acceptance test | Cross-consumer root fixture, packaged-product validation, and legacy transition fixtures |
| Drift guard | Manifest/package parity, no-overlap invariant, one resolver per path class, and lexical guards against retired topology claims |
| Historical witnesses retained | Dated baseline and superseded ADRs remain marked history; current guidance is updated only at activation |

## Remaining implementation details

These choices do not reopen the architecture:

- Python class and field names for root and manifest records;
- exact installer-state JSON schema and version number;
- CLI rendering and diagnostic wording;
- migration and explicit-prune command names; and
- how tests factor reusable fixtures.

Any implementation discovery that requires nested roots, cross-root type
fallback, or reuse of `commonplace/kb/` for the curated product returns to this
workshop as a design conflict.
