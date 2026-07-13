# Implementation plan: one general freshness mechanism, migrated review-first

## Outcome

Replace the review-specific freshness tables with one artifact-neutral freshness substrate, migrate all retained review baselines onto it, and make review commands adapters over that substrate before registering any non-review target. Then add an Epistack-shaped casebook-maintenance target whose accepted inputs include a collection source snapshot. One repository-wide status command must report stale review and casebook targets from the same baseline and selector machinery.

This is a current-state mechanism. It records the exact input snapshots against which a target was accepted, compares them with current resolved versions, and selects affected targets. It does not decide whether changed prose is still true, run a review, update a note, or infer dependencies from authored links.

## Fixed decisions

- **One mechanism and one operational store.** Review freshness migrates first. There will not be a general freshness store beside `freshness_baselines` or a review freshness implementation beside the general one.
- **The existing store becomes general.** Rename the default local database from `kb/reports/review-store.sqlite` to `kb/reports/commonplace-store.sqlite`; replace `COMMONPLACE_REVIEW_DB` with `COMMONPLACE_STORE`. Review jobs and evidence remain review-owned tables in that database, while snapshots, targets, baselines, inputs, selection, and acknowledgement become general.
- **Accepted snapshots, not timestamps or Git, decide freshness.** A version remains the SHA-256 of exact UTF-8 text. Snapshot text is retained so selectors can show accepted-to-current diffs.
- **Targets and inputs are artifact-neutral.** The freshness core sees a target kind, canonical structured key, opaque target policy, named input roles, resolver identities, accepted snapshots, and optional target-owned acceptance metadata. It does not branch on source, ingest, note, report, or criterion paths.
- **Registration is explicit.** Authored links may suggest dependencies to a producer, but only an accepted baseline registers them.
- **Selection is not execution or truth adjudication.** A changed input means the accepted basis changed. Target-owned code decides whether the response is reassessment, regeneration, acknowledgement, retirement, or something else.
- **Optimistic transitions.** Baseline writes compare an expected baseline revision to prevent two writers from silently overwriting each other. They do not lock repository files. A file edit after capture or acceptance makes the new baseline immediately stale on the next check.
- **Review behavior is preserved before extension.** Result kinds, outcomes, model partitions, missing-baseline discovery, stale reasons, diffs, acknowledgement, all-or-nothing finalization, evidence retention, and pruning must have parity before the first Epistack target is registered.
- **Collection source snapshot is a bounded resolver, not a source ontology.** It is implemented as a generic canonical UTF-8 file-set snapshot. Epistack supplies a source-collection configuration; the freshness core sees an ordinary resolved text input.

## Semantic model

### Target

A target is the unit whose freshness can be asked:

```text
target_kind + canonical target_key_json
```

Examples:

- review: `review-pair` plus `{note_path, criterion_path, model_partition}`;
- Epistack: `collection-maintenance` plus `{collection_path}`;
- later: a generated view, report, instruction bundle, note-maintenance target, or another artifact-owned policy.

The target key is identity, not display text. JSON is normalized with sorted keys and compact separators before persistence and comparison.

### Accepted baseline

One current baseline belongs to one target and contains:

- monotonically increasing `revision`;
- `accepted_at`;
- the complete accepted input set;
- optional opaque `policy_json` returned by the selector; and
- target-owned acceptance metadata stored by an adapter, such as the completed evidence pair for a review target.

Replacing a baseline is current-state upsert, not an append-only event log. Superseded snapshots and target-owned evidence are pruned according to their owning subsystem's retention rules.

### Input

Each accepted input has:

- a stable input name within the target;
- an opaque role meaningful to the target adapter;
- resolver kind and canonical resolver key;
- accepted snapshot id, hash, and exact text.

The core emits `input-changed`, `input-missing`, or `resolver-error` with the input name and role. Adapters may project these into existing domain language. The review adapter maps `note` changes to `note-changed` and `criterion` changes to `criterion-changed` without changing the generic result.

### Transitions

