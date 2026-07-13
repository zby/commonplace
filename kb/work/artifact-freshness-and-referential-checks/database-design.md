# Database design: review-first general freshness store

## Decision

Build a new `kb/reports/commonplace-store.sqlite` beside the existing `kb/reports/review-store.sqlite`. The old database is the immutable migration backup: the migration opens it read-only, never renames it, never changes its schema version, and never deletes it. Only after the new database passes structural and behavioral verification do commands switch their default path to `commonplace-store.sqlite`.

The new database contains both:

- general operational freshness state — path-keyed snapshots, current target baselines, accepted inputs, selection, refresh, and acknowledgement; and
- review-owned execution and evidence state — review jobs, review pairs, result protocols, outcomes, model partitions, and the evidence pair retained by a review freshness target.

There is one freshness mechanism. Review becomes the first target adapter over the general tables. `review_freshness_evidence` is review-owned metadata attached to a generic baseline, not a second acceptance or freshness table.

## Physical files and version boundary

| path | role after migration | mutation policy |
|---|---|---|
| `kb/reports/review-store.sqlite` | Schema-v7 backup and migration source | Open read-only; never automatically update or delete. |
| `kb/reports/commonplace-store.sqlite` | Current operational database | All new review and general freshness writes go here. |
| `kb/reports/commonplace-store.sqlite.tmp` | Migration construction path | May be removed after a failed migration; atomically renamed only after verification. |

The new database starts a new store schema line at `PRAGMA user_version = 1`; it is not review schema v8. `commonplace.store` owns connection setup, schema creation, version refusal, foreign-key enforcement, and whole-store integrity dispatch. The old `commonplace.review.review_schema` version check is retired after migration.

Default and override names change together:

| old | new |
|---|---|
| `kb/reports/review-store.sqlite` | `kb/reports/commonplace-store.sqlite` |
| `COMMONPLACE_REVIEW_DB` | `COMMONPLACE_STORE` |
| review-owned connection initialization | `commonplace.store` connection initialization |

There is no fallback that silently opens the old database. Store preparation follows this rule:

- new default exists → open and validate it;
- new default is absent but old default exists → refuse with `migration required`, naming the migration command;
- neither default exists → create a fresh new store; and
- an explicit `COMMONPLACE_STORE` / `--db` path → operate only on that path and never probe the old default.

This prevents an empty new database from masking retained but unmigrated review evidence.

## Current schema-v7 inventory

The source database has four tables and one view:

```text
review_jobs
review_file_snapshots
review_pairs
freshness_baselines
current_freshness_baselines (view)
```

The two live source stores currently have:

| repository | jobs | pairs | file snapshots | freshness baselines | null snapshot texts | integrity |
|---|---:|---:|---:|---:|---:|---|
| Commonplace | 39 | 53 | 19 | 52 | 0 | `integrity_check=ok`, no FK violations |
| Epistack casebooks | 14 | 14 | 17 | 14 | 0 | `integrity_check=ok`, no FK violations |

The one Commonplace review pair without a current baseline remains retained review evidence/history but produces no freshness target.

## Object-by-object change map

| schema-v7 object | new-store object | disposition | exact change |
|---|---|---|---|
| `review_jobs` | `review_jobs` | **Stays** | Same name, columns, checks, indexes, ids, and review ownership. |
| `review_file_snapshots` | `artifact_snapshots` | **Renamed and generalized** | Each `(path, hash, text)` becomes a `file-text` snapshot. Path remains artifact identity; snapshot ids, hashes, text, and timestamps are preserved. |
| `review_pairs` | `review_pairs` | **Stays, foreign keys retargeted** | Same review fields and ids. The two reviewed snapshot columns now reference `artifact_snapshots`. |
| `freshness_baselines` | `freshness_baselines` + `freshness_inputs` | **Generalized** | The old review-shaped row becomes one current `review-pair` baseline and two accepted input roles, `note` and `criterion`. Target identity stays on the baseline row. |
| `freshness_baselines.evidence_review_pair_id` | `review_freshness_evidence.evidence_review_pair_id` | **Moved** | Evidence ownership is review-specific and retains a real FK to `review_pairs`. |
| `freshness_baselines.baseline_note_snapshot_id` | `freshness_inputs.accepted_snapshot_id`, input `note` | **Moved** | The role becomes data instead of a dedicated column. |
| `freshness_baselines.baseline_criterion_snapshot_id` | `freshness_inputs.accepted_snapshot_id`, input `criterion` | **Moved** | Same. |
| `freshness_baselines.baseline_updated_at` | `freshness_baselines.accepted_at` | **Renamed** | Timestamp meaning is unchanged. |
| no equivalent | `freshness_baselines.revision` | **New** | Monotonic current-baseline revision used for optimistic compare-and-swap. Migrated rows start at `1`. |
| no equivalent | `freshness_inputs` | **New** | Accepted target-to-path edge state, with one target-owned input role per dependency. |
| no equivalent | `review_freshness_evidence` | **New** | Review-only extension retaining the completed evidence pair for a generic target. |
| `current_freshness_baselines` | `current_review_freshness_baselines` | **Renamed and reimplemented** | Review-shaped projection over generic targets/inputs plus review evidence. It is an adapter view, not canonical state. |

