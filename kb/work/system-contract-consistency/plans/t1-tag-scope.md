# T1 plan — Align tag membership claims at the KB-root boundary

**State:** open; refreshed 2026-08-27 against the converged but unadopted
[tag-scope proposal](../../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md),
the newer [semantic contract](../../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md),
and the grounded navigation literature they now cite. The current validator,
generated listing, routing, recipes, and mark wording still select incompatible
membership sets. No adoption implementation has landed.

## Resolution selected

Adopt one tag namespace per KB root. A tag string has one sense throughout its
KB. Assigning it to an artifact asserts membership in a reusable semantic
candidate set. Every
exhaustive membership claim ranges over the root's explicitly participating
library collections in the concrete projection being read. A `complete` or
`covered_by` mark licenses skipping only exact resolution of that membership
set. It grants no skip right across another KB root and no right to stop
task-level search.

Every root-owned collection declares `participating` or `non-participating` in
its `COLLECTION.md`. Shared `kb/types/` declares tags prohibited because it has
no single KB owner. Missing participation state fails validation. A pure,
root-aware resolver supplies the same membership set to validation, published
tag-page augmentation, `cp-skill-connect`, operator recipes, and every skip
rule. A cross-KB membership query explicitly unions independently resolved sets
without combining their marks.

Keep three navigation operations distinct. The resolver answers which eligible
artifacts carry a tag. A canonical head supplies stable definition and
contextual local routing. Task-level search may recover artifacts outside that
tag or rank members for the current query. [Link-following and
search](../../../notes/link-following-and-search-impose-different-metadata-requirements.md)
and [pointer design](../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md)
ground this distinction in bounded human evidence and local agent-facing
inference; they do not establish an LLM performance result.

Per-tag heads move to canonical `kb/tags/<tag>-README.md` paths in the adopting
change. The filename supplies tag identity; `index_source: tag`, `index_key`,
the legacy `tags-README.md` hub, and `index_source: tag-indexes` retire.
`trace-learning` remains the single authored source for both website navigation
and the derived matrix Boolean, gains a canonical head, and stays in parity with
the review type's `### Trace-learning` subsection. Redundant source-family tags
are removed.

This replaces the earlier collection-scoped recommendation. Formal collection
scope is now a rejected alternative because it would give one schema field
different namespaces by collection and leave cross-collection library members
outside every complete head.

## Inputs to settle

T1 consumes decisions from the installed-product repairs rather than inventing
a competing topology:

- I3 supplies collection discovery, KB-root ownership, and the status of shared
  `kb/types/`.
- I2 supplies the installed library bundle and the policy for links to omitted
  dependencies.
- I1 supplies preserve-only upgrade semantics; T1 adds the exact scaffold
  migration procedure and fixture for this breaking change.
- V1 supplies the truthful full-validation path used by final source and
  initialized-project checks.

Before implementation, the adopting ADR must reconcile both proposals and
settle their remaining free choices: when heads become mandatory, where
provisional tags may live, how semantic reuse is checked, whether more tag
relations are needed, how resolver results are presented, declaration syntax,
the six projection-sensitive head links, footer behavior for
non-participating layers, treatment of remaining source topic tags, and whether
the known-tags registry rider lands now or separately.

## Work

1. **Record the combined decision.** Add an ADR that defines the KB-root
   namespace, semantic membership predicate, tag-token grammar, explicit
   participation states, projection-relative membership, membership-only mark
   skip right, canonical head identity and routing prefix, the retained
   `trace-learning` facet, redundant source-family tag removal, and its
   relationship to ADRs 025 and 026. Name exact membership recovery, contextual
   head traversal, and task-level search as distinct operations. Keep both
   proposals live until the implementation passes.
2. **Build one membership resolver.** Discover participating collections for
   one KB root, prune embedded foreign KBs, apply declared exclusions and
   artifact-visibility rules, and expose a by-tag operator command. Make absent
   declarations and tags on shared tag-prohibited artifacts validation errors.
   Keep the exact result independent of its path-only, fixed-description, or
   query-conditioned presentation; settle the CLI default in the ADR.
   Treat every membership-affecting declaration as an all-head invalidation
   input; require whole-tag-collection validation for collection creation,
   deletion, or relocation.
3. **Make every consumer use the resolver.** Replace independent membership
   logic in mark validation and impact expansion, ProperDocs generated
   augmentation, `cp-skill-connect`, `AGENTS.md` and `navigation.md` recipes,
   and every mark-based exact-membership skip rule. State at each consumer that
   no mark licenses stopping broader task discovery. ProperDocs resolves a tag
   directly to the declaring root's canonical head and renders plain text when
   none exists.
4. **Install the authoring contracts.** Add participation state to every
   discovered source and scaffold collection; enforce one-string-one-sense and
   the tag-token grammar in root instructions and schemas; prohibit tags in
   shared `kb/types/`; and add the `kb/tags/` collection contract with its
   introduction quality goal, common meaning/use/boundary/route/stopping prefix,
   and cross-library link grammar. Say explicitly that fixed head cues are not
   query-relative relevance judgments.