- **Refresh acceptance** replaces the complete input set and target-owned acceptance metadata. For reviews it records a newly completed evidence pair and its already captured note/criterion snapshots. For an Epistack casebook it records the casebook and source-collection snapshots inspected after the maintenance pass.
- **Acknowledgement** preserves target-owned evidence and advances only explicitly selected input snapshots after the operator has inspected their diffs. Unselected stale inputs remain stale.
- Both transitions require the caller's expected baseline revision. Initial acceptance requires that no baseline exists.
- Captured versions, not whatever files happen to contain later, are written. A subsequent filesystem edit therefore produces ordinary staleness rather than a failed or partially rewritten acceptance.

## Store schema

Create one package-owned operational schema and connection layer under `commonplace.store`; review and freshness modules use it instead of each initializing overlapping schema state.

```text
artifact_snapshots
  snapshot_id INTEGER PRIMARY KEY
  resolver_kind TEXT NOT NULL
  resolver_key_json TEXT NOT NULL
  content_sha256 TEXT NOT NULL
  content_text TEXT NOT NULL
  captured_at TEXT NOT NULL
  UNIQUE(resolver_kind, resolver_key_json, content_sha256)

freshness_targets
  target_id INTEGER PRIMARY KEY
  target_kind TEXT NOT NULL
  target_key_json TEXT NOT NULL
  UNIQUE(target_kind, target_key_json)

freshness_baselines
  target_id INTEGER PRIMARY KEY REFERENCES freshness_targets(target_id)
  revision INTEGER NOT NULL
  accepted_at TEXT NOT NULL
  policy_json TEXT NOT NULL

freshness_inputs
  target_id INTEGER NOT NULL REFERENCES freshness_baselines(target_id) ON DELETE CASCADE
  input_name TEXT NOT NULL
  role TEXT NOT NULL
  resolver_kind TEXT NOT NULL
  resolver_key_json TEXT NOT NULL
  snapshot_id INTEGER NOT NULL REFERENCES artifact_snapshots(snapshot_id)
  PRIMARY KEY(target_id, input_name)
  UNIQUE(target_id, resolver_kind, resolver_key_json, role)

review_freshness_evidence
  target_id INTEGER PRIMARY KEY REFERENCES freshness_baselines(target_id) ON DELETE CASCADE
  evidence_review_pair_id INTEGER NOT NULL REFERENCES review_pairs(review_pair_id)
```

`review_pairs.reviewed_note_snapshot_id` and `reviewed_criterion_snapshot_id` reference `artifact_snapshots`; the old `review_file_snapshots` table disappears. The review evidence bridge is review-owned acceptance metadata, not a second baseline. Review integrity checks require every `review-pair` baseline to have exactly `note` and `criterion` inputs, a matching structured key, and one completed evidence pair under the same model partition.

Do not introduce generic events, runner fields, output tables, scheduling state, or a polymorphic evidence foreign key. Target-specific evidence remains in target-owned extension tables with real foreign keys.

## Resolver contract

Introduce `commonplace.freshness.resolvers` with one result type containing resolver identity, exact text, and content hash.

### `file-text`

- Key: `{path}` with a normalized repository-relative path under `kb/`.
- Reject path escape, symlinks, non-files, non-UTF-8 content, and inconsistent stored hashes.
- Reuse `commonplace.lib.hashing` for the version contract.
- This resolver replaces review's path-specific snapshot helper.

### `file-set-text`

- Key: normalized root plus explicit include/exclude rules.
- Enumerate visible, regular, non-symlink UTF-8 files deterministically; sort normalized repository-relative paths.
- Produce canonical text containing an unambiguous path header and exact content for every member. The combined text is the snapshot, so additions, removals, renames, and edits all change one content hash and yield an accepted-to-current diff without Git.
- The resolver is generic. Epistack names one configured use a **collection source snapshot** and points it at a case's source collection.
- The first version supports Markdown inputs only. Binary/PDF versioning, external URLs, Git revisions, and arbitrary query resolvers remain out of scope.

## Implementation sequence

### 1. Record the architectural change

Write an ADR accepting general freshness and review-first migration. It should:

