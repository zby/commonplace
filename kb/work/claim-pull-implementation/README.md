# Claim-pull implementation

Implement one rule: a writer may use a named external-source claim only after
that claim exists in the source's tracked ingest.

V1 has three parts:

1. an explicit grounding instruction constructs a source-side entry;
2. `cp-skill-ingest` alone appends it and preserves Claims during re-ingest; and
3. `cp-skill-write` reuses an existing normalized claim or stops with the
   grounding route. A source-as-gate review pair checks the resulting dependency.

Grounding only adds entries. It never changes existing ones.

## Status

- [x] Claims shape tested source-first and against a held-out source.
- [x] Retained protocol simplified and rejected machinery removed.
- [ ] Installed-source prerequisite evidence accepted.
- [x] Fresh design-readiness judgment passed.
- [ ] Implementation, tests, migration, and first cleanup cohort completed.

## Files

- [Plan](./plan.md) — interfaces, order, and acceptance
- [Draft ADR](./draft-adr-source-claims-are-pulled-through-ingests.md) — decision
- [Grounding instruction](./draft-ground-source-dependent-claims.md) — operative
  append-only procedure
- [Implementation surface](./implementation-surface.md) — files to change
- [Migration](./ingest-template-migration.md) — structural corpus edit
- [Cleanup](./cleanup-plan.md) — first retrospective pass
- [Evidence](./claims-shape-evidence.md) — conclusions retained from the worked
  cases
- [Prerequisite](./installed-source-prerequisite.md) — already-landed scaffold
  fix awaiting accepted evidence
