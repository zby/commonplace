# Phase 1 — Build the dormant semantic foundation and exact resolver

**State:** ready after minimal I3 `kb-root` semantics.

## Outcome

Implement and test one candidate tag meaning per `kb-root`,
projection-relative participation, one exact membership resolver, and
root-aware transitional head lookup. Keep the machinery dormant: live
collection declarations, binding wording, consumer switches, mandatory-head
enforcement, and the accepted ADR all activate together in Phase 2.

## Decision packet

Maintain the ADR as a workshop draft during this phase. It reconciles both tag
proposals and states:

- assigning a tag asserts membership in a reusable semantic candidate set;
- every collection inside the selected root declares one allowed participation
  state;
- each root's `types/` collection rejects tags because type artifacts are
  structural support, not because they lack a root owner;
- a minimal canonical head is required from first stable participating use;
- provisional tags may exist only outside participating library content;
- canonical heads are the registry and add no new relation beyond
  `covered_by`;
- structure enforces one declared sense, while assignment fit is checked in the
  write path and semantic review;
- marks authorize skipping only exact membership recovery;
- exact resolver output defaults to deterministic path, title, and description
  records, separate from query-conditioned presentation.

Use the fixed declaration, resolver, command, transitional-head, projection,
and fixture contracts from the [readiness pass](./00-readiness.md). Do not reopen
those choices inside implementation unless I3 makes one impossible; return any
such conflict to this workshop before inventing a second root or topology model.

## Resolver work

1. Consume I3's explicit, pairwise-disjoint `kb-root` boundary and collection
   discovery. Do not infer root ownership from path depth.
2. Parse fixture-local `## Tag participation` clauses, discover participating
   collections within one root, prune validation-ignored subtrees, reject
   paths outside the selected root, and apply the existing artifact eligibility
   rules explicitly. Do not add the clauses to live contracts yet.
3. Return one deterministic by-tag set. A cross-root caller may union
   separately resolved sets for navigation and never transfers marks between
   roots.
4. Reject absent participation declarations, invalid tag tokens, and tags on
   prohibited root-local type artifacts.
5. Keep membership independent of presentation. Implement and test the stable
   Python result and the JSON-lines renderer for
   `commonplace-tag-members TAG --root KB_ROOT_PATH`, but do not register
   or document the command until Phase 2 activation.
6. Treat membership-affecting collection changes as invalidation inputs for all
   heads in that root.
7. Resolve current-location heads through `tag-readme` type plus
   `index_source: tag` and `index_key`, rejecting duplicate identities. Do not
   enforce live head completeness or change canonical paths in this phase.

## Acceptance

- Source and pristine installed fixtures identify their roots without
  path-depth heuristics.
- Every collection discovered inside a selected root in the Phase 1 fixtures
  has one valid participation state; live contracts remain unchanged until
  activation.
- Resolver membership is deterministic and independent of head location.
- Sibling host and projected Commonplace KBs resolve independently; an
  explicitly selected reader KB remains a third independent target.
- Root-local type collections cannot enter their root's tag space.
- Exact output can be rendered as path/title/description without adding
  relevance ranking or summary claims.
- No live collection contract, binding authoring surface, mark consumer, build
  hook, skill, or recipe has switched semantics, and no accepted ADR claims
  otherwise.
