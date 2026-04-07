-- SQLite schema for canonical review storage.
--
-- Notes and gate definitions remain file-backed. This database only stores
-- review outputs plus the currently accepted state used by selector and ack.
--
-- For now, gate freshness is keyed by the raw git blob SHA of the gate file.
-- There is no separate bundle manifest hash in the current tree. If
-- bundle-level manifests later become freshness-relevant, this field should
-- widen from a leaf gate-file SHA to an effective review-contract SHA.
--
-- Review execution is bundle-shaped even though freshness remains gate-local.
-- `review_runs` records one review invocation; `review_run_gates` records the
-- requested gate set captured at run start; `gate_reviews` records actual
-- per-gate outcomes.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS review_runs (
    id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    model_id TEXT NOT NULL,
    runner TEXT NOT NULL,
    reviewed_note_sha TEXT NOT NULL,
    reviewed_note_commit TEXT,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (
        status IN ('running', 'completed', 'failed')
    ),
    failure_reason TEXT,
    telemetry_json TEXT,
    raw_bundle_markdown TEXT,
    debug_log TEXT
);

CREATE INDEX IF NOT EXISTS idx_review_runs_note_model_started
ON review_runs(note_path, model_id, started_at DESC);

CREATE TABLE IF NOT EXISTS review_run_gates (
    review_run_id INTEGER NOT NULL REFERENCES review_runs(id) ON DELETE CASCADE,
    gate_id TEXT NOT NULL,
    gate_sha TEXT NOT NULL,
    ordinal INTEGER NOT NULL,
    PRIMARY KEY (review_run_id, gate_id)
);

CREATE INDEX IF NOT EXISTS idx_review_run_gates_run_ordinal
ON review_run_gates(review_run_id, ordinal);

CREATE TABLE IF NOT EXISTS gate_reviews (
    id INTEGER PRIMARY KEY,
    review_run_id INTEGER REFERENCES review_runs(id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_id TEXT NOT NULL,
    model_id TEXT NOT NULL,
    decision TEXT NOT NULL CHECK (
        decision IN ('pass', 'warn', 'fail', 'error', 'unknown')
    ),
    rationale_markdown TEXT NOT NULL,
    evidence_json TEXT,
    gate_sha TEXT NOT NULL,
    reviewed_note_sha TEXT NOT NULL,
    reviewed_note_commit TEXT,
    reviewed_at TEXT NOT NULL,
    review_kind TEXT NOT NULL CHECK (
        review_kind IN ('full-review', 'manual-import')
    )
);

CREATE INDEX IF NOT EXISTS idx_gate_reviews_note_gate_model
ON gate_reviews(note_path, gate_id, model_id);

CREATE INDEX IF NOT EXISTS idx_gate_reviews_reviewed_sha
ON gate_reviews(reviewed_note_sha);

CREATE INDEX IF NOT EXISTS idx_gate_reviews_reviewed_at
ON gate_reviews(reviewed_at);

CREATE TABLE IF NOT EXISTS acceptance_events (
    id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_id TEXT NOT NULL,
    model_id TEXT NOT NULL,
    accepted_review_id INTEGER REFERENCES gate_reviews(id) ON DELETE SET NULL,
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
ON acceptance_events(note_path, gate_id, model_id, id DESC);

CREATE VIEW IF NOT EXISTS current_gate_acceptances AS
SELECT
    e.note_path,
    e.gate_id,
    e.model_id,
    e.accepted_review_id,
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
        MAX(id) AS max_id
    FROM acceptance_events
    GROUP BY note_path, gate_id, model_id
) AS latest
  ON e.id = latest.max_id;

CREATE VIEW IF NOT EXISTS stale_gate_pairs AS
SELECT
    a.note_path,
    a.gate_id,
    a.model_id,
    a.accepted_note_sha,
    a.accepted_gate_sha
FROM current_gate_acceptances AS a;

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
--
-- `review_runs` and `review_run_gates` model execution history. Selector state
-- remains acceptance-driven and gate-local.