- supersede ADR 032 only where it says the universal shape remains review-only;
- supersede ADR 051 only where it defers generalization until a second consumer;
- preserve ADR 051's full-pass-owned captures, retention, and transition policy;
- state that the operational database has become a Commonplace store rather than a review store;
- leave review execution, evidence, result protocols, and model partitions review-owned; and
- retire the source-as-gate branch of `factored-dependency-pairs-for-review-freshness.md` in favor of a general maintenance target, while retaining factored type and collection conformance pairs.

Do not rewrite accepted ADR history to make it appear that the decision was always general.

### 2. Add the general store, schema, models, and migrations

Add:

- `src/commonplace/store.py` and a single packaged schema resource;
- `src/commonplace/freshness/models.py`;
- `src/commonplace/freshness/resolvers.py`;
- `src/commonplace/freshness/store.py` for target, snapshot, baseline, input, transition, integrity, and pruning operations; and
- `scripts/migrate-review-db-v7-to-commonplace-store.py`.

The migration must be transactional and preservation-first:

1. refuse anything except a schema-v7 source that passes `integrity_check`, `foreign_key_check`, and current review-baseline integrity;
2. create generic snapshots while preserving snapshot IDs and exact text;
3. create one `review-pair` target and baseline per old freshness row;
4. create two generic inputs per migrated baseline, named `note` and `criterion`;
5. create one review evidence bridge per migrated baseline;
6. retain queued, completed, and failed review jobs and every review pair unchanged;
7. verify row counts, paths, hashes, evidence ids, outcomes, result kinds, model partitions, and selector classifications before commit;
8. write a byte-identical backup and report its hash before replacing the live store; and
9. refuse to overwrite an existing destination.

Current preservation fixtures:

| repository | jobs | pairs | snapshots | baselines | migrated targets | migrated inputs |
|---|---:|---:|---:|---:|---:|---:|
| Commonplace | 39 | 53 | 19 | 52 | 52 | 104 |
| Epistack casebooks | 14 | 14 | 17 | 14 | 14 | 28 |

The one Commonplace review pair without a current baseline remains review evidence/history and creates no freshness target.

### 3. Put review freshness behind the general API

Change review code in this order:

1. capture note and criterion inputs through `file-text` and `artifact_snapshots`;
2. load `review-pair` targets through the general baseline query and review evidence bridge;
3. make finalization call the generic refresh-acceptance transaction, then perform existing review-evidence pruning;
4. make `commonplace-ack-review` and trivial-change acknowledgement call the generic acknowledgement transaction while preserving the evidence bridge;
5. make the review target selector consume generic resolution results and retain its current missing-baseline discovery and public reason names;
6. make warning selection read the generic baseline projection; and
7. update snapshot/evidence pruning so a snapshot is removed only when neither a queued/retained review pair nor any generic freshness input references it.

Delete the old review-specific baseline read/write helpers, old baseline table/view, and duplicate review snapshot code in the same change. A temporary compatibility adapter is allowed only inside an in-progress commit and must not survive the completed migration.

Review relocation behavior stays unchanged: historical review targets retain their old path identity, and the relocated artifact receives `missing-baseline` under its new path rather than silently re-keying old evidence.

### 4. Prove review parity

Before adding non-review registration:

- run the complete existing review test suite unchanged at its CLI boundary;
- add schema/integrity tests for malformed target keys, missing inputs, wrong evidence pairs, wrong model partitions, incomplete evidence, and corrupted snapshots;
- add migration tests using populated schema-v7 fixtures;
- compare pre/post migration selector JSON for fresh, missing-baseline, note-changed, and criterion-changed cases;
- prove verdict and report pairs keep their distinct completion semantics;
- prove finalization remains all-or-nothing;
- prove ack preserves evidence and refresh replaces it;
- prove superseded evidence and snapshots are pruned without deleting shared generic snapshots; and
- rehearse the migration on copies of both current live stores and compare the counts in the table above.

Do not proceed to Epistack targets until parity passes.

### 5. Add the repository-wide selector

Add `commonplace-freshness-status` as a thin CLI over the general selector.

Default behavior:

- inspect every registered target in `commonplace-store.sqlite`;
- resolve each unique current input once per run;
- print only stale targets unless `--all` is supplied;
- support `--json`, `--diff`, `--target-kind`, and exact target-key filtering;
- return target kind/key, baseline revision, policy, and changed inputs with accepted/current versions and optional diffs;
- exit `0` when all selected registered targets are fresh, `1` when any are stale, and `2` for invocation, resolver, or store-integrity failures.

