# Pure file review store design

This design asks whether the current review system could keep its lineage state in files and directories rather than SQLite, while preserving the operational behavior that made the DB useful.

The premise is not "plain prose files are enough." The premise is that a directory tree can act as an index when the key is known: if the selector knows `(note_path, gate_path, model_partition)`, it can compute a deterministic filename and retrieve that record directly. The design therefore uses files and directories as a filesystem-backed relational store.

## Current Scale

Snapshot from this checkout on 2026-06-24:

| measure | current value |
|---|---:|
| `review-store.sqlite` file size | 96,219,136 bytes |
| SQLite page size / pages / freelist pages | 4,096 / 23,491 / 12,133 |
| Approx live DB pages | 11,358 pages, about 46.5 MB |
| `review_runs` | 4,182 |
| `review_pairs` | 10,479 |
| completed / missing / pending pairs | 9,034 / 1,100 / 345 |
| `acceptance_events` | 9,059 |
| `current_gate_acceptances` | 9,023 |
| distinct reviewed notes / gates / models | 337 / 38 / 23 |
| max pairs per run | 36 |
| max current gates per note+model | 36 |
| max current notes per gate+model | 176 |
| existing `bundle-reviews/` dirs / files / size | 851 dirs / 4,515 files / 26 MB |
| existing `reviews/` dirs / files / size | 154 dirs / 3,507 files / 15 MB |
| max files in one existing run dir / review-note dir | 37 / 34 |

Stored text payloads in the DB:

| payload | bytes |
|---|---:|
| review-pair rationale markdown | 11,467,579 |
| raw bundle markdown | 5,540,717 |
| debug log | 9,435,928 |
| telemetry JSON | 2,615,569 |

This is comfortably within a file-backed design. The current data is thousands of records, not millions. The risk is not capacity; it is consistency and selector complexity.

## Filesystem Assumptions

This checkout is on `ext4` with 4 KB blocks and a 255-byte filename limit. Modern `ext4` directories use indexed lookup for large directories, so retrieving a record by exact filename is fast enough at this scale. APFS and NTFS have similar practical behavior for keyed lookup. Network filesystems and older filesystems may behave worse.

Design assumptions:

- A directory is acceptable as an index when the caller can compute the child filename.
- Directory enumeration is acceptable for hundreds of children and still tolerable for low thousands.
- Avoid depending on flat directories with tens of thousands of files; shard before that.
- Keep filenames under 255 bytes by hashing long note paths and storing the original path inside the record.
- Treat generated index directories as rebuildable; verify them against the authoritative event files.

## Relation Model

The storage-driving relation is:

```text
note_path x gate_path
```

The current review system also partitions that edge by:

```text
model_partition
```

So the current freshness key is:

```text
note_path x gate_path x model_partition
```

`note_path` and `gate_path` are markdown endpoints. `gate_path` is the gate note path and identifies the gate; shorter labels are derived from it. `model_partition` is derivation-state metadata: one model's accepted review does not make another model's review fresh.

## Key Encoding

Every index path should be computable from the logical key.

Suggested keys:

```text
note_key  = n-<16 hex chars of sha256(note_path)>--<truncated note slug>
gate_key  = g-<16 hex chars of sha256(gate_path)>--<truncated gate slug>
model_key = normalized model_partition
```

The hash prevents path-length failures and keeps renames explicit. Each record stores the original `note_path`, `gate_path`, and `model_partition`; writers reject hash collisions.

For larger KBs, shard note keys:

```text
<note_key[0:2]>/<note_key>
```

At current scale this is not necessary for performance, but adding it now avoids a later path migration.

## Proposed Layout

Root:

```text
kb/reports/review-file-store/
```

This remains under `kb/reports/`, not a KB collection.

### Runs

One directory per prompt invocation:

```text
runs/
  004/
    review-run-4182/
      RUN.yaml
      prompt.md
      bundle-output.md
      debug.log
      telemetry.json
      pairs/
        prose__source-residue.md
        semantic__internal-consistency.md
```

`RUN.yaml` is the run manifest:

```yaml
schema: review-run-v1
review_run_id: 4182
runner: codex
model_partition: claude-opus-4-6
packing: note
started_at: "2026-06-24T07:40:00Z"
completed_at: "2026-06-24T07:44:00Z"
status: completed
pairs:
  - note_path: kb/notes/example.md
    note_key: n-2bf0d7e9adf0c633--example
    gate_path: kb/instructions/review-gates/prose/source-residue.md
    gate_key: g-91d955f3e3b1539e--source-residue
    model_partition: claude-opus-4-6
    pair_status: completed
    decision: warn
    reviewed_note_hash: abc123
    reviewed_note_commit: deadbeef
    gate_hash: def456
    result_path: pairs/prose__source-residue.md
```

