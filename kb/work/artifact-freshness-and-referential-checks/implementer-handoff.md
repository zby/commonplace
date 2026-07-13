# Implementer handoff

**Start here.** Authority chain: this file → [implementation-plan.md](./implementation-plan.md) → [database-design.md](./database-design.md) → [freshness-schemas.md](../../reference/freshness-schemas.md).

**Verdict:** go. Build v1 review-first; end at M4 proposals. Do not implement `collection-text` or register non-review targets in this phase.

## Milestones

| gate | deliverable |
|---|---|
| **M1** | `file-text` schema, [freshness-schemas.md](../../reference/freshness-schemas.md), migration script + fixtures (skip 4 dead baselines; fail job `49`) |
| **M2** | full review suite parity at CLI boundary; selector JSON before/after migration |
| **M3** | `commonplace-freshness-{status,accept,ack,retire}` over `review-pair` targets only |
| **M4** | `kb/reference/proposals/collection-as-artifact-freshness.md` from [future-work sketch](./future-work-collection-freshness.md) — **terminal step** |

## v1 scope

- **Store:** new `commonplace-store.sqlite`; old `review-store.sqlite` read-only backup forever.
- **Versioning:** `file-text` only.
- **Targets:** `review-pair` only (migrated + newly finalized).
- **Review adapters stay:** `missing-baseline` discovery, reason mapping (`criterion-changed` before `note-changed`), trivial ack, capture finalization.

## Resolved contracts (do not re-litigate)

1. **Queued-job CAS** — `review_pairs.expected_baseline_revision` at pair create; `finalize_capture_refresh()` CASes against it. Job `49` → `failed` / `stale-queued-capture` at migration when captures ≠ accepted.
2. **Two refresh paths** — capture (review-owned, job snapshots, no live check) vs observation (accept/ack, live revalidation). Generic accept **rejects** `review-pair`.
3. **Dead targets** — skip four `transformation-closure` baselines at migration; `commonplace-freshness-retire` at runtime. `input-missing` → exit `1`.
4. **Done-when** — no duplicated compare/persist in review code; adapters remain.

## Highest-risk areas

- Snapshot pruning across `freshness_inputs` + `review_pairs`.
- Migration row-count parity (48 Commonplace baselines, not 52).
- Capture refresh succeeding while live files diverged — immediate staleness is correct.

## Traps

- No post-migration compatibility shim.
- Malformed baselines → store error, never `missing-baseline`.
- Global status ≠ discovery (`missing-baseline` stays on review selector).
- WAL source DB → checkpoint before read-only migration.
- Stale `.ingest.md` prose is derivative maintenance, not missing validator code.

## Deferred → M4

[collection-text](./future-work-collection-freshness.md) and `collection-maintenance` targets. Per-file `file-text` + semantic workflows suffice until proposal adoption.