The old names `review_file_snapshots` and `current_freshness_baselines` do not survive as compatibility views. Code and tests move to the new names in the same implementation.

## New canonical schema

The DDL below fixes the intended keys, ownership, and delete behavior. Exact constraint spelling may change during implementation only if the same invariant remains executable.

### Artifact snapshots

```sql
CREATE TABLE artifact_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    artifact_path TEXT NOT NULL CHECK (length(artifact_path) > 0),
    version_kind TEXT NOT NULL CHECK (
        version_kind IN ('file-text', 'collection-text')
    ),
    content_sha256 TEXT NOT NULL CHECK (
        length(content_sha256) = 64
        AND content_sha256 NOT GLOB '*[^0-9a-f]*'
    ),
    content_text TEXT NOT NULL,
    captured_at TEXT NOT NULL,
    UNIQUE (artifact_path, version_kind, content_sha256),
    UNIQUE (snapshot_id, artifact_path, version_kind)
);
```

The stored hash must equal `SHA-256(content_text.encode("utf-8"))`. Snapshot text is mandatory because accepted-to-current diffs are part of acknowledgement. Path is artifact identity; `version_kind` fixes how that path is rendered into versioned text. Identical versions of the same path and version kind deduplicate.

`file-text` reads one regular non-symlink UTF-8 file under `kb/`. `collection-text` renders one `COLLECTION.md`-bearing directory with a fixed Commonplace rule: sorted visible regular non-symlink Markdown content, excluding `COLLECTION.md`, `types/` subtrees, and replaced archives. It has no per-target include/exclude configuration.

### Current accepted baseline and target identity

```sql
CREATE TABLE freshness_baselines (
    target_id INTEGER PRIMARY KEY,
    target_kind TEXT NOT NULL CHECK (length(target_kind) > 0),
    target_key_json TEXT NOT NULL CHECK (length(target_key_json) > 0),
    revision INTEGER NOT NULL CHECK (revision >= 1),
    accepted_at TEXT NOT NULL,
    UNIQUE (target_kind, target_key_json)
);
```

`target_key_json` is canonical structured identity. It is retained because review identity is genuinely composite. Review uses:

```json
{
  "criterion_path": "kb/instructions/review-gates/prose/source-residue.md",
  "model_partition": "codex",
  "note_path": "kb/notes/example.md"
}
```

Epistack collection maintenance uses:

```json
{"collection_path":"kb/lhc/notes"}
```

There is exactly one current baseline row per accepted target. There is no separately persisted unaccepted target and no baseline history. Target kind tells the consuming workflow how to respond; any authored contract that affects acceptance is registered as an ordinary input.

### Accepted target inputs

```sql
CREATE TABLE freshness_inputs (
    target_id INTEGER NOT NULL
        REFERENCES freshness_baselines(target_id) ON DELETE CASCADE,
    input_role TEXT NOT NULL CHECK (length(input_role) > 0),
    artifact_path TEXT NOT NULL CHECK (length(artifact_path) > 0),
    version_kind TEXT NOT NULL CHECK (
        version_kind IN ('file-text', 'collection-text')
    ),
    accepted_snapshot_id INTEGER NOT NULL,
    PRIMARY KEY (target_id, input_role),
    UNIQUE (target_id, artifact_path, version_kind),
    FOREIGN KEY (accepted_snapshot_id, artifact_path, version_kind)
        REFERENCES artifact_snapshots(snapshot_id, artifact_path, version_kind)
);

CREATE INDEX idx_freshness_inputs_path
ON freshness_inputs(artifact_path, version_kind, target_id);
```

