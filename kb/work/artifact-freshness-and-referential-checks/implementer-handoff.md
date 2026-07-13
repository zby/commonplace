# Implementer handoff

Authority: [implementation-plan.md](./implementation-plan.md), [database-design.md](./database-design.md).

**Verdict:** architecture is go; **four contracts must be written before persisted hashes / public CLIs** (M1 schema OK; M2 blocked until these land in plan or database-design).

---

## Blocking — resolve in design first

### 1. Queued-job CAS (live today)

Refresh requires `expected_revision`, but queued pairs store captured snapshots only — not revision at job creation. **Job 49** is the case: captured note snapshot `24`, current baseline snapshot `29`; finalize-as-is would overwrite newer evidence.

**Decide:** persist `expected_revision` or `expected_absence` on each pair at job create; on finalize, CAS against that — fail/requeue if baseline moved. Policy for migrated queued jobs with stale captures.

### 2. Two refresh paths — do not conflate

| Path | Live-file check | Writes |
|---|---|---|
| **Capture refresh** (review finalize) | No — job-owned snapshots | Baseline CAS + evidence replace |
| **Observation refresh** (accept CLI, ack) | Yes — must match status output | Baseline CAS, evidence preserved on ack |

Generic `commonplace-freshness-accept` must **not** be the review finalization entry point. Expose one **review-owned transaction** (or extension hook) that atomically: complete pairs → generic refresh from captures → `review_freshness_evidence` update.

### 3. Dead registered targets

No deletion/retirement in v1, but global status scans all registered targets. **Four live baselines** still point at deleted `kb/work/transformation-closure/README.md` → perpetual `input-missing`.

**Decide:** target retirement command, migration-time prune of dead paths, or documented manual SQL — and whether `input-missing` exits `1` (stale) or `2` (integrity).

### 4. Done-when wording

Criterion 1 ("no review-specific selector or acknowledgement implementation") contradicts keeping review adapters for `missing-baseline`, reason mapping, trivial ack.

**Reword:** prohibit **duplicated** freshness compare/persist in review code; adapters and discovery stay.

---

## Pin in M1 (before hashing / JSON CLI)

- **`collection-text` byte format** — recursive scope, nested collections, hidden paths, archive filenames, path framing, newlines. Hash stability depends on this.
- **Status / accept / ack JSON** — canonical schema; ack consumes status output.

---

## Still easy to miss (non-blocking)

- No compatibility shim surviving migration.
- Malformed baselines → store error, never `missing-baseline`.
- `criterion-changed` before `note-changed` in public review output.
- Stale ingests = derivative maintenance via `casebook` / `source-scope` change — not prose parsing.
- Global status ≠ discovery; review selector owns `missing-baseline`.
- WAL DB: checkpoint before read-only migration.
- Snapshot pruning across `freshness_inputs` + `review_pairs` is highest bug risk.