from __future__ import annotations

import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.review.review_db import connect


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "src/commonplace/review/review-schema.sql"


def _write_v7_source(
    *,
    source_path: Path,
    repo_root: Path,
    stale_pair_job_id: int,
) -> tuple[str, str]:
    note_path = "kb/notes/example.md"
    other_note_path = "kb/notes/other.md"
    criterion_path = "kb/instructions/review-gates/prose/source-residue.md"
    note_text = "# Example\n"
    other_note_text = "# Other\n"
    gate_text = "# Gate\n"
    stale_note_text = "# stale\n"
    note_hash = content_sha256_for_text(note_text)
    other_note_hash = content_sha256_for_text(other_note_text)
    gate_hash = content_sha256_for_text(gate_text)
    stale_note_hash = content_sha256_for_text(stale_note_text)
    (repo_root / note_path).parent.mkdir(parents=True, exist_ok=True)
    (repo_root / criterion_path).parent.mkdir(parents=True, exist_ok=True)
    (repo_root / note_path).write_text(note_text, encoding="utf-8")
    (repo_root / other_note_path).write_text(other_note_text, encoding="utf-8")
    (repo_root / criterion_path).write_text(gate_text, encoding="utf-8")

    with sqlite3.connect(source_path) as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        conn.execute("PRAGMA user_version = 7")
        conn.execute(
            """
            INSERT INTO review_file_snapshots (
                snapshot_id, path, content_sha256, content_text, captured_at
            ) VALUES
                (1, ?, ?, ?, '2026-07-13T00:00:00+00:00'),
                (2, ?, ?, ?, '2026-07-13T00:00:00+00:00'),
                (3, ?, ?, ?, '2026-07-13T00:00:00+00:00'),
                (4, ?, ?, ?, '2026-07-13T00:00:00+00:00')
            """,
            (
                note_path,
                note_hash,
                note_text,
                criterion_path,
                gate_hash,
                gate_text,
                other_note_path,
                stale_note_hash,
                stale_note_text,
                other_note_path,
                other_note_hash,
                other_note_text,
            ),
        )
        conn.execute(
            """
            INSERT INTO review_jobs (
                review_job_id, model_partition, created_at, status, grouping, completed_at
            ) VALUES
                (1, 'codex', '2026-07-13T00:00:00+00:00', 'completed', 'note', '2026-07-13T00:00:00+00:00'),
                (?, 'codex', '2026-07-13T01:00:00+00:00', 'queued', 'note', NULL)
            """,
            (stale_pair_job_id,),
        )
        conn.execute(
            """
            INSERT INTO review_pairs (
                review_pair_id, review_job_id, note_path, criterion_path,
                pair_ordinal, result_kind, outcome,
                reviewed_note_snapshot_id, reviewed_criterion_snapshot_id,
                completed_at
            ) VALUES
                (20, 1, ?, ?, 1, 'verdict', 'pass', 1, 2, '2026-07-13T00:00:00+00:00'),
                (21, 1, ?, ?, 2, 'verdict', 'pass', 4, 2, '2026-07-13T00:00:00+00:00'),
                (10, ?, ?, ?, 1, 'verdict', NULL, 1, 2, NULL),
                (11, ?, ?, ?, 2, 'verdict', NULL, 3, 2, NULL)
            """,
            (
                note_path,
                criterion_path,
                other_note_path,
                criterion_path,
                stale_pair_job_id,
                note_path,
                criterion_path,
                stale_pair_job_id,
                other_note_path,
                criterion_path,
            ),
        )
        conn.execute(
            """
            INSERT INTO freshness_baselines (
                note_path, criterion_path, model_partition,
                evidence_review_pair_id,
                baseline_note_snapshot_id,
                baseline_criterion_snapshot_id,
                baseline_updated_at
            ) VALUES
                (?, ?, 'codex', 20, 1, 2, '2026-07-13T00:00:00+00:00'),
                (?, ?, 'codex', 21, 4, 2, '2026-07-13T00:00:00+00:00')
            """,
            (note_path, criterion_path, other_note_path, criterion_path),
        )
        conn.commit()
    return note_path, other_note_path


def test_migration_removes_only_stale_queued_pairs(tmp_path: Path) -> None:
    if not SCHEMA_PATH.is_file():
        pytest.skip("legacy review schema fixture not present")

    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    source = tmp_path / "review-store.sqlite"
    destination = tmp_path / "commonplace-store.sqlite"
    note_path, other_note_path = _write_v7_source(
        source_path=source,
        repo_root=repo_root,
        stale_pair_job_id=49,
    )

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts/migrate-review-db-v7-to-commonplace-store.py"),
            "--repo-root",
            str(repo_root),
            "--source",
            str(source),
            "--destination",
            str(destination),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr

    with connect(destination) as conn:
        job = conn.execute(
            "SELECT status, failure_reason FROM review_jobs WHERE review_job_id = 49"
        ).fetchone()
        pair_count = conn.execute(
            "SELECT count(*) FROM review_pairs WHERE review_job_id = 49"
        ).fetchone()[0]
        remaining_pairs = conn.execute(
            """
            SELECT note_path, reviewed_note_snapshot_id
            FROM review_pairs
            WHERE review_job_id = 49
            ORDER BY pair_ordinal
            """
        ).fetchall()
        other_baseline = conn.execute(
            """
            SELECT note_path
            FROM current_review_freshness_baselines
            WHERE note_path = ?
            """,
            (other_note_path,),
        ).fetchone()

    assert job["status"] == "queued"
    assert job["failure_reason"] is None
    assert pair_count == 1
    assert len(remaining_pairs) == 1
    assert remaining_pairs[0]["note_path"] == note_path
    assert int(remaining_pairs[0]["reviewed_note_snapshot_id"]) == 1
    assert other_baseline is not None