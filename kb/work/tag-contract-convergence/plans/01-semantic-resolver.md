# Phase 1 — Build the dormant semantic foundation and exact resolver

**State:** ready. The 2026-09-25 rebaseline removed the gate on minimal I3.

## Outcome

Implement and test one candidate tag meaning per KB, declared participation,
one exact membership resolver, and transitional head lookup. Keep the machinery
dormant: live collection declarations, binding wording, consumer switches,
mandatory-head enforcement, and the accepted ADR all activate together in
Phase 3.

## Decision packet

Maintain the ADR as a workshop draft during this phase. It reconciles both tag
proposals and states:

- assigning a tag asserts membership in a reusable semantic candidate set;
- one tag string has one canonical sense within one KB; the host project and
  the installed library are separate KBs;
- every discovered collection declares `participating` or `non-participating`;
- type specs carry no tags, enforced by the `type-spec` schema;
- a minimal canonical head is required from first stable participating use;
- provisional tags may exist only outside participating content;
- canonical heads are the registry and add no new relation beyond
  `covered_by`;
- structure enforces one declared sense, while assignment fit is checked in the
  write path and semantic review;
- marks authorize skipping only exact membership recovery;
- exact resolver output defaults to deterministic path, title, and description
  records, separate from query-conditioned presentation;
- whether a headless host tag may route to the library head with the same
  string (default: no; it renders as plain text).

Use the fixed declaration, resolver, command, transitional-head, and fixture
contracts from the [readiness pass](./00-readiness.md). Do not reopen those
choices inside implementation; return a conflict to this workshop.

## Resolver work

1. Take a KB directory as input: the project's `kb/` by default, or
   `library.library_root()` for the installed library. Use the existing
   `project_paths` collection discovery.
2. Parse fixture-local `## Tag participation` clauses, prune validation-ignored
   subtrees and excluded subtrees, and apply the existing artifact eligibility
   rules explicitly. Do not add the clauses to live contracts yet.
3. Return one deterministic by-tag set.
4. Reject absent or malformed participation declarations and invalid tag
   tokens.
5. Keep membership independent of presentation. Implement and test the stable
   Python result and the JSON-lines renderer for
   `commonplace-tag-members TAG [--library]`, but do not register or document
   the command until Phase 3 activation.
6. Treat membership-affecting collection changes as invalidation inputs for all
   heads in the KB.
7. Resolve current-location heads through the `tag-readme` type plus
   `index_source: tag` and `index_key`, rejecting duplicate identities. Do not
   enforce live head completeness or change canonical paths in this phase.

## Acceptance

- Every collection in the Phase 1 fixtures has one valid participation state;
  live contracts remain unchanged until activation.
- Resolver membership is deterministic, spans every participating collection,
  and is independent of head location.
- The project KB and a fixture library root resolve independently.
- Exact output can be rendered as path/title/description without adding
  relevance ranking or summary claims.
- No live collection contract, binding authoring surface, mark consumer, build
  hook, skill, or recipe has switched semantics, and no accepted ADR claims
  otherwise.