At current scale this means 4,182 run directories. Sharding by thousands gives five parent directories; max observed pair files per run is 36.

### Pair Result Files

Each completed pair gets a markdown file with frontmatter for consumed metadata and body prose for inspection:

```yaml
---
schema: review-pair-v1
note_path: kb/notes/example.md
note_key: n-2bf0d7e9adf0c633--example
gate_path: kb/instructions/review-gates/prose/source-residue.md
gate_key: g-91d955f3e3b1539e--source-residue
model_partition: claude-opus-4-6
review_run_id: 4182
pair_status: completed
decision: warn
reviewed_note_hash: abc123
reviewed_note_commit: deadbeef
gate_hash: def456
reviewed_at: "2026-06-24T07:44:00Z"
---

### Findings
...
```

This makes rendered review artifacts self-describing even without the DB. At current scale, completed pairs are 9,034 files if every completed DB row is exported.

### Acceptance Events

Acceptance is append-only:

```text
events/
  acceptances/
    2026/
      06/
        20260624T074400Z-4182-prose__source-residue.yaml
```

Event file:

```yaml
schema: review-acceptance-event-v1
event_id: 20260624T074400Z-4182-prose__source-residue
note_path: kb/notes/example.md
note_key: n-2bf0d7e9adf0c633--example
gate_path: kb/instructions/review-gates/prose/source-residue.md
gate_key: g-91d955f3e3b1539e--source-residue
model_partition: claude-opus-4-6
accepted_review_pair_path: ../../../runs/004/review-run-4182/pairs/prose__source-residue.md
accepted_note_hash: abc123
accepted_note_commit: deadbeef
accepted_gate_hash: def456
accepted_at: "2026-06-24T07:44:00Z"
acceptance_kind: full-review
```

For trivial acks, `accepted_review_pair_path` is null and the event records the current note/gate content hashes.

At current scale this is 9,059 event files. Sharding by date or by event-id prefix keeps directory fan-out modest.

### Current Acceptance Indexes

The acceptance events are authoritative. Current indexes are generated files for fast selectors.

By note:

```text
current/
  by-note/
    claude-opus-4-6/
      n-2b/
        n-2bf0d7e9adf0c633--example/
          prose__source-residue.yaml
```

By gate:

```text
current/
  by-gate/
    claude-opus-4-6/
      prose__source-residue/
        n-2b/
          n-2bf0d7e9adf0c633--example.yaml
```

Each index entry points to the latest acceptance event and the effective review pair:

```yaml
schema: current-review-acceptance-v1
note_path: kb/notes/example.md
gate_path: kb/instructions/review-gates/prose/source-residue.md
model_partition: claude-opus-4-6
accepted_note_hash: abc123
accepted_gate_hash: def456
acceptance_event_path: ../../../../events/acceptances/2026/06/...
accepted_review_pair_path: ../../../../runs/004/review-run-4182/pairs/prose__source-residue.md
effective_review_pair_path: ../../../../runs/004/review-run-4182/pairs/prose__source-residue.md
decision: warn
```

Two indexes are deliberately duplicated:

- `by-note` answers "this note changed; which gates/models need recheck?"
- `by-gate` answers "this gate changed; which notes/models need recheck?"

At current scale, one index direction has 9,023 files. Keeping both directions means about 18,046 generated current-index files. With the proposed path shape:

- max leaf files for a note+model is 36;
- max leaf files for a gate+model is 176;
- top-level model count is 22 current acceptance models.

Those fan-outs are small on the current `ext4` filesystem and reasonable on modern filesystems generally.

### Latest Completed Pair Index

`warn-selector` needs accepted warning reviews. For ack events without an accepted pair, the current DB falls back to the latest completed review pair for the same `(note_path, gate_path, model_partition)` key. A file design should make that lookup explicit:

```text
latest-completed/
  by-edge/
    <model_key>/<note_key-prefix>/<note_key>/<gate_key>.yaml
```

This is generated from run manifests and pair files. It can be rebuilt and checked.

## Selector Behavior

### Missing Review

Given `(note_path, gate_path, model_partition)`:

1. compute `note_key`, `gate_key`, `model_key`;
2. check for `current/by-note/<model>/<note>/<gate>.yaml`;
3. absent file means `missing-review`.

This is direct path lookup.

### Note Changed

Given a changed note:

1. compute `note_key`;
2. enumerate `current/by-note/<model>/<note_key>/`;
3. compare each `accepted_note_hash` to the current note content hash.

