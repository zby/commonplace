# Implementer handoff

Authority: [implementation-plan.md](./implementation-plan.md), [database-design.md](./database-design.md).

## Easy to miss

- **No compatibility shim.** Delete review-specific freshness tables/helpers in the same change that lands the general schema. A temporary adapter inside one in-progress commit is the only allowance.
- **Malformed ≠ stale.** Integrity failures are store errors. Selectors must never downgrade bad baselines to `missing-baseline` or ordinary staleness.
- **Review precedence survives migration.** When both note and criterion changed, public selector output still reports `criterion-changed` before `note-changed`.
- **Finalization may accept job snapshots that are already stale.** That is correct: live text moved on during the run; the new baseline should go stale immediately on the next check — not block finalization or silently substitute current files.
- **`collection-text` hash stability is the contract.** Fix the member delimiter and collection rule in M1 and test it. No per-target include/exclude; changing the rule later invalidates every registered baseline.
- **Stale ingests are derivative maintenance, not validator work.** `.ingest.md` lives in the source collection; casebook edits change `casebook`, ingest edits change `source-scope`. Reassessment revises derivatives — do not parse ingest prose.
- **Global status is not discovery.** `commonplace-freshness-status` reports registered targets only. Review selector still owns `missing-baseline`.
- **WAL sources.** Migration opens the old DB read-only. If `journal_mode=wal`, operator must checkpoint first; migration refuses a changed source hash.

## Gates (do not skip)

1. **M1:** migration fixtures + both live-store copies; old `review-store.sqlite` byte hash unchanged.
2. **M2:** full review test suite at CLI boundary; selector JSON parity pre/post migration. **No Epistack targets before this passes.**
3. **M3:** register casebook targets only after M2.

## Highest bug risk

Shared snapshot pruning across `freshness_inputs` and `review_pairs`. Test: ack one input only, finalization supersede, migration preserving snapshot IDs.

## Rollback

Bad new store → point `COMMONPLACE_STORE` at untouched `review-store.sqlite`. Never auto-delete the backup.

## Out of scope for this build

Semantic truth checks, link-derived registration, resolver plugins, full-pass in SQLite, baseline history, auto-registration of all artifacts.