The composite FK prevents a baseline from pairing one path/version function with another path's snapshot. `input_role` is stable within the target, drives acknowledgement selection, and carries the target-owned meaning (`note`, `criterion`, `casebook`, `source-scope`, or `contract`). The path index is the reverse-selection route from a changed path to affected targets.

### Review-owned evidence extension

```sql
CREATE TABLE review_freshness_evidence (
    target_id INTEGER PRIMARY KEY
        REFERENCES freshness_baselines(target_id) ON DELETE CASCADE,
    evidence_review_pair_id INTEGER NOT NULL UNIQUE
        REFERENCES review_pairs(review_pair_id)
);
```

Every accepted `review-pair` target has exactly one row here. Non-review targets have none. Refresh replaces the evidence pair; acknowledgement preserves it.

## Review tables that stay

### `review_jobs`

`review_jobs` stays byte-for-byte at the logical schema level:

- same `review_job_id` primary key;
- same model partition and runner provenance;
- same `queued` / `completed` / `failed` lifecycle checks;
- same grouping values;
- same indexes; and
- same rows and ids during migration.

No freshness input, path-versioning, or generic transition field is added to `review_jobs`.

### `review_pairs`

Every existing column and constraint stays. Only the FK destination changes:

```sql
reviewed_note_snapshot_id INTEGER REFERENCES artifact_snapshots(snapshot_id),
reviewed_criterion_snapshot_id INTEGER REFERENCES artifact_snapshots(snapshot_id)
```

The column names remain review-specific because they describe the inputs embedded in one review job. They are not the canonical current baseline after finalization; the accepted generic inputs are.

Review result files, prompt paths, job-output paths, result kinds, outcomes, completion checks, and derived artifact naming do not move into general freshness tables.

## Review adapter view

`current_review_freshness_baselines` reconstructs the existing review-facing record from generic state:

- selects `freshness_baselines.target_kind = 'review-pair'`;
- joins inputs with roles `note` and `criterion`;
- joins their accepted snapshots;
- joins `review_freshness_evidence`, `review_pairs`, and `review_jobs`;
- exposes note path, criterion path, model partition, evidence pair id, snapshot ids, hashes, texts, accepted timestamp, result kind, and outcome; and
- includes only completed evidence whose pair paths and model partition agree with the target key and input paths.

The view preserves a convenient review query surface, but malformed targets must raise an integrity error rather than disappear and look like `missing-baseline`. `assert_review_freshness_integrity()` therefore checks every `review-pair` target before the view is used.

The old `current_freshness_baselines` name is removed so no caller can accidentally continue treating the review projection as the canonical general mechanism.

## Ownership by module

| concern | owner |
|---|---|
| DB path, connection, schema version, transaction setup, whole-store integrity | `commonplace.store` |
| Path versioning (`file-text` / `collection-text`), snapshots, hashes, generic baseline/input rows | `commonplace.freshness` |
| Generic current-status and reverse-selection queries | `commonplace.freshness` |
| Refresh acceptance and acknowledgement compare-and-swap | `commonplace.freshness` |
| Review job/pair CRUD and result integrity | `commonplace.review` |
| Mapping review target keys and input roles to review CLI concepts | `commonplace.review` |
| Review evidence bridge and evidence pruning | `commonplace.review` |
| Full-pass packet captures and guards | `commonplace.lib.full_pass`; unchanged and outside this DB |

Whole-store initialization runs generic integrity checks and then the explicit review integrity check. There is no target-kind hook registry, and the freshness core does not import review result semantics.

## Transaction semantics

### Initial acceptance

Within one `BEGIN IMMEDIATE` transaction:

1. require no current target with the same `(target_kind, target_key_json)` baseline;
2. insert or reuse path-keyed snapshots;
3. insert the revision-1 baseline containing target identity;
4. insert the complete input-role set;
5. let the review wrapper write review evidence when the target is a review pair;
6. run generic and review integrity checks; and
7. commit.

