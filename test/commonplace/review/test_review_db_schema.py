from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sqlite3

import pytest

from commonplace.review import review_db
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


REPO_ROOT = Path(__file__).resolve().parents[3]

LEGACY_REVIEW_SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE review_runs (
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

CREATE INDEX idx_review_runs_model_partition_started
ON review_runs(model_partition, started_at DESC);

CREATE INDEX idx_review_runs_status
ON review_runs(status);

CREATE TABLE review_file_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    path TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    content_text TEXT,
    captured_at TEXT NOT NULL,
    UNIQUE (path, content_sha256)
);

CREATE TABLE review_pairs (
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
    UNIQUE (review_run_id, note_path, gate_path),
    UNIQUE (review_run_id, pair_ordinal)
);

CREATE INDEX idx_review_pairs_note_gate_model_partition
ON review_pairs(note_path, gate_path, model_partition);

CREATE INDEX idx_review_pairs_review_run_id
ON review_pairs(review_run_id);

CREATE INDEX idx_review_pairs_pair_status
ON review_pairs(pair_status);

CREATE TABLE acceptance_events (
    acceptance_event_id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    accepted_review_pair_id INTEGER REFERENCES review_pairs(review_pair_id) ON DELETE SET NULL,
    accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_at TEXT NOT NULL
);

CREATE INDEX idx_acceptance_events_note_gate_model_partition
ON acceptance_events(note_path, gate_path, model_partition, accepted_at DESC);

CREATE INDEX idx_acceptance_events_latest_by_key
ON acceptance_events(note_path, gate_path, model_partition, acceptance_event_id DESC);

CREATE VIEW current_gate_acceptances AS
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
    e.accepted_at
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

CREATE VIEW stale_gate_pairs AS
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
"""


def create_legacy_review_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(LEGACY_REVIEW_SCHEMA_SQL)
        conn.execute(
            """
            INSERT INTO review_runs (
                review_run_id,
                model_partition,
                runner,
                started_at,
                completed_at,
                status,
                packing
            ) VALUES (1, 'test-model', 'test-runner', '2026-04-10T10:01:00+00:00', NULL, 'running', 'note')
            """
        )
        conn.execute(
            """
            INSERT INTO review_pairs (
                review_pair_id,
                review_run_id,
                note_path,
                gate_path,
                model_partition,
                pair_ordinal,
                pair_status
            ) VALUES (
                10,
                1,
                'kb/notes/legacy.md',
                'kb/instructions/review-gates/prose/legacy.md',
                'test-model',
                0,
                'pending'
            )
            """
        )
        conn.execute(
            """
            INSERT INTO acceptance_events (
                acceptance_event_id,
                note_path,
                gate_path,
                model_partition,
                accepted_review_pair_id,
                accepted_at
            ) VALUES (
                20,
                'kb/notes/legacy.md',
                'kb/instructions/review-gates/prose/legacy.md',
                'test-model',
                10,
                '2026-04-10T10:02:00+00:00'
            )
            """
        )
        conn.commit()


def test_ensure_db_initializes_schema_that_can_store_current_acceptance(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        view_row = conn.execute(
            """
            SELECT
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/fresh.md'
            """
        ).fetchone()
        migration_table = conn.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'review_schema_migrations'
            """
        ).fetchone()
        user_version = conn.execute("PRAGMA user_version").fetchone()[0]
        job_columns = {row["name"]: row for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        pair_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_pairs)").fetchall()}
        index_names = {
            row["name"]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'index'"
            ).fetchall()
        }
        has_legacy_runs = conn.execute(
            """
            SELECT 1
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'review_runs'
            """
        ).fetchone()

    assert view_row is not None
    assert view_row["accepted_note_snapshot_id"] is None
    assert view_row["accepted_gate_snapshot_id"] is None
    assert view_row["accepted_note_hash"] is None
    assert view_row["accepted_gate_hash"] is None
    assert migration_table is None
    assert user_version == review_db.LATEST_REVIEW_SCHEMA_VERSION
    assert "created_at" in job_columns
    assert job_columns["started_at"]["notnull"] == 0
    assert job_columns["runner"]["notnull"] == 0
    assert "runner_model" in job_columns
    assert "runner_effort" in job_columns
    assert "prompt_path" in job_columns
    assert "model_partition" not in pair_columns
    assert "idx_review_pairs_note_gate" in index_names
    assert "idx_review_pairs_note_gate_model_partition" not in index_names
    assert has_legacy_runs is None


