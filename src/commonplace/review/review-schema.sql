-- SQLite schema for canonical review storage.
--
-- `review_runs` records one review invocation: one prompt/run directory.
-- `review_pairs` records each requested (note_path, gate_path) pair inside
-- that invocation. Freshness and selector state remain acceptance-driven and
-- gate-local.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS review_runs (
    review_run_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT NOT NULL,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (
        status IN ('running', 'completed', 'failed')
    ),
    failure_reason TEXT,
    telemetry_json TEXT,
    bundle_output_path TEXT,
    packing TEXT NOT NULL CHECK (
        packing IN ('note', 'gate')
    )
);

CREATE INDEX IF NOT EXISTS idx_review_runs_model_partition_started
ON review_runs(model_partition, started_at DESC);

CREATE INDEX IF NOT EXISTS idx_review_runs_status
ON review_runs(status);

CREATE TABLE IF NOT EXISTS review_file_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    path TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    content_text TEXT,
    captured_at TEXT NOT NULL,
    UNIQUE (path, content_sha256)
);

CREATE TABLE IF NOT EXISTS review_pairs (
    review_pair_id INTEGER PRIMARY KEY,
    review_run_id INTEGER NOT NULL REFERENCES review_runs(review_run_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    pair_status TEXT NOT NULL CHECK (
        pair_status IN ('pending', 'completed', 'missing')
    ),
    decision TEXT CHECK (
        decision IN ('pass', 'warn', 'fail', 'error', 'unknown')
    ),
    result_path TEXT,
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_at TEXT,
    review_kind TEXT NOT NULL CHECK (
        review_kind IN ('full-review')
    ),
    UNIQUE (review_run_id, note_path, gate_path),
    UNIQUE (review_run_id, pair_ordinal)
);

CREATE INDEX IF NOT EXISTS idx_review_pairs_note_gate_model_partition
ON review_pairs(note_path, gate_path, model_partition);

CREATE INDEX IF NOT EXISTS idx_review_pairs_review_run_id
ON review_pairs(review_run_id);

CREATE INDEX IF NOT EXISTS idx_review_pairs_pair_status
ON review_pairs(pair_status);

CREATE TABLE IF NOT EXISTS acceptance_events (
    acceptance_event_id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    accepted_review_pair_id INTEGER REFERENCES review_pairs(review_pair_id) ON DELETE SET NULL,
    accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_at TEXT NOT NULL,
    acceptance_kind TEXT NOT NULL CHECK (
        acceptance_kind IN (
            'full-review',
            'gate-migration',
            'trivial-change-ack',
            'migration-import',
            'manual-override'
        )
    )
);

CREATE INDEX IF NOT EXISTS idx_acceptance_events_note_gate_model_partition
ON acceptance_events(note_path, gate_path, model_partition, accepted_at DESC);

CREATE INDEX IF NOT EXISTS idx_acceptance_events_latest_by_key
ON acceptance_events(note_path, gate_path, model_partition, acceptance_event_id DESC);

CREATE VIEW IF NOT EXISTS current_gate_acceptances AS
SELECT
    e.note_path,
    e.gate_path,
    e.model_partition,
    e.accepted_review_pair_id,
    e.accepted_note_snapshot_id,
    e.accepted_gate_snapshot_id,
    note_snapshot.content_sha256 AS accepted_note_hash,
    gate_snapshot.content_sha256 AS accepted_gate_hash,
    note_snapshot.content_text AS accepted_note_text,
    gate_snapshot.content_text AS accepted_gate_text,
    e.accepted_at,
    e.acceptance_kind
FROM acceptance_events AS e
LEFT JOIN review_file_snapshots AS note_snapshot
  ON e.accepted_note_snapshot_id = note_snapshot.snapshot_id
LEFT JOIN review_file_snapshots AS gate_snapshot
  ON e.accepted_gate_snapshot_id = gate_snapshot.snapshot_id
JOIN (
    SELECT
        note_path,
        gate_path,
        model_partition,
        MAX(acceptance_event_id) AS max_id
    FROM acceptance_events
    GROUP BY note_path, gate_path, model_partition
) AS latest
  ON e.acceptance_event_id = latest.max_id;

CREATE VIEW IF NOT EXISTS stale_gate_pairs AS
SELECT
    a.note_path,
    a.gate_path,
    a.model_partition,
    a.accepted_note_snapshot_id,
    a.accepted_gate_snapshot_id,
    a.accepted_note_hash,
    a.accepted_gate_hash,
    a.accepted_note_text,
    a.accepted_gate_text
FROM current_gate_acceptances AS a;

CREATE TABLE IF NOT EXISTS review_schema_migrations (
    migration_name TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL
);

-- Query pattern expected for selector:
--
-- 1. resolve current note SHA-256 from candidate note files
-- 2. resolve current gate SHA-256 from gate files
-- 3. LEFT JOIN current_gate_acceptances view on (note_path, gate_path, model_partition)
-- 4. classify:
--      no row                  -> missing-review
--      accepted snapshots null -> missing-review
--      accepted_gate_hash != ? -> gate-changed
--      accepted_note_hash != ? -> note-changed
--      else fresh
