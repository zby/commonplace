-- SQLite schema for canonical review storage.
--
-- Notes and gate definitions remain file-backed. This database only stores
-- review outputs plus the currently accepted state used by selector and ack.
--
-- For now, gate freshness is keyed by the raw git blob SHA of the gate file.
-- That intentionally excludes any shared bundle instructions. If bundle-level
-- instructions later become freshness-relevant, this field should widen from
-- a leaf gate-file SHA to an effective review-contract SHA.
--
-- The current write path produces only per-gate reviews. There is no parent
-- review document or bundle-run table yet. If bundle generation is added
-- later, it should be introduced as an additive extension.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS gate_reviews (
    id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_id TEXT NOT NULL,
    model_id TEXT NOT NULL,
    decision TEXT NOT NULL CHECK (
        decision IN ('pass', 'fail', 'concern', 'error')
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
-- If bundle review generation is added later, the likely extension is:
--   - add review_runs(id, note_path, model_id, raw_markdown, ...)
--   - add nullable gate_reviews.review_run_id REFERENCES review_runs(id)
-- without changing the selector-facing acceptance view.