def test_ensure_db_migrates_legacy_user_version_zero_store(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    create_legacy_review_db(db_path)

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        user_version = conn.execute("PRAGMA user_version").fetchone()[0]
        job = conn.execute(
            """
            SELECT created_at, started_at, status, runner, runner_model, runner_effort, prompt_path
            FROM review_jobs
            WHERE review_job_id = 1
            """
        ).fetchone()
        pair_count = conn.execute("SELECT COUNT(*) FROM review_pairs").fetchone()[0]
        pair_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_pairs)").fetchall()}
        job_columns = {row["name"]: row for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        acceptance = conn.execute(
            """
            SELECT accepted_review_pair_id
            FROM acceptance_events
            WHERE acceptance_event_id = 20
            """
        ).fetchone()
        index_names = {
            row["name"]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'index'"
            ).fetchall()
        }
        foreign_key_violations = conn.execute("PRAGMA foreign_key_check").fetchall()
        has_legacy_runs = conn.execute(
            """
            SELECT 1
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'review_runs'
            """
        ).fetchone()

    assert user_version == review_db.LATEST_REVIEW_SCHEMA_VERSION
    assert dict(job) == {
        "created_at": "2026-04-10T10:01:00+00:00",
        "started_at": "2026-04-10T10:01:00+00:00",
        "status": "running",
        "runner": "test-runner",
        "runner_model": None,
        "runner_effort": None,
        "prompt_path": None,
    }
    assert pair_count == 1
    assert "review_job_id" in pair_columns
    assert "review_run_id" not in pair_columns
    assert "model_partition" not in pair_columns
    assert job_columns["runner"]["notnull"] == 0
    assert acceptance["accepted_review_pair_id"] == 10
    assert "idx_review_jobs_model_partition_created" in index_names
    assert "idx_review_runs_model_partition_started" not in index_names
    assert "idx_review_pairs_note_gate" in index_names
    assert "idx_review_pairs_note_gate_model_partition" not in index_names
    assert "idx_review_pairs_review_job_id" in index_names
    assert "idx_review_pairs_review_run_id" not in index_names
    assert foreign_key_violations == []
    assert has_legacy_runs is None


def test_failed_legacy_migration_rolls_back_and_leaves_old_tables_readable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    db_path = tmp_path / "review-store.sqlite"
    create_legacy_review_db(db_path)
    monkeypatch.setattr(
        review_db,
        "EXPECTED_REVIEW_INDEXES",
        review_db.EXPECTED_REVIEW_INDEXES | {"idx_missing_for_rollback_test"},
    )

    with pytest.raises(RuntimeError, match="missing indexes"):
        review_db.ensure_db(db_path)

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        migrated_job = conn.execute(
            """
            SELECT created_at, started_at, status
            FROM review_jobs
            WHERE review_job_id = 1
            """
        ).fetchone()
        job_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        pair_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_pairs)").fetchall()}
        pair_count = conn.execute("SELECT COUNT(*) FROM review_pairs").fetchone()[0]
        user_version = conn.execute("PRAGMA user_version").fetchone()[0]

    assert dict(migrated_job) == {
        "created_at": "2026-04-10T10:01:00+00:00",
        "started_at": "2026-04-10T10:01:00+00:00",
        "status": "running",
    }
    assert "created_at" in job_columns
    assert "runner_model" not in job_columns
    assert "model_partition" in pair_columns
    assert pair_count == 1
    assert user_version == 2


def test_snapshot_file_deduplicates_per_path_and_hashes_exact_utf8(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    gate = repo / "kb" / "instructions" / "review-gates" / "prose" / "sample.md"
    note.parent.mkdir(parents=True)
    gate.parent.mkdir(parents=True)
    note.write_text("title\n\ncafe\u0301\n", encoding="utf-8")
    gate.write_text("title\n\ncafe\u0301\n", encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        first = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        second = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )

    assert first.snapshot_id == second.snapshot_id
    assert first.path == "kb/notes/sample.md"
    assert first.content_text == "title\n\ncafe\u0301\n"
    assert first.content_sha256 == sha256("title\n\ncafe\u0301\n".encode("utf-8")).hexdigest()
    assert gate_snapshot.snapshot_id != first.snapshot_id
    assert gate_snapshot.content_sha256 == first.content_sha256


def test_load_review_job_exposes_created_at_and_nullable_started_at(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="live-agent",
            created_at="2026-04-10T10:03:00+02:00",
            started_at=None,
            status="queued",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/pending.md",
                    gate_path="kb/instructions/review-gates/prose/pending.md",
                    pair_ordinal=0,
                )
            ],
        )
        review_job = review_db.load_review_job(conn, review_job_id=review_job_id)

    assert review_job is not None
    assert review_job.created_at == "2026-04-10T10:03:00+02:00"
    assert review_job.started_at is None
    assert review_job.status == "queued"


