-- SQLite schema for canonical review storage.
--
-- `review_runs` records one review invocation: one prompt/run directory.
-- `review_pairs` records each requested (note_path, gate_id) pair inside
-- that invocation. Freshness and selector state remain acceptance-driven and
-- gate-local.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS review_runs (
    review_run_id INTEGER PRIMARY KEY,
    model_id TEXT NOT NULL,
    runner TEXT NOT NULL,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (
        status IN ('running', 'completed', 'failed')
    ),
    failure_reason TEXT,
    telemetry_json TEXT,
    raw_bundle_markdown TEXT,
    debug_log TEXT,
    packing TEXT NOT NULL CHECK (
        packing IN ('note', 'gate')
    )
);

CREATE INDEX IF NOT EXISTS idx_review_runs_model_started
ON review_runs(model_id, started_at DESC);

CREATE INDEX IF NOT EXISTS idx_review_runs_status
ON review_runs(status);

CREATE TABLE IF NOT EXISTS review_pairs (
    review_pair_id INTEGER PRIMARY KEY,
    review_run_id INTEGER NOT NULL REFERENCES review_runs(review_run_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_id TEXT NOT NULL,
    model_id TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    pair_status TEXT NOT NULL CHECK (
        pair_status IN ('pending', 'completed', 'missing')
    ),
    decision TEXT CHECK (
        decision IN ('pass', 'warn', 'fail', 'error', 'unknown')
    ),
    rationale_markdown TEXT,
    evidence_json TEXT,
    gate_sha TEXT NOT NULL,
    reviewed_note_sha TEXT NOT NULL,
    reviewed_note_commit TEXT,
    reviewed_at TEXT,
    review_kind TEXT NOT NULL CHECK (
        review_kind IN ('full-review')
    ),
    UNIQUE (review_run_id, note_path, gate_id),
    UNIQUE (review_run_id, pair_ordinal)
);

CREATE INDEX IF NOT EXISTS idx_review_pairs_note_gate_model
ON review_pairs(note_path, gate_id, model_id);

CREATE INDEX IF NOT EXISTS idx_review_pairs_review_run_id
ON review_pairs(review_run_id);

CREATE INDEX IF NOT EXISTS idx_review_pairs_pair_status
ON review_pairs(pair_status);

CREATE INDEX IF NOT EXISTS idx_review_pairs_reviewed_sha
ON review_pairs(reviewed_note_sha);

CREATE TABLE IF NOT EXISTS acceptance_events (
    acceptance_event_id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_id TEXT NOT NULL,
    model_id TEXT NOT NULL,
    accepted_review_pair_id INTEGER REFERENCES review_pairs(review_pair_id) ON DELETE SET NULL,
    accepted_note_sha TEXT NOT NULL,
    accepted_note_commit TEXT,
    accepted_gate_sha TEXT NOT NULL,
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

CREATE INDEX IF NOT EXISTS idx_acceptance_events_note_gate_model
ON acceptance_events(note_path, gate_id, model_id, accepted_at DESC);

CREATE INDEX IF NOT EXISTS idx_acceptance_events_latest_by_key
ON acceptance_events(note_path, gate_id, model_id, acceptance_event_id DESC);

CREATE VIEW IF NOT EXISTS current_gate_acceptances AS
SELECT
    e.note_path,
    e.gate_id,
    e.model_id,
    e.accepted_review_pair_id,
    e.accepted_note_sha,
    e.accepted_note_commit,
    e.accepted_gate_sha,
    e.accepted_at,
    e.acceptance_kind
FROM acceptance_events AS e
JOIN (
    SELECT
        note_path,
        gate_id,
        model_id,
        MAX(acceptance_event_id) AS max_id
    FROM acceptance_events
    GROUP BY note_path, gate_id, model_id
) AS latest
  ON e.acceptance_event_id = latest.max_id;

CREATE VIEW IF NOT EXISTS stale_gate_pairs AS
SELECT
    a.note_path,
    a.gate_id,
    a.model_id,
    a.accepted_note_sha,
    a.accepted_gate_sha
FROM current_gate_acceptances AS a;

CREATE TABLE IF NOT EXISTS review_schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL
);

-- Query pattern expected for selector:
--
-- 1. resolve current note sha from git for candidate notes
-- 2. resolve current gate sha from gate files
-- 3. LEFT JOIN current_gate_acceptances view on (note_path, gate_id, model_id)
-- 4. classify:
--      no row                  -> missing-review
--      accepted_gate_sha != ?  -> gate-changed
--      accepted_note_sha != ?  -> note-changed
--      else fresh
