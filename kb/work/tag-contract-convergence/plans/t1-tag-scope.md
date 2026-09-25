# T1 handoff — Track tag-scope contradiction closure

**State:** open finding; design and implementation transferred on 2026-08-27
to [tag-contract convergence](../README.md).

**Audited against:** commit `6660bd2a`; rebaselined 2026-09-25 after
[ADR 086](../../../reference/adr/086-projects-read-the-library-from-the-installed-package.md)
removed the installed library copy.

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
tag semantic contract, participation rules, an exact resolver, consumer
convergence, and a corpus migration. The owner workshop reports that both
corpus witnesses have since been repaired, so it tests the contract against a
synthetic cross-collection witness instead.

## Disposition

The owner workshop develops and implements:

- semantic foundation and exact membership resolution;
- convergence of validator, publishing, connect, recipes, and skip rules;
- canonical heads, with host-project heads migrated through `commonplace-init`;
- separately reviewable provenance and source-family cleanup.

Since ADR 086 there is one KB per checkout. The installed library is read in
place and keeps the marks validated in source, so T1 no longer depends on
installed-product work.

## Closure check

T1 remains open in this audit until all of the following hold:

- the owner workshop has adopted one semantic and scope contract;
- every exact-membership consumer uses the same resolver set;
- `complete` and `covered_by` authorize skipping only the exact membership
  operation they replace, never task-level discovery;
- the owner workshop's synthetic cross-collection witness fails before the
  change and passes after it;
- the source checkout and a freshly initialized project pass the owner
  workshop's resolver, mark, route, and link checks;
- this workshop rechecks the original operative surfaces and records no
  remaining contradiction.

The bounded agent navigation experiment remains follow-up evidence. It becomes
a closure gate only if an adopted decision claims a retrieval-performance
improvement.