5. **Preserve navigational classification and remove redundant provenance.**
   Keep `trace-learning` in `tags:` and keep `systems_matrix.py` deriving its
   Boolean from that tag. Make the review schema, type, template, writing skill,
   and tests require the tag exactly when the `### Trace-learning` subsection
   applies, correcting the conditional's stale `trace-derived` tag spelling.
   Add a canonical head whose first curated route is the existing comparative
   survey.
   Remove all current `x-*` source-family values and stop the X and GitHub
   producers from emitting redundant classification tags. Derive removal
   inventories at execution time rather than freezing today's counts.
6. **Make source and installed projections coherent.** Scaffold an empty host
   `kb/tags/` collection, ship Commonplace's projection-eligible heads under
   `kb/commonplace/tags/`, isolate host and vendored membership, and disposition
   every projection-sensitive head link. Keep the new `trace-learning` head
   source-only while the installed bundle omits `kb/agent-memory-systems/`, so
   the installed tag collection gains neither a dangling survey link nor a head
   with no subject. Add a fresh initialized-project fixture whose marks,
   canonical routes, head selection, and local links all validate.
7. **Document and test the breaking upgrade.** Add
   `kb/instructions/upgrade-from-previous-scaffold.md`, link it from install and
   command documentation, and distinguish package-owned replacement,
   user-owned merge, promoted-skill refresh, and obsolete-path pruning. Exercise
   that procedure on a checked-in pre-adoption fixture and compare its
   framework-owned result with a fresh scaffold while preserving sentinel user
   content.
8. **Relocate the heads last inside the same adopting change.** Move the 20
   existing per-tag heads to direct children of `kb/tags/`, create the new
   `trace-learning` head there, rewrite relative links and published redirects,
   remove redundant identity fields, move useful hub prose to the collection
   landing, retire the old hub and tag-specific generated-index branches,
   update path-constructing consumers, and include `kb/tags/` in review-sweep
   scope. Land canonical resolution and all 21 source heads together with no
   legacy fallback; let the installed projection apply its eligibility rule.
9. **Close the lifecycle.** After code, contracts, migrations, fixtures, and
   tests pass, annotate ADR 026 forward, archive the adopted proposal through
   the normal proposal lifecycle, and update this workshop's T1 outcome.

## Evidence boundary and follow-up

The recent [Pirolli](../../../sources/pirolli-proximal-information-scent-distal-content.ingest.md),
[Teevan](../../../sources/teevan-perfect-search-engine-orienteering.ingest.md),
and [Tombros–Sanderson](../../../sources/tombros-sanderson-query-biased-summaries.ingest.md)
sources concern human information seeking. They support the structural
distinction among proximal cues, contextual local navigation, and
query-conditioned results. They do not show which interface helps an LLM
agent, so T1 must not claim a retrieval performance improvement as part of
structural adoption.

After the resolver and canonical heads exist, a bounded agent trial can compare
an exact membership listing, a curated head, and query-conditioned result
pointers. Measure membership recovery and task-relevant discovery separately,
then record wrong opens, full-artifact reads, tool calls or context cost, task
outcome, and false stopping. This trial is follow-up evidence, not a T1 closure
gate unless the adopting ADR makes a performance claim.

## Verification

- Resolver, validator, ProperDocs, connect, recipes, and skip rules return or
  consume the same projection-relative membership set.
- Every `complete` and `covered_by` shortcut is stated and tested as an exact
  membership shortcut; no mark suppresses task-level search or claims that a
  tag exhausts the current information need.
- Exact resolver output remains separable from fixed or query-conditioned
  presentation, so a later navigation trial cannot change tag semantics.
- Every discovered collection in both the source checkout and initialized
  fixture has an explicit valid participation state; shared `kb/types/` rejects
  tags, and an embedded KB never enters its host's membership.
- The two violations inside the proposed participating set are dispositioned:
  the external `learning-theory` member satisfies or changes `covered_by`, and
  the `artifact-analysis` head covers or excludes the live proposal member.
- Host and vendored heads validate independently, every eligible artifact's
  footer reaches its own root's head when one exists, and every shipped head's
  local links resolve in that projection.
- Every qualifying review retains `trace-learning` as a tag, every such footer
  reaches the canonical head and complete generated listing, the tag and
  `### Trace-learning` subsection remain in parity, and the matrix Boolean is
  still derived from that tag. No snapshot producer emits `x-*`, `github-issue`,
  or `github-pr` tags.
- All 21 per-tag heads are canonical direct children of `kb/tags/`; no live
  `tags-README.md`, `index_source: tag`, `index_source: tag-indexes`, or
  `index_key` head identity remains.
- The fresh-scaffold and upgraded-scaffold fixtures agree on framework-owned
  paths, preserve declared user additions, and pass mark, route, link-closure,
  and full-validation checks.
- Focused resolver, tag-readme, validation-impact, ProperDocs, snapshot,
  scaffold, upgrade, and matrix tests pass, followed by the full test suite,
  lint, relevant `commonplace-validate` runs, and a site build.

T1 closes when the ADR and its full adoption criteria are implemented, both
proposals are archived, every stated skip right equals the resolver's exact
membership set, no mark implies task-level discovery completeness, and no route
presents a tag page that omits an eligible source artifact.