“Global” means all registered targets. It does not infer unregistered dependencies, discover applicable-but-never-reviewed pairs, or treat every link as a baseline. Review's target selector remains responsible for review-specific missing-baseline discovery.

The first global-status acceptance test is review-only: edit one note and one criterion, then prove the global selector and review selector report the same underlying changed inputs while the review adapter preserves its existing public reason names.

### 6. Add generic acceptance and acknowledgement surfaces

Add library operations before choosing elaborate CLI syntax:

- `accept_target(target, complete_inputs, target_metadata, expected_revision)`;
- `ack_target_inputs(target, selected_observations, expected_revision)`;
- `load_target_status(target)`; and
- `select_stale_targets(filters)`.

The operations accept resolved observations, not bare paths, so producers can pass the exact versions they inspected or consumed. Expose them as:

- `commonplace-freshness-accept --input FILE|-` — initial or refresh acceptance from a target manifest containing target identity, policy, complete resolver specifications, expected baseline revision, and the observed versions being accepted;
- `commonplace-freshness-ack --input FILE|- [--input-name NAME ...]` — advance all or selected changed inputs from `commonplace-freshness-status --json` output while preserving target-owned evidence; and
- `commonplace-freshness-status ... --json` — the canonical observation payload for acknowledgement and external refresh producers.

Accept and ack must reject a mismatched baseline revision or any current version that no longer matches the supplied observation. This is the optimistic-lock boundary: inspect/status, decide, then conditionally advance. Review finalization remains allowed to accept the job-owned snapshots it actually evaluated even when live files have since moved on; the resulting baseline is immediately stale, which is more truthful than silently accepting unseen current text.

Do not build refresh jobs, prompt construction, model dispatch, automatic rewriting, or link-derived registration.

### 7. Add the Epistack-aligned target

Use one coarse maintenance target per casebook rather than staling every note individually:

```json
{
  "target_kind": "collection-maintenance",
  "target_key": {"collection_path": "kb/lhc/notes"},
  "policy": {"on_input_change": "semantic-reassessment"},
  "inputs": {
    "casebook": {
      "role": "maintained-artifact-set",
      "resolver": "file-set-text",
      "root": "kb/lhc/notes"
    },
    "source-scope": {
      "role": "collection-source-snapshot",
      "resolver": "file-set-text",
      "root": "kb/lhc/sources"
    },
    "contract": {
      "role": "maintenance-contract",
      "resolver": "file-text",
      "path": "kb/lhc/notes/COLLECTION.md"
    }
  }
}
```

Use equivalent targets for eggs and COVID. File-set include/exclude configuration must separate collection content from `COLLECTION.md`, local type specifications, hidden files, and generated reports; those dependencies are registered separately only when the target policy needs them.

The coarse snapshot is deliberate. A source addition has no pre-existing per-file edge, so the collection source snapshot detects it. A changed source selects the casebook target; the semantic maintenance workflow decides which notes, if any, require edits. After that workflow, refresh acceptance records the new casebook, source-scope, and contract snapshots. If the source change does not affect the map, acknowledgement advances only `source-scope` after its diff is inspected.

Epistack acceptance cases:

1. adding a source selects exactly its casebook target;
2. editing or removing a source selects the same target and exposes a diff;
3. changing one casebook note selects its casebook target but not another case;
4. changing an unrelated artifact selects no casebook target;
5. acknowledging an irrelevant source diff preserves the accepted casebook snapshot;
6. refreshing after note edits replaces the complete accepted input set;
7. editing again after acceptance makes the target immediately stale; and
8. the same global command reports stale review-pair and collection-maintenance targets together.

### 8. Documentation and rollout

Update, in the implementation commit sequence:

