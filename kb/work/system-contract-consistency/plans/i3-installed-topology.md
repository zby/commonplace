# I3 plan — Give the installed control plane one real topology

**State:** open; partially clarified in `kb/types/COLLECTION.md`, but the
generated template and installed files still disagree.

## Resolution selected

Keep `kb/sources/` and `kb/work/` as writable user collections and scaffold
minimal contracts and landings for both. Classify `kb/types/` as the global type
collection: global describes its semantic reach, while collection describes its
authoring and routing boundary. `kb/commonplace/` remains only a namespace whose
children are collections.

## Work

1. Define one package-owned, machine-readable topology declaration for
   collection roles, writable roots, library roots, the global type collection,
   and non-collection namespaces/support directories. Make scaffold execution
   consume it directly; generate routing where practical and otherwise enforce
   set parity against the generated control plane, package inclusion, fixtures,
   and docs. I1's successor ADR records this decision but is not executable
   configuration.
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
4. After S1 lands, or in the same change, add generic user templates for:
   - `kb/sources/COLLECTION.md` and `README.md`, offering the shipped snapshot,
     ingest-report, source-review, and implicit text types and using the S1
     mutation boundary;
   - `kb/work/COLLECTION.md` and `README.md`, defining temporary workshop
     semantics without importing Commonplace's project-specific scope.
   The templates must be usable as installed defaults, not copies containing
   source-repository-only destinations.
5. Add these four files to the topology-driven scaffold and wheel/sdist
   coverage.
   Preserve the ordinary no-overwrite rule for user-owned contracts on rerun.
6. Change `AGENTS.md.template` from “global type surface, not a collection” to
   “global type collection,” and make every routed write destination point to a
   contract that init actually creates. Populate the read-only library portion
   only after I2 fixes the shipped set.
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

I3 can establish the topology model and discovery semantics first, but cannot
close until S1 supplies the sources mutation contract, I2 supplies the shipped
library set, and I1 records the resulting decision. It closes when generated
routing, material scaffold, discovery, and executable prerequisites describe
the same topology.
