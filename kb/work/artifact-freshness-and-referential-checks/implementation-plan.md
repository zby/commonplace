# Implementation plan: general freshness, review-first (v1)

## Outcome

Replace review-specific freshness tables with one artifact-neutral substrate, migrate retained review baselines, and make review commands adapters over that substrate. Ship repository-wide status and generic accept/ack/retire over **`file-text`** inputs and **`review-pair`** targets.

Collection-as-artifact freshness (`collection-text`, `collection-maintenance`) is **deferred** — sketched in [future-work-collection-freshness.md](./future-work-collection-freshness.md), promoted to a proposal in step 9 (M4). This plan does not implement it.

The mechanism records exact input snapshots against which a target was accepted, compares them with current resolved versions, and selects affected targets. It does not adjudicate truth, run reviews, rewrite notes, or infer dependencies from links.

## Milestones

| gate | blocks | done when |
|---|---|---|
| **M1** | all code | schema + [freshness-schemas.md](../../reference/freshness-schemas.md) pinned; migration fixtures pass; live-store rehearsal; backup byte hash unchanged |
| **M2** | M3 | full review suite at CLI boundary; selector JSON parity pre/post migration |
| **M3** | M4 | `commonplace-freshness-{status,accept,ack,retire}` over review-pair targets |
| **M4** | workshop close | proposal committed; plan ends |

## Fixed decisions

- **One mechanism, one store.** `commonplace-store.sqlite` replaces the default; `review-store.sqlite` stays an untouched read-only backup. No parallel freshness implementations.
- **`file-text` only in v1.** SHA-256 of exact UTF-8 file content; snapshot text retained for diffs.
- **Explicit registration.** Links suggest candidates; only accepted baselines register dependencies.
- **Optimistic revision.** Transitions CAS on `expected_baseline_revision`; no file locks.
- **Queued-job revision at pair create.** `review_pairs.expected_baseline_revision` (or `NULL`). Finalization CASes the stored value. Baseline moved after queue → fail (`stale-baseline-revision` / migration `stale-queued-capture` for job `49`).
- **Two refresh paths.** Capture (review `finalize_capture_refresh()`, job snapshots) vs observation (accept/ack, live revalidation). Generic accept rejects `review-pair`.
- **Retirement.** `commonplace-freshness-retire`; migration skips baselines whose paths no longer exist (four `transformation-closure`). `input-missing` → exit `1`.
- **Review parity before extension.** Missing-baseline discovery, reason mapping, trivial ack, all-or-nothing finalization, evidence retention, pruning — unchanged at the CLI boundary. `criterion-changed` before `note-changed` when both changed.
- **Malformed state is errors.** Never downgrade to `missing-baseline` or ordinary staleness.

## Semantic model

**Target:** `target_kind` + canonical `target_key_json`. v1: `review-pair` + `{note_path, criterion_path, model_partition}`.

**Baseline:** one current row per target — `revision`, `accepted_at`, complete input set, optional review evidence bridge.

**Input:** role + path + `file-text` + accepted snapshot id/hash/text. Core emits `input-changed`, `input-missing`, `version-error`; review adapter maps to `note-changed` / `criterion-changed`.

**Transitions:**

| transition | who | live check | evidence |
|---|---|---|---|
| capture refresh | review finalization | no | replaced |
| observation refresh | `commonplace-freshness-accept` | yes | n/a (rejects review-pair) |
| observation ack | `commonplace-freshness-ack`, `commonplace-ack-review` | yes | preserved |
| retirement | `commonplace-freshness-retire` | — | cascade delete bridge |

Schema authority: [database-design.md](./database-design.md). JSON authority: [freshness-schemas.md](../../reference/freshness-schemas.md).

## Implementation sequence

### 1. ADR

Record general freshness and review-first migration. Supersede ADR 032/051 only where they assume review-only or defer generalization until a second consumer. Preserve ADR 051 full-pass captures. State operational DB is now a Commonplace store. Leave review execution review-owned. Note collection-as-artifact freshness is deferred to a follow-on proposal, not this ADR's implementation scope.

### 2. Store, schema, migration (M1)

Add `commonplace.store`, `commonplace.freshness.*`, `scripts/migrate-review-db-v7-to-commonplace-store.py`.

Migration (read-only source, refuse WAL without checkpoint, refuse existing destination):

1. copy snapshots → `artifact_snapshots` (`file-text`), preserving ids and text;
2. copy jobs/pairs; add `expected_baseline_revision` column (init `NULL`);
3. transform baselines → `review-pair` + two inputs + evidence bridge; **skip** rows whose note or criterion path missing on disk;
4. disposition queued pairs: set `expected_baseline_revision`; fail job when captures ≠ accepted (`job 49`);
5. verify counts, integrity, selector parity; atomically install destination;
6. re-hash source backup unchanged.