- `kb/reference/commands.md`;
- `kb/reference/storage-architecture.md`;
- `kb/reference/lib-modules.md`;
- `kb/reference/README-REVIEW-SYSTEM.md` and `review-architecture.md`;
- the accepted ADR and affected proposal status;
- `.gitignore`, package data, and CLI entry points;
- `AGENTS.md` vocabulary so freshness baseline is no longer defined as review-only; and
- the artifact-freshness and lineage workshops, extracting or retiring the now-implemented deferred generic design.

Rollout order:

1. land schema, migration, generic API, and review adapter with fixture tests;
2. migrate a copy of the Commonplace live store and run full parity checks;
3. migrate the Commonplace live store and switch its default path;
4. migrate a copy of the Epistack live store and run review/global parity checks;
5. migrate the Epistack live store;
6. register the three Epistack collection-maintenance targets;
7. run the first global freshness check and disposition every selected target; and
8. only then make global freshness part of Epistack's normal update/handoff instructions.

## File-level work map

Expected new implementation surfaces:

- `src/commonplace/store.py`
- `src/commonplace/store-schema.sql`
- `src/commonplace/freshness/__init__.py`
- `src/commonplace/freshness/models.py`
- `src/commonplace/freshness/resolvers.py`
- `src/commonplace/freshness/store.py`
- `src/commonplace/freshness/selector.py`
- `src/commonplace/freshness/transitions.py`
- `src/commonplace/cli/freshness_status.py`
- acceptance/ack CLI modules after the library contract settles
- `scripts/migrate-review-db-v7-to-commonplace-store.py`
- corresponding `tests/commonplace/freshness/`, migration, and CLI tests

Expected review edits:

- `src/commonplace/review/review_db.py`
- `src/commonplace/review/review_schema.py` and the old review schema resource, which are replaced or narrowed to review integrity/evidence ownership
- `src/commonplace/review/freshness.py`
- `src/commonplace/review/review_target_selector.py`
- `src/commonplace/review/acknowledgement.py`
- `src/commonplace/review/ack_trivial_note_changes.py`
- `src/commonplace/review/finalization.py`
- `src/commonplace/review/warn_selector.py`
- tests that query old table/view names directly

Extract a shared unified-text-diff helper only when review, full-pass, and general selector call sites can use the same exact input/output contract. Do not force full-pass report parsing or capture retention into the general store.

## Verification commands

At each implementation phase:

```bash
pytest tests/commonplace/freshness
pytest tests/commonplace/review
pytest tests/commonplace/cli/test_guard_full_pass_report.py tests/commonplace/lib/test_full_pass.py
ruff check src tests
pytest
```

For every migrated live-store copy:

```bash
sqlite3 -readonly kb/reports/commonplace-store.sqlite 'PRAGMA integrity_check; PRAGMA foreign_key_check;'
commonplace-review-target-selector --all-gates --model-partition codex --json
commonplace-freshness-status --all --json
```

Use the actual model partitions present in each store when comparing selector output; do not assume `codex` is the only partition.

## Explicit non-goals

- semantic truth checking in deterministic code;
- automatic note rewriting or refresh execution;
- dependency inference from links or prose;
- source- or ingest-specific branches in the freshness core;
- general binary, URL, external-Git, database-row, or package-asset resolvers;
- locks, filesystem transactions, or stronger concurrency before a failed optimistic case;
- migration of full-pass packet state into SQLite;
- append-only lineage events or historical baseline retention;
- automatic registration of every artifact in the KB; and
- claiming that global status proves unregistered work is current.

## Done when

1. no review-specific freshness table, snapshot table, selector implementation, or acknowledgement implementation remains;
2. every retained Commonplace and Epistack review baseline is preserved on the generic schema with parity-tested selection and evidence semantics;
3. review finalization and acknowledgement use the same refresh/ack transitions available to other target kinds;
4. one global command reports all registered stale review and non-review targets from the same store;
5. the file-set resolver detects collection membership and content changes using stored UTF-8 snapshots and diffs;
6. all three Epistack casebooks have registered collection-maintenance baselines and a source change selects the correct casebook without source-specific freshness code;
7. acknowledgement and semantic refresh advance exact accepted versions without conflating changed inputs with false outputs;
8. the full test suite and both live-store migration rehearsals pass; and
9. durable architecture, command, storage, review, and operator documentation describes the shipped mechanism, after which this workshop can close.
