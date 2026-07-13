# Implementer handoff

Authority: [implementation-plan.md](./implementation-plan.md), [database-design.md](./database-design.md), [freshness-schemas.md](./freshness-schemas.md).

**Verdict:** architecture is go; **M2 unblocked**. Plan ends at **M4: write proposals** for deferred work (`kb/reference/proposals/collection-as-artifact-freshness.md`).

---

## Resolved contracts (do not re-litigate)

1. **Queued-job CAS** — `review_pairs.expected_baseline_revision` captured at pair create; `finalize_capture_refresh()` CASes against it. Migration marks job `49` `failed` with `stale-queued-capture` when captures ≠ accepted inputs.
2. **Two refresh paths** — capture refresh (review-owned, no live check) vs observation refresh/ack (live revalidation). Generic accept rejects `review-pair`.
3. **Dead targets** — migration skips four `transformation-closure` baselines; runtime `commonplace-freshness-retire` for later cases. `input-missing` → exit `1`.
4. **Done-when** — prohibit duplicated compare/persist in review; adapters stay.

**M1 pins:** `file-text` versioning only; JSON in freshness-schemas.md. Collection-as-artifact freshness is [deferred](./future-work-collection-freshness.md).

---

## Still easy to miss

- No compatibility shim surviving migration.
- Malformed baselines → store error, never `missing-baseline`.
- `criterion-changed` before `note-changed` in public review output.
- Stale ingests = semantic derivative maintenance — not prose parsing; collection-level selection is deferred.
- Global status ≠ discovery; review selector owns `missing-baseline`.
- WAL DB: checkpoint before read-only migration.
- Snapshot pruning across `freshness_inputs` + `review_pairs` is highest bug risk.
- Capture refresh can succeed while live files diverged; immediate staleness is expected, not a bug.