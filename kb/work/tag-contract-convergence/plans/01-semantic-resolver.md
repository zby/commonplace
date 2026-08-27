# Phase 1 — Adopt the semantic foundation and exact resolver

**State:** ready after minimal I3 logical-root semantics.

## Outcome

Adopt one tag meaning per logical KB root, projection-relative participation,
and one exact resolver. Keep current head locations during this phase so the
semantic model and result set can be reviewed without a simultaneous corpus
move.

## Decision packet

The ADR reconciles both tag proposals and states:

- assigning a tag asserts membership in a reusable semantic candidate set;
- every root-owned collection declares `participating` or
  `non-participating`;
- shared `kb/types/` rejects tags because it has no single root owner;
- a minimal canonical head is required from first stable participating use;
- provisional tags may exist only outside participating library content;
- canonical heads are the registry and add no new relation beyond
  `covered_by`;
- structure enforces one declared sense, while assignment fit is checked in the
  write path and semantic review;
- marks authorize skipping only exact membership recovery;
- exact resolver output defaults to deterministic path, title, and description
  records, separate from query-conditioned presentation.

## Resolver work

1. Consume I3's logical-root boundary and collection discovery. Do not infer
   root ownership indefinitely from path depth.
2. Discover participating collections within one root, prune embedded foreign
   KBs and validation-ignored subtrees, and apply the existing artifact
   eligibility rules explicitly.
3. Return one deterministic by-tag set. A cross-root request unions separately
   resolved sets and never transfers marks between roots.
4. Reject absent participation declarations, invalid tag tokens, and tags on
   tag-prohibited shared artifacts.
5. Keep membership independent of presentation. Provide a stable Python result
   and a thin operator command or equivalent package surface.
6. Treat membership-affecting collection changes as invalidation inputs for all
   heads in that root.

## Acceptance

- Source and pristine installed fixtures identify their roots without
  path-depth heuristics.
- Every discovered root-owned collection has one valid participation state.
- Resolver membership is deterministic and independent of head location.
- Embedded host and vendored KBs resolve independently.
- Shared global types cannot enter either tag space.
- Exact output can be rendered as path/title/description without adding
  relevance ranking or summary claims.