Any failure rolls back the baseline, inputs, and review evidence together.

### Refresh acceptance

Within one transaction:

1. load the target and require `revision == expected_revision`;
2. insert or reuse the exact snapshots the producer inspected or consumed;
3. replace the complete input set;
4. update the acceptance timestamp;
5. increment revision once;
6. let the review wrapper replace evidence when the target is a review pair;
7. run integrity checks;
8. commit; and
9. prune superseded evidence and unreferenced snapshots according to owning references.

Review finalization may accept its job-owned historical snapshots even if live files changed during execution. The selector immediately reports the resulting baseline stale against current text. It never substitutes unseen live text at finalization.

### Acknowledgement

Within one transaction:

1. require the selector payload's expected baseline revision;
2. require each selected current observation still has the version shown to the operator;
3. update only the selected inputs' accepted snapshots;
4. preserve unselected inputs and review evidence, when present;
5. increment revision once and update `accepted_at`;
6. run integrity checks; and
7. commit.

This prevents a displayed diff from acknowledging a later, unseen edit. File locks and filesystem transactions remain out of scope; an edit after the final observation simply makes the new baseline stale.

### Deletion and pruning

There is no generic retirement or target-deletion command in the first implementation. The FK shape nevertheless ensures that an explicitly removed baseline cascades its inputs and review evidence without deleting review jobs or pairs. Snapshot garbage collection occurs only after all `freshness_inputs` and `review_pairs` references are gone.

## Generic selection query

The repository-wide selector:

1. loads registered targets and current accepted inputs;
2. versions each unique `(artifact_path, version_kind)` once per run;
3. compares current content hashes with accepted snapshot hashes;
4. emits `input-changed`, `input-missing`, or `version-error`, including input role, path, accepted/current versions, and optional accepted-to-current diff;
5. groups changed inputs by target; and
6. returns target identity, baseline revision, and changed inputs.

The selector does not create targets for applicable work that has never been accepted. Review-specific discovery still emits `missing-baseline` for derived `(note, criterion, model partition)` pairs with no registered `review-pair` target.

## Review mapping in detail

One old row:

```text
(note_path, criterion_path, model_partition,
 evidence_review_pair_id,
 baseline_note_snapshot_id,
 baseline_criterion_snapshot_id,
 baseline_updated_at)
```

becomes:

```text
freshness_baselines
  target_kind = review-pair
  target_key = {note_path, criterion_path, model_partition}
  revision = 1
  accepted_at = baseline_updated_at

freshness_inputs
  note      -> file-text(note_path),      baseline_note_snapshot_id
  criterion -> file-text(criterion_path), baseline_criterion_snapshot_id

review_freshness_evidence
  evidence_review_pair_id = old evidence_review_pair_id
```

The review selector maps generic results as follows:

| generic result | input | review result |
|---|---|---|
| no registered target for an applicable pair | — | `missing-baseline` |
| `input-changed` | `note` | `note-changed` plus note diff |
| `input-changed` | `criterion` | `criterion-changed` |
| both changed | both | preserve current review precedence unless separately changed by an ADR |
| malformed registered target or evidence | — | integrity error, never `missing-baseline` |

Existing review precedence currently reports `criterion-changed` before `note-changed`; migration preserves that public behavior even though global status may list both changed inputs.

## Epistack mapping

Each casebook gets one `collection-maintenance` target. It registers three path-based inputs:

| input role | version kind | meaning |
|---|---|---|
| `casebook` | `collection-text` over the notes collection | Exact maintained output set accepted by the last maintenance pass. |
| `source-scope` | `collection-text` over the source collection | Collection source snapshot; catches member addition, removal, rename, and content change. |
| `contract` | `file-text` over the notes `COLLECTION.md` | Maintenance semantics applied by the pass. |

`collection-text` stores canonical combined UTF-8 text, not only a directory timestamp or list of hashes. Consequently the same snapshot/diff machinery shows which members and content changed. It applies one fixed Commonplace collection-content rule; no schema column says `source`, `ingest`, or `casebook`.

