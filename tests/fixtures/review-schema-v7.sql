-- SQLite schema for legacy review-store v7 (migration test fixture).
--
-- `review_jobs` records one review invocation: one prompt/job directory.
-- `review_pairs` records each requested (note_path, criterion_path) pair inside
-- that invocation. `criterion_path` names the criterion side, including
-- report assays. Freshness remains baseline-driven and criterion-local; pair
-- completion depends on result_kind, not outcome alone.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    -- Execution adapter/medium, nullable until a queued job is claimed or run.
    runner TEXT,
    -- Concrete runner execution provenance, nullable until known.
    runner_model TEXT,
    runner_effort TEXT,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (
        status IN ('queued', 'completed', 'failed')
    ),
    failure_reason TEXT,
    telemetry_json TEXT,
    grouping TEXT NOT NULL CHECK (
        grouping IN ('note', 'criterion')
    ),
    CHECK (
        (status = 'queued' AND completed_at IS NULL AND failure_reason IS NULL)
        OR (status = 'completed' AND completed_at IS NOT NULL AND failure_reason IS NULL)
        OR (status = 'failed' AND completed_at IS NOT NULL AND failure_reason IS NOT NULL)
    )
);

CREATE INDEX IF NOT EXISTS idx_review_jobs_model_partition_created
ON review_jobs(model_partition, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_review_jobs_status
ON review_jobs(status);

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
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    criterion_path TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    result_kind TEXT NOT NULL CHECK (
        result_kind IN ('verdict', 'report')
    ),
    outcome TEXT CHECK (
        outcome IN ('pass', 'warn', 'fail')
    ),
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_criterion_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    completed_at TEXT,
    CHECK (
        (completed_at IS NULL AND outcome IS NULL)
        OR (
            completed_at IS NOT NULL
            AND (
                (result_kind = 'verdict' AND outcome IS NOT NULL)
                OR (result_kind = 'report' AND outcome IS NULL)
            )
        )
    ),
    UNIQUE (review_job_id, note_path, criterion_path),
    UNIQUE (review_job_id, pair_ordinal)
);

CREATE INDEX IF NOT EXISTS idx_review_pairs_note_criterion
ON review_pairs(note_path, criterion_path);

CREATE INDEX IF NOT EXISTS idx_review_pairs_review_job_id
ON review_pairs(review_job_id);

CREATE TABLE IF NOT EXISTS freshness_baselines (
    note_path TEXT NOT NULL,
    criterion_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    evidence_review_pair_id INTEGER NOT NULL REFERENCES review_pairs(review_pair_id),
    baseline_note_snapshot_id INTEGER NOT NULL REFERENCES review_file_snapshots(snapshot_id),
    baseline_criterion_snapshot_id INTEGER NOT NULL REFERENCES review_file_snapshots(snapshot_id),
    baseline_updated_at TEXT NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_freshness_baselines_note_criterion_model_partition
ON freshness_baselines(note_path, criterion_path, model_partition);

CREATE VIEW IF NOT EXISTS current_freshness_baselines AS
SELECT
    e.note_path,
    e.criterion_path,
    e.model_partition,
    e.evidence_review_pair_id,
    e.baseline_note_snapshot_id,
    e.baseline_criterion_snapshot_id,
    note_snapshot.content_sha256 AS baseline_note_hash,
    criterion_snapshot.content_sha256 AS baseline_criterion_hash,
    note_snapshot.content_text AS baseline_note_text,
    criterion_snapshot.content_text AS baseline_criterion_text,
    e.baseline_updated_at,
    rp.result_kind,
    rp.outcome
FROM freshness_baselines AS e
JOIN review_pairs AS rp
  ON rp.review_pair_id = e.evidence_review_pair_id
 AND rp.note_path = e.note_path
 AND rp.criterion_path = e.criterion_path
JOIN review_jobs AS j
  ON j.review_job_id = rp.review_job_id
 AND j.model_partition = e.model_partition
LEFT JOIN review_file_snapshots AS note_snapshot
  ON e.baseline_note_snapshot_id = note_snapshot.snapshot_id
LEFT JOIN review_file_snapshots AS criterion_snapshot
  ON e.baseline_criterion_snapshot_id = criterion_snapshot.snapshot_id
WHERE j.status = 'completed'
  AND rp.completed_at IS NOT NULL
  AND (rp.result_kind = 'report' OR rp.outcome IS NOT NULL);