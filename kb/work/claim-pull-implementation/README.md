# Claim-pull implementation

Make the [candidate claim-pull proposal](../source-grounding/candidate-procedure-claim-pull.md)
operative without putting its full procedure into every write context. A small
check in `cp-skill-write` dispatches a fresh grounding worker only when the
candidate adds or changes an explicit external-source dependency. The worker
grounds the needed claim in the tracked ingest before the note is saved.

The design is scoped to this public repository's untracked-source-snapshot
constraint. The ADR also preserves the direct-verification option for KBs that
can retain snapshots and the independent cache/index value of `Claims` for large
sources.

Operator direction on 2026-08-24 fixed this as an implementation workshop. The
retrospective cleanup is one rollout workstream, not the workshop's whole scope.

## Status

- [x] Workshop opened and implementation surfaces inventoried.
- [ ] Installed-source-collection bug fixed and its fresh-install evidence
  accepted as a prerequisite.
- [ ] Deployment scope, whole-section grounding, and fidelity choice accepted
  in the draft ADR.
- [ ] Required `## Claims` section and empty-state syntax fixed.
- [ ] Same-checksum re-ingestion preserves `Claims`; changed-checksum
  invalidation fails closed.
- [ ] Delegated grounding-worker instruction made executable and tested.
- [ ] Cheap pre-save router added to `cp-skill-write`.
- [ ] Existing ingest and authoring contracts amended.
- [ ] Structural ingest-template migration completed and validated.
- [ ] Acceptance cases passed.
- [ ] Prospective path deployed before retrospective cleanup begins.
- [ ] First cleanup cohort completed or left with named blockers.
- [ ] Cleanup-only legacy recovery removed from active routing and retired to
  an authorized non-operative archive.
- [ ] Library outputs promoted, validated, and workshop removed.

## Router

- [Installed source collection bug fix](./fix-installed-sources-collection.md) —
  separate implementation handoff that must land before claim-pull changes
- [Implementation plan](./plan.md) — dependency order, design gates,
  acceptance boundary, and closure conditions
- [Draft ADR](./draft-adr-source-claims-are-pulled-through-ingests.md) — intended
  new decision record for the claim-pull invariant, representation, guarantee,
  operativity path, and migration policy
- [Draft grounding-worker instruction](./draft-ground-source-dependent-claims.md)
  — intended new instruction loaded only in a fresh worker after the write
  skill detects an explicit source dependency
- [Draft installed source contract](./draft-user-sources-COLLECTION.md) — earlier
  combined draft retained for disposition; do not install its claim-specific
  clauses as part of the prerequisite bug fix
- [Implementation surface](./implementation-surface.md) — intended new files,
  existing files to amend, consumers, tests, and promotion targets
- [Ingest-template migration](./ingest-template-migration.md) — mechanical
  addition of the required section to the existing ingest corpus
- [Cleanup plan](./cleanup-plan.md) — claim-level repair of debt that predates
  the prospective rule

## Inputs

- [Candidate procedure](../source-grounding/candidate-procedure-claim-pull.md) —
  proposal being implemented
- [First worked case](../source-grounding/worked-case-agents-navigate.md) —
  exposed missing source routes, claim-specific transfer, and contradiction
- [Source-grounding workshop](../source-grounding/README.md) — broader source
  corpus and intermediate-node investigation

## Ownership and handoffs

- This workshop owns the claim-pull decision, tracked claim record, grounding
  worker, re-ingestion preservation, cheap write-skill router, fidelity
  guarantee, acceptance cases, and rollout.
- The prerequisite bug fix owns generic installed-source-collection operativity.
  Claim pulling consumes its result but does not own that fix.
- [Literature disposition](../literature-disposition/README.md) owns whether a
  grounded note is retained, thinned, rewritten around its delta, or retired.
- [Source adoption policy](../../reference/source-adoption-policy.md) owns the
  transfer test; this workshop invokes it rather than creating another test.
- [Linking foundations](../linking-foundations/README.md) owns any new link
  semantics that the implementation cannot express with the current grammar.
- [KB graph loader](../kb-graph-loader/README.md) owns a general referential-check
  architecture. This workshop adds only the smallest source-specific check the
  adopted guarantee requires.