A source-scope change selects one casebook target. The semantic workflow decides which notes to revise. Refresh replaces all three accepted inputs; acknowledgement may advance only `source-scope` when its inspected change does not affect the casebook.

## Migration algorithm: old database remains the backup

The migration is source-to-destination, never in-place:

1. refuse if `commonplace-store.sqlite` or its temporary path already exists;
2. open `review-store.sqlite` with SQLite URI `mode=ro`;
3. begin a stable read transaction and record its byte hash, `user_version`, schema object list, row counts, `integrity_check`, and `foreign_key_check`;
4. require schema v7, `journal_mode=delete` with no live journal sidecar, and validate every current review baseline;
5. create `commonplace-store.sqlite.tmp` with new schema version 1;
6. copy every old snapshot with the same `snapshot_id`, path, hash, exact text, and capture time, setting `version_kind = 'file-text'`;
7. copy every review job and pair with identical ids and values, retargeting snapshot FKs;
8. transform each old baseline using the review mapping above;
9. run new generic, review, FK, and SQLite integrity checks;
10. compare the old `current_freshness_baselines` projection row-for-row with the new `current_review_freshness_baselines` projection;
11. compare review selector JSON on fresh and deliberately changed fixture files;
12. commit and close the destination;
13. atomically rename only the verified temporary destination to `commonplace-store.sqlite`; and
14. re-hash `review-store.sqlite` and require it to match the source hash recorded at step 3.

Both current source stores use `journal_mode=delete`. A source using WAL must be cleanly checkpointed by the operator before this read-only migration; the migration does not mutate it to do so. If another process changes the source during migration, the final hash check refuses installation of the destination. If any step fails, delete only the temporary destination. The old `review-store.sqlite` remains the backup and recovery source. Neither successful migration nor later normal operation removes it automatically.

Expected transformed counts:

| repository | snapshots | baselines | inputs | review evidence rows |
|---|---:|---:|---:|---:|
| Commonplace | 19 | 52 | 104 | 52 |
| Epistack casebooks | 17 | 14 | 28 | 14 |

## Integrity contract

Whole-store initialization and every baseline transition must reject:

- non-canonical target JSON;
- stored snapshot hashes that do not match stored text;
- accepted snapshots whose path or version kind differs from the input;
- baselines without inputs after commit;
- duplicate target identities or duplicate input roles;
- a `review-pair` target without exactly `note` and `criterion` inputs;
- review inputs whose version kind is not `file-text` or whose paths disagree with the target key;
- review evidence whose pair, paths, model partition, completion, result kind, outcome, or parent job does not match the target;
- non-review targets with review evidence rows;
- missing referenced snapshots, baselines, jobs, or pairs; and
- any SQLite foreign-key or integrity-check failure.

Integrity failures are store errors. Selectors must never downgrade malformed accepted state to ordinary staleness or missing-baseline output.

## Indexes

Retain current review indexes. The `UNIQUE` constraints already index snapshot identity/version and target identity. Add only the demonstrated reverse-selection index:

```sql
CREATE INDEX idx_freshness_inputs_path
ON freshness_inputs(artifact_path, version_kind, target_id);
```

The critical new query is reverse selection by artifact path and version kind. No target-type or path-class index belongs in the generic schema until a demonstrated query needs it.

## Deliberately unchanged boundaries

- Markdown remains the canonical artifact surface.
- Review jobs and pairs remain purpose-built execution/evidence state.
- Review result files remain derived paths outside freshness tables.
- Model partition remains review target identity, not a generic freshness column.
- Full-pass captures remain packet-owned files and do not migrate.
- Git and filesystem timestamps remain outside freshness correctness.
- Ordinary links do not become accepted dependencies.
- Semantic reassessment remains outside the selector.
- Baseline history and append-only lineage events remain out of scope.

## Implementation gate

Do not begin schema or review-code changes until this design and the implementation plan agree on:

1. the source-to-destination migration with the old database retained untouched;
2. the exact old-to-new object map;
3. path-keyed snapshot versioning;
4. generic baseline/input keys and delete behavior;
5. the review evidence extension and parity view;
6. refresh and acknowledgement transaction semantics;
7. integrity and pruning ownership; and
8. the Epistack collection source snapshot representation.