Current max enumeration is 36 files for one note+model.

### Gate Changed

Given a changed gate:

1. compute `gate_key`;
2. enumerate `current/by-gate/<model>/<gate_key>/`;
3. compare each `accepted_gate_hash` to the current gate content hash.

Current max enumeration is 176 files for one gate+model.

### Warn/Fix Queue

Enumerate current index entries, filter `decision: warn`, and resolve `effective_review_pair_path` for readable findings. This is a file scan over about 9k current entries today. If that becomes too expensive, add a generated `current-warns/` index by model and note.

## Write Protocol

A pure file store needs a stricter write protocol than SQLite.

1. Acquire a single review-store writer lock.
2. Create run directory and `RUN.yaml` with pending pairs.
3. Write `prompt.md` and expected output path.
4. On ingest, write `bundle-output.md`, pair markdown files, telemetry/debug files, and update `RUN.yaml`.
5. Append one acceptance event file per completed accepted pair.
6. Rebuild affected current indexes by atomic temp-file + rename.
7. Release lock.

Crash recovery:

- If a run has pending pairs and no final status, mark it failed or rerun finalization.
- If acceptance events exist but current indexes are missing or stale, rebuild indexes from events.
- If pair files exist but `RUN.yaml` omits them, treat `RUN.yaml` as canonical and report orphan files.

Use atomic writes (`write temp`, `fsync` when needed, `rename`) for manifests and index entries. Without SQLite transactions, the explicit recovery path is part of the design.

## Directory Growth Projection

Projected current-data file counts:

| surface | projected files |
|---|---:|
| run manifests | 4,182 |
| prompt/raw/debug/telemetry files | up to about 16,728 if all retained separately |
| completed pair markdown files | 9,034 |
| acceptance event files | 9,059 |
| current by-note index files | 9,023 |
| current by-gate index files | 9,023 |
| latest-completed index files | up to 9,034 |

This is roughly 45k-65k files depending on how much run payload is split out. That is fine on ext4 if sharded. It is heavier than SQLite in inode count and directory churn, but still operationally plausible.

Storage estimate:

- pair rationale text is about 11.5 MB;
- raw bundle text is about 5.5 MB;
- debug logs are about 9.4 MB;
- telemetry is about 2.6 MB;
- YAML/frontmatter overhead for events and indexes could easily add 20-50 MB.

Expected total is comparable to the current 92 MB SQLite file plus existing report directories, but distributed across many files. The current SQLite file has about 46.5 MB of live pages and about half its pages on the freelist, so file size alone overstates the live DB payload.

## Tradeoffs

Advantages:

- Fully inspectable with ordinary tools.
- Git history can track event files if we choose to commit them.
- Direct keyed lookup works when filenames are computable.
- The structure is portable to generic artifact-lineage events.
- It demonstrates the "directory as index" idea without requiring SQLite.

Costs:

- No transaction boundary unless we implement locking and recovery carefully.
- Current indexes are duplicated generated truth and need rebuild/check commands.
- Relocation touches many files unless stable artifact IDs replace paths.
- Event ordering needs timestamp/ULID discipline.
- Many small files increase inode use and git churn if tracked.
- Querying arbitrary slices is worse than SQL unless we prebuild another directory index.

## Recommendation

Workshop decision after this analysis: keep SQLite for lineage state. A pure file store is feasible at current scale, but it recreates the same relational structure with weaker transaction and query support.

A pure file review store is feasible at current scale. The right design is not one prose file per review with hidden metadata; it is a filesystem-backed relational store:

- run directories for prompt invocations;
- pair markdown files for readable review bodies;
- append-only event files for acceptance;
- generated current indexes in both note and gate directions;
- generated latest-completed indexes for warn/fix queues.

It would likely work well for the current 10k-pair / 9k-event scale on ext4. It becomes less attractive if review volume grows by one or two orders of magnitude, if concurrent writers become common, or if selectors need ad-hoc relational queries beyond the prebuilt directory indexes. That is the point where SQLite stops being "extra infrastructure" and becomes the simpler implementation of the same relation. Commonplace should use that simpler implementation for lineage, while continuing to expose retained review/report content through markdown files.

## Open Questions

- Should acceptance events be committed, local-only, or gitignored alongside generated reports?
- Should the current indexes be committed or always generated?
- Should note identity be path-hash based, or should Commonplace introduce stable artifact IDs?
- Should review pair markdown frontmatter include model provenance even when DB/file indexes also store `model_partition`?
- Should `latest-completed` be a separate generated index or folded into current acceptance entries?
- Is a pure-file port valuable as production storage, or mainly as a design probe for future artifact-lineage stores?
