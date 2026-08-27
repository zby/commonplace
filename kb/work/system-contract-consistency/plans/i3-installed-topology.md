# I3 plan — Give the installed control plane one real topology

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. Installed
sources now has a contract and landing, and the old generated-template claim
that types is not a collection is gone. Installed work remains contractless;
collection discovery and conformance still exclude `kb/types/`. See the
[witness ledger](../baseline-2026-08-27.md).

## Resolution selected

Keep host `kb/sources/` and `kb/work/` as writable user collections. Retain the
sources templates that now ship and add generic work templates. Each selected
`kb-root` owns its `types/` collection. In the source checkout this is
`kb/types/`; in the projected Commonplace library it is
`commonplace-library/kb/types/`; host operations receive only explicitly
declared type replicas in host `kb/types/`.

Extend the existing `ScaffoldManifest` rather than adding a second topology
inventory. Its entries describe seeded product topology and ownership;
runtime discovery continues to recognize concrete `COLLECTION.md` files inside
an already selected root so a user-created collection needs no package
configuration. Root discovery is explicit. It never discovers an embedded root
and subtracts it from an ancestor.

The [installed-product decision](../installed-product-edition-decision.md)
selects source `commonplace-kb` at `kb/` and, in an initialized project,
pairwise-disjoint `host-kb` at `kb/` and `commonplace-kb` at
`commonplace-library/kb/`. It also supplies per-file ownership values for
directories that mix Commonplace replicas with user content.
The successor installation ADR must adopt those choices before this plan makes
them operative.

## Work

1. Refactor `ScaffoldManifest` entries to carry orthogonal product metadata:
   source and target identity, owning `kb-root` or outside-KB placement,
   collection/template responsibility, ownership, writability,
   materialization/projection, and upgrade policy. Do not collapse these axes
   into one `kind` enum. Scaffold execution consumes these entries
   directly. Generate routing where practical and otherwise enforce set parity
   against the generated control plane, package inclusion, fixtures, and docs.
   I1's successor ADR records the decision but is not executable configuration.
2. Add an explicit `kb-root` path API. Reject overlapping declared roots before
   traversal. Source checkout uses `kb/`; installed operation reads host and
   Commonplace roots from installer state; reader targets require explicit
   selection. Separate two collection APIs if necessary:
   - discovery of every visible contract-bearing collection, including
     `kb/types/`;
   - discovery of knowledge artifacts for consumers that intentionally exclude
     type specs.
   A consumer must not redefine collection merely by filtering out `types`.
3. Make `kb/...` type and schema pointers root-relative and carry root identity
   in canonical artifact identities. Remove topology-specific cross-root
   fallbacks. Apply the collection distinction to
   `src/commonplace/review/collection_conformance.py` and its tests. ADR 060's
   collection-conformance review must include each selected root's type
   collection even when artifact-oriented consumers deliberately exclude type
   specs.
4. Retain and parity-check the existing generic host sources contract and
   landing, which already project S1's mutation boundary. Add generic
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
- Host and projected Commonplace type pointers resolve within their own roots;
  equal root-relative strings cannot collide.
- Snapshot, ingest, connect, and workshop-write smoke cases can read their
  target contract in a pristine install.
- Manifest destinations, AGENTS routing rows, declared `kb-root`s, and
  discovered collection roots are asserted as sets, not by a fixed count.
  Landing validation applies its declared rule inside each selected root; it
  does not infer scope from project-relative depth.

Land the minimal manifest roles, disjoint root boundary, and discovery
semantics before V1. Finish routing, work templates, and projection parity
after I2 chooses the
installed edition. S1's source boundary is already supplied. I3 closes when
generated routing, material scaffold, discovery, and executable prerequisites
describe the same topology and ownership model.
