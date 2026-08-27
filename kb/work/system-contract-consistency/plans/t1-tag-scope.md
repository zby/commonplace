# T1 handoff — Track tag-scope contradiction closure

**State:** open finding; design and implementation transferred on 2026-08-27
to [tag-contract convergence](../../tag-contract-convergence/README.md).

**Audited against:** commit `6660bd2a`; see the [parent witness
ledger](../baseline-2026-08-27.md).

## Finding retained here

Current collection-facing routing and the tag-readme contract use unqualified
membership language, while mark validation and generated listings resolve only
the head's collection. The live cross-collection witness remains
[trace-learning-techniques-in-related-systems.md](../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md):
it carries `learning-theory` without a child declared by the notes collection's
`covered_by` head, yet that head validates. The complete `artifact-analysis`
head also omits a live member in reference under the proposed participating
scope.

No local wording patch is sufficient. Closing the contradiction requires one
tag semantic contract, logical-root and participation rules, an exact resolver,
consumer convergence, projection behavior, and a corpus migration.

## Disposition

The owner workshop develops and implements:

- semantic foundation and exact membership resolution;
- convergence of validator, publishing, connect, recipes, and skip rules;
- canonical heads and the breaking source/installed migration;
- separately reviewable provenance and source-family cleanup.

I1 owns the generic installed-upgrade mechanism. I2 owns projection compilation
and link rewriting. I3 supplies installed roles and logical-root boundaries. V1
supplies the whole-product validation suite. The tag workshop provides inputs
and acceptance criteria to those packets rather than creating parallel
machinery.

## Closure check

T1 remains open in this audit until all of the following hold:

- the owner workshop has adopted one semantic and scope contract;
- every exact-membership consumer uses the same projection-relative resolver
  set;
- `complete` and `covered_by` authorize skipping only the exact membership
  operation they replace, never task-level discovery;
- the two retained corpus witnesses satisfy or change the adopted contract;
- source and pristine/upgraded installed fixtures pass the owner workshop's
  resolver, mark, route, link, and full-validation checks;
- this workshop rechecks the original operative surfaces and records no
  remaining contradiction.

The bounded agent navigation experiment remains follow-up evidence. It becomes
a closure gate only if an adopted decision claims a retrieval-performance
improvement.
