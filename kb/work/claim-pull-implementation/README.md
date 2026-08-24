# Claim-pull implementation

Make the [candidate claim-pull proposal](../source-grounding/candidate-procedure-claim-pull.md)
operative without loading its full source-grounding procedure into every write.
A short check in `cp-skill-write` dispatches a fresh grounding worker only when
the candidate adds or changes an explicit external-source dependency. The
worker grounds the needed primary-source claim in the tracked ingest before the
note is saved.

The default is scoped to Commonplace's untracked-snapshot profile and to fresh
installs with the same retention policy. A KB that retains immutable snapshots
may verify against them directly and use `Claims` only as a sparse cache.

## Status

- [x] Workshop opened and implementation surfaces inventoried.
- [ ] Installed-source-collection prerequisite evidence accepted. Its code has
  landed separately.
- [x] Claims shape and whole-section verification tested with a source-first
  case and a held-out case.
- [x] Re-ingest is the first operative workstream.
- [x] Same-observation preservation, changed-observation authorization, and the
  permanent installed recovery route are specified.
- [x] The mutation protocol is reduced to whole-file backup, mechanical Claims
  reinsertion, live validation, and handled-failure restore. Concurrent edits to
  one ingest are explicitly last-writer-wins.
- [x] Ordinary grounding is append-only and has a defined block for incumbent
  claim repair.
- [ ] Fresh blind readiness judgment completed on the simplified design.
- [ ] Implementation, tests, migration, prospective rollout, and retrospective
  cleanup completed.
- [ ] Durable outputs promoted and workshop removed.

## Router

- [Implementation plan](./plan.md) — dependency order, implementation
  boundary, acceptance conditions, and closure
- [Mutation and dispatch contract](./mutation-and-dispatch-contract.md) — the
  accepted concurrency boundary, Claims preservation, re-ingest modes,
  grounding edit, and writer handoff
- [Draft ADR](./draft-adr-source-claims-are-pulled-through-ingests.md) — intended
  decision record and portability boundary
- [Draft grounding instruction](./draft-ground-source-dependent-claims.md) —
  fresh worker procedure and compact result
- [Implementation surface](./implementation-surface.md) — files to add or
  amend, consumers, acceptance cases, and promotion order
- [Ingest-template migration](./ingest-template-migration.md) — mechanical
  addition of the required section
- [Cleanup plan](./cleanup-plan.md) — claim-level repair of pre-rule debt
- [Installed source collection prerequisite](./fix-installed-sources-collection.md)
  — separate generic scaffold fix
- [Pirolli worked case](./pirolli-claims-worked-case.md) — source-first
  reconstruction and independent whole-section verification
- [Held-out Agent Workflow Memory case](./held-out-agent-workflow-memory-claims-worked-case.md)
  — HTML/table case that fixed extract/location adjacency and caught a source
  contradiction
- [Readiness critique](./readiness-critique-2026-08-24.md) — critic findings on
  the earlier protocol
- [First external review](./review-2026-08-24.md) — scope and missing-state
  findings from the workshops that fed this one; its four concerns are
  dispositioned in the plan and ADR
- [Second external review: proportionality](./review-2026-08-24-proportionality.md)
  — retained-mechanism weight against the operator constraint that
  `cp-skill-write` stay slick. **Start at its Consolidated recommendation**; the
  earlier `Recommendation` section is superseded
- [Critique disposition](./readiness-critique-disposition-2026-08-24.md) — which
  findings are retained, simplified, or accepted as risk
- [Proportionality review](./review-2026-08-24-proportionality.md) — evidence for
  removing the permanent locking subsystem

The earlier [draft installed source contract](./draft-user-sources-COLLECTION.md)
is retained only for disposition. Its generic pieces belong to the prerequisite;
claim-specific rules belong to the ingest type and grounding instruction.

## Inputs

- [Candidate procedure](../source-grounding/candidate-procedure-claim-pull.md)
- [First worked case](../source-grounding/worked-case-agents-navigate.md)
- [Source-grounding workshop](../source-grounding/README.md)

## Ownership and handoffs

This workshop owns the claim-pull decision, Claims representation, grounding
worker, cache-safe ingest/re-ingest behavior, write-time route, acceptance
boundary, migration, and rollout. The prerequisite owns generic installed
source-collection operativity. Literature disposition owns whether a grounded
note is retained or retired; source-adoption policy owns the transfer test; and
collection contracts remain authoritative for link grammar.
