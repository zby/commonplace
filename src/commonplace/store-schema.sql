-- Commonplace operational store schema v1: general freshness + review execution.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS artifact_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    artifact_path TEXT NOT NULL CHECK (length(artifact_path) > 0),
    version_kind TEXT NOT NULL CHECK (version_kind IN ('file-text')),
    content_sha256 TEXT NOT NULL CHECK (
        length(content_sha256) = 64
        AND content_sha256 NOT GLOB '*[^0-9a-f]*'
    ),
    content_text TEXT NOT NULL,
    captured_at TEXT NOT NULL,
    UNIQUE (artifact_path, version_kind, content_sha256),
    UNIQUE (snapshot_id, artifact_path, version_kind)
);

CREATE TABLE IF NOT EXISTS freshness_baselines (
    target_id INTEGER PRIMARY KEY,
    target_kind TEXT NOT NULL CHECK (length(target_kind) > 0),
    target_key_json TEXT NOT NULL CHECK (length(target_key_json) > 0),
    revision INTEGER NOT NULL CHECK (revision >= 1),
    accepted_at TEXT NOT NULL,
    UNIQUE (target_kind, target_key_json)
);

CREATE TABLE IF NOT EXISTS freshness_target_generations (
    target_kind TEXT NOT NULL CHECK (length(target_kind) > 0),
    target_key_json TEXT NOT NULL CHECK (length(target_key_json) > 0),
    next_revision INTEGER NOT NULL CHECK (next_revision >= 1),
    PRIMARY KEY (target_kind, target_key_json)
);

CREATE TABLE IF NOT EXISTS freshness_inputs (
    target_id INTEGER NOT NULL
        REFERENCES freshness_baselines(target_id) ON DELETE CASCADE,
    input_role TEXT NOT NULL CHECK (length(input_role) > 0),
    artifact_path TEXT NOT NULL CHECK (length(artifact_path) > 0),
    version_kind TEXT NOT NULL CHECK (version_kind IN ('file-text')),
    accepted_snapshot_id INTEGER NOT NULL,
    PRIMARY KEY (target_id, input_role),
    UNIQUE (target_id, artifact_path, version_kind),
    FOREIGN KEY (accepted_snapshot_id, artifact_path, version_kind)
        REFERENCES artifact_snapshots(snapshot_id, artifact_path, version_kind)
);

CREATE INDEX IF NOT EXISTS idx_freshness_inputs_path
ON freshness_inputs(artifact_path, version_kind, target_id);

CREATE TABLE IF NOT EXISTS review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT,
    runner_model TEXT,
    runner_effort TEXT,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('queued', 'completed', 'failed')),
    failure_reason TEXT,
    telemetry_json TEXT,
    grouping TEXT NOT NULL CHECK (grouping IN ('note', 'criterion')),
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

CREATE TABLE IF NOT EXISTS review_pairs (
    review_pair_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    criterion_path TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    result_kind TEXT NOT NULL CHECK (result_kind IN ('verdict', 'report')),
    outcome TEXT CHECK (outcome IN ('pass', 'warn', 'fail')),
    reviewed_note_snapshot_id INTEGER REFERENCES artifact_snapshots(snapshot_id),
    reviewed_criterion_snapshot_id INTEGER REFERENCES artifact_snapshots(snapshot_id),
    expected_baseline_revision INTEGER CHECK (
        expected_baseline_revision IS NULL OR expected_baseline_revision >= 1
    ),
    expected_generation_next_revision INTEGER CHECK (
        expected_generation_next_revision IS NULL OR expected_generation_next_revision >= 1
    ),
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

CREATE TABLE IF NOT EXISTS review_freshness_evidence (
    target_id INTEGER PRIMARY KEY
        REFERENCES freshness_baselines(target_id) ON DELETE CASCADE,
    evidence_review_pair_id INTEGER NOT NULL UNIQUE
        REFERENCES review_pairs(review_pair_id)
);

CREATE VIEW IF NOT EXISTS current_review_freshness_baselines AS
SELECT
    json_extract(b.target_key_json, '$.note_path') AS note_path,
    json_extract(b.target_key_json, '$.criterion_path') AS criterion_path,
    json_extract(b.target_key_json, '$.model_partition') AS model_partition,
    e.evidence_review_pair_id,
    note_input.accepted_snapshot_id AS baseline_note_snapshot_id,
    criterion_input.accepted_snapshot_id AS baseline_criterion_snapshot_id,
    note_snapshot.content_sha256 AS baseline_note_hash,
    criterion_snapshot.content_sha256 AS baseline_criterion_hash,
    note_snapshot.content_text AS baseline_note_text,
    criterion_snapshot.content_text AS baseline_criterion_text,
    b.accepted_at AS baseline_updated_at,
    b.revision AS baseline_revision,
    rp.result_kind,
    rp.outcome
FROM freshness_baselines AS b
JOIN review_freshness_evidence AS e
  ON e.target_id = b.target_id
JOIN review_pairs AS rp
  ON rp.review_pair_id = e.evidence_review_pair_id
JOIN review_jobs AS j
  ON j.review_job_id = rp.review_job_id
 AND j.model_partition = json_extract(b.target_key_json, '$.model_partition')
JOIN freshness_inputs AS note_input
  ON note_input.target_id = b.target_id
 AND note_input.input_role = 'note'
JOIN freshness_inputs AS criterion_input
  ON criterion_input.target_id = b.target_id
 AND criterion_input.input_role = 'criterion'
JOIN artifact_snapshots AS note_snapshot
  ON note_snapshot.snapshot_id = note_input.accepted_snapshot_id
JOIN artifact_snapshots AS criterion_snapshot
  ON criterion_snapshot.snapshot_id = criterion_input.accepted_snapshot_id
WHERE b.target_kind = 'review-pair'
  AND j.status = 'completed'
  AND rp.completed_at IS NOT NULL
  AND (rp.result_kind = 'report' OR rp.outcome IS NOT NULL)
  AND rp.note_path = json_extract(b.target_key_json, '$.note_path')
  AND rp.criterion_path = json_extract(b.target_key_json, '$.criterion_path');