| repository | jobs | pairs | snapshots | source baselines | → baselines | → inputs |
|---|---:|---:|---:|---:|---:|---:|
| Commonplace | 39 | 53 | 19 | 52 | 48 | 96 |
| Epistack | 14 | 14 | 17 | 14 | 14 | 28 |

Commonplace delta: 4 skipped `transformation-closure`, 1 failed queued job.

### 3. Review adapter (M2)

In order:

1. snapshots through `file-text` / `artifact_snapshots`;
2. persist `expected_baseline_revision` at pair create;
3. load targets via general baseline + evidence bridge;
4. `finalize_capture_refresh()` — complete job, CAS, refresh from captures, replace evidence, prune;
5. ack paths → observation ack transaction;
6. review target selector ← generic resolution + `missing-baseline` discovery;
7. warn selector ← generic projection;
8. pruning respects both `freshness_inputs` and `review_pairs` references.

Delete old review baseline tables/helpers in the same change. No surviving compatibility shim.

### 4. Review parity tests (M2 gate)

Full review test suite; migration fixtures; selector JSON parity (fresh, missing-baseline, note/criterion/both changed); finalization all-or-nothing; ack preserves evidence; pruning cases including single-input ack and shared snapshots.

Do not proceed to step 5 until M2 passes.

### 5. Global selector (M3)

`commonplace-freshness-status` — all registered targets, deduped resolution, `--json`/`--diff`/`--all`/filters, exit 0/1/2 per [freshness-schemas.md](../../reference/freshness-schemas.md). Review selector keeps `missing-baseline` discovery.

### 6. Generic surfaces (M3)

Library: `accept_target_observations`, `ack_target_inputs`, `refresh_target_from_captures`, `retire_target`, `load_target_status`, `select_stale_targets`.

CLI: `commonplace-freshness-{accept,ack,retire,status}`. Accept rejects `review-pair`. Ack consumes status JSON.

### 7. Documentation and rollout

Update commands, storage-architecture, lib-modules, review docs, ADR, `AGENTS.md` vocabulary, package entry points. Rollout: land code → migrate Commonplace copy → switch default → migrate Epistack copy → global check on review targets. Rollback: restore code + point at v7 backup, or rebuild destination from backup.

### 8. Proposals for deferred work (M4 — terminal)

Promote [future-work-collection-freshness.md](./future-work-collection-freshness.md) to `kb/reference/proposals/collection-as-artifact-freshness.md` per [proposals contract](../../reference/proposals/README.md):

- `description` leads with `Proposal:`; `traits: [design-proposal]`;
- dated current-state anchor on shipped v1 store;
- `collection-text` encoding, `collection-maintenance` shape, schema widening, Epistack acceptance cases, forces, free choices, adoption criteria;
- rationale edges to `kb/notes/`, not inlined theory.

Narrow the workshop scratch to a pointer. Open referential-check questions become additional proposals only when worked material exists.

**This step ends the plan.** Workshop deletion follows M4 commit.

## File map

**New:** `src/commonplace/store.py`, `store-schema.sql`, `freshness/{models,versioning,store,selector,transitions}.py`, `cli/freshness_*.py`, migration script, tests.

**Edit:** `review/{review_db,review_schema,freshness,review_target_selector,acknowledgement,ack_trivial_note_changes,finalization,warn_selector}.py` and tests using old table names.

**Docs:** this workshop set + `kb/reference/proposals/collection-as-artifact-freshness.md` (M4).

## Verification

```bash
pytest tests/commonplace/freshness tests/commonplace/review
pytest tests/commonplace/cli/test_guard_full_pass_report.py tests/commonplace/lib/test_full_pass.py
ruff check src tests && pytest
```

Per migrated store copy:

```bash
sqlite3 -readonly kb/reports/commonplace-store.sqlite 'PRAGMA integrity_check; PRAGMA foreign_key_check;'
commonplace-review-target-selector --all-gates --model-partition <partition> --json
commonplace-freshness-status --all --json
```

## Non-goals

Semantic truth checking; auto-rewrite; link-derived registration; pluggable resolvers; full-pass state in SQLite; lineage events; collection-text / collection-maintenance in v1.

## Done when

1. no duplicated review freshness compare/persist; adapters for discovery, reasons, trivial ack, capture finalization remain;
2. retained review baselines on generic schema with parity-tested behavior;
3. finalization and ack use shared transition primitives (capture vs observation split intact);
4. global status over registered review-pair targets;
5. accept/ack/retire fixture-tested for `file-text`;
6. migration rehearsals pass; backups byte-identical;
7. queued-job CAS, retirement, `input-missing` exit `1` shipped;
8. reference docs + ADR current; and
9. M4 proposal committed — workshop may close.