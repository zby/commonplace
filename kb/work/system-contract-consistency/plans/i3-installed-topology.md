# I3 plan — Give the installed control plane one real topology

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. Installed
sources now has a contract and landing, and the old generated-template claim
that types is not a collection is gone. Installed work remains contractless;
collection discovery and conformance still exclude `kb/types/`. See the
[witness ledger](../baseline-2026-08-27.md).

## Resolution selected

Keep `kb/sources/` and `kb/work/` as writable user collections. Retain the
sources templates that now ship and add generic work templates. Classify
`kb/types/` as the global type collection: global describes its semantic reach,
while collection describes its authoring and routing boundary.

Extend the existing `ScaffoldManifest` rather than adding a second topology
inventory. Its entries describe seeded product topology and ownership;
runtime discovery continues to recognize concrete `COLLECTION.md` files so a
user-created collection needs no package configuration. `kb/commonplace/`
remains a namespace, and the manifest supplies an unambiguous logical-root
boundary for projections nested beneath it.

The [installed-product decision](../installed-product-edition-decision.md)
selects three logical roots: the read-only `commonplace-library`, the writable
`host-kb`, and the `shared-types` support root. It also supplies per-file
ownership classes for directories that mix framework seeds with user content.
The successor installation ADR must adopt those choices before this plan makes
them operative.

## Work

1. Refactor `ScaffoldManifest` entries to carry the required product metadata,
   such as path, kind (`collection`, `namespace`, or `support`), owner,
   writability, source/projection, contract and landing templates, upgrade
   policy, and logical-root identity. Scaffold execution consumes these entries
   directly. Generate routing where practical and otherwise enforce set parity
   against the generated control plane, package inclusion, fixtures, and docs.
   I1's successor ADR records the decision but is not executable configuration.
2. Separate two path APIs if necessary:
   - discovery of every visible contract-bearing collection, including
     `kb/types/`;
   - discovery of knowledge artifacts for consumers that intentionally exclude
     type specs.
   A consumer must not redefine collection merely by filtering out `types`.
3. Apply the same distinction to
   `src/commonplace/review/collection_conformance.py` and its tests. ADR 060's
   collection-conformance review must include the global `kb/types/` collection
   even when artifact-oriented consumers deliberately exclude type specs.
4. Retain and parity-check the existing generic sources contract and landing,
   which already project S1's mutation boundary. Add generic
   `kb/work/COLLECTION.md` and `README.md` templates defining temporary workshop
   semantics without importing this repository's project-specific scope.
5. Add the work files and explicit ownership/upgrade policies to manifest and
   wheel/sdist coverage. Preserve user-owned contracts under I1's rules.
6. Keep the corrected generated definition of collection, make every routed
   write destination point to a contract that init creates, and generate or
   validate the library/root routing only after I2 fixes the installed edition.
7. Update `cp-skill-snapshot-web`, `cp-skill-ingest`, `ingest-directory`, write
   and connect setup, architecture, and collection definitions to use the same
   installed paths and contract rule.

## Verification

- A fresh init has a local `COLLECTION.md` and `README.md` for every writable
  destination routed by the generated control plane.
- `kb/types/COLLECTION.md` is discovered and validated as a collection while
  type-neutral note searches do not accidentally treat schemas as notes.
- Snapshot, ingest, connect, and workshop-write smoke cases can read their
  target contract in a pristine install.
- Manifest destinations, AGENTS routing rows, and discovered collection roots
  are asserted as sets, not by a fixed count. Existing landing validation still
  covers direct children of `kb/`; sources and work therefore gain landings,
  while nested library children do not silently acquire a new landing rule.

Land the minimal manifest roles, root boundary, and discovery semantics before
V1. Finish routing, work templates, and projection parity after I2 chooses the
installed edition. S1's source boundary is already supplied. I3 closes when
generated routing, material scaffold, discovery, and executable prerequisites
describe the same topology and ownership model.