def test_snapshot_file_rehydrates_hash_only_snapshot_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    note.parent.mkdir(parents=True)
    note.write_text("rehydrate me\n", encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        first = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        conn.execute(
            "UPDATE review_file_snapshots SET content_text = NULL WHERE snapshot_id = ?",
            (first.snapshot_id,),
        )
        second = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        stored_text = conn.execute(
            "SELECT content_text FROM review_file_snapshots WHERE snapshot_id = ?",
            (first.snapshot_id,),
        ).fetchone()[0]

    assert second.snapshot_id == first.snapshot_id
    assert second.content_text == "rehydrate me\n"
    assert stored_text == "rehydrate me\n"


def test_prune_obsolete_snapshot_content_keeps_current_and_pending_text(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    files = {
        "kb/notes/old.md": "old note\n",
        "kb/instructions/review-gates/prose/old.md": "old gate\n",
        "kb/notes/current.md": "current note\n",
        "kb/instructions/review-gates/prose/current.md": "current gate\n",
        "kb/notes/pending.md": "pending note\n",
        "kb/instructions/review-gates/prose/pending.md": "pending gate\n",
    }
    for rel_path, content in files.items():
        path = repo / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        old_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/old.md")
        old_gate = review_db.snapshot_file(conn, repo_root=repo, path="kb/instructions/review-gates/prose/old.md")
        current_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/current.md")
        current_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/current.md",
        )
        pending_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/pending.md")
        pending_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/pending.md",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/current.md",
            gate_path="kb/instructions/review-gates/prose/current.md",
            model_partition="opus-4-6",
            accepted_review_pair_id=None,
            accepted_note_snapshot_id=current_note.snapshot_id,
            accepted_gate_snapshot_id=current_gate.snapshot_id,
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="test-runner",
            created_at="2026-04-10T10:03:00+02:00",
            started_at="2026-04-10T10:03:00+02:00",
            status="running",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/pending.md",
                    gate_path="kb/instructions/review-gates/prose/pending.md",
                    pair_ordinal=0,
                    reviewed_note_snapshot_id=pending_note.snapshot_id,
                    reviewed_gate_snapshot_id=pending_gate.snapshot_id,
                )
            ],
        )
        pruned = review_db.prune_obsolete_snapshot_content(conn)
        rows = {
            int(row["snapshot_id"]): row["content_text"]
            for row in conn.execute(
                "SELECT snapshot_id, content_text FROM review_file_snapshots"
            ).fetchall()
        }

    assert pruned == 2
    assert rows[old_note.snapshot_id] is None
    assert rows[old_gate.snapshot_id] is None
    assert rows[current_note.snapshot_id] == "current note\n"
    assert rows[current_gate.snapshot_id] == "current gate\n"
    assert rows[pending_note.snapshot_id] == "pending note\n"
    assert rows[pending_gate.snapshot_id] == "pending gate\n"


def test_current_acceptance_view_exposes_snapshot_hashes(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    gate = repo / "kb" / "instructions" / "review-gates" / "prose" / "sample.md"
    note.parent.mkdir(parents=True)
    gate.parent.mkdir(parents=True)
    note.write_text("note text\n", encoding="utf-8")
    gate.write_text("gate text\n", encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        acceptance_event_id = accept_pair(
            conn,
            review_pair_id=None,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        conn.execute(
            """
            UPDATE acceptance_events
            SET accepted_note_snapshot_id = ?,
                accepted_gate_snapshot_id = ?
            WHERE acceptance_event_id = ?
            """,
            (note_snapshot.snapshot_id, gate_snapshot.snapshot_id, acceptance_event_id),
        )
        view_row = conn.execute(
            """
            SELECT
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/sample.md'
            """
        ).fetchone()

    assert view_row["accepted_note_snapshot_id"] == note_snapshot.snapshot_id
    assert view_row["accepted_gate_snapshot_id"] == gate_snapshot.snapshot_id
    assert view_row["accepted_note_hash"] == note_snapshot.content_sha256
    assert view_row["accepted_gate_hash"] == gate_snapshot.content_sha256


def test_snapshot_file_rejects_non_repo_relative_paths(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        with pytest.raises(ValueError, match="repo-relative"):
            review_db.snapshot_file(conn, repo_root=repo, path="../outside.md")
